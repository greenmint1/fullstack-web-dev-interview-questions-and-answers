# Progressive Web Apps & Service Workers Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 interview questions and answers about Progressive Web Apps (PWAs) and service workers: 150 easy, 150 moderate and 150 advanced. The answers follow the current Web App Manifest, Service Worker, Cache, Push and Notifications specs as they work in today's Chrome, Edge, Safari and Firefox, and Workbox 7 for the library examples. Browser support for some PWA features still differs a lot, so the answers point out where that matters.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a Progressive Web App?](#1-what-is-a-progressive-web-app)
- [2: Why is it called "progressive"?](#2-why-is-it-called-progressive)
- [3: What are the main building blocks of a PWA?](#3-what-are-the-main-building-blocks-of-a-pwa)
- [4: What is a service worker?](#4-what-is-a-service-worker)
- [5: How is a service worker different from a regular script on the page?](#5-how-is-a-service-worker-different-from-a-regular-script-on-the-page)
- [6: How is a service worker different from a Web Worker?](#6-how-is-a-service-worker-different-from-a-web-worker)
- [7: How do you register a service worker?](#7-how-do-you-register-a-service-worker)
- [8: Why do service workers need HTTPS?](#8-why-do-service-workers-need-https)
- [9: What is a web app manifest?](#9-what-is-a-web-app-manifest)
- [10: What does a basic manifest file look like?](#10-what-does-a-basic-manifest-file-look-like)
- [11: What file extension should a manifest have?](#11-what-file-extension-should-a-manifest-have)
- [12: What is the difference between name and short_name in the manifest?](#12-what-is-the-difference-between-name-and-short_name-in-the-manifest)
- [13: What does start_url do?](#13-what-does-start_url-do)
- [14: What are the display modes in a manifest?](#14-what-are-the-display-modes-in-a-manifest)
- [15: What is theme_color used for?](#15-what-is-theme_color-used-for)
- [16: What is background_color used for?](#16-what-is-background_color-used-for)
- [17: Why do you need several icon sizes in the manifest?](#17-why-do-you-need-several-icon-sizes-in-the-manifest)
- [18: What is a maskable icon?](#18-what-is-a-maskable-icon)
- [19: What does "installable" mean for a PWA?](#19-what-does-installable-mean-for-a-pwa)
- [20: How does a user install a PWA?](#20-how-does-a-user-install-a-pwa)
- [21: What is the scope of a service worker?](#21-what-is-the-scope-of-a-service-worker)
- [22: Why do people usually put sw.js in the root of the site?](#22-why-do-people-usually-put-swjs-in-the-root-of-the-site)
- [23: What is the service worker lifecycle?](#23-what-is-the-service-worker-lifecycle)
- [24: What happens in the install event?](#24-what-happens-in-the-install-event)
- [25: What happens in the activate event?](#25-what-happens-in-the-activate-event)
- [26: What does event.waitUntil do?](#26-what-does-eventwaituntil-do)
- [27: What is the fetch event?](#27-what-is-the-fetch-event)
- [28: What does event.respondWith do?](#28-what-does-eventrespondwith-do)
- [29: What is the Cache API?](#29-what-is-the-cache-api)
- [30: Is the Cache API the same as the HTTP cache?](#30-is-the-cache-api-the-same-as-the-http-cache)
- [31: What is the difference between caches.open and caches.match?](#31-what-is-the-difference-between-cachesopen-and-cachesmatch)
- [32: What is the difference between cache.add, cache.addAll and cache.put?](#32-what-is-the-difference-between-cacheadd-cacheaddall-and-cacheput)
- [33: What is the app shell model?](#33-what-is-the-app-shell-model)
- [34: What does "offline first" mean?](#34-what-does-offline-first-mean)
- [35: How do you show an offline page when there is no network?](#35-how-do-you-show-an-offline-page-when-there-is-no-network)
- [36: What is the cache first strategy?](#36-what-is-the-cache-first-strategy)
- [37: What is the network first strategy?](#37-what-is-the-network-first-strategy)
- [38: What is the stale-while-revalidate strategy?](#38-what-is-the-stale-while-revalidate-strategy)
- [39: What are the network only and cache only strategies?](#39-what-are-the-network-only-and-cache-only-strategies)
- [40: Why do you need to clone a response before caching it?](#40-why-do-you-need-to-clone-a-response-before-caching-it)
- [41: What are the main events a service worker can listen to?](#41-what-are-the-main-events-a-service-worker-can-listen-to)
- [42: Can a service worker access the DOM?](#42-can-a-service-worker-access-the-dom)
- [43: What is self inside a service worker?](#43-what-is-self-inside-a-service-worker)
- [44: Can you use localStorage in a service worker?](#44-can-you-use-localstorage-in-a-service-worker)
- [45: How do you check if a page is controlled by a service worker?](#45-how-do-you-check-if-a-page-is-controlled-by-a-service-worker)
- [46: Why doesn't the service worker control the page on the first visit?](#46-why-doesnt-the-service-worker-control-the-page-on-the-first-visit)
- [47: What does navigator.serviceWorker.ready return?](#47-what-does-navigatorserviceworkerready-return)
- [48: How do you unregister a service worker?](#48-how-do-you-unregister-a-service-worker)
- [49: How can you see your service worker in Chrome DevTools?](#49-how-can-you-see-your-service-worker-in-chrome-devtools)
- [50: Can a service worker run when no tab of the site is open?](#50-can-a-service-worker-run-when-no-tab-of-the-site-is-open)
- [51: What are the main benefits of a PWA?](#51-what-are-the-main-benefits-of-a-pwa)
- [52: What are the main limitations of PWAs?](#52-what-are-the-main-limitations-of-pwas)
- [53: What is the difference between a PWA and a native app?](#53-what-is-the-difference-between-a-pwa-and-a-native-app)
- [54: What is the difference between a PWA and a single page application?](#54-what-is-the-difference-between-a-pwa-and-a-single-page-application)
- [55: Does a PWA have to be a single page application?](#55-does-a-pwa-have-to-be-a-single-page-application)
- [56: How do you know if the app is running as an installed PWA?](#56-how-do-you-know-if-the-app-is-running-as-an-installed-pwa)
- [57: What is the beforeinstallprompt event?](#57-what-is-the-beforeinstallprompt-event)
- [58: How do you show a custom install button?](#58-how-do-you-show-a-custom-install-button)
- [59: What is the appinstalled event?](#59-what-is-the-appinstalled-event)
- [60: How do you install a PWA on iPhone?](#60-how-do-you-install-a-pwa-on-iphone)
- [61: What is apple-touch-icon?](#61-what-is-apple-touch-icon)
- [62: Can PWAs send push notifications on iOS?](#62-can-pwas-send-push-notifications-on-ios)
- [63: What is the Push API?](#63-what-is-the-push-api)
- [64: What is the Notifications API?](#64-what-is-the-notifications-api)
- [65: How do you ask the user for notification permission?](#65-how-do-you-ask-the-user-for-notification-permission)
- [66: Why shouldn't you ask for notification permission on page load?](#66-why-shouldnt-you-ask-for-notification-permission-on-page-load)
- [67: What happens when the user clicks a notification?](#67-what-happens-when-the-user-clicks-a-notification)
- [68: What is IndexedDB and why is it used in PWAs?](#68-what-is-indexeddb-and-why-is-it-used-in-pwas)
- [69: What is the idb library?](#69-what-is-the-idb-library)
- [70: How do you detect if the user is online or offline?](#70-how-do-you-detect-if-the-user-is-online-or-offline)
- [71: What is Lighthouse and how does it help with PWAs?](#71-what-is-lighthouse-and-how-does-it-help-with-pwas)
- [72: What is Workbox?](#72-what-is-workbox)
- [73: What is precaching?](#73-what-is-precaching)
- [74: What is runtime caching?](#74-what-is-runtime-caching)
- [75: Why do you version cache names?](#75-why-do-you-version-cache-names)
- [76: How does the browser check for a new service worker?](#76-how-does-the-browser-check-for-a-new-service-worker)
- [77: What does skipWaiting do?](#77-what-does-skipwaiting-do)
- [78: What does clients.claim do?](#78-what-does-clientsclaim-do)
- [79: What is a client in service worker terms?](#79-what-is-a-client-in-service-worker-terms)
- [80: How does a page send a message to its service worker?](#80-how-does-a-page-send-a-message-to-its-service-worker)
- [81: How does a service worker send a message to the page?](#81-how-does-a-service-worker-send-a-message-to-the-page)
- [82: What does the scope field in the manifest do?](#82-what-does-the-scope-field-in-the-manifest-do)
- [83: What is the id field in the manifest?](#83-what-is-the-id-field-in-the-manifest)
- [84: What are app shortcuts in the manifest?](#84-what-are-app-shortcuts-in-the-manifest)
- [85: What are description and screenshots used for in the manifest?](#85-what-are-description-and-screenshots-used-for-in-the-manifest)
- [86: What does the orientation field in the manifest do?](#86-what-does-the-orientation-field-in-the-manifest-do)
- [87: What is the Web Share API?](#87-what-is-the-web-share-api)
- [88: What is the Badging API?](#88-what-is-the-badging-api)
- [89: Can a PWA be published in app stores?](#89-can-a-pwa-be-published-in-app-stores)
- [90: What is a Trusted Web Activity?](#90-what-is-a-trusted-web-activity)
- [91: What is PWABuilder?](#91-what-is-pwabuilder)
- [92: What does a service worker do with requests to other domains?](#92-what-does-a-service-worker-do-with-requests-to-other-domains)
- [93: What is an opaque response?](#93-what-is-an-opaque-response)
- [94: What are the most common reasons a site is not installable?](#94-what-are-the-most-common-reasons-a-site-is-not-installable)
- [95: How do you test a PWA offline?](#95-how-do-you-test-a-pwa-offline)
- [96: What is "Update on reload" in DevTools?](#96-what-is-update-on-reload-in-devtools)
- [97: What does "Bypass for network" do in DevTools?](#97-what-does-bypass-for-network-do-in-devtools)
- [98: Are PWAs good for SEO?](#98-are-pwas-good-for-seo)
- [99: What is navigator.storage.estimate?](#99-what-is-navigatorstorageestimate)
- [100: Can the browser delete a PWA's cached data?](#100-can-the-browser-delete-a-pwas-cached-data)
- [101: How do you request persistent storage?](#101-how-do-you-request-persistent-storage)
- [102: How do you delete a cache or one entry from it?](#102-how-do-you-delete-a-cache-or-one-entry-from-it)
- [103: What does the ignoreSearch option do in cache.match?](#103-what-does-the-ignoresearch-option-do-in-cachematch)
- [104: What is request.mode === 'navigate'?](#104-what-is-requestmode--navigate)
- [105: What is request.destination?](#105-what-is-requestdestination)
- [106: How do you skip non-GET requests in the fetch handler?](#106-how-do-you-skip-non-get-requests-in-the-fetch-handler)
- [107: What is importScripts?](#107-what-is-importscripts)
- [108: Can a service worker be an ES module?](#108-can-a-service-worker-be-an-es-module)
- [109: What HTTP caching header should sw.js have?](#109-what-http-caching-header-should-swjs-have)
- [110: Should you rename sw.js on every deploy, like sw-v2.js?](#110-should-you-rename-swjs-on-every-deploy-like-sw-v2js)
- [111: What is the Service-Worker-Allowed header?](#111-what-is-the-service-worker-allowed-header)
- [112: How do you set a custom scope when registering?](#112-how-do-you-set-a-custom-scope-when-registering)
- [113: What happens if two service workers have overlapping scopes?](#113-what-happens-if-two-service-workers-have-overlapping-scopes)
- [114: What does a service worker do if it throws an error during install?](#114-what-does-a-service-worker-do-if-it-throws-an-error-during-install)
- [115: Do service workers work in private or incognito windows?](#115-do-service-workers-work-in-private-or-incognito-windows)
- [116: What is the difference between Background Sync and normal fetch?](#116-what-is-the-difference-between-background-sync-and-normal-fetch)
- [117: How do you register a background sync?](#117-how-do-you-register-a-background-sync)
- [118: What is Periodic Background Sync?](#118-what-is-periodic-background-sync)
- [119: What are notification options like body, icon, badge and tag?](#119-what-are-notification-options-like-body-icon-badge-and-tag)
- [120: What are notification actions?](#120-what-are-notification-actions)
- [121: What is VAPID?](#121-what-is-vapid)
- [122: What does userVisibleOnly mean in pushManager.subscribe?](#122-what-does-uservisibleonly-mean-in-pushmanagersubscribe)
- [123: Do you need Firebase to send web push?](#123-do-you-need-firebase-to-send-web-push)
- [124: How do you send a push message from Node.js?](#124-how-do-you-send-a-push-message-from-nodejs)
- [125: How does a user uninstall a PWA?](#125-how-does-a-user-uninstall-a-pwa)
- [126: How does an installed PWA get updated?](#126-how-does-an-installed-pwa-get-updated)
- [127: How do you build a Response by hand in a service worker?](#127-how-do-you-build-a-response-by-hand-in-a-service-worker)
- [128: Does the fetch event catch XMLHttpRequest calls?](#128-does-the-fetch-event-catch-xmlhttprequest-calls)
- [129: What are common real-world examples of PWAs?](#129-what-are-common-real-world-examples-of-pwas)
- [130: How do you add PWA support with Vite?](#130-how-do-you-add-pwa-support-with-vite)
- [131: How do you add a service worker to an Angular app?](#131-how-do-you-add-a-service-worker-to-an-angular-app)
- [132: How do you add a service worker to a Next.js app?](#132-how-do-you-add-a-service-worker-to-a-nextjs-app)
- [133: Can you test a service worker on a phone over a local network IP?](#133-can-you-test-a-service-worker-on-a-phone-over-a-local-network-ip)
- [134: Can a normal page use the Cache API?](#134-can-a-normal-page-use-the-cache-api)
- [135: What is the difference between a manifest's display and display_override?](#135-what-is-the-difference-between-a-manifests-display-and-display_override)
- [136: What is a splash screen in a PWA?](#136-what-is-a-splash-screen-in-a-pwa)
- [137: What does the categories field in the manifest do?](#137-what-does-the-categories-field-in-the-manifest-do)
- [138: What is related_applications in the manifest?](#138-what-is-related_applications-in-the-manifest)
- [139: What is navigator.getInstalledRelatedApps?](#139-what-is-navigatorgetinstalledrelatedapps)
- [140: What is the share_target field in the manifest?](#140-what-is-the-share_target-field-in-the-manifest)
- [141: What is the file_handlers field in the manifest?](#141-what-is-the-file_handlers-field-in-the-manifest)
- [142: What is the protocol_handlers field in the manifest?](#142-what-is-the-protocol_handlers-field-in-the-manifest)
- [143: Why must start_url work offline?](#143-why-must-start_url-work-offline)
- [144: Do you still need the apple-mobile-web-app-capable meta tag?](#144-do-you-still-need-the-apple-mobile-web-app-capable-meta-tag)
- [145: What viewport settings does a PWA need?](#145-what-viewport-settings-does-a-pwa-need)
- [146: How do you clear everything a service worker stored while developing?](#146-how-do-you-clear-everything-a-service-worker-stored-while-developing)
- [147: Can a service worker read cookies?](#147-can-a-service-worker-read-cookies)
- [148: Can you use fetch inside a service worker?](#148-can-you-use-fetch-inside-a-service-worker)
- [149: What does it mean that a service worker is event-driven?](#149-what-does-it-mean-that-a-service-worker-is-event-driven)
- [150: What is a good first checklist for turning a site into a PWA?](#150-what-is-a-good-first-checklist-for-turning-a-site-into-a-pwa)

### Moderate Questions (151-300)

- [151: What are registration.installing, waiting and active?](#151-what-are-registrationinstalling-waiting-and-active)
- [152: How do you detect that a new service worker version was found?](#152-how-do-you-detect-that-a-new-service-worker-version-was-found)
- [153: How do you build a "New version available, reload" flow?](#153-how-do-you-build-a-new-version-available-reload-flow)
- [154: Why can calling skipWaiting automatically be risky?](#154-why-can-calling-skipwaiting-automatically-be-risky)
- [155: What is the controllerchange event?](#155-what-is-the-controllerchange-event)
- [156: How do you check for updates in a long-lived single page app?](#156-how-do-you-check-for-updates-in-a-long-lived-single-page-app)
- [157: What does updateViaCache do?](#157-what-does-updateviacache-do)
- [158: How do you make an SPA's routes work offline?](#158-how-do-you-make-an-spas-routes-work-offline)
- [159: What is navigation preload?](#159-what-is-navigation-preload)
- [160: How do you enable and use navigation preload?](#160-how-do-you-enable-and-use-navigation-preload)
- [161: How do you add a timeout to a network first strategy?](#161-how-do-you-add-a-timeout-to-a-network-first-strategy)
- [162: How do you write stale-while-revalidate by hand?](#162-how-do-you-write-stale-while-revalidate-by-hand)
- [163: Why should you avoid caching error responses?](#163-why-should-you-avoid-caching-error-responses)
- [164: How do you limit the size of a runtime cache?](#164-how-do-you-limit-the-size-of-a-runtime-cache)
- [165: What is QuotaExceededError and how do you handle it?](#165-what-is-quotaexceedederror-and-how-do-you-handle-it)
- [166: Why do opaque responses use so much quota?](#166-why-do-opaque-responses-use-so-much-quota)
- [167: What are the main Workbox packages?](#167-what-are-the-main-workbox-packages)
- [168: What is the difference between generateSW and injectManifest in Workbox?](#168-what-is-the-difference-between-generatesw-and-injectmanifest-in-workbox)
- [169: What does self.__WB_MANIFEST do?](#169-what-does-self__wb_manifest-do)
- [170: How does Workbox precaching know which files changed?](#170-how-does-workbox-precaching-know-which-files-changed)
- [171: How do you set up runtime caching with Workbox?](#171-how-do-you-set-up-runtime-caching-with-workbox)
- [172: What does the CacheableResponsePlugin do?](#172-what-does-the-cacheableresponseplugin-do)
- [173: How do you add an offline fallback page in Workbox?](#173-how-do-you-add-an-offline-fallback-page-in-workbox)
- [174: What is setCatchHandler in Workbox?](#174-what-is-setcatchhandler-in-workbox)
- [175: How do you handle SPA navigation in Workbox?](#175-how-do-you-handle-spa-navigation-in-workbox)
- [176: What is workbox-window?](#176-what-is-workbox-window)
- [177: How do you queue failed POST requests with Workbox?](#177-how-do-you-queue-failed-post-requests-with-workbox)
- [178: What are Workbox plugins and lifecycle callbacks?](#178-what-are-workbox-plugins-and-lifecycle-callbacks)
- [179: What does the warmStrategyCache recipe do?](#179-what-does-the-warmstrategycache-recipe-do)
- [180: How does the full web push subscription flow work?](#180-how-does-the-full-web-push-subscription-flow-work)
- [181: How do you save a push subscription on the server?](#181-how-do-you-save-a-push-subscription-on-the-server)
- [182: What do you do when sending a push returns 404 or 410?](#182-what-do-you-do-when-sending-a-push-returns-404-or-410)
- [183: How do you check if the user is already subscribed to push?](#183-how-do-you-check-if-the-user-is-already-subscribed-to-push)
- [184: How do you unsubscribe from push?](#184-how-do-you-unsubscribe-from-push)
- [185: How do you focus an existing tab instead of opening a new one on notification click?](#185-how-do-you-focus-an-existing-tab-instead-of-opening-a-new-one-on-notification-click)
- [186: What do tag and renotify do together?](#186-what-do-tag-and-renotify-do-together)
- [187: What does requireInteraction do in a notification?](#187-what-does-requireinteraction-do-in-a-notification)
- [188: How do you check the notification permission without asking?](#188-how-do-you-check-the-notification-permission-without-asking)
- [189: How do you update the app badge from a push message?](#189-how-do-you-update-the-app-badge-from-a-push-message)
- [190: How do you write Playwright tests for a service worker?](#190-how-do-you-write-playwright-tests-for-a-service-worker)
- [191: What is chrome://serviceworker-internals?](#191-what-is-chromeserviceworker-internals)
- [192: What does "The FetchEvent resulted in a network error response" mean?](#192-what-does-the-fetchevent-resulted-in-a-network-error-response-mean)
- [193: Why does cache.put throw "Request method POST is unsupported"?](#193-why-does-cacheput-throw-request-method-post-is-unsupported)
- [194: How do you cache Google Fonts in a service worker?](#194-how-do-you-cache-google-fonts-in-a-service-worker)
- [195: What is Window Controls Overlay?](#195-what-is-window-controls-overlay)
- [196: What is the tabbed display mode?](#196-what-is-the-tabbed-display-mode)
- [197: What does launch_handler do in the manifest?](#197-what-does-launch_handler-do-in-the-manifest)
- [198: How is storage different for PWAs on iOS Safari?](#198-how-is-storage-different-for-pwas-on-ios-safari)
- [199: What happened with PWAs in the EU on iOS 17.4?](#199-what-happened-with-pwas-in-the-eu-on-ios-174)
- [200: How do you show a fallback image when an image fails offline?](#200-how-do-you-show-a-fallback-image-when-an-image-fails-offline)
- [201: How do you choose a caching strategy for each type of request?](#201-how-do-you-choose-a-caching-strategy-for-each-type-of-request)
- [202: How do you cache API responses that need an auth token?](#202-how-do-you-cache-api-responses-that-need-an-auth-token)
- [203: How does the Vary header affect cache.match?](#203-how-does-the-vary-header-affect-cachematch)
- [204: What should you clean up when a user logs out?](#204-what-should-you-clean-up-when-a-user-logs-out)
- [205: What is BroadcastChannel and how does it help PWAs?](#205-what-is-broadcastchannel-and-how-does-it-help-pwas)
- [206: How do you get a reply from the service worker to a specific message?](#206-how-do-you-get-a-reply-from-the-service-worker-to-a-specific-message)
- [207: What are event.clientId and event.resultingClientId?](#207-what-are-eventclientid-and-eventresultingclientid)
- [208: How does the service worker work with a Content Security Policy?](#208-how-does-the-service-worker-work-with-a-content-security-policy)
- [209: How do you load a manifest that is behind authentication?](#209-how-do-you-load-a-manifest-that-is-behind-authentication)
- [210: How do you set theme_color for dark mode?](#210-how-do-you-set-theme_color-for-dark-mode)
- [211: How do you design a good install promotion?](#211-how-do-you-design-a-good-install-promotion)
- [212: How do you measure how many users install and use the PWA?](#212-how-do-you-measure-how-many-users-install-and-use-the-pwa)
- [213: How do you store app data in IndexedDB for offline use?](#213-how-do-you-store-app-data-in-indexeddb-for-offline-use)
- [214: Should you store JSON API data in the Cache API or in IndexedDB?](#214-should-you-store-json-api-data-in-the-cache-api-or-in-indexeddb)
- [215: How do you build an outbox pattern for offline writes?](#215-how-do-you-build-an-outbox-pattern-for-offline-writes)
- [216: How do you handle background sync in browsers that don't support it?](#216-how-do-you-handle-background-sync-in-browsers-that-dont-support-it)
- [217: What happens if a sync event fails?](#217-what-happens-if-a-sync-event-fails)
- [218: How do you write a precache step without Workbox?](#218-how-do-you-write-a-precache-step-without-workbox)
- [219: Why should precached requests bypass the HTTP cache?](#219-why-should-precached-requests-bypass-the-http-cache)
- [220: How much should you precache?](#220-how-much-should-you-precache)
- [221: Can you precache files from a CDN on another domain?](#221-can-you-precache-files-from-a-cdn-on-another-domain)
- [222: How do you configure caching in Angular's ngsw-config.json?](#222-how-do-you-configure-caching-in-angulars-ngsw-configjson)
- [223: How do you handle updates with Angular's SwUpdate?](#223-how-do-you-handle-updates-with-angulars-swupdate)
- [224: How do you handle the "user is offline" state in the UI?](#224-how-do-you-handle-the-user-is-offline-state-in-the-ui)
- [225: How do you know if a response came from the cache or the network?](#225-how-do-you-know-if-a-response-came-from-the-cache-or-the-network)
- [226: What does workbox-broadcast-update do?](#226-what-does-workbox-broadcast-update-do)
- [227: How do you serve a different response for navigation preload requests on the server?](#227-how-do-you-serve-a-different-response-for-navigation-preload-requests-on-the-server)
- [228: How do you cache video or audio files?](#228-how-do-you-cache-video-or-audio-files)
- [229: How do you let users save content for offline reading?](#229-how-do-you-let-users-save-content-for-offline-reading)
- [230: What are good ways to debug a service worker that won't update?](#230-what-are-good-ways-to-debug-a-service-worker-that-wont-update)
- [231: How do you test push notifications locally?](#231-how-do-you-test-push-notifications-locally)
- [232: What does the Web Share Target look like for files?](#232-what-does-the-web-share-target-look-like-for-files)
- [233: How do you read files opened through file_handlers?](#233-how-do-you-read-files-opened-through-file_handlers)
- [234: What is the Origin Private File System and when would a PWA use it?](#234-what-is-the-origin-private-file-system-and-when-would-a-pwa-use-it)
- [235: How do you keep the screen on in a PWA?](#235-how-do-you-keep-the-screen-on-in-a-pwa)
- [236: What device APIs can a PWA use today?](#236-what-device-apis-can-a-pwa-use-today)
- [237: What is the Media Session API?](#237-what-is-the-media-session-api)
- [238: How do you handle app links so links open in the installed PWA?](#238-how-do-you-handle-app-links-so-links-open-in-the-installed-pwa)
- [239: How do you avoid caching responses for logged-out users and showing them to logged-in users?](#239-how-do-you-avoid-caching-responses-for-logged-out-users-and-showing-them-to-logged-in-users)
- [240: What is a service worker "kill switch"?](#240-what-is-a-service-worker-kill-switch)
- [241: Why is it important that sw.js itself is never served from the service worker's cache?](#241-why-is-it-important-that-swjs-itself-is-never-served-from-the-service-workers-cache)
- [242: How do you show a list of what is available offline?](#242-how-do-you-show-a-list-of-what-is-available-offline)
- [243: How do you avoid the offline page showing for server errors?](#243-how-do-you-avoid-the-offline-page-showing-for-server-errors)
- [244: How do you make sure a new deploy doesn't break users with old cached HTML?](#244-how-do-you-make-sure-a-new-deploy-doesnt-break-users-with-old-cached-html)
- [245: How do you recover when a lazy-loaded chunk fails to load after a deploy?](#245-how-do-you-recover-when-a-lazy-loaded-chunk-fails-to-load-after-a-deploy)
- [246: How do you handle form submissions when offline?](#246-how-do-you-handle-form-submissions-when-offline)
- [247: How do iOS home screen web apps differ from Safari tabs?](#247-how-do-ios-home-screen-web-apps-differ-from-safari-tabs)
- [248: How do you handle "back" navigation in a standalone PWA?](#248-how-do-you-handle-back-navigation-in-a-standalone-pwa)
- [249: What is the getRegistration method used for?](#249-what-is-the-getregistration-method-used-for)
- [250: Does calling register() on every page load cause extra work?](#250-does-calling-register-on-every-page-load-cause-extra-work)
- [251: How big can a push message payload be?](#251-how-big-can-a-push-message-payload-be)
- [252: What are the TTL and Urgency headers in web push?](#252-what-are-the-ttl-and-urgency-headers-in-web-push)
- [253: How do you avoid showing a notification when the user is already looking at the app?](#253-how-do-you-avoid-showing-a-notification-when-the-user-is-already-looking-at-the-app)
- [254: What is the pushsubscriptionchange event?](#254-what-is-the-pushsubscriptionchange-event)
- [255: How do you convert a VAPID public key for pushManager.subscribe?](#255-how-do-you-convert-a-vapid-public-key-for-pushmanagersubscribe)
- [256: How do you see which periodic syncs are registered?](#256-how-do-you-see-which-periodic-syncs-are-registered)
- [257: What does the periodicsync event handler usually do?](#257-what-does-the-periodicsync-event-handler-usually-do)
- [258: What is the monochrome icon purpose?](#258-what-is-the-monochrome-icon-purpose)
- [259: How do you use InjectManifest with webpack?](#259-how-do-you-use-injectmanifest-with-webpack)
- [260: How do you add a "Reload to update" prompt with vite-plugin-pwa?](#260-how-do-you-add-a-reload-to-update-prompt-with-vite-plugin-pwa)
- [261: Can you write a service worker in TypeScript?](#261-can-you-write-a-service-worker-in-typescript)
- [262: How do you monitor service worker errors in production?](#262-how-do-you-monitor-service-worker-errors-in-production)
- [263: How do you measure how long the service worker adds to requests?](#263-how-do-you-measure-how-long-the-service-worker-adds-to-requests)
- [264: Is HTTP caching still needed if you have a service worker?](#264-is-http-caching-still-needed-if-you-have-a-service-worker)
- [265: What is Clear-Site-Data and when would you use it?](#265-what-is-clear-site-data-and-when-would-you-use-it)
- [266: How do you deploy a PWA under a sub-path like GitHub Pages?](#266-how-do-you-deploy-a-pwa-under-a-sub-path-like-github-pages)
- [267: How are relative URLs in the manifest resolved?](#267-how-are-relative-urls-in-the-manifest-resolved)
- [268: What is a WebAPK?](#268-what-is-a-webapk)
- [269: How does PWA install work on desktop Safari?](#269-how-does-pwa-install-work-on-desktop-safari)
- [270: Can you prefetch pages in the service worker?](#270-can-you-prefetch-pages-in-the-service-worker)
- [271: How do Speculation Rules and service workers work together?](#271-how-do-speculation-rules-and-service-workers-work-together)
- [272: Does a service worker affect the back/forward cache?](#272-does-a-service-worker-affect-the-backforward-cache)
- [273: How do you cache third-party API responses?](#273-how-do-you-cache-third-party-api-responses)
- [274: How do you make the service worker ignore certain URLs?](#274-how-do-you-make-the-service-worker-ignore-certain-urls)
- [275: Does a service worker intercept WebSocket connections?](#275-does-a-service-worker-intercept-websocket-connections)
- [276: How do you handle API calls with a stale cache in the UI?](#276-how-do-you-handle-api-calls-with-a-stale-cache-in-the-ui)
- [277: What is the difference between registration.showNotification and new Notification?](#277-what-is-the-difference-between-registrationshownotification-and-new-notification)
- [278: How do you list or close notifications that are already shown?](#278-how-do-you-list-or-close-notifications-that-are-already-shown)
- [279: Can a PWA run code on a schedule like a cron job?](#279-can-a-pwa-run-code-on-a-schedule-like-a-cron-job)
- [280: What are common mistakes in a first service worker?](#280-what-are-common-mistakes-in-a-first-service-worker)
- [281: How do you warm the cache with data the user will likely need offline?](#281-how-do-you-warm-the-cache-with-data-the-user-will-likely-need-offline)
- [282: How do icons and screenshots affect the install prompt quality?](#282-how-do-icons-and-screenshots-affect-the-install-prompt-quality)
- [283: How do you make a PWA feel more like a native app?](#283-how-do-you-make-a-pwa-feel-more-like-a-native-app)
- [284: What does overscroll-behavior do for PWAs?](#284-what-does-overscroll-behavior-do-for-pwas)
- [285: How do you handle safe areas on phones with a notch?](#285-how-do-you-handle-safe-areas-on-phones-with-a-notch)
- [286: How do you make a PWA work when it is loaded inside an iframe?](#286-how-do-you-make-a-pwa-work-when-it-is-loaded-inside-an-iframe)
- [287: What is storage partitioning and how does it affect service workers?](#287-what-is-storage-partitioning-and-how-does-it-affect-service-workers)
- [288: How do you use the Cache API from the page to check what is cached?](#288-how-do-you-use-the-cache-api-from-the-page-to-check-what-is-cached)
- [289: How do you add offline analytics?](#289-how-do-you-add-offline-analytics)
- [290: What happens to the service worker when the user clears browsing data?](#290-what-happens-to-the-service-worker-when-the-user-clears-browsing-data)
- [291: How do you handle different app versions running at the same time?](#291-how-do-you-handle-different-app-versions-running-at-the-same-time)
- [292: How do you migrate an IndexedDB schema in a PWA update?](#292-how-do-you-migrate-an-indexeddb-schema-in-a-pwa-update)
- [293: How do you share state between the service worker and the page?](#293-how-do-you-share-state-between-the-service-worker-and-the-page)
- [294: How do you make an installable PWA for desktop only features like keyboard shortcuts?](#294-how-do-you-make-an-installable-pwa-for-desktop-only-features-like-keyboard-shortcuts)
- [295: How do you let users install the PWA on iOS from a browser other than Safari?](#295-how-do-you-let-users-install-the-pwa-on-ios-from-a-browser-other-than-safari)
- [296: How do you protect a PWA from serving a cached page with an old CSRF token?](#296-how-do-you-protect-a-pwa-from-serving-a-cached-page-with-an-old-csrf-token)
- [297: How do you test a PWA install on Android during development?](#297-how-do-you-test-a-pwa-install-on-android-during-development)
- [298: What are icons purpose any and maskable together?](#298-what-are-icons-purpose-any-and-maskable-together)
- [299: How do you debug why the install prompt isn't showing in Chrome?](#299-how-do-you-debug-why-the-install-prompt-isnt-showing-in-chrome)
- [300: How do you handle localization in a PWA manifest?](#300-how-do-you-handle-localization-in-a-pwa-manifest)

### Advanced Questions (301-450)

- [301: Why does a new service worker wait instead of taking over right away?](#301-why-does-a-new-service-worker-wait-instead-of-taking-over-right-away)
- [302: How exactly does the browser decide a service worker has changed?](#302-how-exactly-does-the-browser-decide-a-service-worker-has-changed)
- [303: How long can a service worker stay alive?](#303-how-long-can-a-service-worker-stay-alive)
- [304: Why are tricks to keep a service worker alive a bad idea?](#304-why-are-tricks-to-keep-a-service-worker-alive-a-bad-idea)
- [305: What bugs come from keeping state in global variables in a service worker?](#305-what-bugs-come-from-keeping-state-in-global-variables-in-a-service-worker)
- [306: Why must respondWith be called synchronously?](#306-why-must-respondwith-be-called-synchronously)
- [307: How do you do background work after responding to a fetch?](#307-how-do-you-do-background-work-after-responding-to-a-fetch)
- [308: How can a service worker stream a page built from several parts?](#308-how-can-a-service-worker-stream-a-page-built-from-several-parts)
- [309: What is the Static Routing API?](#309-what-is-the-static-routing-api)
- [310: When would you use navigation preload versus the Static Routing API?](#310-when-would-you-use-navigation-preload-versus-the-static-routing-api)
- [311: Why is an empty or pass-through fetch handler harmful?](#311-why-is-an-empty-or-pass-through-fetch-handler-harmful)
- [312: How does cache.match decide if a request matches?](#312-how-does-cachematch-decide-if-a-request-matches)
- [313: Is writing to the Cache API safe when several tabs do it at once?](#313-is-writing-to-the-cache-api-safe-when-several-tabs-do-it-at-once)
- [314: The Cache API ignores Cache-Control. How do you add expiration?](#314-the-cache-api-ignores-cache-control-how-do-you-add-expiration)
- [315: How do you do conditional revalidation with ETags from a service worker?](#315-how-do-you-do-conditional-revalidation-with-etags-from-a-service-worker)
- [316: What is the problem with redirected responses in a service worker?](#316-what-is-the-problem-with-redirected-responses-in-a-service-worker)
- [317: What are the different Response types and why do they matter?](#317-what-are-the-different-response-types-and-why-do-they-matter)
- [318: What are request modes and how do they affect what a service worker can do?](#318-what-are-request-modes-and-how-do-they-affect-what-a-service-worker-can-do)
- [319: How can a service worker be abused after an XSS bug?](#319-how-can-a-service-worker-be-abused-after-an-xss-bug)
- [320: What is the Service-Worker request header?](#320-what-is-the-service-worker-request-header)
- [321: Why is hosting user content under your main origin dangerous for service workers?](#321-why-is-hosting-user-content-under-your-main-origin-dangerous-for-service-workers)
- [322: What is cache poisoning in a service worker context?](#322-what-is-cache-poisoning-in-a-service-worker-context)
- [323: How do captive portals break PWAs and how do you avoid it?](#323-how-do-captive-portals-break-pwas-and-how-do-you-avoid-it)
- [324: How do cross-origin isolation headers interact with service workers?](#324-how-do-cross-origin-isolation-headers-interact-with-service-workers)
- [325: How do you protect sensitive offline data on a shared device?](#325-how-do-you-protect-sensitive-offline-data-on-a-shared-device)
- [326: How is a web push payload encrypted?](#326-how-is-a-web-push-payload-encrypted)
- [327: How does VAPID authentication work in detail?](#327-how-does-vapid-authentication-work-in-detail)
- [328: How do you send push notifications to millions of users?](#328-how-do-you-send-push-notifications-to-millions-of-users)
- [329: What delivery guarantees does web push give?](#329-what-delivery-guarantees-does-web-push-give)
- [330: How do browsers limit push and notification abuse?](#330-how-do-browsers-limit-push-and-notification-abuse)
- [331: What is Declarative Web Push?](#331-what-is-declarative-web-push)
- [332: How does Background Sync decide when to fire?](#332-how-does-background-sync-decide-when-to-fire)
- [333: What is the Background Fetch API?](#333-what-is-the-background-fetch-api)
- [334: What is the Content Index API?](#334-what-is-the-content-index-api)
- [335: How does the browser decide how often Periodic Background Sync runs?](#335-how-does-the-browser-decide-how-often-periodic-background-sync-runs)
- [336: How much storage can a PWA use?](#336-how-much-storage-can-a-pwa-use)
- [337: How does storage eviction work?](#337-how-does-storage-eviction-work)
- [338: What is the Storage Buckets API?](#338-what-is-the-storage-buckets-api)
- [339: How would you design an offline-first sync engine?](#339-how-would-you-design-an-offline-first-sync-engine)
- [340: What conflict resolution strategies exist for offline edits?](#340-what-conflict-resolution-strategies-exist-for-offline-edits)
- [341: How do you sync deletes in an offline-first app?](#341-how-do-you-sync-deletes-in-an-offline-first-app)
- [342: How do you implement idempotent replays of queued requests?](#342-how-do-you-implement-idempotent-replays-of-queued-requests)
- [343: How do you make sure only one tab runs the sync at a time?](#343-how-do-you-make-sure-only-one-tab-runs-the-sync-at-a-time)
- [344: When would you use a SharedWorker instead of the service worker for shared state?](#344-when-would-you-use-a-sharedworker-instead-of-the-service-worker-for-shared-state)
- [345: How do you roll out a risky service worker change safely?](#345-how-do-you-roll-out-a-risky-service-worker-change-safely)
- [346: How does a service worker fit with server-side rendering?](#346-how-does-a-service-worker-fit-with-server-side-rendering)
- [347: What are the trade-offs between the app shell model and network first HTML?](#347-what-are-the-trade-offs-between-the-app-shell-model-and-network-first-html)
- [348: Can a service worker make a site slower?](#348-can-a-service-worker-make-a-site-slower)
- [349: What is the "race cache and network" strategy?](#349-what-is-the-race-cache-and-network-strategy)
- [350: How do you measure the real impact of a service worker in production?](#350-how-do-you-measure-the-real-impact-of-a-service-worker-in-production)
- [351: What happens if precaching takes a long time on a slow network?](#351-what-happens-if-precaching-takes-a-long-time-on-a-slow-network)
- [352: Does one failed file in precaching break everything?](#352-does-one-failed-file-in-precaching-break-everything)
- [353: What iOS limits should a PWA architect plan around?](#353-what-ios-limits-should-a-pwa-architect-plan-around)
- [354: When would you choose a PWA over a native app, and when not?](#354-when-would-you-choose-a-pwa-over-a-native-app-and-when-not)
- [355: How does a Trusted Web Activity verify the site?](#355-how-does-a-trusted-web-activity-verify-the-site)
- [356: How do you sell digital goods in a PWA on Google Play?](#356-how-do-you-sell-digital-goods-in-a-pwa-on-google-play)
- [357: How do passkeys work in an installed PWA?](#357-how-do-passkeys-work-in-an-installed-pwa)
- [358: Should a service worker add Authorization headers to requests?](#358-should-a-service-worker-add-authorization-headers-to-requests)
- [359: How do you modify a request in a service worker?](#359-how-do-you-modify-a-request-in-a-service-worker)
- [360: Why do you need to clone a request before retrying it?](#360-why-do-you-need-to-clone-a-request-before-retrying-it)
- [361: How does Workbox store requests for background sync?](#361-how-does-workbox-store-requests-for-background-sync)
- [362: What are the limitations of module service workers?](#362-what-are-the-limitations-of-module-service-workers)
- [363: How does a hard reload interact with the service worker?](#363-how-does-a-hard-reload-interact-with-the-service-worker)
- [364: What problem can clients.claim cause?](#364-what-problem-can-clientsclaim-cause)
- [365: How do you find all clients, including ones the worker doesn't control?](#365-how-do-you-find-all-clients-including-ones-the-worker-doesnt-control)
- [366: How do you answer Range requests yourself in a service worker?](#366-how-do-you-answer-range-requests-yourself-in-a-service-worker)
- [367: Cache API or OPFS for large files?](#367-cache-api-or-opfs-for-large-files)
- [368: How does the number of cache entries affect performance?](#368-how-does-the-number-of-cache-entries-affect-performance)
- [369: Can you use Subresource Integrity when precaching?](#369-can-you-use-subresource-integrity-when-precaching)
- [370: Why is importScripts from a third-party CDN risky?](#370-why-is-importscripts-from-a-third-party-cdn-risky)
- [371: What happens if the manifest scope and service worker scope don't match?](#371-what-happens-if-the-manifest-scope-and-service-worker-scope-dont-match)
- [372: How do you change a PWA's manifest id or start_url without breaking installs?](#372-how-do-you-change-a-pwas-manifest-id-or-start_url-without-breaking-installs)
- [373: How do installed apps pick up manifest changes?](#373-how-do-installed-apps-pick-up-manifest-changes)
- [374: Can you have several installable PWAs on one origin?](#374-can-you-have-several-installable-pwas-on-one-origin)
- [375: What is scope_extensions?](#375-what-is-scope_extensions)
- [376: What are Isolated Web Apps?](#376-what-are-isolated-web-apps)
- [377: How does web push on Safari differ from Chrome?](#377-how-does-web-push-on-safari-differ-from-chrome)
- [378: Why might web push work on Android but not on desktop?](#378-why-might-web-push-work-on-android-but-not-on-desktop)
- [379: A deploy shipped a broken precache list and nobody gets the new version. What do you do?](#379-a-deploy-shipped-a-broken-precache-list-and-nobody-gets-the-new-version-what-do-you-do)
- [380: How do you test service worker logic?](#380-how-do-you-test-service-worker-logic)
- [381: How does Workbox store precached files with revisions?](#381-how-does-workbox-store-precached-files-with-revisions)
- [382: What was AppCache and why was it replaced?](#382-what-was-appcache-and-why-was-it-replaced)
- [383: How does Angular's service worker decide what changed?](#383-how-does-angulars-service-worker-decide-what-changed)
- [384: What is Angular's safety worker?](#384-what-is-angulars-safety-worker)
- [385: What was foreign fetch?](#385-what-was-foreign-fetch)
- [386: How do you stay data friendly with users on slow or expensive connections?](#386-how-do-you-stay-data-friendly-with-users-on-slow-or-expensive-connections)
- [387: How would you design a PWA for a news site with offline reading?](#387-how-would-you-design-a-pwa-for-a-news-site-with-offline-reading)
- [388: How would you design an offline shopping cart?](#388-how-would-you-design-an-offline-shopping-cart)
- [389: How would you design a field inspection app used with bad connectivity?](#389-how-would-you-design-a-field-inspection-app-used-with-bad-connectivity)
- [390: How would you design a chat PWA?](#390-how-would-you-design-a-chat-pwa)
- [391: Users report they still see an old version days after a deploy. How do you investigate?](#391-users-report-they-still-see-an-old-version-days-after-a-deploy-how-do-you-investigate)
- [392: Users complain the app uses too much storage. What do you do?](#392-users-complain-the-app-uses-too-much-storage-what-do-you-do)
- [393: After adding a service worker, LCP got worse on low-end Android. Why, and how do you fix it?](#393-after-adding-a-service-worker-lcp-got-worse-on-low-end-android-why-and-how-do-you-fix-it)
- [394: Logged-in users sometimes see the logged-out page. What is wrong?](#394-logged-in-users-sometimes-see-the-logged-out-page-what-is-wrong)
- [395: Push notifications don't arrive on iPhone. What do you check?](#395-push-notifications-dont-arrive-on-iphone-what-do-you-check)
- [396: Users get the same notification twice. What could cause it?](#396-users-get-the-same-notification-twice-what-could-cause-it)
- [397: You're moving the app to a new domain. What happens to the PWA?](#397-youre-moving-the-app-to-a-new-domain-what-happens-to-the-pwa)
- [398: How do you completely remove a PWA from production?](#398-how-do-you-completely-remove-a-pwa-from-production)
- [399: How can you run A/B tests with a service worker in place?](#399-how-can-you-run-ab-tests-with-a-service-worker-in-place)
- [400: How do you handle a multi-tenant SaaS on subdomains as a PWA?](#400-how-do-you-handle-a-multi-tenant-saas-on-subdomains-as-a-pwa)
- [401: How do micro frontends share one service worker?](#401-how-do-micro-frontends-share-one-service-worker)
- [402: PWA or Electron for a desktop app?](#402-pwa-or-electron-for-a-desktop-app)
- [403: Capacitor or Trusted Web Activity for getting a PWA into stores?](#403-capacitor-or-trusted-web-activity-for-getting-a-pwa-into-stores)
- [404: How do you handle a 409 conflict when syncing an offline change?](#404-how-do-you-handle-a-409-conflict-when-syncing-an-offline-change)
- [405: Can a service worker leak information about which sites a user visited?](#405-can-a-service-worker-leak-information-about-which-sites-a-user-visited)
- [406: How do CSP nonces cause problems with cached HTML?](#406-how-do-csp-nonces-cause-problems-with-cached-html)
- [407: How do you build a simple router in a service worker without Workbox?](#407-how-do-you-build-a-simple-router-in-a-service-worker-without-workbox)
- [408: How can URLPattern help in a service worker?](#408-how-can-urlpattern-help-in-a-service-worker)
- [409: Why should a fetch handler avoid heavy synchronous work?](#409-why-should-a-fetch-handler-avoid-heavy-synchronous-work)
- [410: How does Mock Service Worker (MSW) use service workers?](#410-how-does-mock-service-worker-msw-use-service-workers)
- [411: How do you test the service worker update flow automatically?](#411-how-do-you-test-the-service-worker-update-flow-automatically)
- [412: How do you track service worker version adoption?](#412-how-do-you-track-service-worker-version-adoption)
- [413: Explain what happens step by step on a repeat visit to a PWA with a cached app shell.](#413-explain-what-happens-step-by-step-on-a-repeat-visit-to-a-pwa-with-a-cached-app-shell)
- [414: How do you handle large forms with photos offline on a phone with little storage?](#414-how-do-you-handle-large-forms-with-photos-offline-on-a-phone-with-little-storage)
- [415: Why should you store binary data as Blobs and not base64 in IndexedDB?](#415-why-should-you-store-binary-data-as-blobs-and-not-base64-in-indexeddb)
- [416: What happens to IndexedDB transactions that await unrelated promises?](#416-what-happens-to-indexeddb-transactions-that-await-unrelated-promises)
- [417: How do you keep an IndexedDB connection healthy in a service worker?](#417-how-do-you-keep-an-indexeddb-connection-healthy-in-a-service-worker)
- [418: How do you avoid flashes of old content with stale-while-revalidate?](#418-how-do-you-avoid-flashes-of-old-content-with-stale-while-revalidate)
- [419: How do Early Hints and service workers interact?](#419-how-do-early-hints-and-service-workers-interact)
- [420: How do the Fetch event and CORS preflights interact?](#420-how-do-the-fetch-event-and-cors-preflights-interact)
- [421: Why might cached fonts or images fail to render after being served by the worker?](#421-why-might-cached-fonts-or-images-fail-to-render-after-being-served-by-the-worker)
- [422: How do you serve different cached content to installed and browser users?](#422-how-do-you-serve-different-cached-content-to-installed-and-browser-users)
- [423: What does the Payment Handler API let a PWA do?](#423-what-does-the-payment-handler-api-let-a-pwa-do)
- [424: How do you choose between Cache Storage, IndexedDB, OPFS and localStorage?](#424-how-do-you-choose-between-cache-storage-indexeddb-opfs-and-localstorage)
- [425: How does SQLite in the browser work for offline PWAs?](#425-how-does-sqlite-in-the-browser-work-for-offline-pwas)
- [426: What is the right way to show a notification permission prompt in a PWA?](#426-what-is-the-right-way-to-show-a-notification-permission-prompt-in-a-pwa)
- [427: How do you handle different push topics per user?](#427-how-do-you-handle-different-push-topics-per-user)
- [428: How should you handle the push event when payload decryption fails or data is missing?](#428-how-should-you-handle-the-push-event-when-payload-decryption-fails-or-data-is-missing)
- [429: How do you avoid a stampede on your API when many users get the same push?](#429-how-do-you-avoid-a-stampede-on-your-api-when-many-users-get-the-same-push)
- [430: What should a service worker do on activate besides deleting caches?](#430-what-should-a-service-worker-do-on-activate-besides-deleting-caches)
- [431: Can fetch events be delayed by a slow activate?](#431-can-fetch-events-be-delayed-by-a-slow-activate)
- [432: How do you handle multiple service worker files left over from old setups?](#432-how-do-you-handle-multiple-service-worker-files-left-over-from-old-setups)
- [433: How does the browser handle a navigation when the worker fails to start?](#433-how-does-the-browser-handle-a-navigation-when-the-worker-fails-to-start)
- [434: How do you make sure the offline page itself always works?](#434-how-do-you-make-sure-the-offline-page-itself-always-works)
- [435: How do you design caching for an app that updates content every minute, like a sports scores app?](#435-how-do-you-design-caching-for-an-app-that-updates-content-every-minute-like-a-sports-scores-app)
- [436: How do you keep the app and the service worker using the same version of shared code?](#436-how-do-you-keep-the-app-and-the-service-worker-using-the-same-version-of-shared-code)
- [437: What are the risks of caching POST responses by URL?](#437-what-are-the-risks-of-caching-post-responses-by-url)
- [438: How do you add offline support to a GraphQL app?](#438-how-do-you-add-offline-support-to-a-graphql-app)
- [439: How do you handle authentication expiry for queued offline requests?](#439-how-do-you-handle-authentication-expiry-for-queued-offline-requests)
- [440: How do browsers stop a malicious page from installing a fake PWA of a bank?](#440-how-do-browsers-stop-a-malicious-page-from-installing-a-fake-pwa-of-a-bank)
- [441: What is the "update on navigation" problem in SPAs?](#441-what-is-the-update-on-navigation-problem-in-spas)
- [442: How would you add PWA features to a large existing site step by step?](#442-how-would-you-add-pwa-features-to-a-large-existing-site-step-by-step)
- [443: What should be in a PWA code review checklist?](#443-what-should-be-in-a-pwa-code-review-checklist)
- [444: What new or recent PWA-related features should a senior developer know about?](#444-what-new-or-recent-pwa-related-features-should-a-senior-developer-know-about)
- [445: Why did Chrome stop requiring a service worker for installability?](#445-why-did-chrome-stop-requiring-a-service-worker-for-installability)
- [446: How do you explain the difference between "installable" and "a good PWA"?](#446-how-do-you-explain-the-difference-between-installable-and-a-good-pwa)
- [447: How do you build an "offline-ready" indicator that is honest?](#447-how-do-you-build-an-offline-ready-indicator-that-is-honest)
- [448: How do you decide which features to show when offline?](#448-how-do-you-decide-which-features-to-show-when-offline)
- [449: How would you explain service workers to a non-technical stakeholder?](#449-how-would-you-explain-service-workers-to-a-non-technical-stakeholder)
- [450: Design an offline-first PWA for a team task manager. What are the key decisions?](#450-design-an-offline-first-pwa-for-a-team-task-manager-what-are-the-key-decisions)

---

# Easy Questions (1-150)

## 1: What is a Progressive Web App?

A Progressive Web App (PWA) is a normal website that uses a few browser features so it can behave more like an installed app. It can be added to the home screen or desktop, open in its own window, work offline or on a bad network, and show push notifications.

There is no special framework or file format. A PWA is still HTML, CSS and JavaScript served over HTTPS. What makes it "app-like" is mostly a web app manifest and a service worker.

## 2: Why is it called "progressive"?

Because it is built with progressive enhancement. The site works in every browser as a normal page, and browsers that support extra features (service workers, install, push) give users more on top of that.

A user on an old browser still gets the website. A user on a modern browser gets offline support and an install option. Nobody is locked out.

## 3: What are the main building blocks of a PWA?

- **HTTPS**: required for service workers and most PWA APIs.
- **Web app manifest**: a JSON file with the app name, icons, colors and how it should open.
- **Service worker**: a script that runs in the background and can intercept network requests, cache files and handle push messages.

With these three in place, most browsers will treat the site as installable.

## 4: What is a service worker?

A service worker is a JavaScript file that the browser runs separately from your page, in its own thread. It sits between your page and the network, like a small proxy that you control.

It can catch every request the page makes and decide what to return: a cached file, a fresh network response, or something it builds itself. It also wakes up for events like push messages and background sync, even when no page of your site is open.

## 5: How is a service worker different from a regular script on the page?

A regular script runs on the main thread, has access to the DOM and lives only as long as the page is open. A service worker runs on its own thread, has no access to the DOM, and its life is managed by the browser, not by the page.

The browser starts the service worker when an event comes in (a fetch, a push, a message) and stops it when it has been idle for a while. One service worker controls all open tabs of your site within its scope.

## 6: How is a service worker different from a Web Worker?

Both run off the main thread and have no DOM access. The difference is what they are for and how long they live:

- A **Web Worker** belongs to one page. The page creates it, talks to it with `postMessage`, and it dies when the page closes. It is used for heavy calculations.
- A **service worker** belongs to an origin and a scope, not to a page. It can intercept network requests, keeps working across page loads, and can wake up for push or sync events with no page open.

## 7: How do you register a service worker?

From your page script, call `navigator.serviceWorker.register()` with the path to the worker file. Check that the API exists first so older browsers don't throw.

```js
if ("serviceWorker" in navigator) {
  window.addEventListener("load", async () => {
    try {
      const reg = await navigator.serviceWorker.register("/sw.js");
      console.log("Service worker registered, scope:", reg.scope);
    } catch (err) {
      console.error("Registration failed:", err);
    }
  });
}
```

Waiting for the `load` event is common so that the worker's own downloads don't compete with the first page load.

## 8: Why do service workers need HTTPS?

A service worker can intercept and change every request your site makes. If an attacker could inject a service worker over plain HTTP, they could keep control of the site for that user long after the attack. HTTPS makes sure the worker script really came from your server.

The only exception is `localhost` (and `127.0.0.1`), which browsers treat as secure so you can develop without certificates.

## 9: What is a web app manifest?

It is a JSON file that tells the browser how your app should look and behave when installed: its name, icons, start URL, theme color, and display mode. You link it from every page in the `<head>`.

```html
<link rel="manifest" href="/manifest.webmanifest" />
```

The browser reads it to show the install prompt, the home screen icon and the splash screen.

## 10: What does a basic manifest file look like?

```json
{
  "name": "Task Tracker",
  "short_name": "Tasks",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#1e88e5",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

That is enough for most browsers to consider the app installable, as long as it is on HTTPS.

## 11: What file extension should a manifest have?

The spec recommends `.webmanifest` and the MIME type `application/manifest+json`. In practice browsers also accept `manifest.json` served as `application/json`, and many projects use that name.

What matters most is that the `<link rel="manifest">` points to the right URL and the file is valid JSON.

## 12: What is the difference between name and short_name in the manifest?

`name` is the full app name, shown in places with enough room, like the install dialog or the app list. `short_name` is used where space is tight, like the label under a home screen icon.

If you only give `name`, the browser will cut it off when it doesn't fit, so it is good to provide both.

## 13: What does start_url do?

`start_url` is the page that opens when the user launches the installed app. Usually it is `/` or something like `/app/`.

Teams often add a query parameter, for example `/?source=pwa`, so analytics can tell app launches apart from normal visits. The URL must be within the app's scope.

## 14: What are the display modes in a manifest?

- `fullscreen`: takes the whole screen, no browser UI and no status bar. Good for games.
- `standalone`: opens in its own window with no address bar, like a native app. The most common choice.
- `minimal-ui`: its own window with a small set of browser controls like back and reload. Support varies.
- `browser`: opens in a normal browser tab.

If a browser doesn't support the mode you pick, it falls back down this list.

## 15: What is theme_color used for?

`theme_color` sets the color of the browser or OS UI around your app, like the title bar on desktop or the status bar on Android. It makes the app feel more native and branded.

You can also set it per page with a meta tag, which overrides the manifest while that page is open:

```html
<meta name="theme-color" content="#1e88e5" />
```

## 16: What is background_color used for?

It is the color the browser shows while the installed app is starting and the page hasn't painted yet. On Android, it is the background of the splash screen.

Set it to the same color as your page background so the launch doesn't flash a different color.

## 17: Why do you need several icon sizes in the manifest?

Different places need different sizes: a small icon for the task bar, a medium one for the home screen, and a large one for splash screens and app stores. If you only give one size, the browser has to scale it, which can look blurry.

At minimum provide a 192x192 and a 512x512 PNG. Many teams also add an SVG or more sizes for desktop.

## 18: What is a maskable icon?

A maskable icon is an icon made so the OS can crop it into different shapes (circle, rounded square, squircle) without cutting off the important part. You keep the logo inside a central "safe zone" (a circle with 80% of the icon's width) and fill the rest with background.

You mark it with `purpose`:

```json
{
  "src": "/icons/maskable-512.png",
  "sizes": "512x512",
  "type": "image/png",
  "purpose": "maskable"
}
```

Without a maskable icon, Android may put your icon inside a white circle.

## 19: What does "installable" mean for a PWA?

It means the browser is willing to offer the user to install it, so it gets an icon on the home screen or desktop and opens in its own window. Each browser has its own rules, but they usually need HTTPS, a valid manifest with a name, icons and a start URL, and a display mode other than `browser`.

Chrome used to also require a service worker with a fetch handler. It dropped that requirement in 2023-2024, but you still want a service worker for offline support.

## 20: How does a user install a PWA?

- **Chrome and Edge on desktop**: an install icon in the address bar, or the browser menu.
- **Chrome on Android**: an install banner or "Add to Home screen"/"Install app" in the menu.
- **Safari on iOS and iPadOS**: Share button, then "Add to Home Screen".
- **Safari on macOS**: File menu, then "Add to Dock".

Sites can also show their own install button in browsers that fire the `beforeinstallprompt` event (Chromium-based ones).

## 21: What is the scope of a service worker?

The scope is the set of URLs the service worker controls. By default it is the folder the worker file lives in. A worker at `/sw.js` controls the whole site, and a worker at `/app/sw.js` only controls pages under `/app/`.

The worker only receives `fetch` events for pages inside its scope.

## 22: Why do people usually put sw.js in the root of the site?

So the default scope is `/` and the worker controls every page. If you put it at `/js/sw.js`, it would only control pages under `/js/`, which is almost never what you want.

You can't widen the scope beyond the script's folder unless the server sends a `Service-Worker-Allowed` header, so putting the file at the root is the simple fix.

## 23: What is the service worker lifecycle?

A service worker goes through these steps:

1. **Register**: the page asks the browser to register the script.
2. **Install**: the `install` event fires once for this version. You usually cache files here.
3. **Waiting**: if an older worker still controls open pages, the new one waits.
4. **Activate**: the `activate` event fires. You usually delete old caches here.
5. **Controlling**: the worker now handles `fetch` and other events for pages in its scope.

It ends up **redundant** if installing fails or a newer version replaces it.

## 24: What happens in the install event?

The `install` event fires once when the browser sees a new version of the worker. It is the place to download and cache the files the app needs to work offline (the "app shell").

```js
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open("static-v1")
      .then((cache) =>
        cache.addAll(["/", "/styles.css", "/app.js", "/offline.html"]),
      ),
  );
});
```

If any file in `addAll` fails, the whole install fails and the browser will try again later.

## 25: What happens in the activate event?

`activate` fires when the new worker takes over. It is the right time to clean up after old versions, for example deleting caches the new code no longer uses.

```js
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys.filter((k) => k !== "static-v1").map((k) => caches.delete(k)),
        ),
      ),
  );
});
```

You don't do this in `install` because the old worker might still be using those caches.

## 26: What does event.waitUntil do?

It tells the browser "don't consider this event done, and don't stop the worker, until this promise settles". The browser can kill an idle service worker at any time, so without `waitUntil` your async work could be cut off.

In `install`, if the promise rejects, the install fails. In `activate`, the worker won't handle fetches until the promise finishes. It is also used in `push`, `sync` and `notificationclick` handlers.

## 27: What is the fetch event?

The `fetch` event fires in the service worker for every network request made by a page it controls: the HTML page itself, scripts, styles, images, and `fetch()` calls. You can answer it with `event.respondWith()`.

```js
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches
      .match(event.request)
      .then((cached) => cached || fetch(event.request)),
  );
});
```

If you don't call `respondWith`, the request goes to the network as usual.

## 28: What does event.respondWith do?

It lets the service worker give the page its own response for a request. You pass it a `Response` or a promise that resolves to one. The response can come from the cache, the network, or be built by hand.

You must call it synchronously inside the fetch handler (not after an `await`), otherwise the browser has already decided to let the request go to the network.

## 29: What is the Cache API?

The Cache API is a storage system for pairs of `Request` and `Response` objects. It is made for storing network responses so you can serve them later, even offline.

```js
const cache = await caches.open("images-v1");
await cache.put("/logo.png", await fetch("/logo.png"));
const res = await cache.match("/logo.png");
```

It is available in service workers and in normal pages through the global `caches` object.

## 30: Is the Cache API the same as the HTTP cache?

No. The HTTP cache is managed by the browser automatically, based on headers like `Cache-Control`. You can't control exactly what is in it.

The Cache API is fully under your control. Things only go in when your code puts them there, and they only come out when your code deletes them or the browser clears storage. It ignores `Cache-Control` headers completely.

## 31: What is the difference between caches.open and caches.match?

`caches.open(name)` opens (or creates) one named cache and gives you a `Cache` object you can add to, read from or delete from.

`caches.match(request)` searches across all your caches and returns the first matching response, or `undefined`. It is a shortcut when you don't care which cache it is in.

## 32: What is the difference between cache.add, cache.addAll and cache.put?

- `cache.add(url)` fetches the URL and stores the response.
- `cache.addAll(urls)` does the same for a list. If any one fails, nothing is stored.
- `cache.put(request, response)` stores a response you already have, without fetching.

`add` and `addAll` reject if the response status is not in the 200 range. `put` stores whatever you give it, including error responses, so check `response.ok` first.

## 33: What is the app shell model?

The app shell is the minimal HTML, CSS and JavaScript needed to draw the app's UI frame: header, navigation, layout, loading states. You cache the shell when the service worker installs, so the app opens instantly from cache, and then fill in the content with data from the network.

It fits single page apps well, because the shell rarely changes but the data changes all the time.

## 34: What does "offline first" mean?

Offline first means you design the app so it works without a network by default, and treat the network as a way to get updates. The app reads from local storage or cache first, shows that right away, and syncs with the server when it can.

It is the opposite of the usual approach, where the network is the main source and offline is an error case.

## 35: How do you show an offline page when there is no network?

Cache an `offline.html` page during install, and in the fetch handler return it when a page navigation fails.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request).catch(() => caches.match("/offline.html")),
    );
  }
});
```

This is the smallest useful offline support: users see your branded page instead of the browser's "no internet" screen.

## 36: What is the cache first strategy?

Look in the cache first. If there is a match, return it. If not, go to the network (and often store the result for next time).

```js
event.respondWith(
  caches.match(event.request).then((cached) => cached || fetch(event.request)),
);
```

It is fast and works offline. Use it for files that don't change, like versioned scripts, fonts and images.

## 37: What is the network first strategy?

Try the network first. If it fails or the user is offline, fall back to the cache.

```js
event.respondWith(
  fetch(event.request)
    .then((res) => {
      const copy = res.clone();
      caches.open("pages").then((c) => c.put(event.request, copy));
      return res;
    })
    .catch(() => caches.match(event.request)),
);
```

Use it for content that should be fresh when possible, like HTML pages or API data.

## 38: What is the stale-while-revalidate strategy?

Return the cached version right away (even if it may be old), and at the same time fetch a fresh copy from the network to update the cache for next time.

The user gets a fast response, and the content is never more than one visit out of date. Good for avatars, non-critical API data and CSS that changes sometimes.

## 39: What are the network only and cache only strategies?

- **Network only**: always go to the network, never use the cache. For things that must be live, like payments or analytics pings.
- **Cache only**: only read from the cache, never the network. For files you precached at install time and know are there.

These two are the simplest strategies, and in a real app you mix them with the others per type of request.

## 40: Why do you need to clone a response before caching it?

A `Response` body is a stream and can only be read once. If you put it in the cache and also return it to the page, both would try to read the same stream and one of them would fail.

`response.clone()` makes a copy, so one copy goes into the cache and the other goes to the page.

```js
const res = await fetch(event.request);
cache.put(event.request, res.clone());
return res;
```

## 41: What are the main events a service worker can listen to?

- `install` and `activate`: lifecycle.
- `fetch`: network requests from controlled pages.
- `message`: messages from pages via `postMessage`.
- `push`: a push message from the server.
- `notificationclick` and `notificationclose`: user interaction with notifications.
- `sync` and `periodicsync`: background sync (Chromium browsers).

There are a few more for less common APIs, like `backgroundfetchsuccess` and `paymentrequest`.

## 42: Can a service worker access the DOM?

No. It runs in a separate worker context with no `window` or `document`. If it needs to change something on the page, it sends a message to the page with `client.postMessage()`, and the page script updates the DOM.

It also can't use synchronous storage like `localStorage`. It can use IndexedDB and the Cache API.

## 43: What is self inside a service worker?

`self` is the global object of the service worker, a `ServiceWorkerGlobalScope`. You use it to add event listeners and to reach worker-only things like `self.registration`, `self.clients` and `self.skipWaiting()`.

```js
self.addEventListener("install", () => self.skipWaiting());
```

Writing `self.` makes it clear you mean the worker's global, not a variable.

## 44: Can you use localStorage in a service worker?

No. `localStorage` and `sessionStorage` are synchronous and only exist on `window`. Service workers must not block, so they only get async storage.

Use IndexedDB for structured data and the Cache API for responses. A small wrapper like the `idb` package makes IndexedDB much easier to use.

## 45: How do you check if a page is controlled by a service worker?

Look at `navigator.serviceWorker.controller`. It is the active worker that controls the current page, or `null` if there is none.

```js
if (navigator.serviceWorker.controller) {
  console.log("This page is controlled by a service worker");
}
```

It is `null` on the very first visit, because the page loaded before the worker was installed.

## 46: Why doesn't the service worker control the page on the first visit?

The page was already loaded from the network before the worker was registered and installed. By default a worker only controls pages that start loading after it is active, so the first page stays uncontrolled until the user navigates or reloads.

You can change that by calling `clients.claim()` in the `activate` event.

## 47: What does navigator.serviceWorker.ready return?

A promise that resolves with the `ServiceWorkerRegistration` once there is an active worker for the page's scope. It never rejects; it just waits.

```js
const reg = await navigator.serviceWorker.ready;
await reg.showNotification("Ready to go");
```

It is useful when you want to call something like `pushManager.subscribe()` and need an active worker first.

## 48: How do you unregister a service worker?

Get the registration and call `unregister()`.

```js
const regs = await navigator.serviceWorker.getRegistrations();
for (const reg of regs) await reg.unregister();
```

The worker keeps controlling open pages until they close or reload. Unregistering doesn't delete caches, so clear those separately if needed.

## 49: How can you see your service worker in Chrome DevTools?

Open DevTools, go to the **Application** panel, then **Service workers**. You can see the status, the scope, update or unregister it, and turn on "Update on reload" and "Offline".

The same panel has **Cache storage** to look at cached responses, **Storage** to see usage and clear everything, and **Manifest** to check the manifest and installability.

## 50: Can a service worker run when no tab of the site is open?

Yes, for certain events. The browser can start it to handle a push message, a background sync, or a periodic sync, even if all tabs are closed. It does the work and then gets stopped again.

It can't just run forever in the background. Browsers stop idle workers after a short time (about 30 seconds in Chrome) and limit how long one event can take.

## 51: What are the main benefits of a PWA?

- One codebase for web, desktop and mobile.
- Works offline or on slow networks with cached content.
- Can be installed without an app store, and updates the moment you deploy.
- Faster repeat visits because files come from the cache.
- Can use push notifications and some device features.
- Still a website: it has URLs, can be shared with a link and indexed by search engines.

## 52: What are the main limitations of PWAs?

- Browser support differs a lot, especially on iOS, where many APIs arrived late or are missing.
- Less access to device features than native apps (for example Bluetooth or NFC are Chromium only, and some things are not possible at all).
- Storage can be cleared by the browser under some conditions.
- Discovery through app stores is limited unless you wrap the PWA.
- Background work is restricted: no long-running background tasks.

## 53: What is the difference between a PWA and a native app?

A native app is built for one platform (Swift for iOS, Kotlin for Android), installed from an app store and has full access to the device. A PWA is a website built with web tech, installed from the browser and limited to what the browser allows.

PWAs are cheaper to build and update for many platforms. Native apps still win for heavy graphics, deep OS integration and some hardware features.

## 54: What is the difference between a PWA and a single page application?

They answer different questions. A single page application (SPA) is about how the app renders: one HTML page and JavaScript that swaps views. A PWA is about what the app can do: install, offline, push.

An SPA can be a PWA, a multi-page server-rendered site can also be a PWA, and an SPA without a manifest and service worker is not a PWA.

## 55: Does a PWA have to be a single page application?

No. Any website can be a PWA. A classic server-rendered site with many HTML pages can have a manifest and a service worker that caches pages and assets.

The app shell model fits SPAs best, but multi-page sites can use network first or stale-while-revalidate caching for pages and still work offline.

## 56: How do you know if the app is running as an installed PWA?

Use the `display-mode` media query. In CSS:

```css
@media (display-mode: standalone) {
  .install-button {
    display: none;
  }
}
```

In JavaScript:

```js
const isInstalled = window.matchMedia("(display-mode: standalone)").matches;
```

Older iOS Safari also exposes `navigator.standalone`, which is `true` when launched from the home screen.

## 57: What is the beforeinstallprompt event?

It is an event that Chromium browsers (Chrome, Edge, Samsung Internet) fire when the site meets the install rules. You can save it and later call `prompt()` on it to show the install dialog from your own button.

```js
let deferredPrompt;
window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;
  installButton.hidden = false;
});
```

Safari and Firefox don't fire this event, so you need other instructions for those users.

## 58: How do you show a custom install button?

Save the `beforeinstallprompt` event, show your button, and call `prompt()` when the user clicks it. The event can only be used once.

```js
installButton.addEventListener("click", async () => {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  console.log("User choice:", outcome); // 'accepted' or 'dismissed'
  deferredPrompt = null;
  installButton.hidden = true;
});
```

`prompt()` must be called from a user action like a click.

## 59: What is the appinstalled event?

`appinstalled` fires on `window` after the user installs the PWA, no matter whether they used your button or the browser's own UI.

```js
window.addEventListener("appinstalled", () => {
  installButton.hidden = true;
  analytics.track("pwa_installed");
});
```

It is good for hiding install promotions and tracking installs. It is supported in Chromium browsers.

## 60: How do you install a PWA on iPhone?

Open the site in Safari (or, since iOS 16.4, some other browsers too), tap the Share button, and choose "Add to Home Screen". There is no automatic install prompt and no `beforeinstallprompt` event on iOS.

Because of that, many sites show their own small hint that explains these steps to iOS users.

## 61: What is apple-touch-icon?

It is a `<link>` tag that sets the home screen icon on iOS. Newer Safari versions can read icons from the manifest, but adding this tag is still the safe choice.

```html
<link rel="apple-touch-icon" href="/icons/apple-touch-icon-180.png" />
```

A 180x180 PNG without transparency is the usual size. iOS adds its own rounded corners.

## 62: Can PWAs send push notifications on iOS?

Yes, since iOS and iPadOS 16.4 (2023). The catch is that it only works for web apps added to the home screen, not for the site in a Safari tab. The permission request must come from a user action like a button tap.

The code is the same standard Push API and Notifications API used in other browsers.

## 63: What is the Push API?

The Push API lets your server send a message to the user's browser through a push service, even when your site is not open. The browser wakes up your service worker and fires a `push` event.

The page subscribes with `registration.pushManager.subscribe()`, gets a subscription (an endpoint URL and keys), and sends it to your server. Your server later sends messages to that endpoint.

## 64: What is the Notifications API?

It is the API to show system notifications. From a service worker you use `self.registration.showNotification()`. From a page you first ask permission with `Notification.requestPermission()`.

```js
self.addEventListener("push", (event) => {
  const data = event.data?.json() ?? {};
  event.waitUntil(
    self.registration.showNotification(data.title ?? "New message", {
      body: data.body,
      icon: "/icons/icon-192.png",
    }),
  );
});
```

Push and notifications are two separate APIs that are usually used together.

## 65: How do you ask the user for notification permission?

Call `Notification.requestPermission()`, ideally after a click on a button that explains why, not on page load.

```js
enableButton.addEventListener("click", async () => {
  const permission = await Notification.requestPermission();
  if (permission === "granted") {
    // subscribe to push here
  }
});
```

The result is `'granted'`, `'denied'` or `'default'` (the user closed the prompt). Once a user denies, you can't ask again from code; they have to change it in browser settings.

## 66: Why shouldn't you ask for notification permission on page load?

Users don't know you yet and don't know what the notifications are for, so most of them say no. Once denied, you can't ask again. Browsers also punish this: Chrome shows quieter prompts for sites that many users block, and some browsers require a user gesture anyway.

Ask after the user does something that makes the value clear, like following an order or turning on an "alert me" switch.

## 67: What happens when the user clicks a notification?

The service worker gets a `notificationclick` event. Usually you close the notification and open or focus a page.

```js
self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  event.waitUntil(self.clients.openWindow("/inbox"));
});
```

If you don't handle this event, clicking the notification does nothing on most platforms.

## 68: What is IndexedDB and why is it used in PWAs?

IndexedDB is a database built into the browser. It stores structured data (objects, arrays, files, blobs) with indexes and transactions, and it works in both pages and service workers.

PWAs use it to keep app data offline: drafts, a list of products, messages waiting to be sent. The Cache API is for HTTP responses, and IndexedDB is for your own data.

## 69: What is the idb library?

`idb` is a small library by Jake Archibald that wraps IndexedDB with promises. The raw API is based on events and callbacks, which is hard to read.

```js
import { openDB } from "idb";

const db = await openDB("app-db", 1, {
  upgrade(db) {
    db.createObjectStore("drafts", { keyPath: "id" });
  },
});
await db.put("drafts", { id: 1, text: "Hello" });
const draft = await db.get("drafts", 1);
```

## 70: How do you detect if the user is online or offline?

Use `navigator.onLine` and the `online`/`offline` events.

```js
function updateStatus() {
  banner.hidden = navigator.onLine;
}
window.addEventListener("online", updateStatus);
window.addEventListener("offline", updateStatus);
updateStatus();
```

Note that `navigator.onLine === true` only means the device has a network connection, not that your server is reachable. A real request is the only sure test.

## 71: What is Lighthouse and how does it help with PWAs?

Lighthouse is Google's auditing tool, built into Chrome DevTools. It checks performance, accessibility, best practices and SEO.

It used to have a separate PWA category. That category was removed in Lighthouse 12 (2024), so today you check installability in the **Application > Manifest** panel of DevTools, while Lighthouse still helps with performance and best practices.

## 72: What is Workbox?

Workbox is a set of JavaScript libraries from the Chrome team that makes writing service workers easier. It gives you routing, ready caching strategies, precaching with versioning, expiration, background sync and more.

```js
import { registerRoute } from "workbox-routing";
import { CacheFirst } from "workbox-strategies";

registerRoute(
  ({ request }) => request.destination === "image",
  new CacheFirst({ cacheName: "images" }),
);
```

The current major version is Workbox 7.

## 73: What is precaching?

Precaching means downloading and caching a known list of files when the service worker installs, before the user needs them. This is usually the app shell: HTML, main JS and CSS, logo, offline page.

Tools like Workbox generate the list at build time, with a hash for each file, so only changed files are downloaded again on the next update.

## 74: What is runtime caching?

Runtime caching means caching responses while the app is used, as requests happen, instead of upfront. Images, API responses and pages the user visits get stored the first time and are served from cache later.

You pick a strategy (cache first, network first and so on) per type of request. It's the right choice for content you can't know at build time.

## 75: Why do you version cache names?

Because the old and new service workers can run side by side for a while. If both used one cache called `static`, the new version could overwrite files the old pages still need.

With names like `static-v1` and `static-v2`, the new worker fills its own cache in `install`, and only deletes `static-v1` in `activate`, once the old worker is gone.

## 76: How does the browser check for a new service worker?

When a page in the scope is loaded (a navigation), the browser downloads the worker script again and compares it byte by byte with the installed one. If anything is different, it installs the new version. It also checks on push and sync events if the last check was more than 24 hours ago.

You can trigger a check yourself with `registration.update()`.

## 77: What does skipWaiting do?

`self.skipWaiting()` tells a new worker to stop waiting and activate right away, even if old pages are still open.

```js
self.addEventListener("install", (event) => {
  self.skipWaiting();
});
```

It gets updates out faster, but pages that were loaded with the old version will now be served by the new worker, which can break things if the files changed a lot.

## 78: What does clients.claim do?

`self.clients.claim()` makes a newly activated worker take control of open pages in its scope right away, instead of waiting until they reload.

```js
self.addEventListener("activate", (event) => {
  event.waitUntil(self.clients.claim());
});
```

It is often used with `skipWaiting()` so the very first page load also gets offline support.

## 79: What is a client in service worker terms?

A client is a window, tab, or worker that the service worker can see and talk to, like an open page of your site. You get them with `self.clients.matchAll()`.

```js
const all = await self.clients.matchAll({ type: "window" });
all.forEach((client) => client.postMessage({ type: "NEW_DATA" }));
```

Each client has an `id`, a `url`, and for windows, methods like `focus()` and `navigate()`.

## 80: How does a page send a message to its service worker?

Use `postMessage` on the controller, or on the worker from the registration.

```js
navigator.serviceWorker.controller?.postMessage({ type: "CLEAR_CACHE" });
```

In the worker:

```js
self.addEventListener("message", (event) => {
  if (event.data?.type === "CLEAR_CACHE") {
    event.waitUntil(caches.delete("api-cache"));
  }
});
```

## 81: How does a service worker send a message to the page?

Find the client and call `postMessage` on it. The page listens on `navigator.serviceWorker`.

```js
// sw.js
const clientsList = await self.clients.matchAll();
clientsList.forEach((c) => c.postMessage({ type: "SYNC_DONE" }));
```

```js
// page
navigator.serviceWorker.addEventListener("message", (event) => {
  if (event.data.type === "SYNC_DONE") showToast("Saved");
});
```

## 82: What does the scope field in the manifest do?

The manifest `scope` defines which URLs are part of the installed app. If the user navigates outside it, the browser shows a URL bar or opens the link in a normal browser tab.

```json
{ "start_url": "/app/", "scope": "/app/" }
```

This is a different thing from the service worker scope, though in most apps both are `/`.

## 83: What is the id field in the manifest?

`id` gives the app a stable identity. Browsers use it to know that two manifests belong to the same installed app. If you don't set it, the browser uses `start_url`, so changing `start_url` later could look like a new, different app.

```json
{ "id": "/", "start_url": "/?source=pwa" }
```

Set `id` once and don't change it.

## 84: What are app shortcuts in the manifest?

Shortcuts are quick actions that show when the user long-presses (mobile) or right-clicks (desktop) the app icon.

```json
"shortcuts": [
  { "name": "New task", "url": "/tasks/new", "icons": [{ "src": "/icons/plus.png", "sizes": "96x96" }] },
  { "name": "Today", "url": "/tasks/today" }
]
```

They are supported in Chromium browsers on Android, Windows, macOS and ChromeOS. Safari ignores them.

## 85: What are description and screenshots used for in the manifest?

Chromium browsers use them to show a bigger, app-store-like install dialog with a description and pictures of the app.

```json
"description": "Track your daily tasks.",
"screenshots": [
  { "src": "/shots/phone.png", "sizes": "1080x1920", "type": "image/png", "form_factor": "narrow" },
  { "src": "/shots/desktop.png", "sizes": "1920x1080", "type": "image/png", "form_factor": "wide" }
]
```

`form_factor` tells which screenshots to show on mobile (`narrow`) and desktop (`wide`).

## 86: What does the orientation field in the manifest do?

It sets the default screen orientation for the installed app, for example `portrait` or `landscape`. It is mostly useful for games or apps that only make sense in one direction.

```json
{ "orientation": "portrait" }
```

Desktop browsers ignore it, and you should only lock orientation when you really need to, since users on tablets often rotate.

## 87: What is the Web Share API?

It lets your page open the device's native share sheet, so the user can send a link or text to other apps.

```js
shareButton.addEventListener("click", async () => {
  if (navigator.share) {
    await navigator.share({ title: document.title, url: location.href });
  }
});
```

It needs HTTPS and a user action. It is supported on most mobile browsers and on desktop Chrome, Edge and Safari.

## 88: What is the Badging API?

It lets an installed app show a number or dot on its icon, like an unread count.

```js
if ("setAppBadge" in navigator) {
  navigator.setAppBadge(5);
  // later
  navigator.clearAppBadge();
}
```

It works for installed PWAs in Chromium browsers on desktop and in Safari on iOS (home screen apps) and macOS. It can be called from the page or the service worker.

## 89: Can a PWA be published in app stores?

Yes, with some work. On Google Play you can wrap it in a Trusted Web Activity (TWA), for example using Bubblewrap or PWABuilder. The Microsoft Store accepts PWAs directly. For the Apple App Store you need a native wrapper app, and Apple may reject apps that are only a website in a shell.

## 90: What is a Trusted Web Activity?

A Trusted Web Activity is an Android way to show your PWA full screen inside an Android app, using Chrome (or another supporting browser) as the engine. It is how you put a PWA on Google Play.

To prove you own the site, you publish a Digital Asset Links file at `/.well-known/assetlinks.json`. Without it, the app shows a URL bar.

## 91: What is PWABuilder?

PWABuilder is a free tool, started by Microsoft, that checks a PWA's manifest and service worker and creates packages for app stores: Google Play (TWA), Microsoft Store, and an iOS wrapper project.

It is a quick way to see what your PWA is missing and to get store packages without writing native code.

## 92: What does a service worker do with requests to other domains?

The fetch event fires for cross-origin requests too, like images from a CDN or calls to another API. You can respond from cache or let them through.

Cross-origin requests without CORS give you an "opaque" response: you can store and return it, but you can't read its status or body. That has some side effects for caching, covered later.

## 93: What is an opaque response?

It is the response you get when you fetch a cross-origin resource with `mode: 'no-cors'` (which is what `<img>` and `<script>` do without the `crossorigin` attribute). The status shows as `0`, and headers and body are hidden from your code.

You can still put it in the cache and return it to the page, but you can't tell if it was a success or an error.

## 94: What are the most common reasons a site is not installable?

- Not served over HTTPS.
- No manifest link, or the manifest has JSON errors.
- Missing `name` or `short_name`, or missing a 192px and 512px icon.
- `display` set to `browser`.
- `start_url` outside the scope.
- In older Chrome versions, no service worker with a fetch handler.

The DevTools **Application > Manifest** panel lists these problems for you.

## 95: How do you test a PWA offline?

In Chrome DevTools, open **Application > Service workers** and tick **Offline**, or set the **Network** panel throttling to **Offline**. Then reload and click around.

Also test on a real phone in airplane mode. Real devices show problems DevTools doesn't, like a slow start or the OS killing the app.

## 96: What is "Update on reload" in DevTools?

It is a checkbox in **Application > Service workers**. When on, every reload installs and activates the latest worker right away, skipping the waiting phase.

It saves a lot of time during development. Remember it is only for you; real users go through the normal update flow.

## 97: What does "Bypass for network" do in DevTools?

It makes the browser skip the service worker for requests, so everything goes straight to the network. The worker is still installed, it just doesn't handle fetches.

Use it when you're debugging something that isn't related to the worker and you don't want cached files in the way.

## 98: Are PWAs good for SEO?

A PWA is still a website, so it can be indexed like any other site. The service worker doesn't change what search engines see, because crawlers usually don't run it.

The SEO risks come from how the app renders, not from it being a PWA. A client-side rendered SPA with no server rendering can be harder to index. A fast PWA can also help with Core Web Vitals.

## 99: What is navigator.storage.estimate?

It returns how much storage your origin is using and how much the browser allows it to use.

```js
const { usage, quota } = await navigator.storage.estimate();
console.log(
  `Using ${(usage / 1e6).toFixed(1)} MB of ${(quota / 1e6).toFixed(0)} MB`,
);
```

The numbers are estimates and may be padded for privacy, but they help you decide when to clean up old caches.

## 100: Can the browser delete a PWA's cached data?

Yes. By default storage is "best effort": when the device runs low on space, the browser can clear an origin's data (caches, IndexedDB) starting with the least recently used sites. Users can also clear it.

You can ask for persistent storage with `navigator.storage.persist()`, which makes the browser much less likely to clear it. Safari also has its own rules, explained later.

## 101: How do you request persistent storage?

Call `navigator.storage.persist()`. It returns `true` if the browser agreed.

```js
if (navigator.storage?.persist) {
  const persisted = await navigator.storage.persist();
  console.log("Persistent storage:", persisted);
}
```

Chrome decides on its own, based on things like whether the site is installed or bookmarked, and doesn't show a prompt. Firefox may ask the user. You can check the current state with `navigator.storage.persisted()`.

## 102: How do you delete a cache or one entry from it?

```js
// delete a whole cache
await caches.delete("images-v1");

// delete one entry
const cache = await caches.open("images-v1");
await cache.delete("/img/old-banner.png");
```

Both return `true` if something was deleted. `caches.keys()` lists all cache names, and `cache.keys()` lists all requests in one cache.

## 103: What does the ignoreSearch option do in cache.match?

By default `cache.match` needs the URL to match exactly, including the query string. With `ignoreSearch: true`, it ignores the query part.

```js
// matches /article.html?utm_source=mail as /article.html
const res = await caches.match(event.request, { ignoreSearch: true });
```

Useful when links come with tracking parameters but the page is the same. There are also `ignoreMethod` and `ignoreVary` options.

## 104: What is request.mode === 'navigate'?

It is how you tell in a fetch handler that the request is for a whole page (the user clicked a link, typed a URL or reloaded), not for an image or script inside a page.

```js
if (event.request.mode === "navigate") {
  // handle page loads, for example with network first + offline page
}
```

Navigation requests usually need a different strategy from static files.

## 105: What is request.destination?

It tells what the request is for: `'document'`, `'script'`, `'style'`, `'image'`, `'font'`, `'manifest'`, and so on. An empty string means a `fetch()` or XHR call.

```js
if (event.request.destination === "image") {
  event.respondWith(cacheFirst(event.request));
}
```

It is a cleaner way to pick a strategy than checking file extensions.

## 106: How do you skip non-GET requests in the fetch handler?

The Cache API only stores GET requests, and POST or PUT calls usually should go straight to the server. Just return without calling `respondWith`.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  // caching logic for GET requests
});
```

The browser then handles the request as if there were no service worker.

## 107: What is importScripts?

`importScripts()` loads other scripts into a classic service worker, synchronously.

```js
importScripts("/js/helpers.js", "/js/routes.js");
```

It must be called while the worker script first runs (top level), not later inside events. Imported scripts are checked for updates too. In module service workers you use `import` instead.

## 108: Can a service worker be an ES module?

Yes. Register it with `type: 'module'` and use normal `import` statements.

```js
navigator.serviceWorker.register("/sw.js", { type: "module" });
```

Chromium and Safari support this. Firefox added support only recently (around version 147), so many projects still bundle the worker into one classic script for safety. Dynamic `import()` is not allowed in service workers.

## 109: What HTTP caching header should sw.js have?

Serve the service worker file with `Cache-Control: no-cache` (or a short `max-age`). Browsers already ignore the HTTP cache for the worker script by default since about 2018 (the `updateViaCache` default is `'imports'`), but a CDN in front of your server can still cache it.

If the file is cached for a long time somewhere, users may not get your fix for a broken worker.

## 110: Should you rename sw.js on every deploy, like sw-v2.js?

No. Keep the same URL forever. The browser finds updates by checking the same script URL. If you rename it, the old page (which may be cached by the old worker) still registers the old name, and users can get stuck on the old version.

Change the contents of the file instead. A build tool usually does this by adding a new precache manifest with new hashes.

## 111: What is the Service-Worker-Allowed header?

It is a response header on the worker script that lets the worker have a scope wider than its own folder.

```
Service-Worker-Allowed: /
```

With that header, `/js/sw.js` can be registered with `{ scope: '/' }`. Without it, the browser rejects the registration with a security error.

## 112: How do you set a custom scope when registering?

Pass `scope` in the options.

```js
navigator.serviceWorker.register("/sw.js", { scope: "/app/" });
```

The scope can be narrower than the script's folder without any header. You can even have several service workers on one origin with different scopes, each controlling its own part of the site.

## 113: What happens if two service workers have overlapping scopes?

For each page, the browser picks the registration with the longest matching scope. If you have one at `/` and one at `/admin/`, pages under `/admin/` are controlled by the second, and all other pages by the first.

A page is only ever controlled by one service worker.

## 114: What does a service worker do if it throws an error during install?

The install fails, the new worker becomes `redundant`, and the old worker (if any) keeps running. The browser will try again on the next navigation or update check.

This is why a missing file in `cache.addAll()` is serious: it breaks every install until you fix it.

## 115: Do service workers work in private or incognito windows?

In Chrome, yes, but everything is thrown away when the incognito session ends. In Firefox private windows, service workers were disabled for a long time; newer versions are adding support. Safari supports them in private browsing with temporary storage.

Don't count on offline support in private mode.

## 116: What is the difference between Background Sync and normal fetch?

With normal `fetch`, if the user is offline, the request fails and your code has to handle it. With Background Sync, you register a "sync" with a tag, and the browser fires a `sync` event in your service worker when the connection comes back, even if the user already closed the tab.

It is supported in Chromium browsers only, so you need a fallback, like retrying when the app opens again.

## 117: How do you register a background sync?

```js
// page
const reg = await navigator.serviceWorker.ready;
if ("sync" in reg) {
  await reg.sync.register("send-messages");
}
```

```js
// sw.js
self.addEventListener("sync", (event) => {
  if (event.tag === "send-messages") {
    event.waitUntil(sendQueuedMessages());
  }
});
```

`sendQueuedMessages` would read pending items from IndexedDB and post them to the server.

## 118: What is Periodic Background Sync?

It lets an installed PWA ask the browser to wake its service worker now and then (for example once a day) to fetch fresh content, so the app has new data when opened.

```js
const reg = await navigator.serviceWorker.ready;
await reg.periodicSync.register("refresh-news", {
  minInterval: 24 * 60 * 60 * 1000,
});
```

It works only in Chromium, only for installed apps, and the browser decides the real timing based on how much the user uses the site.

## 119: What are notification options like body, icon, badge and tag?

- `body`: the text under the title.
- `icon`: the image shown in the notification.
- `badge`: a small one-color icon shown in the Android status bar.
- `tag`: an ID. A new notification with the same tag replaces the old one instead of stacking.
- `data`: any data you want in `notificationclick`, like a URL to open.

```js
self.registration.showNotification("New reply", {
  body: "Anna replied to your post",
  icon: "/icons/icon-192.png",
  badge: "/icons/badge-72.png",
  tag: "post-42",
  data: { url: "/posts/42" },
});
```

## 120: What are notification actions?

Actions are buttons shown inside the notification. The `notificationclick` event tells you which one was pressed through `event.action`.

```js
self.registration.showNotification("Meeting in 10 minutes", {
  actions: [
    { action: "join", title: "Join" },
    { action: "snooze", title: "Snooze" },
  ],
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  if (event.action === "join") event.waitUntil(clients.openWindow("/meeting"));
});
```

Support depends on the platform; Chromium shows them, Safari doesn't. Check `Notification.maxActions`.

## 121: What is VAPID?

VAPID (Voluntary Application Server Identification) is a key pair your server uses to identify itself to push services. You put the public key in `pushManager.subscribe()`, and the server signs each push with the private key.

It means only your server can send pushes to subscriptions it created. You generate the keys once, for example with the `web-push` npm package: `npx web-push generate-vapid-keys`.

## 122: What does userVisibleOnly mean in pushManager.subscribe?

It is a promise from you that every push message will show a notification to the user. Chrome requires `userVisibleOnly: true`; silent pushes that do work in the background without telling the user are not allowed.

```js
const sub = await reg.pushManager.subscribe({
  userVisibleOnly: true,
  applicationServerKey: VAPID_PUBLIC_KEY,
});
```

If your push handler often doesn't show a notification, Chrome shows a default one for you.

## 123: Do you need Firebase to send web push?

No. Web push is an open standard. Each browser has its own push service (Google's FCM for Chrome, Mozilla's autopush for Firefox, Apple's for Safari), and your server sends to whatever endpoint the subscription gives, using VAPID.

Firebase Cloud Messaging is one option that adds its own SDK on top, but the `web-push` npm package with VAPID keys works for all browsers.

## 124: How do you send a push message from Node.js?

Use the `web-push` package with your VAPID keys and a saved subscription.

```js
import webpush from "web-push";

webpush.setVapidDetails(
  "mailto:admin@example.com",
  process.env.VAPID_PUBLIC_KEY,
  process.env.VAPID_PRIVATE_KEY,
);

await webpush.sendNotification(
  subscription,
  JSON.stringify({
    title: "Order shipped",
    body: "Your order #1234 is on its way",
  }),
);
```

`subscription` is the JSON object the browser gave you from `pushManager.subscribe()`.

## 125: How does a user uninstall a PWA?

The same way as other apps on that system: long-press the icon and remove it on Android and iOS, or right-click it on desktop. In Chrome and Edge on desktop you can also open the app and choose "Uninstall" from its menu, or go to `chrome://apps`.

Uninstalling the app doesn't always clear the site's data; the user may need to clear site data in the browser too.

## 126: How does an installed PWA get updated?

The code updates like any website. The next time the app is opened and the service worker sees a new version on the server, it installs it. Users get the new code once the new worker activates.

The manifest (name, icons, colors) is also checked again by the browser from time to time, and Chrome updates the installed app's details. There is no app store review step.

## 127: How do you build a Response by hand in a service worker?

Create a `new Response(body, options)`.

```js
event.respondWith(
  new Response(JSON.stringify({ error: "offline" }), {
    status: 503,
    headers: { "Content-Type": "application/json" },
  }),
);
```

This is handy for offline API fallbacks or for small generated files. `Response.json()` is a newer shortcut for JSON bodies.

## 128: Does the fetch event catch XMLHttpRequest calls?

Yes. Requests from `XMLHttpRequest`, `fetch()`, `<img>`, `<script>`, `<link>`, CSS `url()`, fonts and iframes in a controlled page all go through the service worker's fetch event.

The exceptions include requests made by the service worker itself, and some special cases like `<a download>`, which can behave differently between browsers.

## 129: What are common real-world examples of PWAs?

Well-known cases include X (Twitter) Lite, Starbucks' ordering app, Pinterest, Spotify's web player, Uber's light web app, Google Maps Go, Microsoft Teams, Outlook and Photoshop on the web. Many of them reported faster loads, higher engagement or much smaller download sizes than their native apps.

## 130: How do you add PWA support with Vite?

The common way is `vite-plugin-pwa`, which uses Workbox under the hood. It generates the manifest and service worker and adds the registration code.

```js
// vite.config.js
import { VitePWA } from "vite-plugin-pwa";

export default {
  plugins: [
    VitePWA({
      registerType: "autoUpdate",
      manifest: { name: "My App", short_name: "App", theme_color: "#1e88e5" },
    }),
  ],
};
```

## 131: How do you add a service worker to an Angular app?

Run `ng add @angular/pwa`. It installs `@angular/service-worker`, adds a `manifest.webmanifest`, icons, and an `ngsw-config.json` that describes what to cache. Angular builds a service worker (`ngsw-worker.js`) from that config.

You can listen for updates in code with the `SwUpdate` service, and for push with `SwPush`.

## 132: How do you add a service worker to a Next.js app?

Next.js doesn't ship a built-in service worker generator. The common choices are Serwist (`@serwist/next`), which is a maintained fork of Workbox ideas, or writing your own `sw.js` in the `public` folder and registering it from a client component.

`next-pwa` was popular earlier but is no longer actively maintained, so newer projects tend to use Serwist.

## 133: Can you test a service worker on a phone over a local network IP?

Not over plain HTTP. `http://192.168.1.10:3000` is not a secure context, so service workers won't register. Only `localhost` gets that exception.

Options: use Chrome's remote debugging with port forwarding so the phone uses `localhost`, use a tunnel like ngrok or Cloudflare Tunnel that gives you HTTPS, or set up a local certificate with a tool like mkcert.

## 134: Can a normal page use the Cache API?

Yes. `window.caches` is available in secure contexts, so the page can open caches, add files and read them without a service worker.

A common use is a "Save for offline" button that adds an article's URL and images to a cache, which the service worker then serves when offline.

## 135: What is the difference between a manifest's display and display_override?

`display_override` is a list of display modes to try in order, before falling back to `display`. It lets you use newer modes like `window-controls-overlay` or `tabbed` without breaking older browsers.

```json
{
  "display_override": ["window-controls-overlay", "standalone"],
  "display": "standalone"
}
```

Browsers that don't know `display_override` just use `display`.

## 136: What is a splash screen in a PWA?

It is the screen shown while the installed app launches. On Android, Chrome builds it from the manifest: `name`, `background_color`, `theme_color` and a large icon.

iOS doesn't build one from the manifest. You add `<link rel="apple-touch-startup-image">` tags with images for each screen size, which is why many teams use a generator for them.

## 137: What does the categories field in the manifest do?

It is a list of hints about what kind of app it is, like `["productivity", "business"]`. App stores and catalogs can use it for grouping. Browsers mostly ignore it today, so it is optional.

## 138: What is related_applications in the manifest?

It lists native apps that belong to the same product, for example your Android app on Google Play.

```json
"related_applications": [
  { "platform": "play", "id": "com.example.tasks" }
],
"prefer_related_applications": false
```

If `prefer_related_applications` is `true`, Chrome may offer the native app instead of installing the PWA.

## 139: What is navigator.getInstalledRelatedApps?

It lets a page check whether the user already has your native app or PWA installed, so you can hide the install banner or deep link into the app.

```js
if ("getInstalledRelatedApps" in navigator) {
  const apps = await navigator.getInstalledRelatedApps();
  if (apps.length) installBanner.hidden = true;
}
```

It only works in Chromium browsers and only for apps listed in `related_applications` that also prove the link back to your site.

## 140: What is the share_target field in the manifest?

It makes an installed PWA show up in the system share sheet as a target, so other apps can share text, links or files into it.

```json
"share_target": {
  "action": "/share",
  "method": "GET",
  "params": { "title": "title", "text": "text", "url": "url" }
}
```

It works on Android and ChromeOS in Chromium browsers. For files, you use `POST` and `multipart/form-data`, and the service worker usually reads the form data.

## 141: What is the file_handlers field in the manifest?

It lets an installed desktop PWA register as an app that can open certain file types, so users can double-click a file and open it in your app.

```json
"file_handlers": [
  { "action": "/open", "accept": { "text/csv": [".csv"] } }
]
```

The page reads the files with `window.launchQueue`. It is supported in Chromium on desktop.

## 142: What is the protocol_handlers field in the manifest?

It registers the PWA to handle custom link schemes, like `web+tasks://` or standard ones like `mailto:`.

```json
"protocol_handlers": [
  { "protocol": "web+tasks", "url": "/open?link=%s" }
]
```

When the user clicks such a link, the app opens at that URL with `%s` replaced by the full link. Custom schemes must start with `web+`.

## 143: Why must start_url work offline?

If the user taps the app icon while offline and `start_url` isn't cached, they see the browser's error page. That feels broken for something that looks like an installed app.

Make sure `start_url` (with any query parameters) is precached, or that your fetch handler returns the cached shell for navigations, so the app always opens.

## 144: Do you still need the apple-mobile-web-app-capable meta tag?

Not really. Modern Safari reads `display` from the manifest. The old `apple-mobile-web-app-capable` tag still works, and Apple and other browsers also understand the newer `mobile-web-app-capable` name.

Some teams keep the meta tags for older iOS versions, along with `apple-mobile-web-app-status-bar-style` to set the status bar look.

## 145: What viewport settings does a PWA need?

The same as any mobile-friendly site:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

For full screen layouts on phones with notches, add `viewport-fit=cover` and use CSS `env(safe-area-inset-top)` and friends to keep content out of the notch area.

## 146: How do you clear everything a service worker stored while developing?

In Chrome DevTools, go to **Application > Storage** and click **Clear site data**. This removes the service worker registration, caches, IndexedDB, cookies and local storage for that origin.

From code, you can unregister workers and delete all caches, or send a `Clear-Site-Data: "cache", "storage"` header from the server.

## 147: Can a service worker read cookies?

Not through `document.cookie`, since there is no document. Requests made with `fetch` from the worker still send cookies as normal, depending on the `credentials` setting.

The Cookie Store API (`cookieStore.get()`, `cookieStore.set()`) also works in service workers, and a worker can listen for cookie changes after calling `registration.cookies.subscribe()`. Support is best in Chromium; check Safari and Firefox before relying on it.

## 148: Can you use fetch inside a service worker?

Yes. `fetch()` is available and is how the worker gets network responses. Requests made by the worker itself do not trigger its own fetch event, so there is no infinite loop.

```js
const response = await fetch(event.request);
```

You can also fetch other URLs, for example to warm the cache with data the user will probably need next.

## 149: What does it mean that a service worker is event-driven?

It doesn't run code in a loop. It wakes up for an event (fetch, push, sync, message), runs your handler, and goes back to sleep. Global variables can be lost between events because the browser can kill and restart the worker at any time.

So any state you need later must be stored in IndexedDB or the Cache API, not in a variable.

## 150: What is a good first checklist for turning a site into a PWA?

1. Serve the site over HTTPS.
2. Make it responsive and mobile friendly.
3. Add a manifest with `name`, `short_name`, `start_url`, `display`, colors and 192/512 icons, including a maskable one.
4. Register a service worker that caches the app shell and an offline page.
5. Make sure `start_url` loads offline.
6. Check installability in DevTools and test on real Android and iOS devices.

# Moderate Questions (151-300)

## 151: What are registration.installing, waiting and active?

A `ServiceWorkerRegistration` has three slots for workers in different states:

- `installing`: a worker that is running its `install` event right now.
- `waiting`: a worker that finished installing but is waiting for old pages to close.
- `active`: the worker that is handling events.

Each is a `ServiceWorker` object or `null`. You look at them to build update UIs, for example "if `waiting` is set, show a Reload button".

## 152: How do you detect that a new service worker version was found?

Listen for `updatefound` on the registration, then watch the installing worker's `statechange`.

```js
const reg = await navigator.serviceWorker.register("/sw.js");
reg.addEventListener("updatefound", () => {
  const newWorker = reg.installing;
  newWorker.addEventListener("statechange", () => {
    if (newWorker.state === "installed" && navigator.serviceWorker.controller) {
      showUpdateBanner(); // a new version is waiting
    }
  });
});
```

Checking `controller` tells apart the first install from a real update.

## 153: How do you build a "New version available, reload" flow?

1. Detect a waiting worker (from `updatefound` or `reg.waiting` on load).
2. Show a banner. When the user clicks it, send the waiting worker a message.
3. In the worker, call `skipWaiting()` on that message.
4. In the page, reload once the controller changes.

```js
// page
reloadButton.onclick = () => reg.waiting?.postMessage({ type: "SKIP_WAITING" });
navigator.serviceWorker.addEventListener("controllerchange", () =>
  location.reload(),
);
```

```js
// sw.js
self.addEventListener("message", (e) => {
  if (e.data?.type === "SKIP_WAITING") self.skipWaiting();
});
```

## 154: Why can calling skipWaiting automatically be risky?

The page was loaded with the old HTML and maybe lazy loads old JS chunks by hash. After `skipWaiting`, the new worker controls the page and may have deleted the old cache. When the page then asks for `chunk-abc123.js`, it isn't in the new cache and may not exist on the server anymore, so the app breaks.

It is safe when your pages don't depend on files the new version removed, or when you reload the page right after the new worker takes over.

## 155: What is the controllerchange event?

It fires on `navigator.serviceWorker` when the page gets a new controlling worker, either because a new one activated and claimed the page, or because the first worker claimed it.

The common use is reloading after an update. Guard it so it only reloads once, and skip it on the first install if you don't want a reload then.

```js
let refreshing = false;
navigator.serviceWorker.addEventListener("controllerchange", () => {
  if (refreshing) return;
  refreshing = true;
  location.reload();
});
```

## 156: How do you check for updates in a long-lived single page app?

The browser only checks on navigations, and an SPA may stay open for days without one. Call `registration.update()` yourself from time to time or when the tab becomes visible again.

```js
const reg = await navigator.serviceWorker.ready;
setInterval(() => reg.update(), 60 * 60 * 1000);
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "visible") reg.update();
});
```

## 157: What does updateViaCache do?

It is a registration option that says whether the browser's HTTP cache may be used when checking the worker script for updates.

- `'imports'` (default): the main `sw.js` always skips the HTTP cache, but scripts loaded with `importScripts` may use it.
- `'all'`: both may use the HTTP cache.
- `'none'`: neither uses it.

```js
navigator.serviceWorker.register("/sw.js", { updateViaCache: "none" });
```

`'none'` is useful if your imported scripts don't have hashed names.

## 158: How do you make an SPA's routes work offline?

All app routes (`/tasks`, `/tasks/42`, `/settings`) are really the same `index.html`. In the fetch handler, answer navigation requests with the cached shell.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.mode === "navigate") {
    event.respondWith(
      fetch(event.request).catch(() => caches.match("/index.html")),
    );
  }
});
```

Exclude routes that are not part of the SPA, like `/api/` or `/admin/` served by the server, so you don't return the shell for them.

## 159: What is navigation preload?

When a page navigation happens and the service worker is not running, the browser has to start it before your fetch handler can even begin the network request. That boot time can be 50 ms or more on slow phones.

Navigation preload tells the browser to start the network request in parallel with the worker boot. Your handler then uses `event.preloadResponse` instead of starting a new fetch.

## 160: How do you enable and use navigation preload?

```js
self.addEventListener("activate", (event) => {
  event.waitUntil(self.registration.navigationPreload?.enable());
});

self.addEventListener("fetch", (event) => {
  if (event.request.mode !== "navigate") return;
  event.respondWith(
    (async () => {
      const preloaded = await event.preloadResponse;
      if (preloaded) return preloaded;
      try {
        return await fetch(event.request);
      } catch {
        return caches.match("/offline.html");
      }
    })(),
  );
});
```

Preload requests have a `Service-Worker-Navigation-Preload: true` header, which your server can use to send a lighter response. It is only worth enabling when you go to the network for navigations.

## 161: How do you add a timeout to a network first strategy?

Race the fetch against a timer and fall back to cache if the network is too slow.

```js
async function networkFirst(request, timeoutMs = 3000) {
  const cache = await caches.open("pages");
  const timeout = new Promise((resolve) =>
    setTimeout(async () => resolve(await cache.match(request)), timeoutMs),
  );
  const network = fetch(request).then((res) => {
    cache.put(request, res.clone());
    return res;
  });
  const fallback = network.catch(() => cache.match(request));
  const result = await Promise.race([fallback, timeout]);
  return result || (await fallback) || Response.error();
}
```

If the timer wins but there is no cached copy, we still wait for the network. If the network fails, we use the cache, and if both are empty we return a network error. Workbox has this built in as `networkTimeoutSeconds`.

## 162: How do you write stale-while-revalidate by hand?

```js
async function staleWhileRevalidate(event) {
  const cache = await caches.open("swr");
  const cached = await cache.match(event.request);
  const networkPromise = fetch(event.request).then((res) => {
    if (res.ok) cache.put(event.request, res.clone());
    return res;
  });
  event.waitUntil(networkPromise.catch(() => {}));
  return cached || networkPromise;
}

self.addEventListener("fetch", (event) => {
  if (event.request.destination === "style") {
    event.respondWith(staleWhileRevalidate(event));
  }
});
```

`waitUntil` keeps the worker alive until the background update finishes.

## 163: Why should you avoid caching error responses?

If the server returns a 500 or 404 once and you cache it with cache first, users get that error from cache over and over, even after the server is fixed. Always check before storing.

```js
if (response.ok) cache.put(request, response.clone());
```

For opaque responses, `ok` is `false` and status is `0`, so you have to decide on purpose whether to cache those.

## 164: How do you limit the size of a runtime cache?

The Cache API has no size limit or expiry. You have to trim it yourself, for example by keeping only the newest N entries.

```js
async function trimCache(name, maxItems) {
  const cache = await caches.open(name);
  const keys = await cache.keys();
  for (let i = 0; i < keys.length - maxItems; i++) {
    await cache.delete(keys[i]);
  }
}
```

`cache.keys()` returns entries in insertion order, so this removes the oldest. Workbox's `ExpirationPlugin` does this with `maxEntries` and `maxAgeSeconds`.

## 165: What is QuotaExceededError and how do you handle it?

It is thrown when a write to Cache Storage or IndexedDB would go over the origin's quota. If you don't catch it, a `cache.put` inside your fetch handler can reject and break responses.

Catch it, clear less important caches (old images, old API data), and try again or just skip caching. Workbox's `ExpirationPlugin` has `purgeOnQuotaError: true` for this.

## 166: Why do opaque responses use so much quota?

Browsers don't let you see the real size of an opaque response, because that could leak information about another site. So Chrome counts each opaque response as a padded size, around 7 MB, no matter how small it really is.

A few hundred cached cross-origin images without CORS can eat your whole quota. Request them with CORS (`crossorigin` attribute and the right server headers) so they are not opaque, or limit how many you cache.

## 167: What are the main Workbox packages?

- `workbox-routing`: match requests to handlers.
- `workbox-strategies`: `CacheFirst`, `NetworkFirst`, `StaleWhileRevalidate`, `NetworkOnly`, `CacheOnly`.
- `workbox-precaching`: precache files with revisions.
- `workbox-expiration`: limit caches by count and age.
- `workbox-cacheable-response`: decide which responses to cache.
- `workbox-background-sync`: retry failed requests later.
- `workbox-broadcast-update`: tell pages when cached content changed.
- `workbox-recipes`: common setups in one call.
- `workbox-window`: helpers for the page side, like update handling.

## 168: What is the difference between generateSW and injectManifest in Workbox?

- **generateSW**: Workbox writes the whole service worker for you from a config (precache patterns, runtime caching rules). Quick, but you can't add custom code beyond what the config allows.
- **injectManifest**: you write your own `sw.js`, and Workbox only injects the precache list where you put `self.__WB_MANIFEST`. Use it when you need push, custom routes or other logic.

Most apps start with generateSW and switch to injectManifest once they need custom features.

## 169: What does self.__WB_MANIFEST do?

It is a placeholder in your source worker that the Workbox build step replaces with the list of files to precache, each with a URL and a revision.

```js
import { precacheAndRoute, cleanupOutdatedCaches } from "workbox-precaching";

cleanupOutdatedCaches();
precacheAndRoute(self.__WB_MANIFEST);
```

After the build, it becomes something like `[{ url: '/index.html', revision: 'a1b2c3' }, ...]`. Files with a hash in their name get `revision: null`.

## 170: How does Workbox precaching know which files changed?

Each entry in the precache manifest has a revision, usually a hash of the file's contents. Workbox stores the revision with the cached file. On the next install, it only downloads entries whose URL or revision changed and keeps the rest.

That makes updates small: changing one CSS file downloads one file, not the whole app.

## 171: How do you set up runtime caching with Workbox?

```js
import { registerRoute } from "workbox-routing";
import { StaleWhileRevalidate, CacheFirst } from "workbox-strategies";
import { ExpirationPlugin } from "workbox-expiration";

registerRoute(
  ({ url }) => url.pathname.startsWith("/api/products"),
  new StaleWhileRevalidate({ cacheName: "api-products" }),
);

registerRoute(
  ({ request }) => request.destination === "image",
  new CacheFirst({
    cacheName: "images",
    plugins: [
      new ExpirationPlugin({ maxEntries: 100, maxAgeSeconds: 30 * 24 * 3600 }),
    ],
  }),
);
```

Routes are checked in the order they are registered, and the first match wins.

## 172: What does the CacheableResponsePlugin do?

It controls which responses a strategy is allowed to cache, by status code or headers.

```js
import { CacheableResponsePlugin } from "workbox-cacheable-response";

new CacheFirst({
  cacheName: "cdn",
  plugins: [new CacheableResponsePlugin({ statuses: [0, 200] })],
});
```

Including `0` allows opaque responses. By default, `CacheFirst` and `NetworkFirst` only cache 200 responses, while `StaleWhileRevalidate` also caches opaque ones.

## 173: How do you add an offline fallback page in Workbox?

The easiest way is the `offlineFallback` recipe, which precaches the page and uses it when a navigation fails.

```js
import { offlineFallback } from "workbox-recipes";
import { setDefaultHandler } from "workbox-routing";
import { NetworkOnly } from "workbox-strategies";

setDefaultHandler(new NetworkOnly());
offlineFallback({ pageFallback: "/offline.html" });
```

It can also take `imageFallback` and `fontFallback`. Under the hood it uses `setCatchHandler`.

## 174: What is setCatchHandler in Workbox?

It sets a handler that runs when any route's handler throws, for example when the network is down and nothing is cached. You decide what to return based on the request.

```js
import { setCatchHandler } from "workbox-routing";
import { matchPrecache } from "workbox-precaching";

setCatchHandler(async ({ request }) => {
  if (request.destination === "document") return matchPrecache("/offline.html");
  if (request.destination === "image") return matchPrecache("/img/offline.svg");
  return Response.error();
});
```

## 175: How do you handle SPA navigation in Workbox?

Use a `NavigationRoute` that returns the precached `index.html` for navigations, with a denylist for paths the server handles.

```js
import { NavigationRoute, registerRoute } from "workbox-routing";
import { createHandlerBoundToURL } from "workbox-precaching";

registerRoute(
  new NavigationRoute(createHandlerBoundToURL("/index.html"), {
    denylist: [/^\/api\//, /^\/admin\//],
  }),
);
```

`index.html` must be in the precache list for this to work.

## 176: What is workbox-window?

It is a small library for the page side. It registers the worker and gives you clear events for the update flow.

```js
import { Workbox } from "workbox-window";

const wb = new Workbox("/sw.js");
wb.addEventListener("waiting", () => {
  if (confirm("New version available. Reload?")) {
    wb.addEventListener("controlling", () => location.reload());
    wb.messageSkipWaiting();
  }
});
wb.register();
```

`messageSkipWaiting()` sends `{ type: 'SKIP_WAITING' }`, which Workbox-built workers understand.

## 177: How do you queue failed POST requests with Workbox?

Use the `BackgroundSyncPlugin` on a `NetworkOnly` route. Failed requests go into an IndexedDB queue and are replayed when the connection is back.

```js
import { registerRoute } from "workbox-routing";
import { NetworkOnly } from "workbox-strategies";
import { BackgroundSyncPlugin } from "workbox-background-sync";

registerRoute(
  ({ url }) => url.pathname === "/api/comments",
  new NetworkOnly({
    plugins: [
      new BackgroundSyncPlugin("comments", { maxRetentionTime: 24 * 60 }),
    ],
  }),
  "POST",
);
```

In browsers without Background Sync, Workbox replays the queue the next time the worker starts.

## 178: What are Workbox plugins and lifecycle callbacks?

Plugins are objects with callbacks that run at points in a strategy. Common ones:

- `cacheWillUpdate`: decide if a response should be cached.
- `cachedResponseWillBeUsed`: change or reject a cached response before it is used.
- `requestWillFetch`: change the request before it goes to the network.
- `fetchDidFail`: react to network errors.
- `handlerDidError`: return a fallback when the strategy fails.

```js
const onlyJson = {
  cacheWillUpdate: async ({ response }) =>
    response.headers.get("content-type")?.includes("json") ? response : null,
};
```

## 179: What does the warmStrategyCache recipe do?

It fills a runtime cache with a list of URLs when the worker installs, using the same strategy and plugins as the route. That way the first offline visit to those URLs still works, without moving them into the precache.

```js
import { warmStrategyCache } from "workbox-recipes";
import { CacheFirst } from "workbox-strategies";

const strategy = new CacheFirst({ cacheName: "pages" });
warmStrategyCache({ urls: ["/about", "/contact"], strategy });
```

## 180: How does the full web push subscription flow work?

1. Server creates VAPID keys and gives the public key to the page.
2. User clicks "Enable notifications"; page asks permission.
3. Page calls `reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey })`.
4. Browser contacts its push service and returns a `PushSubscription` (endpoint and keys).
5. Page sends `subscription.toJSON()` to your server, which stores it with the user.
6. Later the server encrypts a message and POSTs it to the endpoint, signed with VAPID.
7. Push service delivers it, the browser wakes the worker, and `push` shows a notification.

## 181: How do you save a push subscription on the server?

Send it to an endpoint and store it linked to the user.

```js
// page
const sub = await reg.pushManager.subscribe({
  userVisibleOnly: true,
  applicationServerKey: KEY,
});
await fetch("/api/push/subscribe", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(sub),
});
```

```js
// Express server
app.post("/api/push/subscribe", async (req, res) => {
  const { endpoint, keys } = req.body;
  await db.pushSubscriptions.upsert({ userId: req.user.id, endpoint, keys });
  res.sendStatus(201);
});
```

One user can have many subscriptions, one per browser or device. Use `endpoint` as the unique key.

## 182: What do you do when sending a push returns 404 or 410?

It means the subscription is gone: the user unsubscribed, cleared data, or the browser expired it. Delete it from your database so you stop sending to it.

```js
try {
  await webpush.sendNotification(sub, payload);
} catch (err) {
  if (err.statusCode === 404 || err.statusCode === 410) {
    await db.pushSubscriptions.delete({ endpoint: sub.endpoint });
  } else {
    throw err;
  }
}
```

A 429 means you are rate limited; retry later using the `Retry-After` header.

## 183: How do you check if the user is already subscribed to push?

Call `pushManager.getSubscription()`. It returns the current subscription or `null`.

```js
const reg = await navigator.serviceWorker.ready;
const sub = await reg.pushManager.getSubscription();
toggle.checked = Boolean(sub);
```

It is good practice to send it to the server on each app start too, in case the server lost it or the endpoint changed.

## 184: How do you unsubscribe from push?

Call `unsubscribe()` on the subscription and tell your server to delete it.

```js
const sub = await reg.pushManager.getSubscription();
if (sub) {
  await fetch("/api/push/unsubscribe", {
    method: "POST",
    body: JSON.stringify({ endpoint: sub.endpoint }),
  });
  await sub.unsubscribe();
}
```

This doesn't change the notification permission; the user can still allow or block that in browser settings.

## 185: How do you focus an existing tab instead of opening a new one on notification click?

Look through open window clients for one with the right URL. Focus it if found, otherwise open a new window.

```js
self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = new URL(event.notification.data?.url ?? "/", self.location.origin)
    .href;
  event.waitUntil(
    (async () => {
      const windows = await clients.matchAll({
        type: "window",
        includeUncontrolled: true,
      });
      const existing = windows.find((w) => w.url === url);
      if (existing) return existing.focus();
      return clients.openWindow(url);
    })(),
  );
});
```

`openWindow` and `focus` only work inside a notification click handler (a user action).

## 186: What do tag and renotify do together?

With the same `tag`, a new notification replaces the old one quietly, without sound or vibration. If you also set `renotify: true`, the replacement alerts the user again.

```js
self.registration.showNotification("3 new messages", {
  tag: "chat-room-7",
  renotify: true,
});
```

This is how chat apps keep one notification per conversation and update its count. `renotify` needs a `tag` and is Chromium only.

## 187: What does requireInteraction do in a notification?

`requireInteraction: true` asks the system to keep the notification on screen until the user clicks or closes it, instead of hiding it after a few seconds. Use it for things like incoming calls or important alerts.

It is a hint: some platforms ignore it, and it can annoy users if used for everything.

## 188: How do you check the notification permission without asking?

Read `Notification.permission`, or use the Permissions API to also get changes.

```js
console.log(Notification.permission); // 'default', 'granted' or 'denied'

const status = await navigator.permissions.query({ name: "notifications" });
status.onchange = () => console.log("Changed to", status.state);
```

Use this to decide whether to show the "Enable notifications" button, or a hint to unblock in settings.

## 189: How do you update the app badge from a push message?

The Badging API works in the service worker too, so you can set the count when the push arrives.

```js
self.addEventListener("push", (event) => {
  const data = event.data.json();
  event.waitUntil(
    Promise.all([
      self.registration.showNotification(data.title, { body: data.body }),
      navigator.setAppBadge?.(data.unreadCount),
    ]),
  );
});
```

The `?.` call skips the badge in browsers without the API. Remember that a push should still show a notification, so don't use push only to update the badge.

## 190: How do you write Playwright tests for a service worker?

Playwright can wait for the worker, simulate offline and check what was served.

```js
import { test, expect } from "@playwright/test";

test("works offline", async ({ page, context }) => {
  await page.goto("/");
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload(); // now controlled
  await context.setOffline(true);
  await page.goto("/tasks");
  await expect(page.getByRole("heading", { name: "Tasks" })).toBeVisible();
});
```

Playwright's `serviceWorkers` option is `'allow'` by default. Set it to `'block'` in other tests so `page.route` mocks aren't skipped by the worker.

## 191: What is chrome://serviceworker-internals?

It is a Chrome page that lists every registered service worker in the browser, with its scope, status, script URL and logs. You can start, stop, inspect, or unregister any of them.

It is useful when DevTools doesn't show something, or when you need to see workers for many origins. `chrome://inspect/#service-workers` is another place to find and debug them, including on a connected Android phone.

## 192: What does "The FetchEvent resulted in a network error response" mean?

It means your fetch handler called `respondWith` but the promise rejected or resolved with something that isn't a valid response, for example `undefined` from a `caches.match` that found nothing.

```js
// bug: returns undefined when not cached and offline
event.respondWith(caches.match(event.request));

// fix: always end with a real Response or a network fetch
event.respondWith(
  caches.match(event.request).then((r) => r || fetch(event.request)),
);
```

## 193: Why does cache.put throw "Request method POST is unsupported"?

The Cache API only stores GET requests. If your fetch handler caches every response, a POST will make `cache.put` throw.

Filter by method before caching, or skip non-GET requests at the top of the fetch handler. If you really need to keep POST data offline, store it yourself in IndexedDB.

## 194: How do you cache Google Fonts in a service worker?

Google Fonts has two parts: a CSS file from `fonts.googleapis.com` that changes sometimes, and font files from `fonts.gstatic.com` that never change. Use different strategies.

```js
registerRoute(
  ({ url }) => url.origin === "https://fonts.googleapis.com",
  new StaleWhileRevalidate({ cacheName: "google-fonts-css" }),
);
registerRoute(
  ({ url }) => url.origin === "https://fonts.gstatic.com",
  new CacheFirst({
    cacheName: "google-fonts-files",
    plugins: [
      new CacheableResponsePlugin({ statuses: [0, 200] }),
      new ExpirationPlugin({ maxEntries: 30, maxAgeSeconds: 365 * 24 * 3600 }),
    ],
  }),
);
```

Workbox also ships this as the `googleFontsCache` recipe.

## 195: What is Window Controls Overlay?

It is a desktop display mode where your installed app can draw into the title bar area, leaving only the OS window buttons (close, minimize, maximize). You opt in with `display_override`.

```json
{ "display_override": ["window-controls-overlay"], "display": "standalone" }
```

You place content with CSS `env(titlebar-area-x)`, `env(titlebar-area-width)` and similar, and mark drag areas with `app-region: drag`. It is supported in Chromium on desktop.

## 196: What is the tabbed display mode?

It is a Chromium desktop mode where an installed PWA's window has its own tab strip, so users can open several documents of the app in one window, like a native editor.

```json
{ "display_override": ["tabbed"], "display": "standalone" }
```

It is still not widely supported, so always give a fallback `display`.

## 197: What does launch_handler do in the manifest?

It controls what happens when the installed app is launched while it is already open.

```json
"launch_handler": { "client_mode": "focus-existing" }
```

- `navigate-new`: open a new window.
- `navigate-existing`: reuse the most recent window and navigate it.
- `focus-existing`: focus the existing window without navigating; the page reads the URL from `window.launchQueue`.
- `auto`: let the browser decide.

It is supported in Chromium browsers.

## 198: How is storage different for PWAs on iOS Safari?

Safari's Intelligent Tracking Prevention can delete all script-writable storage (IndexedDB, Cache API, service worker registrations) for a site the user hasn't interacted with in 7 days of Safari use. Home screen web apps are not affected by this rule, because they have their own storage.

That separate storage also means a home screen app doesn't share login state with the site in Safari; users may have to log in again after installing.

## 199: What happened with PWAs in the EU on iOS 17.4?

In early 2024, Apple announced that, because of the Digital Markets Act, home screen web apps would stop working as standalone apps in the EU and open as normal Safari tabs. After pushback from developers and the European Commission, Apple reversed that decision before iOS 17.4 shipped widely, so home screen web apps kept working.

It showed how much PWA support on iOS depends on Apple's decisions.

## 200: How do you show a fallback image when an image fails offline?

Precache a small placeholder and return it when an image request fails and isn't cached.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.destination !== "image") return;
  event.respondWith(
    caches
      .match(event.request)
      .then(
        (cached) =>
          cached ||
          fetch(event.request).catch(() => caches.match("/img/offline.svg")),
      ),
  );
});
```

An SVG placeholder is tiny and scales to any size.

## 201: How do you choose a caching strategy for each type of request?

A simple rule set that fits most apps:

- **Hashed JS and CSS** (`app.3f2a.js`): precache or cache first. The name changes when the content changes.
- **HTML pages**: network first with a cached fallback, or the app shell for SPAs.
- **Images and fonts**: cache first with an expiry and a max count.
- **API data that can be a bit old**: stale-while-revalidate.
- **API data that must be live** (prices, balances, checkout): network only, with an offline message.
- **Analytics and POSTs**: network only, maybe with a background sync queue.

## 202: How do you cache API responses that need an auth token?

The Cache API matches by URL (and method), not by the `Authorization` header. If two users log in on one device, user B could get user A's cached data.

Options: include the user ID in the cache name (`api-user-42`), or in a URL that is unique per user, and always delete user caches on logout. Never cache responses that contain secrets you don't need offline.

## 203: How does the Vary header affect cache.match?

If a cached response has a `Vary` header, for example `Vary: Accept-Language`, `cache.match` only returns it if the new request has the same value for that header. That can cause unexpected misses.

`Vary: *` never matches. You can pass `{ ignoreVary: true }` to `match` to skip this check, if you know the response is fine for all requests.

## 204: What should you clean up when a user logs out?

- Delete caches that hold user data (`caches.delete('api-user-42')`).
- Clear user data in IndexedDB.
- Unsubscribe from push on the server side, or unlink the subscription from the user.
- Clear the app badge.
- Tell other open tabs to log out too, for example with `BroadcastChannel`.

Precached app files can stay, since they are the same for every user.

## 205: What is BroadcastChannel and how does it help PWAs?

`BroadcastChannel` lets pages, workers and the service worker of the same origin send messages to each other by channel name, without keeping references to each other.

```js
// anywhere: page or sw.js
const channel = new BroadcastChannel("app");
channel.postMessage({ type: "LOGGED_OUT" });
channel.onmessage = (e) => {
  if (e.data.type === "LOGGED_OUT") location.assign("/login");
};
```

It is simpler than looping over `clients.matchAll()` when you just want to tell everyone something.

## 206: How do you get a reply from the service worker to a specific message?

Use a `MessageChannel`. Send one port with the message, and the worker answers on it.

```js
// page
function askWorker(message) {
  return new Promise((resolve) => {
    const { port1, port2 } = new MessageChannel();
    port1.onmessage = (e) => resolve(e.data);
    navigator.serviceWorker.controller.postMessage(message, [port2]);
  });
}
const size = await askWorker({ type: "CACHE_SIZE" });
```

```js
// sw.js
self.addEventListener("message", async (event) => {
  if (event.data.type === "CACHE_SIZE") {
    const keys = await (await caches.open("images")).keys();
    event.ports[0].postMessage(keys.length);
  }
});
```

## 207: What are event.clientId and event.resultingClientId?

In a fetch event:

- `clientId` is the ID of the page that made the request (empty for navigations).
- `resultingClientId` is the ID of the new page a navigation will create.

You can use them to send a message to the exact page that made a request, for example with `clients.get(event.clientId)`, or to the page that is about to load.

## 208: How does the service worker work with a Content Security Policy?

CSP's `worker-src` directive controls which URLs can be loaded as service workers (and other workers). If it is not set, browsers fall back to `child-src`, then `script-src`.

```
Content-Security-Policy: script-src 'self'; worker-src 'self'
```

The CSP of the worker itself comes from the headers of the `sw.js` response, not from the page. Also remember `connect-src` for the push and API calls the app makes.

## 209: How do you load a manifest that is behind authentication?

By default the manifest is fetched without credentials, so if your server requires a cookie for it, the request fails. Add `crossorigin="use-credentials"` to the link.

```html
<link
  rel="manifest"
  href="/manifest.webmanifest"
  crossorigin="use-credentials"
/>
```

A better fix is usually to serve the manifest publicly, because it contains nothing secret.

## 210: How do you set theme_color for dark mode?

The manifest only has one `theme_color`. For pages, the `theme-color` meta tag accepts a `media` attribute.

```html
<meta
  name="theme-color"
  content="#ffffff"
  media="(prefers-color-scheme: light)"
/>
<meta
  name="theme-color"
  content="#121212"
  media="(prefers-color-scheme: dark)"
/>
```

Safari and Chromium on Android respect this. Desktop installed app title bars may still use the manifest value.

## 211: How do you design a good install promotion?

- Don't show it on the first visit. Wait until the user has shown interest, like a second visit or finishing a task.
- Put it in context: a button in the menu, a small banner after checkout, or a card in the feed.
- Explain the value: "Open faster, works offline".
- Make it easy to dismiss and remember the dismissal.
- Hide it when the app is already installed (`display-mode: standalone`, `appinstalled`).
- Show iOS users the "Share, Add to Home Screen" steps since there is no prompt there.

## 212: How do you measure how many users install and use the PWA?

- Track `appinstalled` and the `userChoice` result of your custom prompt.
- Add a parameter to `start_url` (`/?source=pwa`) to count launches.
- Check `matchMedia('(display-mode: standalone)')` on load and send it as an analytics dimension.
- Compare standalone and browser users on retention, session length and conversion.

## 213: How do you store app data in IndexedDB for offline use?

Keep a local copy of the data the user needs, read from it first, and refresh it from the server when online.

```js
import { openDB } from "idb";

const db = await openDB("tasks-db", 1, {
  upgrade(db) {
    const store = db.createObjectStore("tasks", { keyPath: "id" });
    store.createIndex("byDueDate", "dueDate");
  },
});

export async function loadTasks() {
  const local = await db.getAll("tasks");
  render(local);
  try {
    const fresh = await (await fetch("/api/tasks")).json();
    const tx = db.transaction("tasks", "readwrite");
    await Promise.all([...fresh.map((t) => tx.store.put(t)), tx.done]);
    render(fresh);
  } catch {
    showOfflineNotice();
  }
}
```

## 214: Should you store JSON API data in the Cache API or in IndexedDB?

- **Cache API**: good when you only need to replay the same response for the same URL, like a stale-while-revalidate list page. No code changes in the app.
- **IndexedDB**: good when the app needs to query, filter, edit or merge the data, or when it changes offline (drafts, outbox).

Many apps use both: the Cache API for simple GET responses and IndexedDB for the real data model.

## 215: How do you build an outbox pattern for offline writes?

1. When the user creates or edits something, save it to IndexedDB with a status `pending` and update the UI right away.
2. Try to send it. If it works, mark it `synced`.
3. If it fails, keep it and register a background sync (or retry on `online` and on app start).
4. When the sync runs, send all pending items in order and update their status.
5. Show the user which items are not synced yet.

This makes the app feel instant and doesn't lose data when the network drops.

## 216: How do you handle background sync in browsers that don't support it?

Use feature detection and a fallback:

```js
async function queueSync() {
  const reg = await navigator.serviceWorker.ready;
  if ("sync" in reg) {
    await reg.sync.register("outbox");
  } else {
    window.addEventListener("online", flushOutbox, { once: true });
    if (navigator.onLine) flushOutbox();
  }
}
```

Also call `flushOutbox()` when the app starts. Safari and Firefox users then sync when the app is open, which is good enough for most cases.

## 217: What happens if a sync event fails?

If the promise passed to `event.waitUntil` rejects, the browser will retry the sync later, with growing delays. Chrome tries a few times (three by default) before giving up. `event.lastChance` is `true` on the final attempt, so you can tell the user or save the failure.

```js
self.addEventListener("sync", (event) => {
  if (event.tag === "outbox") {
    event.waitUntil(
      flushOutbox().catch((err) => {
        if (event.lastChance) notifyUserSyncFailed();
        throw err;
      }),
    );
  }
});
```

## 218: How do you write a precache step without Workbox?

Keep a list of files and a version, cache them in `install`, and delete other caches in `activate`.

```js
const VERSION = "v12";
const STATIC_CACHE = `static-${VERSION}`;
const ASSETS = ["/", "/index.html", "/app.js", "/styles.css", "/offline.html"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(STATIC_CACHE).then((c) => c.addAll(ASSETS)));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys
          .filter((k) => k.startsWith("static-") && k !== STATIC_CACHE)
          .map((k) => caches.delete(k)),
      );
    })(),
  );
});
```

You must remember to bump `VERSION` on each deploy, which is the main reason people use build tools for this.

## 219: Why should precached requests bypass the HTTP cache?

`cache.addAll(['/app.js'])` uses a normal fetch, which may be answered by the browser's HTTP cache. If `app.js` had a long `max-age`, you could precache an old copy into your new cache version.

Request with `{ cache: 'reload' }` to force the network, or use hashed file names. Workbox does this for you.

```js
await cache.addAll(ASSETS.map((url) => new Request(url, { cache: "reload" })));
```

## 220: How much should you precache?

Only what is needed for the app to start and do its main job offline: the shell HTML, main JS and CSS, key icons, and the offline page. Every precached byte is downloaded on install, even if the user never uses that part.

Lazy routes, big images and rarely used features should be cached at runtime instead. Many teams set a budget, like 1-2 MB, and check it in CI.

## 221: Can you precache files from a CDN on another domain?

Yes, if the CDN sends CORS headers, you get a normal response. Without CORS, `cache.addAll` would fail, because `no-cors` responses are opaque and `addAll` rejects anything that isn't a 2xx response.

It's usually simpler to serve your own static files from the same origin, or put the CDN behind the same domain.

## 222: How do you configure caching in Angular's ngsw-config.json?

Angular uses `assetGroups` for app files and `dataGroups` for API calls.

```json
{
  "index": "/index.html",
  "assetGroups": [
    {
      "name": "app",
      "installMode": "prefetch",
      "resources": { "files": ["/index.html", "/*.css", "/*.js"] }
    },
    {
      "name": "assets",
      "installMode": "lazy",
      "updateMode": "prefetch",
      "resources": { "files": ["/assets/**"] }
    }
  ],
  "dataGroups": [
    {
      "name": "api",
      "urls": ["/api/**"],
      "cacheConfig": {
        "strategy": "freshness",
        "maxSize": 100,
        "maxAge": "1h",
        "timeout": "3s"
      }
    }
  ]
}
```

`freshness` is network first; `performance` is cache first.

## 223: How do you handle updates with Angular's SwUpdate?

```ts
import { inject } from "@angular/core";
import { SwUpdate, VersionReadyEvent } from "@angular/service-worker";
import { filter } from "rxjs";

export class UpdateService {
  private swUpdate = inject(SwUpdate);

  constructor() {
    if (!this.swUpdate.isEnabled) return;
    this.swUpdate.versionUpdates
      .pipe(filter((e): e is VersionReadyEvent => e.type === "VERSION_READY"))
      .subscribe(() => {
        if (confirm("New version available. Reload?"))
          document.location.reload();
      });
  }
}
```

`checkForUpdate()` triggers a check, and `unrecoverable` tells you when the cached version is broken and the page must reload.

## 224: How do you handle the "user is offline" state in the UI?

- Show a small, calm banner like "You're offline. Showing saved data."
- Disable or change actions that can't work offline, or queue them with a clear "will send when online" label.
- Show when the data was last updated.
- Don't block the whole screen with an error if cached content is available.
- Remove the banner when the connection is back and refresh data.

## 225: How do you know if a response came from the cache or the network?

The page can't tell directly from the `Response`. Common options:

- Add a custom header in the worker when serving from cache, like `X-From-Cache: true`, by building a new response.
- Send a message to the page from the worker.
- Use DevTools: the Network panel shows "(ServiceWorker)" in the size column.

Workbox's `BroadcastUpdatePlugin` can also tell pages when a cached response was replaced by a newer one.

## 226: What does workbox-broadcast-update do?

When used with stale-while-revalidate, it compares the cached response and the new network response. If they differ (by `Content-Length`, `ETag` and `Last-Modified` by default), it sends a message to open pages, so the page can refresh the data or say "New content available".

```js
import { BroadcastUpdatePlugin } from "workbox-broadcast-update";

new StaleWhileRevalidate({
  cacheName: "api",
  plugins: [new BroadcastUpdatePlugin()],
});
```

## 227: How do you serve a different response for navigation preload requests on the server?

Check the `Service-Worker-Navigation-Preload` header. For example, an app shell site can return only the content part instead of the full page.

```js
app.get("/articles/:id", (req, res) => {
  const article = getArticle(req.params.id);
  if (req.get("Service-Worker-Navigation-Preload")) {
    return res.send(renderArticleBody(article)); // shell comes from cache
  }
  res.send(renderFullPage(article));
});
```

Add `Vary: Service-Worker-Navigation-Preload` so HTTP caches don't mix the two responses.

## 228: How do you cache video or audio files?

Media players use Range requests (`Range: bytes=0-`) and expect `206 Partial Content` responses. A plain cached full response gives a 200, and some browsers (especially Safari) won't play it.

Workbox's `RangeRequestsPlugin` slices the cached full file to answer range requests. You also have to cache the full file on purpose first, since the player won't fetch it as one request.

```js
import { RangeRequestsPlugin } from "workbox-range-requests";

registerRoute(
  ({ url }) => url.pathname.endsWith(".mp4"),
  new CacheOnly({ cacheName: "videos", plugins: [new RangeRequestsPlugin()] }),
);
```

## 229: How do you let users save content for offline reading?

Add a "Save offline" button that puts the page and its assets into a dedicated cache from the page.

```js
saveButton.onclick = async () => {
  const cache = await caches.open("saved-articles");
  await cache.addAll([location.pathname, ...imageUrls]);
  saveButton.textContent = "Saved";
};
```

In the service worker, check `saved-articles` for navigations when offline. Give users a list of saved items and a way to remove them, and request persistent storage.

## 230: What are good ways to debug a service worker that won't update?

1. In DevTools, check if a worker is stuck in "waiting". Old tabs may still be open.
2. Check that `sw.js` really changed on the server and isn't cached by a CDN.
3. Check imported scripts: with the default `updateViaCache`, they can come from the HTTP cache.
4. Look for errors in the worker console; a failing `install` keeps the old one.
5. Use "Update on reload" or `skipWaiting` in DevTools while testing.

## 231: How do you test push notifications locally?

In Chrome DevTools, **Application > Service workers** has a **Push** field where you can send a test payload to the worker, without a server. For the full flow, run a local Node server with `web-push` and a test subscription. Push works on `localhost` without HTTPS.

For iOS, you need a real device with the app on the home screen and a site on HTTPS.

## 232: What does the Web Share Target look like for files?

```json
"share_target": {
  "action": "/share-photo",
  "method": "POST",
  "enctype": "multipart/form-data",
  "params": { "files": [{ "name": "photo", "accept": ["image/*"] }] }
}
```

```js
// sw.js
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (event.request.method === "POST" && url.pathname === "/share-photo") {
    event.respondWith(
      (async () => {
        const form = await event.request.formData();
        const file = form.get("photo");
        const cache = await caches.open("shared");
        await cache.put("/shared/photo", new Response(file));
        return Response.redirect("/edit?shared=1", 303);
      })(),
    );
  }
});
```

The page then reads the file from the cache. The service worker is needed because the POST has no server to land on.

## 233: How do you read files opened through file_handlers?

Use `window.launchQueue` in the page.

```js
if ("launchQueue" in window) {
  launchQueue.setConsumer(async (launchParams) => {
    for (const handle of launchParams.files) {
      const file = await handle.getFile();
      openDocument(await file.text(), file.name);
    }
  });
}
```

The handles are File System Access API handles, so with permission you can also write the changes back to the same file.

## 234: What is the Origin Private File System and when would a PWA use it?

The Origin Private File System (OPFS) is private file storage for your origin, part of the File System API. Users can't see it, but your app can read and write files quickly, and in workers there is a synchronous access handle for very fast I/O.

PWAs use it for big binary data, like editing images, storing offline maps, or running SQLite compiled to WebAssembly. It is supported in all modern browsers.

## 235: How do you keep the screen on in a PWA?

Use the Screen Wake Lock API, for example in a recipe or navigation app.

```js
let lock;
async function keepAwake() {
  lock = await navigator.wakeLock.request("screen");
  lock.addEventListener("release", () => console.log("Wake lock released"));
}
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "visible" && lock?.released) keepAwake();
});
```

The lock is dropped when the page is hidden, so request it again when the user comes back. It is supported in all major browsers now.

## 236: What device APIs can a PWA use today?

Widely supported: geolocation, camera and microphone (getUserMedia), notifications, Web Share, clipboard, screen wake lock, device orientation, Vibration (not on iOS), Media Session for lock screen controls, and file picking.

Chromium only: Web Bluetooth, WebUSB, Web Serial, WebHID, Web NFC (Android), File System Access save dialogs, contact picker (Android), Periodic Sync and Background Sync.

Always use feature detection, because support changes.

## 237: What is the Media Session API?

It lets a web app show media info and controls on the lock screen, in notifications and on hardware keys.

```js
navigator.mediaSession.metadata = new MediaMetadata({
  title: "Episode 12",
  artist: "My Podcast",
  artwork: [{ src: "/covers/12-512.png", sizes: "512x512", type: "image/png" }],
});
navigator.mediaSession.setActionHandler("play", () => audio.play());
navigator.mediaSession.setActionHandler("pause", () => audio.pause());
```

It makes music and podcast PWAs feel native.

## 238: How do you handle app links so links open in the installed PWA?

On Android, when a PWA is installed through Chrome, links inside its scope opened from other apps can open in the PWA (Chrome creates a WebAPK with intent filters). On desktop Chromium, users can turn on "open supported links" for the app.

`scope_extensions` (a newer, still experimental field) lets an app cover several origins. iOS doesn't open links in home screen web apps; they go to Safari.

## 239: How do you avoid caching responses for logged-out users and showing them to logged-in users?

If a page's HTML differs by login state, caching it by URL alone mixes states. Options:

- Use network first for HTML so the server's fresh version wins when online.
- Cache only the generic shell and load user data by API.
- Include a version or user flag in cache names and clear them on login and logout.

The simplest safe design is: HTML shell is the same for everyone, user data is never in shared caches.

## 240: What is a service worker "kill switch"?

It is a plan for disabling a broken service worker in production. You deploy a new `sw.js` at the same URL that removes its caches, unregisters itself and reloads clients.

```js
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(keys.map((k) => caches.delete(k)));
      await self.registration.unregister();
      const windows = await self.clients.matchAll({ type: "window" });
      windows.forEach((w) => w.navigate(w.url));
    })(),
  );
});
```

This only works if the browser can still fetch `sw.js` without your old worker getting in the way, which it can, because update checks bypass the worker.

## 241: Why is it important that sw.js itself is never served from the service worker's cache?

Browsers fetch the worker script for update checks directly, not through the worker, so a cached `sw.js` in Cache Storage doesn't block updates. But if you precache `sw.js` and some code registers it from cache, or if a CDN caches it for days, users can get stuck.

Don't add `sw.js` to your precache list, and serve it with `no-cache`.

## 242: How do you show a list of what is available offline?

Read the cache keys and show them to the user, for example saved articles.

```js
const cache = await caches.open("saved-articles");
const requests = await cache.keys();
const urls = requests.map((r) => new URL(r.url).pathname);
renderOfflineList(urls);
```

For richer info (titles, dates), save metadata in IndexedDB when you cache each item.

## 243: How do you avoid the offline page showing for server errors?

`fetch()` only rejects on network failures. A 500 from the server is a normal response, so `fetch().catch()` won't catch it. That's usually good: the user sees the real error page.

If you want a fallback on 5xx too, check `response.ok` or the status and decide what to return, for example a cached version of the page with a note.

## 244: How do you make sure a new deploy doesn't break users with old cached HTML?

- Keep old hashed JS and CSS files on the server for some time after a deploy, so old HTML can still load them.
- Use network first for HTML.
- Handle failed lazy chunk loads in the app by reloading once.
- Show an update prompt instead of forcing `skipWaiting` with no reload.

Most "blank screen after deploy" bugs come from old HTML asking for chunks that no longer exist.

## 245: How do you recover when a lazy-loaded chunk fails to load after a deploy?

Catch the error from the dynamic import and do a one-time reload, so the page gets the new HTML and new chunk names.

```js
async function loadPage(name) {
  try {
    return await import(`./pages/${name}.js`);
  } catch (err) {
    if (!sessionStorage.getItem("reloaded")) {
      sessionStorage.setItem("reloaded", "1");
      location.reload();
    }
    throw err;
  }
}
```

Clear the flag after a successful load so it can work again on the next deploy. Vite also fires a `vite:preloadError` event you can use for this.

## 246: How do you handle form submissions when offline?

Catch the submit in JavaScript, save the data to IndexedDB, show it as "pending" in the UI, and send it later via background sync or when back online. Don't let the browser do a plain form POST, because offline it fails and the user may lose what they typed.

Also save drafts while typing, so a reload doesn't lose input.

## 247: How do iOS home screen web apps differ from Safari tabs?

- Separate storage and cookies from Safari, so logins aren't shared.
- Push notifications and badging only work for home screen apps.
- No address bar; you need your own back buttons where needed.
- Each app runs in its own process and can be closed by the OS when in the background.
- Opening links outside the scope goes to Safari or an in-app browser view.

## 248: How do you handle "back" navigation in a standalone PWA?

In `standalone` mode there is no browser back button on iOS and desktop. Android has the system back button, which uses browser history.

Use the History API correctly (real URLs per screen, `pushState` on navigation), and add an in-app back button in the header for screens deeper than the main one, especially when `display-mode: standalone` matches.

## 249: What is the getRegistration method used for?

`navigator.serviceWorker.getRegistration(url)` returns the registration that controls a given URL, or `undefined`. Without arguments it uses the current page's URL.

```js
const reg = await navigator.serviceWorker.getRegistration();
if (reg?.waiting) showUpdateBanner();
```

It's useful on startup to check for a waiting worker without registering again. `getRegistrations()` returns all of them for the origin.

## 250: Does calling register() on every page load cause extra work?

No. If the same script URL is already registered with the same scope, `register()` just returns the existing registration and checks for an update. It doesn't reinstall anything unless the script changed.

So it is safe and normal to call it on every page load.

## 251: How big can a push message payload be?

About 4 KB (4096 bytes) after encryption is the limit most push services accept, so plan for less than that in your JSON. Send only what the notification needs: a title, short body, and an ID or URL.

If the app needs more data, the service worker can fetch it from your API inside the `push` handler before showing the notification.

## 252: What are the TTL and Urgency headers in web push?

- `TTL` (time to live, in seconds) tells the push service how long to keep the message if the device is offline. `TTL: 0` means deliver now or drop it.
- `Urgency` (`very-low`, `low`, `normal`, `high`) helps the device decide whether to wake up and spend battery on it.

```js
await webpush.sendNotification(sub, payload, { TTL: 3600, urgency: "high" });
```

A `Topic` header can also replace an older pending message with the same topic, so a device that was offline only gets the latest one.

## 253: How do you avoid showing a notification when the user is already looking at the app?

In the push handler, check if a focused window of your app is open, and send it a message instead of a system notification.

```js
self.addEventListener("push", (event) => {
  const data = event.data.json();
  event.waitUntil(
    (async () => {
      const windows = await clients.matchAll({ type: "window" });
      const focused = windows.find((w) => w.focused);
      if (focused) {
        focused.postMessage({ type: "PUSH", data });
      } else {
        await self.registration.showNotification(data.title, {
          body: data.body,
        });
      }
    })(),
  );
});
```

Be careful in Chrome: if you skip notifications too often while the app is in the background, Chrome shows a generic one.

## 254: What is the pushsubscriptionchange event?

It fires in the service worker when the browser changes or expires the push subscription on its own. You should subscribe again and send the new subscription to the server.

```js
self.addEventListener("pushsubscriptionchange", (event) => {
  event.waitUntil(
    (async () => {
      const sub = await self.registration.pushManager.subscribe(
        event.oldSubscription.options,
      );
      await fetch("/api/push/subscribe", {
        method: "POST",
        body: JSON.stringify(sub),
      });
    })(),
  );
});
```

Support is uneven (Firefox fires it, Chrome rarely does), so also re-check the subscription on each app start.

## 255: How do you convert a VAPID public key for pushManager.subscribe?

Modern browsers accept the base64url string directly as `applicationServerKey`. Older code converts it to a `Uint8Array`, and you'll still see this helper in many projects:

```js
function urlBase64ToUint8Array(base64String) {
  const padding = "=".repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, "+").replace(/_/g, "/");
  return Uint8Array.from(atob(base64), (c) => c.charCodeAt(0));
}

await reg.pushManager.subscribe({
  userVisibleOnly: true,
  applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY),
});
```

## 256: How do you see which periodic syncs are registered?

```js
const reg = await navigator.serviceWorker.ready;
const tags = await reg.periodicSync.getTags();
if (!tags.includes("refresh-news")) {
  await reg.periodicSync.register("refresh-news", {
    minInterval: 12 * 60 * 60 * 1000,
  });
}
```

Before registering, check permission with `navigator.permissions.query({ name: 'periodic-background-sync' })`. You remove one with `periodicSync.unregister(tag)`.

## 257: What does the periodicsync event handler usually do?

It refreshes cached content so the app opens with new data, and it should be quick and cheap.

```js
self.addEventListener("periodicsync", (event) => {
  if (event.tag === "refresh-news") {
    event.waitUntil(
      (async () => {
        const cache = await caches.open("news");
        await cache.add("/api/news/latest");
      })(),
    );
  }
});
```

Don't show notifications from it to "bring users back"; that is what push is for, and browsers watch for abuse.

## 258: What is the monochrome icon purpose?

An icon with `purpose: "monochrome"` is a single-color shape (only the alpha channel is used), which the system can tint to match the theme, for example in Android's themed icons or notification badges.

```json
{
  "src": "/icons/mono.svg",
  "sizes": "any",
  "type": "image/svg+xml",
  "purpose": "monochrome"
}
```

The other values are `any` (default) and `maskable`. You can give one icon several purposes, but separate files usually look better.

## 259: How do you use InjectManifest with webpack?

```js
// webpack.config.js
const { InjectManifest } = require("workbox-webpack-plugin");

module.exports = {
  // ...
  plugins: [
    new InjectManifest({
      swSrc: "./src/sw.js",
      swDest: "sw.js",
      maximumFileSizeToCacheInBytes: 3 * 1024 * 1024,
    }),
  ],
};
```

`src/sw.js` must contain `self.__WB_MANIFEST`. The plugin bundles your worker and replaces that placeholder with the list of webpack's output files.

## 260: How do you add a "Reload to update" prompt with vite-plugin-pwa?

Set `registerType: 'prompt'` and use the virtual module the plugin provides.

```js
import { registerSW } from "virtual:pwa-register";

const updateSW = registerSW({
  onNeedRefresh() {
    if (confirm("New version available. Reload?")) updateSW(true);
  },
  onOfflineReady() {
    showToast("App ready to work offline");
  },
});
```

There are framework helpers too, like `virtual:pwa-register/react` with a `useRegisterSW` hook.

## 261: Can you write a service worker in TypeScript?

Yes. Compile it like any other file (your bundler or `tsc`) and output a plain JS `sw.js`. For types, add the `WebWorker` lib and declare `self`.

```ts
/// <reference lib="webworker" />
declare const self: ServiceWorkerGlobalScope;

self.addEventListener("install", (event: ExtendableEvent) => {
  event.waitUntil(self.skipWaiting());
});
```

Keep the worker in its own `tsconfig` without the `DOM` lib, so you don't accidentally use `window` or `document`.

## 262: How do you monitor service worker errors in production?

Errors in the worker don't show up in the page's error handlers. Add your own:

```js
self.addEventListener("error", (e) =>
  report({ message: e.message, source: "sw" }),
);
self.addEventListener("unhandledrejection", (e) =>
  report({ message: String(e.reason), source: "sw" }),
);

function report(data) {
  fetch("/api/logs", { method: "POST", body: JSON.stringify(data) }).catch(
    () => {},
  );
}
```

Also log the worker version and install or activate failures. Tools like Sentry have SDK support for service workers.

## 263: How do you measure how long the service worker adds to requests?

Use Resource Timing and Navigation Timing in the page. `workerStart` is when the worker started handling the request, and comparing it with `fetchStart` shows the worker startup cost.

```js
const [nav] = performance.getEntriesByType("navigation");
console.log("SW startup + handling:", nav.fetchStart - nav.workerStart, "ms");
console.log("Served by SW:", nav.workerStart > 0);
```

Newer Chromium versions also expose `workerRouterEvaluationStart` and cache lookup times for the Static Routing API.

## 264: Is HTTP caching still needed if you have a service worker?

Yes. Users on the first visit, browsers without service workers, and requests that go to the network through your worker all still use the HTTP cache. Good `Cache-Control` headers (long `max-age` with `immutable` for hashed files, `no-cache` for HTML) are the base layer.

The service worker adds offline support and fine control on top, it doesn't replace HTTP caching.

## 265: What is Clear-Site-Data and when would you use it?

It is a response header that tells the browser to clear data for your origin.

```
Clear-Site-Data: "cache", "cookies", "storage"
```

`"storage"` removes service worker registrations, Cache Storage, IndexedDB and local storage. You'd send it from a logout endpoint, or as an emergency fix when a broken worker is stuck on users' devices. It only works over HTTPS.

## 266: How do you deploy a PWA under a sub-path like GitHub Pages?

When the app lives at `https://user.github.io/my-app/`, everything must be relative to `/my-app/`:

- Register `./sw.js` from the app folder, so the scope is `/my-app/`.
- Set `start_url` and `scope` in the manifest to `./` or `/my-app/`.
- Use the right base path in your bundler (for example `base: '/my-app/'` in Vite).
- Precache URLs must include the sub-path.

Relative URLs in the manifest are resolved against the manifest's own URL, not the page.

## 267: How are relative URLs in the manifest resolved?

`start_url`, `scope`, `id`, icon `src` and other URLs in the manifest are resolved relative to the manifest file's URL. If the manifest is at `/static/manifest.json` and `start_url` is `"./"`, the start URL becomes `/static/`, which is probably wrong.

Either keep the manifest at the root or use absolute paths like `"/"`.

## 268: What is a WebAPK?

When you install a PWA from Chrome on Android, Chrome builds a real Android package (a WebAPK) for it on Google's servers and installs it. That's why the PWA appears in the app drawer and Android settings like a native app, and can handle links in its scope.

If the WebAPK can't be built, Chrome adds a simple home screen shortcut instead. The WebAPK is updated when the manifest changes.

## 269: How does PWA install work on desktop Safari?

Since Safari 17 on macOS Sonoma, users can choose **File > Add to Dock** for any website. Safari creates a separate web app with its own window, icon and storage, using the manifest if present.

There is no `beforeinstallprompt`, so you can't trigger it from code; you can only tell users how.

## 270: Can you prefetch pages in the service worker?

Yes. When the user is on one page, the worker (or the page) can fetch likely next pages and put them in a cache. Then the next navigation is instant and works offline.

```js
self.addEventListener("message", (event) => {
  if (event.data.type === "PREFETCH") {
    event.waitUntil(
      caches.open("pages").then((c) => c.addAll(event.data.urls)),
    );
  }
});
```

Be careful on mobile data: check `navigator.connection.saveData` (Chromium) and don't prefetch too much.

## 271: How do Speculation Rules and service workers work together?

Speculation Rules (`<script type="speculationrules">`) let Chromium prefetch or prerender likely next pages. Prefetch requests made this way can go through your service worker in newer Chrome versions; earlier versions skipped prefetch for pages controlled by a worker.

They solve related problems: speculation rules make the next navigation fast online, the service worker makes pages work offline. Check how your worker handles the `Sec-Purpose: prefetch` header so you don't count prefetches as real visits.

## 272: Does a service worker affect the back/forward cache?

No longer in a bad way. Older Chrome versions excluded pages that were controlled by a service worker in some cases, but today a controlled page can be stored in bfcache. Things that still block bfcache are open connections, `unload` handlers and `Cache-Control: no-store` on the page in some browsers.

Messages from the worker to a page in bfcache aren't delivered while it's hidden, so pages should refresh state on `pageshow` if needed.

## 273: How do you cache third-party API responses?

Treat them like your own API, with extra care:

- Make sure the API sends CORS headers, so you get real responses and can check `ok`.
- Respect the API's terms; some don't allow storing data.
- Use stale-while-revalidate or network first with expiry, never cache first forever.
- Don't cache responses with secrets or tokens in the URL.

## 274: How do you make the service worker ignore certain URLs?

Return early from the fetch handler without calling `respondWith`.

```js
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (url.pathname.startsWith("/api/admin")) return;
  if (url.origin !== self.location.origin) return;
  if (event.request.headers.get("accept")?.includes("text/event-stream"))
    return;
  // handle the rest
});
```

Skipping things like server-sent events, websocket upgrades, admin areas and analytics keeps the worker from getting in the way.

## 275: Does a service worker intercept WebSocket connections?

No. WebSocket connections don't go through the fetch event. Server-sent events (`EventSource`) do go through it, which is why you should usually pass them through untouched.

For offline support with WebSockets, keep a message queue in IndexedDB and resend when the socket reconnects.

## 276: How do you handle API calls with a stale cache in the UI?

Show cached data right away, mark it as possibly old, and update the UI when fresh data arrives.

```js
async function getProducts(render) {
  const cached = await caches.match("/api/products");
  if (cached) render(await cached.json(), { stale: true });
  try {
    const res = await fetch("/api/products");
    render(await res.json(), { stale: false });
  } catch {
    if (!cached) render([], { offline: true });
  }
}
```

Libraries like TanStack Query also support this pattern and can store their cache in IndexedDB.

## 277: What is the difference between registration.showNotification and new Notification?

- `new Notification(title, options)` is shown from a page and is tied to it. On Android Chrome it isn't allowed at all; it throws.
- `registration.showNotification()` is tied to the service worker. It works when no page is open, supports actions, and click events go to `notificationclick` in the worker.

For PWAs, always use `showNotification`.

## 278: How do you list or close notifications that are already shown?

```js
const notifications = await self.registration.getNotifications({
  tag: "chat-room-7",
});
notifications.forEach((n) => n.close());
```

This is useful when the user reads messages in the app: close the matching notifications so they don't stay in the tray.

## 279: Can a PWA run code on a schedule like a cron job?

Not reliably. There is no timer that survives the worker being stopped. Your options are:

- **Push** from your server at the right time (the server does the scheduling).
- **Periodic Background Sync** in Chromium, with intervals the browser controls.
- The Notification Triggers experiment was dropped, so local scheduled notifications are not available.

For reminders and alarms, server push is the standard approach.

## 280: What are common mistakes in a first service worker?

- Caching everything with cache first, so users never see updates.
- Not versioning or cleaning up caches.
- Caching error responses or POST requests.
- Forgetting `event.waitUntil`, so work is cut off.
- Calling `respondWith` after an `await`.
- Serving `sw.js` with a long cache time.
- Calling `skipWaiting` without thinking about old pages.
- Not testing offline and update flows.

## 281: How do you warm the cache with data the user will likely need offline?

After login or on install, fetch the important data in the background.

```js
self.addEventListener("message", (event) => {
  if (event.data.type === "USER_LOGGED_IN") {
    event.waitUntil(
      (async () => {
        const cache = await caches.open("api-user");
        await cache.addAll(["/api/me", "/api/projects", "/api/settings"]);
      })(),
    );
  }
});
```

Keep the list small, and refresh it with stale-while-revalidate as the user uses the app.

## 282: How do icons and screenshots affect the install prompt quality?

Chromium shows a richer install dialog, like an app store page, if the manifest has a `description` and `screenshots` with the right `form_factor`. Without them, users get a small dialog with only the name and icon.

Crisp icons in all sizes, a maskable icon, and real screenshots make installing feel safe and increase install rates.

## 283: How do you make a PWA feel more like a native app?

- Show content instantly from cache; avoid blank screens.
- Use skeleton screens instead of spinners.
- Disable text selection and long-press menus only where it makes sense (buttons, nav).
- Use `overscroll-behavior` to control pull-to-refresh.
- Respect safe areas with `env(safe-area-inset-*)`.
- Add page transitions, for example with the View Transitions API.
- Use system fonts and fast touch feedback.

## 284: What does overscroll-behavior do for PWAs?

It controls what happens when a user scrolls past the edge of a scroll area, like Android's pull-to-refresh or scroll chaining to the page behind a modal.

```css
body {
  overscroll-behavior-y: contain;
}
```

`contain` stops chaining and the pull-to-refresh gesture; `none` also removes the glow or bounce effect. It's useful when your app has its own pull-to-refresh or full-screen views.

## 285: How do you handle safe areas on phones with a notch?

Add `viewport-fit=cover` and pad your layout with the safe area values.

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

```css
header {
  padding-top: env(safe-area-inset-top);
}
nav.bottom {
  padding-bottom: env(safe-area-inset-bottom);
}
```

This matters most in `standalone` and `fullscreen` modes, where there is no browser bar around the app.

## 286: How do you make a PWA work when it is loaded inside an iframe?

A page in an iframe can be controlled by a service worker of its own origin, if it is in the worker's scope. But third-party iframes have partitioned storage in modern browsers, which means a separate set of caches and registrations keyed by the top-level site.

So an embedded widget can't rely on the offline data from when the user visited its site directly.

## 287: What is storage partitioning and how does it affect service workers?

Browsers now split storage by the top-level site. If `widget.com` is embedded on `a.com` and `b.com`, it gets separate storage and separate service worker registrations in each, and they don't share data with `widget.com` opened directly.

This blocks cross-site tracking. For PWAs that are used directly (top level), nothing changes.

## 288: How do you use the Cache API from the page to check what is cached?

```js
const names = await caches.keys();
for (const name of names) {
  const cache = await caches.open(name);
  const keys = await cache.keys();
  console.log(name, keys.length, "entries");
}
```

This is handy for a debug screen or a settings page that shows "Offline data: 23 MB" with a "Clear" button.

## 289: How do you add offline analytics?

Analytics hits sent while offline are lost unless you queue them. Store failed hits and resend them later, with the original time.

With Workbox, the `workbox-google-analytics` package does this for Google Analytics, but it targets the old Universal Analytics and doesn't fully support GA4. For GA4 or other tools, use a `NetworkOnly` route with `BackgroundSyncPlugin`, or send events with `navigator.sendBeacon` and queue them in IndexedDB when offline.

## 290: What happens to the service worker when the user clears browsing data?

Clearing cookies and site data removes service worker registrations, Cache Storage and IndexedDB for that origin. The next visit is a "first visit" again: no controller, everything from the network, and the worker installs again.

Installed PWAs may also lose their data this way, so important data should live on the server too.

## 291: How do you handle different app versions running at the same time?

During an update, an old tab may be served by the new worker or still use old assets. Make the API backward compatible for a while, keep old static files available, and include the app version in API requests so the server can tell old clients to reload if really needed.

Also, store data in IndexedDB with schema versions and migrate it in the `upgrade` callback.

## 292: How do you migrate an IndexedDB schema in a PWA update?

Bump the version number in `openDB`, and handle each old version in `upgrade`.

```js
const db = await openDB("app-db", 3, {
  upgrade(db, oldVersion, newVersion, tx) {
    if (oldVersion < 1) db.createObjectStore("notes", { keyPath: "id" });
    if (oldVersion < 2)
      tx.objectStore("notes").createIndex("byDate", "updatedAt");
    if (oldVersion < 3) db.createObjectStore("outbox", { autoIncrement: true });
  },
});
```

If another tab still has the old version open, the upgrade is blocked. Handle the `blocked` and `blocking` callbacks so tabs close their connections.

## 293: How do you share state between the service worker and the page?

There is no shared memory. Options:

- `postMessage` and `BroadcastChannel` for events.
- IndexedDB for data both can read and write.
- Cache Storage for responses both can see.

A common pattern is: the worker writes to IndexedDB and sends "updated" over `BroadcastChannel`, and the page reads the new data.

## 294: How do you make an installable PWA for desktop only features like keyboard shortcuts?

Add keyboard listeners in the page as usual. In `standalone` mode on desktop, many browser shortcuts (like `Ctrl+T` for a new tab) are not taken by the browser, so your app can use more of them.

Use the Keyboard Lock API (Chromium) if you need keys like `Escape` in fullscreen, and always show users which shortcuts exist.

## 295: How do you let users install the PWA on iOS from a browser other than Safari?

Since iOS 16.4, third-party browsers like Chrome and Edge on iOS can add sites to the home screen through their share menu, using WebKit under the hood. Before that, only Safari could do it.

The result is the same home screen web app with the same features, push included.

## 296: How do you protect a PWA from serving a cached page with an old CSRF token?

If a cached HTML page includes a CSRF token, offline or cache-first loads may use an expired token, and form posts fail.

Don't put tokens in cached HTML. Fetch the token from an API (network only) when needed, or use same-site cookies and other CSRF defenses that don't depend on page content.

## 297: How do you test a PWA install on Android during development?

Connect the phone with USB, enable USB debugging, and open `chrome://inspect` on your computer. Use port forwarding so the phone opens `localhost:3000` from your machine, which counts as secure.

You can then install the app from the Chrome menu, test the WebAPK, and debug the page and the service worker with DevTools.

## 298: What are icons purpose any and maskable together?

You can set `"purpose": "any maskable"` on one icon, but it's usually a bad idea. A maskable icon has a lot of padding for the safe zone, so it looks too small where it's used as a normal icon. An `any` icon gets cut off when masked.

Provide separate files: one with `purpose: "any"` and one with `purpose: "maskable"`.

## 299: How do you debug why the install prompt isn't showing in Chrome?

1. Open **DevTools > Application > Manifest** and read the installability errors.
2. Check the console for manifest warnings.
3. Make sure you didn't already install it, or dismiss the prompt recently (Chrome waits before showing it again).
4. Check that the `beforeinstallprompt` listener is added early, before the event fires.
5. Use the manifest panel's "Install" link to test directly.

## 300: How do you handle localization in a PWA manifest?

The manifest supports `lang` and `dir` for the language and text direction of its own text.

```json
{ "lang": "de", "dir": "ltr", "name": "Aufgaben" }
```

There's no standard way to put several languages in one manifest yet. Most sites serve a different manifest per language, for example `/de/manifest.webmanifest`, linked from pages in that language. A proposal for translations inside the manifest exists but is not widely supported.

# Advanced Questions (301-450)

## 301: Why does a new service worker wait instead of taking over right away?

The rule is that one origin and scope should only have one version of the app running at a time. If the new worker took over while old pages were open, those pages would be using HTML and JS from version 1 while their requests are handled by version 2's logic and caches. Cache names, URL rules and data formats may not match.

Waiting until all controlled clients are closed avoids that mix. `skipWaiting` is the opt-out for teams that know their versions are compatible or that reload the pages.

## 302: How exactly does the browser decide a service worker has changed?

On an update check, the browser fetches the main script (bypassing the HTTP cache by default) and compares it byte by byte with the stored copy. For classic workers, it also re-fetches every script that was loaded with `importScripts` and compares those. For module workers, it compares all statically imported modules.

If any of them differ, a new worker is installed. A change only in a file that the worker fetches with `fetch()` (like a JSON config) does not count.

## 303: How long can a service worker stay alive?

Browsers stop a worker when it has been idle for a while; in Chrome that is about 30 seconds with no events. While an event is running, `waitUntil` and `respondWith` extend its life, but not forever: Chrome kills a worker if a single event keeps it busy for more than about 5 minutes, and a fetch response must start within that window.

Firefox and Safari have similar limits. Design every handler to finish quickly and store progress so work can continue on the next event.

## 304: Why are tricks to keep a service worker alive a bad idea?

People sometimes send messages from the page every few seconds or call `waitUntil` with a never-ending promise to keep the worker running. Browsers treat this as abuse: it wastes battery and memory, and browsers keep adding limits that break these tricks.

If you need long work, use the right API: Background Fetch for large downloads, a dedicated Web Worker while the page is open, or the server for scheduled tasks.

## 305: What bugs come from keeping state in global variables in a service worker?

Globals survive only as long as the worker process. When the browser stops the idle worker and starts it again for the next event, the script runs from the top and globals are reset.

Typical bugs: an in-memory "already synced" flag that resets, a counter for rate limiting that goes back to 0, or a cached auth token that disappears. It often works in DevTools (where the worker stays alive while inspected) and fails for real users. Use IndexedDB for anything that must persist.

## 306: Why must respondWith be called synchronously?

The browser dispatches the fetch event and, as soon as the listener returns, checks whether `respondWith` was called. If you `await` something first, the listener has already returned, the browser has decided to use the network, and a later `respondWith` throws an `InvalidStateError`.

```js
// wrong
self.addEventListener("fetch", async (event) => {
  const cache = await caches.open("v1");
  event.respondWith(cache.match(event.request)); // too late
});

// right
self.addEventListener("fetch", (event) => {
  event.respondWith(caches.open("v1").then((c) => c.match(event.request)));
});
```

Decide synchronously whether to handle a request, then pass a promise.

## 307: How do you do background work after responding to a fetch?

Call `event.waitUntil()` on the fetch event with the extra work. The response goes to the page right away, and the worker stays alive until the extra promise settles.

```js
self.addEventListener("fetch", (event) => {
  if (!event.request.url.endsWith("/api/feed")) return;
  const network = fetch(event.request);
  event.respondWith(
    caches
      .match(event.request)
      .then((c) => c || network.then((r) => r.clone())),
  );
  event.waitUntil(
    network
      .then(async (res) => {
        const cache = await caches.open("feed");
        await cache.put(event.request, res.clone());
      })
      .catch(() => {}),
  );
});
```

Without `waitUntil`, the browser might stop the worker before the cache write finishes.

## 308: How can a service worker stream a page built from several parts?

You can build a `ReadableStream` that sends the cached header first, then the network content, then the cached footer. The browser starts rendering the header right away while the content is still loading.

```js
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (
    event.request.mode !== "navigate" ||
    !url.pathname.startsWith("/articles/")
  )
    return;

  const parts = [
    caches.match("/shell-start.html"),
    fetch(`/partials${url.pathname}`).catch(() =>
      caches.match("/partials/offline.html"),
    ),
    caches.match("/shell-end.html"),
  ];

  const stream = new ReadableStream({
    async start(controller) {
      for (const part of parts) {
        const res = await part;
        const reader = res.body.getReader();
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          controller.enqueue(value);
        }
      }
      controller.close();
    },
  });

  event.respondWith(
    new Response(stream, {
      headers: { "Content-Type": "text/html; charset=utf-8" },
    }),
  );
});
```

This gives the speed of an app shell with the SEO and first-paint benefits of full HTML.

## 309: What is the Static Routing API?

It lets a service worker tell the browser, during `install`, which requests should skip the fetch handler and go straight to the network or a cache. The browser applies those rules without starting the worker, so it removes worker startup cost for those requests.

```js
self.addEventListener("install", (event) => {
  event.addRoutes?.([
    { condition: { urlPattern: "/api/*" }, source: "network" },
    {
      condition: { urlPattern: "/static/*" },
      source: { cacheName: "static-v3" },
    },
    {
      condition: { requestMode: "navigate", runningStatus: "not-running" },
      source: "race-network-and-fetch-handler",
    },
  ]);
});
```

It ships in Chromium (since Chrome 123, with more sources added later). Other browsers ignore it, so keep a normal fetch handler as the fallback.

## 310: When would you use navigation preload versus the Static Routing API?

Navigation preload only helps navigations, and only when your handler wants the network: the request starts in parallel with the worker boot, but the worker still runs.

Static routing can skip the worker entirely for matching requests, for any request type, and can serve from a named cache too. It is the better tool for "this path should always go to the network". Navigation preload is still useful when your handler needs to combine the network response with something else, and it works in Safari and Firefox too.

## 311: Why is an empty or pass-through fetch handler harmful?

If a worker has a fetch listener, the browser must start the worker for every request in scope, just to find out it does nothing. That adds startup time, sometimes 50-100 ms on slow phones, for zero benefit.

```js
// useless and slow
self.addEventListener("fetch", (event) =>
  event.respondWith(fetch(event.request)),
);
```

Chrome now detects some no-op handlers and skips them, logging a warning, but you shouldn't rely on it. If a worker only exists for push, don't add a fetch listener at all.

## 312: How does cache.match decide if a request matches?

It compares:

- The URL, after removing the fragment (`#...`). The query string counts unless `ignoreSearch` is set.
- The method: only GET (and HEAD with `ignoreMethod`) can match.
- The `Vary` header of the stored response: every header named in it must have the same value in the new request, unless `ignoreVary` is set.

It does not look at cookies, credentials or other request headers. So two requests to the same URL with different `Authorization` headers match the same entry, which matters for multi-user caches.

## 313: Is writing to the Cache API safe when several tabs do it at once?

Each `put` is atomic for one entry, and `addAll` is atomic for its batch (all or nothing). But there is no transaction across several operations, so read-then-write logic like "trim to 50 entries" can race if two tabs or the worker and a tab do it at once.

In practice the worst case is a few extra or missing entries. If you need strict logic, do cache writes only in the service worker (one process), or coordinate with the Web Locks API.

## 314: The Cache API ignores Cache-Control. How do you add expiration?

Store the time you cached each entry and check it when reading. You can read the `Date` header of the stored response, or keep metadata in IndexedDB.

```js
async function cacheFirstWithMaxAge(request, cacheName, maxAgeMs) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) {
    const date = Date.parse(cached.headers.get("date") ?? "");
    if (!Number.isNaN(date) && Date.now() - date < maxAgeMs) return cached;
  }
  const fresh = await fetch(request);
  if (fresh.ok) await cache.put(request, fresh.clone());
  return fresh;
}
```

The `Date` header isn't always there or readable (opaque responses), which is why Workbox's `ExpirationPlugin` keeps its own timestamps in IndexedDB.

## 315: How do you do conditional revalidation with ETags from a service worker?

When you have a cached response with an `ETag`, send it in `If-None-Match`. A `304 Not Modified` means the cached copy is still good, which saves bandwidth for large responses.

```js
async function revalidate(request) {
  const cache = await caches.open("api");
  const cached = await cache.match(request);
  const headers = new Headers(request.headers);
  const etag = cached?.headers.get("etag");
  if (etag) headers.set("If-None-Match", etag);

  const res = await fetch(request.url, { headers, cache: "no-store" });
  if (res.status === 304 && cached) return cached;
  if (res.ok) await cache.put(request, res.clone());
  return res;
}
```

`cache: 'no-store'` keeps the browser's HTTP cache from answering the conditional request itself.

## 316: What is the problem with redirected responses in a service worker?

If you cache a response that came from a redirect (`response.redirected === true`) and return it for a navigation, browsers reject it with an error like "a redirected response was used for a request whose redirect mode is not follow". This exists so a worker can't hide a redirect and confuse the URL bar and security checks.

The fix is to copy the response into a fresh one, which clears the redirect flag:

```js
async function cleanResponse(res) {
  if (!res.redirected) return res;
  return new Response(await res.blob(), {
    status: res.status,
    statusText: res.statusText,
    headers: res.headers,
  });
}
```

Workbox does the same with `copyResponse`. Better still, precache the final URL so no redirect is involved.

## 317: What are the different Response types and why do they matter?

- `basic`: same-origin response; everything is readable except some headers like `Set-Cookie`.
- `cors`: cross-origin with CORS; body and allowed headers are readable.
- `opaque`: cross-origin `no-cors`; status 0, nothing readable.
- `opaqueredirect`: result of `redirect: 'manual'`; you can't see where it goes.
- `error`: a network error, made with `Response.error()`.

They limit what you can return: you can't answer a `cors` mode request (like `fetch()` from the page or `<img crossorigin>`) with an opaque response, and you can't answer a navigation with an opaque one. Doing so gives a network error.

## 318: What are request modes and how do they affect what a service worker can do?

`request.mode` is `navigate` (page loads), `same-origin`, `cors` (most `fetch()` calls and `crossorigin` elements) or `no-cors` (plain `<img>`, `<script>`, `<link>`).

It decides what responses are valid: a `no-cors` request can be answered with anything, a `cors` request needs a CORS-valid response, and a `navigate` request needs a non-opaque one. You also can't create a new `Request` with mode `navigate` yourself; if you need to copy a navigation request, use its URL with a different mode.

## 319: How can a service worker be abused after an XSS bug?

If an attacker can run script on your origin, they can register their own service worker (if they can host a script at a same-origin URL, for example an upload endpoint or a JSONP endpoint). That worker can then intercept all traffic for that scope and survive after the XSS is fixed, until it is updated or removed.

Defenses: fix XSS, never serve user-uploaded files from the same origin as executable JavaScript, use `worker-src` in CSP, and check the `Service-Worker` request header on the server.

## 320: What is the Service-Worker request header?

When the browser fetches a script to register or update it as a service worker, it adds `Service-Worker: script`. Servers can reject such requests for any URL that isn't the real worker.

```js
app.use((req, res, next) => {
  if (req.get("Service-Worker") === "script" && req.path !== "/sw.js") {
    return res.status(403).end();
  }
  next();
});
```

This blocks an attacker from registering an uploaded file or an API endpoint as a worker.

## 321: Why is hosting user content under your main origin dangerous for service workers?

Service worker scope is limited by path, but an origin is one security boundary. If users can upload files that are served as JavaScript from `example.com/uploads/`, an attacker can register a worker there that controls `/uploads/` and reads cookies sent to those URLs. With `Service-Worker-Allowed` misconfigured, it can be even wider.

Serve user content from a separate origin, like `usercontent.example-cdn.com`, with safe content types and `Content-Disposition: attachment` where possible.

## 322: What is cache poisoning in a service worker context?

It's when a bad response gets stored in Cache Storage and is then served for a long time. Causes include caching a captive portal page (hotel Wi-Fi login) as your HTML, caching a 200 error page from a misconfigured CDN, or caching a response injected on an insecure network for a cross-origin `no-cors` resource.

Defenses: only cache responses you can verify (`ok`, expected `content-type`, maybe a version header), avoid caching opaque responses with long-lived strategies, and prefer network first for HTML.

## 323: How do captive portals break PWAs and how do you avoid it?

On a hotel or airport network, any request may get back the portal's login page with a 200 status. A network first strategy then happily caches that page as your `/index.html`. Next time the user opens the app, they see the hotel login page.

Check that responses look like yours before caching: the right `content-type`, a custom header your server always sends, or a marker in the response. Precache with hashed revisions so a wrong file can't replace the shell.

## 324: How do cross-origin isolation headers interact with service workers?

Pages that need `SharedArrayBuffer` must be cross-origin isolated with `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`). Every subresource must then be CORS or have `Cross-Origin-Resource-Policy`.

Responses from your service worker must carry these headers too. If you build a `Response` by hand or serve an old cached HTML without COOP/COEP, the page won't be isolated. Some hosts that can't set headers (like GitHub Pages) use a service worker that adds them, the "coi-serviceworker" trick.

## 325: How do you protect sensitive offline data on a shared device?

Anything in IndexedDB or Cache Storage can be read by anyone with access to the browser profile or by an XSS on your origin. Options:

- Don't store highly sensitive data offline at all.
- Encrypt it with the Web Crypto API using a key derived from a user secret (PBKDF2 from a PIN), so data is useless without it.
- Mark generated keys as non-extractable `CryptoKey` objects stored in IndexedDB, which at least prevents easy copying.
- Clear data on logout and after a time limit.

## 326: How is a web push payload encrypted?

Web push uses message encryption (RFC 8291) with the `aes128gcm` content coding (RFC 8188). The subscription contains two keys:

- `p256dh`: the browser's public ECDH key on the P-256 curve.
- `auth`: a 16-byte random secret.

The server creates a temporary key pair, does ECDH with `p256dh`, mixes in `auth` with HKDF to get the content key and nonce, and encrypts with AES-128-GCM. Only the browser can decrypt it; the push service just forwards the bytes. Libraries like `web-push` do all of this for you.

## 327: How does VAPID authentication work in detail?

The server signs a JWT with its private ECDSA P-256 key (ES256). The JWT contains:

- `aud`: the origin of the push service endpoint, like `https://fcm.googleapis.com`.
- `exp`: an expiry time, at most 24 hours ahead.
- `sub`: a `mailto:` or `https:` contact for the push service.

It is sent as `Authorization: vapid t=<jwt>, k=<public key>`. The push service checks that the public key matches the `applicationServerKey` used when subscribing, so stolen endpoints can't be used by someone else.

## 328: How do you send push notifications to millions of users?

- Store subscriptions in a database indexed by user and endpoint.
- Put send jobs into a queue (SQS, RabbitMQ, Kafka) and process them with many workers.
- Limit concurrency per push service and handle 429 with `Retry-After`.
- Reuse VAPID JWTs per audience until close to expiry instead of signing each message.
- Delete subscriptions on 404/410.
- Use `Topic` and `TTL` so offline devices don't get a flood of stale messages.
- Track sent, failed and clicked counts.

Encryption has to be done per subscription, so CPU cost grows with the number of devices.

## 329: What delivery guarantees does web push give?

Very few. The push service accepts the message (201) but doesn't promise delivery. The device may be off past the TTL, the browser may be closed (on desktop, Chrome and Firefox must be running to receive pushes), or the OS may delay low urgency messages.

Treat push as a hint to the user, not as a data sync channel. The app should fetch the real state from the server when opened, and push handlers should be idempotent in case of duplicates.

## 330: How do browsers limit push and notification abuse?

- Chrome shows a quiet permission UI for sites with low accept rates or abusive notifications, and can block notifications for sites flagged as abusive.
- Chrome and Safari require a visible notification for each push; Safari can revoke the subscription for repeated silent pushes.
- Permission prompts need a user gesture in Safari and Firefox.
- Browsers suggest auto-revoking notification permission for sites the user ignores.

So low-value or spammy notifications don't just annoy users, they can shut down your push channel.

## 331: What is Declarative Web Push?

It's a feature Apple added in 2025, starting with iOS and iPadOS 18.4. The server sends a push whose JSON payload already describes the notification (title, body, navigation URL) in a standard format, and the browser can show it without running a service worker. If a service worker exists, it can still change the notification before it's shown.

It makes push more reliable and battery friendly, since the worker isn't required. Other browsers have discussed it, but it isn't widely supported outside Safari yet.

## 332: How does Background Sync decide when to fire?

The browser fires the `sync` event once it thinks there is connectivity, which may be right away if the user is online. It is triggered by the network coming back, not by a timer. If the handler fails, it retries with exponential backoff, a small number of times.

Chrome also limits how long one sync can run (a few minutes) and may delay syncs when the device is in battery saver. There's no guarantee about exact timing, only that it will try when online.

## 333: What is the Background Fetch API?

It lets a PWA start large downloads (videos, podcasts, offline maps) that continue even if the user closes the page or the service worker stops. The browser shows a download progress UI and fires an event when it's done.

```js
const reg = await navigator.serviceWorker.ready;
await reg.backgroundFetch.fetch("episode-12", ["/media/ep12.mp3"], {
  title: "Episode 12",
  icons: [{ src: "/icons/icon-192.png", sizes: "192x192", type: "image/png" }],
  downloadTotal: 60 * 1024 * 1024,
});
```

```js
self.addEventListener("backgroundfetchsuccess", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open("downloads");
      const records = await event.registration.matchAll();
      for (const r of records)
        await cache.put(r.request, await r.responseReady);
      await event.updateUI({ title: "Episode 12 ready offline" });
    })(),
  );
});
```

It is supported in Chromium only.

## 334: What is the Content Index API?

It lets a PWA tell the browser which content is available offline, so the browser can show it in places like Chrome Android's "Articles for you" or the downloads page.

```js
const reg = await navigator.serviceWorker.ready;
await reg.index?.add({
  id: "article-123",
  url: "/articles/123",
  title: "How we cut load time in half",
  description: "A look at our caching changes",
  category: "article",
  icons: [{ src: "/img/article-123.png", sizes: "192x192", type: "image/png" }],
});
```

You must remove entries when the content is deleted from the cache. Support is limited to Chrome on Android.

## 335: How does the browser decide how often Periodic Background Sync runs?

The `minInterval` is only a minimum. Chrome ties the real frequency to the site engagement score: sites the user opens often get syncs more often (up to about once a day), and rarely used ones get fewer or none. It also only runs on a network the device has used before, and only for installed apps.

So treat it as a nice extra for frequent users, not as a feature you can promise.

## 336: How much storage can a PWA use?

It depends on the browser and is usually a share of free or total disk space, per origin:

- Chromium lets one origin use up to about 60% of total disk space.
- Firefox gives best-effort sites a smaller limit (about 10% of disk or 10 GiB per site group) and persistent sites up to half the disk.
- Safari, since version 17, also uses a share of disk size, larger for browser apps and home screen web apps than for embedded content.

Always check with `navigator.storage.estimate()` instead of assuming numbers, and handle `QuotaExceededError`.

## 337: How does storage eviction work?

When the device runs low on space, browsers evict "best effort" origins first, usually least recently used first, and they delete all of an origin's data at once (Cache Storage, IndexedDB, service worker registrations), not just some of it. Persistent origins are only cleared if the user does it.

Safari also has its 7-day rule for sites without user interaction. Design so the app can recover from a full wipe: the server is the source of truth, and the local data is a cache.

## 338: What is the Storage Buckets API?

It lets one origin split its storage into named buckets, each with its own persistence, durability and quota settings, and each deletable on its own.

```js
const drafts = await navigator.storageBuckets.open("drafts", {
  persisted: true,
  durability: "strict",
});
const db = await new Promise((resolve, reject) => {
  const req = drafts.indexedDB.open("drafts-db", 1);
  req.onsuccess = () => resolve(req.result);
  req.onerror = () => reject(req.error);
});
```

Under pressure, the browser can evict a "cache-like" bucket while keeping important user data. It is supported in Chromium.

## 339: How would you design an offline-first sync engine?

1. **Local store**: IndexedDB holds the current data and an outbox of changes.
2. **Writes**: apply changes locally (optimistic UI) and append them to the outbox with a client-generated ID and timestamp.
3. **Push**: send outbox items in order when online, with idempotency keys so retries are safe.
4. **Pull**: fetch server changes since the last known cursor (`?since=<token>`), apply them locally.
5. **Conflicts**: decide a rule per entity (last write wins, server wins, field-level merge, or ask the user).
6. **Deletes**: use tombstones so deletes sync too.
7. **Coordination**: one sync at a time across tabs with Web Locks.

Tools like Replicache, PowerSync, RxDB or Automerge-based CRDT libraries implement parts of this.

## 340: What conflict resolution strategies exist for offline edits?

- **Last write wins**: the newest timestamp wins. Simple, but silently loses edits and depends on clocks.
- **Server wins / client wins**: one side always wins; easy, but can lose data.
- **Field-level merge**: merge changes to different fields, conflict only when the same field changed.
- **Version checks**: each record has a version; the server rejects stale writes with 409, and the client re-applies or asks the user.
- **CRDTs**: data types designed to merge automatically (like collaborative text). No conflicts, but more complex and larger data.

Pick per data type: a profile name can use last write wins, a shared document may need CRDTs.

## 341: How do you sync deletes in an offline-first app?

If you just remove the record locally, the next pull has no way to tell "deleted" from "never seen". Use tombstones: mark the record as deleted with a timestamp (`deletedAt`) and sync that like any other change.

The server keeps tombstones long enough for every client to see them, then cleans them up. Clients that were offline longer than that need a full resync.

## 342: How do you implement idempotent replays of queued requests?

Give each change a unique ID generated on the client (for example `crypto.randomUUID()`) and send it as an `Idempotency-Key` header. The server stores processed keys for some time and returns the earlier result for a repeated key instead of applying the change twice.

```js
await fetch("/api/orders", {
  method: "POST",
  headers: { "Content-Type": "application/json", "Idempotency-Key": item.id },
  body: JSON.stringify(item.payload),
});
```

This matters because background sync may resend a request whose first attempt actually reached the server before the connection dropped.

## 343: How do you make sure only one tab runs the sync at a time?

Use the Web Locks API. It is shared across tabs and workers of the same origin.

```js
async function syncOnce() {
  await navigator.locks.request(
    "sync-outbox",
    { ifAvailable: true },
    async (lock) => {
      if (!lock) return; // another tab or the SW is syncing
      await flushOutbox();
    },
  );
}
```

`ifAvailable: true` skips instead of waiting. The lock is released when the callback's promise settles or the tab closes, so there are no stuck locks.

## 344: When would you use a SharedWorker instead of the service worker for shared state?

A SharedWorker is one worker shared by all open tabs of an origin. It stays alive while at least one tab is connected, so it can hold in-memory state, a single WebSocket connection, or a SQLite database for all tabs.

The service worker can't do this well because it's stopped when idle. Use the service worker for network interception, push and sync, and a SharedWorker for live shared state while the app is open. SharedWorker isn't available in Chrome on Android, so you need a fallback there.

## 345: How do you roll out a risky service worker change safely?

- Ship the worker behind a server-side flag: serve a different `sw.js` body (or config it fetches) to a small percentage of users.
- Log the worker version and errors to your monitoring.
- Watch error rates, offline usage and performance for the cohort.
- Have a kill switch version ready.
- Avoid changing cache names and routes in the same release as big app changes.

Remember that rollback isn't instant: users only get the fixed worker after their next update check.

## 346: How does a service worker fit with server-side rendering?

With SSR, the server sends full HTML for each URL, which is good for SEO and first load. A service worker can still:

- Cache static assets with precaching.
- Use network first for HTML, with cached pages as an offline fallback.
- Use streaming to combine a cached shell with server-rendered content.

What you lose with a pure app shell approach is the server's HTML on repeat visits. Many teams use SSR for the first visit and let the worker serve a shell plus client rendering after that, which needs the app to support both.

## 347: What are the trade-offs between the app shell model and network first HTML?

App shell (cache first HTML shell, data from API):

- Instant start and full offline support.
- But the first paint has no content, and the shell can be out of date until the worker updates.

Network first HTML:

- Always fresh, server-rendered content and good SEO.
- But slow networks mean slow starts, unless you add a timeout and cached fallback.

Streaming a cached header with network content in between is a middle ground.

## 348: Can a service worker make a site slower?

Yes. Starting the worker takes time, especially on low-end phones, and reading from Cache Storage can be slower than the HTTP memory cache or even a fast network on a good connection. A fetch handler that does heavy work, like parsing JSON or many cache lookups, adds delay to every request.

Measure with real user data, comparing controlled and uncontrolled page loads. Use navigation preload, static routing, or no fetch handler for routes that don't benefit.

## 349: What is the "race cache and network" strategy?

Start the cache lookup and the network request at the same time and return whichever comes back first with a usable response. It helps on devices with slow disks, where the network can win.

```js
function raceCacheNetwork(request) {
  return new Promise((resolve, reject) => {
    let failures = 0;
    const fail = () => ++failures === 2 && reject(new Error("both failed"));
    caches.match(request).then((r) => (r ? resolve(r) : fail()), fail);
    fetch(request).then((r) => (r.ok ? resolve(r) : fail()), fail);
  });
}
```

It uses more data, because the network request always runs. The Static Routing API has a built-in `race-network-and-fetch-handler` source.

## 350: How do you measure the real impact of a service worker in production?

Collect Real User Monitoring data with a flag for whether the page was controlled (`navigator.serviceWorker.controller` at load) and how it was served (`workerStart`, `transferSize === 0` for cache hits). Compare TTFB, LCP and INP between controlled and uncontrolled visits, split by device class and network.

You can also run an A/B test by not registering (or unregistering) the worker for a random cohort and comparing business metrics like bounce rate and conversions.

## 351: What happens if precaching takes a long time on a slow network?

`install` doesn't finish until every file is downloaded. If the user leaves before that, the install is aborted and retried on the next visit, possibly forever on a slow connection if the precache is big. Meanwhile, the downloads compete with the page's own requests.

Keep the precache small, register the worker after `load`, and move large assets to runtime caching or a later "download for offline" step.

## 352: Does one failed file in precaching break everything?

With `cache.addAll` or Workbox precaching, yes: if any URL fails, the install fails, and the old worker (or no worker) stays. That is by design, because a half-cached app shell is worse than none.

The danger is a precache list that references a file that doesn't exist on the server (a typo, a file removed by a deploy). Then no user can install the new version. Validate the precache list in CI by checking every URL returns 200.

## 353: What iOS limits should a PWA architect plan around?

- No `beforeinstallprompt`; users must add the app manually.
- No Background Sync, Periodic Sync or Background Fetch.
- Web push only for home screen apps, from iOS 16.4.
- Home screen apps have separate storage and cookies from Safari.
- Script-writable storage can be wiped after 7 days without interaction in Safari (not home screen apps).
- The service worker and app can be killed quickly in the background.
- No Web Bluetooth, WebUSB or other Chromium device APIs.
- All browsers on iOS use WebKit (outside the EU), so Chrome on iOS has the same limits.

## 354: When would you choose a PWA over a native app, and when not?

Choose a PWA when the product is content or forms, reach and low cost matter, you want one codebase, fast updates, and links/SEO, and the needed device features are available on the web.

Choose native (or a native shell) when you need deep OS integration (widgets, background location, Bluetooth on iOS, health data), heavy 3D or real-time media, strong app store presence, or reliable background work and notifications on iOS.

Many teams do both: a PWA for reach and a native app for heavy users.

## 355: How does a Trusted Web Activity verify the site?

The Android app declares the site in its manifest, and the site publishes `/.well-known/assetlinks.json` with the app's package name and signing certificate SHA-256 fingerprint.

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.example.tasks",
      "sha256_cert_fingerprints": ["AB:CD:..."]
    }
  }
]
```

If verification fails, the TWA falls back to showing a Custom Tab with a URL bar. A common mistake is using the upload key fingerprint instead of the Play App Signing key.

## 356: How do you sell digital goods in a PWA on Google Play?

Google Play requires its own billing for digital goods in apps from the store. In a TWA, you use the Digital Goods API together with the Payment Request API.

```js
const service = await window.getDigitalGoodsService(
  "https://play.google.com/billing",
);
const [sku] = await service.getDetails(["premium_monthly"]);
const request = new PaymentRequest(
  [
    {
      supportedMethods: "https://play.google.com/billing",
      data: { sku: sku.itemId },
    },
  ],
  { total: { label: "Total", amount: sku.price } },
);
const response = await request.show();
await verifyOnServer(response.details.purchaseToken);
await response.complete("success");
```

The purchase token must be verified on your server with the Play Developer API.

## 357: How do passkeys work in an installed PWA?

The WebAuthn API works the same in installed PWAs as in the browser, so you can use passkeys for login with `navigator.credentials.create()` and `navigator.credentials.get()`. The credentials are tied to your domain (relying party ID), so they're shared between the PWA and the site in the same browser.

On iOS, home screen apps have separate cookies, but passkeys are stored in iCloud Keychain, which makes logging in again inside the installed app quick.

## 358: Should a service worker add Authorization headers to requests?

It can, but it's risky. To do it, the worker needs the token, which means storing it in IndexedDB or keeping it in a global that disappears when the worker stops. Any script with XSS on your origin can also read IndexedDB, so this doesn't protect the token better than the page keeping it.

Also, creating a modified `Request` can drop or change things like the mode and body stream. Most teams prefer HttpOnly, Secure, SameSite cookies for auth, which the browser attaches automatically, and keep the worker out of auth.

## 359: How do you modify a request in a service worker?

Create a new `Request` from the old one with changes. Some properties can't be changed or copied freely.

```js
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (!url.pathname.startsWith("/api/")) return;
  const headers = new Headers(event.request.headers);
  headers.set("X-App-Version", "4.2.0");
  const modified = new Request(event.request, { headers });
  event.respondWith(fetch(modified));
});
```

You can't create a `navigate` mode request, and for requests with a body you should do this before anyone reads the body. Adding a custom header to a cross-origin request also turns it into a CORS preflight request.

## 360: Why do you need to clone a request before retrying it?

A request with a body (POST, PUT) has a stream that can be read only once. After `fetch(request)` reads it, the same request can't be sent again, so retrying throws.

```js
const backup = event.request.clone(); // before the first fetch
try {
  return await fetch(event.request);
} catch {
  await saveToOutbox(backup); // body still readable
  return new Response(JSON.stringify({ queued: true }), {
    status: 202,
    headers: { "Content-Type": "application/json" },
  });
}
```

For storage in IndexedDB, read the body into text or an ArrayBuffer and save it with the URL, method and headers.

## 361: How does Workbox store requests for background sync?

`workbox-background-sync` serializes the failed request (URL, method, headers, body as an ArrayBuffer, mode, credentials and so on) into an IndexedDB store with a timestamp and queue name. On a `sync` event (or worker startup in browsers without Background Sync), it rebuilds `Request` objects and replays them in order.

Entries older than `maxRetentionTime` are dropped. You can also give a custom `onSync` callback to control replay, for example to stop on a 4xx error instead of retrying forever.

## 362: What are the limitations of module service workers?

- `importScripts()` is not allowed; you use static `import`.
- Dynamic `import()` is not allowed in service workers.
- All statically imported modules are fetched and checked on update, so many small modules add update cost.
- Older Firefox versions didn't support them at all.

Because of this, most production setups still bundle the worker into a single file, even when the source uses ES modules.

## 363: How does a hard reload interact with the service worker?

A hard reload (Shift + Reload, or Ctrl/Cmd + Shift + R) makes the page load without the service worker. The page is uncontrolled, `navigator.serviceWorker.controller` is `null`, and all requests go to the network. A normal reload brings control back.

This confuses debugging: "it works after a hard reload" often means the bug is in the worker or its cache.

## 364: What problem can clients.claim cause?

Without `claim`, a page is either fully controlled or not. With `claim`, a page that started uncontrolled becomes controlled halfway through its life. Requests made before the claim went to the network and requests after go through the worker.

If the page or the worker assumes all requests were handled the same way (for example cache-first HTML and network loaded JS from different deploys), you can get a mix. It's usually fine for the first install, but think carefully before using it with updates.

## 365: How do you find all clients, including ones the worker doesn't control?

`clients.matchAll()` returns only controlled clients by default. Pass `includeUncontrolled: true` to get every same-origin client in scope, like pages loaded with a hard reload or before the worker activated.

```js
const all = await self.clients.matchAll({
  type: "window",
  includeUncontrolled: true,
});
```

This is important in `notificationclick` handlers, where you want to focus any open tab, not only controlled ones.

## 366: How do you answer Range requests yourself in a service worker?

Read the full cached response, slice the bytes, and return a 206 with the right headers.

```js
async function rangeResponse(request, cachedResponse) {
  const buffer = await cachedResponse.arrayBuffer();
  const header = request.headers.get("range"); // "bytes=1000-"
  const [startStr, endStr] = header.replace("bytes=", "").split("-");
  const start = Number(startStr);
  const end = endStr ? Number(endStr) : buffer.byteLength - 1;
  return new Response(buffer.slice(start, end + 1), {
    status: 206,
    headers: {
      "Content-Type": cachedResponse.headers.get("content-type"),
      "Content-Range": `bytes ${start}-${end}/${buffer.byteLength}`,
      "Content-Length": String(end - start + 1),
      "Accept-Ranges": "bytes",
    },
  });
}
```

Loading the whole file into memory for every range is slow for big videos, so Workbox's plugin uses `Blob.slice` instead, and very large media is better stored in OPFS.

## 367: Cache API or OPFS for large files?

The Cache API stores `Response` objects and is convenient when the file came from a URL and will be served back as one. OPFS is a real file system: you can write in parts, seek, update in place and read ranges cheaply.

For offline video, maps or big datasets that you write in chunks or partly update, OPFS is the better choice. For assets you download once and serve as-is, the Cache API is simpler.

## 368: How does the number of cache entries affect performance?

`cache.match` is usually fast, but `cache.keys()` on a cache with tens of thousands of entries can take a long time and use a lot of memory, because it builds a `Request` object for every entry. Trimming logic that calls `keys()` on every fetch can slow everything down.

Keep caches small and split by type, trim in the background (in `waitUntil` and not on every request), and track metadata like access time in IndexedDB with indexes.

## 369: Can you use Subresource Integrity when precaching?

Yes. `Request` has an `integrity` option, and `fetch` will reject if the content doesn't match the hash.

```js
const request = new Request("/app.4f2c.js", {
  integrity:
    "sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC",
});
await cache.add(request);
```

Workbox supports an `integrity` field in precache manifest entries. It protects against a CDN or proxy serving modified files that would then be cached for a long time.

## 370: Why is importScripts from a third-party CDN risky?

The imported code runs with full power inside your service worker, so it can read and change every request and response on your origin. If the CDN is compromised or the script changes, your worker changes with it, and the update check even picks up the new version automatically.

Bundle your dependencies into your own `sw.js` instead, or at least pin exact versions on a CDN you trust. Old Workbox docs used `workbox-sw` from Google's CDN; today bundling is the recommended way.

## 371: What happens if the manifest scope and service worker scope don't match?

They are separate things, so mismatches cause odd behavior:

- If the worker scope is narrower than the manifest scope, some pages of the installed app aren't controlled, so they don't work offline.
- If `start_url` isn't controlled, the app can't open offline.
- If the manifest scope is narrower than the site, navigations to other parts open a browser UI bar or a separate window.

In most apps, set both to the same path.

## 372: How do you change a PWA's manifest id or start_url without breaking installs?

Browsers identify an installed app by its manifest `id` (or `start_url` if `id` is missing). If you change it, the browser treats it as a new app: existing installs won't update and users may end up with two icons.

If you never set `id`, add `"id"` with the value the browser already computed from your current `start_url` (DevTools shows the "Computed App ID"). Then you can freely change `start_url` later.

## 373: How do installed apps pick up manifest changes?

Chromium checks the manifest from time to time when the app is launched. Changes to things like `theme_color`, shortcuts or `display` apply silently. Changes to the name or icons may show a dialog asking the user to accept the update, to stop sites from pretending to be another app.

On Android, the WebAPK is rebuilt and updated by Chrome when the manifest changes, but that can take a day or more. Safari updates are less predictable, so test before relying on manifest changes reaching iOS users.

## 374: Can you have several installable PWAs on one origin?

Yes. Give each its own manifest with a different `id`, `start_url` and `scope`, and optionally its own service worker scope.

```json
// /mail/manifest.webmanifest
{ "id": "/mail/", "start_url": "/mail/", "scope": "/mail/", "name": "Mail" }
```

They still share the origin's storage and quota, so cache names and IndexedDB database names must not clash, and a bad worker in one can't touch the other only if scopes don't overlap.

## 375: What is scope_extensions?

`scope_extensions` is a newer manifest field (Chromium, still rolling out) that lets one app cover several origins, like `example.com` and `example.co.uk` or `app.example.com` and `auth.example.com`. Each extra origin must agree by hosting a `.well-known/web-app-origin-association` file.

Before this, navigating to another origin from an installed app always showed a browser bar or left the app.

## 376: What are Isolated Web Apps?

Isolated Web Apps are a Chromium proposal and feature (mainly on ChromeOS for managed devices) where a web app is packaged as a signed bundle and installed offline, without loading from a live server. Because the code can't change without a new signed version, the browser allows more powerful APIs, like Direct Sockets.

They're aimed at enterprise and kiosk cases, not normal websites, but they show where the line between web and native apps is moving.

## 377: How does web push on Safari differ from Chrome?

The code is the same standard Push API with VAPID; you no longer need an Apple Developer account or Apple-specific setup (that was the old Safari push system). Differences:

- On iOS and iPadOS, only home screen apps can subscribe.
- Endpoints are on `web.push.apple.com`.
- Safari requires a user gesture for the permission prompt.
- Silent pushes are not allowed and can lead to the subscription being removed.
- Safari 18.4+ also supports Declarative Web Push.

## 378: Why might web push work on Android but not on desktop?

On Android, the OS receives the push and starts Chrome when needed. On Windows and Linux, Chrome and Firefox must be running (even in the background) to receive pushes; if the browser is fully closed, messages wait until it starts or expire after the TTL.

Other causes: OS-level "Do Not Disturb" or Focus modes, notifications turned off for the browser in OS settings, or the user's browser profile not being the one that subscribed.

## 379: A deploy shipped a broken precache list and nobody gets the new version. What do you do?

1. Find the failing URL in the worker console or by checking each precache URL.
2. Deploy a fix that makes the URL work (restore the file) or remove it from the list. Old clients still run the last good worker, so they are fine meanwhile.
3. If the broken version did install and breaks the app, deploy a kill switch or a quick fix with `skipWaiting` and a page reload.
4. Add a CI check that requests every precache URL from the built output.

Users get the fix on their next navigation, since update checks bypass the worker.

## 380: How do you test service worker logic?

- **Unit tests**: put routing and strategy decisions in plain functions (`chooseStrategy(request)`) and test them in Node or Vitest. You can use `undici`'s `Request` and `Response` or the global ones in Node 18+.
- **Integration tests**: run the real worker in a browser with Playwright: install, go offline, reload, check content, deploy a new version and test the update prompt.
- **Manual checks**: real Android and iOS devices, slow 3G, storage nearly full.

Mocking the whole service worker environment is possible with libraries but tends to drift from real browsers.

## 381: How does Workbox store precached files with revisions?

Workbox uses one precache cache per scope, and the cache key is the URL with a `__WB_REVISION__=<hash>` query parameter for files without a hash in the name. When serving, it maps the clean URL to the versioned key.

On a new install, it compares the manifest with what's cached, fetches only new keys into the cache, and in `activate` removes keys that are no longer in the manifest. `cleanupOutdatedCaches()` removes precache caches from older Workbox versions with different naming.

## 382: What was AppCache and why was it replaced?

AppCache was the first offline web feature: a manifest file listing URLs to cache. It was declarative and simple, but had serious problems: files were always served from cache first, any change required updating the manifest, a single failure broke the update, the page that referenced the manifest was always cached ("master entries"), and there was no way to customize behavior.

It was removed from browsers (Chrome removed it in 2021). Service workers replaced it with a programmable proxy, so developers decide the rules instead of fighting fixed ones.

## 383: How does Angular's service worker decide what changed?

Angular's build creates `ngsw.json`, which lists every asset with a SHA-1 hash, plus your caching config. The Angular worker (`ngsw-worker.js`) fetches `ngsw.json` to check for updates and treats a changed hash table as a new app version. It can keep several versions cached and serve each open tab the version it started with.

If files on the server don't match the hashes (for example a CDN serves a newer file), it marks the version broken and may report `UNRECOVERABLE_STATE` through `SwUpdate`.

## 384: What is Angular's safety worker?

`@angular/service-worker` ships a `safety-worker.js`. It is a minimal worker that unregisters itself and clears Angular's caches. To remove Angular's service worker from users' devices, you serve the safety worker at the `ngsw-worker.js` URL (and any other worker URLs you used).

It is the official version of the "kill switch" pattern for Angular apps.

## 385: What was foreign fetch?

Foreign fetch was an experimental Chrome feature that let a service worker from one origin intercept requests made to it by other sites, for example a font CDN serving fonts from its own worker cache to every site using it. It was removed in 2017 because of privacy and complexity concerns.

Today a service worker only sees requests from pages it controls on its own origin and scope. Storage partitioning made cross-site caching like that impossible by design.

## 386: How do you stay data friendly with users on slow or expensive connections?

Check `navigator.connection` (Chromium) and the `Save-Data` header.

```js
const saveData = navigator.connection?.saveData;
const slow = ["slow-2g", "2g"].includes(navigator.connection?.effectiveType);
if (!saveData && !slow) prefetchNextArticles();
```

In the worker, you can read the `Save-Data: on` request header and serve smaller images or skip prefetch and background refreshes.

## 387: How would you design a PWA for a news site with offline reading?

- **Shell and assets**: precache layout CSS, JS, fonts and the offline page.
- **Article HTML**: network first with a 3 second timeout, cache what users open, limit to the last 50 articles with expiry.
- **Images**: cache first with `maxEntries`, plus a placeholder fallback.
- **Saved articles**: a "save" button that writes to a separate persistent cache, with a list page.
- **Freshness**: periodic sync on Chromium to fetch top stories for installed users.
- **Push**: breaking news with topic and TTL headers.
- Watch quota, request persistent storage when users save articles.

## 388: How would you design an offline shopping cart?

- Store the cart in IndexedDB as the main local source; render it instantly.
- Sync to the server when online, keyed by cart ID, with last write wins per item.
- Show cached product data with a "prices may have changed" note when offline.
- Never complete checkout offline: payment and stock checks need the network, so make checkout network only with a clear message.
- On reconnect, re-validate prices and stock and show the differences before payment.

## 389: How would you design a field inspection app used with bad connectivity?

- Users download "jobs" for the day while on Wi-Fi: forms, reference data, maps (OPFS for big files), with persistent storage requested.
- Every form change is saved locally right away, with IDs created on the device.
- Photos are compressed in a worker and stored as blobs in IndexedDB.
- An outbox uploads items in order when online, photos in chunks with resume, and idempotency keys.
- A clear sync status per job, and warnings before logout if unsynced data exists.
- On iOS (no background sync), sync runs while the app is open and on each launch.

## 390: How would you design a chat PWA?

- **Live messages**: WebSocket while open; push notifications when not focused.
- **Local data**: messages in IndexedDB per conversation with indexes, so opening a chat is instant and works offline.
- **Sending**: write to the outbox with a client ID, show "sending", update to "sent" on server ack; retry with background sync or on reconnect.
- **Notifications**: one per conversation using `tag`, close them when the chat is read, badge count with the Badging API.
- **Multi-tab**: BroadcastChannel to update all tabs, Web Locks so one tab owns the socket or use a SharedWorker.

## 391: Users report they still see an old version days after a deploy. How do you investigate?

1. Check if `sw.js` is cached by a CDN or with a long `Cache-Control`.
2. Check whether the new worker installs but stays in "waiting" because users keep a tab open (common for SPAs). Add an update prompt or periodic `reg.update()`.
3. Check the worker console for install errors (bad precache URL).
4. Check whether HTML is cache first with no revalidation.
5. Check `importScripts` files cached by the HTTP cache with `updateViaCache`.
6. Log the worker version from clients to see the real adoption curve.

## 392: Users complain the app uses too much storage. What do you do?

- Measure: report `navigator.storage.estimate()` and per-cache entry counts from clients.
- Look for opaque responses (padded to MB each) and cache with CORS instead.
- Add `maxEntries` and `maxAgeSeconds` to every runtime cache.
- Delete old precache versions and caches from old naming schemes on activate.
- Move large optional downloads behind an explicit "download" button with a manager UI.
- Add a "Clear offline data" option in settings.

## 393: After adding a service worker, LCP got worse on low-end Android. Why, and how do you fix it?

Likely causes: worker startup time on each navigation, a fetch handler that does slow work, HTML served network first through the worker without navigation preload, or precaching competing with the first load.

Fixes: enable navigation preload, use static routing to skip the worker for some requests, serve HTML from cache with streaming, make the fetch handler do the minimum, and delay registration until after `load`. Compare RUM data for controlled and uncontrolled loads to confirm.

## 394: Logged-in users sometimes see the logged-out page. What is wrong?

A cache likely stores the HTML from a logged-out visit (cache first or stale-while-revalidate) and serves it after login, because the Cache API matches by URL only and ignores cookies.

Fixes: use network first for HTML that depends on auth, or make HTML the same for everyone and load user state by API; clear page caches on login and logout; and never cache responses that set or depend on session cookies.

## 395: Push notifications don't arrive on iPhone. What do you check?

- Is the app added to the home screen and opened from there? Safari tabs can't subscribe.
- Is iOS 16.4 or newer?
- Was `requestPermission()` called from a tap?
- Is the subscription saved on the server, and is the endpoint `web.push.apple.com`?
- Does every push show a notification? Silent pushes can lead to revocation.
- Is the VAPID `sub` claim a valid `mailto:` or `https:` URL? Apple rejects bad values.
- Check the push service's HTTP response codes on the server side.
- Check iOS Focus and notification settings for the app.

## 396: Users get the same notification twice. What could cause it?

- Several subscriptions for one device (after re-subscribing) all stored on the server. Use the endpoint as a unique key and clean up old ones.
- The server retried a send that actually succeeded.
- Both the page (`new Notification`) and the worker show it.
- Two service workers in different scopes both subscribed.

Use a stable `tag` per event so duplicates replace each other, and make sends idempotent on the server.

## 397: You're moving the app to a new domain. What happens to the PWA?

Service workers, caches, IndexedDB, push subscriptions and installs are all tied to the old origin and don't move. Plan:

1. Keep the old domain serving a worker that redirects or shows a notice, and eventually a kill switch.
2. Redirect HTTP traffic to the new domain (the old worker may intercept navigations, so update it first).
3. Users need to install the app again from the new domain; tell them in the old app.
4. Re-subscribe push on the new origin; there's no way to transfer permission.
5. Move data by syncing to the server from the old origin, then loading it on the new one.

## 398: How do you completely remove a PWA from production?

1. Replace `sw.js` with a kill switch worker that deletes caches, unregisters itself and reloads clients.
2. Keep serving that file at the same URL for months, since some users visit rarely.
3. Remove the manifest link and the registration code from pages.
4. Optionally send `Clear-Site-Data: "storage"` on some responses.
5. Stop sending pushes and delete subscriptions.

Don't just delete `sw.js`. A 404 on the update check makes the update fail, but the old worker stays installed and keeps serving its caches, so users can stay on the old app.

## 399: How can you run A/B tests with a service worker in place?

If variants are decided on the server and HTML is cached, users may get stuck in one variant or see mixed versions. Options:

- Decide the variant on the client from a stored assignment, with the same cached assets for all.
- Include the variant in cache keys or cache names.
- Use network first for HTML so the server's choice applies.

Don't let the worker cache variant-specific HTML under a shared URL.

## 400: How do you handle a multi-tenant SaaS on subdomains as a PWA?

Each subdomain (`acme.app.com`, `globex.app.com`) is its own origin, so each gets its own service worker, storage and install. That's good for data isolation, but you build and test the same worker for many origins.

Use one shared `sw.js` that reads tenant config at runtime, a manifest generated per tenant (name, icons, colors, `id`), and keep cache names neutral. If tenants share a domain by path instead (`app.com/acme/`), storage is shared, so you must separate data by tenant in IndexedDB and caches yourself.

## 401: How do micro frontends share one service worker?

An origin and scope can only have one active worker per page, so separately deployed micro frontends can't each register their own worker for the same scope without replacing each other.

Common approaches: the shell app owns the only `sw.js` and loads route and caching rules from a config each micro frontend publishes (a JSON file the worker fetches), or each micro frontend lives under its own path and registers a worker with a narrower scope. The first keeps one update flow; the second gives teams independence but splits offline support.

## 402: PWA or Electron for a desktop app?

PWA: no installer, tiny download, automatic updates, runs in the user's browser engine, sandboxed. But only Chromium browsers support full desktop install features, and file system and OS access are limited.

Electron: full Node.js and OS access, the same Chromium on every machine, native menus and tray icons. But big downloads (100+ MB), you ship and patch Chromium yourself, and security is your responsibility.

Choose a PWA when web APIs cover what you need; choose Electron (or Tauri) for deep OS integration.

## 403: Capacitor or Trusted Web Activity for getting a PWA into stores?

A TWA (Android only) runs your live website in Chrome full screen. It has no native code, updates with your site, and uses the browser's features and limits.

Capacitor wraps your web app in a native WebView for Android and iOS, with plugins for native APIs (push through APNs/FCM, file system, biometrics). The app bundle ships inside the store package, so you get iOS support and native features but also store reviews for native changes.

Use a TWA for a simple Android listing; use Capacitor when you need iOS store presence or native APIs.

## 404: How do you handle a 409 conflict when syncing an offline change?

The server rejects a write because the record changed since the client's version. Options for the client:

1. Fetch the latest server version.
2. If the changed fields don't overlap, merge and retry automatically with the new version number.
3. If they overlap, keep both versions and ask the user, or apply the rule for that entity (for example server wins for prices).
4. Remove the item from the outbox only after it's resolved.

Never just drop the local change silently; at least keep it in a "conflicts" list.

## 405: Can a service worker leak information about which sites a user visited?

Without care, yes. Timing how long a cached request takes can show whether something was cached, which can hint at past visits (a cache timing attack, a kind of XS-Leak). The Cache API itself is per-origin, so other sites can't read it directly.

Browsers now partition storage and HTTP caches by top-level site, which blocks most cross-site versions of these attacks. On your own site, avoid exposing cache state through cross-origin readable endpoints.

## 406: How do CSP nonces cause problems with cached HTML?

A CSP nonce must be unique and random for every response. If the service worker caches HTML with a nonce in the CSP header and in `<script nonce>` tags, every visit served from cache reuses the same nonce, which weakens the protection.

Options: use hash-based CSP (`'sha256-...'`) for inline scripts instead of nonces when HTML is cached, or use network first for HTML so each response has a fresh nonce. Some setups rewrite nonces in the worker, but then the worker becomes part of your security boundary.

## 407: How do you build a simple router in a service worker without Workbox?

Keep an ordered list of matchers and handlers, and call the first match.

```js
const routes = [];
const route = (match, handler) => routes.push({ match, handler });

route(({ request }) => request.mode === "navigate", networkFirst);
route(({ url }) => url.pathname.startsWith("/static/"), cacheFirst);
route(({ request }) => request.destination === "image", cacheFirst);

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  const found = routes.find((r) => r.match({ request: event.request, url }));
  if (found) event.respondWith(found.handler(event.request));
});
```

`networkFirst` and `cacheFirst` would be your strategy functions that take a request and return a promise of a `Response`.

## 408: How can URLPattern help in a service worker?

`URLPattern` matches URLs with a path syntax similar to Express routes and gives you the matched parts.

```js
const articlePattern = new URLPattern({ pathname: "/articles/:slug" });

self.addEventListener("fetch", (event) => {
  const match = articlePattern.exec(event.request.url);
  if (match) {
    const { slug } = match.pathname.groups;
    event.respondWith(serveArticle(slug, event.request));
  }
});
```

It's supported in Chromium and in recent Firefox and Safari versions; use the `urlpattern-polyfill` package for older browsers. The Static Routing API also uses URL patterns for its conditions.

## 409: Why should a fetch handler avoid heavy synchronous work?

The service worker is single-threaded and handles all fetch events for all controlled tabs. If one handler parses a big JSON file or loops over thousands of cache keys synchronously, every other request waits, including images and scripts on the page.

Keep handlers small: decide quickly, return promises, move heavy work into `waitUntil` after responding, or do it in the page with a dedicated Web Worker.

## 410: How does Mock Service Worker (MSW) use service workers?

MSW registers a real service worker in the browser during development and tests. The worker forwards intercepted requests to the page over `MessageChannel`, where your handlers (written with `http.get('/api/user', ...)`) return mock responses. The worker then answers the request with that response.

Because it intercepts at the network level, your app code uses real `fetch` with no mocking in the code. In Node, MSW uses request interception modules instead of a service worker.

## 411: How do you test the service worker update flow automatically?

With Playwright and a test server you control:

1. Serve version A of `sw.js`, load the page, wait for `navigator.serviceWorker.ready`.
2. Change the server to serve version B.
3. Trigger `reg.update()` from `page.evaluate`.
4. Check that your "new version" banner appears.
5. Click it and check the page reloads with version B (for example a version string in the DOM).

This catches bugs in the `waiting`, `SKIP_WAITING` and `controllerchange` logic that are hard to test by hand.

## 412: How do you track service worker version adoption?

Put a version constant in the worker and report it.

```js
// sw.js
const SW_VERSION = "2026.11.25-1";
self.addEventListener("message", (event) => {
  if (event.data?.type === "GET_VERSION")
    event.ports[0].postMessage(SW_VERSION);
});
```

The page asks for the version on load (with a `MessageChannel`) and sends it to analytics together with the app version. A chart of versions over time shows how fast updates reach users and whether some users are stuck.

## 413: Explain what happens step by step on a repeat visit to a PWA with a cached app shell.

1. User opens the app; the browser sees the URL is in a registered scope.
2. The browser starts the service worker if it isn't running (and starts navigation preload if enabled).
3. The fetch event for the navigation runs; the worker returns `index.html` from Cache Storage.
4. The browser parses the HTML; requests for JS and CSS go through the worker and come from the precache.
5. The app renders the shell and reads local data from IndexedDB.
6. The app calls APIs; the worker applies network first or stale-while-revalidate.
7. In parallel, the browser checks `sw.js` for updates; if changed, a new worker installs and waits.

## 414: How do you handle large forms with photos offline on a phone with little storage?

- Resize and compress photos before storing them (with `createImageBitmap` and `OffscreenCanvas` in a worker, then `convertToBlob` to WebP or JPEG).
- Store blobs in IndexedDB or OPFS, not as base64 strings, which are about a third bigger.
- Check `storage.estimate()` before accepting new photos and warn the user.
- Upload and delete local copies as soon as the server confirms.
- Request persistent storage so the browser doesn't evict unsent data.

## 415: Why should you store binary data as Blobs and not base64 in IndexedDB?

IndexedDB can store `Blob`, `File` and `ArrayBuffer` values directly. Base64 strings are about 33% larger, need extra CPU to encode and decode, and the whole string has to be in memory.

Storing a `Blob` also lets you create an object URL (`URL.createObjectURL(blob)`) to show an image without copying data.

## 416: What happens to IndexedDB transactions that await unrelated promises?

An IndexedDB transaction auto-commits when no requests are pending and control returns to the event loop. If you `await fetch()` in the middle of a transaction, it commits before the fetch finishes, and the next operation throws `TransactionInactiveError`.

```js
// wrong
const tx = db.transaction("items", "readwrite");
const data = await (await fetch("/api/items")).json(); // tx closes here
await tx.store.put(data[0]); // error

// right: fetch first, then open the transaction
const data2 = await (await fetch("/api/items")).json();
const tx2 = db.transaction("items", "readwrite");
await Promise.all([...data2.map((i) => tx2.store.put(i)), tx2.done]);
```

## 417: How do you keep an IndexedDB connection healthy in a service worker?

Open the database lazily and reuse the promise while the worker is alive. Handle `versionchange` so a page that needs to upgrade the schema isn't blocked by the worker.

```js
let dbPromise;
function getDB() {
  dbPromise ??= openDB("app-db", 3, {
    upgrade: migrate,
    blocking() {
      dbPromise?.then((db) => db.close());
      dbPromise = undefined;
    },
  });
  return dbPromise;
}
```

When the worker stops, the connection closes automatically, and the next event opens it again.

## 418: How do you avoid flashes of old content with stale-while-revalidate?

Stale-while-revalidate shows the cached version first, then the new version only appears on the next load, or replaces the old one on screen if you listen for updates. Both can confuse users if the data changed a lot.

Options: use it only for data where old values are fine; use `BroadcastUpdatePlugin` and update the UI quietly with a small "Updated" note; or add an age limit so very old cached data falls back to network first.

## 419: How do Early Hints and service workers interact?

`103 Early Hints` lets the server tell the browser to preload resources before the final response. When a service worker handles the navigation, the browser doesn't send the request to the server directly, so early hints from the network aren't received in the same way.

If you rely on Early Hints for first visits, that's fine; on repeat visits the worker usually serves assets from cache anyway. With navigation preload, Chromium can process early hints on the preload request.

## 420: How do the Fetch event and CORS preflights interact?

Preflight `OPTIONS` requests are made by the browser's network layer and never reach the service worker. But when your worker calls `fetch()` for a cross-origin request with custom headers, the browser will send a preflight for that worker request.

So adding a header like `X-App-Version` to every API call in the worker can double the number of round trips to a cross-origin API. Only modify same-origin requests, or make sure the API caches preflights with `Access-Control-Max-Age`.

## 421: Why might cached fonts or images fail to render after being served by the worker?

Common causes:

- An opaque response returned for a request made in `cors` mode, like fonts (`@font-face` requests use CORS). The browser rejects it.
- A cached response with the wrong `Content-Type`, for example a captive portal HTML page cached as an image.
- A redirected response used for a request that doesn't allow it.

Check the console for "the response was opaque" or type errors, and only cache fonts with CORS responses.

## 422: How do you serve different cached content to installed and browser users?

The worker can't see `display-mode` directly, but the request can tell it. Use a `start_url` with a parameter (`/?mode=standalone`), or have the page send a message with `matchMedia('(display-mode: standalone)').matches`, and store that in IndexedDB for the worker.

Use it carefully: the same URL should usually give the same content, and differences belong in the client rendering.

## 423: What does the Payment Handler API let a PWA do?

It lets a PWA act as a payment app for other sites. The service worker registers payment instruments, and when a merchant site calls `PaymentRequest` with your payment method URL, the browser fires a `paymentrequest` event in your worker, which can open a window to complete the payment.

It is Chromium only and used by a small number of wallets. Most PWAs are on the other side, as merchants calling the Payment Request API.

## 424: How do you choose between Cache Storage, IndexedDB, OPFS and localStorage?

- **Cache Storage**: HTTP responses by URL, used by the service worker.
- **IndexedDB**: structured data, queries, blobs, outboxes; works in workers.
- **OPFS**: large files, random access, SQLite; fast in workers.
- **localStorage**: tiny settings only; synchronous, blocks the main thread, not available in workers.

Cookies are for things the server must see. Don't put large data in any synchronous storage.

## 425: How does SQLite in the browser work for offline PWAs?

The official SQLite WebAssembly build can store its database in OPFS using synchronous access handles inside a dedicated Web Worker. The app talks to that worker to run SQL. This gives real SQL with transactions and indexes, which is handy for complex offline apps.

Because the synchronous OPFS API only works in dedicated workers, the service worker can't use it directly. The service worker and page talk to the database worker or a SharedWorker instead.

## 426: What is the right way to show a notification permission prompt in a PWA?

1. Check `Notification.permission`. If `denied`, show settings help instead of a button.
2. Show your own UI first that explains what notifications you'll send ("Get a message when your order ships").
3. When the user taps "Yes", call `Notification.requestPermission()` in that click handler.
4. If granted, subscribe to push and save the subscription.
5. Offer a way to turn categories on and off in your settings, so users don't block everything.

The custom UI step protects your real permission from being denied forever.

## 427: How do you handle different push topics per user?

Store user preferences on the server (for example `orderUpdates: true, marketing: false`) and filter before sending. You can't subscribe one device to "topics" with plain web push; every message is sent to a specific subscription.

For large fan-outs by topic, keep a table that maps topics to subscriptions and send to each. Firebase Cloud Messaging offers topics on top of web push if you prefer a managed service.

## 428: How should you handle the push event when payload decryption fails or data is missing?

`event.data` can be `null` (a push without payload), and `json()` can throw on bad data. Still show something, since a push must produce a notification.

```js
self.addEventListener("push", (event) => {
  let data = {};
  try {
    data = event.data?.json() ?? {};
  } catch {
    data = { title: "New update", body: event.data?.text() };
  }
  event.waitUntil(
    self.registration.showNotification(data.title ?? "New update", {
      body: data.body ?? "Open the app to see what is new",
      data: { url: data.url ?? "/" },
    }),
  );
});
```

## 429: How do you avoid a stampede on your API when many users get the same push?

If a push to 1 million users makes every worker fetch `/api/latest` right away, your API gets a huge spike. Options:

- Put the content needed for the notification in the payload, so no fetch is needed.
- Fetch details only when the user clicks.
- Spread sends over minutes in the queue.
- Serve the shared data from a CDN with caching.

## 430: What should a service worker do on activate besides deleting caches?

- Enable navigation preload if used.
- Migrate IndexedDB data that the new version needs in a new format.
- Call `clients.claim()` if you want to control open pages right away.
- Notify clients of the new version, if useful.

Keep it short and wrapped in `waitUntil`: while `activate` runs, fetch events wait, so slow work here delays page loads.

## 431: Can fetch events be delayed by a slow activate?

Yes. Fetch events that arrive while the worker is activating are queued until the `activate` promise settles. If you run a big migration in `activate`, page loads hang during it.

Do only essential cleanup in `activate`. Move slow work to a later event, or do it lazily when the data is first used.

## 432: How do you handle multiple service worker files left over from old setups?

If you once registered `/service-worker.js` and now use `/sw.js`, users may still have the old registration, and it may control the same scope. A new `register('/sw.js')` with the same scope replaces it, since one scope can have one registration with a new script URL.

But if the old one had a different scope, it stays. Keep serving a kill switch at the old URL, and in the page you can find and unregister registrations whose `active.scriptURL` is the old one.

## 433: How does the browser handle a navigation when the worker fails to start?

If the worker script throws while starting, or the browser can't start it, Chromium falls back to the network for that request so the site still loads. A worker that crashes repeatedly may be skipped for a while.

That's one reason a broken worker doesn't always make the site unusable. A worker that starts but returns bad responses is much worse, because the browser trusts what it returns.

## 434: How do you make sure the offline page itself always works?

- Precache it, with all its CSS, images and fonts, or inline them so it's one file.
- Don't load JS bundles that depend on the network.
- Test it by blocking the network after install.
- Give it a "Retry" button that reloads.
- Keep it small so it never fails to install.

An offline page that tries to load the main app bundle from the network will show a blank screen.

## 435: How do you design caching for an app that updates content every minute, like a sports scores app?

- HTML shell and assets: precache.
- Score API: network first with a short timeout and a small cache, or network only with the last value from IndexedDB as fallback.
- Show the time of the last update clearly when offline.
- Push for important events (goals) with `Topic` per match so old ones are replaced.
- Avoid stale-while-revalidate for scores; showing an old score as current is worse than showing a loading state.

## 436: How do you keep the app and the service worker using the same version of shared code?

If the page and the worker share code (for example a data model or IndexedDB schema), they can be out of sync during updates: a new page with an old worker, or the other way.

Options: bundle shared code into both from the same build and update them together (reload on `controllerchange`), version messages and schemas so each side can tell, and make the worker tolerate older pages for one version.

## 437: What are the risks of caching POST responses by URL?

Workbox and the Cache API won't cache POST requests directly, but some apps work around it by caching a POST response under a GET key. That can serve one user's search result or form result to another request with a different body, because the body isn't part of the key.

If you need to cache POST-based queries (like GraphQL), build a key from a hash of the body and store it separately, and only for queries that don't change data.

## 438: How do you add offline support to a GraphQL app?

GraphQL usually uses POST to one URL, so URL-based caching doesn't work. Better options:

- Use the client's own cache (Apollo or urql) and persist it to IndexedDB (`apollo3-cache-persist` or similar).
- Use persisted queries sent as GET with a hash, which can then be cached by URL.
- Queue mutations in an outbox for offline writes.

The service worker then mostly handles the shell and static assets.

## 439: How do you handle authentication expiry for queued offline requests?

When the user comes back online days later, their session may be expired, and replaying the queue returns 401.

Stop the replay on 401 instead of dropping the items, ask the user to log in again, then resume. Don't store passwords to re-login automatically. With refresh tokens in HttpOnly cookies, the server can often refresh the session on the first request, so make the replay go through the same refresh logic the app uses.

## 440: How do browsers stop a malicious page from installing a fake PWA of a bank?

The install dialog shows the app's origin, and name and icon changes later need user approval. The installed window shows the origin when navigating out of scope, and Chromium shows the origin briefly when the app opens. Phishing sites can still make an app that looks like a bank, so browsers rely on Safe Browsing and other protections too.

As a developer of a real brand, publish your app through official channels and teach users where to install it from.

## 441: What is the "update on navigation" problem in SPAs?

An SPA uses client-side routing, so after the first load there are no real navigations, and the browser never re-checks `sw.js`. A user who keeps the tab open for a week runs old code all week.

Fix with periodic `reg.update()` calls, on `visibilitychange` and on route changes, then show the update prompt when a new worker is waiting.

## 442: How would you add PWA features to a large existing site step by step?

1. Add a manifest and icons; check installability.
2. Add a minimal worker with only an offline fallback page.
3. Add precaching for hashed static assets.
4. Add runtime caching for images and fonts with limits.
5. Add network first HTML with a timeout for key pages.
6. Add push for one clear use case.
7. Add offline data with IndexedDB for the main feature.

Ship each step separately with monitoring, so you know which change caused any problem.

## 443: What should be in a PWA code review checklist?

- Every cache has a name, version and size or age limit.
- No error, opaque or auth-specific responses cached by accident.
- Non-GET and third-party requests are skipped unless needed.
- `waitUntil` and `respondWith` used correctly.
- Update flow handles waiting workers and reloads.
- No secrets in caches or IndexedDB without need.
- `sw.js` served with `no-cache`, not precached.
- Offline and update flows covered by tests.
- Feature detection for every non-universal API.

## 444: What new or recent PWA-related features should a senior developer know about?

- Static Routing API to skip the worker for some requests (Chromium).
- Declarative Web Push (Safari).
- Storage Buckets (Chromium).
- `launch_handler`, `scope_extensions` and tabbed mode in the manifest (Chromium).
- Module service workers across all major browsers.
- Installability no longer needing a fetch handler in Chrome.
- Lighthouse dropping its PWA category.
- Firefox working on desktop web app support.

The direction is clear: fewer special requirements for "PWA", and more web app features available to any site.

## 445: Why did Chrome stop requiring a service worker for installability?

Many sites added an empty or useless fetch handler only to pass the install check, which slowed every request and gave no offline benefit. The requirement didn't really guarantee a good offline experience either.

Chrome removed the fetch handler requirement so sites can be installable based on the manifest alone, and now treats offline support as a quality feature, not a gate.

## 446: How do you explain the difference between "installable" and "a good PWA"?

Installable is a low bar: HTTPS and a valid manifest. A good PWA also loads fast on bad networks, works offline for its main use cases, keeps user data safe through network failures, updates without breaking, respects permissions, and feels native in the window it runs in.

In interviews, focus on reliability and user experience, not just the checklist.

## 447: How do you build an "offline-ready" indicator that is honest?

Only show "Ready to work offline" after the worker is active and the precache finished, for example on the first `controllerchange` or from the Workbox `installed` event when there was no previous controller.

For data features, mark each item ("Available offline") based on whether its data is really in IndexedDB or a cache, not on a general flag. If storage is not persistent, say that the browser may clear it.

## 448: How do you decide which features to show when offline?

Group features into three buckets:

- **Works fully offline**: reading cached content, editing drafts, local search.
- **Works with a delay**: actions that can be queued (send message, save form).
- **Needs the network**: payments, live search, new content, account changes.

Show the first normally, mark the second with "will sync", and disable the third with a clear reason. Avoid hiding features without saying why.

## 449: How would you explain service workers to a non-technical stakeholder?

A service worker is a small helper the website installs in the browser. It sits between the app and the internet. When the internet is slow or gone, it can answer from a local copy, so the app still opens and the user can keep working. It also lets us send notifications and get updates out without an app store.

The trade-off: it needs careful updates and testing, because a mistake can keep users on an old version.

## 450: Design an offline-first PWA for a team task manager. What are the key decisions?

- **Platform**: PWA with install promotion, TWA for Google Play; iOS users add to home screen.
- **Shell**: precache with Workbox `injectManifest`; update prompt with `workbox-window`.
- **Data**: tasks and projects in IndexedDB; sync engine with cursors, outbox with idempotency keys, field-level merge for task edits, tombstones for deletes.
- **Sync triggers**: on app start, on `online`, background sync on Chromium, Web Locks to keep it to one tab.
- **Real time**: WebSocket or SSE while open, push for assignments and mentions with tags per task.
- **Storage**: request persistence, limits on attachments, OPFS for large files.
- **Security**: HttpOnly cookies, clear data on logout, no tokens in caches.
- **Quality**: Playwright offline and update tests, RUM split by controlled/uncontrolled, version telemetry, and a kill switch ready.
