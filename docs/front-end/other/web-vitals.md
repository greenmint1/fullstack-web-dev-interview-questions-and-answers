# Web Vitals Interview Questions and Answers

_Last updated: October 28, 2026_

90 Web Vitals interview questions with answers, split into three levels: 30 easy, 30 moderate and 30 advanced.

The answers follow the Core Web Vitals as they are in 2026: LCP, INP and CLS, plus the supporting metrics FCP and TTFB. Code examples use the `web-vitals` library v6 and the browser Performance APIs. FID, which INP replaced in March 2024, is mentioned only as legacy.

## Table of Contents

- [Easy Questions (1-30)](#easy-questions-1-30)
- [Moderate Questions (31-60)](#moderate-questions-31-60)
- [Advanced Questions (61-90)](#advanced-questions-61-90)

### Easy Questions (1-30)

- [1: What are Web Vitals?](#1-what-are-web-vitals)
- [2: What are Core Web Vitals?](#2-what-are-core-web-vitals)
- [3: What is LCP?](#3-what-is-lcp)
- [4: What is a good LCP score?](#4-what-is-a-good-lcp-score)
- [5: Which elements can be the LCP element?](#5-which-elements-can-be-the-lcp-element)
- [6: What is INP?](#6-what-is-inp)
- [7: What is a good INP score?](#7-what-is-a-good-inp-score)
- [8: Which interactions count for INP?](#8-which-interactions-count-for-inp)
- [9: What is CLS?](#9-what-is-cls)
- [10: What is a good CLS score?](#10-what-is-a-good-cls-score)
- [11: What are common causes of layout shifts?](#11-what-are-common-causes-of-layout-shifts)
- [12: What happened to FID?](#12-what-happened-to-fid)
- [13: What is TTFB?](#13-what-is-ttfb)
- [14: What is FCP?](#14-what-is-fcp)
- [15: What is the difference between FCP and LCP?](#15-what-is-the-difference-between-fcp-and-lcp)
- [16: Why are Web Vitals measured at the 75th percentile?](#16-why-are-web-vitals-measured-at-the-75th-percentile)
- [17: What is the difference between lab data and field data?](#17-what-is-the-difference-between-lab-data-and-field-data)
- [18: What is CrUX?](#18-what-is-crux)
- [19: What is Lighthouse?](#19-what-is-lighthouse)
- [20: What is PageSpeed Insights?](#20-what-is-pagespeed-insights)
- [21: Why are Web Vitals reported separately for mobile and desktop?](#21-why-are-web-vitals-reported-separately-for-mobile-and-desktop)
- [22: Do Core Web Vitals affect SEO?](#22-do-core-web-vitals-affect-seo)
- [23: What is the web-vitals library and how do you use it?](#23-what-is-the-web-vitals-library-and-how-do-you-use-it)
- [24: How do you check Web Vitals in Chrome DevTools?](#24-how-do-you-check-web-vitals-in-chrome-devtools)
- [25: Why can't Lighthouse measure INP?](#25-why-cant-lighthouse-measure-inp)
- [26: What is Total Blocking Time (TBT)?](#26-what-is-total-blocking-time-tbt)
- [27: What is a long task?](#27-what-is-a-long-task)
- [28: How do you prevent layout shifts caused by images?](#28-how-do-you-prevent-layout-shifts-caused-by-images)
- [29: Which layout shifts are not counted in CLS?](#29-which-layout-shifts-are-not-counted-in-cls)
- [30: Which browsers support Core Web Vitals measurement?](#30-which-browsers-support-core-web-vitals-measurement)

### Moderate Questions (31-60)

- [31: What are the four parts of LCP?](#31-what-are-the-four-parts-of-lcp)
- [32: How do you make the LCP image load faster?](#32-how-do-you-make-the-lcp-image-load-faster)
- [33: Why shouldn't you lazy-load the LCP image?](#33-why-shouldnt-you-lazy-load-the-lcp-image)
- [34: What does the fetchpriority attribute do?](#34-what-does-the-fetchpriority-attribute-do)
- [35: What is the difference between preload, preconnect and dns-prefetch?](#35-what-is-the-difference-between-preload-preconnect-and-dns-prefetch)
- [36: How do web fonts affect LCP and CLS?](#36-how-do-web-fonts-affect-lcp-and-cls)
- [37: How do render-blocking CSS and JavaScript affect LCP?](#37-how-do-render-blocking-css-and-javascript-affect-lcp)
- [38: What are the three parts of INP?](#38-what-are-the-three-parts-of-inp)
- [39: How do you break up long tasks?](#39-how-do-you-break-up-long-tasks)
- [40: How do you make an event handler respond faster?](#40-how-do-you-make-an-event-handler-respond-faster)
- [41: What is layout thrashing and how does it hurt INP?](#41-what-is-layout-thrashing-and-how-does-it-hurt-inp)
- [42: How do you prevent layout shifts from ads, embeds and dynamic content?](#42-how-do-you-prevent-layout-shifts-from-ads-embeds-and-dynamic-content)
- [43: How do animations affect CLS?](#43-how-do-animations-affect-cls)
- [44: How do you send Web Vitals data to your analytics?](#44-how-do-you-send-web-vitals-data-to-your-analytics)
- [45: What do value, delta, id and rating mean in the web-vitals metric object?](#45-what-do-value-delta-id-and-rating-mean-in-the-web-vitals-metric-object)
- [46: What is the attribution build of web-vitals?](#46-what-is-the-attribution-build-of-web-vitals)
- [47: How can you access CrUX data?](#47-how-can-you-access-crux-data)
- [48: Why are Lighthouse numbers different from field data?](#48-why-are-lighthouse-numbers-different-from-field-data)
- [49: How do you use Lighthouse in CI to catch regressions?](#49-how-do-you-use-lighthouse-in-ci-to-catch-regressions)
- [50: How do you improve TTFB?](#50-how-do-you-improve-ttfb)
- [51: What is the back/forward cache and how does it help Web Vitals?](#51-what-is-the-backforward-cache-and-how-does-it-help-web-vitals)
- [52: How does client-side rendering affect LCP compared to server-side rendering?](#52-how-does-client-side-rendering-affect-lcp-compared-to-server-side-rendering)
- [53: How do third-party scripts affect Web Vitals?](#53-how-do-third-party-scripts-affect-web-vitals)
- [54: What is content-visibility and how can it help?](#54-what-is-content-visibility-and-how-can-it-help)
- [55: How do image size and format affect LCP?](#55-how-do-image-size-and-format-affect-lcp)
- [56: How does the Core Web Vitals report in Search Console work?](#56-how-does-the-core-web-vitals-report-in-search-console-work)
- [57: When does a page "pass" the Core Web Vitals assessment?](#57-when-does-a-page-pass-the-core-web-vitals-assessment)
- [58: How can cookie banners and late-loading UI hurt CLS and LCP?](#58-how-can-cookie-banners-and-late-loading-ui-hurt-cls-and-lcp)
- [59: What is an infinite scroll and how do you keep it from causing CLS?](#59-what-is-an-infinite-scroll-and-how-do-you-keep-it-from-causing-cls)
- [60: How do you find the cause of a poor INP using Chrome DevTools?](#60-how-do-you-find-the-cause-of-a-poor-inp-using-chrome-devtools)

### Advanced Questions (61-90)

- [61: How is the CLS score calculated?](#61-how-is-the-cls-score-calculated)
- [62: What are session windows in CLS and why were they added?](#62-what-are-session-windows-in-cls-and-why-were-they-added)
- [63: How exactly is INP calculated?](#63-how-exactly-is-inp-calculated)
- [64: When does the browser stop looking for a new LCP candidate?](#64-when-does-the-browser-stop-looking-for-a-new-lcp-candidate)
- [65: How do you measure LCP and CLS yourself with PerformanceObserver?](#65-how-do-you-measure-lcp-and-cls-yourself-with-performanceobserver)
- [66: What is the Event Timing API and what is durationThreshold?](#66-what-is-the-event-timing-api-and-what-is-durationthreshold)
- [67: What is the Long Animation Frames API and how does it help with INP?](#67-what-is-the-long-animation-frames-api-and-how-does-it-help-with-inp)
- [68: How are Web Vitals measured in single-page apps with soft navigations?](#68-how-are-web-vitals-measured-in-single-page-apps-with-soft-navigations)
- [69: How do prerendering and the Speculation Rules API affect Web Vitals?](#69-how-do-prerendering-and-the-speculation-rules-api-affect-web-vitals)
- [70: How do iframes affect Web Vitals?](#70-how-do-iframes-affect-web-vitals)
- [71: How does a page restored from bfcache report metrics?](#71-how-does-a-page-restored-from-bfcache-report-metrics)
- [72: Why can your RUM data differ from CrUX?](#72-why-can-your-rum-data-differ-from-crux)
- [73: How does hydration affect INP?](#73-how-does-hydration-affect-inp)
- [74: How can the Server-Timing header help with Web Vitals?](#74-how-can-the-server-timing-header-help-with-web-vitals)
- [75: What are 103 Early Hints and how can they help LCP?](#75-what-are-103-early-hints-and-how-can-they-help-lcp)
- [76: The LCP image downloads quickly, but LCP is still slow. What could cause it?](#76-the-lcp-image-downloads-quickly-but-lcp-is-still-slow-what-could-cause-it)
- [77: How do client-side A/B testing tools affect Web Vitals?](#77-how-do-client-side-ab-testing-tools-affect-web-vitals)
- [78: What is the difference between scheduler.yield() and setTimeout(0) for yielding?](#78-what-is-the-difference-between-scheduleryield-and-settimeout0-for-yielding)
- [79: How does DOM size affect INP and how do you handle very large DOMs?](#79-how-does-dom-size-affect-inp-and-how-do-you-handle-very-large-doms)
- [80: How do you reduce presentation delay in INP?](#80-how-do-you-reduce-presentation-delay-in-inp)
- [81: How would you design a RUM pipeline for Web Vitals at scale?](#81-how-would-you-design-a-rum-pipeline-for-web-vitals-at-scale)
- [82: Why shouldn't you average Web Vitals values?](#82-why-shouldnt-you-average-web-vitals-values)
- [83: How do you prevent Web Vitals regressions in a team?](#83-how-do-you-prevent-web-vitals-regressions-in-a-team)
- [84: Scenario: LCP is good in Lighthouse but poor in field data. How do you investigate?](#84-scenario-lcp-is-good-in-lighthouse-but-poor-in-field-data-how-do-you-investigate)
- [85: Scenario: INP is poor on mobile on a product listing page with filters. How do you approach it?](#85-scenario-inp-is-poor-on-mobile-on-a-product-listing-page-with-filters-how-do-you-approach-it)
- [86: Scenario: CLS jumped after a release. How do you find the cause?](#86-scenario-cls-jumped-after-a-release-how-do-you-find-the-cause)
- [87: Scenario: TTFB is poor for users in some countries. What do you do?](#87-scenario-ttfb-is-poor-for-users-in-some-countries-what-do-you-do)
- [88: When does moving work to a Web Worker help INP, and what are its limits?](#88-when-does-moving-work-to-a-web-worker-help-inp-and-what-are-its-limits)
- [89: How do you measure the performance of a specific element or user flow beyond Core Web Vitals?](#89-how-do-you-measure-the-performance-of-a-specific-element-or-user-flow-beyond-core-web-vitals)
- [90: How do Core Web Vitals change over time, and how do you keep up?](#90-how-do-core-web-vitals-change-over-time-and-how-do-you-keep-up)

---

# Easy Questions (1-30)

## 1: What are Web Vitals?

Web Vitals is a Google initiative that gives a set of metrics for measuring how real users experience a page. Before it, there were many different performance numbers and teams didn't know which ones mattered. Web Vitals picks a small set and gives each one a clear "good" target.

The metrics cover three things: how fast the main content loads, how fast the page reacts when you click or type, and how stable the layout is while the page loads.

## 2: What are Core Web Vitals?

Core Web Vitals are the three most important Web Vitals. Google says every site should track them:

- **LCP (Largest Contentful Paint)**: loading speed
- **INP (Interaction to Next Paint)**: responsiveness
- **CLS (Cumulative Layout Shift)**: visual stability

They are measured on real users and used in Google Search ranking. Other metrics like TTFB and FCP are not "core", but they help you find out why a core metric is bad.

## 3: What is LCP?

Largest Contentful Paint is the time from when the user starts loading the page until the biggest image or text block in the viewport is rendered. It's a simple way to answer "when did the user see the main content?".

For most pages, the LCP element is a hero image, a product photo, a banner or a big heading. The browser can report several LCP candidates while the page loads, as bigger elements appear. The last one before the user interacts with the page is the final LCP.

## 4: What is a good LCP score?

| Rating            | LCP           |
| ----------------- | ------------- |
| Good              | 2.5 s or less |
| Needs improvement | 2.5 s to 4 s  |
| Poor              | more than 4 s |

The score is checked at the 75th percentile of page loads, split by mobile and desktop. So at least 75% of visits should have LCP of 2.5 seconds or less.

## 5: Which elements can be the LCP element?

- `<img>` elements (the first frame for animated images like GIFs)
- `<image>` elements inside `<svg>`
- `<video>` elements (the poster image or the first frame)
- Elements with a background image loaded with `url()` in CSS
- Block-level elements that contain text

The browser ignores some elements, for example ones with `opacity: 0`, images that cover the whole viewport (treated as background) and placeholder images with very little detail. Only the part of the element that is visible in the viewport counts for its size.

## 6: What is INP?

Interaction to Next Paint measures how quickly the page shows a visual response after the user interacts with it. For each click, tap or key press, the browser measures the time from the input until the next frame is painted. At the end of the visit, INP is (roughly) the slowest interaction.

A low INP means the page feels fast when you use it. A high INP means the user clicks a button and nothing happens for a while, which often makes them click again or leave.

## 7: What is a good INP score?

| Rating            | INP              |
| ----------------- | ---------------- |
| Good              | 200 ms or less   |
| Needs improvement | 200 ms to 500 ms |
| Poor              | more than 500 ms |

As with the other Core Web Vitals, it's checked at the 75th percentile of page visits.

## 8: Which interactions count for INP?

Only these:

- mouse clicks
- taps on a touchscreen
- key presses on a physical or on-screen keyboard

Scrolling, hovering and zooming are not counted. Note that a keyboard or click handler that runs during scrolling can still make a later interaction slow, but the scroll itself is not an interaction for INP.

If the user never clicks, taps or types, the page has no INP value.

## 9: What is CLS?

Cumulative Layout Shift measures how much visible content moves around unexpectedly while the user is on the page. A layout shift happens when an element that is already on screen changes its position between two frames, for example because an image or ad loaded above it and pushed it down.

CLS is a score without units. It's not a time. A page where nothing moves has a CLS of 0.

## 10: What is a good CLS score?

| Rating            | CLS            |
| ----------------- | -------------- |
| Good              | 0.1 or less    |
| Needs improvement | 0.1 to 0.25    |
| Poor              | more than 0.25 |

Checked at the 75th percentile of page visits.

## 11: What are common causes of layout shifts?

- Images and videos without `width` and `height` (or `aspect-ratio`), so the browser doesn't know how much space to keep
- Ads, embeds and iframes that load later and have no reserved space
- Content added at the top of the page after load, like cookie banners, promo bars or "app install" banners
- Web fonts that swap in and have different sizes than the fallback font
- Animations that change `top`, `left`, `width`, `height` or `margin` instead of `transform`
- Content that loads from an API and replaces a smaller placeholder

## 12: What happened to FID?

First Input Delay (FID) was the responsiveness metric in Core Web Vitals. It only measured the delay before the browser could start handling the **first** interaction. It didn't measure how long the event handlers ran or how long it took to paint the result, and it ignored all later interactions.

On March 12, 2024, INP replaced FID as a Core Web Vital. FID is deprecated, and the `web-vitals` library removed `onFID()` in version 5. If you see FID in old dashboards or blog posts, it's legacy.

## 13: What is TTFB?

Time to First Byte is the time from the start of the navigation until the browser gets the first byte of the HTML response. It includes redirects, service worker startup, DNS lookup, connection setup (TCP and TLS) and the time the server needs to start sending the response.

| Rating            | TTFB            |
| ----------------- | --------------- |
| Good              | 0.8 s or less   |
| Needs improvement | 0.8 s to 1.8 s  |
| Poor              | more than 1.8 s |

TTFB is not a Core Web Vital, but a slow TTFB makes FCP and LCP slow too, because nothing can render before the HTML arrives.

## 14: What is FCP?

First Contentful Paint is the time from the start of the navigation until the browser renders the first piece of content: text, an image, an SVG or a non-white `<canvas>`. It tells the user "something is happening".

| Rating            | FCP           |
| ----------------- | ------------- |
| Good              | 1.8 s or less |
| Needs improvement | 1.8 s to 3 s  |
| Poor              | more than 3 s |

## 15: What is the difference between FCP and LCP?

FCP is when the **first** content shows up. That could be a small logo, a loading spinner text or a nav bar. LCP is when the **largest** content element shows up, which is usually the main thing the user came for.

A page can have a fast FCP and a slow LCP. For example, the header renders right away, but the hero image takes 4 seconds. That's why LCP is the Core Web Vital and FCP is only a supporting metric.

## 16: Why are Web Vitals measured at the 75th percentile?

Users have very different devices and networks, so the same page can load in 1 second for one person and 6 seconds for another. An average hides this. The 75th percentile means "75% of visits were this good or better".

It's a balance. It's high enough that most users get a good experience, but it isn't affected too much by a few extreme outliers, like someone on a broken train Wi-Fi.

## 17: What is the difference between lab data and field data?

**Lab data** is collected in a controlled environment: one device, one network speed, one location. Lighthouse and the DevTools Performance panel give lab data. It's repeatable and good for debugging and testing before release.

**Field data** (also called RUM, real user monitoring) is collected from real users visiting your site. CrUX and the `web-vitals` library give field data. It shows what users actually experience, but it's noisier and harder to debug.

Google uses field data for search ranking. Use field data to know if you have a problem, and lab data to find out why.

## 18: What is CrUX?

The Chrome User Experience Report (CrUX) is a public dataset of real-user performance data collected by Chrome. It includes Core Web Vitals and other metrics for millions of websites, at origin level and for popular URLs.

Data only comes from Chrome users who opted in to sharing usage statistics, and only for pages that are public and have enough traffic. It uses a rolling 28-day window. Google Search uses CrUX for the page experience signal, and tools like PageSpeed Insights and Search Console show CrUX data.

## 19: What is Lighthouse?

Lighthouse is an open-source tool from Google that runs an automated audit of a page. It loads the page in a simulated environment (by default a mid-range mobile device with a slow network) and reports scores for performance, accessibility, best practices and SEO.

The performance score is based on lab metrics like FCP, LCP, TBT, CLS and Speed Index. You can run it from Chrome DevTools, from the command line, from Node.js or through PageSpeed Insights.

A good Lighthouse score doesn't guarantee good Core Web Vitals for real users. It's a lab test.

## 20: What is PageSpeed Insights?

PageSpeed Insights (pagespeed.web.dev) is a free Google tool. You enter a URL and it shows two things:

1. **Field data from CrUX**: real-user LCP, INP, CLS, FCP and TTFB for that URL and origin, if there's enough traffic.
2. **Lab data from Lighthouse**: a test run on Google's servers with suggestions on what to fix.

The field data part at the top is the one that tells you whether the page passes Core Web Vitals.

## 21: Why are Web Vitals reported separately for mobile and desktop?

Mobile and desktop users have very different conditions. Phones usually have slower CPUs and worse network connections, and the layout is different, so the LCP element can even be a different element. If you mix them, good desktop numbers can hide bad mobile numbers.

CrUX, PageSpeed Insights and Search Console all show mobile and desktop data separately, and Google Search uses the data that matches the device of the person searching.

## 22: Do Core Web Vitals affect SEO?

Yes, but not a lot. Core Web Vitals are part of Google's page experience signals, which are used in ranking. Google has said many times that relevant, helpful content matters much more. Good Core Web Vitals won't make a weak page rank first.

Where they matter most is when several pages are similar in quality. And besides SEO, faster and more stable pages usually have better conversion rates and lower bounce rates, which is often a bigger reason to care.

## 23: What is the web-vitals library and how do you use it?

`web-vitals` is a small JavaScript library (around 2-3 KB compressed) from the Chrome team. It measures Core Web Vitals and other metrics on real users in the same way Chrome and CrUX measure them.

```bash
npm install web-vitals
```

```js
import { onCLS, onINP, onLCP, onFCP, onTTFB } from "web-vitals";

onCLS(console.log);
onINP(console.log);
onLCP(console.log);
onFCP(console.log);
onTTFB(console.log);
```

Each function takes a callback that gets a metric object with `name`, `value`, `rating` and other fields. In a real app you send these values to your analytics instead of logging them.

## 24: How do you check Web Vitals in Chrome DevTools?

Open the **Performance** panel. Before you even record anything, it shows live local values for LCP, CLS and INP as you use the page. If the page has CrUX data, it can also show the field values next to them so you can compare.

To dig deeper, click record, reload or interact with the page, and stop. The trace shows the LCP element, layout shifts and each interaction with its timing breakdown.

You can also turn on CPU and network throttling to see how the page behaves on a slower device.

## 25: Why can't Lighthouse measure INP?

INP needs real user interactions, and Lighthouse just loads the page without clicking or typing. So it can't know which interactions will be slow.

Lighthouse uses **Total Blocking Time (TBT)** instead. TBT shows how much the main thread was blocked during load, and pages with high TBT usually have bad INP. For actual INP in the lab, you can use the Lighthouse "Timespan" mode, where you interact with the page yourself, or the DevTools Performance panel.

## 26: What is Total Blocking Time (TBT)?

TBT is a lab metric. It adds up the "blocking" part of every long task between FCP and the time the page becomes fully interactive. The blocking part is anything over 50 ms. For example, a task of 120 ms adds 70 ms to TBT.

It's a good indicator of how busy the main thread is during load. If TBT is high, the page will probably feel slow when users try to interact with it early, which hurts INP.

## 27: What is a long task?

A long task is any task on the main thread that runs for more than 50 ms. While it runs, the browser can't respond to user input or paint new frames, so clicks and key presses have to wait.

Long tasks usually come from big JavaScript bundles being parsed and executed, heavy event handlers, rendering large lists, or third-party scripts. You can see them in the DevTools Performance panel as tasks with a red corner.

## 28: How do you prevent layout shifts caused by images?

Always tell the browser how big the image will be before it downloads. The simplest way is to set `width` and `height` attributes. Browsers use them to calculate the aspect ratio and reserve space, even if CSS makes the image responsive.

```html
<img src="/photo.jpg" width="800" height="600" alt="Product photo" />
```

```css
img {
  max-width: 100%;
  height: auto;
}
```

For elements where you don't have fixed dimensions, like a container for an embed, use the CSS `aspect-ratio` property or a `min-height`.

## 29: Which layout shifts are not counted in CLS?

- **Shifts right after user input.** Shifts that happen within 500 ms of a click, tap or key press are excluded, because the user expects the page to change. These entries have `hadRecentInput: true`. Scrolling doesn't count as input here.
- **Elements that are added for the first time.** A new element appearing isn't a shift. Only existing elements moving count.
- **Transform animations.** Moving an element with CSS `transform` doesn't cause a layout shift.
- **Content outside the viewport.** Shifts of elements the user can't see don't count.

## 30: Which browsers support Core Web Vitals measurement?

All metrics work in Chromium browsers (Chrome, Edge, Opera and others).

Since Safari 26.2 (December 2025), LCP and INP are supported in all major browsers, and they are now Baseline Newly available. Firefox had support for both a bit earlier. FCP and TTFB have worked everywhere for a long time.

CLS is still only available in Chromium, because the Layout Instability API isn't supported by Firefox or Safari. Keep in mind that CrUX only contains Chrome data, so Google's official numbers come only from Chrome users.

# Moderate Questions (31-60)

## 31: What are the four parts of LCP?

LCP can be split into four parts that follow each other:

1. **Time to First Byte**: until the first byte of HTML arrives.
2. **Resource load delay**: from TTFB until the browser starts downloading the LCP resource (for example the hero image).
3. **Resource load duration**: how long the LCP resource takes to download.
4. **Element render delay**: from when the resource finished downloading until the element is actually painted.

If the LCP element is text, parts 2 and 3 are zero. Splitting LCP like this tells you where to look. A big load delay usually means the browser found the image late. A big render delay usually means the main thread was busy or something was blocking rendering. In a well optimized page, most of the time is in TTFB and load duration, and the two delays are small.

## 32: How do you make the LCP image load faster?

- Put it in the HTML as a normal `<img>`, not as a CSS background or something added by JavaScript, so the preload scanner finds it early.
- Add `fetchpriority="high"` so the browser downloads it before other images.
- Don't lazy-load it.
- Serve the right size with `srcset` and `sizes`, and use modern formats like AVIF or WebP.
- Serve it from the same origin or a fast CDN, or `preconnect` to the image host.
- If it has to be a CSS background or is discovered late, use `<link rel="preload">`.

```html
<img
  src="/hero-1200.avif"
  srcset="/hero-600.avif 600w, /hero-1200.avif 1200w"
  sizes="100vw"
  width="1200"
  height="600"
  fetchpriority="high"
  alt="Summer sale"
/>
```

## 33: Why shouldn't you lazy-load the LCP image?

`loading="lazy"` tells the browser to wait until it knows the image is near the viewport. To know that, it has to do layout first, which only happens after the CSS is loaded. So the download starts later than it would for a normal image, and LCP gets slower.

Lazy loading is great for images below the fold. A common mistake is a component or CMS that adds `loading="lazy"` to every image, including the hero. Lazy-load everything except images that are likely to be in the first viewport.

## 34: What does the fetchpriority attribute do?

`fetchpriority` gives the browser a hint about how important a resource is compared to others of the same type. The values are `high`, `low` and `auto` (default).

By default, Chrome loads images with low priority until it knows they are in the viewport, and only the first few large images get a small boost. With `fetchpriority="high"`, the LCP image starts with high priority right away.

```html
<img src="/hero.jpg" fetchpriority="high" alt="" />
<link rel="preload" href="/hero.jpg" as="image" fetchpriority="high" />
<img src="/carousel-slide-2.jpg" fetchpriority="low" alt="" />
```

It's a hint, not a command, and it should be used on one or two resources. If everything is high priority, nothing is.

## 35: What is the difference between preload, preconnect and dns-prefetch?

- **`dns-prefetch`**: only resolves the DNS of another domain. Very cheap.
- **`preconnect`**: resolves DNS and also opens the TCP and TLS connection, so a later request to that origin can start right away. Use it for a few important origins, like your image CDN or font host.
- **`preload`**: actually downloads a specific file early, because you know the page needs it soon. Use it for resources the browser finds late, like a font referenced in CSS or a background image.

```html
<link rel="preconnect" href="https://cdn.example.com" />
<link rel="dns-prefetch" href="https://analytics.example.com" />
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>
```

Too many preloads compete with each other for bandwidth and can make LCP worse.

## 36: How do web fonts affect LCP and CLS?

If the LCP element is text, it can't be painted until a font is available. With the default `font-display: auto`, most browsers hide the text for up to 3 seconds while the font loads, which delays LCP.

When the font finally loads and replaces the fallback font, the text can change size and push content around, which causes CLS.

Fixes:

- Use `font-display: swap` or `optional`. `optional` is best for CLS, because if the font isn't ready very quickly, the fallback is used for that page view.
- Preload the main font file and self-host it.
- Use fallback font metrics (`size-adjust`, `ascent-override`, `descent-override`) so the fallback takes the same space.

```css
@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
}

body {
  font-family: "Inter", "Inter Fallback", sans-serif;
}
```

## 37: How do render-blocking CSS and JavaScript affect LCP?

By default, the browser won't render anything until all CSS in the `<head>` is downloaded and parsed. Classic `<script>` tags without `async` or `defer` also block HTML parsing. So a large CSS file or a slow script delays FCP and LCP, even if the LCP image is already downloaded.

How to reduce it:

- Add `defer` (or `type="module"`) to scripts that aren't needed for the first render.
- Keep CSS small, inline the critical CSS for the first viewport and load the rest later.
- Remove unused CSS and JS.
- Avoid `@import` in CSS, because it creates a chain of requests.

## 38: What are the three parts of INP?

Each interaction has three parts:

1. **Input delay**: time from the user's input until the event handlers start running. It's long when the main thread is busy with another task.
2. **Processing duration**: time spent running all event handlers for the interaction (`pointerdown`, `pointerup`, `click`, `keydown` and so on).
3. **Presentation delay**: time from when the handlers finish until the next frame is painted. This includes style recalculation, layout, paint and compositing.

Knowing which part is large tells you what to fix. Long input delay means other tasks are in the way. Long processing means your handlers are too heavy. Long presentation delay means the DOM update is too big or too complex.

## 39: How do you break up long tasks?

Split the work into smaller pieces and give control back to the browser (yield) between them, so it can handle user input and paint. The modern way is `scheduler.yield()`. It's supported in Chromium and Firefox, so use a fallback for other browsers.

```js
function yieldToMain() {
  if (globalThis.scheduler?.yield) {
    return scheduler.yield();
  }
  return new Promise((resolve) => setTimeout(resolve, 0));
}

async function processItems(items) {
  let lastYield = performance.now();

  for (const item of items) {
    processItem(item);

    if (performance.now() - lastYield > 50) {
      await yieldToMain();
      lastYield = performance.now();
    }
  }
}
```

Yielding every ~50 ms keeps tasks short without adding too much overhead. Yielding after every single item can make the total work much slower.

## 40: How do you make an event handler respond faster?

Do the minimum work needed to show feedback, let the browser paint, and do the rest later.

```js
button.addEventListener("click", async () => {
  // 1. Visible feedback first
  button.disabled = true;
  status.textContent = "Saving...";

  // 2. Let the browser paint (yieldToMain from the previous question)
  await yieldToMain();

  // 3. Heavy or non-urgent work after
  saveDraft();
  sendAnalytics();
});
```

Other tips:

- Debounce handlers on `input` that do expensive work like filtering a big list.
- Don't run analytics or logging code synchronously in the handler.
- Move heavy calculations to a Web Worker.
- In React, use `startTransition` for updates that don't need to be instant.

## 41: What is layout thrashing and how does it hurt INP?

Layout thrashing (also called forced synchronous layout) happens when JavaScript writes to the DOM and then reads a layout property like `offsetHeight`, `getBoundingClientRect()` or `scrollTop`. The browser has to calculate layout right away to give a correct answer. Doing this in a loop makes the browser calculate layout many times in one task.

```js
// Bad: read and write mixed in a loop
for (const box of boxes) {
  box.style.width = container.offsetWidth / 2 + "px";
}

// Good: read once, then write
const half = container.offsetWidth / 2;
for (const box of boxes) {
  box.style.width = half + "px";
}
```

It makes event handlers slower, which increases the processing duration of INP. In the Performance panel, it shows up as purple "Layout" blocks inside JavaScript with a "Forced reflow" warning.

## 42: How do you prevent layout shifts from ads, embeds and dynamic content?

Reserve the space before the content arrives.

```css
.ad-slot {
  min-height: 250px;
}

.video-embed {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

- For ads with different possible sizes, reserve space for the most common size, or the smallest one if you have to choose.
- Don't remove an empty ad slot when no ad is returned. Show a placeholder instead.
- Use skeleton loaders that have the same size as the final content.
- Don't insert content above existing content unless it's a response to a user action. Put banners in an overlay or at the bottom instead.

## 43: How do animations affect CLS?

Animating properties like `top`, `left`, `width`, `height` or `margin` changes the layout, so each frame can count as a layout shift and other elements may move too. It's also slower because the browser has to recalculate layout every frame.

Animating `transform` and `opacity` doesn't change the layout, doesn't cause layout shifts, and can run on the compositor.

```css
/* Bad: causes layout shifts */
.toast.show {
  top: 20px;
  transition: top 0.3s;
}

/* Good: no layout shifts */
.toast {
  transform: translateY(-100%);
  transition: transform 0.3s;
}
.toast.show {
  transform: translateY(0);
}
```

## 44: How do you send Web Vitals data to your analytics?

Use the `web-vitals` library and send each metric when it's reported. Use `navigator.sendBeacon()` (or `fetch` with `keepalive: true`), because CLS and INP are often reported when the page is being hidden or closed, and normal requests might be cancelled.

```js
import { onCLS, onINP, onLCP } from "web-vitals";

function sendToAnalytics(metric) {
  const body = JSON.stringify({
    name: metric.name,
    value: metric.value,
    delta: metric.delta,
    rating: metric.rating,
    id: metric.id,
    navigationType: metric.navigationType,
    page: location.pathname,
  });

  if (!navigator.sendBeacon("/analytics", body)) {
    fetch("/analytics", { body, method: "POST", keepalive: true });
  }
}

onCLS(sendToAnalytics);
onINP(sendToAnalytics);
onLCP(sendToAnalytics);
```

Call each `onXXX()` function only once per page load.

## 45: What do value, delta, id and rating mean in the web-vitals metric object?

- **`value`**: the current value of the metric.
- **`delta`**: how much the value changed since the last time this metric was reported. On the first report, `delta` equals `value`.
- **`id`**: a unique id for this metric instance on this page load. If the page is restored from bfcache, new ids are created.
- **`rating`**: `"good"`, `"needs-improvement"` or `"poor"`, based on the official thresholds.

CLS and INP can be reported more than once on the same page. If your analytics tool can only sum values (like event values in some tools), send `delta` and group by `id`. If it can store the latest value, send `value` and keep the last one per `id`.

## 46: What is the attribution build of web-vitals?

It's a version of the library that adds an `attribution` object to each metric with debug information. It tells you _why_ a metric has its value, which is the hard part of fixing field data. It's about 1.5 KB bigger.

```js
import { onLCP, onINP, onCLS } from "web-vitals/attribution";

onLCP(({ value, attribution }) => {
  console.log("LCP", value, attribution.target, attribution.url);
  console.log("Load delay", attribution.resourceLoadDelay);
  console.log("Render delay", attribution.elementRenderDelay);
});

onINP(({ value, attribution }) => {
  console.log("INP", value, attribution.interactionTarget);
  console.log(
    attribution.inputDelay,
    attribution.processingDuration,
    attribution.presentationDelay,
  );
});

onCLS(({ value, attribution }) => {
  console.log("CLS", value, attribution.largestShiftTarget);
});
```

Sending `target` selectors with your metrics lets you see, for example, that most poor INP values come from one specific filter button.

## 47: How can you access CrUX data?

- **PageSpeed Insights**: quickest way to check one URL or origin.
- **CrUX API**: returns the latest 28-day data for a URL or origin as JSON. Needs an API key.
- **CrUX History API**: returns weekly data points for about the last six months, good for trends.
- **CrUX Vis**: a web tool to see trends over time for an origin or URL.
- **BigQuery**: the full public dataset, updated monthly, at origin level. Good for comparing with competitors or large analysis.
- **Search Console**: the Core Web Vitals report for your own site.

```bash
curl -s "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/", "formFactor": "PHONE"}'
```

If a URL doesn't have enough traffic, CrUX has no data for it, and you only get origin-level data.

## 48: Why are Lighthouse numbers different from field data?

Lighthouse runs one page load on one simulated device and network. Real users have all kinds of devices, networks, locations and cache states. There are many reasons the numbers don't match:

- Real users may have the page cached, or arrive from bfcache or prerender, so loads are faster.
- Real users may have slower phones than the Lighthouse profile.
- The LCP element can be different, for example because of cookie banners, personalization or a different viewport.
- Lighthouse measures CLS only during load, but field CLS covers the whole visit, including scrolling.
- Lighthouse doesn't log in, so it may test a different page than most users see.

Field data is the truth for what users experience. Use lab tools to reproduce and fix issues.

## 49: How do you use Lighthouse in CI to catch regressions?

Lighthouse CI (`@lhci/cli`) runs Lighthouse on every commit or pull request and can fail the build if scores or metrics are worse than allowed.

```js
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      url: ["http://localhost:3000/", "http://localhost:3000/product/1"],
      startServerCommand: "npm run start",
      numberOfRuns: 3,
    },
    assert: {
      assertions: {
        "largest-contentful-paint": ["error", { maxNumericValue: 2500 }],
        "cumulative-layout-shift": ["error", { maxNumericValue: 0.1 }],
        "total-blocking-time": ["warn", { maxNumericValue: 200 }],
      },
    },
  },
};
```

Run it several times per URL, because lab results vary between runs. CI tests help catch big mistakes before release, but you still need field data to see the real impact.

## 50: How do you improve TTFB?

- Use a CDN and cache HTML at the edge when possible, even for a short time.
- Avoid redirects, especially chains like `http` → `https` → `www`.
- Make the server faster: database queries, caching, less work before sending the response.
- Stream the HTML so the `<head>` is sent early, before the whole page is ready.
- Use **103 Early Hints** so the browser can start loading CSS and fonts while the server is still working.
- Use modern protocols (HTTP/2, HTTP/3) and keep TLS setup fast.
- If you have a service worker, make sure it doesn't slow down navigation requests.

## 51: What is the back/forward cache and how does it help Web Vitals?

The back/forward cache (bfcache) keeps a full snapshot of a page in memory when the user navigates away. If they press back or forward, the page is restored instantly instead of loading again. LCP is almost zero and there are no load-time layout shifts.

Things that can make a page not eligible:

- `unload` event listeners (use `pagehide` instead)
- `Cache-Control: no-store` on the HTML in many cases
- open connections like WebSockets or IndexedDB transactions when leaving the page
- `window.opener` references

You can check eligibility in DevTools under **Application → Back/forward cache**. The `web-vitals` library reports new metrics for bfcache restores with `navigationType: 'back-forward-cache'`.

## 52: How does client-side rendering affect LCP compared to server-side rendering?

With client-side rendering (CSR), the HTML is almost empty. The browser has to download the JavaScript, run it, often fetch data from an API, and only then render the content and discover the LCP image. Each step adds time, so LCP is often slow, especially on mobile.

With server-side rendering (SSR) or static generation, the HTML already contains the content and the `<img>` tag, so the browser can find and load the LCP image right away.

SSR can make TTFB a bit slower and INP worse during hydration if the bundle is large. Still, for content pages and landing pages, SSR or static HTML is usually much better for LCP.

## 53: How do third-party scripts affect Web Vitals?

Third-party scripts like analytics, tag managers, chat widgets, ads and A/B testing tools often:

- run long tasks on the main thread, which hurts INP
- block rendering if loaded synchronously in the `<head>`, which hurts LCP
- insert content into the page, which causes CLS

What you can do:

- Audit them regularly and remove the ones nobody uses.
- Load them with `async` or `defer`, or after the page load, or on user interaction (for example load the chat widget when the user clicks the chat button).
- Use a facade, like a static preview image instead of a full YouTube embed until the user clicks.
- Reserve space for anything they inject.

## 54: What is content-visibility and how can it help?

`content-visibility: auto` tells the browser it can skip rendering work (style, layout, paint) for an element while it's off-screen. For long pages, this can make the initial render and later updates much faster.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 800px;
}
```

`contain-intrinsic-size` gives the element an estimated size while it's skipped. Without it, the element has zero height, and the scrollbar jumps when it renders, which can cause layout shifts. The `auto` keyword makes the browser remember the real size after the element was rendered once.

## 55: How do image size and format affect LCP?

A big image takes longer to download, which increases the resource load duration part of LCP. Common problems are serving a 3000 px wide photo to a 400 px wide phone, or using PNG for photos.

- Use `srcset` and `sizes` so each device gets a fitting size.
- Use AVIF or WebP, with `<picture>` if you need a fallback.
- Compress images with a reasonable quality setting.
- Use an image CDN that resizes and converts images automatically.

```html
<picture>
  <source srcset="/hero.avif" type="image/avif" />
  <source srcset="/hero.webp" type="image/webp" />
  <img src="/hero.jpg" width="1200" height="600" fetchpriority="high" alt="" />
</picture>
```

## 56: How does the Core Web Vitals report in Search Console work?

It shows field data from CrUX for your site, split into mobile and desktop. URLs are grouped together when they have similar content and performance (for example all product pages), and the group gets the status of its data. For each group you can see if it's "Good", "Needs improvement" or "Poor" and which metric is the problem.

The data is based on the last 28 days. So after you fix something, it takes up to four weeks for the report to fully reflect it. You can click "Validate fix" to start tracking whether the issue is gone.

## 57: When does a page "pass" the Core Web Vitals assessment?

A page (or origin) passes when all three Core Web Vitals are "good" at the 75th percentile:

- LCP ≤ 2.5 s
- INP ≤ 200 ms
- CLS ≤ 0.1

If a page doesn't have enough INP data (for example users rarely interact), it can still pass based on LCP and CLS. If there isn't enough data at all for a URL, PageSpeed Insights shows origin-level data instead.

## 58: How can cookie banners and late-loading UI hurt CLS and LCP?

A cookie banner that is pushed in at the top of the page, after the content has rendered, moves everything down. That's a layout shift. If it's added as a fixed overlay at the bottom, it doesn't move other content and causes no CLS.

Banners can also hurt LCP. If the banner has a big block of text, it can become the LCP element. If it's loaded by a slow third-party script, LCP may be counted when the banner appears.

Best practice: render the banner with the page (not later), use `position: fixed`, and keep it reasonably small.

## 59: What is an infinite scroll and how do you keep it from causing CLS?

When the user scrolls near the bottom and new items load, adding them below the visible content is fine. Problems come from content that moves the user's current position: a footer that gets pushed down while the user is looking at it, ads inserted between existing items, or loaders that change height.

- Reserve space for the next batch with a fixed-height placeholder.
- Don't show a footer below an infinite list, or use a "Load more" button.
- Don't insert items above the current scroll position.

Shifts that happen within 500 ms after a click on "Load more" don't count, because they follow user input.

## 60: How do you find the cause of a poor INP using Chrome DevTools?

1. Check field data first (CrUX or your RUM) to know which page and, if you have attribution data, which element is slow.
2. Open the **Performance** panel and turn on CPU throttling (for example 4x or 6x slowdown) to simulate a mobile device.
3. Interact with the element. The live metrics view shows the INP and the slowest interaction.
4. Record a trace while doing the interaction. In the **Interactions** track you see the interaction split into input delay, processing duration and presentation delay.
5. Look at the main thread at that time. Find long JavaScript tasks, forced layouts, or big style and layout work after the handler.
6. Fix, then measure again with the same steps.

# Advanced Questions (61-90)

## 61: How is the CLS score calculated?

Each single layout shift gets a score:

```
layout shift score = impact fraction × distance fraction
```

- **Impact fraction**: how much of the viewport is affected. It's the area covered by the unstable elements before and after the shift, combined, divided by the viewport area.
- **Distance fraction**: the largest distance any unstable element moved, divided by the viewport's largest dimension (width or height).

Example: an element covers 50% of the viewport and moves down by 25% of the viewport height. The impact area (before plus after) is 75% of the viewport, so the impact fraction is 0.75. The distance fraction is 0.25. The score is 0.75 × 0.25 = 0.1875.

Shift scores are then grouped into **session windows**, and CLS is the sum of the worst window (see the next question).

## 62: What are session windows in CLS and why were they added?

A session window is a group of layout shifts that happen close to each other. A new window starts when there's a gap of more than 1 second without shifts, and a window can be at most 5 seconds long. CLS is the total score of the window with the highest sum, not the sum of all shifts during the visit.

Before this change (in 2021), CLS added up every shift for the whole life of the page. Pages that users kept open for a long time, like SPAs or infinite feeds, got worse scores just because they were open longer. Session windows make the score reflect the worst burst of instability, so long-lived pages are judged more fairly.

## 63: How exactly is INP calculated?

1. The browser gets Event Timing entries for each event. Events that belong to the same user interaction (for example `pointerdown`, `pointerup` and `click` for one tap) share the same `interactionId`.
2. The duration of an interaction is the longest duration among its events. It goes from the input time to the next paint, and it's rounded to 8 ms.
3. INP is the longest interaction duration, with one exception: for every 50 interactions, the single worst one is ignored. This filters out random spikes on very interactive pages.

So on a page with fewer than 50 interactions, INP is the worst interaction. With 120 interactions, the two worst are ignored and INP is the third worst. The `web-vitals` library keeps the 10 longest interactions in memory to calculate this without storing everything.

## 64: When does the browser stop looking for a new LCP candidate?

The browser emits a new `largest-contentful-paint` entry every time a bigger element is painted. It stops reporting new candidates when:

- the user interacts with the page (click, tap, key press or scroll), because after that, new content is likely a result of the interaction
- the page is hidden (for example the user switches tabs)

Also note:

- If the page loads in a background tab, LCP isn't reported at all by `web-vitals`, because the timing would be meaningless.
- An element that was the LCP candidate and was later removed from the DOM still counts. So a big image in a carousel that rotates out can still be the LCP.
- Images that are added later but are bigger can become the LCP even after several seconds, if the user hasn't interacted yet.

## 65: How do you measure LCP and CLS yourself with PerformanceObserver?

```js
// LCP candidates
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const last = entries[entries.length - 1];
  console.log("LCP candidate", last.startTime, last.element);
}).observe({ type: "largest-contentful-paint", buffered: true });

// Layout shifts
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      console.log("Layout shift", entry.value, entry.sources);
    }
  }
}).observe({ type: "layout-shift", buffered: true });
```

`buffered: true` gives you entries that happened before the observer was created. This is fine for debugging, but in production you should use `web-vitals`. It handles many edge cases: session windows for CLS, pages loaded in the background, prerendered pages, bfcache restores, `activationStart`, reporting on `visibilitychange` and more. Writing all this yourself is easy to get wrong.

## 66: What is the Event Timing API and what is durationThreshold?

The Event Timing API reports `event` performance entries with details about each event: `startTime` (input time), `processingStart`, `processingEnd`, `duration` and `interactionId`. INP is built on top of it.

By default, the browser only reports events with a duration of at least 104 ms, to save memory. You can lower this with `durationThreshold`, down to a minimum of 16 ms.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.interactionId) continue;

    const inputDelay = entry.processingStart - entry.startTime;
    const processing = entry.processingEnd - entry.processingStart;
    console.log(entry.name, entry.duration, { inputDelay, processing });
  }
}).observe({ type: "event", durationThreshold: 16, buffered: true });
```

The `web-vitals` library uses a threshold of 40 ms by default. You can change it with the `durationThreshold` option of `onINP()`. A lower threshold gives more accurate INP on pages where all interactions are fast, at the cost of more entries.

## 67: What is the Long Animation Frames API and how does it help with INP?

The Long Animation Frames API (LoAF) reports animation frames that took more than 50 ms to render. It replaced the older Long Tasks API for this kind of debugging. LoAF is more useful because it measures the whole frame, including rendering work, and it tells you which **scripts** ran during the frame: the source URL, the function name, and how long each one took.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    for (const script of entry.scripts) {
      console.log(script.sourceURL, script.sourceFunctionName, script.duration);
    }
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

In the field, this is how you find out that a slow interaction was caused by a specific third-party script. The `web-vitals` attribution build already links LoAF entries to the INP interaction and gives `longestScript`, `totalScriptDuration` and `totalStyleAndLayoutDuration`. LoAF is currently available in Chromium only.

## 68: How are Web Vitals measured in single-page apps with soft navigations?

In an SPA, moving to a new "page" usually just changes the URL with the History API and re-renders, without a real browser navigation. This is a soft navigation. Originally, Core Web Vitals were only tracked for hard (real) navigations, so in an SPA:

- LCP was only measured for the first page
- CLS and INP were collected across all the routes together and blamed on the first URL

Chrome added soft navigation measurement in Chromium 151. A soft navigation is detected when a user interaction leads to a URL change and new content is painted. After that, FCP, LCP, CLS and INP start again for the new route. TTFB is reported as 0.

The `web-vitals` library supports this with the `reportSoftNavs` option:

```js
import { onCLS, onINP, onLCP } from "web-vitals";

const opts = { reportSoftNavs: true };

onLCP(sendToAnalytics, opts);
onCLS(sendToAnalytics, opts);
onINP(sendToAnalytics, opts);

function sendToAnalytics(metric) {
  // metric.navigationURL is the route the metric belongs to
  // metric.navigationType is 'soft-navigation' for soft navs
}
```

Other browsers don't support it yet, so the same app will report differently there. When comparing your RUM data with CrUX, check whether your CrUX source includes soft navigation data before you rely on it.

## 69: How do prerendering and the Speculation Rules API affect Web Vitals?

With the Speculation Rules API, you can tell the browser to prerender a page the user is likely to open next. If they do open it, the page is shown almost instantly, with LCP close to zero.

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

For measurement, the important detail is `activationStart` on the navigation entry. It's the time the user actually navigated to the prerendered page. Metrics should be measured from that moment, not from when prerendering started in the background. `web-vitals` does this for you and sets `navigationType` to `'prerender'`.

Things to watch out for: analytics or ads that fire during prerender (use `document.prerendering` and the `prerenderingchange` event to wait), and extra server load from pages that are prerendered but never visited.

## 70: How do iframes affect Web Vitals?

- **CLS**: layout shifts inside iframes are included in the CrUX CLS of the top page. But JavaScript on the main page can't see shifts inside cross-origin iframes, so your own RUM data can show lower CLS than CrUX. Shifts of the iframe element itself on the parent page are counted normally.
- **LCP**: content inside cross-origin iframes is not visible to the parent page's `PerformanceObserver`. Chrome includes iframe content in LCP in some cases, which again can make CrUX and RUM data differ.
- **INP**: interactions inside an iframe are measured by the iframe document, not the parent. Embedded widgets like video players or maps can have their own bad INP that doesn't show in your RUM.

If you control the iframe content, you can run `web-vitals` inside it and send the data with `postMessage` to the parent.

## 71: How does a page restored from bfcache report metrics?

When a page is restored from bfcache, the `pageshow` event fires with `event.persisted === true`. No new navigation happens, so there's no new navigation entry.

`web-vitals` treats a restore as a new page visit. It creates new metric instances with new ids and `navigationType: 'back-forward-cache'`. LCP and FCP are measured as the time from the restore until the next frames are painted, using `requestAnimationFrame`. CLS and INP start from zero again.

```js
window.addEventListener("pageshow", (event) => {
  if (event.persisted) {
    console.log("Restored from bfcache");
  }
});
```

This is why it's useful to break down your RUM data by `navigationType`. A page with lots of bfcache restores will have much better field numbers than its normal load would suggest.

## 72: Why can your RUM data differ from CrUX?

- **Browsers**: CrUX only includes Chrome. Your RUM may include Safari and Firefox, which handle metrics a bit differently and don't report CLS.
- **Users**: CrUX only includes Chrome users who opted in to sharing usage statistics.
- **Sampling**: your RUM may sample only some sessions, or lose beacons when users close the tab.
- **Time range**: CrUX is a rolling 28-day window. Your dashboard may show the last day or week.
- **Iframes**: CrUX can include data from cross-origin iframes that your JavaScript can't see.
- **Page types**: CrUX groups data by URL or origin, and URLs without enough traffic are not included separately.
- **Library**: an old version of `web-vitals` or a custom implementation may calculate metrics differently.

Don't expect the numbers to match exactly. They should show the same trends.

## 73: How does hydration affect INP?

In SSR frameworks, the user sees the HTML before the JavaScript has attached event handlers. Hydration runs as one or more long tasks. If the user clicks during hydration, the input has to wait, which gives a long input delay. And if the handler isn't attached yet, the click may do nothing at all.

Ways to reduce this:

- Ship less JavaScript to the client. Use React Server Components, islands (like Astro) or partial hydration so static parts don't need JavaScript.
- Use frameworks that hydrate in chunks and prioritize the part the user interacts with. React 18+ does selective hydration with `Suspense` boundaries.
- Lazy-load components below the fold.
- Look at the `loadState` in INP attribution. If many slow interactions happen in `dom-interactive` or `dom-content-loaded`, hydration is likely the cause.

## 74: How can the Server-Timing header help with Web Vitals?

The `Server-Timing` HTTP header lets the server send its own timing data to the browser. You can see it in the DevTools Network panel, and read it in JavaScript from the navigation entry.

```
Server-Timing: db;dur=53, cache;desc="miss", render;dur=120
```

```js
const [nav] = performance.getEntriesByType("navigation");
for (const timing of nav.serverTiming) {
  console.log(timing.name, timing.duration, timing.description);
}
```

If you send this with your Web Vitals data, you can connect a slow TTFB or LCP in the field with what happened on the server, like a cache miss or a slow database query. The `web-vitals` attribution build exposes the navigation entry in `attribution.navigationEntry`.

## 75: What are 103 Early Hints and how can they help LCP?

103 Early Hints is an HTTP status code the server (or CDN) sends before the final response. It contains `Link` headers telling the browser what to preconnect to or preload. The browser can start doing that while the server is still generating the HTML.

```
HTTP/1.1 103 Early Hints
Link: </styles/main.css>; rel=preload; as=style
Link: <https://cdn.example.com>; rel=preconnect

HTTP/1.1 200 OK
Content-Type: text/html
...
```

It helps most when the server has a slow TTFB, because that "think time" is used to download critical resources. It doesn't help much if the HTML is already cached at the edge and sent quickly. Preloading too much in Early Hints can also take bandwidth away from the HTML itself.

## 76: The LCP image downloads quickly, but LCP is still slow. What could cause it?

This is a long **element render delay**. The image is in the browser, but it isn't painted yet. Common reasons:

- Render-blocking CSS or synchronous scripts in the `<head>` are still loading.
- The image is rendered by JavaScript (CSR or a slider library), which hasn't run yet.
- A long task is blocking the main thread, so the browser can't paint.
- An A/B testing tool hides the page (anti-flicker snippet) until its script finishes.
- The element is hidden with `opacity: 0` and fades in with an animation, so LCP is only counted when it's visible.
- The LCP is text that waits for a web font with `font-display: block`.

Use the `elementRenderDelay` from the `web-vitals` attribution build in the field, and the LCP breakdown in the DevTools Performance panel in the lab, to confirm.

## 77: How do client-side A/B testing tools affect Web Vitals?

Most client-side A/B testing tools load a script that changes the page after it's loaded. To avoid users seeing the original version first (flicker), they often add an anti-flicker snippet that hides the whole page with `opacity: 0` until the script is done.

- **LCP**: nothing is painted until the script loads and runs, which can add hundreds of milliseconds or even seconds.
- **CLS**: if the experiment changes the layout after the page is shown, it causes layout shifts.
- **INP**: the script often runs long tasks during load.

Better options: run experiments on the server or at the edge (CDN workers), so the HTML is already the right version. If you have to use client-side testing, limit the anti-flicker timeout, only hide the specific element being tested, and load the script as early as possible.

## 78: What is the difference between scheduler.yield() and setTimeout(0) for yielding?

Both give the main thread back to the browser so it can handle input and paint. The difference is what happens next:

- **`setTimeout(fn, 0)`** puts the rest of your work at the end of the task queue. Any other tasks that were queued, like third-party scripts, can run before your work continues. Browsers also clamp nested timeouts to at least 4 ms after several levels.
- **`scheduler.yield()`** returns a promise, and the rest of your work is scheduled with higher priority than other tasks of the same priority. So your work continues sooner, but the browser can still handle input and render in between.

```js
async function handleClick() {
  updateButtonState();
  await scheduler.yield(); // paint can happen here
  runHeavyFilter(); // continues before most other queued tasks
}
```

`scheduler.yield()` is available in Chromium and Firefox. Use a `setTimeout` fallback for other browsers (see question 39). There's also `scheduler.postTask()` for scheduling work with `user-blocking`, `user-visible` or `background` priority.

## 79: How does DOM size affect INP and how do you handle very large DOMs?

The larger the DOM, the more work the browser has to do on style recalculation and layout after every update. An interaction that changes a class on `<body>` may force style recalculation for thousands of elements. This shows up as a long presentation delay.

Ways to handle it:

- **Virtualize long lists** so only visible rows exist in the DOM (for example with TanStack Virtual or react-window).
- Use `content-visibility: auto` for large off-screen sections.
- Use CSS containment (`contain: layout paint` or `contain: content`) on independent widgets so changes inside don't affect the rest of the page.
- Keep CSS selectors simple and avoid toggling classes high in the tree when only a small part needs to change.
- Remove hidden content that's never shown, like big menus duplicated for mobile and desktop.

## 80: How do you reduce presentation delay in INP?

Presentation delay is the time between the end of the event handlers and the next paint. It's mostly rendering work.

- Make the DOM update smaller. Update only what changed, not the whole component tree.
- Avoid big synchronous re-renders. In React, use `startTransition` or `useDeferredValue` for non-urgent updates, so the urgent part (like the input value) renders first.
- Don't do heavy work in `requestAnimationFrame` callbacks, `ResizeObserver` or `IntersectionObserver` callbacks triggered by the interaction. They run before the paint.
- Reduce layout cost with containment and a smaller DOM.
- Avoid rendering a large amount of HTML with `innerHTML` in the handler.

```jsx
const [query, setQuery] = useState("");
const deferredQuery = useDeferredValue(query);

return (
  <>
    <input value={query} onChange={(e) => setQuery(e.target.value)} />
    <ResultsList query={deferredQuery} />
  </>
);
```

## 81: How would you design a RUM pipeline for Web Vitals at scale?

1. **Collection**: use the `web-vitals` attribution build. Send `name`, `value`, `delta`, `id`, `rating`, `navigationType` and a few attribution fields (target, LCP subparts, INP phases, `loadState`).
2. **Context**: add page template or route (not the full URL with ids), device type, effective connection type, country, app version and whether the user is logged in. Don't send personal data.
3. **Sending**: batch metrics and send them on `visibilitychange` to hidden using `sendBeacon`. This also catches the final CLS and INP values.
4. **Sampling**: on high-traffic sites, sample a percentage of sessions, but sample by session, not per metric, so you get full data for each sampled visit.
5. **Storage**: store raw events in a columnar store (BigQuery, ClickHouse and similar). Dedupe by `id` and keep the last value.
6. **Analysis**: show p75 per page template and device, plus distributions. Alert on p75 changes after deploys.
7. **Debugging**: group poor values by attribution target to find the top offenders.

## 82: Why shouldn't you average Web Vitals values?

Performance data is skewed. Most values are close together, and there's a long tail of very slow values. An average gets pulled by extreme outliers, so one 60-second LCP from a broken connection can move it a lot. It also doesn't tell you how many users had a bad experience.

Use percentiles. p75 matches what Google uses. p50 shows the typical user, and p95 or p99 shows the tail. Histograms or the share of good / needs improvement / poor are also very useful, because a change from "70% good" to "80% good" is easy to understand.

Also be careful when combining percentiles. The p75 of several pages can't be calculated by averaging each page's p75. You need to compute it from the raw data.

## 83: How do you prevent Web Vitals regressions in a team?

- **Performance budgets**: limits for bundle size, number of requests, image weight, and lab metrics like LCP and TBT. Check them in CI with Lighthouse CI or bundle size tools, and fail the build if they're broken.
- **Field monitoring with alerts**: watch p75 per page template after each deploy. Lab tests don't catch everything, especially INP.
- **Code review rules**: no `loading="lazy"` on hero images, always set image dimensions, new third-party scripts need approval.
- **Ownership**: each important page has an owner who looks at its metrics.
- **Release tags**: send the app version with RUM data so you can link a regression to a deploy.
- **Feature flags**: so you can turn off a change that made things worse without a full rollback.

## 84: Scenario: LCP is good in Lighthouse but poor in field data. How do you investigate?

1. **Check which pages and devices.** Look at CrUX or RUM by page template and device. Often only mobile is bad, or only some page types.
2. **Find the real LCP element.** Use RUM attribution `target`. In the field, it's often something Lighthouse doesn't see: a cookie banner, a personalized block, a different image for logged-in users, or a different element on small screens.
3. **Look at the LCP subparts in the field.** A high TTFB may come from users far from your servers or cache misses. A large load delay means the image is discovered late.
4. **Check geography and network.** Lighthouse runs from one location with a fixed throttling profile. Real users in other countries may have higher latency.
5. **Check navigation types.** Compare normal loads, reloads, bfcache and prerender.
6. **Reproduce** in the lab with the same conditions: slower CPU, the right viewport, a logged-in session, the cookie banner shown.
7. **Fix and wait** for the 28-day CrUX window to update, but watch your RUM for faster feedback.

## 85: Scenario: INP is poor on mobile on a product listing page with filters. How do you approach it?

1. Use RUM attribution to confirm the slow interaction. Say most poor INP values have `interactionTarget` on the filter checkboxes.
2. Check the phases. If **processing duration** is high, the filter handler is doing too much: filtering thousands of items, re-rendering the whole list, or sending analytics synchronously.
3. If **presentation delay** is high, the DOM update is too big. Rendering 500 product cards at once is a common cause.
4. If **input delay** is high, something else is blocking the main thread: hydration, third-party scripts, or a timer.

Possible fixes:

- Update the checkbox state immediately, then yield and apply the filter.
- Use `startTransition` (React) so the list update is not urgent.
- Virtualize or paginate the product list.
- Move filtering to the server, or to a Web Worker for big data sets.
- Debounce if the filter also triggers on text input.

Test the result with CPU throttling in DevTools and then confirm in field data.

## 86: Scenario: CLS jumped after a release. How do you find the cause?

1. Look at RUM data by app version to confirm the release caused it, and by page template to see where.
2. Check the attribution `largestShiftTarget`, `largestShiftTime` and `loadState`. They tell you which element moved and whether it was during load or later.
3. Reproduce it in DevTools. Record a Performance trace and look at the **Layout shifts** track. Each shift shows the elements that moved. You can also use the Rendering tab option "Layout shift regions" to highlight shifts on screen.
4. Check the diff of the release for typical causes: new images without dimensions, a new banner at the top, a changed font, a component that renders a loading state with a different height, or CSS that changed from `transform` to `top`.
5. If the shift happens only for some users, check A/B tests and personalization.
6. Fix it by reserving space, then compare the metric again for the next version.

## 87: Scenario: TTFB is poor for users in some countries. What do you do?

1. Split TTFB by country in RUM and see if it's network latency (far from the origin), server time, or redirects. `Server-Timing` and the navigation timing breakdown (DNS, connect, request) help here.
2. If users are far from the origin, put a CDN in front and cache HTML at the edge, even for a short time with `stale-while-revalidate`.
3. For personalized pages that can't be fully cached, cache the shared shell and fetch personal parts separately, or render at the edge.
4. Check for redirects (`/` → `/en/` → `/en/home`) that add a full round trip each, which is very expensive on high-latency connections.
5. Use 103 Early Hints so the browser can start loading CSS and fonts during the server wait.
6. Make sure HTTP/3 and TLS 1.3 are enabled to reduce connection setup time.

## 88: When does moving work to a Web Worker help INP, and what are its limits?

A Web Worker runs JavaScript on a separate thread, so long calculations don't block the main thread. It helps when the slow part of an interaction is pure computation: filtering or sorting large data sets, parsing big JSON, search indexing, image processing or encryption.

```js
// main.js
const worker = new Worker(new URL("./filter-worker.js", import.meta.url), {
  type: "module",
});

worker.onmessage = (event) => renderResults(event.data);

input.addEventListener("input", () => {
  worker.postMessage({ query: input.value });
});
```

Limits:

- Workers can't access the DOM, so rendering still happens on the main thread. If the slow part is rendering, a worker won't help.
- Sending data with `postMessage` copies it (structured clone). Sending very large objects back and forth can be slow itself. Transferable objects like `ArrayBuffer` avoid the copy.
- It adds complexity: async communication, separate bundles, error handling.

## 89: How do you measure the performance of a specific element or user flow beyond Core Web Vitals?

Core Web Vitals are generic. For your own important moments, use custom metrics:

- **User Timing API** (`performance.mark()` and `performance.measure()`) to measure your own steps, like "search results shown" or "checkout form ready".
- **Element Timing API** to know when a specific image or text element was painted. Add the `elementtiming` attribute. It's Chromium only.

```html
<img src="/product.jpg" elementtiming="product-image" alt="" />
```

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(entry.identifier, entry.renderTime || entry.loadTime);
  }
}).observe({ type: "element", buffered: true });

performance.mark("search-start");
await runSearch();
performance.mark("search-end");
performance.measure("search", "search-start", "search-end");
```

User Timing marks also appear in the DevTools Performance panel, which makes traces easier to read.

## 90: How do Core Web Vitals change over time, and how do you keep up?

Google changes the metrics when they find problems with them. Examples are CLS moving to session windows in 2021, INP replacing FID in 2024, and smaller fixes to how LCP picks elements (like ignoring low-detail placeholder images). New metrics usually go through an "experimental" or "pending" stage first, and Google announces them long before they become Core Web Vitals.

Each change can move your numbers without any change on your site. To keep up:

- Follow the Chrome speed metrics changelog and web.dev blog.
- Keep the `web-vitals` library updated, and read its changelog for breaking changes (for example `onFID()` was removed in v5).
- Add the library version to your RUM data, so you can tell if a change in numbers came from your code or from a change in how metrics are measured.
- Note browser changes too. When Safari added LCP and INP, RUM data for those metrics suddenly included many more users.
