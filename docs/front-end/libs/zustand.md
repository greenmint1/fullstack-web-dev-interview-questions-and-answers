# Zustand Interview Questions and Answers

_Last updated: October 28, 2026_

450 Zustand interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are written for Zustand v5 (5.0.x) with React 18 and later. Things that changed from v4, like `useShallow`, `zustand/traditional` and the new `persist` behavior, are pointed out where they matter, since you will still see v4 code in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Zustand?](#1-what-is-zustand)
- [2: Why would you pick Zustand over plain React state?](#2-why-would-you-pick-zustand-over-plain-react-state)
- [3: How do you install Zustand?](#3-how-do-you-install-zustand)
- [4: What is the current major version of Zustand and what does it need?](#4-what-is-the-current-major-version-of-zustand-and-what-does-it-need)
- [5: How do you create a basic store?](#5-how-do-you-create-a-basic-store)
- [6: How do you read state from a store in a component?](#6-how-do-you-read-state-from-a-store-in-a-component)
- [7: Do you need a Provider to use Zustand?](#7-do-you-need-a-provider-to-use-zustand)
- [8: What does the `set` function do?](#8-what-does-the-set-function-do)
- [9: Does `set` replace the whole state or merge it?](#9-does-set-replace-the-whole-state-or-merge-it)
- [10: Does the merge in `set` work for nested objects?](#10-does-the-merge-in-set-work-for-nested-objects)
- [11: What is the `get` function in a store?](#11-what-is-the-get-function-in-a-store)
- [12: What is a selector?](#12-what-is-a-selector)
- [13: What happens if you call the store hook without a selector?](#13-what-happens-if-you-call-the-store-hook-without-a-selector)
- [14: How does Zustand decide whether a component should re-render?](#14-how-does-zustand-decide-whether-a-component-should-re-render)
- [15: What is an action in Zustand?](#15-what-is-an-action-in-zustand)
- [16: Where do you usually put actions?](#16-where-do-you-usually-put-actions)
- [17: How do you update state in an immutable way?](#17-how-do-you-update-state-in-an-immutable-way)
- [18: What happens if you mutate state directly instead of calling `set`?](#18-what-happens-if-you-mutate-state-directly-instead-of-calling-set)
- [19: How do you read state outside of React components?](#19-how-do-you-read-state-outside-of-react-components)
- [20: How do you update state outside of React components?](#20-how-do-you-update-state-outside-of-react-components)
- [21: What methods are attached to the hook returned by `create`?](#21-what-methods-are-attached-to-the-hook-returned-by-create)
- [22: What does `subscribe` do?](#22-what-does-subscribe-do)
- [23: What does `getInitialState` return?](#23-what-does-getinitialstate-return)
- [24: How do you reset a store to its initial state?](#24-how-do-you-reset-a-store-to-its-initial-state)
- [25: How do you write an async action?](#25-how-do-you-write-an-async-action)
- [26: Does Zustand need middleware like redux-thunk for async code?](#26-does-zustand-need-middleware-like-redux-thunk-for-async-code)
- [27: How do you handle loading and error states in an async action?](#27-how-do-you-handle-loading-and-error-states-in-an-async-action)
- [28: Can you have more than one store in an app?](#28-can-you-have-more-than-one-store-in-an-app)
- [29: What is the naming convention for Zustand stores?](#29-what-is-the-naming-convention-for-zustand-stores)
- [30: Can you use Zustand without React?](#30-can-you-use-zustand-without-react)
- [31: What is the difference between `create` and `createStore`?](#31-what-is-the-difference-between-create-and-createstore)
- [32: How do you use a vanilla store inside React?](#32-how-do-you-use-a-vanilla-store-inside-react)
- [33: What are the main entry points in the zustand package?](#33-what-are-the-main-entry-points-in-the-zustand-package)
- [34: Does Zustand have a default export?](#34-does-zustand-have-a-default-export)
- [35: How big is Zustand?](#35-how-big-is-zustand)
- [36: What is the store creator function?](#36-what-is-the-store-creator-function)
- [37: How do you select an action from the store?](#37-how-do-you-select-an-action-from-the-store)
- [38: Why is it fine to select functions from the store?](#38-why-is-it-fine-to-select-functions-from-the-store)
- [39: How do you select several values from a store?](#39-how-do-you-select-several-values-from-a-store)
- [40: What is `useShallow`?](#40-what-is-useshallow)
- [41: What does "shallow equal" mean?](#41-what-does-shallow-equal-mean)
- [42: What is the `shallow` function?](#42-what-is-the-shallow-function)
- [43: How do you use Zustand with TypeScript?](#43-how-do-you-use-zustand-with-typescript)
- [44: Why do you write `create<T>()(...)` with two sets of parentheses in TypeScript?](#44-why-do-you-write-createt-with-two-sets-of-parentheses-in-typescript)
- [45: What is middleware in Zustand?](#45-what-is-middleware-in-zustand)
- [46: What middleware comes with Zustand?](#46-what-middleware-comes-with-zustand)
- [47: How do you save store state to localStorage?](#47-how-do-you-save-store-state-to-localstorage)
- [48: What is the `name` option in `persist`?](#48-what-is-the-name-option-in-persist)
- [49: How do you use sessionStorage instead of localStorage?](#49-how-do-you-use-sessionstorage-instead-of-localstorage)
- [50: How do you see Zustand state in the Redux DevTools?](#50-how-do-you-see-zustand-state-in-the-redux-devtools)
- [51: What is the immer middleware used for?](#51-what-is-the-immer-middleware-used-for)
- [52: How is Zustand different from Redux?](#52-how-is-zustand-different-from-redux)
- [53: How is Zustand different from React Context?](#53-how-is-zustand-different-from-react-context)
- [54: How is Zustand different from Jotai?](#54-how-is-zustand-different-from-jotai)
- [55: How is Zustand different from Valtio?](#55-how-is-zustand-different-from-valtio)
- [56: Should you put server data in Zustand or use TanStack Query?](#56-should-you-put-server-data-in-zustand-or-use-tanstack-query)
- [57: What kind of state is a good fit for Zustand?](#57-what-kind-of-state-is-a-good-fit-for-zustand)
- [58: When would you not use Zustand?](#58-when-would-you-not-use-zustand)
- [59: How do you compute derived values from the store?](#59-how-do-you-compute-derived-values-from-the-store)
- [60: Should you store derived data in the store?](#60-should-you-store-derived-data-in-the-store)
- [61: How do you toggle a boolean in a store?](#61-how-do-you-toggle-a-boolean-in-a-store)
- [62: When should you use the function form of `set`?](#62-when-should-you-use-the-function-form-of-set)
- [63: How do you add an item to an array in the store?](#63-how-do-you-add-an-item-to-an-array-in-the-store)
- [64: How do you remove an item from an array in the store?](#64-how-do-you-remove-an-item-from-an-array-in-the-store)
- [65: How do you update one item in an array in the store?](#65-how-do-you-update-one-item-in-an-array-in-the-store)
- [66: How do you pass arguments to an action?](#66-how-do-you-pass-arguments-to-an-action)
- [67: Can one action call another action?](#67-can-one-action-call-another-action)
- [68: Can you use a store inside a custom hook?](#68-can-you-use-a-store-inside-a-custom-hook)
- [69: Does Zustand follow the rules of hooks?](#69-does-zustand-follow-the-rules-of-hooks)
- [70: How do you use a store value in an event handler without subscribing to it?](#70-how-do-you-use-a-store-value-in-an-event-handler-without-subscribing-to-it)
- [71: How does Zustand work with React 18 and later?](#71-how-does-zustand-work-with-react-18-and-later)
- [72: What is tearing?](#72-what-is-tearing)
- [73: What is the `combine` middleware?](#73-what-is-the-combine-middleware)
- [74: What is the `subscribeWithSelector` middleware?](#74-what-is-the-subscribewithselector-middleware)
- [75: What is the `redux` middleware?](#75-what-is-the-redux-middleware)
- [76: What is the slices pattern?](#76-what-is-the-slices-pattern)
- [77: Should you use one big store or many small stores?](#77-should-you-use-one-big-store-or-many-small-stores)
- [78: Can a component use several stores?](#78-can-a-component-use-several-stores)
- [79: How do you clear persisted data?](#79-how-do-you-clear-persisted-data)
- [80: How do you persist only some fields of the state?](#80-how-do-you-persist-only-some-fields-of-the-state)
- [81: What is hydration in the context of `persist`?](#81-what-is-hydration-in-the-context-of-persist)
- [82: How do you check if a persisted store has finished hydrating?](#82-how-do-you-check-if-a-persisted-store-has-finished-hydrating)
- [83: How do you use Zustand persist with React Native?](#83-how-do-you-use-zustand-persist-with-react-native)
- [84: Does Zustand work with React Native?](#84-does-zustand-work-with-react-native)
- [85: Can you use Zustand in a Next.js app?](#85-can-you-use-zustand-in-a-nextjs-app)
- [86: Does Zustand work with React Server Components?](#86-does-zustand-work-with-react-server-components)
- [87: What does the devtools middleware need to work?](#87-what-does-the-devtools-middleware-need-to-work)
- [88: How do you turn off devtools in production?](#88-how-do-you-turn-off-devtools-in-production)
- [89: How do you name actions in Redux DevTools?](#89-how-do-you-name-actions-in-redux-devtools)
- [90: How do you write a simple counter with Zustand?](#90-how-do-you-write-a-simple-counter-with-zustand)
- [91: How do you write a simple todo store?](#91-how-do-you-write-a-simple-todo-store)
- [92: How do you store a simple auth state?](#92-how-do-you-store-a-simple-auth-state)
- [93: How do you store a theme setting?](#93-how-do-you-store-a-theme-setting)
- [94: How do you use a store value in a `useEffect`?](#94-how-do-you-use-a-store-value-in-a-useeffect)
- [95: Is it a problem to call `set` in a render function?](#95-is-it-a-problem-to-call-set-in-a-render-function)
- [96: What happens if `set` is called with the same value?](#96-what-happens-if-set-is-called-with-the-same-value)
- [97: Can you store functions other than actions in the store?](#97-can-you-store-functions-other-than-actions-in-the-store)
- [98: Can you store class instances in the store?](#98-can-you-store-class-instances-in-the-store)
- [99: Can you store a Map or a Set in the store?](#99-can-you-store-a-map-or-a-set-in-the-store)
- [100: Where should you put store files in a project?](#100-where-should-you-put-store-files-in-a-project)
- [101: How do you export selectors from a store file?](#101-how-do-you-export-selectors-from-a-store-file)
- [102: Why is a selector defined outside the component a good idea?](#102-why-is-a-selector-defined-outside-the-component-a-good-idea)
- [103: What does the `version` option in `persist` do?](#103-what-does-the-version-option-in-persist-do)
- [104: What does `migrate` do in `persist`?](#104-what-does-migrate-do-in-persist)
- [105: How do you check what's in the store while debugging without DevTools?](#105-how-do-you-check-whats-in-the-store-while-debugging-without-devtools)
- [106: Does Zustand batch updates?](#106-does-zustand-batch-updates)
- [107: Can several components share one store without passing props?](#107-can-several-components-share-one-store-without-passing-props)
- [108: What is "state" and what are "actions" in a Zustand store?](#108-what-is-state-and-what-are-actions-in-a-zustand-store)
- [109: What is `StateCreator` in TypeScript?](#109-what-is-statecreator-in-typescript)
- [110: What is `StoreApi` in TypeScript?](#110-what-is-storeapi-in-typescript)
- [111: What is `ExtractState`?](#111-what-is-extractstate)
- [112: How do you type a selector in TypeScript?](#112-how-do-you-type-a-selector-in-typescript)
- [113: Does Zustand store state immutably?](#113-does-zustand-store-state-immutably)
- [114: What happens to the store when a component unmounts?](#114-what-happens-to-the-store-when-a-component-unmounts)
- [115: Does the store keep state across page reloads?](#115-does-the-store-keep-state-across-page-reloads)
- [116: How do you share a store between tabs?](#116-how-do-you-share-a-store-between-tabs)
- [117: How do you set state from inside a `setTimeout` or `setInterval`?](#117-how-do-you-set-state-from-inside-a-settimeout-or-setinterval)
- [118: What is a common beginner mistake with selectors?](#118-what-is-a-common-beginner-mistake-with-selectors)
- [119: What is another common beginner mistake with Zustand?](#119-what-is-another-common-beginner-mistake-with-zustand)
- [120: Can you use Zustand with class components?](#120-can-you-use-zustand-with-class-components)
- [121: Can you call the store hook conditionally?](#121-can-you-call-the-store-hook-conditionally)
- [122: How do you handle a form with Zustand?](#122-how-do-you-handle-a-form-with-zustand)
- [123: How do you store a multi-step wizard state?](#123-how-do-you-store-a-multi-step-wizard-state)
- [124: How do you open and close a modal with Zustand?](#124-how-do-you-open-and-close-a-modal-with-zustand)
- [125: How do you show toast notifications with a store?](#125-how-do-you-show-toast-notifications-with-a-store)
- [126: Where can you find the official Zustand documentation?](#126-where-can-you-find-the-official-zustand-documentation)
- [127: Is Zustand only for small apps?](#127-is-zustand-only-for-small-apps)
- [128: Does Zustand have any opinion about how to structure code?](#128-does-zustand-have-any-opinion-about-how-to-structure-code)
- [129: What are the "flux inspired" practices the docs mention?](#129-what-are-the-flux-inspired-practices-the-docs-mention)
- [130: How do you put actions outside the store?](#130-how-do-you-put-actions-outside-the-store)
- [131: What is the benefit of actions outside the store?](#131-what-is-the-benefit-of-actions-outside-the-store)
- [132: How do you write a selector that uses component props?](#132-how-do-you-write-a-selector-that-uses-component-props)
- [133: Can selectors return `undefined`?](#133-can-selectors-return-undefined)
- [134: Can you use the same store in two separate React roots?](#134-can-you-use-the-same-store-in-two-separate-react-roots)
- [135: How do you write the store creator without using `set`?](#135-how-do-you-write-the-store-creator-without-using-set)
- [136: Can you subscribe to a store inside a component?](#136-can-you-subscribe-to-a-store-inside-a-component)
- [137: What does the third argument of the store creator give you?](#137-what-does-the-third-argument-of-the-store-creator-give-you)
- [138: Can you use JavaScript instead of TypeScript with Zustand?](#138-can-you-use-javascript-instead-of-typescript-with-zustand)
- [139: How do you test a component that uses a Zustand store?](#139-how-do-you-test-a-component-that-uses-a-zustand-store)
- [140: Why do you need to reset stores between tests?](#140-why-do-you-need-to-reset-stores-between-tests)
- [141: How do you test a store without React?](#141-how-do-you-test-a-store-without-react)
- [142: How do you share types between the store and components?](#142-how-do-you-share-types-between-the-store-and-components)
- [143: How do you install the immer middleware?](#143-how-do-you-install-the-immer-middleware)
- [144: Why is immer middleware imported from a separate path?](#144-why-is-immer-middleware-imported-from-a-separate-path)
- [145: What is the difference between `set` and `setState`?](#145-what-is-the-difference-between-set-and-setstate)
- [146: Can you rename `set` and `get` in the store creator?](#146-can-you-rename-set-and-get-in-the-store-creator)
- [147: How do you add a new field to a store later?](#147-how-do-you-add-a-new-field-to-a-store-later)
- [148: How do you show a value from the store and update it from an input?](#148-how-do-you-show-a-value-from-the-store-and-update-it-from-an-input)
- [149: What does Zustand give you that `useReducer` + context doesn't?](#149-what-does-zustand-give-you-that-usereducer--context-doesnt)
- [150: How would you explain Zustand to someone new in one or two sentences?](#150-how-would-you-explain-zustand-to-someone-new-in-one-or-two-sentences)

### Moderate Questions (151-300)

- [151: In what order should you apply several middlewares?](#151-in-what-order-should-you-apply-several-middlewares)
- [152: Why do the Zustand docs say to use `devtools` as the last middleware?](#152-why-do-the-zustand-docs-say-to-use-devtools-as-the-last-middleware)
- [153: How do you type a store that uses several middlewares in TypeScript?](#153-how-do-you-type-a-store-that-uses-several-middlewares-in-typescript)
- [154: How do you type slices in TypeScript?](#154-how-do-you-type-slices-in-typescript)
- [155: What do the second and third type parameters of `StateCreator` mean?](#155-what-do-the-second-and-third-type-parameters-of-statecreator-mean)
- [156: Where should middleware go when you use the slices pattern?](#156-where-should-middleware-go-when-you-use-the-slices-pattern)
- [157: How do you reset all slices of a store?](#157-how-do-you-reset-all-slices-of-a-store)
- [158: How do you reset several separate stores at once, for example on logout?](#158-how-do-you-reset-several-separate-stores-at-once-for-example-on-logout)
- [159: How do you create a store per component instance with context?](#159-how-do-you-create-a-store-per-component-instance-with-context)
- [160: When do you need a store in context instead of a global store?](#160-when-do-you-need-a-store-in-context-instead-of-a-global-store)
- [161: Why should you create the context store in `useState(() => ...)` or `useRef` and not in the render body?](#161-why-should-you-create-the-context-store-in-usestate---or-useref-and-not-in-the-render-body)
- [162: Why does the context hold the store and not the state?](#162-why-does-the-context-hold-the-store-and-not-the-state)
- [163: How do you initialize a store with props?](#163-how-do-you-initialize-a-store-with-props)
- [164: What happened to `zustand/context`?](#164-what-happened-to-zustandcontext)
- [165: How do you auto-generate selectors for every field in a store?](#165-how-do-you-auto-generate-selectors-for-every-field-in-a-store)
- [166: What is `createWithEqualityFn` and when do you use it?](#166-what-is-createwithequalityfn-and-when-do-you-use-it)
- [167: What is `useStoreWithEqualityFn`?](#167-what-is-usestorewithequalityfn)
- [168: What is the difference between `useShallow` and passing `shallow` to `createWithEqualityFn`?](#168-what-is-the-difference-between-useshallow-and-passing-shallow-to-createwithequalityfn)
- [169: Why did v5 remove the equality function from `create`?](#169-why-did-v5-remove-the-equality-function-from-create)
- [170: Why can a selector that returns a new array cause an infinite loop in v5?](#170-why-can-a-selector-that-returns-a-new-array-cause-an-infinite-loop-in-v5)
- [171: How do you fix a selector that returns a filtered list?](#171-how-do-you-fix-a-selector-that-returns-a-filtered-list)
- [172: Why should a fallback value in a selector be a constant?](#172-why-should-a-fallback-value-in-a-selector-be-a-constant)
- [173: How do you select several actions at once?](#173-how-do-you-select-several-actions-at-once)
- [174: What is the downside of the nested `actions` object pattern?](#174-what-is-the-downside-of-the-nested-actions-object-pattern)
- [175: How do you debug unnecessary re-renders in a Zustand app?](#175-how-do-you-debug-unnecessary-re-renders-in-a-zustand-app)
- [176: How do you log every state change in development?](#176-how-do-you-log-every-state-change-in-development)
- [177: How do you write a simple custom middleware?](#177-how-do-you-write-a-simple-custom-middleware)
- [178: How do you make a custom middleware also catch `setState` calls from outside the store?](#178-how-do-you-make-a-custom-middleware-also-catch-setstate-calls-from-outside-the-store)
- [179: How does `persist` work with a custom storage?](#179-how-does-persist-work-with-a-custom-storage)
- [180: How do you persist a Map, Set or Date?](#180-how-do-you-persist-a-map-set-or-date)
- [181: What does the `merge` option in `persist` do?](#181-what-does-the-merge-option-in-persist-do)
- [182: What does `onRehydrateStorage` do?](#182-what-does-onrehydratestorage-do)
- [183: What does `skipHydration` do?](#183-what-does-skiphydration-do)
- [184: Why does a persisted store cause a hydration mismatch in Next.js?](#184-why-does-a-persisted-store-cause-a-hydration-mismatch-in-nextjs)
- [185: How do you write a hook that waits for a persisted store to hydrate?](#185-how-do-you-write-a-hook-that-waits-for-a-persisted-store-to-hydrate)
- [186: What do `persist.onHydrate` and `persist.onFinishHydration` do?](#186-what-do-persistonhydrate-and-persistonfinishhydration-do)
- [187: How do you change `persist` options at runtime?](#187-how-do-you-change-persist-options-at-runtime)
- [188: Can `migrate` be async?](#188-can-migrate-be-async)
- [189: Does `persist` write to storage when the store is created?](#189-does-persist-write-to-storage-when-the-store-is-created)
- [190: How do you persist state in the URL instead of localStorage?](#190-how-do-you-persist-state-in-the-url-instead-of-localstorage)
- [191: Should you use Zustand or the URL for filter and search state?](#191-should-you-use-zustand-or-the-url-for-filter-and-search-state)
- [192: What does the devtools `store` option do?](#192-what-does-the-devtools-store-option-do)
- [193: What is `anonymousActionType` in devtools?](#193-what-is-anonymousactiontype-in-devtools)
- [194: What does `store.devtools.cleanup()` do?](#194-what-does-storedevtoolscleanup-do)
- [195: Can you time-travel with Zustand devtools?](#195-can-you-time-travel-with-zustand-devtools)
- [196: How do you use immer with devtools?](#196-how-do-you-use-immer-with-devtools)
- [197: In the immer middleware, can you still return a new object from `set`?](#197-in-the-immer-middleware-can-you-still-return-a-new-object-from-set)
- [198: What are the downsides of the immer middleware?](#198-what-are-the-downsides-of-the-immer-middleware)
- [199: How do you subscribe to a specific field outside React?](#199-how-do-you-subscribe-to-a-specific-field-outside-react)
- [200: What options does `subscribeWithSelector` accept?](#200-what-options-does-subscribewithselector-accept)
- [201: How do you handle race conditions in async actions?](#201-how-do-you-handle-race-conditions-in-async-actions)
- [202: How do you do an optimistic update with Zustand?](#202-how-do-you-do-an-optimistic-update-with-zustand)
- [203: How do you debounce an action in a store?](#203-how-do-you-debounce-an-action-in-a-store)
- [204: Should timers, sockets or AbortControllers be stored in state?](#204-should-timers-sockets-or-abortcontrollers-be-stored-in-state)
- [205: How do you keep a websocket connection in sync with a store?](#205-how-do-you-keep-a-websocket-connection-in-sync-with-a-store)
- [206: How do you use the auth token from a store in a fetch helper?](#206-how-do-you-use-the-auth-token-from-a-store-in-a-fetch-helper)
- [207: How do you use Zustand together with TanStack Query?](#207-how-do-you-use-zustand-together-with-tanstack-query)
- [208: How do you use a store in React Router loaders or actions?](#208-how-do-you-use-a-store-in-react-router-loaders-or-actions)
- [209: How do you set up Zustand in the Next.js App Router?](#209-how-do-you-set-up-zustand-in-the-nextjs-app-router)
- [210: Why shouldn't you use a module-level store for per-user data in Next.js?](#210-why-shouldnt-you-use-a-module-level-store-for-per-user-data-in-nextjs)
- [211: Where should the Provider go in the Next.js App Router?](#211-where-should-the-provider-go-in-the-nextjs-app-router)
- [212: How do you pass server data into a Zustand store in Next.js?](#212-how-do-you-pass-server-data-into-a-zustand-store-in-nextjs)
- [213: How do you mock Zustand in Jest so every store resets after each test?](#213-how-do-you-mock-zustand-in-jest-so-every-store-resets-after-each-test)
- [214: How do you do the same reset setup in Vitest?](#214-how-do-you-do-the-same-reset-setup-in-vitest)
- [215: Why are store updates wrapped in `act` in tests?](#215-why-are-store-updates-wrapped-in-act-in-tests)
- [216: How do you test an async action that calls fetch?](#216-how-do-you-test-an-async-action-that-calls-fetch)
- [217: How do you test a component with a store that lives in context?](#217-how-do-you-test-a-component-with-a-store-that-lives-in-context)
- [218: How do you test a persisted store?](#218-how-do-you-test-a-persisted-store)
- [219: Should you mock the store itself in component tests?](#219-should-you-mock-the-store-itself-in-component-tests)
- [220: How do you use Zustand stores in Storybook?](#220-how-do-you-use-zustand-stores-in-storybook)
- [221: How do you migrate from React Context + useReducer to Zustand?](#221-how-do-you-migrate-from-react-context--usereducer-to-zustand)
- [222: How do you migrate from Redux to Zustand step by step?](#222-how-do-you-migrate-from-redux-to-zustand-step-by-step)
- [223: What changed between Zustand v4 and v5 that you need to know when upgrading?](#223-what-changed-between-zustand-v4-and-v5-that-you-need-to-know-when-upgrading)
- [224: What is the recommended way to upgrade an old v3 or v4 project to v5?](#224-what-is-the-recommended-way-to-upgrade-an-old-v3-or-v4-project-to-v5)
- [225: How do you handle a dynamic `replace` flag in TypeScript after v5?](#225-how-do-you-handle-a-dynamic-replace-flag-in-typescript-after-v5)
- [226: What is `UseBoundStore`?](#226-what-is-useboundstore)
- [227: How do you type a hook that uses a vanilla store with an optional selector?](#227-how-do-you-type-a-hook-that-uses-a-vanilla-store-with-an-optional-selector)
- [228: How do you type `get` and `set` when actions call each other?](#228-how-do-you-type-get-and-set-when-actions-call-each-other)
- [229: When is `combine` a good choice for TypeScript users?](#229-when-is-combine-a-good-choice-for-typescript-users)
- [230: How do you type a persisted store when using `partialize`?](#230-how-do-you-type-a-persisted-store-when-using-partialize)
- [231: How do you avoid persisting secrets like tokens in localStorage?](#231-how-do-you-avoid-persisting-secrets-like-tokens-in-localstorage)
- [232: How do you normalize a list of entities in a store?](#232-how-do-you-normalize-a-list-of-entities-in-a-store)
- [233: Why is it good for list rows to select their own item by id?](#233-why-is-it-good-for-list-rows-to-select-their-own-item-by-id)
- [234: How do you store pagination state?](#234-how-do-you-store-pagination-state)
- [235: How do two stores talk to each other?](#235-how-do-two-stores-talk-to-each-other)
- [236: How do you react in one store when another store changes?](#236-how-do-you-react-in-one-store-when-another-store-changes)
- [237: How do you memoize an expensive derived value?](#237-how-do-you-memoize-an-expensive-derived-value)
- [238: What is a "transient update" in Zustand?](#238-what-is-a-transient-update-in-zustand)
- [239: How do you implement undo and redo?](#239-how-do-you-implement-undo-and-redo)
- [240: How do you split stores for code splitting?](#240-how-do-you-split-stores-for-code-splitting)
- [241: Can you add a slice to a store after it was created?](#241-can-you-add-a-slice-to-a-store-after-it-was-created)
- [242: How do you handle errors thrown in actions?](#242-how-do-you-handle-errors-thrown-in-actions)
- [243: How do you show a global error banner from any action?](#243-how-do-you-show-a-global-error-banner-from-any-action)
- [244: How do you sync a store with `localStorage` changes from other tabs?](#244-how-do-you-sync-a-store-with-localstorage-changes-from-other-tabs)
- [245: How do you prevent a component from re-rendering when only an unrelated field in an object changes?](#245-how-do-you-prevent-a-component-from-re-rendering-when-only-an-unrelated-field-in-an-object-changes)
- [246: What does `useShallow` compare when the selector returns an array of values?](#246-what-does-useshallow-compare-when-the-selector-returns-an-array-of-values)
- [247: When can `useShallow` still cause re-renders?](#247-when-can-useshallow-still-cause-re-renders)
- [248: Can you pass the same selector function to many components?](#248-can-you-pass-the-same-selector-function-to-many-components)
- [249: What is a good file structure for a medium-sized app with Zustand?](#249-what-is-a-good-file-structure-for-a-medium-sized-app-with-zustand)
- [250: Why is it a good idea to export custom hooks instead of the raw store?](#250-why-is-it-a-good-idea-to-export-custom-hooks-instead-of-the-raw-store)
- [251: How do you persist only part of a store when using the slices pattern?](#251-how-do-you-persist-only-part-of-a-store-when-using-the-slices-pattern)
- [252: How do you exclude a few keys from persistence instead of listing the ones to keep?](#252-how-do-you-exclude-a-few-keys-from-persistence-instead-of-listing-the-ones-to-keep)
- [253: What happens if `localStorage` is not available, for example in private mode or on the server?](#253-what-happens-if-localstorage-is-not-available-for-example-in-private-mode-or-on-the-server)
- [254: How do you persist with cookies so the server can read the state?](#254-how-do-you-persist-with-cookies-so-the-server-can-read-the-state)
- [255: How do you wait for hydration before rendering an app that uses async storage?](#255-how-do-you-wait-for-hydration-before-rendering-an-app-that-uses-async-storage)
- [256: How do you store a `_hasHydrated` flag inside the store itself?](#256-how-do-you-store-a-_hashydrated-flag-inside-the-store-itself)
- [257: How do you persist two different stores with different storages?](#257-how-do-you-persist-two-different-stores-with-different-storages)
- [258: How can a selector read from two stores?](#258-how-can-a-selector-read-from-two-stores)
- [259: How do you use Zustand with forms built with React Hook Form?](#259-how-do-you-use-zustand-with-forms-built-with-react-hook-form)
- [260: How do you keep a store in sync with a prop that changes?](#260-how-do-you-keep-a-store-in-sync-with-a-prop-that-changes)
- [261: How do you reset a context store when a route changes?](#261-how-do-you-reset-a-context-store-when-a-route-changes)
- [262: Can you use Zustand with Preact or other frameworks?](#262-can-you-use-zustand-with-preact-or-other-frameworks)
- [263: How do you use a vanilla store in a non-React part of the app, like a chart library?](#263-how-do-you-use-a-vanilla-store-in-a-non-react-part-of-the-app-like-a-chart-library)
- [264: How do you handle a store field that holds a big list from the server?](#264-how-do-you-handle-a-store-field-that-holds-a-big-list-from-the-server)
- [265: How do you avoid stale state in an async action?](#265-how-do-you-avoid-stale-state-in-an-async-action)
- [266: When would you use `set` with `replace: true`?](#266-when-would-you-use-set-with-replace-true)
- [267: What goes wrong with `set({}, true)`?](#267-what-goes-wrong-with-set-true)
- [268: How do you make actions available to tests without rendering?](#268-how-do-you-make-actions-available-to-tests-without-rendering)
- [269: How do you test a selector?](#269-how-do-you-test-a-selector)
- [270: How do you test `subscribe` logic?](#270-how-do-you-test-subscribe-logic)
- [271: How do you write an action that updates several fields at once?](#271-how-do-you-write-an-action-that-updates-several-fields-at-once)
- [272: Is it bad to call `set` many times in a row in one action?](#272-is-it-bad-to-call-set-many-times-in-a-row-in-one-action)
- [273: How do you add a computed getter to the store?](#273-how-do-you-add-a-computed-getter-to-the-store)
- [274: Why don't JavaScript getters work well in Zustand state?](#274-why-dont-javascript-getters-work-well-in-zustand-state)
- [275: How do you share common logic between several stores?](#275-how-do-you-share-common-logic-between-several-stores)
- [276: How do you combine Zustand with Immer without the middleware?](#276-how-do-you-combine-zustand-with-immer-without-the-middleware)
- [277: What is the difference between `zustand/react` and `zustand`?](#277-what-is-the-difference-between-zustandreact-and-zustand)
- [278: How do you read the state at the time of a click and also show it?](#278-how-do-you-read-the-state-at-the-time-of-a-click-and-also-show-it)
- [279: How do you build a shopping cart store with quantities?](#279-how-do-you-build-a-shopping-cart-store-with-quantities)
- [280: How do you handle feature flags with Zustand?](#280-how-do-you-handle-feature-flags-with-zustand)
- [281: How do you handle permissions in the UI with a store?](#281-how-do-you-handle-permissions-in-the-ui-with-a-store)
- [282: How do you use Zustand for a dark mode that respects the system setting?](#282-how-do-you-use-zustand-for-a-dark-mode-that-respects-the-system-setting)
- [283: How do you test that a component doesn't re-render too often?](#283-how-do-you-test-that-a-component-doesnt-re-render-too-often)
- [284: Why might a component re-render even though its selected value didn't change?](#284-why-might-a-component-re-render-even-though-its-selected-value-didnt-change)
- [285: How do you write a store for a multi-step async flow, like upload then process?](#285-how-do-you-write-a-store-for-a-multi-step-async-flow-like-upload-then-process)
- [286: How do you handle very frequent updates like a progress bar or drag position?](#286-how-do-you-handle-very-frequent-updates-like-a-progress-bar-or-drag-position)
- [287: How do you persist a store and also version it from the start?](#287-how-do-you-persist-a-store-and-also-version-it-from-the-start)
- [288: How do you write a migration that handles several old versions?](#288-how-do-you-write-a-migration-that-handles-several-old-versions)
- [289: What is a good way to name actions for devtools in a large store?](#289-what-is-a-good-way-to-name-actions-for-devtools-in-a-large-store)
- [290: How do you keep Zustand and the URL in sync both ways?](#290-how-do-you-keep-zustand-and-the-url-in-sync-both-ways)
- [291: Is it okay to call a store action in `useEffect` on mount to load data?](#291-is-it-okay-to-call-a-store-action-in-useeffect-on-mount-to-load-data)
- [292: How do you prevent duplicate fetches when several components call the same load action?](#292-how-do-you-prevent-duplicate-fetches-when-several-components-call-the-same-load-action)
- [293: How do you split one large store into slices without breaking components?](#293-how-do-you-split-one-large-store-into-slices-without-breaking-components)
- [294: How do you use Zustand with Suspense?](#294-how-do-you-use-zustand-with-suspense)
- [295: How do you store a selection of items, like checked rows in a table?](#295-how-do-you-store-a-selection-of-items-like-checked-rows-in-a-table)
- [296: How do you add a "dirty" flag to know if a form has unsaved changes?](#296-how-do-you-add-a-dirty-flag-to-know-if-a-form-has-unsaved-changes)
- [297: How do you warn the user before leaving with unsaved changes?](#297-how-do-you-warn-the-user-before-leaving-with-unsaved-changes)
- [298: What are some useful third-party libraries around Zustand?](#298-what-are-some-useful-third-party-libraries-around-zustand)
- [299: How do you make a store that is created lazily on first use?](#299-how-do-you-make-a-store-that-is-created-lazily-on-first-use)
- [300: What are the most common Zustand mistakes you have seen in code reviews?](#300-what-are-the-most-common-zustand-mistakes-you-have-seen-in-code-reviews)

### Advanced Questions (301-450)

- [301: How does `createStore` work internally?](#301-how-does-createstore-work-internally)
- [302: When does `setState` skip notifying listeners?](#302-when-does-setstate-skip-notifying-listeners)
- [303: What happens if you call `setState` with a primitive or `null`?](#303-what-happens-if-you-call-setstate-with-a-primitive-or-null)
- [304: Are listeners called synchronously?](#304-are-listeners-called-synchronously)
- [305: What happens if a listener calls `setState` again?](#305-what-happens-if-a-listener-calls-setstate-again)
- [306: What happens if a listener unsubscribes another listener while the store is notifying?](#306-what-happens-if-a-listener-unsubscribes-another-listener-while-the-store-is-notifying)
- [307: How does `useStore` connect to React?](#307-how-does-usestore-connect-to-react)
- [308: Why does Zustand use `getInitialState` for the server snapshot?](#308-why-does-zustand-use-getinitialstate-for-the-server-snapshot)
- [309: Why is the selector wrapped in `useCallback` inside `useStore`?](#309-why-is-the-selector-wrapped-in-usecallback-inside-usestore)
- [310: Why does an unstable selector result cause "Maximum update depth exceeded" with `useSyncExternalStore`?](#310-why-does-an-unstable-selector-result-cause-maximum-update-depth-exceeded-with-usesyncexternalstore)
- [311: How does `useShallow` work internally?](#311-how-does-useshallow-work-internally)
- [312: How does `zustand/traditional` support equality functions?](#312-how-does-zustandtraditional-support-equality-functions)
- [313: How does the `shallow` function compare Maps, Sets, arrays and plain objects?](#313-how-does-the-shallow-function-compare-maps-sets-arrays-and-plain-objects)
- [314: Does `shallow` treat two Sets with the same items in different order as equal?](#314-does-shallow-treat-two-sets-with-the-same-items-in-different-order-as-equal)
- [315: What does `useDebugValue` do in `useStore`?](#315-what-does-usedebugvalue-do-in-usestore)
- [316: What is the cost of having many components subscribed to one store?](#316-what-is-the-cost-of-having-many-components-subscribed-to-one-store)
- [317: How would you scale a store that updates many times per second with thousands of subscribers?](#317-how-would-you-scale-a-store-that-updates-many-times-per-second-with-thousands-of-subscribers)
- [318: How would you batch many incoming updates into one `set`?](#318-how-would-you-batch-many-incoming-updates-into-one-set)
- [319: How do React transitions work with Zustand updates?](#319-how-do-react-transitions-work-with-zustand-updates)
- [320: How can `useDeferredValue` help with a slow component that reads from Zustand?](#320-how-can-usedeferredvalue-help-with-a-slow-component-that-reads-from-zustand)
- [321: Does Zustand work with the React Compiler?](#321-does-zustand-work-with-the-react-compiler)
- [322: What is the `StoreMutators` interface used for?](#322-what-is-the-storemutators-interface-used-for)
- [323: How do you write a typed custom middleware that adds a method to the store?](#323-how-do-you-write-a-typed-custom-middleware-that-adds-a-method-to-the-store)
- [324: Why do built-in middleware implementations use a cast to a more complex type?](#324-why-do-built-in-middleware-implementations-use-a-cast-to-a-more-complex-type)
- [325: How does `Mutate<S, Ms>` work?](#325-how-does-mutates-ms-work)
- [326: Why do you need `create<T>()(...)` but not `create(...)` in plain JavaScript?](#326-why-do-you-need-createt-but-not-create-in-plain-javascript)
- [327: What does `create()` with no arguments return at runtime?](#327-what-does-create-with-no-arguments-return-at-runtime)
- [328: How does the `persist` middleware hook into `setState`?](#328-how-does-the-persist-middleware-hook-into-setstate)
- [329: When does `persist` hydrate, and is it sync or async?](#329-when-does-persist-hydrate-and-is-it-sync-or-async)
- [330: What does `persist` do if `rehydrate` is called twice quickly?](#330-what-does-persist-do-if-rehydrate-is-called-twice-quickly)
- [331: How does `persist` change `getInitialState`?](#331-how-does-persist-change-getinitialstate)
- [332: In what order do `migrate` and `merge` run during hydration?](#332-in-what-order-do-migrate-and-merge-run-during-hydration)
- [333: What happens if hydration fails because the stored JSON is broken?](#333-what-happens-if-hydration-fails-because-the-stored-json-is-broken)
- [334: Can `merge` be used to protect against tampered persisted data?](#334-can-merge-be-used-to-protect-against-tampered-persisted-data)
- [335: Why can't you trust persisted state for security decisions?](#335-why-cant-you-trust-persisted-state-for-security-decisions)
- [336: What are the security risks of persisting state in `localStorage`?](#336-what-are-the-security-risks-of-persisting-state-in-localstorage)
- [337: Can a malicious persisted value cause prototype pollution through the default merge?](#337-can-a-malicious-persisted-value-cause-prototype-pollution-through-the-default-merge)
- [338: How does the devtools middleware record actions?](#338-how-does-the-devtools-middleware-record-actions)
- [339: Why can the devtools action name sometimes show the wrong function or "anonymous"?](#339-why-can-the-devtools-action-name-sometimes-show-the-wrong-function-or-anonymous)
- [340: What is the cost of the devtools middleware in production?](#340-what-is-the-cost-of-the-devtools-middleware-in-production)
- [341: How does the immer middleware work internally?](#341-how-does-the-immer-middleware-work-internally)
- [342: Why does Immer make structural sharing important for Zustand selectors?](#342-why-does-immer-make-structural-sharing-important-for-zustand-selectors)
- [343: How does `subscribeWithSelector` work internally?](#343-how-does-subscribewithselector-work-internally)
- [344: What does `combine` do at runtime?](#344-what-does-combine-do-at-runtime)
- [345: What is `unstable_ssrSafe` in `zustand/middleware`?](#345-what-is-unstable_ssrsafe-in-zustandmiddleware)
- [346: Why is a global store dangerous on a Node.js server?](#346-why-is-a-global-store-dangerous-on-a-nodejs-server)
- [347: Is reading a global store on the server safe?](#347-is-reading-a-global-store-on-the-server-safe)
- [348: How do you make sure the same store instance is used on server render and hydration in a context-based setup?](#348-how-do-you-make-sure-the-same-store-instance-is-used-on-server-render-and-hydration-in-a-context-based-setup)
- [349: Why might you get a hydration error even with a per-request store?](#349-why-might-you-get-a-hydration-error-even-with-a-per-request-store)
- [350: How do you avoid duplicate Zustand copies in a monorepo or micro-frontend setup?](#350-how-do-you-avoid-duplicate-zustand-copies-in-a-monorepo-or-micro-frontend-setup)
- [351: Can a Zustand store be used inside a Web Worker?](#351-can-a-zustand-store-be-used-inside-a-web-worker)
- [352: How would you sync a store across tabs without `localStorage` events?](#352-how-would-you-sync-a-store-across-tabs-without-localstorage-events)
- [353: How do you keep store state consistent when an async action is canceled halfway?](#353-how-do-you-keep-store-state-consistent-when-an-async-action-is-canceled-halfway)
- [354: Why can a component see a different value from `getState()` than from its hook during render?](#354-why-can-a-component-see-a-different-value-from-getstate-than-from-its-hook-during-render)
- [355: What are the trade-offs between a single global store and many small stores?](#355-what-are-the-trade-offs-between-a-single-global-store-and-many-small-stores)
- [356: How would you design state management for a large app with several teams?](#356-how-would-you-design-state-management-for-a-large-app-with-several-teams)
- [357: How do you prevent other modules from writing to a store directly?](#357-how-do-you-prevent-other-modules-from-writing-to-a-store-directly)
- [358: When would you choose Redux Toolkit over Zustand for a new project?](#358-when-would-you-choose-redux-toolkit-over-zustand-for-a-new-project)
- [359: When would you choose Jotai over Zustand?](#359-when-would-you-choose-jotai-over-zustand)
- [360: When would you choose XState (or another state machine library) over Zustand?](#360-when-would-you-choose-xstate-or-another-state-machine-library-over-zustand)
- [361: How would you model a finite state machine in a Zustand store without a library?](#361-how-would-you-model-a-finite-state-machine-in-a-zustand-store-without-a-library)
- [362: What happens if two components call the same async action at the same time?](#362-what-happens-if-two-components-call-the-same-async-action-at-the-same-time)
- [363: How do you design a store API so components can't create invalid state?](#363-how-do-you-design-a-store-api-so-components-cant-create-invalid-state)
- [364: Why do you need `replace: true` with discriminated union state?](#364-why-do-you-need-replace-true-with-discriminated-union-state)
- [365: How would you structure a store that holds both a union state and actions?](#365-how-would-you-structure-a-store-that-holds-both-a-union-state-and-actions)
- [366: A component re-renders on every keystroke in an unrelated input. How do you find the cause?](#366-a-component-re-renders-on-every-keystroke-in-an-unrelated-input-how-do-you-find-the-cause)
- [367: After upgrading to v5, the app crashes with "Maximum update depth exceeded". How do you fix it?](#367-after-upgrading-to-v5-the-app-crashes-with-maximum-update-depth-exceeded-how-do-you-fix-it)
- [368: Users report that their saved settings disappear after a deploy. What could be wrong?](#368-users-report-that-their-saved-settings-disappear-after-a-deploy-what-could-be-wrong)
- [369: The persisted store shows old values for a moment after a page load in React Native. Why?](#369-the-persisted-store-shows-old-values-for-a-moment-after-a-page-load-in-react-native-why)
- [370: A test passes alone but fails when run with others. What is a likely Zustand cause?](#370-a-test-passes-alone-but-fails-when-run-with-others-what-is-a-likely-zustand-cause)
- [371: You see private data from another user in a server-rendered page. How would you investigate?](#371-you-see-private-data-from-another-user-in-a-server-rendered-page-how-would-you-investigate)
- [372: How do you design a store for a collaborative editor with remote updates?](#372-how-do-you-design-a-store-for-a-collaborative-editor-with-remote-updates)
- [373: How would you implement middleware that validates every state update in development?](#373-how-would-you-implement-middleware-that-validates-every-state-update-in-development)
- [374: How would you implement a simple time-travel debugger for one store?](#374-how-would-you-implement-a-simple-time-travel-debugger-for-one-store)
- [375: Why is immutability what makes cheap snapshots possible?](#375-why-is-immutability-what-makes-cheap-snapshots-possible)
- [376: How would you implement a "lazy" store that loads its initial data on first subscription?](#376-how-would-you-implement-a-lazy-store-that-loads-its-initial-data-on-first-subscription)
- [377: What can go wrong if you replace `api.subscribe` in a middleware?](#377-what-can-go-wrong-if-you-replace-apisubscribe-in-a-middleware)
- [378: How does React handle the `subscribe` function changing between renders?](#378-how-does-react-handle-the-subscribe-function-changing-between-renders)
- [379: What happens to subscriptions when a Provider replaces its store?](#379-what-happens-to-subscriptions-when-a-provider-replaces-its-store)
- [380: How can a Zustand store cause a memory leak?](#380-how-can-a-zustand-store-cause-a-memory-leak)
- [381: How would you implement an LRU-style cache inside a store?](#381-how-would-you-implement-an-lru-style-cache-inside-a-store)
- [382: What are the pros and cons of putting actions inside vs outside the store?](#382-what-are-the-pros-and-cons-of-putting-actions-inside-vs-outside-the-store)
- [383: How would you share a store between a React app and a vanilla JavaScript widget on the same page?](#383-how-would-you-share-a-store-between-a-react-app-and-a-vanilla-javascript-widget-on-the-same-page)
- [384: How would you design a plugin system where plugins add state to a store?](#384-how-would-you-design-a-plugin-system-where-plugins-add-state-to-a-store)
- [385: Why is it hard to code-split slices of a single store?](#385-why-is-it-hard-to-code-split-slices-of-a-single-store)
- [386: How would you handle errors from `persist` when storage quota is exceeded?](#386-how-would-you-handle-errors-from-persist-when-storage-quota-is-exceeded)
- [387: How do you limit how often `persist` writes to storage?](#387-how-do-you-limit-how-often-persist-writes-to-storage)
- [388: Why can `persist` be slow for large states?](#388-why-can-persist-be-slow-for-large-states)
- [389: How does `useShallow` behave if the selector function changes on every render?](#389-how-does-useshallow-behave-if-the-selector-function-changes-on-every-render)
- [390: Why should you not call `useShallow` conditionally or inside a callback?](#390-why-should-you-not-call-useshallow-conditionally-or-inside-a-callback)
- [391: How does Zustand compare to `useSyncExternalStore` written by hand?](#391-how-does-zustand-compare-to-usesyncexternalstore-written-by-hand)
- [392: How would you write a minimal Zustand-like store from scratch?](#392-how-would-you-write-a-minimal-zustand-like-store-from-scratch)
- [393: In what situations would `getState()` inside a render be a bug?](#393-in-what-situations-would-getstate-inside-a-render-be-a-bug)
- [394: How do you handle a store that must be reset when the logged-in user changes, without a page reload?](#394-how-do-you-handle-a-store-that-must-be-reset-when-the-logged-in-user-changes-without-a-page-reload)
- [395: How do you implement optimistic updates that are safe with concurrent edits?](#395-how-do-you-implement-optimistic-updates-that-are-safe-with-concurrent-edits)
- [396: What are the downsides of storing derived data in the store to avoid recomputing?](#396-what-are-the-downsides-of-storing-derived-data-in-the-store-to-avoid-recomputing)
- [397: How would you keep a derived value in the store updated automatically?](#397-how-would-you-keep-a-derived-value-in-the-store-updated-automatically)
- [398: How do you prevent the second update from the previous pattern from looping?](#398-how-do-you-prevent-the-second-update-from-the-previous-pattern-from-looping)
- [399: How would you design a store for an infinite scroll list?](#399-how-would-you-design-a-store-for-an-infinite-scroll-list)
- [400: How would you test an action that uses a debounce timer?](#400-how-would-you-test-an-action-that-uses-a-debounce-timer)
- [401: Why did Zustand choose to work without a Provider by default?](#401-why-did-zustand-choose-to-work-without-a-provider-by-default)
- [402: Why does Zustand use explicit selectors instead of tracking which properties you read?](#402-why-does-zustand-use-explicit-selectors-instead-of-tracking-which-properties-you-read)
- [403: How do signals (like in Preact Signals or Solid) differ from Zustand's model?](#403-how-do-signals-like-in-preact-signals-or-solid-differ-from-zustands-model)
- [404: How does Hot Module Replacement affect a Zustand store?](#404-how-does-hot-module-replacement-affect-a-zustand-store)
- [405: How does React Strict Mode affect Zustand?](#405-how-does-react-strict-mode-affect-zustand)
- [406: How do you write a selector factory for parameterized selectors?](#406-how-do-you-write-a-selector-factory-for-parameterized-selectors)
- [407: How do you write a memoized selector per component instance?](#407-how-do-you-write-a-memoized-selector-per-component-instance)
- [408: What is the risk of using a deep equality function with `createWithEqualityFn`?](#408-what-is-the-risk-of-using-a-deep-equality-function-with-createwithequalityfn)
- [409: How would you implement an offline action queue with Zustand?](#409-how-would-you-implement-an-offline-action-queue-with-zustand)
- [410: How would you handle refreshing an auth token only once when many requests fail at the same time?](#410-how-would-you-handle-refreshing-an-auth-token-only-once-when-many-requests-fail-at-the-same-time)
- [411: How would you send analytics events for certain state changes without touching each action?](#411-how-would-you-send-analytics-events-for-certain-state-changes-without-touching-each-action)
- [412: How would you build a middleware that records named actions for analytics?](#412-how-would-you-build-a-middleware-that-records-named-actions-for-analytics)
- [413: What happens with errors thrown inside a `subscribe` listener?](#413-what-happens-with-errors-thrown-inside-a-subscribe-listener)
- [414: Do React error boundaries catch errors in Zustand actions?](#414-do-react-error-boundaries-catch-errors-in-zustand-actions)
- [415: Can a selector throw, and what happens if it does?](#415-can-a-selector-throw-and-what-happens-if-it-does)
- [416: What are the problems with storing `Error` objects in state?](#416-what-are-the-problems-with-storing-error-objects-in-state)
- [417: How do you store a `BigInt` in a persisted store?](#417-how-do-you-store-a-bigint-in-a-persisted-store)
- [418: How do you handle Dates correctly with `persist`?](#418-how-do-you-handle-dates-correctly-with-persist)
- [419: How would you migrate a store from a module-level hook to a context-based store without changing components?](#419-how-would-you-migrate-a-store-from-a-module-level-hook-to-a-context-based-store-without-changing-components)
- [420: What is the "dual package hazard" and can it affect Zustand?](#420-what-is-the-dual-package-hazard-and-can-it-affect-zustand)
- [421: How tree-shakable is Zustand?](#421-how-tree-shakable-is-zustand)
- [422: How would you design a store for a drag-and-drop board (like Trello)?](#422-how-would-you-design-a-store-for-a-drag-and-drop-board-like-trello)
- [423: Why separate "hot" UI state from "domain" state into different stores?](#423-why-separate-hot-ui-state-from-domain-state-into-different-stores)
- [424: How do you decide what belongs in Zustand, in the URL, in a server cache and in local component state?](#424-how-do-you-decide-what-belongs-in-zustand-in-the-url-in-a-server-cache-and-in-local-component-state)
- [425: What are the risks of calling `getState()` inside a selector?](#425-what-are-the-risks-of-calling-getstate-inside-a-selector)
- [426: How can you make an action easy to undo with a command pattern?](#426-how-can-you-make-an-action-easy-to-undo-with-a-command-pattern)
- [427: How do you write type-safe access to another slice from inside a slice?](#427-how-do-you-write-type-safe-access-to-another-slice-from-inside-a-slice)
- [428: How do you avoid circular imports between slice files?](#428-how-do-you-avoid-circular-imports-between-slice-files)
- [429: What happens if two slices define the same key?](#429-what-happens-if-two-slices-define-the-same-key)
- [430: Why might someone nest slice data under a key (like `cart: { ... }`) and what is the trade-off?](#430-why-might-someone-nest-slice-data-under-a-key-like-cart----and-what-is-the-trade-off)
- [431: How do you handle a selector that needs data from props and from two different stores efficiently?](#431-how-do-you-handle-a-selector-that-needs-data-from-props-and-from-two-different-stores-efficiently)
- [432: How would you implement a global loading indicator that shows when any request is running?](#432-how-would-you-implement-a-global-loading-indicator-that-shows-when-any-request-is-running)
- [433: How do you make a store work in both the browser and tests without touching `window`?](#433-how-do-you-make-a-store-work-in-both-the-browser-and-tests-without-touching-window)
- [434: How would you use dependency injection to make a store easier to test?](#434-how-would-you-use-dependency-injection-to-make-a-store-easier-to-test)
- [435: What are the limits of `useShallow` for nested data, and how do you work around them?](#435-what-are-the-limits-of-useshallow-for-nested-data-and-how-do-you-work-around-them)
- [436: How would you profile the cost of selectors?](#436-how-would-you-profile-the-cost-of-selectors)
- [437: How would you migrate a large app from Zustand v4's `create(selector, shallow)` usage to v5 safely?](#437-how-would-you-migrate-a-large-app-from-zustand-v4s-createselector-shallow-usage-to-v5-safely)
- [438: How do you keep store logic framework-independent so it can be reused in a React Native and a web app?](#438-how-do-you-keep-store-logic-framework-independent-so-it-can-be-reused-in-a-react-native-and-a-web-app)
- [439: What is the effect of putting a very large object (like 10 MB of JSON) into a store?](#439-what-is-the-effect-of-putting-a-very-large-object-like-10-mb-of-json-into-a-store)
- [440: How would you freeze state in development to catch accidental mutations?](#440-how-would-you-freeze-state-in-development-to-catch-accidental-mutations)
- [441: Why does the immer middleware make accidental mutation bugs less likely?](#441-why-does-the-immer-middleware-make-accidental-mutation-bugs-less-likely)
- [442: How would you handle a store that needs initialization from an async source before the app starts?](#442-how-would-you-handle-a-store-that-needs-initialization-from-an-async-source-before-the-app-starts)
- [443: When should a component subscribe with the hook vs use `subscribe` in an effect?](#443-when-should-a-component-subscribe-with-the-hook-vs-use-subscribe-in-an-effect)
- [444: How do you avoid stale closures when subscribing inside an effect?](#444-how-do-you-avoid-stale-closures-when-subscribing-inside-an-effect)
- [445: What would you check in a code review of a new Zustand store?](#445-what-would-you-check-in-a-code-review-of-a-new-zustand-store)
- [446: An app's main page feels slow, and the profiler shows a list component re-rendering on every store update. Walk through how you'd fix it.](#446-an-apps-main-page-feels-slow-and-the-profiler-shows-a-list-component-re-rendering-on-every-store-update-walk-through-how-youd-fix-it)
- [447: How would you explain the difference between "the store changed" and "the component re-rendered" in Zustand?](#447-how-would-you-explain-the-difference-between-the-store-changed-and-the-component-re-rendered-in-zustand)
- [448: How would you build a "recent searches" feature with Zustand?](#448-how-would-you-build-a-recent-searches-feature-with-zustand)
- [449: What would you say are the main strengths and weaknesses of Zustand?](#449-what-would-you-say-are-the-main-strengths-and-weaknesses-of-zustand)
- [450: Walk through what happens, step by step, when a user clicks a button that calls a Zustand action.](#450-walk-through-what-happens-step-by-step-when-a-user-clicks-a-button-that-calls-a-zustand-action)

---

## Easy Questions (1-150)

### 1: What is Zustand?

Zustand is a small state management library for React. You create a store with a function called `create`, and it gives you back a hook that components use to read state and call actions. There are no providers, reducers or action types by default, so the amount of code you write is small.

The name means "state" in German. It is maintained by the Poimandres (pmndrs) group, the same people behind Jotai and React Three Fiber.

### 2: Why would you pick Zustand over plain React state?

`useState` and `useReducer` keep state inside one component. When many components in different parts of the tree need the same data, you end up passing props down several levels or putting it in context. Zustand gives you a shared store that any component can read from directly, and components only re-render when the part of the state they select changes.

### 3: How do you install Zustand?

```bash
npm install zustand
```

That is enough for the normal `create` API. If you want to use `zustand/traditional` (`createWithEqualityFn`), you also need `use-sync-external-store`, and for the immer middleware you need `immer`.

### 4: What is the current major version of Zustand and what does it need?

The current major version is v5 (5.0.x). It needs React 18 or newer and TypeScript 4.5 or newer if you use TypeScript. It uses React's built-in `useSyncExternalStore`, so the core has no runtime dependencies.

### 5: How do you create a basic store?

You call `create` with a function that returns the initial state and the actions.

```js
import { create } from "zustand";

const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}));
```

The result, `useCounterStore`, is a React hook.

### 6: How do you read state from a store in a component?

Call the hook with a selector function that picks the value you need.

```jsx
function Counter() {
  const count = useCounterStore((state) => state.count);
  const increment = useCounterStore((state) => state.increment);

  return <button onClick={increment}>Count: {count}</button>;
}
```

### 7: Do you need a Provider to use Zustand?

No. A store made with `create` lives in a module, outside of React, so any component that imports the hook can use it. You only add a React context when you want a separate store per component tree, for example per request in server rendering or per instance of a widget.

### 8: What does the `set` function do?

`set` updates the store state and notifies subscribers. You can pass it an object with the fields you want to change, or a function that receives the current state and returns those fields.

```js
set({ loading: true });
set((state) => ({ count: state.count + 1 }));
```

### 9: Does `set` replace the whole state or merge it?

By default it does a shallow merge. Only the top-level keys you return are changed, and the other keys stay as they were. If you want to replace the whole state, pass `true` as the second argument: `set(newState, true)`.

### 10: Does the merge in `set` work for nested objects?

No, the merge is only one level deep. If you update a nested object you must copy it yourself.

```js
set((state) => ({
  user: { ...state.user, name: "Ana" },
}));
```

If you only return `{ user: { name: 'Ana' } }`, every other field inside `user` is lost.

### 11: What is the `get` function in a store?

`get` is the second argument of the store creator. It returns the current state, so you can read state inside actions without a functional `set`.

```js
const useCartStore = create((set, get) => ({
  items: [],
  total: () => get().items.reduce((sum, item) => sum + item.price, 0),
  clear: () => set({ items: [] }),
}));
```

### 12: What is a selector?

A selector is a function that takes the full state and returns the part a component needs, such as `(state) => state.count`. Zustand runs it on every state change and re-renders the component only when the returned value is different from the previous one.

### 13: What happens if you call the store hook without a selector?

`useStore()` with no selector returns the whole state object. The component then re-renders on every state change, even for fields it doesn't use. It works, but it is not recommended for anything except very small stores.

### 14: How does Zustand decide whether a component should re-render?

It compares the old and new result of your selector with `Object.is`. If they are equal, the component does not re-render. That is why selecting a primitive like a number or string is cheap, and why returning a new object or array from a selector needs extra care.

### 15: What is an action in Zustand?

An action is just a function stored in the state that calls `set`. There is no special syntax or action type. You call it like any function: `useCounterStore.getState().increment()` or by selecting it in a component.

### 16: Where do you usually put actions?

Most people put them in the same object as the state, inside the `create` call. Another option is to define them as plain functions outside the store that call `useStore.setState`. Both are supported; the docs show the second as "practice with no store actions".

### 17: How do you update state in an immutable way?

You never change the current state object directly. Instead, you return new values from `set`. For arrays, use methods that return a new array such as `map`, `filter` or the spread operator.

```js
addTodo: (text) =>
  set((state) => ({ todos: [...state.todos, { id: Date.now(), text, done: false }] })),
```

### 18: What happens if you mutate state directly instead of calling `set`?

Zustand won't know the state changed, so no listener is called and no component re-renders. Even if you later call `set` with the same object, `Object.is` sees the same reference and may skip the update. Always create new objects for changed data.

### 19: How do you read state outside of React components?

The hook returned by `create` also has the store methods attached to it, so you can call `getState()` anywhere.

```js
const count = useCounterStore.getState().count;
useCounterStore.getState().increment();
```

This is useful in event handlers, utility functions or API code.

### 20: How do you update state outside of React components?

Use `setState` on the hook.

```js
useCounterStore.setState({ count: 10 });
useCounterStore.setState((state) => ({ count: state.count + 1 }));
```

It works the same way as `set` inside the store.

### 21: What methods are attached to the hook returned by `create`?

The hook has `getState`, `setState`, `getInitialState` and `subscribe`. Middleware can add more, for example `persist` adds a `persist` object and `devtools` adds `devtools.cleanup`.

### 22: What does `subscribe` do?

`subscribe` registers a listener that runs after every state change. The listener gets the new state and the previous state. It returns a function that removes the listener.

```js
const unsubscribe = useCounterStore.subscribe((state, prevState) => {
  console.log("count changed from", prevState.count, "to", state.count);
});

unsubscribe();
```

### 23: What does `getInitialState` return?

It returns the state that the store creator returned when the store was created. It is handy for reset functions and tests, because you don't have to keep a separate copy of the initial values.

### 24: How do you reset a store to its initial state?

Replace the current state with the initial state.

```js
useCounterStore.setState(useCounterStore.getInitialState(), true);
```

You can also add a `reset` action inside the store that does the same thing.

### 25: How do you write an async action?

Write a normal async function and call `set` when you have the data. Zustand doesn't care whether an action is sync or async.

```js
const useUserStore = create((set) => ({
  user: null,
  loading: false,
  fetchUser: async (id) => {
    set({ loading: true });
    const res = await fetch(`/api/users/${id}`);
    const user = await res.json();
    set({ user, loading: false });
  },
}));
```

### 26: Does Zustand need middleware like redux-thunk for async code?

No. Actions are plain functions, so they can be async and call `set` as many times as they want. No extra middleware is needed.

### 27: How do you handle loading and error states in an async action?

Keep them as fields in the store and set them at the right moments.

```js
fetchPosts: async () => {
  set({ status: 'loading', error: null })
  try {
    const res = await fetch('/api/posts')
    if (!res.ok) throw new Error('Request failed')
    set({ posts: await res.json(), status: 'success' })
  } catch (err) {
    set({ status: 'error', error: err.message })
  }
},
```

### 28: Can you have more than one store in an app?

Yes. You can create as many stores as you like, usually one per feature or domain (for example `useAuthStore`, `useCartStore`). Another common approach is one store built from several "slices". Both are fine.

### 29: What is the naming convention for Zustand stores?

Since `create` returns a hook, the name usually starts with `use`, for example `useBearStore` or `useCartStore`. This keeps the rules of hooks lint rule working and makes it clear that it is a hook.

### 30: Can you use Zustand without React?

Yes. `createStore` from `zustand/vanilla` creates a store with no React dependency. It has the same `getState`, `setState`, `subscribe` and `getInitialState` methods. You can use it in plain JavaScript, in other frameworks, or connect it to React later with `useStore`.

```js
import { createStore } from "zustand/vanilla";

const counterStore = createStore((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
}));
```

### 31: What is the difference between `create` and `createStore`?

`createStore` (from `zustand/vanilla`, also exported from `zustand`) returns a plain store object. `create` (from `zustand`) creates the same kind of store, then wraps it in a React hook and copies the store methods onto that hook. Use `create` in React apps and `createStore` when you need a store without React or a store you create per component tree.

### 32: How do you use a vanilla store inside React?

Use the `useStore` hook and pass it the store and a selector.

```jsx
import { useStore } from "zustand";

function Counter() {
  const count = useStore(counterStore, (state) => state.count);
  return <span>{count}</span>;
}
```

### 33: What are the main entry points in the zustand package?

- `zustand` - `create`, `createStore`, `useStore` and the types.
- `zustand/vanilla` - `createStore` with no React.
- `zustand/react` - `create` and `useStore`.
- `zustand/shallow` - `shallow` and `useShallow`.
- `zustand/middleware` - `persist`, `devtools`, `subscribeWithSelector`, `combine`, `redux`, `createJSONStorage`.
- `zustand/middleware/immer` - the `immer` middleware.
- `zustand/traditional` - `createWithEqualityFn` and `useStoreWithEqualityFn`.

### 34: Does Zustand have a default export?

Not anymore. v5 removed default exports, so you must use named imports: `import { create } from 'zustand'`. Older code that does `import create from 'zustand'` is v3 style and won't work on v5.

### 35: How big is Zustand?

The core is very small, around 1 KB minified and gzipped. Most of the code is in middleware, which you only pay for if you import it.

### 36: What is the store creator function?

It is the function you pass to `create` or `createStore`. It receives `set`, `get` and the store API, and it returns the initial state including actions.

```js
const useStore = create((set, get, store) => ({
  value: 0,
}));
```

The third argument is rarely needed, but middleware uses it.

### 37: How do you select an action from the store?

The same way as any value: `const increment = useCounterStore((s) => s.increment)`. Actions are defined once when the store is created, so their reference doesn't change and selecting them never causes extra re-renders.

### 38: Why is it fine to select functions from the store?

Because actions are created one time inside the store creator and keep the same reference for the life of the store. The selector returns the same function every time, `Object.is` says it is equal, and the component doesn't re-render.

### 39: How do you select several values from a store?

The simplest way is one hook call per value.

```jsx
const count = useCounterStore((s) => s.count);
const step = useCounterStore((s) => s.step);
```

If you want one call that returns an object or array, wrap the selector with `useShallow`, otherwise you'll get extra re-renders or an infinite loop warning.

### 40: What is `useShallow`?

`useShallow` is a hook from `zustand/shallow` that wraps a selector. It remembers the last result and returns the old reference when the new result is shallowly equal. This makes selectors that return objects or arrays safe to use.

```jsx
import { useShallow } from "zustand/shallow";

const { count, step } = useCounterStore(
  useShallow((s) => ({ count: s.count, step: s.step })),
);
```

### 41: What does "shallow equal" mean?

Two values are shallowly equal if they have the same keys (or the same items for arrays) and each value is equal with `Object.is`. It doesn't go deeper into nested objects. So `{ a: 1 }` and `{ a: 1 }` are shallowly equal, but `{ a: { b: 1 } }` and `{ a: { b: 1 } }` are not, because the inner objects are different references.

### 42: What is the `shallow` function?

`shallow` is a plain function that compares two values shallowly and returns `true` or `false`. It works with objects, arrays, Maps and Sets. It is used inside `useShallow`, and you can also pass it as an equality function to `createWithEqualityFn` or `subscribeWithSelector`.

```js
import { shallow } from "zustand/shallow";

shallow({ a: 1 }, { a: 1 }); // true
shallow([1, 2], [1, 2]); // true
```

### 43: How do you use Zustand with TypeScript?

Define a type for the state and pass it to `create`. Note the extra `()` after `create<State>()`. It is needed for TypeScript to infer types correctly, especially with middleware.

```ts
import { create } from "zustand";

interface CounterState {
  count: number;
  increment: () => void;
}

const useCounterStore = create<CounterState>()((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
}));
```

### 44: Why do you write `create<T>()(...)` with two sets of parentheses in TypeScript?

It is a curried call. The first call takes only the state type, and the second takes the store creator. TypeScript can't partially infer generic parameters, so this split lets you give the state type while middleware types are still inferred. Without the extra `()`, middleware like `persist` and `devtools` won't type correctly.

### 45: What is middleware in Zustand?

Middleware is a function that wraps the store creator to add behavior. For example, `persist` saves state to storage and `devtools` connects to the Redux DevTools. You apply it by wrapping the store creator.

```js
import { create } from "zustand";
import { persist } from "zustand/middleware";

const useStore = create(
  persist((set) => ({ theme: "light" }), { name: "settings" }),
);
```

### 46: What middleware comes with Zustand?

- `persist` - saves and loads state from storage.
- `devtools` - connects to Redux DevTools.
- `immer` - lets you write updates that look like mutations.
- `subscribeWithSelector` - lets you subscribe to a selected part of the state.
- `combine` - merges initial state with actions and infers types.
- `redux` - lets you use a reducer and `dispatch`.

### 47: How do you save store state to localStorage?

Wrap the store with the `persist` middleware and give it a unique `name`. By default it uses `localStorage`.

```js
import { create } from "zustand";
import { persist } from "zustand/middleware";

const useSettingsStore = create(
  persist(
    (set) => ({
      theme: "light",
      setTheme: (theme) => set({ theme }),
    }),
    { name: "settings-storage" },
  ),
);
```

### 48: What is the `name` option in `persist`?

It is the key used in storage, so in the example above the data is saved under `localStorage['settings-storage']`. It must be unique for each persisted store, otherwise two stores would overwrite each other's data.

### 49: How do you use sessionStorage instead of localStorage?

Pass a different storage with `createJSONStorage`.

```js
import { persist, createJSONStorage } from "zustand/middleware";

persist(storeCreator, {
  name: "form-draft",
  storage: createJSONStorage(() => sessionStorage),
});
```

### 50: How do you see Zustand state in the Redux DevTools?

Wrap the store with the `devtools` middleware and install the Redux DevTools browser extension.

```js
import { create } from "zustand";
import { devtools } from "zustand/middleware";

const useCounterStore = create(
  devtools(
    (set) => ({
      count: 0,
      increment: () =>
        set((s) => ({ count: s.count + 1 }), undefined, "counter/increment"),
    }),
    { name: "CounterStore" },
  ),
);
```

The third argument to `set` is the action name shown in DevTools.

### 51: What is the immer middleware used for?

It lets you write state updates as if you were changing the state directly. Immer turns those changes into a new immutable state for you. This is handy when you update deeply nested data.

```js
import { create } from "zustand";
import { immer } from "zustand/middleware/immer";

const useTodoStore = create(
  immer((set) => ({
    todos: [],
    toggle: (id) =>
      set((state) => {
        const todo = state.todos.find((t) => t.id === id);
        if (todo) todo.done = !todo.done;
      }),
  })),
);
```

You need to install `immer` yourself.

### 52: How is Zustand different from Redux?

Both keep state in a store outside of React. Redux uses a single store, actions with types, reducers and usually a Provider. Zustand has no required structure: you write state and functions in one object, there is no Provider, and you can have many stores. Redux (with Redux Toolkit) gives you more structure, built-in conventions and RTK Query. Zustand is smaller and has less boilerplate.

### 53: How is Zustand different from React Context?

Context is a way to pass a value down the tree, not a state manager. When the context value changes, every component that reads the context re-renders, even if it only uses one field. Zustand lets each component subscribe to just the part it needs, so only those components re-render. Zustand also works outside React components.

### 54: How is Zustand different from Jotai?

Both come from the same team. Zustand is store-based (top-down): you build one object with state and actions. Jotai is atom-based (bottom-up): you create small atoms and combine them. Zustand stores live outside React, while Jotai atoms usually live in React (with an optional Provider). Pick Zustand when you think in terms of a store, and Jotai when you have many small independent pieces of state.

### 55: How is Zustand different from Valtio?

Valtio uses proxies so you mutate state directly (`state.count++`) and it tracks what each component reads. Zustand uses immutable updates with `set` and explicit selectors. Valtio feels like plain objects; Zustand is more explicit and predictable.

### 56: Should you put server data in Zustand or use TanStack Query?

For data that comes from an API, TanStack Query (or RTK Query, SWR) is usually the better tool, because it handles caching, refetching, deduping and stale data. Zustand is a better fit for client state: UI state, user preferences, form drafts, selections, and so on. Many apps use both together.

### 57: What kind of state is a good fit for Zustand?

State that many components share and that lives on the client: auth info, theme, sidebar open or closed, items in a cart, filters, wizard steps, a selected item, or the state of an editor or game. State used by only one component can stay in `useState`.

### 58: When would you not use Zustand?

When the state belongs to one component, `useState` is simpler. When the data comes from a server and needs caching, a data fetching library is better. When the team already uses Redux Toolkit with its conventions, adding another store library may just add confusion. For form inputs, a form library is often a better choice.

### 59: How do you compute derived values from the store?

Compute them in a selector. You don't need to store derived values in state.

```js
const total = useCartStore((s) =>
  s.items.reduce((sum, item) => sum + item.price * item.qty, 0),
);
```

If the result is a primitive like a number, this is cheap and causes no extra re-renders.

### 60: Should you store derived data in the store?

Usually no. If you store both `items` and `total`, you must keep them in sync on every change, which is easy to get wrong. Compute derived values in selectors instead. Store them only if the calculation is expensive and you need to cache it.

### 61: How do you toggle a boolean in a store?

```js
const useUiStore = create((set) => ({
  sidebarOpen: false,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
}));
```

Use the function form of `set` because the new value depends on the old one.

### 62: When should you use the function form of `set`?

Use `set((state) => ...)` when the new value depends on the current state, like increments, toggles or adding to a list. Use the object form, `set({ ... })`, when you just set a fixed value. Both are fine; the function form avoids reading stale values.

### 63: How do you add an item to an array in the store?

```js
addItem: (item) => set((state) => ({ items: [...state.items, item] })),
```

### 64: How do you remove an item from an array in the store?

```js
removeItem: (id) =>
  set((state) => ({ items: state.items.filter((item) => item.id !== id) })),
```

### 65: How do you update one item in an array in the store?

```js
updateItem: (id, changes) =>
  set((state) => ({
    items: state.items.map((item) =>
      item.id === id ? { ...item, ...changes } : item,
    ),
  })),
```

### 66: How do you pass arguments to an action?

Actions are normal functions, so you define parameters and pass values when you call them.

```jsx
const useCartStore = create((set) => ({
  qty: 1,
  setQty: (qty) => set({ qty }),
}))

// in a component
const setQty = useCartStore((s) => s.setQty)
<button onClick={() => setQty(5)}>Set 5</button>
```

### 67: Can one action call another action?

Yes. Use `get()` to read the other action and call it.

```js
const useStore = create((set, get) => ({
  items: [],
  clear: () => set({ items: [] }),
  checkout: async () => {
    await fetch("/api/checkout", {
      method: "POST",
      body: JSON.stringify(get().items),
    });
    get().clear();
  },
}));
```

### 68: Can you use a store inside a custom hook?

Yes. Store hooks are normal hooks, so you can wrap them in your own hooks to give components a simpler API.

```js
export function useIsLoggedIn() {
  return useAuthStore((s) => s.user !== null);
}
```

### 69: Does Zustand follow the rules of hooks?

The hook returned by `create` is a real React hook, so you must call it at the top level of a component or custom hook, not inside loops, conditions or callbacks. The store methods like `getState` and `setState` are not hooks and can be called anywhere.

### 70: How do you use a store value in an event handler without subscribing to it?

Read it with `getState()` inside the handler. The component won't re-render when that value changes, which is what you want if you only need the value at click time.

```jsx
function SaveButton() {
  const save = () => {
    const draft = useEditorStore.getState().draft;
    fetch("/api/save", { method: "POST", body: JSON.stringify(draft) });
  };
  return <button onClick={save}>Save</button>;
}
```

### 71: How does Zustand work with React 18 and later?

It uses React's `useSyncExternalStore` hook. This hook was made for subscribing to stores that live outside React, and it keeps rendering consistent during concurrent rendering, so you don't get "tearing" (different components showing different versions of the same state).

### 72: What is tearing?

Tearing is when two components show different values for the same state during one render because the external store changed while React was rendering. `useSyncExternalStore`, which Zustand uses, prevents this.

### 73: What is the `combine` middleware?

`combine` takes an initial state object and a function that creates actions, and merges them. Its main use is TypeScript: the state type is inferred from the initial object, so you don't have to write an interface.

```ts
import { create } from "zustand";
import { combine } from "zustand/middleware";

const useCounterStore = create(
  combine({ count: 0 }, (set) => ({
    increment: () => set((s) => ({ count: s.count + 1 })),
  })),
);
```

### 74: What is the `subscribeWithSelector` middleware?

It changes the store's `subscribe` method so you can pass a selector and only be called when that selected value changes. You can also give an equality function and ask it to fire right away.

```js
import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";

const useStore = create(subscribeWithSelector(() => ({ count: 0, name: "" })));

useStore.subscribe(
  (state) => state.count,
  (count, prevCount) => console.log(prevCount, "->", count),
);
```

### 75: What is the `redux` middleware?

It lets you write the store as a reducer and update it with `dispatch`, like in Redux.

```js
import { create } from "zustand";
import { redux } from "zustand/middleware";

const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    default:
      return state;
  }
};

const useCounterStore = create(redux(reducer, { count: 0 }));

useCounterStore.dispatch({ type: "increment" });
```

It is useful when moving from Redux or when you like the reducer pattern.

### 76: What is the slices pattern?

It is a way to split a big store into smaller pieces. Each slice is a function that gets `set` and `get` and returns part of the state. You combine them in one `create` call.

```js
const createBearSlice = (set) => ({
  bears: 0,
  addBear: () => set((s) => ({ bears: s.bears + 1 })),
});

const createFishSlice = (set) => ({
  fishes: 0,
  addFish: () => set((s) => ({ fishes: s.fishes + 1 })),
});

const useBoundStore = create((...a) => ({
  ...createBearSlice(...a),
  ...createFishSlice(...a),
}));
```

### 77: Should you use one big store or many small stores?

Both work. Many small stores (one per feature) are easy to reason about and code split. One store with slices is better when slices need to read or update each other often, or when you want one place for middleware like `persist` or `devtools`. A common rule is: start with small separate stores and combine only when you need to.

### 78: Can a component use several stores?

Yes. Just call each store hook.

```jsx
function Header() {
  const user = useAuthStore((s) => s.user);
  const itemCount = useCartStore((s) => s.items.length);
  return (
    <div>
      {user?.name} ({itemCount})
    </div>
  );
}
```

### 79: How do you clear persisted data?

Call `clearStorage` on the store's `persist` API.

```js
useSettingsStore.persist.clearStorage();
```

This removes the item from storage but does not change the in-memory state. Reset the state separately if you need to.

### 80: How do you persist only some fields of the state?

Use the `partialize` option to return only the fields you want saved.

```js
persist(storeCreator, {
  name: "app",
  partialize: (state) => ({ theme: state.theme, language: state.language }),
});
```

Actions are not saved anyway, because functions can't be turned into JSON.

### 81: What is hydration in the context of `persist`?

Hydration is when `persist` reads the saved data from storage and merges it into the store. With `localStorage`, this happens right when the store is created. With async storage (like AsyncStorage in React Native or IndexedDB), it happens a bit later, so the first render may still show the default values.

### 82: How do you check if a persisted store has finished hydrating?

Use `persist.hasHydrated()`, or listen with `persist.onFinishHydration`.

```js
const hydrated = useSettingsStore.persist.hasHydrated();

const unsub = useSettingsStore.persist.onFinishHydration((state) => {
  console.log("hydrated", state);
});
```

### 83: How do you use Zustand persist with React Native?

Use `createJSONStorage` with AsyncStorage.

```js
import AsyncStorage from "@react-native-async-storage/async-storage";
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

const useStore = create(
  persist((set) => ({ token: null, setToken: (token) => set({ token }) }), {
    name: "auth",
    storage: createJSONStorage(() => AsyncStorage),
  }),
);
```

Because AsyncStorage is async, check `hasHydrated` before relying on the saved values.

### 84: Does Zustand work with React Native?

Yes. The core only depends on React, so it works the same in React Native as on the web. For persistence, use AsyncStorage or MMKV instead of `localStorage`.

### 85: Can you use Zustand in a Next.js app?

Yes, but only in client components (`'use client'`). Server components can't use hooks. Be careful with module-level stores on the server, because a store defined at module level is shared by all requests. For per-request data, the docs recommend creating the store per request and providing it through React context.

### 86: Does Zustand work with React Server Components?

No. Zustand hooks only work in client components. Server components should not read from or write to a Zustand store. You can fetch data in a server component and pass it as props to a client component that puts it into a store.

### 87: What does the devtools middleware need to work?

It needs the Redux DevTools browser extension. If the extension is not installed, the middleware does nothing and the store works as normal. By default it is turned on when not in production mode, and you can control that with the `enabled` option.

### 88: How do you turn off devtools in production?

Use the `enabled` option.

```js
devtools(storeCreator, {
  name: "AppStore",
  enabled: process.env.NODE_ENV !== "production",
});
```

Without `enabled`, the middleware is already off when the build runs in production mode (it checks `process.env.NODE_ENV` in the CommonJS build and `import.meta.env.MODE` in the ESM build), but setting `enabled` makes it explicit.

### 89: How do you name actions in Redux DevTools?

Pass a name as the third argument of `set`.

```js
increment: () => set((s) => ({ count: s.count + 1 }), undefined, 'counter/increment'),
```

The second argument is the `replace` flag, so pass `undefined` or `false` there. You can also pass an object like `{ type: 'counter/add', amount: 2 }`.

### 90: How do you write a simple counter with Zustand?

```jsx
import { create } from "zustand";

const useCounterStore = create((set) => ({
  count: 0,
  inc: () => set((s) => ({ count: s.count + 1 })),
  dec: () => set((s) => ({ count: s.count - 1 })),
}));

export default function Counter() {
  const count = useCounterStore((s) => s.count);
  const inc = useCounterStore((s) => s.inc);
  const dec = useCounterStore((s) => s.dec);

  return (
    <div>
      <button onClick={dec}>-</button>
      <span>{count}</span>
      <button onClick={inc}>+</button>
    </div>
  );
}
```

### 91: How do you write a simple todo store?

```js
import { create } from "zustand";

const useTodoStore = create((set) => ({
  todos: [],
  add: (text) =>
    set((s) => ({
      todos: [...s.todos, { id: crypto.randomUUID(), text, done: false }],
    })),
  toggle: (id) =>
    set((s) => ({
      todos: s.todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
    })),
  remove: (id) => set((s) => ({ todos: s.todos.filter((t) => t.id !== id) })),
}));
```

### 92: How do you store a simple auth state?

```js
const useAuthStore = create((set) => ({
  user: null,
  token: null,
  login: (user, token) => set({ user, token }),
  logout: () => set({ user: null, token: null }),
}));
```

Often this store is wrapped in `persist` so the user stays logged in after a page reload. Be careful about what you save, since `localStorage` can be read by any script on the page.

### 93: How do you store a theme setting?

```js
const useThemeStore = create(
  persist(
    (set) => ({
      theme: "light",
      toggleTheme: () =>
        set((s) => ({ theme: s.theme === "light" ? "dark" : "light" })),
    }),
    { name: "theme" },
  ),
);
```

### 94: How do you use a store value in a `useEffect`?

Select the value and use it as a dependency like any other value.

```jsx
const query = useSearchStore((s) => s.query);

useEffect(() => {
  if (!query) return;
  fetchResults(query);
}, [query]);
```

Actions can be called from effects too, and since their reference is stable they don't cause the effect to rerun.

### 95: Is it a problem to call `set` in a render function?

Yes. Calling `set` while rendering changes the store during render, which triggers more renders and can cause loops or React warnings. Call `set` in event handlers, effects or async callbacks, not during render.

### 96: What happens if `set` is called with the same value?

If the function form of `set` returns the current state object itself, nothing happens: no listeners are called. With the object form of `set`, a new state object is always created by the merge, so listeners do run, but components whose selected values didn't change won't re-render.

### 97: Can you store functions other than actions in the store?

Yes, any value can go in the store. But functions can't be saved with `persist` (JSON can't store them) and they don't show nicely in DevTools. Most of the time, functions in the store are actions.

### 98: Can you store class instances in the store?

You can, but be careful. If you mutate the instance, Zustand won't see the change. You must create a new instance or wrap it in a new object to trigger updates. Class instances also don't survive JSON persistence. Plain objects and arrays are easier.

### 99: Can you store a Map or a Set in the store?

Yes, but you must create a new Map or Set when it changes, because mutating it keeps the same reference.

```js
const useStore = create((set) => ({
  selected: new Set(),
  toggle: (id) =>
    set((s) => {
      const next = new Set(s.selected);
      next.has(id) ? next.delete(id) : next.add(id);
      return { selected: next };
    }),
}));
```

Note that Maps and Sets don't serialize to JSON, so `persist` needs a custom `replacer` and `reviver`.

### 100: Where should you put store files in a project?

There is no rule. Common choices are a `stores/` folder with one file per store (`stores/useCartStore.ts`), or keeping the store next to the feature that uses it (`features/cart/store.ts`). Keep the store and its selectors together.

### 101: How do you export selectors from a store file?

Write them as plain functions and export them, so components don't repeat the same logic.

```js
export const selectItemCount = (state) => state.items.length;
export const selectTotal = (state) =>
  state.items.reduce((sum, i) => sum + i.price * i.qty, 0);

// in a component
const total = useCartStore(selectTotal);
```

### 102: Why is a selector defined outside the component a good idea?

A selector defined outside the component has a stable reference, which is slightly better for performance, and it can be reused and tested on its own. Inline selectors like `(s) => s.count` are also fine for simple cases.

### 103: What does the `version` option in `persist` do?

It marks the shape of the saved data. When you change the state shape in a breaking way, you bump the version. On load, if the saved version is different, `persist` calls your `migrate` function to update the old data.

### 104: What does `migrate` do in `persist`?

`migrate` receives the old saved state and its version, and returns the state in the new shape.

```js
persist(storeCreator, {
  name: "settings",
  version: 1,
  migrate: (persistedState, version) => {
    if (version === 0) {
      return {
        ...persistedState,
        language: persistedState.lang,
        lang: undefined,
      };
    }
    return persistedState;
  },
});
```

If the version changes and there is no `migrate`, the saved state is not used and an error is logged.

### 105: How do you check what's in the store while debugging without DevTools?

Log it from the console or from code. Since the store is a module, you can expose it for debugging, for example `window.cartStore = useCartStore` in development, then call `cartStore.getState()` in the browser console. You can also `subscribe` and log every change.

### 106: Does Zustand batch updates?

Each `set` call updates the store right away and calls listeners. React 18 and later batch the resulting re-renders automatically, so calling `set` a few times in a row inside one event usually produces one render. You can also put several changes in one `set` call.

### 107: Can several components share one store without passing props?

Yes, that's the main point of Zustand. Any component that imports the store hook can read and update the same state, no matter where it is in the tree.

### 108: What is "state" and what are "actions" in a Zustand store?

State is the data, like `count` or `todos`. Actions are the functions that change the data, like `increment` or `addTodo`. In Zustand both are fields of the same object returned by the store creator.

### 109: What is `StateCreator` in TypeScript?

`StateCreator` is the type of the function you pass to `create`. You use it mostly when writing slices or reusable store parts.

```ts
import type { StateCreator } from "zustand";

interface BearSlice {
  bears: number;
  addBear: () => void;
}

const createBearSlice: StateCreator<BearSlice> = (set) => ({
  bears: 0,
  addBear: () => set((s) => ({ bears: s.bears + 1 })),
});
```

### 110: What is `StoreApi` in TypeScript?

`StoreApi<T>` is the type of a vanilla store object, with `getState`, `setState`, `getInitialState` and `subscribe`. It is often used when you pass a store around, for example in a context.

### 111: What is `ExtractState`?

`ExtractState` is a type helper that gets the state type from a store or a store hook.

```ts
import type { ExtractState } from "zustand";

type CounterState = ExtractState<typeof useCounterStore>;
```

It saves you from exporting the state interface separately.

### 112: How do you type a selector in TypeScript?

The state type comes from the store, so inline selectors are typed for you. For selectors defined outside the component, type the parameter.

```ts
const selectCount = (state: CounterState) => state.count;
const count = useCounterStore(selectCount); // number
```

### 113: Does Zustand store state immutably?

Zustand expects you to treat state as immutable. It doesn't freeze objects or stop you from mutating them; it just relies on new references to detect changes. If you mutate, updates get lost. The immer middleware makes immutable updates easier.

### 114: What happens to the store when a component unmounts?

Nothing. A store created with `create` lives at module level, so it keeps its state when components unmount and mount again. Only the component's subscription is removed. If you want state that resets with a component, use a store per component through context, or reset it yourself.

### 115: Does the store keep state across page reloads?

No, not by default. State is in memory and is lost on reload. Use the `persist` middleware to keep it in `localStorage`, `sessionStorage` or another storage.

### 116: How do you share a store between tabs?

Zustand doesn't sync tabs by itself. With `persist` and `localStorage`, you can listen to the browser `storage` event and call `persist.rehydrate()` so other tabs pick up the change.

```js
window.addEventListener("storage", (e) => {
  if (e.key === "settings-storage") {
    useSettingsStore.persist.rehydrate();
  }
});
```

There are also community packages built for this.

### 117: How do you set state from inside a `setTimeout` or `setInterval`?

Call the action or `setState` as usual. Since the store is outside React, there are no stale closure problems for store state the way there are with `useState`.

```js
setInterval(() => {
  useClockStore.getState().tick();
}, 1000);
```

### 118: What is a common beginner mistake with selectors?

Returning a new object or array from the selector without `useShallow`, for example `useStore((s) => ({ a: s.a, b: s.b }))`. The object is new on every call, so in v5 this can cause a "Maximum update depth exceeded" error. Use separate selectors or wrap it in `useShallow`.

### 119: What is another common beginner mistake with Zustand?

Destructuring the whole store: `const { count, inc } = useCounterStore()`. It looks clean, but the component then re-renders on every change in the store. Select only what you need.

### 120: Can you use Zustand with class components?

Not with the hook directly, because hooks only work in function components. You can wrap the class component in a small function component that reads the store and passes props, or use `subscribe` in `componentDidMount` and unsubscribe in `componentWillUnmount`.

### 121: Can you call the store hook conditionally?

No, it is a hook, so it can't be inside `if` statements. Call it unconditionally and handle the condition in the selector or after.

```jsx
const user = useAuthStore((s) => (enabled ? s.user : null));
```

### 122: How do you handle a form with Zustand?

Keep the field values in the store and update them with an action. For simple forms this is fine. For big forms with validation, a form library is usually better, and you only put the final result into Zustand.

```js
const useSignupStore = create((set) => ({
  values: { email: "", password: "" },
  setField: (name, value) =>
    set((s) => ({ values: { ...s.values, [name]: value } })),
}));
```

### 123: How do you store a multi-step wizard state?

```js
const useWizardStore = create((set) => ({
  step: 1,
  data: {},
  next: () => set((s) => ({ step: s.step + 1 })),
  back: () => set((s) => ({ step: Math.max(1, s.step - 1) })),
  setData: (part) => set((s) => ({ data: { ...s.data, ...part } })),
}));
```

Wrapping it in `persist` with `sessionStorage` keeps the progress if the user reloads the page.

### 124: How do you open and close a modal with Zustand?

```js
const useModalStore = create((set) => ({
  modal: null,
  open: (name, props = {}) => set({ modal: { name, props } }),
  close: () => set({ modal: null }),
}));
```

A single `<ModalRoot />` component reads `modal` and renders the right modal. Any component can call `open('confirm')` without passing props through the tree.

### 125: How do you show toast notifications with a store?

```js
const useToastStore = create((set) => ({
  toasts: [],
  show: (message) => {
    const id = crypto.randomUUID();
    set((s) => ({ toasts: [...s.toasts, { id, message }] }));
    setTimeout(() => {
      set((s) => ({ toasts: s.toasts.filter((t) => t.id !== id) }));
    }, 3000);
  },
}));
```

Because `show` can be called with `useToastStore.getState().show('Saved')`, even non-React code like API helpers can show toasts.

### 126: Where can you find the official Zustand documentation?

At zustand.docs.pmnd.rs. The source code and issues are on GitHub at pmndrs/zustand. The docs have guides (TypeScript, slices, testing, SSR, Next.js) and an API reference for every function and middleware.

### 127: Is Zustand only for small apps?

No. It is small, but people use it in large apps too. For large apps you still need structure: separate stores or slices per feature, exported selectors, clear naming, and tests. Zustand doesn't force any structure, so the team has to agree on one.

### 128: Does Zustand have any opinion about how to structure code?

Very little. It gives you `set`, `get` and a hook. Where you put actions, how you split stores, and how you name things is up to you. The docs suggest some patterns (slices, actions in the store or outside it, flux-inspired practices) but none of them are required.

### 129: What are the "flux inspired" practices the docs mention?

The docs suggest a few habits: keep a single store per area of state, update state only through `set` or `setState`, and keep actions together with the state they change. You can also use the `redux` middleware if you want reducers and dispatch.

### 130: How do you put actions outside the store?

Define the store with only data, and write actions as plain module functions.

```js
export const useCounterStore = create(() => ({ count: 0 }));

export const increment = () =>
  useCounterStore.setState((s) => ({ count: s.count + 1 }));
```

Components import `increment` directly, and you don't need a hook to call it. It also helps with code splitting.

### 131: What is the benefit of actions outside the store?

You can call them without a hook, they don't need to be selected in components, and unused actions can be removed by tree shaking. The downside is that the store and its actions are less grouped together, and middleware that relies on `set` inside the store (like devtools action names) needs a bit more care.

### 132: How do you write a selector that uses component props?

Use the prop inside the selector.

```jsx
function TodoItem({ id }) {
  const todo = useTodoStore((s) => s.todos.find((t) => t.id === id));
  return <li>{todo?.text}</li>;
}
```

`find` returns the existing object from the array, so the reference only changes when that todo changes.

### 133: Can selectors return `undefined`?

Yes. If the value doesn't exist, the selector returns `undefined`, and the component re-renders only when it becomes something else. Handle `undefined` in the component as usual.

### 134: Can you use the same store in two separate React roots?

Yes. A module-level store is shared by anything that imports it, including two different React roots on the same page or even non-React code. This is one of the reasons it doesn't need a Provider.

### 135: How do you write the store creator without using `set`?

If the store has no actions inside it, you can ignore all arguments.

```js
const usePositionStore = create(() => ({ x: 0, y: 0 }));

usePositionStore.setState({ x: 10 });
```

### 136: Can you subscribe to a store inside a component?

Yes, but usually you use the hook with a selector. Subscribing manually is for cases where you want to react to changes without re-rendering, for example updating a DOM node or a canvas. Do it in `useEffect` and return the unsubscribe function.

```jsx
useEffect(() => {
  return usePositionStore.subscribe((state) => {
    ref.current.style.transform = `translate(${state.x}px, ${state.y}px)`;
  });
}, []);
```

### 137: What does the third argument of the store creator give you?

The store API itself (`setState`, `getState`, `getInitialState`, `subscribe` and anything middleware added). It is mostly used by middleware and by slices that need to subscribe to the store.

### 138: Can you use JavaScript instead of TypeScript with Zustand?

Yes. All APIs work in plain JavaScript. TypeScript only adds type checking. The `create<T>()(...)` pattern is only needed in TypeScript.

### 139: How do you test a component that uses a Zustand store?

Render the component normally with React Testing Library. The store is real, so you can set it up with `setState` before rendering and reset it after each test.

```jsx
beforeEach(() => {
  useCounterStore.setState(useCounterStore.getInitialState(), true);
});

test("shows count", () => {
  useCounterStore.setState({ count: 5 });
  render(<Counter />);
  expect(screen.getByText("Count: 5")).toBeInTheDocument();
});
```

### 140: Why do you need to reset stores between tests?

Stores live at module level, so state from one test stays for the next test in the same file. Without a reset, tests depend on order and can fail randomly. Reset in `beforeEach` or `afterEach`.

### 141: How do you test a store without React?

Call actions and read state directly.

```js
test("increment", () => {
  useCounterStore.getState().increment();
  expect(useCounterStore.getState().count).toBe(1);
});
```

No rendering is needed, which makes store tests fast and simple.

### 142: How do you share types between the store and components?

Export the state interface from the store file, or use `ExtractState<typeof useMyStore>`. Selectors and components can then import the type.

### 143: How do you install the immer middleware?

```bash
npm install immer
```

Then import it from `zustand/middleware/immer`, not from `zustand/middleware`.

```js
import { immer } from "zustand/middleware/immer";
```

### 144: Why is immer middleware imported from a separate path?

Because it depends on the `immer` package. Keeping it in its own entry point means people who don't use immer don't need to install it.

### 145: What is the difference between `set` and `setState`?

They do the same thing. `set` is the name of the first argument inside the store creator. `setState` is the method on the store object, for use outside the store. Middleware can wrap both.

### 146: Can you rename `set` and `get` in the store creator?

Yes, they are just function parameters, so the names are up to you. `set` and `get` are the convention, and most examples and docs use them.

### 147: How do you add a new field to a store later?

Add it to the object returned by the store creator, with a default value. If the store is persisted, old saved data won't have it, but the default `merge` in `persist` keeps your default value for missing keys. If you rename or change existing fields, bump `version` and add a `migrate` function.

### 148: How do you show a value from the store and update it from an input?

```jsx
function NameInput() {
  const name = useProfileStore((s) => s.name);
  const setName = useProfileStore((s) => s.setName);
  return <input value={name} onChange={(e) => setName(e.target.value)} />;
}
```

### 149: What does Zustand give you that `useReducer` + context doesn't?

Selective re-renders (only the components that use the changed value re-render), access to state outside of React, no Provider needed, built-in middleware like persist and devtools, and less code. With `useReducer` plus context, every consumer of the context re-renders when the value changes.

### 150: How would you explain Zustand to someone new in one or two sentences?

Zustand is a small library where you put shared state and the functions that change it into one object, and any component can read just the part it needs with a hook. It has no Provider, no reducers and no action types unless you want them.

## Moderate Questions (151-300)

### 151: In what order should you apply several middlewares?

Put `devtools` on the outside, so it sees the final `setState` after all the other middleware changed it. A common order is:

```ts
const useStore = create<State>()(
  devtools(
    persist(
      immer((set) => ({
        // state and actions
      })),
      { name: "app" },
    ),
    { name: "AppStore" },
  ),
);
```

If `devtools` is inside `persist` or `immer`, actions from those wrappers may not show up correctly, and TypeScript may lose the extra `set` argument for action names.

### 152: Why do the Zustand docs say to use `devtools` as the last middleware?

`devtools` replaces `setState` with a version that sends every change to the extension. Other middleware like `immer` also replaces `setState`. If another middleware wraps `devtools`, its changes go around the devtools version and are not recorded. Putting `devtools` last (outermost) means every update passes through it.

### 153: How do you type a store that uses several middlewares in TypeScript?

Use the curried `create<State>()` and wrap normally. Types for `persist`, `devtools` and `immer` are inferred from the middleware.

```ts
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

interface BearState {
  bears: number;
  increase: (by: number) => void;
}

const useBearStore = create<BearState>()(
  devtools(
    persist(
      (set) => ({
        bears: 0,
        increase: (by) => set((s) => ({ bears: s.bears + by })),
      }),
      { name: "bear-storage" },
    ),
  ),
);
```

### 154: How do you type slices in TypeScript?

Give each slice a `StateCreator` with the full combined state as the first type and the slice as the last.

```ts
import { create, type StateCreator } from "zustand";

interface BearSlice {
  bears: number;
  addBear: () => void;
  eatFish: () => void;
}
interface FishSlice {
  fishes: number;
  addFish: () => void;
}

const createBearSlice: StateCreator<
  BearSlice & FishSlice,
  [],
  [],
  BearSlice
> = (set) => ({
  bears: 0,
  addBear: () => set((s) => ({ bears: s.bears + 1 })),
  eatFish: () => set((s) => ({ fishes: s.fishes - 1 })),
});

const createFishSlice: StateCreator<
  BearSlice & FishSlice,
  [],
  [],
  FishSlice
> = (set) => ({
  fishes: 0,
  addFish: () => set((s) => ({ fishes: s.fishes + 1 })),
});

export const useBoundStore = create<BearSlice & FishSlice>()((...a) => ({
  ...createBearSlice(...a),
  ...createFishSlice(...a),
}));
```

The first type lets a slice read and update other slices.

### 155: What do the second and third type parameters of `StateCreator` mean?

They describe middleware "mutators". The second list is the middleware applied around this creator (what `set` and the store look like inside it), and the third is the middleware this creator itself adds. For a slice used inside `devtools`, you write:

```ts
const createBearSlice: StateCreator<
  BearSlice & FishSlice,
  [["zustand/devtools", never]],
  [],
  BearSlice
> = (set) => ({
  bears: 0,
  addBear: () =>
    set((s) => ({ bears: s.bears + 1 }), undefined, "bear/addBear"),
  eatFish: () => set((s) => ({ fishes: s.fishes - 1 })),
});
```

Now `set` accepts the third argument (the action name) that `devtools` adds.

### 156: Where should middleware go when you use the slices pattern?

Apply middleware once, on the combined store, not inside each slice. Applying `persist` or `devtools` inside a slice can cause odd behavior because the slice only sees part of the state.

```ts
const useBoundStore = create<BearSlice & FishSlice>()(
  devtools(
    persist(
      (...a) => ({
        ...createBearSlice(...a),
        ...createFishSlice(...a),
      }),
      { name: "bound-store" },
    ),
  ),
);
```

### 157: How do you reset all slices of a store?

Each slice can register its initial state, and a shared `resetAll` puts them back.

```ts
const sliceResetFns = new Set<() => void>();

export const resetAllSlices = () => {
  sliceResetFns.forEach((reset) => reset());
};

const initialBearState = { bears: 0 };

const createBearSlice: StateCreator<
  BearSlice & FishSlice,
  [],
  [],
  BearSlice
> = (set) => {
  sliceResetFns.add(() => set(initialBearState));
  return {
    ...initialBearState,
    addBear: () => set((s) => ({ bears: s.bears + 1 })),
    eatFish: () => set((s) => ({ fishes: s.fishes - 1 })),
  };
};
```

If you only need to reset the whole store, `setState(getInitialState(), true)` is simpler.

### 158: How do you reset several separate stores at once, for example on logout?

Keep a list of reset functions and call them all.

```ts
const resetters: (() => void)[] = [];

export function createResettable<T>(initializer: StateCreator<T>) {
  const store = create<T>()(initializer);
  resetters.push(() => store.setState(store.getInitialState(), true));
  return store;
}

export const resetAllStores = () => resetters.forEach((reset) => reset());
```

Call `resetAllStores()` in your logout action. Persisted stores also need `persist.clearStorage()`.

### 159: How do you create a store per component instance with context?

Use `createStore` with `useState` (or `useRef`) so the store is created once per Provider, then read it with `useStore`.

```tsx
import { createContext, useContext, useState, type ReactNode } from "react";
import { createStore, useStore, type StoreApi } from "zustand";

interface CounterState {
  count: number;
  inc: () => void;
}

const createCounterStore = (initial: number) =>
  createStore<CounterState>()((set) => ({
    count: initial,
    inc: () => set((s) => ({ count: s.count + 1 })),
  }));

const CounterContext = createContext<StoreApi<CounterState> | null>(null);

export function CounterProvider({
  initial,
  children,
}: {
  initial: number;
  children: ReactNode;
}) {
  const [store] = useState(() => createCounterStore(initial));
  return (
    <CounterContext.Provider value={store}>{children}</CounterContext.Provider>
  );
}

export function useCounter<T>(selector: (s: CounterState) => T): T {
  const store = useContext(CounterContext);
  if (!store) throw new Error("useCounter must be used inside CounterProvider");
  return useStore(store, selector);
}
```

### 160: When do you need a store in context instead of a global store?

When you need more than one instance of the same state: several copies of a widget on a page, a store per tab, a store that must be created with props, a store per request in server rendering, or a store that should reset when part of the tree unmounts. For app-wide client state, a global store is fine.

### 161: Why should you create the context store in `useState(() => ...)` or `useRef` and not in the render body?

If you call `createStore` directly in the render body, a new store is created on every render, and all state is lost each time. A lazy `useState` initializer or a `useRef` that is filled once keeps the same store for the life of the Provider.

### 162: Why does the context hold the store and not the state?

If you put the state in context, every consumer re-renders on every change, which is the problem Zustand is trying to fix. The store object itself never changes, so the context value is stable. Components then use `useStore` with a selector to subscribe to just what they need.

### 163: How do you initialize a store with props?

Create the store in a Provider with the props as initial values.

```tsx
const createBearStore = (initProps?: Partial<BearProps>) =>
  createStore<BearState>()((set) => ({
    bears: 0,
    ...initProps,
    addBear: () => set((s) => ({ bears: s.bears + 1 })),
  }));
```

The props are only used when the store is created. If the props change later, you have to sync them yourself, for example with an effect that calls `setState`.

### 164: What happened to `zustand/context`?

It was a helper (`createContext`) from v3. It was deprecated in v4 and removed in v5. The recommended way now is to use React's own `createContext` with `createStore` and `useStore`, like in the context examples above.

### 165: How do you auto-generate selectors for every field in a store?

The docs show a small helper that adds a `use` object with one hook per key.

```ts
import type { StoreApi, UseBoundStore } from "zustand";

type WithSelectors<S> = S extends { getState: () => infer T }
  ? S & { use: { [K in keyof T]: () => T[K] } }
  : never;

export const createSelectors = <S extends UseBoundStore<StoreApi<object>>>(
  _store: S,
) => {
  const store = _store as WithSelectors<typeof _store>;
  store.use = {};
  for (const k of Object.keys(store.getState())) {
    (store.use as any)[k] = () => store((s) => s[k as keyof typeof s]);
  }
  return store;
};

const useBearStore = createSelectors(useBearStoreBase);
const bears = useBearStore.use.bears();
```

It saves typing but every call is still a separate subscription to one field.

### 166: What is `createWithEqualityFn` and when do you use it?

It comes from `zustand/traditional`. It works like `create`, but the hook accepts an equality function as the second argument, and you can set a default equality function for the whole store. It is useful when moving from v4, where `create` accepted `shallow` as a second argument.

```ts
import { createWithEqualityFn } from "zustand/traditional";
import { shallow } from "zustand/shallow";

const useStore = createWithEqualityFn<State>()(
  (set) => ({ a: 1, b: 2 }),
  shallow,
);

const { a, b } = useStore((s) => ({ a: s.a, b: s.b }));
```

It needs the `use-sync-external-store` package.

### 167: What is `useStoreWithEqualityFn`?

It is the vanilla store version of `createWithEqualityFn`. You pass a vanilla store, a selector and an equality function.

```ts
import { useStoreWithEqualityFn } from "zustand/traditional";
import { shallow } from "zustand/shallow";

const { x, y } = useStoreWithEqualityFn(
  positionStore,
  (s) => ({ x: s.x, y: s.y }),
  shallow,
);
```

### 168: What is the difference between `useShallow` and passing `shallow` to `createWithEqualityFn`?

Both stop re-renders when the selected object is shallowly equal. `useShallow` wraps the selector and returns a stable reference, so it works with the normal `create` hook and plain `useStore`. `shallow` as an equality function needs the `traditional` APIs and `use-sync-external-store`. For new code, `useShallow` is the usual choice.

### 169: Why did v5 remove the equality function from `create`?

v5 uses React's `useSyncExternalStore` directly, which doesn't support a custom equality function. Keeping it would mean depending on the `use-sync-external-store/with-selector` shim. So the default became simpler, and the old behavior moved to `zustand/traditional`.

### 170: Why can a selector that returns a new array cause an infinite loop in v5?

`useSyncExternalStore` expects the snapshot to be the same when nothing changed. A selector like `(s) => s.items.filter((i) => i.done)` returns a new array every call. React sees a different value each time it checks, thinks the store changed, re-renders, and repeats, which ends in "Maximum update depth exceeded". Use `useShallow` or select the raw data and filter in the component (or with `useMemo`).

### 171: How do you fix a selector that returns a filtered list?

Option 1, `useShallow`:

```ts
const doneTodos = useTodoStore(
  useShallow((s) => s.todos.filter((t) => t.done)),
);
```

Option 2, select the source and derive in the component:

```ts
const todos = useTodoStore((s) => s.todos);
const doneTodos = useMemo(() => todos.filter((t) => t.done), [todos]);
```

The second is better when the filter is expensive, because `useShallow` still runs the filter on every store change.

### 172: Why should a fallback value in a selector be a constant?

A selector like `(s) => s.list ?? []` returns a new empty array every time `list` is missing, which can cause re-renders or the infinite loop error. Use a constant defined outside the component.

```ts
const EMPTY: Item[] = [];
const list = useStore((s) => s.list ?? EMPTY);
```

### 173: How do you select several actions at once?

Actions are stable, so `useShallow` works well.

```ts
const { add, remove, clear } = useCartStore(
  useShallow((s) => ({ add: s.add, remove: s.remove, clear: s.clear })),
);
```

Some teams group actions in a nested `actions` object so one selector returns them all with a stable reference.

```ts
const useCartStore = create<CartState>()((set) => ({
  items: [],
  actions: {
    add: (item) => set((s) => ({ items: [...s.items, item] })),
    clear: () => set({ items: [] }),
  },
}));

export const useCartActions = () => useCartStore((s) => s.actions);
```

### 174: What is the downside of the nested `actions` object pattern?

With `persist`, the `actions` object is saved as `{}` (JSON drops the functions inside it), and on reload the default shallow merge replaces your real actions with that empty object. So you must exclude it with `partialize`. Also, `set` merges only the top level, so you must never return a new `actions` object by mistake.

### 175: How do you debug unnecessary re-renders in a Zustand app?

Use the React DevTools Profiler with "Highlight updates" to see which components re-render. Then check their selectors: look for hooks called without a selector, selectors returning new objects or arrays, and inline fallbacks like `?? []`. You can also log inside a selector or use `subscribe` to see how often the store changes.

### 176: How do you log every state change in development?

Subscribe and log both states.

```ts
if (import.meta.env.DEV) {
  useCartStore.subscribe((state, prev) => {
    console.log("[cart]", prev, "->", state);
  });
}
```

For a nicer view, use the `devtools` middleware.

### 177: How do you write a simple custom middleware?

A middleware takes a store creator and returns a new one. Here is a logger:

```js
const logger = (config) => (set, get, api) =>
  config(
    (...args) => {
      console.log("before", get());
      set(...args);
      console.log("after", get());
    },
    get,
    api,
  );

const useStore = create(
  logger((set) => ({
    count: 0,
    inc: () => set((s) => ({ count: s.count + 1 })),
  })),
);
```

Note that this only wraps the `set` used inside the store. Calls to `useStore.setState` from outside skip it unless you also replace `api.setState`.

### 178: How do you make a custom middleware also catch `setState` calls from outside the store?

Replace `api.setState` too, and pass the wrapped one into the creator.

```js
const logger = (config) => (set, get, api) => {
  const loggedSet = (...args) => {
    set(...args);
    console.log("new state", get());
  };
  api.setState = loggedSet;
  return config(loggedSet, get, api);
};
```

This is the same approach the built-in `persist` and `immer` middleware use.

### 179: How does `persist` work with a custom storage?

You give it an object with `getItem`, `setItem` and `removeItem`. With `createJSONStorage`, your storage only needs to work with strings, and Zustand handles `JSON.stringify` and `JSON.parse`.

```ts
import { get, set, del } from "idb-keyval";
import { createJSONStorage, type StateStorage } from "zustand/middleware";

const idbStorage: StateStorage = {
  getItem: async (name) => (await get(name)) ?? null,
  setItem: async (name, value) => {
    await set(name, value);
  },
  removeItem: async (name) => {
    await del(name);
  },
};

persist(storeCreator, {
  name: "big-store",
  storage: createJSONStorage(() => idbStorage),
});
```

### 180: How do you persist a Map, Set or Date?

JSON can't represent them, so pass a `replacer` and `reviver` to `createJSONStorage`.

```ts
storage: createJSONStorage(() => localStorage, {
  replacer: (key, value) =>
    value instanceof Map ? { __type: 'Map', entries: [...value] } : value,
  reviver: (key, value: any) =>
    value && value.__type === 'Map' ? new Map(value.entries) : value,
}),
```

Dates are a special case: `JSON.stringify` calls `toJSON` before your replacer, so the replacer already receives a string. It is often simpler to store timestamps as numbers or ISO strings and convert them where you use them.

### 181: What does the `merge` option in `persist` do?

It decides how saved state is combined with the current state during hydration. The default is a shallow merge: `{ ...currentState, ...persistedState }`. That means a nested object from storage completely replaces the default nested object, and new nested fields you added in code are lost. Write a custom `merge` (often a deep merge) if your state is nested.

```ts
merge: (persisted, current) => ({
  ...current,
  ...(persisted as Partial<State>),
  settings: { ...current.settings, ...(persisted as Partial<State>).settings },
}),
```

### 182: What does `onRehydrateStorage` do?

It runs before hydration starts and can return a function that runs after hydration finishes or fails.

```ts
persist(storeCreator, {
  name: "app",
  onRehydrateStorage: (state) => {
    console.log("hydration starts");
    return (state, error) => {
      if (error) console.error("hydration failed", error);
      else console.log("hydration finished");
    };
  },
});
```

It is often used to set a `hasHydrated` flag in the store.

### 183: What does `skipHydration` do?

When `skipHydration: true`, `persist` doesn't read storage when the store is created. You call `persist.rehydrate()` yourself when you are ready, for example in a `useEffect` after the first client render. This helps avoid server/client mismatches in SSR apps.

```tsx
useEffect(() => {
  useSettingsStore.persist.rehydrate();
}, []);
```

### 184: Why does a persisted store cause a hydration mismatch in Next.js?

On the server there is no `localStorage`, so the server renders the default state. On the client, `persist` reads `localStorage` right away, so the first client render may show different values. React then reports a hydration error. Fix it with `skipHydration` plus `rehydrate()` in an effect, or by rendering persisted values only after a "mounted" or "hydrated" flag is true.

### 185: How do you write a hook that waits for a persisted store to hydrate?

```ts
import { useEffect, useState } from "react";

export function useHydrated() {
  const [hydrated, setHydrated] = useState(
    useSettingsStore.persist.hasHydrated(),
  );

  useEffect(() => {
    const unsubFinish = useSettingsStore.persist.onFinishHydration(() =>
      setHydrated(true),
    );
    setHydrated(useSettingsStore.persist.hasHydrated());
    return unsubFinish;
  }, []);

  return hydrated;
}
```

Show a loader or default UI until it returns `true`.

### 186: What do `persist.onHydrate` and `persist.onFinishHydration` do?

`onHydrate` registers a listener called when hydration starts, and `onFinishHydration` registers one called when it ends. Both get the state and return an unsubscribe function. They are useful outside of the store config, for example in a component.

### 187: How do you change `persist` options at runtime?

Use `persist.setOptions`. For example, change the storage key when the user changes, then rehydrate.

```ts
useCartStore.persist.setOptions({ name: `cart-${userId}` });
await useCartStore.persist.rehydrate();
```

`persist.getOptions()` returns the current options.

### 188: Can `migrate` be async?

Yes. `migrate` can return a Promise, and hydration waits for it. This is useful when the migration needs to read data from another place, like an old IndexedDB database.

### 189: Does `persist` write to storage when the store is created?

Not in v5 (and since v4.5.5). It only writes when state changes through `set` or `setState`. If you need the initial state saved right away, call `setState` once after creating the store.

### 190: How do you persist state in the URL instead of localStorage?

Write a custom `StateStorage` that reads and writes the URL.

```ts
const hashStorage: StateStorage = {
  getItem: (key) => {
    const params = new URLSearchParams(location.hash.slice(1));
    const value = params.get(key);
    return value ? JSON.parse(value) : null;
  },
  setItem: (key, value) => {
    const params = new URLSearchParams(location.hash.slice(1));
    params.set(key, JSON.stringify(value));
    location.hash = params.toString();
  },
  removeItem: (key) => {
    const params = new URLSearchParams(location.hash.slice(1));
    params.delete(key);
    location.hash = params.toString();
  },
};

persist(storeCreator, {
  name: "filters",
  storage: createJSONStorage(() => hashStorage),
});
```

Here `getItem` must return a string, which is why the stored value is parsed once. The docs have a similar example called "connect to state with URL hash".

### 191: Should you use Zustand or the URL for filter and search state?

If the state should be shareable or survive a refresh with a link (search text, filters, page number, tab), the URL is usually the source of truth, often through the router's search params. You can still mirror it in a store if many components need it, but keep the URL as the main copy so links work.

### 192: What does the devtools `store` option do?

It lets several stores share one DevTools connection. All stores with the same `name` appear together, each under its `store` key, and action types are prefixed with the store name.

```ts
const useBearStore = create<BearState>()(
  devtools((set) => ({ bears: 0 }), { name: "MyApp", store: "bears" }),
);
const useFishStore = create<FishState>()(
  devtools((set) => ({ fishes: 0 }), { name: "MyApp", store: "fishes" }),
);
```

### 193: What is `anonymousActionType` in devtools?

It is the action name used when you call `set` without a name. If you don't set it, the middleware tries to read the name of the calling function from the stack trace and falls back to `"anonymous"`. Setting it gives you a fixed default.

### 194: What does `store.devtools.cleanup()` do?

It disconnects the store from the DevTools extension and stops listening to messages from it. It is useful in tests or when you create and throw away stores, such as per-component stores, so connections don't pile up.

### 195: Can you time-travel with Zustand devtools?

Yes, mostly. The devtools middleware listens to jump and reset messages from the extension and sets the store state to the selected point. Dispatching custom actions from the extension only works when the store uses the `redux` middleware, which provides a `dispatch` function.

### 196: How do you use immer with devtools?

Wrap `immer` inside `devtools`. The action name still goes in the third argument of `set`.

```ts
const useTodoStore = create<TodoState>()(
  devtools(
    immer((set) => ({
      todos: [],
      add: (text) =>
        set(
          (state) => {
            state.todos.push({ id: crypto.randomUUID(), text, done: false });
          },
          undefined,
          "todos/add",
        ),
    })),
  ),
);
```

### 197: In the immer middleware, can you still return a new object from `set`?

Yes. You can either mutate the draft and return nothing, or pass a plain object for a normal merge. What you should not do is mutate the draft and also return a value from the same function; immer will throw an error for that.

```ts
set((state) => {
  state.count += 1;
}); // mutate draft
set({ count: 0 }); // plain partial object
```

### 198: What are the downsides of the immer middleware?

It adds the `immer` dependency (a few KB) and a small cost on every update. Drafts are proxies, so logging them shows proxy objects (use `current(draft)` from immer to see values). Also, people new to the codebase may forget that the mutation style only works inside the immer `set`, and mutate state elsewhere.

### 199: How do you subscribe to a specific field outside React?

Use `subscribeWithSelector`, or write the comparison yourself with plain `subscribe`.

```ts
// with the middleware
useStore.subscribe(
  (s) => s.user,
  (user) => analytics.identify(user?.id),
);

// without it
useStore.subscribe((state, prev) => {
  if (state.user !== prev.user) analytics.identify(state.user?.id);
});
```

### 200: What options does `subscribeWithSelector` accept?

The third argument has `equalityFn` and `fireImmediately`.

```ts
import { shallow } from "zustand/shallow";

useStore.subscribe(
  (s) => [s.x, s.y],
  ([x, y]) => console.log(x, y),
  { equalityFn: shallow, fireImmediately: true },
);
```

`equalityFn` decides whether the selected value changed (default `Object.is`). `fireImmediately` calls the listener once right away with the current value.

### 201: How do you handle race conditions in async actions?

If the user triggers the same request twice, the slower old response can overwrite the newer one. Keep a request id and ignore old responses, or cancel the old request with `AbortController`.

```ts
let controller: AbortController | null = null;

const useSearchStore = create<SearchState>()((set) => ({
  results: [],
  search: async (query) => {
    controller?.abort();
    controller = new AbortController();
    try {
      const res = await fetch(`/api/search?q=${query}`, {
        signal: controller.signal,
      });
      set({ results: await res.json() });
    } catch (err) {
      if ((err as Error).name !== "AbortError") throw err;
    }
  },
}));
```

### 202: How do you do an optimistic update with Zustand?

Update the store first, send the request, and roll back if it fails.

```ts
toggleLike: async (postId) => {
  const prev = get().posts
  set({
    posts: prev.map((p) => (p.id === postId ? { ...p, liked: !p.liked } : p)),
  })
  try {
    await fetch(`/api/posts/${postId}/like`, { method: 'POST' })
  } catch {
    set({ posts: prev })
  }
},
```

Rolling back to `prev` can undo other changes made in the meantime. For more safety, roll back only the item you changed.

### 203: How do you debounce an action in a store?

Keep the timer outside the state and clear it on each call.

```ts
let timer: ReturnType<typeof setTimeout> | undefined;

const useSearchStore = create<SearchState>()((set, get) => ({
  query: "",
  setQuery: (query) => {
    set({ query });
    clearTimeout(timer);
    timer = setTimeout(() => get().search(query), 300);
  },
  search: async (q) => {
    /* ... */
  },
}));
```

The input updates right away, and the request runs only after the user stops typing.

### 204: Should timers, sockets or AbortControllers be stored in state?

Usually no. They are not data for the UI, they don't serialize, and changing them would notify subscribers for no reason. Keep them in module variables or in a closure inside the store creator.

### 205: How do you keep a websocket connection in sync with a store?

Open the socket outside React (or in a top-level effect) and call `setState` when messages arrive.

```ts
export function connectPrices() {
  const ws = new WebSocket("wss://example.com/prices");
  ws.onmessage = (event) => {
    const { symbol, price } = JSON.parse(event.data);
    usePriceStore.setState((s) => ({
      prices: { ...s.prices, [symbol]: price },
    }));
  };
  return () => ws.close();
}
```

Components select only the symbols they show, so a price change for one symbol doesn't re-render the whole list.

### 206: How do you use the auth token from a store in a fetch helper?

Read it with `getState()`. No hook is needed.

```ts
export async function api(path: string, init: RequestInit = {}) {
  const token = useAuthStore.getState().token;
  const res = await fetch(path, {
    ...init,
    headers: { ...init.headers, Authorization: `Bearer ${token}` },
  });
  if (res.status === 401) useAuthStore.getState().logout();
  return res;
}
```

The same works in an axios interceptor.

### 207: How do you use Zustand together with TanStack Query?

Let TanStack Query own server data and Zustand own client state. A typical example: Zustand holds the filters, and the query key uses them.

```tsx
function ProductList() {
  const filters = useFilterStore(
    useShallow((s) => ({ category: s.category, sort: s.sort })),
  );
  const { data } = useQuery({
    queryKey: ["products", filters],
    queryFn: () => fetchProducts(filters),
  });
  return <List items={data ?? []} />;
}
```

Avoid copying query results into a Zustand store, because then you have two caches to keep in sync.

### 208: How do you use a store in React Router loaders or actions?

Loaders run outside components, so use `getState()` and `setState()`.

```ts
export async function loader() {
  const { token } = useAuthStore.getState();
  if (!token) throw redirect("/login");
  return fetchDashboard(token);
}
```

### 209: How do you set up Zustand in the Next.js App Router?

The docs recommend a store factory, a client Provider that creates the store once, and a hook that reads it from context.

```tsx
// stores/counter-store.ts
import { createStore } from "zustand/vanilla";

export type CounterState = { count: number };
export type CounterActions = { inc: () => void };
export type CounterStore = CounterState & CounterActions;

export const createCounterStore = (initState: CounterState = { count: 0 }) =>
  createStore<CounterStore>()((set) => ({
    ...initState,
    inc: () => set((s) => ({ count: s.count + 1 })),
  }));
```

```tsx
// providers/counter-store-provider.tsx
"use client";
import { createContext, useContext, useState, type ReactNode } from "react";
import { useStore } from "zustand";
import { createCounterStore, type CounterStore } from "@/stores/counter-store";

type CounterStoreApi = ReturnType<typeof createCounterStore>;
const CounterStoreContext = createContext<CounterStoreApi | undefined>(
  undefined,
);

export function CounterStoreProvider({ children }: { children: ReactNode }) {
  const [store] = useState(() => createCounterStore());
  return (
    <CounterStoreContext.Provider value={store}>
      {children}
    </CounterStoreContext.Provider>
  );
}

export function useCounterStore<T>(selector: (store: CounterStore) => T): T {
  const store = useContext(CounterStoreContext);
  if (!store)
    throw new Error("useCounterStore must be used within CounterStoreProvider");
  return useStore(store, selector);
}
```

Put the Provider in a layout or page. The store is created once per request on the server and once in the browser.

### 210: Why shouldn't you use a module-level store for per-user data in Next.js?

On the server, a module is loaded once and shared by all requests. If you write user data into a module-level store during server rendering, the next request from a different user can see it. That leaks data between users. Create the store per request (in a Provider) or only write to global stores on the client.

### 211: Where should the Provider go in the Next.js App Router?

Put it as low in the tree as possible, around the part of the app that needs the store. If it is in the root layout, it wraps everything, which is fine for app-wide state. Note that a Provider in a layout keeps its store across navigations between pages of that layout. If you want fresh state per page, put the Provider in the page.

### 212: How do you pass server data into a Zustand store in Next.js?

Fetch in a server component and pass the data as a prop to the client Provider, which uses it as the initial state.

```tsx
// app/cart/page.tsx (server component)
export default async function CartPage() {
  const cart = await getCart();
  return (
    <CartStoreProvider initialItems={cart.items}>
      <Cart />
    </CartStoreProvider>
  );
}
```

The Provider calls `createCartStore({ items: initialItems })` once in `useState`. Server and client start with the same data, so there is no hydration mismatch.

### 213: How do you mock Zustand in Jest so every store resets after each test?

The docs show a `__mocks__/zustand.ts` file that wraps `create` and `createStore`, records each store's initial state, and resets them all in `afterEach`.

```ts
// __mocks__/zustand.ts
import { act } from "@testing-library/react";
import type * as ZustandExportedTypes from "zustand";
export * from "zustand";

const { create: actualCreate, createStore: actualCreateStore } =
  jest.requireActual<typeof ZustandExportedTypes>("zustand");

export const storeResetFns = new Set<() => void>();

const createUncurried = <T>(
  stateCreator: ZustandExportedTypes.StateCreator<T>,
) => {
  const store = actualCreate(stateCreator);
  const initialState = store.getInitialState();
  storeResetFns.add(() => store.setState(initialState, true));
  return store;
};

export const create = (<T>(
  stateCreator: ZustandExportedTypes.StateCreator<T>,
) =>
  typeof stateCreator === "function"
    ? createUncurried(stateCreator)
    : createUncurried) as typeof ZustandExportedTypes.create;

const createStoreUncurried = <T>(
  stateCreator: ZustandExportedTypes.StateCreator<T>,
) => {
  const store = actualCreateStore(stateCreator);
  const initialState = store.getInitialState();
  storeResetFns.add(() => store.setState(initialState, true));
  return store;
};

export const createStore = (<T>(
  stateCreator: ZustandExportedTypes.StateCreator<T>,
) =>
  typeof stateCreator === "function"
    ? createStoreUncurried(stateCreator)
    : createStoreUncurried) as typeof ZustandExportedTypes.createStore;

afterEach(() => {
  act(() => {
    storeResetFns.forEach((resetFn) => resetFn());
  });
});
```

The `__mocks__` folder must be next to `node_modules` (the project root) for Jest to pick it up automatically.

### 214: How do you do the same reset setup in Vitest?

Vitest doesn't automatically pick up root `__mocks__` for packages. Put the mock in `__mocks__/zustand.ts`, use `vi.importActual` instead of `jest.requireActual`, and call `vi.mock('zustand')` in a setup file.

```ts
// __mocks__/zustand.ts (top part)
const { create: actualCreate, createStore: actualCreateStore } =
  await vi.importActual<typeof ZustandExportedTypes>("zustand");
```

```ts
// setup-vitest.ts
import "@testing-library/jest-dom/vitest";
vi.mock("zustand");
```

Add the setup file to `test.setupFiles` in the Vitest config. You also need a `__mocks__` folder at the project root, as with Jest.

### 215: Why are store updates wrapped in `act` in tests?

When a test changes the store while components are rendered, React needs to process the resulting re-renders. Wrapping the change in `act` makes React finish those updates before your assertions run, and it removes the "not wrapped in act" warnings.

```tsx
act(() => {
  useCounterStore.getState().increment();
});
expect(screen.getByText("Count: 1")).toBeInTheDocument();
```

Events fired through `userEvent` or `fireEvent` are already wrapped.

### 216: How do you test an async action that calls fetch?

Mock `fetch` (or use MSW), call the action, await it, and check the state.

```ts
test("fetchUser stores the user", async () => {
  global.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: async () => ({ id: 1, name: "Ana" }),
  }) as unknown as typeof fetch;

  await useUserStore.getState().fetchUser(1);

  expect(useUserStore.getState().user).toEqual({ id: 1, name: "Ana" });
  expect(useUserStore.getState().loading).toBe(false);
});
```

### 217: How do you test a component with a store that lives in context?

Render it inside the Provider, and if needed pass initial values through the Provider's props. Each test gets a fresh store, so no reset is needed.

```tsx
render(
  <CounterProvider initial={3}>
    <Counter />
  </CounterProvider>,
);
```

This is one of the nice side effects of the context pattern.

### 218: How do you test a persisted store?

In jsdom, `localStorage` exists, so `persist` works. Clear it between tests with `localStorage.clear()` and `persist.clearStorage()`. To test hydration, write data to `localStorage` before calling `persist.rehydrate()`, then check the state.

```ts
localStorage.setItem(
  "settings",
  JSON.stringify({ state: { theme: "dark" }, version: 0 }),
);
await useSettingsStore.persist.rehydrate();
expect(useSettingsStore.getState().theme).toBe("dark");
```

### 219: Should you mock the store itself in component tests?

Usually not. The store is fast and has no side effects, so using the real one makes tests closer to real behavior. Set the state you need with `setState` before rendering. Mock only external things like network calls. Mocking the hook with `vi.mock` is possible but makes tests break when you refactor selectors.

### 220: How do you use Zustand stores in Storybook?

Set the state you need in a decorator or in the story's `beforeEach`/`loaders` before rendering.

```tsx
export const Empty: Story = {
  decorators: [
    (Story) => {
      useCartStore.setState({ items: [] });
      return <Story />;
    },
  ],
};
```

For stores in context, wrap the story in the Provider with the initial values you want.

### 221: How do you migrate from React Context + useReducer to Zustand?

Move the reducer's state into a store, turn each `case` into an action, and replace `useContext(MyContext)` with selector calls. You can keep the reducer and use the `redux` middleware as a first step. Remove the Provider once no component reads the context.

### 222: How do you migrate from Redux to Zustand step by step?

Move one slice at a time. Create a Zustand store for that feature, change its components to use the store, and delete the slice from Redux. Code that ran in thunks becomes async actions. Selectors usually move over almost unchanged. Both libraries can live side by side during the migration.

### 223: What changed between Zustand v4 and v5 that you need to know when upgrading?

- Default exports are gone; use named imports.
- React 18 and TypeScript 4.5 are the minimum.
- `create` no longer takes an equality function; use `useShallow` or `zustand/traditional`.
- Selectors that return a new reference can cause infinite loops.
- `setState(x, true)` requires a full state object in TypeScript.
- `persist` no longer saves state when the store is created.
- UMD/SystemJS and ES5 builds were dropped.
- Deprecated APIs like `zustand/context` were removed.

### 224: What is the recommended way to upgrade an old v3 or v4 project to v5?

Upgrade to the latest v4 first and fix all the deprecation warnings it prints. Then switch to v5 and fix the breaking changes: imports, equality functions, unstable selectors, and the `replace` flag types. Run the app and look for "Maximum update depth exceeded" errors, which point to selectors that return new references.

### 225: How do you handle a dynamic `replace` flag in TypeScript after v5?

`setState` has two overloads, one for `replace?: false` and one for `replace: true`. A plain `boolean` matches neither. The docs suggest casting the arguments to the parameters type.

```ts
const useBearStore = create<{ bears: number }>()(() => ({ bears: 0 }));

const replaceFlag = Math.random() > 0.5;
const args = [{ bears: 5 }, replaceFlag] as Parameters<
  typeof useBearStore.setState
>;
useBearStore.setState(...args);
```

This only type checks when the object is a full state, because one of the overloads needs it.

### 226: What is `UseBoundStore`?

It is the type of the hook returned by `create`: a function you can call with or without a selector, plus all the store methods. You use it when writing helpers that accept a store hook, like `createSelectors`.

### 227: How do you type a hook that uses a vanilla store with an optional selector?

Write overloads, so it returns the whole state without a selector and the selected value with one.

```ts
import { useStore } from "zustand";

export function useBear(): BearState;
export function useBear<T>(selector: (s: BearState) => T): T;
export function useBear<T>(selector?: (s: BearState) => T) {
  return useStore(bearStore, selector!);
}
```

### 228: How do you type `get` and `set` when actions call each other?

The types come from the state interface, so `get()` returns the full state with all actions typed. You only need to make sure the interface includes every action.

```ts
interface CartState {
  items: Item[];
  add: (item: Item) => void;
  addMany: (items: Item[]) => void;
}

const useCartStore = create<CartState>()((set, get) => ({
  items: [],
  add: (item) => set((s) => ({ items: [...s.items, item] })),
  addMany: (items) => items.forEach((item) => get().add(item)),
}));
```

`addMany` here calls `set` once per item. For large lists it is better to do one `set`.

### 229: When is `combine` a good choice for TypeScript users?

When the state is simple and you want types without writing an interface. The state type is inferred from the first argument. It gets awkward when actions need `get()` to return actions too, because inside `combine`, `get` and `set` only know the initial state part. For bigger stores, an explicit interface is clearer.

### 230: How do you type a persisted store when using `partialize`?

The second generic of `persist` is the persisted shape. It is inferred from `partialize`, so usually you don't write it. If you need to, you can pass it.

```ts
const useStore = create<State>()(
  persist(
    (set) => ({
      theme: "light",
      token: null,
      setTheme: (theme) => set({ theme }),
    }),
    {
      name: "app",
      partialize: (s) => ({ theme: s.theme }),
    },
  ),
);
```

`migrate` then must return the persisted shape (`{ theme }`), not the full state.

### 231: How do you avoid persisting secrets like tokens in localStorage?

Exclude them with `partialize`, or keep them in a separate non-persisted store. Better still, keep auth tokens in httpOnly cookies set by the server so JavaScript can't read them at all. Anything in `localStorage` can be read by any script that runs on your page, including injected ones.

### 232: How do you normalize a list of entities in a store?

Store items by id in an object, and keep the order in a separate array.

```ts
interface TodoState {
  byId: Record<string, Todo>
  ids: string[]
  update: (id: string, changes: Partial<Todo>) => void
}

update: (id, changes) =>
  set((s) => ({ byId: { ...s.byId, [id]: { ...s.byId[id], ...changes } } })),
```

Updating one item then doesn't create a new `ids` array, so a list component that selects `ids` won't re-render. Each row selects `s.byId[id]`.

### 233: Why is it good for list rows to select their own item by id?

The parent selects only the list of ids and renders rows. Each row selects its own item. When one item changes, only that row re-renders, not the parent and all the other rows. This makes long lists much faster.

```tsx
function TodoList() {
  const ids = useTodoStore((s) => s.ids);
  return ids.map((id) => <TodoRow key={id} id={id} />);
}

function TodoRow({ id }: { id: string }) {
  const todo = useTodoStore((s) => s.byId[id]);
  return <li>{todo.text}</li>;
}
```

### 234: How do you store pagination state?

Keep the page, page size and totals together, and reset the page when filters change.

```ts
const useListStore = create<ListState>()((set) => ({
  page: 1,
  pageSize: 20,
  filter: "",
  setPage: (page) => set({ page }),
  setFilter: (filter) => set({ filter, page: 1 }),
}));
```

Doing both changes in one `set` keeps them consistent and causes one update.

### 235: How do two stores talk to each other?

One store's action can read or update another store directly through `getState` and `setState`.

```ts
const useCartStore = create<CartState>()((set) => ({
  items: [],
  checkout: async () => {
    const user = useAuthStore.getState().user;
    if (!user) return useModalStore.getState().open("login");
    // ...
  },
}));
```

Keep these links one-directional where you can, so you don't end up with circular imports.

### 236: How do you react in one store when another store changes?

Subscribe to the first store and update the second.

```ts
useAuthStore.subscribe((state, prev) => {
  if (prev.user && !state.user) {
    useCartStore.setState(useCartStore.getInitialState(), true);
  }
});
```

Put this kind of wiring in one place, for example an `initStores.ts` file, so it is easy to find.

### 237: How do you memoize an expensive derived value?

Options, from simplest:

1. Select the raw data and use `useMemo` in the component.
2. Write a memoized selector with a small cache (or a library like `reselect` or `proxy-memoize`) and pass it to the hook.

```ts
import { createSelector } from "reselect";

const selectVisibleTodos = createSelector(
  [(s: TodoState) => s.todos, (s: TodoState) => s.filter],
  (todos, filter) => todos.filter((t) => (filter === "done" ? t.done : true)),
);

const visible = useTodoStore(selectVisibleTodos);
```

A memoized selector returns the same array until its inputs change, so it also avoids the new-reference problem.

### 238: What is a "transient update" in Zustand?

It means reacting to frequent state changes without re-rendering the component. You subscribe in an effect and update a ref or the DOM directly. It is useful for things like mouse positions, scroll, animations or game loops.

```tsx
function Cursor() {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(
    () =>
      useMouseStore.subscribe((s) => {
        if (ref.current)
          ref.current.style.transform = `translate(${s.x}px, ${s.y}px)`;
      }),
    [],
  );
  return <div ref={ref} className="cursor" />;
}
```

### 239: How do you implement undo and redo?

Keep a history of past states in the store, or use the `zundo` middleware, which adds `undo`, `redo` and a history limit to any store.

A small manual version:

```ts
const useEditorStore = create<EditorState>()((set, get) => ({
  text: "",
  past: [],
  future: [],
  setText: (text) =>
    set((s) => ({ past: [...s.past, s.text], text, future: [] })),
  undo: () => {
    const { past, text, future } = get();
    if (!past.length) return;
    set({
      text: past[past.length - 1],
      past: past.slice(0, -1),
      future: [text, ...future],
    });
  },
  redo: () => {
    const { past, text, future } = get();
    if (!future.length) return;
    set({ text: future[0], past: [...past, text], future: future.slice(1) });
  },
}));
```

### 240: How do you split stores for code splitting?

Keep each feature's store in its own file and import it only from that feature's components. When the feature is lazy loaded, its store is in the same chunk and loads with it. A store created with `create` costs nothing until its module is imported.

### 241: Can you add a slice to a store after it was created?

Not cleanly. `create` builds the state once. You can call `setState` to add new keys and functions later, but TypeScript won't know about them and middleware like `persist` won't handle them nicely. If you need lazy features, use a separate store per feature instead.

### 242: How do you handle errors thrown in actions?

Errors in actions are normal JavaScript errors. A sync error is thrown to the caller. An async action returns a rejected promise, which the caller should handle, or you catch it inside the action and store it in an `error` field. Don't let rejected promises go unhandled in event handlers.

### 243: How do you show a global error banner from any action?

Have one error store, and call it from actions or from a fetch helper.

```ts
export const useErrorStore = create<{
  message: string | null;
  show: (m: string) => void;
  clear: () => void;
}>()((set) => ({
  message: null,
  show: (message) => set({ message }),
  clear: () => set({ message: null }),
}));

// anywhere
useErrorStore.getState().show("Could not save");
```

### 244: How do you sync a store with `localStorage` changes from other tabs?

Listen to the `storage` event and rehydrate.

```ts
window.addEventListener("storage", (event) => {
  if (event.key === useSettingsStore.persist.getOptions().name) {
    useSettingsStore.persist.rehydrate();
  }
});
```

The `storage` event only fires in other tabs, not in the tab that made the change, so there is no loop.

### 245: How do you prevent a component from re-rendering when only an unrelated field in an object changes?

Select the specific field, not the parent object. Selecting `s.user` re-renders on any change to the user object. Selecting `s.user.name` re-renders only when the name changes.

```ts
const name = useAuthStore((s) => s.user?.name);
```

### 246: What does `useShallow` compare when the selector returns an array of values?

It compares the arrays item by item with `Object.is`. If the length and every item are the same, it returns the previous array. So `useShallow((s) => [s.a, s.b])` only triggers a re-render when `a` or `b` changes.

### 247: When can `useShallow` still cause re-renders?

When one of the selected values is itself a new object every time, for example `useShallow((s) => ({ user: { ...s.user } }))` or `({ list: s.items.map(...) })`. `useShallow` only compares one level. The nested values must be stable references from the store.

### 248: Can you pass the same selector function to many components?

Yes. Selectors are pure functions, so the same one can be used anywhere. Each component keeps its own subscription and its own last value.

### 249: What is a good file structure for a medium-sized app with Zustand?

One common setup:

```text
src/
  features/
    cart/
      cart.store.ts       // store, actions
      cart.selectors.ts   // exported selectors
      CartPage.tsx
    auth/
      auth.store.ts
  stores/
    ui.store.ts           // app-wide UI state
    reset.ts              // resetAllStores helper
```

Components import selectors and custom hooks, not the raw store, which makes refactoring easier.

### 250: Why is it a good idea to export custom hooks instead of the raw store?

Custom hooks like `useCartCount()` or `useCartActions()` hide the store shape. If you later rename a field, change it to a context store, or split the store, only the hooks change, not every component. It also stops people from calling the hook with no selector.

### 251: How do you persist only part of a store when using the slices pattern?

Use `partialize` on the combined store and pick fields from each slice.

```ts
persist((...a) => ({ ...createCartSlice(...a), ...createUiSlice(...a) }), {
  name: "shop",
  partialize: (s) => ({ items: s.items, currency: s.currency }),
});
```

UI fields like `isMenuOpen` are left out so they reset on every visit.

### 252: How do you exclude a few keys from persistence instead of listing the ones to keep?

Filter the keys in `partialize`.

```ts
partialize: (state) =>
  Object.fromEntries(
    Object.entries(state).filter(([key]) => !['isLoading', 'error'].includes(key)),
  ),
```

### 253: What happens if `localStorage` is not available, for example in private mode or on the server?

`createJSONStorage` catches the error from getting the storage and returns `undefined`. `persist` then works as a normal store and logs a warning when you update it, saying the storage is unavailable. The app doesn't crash, but nothing is saved.

### 254: How do you persist with cookies so the server can read the state?

Write a `StateStorage` that reads and writes `document.cookie` (or use a cookie library). Keep the data small, since cookies are sent with every request and have a size limit of about 4 KB. Mark them carefully, and never use this for secrets that should be httpOnly.

### 255: How do you wait for hydration before rendering an app that uses async storage?

Show a splash screen until `hasHydrated()` is true.

```tsx
export function App() {
  const [ready, setReady] = useState(useAuthStore.persist.hasHydrated());

  useEffect(() => {
    const unsub = useAuthStore.persist.onFinishHydration(() => setReady(true));
    if (useAuthStore.persist.hasHydrated()) setReady(true);
    return unsub;
  }, []);

  if (!ready) return <Splash />;
  return <Routes />;
}
```

This is common in React Native, where AsyncStorage is async.

### 256: How do you store a `_hasHydrated` flag inside the store itself?

Set it from `onRehydrateStorage` and exclude it from persistence.

```ts
const useStore = create<State>()(
  persist(
    (set) => ({
      _hasHydrated: false,
      setHasHydrated: (v: boolean) => set({ _hasHydrated: v }),
      // ...
    }),
    {
      name: "app",
      partialize: ({ _hasHydrated, setHasHydrated, ...rest }) => rest,
      onRehydrateStorage: () => (state) => {
        state?.setHasHydrated(true);
      },
    },
  ),
);
```

Components can then select `s._hasHydrated` like any other value.

### 257: How do you persist two different stores with different storages?

Each store has its own `persist` options, so you can use `localStorage` for one and `sessionStorage` or IndexedDB for another. Just make sure the `name` values are different.

### 258: How can a selector read from two stores?

A single selector can only read one store. Call both hooks and combine in the component, or write a custom hook.

```ts
export function useCanCheckout() {
  const loggedIn = useAuthStore((s) => s.user !== null);
  const hasItems = useCartStore((s) => s.items.length > 0);
  return loggedIn && hasItems;
}
```

### 259: How do you use Zustand with forms built with React Hook Form?

Let React Hook Form manage field values and validation. Use Zustand for things around the form, such as a saved draft or wizard steps. On submit, copy the result into the store.

```tsx
const { register, handleSubmit } = useForm({
  defaultValues: useWizardStore.getState().data,
});
const onSubmit = (values) => {
  useWizardStore.getState().setData(values);
  useWizardStore.getState().next();
};
```

### 260: How do you keep a store in sync with a prop that changes?

Update the store in an effect when the prop changes.

```tsx
function Editor({ documentId }: { documentId: string }) {
  const load = useEditorStore((s) => s.load);
  useEffect(() => {
    load(documentId);
  }, [documentId, load]);
  // ...
}
```

If the store is inside a Provider, you can also give the Provider a `key={documentId}` to create a fresh store each time the id changes.

### 261: How do you reset a context store when a route changes?

Use the route param as the `key` of the Provider. When the key changes, React unmounts the old Provider and mounts a new one, which creates a new store.

```tsx
<EditorStoreProvider key={params.id} documentId={params.id}>
  <Editor />
</EditorStoreProvider>
```

### 262: Can you use Zustand with Preact or other frameworks?

The vanilla store works anywhere. For Preact, `preact/compat` provides `useSyncExternalStore`, so the React bindings work through it. For Vue, Svelte or Angular there are community adapters, or you can subscribe to a vanilla store yourself and push values into the framework's own reactivity.

### 263: How do you use a vanilla store in a non-React part of the app, like a chart library?

Subscribe and call the library's update method.

```ts
const chart = new Chart(canvas, config);

const unsub = statsStore.subscribe((state, prev) => {
  if (state.points !== prev.points) {
    chart.data.datasets[0].data = state.points;
    chart.update();
  }
});
```

### 264: How do you handle a store field that holds a big list from the server?

Store it once and avoid copying it. Select the array itself (stable reference) rather than a filtered copy. If you need filtering, use a memoized selector or `useMemo` in the component. For very large lists, combine this with list virtualization.

### 265: How do you avoid stale state in an async action?

Read the latest state with `get()` after the `await`, not before. Values you read before an `await` may be outdated when the promise resolves.

```ts
save: async () => {
  const draft = get().draft
  await api.save(draft)
  // read again here, the draft may have changed while saving
  if (get().draft === draft) set({ dirty: false })
},
```

### 266: When would you use `set` with `replace: true`?

When you want to remove keys from the state or restore a full snapshot, for example resetting to `getInitialState()` or loading a saved state. Be careful: if your actions live in the state object, replacing it with an object that has no actions deletes them.

### 267: What goes wrong with `set({}, true)`?

It replaces the whole state with an empty object, so every field and action is gone. Components that call `s.increment` will get `undefined`. In v5 TypeScript catches this, because `replace: true` requires a full state.

### 268: How do you make actions available to tests without rendering?

Actions live in the state, so `useStore.getState().someAction()` calls them directly. If actions are outside the store (module functions), import and call them. Both styles are easy to test.

### 269: How do you test a selector?

Selectors are pure functions, so test them with plain objects.

```ts
test("selectTotal", () => {
  const state = {
    items: [
      { price: 2, qty: 3 },
      { price: 5, qty: 1 },
    ],
  } as CartState;
  expect(selectTotal(state)).toBe(11);
});
```

### 270: How do you test `subscribe` logic?

Subscribe with a mock function, change state, and check the calls.

```ts
test("subscribe gets new and old state", () => {
  const listener = vi.fn();
  const unsub = useCounterStore.subscribe(listener);
  useCounterStore.getState().increment();
  expect(listener).toHaveBeenCalledWith(
    expect.objectContaining({ count: 1 }),
    expect.objectContaining({ count: 0 }),
  );
  unsub();
});
```

### 271: How do you write an action that updates several fields at once?

Return all of them from one `set` call. It is one update, so subscribers and components see a consistent state.

```ts
finishOrder: (orderId) =>
  set((s) => ({
    items: [],
    lastOrderId: orderId,
    status: 'done',
  })),
```

### 272: Is it bad to call `set` many times in a row in one action?

It works, but each call notifies all listeners, and in between, other code can see a half-updated state. Prefer one `set` with all changes. Multiple calls are fine in async actions where updates happen at different times (loading, then data).

### 273: How do you add a computed getter to the store?

You can add a function that uses `get()`.

```ts
const useCartStore = create<CartState>()((set, get) => ({
  items: [],
  total: () => get().items.reduce((sum, i) => sum + i.price * i.qty, 0),
}));
```

But a component that selects `s.total` gets the function, not the value, and won't re-render when items change. In components, use a selector like `useCartStore((s) => s.total())` or a separate `selectTotal` function. JavaScript `get total()` getters on the state object are not a good replacement either (see the next question).

### 274: Why don't JavaScript getters work well in Zustand state?

`set` creates the new state with `Object.assign({}, state, partial)`. `Object.assign` reads the getter and copies the value as a normal property, so after the first update the getter is gone and the value is frozen. Use selectors or functions instead.

### 275: How do you share common logic between several stores?

Write a generic slice creator and reuse it.

```ts
interface LoadingSlice {
  loading: boolean;
  error: string | null;
  start: () => void;
  fail: (error: string) => void;
}

export const createLoadingSlice =
  <T extends LoadingSlice>(): StateCreator<T, [], [], LoadingSlice> =>
  (set) => ({
    loading: false,
    error: null,
    start: () => set({ loading: true, error: null } as Partial<T>),
    fail: (error) => set({ loading: false, error } as Partial<T>),
  });

interface UserState extends LoadingSlice {
  user: User | null;
}

const useUserStore = create<UserState>()((...a) => ({
  user: null,
  ...createLoadingSlice<UserState>()(...a),
}));
```

Any store whose state includes `LoadingSlice` can spread it in.

### 276: How do you combine Zustand with Immer without the middleware?

Call `produce` yourself inside `set`.

```ts
import { produce } from 'immer'

toggle: (id) =>
  set(
    produce((state: TodoState) => {
      const todo = state.todos.find((t) => t.id === id)
      if (todo) todo.done = !todo.done
    }),
  ),
```

This works because `produce` with one argument returns a function that takes the state and returns the new state. It is useful when only a few actions need Immer.

### 277: What is the difference between `zustand/react` and `zustand`?

`zustand` re-exports everything from `zustand/vanilla` and `zustand/react`, so it gives you `createStore`, `create` and `useStore` together. `zustand/react` has only the React parts. Most people import from `zustand`; the separate paths exist for clarity and bundle control.

### 278: How do you read the state at the time of a click and also show it?

Select it for display, and inside the click handler use the selected value or `getState()`. Both give the same value at click time. `getState()` is better inside long async handlers because it always returns the latest value.

### 279: How do you build a shopping cart store with quantities?

```ts
interface CartItem {
  id: string;
  name: string;
  price: number;
  qty: number;
}

const useCartStore = create<CartState>()(
  persist(
    (set) => ({
      items: [],
      add: (product) =>
        set((s) => {
          const existing = s.items.find((i) => i.id === product.id);
          if (existing) {
            return {
              items: s.items.map((i) =>
                i.id === product.id ? { ...i, qty: i.qty + 1 } : i,
              ),
            };
          }
          return { items: [...s.items, { ...product, qty: 1 }] };
        }),
      setQty: (id, qty) =>
        set((s) => ({
          items:
            qty <= 0
              ? s.items.filter((i) => i.id !== id)
              : s.items.map((i) => (i.id === id ? { ...i, qty } : i)),
        })),
      clear: () => set({ items: [] }),
    }),
    { name: "cart" },
  ),
);
```

### 280: How do you handle feature flags with Zustand?

Load flags once at startup, put them in a store, and select single flags in components.

```ts
const useFlagStore = create<{ flags: Record<string, boolean> }>()(() => ({
  flags: {},
}));

export async function loadFlags() {
  const flags = await fetch("/api/flags").then((r) => r.json());
  useFlagStore.setState({ flags });
}

export const useFlag = (name: string) =>
  useFlagStore((s) => s.flags[name] ?? false);
```

### 281: How do you handle permissions in the UI with a store?

Keep the user's roles in the auth store and write small hooks for checks.

```ts
export const useCan = (permission: string) =>
  useAuthStore((s) => s.user?.permissions.includes(permission) ?? false);
```

The hook returns a boolean, so components only re-render when the answer changes. Remember that UI checks are only for display; the server must enforce permissions.

### 282: How do you use Zustand for a dark mode that respects the system setting?

Store the user's choice (`'light' | 'dark' | 'system'`), persist it, and compute the actual theme with `matchMedia`.

```ts
const useThemeStore = create<ThemeState>()(
  persist((set) => ({ mode: "system", setMode: (mode) => set({ mode }) }), {
    name: "theme",
  }),
);

useThemeStore.subscribe((s) => applyTheme(s.mode));
applyTheme(useThemeStore.getState().mode);
```

`applyTheme` sets a class on `<html>`. To avoid a flash on load, a small inline script in the HTML head can read `localStorage` before React starts.

### 283: How do you test that a component doesn't re-render too often?

Count renders with a mock or the React Profiler API, change an unrelated field, and assert the count didn't change.

```tsx
const renders = vi.fn();
function Name() {
  renders();
  return <span>{useUserStore((s) => s.name)}</span>;
}

render(<Name />);
act(() => useUserStore.setState({ age: 30 }));
expect(renders).toHaveBeenCalledTimes(1);
```

### 284: Why might a component re-render even though its selected value didn't change?

Its parent re-rendered. Zustand only controls re-renders caused by the store. If the parent renders for another reason, the child renders too unless it is wrapped in `memo` (or the React Compiler handles it). Check the Profiler to see why a component rendered.

### 285: How do you write a store for a multi-step async flow, like upload then process?

Model the steps as a status field and move through them in one action.

```ts
type Status = 'idle' | 'uploading' | 'processing' | 'done' | 'error'

start: async (file: File) => {
  set({ status: 'uploading', progress: 0 })
  try {
    const { id } = await upload(file, (p) => set({ progress: p }))
    set({ status: 'processing' })
    await waitForProcessing(id)
    set({ status: 'done' })
  } catch (e) {
    set({ status: 'error', error: String(e) })
  }
},
```

A single status field is easier to reason about than several booleans like `isUploading` and `isProcessing`.

### 286: How do you handle very frequent updates like a progress bar or drag position?

Updating the store 60 times a second is fine for Zustand itself, but every subscribed component re-renders. Keep the number of subscribers small, select narrow values, or use transient updates through `subscribe` and refs. You can also throttle the updates with `requestAnimationFrame`.

### 287: How do you persist a store and also version it from the start?

Set `version: 0` (the default) or `1` from the first release and add a `migrate` function only when you change the shape. Starting with an explicit version makes it obvious to the next developer that migrations exist.

### 288: How do you write a migration that handles several old versions?

Apply the steps in order.

```ts
migrate: (persisted: any, version) => {
  if (version < 1) {
    persisted.language = persisted.lang ?? 'en'
    delete persisted.lang
  }
  if (version < 2) {
    persisted.notifications = { email: true, push: false }
  }
  return persisted
},
version: 2,
```

A user who skipped version 1 still gets both changes.

### 289: What is a good way to name actions for devtools in a large store?

Use a `feature/action` pattern, like `cart/add` or `auth/logout`. Some teams wrap `set` in a helper that adds the prefix automatically, so they don't repeat the slice name in every action.

```ts
const createCartSlice: StateCreator<
  Store,
  [["zustand/devtools", never]],
  [],
  CartSlice
> = (set) => ({
  items: [],
  add: (item) =>
    set((s) => ({ items: [...s.items, item] }), undefined, "cart/add"),
});
```

### 290: How do you keep Zustand and the URL in sync both ways?

Read the URL into the store on load, update the URL when the store changes, and listen to `popstate` for back/forward navigation. Guard against loops by only writing when the value is actually different.

```ts
useFilterStore.subscribe((s, prev) => {
  if (s.query === prev.query) return;
  const url = new URL(location.href);
  url.searchParams.set("q", s.query);
  history.replaceState(null, "", url);
});

window.addEventListener("popstate", () => {
  const q = new URL(location.href).searchParams.get("q") ?? "";
  if (q !== useFilterStore.getState().query)
    useFilterStore.setState({ query: q });
});
```

With a router, use the router's search params API instead of `history` directly.

### 291: Is it okay to call a store action in `useEffect` on mount to load data?

Yes, that is a common pattern for client-only data. Make sure the action handles being called twice, because Strict Mode in development runs effects twice. Using an AbortController or a "loading already" check prevents double requests.

### 292: How do you prevent duplicate fetches when several components call the same load action?

Keep the in-flight promise and return it if a request is already running.

```ts
let inflight: Promise<void> | null = null

loadUser: () => {
  if (get().user) return Promise.resolve()
  if (!inflight) {
    inflight = fetch('/api/me')
      .then((r) => r.json())
      .then((user) => set({ user }))
      .finally(() => {
        inflight = null
      })
  }
  return inflight
},
```

If you need this a lot, it is a sign that TanStack Query or a similar tool would fit better.

### 293: How do you split one large store into slices without breaking components?

Keep the same hook and the same field names, and move the code into slice files that are spread into the same `create` call. Components don't notice, since the final state shape is unchanged. Then you can refactor slices one at a time.

### 294: How do you use Zustand with Suspense?

Zustand doesn't suspend by itself. If you want Suspense, store a promise and read it with React's `use` hook, or let a data library handle it. Most apps keep loading flags in the store and show spinners instead.

```tsx
const promise = useDataStore((s) => s.promise);
const data = use(promise);
```

The promise must be created once and kept in the store; creating it during render would cause an endless loop.

### 295: How do you store a selection of items, like checked rows in a table?

Use a `Record<string, true>` or a `Set`. A record is simpler to persist and to select from.

```ts
const useSelectionStore = create<{
  selected: Record<string, true>;
  toggle: (id: string) => void;
}>()((set) => ({
  selected: {},
  toggle: (id) =>
    set((s) => {
      const next = { ...s.selected };
      if (next[id]) delete next[id];
      else next[id] = true;
      return { selected: next };
    }),
}));

const isSelected = useSelectionStore((s) => !!s.selected[rowId]);
```

Each row selects a boolean, so toggling one row re-renders only that row (and anything that reads the whole selection).

### 296: How do you add a "dirty" flag to know if a form has unsaved changes?

Compare the current values with the saved ones in a selector.

```ts
const isDirty = useFormStore(
  (s) => JSON.stringify(s.values) !== JSON.stringify(s.saved),
);
```

For bigger forms, keep a `dirty` boolean that each `setField` sets to `true` and `save` sets to `false`, so you don't stringify on every change.

### 297: How do you warn the user before leaving with unsaved changes?

Subscribe to the dirty flag and add or remove a `beforeunload` listener.

```ts
const handler = (e: BeforeUnloadEvent) => e.preventDefault();

useFormStore.subscribe((s, prev) => {
  if (s.dirty === prev.dirty) return;
  if (s.dirty) window.addEventListener("beforeunload", handler);
  else window.removeEventListener("beforeunload", handler);
});
```

### 298: What are some useful third-party libraries around Zustand?

The docs list many. A few that come up often: `zundo` (undo/redo middleware), `react-native-mmkv` wrapped in a custom `StateStorage` for fast persistence in React Native, and libraries that sync stores across tabs. Check the "Third-party libraries" page in the docs, and check that a package supports v5 before using it.

### 299: How do you make a store that is created lazily on first use?

Wrap the creation in a function that caches the result.

```ts
let store: ReturnType<typeof createHeavyStore> | undefined;

export const getHeavyStore = () => (store ??= createHeavyStore());
export const useHeavy = <T>(selector: (s: HeavyState) => T) =>
  useStore(getHeavyStore(), selector);
```

Usually this isn't needed, because a module is only evaluated when it is first imported.

### 300: What are the most common Zustand mistakes you have seen in code reviews?

- Calling the hook without a selector and re-rendering on every change.
- Selectors returning new objects or arrays without `useShallow`.
- Mutating state (pushing to an array, changing a nested field) instead of copying.
- Forgetting that the merge is shallow and losing nested fields.
- Module-level stores holding user data in server rendering.
- Persisting functions, secrets or UI-only flags.
- Putting server data in a store and building a cache by hand.

## Advanced Questions (301-450)

### 301: How does `createStore` work internally?

It is a short closure. It keeps `state` and a `Set` of listeners in local variables, and builds an `api` object with `setState`, `getState`, `getInitialState` and `subscribe`. Then it calls your store creator with `(setState, getState, api)` and saves the result as both the current and the initial state.

```js
const createStoreImpl = (createState) => {
  let state;
  const listeners = new Set();
  const setState = (partial, replace) => {
    const nextState = typeof partial === "function" ? partial(state) : partial;
    if (!Object.is(nextState, state)) {
      const previousState = state;
      state =
        (replace ?? (typeof nextState !== "object" || nextState === null))
          ? nextState
          : Object.assign({}, state, nextState);
      listeners.forEach((listener) => listener(state, previousState));
    }
  };
  const getState = () => state;
  const getInitialState = () => initialState;
  const subscribe = (listener) => {
    listeners.add(listener);
    return () => listeners.delete(listener);
  };
  const api = { setState, getState, getInitialState, subscribe };
  const initialState = (state = createState(setState, getState, api));
  return api;
};
```

There is no scheduler, no queue and no batching inside the store. Everything happens synchronously.

### 302: When does `setState` skip notifying listeners?

Only when the value you pass (or the value your function returns) is the same reference as the current state, checked with `Object.is`. A partial object like `{ count: 1 }` is always a new object, so it always produces a new merged state and always notifies listeners, even if `count` was already `1`. Skipping re-renders is then the job of the selectors.

### 303: What happens if you call `setState` with a primitive or `null`?

The merge only happens when the next state is a non-null object. For a primitive or `null`, the state is replaced with that value. So a store can technically hold a number as its whole state, but then every selector and action must handle that, and middleware like `persist` expects an object. In practice, always use an object.

### 304: Are listeners called synchronously?

Yes. `setState` calls every listener in a loop before it returns. That means a `subscribe` callback runs inside the `set` call, and code after `set` sees the listeners already done. React re-renders are scheduled by React itself, so components don't render inside that loop.

### 305: What happens if a listener calls `setState` again?

The inner `setState` runs right away, updates the state and calls all listeners with the newer state, then the outer loop continues. The remaining listeners from the first round then get called with the newest `state` value, but with the `previousState` from the first update. This can cause confusing behavior and even infinite loops if listeners keep setting state. Avoid setting state from listeners unless you guard it carefully.

### 306: What happens if a listener unsubscribes another listener while the store is notifying?

Listeners are kept in a `Set` and called with `forEach`. If a listener is removed during iteration before it is visited, it won't be called. A listener added during iteration will be visited in that same loop. This follows normal `Set` iteration rules, so be careful when subscribing or unsubscribing inside listeners.

### 307: How does `useStore` connect to React?

It calls React's `useSyncExternalStore`:

```js
function useStore(api, selector = identity) {
  const slice = React.useSyncExternalStore(
    api.subscribe,
    React.useCallback(() => selector(api.getState()), [api, selector]),
    () => selector(api.getInitialState()),
  );
  React.useDebugValue(slice);
  return slice;
}
```

`subscribe` tells React when to check again, the second function returns the selected value (the snapshot), and the third is used for server rendering and hydration.

### 308: Why does Zustand use `getInitialState` for the server snapshot?

During server rendering and hydration, React calls the third function (`getServerSnapshot`). Using the initial state means the server output and the first client render use the same data, as long as nothing changed the store before hydration. If you change the store on the client before hydration finishes (for example with `persist` reading `localStorage`), you can get mismatches.

### 309: Why is the selector wrapped in `useCallback` inside `useStore`?

`useSyncExternalStore` calls the snapshot function on every render and whenever the store notifies. Wrapping the selector in `useCallback` with `[api, selector]` keeps the same snapshot function when the selector reference doesn't change. If you pass an inline selector, it changes every render, which is fine; React just calls the new function.

### 310: Why does an unstable selector result cause "Maximum update depth exceeded" with `useSyncExternalStore`?

React calls the snapshot function and compares the result with the previous result using `Object.is`. If the result is always a new object, React thinks the store changed during render and schedules another render. In development it also checks that calling the snapshot twice gives the same value, and warns "The result of getSnapshot should be cached". The loop never settles, so React stops with the error.

### 311: How does `useShallow` work internally?

It keeps the previous result in a `useRef`. Each time the wrapped selector runs, it compares the new result with the stored one using `shallow`. If they are shallowly equal, it returns the old reference; otherwise it saves and returns the new one.

```js
function useShallow(selector) {
  const prev = React.useRef(undefined);
  return (state) => {
    const next = selector(state);
    return shallow(prev.current, next) ? prev.current : (prev.current = next);
  };
}
```

Because it returns a stable reference for equal values, `useSyncExternalStore` sees no change.

### 312: How does `zustand/traditional` support equality functions?

It uses `useSyncExternalStoreWithSelector` from the `use-sync-external-store/shim/with-selector` package. That hook keeps the previous selection and only returns a new value when your `equalityFn` says it changed. This is why `use-sync-external-store` is a peer dependency for that entry point.

### 313: How does the `shallow` function compare Maps, Sets, arrays and plain objects?

It first checks `Object.is`. Then both values must be non-null objects with the same prototype. If they are iterables that have an `entries()` method (Maps, Sets and arrays all do), it builds a Map from the entries of each and compares the key/value pairs. Iterables without `entries()` are compared item by item in order. Plain objects are compared through `Object.entries`. Values are always compared with `Object.is`, never deeply.

### 314: Does `shallow` treat two Sets with the same items in different order as equal?

Yes. A Set's `entries()` gives `[value, value]` pairs, so `shallow` compares Sets the same way as Maps: by key, not by position. `shallow(new Set([1, 2]), new Set([2, 1]))` returns `true`. Arrays are different, because their entries are `[index, value]`, so `[1, 2]` and `[2, 1]` are not equal.

### 315: What does `useDebugValue` do in `useStore`?

It shows the selected value next to the hook in React DevTools' component inspector. It has no effect in production and doesn't change behavior. It just makes it easier to see what a component selected from the store.

### 316: What is the cost of having many components subscribed to one store?

Every `setState` calls every listener. For each subscribed component, React calls its selector and compares the result. With thousands of subscribers and frequent updates, this adds up even if few components re-render. Keep selectors cheap, avoid expensive work like sorting inside selectors, and split very busy state into its own store so unrelated subscribers are not checked.

### 317: How would you scale a store that updates many times per second with thousands of subscribers?

- Split the hot state into a separate store, so only its subscribers are checked.
- Use transient updates (subscribe + refs) for high-frequency visual updates.
- Make selectors O(1), for example `s.byId[id]`, not `s.items.find(...)`.
- Batch incoming updates (for example, collect websocket messages and apply them once per animation frame).
- Use list virtualization so only visible rows are subscribed.

### 318: How would you batch many incoming updates into one `set`?

Collect them in a buffer and flush on the next animation frame.

```ts
let buffer: Record<string, number> = {};
let scheduled = false;

export function onPrice(symbol: string, price: number) {
  buffer[symbol] = price;
  if (scheduled) return;
  scheduled = true;
  requestAnimationFrame(() => {
    const updates = buffer;
    buffer = {};
    scheduled = false;
    usePriceStore.setState((s) => ({ prices: { ...s.prices, ...updates } }));
  });
}
```

One `set` per frame means one round of selector checks, no matter how many messages arrived.

### 319: How do React transitions work with Zustand updates?

Updates from external stores read through `useSyncExternalStore` can't be rendered as non-blocking transitions. If you call `set` inside `startTransition`, React still renders the change synchronously (it will not show the old UI while preparing the new one). If you need transition behavior, keep that piece of state in `useState` or `useReducer`, or put the slow part behind `useDeferredValue`.

### 320: How can `useDeferredValue` help with a slow component that reads from Zustand?

Select the value as usual, then pass it through `useDeferredValue` before giving it to the slow part. React renders the fast parts with the new value first and renders the slow part in the background.

```tsx
const query = useSearchStore((s) => s.query);
const deferredQuery = useDeferredValue(query);
return <SlowResults query={deferredQuery} />;
```

`SlowResults` should be memoized so it only re-renders when `deferredQuery` changes.

### 321: Does Zustand work with the React Compiler?

Yes. The compiler memoizes components and hooks, and Zustand hooks are normal hooks that follow the rules. The compiler can even make inline selectors stable. It doesn't change how store subscriptions work. What it can't fix is a selector that returns a new object each time from store data; you still need `useShallow` or stable selectors for that.

### 322: What is the `StoreMutators` interface used for?

It is a type registry. Each middleware adds an entry to `StoreMutators` through module augmentation, describing how it changes the store type. For example, `persist` registers `'zustand/persist'` and adds the `persist` API. The `Mutate` type then applies these changes in order to get the final store type.

### 323: How do you write a typed custom middleware that adds a method to the store?

Declare a mutator with module augmentation and type the middleware with the mutator lists.

```ts
import type { StateCreator, StoreMutatorIdentifier } from "zustand";

type WithReset<S> = S & { reset: () => void };

declare module "zustand/vanilla" {
  interface StoreMutators<S, A> {
    "myapp/reset": WithReset<S>;
  }
}

type Resettable = <
  T,
  Mps extends [StoreMutatorIdentifier, unknown][] = [],
  Mcs extends [StoreMutatorIdentifier, unknown][] = [],
>(
  initializer: StateCreator<T, [...Mps, ["myapp/reset", never]], Mcs>,
) => StateCreator<T, Mps, [["myapp/reset", never], ...Mcs]>;

type ResettableImpl = <T>(
  initializer: StateCreator<T, [], []>,
) => StateCreator<T, [], []>;

const resettableImpl: ResettableImpl = (initializer) => (set, get, store) => {
  const initial = initializer(set, get, store);
  (store as WithReset<typeof store>).reset = () =>
    store.setState(initial, true);
  return initial;
};

export const resettable = resettableImpl as unknown as Resettable;
```

Now `useStore.reset()` is typed after `create<State>()(resettable(...))`. The cast at the end is the same trick the built-in middleware use.

### 324: Why do built-in middleware implementations use a cast to a more complex type?

The public type has to track the mutator lists so that `set`, `get` and the store are typed correctly inside and outside. Writing the implementation against those complex generics is very hard. So the code is written against a simple signature and cast to the public type. The docs for advanced TypeScript use the same pattern for custom middleware.

### 325: How does `Mutate<S, Ms>` work?

It is a recursive type. It takes a store type `S` and a list of `[identifier, argument]` pairs, looks up each identifier in `StoreMutators`, applies it to the store, and continues with the rest of the list. The result is the store type with every middleware's additions, in the right order.

### 326: Why do you need `create<T>()(...)` but not `create(...)` in plain JavaScript?

In TypeScript, `T` (the state type) is invariant: it appears both as input (in `set`) and output (returned state). TypeScript can't infer it well from the creator function, especially with middleware. Passing `T` explicitly and letting the middleware generics be inferred needs the curried form. JavaScript has no types, so the extra call is not needed (but it still works, since `create()` with no argument returns the same function).

### 327: What does `create()` with no arguments return at runtime?

It returns `createImpl`, the function that takes a store creator. That's how the curried TypeScript form works: `create<T>()` gives back a function, and calling it with your creator builds the store. Same for `createStore()`.

### 328: How does the `persist` middleware hook into `setState`?

It wraps both the `set` passed to your creator and `api.setState`. After each call, it runs `partialize` on the current state and writes `{ state, version }` to storage under `name`. With an async storage, `setItem` returns a promise, and `set` returns it too, but nothing waits for it.

### 329: When does `persist` hydrate, and is it sync or async?

It hydrates once during store creation unless `skipHydration` is set. Internally it wraps the storage call so that a sync storage resolves right away, and an async one resolves later. With `localStorage`, the store has the saved data before `create` returns, so the first render already shows it. With async storage, the first render uses defaults and the store updates when the promise resolves.

### 330: What does `persist` do if `rehydrate` is called twice quickly?

It keeps a hydration counter. Each call increments it, and when a promise resolves it checks whether it is still the latest hydration. Older ones are ignored, so a slow first read can't overwrite a newer second read. `clearStorage` also bumps the counter to cancel a hydration in progress.

### 331: How does `persist` change `getInitialState`?

It replaces `api.getInitialState` with a function that returns the state from your creator (before hydration). So `getInitialState()` gives the defaults, not the values loaded from storage. That makes resets go back to defaults, and it also means server snapshots use defaults.

### 332: In what order do `migrate` and `merge` run during hydration?

First the stored value is read. If its version is different from the current `version`, `migrate` runs and returns the migrated state. Then `merge(persistedOrMigratedState, currentState)` combines it with the current state, and the result replaces the store state. If a migration ran, the new state is written back to storage. Finally, the `onRehydrateStorage` callback and `onFinishHydration` listeners run.

### 333: What happens if hydration fails because the stored JSON is broken?

`JSON.parse` throws, the hydration promise rejects, and `persist` calls the post-rehydration callback from `onRehydrateStorage` with `(undefined, error)`. The store keeps its default state. `hasHydrated()` stays `false` in that case, so a UI that waits for hydration would wait forever. Handle the error in `onRehydrateStorage` and set your own flag or clear the broken storage.

### 334: Can `merge` be used to protect against tampered persisted data?

Yes, and it is a good idea for important fields. Data in `localStorage` can be edited by the user or by malicious scripts. In `merge` you can validate the persisted value (for example with Zod) and fall back to the current state when it is invalid.

```ts
merge: (persisted, current) => {
  const parsed = SettingsSchema.safeParse(persisted)
  return parsed.success ? { ...current, ...parsed.data } : current
},
```

### 335: Why can't you trust persisted state for security decisions?

It lives on the client, so the user can change it any time. A persisted `isAdmin: true` or a fake token is easy to create in DevTools. Use persisted state only for convenience (UI preferences, drafts). Any security decision must be checked on the server.

### 336: What are the security risks of persisting state in `localStorage`?

Any script running on your origin can read and change it, so an XSS bug can steal tokens or personal data stored there. Data also stays after logout unless you clear it, and it is shared by all tabs and users of that browser profile. Keep sensitive data out of persisted stores, clear storage on logout, and use a strict Content Security Policy.

### 337: Can a malicious persisted value cause prototype pollution through the default merge?

The default merge is `{ ...currentState, ...persistedState }`. Object spread defines own properties, and `JSON.parse` creates `__proto__` as an own property, not a prototype change, so the default merge doesn't pollute `Object.prototype`. A hand-written deep merge that walks keys and assigns with `target[key] = ...` can be vulnerable. If you write a deep merge, skip `__proto__`, `constructor` and `prototype` keys or use a safe library.

### 338: How does the devtools middleware record actions?

It replaces `api.setState` with a function that calls the real `set`, then sends `{ type }` and the new state to the extension through a connection. The type is the third argument to `set`, or `anonymousActionType`, or the caller function name found from the stack trace, or `"anonymous"`. When the extension sends a "jump" message, it sets state with recording turned off so the jump doesn't appear as a new action.

### 339: Why can the devtools action name sometimes show the wrong function or "anonymous"?

When no name is given, the middleware creates an `Error` and parses its stack to find the function that called `setState`. Minified code, different browsers, arrow functions and wrapper functions all change the stack, so the name can be missing or misleading. Passing an explicit name is the reliable way.

### 340: What is the cost of the devtools middleware in production?

If it is disabled, it returns the original creator and adds almost nothing. If it is enabled and the extension is installed, every update serializes the state for the extension, which can be slow for big states, and it exposes your state to anyone who opens DevTools. Keep it disabled in production.

### 341: How does the immer middleware work internally?

It replaces `store.setState` with a function that checks whether the updater is a function. If it is, it wraps it with Immer's `produce`, so the function receives a draft and returns a new immutable state. Then it calls the original `set`. Plain objects go through unchanged.

```js
const immerImpl = (initializer) => (set, get, store) => {
  store.setState = (updater, replace, ...args) => {
    const nextState =
      typeof updater === "function" ? produce(updater) : updater;
    return set(nextState, replace, ...args);
  };
  return initializer(store.setState, get, store);
};
```

### 342: Why does Immer make structural sharing important for Zustand selectors?

Immer only creates new objects for the parts of the tree you changed and reuses everything else. That means selectors for untouched parts still return the same references, so `Object.is` says they are equal and those components don't re-render. Manual spreading does the same if done correctly, but it is easy to spread too much and create new references for unchanged data.

### 343: How does `subscribeWithSelector` work internally?

It replaces `api.subscribe`. When called with a selector and a listener, it runs the selector once to store the current slice, then subscribes a wrapper that runs the selector on every change and calls your listener only when `equalityFn` says the slice changed. Called with one argument, it behaves like the normal `subscribe`.

### 344: What does `combine` do at runtime?

Almost nothing. It returns a creator that calls your actions function and merges the result into a copy of the initial state with `Object.assign`. All its value is in the types: it infers the state from the initial object so you don't write an interface.

### 345: What is `unstable_ssrSafe` in `zustand/middleware`?

It is an experimental middleware. When it detects server rendering (by default, `typeof window === 'undefined'`), it replaces `set` and `api.setState` with a function that throws "Cannot set state of Zustand store in SSR". The goal is to catch code that writes to a shared module-level store on the server, which could leak data between requests. Being `unstable_`, its API may change.

### 346: Why is a global store dangerous on a Node.js server?

Node loads each module once per process and reuses it for every request. A store created at module level is one object for all users. If request A writes user data and request B renders before it is reset, B sees A's data. This is both a bug and a privacy issue. Per-request stores avoid it.

### 347: Is reading a global store on the server safe?

Reading default values is safe as long as nothing on the server writes to the store. Problems only start when server code writes request-specific data. A good rule is: on the server, global stores are read-only defaults, and request data goes into per-request stores or props.

### 348: How do you make sure the same store instance is used on server render and hydration in a context-based setup?

You can't share the exact instance across the network. Instead, you create the store on the server with some initial data, render, and pass the same initial data to the client (as props from a server component, or serialized in the page). The client Provider creates its own store from that data. As long as both sides start from the same data, the output matches.

### 349: Why might you get a hydration error even with a per-request store?

If the client changes the store before hydration finishes. Common causes: `persist` reading `localStorage`, code at module level that calls `setState` in the browser (for example reading `window.innerWidth`), or `Date.now()`/random values in the initial state. Move these changes into effects that run after hydration.

### 350: How do you avoid duplicate Zustand copies in a monorepo or micro-frontend setup?

If two copies of `zustand` are bundled, that's mostly fine, since stores are just objects. But if apps need to share one store, they must import the same module instance. Use module federation `shared` with `singleton: true` for the module that defines the store, or expose the store on a shared host module. Make sure React is a singleton too, because `useSyncExternalStore` must come from the same React as the renderer.

### 351: Can a Zustand store be used inside a Web Worker?

Yes, the vanilla store has no DOM or React dependency. But a store in a worker and a store in the main thread are separate objects; they don't share memory. To sync them, send messages with `postMessage` and apply them with `setState` on the other side. Only send serializable data (no functions).

```ts
// worker.ts
const store = createStore(() => ({ result: null as number | null }));
store.subscribe((s) => postMessage({ type: "state", state: s }));

// main.ts
worker.onmessage = (e) => {
  if (e.data.type === "state") useResultStore.setState(e.data.state);
};
```

### 352: How would you sync a store across tabs without `localStorage` events?

Use a `BroadcastChannel`. Send changes from one tab and apply them in others, with a flag to avoid echoing them back.

```ts
const channel = new BroadcastChannel("cart");
let fromRemote = false;

useCartStore.subscribe((s, prev) => {
  if (fromRemote || s.items === prev.items) return;
  channel.postMessage({ items: s.items });
});

channel.onmessage = (e) => {
  fromRemote = true;
  useCartStore.setState({ items: e.data.items });
  fromRemote = false;
};
```

This works without persistence and is faster than writing to storage. The `fromRemote` flag works because `setState` and listeners run synchronously.

### 353: How do you keep store state consistent when an async action is canceled halfway?

Make the final state changes happen in one `set` at the end, after all awaits, so a canceled action leaves no partial state. If you must show progress, track it in a separate field and reset that field in a `finally` block. For cancellation, check `signal.aborted` after each `await` and stop before calling `set`.

### 354: Why can a component see a different value from `getState()` than from its hook during render?

The hook returns the snapshot React used for this render. `getState()` returns the latest store state right now. If the store changed after React started rendering, the two can differ. `useSyncExternalStore` will detect the change and re-render, but inside that render you should use the hook value, not `getState()`, to stay consistent.

### 355: What are the trade-offs between a single global store and many small stores?

A single store gives one place for middleware, easy cross-slice actions, and one DevTools view. But every subscriber is checked on every update, and the store file can grow large. Many small stores keep updates isolated (only that store's subscribers are checked), split code naturally and are easier to own per team. The cost is that cross-store logic needs explicit `getState` calls or subscriptions.

### 356: How would you design state management for a large app with several teams?

- Each team owns stores for its feature, in its own folder.
- Each feature exports hooks and actions, not the raw store.
- Shared app-wide state (auth, theme, flags) lives in a small number of core stores owned by a platform team.
- Cross-feature communication goes through actions or events, not direct writes into another team's store.
- Server data goes through a data fetching library.
- Lint rules and code review catch hooks without selectors and mutations.

### 357: How do you prevent other modules from writing to a store directly?

Don't export the store. Export only selector hooks and action functions.

```ts
const useCartStoreBase = create<CartState>()(() => ({ items: [] }));

export const useCartItems = () => useCartStoreBase((s) => s.items);
export const addToCart = (item: Item) =>
  useCartStoreBase.setState((s) => ({ items: [...s.items, item] }));
```

Now the only way to change the cart is through `addToCart`, which keeps all update logic in one file.

### 358: When would you choose Redux Toolkit over Zustand for a new project?

When you want strong conventions for a large team, the Redux DevTools workflow with replay and action logs as a core part of debugging, the listener middleware for complex side effects, or RTK Query fully tied into the same store. When the team already knows Redux well, that also counts. Zustand wins when you want less code, simpler mental model and more freedom.

### 359: When would you choose Jotai over Zustand?

When state is naturally many small independent pieces with dependencies between them, for example a form builder or a spreadsheet where each cell has derived values. Jotai's atoms track dependencies automatically and only recompute what changed. Zustand works better when state is one coherent object with actions that update several fields together.

### 360: When would you choose XState (or another state machine library) over Zustand?

When the logic has many states and transitions that must follow strict rules, such as a checkout flow, a video call, or a multi-step wizard with branches and timeouts. A state machine makes invalid states impossible and is easy to visualize. You can still use Zustand for the surrounding UI state, or store the machine's state in a Zustand store.

### 361: How would you model a finite state machine in a Zustand store without a library?

Use one `status` field and a transition table, and only allow known transitions.

```ts
type Status = "idle" | "loading" | "success" | "error";
type Event = "FETCH" | "RESOLVE" | "REJECT" | "RESET";

const transitions: Record<Status, Partial<Record<Event, Status>>> = {
  idle: { FETCH: "loading" },
  loading: { RESOLVE: "success", REJECT: "error" },
  success: { FETCH: "loading", RESET: "idle" },
  error: { FETCH: "loading", RESET: "idle" },
};

const useMachine = create<{ status: Status; send: (e: Event) => void }>()(
  (set, get) => ({
    status: "idle",
    send: (event) => {
      const next = transitions[get().status][event];
      if (next) set({ status: next });
    },
  }),
);
```

### 362: What happens if two components call the same async action at the same time?

Both calls run independently. Both set `loading: true`, both fetch, and both set the result. The last response wins, which can be the older request. Fix it with a request id check, an AbortController, or by reusing the in-flight promise.

### 363: How do you design a store API so components can't create invalid state?

Expose actions with meaning, not raw setters. Instead of `setStatus` and `setData` that can be called in any order, expose `loadSucceeded(data)` that sets both at once. Use TypeScript discriminated unions so `data` only exists when `status === 'success'`.

```ts
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: User }
  | { status: "error"; error: string };
```

Use `replace: true` when switching between union members so leftover keys don't stay around.

### 364: Why do you need `replace: true` with discriminated union state?

The default merge keeps old keys. If you go from `{ status: 'success', data }` to `{ status: 'loading' }` with a normal merge, `data` stays in the state, so the state no longer matches the union. Replacing makes the state exactly what you set. Keep actions in a separate object or outside the store, or include them in every replacement, otherwise replacing deletes them.

### 365: How would you structure a store that holds both a union state and actions?

Put the union under one key, so actions stay at the top level and the default merge works.

```ts
interface Store {
  request: RequestState;
  load: () => Promise<void>;
}

const useUserStore = create<Store>()((set) => ({
  request: { status: "idle" },
  load: async () => {
    set({ request: { status: "loading" } });
    try {
      set({ request: { status: "success", data: await fetchUser() } });
    } catch (e) {
      set({ request: { status: "error", error: String(e) } });
    }
  },
}));
```

Each `set` replaces `request` completely, so no leftover keys.

### 366: A component re-renders on every keystroke in an unrelated input. How do you find the cause?

Use the React DevTools Profiler to confirm what triggered the render ("Why did this render?"). If it's a hook change, check the component's store hooks: likely a hook without a selector, a selector returning a new object, or selecting a parent object (like `s.form`) that changes on every keystroke. Fix the selector to pick only the needed field or use `useShallow`.

### 367: After upgrading to v5, the app crashes with "Maximum update depth exceeded". How do you fix it?

Search for selectors that create new references: `({ ... })`, `[ ... ]`, `.map`, `.filter`, `?? []`, `?? {}`, `Object.keys`. Wrap the ones that return objects or arrays with `useShallow`, move fallbacks to constants, and move expensive derived arrays to `useMemo` or memoized selectors. As a quick fix, you can switch to `createWithEqualityFn` from `zustand/traditional`, but fixing selectors is better.

### 368: Users report that their saved settings disappear after a deploy. What could be wrong?

Possible causes:

- The `version` was changed but there is no `migrate`, so stored data is ignored.
- The `name` (storage key) changed.
- A shallow default `merge` dropped nested fields, or a new nested default replaced saved data the wrong way around.
- `partialize` stopped including a field.
- The app moved to a new domain or subdomain, so `localStorage` is different.

Check the stored JSON in the browser and the `persist` options in the diff.

### 369: The persisted store shows old values for a moment after a page load in React Native. Why?

AsyncStorage is async, so the first render uses defaults and the store updates after hydration finishes. Show a splash screen until `persist.hasHydrated()` is true, or render only the parts that don't depend on persisted values. You can also use a sync storage like MMKV, which hydrates during store creation.

### 370: A test passes alone but fails when run with others. What is a likely Zustand cause?

Stores are module-level singletons, so state from an earlier test leaks into the next one. Add a reset in `afterEach` (with `getInitialState()` and `replace: true`), use the shared `__mocks__/zustand` reset pattern, or use per-test stores via context. Also clear `localStorage` if stores are persisted.

### 371: You see private data from another user in a server-rendered page. How would you investigate?

Look for module-level Zustand stores that are written during server rendering, for example in a server component, a layout, a `getServerSideProps`-style function or middleware. Any write to a shared store on the server is a leak. Move that state into a per-request store created in a Provider, or pass the data as props. `unstable_ssrSafe` can help find writes on the server.

### 372: How do you design a store for a collaborative editor with remote updates?

Keep the document in a structure that supports fine-grained updates (by id), apply remote patches in batches, and keep local and remote changes separate when conflicts are possible. Often the real source of truth is a CRDT library like Yjs, and the Zustand store only mirrors what the UI needs, updated from the CRDT's change events. Use transient updates for cursors and presence, since they change very often.

### 373: How would you implement middleware that validates every state update in development?

Wrap `set` and `api.setState`, run the update, then validate the new state with a schema and throw or log if it fails.

```ts
const validate =
  <T>(schema: { parse: (v: unknown) => T }) =>
  (config: StateCreator<T>): StateCreator<T> =>
  (set, get, api) => {
    const checkedSet = ((...args: Parameters<typeof set>) => {
      set(...args);
      if (process.env.NODE_ENV !== "production") schema.parse(get());
    }) as typeof set;
    api.setState = checkedSet;
    return config(checkedSet, get, api);
  };
```

Validating on every update can be slow, so keep it for development.

### 374: How would you implement a simple time-travel debugger for one store?

Subscribe and save snapshots, then restore one with `replace: true`.

```ts
const history: State[] = [useStore.getState()];
let restoring = false;

useStore.subscribe((s) => {
  if (!restoring) history.push(s);
});

export function goTo(index: number) {
  restoring = true;
  useStore.setState(history[index], true);
  restoring = false;
}
```

Because updates are immutable, each snapshot is cheap: unchanged parts share references.

### 375: Why is immutability what makes cheap snapshots possible?

Each update creates a new top-level object but reuses every unchanged nested object. Keeping 100 snapshots doesn't mean 100 full copies; most of the data is shared. If you mutated in place, all snapshots would point to the same changed objects and history would be useless.

### 376: How would you implement a "lazy" store that loads its initial data on first subscription?

Track the number of subscribers by wrapping `subscribe`.

```ts
const store = createStore<State>()(() => ({ data: null, loading: false }));
const originalSubscribe = store.subscribe;
let count = 0;

store.subscribe = (listener) => {
  if (count++ === 0 && !store.getState().data) {
    store.setState({ loading: true });
    fetchData().then((data) => store.setState({ data, loading: false }));
  }
  const unsub = originalSubscribe(listener);
  return () => {
    count--;
    unsub();
  };
};
```

This is similar to how some data libraries start fetching only when someone is listening.

### 377: What can go wrong if you replace `api.subscribe` in a middleware?

Other middleware may also replace it (like `subscribeWithSelector`), and the order decides which version is used. Also, React passes its own callback to `subscribe` and expects an unsubscribe function back. If your version forgets to return it, or calls listeners when nothing changed, components leak subscriptions or render for no reason. Keep the same contract as the original.

### 378: How does React handle the `subscribe` function changing between renders?

If `subscribe` is a different function, `useSyncExternalStore` unsubscribes and subscribes again. In Zustand, `api.subscribe` is the same function for the life of the store, so this only happens if you pass a different store to `useStore`, for example after a Provider created a new store.

### 379: What happens to subscriptions when a Provider replaces its store?

Components using `useStore(store, selector)` get a new `store` from context. React sees the new `subscribe` and snapshot functions, unsubscribes from the old store, and subscribes to the new one. The old store is garbage collected once nothing references it. If something outside React still subscribes to the old store, it keeps it alive.

### 380: How can a Zustand store cause a memory leak?

- Subscriptions created outside React that are never unsubscribed.
- Per-component stores that are subscribed to by long-lived code.
- Growing lists (logs, history, cache maps) that are never trimmed.
- Devtools connections from many short-lived stores without `devtools.cleanup()`.
- Closures in actions that hold large objects.

Clean up subscriptions and cap the size of any history you keep.

### 381: How would you implement an LRU-style cache inside a store?

Keep a Map and an order array, and drop the oldest entries when you go over the limit.

```ts
const MAX = 50

put: (key, value) =>
  set((s) => {
    const order = [key, ...s.order.filter((k) => k !== key)].slice(0, MAX)
    const entries = Object.fromEntries(order.map((k) => [k, k === key ? value : s.entries[k]]))
    return { order, entries }
  }),
```

For server data, a data fetching library with built-in cache eviction is usually a better choice.

### 382: What are the pros and cons of putting actions inside vs outside the store?

Inside: grouped with state, `set` and `get` are available, works naturally with middleware, slices and devtools action names. Outside: no need to select them, tree-shakable, callable from anywhere without a hook, and the state object stays pure data (easier to persist and replace). Inside is the more common style; outside fits well for big apps that want a strict boundary.

### 383: How would you share a store between a React app and a vanilla JavaScript widget on the same page?

Create a vanilla store in a shared module. The React app reads it with `useStore(store, selector)`, and the widget uses `store.subscribe` and `store.getState()`. Both see the same state because they reference the same object. If they are separate bundles, expose the store on `window` or through a shared module so both use the same instance.

### 384: How would you design a plugin system where plugins add state to a store?

Give each plugin its own store and register it in a central registry, instead of injecting keys into one store. The host can then read plugin stores by id.

```ts
const registry = new Map<string, StoreApi<unknown>>();

export function registerPluginStore<T>(id: string, creator: StateCreator<T>) {
  const store = createStore<T>()(creator);
  registry.set(id, store as StoreApi<unknown>);
  return store;
}
```

Each plugin owns its types, and unloading a plugin is just removing its store.

### 385: Why is it hard to code-split slices of a single store?

`create` calls the creator once and builds the full state. Slices that are not loaded yet can't be part of that call. Adding them later with `setState` works at runtime but breaks the typing (the store type is fixed) and middleware like `persist`, which may already have hydrated without them. Separate stores per lazy feature avoid all of this.

### 386: How would you handle errors from `persist` when storage quota is exceeded?

`localStorage.setItem` throws `QuotaExceededError`. Since `persist` calls it inside `set`, the error is thrown from your action. Wrap your storage in a custom `StateStorage` that catches the error, logs it, and maybe clears old data, so the app keeps working.

```ts
const safeLocalStorage: StateStorage = {
  getItem: (k) => localStorage.getItem(k),
  setItem: (k, v) => {
    try {
      localStorage.setItem(k, v);
    } catch (e) {
      console.warn("persist failed", e);
    }
  },
  removeItem: (k) => localStorage.removeItem(k),
};
```

### 387: How do you limit how often `persist` writes to storage?

Write a storage wrapper that debounces `setItem`.

```ts
const debounced = (storage: StateStorage, ms = 500): StateStorage => {
  let timer: ReturnType<typeof setTimeout> | undefined;
  return {
    getItem: storage.getItem,
    removeItem: storage.removeItem,
    setItem: (name, value) => {
      clearTimeout(timer);
      timer = setTimeout(() => storage.setItem(name, value), ms);
    },
  };
};

persist(creator, {
  name: "editor",
  storage: createJSONStorage(() => debounced(localStorage)),
});
```

Note that `JSON.stringify` still runs on every update. To save that cost too, write a `PersistStorage` (the non-JSON interface) that debounces before stringifying. Also flush on `pagehide` so the last change isn't lost.

### 388: Why can `persist` be slow for large states?

On every `set`, it runs `partialize` and `JSON.stringify` on the result, then writes to storage. `localStorage` writes are synchronous and block the main thread. For large or frequently changing state, persist only what you need, debounce writes, or use IndexedDB with an async storage.

### 389: How does `useShallow` behave if the selector function changes on every render?

It still works. The ref with the previous result lives across renders, and the comparison uses the stored result, not the function. A new wrapper function each render is fine because `useStore` just calls the newest one. The stable result reference is what matters.

### 390: Why should you not call `useShallow` conditionally or inside a callback?

`useShallow` is a hook (it uses `useRef`), so the rules of hooks apply. It must be called at the top level of a component or custom hook, every render, in the same order. Creating it inside a `useMemo` or an `if` breaks those rules.

### 391: How does Zustand compare to `useSyncExternalStore` written by hand?

Zustand is basically a small, well-tested wrapper around the same idea: a store with `subscribe` and `getSnapshot`, plus selectors. Writing it yourself is possible in 20 lines, but you would also need to handle selector stability, middleware, TypeScript types, persistence and devtools. Zustand gives you those for about 1 KB.

### 392: How would you write a minimal Zustand-like store from scratch?

```ts
import { useSyncExternalStore } from "react";

export function createMiniStore<T extends object>(init: T) {
  let state = init;
  const listeners = new Set<() => void>();

  const setState = (partial: Partial<T> | ((s: T) => Partial<T>)) => {
    const next = typeof partial === "function" ? partial(state) : partial;
    state = { ...state, ...next };
    listeners.forEach((l) => l());
  };
  const subscribe = (l: () => void) => {
    listeners.add(l);
    return () => listeners.delete(l);
  };
  const useStore = <U>(selector: (s: T) => U) =>
    useSyncExternalStore(
      subscribe,
      () => selector(state),
      () => selector(init),
    );

  return { getState: () => state, setState, subscribe, useStore };
}
```

This shows the core idea: a closure, a listener set and `useSyncExternalStore`.

### 393: In what situations would `getState()` inside a render be a bug?

Reading `getState()` during render doesn't subscribe, so the component won't update when that value changes. It may also read a newer value than the snapshot React is using, which can cause tearing within one render. Always use the hook for values you display.

### 394: How do you handle a store that must be reset when the logged-in user changes, without a page reload?

Subscribe to the auth store and reset dependent stores when the user id changes. For persisted stores, also switch their storage key per user and rehydrate.

```ts
useAuthStore.subscribe((s, prev) => {
  if (s.user?.id === prev.user?.id) return;
  useCartStore.setState(useCartStore.getInitialState(), true);
  useCartStore.persist.setOptions({ name: `cart-${s.user?.id ?? "guest"}` });
  useCartStore.persist.rehydrate();
});
```

### 395: How do you implement optimistic updates that are safe with concurrent edits?

Don't snapshot the whole state for rollback. Store the pending change with an id, apply it, and on failure undo only that change. On success, replace it with the server version.

```ts
toggleLike: async (id) => {
  set((s) => ({ posts: flip(s.posts, id) }))
  try {
    const updated = await api.toggleLike(id)
    set((s) => ({ posts: s.posts.map((p) => (p.id === id ? updated : p)) }))
  } catch {
    set((s) => ({ posts: flip(s.posts, id) }))
  }
},
```

Undoing with the same function (`flip`) on the latest state keeps other changes made in the meantime.

### 396: What are the downsides of storing derived data in the store to avoid recomputing?

You must update it in every action that changes its inputs, and forgetting one creates bugs where the derived value is stale. It also gets persisted and shown in DevTools unless you exclude it. Only do it when the computation is expensive and called often, and keep all updates of the inputs in one place.

### 397: How would you keep a derived value in the store updated automatically?

Subscribe to the inputs and update the derived field when they change.

```ts
useCartStore.subscribe((s, prev) => {
  if (s.items === prev.items) return;
  const total = s.items.reduce((sum, i) => sum + i.price * i.qty, 0);
  useCartStore.setState({ total });
});
```

This triggers a second update right after the first, and for a moment listeners see the old `total`. Usually a memoized selector is the better design.

### 398: How do you prevent the second update from the previous pattern from looping?

The guard `if (s.items === prev.items) return` does it. The second `setState` only changes `total`, so `items` keeps its reference and the listener returns early. Without that check, each update would trigger another update forever.

### 399: How would you design a store for an infinite scroll list?

Keep pages of ids and a map of items, plus a cursor and status.

```ts
interface FeedState {
  ids: string[];
  byId: Record<string, Post>;
  cursor: string | null;
  status: "idle" | "loading" | "error" | "done";
  loadMore: () => Promise<void>;
}
```

`loadMore` returns early if `status` is `loading` or `done`, appends new ids, and merges items into `byId`. Rows select by id, so loading more pages doesn't re-render existing rows. With TanStack Query's `useInfiniteQuery` you get this for free, so use that when the data is from a server.

### 400: How would you test an action that uses a debounce timer?

Use fake timers, trigger the update, advance time, and assert.

```ts
test("debounced search", async () => {
  vi.useFakeTimers();
  const search = vi.fn();
  useSearchStore.setState({ search });

  useSearchStore.getState().setQuery("re");
  useSearchStore.getState().setQuery("react");
  vi.advanceTimersByTime(300);

  expect(search).toHaveBeenCalledTimes(1);
  expect(search).toHaveBeenCalledWith("react");
  vi.useRealTimers();
});
```

Replacing the `search` action with a mock through `setState` works because actions are just state fields.

### 401: Why did Zustand choose to work without a Provider by default?

A store is just a JavaScript object with a subscribe method, so it doesn't need React to exist. Without a Provider, you can use the store in non-React code, in tests without rendering, and from anywhere in the tree with one import. The trade-off is that module-level stores are singletons, which is a problem for SSR and multiple instances. For those cases, the docs show how to add a Provider yourself.

### 402: Why does Zustand use explicit selectors instead of tracking which properties you read?

Explicit selectors are simple and predictable: you see exactly what a component depends on, and the comparison is just `Object.is`. Automatic tracking (like Valtio or MobX) needs proxies, which add runtime cost, can be confusing when values are passed around, and are harder to debug. Zustand chose the smaller and more explicit model.

### 403: How do signals (like in Preact Signals or Solid) differ from Zustand's model?

Signals track dependencies automatically and can update a single DOM node without re-rendering the component. Zustand works through React's render cycle: a change re-renders the subscribed components, and React updates the DOM. Signals can be faster for very fine-grained updates. Zustand fits better with normal React patterns and tools, and transient updates cover many of the cases where you would want signals.

### 404: How does Hot Module Replacement affect a Zustand store?

When you edit the store file, the bundler re-runs that module and creates a new store, so the state resets. Components that import the hook get the new store after the update. If you want to keep state during development, save it in `import.meta.hot.data` before the module is replaced and restore it.

```ts
export const useCounterStore = create<CounterState>()((set) => ({
  count: import.meta.hot?.data.count ?? 0,
  inc: () => set((s) => ({ count: s.count + 1 })),
}));

if (import.meta.hot) {
  import.meta.hot.dispose((data) => {
    data.count = useCounterStore.getState().count;
  });
}
```

### 405: How does React Strict Mode affect Zustand?

Strict Mode in development renders components twice and runs effects twice (mount, unmount, mount). Store subscriptions handle this fine, since `useSyncExternalStore` subscribes and unsubscribes correctly. But actions called from effects, like `fetchData()` on mount, run twice. Make those actions idempotent or guard against duplicate requests.

### 406: How do you write a selector factory for parameterized selectors?

Return a selector from a function, and keep it stable with `useCallback` if needed.

```ts
export const selectTodoById = (id: string) => (s: TodoState) => s.byId[id]

function TodoRow({ id }: { id: string }) {
  const todo = useTodoStore(useCallback(selectTodoById(id), [id]))
  return <li>{todo.text}</li>
}
```

The `useCallback` is optional for correctness, since the result `s.byId[id]` is stable anyway. It matters more when the selector is memoized and has its own cache, because a new selector each render would lose the cache.

### 407: How do you write a memoized selector per component instance?

Create the memoized selector once per component with `useMemo`, so each instance has its own cache.

```ts
const makeSelectVisible = () =>
  createSelector(
    [(s: TodoState) => s.todos, (_: TodoState, filter: string) => filter],
    (todos, filter) => todos.filter((t) => t.text.includes(filter)),
  )

function TodoList({ filter }: { filter: string }) {
  const selectVisible = useMemo(makeSelectVisible, [])
  const visible = useTodoStore((s) => selectVisible(s, filter))
  return <List items={visible} />
}
```

A shared memoized selector with a cache size of one would be recomputed every time two components use different `filter` values.

### 408: What is the risk of using a deep equality function with `createWithEqualityFn`?

Deep comparison walks the whole selected value on every store change for every subscribed component. For large objects this is slow, and it hides the real problem (selectors creating new objects). It is usually better to select smaller, stable pieces and use `shallow` only where needed.

### 409: How would you implement an offline action queue with Zustand?

Store pending actions in a persisted queue, process them when online, and remove each one after success.

```ts
const useQueueStore = create<QueueState>()(
  persist(
    (set, get) => ({
      queue: [] as Job[],
      enqueue: (job: Job) => set((s) => ({ queue: [...s.queue, job] })),
      flush: async () => {
        for (const job of get().queue) {
          try {
            await send(job);
            set((s) => ({ queue: s.queue.filter((j) => j.id !== job.id) }));
          } catch {
            break;
          }
        }
      },
    }),
    { name: "offline-queue" },
  ),
);

window.addEventListener("online", () => useQueueStore.getState().flush());
```

Make jobs idempotent on the server (with a job id), because a job can be sent twice if the app closes after sending but before removing it.

### 410: How would you handle refreshing an auth token only once when many requests fail at the same time?

Keep a single refresh promise outside the state, and let all callers wait for it.

```ts
let refreshing: Promise<string> | null = null;

async function getFreshToken() {
  if (!refreshing) {
    refreshing = refreshToken(useAuthStore.getState().refreshToken)
      .then((token) => {
        useAuthStore.setState({ token });
        return token;
      })
      .finally(() => {
        refreshing = null;
      });
  }
  return refreshing;
}
```

Every 401 handler calls `getFreshToken()` and retries with the result, so only one refresh request is sent.

### 411: How would you send analytics events for certain state changes without touching each action?

Subscribe to the store and compare old and new state.

```ts
useCartStore.subscribe((s, prev) => {
  if (s.items.length > prev.items.length) {
    const added = s.items.find((i) => !prev.items.some((p) => p.id === i.id));
    if (added) analytics.track("add_to_cart", { id: added.id });
  }
});
```

Or write a middleware that reads the devtools-style action name (third argument of `set`) and sends it. Keep analytics out of components so it is easy to find and test.

### 412: How would you build a middleware that records named actions for analytics?

Wrap `set` and use the third argument as the event name.

```ts
const track = (config) => (set, get, api) => {
  const trackedSet = (partial, replace, name) => {
    set(partial, replace, name);
    if (typeof name === "string") analytics.track(name);
  };
  api.setState = trackedSet;
  return config(trackedSet, get, api);
};
```

Passing `name` on to `set` matters: if `track` sits inside `devtools`, that `set` is the devtools version, which uses the name for the action label. For TypeScript, you would declare a mutator so `set` accepts the third argument.

### 413: What happens with errors thrown inside a `subscribe` listener?

The error is thrown from the `forEach` loop inside `setState`, so it stops notifying the remaining listeners and is thrown to whoever called `set`. The state itself was already updated. One bad listener can therefore break unrelated code. Catch errors inside listeners that do risky work.

### 414: Do React error boundaries catch errors in Zustand actions?

No. Error boundaries only catch errors thrown during rendering, in lifecycle methods and in constructors. Actions usually run in event handlers or async code, which error boundaries don't catch. Handle those errors in the action (store them in state) or with try/catch where the action is called. An error thrown inside a selector does happen during render, so a boundary does catch that.

### 415: Can a selector throw, and what happens if it does?

Yes. If a selector throws, for example because it reads a property of `undefined`, the error happens while React renders the component, and the nearest error boundary catches it. This often happens after `replace: true` removes fields or after a bad hydration. Write selectors defensively with optional chaining for data that may be missing.

### 416: What are the problems with storing `Error` objects in state?

`Error` objects don't serialize to JSON (they become `{}`), so they break `persist` and show poorly in DevTools. They also hold stack traces, which can be big. Store a message and maybe a code instead: `{ error: { message: e.message, code: e.code } }`.

### 417: How do you store a `BigInt` in a persisted store?

`JSON.stringify` throws on `BigInt`. Use a `replacer` and `reviver` in `createJSONStorage` that convert it to a tagged string and back.

```ts
createJSONStorage(() => localStorage, {
  replacer: (_, v) => (typeof v === "bigint" ? { __bigint: v.toString() } : v),
  reviver: (_, v: any) =>
    v && typeof v.__bigint === "string" ? BigInt(v.__bigint) : v,
});
```

### 418: How do you handle Dates correctly with `persist`?

`JSON.stringify` calls `Date.prototype.toJSON` before your replacer sees the value, so the replacer receives an ISO string, not a `Date`. On load, they stay strings unless you convert them back. Options: store timestamps as numbers, store ISO strings and convert in selectors, or fix them in `merge` or `onRehydrateStorage` after loading. A reviver that converts every ISO-looking string to a `Date` is risky, since it can change strings that should stay strings.

### 419: How would you migrate a store from a module-level hook to a context-based store without changing components?

Keep the hook name and signature, and change only its implementation.

```ts
// before
export const useCartStore = create<CartState>()(creator);

// after
export const createCartStore = () => createStore<CartState>()(creator);
const CartContext = createContext<StoreApi<CartState> | null>(null);

export function useCartStore<T>(selector: (s: CartState) => T): T {
  const store = useContext(CartContext);
  if (!store) throw new Error("Missing CartProvider");
  return useStore(store, selector);
}
```

Then add the Provider at the top. Code that used `useCartStore.getState()` outside React has to change, because there is no global store anymore. Find those calls first.

### 420: What is the "dual package hazard" and can it affect Zustand?

When a package ships both ESM and CommonJS builds, a project might load both copies (one through `import`, another through `require`). For stateless functions this is harmless. For your own store modules it matters: if the store module is loaded twice, you get two separate stores. Zustand itself has no global state, so two copies of the library are fine, but make sure your store file is only loaded once (one module format, no duplicate bundles).

### 421: How tree-shakable is Zustand?

Very. The core is small, and each middleware is a separate named export, so unused middleware is removed by the bundler. `immer` is in its own entry point so it doesn't pull in Immer unless used. Your own stores are just modules, so unused stores are dropped too, as long as nothing imports them.

### 422: How would you design a store for a drag-and-drop board (like Trello)?

Keep columns and cards normalized, and separate the persistent board data from the temporary drag state.

```ts
interface BoardState {
  columns: Record<string, { id: string; cardIds: string[] }>;
  cards: Record<string, Card>;
  moveCard: (cardId: string, from: string, to: string, index: number) => void;
}
```

During dragging, keep the pointer position in a separate store or use transient updates, so the board doesn't re-render on every mouse move. Only call `moveCard` on drop, which changes just two `cardIds` arrays, so only those two columns re-render.

### 423: Why separate "hot" UI state from "domain" state into different stores?

Hot state (pointer position, scroll, hover, drag preview) changes many times per second. If it lives in the same store as domain data, every change checks all domain subscribers. Putting it in its own store limits work to the few components that need it, and keeps the domain store clean for persistence and DevTools.

### 424: How do you decide what belongs in Zustand, in the URL, in a server cache and in local component state?

- URL: anything that should survive a refresh or be shareable (filters, page, selected tab).
- Server cache (TanStack Query etc.): data owned by the server.
- Zustand: client state shared by several components or used outside React.
- Local state: state only one component cares about (input text before submit, open dropdown).

Ask "who owns this data" and "who needs to read it" for each piece.

### 425: What are the risks of calling `getState()` inside a selector?

A selector should only use the state passed to it. Calling `otherStore.getState()` inside a selector means the component won't re-render when that other store changes, because it is not subscribed to it. It also makes the selector impure, which can cause stale values. Call the other store's hook instead.

### 426: How can you make an action easy to undo with a command pattern?

Have each action return or record an inverse operation.

```ts
interface Command {
  do: () => void;
  undo: () => void;
}

const undoStack: Command[] = [];

export function run(cmd: Command) {
  cmd.do();
  undoStack.push(cmd);
}

export function undo() {
  undoStack.pop()?.undo();
}

run({
  do: () => useBoardStore.getState().moveCard("c1", "todo", "done", 0),
  undo: () => useBoardStore.getState().moveCard("c1", "done", "todo", 0),
});
```

This uses less memory than storing full snapshots and works across several stores.

### 427: How do you write type-safe access to another slice from inside a slice?

Type `get` with the combined store type using the first `StateCreator` generic.

```ts
const createCartSlice: StateCreator<Store, [], [], CartSlice> = (set, get) => ({
  items: [],
  checkout: () => {
    if (!get().user) get().openLogin(); // from AuthSlice
  },
});
```

`Store` is the intersection of all slices. TypeScript then checks that `user` and `openLogin` exist in some slice.

### 428: How do you avoid circular imports between slice files?

Put the combined `Store` type in its own `types.ts` that only imports slice interfaces (types only, with `import type`). Slice files import the `Store` type, and the store file imports the slice creators. Since type-only imports are erased at build time, there is no runtime cycle.

### 429: What happens if two slices define the same key?

The later spread wins: `{ ...sliceA, ...sliceB }` keeps `sliceB`'s value. If both define an action with the same name, one silently overwrites the other. TypeScript may not catch it if the types are compatible. Use unique names or nest each slice's data under its own key.

### 430: Why might someone nest slice data under a key (like `cart: { ... }`) and what is the trade-off?

Nesting avoids name collisions and makes each slice's data clear. But `set` only merges the top level, so updates need manual spreading of the nested object, and selectors are a bit longer. Immer middleware makes nested updates easy again. Flat slices are simpler but need care with naming.

### 431: How do you handle a selector that needs data from props and from two different stores efficiently?

Select the minimal primitive from each store, then compute in the component.

```tsx
function Price({ productId }: { productId: string }) {
  const base = useProductStore((s) => s.byId[productId]?.price ?? 0);
  const rate = useCurrencyStore((s) => s.rate);
  return <span>{(base * rate).toFixed(2)}</span>;
}
```

Both hooks return numbers, so the component only re-renders when one of the numbers actually changes.

### 432: How would you implement a global loading indicator that shows when any request is running?

Keep a counter in a store and wrap requests.

```ts
const useLoadingStore = create<{ pending: number }>()(() => ({ pending: 0 }));

export async function tracked<T>(promise: Promise<T>) {
  useLoadingStore.setState((s) => ({ pending: s.pending + 1 }));
  try {
    return await promise;
  } finally {
    useLoadingStore.setState((s) => ({ pending: s.pending - 1 }));
  }
}

export const useIsLoading = () => useLoadingStore((s) => s.pending > 0);
```

A counter is safer than a boolean, because two parallel requests would otherwise turn it off too early.

### 433: How do you make a store work in both the browser and tests without touching `window`?

Avoid reading `window`, `localStorage` or `navigator` at module level. Read them inside actions or in an init function, or inject them. For `persist`, pass the storage through `createJSONStorage(() => localStorage)`, which is called lazily and returns `undefined` safely if storage is not available.

### 434: How would you use dependency injection to make a store easier to test?

Create the store with a factory that receives its dependencies.

```ts
export const createUserStore = (api: {
  getUser: (id: string) => Promise<User>;
}) =>
  createStore<UserState>()((set) => ({
    user: null,
    load: async (id) => set({ user: await api.getUser(id) }),
  }));

// app
export const userStore = createUserStore(realApi);

// test
const store = createUserStore({
  getUser: async () => ({ id: "1", name: "Test" }),
});
```

Tests get a fresh store with a fake API, without mocking modules.

### 435: What are the limits of `useShallow` for nested data, and how do you work around them?

`useShallow` only compares the top level of what you return. If you return `{ address: s.user.address }`, it works because `address` is a reference from the store. If you build new nested objects in the selector, like `{ address: { city: s.city } }`, it fails, because the inner object is new every time. Return references from the store or primitives, or flatten the result.

### 436: How would you profile the cost of selectors?

Wrap selectors in a timing helper during development, or use the browser Performance panel to record a slow interaction and look for time spent in selector functions (they run inside `useSyncExternalStore` checks after each `set`). If a selector shows up, make it O(1), memoize it, or reduce how many components use it.

### 437: How would you migrate a large app from Zustand v4's `create(selector, shallow)` usage to v5 safely?

1. Upgrade to the latest v4 and fix deprecation warnings.
2. Replace `import create from 'zustand'` with named imports.
3. Find all hooks called with a second argument (`shallow` or custom). Wrap those selectors with `useShallow`, or switch those stores to `createWithEqualityFn`.
4. Grep for selectors that build new arrays or objects, and fix them.
5. Fix TypeScript errors around `setState(..., true)`.
6. Check `persist` stores that relied on writing the initial state at creation.
7. Run the app and tests looking for "Maximum update depth exceeded".

### 438: How do you keep store logic framework-independent so it can be reused in a React Native and a web app?

Write stores with `createStore` from `zustand/vanilla` in a shared package, with no imports from React, DOM or React Native. Inject platform things like storage and API clients through factories. Each app then wraps the store with `useStore` and passes its own storage (`localStorage` on web, AsyncStorage or MMKV on native).

### 439: What is the effect of putting a very large object (like 10 MB of JSON) into a store?

`set` itself is cheap because it only copies the top level. But anything that walks the whole state becomes slow: `persist` (stringifying 10 MB on every update), `devtools` (serializing for the extension), and deep equality checks. Selecting parts of it is fine. Keep large data out of persisted and devtools-tracked stores, or exclude it with `partialize`.

### 440: How would you freeze state in development to catch accidental mutations?

Write a middleware that deep-freezes the state after each update in development.

```ts
const deepFreeze = (obj: any) => {
  if (obj && typeof obj === "object" && !Object.isFrozen(obj)) {
    Object.freeze(obj);
    Object.values(obj).forEach(deepFreeze);
  }
  return obj;
};

const freeze = (config) => (set, get, api) => {
  const frozenSet = (...args) => {
    set(...args);
    if (process.env.NODE_ENV !== "production") deepFreeze(get());
  };
  api.setState = frozenSet;
  return deepFreeze(config(frozenSet, get, api));
};
```

Mutations then throw in strict mode code instead of silently failing. Immer already freezes the state it produces by default.

### 441: Why does the immer middleware make accidental mutation bugs less likely?

Immer gives you a draft to change and builds a new state from it, so "mutation" inside `set` is safe. It also auto-freezes the state it returns by default, so if code elsewhere tries to change state directly, it throws an error in strict mode instead of silently doing nothing.

### 442: How would you handle a store that needs initialization from an async source before the app starts?

Create the store with defaults and an `init` action, and call it before rendering.

```ts
async function bootstrap() {
  await useConfigStore.getState().init()
  createRoot(document.getElementById('root')!).render(<App />)
}
bootstrap()
```

If you can't delay rendering, keep a `status` field and show a loading screen until it is ready.

### 443: When should a component subscribe with the hook vs use `subscribe` in an effect?

Use the hook when the value affects what the component renders. Use `subscribe` in an effect when you need to react to changes with a side effect (logging, imperative DOM or canvas updates, calling a third-party library) and the render output doesn't depend on the value. The hook re-renders; `subscribe` doesn't.

### 444: How do you avoid stale closures when subscribing inside an effect?

Read the latest props through a ref, or include them in the effect's dependency list so the subscription is recreated.

```tsx
const thresholdRef = useRef(threshold);
thresholdRef.current = threshold;

useEffect(
  () =>
    useSensorStore.subscribe((s) => {
      if (s.value > thresholdRef.current) alarm();
    }),
  [],
);
```

The store state itself is never stale inside the listener because it is passed in.

### 445: What would you check in a code review of a new Zustand store?

- Every component hook call has a selector.
- No selector builds new objects or arrays without `useShallow` or memoization.
- No mutation of state; nested updates copy correctly.
- Async actions handle errors, loading and races.
- `persist` uses a unique `name`, `partialize`, and a `version` if the shape may change.
- No secrets or tokens persisted in `localStorage`.
- `devtools` is outermost and off in production.
- No module-level store writes during server rendering.
- Tests reset the store between cases.

### 446: An app's main page feels slow, and the profiler shows a list component re-rendering on every store update. Walk through how you'd fix it.

1. Check the list's hook: if it selects `s.items` and items is replaced on every update, the list must re-render. Find which actions create a new `items` array without real changes.
2. Change the list to select only ids (`s.ids`), and have each row select its own item by id.
3. Wrap rows in `memo` so the parent rendering doesn't re-render all rows.
4. Make sure no other hook in the list returns a new object.
5. If the list is long, add virtualization.
6. Profile again and confirm only changed rows render.

### 447: How would you explain the difference between "the store changed" and "the component re-rendered" in Zustand?

Every `set` with a new state changes the store and calls all listeners. For each subscribed component, React runs the selector and compares the result with the previous one. The component re-renders only if that result is different. So many store changes can happen with zero re-renders, as long as the selected values stay the same.

### 448: How would you build a "recent searches" feature with Zustand?

```ts
const useRecentStore = create<RecentState>()(
  persist(
    (set) => ({
      recent: [] as string[],
      add: (q: string) =>
        set((s) => ({
          recent: [q, ...s.recent.filter((r) => r !== q)].slice(0, 10),
        })),
      clear: () => set({ recent: [] }),
    }),
    { name: "recent-searches", version: 1 },
  ),
);
```

It keeps the newest search first, removes duplicates and caps the list at 10, so storage never grows without limit.

### 449: What would you say are the main strengths and weaknesses of Zustand?

Strengths: tiny, very little boilerplate, no Provider, works outside React, selectors give fine control over re-renders, simple middleware for persistence and devtools, easy to test, good TypeScript support.

Weaknesses: no enforced structure (teams must agree on conventions), easy to cause re-renders or infinite loops with bad selectors, module-level stores are a trap in SSR, no built-in server data caching, and complex TypeScript types once you write custom middleware.

### 450: Walk through what happens, step by step, when a user clicks a button that calls a Zustand action.

1. The click handler calls the action, for example `increment()`.
2. The action calls `set((s) => ({ count: s.count + 1 }))`.
3. Middleware wrappers run first if any (immer turns a draft function into a new state, devtools records the action, persist will write to storage).
4. The core `setState` computes the next state, checks `Object.is` against the current state, and merges it into a new state object.
5. It calls every listener synchronously with the new and previous state.
6. For each subscribed component, `useSyncExternalStore` runs its selector against the new state and compares the result with the last one using `Object.is`.
7. Components whose selected values changed are scheduled to re-render; React batches these into one render pass.
8. React renders those components with the new values and updates the DOM.
9. After `set` returns, `persist` has already written the new state to storage (or started an async write).
