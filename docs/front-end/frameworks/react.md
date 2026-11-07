# React Interview Questions and Answers

_Last updated: October 28, 2026_

450 React interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers are based on React 19 (including the 19.1 and 19.2 releases), so they use the current APIs: `createRoot`, hooks, Actions, `use`, `ref` as a prop, Server Components, the React Compiler and so on. Code examples are included where they help.

If you spot a mistake or something that is out of date, feel free to open an issue or a pull request.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is React?](#1-what-is-react)
- [2: Who created React and who maintains it now?](#2-who-created-react-and-who-maintains-it-now)
- [3: What is the current major version of React?](#3-what-is-the-current-major-version-of-react)
- [4: What are the main features of React?](#4-what-are-the-main-features-of-react)
- [5: What is JSX?](#5-what-is-jsx)
- [6: Is JSX required to use React?](#6-is-jsx-required-to-use-react)
- [7: What does JSX compile to?](#7-what-does-jsx-compile-to)
- [8: Why don't we need to write `import React from "react"` at the top of every file anymore?](#8-why-dont-we-need-to-write-import-react-from-react-at-the-top-of-every-file-anymore)
- [9: What is a component?](#9-what-is-a-component)
- [10: What is the difference between function components and class components? Which one should you use?](#10-what-is-the-difference-between-function-components-and-class-components-which-one-should-you-use)
- [11: How do you create a function component?](#11-how-do-you-create-a-function-component)
- [12: What are props?](#12-what-are-props)
- [13: Can a component change its own props?](#13-can-a-component-change-its-own-props)
- [14: What is state?](#14-what-is-state)
- [15: What is the difference between props and state?](#15-what-is-the-difference-between-props-and-state)
- [16: What is `useState`?](#16-what-is-usestate)
- [17: Why shouldn't you modify state directly?](#17-why-shouldnt-you-modify-state-directly)
- [18: How do you update state based on the previous state?](#18-how-do-you-update-state-based-on-the-previous-state)
- [19: What is the Virtual DOM?](#19-what-is-the-virtual-dom)
- [20: What is reconciliation?](#20-what-is-reconciliation)
- [21: What is a React element?](#21-what-is-a-react-element)
- [22: What is the difference between an element and a component?](#22-what-is-the-difference-between-an-element-and-a-component)
- [23: How do you render a React app into the page?](#23-how-do-you-render-a-react-app-into-the-page)
- [24: What is the `root` element in a React app?](#24-what-is-the-root-element-in-a-react-app)
- [25: What are Fragments?](#25-what-are-fragments)
- [26: When do you need `<Fragment>` instead of `<>`?](#26-when-do-you-need-fragment-instead-of-)
- [27: How do you render a list in React?](#27-how-do-you-render-a-list-in-react)
- [28: What are keys and why are they needed?](#28-what-are-keys-and-why-are-they-needed)
- [29: Why is using the array index as a key a bad idea?](#29-why-is-using-the-array-index-as-a-key-a-bad-idea)
- [30: How do you render something conditionally?](#30-how-do-you-render-something-conditionally)
- [31: What is the problem with `{count && <Badge />}`?](#31-what-is-the-problem-with-count--badge-)
- [32: How do you handle events in React?](#32-how-do-you-handle-events-in-react)
- [33: What is a synthetic event?](#33-what-is-a-synthetic-event)
- [34: How do you pass arguments to an event handler?](#34-how-do-you-pass-arguments-to-an-event-handler)
- [35: How do you prevent the default browser behavior?](#35-how-do-you-prevent-the-default-browser-behavior)
- [36: What is the `children` prop?](#36-what-is-the-children-prop)
- [37: How can you style React components?](#37-how-can-you-style-react-components)
- [38: Why do we use `className` instead of `class` in JSX?](#38-why-do-we-use-classname-instead-of-class-in-jsx)
- [39: How do you write inline styles in React?](#39-how-do-you-write-inline-styles-in-react)
- [40: What is a controlled component?](#40-what-is-a-controlled-component)
- [41: What is an uncontrolled component?](#41-what-is-an-uncontrolled-component)
- [42: How do you handle a text input in React?](#42-how-do-you-handle-a-text-input-in-react)
- [43: How do you handle checkboxes and select elements?](#43-how-do-you-handle-checkboxes-and-select-elements)
- [44: What is `useEffect`?](#44-what-is-useeffect)
- [45: How does the dependency array of `useEffect` work?](#45-how-does-the-dependency-array-of-useeffect-work)
- [46: What is the cleanup function in `useEffect`?](#46-what-is-the-cleanup-function-in-useeffect)
- [47: How do you fetch data with `useEffect`?](#47-how-do-you-fetch-data-with-useeffect)
- [48: What are hooks?](#48-what-are-hooks)
- [49: What are the rules of hooks?](#49-what-are-the-rules-of-hooks)
- [50: Can you use hooks in class components?](#50-can-you-use-hooks-in-class-components)
- [51: What is `useRef`?](#51-what-is-useref)
- [52: How do you access a DOM element in React?](#52-how-do-you-access-a-dom-element-in-react)
- [53: What is the difference between `useRef` and `useState`?](#53-what-is-the-difference-between-useref-and-usestate)
- [54: What is lifting state up?](#54-what-is-lifting-state-up)
- [55: What is prop drilling?](#55-what-is-prop-drilling)
- [56: What is Context in React?](#56-what-is-context-in-react)
- [57: How do you create and use Context?](#57-how-do-you-create-and-use-context)
- [58: How do you set default values for props?](#58-how-do-you-set-default-values-for-props)
- [59: What are PropTypes and are they still used?](#59-what-are-proptypes-and-are-they-still-used)
- [60: How do you pass a function as a prop?](#60-how-do-you-pass-a-function-as-a-prop)
- [61: How does data flow in React?](#61-how-does-data-flow-in-react)
- [62: What is `StrictMode`?](#62-what-is-strictmode)
- [63: Why does my component render twice or my effect run twice in development?](#63-why-does-my-component-render-twice-or-my-effect-run-twice-in-development)
- [64: What is Create React App and should you still use it?](#64-what-is-create-react-app-and-should-you-still-use-it)
- [65: How do you start a new React project today?](#65-how-do-you-start-a-new-react-project-today)
- [66: What is Vite?](#66-what-is-vite)
- [67: What is a React framework like Next.js?](#67-what-is-a-react-framework-like-nextjs)
- [68: How do you render raw HTML in React?](#68-how-do-you-render-raw-html-in-react)
- [69: How do you write comments in JSX?](#69-how-do-you-write-comments-in-jsx)
- [70: How do you use JavaScript expressions in JSX?](#70-how-do-you-use-javascript-expressions-in-jsx)
- [71: Can a component return `null`?](#71-can-a-component-return-null)
- [72: What can a component return?](#72-what-can-a-component-return)
- [73: What is component composition?](#73-what-is-component-composition)
- [74: Why must component names start with a capital letter?](#74-why-must-component-names-start-with-a-capital-letter)
- [75: What does it mean for a component to be pure?](#75-what-does-it-mean-for-a-component-to-be-pure)
- [76: What is a side effect?](#76-what-is-a-side-effect)
- [77: What are React Developer Tools?](#77-what-are-react-developer-tools)
- [78: What is the difference between `react` and `react-dom`?](#78-what-is-the-difference-between-react-and-react-dom)
- [79: What is React Native?](#79-what-is-react-native)
- [80: What is a single-page application (SPA)?](#80-what-is-a-single-page-application-spa)
- [81: How do you add routing to a React app?](#81-how-do-you-add-routing-to-a-react-app)
- [82: How do you pass all properties of an object as props?](#82-how-do-you-pass-all-properties-of-an-object-as-props)
- [83: How do you update an object in state?](#83-how-do-you-update-an-object-in-state)
- [84: How do you add, remove and update items in an array in state?](#84-how-do-you-add-remove-and-update-items-in-an-array-in-state)
- [85: Does calling the state setter change the value immediately?](#85-does-calling-the-state-setter-change-the-value-immediately)
- [86: What is batching?](#86-what-is-batching)
- [87: What causes a component to re-render?](#87-what-causes-a-component-to-re-render)
- [88: When a parent re-renders, do its children re-render too?](#88-when-a-parent-re-renders-do-its-children-re-render-too)
- [89: How can you reset a component's state?](#89-how-can-you-reset-a-components-state)
- [90: How do you show a loading indicator?](#90-how-do-you-show-a-loading-indicator)
- [91: What is an error boundary?](#91-what-is-an-error-boundary)
- [92: What is `lazy`?](#92-what-is-lazy)
- [93: What is Suspense?](#93-what-is-suspense)
- [94: What is `use` in React 19?](#94-what-is-use-in-react-19)
- [95: What is `useId`?](#95-what-is-useid)
- [96: How do you connect a label to an input in JSX?](#96-how-do-you-connect-a-label-to-an-input-in-jsx)
- [97: Which attribute names are different in JSX?](#97-which-attribute-names-are-different-in-jsx)
- [98: How do you handle several inputs with one change handler?](#98-how-do-you-handle-several-inputs-with-one-change-handler)
- [99: What is a form action in React 19?](#99-what-is-a-form-action-in-react-19)
- [100: What is a custom hook?](#100-what-is-a-custom-hook)
- [101: Write a simple `useToggle` hook.](#101-write-a-simple-usetoggle-hook)
- [102: Why shouldn't you put side effects directly in the component body?](#102-why-shouldnt-you-put-side-effects-directly-in-the-component-body)
- [103: How do you run code only once when a component mounts?](#103-how-do-you-run-code-only-once-when-a-component-mounts)
- [104: What is the difference between `useEffect(fn)`, `useEffect(fn, [])` and `useEffect(fn, [a])`?](#104-what-is-the-difference-between-useeffectfn-useeffectfn--and-useeffectfn-a)
- [105: What is `memo`?](#105-what-is-memo)
- [106: What is `useMemo`?](#106-what-is-usememo)
- [107: What is `useCallback`?](#107-what-is-usecallback)
- [108: What is the React Compiler?](#108-what-is-the-react-compiler)
- [109: What are React Server Components?](#109-what-are-react-server-components)
- [110: What does `"use client"` mean?](#110-what-does-use-client-mean)
- [111: What does `"use server"` mean?](#111-what-does-use-server-mean)
- [112: What is server-side rendering (SSR)?](#112-what-is-server-side-rendering-ssr)
- [113: What is client-side rendering (CSR)?](#113-what-is-client-side-rendering-csr)
- [114: What is hydration?](#114-what-is-hydration)
- [115: What is a portal?](#115-what-is-a-portal)
- [116: How do you build a simple modal?](#116-how-do-you-build-a-simple-modal)
- [117: How do you set the page title in React 19?](#117-how-do-you-set-the-page-title-in-react-19)
- [118: How do you test a React component?](#118-how-do-you-test-a-react-component)
- [119: What are Jest and Vitest?](#119-what-are-jest-and-vitest)
- [120: How do you type props with TypeScript?](#120-how-do-you-type-props-with-typescript)
- [121: How do you type `useState` in TypeScript?](#121-how-do-you-type-usestate-in-typescript)
- [122: How do you type event handlers in TypeScript?](#122-how-do-you-type-event-handlers-in-typescript)
- [123: How can components share logic?](#123-how-can-components-share-logic)
- [124: Should you use inheritance between components?](#124-should-you-use-inheritance-between-components)
- [125: What is a higher-order component (HOC)?](#125-what-is-a-higher-order-component-hoc)
- [126: What is the render props pattern?](#126-what-is-the-render-props-pattern)
- [127: How do you use environment variables in a React app?](#127-how-do-you-use-environment-variables-in-a-react-app)
- [128: Is React a library or a framework?](#128-is-react-a-library-or-a-framework)
- [129: How do you debug a React app?](#129-how-do-you-debug-a-react-app)
- [130: How do you use images in a React app?](#130-how-do-you-use-images-in-a-react-app)
- [131: What does the warning "Each child in a list should have a unique key prop" mean?](#131-what-does-the-warning-each-child-in-a-list-should-have-a-unique-key-prop-mean)
- [132: How do you add CSS classes conditionally?](#132-how-do-you-add-css-classes-conditionally)
- [133: What are CSS Modules?](#133-what-are-css-modules)
- [134: How do you use Tailwind CSS with React?](#134-how-do-you-use-tailwind-css-with-react)
- [135: Write a counter component with increment, decrement and reset.](#135-write-a-counter-component-with-increment-decrement-and-reset)
- [136: Why does `console.log` right after `setState` show the old value?](#136-why-does-consolelog-right-after-setstate-show-the-old-value)
- [137: How do you avoid an infinite loop in `useEffect`?](#137-how-do-you-avoid-an-infinite-loop-in-useeffect)
- [138: How do you keep the previous value of a prop or state?](#138-how-do-you-keep-the-previous-value-of-a-prop-or-state)
- [139: How do you focus an input when a component appears?](#139-how-do-you-focus-an-input-when-a-component-appears)
- [140: What is the difference between `onClick={handleClick}` and `onClick={handleClick()}`?](#140-what-is-the-difference-between-onclickhandleclick-and-onclickhandleclick)
- [141: Why did class components need `this.handleClick = this.handleClick.bind(this)`?](#141-why-did-class-components-need-thishandleclick--thishandleclickbindthis)
- [142: What are lifecycle methods?](#142-what-are-lifecycle-methods)
- [143: How do class lifecycle methods map to hooks?](#143-how-do-class-lifecycle-methods-map-to-hooks)
- [144: What is the difference between `value` and `defaultValue`?](#144-what-is-the-difference-between-value-and-defaultvalue)
- [145: What is a ref callback?](#145-what-is-a-ref-callback)
- [146: Is `setState` asynchronous?](#146-is-setstate-asynchronous)
- [147: How do you read form values on submit without controlled inputs?](#147-how-do-you-read-form-values-on-submit-without-controlled-inputs)
- [148: How does a child send data to its parent?](#148-how-does-a-child-send-data-to-its-parent)
- [149: What are some common beginner mistakes in React?](#149-what-are-some-common-beginner-mistakes-in-react)
- [150: What are the main differences between React 18 and React 19?](#150-what-are-the-main-differences-between-react-18-and-react-19)

### Moderate Questions (151-300)

- [151: How does React's diffing algorithm work?](#151-how-does-reacts-diffing-algorithm-work)
- [152: What is React Fiber?](#152-what-is-react-fiber)
- [153: What is the difference between the render phase and the commit phase?](#153-what-is-the-difference-between-the-render-phase-and-the-commit-phase)
- [154: What are the steps React goes through to show something on screen?](#154-what-are-the-steps-react-goes-through-to-show-something-on-screen)
- [155: What does "state as a snapshot" mean?](#155-what-does-state-as-a-snapshot-mean)
- [156: What is automatic batching?](#156-what-is-automatic-batching)
- [157: What is `flushSync` and when would you use it?](#157-what-is-flushsync-and-when-would-you-use-it)
- [158: What does this code render after one click, and why?](#158-what-does-this-code-render-after-one-click-and-why)
- [159: What is `useReducer`?](#159-what-is-usereducer)
- [160: When should you use `useReducer` instead of `useState`?](#160-when-should-you-use-usereducer-instead-of-usestate)
- [161: How do you combine `useReducer` with Context?](#161-how-do-you-combine-usereducer-with-context)
- [162: What is lazy initial state?](#162-what-is-lazy-initial-state)
- [163: How do you lazily initialize `useReducer`?](#163-how-do-you-lazily-initialize-usereducer)
- [164: What is the difference between `useEffect` and `useLayoutEffect`?](#164-what-is-the-difference-between-useeffect-and-uselayouteffect)
- [165: What is `useInsertionEffect`?](#165-what-is-useinsertioneffect)
- [166: When do you NOT need an effect?](#166-when-do-you-not-need-an-effect)
- [167: What is derived state and how should you handle it?](#167-what-is-derived-state-and-how-should-you-handle-it)
- [168: How do you reset all state in a component when a prop changes?](#168-how-do-you-reset-all-state-in-a-component-when-a-prop-changes)
- [169: How do you adjust some state when a prop changes, without an effect?](#169-how-do-you-adjust-some-state-when-a-prop-changes-without-an-effect)
- [170: What is a stale closure in React?](#170-what-is-a-stale-closure-in-react)
- [171: What is a race condition in data fetching and how do you avoid it?](#171-what-is-a-race-condition-in-data-fetching-and-how-do-you-avoid-it)
- [172: How do you cancel a fetch request when a component unmounts or a dependency changes?](#172-how-do-you-cancel-a-fetch-request-when-a-component-unmounts-or-a-dependency-changes)
- [173: What is `useEffectEvent`?](#173-what-is-useeffectevent)
- [174: How should you deal with effects running twice in Strict Mode?](#174-how-should-you-deal-with-effects-running-twice-in-strict-mode)
- [175: When is `useCallback` actually useful?](#175-when-is-usecallback-actually-useful)
- [176: When is `useMemo` actually useful?](#176-when-is-usememo-actually-useful)
- [177: How do you use a custom comparison function with `memo`?](#177-how-do-you-use-a-custom-comparison-function-with-memo)
- [178: Why does `memo` sometimes not prevent re-renders?](#178-why-does-memo-sometimes-not-prevent-re-renders)
- [179: How does the React Compiler work, and does it replace `useMemo` and `useCallback`?](#179-how-does-the-react-compiler-work-and-does-it-replace-usememo-and-usecallback)
- [180: How do you enable the React Compiler?](#180-how-do-you-enable-the-react-compiler)
- [181: What rules does your code need to follow for the React Compiler to work?](#181-what-rules-does-your-code-need-to-follow-for-the-react-compiler-to-work)
- [182: Why can Context cause performance problems?](#182-why-can-context-cause-performance-problems)
- [183: How can you split Context to reduce re-renders?](#183-how-can-you-split-context-to-reduce-re-renders)
- [184: When should you use Context and when a state management library?](#184-when-should-you-use-context-and-when-a-state-management-library)
- [185: How does Redux Toolkit work with React?](#185-how-does-redux-toolkit-work-with-react)
- [186: What is Zustand?](#186-what-is-zustand)
- [187: Why use TanStack Query (React Query) instead of fetching in `useEffect`?](#187-why-use-tanstack-query-react-query-instead-of-fetching-in-useeffect)
- [188: What is the difference between server state and client state?](#188-what-is-the-difference-between-server-state-and-client-state)
- [189: What are Actions in React 19?](#189-what-are-actions-in-react-19)
- [190: What is `useActionState`?](#190-what-is-useactionstate)
- [191: What is `useFormStatus`?](#191-what-is-useformstatus)
- [192: What is `useOptimistic`?](#192-what-is-useoptimistic)
- [193: How does form reset work with React 19 form actions?](#193-how-does-form-reset-work-with-react-19-form-actions)
- [194: What is `useTransition`?](#194-what-is-usetransition)
- [195: What is the difference between `startTransition` and `useTransition`?](#195-what-is-the-difference-between-starttransition-and-usetransition)
- [196: How do async transitions work in React 19, and what is the caveat?](#196-how-do-async-transitions-work-in-react-19-and-what-is-the-caveat)
- [197: What is `useDeferredValue`?](#197-what-is-usedeferredvalue)
- [198: What does the `initialValue` argument of `useDeferredValue` do?](#198-what-does-the-initialvalue-argument-of-usedeferredvalue-do)
- [199: How are transitions different from debouncing or throttling?](#199-how-are-transitions-different-from-debouncing-or-throttling)
- [200: How does `use` work with promises?](#200-how-does-use-work-with-promises)
- [201: How is `use(Context)` different from `useContext`?](#201-how-is-usecontext-different-from-usecontext)
- [202: How does Suspense work for data fetching?](#202-how-does-suspense-work-for-data-fetching)
- [203: How do nested Suspense boundaries work?](#203-how-do-nested-suspense-boundaries-work)
- [204: How do you stop Suspense from replacing content that's already on the screen with a fallback?](#204-how-do-you-stop-suspense-from-replacing-content-thats-already-on-the-screen-with-a-fallback)
- [205: How do you lazy load a component that uses a named export?](#205-how-do-you-lazy-load-a-component-that-uses-a-named-export)
- [206: How do you split code by route?](#206-how-do-you-split-code-by-route)
- [207: How do you write an error boundary?](#207-how-do-you-write-an-error-boundary)
- [208: What errors do error boundaries NOT catch?](#208-what-errors-do-error-boundaries-not-catch)
- [209: What is `react-error-boundary`?](#209-what-is-react-error-boundary)
- [210: What are `onCaughtError`, `onUncaughtError` and `onRecoverableError`?](#210-what-are-oncaughterror-onuncaughterror-and-onrecoverableerror)
- [211: How do refs work for function components in React 19?](#211-how-do-refs-work-for-function-components-in-react-19)
- [212: What is `useImperativeHandle`?](#212-what-is-useimperativehandle)
- [213: What are ref callback cleanup functions?](#213-what-are-ref-callback-cleanup-functions)
- [214: When should you use a ref and when state?](#214-when-should-you-use-a-ref-and-when-state)
- [215: How do you build a stopwatch with refs?](#215-how-do-you-build-a-stopwatch-with-refs)
- [216: Write a `useDebounce` hook.](#216-write-a-usedebounce-hook)
- [217: Write a `useLocalStorage` hook.](#217-write-a-uselocalstorage-hook)
- [218: Write a `useOnlineStatus` hook.](#218-write-a-useonlinestatus-hook)
- [219: What is `useSyncExternalStore`?](#219-what-is-usesyncexternalstore)
- [220: Do two components using the same custom hook share state?](#220-do-two-components-using-the-same-custom-hook-share-state)
- [221: Should every function that starts with `use` be a hook?](#221-should-every-function-that-starts-with-use-be-a-hook)
- [222: What is the compound components pattern?](#222-what-is-the-compound-components-pattern)
- [223: Why did hooks mostly replace render props and HOCs?](#223-why-did-hooks-mostly-replace-render-props-and-hocs)
- [224: Are higher-order components still used?](#224-are-higher-order-components-still-used)
- [225: How do you build a component that can be both controlled and uncontrolled?](#225-how-do-you-build-a-component-that-can-be-both-controlled-and-uncontrolled)
- [226: How does event bubbling work with portals?](#226-how-does-event-bubbling-work-with-portals)
- [227: Can components inside a portal read context from above?](#227-can-components-inside-a-portal-read-context-from-above)
- [228: Why shouldn't you use random values as keys?](#228-why-shouldnt-you-use-random-values-as-keys)
- [229: Do keys need to be unique across the whole app?](#229-do-keys-need-to-be-unique-across-the-whole-app)
- [230: How does React decide whether to keep or reset a component's state?](#230-how-does-react-decide-whether-to-keep-or-reset-a-components-state)
- [231: Why shouldn't you define a component inside another component?](#231-why-shouldnt-you-define-a-component-inside-another-component)
- [232: What happens to state when you conditionally render something before a component?](#232-what-happens-to-state-when-you-conditionally-render-something-before-a-component)
- [233: Why are `Children` and `cloneElement` considered legacy?](#233-why-are-children-and-cloneelement-considered-legacy)
- [234: How does React 19 handle `<title>`, `<meta>` and `<link>` tags?](#234-how-does-react-19-handle-title-meta-and-link-tags)
- [235: How does React 19 handle stylesheets?](#235-how-does-react-19-handle-stylesheets)
- [236: How does React 19 handle async scripts?](#236-how-does-react-19-handle-async-scripts)
- [237: What are `preload`, `preinit`, `preconnect` and `prefetchDNS`?](#237-what-are-preload-preinit-preconnect-and-prefetchdns)
- [238: How is the Context provider written in React 19?](#238-how-is-the-context-provider-written-in-react-19)
- [239: Which APIs were removed in React 19?](#239-which-apis-were-removed-in-react-19)
- [240: How do you upgrade an app to React 19?](#240-how-do-you-upgrade-an-app-to-react-19)
- [241: What changed in TypeScript types with React 19?](#241-what-changed-in-typescript-types-with-react-19)
- [242: How do you type the `children` prop?](#242-how-do-you-type-the-children-prop)
- [243: How do you type a component that wraps a native element and accepts all its props?](#243-how-do-you-type-a-component-that-wraps-a-native-element-and-accepts-all-its-props)
- [244: How do you write a generic component in TypeScript?](#244-how-do-you-write-a-generic-component-in-typescript)
- [245: How do you type `useReducer` actions?](#245-how-do-you-type-usereducer-actions)
- [246: How do you type a Context that has no sensible default value?](#246-how-do-you-type-a-context-that-has-no-sensible-default-value)
- [247: Which queries should you prefer in React Testing Library?](#247-which-queries-should-you-prefer-in-react-testing-library)
- [248: How do you simulate user interactions in tests?](#248-how-do-you-simulate-user-interactions-in-tests)
- [249: How do you test asynchronous UI?](#249-how-do-you-test-asynchronous-ui)
- [250: How do you mock API calls in React tests?](#250-how-do-you-mock-api-calls-in-react-tests)
- [251: How do you test a custom hook?](#251-how-do-you-test-a-custom-hook)
- [252: What is `act()`?](#252-what-is-act)
- [253: What happened to `react-test-renderer`?](#253-what-happened-to-react-test-renderer)
- [254: What is the `<Profiler>` component?](#254-what-is-the-profiler-component)
- [255: How do you find out why a component re-renders?](#255-how-do-you-find-out-why-a-component-re-renders)
- [256: What is list virtualization?](#256-what-is-list-virtualization)
- [257: How do you debounce a search input that calls an API?](#257-how-do-you-debounce-a-search-input-that-calls-an-api)
- [258: What's wrong with chaining effects that set state?](#258-whats-wrong-with-chaining-effects-that-set-state)
- [259: What are the main differences between Server Components and Client Components?](#259-what-are-the-main-differences-between-server-components-and-client-components)
- [260: What props can a Server Component pass to a Client Component?](#260-what-props-can-a-server-component-pass-to-a-client-component)
- [261: How can a Client Component render a Server Component?](#261-how-can-a-client-component-render-a-server-component)
- [262: What are Server Functions?](#262-what-are-server-functions)
- [263: What security issues should you think about with Server Functions?](#263-what-security-issues-should-you-think-about-with-server-functions)
- [264: How does streaming SSR work?](#264-how-does-streaming-ssr-work)
- [265: What are common causes of hydration mismatches?](#265-what-are-common-causes-of-hydration-mismatches)
- [266: What is `suppressHydrationWarning`?](#266-what-is-suppresshydrationwarning)
- [267: What is `hydrateRoot`?](#267-what-is-hydrateroot)
- [268: Why is `useId` important for server rendering?](#268-why-is-useid-important-for-server-rendering)
- [269: What is `<Activity>`?](#269-what-is-activity)
- [270: How is `<Activity>` different from conditional rendering?](#270-how-is-activity-different-from-conditional-rendering)
- [271: How do Next.js and React Server Components relate?](#271-how-do-nextjs-and-react-server-components-relate)
- [272: How do loaders and actions work in React Router v7?](#272-how-do-loaders-and-actions-work-in-react-router-v7)
- [273: What are fetch-on-render and render-as-you-fetch?](#273-what-are-fetch-on-render-and-render-as-you-fetch)
- [274: What is a network waterfall and how do you avoid it?](#274-what-is-a-network-waterfall-and-how-do-you-avoid-it)
- [275: How do you update deeply nested state without a lot of spreading?](#275-how-do-you-update-deeply-nested-state-without-a-lot-of-spreading)
- [276: What are good rules for structuring state?](#276-what-are-good-rules-for-structuring-state)
- [277: What is state normalization?](#277-what-is-state-normalization)
- [278: What is state colocation?](#278-what-is-state-colocation)
- [279: How do you make React apps accessible?](#279-how-do-you-make-react-apps-accessible)
- [280: How do you manage focus when opening and closing a modal?](#280-how-do-you-manage-focus-when-opening-and-closing-a-modal)
- [281: How does event propagation work in React?](#281-how-does-event-propagation-work-in-react)
- [282: Where does React attach its event listeners?](#282-where-does-react-attach-its-event-listeners)
- [283: How is React's `onChange` different from the native `change` event?](#283-how-is-reacts-onchange-different-from-the-native-change-event)
- [284: When should you use uncontrolled inputs?](#284-when-should-you-use-uncontrolled-inputs)
- [285: Why is a file input always uncontrolled?](#285-why-is-a-file-input-always-uncontrolled)
- [286: Why does the cursor jump to the end of a controlled input?](#286-why-does-the-cursor-jump-to-the-end-of-a-controlled-input)
- [287: How do you handle global UI state like toasts and modals?](#287-how-do-you-handle-global-ui-state-like-toasts-and-modals)
- [288: How do you add internationalization (i18n) to a React app?](#288-how-do-you-add-internationalization-i18n-to-a-react-app)
- [289: How do you write code that only runs in development?](#289-how-do-you-write-code-that-only-runs-in-development)
- [290: How do you protect routes in a client-side React app?](#290-how-do-you-protect-routes-in-a-client-side-react-app)
- [291: How do you implement infinite scroll?](#291-how-do-you-implement-infinite-scroll)
- [292: Write a hook that tracks the window size.](#292-write-a-hook-that-tracks-the-window-size)
- [293: What are common causes of memory leaks in React apps?](#293-what-are-common-causes-of-memory-leaks-in-react-apps)
- [294: How do you animate list items entering and leaving?](#294-how-do-you-animate-list-items-entering-and-leaving)
- [295: How do you use a non-React library (like a chart or map library) inside a component?](#295-how-do-you-use-a-non-react-library-like-a-chart-or-map-library-inside-a-component)
- [296: How do you protect against XSS in React?](#296-how-do-you-protect-against-xss-in-react)
- [297: What does React do with `javascript:` URLs?](#297-what-does-react-do-with-javascript-urls)
- [298: How do you handle errors from async code in event handlers?](#298-how-do-you-handle-errors-from-async-code-in-event-handlers)
- [299: How would you structure folders in a medium-sized React project?](#299-how-would-you-structure-folders-in-a-medium-sized-react-project)
- [300: Why shouldn't you disable the `react-hooks/exhaustive-deps` lint rule?](#300-why-shouldnt-you-disable-the-react-hooksexhaustive-deps-lint-rule)

### Advanced Questions (301-450)

- [301: How does the Fiber architecture work in more detail?](#301-how-does-the-fiber-architecture-work-in-more-detail)
- [302: What are lanes in React?](#302-what-are-lanes-in-react)
- [303: What does concurrent rendering actually mean?](#303-what-does-concurrent-rendering-actually-mean)
- [304: How does React yield to the browser during rendering?](#304-how-does-react-yield-to-the-browser-during-rendering)
- [305: When does React skip rendering a component (bailout)?](#305-when-does-react-skip-rendering-a-component-bailout)
- [306: Why does a component sometimes render once more even when I set state to the same value?](#306-why-does-a-component-sometimes-render-once-more-even-when-i-set-state-to-the-same-value)
- [307: How are hooks stored internally?](#307-how-are-hooks-stored-internally)
- [308: Why do hooks need to be called in the same order every render?](#308-why-do-hooks-need-to-be-called-in-the-same-order-every-render)
- [309: What is tearing and how does `useSyncExternalStore` prevent it?](#309-what-is-tearing-and-how-does-usesyncexternalstore-prevent-it)
- [310: What is `getServerSnapshot` for?](#310-what-is-getserversnapshot-for)
- [311: Why should state libraries use `useSyncExternalStore` instead of `useState` + `useEffect` subscriptions?](#311-why-should-state-libraries-use-usesyncexternalstore-instead-of-usestate--useeffect-subscriptions)
- [312: How does Suspense work internally?](#312-how-does-suspense-work-internally)
- [313: Why can't you create the promise inside the component that calls `use`?](#313-why-cant-you-create-the-promise-inside-the-component-that-calls-use)
- [314: What changed about Suspense sibling rendering in React 19?](#314-what-changed-about-suspense-sibling-rendering-in-react-19)
- [315: What is selective hydration?](#315-what-is-selective-hydration)
- [316: What happens to user events that fire before hydration finishes?](#316-what-happens-to-user-events-that-fire-before-hydration-finishes)
- [317: What is the RSC payload?](#317-what-is-the-rsc-payload)
- [318: How do bundlers handle `"use client"` boundaries?](#318-how-do-bundlers-handle-use-client-boundaries)
- [319: Why must props passed from Server to Client Components be serializable?](#319-why-must-props-passed-from-server-to-client-components-be-serializable)
- [320: How does calling a Server Function work under the hood?](#320-how-does-calling-a-server-function-work-under-the-hood)
- [321: How do forms with Server Functions support progressive enhancement?](#321-how-do-forms-with-server-functions-support-progressive-enhancement)
- [322: What is `cache` in React?](#322-what-is-cache-in-react)
- [323: What is `cacheSignal`?](#323-what-is-cachesignal)
- [324: What is Partial Pre-rendering in React 19.2?](#324-what-is-partial-pre-rendering-in-react-192)
- [325: What is the difference between `prerender` and `renderToReadableStream`?](#325-what-is-the-difference-between-prerender-and-rendertoreadablestream)
- [326: What are the limitations of `renderToString`?](#326-what-are-the-limitations-of-rendertostring)
- [327: How do you handle errors in streaming SSR?](#327-how-do-you-handle-errors-in-streaming-ssr)
- [328: How did hydration error handling improve in React 19?](#328-how-did-hydration-error-handling-improve-in-react-19)
- [329: What exactly happens inside a hidden `<Activity>`?](#329-what-exactly-happens-inside-a-hidden-activity)
- [330: What are the rules and limits of `useEffectEvent`?](#330-what-are-the-rules-and-limits-of-useeffectevent)
- [331: How do you build an optimistic update that rolls back on error?](#331-how-do-you-build-an-optimistic-update-that-rolls-back-on-error)
- [332: Why do state updates after `await` inside `startTransition` lose their transition status?](#332-why-do-state-updates-after-await-inside-starttransition-lose-their-transition-status)
- [333: How does `useActionState` handle multiple quick submissions?](#333-how-does-useactionstate-handle-multiple-quick-submissions)
- [334: How would you design a simple data fetching layer that works with Suspense?](#334-how-would-you-design-a-simple-data-fetching-layer-that-works-with-suspense)
- [335: How do you avoid waterfalls in Server Components?](#335-how-do-you-avoid-waterfalls-in-server-components)
- [336: How do you pass a promise from a Server Component to a Client Component?](#336-how-do-you-pass-a-promise-from-a-server-component-to-a-client-component)
- [337: How do you let users retry after an error in a Suspense-based component?](#337-how-do-you-let-users-retry-after-an-error-in-a-suspense-based-component)
- [338: How do errors in Server Components work?](#338-how-do-errors-in-server-components-work)
- [339: How does the React Compiler work internally?](#339-how-does-the-react-compiler-work-internally)
- [340: How do you adopt the React Compiler gradually or opt out?](#340-how-do-you-adopt-the-react-compiler-gradually-or-opt-out)
- [341: When does the React Compiler skip a component?](#341-when-does-the-react-compiler-skip-a-component)
- [342: How do the newer `eslint-plugin-react-hooks` rules relate to the compiler?](#342-how-do-the-newer-eslint-plugin-react-hooks-rules-relate-to-the-compiler)
- [343: Why can using objects as effect dependencies cause problems, and what are the options?](#343-why-can-using-objects-as-effect-dependencies-cause-problems-and-what-are-the-options)
- [344: How would you build a small global store with selectors using `useSyncExternalStore`?](#344-how-would-you-build-a-small-global-store-with-selectors-using-usesyncexternalstore)
- [345: Why doesn't Context support selectors, and how do people work around it?](#345-why-doesnt-context-support-selectors-and-how-do-people-work-around-it)
- [346: How can you avoid re-rendering expensive children when a parent's state changes, without `memo`?](#346-how-can-you-avoid-re-rendering-expensive-children-when-a-parents-state-changes-without-memo)
- [347: What are React Performance Tracks?](#347-what-are-react-performance-tracks)
- [348: What information does the Profiler's `onRender` callback give you?](#348-what-information-does-the-profilers-onrender-callback-give-you)
- [349: What should you watch out for when building a virtualized list?](#349-what-should-you-watch-out-for-when-building-a-virtualized-list)
- [350: How do you speed up a slow list that doesn't need virtualization?](#350-how-do-you-speed-up-a-slow-list-that-doesnt-need-virtualization)
- [351: How can closures cause memory issues in React?](#351-how-can-closures-cause-memory-issues-in-react)
- [352: What is the issue with `useLayoutEffect` and server rendering?](#352-what-is-the-issue-with-uselayouteffect-and-server-rendering)
- [353: What are the pitfalls of `flushSync`?](#353-what-are-the-pitfalls-of-flushsync)
- [354: How do you position a tooltip based on its own size without flicker?](#354-how-do-you-position-a-tooltip-based-on-its-own-size-without-flicker)
- [355: How would you design an imperative API for a component with `useImperativeHandle`?](#355-how-would-you-design-an-imperative-api-for-a-component-with-useimperativehandle)
- [356: How do you observe an element's size when the element can mount and unmount?](#356-how-do-you-observe-an-elements-size-when-the-element-can-mount-and-unmount)
- [357: How do you build an accessible modal without the native `<dialog>` element?](#357-how-do-you-build-an-accessible-modal-without-the-native-dialog-element)
- [358: What is a custom React renderer?](#358-what-is-a-custom-react-renderer)
- [359: How does React Native's New Architecture relate to React?](#359-how-does-react-natives-new-architecture-relate-to-react)
- [360: What exactly does Strict Mode do in React 19?](#360-what-exactly-does-strict-mode-do-in-react-19)
- [361: What does it mean for an effect to be "resilient to remounting"?](#361-what-does-it-mean-for-an-effect-to-be-resilient-to-remounting)
- [362: What are owner stacks and `captureOwnerStack`?](#362-what-are-owner-stacks-and-captureownerstack)
- [363: How does React 19 report errors differently from React 18?](#363-how-does-react-19-report-errors-differently-from-react-18)
- [364: Why must rendering be pure for concurrent features to work?](#364-why-must-rendering-be-pure-for-concurrent-features-to-work)
- [365: Why shouldn't you read or write `ref.current` during render?](#365-why-shouldnt-you-read-or-write-refcurrent-during-render)
- [366: What can go wrong if you mutate props or state?](#366-what-can-go-wrong-if-you-mutate-props-or-state)
- [367: How do you make sure secrets never reach Client Components?](#367-how-do-you-make-sure-secrets-never-reach-client-components)
- [368: What are the `server-only` and `client-only` packages?](#368-what-are-the-server-only-and-client-only-packages)
- [369: Do you need `"use client"` in every interactive component?](#369-do-you-need-use-client-in-every-interactive-component)
- [370: Can a Client Component import a Server Component?](#370-can-a-client-component-import-a-server-component)
- [371: Can you use Context in Server Components?](#371-can-you-use-context-in-server-components)
- [372: How does streaming work with Server Components and Suspense?](#372-how-does-streaming-work-with-server-components-and-suspense)
- [373: How do you refresh data on the page after a Server Function mutates it?](#373-how-do-you-refresh-data-on-the-page-after-a-server-function-mutates-it)
- [374: How do you return validation errors from a form action?](#374-how-do-you-return-validation-errors-from-a-form-action)
- [375: Why does `useFormStatus` return `pending: false` in my form?](#375-why-does-useformstatus-return-pending-false-in-my-form)
- [376: How do you have several buttons in one form that do different things?](#376-how-do-you-have-several-buttons-in-one-form-that-do-different-things)
- [377: How do you combine `useOptimistic` with `useActionState`?](#377-how-do-you-combine-useoptimistic-with-useactionstate)
- [378: How do you avoid flashing spinners for fast transitions?](#378-how-do-you-avoid-flashing-spinners-for-fast-transitions)
- [379: What changed about revealing Suspense boundaries during SSR in React 19.2?](#379-what-changed-about-revealing-suspense-boundaries-during-ssr-in-react-192)
- [380: What is `<ViewTransition>`?](#380-what-is-viewtransition)
- [381: How do routers use transitions?](#381-how-do-routers-use-transitions)
- [382: When should you use `useDeferredValue` instead of `useTransition`?](#382-when-should-you-use-usedeferredvalue-instead-of-usetransition)
- [383: Can concurrent rendering cause problems with layout effects or refs?](#383-can-concurrent-rendering-cause-problems-with-layout-effects-or-refs)
- [384: How do you render content that depends on the browser (like `localStorage` or the current time) without hydration errors?](#384-how-do-you-render-content-that-depends-on-the-browser-like-localstorage-or-the-current-time-without-hydration-errors)
- [385: How do you detect whether code is running on the client after hydration without an extra state variable?](#385-how-do-you-detect-whether-code-is-running-on-the-client-after-hydration-without-an-extra-state-variable)
- [386: How would you build a modal manager that can open modals from anywhere?](#386-how-would-you-build-a-modal-manager-that-can-open-modals-from-anywhere)
- [387: How would you build accessible Tabs as compound components?](#387-how-would-you-build-accessible-tabs-as-compound-components)
- [388: How do you type a polymorphic component (an `as` prop) in TypeScript?](#388-how-do-you-type-a-polymorphic-component-an-as-prop-in-typescript)
- [389: How do you type a component that accepts a `ref` in React 19?](#389-how-do-you-type-a-component-that-accepts-a-ref-in-react-19)
- [390: How do you type a generic custom hook so callers get good inference?](#390-how-do-you-type-a-generic-custom-hook-so-callers-get-good-inference)
- [391: How do you type a Server Function used as a form action?](#391-how-do-you-type-a-server-function-used-as-a-form-action)
- [392: How do you use discriminated unions for component props?](#392-how-do-you-use-discriminated-unions-for-component-props)
- [393: How do you test components that use `use()` and Suspense?](#393-how-do-you-test-components-that-use-use-and-suspense)
- [394: How do you test Server Components?](#394-how-do-you-test-server-components)
- [395: What is a good testing strategy for a large React app?](#395-what-is-a-good-testing-strategy-for-a-large-react-app)
- [396: How do you test an error boundary?](#396-how-do-you-test-an-error-boundary)
- [397: What are the challenges of micro-frontends with React?](#397-what-are-the-challenges-of-micro-frontends-with-react)
- [398: Can you have multiple React roots on one page, and how do they share state?](#398-can-you-have-multiple-react-roots-on-one-page-and-how-do-they-share-state)
- [399: How do you add React to an existing non-React page?](#399-how-do-you-add-react-to-an-existing-non-react-page)
- [400: How do you unmount a React root?](#400-how-do-you-unmount-a-react-root)
- [401: How does React 19 support Web Components (custom elements)?](#401-how-does-react-19-support-web-components-custom-elements)
- [402: Which React events behave differently from native DOM events?](#402-which-react-events-behave-differently-from-native-dom-events)
- [403: Why can't you call `preventDefault()` in a React `onWheel` or `onTouchMove` handler?](#403-why-cant-you-call-preventdefault-in-a-react-onwheel-or-ontouchmove-handler)
- [404: What does "A component is changing an uncontrolled input to be controlled" mean?](#404-what-does-a-component-is-changing-an-uncontrolled-input-to-be-controlled-mean)
- [405: How would you implement undo and redo?](#405-how-would-you-implement-undo-and-redo)
- [406: When would you use a state machine for UI state?](#406-when-would-you-use-a-state-machine-for-ui-state)
- [407: Without the compiler, how would you cache an expensive calculation that many components need?](#407-without-the-compiler-how-would-you-cache-an-expensive-calculation-that-many-components-need)
- [408: How do you keep a large form fast?](#408-how-do-you-keep-a-large-form-fast)
- [409: What does "Too many re-renders" mean?](#409-what-does-too-many-re-renders-mean)
- [410: When is it okay to set state during render?](#410-when-is-it-okay-to-set-state-during-render)
- [411: What are the costs of resetting a component with `key`?](#411-what-are-the-costs-of-resetting-a-component-with-key)
- [412: Why does a component keep its state when you swap it with a ternary?](#412-why-does-a-component-keep-its-state-when-you-swap-it-with-a-ternary)
- [413: Why is calling a HOC inside a component a bug?](#413-why-is-calling-a-hoc-inside-a-component-a-bug)
- [414: What problems do HOCs have with refs and static methods?](#414-what-problems-do-hocs-have-with-refs-and-static-methods)
- [415: How can you make lazy-loaded components load faster when the user needs them?](#415-how-can-you-make-lazy-loaded-components-load-faster-when-the-user-needs-them)
- [416: How do you analyze and reduce the bundle size of a React app?](#416-how-do-you-analyze-and-reduce-the-bundle-size-of-a-react-app)
- [417: What are the differences between React's development and production builds?](#417-what-are-the-differences-between-reacts-development-and-production-builds)
- [418: How do you handle authentication in an app with Server Components and Server Functions?](#418-how-do-you-handle-authentication-in-an-app-with-server-components-and-server-functions)
- [419: What happens in the UI when a Server Function throws?](#419-what-happens-in-the-ui-when-a-server-function-throws)
- [420: How do you use React's server rendering in edge runtimes?](#420-how-do-you-use-reacts-server-rendering-in-edge-runtimes)
- [421: What do `bootstrapScripts` and `bootstrapModules` do?](#421-what-do-bootstrapscripts-and-bootstrapmodules-do)
- [422: How does React 19 handle duplicate `<meta>` or `<title>` tags rendered by different components?](#422-how-does-react-19-handle-duplicate-meta-or-title-tags-rendered-by-different-components)
- [423: How do you start loading critical resources early in a Server Component?](#423-how-do-you-start-loading-critical-resources-early-in-a-server-component)
- [424: How does `fetchPriority` help in React apps?](#424-how-does-fetchpriority-help-in-react-apps)
- [425: Are updates outside React event handlers batched?](#425-are-updates-outside-react-event-handlers-batched)
- [426: How can you use Web Workers with React?](#426-how-can-you-use-web-workers-with-react)
- [427: How do you run high-frequency animations without re-rendering on every frame?](#427-how-do-you-run-high-frequency-animations-without-re-rendering-on-every-frame)
- [428: How do you integrate a library like D3 that wants to control the DOM?](#428-how-do-you-integrate-a-library-like-d3-that-wants-to-control-the-dom)
- [429: How do you debug "Maximum update depth exceeded"?](#429-how-do-you-debug-maximum-update-depth-exceeded)
- [430: What does "Cannot update a component while rendering a different component" mean?](#430-what-does-cannot-update-a-component-while-rendering-a-different-component-mean)
- [431: What does "Rendered more hooks than during the previous render" mean?](#431-what-does-rendered-more-hooks-than-during-the-previous-render-mean)
- [432: What does "Objects are not valid as a React child" mean?](#432-what-does-objects-are-not-valid-as-a-react-child-mean)
- [433: What happens when two list items have the same key?](#433-what-happens-when-two-list-items-have-the-same-key)
- [434: What causes "Invalid hook call"?](#434-what-causes-invalid-hook-call)
- [435: How do you safely put initial data into server-rendered HTML?](#435-how-do-you-safely-put-initial-data-into-server-rendered-html)
- [436: Does `useEffect` always run after the browser paints?](#436-does-useeffect-always-run-after-the-browser-paints)
- [437: In what order do effects and cleanups run between parents and children?](#437-in-what-order-do-effects-and-cleanups-run-between-parents-and-children)
- [438: What are headless components?](#438-what-are-headless-components)
- [439: How would you design the API of a reusable component library?](#439-how-would-you-design-the-api-of-a-reusable-component-library)
- [440: How do you handle internationalization with Server Components?](#440-how-do-you-handle-internationalization-with-server-components)
- [441: How would you organize state in a large React application?](#441-how-would-you-organize-state-in-a-large-react-application)
- [442: What was the December 2025 React Server Components vulnerability, and what does it teach?](#442-what-was-the-december-2025-react-server-components-vulnerability-and-what-does-it-teach)
- [443: How would you approach a slow React app?](#443-how-would-you-approach-a-slow-react-app)
- [444: How do you choose between CSR, SSR, SSG and Server Components?](#444-how-do-you-choose-between-csr-ssr-ssg-and-server-components)
- [445: How would you migrate a large codebase from React 17 to React 19?](#445-how-would-you-migrate-a-large-codebase-from-react-17-to-react-19)
- [446: How do you migrate a Create React App project to Vite?](#446-how-do-you-migrate-a-create-react-app-project-to-vite)
- [447: Which React features are still experimental at the time of writing?](#447-which-react-features-are-still-experimental-at-the-time-of-writing)
- [448: How do Suspense, transitions and error boundaries work together during a navigation?](#448-how-do-suspense-transitions-and-error-boundaries-work-together-during-a-navigation)
- [449: Can you still use class components in React 19?](#449-can-you-still-use-class-components-in-react-19)
- [450: Explain what happens from a `setState` call to pixels on the screen.](#450-explain-what-happens-from-a-setstate-call-to-pixels-on-the-screen)

---

## Easy Questions (1-150)

### 1: What is React?

React is a JavaScript library for building user interfaces. You describe what the UI should look like for a given state, and React updates the DOM when that state changes. You build the UI out of small pieces called components.

React itself only cares about the UI. For routing, data fetching and server rendering you usually add other libraries or use a framework built on top of React, like Next.js or React Router.

### 2: Who created React and who maintains it now?

React was created by Jordan Walke at Facebook (now Meta) and was open sourced in 2013. For most of its life it was maintained by a team at Meta together with open source contributors. In 2025 the React team announced that React and React Native would move to the React Foundation, an independent foundation, so the project is no longer controlled by a single company.

### 3: What is the current major version of React?

At the time of writing it is React 19. React 19.0 came out in December 2024, and minor releases like 19.1 and 19.2 added more features such as `<Activity>`, `useEffectEvent` and owner stacks. When you answer this in an interview it's good to mention a few things React 19 added: Actions, `useActionState`, `useOptimistic`, the `use` API, `ref` as a normal prop, and support for `<title>` and `<meta>` tags inside components.

### 4: What are the main features of React?

- **Components**: the UI is split into reusable pieces.
- **JSX**: an HTML-like syntax for describing UI inside JavaScript.
- **Declarative**: you describe the result, not the steps to change the DOM.
- **One-way data flow**: data goes from parent to child through props.
- **Hooks**: functions like `useState` and `useEffect` that add state and other features to function components.
- **Virtual DOM and reconciliation**: React figures out the minimum DOM changes needed.
- **Concurrent rendering**: React can prepare updates in the background without blocking the UI.
- **Server Components**: components that run only on the server (when used with a framework that supports them).

### 5: What is JSX?

JSX is a syntax extension for JavaScript that looks like HTML. It lets you write markup inside your JavaScript code.

```jsx
function Greeting() {
  const name = "Anna";
  return <h1>Hello, {name}!</h1>;
}
```

Browsers don't understand JSX, so a compiler like Babel, SWC or esbuild turns it into normal JavaScript function calls before the code runs.

### 6: Is JSX required to use React?

No. JSX is just a nicer way to write calls to create elements. You could write the same thing without it:

```jsx
import { createElement } from "react";

function Greeting() {
  return createElement("h1", null, "Hello!");
}
```

In practice almost everyone uses JSX because it is much easier to read.

### 7: What does JSX compile to?

With the modern JSX transform (React 17 and later), this:

```jsx
const el = <h1 className="title">Hi</h1>;
```

compiles to roughly this:

```js
import { jsx as _jsx } from "react/jsx-runtime";
const el = _jsx("h1", { className: "title", children: "Hi" });
```

The result is a plain JavaScript object called a React element that describes what to show on the screen.

### 8: Why don't we need to write `import React from "react"` at the top of every file anymore?

The old JSX transform turned JSX into `React.createElement(...)`, so `React` had to be in scope. Since React 17 the new JSX transform imports the helper functions from `react/jsx-runtime` automatically. You only import what you actually use, like `useState`.

### 9: What is a component?

A component is a JavaScript function that returns markup (JSX). It's a reusable piece of UI that can have its own logic and state.

```jsx
function Button() {
  return <button>Click me</button>;
}

function App() {
  return (
    <div>
      <Button />
      <Button />
    </div>
  );
}
```

### 10: What is the difference between function components and class components? Which one should you use?

Class components are ES6 classes that extend `React.Component` and use lifecycle methods like `componentDidMount`. Function components are plain functions and use hooks for state and side effects.

```jsx
// Class component
class Counter extends React.Component {
  state = { count: 0 };
  render() {
    return (
      <button onClick={() => this.setState({ count: this.state.count + 1 })}>
        {this.state.count}
      </button>
    );
  }
}

// Function component
function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

For new code you should use function components. They are shorter, easier to reuse logic with (custom hooks), and all new React features are built for them. Class components still work, and the only thing you still need a class for is an error boundary (unless you use a library for it).

### 11: How do you create a function component?

Write a function whose name starts with a capital letter and return JSX from it.

```jsx
export default function ProfileCard() {
  return (
    <div className="card">
      <img src="/avatar.png" alt="User avatar" />
      <p>John Smith</p>
    </div>
  );
}
```

You can also use an arrow function: `const ProfileCard = () => <div>...</div>;`

### 12: What are props?

Props (short for properties) are the inputs of a component. A parent passes them to a child, similar to HTML attributes.

```jsx
function Avatar({ name, size }) {
  return <img src={`/img/${name}.png`} width={size} alt={name} />;
}

function App() {
  return <Avatar name="lin" size={64} />;
}
```

Props can be any JavaScript value: strings, numbers, objects, arrays, functions and even other JSX.

### 13: Can a component change its own props?

No. Props are read-only. A component should never modify the props it receives. If something needs to change over time, it should be state, either in the component itself or in a parent that passes a new value down.

```jsx
function Price({ amount }) {
  amount = amount * 2; // don't do this
  return <span>{amount}</span>;
}
```

If you need a different value, create a new variable: `const doubled = amount * 2;`.

### 14: What is state?

State is data that belongs to a component and can change over time. When state changes, React renders the component again so the screen shows the new value.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>Clicked {count} times</button>
  );
}
```

Regular local variables don't work for this, because they reset on every render and changing them doesn't tell React to re-render.

### 15: What is the difference between props and state?

| Props                          | State                                                                     |
| ------------------------------ | ------------------------------------------------------------------------- |
| Passed in from the parent      | Owned by the component itself                                             |
| Read-only inside the component | Can be changed with a setter function                                     |
| Used to configure a component  | Used for values that change over time (user input, toggles, fetched data) |

A common pattern is that one component holds a value in state and passes it to its children as props.

### 16: What is `useState`?

`useState` is a hook that adds a state variable to a function component. It returns an array with two items: the current value and a function to update it.

```jsx
const [name, setName] = useState("");
```

The argument is the initial value. It's only used on the first render. When you call `setName("Bob")`, React stores the new value and re-renders the component.

### 17: Why shouldn't you modify state directly?

React doesn't watch your variables. It only knows something changed when you call the setter function. If you mutate state directly, React won't re-render, and even if something else causes a render, you can get bugs because the old and new values are the same object.

```jsx
// Wrong
user.name = "Bob";
setUser(user); // same object, React may skip the update

// Right
setUser({ ...user, name: "Bob" });
```

### 18: How do you update state based on the previous state?

Pass a function to the setter. React calls it with the latest state value.

```jsx
setCount((prev) => prev + 1);
```

This matters when you update the same state several times in a row or when the update happens later (for example in a timeout), because `count` in your code might be an old value.

### 19: What is the Virtual DOM?

The Virtual DOM is a term for the lightweight JavaScript objects (React elements) that describe the UI. When state changes, React creates a new tree of these objects, compares it with the previous one, and then updates only the parts of the real DOM that changed.

The React docs don't use the term much anymore, but the idea is the same: changing plain objects is cheap, changing the real DOM is more expensive, so React works out the changes first and then applies them.

### 20: What is reconciliation?

Reconciliation is the process React uses to compare the new element tree with the previous one and decide what needs to change in the DOM. If an element has the same type in the same position, React keeps it and updates its props. If the type changes (for example `<div>` becomes `<span>`), React removes the old one and creates a new one. Keys help React match items in lists.

### 21: What is a React element?

A React element is a plain object that describes what you want to see on the screen. JSX creates elements.

```jsx
const element = <h1 className="title">Hello</h1>;
// roughly: { type: "h1", props: { className: "title", children: "Hello" }, ... }
```

Elements are immutable. Once created you don't change them; React creates new ones on every render.

### 22: What is the difference between an element and a component?

A component is a function (or class) that returns elements. An element is the object that comes out of it, describing one piece of UI.

```jsx
function Hello() {
  // component
  return <p>Hi</p>; // <p>Hi</p> is an element
}

const el = <Hello />; // also an element, with type: Hello
```

Think of a component as a recipe and an element as one description that the recipe produced.

### 23: How do you render a React app into the page?

Use `createRoot` from `react-dom/client` and call `render` on it.

```jsx
import { createRoot } from "react-dom/client";
import App from "./App";

const root = createRoot(document.getElementById("root"));
root.render(<App />);
```

The old `ReactDOM.render` was removed in React 19, so you will get an error if you try to use it.

### 24: What is the `root` element in a React app?

It's a normal DOM node in your HTML file, usually `<div id="root"></div>`, where React puts the whole app. React manages everything inside that node. You normally have one root per app, but you can have several if you add React to parts of an existing page.

### 25: What are Fragments?

A component has to return a single parent element. If you don't want to add an extra `<div>` to the DOM, wrap the elements in a Fragment.

```jsx
function Columns() {
  return (
    <>
      <td>Name</td>
      <td>Age</td>
    </>
  );
}
```

`<>...</>` is the short syntax. It doesn't add anything to the DOM.

### 26: When do you need `<Fragment>` instead of `<>`?

When you need to pass a `key`, for example when rendering a list where each item returns several elements. The short syntax doesn't accept props.

```jsx
import { Fragment } from "react";

function Glossary({ items }) {
  return (
    <dl>
      {items.map((item) => (
        <Fragment key={item.id}>
          <dt>{item.term}</dt>
          <dd>{item.description}</dd>
        </Fragment>
      ))}
    </dl>
  );
}
```

### 27: How do you render a list in React?

Use `map` to turn an array of data into an array of elements. Give each item a `key`.

```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  );
}
```

### 28: What are keys and why are they needed?

A key is a special prop that tells React which item in a list is which. When the list changes (items added, removed or reordered), React uses keys to match old items with new ones, so it can keep their state and DOM nodes instead of recreating everything.

Keys must be unique among siblings and should stay the same between renders. An ID from your data is usually the best choice.

### 29: Why is using the array index as a key a bad idea?

If the list can be reordered, filtered, or have items inserted in the middle, the index of an item changes. React then thinks the item at index 0 is the same item as before, even though it's different data. This can cause wrong state in inputs, broken animations and slower updates.

Using the index is OK only when the list is static and never reordered or filtered.

### 30: How do you render something conditionally?

You use normal JavaScript: `if`, the ternary operator, or `&&`.

```jsx
function Status({ isOnline }) {
  if (!isOnline) {
    return <p>Offline</p>;
  }
  return <p>Online</p>;
}

function Message({ unread }) {
  return (
    <div>
      {unread > 0 ? (
        <span>{unread} new messages</span>
      ) : (
        <span>No messages</span>
      )}
    </div>
  );
}
```

### 31: What is the problem with `{count && <Badge />}`?

If `count` is `0`, the expression evaluates to `0`, and React renders the number `0` on the screen. `false`, `null` and `undefined` render nothing, but numbers do render.

```jsx
// Shows "0" when count is 0
{
  count && <Badge count={count} />;
}

// Fix
{
  count > 0 && <Badge count={count} />;
}
```

### 32: How do you handle events in React?

Pass a function to an event prop written in camelCase, like `onClick` or `onChange`.

```jsx
function SaveButton() {
  function handleClick() {
    alert("Saved!");
  }
  return <button onClick={handleClick}>Save</button>;
}
```

Pass the function itself, don't call it: `onClick={handleClick}`, not `onClick={handleClick()}`.

### 33: What is a synthetic event?

React wraps the browser's native event in its own object called a SyntheticEvent. It has the same interface as the native event (`target`, `preventDefault()`, `stopPropagation()` and so on) and works the same way across browsers. If you need the original browser event, you can use `e.nativeEvent`.

### 34: How do you pass arguments to an event handler?

Wrap the call in an arrow function.

```jsx
function List({ items, onDelete }) {
  return items.map((item) => (
    <button key={item.id} onClick={() => onDelete(item.id)}>
      Delete {item.name}
    </button>
  ));
}
```

### 35: How do you prevent the default browser behavior?

Call `e.preventDefault()` in the handler. Returning `false` doesn't work in React.

```jsx
function SearchForm() {
  function handleSubmit(e) {
    e.preventDefault(); // stop the page reload
    // do the search
  }
  return (
    <form onSubmit={handleSubmit}>
      <input name="q" />
      <button>Search</button>
    </form>
  );
}
```

### 36: What is the `children` prop?

`children` holds whatever you put between the opening and closing tag of a component. It lets you build wrapper components.

```jsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}

function App() {
  return (
    <Card>
      <h2>Title</h2>
      <p>Some text</p>
    </Card>
  );
}
```

### 37: How can you style React components?

There are several common options:

- Plain CSS files with `className`
- CSS Modules (`Button.module.css`) for locally scoped class names
- Utility CSS like Tailwind
- CSS-in-JS libraries (styled-components, Emotion), though runtime CSS-in-JS doesn't work well with Server Components
- Inline styles with the `style` prop for small dynamic values

```jsx
import "./Button.css";

function Button() {
  return <button className="primary-button">OK</button>;
}
```

### 38: Why do we use `className` instead of `class` in JSX?

JSX is JavaScript, and `class` is a reserved word in JavaScript. JSX also follows the DOM property names, and the DOM property is `element.className`. The same goes for `htmlFor` instead of `for` on labels.

### 39: How do you write inline styles in React?

Pass an object to the `style` prop. Property names are camelCase and values are usually strings. Numbers are treated as pixels for most properties.

```jsx
function Box({ color }) {
  return (
    <div style={{ backgroundColor: color, padding: 16, fontSize: "1.2rem" }}>
      Hello
    </div>
  );
}
```

The double braces are just a JavaScript object inside a JSX expression.

### 40: What is a controlled component?

A controlled component is a form input whose value comes from React state. Every change goes through an `onChange` handler that updates the state.

```jsx
function NameInput() {
  const [name, setName] = useState("");
  return <input value={name} onChange={(e) => setName(e.target.value)} />;
}
```

React state is the single source of truth, so you can validate, format or reset the value easily.

### 41: What is an uncontrolled component?

An uncontrolled input keeps its own value in the DOM. React doesn't track every keystroke. You set a starting value with `defaultValue` and read the value when you need it, for example on submit.

```jsx
function SignupForm() {
  function handleSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    console.log(formData.get("email"));
  }
  return (
    <form onSubmit={handleSubmit}>
      <input name="email" defaultValue="" />
      <button>Sign up</button>
    </form>
  );
}
```

Uncontrolled inputs are simpler and work well with React 19 form actions.

### 42: How do you handle a text input in React?

The most common way is a controlled input: keep the value in state and update it in `onChange`.

```jsx
function Search() {
  const [query, setQuery] = useState("");
  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <p>You typed: {query}</p>
    </>
  );
}
```

### 43: How do you handle checkboxes and select elements?

For checkboxes use `checked` instead of `value`. For `<select>`, put `value` on the `<select>` itself, not `selected` on an `<option>`.

```jsx
function Settings() {
  const [agree, setAgree] = useState(false);
  const [color, setColor] = useState("red");

  return (
    <>
      <input
        type="checkbox"
        checked={agree}
        onChange={(e) => setAgree(e.target.checked)}
      />
      <select value={color} onChange={(e) => setColor(e.target.value)}>
        <option value="red">Red</option>
        <option value="blue">Blue</option>
      </select>
    </>
  );
}
```

### 44: What is `useEffect`?

`useEffect` lets you run code after React has updated the screen. You use it to sync your component with something outside React: a network request, a subscription, a timer, or a browser API.

```jsx
useEffect(() => {
  document.body.style.overflow = isOpen ? "hidden" : "";
}, [isOpen]);
```

The first argument is the effect function, the second is the dependency array.

### 45: How does the dependency array of `useEffect` work?

React runs the effect after the first render and then again only when one of the values in the array has changed since the last render. React compares each value with `Object.is`.

```jsx
useEffect(() => {
  fetchUser(userId);
}, [userId]); // re-run when userId changes
```

You should list every reactive value (props, state, and values computed from them) that the effect uses. The `eslint-plugin-react-hooks` linter checks this for you.

### 46: What is the cleanup function in `useEffect`?

If the effect returns a function, React calls it before running the effect again and when the component is removed from the screen. You use it to undo what the effect did.

```jsx
useEffect(() => {
  const id = setInterval(() => setSeconds((s) => s + 1), 1000);
  return () => clearInterval(id);
}, []);
```

Without cleanup you can get memory leaks, duplicate subscriptions or timers that keep running.

### 47: How do you fetch data with `useEffect`?

```jsx
function User({ id }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    let ignore = false;
    fetch(`/api/users/${id}`)
      .then((res) => res.json())
      .then((data) => {
        if (!ignore) setUser(data);
      });
    return () => {
      ignore = true;
    };
  }, [id]);

  if (!user) return <p>Loading...</p>;
  return <h1>{user.name}</h1>;
}
```

The `ignore` flag stops an old response from overwriting a newer one if `id` changes quickly. In real apps it's usually better to use a framework's data loading or a library like TanStack Query, which handles caching, retries and race conditions for you.

### 48: What are hooks?

Hooks are functions that start with `use` and let function components use React features: state (`useState`), side effects (`useEffect`), context (`useContext`), refs (`useRef`) and more. They were added in React 16.8. You can also write your own hooks to reuse logic.

### 49: What are the rules of hooks?

1. Only call hooks at the top level of a component or custom hook. Don't call them inside loops, conditions, nested functions or after an early `return`.
2. Only call hooks from React function components or custom hooks, not from regular JavaScript functions or class components.

React relies on the order of hook calls to know which state belongs to which hook, so the order must be the same on every render. The `use` API is an exception: it can be called inside conditions and loops.

### 50: Can you use hooks in class components?

No. Hooks only work in function components and custom hooks. If you need hook-based logic in a class component, you can wrap the class with a small function component that calls the hook and passes the result down as props.

### 51: What is `useRef`?

`useRef` gives you an object with a `current` property that keeps its value between renders. Changing `ref.current` does not cause a re-render.

```jsx
const countRef = useRef(0);
countRef.current += 1; // no re-render
```

Common uses are holding a DOM node, a timer ID, or any value you need to keep but don't want to show on screen.

### 52: How do you access a DOM element in React?

Create a ref and pass it to the `ref` attribute of the element. After React puts the element on the page, `ref.current` points to the DOM node.

```jsx
function SearchBox() {
  const inputRef = useRef(null);

  return (
    <>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  );
}
```

### 53: What is the difference between `useRef` and `useState`?

| `useState`                           | `useRef`                                                        |
| ------------------------------------ | --------------------------------------------------------------- |
| Changing it re-renders the component | Changing it does not re-render                                  |
| Value is a snapshot for each render  | `current` is mutable and always the latest                      |
| Use for data shown on the screen     | Use for DOM nodes, timer IDs, and values not used for rendering |

Don't read or write `ref.current` during rendering (except for lazy initialization). Use it in event handlers and effects.

### 54: What is lifting state up?

When two components need the same data, you move the state to their closest common parent and pass it down as props, along with functions to change it.

```jsx
function Parent() {
  const [value, setValue] = useState("");
  return (
    <>
      <Input value={value} onChange={setValue} />
      <Preview text={value} />
    </>
  );
}
```

Now both children always show the same value.

### 55: What is prop drilling?

Prop drilling is when you pass props through several layers of components that don't use them, only to get the data to a deeply nested child.

```jsx
<App user={user}>
  <Layout user={user}>
    <Sidebar user={user}>
      <Avatar user={user} />
```

It works, but it gets annoying. You can avoid it with composition (passing JSX as children) or with Context.

### 56: What is Context in React?

Context lets a parent component make a value available to all components below it in the tree, without passing it through props at every level. It's good for things like the current theme, the logged-in user or the language.

### 57: How do you create and use Context?

```jsx
import { createContext, useContext, useState } from "react";

const ThemeContext = createContext("light");

function App() {
  const [theme, setTheme] = useState("dark");
  return (
    <ThemeContext value={theme}>
      <Toolbar />
    </ThemeContext>
  );
}

function Toolbar() {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Toolbar</div>;
}
```

In React 19 you can render `<ThemeContext>` directly as the provider. Before React 19 you had to write `<ThemeContext.Provider>`, which still works but will be deprecated later.

### 58: How do you set default values for props?

Use default values in destructuring.

```jsx
function Button({ size = "medium", variant = "primary", children }) {
  return <button className={`${size} ${variant}`}>{children}</button>;
}
```

`defaultProps` on function components was removed in React 19. It still works on class components.

### 59: What are PropTypes and are they still used?

PropTypes was a way to check prop types at runtime in development. In React 19 the checks for `propTypes` were removed from React, so they are silently ignored. Today the standard way to type props is TypeScript.

```tsx
type ButtonProps = {
  label: string;
  onClick: () => void;
};

function Button({ label, onClick }: ButtonProps) {
  return <button onClick={onClick}>{label}</button>;
}
```

### 60: How do you pass a function as a prop?

Same as any other prop. This is how a child tells its parent that something happened.

```jsx
function Parent() {
  function handleSelect(item) {
    console.log("Selected", item);
  }
  return <ItemList onSelect={handleSelect} />;
}

function ItemList({ onSelect }) {
  return <button onClick={() => onSelect("apple")}>Apple</button>;
}
```

By convention, event props start with `on` and handlers start with `handle`.

### 61: How does data flow in React?

Data flows one way: from parent to child through props. A child can't change the parent's data directly. If it needs to, the parent passes down a function that the child calls. This makes it easier to understand where data comes from and to track down bugs.

### 62: What is `StrictMode`?

`<StrictMode>` is a component that turns on extra checks in development. It doesn't render anything visible and has no effect in production.

```jsx
createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

It renders components twice, runs effects twice and calls ref callbacks twice to help you find impure code and missing cleanup. It also warns about deprecated APIs.

### 63: Why does my component render twice or my effect run twice in development?

That's `StrictMode`. In development it calls your component function twice and mounts, unmounts and mounts the component again to make sure your code is pure and your effects clean up properly. If something breaks because of this, it usually means the effect is missing a cleanup function. This doesn't happen in production builds.

### 64: What is Create React App and should you still use it?

Create React App (CRA) was the official tool to start a React project. In February 2025 the React team deprecated it. It's no longer maintained, so you shouldn't use it for new projects. Existing CRA apps can migrate to a framework or a build tool like Vite.

### 65: How do you start a new React project today?

The React docs recommend starting with a framework:

- **Next.js** (App Router) for full-stack apps
- **React Router** (framework mode, v7)
- **Expo** for native apps

If you only need a client-side app, or want to set things up yourself, you can use a build tool like **Vite**, **Parcel** or **Rsbuild**:

```bash
npm create vite@latest my-app -- --template react-ts
```

### 66: What is Vite?

Vite is a build tool and development server. It starts very fast because in development it serves your source files as native ES modules, and it uses Rollup-based bundling for production. It has official templates for React and is the most popular choice for client-side React apps that don't use a framework.

### 67: What is a React framework like Next.js?

A framework is built on top of React and gives you things React itself doesn't: file-based routing, server rendering, data loading, bundling, and support for Server Components and Server Functions. Next.js and React Router are the most common ones. You still write React components, but the framework decides how the app is built and served.

### 68: How do you render raw HTML in React?

Use `dangerouslySetInnerHTML`. The name is long on purpose because it can open your app to XSS attacks if the HTML comes from users.

```jsx
function Article({ html }) {
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}
```

Only use it with HTML you trust or have sanitized, for example with DOMPurify.

### 69: How do you write comments in JSX?

Inside JSX use curly braces with a JavaScript block comment.

```jsx
return (
  <div>
    {/* This is a comment */}
    <p>Hello</p>
  </div>
);
```

### 70: How do you use JavaScript expressions in JSX?

Put them in curly braces. Any expression works: variables, function calls, math, ternaries.

```jsx
const user = { first: "Ann", last: "Lee" };

<p>
  {user.first} {user.last} is {2026 - 1990} years old.
  {user.isAdmin ? " (admin)" : ""}
</p>;
```

Statements like `if` and `for` can't go inside JSX directly. Use them before the `return` or use ternaries and `map`.

### 71: Can a component return `null`?

Yes. Returning `null` means the component renders nothing.

```jsx
function Warning({ show }) {
  if (!show) return null;
  return <div className="warning">Careful!</div>;
}
```

### 72: What can a component return?

- JSX elements
- Strings and numbers (rendered as text)
- Arrays of elements (each needs a key)
- Fragments
- `null`, `undefined`, `true`, `false` (render nothing)
- Portals

Plain objects can't be rendered. You get the error "Objects are not valid as a React child".

### 73: What is component composition?

Composition means building bigger components out of smaller ones, often by passing components or JSX as props.

```jsx
function Layout({ sidebar, children }) {
  return (
    <div className="layout">
      <aside>{sidebar}</aside>
      <main>{children}</main>
    </div>
  );
}

<Layout sidebar={<Menu />}>
  <Dashboard />
</Layout>;
```

This is the main way to reuse UI in React.

### 74: Why must component names start with a capital letter?

JSX uses the first letter to decide what you mean. Lowercase tags like `<div>` are treated as HTML elements. Capitalized tags like `<Header>` are treated as variables pointing to components. If you name a component `header`, React will try to render an HTML `<header>` tag.

### 75: What does it mean for a component to be pure?

A pure component always returns the same JSX for the same props, state and context, and doesn't change anything outside itself while rendering. It doesn't modify variables that existed before rendering, doesn't mutate props, and doesn't make network requests during render.

```jsx
let guest = 0;

// Impure: changes an outside variable
function Cup() {
  guest = guest + 1;
  return <h2>Tea cup for guest #{guest}</h2>;
}

// Pure
function Cup({ guest }) {
  return <h2>Tea cup for guest #{guest}</h2>;
}
```

React expects components to be pure. It can then render them twice, skip renders, or pause rendering without bugs.

### 76: What is a side effect?

A side effect is anything a function does besides returning a value: changing the DOM manually, making a network request, writing to localStorage, setting a timer, logging. In React, side effects belong in event handlers or, if they need to happen because the component appeared on screen, in `useEffect`. They shouldn't happen during rendering.

### 77: What are React Developer Tools?

React DevTools is a browser extension (Chrome, Firefox, Edge) and a standalone app. It lets you look at the component tree, see each component's props, state and hooks, find out why a component rendered, and record performance with the Profiler tab.

### 78: What is the difference between `react` and `react-dom`?

`react` contains the core: components, hooks, elements, and the logic that doesn't depend on any platform. `react-dom` connects React to the browser DOM. It has `createRoot`, `createPortal`, `flushSync`, server rendering APIs (`react-dom/server`) and form hooks like `useFormStatus`. React Native uses `react` with a different renderer instead of `react-dom`.

### 79: What is React Native?

React Native lets you build native mobile apps (iOS and Android) using React. You write components the same way, but instead of `<div>` and `<span>` you use native components like `<View>` and `<Text>`. Hooks, state and props work the same as in React for the web.

### 80: What is a single-page application (SPA)?

An SPA loads one HTML page and then updates the content with JavaScript as the user navigates, without full page reloads. A client-side React app built with Vite is an SPA by default. The downside is that the first load needs the JavaScript before anything shows, which is why many apps also use server rendering.

### 81: How do you add routing to a React app?

React itself has no router. The most common choice is React Router. In a framework like Next.js, routing is based on files and folders.

```jsx
import { BrowserRouter, Routes, Route, Link } from "react-router";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
```

In React Router v7 you import from `react-router` (the separate `react-router-dom` package is no longer needed).

### 82: How do you pass all properties of an object as props?

Use the spread syntax.

```jsx
const user = { name: "Ann", age: 30 };

<Profile {...user} />;
// same as <Profile name="Ann" age={30} />
```

It's handy for forwarding props, but don't overuse it, because it makes it harder to see which props a component actually gets.

### 83: How do you update an object in state?

Create a new object with the spread syntax and change only what you need.

```jsx
const [form, setForm] = useState({ name: "", email: "" });

function handleNameChange(e) {
  setForm({ ...form, name: e.target.value });
}
```

For nested objects you need to copy each level that changes:

```jsx
setUser({
  ...user,
  address: { ...user.address, city: "Paris" },
});
```

### 84: How do you add, remove and update items in an array in state?

Use methods that return a new array instead of ones that mutate.

```jsx
// Add
setTodos([...todos, newTodo]);

// Remove
setTodos(todos.filter((t) => t.id !== id));

// Update one item
setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
```

Avoid `push`, `splice`, `sort` and `reverse` on the state array directly. For sorting, copy first (`[...todos].sort()`) or use `toSorted()`.

### 85: Does calling the state setter change the value immediately?

No. The setter schedules a re-render. Inside the current render the state variable keeps its old value.

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count); // still the old value
}
```

The new value shows up on the next render. If you need the new value right away in the same function, put it in a variable first.

### 86: What is batching?

React groups several state updates into one re-render. Since React 18 this happens everywhere: in event handlers, timeouts, promises and native event listeners.

```jsx
function handleClick() {
  setName("Ann");
  setAge(30);
  // only one re-render
}
```

### 87: What causes a component to re-render?

- Its state changes (through a setter or dispatch)
- Its parent re-renders
- A context it uses changes

Changing props alone isn't really a separate cause: props only change because the parent rendered again.

### 88: When a parent re-renders, do its children re-render too?

Yes, by default all children re-render, even if their props didn't change. This is usually fine because rendering is fast. If a child is slow, you can wrap it in `memo` so it skips rendering when its props are the same. The React Compiler can also do this automatically.

### 89: How can you reset a component's state?

Give it a different `key`. When the key changes, React treats it as a new component, throws away the old state and starts fresh.

```jsx
<ChatForm key={contactId} contact={contact} />
```

When the user switches contacts, the form's draft text is cleared automatically.

### 90: How do you show a loading indicator?

Keep a loading flag in state, or use Suspense with a data source that supports it.

```jsx
function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/users")
      .then((r) => r.json())
      .then((data) => setUsers(data))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading...</p>;
  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}
```

### 91: What is an error boundary?

An error boundary is a component that catches errors thrown while rendering its children and shows a fallback UI instead of crashing the whole app. Without one, an error during rendering removes the whole React tree from the screen.

```jsx
<ErrorBoundary fallback={<p>Something went wrong.</p>}>
  <Profile />
</ErrorBoundary>
```

Error boundaries have to be written as class components, or you can use the `react-error-boundary` package.

### 92: What is `lazy`?

`lazy` lets you load a component's code only when it's first rendered. This makes the initial bundle smaller.

```jsx
import { lazy, Suspense } from "react";

const Settings = lazy(() => import("./Settings"));

function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Settings />
    </Suspense>
  );
}
```

Call `lazy` at the top level of a module, not inside a component.

### 93: What is Suspense?

`<Suspense>` shows a fallback while something inside it is loading. That can be code loaded with `lazy`, data read with `use`, or data from a Suspense-enabled framework or library.

```jsx
<Suspense fallback={<Spinner />}>
  <Comments />
</Suspense>
```

When everything inside is ready, React replaces the fallback with the real content.

### 94: What is `use` in React 19?

`use` is an API that reads the value of a promise or a context.

```jsx
import { use } from "react";

function Message({ messagePromise }) {
  const message = use(messagePromise);
  return <p>{message}</p>;
}
```

If the promise isn't resolved yet, the component suspends and the closest `<Suspense>` shows its fallback. Unlike hooks, `use` can be called inside `if` statements and loops.

### 95: What is `useId`?

`useId` generates a unique ID that is the same on the server and the client. It's mainly for linking labels and inputs or for ARIA attributes.

```jsx
function EmailField() {
  const id = useId();
  return (
    <>
      <label htmlFor={id}>Email</label>
      <input id={id} type="email" />
    </>
  );
}
```

Don't use it for list keys.

### 96: How do you connect a label to an input in JSX?

Use `htmlFor` on the label (because `for` is a reserved word in JavaScript), or wrap the input inside the label.

```jsx
<label htmlFor="name">Name</label>
<input id="name" />

<label>
  Age <input type="number" />
</label>
```

### 97: Which attribute names are different in JSX?

Most attributes are written in camelCase:

- `class` → `className`
- `for` → `htmlFor`
- `tabindex` → `tabIndex`
- `onclick` → `onClick`
- `stroke-width` (SVG) → `strokeWidth`

The exceptions are `aria-*` and `data-*` attributes, which keep their dashes: `aria-label`, `data-id`.

### 98: How do you handle several inputs with one change handler?

Use the input's `name` attribute.

```jsx
function Form() {
  const [values, setValues] = useState({ first: "", last: "" });

  function handleChange(e) {
    const { name, value } = e.target;
    setValues((prev) => ({ ...prev, [name]: value }));
  }

  return (
    <>
      <input name="first" value={values.first} onChange={handleChange} />
      <input name="last" value={values.last} onChange={handleChange} />
    </>
  );
}
```

### 99: What is a form action in React 19?

In React 19 you can pass a function to the `action` prop of a `<form>`. React calls it with the form's `FormData` when the form is submitted. You don't need `e.preventDefault()`.

```jsx
function Newsletter() {
  async function subscribe(formData) {
    await fetch("/api/subscribe", {
      method: "POST",
      body: formData,
    });
  }

  return (
    <form action={subscribe}>
      <input name="email" type="email" />
      <button type="submit">Subscribe</button>
    </form>
  );
}
```

After the action finishes successfully, React resets uncontrolled fields in the form.

### 100: What is a custom hook?

A custom hook is a function whose name starts with `use` and that calls other hooks. It lets you reuse stateful logic between components.

```jsx
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);

  return width;
}

function Header() {
  const width = useWindowWidth();
  return <p>Window width: {width}</p>;
}
```

### 101: Write a simple `useToggle` hook.

```jsx
import { useState, useCallback } from "react";

function useToggle(initial = false) {
  const [on, setOn] = useState(initial);
  const toggle = useCallback(() => setOn((v) => !v), []);
  return [on, toggle];
}

function Panel() {
  const [open, toggleOpen] = useToggle();
  return (
    <>
      <button onClick={toggleOpen}>{open ? "Hide" : "Show"}</button>
      {open && <p>Details...</p>}
    </>
  );
}
```

### 102: Why shouldn't you put side effects directly in the component body?

The component body runs during rendering. React may render a component many times, render it twice in Strict Mode, or start a render and throw it away. If you make a network request or change the DOM there, it can happen more often than you expect or at the wrong time. Side effects belong in event handlers or `useEffect`.

### 103: How do you run code only once when a component mounts?

Use `useEffect` with an empty dependency array.

```jsx
useEffect(() => {
  console.log("Mounted");
  return () => console.log("Unmounted");
}, []);
```

Keep in mind that in development, Strict Mode runs it twice (mount, unmount, mount). Your code should handle that with proper cleanup. If you truly need something once per app load, put it outside the component at module level.

### 104: What is the difference between `useEffect(fn)`, `useEffect(fn, [])` and `useEffect(fn, [a])`?

- `useEffect(fn)`: runs after every render.
- `useEffect(fn, [])`: runs only after the first render (mount), and cleans up on unmount.
- `useEffect(fn, [a])`: runs after the first render and again when `a` changes.

### 105: What is `memo`?

`memo` wraps a component so it skips re-rendering when its props are the same as last time (compared with `Object.is` for each prop).

```jsx
import { memo } from "react";

const ExpensiveList = memo(function ExpensiveList({ items }) {
  return items.map((item) => <Row key={item.id} item={item} />);
});
```

It's a performance tool. Your code should work correctly without it.

### 106: What is `useMemo`?

`useMemo` caches the result of a calculation between renders. It recalculates only when a dependency changes.

```jsx
const visibleTodos = useMemo(
  () => todos.filter((t) => t.status === filter),
  [todos, filter],
);
```

Use it for expensive calculations or to keep an object reference stable. Don't add it everywhere. If you use the React Compiler, you rarely need to write it yourself.

### 107: What is `useCallback`?

`useCallback` caches a function between renders so you get the same function object until a dependency changes.

```jsx
const handleSubmit = useCallback(
  (data) => {
    post(`/product/${productId}/buy`, data);
  },
  [productId],
);
```

It's useful when you pass the function to a `memo` component or use it as an effect dependency. `useCallback(fn, deps)` is the same as `useMemo(() => fn, deps)`.

### 108: What is the React Compiler?

The React Compiler is a build-time tool (a Babel plugin) that automatically adds memoization to your components and hooks. It reached its stable 1.0 release in October 2025. With it you mostly don't need to write `useMemo`, `useCallback` and `memo` by hand. It only works correctly if your code follows the rules of React (pure components, no mutation of props and state, rules of hooks).

### 109: What are React Server Components?

Server Components are components that render ahead of time, on the server or at build time, and never ship their code to the browser. They can be `async` and read data directly from a database or file system.

```jsx
// Server Component (in a framework like Next.js)
export default async function Posts() {
  const posts = await db.posts.findMany();
  return (
    <ul>
      {posts.map((p) => (
        <li key={p.id}>{p.title}</li>
      ))}
    </ul>
  );
}
```

They can't use state, effects or browser APIs. You need a framework that supports them.

### 110: What does `"use client"` mean?

`"use client"` at the top of a file marks it as a client module. Components from that file (and everything it imports) are sent to the browser and can use state, effects and event handlers. It marks the boundary between Server Components and Client Components.

```jsx
"use client";

import { useState } from "react";

export default function LikeButton() {
  const [liked, setLiked] = useState(false);
  return <button onClick={() => setLiked(!liked)}>{liked ? "♥" : "♡"}</button>;
}
```

It doesn't mean "render only on the client". Client Components still get rendered to HTML on the server during SSR.

### 111: What does `"use server"` mean?

`"use server"` marks async functions as Server Functions that the client can call. When a Client Component calls one, the framework sends a request to the server, runs the function there, and returns the result.

```jsx
// actions.js
"use server";

export async function addComment(formData) {
  const text = formData.get("text");
  await db.comments.create({ text });
}
```

`"use server"` is not used to mark Server Components. Server Components don't need any directive.

### 112: What is server-side rendering (SSR)?

With SSR the server runs your React components and sends HTML to the browser. The user sees content before the JavaScript loads. Then React hydrates the page on the client to make it interactive. SSR helps with first load speed and SEO.

### 113: What is client-side rendering (CSR)?

With CSR the server sends an almost empty HTML file and a JavaScript bundle. The browser runs the JavaScript, and React builds the whole page in the browser. It's simple to host, but the user sees nothing useful until the JavaScript has loaded and run.

### 114: What is hydration?

Hydration is when React takes HTML that was rendered on the server and attaches event handlers and state to it on the client, so it becomes interactive. React expects the HTML to match what the client would render. If it doesn't, you get a hydration mismatch error.

```jsx
import { hydrateRoot } from "react-dom/client";

hydrateRoot(document.getElementById("root"), <App />);
```

### 115: What is a portal?

A portal renders children into a different DOM node, outside the parent component's DOM. The component still behaves like a normal child in the React tree (context and event bubbling work as usual).

```jsx
import { createPortal } from "react-dom";

function Modal({ children }) {
  return createPortal(<div className="modal">{children}</div>, document.body);
}
```

It's useful for modals, tooltips and dropdowns that would otherwise be clipped by `overflow: hidden` or `z-index` of a parent.

### 116: How do you build a simple modal?

```jsx
function App() {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button onClick={() => setOpen(true)}>Open</button>
      {open && (
        <Modal onClose={() => setOpen(false)}>
          <p>Hello from the modal</p>
        </Modal>
      )}
    </>
  );
}

function Modal({ children, onClose }) {
  return createPortal(
    <div className="backdrop" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.body,
  );
}
```

You can also use the native `<dialog>` element, which gives you focus handling and the Escape key for free.

### 117: How do you set the page title in React 19?

Render a `<title>` tag anywhere in your component. React 19 moves it into `<head>` for you. The same works for `<meta>` and `<link>`.

```jsx
function BlogPost({ post }) {
  return (
    <article>
      <title>{post.title}</title>
      <meta name="description" content={post.summary} />
      <h1>{post.title}</h1>
    </article>
  );
}
```

Before React 19 you needed a library like `react-helmet` for this.

### 118: How do you test a React component?

The common setup is Vitest or Jest with React Testing Library. You render the component, find elements the way a user would, interact with them and check the result.

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Counter from "./Counter";

test("increments the count", async () => {
  render(<Counter />);
  await userEvent.click(screen.getByRole("button", { name: /clicked 0/i }));
  expect(screen.getByRole("button")).toHaveTextContent("Clicked 1 times");
});
```

### 119: What are Jest and Vitest?

Both are JavaScript test runners. Jest has been the standard for years. Vitest is newer, uses Vite's config and transforms, is fast, and has a Jest-compatible API. For a Vite project, Vitest is usually the easier choice.

### 120: How do you type props with TypeScript?

Define a type or interface and use it for the props parameter.

```tsx
type CardProps = {
  title: string;
  description?: string;
  children: React.ReactNode;
};

function Card({ title, description, children }: CardProps) {
  return (
    <section>
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {children}
    </section>
  );
}
```

`React.FC` is not needed. Typing the props parameter directly is the common style now.

### 121: How do you type `useState` in TypeScript?

Usually TypeScript infers the type from the initial value. When the initial value doesn't tell the full story (like `null` or an empty array), pass the type explicitly.

```tsx
const [count, setCount] = useState(0); // number

type User = { id: number; name: string };
const [user, setUser] = useState<User | null>(null);
const [tags, setTags] = useState<string[]>([]);
```

### 122: How do you type event handlers in TypeScript?

React exports event types. The generic parameter is the element type.

```tsx
function Form() {
  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    console.log(e.target.value);
  }

  function handleClick(e: React.MouseEvent<HTMLButtonElement>) {
    console.log(e.clientX);
  }

  return (
    <>
      <input onChange={handleChange} />
      <button onClick={handleClick}>Go</button>
    </>
  );
}
```

If you write the handler inline, TypeScript infers the type for you.

### 123: How can components share logic?

- **Custom hooks** for stateful logic (the main way today)
- **Plain functions** for logic without state (formatting, calculations)
- **Composition** with `children` or props that take JSX
- Higher-order components and render props, which are older patterns you still see in some libraries

### 124: Should you use inheritance between components?

No. React recommends composition over inheritance. Instead of a `SpecialButton extends Button`, you make a `Button` that accepts props and children, and then build other components that render it with specific props.

```jsx
function Button({ variant = "default", ...props }) {
  return <button className={`btn btn-${variant}`} {...props} />;
}

function DangerButton(props) {
  return <Button variant="danger" {...props} />;
}
```

### 125: What is a higher-order component (HOC)?

A HOC is a function that takes a component and returns a new component with extra behavior.

```jsx
function withLogger(Component) {
  return function Logged(props) {
    useEffect(() => {
      console.log("Mounted", Component.name);
    }, []);
    return <Component {...props} />;
  };
}

const LoggedButton = withLogger(Button);
```

HOCs were common before hooks. Today custom hooks are usually a simpler way to share logic.

### 126: What is the render props pattern?

A component takes a function as a prop and calls it to decide what to render.

```jsx
function MouseTracker({ render }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return (
    <div onMouseMove={(e) => setPos({ x: e.clientX, y: e.clientY })}>
      {render(pos)}
    </div>
  );
}

<MouseTracker
  render={({ x, y }) => (
    <p>
      {x}, {y}
    </p>
  )}
/>;
```

Like HOCs, this is mostly replaced by custom hooks, but some libraries still use it.

### 127: How do you use environment variables in a React app?

It depends on the build tool. In Vite, variables in `.env` that start with `VITE_` are exposed through `import.meta.env`.

```js
// .env
VITE_API_URL=https://api.example.com

// code
const apiUrl = import.meta.env.VITE_API_URL;
```

In Next.js, only variables starting with `NEXT_PUBLIC_` are sent to the browser. Anything that reaches client code is visible to users, so never put secrets there.

### 128: Is React a library or a framework?

React calls itself a library. It handles rendering the UI, but doesn't decide how you do routing, data fetching or builds. Frameworks like Next.js and React Router add those parts. In interviews it's fine to say React is a UI library, and frameworks are built on top of it.

### 129: How do you debug a React app?

- React DevTools to inspect components, props, state and hooks
- `console.log` or the `debugger` statement
- Browser DevTools breakpoints (source maps map back to your code)
- The Profiler tab in React DevTools for performance
- Reading the error messages and component stacks React prints in development

### 130: How do you use images in a React app?

Put them in the `public` folder and reference them by path, or import them so the build tool handles them.

```jsx
import logo from "./logo.png";

function Header() {
  return (
    <>
      <img src={logo} alt="Company logo" />
      <img src="/banner.jpg" alt="Banner" />
    </>
  );
}
```

Always add an `alt` attribute. Frameworks like Next.js have their own `<Image>` component that resizes and lazy loads images.

### 131: What does the warning "Each child in a list should have a unique key prop" mean?

You rendered an array of elements without a `key` on each item, or some keys are duplicated. Add a stable unique key, usually the item's ID.

```jsx
{
  users.map((user) => <UserRow key={user.id} user={user} />);
}
```

The key goes on the outermost element returned from `map`, not on an element inside the child component.

### 132: How do you add CSS classes conditionally?

Build the class string with a template literal, or use a small helper like `clsx`.

```jsx
<button className={`btn ${isActive ? "btn-active" : ""}`}>Save</button>;

// with clsx
import clsx from "clsx";
<button
  className={clsx("btn", { "btn-active": isActive, "btn-disabled": disabled })}
>
  Save
</button>;
```

### 133: What are CSS Modules?

CSS Modules are CSS files where class names are scoped to the file. The build tool renames the classes so they don't clash with other components.

```jsx
// Button.module.css
.primary { background: blue; }

// Button.jsx
import styles from "./Button.module.css";

function Button() {
  return <button className={styles.primary}>OK</button>;
}
```

Vite and Next.js support them out of the box.

### 134: How do you use Tailwind CSS with React?

Tailwind gives you small utility classes that you put directly in `className`.

```jsx
function Alert({ children }) {
  return (
    <div className="rounded-md bg-yellow-100 p-4 text-yellow-800">
      {children}
    </div>
  );
}
```

There is no runtime cost because the CSS is generated at build time, so it works fine with Server Components.

### 135: Write a counter component with increment, decrement and reset.

```jsx
import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c - 1)}>-</button>
      <button onClick={() => setCount((c) => c + 1)}>+</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

### 136: Why does `console.log` right after `setState` show the old value?

Because state in a render is a fixed snapshot. Calling `setState` asks React to render again with the new value. The variable in the current function call doesn't change.

```jsx
function handleClick() {
  setCount(count + 1);
  console.log(count); // old value
}
```

If you want to see the new value, log it during render or in an effect that depends on it.

### 137: How do you avoid an infinite loop in `useEffect`?

An infinite loop usually happens when an effect sets state that is also in its dependency array, or when you have no dependency array and set state in the effect.

```jsx
// Infinite loop: runs after every render and causes a render
useEffect(() => {
  setCount(count + 1);
});

// Infinite loop: options is a new object every render
const options = { page: 1 };
useEffect(() => {
  fetchData(options).then(setData);
}, [options]);
```

Fixes: add correct dependencies, move objects inside the effect, or use primitive values like `page` as dependencies. Also ask whether you need the effect at all.

### 138: How do you keep the previous value of a prop or state?

One way is to store it in state and compare during render:

```jsx
function Price({ value }) {
  const [prev, setPrev] = useState(value);
  const [trend, setTrend] = useState(null);

  if (value !== prev) {
    setPrev(value);
    setTrend(value > prev ? "up" : "down");
  }

  return (
    <span>
      {value} {trend}
    </span>
  );
}
```

You'll also see a `usePrevious` hook that writes to a ref in an effect. That works, but reading refs during render goes against React's rules, so the state version is the one the docs suggest.

### 139: How do you focus an input when a component appears?

Use the `autoFocus` prop, or a ref with an effect.

```jsx
<input autoFocus />;

// or
function Search() {
  const ref = useRef(null);
  useEffect(() => {
    ref.current.focus();
  }, []);
  return <input ref={ref} />;
}
```

### 140: What is the difference between `onClick={handleClick}` and `onClick={handleClick()}`?

`onClick={handleClick}` passes the function, and React calls it when the user clicks. `onClick={handleClick()}` calls the function immediately during render and passes its return value. If `handleClick` sets state, this causes an infinite render loop ("Too many re-renders").

### 141: Why did class components need `this.handleClick = this.handleClick.bind(this)`?

In JavaScript class methods are not bound to the instance. When you pass `this.handleClick` as a callback, `this` is `undefined` when it's called. So people either bound methods in the constructor or used class field arrow functions:

```jsx
class Toggle extends React.Component {
  state = { on: false };
  handleClick = () => {
    this.setState({ on: !this.state.on });
  };
  render() {
    return (
      <button onClick={this.handleClick}>{this.state.on ? "On" : "Off"}</button>
    );
  }
}
```

Function components don't have this problem.

### 142: What are lifecycle methods?

Lifecycle methods are methods on class components that React calls at certain times:

- `constructor`: set up initial state
- `render`: return the UI
- `componentDidMount`: after the component is added to the DOM
- `componentDidUpdate`: after an update
- `componentWillUnmount`: before removal
- `shouldComponentUpdate`: decide whether to re-render
- `getDerivedStateFromError` and `componentDidCatch`: for error boundaries

Old methods like `componentWillMount` and `componentWillReceiveProps` are deprecated and only work with the `UNSAFE_` prefix.

### 143: How do class lifecycle methods map to hooks?

| Class                        | Hooks                                      |
| ---------------------------- | ------------------------------------------ |
| `constructor` / `this.state` | `useState`, `useReducer`                   |
| `componentDidMount`          | `useEffect(fn, [])`                        |
| `componentDidUpdate`         | `useEffect(fn, [deps])`                    |
| `componentWillUnmount`       | cleanup function returned from `useEffect` |
| `shouldComponentUpdate`      | `memo`                                     |
| instance variables           | `useRef`                                   |

It's not an exact match. Effects are better thought of as "keep this in sync with that", not as lifecycle events.

### 144: What is the difference between `value` and `defaultValue`?

`value` makes the input controlled: React sets the value on every render, and you must update it through `onChange`. `defaultValue` only sets the starting value, and after that the DOM keeps track of it (uncontrolled). For checkboxes the equivalents are `checked` and `defaultChecked`.

If you pass `value` without `onChange`, the input becomes read-only and React warns you.

### 145: What is a ref callback?

Instead of a ref object, you can pass a function to `ref`. React calls it with the DOM node when it's attached. In React 19 the function can return a cleanup function, which React calls when the node is removed.

```jsx
<div
  ref={(node) => {
    console.log("attached", node);
    return () => console.log("detached");
  }}
/>
```

### 146: Is `setState` asynchronous?

Not in the sense of returning a promise. Calling the setter doesn't update the variable right away. React queues the update and processes it with other updates before the next render. You can't `await` it. If you need to run code after the DOM updates, use an effect or a ref callback.

### 147: How do you read form values on submit without controlled inputs?

Use `FormData`. Give each input a `name`.

```jsx
function LoginForm() {
  function handleSubmit(e) {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    const email = data.get("email");
    const password = data.get("password");
    login(email, password);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" type="email" />
      <input name="password" type="password" />
      <button>Log in</button>
    </form>
  );
}
```

With React 19 form actions, the function receives `FormData` directly.

### 148: How does a child send data to its parent?

The parent passes a callback function as a prop, and the child calls it with the data.

```jsx
function Parent() {
  const [color, setColor] = useState("red");
  return <ColorPicker onPick={setColor} />;
}

function ColorPicker({ onPick }) {
  return <button onClick={() => onPick("blue")}>Blue</button>;
}
```

### 149: What are some common beginner mistakes in React?

- Mutating state or props instead of creating new objects
- Calling a handler instead of passing it: `onClick={doThing()}`
- Missing or unstable `key` values in lists
- Using effects for things that can be calculated during render
- Missing dependencies in `useEffect`
- Forgetting cleanup for timers and subscriptions
- Defining a component inside another component
- Rendering `0` with `&&`
- Expecting state to update immediately after calling the setter

### 150: What are the main differences between React 18 and React 19?

React 18 introduced concurrent rendering, automatic batching, transitions, Suspense on the server and `createRoot`. React 19 builds on that and adds:

- Actions: async functions in transitions, `<form action={fn}>`, `useActionState`, `useFormStatus`, `useOptimistic`
- The `use` API for promises and context
- `ref` as a regular prop for function components (no `forwardRef` needed)
- `<Context>` as a provider
- Ref callback cleanup functions
- `<title>`, `<meta>`, `<link>` support inside components, stylesheet and script handling
- Stable Server Components and Server Functions
- Better hydration error messages
- Removal of old APIs: `ReactDOM.render`, `hydrate`, `findDOMNode`, string refs, `propTypes` checks and `defaultProps` for function components

Later 19.x releases added `<Activity>`, `useEffectEvent`, `cacheSignal` and partial pre-rendering.

---

## Moderate Questions (151-300)

### 151: How does React's diffing algorithm work?

Comparing two arbitrary trees is expensive, so React uses two simple rules that make it fast (roughly O(n)):

1. **Different types produce different trees.** If an element changes from `<div>` to `<section>`, or from `<Header>` to `<Footer>`, React tears down the old subtree (including its state) and builds a new one.
2. **Keys identify children.** When comparing lists of children, React matches them by `key`. Without keys it matches them by position.

If the type is the same, React keeps the DOM node or component instance and only updates the changed props, then continues with the children.

### 152: What is React Fiber?

Fiber is the internal engine React has used since version 16. Each component instance in the tree has a "fiber" object that stores its type, props, state, hooks and links to its parent, child and sibling. Because work is split into small units (one fiber at a time), React can pause rendering, handle something more urgent, and continue later. This is what makes concurrent features like transitions and Suspense possible.

### 153: What is the difference between the render phase and the commit phase?

- **Render phase**: React calls your components to figure out what the UI should look like and compares it with the previous result. This phase must be pure. React may pause it, restart it or throw it away.
- **Commit phase**: React applies the changes to the DOM, attaches refs and runs layout effects. This phase is synchronous and can't be interrupted.

After the commit and after the browser paints, React runs regular `useEffect` effects.

### 154: What are the steps React goes through to show something on screen?

1. **Trigger**: an initial render (`root.render`) or a state update.
2. **Render**: React calls the component functions that need to update.
3. **Commit**: React updates the DOM with the differences.

Then the browser paints the screen. Rendering doesn't always lead to DOM changes. If the output is the same, React doesn't touch the DOM.

### 155: What does "state as a snapshot" mean?

Each render has its own fixed values of props and state. Event handlers and effects created in that render see those values, even if they run later.

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 5);
    setTimeout(() => {
      alert(count); // shows the value from when you clicked, not the new one
    }, 3000);
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

This is why `setCount(count + 1)` three times in a row only adds 1.

### 156: What is automatic batching?

Since React 18, all state updates that happen in the same tick are grouped into a single re-render, no matter where they come from: event handlers, promises, `setTimeout` or native event listeners. Before React 18, updates were only batched inside React event handlers.

```jsx
setTimeout(() => {
  setCount((c) => c + 1);
  setFlag((f) => !f);
  // React 18+: one render. React 17: two renders.
}, 1000);
```

### 157: What is `flushSync` and when would you use it?

`flushSync` from `react-dom` forces React to apply the updates inside it right away and update the DOM synchronously.

```jsx
import { flushSync } from "react-dom";

function handleAdd() {
  flushSync(() => {
    setTodos([...todos, newTodo]);
  });
  // DOM is updated here
  listRef.current.lastChild.scrollIntoView();
}
```

Use it rarely, for example when you need to measure or scroll the DOM right after an update, or when a browser API like `onbeforeprint` needs the DOM updated immediately. It hurts performance if overused.

### 158: What does this code render after one click, and why?

```jsx
function handleClick() {
  setNumber(number + 1);
  setNumber(number + 1);
  setNumber(number + 1);
}
```

It adds 1, not 3. `number` is the same snapshot value in all three calls, so each call says "set it to 0 + 1". With updater functions it adds 3:

```jsx
setNumber((n) => n + 1);
setNumber((n) => n + 1);
setNumber((n) => n + 1);
```

React puts the updaters in a queue and runs them in order during the next render, passing each one the result of the previous.

### 159: What is `useReducer`?

`useReducer` manages state with a reducer function: you dispatch actions, and the reducer returns the new state.

```jsx
function reducer(state, action) {
  switch (action.type) {
    case "added":
      return [...state, { id: action.id, text: action.text, done: false }];
    case "toggled":
      return state.map((t) =>
        t.id === action.id ? { ...t, done: !t.done } : t,
      );
    case "deleted":
      return state.filter((t) => t.id !== action.id);
    default:
      throw new Error("Unknown action: " + action.type);
  }
}

function TodoApp() {
  const [todos, dispatch] = useReducer(reducer, []);
  // dispatch({ type: "added", id: 1, text: "Buy milk" });
}
```

The reducer must be pure and must return new objects instead of mutating.

### 160: When should you use `useReducer` instead of `useState`?

- When the state has several related values that change together
- When many event handlers update the same state in different ways
- When the next state depends on the previous one in complex ways
- When you want to test the update logic separately (a reducer is a plain function)

For a simple toggle or input value, `useState` is easier.

### 161: How do you combine `useReducer` with Context?

Put the state and `dispatch` in context so any component in the tree can read and update it.

```jsx
const TasksContext = createContext(null);
const TasksDispatchContext = createContext(null);

function TasksProvider({ children }) {
  const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
  return (
    <TasksContext value={tasks}>
      <TasksDispatchContext value={dispatch}>{children}</TasksDispatchContext>
    </TasksContext>
  );
}

function AddTask() {
  const dispatch = useContext(TasksDispatchContext);
  return (
    <button onClick={() => dispatch({ type: "added", text: "New" })}>
      Add
    </button>
  );
}
```

Splitting state and dispatch into two contexts means components that only dispatch don't re-render when the tasks change, because `dispatch` never changes.

### 162: What is lazy initial state?

If computing the initial state is expensive, pass a function to `useState`. React calls it only on the first render.

```jsx
// Runs on every render (the result is ignored after the first)
const [todos, setTodos] = useState(createInitialTodos());

// Runs only once
const [todos, setTodos] = useState(createInitialTodos);
const [data, setData] = useState(() =>
  JSON.parse(localStorage.getItem("data")),
);
```

### 163: How do you lazily initialize `useReducer`?

Pass an init function as the third argument. React calls `init(initialArg)` once.

```jsx
function init(username) {
  return { username, todos: loadTodos(username) };
}

const [state, dispatch] = useReducer(reducer, username, init);
```

### 164: What is the difference between `useEffect` and `useLayoutEffect`?

`useEffect` runs after the browser has painted. `useLayoutEffect` runs after the DOM is updated but before the browser paints, and it blocks painting until it finishes.

Use `useLayoutEffect` when you need to measure the DOM and change something before the user sees it, to avoid a flicker. For example, positioning a tooltip based on its size.

```jsx
useLayoutEffect(() => {
  const { height } = ref.current.getBoundingClientRect();
  setTooltipHeight(height);
}, []);
```

In all other cases use `useEffect`, because `useLayoutEffect` can slow down rendering.

### 165: What is `useInsertionEffect`?

It runs before any layout effects, so a library can insert `<style>` tags into the DOM before other code reads layout. It exists for CSS-in-JS library authors. You almost never need it in app code. It can't update state or access refs.

### 166: When do you NOT need an effect?

You don't need an effect when:

- **Transforming data for rendering**: compute it during render.
- **Handling user events**: do it in the event handler.
- **Resetting state when a prop changes**: use a `key`.
- **Notifying a parent about a change**: call the callback in the same event handler.
- **Chains of effects that update state based on other state**: compute in the event handler instead.

```jsx
// Unnecessary effect
const [fullName, setFullName] = useState("");
useEffect(() => {
  setFullName(first + " " + last);
}, [first, last]);

// Better
const fullName = first + " " + last;
```

Effects are for syncing with external systems: network, DOM APIs, third-party widgets, subscriptions.

### 167: What is derived state and how should you handle it?

Derived state is a value you can calculate from props or other state. Don't store it in its own state, because then you have to keep two values in sync. Calculate it during render.

```jsx
function TodoList({ todos, filter }) {
  const visible = todos.filter((t) => (filter === "done" ? t.done : true));
  return <List items={visible} />;
}
```

If the calculation is slow, wrap it in `useMemo` (or let the React Compiler handle it).

### 168: How do you reset all state in a component when a prop changes?

Pass the prop as a `key` from the parent.

```jsx
function ProfilePage({ userId }) {
  return <Profile userId={userId} key={userId} />;
}
```

When `userId` changes, React unmounts the old `Profile` and mounts a new one with fresh state. This is cleaner than an effect that resets each state variable.

### 169: How do you adjust some state when a prop changes, without an effect?

Store the previous prop in state and compare during render. If it changed, set state right there. React will throw away the current output and re-render immediately, before the children render.

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

This is better than an effect, which would render once with stale state first. But often you can avoid it entirely, for example by storing the selected ID and computing the selected item from `items`.

### 170: What is a stale closure in React?

A function captures the variables from the render where it was created. If it runs later and those values have changed since, it still sees the old ones.

```jsx
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // count is always 0 here
    }, 1000);
    return () => clearInterval(id);
  }, []); // missing dependency

  return <p>{count}</p>;
}
```

The fix here is the updater form `setCount(c => c + 1)`. In general: list all dependencies, use updater functions, or use `useEffectEvent` for logic that should always read the latest values.

### 171: What is a race condition in data fetching and how do you avoid it?

If the user changes a value quickly, several requests are in flight at once and may come back in any order. An older response can arrive last and overwrite the correct data.

Fix it by ignoring stale responses in the cleanup:

```jsx
useEffect(() => {
  let cancelled = false;
  fetchResults(query).then((results) => {
    if (!cancelled) setResults(results);
  });
  return () => {
    cancelled = true;
  };
}, [query]);
```

Data fetching libraries like TanStack Query and SWR handle this for you.

### 172: How do you cancel a fetch request when a component unmounts or a dependency changes?

Use `AbortController`.

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch(`/api/search?q=${query}`, { signal: controller.signal })
    .then((r) => r.json())
    .then(setResults)
    .catch((err) => {
      if (err.name !== "AbortError") setError(err);
    });

  return () => controller.abort();
}, [query]);
```

This also saves network bandwidth, unlike a simple `ignore` flag.

### 173: What is `useEffectEvent`?

`useEffectEvent` (stable since React 19.2) lets you pull logic out of an effect that should read the latest props or state but shouldn't make the effect re-run.

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
  }, [roomId]); // theme is not a dependency
}
```

Changing `theme` no longer reconnects to the chat, but the notification still uses the current theme. Only call the returned function from inside effects, and don't pass it to other components or hooks.

### 174: How should you deal with effects running twice in Strict Mode?

Don't try to stop it. Make the effect handle being set up, cleaned up and set up again. Usually that means adding the right cleanup:

```jsx
useEffect(() => {
  const connection = createConnection(roomId);
  connection.connect();
  return () => connection.disconnect();
}, [roomId]);
```

For data fetching, ignore or abort the first request in cleanup. For things that really must run once per app (like initializing analytics), do it outside components at module level. Using a ref to skip the second run just hides the problem.

### 175: When is `useCallback` actually useful?

It helps when the function's identity matters:

1. You pass it to a child wrapped in `memo`, and you want the child to skip re-renders.
2. It is a dependency of an effect or of another hook.
3. It's returned from a custom hook that others might use as a dependency.

Wrapping every handler in `useCallback` just adds noise and some cost. If you use the React Compiler, it handles this automatically.

### 176: When is `useMemo` actually useful?

- The calculation is noticeably slow (you can measure it with `console.time`; around 1ms or more is worth looking at)
- You pass the result to a `memo` component and want to keep the reference stable
- The value is a dependency of another hook

```jsx
const sorted = useMemo(
  () => [...products].sort((a, b) => a.price - b.price),
  [products],
);
```

`useMemo` is only a performance hint. React can discard the cache in some cases, so your code must still work without it.

### 177: How do you use a custom comparison function with `memo`?

Pass it as the second argument. It returns `true` if the props are equal (meaning skip the render).

```jsx
const Chart = memo(
  function Chart({ data, title }) {
    return <Canvas data={data} title={title} />;
  },
  (prev, next) =>
    prev.title === next.title && prev.data.length === next.data.length,
);
```

Be careful: if you skip a prop that's actually used (like a callback), the component can show stale data or call an old function. Deep comparisons can also be slower than just re-rendering.

### 178: Why does `memo` sometimes not prevent re-renders?

Because one of the props is a new object, array or function on every render.

```jsx
function Parent() {
  return (
    <MemoChild
      style={{ color: "red" }} // new object every render
      onClick={() => console.log()} // new function every render
      items={list.filter((x) => x.ok)} // new array every render
    />
  );
}
```

Fix it by moving constants outside the component, using `useMemo`/`useCallback`, or enabling the React Compiler. Also note that a component re-renders anyway if its own state or a context it reads changes, even when wrapped in `memo`.

### 179: How does the React Compiler work, and does it replace `useMemo` and `useCallback`?

The compiler analyzes your components and hooks at build time and inserts caching code. It memoizes JSX, calculations and callbacks based on what each piece actually depends on, at a finer level than you'd do by hand. It can even memoize after a conditional return, which hooks can't.

For most code it replaces manual `useMemo`, `useCallback` and `memo`. You can keep existing ones; the compiler works with them. You may still use `useMemo` or `useCallback` as an escape hatch when you need exact control, for example to keep an effect dependency stable.

### 180: How do you enable the React Compiler?

Install the Babel plugin and add it to your build. With Vite:

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

Next.js and Expo have their own config options for it. The compiler works best with React 19, but it also supports React 17 and 18 through the `react-compiler-runtime` package and a `target` option. Also enable the latest `eslint-plugin-react-hooks` so you see rule violations that would make the compiler skip a component.

### 181: What rules does your code need to follow for the React Compiler to work?

The compiler assumes your code follows the Rules of React:

- Components and hooks are pure during render (same input, same output, no side effects)
- Props, state and hook return values are treated as immutable
- Values passed to JSX are not mutated after render
- Hooks are called at the top level, in the same order every render
- Refs are not read or written during render

If the compiler detects code that breaks these rules, it skips that component instead of compiling it incorrectly. The `eslint-plugin-react-hooks` rules show these problems in your editor.

### 182: Why can Context cause performance problems?

Every component that calls `useContext(SomeContext)` re-renders when the context value changes. A common mistake is creating a new object as the value on every render:

```jsx
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  // new object every time AuthProvider renders
  return <AuthContext value={{ user, setUser }}>{children}</AuthContext>;
}
```

Now every consumer re-renders whenever `AuthProvider` renders, even if `user` didn't change. Fix it with `useMemo` (or the compiler):

```jsx
const value = useMemo(() => ({ user, setUser }), [user]);
return <AuthContext value={value}>{children}</AuthContext>;
```

### 183: How can you split Context to reduce re-renders?

Put values that change at different rates in different contexts. A common split is state vs. actions:

```jsx
const CartStateContext = createContext(null);
const CartActionsContext = createContext(null);

function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const actions = useMemo(
    () => ({
      add: (item) => setItems((prev) => [...prev, item]),
      clear: () => setItems([]),
    }),
    [],
  );

  return (
    <CartActionsContext value={actions}>
      <CartStateContext value={items}>{children}</CartStateContext>
    </CartActionsContext>
  );
}
```

A button that only adds items reads `CartActionsContext` and won't re-render when the cart changes.

### 184: When should you use Context and when a state management library?

Context is a way to pass values down the tree. It's great for values that don't change often: theme, current user, locale, feature flags.

A library like Zustand, Redux Toolkit or Jotai is worth it when:

- Many components read and update the same frequently changing state
- You need components to subscribe to only part of the state (selectors)
- You want devtools, middleware or persistence

For server data (API responses), a data fetching library like TanStack Query is usually a better fit than either.

### 185: How does Redux Toolkit work with React?

Redux Toolkit is the official way to write Redux. You create slices with reducers, and RTK uses Immer so you can write "mutating" code that becomes immutable updates.

```jsx
import { createSlice, configureStore } from "@reduxjs/toolkit";
import { Provider, useSelector, useDispatch } from "react-redux";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
  },
});

const store = configureStore({ reducer: { counter: counterSlice.reducer } });

function Counter() {
  const value = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();
  return (
    <button onClick={() => dispatch(counterSlice.actions.increment())}>
      {value}
    </button>
  );
}

<Provider store={store}>
  <Counter />
</Provider>;
```

`useSelector` only re-renders the component when the selected value changes.

### 186: What is Zustand?

Zustand is a small state library. You create a store with a hook and select what you need. No provider is required.

```jsx
import { create } from "zustand";

const useCartStore = create((set) => ({
  items: [],
  add: (item) => set((state) => ({ items: [...state.items, item] })),
}));

function CartCount() {
  const count = useCartStore((state) => state.items.length);
  return <span>{count}</span>;
}
```

Components re-render only when the selected value changes. Internally it uses `useSyncExternalStore`.

### 187: Why use TanStack Query (React Query) instead of fetching in `useEffect`?

Fetching in effects means you have to handle loading, errors, caching, race conditions, refetching, deduplication and retries yourself. TanStack Query does all of that.

```jsx
import { useQuery } from "@tanstack/react-query";

function Todos() {
  const { data, isPending, error } = useQuery({
    queryKey: ["todos"],
    queryFn: () => fetch("/api/todos").then((r) => r.json()),
  });

  if (isPending) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  return (
    <ul>
      {data.map((t) => (
        <li key={t.id}>{t.title}</li>
      ))}
    </ul>
  );
}
```

Two components using the same `queryKey` share one request and one cache entry.

### 188: What is the difference between server state and client state?

- **Client state** lives only in the browser: whether a modal is open, the current tab, form drafts. You own it fully.
- **Server state** is data stored on the server that you show a copy of: users, products, orders. It can be changed by others, gets stale, and needs fetching, caching and refreshing.

Mixing them in one global store is a common source of bugs. A good setup is local state or a small store for client state, and a framework loader, Server Components or TanStack Query for server state.

### 189: What are Actions in React 19?

An Action is an async function that you run inside a transition. React tracks it for you: it gives you a pending state, handles errors through error boundaries, supports optimistic updates and works with forms.

```jsx
function UpdateName() {
  const [name, setName] = useState("");
  const [error, setError] = useState(null);
  const [isPending, startTransition] = useTransition();

  function handleSubmit() {
    startTransition(async () => {
      const error = await updateName(name);
      if (error) {
        setError(error);
        return;
      }
      redirect("/profile");
    });
  }

  return (
    <>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button onClick={handleSubmit} disabled={isPending}>
        Update
      </button>
      {error && <p>{error}</p>}
    </>
  );
}
```

By convention, props that take actions are named `action` or end with `Action`.

### 190: What is `useActionState`?

`useActionState` wraps an action and keeps the result of the last call as state. It also gives you a pending flag.

```jsx
import { useActionState } from "react";

async function addToCart(prevState, formData) {
  const itemId = formData.get("itemId");
  const res = await fetch("/api/cart", { method: "POST", body: formData });
  if (!res.ok) return { error: "Could not add item" };
  return { error: null, added: itemId };
}

function AddToCartForm({ itemId }) {
  const [state, formAction, isPending] = useActionState(addToCart, {
    error: null,
  });

  return (
    <form action={formAction}>
      <input type="hidden" name="itemId" value={itemId} />
      <button disabled={isPending}>Add to cart</button>
      {state.error && <p>{state.error}</p>}
    </form>
  );
}
```

The action receives the previous state as the first argument and the form data as the second. It used to be called `useFormState` in canary releases; that name is gone.

### 191: What is `useFormStatus`?

`useFormStatus` from `react-dom` gives a component the status of the parent `<form>` it's inside: `pending`, `data`, `method` and `action`.

```jsx
import { useFormStatus } from "react-dom";

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? "Saving..." : "Save"}
    </button>
  );
}

function ProfileForm() {
  return (
    <form action={saveProfile}>
      <input name="name" />
      <SubmitButton />
    </form>
  );
}
```

It only works in a component rendered inside a `<form>`. It doesn't track a form rendered in the same component that calls it.

### 192: What is `useOptimistic`?

`useOptimistic` shows a temporary value while an async action is running. When the action finishes, the optimistic value is replaced by the real state.

```jsx
import { useOptimistic } from "react";

function Thread({ messages, sendMessage }) {
  const [optimisticMessages, addOptimistic] = useOptimistic(
    messages,
    (current, newText) => [...current, { text: newText, sending: true }],
  );

  async function formAction(formData) {
    const text = formData.get("message");
    addOptimistic(text);
    await sendMessage(text);
  }

  return (
    <>
      {optimisticMessages.map((m, i) => (
        <p key={i}>
          {m.text} {m.sending && <small>(sending...)</small>}
        </p>
      ))}
      <form action={formAction}>
        <input name="message" />
      </form>
    </>
  );
}
```

If the action fails, the optimistic value just goes away, since the real `messages` never changed. You call the setter from inside an action or transition.

### 193: How does form reset work with React 19 form actions?

When you pass a function to `<form action>` and the action finishes successfully, React automatically resets the uncontrolled inputs in that form. Controlled inputs keep whatever value is in state.

If you need to reset a form manually from inside a transition, use `requestFormReset`:

```jsx
import { requestFormReset } from "react-dom";

startTransition(async () => {
  await save(formData);
  requestFormReset(formRef.current);
});
```

### 194: What is `useTransition`?

`useTransition` lets you mark a state update as non-urgent. React keeps the UI responsive (typing, clicking) while it renders the transition in the background, and it can interrupt the transition if something more urgent happens.

```jsx
function TabContainer() {
  const [tab, setTab] = useState("about");
  const [isPending, startTransition] = useTransition();

  function selectTab(next) {
    startTransition(() => {
      setTab(next);
    });
  }

  return (
    <>
      <TabButtons onSelect={selectTab} />
      {isPending && <Spinner />}
      {tab === "posts" ? <SlowPosts /> : <About />}
    </>
  );
}
```

Transitions can't be used for controlled text inputs, because input updates need to be urgent.

### 195: What is the difference between `startTransition` and `useTransition`?

Both mark updates as transitions. `useTransition` is a hook that also gives you `isPending`. `startTransition` is a standalone function you can import from `react` and call anywhere, including outside components (for example in a data library or router), but it doesn't tell you whether the transition is pending.

```jsx
import { startTransition } from "react";

startTransition(() => {
  setPage("/settings");
});
```

### 196: How do async transitions work in React 19, and what is the caveat?

In React 19 you can pass an async function to `startTransition`. `isPending` stays `true` until the whole function finishes.

The caveat: state updates that happen after an `await` are not automatically marked as transitions, because JavaScript loses the context across `await`. You need to wrap them in another `startTransition`:

```jsx
startTransition(async () => {
  await updateQuantity(newQuantity);
  startTransition(() => {
    setQuantity(newQuantity);
  });
});
```

This is a known limitation that should go away once JavaScript gets something like AsyncContext.

### 197: What is `useDeferredValue`?

`useDeferredValue` gives you a version of a value that "lags behind". React first re-renders with the old deferred value (fast), then renders again in the background with the new value. If the value changes again, the background render is thrown away.

```jsx
function SearchPage() {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;

  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <div style={{ opacity: isStale ? 0.5 : 1 }}>
        <SlowResults query={deferredQuery} />
      </div>
    </>
  );
}
```

`SlowResults` should be wrapped in `memo`, otherwise it re-renders with the old value anyway and you lose the benefit.

### 198: What does the `initialValue` argument of `useDeferredValue` do?

Added in React 19, it lets you give a value to use on the first render.

```jsx
const value = useDeferredValue(deferredValue, "");
```

On the initial render React uses `initialValue`, then schedules a background render with the real value. This is useful for showing something cheap (like an empty list) first and filling in the expensive content right after.

### 199: How are transitions different from debouncing or throttling?

Debouncing waits a fixed amount of time before doing something. Throttling limits how often it runs. Both delay work even on fast devices.

Transitions and `useDeferredValue` don't use a fixed delay. React starts rendering right away in the background and can drop that work if new input arrives. On a fast device the update shows almost immediately, on a slow device it stays responsive. For network requests you may still want debouncing to avoid sending too many requests.

### 200: How does `use` work with promises?

`use(promise)` returns the resolved value. If the promise is still pending, the component suspends and the nearest `<Suspense>` shows its fallback. If the promise rejects, the nearest error boundary catches it.

```jsx
import { use, Suspense } from "react";

function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map((c) => <p key={c.id}>{c.text}</p>);
}

function Page({ commentsPromise }) {
  return (
    <Suspense fallback={<p>Loading comments...</p>}>
      <Comments commentsPromise={commentsPromise} />
    </Suspense>
  );
}
```

The promise must be created outside the component that reads it (for example in a Server Component, a loader, or a cache). A promise created during render would be a new one every time.

### 201: How is `use(Context)` different from `useContext`?

They return the same value, but `use` can be called conditionally, inside `if` blocks and loops. `useContext` must follow the rules of hooks.

```jsx
function Heading({ children }) {
  if (children == null) {
    return null;
  }
  // useContext could not be called here, after an early return
  const theme = use(ThemeContext);
  return <h1 style={{ color: theme.color }}>{children}</h1>;
}
```

`use` still has to be called inside a component or hook, not in a regular function or event handler.

### 202: How does Suspense work for data fetching?

When a component tries to read data that isn't ready (through `use(promise)`, `lazy`, or a Suspense-enabled library), it "suspends". React stops rendering that part, shows the closest `<Suspense>` fallback, and tries again when the data is ready.

```jsx
<Suspense fallback={<ProfileSkeleton />}>
  <Profile /> {/* suspends while loading */}
</Suspense>
```

Suspense does not detect data fetched in `useEffect`. It only works with data sources built for it: Server Components, `use` with a cached promise, frameworks like Next.js, and libraries like TanStack Query (`useSuspenseQuery`) or Relay.

### 203: How do nested Suspense boundaries work?

Each boundary shows its own fallback for its own content, so you can reveal the page in steps.

```jsx
<Suspense fallback={<PageSpinner />}>
  <Header />
  <Suspense fallback={<PostsSkeleton />}>
    <Posts />
    <Suspense fallback={<CommentsSkeleton />}>
      <Comments />
    </Suspense>
  </Suspense>
</Suspense>
```

Everything inside one boundary is shown together. If `Header` suspends, the whole page shows `PageSpinner`. Once it's ready, `Posts` can show while `Comments` is still loading. Placing boundaries is a design decision about what should appear together.

### 204: How do you stop Suspense from replacing content that's already on the screen with a fallback?

Wrap the update that causes the suspension in a transition. React will then keep showing the old content until the new content is ready, instead of hiding it behind the fallback.

```jsx
function Router() {
  const [page, setPage] = useState("/");
  const [isPending, startTransition] = useTransition();

  function navigate(url) {
    startTransition(() => {
      setPage(url);
    });
  }
  // ...
}
```

Most routers that support Suspense already wrap navigations in transitions. Fallbacks are still shown for parts of the tree that are appearing for the first time.

### 205: How do you lazy load a component that uses a named export?

`lazy` expects a module with a default export. For a named export, map it in the import:

```jsx
const Chart = lazy(() =>
  import("./charts").then((module) => ({ default: module.Chart })),
);
```

### 206: How do you split code by route?

Lazy load each page and wrap the routes in Suspense.

```jsx
import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router";

const Home = lazy(() => import("./pages/Home"));
const Dashboard = lazy(() => import("./pages/Dashboard"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<PageLoader />}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

Frameworks like Next.js and React Router (framework mode) split code by route automatically.

### 207: How do you write an error boundary?

It's a class component that implements `static getDerivedStateFromError` (to render a fallback) and optionally `componentDidCatch` (to log the error).

```jsx
class ErrorBoundary extends React.Component {
  state = { error: null };

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidCatch(error, info) {
    logError(error, info.componentStack);
  }

  render() {
    if (this.state.error) {
      return this.props.fallback ?? <p>Something went wrong.</p>;
    }
    return this.props.children;
  }
}
```

There is no hook equivalent yet, so you either write this class once or use `react-error-boundary`.

### 208: What errors do error boundaries NOT catch?

- Errors in event handlers (use `try/catch` there)
- Errors in async code like `setTimeout` or promise callbacks that don't go through React
- Errors during server-side rendering (handled by the server rendering APIs)
- Errors thrown inside the error boundary itself (only its children are covered)

They do catch errors from rendering, lifecycle methods, effects, and rejected promises read with `use`. Errors thrown inside a transition (including Actions) also go to the closest error boundary.

### 209: What is `react-error-boundary`?

It's a popular package that gives you a ready-made error boundary component with extra features like a reset function and resetting when certain values change.

```jsx
import { ErrorBoundary } from "react-error-boundary";

function Fallback({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <p>Error: {error.message}</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

<ErrorBoundary FallbackComponent={Fallback} resetKeys={[userId]}>
  <UserProfile userId={userId} />
</ErrorBoundary>;
```

### 210: What are `onCaughtError`, `onUncaughtError` and `onRecoverableError`?

They are options for `createRoot` and `hydrateRoot` added in React 19 to control how errors are reported.

```jsx
const root = createRoot(container, {
  onCaughtError(error, errorInfo) {
    // error caught by an error boundary
    reportToService(error, errorInfo.componentStack);
  },
  onUncaughtError(error, errorInfo) {
    // error not caught by any boundary (app crashes)
    reportToService(error, errorInfo.componentStack);
  },
  onRecoverableError(error, errorInfo) {
    // React recovered automatically, e.g. a hydration mismatch
    console.warn(error);
  },
});
```

In React 19, errors are no longer thrown twice. Uncaught errors go to `window.reportError` and caught errors go to `console.error` by default.

### 211: How do refs work for function components in React 19?

In React 19 a function component can accept `ref` as a normal prop. You no longer need `forwardRef`.

```jsx
function TextInput({ placeholder, ref }) {
  return <input placeholder={placeholder} ref={ref} />;
}

function Form() {
  const inputRef = useRef(null);
  return (
    <>
      <TextInput ref={inputRef} placeholder="Name" />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  );
}
```

`forwardRef` still works, but it will be deprecated in a future version. A codemod exists to remove it. Class components still don't receive `ref` as a prop, because there the ref points to the instance.

### 212: What is `useImperativeHandle`?

It lets you choose what a parent gets when it uses a ref on your component. Instead of the whole DOM node, you expose only certain methods.

```jsx
import { useRef, useImperativeHandle } from "react";

function VideoPlayer({ src, ref }) {
  const videoRef = useRef(null);

  useImperativeHandle(
    ref,
    () => ({
      play() {
        videoRef.current.play();
      },
      pause() {
        videoRef.current.pause();
      },
    }),
    [],
  );

  return <video ref={videoRef} src={src} />;
}

// parent: playerRef.current.play()
```

Use it only for things you can't express with props, like focus, scrolling or media playback.

### 213: What are ref callback cleanup functions?

In React 19 a ref callback can return a cleanup function. React calls the cleanup when the element is removed or when the ref callback changes.

```jsx
function Box() {
  return (
    <div
      ref={(node) => {
        const observer = new ResizeObserver((entries) => {
          console.log(entries[0].contentRect.width);
        });
        observer.observe(node);
        return () => observer.disconnect();
      }}
    />
  );
}
```

Before this, React called the callback with `null` on unmount. If you return a cleanup, React won't call it with `null`. Because of this change, returning anything else from a ref callback (like an implicit arrow function return) is now an error in TypeScript, so `ref={n => (instance = n)}` should be written with braces.

### 214: When should you use a ref and when state?

Use state for anything that should show on screen. Use a ref for values that event handlers or effects need but that don't affect rendering: timer IDs, DOM nodes, previous values for comparisons inside effects, or a flag for "is a request in progress".

Don't read or write `ref.current` during render (except initializing it once). The value can be out of date, and the React Compiler assumes you don't do this.

```jsx
// Allowed: lazy init
if (ref.current === null) {
  ref.current = new ExpensiveObject();
}
```

### 215: How do you build a stopwatch with refs?

```jsx
function Stopwatch() {
  const [startTime, setStartTime] = useState(null);
  const [now, setNow] = useState(null);
  const intervalRef = useRef(null);

  function handleStart() {
    setStartTime(Date.now());
    setNow(Date.now());
    clearInterval(intervalRef.current);
    intervalRef.current = setInterval(() => setNow(Date.now()), 10);
  }

  function handleStop() {
    clearInterval(intervalRef.current);
  }

  const seconds = startTime && now ? (now - startTime) / 1000 : 0;

  return (
    <>
      <h1>{seconds.toFixed(3)}</h1>
      <button onClick={handleStart}>Start</button>
      <button onClick={handleStop}>Stop</button>
    </>
  );
}
```

The interval ID isn't shown on screen, so it goes in a ref.

### 216: Write a `useDebounce` hook.

```jsx
function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);

  return debounced;
}

function Search() {
  const [text, setText] = useState("");
  const query = useDebounce(text, 400);
  const results = useSearch(query); // only fetches after typing pauses

  return <input value={text} onChange={(e) => setText(e.target.value)} />;
}
```

### 217: Write a `useLocalStorage` hook.

```jsx
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const stored = localStorage.getItem(key);
      return stored !== null ? JSON.parse(stored) : initialValue;
    } catch {
      return initialValue;
    }
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}

const [theme, setTheme] = useLocalStorage("theme", "light");
```

With SSR this needs extra care, because `localStorage` doesn't exist on the server and the first client render must match the server HTML.

### 218: Write a `useOnlineStatus` hook.

The right tool for subscribing to a browser value is `useSyncExternalStore`.

```jsx
import { useSyncExternalStore } from "react";

function subscribe(callback) {
  window.addEventListener("online", callback);
  window.addEventListener("offline", callback);
  return () => {
    window.removeEventListener("online", callback);
    window.removeEventListener("offline", callback);
  };
}

export function useOnlineStatus() {
  return useSyncExternalStore(
    subscribe,
    () => navigator.onLine, // client value
    () => true, // server value
  );
}
```

`subscribe` is defined outside the component so it's the same function every render, otherwise React would resubscribe each time.

### 219: What is `useSyncExternalStore`?

It's a hook for reading data from a store outside React (a state library, a browser API, a global object) in a way that's safe with concurrent rendering.

```jsx
const snapshot = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?);
```

- `subscribe(callback)` starts listening and returns an unsubscribe function
- `getSnapshot()` returns the current value. It must return the same value (same reference) if nothing changed, otherwise you get an infinite loop.
- `getServerSnapshot()` is used during SSR and hydration

State libraries like Zustand and Redux use it internally.

### 220: Do two components using the same custom hook share state?

No. Each call to a hook gets its own independent state. A custom hook shares logic, not data.

```jsx
function useCounter() {
  const [count, setCount] = useState(0);
  return [count, () => setCount((c) => c + 1)];
}

function A() {
  const [count] = useCounter(); /* own count */
}
function B() {
  const [count] = useCounter(); /* separate count */
}
```

To share the data, lift state up, use context, or use an external store.

### 221: Should every function that starts with `use` be a hook?

Only functions that call hooks should start with `use`. The name tells React tools and the linter that the rules of hooks apply. If a function doesn't call any hooks, give it a normal name like `getSortedItems`, so it can be called anywhere, including conditionally.

### 222: What is the compound components pattern?

A group of components that work together and share state through context, giving users a flexible API.

```jsx
const TabsContext = createContext(null);

function Tabs({ defaultValue, children }) {
  const [active, setActive] = useState(defaultValue);
  return <TabsContext value={{ active, setActive }}>{children}</TabsContext>;
}

function Tab({ value, children }) {
  const { active, setActive } = use(TabsContext);
  return (
    <button aria-selected={active === value} onClick={() => setActive(value)}>
      {children}
    </button>
  );
}

function TabPanel({ value, children }) {
  const { active } = use(TabsContext);
  return active === value ? <div>{children}</div> : null;
}

<Tabs defaultValue="a">
  <Tab value="a">First</Tab>
  <Tab value="b">Second</Tab>
  <TabPanel value="a">Content A</TabPanel>
  <TabPanel value="b">Content B</TabPanel>
</Tabs>;
```

Libraries like Radix UI use this pattern a lot.

### 223: Why did hooks mostly replace render props and HOCs?

Render props and HOCs add extra layers to the component tree ("wrapper hell"), make it unclear where props come from, and can have name collisions between props. Hooks let you reuse logic by calling a function, without changing the tree. You can use several hooks in one component and see clearly what each returns.

Render props are still useful when the shared thing is actually rendering, like a list that lets the user customize each row.

### 224: Are higher-order components still used?

Less than before, but you still see them: `connect` in older Redux code, `withRouter` in old React Router, and some auth or analytics wrappers. Problems with HOCs: wrapper layers, prop name collisions, and in the past ref forwarding issues. For new code prefer hooks. If you write a HOC, don't create it inside a render function, because that makes a new component type every render and resets state.

### 225: How do you build a component that can be both controlled and uncontrolled?

Accept `value`, `defaultValue` and `onChange`. If `value` is passed, use it; otherwise keep internal state.

```jsx
function Toggle({ value, defaultValue = false, onChange }) {
  const [internal, setInternal] = useState(defaultValue);
  const isControlled = value !== undefined;
  const on = isControlled ? value : internal;

  function handleClick() {
    const next = !on;
    if (!isControlled) setInternal(next);
    onChange?.(next);
  }

  return (
    <button aria-pressed={on} onClick={handleClick}>
      {on ? "On" : "Off"}
    </button>
  );
}
```

This matches how native inputs behave and is common in component libraries.

### 226: How does event bubbling work with portals?

Events bubble through the React tree, not the DOM tree. So an event inside a portal reaches the parent component that rendered the portal, even though in the DOM the portal is attached somewhere else (like `document.body`).

```jsx
<div onClick={() => console.log("parent got the click")}>
  {createPortal(<button>Click</button>, document.body)}
</div>
```

Clicking the button logs the message. This can surprise you, for example when a click inside a modal triggers an `onClick` on a card behind it. Use `e.stopPropagation()` if needed.

### 227: Can components inside a portal read context from above?

Yes. A portal only changes where the DOM nodes go. In the React tree it's still a child of the component that rendered it, so context, state and event bubbling all work as usual.

### 228: Why shouldn't you use random values as keys?

```jsx
{
  items.map((item) => <Row key={Math.random()} item={item} />);
}
```

The key changes every render, so React thinks every item is new. It destroys and recreates all rows, losing their state and focus, and it's slow. Keys must be stable. Generate IDs when you create the data (for example with `crypto.randomUUID()`), not during rendering.

### 229: Do keys need to be unique across the whole app?

No. Keys only need to be unique among siblings in the same array. Two different lists can use the same keys. Also, the `key` is not passed to the component as a prop. If the component needs the ID, pass it separately:

```jsx
<Item key={item.id} id={item.id} />
```

### 230: How does React decide whether to keep or reset a component's state?

State is tied to the position of a component in the tree. As long as the same component type is rendered at the same position, React keeps its state. If a different type appears at that position, or the component is removed, the state is gone.

```jsx
// Same position, same type: state is kept when isFancy changes
{
  isFancy ? <Counter isFancy /> : <Counter />;
}

// Different positions: state resets
{
  isFancy && <Counter isFancy />;
}
{
  !isFancy && <Counter />;
}
```

A different `key` also counts as a different component, which forces a reset.

### 231: Why shouldn't you define a component inside another component?

```jsx
function Parent() {
  function Child() {
    return <input />;
  }
  return <Child />;
}
```

Every time `Parent` renders, `Child` is a new function, so React sees a different component type and unmounts and remounts it. The input loses its value and focus on every render. It's also slower. Define components at the top level of the module and pass data as props.

### 232: What happens to state when you conditionally render something before a component?

The position of components matters, but React treats `false`, `null` and `undefined` as "empty slots" that keep their position. So this keeps the `Form` state:

```jsx
<div>
  {showBanner && <Banner />}
  <Form />
</div>
```

`Form` is always the second child, whether or not the banner shows. Problems happen when the structure changes, like wrapping the component in a different parent element in one branch.

### 233: Why are `Children` and `cloneElement` considered legacy?

`Children.map`, `cloneElement` and similar APIs let a parent inspect and change its children's props. This is fragile: it breaks when children are wrapped in another component or a fragment, and it hides where props come from. The docs list them as legacy APIs.

Alternatives:

- Accept data as an array prop and render the items yourself
- Use render props
- Use context so children read what they need (compound components)

```jsx
// Instead of cloning children to inject "isActive"
<List
  items={items}
  renderItem={(item, isActive) => <Row item={item} active={isActive} />}
/>
```

### 234: How does React 19 handle `<title>`, `<meta>` and `<link>` tags?

When you render these tags anywhere in your components, React 19 hoists them into the document `<head>`. This works in client rendering, SSR and Server Components.

```jsx
function ProductPage({ product }) {
  return (
    <>
      <title>{`${product.name} | Shop`}</title>
      <meta name="description" content={product.description} />
      <link rel="canonical" href={`https://shop.com/p/${product.slug}`} />
      <h1>{product.name}</h1>
    </>
  );
}
```

Note that `<title>` should have a single string child, which is why a template literal is used above. For more complex needs (like overriding tags from parent layouts) frameworks still offer their own metadata APIs.

### 235: How does React 19 handle stylesheets?

If you render `<link rel="stylesheet">` with a `precedence` prop, React manages it: it inserts it in the right order in `<head>`, removes duplicates, and during Suspense waits for the stylesheet to load before showing the content that needs it.

```jsx
function Widget() {
  return (
    <Suspense fallback="loading...">
      <link rel="stylesheet" href="/widget.css" precedence="default" />
      <div className="widget">...</div>
    </Suspense>
  );
}
```

Inline `<style>` tags with `href` and `precedence` are supported in the same way. This helps components bring their own CSS without flashing unstyled content.

### 236: How does React 19 handle async scripts?

You can render `<script async src="...">` anywhere in the tree. React deduplicates it, so even if several components render the same script, it loads once. In SSR it's placed in `<head>` with lower priority than critical resources.

```jsx
function MapWidget() {
  return (
    <div>
      <script async src="https://maps.example.com/sdk.js" />
      <div id="map" />
    </div>
  );
}
```

### 237: What are `preload`, `preinit`, `preconnect` and `prefetchDNS`?

They are functions from `react-dom` (React 19) that tell the browser about resources it will need soon.

```jsx
import { prefetchDNS, preconnect, preload, preinit } from "react-dom";

function App() {
  preinit("https://cdn.example.com/script.js", { as: "script" }); // load and run now
  preload("https://cdn.example.com/font.woff2", { as: "font" }); // download now
  preconnect("https://api.example.com"); // open connection
  prefetchDNS("https://images.example.com"); // resolve DNS
  // ...
}
```

React puts the matching `<link>` tags in the document head (or in the SSR output) and removes duplicates. They're especially useful in Server Components and SSR, where they can start downloads early.

### 238: How is the Context provider written in React 19?

You can render the context object itself as the provider:

```jsx
const LangContext = createContext("en");

function App() {
  return (
    <LangContext value="fr">
      <Page />
    </LangContext>
  );
}
```

`<LangContext.Provider value="fr">` still works but is planned to be deprecated. `<Context.Consumer>` is also an old pattern; use `useContext` or `use` instead.

### 239: Which APIs were removed in React 19?

- `ReactDOM.render` and `ReactDOM.hydrate` (use `createRoot` and `hydrateRoot`)
- `unmountComponentAtNode` (use `root.unmount()`)
- `ReactDOM.findDOMNode` (use refs)
- String refs like `ref="input"` (use ref objects or callbacks)
- `propTypes` checks and `defaultProps` for function components
- Legacy context (`contextTypes`, `getChildContext`)
- Module pattern factories and `createFactory`
- `react-dom/test-utils` `act` moved to `react` (`import { act } from "react"`)
- UMD builds

`react-test-renderer` is deprecated.

### 240: How do you upgrade an app to React 19?

1. Upgrade to React 18.3 first. It's the same as 18.2 but warns about APIs that are removed in 19.
2. Fix the warnings.
3. Install React 19: `npm install react@^19 react-dom@^19`, and `@types/react@^19 @types/react-dom@^19` for TypeScript.
4. Run the codemods:

```bash
npx codemod@latest react/19/migration-recipe
npx types-react-codemod@latest preset-19 ./src
```

5. Check third-party libraries for React 19 support and test the app, especially error handling and Strict Mode behavior.

### 241: What changed in TypeScript types with React 19?

- `useRef` now requires an argument: `useRef<HTMLDivElement>(null)`. All refs are mutable, `MutableRefObject` is deprecated in favor of `RefObject`.
- The global `JSX` namespace was removed. Use `React.JSX` instead (for example `React.JSX.Element`).
- `ReactElement` props default to `unknown` instead of `any`.
- Ref callbacks can't implicitly return values (because of ref cleanup).
- Some deprecated types were removed, like `ReactChild` and `VoidFunctionComponent`.

The `types-react-codemod` tool can fix most of this automatically.

### 242: How do you type the `children` prop?

Use `React.ReactNode`. It covers everything React can render: elements, strings, numbers, arrays, `null`, `undefined` and booleans.

```tsx
type ModalProps = {
  title: string;
  children: React.ReactNode;
};
```

Use `React.ReactElement` only if you need specifically a single element (not a string or `null`). `PropsWithChildren<P>` is a helper that adds an optional `children` to your props.

### 243: How do you type a component that wraps a native element and accepts all its props?

Use `ComponentProps` (or `ComponentPropsWithoutRef` / `ComponentPropsWithRef`).

```tsx
type ButtonProps = React.ComponentProps<"button"> & {
  variant?: "primary" | "secondary";
};

function Button({ variant = "primary", className, ...rest }: ButtonProps) {
  return <button className={`btn-${variant} ${className ?? ""}`} {...rest} />;
}
```

Since `ref` is a regular prop in React 19, `ComponentProps<"button">` already includes it, so the ref is passed through with `...rest`.

### 244: How do you write a generic component in TypeScript?

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  renderItem: (item: T) => React.ReactNode;
};

function List<T>({ items, getKey, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={getKey(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}

<List
  items={users}
  getKey={(u) => u.id}
  renderItem={(u) => u.name} // u is inferred as User
/>;
```

In a `.tsx` file, if you use an arrow function, write `<T,>` so it isn't parsed as JSX.

### 245: How do you type `useReducer` actions?

Use a discriminated union so TypeScript knows the payload for each action type.

```tsx
type State = { count: number; step: number };

type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "setStep"; step: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "increment":
      return { ...state, count: state.count + state.step };
    case "decrement":
      return { ...state, count: state.count - state.step };
    case "setStep":
      return { ...state, step: action.step }; // step is known here
  }
}

const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
```

### 246: How do you type a Context that has no sensible default value?

Use `null` as the default and write a custom hook that throws if the provider is missing.

```tsx
type AuthContextValue = { user: User | null; logout: () => void };

const AuthContext = createContext<AuthContextValue | null>(null);

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used inside <AuthProvider>");
  }
  return ctx;
}
```

Consumers get a non-null type and a clear error if they forget the provider.

### 247: Which queries should you prefer in React Testing Library?

The library suggests this order, based on how users and assistive tech find elements:

1. `getByRole` (with `name`), e.g. `getByRole("button", { name: /save/i })`
2. `getByLabelText` for form fields
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue`
6. `getByAltText`, `getByTitle`
7. `getByTestId` as a last resort

Variants: `getBy` throws if not found, `queryBy` returns `null` (good for checking something is absent), `findBy` returns a promise and waits (for async UI).

### 248: How do you simulate user interactions in tests?

Use `@testing-library/user-event`. It simulates real events more closely than `fireEvent` (focus, keydown, input, keyup, and so on).

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

test("submits the form", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();
  render(<LoginForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText(/email/i), "a@b.com");
  await user.click(screen.getByRole("button", { name: /log in/i }));

  expect(onSubmit).toHaveBeenCalledWith({ email: "a@b.com" });
});
```

### 249: How do you test asynchronous UI?

Use `findBy*` queries or `waitFor`.

```jsx
test("shows users after loading", async () => {
  render(<UserList />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
  expect(await screen.findByText("Alice")).toBeInTheDocument();
});

await waitFor(() => {
  expect(screen.queryByText(/loading/i)).not.toBeInTheDocument();
});
```

Avoid fixed `setTimeout` waits in tests. They make tests slow and flaky.

### 250: How do you mock API calls in React tests?

A good option is Mock Service Worker (MSW). It intercepts requests at the network level, so your components use their real fetch code.

```js
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

const server = setupServer(
  http.get("/api/users", () => HttpResponse.json([{ id: 1, name: "Alice" }])),
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

You can also mock `fetch` or a module with `vi.mock` / `jest.mock`, but that ties tests to implementation details.

### 251: How do you test a custom hook?

Use `renderHook` from React Testing Library.

```jsx
import { renderHook, act } from "@testing-library/react";

test("useCounter increments", () => {
  const { result } = renderHook(() => useCounter(5));

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(6);
});
```

Often it's better to test the hook through a component that uses it, the way a user would.

### 252: What is `act()`?

`act` makes sure all updates, effects and renders caused by some code are finished before you make assertions. React Testing Library wraps `render`, `fireEvent` and `user-event` calls in `act` for you, so you rarely call it directly.

In React 19, `act` is imported from `react`:

```js
import { act } from "react";

await act(async () => {
  root.render(<App />);
});
```

The old `act` from `react-dom/test-utils` was removed.

### 253: What happened to `react-test-renderer`?

It's deprecated as of React 19 and prints a warning. The React team recommends React Testing Library for web, and React Native Testing Library for native apps. Snapshot tests based on `react-test-renderer` should be moved to those tools.

### 254: What is the `<Profiler>` component?

`<Profiler>` measures how often a part of the tree renders and how long it takes.

```jsx
import { Profiler } from "react";

function onRender(
  id,
  phase,
  actualDuration,
  baseDuration,
  startTime,
  commitTime,
) {
  console.log(id, phase, actualDuration);
}

<Profiler id="Sidebar" onRender={onRender}>
  <Sidebar />
</Profiler>;
```

It's disabled in production builds by default (there is a special profiling build). In practice the Profiler tab in React DevTools is easier to use for finding slow components.

### 255: How do you find out why a component re-renders?

- React DevTools Profiler: record an interaction, then click a component to see "Why did this render?" (enable "Record why each component rendered" in settings).
- "Highlight updates when components render" in DevTools settings shows renders visually.
- In Chrome, React 19.2 adds React tracks to the Performance panel, showing scheduler work and component renders on a timeline.
- Libraries like `why-did-you-render` or `react-scan` can log or show unnecessary renders.

Look for new object or function props, context values that change too often, or state that's placed too high in the tree.

### 256: What is list virtualization?

Virtualization (or windowing) renders only the list items currently visible on screen plus a small buffer, instead of thousands of DOM nodes.

```jsx
import { useVirtualizer } from "@tanstack/react-virtual";

function BigList({ rows }) {
  const parentRef = useRef(null);
  const virtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 35,
  });

  return (
    <div ref={parentRef} style={{ height: 400, overflow: "auto" }}>
      <div style={{ height: virtualizer.getTotalSize(), position: "relative" }}>
        {virtualizer.getVirtualItems().map((item) => (
          <div
            key={item.key}
            style={{
              position: "absolute",
              top: 0,
              transform: `translateY(${item.start}px)`,
              height: item.size,
            }}
          >
            {rows[item.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

Other libraries: `react-window`, `react-virtuoso`.

### 257: How do you debounce a search input that calls an API?

Keep the input controlled for instant typing feedback, and debounce the value used for fetching.

```jsx
function Search() {
  const [text, setText] = useState("");
  const [results, setResults] = useState([]);

  useEffect(() => {
    if (!text) {
      setResults([]);
      return;
    }
    const controller = new AbortController();
    const id = setTimeout(() => {
      fetch(`/api/search?q=${encodeURIComponent(text)}`, {
        signal: controller.signal,
      })
        .then((r) => r.json())
        .then(setResults)
        .catch(() => {});
    }, 300);

    return () => {
      clearTimeout(id);
      controller.abort();
    };
  }, [text]);

  return (
    <>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <ul>
        {results.map((r) => (
          <li key={r.id}>{r.title}</li>
        ))}
      </ul>
    </>
  );
}
```

The cleanup cancels both the pending timer and any request already sent.

### 258: What's wrong with chaining effects that set state?

```jsx
useEffect(() => {
  if (card.gold) setGoldCount((c) => c + 1);
}, [card]);

useEffect(() => {
  if (goldCount > 3) {
    setRound((r) => r + 1);
    setGoldCount(0);
  }
}, [goldCount]);
```

Each effect causes another render, so one user action leads to several renders in a row. It's also hard to follow. Instead, calculate what you can during render and do all the updates in the event handler that started it:

```jsx
function handlePlaceCard(nextCard) {
  setCard(nextCard);
  if (nextCard.gold) {
    if (goldCount < 3) {
      setGoldCount(goldCount + 1);
    } else {
      setGoldCount(0);
      setRound(round + 1);
    }
  }
}
```

### 259: What are the main differences between Server Components and Client Components?

| Server Components                                 | Client Components                          |
| ------------------------------------------------- | ------------------------------------------ |
| Default in RSC frameworks, no directive           | Marked with `"use client"` in the file     |
| Run on the server or at build time only           | Run on the server (SSR) and in the browser |
| Code is not sent to the browser                   | Code is in the JS bundle                   |
| Can be `async`, can access DB, files, secrets     | Can't access server-only resources         |
| No state, effects, event handlers or browser APIs | Can use hooks, events, browser APIs        |

Use Server Components for data fetching and static parts, and Client Components for interactivity.

### 260: What props can a Server Component pass to a Client Component?

Only values React can serialize:

- Primitives: string, number, bigint, boolean, `undefined`, `null`
- Plain objects and arrays of serializable values
- `Date`, `Map`, `Set`, typed arrays, `FormData`
- Promises (the client can read them with `use`)
- JSX elements (including Server Components)
- Server Functions (functions marked with `"use server"`)

Not allowed: regular functions, class instances, symbols that aren't registered globally, and other non-plain objects.

### 261: How can a Client Component render a Server Component?

A Client Component can't import a Server Component, because everything it imports becomes client code. But a Server Component can pass another Server Component to it as `children` or another prop.

```jsx
// Layout.server.jsx (Server Component)
import Sidebar from "./Sidebar"; // client component
import Recommendations from "./Recommendations"; // server component

export default function Layout() {
  return (
    <Sidebar>
      <Recommendations />
    </Sidebar>
  );
}
```

```jsx
// Sidebar.jsx
"use client";
export default function Sidebar({ children }) {
  const [open, setOpen] = useState(true);
  return open ? <aside>{children}</aside> : null;
}
```

`Recommendations` is rendered on the server and passed to the client as already rendered output.

### 262: What are Server Functions?

Server Functions are async functions that run on the server but can be called from Client Components. You mark them with `"use server"`, either at the top of a file or at the top of the function body.

```jsx
// actions.js
"use server";

export async function createTodo(formData) {
  const title = formData.get("title");
  await db.todos.create({ title });
}
```

```jsx
"use client";
import { createTodo } from "./actions";

export function TodoForm() {
  return (
    <form action={createTodo}>
      <input name="title" />
      <button>Add</button>
    </form>
  );
}
```

When used in a form `action` or inside `startTransition`, they're called Server Actions. Before September 2024 all of them were called Server Actions.

### 263: What security issues should you think about with Server Functions?

A Server Function is basically a public API endpoint. Anyone can call it with any arguments, not only your UI.

- Always validate input (for example with Zod)
- Check authentication and authorization inside the function, every time
- Don't trust IDs from the client without checking ownership
- Don't return sensitive data you wouldn't put in an API response
- Keep `react-server-dom-*` and your framework updated, since vulnerabilities in the RSC protocol have been found and patched (for example in December 2025)

```js
"use server";

export async function deletePost(postId) {
  const user = await getCurrentUser();
  if (!user) throw new Error("Not logged in");
  const post = await db.posts.find(postId);
  if (post.authorId !== user.id) throw new Error("Forbidden");
  await db.posts.delete(postId);
}
```

### 264: How does streaming SSR work?

Instead of waiting for the whole page to render, the server sends HTML in chunks. It sends the shell (layout and Suspense fallbacks) first, then streams each Suspense boundary's HTML when it's ready, along with a small inline script that swaps it into place.

```js
import { renderToPipeableStream } from "react-dom/server";

app.get("/", (req, res) => {
  const { pipe } = renderToPipeableStream(<App />, {
    bootstrapScripts: ["/main.js"],
    onShellReady() {
      res.setHeader("content-type", "text/html");
      pipe(res);
    },
  });
});
```

For Web Streams environments (Deno, Bun, edge runtimes) use `renderToReadableStream`.

### 265: What are common causes of hydration mismatches?

The server HTML doesn't match what the client renders on its first render. Common causes:

- Using `Date.now()`, `new Date()` or `Math.random()` in render
- Reading `window`, `localStorage` or `navigator` during render
- Different locale or time zone formatting between server and client
- Invalid HTML nesting, like a `<div>` inside a `<p>`, which the browser fixes up
- Browser extensions changing the DOM
- Conditional rendering based on `typeof window !== "undefined"`

In React 19 you get a single error with a diff showing what didn't match, which makes these easier to track down.

### 266: What is `suppressHydrationWarning`?

It tells React not to warn when the text content or attributes of that one element differ between server and client. It only works one level deep.

```jsx
<time suppressHydrationWarning>{new Date().toLocaleTimeString()}</time>
```

It's an escape hatch for values that can't match, like timestamps. Don't use it to hide real bugs.

### 267: What is `hydrateRoot`?

It's the client function used to hydrate server-rendered HTML.

```jsx
import { hydrateRoot } from "react-dom/client";

hydrateRoot(document.getElementById("root"), <App />, {
  onRecoverableError(error) {
    console.warn("Hydration issue:", error);
  },
});
```

Unlike `createRoot`, it reuses the existing DOM. The `<App />` you pass must produce the same output as on the server. The old `ReactDOM.hydrate` is removed in React 19.

### 268: Why is `useId` important for server rendering?

If you generate IDs with a counter or `Math.random()`, the server and client get different values, which causes hydration mismatches. `useId` creates IDs based on the component's position in the tree, so they're the same in both places.

```jsx
function PasswordField() {
  const hintId = useId();
  return (
    <>
      <input type="password" aria-describedby={hintId} />
      <p id={hintId}>At least 12 characters</p>
    </>
  );
}
```

If you have several React apps on one page, use the `identifierPrefix` option on `createRoot`/`hydrateRoot` to avoid collisions.

### 269: What is `<Activity>`?

`<Activity>` (stable in React 19.2) lets you hide part of the UI while keeping its state, instead of unmounting it.

```jsx
import { Activity } from "react";

function App({ tab }) {
  return (
    <>
      <Activity mode={tab === "home" ? "visible" : "hidden"}>
        <Home />
      </Activity>
      <Activity mode={tab === "search" ? "visible" : "hidden"}>
        <Search />
      </Activity>
    </>
  );
}
```

When `mode="hidden"`, React hides the children with `display: none`, cleans up their effects, and gives updates to them low priority. When it becomes visible again, the state (like typed text or scroll position inside components) is still there and effects run again. You can also use it to pre-render content the user will probably open next.

### 270: How is `<Activity>` different from conditional rendering?

| `{show && <Panel />}`         | `<Activity mode={show ? "visible" : "hidden"}>` |
| ----------------------------- | ----------------------------------------------- |
| Hidden component is unmounted | Hidden component stays mounted                  |
| State is lost                 | State is kept                                   |
| Effects cleaned up            | Effects cleaned up, re-run when visible         |
| Nothing rendered while hidden | Can render in the background at low priority    |

The trade-off is memory: hidden subtrees stay in memory and in the DOM, so don't wrap huge numbers of screens with it.

### 271: How do Next.js and React Server Components relate?

React defines Server Components, Server Functions, the directives and the streaming format. But React doesn't include a router or bundler setup for them, so you need a framework that implements them. Next.js App Router is the most widely used one. In it, every component in the `app` folder is a Server Component by default, and you add `"use client"` for interactive parts. React Router and other frameworks are also adding RSC support.

### 272: How do loaders and actions work in React Router v7?

In framework mode (or data mode), each route can export a `loader` to fetch data before rendering and an `action` to handle form submissions.

```jsx
// routes/product.jsx
export async function loader({ params }) {
  const product = await getProduct(params.id);
  return { product };
}

export async function action({ request, params }) {
  const formData = await request.formData();
  await addReview(params.id, formData.get("text"));
  return { ok: true };
}

export default function Product({ loaderData }) {
  return (
    <>
      <h1>{loaderData.product.name}</h1>
      <Form method="post">
        <textarea name="text" />
        <button>Post review</button>
      </Form>
    </>
  );
}
```

Data loads in parallel with the code for the route, which avoids fetch-in-effect waterfalls. After an action, loaders run again so the UI shows fresh data.

### 273: What are fetch-on-render and render-as-you-fetch?

- **Fetch-on-render**: a component renders, then starts fetching in an effect. Child components that also fetch wait for the parent to finish. This causes waterfalls.
- **Fetch-then-render**: fetch all data first, then render. No waterfall, but nothing shows until all data is in.
- **Render-as-you-fetch**: start fetching as early as possible (on navigation, in a loader, in a Server Component), and render immediately with Suspense showing fallbacks until each piece of data is ready.

Modern frameworks and Server Components push you towards render-as-you-fetch.

### 274: What is a network waterfall and how do you avoid it?

A waterfall is when requests happen one after another even though they could run in parallel.

```jsx
// Waterfall: Posts can't start fetching until User finished
function Profile() {
  const user = useFetch("/api/user");
  if (!user) return <Spinner />;
  return <Posts userId={user.id} />;
}
```

Ways to avoid it:

- Start independent requests at the same time (`Promise.all`)
- Fetch on the route level (loaders) instead of inside nested components
- In Server Components, start promises early and await them later, or pass promises to children
- Use prefetching on hover or navigation

### 275: How do you update deeply nested state without a lot of spreading?

Use Immer. It lets you write code that looks like mutation, and produces a new immutable object.

```jsx
import { useImmer } from "use-immer";

function Profile() {
  const [person, updatePerson] = useImmer({
    name: "Ann",
    artwork: { title: "Blue Nana", city: "Hamburg" },
  });

  function handleCityChange(e) {
    updatePerson((draft) => {
      draft.artwork.city = e.target.value;
    });
  }
  // ...
}
```

Redux Toolkit uses Immer internally. Another option is to flatten (normalize) your state so it isn't deeply nested.

### 276: What are good rules for structuring state?

- **Group related state**: if two values always change together, put them in one object.
- **Avoid contradictions**: instead of `isSending` and `isSent` booleans, use one `status` value.
- **Avoid redundant state**: don't store what you can calculate from props or other state.
- **Avoid duplication**: store the selected item's ID, not a copy of the item.
- **Avoid deep nesting**: flat state is easier to update.

```jsx
// Instead of
const [selectedItem, setSelectedItem] = useState(items[0]);
// use
const [selectedId, setSelectedId] = useState(items[0].id);
const selectedItem = items.find((i) => i.id === selectedId);
```

### 277: What is state normalization?

Storing data like a database table: items by ID in an object, and arrays of IDs for order and relationships.

```js
const state = {
  posts: {
    byId: {
      p1: { id: "p1", title: "Hello", authorId: "u1", commentIds: ["c1"] },
    },
    allIds: ["p1"],
  },
  users: { byId: { u1: { id: "u1", name: "Ann" } } },
  comments: { byId: { c1: { id: "c1", text: "Nice" } } },
};
```

Updating one item becomes simple, and there's only one copy of each item. Redux Toolkit has `createEntityAdapter` to help with this.

### 278: What is state colocation?

Keeping state as close as possible to where it's used. If only one component needs a value, keep it there instead of in a parent or global store. This reduces re-renders (only that part of the tree updates) and makes code easier to understand. Lift state up only when siblings actually need to share it.

### 279: How do you make React apps accessible?

- Use semantic HTML (`<button>`, `<nav>`, `<main>`, `<label>`) instead of clickable `<div>`s
- Connect labels to inputs (`htmlFor` + `id`, or `useId`)
- Add `alt` text to images
- Use ARIA attributes only when HTML can't express it (`aria-expanded`, `aria-live`)
- Manage focus in modals and after route changes
- Make everything work with the keyboard
- Check color contrast
- Test with `eslint-plugin-jsx-a11y`, axe, and a screen reader

### 280: How do you manage focus when opening and closing a modal?

When the modal opens, move focus inside it. Keep Tab inside it while open. When it closes, return focus to the element that opened it.

```jsx
function Modal({ open, onClose, children }) {
  const dialogRef = useRef(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (open) {
      dialog.showModal(); // native focus handling and focus trapping
    } else if (dialog.open) {
      dialog.close();
    }
  }, [open]);

  return (
    <dialog ref={dialogRef} onClose={onClose}>
      {children}
      <button onClick={onClose}>Close</button>
    </dialog>
  );
}
```

The native `<dialog>` with `showModal()` traps focus, handles Escape and returns focus to the previous element. For custom modals, libraries like Radix or React Aria handle this for you.

### 281: How does event propagation work in React?

React events bubble up the component tree just like DOM events. You can stop them with `e.stopPropagation()`. To handle an event in the capture phase (from top to bottom, before children), add `Capture` to the event name.

```jsx
<div
  onClickCapture={() => console.log("1. capture on parent")}
  onClick={() => console.log("3. bubble on parent")}
>
  <button onClick={() => console.log("2. button")}>Click</button>
</div>
```

All React events bubble except `onScroll`, which only fires on the element you attach it to.

### 282: Where does React attach its event listeners?

Since React 17, React attaches listeners to the root container (the element you passed to `createRoot`), not to `document`. It uses one listener per event type and figures out which component handlers to call. This made it possible to have several React versions on one page and to mix React with other code that calls `stopPropagation` on `document`.

### 283: How is React's `onChange` different from the native `change` event?

In the DOM, `change` on a text input fires only when the input loses focus. React's `onChange` fires on every keystroke, like the native `input` event. This is what makes controlled inputs work. If you really want the blur-time behavior, use `onBlur`.

### 284: When should you use uncontrolled inputs?

- Simple forms where you only need the values on submit
- Forms using React 19 actions (`<form action>`), where you get `FormData`
- Performance-sensitive forms with many fields, where re-rendering on each keystroke is expensive
- Integrating with non-React code that manages the input

Use controlled inputs when you need to react to each change: live validation, formatting, disabling a button until valid, or syncing the value with other UI. Libraries like React Hook Form use uncontrolled inputs with refs to get good performance with a nice API.

### 285: Why is a file input always uncontrolled?

The value of `<input type="file">` can only be set by the user for security reasons. You can't set it from code. So you read the selected files in `onChange` or through a ref or `FormData`.

```jsx
function Upload() {
  function handleChange(e) {
    const file = e.target.files[0];
    if (file) uploadFile(file);
  }
  return <input type="file" onChange={handleChange} />;
}
```

### 286: Why does the cursor jump to the end of a controlled input?

This happens when the input's new value isn't set synchronously during the change event. For example, if you update the value after an `await`, or in a transition, or if you change the value (like formatting) so it no longer matches what the user typed. React then sets a different value than the DOM has and the browser moves the cursor.

Fixes: update the state synchronously in `onChange`, don't wrap input state updates in `startTransition`, and for slow parts of the UI use `useDeferredValue` instead of delaying the input itself.

### 287: How do you handle global UI state like toasts and modals?

A common approach is a provider with context and a portal.

```jsx
const ToastContext = createContext(null);

function ToastProvider({ children }) {
  const [toasts, setToasts] = useState([]);

  const show = useCallback((message) => {
    const id = crypto.randomUUID();
    setToasts((t) => [...t, { id, message }]);
    setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), 3000);
  }, []);

  return (
    <ToastContext value={show}>
      {children}
      {createPortal(
        <div className="toasts" role="status">
          {toasts.map((t) => (
            <div key={t.id}>{t.message}</div>
          ))}
        </div>,
        document.body,
      )}
    </ToastContext>
  );
}

const useToast = () => useContext(ToastContext);
```

Any component can call `useToast()("Saved!")`. Because the context value is a stable function, consumers don't re-render when toasts change.

### 288: How do you add internationalization (i18n) to a React app?

Use a library such as `react-i18next`, `react-intl` (FormatJS) or Lingui. They give you translation lookups, plurals and formatting.

```jsx
import { useTranslation } from "react-i18next";

function Greeting({ name }) {
  const { t } = useTranslation();
  return <p>{t("greeting", { name })}</p>;
}
```

For dates and numbers you can also use the built-in `Intl` APIs. Be careful with SSR: the server and client must use the same locale and time zone, or you get hydration mismatches.

### 289: How do you write code that only runs in development?

Check `process.env.NODE_ENV` (or `import.meta.env.DEV` in Vite). Bundlers replace it with a constant, and the dead branch is removed from the production build.

```js
if (process.env.NODE_ENV !== "production") {
  console.warn("This prop is deprecated");
}

if (import.meta.env.DEV) {
  enableMockApi();
}
```

### 290: How do you protect routes in a client-side React app?

Check auth state and redirect if the user isn't logged in.

```jsx
import { Navigate, Outlet, useLocation } from "react-router";

function RequireAuth() {
  const { user } = useAuth();
  const location = useLocation();

  if (!user) {
    return <Navigate to="/login" replace state={{ from: location }} />;
  }
  return <Outlet />;
}

<Route element={<RequireAuth />}>
  <Route path="/dashboard" element={<Dashboard />} />
</Route>;
```

Remember this only hides UI. Real protection has to happen on the server: every API call must check the user's permissions. In React Router framework mode or Next.js, you can do the check in a loader or middleware before rendering.

### 291: How do you implement infinite scroll?

Watch a sentinel element at the bottom of the list with `IntersectionObserver`, and load more when it becomes visible.

```jsx
function Feed() {
  const [items, setItems] = useState([]);
  const [page, setPage] = useState(1);
  const sentinelRef = useRef(null);

  useEffect(() => {
    let ignore = false;
    fetchPage(page).then((newItems) => {
      if (!ignore) setItems((prev) => [...prev, ...newItems]);
    });
    return () => {
      ignore = true;
    };
  }, [page]);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) setPage((p) => p + 1);
    });
    observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, []);

  return (
    <>
      {items.map((item) => (
        <Post key={item.id} post={item} />
      ))}
      <div ref={sentinelRef} />
    </>
  );
}
```

In real apps, `useInfiniteQuery` from TanStack Query handles pages, loading states and errors.

### 292: Write a hook that tracks the window size.

```jsx
function subscribe(callback) {
  window.addEventListener("resize", callback);
  return () => window.removeEventListener("resize", callback);
}

export function useWindowWidth() {
  return useSyncExternalStore(
    subscribe,
    () => window.innerWidth,
    () => 1024, // fallback on the server
  );
}
```

`getSnapshot` returns a number, so it's stable. If you returned an object like `{ width, height }`, you'd create a new object every time, and React would loop forever. In that case, keep two separate hooks or cache the object.

### 293: What are common causes of memory leaks in React apps?

- Subscriptions, event listeners or intervals without cleanup
- Async callbacks that keep references to large data after unmount
- Global caches or arrays that keep growing
- Closures in long-lived objects (like a global event bus) that capture component state
- Third-party library instances (charts, maps) that are never destroyed

The fix is almost always a proper cleanup function in `useEffect` or a ref callback. Note that the old warning "Can't perform a React state update on an unmounted component" was removed in React 18 because it was often misleading.

### 294: How do you animate list items entering and leaving?

React removes elements from the DOM immediately, so you need a way to keep them around during the exit animation. Common options:

- **Motion** (formerly Framer Motion) with `AnimatePresence`
- CSS transitions plus a library like `react-transition-group`
- The browser View Transitions API (React has an experimental `<ViewTransition>` component for this)

```jsx
import { AnimatePresence, motion } from "motion/react";

<AnimatePresence>
  {items.map((item) => (
    <motion.li
      key={item.id}
      initial={{ opacity: 0, y: -10 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0 }}
    >
      {item.text}
    </motion.li>
  ))}
</AnimatePresence>;
```

Stable keys are essential, otherwise the wrong items animate.

### 295: How do you use a non-React library (like a chart or map library) inside a component?

Give the library a DOM node through a ref, create it in an effect, update it when props change, and destroy it in cleanup.

```jsx
function Chart({ data }) {
  const containerRef = useRef(null);
  const chartRef = useRef(null);

  useEffect(() => {
    chartRef.current = new ChartLib(containerRef.current);
    return () => {
      chartRef.current.destroy();
      chartRef.current = null;
    };
  }, []);

  useEffect(() => {
    chartRef.current.setData(data);
  }, [data]);

  return <div ref={containerRef} />;
}
```

Let the library own everything inside that `<div>`. React shouldn't render children into it.

### 296: How do you protect against XSS in React?

React escapes all values put in JSX, so `<p>{userInput}</p>` is safe. Risks come from:

- `dangerouslySetInnerHTML` with untrusted HTML. Sanitize with DOMPurify first.
- URLs from users in `href` or `src`. Validate that they start with `http:` or `https:`.
- Directly setting `innerHTML` through refs.
- Server rendering where you put JSON into a `<script>` tag without escaping `<`.
- Spreading user-controlled objects as props, which could set unexpected attributes.

```jsx
import DOMPurify from "dompurify";

<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(comment.html) }} />;
```

### 297: What does React do with `javascript:` URLs?

React 19 blocks `javascript:` URLs in attributes like `href` and `src`. It replaces them with a safe value that throws an error if the link is used. React 16.9 started warning about them. This protects against a common XSS vector, but you should still validate URLs coming from users.

### 298: How do you handle errors from async code in event handlers?

Error boundaries don't catch errors from event handlers or plain promises. Use `try/catch` and put the error in state:

```jsx
function SaveButton() {
  const [error, setError] = useState(null);

  async function handleClick() {
    try {
      await save();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <>
      <button onClick={handleClick}>Save</button>
      {error && <p role="alert">{error}</p>}
    </>
  );
}
```

Alternatively, run the async work as an Action with `startTransition` or `useActionState`. Errors thrown inside a transition are sent to the nearest error boundary.

### 299: How would you structure folders in a medium-sized React project?

There's no single right way, but a common approach is grouping by feature instead of by file type:

```
src/
  app/            # app setup, routes, providers
  features/
    auth/
      components/
      hooks/
      api.ts
      index.ts
    cart/
  components/     # shared UI (Button, Modal)
  hooks/          # shared hooks
  lib/            # utilities, API client
```

Keep things that change together close together. Avoid very deep nesting. If you use a framework, follow its conventions for routes (like the `app` folder in Next.js).

### 300: Why shouldn't you disable the `react-hooks/exhaustive-deps` lint rule?

The rule makes sure every reactive value used in an effect, `useMemo` or `useCallback` is in the dependency array. If you ignore it, the effect uses stale values, which causes bugs that are hard to find.

If adding a dependency makes the effect run too often, the problem is usually in the code:

- Move functions or objects inside the effect
- Move constants outside the component
- Use updater functions (`setX(x => ...)`) to avoid depending on state
- Use `useEffectEvent` for logic that should read the latest value without re-running the effect
- Ask whether this should be an effect at all

The newer versions of `eslint-plugin-react-hooks` also include rules based on the React Compiler, which catch more problems like mutating props or reading refs during render.

---

## Advanced Questions (301-450)

### 301: How does the Fiber architecture work in more detail?

Each element in the tree gets a fiber node. A fiber holds:

- `type`, `key`, `pendingProps` and `memoizedProps`
- `memoizedState` (for function components, the linked list of hooks)
- `child`, `sibling` and `return` (parent) pointers, so the tree can be walked without recursion
- `flags` describing side effects (placement, update, deletion)
- `lanes` describing pending work priority
- `alternate`, pointing to the other version of this fiber

React keeps two trees: the **current** tree (what's on screen) and the **work-in-progress** tree (being built). During render, React walks the work-in-progress tree one fiber at a time with `beginWork` and `completeWork`. Because it's a loop over linked nodes and not a recursive call stack, React can stop after any unit of work and continue later. At commit, React swaps the pointers so the work-in-progress tree becomes current. This is called double buffering.

### 302: What are lanes in React?

Lanes are React's internal priority system. Each update gets a lane, which is a bit in a 31-bit bitmask. Examples are `SyncLane` (discrete events like clicks), `InputContinuousLane` (mouse move, scroll), `DefaultLane`, `TransitionLanes`, `RetryLanes` (Suspense retries) and `IdleLane`.

Because lanes are bits, React can cheaply group several updates into one render, check whether a fiber has work at a given priority, and process high priority lanes first while leaving lower ones for later. When you call `startTransition`, your updates go into a transition lane, so a click (sync lane) can interrupt them.

### 303: What does concurrent rendering actually mean?

It means React can prepare more than one version of the UI at the same time and can interrupt rendering. Rendering is no longer one big blocking task. If an urgent update arrives (like typing) while React is rendering a transition, React can pause or throw away the transition work, handle the urgent update, and then restart the transition.

It doesn't mean multi-threading. It's still one JavaScript thread. React just splits work into small pieces and checks between them whether it should yield. Concurrency is opt-in through features like `startTransition`, `useDeferredValue` and Suspense. Plain updates in event handlers still render synchronously.

### 304: How does React yield to the browser during rendering?

React's scheduler runs the work loop in time slices of about 5 milliseconds. After each fiber, during concurrent rendering, it checks `shouldYield()`. If the slice is used up, React stops and schedules a continuation with a `MessageChannel` message (not `setTimeout`, which has a minimum delay). This gives the browser a chance to handle input and paint.

Synchronous updates (from discrete events like clicks, or `flushSync`) don't yield. They render all at once.

### 305: When does React skip rendering a component (bailout)?

React skips calling a component, and reuses its previous output, when all of these are true:

- Its props object is the same reference as last time (or shallowly equal if it's wrapped in `memo`)
- It has no pending state updates
- The context values it reads haven't changed

If the component bails out, React also checks whether any children have pending work. If none do, it skips the whole subtree. This is why the "pass children as props" trick works: elements created by the parent keep the same reference when only the wrapper component's own state changes.

### 306: Why does a component sometimes render once more even when I set state to the same value?

React uses `Object.is` to compare the new state with the current one. If they're equal, React usually skips the render. But in some cases React can't know that early, so it calls the component once more and only then sees that nothing changed. It then throws away the result and doesn't render the children or commit anything.

So setting the same value is cheap, but not always zero cost. It's not something you need to optimize in normal code.

### 307: How are hooks stored internally?

For each function component, the fiber's `memoizedState` points to a linked list of hook objects. Each call to `useState`, `useEffect`, `useMemo` and so on during render moves to the next item in that list.

```
fiber.memoizedState → [useState hook] → [useEffect hook] → [useMemo hook] → null
```

On the first render React creates the list. On later renders it walks the same list in the same order. A `useState` hook object holds its current state and a queue of pending updates. An effect hook holds the effect function, deps and cleanup.

### 308: Why do hooks need to be called in the same order every render?

Because React identifies hooks by their position in the call order, not by a name. If a hook is skipped in one render because of an `if`, all later hooks get matched with the wrong stored data.

```jsx
function Form({ showName }) {
  if (showName) {
    const [name, setName] = useState(""); // hook #1 sometimes
  }
  const [email, setEmail] = useState(""); // hook #1 or #2
}
```

When `showName` flips, `email` reads the state of the old `name` hook. React detects this and throws "Rendered more hooks than during the previous render" or similar errors. `use` is the exception because it doesn't store anything in the hook list in the same way.

### 309: What is tearing and how does `useSyncExternalStore` prevent it?

Tearing is when different parts of the UI show different values for the same data in the same frame. With concurrent rendering, React can pause in the middle of a render. If an external store changes during that pause, components rendered before the pause show the old value and components rendered after show the new one.

`useSyncExternalStore` prevents this. It checks the snapshot again before committing. If the store changed during rendering, React re-renders synchronously so the whole tree shows one consistent value. The cost is that updates from external stores can't be non-blocking transitions in the same way React state updates can.

### 310: What is `getServerSnapshot` for?

It's the third argument to `useSyncExternalStore`. React uses it during server rendering and during hydration on the client. It must return the same value on server and client, so the initial HTML matches.

```jsx
const isOnline = useSyncExternalStore(
  subscribe,
  () => navigator.onLine,
  () => true, // assume online during SSR and hydration
);
```

After hydration, React switches to `getSnapshot` and re-renders if the value differs. If you leave it out and the component is server-rendered, React throws an error, which makes the nearest Suspense boundary render on the client only.

### 311: Why should state libraries use `useSyncExternalStore` instead of `useState` + `useEffect` subscriptions?

The old pattern was:

```jsx
const [state, setState] = useState(store.getState());
useEffect(() => store.subscribe(() => setState(store.getState())), []);
```

Problems with it:

- Updates that happen between render and the effect running are missed
- With concurrent rendering, different components can read different values (tearing)
- It doesn't support server snapshots for hydration

`useSyncExternalStore` handles all of this. That's why Redux, Zustand and other libraries moved to it in React 18.

### 312: How does Suspense work internally?

When a component needs data that isn't ready, it throws a promise (or `use` does something equivalent internally). React catches it in the render loop, finds the closest `<Suspense>` boundary above, and renders its fallback instead. React attaches a callback to the promise and, when it resolves, schedules a retry render of that boundary.

You shouldn't throw promises yourself. That was never a public API. Use `use(promise)`, `lazy`, or a library that supports Suspense. React 19 uses a special internal exception (`SuspenseException`) for `use`, and tracks thenables so it can sometimes unwrap an already resolved promise without suspending.

### 313: Why can't you create the promise inside the component that calls `use`?

```jsx
function Profile({ id }) {
  const user = use(fetch(`/api/users/${id}`).then((r) => r.json())); // bad
}
```

When the component suspends, React throws away that render. When the promise resolves, React renders the component again, which creates a brand new promise, which suspends again. You get an endless loop of requests.

The promise must be stable across renders. Create it outside the component (in a loader, a Server Component, an event handler) or store it in a cache keyed by its arguments:

```js
const cache = new Map();
export function fetchUser(id) {
  if (!cache.has(id)) {
    cache.set(
      id,
      fetch(`/api/users/${id}`).then((r) => r.json()),
    );
  }
  return cache.get(id);
}
```

In Client Components, React warns if you pass a promise created during render that isn't cached.

### 314: What changed about Suspense sibling rendering in React 19?

In React 18, when one component inside a Suspense boundary suspended, React kept rendering its siblings before showing the fallback. That pre-rendering delayed the fallback.

In React 19, when a component suspends, React commits the fallback right away, so users see the loading state sooner. Then it "pre-warms" the siblings in the background so their lazy code and data requests start early. This avoids the delay, though it initially caused some discussion because it can create waterfalls for data fetched inside sibling components. The general advice is to start data fetching early (at the route level) instead of inside each component.

### 315: What is selective hydration?

With streaming SSR and Suspense, the page doesn't have to hydrate all at once. Each Suspense boundary can hydrate on its own once its code and HTML are ready. React hydrates in the background and in small slices, so the page stays responsive.

If the user interacts with a part that hasn't hydrated yet, React gives that boundary higher priority and hydrates it first. So a slow comments section doesn't block the header from becoming interactive.

### 316: What happens to user events that fire before hydration finishes?

React records discrete events (like clicks) that happen on not-yet-hydrated Suspense boundaries. It hydrates the target boundary with high priority, then replays the event so the handler runs as if the page was ready. For continuous events (like mouse moves), React only uses them to raise the hydration priority and doesn't replay them.

### 317: What is the RSC payload?

When Server Components render, they don't produce HTML directly. They produce a serialized description of the UI, often called the RSC payload or Flight format. It contains:

- The rendered output of Server Components (elements, text)
- References to Client Components (module ID and export name), with the props to pass them
- Serialized props, promises, and Server Function references

On the client, React reads this stream and builds the tree, loading Client Component code as needed. For the initial page load, frameworks also run the payload through SSR to produce HTML, and embed the payload in the page so the client can hydrate without re-fetching. On navigation, the client fetches just the payload for the new route.

### 318: How do bundlers handle `"use client"` boundaries?

The bundler (with React's integration package like `react-server-dom-webpack`, `react-server-dom-turbopack` or `react-server-dom-parcel`) builds two module graphs: one for the server, one for the client.

When the server graph reaches a file with `"use client"`, it doesn't include the real component. It replaces the exports with client references, which are objects saying "module X, export Y". When a Server Component renders one, React writes that reference into the payload. The client bundle contains the real code, and the client looks it up by that reference.

That's why `"use client"` marks a boundary in the module graph, not individual components. Everything imported from that file is client code.

### 319: Why must props passed from Server to Client Components be serializable?

The Server Component runs on the server, and the Client Component runs in the browser. Props have to travel over the network inside the RSC payload. A function, class instance or DOM node can't be turned into data and recreated on the other side. Server Functions are the exception: React sends a reference (an ID), and calling it makes a request back to the server.

### 320: How does calling a Server Function work under the hood?

1. The bundler sees `"use server"` and on the client side replaces the function with a reference containing an ID.
2. When the client calls it, React serializes the arguments (using the same serialization rules as the RSC payload, plus `FormData`) and sends a POST request to the server with the function ID.
3. The server finds the function by ID, deserializes arguments, runs it, and serializes the return value.
4. The client receives the result. Frameworks can also send back an updated RSC payload, so the UI refreshes with new server data in the same round trip.

Because the endpoint is reachable by anyone, arguments must be validated and authorization checked inside the function.

### 321: How do forms with Server Functions support progressive enhancement?

If you pass a Server Function to `<form action>`, React renders the form in SSR so it can submit as a normal HTML form even before JavaScript loads. The framework handles the POST, runs the function and returns a new page.

With `useActionState`, you can also pass a `permalink` as the third argument. If the form is submitted before hydration, the browser navigates to that URL, where the same form component is rendered so React can pass the state through.

```jsx
const [state, formAction] = useActionState(subscribe, null, "/newsletter");
```

Once JavaScript loads, the same form works without a full page reload.

### 322: What is `cache` in React?

`cache` is a function for Server Components that memoizes a function's result for the duration of a single server request.

```jsx
import { cache } from "react";

export const getUser = cache(async (id) => {
  return db.users.find(id);
});

async function Header() {
  const user = await getUser(1);
}

async function Sidebar() {
  const user = await getUser(1); // reuses the same result, one DB call
}
```

The cache is reset for each request, so data doesn't leak between users. Arguments are compared by reference (`Object.is`), so pass primitives, not new objects. Call `cache` at module level, not inside a component, otherwise each component gets its own cache. It's only available in Server Components.

### 323: What is `cacheSignal`?

`cacheSignal` (React 19.2) returns an `AbortSignal` that is aborted when the current `cache()` lifetime ends. That happens when the render finishes, is aborted, or fails. You use it in Server Components to cancel work whose result is no longer needed.

```jsx
import { cache, cacheSignal } from "react";

const getProduct = cache(async (id) => {
  const res = await fetch(`https://api.example.com/products/${id}`, {
    signal: cacheSignal(),
  });
  return res.json();
});
```

If the request is cancelled (for example the user navigated away), the fetch is aborted instead of finishing for nothing.

### 324: What is Partial Pre-rendering in React 19.2?

It lets you pre-render the static parts of a page ahead of time (at build time or on a CDN), and fill in the dynamic parts later.

```js
import { prerender } from "react-dom/static";
import { resume } from "react-dom/server";

// At build time
const controller = new AbortController();
const { prelude, postponed } = await prerender(<App />, {
  signal: controller.signal,
});
// save postponed state, serve prelude from the CDN

// At request time
const stream = await resume(<App />, postponed);
// stream the rest of the content into the page
```

The parts that can't be pre-rendered are left as Suspense fallbacks in the prelude. At request time, `resume` renders those parts and streams them in. There are also Node stream versions (`prerenderToNodeStream`, `resumeToPipeableStream`), and `resumeAndPrerender` if you want to resume into static HTML instead of a stream. Frameworks like Next.js build their own features on top of these APIs.

### 325: What is the difference between `prerender` and `renderToReadableStream`?

Both are server APIs. `renderToReadableStream` (in `react-dom/server`) starts streaming as soon as the shell is ready and sends the rest as data loads. It's for dynamic, per-request rendering.

`prerender` (in `react-dom/static`) waits until all data is loaded before resolving, and gives you the complete HTML. It's meant for static site generation. In 19.2 it can also be aborted to produce a partial result plus `postponed` state for resuming later.

### 326: What are the limitations of `renderToString`?

`renderToString` renders synchronously to a string. It doesn't support streaming and doesn't wait for data. When a component suspends, it immediately renders the Suspense fallback into the HTML, and the real content is rendered on the client. It also blocks the server until it's done.

It's still OK for simple cases, like rendering an email template. For pages, use `renderToPipeableStream` or `renderToReadableStream`. For static generation, use `prerender`.

### 327: How do you handle errors in streaming SSR?

`renderToPipeableStream` gives you callbacks:

```js
let didError = false;

const { pipe, abort } = renderToPipeableStream(<App />, {
  bootstrapScripts: ["/main.js"],
  onShellReady() {
    res.statusCode = didError ? 500 : 200;
    res.setHeader("content-type", "text/html");
    pipe(res);
  },
  onShellError(error) {
    res.statusCode = 500;
    res.send("<h1>Something went wrong</h1>");
  },
  onError(error) {
    didError = true;
    console.error(error);
  },
});

setTimeout(() => abort(), 10000);
```

- If an error happens inside a Suspense boundary, React sends the fallback for that boundary and tries to render it again on the client. If it fails there too, the nearest error boundary handles it.
- If the shell itself fails, `onShellError` runs, and you send a fallback page.
- `abort()` stops waiting and renders remaining boundaries on the client.

### 328: How did hydration error handling improve in React 19?

- Instead of several vague warnings, React logs one error with a diff of the server and client output.
- React 19 skips unexpected tags in `<head>` and `<body>` that were added by browser extensions or third-party scripts, so they don't cause mismatch errors anymore.
- Stylesheets inserted by extensions are kept.
- `onRecoverableError` on `hydrateRoot` lets you report mismatches React recovered from (it re-renders the boundary on the client).

### 329: What exactly happens inside a hidden `<Activity>`?

- The children's DOM stays but is hidden with `display: none`.
- Effects are cleaned up (like an unmount), so subscriptions and timers stop. Layout effects are cleaned up too.
- State and DOM state are kept.
- The subtree can still re-render when its props change, but at the lowest priority, after visible work is done.
- When it becomes visible, effects are created again.

During SSR, a hidden `Activity` doesn't render its children into the HTML. Also, a hidden `Activity` takes part in pre-rendering: React can render content inside it before it's shown, so data and code load early and the reveal is instant.

### 330: What are the rules and limits of `useEffectEvent`?

- Only call the function it returns from inside effects (or other effect events). Don't call it during rendering.
- Don't pass it to other components or hooks.
- Don't add it to dependency arrays; the linter knows to leave it out.
- Don't use it just to avoid listing dependencies you actually need. It's for logic that is "event-like": it should run because the effect fired, using the latest values, but it shouldn't cause the effect to fire.

A good test: if a value changes, should the effect re-synchronize? If yes, it's a dependency. If no, and you only need its latest value when the effect does something, read it inside an effect event.

### 331: How do you build an optimistic update that rolls back on error?

With `useOptimistic` the rollback is automatic: the optimistic value only lives while the action is running. You just need to show the error.

```jsx
function LikeButton({ liked, onToggle }) {
  const [optimisticLiked, setOptimisticLiked] = useOptimistic(liked);
  const [error, setError] = useState(null);
  const [, startTransition] = useTransition();

  function handleClick() {
    startTransition(async () => {
      setOptimisticLiked(!optimisticLiked);
      try {
        await onToggle(!liked); // updates the real "liked" in the parent on success
        setError(null);
      } catch (err) {
        setError("Could not save. Try again.");
        // no manual rollback: when the transition ends, the value goes back to "liked"
      }
    });
  }

  return (
    <>
      <button onClick={handleClick}>{optimisticLiked ? "♥" : "♡"}</button>
      {error && <span role="alert">{error}</span>}
    </>
  );
}
```

Without `useOptimistic` (for example with TanStack Query), you'd save the previous value before the mutation and restore it in `onError`.

### 332: Why do state updates after `await` inside `startTransition` lose their transition status?

React marks updates as transitions by setting a global flag while your callback runs synchronously. When your async function hits `await`, the callback returns, React resets the flag, and the code after `await` runs later in a microtask without the flag set. So `setState` there is treated as a normal update.

```jsx
startTransition(async () => {
  await save();
  setPage("done"); // not a transition
  startTransition(() => setPage("done")); // is a transition
});
```

The pending state still covers the whole async function, because React tracks the returned promise. The fix will come once JavaScript has a standard way to carry context across `await` (the AsyncContext proposal). Until then, wrap post-`await` updates in `startTransition` again.

### 333: How does `useActionState` handle multiple quick submissions?

Calls to the action are queued and run one after another, not in parallel. Each call receives the state returned by the previous call. This keeps the state consistent but means a slow request delays later ones.

If you need parallel requests or cancelling old ones, `useActionState` isn't a good fit. Use `useTransition` with your own logic, or a data library. For cases like "add to cart" where order matters, the queueing is helpful.

### 334: How would you design a simple data fetching layer that works with Suspense?

You need a cache so the same request returns the same promise across renders, and a way to invalidate it.

```jsx
const cache = new Map();

export function getData(url) {
  if (!cache.has(url)) {
    const promise = fetch(url).then((r) => {
      if (!r.ok) throw new Error(r.statusText);
      return r.json();
    });
    cache.set(url, promise);
  }
  return cache.get(url);
}

export function invalidate(url) {
  cache.delete(url);
}

function Product({ id }) {
  const product = use(getData(`/api/products/${id}`));
  return <h1>{product.name}</h1>;
}
```

Problems you'd still need to solve: cache size limits, failed requests staying cached, refetching on focus, mutations, and SSR. That's why the docs recommend using a framework or a library like TanStack Query or Relay instead of rolling your own.

### 335: How do you avoid waterfalls in Server Components?

Awaiting one after another in the same component creates a waterfall:

```jsx
async function Page({ id }) {
  const user = await getUser(id);
  const posts = await getPosts(id); // waits for getUser even though it doesn't need it
}
```

Start independent requests together:

```jsx
async function Page({ id }) {
  const [user, posts] = await Promise.all([getUser(id), getPosts(id)]);
}
```

Or start promises early and let children await them inside their own Suspense boundaries:

```jsx
function Page({ id }) {
  const postsPromise = getPosts(id); // not awaited
  return (
    <>
      <UserHeader id={id} />
      <Suspense fallback={<PostsSkeleton />}>
        <Posts postsPromise={postsPromise} />
      </Suspense>
    </>
  );
}
```

Also be careful with nested components that each fetch, because a child can't start until its parent finishes awaiting.

### 336: How do you pass a promise from a Server Component to a Client Component?

Start the fetch on the server without awaiting, pass the promise as a prop, and read it on the client with `use`.

```jsx
// Server Component
import Comments from "./Comments";

export default async function Post({ id }) {
  const post = await getPost(id);
  const commentsPromise = getComments(id); // not awaited

  return (
    <article>
      <h1>{post.title}</h1>
      <Suspense fallback={<p>Loading comments...</p>}>
        <Comments commentsPromise={commentsPromise} />
      </Suspense>
    </article>
  );
}
```

```jsx
"use client";
import { use } from "react";

export default function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map((c) => <p key={c.id}>{c.text}</p>);
}
```

The post content streams first. The comments stream in when the promise resolves. The resolved value must be serializable.

### 337: How do you let users retry after an error in a Suspense-based component?

Combine an error boundary that can reset with a way to clear the failed request from the cache.

```jsx
import { ErrorBoundary } from "react-error-boundary";

function ProductSection({ id }) {
  return (
    <ErrorBoundary
      onReset={() => invalidate(`/api/products/${id}`)}
      fallbackRender={({ error, resetErrorBoundary }) => (
        <div>
          <p>Failed to load: {error.message}</p>
          <button onClick={resetErrorBoundary}>Retry</button>
        </div>
      )}
    >
      <Suspense fallback={<Spinner />}>
        <Product id={id} />
      </Suspense>
    </ErrorBoundary>
  );
}
```

If the cached rejected promise isn't removed, resetting the boundary just throws the same error again. TanStack Query has `QueryErrorResetBoundary` for this.

### 338: How do errors in Server Components work?

If a Server Component throws, the error is serialized into the RSC payload at that point in the tree. On the client, React throws it again inside the matching position, so the nearest client error boundary catches it. In production, frameworks replace the error message with a generic one and a digest (an ID) so server details aren't exposed, and you find the real error in server logs.

For expected errors, like "not found" or validation errors, it's better to return a value and render something specific than to throw.

### 339: How does the React Compiler work internally?

1. It parses each component and hook with Babel.
2. It converts the code into its own intermediate representation (HIR, a control flow graph).
3. It runs analysis passes: which values are reactive (depend on props, state, context), which values are mutated and where, and which values can be grouped together.
4. It builds "reactive scopes", groups of code that produce a value from the same inputs.
5. It generates code that stores each scope's result in a per-component cache array, and only recomputes when inputs change.

The output looks roughly like this:

```js
import { c as _c } from "react/compiler-runtime";

function Greeting({ name }) {
  const $ = _c(2);
  let t0;
  if ($[0] !== name) {
    t0 = <h1>Hello {name}</h1>;
    $[0] = name;
    $[1] = t0;
  } else {
    t0 = $[1];
  }
  return t0;
}
```

`_c` is a hook (`useMemoCache`) that gives the component a fixed-size cache array that lives on the fiber.

### 340: How do you adopt the React Compiler gradually or opt out?

- Use `compilationMode: "annotation"` to compile only functions with a `"use memo"` directive, then grow from there.
- Use the `sources` option (or framework config) to compile only certain folders.
- Put `"use no memo"` at the top of a component or file to opt it out, as a temporary escape hatch while you fix a problem.

```jsx
function LegacyWidget() {
  "use no memo";
  // compiler skips this component
}
```

Check that the lint rules from `eslint-plugin-react-hooks` pass before enabling it in a module. Run your tests, especially on code that relied on mutation or on effects firing at specific times.

### 341: When does the React Compiler skip a component?

The compiler skips (bails out on) a component or hook when it can't prove the optimization is safe. Common reasons:

- Mutating props, state, or values after they were used in JSX
- Reading or writing `ref.current` during render
- Conditional hook calls or other rules-of-hooks violations
- Some JavaScript patterns it doesn't support yet
- Code that the linter flags with suppressions like `// eslint-disable-next-line react-hooks/...`

When it skips, the component still works exactly as before, just without automatic memoization. The ESLint rules show these issues so you can fix them.

### 342: How do the newer `eslint-plugin-react-hooks` rules relate to the compiler?

Recent versions of `eslint-plugin-react-hooks` include rules powered by the same analysis as the compiler (the separate `eslint-plugin-react-compiler` was merged into it). Besides `rules-of-hooks` and `exhaustive-deps`, they catch things like:

- Setting state during render in a way that causes loops
- Mutating values that should be immutable (props, state, hook arguments)
- Reading refs during render
- Calling impure functions like `Date.now()` during render
- Creating components during render

You get these warnings even if you don't use the compiler. They point to code that may break with concurrent rendering anyway.

### 343: Why can using objects as effect dependencies cause problems, and what are the options?

React compares dependencies with `Object.is`. An object or array created during render is a new reference every time, so the effect runs after every render.

```jsx
function Chat({ roomId, serverUrl }) {
  const options = { roomId, serverUrl }; // new object every render
  useEffect(() => {
    const conn = createConnection(options);
    conn.connect();
    return () => conn.disconnect();
  }, [options]); // reconnects every render
}
```

Options:

1. Create the object inside the effect and depend on primitives (`[roomId, serverUrl]`). This is usually best.
2. Memoize it with `useMemo` (or let the compiler do it).
3. Destructure primitive values from object props before the effect.

Deep comparison hooks (`useDeepCompareEffect`) exist but they're slower and can hide design problems.

### 344: How would you build a small global store with selectors using `useSyncExternalStore`?

```jsx
import { useSyncExternalStore } from "react";

function createStore(initialState) {
  let state = initialState;
  const listeners = new Set();

  return {
    getState: () => state,
    setState(updater) {
      state = typeof updater === "function" ? updater(state) : updater;
      listeners.forEach((l) => l());
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}

const store = createStore({ count: 0, user: null });

function useStore(selector) {
  return useSyncExternalStore(
    store.subscribe,
    () => selector(store.getState()),
    () => selector(store.getState()),
  );
}

function Count() {
  const count = useStore((s) => s.count); // re-renders only when count changes
  return (
    <button
      onClick={() => store.setState((s) => ({ ...s, count: s.count + 1 }))}
    >
      {count}
    </button>
  );
}
```

The selector must return a stable value. If it returns a new object each time (like `s => ({ a: s.a })`), you need extra memoization, which is what `useSyncExternalStoreWithSelector` from the `use-sync-external-store` package does.

### 345: Why doesn't Context support selectors, and how do people work around it?

`useContext` subscribes to the whole value. When it changes (by reference), every consumer re-renders, even if it only uses one field. React has explored context selectors but hasn't shipped them.

Workarounds:

- Split into several smaller contexts
- Put a stable store object in context (that never changes) and subscribe to parts of it with `useSyncExternalStore`. This is how libraries like Zustand (with a provider), Jotai and `use-context-selector` work.
- Memoize expensive children so the re-render is cheap
- Let the React Compiler reduce the cost of re-rendering

### 346: How can you avoid re-rendering expensive children when a parent's state changes, without `memo`?

Move the state down, or lift the expensive content up and pass it as `children`.

```jsx
// Before: typing re-renders ExpensiveTree
function App() {
  const [color, setColor] = useState("red");
  return (
    <div style={{ color }}>
      <input value={color} onChange={(e) => setColor(e.target.value)} />
      <ExpensiveTree />
    </div>
  );
}

// After: ExpensiveTree is created by App, which doesn't re-render
function App() {
  return (
    <ColorPicker>
      <ExpensiveTree />
    </ColorPicker>
  );
}

function ColorPicker({ children }) {
  const [color, setColor] = useState("red");
  return (
    <div style={{ color }}>
      <input value={color} onChange={(e) => setColor(e.target.value)} />
      {children}
    </div>
  );
}
```

`children` is the same element object between `ColorPicker` renders, so React bails out on it.

### 347: What are React Performance Tracks?

React 19.2 adds custom tracks to the Performance panel in Chrome DevTools. When you record a profile in a development (or profiling) build, you see:

- A **Scheduler** track showing the work React is doing by priority (blocking, transition, and so on), including when updates are scheduled and when React is waiting
- A **Components** track showing which components rendered and ran effects, and how long each took

This makes it easier to connect React work with other browser activity like network requests, layout and paint, in one timeline.

### 348: What information does the Profiler's `onRender` callback give you?

```js
function onRender(
  id,
  phase,
  actualDuration,
  baseDuration,
  startTime,
  commitTime,
) {}
```

- `id`: the `id` prop of the Profiler
- `phase`: `"mount"`, `"update"` or `"nested-update"`
- `actualDuration`: time spent rendering this commit (lower when memoization works)
- `baseDuration`: estimated time to render the whole subtree without memoization (worst case)
- `startTime`: when React started rendering this update
- `commitTime`: when React committed this update

Comparing `actualDuration` to `baseDuration` tells you how much memoization is helping. To use it in production you need the profiling build of `react-dom` (`react-dom/profiling`).

### 349: What should you watch out for when building a virtualized list?

- **Variable heights**: you need to measure items after render and adjust positions, which can cause scroll jumps.
- **Keys**: use item IDs, not the virtual index, or state jumps between items while scrolling.
- **Scroll restoration** when navigating back.
- **Accessibility**: screen readers and Ctrl+F only see rendered items. Use `aria-rowcount`/`aria-setsize` and `aria-posinset` where it makes sense.
- **Overscan**: render a few extra items to avoid blank areas during fast scroll.
- **Sticky headers and grids** add complexity.

Sometimes CSS `content-visibility: auto` is a simpler option: the browser skips layout and paint for offscreen items while they stay in the DOM.

### 350: How do you speed up a slow list that doesn't need virtualization?

- Make sure keys are stable so React doesn't recreate rows
- Wrap the row component in `memo` and keep row props stable (or use the compiler)
- Avoid passing the whole list or a changing callback to every row
- Move per-row state into the row, not the parent
- Use `useDeferredValue` for filtering so typing stays smooth
- Use `content-visibility: auto` in CSS for long pages
- Paginate or load more on scroll

Measure with the Profiler before and after each change.

### 351: How can closures cause memory issues in React?

Every function created during render captures the variables of that render. If that function is stored somewhere long-lived, everything it references stays in memory.

```jsx
function Report({ hugeData }) {
  useEffect(() => {
    globalEmitter.on("export", () => exportData(hugeData)); // never removed
  }, [hugeData]);
}
```

Each time `hugeData` changes, a new listener captures a new large object, and none are released. Always remove listeners in cleanup. Also watch for caches (like a `Map` at module level) that hold on to data per component and are never cleared.

### 352: What is the issue with `useLayoutEffect` and server rendering?

Layout effects don't run on the server, because there's no layout there. If your component's first paint depends on a layout effect, the server HTML shows one thing and the client changes it right after hydration, causing a jump.

Older React versions printed a warning about this. React 19 no longer warns, but the visual problem is still there. Options:

- Render a version that doesn't depend on measurement on the server, then adjust on the client
- Only render the component on the client (for example after a `useEffect` sets `mounted` to true)
- Use CSS for the layout instead of measuring

You may see an `useIsomorphicLayoutEffect` helper in libraries that picks `useEffect` on the server and `useLayoutEffect` on the client.

### 353: What are the pitfalls of `flushSync`?

- It forces a synchronous render, skipping batching and concurrent features, so it can hurt performance.
- Calling it inside a render or inside an effect causes a warning; it can't flush while React is already rendering.
- It can make Suspense boundaries show their fallback, because the update isn't a transition.
- Overusing it to "fix" timing problems usually hides a design issue.

Good uses: scrolling to a newly added item, updating the DOM before `window.print()`, or integrating with third-party code that needs the DOM updated right away.

### 354: How do you position a tooltip based on its own size without flicker?

Render it, measure it in `useLayoutEffect`, then set the position before the browser paints.

```jsx
function Tooltip({ targetRect, children }) {
  const ref = useRef(null);
  const [height, setHeight] = useState(0);

  useLayoutEffect(() => {
    const { height } = ref.current.getBoundingClientRect();
    setHeight(height);
  }, []);

  let top = targetRect.top - height;
  if (top < 0) top = targetRect.bottom; // flip below if no room

  return createPortal(
    <div
      ref={ref}
      className="tooltip"
      style={{ position: "fixed", top, left: targetRect.left }}
    >
      {children}
    </div>,
    document.body,
  );
}
```

React runs the first render, the layout effect sets state, and React re-renders synchronously before paint. The user only sees the final position. For real projects, Floating UI handles edge cases like scrolling and collision detection.

### 355: How would you design an imperative API for a component with `useImperativeHandle`?

Keep it small and focused on actions that can't be expressed as props. Return stable methods, and include dependencies if they use props.

```jsx
function Carousel({ items, ref }) {
  const [index, setIndex] = useState(0);
  const listRef = useRef(null);

  useImperativeHandle(
    ref,
    () => ({
      next() {
        setIndex((i) => Math.min(i + 1, items.length - 1));
      },
      prev() {
        setIndex((i) => Math.max(i - 1, 0));
      },
      scrollToItem(i) {
        listRef.current.children[i]?.scrollIntoView({ behavior: "smooth" });
        setIndex(i);
      },
    }),
    [items.length],
  );

  return <ul ref={listRef}>{/* ... */}</ul>;
}
```

Don't expose internal state setters that let parents control things that should be props, like `setItems`. If the parent needs to control the index, make `index` a prop instead.

### 356: How do you observe an element's size when the element can mount and unmount?

A ref callback with cleanup handles this well, because it runs when the node is attached and detached.

```jsx
function useElementSize() {
  const [size, setSize] = useState({ width: 0, height: 0 });

  const ref = useCallback((node) => {
    if (!node) return;
    const observer = new ResizeObserver(([entry]) => {
      const { width, height } = entry.contentRect;
      setSize({ width, height });
    });
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return [ref, size];
}

function Panel() {
  const [ref, { width }] = useElementSize();
  return <div ref={ref}>Width: {width}</div>;
}
```

The callback must be stable (with `useCallback` or the compiler). If it's a new function every render, React calls the cleanup and the new callback on every render.

### 357: How do you build an accessible modal without the native `<dialog>` element?

- Render through a portal to `document.body`
- Use `role="dialog"`, `aria-modal="true"` and `aria-labelledby`
- Move focus into the modal on open, and restore focus to the trigger on close
- Trap focus with Tab and Shift+Tab inside the modal
- Close on Escape
- Make the rest of the page unreachable: set the `inert` attribute on the main app container (React 19 supports `inert` as a boolean prop)
- Prevent background scrolling

```jsx
<div id="app" inert={isModalOpen}>
  ...
</div>
```

Because so many details are involved, most teams use Radix UI, React Aria or Headless UI.

### 358: What is a custom React renderer?

React's core (the reconciler) doesn't know about the DOM. Renderers connect it to a platform. `react-dom` is one, React Native is another. The `react-reconciler` package lets you build your own by implementing a "host config": functions like `createInstance`, `appendChild`, `commitUpdate` and `removeChild`.

Examples of custom renderers: React Three Fiber (3D with Three.js), Ink (command line apps), `react-pdf`, and renderers for canvas or native desktop UIs. They get hooks, state, context and Suspense for free.

### 359: How does React Native's New Architecture relate to React?

React Native's New Architecture (default since React Native 0.76) replaced the old asynchronous bridge with JSI (direct calls between JavaScript and native code), a new renderer called Fabric, and TurboModules for native modules. Fabric supports concurrent React features like transitions and Suspense, and synchronous layout reads, which the old renderer couldn't do. So React Native apps can now use the same React 18/19 features as the web.

### 360: What exactly does Strict Mode do in React 19?

In development only:

- Calls component functions, initializers, updater functions and reducers twice, to find impure code. In React 19, during the second render it reuses memoized results from `useMemo` and `useCallback` of the first render.
- Runs every effect setup, cleanup and setup again on mount, to find missing cleanup.
- Calls ref callbacks twice on mount (attach, detach, attach), to check ref cleanup.
- Warns about deprecated APIs (like `UNSAFE_` lifecycles in class components).

It doesn't change production behavior. Console logs from the second render are dimmed in React DevTools.

### 361: What does it mean for an effect to be "resilient to remounting"?

Running setup → cleanup → setup should give the same visible result as running setup once. Patterns:

```jsx
// Subscriptions: subscribe and unsubscribe
useEffect(() => {
  const unsub = store.subscribe(onChange);
  return unsub;
}, []);

// Widgets: create and destroy
useEffect(() => {
  const map = new MapWidget(ref.current);
  return () => map.destroy();
}, []);

// Animations: reset on cleanup
useEffect(() => {
  ref.current.style.opacity = 1;
  return () => {
    ref.current.style.opacity = 0;
  };
}, []);
```

Some things aren't naturally reversible, like a POST request to "buy" something. Those don't belong in effects at all. They belong in event handlers. This matters beyond Strict Mode, since features like `<Activity>` and Fast Refresh also mount and unmount effects without the component going away.

### 362: What are owner stacks and `captureOwnerStack`?

An owner stack shows which components rendered the component where a problem happened, as opposed to the parent stack, which shows the nesting in the tree. For example, if `<Page>` creates `<Button>` and passes it as children to `<Card>`, the owner of `Button` is `Page`, not `Card`. Owner stacks point you to the code that actually created the element.

React 19.1 added `captureOwnerStack()`, available in development only, so you can include the owner stack in your own error logging.

```js
import { captureOwnerStack } from "react";

const root = createRoot(container, {
  onCaughtError(error, info) {
    console.error(error, info.componentStack, captureOwnerStack());
  },
});
```

In production it returns `null`.

### 363: How does React 19 report errors differently from React 18?

In React 18, an error in rendering was thrown, caught by React, then re-thrown, and also logged, so you'd often see the same error two or three times in the console.

In React 19:

- Uncaught errors (no error boundary) are reported once with `window.reportError`.
- Errors caught by an error boundary are reported with `console.error`.
- Recoverable errors (like hydration mismatches) are logged once.
- You can control all three with `onUncaughtError`, `onCaughtError` and `onRecoverableError` on the root.

This makes error monitoring tools see each error once, with the component stack in `errorInfo`.

### 364: Why must rendering be pure for concurrent features to work?

With concurrent rendering, React may:

- Render a component and then throw the result away (an interrupted transition)
- Render it several times before committing
- Render content in the background that isn't shown yet (`<Activity>`, pre-warming)

If rendering has side effects, like changing a global variable, sending analytics or mutating a prop, those effects happen for renders the user never saw, or happen multiple times. Pure rendering means React can render as often as it wants, at any priority, and the result is only what gets committed.

### 365: Why shouldn't you read or write `ref.current` during render?

Refs are mutable and React doesn't track them. If you read a ref during render:

- The value may change without a re-render, so the UI shows stale data
- With concurrent rendering, two renders can see different values
- The React Compiler assumes refs aren't read in render, and it may cache JSX that used the ref value

Writing to a ref during render is worse, because a render that gets thrown away still changed the ref. The exception is lazy initialization (`if (ref.current === null) ref.current = ...`), because it always produces the same result.

### 366: What can go wrong if you mutate props or state?

```jsx
function List({ items }) {
  items.sort((a, b) => a.name.localeCompare(b.name)); // mutates the parent's array
  return items.map((i) => <Row key={i.id} item={i} />);
}
```

- The parent's data changes without the parent knowing
- `memo`, `useMemo` and the compiler compare by reference, so they think nothing changed and skip updates
- Strict Mode's double render can produce different results
- Time-travel debugging and undo stop working
- Concurrent renders that get thrown away still left their mutations behind

Always create new objects: `const sorted = items.toSorted(...)`.

### 367: How do you make sure secrets never reach Client Components?

- Keep secret access in modules that only run on the server.
- Import the `server-only` package at the top of those modules. If a Client Component imports them, the build fails.
- Only pass the fields the client needs as props, not whole database records. Use a DTO (data transfer object) layer.
- Don't put secrets in environment variables with client prefixes (`NEXT_PUBLIC_`, `VITE_`).
- Remember that anything passed to a Client Component as a prop ends up in the RSC payload in the page source.

React also has experimental "taint" APIs (`experimental_taintObjectReference`, `experimental_taintUniqueValue`) that throw if a marked object or value is passed to the client. They're a safety net, not a replacement for the steps above.

### 368: What are the `server-only` and `client-only` packages?

They're tiny packages that make the build fail when code is imported in the wrong environment.

```js
// lib/db.js
import "server-only";

export async function getSecretData() {
  return fetch(url, { headers: { Authorization: process.env.API_KEY } });
}
```

If a `"use client"` file imports `lib/db.js`, bundlers that support the `react-server` export condition (like Next.js) throw a build error. `client-only` does the opposite for code that uses browser APIs.

### 369: Do you need `"use client"` in every interactive component?

No. `"use client"` is only needed at the entry point of the client part of the tree, the file that a Server Component imports. Everything imported by that file is already client code.

```
page.jsx (server)
 └─ imports Counter.jsx  ← needs "use client"
       └─ imports Button.jsx ← doesn't need it, already client
```

Adding it to every file isn't harmful in most cases, but it makes those files entry points and their props must be serializable. Also, a component without the directive can be a Server Component in one place and a Client Component in another, depending on who imports it.

### 370: Can a Client Component import a Server Component?

No. When a Client Component imports a module, that module becomes part of the client bundle. If the "Server Component" uses server-only things (like a database or `async`), it breaks. The supported way is to pass Server Components as props (usually `children`) from a parent Server Component, so they're rendered on the server and the Client Component just places the result.

### 371: Can you use Context in Server Components?

No. Server Components can't create or read context, because context is part of the client runtime that tracks values through the tree. Options:

- For data needed by many Server Components in one request, use `cache()` functions, which act like request-scoped storage.
- For context that Client Components need, create a Client Component provider and render it from a Server Component:

```jsx
// ThemeProvider.jsx
"use client";
export function ThemeProvider({ theme, children }) {
  return <ThemeContext value={theme}>{children}</ThemeContext>;
}

// layout.jsx (Server Component)
export default async function Layout({ children }) {
  const theme = await getUserTheme();
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
}
```

Server Components passed as `children` still render on the server; only Client Components below can read the context.

### 372: How does streaming work with Server Components and Suspense?

When a Server Component awaits slow data inside a Suspense boundary, React sends the rest of the tree immediately with the fallback in that spot. When the data resolves, React streams the rendered content for that boundary as another chunk of the RSC payload (and of the HTML during the initial SSR). The client puts it in place.

```jsx
export default function Page() {
  return (
    <>
      <Header />
      <Suspense fallback={<FeedSkeleton />}>
        <Feed /> {/* async, slow */}
      </Suspense>
    </>
  );
}
```

Without the boundary, the whole page would wait for `Feed`. Frameworks often add route-level boundaries (like `loading.js` in Next.js).

### 373: How do you refresh data on the page after a Server Function mutates it?

That part is handled by the framework, since React itself doesn't have a router or cache. Common approaches:

- **Next.js**: call `revalidatePath("/posts")` or `revalidateTag("posts")` inside the Server Action, and the framework sends updated RSC payload in the response.
- **React Router**: after an `action` finishes, loaders on the page run again automatically.
- **Client cache libraries**: invalidate the query (`queryClient.invalidateQueries`) after the mutation.

The goal is one round trip: mutate and get fresh UI back, instead of a second fetch.

### 374: How do you return validation errors from a form action?

Return them as state from the action, and render them with `useActionState`.

```jsx
"use server";
import { z } from "zod";

const Schema = z.object({
  email: z.string().email(),
  name: z.string().min(2),
});

export async function signup(prevState, formData) {
  const result = Schema.safeParse(Object.fromEntries(formData));
  if (!result.success) {
    return {
      errors: result.error.flatten().fieldErrors,
      values: Object.fromEntries(formData),
    };
  }
  await createUser(result.data);
  return { errors: {}, success: true };
}
```

```jsx
"use client";
export function SignupForm() {
  const [state, action, pending] = useActionState(signup, { errors: {} });
  return (
    <form action={action}>
      <input name="email" defaultValue={state.values?.email} />
      {state.errors.email && <p>{state.errors.email[0]}</p>}
      <input name="name" defaultValue={state.values?.name} />
      {state.errors.name && <p>{state.errors.name[0]}</p>}
      <button disabled={pending}>Sign up</button>
    </form>
  );
}
```

Returning the submitted values matters because React resets uncontrolled fields after the action finishes, so without them the user would lose what they typed.

### 375: Why does `useFormStatus` return `pending: false` in my form?

`useFormStatus` reads the status of the nearest parent `<form>` in the tree. If you call it in the same component that renders the `<form>`, there's no parent form, so it's always idle.

```jsx
// Doesn't work
function Form() {
  const { pending } = useFormStatus();
  return (
    <form action={submit}>
      <button disabled={pending}>Go</button>
    </form>
  );
}

// Works
function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>Go</button>;
}

function Form() {
  return (
    <form action={submit}>
      <SubmitButton />
    </form>
  );
}
```

It also only works with forms that use a function as `action`, not with `onSubmit` handlers.

### 376: How do you have several buttons in one form that do different things?

Use `formAction` on the buttons. Each button can submit the form to a different action.

```jsx
function PostEditor() {
  return (
    <form action={publish}>
      <textarea name="content" />
      <button type="submit">Publish</button>
      <button type="submit" formAction={saveDraft}>
        Save draft
      </button>
    </form>
  );
}
```

Both actions receive the same `FormData`. You can also give buttons a `name` and `value` and check `formData.get("intent")` in one action.

### 377: How do you combine `useOptimistic` with `useActionState`?

```jsx
function TodoList({ todos }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo) => [...state, { ...newTodo, pending: true }],
  );

  const [state, formAction, isPending] = useActionState(
    async (prev, formData) => {
      const title = formData.get("title");
      addOptimisticTodo({ id: crypto.randomUUID(), title });
      const result = await createTodo(title); // server function, revalidates todos
      return result.error ? { error: result.error } : { error: null };
    },
    { error: null },
  );

  return (
    <>
      <ul>
        {optimisticTodos.map((t) => (
          <li key={t.id} style={{ opacity: t.pending ? 0.5 : 1 }}>
            {t.title}
          </li>
        ))}
      </ul>
      <form action={formAction}>
        <input name="title" />
        <button disabled={isPending}>Add</button>
      </form>
      {state.error && <p role="alert">{state.error}</p>}
    </>
  );
}
```

The action runs inside a transition, so `addOptimisticTodo` is allowed there. The new item shows right away and disappears or gets replaced when `todos` updates from the server.

### 378: How do you avoid flashing spinners for fast transitions?

- Use `isPending` from `useTransition` and show the indicator only after a short delay with CSS (for example `animation-delay: 300ms` on the spinner), so fast updates never show it.
- Keep old content visible (dimmed) instead of switching to a fallback, which transitions already do for content that's on screen.
- Use skeletons in Suspense fallbacks that match the final layout to reduce layout shifts.

React itself also throttles Suspense reveals: when content resolves, React waits a short time (around 300ms) to group nearby boundaries and reveal them together, instead of popping each one in separately.

### 379: What changed about revealing Suspense boundaries during SSR in React 19.2?

Before 19.2, during streaming SSR each Suspense boundary was revealed as soon as its content arrived, which could cause many small layout shifts and didn't match how client rendering grouped reveals.

In 19.2, React batches the reveal of server-rendered Suspense boundaries for a short time, so several boundaries that finish close together appear at once. This makes server rendering behave like client rendering and prepares for animating reveals with View Transitions. React makes sure this doesn't hurt Core Web Vitals like LCP.

### 380: What is `<ViewTransition>`?

`<ViewTransition>` is a React component that uses the browser's View Transitions API to animate changes in the UI, like page navigations, list reorders and Suspense reveals. React decides when to start the view transition based on transitions and Suspense, and applies the `view-transition-name` for you.

```jsx
import { unstable_ViewTransition as ViewTransition } from "react";

<ViewTransition>
  <Page key={url} />
</ViewTransition>;
```

At the time of writing it's only available in React's canary and experimental channels, and its API may still change. Check the React docs for its current status before using it in production.

### 381: How do routers use transitions?

When you click a link, a Suspense-enabled router wraps the navigation in `startTransition`. That way:

- The current page stays on screen while the next page loads, instead of showing a fallback for the whole page
- The router can show a pending indicator using the transition's pending state
- If you click another link, the first navigation's render is abandoned
- The browser stays responsive while the new page renders

Next.js App Router and React Router both do this. That's why calling `startTransition` around your own state updates during navigation behaves well with Suspense.

### 382: When should you use `useDeferredValue` instead of `useTransition`?

Use `useTransition` when you control the state update and can wrap the `setState` call. Use `useDeferredValue` when you receive a value you don't control, like a prop or a value from a third-party hook, and want the slow part of the UI to lag behind it.

```jsx
function Results({ query }) {
  // query comes from a parent
  const deferredQuery = useDeferredValue(query);
  return <SlowList query={deferredQuery} />;
}
```

Both use the same mechanism underneath: a low-priority render that can be interrupted.

### 383: Can concurrent rendering cause problems with layout effects or refs?

Layout effects and refs only run in the commit phase, which is synchronous, so they always see a consistent DOM. Problems usually come from code that runs during render and assumes it will be committed:

- Measuring the DOM during render (it may be from an old commit)
- Starting animations in render
- Assuming a render is followed immediately by its layout effect (an interrupted render never commits)

Keep DOM reading in layout effects, event handlers or ref callbacks, never in the component body.

### 384: How do you render content that depends on the browser (like `localStorage` or the current time) without hydration errors?

Render the same thing on the server and in the first client render, then update after hydration.

```jsx
function Greeting() {
  const [name, setName] = useState(null);

  useEffect(() => {
    setName(localStorage.getItem("name"));
  }, []);

  return <p>Hello{name ? `, ${name}` : ""}!</p>;
}
```

This causes one extra render after hydration but no mismatch. For values from browser APIs that can change, `useSyncExternalStore` with a `getServerSnapshot` is cleaner. For things like dates, you can also format on the server in a fixed time zone, or pass the server time to the client.

### 385: How do you detect whether code is running on the client after hydration without an extra state variable?

Use `useSyncExternalStore` with different server and client snapshots.

```jsx
const emptySubscribe = () => () => {};

function useIsClient() {
  return useSyncExternalStore(
    emptySubscribe,
    () => true, // client
    () => false, // server and hydration
  );
}

function ClientOnly({ children, fallback = null }) {
  return useIsClient() ? children : fallback;
}
```

During hydration React uses the server snapshot (`false`), so the HTML matches. Then it re-renders with `true`. On later client-only mounts (after navigation), it's `true` from the start, so there's no flash. The `useEffect` + `useState` approach always renders the fallback first.

### 386: How would you build a modal manager that can open modals from anywhere?

```jsx
const ModalContext = createContext(null);

export function ModalProvider({ children }) {
  const [stack, setStack] = useState([]);

  const api = useMemo(
    () => ({
      open(render) {
        const id = crypto.randomUUID();
        setStack((s) => [...s, { id, render }]);
        return id;
      },
      close(id) {
        setStack((s) => s.filter((m) => m.id !== id));
      },
    }),
    [],
  );

  return (
    <ModalContext value={api}>
      <div inert={stack.length > 0}>{children}</div>
      {stack.map(({ id, render }) =>
        createPortal(
          <div className="backdrop" key={id}>
            {render(() => api.close(id))}
          </div>,
          document.body,
        ),
      )}
    </ModalContext>
  );
}

export const useModal = () => useContext(ModalContext);

// usage
const modal = useModal();
modal.open((close) => (
  <ConfirmDialog
    onCancel={close}
    onConfirm={() => {
      deleteItem();
      close();
    }}
  />
));
```

Points to discuss: stacking (only the top modal handles Escape), focus restoration, scroll locking, and that `render` functions stored in state capture values from when they were opened.

### 387: How would you build accessible Tabs as compound components?

```jsx
const TabsContext = createContext(null);

function Tabs({ children, defaultValue }) {
  const [value, setValue] = useState(defaultValue);
  const baseId = useId();
  return (
    <TabsContext value={{ value, setValue, baseId }}>{children}</TabsContext>
  );
}

function TabList({ children }) {
  function handleKeyDown(e) {
    const tabs = [...e.currentTarget.querySelectorAll('[role="tab"]')];
    const i = tabs.indexOf(document.activeElement);
    if (e.key === "ArrowRight") tabs[(i + 1) % tabs.length].focus();
    if (e.key === "ArrowLeft")
      tabs[(i - 1 + tabs.length) % tabs.length].focus();
  }
  return (
    <div role="tablist" onKeyDown={handleKeyDown}>
      {children}
    </div>
  );
}

function Tab({ value, children }) {
  const ctx = use(TabsContext);
  const selected = ctx.value === value;
  return (
    <button
      role="tab"
      id={`${ctx.baseId}-tab-${value}`}
      aria-selected={selected}
      aria-controls={`${ctx.baseId}-panel-${value}`}
      tabIndex={selected ? 0 : -1}
      onClick={() => ctx.setValue(value)}
      onFocus={() => ctx.setValue(value)}
    >
      {children}
    </button>
  );
}

function TabPanel({ value, children }) {
  const ctx = use(TabsContext);
  if (ctx.value !== value) return null;
  return (
    <div
      role="tabpanel"
      id={`${ctx.baseId}-panel-${value}`}
      aria-labelledby={`${ctx.baseId}-tab-${value}`}
    >
      {children}
    </div>
  );
}
```

This uses a roving `tabIndex` (only the selected tab is in the Tab order), arrow key navigation, and `useId` for SSR-safe IDs.

### 388: How do you type a polymorphic component (an `as` prop) in TypeScript?

```tsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & Omit<React.ComponentProps<C>, "as" | "children">;

function Text<C extends React.ElementType = "span">({
  as,
  children,
  ...rest
}: TextProps<C>) {
  const Component = as ?? "span";
  return <Component {...rest}>{children}</Component>;
}

<Text as="a" href="/home">Home</Text>          // href is allowed
<Text as="button" onClick={() => {}}>Hi</Text> // onClick typed for button
```

Because `ref` is a normal prop in React 19, `ComponentProps<C>` includes it, so refs work without `forwardRef` and its typing problems with generics. Many libraries use an `asChild` pattern (Radix `Slot`) instead, which avoids this typing complexity.

### 389: How do you type a component that accepts a `ref` in React 19?

Include `ref` in the props type, either directly or through `ComponentProps`.

```tsx
type InputProps = {
  label: string;
  ref?: React.Ref<HTMLInputElement>;
} & Omit<React.ComponentProps<"input">, "ref">;

function Input({ label, ref, ...rest }: InputProps) {
  return (
    <label>
      {label}
      <input ref={ref} {...rest} />
    </label>
  );
}

const inputRef = useRef<HTMLInputElement>(null);
<Input label="Name" ref={inputRef} />;
```

`React.Ref<T>` accepts both ref objects and ref callbacks.

### 390: How do you type a generic custom hook so callers get good inference?

```tsx
function useLocalStorage<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    const raw = localStorage.getItem(key);
    return raw !== null ? (JSON.parse(raw) as T) : initial;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}

const [theme, setTheme] = useLocalStorage("theme", "light" as "light" | "dark");
```

`as const` makes the return type a tuple `[T, Dispatch<SetStateAction<T>>]` instead of an array of a union type, so destructuring keeps the right types. Note that `JSON.parse` isn't type-safe; for untrusted data, validate with a schema.

### 391: How do you type a Server Function used as a form action?

A function passed directly to `<form action>` receives `FormData`. With `useActionState` it receives the previous state first.

```tsx
"use server";

type State = { error: string | null };

export async function updateName(
  prev: State,
  formData: FormData,
): Promise<State> {
  const name = formData.get("name");
  if (typeof name !== "string" || name.length < 2) {
    return { error: "Name is too short" };
  }
  await db.user.update({ name });
  return { error: null };
}
```

`formData.get()` returns `FormDataEntryValue | null` (a string or a `File`), so you need to check the type. Never assume the shape is correct, since anyone can call the function with any data.

### 392: How do you use discriminated unions for component props?

When some props only make sense together, model them as a union so invalid combinations don't compile.

```tsx
type ButtonProps =
  | { variant: "link"; href: string; onClick?: never }
  | { variant: "button"; onClick: () => void; href?: never };

function Action(props: ButtonProps) {
  if (props.variant === "link") {
    return <a href={props.href}>Go</a>;
  }
  return <button onClick={props.onClick}>Go</button>;
}

<Action variant="link" href="/home" />          // OK
<Action variant="button" href="/home" />        // Error
```

Note: if you destructure the props in the parameter list, TypeScript can lose the narrowing, so check `props.variant` first.

### 393: How do you test components that use `use()` and Suspense?

Render inside a `<Suspense>` boundary, pass a promise you control, and use async queries.

```jsx
import { Suspense } from "react";
import { render, screen } from "@testing-library/react";

test("shows user after loading", async () => {
  const userPromise = Promise.resolve({ name: "Alice" });

  render(
    <Suspense fallback={<p>Loading...</p>}>
      <UserName userPromise={userPromise} />
    </Suspense>,
  );

  expect(await screen.findByText("Alice")).toBeInTheDocument();
});
```

For the error case, pass a rejected promise and wrap in an error boundary. Remember that the promise must be created outside the component, just like in real code. Don't create it inside the component under test.

### 394: How do you test Server Components?

Testing support for async Server Components in unit test tools is still limited. Common approaches:

- Test the logic separately: data access functions and Server Functions are regular async functions you can unit test.
- For simple async Server Components, you can `await` the component as a function and render the result: `render(await Page({ params }))`. This works when the component and its children don't need a real RSC environment.
- Test Client Components with React Testing Library as usual.
- Use end-to-end tests (Playwright, Cypress) for the full flow through the framework.

### 395: What is a good testing strategy for a large React app?

A rough split:

- **Static checks**: TypeScript and ESLint (including the hooks and a11y plugins) catch a lot for free.
- **Unit tests** for pure functions, reducers, and custom hooks with complex logic.
- **Integration tests** with React Testing Library for components and features: render a screen, interact like a user, mock the network with MSW. These give most of the confidence.
- **End-to-end tests** with Playwright for critical user flows (login, checkout) against a real build.
- **Visual regression tests** (Storybook with Chromatic, or Playwright screenshots) for design systems.

Test behavior, not implementation details like internal state or component names.

### 396: How do you test an error boundary?

Render a component that throws and check that the fallback shows. Silence `console.error` for the test since React logs caught errors.

```jsx
function Bomb() {
  throw new Error("Boom");
}

test("shows fallback on error", () => {
  const spy = vi.spyOn(console, "error").mockImplementation(() => {});

  render(
    <ErrorBoundary fallback={<p>Something went wrong</p>}>
      <Bomb />
    </ErrorBoundary>,
  );

  expect(screen.getByText("Something went wrong")).toBeInTheDocument();
  spy.mockRestore();
});
```

### 397: What are the challenges of micro-frontends with React?

- **Multiple React copies**: if each micro-frontend bundles React, hooks break when components from one are rendered by another ("Invalid hook call"). Module Federation with React as a shared singleton solves this.
- **Version alignment**: shared React requires compatible versions across teams.
- **Bundle size**: duplicated dependencies add up.
- **Shared state and routing**: need clear contracts (URL, events, or a small shared store).
- **Styling conflicts**: CSS needs scoping.

If parts truly need different React versions, mount each one in its own root on separate DOM nodes and communicate through events or URLs, never by passing React elements between them.

### 398: Can you have multiple React roots on one page, and how do they share state?

Yes. Call `createRoot` on several DOM nodes. Each root is independent: separate trees, no shared context.

```jsx
createRoot(document.getElementById("header-widget")).render(<CartIcon />);
createRoot(document.getElementById("product-page")).render(<AddToCart />);
```

To share state, use an external store (Zustand, Redux, or a custom `useSyncExternalStore` store) that both roots import. Updates in one root then show up in the other. Alternatively, use one root and render the other parts into those nodes with portals, which keeps a single tree and shared context.

### 399: How do you add React to an existing non-React page?

Install React, build your components, and mount them on specific elements.

```jsx
import { createRoot } from "react-dom/client";

document.querySelectorAll("[data-react-comments]").forEach((node) => {
  const postId = node.dataset.postId;
  createRoot(node).render(<Comments postId={postId} />);
});
```

React only controls those nodes. The rest of the page keeps working as before. You can slowly move more of the page into React over time.

### 400: How do you unmount a React root?

Call `root.unmount()`. React removes the tree, runs all effect cleanups, and clears the container.

```jsx
const root = createRoot(container);
root.render(<Widget />);

// later
root.unmount();
```

This is important when React lives inside a larger non-React app that removes the container, otherwise listeners and subscriptions leak. `ReactDOM.unmountComponentAtNode` was removed in React 19.

### 401: How does React 19 support Web Components (custom elements)?

React 19 fully supports custom elements. Before, React passed all props to custom elements as string attributes, which broke objects, arrays and event listeners. Now:

- During client rendering, if the custom element has a property with that name, React sets it as a property; otherwise it's set as an attribute.
- During SSR, primitive values are rendered as attributes, and objects/functions are skipped.
- Event props are attached as listeners for custom events.

```jsx
<my-chart data={chartData} onpointselect={handleSelect} theme="dark" />
```

React 19 passes all tests on Custom Elements Everywhere, a site that checks framework support.

### 402: Which React events behave differently from native DOM events?

- `onScroll` doesn't bubble in React (since React 17), matching browser behavior.
- `onMouseEnter`, `onMouseLeave`, `onPointerEnter` and `onPointerLeave` don't bubble; React handles them specially.
- `onChange` fires on every input, like the native `input` event.
- `onFocus` and `onBlur` bubble in React (they use `focusin` and `focusout` under the hood since React 17).
- `onDoubleClick` instead of `ondblclick`.

When something seems off, check `e.nativeEvent` to see the real browser event.

### 403: Why can't you call `preventDefault()` in a React `onWheel` or `onTouchMove` handler?

Since React 17, React registers `touchstart`, `touchmove` and `wheel` listeners as passive, so the browser can scroll smoothly without waiting for JavaScript. In a passive listener, `preventDefault()` is ignored and the browser warns.

If you need to block scrolling (for example zooming a canvas with the wheel), add a non-passive listener yourself:

```jsx
useEffect(() => {
  const node = ref.current;
  function onWheel(e) {
    e.preventDefault();
    zoom(e.deltaY);
  }
  node.addEventListener("wheel", onWheel, { passive: false });
  return () => node.removeEventListener("wheel", onWheel);
}, []);
```

### 404: What does "A component is changing an uncontrolled input to be controlled" mean?

The input started with `value={undefined}` (uncontrolled) and later got a real value (controlled). React doesn't support switching modes during an input's lifetime.

```jsx
const [user, setUser] = useState({});
<input value={user.name} onChange={...} /> // undefined at first
```

Fix it by always passing a defined value:

```jsx
<input value={user.name ?? ""} onChange={...} />
```

The opposite warning ("controlled to uncontrolled") happens when the value becomes `undefined` or `null` later.

### 405: How would you implement undo and redo?

Keep a history of states with a reducer.

```jsx
function undoable(reducer) {
  const initial = { past: [], present: undefined, future: [] };

  return function (state = initial, action) {
    const { past, present, future } = state;
    switch (action.type) {
      case "UNDO":
        if (past.length === 0) return state;
        return {
          past: past.slice(0, -1),
          present: past.at(-1),
          future: [present, ...future],
        };
      case "REDO":
        if (future.length === 0) return state;
        return {
          past: [...past, present],
          present: future[0],
          future: future.slice(1),
        };
      default: {
        const next = reducer(present, action);
        if (next === present) return state;
        return { past: [...past, present], present: next, future: [] };
      }
    }
  };
}

const [state, dispatch] = useReducer(undoable(editorReducer), {
  past: [],
  present: initialDoc,
  future: [],
});
```

Immutable updates make this cheap, since unchanged parts of the state are shared between history entries. Limit the history length for large documents.

### 406: When would you use a state machine for UI state?

When a component has several states with strict rules about which transitions are allowed: multi-step forms, payment flows, media players, drag and drop. Booleans like `isLoading`, `isError`, `isSuccess` can end up in impossible combinations. A state machine makes the possible states explicit.

```jsx
function reducer(state, event) {
  switch (state.status) {
    case "idle":
      if (event.type === "SUBMIT") return { status: "submitting" };
      return state;
    case "submitting":
      if (event.type === "SUCCESS") return { status: "success" };
      if (event.type === "FAILURE")
        return { status: "error", error: event.error };
      return state;
    case "error":
      if (event.type === "RETRY") return { status: "submitting" };
      return state;
    default:
      return state;
  }
}
```

For complex cases, XState gives you visual tools, nested and parallel states, and actors.

### 407: Without the compiler, how would you cache an expensive calculation that many components need?

`useMemo` caches per component instance. If many components compute the same thing from the same input, options are:

- Compute it once higher up and pass it down (or through context)
- Use a module-level memoized selector (like `reselect`'s `createSelector`) keyed on input references
- Store the derived value in an external store that recomputes on change
- Use a `WeakMap` cache keyed by the input object

```js
const cache = new WeakMap();
export function getStats(data) {
  if (!cache.has(data)) cache.set(data, computeStats(data));
  return cache.get(data);
}
```

A `WeakMap` lets the cache entry be garbage-collected when the data object is no longer used.

### 408: How do you keep a large form fast?

- Use uncontrolled inputs (React Hook Form, or plain `FormData`), so typing doesn't re-render the whole form
- If inputs are controlled, keep state per field component instead of one big object at the top
- Split the form into memoized sections
- Run validation on blur or submit instead of every keystroke, or debounce it
- Use `useDeferredValue` for expensive previews based on form values
- Virtualize very long repeated field lists

```jsx
import { useForm } from "react-hook-form";

function Profile() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();
  return (
    <form onSubmit={handleSubmit(save)}>
      <input {...register("email", { required: true })} />
      {errors.email && <span>Required</span>}
    </form>
  );
}
```

### 409: What does "Too many re-renders" mean?

React stopped an infinite loop where state is set during render, which triggers another render, which sets state again.

```jsx
function Counter() {
  const [count, setCount] = useState(0);
  setCount(count + 1); // runs on every render
  return <button onClick={setCount(0)}>Reset</button>; // also called during render
}
```

Common causes: calling a setter at the top level of a component without a condition, or calling a function instead of passing it to an event prop. Fix: `onClick={() => setCount(0)}`, and only set state during render inside a condition that stops after one update.

### 410: When is it okay to set state during render?

Only for the state of the component that's currently rendering, and only inside a condition that becomes false after the update. React supports this to adjust state based on changed props without an extra effect render.

```jsx
function CountLabel({ count }) {
  const [prevCount, setPrevCount] = useState(count);
  const [trend, setTrend] = useState(null);

  if (prevCount !== count) {
    setPrevCount(count);
    setTrend(count > prevCount ? "increasing" : "decreasing");
  }

  return (
    <h1>
      {count} {trend && `(${trend})`}
    </h1>
  );
}
```

React re-runs the component immediately with the new state, before rendering children. Setting state of a different component during render is not allowed and causes the warning "Cannot update a component while rendering a different component".

### 411: What are the costs of resetting a component with `key`?

Changing the key unmounts the old subtree and mounts a new one. That means:

- All DOM nodes in the subtree are recreated (slower than an update for large trees)
- All state below is lost, including state you might want to keep (like scroll position or an open dropdown)
- Effects clean up and run again, which may refetch data

It's the right tool when you really want a fresh instance (a different user's form). If only one piece of state should reset, adjust just that state, or put the key on a smaller part of the tree.

### 412: Why does a component keep its state when you swap it with a ternary?

```jsx
{
  isPlayerA ? <Counter person="Taylor" /> : <Counter person="Sarah" />;
}
```

Both branches render `Counter` at the same position, so React sees the same component type in the same place and keeps the state. Only the `person` prop changes. To make them separate, either give them different keys or render them in different positions:

```jsx
{
  isPlayerA ? (
    <Counter key="Taylor" person="Taylor" />
  ) : (
    <Counter key="Sarah" person="Sarah" />
  );
}
```

### 413: Why is calling a HOC inside a component a bug?

```jsx
function Page() {
  const EnhancedList = withSorting(List); // new component type every render
  return <EnhancedList items={items} />;
}
```

Every render creates a new function, so React sees a different component type and remounts the whole subtree, losing state and DOM. It's the same problem as defining a component inside another component. Call HOCs at module level:

```jsx
const EnhancedList = withSorting(List);
function Page() {
  return <EnhancedList items={items} />;
}
```

### 414: What problems do HOCs have with refs and static methods?

- **Refs**: before React 19, a `ref` on the HOC result pointed to the wrapper, not the inner component, unless the HOC used `forwardRef`. In React 19 `ref` is a prop for function components, so a HOC that spreads `{...props}` passes it through automatically.
- **Static methods**: statics on the wrapped component (like `Component.preload`) aren't copied to the wrapper. Libraries used `hoist-non-react-statics` for this.
- **Display name**: set ``Wrapped.displayName = `withX(${name})` `` for nicer DevTools output.
- **Prop collisions**: the HOC and the parent might both set the same prop.

### 415: How can you make lazy-loaded components load faster when the user needs them?

Start loading the code before the component renders, for example on hover or when the route is likely.

```jsx
const loadSettings = () => import("./Settings");
const Settings = lazy(loadSettings);

function Nav() {
  return (
    <Link to="/settings" onMouseEnter={loadSettings} onFocus={loadSettings}>
      Settings
    </Link>
  );
}
```

The browser caches the module, so when `lazy` calls the same import later, it resolves immediately. You can also preload during idle time, or let the framework prefetch route code for visible links (Next.js does this by default).

### 416: How do you analyze and reduce the bundle size of a React app?

- Visualize the bundle: `rollup-plugin-visualizer` for Vite, `@next/bundle-analyzer` for Next.js
- Split code by route and by heavy components (`lazy`)
- Replace large libraries (moment → date-fns or `Intl`, lodash → per-function imports or native methods)
- Make sure imports allow tree-shaking (ES modules, avoid importing whole libraries)
- Move non-interactive parts to Server Components so their code isn't shipped at all
- Check for duplicate packages in the lockfile

Measure the result with Lighthouse or real user monitoring, not only the bundle size.

### 417: What are the differences between React's development and production builds?

Development builds include:

- Warnings and detailed error messages
- Extra checks (keys, hook rules, Strict Mode double-invoking)
- Component stacks and owner stacks
- Performance tracks and DevTools features

Production builds strip all of that, are minified, and are much faster. Errors in production have short codes with a link to the full message. Never measure performance on a development build. Bundlers pick the right build based on `NODE_ENV`.

### 418: How do you handle authentication in an app with Server Components and Server Functions?

- Read the session (cookie or token) on the server, in middleware, layouts, or data access functions.
- Check authorization close to the data: in the data access layer or inside each Server Function, not only in a layout. Layouts may not re-run on every navigation, and Server Functions can be called directly.
- Use `httpOnly`, `secure`, `sameSite` cookies for sessions.
- Pass only what the client needs (like the user's name), not the session token.
- Rely on the framework's CSRF protections for Server Actions (for example Origin header checks), and keep the framework updated.

```js
import "server-only";
import { cache } from "react";

export const getCurrentUser = cache(async () => {
  const session = await getSession();
  if (!session) return null;
  return db.users.find(session.userId);
});
```

### 419: What happens in the UI when a Server Function throws?

If it's called inside a transition (as a form action, through `useActionState`, or inside `startTransition`), the error is thrown again on the client and goes to the nearest error boundary. With `useActionState`, the error also ends the queued actions.

In production, the error message is replaced by a generic one so server details don't leak. For expected problems (validation, permission), return a value describing the error instead of throwing, so you can show a helpful message in the form.

### 420: How do you use React's server rendering in edge runtimes?

Edge runtimes (Cloudflare Workers, Deno, Bun, Vercel Edge) use Web Streams instead of Node streams, so use `renderToReadableStream`:

```js
import { renderToReadableStream } from "react-dom/server";

export default {
  async fetch(request) {
    const stream = await renderToReadableStream(<App url={request.url} />, {
      bootstrapScripts: ["/client.js"],
      onError(error) {
        console.error(error);
      },
    });
    return new Response(stream, {
      headers: { "content-type": "text/html" },
    });
  },
};
```

The promise resolves when the shell is ready. If you need the complete HTML (for bots), await `stream.allReady` before returning the response.

### 421: What do `bootstrapScripts` and `bootstrapModules` do?

They tell the server rendering APIs which scripts to include in the HTML to start the client app (which calls `hydrateRoot`).

```js
renderToPipeableStream(<App />, {
  bootstrapScripts: ["/main.js"], // <script src="/main.js" async>
  bootstrapModules: ["/entry.mjs"], // <script type="module">
  bootstrapScriptContent: "window.__INITIAL_DATA__ = ...",
});
```

React emits them so the browser can start downloading early and they don't block the HTML. In React 19 there's also an `importMap` option for module import maps. Be careful with `bootstrapScriptContent`: if you put data in it, escape it so it can't close the script tag.

### 422: How does React 19 handle duplicate `<meta>` or `<title>` tags rendered by different components?

React hoists each `<title>`, `<meta>` and `<link>` to the head, but it doesn't merge or override them. If two components render `<title>`, you get two, and the browser uses the first. Stylesheets (`<link rel="stylesheet" precedence>`) and async scripts are deduplicated by `href`/`src`, but metadata tags aren't.

So in larger apps you still want one place that decides the final metadata for a route: either render `<title>` only in page-level components, or use your framework's metadata API, which merges values from nested layouts.

### 423: How do you start loading critical resources early in a Server Component?

Call React DOM's resource functions during render. In SSR they're added to the `<head>` of the HTML. In RSC, they're sent in the payload so the client preloads them.

```jsx
import { preload, preinit } from "react-dom";

export default async function ProductPage({ id }) {
  preload(`/images/products/${id}-large.webp`, {
    as: "image",
    fetchPriority: "high",
  });
  preinit("/styles/product.css", { as: "style", precedence: "default" });
  const product = await getProduct(id);
  return <Product product={product} />;
}
```

Because `preload` is called before `await`, the browser can start downloading the image while the server is still fetching data.

### 424: How does `fetchPriority` help in React apps?

`fetchPriority` (`"high"`, `"low"`, `"auto"`) is a browser attribute on `<img>`, `<link>` and `<script>` that hints at loading priority. React 19 passes it through correctly.

```jsx
<img src={hero} alt="" fetchPriority="high" />          // LCP image
<img src={thumb} alt="" loading="lazy" fetchPriority="low" />
```

Use `high` for the largest above-the-fold image to improve LCP, and lazy load images below the fold.

### 425: Are updates outside React event handlers batched?

Yes, since React 18 with `createRoot`, updates are batched everywhere: in timeouts, promises, native event listeners and third-party callbacks. Updates in the same microtask are grouped into one render.

```js
socket.on("message", (msg) => {
  setMessages((m) => [...m, msg]);
  setUnread((u) => u + 1);
  // one render
});
```

The priority depends on the source: updates from discrete events (click, keydown) are synchronous priority, while updates from timeouts or network callbacks get default priority.

### 426: How can you use Web Workers with React?

Move heavy computations off the main thread so rendering stays smooth.

```jsx
// worker.js
self.onmessage = (e) => {
  const result = expensiveCalculation(e.data);
  self.postMessage(result);
};

// component
function Analysis({ data }) {
  const [result, setResult] = useState(null);

  useEffect(() => {
    const worker = new Worker(new URL("./worker.js", import.meta.url), {
      type: "module",
    });
    worker.onmessage = (e) => setResult(e.data);
    worker.postMessage(data);
    return () => worker.terminate();
  }, [data]);

  return result ? <Chart data={result} /> : <Spinner />;
}
```

Libraries like Comlink make the message passing feel like regular function calls. React itself still renders on the main thread.

### 427: How do you run high-frequency animations without re-rendering on every frame?

Don't put per-frame values in state. Update the DOM directly through a ref inside `requestAnimationFrame`, or use CSS animations.

```jsx
function FollowCursor() {
  const dotRef = useRef(null);

  useEffect(() => {
    let frame;
    let x = 0,
      y = 0;

    function onMove(e) {
      x = e.clientX;
      y = e.clientY;
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        dotRef.current.style.transform = `translate(${x}px, ${y}px)`;
      });
    }

    window.addEventListener("pointermove", onMove);
    return () => {
      window.removeEventListener("pointermove", onMove);
      cancelAnimationFrame(frame);
    };
  }, []);

  return <div ref={dotRef} className="dot" />;
}
```

Animation libraries like Motion use the same idea with "motion values" that change outside React's render cycle.

### 428: How do you integrate a library like D3 that wants to control the DOM?

Two approaches:

1. **Let React render, D3 calculates**: use D3 only for scales, layouts and path generators, and render SVG elements with JSX. This works well with React's model and SSR.

```jsx
function Bars({ data, width, height }) {
  const x = scaleBand()
    .domain(data.map((d) => d.label))
    .range([0, width])
    .padding(0.1);
  const y = scaleLinear()
    .domain([0, max(data, (d) => d.value)])
    .range([height, 0]);
  return (
    <svg width={width} height={height}>
      {data.map((d) => (
        <rect
          key={d.label}
          x={x(d.label)}
          y={y(d.value)}
          width={x.bandwidth()}
          height={height - y(d.value)}
        />
      ))}
    </svg>
  );
}
```

2. **Let D3 own a node**: give D3 a ref to an empty `<svg>` and run it in an effect (good for axes, zoom, brushes, transitions). React must not render children into that node.

### 429: How do you debug "Maximum update depth exceeded"?

It means a component keeps updating in a loop, usually from `useEffect` or `componentDidUpdate` setting state every time it runs.

```jsx
useEffect(() => {
  setItems(items.filter(Boolean)); // new array every time → effect runs again
}, [items]);
```

Steps:

1. Look at the component stack in the error.
2. Find effects that set state and check their dependencies.
3. Look for objects or functions created during render used as dependencies.
4. Check `getSnapshot` in `useSyncExternalStore` returning new objects.
5. Check ref callbacks that set state and are recreated every render.

Usually the fix is to derive the value during render instead of syncing it with an effect.

### 430: What does "Cannot update a component while rendering a different component" mean?

During one component's render, you set state in another component. This often happens when a child calls a parent's setter during render:

```jsx
function Child({ onLoaded }) {
  onLoaded(true); // sets parent state during Child's render
  return <div />;
}
```

Fixes: call it in an event handler or, if it's really a sync with something external, in an effect. Even better, restructure so the parent computes the value itself instead of the child reporting it.

### 431: What does "Rendered more hooks than during the previous render" mean?

The number of hooks called changed between renders. Usually a hook is called after an early return or inside a condition:

```jsx
function Profile({ user }) {
  if (!user) return null;
  const [tab, setTab] = useState("posts"); // skipped when user is null
}
```

Move all hooks above any early returns. The linter catches this with `rules-of-hooks`.

### 432: What does "Objects are not valid as a React child" mean?

You tried to render a plain object (or something like a `Date` or a `Map`) directly in JSX.

```jsx
<p>{user}</p>          // user is { name: "Ann" }
<p>{new Date()}</p>    // Date object
```

Render a property or a string instead: `{user.name}`, `{date.toLocaleDateString()}`. If you see it with an array, check that the array contains elements or strings, not objects. A common cause is rendering a whole API response while debugging; use `<pre>{JSON.stringify(data, null, 2)}</pre>` for that.

### 433: What happens when two list items have the same key?

React warns, and the behavior is undefined: it may drop one of the items, duplicate one, or mix up their state, because it can't tell them apart. It often shows up after adding items with a timestamp key created in the same millisecond, or when data from the server has duplicates. Make sure keys are unique, for example by combining fields (`${item.type}-${item.id}`) or generating IDs when the data is created.

### 434: What causes "Invalid hook call"?

Three common reasons:

1. **Hooks called outside a component**: in a regular function, a class component, or an event handler.
2. **Mismatched React and React DOM versions**.
3. **Two copies of React in the bundle**: hooks use a shared dispatcher, and if your component uses one copy of `react` while `react-dom` uses another, the dispatcher is empty.

Duplicate copies often happen with `npm link`, monorepos, or a library that lists `react` as a dependency instead of a peer dependency. Check with `npm ls react`, and fix it with peer dependencies, workspace hoisting, or a bundler alias that points to one copy.

### 435: How do you safely put initial data into server-rendered HTML?

If you embed JSON in a `<script>` tag, a value like `"</script><script>alert(1)</script>"` can break out of the tag. Escape `<` (and ideally `>`, `&`, U+2028, U+2029):

```js
function safeJson(data) {
  return JSON.stringify(data)
    .replace(/</g, "\\u003c")
    .replace(/>/g, "\\u003e")
    .replace(/&/g, "\\u0026")
    .replace(/
/g, "\\u2028")
    .replace(/
/g, "\\u2029");
}

<script
  dangerouslySetInnerHTML={{ __html: `window.__DATA__ = ${safeJson(data)}` }}
/>
```

Libraries like `serialize-javascript` or `devalue` do this for you. With RSC, the framework handles serialization of the payload safely.

### 436: Does `useEffect` always run after the browser paints?

Usually, but not always. For updates caused by discrete user input (click, keydown), React 18+ flushes the effects of that render synchronously before the browser paints. This makes sure the result of an effect (like a controlled input fix-up or an event-driven state change) is visible in the same frame.

For other updates (initial render, network responses, transitions), effects run after paint. Your code shouldn't depend on the exact timing. If you need to run something before paint every time, use `useLayoutEffect`.

### 437: In what order do effects and cleanups run between parents and children?

During mount, effects run from the bottom up: children's effects run before their parent's, because the child finishes first. Layout effects of the whole tree run before any regular effects.

During an update, React runs all the cleanups that need to run first (for effects with changed dependencies), then all the new setups. During unmount, cleanup runs for the parent and its children (the exact order shouldn't be relied on).

```jsx
function Parent() {
  useEffect(() => console.log("parent effect"));
  return <Child />;
}
function Child() {
  useEffect(() => console.log("child effect"));
  return null;
}
// mount logs: "child effect", then "parent effect"
```

This is why a parent's effect can safely assume the child's DOM and ref are ready.

### 438: What are headless components?

Headless components (or hooks) provide behavior, state and accessibility logic but no styling or markup decisions. You bring your own UI.

```jsx
function useDisclosure(initial = false) {
  const [open, setOpen] = useState(initial);
  const id = useId();
  return {
    open,
    toggle: () => setOpen((o) => !o),
    buttonProps: {
      "aria-expanded": open,
      "aria-controls": id,
      onClick: () => setOpen((o) => !o),
    },
    panelProps: { id, hidden: !open },
  };
}

function FAQItem({ q, a }) {
  const { buttonProps, panelProps } = useDisclosure();
  return (
    <div className="faq">
      <button {...buttonProps}>{q}</button>
      <div {...panelProps}>{a}</div>
    </div>
  );
}
```

Libraries like Radix Primitives, React Aria, Headless UI, TanStack Table and Downshift follow this idea. It separates hard-to-get-right logic (keyboard support, ARIA) from design.

### 439: How would you design the API of a reusable component library?

- **Follow HTML**: accept native props and pass the rest through (`...rest`), forward `ref` (a plain prop in React 19), support `className`.
- **Controlled and uncontrolled modes**: `value`/`defaultValue`/`onValueChange`.
- **Composition over configuration**: compound components or slots instead of dozens of boolean props.
- **Accessible by default**: correct roles, keyboard support and focus management built in.
- **Theming with CSS variables** so it works with Server Components and has no runtime cost.
- **Stable, typed API** with TypeScript, and clear deprecation paths.
- **Server Component friendly**: mark interactive parts with `"use client"` inside the library, keep static parts usable from the server.
- **Peer dependency on React**, never a direct dependency.

### 440: How do you handle internationalization with Server Components?

Load translations on the server and render text there, so translation files aren't sent to the browser for static content.

```jsx
// Server Component
export default async function Page({ params }) {
  const t = await getTranslations(params.locale);
  return <h1>{t("home.title")}</h1>;
}
```

Client Components that need translations get only the messages they use, through a provider created in a Server Component. Libraries like `next-intl` handle this split. Get the locale from the URL (like `/fr/...`) rather than from headers alone, so pages can be cached and shared.

### 441: How would you organize state in a large React application?

Split state by type and keep each kind in the right place:

- **Server data**: framework loaders, Server Components, or TanStack Query. Don't copy it into global client state.
- **URL state**: filters, pagination, selected tab, search query. Keep it in the URL so it's shareable and survives refresh.
- **Form state**: inside the form (uncontrolled + actions, or a form library).
- **Local UI state**: in the component that uses it (`useState`).
- **Shared client state**: small stores (Zustand, Jotai, or context with a reducer) for things like the current user's preferences or a shopping cart.

Then make sure each team or feature owns its state, with clear interfaces between features. Most "we need Redux" problems in large apps turn out to be server state in disguise.

### 442: What was the December 2025 React Server Components vulnerability, and what does it teach?

In December 2025 a critical vulnerability (CVE-2025-55182) was disclosed in the React Server Components packages (`react-server-dom-webpack`, `react-server-dom-parcel` and `react-server-dom-turbopack`). Because of how the server deserialized requests to Server Function endpoints, an attacker could get remote code execution without logging in. It affected React 19.0 to 19.2.0 and frameworks that bundle these packages, like Next.js. Patches were released in 19.0.1, 19.1.2 and 19.2.1, and some follow-up issues (denial of service and source code exposure) led to more patch releases after that.

Lessons:

- Apps using RSC expose an endpoint that accepts serialized data, even if you never wrote a Server Function yourself
- Keep React and your framework on the latest patch version and watch security advisories
- Treat all Server Function inputs as untrusted
- Use defense in depth: WAF rules, least-privilege server credentials, and monitoring

### 443: How would you approach a slow React app?

1. **Measure first**: React DevTools Profiler, Chrome Performance panel (with React tracks), Lighthouse, and real user data (Core Web Vitals, especially INP and LCP).
2. **Find the type of problem**:
   - Slow initial load → bundle size, code splitting, SSR/RSC, image optimization, fewer waterfalls
   - Slow interactions → too many re-renders, expensive renders, large lists, layout thrashing
3. **Fix the biggest cause**:
   - Colocate state, split contexts, use the compiler or `memo` for expensive subtrees
   - Virtualize long lists
   - Use transitions or `useDeferredValue` for heavy updates
   - Move heavy computation to workers or the server
4. **Measure again** and add a performance budget to CI so it doesn't regress.

### 444: How do you choose between CSR, SSR, SSG and Server Components?

- **CSR (client only)**: internal dashboards and apps behind login where SEO doesn't matter. Simple hosting.
- **SSG (static generation)**: content that changes rarely, like docs, marketing pages and blogs. Fastest, can be served from a CDN.
- **SSR**: pages with per-request or personalized data that need good SEO or fast first paint.
- **Server Components**: reduce client JavaScript by keeping non-interactive parts on the server, and fetch data close to where it's used. They work with both SSR and static generation.

Modern frameworks let you mix them per route. Partial pre-rendering blends static and dynamic in one page: static shell from the CDN, dynamic holes filled per request.

### 445: How would you migrate a large codebase from React 17 to React 19?

1. Upgrade dependencies (router, state libs, UI kits) to versions that support React 18/19. This is often the hardest part.
2. Move to React 18 first: switch to `createRoot`, fix Strict Mode double-effect issues, test automatic batching changes.
3. Upgrade to 18.3 and fix all deprecation warnings (string refs, `findDOMNode`, `defaultProps` on functions, legacy context).
4. Upgrade to 19 and run the codemods (`react/19/migration-recipe`, `types-react-codemod`).
5. Update tests: `act` from `react`, replace `react-test-renderer`.
6. Check error reporting setup (new root error options).
7. Then gradually adopt new features: actions, `use`, ref as prop, the compiler.

Do it behind CI with good test coverage, and ship each step separately.

### 446: How do you migrate a Create React App project to Vite?

1. Install `vite` and `@vitejs/plugin-react`, remove `react-scripts`.
2. Add `vite.config.js` with the React plugin.
3. Move `public/index.html` to the project root, remove `%PUBLIC_URL%`, and add `<script type="module" src="/src/index.jsx"></script>`.
4. Rename files with JSX to `.jsx`/`.tsx` (Vite doesn't parse JSX in `.js` by default).
5. Change env variables from `REACT_APP_` + `process.env` to `VITE_` + `import.meta.env`.
6. Update scripts: `"dev": "vite"`, `"build": "vite build"`, `"preview": "vite preview"`.
7. Replace Jest config with Vitest (or keep Jest with Babel), and fix SVG imports (`vite-plugin-svgr`).

It's also a good moment to consider a framework if you need routing, data loading or SSR.

### 447: Which React features are still experimental at the time of writing?

React ships stable features in `react@latest`, and new ideas first in the canary and experimental channels. Things that have been in canary or experimental include:

- `<ViewTransition>` for animations with the View Transitions API
- Fragment refs (refs on `<Fragment>` to work with a group of DOM nodes)
- The taint APIs for keeping server data out of the client
- Gesture-driven transitions

These may change or be removed. Before mentioning one as available in an interview, say that it's experimental, and check the React blog and docs, because features move to stable in minor releases (like `<Activity>` and `useEffectEvent` did in 19.2).

### 448: How do Suspense, transitions and error boundaries work together during a navigation?

Take a route change wrapped in `startTransition`:

1. The router sets the new URL state inside a transition.
2. React starts rendering the new page in the background. The old page stays on screen and `isPending` is `true`.
3. A component in the new page suspends (data or code not ready). Because it's a transition, React keeps waiting instead of showing a fallback for content that's already visible. New Suspense boundaries deeper in the new page may show their fallbacks.
4. When the data resolves, React finishes rendering and commits the new page.
5. If a component throws (or a promise rejects), the nearest error boundary renders its fallback in the new page.
6. If the user navigates again before step 4, React drops the in-progress render and starts the newer one.

The result: no blank screens, no half-loaded flashes, and a clear pending indicator.

### 449: Can you still use class components in React 19?

Yes. Class components are still supported and not deprecated. What changed in React 19 is the removal of legacy APIs that were mostly used with classes: string refs, legacy context (`contextTypes`), `propTypes` checks and `findDOMNode`. `defaultProps` still works for classes.

They can't use hooks, and new features like the compiler and actions are designed for function components. Error boundaries are the one place where you still need a class (or a library that wraps one).

### 450: Explain what happens from a `setState` call to pixels on the screen.

1. **Update is queued**: the setter creates an update object with a lane (priority) based on where it was called (click → sync, transition → transition lane) and adds it to the hook's queue. React marks the fiber and its parents as having pending work and asks the scheduler for a render.
2. **Batching**: other updates in the same tick join the same render.
3. **Render phase**: React walks the fiber tree from the root, skipping subtrees with no work. For each component that needs it, React calls the function, processes the hook update queue to get the new state, and compares the returned elements with the current children (reconciliation), marking fibers with effect flags. For non-urgent lanes, this work can be interrupted and resumed.
4. **Suspense check**: if something suspends, React shows a fallback or, in a transition, keeps the old UI and waits.
5. **Commit phase**: synchronous. React runs "before mutation" work, applies DOM changes (insertions, updates, deletions), detaches and attaches refs, swaps the current tree, and runs layout effects (`useLayoutEffect`, `componentDidMount`/`Update`).
6. **Browser paints** the new frame.
7. **Passive effects**: React runs `useEffect` cleanups and setups (before paint for discrete events, otherwise after).

If an effect sets state, the whole cycle starts again, which is why chains of effects are slow.
