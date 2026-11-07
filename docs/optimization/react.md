# React Optimization Interview Questions and Answers

_Last updated: October 28, 2026_

450 questions about making React apps fast, split into three levels: 150 easy, 150 moderate and 150 advanced. Each level covers the same ten areas, from how rendering works to profiling, server rendering and bundle size.

The answers target React 19.2 and React Compiler 1.0. Older patterns like class components, `PureComponent` and `shouldComponentUpdate` are mentioned where you will still see them in real code, and they are marked as legacy.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
  - [Rendering and Re-renders (1-15)](#easy-rendering-and-re-renders-1-15)
  - [Memoization and the React Compiler (16-30)](#easy-memoization-and-the-react-compiler-16-30)
  - [State and Context (31-45)](#easy-state-and-context-31-45)
  - [Lists and Large Data (46-60)](#easy-lists-and-large-data-46-60)
  - [Effects and Data Fetching (61-75)](#easy-effects-and-data-fetching-61-75)
  - [Concurrent Features and Suspense (76-90)](#easy-concurrent-features-and-suspense-76-90)
  - [Code Splitting and Bundle Size (91-105)](#easy-code-splitting-and-bundle-size-91-105)
  - [Server Rendering and Hydration (106-120)](#easy-server-rendering-and-hydration-106-120)
  - [Profiling and Measuring (121-135)](#easy-profiling-and-measuring-121-135)
  - [Assets, Forms and Everyday Patterns (136-150)](#easy-assets-forms-and-everyday-patterns-136-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
  - [Rendering and Re-renders (151-165)](#moderate-rendering-and-re-renders-151-165)
  - [Memoization and the React Compiler (166-180)](#moderate-memoization-and-the-react-compiler-166-180)
  - [State and Context (181-195)](#moderate-state-and-context-181-195)
  - [Lists and Large Data (196-210)](#moderate-lists-and-large-data-196-210)
  - [Effects and Data Fetching (211-225)](#moderate-effects-and-data-fetching-211-225)
  - [Concurrent Features and Suspense (226-240)](#moderate-concurrent-features-and-suspense-226-240)
  - [Code Splitting and Bundle Size (241-255)](#moderate-code-splitting-and-bundle-size-241-255)
  - [Server Rendering and Hydration (256-270)](#moderate-server-rendering-and-hydration-256-270)
  - [Profiling and Measuring (271-285)](#moderate-profiling-and-measuring-271-285)
  - [Assets, Forms and Everyday Patterns (286-300)](#moderate-assets-forms-and-everyday-patterns-286-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)
  - [Rendering and Re-renders (301-315)](#advanced-rendering-and-re-renders-301-315)
  - [Memoization and the React Compiler (316-330)](#advanced-memoization-and-the-react-compiler-316-330)
  - [State and Context (331-345)](#advanced-state-and-context-331-345)
  - [Lists and Large Data (346-360)](#advanced-lists-and-large-data-346-360)
  - [Effects and Data Fetching (361-375)](#advanced-effects-and-data-fetching-361-375)
  - [Concurrent Features and Suspense (376-390)](#advanced-concurrent-features-and-suspense-376-390)
  - [Code Splitting and Bundle Size (391-405)](#advanced-code-splitting-and-bundle-size-391-405)
  - [Server Rendering and Hydration (406-420)](#advanced-server-rendering-and-hydration-406-420)
  - [Profiling and Measuring (421-435)](#advanced-profiling-and-measuring-421-435)
  - [Assets, Forms and Everyday Patterns (436-450)](#advanced-assets-forms-and-everyday-patterns-436-450)

### Easy Questions (1-150)

- [1: What does "rendering" mean in React?](#1-what-does-rendering-mean-in-react)
- [2: What are the render phase and the commit phase?](#2-what-are-the-render-phase-and-the-commit-phase)
- [3: What causes a component to re-render?](#3-what-causes-a-component-to-re-render)
- [4: Does a child re-render when its parent re-renders, even if its props didn't change?](#4-does-a-child-re-render-when-its-parent-re-renders-even-if-its-props-didnt-change)
- [5: Is a re-render always a performance problem?](#5-is-a-re-render-always-a-performance-problem)
- [6: What is the virtual DOM?](#6-what-is-the-virtual-dom)
- [7: What is reconciliation?](#7-what-is-reconciliation)
- [8: Why should you not define a component inside another component?](#8-why-should-you-not-define-a-component-inside-another-component)
- [9: What is automatic batching?](#9-what-is-automatic-batching)
- [10: What happens if you set state to the same value it already has?](#10-what-happens-if-you-set-state-to-the-same-value-it-already-has)
- [11: Why should component functions be pure?](#11-why-should-component-functions-be-pure)
- [12: Why does StrictMode render components twice?](#12-why-does-strictmode-render-components-twice)
- [13: What is the difference between a development build and a production build of React?](#13-what-is-the-difference-between-a-development-build-and-a-production-build-of-react)
- [14: How does the `key` prop affect rendering?](#14-how-does-the-key-prop-affect-rendering)
- [15: What is the cheapest way to avoid a re-render?](#15-what-is-the-cheapest-way-to-avoid-a-re-render)
- [16: What is memoization?](#16-what-is-memoization)
- [17: What does `memo` do?](#17-what-does-memo-do)
- [18: What does `useMemo` do?](#18-what-does-usememo-do)
- [19: What does `useCallback` do?](#19-what-does-usecallback-do)
- [20: What is the difference between `useMemo` and `useCallback`?](#20-what-is-the-difference-between-usememo-and-usecallback)
- [21: Should you wrap every component in `memo` and every function in `useCallback`?](#21-should-you-wrap-every-component-in-memo-and-every-function-in-usecallback)
- [22: What is the React Compiler?](#22-what-is-the-react-compiler)
- [23: How do you enable the React Compiler?](#23-how-do-you-enable-the-react-compiler)
- [24: Do you still need `memo`, `useMemo` and `useCallback` if you use the React Compiler?](#24-do-you-still-need-memo-usememo-and-usecallback-if-you-use-the-react-compiler)
- [25: What are the Rules of React and why do they matter for performance?](#25-what-are-the-rules-of-react-and-why-do-they-matter-for-performance)
- [26: What does `"use no memo"` do?](#26-what-does-use-no-memo-do)
- [27: What is `PureComponent`?](#27-what-is-purecomponent)
- [28: What is `shouldComponentUpdate`?](#28-what-is-shouldcomponentupdate)
- [29: Why does passing an inline object as a prop break `memo`?](#29-why-does-passing-an-inline-object-as-a-prop-break-memo)
- [30: What does the ESLint plugin for React hooks check?](#30-what-does-the-eslint-plugin-for-react-hooks-check)
- [31: Why does where you put state matter for performance?](#31-why-does-where-you-put-state-matter-for-performance)
- [32: What is derived state and why should you avoid storing it?](#32-what-is-derived-state-and-why-should-you-avoid-storing-it)
- [33: What is lazy initial state?](#33-what-is-lazy-initial-state)
- [34: What is the difference between `useState` and `useRef` for storing values?](#34-what-is-the-difference-between-usestate-and-useref-for-storing-values)
- [35: Why do functional updates help with performance?](#35-why-do-functional-updates-help-with-performance)
- [36: What is Context and how does it cause re-renders?](#36-what-is-context-and-how-does-it-cause-re-renders)
- [37: Why should you not pass a new object to a Context provider on every render?](#37-why-should-you-not-pass-a-new-object-to-a-context-provider-on-every-render)
- [38: How does splitting a context help?](#38-how-does-splitting-a-context-help)
- [39: When is Context a bad choice for state?](#39-when-is-context-a-bad-choice-for-state)
- [40: What is a selector in a state library?](#40-what-is-a-selector-in-a-state-library)
- [41: What is `useReducer` and does it help with performance?](#41-what-is-usereducer-and-does-it-help-with-performance)
- [42: Is the setter function from `useState` stable?](#42-is-the-setter-function-from-usestate-stable)
- [43: What is prop drilling, and is it a performance problem?](#43-what-is-prop-drilling-and-is-it-a-performance-problem)
- [44: Why should you not mutate state directly?](#44-why-should-you-not-mutate-state-directly)
- [45: What does it mean to keep state minimal?](#45-what-does-it-mean-to-keep-state-minimal)
- [46: Why do list items need keys?](#46-why-do-list-items-need-keys)
- [47: Why is using the array index as a key a problem?](#47-why-is-using-the-array-index-as-a-key-a-problem)
- [48: Why should you not use `Math.random()` or `crypto.randomUUID()` as a key during render?](#48-why-should-you-not-use-mathrandom-or-cryptorandomuuid-as-a-key-during-render)
- [49: What is list virtualization?](#49-what-is-list-virtualization)
- [50: Which libraries can you use for virtualization in React?](#50-which-libraries-can-you-use-for-virtualization-in-react)
- [51: How many items is "too many" to render without virtualization?](#51-how-many-items-is-too-many-to-render-without-virtualization)
- [52: What is pagination and how is it different from virtualization?](#52-what-is-pagination-and-how-is-it-different-from-virtualization)
- [53: What is infinite scroll?](#53-what-is-infinite-scroll)
- [54: Why should you avoid filtering or sorting a big list on every render?](#54-why-should-you-avoid-filtering-or-sorting-a-big-list-on-every-render)
- [55: How can you make each row of a list cheaper to render?](#55-how-can-you-make-each-row-of-a-list-cheaper-to-render)
- [56: Why does updating one item in a list sometimes re-render all items?](#56-why-does-updating-one-item-in-a-list-sometimes-re-render-all-items)
- [57: What is the CSS property `content-visibility` and how does it help long lists?](#57-what-is-the-css-property-content-visibility-and-how-does-it-help-long-lists)
- [58: Why should you normalize large data sets?](#58-why-should-you-normalize-large-data-sets)
- [59: What is the problem with rendering large tables?](#59-what-is-the-problem-with-rendering-large-tables)
- [60: Why can rendering a long list in one go freeze the page?](#60-why-can-rendering-a-long-list-in-one-go-freeze-the-page)
- [61: When does `useEffect` run?](#61-when-does-useeffect-run)
- [62: What is the difference between `useEffect` and `useLayoutEffect`?](#62-what-is-the-difference-between-useeffect-and-uselayouteffect)
- [63: Why can effects cause extra renders?](#63-why-can-effects-cause-extra-renders)
- [64: What does "You Might Not Need an Effect" mean?](#64-what-does-you-might-not-need-an-effect-mean)
- [65: What happens if you forget the dependency array in `useEffect`?](#65-what-happens-if-you-forget-the-dependency-array-in-useeffect)
- [66: Why does an object in the dependency array make an effect run on every render?](#66-why-does-an-object-in-the-dependency-array-make-an-effect-run-on-every-render)
- [67: Why do you need a cleanup function in effects?](#67-why-do-you-need-a-cleanup-function-in-effects)
- [68: How do you cancel a fetch request in an effect?](#68-how-do-you-cancel-a-fetch-request-in-an-effect)
- [69: Why is fetching data in `useEffect` often not the best option?](#69-why-is-fetching-data-in-useeffect-often-not-the-best-option)
- [70: What is a request waterfall?](#70-what-is-a-request-waterfall)
- [71: What does a data fetching library like TanStack Query give you?](#71-what-does-a-data-fetching-library-like-tanstack-query-give-you)
- [72: What is a race condition in data fetching?](#72-what-is-a-race-condition-in-data-fetching)
- [73: What is debouncing and when do you use it in React?](#73-what-is-debouncing-and-when-do-you-use-it-in-react)
- [74: What is throttling?](#74-what-is-throttling)
- [75: What is the `use` hook?](#75-what-is-the-use-hook)
- [76: What is concurrent rendering?](#76-what-is-concurrent-rendering)
- [77: What is a transition?](#77-what-is-a-transition)
- [78: What does `useTransition` return?](#78-what-does-usetransition-return)
- [79: What is `useDeferredValue`?](#79-what-is-usedeferredvalue)
- [80: What is the difference between `useTransition` and `useDeferredValue`?](#80-what-is-the-difference-between-usetransition-and-usedeferredvalue)
- [81: Can you use a transition for a controlled input?](#81-can-you-use-a-transition-for-a-controlled-input)
- [82: What is `<Suspense>`?](#82-what-is-suspense)
- [83: Where should you put Suspense boundaries?](#83-where-should-you-put-suspense-boundaries)
- [84: What is a skeleton screen?](#84-what-is-a-skeleton-screen)
- [85: How does a transition change what Suspense shows?](#85-how-does-a-transition-change-what-suspense-shows)
- [86: What is `startTransition` without the hook used for?](#86-what-is-starttransition-without-the-hook-used-for)
- [87: What is the `<Activity>` component?](#87-what-is-the-activity-component)
- [88: What is the difference between hiding a component with `<Activity>` and with conditional rendering?](#88-what-is-the-difference-between-hiding-a-component-with-activity-and-with-conditional-rendering)
- [89: What is `useOptimistic`?](#89-what-is-useoptimistic)
- [90: What is a long task and why does it matter for React?](#90-what-is-a-long-task-and-why-does-it-matter-for-react)
- [91: Why does bundle size matter for React apps?](#91-why-does-bundle-size-matter-for-react-apps)
- [92: What is code splitting?](#92-what-is-code-splitting)
- [93: What does `lazy` do?](#93-what-does-lazy-do)
- [94: Where should you declare a `lazy` component?](#94-where-should-you-declare-a-lazy-component)
- [95: What is route-based code splitting?](#95-what-is-route-based-code-splitting)
- [96: What is component-based code splitting?](#96-what-is-component-based-code-splitting)
- [97: What is tree shaking?](#97-what-is-tree-shaking)
- [98: How can a single import make the bundle much larger?](#98-how-can-a-single-import-make-the-bundle-much-larger)
- [99: How do you check what is in your bundle?](#99-how-do-you-check-what-is-in-your-bundle)
- [100: What is minification?](#100-what-is-minification)
- [101: What is the difference between minification and compression?](#101-what-is-the-difference-between-minification-and-compression)
- [102: Why should you avoid large dependencies for small tasks?](#102-why-should-you-avoid-large-dependencies-for-small-tasks)
- [103: What is a vendor chunk?](#103-what-is-a-vendor-chunk)
- [104: How does long-term caching work with hashed file names?](#104-how-does-long-term-caching-work-with-hashed-file-names)
- [105: What is preloading a lazy component?](#105-what-is-preloading-a-lazy-component)
- [106: What is client-side rendering (CSR)?](#106-what-is-client-side-rendering-csr)
- [107: What is server-side rendering (SSR)?](#107-what-is-server-side-rendering-ssr)
- [108: What is hydration?](#108-what-is-hydration)
- [109: What is a hydration mismatch?](#109-what-is-a-hydration-mismatch)
- [110: What is static site generation (SSG)?](#110-what-is-static-site-generation-ssg)
- [111: What is the difference between SSR and SSG?](#111-what-is-the-difference-between-ssr-and-ssg)
- [112: What are React Server Components?](#112-what-are-react-server-components)
- [113: What does `"use client"` mean?](#113-what-does-use-client-mean)
- [114: Why do Server Components help performance?](#114-why-do-server-components-help-performance)
- [115: What is streaming SSR?](#115-what-is-streaming-ssr)
- [116: What is selective hydration?](#116-what-is-selective-hydration)
- [117: What is Time to First Byte (TTFB)?](#117-what-is-time-to-first-byte-ttfb)
- [118: What is `suppressHydrationWarning`?](#118-what-is-suppresshydrationwarning)
- [119: How do you render something only on the client to avoid a hydration mismatch?](#119-how-do-you-render-something-only-on-the-client-to-avoid-a-hydration-mismatch)
- [120: What is the "shell" in streaming SSR?](#120-what-is-the-shell-in-streaming-ssr)
- [121: Why should you measure before optimizing?](#121-why-should-you-measure-before-optimizing)
- [122: What is React DevTools?](#122-what-is-react-devtools)
- [123: How do you use the React DevTools Profiler?](#123-how-do-you-use-the-react-devtools-profiler)
- [124: What does "Highlight updates when components render" do?](#124-what-does-highlight-updates-when-components-render-do)
- [125: What does "Record why each component rendered while profiling" show?](#125-what-does-record-why-each-component-rendered-while-profiling-show)
- [126: What is the `<Profiler>` component?](#126-what-is-the-profiler-component)
- [127: What is the difference between `actualDuration` and `baseDuration`?](#127-what-is-the-difference-between-actualduration-and-baseduration)
- [128: What is the Chrome DevTools Performance panel used for in React apps?](#128-what-is-the-chrome-devtools-performance-panel-used-for-in-react-apps)
- [129: What are React Performance Tracks?](#129-what-are-react-performance-tracks)
- [130: What are Core Web Vitals?](#130-what-are-core-web-vitals)
- [131: How do you measure Web Vitals in a React app?](#131-how-do-you-measure-web-vitals-in-a-react-app)
- [132: What is Lighthouse?](#132-what-is-lighthouse)
- [133: What is the difference between lab data and field data?](#133-what-is-the-difference-between-lab-data-and-field-data)
- [134: Why should you throttle the CPU when profiling?](#134-why-should-you-throttle-the-cpu-when-profiling)
- [135: What is React Scan?](#135-what-is-react-scan)
- [136: How do you lazy load images in React?](#136-how-do-you-lazy-load-images-in-react)
- [137: Why should images have a width and height?](#137-why-should-images-have-a-width-and-height)
- [138: What is `fetchPriority` and how do you use it in React?](#138-what-is-fetchpriority-and-how-do-you-use-it-in-react)
- [139: What image formats should you use for performance?](#139-what-image-formats-should-you-use-for-performance)
- [140: What is the difference between controlled and uncontrolled inputs?](#140-what-is-the-difference-between-controlled-and-uncontrolled-inputs)
- [141: How do React 19 form actions help with performance?](#141-how-do-react-19-form-actions-help-with-performance)
- [142: Why can CSS-in-JS libraries that work at runtime slow down an app?](#142-why-can-css-in-js-libraries-that-work-at-runtime-slow-down-an-app)
- [143: Why are inline styles sometimes a performance concern?](#143-why-are-inline-styles-sometimes-a-performance-concern)
- [144: How do you avoid memory leaks in React components?](#144-how-do-you-avoid-memory-leaks-in-react-components)
- [145: Why should you avoid animating with React state on every frame?](#145-why-should-you-avoid-animating-with-react-state-on-every-frame)
- [146: What is the cost of rendering icons as React components?](#146-what-is-the-cost-of-rendering-icons-as-react-components)
- [147: How do Portals affect performance?](#147-how-do-portals-affect-performance)
- [148: Why should you avoid heavy work in event handlers?](#148-why-should-you-avoid-heavy-work-in-event-handlers)
- [149: What is a Web Worker and when would a React app use one?](#149-what-is-a-web-worker-and-when-would-a-react-app-use-one)
- [150: What are the most common causes of a slow React app?](#150-what-are-the-most-common-causes-of-a-slow-react-app)

### Moderate Questions (151-300)

- [151: How does passing components as `children` prevent re-renders?](#151-how-does-passing-components-as-children-prevent-re-renders)
- [152: Why does React skip re-rendering an element if it is the same object as last time?](#152-why-does-react-skip-re-rendering-an-element-if-it-is-the-same-object-as-last-time)
- [153: What happens when you conditionally render different component types in the same position?](#153-what-happens-when-you-conditionally-render-different-component-types-in-the-same-position)
- [154: How can you find out why a component re-rendered?](#154-how-can-you-find-out-why-a-component-re-rendered)
- [155: What is the difference between a re-render and a remount?](#155-what-is-the-difference-between-a-re-render-and-a-remount)
- [156: How do fragments affect rendering performance?](#156-how-do-fragments-affect-rendering-performance)
- [157: Is it bad to return a large JSX tree from one component?](#157-is-it-bad-to-return-a-large-jsx-tree-from-one-component)
- [158: How does `flushSync` affect performance?](#158-how-does-flushsync-affect-performance)
- [159: Why can a `useLayoutEffect` that sets state hurt performance?](#159-why-can-a-uselayouteffect-that-sets-state-hurt-performance)
- [160: How do you stop a parent's re-render from re-rendering a heavy child, without `memo`?](#160-how-do-you-stop-a-parents-re-render-from-re-rendering-a-heavy-child-without-memo)
- [161: What are the costs of very deep component trees?](#161-what-are-the-costs-of-very-deep-component-trees)
- [162: What is "render props" and how does it affect performance?](#162-what-is-render-props-and-how-does-it-affect-performance)
- [163: How do higher-order components (HOCs) affect performance?](#163-how-do-higher-order-components-hocs-affect-performance)
- [164: When would you use `key` to reset state instead of an effect?](#164-when-would-you-use-key-to-reset-state-instead-of-an-effect)
- [165: How do you adjust state when a prop changes without an effect?](#165-how-do-you-adjust-state-when-a-prop-changes-without-an-effect)
- [166: When is `useMemo` worth it for a calculation?](#166-when-is-usememo-worth-it-for-a-calculation)
- [167: Why does `memo` not help when you pass `children`?](#167-why-does-memo-not-help-when-you-pass-children)
- [168: How do you write a custom comparison function for `memo`?](#168-how-do-you-write-a-custom-comparison-function-for-memo)
- [169: What does the React Compiler actually memoize?](#169-what-does-the-react-compiler-actually-memoize)
- [170: How does the React Compiler know which functions to compile?](#170-how-does-the-react-compiler-know-which-functions-to-compile)
- [171: What happens when the React Compiler finds code that breaks the Rules of React?](#171-what-happens-when-the-react-compiler-finds-code-that-breaks-the-rules-of-react)
- [172: How do you roll out the React Compiler in an existing app?](#172-how-do-you-roll-out-the-react-compiler-in-an-existing-app)
- [173: Can you use the React Compiler with React 17 or 18?](#173-can-you-use-the-react-compiler-with-react-17-or-18)
- [174: How can you check that the React Compiler optimized a component?](#174-how-can-you-check-that-the-react-compiler-optimized-a-component)
- [175: Why should you not write to or read from `ref.current` during render?](#175-why-should-you-not-write-to-or-read-from-refcurrent-during-render)
- [176: What is the problem with `useCallback` when the callback depends on frequently changing state?](#176-what-is-the-problem-with-usecallback-when-the-callback-depends-on-frequently-changing-state)
- [177: Why might `memo` not stop re-renders of a component that uses context?](#177-why-might-memo-not-stop-re-renders-of-a-component-that-uses-context)
- [178: Does `useMemo` guarantee that the value is never recalculated?](#178-does-usememo-guarantee-that-the-value-is-never-recalculated)
- [179: How does the React Compiler work with existing `useMemo` and `useCallback` calls?](#179-how-does-the-react-compiler-work-with-existing-usememo-and-usecallback-calls)
- [180: Is memoizing a component that renders very little worth it?](#180-is-memoizing-a-component-that-renders-very-little-worth-it)
- [181: How do you split a context into state and dispatch to reduce re-renders?](#181-how-do-you-split-a-context-into-state-and-dispatch-to-reduce-re-renders)
- [182: How do you avoid re-renders when only part of a context value is needed?](#182-how-do-you-avoid-re-renders-when-only-part-of-a-context-value-is-needed)
- [183: Why is a Zustand or Redux store often faster than Context for shared state?](#183-why-is-a-zustand-or-redux-store-often-faster-than-context-for-shared-state)
- [184: What is the problem with selectors that return new objects?](#184-what-is-the-problem-with-selectors-that-return-new-objects)
- [185: What is a memoized selector and when do you need one?](#185-what-is-a-memoized-selector-and-when-do-you-need-one)
- [186: How do you share state between distant components without re-rendering everything in between?](#186-how-do-you-share-state-between-distant-components-without-re-rendering-everything-in-between)
- [187: What is `useSyncExternalStore` and why does it matter for performance?](#187-what-is-usesyncexternalstore-and-why-does-it-matter-for-performance)
- [188: How should you store server data versus UI state?](#188-how-should-you-store-server-data-versus-ui-state)
- [189: How does storing form input in global state affect performance?](#189-how-does-storing-form-input-in-global-state-affect-performance)
- [190: What is the problem with putting everything in one big `useState` object?](#190-what-is-the-problem-with-putting-everything-in-one-big-usestate-object)
- [191: How do atomic state libraries like Jotai help with performance?](#191-how-do-atomic-state-libraries-like-jotai-help-with-performance)
- [192: How do you store state in the URL without slowing the app down?](#192-how-do-you-store-state-in-the-url-without-slowing-the-app-down)
- [193: How do you avoid passing many props that change often to deep children?](#193-how-do-you-avoid-passing-many-props-that-change-often-to-deep-children)
- [194: What is "state colocation"?](#194-what-is-state-colocation)
- [195: What is the cost of putting a big object in state and updating it immutably?](#195-what-is-the-cost-of-putting-a-big-object-in-state-and-updating-it-immutably)
- [196: How do you virtualize a list with TanStack Virtual?](#196-how-do-you-virtualize-a-list-with-tanstack-virtual)
- [197: How do you virtualize rows with different heights?](#197-how-do-you-virtualize-rows-with-different-heights)
- [198: What is overscan in virtualization?](#198-what-is-overscan-in-virtualization)
- [199: What are the downsides of virtualization?](#199-what-are-the-downsides-of-virtualization)
- [200: How do you keep row state when rows scroll out of a virtualized list?](#200-how-do-you-keep-row-state-when-rows-scroll-out-of-a-virtualized-list)
- [201: How do you make a fast client-side search over thousands of items?](#201-how-do-you-make-a-fast-client-side-search-over-thousands-of-items)
- [202: How do you avoid re-rendering every row when the selection changes?](#202-how-do-you-avoid-re-rendering-every-row-when-the-selection-changes)
- [203: How do you handle a list that receives frequent real-time updates?](#203-how-do-you-handle-a-list-that-receives-frequent-real-time-updates)
- [204: What is the cost of sorting inside a render in a table with many columns?](#204-what-is-the-cost-of-sorting-inside-a-render-in-a-table-with-many-columns)
- [205: How does TanStack Table help with large tables?](#205-how-does-tanstack-table-help-with-large-tables)
- [206: When should you do filtering and pagination on the server instead of the client?](#206-when-should-you-do-filtering-and-pagination-on-the-server-instead-of-the-client)
- [207: How do you make infinite scroll with TanStack Query?](#207-how-do-you-make-infinite-scroll-with-tanstack-query)
- [208: How do you render a grid of thousands of images efficiently?](#208-how-do-you-render-a-grid-of-thousands-of-images-efficiently)
- [209: What is "time slicing" for big lists, and how do you do it in React?](#209-what-is-time-slicing-for-big-lists-and-how-do-you-do-it-in-react)
- [210: How do you show a large tree (like a file explorer) efficiently?](#210-how-do-you-show-a-large-tree-like-a-file-explorer-efficiently)
- [211: What is `useEffectEvent` and how does it help?](#211-what-is-useeffectevent-and-how-does-it-help)
- [212: How do you fetch data in parallel instead of in a waterfall?](#212-how-do-you-fetch-data-in-parallel-instead-of-in-a-waterfall)
- [213: What is "fetch on render" vs "render as you fetch"?](#213-what-is-fetch-on-render-vs-render-as-you-fetch)
- [214: How do you prefetch data before the user needs it?](#214-how-do-you-prefetch-data-before-the-user-needs-it)
- [215: What is `staleTime` in TanStack Query and why does it matter?](#215-what-is-staletime-in-tanstack-query-and-why-does-it-matter)
- [216: What is stale-while-revalidate?](#216-what-is-stale-while-revalidate)
- [217: How do you avoid a loading spinner flash on fast requests?](#217-how-do-you-avoid-a-loading-spinner-flash-on-fast-requests)
- [218: How do Server Actions or form actions reduce client code?](#218-how-do-server-actions-or-form-actions-reduce-client-code)
- [219: Why should you avoid chaining effects that set state?](#219-why-should-you-avoid-chaining-effects-that-set-state)
- [220: How does `cache` from React help in Server Components?](#220-how-does-cache-from-react-help-in-server-components)
- [221: How do you handle data that many components need, without fetching it many times?](#221-how-do-you-handle-data-that-many-components-need-without-fetching-it-many-times)
- [222: What is the cost of refetching on window focus?](#222-what-is-the-cost-of-refetching-on-window-focus)
- [223: How do you optimize polling in React?](#223-how-do-you-optimize-polling-in-react)
- [224: How do you avoid a re-render storm from a WebSocket?](#224-how-do-you-avoid-a-re-render-storm-from-a-websocket)
- [225: Why does StrictMode make effects run twice, and should you work around it?](#225-why-does-strictmode-make-effects-run-twice-and-should-you-work-around-it)
- [226: How do you use a transition to keep a tab switch responsive?](#226-how-do-you-use-a-transition-to-keep-a-tab-switch-responsive)
- [227: Can you use async functions inside `startTransition`?](#227-can-you-use-async-functions-inside-starttransition)
- [228: Why doesn't `useDeferredValue` help if the slow component isn't memoized?](#228-why-doesnt-usedeferredvalue-help-if-the-slow-component-isnt-memoized)
- [229: What does the `initialValue` argument of `useDeferredValue` do?](#229-what-does-the-initialvalue-argument-of-usedeferredvalue-do)
- [230: How do Suspense and transitions work together when navigating?](#230-how-do-suspense-and-transitions-work-together-when-navigating)
- [231: What does it mean that Suspense boundaries "reveal together"?](#231-what-does-it-mean-that-suspense-boundaries-reveal-together)
- [232: How do you keep old content visible during a search instead of showing a fallback?](#232-how-do-you-keep-old-content-visible-during-a-search-instead-of-showing-a-fallback)
- [233: What is tearing and how does React prevent it?](#233-what-is-tearing-and-how-does-react-prevent-it)
- [234: How should you use `<Activity>` to make tab switches faster?](#234-how-should-you-use-activity-to-make-tab-switches-faster)
- [235: What happens to effects inside a hidden `<Activity>`?](#235-what-happens-to-effects-inside-a-hidden-activity)
- [236: When should you not use a transition?](#236-when-should-you-not-use-a-transition)
- [237: How does Suspense with `lazy` and data fetching combine?](#237-how-does-suspense-with-lazy-and-data-fetching-combine)
- [238: How do you avoid a "popcorn" effect where many parts load in one by one?](#238-how-do-you-avoid-a-popcorn-effect-where-many-parts-load-in-one-by-one)
- [239: What are error boundaries and how do they relate to performance?](#239-what-are-error-boundaries-and-how-do-they-relate-to-performance)
- [240: How does React decide which update to handle first?](#240-how-does-react-decide-which-update-to-handle-first)
- [241: How do you lazy load a named export?](#241-how-do-you-lazy-load-a-named-export)
- [242: How do you handle errors when a lazy chunk fails to load?](#242-how-do-you-handle-errors-when-a-lazy-chunk-fails-to-load)
- [243: How do you code split with `next/dynamic` in Next.js?](#243-how-do-you-code-split-with-nextdynamic-in-nextjs)
- [244: What is the problem with too much code splitting?](#244-what-is-the-problem-with-too-much-code-splitting)
- [245: What does the `sideEffects` field in `package.json` do?](#245-what-does-the-sideeffects-field-in-packagejson-do)
- [246: Why do barrel files sometimes make bundles bigger or builds slower?](#246-why-do-barrel-files-sometimes-make-bundles-bigger-or-builds-slower)
- [247: How do you find and remove unused code from a React app?](#247-how-do-you-find-and-remove-unused-code-from-a-react-app)
- [248: How do you keep polyfills from making the bundle bigger for modern browsers?](#248-how-do-you-keep-polyfills-from-making-the-bundle-bigger-for-modern-browsers)
- [249: How do you load a heavy library only when needed?](#249-how-do-you-load-a-heavy-library-only-when-needed)
- [250: What is the difference between `preload` and `prefetch` for chunks?](#250-what-is-the-difference-between-preload-and-prefetch-for-chunks)
- [251: What resource loading APIs does React 19 add?](#251-what-resource-loading-apis-does-react-19-add)
- [252: How do you reduce the size of icon and date libraries?](#252-how-do-you-reduce-the-size-of-icon-and-date-libraries)
- [253: How do Server Components reduce bundle size compared to code splitting?](#253-how-do-server-components-reduce-bundle-size-compared-to-code-splitting)
- [254: Why is it important to check bundle size in CI?](#254-why-is-it-important-to-check-bundle-size-in-ci)
- [255: What is the cost of shipping source maps to production?](#255-what-is-the-cost-of-shipping-source-maps-to-production)
- [256: How do you stream HTML with `renderToPipeableStream` in Node.js?](#256-how-do-you-stream-html-with-rendertopipeablestream-in-nodejs)
- [257: Why should you avoid `renderToString` for new SSR code?](#257-why-should-you-avoid-rendertostring-for-new-ssr-code)
- [258: How do you reduce the cost of hydration?](#258-how-do-you-reduce-the-cost-of-hydration)
- [259: What does a hydration mismatch cost in React 19?](#259-what-does-a-hydration-mismatch-cost-in-react-19)
- [260: How do you render dates and times without hydration mismatches?](#260-how-do-you-render-dates-and-times-without-hydration-mismatches)
- [261: What is the cost of passing large props from Server Components to Client Components?](#261-what-is-the-cost-of-passing-large-props-from-server-components-to-client-components)
- [262: How do you keep `"use client"` boundaries small?](#262-how-do-you-keep-use-client-boundaries-small)
- [263: How do you stream data from a Server Component without blocking the page?](#263-how-do-you-stream-data-from-a-server-component-without-blocking-the-page)
- [264: What is partial pre-rendering?](#264-what-is-partial-pre-rendering)
- [265: How do you cache SSR output?](#265-how-do-you-cache-ssr-output)
- [266: How does where you run SSR affect performance?](#266-how-does-where-you-run-ssr-affect-performance)
- [267: How do you avoid sending the same data twice with SSR?](#267-how-do-you-avoid-sending-the-same-data-twice-with-ssr)
- [268: What should go in the shell to improve perceived performance?](#268-what-should-go-in-the-shell-to-improve-perceived-performance)
- [269: How do you hydrate only part of a page?](#269-how-do-you-hydrate-only-part-of-a-page)
- [270: How do `onCaughtError` and `onUncaughtError` help in production?](#270-how-do-oncaughterror-and-onuncaughterror-help-in-production)
- [271: How do you read the flame chart in the React Profiler?](#271-how-do-you-read-the-flame-chart-in-the-react-profiler)
- [272: What does the ranked chart in the React Profiler show?](#272-what-does-the-ranked-chart-in-the-react-profiler-show)
- [273: How do you profile a React app in production?](#273-how-do-you-profile-a-react-app-in-production)
- [274: How do you find what is causing a slow interaction (bad INP)?](#274-how-do-you-find-what-is-causing-a-slow-interaction-bad-inp)
- [275: What are the three parts of INP and how do they map to React?](#275-what-are-the-three-parts-of-inp-and-how-do-they-map-to-react)
- [276: How do you use `<Profiler>` to send render timings to analytics?](#276-how-do-you-use-profiler-to-send-render-timings-to-analytics)
- [277: How do you add your own marks to the Chrome performance timeline?](#277-how-do-you-add-your-own-marks-to-the-chrome-performance-timeline)
- [278: Why might a component look slow in the Profiler but not be the real problem?](#278-why-might-a-component-look-slow-in-the-profiler-but-not-be-the-real-problem)
- [279: How do you detect unnecessary renders automatically?](#279-how-do-you-detect-unnecessary-renders-automatically)
- [280: How do you measure the time it takes to load a lazy component?](#280-how-do-you-measure-the-time-it-takes-to-load-a-lazy-component)
- [281: How do you find memory leaks in a React app?](#281-how-do-you-find-memory-leaks-in-a-react-app)
- [282: How do you check for layout shift caused by React rendering?](#282-how-do-you-check-for-layout-shift-caused-by-react-rendering)
- [283: What does the Coverage tab show and how does it help a React app?](#283-what-does-the-coverage-tab-show-and-how-does-it-help-a-react-app)
- [284: How do you compare performance before and after a change?](#284-how-do-you-compare-performance-before-and-after-a-change)
- [285: How does the React DevTools "Timeline" view differ from the flame chart?](#285-how-does-the-react-devtools-timeline-view-differ-from-the-flame-chart)
- [286: How do you optimize a large form in React?](#286-how-do-you-optimize-a-large-form-in-react)
- [287: How does `useActionState` help with form performance?](#287-how-does-useactionstate-help-with-form-performance)
- [288: How do you load fonts without hurting performance?](#288-how-do-you-load-fonts-without-hurting-performance)
- [289: How do you render stylesheets in React 19 so they load in the right order?](#289-how-do-you-render-stylesheets-in-react-19-so-they-load-in-the-right-order)
- [290: How do you optimize drag and drop in React?](#290-how-do-you-optimize-drag-and-drop-in-react)
- [291: How do you make an expensive tooltip or popover cheap?](#291-how-do-you-make-an-expensive-tooltip-or-popover-cheap)
- [292: How do you handle scroll events without slowing down the app?](#292-how-do-you-handle-scroll-events-without-slowing-down-the-app)
- [293: How do you use a Web Worker from a React component cleanly?](#293-how-do-you-use-a-web-worker-from-a-react-component-cleanly)
- [294: How do third-party scripts affect a React app?](#294-how-do-third-party-scripts-affect-a-react-app)
- [295: How do you avoid layout shift when content loads in React?](#295-how-do-you-avoid-layout-shift-when-content-loads-in-react)
- [296: How do you optimize animations in React?](#296-how-do-you-optimize-animations-in-react)
- [297: How do you show many charts on a dashboard without freezing the page?](#297-how-do-you-show-many-charts-on-a-dashboard-without-freezing-the-page)
- [298: How does `useId` relate to performance?](#298-how-does-useid-relate-to-performance)
- [299: What are ref callbacks with cleanup in React 19, and how do they help?](#299-what-are-ref-callbacks-with-cleanup-in-react-19-and-how-do-they-help)
- [300: How is optimizing a React Native app different from optimizing a React web app?](#300-how-is-optimizing-a-react-native-app-different-from-optimizing-a-react-web-app)

### Advanced Questions (301-450)

- [301: What is a Fiber?](#301-what-is-a-fiber)
- [302: What is double buffering in React's fiber tree?](#302-what-is-double-buffering-in-reacts-fiber-tree)
- [303: How does React bail out of rendering a subtree?](#303-how-does-react-bail-out-of-rendering-a-subtree)
- [304: What is the "eager state" optimization and when does it apply?](#304-what-is-the-eager-state-optimization-and-when-does-it-apply)
- [305: How does React update a DOM element when its props change?](#305-how-does-react-update-a-dom-element-when-its-props-change)
- [306: How does the React work loop yield to the browser?](#306-how-does-the-react-work-loop-yield-to-the-browser)
- [307: What are lanes and how do they replace the old expiration times?](#307-what-are-lanes-and-how-do-they-replace-the-old-expiration-times)
- [308: What is starvation in concurrent rendering, and how does React handle it?](#308-what-is-starvation-in-concurrent-rendering-and-how-does-react-handle-it)
- [309: Why can a component render without committing?](#309-why-can-a-component-render-without-committing)
- [310: How do you debug a component that re-renders in an infinite loop?](#310-how-do-you-debug-a-component-that-re-renders-in-an-infinite-loop)
- [311: What is the cost of very large props objects or spreading props through many layers?](#311-what-is-the-cost-of-very-large-props-objects-or-spreading-props-through-many-layers)
- [312: How does React handle a component returning the same JSX structure but with different keys at the root?](#312-how-does-react-handle-a-component-returning-the-same-jsx-structure-but-with-different-keys-at-the-root)
- [313: What is "render-phase update" and why does React warn about updating another component during render?](#313-what-is-render-phase-update-and-why-does-react-warn-about-updating-another-component-during-render)
- [314: How does `memo` interact with `ref` props in React 19?](#314-how-does-memo-interact-with-ref-props-in-react-19)
- [315: A page is slow only after the user has been on it for a while. What would you check?](#315-a-page-is-slow-only-after-the-user-has-been-on-it-for-a-while-what-would-you-check)
- [316: What does the output of the React Compiler look like?](#316-what-does-the-output-of-the-react-compiler-look-like)
- [317: How is the compiler's memoization different from `useMemo`?](#317-how-is-the-compilers-memoization-different-from-usememo)
- [318: Why does the React Compiler need code to follow the Rules of React to be correct?](#318-why-does-the-react-compiler-need-code-to-follow-the-rules-of-react-to-be-correct)
- [319: What kinds of bugs can show up after enabling the React Compiler?](#319-what-kinds-of-bugs-can-show-up-after-enabling-the-react-compiler)
- [320: How do you handle a third-party hook that returns a mutable object with the React Compiler?](#320-how-do-you-handle-a-third-party-hook-that-returns-a-mutable-object-with-the-react-compiler)
- [321: Does the React Compiler make `memo` around components unnecessary?](#321-does-the-react-compiler-make-memo-around-components-unnecessary)
- [322: How does memoization interact with Context in compiled code?](#322-how-does-memoization-interact-with-context-in-compiled-code)
- [323: How do you measure whether the React Compiler improved performance?](#323-how-do-you-measure-whether-the-react-compiler-improved-performance)
- [324: What is the cost of memoization itself?](#324-what-is-the-cost-of-memoization-itself)
- [325: How would you memoize an expensive function across components, not only within one?](#325-how-would-you-memoize-an-expensive-function-across-components-not-only-within-one)
- [326: When does the compiler skip memoizing a value?](#326-when-does-the-compiler-skip-memoizing-a-value)
- [327: How do `useMemo` and `useCallback` behave in StrictMode during development?](#327-how-do-usememo-and-usecallback-behave-in-strictmode-during-development)
- [328: Why can memoization hide bugs, and how do you test for that?](#328-why-can-memoization-hide-bugs-and-how-do-you-test-for-that)
- [329: How do you deal with callbacks passed to many memoized children that need fresh state?](#329-how-do-you-deal-with-callbacks-passed-to-many-memoized-children-that-need-fresh-state)
- [330: What is the trade-off between fine-grained memoization and code size in the compiler output?](#330-what-is-the-trade-off-between-fine-grained-memoization-and-code-size-in-the-compiler-output)
- [331: How does React propagate a context change internally?](#331-how-does-react-propagate-a-context-change-internally)
- [332: How would you build a context with selectors yourself?](#332-how-would-you-build-a-context-with-selectors-yourself)
- [333: How do you design state for a large editor or canvas app where many items change often?](#333-how-do-you-design-state-for-a-large-editor-or-canvas-app-where-many-items-change-often)
- [334: What is the problem with storing derived data in a global store?](#334-what-is-the-problem-with-storing-derived-data-in-a-global-store)
- [335: How do you prevent a frequently updating value (like a timer) from re-rendering the whole app?](#335-how-do-you-prevent-a-frequently-updating-value-like-a-timer-from-re-rendering-the-whole-app)
- [336: How does `useSyncExternalStore` affect concurrent features?](#336-how-does-usesyncexternalstore-affect-concurrent-features)
- [337: How do you handle state that needs to be shared between Server Components and Client Components?](#337-how-do-you-handle-state-that-needs-to-be-shared-between-server-components-and-client-components)
- [338: How do you avoid re-renders from a context that holds functions?](#338-how-do-you-avoid-re-renders-from-a-context-that-holds-functions)
- [339: When does lifting state up become a performance problem, and what's the alternative?](#339-when-does-lifting-state-up-become-a-performance-problem-and-whats-the-alternative)
- [340: How do you persist state to `localStorage` without slowing down every update?](#340-how-do-you-persist-state-to-localstorage-without-slowing-down-every-update)
- [341: How does Immer's structural sharing help memoization?](#341-how-does-immers-structural-sharing-help-memoization)
- [342: What are signals and how do they compare to React's model?](#342-what-are-signals-and-how-do-they-compare-to-reacts-model)
- [343: How do you split a large Redux store so updates don't touch unrelated components?](#343-how-do-you-split-a-large-redux-store-so-updates-dont-touch-unrelated-components)
- [344: How do you handle state for very large forms with hundreds of fields?](#344-how-do-you-handle-state-for-very-large-forms-with-hundreds-of-fields)
- [345: Your app has a single top-level context with user, theme, cart and notifications. Typing in a search box is slow. How do you approach it?](#345-your-app-has-a-single-top-level-context-with-user-theme-cart-and-notifications-typing-in-a-search-box-is-slow-how-do-you-approach-it)
- [346: How does React's list reconciliation work, and what is its cost?](#346-how-does-reacts-list-reconciliation-work-and-what-is-its-cost)
- [347: Why is moving an item from the end of a list to the start more expensive than the other way?](#347-why-is-moving-an-item-from-the-end-of-a-list-to-the-start-more-expensive-than-the-other-way)
- [348: How do you build a virtualized chat that keeps the scroll position when older messages load at the top?](#348-how-do-you-build-a-virtualized-chat-that-keeps-the-scroll-position-when-older-messages-load-at-the-top)
- [349: How do you virtualize a grid with both many rows and many columns?](#349-how-do-you-virtualize-a-grid-with-both-many-rows-and-many-columns)
- [350: How would you render a table with 100,000 rows that the user can sort and filter?](#350-how-would-you-render-a-table-with-100000-rows-that-the-user-can-sort-and-filter)
- [351: How do you avoid creating 100,000 objects on every update in a big data set?](#351-how-do-you-avoid-creating-100000-objects-on-every-update-in-a-big-data-set)
- [352: How does `key` choice affect performance when data is refetched?](#352-how-does-key-choice-affect-performance-when-data-is-refetched)
- [353: What is structural sharing in TanStack Query?](#353-what-is-structural-sharing-in-tanstack-query)
- [354: How do you use the `select` option in TanStack Query to reduce re-renders?](#354-how-do-you-use-the-select-option-in-tanstack-query-to-reduce-re-renders)
- [355: How do you render very large text or logs efficiently?](#355-how-do-you-render-very-large-text-or-logs-efficiently)
- [356: When should you move list rendering to canvas or WebGL?](#356-when-should-you-move-list-rendering-to-canvas-or-webgl)
- [357: How do you keep a virtualized list accessible?](#357-how-do-you-keep-a-virtualized-list-accessible)
- [358: How do you avoid jank when a virtualized list's rows contain images?](#358-how-do-you-avoid-jank-when-a-virtualized-lists-rows-contain-images)
- [359: How do you handle sorting and grouping that change the structure of a big list without remounting everything?](#359-how-do-you-handle-sorting-and-grouping-that-change-the-structure-of-a-big-list-without-remounting-everything)
- [360: A list of 2,000 cards takes 800 ms to render on first load. How do you fix it?](#360-a-list-of-2000-cards-takes-800-ms-to-render-on-first-load-how-do-you-fix-it)
- [361: How do Server Components remove client-side waterfalls?](#361-how-do-server-components-remove-client-side-waterfalls)
- [362: How do you avoid a waterfall between parent and child Server Components?](#362-how-do-you-avoid-a-waterfall-between-parent-and-child-server-components)
- [363: What is `cacheSignal` and when would you use it?](#363-what-is-cachesignal-and-when-would-you-use-it)
- [364: How do you design client-side cache invalidation after a mutation?](#364-how-do-you-design-client-side-cache-invalidation-after-a-mutation)
- [365: How do you implement optimistic updates safely?](#365-how-do-you-implement-optimistic-updates-safely)
- [366: How can effects make INP worse?](#366-how-can-effects-make-inp-worse)
- [367: When does React run `useEffect` before the browser paints?](#367-when-does-react-run-useeffect-before-the-browser-paints)
- [368: How do you deduplicate requests made at the same time by different components without a library?](#368-how-do-you-deduplicate-requests-made-at-the-same-time-by-different-components-without-a-library)
- [369: Why can't you create a promise in a Client Component render and pass it to `use`?](#369-why-cant-you-create-a-promise-in-a-client-component-render-and-pass-it-to-use)
- [370: How do you avoid fetching data twice with SSR and a client data library?](#370-how-do-you-avoid-fetching-data-twice-with-ssr-and-a-client-data-library)
- [371: How does `useEffect` cleanup ordering affect performance when navigating?](#371-how-does-useeffect-cleanup-ordering-affect-performance-when-navigating)
- [372: How do you handle a slow third-party widget that must be initialized in an effect?](#372-how-do-you-handle-a-slow-third-party-widget-that-must-be-initialized-in-an-effect)
- [373: What are the performance trade-offs of GraphQL clients like Apollo in React?](#373-what-are-the-performance-trade-offs-of-graphql-clients-like-apollo-in-react)
- [374: How do you stop an expensive effect from running when only a callback prop changes identity?](#374-how-do-you-stop-an-expensive-effect-from-running-when-only-a-callback-prop-changes-identity)
- [375: A dashboard makes 40 API calls on load. How would you improve it?](#375-a-dashboard-makes-40-api-calls-on-load-how-would-you-improve-it)
- [376: How are transitions implemented internally?](#376-how-are-transitions-implemented-internally)
- [377: Why can a transition still make the page janky?](#377-why-can-a-transition-still-make-the-page-janky)
- [378: How does React decide whether to show a Suspense fallback or keep old content?](#378-how-does-react-decide-whether-to-show-a-suspense-fallback-or-keep-old-content)
- [379: What does "throttling of Suspense fallbacks" mean?](#379-what-does-throttling-of-suspense-fallbacks-mean)
- [380: How does `<Activity>` pre-rendering work and what does it cost?](#380-how-does-activity-pre-rendering-work-and-what-does-it-cost)
- [381: Why should you be careful with `<Activity>` and things like videos or audio?](#381-why-should-you-be-careful-with-activity-and-things-like-videos-or-audio)
- [382: How does selective hydration prioritize user input?](#382-how-does-selective-hydration-prioritize-user-input)
- [383: What is the difference between `useDeferredValue` and debouncing for performance?](#383-what-is-the-difference-between-usedeferredvalue-and-debouncing-for-performance)
- [384: How can you yield to the browser inside a long event handler?](#384-how-can-you-yield-to-the-browser-inside-a-long-event-handler)
- [385: Why might `isPending` from `useTransition` flicker, and how do you fix it?](#385-why-might-ispending-from-usetransition-flicker-and-how-do-you-fix-it)
- [386: How do concurrent renders interact with refs and DOM measurement?](#386-how-do-concurrent-renders-interact-with-refs-and-dom-measurement)
- [387: What is the `<ViewTransition>` component and what is its status?](#387-what-is-the-viewtransition-component-and-what-is-its-status)
- [388: What happens when a component suspends during a sync update?](#388-what-happens-when-a-component-suspends-during-a-sync-update)
- [389: How do you test that an update is non-blocking?](#389-how-do-you-test-that-an-update-is-non-blocking)
- [390: Typing in a filter box is laggy because the results list re-renders on each key press. Walk through the fix.](#390-typing-in-a-filter-box-is-laggy-because-the-results-list-re-renders-on-each-key-press-walk-through-the-fix)
- [391: How do you avoid a chunk loading waterfall with nested lazy components?](#391-how-do-you-avoid-a-chunk-loading-waterfall-with-nested-lazy-components)
- [392: How do frameworks preload route chunks before navigation?](#392-how-do-frameworks-preload-route-chunks-before-navigation)
- [393: What are the risks of `lazy` for components above the fold?](#393-what-are-the-risks-of-lazy-for-components-above-the-fold)
- [394: How do you analyze why a specific module ended up in the main bundle?](#394-how-do-you-analyze-why-a-specific-module-ended-up-in-the-main-bundle)
- [395: How do you split a large component library so apps only load what they use?](#395-how-do-you-split-a-large-component-library-so-apps-only-load-what-they-use)
- [396: What is module federation and what are its performance costs?](#396-what-is-module-federation-and-what-are-its-performance-costs)
- [397: How do you keep two copies of React from ending up in the bundle?](#397-how-do-you-keep-two-copies-of-react-from-ending-up-in-the-bundle)
- [398: How does using Server Components change the code splitting strategy?](#398-how-does-using-server-components-change-the-code-splitting-strategy)
- [399: How do you measure the real cost of JavaScript, not just its size?](#399-how-do-you-measure-the-real-cost-of-javascript-not-just-its-size)
- [400: How does the browser's code cache affect repeat visits, and how do you help it?](#400-how-does-the-browsers-code-cache-affect-repeat-visits-and-how-do-you-help-it)
- [401: When would you inline critical JavaScript or CSS, and what are the trade-offs?](#401-when-would-you-inline-critical-javascript-or-css-and-what-are-the-trade-offs)
- [402: How do you lazy load translations in a large internationalized React app?](#402-how-do-you-lazy-load-translations-in-a-large-internationalized-react-app)
- [403: What is the cost of the React runtime itself, and can you make it smaller?](#403-what-is-the-cost-of-the-react-runtime-itself-and-can-you-make-it-smaller)
- [404: How do you prevent a new dependency from silently growing the bundle in a team?](#404-how-do-you-prevent-a-new-dependency-from-silently-growing-the-bundle-in-a-team)
- [405: The main bundle is 1.2 MB and LCP is 5 seconds on mobile. What's your plan?](#405-the-main-bundle-is-12-mb-and-lcp-is-5-seconds-on-mobile-whats-your-plan)
- [406: How does streaming SSR send content out of order?](#406-how-does-streaming-ssr-send-content-out-of-order)
- [407: What is the RSC payload and why does its size matter?](#407-what-is-the-rsc-payload-and-why-does-its-size-matter)
- [408: Why does initial HTML with RSC contain the data twice, and how do you reduce it?](#408-why-does-initial-html-with-rsc-contain-the-data-twice-and-how-do-you-reduce-it)
- [409: How do you choose between SSR, SSG, ISR and client rendering for each route?](#409-how-do-you-choose-between-ssr-ssg-isr-and-client-rendering-for-each-route)
- [410: How do you find what's slowing down server rendering?](#410-how-do-you-find-whats-slowing-down-server-rendering)
- [411: How do you avoid blocking the Node.js event loop with SSR?](#411-how-do-you-avoid-blocking-the-nodejs-event-loop-with-ssr)
- [412: What is progressive hydration and how does React support it?](#412-what-is-progressive-hydration-and-how-does-react-support-it)
- [413: How do you handle authentication and personalization without losing caching?](#413-how-do-you-handle-authentication-and-personalization-without-losing-caching)
- [414: What happens to hydration if the server HTML has an error in a Suspense boundary?](#414-what-happens-to-hydration-if-the-server-html-has-an-error-in-a-suspense-boundary)
- [415: How do browser extensions cause hydration mismatches, and how does React 19 deal with it?](#415-how-do-browser-extensions-cause-hydration-mismatches-and-how-does-react-19-deal-with-it)
- [416: How do you stream a large page to bots and users differently?](#416-how-do-you-stream-a-large-page-to-bots-and-users-differently)
- [417: How do you make sure the LCP element is in the initial HTML with SSR?](#417-how-do-you-make-sure-the-lcp-element-is-in-the-initial-html-with-ssr)
- [418: What is the cost of rendering a big component tree on the server on every request?](#418-what-is-the-cost-of-rendering-a-big-component-tree-on-the-server-on-every-request)
- [419: How do you debug a slow hydration?](#419-how-do-you-debug-a-slow-hydration)
- [420: Your SSR page has good LCP but bad INP in the first few seconds. What's going on?](#420-your-ssr-page-has-good-lcp-but-bad-inp-in-the-first-few-seconds-whats-going-on)
- [421: How do you connect a slow INP in field data to a specific React component?](#421-how-do-you-connect-a-slow-inp-in-field-data-to-a-specific-react-component)
- [422: What is the Long Animation Frames API and how does it help React apps?](#422-what-is-the-long-animation-frames-api-and-how-does-it-help-react-apps)
- [423: How do you write a performance regression test for a React component?](#423-how-do-you-write-a-performance-regression-test-for-a-react-component)
- [424: Why can Profiler numbers be misleading for very fast components?](#424-why-can-profiler-numbers-be-misleading-for-very-fast-components)
- [425: How do you profile commit-phase costs versus render-phase costs?](#425-how-do-you-profile-commit-phase-costs-versus-render-phase-costs)
- [426: How do you detect forced synchronous layout caused by React code?](#426-how-do-you-detect-forced-synchronous-layout-caused-by-react-code)
- [427: How do you profile memory usage of a React app over a long session?](#427-how-do-you-profile-memory-usage-of-a-react-app-over-a-long-session)
- [428: How do you know whether a slow page is a React problem or a browser rendering problem?](#428-how-do-you-know-whether-a-slow-page-is-a-react-problem-or-a-browser-rendering-problem)
- [429: How do you use the Performance panel's insights for a React app?](#429-how-do-you-use-the-performance-panels-insights-for-a-react-app)
- [430: How do you measure the effect of a change on real users?](#430-how-do-you-measure-the-effect-of-a-change-on-real-users)
- [431: How do you track custom performance metrics like "time until the dashboard is usable"?](#431-how-do-you-track-custom-performance-metrics-like-time-until-the-dashboard-is-usable)
- [432: Why should you profile with realistic data?](#432-why-should-you-profile-with-realistic-data)
- [433: How do you find which state update caused a slow render?](#433-how-do-you-find-which-state-update-caused-a-slow-render)
- [434: What is the effect of React DevTools being open on performance?](#434-what-is-the-effect-of-react-devtools-being-open-on-performance)
- [435: Your Lighthouse score is 95 but users complain the app is slow. How do you investigate?](#435-your-lighthouse-score-is-95-but-users-complain-the-app-is-slow-how-do-you-investigate)
- [436: How do you build responsive images in a React app without a framework component?](#436-how-do-you-build-responsive-images-in-a-react-app-without-a-framework-component)
- [437: How do you preload the LCP image when it's rendered by a client component?](#437-how-do-you-preload-the-lcp-image-when-its-rendered-by-a-client-component)
- [438: How does CSS-in-JS with runtime injection interact with concurrent rendering?](#438-how-does-css-in-js-with-runtime-injection-interact-with-concurrent-rendering)
- [439: How do you avoid re-rendering a whole form on every keystroke while showing live validation?](#439-how-do-you-avoid-re-rendering-a-whole-form-on-every-keystroke-while-showing-live-validation)
- [440: How do you handle a heavy calculation that must run on every keystroke, like a live markdown preview?](#440-how-do-you-handle-a-heavy-calculation-that-must-run-on-every-keystroke-like-a-live-markdown-preview)
- [441: How do you implement a fast autocomplete with server results?](#441-how-do-you-implement-a-fast-autocomplete-with-server-results)
- [442: How do you keep animations smooth while React is rendering?](#442-how-do-you-keep-animations-smooth-while-react-is-rendering)
- [443: How would you optimize a React app that runs inside a low-powered device, like a smart TV?](#443-how-would-you-optimize-a-react-app-that-runs-inside-a-low-powered-device-like-a-smart-tv)
- [444: How do you use `useInsertionEffect`, and why is it only for CSS-in-JS libraries?](#444-how-do-you-use-useinsertioneffect-and-why-is-it-only-for-css-in-js-libraries)
- [445: How do you handle very large file uploads without freezing the UI?](#445-how-do-you-handle-very-large-file-uploads-without-freezing-the-ui)
- [446: What makes modals and drawers expensive, and how do you make them cheap?](#446-what-makes-modals-and-drawers-expensive-and-how-do-you-make-them-cheap)
- [447: How do you optimize a React app for slow networks?](#447-how-do-you-optimize-a-react-app-for-slow-networks)
- [448: When should you not optimize a React component?](#448-when-should-you-not-optimize-a-react-component)
- [449: How would you set up a performance culture in a React team?](#449-how-would-you-set-up-a-performance-culture-in-a-react-team)
- [450: You join a project with a slow React app and no performance data. What do you do first?](#450-you-join-a-project-with-a-slow-react-app-and-no-performance-data-what-do-you-do-first)

---

## Easy Questions (1-150)

### Easy: Rendering and Re-renders (1-15)

#### 1: What does "rendering" mean in React?

Rendering means React calls your component function to find out what the UI should look like. The function returns JSX, React compares the result with the previous one, and then updates only the parts of the real DOM that changed. So a render is not the same as a DOM update. A component can render many times and the DOM may not change at all.

#### 2: What are the render phase and the commit phase?

The render phase is when React calls your components and works out what changed. It has no visible effect on the screen and React can pause or throw it away. The commit phase is when React applies the changes to the DOM, attaches refs and runs layout effects. After the browser paints, React runs regular effects (`useEffect`). Slow code in the render phase makes every update slow. Slow code in layout effects blocks the paint.

#### 3: What causes a component to re-render?

A component re-renders when:

- its own state changes (`useState`, `useReducer`),
- its parent re-renders,
- a context it reads with `use` or `useContext` changes,
- an external store it subscribes to (through `useSyncExternalStore`) changes.

Prop changes are not a separate cause. Props only change because the parent rendered again, and by default the child re-renders when the parent does, whether the props changed or not.

#### 4: Does a child re-render when its parent re-renders, even if its props didn't change?

Yes. By default React renders the whole subtree under the component that updated. It does not compare props unless you wrap the child in `memo` or use the React Compiler. Usually this is fine because rendering is cheap, but it becomes a problem when the subtree is big or a child does heavy work.

```jsx
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <>
      <button onClick={() => setCount(count + 1)}>{count}</button>
      <Child /> {/* renders again on every click */}
    </>
  );
}
```

#### 5: Is a re-render always a performance problem?

No. Most re-renders take well under a millisecond and nobody notices them. A re-render only matters when it is slow (heavy calculations, many components, big lists) or when it happens very often (on every keystroke, scroll or mouse move). Measure first with the React DevTools Profiler before you try to remove re-renders.

#### 6: What is the virtual DOM?

The virtual DOM is the tree of plain JavaScript objects that your JSX turns into. React keeps the previous tree, builds a new one on each render, compares the two and then updates only the real DOM nodes that differ. Working with plain objects is much cheaper than touching the real DOM, which is why React can render often without being slow.

#### 7: What is reconciliation?

Reconciliation is the process of comparing the new element tree with the old one to decide what to change in the DOM. React uses a few simple rules to keep it fast: if the element type changes (for example `div` to `span`, or `ProfilePage` to `SettingsPage`), React throws away the old subtree and builds a new one. If the type stays the same, it keeps the DOM node or component instance and only updates what changed. For lists, it uses keys to match items.

#### 8: Why should you not define a component inside another component?

Because each render of the parent creates a new function, so React sees a new component type every time. It unmounts the old one and mounts a fresh one, which loses its state and recreates its DOM. This is slow and causes bugs like inputs losing focus.

```jsx
// Bad
function Page() {
  function Row() {
    return <input />;
  }
  return <Row />; // new Row type on every render
}

// Good
function Row() {
  return <input />;
}
function Page() {
  return <Row />;
}
```

#### 9: What is automatic batching?

Since React 18, React groups several state updates into one re-render, even if they happen in a promise, a `setTimeout` or a native event handler. Before React 18, only updates inside React event handlers were batched.

```jsx
function handleClick() {
  setCount((c) => c + 1);
  setFlag((f) => !f);
  // one re-render, not two
}

setTimeout(() => {
  setCount((c) => c + 1);
  setFlag((f) => !f);
  // also one re-render in React 18+
}, 1000);
```

#### 10: What happens if you set state to the same value it already has?

React compares the new value with the old one using `Object.is`. If they are the same, React skips re-rendering the component and its children. It may still call the component once before bailing out, but it won't commit anything. Note that a new object or array is never equal to the old one, even with the same contents.

```jsx
setName("Ann"); // no re-render if name is already "Ann"
setUser({ ...user }); // always re-renders, new object
```

#### 11: Why should component functions be pure?

A pure component returns the same JSX for the same props, state and context, and doesn't change anything outside itself while rendering. React depends on this. It may render a component more than once, pause a render, or throw one away, and features like concurrent rendering and the React Compiler assume your components are pure. Side effects like network calls or changing global variables belong in event handlers or effects.

#### 12: Why does StrictMode render components twice?

In development, `<StrictMode>` calls your component functions twice and runs effects setup, cleanup and setup again. This helps you find impure code and missing cleanup. It only happens in development, so it doesn't affect production speed. Don't measure performance in development mode with StrictMode on and assume production behaves the same.

#### 13: What is the difference between a development build and a production build of React?

The development build includes extra checks, warnings, readable error messages and StrictMode double rendering. The production build removes all of that and is minified, so it is much smaller and faster. Always test performance with a production build. Tools like Vite and Next.js pick the right build automatically based on `NODE_ENV`.

#### 14: How does the `key` prop affect rendering?

React uses `key` to know which element is which between renders. If the key stays the same, React keeps the existing component and its state. If the key changes, React unmounts the old one and mounts a new one. In lists, stable keys let React move items instead of recreating them. Outside lists, changing a key on purpose is a simple way to reset a component's state.

```jsx
<ProfileForm key={userId} userId={userId} />
```

#### 15: What is the cheapest way to avoid a re-render?

Often it's not `memo` but just moving state down. If only one small part of the page uses some state, put that state in a small component instead of the top-level page. Then only that small component re-renders when the state changes.

```jsx
// Before: the whole page re-renders on every keystroke
function Page() {
  const [query, setQuery] = useState("");
  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <HeavyChart />
    </>
  );
}

// After: only SearchBox re-renders
function SearchBox() {
  const [query, setQuery] = useState("");
  return <input value={query} onChange={(e) => setQuery(e.target.value)} />;
}
function Page() {
  return (
    <>
      <SearchBox />
      <HeavyChart />
    </>
  );
}
```

### Easy: Memoization and the React Compiler (16-30)

#### 16: What is memoization?

Memoization means saving the result of some work and reusing it when the inputs are the same, instead of doing the work again. In React it is used in three ways: `memo` skips re-rendering a component when props are the same, `useMemo` caches a calculated value, and `useCallback` caches a function. The React Compiler can add all of this for you automatically.

#### 17: What does `memo` do?

`memo` wraps a component and makes React skip re-rendering it when its props are the same as last time. React compares each prop with `Object.is`. The component still re-renders if its own state or a context it uses changes.

```jsx
import { memo } from "react";

const UserCard = memo(function UserCard({ name }) {
  return <div>{name}</div>;
});
```

#### 18: What does `useMemo` do?

`useMemo` caches the result of a calculation between renders. React runs the function on the first render and then only again when one of the dependencies changes.

```jsx
const visibleTodos = useMemo(
  () => todos.filter((t) => t.status === filter),
  [todos, filter],
);
```

It is useful for slow calculations and for keeping the same object or array reference so that a memoized child or an effect doesn't run again for no reason.

#### 19: What does `useCallback` do?

`useCallback` returns the same function between renders until one of its dependencies changes. It doesn't make the function run faster. It only keeps the reference stable, which matters when you pass the function to a `memo` child or use it in an effect's dependency list.

```jsx
const handleSelect = useCallback((id) => {
  setSelectedId(id);
}, []);
```

#### 20: What is the difference between `useMemo` and `useCallback`?

`useMemo` caches the value a function returns. `useCallback` caches the function itself. `useCallback(fn, deps)` is the same as `useMemo(() => fn, deps)`.

#### 21: Should you wrap every component in `memo` and every function in `useCallback`?

No, not by hand. Each one adds code and a dependency list you have to keep right, and comparing props has a small cost. If the props change on every render anyway, `memo` does nothing useful. Add manual memoization where the Profiler shows a real problem, or let the React Compiler handle it for the whole app.

#### 22: What is the React Compiler?

The React Compiler is a build-time tool that reads your components and hooks and adds memoization automatically. It caches JSX, values and functions so that only the parts affected by a change are recomputed. Version 1.0 was released in October 2025. It works best with code that follows the Rules of React (pure components, no mutating props or state).

#### 23: How do you enable the React Compiler?

You add the Babel plugin to your build. In a Vite project:

```bash
npm install -D babel-plugin-react-compiler
```

```js
// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [
    react({
      babel: {
        plugins: ["babel-plugin-react-compiler"],
      },
    }),
  ],
});
```

In Next.js you set `reactCompiler: true` in `next.config`. Some frameworks, like newer Expo templates, turn it on by default.

#### 24: Do you still need `memo`, `useMemo` and `useCallback` if you use the React Compiler?

Mostly no. The compiler memoizes at a finer level than you would by hand. You can keep the existing calls since the compiler works with them, but new code usually doesn't need them. Some people still use `useMemo` or `useCallback` as an escape hatch when they need an exact guarantee, for example when a value is used as an effect dependency and must not change.

#### 25: What are the Rules of React and why do they matter for performance?

The main rules are: components and hooks must be pure, props and state are read-only (don't mutate them), hooks are called only at the top level, and you only call hooks from components or other hooks. Concurrent rendering, StrictMode and the React Compiler all depend on these rules. If code breaks them, the compiler skips that component, so you lose the automatic optimization.

#### 26: What does `"use no memo"` do?

It is a directive that tells the React Compiler to skip a specific component or hook. You put it at the top of the function body. It is meant as a temporary escape hatch when the compiled version causes a bug, while you fix the underlying code.

```jsx
function LegacyWidget() {
  "use no memo";
  // ...
}
```

#### 27: What is `PureComponent`?

It's the legacy class version of `memo`. A class that extends `PureComponent` re-renders only when a shallow comparison of props or state shows a change. You will see it in older code bases. In new code, use function components with `memo` or the React Compiler.

#### 28: What is `shouldComponentUpdate`?

It's a legacy class component method that returns `true` or `false` to tell React whether to re-render. It gives full control but is easy to get wrong, for example by forgetting to compare a new prop. In function components, `memo` with a custom compare function does the same job.

#### 29: Why does passing an inline object as a prop break `memo`?

Because `{}` creates a new object on every render, so `Object.is` sees a different value each time and the memoized child re-renders anyway. The same goes for inline arrays and arrow functions.

```jsx
// Child re-renders every time
<Chart options={{ color: "red" }} />;

// Stable reference
const chartOptions = { color: "red" }; // outside the component
<Chart options={chartOptions} />;
```

If the value depends on props or state, use `useMemo`, or let the compiler do it.

#### 30: What does the ESLint plugin for React hooks check?

`eslint-plugin-react-hooks` checks the Rules of Hooks and missing or extra dependencies in `useEffect`, `useMemo` and `useCallback` (the `exhaustive-deps` rule). Since version 6 its recommended config also includes rules that come from the React Compiler, so it warns about code the compiler can't optimize, like mutating props or reading refs during render. Running it is the easiest way to keep code compiler-friendly.

### Easy: State and Context (31-45)

#### 31: Why does where you put state matter for performance?

When state changes, the component that owns it and all its children re-render. State at the top of the app means a large part of the tree re-renders on every change. Keep state as close as possible to the components that use it. Lift it up only when several components really need to share it.

#### 32: What is derived state and why should you avoid storing it?

Derived state is data you can calculate from existing props or state, like a filtered list or a full name. If you store it in its own `useState` and sync it with an effect, you get an extra render and a chance for the two values to be out of sync. Just calculate it during render. If the calculation is slow, wrap it in `useMemo`.

```jsx
// Avoid
const [fullName, setFullName] = useState("");
useEffect(() => setFullName(first + " " + last), [first, last]);

// Prefer
const fullName = first + " " + last;
```

#### 33: What is lazy initial state?

If the initial value of `useState` is expensive to create, pass a function instead of the value. React calls it only on the first render. If you pass the value directly, the expensive code runs on every render even though the result is thrown away.

```jsx
// Runs on every render
const [items, setItems] = useState(loadItemsFromStorage());

// Runs once
const [items, setItems] = useState(() => loadItemsFromStorage());
```

#### 34: What is the difference between `useState` and `useRef` for storing values?

Updating state triggers a re-render. Changing `ref.current` does not. Use state for values that affect what is shown on screen. Use a ref for values you need to keep between renders but that don't affect the output, like a timer id, a previous value or a DOM node.

```jsx
const intervalRef = useRef(null);

function start() {
  intervalRef.current = setInterval(tick, 1000); // no re-render
}
```

#### 35: Why do functional updates help with performance?

A functional update like `setCount(c => c + 1)` reads the latest state inside the update, so your handler doesn't need the current value from the closure. That means a `useCallback` around the handler can have an empty dependency list and stay stable, which keeps memoized children from re-rendering.

```jsx
const increment = useCallback(() => {
  setCount((c) => c + 1);
}, []);
```

#### 36: What is Context and how does it cause re-renders?

Context passes a value down the tree without passing props through every level. When the value of a context provider changes, every component that reads that context re-renders, even if it only uses one small part of the value. This makes context a common source of extra re-renders in big apps.

#### 37: Why should you not pass a new object to a Context provider on every render?

If you write `value={{ user, setUser }}` directly, a new object is created each time the provider's component renders. All consumers then re-render, even if `user` didn't change. Memoize the value or let the compiler do it.

```jsx
function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  const value = useMemo(() => ({ user, setUser }), [user]);
  return <UserContext value={value}>{children}</UserContext>;
}
```

In React 19 you can render `<UserContext>` directly as a provider. `<UserContext.Provider>` still works.

#### 38: How does splitting a context help?

If one context holds both data that changes often and data that rarely changes, every consumer re-renders whenever anything changes. Splitting it into two contexts (for example `ThemeContext` and `UserContext`, or a state context and a dispatch context) means each component only re-renders for the data it actually reads.

#### 39: When is Context a bad choice for state?

Context is fine for values that rarely change, like the theme, the current user or the locale. It is a poor fit for state that changes very often, like form input, mouse position or a large shared cache, because every consumer re-renders on every change and there's no built-in way to subscribe to only part of the value. For that kind of state, use local state or a store library with selectors such as Zustand, Redux Toolkit or Jotai.

#### 40: What is a selector in a state library?

A selector is a function that picks the part of the store a component needs. The component only re-renders when that picked value changes, not when any part of the store changes.

```jsx
// Zustand
const count = useStore((state) => state.count);

// Redux Toolkit
const todos = useSelector((state) => state.todos.items);
```

#### 41: What is `useReducer` and does it help with performance?

`useReducer` manages state with a reducer function and returns a `dispatch` function. It isn't faster than `useState` by itself, but `dispatch` never changes, so you can pass it down to children or through context without breaking memoization. It also helps when several pieces of state change together.

#### 42: Is the setter function from `useState` stable?

Yes. React guarantees that the `set` function from `useState` and the `dispatch` function from `useReducer` keep the same identity for the life of the component. You don't need to add them to dependency lists or wrap them in `useCallback`.

#### 43: What is prop drilling, and is it a performance problem?

Prop drilling means passing props through several layers of components that don't use them, just to reach a deeper child. It's mostly a code readability problem, not a speed problem. Context or a store library can fix it, but they bring their own re-render behavior. Sometimes passing JSX as `children` is the simplest fix, because the middle components don't need to know about the props at all.

#### 44: Why should you not mutate state directly?

React decides whether to re-render by comparing references. If you push to an existing array or change an object's field, the reference stays the same, so React may skip the update and the screen shows old data. Mutation also breaks `memo`, `useMemo` and the React Compiler, which all expect new data to come with a new reference.

```jsx
// Wrong
items.push(newItem);
setItems(items);

// Right
setItems([...items, newItem]);
```

#### 45: What does it mean to keep state minimal?

Store only what you can't calculate. Avoid duplicates (the same data in two places), avoid storing a whole selected object when its id is enough, and avoid storing values derived from other state. Less state means fewer updates, fewer re-renders and fewer bugs from values getting out of sync.

```jsx
// Store the id, find the item during render
const [selectedId, setSelectedId] = useState(null);
const selectedItem = items.find((i) => i.id === selectedId);
```

### Easy: Lists and Large Data (46-60)

#### 46: Why do list items need keys?

Keys let React match each item in the new list with the same item in the old list. With good keys, React can keep, move, add or remove only the items that changed. Without keys, or with bad ones, React may update the wrong items, recreate DOM nodes for no reason and mix up component state between rows.

#### 47: Why is using the array index as a key a problem?

If items are added, removed or reordered, the index of each item changes. React then thinks item 0 is still item 0 and reuses its component and state for different data. This causes wrong state in inputs and extra DOM updates. Index keys are only safe when the list never changes order and items are never inserted or removed in the middle.

```jsx
// Prefer a stable id from the data
{
  todos.map((todo) => <TodoItem key={todo.id} todo={todo} />);
}
```

#### 48: Why should you not use `Math.random()` or `crypto.randomUUID()` as a key during render?

Because the key changes on every render, so React thinks every item is new. It unmounts and remounts all rows each time, which is slow and resets their state. Generate ids once, when the data is created, and store them with the data.

#### 49: What is list virtualization?

Virtualization (also called windowing) means rendering only the rows that are visible on screen, plus a few extra above and below. As the user scrolls, the rendered rows change. A list of 10,000 items might only have 20 or 30 rows in the DOM at once, which keeps rendering and memory use low.

#### 50: Which libraries can you use for virtualization in React?

The common ones are TanStack Virtual (`@tanstack/react-virtual`), `react-window` and `react-virtuoso`. TanStack Virtual is headless, so you write the markup yourself. `react-window` and `react-virtuoso` give you ready-made list components. Many table and grid libraries also have virtualization built in.

#### 51: How many items is "too many" to render without virtualization?

There's no fixed number, since it depends on how heavy each row is and on the user's device. A list of a few hundred simple rows is usually fine. Once you have thousands of rows, or rows with many elements, images or inputs, you'll usually see slow first render and janky scrolling. Profile on a mid-range phone, not only on a fast laptop.

#### 52: What is pagination and how is it different from virtualization?

Pagination splits data into pages and loads or shows one page at a time. Virtualization keeps all data in one scrollable list but only renders the visible part. Pagination also reduces how much data you fetch from the server. Virtualization only reduces how much you render. They are often combined, for example infinite scroll that fetches pages and virtualizes the rows.

#### 53: What is infinite scroll?

Infinite scroll loads more items when the user gets close to the end of the list, instead of showing page buttons. It is usually built with an `IntersectionObserver` on a sentinel element at the bottom, or with the helpers in TanStack Query's `useInfiniteQuery`. Without virtualization, the DOM keeps growing as the user scrolls, so long sessions get slower.

#### 54: Why should you avoid filtering or sorting a big list on every render?

Filtering and sorting thousands of items takes time, and if it runs on every render it slows down every update, even ones that have nothing to do with the list. Wrap it in `useMemo` so it only runs when the data or the filter changes, or let the React Compiler cache it.

```jsx
const sorted = useMemo(
  () => [...products].sort((a, b) => a.price - b.price),
  [products],
);
```

#### 55: How can you make each row of a list cheaper to render?

Keep rows simple: fewer DOM elements, no heavy calculations, and no inline components. Move shared logic out of the row. Wrap the row component in `memo` (or use the compiler) and pass stable props, so that updating one row doesn't re-render the others. Pass ids and primitive values instead of new objects when you can.

#### 56: Why does updating one item in a list sometimes re-render all items?

Usually because the list component re-renders and the row components aren't memoized, or because the rows get new props every time, like an inline `onClick={() => select(item.id)}` or a new `style` object. Memoize the row and give it a stable handler that takes the id as an argument.

```jsx
const Row = memo(function Row({ item, onSelect }) {
  return <li onClick={() => onSelect(item.id)}>{item.name}</li>;
});
```

#### 57: What is the CSS property `content-visibility` and how does it help long lists?

`content-visibility: auto` tells the browser to skip layout and paint for elements that are off screen. It doesn't reduce the number of React components or DOM nodes, but it can make the browser's work much cheaper for long pages. It is a lighter option than full virtualization when you have a moderate number of heavy sections.

```css
.card {
  content-visibility: auto;
  contain-intrinsic-size: auto 300px;
}
```

#### 58: Why should you normalize large data sets?

Normalizing means storing items in an object keyed by id instead of nested arrays, like `{ byId: { 1: {...} }, allIds: [1, 2] }`. Looking up or updating one item becomes fast, and you only create new references for the item that changed. That keeps memoized rows from re-rendering when other items update. Redux Toolkit's `createEntityAdapter` does this for you.

#### 59: What is the problem with rendering large tables?

Tables have many cells, so even a few hundred rows can mean tens of thousands of DOM nodes. Browser table layout can also be slow because column widths depend on all rows. Use virtualization, fixed column widths (`table-layout: fixed`) and memoized rows. Libraries like TanStack Table handle sorting and filtering, and you pair them with a virtualizer for rendering.

#### 60: Why can rendering a long list in one go freeze the page?

A big render is one long task on the main thread. While it runs, the browser can't respond to clicks or scroll, so the page looks frozen. Fixes are virtualization, pagination, and marking the update as non-urgent with `startTransition` so React can pause between components and handle user input in the middle.

### Easy: Effects and Data Fetching (61-75)

#### 61: When does `useEffect` run?

`useEffect` runs after React has committed the changes to the DOM and usually after the browser has painted. So it doesn't block the user from seeing the update. It runs after the first render and again whenever one of its dependencies changes. The cleanup runs before the next effect and when the component unmounts.

#### 62: What is the difference between `useEffect` and `useLayoutEffect`?

`useLayoutEffect` runs right after the DOM changes but before the browser paints. It is meant for measuring layout (like an element's size) and updating something before the user sees it, to avoid flicker. Because it blocks painting, slow code in it makes the app feel slow. Use `useEffect` by default.

#### 63: Why can effects cause extra renders?

If an effect calls `setState`, React renders again after the first render has been committed. Code that sets state in an effect just to transform data (derived state) or to respond to a prop change causes a double render every time. Most of those cases can be handled during render or in the event handler instead.

#### 64: What does "You Might Not Need an Effect" mean?

It's the title of a page in the React docs that explains that many effects are unnecessary. Effects are for syncing with something outside React, like a network connection, a browser API or a third-party widget. You don't need an effect to compute values from props, to reset state when a prop changes (use a `key`) or to run code in response to a click (put it in the handler). Removing those effects removes extra renders.

#### 65: What happens if you forget the dependency array in `useEffect`?

The effect runs after every render. If it fetches data, it fetches on every render. If it also sets state, it causes another render, which runs the effect again, and you get an infinite loop. An empty array `[]` makes it run only after mount. A list of values makes it run when one of them changes.

#### 66: Why does an object in the dependency array make an effect run on every render?

Effects compare dependencies with `Object.is`. An object or array created during render is a new reference each time, so React thinks it changed. Move the object inside the effect, depend on its primitive fields, or memoize it.

```jsx
// Runs every render
const options = { roomId };
useEffect(() => connect(options), [options]);

// Runs only when roomId changes
useEffect(() => connect({ roomId }), [roomId]);
```

#### 67: Why do you need a cleanup function in effects?

The cleanup function undoes what the effect did: it removes event listeners, clears timers, closes connections and cancels requests. Without cleanup, these keep running after the component is gone or after the dependencies change. That leaks memory, wastes CPU and can update state with stale data.

```jsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);
}, []);
```

#### 68: How do you cancel a fetch request in an effect?

Use an `AbortController` and abort it in the cleanup. This stops the request when the component unmounts or the dependency changes, so you don't waste bandwidth and you don't show results from an old request.

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

#### 69: Why is fetching data in `useEffect` often not the best option?

Effects run after render, so the request starts late. Nested components each fetching in their own effects create waterfalls, where one request waits for the parent's request to finish. You also have to handle caching, race conditions, loading states and duplicate requests yourself. A data library like TanStack Query or SWR, or your framework's data loading (Server Components, route loaders), solves these problems.

#### 70: What is a request waterfall?

A waterfall is when requests run one after another instead of in parallel, because each one only starts after the previous one finished. In React this often happens when a parent fetches data, renders a child, and only then the child starts its own fetch. The page takes as long as the sum of all requests instead of the longest one. Fix it by starting requests together, higher in the tree or in the route loader.

#### 71: What does a data fetching library like TanStack Query give you?

It caches responses by key, so several components asking for the same data share one request. It removes duplicate requests, refetches in the background, retries on failure, and handles loading and error states. It also cancels outdated requests. All of that means fewer network calls and fewer unneeded renders.

```jsx
const { data, isPending } = useQuery({
  queryKey: ["user", id],
  queryFn: () => fetch(`/api/users/${id}`).then((r) => r.json()),
});
```

#### 72: What is a race condition in data fetching?

If the user changes the input quickly, several requests can be in flight at once, and they may come back in any order. If the older one finishes last, its result overwrites the newer one and the screen shows wrong data. Fix it by aborting old requests, ignoring stale results with a flag in the cleanup, or using a data library that handles it.

#### 73: What is debouncing and when do you use it in React?

Debouncing waits until the user stops doing something for a short time before running the code. It's common for search inputs, where you don't want to send a request on every keystroke.

```jsx
useEffect(() => {
  const id = setTimeout(() => {
    search(query);
  }, 300);
  return () => clearTimeout(id);
}, [query]);
```

For keeping the UI responsive while filtering local data, `useDeferredValue` is often a better fit than a debounce.

#### 74: What is throttling?

Throttling runs a function at most once in a set time window, no matter how often the event fires. It fits events that fire constantly, like scroll, resize or mouse move, where you want regular updates but not hundreds per second. For visual updates, `requestAnimationFrame` is another option, since it limits work to once per frame.

#### 75: What is the `use` hook?

`use` is a React 19 API that reads the value of a promise or a context. When you pass it a promise, the component suspends until the promise resolves, and the nearest `<Suspense>` boundary shows its fallback. Unlike other hooks, `use` can be called inside conditions and loops. On the client, the promise must come from a cache or from a parent (for example a Server Component), not be created during render, or it will be recreated on every render.

```jsx
function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map((c) => <p key={c.id}>{c.text}</p>);
}
```

### Easy: Concurrent Features and Suspense (76-90)

#### 76: What is concurrent rendering?

Concurrent rendering lets React prepare several versions of the UI at once and pause, resume or drop a render that's in progress. This means an urgent update, like typing, can interrupt a slow, non-urgent one, like re-rendering a big list. You turn it on by using `createRoot` and opt in per update with features like `startTransition` and `useDeferredValue`.

#### 77: What is a transition?

A transition marks a state update as non-urgent. React renders it in the background and lets urgent updates (typing, clicking) go first. If a newer transition starts, React drops the old one. The current UI stays on screen until the new one is ready.

```jsx
import { startTransition } from "react";

function selectTab(nextTab) {
  startTransition(() => {
    setTab(nextTab);
  });
}
```

#### 78: What does `useTransition` return?

It returns `[isPending, startTransition]`. `isPending` is `true` while the transition is rendering, so you can show a spinner or dim the old content. `startTransition` wraps the state update you want to mark as non-urgent.

```jsx
const [isPending, startTransition] = useTransition();

<button onClick={() => startTransition(() => setTab("posts"))}>
  Posts {isPending && <Spinner />}
</button>;
```

#### 79: What is `useDeferredValue`?

`useDeferredValue` gives you a version of a value that "lags behind" during fast updates. React first re-renders with the old value, which is quick, and then renders again in the background with the new value. It's useful when the value comes from somewhere you don't control, like a prop, and you want a slow part of the UI to update after the fast part.

```jsx
const [query, setQuery] = useState("");
const deferredQuery = useDeferredValue(query);

<input value={query} onChange={(e) => setQuery(e.target.value)} />
<SlowResults query={deferredQuery} />
```

`SlowResults` should be wrapped in `memo` (or compiled) so it can skip the urgent render.

#### 80: What is the difference between `useTransition` and `useDeferredValue`?

Both mark work as non-urgent. Use `useTransition` when you control the state update and can wrap the `set` call. Use `useDeferredValue` when you only have the value, for example from props or from a hook you don't own. `useTransition` also gives you an `isPending` flag. With `useDeferredValue` you can compare `value !== deferredValue` to know if an update is pending.

#### 81: Can you use a transition for a controlled input?

No. Updates to a controlled input's value must be urgent, otherwise the input would lag behind typing. Keep the input's state update outside the transition, and put only the slow part (like filtering results) in a transition, or use `useDeferredValue` for the value that drives the slow part.

#### 82: What is `<Suspense>`?

`<Suspense>` shows a fallback, like a spinner or skeleton, while its children are not ready yet. Children "suspend" when they load lazy code with `lazy`, read a promise with `use`, or use a Suspense-enabled data library. Once everything inside is ready, React shows the real content.

```jsx
<Suspense fallback={<Spinner />}>
  <Comments />
</Suspense>
```

#### 83: Where should you put Suspense boundaries?

Put them around parts of the page that can load on their own and where showing a placeholder makes sense, like a sidebar, a comment section or a chart. One boundary around the whole app means the user sees a single spinner until everything is ready. Too many small boundaries can make content pop in piece by piece. Think about what the user should see first.

#### 84: What is a skeleton screen?

A skeleton is a placeholder that has the rough shape of the real content, like grey bars where the text will go. It's often used as a Suspense fallback. It feels faster than a spinner and, if it has the same size as the real content, it avoids layout shift when the content arrives.

#### 85: How does a transition change what Suspense shows?

If an update inside a transition causes already visible content to suspend, React keeps showing the old content instead of replacing it with the fallback. This avoids flashing spinners when the user switches tabs or pages. New Suspense boundaries that appear for the first time still show their fallback.

#### 86: What is `startTransition` without the hook used for?

The standalone `startTransition` imported from `react` works the same as the one from `useTransition`, but you don't get `isPending`. You can call it outside components, for example in a router or a store, where hooks are not allowed.

#### 87: What is the `<Activity>` component?

`<Activity>` was added in React 19.2. It lets you hide part of the UI without unmounting it. With `mode="hidden"` the children are hidden with `display: none`, their effects are cleaned up, and updates to them are given low priority. With `mode="visible"` they show again with their state kept. It's useful for tabs and for pre-rendering screens the user is likely to visit next.

```jsx
import { Activity } from "react";

<Activity mode={tab === "posts" ? "visible" : "hidden"}>
  <Posts />
</Activity>;
```

#### 88: What is the difference between hiding a component with `<Activity>` and with conditional rendering?

With `{show && <Panel />}`, hiding unmounts `Panel`, so its state and DOM are thrown away and showing it again starts from scratch. With `<Activity mode="hidden">`, the state and DOM are kept, so showing it again is instant. The cost is that hidden content still takes up memory, so don't keep too many large screens hidden.

#### 89: What is `useOptimistic`?

`useOptimistic` is a React 19 hook that shows a change in the UI immediately, before the server confirms it. When the action finishes, React switches to the real state. It makes the app feel faster for things like likes, sending messages or toggling a setting.

```jsx
const [optimisticLikes, addOptimisticLike] = useOptimistic(
  likes,
  (current, amount) => current + amount,
);

async function like() {
  addOptimisticLike(1);
  await saveLike();
}
```

`addOptimisticLike` has to be called inside an action or a transition, for example in a form `action` or inside `startTransition`.

#### 90: What is a long task and why does it matter for React?

A long task is any piece of work on the main thread that takes more than 50 ms. While it runs, the browser can't respond to input. A big synchronous React render is a long task. Concurrent features let React split rendering into small pieces and give control back to the browser between them, so the page stays responsive.

### Easy: Code Splitting and Bundle Size (91-105)

#### 91: Why does bundle size matter for React apps?

The browser has to download, parse and run all the JavaScript before your app becomes interactive. A big bundle means a slower first load, especially on phones and slow networks. Parsing and running JavaScript is also expensive on low-end CPUs, so a smaller bundle helps even when the network is fast.

#### 92: What is code splitting?

Code splitting breaks your app into several smaller JavaScript files (chunks) instead of one big bundle. The browser only loads the code needed for the current page, and other chunks load later when they are needed. Bundlers like Vite, webpack and the one in Next.js create a new chunk for every dynamic `import()`.

#### 93: What does `lazy` do?

`lazy` lets you load a component's code only when it is rendered for the first time. It takes a function that returns a dynamic `import()`. The component must be rendered inside a `<Suspense>` boundary, which shows a fallback while the code loads.

```jsx
import { lazy, Suspense } from "react";

const Settings = lazy(() => import("./Settings"));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Settings />
    </Suspense>
  );
}
```

#### 94: Where should you declare a `lazy` component?

At the top level of a module, outside any component. If you call `lazy` inside a component, a new lazy component is created on every render, so React remounts it and loses its state each time.

#### 95: What is route-based code splitting?

It means loading the code for each page (route) only when the user goes to that page. Routes are a natural split point because users only see one page at a time. Next.js and React Router's framework mode do this for you. In a plain setup you can use `lazy` for each route component.

#### 96: What is component-based code splitting?

It means lazy loading large components that aren't needed right away, even on the same page. Good candidates are modals, rich text editors, charts, maps and admin-only panels. The rest of the page loads fast and the heavy part loads when the user opens it.

#### 97: What is tree shaking?

Tree shaking is when the bundler removes code that is exported but never imported. It works with ES modules (`import` and `export`), because their imports can be analyzed at build time. It doesn't work well with CommonJS (`require`). Importing only what you need helps the bundler do this.

```js
// Lets the bundler drop unused functions
import { debounce } from "lodash-es";
```

#### 98: How can a single import make the bundle much larger?

Some libraries pull in a lot of code even when you use one function, for example importing the whole of `lodash`, a full icon library or all the locales of a date library. Check with a bundle analyzer, import from the specific path or package that supports tree shaking, and look for smaller alternatives.

#### 99: How do you check what is in your bundle?

Use a bundle analyzer. It shows a map of every module and how much space it takes. For Vite there is `rollup-plugin-visualizer`, for webpack there is `webpack-bundle-analyzer`, and for Next.js there is `@next/bundle-analyzer`. `source-map-explorer` works with any bundler that outputs source maps.

#### 100: What is minification?

Minification removes whitespace, comments and long names from your code, and makes other small changes to shrink it, without changing what it does. Production builds do it automatically with tools like esbuild, Terser or SWC. Together with compression (gzip or Brotli) on the server, it makes files much smaller to download.

#### 101: What is the difference between minification and compression?

Minification rewrites the code itself to be shorter. Compression (gzip or Brotli) is done by the server or CDN on the bytes it sends, and the browser decompresses them. You want both. Brotli usually gives smaller files than gzip for JavaScript and CSS.

#### 102: Why should you avoid large dependencies for small tasks?

A library adds its full size to your bundle, plus its own dependencies. Using a large date library to format one date, or a big utility library for one helper, costs users download and parse time on every visit. Check a package's size before adding it. Sites like bundlephobia show the cost, and often a few lines of your own code or a built-in browser API (`Intl.DateTimeFormat`, `structuredClone`) does the job.

#### 103: What is a vendor chunk?

A vendor chunk is a separate file that holds third-party code like React and other libraries. Since library code changes less often than your app code, the browser can keep the vendor chunk in cache across deploys. Most bundlers handle chunking on their own, so you only tune it if the analyzer shows a problem.

#### 104: How does long-term caching work with hashed file names?

Build tools add a content hash to file names, like `main.4f3a1c.js`. When the file changes, the name changes, so you can tell the browser to cache files for a very long time (for example `Cache-Control: public, max-age=31536000, immutable`). Users only download files that actually changed after a deploy.

#### 105: What is preloading a lazy component?

Preloading means starting the download of a lazy component before it's rendered, so it's ready when the user needs it. A common trick is to start the import when the user hovers over or focuses a button.

```jsx
const loadEditor = () => import("./Editor");
const Editor = lazy(loadEditor);

<button onMouseEnter={loadEditor} onClick={() => setOpen(true)}>
  Edit
</button>;
```

The browser caches the module, so the later `lazy` call reuses the same download.

### Easy: Server Rendering and Hydration (106-120)

#### 106: What is client-side rendering (CSR)?

With CSR, the server sends an almost empty HTML page and a JavaScript bundle. The browser downloads and runs the JavaScript, and React builds the whole page in the browser. It is simple to host, but the user sees nothing useful until the JavaScript has loaded and run, which hurts first load time and SEO.

#### 107: What is server-side rendering (SSR)?

With SSR, the server runs your React components and sends the finished HTML. The user sees the content quickly, before the JavaScript is ready. Then React loads in the browser and attaches event handlers to the existing HTML (hydration). SSR improves first paint and SEO but adds server work.

#### 108: What is hydration?

Hydration is when React in the browser takes over the HTML that came from the server. It renders the components again, matches them to the existing DOM, and attaches event handlers instead of creating new DOM nodes. Until hydration is done, buttons and inputs on the page don't respond to React handlers.

```jsx
import { hydrateRoot } from "react-dom/client";

hydrateRoot(document.getElementById("root"), <App />);
```

#### 109: What is a hydration mismatch?

A mismatch happens when the HTML rendered on the server is different from what React renders in the browser during hydration. Common causes are using `Date.now()`, `Math.random()`, `window` or `localStorage` while rendering, or invalid HTML nesting. React then has to fix the DOM or re-render that part on the client, which is slower and can cause flicker.

#### 110: What is static site generation (SSG)?

SSG renders pages to HTML at build time instead of on each request. The HTML files can be served from a CDN, which is very fast and cheap. It fits pages that are the same for every user and change rarely, like blogs, docs or marketing pages.

#### 111: What is the difference between SSR and SSG?

SSR renders HTML on every request, so it can show fresh, per-user data, but it needs a server and adds work per request. SSG renders once at build time, so it's faster to serve but the content is only as fresh as the last build. Frameworks like Next.js also offer options in between, like re-generating static pages after a set time.

#### 112: What are React Server Components?

Server Components are components that run only on the server (or at build time). Their code is never sent to the browser, so they don't add to the JavaScript bundle. They can read from a database or file system directly and pass the result to Client Components. They are used through frameworks like Next.js App Router.

#### 113: What does `"use client"` mean?

`"use client"` at the top of a file marks it as the boundary where the code starts running on the client. That component and everything it imports are sent to the browser. Components without it are Server Components by default in a framework that supports them. Keep `"use client"` as low in the tree as you can so less code is shipped.

#### 114: Why do Server Components help performance?

Their code and dependencies stay on the server, so a big markdown parser or date library used only in a Server Component adds nothing to the bundle. They can fetch data close to the database, so there are fewer round trips from the browser. The browser gets ready-made output and only hydrates the interactive Client Components.

#### 115: What is streaming SSR?

Streaming SSR sends HTML to the browser in chunks as it becomes ready, instead of waiting for the whole page. React sends the shell first, with Suspense fallbacks in place of slow parts, and then streams in the rest as their data loads. The user sees content sooner, and slow data doesn't block the whole page.

#### 116: What is selective hydration?

With selective hydration, React hydrates parts of the page wrapped in `<Suspense>` separately, as soon as their code and HTML are ready. If the user clicks on a part that isn't hydrated yet, React hydrates that part first. A slow component no longer blocks the rest of the page from becoming interactive.

#### 117: What is Time to First Byte (TTFB)?

TTFB is the time from the request until the first byte of the response reaches the browser. With SSR, slow data fetching on the server makes TTFB high, because the server can't send anything until it has the data. Streaming, caching and moving slow data behind Suspense boundaries help keep it low.

#### 118: What is `suppressHydrationWarning`?

It's a prop that tells React not to warn when the text content of that one element differs between server and client. It's meant for values that are expected to differ, like a timestamp. It only works one level deep and doesn't fix the mismatch, so use it rarely.

```jsx
<time suppressHydrationWarning>{new Date().toLocaleTimeString()}</time>
```

#### 119: How do you render something only on the client to avoid a hydration mismatch?

Render a placeholder on the server and on the first client render, then switch to the client-only content after hydration, in an effect.

```jsx
function ClientOnly({ children }) {
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);
  return mounted ? children : null;
}
```

This causes one extra render, so use it only for parts that really need browser APIs. In Next.js you can also use `next/dynamic` with `ssr: false` inside a Client Component.

#### 120: What is the "shell" in streaming SSR?

The shell is the part of the page outside all Suspense boundaries: usually the layout, header and navigation, plus the fallbacks. React sends it first. A good shell shows the page structure right away so the user knows something is happening, and it should not depend on slow data.

### Easy: Profiling and Measuring (121-135)

#### 121: Why should you measure before optimizing?

Because guesses are often wrong. The code that looks slow may not be, and adding `memo` or `useMemo` in the wrong place adds complexity for no gain. Profiling shows which components render, how often, and how long they take, so you fix the real problem and can confirm that the fix helped.

#### 122: What is React DevTools?

React DevTools is a browser extension for Chrome, Firefox and Edge (and a standalone app for React Native). It adds a Components tab, where you can look at the component tree, props, state and hooks, and a Profiler tab, where you can record renders and see how long each component took.

#### 123: How do you use the React DevTools Profiler?

Open the Profiler tab, click record, use the app, then stop. You get a list of commits (each time React updated the DOM). For each commit you can see a flame chart of which components rendered and how long they took, and a ranked chart sorted by time. Grey components didn't render in that commit.

#### 124: What does "Highlight updates when components render" do?

It's a setting in React DevTools that draws a colored border around components every time they render. It's a quick way to spot components that re-render when you don't expect them to, for example the whole page flashing when you type in one input.

#### 125: What does "Record why each component rendered while profiling" show?

When you turn this setting on in the Profiler, each component in a commit shows the reason it rendered: its props changed (and which ones), its state or hooks changed, its context changed, or its parent rendered. This makes it much easier to find the cause of an unwanted re-render.

#### 126: What is the `<Profiler>` component?

`<Profiler>` is a built-in component that measures rendering of its subtree from code. React calls `onRender` every time something inside commits.

```jsx
import { Profiler } from "react";

function onRender(id, phase, actualDuration, baseDuration) {
  console.log(id, phase, actualDuration, baseDuration);
}

<Profiler id="Sidebar" onRender={onRender}>
  <Sidebar />
</Profiler>;
```

Profiling is turned off in normal production builds. You need a profiling build to use it in production.

#### 127: What is the difference between `actualDuration` and `baseDuration`?

`actualDuration` is how long the render of the subtree took in this commit. If memoization worked, it can be small because many components were skipped. `baseDuration` is an estimate of how long it would take to render the whole subtree with no memoization. Comparing them tells you how much memoization saves.

#### 128: What is the Chrome DevTools Performance panel used for in React apps?

It records everything on the main thread: JavaScript, style, layout, paint and network. You can see long tasks, which functions take the most time, and whether the cost is in React rendering or in the browser's layout and paint. Since React 19.2, it also shows React's own tracks (Scheduler and Components) in the timeline when you use a development or profiling build.

#### 129: What are React Performance Tracks?

They are custom tracks that React 19.2 adds to the Chrome DevTools Performance panel. The Scheduler track shows React's work by priority (for example blocking work for user input versus transition work). The Components track shows which components rendered and how long their effects took. They help you see React's work next to network and browser activity in the same timeline.

#### 130: What are Core Web Vitals?

They are three Google metrics for user experience:

- **LCP (Largest Contentful Paint):** how fast the main content shows. Good is 2.5 seconds or less.
- **INP (Interaction to Next Paint):** how fast the page responds to clicks, taps and key presses. Good is 200 ms or less.
- **CLS (Cumulative Layout Shift):** how much the layout jumps around. Good is 0.1 or less.

React apps most often struggle with INP (slow renders after input) and LCP (big bundles, client rendering).

#### 131: How do you measure Web Vitals in a React app?

Use the `web-vitals` library and send the results to your analytics.

```js
import { onCLS, onINP, onLCP } from "web-vitals";

function send(metric) {
  navigator.sendBeacon("/analytics", JSON.stringify(metric));
}

onCLS(send);
onINP(send);
onLCP(send);
```

Next.js also has a `useReportWebVitals` hook. Field data from real users matters more than numbers from your own machine.

#### 132: What is Lighthouse?

Lighthouse is a tool built into Chrome DevTools (and available as a CLI) that loads a page in a controlled environment and gives scores for performance, accessibility, SEO and best practices. It lists problems like large JavaScript bundles, unused code and render-blocking resources. It's lab data, so it doesn't show interaction delays real users hit later in a session.

#### 133: What is the difference between lab data and field data?

Lab data comes from a test run in a controlled setup, like Lighthouse or a DevTools recording. It's repeatable and good for debugging. Field data comes from real users on real devices and networks, for example from the `web-vitals` library or the Chrome UX Report. Field data shows the real experience, including slow phones and long sessions.

#### 134: Why should you throttle the CPU when profiling?

Your development machine is probably much faster than an average user's phone. A render that takes 10 ms for you might take 50 ms or more on a cheap phone. Chrome DevTools lets you slow the CPU down (for example 4x or 6x) to get a more honest picture.

#### 135: What is React Scan?

React Scan is an open source tool that highlights components on the page as they re-render and shows which renders were unneeded. You can add it with a script tag or an npm package in development. It's a quick visual way to find re-render problems without opening the Profiler.

### Easy: Assets, Forms and Everyday Patterns (136-150)

#### 136: How do you lazy load images in React?

Use the native `loading="lazy"` attribute. The browser only downloads the image when it gets close to the viewport. Don't lazy load the main image at the top of the page, since that delays LCP.

```jsx
<img src="/photo.jpg" alt="Beach" width={800} height={600} loading="lazy" />
```

#### 137: Why should images have a width and height?

Without size information, the browser doesn't know how much space to reserve, so content jumps when the image loads. That's layout shift, which hurts CLS. Setting `width` and `height` (or a CSS `aspect-ratio`) lets the browser reserve the right space before the image arrives.

#### 138: What is `fetchPriority` and how do you use it in React?

`fetchPriority` tells the browser how important a resource is. Setting it to `"high"` on the LCP image makes the browser fetch it earlier. React 19 supports it as a prop.

```jsx
<img src="/hero.avif" alt="" fetchPriority="high" width={1200} height={600} />
```

#### 139: What image formats should you use for performance?

AVIF and WebP are much smaller than JPEG and PNG for the same quality, and modern browsers support them. Use SVG for icons and simple graphics. Serve the right size for the device with `srcset` and `sizes`, so phones don't download desktop-sized images. Frameworks like Next.js (`next/image`) do this automatically.

#### 140: What is the difference between controlled and uncontrolled inputs?

A controlled input gets its value from React state and updates state on every change, so the component re-renders on every keystroke. An uncontrolled input keeps its own value in the DOM, and you read it when needed, for example on submit with `FormData` or a ref. For large forms, uncontrolled inputs or a library like React Hook Form avoid re-rendering the whole form on each keystroke.

#### 141: How do React 19 form actions help with performance?

You can pass a function to a form's `action` prop. React reads the values with `FormData` when the form is submitted, so you don't need state for every field. `useActionState` and `useFormStatus` handle pending and result states without extra code.

```jsx
function Signup() {
  async function signup(formData) {
    await createUser(formData.get("email"));
  }
  return (
    <form action={signup}>
      <input name="email" type="email" />
      <button type="submit">Sign up</button>
    </form>
  );
}
```

#### 142: Why can CSS-in-JS libraries that work at runtime slow down an app?

Libraries that generate styles at runtime have to create and insert CSS while rendering. That adds JavaScript work to every render and can cause the browser to recalculate styles often. They also add their own code to the bundle. Static CSS (CSS Modules, Tailwind CSS, or CSS-in-JS libraries that extract CSS at build time) avoids this cost.

#### 143: Why are inline styles sometimes a performance concern?

`style={{ ... }}` creates a new object on every render, which breaks `memo` on children that receive it. Many inline styles also make the HTML bigger with SSR. For styles that don't change, use classes. For values that change often, like a position during drag, inline styles or CSS variables are fine.

#### 144: How do you avoid memory leaks in React components?

Clean up everything an effect starts: event listeners, intervals, timeouts, subscriptions, WebSocket connections and observers. Abort fetch requests that are no longer needed. Don't keep references to DOM nodes or large objects in module-level variables that outlive the component.

```jsx
useEffect(() => {
  function onResize() {
    setWidth(window.innerWidth);
  }
  window.addEventListener("resize", onResize);
  return () => window.removeEventListener("resize", onResize);
}, []);
```

#### 145: Why should you avoid animating with React state on every frame?

Updating state 60 times a second re-renders the component (and maybe its children) 60 times a second. That uses a lot of CPU and can drop frames. CSS transitions and animations, or libraries that update the DOM directly (like Motion), avoid going through React for each frame. Animate `transform` and `opacity`, which the browser can handle without layout.

#### 146: What is the cost of rendering icons as React components?

Each SVG icon component adds nodes to the DOM and code to the bundle. Importing a whole icon set instead of single icons can add hundreds of kilobytes. Import icons one by one so tree shaking works, and for many repeated icons consider an SVG sprite with `<use>`.

#### 147: How do Portals affect performance?

A portal (`createPortal`) renders children into a different DOM node, like `document.body` for a modal. It doesn't make rendering faster or slower by itself. The portal's content is still part of the React tree, so it re-renders with its parent and gets context as usual. The main benefit is avoiding CSS problems with `overflow` and `z-index`.

#### 148: Why should you avoid heavy work in event handlers?

The handler runs on the main thread. If a click handler does a lot of work before React can render the result, the user waits and INP gets worse. Show feedback first (for example set a loading state), then do the heavy work in a transition, after yielding to the browser, or in a Web Worker.

#### 149: What is a Web Worker and when would a React app use one?

A Web Worker runs JavaScript on a separate thread, so heavy work doesn't block the UI. React can't render inside a worker, but you can move expensive calculations there, like parsing a big file, image processing or complex filtering, and send the result back to the component.

```js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
worker.postMessage(bigData);
worker.onmessage = (e) => setResult(e.data);
```

#### 150: What are the most common causes of a slow React app?

- Big JavaScript bundles with no code splitting.
- State placed too high, causing large parts of the tree to re-render.
- Context values that change often or get a new object every render.
- Long lists without virtualization.
- Slow calculations during render without caching.
- Data fetching waterfalls.
- Unoptimized images and layout shifts.
- Measuring in development mode and missing the real problems.

## Moderate Questions (151-300)

### Moderate: Rendering and Re-renders (151-165)

#### 151: How does passing components as `children` prevent re-renders?

When a component renders `{children}`, the `children` elements were created by its parent, not by itself. If the component's own state changes, React re-renders it, but the `children` element objects are the same as before, so React skips them. This is a simple way to keep a heavy subtree from re-rendering when a wrapper's state changes.

```jsx
function ScrollTracker({ children }) {
  const [scrollY, setScrollY] = useState(0);
  // ...update scrollY on scroll
  return (
    <div>
      <ProgressBar value={scrollY} />
      {children}
    </div>
  );
}

<ScrollTracker>
  <Article /> {/* does not re-render when scrollY changes */}
</ScrollTracker>;
```

#### 152: Why does React skip re-rendering an element if it is the same object as last time?

During reconciliation, if the new element is exactly the same object as the old one (same reference), React knows nothing about it could have changed and skips that subtree. This is what makes the `children` pattern and memoized JSX work. If you create the element with JSX again, it's a new object, even if it looks the same.

#### 153: What happens when you conditionally render different component types in the same position?

If the type at a given position changes, React unmounts the old subtree and mounts the new one, losing state and DOM. If the same type stays at the same position, React keeps it, even across branches of a condition. Sometimes this is what you want, sometimes it causes stale state, and the fix in both cases is a `key`.

```jsx
// Same type, same position: state is kept when isAdmin changes
{
  isAdmin ? <Form role="admin" /> : <Form role="user" />;
}

// Different keys: state is reset
{
  isAdmin ? <Form key="admin" /> : <Form key="user" />;
}
```

#### 154: How can you find out why a component re-rendered?

In React DevTools turn on "Record why each component rendered while profiling", record an interaction and click the component in the flame chart. It shows which props, hooks or context changed. You can also turn on "Highlight updates" to see renders on the page, or use React Scan. For a quick check in code, log in the component body or compare previous props with a ref.

#### 155: What is the difference between a re-render and a remount?

A re-render calls the component function again but keeps its state, refs and DOM. A remount destroys the component, runs effect cleanups, throws away state and DOM, then creates everything again from scratch and runs effects again. Remounts are much more expensive. They happen when the key or the component type changes at a position.

#### 156: How do fragments affect rendering performance?

Fragments (`<>...</>`) let you return several elements without adding an extra DOM node. Fewer wrapper `<div>`s means a smaller DOM and less layout work. They don't change how React reconciles children. If you need a key on a fragment in a list, use `<Fragment key={id}>`.

#### 157: Is it bad to return a large JSX tree from one component?

Not by itself. The cost of a render depends on how much work happens, not on file size. But a large component usually holds a lot of state, so any state change re-renders all of it. Splitting it into smaller components, each with its own state, limits how much re-renders on each change and makes memoization easier to apply.

#### 158: How does `flushSync` affect performance?

`flushSync` from `react-dom` forces React to apply an update right away and synchronously, instead of batching it. It's sometimes needed, for example to read the updated DOM right after a state change or to integrate with a third-party library. But it turns off batching and can't be interrupted, so calling it often makes updates slower.

```jsx
import { flushSync } from "react-dom";

flushSync(() => setItems([...items, newItem]));
listRef.current.lastChild.scrollIntoView();
```

#### 159: Why can a `useLayoutEffect` that sets state hurt performance?

Setting state inside `useLayoutEffect` triggers a second render that runs synchronously before the browser paints. So the user waits for two renders and two commits before seeing anything. It's acceptable for things like positioning a tooltip based on its measured size, but doing it for data that doesn't need measuring just delays the paint.

#### 160: How do you stop a parent's re-render from re-rendering a heavy child, without `memo`?

Several options:

- Move the state that changes into a smaller component, so the parent doesn't re-render at all.
- Pass the heavy child as `children` or another prop from above the component with the state.
- Let the React Compiler handle it.

These are often cleaner than `memo` because they change the structure instead of adding a comparison.

#### 161: What are the costs of very deep component trees?

Each component adds work: calling the function, running hooks and reconciling its children. Deep trees from many wrapper components (providers, higher-order components, layout wrappers) add up, especially when a change near the top re-renders everything. They also make DevTools harder to read. Flattening providers and removing wrappers that don't do anything helps.

#### 162: What is "render props" and how does it affect performance?

A render prop is a function prop that returns JSX, like `<DataLoader render={(data) => <List data={data} />} />`. Because the function is usually inline, it's a new reference each render, which breaks `memo` on the component that takes it. Today, custom hooks cover most render prop uses with less nesting.

#### 163: How do higher-order components (HOCs) affect performance?

An HOC wraps a component in another component, adding a layer to the tree for each HOC. Several HOCs stack up layers and can pass new props on every render, which breaks memoization below. A common mistake is calling an HOC inside render, which creates a new component type each time and remounts the child. HOCs are now mostly replaced by hooks.

#### 164: When would you use `key` to reset state instead of an effect?

When a component should start fresh for a new item, for example a form for a different user. Resetting state in an effect means rendering once with old state, then again with reset state. Changing the `key` makes React remount the component with fresh state in a single render.

```jsx
// Avoid
useEffect(() => {
  setComment("");
}, [userId]);

// Prefer
<CommentForm key={userId} userId={userId} />;
```

#### 165: How do you adjust state when a prop changes without an effect?

If you really need to, you can compare with the previous value during render and set state right away. React re-runs the component immediately before rendering children, which is cheaper than an effect that runs after commit.

```jsx
function List({ items }) {
  const [selection, setSelection] = useState(null);
  const [prevItems, setPrevItems] = useState(items);

  if (items !== prevItems) {
    setPrevItems(items);
    setSelection(null);
  }
  // ...
}
```

Usually it's even better to avoid it, for example by storing the selected id and checking whether it still exists in `items`.

### Moderate: Memoization and the React Compiler (166-180)

#### 166: When is `useMemo` worth it for a calculation?

When the calculation is noticeably slow, usually 1 ms or more, or when you need a stable reference for a memoized child or an effect. You can time it with `console.time` around the calculation, ideally with a slowed-down CPU. Cheap things like adding two numbers or mapping a few items are not worth memoizing by hand.

```jsx
console.time("filter");
const visible = filterTodos(todos, tab);
console.timeEnd("filter");
```

#### 167: Why does `memo` not help when you pass `children`?

JSX passed as `children` is a new element object on every parent render, so a `memo` component that receives `children` always sees a changed prop. If you need the memo to work, memoize the children too, or restructure so the memoized component doesn't take JSX that changes every time.

```jsx
const Card = memo(function Card({ children }) {
  return <div className="card">{children}</div>;
});

// Card re-renders every time, because <p> is a new element
<Card>
  <p>Hello</p>
</Card>;
```

#### 168: How do you write a custom comparison function for `memo`?

Pass a second argument, `arePropsEqual(oldProps, newProps)`, that returns `true` if the component can skip rendering. It must compare every prop that matters, including functions. Missing one causes bugs where the component shows stale data, and a deep comparison can be slower than just rendering.

```jsx
const Chart = memo(
  function Chart({ points, color }) {
    /* ... */
  },
  (prev, next) =>
    prev.color === next.color &&
    prev.points.length === next.points.length &&
    prev.points.every((p, i) => p === next.points[i]),
);
```

#### 169: What does the React Compiler actually memoize?

It memoizes values, JSX elements and callbacks inside components and hooks, based on which inputs they depend on. Unlike `useMemo`, it can memoize parts of the JSX separately and even code after an early return. The compiled component reuses cached JSX for parts whose inputs didn't change, so React skips those subtrees. It doesn't memoize plain functions outside components and hooks.

#### 170: How does the React Compiler know which functions to compile?

By default (`compilationMode: 'infer'`) it compiles functions that look like components or hooks: names starting with a capital letter that return JSX, or names starting with `use` that call hooks. You can switch to `compilationMode: 'annotation'` to compile only functions marked with `"use memo"`, which helps with a gradual rollout.

```js
["babel-plugin-react-compiler", { compilationMode: "annotation" }];
```

```jsx
function Dashboard() {
  "use memo";
  // ...
}
```

#### 171: What happens when the React Compiler finds code that breaks the Rules of React?

It skips that component or hook and leaves it as it was, without failing the build. The rest of the app still gets compiled. The ESLint rules in `eslint-plugin-react-hooks` report these cases so you can fix them, for example writing to a ref during render or mutating a prop.

#### 172: How do you roll out the React Compiler in an existing app?

Fix ESLint errors from the compiler rules first. Then enable it for part of the code: through `compilationMode: 'annotation'`, or by limiting the Babel plugin to certain folders in your build config. Test the main flows and watch for bugs where something stops updating. Use `"use no memo"` to opt out components that break, and widen the scope step by step. Have good tests before you start.

#### 173: Can you use the React Compiler with React 17 or 18?

Yes. Set the compiler's `target` option to `'17'` or `'18'` and install `react-compiler-runtime`, which provides the cache hook the compiled code needs. React 19 has it built in.

```js
["babel-plugin-react-compiler", { target: "18" }];
```

#### 174: How can you check that the React Compiler optimized a component?

In React DevTools, compiled components show a "Memo ✨" badge next to their name. You can also look at the compiled output in your build or in the React Compiler Playground, where you'll see calls to a cache from `react/compiler-runtime`. The ESLint rules tell you about components that couldn't be compiled.

#### 175: Why should you not write to or read from `ref.current` during render?

Refs are mutable, and React doesn't know when they change, so reading them in render can show stale values and makes the output depend on something outside props and state. That breaks purity, and the React Compiler can't safely memoize such code. Read and write refs in event handlers and effects. The one accepted exception is lazy initialization: `if (ref.current === null) ref.current = new Thing()`.

#### 176: What is the problem with `useCallback` when the callback depends on frequently changing state?

If the state is in the dependency list, a new function is created every time the state changes, so memoized children still re-render. Use a functional state update to drop the dependency, or for callbacks used inside effects, use `useEffectEvent`.

```jsx
// New function on every text change
const onSubmit = useCallback(() => send(text), [text]);
```

#### 177: Why might `memo` not stop re-renders of a component that uses context?

`memo` only compares props. If the component reads a context with `useContext` or `use`, it still re-renders when that context value changes, no matter what. To limit this, split the context, pass the needed value as a prop from a parent that reads the context, or use a store with selectors.

#### 178: Does `useMemo` guarantee that the value is never recalculated?

No. The React docs treat `useMemo` as a performance hint, not a guarantee. React may throw away the cache in some cases, for example in development when you edit a file, or when a component suspends during its first mount. Your code must work correctly even if the value is recalculated. If you need something stored for sure, use state or a ref.

#### 179: How does the React Compiler work with existing `useMemo` and `useCallback` calls?

It keeps them and checks that its own memoization matches them. If it can't preserve the memoization you wrote, for example because the dependency list is wrong, it may skip that component to be safe and report it through the linter. You can remove them over time, but test first, especially where a value is used as an effect dependency.

#### 180: Is memoizing a component that renders very little worth it?

Usually not. If a component renders a few elements and has cheap props, the prop comparison costs about as much as the render. Memoize components that are expensive to render, that render often, or that sit high in a tree so skipping them skips a lot of children.

### Moderate: State and Context (181-195)

#### 181: How do you split a context into state and dispatch to reduce re-renders?

Put the state in one context and the `dispatch` (or setter functions) in another. Components that only trigger actions, like buttons, read the dispatch context, which never changes, so they don't re-render when the state changes.

```jsx
const TodosContext = createContext(null);
const TodosDispatchContext = createContext(null);

function TodosProvider({ children }) {
  const [todos, dispatch] = useReducer(todosReducer, []);
  return (
    <TodosContext value={todos}>
      <TodosDispatchContext value={dispatch}>{children}</TodosDispatchContext>
    </TodosContext>
  );
}
```

#### 182: How do you avoid re-renders when only part of a context value is needed?

React has no built-in context selectors. Options:

- Split the context into smaller ones.
- Read the context in a parent and pass only the needed field to a `memo` child as a prop.
- Use a library like `use-context-selector`.
- Move that state to a store with selectors (Zustand, Redux Toolkit, Jotai), and use context only to pass the store, which never changes.

#### 183: Why is a Zustand or Redux store often faster than Context for shared state?

These stores live outside React and components subscribe with selectors. When the store updates, each subscriber runs its selector and only re-renders if the selected value changed. With Context, every consumer re-renders when the value changes. For state that changes often and is read in many places, that makes a big difference.

#### 184: What is the problem with selectors that return new objects?

If a selector returns a new object or array every time, like `state => ({ a: state.a, b: state.b })`, the result is never equal to the last one, so the component re-renders on every store update. Select single values, use a shallow compare helper, or memoize the selector.

```jsx
// Zustand
import { useShallow } from "zustand/react/shallow";
const { a, b } = useStore(useShallow((s) => ({ a: s.a, b: s.b })));

// Redux
import { shallowEqual, useSelector } from "react-redux";
const { a, b } = useSelector((s) => ({ a: s.a, b: s.b }), shallowEqual);
```

#### 185: What is a memoized selector and when do you need one?

A memoized selector, like one made with Reselect's `createSelector` (included in Redux Toolkit), caches its output and only recalculates when its inputs change. You need it when the selector does real work, like filtering or sorting, or returns a derived array. Without it, the work runs and a new array is returned on every store update, causing re-renders.

```js
import { createSelector } from "@reduxjs/toolkit";

const selectDoneTodos = createSelector([(state) => state.todos], (todos) =>
  todos.filter((t) => t.done),
);
```

#### 186: How do you share state between distant components without re-rendering everything in between?

Use context or a store, so the middle components don't hold the state and don't re-render. Make sure the provider is placed so that its own re-renders don't affect much, and that only the components that read the value re-render. Passing JSX through `children` also lets a component near the top hold state without re-rendering the components passed in.

#### 187: What is `useSyncExternalStore` and why does it matter for performance?

It's the hook for subscribing to a store outside React, like a browser API or a state library. It makes sure all components see the same value during a concurrent render (no tearing) and re-renders only when the snapshot changes.

```jsx
function subscribe(callback) {
  window.addEventListener("online", callback);
  window.addEventListener("offline", callback);
  return () => {
    window.removeEventListener("online", callback);
    window.removeEventListener("offline", callback);
  };
}

function useOnlineStatus() {
  return useSyncExternalStore(
    subscribe,
    () => navigator.onLine,
    () => true,
  );
}
```

`getSnapshot` must return the same value if nothing changed, or React re-renders forever. Define `subscribe` outside the component so it isn't recreated.

#### 188: How should you store server data versus UI state?

Keep server data (lists, user profiles, anything from an API) in a cache like TanStack Query, SWR or the framework's data layer. Keep UI state (which modal is open, form input, selected tab) in local state or a small store. Mixing them, for example copying API data into Redux by hand, leads to duplicated data, manual cache invalidation and more re-renders than needed.

#### 189: How does storing form input in global state affect performance?

Every keystroke updates the global store, which notifies every subscriber and may re-render many components that have nothing to do with the form. Keep form input local to the form, or use a form library that doesn't re-render on every change. Only put the final values into global state when you need them elsewhere.

#### 190: What is the problem with putting everything in one big `useState` object?

When any field changes, you create a new object, and everything that reads the object re-renders, even if it only cares about another field. It also makes `memo` and dependency lists less precise. Use several `useState` calls for unrelated values, or `useReducer` for related ones, and pass only the fields each child needs.

#### 191: How do atomic state libraries like Jotai help with performance?

They split state into small independent pieces called atoms. A component subscribes only to the atoms it reads, and derived atoms recalculate only when their inputs change. Updating one atom re-renders only the components that use it, without selectors or splitting contexts by hand.

#### 192: How do you store state in the URL without slowing the app down?

URL state (search params) is good for filters and pagination because it can be shared and survives a reload. But updating it on every keystroke means a navigation and a re-render of the route each time. Debounce the update, or keep the input in local state and push to the URL after a pause. Some routers also let you update the URL without re-running data loaders.

#### 193: How do you avoid passing many props that change often to deep children?

Group what changes often and what doesn't. Pass stable values, like ids and setters, down the tree, and let deep children read the changing data themselves from a store with a selector. That way, only the leaves that need the changing data re-render, not every component on the path.

#### 194: What is "state colocation"?

It means keeping state in the component closest to where it's used, and moving it up only when needed. Colocated state limits re-renders to a small subtree and makes code easier to follow. When a feature is removed, its state goes with it instead of being left in a global store.

#### 195: What is the cost of putting a big object in state and updating it immutably?

Each update copies the parts of the object along the path to the changed field. For a few levels of nesting that's cheap. For very large objects or arrays updated often, copying can add up, and every component reading the object re-renders. Normalize the data, split it into smaller pieces, or use Immer, which only copies what changes and keeps everything else shared.

```js
import { produce } from "immer";

setState((s) =>
  produce(s, (draft) => {
    draft.users[id].name = newName;
  }),
);
```

### Moderate: Lists and Large Data (196-210)

#### 196: How do you virtualize a list with TanStack Virtual?

You give `useVirtualizer` the number of items, the scroll container and an estimated row size. It returns the rows to render and the total height. Each row is positioned with a `transform`.

```jsx
import { useRef } from "react";
import { useVirtualizer } from "@tanstack/react-virtual";

function BigList({ items }) {
  const parentRef = useRef(null);
  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 40,
    overscan: 5,
  });

  return (
    <div ref={parentRef} style={{ height: 500, overflow: "auto" }}>
      <div style={{ height: virtualizer.getTotalSize(), position: "relative" }}>
        {virtualizer.getVirtualItems().map((row) => (
          <div
            key={row.key}
            style={{
              position: "absolute",
              top: 0,
              left: 0,
              width: "100%",
              height: row.size,
              transform: `translateY(${row.start}px)`,
            }}
          >
            {items[row.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

#### 197: How do you virtualize rows with different heights?

Give an estimated size and let the library measure the real size after rendering. In TanStack Virtual, you pass `virtualizer.measureElement` as the row's `ref` and set `data-index` on it. The library then updates positions as rows are measured. Don't set a fixed height on the row in that case.

```jsx
<div
  key={row.key}
  data-index={row.index}
  ref={virtualizer.measureElement}
  style={{
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    transform: `translateY(${row.start}px)`,
  }}
>
  <Message message={messages[row.index]} />
</div>
```

#### 198: What is overscan in virtualization?

Overscan is the number of extra rows rendered above and below the visible area. A few extra rows hide blank gaps when the user scrolls fast. Too many and you lose the benefit of virtualization. A value between 3 and 10 is common.

#### 199: What are the downsides of virtualization?

- The browser's find-in-page (Ctrl+F) can't find rows that aren't rendered.
- Screen readers only see the rendered rows, so you may need ARIA attributes like `aria-rowcount` and `aria-rowindex`.
- Rows with unknown heights can make the scrollbar jump.
- Scroll restoration, sticky headers and "scroll to item" need extra work.
- Rows lose their local state when they scroll out, since they unmount.

#### 200: How do you keep row state when rows scroll out of a virtualized list?

Rows unmount when they leave the window, so local state is lost. Lift state that must survive (like an expanded flag or a draft input) out of the row into the parent, keyed by item id, or into a store. The row then reads its state by id when it mounts again.

#### 201: How do you make a fast client-side search over thousands of items?

- Keep the input state urgent and the results update deferred (with `useDeferredValue`), so typing stays smooth.
- Memoize the filtering so it only runs when the query or data changes.
- Precompute a lowercase search field once, instead of lowercasing every item on every keystroke.
- Virtualize the results.
- For very large data sets, use a search index library or move filtering to a Web Worker.

```jsx
const deferredQuery = useDeferredValue(query);
const results = useMemo(
  () => items.filter((i) => i.searchText.includes(deferredQuery.toLowerCase())),
  [items, deferredQuery],
);
```

#### 202: How do you avoid re-rendering every row when the selection changes?

If every row receives `selectedId`, every row re-renders when it changes. Instead, pass a boolean like `isSelected={item.id === selectedId}`. With memoized rows, only the row that was selected and the one that becomes selected get a different prop, so only two rows re-render.

```jsx
{
  items.map((item) => (
    <Row
      key={item.id}
      item={item}
      isSelected={item.id === selectedId}
      onSelect={setSelectedId}
    />
  ));
}
```

#### 203: How do you handle a list that receives frequent real-time updates?

Batch incoming messages and apply them in one state update every so often (for example every 100 ms or once per animation frame) instead of on every message. Store items by id so you only replace changed items, keep rows memoized, and virtualize the list. If updates are not urgent, apply them in a transition.

#### 204: What is the cost of sorting inside a render in a table with many columns?

A sort with a custom comparator on thousands of rows can take several milliseconds, and if it runs on every render (like each time you hover a row), the table feels slow. Memoize the sorted rows based on data and sort settings, use a stable compare function, and for huge data sort on the server or in a worker.

#### 205: How does TanStack Table help with large tables?

TanStack Table is headless, so it gives you the logic (sorting, filtering, grouping, pagination, column visibility) and you write the markup. Its row models are memoized, so they only recalculate when the related state changes. It doesn't virtualize by itself, so for large tables you combine it with TanStack Virtual.

#### 206: When should you do filtering and pagination on the server instead of the client?

When the full data set is large (tens of thousands of rows or more), when it takes long to download, or when users only ever look at a small part. Sending everything to the client wastes bandwidth and memory and makes the first load slow. Server-side pagination with cursor or offset parameters, plus caching of pages, scales better.

#### 207: How do you make infinite scroll with TanStack Query?

`useInfiniteQuery` loads pages and keeps them together. You tell it how to find the next page, and call `fetchNextPage` when the user gets near the end.

```jsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery({
    queryKey: ["posts"],
    queryFn: ({ pageParam }) =>
      fetch(`/api/posts?cursor=${pageParam}`).then((r) => r.json()),
    initialPageParam: 0,
    getNextPageParam: (lastPage) => lastPage.nextCursor,
  });

const posts = data?.pages.flatMap((p) => p.items) ?? [];
```

Trigger `fetchNextPage` from an `IntersectionObserver` or from the virtualizer when the last rendered row is near the end.

#### 208: How do you render a grid of thousands of images efficiently?

Virtualize rows of the grid, lazy load images with `loading="lazy"`, give each image a fixed size or aspect ratio to avoid layout shift, and serve thumbnails instead of full-size files. Use `decoding="async"` so decoding doesn't block the main thread. Memoize the cell component so scrolling doesn't re-render visible cells.

#### 209: What is "time slicing" for big lists, and how do you do it in React?

Time slicing means splitting a big render into small pieces so the browser can handle input between them. React does this automatically for updates inside a transition, since concurrent rendering yields to the browser every few milliseconds. Before concurrent React, people rendered lists in chunks with `requestIdleCallback` or `setTimeout`. With transitions, that's rarely needed.

#### 210: How do you show a large tree (like a file explorer) efficiently?

Only render expanded nodes, and keep expanded state by node id outside the nodes. For very large trees, flatten the visible nodes into one list (with depth for indentation) and virtualize that list. Memoize nodes so toggling one folder doesn't re-render the whole tree. Load children lazily from the server when a folder is opened.

### Moderate: Effects and Data Fetching (211-225)

#### 211: What is `useEffectEvent` and how does it help?

`useEffectEvent`, added in React 19.2, creates an "effect event": a function that always sees the latest props and state, but isn't a dependency of the effect. This lets you read a value inside an effect without making the effect re-run when that value changes.

```jsx
import { useEffect, useEffectEvent } from "react";

function ChatRoom({ roomId, theme }) {
  const onConnected = useEffectEvent(() => {
    showNotification("Connected!", theme);
  });

  useEffect(() => {
    const connection = createConnection(roomId);
    connection.on("connected", () => onConnected());
    connection.connect();
    return () => connection.disconnect();
  }, [roomId]); // theme changes don't reconnect
}
```

Only call effect events from inside effects, and don't pass them to other components.

#### 212: How do you fetch data in parallel instead of in a waterfall?

Start all independent requests before awaiting any of them. On the server or in a loader, use `Promise.all`. In components, fetch in a common parent or route loader instead of in each child, or use a data library that starts requests as soon as the hooks run.

```js
// Waterfall
const user = await getUser(id);
const posts = await getPosts(id);

// Parallel
const [user, posts] = await Promise.all([getUser(id), getPosts(id)]);
```

#### 213: What is "fetch on render" vs "render as you fetch"?

In "fetch on render", the component starts fetching after it renders, usually in an effect, so nested components create waterfalls. In "render as you fetch", requests start as early as possible, for example in a route loader or an event handler, and components read the data (with `use` or a Suspense-ready library) and suspend until it arrives. The second approach starts the network work sooner.

#### 214: How do you prefetch data before the user needs it?

Start the request on a hint of intent, like hovering a link, focusing a button or when a page becomes visible. TanStack Query has `queryClient.prefetchQuery`, routers often prefetch route data on link hover, and Next.js prefetches routes when links come into view.

```jsx
<Link
  to={`/users/${id}`}
  onMouseEnter={() =>
    queryClient.prefetchQuery({
      queryKey: ["user", id],
      queryFn: () => fetchUser(id),
    })
  }
>
  {name}
</Link>
```

#### 215: What is `staleTime` in TanStack Query and why does it matter?

`staleTime` is how long data is considered fresh. While data is fresh, components that mount with the same query key use the cache without making a request. The default is 0, so data is stale right away and gets refetched in the background on mount, on window focus and on reconnect. Setting a sensible `staleTime` for data that doesn't change often removes a lot of extra requests.

#### 216: What is stale-while-revalidate?

It's a caching strategy where you show cached (possibly old) data right away and fetch fresh data in the background. When the new data arrives, the UI updates. Users see content immediately instead of a spinner. SWR is named after it, and TanStack Query works the same way by default.

#### 217: How do you avoid a loading spinner flash on fast requests?

If the request is quick, showing a spinner for 50 ms looks like a flicker. Options: keep showing old content during the update with a transition or `placeholderData: keepPreviousData` in TanStack Query, show the spinner only after a short delay, or use Suspense with transitions so React keeps the old UI until the new one is ready.

#### 218: How do Server Actions or form actions reduce client code?

The data mutation runs on the server and the client only calls it. You don't need a separate API route, a fetch call, loading state and error handling code in the client bundle. With frameworks that support it, the server can also send the updated UI back in the same round trip, so you don't need a second request to refetch data.

#### 219: Why should you avoid chaining effects that set state?

When one effect sets state that triggers another effect, which sets more state, each step adds a render and a commit. The user may see in-between states, and the logic is hard to follow. Compute what you can during render, and do all the related updates together in the event handler that caused them.

#### 220: How does `cache` from React help in Server Components?

`cache` wraps a function so that calls with the same arguments during a single server request return the same result. Several Server Components can call `getUser(id)` and only one database query runs. The cache is reset for each request.

```js
import { cache } from "react";

export const getUser = cache(async (id) => {
  return db.user.findUnique({ where: { id } });
});
```

`cache` only works in Server Components. On the client, use a data library.

#### 221: How do you handle data that many components need, without fetching it many times?

Use a shared cache keyed by what you're fetching, so the first call fetches and the others reuse the result. TanStack Query, SWR, RTK Query and Apollo all dedupe requests with the same key. In Server Components, `cache` or the framework's fetch caching does the same job. Avoid separate `useEffect` fetches in each component.

#### 222: What is the cost of refetching on window focus?

Libraries like TanStack Query refetch stale queries when the browser tab gets focus again. It keeps data fresh but can cause bursts of requests and re-renders every time the user switches tabs. For data that rarely changes, raise `staleTime` or turn off `refetchOnWindowFocus` for those queries.

#### 223: How do you optimize polling in React?

Poll only when it's needed: stop when the tab is hidden (check `document.visibilityState`), back off when nothing changes, and stop when the component unmounts. Data libraries have options for this, like `refetchInterval` and `refetchIntervalInBackground: false` in TanStack Query. For data that changes often, WebSockets or server-sent events are usually cheaper than polling.

#### 224: How do you avoid a re-render storm from a WebSocket?

Don't call `setState` for every message. Collect messages in a ref or buffer and flush them in one update on a timer or `requestAnimationFrame`. Put the data in a store so only components that read the changed part re-render. Make sure the socket is opened once (not in every component) and closed in cleanup.

#### 225: Why does StrictMode make effects run twice, and should you work around it?

In development, StrictMode mounts, unmounts and mounts again to check that cleanup works. If your effect breaks when run twice, it means it would also break in other cases, like fast navigation or `<Activity>` hiding and showing it. Fix the cleanup instead of turning off StrictMode. Duplicate fetches in development are fine if you abort or ignore the first one. It doesn't happen in production.

### Moderate: Concurrent Features and Suspense (226-240)

#### 226: How do you use a transition to keep a tab switch responsive?

Wrap the state update that switches the tab in `startTransition`. If the new tab is slow to render, the user can still click other tabs, and React drops the unfinished render and starts the new one. `isPending` lets you show that something is happening on the old tab.

```jsx
function Tabs() {
  const [tab, setTab] = useState("about");
  const [isPending, startTransition] = useTransition();

  function selectTab(next) {
    startTransition(() => setTab(next));
  }

  return (
    <>
      <TabButtons current={tab} onSelect={selectTab} />
      <div style={{ opacity: isPending ? 0.6 : 1 }}>
        {tab === "posts" ? <SlowPosts /> : <About />}
      </div>
    </>
  );
}
```

#### 227: Can you use async functions inside `startTransition`?

Yes, since React 19. You can pass an async function, and `isPending` stays `true` until it finishes. State updates made after an `await` need their own `startTransition` call to be marked as a transition, since React can't keep track of the context across `await` yet.

```jsx
startTransition(async () => {
  const data = await saveName(name);
  startTransition(() => {
    setResult(data);
  });
});
```

#### 228: Why doesn't `useDeferredValue` help if the slow component isn't memoized?

With `useDeferredValue`, React first renders with the old deferred value, which only helps if the slow part can skip that render. If `SlowList` isn't wrapped in `memo` (or compiled), it re-renders anyway because its parent did, so the urgent render is still slow. The memoization is what makes the first render fast.

#### 229: What does the `initialValue` argument of `useDeferredValue` do?

Since React 19, you can pass a second argument: `useDeferredValue(value, initialValue)`. On the first render, React returns `initialValue` and then renders again in the background with the real `value`. It's useful to show something cheap first, like an empty list, and render the expensive version right after.

```jsx
const deferredQuery = useDeferredValue(query, "");
```

#### 230: How do Suspense and transitions work together when navigating?

Wrap the navigation state update in a transition. If the new page suspends while loading data or code, React keeps showing the current page instead of replacing it with a fallback. Most routers that support Suspense, like React Router and Next.js, wrap navigations in transitions for you. Add a pending indicator so users know the click registered.

#### 231: What does it mean that Suspense boundaries "reveal together"?

All components inside one Suspense boundary are shown at the same time, when all of them are ready. If you want parts to appear separately, give each its own boundary. If you want them to appear together to avoid a jumpy layout, keep them under one boundary.

```jsx
<Suspense fallback={<PageSkeleton />}>
  <Header />
  <Suspense fallback={<FeedSkeleton />}>
    <Feed />
  </Suspense>
</Suspense>
```

#### 232: How do you keep old content visible during a search instead of showing a fallback?

Use `useDeferredValue` on the query. The results component receives the deferred value. While the new results load, React keeps showing the old ones, because the deferred render happens in the background. You can dim the old results when `query !== deferredQuery`.

```jsx
const deferredQuery = useDeferredValue(query);
const isStale = query !== deferredQuery;

<Suspense fallback={<Spinner />}>
  <div style={{ opacity: isStale ? 0.5 : 1 }}>
    <SearchResults query={deferredQuery} />
  </div>
</Suspense>;
```

#### 233: What is tearing and how does React prevent it?

Tearing is when different parts of the screen show different versions of the same data during one render. It can happen in concurrent rendering if an external store changes while React is in the middle of a render that it paused. `useSyncExternalStore` prevents this by checking the store before committing and re-rendering synchronously if it changed.

#### 234: How should you use `<Activity>` to make tab switches faster?

Wrap each tab in `<Activity>` and switch the `mode` instead of unmounting. Hidden tabs keep their state and DOM, so switching back is instant and doesn't refetch data. You can also render the next tab hidden ahead of time so its code and data load in the background.

```jsx
<>
  <Activity mode={tab === "home" ? "visible" : "hidden"}>
    <Home />
  </Activity>
  <Activity mode={tab === "videos" ? "visible" : "hidden"}>
    <Videos />
  </Activity>
</>
```

#### 235: What happens to effects inside a hidden `<Activity>`?

When the `Activity` becomes hidden, React runs the cleanups of the effects inside it, so subscriptions and timers stop. When it becomes visible again, the effects run again. The state is kept. Updates to hidden content are rendered at low priority. This means effects need correct cleanup, the same as for StrictMode.

#### 236: When should you not use a transition?

Don't use it for updates that must be shown right away, like a controlled input's value, a checkbox the user just clicked, or anything where a delay would feel broken. Transitions are for updates where showing the old UI for a bit longer is fine, like switching screens, filtering results or loading the next page.

#### 237: How does Suspense with `lazy` and data fetching combine?

A boundary waits for both code and data. If a lazy component's code is still loading and its data is also loading, the fallback stays until both are ready. To avoid waiting for the code first and then the data, start both early: preload the module and start the data request at the same time, for example in a route loader.

#### 238: How do you avoid a "popcorn" effect where many parts load in one by one?

Group related parts under one Suspense boundary so they appear together. Use nested boundaries only where it makes sense to show something earlier, like the main content before the sidebar. Since React 19, when something suspends, React commits the fallback right away and then pre-renders the siblings, and with streaming SSR React 19.2 batches reveals of boundaries that are ready close together.

#### 239: What are error boundaries and how do they relate to performance?

An error boundary catches errors during rendering in its subtree and shows a fallback instead of crashing the whole app. It doesn't make things faster, but placing boundaries around independent sections, together with Suspense boundaries, means one broken or slow widget doesn't take down the page. There's no hook for it yet, so you write a class component or use `react-error-boundary`.

#### 240: How does React decide which update to handle first?

Each update gets a priority, called a lane. Updates from discrete user events like clicks and key presses get the highest priority and are rendered synchronously. Continuous events like scroll or mouse move get a slightly lower priority. Transitions and deferred values get lower priorities, and hidden `<Activity>` content gets the lowest. React always works on the highest priority pending work first and can interrupt lower priority renders.

### Moderate: Code Splitting and Bundle Size (241-255)

#### 241: How do you lazy load a named export?

`lazy` expects a module with a default export. For a named export, map it in the import function.

```jsx
const Chart = lazy(() =>
  import("./charts").then((module) => ({ default: module.LineChart })),
);
```

#### 242: How do you handle errors when a lazy chunk fails to load?

Chunk loading can fail because of the network or because a new deploy removed old files. Wrap lazy parts in an error boundary that shows a retry button. A common fix for the deploy case is to reload the page once when a chunk load error happens, so the browser gets the new file names.

```jsx
<ErrorBoundary
  fallback={
    <p>
      Could not load. <button onClick={() => location.reload()}>Retry</button>
    </p>
  }
>
  <Suspense fallback={<Spinner />}>
    <Settings />
  </Suspense>
</ErrorBoundary>
```

#### 243: How do you code split with `next/dynamic` in Next.js?

`next/dynamic` works like `lazy` plus Suspense, with an option for a loading component. In a Client Component you can also pass `ssr: false` to skip server rendering for components that need browser APIs.

```jsx
"use client";
import dynamic from "next/dynamic";

const Map = dynamic(() => import("./Map"), {
  ssr: false,
  loading: () => <p>Loading map...</p>,
});
```

#### 244: What is the problem with too much code splitting?

Each chunk is a separate request with its own overhead. If you split into many tiny chunks, the browser may need many round trips, especially when chunks depend on each other (a chunk waterfall). The user also waits for a chunk every time they open something. Split at meaningful points like routes and heavy features, and preload chunks the user is likely to need.

#### 245: What does the `sideEffects` field in `package.json` do?

It tells the bundler whether importing a module can have side effects. If a library sets `"sideEffects": false`, the bundler can safely drop whole files that you import but don't use. If files do have side effects, like CSS imports or polyfills, they must be listed so they aren't removed.

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js"]
}
```

#### 246: Why do barrel files sometimes make bundles bigger or builds slower?

A barrel file is an `index.js` that re-exports everything from a folder. Importing one item from it can make the bundler load and process the whole folder, and if any module has side effects, tree shaking can't remove the rest. In development it also slows down the server, since many modules load for each import. Import from the specific file, or use framework options that rewrite barrel imports, like `optimizePackageImports` in Next.js.

#### 247: How do you find and remove unused code from a React app?

Use the Coverage tab in Chrome DevTools to see how much of each loaded file actually runs on a page. Use a bundle analyzer to find large modules. Tools like Knip find unused files, exports and dependencies. Remove dead features, replace heavy libraries, and lazy load code that only some users need.

#### 248: How do you keep polyfills from making the bundle bigger for modern browsers?

Set a browserslist that matches the browsers you actually support, so the build tool only adds the polyfills and syntax changes needed for them. Old targets add a lot of code. Some setups build a modern bundle and a legacy bundle and serve the right one, but if you only support modern browsers, a single modern build is simpler.

#### 249: How do you load a heavy library only when needed?

Use a dynamic `import()` inside the event handler or effect that needs it. The library becomes its own chunk and only loads when the code runs.

```jsx
async function exportPdf() {
  const { jsPDF } = await import("jspdf");
  const doc = new jsPDF();
  doc.text("Report", 10, 10);
  doc.save("report.pdf");
}
```

#### 250: What is the difference between `preload` and `prefetch` for chunks?

`preload` loads a resource with high priority because the current page needs it soon. `prefetch` loads a resource with low priority during idle time because a future page might need it. Use preload for the current route's critical chunks and prefetch for routes the user is likely to visit next. Next.js prefetches routes for links automatically.

#### 251: What resource loading APIs does React 19 add?

`react-dom` exports functions you can call while rendering or in event handlers to tell the browser about resources early:

- `prefetchDNS(href)` and `preconnect(href)` for origins you'll use soon.
- `preload(href, { as })` for fonts, images, stylesheets and scripts.
- `preinit(href, { as })` to load and run a script or insert a stylesheet.
- `preloadModule` and `preinitModule` for ES modules.

```jsx
import { preconnect, preload } from "react-dom";

function App() {
  preconnect("https://api.example.com");
  preload("/fonts/inter.woff2", {
    as: "font",
    type: "font/woff2",
    crossOrigin: "",
  });
  return <Main />;
}
```

React dedupes the calls and, during SSR, puts the hints in the HTML `<head>`.

#### 252: How do you reduce the size of icon and date libraries?

For icons, import single icons from packages that support tree shaking (like `lucide-react`), not a full set. For dates, use `date-fns` with direct imports, or a small library like Day.js, or the built-in `Intl` APIs. For locales, load only the ones you need, and load them lazily if there are many.

#### 253: How do Server Components reduce bundle size compared to code splitting?

Code splitting still sends the code to the browser, just later. Server Components never send their code. If a component renders markdown with a large library, as a Server Component the library stays on the server and the browser only gets the result. So Server Components remove code from the client, while code splitting only delays it.

#### 254: Why is it important to check bundle size in CI?

Bundle size tends to grow slowly with every new dependency, and nobody notices until the app is slow. A CI check that fails or warns when a bundle grows past a limit catches the problem in the pull request that caused it. Tools like `size-limit` or bundle reports from your build tool can do this.

#### 255: What is the cost of shipping source maps to production?

Source maps don't affect users, because the browser only downloads them when DevTools is open. The cost is that your original source becomes easy to read for anyone. Many teams upload source maps to their error tracking service (like Sentry) and don't serve them publicly, so they can read stack traces without exposing the code.

### Moderate: Server Rendering and Hydration (256-270)

#### 256: How do you stream HTML with `renderToPipeableStream` in Node.js?

`renderToPipeableStream` renders the app to a Node stream. You start piping in `onShellReady`, so the browser gets the shell right away and the Suspense content streams in later.

```jsx
import { renderToPipeableStream } from "react-dom/server";

app.get("/", (req, res) => {
  const { pipe, abort } = renderToPipeableStream(<App />, {
    bootstrapScripts: ["/main.js"],
    onShellReady() {
      res.setHeader("Content-Type", "text/html");
      pipe(res);
    },
    onShellError() {
      res.statusCode = 500;
      res.send("<h1>Something went wrong</h1>");
    },
  });
  setTimeout(abort, 10000);
});
```

For crawlers that need the full page, you can wait for `onAllReady` instead. In environments with Web Streams (Deno, edge runtimes, and Node.js too), use `renderToReadableStream`.

#### 257: Why should you avoid `renderToString` for new SSR code?

`renderToString` waits for the whole page and returns it as one string. It can't stream, and it doesn't support waiting for data inside Suspense: suspended parts are sent as their fallback and then rendered on the client. Slow data blocks the whole response. The streaming APIs send the shell early and stream the rest, which gives a faster first paint.

#### 258: How do you reduce the cost of hydration?

- Send less JavaScript: use Server Components so non-interactive parts don't hydrate.
- Wrap independent parts in `<Suspense>` so they hydrate separately and in order of user interaction.
- Avoid hydration mismatches, which force React to re-render parts on the client.
- Lazy load components that aren't visible at first.
- Keep the initial render cheap, since hydration runs your components again.

#### 259: What does a hydration mismatch cost in React 19?

If text content differs, React logs one error with a diff of the mismatch. When the mismatch can't be patched, React throws away the server HTML up to the nearest Suspense boundary and renders that part from scratch on the client. That costs more CPU, can cause flicker and wastes the work the server did. You can catch them in production with `onRecoverableError` on `hydrateRoot`.

```jsx
hydrateRoot(document.getElementById("root"), <App />, {
  onRecoverableError(error) {
    reportToMonitoring(error);
  },
});
```

#### 260: How do you render dates and times without hydration mismatches?

The server and the browser may have different time zones and locales, so formatting a date can give different text. Options: format with a fixed time zone and locale on both sides, send the formatted string from the server, or render the local time only on the client after hydration. Avoid `new Date()` during render for "now", since the time passes between server and client.

#### 261: What is the cost of passing large props from Server Components to Client Components?

Props passed to Client Components are serialized into the RSC payload, which is sent to the browser and kept in memory. Passing a full database record when the client needs two fields, or a huge list, makes the payload and the HTML bigger. Pass only what the Client Component uses.

```jsx
// Avoid
<UserMenu user={fullUserRecord} />

// Prefer
<UserMenu name={user.name} avatarUrl={user.avatarUrl} />
```

#### 262: How do you keep `"use client"` boundaries small?

Put the client directive on the small interactive part, not on the whole page. For example, a product page can be a Server Component that renders a `"use client"` `AddToCartButton`. You can also pass Server Components as `children` to a Client Component, so a client wrapper like a modal or tabs doesn't pull its content into the client bundle.

```jsx
// Server Component
<ClientTabs>
  <ServerRenderedContent />
</ClientTabs>
```

#### 263: How do you stream data from a Server Component without blocking the page?

Wrap the slow component in `<Suspense>`. The rest of the page is sent first, and the slow part streams in when its data is ready. You can also start a promise in a Server Component and pass it to a Client Component, which reads it with `use`.

```jsx
export default function Page() {
  const reviewsPromise = getReviews();
  return (
    <>
      <ProductDetails />
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews reviewsPromise={reviewsPromise} />
      </Suspense>
    </>
  );
}
```

#### 264: What is partial pre-rendering?

Partial pre-rendering means building the static part of a page ahead of time (at build time or once) and filling in the dynamic parts per request. React 19.2 added APIs for it: `prerender` from `react-dom/static` creates the static shell and a `postponed` state, and `resume` (or `resumeAndPrerender`) continues rendering the postponed dynamic parts later. Frameworks like Next.js build features on top of this. The static shell can be served from a CDN, so the first bytes arrive very fast.

#### 265: How do you cache SSR output?

Cache full pages at the CDN when they're the same for everyone, using `Cache-Control` headers like `s-maxage` and `stale-while-revalidate`. For pages with some per-user content, cache the shared parts (or the data) and render the personalized parts on each request or on the client. Frameworks like Next.js have their own caching layers for data and rendered output. Be careful not to cache pages with private data at a shared cache.

#### 266: How does where you run SSR affect performance?

Rendering close to the user (edge) cuts network latency for the HTML. But if the data lives in one region, every database call from the edge has to travel far, which can make the page slower overall. Render near the data when the page needs many data calls, or cache data at the edge. Measure TTFB from different regions.

#### 267: How do you avoid sending the same data twice with SSR?

With classic SSR, the data is used to render the HTML and also sent as JSON so the client can hydrate, which doubles the payload. Send only the data hydration needs. With Server Components, data used only on the server isn't sent again, only props passed to Client Components are. With data libraries, use their dehydrate and hydrate helpers so the client cache starts filled and doesn't refetch.

#### 268: What should go in the shell to improve perceived performance?

The layout, navigation, page title, and anything the user needs to orient themselves, plus skeletons for content that's still loading. Keep slow data out of the shell. A shell that depends on a slow call delays the whole page. Include the CSS needed for the shell so it renders styled.

#### 269: How do you hydrate only part of a page?

React hydrates whatever root you give it, so you can call `hydrateRoot` on several separate DOM nodes, one per interactive widget, and leave the rest of the page as static HTML. This "islands" approach is what frameworks like Astro use. With Server Components in Next.js, you get something similar, since only Client Components hydrate.

#### 270: How do `onCaughtError` and `onUncaughtError` help in production?

React 19 added these options to `createRoot` and `hydrateRoot`. `onCaughtError` runs when an error boundary catches an error, and `onUncaughtError` runs when an error isn't caught. Together with `onRecoverableError`, they let you send all render errors to your monitoring tool, including hydration problems that slow down the page.

### Moderate: Profiling and Measuring (271-285)

#### 271: How do you read the flame chart in the React Profiler?

Each bar is a component. Width shows how long the component and its children took to render in that commit. Color shows how long the component itself took: yellow is slow, blue and green are fast, and grey means it didn't render in this commit. Click a bar to see why it rendered and its render times across commits.

#### 272: What does the ranked chart in the React Profiler show?

It lists the components that rendered in the selected commit, sorted by how long they took themselves, with the slowest at the top. It's the fastest way to find the single most expensive component in a commit.

#### 273: How do you profile a React app in production?

The normal production build has profiling turned off. Use the profiling build, which keeps the timing code with a small cost. With a bundler, alias `react-dom/client` to `react-dom/profiling`.

```js
// vite.config.js
export default {
  resolve: {
    alias: {
      "react-dom/client": "react-dom/profiling",
    },
  },
};
```

Then you can use the DevTools Profiler, `<Profiler>`, and React's tracks in Chrome on a build that is close to what users run. Next.js has a `--profile` flag for `next build`.

#### 274: How do you find what is causing a slow interaction (bad INP)?

Record the interaction in the Chrome Performance panel with CPU throttling. Look at the interaction in the Interactions track and split its time into input delay (main thread busy before the handler), processing time (your handlers and React render), and presentation delay (layout, paint). Then look at the flame chart under it to see which functions or React components take the time.

#### 275: What are the three parts of INP and how do they map to React?

- **Input delay:** something else is running when the user interacts, like a big render, hydration or a third-party script.
- **Processing time:** your event handlers and the React render and commit they cause.
- **Presentation delay:** the browser's style, layout and paint after React updates the DOM, which grows with large DOM changes.

Transitions help with processing time, smaller DOM changes help presentation delay, and breaking up long tasks helps input delay.

#### 276: How do you use `<Profiler>` to send render timings to analytics?

Wrap a part of the app and send `onRender` data, but sample it and batch it so the reporting doesn't slow the app down. Remember that in a normal production build `onRender` isn't called, so this needs a profiling build.

```jsx
function onRender(id, phase, actualDuration) {
  if (actualDuration > 16 && Math.random() < 0.1) {
    queueMetric({ id, phase, actualDuration });
  }
}
```

#### 277: How do you add your own marks to the Chrome performance timeline?

Use the User Timing API: `performance.mark` and `performance.measure`. They show up in the Timings track, so you can see how long your own code takes next to React's tracks.

```js
performance.mark("filter-start");
const result = filterProducts(products, query);
performance.mark("filter-end");
performance.measure("filter products", "filter-start", "filter-end");
```

Chrome also supports adding a `detail.devtools` object to these calls to put entries on custom tracks.

#### 278: Why might a component look slow in the Profiler but not be the real problem?

The Profiler shows render time in development mode, which is slower than production because of extra checks. StrictMode and DevTools itself also add overhead. A component can also look slow because it renders many cheap children. Confirm with a profiling or production build, and check whether the time is in the component itself ("self" time) or in its children.

#### 279: How do you detect unnecessary renders automatically?

React DevTools highlighting and React Scan show them visually. In tests, you can count renders with `<Profiler>`'s `onRender` or with a mock, and assert that an action renders only the expected components. That catches regressions where a change starts re-rendering a large list on every keystroke.

#### 280: How do you measure the time it takes to load a lazy component?

Use the Network panel to see when the chunk is requested and how long it takes. In code, you can wrap the import with timing.

```jsx
const Editor = lazy(async () => {
  const start = performance.now();
  const module = await import("./Editor");
  reportMetric("editor-chunk-ms", performance.now() - start);
  return module;
});
```

#### 281: How do you find memory leaks in a React app?

Take a heap snapshot in Chrome DevTools Memory panel, do the action (open and close a page) several times, take another snapshot and compare. Look for "Detached" DOM nodes and growing counts of your objects. The usual causes are listeners, timers and subscriptions that were never cleaned up, and caches that keep growing.

#### 282: How do you check for layout shift caused by React rendering?

In the Chrome Performance panel, the Layout shifts track shows each shift and the elements that moved. The `web-vitals` library with the attribution build tells you the element that caused the largest shift. In React apps, shifts usually come from images without size, content loading into an empty area, fonts swapping, and banners inserted at the top.

#### 283: What does the Coverage tab show and how does it help a React app?

It shows how many bytes of each JavaScript and CSS file were actually used during the recording. A large unused share in the main bundle on the first page means you're shipping code that isn't needed yet, which is a sign to code split or remove it.

#### 284: How do you compare performance before and after a change?

Use the same conditions: production or profiling build, the same CPU throttling, the same data and the same steps. Record several runs since numbers vary. Compare the specific metric you care about, like render time of a component, INP for a click, or LCP. Tools like Lighthouse CI or custom performance tests in CI help keep it repeatable.

#### 285: How does the React DevTools "Timeline" view differ from the flame chart?

The Timeline (in newer DevTools versions when profiling React 18+) shows React's work over time: when updates were scheduled, which lane they used, when renders and commits ran, and when components suspended. It helps you understand ordering and priority, while the flame chart focuses on how long each component took in one commit.

### Moderate: Assets, Forms and Everyday Patterns (286-300)

#### 286: How do you optimize a large form in React?

- Use uncontrolled inputs and read values with `FormData`, or a library like React Hook Form that doesn't re-render the form on each keystroke.
- Split the form into sections with their own state.
- Validate on blur or submit instead of on every key press, or debounce validation.
- Memoize heavy field components.

```jsx
import { useForm } from "react-hook-form";

function Profile() {
  const { register, handleSubmit } = useForm();
  return (
    <form onSubmit={handleSubmit(save)}>
      <input {...register("firstName")} />
      <input {...register("lastName")} />
      <button type="submit">Save</button>
    </form>
  );
}
```

#### 287: How does `useActionState` help with form performance?

It holds the result and pending state of a form action, so you don't need separate `useState` calls for loading, error and data. With frameworks that support it, it also works before the JavaScript loads, because the form can submit as a normal HTML form.

```jsx
import { useActionState } from "react";

function NewsletterForm() {
  const [state, formAction, isPending] = useActionState(subscribe, null);
  return (
    <form action={formAction}>
      <input name="email" />
      <button disabled={isPending}>Subscribe</button>
      {state?.error && <p>{state.error}</p>}
    </form>
  );
}
```

#### 288: How do you load fonts without hurting performance?

Self-host the fonts, use WOFF2, subset them to the characters you need and preload the main font. Set `font-display: swap` or `optional` so text shows right away. Use fallback font metric overrides (`size-adjust`, `ascent-override`) to reduce layout shift when the font swaps. Next.js `next/font` does most of this for you.

#### 289: How do you render stylesheets in React 19 so they load in the right order?

React 19 lets you render `<link rel="stylesheet">` with a `precedence` prop anywhere in the tree. React moves it to the `<head>`, dedupes it, and orders stylesheets by precedence. During streaming SSR or a client transition, React waits for the stylesheet before showing the content that needs it, which avoids a flash of unstyled content.

```jsx
<link rel="stylesheet" href="/widget.css" precedence="default" />
```

#### 290: How do you optimize drag and drop in React?

Don't update React state for every pointer move. Move the dragged element with CSS `transform` directly on the DOM node (through a ref) or with a library that does this, and update React state only on drop. Memoize list items so the rest of the list doesn't re-render while dragging. Libraries like dnd kit are built to avoid unneeded renders.

#### 291: How do you make an expensive tooltip or popover cheap?

Don't mount the popover's content until it's opened. Share one popover instance for many triggers instead of one per row. Use CSS for simple hover effects. Position it with a lightweight library, and avoid measuring layout on every scroll. For tables with many rows, attach one delegated event handler instead of many.

#### 292: How do you handle scroll events without slowing down the app?

Use `IntersectionObserver` when you only need to know if something is visible. For scroll position, throttle updates with `requestAnimationFrame`, keep the value in a ref if it doesn't need to render, and register the listener as passive. For scroll-linked visuals, CSS scroll-driven animations avoid JavaScript entirely in browsers that support them.

```jsx
useEffect(() => {
  let frame = 0;
  function onScroll() {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => setScrolled(window.scrollY > 100));
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  return () => {
    cancelAnimationFrame(frame);
    window.removeEventListener("scroll", onScroll);
  };
}, []);
```

Since `setScrolled` gets a boolean, React bails out when it doesn't change.

#### 293: How do you use a Web Worker from a React component cleanly?

Create the worker in an effect (or once, outside the component), send it messages, put the result into state, and terminate it in cleanup. Libraries like Comlink let you call worker functions as if they were async functions.

```jsx
useEffect(() => {
  const worker = new Worker(new URL("./parse.worker.js", import.meta.url), {
    type: "module",
  });
  worker.onmessage = (e) => setRows(e.data);
  worker.postMessage(fileText);
  return () => worker.terminate();
}, [fileText]);
```

#### 294: How do third-party scripts affect a React app?

Analytics, chat widgets, ads and tag managers run on the same main thread, so they can delay hydration and make interactions slow. Load them with `async` or `defer`, after the page is interactive, or only when needed (for example the chat widget on click). In Next.js, `next/script` with `strategy="lazyOnload"` helps. Audit them regularly, since they're often the biggest cost on the page.

#### 295: How do you avoid layout shift when content loads in React?

Reserve space for content before it arrives: set sizes on images and embeds, give skeletons the same size as the final content, and don't insert banners above existing content. If something must appear on top, overlay it instead of pushing content down. With Suspense, make the fallback match the size of the loaded content.

#### 296: How do you optimize animations in React?

Animate `transform` and `opacity` only, so the browser doesn't need layout or paint. Use CSS transitions or the Web Animations API for simple cases, and libraries that animate outside React's render cycle for complex ones. Use `will-change` sparingly. For enter and exit animations of lists, avoid measuring every item on every frame.

#### 297: How do you show many charts on a dashboard without freezing the page?

Lazy load the chart library, render charts only when they scroll into view, and render them in a transition so the rest of the page responds first. Downsample data, since a chart rarely needs more points than it has pixels. Choose canvas-based charts for very large data sets, since SVG creates a DOM node per point.

#### 298: How does `useId` relate to performance?

`useId` generates stable unique ids that are the same on the server and client, which avoids hydration mismatches you'd get with random ids or counters. It doesn't change render speed, but it avoids the client re-render a mismatch causes. Don't use it for list keys.

#### 299: What are ref callbacks with cleanup in React 19, and how do they help?

Since React 19, a ref callback can return a cleanup function. React calls it when the element is removed. This makes it easy to attach observers or listeners to a DOM node and clean them up without a separate effect.

```jsx
<div
  ref={(node) => {
    const observer = new ResizeObserver(() => onResize(node));
    observer.observe(node);
    return () => observer.disconnect();
  }}
/>
```

If the callback is an inline function, React runs cleanup and the callback again after every render, so wrap it in `useCallback` (or rely on the compiler) when that's costly.

#### 300: How is optimizing a React Native app different from optimizing a React web app?

React Native apps don't have a DOM, so things like layout shift and bundle download work differently, but the React side is the same: re-renders, memoization, list virtualization (`FlatList`, FlashList) and heavy work on the JS thread. The New Architecture removes the old bridge, and the React Compiler works there too. Tools are React Native DevTools and native profilers (Xcode Instruments, Android Studio) for frame drops.

## Advanced Questions (301-450)

### Advanced: Rendering and Re-renders (301-315)

#### 301: What is a Fiber?

A Fiber is React's internal object for one unit of work, usually one component or DOM element. It holds the type, props, state, hooks list, effects and pointers to its parent (`return`), first child (`child`) and next sibling (`sibling`). Because the tree is a linked list of fibers, React can stop after any fiber and continue later, which is what makes interruptible rendering possible.

#### 302: What is double buffering in React's fiber tree?

React keeps two trees: the `current` tree, which matches what's on screen, and the work-in-progress tree, which it builds during a render. Each fiber points to its counterpart through `alternate`. When the render is done, React commits and swaps the pointer so the work-in-progress tree becomes current. Reusing alternates avoids allocating new fibers on every render.

#### 303: How does React bail out of rendering a subtree?

When React reaches a fiber during render, it checks whether the props object is the same as before, whether there's pending work on that fiber, and whether context it depends on changed. If nothing changed, it skips calling the component. If the children also have no pending work (tracked with `childLanes`), it skips the whole subtree and reuses the existing fibers. This is why the same element reference, `memo` and compiled JSX skip work.

#### 304: What is the "eager state" optimization and when does it apply?

When you call `setState` and the fiber has no other pending updates, React can calculate the new state right away, before scheduling a render. If the new state is equal to the current one (`Object.is`), React doesn't schedule a render at all. If there are pending updates, React can't know the result yet, so it schedules a render and may bail out later, after calling the component once. That's why you sometimes see one extra render even when setting the same value.

#### 305: How does React update a DOM element when its props change?

For host elements like `<div>` or `<input>`, React compares the old and new props and only touches the attributes, styles and properties that changed. Event handlers are not attached to each DOM node. Since React 17, React listens for events once at the root and calls your handler from there, so passing a new `onClick` function each render doesn't touch the DOM at all. The expensive part is usually the number of elements that change and the layout work the browser does afterwards, not React's diffing.

#### 306: How does the React work loop yield to the browser?

In concurrent mode, React's work loop processes one fiber at a time and checks `shouldYield()` between fibers. The Scheduler gives React a time slice of about 5 ms. When it runs out, React stops, schedules the rest with `MessageChannel`, and lets the browser handle input and paint. Synchronous updates (like those from a click) use a loop without yielding.

#### 307: What are lanes and how do they replace the old expiration times?

Lanes are bits in a 31-bit number. Each update is given a lane depending on its priority: sync, input continuous, default, transition lanes, retry lanes, idle and offscreen. React can group lanes with bitwise operations, render several at once, and track which lanes are pending on each fiber. Compared to the old single expiration time per update, lanes make it possible to batch related transitions and process them independently from urgent work.

#### 308: What is starvation in concurrent rendering, and how does React handle it?

If urgent updates keep coming, a low-priority transition might never finish. React tracks how long each lane has been waiting and marks it as expired after a timeout. Expired lanes are then rendered synchronously without yielding, so they finish even if the user keeps typing.

#### 309: Why can a component render without committing?

In concurrent rendering, React may start rendering an update and then throw away the result because a higher-priority update came in, because a component suspended, or because a newer transition replaced the old one. In StrictMode, the second render is also thrown away. So a component function being called doesn't mean anything changed on screen. That's why side effects in render are dangerous.

#### 310: How do you debug a component that re-renders in an infinite loop?

Look for `setState` called directly during render without a condition, an effect that sets state it also depends on, or a dependency that is a new object every render. React stops with "Too many re-renders" for render loops, and with "Maximum update depth exceeded" for effect loops. Use the Profiler or a log with the changed values to find which dependency changes each time, then compute it during render, memoize it or move it inside the effect.

#### 311: What is the cost of very large props objects or spreading props through many layers?

Spreading `{...props}` passes every prop down, including ones that change often and ones the child doesn't use. Any of them changing breaks memoization below. Very large props objects also make custom comparisons expensive. Pass only what each component needs, and keep stable values separate from changing ones.

#### 312: How does React handle a component returning the same JSX structure but with different keys at the root?

If the root element's `key` changes, React treats it as a different element: it unmounts the old subtree with all its state and DOM and mounts a new one. This is useful for resetting, but if a key is accidentally computed from changing data (like a timestamp or index after sorting), the component remounts on every render, which is very expensive and loses focus and scroll position.

#### 313: What is "render-phase update" and why does React warn about updating another component during render?

Setting your own state during render is allowed for adjusting state based on props, and React re-runs the component right away. Setting state of a different component during render is not allowed, because it causes that component to update in the middle of rendering a different one, which can lead to inconsistent UI and wasted renders. React warns "Cannot update a component while rendering a different component". Move that update into an effect or handler.

#### 314: How does `memo` interact with `ref` props in React 19?

In React 19, `ref` is a regular prop for function components, so `memo` compares it like any other prop. A stable ref object from `useRef` doesn't break memoization, but an inline callback ref is a new function each render and makes the memo component re-render. Use a stable callback ref with `useCallback`, or a ref object.

#### 315: A page is slow only after the user has been on it for a while. What would you check?

This usually points to something growing over time:

- memory leaks from listeners, timers or subscriptions that weren't cleaned up,
- lists or caches that keep growing (chat messages, logs, infinite scroll without virtualization),
- more and more subscribers to a store or event emitter,
- intervals that were started twice.

Take heap snapshots over time, check the number of DOM nodes and event listeners in the Performance monitor, and record a Profiler session after a long session to see if renders got slower.

### Advanced: Memoization and the React Compiler (316-330)

#### 316: What does the output of the React Compiler look like?

The compiler adds a cache array to each component using a hook from `react/compiler-runtime`. It then checks whether each input has changed before recomputing each value or JSX block.

```jsx
// Input
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}

// Roughly what the compiler outputs
import { c as _c } from "react/compiler-runtime";
function Greeting(t0) {
  const $ = _c(2);
  const { name } = t0;
  let t1;
  if ($[0] !== name) {
    t1 = <h1>Hello, {name}</h1>;
    $[0] = name;
    $[1] = t1;
  } else {
    t1 = $[1];
  }
  return t1;
}
```

Since the JSX object is the same when `name` doesn't change, React bails out of rendering the `<h1>` subtree.

#### 317: How is the compiler's memoization different from `useMemo`?

`useMemo` caches one value with a dependency list you write by hand. The compiler analyzes the data flow and creates many small cache slots, one per group of values that change together, with dependencies it finds itself. It can memoize after conditionals and early returns, where you can't call hooks, and it doesn't miss dependencies. It also only compares the inputs that each block actually reads.

#### 318: Why does the React Compiler need code to follow the Rules of React to be correct?

The compiler assumes that if the inputs are the same, the output is the same, and that values are not mutated after they're created. If a component mutates a prop, reads a global that changes, or writes to a ref during render, cached output might be reused when it shouldn't be, and the UI stops updating. The compiler tries to detect these cases and skip such code, but it can't catch everything, which is why linting and tests matter.

#### 319: What kinds of bugs can show up after enabling the React Compiler?

- UI not updating because code mutated an object or array instead of creating a new one.
- Effects running a different number of times, because a dependency that used to be a new object every render is now stable (or the other way around).
- Code that relied on a value being recomputed each render, like reading `Date.now()` or a mutable global in render.
- Third-party libraries that return mutable objects from hooks, which the compiler then treats as unchanged.

Most of these are bugs in the original code that the compiler exposes.

#### 320: How do you handle a third-party hook that returns a mutable object with the React Compiler?

If a library returns the same object and mutates it, the compiler sees the same reference and reuses cached JSX, so the component doesn't update. Options: update the library (many fixed this for compiler support), read the specific primitive values from the object instead of passing the object, or opt that component out with `"use no memo"`. Libraries that use `useSyncExternalStore` with immutable snapshots work fine.

#### 321: Does the React Compiler make `memo` around components unnecessary?

Mostly. Because the compiler memoizes the JSX in the parent, a child element that receives the same props is the same object, so React skips it without `memo`. The child itself is also compiled. `memo` can still be useful for components that aren't compiled (for example in an uncompiled library) or when the parent is not compiled.

#### 322: How does memoization interact with Context in compiled code?

Context reads are not skipped by memoization. When a context value changes, every component that reads it re-renders, compiled or not. Inside that component, the compiler's cache still helps: only the parts that use the changed value are recomputed, and children that don't depend on it get the same JSX and are skipped. So the cost of a context change becomes smaller but doesn't go away.

#### 323: How do you measure whether the React Compiler improved performance?

Profile key interactions before and after with a production profiling build, using the same data and CPU throttling. Compare commit durations, number of components rendered per interaction, and INP in the field. Also check the bundle, since compiled code is a bit larger. Teams that rolled it out usually saw faster interactions in some screens and little change in screens that were already fast or were dominated by network or layout costs.

#### 324: What is the cost of memoization itself?

Each cached value takes memory for as long as the component is mounted, and each render has to compare dependencies. For components that render once or whose inputs change every time, memoization adds work without saving any. Comparing large arrays with a custom deep comparison can cost more than rendering. Over-memoizing by hand also makes code harder to read and dependency lists easy to get wrong.

#### 325: How would you memoize an expensive function across components, not only within one?

`useMemo` is per component instance. For sharing across components, cache outside React: a module-level `Map` keyed by input (with a size limit), a memoized selector in your store, or a data library cache. On the server, React's `cache` shares within one request.

```js
const cache = new Map();

export function getChartData(datasetId, raw) {
  const key = datasetId;
  if (!cache.has(key)) {
    if (cache.size > 50) cache.delete(cache.keys().next().value);
    cache.set(key, expensiveTransform(raw));
  }
  return cache.get(key);
}
```

Be careful with stale entries when the raw data changes. Include a version in the key if needed.

#### 326: When does the compiler skip memoizing a value?

It doesn't memoize primitives that are cheap to compare and recompute in a way that matters, and it skips values that it can't prove are safe, like those that escape into mutable places or depend on code it can't analyze. It also bails out of a whole function if it finds a Rules of React violation, like conditional hook calls, or unsupported syntax. The ESLint rules and the playground show these bailouts.

#### 327: How do `useMemo` and `useCallback` behave in StrictMode during development?

In development, StrictMode calls the calculation function in `useMemo` (and the initializer of `useState`) twice to help find impure code. Since React 19, during the double render, React reuses the memoized result from the first call instead of keeping two different values, so that `useMemo` and `useCallback` results stay consistent. This only affects development.

#### 328: Why can memoization hide bugs, and how do you test for that?

If a component only works correctly because a value is memoized (for example, an effect that would loop forever without `useMemo`), the code is fragile: when React drops the cache, the bug appears. Test by temporarily removing memoization or by running under StrictMode, and make sure effects behave correctly when dependencies change identity. Code should be correct without memoization and only faster with it.

#### 329: How do you deal with callbacks passed to many memoized children that need fresh state?

Using `useCallback` with the state in the dependency list gives a new function on every state change, so all children re-render. Options:

- Use functional updates so the callback doesn't need the state.
- Use `useReducer` and pass `dispatch`.
- Keep the latest state in a ref updated in an effect, and read it in a stable callback. Use this one with care, since it reads values outside render.

```jsx
const latest = useRef(items);
useEffect(() => {
  latest.current = items;
});
const onSave = useCallback(() => save(latest.current), []);
```

#### 330: What is the trade-off between fine-grained memoization and code size in the compiler output?

Compiled code has extra comparisons and cache slots, so it's somewhat bigger than the original, which adds a little to the bundle and parsing cost. In exchange, renders do less work. For most apps the runtime savings are bigger than the size cost, but if most of your components render once and never update, you pay the size without much gain. Measure both bundle size and interaction speed.

### Advanced: State and Context (331-345)

#### 331: How does React propagate a context change internally?

When a provider's value changes (`Object.is`), React walks down the subtree looking for fibers that depend on that context and marks them, and their parents' `childLanes`, as needing work. Then the render visits those fibers even if components in between bailed out. That's why a memoized component in between doesn't stop context consumers below it from updating, and why the cost of a context change grows with the size of the subtree.

#### 332: How would you build a context with selectors yourself?

Put a stable store object in context (it never changes), and have components subscribe to the store with `useSyncExternalStore` and a selector. Only components whose selected value changes will re-render.

```jsx
function createStore(initial) {
  let state = initial;
  const listeners = new Set();
  return {
    get: () => state,
    set: (fn) => {
      state = fn(state);
      listeners.forEach((l) => l());
    },
    subscribe: (l) => {
      listeners.add(l);
      return () => listeners.delete(l);
    },
  };
}

const StoreContext = createContext(null);

function useStoreSelector(selector) {
  const store = use(StoreContext);
  return useSyncExternalStore(store.subscribe, () => selector(store.get()));
}
```

The selector must return a stable value (a primitive or a cached object), otherwise the component re-renders every time. This is basically what Zustand does.

#### 333: How do you design state for a large editor or canvas app where many items change often?

Keep item data in a normalized store outside React, keyed by id. Each item component subscribes to its own item by id, so moving one item only re-renders that item. Keep transient state, like the drag position, out of React state when possible and apply it directly to the DOM or canvas. Batch updates per frame. Use React for the structure and a canvas or direct DOM updates for very frequent visual changes.

#### 334: What is the problem with storing derived data in a global store?

Derived data must be kept in sync manually with its source on every change, which is easy to forget and causes stale UI. Every update also has to write both values, creating more store notifications. Use memoized selectors to compute derived data on read, so it's always correct and only recalculated when inputs change.

#### 335: How do you prevent a frequently updating value (like a timer) from re-rendering the whole app?

Keep it in the smallest component that shows it. If many places need it, put it in a store and subscribe only where it's displayed. For values that drive visuals only, update the DOM directly through a ref or use CSS animations. Never put a fast ticking value in a context at the top of the app.

#### 336: How does `useSyncExternalStore` affect concurrent features?

If an external store changes during a concurrent render, React can't use the in-progress render safely, so it re-renders synchronously. Updates to external stores are always treated as blocking, so they can't be in a transition the way `useState` updates can. That's a trade-off: you get no tearing, but you lose the ability to keep the old UI during a slow update. Some libraries add transition support by combining their store with React state.

#### 337: How do you handle state that needs to be shared between Server Components and Client Components?

Server Components don't have state, since they render once per request. Pass data from the server as props to Client Components, and keep interactive state on the client. For values that must survive navigation and be readable on the server, use the URL or cookies. After a mutation, revalidate or refresh the server data instead of copying it into client state.

#### 338: How do you avoid re-renders from a context that holds functions?

Functions created in the provider are new on every render unless memoized, which changes the context value. Wrap them in `useCallback` (or let the compiler do it), or use `useReducer` and expose `dispatch`, which is stable. Better yet, split actions into their own context that never changes.

#### 339: When does lifting state up become a performance problem, and what's the alternative?

When the common parent is high in the tree and the state changes often, every update re-renders a large subtree. Alternatives: keep the state in a store and subscribe only where it's used, pass the changing value only to the leaves that need it, or use composition so the parent doesn't render the heavy siblings itself. Sometimes duplicating a small piece of UI state is fine if it avoids coupling.

#### 340: How do you persist state to `localStorage` without slowing down every update?

Writing to `localStorage` is synchronous and serializing large objects is slow. Debounce writes, only save the part of the state you need, and write in an effect or a store subscription instead of in the render. Read once with lazy initial state. For large data, use IndexedDB, which is asynchronous.

```jsx
const [draft, setDraft] = useState(() => localStorage.getItem("draft") ?? "");

useEffect(() => {
  const id = setTimeout(() => localStorage.setItem("draft", draft), 500);
  return () => clearTimeout(id);
}, [draft]);
```

#### 341: How does Immer's structural sharing help memoization?

Immer creates a new object only along the path to the changed field and reuses everything else. So after updating one item in a list, the list and that item are new references, but all other items keep their old references. Memoized rows for unchanged items see the same props and skip rendering.

#### 342: What are signals and how do they compare to React's model?

Signals (in Solid, Preact Signals, Angular, Vue) track which code reads each value and update only that code when the value changes, without re-running components. React re-runs components and compares output, then relies on memoization to skip work. Signals can be more precise by default, while React's model is simpler to reason about and the compiler closes much of the gap. Preact Signals has a React integration, but it works outside React's rules, so it's not common in React apps.

#### 343: How do you split a large Redux store so updates don't touch unrelated components?

Each `useSelector` runs on every store update, so keep selectors cheap and specific. Use memoized selectors for derived data. Normalize entities so one update creates few new references. Avoid selectors that return the whole slice. If the store is huge, code split slices with lazy reducers (`combineSlices` with `inject` in Redux Toolkit) so they only load with their feature.

#### 344: How do you handle state for very large forms with hundreds of fields?

Avoid one big state object at the top. Use a form library that keeps values in a ref-based store and lets each field subscribe to its own value (React Hook Form's `useController` or `useWatch`, for example). Validate per field and only re-render the fields that change. Split long forms into steps or sections, and lazy render sections that are collapsed.

#### 345: Your app has a single top-level context with user, theme, cart and notifications. Typing in a search box is slow. How do you approach it?

Profile first. You'll likely see the whole app re-render when something in the context changes, for example notifications polling every few seconds or the search state living there. Then:

- Move the search input state into the search component.
- Split the context into separate ones, at least by how often they change.
- Memoize each provider value.
- Move notifications and the cart into a store with selectors.
- Make sure big parts of the tree are passed as `children` to providers, not rendered by them.

### Advanced: Lists and Large Data (346-360)

#### 346: How does React's list reconciliation work, and what is its cost?

React walks the old and new children lists from the start, matching items while keys are the same. When it finds a difference, it puts the remaining old children into a map by key, then looks up each remaining new child in that map to reuse or create it. Items whose position changed are moved. This is roughly linear in the number of children. The real cost is usually rendering the rows, not the matching, which is why memoized rows and stable keys matter more than the algorithm.

#### 347: Why is moving an item from the end of a list to the start more expensive than the other way?

React's algorithm tracks the last placed index of reused items. When an item moves to the front, every other item now appears after it in the new list, but their old positions are lower than the last placed index, so React marks all of them as moved and does a DOM insert for each. Moving an item from the front to the end only marks that one item as moved. For lists where items often go to the top, like chat or feeds, consider rendering in reverse order with CSS (`flex-direction: column-reverse`) if that fits.

#### 348: How do you build a virtualized chat that keeps the scroll position when older messages load at the top?

When items are prepended, everything shifts down. You need to adjust the scroll offset by the height of the new items. Measure the scroll height before and after the update and correct `scrollTop` in a layout effect, so the user doesn't see a jump. Libraries like `react-virtuoso` have built-in support for this. Also keep "stick to bottom" logic when the user is at the end and new messages arrive.

```jsx
const prevHeight = useRef(0);

useLayoutEffect(() => {
  const el = scrollRef.current;
  const diff = el.scrollHeight - prevHeight.current;
  if (prepended) el.scrollTop += diff;
  prevHeight.current = el.scrollHeight;
}, [messages]);
```

#### 349: How do you virtualize a grid with both many rows and many columns?

Use two virtualizers, one for rows and one for columns, and only render the cells in the visible rows and columns. Keep headers sticky outside the virtualized area or virtualize them with the column virtualizer. Fixed sizes are simpler and faster. If columns have variable widths, measure once and cache. Libraries like TanStack Virtual support this with a horizontal virtualizer.

#### 350: How would you render a table with 100,000 rows that the user can sort and filter?

- Keep the data in a plain array or typed structure, not in React state of each row.
- Sort and filter in a Web Worker or with pre-built indexes, and send back only the order of ids.
- Virtualize rows and columns.
- Memoize rows by id, and pass only primitives.
- Mark sort and filter changes as transitions so the UI stays responsive.
- If the data comes from a server, consider doing sorting and filtering there and fetching only visible pages.

#### 351: How do you avoid creating 100,000 objects on every update in a big data set?

Avoid mapping the whole data set to new objects in render (for example `data.map(d => ({ ...d, label }))`). Compute derived fields once when the data arrives, keep the same item objects across updates, and update only changed items by id. Store large numeric data in typed arrays if that fits. Memoize transformations so they run only when the source data changes.

#### 352: How does `key` choice affect performance when data is refetched?

If the server returns new objects for the same items, but keys are stable ids, React reuses the existing components and DOM and only updates changed content. If keys are generated per fetch, every refetch remounts all rows. Also, if rows are memoized, new objects with the same data still break memoization, so data libraries that keep unchanged objects (TanStack Query's structural sharing) help a lot.

#### 353: What is structural sharing in TanStack Query?

When new data arrives, TanStack Query compares it with the old data and keeps the old object references for parts that didn't change. Components that select unchanged parts see the same references, so memoization works and they don't re-render. It's on by default for JSON data. For very large responses, the deep comparison itself has a cost, and you can turn it off with `structuralSharing: false`.

#### 354: How do you use the `select` option in TanStack Query to reduce re-renders?

`select` transforms or picks part of the query data for one component. The component only re-renders when the selected result changes, even if other parts of the cached data change. Keep the `select` function stable (defined outside or memoized) so it isn't re-run on every render.

```jsx
const selectCount = (todos) => todos.length;

function TodoCount() {
  const { data: count } = useQuery({
    queryKey: ["todos"],
    queryFn: fetchTodos,
    select: selectCount,
  });
  return <span>{count}</span>;
}
```

#### 355: How do you render very large text or logs efficiently?

Don't render megabytes of text in one element. Split it into lines, virtualize the lines, and only keep a limited window in memory if it's a live log (a ring buffer). Use a monospace font and fixed line height so you don't need to measure. Search and highlighting should run on the data, not by scanning the DOM.

#### 356: When should you move list rendering to canvas or WebGL?

When you need to draw tens of thousands of items that change often, like a big scatter plot, a map with many markers or a game-like view, DOM nodes become too heavy even with virtualization. Canvas or WebGL draws pixels without DOM nodes. You lose built-in accessibility, text selection and events per item, so you need to add hit testing and an accessible alternative yourself.

#### 357: How do you keep a virtualized list accessible?

Use proper roles (`list`/`listitem`, or `grid`/`row`/`gridcell`), and set `aria-setsize` and `aria-posinset` (or `aria-rowcount` and `aria-rowindex`) so screen readers know the full size. Keep keyboard navigation working by scrolling the focused item into view and keeping focus on it as rows are recycled. Provide a search or "jump to" feature since find-in-page doesn't work for unrendered rows.

#### 358: How do you avoid jank when a virtualized list's rows contain images?

Images that load after the row is measured change the row height and cause jumps. Give images fixed dimensions or aspect ratios, use thumbnails, and decode them asynchronously. Avoid starting many image downloads while scrolling fast. Some apps only load images once scrolling slows down, and lower `overscan` while scrolling quickly.

#### 359: How do you handle sorting and grouping that change the structure of a big list without remounting everything?

Keep keys based on item ids, not on position or group. If grouping adds header rows, give headers their own stable keys like `group-${name}`. When structure changes, React can then move existing rows instead of recreating them. With virtualization, only the visible rows are affected anyway, so make sure the virtualizer's `getItemKey` uses ids so its measurement cache stays valid.

#### 360: A list of 2,000 cards takes 800 ms to render on first load. How do you fix it?

Profile to see where the time goes: React render, layout, images or data processing. Likely fixes:

- Virtualize the list, or render the first screen and load more on scroll.
- Simplify each card (fewer elements, no heavy components inside).
- Move data processing out of render or into a worker.
- Use `content-visibility: auto` if you can't virtualize.
- Render the list in a transition after the shell, so the page appears and stays responsive.

### Advanced: Effects and Data Fetching (361-375)

#### 361: How do Server Components remove client-side waterfalls?

Data fetching happens on the server, close to the database, where each request is fast. Even if components fetch one after another, the round trips are much shorter than from the browser. And the browser gets the rendered result in one response instead of making several requests after the JavaScript loads. You can still create server waterfalls, so start independent fetches in parallel and use Suspense to stream parts that are slow.

#### 362: How do you avoid a waterfall between parent and child Server Components?

Start the child's data request in the parent before awaiting the parent's own data, and pass the promise down. Or have both start at the same time and await only where needed. Wrapping the child in Suspense lets the parent render without waiting for the child's data.

```jsx
export default async function Page({ params }) {
  const { id } = await params;
  const postsPromise = getPosts(id); // starts now
  const user = await getUser(id);
  return (
    <>
      <Profile user={user} />
      <Suspense fallback={<PostsSkeleton />}>
        <Posts postsPromise={postsPromise} />
      </Suspense>
    </>
  );
}
```

#### 363: What is `cacheSignal` and when would you use it?

`cacheSignal`, added in React 19.2 for Server Components, returns an `AbortSignal` that is aborted when the lifetime of the current `cache()` scope ends: when the render finished, was aborted or failed. You pass it to `fetch` or other async work so that requests no longer needed are cancelled instead of wasting server resources.

```js
import { cache, cacheSignal } from "react";

const getUser = cache((id) =>
  fetch(`/api/users/${id}`, { signal: cacheSignal() }),
);
```

#### 364: How do you design client-side cache invalidation after a mutation?

Invalidate or update only the queries that the mutation affects. With TanStack Query you can update the cache directly from the mutation response with `setQueryData` (no refetch), or invalidate by key prefix to refetch. For lists, an optimistic update plus a background refetch gives fast feedback and correct data. Invalidating everything is simple but causes many requests and re-renders.

```js
const mutation = useMutation({
  mutationFn: updateTodo,
  onSuccess: (updated) => {
    queryClient.setQueryData(["todo", updated.id], updated);
    queryClient.invalidateQueries({ queryKey: ["todos"] });
  },
});
```

#### 365: How do you implement optimistic updates safely?

Apply the change in the UI immediately, keep the previous state, send the request, and roll back if it fails. Cancel in-flight refetches of the same data first, so they don't overwrite the optimistic state. Refetch after the mutation settles to get the real server data. In React 19, `useOptimistic` handles the "show and revert" part automatically when the action finishes.

#### 366: How can effects make INP worse?

Effects from `useEffect` run after paint, so normally they don't delay the visual response. But if an effect does heavy work or sets state that causes another big render, that work can block the next interaction. Layout effects are worse since they run before paint. Also, if the user interacts before passive effects ran, React flushes them first, adding to the delay. Keep effects small and move heavy work to idle time or a worker.

#### 367: When does React run `useEffect` before the browser paints?

Normally `useEffect` runs after paint. But if the update was caused by a discrete user input like a click, React may run the effects at the end of the commit, before the browser paints, so the result of the effect is visible together with the update. React also flushes any pending effects before it starts the next render. So a slow `useEffect` after a click can delay the paint and make INP worse, even though it isn't a layout effect.

#### 368: How do you deduplicate requests made at the same time by different components without a library?

Keep a module-level map of in-flight promises keyed by URL. The first caller creates the promise, and later callers get the same one. Remove the entry when it settles or keep it as a cache with an expiry.

```js
const inflight = new Map();

export function getJSON(url) {
  if (!inflight.has(url)) {
    const p = fetch(url)
      .then((r) => r.json())
      .finally(() => setTimeout(() => inflight.delete(url), 1000));
    inflight.set(url, p);
  }
  return inflight.get(url);
}
```

This kind of stable promise can also be passed to `use` on the client.

#### 369: Why can't you create a promise in a Client Component render and pass it to `use`?

Every render would create a new promise, so `use` would suspend again each time, and React would keep showing the fallback or loop. React warns about uncached promises. Promises for `use` on the client must come from a cache (keyed by input), a Suspense-ready library, or a Server Component that passes them as props.

#### 370: How do you avoid fetching data twice with SSR and a client data library?

Fetch on the server, put the result into the library's cache, serialize (dehydrate) the cache into the HTML, and hydrate it on the client before rendering. With TanStack Query, use `dehydrate` on the server and `HydrationBoundary` on the client, and set a `staleTime` above zero so the client doesn't refetch right after hydration.

#### 371: How does `useEffect` cleanup ordering affect performance when navigating?

When a page unmounts, React runs all its effect cleanups. If cleanups do heavy work, like saving large state synchronously or tearing down big third-party widgets, the navigation feels slow. Keep cleanups cheap, defer heavy saving, and consider `<Activity>` for screens the user returns to often, so they don't mount and unmount each time.

#### 372: How do you handle a slow third-party widget that must be initialized in an effect?

Lazy load its script, initialize it only when its container is visible (`IntersectionObserver`), and do it in an idle callback if it isn't urgent. Make sure it's created once and destroyed in cleanup, and that it doesn't re-initialize when unrelated props change. Keep options stable with `useMemo` or compare the relevant primitives in the effect deps.

#### 373: What are the performance trade-offs of GraphQL clients like Apollo in React?

They give a normalized cache, so one update to an entity updates every component that shows it, and they dedupe queries. But the normalized cache adds CPU work on every write and read, and large queries can make re-renders broad if many components watch the same entities. Use fragments to limit what each component reads, avoid over-fetching fields, and watch the client bundle size.

#### 374: How do you stop an expensive effect from running when only a callback prop changes identity?

If the parent passes a new function each render, an effect that depends on it re-runs each time. Use `useEffectEvent` to read the latest callback without adding it to the deps, so the effect only re-runs when real inputs change.

```jsx
function Map({ center, onMove }) {
  const handleMove = useEffectEvent((e) => onMove(e));

  useEffect(() => {
    const map = createMap(center);
    map.on("move", handleMove);
    return () => map.destroy();
  }, [center]);
}
```

#### 375: A dashboard makes 40 API calls on load. How would you improve it?

- Check for duplicates and dedupe with a shared cache.
- Check for waterfalls and start independent requests in parallel or in a route loader.
- Combine related endpoints into one (a backend-for-frontend or a GraphQL query).
- Load only what is visible at first, and lazy load widgets below the fold.
- Cache with a sensible `staleTime`, and use HTTP caching for data that rarely changes.
- Move data fetching to the server with Server Components if the framework supports it.

### Advanced: Concurrent Features and Suspense (376-390)

#### 376: How are transitions implemented internally?

`startTransition` sets a flag while your callback runs, so updates scheduled inside get a transition lane instead of a sync or default lane. React then renders those lanes in a concurrent loop that yields every few milliseconds. If an urgent update arrives, React pauses, renders the urgent update on top of the current tree, and then restarts the transition from scratch on the new state. Transition renders that suspend don't commit fallbacks for already visible content.

#### 377: Why can a transition still make the page janky?

React can only yield between components. If a single component takes 200 ms to render, React can't interrupt it, so input still waits. Concurrent rendering also doesn't help with the commit phase, layout and paint, which are synchronous. Make individual components cheaper, split heavy work across components, or move it to a worker. Large DOM changes at commit time also block the main thread.

#### 378: How does React decide whether to show a Suspense fallback or keep old content?

If a boundary is being shown for the first time, React shows the fallback. If the boundary already shows content and the update that suspends is a transition, React keeps the old content and waits. If the update is urgent (not a transition), React shows the fallback for already visible content, which is why navigations should be wrapped in transitions.

#### 379: What does "throttling of Suspense fallbacks" mean?

When content inside nested Suspense boundaries resolves at slightly different times, React waits a little (around 300 ms) before revealing the next level, so the UI doesn't flash through many states. This throttling trades a slightly later reveal for a calmer loading experience.

#### 380: How does `<Activity>` pre-rendering work and what does it cost?

Content in a hidden `<Activity>` is rendered at the lowest priority, after all visible work is done. It can fetch data with Suspense and load code, so when it becomes visible it's ready. Effects don't run while hidden. The cost is memory for the hidden DOM and state, and CPU time in the background. Use it for a few likely next screens, not for every possible page.

#### 381: Why should you be careful with `<Activity>` and things like videos or audio?

Hidden content is only `display: none`, so elements keep their state. A playing `<video>` keeps playing sound when hidden, and timers in non-effect code keep running. Pause media in an effect cleanup (which runs when the Activity is hidden), and check that any code that runs while hidden is safe.

```jsx
useLayoutEffect(() => {
  const video = videoRef.current;
  return () => video.pause();
}, []);
```

A layout effect is used so the pause happens as soon as the content is hidden.

#### 382: How does selective hydration prioritize user input?

During hydration, React hydrates Suspense boundaries one at a time. If the user clicks inside a boundary that isn't hydrated yet, React records the event, raises the priority of that boundary, hydrates it synchronously, and then replays the event so the click isn't lost. Other boundaries continue hydrating afterwards. This only works if the page is split into Suspense boundaries.

#### 383: What is the difference between `useDeferredValue` and debouncing for performance?

Debouncing waits a fixed time before doing work, even on fast devices, and the work itself still blocks once it starts. `useDeferredValue` starts the background render right away, can be interrupted by new input, and adapts to the device: on a fast machine results update almost immediately, on a slow one they lag more. Debouncing is still the right choice for network requests, where you want to send fewer calls.

#### 384: How can you yield to the browser inside a long event handler?

Split the work and give control back between chunks. `scheduler.yield()` is available in Chromium-based browsers. Elsewhere, `setTimeout(0)` or a `MessageChannel` works. Show visual feedback first, then yield, then do the rest.

```js
async function handleClick() {
  setLoading(true);
  await yieldToMain();
  const result = heavyCalculation();
  startTransition(() => setResult(result));
}

function yieldToMain() {
  if (globalThis.scheduler?.yield) return scheduler.yield();
  return new Promise((resolve) => setTimeout(resolve, 0));
}
```

#### 385: Why might `isPending` from `useTransition` flicker, and how do you fix it?

If the transition finishes very quickly, `isPending` turns on and off in a few milliseconds, and a spinner flashes. Show the pending indicator only after a short delay with CSS (`transition-delay` or an animation with a delay), or keep it for a minimum time. The CSS approach doesn't need any extra state.

```css
.spinner {
  opacity: 0;
  animation: show 0s 300ms forwards;
}
@keyframes show {
  to {
    opacity: 1;
  }
}
```

#### 386: How do concurrent renders interact with refs and DOM measurement?

During render, the DOM still shows the old UI and refs point to old nodes, because nothing is committed yet. A concurrent render may also be thrown away. So you can only measure the new layout in `useLayoutEffect` or ref callbacks after commit. Reading the DOM during render gives stale or wrong values and isn't safe.

#### 387: What is the `<ViewTransition>` component and what is its status?

`<ViewTransition>` is a React component that animates UI changes using the browser's View Transitions API, for example when switching pages in a transition. As of React 19.2 it's available in the canary and experimental channels, not in the stable release. The browser does the animation on the compositor with snapshots, which can be cheaper than JavaScript animation, but large or many named transitions still have a cost.

#### 388: What happens when a component suspends during a sync update?

For an urgent update, React can't keep the old UI, so it shows the nearest Suspense fallback, even for content that was already visible. Since React 19, React commits the fallback immediately and then tries to render the suspended siblings in the background ("pre-warming"), so their data requests start early. Wrapping updates in transitions avoids hiding visible content.

#### 389: How do you test that an update is non-blocking?

In the browser, record the interaction in the Performance panel and check that the input event's handling is short and the transition render is split into small tasks. With React's Performance Tracks, you can see the update in the Transition lane separate from the blocking one. In tests, `act` flushes everything, so it can't show this. Real profiling is the right tool.

#### 390: Typing in a filter box is laggy because the results list re-renders on each key press. Walk through the fix.

1. Confirm with the Profiler that the list render is the cost.
2. Keep the input controlled by its own state, updated urgently.
3. Pass `useDeferredValue(query)` to the results.
4. Make the results component memoized (`memo` or compiler) so it skips the urgent render.
5. Memoize the filtering.
6. If the list is long, virtualize it.
7. Profile again on a throttled CPU to confirm typing stays smooth.

### Advanced: Code Splitting and Bundle Size (391-405)

#### 391: How do you avoid a chunk loading waterfall with nested lazy components?

If a lazy page renders a lazy child, the browser loads the page chunk, runs it, and only then discovers the child chunk. Start both imports together: preload the child's import when the route starts loading, or use a framework that knows the route's module graph and adds `modulepreload` links for all chunks of the route. Avoid many levels of `lazy` inside each other for code that is always needed together.

#### 392: How do frameworks preload route chunks before navigation?

They build a manifest that maps each route to its JavaScript and CSS files. When a link becomes visible or is hovered, the router adds `<link rel="modulepreload">` or `prefetch` for those files, and may also start the route's data loader. When the user clicks, the code is already in the cache. React Router framework mode, Next.js and TanStack Router all do some version of this.

#### 393: What are the risks of `lazy` for components above the fold?

If the first screen depends on a lazy component, the browser has to download the main bundle, run it, then request the lazy chunk, then render. That adds at least one round trip before LCP. With SSR the HTML is there, but hydration of that part waits for the chunk. Code split below-the-fold and on-interaction parts, not the main content.

#### 394: How do you analyze why a specific module ended up in the main bundle?

Use the bundle analyzer to find it, then check which file imports it. Vite's `rollup-plugin-visualizer` and webpack's stats with tools like Statoscope show import chains. Often it's a shared utility file that imports a heavy library, a barrel file, or a static import in a component that should be dynamic. Moving that import into a separate module or behind `import()` fixes it.

#### 395: How do you split a large component library so apps only load what they use?

Publish ES modules with one file per component, mark the package as `"sideEffects": false` (listing CSS files if any), and provide `exports` subpaths. Avoid a single entry that imports everything with side effects. Keep peer dependencies (React) as peers, not bundled. Test tree shaking by building a sample app that imports one component and checking its size.

#### 396: What is module federation and what are its performance costs?

Module federation lets separate builds share and load code from each other at runtime, which is common in micro frontends. The cost is extra network requests for remote entry files, possible duplicate copies of React if sharing is set up wrong, and harder caching. Make sure React is shared as a singleton and that remotes are loaded in parallel and cached.

#### 397: How do you keep two copies of React from ending up in the bundle?

Two copies happen when a dependency bundles React or declares a different version in `dependencies` instead of `peerDependencies`. Check with `npm ls react` and the bundle analyzer. Fix it with dedupe (`npm dedupe`, package manager overrides) or a bundler alias like Vite's `resolve.dedupe: ["react", "react-dom"]`. Besides size, two copies break hooks with the "Invalid hook call" error.

#### 398: How does using Server Components change the code splitting strategy?

Client Components imported by a Server Component are automatically split into their own chunks, and the RSC payload tells the client which chunks to load. So the split points are the `"use client"` boundaries. You think less about `lazy` for routes and more about keeping client boundaries small and not importing large libraries into Client Components. You can still use `lazy` or `next/dynamic` for client code that only appears after interaction.

#### 399: How do you measure the real cost of JavaScript, not just its size?

Size over the network is only part of it. Look at parse and compile time and execution time in the Chrome Performance panel, on a throttled CPU. 100 KB of compressed JavaScript can be 300-500 KB uncompressed, and it all has to be parsed and run. Track Total Blocking Time in lab tests and INP and LCP in the field. Code that runs on startup matters most.

#### 400: How does the browser's code cache affect repeat visits, and how do you help it?

V8 caches compiled code for scripts it has seen before, so repeat visits skip some parse and compile work. Changing a file's content creates a new hash and loses the cache for that file. Splitting stable code (like React and other libraries) from often-changing app code means most of the cache survives a deploy. Service workers can also store scripts so they load even without the network.

#### 401: When would you inline critical JavaScript or CSS, and what are the trade-offs?

Inlining small critical CSS (or a tiny script) in the HTML removes a request from the critical path and helps first paint. The trade-off is that inlined code can't be cached separately, so it's downloaded with every HTML response. Inline only what's needed for the first screen, and load the rest normally. Frameworks often do this for CSS automatically.

#### 402: How do you lazy load translations in a large internationalized React app?

Split messages by locale and by feature, and load the needed bundle with a dynamic import when the locale or route changes. Don't import all locales into the main bundle. Preload the current locale's messages with the HTML, and use Suspense or a loading state while switching. Libraries like `i18next` and `react-intl` support async loading of resources.

```js
async function loadMessages(locale, ns) {
  const mod = await import(`./locales/${locale}/${ns}.json`);
  return mod.default;
}
```

#### 403: What is the cost of the React runtime itself, and can you make it smaller?

`react` plus `react-dom` is around 60 KB gzipped in production, and it's the base cost for every page. You can't tree shake much of it. Ways to reduce what it costs users: cache it well with a separate chunk, use Server Components so less app code ships on top of it, or for very small widgets consider Preact with `preact/compat`, at the cost of some compatibility.

#### 404: How do you prevent a new dependency from silently growing the bundle in a team?

Set size budgets per entry or route with `size-limit` or bundler warnings, run them in CI, and post a size diff comment on pull requests. Require a short note on why a large dependency is needed. Keep an allow list of approved libraries for common tasks like dates and charts. Review the bundle analyzer output regularly, for example each release.

#### 405: The main bundle is 1.2 MB and LCP is 5 seconds on mobile. What's your plan?

1. Run a bundle analyzer and the Coverage tab to see what's in the bundle and how much is used on the first page.
2. Split by route and lazy load heavy features like editors, charts and maps.
3. Replace or remove large dependencies and fix imports that break tree shaking.
4. Check for duplicate libraries and polyfills for old browsers.
5. Move to SSR or static rendering for the main pages so content shows before JavaScript runs, and use Server Components if possible.
6. Make sure the LCP element (often an image) is discoverable in HTML and has `fetchPriority="high"`.
7. Add size budgets in CI so it doesn't grow back.

### Advanced: Server Rendering and Hydration (406-420)

#### 406: How does streaming SSR send content out of order?

React sends the shell with placeholders for Suspense boundaries. When a boundary's content is ready, React sends its HTML in a hidden element at the end of the stream, plus a small inline script that moves it into the right place and removes the fallback. So the stream order doesn't have to match the page order, and a slow section doesn't block sections after it.

#### 407: What is the RSC payload and why does its size matter?

The RSC payload is the serialized output of Server Components: the element tree, references to Client Component chunks and the props passed to them. It's sent with the initial HTML (inlined in script tags) and on client navigations. A large payload means more bytes to download, parse and keep in memory, and it's often duplicated with the HTML on first load. Keep it small by passing less data to Client Components and not rendering huge static trees through the client boundary.

#### 408: Why does initial HTML with RSC contain the data twice, and how do you reduce it?

The first response includes the HTML for display and the RSC payload so React on the client can reconstruct the tree without another request. Text content therefore appears in both. You reduce it by keeping props to Client Components minimal, avoiding big JSON blobs as props, and rendering large static content in Server Components that don't need to be re-created on the client (they still appear in the payload as elements, but without client code).

#### 409: How do you choose between SSR, SSG, ISR and client rendering for each route?

- Content that's the same for everyone and changes rarely: static (SSG), served from a CDN.
- Content that changes sometimes: static with revalidation (ISR in Next.js) or cached SSR.
- Personalized or real-time content: SSR with streaming, or a static shell with dynamic parts (partial pre-rendering).
- Highly interactive app screens behind login, where SEO doesn't matter: client rendering can be fine, with a fast shell.

Most apps mix these per route.

#### 410: How do you find what's slowing down server rendering?

Measure the time of each data call on the server and the render time separately, using server timing logs or the `Server-Timing` header, which shows in the DevTools Network panel. Profile the Node process with `--cpu-prof` or the inspector to see if rendering itself is slow (huge trees, heavy CSS-in-JS). Common causes are slow or sequential data calls, missing caches, and rendering big lists on the server.

```js
res.setHeader("Server-Timing", `db;dur=${dbMs}, render;dur=${renderMs}`);
```

#### 411: How do you avoid blocking the Node.js event loop with SSR?

Rendering is CPU work, so one slow render blocks all other requests on that process. Use streaming so work is split, cache rendered output or data, run several processes (cluster or containers) to use all cores, and keep heavy computations out of the render path. Set timeouts with `abort` so a stuck render doesn't hold the server.

#### 412: What is progressive hydration and how does React support it?

Progressive hydration means hydrating parts of the page over time instead of all at once. React does this with Suspense boundaries: each boundary hydrates on its own when its code is ready, and interaction raises its priority. You can push less important parts further back by lazy loading them, so their code arrives later and they hydrate last.

#### 413: How do you handle authentication and personalization without losing caching?

Keep the page mostly the same for everyone, so it can be cached, and render personal parts separately: as a dynamic section in partial pre-rendering, as a small Client Component that fetches user data, or via edge logic that only varies by a few cookie values. Avoid reading cookies or headers at the top of the page if only a small widget needs them, since that makes the whole page dynamic in some frameworks.

#### 414: What happens to hydration if the server HTML has an error in a Suspense boundary?

If a component throws on the server, React sends the boundary's fallback in the HTML and includes the error so the client tries to render that part from scratch. On the client, React renders it without hydration. If it works, the content shows. If it fails again, the nearest error boundary catches it. So server errors don't break the whole page, but they move rendering cost to the client.

#### 415: How do browser extensions cause hydration mismatches, and how does React 19 deal with it?

Extensions sometimes insert elements or attributes into the page before React hydrates. Earlier React versions treated this as a mismatch and re-rendered. React 19 skips unexpected tags inserted by third-party scripts in `<head>` and `<body>` and stylesheets added by extensions, so it doesn't throw away the whole page for them. Mismatches inside your own components are still reported.

#### 416: How do you stream a large page to bots and users differently?

Users benefit from streaming the shell early. Some crawlers prefer the full HTML at once. With `renderToPipeableStream`, you can pipe in `onShellReady` for users and wait for `onAllReady` for bots (detected by user agent). The content is the same, only the timing differs.

```jsx
const isBot = /bot|crawler|spider/i.test(req.headers["user-agent"] ?? "");
const { pipe } = renderToPipeableStream(<App />, {
  bootstrapScripts: ["/main.js"],
  [isBot ? "onAllReady" : "onShellReady"]() {
    res.setHeader("Content-Type", "text/html");
    pipe(res);
  },
});
```

#### 417: How do you make sure the LCP element is in the initial HTML with SSR?

Render the main content (hero image, main heading, first product image) outside Suspense boundaries that wait for slow data, or make its data fast. Include the `<img>` with `src`, `width`, `height` and `fetchPriority="high"` in the server HTML so the browser finds it early. Don't hide it behind client-only rendering, lazy components or `loading="lazy"`.

#### 418: What is the cost of rendering a big component tree on the server on every request?

Every request runs every component, creates element objects and strings, and allocates memory, which uses CPU and causes garbage collection. For large pages under heavy traffic, this can limit how many requests a server can handle. Caching rendered output, static generation, smaller trees and moving rarely changing parts to static HTML reduce it.

#### 419: How do you debug a slow hydration?

Record the page load in the Chrome Performance panel and look for the long task after the main script runs. React's tracks show the hydration render. Check how much time goes to your components (heavy initial render logic, large lists) versus React itself. Use Suspense boundaries to split it, move non-interactive parts to Server Components, and lazy load parts below the fold.

#### 420: Your SSR page has good LCP but bad INP in the first few seconds. What's going on?

The HTML shows quickly, but the page isn't interactive yet: hydration is a long task, and clicks during it are delayed. Third-party scripts may also run at the same time. Fixes:

- Split hydration with Suspense boundaries so React can respond to input between them.
- Ship less JavaScript (Server Components, code splitting).
- Delay third-party scripts.
- Make components cheaper on first render.

### Advanced: Profiling and Measuring (421-435)

#### 421: How do you connect a slow INP in field data to a specific React component?

Use the `web-vitals` attribution build, which reports the interaction target, the event type and the breakdown into input delay, processing and presentation. With Long Animation Frames (LoAF) data, you also get the scripts that ran during the slow frame. Send these with the route name to analytics. Then reproduce that interaction locally on a throttled CPU with the profiling build to find the component.

```js
import { onINP } from "web-vitals/attribution";

onINP(({ value, attribution }) => {
  send({
    value,
    target: attribution.interactionTarget,
    inputDelay: attribution.inputDelay,
    processing: attribution.processingDuration,
    presentation: attribution.presentationDelay,
  });
});
```

#### 422: What is the Long Animation Frames API and how does it help React apps?

LoAF reports frames that took longer than 50 ms to render, with details on which scripts ran, how long each took and where they came from. Compared to the older Long Tasks API, it also shows rendering work and attributes time to specific script sources. For a React app, it can show if a slow frame was your bundle (React render), a third-party script, or layout.

```js
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(entry.duration, entry.scripts);
  }
}).observe({ type: "long-animation-frame", buffered: true });
```

#### 423: How do you write a performance regression test for a React component?

For timing, render the component in a real browser (Playwright or a benchmark tool), repeat the interaction many times and record a metric like the time from input to next paint. Use a profiling build and fixed CPU throttling to reduce noise, and fail only on clear regressions against a baseline. A cheaper and more stable check is to count renders in a unit test, so you catch changes that make a component render when it shouldn't.

```jsx
const renderSpy = vi.fn();

const Results = memo(function Results() {
  renderSpy();
  return <ul>{/* ... */}</ul>;
});

function Page() {
  const [note, setNote] = useState("");
  return (
    <>
      <input
        aria-label="note"
        value={note}
        onChange={(e) => setNote(e.target.value)}
      />
      <Results />
    </>
  );
}

test("typing a note does not re-render the results", async () => {
  render(<Page />);
  renderSpy.mockClear();
  await userEvent.type(screen.getByLabelText("note"), "abc");
  expect(renderSpy).not.toHaveBeenCalled();
});
```

#### 424: Why can Profiler numbers be misleading for very fast components?

Timer resolution and the cost of profiling itself can be bigger than the render of a small component. A component that shows 0.1 ms may be noise. Focus on components that take several milliseconds or on the total commit time. Also, the first render includes JIT warm-up, so later renders are often faster.

#### 425: How do you profile commit-phase costs versus render-phase costs?

The React Profiler mostly shows render-phase time per component. Commit costs (DOM updates, layout effects, ref callbacks) show in the Chrome Performance panel and in React's Components track, which also shows effect durations. If commits are slow, look at layout effects, how many DOM nodes change, and forced layouts from reading layout properties after writes.

#### 426: How do you detect forced synchronous layout caused by React code?

In the Performance panel, look for purple "Layout" blocks inside your JavaScript with a warning "Forced reflow". It happens when code writes to the DOM and then reads layout values like `offsetHeight` or `getBoundingClientRect()` in the same task. In React this often comes from layout effects or ref callbacks that measure many elements one by one after changing styles. Batch all reads before writes, or use `ResizeObserver`.

#### 427: How do you profile memory usage of a React app over a long session?

Use the Memory panel's "Allocation instrumentation on timeline" to see which objects are created and kept over time, and compare heap snapshots between actions. Watch the JS heap size and DOM node count in the Performance monitor during a long session. Look for retained detached DOM trees, closures held by listeners, and caches without limits. In the field, `performance.measureUserAgentSpecificMemory()` (where supported, with cross-origin isolation) gives a rough number.

#### 428: How do you know whether a slow page is a React problem or a browser rendering problem?

Record in the Performance panel. If most of the long task is JavaScript under React functions, the problem is rendering logic. If most of the time is in "Recalculate style", "Layout" or "Paint", it's the DOM size, CSS complexity or layout thrashing. Big style recalculations often come from changing a class on a high-level element that affects many nodes. React's Scheduler and Components tracks help line up React work with browser work.

#### 429: How do you use the Performance panel's insights for a React app?

Newer Chrome versions show an Insights sidebar with LCP breakdown, INP breakdown, layout shift causes, render-blocking requests and third-party impact for a recording. For React apps, the LCP breakdown shows if the delay is in TTFB, resource load or render delay (often JavaScript), and the INP breakdown points to the slow interaction phase. Start there before digging into the flame chart.

#### 430: How do you measure the effect of a change on real users?

Ship it behind a feature flag or to a percentage of users, and compare field metrics (LCP, INP, CLS, custom timings) between the groups. Field data is noisy, so look at the 75th percentile and use enough traffic. Also segment by device type and connection, since improvements often show mostly on slow devices.

#### 431: How do you track custom performance metrics like "time until the dashboard is usable"?

Mark the start (navigation start or the click) and the point when the important content is rendered and interactive, for example in a layout effect of the last important component, and send `performance.measure` results to analytics. Use the Element Timing API (`elementtiming` attribute) in Chromium to get the render time of specific images or text. Keep definitions stable so trends are comparable.

```jsx
<h1 elementtiming="dashboard-title">Dashboard</h1>
```

#### 432: Why should you profile with realistic data?

Many problems only show up with real data sizes: lists of thousands of items, long text, many nested comments or big images. Test data with ten items hides slow filtering and missing virtualization. Use production-like data sets (anonymized if needed) and the heaviest realistic user accounts when profiling.

#### 433: How do you find which state update caused a slow render?

In React DevTools Timeline, each update shows the component that scheduled it. In the Profiler, the "why did this render" info shows which hook or prop changed in the root component of the commit. React 19.2's Performance Tracks in Chrome also show which updates were scheduled and in which lane. Logging the stack trace in the setter's call site is a quick last resort.

#### 434: What is the effect of React DevTools being open on performance?

The extension adds hooks into React that collect information about every commit, which slows rendering, especially in large trees and when profiling or highlighting updates is on. That's fine for finding relative problems, but absolute numbers should be taken with DevTools closed or in a profiling build without the extension recording.

#### 435: Your Lighthouse score is 95 but users complain the app is slow. How do you investigate?

Lighthouse measures the first load in a lab and doesn't catch slow interactions later in a session. Collect field data: INP with attribution, long animation frames and custom timings for key actions. Ask which screens and actions feel slow, and reproduce them with realistic data on a throttled CPU. Common causes are slow re-renders after typing or clicking, big lists, memory growth over time and slow API responses.

### Advanced: Assets, Forms and Everyday Patterns (436-450)

#### 436: How do you build responsive images in a React app without a framework component?

Use `srcSet` and `sizes` so the browser picks the right file, `<picture>` for format fallbacks, and set dimensions. Generate the sizes at build time or with an image CDN.

```jsx
<picture>
  <source
    type="image/avif"
    srcSet="/hero-640.avif 640w, /hero-1280.avif 1280w"
    sizes="100vw"
  />
  <img
    src="/hero-1280.jpg"
    srcSet="/hero-640.jpg 640w, /hero-1280.jpg 1280w"
    sizes="100vw"
    width={1280}
    height={640}
    alt="Mountains"
    fetchPriority="high"
  />
</picture>
```

#### 437: How do you preload the LCP image when it's rendered by a client component?

If the image only appears after JavaScript runs, the browser can't discover it early. Add a preload hint to the HTML, or call `preload` from `react-dom` during SSR so React puts it in the `<head>`. Better, render the image in the server HTML. With responsive images, preload with `imageSrcSet` and `imageSizes` so the right size is fetched.

```jsx
import { preload } from "react-dom";

function Hero() {
  preload("/hero-1280.avif", {
    as: "image",
    fetchPriority: "high",
    imageSrcSet: "/hero-640.avif 640w, /hero-1280.avif 1280w",
    imageSizes: "100vw",
  });
  return <img src="/hero-1280.avif" alt="" />;
}
```

#### 438: How does CSS-in-JS with runtime injection interact with concurrent rendering?

Runtime libraries insert `<style>` rules during render. In concurrent mode, a render can be paused or thrown away, and inserting styles in the middle forces the browser to recalculate styles many times per frame. React added `useInsertionEffect` for these libraries so they insert rules before layout effects run, once per commit. Even so, runtime style generation costs CPU on every render, so zero-runtime solutions (CSS Modules, Tailwind, vanilla-extract, Linaria, StyleX) are usually faster and work better with Server Components.

#### 439: How do you avoid re-rendering a whole form on every keystroke while showing live validation?

Keep field values in a store or form library outside React state, and let each field subscribe to its own value and error. Run validation per field, and debounce expensive or async checks. Show cross-field errors only in the components that need them. With React Hook Form, use `mode: "onBlur"` or `onTouched` for less frequent validation, and `useWatch` for parts that need live values.

#### 440: How do you handle a heavy calculation that must run on every keystroke, like a live markdown preview?

Keep the input urgent, defer the preview with `useDeferredValue`, and memoize the preview component. If parsing is slow even for one render, move it into a Web Worker and show the last result until the new one arrives. For very large documents, parse only the changed part, or render the preview only for the visible area.

```jsx
const deferredText = useDeferredValue(text);
const html = useMemo(() => renderMarkdown(deferredText), [deferredText]);
```

#### 441: How do you implement a fast autocomplete with server results?

- Debounce the request (around 150-300 ms) and cancel outdated ones with `AbortController`.
- Cache results by query so backspacing is instant.
- Keep the input urgent and show the previous results while new ones load.
- Limit results on the server.
- Prefetch popular queries.
- Handle keyboard navigation without re-rendering all options (memoized options, `isActive` boolean prop).

#### 442: How do you keep animations smooth while React is rendering?

React rendering runs on the main thread, so JavaScript-driven animations stall during long renders. Use CSS animations of `transform` and `opacity`, which run on the compositor thread and keep going even when the main thread is busy. Use the Web Animations API instead of `requestAnimationFrame` loops when possible, and render heavy updates in transitions so React yields between components.

#### 443: How would you optimize a React app that runs inside a low-powered device, like a smart TV?

Assume a slow CPU and little memory. Ship a small bundle, avoid big libraries, and render less: virtualize everything, keep the DOM small, and avoid expensive CSS like large shadows, blur filters and many layers. Use spatial navigation that doesn't re-render all items on focus change. Avoid memory leaks, since the app may run for hours. Test on the real device, since browser emulation doesn't show the real limits.

#### 444: How do you use `useInsertionEffect`, and why is it only for CSS-in-JS libraries?

`useInsertionEffect` runs before any layout effects, so a library can insert `<style>` tags before other code reads layout. That avoids layout being calculated with missing styles and then calculated again. It can't read refs or schedule updates, and it's only meant for library authors who inject styles. App code should use `useEffect` or `useLayoutEffect`.

```jsx
function useCSS(rule) {
  useInsertionEffect(() => {
    if (!inserted.has(rule)) {
      inserted.add(rule);
      document.head.appendChild(createStyleTag(rule));
    }
  });
  return getClassName(rule);
}
```

#### 445: How do you handle very large file uploads without freezing the UI?

Don't read the whole file into memory in the main thread. Upload it in chunks with `fetch` and `file.slice()`, track progress per chunk, and update the progress state at a limited rate (for example every 100 ms, not on every byte event). Do hashing or parsing in a Web Worker. Allow canceling with `AbortController`.

#### 446: What makes modals and drawers expensive, and how do you make them cheap?

They're often rendered (hidden) all the time, with all their content and effects, or they re-render the whole page when opened because the open state lives at the top. Mount the content only when open (or keep it in `<Activity>` if reopening must be instant), keep the open state close to the trigger or in a small store, lazy load heavy modal content, and use the native `<dialog>` element for focus and layering.

#### 447: How do you optimize a React app for slow networks?

- Server render or pre-render the first screen so content shows before JavaScript.
- Keep the critical path small: few blocking resources, small CSS, preloaded fonts and LCP image.
- Cache aggressively with hashed files and a service worker.
- Use stale-while-revalidate data, optimistic updates and offline support where it makes sense.
- Show skeletons and keep old content during transitions.
- Compress responses with Brotli and use HTTP/2 or HTTP/3.

#### 448: When should you not optimize a React component?

When the Profiler shows it's fast, when it renders rarely, when the slowness is elsewhere (network, server, layout), or when the optimization makes the code much harder to understand for a tiny gain. Premature memoization and complex caching add bugs and maintenance cost. Fix the biggest measured problem first, and move on when the user experience is good enough.

#### 449: How would you set up a performance culture in a React team?

- Agree on target metrics (Core Web Vitals and a few custom timings) and track them in field monitoring.
- Add bundle size budgets and Lighthouse CI to pull requests.
- Enable the React Compiler and the hooks ESLint plugin so common re-render problems are handled automatically.
- Have a short checklist for new features: virtualization for long lists, lazy loading for heavy parts, image sizes and priorities.
- Review performance dashboards regularly and test on low-end devices.

#### 450: You join a project with a slow React app and no performance data. What do you do first?

1. Add field monitoring for LCP, INP and CLS by route, so you know where users suffer.
2. Run Lighthouse and look at the bundle with an analyzer to catch obvious load problems.
3. Profile the slowest screens and interactions with the React Profiler and the Performance panel, on a throttled CPU and with real data.
4. Fix the biggest problems first: often bundle size, data waterfalls, state placed too high and long lists.
5. Turn on the React Compiler if the code follows the Rules of React.
6. Add budgets and checks so things don't get slow again, and measure again after each change.
