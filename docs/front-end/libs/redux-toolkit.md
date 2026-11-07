# Redux Toolkit Interview Questions and Answers

_Last updated: October 28, 2026_

450 questions split into three levels: easy, moderate and advanced. The answers follow Redux Toolkit 2.x (with React-Redux 9, Reselect 5 and Immer 10), including RTK Query.

## Table of Contents

- [Easy Questions](#easy-questions)
- [Moderate Questions](#moderate-questions)
- [Advanced Questions](#advanced-questions)

### Easy Questions (1-150)

- [1: What is Redux Toolkit?](#1-what-is-redux-toolkit)
- [2: What problems does Redux Toolkit solve?](#2-what-problems-does-redux-toolkit-solve)
- [3: How do you install Redux Toolkit?](#3-how-do-you-install-redux-toolkit)
- [4: What are the main APIs in Redux Toolkit?](#4-what-are-the-main-apis-in-redux-toolkit)
- [5: Is Redux Toolkit a replacement for Redux?](#5-is-redux-toolkit-a-replacement-for-redux)
- [6: What is a Redux store?](#6-what-is-a-redux-store)
- [7: How do you create a store with Redux Toolkit?](#7-how-do-you-create-a-store-with-redux-toolkit)
- [8: What does `configureStore` set up by default?](#8-what-does-configurestore-set-up-by-default)
- [9: What is a slice?](#9-what-is-a-slice)
- [10: What does `createSlice` do?](#10-what-does-createslice-do)
- [11: What is the `name` option in `createSlice` used for?](#11-what-is-the-name-option-in-createslice-used-for)
- [12: What is `initialState` in a slice?](#12-what-is-initialstate-in-a-slice)
- [13: What is an action in Redux?](#13-what-is-an-action-in-redux)
- [14: What is an action creator?](#14-what-is-an-action-creator)
- [15: What is `payload`?](#15-what-is-payload)
- [16: What is `PayloadAction`?](#16-what-is-payloadaction)
- [17: What is a reducer?](#17-what-is-a-reducer)
- [18: What rules must a reducer follow?](#18-what-rules-must-a-reducer-follow)
- [19: How can RTK reducers "mutate" state if Redux requires immutable updates?](#19-how-can-rtk-reducers-mutate-state-if-redux-requires-immutable-updates)
- [20: Can you return a new state from an RTK reducer instead of mutating it?](#20-can-you-return-a-new-state-from-an-rtk-reducer-instead-of-mutating-it)
- [21: Can you mutate the draft and also return a value in the same reducer?](#21-can-you-mutate-the-draft-and-also-return-a-value-in-the-same-reducer)
- [22: How do you reset a slice to its initial state?](#22-how-do-you-reset-a-slice-to-its-initial-state)
- [23: How do you handle a slice whose state is a primitive value like a number?](#23-how-do-you-handle-a-slice-whose-state-is-a-primitive-value-like-a-number)
- [24: What is `dispatch`?](#24-what-is-dispatch)
- [25: What is `getState`?](#25-what-is-getstate)
- [26: What is the `Provider` component?](#26-what-is-the-provider-component)
- [27: What is `useSelector`?](#27-what-is-useselector)
- [28: What is `useDispatch`?](#28-what-is-usedispatch)
- [29: What is `useStore`?](#29-what-is-usestore)
- [30: Show a full counter example with Redux Toolkit and React.](#30-show-a-full-counter-example-with-redux-toolkit-and-react)
- [31: What is a selector?](#31-what-is-a-selector)
- [32: Why define selectors in the slice file instead of writing them inline in components?](#32-why-define-selectors-in-the-slice-file-instead-of-writing-them-inline-in-components)
- [33: How do you combine multiple slices into one store?](#33-how-do-you-combine-multiple-slices-into-one-store)
- [34: What is `combineReducers` and do you still need it?](#34-what-is-combinereducers-and-do-you-still-need-it)
- [35: How do you get the `RootState` type?](#35-how-do-you-get-the-rootstate-type)
- [36: How do you get the `AppDispatch` type and why do you need it?](#36-how-do-you-get-the-appdispatch-type-and-why-do-you-need-it)
- [37: How do you create typed React-Redux hooks?](#37-how-do-you-create-typed-react-redux-hooks)
- [38: What are the Redux DevTools?](#38-what-are-the-redux-devtools)
- [39: How do you turn off DevTools in production?](#39-how-do-you-turn-off-devtools-in-production)
- [40: What is middleware in Redux?](#40-what-is-middleware-in-redux)
- [41: Which middleware does `configureStore` add by default?](#41-which-middleware-does-configurestore-add-by-default)
- [42: How do you add your own middleware to the store?](#42-how-do-you-add-your-own-middleware-to-the-store)
- [43: What is the difference between `concat` and `prepend` on the default middleware?](#43-what-is-the-difference-between-concat-and-prepend-on-the-default-middleware)
- [44: What is a thunk?](#44-what-is-a-thunk)
- [45: How do you type a thunk manually?](#45-how-do-you-type-a-thunk-manually)
- [46: What is `createAsyncThunk`?](#46-what-is-createasyncthunk)
- [47: Which actions does `createAsyncThunk` dispatch?](#47-which-actions-does-createasyncthunk-dispatch)
- [48: How do you handle `createAsyncThunk` actions in a slice?](#48-how-do-you-handle-createasyncthunk-actions-in-a-slice)
- [49: What is the difference between `reducers` and `extraReducers` in `createSlice`?](#49-what-is-the-difference-between-reducers-and-extrareducers-in-createslice)
- [50: What is the builder callback?](#50-what-is-the-builder-callback)
- [51: What does `builder.addCase` do?](#51-what-does-builderaddcase-do)
- [52: What is a common pattern for tracking loading state?](#52-what-is-a-common-pattern-for-tracking-loading-state)
- [53: What is `rejectWithValue`?](#53-what-is-rejectwithvalue)
- [54: What does `.unwrap()` do on a dispatched thunk?](#54-what-does-unwrap-do-on-a-dispatched-thunk)
- [55: What does `createAction` do?](#55-what-does-createaction-do)
- [56: What is a prepare callback?](#56-what-is-a-prepare-callback)
- [57: What is `nanoid`?](#57-what-is-nanoid)
- [58: What is `createReducer`?](#58-what-is-createreducer)
- [59: What is RTK Query?](#59-what-is-rtk-query)
- [60: When should you use RTK Query instead of `createAsyncThunk`?](#60-when-should-you-use-rtk-query-instead-of-createasyncthunk)
- [61: How do you define an API with `createApi`?](#61-how-do-you-define-an-api-with-createapi)
- [62: What is `fetchBaseQuery`?](#62-what-is-fetchbasequery)
- [63: What is the difference between a query and a mutation endpoint?](#63-what-is-the-difference-between-a-query-and-a-mutation-endpoint)
- [64: How are RTK Query hook names generated?](#64-how-are-rtk-query-hook-names-generated)
- [65: How do you add an RTK Query API to the store?](#65-how-do-you-add-an-rtk-query-api-to-the-store)
- [66: What is `reducerPath` in `createApi`?](#66-what-is-reducerpath-in-createapi)
- [67: What does `useQuery` return?](#67-what-does-usequery-return)
- [68: What is the difference between `isLoading` and `isFetching`?](#68-what-is-the-difference-between-isloading-and-isfetching)
- [69: How do you use a mutation hook?](#69-how-do-you-use-a-mutation-hook)
- [70: What are tags in RTK Query?](#70-what-are-tags-in-rtk-query)
- [71: What is `tagTypes` for?](#71-what-is-tagtypes-for)
- [72: How do you manually refetch a query?](#72-how-do-you-manually-refetch-a-query)
- [73: How do you skip a query until some value is ready?](#73-how-do-you-skip-a-query-until-some-value-is-ready)
- [74: What is `keepUnusedDataFor`?](#74-what-is-keepunuseddatafor)
- [75: What is `createEntityAdapter`?](#75-what-is-createentityadapter)
- [76: What is normalized state?](#76-what-is-normalized-state)
- [77: What does `adapter.getInitialState()` return?](#77-what-does-adaptergetinitialstate-return)
- [78: Which CRUD methods does an entity adapter provide?](#78-which-crud-methods-does-an-entity-adapter-provide)
- [79: How do you use the adapter selectors?](#79-how-do-you-use-the-adapter-selectors)
- [80: What is `sortComparer` in `createEntityAdapter`?](#80-what-is-sortcomparer-in-createentityadapter)
- [81: What is `selectId` in `createEntityAdapter`?](#81-what-is-selectid-in-createentityadapter)
- [82: What is `createSelector`?](#82-what-is-createselector)
- [83: Why do selectors need memoization?](#83-why-do-selectors-need-memoization)
- [84: Why should Redux state and actions be serializable?](#84-why-should-redux-state-and-actions-be-serializable)
- [85: What does the serializability check middleware do?](#85-what-does-the-serializability-check-middleware-do)
- [86: What does the immutability check middleware do?](#86-what-does-the-immutability-check-middleware-do)
- [87: How should you store a date in Redux state?](#87-how-should-you-store-a-date-in-redux-state)
- [88: When should you use Redux instead of React Context?](#88-when-should-you-use-redux-instead-of-react-context)
- [89: Should all state go into Redux?](#89-should-all-state-go-into-redux)
- [90: What folder structure is recommended for Redux Toolkit projects?](#90-what-folder-structure-is-recommended-for-redux-toolkit-projects)
- [91: What is the "ducks" pattern?](#91-what-is-the-ducks-pattern)
- [92: What does `actionCreator.match` do?](#92-what-does-actioncreatormatch-do)
- [93: What is `slice.caseReducers`?](#93-what-is-slicecasereducers)
- [94: What is `slice.getInitialState()`?](#94-what-is-slicegetinitialstate)
- [95: What is `preloadedState`?](#95-what-is-preloadedstate)
- [96: Can you use Redux Toolkit without React?](#96-can-you-use-redux-toolkit-without-react)
- [97: What does `store.subscribe` do?](#97-what-does-storesubscribe-do)
- [98: What are the three principles of Redux?](#98-what-are-the-three-principles-of-redux)
- [99: What is one-way data flow in Redux?](#99-what-is-one-way-data-flow-in-redux)
- [100: Can you have more than one Redux store?](#100-can-you-have-more-than-one-redux-store)
- [101: What is the thunk "extra argument"?](#101-what-is-the-thunk-extra-argument)
- [102: What does `dispatch` return when you dispatch a thunk?](#102-what-does-dispatch-return-when-you-dispatch-a-thunk)
- [103: What is `current` from Immer and why is it exported by RTK?](#103-what-is-current-from-immer-and-why-is-it-exported-by-rtk)
- [104: What does `isAnyOf` do?](#104-what-does-isanyof-do)
- [105: Why is `createStore` deprecated?](#105-why-is-createstore-deprecated)
- [106: What were the main changes in Redux Toolkit 2.0?](#106-what-were-the-main-changes-in-redux-toolkit-20)
- [107: Why must action types be strings?](#107-why-must-action-types-be-strings)
- [108: What is `UnknownAction`?](#108-what-is-unknownaction)
- [109: What import paths does Redux Toolkit have?](#109-what-import-paths-does-redux-toolkit-have)
- [110: What is the difference between importing `createApi` from `/query` and `/query/react`?](#110-what-is-the-difference-between-importing-createapi-from-query-and-queryreact)
- [111: What is `setupListeners`?](#111-what-is-setuplisteners)
- [112: What is `refetchOnFocus`?](#112-what-is-refetchonfocus)
- [113: How do you poll data with RTK Query?](#113-how-do-you-poll-data-with-rtk-query)
- [114: What is `transformResponse`?](#114-what-is-transformresponse)
- [115: How do you add an auth token to every request?](#115-how-do-you-add-an-auth-token-to-every-request)
- [116: How do you send a POST request with a body and query params?](#116-how-do-you-send-a-post-request-with-a-body-and-query-params)
- [117: What is the difference between `data` and `currentData` in a query result?](#117-what-is-the-difference-between-data-and-currentdata-in-a-query-result)
- [118: What does an error from `fetchBaseQuery` look like?](#118-what-does-an-error-from-fetchbasequery-look-like)
- [119: How do you handle errors from a mutation?](#119-how-do-you-handle-errors-from-a-mutation)
- [120: What is `useLazyQuery`?](#120-what-is-uselazyquery)
- [121: Why should you avoid storing derived data in Redux state?](#121-why-should-you-avoid-storing-derived-data-in-redux-state)
- [122: Where should most of the business logic go?](#122-where-should-most-of-the-business-logic-go)
- [123: What does "model actions as events, not setters" mean?](#123-what-does-model-actions-as-events-not-setters-mean)
- [124: What is the Redux Style Guide?](#124-what-is-the-redux-style-guide)
- [125: How do you update nested state with Immer?](#125-how-do-you-update-nested-state-with-immer)
- [126: How do you add, update and remove items in an array in a slice reducer?](#126-how-do-you-add-update-and-remove-items-in-an-array-in-a-slice-reducer)
- [127: How do you toggle a boolean in a slice?](#127-how-do-you-toggle-a-boolean-in-a-slice)
- [128: Can a reducer make an API call?](#128-can-a-reducer-make-an-api-call)
- [129: Can a reducer dispatch an action?](#129-can-a-reducer-dispatch-an-action)
- [130: What happens if you dispatch an action no reducer handles?](#130-what-happens-if-you-dispatch-an-action-no-reducer-handles)
- [131: How do you test a slice reducer?](#131-how-do-you-test-a-slice-reducer)
- [132: How do you test an action creator?](#132-how-do-you-test-an-action-creator)
- [133: Does Redux Toolkit include `react-redux`?](#133-does-redux-toolkit-include-react-redux)
- [134: Which React-Redux version works with Redux Toolkit 2.x?](#134-which-react-redux-version-works-with-redux-toolkit-2x)
- [135: How do you read the arguments that were passed to a thunk in a reducer?](#135-how-do-you-read-the-arguments-that-were-passed-to-a-thunk-in-a-reducer)
- [136: What is `action.meta.requestId`?](#136-what-is-actionmetarequestid)
- [137: How do you pass multiple arguments to a `createAsyncThunk` payload creator?](#137-how-do-you-pass-multiple-arguments-to-a-createasyncthunk-payload-creator)
- [138: How do you get the state inside a `createAsyncThunk`?](#138-how-do-you-get-the-state-inside-a-createasyncthunk)
- [139: How does a slice respond to an action from another slice?](#139-how-does-a-slice-respond-to-an-action-from-another-slice)
- [140: What does `builder.addDefaultCase` do?](#140-what-does-builderadddefaultcase-do)
- [141: What is `invalidatesTags` on a mutation?](#141-what-is-invalidatestags-on-a-mutation)
- [142: What is `providesTags` on a query?](#142-what-is-providestags-on-a-query)
- [143: Does RTK Query send two requests if two components use the same query with the same argument?](#143-does-rtk-query-send-two-requests-if-two-components-use-the-same-query-with-the-same-argument)
- [144: How do you get a typed error message out of an RTK Query error?](#144-how-do-you-get-a-typed-error-message-out-of-an-rtk-query-error)
- [145: What does `isSuccess` mean in a query result?](#145-what-does-issuccess-mean-in-a-query-result)
- [146: Can you use multiple query hooks in one component?](#146-can-you-use-multiple-query-hooks-in-one-component)
- [147: What is the `AppStore` type and when do you need it?](#147-what-is-the-appstore-type-and-when-do-you-need-it)
- [148: How do you dispatch an action outside of React?](#148-how-do-you-dispatch-an-action-outside-of-react)
- [149: What is the difference between RTK and Zustand?](#149-what-is-the-difference-between-rtk-and-zustand)
- [150: What is the difference between RTK Query and TanStack Query?](#150-what-is-the-difference-between-rtk-query-and-tanstack-query)

### Moderate Questions (151-300)

- [151: How do you define selectors inside `createSlice`?](#151-how-do-you-define-selectors-inside-createslice)
- [152: What is `reducerPath` on a slice?](#152-what-is-reducerpath-on-a-slice)
- [153: What is the difference between `slice.selectors` and `slice.getSelectors()`?](#153-what-is-the-difference-between-sliceselectors-and-slicegetselectors)
- [154: How do selectors with extra arguments work in `slice.selectors`?](#154-how-do-selectors-with-extra-arguments-work-in-sliceselectors)
- [155: What is the `create` callback syntax for `reducers` in `createSlice`?](#155-what-is-the-create-callback-syntax-for-reducers-in-createslice)
- [156: How do you define an async thunk inside `createSlice`?](#156-how-do-you-define-an-async-thunk-inside-createslice)
- [157: What is `combineSlices`?](#157-what-is-combineslices)
- [158: How do you inject a slice later with `combineSlices`?](#158-how-do-you-inject-a-slice-later-with-combineslices)
- [159: How do you type lazy-loaded slices with `combineSlices`?](#159-how-do-you-type-lazy-loaded-slices-with-combineslices)
- [160: What happens if you call a slice selector before the slice is injected?](#160-what-happens-if-you-call-a-slice-selector-before-the-slice-is-injected)
- [161: What does the second argument to the `createAsyncThunk` payload creator contain?](#161-what-does-the-second-argument-to-the-createasyncthunk-payload-creator-contain)
- [162: What is `fulfillWithValue`?](#162-what-is-fulfillwithvalue)
- [163: How do you type `createAsyncThunk` with generics?](#163-how-do-you-type-createasyncthunk-with-generics)
- [164: What is `createAsyncThunk.withTypes()`?](#164-what-is-createasyncthunkwithtypes)
- [165: What is the `condition` option of `createAsyncThunk`?](#165-what-is-the-condition-option-of-createasyncthunk)
- [166: What does `dispatchConditionRejection` do?](#166-what-does-dispatchconditionrejection-do)
- [167: How do you cancel a `createAsyncThunk` request?](#167-how-do-you-cancel-a-createasyncthunk-request)
- [168: How can you tell in a reducer that a thunk was aborted?](#168-how-can-you-tell-in-a-reducer-that-a-thunk-was-aborted)
- [169: What does `serializeError` do in `createAsyncThunk`?](#169-what-does-serializeerror-do-in-createasyncthunk)
- [170: What is `idGenerator` in `createAsyncThunk`?](#170-what-is-idgenerator-in-createasyncthunk)
- [171: What is `getPendingMeta`?](#171-what-is-getpendingmeta)
- [172: How do you prevent an older request from overwriting newer data?](#172-how-do-you-prevent-an-older-request-from-overwriting-newer-data)
- [173: What are `isPending`, `isFulfilled` and `isRejected`?](#173-what-are-ispending-isfulfilled-and-isrejected)
- [174: What is `builder.addMatcher`?](#174-what-is-builderaddmatcher)
- [175: In what order must you call the builder methods?](#175-in-what-order-must-you-call-the-builder-methods)
- [176: What does `isRejectedWithValue` do?](#176-what-does-isrejectedwithvalue-do)
- [177: How do you write a typed custom middleware in RTK 2.x?](#177-how-do-you-write-a-typed-custom-middleware-in-rtk-2x)
- [178: How do you configure the serializability check?](#178-how-do-you-configure-the-serializability-check)
- [179: How do you configure Redux Toolkit to work with `redux-persist`?](#179-how-do-you-configure-redux-toolkit-to-work-with-redux-persist)
- [180: How do you configure the immutability check?](#180-how-do-you-configure-the-immutability-check)
- [181: What is `Tuple` and why does it exist?](#181-what-is-tuple-and-why-does-it-exist)
- [182: How do you add a store enhancer in RTK 2.x?](#182-how-do-you-add-a-store-enhancer-in-rtk-2x)
- [183: What does the `autoBatchEnhancer` do?](#183-what-does-the-autobatchenhancer-do)
- [184: What options can you pass to `devTools` in `configureStore`?](#184-what-options-can-you-pass-to-devtools-in-configurestore)
- [185: How do you inject dependencies into thunks for testing?](#185-how-do-you-inject-dependencies-into-thunks-for-testing)
- [186: What is the listener middleware?](#186-what-is-the-listener-middleware)
- [187: What are the ways to choose which actions a listener runs for?](#187-what-are-the-ways-to-choose-which-actions-a-listener-runs-for)
- [188: What does the `listenerApi` give you inside an effect?](#188-what-does-the-listenerapi-give-you-inside-an-effect)
- [189: When should you use a listener instead of a thunk?](#189-when-should-you-use-a-listener-instead-of-a-thunk)
- [190: How do you debounce with the listener middleware?](#190-how-do-you-debounce-with-the-listener-middleware)
- [191: What do `condition` and `take` do in a listener?](#191-what-do-condition-and-take-do-in-a-listener)
- [192: How do you add a listener from a component?](#192-how-do-you-add-a-listener-from-a-component)
- [193: How do you type the listener middleware?](#193-how-do-you-type-the-listener-middleware)
- [194: How do you remove a listener?](#194-how-do-you-remove-a-listener)
- [195: What is the difference between `addOne`, `setOne` and `upsertOne`?](#195-what-is-the-difference-between-addone-setone-and-upsertone)
- [196: How does `updateOne` work?](#196-how-does-updateone-work)
- [197: What is the difference between `setAll` and `setMany`?](#197-what-is-the-difference-between-setall-and-setmany)
- [198: How do you combine an entity adapter with `createAsyncThunk`?](#198-how-do-you-combine-an-entity-adapter-with-createasyncthunk)
- [199: Are the adapter selectors memoized?](#199-are-the-adapter-selectors-memoized)
- [200: How do you type entity adapters with non-string IDs?](#200-how-do-you-type-entity-adapters-with-non-string-ids)
- [201: What are input selectors and output selectors in `createSelector`?](#201-what-are-input-selectors-and-output-selectors-in-createselector)
- [202: How do you pass arguments to a memoized selector?](#202-how-do-you-pass-arguments-to-a-memoized-selector)
- [203: What changed in Reselect 5 memoization?](#203-what-changed-in-reselect-5-memoization)
- [204: What is `createSelector.withTypes()`?](#204-what-is-createselectorwithtypes)
- [205: What dev checks do Reselect 5 and React-Redux 9 run on selectors?](#205-what-dev-checks-do-reselect-5-and-react-redux-9-run-on-selectors)
- [206: What is a common mistake that breaks memoization?](#206-what-is-a-common-mistake-that-breaks-memoization)
- [207: What is `createDraftSafeSelector`?](#207-what-is-createdraftsafeselector)
- [208: When should you pass `shallowEqual` to `useSelector`?](#208-when-should-you-pass-shallowequal-to-useselector)
- [209: How does the function form of `providesTags` help?](#209-how-does-the-function-form-of-providestags-help)
- [210: What is the `LIST` tag pattern?](#210-what-is-the-list-tag-pattern)
- [211: What does invalidating a tag without an ID do?](#211-what-does-invalidating-a-tag-without-an-id-do)
- [212: What is `onQueryStarted`?](#212-what-is-onquerystarted)
- [213: How do you do an optimistic update in RTK Query?](#213-how-do-you-do-an-optimistic-update-in-rtk-query)
- [214: What is a pessimistic update?](#214-what-is-a-pessimistic-update)
- [215: What is the difference between `updateQueryData` and `upsertQueryData`?](#215-what-is-the-difference-between-updatequerydata-and-upsertquerydata)
- [216: What is `upsertQueryEntries`?](#216-what-is-upsertqueryentries)
- [217: How do you prefetch data with RTK Query?](#217-how-do-you-prefetch-data-with-rtk-query)
- [218: What is `selectFromResult`?](#218-what-is-selectfromresult)
- [219: What is `refetchOnMountOrArgChange`?](#219-what-is-refetchonmountorargchange)
- [220: What is `injectEndpoints`?](#220-what-is-injectendpoints)
- [221: What is `enhanceEndpoints`?](#221-what-is-enhanceendpoints)
- [222: What is `queryFn`?](#222-what-is-queryfn)
- [223: What is `transformErrorResponse`?](#223-what-is-transformerrorresponse)
- [224: How do you retry failed requests in RTK Query?](#224-how-do-you-retry-failed-requests-in-rtk-query)
- [225: How do you write a custom base query with axios?](#225-how-do-you-write-a-custom-base-query-with-axios)
- [226: Which options does `fetchBaseQuery` accept?](#226-which-options-does-fetchbasequery-accept)
- [227: How do you send cookies with `fetchBaseQuery`?](#227-how-do-you-send-cookies-with-fetchbasequery)
- [228: How do you upload a file with RTK Query?](#228-how-do-you-upload-a-file-with-rtk-query)
- [229: How do you treat a 200 response with an error body as an error?](#229-how-do-you-treat-a-200-response-with-an-error-body-as-an-error)
- [230: What is `fixedCacheKey` on a mutation?](#230-what-is-fixedcachekey-on-a-mutation)
- [231: What does `reset` do on a mutation result?](#231-what-does-reset-do-on-a-mutation-result)
- [232: How do you read cached query data outside of a hook?](#232-how-do-you-read-cached-query-data-outside-of-a-hook)
- [233: How do you run a query outside of React?](#233-how-do-you-run-a-query-outside-of-react)
- [234: What options does `initiate` accept?](#234-what-options-does-initiate-accept)
- [235: What are `useQueryState` and `useQuerySubscription`?](#235-what-are-usequerystate-and-usequerysubscription)
- [236: How do you invalidate tags from outside an endpoint?](#236-how-do-you-invalidate-tags-from-outside-an-endpoint)
- [237: How do you clear the whole RTK Query cache?](#237-how-do-you-clear-the-whole-rtk-query-cache)
- [238: What is `ApiProvider`?](#238-what-is-apiprovider)
- [239: How does RTK Query build a cache key?](#239-how-does-rtk-query-build-a-cache-key)
- [240: How do you make one query depend on another?](#240-how-do-you-make-one-query-depend-on-another)
- [241: What is the difference between `skip: true` and `skipToken`?](#241-what-is-the-difference-between-skip-true-and-skiptoken)
- [242: What is `structuralSharing` in RTK Query?](#242-what-is-structuralsharing-in-rtk-query)
- [243: How do you store RTK Query results in normalized form?](#243-how-do-you-store-rtk-query-results-in-normalized-form)
- [244: What does `keepUnusedDataFor: 0` do?](#244-what-does-keepunuseddatafor-0-do)
- [245: What is `invalidationBehavior` in `createApi`?](#245-what-is-invalidationbehavior-in-createapi)
- [246: What does the lazy query trigger return?](#246-what-does-the-lazy-query-trigger-return)
- [247: What are infinite queries in RTK Query?](#247-what-are-infinite-queries-in-rtk-query)
- [248: How do you use the infinite query hook?](#248-how-do-you-use-the-infinite-query-hook)
- [249: What does `getNextPageParam` receive and what should it return?](#249-what-does-getnextpageparam-receive-and-what-should-it-return)
- [250: What is schema validation in RTK Query?](#250-what-is-schema-validation-in-rtk-query)
- [251: What happens when a schema check fails?](#251-what-happens-when-a-schema-check-fails)
- [252: What is RTK Query code generation?](#252-what-is-rtk-query-code-generation)
- [253: How do you set up the store for tests?](#253-how-do-you-set-up-the-store-for-tests)
- [254: How do you write a `renderWithProviders` test helper?](#254-how-do-you-write-a-renderwithproviders-test-helper)
- [255: How do you test components that use RTK Query?](#255-how-do-you-test-components-that-use-rtk-query)
- [256: How do you test a `createAsyncThunk`?](#256-how-do-you-test-a-createasyncthunk)
- [257: How do you set up Redux Toolkit in the Next.js App Router?](#257-how-do-you-set-up-redux-toolkit-in-the-nextjs-app-router)
- [258: How do you pass server data into the store in Next.js?](#258-how-do-you-pass-server-data-into-the-store-in-nextjs)
- [259: How do you migrate an old Redux codebase to Redux Toolkit?](#259-how-do-you-migrate-an-old-redux-codebase-to-redux-toolkit)
- [260: How do you replace `connect` with hooks?](#260-how-do-you-replace-connect-with-hooks)
- [261: How do you reset all state on logout?](#261-how-do-you-reset-all-state-on-logout)
- [262: How do you avoid circular imports between the store and slices?](#262-how-do-you-avoid-circular-imports-between-the-store-and-slices)
- [263: How do you add `meta` or `error` to an action with a prepare callback?](#263-how-do-you-add-meta-or-error-to-an-action-with-a-prepare-callback)
- [264: What is the difference between `current` and `original`?](#264-what-is-the-difference-between-current-and-original)
- [265: What is `isDraft`?](#265-what-is-isdraft)
- [266: Why doesn't reassigning `state` work in a reducer?](#266-why-doesnt-reassigning-state-work-in-a-reducer)
- [267: Can you use a draft after an `await`?](#267-can-you-use-a-draft-after-an-await)
- [268: When does a component using `useSelector` re-render?](#268-when-does-a-component-using-useselector-re-render)
- [269: How do you keep `useSelector` from causing extra renders?](#269-how-do-you-keep-useselector-from-causing-extra-renders)
- [270: How do you normalize nested API data?](#270-how-do-you-normalize-nested-api-data)
- [271: How do you handle `selectById` returning `undefined`?](#271-how-do-you-handle-selectbyid-returning-undefined)
- [272: What does `isAllOf` do?](#272-what-does-isallof-do)
- [273: What does `isAsyncThunkAction` do?](#273-what-does-isasyncthunkaction-do)
- [274: What does the action creator check middleware catch?](#274-what-does-the-action-creator-check-middleware-catch)
- [275: How do you react to RTK Query results in a regular slice?](#275-how-do-you-react-to-rtk-query-results-in-a-regular-slice)
- [276: How do you stop polling when a condition is met?](#276-how-do-you-stop-polling-when-a-condition-is-met)
- [277: How do you use response headers in `transformResponse`?](#277-how-do-you-use-response-headers-in-transformresponse)
- [278: What happens to `providesTags` when a query fails?](#278-what-happens-to-providestags-when-a-query-fails)
- [279: What is `extraOptions` on an endpoint?](#279-what-is-extraoptions-on-an-endpoint)
- [280: Can you use the hooks from `api.endpoints` instead of the named exports?](#280-can-you-use-the-hooks-from-apiendpoints-instead-of-the-named-exports)
- [281: How do you type a query that takes no argument?](#281-how-do-you-type-a-query-that-takes-no-argument)
- [282: How do you set defaults for all endpoints in an API?](#282-how-do-you-set-defaults-for-all-endpoints-in-an-api)
- [283: How do you download a file with RTK Query?](#283-how-do-you-download-a-file-with-rtk-query)
- [284: How do you read the arguments of a mutation from its result?](#284-how-do-you-read-the-arguments-of-a-mutation-from-its-result)
- [285: How do you create a memoized selector for derived RTK Query data inside a component?](#285-how-do-you-create-a-memoized-selector-for-derived-rtk-query-data-inside-a-component)
- [286: Why does React 18 batching matter for Redux?](#286-why-does-react-18-batching-matter-for-redux)
- [287: How do you create a reusable slice factory?](#287-how-do-you-create-a-reusable-slice-factory)
- [288: When should you split state into multiple slices?](#288-when-should-you-split-state-into-multiple-slices)
- [289: How do you share one action between several slices?](#289-how-do-you-share-one-action-between-several-slices)
- [290: How do you handle global loading state for many thunks?](#290-how-do-you-handle-global-loading-state-for-many-thunks)
- [291: How do you show a toast for every failed RTK Query request?](#291-how-do-you-show-a-toast-for-every-failed-rtk-query-request)
- [292: How does `createSlice` infer action types from reducers?](#292-how-does-createslice-infer-action-types-from-reducers)
- [293: How do you type `initialState` correctly in a slice?](#293-how-do-you-type-initialstate-correctly-in-a-slice)
- [294: What is `AnyAction` and why should you stop using it?](#294-what-is-anyaction-and-why-should-you-stop-using-it)
- [295: What is `PayloadActionCreator`?](#295-what-is-payloadactioncreator)
- [296: What is `ThunkDispatch`?](#296-what-is-thunkdispatch)
- [297: How do you keep request status for each item separately?](#297-how-do-you-keep-request-status-for-each-item-separately)
- [298: How do you make a slice state persist to `localStorage` without a library?](#298-how-do-you-make-a-slice-state-persist-to-localstorage-without-a-library)
- [299: What is the difference between `createAsyncThunk` returning a value and calling `fulfillWithValue`?](#299-what-is-the-difference-between-createasyncthunk-returning-a-value-and-calling-fulfillwithvalue)
- [300: How do you handle optimistic updates for a list and a detail query at the same time?](#300-how-do-you-handle-optimistic-updates-for-a-list-and-a-detail-query-at-the-same-time)

### Advanced Questions (301-450)

- [301: How is the RTK Query cache stored in the Redux state?](#301-how-is-the-rtk-query-cache-stored-in-the-redux-state)
- [302: How does RTK Query decide when to remove cached data?](#302-how-does-rtk-query-decide-when-to-remove-cached-data)
- [303: What happens step by step when a component calls `useGetPostQuery(5)`?](#303-what-happens-step-by-step-when-a-component-calls-usegetpostquery5)
- [304: How do you handle streaming updates (websockets) with RTK Query?](#304-how-do-you-handle-streaming-updates-websockets-with-rtk-query)
- [305: What are `cacheDataLoaded` and `cacheEntryRemoved`?](#305-what-are-cachedataloaded-and-cacheentryremoved)
- [306: What is the difference between `updateCachedData` and `api.util.updateQueryData`?](#306-what-is-the-difference-between-updatecacheddata-and-apiutilupdatequerydata)
- [307: How do you refresh an expired token automatically in RTK Query?](#307-how-do-you-refresh-an-expired-token-automatically-in-rtk-query)
- [308: How do you call two different backends from one API?](#308-how-do-you-call-two-different-backends-from-one-api)
- [309: How do you use RTK Query with GraphQL?](#309-how-do-you-use-rtk-query-with-graphql)
- [310: What is `buildCreateApi` and when do you need it?](#310-what-is-buildcreateapi-and-when-do-you-need-it)
- [311: What happens if `injectEndpoints` adds an endpoint name that already exists?](#311-what-happens-if-injectendpoints-adds-an-endpoint-name-that-already-exists)
- [312: How do you code split both reducers and API endpoints for a lazy route?](#312-how-do-you-code-split-both-reducers-and-api-endpoints-for-a-lazy-route)
- [313: What is `createDynamicMiddleware`?](#313-what-is-createdynamicmiddleware)
- [314: How do you use dynamic middleware from a React component?](#314-how-do-you-use-dynamic-middleware-from-a-react-component)
- [315: What does `listenerApi.fork` do?](#315-what-does-listenerapifork-do)
- [316: What is `autoJoin` in `fork`?](#316-what-is-autojoin-in-fork)
- [317: What is a `TaskAbortError`?](#317-what-is-a-taskaborterror)
- [318: How are errors in listener effects handled?](#318-how-are-errors-in-listener-effects-handled)
- [319: What are the limits of `getOriginalState`?](#319-what-are-the-limits-of-getoriginalstate)
- [320: How do you make a listener run only once?](#320-how-do-you-make-a-listener-run-only-once)
- [321: How do you write a long-running workflow with the listener middleware?](#321-how-do-you-write-a-long-running-workflow-with-the-listener-middleware)
- [322: How do you throttle with the listener middleware?](#322-how-do-you-throttle-with-the-listener-middleware)
- [323: How do Redux-Saga effects map to the listener middleware?](#323-how-do-redux-saga-effects-map-to-the-listener-middleware)
- [324: How do you fetch RTK Query data on the server for SSR?](#324-how-do-you-fetch-rtk-query-data-on-the-server-for-ssr)
- [325: What is `extractRehydrationInfo`?](#325-what-is-extractrehydrationinfo)
- [326: Should you persist the RTK Query cache with `redux-persist`?](#326-should-you-persist-the-rtk-query-cache-with-redux-persist)
- [327: How do you build bidirectional infinite scrolling with a page limit?](#327-how-do-you-build-bidirectional-infinite-scrolling-with-a-page-limit)
- [328: How do you use cursor-based pagination with infinite queries?](#328-how-do-you-use-cursor-based-pagination-with-infinite-queries)
- [329: What happens when an infinite query is refetched or invalidated?](#329-what-happens-when-an-infinite-query-is-refetched-or-invalidated)
- [330: How was infinite scroll done before infinite queries existed?](#330-how-was-infinite-scroll-done-before-infinite-queries-existed)
- [331: When would you write a custom `serializeQueryArgs`?](#331-when-would-you-write-a-custom-serializequeryargs)
- [332: What does `forceRefetch` do?](#332-what-does-forcerefetch-do)
- [333: How do you combine optimistic updates with invalidation as a safety net?](#333-how-do-you-combine-optimistic-updates-with-invalidation-as-a-safety-net)
- [334: What is `patchQueryData`?](#334-what-is-patchquerydata)
- [335: What is the `updateProvided` argument of `updateQueryData`?](#335-what-is-the-updateprovided-argument-of-updatequerydata)
- [336: What is `api.util.selectInvalidatedBy`?](#336-what-is-apiutilselectinvalidatedby)
- [337: What is `api.util.selectCachedArgsForQuery`?](#337-what-is-apiutilselectcachedargsforquery)
- [338: Is the RTK Query cache normalized?](#338-is-the-rtk-query-cache-normalized)
- [339: What is the difference between `onQueryStarted` and `onCacheEntryAdded`?](#339-what-is-the-difference-between-onquerystarted-and-oncacheentryadded)
- [340: What should you know about memory with `weakMapMemoize`?](#340-what-should-you-know-about-memory-with-weakmapmemoize)
- [341: How do you avoid re-rendering every row when one item in an RTK Query list changes?](#341-how-do-you-avoid-re-rendering-every-row-when-one-item-in-an-rtk-query-list-changes)
- [342: How do you mark your own actions as low priority for the `autoBatchEnhancer`?](#342-how-do-you-mark-your-own-actions-as-low-priority-for-the-autobatchenhancer)
- [343: How do you deal with slow dev checks in a large app?](#343-how-do-you-deal-with-slow-dev-checks-in-a-large-app)
- [344: How do you keep Immer fast in reducers?](#344-how-do-you-keep-immer-fast-in-reducers)
- [345: Does Immer freeze the state, and can you turn that off?](#345-does-immer-freeze-the-state-and-can-you-turn-that-off)
- [346: How do you type a custom base query?](#346-how-do-you-type-a-custom-base-query)
- [347: How do you safely narrow errors from RTK Query and thunks?](#347-how-do-you-safely-narrow-errors-from-rtk-query-and-thunks)
- [348: How do you type a wrapper around an RTK Query hook?](#348-how-do-you-type-a-wrapper-around-an-rtk-query-hook)
- [349: How do you type a middleware that changes what `dispatch` accepts or returns?](#349-how-do-you-type-a-middleware-that-changes-what-dispatch-accepts-or-returns)
- [350: How do you give listeners access to services, and type them?](#350-how-do-you-give-listeners-access-to-services-and-type-them)
- [351: How do you update every cached list entry of an endpoint after a change?](#351-how-do-you-update-every-cached-list-entry-of-an-endpoint-after-a-change)
- [352: How do you give non-React code, like an axios interceptor, access to the store?](#352-how-do-you-give-non-react-code-like-an-axios-interceptor-access-to-the-store)
- [353: How do you handle a 401 globally with RTK Query?](#353-how-do-you-handle-a-401-globally-with-rtk-query)
- [354: How do you cancel the previous `createAsyncThunk` call when a new one starts?](#354-how-do-you-cancel-the-previous-createasyncthunk-call-when-a-new-one-starts)
- [355: How does React Strict Mode affect thunks and RTK Query in development?](#355-how-does-react-strict-mode-affect-thunks-and-rtk-query-in-development)
- [356: How does `useSelector` work internally?](#356-how-does-useselector-work-internally)
- [357: Why doesn't the React-Redux `Provider` re-render every component on each state change?](#357-why-doesnt-the-react-redux-provider-re-render-every-component-on-each-state-change)
- [358: How do you hot reload reducers?](#358-how-do-you-hot-reload-reducers)
- [359: What is `buildCreateSlice` for besides async thunks?](#359-what-is-buildcreateslice-for-besides-async-thunks)
- [360: How do selectors work with slices that might not be injected yet?](#360-how-do-selectors-work-with-slices-that-might-not-be-injected-yet)
- [361: Are selectors in `createSlice.selectors` memoized?](#361-are-selectors-in-createsliceselectors-memoized)
- [362: How do you keep the Redux DevTools fast with large state or many actions?](#362-how-do-you-keep-the-redux-devtools-fast-with-large-state-or-many-actions)
- [363: Why do Redux errors in production look like "Minified Redux error #N"?](#363-why-do-redux-errors-in-production-look-like-minified-redux-error-n)
- [364: How does Redux Toolkit's packaging affect bundle size?](#364-how-does-redux-toolkits-packaging-affect-bundle-size)
- [365: How do you use RTK Query with Angular, Vue or Svelte?](#365-how-do-you-use-rtk-query-with-angular-vue-or-svelte)
- [366: Should you have one `createApi` or many?](#366-should-you-have-one-createapi-or-many)
- [367: Can a mutation invalidate tags only when it succeeds?](#367-can-a-mutation-invalidate-tags-only-when-it-succeeds)
- [368: How does `invalidationBehavior: 'delayed'` interact with optimistic updates?](#368-how-does-invalidationbehavior-delayed-interact-with-optimistic-updates)
- [369: How do `keepUnusedDataFor` and `refetchOnMountOrArgChange` interact?](#369-how-do-keepunuseddatafor-and-refetchonmountorargchange-interact)
- [370: How do you set up `refetchOnFocus` and `refetchOnReconnect` in React Native?](#370-how-do-you-set-up-refetchonfocus-and-refetchonreconnect-in-react-native)
- [371: Can you cancel an in-flight RTK Query request?](#371-can-you-cancel-an-in-flight-rtk-query-request)
- [372: How do you support cancellation in a `queryFn`?](#372-how-do-you-support-cancellation-in-a-queryfn)
- [373: How would you design authentication with RTK and RTK Query?](#373-how-would-you-design-authentication-with-rtk-and-rtk-query)
- [374: How do you fully reset the app state on logout, including RTK Query?](#374-how-do-you-fully-reset-the-app-state-on-logout-including-rtk-query)
- [375: How do you render a large list from Redux efficiently?](#375-how-do-you-render-a-large-list-from-redux-efficiently)
- [376: What does a `sortComparer` cost in an entity adapter?](#376-what-does-a-sortcomparer-cost-in-an-entity-adapter)
- [377: How do you memoize a selector with arguments when many components use different arguments?](#377-how-do-you-memoize-a-selector-with-arguments-when-many-components-use-different-arguments)
- [378: How would you implement undo/redo with Redux Toolkit?](#378-how-would-you-implement-undoredo-with-redux-toolkit)
- [379: How do you write a custom store enhancer?](#379-how-do-you-write-a-custom-store-enhancer)
- [380: Does middleware order matter in RTK, and what's a good order?](#380-does-middleware-order-matter-in-rtk-and-whats-a-good-order)
- [381: How do you update several RTK Query cache entries from one websocket message?](#381-how-do-you-update-several-rtk-query-cache-entries-from-one-websocket-message)
- [382: How do you do an optimistic create when the server assigns the ID?](#382-how-do-you-do-an-optimistic-create-when-the-server-assigns-the-id)
- [383: How do you replace a temporary ID in an entity adapter?](#383-how-do-you-replace-a-temporary-id-in-an-entity-adapter)
- [384: How do you update the cache of an infinite query?](#384-how-do-you-update-the-cache-of-an-infinite-query)
- [385: When should server data live in a slice instead of RTK Query?](#385-when-should-server-data-live-in-a-slice-instead-of-rtk-query)
- [386: How do you combine UI state in slices with RTK Query?](#386-how-do-you-combine-ui-state-in-slices-with-rtk-query)
- [387: How can several micro-frontends share Redux?](#387-how-can-several-micro-frontends-share-redux)
- [388: What security issues should you keep in mind with Redux?](#388-what-security-issues-should-you-keep-in-mind-with-redux)
- [389: Why can you lose error information in `createAsyncThunk` and how do you avoid it?](#389-why-can-you-lose-error-information-in-createasyncthunk-and-how-do-you-avoid-it)
- [390: What does a thunk return when `condition` cancels it?](#390-what-does-a-thunk-return-when-condition-cancels-it)
- [391: How do you add a timeout to `createAsyncThunk`?](#391-how-do-you-add-a-timeout-to-createasyncthunk)
- [392: How do you set a timeout for one RTK Query endpoint?](#392-how-do-you-set-a-timeout-for-one-rtk-query-endpoint)
- [393: How do you use `fetchBaseQuery` during SSR?](#393-how-do-you-use-fetchbasequery-during-ssr)
- [394: What are `getRunningQueryThunk` and `getRunningMutationsThunk`?](#394-what-are-getrunningquerythunk-and-getrunningmutationsthunk)
- [395: How do you keep tests isolated when using RTK Query?](#395-how-do-you-keep-tests-isolated-when-using-rtk-query)
- [396: How do you test the listener middleware?](#396-how-do-you-test-the-listener-middleware)
- [397: How do you test an RTK Query hook directly?](#397-how-do-you-test-an-rtk-query-hook-directly)
- [398: What are common problems when testing RTK Query with MSW in Node?](#398-what-are-common-problems-when-testing-rtk-query-with-msw-in-node)
- [399: How do you type `preloadedState` when using lazy-loaded slices?](#399-how-do-you-type-preloadedstate-when-using-lazy-loaded-slices)
- [400: Can you nest `combineSlices`?](#400-can-you-nest-combineslices)
- [401: Does RTK Query support React Suspense?](#401-does-rtk-query-support-react-suspense)
- [402: Can you use Redux in React Server Components?](#402-can-you-use-redux-in-react-server-components)
- [403: How do you implement polling with backoff using a listener?](#403-how-do-you-implement-polling-with-backoff-using-a-listener)
- [404: How do you manage a websocket connection that depends on login state?](#404-how-do-you-manage-a-websocket-connection-that-depends-on-login-state)
- [405: How do you sync state between browser tabs?](#405-how-do-you-sync-state-between-browser-tabs)
- [406: How would you build an offline queue for mutations?](#406-how-would-you-build-an-offline-queue-for-mutations)
- [407: How do you handle large binary data like images or files with Redux?](#407-how-do-you-handle-large-binary-data-like-images-or-files-with-redux)
- [408: How do you build denormalized view data from normalized state efficiently?](#408-how-do-you-build-denormalized-view-data-from-normalized-state-efficiently)
- [409: What is `createStructuredSelector`?](#409-what-is-createstructuredselector)
- [410: How do you check whether a memoized selector is working?](#410-how-do-you-check-whether-a-memoized-selector-is-working)
- [411: What is the difference between `memoize` and `argsMemoize` in Reselect 5?](#411-what-is-the-difference-between-memoize-and-argsmemoize-in-reselect-5)
- [412: What is the difference between `refetch` and `invalidateTags`?](#412-what-is-the-difference-between-refetch-and-invalidatetags)
- [413: What happens when several components subscribe to the same query with different options?](#413-what-happens-when-several-components-subscribe-to-the-same-query-with-different-options)
- [414: When should you use `upsertQueryEntries` instead of `upsertQueryData`?](#414-when-should-you-use-upsertqueryentries-instead-of-upsertquerydata)
- [415: How do you write `providesTags` that work even when the result is empty or failed?](#415-how-do-you-write-providestags-that-work-even-when-the-result-is-empty-or-failed)
- [416: What happens to a mutation if the component unmounts before it finishes?](#416-what-happens-to-a-mutation-if-the-component-unmounts-before-it-finishes)
- [417: Is `keepUnusedDataFor: Infinity` a good idea?](#417-is-keepunuseddatafor-infinity-a-good-idea)
- [418: How do you use RTK Query with React Router data loaders?](#418-how-do-you-use-rtk-query-with-react-router-data-loaders)
- [419: How would you organize error handling in a large RTK app?](#419-how-would-you-organize-error-handling-in-a-large-rtk-app)
- [420: How do you show server validation errors from a mutation in a form?](#420-how-do-you-show-server-validation-errors-from-a-mutation-in-a-form)
- [421: What naming conventions work well for actions?](#421-what-naming-conventions-work-well-for-actions)
- [422: How can you use action replays in tests?](#422-how-can-you-use-action-replays-in-tests)
- [423: When is Redux Toolkit not a good fit?](#423-when-is-redux-toolkit-not-a-good-fit)
- [424: How does `createSlice` generate actions internally?](#424-how-does-createslice-generate-actions-internally)
- [425: How does `createAsyncThunk` work internally?](#425-how-does-createasyncthunk-work-internally)
- [426: How does Immer's `produce` work?](#426-how-does-immers-produce-work)
- [427: How does the middleware chain get built?](#427-how-does-the-middleware-chain-get-built)
- [428: How is the thunk middleware implemented?](#428-how-is-the-thunk-middleware-implemented)
- [429: Why can't you dispatch while middleware is being set up?](#429-why-cant-you-dispatch-while-middleware-is-being-set-up)
- [430: Why does purity of reducers matter so much?](#430-why-does-purity-of-reducers-matter-so-much)
- [431: Where should you generate random IDs or timestamps?](#431-where-should-you-generate-random-ids-or-timestamps)
- [432: What issues can RTK 2's ESM packaging cause in Jest?](#432-what-issues-can-rtk-2s-esm-packaging-cause-in-jest)
- [433: What TypeScript settings does RTK 2 need?](#433-what-typescript-settings-does-rtk-2-need)
- [434: What should you check when upgrading from RTK 1.x to 2.x?](#434-what-should-you-check-when-upgrading-from-rtk-1x-to-2x)
- [435: What codemods are available for the RTK 2 upgrade?](#435-what-codemods-are-available-for-the-rtk-2-upgrade)
- [436: Are the functions returned by RTK Query hooks stable?](#436-are-the-functions-returned-by-rtk-query-hooks-stable)
- [437: How do you structure Redux in a large monorepo with feature packages?](#437-how-do-you-structure-redux-in-a-large-monorepo-with-feature-packages)
- [438: How do you log Redux actions to an error tracking tool?](#438-how-do-you-log-redux-actions-to-an-error-tracking-tool)
- [439: How do you find performance problems in a Redux app?](#439-how-do-you-find-performance-problems-in-a-redux-app)
- [440: How do you choose between a thunk, a listener and RTK Query lifecycle callbacks?](#440-how-do-you-choose-between-a-thunk-a-listener-and-rtk-query-lifecycle-callbacks)
- [441: How would you design the state for a project management app?](#441-how-would-you-design-the-state-for-a-project-management-app)
- [442: How do you keep cached data separate per tenant or workspace?](#442-how-do-you-keep-cached-data-separate-per-tenant-or-workspace)
- [443: How do you invalidate tags based on the mutation response?](#443-how-do-you-invalidate-tags-based-on-the-mutation-response)
- [444: How do you wait for a specific running query, for example before a navigation?](#444-how-do-you-wait-for-a-specific-running-query-for-example-before-a-navigation)
- [445: How do you use entity adapter selectors in `createSlice.selectors`?](#445-how-do-you-use-entity-adapter-selectors-in-createsliceselectors)
- [446: How do you write a reusable helper for list tags?](#446-how-do-you-write-a-reusable-helper-for-list-tags)
- [447: What are good rules for the shape of the root state?](#447-what-are-good-rules-for-the-shape-of-the-root-state)
- [448: Should form state go into Redux?](#448-should-form-state-go-into-redux)
- [449: How would you move data fetching from sagas to RTK Query step by step?](#449-how-would-you-move-data-fetching-from-sagas-to-rtk-query-step-by-step)
- [450: Walk through what happens when you dispatch a slice action in an RTK store.](#450-walk-through-what-happens-when-you-dispatch-a-slice-action-in-an-rtk-store)

---

## Easy Questions

### 1: What is Redux Toolkit?

Redux Toolkit (RTK) is the official package for writing Redux logic. It wraps the Redux core and adds helpers that remove most of the boilerplate people used to write by hand: store setup, action types, action creators, immutable updates, async logic and data fetching.

The package name is `@reduxjs/toolkit`. The current major version is 2.x, which is built on Redux 5, Reselect 5, Immer 10 and Redux Thunk 3.

### 2: What problems does Redux Toolkit solve?

Plain Redux had three common complaints:

- Setting up a store took too many steps (combine reducers, apply middleware, add DevTools).
- You had to write a lot of code: action type constants, action creators, switch statements and spread operators for immutable updates.
- You needed extra packages for common things like async logic, memoized selectors and immutable updates.

RTK gives you `configureStore`, `createSlice`, `createAsyncThunk`, `createEntityAdapter`, `createSelector` and RTK Query, so most of that work is done for you with good defaults.

### 3: How do you install Redux Toolkit?

```bash
npm install @reduxjs/toolkit react-redux
```

`react-redux` is only needed if you use React. To start a new project with a template:

```bash
npx degit reduxjs/redux-templates/packages/vite-template-redux my-app
```

### 4: What are the main APIs in Redux Toolkit?

- `configureStore` - creates the store with good defaults.
- `createSlice` - creates a reducer and its action creators together.
- `createAction` and `createReducer` - lower level helpers for actions and reducers.
- `createAsyncThunk` - handles async logic and dispatches pending/fulfilled/rejected actions.
- `createEntityAdapter` - helpers for normalized collections of items.
- `createSelector` - memoized selectors (re-exported from Reselect).
- `createListenerMiddleware` - run side effects in response to actions.
- `combineSlices` and `createDynamicMiddleware` - code splitting helpers.
- RTK Query (`createApi`, `fetchBaseQuery`) - data fetching and caching.

### 5: Is Redux Toolkit a replacement for Redux?

No. Redux Toolkit uses the Redux core under the hood. It is the recommended way to write Redux code. The Redux team says that all new Redux code should be written with RTK, and the old `createStore` from the core is marked as deprecated to push people toward `configureStore`.

### 6: What is a Redux store?

The store is the object that holds the whole state of your app. It has three main methods:

- `getState()` - returns the current state.
- `dispatch(action)` - sends an action to update the state.
- `subscribe(listener)` - registers a callback that runs after every dispatch.

There is normally only one store per app.

### 7: How do you create a store with Redux Toolkit?

Use `configureStore` and pass it your reducers.

```ts
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./features/counter/counterSlice";
import todosReducer from "./features/todos/todosSlice";

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    todos: todosReducer,
  },
});
```

When you pass an object to `reducer`, `configureStore` calls `combineReducers` for you.

### 8: What does `configureStore` set up by default?

- Combines your slice reducers if you pass an object.
- Adds the default middleware: `redux-thunk`, plus the immutability check, serializability check and action creator check in development.
- Turns on the Redux DevTools Extension connection.
- Adds the `autoBatchEnhancer` (since RTK 2.0).

You get all of this with one function call and no extra config.

### 9: What is a slice?

A slice is the part of the Redux state for one feature, together with the reducer logic and actions for that feature. For example, `state.todos` and `state.user` are two slices. The name comes from the idea of slicing the root state object into pieces.

### 10: What does `createSlice` do?

`createSlice` takes a name, an initial state and an object of reducer functions. It returns a slice object with:

- `reducer` - the slice reducer.
- `actions` - action creators, one per reducer.
- `caseReducers`, `getInitialState`, `selectors` and a few other fields.

```ts
import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface CounterState {
  value: number;
}

const initialState: CounterState = { value: 0 };

const counterSlice = createSlice({
  name: "counter",
  initialState,
  reducers: {
    increment(state) {
      state.value += 1;
    },
    decrement(state) {
      state.value -= 1;
    },
    incrementByAmount(state, action: PayloadAction<number>) {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;
export default counterSlice.reducer;
```

### 11: What is the `name` option in `createSlice` used for?

It is used as the prefix for the generated action types. With `name: 'counter'` and a reducer called `increment`, the action type becomes `'counter/increment'`. It is also the default `reducerPath` that slice selectors use to find the slice state in the root state.

### 12: What is `initialState` in a slice?

It is the value the slice state starts with. When the store is created, Redux dispatches an internal init action and each reducer returns its initial state. You can pass a plain value or a function that returns the value (lazy initializer).

```ts
const slice = createSlice({
  name: "settings",
  initialState: () => ({ theme: localStorage.getItem("theme") ?? "light" }),
  reducers: {},
});
```

### 13: What is an action in Redux?

An action is a plain object that describes something that happened. It must have a `type` field, which must be a string. Most actions also have a `payload` field with data.

```ts
{ type: 'todos/todoAdded', payload: { id: '1', text: 'Buy milk' } }
```

### 14: What is an action creator?

An action creator is a function that returns an action object. `createSlice` and `createAction` generate them for you.

```ts
increment(); // { type: 'counter/increment', payload: undefined }
incrementByAmount(5); // { type: 'counter/incrementByAmount', payload: 5 }
```

### 15: What is `payload`?

`payload` is the conventional field name for the data that comes with an action. RTK action creators put the first argument you pass into `action.payload`.

### 16: What is `PayloadAction`?

`PayloadAction<P>` is a TypeScript type for an action with a payload of type `P`. You use it to type the `action` argument in slice reducers.

```ts
addTodo(state, action: PayloadAction<{ id: string; text: string }>) {
  state.push({ ...action.payload, completed: false })
}
```

It also accepts optional generics for the type string, `meta` and `error`: `PayloadAction<P, T, M, E>`.

### 17: What is a reducer?

A reducer is a function that takes the current state and an action, and returns the next state: `(state, action) => newState`. Reducers decide how state changes in response to actions.

### 18: What rules must a reducer follow?

- Only calculate the new state from `state` and `action`.
- Do not modify the existing state directly (immutable updates). In RTK, Immer handles this for you.
- No side effects: no API calls, no timers, no random values, no logging that affects behavior.

### 19: How can RTK reducers "mutate" state if Redux requires immutable updates?

`createSlice` and `createReducer` use Immer. Immer gives your reducer a draft object. You write mutating code on the draft, and Immer tracks the changes and produces a new immutable state at the end. The original state is never changed.

```ts
todoToggled(state, action: PayloadAction<string>) {
  const todo = state.find((t) => t.id === action.payload)
  if (todo) todo.completed = !todo.completed
}
```

This only works inside `createSlice` and `createReducer`. Mutating state in a plain reducer or a component is still a bug.

### 20: Can you return a new state from an RTK reducer instead of mutating it?

Yes. You can either mutate the draft or return a new value. Both are fine.

```ts
reducers: {
  reset() {
    return initialState
  },
  removeCompleted(state) {
    return state.filter((todo) => !todo.completed)
  },
}
```

### 21: Can you mutate the draft and also return a value in the same reducer?

No. Immer throws an error if you modify the draft and also return a different value. Pick one. A common mistake is an arrow function that implicitly returns the result of an assignment:

```ts
// Wrong: returns the result of the assignment
setValue: (state, action) => (state.value = action.payload);

// Right: wrap in braces so nothing is returned
setValue: (state, action) => {
  state.value = action.payload;
};
```

### 22: How do you reset a slice to its initial state?

Return the initial state from a reducer.

```ts
reducers: {
  reset: () => initialState,
}
```

Writing `state = initialState` does not work, because it only reassigns the local variable and Immer never sees a change.

### 23: How do you handle a slice whose state is a primitive value like a number?

Primitives cannot be mutated, so you must return the new value.

```ts
const countSlice = createSlice({
  name: "count",
  initialState: 0,
  reducers: {
    increment: (state) => state + 1,
    set: (_state, action: PayloadAction<number>) => action.payload,
  },
});
```

### 24: What is `dispatch`?

`dispatch` is the store method you call to send an action. The store runs the root reducer with the current state and the action, saves the result as the new state, and notifies subscribers.

```ts
store.dispatch(increment());
```

### 25: What is `getState`?

`store.getState()` returns the current state tree. In components you usually read state with `useSelector` instead. In thunks you get `getState` as the second argument.

### 26: What is the `Provider` component?

`Provider` comes from `react-redux`. It puts the store into React context so any component in the tree can read state and dispatch actions.

```tsx
import { Provider } from "react-redux";
import { store } from "./app/store";

createRoot(document.getElementById("root")!).render(
  <Provider store={store}>
    <App />
  </Provider>,
);
```

### 27: What is `useSelector`?

A React-Redux hook that reads a value from the store state. The component re-renders when the selected value changes (compared with `===` by default).

```tsx
const count = useSelector((state: RootState) => state.counter.value);
```

### 28: What is `useDispatch`?

A React-Redux hook that returns the store's `dispatch` function.

```tsx
const dispatch = useDispatch();
return <button onClick={() => dispatch(increment())}>+</button>;
```

### 29: What is `useStore`?

It returns the store object itself. You rarely need it in components, because reading state with `store.getState()` does not subscribe the component to updates. It is sometimes used for one-time reads or for passing the store to non-React code.

### 30: Show a full counter example with Redux Toolkit and React.

```tsx
// counterSlice.ts
import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment(state) {
      state.value += 1;
    },
    decrement(state) {
      state.value -= 1;
    },
  },
});

export const { increment, decrement } = counterSlice.actions;
export default counterSlice.reducer;

// store.ts
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterSlice";

export const store = configureStore({ reducer: { counter: counterReducer } });
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Counter.tsx
import { useAppDispatch, useAppSelector } from "./hooks";
import { increment, decrement } from "./counterSlice";

export function Counter() {
  const count = useAppSelector((state) => state.counter.value);
  const dispatch = useAppDispatch();

  return (
    <div>
      <button onClick={() => dispatch(decrement())}>-</button>
      <span>{count}</span>
      <button onClick={() => dispatch(increment())}>+</button>
    </div>
  );
}
```

### 31: What is a selector?

A selector is a function that takes the Redux state and returns some piece of it, or a value derived from it.

```ts
export const selectTodos = (state: RootState) => state.todos;
export const selectCompletedCount = (state: RootState) =>
  state.todos.filter((t) => t.completed).length;
```

Keeping selectors in the slice file means components don't need to know the shape of the state.

### 32: Why define selectors in the slice file instead of writing them inline in components?

- If the state shape changes, you only update the selector, not every component.
- Selectors can be reused and tested on their own.
- Derived values can be memoized in one place.

Inline selectors are fine for very simple reads, but named selectors scale better.

### 33: How do you combine multiple slices into one store?

Pass an object of reducers to `configureStore`. Each key becomes a top-level key in the state.

```ts
const store = configureStore({
  reducer: {
    auth: authReducer,
    posts: postsReducer,
    comments: commentsReducer,
  },
});
// state shape: { auth, posts, comments }
```

### 34: What is `combineReducers` and do you still need it?

`combineReducers` builds one root reducer out of several slice reducers. `configureStore` calls it for you when you pass an object, so you only need it yourself when you want to build the root reducer separately, for example to wrap it for a "reset on logout" feature or to nest reducers. RTK re-exports it, so you can import it from `@reduxjs/toolkit`. RTK 2.0 also added `combineSlices`, which can inject slices later.

### 35: How do you get the `RootState` type?

Infer it from the store.

```ts
export const store = configureStore({ reducer: { counter: counterReducer } });
export type RootState = ReturnType<typeof store.getState>;
```

Inferring the type means it updates automatically when you add a slice.

### 36: How do you get the `AppDispatch` type and why do you need it?

```ts
export type AppDispatch = typeof store.dispatch;
```

The default `Dispatch` type does not know about thunks. `AppDispatch` includes the types added by middleware, so `dispatch(someThunk())` is typed correctly and `dispatch(...).unwrap()` works.

### 37: How do you create typed React-Redux hooks?

Since React-Redux 9 you can use `.withTypes()`:

```ts
// hooks.ts
import { useDispatch, useSelector, useStore } from "react-redux";
import type { AppDispatch, AppStore, RootState } from "./store";

export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
export const useAppStore = useStore.withTypes<AppStore>();
```

Use these hooks across the app instead of the plain ones so you don't have to type `state` every time.

### 38: What are the Redux DevTools?

A browser extension that shows every dispatched action, the state after each action, the diff between states, and lets you "time travel" by jumping between past states. `configureStore` connects to it automatically.

### 39: How do you turn off DevTools in production?

```ts
const store = configureStore({
  reducer: rootReducer,
  devTools: process.env.NODE_ENV !== "production",
});
```

You can also pass an options object, for example `devTools: { name: 'MyApp', maxAge: 50 }`.

### 40: What is middleware in Redux?

Middleware sits between `dispatch` and the reducer. Each dispatched action passes through the middleware chain before it reaches the reducer. Middleware can log, change, delay, stop actions or run side effects. Thunks, the listener middleware and RTK Query all work as middleware.

```ts
const logger: Middleware = (storeApi) => (next) => (action) => {
  console.log("dispatching", action);
  const result = next(action);
  console.log("next state", storeApi.getState());
  return result;
};
```

### 41: Which middleware does `configureStore` add by default?

- `thunk` - always.
- Immutability check - development only.
- Serializability check - development only.
- Action creator check - development only (warns if you dispatch an action creator instead of calling it).

The dev checks are removed from production builds.

### 42: How do you add your own middleware to the store?

Pass a callback to `middleware`, call `getDefaultMiddleware()` and add yours with `.concat()` or `.prepend()`.

```ts
const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
});
```

In RTK 2.0 the `middleware` option must be a callback. The old array form was removed.

### 43: What is the difference between `concat` and `prepend` on the default middleware?

`getDefaultMiddleware()` returns a `Tuple`. `concat` adds middleware after the defaults, `prepend` adds them before. Order matters because each middleware sees an action before the ones after it. The listener middleware is usually prepended so it runs before others like the serializable check.

### 44: What is a thunk?

A thunk is a function you dispatch instead of an action object. The thunk middleware calls it with `dispatch` and `getState`, so you can run async code and dispatch actions when you are done.

```ts
export const fetchUser =
  (id: string): AppThunk =>
  async (dispatch) => {
    dispatch(userLoading());
    const res = await fetch(`/api/users/${id}`);
    const user = await res.json();
    dispatch(userLoaded(user));
  };
```

### 45: How do you type a thunk manually?

Define an `AppThunk` type in your store file:

```ts
import type { Action, ThunkAction } from "@reduxjs/toolkit";

export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action
>;
```

### 46: What is `createAsyncThunk`?

A helper for async requests. You give it an action type prefix and an async function. It returns a thunk that dispatches `pending` before the call, then `fulfilled` with the result or `rejected` with the error.

```ts
export const fetchTodos = createAsyncThunk("todos/fetchTodos", async () => {
  const res = await fetch("/api/todos");
  return (await res.json()) as Todo[];
});
```

### 47: Which actions does `createAsyncThunk` dispatch?

For a prefix `'todos/fetchTodos'`:

- `todos/fetchTodos/pending` - when the thunk starts.
- `todos/fetchTodos/fulfilled` - when the promise resolves. `action.payload` is the returned value.
- `todos/fetchTodos/rejected` - when it throws or rejects. `action.error` holds a serialized error, and `action.payload` holds the value if you used `rejectWithValue`.

The action creators are available as `fetchTodos.pending`, `fetchTodos.fulfilled` and `fetchTodos.rejected`.

### 48: How do you handle `createAsyncThunk` actions in a slice?

Use `extraReducers` with the builder callback.

```ts
interface TodosState {
  items: Todo[];
  status: "idle" | "loading" | "succeeded" | "failed";
  error: string | null;
}

const initialState: TodosState = { items: [], status: "idle", error: null };

const todosSlice = createSlice({
  name: "todos",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTodos.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.items = action.payload;
      })
      .addCase(fetchTodos.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message ?? "Something went wrong";
      });
  },
});
```

### 49: What is the difference between `reducers` and `extraReducers` in `createSlice`?

- `reducers` defines actions that belong to this slice. RTK generates action creators for them.
- `extraReducers` lets the slice respond to actions defined somewhere else, like thunks, actions from other slices or RTK Query endpoints. No action creators are generated.

### 50: What is the builder callback?

`extraReducers` and `createReducer` take a function that receives a `builder` object. You add handlers with `addCase`, `addMatcher` and `addDefaultCase`. The builder gives correct TypeScript types for each action. In RTK 2.0 the old object syntax (`extraReducers: { [action]: fn }`) was removed, so the builder is the only option.

### 51: What does `builder.addCase` do?

It adds a reducer for one exact action type. You can pass an action creator or a type string.

```ts
builder.addCase(userLoggedOut, () => initialState);
builder.addCase("app/reset", () => initialState);
```

Using the action creator is better because TypeScript infers the action type from it.

### 52: What is a common pattern for tracking loading state?

Use a single `status` field with a string union instead of several booleans:

```ts
status: "idle" | "loading" | "succeeded" | "failed";
```

Booleans like `isLoading` and `isError` can end up in impossible combinations. One status field can only be in one state at a time.

### 53: What is `rejectWithValue`?

A function from the thunk API that lets you reject with your own payload, for example the error body from the server.

```ts
export const login = createAsyncThunk(
  "auth/login",
  async (credentials: Credentials, { rejectWithValue }) => {
    const res = await fetch("/api/login", {
      method: "POST",
      body: JSON.stringify(credentials),
    });
    if (!res.ok) {
      return rejectWithValue(await res.json());
    }
    return res.json();
  },
);
```

In the `rejected` case, the value is in `action.payload`.

### 54: What does `.unwrap()` do on a dispatched thunk?

`dispatch(thunk())` always returns a promise that resolves with the final action, even when the thunk fails. Calling `.unwrap()` returns a promise that resolves with the payload or throws the error, which is easier to use in components.

```tsx
const onSave = async () => {
  try {
    const post = await dispatch(addPost(newPost)).unwrap();
    navigate(`/posts/${post.id}`);
  } catch (err) {
    setError("Failed to save the post");
  }
};
```

### 55: What does `createAction` do?

It creates an action creator for a given type.

```ts
import { createAction } from "@reduxjs/toolkit";

export const userLoggedOut = createAction("auth/userLoggedOut");
export const itemAdded = createAction<{ id: string; name: string }>(
  "cart/itemAdded",
);

itemAdded({ id: "1", name: "Shoes" });
// { type: 'cart/itemAdded', payload: { id: '1', name: 'Shoes' } }

itemAdded.type; // 'cart/itemAdded'
```

### 56: What is a prepare callback?

A prepare callback lets you customize how the action is built from the arguments. It must return an object with `payload`, and can also return `meta` and `error`. It's a good place for generating IDs or timestamps, since reducers must stay pure.

```ts
const todosSlice = createSlice({
  name: "todos",
  initialState: [] as Todo[],
  reducers: {
    todoAdded: {
      reducer(state, action: PayloadAction<Todo>) {
        state.push(action.payload);
      },
      prepare(text: string) {
        return {
          payload: { id: nanoid(), text, completed: false },
        };
      },
    },
  },
});

dispatch(todoAdded("Buy milk"));
```

### 57: What is `nanoid`?

A small function exported by RTK that generates random string IDs. It's handy for client-side IDs in prepare callbacks. It is not cryptographically secure, so don't use it for tokens.

### 58: What is `createReducer`?

A helper to write a reducer with the builder callback and Immer, without creating a slice. It's useful when the action creators are defined elsewhere.

```ts
const increment = createAction("counter/increment");
const incrementBy = createAction<number>("counter/incrementBy");

const counterReducer = createReducer(0, (builder) => {
  builder
    .addCase(increment, (state) => state + 1)
    .addCase(incrementBy, (state, action) => state + action.payload);
});
```

Most of the time `createSlice` is the better choice.

### 59: What is RTK Query?

RTK Query is a data fetching and caching tool included in `@reduxjs/toolkit`. You describe your API endpoints once, and it generates React hooks that fetch data, cache it, track loading and error state, avoid duplicate requests and refetch when data is invalidated. It removes the need to write thunks, loading flags and reducers for server data.

### 60: When should you use RTK Query instead of `createAsyncThunk`?

Use RTK Query when you fetch and cache server data, which covers most API calls in a typical app. Use `createAsyncThunk` when you have async logic that is not really "fetch and cache", for example a multi-step process, or when the result needs to be merged into a slice in a custom way.

### 61: How do you define an API with `createApi`?

```ts
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

interface Post {
  id: number;
  title: string;
  body: string;
}

export const api = createApi({
  reducerPath: "api",
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  endpoints: (build) => ({
    getPosts: build.query<Post[], void>({
      query: () => "posts",
    }),
    getPost: build.query<Post, number>({
      query: (id) => `posts/${id}`,
    }),
    addPost: build.mutation<Post, Omit<Post, "id">>({
      query: (body) => ({ url: "posts", method: "POST", body }),
    }),
  }),
});

export const { useGetPostsQuery, useGetPostQuery, useAddPostMutation } = api;
```

### 62: What is `fetchBaseQuery`?

A small wrapper around `fetch` that RTK Query provides as a default `baseQuery`. It sets the base URL, serializes JSON bodies, parses JSON responses, and returns errors in a standard shape. You can customize headers with `prepareHeaders`.

### 63: What is the difference between a query and a mutation endpoint?

- `build.query` is for reading data. Results are cached by endpoint name plus arguments, and hooks fetch automatically.
- `build.mutation` is for changing data on the server (POST, PUT, PATCH, DELETE). It doesn't run until you call the trigger function, and its results are not cached for reuse.

### 64: How are RTK Query hook names generated?

From the endpoint name: `use` + capitalized name + `Query`, `LazyQuery`, `InfiniteQuery` or `Mutation`.

- `getPosts` query gives `useGetPostsQuery` and `useLazyGetPostsQuery`.
- `addPost` mutation gives `useAddPostMutation`.
- `getFeed` infinite query gives `useGetFeedInfiniteQuery`.

Hooks are only generated when you import `createApi` from `@reduxjs/toolkit/query/react`.

### 65: How do you add an RTK Query API to the store?

Add its reducer under `reducerPath` and add its middleware.

```ts
export const store = configureStore({
  reducer: {
    [api.reducerPath]: api.reducer,
    counter: counterReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(api.middleware),
});
```

The middleware is needed for caching, cache lifetimes, invalidation and polling.

### 66: What is `reducerPath` in `createApi`?

The key in the root state where the API's cache is stored. The default is `'api'`. If you have more than one API, each needs a unique `reducerPath`.

### 67: What does `useQuery` return?

Some of the most used fields:

- `data` - the latest successful result for the current or last arguments.
- `currentData` - the result for the current arguments only.
- `error` - the error, if any.
- `isUninitialized`, `isLoading`, `isFetching`, `isSuccess`, `isError`.
- `refetch` - a function to force a new request.

```tsx
function PostsList() {
  const { data: posts = [], isLoading, isError } = useGetPostsQuery();

  if (isLoading) return <p>Loading...</p>;
  if (isError) return <p>Could not load posts</p>;

  return (
    <ul>
      {posts.map((p) => (
        <li key={p.id}>{p.title}</li>
      ))}
    </ul>
  );
}
```

### 68: What is the difference between `isLoading` and `isFetching`?

- `isLoading` is true only on the first load, when there is no data yet.
- `isFetching` is true whenever a request is in flight, including refetches and argument changes.

Use `isLoading` for a full spinner and `isFetching` for a small "refreshing" indicator over existing data.

### 69: How do you use a mutation hook?

The hook returns a tuple: a trigger function and a result object.

```tsx
function AddPostForm() {
  const [addPost, { isLoading }] = useAddPostMutation();
  const [title, setTitle] = useState("");

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await addPost({ title, body: "" }).unwrap();
      setTitle("");
    } catch (err) {
      console.error("Failed to save post", err);
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <input value={title} onChange={(e) => setTitle(e.target.value)} />
      <button disabled={isLoading}>Save</button>
    </form>
  );
}
```

### 70: What are tags in RTK Query?

Tags connect queries and mutations for automatic refetching. A query says which tags its data "provides", and a mutation says which tags it "invalidates". When a mutation finishes, every cached query that provides one of those tags gets refetched.

```ts
export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  tagTypes: ["Post"],
  endpoints: (build) => ({
    getPosts: build.query<Post[], void>({
      query: () => "posts",
      providesTags: ["Post"],
    }),
    addPost: build.mutation<Post, Partial<Post>>({
      query: (body) => ({ url: "posts", method: "POST", body }),
      invalidatesTags: ["Post"],
    }),
  }),
});
```

### 71: What is `tagTypes` for?

It lists every tag name the API uses. TypeScript checks `providesTags` and `invalidatesTags` against this list, so a typo becomes a type error.

### 72: How do you manually refetch a query?

Call `refetch` from the hook result.

```tsx
const { data, refetch } = useGetPostsQuery()
<button onClick={() => refetch()}>Reload</button>
```

You can also invalidate tags with `dispatch(api.util.invalidateTags(['Post']))`.

### 73: How do you skip a query until some value is ready?

Use the `skip` option or pass `skipToken` as the argument.

```tsx
import { skipToken } from "@reduxjs/toolkit/query/react";

const { data } = useGetUserQuery(userId ?? skipToken);
// or
const { data } = useGetUserQuery(userId!, { skip: !userId });
```

`skipToken` is better with TypeScript because you don't need the `!` assertion.

### 74: What is `keepUnusedDataFor`?

How long, in seconds, RTK Query keeps cached data after the last component using it unmounts. The default is 60 seconds. If a component asks for the same data within that time, it gets the cached result right away.

```ts
getPosts: build.query<Post[], void>({
  query: () => 'posts',
  keepUnusedDataFor: 300,
}),
```

### 75: What is `createEntityAdapter`?

A helper for storing collections of items in a normalized shape `{ ids: [], entities: {} }`. It generates reducer functions for adding, updating and removing items, and selectors for reading them.

```ts
import { createEntityAdapter, createSlice } from "@reduxjs/toolkit";

interface Book {
  id: string;
  title: string;
}

const booksAdapter = createEntityAdapter<Book>();

const booksSlice = createSlice({
  name: "books",
  initialState: booksAdapter.getInitialState(),
  reducers: {
    bookAdded: booksAdapter.addOne,
    booksReceived: booksAdapter.setAll,
  },
});
```

### 76: What is normalized state?

Normalized state stores each item once, in a lookup table keyed by ID, and keeps an array of IDs for ordering.

```ts
{
  ids: ['a', 'b'],
  entities: {
    a: { id: 'a', title: 'First' },
    b: { id: 'b', title: 'Second' },
  },
}
```

Lookups by ID are fast, there is no duplicated data, and updating one item doesn't require searching an array.

### 77: What does `adapter.getInitialState()` return?

An object `{ ids: [], entities: {} }`. You can pass extra fields to add them to the state:

```ts
const initialState = booksAdapter.getInitialState({
  status: "idle" as "idle" | "loading",
  error: null as string | null,
});
// { ids: [], entities: {}, status: 'idle', error: null }
```

### 78: Which CRUD methods does an entity adapter provide?

- `addOne`, `addMany` - add items, skip if the ID already exists.
- `setOne`, `setMany` - add or fully replace items.
- `setAll` - replace all items.
- `removeOne`, `removeMany`, `removeAll`.
- `updateOne`, `updateMany` - shallow update with `{ id, changes }`.
- `upsertOne`, `upsertMany` - add if missing, shallow merge if present.

Each can be used as a case reducer directly or called inside one: `booksAdapter.addOne(state, book)`.

### 79: How do you use the adapter selectors?

`getSelectors` returns `selectIds`, `selectEntities`, `selectAll`, `selectTotal` and `selectById`. Pass a function that picks the slice state from the root state:

```ts
export const {
  selectAll: selectAllBooks,
  selectById: selectBookById,
  selectIds: selectBookIds,
} = booksAdapter.getSelectors((state: RootState) => state.books);

const book = useAppSelector((state) => selectBookById(state, bookId));
```

### 80: What is `sortComparer` in `createEntityAdapter`?

A compare function that keeps the `ids` array sorted. It works like the function you pass to `Array.prototype.sort`.

```ts
const booksAdapter = createEntityAdapter<Book>({
  sortComparer: (a, b) => a.title.localeCompare(b.title),
});
```

`selectAll` will then return items in that order.

### 81: What is `selectId` in `createEntityAdapter`?

A function that tells the adapter which field is the ID. Use it when your items don't have an `id` field.

```ts
const usersAdapter = createEntityAdapter({
  selectId: (user: User) => user.userId,
});
```

### 82: What is `createSelector`?

A function from Reselect, re-exported by RTK, that creates memoized selectors. It takes input selectors and a result function. The result function only runs again when one of the inputs changes.

```ts
import { createSelector } from "@reduxjs/toolkit";

const selectTodos = (state: RootState) => state.todos.items;
const selectFilter = (state: RootState) => state.todos.filter;

export const selectVisibleTodos = createSelector(
  [selectTodos, selectFilter],
  (todos, filter) =>
    filter === "all" ? todos : todos.filter((t) => t.status === filter),
);
```

### 83: Why do selectors need memoization?

`useSelector` re-renders the component when the selector returns a new reference. A selector that uses `filter` or `map` returns a new array every time, so the component would re-render after every action, even unrelated ones. Memoization returns the same array reference until the inputs change.

### 84: Why should Redux state and actions be serializable?

Serializable means plain objects, arrays, strings, numbers, booleans and null. Keeping state serializable makes the DevTools work, allows time travel debugging, lets you persist state to storage and makes behavior predictable. Things like class instances, Promises, functions, Maps, Sets and Dates break those features.

### 85: What does the serializability check middleware do?

In development, it checks every action and the state after each dispatch. If it finds non-serializable values it logs a warning with the path to the value. It is removed in production builds.

### 86: What does the immutability check middleware do?

In development, it detects when state is mutated outside a reducer or between dispatches, for example a component that changes an array from the store. It throws an error pointing to the path that changed. These bugs are hard to find otherwise because Redux depends on reference changes.

### 87: How should you store a date in Redux state?

Store a serializable form, like an ISO string or a timestamp number, and convert it when you display it.

```ts
state.createdAt = new Date().toISOString();
```

### 88: When should you use Redux instead of React Context?

Context is a way to pass a value down the tree. It is not a state manager by itself. Every consumer re-renders when the context value changes. Redux is a better fit when:

- A lot of state is shared across many parts of the app.
- State updates often.
- Update logic is complex.
- You want DevTools, middleware or a clear history of changes.

For a theme or the current user, Context is often enough.

### 89: Should all state go into Redux?

No. Put state in Redux when other parts of the app need it, when it should survive a component unmounting, or when you want to debug it with the DevTools. Form input values, open/closed toggles and hover state usually belong in local component state.

### 90: What folder structure is recommended for Redux Toolkit projects?

Group files by feature:

```
src/
  app/
    store.ts
    hooks.ts
  features/
    todos/
      todosSlice.ts
      TodoList.tsx
    auth/
      authSlice.ts
      LoginForm.tsx
  services/
    api.ts
```

Each feature folder holds its slice, components and tests together.

### 91: What is the "ducks" pattern?

Putting the action types, action creators and reducer for one feature in one file. `createSlice` follows this idea by default: one slice file exports the reducer and the actions.

### 92: What does `actionCreator.match` do?

Every RTK action creator has a `match` method. It checks whether an action has the same type, and works as a TypeScript type guard.

```ts
if (increment.match(action)) {
  // action is typed as the increment action here
}
```

It's useful in custom middleware and listener predicates.

### 93: What is `slice.caseReducers`?

An object with the original reducer functions you wrote in `reducers`. You can call one from another reducer, or test them directly.

```ts
reducers: {
  increment(state) {
    state.value += 1
  },
  incrementTwice(state) {
    counterSlice.caseReducers.increment(state)
    counterSlice.caseReducers.increment(state)
  },
}
```

### 94: What is `slice.getInitialState()`?

A function that returns the initial state of the slice. It's handy in tests and for reset reducers, especially when `initialState` is a lazy function.

### 95: What is `preloadedState`?

An option for `configureStore` to set the initial state of the store, for example from server-rendered data or saved storage. It overrides the reducers' own initial values.

```ts
const store = configureStore({
  reducer: rootReducer,
  preloadedState: { counter: { value: 10 } },
});
```

### 96: Can you use Redux Toolkit without React?

Yes. The core of RTK has no React dependency. You can use it with Vue, Angular, Svelte, vanilla JS or Node.js. RTK Query also works without React if you import from `@reduxjs/toolkit/query` and dispatch `api.endpoints.x.initiate()` yourself.

### 97: What does `store.subscribe` do?

It registers a callback that runs after every dispatched action. It returns a function to unsubscribe. React-Redux uses it internally. You'd use it directly in non-React code.

```ts
const unsubscribe = store.subscribe(() => {
  console.log(store.getState());
});
unsubscribe();
```

### 98: What are the three principles of Redux?

- Single source of truth: the app state lives in one store.
- State is read-only: you change it only by dispatching actions.
- Changes are made with pure functions: reducers calculate the next state without side effects.

### 99: What is one-way data flow in Redux?

1. The UI dispatches an action.
2. The store runs the reducer with the current state and the action.
3. The reducer returns a new state.
4. The store notifies subscribers.
5. Components read the new state and re-render.

Data always moves in one direction, which makes it easier to follow.

### 100: Can you have more than one Redux store?

Technically yes, but it's not recommended. One store with several slices is the standard setup. Multiple stores make DevTools, middleware and cross-feature logic harder. A rare exception is a library or micro frontend that needs fully separate state.

### 101: What is the thunk "extra argument"?

A value you pass when configuring the thunk middleware. Every thunk then receives it as the third argument, and `createAsyncThunk` exposes it as `extra`. It's useful for injecting an API client so it can be swapped in tests.

```ts
const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      thunk: { extraArgument: { apiClient } },
    }),
});
```

### 102: What does `dispatch` return when you dispatch a thunk?

Whatever the thunk function returns. For `createAsyncThunk`, it's a promise of the final action. That promise also has `.unwrap()`, `.abort()`, `.arg` and `.requestId`.

### 103: What is `current` from Immer and why is it exported by RTK?

Logging a draft in a reducer shows a Proxy, which is hard to read. `current(draft)` returns a plain copy of the draft's current value.

```ts
import { current } from '@reduxjs/toolkit'

todoToggled(state, action) {
  console.log(current(state))
}
```

### 104: What does `isAnyOf` do?

It builds a matcher that matches an action if it matches any of the given action creators. Use it with `addMatcher`.

```ts
builder.addMatcher(isAnyOf(todoAdded, todoDeleted, todoToggled), (state) => {
  state.lastUpdated = Date.now();
});
```

### 105: Why is `createStore` deprecated?

The Redux core marked `createStore` as deprecated to tell people to use `configureStore` from RTK. It still works, and nothing will break. You can import `legacy_createStore` to avoid the warning. The deprecation is a visual hint in editors, not a removal.

### 106: What were the main changes in Redux Toolkit 2.0?

- The object syntax for `createSlice.extraReducers` and `createReducer` was removed. Use the builder.
- `configureStore.middleware` and `enhancers` must be callbacks.
- Action types must be strings.
- `AnyAction` is deprecated in favor of `UnknownAction`.
- New APIs: `combineSlices`, `createDynamicMiddleware`, slice `selectors`, the `create` callback for reducers, `buildCreateSlice`.
- Packaging changed to modern ESM with a CJS fallback.
- Built on Redux 5, Reselect 5, Immer 10 and Redux Thunk 3.
- `autoBatchEnhancer` is on by default.
- RTK Query's default `invalidationBehavior` became `'delayed'`.

### 107: Why must action types be strings?

Redux 5 throws an error if `action.type` is not a string. String types are serializable, show up properly in the DevTools and are easy to compare. Symbols and numbers were technically allowed before but caused problems.

### 108: What is `UnknownAction`?

A type from Redux 5 for an action whose fields other than `type` are typed as `unknown`. It replaced `AnyAction`, which typed extra fields as `any`. With `UnknownAction` you must narrow the action before reading its fields, usually with `actionCreator.match()` or a type guard.

### 109: What import paths does Redux Toolkit have?

- `@reduxjs/toolkit` - core RTK APIs.
- `@reduxjs/toolkit/react` - core APIs plus React-specific extras, like the React version of `createDynamicMiddleware`.
- `@reduxjs/toolkit/query` - RTK Query without React hooks.
- `@reduxjs/toolkit/query/react` - RTK Query with React hooks.

### 110: What is the difference between importing `createApi` from `/query` and `/query/react`?

Both create an API slice. The `/query/react` version also generates React hooks like `useGetPostsQuery`. Use `/query` for non-React apps.

### 111: What is `setupListeners`?

A helper that adds `focus`, `visibilitychange`, `online` and `offline` event listeners and dispatches actions RTK Query uses for `refetchOnFocus` and `refetchOnReconnect`.

```ts
import { setupListeners } from "@reduxjs/toolkit/query";

setupListeners(store.dispatch);
```

### 112: What is `refetchOnFocus`?

An option that refetches subscribed queries when the browser window regains focus. You can set it on the API or per hook. It needs `setupListeners` to be called.

```ts
useGetPostsQuery(undefined, { refetchOnFocus: true });
```

### 113: How do you poll data with RTK Query?

Use `pollingInterval` in milliseconds.

```tsx
const { data } = useGetStatusQuery(jobId, { pollingInterval: 5000 });
```

The polling stops when the component unmounts. Add `skipPollingIfUnfocused: true` to pause polling while the window is not focused.

### 114: What is `transformResponse`?

A function that changes the response before it's cached. It receives the response, the meta object and the query argument.

```ts
getPosts: build.query<Post[], void>({
  query: () => 'posts',
  transformResponse: (response: { data: Post[] }) => response.data,
}),
```

### 115: How do you add an auth token to every request?

Use `prepareHeaders` in `fetchBaseQuery`.

```ts
const baseQuery = fetchBaseQuery({
  baseUrl: "/api",
  prepareHeaders: (headers, { getState }) => {
    const token = (getState() as RootState).auth.token;
    if (token) {
      headers.set("authorization", `Bearer ${token}`);
    }
    return headers;
  },
});
```

### 116: How do you send a POST request with a body and query params?

Return an object from `query` instead of a string.

```ts
updatePost: build.mutation<Post, Partial<Post> & Pick<Post, 'id'>>({
  query: ({ id, ...patch }) => ({
    url: `posts/${id}`,
    method: 'PATCH',
    body: patch,
    params: { notify: true },
  }),
}),
```

`fetchBaseQuery` serializes `body` as JSON and adds the content type header for you.

### 117: What is the difference between `data` and `currentData` in a query result?

When the argument changes, `data` keeps showing the last result until the new one arrives. `currentData` is `undefined` until the result for the current argument is ready. Use `data` to avoid a blank screen while switching, and `currentData` when showing old data for a new argument would be confusing.

### 118: What does an error from `fetchBaseQuery` look like?

It is a `FetchBaseQueryError`:

- `{ status: number, data: unknown }` for HTTP errors like 404 or 500.
- `{ status: 'FETCH_ERROR', error: string }` for network errors.
- `{ status: 'PARSING_ERROR', originalStatus, data, error }` when the body can't be parsed.
- `{ status: 'TIMEOUT_ERROR', error: string }` when the `timeout` is hit.
- `{ status: 'CUSTOM_ERROR', data?, error }` for your own errors.

The hook's `error` can also be a `SerializedError` if something throws inside your code.

### 119: How do you handle errors from a mutation?

Call `.unwrap()` on the trigger result and use `try/catch`, or read `error` from the hook result.

```tsx
const [deletePost, { error }] = useDeletePostMutation();

const onDelete = async () => {
  try {
    await deletePost(id).unwrap();
  } catch (err) {
    toast.error("Could not delete the post");
  }
};
```

### 120: What is `useLazyQuery`?

A query hook that doesn't fetch on mount. It returns a trigger function, so you decide when to run the request.

```tsx
const [trigger, { data, isFetching }] = useLazyGetUserQuery()

<button onClick={() => trigger(userId)}>Load user</button>
```

### 121: Why should you avoid storing derived data in Redux state?

If you store both a list and a filtered version of it, they can get out of sync. Store the minimal data and compute the rest with selectors. For example, store `todos` and compute `completedCount` in a selector.

### 122: Where should most of the business logic go?

The Redux style guide suggests putting as much logic as possible in reducers, since they are pure and easy to test. Keep components thin: they dispatch actions that describe what happened, and reducers decide how state changes.

### 123: What does "model actions as events, not setters" mean?

Name actions after what happened, not after which field to change. For example `orderPlaced` instead of `setCartItems`, `setOrderStatus` and `setTotal`. One event can then update several slices, and the action log in the DevTools reads like a history of what the user did.

### 124: What is the Redux Style Guide?

The official list of recommended practices on the Redux docs site. Some rules are marked essential, like "do not mutate state" and "reducers must not have side effects". Others are strongly recommended, like "use Redux Toolkit", "use feature folders", "normalize complex state" and "use the React-Redux hooks API".

### 125: How do you update nested state with Immer?

Just write to the nested path on the draft.

```ts
userAddressUpdated(state, action: PayloadAction<{ city: string }>) {
  state.user.profile.address.city = action.payload.city
}
```

Without Immer you'd have to spread every level.

### 126: How do you add, update and remove items in an array in a slice reducer?

```ts
reducers: {
  itemAdded(state, action: PayloadAction<Item>) {
    state.items.push(action.payload)
  },
  itemUpdated(state, action: PayloadAction<Item>) {
    const index = state.items.findIndex((i) => i.id === action.payload.id)
    if (index !== -1) state.items[index] = action.payload
  },
  itemRemoved(state, action: PayloadAction<string>) {
    state.items = state.items.filter((i) => i.id !== action.payload)
  },
}
```

Assigning `state.items = ...` is fine because you change a property of the draft, not the draft variable itself.

### 127: How do you toggle a boolean in a slice?

```ts
sidebarToggled(state) {
  state.sidebarOpen = !state.sidebarOpen
}
```

### 128: Can a reducer make an API call?

No. Reducers must be pure and synchronous. Put API calls in thunks, listener effects or RTK Query endpoints, then dispatch actions with the results.

### 129: Can a reducer dispatch an action?

No. Dispatching from a reducer throws an error in Redux. If one action should cause another, either handle the first action in multiple reducers with `extraReducers`, or use a thunk or listener to dispatch the second action.

### 130: What happens if you dispatch an action no reducer handles?

Nothing changes. Each reducer returns its current state, so the state reference stays the same, and React-Redux skips re-renders because selected values didn't change. The action still shows up in the DevTools.

### 131: How do you test a slice reducer?

Call the reducer with a state and an action and check the result.

```ts
import reducer, { todoAdded } from "./todosSlice";

test("adds a todo", () => {
  const prev = { items: [] };
  const next = reducer(prev, todoAdded({ id: "1", text: "Test" }));
  expect(next.items).toHaveLength(1);
  expect(next.items[0].text).toBe("Test");
});

test("returns the initial state", () => {
  expect(reducer(undefined, { type: "unknown" })).toEqual({ items: [] });
});
```

### 132: How do you test an action creator?

Check the object it returns.

```ts
expect(incrementByAmount(5)).toEqual({
  type: "counter/incrementByAmount",
  payload: 5,
});
```

Usually it's more useful to test the reducer and the store together than action creators alone.

### 133: Does Redux Toolkit include `react-redux`?

No. `react-redux` is a separate package. RTK lists React and React-Redux as optional peer dependencies, which are only needed for React features like RTK Query hooks.

### 134: Which React-Redux version works with Redux Toolkit 2.x?

React-Redux 9.x. It supports React 18 and 19 and uses `useSyncExternalStore` internally. It also adds `.withTypes()` on the hooks.

### 135: How do you read the arguments that were passed to a thunk in a reducer?

`createAsyncThunk` puts them in `action.meta.arg` for all three lifecycle actions.

```ts
builder.addCase(fetchPost.pending, (state, action) => {
  state.loadingId = action.meta.arg;
});
```

### 136: What is `action.meta.requestId`?

A unique ID that `createAsyncThunk` generates for each call. It is the same for the `pending`, `fulfilled` and `rejected` actions of one call, so you can match them up and ignore responses from older requests.

### 137: How do you pass multiple arguments to a `createAsyncThunk` payload creator?

The payload creator takes only one argument, so pass an object.

```ts
export const fetchComments = createAsyncThunk(
  "comments/fetch",
  async ({ postId, page }: { postId: string; page: number }) => {
    const res = await fetch(`/api/posts/${postId}/comments?page=${page}`);
    return res.json();
  },
);

dispatch(fetchComments({ postId: "42", page: 2 }));
```

### 138: How do you get the state inside a `createAsyncThunk`?

Use `getState` from the second argument.

```ts
export const saveDraft = createAsyncThunk(
  "editor/saveDraft",
  async (_, { getState }) => {
    const { editor } = getState() as RootState;
    await api.saveDraft(editor.content);
  },
);
```

Using `createAsyncThunk.withTypes` avoids the type cast. That's covered in the moderate section.

### 139: How does a slice respond to an action from another slice?

Use `extraReducers`.

```ts
import { userLoggedOut } from "../auth/authSlice";

const cartSlice = createSlice({
  name: "cart",
  initialState,
  reducers: {/* ... */},
  extraReducers: (builder) => {
    builder.addCase(userLoggedOut, () => initialState);
  },
});
```

### 140: What does `builder.addDefaultCase` do?

It adds a reducer that runs when no `addCase` or `addMatcher` handled the action. It must be the last call on the builder.

### 141: What is `invalidatesTags` on a mutation?

It lists the tags that should be marked stale after the mutation finishes. Any active query that provides one of those tags refetches automatically.

```ts
deletePost: build.mutation<void, number>({
  query: (id) => ({ url: `posts/${id}`, method: 'DELETE' }),
  invalidatesTags: (result, error, id) => [{ type: 'Post', id }],
}),
```

### 142: What is `providesTags` on a query?

It tells RTK Query which tags the cached data belongs to. It can be an array, or a function of `(result, error, arg)`.

```ts
getPost: build.query<Post, number>({
  query: (id) => `posts/${id}`,
  providesTags: (result, error, id) => [{ type: 'Post', id }],
}),
```

### 143: Does RTK Query send two requests if two components use the same query with the same argument?

No. RTK Query dedupes requests. Both components subscribe to the same cache entry, one request is made, and both get the result. The cache entry stays alive as long as at least one subscriber exists, plus `keepUnusedDataFor` seconds.

### 144: How do you get a typed error message out of an RTK Query error?

Narrow the error type first:

```tsx
const { error } = useGetPostQuery(id);

if (error) {
  if ("status" in error) {
    const message = "error" in error ? error.error : JSON.stringify(error.data);
    return <p>Error: {message}</p>;
  }
  return <p>{error.message}</p>;
}
```

`'status' in error` means a `FetchBaseQueryError`. Otherwise it's a `SerializedError`.

### 145: What does `isSuccess` mean in a query result?

The query has data from a successful request. It stays `true` while refetching in the background, so it doesn't flip back to `false` when `isFetching` is true.

### 146: Can you use multiple query hooks in one component?

Yes. Each hook manages its own cache entry and status.

```tsx
const { data: user } = useGetUserQuery(userId);
const { data: posts } = useGetPostsByUserQuery(userId);
```

### 147: What is the `AppStore` type and when do you need it?

```ts
export type AppStore = typeof store;
```

Or, when you create the store with a function:

```ts
export const makeStore = () => configureStore({ reducer: rootReducer });
export type AppStore = ReturnType<typeof makeStore>;
```

You need it for typed `useStore`, test helpers and frameworks like Next.js where you create a store per request.

### 148: How do you dispatch an action outside of React?

Import the store and call `store.dispatch`.

```ts
import { store } from "./app/store";
import { sessionExpired } from "./features/auth/authSlice";

store.dispatch(sessionExpired());
```

Be careful with importing the store directly from modules that the store itself imports. It can create circular imports. Passing the store or using the thunk extra argument is often cleaner.

### 149: What is the difference between RTK and Zustand?

Both manage global state. Zustand is smaller and has less structure: a hook-based store with no actions or reducers required. RTK is more structured: actions, reducers, middleware, DevTools time travel, and built-in data fetching with RTK Query. RTK fits larger apps with many developers and complex state, Zustand fits smaller apps or when you want less ceremony.

### 150: What is the difference between RTK Query and TanStack Query?

Both fetch and cache server data. TanStack Query doesn't need Redux and you write a query function per hook. RTK Query is part of Redux Toolkit, keeps its cache in the Redux store, uses a central API definition with endpoints and tags, and works with the DevTools and the rest of your Redux code. If you already use Redux, RTK Query is a natural fit. If you don't, TanStack Query is lighter.

## Moderate Questions

### 151: How do you define selectors inside `createSlice`?

RTK 2.0 added a `selectors` field. Each selector receives the slice state as its first argument. The slice wraps them so you call them with the root state.

```ts
const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment(state) {
      state.value += 1;
    },
  },
  selectors: {
    selectValue: (sliceState) => sliceState.value,
    selectIsPositive: (sliceState) => sliceState.value > 0,
  },
});

export const { selectValue, selectIsPositive } = counterSlice.selectors;

// in a component
const value = useAppSelector(selectValue);
```

The wrapped selectors look up the slice state at `rootState[slice.reducerPath]`.

### 152: What is `reducerPath` on a slice?

It is the key where the slice is expected to live in the root state. It defaults to `name`, but you can set it separately.

```ts
const slice = createSlice({
  name: "user/settings",
  reducerPath: "settings",
  initialState,
  reducers: {},
});
```

Action types use `name` (`'user/settings/...'`), while `slice.selectors` read from `state.settings`. `combineSlices` also uses `reducerPath` as the key.

### 153: What is the difference between `slice.selectors` and `slice.getSelectors()`?

- `slice.selectors` expect the root state and read from `state[reducerPath]`.
- `slice.getSelectors()` with no argument returns selectors that expect the slice state directly.
- `slice.getSelectors(selectState)` returns selectors that use your function to find the slice state. Use this when the slice is mounted under a different key.

```ts
const { selectValue } = counterSlice.getSelectors(
  (state: RootState) => state.nested.counter,
);
```

### 154: How do selectors with extra arguments work in `slice.selectors`?

Extra arguments are passed through after the state.

```ts
selectors: {
  selectTodoById: (state, id: string) => state.items.find((t) => t.id === id),
}

const todo = useAppSelector((state) => selectTodoById(state, todoId))
```

### 155: What is the `create` callback syntax for `reducers` in `createSlice`?

Instead of an object, you can pass a function that receives a `create` helper. It is needed for defining async thunks inside a slice, and it also has `create.reducer` and `create.preparedReducer`.

```ts
const todosSlice = createSlice({
  name: "todos",
  initialState: { items: [] as Todo[] },
  reducers: (create) => ({
    deleteTodo: create.reducer<string>((state, action) => {
      state.items = state.items.filter((t) => t.id !== action.payload);
    }),
    addTodo: create.preparedReducer(
      (text: string) => ({ payload: { id: nanoid(), text, completed: false } }),
      (state, action) => {
        state.items.push(action.payload);
      },
    ),
  }),
});
```

The callback form makes TypeScript inference for prepared reducers easier, since the prepare and reducer are linked.

### 156: How do you define an async thunk inside `createSlice`?

Use `create.asyncThunk`. It isn't included by default because it would pull `createAsyncThunk` into every bundle, so you build a custom `createSlice` with `buildCreateSlice`:

```ts
import { asyncThunkCreator, buildCreateSlice } from "@reduxjs/toolkit";

export const createAppSlice = buildCreateSlice({
  creators: { asyncThunk: asyncThunkCreator },
});

const todosSlice = createAppSlice({
  name: "todos",
  initialState: {
    items: [] as Todo[],
    loading: false,
    error: null as string | null,
  },
  reducers: (create) => ({
    fetchTodo: create.asyncThunk(
      async (id: string, thunkApi) => {
        const res = await fetch(`/api/todos/${id}`);
        if (!res.ok) return thunkApi.rejectWithValue("Request failed");
        return (await res.json()) as Todo;
      },
      {
        pending: (state) => {
          state.loading = true;
        },
        rejected: (state, action) => {
          state.error = (action.payload as string) ?? "Unknown error";
        },
        fulfilled: (state, action) => {
          state.items.push(action.payload);
        },
        settled: (state) => {
          state.loading = false;
        },
      },
    ),
  }),
});

export const { fetchTodo } = todosSlice.actions;
```

`settled` runs after both `fulfilled` and `rejected`.

### 157: What is `combineSlices`?

A function added in RTK 2.0 that builds a root reducer from slices, RTK Query APIs and reducer maps. It uses each slice's `reducerPath` as the key, and the result can have more slices injected later.

```ts
import { combineSlices } from "@reduxjs/toolkit";

export const rootReducer = combineSlices(counterSlice, authSlice, api, {
  legacy: legacyReducer,
});
export type RootState = ReturnType<typeof rootReducer>;
```

### 158: How do you inject a slice later with `combineSlices`?

Call `rootReducer.inject(slice)` or `slice.injectInto(rootReducer)`. The store picks up the new reducer on the next dispatch, and you don't need `replaceReducer`.

```ts
// features/reports/reportsSlice.ts
import { rootReducer } from "../../app/rootReducer";

const reportsSlice = createSlice({
  name: "reports",
  initialState,
  reducers: {},
});

export const injectedReportsSlice = reportsSlice.injectInto(rootReducer);
export const { selectReports } = injectedReportsSlice.selectors;
```

This lets you load reducers together with lazy-loaded routes.

### 159: How do you type lazy-loaded slices with `combineSlices`?

Declare them with `withLazyLoadedSlices` and the `WithSlice` helper type. The state type then includes them as optional keys.

```ts
// rootReducer.ts
export interface LazyLoadedSlices {}

export const rootReducer =
  combineSlices(counterSlice).withLazyLoadedSlices<LazyLoadedSlices>();

// reportsSlice.ts
declare module "../../app/rootReducer" {
  export interface LazyLoadedSlices extends WithSlice<typeof reportsSlice> {}
}
const injected = reportsSlice.injectInto(rootReducer);
```

The module augmentation keeps the root file from importing every lazy slice.

### 160: What happens if you call a slice selector before the slice is injected?

Selectors from an injected slice (`injectedSlice.selectors`) handle that case: if the slice state is missing, they use the slice's initial state instead of crashing on `undefined`. You can do the same for your own selectors with `rootReducer.selector(...)`.

```ts
const selectReportCount = rootReducer.selector(
  (state) => state.reports.items.length,
);
```

### 161: What does the second argument to the `createAsyncThunk` payload creator contain?

The `thunkAPI` object:

- `dispatch`, `getState`
- `extra` - the thunk extra argument
- `requestId` - unique ID for this call
- `signal` - an `AbortSignal` for cancellation
- `rejectWithValue(value, meta?)`
- `fulfillWithValue(value, meta?)`

### 162: What is `fulfillWithValue`?

It lets you return a fulfilled value with extra `meta` data attached to the `fulfilled` action. It's mostly used with the `fulfilledMeta` type option.

```ts
const fetchItems = createAsyncThunk<
  Item[],
  void,
  { fulfilledMeta: { fromCache: boolean } }
>("items/fetch", async (_, { fulfillWithValue }) => {
  const items = await loadItems();
  return fulfillWithValue(items, { fromCache: false });
});
```

### 163: How do you type `createAsyncThunk` with generics?

The generics are `<Returned, ThunkArg, ThunkApiConfig>`.

```ts
const updateUser = createAsyncThunk<
  User,
  { id: string; changes: Partial<User> },
  {
    state: RootState;
    dispatch: AppDispatch;
    rejectValue: ApiError;
    extra: { apiClient: ApiClient };
  }
>("users/update", async ({ id, changes }, { extra, rejectWithValue }) => {
  try {
    return await extra.apiClient.updateUser(id, changes);
  } catch (err) {
    return rejectWithValue(toApiError(err));
  }
});
```

### 164: What is `createAsyncThunk.withTypes()`?

It creates a pre-typed version of `createAsyncThunk` so you don't have to repeat the `state`, `dispatch` and other types each time.

```ts
// app/withTypes.ts
export const createAppAsyncThunk = createAsyncThunk.withTypes<{
  state: RootState;
  dispatch: AppDispatch;
  rejectValue: string;
  extra: { apiClient: ApiClient };
}>();

// in a feature
export const fetchPosts = createAppAsyncThunk(
  "posts/fetch",
  async (_, { getState }) => {
    const { posts } = getState(); // typed as RootState
    // ...
  },
);
```

### 165: What is the `condition` option of `createAsyncThunk`?

A function that runs before the payload creator. If it returns `false`, the thunk is cancelled and nothing is dispatched. It is commonly used to avoid duplicate requests.

```ts
export const fetchUser = createAsyncThunk(
  "users/fetch",
  async (id: string) => api.getUser(id),
  {
    condition: (id, { getState }) => {
      const { users } = getState() as RootState;
      const status = users.statusById[id];
      if (status === "loading" || status === "succeeded") return false;
    },
  },
);
```

It can also be async.

### 166: What does `dispatchConditionRejection` do?

By default, when `condition` returns `false` no action is dispatched at all. If you set `dispatchConditionRejection: true`, a `rejected` action is dispatched with `meta.condition: true`, so your reducers can see that the call was skipped.

### 167: How do you cancel a `createAsyncThunk` request?

The promise returned from `dispatch` has an `abort()` method. It rejects the thunk with an `AbortError` and fires the `signal` given to the payload creator. Pass that `signal` to `fetch` so the HTTP request is also cancelled.

```tsx
useEffect(() => {
  const promise = dispatch(fetchResults(query));
  return () => promise.abort();
}, [query, dispatch]);

export const fetchResults = createAsyncThunk(
  "search/fetchResults",
  async (query: string, { signal }) => {
    const res = await fetch(`/api/search?q=${query}`, { signal });
    return res.json();
  },
);
```

### 168: How can you tell in a reducer that a thunk was aborted?

The `rejected` action has `action.meta.aborted === true`, and `action.error.name` is `'AbortError'`. You usually ignore it instead of showing an error.

```ts
builder.addCase(fetchResults.rejected, (state, action) => {
  if (action.meta.aborted) return;
  state.error = action.error.message ?? null;
});
```

### 169: What does `serializeError` do in `createAsyncThunk`?

When the payload creator throws, RTK turns the error into a plain object with `name`, `message`, `stack` and `code` using `miniSerializeError`. Pass `serializeError` to change that, for example to keep extra fields from a custom error class.

```ts
createAsyncThunk("x", payloadCreator, {
  serializeError: (err) => ({
    message: (err as Error).message,
    code: (err as AppError).code,
  }),
});
```

Using `rejectWithValue` is usually simpler.

### 170: What is `idGenerator` in `createAsyncThunk`?

A function to create the `requestId` instead of the default `nanoid`. It receives the thunk argument. You might use it to make request IDs readable in the DevTools or deterministic in tests.

### 171: What is `getPendingMeta`?

A function in the thunk options that returns extra fields to merge into `pending` action's `meta`. It receives `{ arg, requestId }` and `{ getState, extra }`.

```ts
createAsyncThunk("items/fetch", payloadCreator, {
  getPendingMeta: () => ({ startedAt: Date.now() }),
});
```

### 172: How do you prevent an older request from overwriting newer data?

Save the `requestId` when the request starts and ignore results from other requests.

```ts
builder
  .addCase(search.pending, (state, action) => {
    state.currentRequestId = action.meta.requestId;
    state.loading = true;
  })
  .addCase(search.fulfilled, (state, action) => {
    if (state.currentRequestId !== action.meta.requestId) return;
    state.results = action.payload;
    state.loading = false;
  });
```

Aborting the previous promise is another option.

### 173: What are `isPending`, `isFulfilled` and `isRejected`?

Matcher helpers for async thunk actions. With no arguments, they match any thunk's pending/fulfilled/rejected action. With thunks as arguments, they match only those.

```ts
builder
  .addMatcher(isPending(fetchPosts, fetchComments), (state) => {
    state.loading = true;
  })
  .addMatcher(isRejected, (state, action) => {
    state.lastError = action.error.message;
  });
```

There are also `isAsyncThunkAction` and `isRejectedWithValue`.

### 174: What is `builder.addMatcher`?

It adds a reducer that runs for every action where the matcher function returns `true`. Any type guard function works as a matcher.

```ts
builder.addMatcher(
  (action: UnknownAction) => action.type.endsWith("/rejected"),
  (state) => {
    state.errorCount += 1;
  },
);
```

### 175: In what order must you call the builder methods?

All `addCase` calls first, then `addMatcher` calls, then `addDefaultCase` at the end. RTK throws if you break the order. At runtime, the matching `addCase` runs first, then every matching `addMatcher` in the order you added them.

### 176: What does `isRejectedWithValue` do?

It matches rejected thunk actions where the payload was set with `rejectWithValue`. RTK Query also uses `rejectWithValue` for API errors, so this is a common way to catch failed requests in middleware.

```ts
export const rtkQueryErrorLogger: Middleware = () => (next) => (action) => {
  if (isRejectedWithValue(action)) {
    console.warn("Async error", action.payload);
  }
  return next(action);
};
```

### 177: How do you write a typed custom middleware in RTK 2.x?

In Redux 5 the `action` and `next` are typed as `unknown`, so you narrow the action before reading it.

```ts
import type { Middleware } from "@reduxjs/toolkit";
import { isAction } from "@reduxjs/toolkit";

export const analyticsMiddleware: Middleware<{}, RootState> =
  (storeApi) => (next) => (action) => {
    if (isAction(action) && action.type.startsWith("cart/")) {
      track(action.type, storeApi.getState().cart.items.length);
    }
    return next(action);
  };
```

Using `someAction.match(action)` gives you a fully typed payload.

### 178: How do you configure the serializability check?

Pass options through `getDefaultMiddleware`.

```ts
middleware: (getDefaultMiddleware) =>
  getDefaultMiddleware({
    serializableCheck: {
      ignoredActions: ['upload/fileSelected'],
      ignoredActionPaths: ['meta.arg', 'payload.timestamp'],
      ignoredPaths: ['ui.lastFile'],
      warnAfter: 64,
    },
  }),
```

`warnAfter` controls when it warns that the check itself is slow (in ms). You can also pass `false` to turn the check off.

### 179: How do you configure Redux Toolkit to work with `redux-persist`?

`redux-persist` dispatches actions with functions in them, so ignore those action types in the serializability check.

```ts
import {
  FLUSH,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
  REHYDRATE,
  persistReducer,
  persistStore,
} from "redux-persist";
import storage from "redux-persist/lib/storage";

const persistedReducer = persistReducer(
  { key: "root", storage, whitelist: ["auth"] },
  rootReducer,
);

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    }),
});

export const persistor = persistStore(store);
```

Usually you should not persist the RTK Query cache.

### 180: How do you configure the immutability check?

```ts
getDefaultMiddleware({
  immutableCheck: {
    ignoredPaths: ["bigData.rows"],
    warnAfter: 128,
  },
});
```

For very large states it can be slow in development. Ignore the large paths or turn it off with `immutableCheck: false`.

### 181: What is `Tuple` and why does it exist?

`Tuple` is an array subclass that keeps the type of each item. `getDefaultMiddleware()` returns one. TypeScript loses per-item types with plain arrays, so the store's `dispatch` type wouldn't know about thunks. If you build the list yourself, wrap it in `Tuple`:

```ts
import { Tuple } from "@reduxjs/toolkit";

const store = configureStore({
  reducer: rootReducer,
  middleware: () => new Tuple(thunk, logger),
});
```

### 182: How do you add a store enhancer in RTK 2.x?

Use the `enhancers` callback with `getDefaultEnhancers`.

```ts
const store = configureStore({
  reducer: rootReducer,
  enhancers: (getDefaultEnhancers) =>
    getDefaultEnhancers().concat(sentryEnhancer),
});
```

Don't drop the defaults. They include `applyMiddleware` and `autoBatchEnhancer`, and without them your middleware won't run.

### 183: What does the `autoBatchEnhancer` do?

It delays notifying subscribers for actions marked as "low priority" (with `meta[SHOULD_AUTOBATCH]`) so that several updates cause one UI render. RTK Query marks many of its internal actions this way. It's on by default in RTK 2.0, and you can configure it:

```ts
enhancers: (getDefaultEnhancers) =>
  getDefaultEnhancers({ autoBatch: { type: 'tick' } }),
```

Options are `'raf'` (default), `'tick'`, `'timer'` and `'callback'`.

### 184: What options can you pass to `devTools` in `configureStore`?

Any option from the Redux DevTools Extension, for example:

```ts
devTools: {
  name: 'Admin app',
  maxAge: 100,
  trace: true,
  actionsDenylist: ['ui/mouseMoved'],
  actionSanitizer: (action) =>
    action.type === 'files/loaded' ? { ...action, payload: '<<LARGE>>' } : action,
  stateSanitizer: (state) => ({ ...state, files: '<<LARGE>>' }),
}
```

### 185: How do you inject dependencies into thunks for testing?

Pass them as the thunk extra argument, then replace them in tests.

```ts
// store
export const makeStore = (apiClient = realApiClient) =>
  configureStore({
    reducer: rootReducer,
    middleware: (gDM) => gDM({ thunk: { extraArgument: { apiClient } } }),
  });

// thunk
export const loadUser = createAppAsyncThunk(
  "user/load",
  async (id: string, { extra }) => extra.apiClient.getUser(id),
);

// test
const store = makeStore(fakeApiClient);
await store.dispatch(loadUser("1"));
```

### 186: What is the listener middleware?

`createListenerMiddleware` creates a middleware that runs "effect" callbacks when matching actions are dispatched. It is RTK's simpler alternative to sagas and observables for reactive side effects.

```ts
import { createListenerMiddleware } from "@reduxjs/toolkit";

export const listenerMiddleware = createListenerMiddleware();

listenerMiddleware.startListening({
  actionCreator: todoAdded,
  effect: async (action, listenerApi) => {
    await saveToServer(action.payload);
    listenerApi.dispatch(todoSaved(action.payload.id));
  },
});

export const store = configureStore({
  reducer: rootReducer,
  middleware: (gDM) => gDM().prepend(listenerMiddleware.middleware),
});
```

### 187: What are the ways to choose which actions a listener runs for?

Pass exactly one of these to `startListening`:

- `actionCreator` - one action creator.
- `type` - an action type string.
- `matcher` - a matcher like `isAnyOf(a, b)`.
- `predicate` - `(action, currentState, previousState) => boolean`.

The `predicate` option lets you react to state changes, not just actions.

```ts
startListening({
  predicate: (action, currentState, previousState) =>
    currentState.settings.theme !== previousState.settings.theme,
  effect: (action, api) => {
    localStorage.setItem("theme", api.getState().settings.theme);
  },
});
```

### 188: What does the `listenerApi` give you inside an effect?

- `dispatch`, `getState`, `getOriginalState` (state before this action, only usable synchronously)
- `extra` - the extra argument from `createListenerMiddleware({ extra })`
- `condition(predicate, timeout?)` and `take(predicate, timeout?)` - wait for future actions or state
- `delay(ms)` and `pause(promise)` - cancellation-aware waiting
- `fork(executor)` - start a child task
- `cancelActiveListeners()`, `cancel()`, `throwIfCancelled()`, `signal`
- `unsubscribe()`, `subscribe()` - stop or restart this listener

### 189: When should you use a listener instead of a thunk?

- A thunk runs when you call it. Use it for "do this now" logic started from the UI.
- A listener runs in response to actions or state changes. Use it for "whenever X happens, do Y" logic, like saving to storage when settings change, analytics, or starting a sync after login.

Listeners keep components from having to know about every side effect.

### 190: How do you debounce with the listener middleware?

Cancel previous runs and wait.

```ts
startAppListening({
  actionCreator: searchTextChanged,
  effect: async (action, listenerApi) => {
    listenerApi.cancelActiveListeners();
    await listenerApi.delay(300);
    listenerApi.dispatch(searchApi.endpoints.search.initiate(action.payload));
  },
});
```

If a new action comes in during the delay, the previous effect is cancelled and its `delay` throws a `TaskAbortError`, which the middleware handles quietly.

### 191: What do `condition` and `take` do in a listener?

Both pause the effect until something happens.

- `condition(predicate, timeout?)` resolves to `true` when the predicate passes, or `false` on timeout.
- `take(predicate, timeout?)` resolves to `[action, currentState, previousState]` when a matching action comes in, or `null` on timeout.

```ts
effect: async (action, listenerApi) => {
  const result = await listenerApi.take(paymentConfirmed.match, 30_000);
  if (!result) {
    listenerApi.dispatch(paymentTimedOut());
  }
};
```

### 192: How do you add a listener from a component?

Dispatch the `addListener` action. Dispatching it returns an unsubscribe function, so it works well in `useEffect`.

```tsx
useEffect(() => {
  const unsubscribe = dispatch(
    addListener({
      actionCreator: notificationReceived,
      effect: (action) => showToast(action.payload.message),
    }),
  );
  return unsubscribe;
}, [dispatch]);
```

### 193: How do you type the listener middleware?

Create pre-typed versions of `startListening` and `addListener`.

```ts
export const listenerMiddleware = createListenerMiddleware();

export const startAppListening = listenerMiddleware.startListening.withTypes<
  RootState,
  AppDispatch
>();

export const addAppListener = addListener.withTypes<RootState, AppDispatch>();
```

### 194: How do you remove a listener?

- Call the unsubscribe function returned by `startListening`.
- Call `listenerMiddleware.stopListening({ actionCreator, effect })` with the same options.
- Dispatch `removeListener({ ... })`.
- Call `listenerMiddleware.clearListeners()` or dispatch `clearAllListeners()` to remove all of them.

`stopListening` and `removeListener` accept `cancelActive: true` to also cancel running effects.

### 195: What is the difference between `addOne`, `setOne` and `upsertOne`?

- `addOne` adds the item only if the ID doesn't exist. Existing items are left alone.
- `setOne` adds the item, or fully replaces it if it exists.
- `upsertOne` adds the item, or shallow merges the new fields into the existing one.

The same applies to `addMany`, `setMany` and `upsertMany`.

### 196: How does `updateOne` work?

It takes `{ id, changes }` and does a shallow merge of `changes` into the existing entity. If the ID is not found, nothing happens.

```ts
postUpdated(state, action: PayloadAction<{ id: string; title: string }>) {
  const { id, title } = action.payload
  postsAdapter.updateOne(state, { id, changes: { title } })
}
```

If `changes` contains a new `id`, the entity is moved to the new key.

### 197: What is the difference between `setAll` and `setMany`?

- `setAll` replaces the whole collection. Items not in the new list are removed.
- `setMany` adds or replaces only the given items and keeps all others.

Use `setAll` when a response is the full list, and `setMany` when it's one page of results.

### 198: How do you combine an entity adapter with `createAsyncThunk`?

```ts
const postsAdapter = createEntityAdapter<Post>();

const initialState = postsAdapter.getInitialState({
  status: "idle" as "idle" | "loading" | "failed",
});

export const fetchPosts = createAppAsyncThunk("posts/fetch", async () => {
  const res = await fetch("/api/posts");
  return (await res.json()) as Post[];
});

const postsSlice = createSlice({
  name: "posts",
  initialState,
  reducers: {
    postAdded: postsAdapter.addOne,
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchPosts.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchPosts.fulfilled, (state, action) => {
        state.status = "idle";
        postsAdapter.setAll(state, action.payload);
      });
  },
});
```

### 199: Are the adapter selectors memoized?

`selectAll` is memoized with `createSelector`, so it returns the same array as long as `ids` and `entities` don't change. `selectById` just reads `entities[id]`, so it already returns a stable reference. You can pass your own `createSelector` with `getSelectors(selectState, { createSelector })` to change the memoization.

### 200: How do you type entity adapters with non-string IDs?

In RTK 2.0 the adapter infers the ID type from `selectId`. `EntityState` takes two generics: `EntityState<T, Id>`.

```ts
interface Product {
  sku: number;
  name: string;
}

const productsAdapter = createEntityAdapter({
  selectId: (p: Product) => p.sku,
});

type ProductsState = EntityState<Product, number>;
```

### 201: What are input selectors and output selectors in `createSelector`?

- Input selectors pull raw values from the state and the arguments. They should be simple lookups.
- The output (result) function receives the input values and does the actual work, like filtering or mapping.

The result function only runs when an input value changes by reference.

### 202: How do you pass arguments to a memoized selector?

Arguments are passed to every input selector. Add an input selector that returns the argument.

```ts
export const selectPostsByUser = createSelector(
  [selectAllPosts, (state: RootState, userId: string) => userId],
  (posts, userId) => posts.filter((p) => p.userId === userId),
);

const posts = useAppSelector((state) => selectPostsByUser(state, userId));
```

### 203: What changed in Reselect 5 memoization?

Reselect 5 uses `weakMapMemoize` by default instead of a cache of size 1. It keeps a cache tree keyed by the arguments, so calling the same selector with different arguments (for example from several components with different IDs) doesn't keep throwing away the cache. Old behavior is still available as `lruMemoize`.

```ts
import { createSelector, lruMemoize } from "@reduxjs/toolkit";

const selectX = createSelector([selectA], (a) => compute(a), {
  memoize: lruMemoize,
  memoizeOptions: { maxSize: 10 },
});
```

### 204: What is `createSelector.withTypes()`?

It creates a version of `createSelector` with the state type set, so you don't have to type `state` in every input selector.

```ts
export const createAppSelector = createSelector.withTypes<RootState>();

export const selectTodoCount = createAppSelector(
  [(state) => state.todos.items],
  (items) => items.length,
);
```

### 205: What dev checks do Reselect 5 and React-Redux 9 run on selectors?

- Input stability check: Reselect runs the input selectors twice the first time and warns if they return different references for the same input. That means an input selector is creating new objects, which breaks memoization.
- Identity function check: warns if the result function just returns its input, which means the memoization is useless.
- `useSelector` stability check: warns if your selector returns a different reference when called twice with the same state.

They only run in development. You can configure them with `devModeChecks`.

### 206: What is a common mistake that breaks memoization?

Doing the work in an input selector instead of the result function:

```ts
// Wrong: filter runs in the input selector, so the input changes every time
const selectDone = createSelector(
  [(state: RootState) => state.todos.filter((t) => t.done)],
  (done) => done.length,
);

// Right
const selectDone = createSelector(
  [(state: RootState) => state.todos],
  (todos) => todos.filter((t) => t.done).length,
);
```

### 207: What is `createDraftSafeSelector`?

A version of `createSelector` that works correctly when called with an Immer draft inside a reducer. A normal memoized selector would see the same draft reference and could return a stale value. `createDraftSafeSelector` detects drafts and uses `current()` on them first. Entity adapter selectors use it internally.

### 208: When should you pass `shallowEqual` to `useSelector`?

When your selector returns a new object built from several fields, and you don't want to use `createSelector`.

```tsx
import { shallowEqual } from "react-redux";

const { name, email } = useAppSelector(
  (state) => ({ name: state.user.name, email: state.user.email }),
  shallowEqual,
);
```

Often it's simpler to call `useSelector` twice.

### 209: How does the function form of `providesTags` help?

You can create one tag per item, plus a list tag. This allows precise invalidation.

```ts
getPosts: build.query<Post[], void>({
  query: () => 'posts',
  providesTags: (result = []) => [
    ...result.map(({ id }) => ({ type: 'Post' as const, id })),
    { type: 'Post' as const, id: 'LIST' },
  ],
}),
```

### 210: What is the `LIST` tag pattern?

Add a special tag ID (often `'LIST'`) to queries that return a list. Then:

- Creating an item invalidates `{ type: 'Post', id: 'LIST' }`, which refetches the list but not single post queries.
- Updating an item invalidates `{ type: 'Post', id }`, which refetches that post and any list that contains it.

```ts
addPost: build.mutation<Post, Partial<Post>>({
  query: (body) => ({ url: 'posts', method: 'POST', body }),
  invalidatesTags: [{ type: 'Post', id: 'LIST' }],
}),
updatePost: build.mutation<Post, Partial<Post> & Pick<Post, 'id'>>({
  query: ({ id, ...patch }) => ({ url: `posts/${id}`, method: 'PATCH', body: patch }),
  invalidatesTags: (result, error, { id }) => [{ type: 'Post', id }],
}),
```

### 211: What does invalidating a tag without an ID do?

`invalidatesTags: ['Post']` (or `{ type: 'Post' }`) invalidates every query that provides any `Post` tag, with or without an ID. Invalidating `{ type: 'Post', id: 1 }` only affects queries that provide that exact tag.

### 212: What is `onQueryStarted`?

A lifecycle callback on an endpoint that runs when a query or mutation starts. It receives the argument and an object with `dispatch`, `getState`, `queryFulfilled` and more. It's used for optimistic updates and for side effects like saving a token.

```ts
login: build.mutation<LoginResponse, Credentials>({
  query: (body) => ({ url: 'login', method: 'POST', body }),
  async onQueryStarted(arg, { dispatch, queryFulfilled }) {
    try {
      const { data } = await queryFulfilled
      dispatch(tokenReceived(data.token))
    } catch {
      // errors are handled by the component
    }
  },
}),
```

### 213: How do you do an optimistic update in RTK Query?

Update the cache with `updateQueryData` before the request finishes, and undo it if the request fails.

```ts
updatePost: build.mutation<void, Pick<Post, 'id'> & Partial<Post>>({
  query: ({ id, ...patch }) => ({ url: `posts/${id}`, method: 'PATCH', body: patch }),
  async onQueryStarted({ id, ...patch }, { dispatch, queryFulfilled }) {
    const patchResult = dispatch(
      api.util.updateQueryData('getPost', id, (draft) => {
        Object.assign(draft, patch)
      }),
    )
    try {
      await queryFulfilled
    } catch {
      patchResult.undo()
    }
  },
}),
```

### 214: What is a pessimistic update?

You wait for the server response, then write the returned data into the cache. It avoids an extra refetch and you never show data the server rejected.

```ts
async onQueryStarted({ id }, { dispatch, queryFulfilled }) {
  try {
    const { data: updatedPost } = await queryFulfilled
    dispatch(
      api.util.updateQueryData('getPost', id, (draft) => {
        Object.assign(draft, updatedPost)
      }),
    )
  } catch {}
},
```

### 215: What is the difference between `updateQueryData` and `upsertQueryData`?

- `updateQueryData(endpointName, arg, recipe)` changes an existing cache entry with an Immer recipe. If there is no entry, nothing happens.
- `upsertQueryData(endpointName, arg, value)` creates the entry if it doesn't exist, or replaces its data. It runs like a real query (async thunk), so it goes through the pending/fulfilled flow.

### 216: What is `upsertQueryEntries`?

A utility action that adds or replaces many cache entries at once, synchronously. A common use is filling individual item entries from a list response, so opening a detail page doesn't need another request.

```ts
getPosts: build.query<Post[], void>({
  query: () => 'posts',
  async onQueryStarted(_, { dispatch, queryFulfilled }) {
    const { data } = await queryFulfilled
    dispatch(
      api.util.upsertQueryEntries(
        data.map((post) => ({ endpointName: 'getPost', arg: post.id, value: post })),
      ),
    )
  },
}),
```

### 217: How do you prefetch data with RTK Query?

Use the `usePrefetch` hook or dispatch `api.util.prefetch`.

```tsx
const prefetchPost = usePrefetch('getPost')

<Link to={`/posts/${id}`} onMouseEnter={() => prefetchPost(id, { ifOlderThan: 60 })}>
  {title}
</Link>
```

`ifOlderThan` skips the request if cached data is newer than the given seconds. `force: true` always refetches.

### 218: What is `selectFromResult`?

A hook option that picks part of the query result. The component only re-renders when the selected value changes.

```tsx
const { post } = useGetPostsQuery(undefined, {
  selectFromResult: ({ data }) => ({
    post: data?.find((p) => p.id === postId),
  }),
});
```

If you return a new derived array, use a memoized selector so the reference stays stable.

### 219: What is `refetchOnMountOrArgChange`?

It controls whether a query refetches when a component mounts or the argument changes, even if cached data exists.

- `false` (default) - use the cache if it exists.
- `true` - always refetch on mount.
- A number - refetch if the cached data is older than that many seconds.

```ts
useGetNotificationsQuery(undefined, { refetchOnMountOrArgChange: 30 });
```

### 220: What is `injectEndpoints`?

It adds endpoints to an existing API later, usually from another file. This lets you split a large API definition and load endpoints with the features that use them.

```ts
// features/users/usersApi.ts
import { api } from "../../services/api";

export const usersApi = api.injectEndpoints({
  endpoints: (build) => ({
    getUsers: build.query<User[], void>({
      query: () => "users",
    }),
  }),
});

export const { useGetUsersQuery } = usersApi;
```

### 221: What is `enhanceEndpoints`?

It changes options on existing endpoints, like adding tags. This is most useful with code-generated APIs, where you can't edit the generated file.

```ts
const enhancedApi = generatedApi.enhanceEndpoints({
  addTagTypes: ["User"],
  endpoints: {
    getUsers: { providesTags: ["User"] },
    updateUser: { invalidatesTags: ["User"] },
  },
});
```

### 222: What is `queryFn`?

An alternative to `query` that lets you run any async code instead of the `baseQuery`. It must return `{ data }` or `{ error }`, and it should not throw.

```ts
getRandomUser: build.query<User, void>({
  async queryFn(_arg, _api, _extraOptions, baseQuery) {
    const idResult = await baseQuery('users/random-id')
    if (idResult.error) return { error: idResult.error }

    const userResult = await baseQuery(`users/${idResult.data}`)
    return userResult.error ? { error: userResult.error } : { data: userResult.data as User }
  },
}),
```

It's also how you use RTK Query with Firebase, IndexedDB or other non-HTTP sources.

### 223: What is `transformErrorResponse`?

Like `transformResponse`, but for errors. It changes the error before it's stored in the cache.

```ts
getPost: build.query<Post, number>({
  query: (id) => `posts/${id}`,
  transformErrorResponse: (response) => ({
    status: response.status,
    message: (response.data as { message?: string })?.message ?? 'Unknown error',
  }),
}),
```

### 224: How do you retry failed requests in RTK Query?

Wrap the base query with `retry`.

```ts
import { retry } from "@reduxjs/toolkit/query/react";

const baseQueryWithRetry = retry(fetchBaseQuery({ baseUrl: "/api" }), {
  maxRetries: 3,
});

export const api = createApi({
  baseQuery: baseQueryWithRetry,
  endpoints: (build) => ({
    getPosts: build.query<Post[], void>({ query: () => "posts" }),
    login: build.mutation<Token, Credentials>({
      query: (body) => ({ url: "login", method: "POST", body }),
      extraOptions: { maxRetries: 0 },
    }),
  }),
});
```

It uses exponential backoff. Inside a custom base query, `retry.fail(error)` stops retrying right away.

### 225: How do you write a custom base query with axios?

A base query is a function `(args, api, extraOptions) => { data } | { error }`.

```ts
import type { BaseQueryFn } from "@reduxjs/toolkit/query";
import axios, { type AxiosError, type AxiosRequestConfig } from "axios";

const axiosBaseQuery =
  ({
    baseUrl,
  }: {
    baseUrl: string;
  }): BaseQueryFn<
    {
      url: string;
      method?: AxiosRequestConfig["method"];
      data?: unknown;
      params?: unknown;
    },
    unknown,
    { status?: number; data?: unknown }
  > =>
  async ({ url, method = "GET", data, params }, { signal }) => {
    try {
      const result = await axios({
        url: baseUrl + url,
        method,
        data,
        params,
        signal,
      });
      return { data: result.data };
    } catch (err) {
      const error = err as AxiosError;
      return {
        error: {
          status: error.response?.status,
          data: error.response?.data ?? error.message,
        },
      };
    }
  };
```

Pass `signal` so RTK Query can cancel requests.

### 226: Which options does `fetchBaseQuery` accept?

The common ones:

- `baseUrl` - prefix for all URLs.
- `prepareHeaders(headers, api)` - set headers before every request.
- `fetchFn` - a custom `fetch` (useful in tests or SSR).
- `paramsSerializer` - custom serializer for `params`.
- `timeout` - abort the request after this many milliseconds.
- `responseHandler` - `'json'`, `'text'`, `'content-type'` or a function.
- `validateStatus(response, body)` - decide which responses count as errors.
- `credentials`, `mode` and other `RequestInit` fields.
- `jsonContentType`, `isJsonContentType` and `jsonReplacer` to control JSON handling.

Most of these can also be set per request in the object returned from `query`.

### 227: How do you send cookies with `fetchBaseQuery`?

Set `credentials: 'include'` so the browser sends cookies on cross-origin requests.

```ts
const baseQuery = fetchBaseQuery({
  baseUrl: "https://api.example.com",
  credentials: "include",
});
```

### 228: How do you upload a file with RTK Query?

Send a `FormData` body. `fetchBaseQuery` doesn't JSON-encode `FormData` and lets the browser set the multipart header.

```ts
uploadAvatar: build.mutation<{ url: string }, { userId: string; file: File }>({
  query: ({ userId, file }) => {
    const body = new FormData()
    body.append('file', file)
    return { url: `users/${userId}/avatar`, method: 'POST', body }
  },
}),
```

A `File` is not serializable. The serializability check ignores `meta.arg` on actions by default, but the mutation's `originalArgs` is also kept in the store, so you may still see a warning. If you do, add that path to `ignoredPaths`, or turn the `File` into an upload URL first.

### 229: How do you treat a 200 response with an error body as an error?

Use `validateStatus`.

```ts
getReport: build.query<Report, string>({
  query: (id) => ({
    url: `reports/${id}`,
    validateStatus: (response, result) => response.status === 200 && !result.isError,
  }),
}),
```

### 230: What is `fixedCacheKey` on a mutation?

By default every `useMutation` call has its own result. With `fixedCacheKey`, all hook instances that use the same key share one result, so another component can see whether a mutation is running or failed.

```tsx
// Save button
const [saveDraft, { isLoading }] = useSaveDraftMutation({
  fixedCacheKey: "save-draft",
});

// Status bar somewhere else
const [, { isLoading: isSaving, isError }] = useSaveDraftMutation({
  fixedCacheKey: "save-draft",
});
```

### 231: What does `reset` do on a mutation result?

It clears the mutation's result back to the uninitialized state, removing `data` and `error`. Use it after showing a success message or when the user closes a form.

```tsx
const [addPost, { isSuccess, reset }] = useAddPostMutation();

useEffect(() => {
  if (isSuccess) {
    const timer = setTimeout(reset, 3000);
    return () => clearTimeout(timer);
  }
}, [isSuccess, reset]);
```

### 232: How do you read cached query data outside of a hook?

Use the endpoint's `select` method. It creates a selector for a given argument.

```ts
const selectPostsResult = api.endpoints.getPosts.select();

const selectPostsData = createSelector(
  [selectPostsResult],
  (result) => result.data ?? [],
);

const posts = selectPostsData(store.getState());
```

Reading doesn't start a request. If nothing fetched it yet, `data` is `undefined`.

### 233: How do you run a query outside of React?

Dispatch `initiate`. It returns a promise-like object that also adds a cache subscription.

```ts
const promise = store.dispatch(api.endpoints.getPost.initiate(5));
try {
  const post = await promise.unwrap();
} finally {
  promise.unsubscribe();
}
```

Call `unsubscribe()` when you are done, or pass `{ subscribe: false }` if you only need the data once. Otherwise the cache entry stays alive forever.

### 234: What options does `initiate` accept?

For queries: `subscribe`, `forceRefetch`, `subscriptionOptions` (like `pollingInterval`) and for infinite queries `direction`. For mutations: `fixedCacheKey` and `track`.

```ts
dispatch(
  api.endpoints.getPosts.initiate(undefined, {
    forceRefetch: true,
    subscribe: false,
  }),
);
```

### 235: What are `useQueryState` and `useQuerySubscription`?

The normal `useQuery` hook is made of these two:

- `useQuerySubscription` - starts the request and keeps the cache entry alive, but doesn't return data.
- `useQueryState` - reads the cache entry, but doesn't start a request.

You get them from `api.endpoints.getPosts.useQueryState(arg)`. `useQueryState` is useful when a child component wants to read data that a parent already fetches, without adding another subscription.

### 236: How do you invalidate tags from outside an endpoint?

Dispatch `api.util.invalidateTags`.

```ts
dispatch(api.util.invalidateTags([{ type: "Post", id: "LIST" }]));
```

It's useful after a websocket message tells you data changed, or from a listener.

### 237: How do you clear the whole RTK Query cache?

Dispatch `api.util.resetApiState()`. This removes all queries and mutations from that API. Components still mounted will refetch. A common use is on logout, so the next user doesn't see the previous user's data.

```ts
const logout = (): AppThunk => (dispatch) => {
  dispatch(loggedOut());
  dispatch(api.util.resetApiState());
};
```

### 238: What is `ApiProvider`?

A component that creates a small Redux store just for an RTK Query API. Use it only when your app doesn't have a Redux store and you only want RTK Query.

```tsx
import { ApiProvider } from "@reduxjs/toolkit/query/react";

<ApiProvider api={api}>
  <App />
</ApiProvider>;
```

Don't use it together with an existing Redux `Provider`. Add the API to your store instead.

### 239: How does RTK Query build a cache key?

From the endpoint name and the serialized query argument, for example `getPost(5)` or `getPosts({"page":2,"sort":"date"})`. The default serializer sorts object keys, so `{ a: 1, b: 2 }` and `{ b: 2, a: 1 }` share an entry. You can change this with `serializeQueryArgs`.

### 240: How do you make one query depend on another?

Pass `skipToken` to the second query until the first one has the value you need.

```tsx
const { data: user } = useGetUserQuery(userId);
const { data: projects } = useGetProjectsQuery(user?.orgId ?? skipToken);
```

### 241: What is the difference between `skip: true` and `skipToken`?

They behave the same at runtime: no request and no subscription. `skipToken` is better with TypeScript because it can replace the argument, so you don't need a non-null assertion. Also, with `skip` the result becomes uninitialized. Both clear `data` while skipped.

### 242: What is `structuralSharing` in RTK Query?

When new data arrives, RTK Query compares it with the old data and keeps the old references for parts that didn't change. That keeps re-renders low. It's on by default. For very large responses the comparison can cost a lot, so you can turn it off per endpoint:

```ts
getBigReport: build.query<Report, void>({
  query: () => 'report',
  structuralSharing: false,
}),
```

### 243: How do you store RTK Query results in normalized form?

Use an entity adapter in `transformResponse`.

```ts
const usersAdapter = createEntityAdapter<User>()

getUsers: build.query<EntityState<User, string>, void>({
  query: () => 'users',
  transformResponse: (response: User[]) =>
    usersAdapter.setAll(usersAdapter.getInitialState(), response),
}),

// selectors
const emptyUsers = usersAdapter.getInitialState()
const selectUsersResult = api.endpoints.getUsers.select()
const selectUsersData = createSelector(selectUsersResult, (r) => r.data)
export const { selectAll: selectAllUsers, selectById: selectUserById } =
  usersAdapter.getSelectors((state: RootState) => selectUsersData(state) ?? emptyUsers)
```

### 244: What does `keepUnusedDataFor: 0` do?

The cache entry is removed as soon as the last subscriber unmounts. Use it for data that should always be fresh or is sensitive. Note that it can cause refetches when a component quickly unmounts and mounts again.

### 245: What is `invalidationBehavior` in `createApi`?

It controls when invalidated queries refetch.

- `'delayed'` (default since RTK 2.0) - wait until no queries or mutations are pending, then refetch everything that was invalidated. This avoids extra requests when several mutations run close together.
- `'immediately'` - refetch right after each invalidation.

### 246: What does the lazy query trigger return?

A promise-like object with `unwrap()`, `abort()`, `unsubscribe()`, `refetch()` and the `arg`. The second argument `preferCacheValue` returns cached data without a request if it exists.

```tsx
const [getUser] = useLazyGetUserQuery();

const onSelect = async (id: string) => {
  const user = await getUser(id, true).unwrap();
  openProfile(user);
};
```

### 247: What are infinite queries in RTK Query?

Added in RTK 2.6, they handle "load more" and infinite scroll. One cache entry stores many pages, and RTK Query tracks the page params for you.

```ts
getPokemon: build.infiniteQuery<Pokemon[], string, number>({
  infiniteQueryOptions: {
    initialPageParam: 1,
    getNextPageParam: (lastPage, allPages, lastPageParam) =>
      lastPage.length === 0 ? undefined : lastPageParam + 1,
  },
  query: ({ queryArg, pageParam }) => `pokemon?type=${queryArg}&page=${pageParam}`,
}),
```

The generics are `<PageResult, QueryArg, PageParam>`.

### 248: How do you use the infinite query hook?

```tsx
function PokemonList({ type }: { type: string }) {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage, isLoading } =
    useGetPokemonInfiniteQuery(type);

  if (isLoading) return <p>Loading...</p>;

  const allPokemon = data?.pages.flat() ?? [];

  return (
    <>
      {allPokemon.map((p) => (
        <div key={p.id}>{p.name}</div>
      ))}
      <button
        disabled={!hasNextPage || isFetchingNextPage}
        onClick={() => fetchNextPage()}
      >
        {isFetchingNextPage ? "Loading..." : "Load more"}
      </button>
    </>
  );
}
```

`data` has the shape `{ pages, pageParams }`.

### 249: What does `getNextPageParam` receive and what should it return?

It receives `(lastPage, allPages, lastPageParam, allPageParams, queryArg)` and returns the param for the next page. Returning `undefined` or `null` means there are no more pages, which sets `hasNextPage` to `false`. `getPreviousPageParam` works the same way in the other direction.

### 250: What is schema validation in RTK Query?

Since RTK 2.7, endpoints accept schemas from any Standard Schema library (Zod, Valibot, ArkType and others) to check data at runtime.

```ts
import * as v from 'valibot'

const postSchema = v.object({ id: v.number(), title: v.string() })

getPost: build.query({
  query: (id: number) => `posts/${id}`,
  responseSchema: postSchema,
}),
```

You can validate `argSchema`, `rawResponseSchema` (before `transformResponse`), `responseSchema` (after), `errorResponseSchema` and `metaSchema`. The result type can also be inferred from the schema.

### 251: What happens when a schema check fails?

By default the endpoint throws a schema error, which is treated as an unhandled error. You can:

- Use `onSchemaFailure(error, info)` to log failures, for example to Sentry.
- Use `catchSchemaFailure` to turn the failure into a normal query error.
- Use `skipSchemaValidation` to turn validation off, for example in production or for specific schema types.

These can be set on `createApi` or per endpoint.

### 252: What is RTK Query code generation?

`@rtk-query/codegen-openapi` reads an OpenAPI (Swagger) spec and generates endpoints and hooks for you. You keep a small base API with `createApi`, and the generated file injects endpoints into it.

```ts
// openapi-config.ts
const config = {
  schemaFile: "https://api.example.com/openapi.json",
  apiFile: "./src/store/emptyApi.ts",
  apiImport: "emptySplitApi",
  outputFile: "./src/store/petApi.ts",
  exportName: "petApi",
  hooks: true,
};
export default config;
```

```bash
npx @rtk-query/codegen-openapi openapi-config.ts
```

Use `enhanceEndpoints` to add tags to the generated endpoints.

### 253: How do you set up the store for tests?

Export a function that creates a new store, so each test gets a clean one.

```ts
// store.ts
const rootReducer = combineSlices(counterSlice, api);
export type RootState = ReturnType<typeof rootReducer>;

export const setupStore = (preloadedState?: Partial<RootState>) =>
  configureStore({
    reducer: rootReducer,
    preloadedState,
    middleware: (gDM) => gDM().concat(api.middleware),
  });

export type AppStore = ReturnType<typeof setupStore>;
```

### 254: How do you write a `renderWithProviders` test helper?

```tsx
import { render, type RenderOptions } from "@testing-library/react";
import { Provider } from "react-redux";

interface ExtendedRenderOptions extends Omit<RenderOptions, "queries"> {
  preloadedState?: Partial<RootState>;
  store?: AppStore;
}

export function renderWithProviders(
  ui: React.ReactElement,
  {
    preloadedState = {},
    store = setupStore(preloadedState),
    ...renderOptions
  }: ExtendedRenderOptions = {},
) {
  const Wrapper = ({ children }: { children: React.ReactNode }) => (
    <Provider store={store}>{children}</Provider>
  );
  return { store, ...render(ui, { wrapper: Wrapper, ...renderOptions }) };
}
```

The Redux docs recommend integration tests like this over mocking hooks or the store.

### 255: How do you test components that use RTK Query?

Use a real store and mock the network with Mock Service Worker (MSW).

```ts
import { http, HttpResponse } from 'msw'
import { setupServer } from 'msw/node'

const server = setupServer(
  http.get('/api/posts', () => HttpResponse.json([{ id: 1, title: 'Hello' }])),
)

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

test('shows posts', async () => {
  renderWithProviders(<PostsList />)
  expect(await screen.findByText('Hello')).toBeInTheDocument()
})
```

### 256: How do you test a `createAsyncThunk`?

Dispatch it against a real store and check the resulting state, with the network mocked by MSW or the API client passed through the extra argument.

```ts
test("fetchTodos stores items", async () => {
  const store = setupStore();
  await store.dispatch(fetchTodos());
  expect(store.getState().todos.items).toHaveLength(2);
  expect(store.getState().todos.status).toBe("succeeded");
});
```

You can also check the returned action: `const action = await store.dispatch(fetchTodos()); expect(fetchTodos.fulfilled.match(action)).toBe(true)`.

### 257: How do you set up Redux Toolkit in the Next.js App Router?

Don't create one global store, because on the server it would be shared between requests. Create a store per request in a client component.

```tsx
// lib/store.ts
export const makeStore = () =>
  configureStore({
    reducer: rootReducer,
    middleware: (gDM) => gDM().concat(api.middleware),
  });
export type AppStore = ReturnType<typeof makeStore>;
export type RootState = ReturnType<AppStore["getState"]>;
export type AppDispatch = AppStore["dispatch"];

// app/StoreProvider.tsx
("use client");
import { useRef } from "react";
import { Provider } from "react-redux";
import { makeStore, type AppStore } from "../lib/store";

export default function StoreProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const storeRef = useRef<AppStore | null>(null);
  if (!storeRef.current) {
    storeRef.current = makeStore();
  }
  return <Provider store={storeRef.current}>{children}</Provider>;
}
```

Wrap the app in `StoreProvider` from the root layout. Server Components should not read or write the Redux store.

### 258: How do you pass server data into the store in Next.js?

Give `StoreProvider` a prop and dispatch it once when the store is created.

```tsx
export default function StoreProvider({
  count,
  children,
}: {
  count: number;
  children: React.ReactNode;
}) {
  const storeRef = useRef<AppStore | null>(null);
  if (!storeRef.current) {
    storeRef.current = makeStore();
    storeRef.current.dispatch(initializeCount(count));
  }
  return <Provider store={storeRef.current}>{children}</Provider>;
}
```

### 259: How do you migrate an old Redux codebase to Redux Toolkit?

Step by step, without rewriting everything at once:

1. Replace `createStore` with `configureStore`, passing your existing root reducer and middleware.
2. Convert one reducer at a time to `createSlice`. Old and new reducers can live side by side.
3. Replace hand-written thunks with `createAsyncThunk` or move data fetching to RTK Query.
4. Replace `connect` with `useSelector` and `useDispatch` where it helps.
5. Fix the warnings from the immutability and serializability checks, which often show real bugs.

### 260: How do you replace `connect` with hooks?

```tsx
// Before
const mapState = (state: RootState) => ({ todos: state.todos });
const mapDispatch = { toggleTodo };
export default connect(mapState, mapDispatch)(TodoList);

// After
export default function TodoList() {
  const todos = useAppSelector((state) => state.todos);
  const dispatch = useAppDispatch();
  // dispatch(toggleTodo(id))
}
```

`connect` still works and is supported, but hooks are the recommended API.

### 261: How do you reset all state on logout?

Wrap the root reducer and return `undefined` state for the logout action, so each slice reducer falls back to its initial state.

```ts
const appReducer = combineSlices(authSlice, cartSlice, api);

export const rootReducer: typeof appReducer = (state, action) => {
  if (loggedOut.match(action)) {
    return appReducer(undefined, action);
  }
  return appReducer(state, action);
};
```

Another option is for each slice to handle `loggedOut` in its own `extraReducers`, which is more explicit. For RTK Query, also dispatch `api.util.resetApiState()`.

### 262: How do you avoid circular imports between the store and slices?

- Import types with `import type { RootState } from './store'`. Type-only imports are removed at build time.
- Don't import the `store` instance into slices. Use `getState` in thunks and `dispatch` from hooks.
- If two slices need each other's actions, move the shared action into a separate file with `createAction`.

### 263: How do you add `meta` or `error` to an action with a prepare callback?

```ts
messageSent: {
  reducer(state, action: PayloadAction<Message, string, { sentAt: string }>) {
    state.messages.push({ ...action.payload, sentAt: action.meta.sentAt })
  },
  prepare(message: Message) {
    return { payload: message, meta: { sentAt: new Date().toISOString() } }
  },
},
```

### 264: What is the difference between `current` and `original`?

Both work on Immer drafts.

- `current(draft)` gives a plain snapshot of the draft's value right now, including changes made so far.
- `original(draft)` gives the value before this reducer made any changes.

```ts
itemsSorted(state) {
  const before = original(state.items)
  state.items.sort((a, b) => a.order - b.order)
  console.log(before === original(state.items)) // true
}
```

### 265: What is `isDraft`?

It checks whether a value is an Immer draft. It's useful in helper functions that might be called with either a draft or a plain object.

### 266: Why doesn't reassigning `state` work in a reducer?

```ts
reset(state) {
  state = initialState // does nothing
}
```

`state` is a local variable pointing to the draft. Reassigning it doesn't change the draft, so Immer sees no changes and returns the old state. Return the new value instead: `reset: () => initialState`.

### 267: Can you use a draft after an `await`?

No. Reducers are synchronous and the draft is finalized as soon as the reducer returns. If you save a reference to a draft and use it later, you get a "Cannot perform 'set' on a proxy that has been revoked" error. This usually happens when someone writes an async function as a reducer, which you should never do.

### 268: When does a component using `useSelector` re-render?

After every dispatch, React-Redux runs the selector and compares the result to the previous one with `===` (or your equality function). The component only re-renders if the result changed. A re-render of the parent also re-renders the child, as usual in React.

### 269: How do you keep `useSelector` from causing extra renders?

- Select the smallest piece of data you need.
- Don't return new objects or arrays from inline selectors. Use `createSelector` or `shallowEqual`.
- Select IDs in a list component and let each item component select its own item by ID.
- Use `selectFromResult` with RTK Query hooks.

### 270: How do you normalize nested API data?

Split nested objects into separate slices or adapters, and keep only IDs in parents.

```ts
// API: [{ id: 'p1', author: { id: 'u1', name: 'Ann' }, title: '...' }]

postsReceived(state, action: PayloadAction<ApiPost[]>) {
  usersAdapter.upsertMany(state.users, action.payload.map((p) => p.author))
  postsAdapter.setAll(
    state.posts,
    action.payload.map(({ author, ...post }) => ({ ...post, authorId: author.id })),
  )
}
```

For deep data, a library like `normalizr` can help.

### 271: How do you handle `selectById` returning `undefined`?

The item might not be loaded yet or might have been deleted, so always handle that case in the UI.

```tsx
const post = useAppSelector((state) => selectPostById(state, postId));
if (!post) {
  return <p>Post not found</p>;
}
```

### 272: What does `isAllOf` do?

It creates a matcher that only matches when all the given matchers match.

```ts
const isRejectedPostAction = isAllOf(isRejected, (action: UnknownAction) =>
  action.type.startsWith("posts/"),
);
```

### 273: What does `isAsyncThunkAction` do?

It matches any action dispatched by a `createAsyncThunk` thunk (pending, fulfilled or rejected). With arguments, it only matches those thunks.

```ts
builder.addMatcher(
  isAsyncThunkAction(fetchPosts, savePost),
  (state, action) => {
    state.lastRequestId = action.meta.requestId;
  },
);
```

### 274: What does the action creator check middleware catch?

It warns in development when you dispatch the action creator function instead of calling it:

```ts
dispatch(increment); // warning
dispatch(increment()); // correct
```

Without the check, the thunk middleware would call `increment` as if it were a thunk, and nothing obvious would happen.

### 275: How do you react to RTK Query results in a regular slice?

Every endpoint has matchers: `matchPending`, `matchFulfilled` and `matchRejected`.

```ts
const authSlice = createSlice({
  name: "auth",
  initialState: { token: null as string | null, user: null as User | null },
  reducers: {
    loggedOut: () => ({ token: null, user: null }),
  },
  extraReducers: (builder) => {
    builder.addMatcher(
      api.endpoints.login.matchFulfilled,
      (state, { payload }) => {
        state.token = payload.token;
        state.user = payload.user;
      },
    );
  },
});
```

### 276: How do you stop polling when a condition is met?

Make `pollingInterval` depend on the data.

```tsx
const [stopped, setStopped] = useState(false);
const { data } = useGetJobQuery(jobId, { pollingInterval: stopped ? 0 : 2000 });

useEffect(() => {
  if (data?.status === "done") setStopped(true);
}, [data]);
```

Setting the interval to `0` turns polling off.

### 277: How do you use response headers in `transformResponse`?

The second argument is `meta`, which has `request` and `response` for `fetchBaseQuery`.

```ts
getPosts: build.query<{ posts: Post[]; total: number }, number>({
  query: (page) => `posts?page=${page}`,
  transformResponse: (posts: Post[], meta) => ({
    posts,
    total: Number(meta?.response?.headers.get('X-Total-Count') ?? 0),
  }),
}),
```

### 278: What happens to `providesTags` when a query fails?

The function is still called, with `result` as `undefined` and `error` set. If you don't return any tags, an error result won't be refetched on invalidation. A common approach is to return a generic tag on error:

```ts
providesTags: (result, error) =>
  result ? result.map(({ id }) => ({ type: 'Post' as const, id })) : ['UNKNOWN_ERROR'],
```

Then invalidating `'UNKNOWN_ERROR'` (for example after login) retries failed queries.

### 279: What is `extraOptions` on an endpoint?

An object passed as the third argument to the base query. Use it to change base query behavior per endpoint, like retries or a different auth mode.

```ts
const baseQuery: BaseQueryFn<string | FetchArgs, unknown, FetchBaseQueryError, { skipAuth?: boolean }> =
  async (args, api, extraOptions) => {
    // read extraOptions?.skipAuth here
    return rawBaseQuery(args, api, extraOptions)
  }

getPublicConfig: build.query<Config, void>({
  query: () => 'config',
  extraOptions: { skipAuth: true },
}),
```

### 280: Can you use the hooks from `api.endpoints` instead of the named exports?

Yes. `api.endpoints.getPosts.useQuery()` is the same hook as `useGetPostsQuery()`. The named exports are just shortcuts. The endpoint object form is handy when you pick the endpoint dynamically or in shared helpers.

### 281: How do you type a query that takes no argument?

Use `void` as the argument type. The hook can then be called with no arguments.

```ts
getPosts: build.query<Post[], void>({ query: () => "posts" });

useGetPostsQuery();
useGetPostsQuery(undefined, { pollingInterval: 3000 });
```

### 282: How do you set defaults for all endpoints in an API?

Pass them to `createApi`. Endpoints and hooks can override them.

```ts
export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  keepUnusedDataFor: 120,
  refetchOnFocus: true,
  refetchOnReconnect: true,
  refetchOnMountOrArgChange: 30,
  tagTypes: ["Post", "User"],
  endpoints: () => ({}),
});
```

### 283: How do you download a file with RTK Query?

You can use a custom `responseHandler`, but a `Blob` is not serializable and shouldn't go into the cache. A cleaner option is a `queryFn` or a mutation that saves the file directly and returns nothing:

```ts
downloadReport: build.mutation<null, string>({
  queryFn: async (id, _api, _extra, baseQuery) => {
    const result = await baseQuery({
      url: `reports/${id}/file`,
      responseHandler: async (response) => {
        const url = URL.createObjectURL(await response.blob())
        const a = document.createElement('a')
        a.href = url
        a.download = `report-${id}.pdf`
        a.click()
        URL.revokeObjectURL(url)
        return null
      },
      cache: 'no-cache',
    })
    return result.error ? { error: result.error } : { data: null }
  },
}),
```

### 284: How do you read the arguments of a mutation from its result?

The mutation result has `originalArgs`, which holds the arguments of the last call.

```tsx
const [deletePost, { isLoading, originalArgs }] = useDeletePostMutation();

{
  posts.map((p) => (
    <button key={p.id} onClick={() => deletePost(p.id)}>
      {isLoading && originalArgs === p.id ? "Deleting..." : "Delete"}
    </button>
  ));
}
```

### 285: How do you create a memoized selector for derived RTK Query data inside a component?

Create the selector with `useMemo` so each component instance has its own.

```tsx
function UserPosts({ userId }: { userId: string }) {
  const selectPostsForUser = useMemo(
    () =>
      createSelector(
        [
          (res: { data?: Post[] }) => res.data,
          (_res: unknown, id: string) => id,
        ],
        (data, id) => data?.filter((p) => p.userId === id) ?? [],
      ),
    [],
  );

  const { postsForUser } = useGetPostsQuery(undefined, {
    selectFromResult: (result) => ({
      ...result,
      postsForUser: selectPostsForUser(result, userId),
    }),
  });
}
```

### 286: Why does React 18 batching matter for Redux?

React 18 batches all state updates in event handlers, timeouts and promises by default. Several dispatches in a row inside one event or async callback lead to one render. React-Redux 9 uses `useSyncExternalStore`, so updates from the store work correctly with concurrent rendering and don't cause "tearing" where components show different versions of the state.

### 287: How do you create a reusable slice factory?

Wrap `createSlice` in a function. Keep the types generic so the result is still well typed.

```ts
interface GenericState<T> {
  data?: T;
  status: "idle" | "loading" | "finished" | "error";
}

export const createGenericSlice = <
  T,
  Reducers extends SliceCaseReducers<GenericState<T>>,
>({
  name = "",
  initialState,
  reducers,
}: {
  name: string;
  initialState: GenericState<T>;
  reducers: ValidateSliceCaseReducers<GenericState<T>, Reducers>;
}) =>
  createSlice({
    name,
    initialState,
    reducers: {
      start(state) {
        state.status = "loading";
      },
      success(state: GenericState<T>, action: PayloadAction<T>) {
        state.data = action.payload;
        state.status = "finished";
      },
      ...reducers,
    },
  });
```

### 288: When should you split state into multiple slices?

Split by feature or by domain data, not by component. A slice should own data that changes together and has its own actions. Signs a slice is too big: unrelated fields, many reducers that touch only part of the state, or merge conflicts between teams. Signs slices are too small: many actions that must update several slices together every time.

### 289: How do you share one action between several slices?

Define it once and handle it in each slice's `extraReducers`.

```ts
// app/actions.ts
export const appReset = createAction("app/reset");

// in each slice
extraReducers: (builder) => {
  builder.addCase(appReset, () => initialState);
};
```

Or define it in one slice and import it into others.

### 290: How do you handle global loading state for many thunks?

Use a matcher in a UI slice.

```ts
const uiSlice = createSlice({
  name: "ui",
  initialState: { pendingRequests: 0 },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addMatcher(isPending, (state) => {
        state.pendingRequests += 1;
      })
      .addMatcher(isAnyOf(isFulfilled, isRejected), (state) => {
        state.pendingRequests -= 1;
      });
  },
});
```

Show a global spinner when `pendingRequests > 0`.

### 291: How do you show a toast for every failed RTK Query request?

Use a middleware (or listener) with `isRejectedWithValue`.

```ts
export const errorToastMiddleware: Middleware = () => (next) => (action) => {
  if (isRejectedWithValue(action)) {
    const payload = action.payload as { data?: { message?: string } };
    toast.error(payload.data?.message ?? "Request failed");
  }
  return next(action);
};
```

`rejectWithValue` covers server error responses. Errors thrown in your own code show up as `isRejected` without a value.

### 292: How does `createSlice` infer action types from reducers?

For each reducer, TypeScript looks at the type of the `action` parameter. A reducer with `action: PayloadAction<number>` produces an action creator that takes a `number`. A reducer with no `action` parameter produces one with no arguments. A reducer object with `prepare` uses the prepare function's parameters.

### 293: How do you type `initialState` correctly in a slice?

Declare an interface and type the variable, or use `as` on the initial value. Otherwise TypeScript infers too narrow types, like `null` instead of `string | null`.

```ts
interface AuthState {
  user: User | null;
  status: "idle" | "loading";
}

const initialState: AuthState = { user: null, status: "idle" };

const authSlice = createSlice({ name: "auth", initialState, reducers: {} });
```

### 294: What is `AnyAction` and why should you stop using it?

`AnyAction` typed every extra field as `any`, which hid type errors. It's deprecated in Redux 5. Use `UnknownAction` and narrow with `.match()` or type guards, or use `Action` when you only need `type`.

### 295: What is `PayloadActionCreator`?

The type of action creators made by `createAction` and `createSlice`. You rarely write it, but it's useful when a function receives an action creator as a parameter.

```ts
function logWhen<P>(creator: PayloadActionCreator<P>) {
  return (action: UnknownAction) =>
    creator.match(action) && console.log(action.payload);
}
```

### 296: What is `ThunkDispatch`?

The `dispatch` type that knows about thunks. You normally get it via `AppDispatch`, but you can write it manually: `ThunkDispatch<RootState, ExtraArg, UnknownAction>`.

### 297: How do you keep request status for each item separately?

Store status by ID.

```ts
interface UsersState {
  statusById: Record<string, "idle" | "loading" | "failed" | "succeeded">;
}

builder
  .addCase(fetchUser.pending, (state, action) => {
    state.statusById[action.meta.arg] = "loading";
  })
  .addCase(fetchUser.fulfilled, (state, action) => {
    state.statusById[action.meta.arg] = "succeeded";
  });
```

RTK Query does this automatically per cache entry.

### 298: How do you make a slice state persist to `localStorage` without a library?

Read it as the preloaded state and save it with a listener.

```ts
const saved = localStorage.getItem("settings");

export const store = configureStore({
  reducer: rootReducer,
  preloadedState: saved ? { settings: JSON.parse(saved) } : undefined,
  middleware: (gDM) => gDM().prepend(listenerMiddleware.middleware),
});

startAppListening({
  predicate: (_action, current, previous) =>
    current.settings !== previous.settings,
  effect: (_action, api) => {
    localStorage.setItem("settings", JSON.stringify(api.getState().settings));
  },
});
```

### 299: What is the difference between `createAsyncThunk` returning a value and calling `fulfillWithValue`?

Returning a value is the normal way, and the value becomes `action.payload`. `fulfillWithValue` does the same but also lets you set `action.meta` fields. You only need it when you want custom meta on the fulfilled action.

### 300: How do you handle optimistic updates for a list and a detail query at the same time?

Patch both cache entries and undo both on failure.

```ts
async onQueryStarted({ id, ...patch }, { dispatch, queryFulfilled }) {
  const patches = [
    dispatch(api.util.updateQueryData('getPost', id, (draft) => {
      Object.assign(draft, patch)
    })),
    dispatch(api.util.updateQueryData('getPosts', undefined, (draft) => {
      const post = draft.find((p) => p.id === id)
      if (post) Object.assign(post, patch)
    })),
  ]
  try {
    await queryFulfilled
  } catch {
    patches.forEach((p) => p.undo())
  }
},
```

If the list is cached under several arguments (pages, filters), see question 351 for how to update all of them.

## Advanced Questions

### 301: How is the RTK Query cache stored in the Redux state?

Under `state[reducerPath]` there are a few sections:

- `queries` - one entry per cache key with `status`, `data`, `error`, `originalArgs`, `endpointName`, `requestId`, timestamps.
- `mutations` - one entry per mutation request (or per `fixedCacheKey`).
- `provided` - a map from tags to the cache keys that provide them, used for invalidation.
- `subscriptions` - which components or callers are subscribed to which cache entries.
- `config` - things like `online`, `focused` and `keepUnusedDataFor`.

This shape is internal and has changed between versions. Read data with the endpoint `select` functions and hooks, not by reaching into the state directly.

### 302: How does RTK Query decide when to remove cached data?

It uses reference counting. Every `useQuery` call, or `initiate` without `subscribe: false`, adds a subscription to the cache entry. When a subscription is removed (component unmounts or `unsubscribe()` is called) and the count reaches zero, the middleware starts a timer for `keepUnusedDataFor` seconds. If no one subscribes before the timer ends, the entry is removed. A new subscription cancels the timer.

### 303: What happens step by step when a component calls `useGetPostQuery(5)`?

1. On mount, the hook dispatches `api.endpoints.getPost.initiate(5)`.
2. The thunk adds a subscription for this component to the cache key `getPost(5)`.
3. If there is no data, or `refetchOnMountOrArgChange` says it's stale, the query thunk starts. A `pending` action creates or updates the cache entry.
4. The base query runs. On success, a `fulfilled` action saves `data` and the provided tags. On failure, `rejected` saves the `error`.
5. The hook uses `useSelector` on the cache entry and returns the derived flags (`isLoading`, `isFetching` and so on).
6. On unmount or argument change, the hook removes its subscription, and the cache lifetime logic from the previous question takes over.

If another component already has an in-flight request for the same key, step 3 is skipped and both wait for the same request.

### 304: How do you handle streaming updates (websockets) with RTK Query?

Use `onCacheEntryAdded`. It runs once when a cache entry is created and lets you keep it updated until it's removed.

```ts
getMessages: build.query<Message[], string>({
  query: (channel) => `messages/${channel}`,
  async onCacheEntryAdded(channel, { updateCachedData, cacheDataLoaded, cacheEntryRemoved }) {
    const ws = new WebSocket('wss://chat.example.com')
    try {
      await cacheDataLoaded

      ws.addEventListener('message', (event: MessageEvent) => {
        const message = JSON.parse(event.data) as Message
        if (message.channel !== channel) return
        updateCachedData((draft) => {
          draft.push(message)
        })
      })
    } catch {
      // cacheEntryRemoved resolved before cacheDataLoaded
    }
    await cacheEntryRemoved
    ws.close()
  },
}),
```

The initial data comes from the normal request. The socket only adds updates.

### 305: What are `cacheDataLoaded` and `cacheEntryRemoved`?

Two promises given to `onCacheEntryAdded`:

- `cacheDataLoaded` resolves with `{ data, meta }` when the first value is saved in the cache. It rejects if the entry is removed before any data arrives, which is why you wrap it in `try/catch`.
- `cacheEntryRemoved` resolves when the cache entry is removed, which is your signal to clean up subscriptions, sockets and timers.

### 306: What is the difference between `updateCachedData` and `api.util.updateQueryData`?

`updateCachedData` is only available inside `onQueryStarted` (for queries) and `onCacheEntryAdded`. It updates the current cache entry without you passing the endpoint name and argument. `api.util.updateQueryData` is a thunk you can dispatch from anywhere, and you must say which entry to update. It also returns a patch result with `undo`.

### 307: How do you refresh an expired token automatically in RTK Query?

Wrap the base query. On a 401, call the refresh endpoint, save the new token and retry. A mutex stops several parallel requests from all refreshing at once.

```ts
import { Mutex } from "async-mutex";

const mutex = new Mutex();
const rawBaseQuery = fetchBaseQuery({ baseUrl: "/api", prepareHeaders });

export const baseQueryWithReauth: BaseQueryFn<
  string | FetchArgs,
  unknown,
  FetchBaseQueryError
> = async (args, api, extraOptions) => {
  await mutex.waitForUnlock();
  let result = await rawBaseQuery(args, api, extraOptions);

  if (result.error?.status === 401) {
    if (!mutex.isLocked()) {
      const release = await mutex.acquire();
      try {
        const refresh = await rawBaseQuery(
          { url: "auth/refresh", method: "POST" },
          api,
          extraOptions,
        );
        if (refresh.data) {
          api.dispatch(tokenReceived(refresh.data as TokenResponse));
          result = await rawBaseQuery(args, api, extraOptions);
        } else {
          api.dispatch(loggedOut());
        }
      } finally {
        release();
      }
    } else {
      await mutex.waitForUnlock();
      result = await rawBaseQuery(args, api, extraOptions);
    }
  }
  return result;
};
```

### 308: How do you call two different backends from one API?

Use a base query that picks the target based on the args, or use `queryFn` for the odd endpoints. Both still share one cache and one set of tags.

```ts
const usersBaseQuery = fetchBaseQuery({ baseUrl: "https://users.example.com" });
const billingBaseQuery = fetchBaseQuery({
  baseUrl: "https://billing.example.com",
});

const multiBaseQuery: BaseQueryFn<
  FetchArgs & { service?: "users" | "billing" }
> = (args, api, extra) =>
  args.service === "billing"
    ? billingBaseQuery(args, api, extra)
    : usersBaseQuery(args, api, extra);
```

If the two services don't share data or tags at all, two separate `createApi` instances are also fine.

### 309: How do you use RTK Query with GraphQL?

Write or use a GraphQL base query. There is an official one built on `graphql-request`:

```ts
import { graphqlRequestBaseQuery } from "@rtk-query/graphql-request-base-query";
import { gql } from "graphql-request";

export const api = createApi({
  baseQuery: graphqlRequestBaseQuery({ url: "/graphql" }),
  endpoints: (build) => ({
    getPosts: build.query<GetPostsResponse, { page: number }>({
      query: ({ page }) => ({
        document: gql`
          query GetPosts($page: Int) {
            posts(page: $page) {
              id
              title
            }
          }
        `,
        variables: { page },
      }),
    }),
  }),
});
```

GraphQL Codegen also has a plugin that generates RTK Query endpoints from your operations.

### 310: What is `buildCreateApi` and when do you need it?

`createApi` is built from modules: `coreModule` (cache and thunks) and `reactHooksModule` (hooks). `buildCreateApi` lets you build your own `createApi`. A common reason is using a custom React-Redux context, so the hooks read from the right store:

```ts
import {
  buildCreateApi,
  coreModule,
  reactHooksModule,
} from "@reduxjs/toolkit/query/react";
import {
  createDispatchHook,
  createSelectorHook,
  createStoreHook,
} from "react-redux";

export const MyContext = React.createContext<ReactReduxContextValue | null>(
  null,
);

export const createApi = buildCreateApi(
  coreModule(),
  reactHooksModule({
    hooks: {
      useDispatch: createDispatchHook(MyContext),
      useSelector: createSelectorHook(MyContext),
      useStore: createStoreHook(MyContext),
    },
  }),
);
```

### 311: What happens if `injectEndpoints` adds an endpoint name that already exists?

By default the existing definition is kept and a warning is logged in development. Pass `overrideExisting: true` to replace it, or `'throw'` to throw an error. Overriding is mostly useful with hot reloading.

```ts
api.injectEndpoints({
  endpoints: (build) => ({/* ... */}),
  overrideExisting: process.env.NODE_ENV === "development",
});
```

### 312: How do you code split both reducers and API endpoints for a lazy route?

Put both injections in the lazy-loaded module. When the route chunk loads, the slice is injected into `combineSlices` and the endpoints are added to the base API.

```ts
// features/admin/index.ts (loaded with React.lazy)
import { rootReducer } from "../../app/rootReducer";
import { api } from "../../services/api";
import { adminSlice } from "./adminSlice";

adminSlice.injectInto(rootReducer);

export const adminApi = api.injectEndpoints({
  endpoints: (build) => ({
    getAuditLog: build.query<AuditEntry[], void>({
      query: () => "admin/audit",
    }),
  }),
});
```

The API's reducer and middleware are added once in the main bundle. Only the endpoint definitions are split.

### 313: What is `createDynamicMiddleware`?

An RTK 2.0 API that lets you add middleware after the store is created, for code-split features.

```ts
import { createDynamicMiddleware } from "@reduxjs/toolkit";

export const dynamicMiddleware = createDynamicMiddleware();

export const store = configureStore({
  reducer: rootReducer,
  middleware: (gDM) => gDM().prepend(dynamicMiddleware.middleware),
});

// later, in a lazy-loaded feature
dynamicMiddleware.addMiddleware(featureMiddleware);
```

Adding the same middleware twice is ignored, so it's safe to call from module top level. You can also dispatch `dynamicMiddleware.withMiddleware(mw)`, which adds it and returns the extended `dispatch`.

### 314: How do you use dynamic middleware from a React component?

Import from `@reduxjs/toolkit/react`. That version adds `createDispatchWithMiddlewareHook`, which adds the middleware and gives you a typed `dispatch`.

```ts
import { createDynamicMiddleware } from "@reduxjs/toolkit/react";

export const dynamicMiddleware = createDynamicMiddleware();
export const useDispatchWithAnalytics =
  dynamicMiddleware.createDispatchWithMiddlewareHook(analyticsMiddleware);

function Checkout() {
  const dispatch = useDispatchWithAnalytics();
  // ...
}
```

### 315: What does `listenerApi.fork` do?

It starts a child task inside an effect. The child runs in parallel, can be cancelled independently, and is cancelled automatically when the parent effect is cancelled.

```ts
startAppListening({
  actionCreator: pollingStarted,
  effect: async (action, listenerApi) => {
    const task = listenerApi.fork(async (forkApi) => {
      while (true) {
        await forkApi.delay(5000);
        const status = await forkApi.pause(api.fetchStatus());
        listenerApi.dispatch(statusReceived(status));
      }
    });

    await listenerApi.condition(pollingStopped.match);
    task.cancel();
  },
});
```

The task's `result` promise resolves to `{ status: 'ok', value }`, `{ status: 'rejected', error }` or `{ status: 'cancelled', error }`.

### 316: What is `autoJoin` in `fork`?

`listenerApi.fork(executor, { autoJoin: true })` makes the parent effect wait for the child to finish before the parent counts as done. Without it, the parent can finish while the child keeps running (until the parent is cancelled). It's useful when cancellation of the parent should also be the only way the child stops, and you want `cancelActiveListeners` to reach it.

### 317: What is a `TaskAbortError`?

The error that cancellation-aware methods throw when the effect or fork is cancelled: `delay`, `pause`, `take`, `condition`, `throwIfCancelled`. The listener middleware catches it, so you don't see it as an unhandled error. If you have your own `try/catch`, check for it and re-throw or exit:

```ts
try {
  await listenerApi.delay(1000);
} catch (err) {
  if (err instanceof TaskAbortError) return;
  throw err;
}
```

Plain `await fetch(...)` is not cancellation-aware. Wrap it in `listenerApi.pause(...)` or pass `listenerApi.signal` to `fetch`.

### 318: How are errors in listener effects handled?

Errors thrown in an effect don't break the dispatch. They are passed to `onError`, which logs them by default. Set your own handler to report them.

```ts
export const listenerMiddleware = createListenerMiddleware({
  onError: (error, errorInfo) => {
    Sentry.captureException(error, { extra: { raisedBy: errorInfo.raisedBy } });
  },
});
```

`raisedBy` tells you whether the error came from the effect or the predicate.

### 319: What are the limits of `getOriginalState`?

It returns the state from before the current action was processed. It can only be called synchronously during the first part of the effect, before any `await`. Calling it later throws an error, because after other actions run, "original" would no longer mean anything clear.

### 320: How do you make a listener run only once?

Call `listenerApi.unsubscribe()` at the start of the effect.

```ts
startAppListening({
  actionCreator: appLoaded,
  effect: async (action, listenerApi) => {
    listenerApi.unsubscribe();
    await initAnalytics();
  },
});
```

You can call `listenerApi.subscribe()` later to turn it back on. That makes "wait for X, do Y, then listen again" flows possible.

### 321: How do you write a long-running workflow with the listener middleware?

Use `take` and `condition` to wait for steps, and `cancelActiveListeners` to make sure only one instance runs.

```ts
startAppListening({
  actionCreator: checkoutStarted,
  effect: async (action, listenerApi) => {
    listenerApi.cancelActiveListeners();

    const paymentResult = await listenerApi.take(
      isAnyOf(paymentSucceeded, paymentFailed),
      5 * 60_000,
    );
    if (!paymentResult) {
      listenerApi.dispatch(checkoutTimedOut());
      return;
    }

    const [paymentAction] = paymentResult;
    if (paymentSucceeded.match(paymentAction)) {
      await listenerApi.pause(
        orderService.confirm(paymentAction.payload.orderId),
      );
      listenerApi.dispatch(checkoutCompleted());
    } else {
      listenerApi.dispatch(checkoutFailed());
    }
  },
});
```

### 322: How do you throttle with the listener middleware?

Ignore new actions while the effect is "cooling down". One way is to unsubscribe, wait, then subscribe again.

```ts
startAppListening({
  actionCreator: scrollPositionChanged,
  effect: async (action, listenerApi) => {
    listenerApi.unsubscribe();
    saveScrollPosition(action.payload);
    await listenerApi.delay(500);
    listenerApi.subscribe();
  },
});
```

### 323: How do Redux-Saga effects map to the listener middleware?

| Saga              | Listener                                               |
| ----------------- | ------------------------------------------------------ |
| `takeEvery`       | a normal `startListening`                              |
| `takeLatest`      | `cancelActiveListeners()` at the start of the effect   |
| `takeLeading`     | `unsubscribe()` at the start, `subscribe()` at the end |
| `take`            | `listenerApi.take`                                     |
| `call`            | `await` (or `listenerApi.pause` for cancellation)      |
| `put`             | `listenerApi.dispatch`                                 |
| `select`          | `listenerApi.getState`                                 |
| `fork` / `cancel` | `listenerApi.fork` / `task.cancel()`                   |
| `delay`           | `listenerApi.delay`                                    |
| `race`            | `Promise.race` with `take` or `condition`              |

The listener middleware uses async/await instead of generators, so it's easier to type and read.

### 324: How do you fetch RTK Query data on the server for SSR?

Dispatch the queries, wait for all running queries, then send the state to the client.

```ts
export async function renderPage(req: Request) {
  const store = makeStore()
  store.dispatch(api.endpoints.getPosts.initiate())
  store.dispatch(api.endpoints.getUser.initiate(req.userId))

  await Promise.all(store.dispatch(api.util.getRunningQueriesThunk()))

  const html = renderToString(
    <Provider store={store}>
      <App />
    </Provider>,
  )
  return { html, preloadedState: store.getState() }
}
```

On the client, create the store with that `preloadedState`. The hooks find the data in the cache and don't refetch.

### 325: What is `extractRehydrationInfo`?

A `createApi` option that tells RTK Query how to find its state inside a "hydrate" action from another library, like `next-redux-wrapper` (`HYDRATE`) or `redux-persist` (`REHYDRATE`).

```ts
import { HYDRATE } from "next-redux-wrapper";

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: "/api" }),
  extractRehydrationInfo(action, { reducerPath }) {
    if (action.type === HYDRATE) {
      return (action as any).payload[reducerPath];
    }
  },
  endpoints: () => ({}),
});
```

RTK Query then merges the hydrated entries correctly instead of you overwriting its state.

### 326: Should you persist the RTK Query cache with `redux-persist`?

Usually not. The cache is meant to be short-lived and refetched. Persisting it can show outdated data, keep entries in a "pending" state after reload, and fill storage. If you really need offline data, persist only fulfilled entries and use `extractRehydrationInfo` to restore them, or keep offline data in your own slice.

### 327: How do you build bidirectional infinite scrolling with a page limit?

Provide `getPreviousPageParam` and `maxPages`. When the limit is reached, pages at the other end are dropped from the cache.

```ts
getFeed: build.infiniteQuery<FeedPage, void, number>({
  infiniteQueryOptions: {
    initialPageParam: 0,
    maxPages: 3,
    getNextPageParam: (lastPage, _all, lastPageParam) =>
      lastPage.hasMore ? lastPageParam + 1 : undefined,
    getPreviousPageParam: (_firstPage, _all, firstPageParam) =>
      firstPageParam > 0 ? firstPageParam - 1 : undefined,
  },
  query: ({ pageParam }) => `feed?page=${pageParam}`,
}),
```

`maxPages` requires both page param functions, so the user can scroll back to dropped pages. This keeps memory use flat on very long lists.

### 328: How do you use cursor-based pagination with infinite queries?

Make the page param the cursor and read the next cursor from the last page.

```ts
interface ItemsPage {
  items: Item[]
  nextCursor: string | null
}

getItems: build.infiniteQuery<ItemsPage, string, string>({
  infiniteQueryOptions: {
    initialPageParam: '',
    getNextPageParam: (lastPage) => lastPage.nextCursor ?? undefined,
  },
  query: ({ queryArg, pageParam }) => ({
    url: 'items',
    params: { search: queryArg, ...(pageParam ? { cursor: pageParam } : {}) },
  }),
}),
```

### 329: What happens when an infinite query is refetched or invalidated?

RTK Query refetches all cached pages in order, starting from the first page param, and calls `getNextPageParam` after each page. This keeps the pages consistent, since items might have moved between pages. With many pages this means many requests, which is another reason to use `maxPages`.

### 330: How was infinite scroll done before infinite queries existed?

With `serializeQueryArgs`, `merge` and `forceRefetch` on a normal query, so all pages share one cache entry:

```ts
listItems: build.query<Item[], number>({
  query: (page) => `items?page=${page}`,
  serializeQueryArgs: ({ endpointName }) => endpointName,
  merge: (currentCache, newItems) => {
    currentCache.push(...newItems)
  },
  forceRefetch: ({ currentArg, previousArg }) => currentArg !== previousArg,
}),
```

This still works, but invalidation and refetching are awkward, because RTK Query only knows the last page argument. Use `build.infiniteQuery` for new code.

### 331: When would you write a custom `serializeQueryArgs`?

When some arguments shouldn't create separate cache entries. For example, a callback or a "request source" field that doesn't change the data.

```ts
search: build.query<Result[], { term: string; trackingId: string }>({
  query: ({ term }) => `search?q=${term}`,
  serializeQueryArgs: ({ queryArgs }) => ({ term: queryArgs.term }),
}),
```

Returning an object or primitive is fine. RTK Query serializes it with the default serializer.

### 332: What does `forceRefetch` do?

A function `({ currentArg, previousArg, state, endpointState }) => boolean` that decides if a request should be made even though there's a cache entry for the key. It's used together with `serializeQueryArgs` when several arguments map to one cache entry.

### 333: How do you combine optimistic updates with invalidation as a safety net?

Patch the cache optimistically. On failure, undo the patch. If the undo might not be exact (for example, other changes happened in the meantime), invalidate the tag so the data refetches from the server.

```ts
async onQueryStarted({ id, ...patch }, { dispatch, queryFulfilled }) {
  const patchResult = dispatch(
    api.util.updateQueryData('getPost', id, (draft) => {
      Object.assign(draft, patch)
    }),
  )
  try {
    await queryFulfilled
  } catch {
    patchResult.undo()
    dispatch(api.util.invalidateTags([{ type: 'Post', id }]))
  }
},
```

### 334: What is `patchQueryData`?

It applies Immer patches to a cache entry. `updateQueryData` returns `patches` and `inversePatches`, so you can store them and apply them later, for example to build undo/redo or to replay changes from another tab.

```ts
const { inversePatches } = dispatch(
  api.util.updateQueryData("getTodos", undefined, recipe),
);
// later
dispatch(api.util.patchQueryData("getTodos", undefined, inversePatches));
```

### 335: What is the `updateProvided` argument of `updateQueryData`?

By default, manual cache updates don't recalculate the entry's provided tags. If your update adds or removes items (and so changes which tags the entry should provide), pass `true` as the fourth argument so `providesTags` runs again. Otherwise later invalidations might miss the new items.

```ts
dispatch(
  api.util.updateQueryData(
    "getPosts",
    undefined,
    (draft) => {
      draft.push(newPost);
    },
    true,
  ),
);
```

### 336: What is `api.util.selectInvalidatedBy`?

A selector that returns the cache entries that would be invalidated by a list of tags, without invalidating them. Each item has `endpointName`, `originalArgs` and `queryCacheKey`.

```ts
const entries = api.util.selectInvalidatedBy(getState(), [
  { type: "Post", id: 5 },
]);
// [{ endpointName: 'getPost', originalArgs: 5, queryCacheKey: 'getPost(5)' }, ...]
```

### 337: What is `api.util.selectCachedArgsForQuery`?

It returns all arguments currently in the cache for one endpoint. It's a simpler option than `selectInvalidatedBy` when you know the endpoint name.

```ts
const pagesInCache = api.util.selectCachedArgsForQuery(getState(), "getPosts");
// [{ page: 1 }, { page: 2 }]
```

### 338: Is the RTK Query cache normalized?

No. It is a document cache: each endpoint plus argument has its own copy of the response. If one post appears in a list and a detail query, it is stored twice. Tags and refetching keep them in sync. This is simpler, matches how most REST APIs work, and avoids the cost of normalizing. The trade-off is that updates to one entity don't show up in other entries automatically. You either invalidate tags or update each entry manually.

### 339: What is the difference between `onQueryStarted` and `onCacheEntryAdded`?

- `onQueryStarted` runs every time a request starts for the endpoint (including refetches). Use it for optimistic updates and reacting to one request.
- `onCacheEntryAdded` runs once when a cache entry is created, and its promises let you work until the entry is removed. Use it for long-lived things like sockets.

Mutations have both too, but `onCacheEntryAdded` is rarely useful there.

### 340: What should you know about memory with `weakMapMemoize`?

It caches results per unique set of arguments, using `WeakMap` for objects and `Map` for primitives. Object keys (like the state) can be garbage collected, but primitive arguments (like many different IDs) stay in the cache as long as the selector exists. For selectors called with a very large number of different primitive arguments, consider `lruMemoize` with a `maxSize`, or create a selector per component instance. You can call `selector.clearCache()` to reset it.

### 341: How do you avoid re-rendering every row when one item in an RTK Query list changes?

Have the list component select only IDs and pass the ID to each row. Each row selects its own item with `selectFromResult`.

```tsx
function PostList() {
  const { ids } = useGetPostsQuery(undefined, {
    selectFromResult: ({ data }) => ({ ids: data?.ids ?? emptyIds }),
  });
  return ids.map((id) => <PostRow key={id} id={id} />);
}

function PostRow({ id }: { id: number }) {
  const { post } = useGetPostsQuery(undefined, {
    selectFromResult: ({ data }) => ({ post: data?.entities[id] }),
  });
  return <div>{post?.title}</div>;
}
```

This assumes the data is normalized with an entity adapter in `transformResponse`. `emptyIds` should be a constant so the fallback reference is stable. With structural sharing, unchanged posts keep the same reference, so their rows don't re-render. Wrap `PostRow` in `React.memo` too.

### 342: How do you mark your own actions as low priority for the `autoBatchEnhancer`?

Use `prepareAutoBatched` as the prepare callback. It adds `meta[SHOULD_AUTOBATCH] = true`.

```ts
import { prepareAutoBatched } from "@reduxjs/toolkit";

const cursorSlice = createSlice({
  name: "cursor",
  initialState: { x: 0, y: 0 },
  reducers: {
    cursorMoved: {
      reducer(state, action: PayloadAction<{ x: number; y: number }>) {
        state.x = action.payload.x;
        state.y = action.payload.y;
      },
      prepare: prepareAutoBatched<{ x: number; y: number }>(),
    },
  },
});
```

The reducer still runs right away. Only the subscriber notification is delayed, so the UI updates once per frame instead of once per action. Any normal action dispatched in the meantime flushes the notification immediately.

### 343: How do you deal with slow dev checks in a large app?

The immutability and serializability checks walk the whole state after every action. With a large state this can make development slow, and you'll see warnings like "SerializableStateInvariantMiddleware took 120ms".

- Ignore large paths that you know are safe with `ignoredPaths`.
- Raise `warnAfter` if the time is acceptable.
- Turn a check off for some environments: `immutableCheck: false`.
- Move big data that doesn't need to be in Redux (like large files) out of the store.

These checks never run in production builds.

### 344: How do you keep Immer fast in reducers?

- Avoid deep copying or touching many items when you only change one. Immer only copies what you modify.
- For large arrays, replacing the whole array (`state.items = newItems`) is cheaper than many `push` calls.
- Don't read and write in a loop over thousands of drafts if you can build a new value first and assign it once.
- Don't put huge, never-changing data in the store. If you must, `Object.freeze` it before it goes in, so Immer can skip it when it freezes the new state.
- Use `current()` only for debugging, since it copies the draft.

In most apps Immer's cost is small compared to rendering.

### 345: Does Immer freeze the state, and can you turn that off?

Yes. Immer freezes the produced state with `Object.freeze` by default, in development and production, so accidental mutations outside reducers throw in strict mode. You can call `setAutoFreeze(false)` from `immer` for performance in rare cases, but you lose that safety. RTK doesn't re-export `setAutoFreeze`, so import it from `immer` directly.

### 346: How do you type a custom base query?

Use `BaseQueryFn<Args, Result, Error, DefinitionExtraOptions, Meta>`.

```ts
import type { BaseQueryFn } from "@reduxjs/toolkit/query";

type Args = { url: string; method?: string; body?: unknown };
type ApiError = { status: number; message: string };
type Meta = { requestId: string };

const customBaseQuery: BaseQueryFn<
  Args,
  unknown,
  ApiError,
  { retries?: number },
  Meta
> = async (args, api, extraOptions) => {
  // ...
  return { data: {}, meta: { requestId: "..." } };
};
```

The `Error` type becomes the `error` type in hooks, `extraOptions` type is checked on each endpoint, and `Meta` is passed to `transformResponse` and lifecycle callbacks.

### 347: How do you safely narrow errors from RTK Query and thunks?

Write type guards and use them everywhere you show errors.

```ts
import type { FetchBaseQueryError } from "@reduxjs/toolkit/query";

export function isFetchBaseQueryError(
  error: unknown,
): error is FetchBaseQueryError {
  return typeof error === "object" && error != null && "status" in error;
}

export function isErrorWithMessage(
  error: unknown,
): error is { message: string } {
  return (
    typeof error === "object" &&
    error != null &&
    "message" in error &&
    typeof (error as { message: unknown }).message === "string"
  );
}

try {
  await addPost(body).unwrap();
} catch (err) {
  if (isFetchBaseQueryError(err)) {
    const msg = "error" in err ? err.error : JSON.stringify(err.data);
    showError(msg);
  } else if (isErrorWithMessage(err)) {
    showError(err.message);
  }
}
```

### 348: How do you type a wrapper around an RTK Query hook?

Use the exported helper types, like `TypedUseQueryHookResult`, `TypedUseQueryStateResult` and `TypedUseMutationResult`.

```ts
import type { TypedUseQueryHookResult } from "@reduxjs/toolkit/query/react";

type PostsResult = TypedUseQueryHookResult<Post[], void, typeof baseQuery>;

export function usePublishedPosts(): PostsResult & { published: Post[] } {
  const result = useGetPostsQuery();
  const published = useMemo(
    () => result.data?.filter((p) => p.published) ?? [],
    [result.data],
  );
  return { ...result, published };
}
```

### 349: How do you type a middleware that changes what `dispatch` accepts or returns?

The first generic of `Middleware` describes the dispatch extension. `configureStore` adds it to the store's `dispatch` type when the middleware is in a `Tuple`.

```ts
type PromiseDispatch = (
  action: Promise<UnknownAction>,
) => Promise<UnknownAction>;

const promiseMiddleware: Middleware<PromiseDispatch, RootState> =
  (api) => (next) => (action) => {
    if (action instanceof Promise) {
      return action.then((resolved) => api.dispatch(resolved));
    }
    return next(action);
  };

const store = configureStore({
  reducer: rootReducer,
  middleware: (gDM) => gDM().concat(promiseMiddleware),
});

store.dispatch(Promise.resolve(increment())); // typed
```

Avoid importing `RootState` in a way that makes the types circular. If that happens, type the state in the middleware with only the fields it needs.

### 350: How do you give listeners access to services, and type them?

Pass an `extra` object to `createListenerMiddleware` and add it to `withTypes`.

```ts
interface ListenerExtra {
  analytics: AnalyticsClient;
  storage: StorageService;
}

export const listenerMiddleware = createListenerMiddleware({
  extra: { analytics, storage } satisfies ListenerExtra,
});

export const startAppListening = listenerMiddleware.startListening.withTypes<
  RootState,
  AppDispatch,
  ListenerExtra
>();

startAppListening({
  actionCreator: orderPlaced,
  effect: (action, { extra }) => {
    extra.analytics.track("order_placed", action.payload);
  },
});
```

In tests you create the middleware with fake services.

### 351: How do you update every cached list entry of an endpoint after a change?

A list endpoint can be cached under many arguments (pages, filters). Find all of them and update each one.

```ts
async onQueryStarted({ id, ...patch }, { dispatch, getState, queryFulfilled }) {
  const patchResults = api.util
    .selectCachedArgsForQuery(getState(), 'getPosts')
    .map((args) =>
      dispatch(
        api.util.updateQueryData('getPosts', args, (draft) => {
          const post = draft.items.find((p) => p.id === id)
          if (post) Object.assign(post, patch)
        }),
      ),
    )

  try {
    await queryFulfilled
  } catch {
    patchResults.forEach((r) => r.undo())
  }
},
```

You can do the same with `selectInvalidatedBy` and a tag, which also works across several endpoints.

### 352: How do you give non-React code, like an axios interceptor, access to the store?

Don't import the store into the API module directly, since the store usually imports the API module and that creates a cycle. Inject it at startup instead.

```ts
// apiClient.ts
let store: AppStore | undefined;

export const injectStore = (s: AppStore) => {
  store = s;
};

apiClient.interceptors.request.use((config) => {
  const token = store?.getState().auth.token;
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// main.tsx
injectStore(store);
```

Inside thunks and listeners prefer `getState` and `dispatch` from their arguments.

### 353: How do you handle a 401 globally with RTK Query?

Either wrap the base query (see question 307), or use a middleware that watches rejected actions.

```ts
export const unauthorizedMiddleware: Middleware =
  (api) => (next) => (action) => {
    if (
      isRejectedWithValue(action) &&
      (action.payload as FetchBaseQueryError)?.status === 401
    ) {
      api.dispatch(loggedOut());
    }
    return next(action);
  };
```

The base query approach is better when you want to refresh the token and retry. The middleware approach is simpler when a 401 always means "log out".

### 354: How do you cancel the previous `createAsyncThunk` call when a new one starts?

Keep the promise and abort it.

```tsx
function Search() {
  const dispatch = useAppDispatch();
  const promiseRef = useRef<{ abort: () => void } | null>(null);

  const onChange = (q: string) => {
    promiseRef.current?.abort();
    promiseRef.current = dispatch(searchProducts(q));
  };
  // ...
}
```

Aborting only matters if the payload creator passes `signal` to `fetch`, otherwise the old request still completes in the background, but its result is dispatched as `rejected` with `meta.aborted`. In a listener, `cancelActiveListeners` gives the same "latest wins" behavior without refs.

### 355: How does React Strict Mode affect thunks and RTK Query in development?

In development, Strict Mode mounts, unmounts and mounts components again, so effects run twice.

- RTK Query handles this: the second mount reuses the same cache entry and the in-flight request, so you see one request.
- A thunk dispatched in `useEffect` runs twice. Use `condition` to skip it if data is loading or loaded, or abort it in the effect's cleanup.

```ts
useEffect(() => {
  const promise = dispatch(fetchTodos());
  return () => promise.abort();
}, [dispatch]);
```

### 356: How does `useSelector` work internally?

React-Redux 9 uses React's `useSyncExternalStore` (through the "with selector" variant). The `Provider` creates a subscription to the store. Each `useSelector` call subscribes to it. After every dispatch, React calls the selector with the new state, compares the result to the last one with the equality function, and only schedules a re-render if they differ. Using `useSyncExternalStore` makes sure all components see the same state during a concurrent render.

### 357: Why doesn't the React-Redux `Provider` re-render every component on each state change?

The context value is the store (plus a subscription object), and those references don't change. State updates don't go through context. Each `useSelector` subscribes to the store itself and decides on its own whether to re-render. This is the main difference from putting a large state object in React Context, where every consumer re-renders on every change.

### 358: How do you hot reload reducers?

Use `store.replaceReducer` when the reducer module changes. With Vite:

```ts
if (import.meta.hot) {
  import.meta.hot.accept("./rootReducer", (newModule) => {
    if (newModule) store.replaceReducer(newModule.rootReducer);
  });
}
```

`replaceReducer` dispatches an internal action so the new reducer can initialize any new slices. With `combineSlices` you don't need `replaceReducer` for injecting slices, only for swapping the whole reducer.

### 359: What is `buildCreateSlice` for besides async thunks?

It creates a custom `createSlice` with extra "creators" that become available in the `create` callback. Right now the official creator is `asyncThunkCreator`. The reason for this design is that `createSlice` stays small by default, and apps only include the extra code they use. Most apps create one `createAppSlice` in a shared file and use it everywhere.

### 360: How do selectors work with slices that might not be injected yet?

`slice.injectInto(rootReducer)` returns an injected slice. Its `selectors` are wrapped so that if `state[reducerPath]` is `undefined`, they get the slice's initial state instead. For selectors that read several lazy slices, wrap them with `rootReducer.selector`, which uses a proxy to fill in initial state for any lazy slice that isn't there.

```ts
const selectDashboardSummary = rootReducer.selector((state) => ({
  reports: state.reports.items.length,
  alerts: state.alerts.unread,
}));
```

Remember to memoize if the selector returns a new object.

### 361: Are selectors in `createSlice.selectors` memoized?

No. They are just wrapped to find the slice state. If a selector returns derived data like a filtered array, wrap the logic in `createSelector` yourself.

```ts
const selectTodos = (state: TodosState) => state.items;

const todosSlice = createSlice({
  name: "todos",
  initialState,
  reducers: {},
  selectors: {
    selectCompletedTodos: createSelector([selectTodos], (items) =>
      items.filter((t) => t.completed),
    ),
  },
});
```

Since the wrapped version calls your selector with the slice state each time, memoization still works as long as the slice state reference doesn't change.

### 362: How do you keep the Redux DevTools fast with large state or many actions?

- Lower `maxAge` so fewer past states are kept.
- Use `actionsDenylist` to hide noisy actions like mouse moves.
- Use `actionSanitizer` and `stateSanitizer` to replace big payloads with short placeholders.
- Turn on `trace: true` only when you need stack traces for where actions came from, since it adds overhead.

### 363: Why do Redux errors in production look like "Minified Redux error #N"?

To keep bundles small, the full error messages are replaced with short codes in production builds. The message includes a link to the Redux docs where you can read the full text for that code. RTK does the same for its own errors.

### 364: How does Redux Toolkit's packaging affect bundle size?

RTK 2.x ships modern ESM with `exports` in `package.json`, plus a CJS build. Bundlers can tree-shake unused APIs. RTK Query is in a separate entry point, so you only pay for it if you import from `@reduxjs/toolkit/query`. Immer is the biggest dependency, and it's needed by `createSlice`. `create.asyncThunk` is opt-in through `buildCreateSlice` for the same reason.

### 365: How do you use RTK Query with Angular, Vue or Svelte?

Import from `@reduxjs/toolkit/query`, add the API to a store, and use the endpoint thunks and selectors.

```ts
const sub = store.dispatch(api.endpoints.getPosts.initiate());
const selectPosts = api.endpoints.getPosts.select();

const unsubscribeStore = store.subscribe(() => {
  const { data, isLoading } = selectPosts(store.getState());
  render(data, isLoading);
});

// on teardown
sub.unsubscribe();
unsubscribeStore();
```

Community packages exist that wrap this into framework-style hooks or signals.

### 366: Should you have one `createApi` or many?

The docs recommend one API per base URL your app talks to. Tags only work within a single API, so splitting related endpoints across APIs means mutations in one can't invalidate queries in the other. Use `injectEndpoints` to split the code into files. Create a second API only for a truly separate service, like a third-party API with its own base URL and no shared data.

### 367: Can a mutation invalidate tags only when it succeeds?

`invalidatesTags` runs on both success and failure, and receives `(result, error, arg)`. Return an empty array on error if you don't want any refetching.

```ts
updatePost: build.mutation<Post, UpdatePostArgs>({
  query: ({ id, ...body }) => ({ url: `posts/${id}`, method: 'PUT', body }),
  invalidatesTags: (result, error, { id }) => (error ? [] : [{ type: 'Post', id }]),
}),
```

Sometimes you do want refetching on error, for example after a conflict error, to show the latest server data.

### 368: How does `invalidationBehavior: 'delayed'` interact with optimistic updates?

With `'delayed'`, invalidated queries refetch only after all pending queries and mutations are done. If the user fires several optimistic mutations quickly, the cache keeps the optimistic values until the last one finishes, and then one round of refetches runs. With `'immediately'`, a refetch from the first mutation could come back with old data and overwrite the optimistic changes from later mutations, causing flicker.

### 369: How do `keepUnusedDataFor` and `refetchOnMountOrArgChange` interact?

`keepUnusedDataFor` decides how long data stays after the last subscriber leaves. `refetchOnMountOrArgChange` decides if a new subscriber triggers a refetch. With the defaults, a component that mounts within 60 seconds gets cached data and no request. If you set `refetchOnMountOrArgChange: 10`, it gets the cached data right away and also a background refetch if the data is older than 10 seconds. If the entry was already removed, a request happens anyway.

### 370: How do you set up `refetchOnFocus` and `refetchOnReconnect` in React Native?

`setupListeners` uses browser events by default. Pass a custom handler that uses `AppState` and `NetInfo`.

```ts
import { AppState } from "react-native";
import NetInfo from "@react-native-community/netinfo";

setupListeners(
  store.dispatch,
  (dispatch, { onFocus, onFocusLost, onOnline, onOffline }) => {
    const appStateSub = AppState.addEventListener("change", (state) => {
      if (state === "active") dispatch(onFocus());
      else dispatch(onFocusLost());
    });
    const unsubscribeNetInfo = NetInfo.addEventListener((state) => {
      dispatch(state.isConnected ? onOnline() : onOffline());
    });
    return () => {
      appStateSub.remove();
      unsubscribeNetInfo();
    };
  },
);
```

### 371: Can you cancel an in-flight RTK Query request?

Yes, through the promise from `initiate` or a lazy trigger: `promise.abort()`. The `useQuery` hooks don't abort when a component unmounts. The request is left to finish so the result can be cached for the next user of that data. If you need cancellation, use the lazy hook and abort in an effect cleanup.

```tsx
const [trigger] = useLazySearchQuery();

useEffect(() => {
  const request = trigger(term);
  return () => request.abort();
}, [term, trigger]);
```

### 372: How do you support cancellation in a `queryFn`?

The second argument has a `signal`. Pass it to anything that supports `AbortSignal`.

```ts
search: build.query<Result[], string>({
  async queryFn(term, { signal }) {
    try {
      const res = await fetch(`/api/search?q=${term}`, { signal })
      return { data: await res.json() }
    } catch (error) {
      return { error: { status: 'FETCH_ERROR', error: String(error) } as FetchBaseQueryError }
    }
  },
}),
```

### 373: How would you design authentication with RTK and RTK Query?

1. An `authSlice` holds the token (or just a "logged in" flag if you use httpOnly cookies) and the current user.
2. `login` and `logout` are RTK Query mutations. The slice listens to `login.matchFulfilled` to store the token.
3. `prepareHeaders` adds the token to every request.
4. A wrapped base query handles 401 by refreshing the token or logging out.
5. On logout, reset the slices and call `api.util.resetApiState()`.
6. Queries that return user-specific data provide tags that the login mutation invalidates, so data refreshes for the new user.

Avoid storing long-lived secrets in `localStorage` when you can use httpOnly cookies.

### 374: How do you fully reset the app state on logout, including RTK Query?

Combine a root reducer reset with the API reset.

```ts
export const logout = createAppAsyncThunk(
  "auth/logout",
  async (_, { dispatch }) => {
    await dispatch(api.endpoints.logout.initiate())
      .unwrap()
      .catch(() => {});
    dispatch(loggedOut());
    dispatch(api.util.resetApiState());
  },
);
```

With the root reducer resetting all slices on `loggedOut` (question 261), and `resetApiState` clearing the cache. Also cancel long-running listeners and close sockets that were started for the user, for example by having them `take(loggedOut.match)`.

### 375: How do you render a large list from Redux efficiently?

- Store items normalized with an entity adapter.
- The list selects `selectIds`, which only changes when items are added, removed or reordered.
- Each row is wrapped in `React.memo` and selects its own entity with `selectById`.
- Use list virtualization (for example `react-window` or `@tanstack/react-virtual`) so only visible rows mount.

```tsx
function TodoList() {
  const ids = useAppSelector(selectTodoIds);
  return ids.map((id) => <TodoRow key={id} id={id} />);
}

const TodoRow = memo(function TodoRow({ id }: { id: string }) {
  const todo = useAppSelector((state) => selectTodoById(state, id));
  return <li>{todo.text}</li>;
});
```

Updating one todo then re-renders one row.

### 376: What does a `sortComparer` cost in an entity adapter?

Every add, set, upsert or update that touches sort fields has to place the changed items in the right spot in `ids`. With thousands of items and frequent updates this adds up. If you only need sorting for display, you can skip `sortComparer` and sort in a memoized selector, which only runs when the data actually changes and only for components that need the sorted view.

### 377: How do you memoize a selector with arguments when many components use different arguments?

Two options:

1. Rely on Reselect 5's `weakMapMemoize`, which caches per argument, so one shared selector works for many IDs.
2. Create a selector per component with `useMemo`, so each instance has its own cache.

```tsx
const makeSelectCommentsForPost = () =>
  createSelector(
    [selectAllComments, (_state: RootState, postId: string) => postId],
    (comments, postId) => comments.filter((c) => c.postId === postId),
  );

function Comments({ postId }: { postId: string }) {
  const selectCommentsForPost = useMemo(makeSelectCommentsForPost, []);
  const comments = useAppSelector((state) =>
    selectCommentsForPost(state, postId),
  );
}
```

The factory version is better when the cache would otherwise grow without bound, since it goes away with the component.

### 378: How would you implement undo/redo with Redux Toolkit?

Wrap a slice reducer in a higher-order reducer that keeps past and future states.

```ts
interface History<T> {
  past: T[];
  present: T;
  future: T[];
}

export const undo = createAction("history/undo");
export const redo = createAction("history/redo");

export function undoable<T>(
  reducer: Reducer<T>,
  limit = 50,
): Reducer<History<T>> {
  const initial: History<T> = {
    past: [],
    present: reducer(undefined, { type: "@@INIT" }),
    future: [],
  };

  return (state = initial, action) => {
    const { past, present, future } = state;

    if (undo.match(action)) {
      if (past.length === 0) return state;
      return {
        past: past.slice(0, -1),
        present: past[past.length - 1],
        future: [present, ...future],
      };
    }
    if (redo.match(action)) {
      if (future.length === 0) return state;
      return {
        past: [...past, present],
        present: future[0],
        future: future.slice(1),
      };
    }

    const newPresent = reducer(present, action);
    if (newPresent === present) return state;
    return {
      past: [...past, present].slice(-limit),
      present: newPresent,
      future: [],
    };
  };
}
```

Because states are immutable, keeping old ones is cheap thanks to structural sharing. Libraries like `redux-undo` do the same with more options. Immer patches are another approach for large documents.

### 379: How do you write a custom store enhancer?

An enhancer wraps `createStore` and returns a store with changed behavior.

```ts
import type { StoreEnhancer } from "@reduxjs/toolkit";

export const timingEnhancer: StoreEnhancer =
  (createStore) => (reducer, preloadedState) => {
    const store = createStore(reducer, preloadedState);

    const dispatch: typeof store.dispatch = (action) => {
      const start = performance.now();
      const result = store.dispatch(action);
      const time = performance.now() - start;
      if (time > 16) console.warn("Slow dispatch", action, time);
      return result;
    };

    return { ...store, dispatch };
  };

configureStore({
  reducer: rootReducer,
  enhancers: (getDefaultEnhancers) =>
    getDefaultEnhancers().concat(timingEnhancer),
});
```

Most things can be done with middleware instead, which is simpler. Enhancers are for changing `getState`, `subscribe` or the store itself.

### 380: Does middleware order matter in RTK, and what's a good order?

Yes. Each middleware sees the action before the ones after it, and can stop or change it.

- Listener middleware: `prepend`, so effects see actions before anything else, and actions it dispatches go through the full chain.
- Dynamic middleware: usually `prepend` too.
- Default middleware: thunk, then dev checks.
- RTK Query middleware: `concat` after defaults.
- Logging or error reporting middleware: often last, so it sees the final action that reaches the reducer.

```ts
middleware: (gDM) =>
  gDM()
    .prepend(listenerMiddleware.middleware)
    .concat(api.middleware, errorLoggerMiddleware),
```

### 381: How do you update several RTK Query cache entries from one websocket message?

Run the socket in a listener (or a long-lived `onCacheEntryAdded`) and dispatch `updateQueryData` for every affected entry.

```ts
startAppListening({
  actionCreator: socketMessageReceived,
  effect: (action, { dispatch, getState }) => {
    const msg = action.payload;
    if (msg.kind !== "post-updated") return;

    const affected = api.util.selectInvalidatedBy(getState(), [
      { type: "Post", id: msg.post.id },
    ]);
    for (const { endpointName, originalArgs } of affected) {
      if (endpointName === "getPost") {
        dispatch(
          api.util.updateQueryData("getPost", originalArgs, () => msg.post),
        );
      }
      if (endpointName === "getPosts") {
        dispatch(
          api.util.updateQueryData("getPosts", originalArgs, (draft) => {
            const i = draft.findIndex((p) => p.id === msg.post.id);
            if (i !== -1) draft[i] = msg.post;
          }),
        );
      }
    }
  },
});
```

If the message only says "something changed", invalidating the tag is simpler.

### 382: How do you do an optimistic create when the server assigns the ID?

Insert an item with a temporary ID, then replace it with the real one when the response comes back.

```ts
addTodo: build.mutation<Todo, { text: string }>({
  query: (body) => ({ url: 'todos', method: 'POST', body }),
  async onQueryStarted({ text }, { dispatch, queryFulfilled, requestId }) {
    const tempId = `temp-${requestId}`
    const patch = dispatch(
      api.util.updateQueryData('getTodos', undefined, (draft) => {
        draft.push({ id: tempId, text, completed: false })
      }),
    )
    try {
      const { data } = await queryFulfilled
      dispatch(
        api.util.updateQueryData('getTodos', undefined, (draft) => {
          const index = draft.findIndex((t) => t.id === tempId)
          if (index !== -1) draft[index] = data
        }),
      )
    } catch {
      patch.undo()
    }
  },
}),
```

Disable actions on items with a temporary ID, since the server doesn't know that ID yet.

### 383: How do you replace a temporary ID in an entity adapter?

`updateOne` with a new `id` in `changes` moves the entity to the new key.

```ts
builder.addCase(saveTodo.fulfilled, (state, action) => {
  todosAdapter.updateOne(state, {
    id: action.meta.arg.tempId,
    changes: { id: action.payload.id, savedAt: action.payload.savedAt },
  });
});
```

Any other state that stores the temp ID (like a "selected item") needs to be updated too.

### 384: How do you update the cache of an infinite query?

The draft has the shape `{ pages, pageParams }`, so find the item inside the pages.

```ts
dispatch(
  api.util.updateQueryData("getFeed", undefined, (draft) => {
    for (const page of draft.pages) {
      const post = page.items.find((p) => p.id === id);
      if (post) {
        post.liked = true;
        break;
      }
    }
  }),
);
```

Don't change `pageParams` unless you also change which pages are loaded.

### 385: When should server data live in a slice instead of RTK Query?

RTK Query is the default for server data. A slice still makes sense when:

- The data is edited heavily on the client before saving, like a document editor or a multi-step wizard.
- You need to combine and normalize data from many endpoints in ways the document cache doesn't handle well.
- The data comes from a source that doesn't fit request/response, and you'd be writing your own cache logic anyway.

Even then you can use RTK Query to fetch, and copy the result into a slice with `extraReducers` and `matchFulfilled`. Avoid keeping the same data in both places without a clear owner.

### 386: How do you combine UI state in slices with RTK Query?

Keep UI state (filters, sorting, selected IDs, current page) in a slice, and use it to build the query arguments.

```tsx
function ProductsPage() {
  const filters = useAppSelector(selectProductFilters);
  const { data, isFetching } = useGetProductsQuery(filters);
  // ...
}
```

The slice is the source of truth for "what the user wants to see", and RTK Query caches each combination. Changing a filter back to a previous value shows cached data instantly.

### 387: How can several micro-frontends share Redux?

Options, from loosest to tightest:

- Each micro-frontend has its own store. Communicate with custom events or a small shared event bus. This is the safest.
- A host app owns one store and exposes it. Remotes inject their slices with `combineSlices` and their middleware with `createDynamicMiddleware`, and their endpoints with `injectEndpoints`. All parts must share the same `@reduxjs/toolkit` and `react-redux` instances (for example as Module Federation singletons), or context and `instanceof` checks break.

Sharing a store couples the teams' release cycles, so only do it when the features really share state.

### 388: What security issues should you keep in mind with Redux?

- Everything in the store is readable by any script on the page and by the DevTools. Don't store secrets that aren't needed on the client.
- Turn DevTools off in production, or at least sanitize sensitive state and actions.
- Be careful with `preloadedState` from the server: escape it when embedding it in HTML (for example replace `<` with `<`) to prevent XSS.
- Persisted state in `localStorage` is readable by XSS. Prefer httpOnly cookies for tokens.
- Clear the store and RTK Query cache on logout so the next user on the same device doesn't see old data.

### 389: Why can you lose error information in `createAsyncThunk` and how do you avoid it?

When the payload creator throws, RTK runs the error through `miniSerializeError`, which keeps only `name`, `message`, `stack` and `code`. Fields like an axios `response.data` or a custom `details` array are dropped, because the error object must be serializable for the action. To keep them, catch the error and use `rejectWithValue` with the data you need.

```ts
async (arg, { rejectWithValue }) => {
  try {
    return (await client.post("/orders", arg)).data;
  } catch (err) {
    const error = err as AxiosError<{ fieldErrors: Record<string, string> }>;
    return rejectWithValue(error.response?.data ?? { fieldErrors: {} });
  }
};
```

### 390: What does a thunk return when `condition` cancels it?

The returned promise resolves with a `rejected` action whose `meta.condition` is `true` and `error.name` is `'ConditionError'`. If `dispatchConditionRejection` is `false` (the default), that action is not dispatched to the store, but you still get it from the promise. Calling `.unwrap()` on it throws, so code that awaits `unwrap()` must expect this case.

### 391: How do you add a timeout to `createAsyncThunk`?

Combine the thunk `signal` with a timeout signal.

```ts
export const fetchReport = createAppAsyncThunk(
  "reports/fetch",
  async (id: string, { signal }) => {
    const res = await fetch(`/api/reports/${id}`, {
      signal: AbortSignal.any([signal, AbortSignal.timeout(10_000)]),
    });
    if (!res.ok) throw new Error(`Request failed: ${res.status}`);
    return (await res.json()) as Report;
  },
);
```

`AbortSignal.any` and `AbortSignal.timeout` are available in modern browsers and Node 20+.

### 392: How do you set a timeout for one RTK Query endpoint?

`fetchBaseQuery` accepts `timeout` globally and per request.

```ts
const baseQuery = fetchBaseQuery({ baseUrl: '/api', timeout: 10_000 })

generateReport: build.mutation<Report, ReportParams>({
  query: (body) => ({ url: 'reports', method: 'POST', body, timeout: 60_000 }),
}),
```

When it times out, the error is `{ status: 'TIMEOUT_ERROR', error: '...' }`.

### 393: How do you use `fetchBaseQuery` during SSR?

- Use an absolute `baseUrl`, since relative URLs don't work in Node.
- Forward the user's cookies or auth header from the incoming request.

```ts
export const makeStore = (req?: IncomingMessage) =>
  configureStore({
    reducer: rootReducer,
    middleware: (gDM) =>
      gDM({ thunk: { extraArgument: { cookie: req?.headers.cookie } } }).concat(
        api.middleware,
      ),
  });

const baseQuery = fetchBaseQuery({
  baseUrl: process.env.API_URL,
  prepareHeaders: (headers, { extra }) => {
    const cookie = (extra as { cookie?: string })?.cookie;
    if (cookie) headers.set("cookie", cookie);
    return headers;
  },
});
```

The `extra` value in `prepareHeaders` is the thunk extra argument, so each request-scoped store can carry its own headers.

### 394: What are `getRunningQueryThunk` and `getRunningMutationsThunk`?

- `api.util.getRunningQueryThunk(endpointName, arg)` returns the promise of a running query for that cache key, or `undefined`.
- `api.util.getRunningQueriesThunk()` returns all running query promises.
- `api.util.getRunningMutationThunk(endpointName, requestIdOrCacheKey)` and `getRunningMutationsThunk()` do the same for mutations.

They are mostly used in SSR (wait for everything before rendering) and in tests (wait for requests to settle).

```ts
await Promise.all(store.dispatch(api.util.getRunningMutationsThunk()));
```

### 395: How do you keep tests isolated when using RTK Query?

- Create a new store for each test, so the cache starts empty.
- If a store is reused, dispatch `api.util.resetApiState()` in `afterEach`.
- Reset MSW handlers after each test.
- Be careful with fake timers. RTK Query uses timers for `keepUnusedDataFor` and polling, and some testing libraries' async helpers wait on timers. Use real timers by default, and with fake timers advance them explicitly.

### 396: How do you test the listener middleware?

Create a fresh middleware and store per test, add the listener, dispatch actions and check the results.

```ts
test("saves settings when the theme changes", async () => {
  const storage = { set: vi.fn() };
  const listenerMiddleware = createListenerMiddleware({ extra: { storage } });
  addSettingsListeners(
    listenerMiddleware.startListening.withTypes<
      RootState,
      AppDispatch,
      Extra
    >(),
  );

  const store = configureStore({
    reducer: rootReducer,
    middleware: (gDM) => gDM().prepend(listenerMiddleware.middleware),
  });

  store.dispatch(themeChanged("dark"));
  await vi.waitFor(() =>
    expect(storage.set).toHaveBeenCalledWith("theme", "dark"),
  );
});
```

Export a function that registers listeners (like `addSettingsListeners`) so tests can attach them to a new middleware.

### 397: How do you test an RTK Query hook directly?

Use `renderHook` with a Provider wrapper and MSW.

```tsx
test("useGetPostsQuery returns posts", async () => {
  const store = setupStore();
  const wrapper = ({ children }: { children: React.ReactNode }) => (
    <Provider store={store}>{children}</Provider>
  );

  const { result } = renderHook(() => useGetPostsQuery(), { wrapper });

  expect(result.current.isLoading).toBe(true);
  await waitFor(() => expect(result.current.isSuccess).toBe(true));
  expect(result.current.data).toHaveLength(2);
});
```

Most of the time testing the component that uses the hook gives more value.

### 398: What are common problems when testing RTK Query with MSW in Node?

- Relative `baseUrl` like `/api` fails because there is no `window.location`. Use an absolute URL in tests, or set a base URL in your test environment.
- If your test environment replaces `fetch`, `Request` or `AbortController` with versions that don't match each other, requests can fail with odd errors. Use Node's built-in versions (Node 18+) where possible.
- Unhandled requests silently hang or fail. Configure `server.listen({ onUnhandledRequest: 'error' })`.
- Data from one test leaking into another, because the store or cache was reused.

### 399: How do you type `preloadedState` when using lazy-loaded slices?

`RootState` from `combineSlices(...).withLazyLoadedSlices<...>()` marks lazy slices as optional, so `preloadedState` can include or leave them out.

```ts
export const rootReducer = combineSlices(
  authSlice,
  api,
).withLazyLoadedSlices<LazyLoadedSlices>();
export type RootState = ReturnType<typeof rootReducer>;

export const makeStore = (preloadedState?: Partial<RootState>) =>
  configureStore({ reducer: rootReducer, preloadedState });
```

When you preload a lazy slice's state before injecting it, the slice reducer gets that state on injection instead of the initial state.

### 400: Can you nest `combineSlices`?

Yes. A combined reducer can be passed into another `combineSlices` as part of a reducer map, or a slice can be injected at a nested path using `reducerPath` with a parent combined reducer that you inject into. In practice, flat state is easier to work with and is what slice selectors assume, so nest only when there's a clear reason, like grouping all admin slices under `state.admin`.

### 401: Does RTK Query support React Suspense?

Not directly. RTK Query hooks return loading flags instead of throwing promises. You can build a small wrapper that throws the `initiate` promise while loading, but you have to handle subscriptions carefully so the cache entry isn't removed while suspended. Most RTK Query apps use the status flags and skeleton components. Check the current docs before relying on a Suspense pattern, since this area changes.

### 402: Can you use Redux in React Server Components?

No. Server Components render once on the server and can't use hooks or subscribe to a store. The store must live in client components. Fetch data in Server Components with `fetch` or your data layer directly, and pass it to client components as props. If client components need it in Redux, dispatch it once when the client store is created (see question 258). Don't use a global store module on the server, because it would be shared across requests.

### 403: How do you implement polling with backoff using a listener?

```ts
startAppListening({
  actionCreator: jobStarted,
  effect: async (action, listenerApi) => {
    listenerApi.cancelActiveListeners();
    let delayMs = 1000;

    while (true) {
      await listenerApi.delay(delayMs);
      const result = await listenerApi.dispatch(
        api.endpoints.getJob.initiate(action.payload.jobId, {
          subscribe: false,
          forceRefetch: true,
        }),
      );
      if (result.data?.status === "done" || result.data?.status === "failed") {
        listenerApi.dispatch(jobFinished(result.data));
        return;
      }
      delayMs = Math.min(delayMs * 2, 30_000);
    }
  },
});
```

Dispatching `jobStarted` again cancels the old loop. `delay` throws when cancelled, which ends the loop.

### 404: How do you manage a websocket connection that depends on login state?

Start the socket in a listener on login and stop it on logout.

```ts
startAppListening({
  actionCreator: loggedIn,
  effect: async (action, listenerApi) => {
    listenerApi.cancelActiveListeners();
    const socket = new WebSocket(
      `wss://example.com?token=${action.payload.token}`,
    );

    socket.onmessage = (event) => {
      listenerApi.dispatch(socketMessageReceived(JSON.parse(event.data)));
    };

    try {
      await listenerApi.take(loggedOut.match);
    } finally {
      socket.close();
    }
  },
});
```

The `finally` also runs if the effect is cancelled, so the socket is always closed.

### 405: How do you sync state between browser tabs?

Use `BroadcastChannel` in a listener. Send actions out, and dispatch actions that come in, marking them so they aren't sent back.

```ts
const channel = new BroadcastChannel("app-sync");
const syncedActions = isAnyOf(loggedOut, themeChanged, cartUpdated);

startAppListening({
  matcher: syncedActions,
  effect: (action) => {
    if (!(action as { meta?: { fromOtherTab?: boolean } }).meta?.fromOtherTab) {
      channel.postMessage(action);
    }
  },
});

channel.onmessage = (event) => {
  store.dispatch({
    ...event.data,
    meta: { ...event.data.meta, fromOtherTab: true },
  });
};
```

Only sync serializable, event-style actions, not RTK Query internals.

### 406: How would you build an offline queue for mutations?

1. Keep a `pendingMutations` slice storing serializable descriptions (`{ id, endpointName, arg }`).
2. When offline (`state.api.config.online` is false or `navigator.onLine` is false), add to the queue instead of calling the mutation, and apply an optimistic update.
3. Persist the queue slice.
4. A listener waits for the `onOnline` action from `setupListeners` and replays the queue in order with `api.endpoints[endpointName].initiate(arg)`, removing each item on success.
5. On a conflict error, stop and let the user resolve it.

RTK doesn't have built-in offline support, so this is custom code. Keep it small and test reordering and failure cases carefully.

### 407: How do you handle large binary data like images or files with Redux?

Don't put them in the store. Keep them in a separate cache (an in-memory `Map`, IndexedDB, or object URLs) and store only a serializable reference, like an ID or URL, in Redux.

```ts
const fileCache = new Map<string, File>();

export const fileSelected =
  (file: File): AppThunk =>
  (dispatch) => {
    const id = nanoid();
    fileCache.set(id, file);
    dispatch(uploadQueued({ id, name: file.name, size: file.size }));
  };
```

This keeps the DevTools, serializability checks and persistence working.

### 408: How do you build denormalized view data from normalized state efficiently?

Use `createSelector` with the entity maps as inputs.

```ts
export const selectPostsWithAuthors = createAppSelector(
  [selectAllPosts, selectUserEntities],
  (posts, users) =>
    posts.map((post) => ({
      ...post,
      author: users[post.authorId],
    })),
);
```

The result only recomputes when posts or users change. If one user's name changes, the whole list is rebuilt, so for very large lists it's better to denormalize per row (each row selects its post and author).

### 409: What is `createStructuredSelector`?

A Reselect helper that builds one memoized selector from an object of selectors. The result object keeps the same reference until one of the values changes.

```ts
import { createStructuredSelector } from "reselect";

const selectHeaderData = createStructuredSelector(
  {
    user: selectCurrentUser,
    unreadCount: selectUnreadCount,
    theme: selectTheme,
  },
  createAppSelector,
);

const { user, unreadCount, theme } = useAppSelector(selectHeaderData);
```

RTK doesn't re-export it, so import it from `reselect`.

### 410: How do you check whether a memoized selector is working?

Reselect selectors have debugging helpers:

```ts
selectVisibleTodos(state);
selectVisibleTodos(state);
console.log(selectVisibleTodos.recomputations()); // 1 if memoized correctly
console.log(selectVisibleTodos.dependencyRecomputations());
selectVisibleTodos.resetRecomputations();
```

The dev mode checks also warn if input selectors return new references. React DevTools Profiler can show which components re-render after an action.

### 411: What is the difference between `memoize` and `argsMemoize` in Reselect 5?

A selector has two levels of caching:

- `argsMemoize` caches based on the arguments passed to the selector (the state and extra args). If the arguments are the same, the input selectors don't even run.
- `memoize` caches the result function based on the values returned by the input selectors.

Both default to `weakMapMemoize`. You can set each one separately in the options.

### 412: What is the difference between `refetch` and `invalidateTags`?

- `refetch()` from a hook refetches that one cache entry, right away, no matter what tags it provides.
- `invalidateTags` refetches every subscribed entry that provides those tags, following `invalidationBehavior`. Unsubscribed entries are marked so they refetch on next use.

Use `refetch` for a "reload this" button, and tags for "data changed on the server".

### 413: What happens when several components subscribe to the same query with different options?

RTK Query merges subscription options per cache entry:

- `pollingInterval`: the lowest non-zero interval among subscribers is used.
- `refetchOnFocus` and `refetchOnReconnect`: the entry refetches if any subscriber asked for it.
- `skipPollingIfUnfocused`: each subscriber's setting is considered when picking the interval.

`refetchOnMountOrArgChange` is checked per subscriber when it mounts.

### 414: When should you use `upsertQueryEntries` instead of `upsertQueryData`?

`upsertQueryData` runs the full query thunk lifecycle (pending, fulfilled, lifecycle callbacks), one entry at a time, and is async. `upsertQueryEntries` is a single synchronous action that writes many entries at once, without starting requests or running `onQueryStarted`. Use `upsertQueryEntries` when seeding many detail entries from a list response, because it's much cheaper and causes one state update.

### 415: How do you write `providesTags` that work even when the result is empty or failed?

Use the argument to build tags, since it's always available.

```ts
getPostComments: build.query<Comment[], number>({
  query: (postId) => `posts/${postId}/comments`,
  providesTags: (result, error, postId) => [
    { type: 'Comments', id: postId },
    ...(result ?? []).map((c) => ({ type: 'Comment' as const, id: c.id })),
  ],
}),

addComment: build.mutation<Comment, { postId: number; text: string }>({
  query: ({ postId, text }) => ({ url: `posts/${postId}/comments`, method: 'POST', body: { text } }),
  invalidatesTags: (result, error, { postId }) => [{ type: 'Comments', id: postId }],
}),
```

An empty comments list still provides `Comments:postId`, so adding the first comment refetches it.

### 416: What happens to a mutation if the component unmounts before it finishes?

The request keeps running and the result is written to the store. Tags are invalidated as usual, and `onQueryStarted` still runs. The component just won't see the result in its hook. If the mutation result is only stored for this component, it's removed after the request finishes. If you need the result elsewhere, use `fixedCacheKey` or handle it in `onQueryStarted` or a listener.

### 417: Is `keepUnusedDataFor: Infinity` a good idea?

It keeps data forever after the last subscriber leaves. It can be fine for small, static reference data like a list of countries. For data keyed by many different arguments (search results, paginated lists), the cache only grows and memory use climbs over a long session. Prefer a large finite value, or keep reference data in a slice.

### 418: How do you use RTK Query with React Router data loaders?

Start the request in the loader and let the component read it from the cache.

```ts
export const postLoader =
  (store: AppStore) =>
  async ({ params }: LoaderFunctionArgs) => {
    const promise = store.dispatch(api.endpoints.getPost.initiate(Number(params.id)))
    try {
      await promise.unwrap()
    } catch {
      throw new Response('Not found', { status: 404 })
    } finally {
      promise.unsubscribe()
    }
    return null
  }

// route
{ path: 'posts/:id', loader: postLoader(store), element: <PostPage /> }
```

The component calls `useGetPostQuery(id)` and gets the data immediately. Unsubscribing in the loader is safe because the component subscribes within `keepUnusedDataFor`.

### 419: How would you organize error handling in a large RTK app?

Use layers:

1. Base query: normalize errors into one shape, handle 401 and retries.
2. Endpoint: `transformErrorResponse` for endpoint-specific shapes.
3. Global middleware or listener: log errors, show toasts for unexpected failures, using `isRejectedWithValue` and `isRejected`.
4. Component: show inline messages and field errors for expected failures, using `.unwrap()` and the hook `error`.
5. Listener `onError` and React error boundaries for bugs in your own code.

Decide which errors are "expected" (validation, not found) and handled locally, and which are "unexpected" and handled globally, so users don't see two messages for one problem.

### 420: How do you show server validation errors from a mutation in a form?

Normalize the error into field errors and set them on the form.

```tsx
const [register] = useRegisterMutation();

const onSubmit = async (values: FormValues) => {
  try {
    await register(values).unwrap();
  } catch (err) {
    if (isFetchBaseQueryError(err) && err.status === 422) {
      const { fieldErrors } = err.data as {
        fieldErrors: Record<string, string>;
      };
      Object.entries(fieldErrors).forEach(([field, message]) =>
        setError(field as keyof FormValues, { message }),
      );
    } else {
      setError("root", { message: "Something went wrong" });
    }
  }
};
```

Form state itself stays in the form library, not in Redux.

### 421: What naming conventions work well for actions?

- Type format: `domain/eventName`, like `cart/itemAdded` or `auth/sessionExpired`. `createSlice` does this for you.
- Name reducers in past tense for events (`itemAdded`, `orderPlaced`) instead of setters (`setItems`).
- Async thunks: `domain/verbNoun`, like `posts/fetchPosts`, since RTK appends `/pending` and so on.
- Keep names unique across the app so the DevTools log is easy to read.

### 422: How can you use action replays in tests?

Reducers are pure, so you can build a state from a list of actions with `reduce` and assert on the result.

```ts
const actions = [
  todoAdded("a"),
  todoAdded("b"),
  todoToggled("a"),
  completedCleared(),
];
const finalState = actions.reduce(
  todosReducer,
  todosReducer(undefined, { type: "init" }),
);
expect(selectTodoTexts({ todos: finalState } as RootState)).toEqual(["b"]);
```

You can also export an action log from the DevTools to reproduce a bug as a test.

### 423: When is Redux Toolkit not a good fit?

- Small apps with little shared state, where React state and Context are enough.
- Apps where almost all state is server data and you don't need Redux for anything else. TanStack Query alone may be simpler.
- Very high-frequency local updates (like drag positions at 60fps) that don't need to be global. Keep them in local state or refs.

RTK removes most of the old boilerplate, but it still adds concepts (actions, reducers, middleware) that need to pay for themselves.

### 424: How does `createSlice` generate actions internally?

In simple terms, for each key in `reducers` it:

1. Builds the type string: `${name}/${key}`.
2. Creates an action creator with `createAction(type, prepare)`, which has `.type` and `.match`.
3. Adds the case reducer to a map from type to reducer.

Then it calls `createReducer(initialState, builder => { ...addCase for each type...; extraReducers(builder) })`. The final reducer looks up the action type in the map, runs the case reducer through Immer's `produce`, then runs matching `addMatcher` reducers.

### 425: How does `createAsyncThunk` work internally?

A simplified version:

```ts
function createAsyncThunkSimplified(typePrefix, payloadCreator) {
  const pending = createAction(`${typePrefix}/pending`, (requestId, arg) => ({
    payload: undefined,
    meta: { requestId, arg, requestStatus: "pending" },
  }));
  const fulfilled = createAction(
    `${typePrefix}/fulfilled`,
    (payload, requestId, arg) => ({
      payload,
      meta: { requestId, arg, requestStatus: "fulfilled" },
    }),
  );
  const rejected = createAction(
    `${typePrefix}/rejected`,
    (error, requestId, arg, payload) => ({
      payload,
      error: miniSerializeError(error),
      meta: { requestId, arg, requestStatus: "rejected" },
    }),
  );

  return (arg) => (dispatch, getState, extra) => {
    const requestId = nanoid();
    const controller = new AbortController();
    const promise = (async () => {
      dispatch(pending(requestId, arg));
      try {
        const result = await payloadCreator(arg, {
          dispatch,
          getState,
          extra,
          requestId,
          signal: controller.signal,
        });
        return dispatch(fulfilled(result, requestId, arg));
      } catch (err) {
        return dispatch(rejected(err, requestId, arg));
      }
    })();
    return Object.assign(promise, {
      abort: () => controller.abort(),
      requestId,
      arg,
      unwrap: () => promise.then(unwrapResult),
    });
  };
}
```

The real version also handles `condition`, `rejectWithValue`, abort racing and the options.

### 426: How does Immer's `produce` work?

1. It wraps the base state in a Proxy (the draft).
2. Reads return values from the base state, wrapping nested objects in Proxies as they're accessed.
3. On the first write to an object, Immer makes a shallow copy of it and its parents, and writes to the copy.
4. When the recipe ends, Immer builds the final state: changed objects use the copies, unchanged objects keep their original references.
5. The result is frozen.

So only the changed path gets new references, which is exactly what `useSelector` and memoized selectors rely on.

### 427: How does the middleware chain get built?

`applyMiddleware` gives each middleware a `{ getState, dispatch }` API, then composes them from right to left.

```ts
function applyMiddleware(...middlewares) {
  return (createStore) => (reducer, preloadedState) => {
    const store = createStore(reducer, preloadedState);
    let dispatch = () => {
      throw new Error(
        "Dispatching while constructing your middleware is not allowed.",
      );
    };
    const middlewareAPI = {
      getState: store.getState,
      dispatch: (...args) => dispatch(...args),
    };
    const chain = middlewares.map((middleware) => middleware(middlewareAPI));
    dispatch = compose(...chain)(store.dispatch);
    return { ...store, dispatch };
  };
}
```

Each `next` is the next middleware's handler, and the last `next` is the real `store.dispatch`. `middlewareAPI.dispatch` points to the full chain, which is why dispatching from a middleware starts again from the top.

### 428: How is the thunk middleware implemented?

It is a few lines:

```ts
function createThunkMiddleware(extraArgument) {
  return ({ dispatch, getState }) =>
    (next) =>
    (action) => {
      if (typeof action === "function") {
        return action(dispatch, getState, extraArgument);
      }
      return next(action);
    };
}
```

If the dispatched value is a function, it calls it instead of passing it on. That's also why dispatching an action creator by mistake calls it as a thunk, which the action creator check warns about.

### 429: Why can't you dispatch while middleware is being set up?

During `applyMiddleware`, the final `dispatch` isn't built yet. If a middleware calls `dispatch` in its outer function (when it receives `storeApi`), Redux throws "Dispatching while constructing your middleware is not allowed". Dispatch only inside the `action => {}` handler, or later from effects.

### 430: Why does purity of reducers matter so much?

- The DevTools replays actions to recompute states when you toggle or reorder actions. Side effects would run again.
- Time travel and action replay in tests require that the same actions always give the same state.
- React-Redux and selectors use reference equality to skip work. Mutating instead of returning new references breaks that.
- RTK Query and other middleware assume reducers return immediately and don't dispatch.

### 431: Where should you generate random IDs or timestamps?

In a prepare callback, a thunk, or the component, never in the reducer. The reducer must return the same output for the same input.

```ts
messageAdded: {
  reducer(state, action: PayloadAction<Message>) {
    state.push(action.payload)
  },
  prepare(text: string) {
    return { payload: { id: nanoid(), text, createdAt: Date.now() } }
  },
},
```

The values become part of the action, so replaying the action gives the same result.

### 432: What issues can RTK 2's ESM packaging cause in Jest?

Jest (with CommonJS) can pick the wrong build or fail on `export` syntax in dependencies. Things that help:

- Use a current Jest version, which supports the `exports` field.
- If a dependency still fails, add it to `transformIgnorePatterns` exceptions so it's transpiled.
- Or use Vitest, which handles ESM natively and is what the official templates use.

RTK 2 ships both ESM and CJS builds, so most setups work without changes.

### 433: What TypeScript settings does RTK 2 need?

A recent TypeScript 5.x version, `strict: true` (inference relies on strict null checks), and a `moduleResolution` that understands the `exports` field: `"bundler"`, `"node16"` or `"nodenext"`. Older `"node"` resolution may still work through fallbacks, but the newer options are recommended. `skipLibCheck: true` speeds up builds and is common.

### 434: What should you check when upgrading from RTK 1.x to 2.x?

1. Convert `extraReducers` and `createReducer` from object syntax to the builder (codemods exist).
2. Change `configureStore({ middleware: [...] })` to the callback form, and `enhancers` to a callback.
3. Replace `getDefaultMiddleware` imports with the callback argument.
4. Replace `AnyAction` with `UnknownAction` and narrow actions in middleware.
5. Make sure all action types are strings.
6. Update React-Redux to 9 and Reselect usage (`defaultMemoize` is now `lruMemoize`).
7. Entity adapter types now include the ID type: `EntityState<T, Id>`.
8. RTK Query: check code that relied on immediate invalidation, since `'delayed'` is now the default.
9. Run tests and watch for new dev check warnings from Reselect and `useSelector`.

### 435: What codemods are available for the RTK 2 upgrade?

The `@reduxjs/rtk-codemods` package has transforms such as `createReducerBuilder`, `createSliceBuilder` and `createSliceReducerBuilder`, which convert the old object syntax to the builder and callback forms.

```bash
npx @reduxjs/rtk-codemods createSliceBuilder ./src/**/*.ts
```

Review the changes before committing, especially in files with complex TypeScript types.

### 436: Are the functions returned by RTK Query hooks stable?

The trigger functions from `useMutation` and `useLazyQuery`, and `refetch` from `useQuery`, are memoized inside the hook and keep the same identity across renders, so they are safe in `useEffect` dependency lists. The result objects themselves are new when any field changes, so don't put the whole result object in a dependency list. Depend on the fields you use.

### 437: How do you structure Redux in a large monorepo with feature packages?

- A core package creates the store with `combineSlices`, a base `createApi` with empty endpoints, a listener middleware and a dynamic middleware.
- Each feature package exports a setup function or self-injects: `slice.injectInto(rootReducer)`, `api.injectEndpoints(...)`, `startAppListening(...)`.
- Features depend on the core package, never on each other's internals. Cross-feature communication goes through shared action creators or public selectors.
- Use `withLazyLoadedSlices` and module augmentation so `RootState` knows about features without importing them.
- Keep one copy of `@reduxjs/toolkit` and `react-redux` in the dependency tree.

### 438: How do you log Redux actions to an error tracking tool?

Add breadcrumbs from a middleware, and include a sanitized state snapshot when errors happen.

```ts
export const breadcrumbMiddleware: Middleware = () => (next) => (action) => {
  if (isAction(action)) {
    Sentry.addBreadcrumb({
      category: "redux",
      message: action.type,
      level: "info",
    });
  }
  return next(action);
};
```

Log only the type, not the payload, unless you are sure the payload has no personal data. Sentry also has a Redux enhancer that does this with options for sanitizing.

### 439: How do you find performance problems in a Redux app?

1. React DevTools Profiler: record an interaction and see which components rendered and why.
2. Redux DevTools: check how many actions fire and how big the state changes are.
3. Look for selectors that return new references (the dev mode checks help), components selecting too much state, and lists without memoized rows.
4. Look at reducer time with the browser performance panel if dispatches feel slow. Large Immer drafts or dev checks are common causes in development.
5. Always test production builds before deciding, because dev checks and Immer dev behavior slow development builds.

### 440: How do you choose between a thunk, a listener and RTK Query lifecycle callbacks?

- RTK Query endpoint or lifecycle callback: anything about fetching and caching server data, optimistic updates, streaming into a cache entry.
- Thunk: imperative logic started by the UI that needs `dispatch` and `getState`, like "submit this form, then navigate".
- Listener: reactive logic that runs when something happens, regardless of who caused it, like persistence, analytics, starting sockets after login, debouncing, or multi-step workflows.

If you find yourself dispatching an action just so a thunk can run, it may be a listener. If you write a thunk that only fetches and stores data, it's probably an RTK Query endpoint.

### 441: How would you design the state for a project management app?

```ts
{
  api: { /* RTK Query cache: projects, tasks, users, comments */ },
  auth: { userId, status },
  ui: {
    sidebarOpen,
    activeProjectId,
    taskFilters: { assignee, status, search },
  },
  drafts: {
    // tasks being edited, keyed by id, normalized with an entity adapter
  },
}
```

- Server data lives in RTK Query, with tags per entity and LIST tags.
- UI choices that affect queries (filters, active project) live in a `ui` slice and become query arguments.
- Data heavily edited before saving lives in a `drafts` slice, created from the cached server data.
- Listeners handle autosave of drafts with debouncing and a websocket for live updates.
- Form inputs and hover states stay in components.

### 442: How do you keep cached data separate per tenant or workspace?

Include the tenant ID in every query argument, so cache keys differ per tenant, or reset the API state when the tenant changes.

```ts
getProjects: build.query<Project[], { workspaceId: string }>({
  query: ({ workspaceId }) => `workspaces/${workspaceId}/projects`,
  providesTags: (result, error, { workspaceId }) => [{ type: 'Project', id: `LIST-${workspaceId}` }],
}),
```

If the tenant comes from the auth token and isn't in the URL, it's easy to show data from the wrong tenant after switching. In that case call `api.util.resetApiState()` on switch.

### 443: How do you invalidate tags based on the mutation response?

`invalidatesTags` receives the result, so the server can tell you what changed.

```ts
bulkArchive: build.mutation<{ archivedIds: string[] }, string[]>({
  query: (ids) => ({ url: 'tasks/archive', method: 'POST', body: { ids } }),
  invalidatesTags: (result) =>
    result
      ? [...result.archivedIds.map((id) => ({ type: 'Task' as const, id })), { type: 'Task', id: 'LIST' }]
      : [],
}),
```

### 444: How do you wait for a specific running query, for example before a navigation?

Use `getRunningQueryThunk`.

```ts
const running = dispatch(api.util.getRunningQueryThunk("getPost", postId));
if (running) {
  await running;
}
```

It returns `undefined` if there's no request in flight for that key.

### 445: How do you use entity adapter selectors in `createSlice.selectors`?

Spread `adapter.getSelectors()` (with no argument) into `selectors`. The slice wraps them to work with the root state.

```ts
const todosSlice = createSlice({
  name: "todos",
  initialState: todosAdapter.getInitialState(),
  reducers: { todoAdded: todosAdapter.addOne },
  selectors: {
    ...todosAdapter.getSelectors(),
    selectOpenCount: (state) =>
      state.ids.filter((id) => !state.entities[id].completed).length,
  },
});

export const { selectAll: selectAllTodos, selectById: selectTodoById } =
  todosSlice.selectors;

const todo = useAppSelector((state) => selectTodoById(state, id));
```

### 446: How do you write a reusable helper for list tags?

```ts
function providesList<R extends { id: string | number }[], T extends string>(
  resultsWithIds: R | undefined,
  tagType: T,
) {
  return resultsWithIds
    ? [{ type: tagType, id: 'LIST' }, ...resultsWithIds.map(({ id }) => ({ type: tagType, id }))]
    : [{ type: tagType, id: 'LIST' }]
}

getPosts: build.query<Post[], void>({
  query: () => 'posts',
  providesTags: (result) => providesList(result, 'Post'),
}),
```

### 447: What are good rules for the shape of the root state?

- Keep it flat. Top-level keys per domain or feature.
- Separate entity data, UI state and session state.
- Normalize collections that are looked up by ID or appear in several places.
- Store minimal data and derive the rest with selectors.
- Keep everything serializable.
- Don't mirror the component tree. Components change more often than domain data.

### 448: Should form state go into Redux?

Usually no. Form input values change on every keystroke, are local to one form, and are thrown away after submit. Libraries like React Hook Form or plain `useState` handle them better. Put a form in Redux only when the data must survive navigation (a long wizard), be visible elsewhere (a live preview in another part of the app), or be autosaved by a listener. Even then, update Redux on blur or with debouncing instead of every keystroke if performance becomes a problem.

### 449: How would you move data fetching from sagas to RTK Query step by step?

1. Add a base `createApi` and its middleware next to the saga middleware.
2. Pick one read-only feature. Add a query endpoint and switch its components to the hook.
3. Remove that feature's fetch saga, its loading/error reducers and its data from the slice, once nothing reads them.
4. Move mutations next, using tags to replace "refetch after save" sagas.
5. Move remaining non-fetching sagas (workflows, sockets) to the listener middleware.
6. Remove `redux-saga` when nothing uses it.

Each step ships on its own, so the app keeps working the whole time.

### 450: Walk through what happens when you dispatch a slice action in an RTK store.

1. `dispatch(todoAdded('Buy milk'))` calls the action creator. The prepare callback builds `{ type: 'todos/todoAdded', payload: {...} }`.
2. The action goes through the middleware chain: listener middleware (if prepended), thunk (passes plain objects on), dev checks, RTK Query middleware, your own middleware.
3. It reaches the real `dispatch`, which calls the root reducer.
4. The root reducer calls each slice reducer. The todos reducer finds the case reducer by type and runs it with Immer, which returns a new state with new references only on the changed path. Other slices return their current state.
5. The store saves the new state.
6. Subscribers are notified. If the action was marked for auto-batching, notification may wait until the end of the frame.
7. Back in the middleware chain, code after `next(action)` runs. The serializability and immutability checks inspect the new state, and listener predicates and effects run.
8. React-Redux runs every `useSelector` selector, compares results, and re-renders only the components whose selected values changed.
