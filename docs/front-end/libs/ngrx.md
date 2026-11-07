# NgRx Interview Questions and Answers

_Last updated: October 28, 2026_

450 NgRx interview questions with answers, split into easy, moderate and advanced. The examples use the current NgRx APIs: standalone providers (`provideStore`, `provideState`, `provideEffects`), functional effects, `createActionGroup`, `createFeature`, `selectSignal`, and `@ngrx/signals` (SignalStore, entities, `rxMethod`, `signalMethod` and the events plugin), together with modern Angular (signals, `inject()`, `input()`, built-in control flow).

## Table of Contents

- [Easy Questions (1-150)](#easy-questions)
- [Moderate Questions (151-300)](#moderate-questions)
- [Advanced Questions (301-450)](#advanced-questions)

### Easy Questions (1-150)

- [1: What is NgRx?](#1-what-is-ngrx)
- [2: What problem does NgRx solve?](#2-what-problem-does-ngrx-solve)
- [3: What are the main packages in NgRx?](#3-what-are-the-main-packages-in-ngrx)
- [4: What is the Redux pattern?](#4-what-is-the-redux-pattern)
- [5: What are the core principles behind NgRx Store?](#5-what-are-the-core-principles-behind-ngrx-store)
- [6: What is the Store?](#6-what-is-the-store)
- [7: What is an action?](#7-what-is-an-action)
- [8: What is a reducer?](#8-what-is-a-reducer)
- [9: What is a selector?](#9-what-is-a-selector)
- [10: What is an effect?](#10-what-is-an-effect)
- [11: How do you install NgRx?](#11-how-do-you-install-ngrx)
- [12: What does `ng add @ngrx/store` do?](#12-what-does-ng-add-ngrxstore-do)
- [13: How do you register the store in a standalone Angular app?](#13-how-do-you-register-the-store-in-a-standalone-angular-app)
- [14: What is `provideState`?](#14-what-is-providestate)
- [15: How do you create an action with `createAction`?](#15-how-do-you-create-an-action-with-createaction)
- [16: What is `props<>()`?](#16-what-is-props)
- [17: What is `emptyProps()`?](#17-what-is-emptyprops)
- [18: What is `createActionGroup`?](#18-what-is-createactiongroup)
- [19: How are event names turned into function names in `createActionGroup`?](#19-how-are-event-names-turned-into-function-names-in-createactiongroup)
- [20: What is the `[Source] Event` naming convention?](#20-what-is-the-source-event-naming-convention)
- [21: Why should every action type be unique?](#21-why-should-every-action-type-be-unique)
- [22: What is "good action hygiene"?](#22-what-is-good-action-hygiene)
- [23: How do you dispatch an action?](#23-how-do-you-dispatch-an-action)
- [24: Can you dispatch an action from a template?](#24-can-you-dispatch-an-action-from-a-template)
- [25: What does `createReducer` do?](#25-what-does-createreducer-do)
- [26: What is the `on()` function?](#26-what-is-the-on-function)
- [27: Why must reducers be pure functions?](#27-why-must-reducers-be-pure-functions)
- [28: How do you return a new state without mutating the old one?](#28-how-do-you-return-a-new-state-without-mutating-the-old-one)
- [29: What is initial state?](#29-what-is-initial-state)
- [30: Can one `on()` handle several actions?](#30-can-one-on-handle-several-actions)
- [31: What happens to actions a reducer doesn't handle?](#31-what-happens-to-actions-a-reducer-doesnt-handle)
- [32: What is `createFeature`?](#32-what-is-createfeature)
- [33: Which selectors does `createFeature` create for you?](#33-which-selectors-does-createfeature-create-for-you)
- [34: What is `createFeatureSelector`?](#34-what-is-createfeatureselector)
- [35: What is `createSelector`?](#35-what-is-createselector)
- [36: How do you read state in a component using `store.select`?](#36-how-do-you-read-state-in-a-component-using-storeselect)
- [37: What is `store.selectSignal`?](#37-what-is-storeselectsignal)
- [38: What is the difference between `select` and `selectSignal`?](#38-what-is-the-difference-between-select-and-selectsignal)
- [39: Why use selectors instead of reading state directly?](#39-why-use-selectors-instead-of-reading-state-directly)
- [40: What is memoization in selectors?](#40-what-is-memoization-in-selectors)
- [41: How many input selectors can `createSelector` take?](#41-how-many-input-selectors-can-createselector-take)
- [42: What is a projector function?](#42-what-is-a-projector-function)
- [43: How do you use a selected signal in a template?](#43-how-do-you-use-a-selected-signal-in-a-template)
- [44: How do you use `store.select` with the `async` pipe?](#44-how-do-you-use-storeselect-with-the-async-pipe)
- [45: What is `@ngrx/effects`?](#45-what-is-ngrxeffects)
- [46: What is the `Actions` stream?](#46-what-is-the-actions-stream)
- [47: What is `ofType`?](#47-what-is-oftype)
- [48: How do you write a class-based effect?](#48-how-do-you-write-a-class-based-effect)
- [49: How do you write a functional effect?](#49-how-do-you-write-a-functional-effect)
- [50: How do you register effects with `provideEffects`?](#50-how-do-you-register-effects-with-provideeffects)
- [51: What does `{ dispatch: false }` mean in an effect?](#51-what-does--dispatch-false--mean-in-an-effect)
- [52: What happens if an effect with default config emits something that isn't an action?](#52-what-happens-if-an-effect-with-default-config-emits-something-that-isnt-an-action)
- [53: What is a side effect in the context of NgRx?](#53-what-is-a-side-effect-in-the-context-of-ngrx)
- [54: Can you show a simple effect that loads data with `HttpClient`?](#54-can-you-show-a-simple-effect-that-loads-data-with-httpclient)
- [55: How do you handle errors in an effect?](#55-how-do-you-handle-errors-in-an-effect)
- [56: Why should `catchError` be inside the inner observable and not on the outer stream?](#56-why-should-catcherror-be-inside-the-inner-observable-and-not-on-the-outer-stream)
- [57: What is `@ngrx/store-devtools`?](#57-what-is-ngrxstore-devtools)
- [58: How do you set up Store DevTools?](#58-how-do-you-set-up-store-devtools)
- [59: What does the `maxAge` option do?](#59-what-does-the-maxage-option-do)
- [60: What does the `logOnly` option do?](#60-what-does-the-logonly-option-do)
- [61: What is time-travel debugging?](#61-what-is-time-travel-debugging)
- [62: What is `@ngrx/entity`?](#62-what-is-ngrxentity)
- [63: What is `EntityState`?](#63-what-is-entitystate)
- [64: What is `createEntityAdapter`?](#64-what-is-createentityadapter)
- [65: What does `getInitialState` do?](#65-what-does-getinitialstate-do)
- [66: Name some entity adapter methods.](#66-name-some-entity-adapter-methods)
- [67: What is the difference between `addOne` and `setOne`?](#67-what-is-the-difference-between-addone-and-setone)
- [68: What does `getSelectors` return?](#68-what-does-getselectors-return)
- [69: What is the `selectId` option in `createEntityAdapter`?](#69-what-is-the-selectid-option-in-createentityadapter)
- [70: What is the `sortComparer` option?](#70-what-is-the-sortcomparer-option)
- [71: What is `@ngrx/router-store`?](#71-what-is-ngrxrouter-store)
- [72: How do you set up router-store?](#72-how-do-you-set-up-router-store)
- [73: What is `getRouterSelectors`?](#73-what-is-getrouterselectors)
- [74: What is `@ngrx/signals`?](#74-what-is-ngrxsignals)
- [75: What is NgRx SignalStore?](#75-what-is-ngrx-signalstore)
- [76: What does the `signalStore()` function return?](#76-what-does-the-signalstore-function-return)
- [77: What does `withState` do?](#77-what-does-withstate-do)
- [78: What does `withComputed` do?](#78-what-does-withcomputed-do)
- [79: What does `withMethods` do?](#79-what-does-withmethods-do)
- [80: What is `patchState`?](#80-what-is-patchstate)
- [81: How do you provide a SignalStore?](#81-how-do-you-provide-a-signalstore)
- [82: How do you use a SignalStore in a component?](#82-how-do-you-use-a-signalstore-in-a-component)
- [83: What is `signalState`?](#83-what-is-signalstate)
- [84: What is the difference between `signalState` and `signalStore`?](#84-what-is-the-difference-between-signalstate-and-signalstore)
- [85: What is `withHooks`?](#85-what-is-withhooks)
- [86: What is `rxMethod`?](#86-what-is-rxmethod)
- [87: What is `@ngrx/component`?](#87-what-is-ngrxcomponent)
- [88: What is the `ngrxPush` pipe?](#88-what-is-the-ngrxpush-pipe)
- [89: What is the `*ngrxLet` directive?](#89-what-is-the-ngrxlet-directive)
- [90: What is `@ngrx/component-store`?](#90-what-is-ngrxcomponent-store)
- [91: What is `@ngrx/operators`?](#91-what-is-ngrxoperators)
- [92: What is `tapResponse`?](#92-what-is-tapresponse)
- [93: What is `concatLatestFrom`?](#93-what-is-concatlatestfrom)
- [94: What is `@ngrx/schematics`?](#94-what-is-ngrxschematics)
- [95: What is `@ngrx/eslint-plugin`?](#95-what-is-ngrxeslint-plugin)
- [96: What are runtime checks in NgRx Store?](#96-what-are-runtime-checks-in-ngrx-store)
- [97: Which runtime checks are on by default?](#97-which-runtime-checks-are-on-by-default)
- [98: What is the `@ngrx/store/init` action?](#98-what-is-the-ngrxstoreinit-action)
- [99: How do you type a feature state?](#99-how-do-you-type-a-feature-state)
- [100: Should you type the global store with `Store<AppState>`?](#100-should-you-type-the-global-store-with-storeappstate)
- [101: What is a feature state?](#101-what-is-a-feature-state)
- [102: What is root state?](#102-what-is-root-state)
- [103: How do you lazy load feature state?](#103-how-do-you-lazy-load-feature-state)
- [104: What is a meta-reducer?](#104-what-is-a-meta-reducer)
- [105: What are common uses for meta-reducers?](#105-what-are-common-uses-for-meta-reducers)
- [106: What does `Store` extend?](#106-what-does-store-extend)
- [107: Does the store emit the current state when you subscribe?](#107-does-the-store-emit-the-current-state-when-you-subscribe)
- [108: What is unidirectional data flow?](#108-what-is-unidirectional-data-flow)
- [109: When should you not use NgRx Store?](#109-when-should-you-not-use-ngrx-store)
- [110: How has NgRx reduced boilerplate over time?](#110-how-has-ngrx-reduced-boilerplate-over-time)
- [111: How do you test a reducer?](#111-how-do-you-test-a-reducer)
- [112: How do you test a selector?](#112-how-do-you-test-a-selector)
- [113: What is `provideMockStore`?](#113-what-is-providemockstore)
- [114: What is `MockStore`?](#114-what-is-mockstore)
- [115: What is `overrideSelector`?](#115-what-is-overrideselector)
- [116: What is `provideMockActions`?](#116-what-is-providemockactions)
- [117: How do you write a simple test for a SignalStore?](#117-how-do-you-write-a-simple-test-for-a-signalstore)
- [118: Why should action payloads be serializable?](#118-why-should-action-payloads-be-serializable)
- [119: Can an action have no payload?](#119-can-an-action-have-no-payload)
- [120: What is the `type` property of an action creator?](#120-what-is-the-type-property-of-an-action-creator)
- [121: Can you use string enums for action types?](#121-can-you-use-string-enums-for-action-types)
- [122: What is the `Action` interface?](#122-what-is-the-action-interface)
- [123: What is the `ActionReducer` type?](#123-what-is-the-actionreducer-type)
- [124: What is the `select` operator from `@ngrx/store`?](#124-what-is-the-select-operator-from-ngrxstore)
- [125: Why doesn't the UI re-render when unrelated state changes?](#125-why-doesnt-the-ui-re-render-when-unrelated-state-changes)
- [126: How do you combine several pieces of state for a component?](#126-how-do-you-combine-several-pieces-of-state-for-a-component)
- [127: What is a view model selector?](#127-what-is-a-view-model-selector)
- [128: How can you reset the whole state on logout?](#128-how-can-you-reset-the-whole-state-on-logout)
- [129: How do you keep track of loading and error states?](#129-how-do-you-keep-track-of-loading-and-error-states)
- [130: How do you show a loading spinner with NgRx state?](#130-how-do-you-show-a-loading-spinner-with-ngrx-state)
- [131: What is normalized state?](#131-what-is-normalized-state)
- [132: Why should state be serializable?](#132-why-should-state-be-serializable)
- [133: Should form input values live in the store?](#133-should-form-input-values-live-in-the-store)
- [134: What kind of state belongs in the global store?](#134-what-kind-of-state-belongs-in-the-global-store)
- [135: What are container and presentational components in an NgRx app?](#135-what-are-container-and-presentational-components-in-an-ngrx-app)
- [136: Do you need to unsubscribe from store selections?](#136-do-you-need-to-unsubscribe-from-store-selections)
- [137: How do NgRx versions relate to Angular versions?](#137-how-do-ngrx-versions-relate-to-angular-versions)
- [138: How do you upgrade NgRx?](#138-how-do-you-upgrade-ngrx)
- [139: What are NgRx migration schematics?](#139-what-are-ngrx-migration-schematics)
- [140: What is `withEntities`?](#140-what-is-withentities)
- [141: Which entity updaters are there in `@ngrx/signals/entities`?](#141-which-entity-updaters-are-there-in-ngrxsignalsentities)
- [142: What does `getState` do?](#142-what-does-getstate-do)
- [143: What is `withProps`?](#143-what-is-withprops)
- [144: Can you call `patchState` on a SignalStore from outside the store?](#144-can-you-call-patchstate-on-a-signalstore-from-outside-the-store)
- [145: What is the `type<T>()` helper?](#145-what-is-the-typet-helper)
- [146: What does `{ providedIn: 'root' }` do in `signalStore`?](#146-what-does--providedin-root--do-in-signalstore)
- [147: What is a DeepSignal?](#147-what-is-a-deepsignal)
- [148: Can you use NgRx with standalone components?](#148-can-you-use-ngrx-with-standalone-components)
- [149: Can you still use NgRx with NgModules?](#149-can-you-still-use-ngrx-with-ngmodules)
- [150: What is the difference between NgRx Store and SignalStore, in simple terms?](#150-what-is-the-difference-between-ngrx-store-and-signalstore-in-simple-terms)

### Moderate Questions (151-300)

- [151: Walk through what happens from `dispatch` to the UI update.](#151-walk-through-what-happens-from-dispatch-to-the-ui-update)
- [152: Do reducers or effects see an action first?](#152-do-reducers-or-effects-see-an-action-first)
- [153: What are `extraSelectors` in `createFeature`?](#153-what-are-extraselectors-in-createfeature)
- [154: How do you write a selector that takes a parameter?](#154-how-do-you-write-a-selector-that-takes-a-parameter)
- [155: Why were selectors with props removed?](#155-why-were-selectors-with-props-removed)
- [156: How does selector memoization decide whether to recompute?](#156-how-does-selector-memoization-decide-whether-to-recompute)
- [157: What does `release()` do on a selector?](#157-what-does-release-do-on-a-selector)
- [158: How do you change the memoization of a selector?](#158-how-do-you-change-the-memoization-of-a-selector)
- [159: What are `defaultMemoize` and `isEqualCheck`?](#159-what-are-defaultmemoize-and-isequalcheck)
- [160: Why does memoization matter for selectors that filter or map lists?](#160-why-does-memoization-matter-for-selectors-that-filter-or-map-lists)
- [161: A selector returns a new object every time. Why is that a problem and how do you fix it?](#161-a-selector-returns-a-new-object-every-time-why-is-that-a-problem-and-how-do-you-fix-it)
- [162: What is the `equal` option of `selectSignal`?](#162-what-is-the-equal-option-of-selectsignal)
- [163: What is the difference between `switchMap`, `mergeMap`, `concatMap` and `exhaustMap` in effects?](#163-what-is-the-difference-between-switchmap-mergemap-concatmap-and-exhaustmap-in-effects)
- [164: When would you use `exhaustMap`?](#164-when-would-you-use-exhaustmap)
- [165: When would you use `concatMap`?](#165-when-would-you-use-concatmap)
- [166: When would you use `mergeMap`?](#166-when-would-you-use-mergemap)
- [167: Why is `switchMap` risky for write operations?](#167-why-is-switchmap-risky-for-write-operations)
- [168: How do you read state inside an effect?](#168-how-do-you-read-state-inside-an-effect)
- [169: Why use `concatLatestFrom` instead of `withLatestFrom`?](#169-why-use-concatlatestfrom-instead-of-withlatestfrom)
- [170: Can an effect start from something other than an action?](#170-can-an-effect-start-from-something-other-than-an-action)
- [171: What is `ROOT_EFFECTS_INIT`?](#171-what-is-root_effects_init)
- [172: What is the `OnInitEffects` interface?](#172-what-is-the-oniniteffects-interface)
- [173: What does NgRx do by default when an effect throws?](#173-what-does-ngrx-do-by-default-when-an-effect-throws)
- [174: How do you write a custom effects error handler?](#174-how-do-you-write-a-custom-effects-error-handler)
- [175: Can an effect dispatch more than one action?](#175-can-an-effect-dispatch-more-than-one-action)
- [176: How do you navigate from an effect?](#176-how-do-you-navigate-from-an-effect)
- [177: How do functional effects make testing easier?](#177-how-do-functional-effects-make-testing-easier)
- [178: Where do effects run and how long do they live?](#178-where-do-effects-run-and-how-long-do-they-live)
- [179: How do you debounce a search in an effect?](#179-how-do-you-debounce-a-search-in-an-effect)
- [180: How do you poll an API with effects?](#180-how-do-you-poll-an-api-with-effects)
- [181: How do you cancel an in-flight request with an action?](#181-how-do-you-cancel-an-in-flight-request-with-an-action)
- [182: What are the options of `tapResponse`?](#182-what-are-the-options-of-tapresponse)
- [183: What is `mapResponse`?](#183-what-is-mapresponse)
- [184: How does `createActionGroup` keep things type safe?](#184-how-does-createactiongroup-keep-things-type-safe)
- [185: How do you get the type of an action created with an action creator?](#185-how-do-you-get-the-type-of-an-action-created-with-an-action-creator)
- [186: How does typing work when one `on` handles actions with different props?](#186-how-does-typing-work-when-one-on-handles-actions-with-different-props)
- [187: How do you update deeply nested state in a reducer?](#187-how-do-you-update-deeply-nested-state-in-a-reducer)
- [188: Can you use Immer with NgRx?](#188-can-you-use-immer-with-ngrx)
- [189: Show a meta-reducer that resets state on logout, with types.](#189-show-a-meta-reducer-that-resets-state-on-logout-with-types)
- [190: How do you save and load state from `localStorage` with a meta-reducer?](#190-how-do-you-save-and-load-state-from-localstorage-with-a-meta-reducer)
- [191: How do you add meta-reducers to a single feature?](#191-how-do-you-add-meta-reducers-to-a-single-feature)
- [192: When should you turn on `strictActionWithinNgZone` and `strictActionTypeUniqueness`?](#192-when-should-you-turn-on-strictactionwithinngzone-and-strictactiontypeuniqueness)
- [193: When is it OK to turn off the serializability checks?](#193-when-is-it-ok-to-turn-off-the-serializability-checks)
- [194: How do you use `updateOne`, `upsertOne` and `mapOne`?](#194-how-do-you-use-updateone-upsertone-and-mapone)
- [195: How do you keep extra fields next to entities?](#195-how-do-you-keep-extra-fields-next-to-entities)
- [196: How do you combine entity selectors with `createFeature`?](#196-how-do-you-combine-entity-selectors-with-createfeature)
- [197: What is the cost of `sortComparer`?](#197-what-is-the-cost-of-sortcomparer)
- [198: How do you select route params inside a feature selector?](#198-how-do-you-select-route-params-inside-a-feature-selector)
- [199: Which actions does router-store dispatch?](#199-which-actions-does-router-store-dispatch)
- [200: What is the `navigationActionTiming` option?](#200-what-is-the-navigationactiontiming-option)
- [201: What is the difference between `RouterState.Minimal` and `RouterState.Full`?](#201-what-is-the-difference-between-routerstateminimal-and-routerstatefull)
- [202: How do you write a custom router state serializer?](#202-how-do-you-write-a-custom-router-state-serializer)
- [203: How do you read route `data` and `title` with router-store?](#203-how-do-you-read-route-data-and-title-with-router-store)
- [204: Can `withState` take a function?](#204-can-withstate-take-a-function)
- [205: Can a `withComputed` use members from an earlier `withComputed`?](#205-can-a-withcomputed-use-members-from-an-earlier-withcomputed)
- [206: How do you use injected services in `withMethods`?](#206-how-do-you-use-injected-services-in-withmethods)
- [207: How do you write a Promise-based async method in SignalStore?](#207-how-do-you-write-a-promise-based-async-method-in-signalstore)
- [208: Show an `rxMethod` that searches as the query signal changes.](#208-show-an-rxmethod-that-searches-as-the-query-signal-changes)
- [209: What kinds of input can an `rxMethod` accept?](#209-what-kinds-of-input-can-an-rxmethod-accept)
- [210: What is `signalMethod`?](#210-what-is-signalmethod)
- [211: When do you pick `signalMethod` over `rxMethod`?](#211-when-do-you-pick-signalmethod-over-rxmethod)
- [212: How do you use injected services inside `withHooks`?](#212-how-do-you-use-injected-services-inside-withhooks)
- [213: How do you write reusable updater functions for `patchState`?](#213-how-do-you-write-reusable-updater-functions-for-patchstate)
- [214: What is `watchState`?](#214-what-is-watchstate)
- [215: How do you use named collections with `withEntities`?](#215-how-do-you-use-named-collections-with-withentities)
- [216: What is `entityConfig`?](#216-what-is-entityconfig)
- [217: How do you handle entities without an `id` property in SignalStore?](#217-how-do-you-handle-entities-without-an-id-property-in-signalstore)
- [218: What is `signalStoreFeature`?](#218-what-is-signalstorefeature)
- [219: How do you write a custom feature that needs something from the store?](#219-how-do-you-write-a-custom-feature-that-needs-something-from-the-store)
- [220: How do you write updaters that go with a custom feature?](#220-how-do-you-write-updaters-that-go-with-a-custom-feature)
- [221: What is `withProps` used for besides services?](#221-what-is-withprops-used-for-besides-services)
- [222: How do private members work in SignalStore?](#222-how-do-private-members-work-in-signalstore)
- [223: Why is `protectedState` true by default?](#223-why-is-protectedstate-true-by-default)
- [224: What happens when a SignalStore is provided in a component?](#224-what-happens-when-a-signalstore-is-provided-in-a-component)
- [225: How can several components share one SignalStore instance without it being global?](#225-how-can-several-components-share-one-signalstore-instance-without-it-being-global)
- [226: What is `deepComputed`?](#226-what-is-deepcomputed)
- [227: How do you turn a SignalStore signal into an observable?](#227-how-do-you-turn-a-signalstore-signal-into-an-observable)
- [228: How do you use Angular `resource` or `httpResource` with SignalStore?](#228-how-do-you-use-angular-resource-or-httpresource-with-signalstore)
- [229: What is `withLinkedState`?](#229-what-is-withlinkedstate)
- [230: What is `withFeature`?](#230-what-is-withfeature)
- [231: How do you set state directly in a SignalStore test?](#231-how-do-you-set-state-directly-in-a-signalstore-test)
- [232: How do you test a store method that uses `rxMethod` and debounce?](#232-how-do-you-test-a-store-method-that-uses-rxmethod-and-debounce)
- [233: How do you mock dependencies of a SignalStore?](#233-how-do-you-mock-dependencies-of-a-signalstore)
- [234: What are `setState` and `refreshState` in `MockStore`?](#234-what-are-setstate-and-refreshstate-in-mockstore)
- [235: How do you test a class-based effect with `provideMockActions`?](#235-how-do-you-test-a-class-based-effect-with-providemockactions)
- [236: How do you test a component that uses `selectSignal` with `MockStore`?](#236-how-do-you-test-a-component-that-uses-selectsignal-with-mockstore)
- [237: When would you write an integration test with the real store?](#237-when-would-you-write-an-integration-test-with-the-real-store)
- [238: What does `resetSelectors` do on `MockStore`?](#238-what-does-resetselectors-do-on-mockstore)
- [239: What are the main parts of the `ComponentStore` API?](#239-what-are-the-main-parts-of-the-componentstore-api)
- [240: How does ComponentStore compare to SignalStore?](#240-how-does-componentstore-compare-to-signalstore)
- [241: How does `*ngrxLet` handle errors and loading?](#241-how-does-ngrxlet-handle-errors-and-loading)
- [242: How is `ngrxPush` different from `async`?](#242-how-is-ngrxpush-different-from-async)
- [243: Does NgRx work with zoneless Angular?](#243-does-ngrx-work-with-zoneless-angular)
- [244: Why do NgRx and `OnPush` work well together?](#244-why-do-ngrx-and-onpush-work-well-together)
- [245: How would you organize NgRx files in a feature folder?](#245-how-would-you-organize-ngrx-files-in-a-feature-folder)
- [246: What naming conventions are common in NgRx code?](#246-what-naming-conventions-are-common-in-ngrx-code)
- [247: What is the facade pattern with NgRx and what are its pros and cons?](#247-what-is-the-facade-pattern-with-ngrx-and-what-are-its-pros-and-cons)
- [248: What is the difference between event-style and command-style actions?](#248-what-is-the-difference-between-event-style-and-command-style-actions)
- [249: Why should you avoid dispatching several actions one after another?](#249-why-should-you-avoid-dispatching-several-actions-one-after-another)
- [250: What is an optimistic update and how do you do it with NgRx Store?](#250-what-is-an-optimistic-update-and-how-do-you-do-it-with-ngrx-store)
- [251: What is a pessimistic update?](#251-what-is-a-pessimistic-update)
- [252: How do you handle a form submit with NgRx Store and show server errors?](#252-how-do-you-handle-a-form-submit-with-ngrx-store-and-show-server-errors)
- [253: How can you add and remove reducers at runtime?](#253-how-can-you-add-and-remove-reducers-at-runtime)
- [254: Which NgRx schematics commands are most useful?](#254-which-ngrx-schematics-commands-are-most-useful)
- [255: How do you make NgRx the default schematics collection?](#255-how-do-you-make-ngrx-the-default-schematics-collection)
- [256: Name some useful rules from `@ngrx/eslint-plugin`.](#256-name-some-useful-rules-from-ngrxeslint-plugin)
- [257: What lint rules exist for `@ngrx/signals`?](#257-what-lint-rules-exist-for-ngrxsignals)
- [258: Why can't the root of SignalStore state be an array?](#258-why-cant-the-root-of-signalstore-state-be-an-array)
- [259: How do you hide sensitive data in DevTools?](#259-how-do-you-hide-sensitive-data-in-devtools)
- [260: What does the `trace` option in DevTools do?](#260-what-does-the-trace-option-in-devtools-do)
- [261: Should Store DevTools be enabled in production?](#261-should-store-devtools-be-enabled-in-production)
- [262: Can you use Redux DevTools with SignalStore?](#262-can-you-use-redux-devtools-with-signalstore)
- [263: How do you avoid fetching data twice with SSR and NgRx Store?](#263-how-do-you-avoid-fetching-data-twice-with-ssr-and-ngrx-store)
- [264: Where should the auth token live?](#264-where-should-the-auth-token-live)
- [265: Why is putting a `Date` object in state a problem?](#265-why-is-putting-a-date-object-in-state-a-problem)
- [266: How do you write a selector that uses data from two features?](#266-how-do-you-write-a-selector-that-uses-data-from-two-features)
- [267: What are good rules for dependencies between features?](#267-what-are-good-rules-for-dependencies-between-features)
- [268: How do you mix store signals with component-only state?](#268-how-do-you-mix-store-signals-with-component-only-state)
- [269: Can `store.dispatch` take a signal?](#269-can-storedispatch-take-a-signal)
- [270: What does `dispatch` return when you pass a function?](#270-what-does-dispatch-return-when-you-pass-a-function)
- [271: How do you use a component input with a factory selector?](#271-how-do-you-use-a-component-input-with-a-factory-selector)
- [272: How do you use the store in a functional route guard?](#272-how-do-you-use-the-store-in-a-functional-route-guard)
- [273: How do you make sure data is loaded before a route activates?](#273-how-do-you-make-sure-data-is-loaded-before-a-route-activates)
- [274: Should you load data when a component starts or on router navigation?](#274-should-you-load-data-when-a-component-starts-or-on-router-navigation)
- [275: How do you keep an error per entity, for example per row?](#275-how-do-you-keep-an-error-per-entity-for-example-per-row)
- [276: How would you model pagination state?](#276-how-would-you-model-pagination-state)
- [277: Where should filtering and sorting happen?](#277-where-should-filtering-and-sorting-happen)
- [278: How do you avoid fetching data that is already in the store?](#278-how-do-you-avoid-fetching-data-that-is-already-in-the-store)
- [279: How do you clear a feature's state when the user leaves the page?](#279-how-do-you-clear-a-features-state-when-the-user-leaves-the-page)
- [280: Can a component listen to `Actions` directly, for example to close a dialog on success?](#280-can-a-component-listen-to-actions-directly-for-example-to-close-a-dialog-on-success)
- [281: How do HTTP interceptors fit with NgRx effects?](#281-how-do-http-interceptors-fit-with-ngrx-effects)
- [282: How do you retry a failed request in an effect?](#282-how-do-you-retry-a-failed-request-in-an-effect)
- [283: How do you cancel a request when the user navigates away?](#283-how-do-you-cancel-a-request-when-the-user-navigates-away)
- [284: How do you handle a WebSocket with effects?](#284-how-do-you-handle-a-websocket-with-effects)
- [285: Can `createAction` take a function instead of `props`?](#285-can-createaction-take-a-function-instead-of-props)
- [286: Can `createActionGroup` events use creator functions too?](#286-can-createactiongroup-events-use-creator-functions-too)
- [287: Can you call `store.select` with a string key?](#287-can-you-call-storeselect-with-a-string-key)
- [288: What types do selectors have?](#288-what-types-do-selectors-have)
- [289: What makes a good state shape?](#289-what-makes-a-good-state-shape)
- [290: How would you add simple undo to a feature?](#290-how-would-you-add-simple-undo-to-a-feature)
- [291: How can one SignalStore use another SignalStore?](#291-how-can-one-signalstore-use-another-signalstore)
- [292: How do you call one store method from another?](#292-how-do-you-call-one-store-method-from-another)
- [293: Does the order of features in `signalStore` matter?](#293-does-the-order-of-features-in-signalstore-matter)
- [294: How would you move from ComponentStore to SignalStore?](#294-how-would-you-move-from-componentstore-to-signalstore)
- [295: How do you migrate an NgModule-based NgRx setup to standalone providers?](#295-how-do-you-migrate-an-ngmodule-based-ngrx-setup-to-standalone-providers)
- [296: How do you share selectors between the global store and a SignalStore?](#296-how-do-you-share-selectors-between-the-global-store-and-a-signalstore)
- [297: What should you check in a code review of an action file?](#297-what-should-you-check-in-a-code-review-of-an-action-file)
- [298: How do you keep a selector from re-running for big lists when only one item changes?](#298-how-do-you-keep-a-selector-from-re-running-for-big-lists-when-only-one-item-changes)
- [299: What's the difference between `setAll` / `setAllEntities` and `addMany` / `addEntities`?](#299-whats-the-difference-between-setall--setallentities-and-addmany--addentities)
- [300: How do you decide between NgRx Store, SignalStore, and a simple signal service for a new feature?](#300-how-do-you-decide-between-ngrx-store-signalstore-and-a-simple-signal-service-for-a-new-feature)

### Advanced Questions (301-450)

- [301: How does NgRx Store work internally?](#301-how-does-ngrx-store-work-internally)
- [302: Why does `State` use `observeOn(queueScheduler)`?](#302-why-does-state-use-observeonqueuescheduler)
- [303: Why do effects listen to `ScannedActionsSubject` and not `ActionsSubject`?](#303-why-do-effects-listen-to-scannedactionssubject-and-not-actionssubject)
- [304: How is `selectSignal` implemented?](#304-how-is-selectsignal-implemented)
- [305: How does `createSelector` memoization work in detail?](#305-how-does-createselector-memoization-work-in-detail)
- [306: How does `resultMemoize` differ from the default memoization?](#306-how-does-resultmemoize-differ-from-the-default-memoization)
- [307: How do `select`'s `distinctUntilChanged` and selector memoization work together?](#307-how-do-selects-distinctuntilchanged-and-selector-memoization-work-together)
- [308: How does `createActionGroup` build its types?](#308-how-does-createactiongroup-build-its-types)
- [309: Why does `createFeature` not allow optional properties at the root of the feature state?](#309-why-does-createfeature-not-allow-optional-properties-at-the-root-of-the-feature-state)
- [310: Why is `on-function-explicit-return-type` recommended?](#310-why-is-on-function-explicit-return-type-recommended)
- [311: How are `on` handlers combined when several handle the same action?](#311-how-are-on-handlers-combined-when-several-handle-the-same-action)
- [312: How does `combineReducers` handle features and what does `ActionReducerMap` mean?](#312-how-does-combinereducers-handle-features-and-what-does-actionreducermap-mean)
- [313: How do effects get registered and run internally?](#313-how-do-effects-get-registered-and-run-internally)
- [314: What is `OnRunEffects` used for?](#314-what-is-onruneffects-used-for)
- [315: What is `OnIdentifyEffects` for?](#315-what-is-onidentifyeffects-for)
- [316: What happens if you provide the same effects class in two lazy routes?](#316-what-happens-if-you-provide-the-same-effects-class-in-two-lazy-routes)
- [317: How do you handle errors in an effect without the default error handler?](#317-how-do-you-handle-errors-in-an-effect-without-the-default-error-handler)
- [318: What can cause memory leaks in effects?](#318-what-can-cause-memory-leaks-in-effects)
- [319: How do you deal with race conditions when the same action is handled with different ids?](#319-how-do-you-deal-with-race-conditions-when-the-same-action-is-handled-with-different-ids)
- [320: How do you test effects with marble diagrams?](#320-how-do-you-test-effects-with-marble-diagrams)
- [321: How do you test a debounced effect with `TestScheduler`?](#321-how-do-you-test-a-debounced-effect-with-testscheduler)
- [322: How would you test that `exhaustMap` ignores clicks while a request runs?](#322-how-would-you-test-that-exhaustmap-ignores-clicks-while-a-request-runs)
- [323: Do runtime checks affect production performance?](#323-do-runtime-checks-affect-production-performance)
- [324: What problems can `strictStateImmutability` cause with third-party libraries?](#324-what-problems-can-strictstateimmutability-cause-with-third-party-libraries)
- [325: How do you keep selectors fast in a store with a lot of state?](#325-how-do-you-keep-selectors-fast-in-a-store-with-a-lot-of-state)
- [326: How do you model relationships between entities?](#326-how-do-you-model-relationships-between-entities)
- [327: How do you put related data back together for the UI?](#327-how-do-you-put-related-data-back-together-for-the-ui)
- [328: How do you handle many-to-many relationships?](#328-how-do-you-handle-many-to-many-relationships)
- [329: How do you memoize a factory selector per id?](#329-how-do-you-memoize-a-factory-selector-per-id)
- [330: How would you design state for a list with virtual scrolling and lazy loaded pages?](#330-how-would-you-design-state-for-a-list-with-virtual-scrolling-and-lazy-loaded-pages)
- [331: Why should you avoid calling functions in templates that compute from store data?](#331-why-should-you-avoid-calling-functions-in-templates-that-compute-from-store-data)
- [332: What are batch actions and when are they useful?](#332-what-are-batch-actions-and-when-are-they-useful)
- [333: How is NgRx related to event sourcing?](#333-how-is-ngrx-related-to-event-sourcing)
- [334: Show a more complete undo/redo meta-reducer.](#334-show-a-more-complete-undoredo-meta-reducer)
- [335: How do you sync state between browser tabs?](#335-how-do-you-sync-state-between-browser-tabs)
- [336: How do you transfer NgRx Store state from server to client with `TransferState`?](#336-how-do-you-transfer-ngrx-store-state-from-server-to-client-with-transferstate)
- [337: How would you share NgRx state between micro-frontends?](#337-how-would-you-share-ngrx-state-between-micro-frontends)
- [338: Can an app have more than one global `Store`?](#338-can-an-app-have-more-than-one-global-store)
- [339: How does `provideState` work with lazy loaded routes behind the scenes?](#339-how-does-providestate-work-with-lazy-loaded-routes-behind-the-scenes)
- [340: In what order should you register `provideState` and `provideEffects` for a lazy feature?](#340-in-what-order-should-you-register-providestate-and-provideeffects-for-a-lazy-feature)
- [341: How do `provideStore` and the other `provide*` functions work in DI?](#341-how-do-providestore-and-the-other-provide-functions-work-in-di)
- [342: How do you use NgRx inside an Angular library?](#342-how-do-you-use-ngrx-inside-an-angular-library)
- [343: How does `signalStore` build the store class?](#343-how-does-signalstore-build-the-store-class)
- [344: What is `STATE_SOURCE` and how does `patchState` use it?](#344-what-is-state_source-and-how-does-patchstate-use-it)
- [345: How are DeepSignals implemented?](#345-how-are-deepsignals-implemented)
- [346: Why are DeepSignals only created for plain objects?](#346-why-are-deepsignals-only-created-for-plain-objects)
- [347: How does protected state work at the type and runtime level?](#347-how-does-protected-state-work-at-the-type-and-runtime-level)
- [348: How do `getState` and `watchState` work?](#348-how-do-getstate-and-watchstate-work)
- [349: When should you use `watchState` and when `effect`?](#349-when-should-you-use-watchstate-and-when-effect)
- [350: Does SignalStore freeze state?](#350-does-signalstore-freeze-state)
- [351: How do you type a custom feature that needs state, props and methods from the host store?](#351-how-do-you-type-a-custom-feature-that-needs-state-props-and-methods-from-the-host-store)
- [352: How do you write a custom feature that takes a config, like `withEntities` does?](#352-how-do-you-write-a-custom-feature-that-takes-a-config-like-withentities-does)
- [353: How do you make a custom feature with a named collection prefix?](#353-how-do-you-make-a-custom-feature-with-a-named-collection-prefix)
- [354: How would you build an undo/redo feature for SignalStore?](#354-how-would-you-build-an-undoredo-feature-for-signalstore)
- [355: How would you build a feature that syncs SignalStore state to `localStorage`?](#355-how-would-you-build-a-feature-that-syncs-signalstore-state-to-localstorage)
- [356: Why does `withFeature` exist when `signalStoreFeature` already has inputs?](#356-why-does-withfeature-exist-when-signalstorefeature-already-has-inputs)
- [357: How does `withLinkedState` work with an explicit `linkedSignal`?](#357-how-does-withlinkedstate-work-with-an-explicit-linkedsignal)
- [358: What are the trade-offs of keeping a `resource` in SignalStore instead of state?](#358-what-are-the-trade-offs-of-keeping-a-resource-in-signalstore-instead-of-state)
- [359: What must you know about `rxMethod` lifetimes?](#359-what-must-you-know-about-rxmethod-lifetimes)
- [360: How do you call `rxMethod` outside an injection context with a signal?](#360-how-do-you-call-rxmethod-outside-an-injection-context-with-a-signal)
- [361: How do you keep an `rxMethod` alive after an error?](#361-how-do-you-keep-an-rxmethod-alive-after-an-error)
- [362: How do you choose the flattening operator inside `rxMethod`?](#362-how-do-you-choose-the-flattening-operator-inside-rxmethod)
- [363: When are Promise-based methods better than `rxMethod`, and when worse?](#363-when-are-promise-based-methods-better-than-rxmethod-and-when-worse)
- [364: What is the SignalStore events plugin?](#364-what-is-the-signalstore-events-plugin)
- [365: How do you define events with `eventGroup`?](#365-how-do-you-define-events-with-eventgroup)
- [366: How do you update state from events with `withReducer`?](#366-how-do-you-update-state-from-events-with-withreducer)
- [367: How do you handle side effects with `withEventHandlers`?](#367-how-do-you-handle-side-effects-with-witheventhandlers)
- [368: How do components dispatch events in a SignalStore setup?](#368-how-do-components-dispatch-events-in-a-signalstore-setup)
- [369: What are scoped events?](#369-what-are-scoped-events)
- [370: When should you use events instead of plain store methods?](#370-when-should-you-use-events-instead-of-plain-store-methods)
- [371: How do several stores react to the same event?](#371-how-do-several-stores-react-to-the-same-event)
- [372: How do you test a store that uses the events plugin?](#372-how-do-you-test-a-store-that-uses-the-events-plugin)
- [373: How would you handle two entity collections with custom ids in one SignalStore?](#373-how-would-you-handle-two-entity-collections-with-custom-ids-in-one-signalstore)
- [374: How do you update several entities by a condition in SignalStore?](#374-how-do-you-update-several-entities-by-a-condition-in-signalstore)
- [375: Should components read `entities()` or `entityMap()`?](#375-should-components-read-entities-or-entitymap)
- [376: What should you watch out for when using SignalStore with SSR?](#376-what-should-you-watch-out-for-when-using-signalstore-with-ssr)
- [377: How do you transfer SignalStore state from server to browser?](#377-how-do-you-transfer-signalstore-state-from-server-to-browser)
- [378: How long does a SignalStore provided in route `providers` live?](#378-how-long-does-a-signalstore-provided-in-route-providers-live)
- [379: Can you extend a SignalStore class?](#379-can-you-extend-a-signalstore-class)
- [380: How do you get the type of a SignalStore instance?](#380-how-do-you-get-the-type-of-a-signalstore-instance)
- [381: How do you mock a SignalStore when testing a component?](#381-how-do-you-mock-a-signalstore-when-testing-a-component)
- [382: How do you test a custom SignalStore feature by itself?](#382-how-do-you-test-a-custom-signalstore-feature-by-itself)
- [383: How do you test `onDestroy` hooks?](#383-how-do-you-test-ondestroy-hooks)
- [384: How do you combine the global Store and SignalStore in one architecture?](#384-how-do-you-combine-the-global-store-and-signalstore-in-one-architecture)
- [385: How would you migrate a feature from NgRx Store to SignalStore?](#385-how-would-you-migrate-a-feature-from-ngrx-store-to-signalstore)
- [386: What is the status of `@ngrx/data` and what should you use instead?](#386-what-is-the-status-of-ngrxdata-and-what-should-you-use-instead)
- [387: How would you organize NgRx code in an Nx monorepo?](#387-how-would-you-organize-ngrx-code-in-an-nx-monorepo)
- [388: How do you keep feature state ownership clear in a big team?](#388-how-do-you-keep-feature-state-ownership-clear-in-a-big-team)
- [389: How would you write a facade with signals that doesn't lose the event log?](#389-how-would-you-write-a-facade-with-signals-that-doesnt-lose-the-event-log)
- [390: What is "action ping-pong" and why is it a problem?](#390-what-is-action-ping-pong-and-why-is-it-a-problem)
- [391: How do you handle long-running multi-step workflows with effects?](#391-how-do-you-handle-long-running-multi-step-workflows-with-effects)
- [392: How would you build a multi-step wizard with SignalStore?](#392-how-would-you-build-a-multi-step-wizard-with-signalstore)
- [393: How would you queue writes while the user is offline?](#393-how-would-you-queue-writes-while-the-user-is-offline)
- [394: How would you write a WebSocket `rxMethod` that reconnects with backoff?](#394-how-would-you-write-a-websocket-rxmethod-that-reconnects-with-backoff)
- [395: How do you report errors from NgRx in one place?](#395-how-do-you-report-errors-from-ngrx-in-one-place)
- [396: How do you find performance problems in an NgRx app?](#396-how-do-you-find-performance-problems-in-an-ngrx-app)
- [397: Is `selectSignal` faster than `select` with the `async` pipe?](#397-is-selectsignal-faster-than-select-with-the-async-pipe)
- [398: How is `computed` over selector signals different from `combineLatest` over `select` observables?](#398-how-is-computed-over-selector-signals-different-from-combinelatest-over-select-observables)
- [399: What can you do when a selector is truly expensive?](#399-what-can-you-do-when-a-selector-is-truly-expensive)
- [400: What can cause high memory use from DevTools?](#400-what-can-cause-high-memory-use-from-devtools)
- [401: How expensive are immutable updates on large arrays?](#401-how-expensive-are-immutable-updates-on-large-arrays)
- [402: How do you type a meta-reducer that only reacts to some actions?](#402-how-do-you-type-a-meta-reducer-that-only-reacts-to-some-actions)
- [403: How do you enforce NgRx architecture rules automatically?](#403-how-do-you-enforce-ngrx-architecture-rules-automatically)
- [404: How do you sync a form with NgRx without putting every keystroke in the store?](#404-how-do-you-sync-a-form-with-ngrx-without-putting-every-keystroke-in-the-store)
- [405: How do you handle changes in the shape of persisted state between app versions?](#405-how-do-you-handle-changes-in-the-shape-of-persisted-state-between-app-versions)
- [406: How do you handle switching accounts or tenants in an NgRx app?](#406-how-do-you-handle-switching-accounts-or-tenants-in-an-ngrx-app)
- [407: How would you store feature flags with NgRx?](#407-how-would-you-store-feature-flags-with-ngrx)
- [408: What does "URL as the source of truth" mean in an NgRx app?](#408-what-does-url-as-the-source-of-truth-mean-in-an-ngrx-app)
- [409: Why does `selectRouteParam` sometimes return `undefined` with nested routes?](#409-why-does-selectrouteparam-sometimes-return-undefined-with-nested-routes)
- [410: An action is dispatched but the state doesn't change. How do you debug it?](#410-an-action-is-dispatched-but-the-state-doesnt-change-how-do-you-debug-it)
- [411: The state changes, but the component doesn't update. What do you check?](#411-the-state-changes-but-the-component-doesnt-update-what-do-you-check)
- [412: An effect runs twice for one action. What could be the cause?](#412-an-effect-runs-twice-for-one-action-what-could-be-the-cause)
- [413: How do you find and fix an infinite loop of actions?](#413-how-do-you-find-and-fix-an-infinite-loop-of-actions)
- [414: You get "Cannot assign to read only property" in development. What happened?](#414-you-get-cannot-assign-to-read-only-property-in-development-what-happened)
- [415: You call a SignalStore method and the UI doesn't update. Why?](#415-you-call-a-signalstore-method-and-the-ui-doesnt-update-why)
- [416: What happens if `patchState` sets a value to the same reference?](#416-what-happens-if-patchstate-sets-a-value-to-the-same-reference)
- [417: Why might `toSignal(store.select(...))` behave differently from `selectSignal`?](#417-why-might-tosignalstoreselect-behave-differently-from-selectsignal)
- [418: What steps do you follow to upgrade NgRx in a large app?](#418-what-steps-do-you-follow-to-upgrade-ngrx-in-a-large-app)
- [419: What API changes in recent NgRx versions should you know about?](#419-what-api-changes-in-recent-ngrx-versions-should-you-know-about)
- [420: How big is NgRx in the bundle and how do you keep it small?](#420-how-big-is-ngrx-in-the-bundle-and-how-do-you-keep-it-small)
- [421: How do you use the Store in a functional HTTP interceptor?](#421-how-do-you-use-the-store-in-a-functional-http-interceptor)
- [422: Why can injecting the Store in an interceptor cause a circular dependency, and how do you avoid it?](#422-why-can-injecting-the-store-in-an-interceptor-cause-a-circular-dependency-and-how-do-you-avoid-it)
- [423: Why shouldn't services called from effects dispatch actions themselves?](#423-why-shouldnt-services-called-from-effects-dispatch-actions-themselves)
- [424: How would you design state for a real-time collaborative feature, like a shared board?](#424-how-would-you-design-state-for-a-real-time-collaborative-feature-like-a-shared-board)
- [425: How do you handle conflicts when two users edit the same record?](#425-how-do-you-handle-conflicts-when-two-users-edit-the-same-record)
- [426: How would you cache results per query?](#426-how-would-you-cache-results-per-query)
- [427: How do you implement stale-while-revalidate with NgRx?](#427-how-do-you-implement-stale-while-revalidate-with-ngrx)
- [428: Where should you normalize API responses, in the effect or the reducer?](#428-where-should-you-normalize-api-responses-in-the-effect-or-the-reducer)
- [429: How do you handle token refresh with NgRx?](#429-how-do-you-handle-token-refresh-with-ngrx)
- [430: What is a good global error handling strategy with NgRx?](#430-what-is-a-good-global-error-handling-strategy-with-ngrx)
- [431: How do you show one global loading bar for many parallel requests?](#431-how-do-you-show-one-global-loading-bar-for-many-parallel-requests)
- [432: How would you write a generic CRUD feature for SignalStore?](#432-how-would-you-write-a-generic-crud-feature-for-signalstore)
- [433: How do you avoid duplicate requests when several components ask for the same data?](#433-how-do-you-avoid-duplicate-requests-when-several-components-ask-for-the-same-data)
- [434: How do parent and child SignalStores talk to each other?](#434-how-do-parent-and-child-signalstores-talk-to-each-other)
- [435: What happens if a component that provides a store also injects a parent's store of the same class?](#435-what-happens-if-a-component-that-provides-a-store-also-injects-a-parents-store-of-the-same-class)
- [436: How do you stop polling or socket effects from running during SSR?](#436-how-do-you-stop-polling-or-socket-effects-from-running-during-ssr)
- [437: How do `@defer` blocks and incremental hydration affect NgRx?](#437-how-do-defer-blocks-and-incremental-hydration-affect-ngrx)
- [438: How do you test code that uses Angular `effect` or `watchState` in a SignalStore?](#438-how-do-you-test-code-that-uses-angular-effect-or-watchstate-in-a-signalstore)
- [439: How do you test a component with signal inputs that uses a selector based on the input?](#439-how-do-you-test-a-component-with-signal-inputs-that-uses-a-selector-based-on-the-input)
- [440: Is it OK to create a SignalStore for every row in a big list?](#440-is-it-ok-to-create-a-signalstore-for-every-row-in-a-big-list)
- [441: How would you explain the trade-offs of NgRx Store to a team that says it's too much boilerplate?](#441-how-would-you-explain-the-trade-offs-of-ngrx-store-to-a-team-that-says-its-too-much-boilerplate)
- [442: What do you look for when reviewing NgRx code?](#442-what-do-you-look-for-when-reviewing-ngrx-code)
- [443: What are common NgRx anti-patterns?](#443-what-are-common-ngrx-anti-patterns)
- [444: How would you structure state for a large enterprise Angular app?](#444-how-would-you-structure-state-for-a-large-enterprise-angular-app)
- [445: How would you bring NgRx into an existing app that uses services with `BehaviorSubject`s?](#445-how-would-you-bring-ngrx-into-an-existing-app-that-uses-services-with-behaviorsubjects)
- [446: How do you decide what goes into SignalStore state vs `withProps`?](#446-how-do-you-decide-what-goes-into-signalstore-state-vs-withprops)
- [447: What does `withComputed` with private members let you do in custom features?](#447-what-does-withcomputed-with-private-members-let-you-do-in-custom-features)
- [448: How do you keep event handlers in SignalStore from reacting to events meant for other instances?](#448-how-do-you-keep-event-handlers-in-signalstore-from-reacting-to-events-meant-for-other-instances)
- [449: How do you keep NgRx code easy to change over time?](#449-how-do-you-keep-ngrx-code-easy-to-change-over-time)
- [450: What direction has NgRx taken in recent versions, and how does that affect new projects?](#450-what-direction-has-ngrx-taken-in-recent-versions-and-how-does-that-affect-new-projects)

---

## Easy Questions

### 1: What is NgRx?

NgRx is a set of libraries for managing state in Angular applications. It started as a Redux-style store built on RxJS and now also includes SignalStore, which is built on Angular signals.

The main idea is that application state lives in one predictable place, changes only in known ways, and components read it instead of keeping their own copies.

### 2: What problem does NgRx solve?

In a bigger Angular app, many components need the same data (current user, cart, settings, lists loaded from the API). Without a clear pattern, each service and component keeps its own copy, data goes out of sync, and it gets hard to tell who changed what.

NgRx solves this by:

- Keeping shared state in one place.
- Making every change go through a described event (an action) or a store method.
- Moving side effects like HTTP calls out of components.
- Giving you good debugging tools (Redux DevTools, action history, time travel).

### 3: What are the main packages in NgRx?

- `@ngrx/store` - the global Redux-style store (actions, reducers, selectors).
- `@ngrx/effects` - side effects for the global store.
- `@ngrx/signals` - SignalStore, signalState, entity helpers, rxMethod, events plugin.
- `@ngrx/entity` - entity adapter for collections in the global store.
- `@ngrx/router-store` - connects Angular Router state to the store.
- `@ngrx/store-devtools` - Redux DevTools integration.
- `@ngrx/operators` - RxJS helpers like `tapResponse`, `mapResponse` and `concatLatestFrom`.
- `@ngrx/component` - `ngrxPush` pipe and `*ngrxLet` directive.
- `@ngrx/component-store` - local store based on RxJS (still supported, but SignalStore is the recommended choice for new code).
- `@ngrx/schematics` - code generators for the Angular CLI.
- `@ngrx/eslint-plugin` - lint rules for NgRx code.
- `@ngrx/data` - entity data management on top of store and effects (in maintenance mode).

### 4: What is the Redux pattern?

Redux is a pattern where:

1. The whole state is kept in a single store.
2. You change state by dispatching an action (a plain object that describes what happened).
3. A reducer, which is a pure function, takes the current state and the action and returns a new state.
4. The view reads state and re-renders when it changes.

NgRx Store follows this pattern and uses RxJS observables and Angular signals to deliver state to components.

### 5: What are the core principles behind NgRx Store?

- **Single source of truth**: global state lives in one store.
- **State is read-only**: you never change it directly. You dispatch actions.
- **Changes are made with pure functions**: reducers take old state and an action and return new state without side effects.

### 6: What is the Store?

`Store` is an injectable service from `@ngrx/store`. It holds the current state and lets you:

- Dispatch actions with `store.dispatch(action)`.
- Read state with `store.select(selector)` (returns an observable) or `store.selectSignal(selector)` (returns a signal).

```ts
import { Component, inject } from "@angular/core";
import { Store } from "@ngrx/store";

@Component({/* ... */})
export class BooksPage {
  private readonly store = inject(Store);
  readonly books = this.store.selectSignal(selectBooks);
}
```

### 7: What is an action?

An action is a plain object that describes something that happened in the app. It must have a `type` string and can carry extra data.

```ts
{ type: '[Books Page] Search', query: 'angular' }
```

You normally don't write these objects by hand. You use action creators like `createAction` or `createActionGroup`.

### 8: What is a reducer?

A reducer is a pure function that takes the current state and an action and returns the next state. In NgRx you build reducers with `createReducer` and `on`.

```ts
import { createReducer, on } from "@ngrx/store";

export interface CounterState {
  count: number;
}

const initialState: CounterState = { count: 0 };

export const counterReducer = createReducer(
  initialState,
  on(CounterActions.increment, (state) => ({
    ...state,
    count: state.count + 1,
  })),
  on(CounterActions.reset, () => initialState),
);
```

### 9: What is a selector?

A selector is a pure function that reads a piece of state, or computes something from it. Selectors are created with `createSelector` and `createFeatureSelector`, and they are memoized, so the result is reused when the inputs don't change.

```ts
export const selectCounterState =
  createFeatureSelector<CounterState>("counter");

export const selectCount = createSelector(
  selectCounterState,
  (state) => state.count,
);
```

### 10: What is an effect?

An effect is a place for side effects like HTTP requests, local storage access, navigation, or websockets. Effects listen to the stream of dispatched actions, do some work, and usually dispatch a new action with the result.

This keeps components and reducers free from async logic.

### 11: How do you install NgRx?

The easiest way is with `ng add`, which installs the package and updates your app config:

```bash
ng add @ngrx/store@latest
ng add @ngrx/effects@latest
ng add @ngrx/store-devtools@latest
ng add @ngrx/signals@latest
```

You can also use npm directly:

```bash
npm install @ngrx/store @ngrx/effects @ngrx/signals
```

With plain npm you have to add the providers yourself.

### 12: What does `ng add @ngrx/store` do?

It installs `@ngrx/store` with a version that matches your Angular version and adds `provideStore()` to your application providers (for a standalone app) or `StoreModule.forRoot({})` (for an NgModule app). It can also create a starting state setup if you pass options like `--state-path`.

### 13: How do you register the store in a standalone Angular app?

Use `provideStore` in `app.config.ts`:

```ts
import { ApplicationConfig, isDevMode } from "@angular/core";
import { provideStore } from "@ngrx/store";
import { provideEffects } from "@ngrx/effects";
import { provideStoreDevtools } from "@ngrx/store-devtools";

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore(),
    provideEffects(),
    provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() }),
  ],
};
```

You can pass root reducers to `provideStore({ router: routerReducer })` if you have some.

### 14: What is `provideState`?

`provideState` registers a feature state (a slice of the global state) with its reducer. You can use it in the app config or in route providers for lazy loading.

```ts
provideState(booksFeature);
// or
provideState("books", booksReducer);
```

### 15: How do you create an action with `createAction`?

```ts
import { createAction, props } from "@ngrx/store";

export const loadBooks = createAction("[Books Page] Load Books");

export const searchBooks = createAction(
  "[Books Page] Search Books",
  props<{ query: string }>(),
);

// usage
store.dispatch(searchBooks({ query: "ngrx" }));
```

`createAction` returns a function that creates the action object and also has a `type` property you can use in reducers and effects.

### 16: What is `props<>()`?

`props` defines the shape of the extra data an action carries. It is only used for typing.

```ts
export const bookSelected = createAction(
  "[Books Page] Book Selected",
  props<{ bookId: string }>(),
);

bookSelected({ bookId: "42" }); // { type: '[Books Page] Book Selected', bookId: '42' }
```

### 17: What is `emptyProps()`?

`emptyProps()` is used in `createActionGroup` for events that have no payload.

```ts
export const BooksPageActions = createActionGroup({
  source: "Books Page",
  events: {
    Opened: emptyProps(),
    "Query Changed": props<{ query: string }>(),
  },
});
```

### 18: What is `createActionGroup`?

`createActionGroup` creates several action creators that share the same source. It cuts down on repeated code.

```ts
import { createActionGroup, emptyProps, props } from "@ngrx/store";

export const BooksApiActions = createActionGroup({
  source: "Books API",
  events: {
    "Load Success": props<{ books: Book[] }>(),
    "Load Failure": props<{ error: string }>(),
    "Clear Cache": emptyProps(),
  },
});

BooksApiActions.loadSuccess({ books });
// type: '[Books API] Load Success'
```

### 19: How are event names turned into function names in `createActionGroup`?

The event name is converted to camel case. `'Load Success'` becomes `loadSuccess`, and `'Clear Cache'` becomes `clearCache`. The action type is built as `[Source] Event Name`, so `'[Books API] Load Success'`.

TypeScript knows these names at compile time, so you get autocomplete and errors if you use a wrong name.

### 20: What is the `[Source] Event` naming convention?

Action types are written as `[Where it happened] What happened`, for example `[Login Page] Submit` or `[Auth API] Login Success`. This makes the action log in DevTools easy to read, because you can see where each action came from. `createActionGroup` follows this format automatically.

### 21: Why should every action type be unique?

Reducers and effects match on the `type` string. If two different actions have the same type, a reducer or effect may react to the wrong one. There is a runtime check called `strictActionTypeUniqueness` that can warn you about duplicates.

### 22: What is "good action hygiene"?

It means writing actions as unique events instead of reusing a generic action in many places. For example, instead of dispatching `loadBooks` from three places, you dispatch `[Books Page] Opened`, `[Search Page] Opened` and `[Books Refresh Button] Clicked`.

Benefits:

- The action log tells you exactly what happened and where.
- Each event can be handled differently later if needed.
- Debugging is easier.

### 23: How do you dispatch an action?

Inject `Store` and call `dispatch`:

```ts
export class BooksPage {
  private readonly store = inject(Store);

  search(query: string) {
    this.store.dispatch(BooksPageActions.queryChanged({ query }));
  }
}
```

### 24: Can you dispatch an action from a template?

Not directly, because the template can't call `store.dispatch` unless you expose the store. The normal way is to call a component method from the template, and the method dispatches the action:

```html
<button (click)="refresh()">Refresh</button>
```

```ts
refresh() {
  this.store.dispatch(BooksPageActions.refreshClicked());
}
```

### 25: What does `createReducer` do?

`createReducer` builds a reducer function from an initial state and a list of `on` handlers. Each `on` connects one or more action creators to a state change function.

```ts
export const booksReducer = createReducer(
  initialState,
  on(BooksPageActions.opened, (state) => ({ ...state, loading: true })),
  on(BooksApiActions.loadSuccess, (state, { books }) => ({
    ...state,
    books,
    loading: false,
  })),
);
```

### 26: What is the `on()` function?

`on` is used inside `createReducer`. It takes one or more action creators and a function that returns the new state. The second argument of that function is the action, already typed, so you can destructure its props.

```ts
on(BooksApiActions.loadFailure, (state, { error }) => ({
  ...state,
  error,
  loading: false,
}));
```

### 27: Why must reducers be pure functions?

A pure function always returns the same output for the same input and has no side effects. This matters because:

- State changes become predictable and easy to test.
- Time travel debugging in DevTools works by replaying actions through reducers.
- Change detection can rely on reference checks.

So inside a reducer you should not make HTTP calls, read `Date.now()`, use `Math.random()`, or change the existing state object.

### 28: How do you return a new state without mutating the old one?

Use the spread operator and array methods that return new arrays:

```ts
(on(TodoActions.added, (state, { todo }) => ({
  ...state,
  todos: [...state.todos, todo],
})),
  on(TodoActions.removed, (state, { id }) => ({
    ...state,
    todos: state.todos.filter((t) => t.id !== id),
  })),
  on(TodoActions.toggled, (state, { id }) => ({
    ...state,
    todos: state.todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
  })));
```

Avoid `push`, `splice`, `sort` (on the original array) and direct assignment like `state.count++`.

### 29: What is initial state?

Initial state is the value a slice of state has before any action has changed it. You pass it as the first argument of `createReducer`.

```ts
export interface BooksState {
  books: Book[];
  loading: boolean;
  error: string | null;
}

export const initialState: BooksState = {
  books: [],
  loading: false,
  error: null,
};
```

### 30: Can one `on()` handle several actions?

Yes. Pass several action creators before the handler:

```ts
on(BooksPageActions.opened, BooksPageActions.refreshClicked, (state) => ({
  ...state,
  loading: true,
}));
```

The action type in the handler becomes a union of those actions.

### 31: What happens to actions a reducer doesn't handle?

The reducer returns the current state unchanged. `createReducer` does this for you. Every action goes through every registered reducer, but only the matching `on` handlers do anything.

### 32: What is `createFeature`?

`createFeature` takes a feature name and a reducer, and gives you back the name, the reducer, and selectors for every top-level property in the state. It removes a lot of selector boilerplate.

```ts
export const booksFeature = createFeature({
  name: "books",
  reducer: createReducer(
    initialState,
    on(BooksApiActions.loadSuccess, (state, { books }) => ({
      ...state,
      books,
    })),
  ),
});

export const { selectBooks, selectLoading, selectError, selectBooksState } =
  booksFeature;
```

Register it with `provideState(booksFeature)`.

### 33: Which selectors does `createFeature` create for you?

- One feature selector named `select{FeatureName}State`, for example `selectBooksState`.
- One selector for each top-level property of the state, for example `selectBooks`, `selectLoading`, `selectError`.

You can add your own derived selectors with the `extraSelectors` option.

### 34: What is `createFeatureSelector`?

It creates a selector that returns a whole feature slice of the state by its key.

```ts
export const selectBooksState = createFeatureSelector<BooksState>("books");
```

If you use `createFeature`, you don't need to write this yourself.

### 35: What is `createSelector`?

`createSelector` builds a selector from one or more input selectors and a projector function. The projector gets the results of the input selectors.

```ts
export const selectBooks = createSelector(selectBooksState, (s) => s.books);
export const selectQuery = createSelector(selectBooksState, (s) => s.query);

export const selectFilteredBooks = createSelector(
  selectBooks,
  selectQuery,
  (books, query) =>
    books.filter((b) => b.title.toLowerCase().includes(query.toLowerCase())),
);
```

### 36: How do you read state in a component using `store.select`?

`store.select` returns an observable. You can use it with the `async` pipe:

```ts
export class BooksPage {
  private readonly store = inject(Store);
  readonly books$ = this.store.select(selectBooks);
}
```

```html
@for (book of books$ | async; track book.id) {
<app-book-card [book]="book" />
}
```

### 37: What is `store.selectSignal`?

`selectSignal` returns an Angular signal instead of an observable. It is the most common way to read store state in modern Angular code.

```ts
export class BooksPage {
  private readonly store = inject(Store);
  readonly books = this.store.selectSignal(selectBooks);
  readonly loading = this.store.selectSignal(selectLoading);
}
```

```html
@if (loading()) {
<app-spinner />
} @for (book of books(); track book.id) {
<app-book-card [book]="book" />
}
```

### 38: What is the difference between `select` and `selectSignal`?

- `select` returns an `Observable`. You need the `async` pipe or a subscription to read it. It's useful when you want to combine the value with other RxJS operators.
- `selectSignal` returns a read-only `Signal`. You read it by calling it, no subscriptions needed, and it works well with `computed`, `effect`, OnPush and zoneless change detection.

### 39: Why use selectors instead of reading state directly?

- Components don't need to know the shape of the state, so you can change the state structure in one place.
- Selectors are memoized, so heavy calculations don't run again unless inputs change.
- Selectors are easy to reuse and combine.
- Selectors are pure functions, so they are easy to test.

### 40: What is memoization in selectors?

Memoization means the selector remembers its last inputs and last result. If the inputs are the same (by reference) the next time it runs, it returns the saved result without running the projector again.

This saves work, and it also means the selector returns the same object reference, so the UI doesn't re-render for no reason.

### 41: How many input selectors can `createSelector` take?

The typed overloads support up to eight input selectors in array form plus the projector. You can also pass a dictionary of selectors:

```ts
export const selectBooksViewModel = createSelector({
  books: selectFilteredBooks,
  loading: selectLoading,
  error: selectError,
});
// returns { books, loading, error }
```

If you need more inputs, it usually means you should split the selector into smaller ones.

### 42: What is a projector function?

It's the last function you pass to `createSelector`. It receives the results of the input selectors and returns the computed value. Every memoized selector exposes it as `selector.projector`, which is handy in unit tests.

```ts
const result = selectFilteredBooks.projector(books, "angular");
```

### 43: How do you use a selected signal in a template?

Call it like a function:

```ts
readonly user = this.store.selectSignal(selectCurrentUser);
```

```html
@if (user(); as user) {
<p>Hello {{ user.name }}</p>
}
```

### 44: How do you use `store.select` with the `async` pipe?

```ts
readonly count$ = this.store.select(selectCount);
```

```html
<p>Count: {{ count$ | async }}</p>
```

The `async` pipe subscribes when the view is created and unsubscribes when it's destroyed, so you don't leak subscriptions.

### 45: What is `@ngrx/effects`?

It's the package that handles side effects for the global store. It gives you the `Actions` stream, the `ofType` operator, `createEffect`, and `provideEffects`. Effects take actions in and send actions out.

### 46: What is the `Actions` stream?

`Actions` is an injectable observable that emits every action dispatched to the store, after the reducers have handled it. Effects inject it and filter it with `ofType`.

```ts
const actions$ = inject(Actions);
```

### 47: What is `ofType`?

`ofType` is an RxJS operator that filters the actions stream by action creator. It also narrows the action type, so the next operator knows the action's props.

```ts
actions$.pipe(
  ofType(BooksPageActions.queryChanged),
  map(({ query }) => query),
);
```

### 48: How do you write a class-based effect?

```ts
import { Injectable, inject } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { catchError, exhaustMap, map, of } from "rxjs";

@Injectable()
export class BooksEffects {
  private readonly actions$ = inject(Actions);
  private readonly booksService = inject(BooksService);

  loadBooks$ = createEffect(() =>
    this.actions$.pipe(
      ofType(BooksPageActions.opened),
      exhaustMap(() =>
        this.booksService.getAll().pipe(
          map((books) => BooksApiActions.loadSuccess({ books })),
          catchError((error: { message: string }) =>
            of(BooksApiActions.loadFailure({ error: error.message })),
          ),
        ),
      ),
    ),
  );
}
```

Register it with `provideEffects(BooksEffects)`.

### 49: How do you write a functional effect?

A functional effect is a constant created with `createEffect` and `{ functional: true }`. Dependencies are injected as default parameter values.

```ts
export const loadBooks = createEffect(
  (actions$ = inject(Actions), booksService = inject(BooksService)) =>
    actions$.pipe(
      ofType(BooksPageActions.opened),
      exhaustMap(() =>
        booksService.getAll().pipe(
          map((books) => BooksApiActions.loadSuccess({ books })),
          catchError((error: { message: string }) =>
            of(BooksApiActions.loadFailure({ error: error.message })),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

Register all functional effects from a file at once:

```ts
import * as booksEffects from "./books.effects";

provideEffects(booksEffects);
```

### 50: How do you register effects with `provideEffects`?

Pass effect classes and/or objects that hold functional effects:

```ts
providers: [provideStore(), provideEffects(AuthEffects, routerEffects)];
```

For a lazy feature, use it inside route providers:

```ts
{
  path: 'books',
  loadComponent: () => import('./books-page'),
  providers: [provideState(booksFeature), provideEffects(booksEffects)],
}
```

### 51: What does `{ dispatch: false }` mean in an effect?

By default NgRx dispatches whatever the effect emits, so it must emit actions. If the effect only does something on the side (logging, navigation, showing a toast) and doesn't return an action, set `dispatch: false`.

```ts
export const showError = createEffect(
  (actions$ = inject(Actions), snackBar = inject(MatSnackBar)) =>
    actions$.pipe(
      ofType(BooksApiActions.loadFailure),
      tap(({ error }) => snackBar.open(error, "Close")),
    ),
  { functional: true, dispatch: false },
);
```

### 52: What happens if an effect with default config emits something that isn't an action?

NgRx reports an error, because it tries to dispatch the emitted value and it isn't a valid action (no `type`). Either map to an action or set `dispatch: false`.

### 53: What is a side effect in the context of NgRx?

Anything that reaches outside the pure state update: HTTP calls, timers, reading or writing local storage, navigating, logging to a server, opening dialogs, using websockets. These belong in effects (or in SignalStore methods), not in reducers or selectors.

### 54: Can you show a simple effect that loads data with `HttpClient`?

```ts
@Injectable({ providedIn: "root" })
export class BooksService {
  private readonly http = inject(HttpClient);
  getAll() {
    return this.http.get<Book[]>("/api/books");
  }
}

export const loadBooks = createEffect(
  (actions$ = inject(Actions), api = inject(BooksService)) =>
    actions$.pipe(
      ofType(BooksPageActions.opened),
      switchMap(() =>
        api.getAll().pipe(
          map((books) => BooksApiActions.loadSuccess({ books })),
          catchError(() =>
            of(BooksApiActions.loadFailure({ error: "Could not load books" })),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

### 55: How do you handle errors in an effect?

Put `catchError` on the inner observable (the HTTP call) and return a failure action:

```ts
switchMap(() =>
  api.getAll().pipe(
    map((books) => BooksApiActions.loadSuccess({ books })),
    catchError((err) =>
      of(BooksApiActions.loadFailure({ error: err.message })),
    ),
  ),
);
```

### 56: Why should `catchError` be inside the inner observable and not on the outer stream?

If an error reaches the outer `actions$` stream, that stream completes. `catchError` on the outside replaces the stream with whatever you return, so the effect stops listening for new actions.

NgRx does have a default error handler that resubscribes effects after errors (up to 10 times), but you shouldn't depend on it. Catching errors in the inner observable keeps the effect alive and turns errors into normal failure actions.

### 57: What is `@ngrx/store-devtools`?

It connects the store to the Redux DevTools browser extension. You can see every dispatched action, the state after each action, the diff, and you can jump back to earlier states.

### 58: How do you set up Store DevTools?

```ts
import { isDevMode } from "@angular/core";
import { provideStoreDevtools } from "@ngrx/store-devtools";

providers: [
  provideStore(),
  provideStoreDevtools({
    maxAge: 25,
    logOnly: !isDevMode(),
    autoPause: true,
  }),
];
```

Then install the Redux DevTools extension in your browser.

### 59: What does the `maxAge` option do?

`maxAge` limits how many actions DevTools keeps in its history. Older ones are dropped. A small number like 25 keeps memory usage low. It must be greater than 1 if set.

### 60: What does the `logOnly` option do?

With `logOnly: true`, DevTools only shows actions and state. Features like dispatching actions from the extension, skipping actions, and time travel are turned off. It's common to set `logOnly: !isDevMode()` so production builds are safer.

### 61: What is time-travel debugging?

Because state is only changed by actions going through pure reducers, DevTools can replay or skip actions and show what the state was at any point. You can click an earlier action and the app UI shows the state from that moment. This helps when you are trying to see which action broke something.

### 62: What is `@ngrx/entity`?

`@ngrx/entity` helps you manage collections of records (users, products, orders) in the global store. It stores data in a normalized format and gives you an adapter with ready-made methods for adding, updating and removing items, plus selectors.

### 63: What is `EntityState`?

`EntityState<T>` is the shape used by the entity adapter:

```ts
interface EntityState<T> {
  ids: string[] | number[];
  entities: { [id: string]: T | undefined };
}
```

`ids` keeps the order, and `entities` is a lookup map by id. You extend it with your own fields:

```ts
export interface BooksState extends EntityState<Book> {
  selectedBookId: string | null;
  loading: boolean;
}
```

### 64: What is `createEntityAdapter`?

It creates an adapter object for one entity type:

```ts
import { createEntityAdapter, EntityAdapter } from "@ngrx/entity";

export const booksAdapter: EntityAdapter<Book> = createEntityAdapter<Book>();
```

The adapter gives you `getInitialState`, state change methods (`addOne`, `setAll`, `updateOne`, ...), and `getSelectors`.

### 65: What does `getInitialState` do?

It returns an empty entity state (`{ ids: [], entities: {} }`) merged with any extra fields you pass:

```ts
export const initialState: BooksState = booksAdapter.getInitialState({
  selectedBookId: null,
  loading: false,
});
```

### 66: Name some entity adapter methods.

- `addOne`, `addMany` - add if not already there.
- `setOne`, `setMany` - add or fully replace.
- `setAll` - replace the whole collection.
- `updateOne`, `updateMany` - partial update by id.
- `upsertOne`, `upsertMany` - add or partially update.
- `mapOne`, `map` - update using a function.
- `removeOne`, `removeMany`, `removeAll`.

Each one takes the current state as the last argument and returns new state:

```ts
on(BooksApiActions.loadSuccess, (state, { books }) =>
  booksAdapter.setAll(books, { ...state, loading: false }),
);
```

### 67: What is the difference between `addOne` and `setOne`?

- `addOne` adds the entity only if its id doesn't exist yet. If it exists, nothing changes.
- `setOne` adds the entity, or replaces the existing one completely if the id already exists.

### 68: What does `getSelectors` return?

It returns four selectors:

- `selectIds` - the array of ids.
- `selectEntities` - the dictionary of entities.
- `selectAll` - an array of all entities in order.
- `selectTotal` - the number of entities.

```ts
const { selectAll, selectEntities, selectTotal } = booksAdapter.getSelectors();
```

If you pass a feature selector, `getSelectors(selectBooksState)`, they work directly on the root state.

### 69: What is the `selectId` option in `createEntityAdapter`?

By default the adapter uses the `id` property. If your model uses a different key, give a `selectId` function:

```ts
export const adapter = createEntityAdapter<Country>({
  selectId: (country) => country.code,
});
```

### 70: What is the `sortComparer` option?

`sortComparer` keeps the `ids` array sorted every time the collection changes:

```ts
export const adapter = createEntityAdapter<Book>({
  sortComparer: (a, b) => a.title.localeCompare(b.title),
});
```

If you don't need sorting, leave it out (or set it to `false`), since sorting on every change costs time.

### 71: What is `@ngrx/router-store`?

It connects the Angular Router to the store. It puts the current router state (url, params, query params, data) into the store and dispatches actions on navigation. Then you can read route params with selectors, and effects can react to navigation.

### 72: How do you set up router-store?

```ts
import { provideRouterStore, routerReducer } from "@ngrx/router-store";

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideStore({ router: routerReducer }),
    provideRouterStore(),
  ],
};
```

The key `router` is the default name the router selectors look for.

### 73: What is `getRouterSelectors`?

It returns ready-made selectors for router state:

```ts
import { getRouterSelectors } from "@ngrx/router-store";

export const {
  selectCurrentRoute,
  selectQueryParams,
  selectQueryParam,
  selectRouteParams,
  selectRouteParam,
  selectRouteData,
  selectUrl,
  selectTitle,
  selectFragment,
} = getRouterSelectors();

export const selectBookId = selectRouteParam("bookId");
```

### 74: What is `@ngrx/signals`?

It's the NgRx package for state management built on Angular signals. It includes:

- `signalStore` and its features (`withState`, `withComputed`, `withMethods`, `withHooks`, `withProps`, ...).
- `signalState` for simple state objects.
- `patchState`, `getState`, `watchState`.
- Entity support in `@ngrx/signals/entities`.
- `rxMethod` in `@ngrx/signals/rxjs-interop`.
- The events plugin in `@ngrx/signals/events`.

It doesn't depend on `@ngrx/store`, so you can use it alone.

### 75: What is NgRx SignalStore?

SignalStore is a store built from signals. You compose it from small features and it gives you an injectable class with state signals, computed signals and methods.

```ts
import {
  signalStore,
  withState,
  withComputed,
  withMethods,
  patchState,
} from "@ngrx/signals";
import { computed } from "@angular/core";

export const CounterStore = signalStore(
  withState({ count: 0 }),
  withComputed(({ count }) => ({
    double: computed(() => count() * 2),
  })),
  withMethods((store) => ({
    increment() {
      patchState(store, (s) => ({ count: s.count + 1 }));
    },
  })),
);
```

It has much less boilerplate than the action/reducer/effect setup and works well for both feature state and component state.

### 76: What does the `signalStore()` function return?

It returns a class (an injectable service). You can provide it like any Angular service and inject it in components. You don't call `new` on it yourself, Angular DI creates the instance.

```ts
export const BooksStore = signalStore(withState({ books: [] as Book[] }));

@Component({
  providers: [BooksStore],
})
export class BooksPage {
  readonly store = inject(BooksStore);
}
```

### 77: What does `withState` do?

`withState` adds state to a SignalStore. Each top-level property becomes a signal on the store. Nested objects become deep signals, so you can read nested properties as signals too.

```ts
type BooksState = {
  books: Book[];
  isLoading: boolean;
  filter: { query: string; order: "asc" | "desc" };
};

const initialState: BooksState = {
  books: [],
  isLoading: false,
  filter: { query: "", order: "asc" },
};

export const BooksStore = signalStore(withState(initialState));

// store.books(), store.isLoading(), store.filter(), store.filter.query()
```

### 78: What does `withComputed` do?

It adds derived signals to the store. The factory gets the store members defined before it.

```ts
withComputed(({ books, filter }) => ({
  booksCount: computed(() => books().length),
  sortedBooks: computed(() => {
    const dir = filter.order() === "asc" ? 1 : -1;
    return [...books()].sort((a, b) => dir * a.title.localeCompare(b.title));
  }),
}));
```

### 79: What does `withMethods` do?

It adds methods to the store. This is where you update state and do async work. The factory runs in an injection context, so you can use `inject()`.

```ts
withMethods((store, booksService = inject(BooksService)) => ({
  updateQuery(query: string): void {
    patchState(store, (state) => ({ filter: { ...state.filter, query } }));
  },
  async loadAll(): Promise<void> {
    patchState(store, { isLoading: true });
    const books = await booksService.getAll();
    patchState(store, { books, isLoading: false });
  },
}));
```

### 80: What is `patchState`?

`patchState` updates the state of a SignalStore or `signalState`. You can pass partial state objects or updater functions:

```ts
patchState(store, { isLoading: true });
patchState(store, (state) => ({ count: state.count + 1 }));
patchState(store, { isLoading: false }, (state) => ({
  books: [...state.books, book],
}));
```

It merges the result into the current state, it doesn't replace the whole state.

### 81: How do you provide a SignalStore?

Two common ways:

- Globally, by passing `{ providedIn: 'root' }` as the first argument. You get one shared instance.

```ts
export const AuthStore = signalStore(
  { providedIn: "root" },
  withState(initialAuthState),
);
```

- Locally, by listing it in a component's (or route's) `providers`. Each component instance gets its own store, and it's destroyed with the component.

```ts
@Component({
  providers: [BooksStore],
})
export class BooksPage {}
```

### 82: How do you use a SignalStore in a component?

```ts
@Component({
  selector: "app-books-page",
  providers: [BooksStore],
  template: `
    <input [value]="store.filter.query()" (input)="onQuery($event)" />
    @if (store.isLoading()) {
      <p>Loading...</p>
    }
    @for (book of store.sortedBooks(); track book.id) {
      <p>{{ book.title }}</p>
    }
  `,
})
export class BooksPage {
  readonly store = inject(BooksStore);

  onQuery(event: Event) {
    this.store.updateQuery((event.target as HTMLInputElement).value);
  }
}
```

### 83: What is `signalState`?

`signalState` creates a single state object as a signal with deep signals for nested properties. It's lighter than `signalStore` and works well inside a component or a service.

```ts
import { signalState, patchState } from "@ngrx/signals";

export class UserForm {
  readonly state = signalState({ name: "", age: 0, address: { city: "" } });

  setCity(city: string) {
    patchState(this.state, (s) => ({ address: { ...s.address, city } }));
  }
}

// read: this.state(), this.state.name(), this.state.address.city()
```

### 84: What is the difference between `signalState` and `signalStore`?

- `signalState` is just a state signal. No methods, computed or hooks. You create it with a function call in a class field.
- `signalStore` creates an injectable class. You can add state, computed signals, methods, hooks, props, entities and custom features. It's the better choice when logic grows or the state is shared.

### 85: What is `withHooks`?

`withHooks` lets you run code when the store is created (`onInit`) and destroyed (`onDestroy`).

```ts
export const BooksStore = signalStore(
  withState(initialState),
  withMethods(/* ... */),
  withHooks({
    onInit(store) {
      store.loadAll();
    },
    onDestroy(store) {
      console.log("books store destroyed", store.books().length);
    },
  }),
);
```

### 86: What is `rxMethod`?

`rxMethod` from `@ngrx/signals/rxjs-interop` creates a method backed by an RxJS pipeline. You can call it with a plain value, a signal, or an observable. It's useful for things like debounced search where RxJS operators help.

```ts
import { rxMethod } from "@ngrx/signals/rxjs-interop";
import { tapResponse } from "@ngrx/operators";

withMethods((store, api = inject(BooksService)) => ({
  search: rxMethod<string>(
    pipe(
      debounceTime(300),
      distinctUntilChanged(),
      tap(() => patchState(store, { isLoading: true })),
      switchMap((query) =>
        api.search(query).pipe(
          tapResponse({
            next: (books) => patchState(store, { books }),
            error: console.error,
            finalize: () => patchState(store, { isLoading: false }),
          }),
        ),
      ),
    ),
  ),
}));
```

### 87: What is `@ngrx/component`?

It contains two standalone helpers for templates:

- `PushPipe` (`ngrxPush`) - like `async` but built with zoneless and fine-grained change detection in mind.
- `LetDirective` (`*ngrxLet`) - binds an observable to a template variable and handles loading and error states.

Now that signals are common, many apps don't need it as much, but it's still supported.

### 88: What is the `ngrxPush` pipe?

It's a replacement for `async` that schedules change detection for the component when a new value arrives, so it works without Zone.js.

```ts
@Component({
  imports: [PushPipe],
  template: `<p>{{ count$ | ngrxPush }}</p>`,
})
export class Counter {}
```

### 89: What is the `*ngrxLet` directive?

It binds the value of an observable to a local variable. It also shows the value `0`, `false`, `''` correctly (unlike `*ngIf` with `async`), and supports `suspense` and `error` templates.

```html
<ng-container *ngrxLet="book$ as book; error as err; suspense: loading">
  <h1>{{ book.title }}</h1>
</ng-container>

<ng-template #loading>Loading...</ng-template>
```

### 90: What is `@ngrx/component-store`?

`ComponentStore` is an RxJS-based store meant for local component state. It has `select`, `updater`, `effect`, `setState` and `patchState`. It is still maintained, but for new code the NgRx team recommends SignalStore, which covers the same use cases using signals.

### 91: What is `@ngrx/operators`?

It's a small package of RxJS operators used across NgRx:

- `tapResponse` - handles next, error, complete and finalize without killing the stream.
- `mapResponse` - maps success and error to values (often actions or events).
- `concatLatestFrom` - reads latest values from other observables when the source emits.

`tapResponse` and `concatLatestFrom` used to live in `@ngrx/component-store` and `@ngrx/effects`. They were moved here in NgRx 18.

### 92: What is `tapResponse`?

`tapResponse` is an operator that lets you handle success and error of an inner observable in one place, and it catches the error so the outer stream keeps working.

```ts
switchMap((id) =>
  api.getBook(id).pipe(
    tapResponse({
      next: (book) => patchState(store, { book }),
      error: (err: HttpErrorResponse) =>
        patchState(store, { error: err.message }),
      finalize: () => patchState(store, { isLoading: false }),
    }),
  ),
);
```

### 93: What is `concatLatestFrom`?

It's an operator that adds the latest value from another observable (often a selector) to the emitted value. It only subscribes to the other observable when the source emits, so selectors are read lazily.

```ts
import { concatLatestFrom } from "@ngrx/operators";

export const saveBook = createEffect(
  (
    actions$ = inject(Actions),
    store = inject(Store),
    api = inject(BooksService),
  ) =>
    actions$.pipe(
      ofType(BookFormActions.saveClicked),
      concatLatestFrom(() => store.select(selectCurrentUserId)),
      concatMap(([{ book }, userId]) =>
        api.save(book, userId).pipe(
          map((saved) => BooksApiActions.saveSuccess({ book: saved })),
          catchError(() => of(BooksApiActions.saveFailure())),
        ),
      ),
    ),
  { functional: true },
);
```

### 94: What is `@ngrx/schematics`?

It adds Angular CLI generators for NgRx code: actions, reducers, effects, selectors, features, entities, containers and component stores.

```bash
ng add @ngrx/schematics@latest
ng generate feature books/Book --group
ng generate action auth/Auth
```

### 95: What is `@ngrx/eslint-plugin`?

It's an ESLint plugin with rules that catch common NgRx mistakes, like dispatching several actions in a row, subscribing to the store in components, forgetting `ofType`, or not using `protectedState` in SignalStore.

```bash
ng add @ngrx/eslint-plugin
```

It ships configs for store, effects, component-store, operators and signals.

### 96: What are runtime checks in NgRx Store?

Runtime checks are checks that run in development mode to catch mistakes early:

- `strictStateImmutability` - state must not be mutated.
- `strictActionImmutability` - actions must not be mutated.
- `strictStateSerializability` - state must be serializable.
- `strictActionSerializability` - actions must be serializable.
- `strictActionWithinNgZone` - actions must be dispatched inside NgZone.
- `strictActionTypeUniqueness` - action types must be unique.

```ts
provideStore(reducers, {
  runtimeChecks: {
    strictStateImmutability: true,
    strictActionImmutability: true,
    strictStateSerializability: true,
    strictActionSerializability: true,
    strictActionTypeUniqueness: true,
  },
});
```

### 97: Which runtime checks are on by default?

`strictStateImmutability` and `strictActionImmutability` are on by default. The others are off unless you enable them. All runtime checks only run in development mode, so they don't slow down production builds.

### 98: What is the `@ngrx/store/init` action?

It's the first action NgRx dispatches when the store is created. Every reducer receives it and returns its initial state. When feature states are added later (for example in lazy routes), NgRx dispatches `@ngrx/store/update-reducers` so the new reducers can set their initial state.

You can import them as `INIT` and `UPDATE` from `@ngrx/store`.

### 99: How do you type a feature state?

Write an interface (or type) for the slice and use it in the initial state:

```ts
export interface AuthState {
  user: User | null;
  token: string | null;
  status: "idle" | "loading" | "error";
}

export const initialAuthState: AuthState = {
  user: null,
  token: null,
  status: "idle",
};
```

`createReducer` and `createFeature` infer the type from the initial state.

### 100: Should you type the global store with `Store<AppState>`?

It's not recommended. The generic on `Store` gives a false sense of type safety, because the state can contain lazy features that aren't loaded yet. The `no-typed-global-store` lint rule warns about it. Instead, inject `Store` without a generic and use typed selectors, which already return the right type.

```ts
private readonly store = inject(Store);
readonly user = this.store.selectSignal(selectUser); // Signal<User | null>
```

### 101: What is a feature state?

A feature state is one slice of the global state owned by a feature, like `books` or `auth`. It has its own reducer and is registered with `provideState`. The global state object then looks like `{ books: {...}, auth: {...} }`.

### 102: What is root state?

Root state is the state registered with `provideStore(...)` when the app starts. Feature states are added to it later or at the same time. Many apps leave the root empty (`provideStore()`) and register everything as features.

### 103: How do you lazy load feature state?

Add `provideState` (and `provideEffects`) to the route's `providers`. The reducer is registered the first time the route loads.

```ts
export const routes: Routes = [
  {
    path: "admin",
    loadChildren: () => import("./admin/admin.routes"),
    providers: [provideState(adminFeature), provideEffects(adminEffects)],
  },
];
```

### 104: What is a meta-reducer?

A meta-reducer is a function that takes a reducer and returns a new reducer. It wraps your reducers, so it sees every action and every state change. It's like middleware for reducers.

```ts
export function logger(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) => {
    const next = reducer(state, action);
    console.log(action.type, { before: state, after: next });
    return next;
  };
}

provideStore(reducers, { metaReducers: isDevMode() ? [logger] : [] });
```

### 105: What are common uses for meta-reducers?

- Logging actions and state.
- Resetting all state on logout.
- Saving state to and loading it from local storage.
- Undo and redo.
- Reporting errors to a monitoring tool.

### 106: What does `Store` extend?

`Store` extends `Observable`, so you can pipe it directly. It also implements `Observer<Action>`, so `store.next(action)` works like dispatch (though you should use `dispatch`).

### 107: Does the store emit the current state when you subscribe?

Yes. Internally state is kept in a `BehaviorSubject`, so any new subscriber gets the current state right away, then every new state after that. `store.select` also uses `distinctUntilChanged`, so you only get a new value when the selected value changes by reference.

### 108: What is unidirectional data flow?

Data moves in one direction:

1. The component dispatches an action.
2. Reducers create new state.
3. Selectors read the new state.
4. The component shows it.

Effects sit on the side: they listen to actions and dispatch new ones. Because it always goes the same way, it's easier to follow what happened.

### 109: When should you not use NgRx Store?

- Small apps with little shared state.
- State that only one component uses (local `signal()` is enough).
- Form input values while the user is typing.
- When the team doesn't know the pattern and the app won't benefit from it.

In many of these cases a simple service with signals, or a SignalStore, is a better fit than the full Redux setup.

### 110: How has NgRx reduced boilerplate over time?

- `createActionGroup` makes many actions at once.
- `createFeature` builds feature selectors for you.
- Functional effects remove the need for effect classes.
- `provideStore`, `provideState`, `provideEffects` replace NgModules.
- `selectSignal` removes subscription code.
- SignalStore gives a state, computed and methods setup without actions and reducers at all.

### 111: How do you test a reducer?

A reducer is a pure function, so you call it with state and an action and check the result:

```ts
describe("booksReducer", () => {
  it("sets books on load success", () => {
    const books = [{ id: "1", title: "NgRx" }] as Book[];
    const state = booksFeature.reducer(
      initialState,
      BooksApiActions.loadSuccess({ books }),
    );
    expect(state.books).toEqual(books);
    expect(state.loading).toBe(false);
  });
});
```

### 112: How do you test a selector?

Use the `projector` function to test the logic without building a full state:

```ts
it("filters books by query", () => {
  const books = [
    { id: "1", title: "Angular" },
    { id: "2", title: "React" },
  ] as Book[];
  const result = selectFilteredBooks.projector(books, "ang");
  expect(result).toEqual([books[0]]);
});
```

You can also call the selector with a full state object: `selectFilteredBooks({ books: { ... } })`.

### 113: What is `provideMockStore`?

It's a testing provider from `@ngrx/store/testing` that replaces the real store with `MockStore`. You can give it an initial state and selector values. Reducers and effects don't run.

```ts
TestBed.configureTestingModule({
  imports: [BooksPage],
  providers: [
    provideMockStore({
      initialState: { books: initialState },
      selectors: [{ selector: selectBooks, value: [] }],
    }),
  ],
});
```

### 114: What is `MockStore`?

`MockStore` is the fake store you get from `provideMockStore`. You inject it in tests to set state, override selectors and spy on dispatch.

```ts
const store = TestBed.inject(MockStore);
const dispatchSpy = spyOn(store, "dispatch");
```

### 115: What is `overrideSelector`?

It makes a selector return a fixed value in tests:

```ts
store.overrideSelector(selectBooks, [{ id: "1", title: "NgRx" } as Book]);
store.refreshState();
fixture.detectChanges();
```

It also works with `selectSignal`.

### 116: What is `provideMockActions`?

It's a testing provider from `@ngrx/effects/testing` that lets you control the `Actions` stream in effect tests:

```ts
let actions$: Observable<Action>;

TestBed.configureTestingModule({
  providers: [BooksEffects, provideMockActions(() => actions$)],
});

actions$ = of(BooksPageActions.opened());
```

### 117: How do you write a simple test for a SignalStore?

Provide the store with `TestBed`, inject it, and call its methods:

```ts
describe("CounterStore", () => {
  it("increments", () => {
    TestBed.configureTestingModule({ providers: [CounterStore] });
    const store = TestBed.inject(CounterStore);

    store.increment();

    expect(store.count()).toBe(1);
    expect(store.double()).toBe(2);
  });
});
```

### 118: Why should action payloads be serializable?

Serializable data (strings, numbers, booleans, plain objects, arrays) can be logged, shown in DevTools, saved, replayed and sent between tabs. Class instances, functions, `Date`, `Map` or DOM elements can break DevTools and time travel. `strictActionSerializability` can catch this.

### 119: Can an action have no payload?

Yes. With `createAction`, leave out `props`. With `createActionGroup`, use `emptyProps()`.

```ts
export const logout = createAction("[Header] Logout Clicked");
store.dispatch(logout());
```

### 120: What is the `type` property of an action creator?

Each action creator has a static `type` property equal to the action type string:

```ts
BooksApiActions.loadSuccess.type; // '[Books API] Load Success'
```

You rarely need it, because `on` and `ofType` accept the creator itself.

### 121: Can you use string enums for action types?

You can, but it's an older approach. With `createAction` and `createActionGroup` the type string is created and typed for you, so enums only add more code. The `prefer-action-creator` lint rule pushes toward action creators.

### 122: What is the `Action` interface?

It's the basic type every action follows:

```ts
interface Action<T extends string = string> {
  type: T;
}
```

Action creators return objects that extend this with their props.

### 123: What is the `ActionReducer` type?

`ActionReducer<S, A>` is the type of a reducer function:

```ts
type ActionReducer<S, A extends Action = Action> = (
  state: S | undefined,
  action: A,
) => S;
```

It's mostly used when writing meta-reducers.

### 124: What is the `select` operator from `@ngrx/store`?

It's the operator version of `store.select`. It maps state to a slice and adds `distinctUntilChanged`.

```ts
import { select } from "@ngrx/store";

this.store.pipe(select(selectBooks));
```

`store.select(selectBooks)` does the same thing and is more common.

### 125: Why doesn't the UI re-render when unrelated state changes?

`store.select` and `store.selectSignal` only emit or notify when the selected value changes by reference. Combined with memoized selectors that return the same reference when inputs are unchanged, a component isn't notified when another part of the state changes.

### 126: How do you combine several pieces of state for a component?

Either build a selector that combines them, or combine signals in the component with `computed`:

```ts
export const selectCartSummary = createSelector(
  selectCartItems,
  selectDiscount,
  (items, discount) => ({
    count: items.length,
    total: items.reduce((sum, i) => sum + i.price, 0) * (1 - discount),
  }),
);
```

```ts
readonly items = this.store.selectSignal(selectCartItems);
readonly discount = this.store.selectSignal(selectDiscount);
readonly total = computed(() =>
  this.items().reduce((s, i) => s + i.price, 0) * (1 - this.discount())
);
```

Selectors are better when the logic is reused or should be tested on its own.

### 127: What is a view model selector?

It's a selector that returns everything one component needs in one object:

```ts
export const selectBooksPageViewModel = createSelector({
  books: selectFilteredBooks,
  loading: selectLoading,
  query: selectQuery,
});
```

```ts
readonly vm = this.store.selectSignal(selectBooksPageViewModel);
```

The component then reads `vm().books`, `vm().loading` and so on.

### 128: How can you reset the whole state on logout?

A common way is a meta-reducer that returns `undefined` state when it sees the logout action, so every reducer goes back to its initial state:

```ts
export function clearOnLogout(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) => {
    if (action.type === AuthActions.logoutSuccess.type) {
      return reducer(undefined, action);
    }
    return reducer(state, action);
  };
}
```

### 129: How do you keep track of loading and error states?

Add fields for them in the feature state and update them in the reducer:

```ts
export interface BooksState {
  books: Book[];
  loading: boolean;
  error: string | null;
}

createReducer(
  initialState,
  on(BooksPageActions.opened, (s) => ({ ...s, loading: true, error: null })),
  on(BooksApiActions.loadSuccess, (s, { books }) => ({
    ...s,
    books,
    loading: false,
  })),
  on(BooksApiActions.loadFailure, (s, { error }) => ({
    ...s,
    error,
    loading: false,
  })),
);
```

Some teams use one `status: 'idle' | 'loading' | 'loaded' | 'error'` field instead of two booleans, which avoids impossible combinations.

### 130: How do you show a loading spinner with NgRx state?

Select the loading flag and use it in the template:

```ts
readonly loading = this.store.selectSignal(selectLoading);
```

```html
@if (loading()) {
<app-spinner />
} @else {
<app-books-list [books]="books()" />
}
```

### 131: What is normalized state?

Normalized state stores each entity once, in a lookup by id, and other parts of the state refer to it by id instead of holding copies.

```ts
// not normalized
{ orders: [{ id: 1, customer: { id: 7, name: 'Ann' } }] }

// normalized
{
  customers: { ids: [7], entities: { 7: { id: 7, name: 'Ann' } } },
  orders: { ids: [1], entities: { 1: { id: 1, customerId: 7 } } },
}
```

Updates happen in one place and lookups by id are fast. `@ngrx/entity` and `withEntities` help with this.

### 132: Why should state be serializable?

So it can be shown in DevTools, saved to local storage, sent from the server for SSR, and compared easily. Avoid putting class instances, functions, `Map`, `Set`, `Date` objects, promises or observables in state. Store dates as ISO strings or timestamps.

### 133: Should form input values live in the store?

Usually not while the user is typing. Keep the live form state in the component (reactive forms or signal forms) and dispatch an action when something meaningful happens, like submit or save draft. Putting every keystroke in the global store adds a lot of actions and rarely helps.

### 134: What kind of state belongs in the global store?

State that is shared between features or routes, or needs to survive navigation:

- Logged-in user and permissions.
- Data from the server used in many places.
- App settings like theme or language.
- Shopping cart.

Things like "is this dropdown open" or a component's local filter usually belong in the component or a local SignalStore.

### 135: What are container and presentational components in an NgRx app?

- **Container (smart) components** inject the store, select data and dispatch actions.
- **Presentational (dumb) components** get data through inputs and send events through outputs. They don't know about NgRx.

```ts
@Component({
  selector: "app-book-list",
  template: `@for (b of books(); track b.id) {
    <p (click)="select.emit(b.id)">{{ b.title }}</p>
  }`,
})
export class BookList {
  readonly books = input.required<Book[]>();
  readonly select = output<string>();
}
```

This keeps most components easy to reuse and test.

### 136: Do you need to unsubscribe from store selections?

Not if you use `selectSignal`, the `async` pipe, or `ngrxPush`. They handle cleanup for you. If you subscribe manually in a component, you should clean up, for example with `takeUntilDestroyed()`. The `no-store-subscription` lint rule warns about manual subscriptions.

### 137: How do NgRx versions relate to Angular versions?

NgRx major versions follow Angular major versions. NgRx 21 is meant for Angular 21, and so on. When you upgrade Angular to a new major, you upgrade NgRx to the same major.

### 138: How do you upgrade NgRx?

Use `ng update`:

```bash
ng update @ngrx/store
```

It updates all installed NgRx packages together and runs migration schematics that fix code for breaking changes, such as moved imports.

### 139: What are NgRx migration schematics?

Scripts that run during `ng update` and change your code for you. For example, when `concatLatestFrom` and `tapResponse` moved to `@ngrx/operators` in v18, the migration updated the imports automatically.

### 140: What is `withEntities`?

`withEntities` from `@ngrx/signals/entities` adds an entity collection to a SignalStore. It adds `ids`, `entityMap` and a computed `entities` array.

```ts
import { withEntities, addEntity, removeEntity } from "@ngrx/signals/entities";

export const TodosStore = signalStore(
  withEntities<Todo>(),
  withMethods((store) => ({
    add(todo: Todo) {
      patchState(store, addEntity(todo));
    },
    remove(id: string) {
      patchState(store, removeEntity(id));
    },
  })),
);

// store.entities(), store.ids(), store.entityMap()
```

### 141: Which entity updaters are there in `@ngrx/signals/entities`?

- `addEntity`, `addEntities` - add if not present.
- `prependEntity`, `prependEntities` - add to the start.
- `setEntity`, `setEntities` - add or replace.
- `setAllEntities` - replace the whole collection.
- `updateEntity`, `updateEntities`, `updateAllEntities` - partial updates.
- `upsertEntity`, `upsertEntities` - add or merge.
- `removeEntity`, `removeEntities`, `removeAllEntities`.

All of them are passed to `patchState`:

```ts
patchState(store, updateEntity({ id: "1", changes: { done: true } }));
patchState(
  store,
  removeEntities((todo) => todo.done),
);
```

### 142: What does `getState` do?

`getState(store)` returns the current state of a SignalStore or `signalState` as a plain object. It's useful for logging or saving state.

```ts
const snapshot = getState(store);
localStorage.setItem("books", JSON.stringify(snapshot));
```

If you call it inside a `computed` or `effect`, it tracks the whole state.

### 143: What is `withProps`?

`withProps` adds properties that are not state, computed or methods. Common uses are injected services, observables, or Angular resources.

```ts
export const BooksStore = signalStore(
  withState(initialState),
  withProps(({ isLoading }) => ({
    _api: inject(BooksService),
    isLoading$: toObservable(isLoading),
  })),
  withMethods((store) => ({
    async load() {
      patchState(store, { books: await store._api.getAll() });
    },
  })),
);
```

Members that start with `_` are private and not exposed on the store instance.

### 144: Can you call `patchState` on a SignalStore from outside the store?

Not by default. SignalStore state is protected, so only the store's own methods can update it. This keeps all state changes in one place. If you really need outside updates, you can set `{ protectedState: false }`:

```ts
export const SettingsStore = signalStore(
  { providedIn: "root", protectedState: false },
  withState({ theme: "light" }),
);
```

In tests you can use `unprotected(store)` from `@ngrx/signals/testing` instead of turning protection off.

### 145: What is the `type<T>()` helper?

`type` from `@ngrx/signals` is a helper that only carries a TypeScript type. It's used when you need to tell a function about a type without giving a real value:

```ts
withEntities({ entity: type<Todo>(), collection: "todo" });

eventGroup({
  source: "Books Page",
  events: { queryChanged: type<string>() },
});
```

### 146: What does `{ providedIn: 'root' }` do in `signalStore`?

It makes the store a root-level singleton, like `@Injectable({ providedIn: 'root' })`. You can inject it anywhere without adding it to any `providers` array.

### 147: What is a DeepSignal?

When a state property is an object, SignalStore and `signalState` turn it into a DeepSignal. It's a signal you can call to get the whole object, and it also has signals for each nested property.

```ts
const state = signalState({
  user: { name: "Ann", address: { city: "Tbilisi" } },
});

state.user(); // { name: 'Ann', address: {...} }
state.user.name(); // 'Ann'
state.user.address.city(); // 'Tbilisi'
```

Nested signals are created lazily, only when you read them.

### 148: Can you use NgRx with standalone components?

Yes, and that's the main way now. Use `provideStore`, `provideState`, `provideEffects`, `provideStoreDevtools` and `provideRouterStore` in your app config or route providers. SignalStore works the same with or without NgModules.

### 149: Can you still use NgRx with NgModules?

Yes. The NgModule APIs still exist:

```ts
@NgModule({
  imports: [
    StoreModule.forRoot({}),
    StoreModule.forFeature(booksFeature),
    EffectsModule.forRoot([BooksEffects]),
    StoreDevtoolsModule.instrument({ maxAge: 25 }),
  ],
})
export class AppModule {}
```

New projects usually use the standalone `provide*` functions.

### 150: What is the difference between NgRx Store and SignalStore, in simple terms?

- **NgRx Store** is one global store for the whole app. You change it with actions and reducers, and handle async work in effects. It gives you a full action log, strong DevTools support and a strict structure.
- **SignalStore** is a store you build from features and provide where you need it (globally or per component). You change state with methods and `patchState`. It needs less code and uses signals directly.

Many apps use both: NgRx Store for big shared state, SignalStore for feature or component state. Some newer apps only use SignalStore, optionally with the events plugin when they want an event-based flow.

## Moderate Questions

### 151: Walk through what happens from `dispatch` to the UI update.

1. A component calls `store.dispatch(BooksPageActions.opened())`.
2. The action goes into `ActionsSubject`.
3. The `State` service runs the action through the combined reducer (root reducers plus all feature reducers, wrapped by meta-reducers) and gets the new state.
4. The new state is pushed into the state `BehaviorSubject` and the state signal.
5. The action is then pushed to `ScannedActionsSubject`, which feeds the `Actions` stream that effects listen to.
6. Selectors re-run. Memoized selectors only recompute if their inputs changed.
7. `select` observables and `selectSignal` signals that got a new value notify the components, and Angular updates the view.
8. If an effect matched the action, it does its work and dispatches a new action, and the cycle starts again.

### 152: Do reducers or effects see an action first?

Reducers. The state is updated first, and only then is the action sent to the `Actions` stream. So when an effect reads state with `concatLatestFrom`, it already sees the state after that action was reduced.

### 153: What are `extraSelectors` in `createFeature`?

`extraSelectors` lets you add derived selectors to a feature. The function receives the selectors that `createFeature` generated.

```ts
export const booksFeature = createFeature({
  name: "books",
  reducer: booksReducer,
  extraSelectors: ({ selectBooks, selectQuery }) => ({
    selectFilteredBooks: createSelector(
      selectBooks,
      selectQuery,
      (books, query) => books.filter((b) => b.title.includes(query)),
    ),
  }),
});

export const { selectFilteredBooks } = booksFeature;
```

With entity state you can spread the adapter selectors:

```ts
extraSelectors: ({ selectBooksState }) => ({
  ...booksAdapter.getSelectors(selectBooksState),
});
```

### 154: How do you write a selector that takes a parameter?

Use a factory function that returns a selector:

```ts
export const selectBookById = (id: string) =>
  createSelector(selectBookEntities, (entities) => entities[id]);
```

```ts
readonly book = this.store.selectSignal(selectBookById(this.bookId));
```

Each call creates a new selector with its own memoization. If you call it again and again with the same id (for example in a template), cache it or call it once in a field.

### 155: Why were selectors with props removed?

Old selectors accepted a `props` argument: `store.select(selectBook, { id })`. They had problems:

- Memoization was shared, so using the same selector with different props in two places broke the cache.
- Typing was weak.
- The props were passed to every input selector, which was confusing.

Factory selectors (see the previous question) solve all of these and are the supported approach.

### 156: How does selector memoization decide whether to recompute?

`createSelector` remembers the last arguments to the projector. When the selector runs:

1. It runs the input selectors.
2. It compares each result to the previous one by reference (`===`).
3. If all are the same, it returns the cached result.
4. If any changed, it runs the projector and caches the new result.

So memoization only works if reducers keep unchanged parts of the state as the same references, which immutable updates do.

### 157: What does `release()` do on a selector?

`release()` clears the selector's memoized values, and does the same for its input selectors. It can free memory for selectors that hold big results and are no longer needed, for example factory selectors created per component.

```ts
const selectBook = selectBookById("42");
// ...
selectBook.release();
```

### 158: How do you change the memoization of a selector?

Use `createSelectorFactory` with a custom memoize function. A common case is comparing the result deeply so the selector doesn't emit a new array that has the same content:

```ts
import { createSelectorFactory, resultMemoize } from "@ngrx/store";
import { isEqual } from "lodash-es";

const createDeepEqualSelector = createSelectorFactory((projector) =>
  resultMemoize(projector, isEqual),
);

export const selectActiveIds = createDeepEqualSelector(
  selectTodos,
  (todos: Todo[]) => todos.filter((t) => !t.done).map((t) => t.id),
);
```

### 159: What are `defaultMemoize` and `isEqualCheck`?

`defaultMemoize` is the memoize function NgRx uses by default. It caches the last arguments and result. `isEqualCheck` is the comparison it uses by default, which is a plain `===`. You can pass your own comparison functions to `defaultMemoize` or use `resultMemoize` to compare results.

### 160: Why does memoization matter for selectors that filter or map lists?

`filter` and `map` always return a new array. Without memoization, every state change (even an unrelated one) would produce a new array, and every component using it would re-render. With memoization, the projector only runs when the inputs change, so the array reference stays the same.

### 161: A selector returns a new object every time. Why is that a problem and how do you fix it?

Example:

```ts
// bad: the projector only depends on state, which changes on every action
export const selectSummary = createSelector(
  (state: AppState) => state,
  (state) => ({ count: state.books.books.length }),
);
```

The input selector returns the whole state, which changes on every action, so the projector runs every time and returns a new object. Components then update for no reason.

Fix it by using narrow input selectors:

```ts
export const selectSummary = createSelector(selectBooks, (books) => ({
  count: books.length,
}));
```

### 162: What is the `equal` option of `selectSignal`?

`selectSignal` accepts the same `equal` option as Angular's `computed`. It decides when the signal value is considered changed.

```ts
readonly ids = this.store.selectSignal(selectActiveIds, {
  equal: (a, b) => a.length === b.length && a.every((id, i) => id === b[i]),
});
```

This helps when a selector returns new arrays that are equal by content.

### 163: What is the difference between `switchMap`, `mergeMap`, `concatMap` and `exhaustMap` in effects?

All four map an action to an inner observable (usually an HTTP call). They differ in what happens when a new action comes in before the previous call is done:

- `switchMap` cancels the previous call and starts the new one.
- `mergeMap` runs all calls in parallel.
- `concatMap` queues calls and runs them one by one in order.
- `exhaustMap` ignores new actions while a call is running.

### 164: When would you use `exhaustMap`?

When repeated triggers should be ignored until the current one is done. Typical cases:

- Login: the user clicks "Log in" twice, you only want one request.
- Loading a page when it opens: a second "opened" while loading doesn't need a new request.

```ts
actions$.pipe(
  ofType(LoginPageActions.submitted),
  exhaustMap(({ credentials }) =>
    auth.login(credentials).pipe(
      map((user) => AuthApiActions.loginSuccess({ user })),
      catchError((e) => of(AuthApiActions.loginFailure({ error: e.message }))),
    ),
  ),
);
```

### 165: When would you use `concatMap`?

When order matters and you don't want to lose any request. For example saving changes to the same record: every save should go to the server and in the order they were made.

### 166: When would you use `mergeMap`?

When requests are independent and can run in parallel, and none should be cancelled. For example deleting several items: each delete action should run its own request.

### 167: Why is `switchMap` risky for write operations?

`switchMap` unsubscribes from the previous inner observable. For an HTTP call this cancels the request on the client side, but the server may have already received it and done the write. Your app then never gets the response, so the state can get out of sync with the server. Use `switchMap` for reads (like search) and `concatMap` / `mergeMap` / `exhaustMap` for writes.

### 168: How do you read state inside an effect?

Use `concatLatestFrom` with a selector:

```ts
export const loadNextPage = createEffect(
  (
    actions$ = inject(Actions),
    store = inject(Store),
    api = inject(BooksService),
  ) =>
    actions$.pipe(
      ofType(BooksPageActions.nextPageClicked),
      concatLatestFrom(() => [
        store.select(selectPage),
        store.select(selectQuery),
      ]),
      switchMap(([, page, query]) =>
        api.search(query, page + 1).pipe(
          map((result) => BooksApiActions.pageLoaded({ result })),
          catchError(() => of(BooksApiActions.pageFailed())),
        ),
      ),
    ),
  { functional: true },
);
```

### 169: Why use `concatLatestFrom` instead of `withLatestFrom`?

`withLatestFrom` subscribes to the other observable right away, when the effect is set up. If the selector depends on state that isn't ready yet (for example a lazy feature), it can run too early or throw. `concatLatestFrom` takes a function and only subscribes when an action actually arrives, so the selector is read at the right time. The `prefer-concat-latest-from` lint rule enforces this.

### 170: Can an effect start from something other than an action?

Yes. An effect is just an observable, so it can start from any source: a timer, a websocket, a `fromEvent` on `window`, or Router events.

```ts
export const onlineStatus = createEffect(
  () =>
    merge(fromEvent(window, "online"), fromEvent(window, "offline")).pipe(
      map(() => NetworkActions.statusChanged({ online: navigator.onLine })),
    ),
  { functional: true },
);
```

### 171: What is `ROOT_EFFECTS_INIT`?

It's an action dispatched when root effects have been added (`@ngrx/effects/init`). You can listen to it to run something once at startup:

```ts
export const init = createEffect(
  (actions$ = inject(Actions)) =>
    actions$.pipe(
      ofType(ROOT_EFFECTS_INIT),
      map(() => AppActions.started()),
    ),
  { functional: true },
);
```

### 172: What is the `OnInitEffects` interface?

A class-based effect can implement `OnInitEffects`. Its `ngrxOnInitEffects()` method returns an action that is dispatched once the effect class is registered. It's useful for lazy features that need to load something when they are first used.

```ts
@Injectable()
export class SettingsEffects implements OnInitEffects {
  ngrxOnInitEffects(): Action {
    return SettingsActions.init();
  }
}
```

### 173: What does NgRx do by default when an effect throws?

The default effects error handler logs the error with Angular's `ErrorHandler` and resubscribes the effect, up to 10 times. This stops one bad error from killing the effect completely. You can turn this off for one effect with `useEffectsErrorHandler: false`, but then an unhandled error ends that effect for good.

### 174: How do you write a custom effects error handler?

Provide `EFFECTS_ERROR_HANDLER`:

```ts
import { EFFECTS_ERROR_HANDLER } from "@ngrx/effects";
import { ErrorHandler } from "@angular/core";
import { Observable, retry } from "rxjs";

export function effectsErrorHandler<T extends Action>(
  observable$: Observable<T>,
  errorHandler: ErrorHandler,
): Observable<T> {
  return observable$.pipe(
    retry({
      count: 3,
      delay: 1000,
      resetOnSuccess: true,
    }),
  );
}

providers: [{ provide: EFFECTS_ERROR_HANDLER, useValue: effectsErrorHandler }];
```

### 175: Can an effect dispatch more than one action?

Yes, by emitting several actions, for example with `switchMap` returning an array or `of(a, b)`:

```ts
switchMap(({ order }) => [
  OrderApiActions.placed({ order }),
  CartActions.cleared(),
]);
```

It's often better, though, to dispatch one action and let other reducers react to it. The `no-multiple-actions-in-effects` lint rule points this out. Here, the cart reducer could listen to `OrderApiActions.placed` directly.

### 176: How do you navigate from an effect?

Inject `Router` and use `dispatch: false`:

```ts
export const redirectAfterLogin = createEffect(
  (actions$ = inject(Actions), router = inject(Router)) =>
    actions$.pipe(
      ofType(AuthApiActions.loginSuccess),
      tap(() => router.navigate(["/dashboard"])),
    ),
  { functional: true, dispatch: false },
);
```

### 177: How do functional effects make testing easier?

Dependencies are default parameters. In a test you can call the effect function directly and pass mocks, without TestBed:

```ts
it("loads books", (done) => {
  const actions$ = of(BooksPageActions.opened());
  const api = { getAll: () => of([book]) } as unknown as BooksService;

  loadBooks(actions$, api).subscribe((action) => {
    expect(action).toEqual(BooksApiActions.loadSuccess({ books: [book] }));
    done();
  });
});
```

### 178: Where do effects run and how long do they live?

Effects run in the environment injector where they were provided. Root effects start when the app starts and live for the whole app. Effects in a lazy route's `providers` start the first time that route's injector is created. They are not stopped when you leave the route, because the route injector stays around. Effects listen to all actions in the app, not just the feature's actions.

### 179: How do you debounce a search in an effect?

```ts
export const search = createEffect(
  (actions$ = inject(Actions), api = inject(BooksService)) =>
    actions$.pipe(
      ofType(BooksPageActions.queryChanged),
      debounceTime(300),
      map(({ query }) => query.trim()),
      distinctUntilChanged(),
      switchMap((query) =>
        api.search(query).pipe(
          map((books) => BooksApiActions.searchSuccess({ books })),
          catchError(() => of(BooksApiActions.searchFailure())),
        ),
      ),
    ),
  { functional: true },
);
```

To test debounce logic easier, you can inject the scheduler or use `TestScheduler`.

### 180: How do you poll an API with effects?

Start a timer when polling starts and stop it with `takeUntil` when a stop action arrives:

```ts
export const pollStatus = createEffect(
  (actions$ = inject(Actions), api = inject(JobsService)) =>
    actions$.pipe(
      ofType(JobPageActions.pollingStarted),
      switchMap(({ jobId }) =>
        timer(0, 5000).pipe(
          switchMap(() =>
            api.status(jobId).pipe(
              map((status) => JobApiActions.statusLoaded({ status })),
              catchError(() => of(JobApiActions.statusFailed())),
            ),
          ),
          takeUntil(actions$.pipe(ofType(JobPageActions.pollingStopped))),
        ),
      ),
    ),
  { functional: true },
);
```

### 181: How do you cancel an in-flight request with an action?

Use `takeUntil` on the inner observable:

```ts
switchMap(({ fileId }) =>
  api.upload(fileId).pipe(
    map(() => UploadApiActions.done({ fileId })),
    catchError(() => of(UploadApiActions.failed({ fileId }))),
    takeUntil(actions$.pipe(ofType(UploadActions.cancelled))),
  ),
);
```

### 182: What are the options of `tapResponse`?

`tapResponse` takes an object with:

- `next` - called on each value.
- `error` - called on error. The error is caught, so the outer stream continues.
- `complete` - optional, called when the inner observable completes.
- `finalize` - optional, called after complete or error. Good for turning off loading flags.

```ts
tapResponse({
  next: (user) => patchState(store, { user }),
  error: (e: HttpErrorResponse) => patchState(store, { error: e.message }),
  finalize: () => patchState(store, { loading: false }),
});
```

The older form with positional arguments `tapResponse(next, error)` is still supported, but the object form is clearer.

### 183: What is `mapResponse`?

`mapResponse` maps success and error to new values, usually actions or events, and catches errors. It's like `map` + `catchError` in one call.

```ts
import { mapResponse } from "@ngrx/operators";

exhaustMap(() =>
  api.getAll().pipe(
    mapResponse({
      next: (books) => BooksApiActions.loadSuccess({ books }),
      error: (e: HttpErrorResponse) =>
        BooksApiActions.loadFailure({ error: e.message }),
    }),
  ),
);
```

### 184: How does `createActionGroup` keep things type safe?

The source and event names are turned into types using TypeScript template literal types, so:

- `BooksApiActions.loadSuccess` exists and `BooksApiActions.loadsuccess` gives an error.
- The action `type` is the literal `'[Books API] Load Success'`, not just `string`.
- Props are typed from `props<...>()`.

It also rejects duplicate event names in the same group and event names that would collide after camel casing.

### 185: How do you get the type of an action created with an action creator?

Use `ReturnType`:

```ts
type LoadSuccessAction = ReturnType<typeof BooksApiActions.loadSuccess>;
```

To get a union of all actions in a group:

```ts
type BooksApiAction = ReturnType<
  (typeof BooksApiActions)[keyof typeof BooksApiActions]
>;
```

### 186: How does typing work when one `on` handles actions with different props?

The handler's action is a union of the action types. You can only safely read props that exist on all of them, or check the `type` first:

```ts
on(
  BooksApiActions.createSuccess,
  BooksApiActions.updateSuccess,
  (state, action) => ({
    ...state,
    lastSaved: action.book, // both have `book`
  }),
);
```

If the props are different, it's usually clearer to write two `on` handlers.

### 187: How do you update deeply nested state in a reducer?

Copy every level you change:

```ts
on(SettingsActions.themeColorChanged, (state, { color }) => ({
  ...state,
  preferences: {
    ...state.preferences,
    theme: {
      ...state.preferences.theme,
      color,
    },
  },
}));
```

If this gets painful, it's often a sign the state is too nested. Flatten it, or split it into more features. Some teams use Immer through community packages like `ngrx-immer`.

### 188: Can you use Immer with NgRx?

Yes, through community libraries like `ngrx-immer`, which provide `immerOn` for reducers. Immer lets you write code that looks like mutation, and it produces a new immutable object:

```ts
import { immerOn } from "ngrx-immer/store";

createReducer(
  initialState,
  immerOn(TodoActions.toggled, (state, { id }) => {
    const todo = state.todos.find((t) => t.id === id);
    if (todo) todo.done = !todo.done;
  }),
);
```

It's not part of NgRx itself, so weigh the extra dependency.

### 189: Show a meta-reducer that resets state on logout, with types.

```ts
import { ActionReducer, MetaReducer } from "@ngrx/store";

export function resetOnLogout<S>(reducer: ActionReducer<S>): ActionReducer<S> {
  return (state, action) => {
    if (action.type === AuthActions.logoutSuccess.type) {
      // keep only what should survive logout
      return reducer(undefined, action);
    }
    return reducer(state, action);
  };
}

export const metaReducers: MetaReducer[] = [resetOnLogout];

provideStore({}, { metaReducers });
```

### 190: How do you save and load state from `localStorage` with a meta-reducer?

```ts
const KEY = "app-state";
const KEYS_TO_SAVE = ["cart", "settings"] as const;

export function localStorageSync(
  reducer: ActionReducer<any>,
): ActionReducer<any> {
  return (state, action) => {
    if (action.type === INIT || action.type === UPDATE) {
      const saved = localStorage.getItem(KEY);
      if (saved) {
        const next = reducer(state, action);
        return { ...next, ...JSON.parse(saved) };
      }
    }

    const next = reducer(state, action);
    const toSave = Object.fromEntries(KEYS_TO_SAVE.map((k) => [k, next[k]]));
    localStorage.setItem(KEY, JSON.stringify(toSave));
    return next;
  };
}
```

Things to watch: SSR (no `localStorage` on the server), state shape changes between app versions, and writing on every action (you might want to throttle it or do it in an effect instead). The community library `ngrx-store-localstorage` handles many of these cases.

### 191: How do you add meta-reducers to a single feature?

Pass them in the third argument of `provideState`:

```ts
provideState("books", booksReducer, { metaReducers: [booksLogger] });
```

They wrap only that feature's reducer.

### 192: When should you turn on `strictActionWithinNgZone` and `strictActionTypeUniqueness`?

- `strictActionWithinNgZone` warns when an action is dispatched outside Angular's zone, which can cause the UI to not update in zone-based apps. It doesn't matter in zoneless apps.
- `strictActionTypeUniqueness` warns when two action creators have the same type. It's a cheap way to catch copy-paste mistakes, and it's worth turning on.

### 193: When is it OK to turn off the serializability checks?

When you knowingly keep something non-serializable in state or actions and accept that DevTools and persistence may not work for it, like a `File` in an upload action. Even then it's better to keep the non-serializable thing outside the store (for example in a service keyed by id) and only put serializable data in actions.

### 194: How do you use `updateOne`, `upsertOne` and `mapOne`?

```ts
// partial update by id
booksAdapter.updateOne({ id: book.id, changes: { title: "New title" } }, state);

// add if missing, merge if present
booksAdapter.upsertOne(book, state);

// update using a function
booksAdapter.mapOne({ id, map: (b) => ({ ...b, likes: b.likes + 1 }) }, state);
```

`updateOne` takes an `Update<T>` object with `id` and `changes`.

### 195: How do you keep extra fields next to entities?

Extend `EntityState` and pass the extra fields to `getInitialState`:

```ts
export interface BooksState extends EntityState<Book> {
  selectedId: string | null;
  status: "idle" | "loading" | "error";
}

export const adapter = createEntityAdapter<Book>();

export const initialState: BooksState = adapter.getInitialState({
  selectedId: null,
  status: "idle",
});
```

### 196: How do you combine entity selectors with `createFeature`?

```ts
export const booksFeature = createFeature({
  name: "books",
  reducer: booksReducer,
  extraSelectors: ({ selectBooksState, selectEntities, selectSelectedId }) => ({
    ...adapter.getSelectors(selectBooksState),
    selectSelectedBook: createSelector(
      selectEntities,
      selectSelectedId,
      (entities, id) => (id ? entities[id] : undefined),
    ),
  }),
});

export const { selectAll, selectTotal, selectSelectedBook } = booksFeature;
```

`selectEntities` and `selectIds` are generated by `createFeature` from the `entities` and `ids` properties, and `getSelectors` adds `selectAll` and `selectTotal`.

### 197: What is the cost of `sortComparer`?

The adapter keeps `ids` sorted after every add or update, which costs time on big collections with many updates. If you only need sorting for display, it can be cheaper to sort in a memoized selector instead, since that only runs when the collection changes and when someone reads it.

### 198: How do you select route params inside a feature selector?

Combine router selectors with feature selectors:

```ts
export const selectBookId = selectRouteParam("bookId");

export const selectBookFromRoute = createSelector(
  selectBookEntities,
  selectBookId,
  (entities, id) => (id ? entities[id] : undefined),
);
```

The component then doesn't need `ActivatedRoute` at all.

### 199: Which actions does router-store dispatch?

- `ROUTER_REQUEST` - navigation started.
- `ROUTER_NAVIGATION` - before guards and resolvers run (with default timing).
- `ROUTER_NAVIGATED` - navigation finished.
- `ROUTER_CANCEL` - navigation was cancelled, for example by a guard.
- `ROUTER_ERROR` - navigation failed.

There are action creators for them: `routerRequestAction`, `routerNavigationAction`, `routerNavigatedAction`, `routerCancelAction`, `routerErrorAction`.

```ts
actions$.pipe(ofType(routerNavigatedAction) /* ... */);
```

### 200: What is the `navigationActionTiming` option?

It controls when `ROUTER_NAVIGATION` is dispatched:

- `NavigationActionTiming.PreActivation` (default) - before guards and resolvers.
- `NavigationActionTiming.PostActivation` - after guards and resolvers.

```ts
provideRouterStore({
  navigationActionTiming: NavigationActionTiming.PostActivation,
});
```

Use `PostActivation` if your effects should only react to navigations that guards allowed.

### 201: What is the difference between `RouterState.Minimal` and `RouterState.Full`?

- `Minimal` stores a serializable, smaller version of the router snapshot: url, params, query params, data, fragment and so on. It works well with DevTools and runtime checks.
- `Full` stores the full `ActivatedRouteSnapshot`, which has circular references and is not serializable. It is mostly kept for older apps. Prefer `Minimal` and set it explicitly so the intent is clear.

```ts
provideRouterStore({ routerState: RouterState.Minimal });
```

### 202: How do you write a custom router state serializer?

Implement `RouterStateSerializer` and return only what you need:

```ts
export interface AppRouterState {
  url: string;
  params: Params;
  queryParams: Params;
}

export class CustomSerializer implements RouterStateSerializer<AppRouterState> {
  serialize(routerState: RouterStateSnapshot): AppRouterState {
    let route = routerState.root;
    let params: Params = {};
    while (route.firstChild) {
      route = route.firstChild;
      params = { ...params, ...route.params };
    }
    return {
      url: routerState.url,
      params,
      queryParams: routerState.root.queryParams,
    };
  }
}

provideRouterStore({ serializer: CustomSerializer });
```

This example also merges params from parent routes, which the default doesn't do.

### 203: How do you read route `data` and `title` with router-store?

```ts
const { selectRouteData, selectRouteDataParam, selectTitle } =
  getRouterSelectors();

export const selectPageLayout = selectRouteDataParam("layout");
```

`selectRouteData` returns the data of the current (deepest) route, and `selectTitle` returns the resolved route title.

### 204: Can `withState` take a function?

Yes. `withState` accepts either an object or a factory function. The factory runs in an injection context, so you can inject tokens:

```ts
export const SettingsStore = signalStore(
  withState(() => inject(INITIAL_SETTINGS)),
);
```

It's also useful to make sure each store instance gets a fresh object.

### 205: Can a `withComputed` use members from an earlier `withComputed`?

Yes. Each feature receives everything defined before it. You can split computed signals into steps:

```ts
signalStore(
  withState({ items: [] as CartItem[], taxRate: 0.18 }),
  withComputed(({ items }) => ({
    subtotal: computed(() => items().reduce((s, i) => s + i.price * i.qty, 0)),
  })),
  withComputed(({ subtotal, taxRate }) => ({
    total: computed(() => subtotal() * (1 + taxRate())),
  })),
);
```

### 206: How do you use injected services in `withMethods`?

Inject them as default parameters of the factory, or inject them inside the factory body:

```ts
withMethods(
  (store, api = inject(OrdersService), toast = inject(ToastService)) => ({
    async cancel(id: string) {
      await api.cancel(id);
      patchState(store, removeEntity(id));
      toast.show("Order cancelled");
    },
  }),
);
```

### 207: How do you write a Promise-based async method in SignalStore?

```ts
withMethods((store, http = inject(HttpClient)) => ({
  async loadUser(id: string): Promise<void> {
    patchState(store, { status: "loading" });
    try {
      const user = await firstValueFrom(http.get<User>(`/api/users/${id}`));
      patchState(store, { user, status: "loaded" });
    } catch (e) {
      patchState(store, { status: "error", error: String(e) });
    }
  },
}));
```

Promise methods are easy to read but don't handle cancellation or races. If the user can trigger the method quickly many times, `rxMethod` with `switchMap` is safer.

### 208: Show an `rxMethod` that searches as the query signal changes.

```ts
export const BooksSearchStore = signalStore(
  withState({ query: "", books: [] as Book[], isLoading: false }),
  withMethods((store, api = inject(BooksService)) => ({
    setQuery(query: string) {
      patchState(store, { query });
    },
    searchByQuery: rxMethod<string>(
      pipe(
        debounceTime(300),
        distinctUntilChanged(),
        tap(() => patchState(store, { isLoading: true })),
        switchMap((query) =>
          api.search(query).pipe(
            tapResponse({
              next: (books) => patchState(store, { books }),
              error: console.error,
              finalize: () => patchState(store, { isLoading: false }),
            }),
          ),
        ),
      ),
    ),
  })),
  withHooks({
    onInit(store) {
      // re-runs every time query changes
      store.searchByQuery(store.query);
    },
  }),
);
```

### 209: What kinds of input can an `rxMethod` accept?

- A static value: `store.load(5)` runs once with 5.
- A signal: `store.load(this.id)` runs now and again every time the signal changes.
- An observable: `store.load(id$)` runs for every emission.

This lets the same method work for one-off calls and for reactive inputs.

### 210: What is `signalMethod`?

`signalMethod` from `@ngrx/signals` is like `rxMethod` but without RxJS. It creates a function that accepts a value or a signal. When given a signal, it runs the handler every time the signal changes.

```ts
import { signalMethod } from "@ngrx/signals";

withMethods((store) => ({
  logPage: signalMethod<number>((page) => {
    console.log("page changed", page);
  }),
}));
```

```ts
// in a component
readonly page = signal(1);
constructor() {
  this.store.logPage(this.page);
}
```

### 211: When do you pick `signalMethod` over `rxMethod`?

- `signalMethod` - simple synchronous reactions to a value, no need for RxJS operators, and you want to avoid RxJS in that code.
- `rxMethod` - you need operators like `debounceTime`, `switchMap`, `exhaustMap`, retries, or cancellation of async work.

`signalMethod` does not handle race conditions for async work, so for HTTP calls that can overlap, `rxMethod` is usually the better choice.

### 212: How do you use injected services inside `withHooks`?

Use the factory form. The factory runs in an injection context and returns the hooks object:

```ts
withHooks((store) => {
  const logger = inject(Logger);
  return {
    onInit() {
      logger.info("store created");
      store.load();
    },
    onDestroy() {
      logger.info("store destroyed");
    },
  };
});
```

### 213: How do you write reusable updater functions for `patchState`?

An updater is a function that takes state and returns a partial state. You can write them outside the store and reuse them:

```ts
import { PartialStateUpdater } from "@ngrx/signals";

export function setLoading(): { isLoading: boolean } {
  return { isLoading: true };
}

export function addTodo(todo: Todo): PartialStateUpdater<{ todos: Todo[] }> {
  return (state) => ({ todos: [...state.todos, todo] });
}

patchState(store, setLoading(), addTodo(newTodo));
```

The entity updaters in `@ngrx/signals/entities` follow the same idea.

### 214: What is `watchState`?

`watchState` runs a function every time the state of a SignalStore or `signalState` changes. Unlike Angular `effect`, it runs synchronously on every `patchState` call, not once after several changes.

```ts
withHooks({
  onInit(store) {
    watchState(store, (state) => {
      console.log("[BooksStore] state changed", state);
    });
  },
});
```

When called inside an injection context, it stops automatically when that context is destroyed. Outside of one, pass `{ injector }` or call the returned `destroy()`.

### 215: How do you use named collections with `withEntities`?

Pass a `collection` name. All members are then prefixed with that name:

```ts
export const LibraryStore = signalStore(
  withEntities({ entity: type<Book>(), collection: "book" }),
  withEntities({ entity: type<Author>(), collection: "author" }),
  withMethods((store) => ({
    addBook(book: Book) {
      patchState(store, addEntity(book, { collection: "book" }));
    },
  })),
);

// store.bookEntities(), store.bookIds(), store.bookEntityMap()
// store.authorEntities(), ...
```

### 216: What is `entityConfig`?

`entityConfig` lets you define the entity type, collection name and `selectId` once, and reuse it in `withEntities` and in updaters:

```ts
import { entityConfig, withEntities, addEntity } from "@ngrx/signals/entities";

const bookConfig = entityConfig({
  entity: type<Book>(),
  collection: "book",
  selectId: (book) => book.isbn,
});

export const BooksStore = signalStore(
  withEntities(bookConfig),
  withMethods((store) => ({
    add(book: Book) {
      patchState(store, addEntity(book, bookConfig));
    },
  })),
);
```

### 217: How do you handle entities without an `id` property in SignalStore?

Pass `selectId` to the updaters (or use `entityConfig`):

```ts
const selectId: SelectEntityId<Country> = (c) => c.code;

patchState(store, setAllEntities(countries, { selectId }));
patchState(
  store,
  updateEntity({ id: "GE", changes: { name: "Georgia" } }, { selectId }),
);
```

### 218: What is `signalStoreFeature`?

It lets you group several features into one reusable feature. You then use it in any store like a built-in feature.

```ts
export function withRequestStatus() {
  return signalStoreFeature(
    withState<{
      requestStatus: "idle" | "pending" | "fulfilled" | { error: string };
    }>({
      requestStatus: "idle",
    }),
    withComputed(({ requestStatus }) => ({
      isPending: computed(() => requestStatus() === "pending"),
      isFulfilled: computed(() => requestStatus() === "fulfilled"),
      error: computed(() => {
        const s = requestStatus();
        return typeof s === "object" ? s.error : null;
      }),
    })),
  );
}

export const BooksStore = signalStore(
  withEntities<Book>(),
  withRequestStatus(),
);
```

### 219: How do you write a custom feature that needs something from the store?

Pass an input object with `type<...>()` as the first argument to `signalStoreFeature`. Then the feature can only be used in stores that have those members.

```ts
export function withSelectedEntity<E extends { id: string }>() {
  return signalStoreFeature(
    { state: type<EntityState<E>>() },
    withState({ selectedId: null as string | null }),
    withComputed(({ entityMap, selectedId }) => ({
      selected: computed(() => {
        const id = selectedId();
        return id ? entityMap()[id] : undefined;
      }),
    })),
  );
}
```

The input can describe `state`, `props` and `methods`.

### 220: How do you write updaters that go with a custom feature?

Export updater functions next to the feature, so stores can use them with `patchState`:

```ts
export function setPending(): { requestStatus: 'pending' } {
  return { requestStatus: 'pending' };
}
export function setFulfilled(): { requestStatus: 'fulfilled' } {
  return { requestStatus: 'fulfilled' };
}
export function setError(error: string): { requestStatus: { error: string } } {
  return { requestStatus: { error } };
}

// in the store
async load() {
  patchState(store, setPending());
  try {
    patchState(store, setAllEntities(await api.getAll()), setFulfilled());
  } catch (e) {
    patchState(store, setError(String(e)));
  }
}
```

### 221: What is `withProps` used for besides services?

- Exposing observables built from signals: `isLoading$: toObservable(isLoading)`.
- Holding Angular `resource` or `httpResource` instances.
- Holding constant config or helper objects.
- Sharing private dependencies (prefixed with `_`) between later features.

```ts
withProps(() => ({
  _http: inject(HttpClient),
  pageSize: 20,
}));
```

### 222: How do private members work in SignalStore?

Any state, computed, prop or method whose name starts with `_` is private. It can be used by later features inside the store, but it's not available on the injected store instance.

```ts
signalStore(
  withState({ _cache: {} as Record<string, Book>, books: [] as Book[] }),
  withMethods((store) => ({
    _remember(book: Book) {
      patchState(store, (s) => ({ _cache: { ...s._cache, [book.id]: book } }));
    },
  })),
);

// inject(Store)._cache  -> TypeScript error, and undefined at runtime
```

### 223: Why is `protectedState` true by default?

If any component could call `patchState(store, ...)`, state changes would be spread across the app and hard to trace. With protected state, only the store's own methods can change it, so you can look at one file to see every possible change. It's the same idea as only changing global state through reducers.

### 224: What happens when a SignalStore is provided in a component?

A new instance is created when the component is created, and destroyed when the component is destroyed. `onDestroy` hooks run, and `rxMethod`, `signalMethod` and `watchState` calls made inside the store are cleaned up. Child components of that component can inject the same instance.

### 225: How can several components share one SignalStore instance without it being global?

Provide it in a common parent component (or in route `providers`). Every child in that part of the component tree that injects it gets the same instance:

```ts
@Component({
  selector: "app-checkout",
  providers: [CheckoutStore],
  template: `<app-cart-step /> <app-payment-step />`,
})
export class Checkout {}

@Component({ selector: "app-payment-step" /* ... */ })
export class PaymentStep {
  readonly store = inject(CheckoutStore); // same instance as in Checkout
}
```

### 226: What is `deepComputed`?

`deepComputed` from `@ngrx/signals` works like `computed`, but if the result is an object, you get a DeepSignal with signals for each nested property.

```ts
import { deepComputed } from "@ngrx/signals";

withComputed(({ page, pageSize, total }) => ({
  pagination: deepComputed(() => ({
    current: page(),
    totalPages: Math.ceil(total() / pageSize()),
  })),
}));

// store.pagination.totalPages()
```

### 227: How do you turn a SignalStore signal into an observable?

Use `toObservable` from `@angular/core/rxjs-interop`. It needs an injection context, so `withProps` is a good place:

```ts
withProps(({ query }) => ({
  query$: toObservable(query),
}));
```

You can also call it in a component constructor or field initializer.

### 228: How do you use Angular `resource` or `httpResource` with SignalStore?

Create the resource in `withProps` and expose its value with `withComputed`:

```ts
export const BookStore = signalStore(
  withState({ bookId: null as string | null }),
  withProps(({ bookId }) => ({
    _bookResource: httpResource<Book>(() => {
      const id = bookId();
      return id ? `/api/books/${id}` : undefined;
    }),
  })),
  withComputed(({ _bookResource }) => ({
    book: computed(() => _bookResource.value()),
    isLoading: computed(() => _bookResource.isLoading()),
  })),
  withMethods((store) => ({
    selectBook(bookId: string) {
      patchState(store, { bookId });
    },
  })),
);
```

When `bookId` changes, the resource fetches again by itself. Note that the resource's data is not part of the store state, so `getState` won't include it.

### 229: What is `withLinkedState`?

`withLinkedState` adds state that is derived from other signals but can also be changed by hand, like Angular's `linkedSignal`. When the source changes, the value is recalculated. Between changes you can still update it with `patchState`.

```ts
import { withLinkedState } from "@ngrx/signals";

export const OptionsStore = signalStore(
  withState({ options: [] as Option[] }),
  withLinkedState(({ options }) => ({
    // resets to the first option every time options change
    selectedOption: () => options()[0] ?? null,
  })),
  withMethods((store) => ({
    select(option: Option) {
      patchState(store, { selectedOption: option });
    },
  })),
);
```

You can also pass an explicit `linkedSignal({ source, computation })` if you need the previous value.

### 230: What is `withFeature`?

`withFeature` lets you call a custom feature with values from the current store. Normal custom features only see store members through their declared input. `withFeature` gives you the store instance, so you can pass its members as arguments.

```ts
export const BookStore = signalStore(
  withMethods((store, api = inject(BooksService)) => ({
    load(id: string): Promise<Book> {
      return api.get(id);
    },
  })),
  withFeature((store) => withEntityLoader((id) => store.load(id))),
);
```

This keeps the custom feature generic, because it doesn't need to know the method names of the store using it.

### 231: How do you set state directly in a SignalStore test?

Use `unprotected` from `@ngrx/signals/testing`. It lets you call `patchState` on a protected store in tests only:

```ts
import { unprotected } from "@ngrx/signals/testing";

it("shows sorted books", () => {
  TestBed.configureTestingModule({ providers: [BooksStore] });
  const store = TestBed.inject(BooksStore);

  patchState(unprotected(store), {
    books: [
      { id: "2", title: "B" },
      { id: "1", title: "A" },
    ] as Book[],
  });

  expect(store.sortedBooks().map((b) => b.title)).toEqual(["A", "B"]);
});
```

### 232: How do you test a store method that uses `rxMethod` and debounce?

Use fake timers and mock the service:

```ts
it("searches after debounce", fakeAsync(() => {
  const api = { search: jasmine.createSpy().and.returnValue(of([book])) };
  TestBed.configureTestingModule({
    providers: [BooksSearchStore, { provide: BooksService, useValue: api }],
  });
  const store = TestBed.inject(BooksSearchStore);

  store.searchByQuery("ngrx");
  tick(300);

  expect(api.search).toHaveBeenCalledWith("ngrx");
  expect(store.books()).toEqual([book]);
}));
```

With Vitest you'd use `vi.useFakeTimers()` and `vi.advanceTimersByTime(300)` instead.

### 233: How do you mock dependencies of a SignalStore?

Store dependencies come from DI, so you replace them in `TestBed` providers:

```ts
TestBed.configureTestingModule({
  providers: [
    BooksStore,
    {
      provide: BooksService,
      useValue: { getAll: () => Promise.resolve([book]) },
    },
  ],
});
```

You don't need to change the store code for tests.

### 234: What are `setState` and `refreshState` in `MockStore`?

- `setState(state)` replaces the whole mock state. Selectors that are not overridden recompute from it.
- `refreshState()` makes the store emit again. You call it after `overrideSelector` or `setResult` changes when the state itself didn't change.

```ts
store.setState({ books: { ...initialState, loading: true } });
fixture.detectChanges();
```

### 235: How do you test a class-based effect with `provideMockActions`?

```ts
describe("BooksEffects", () => {
  let actions$: Observable<Action>;
  let effects: BooksEffects;
  const api = { getAll: jasmine.createSpy() };

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        BooksEffects,
        provideMockActions(() => actions$),
        { provide: BooksService, useValue: api },
      ],
    });
    effects = TestBed.inject(BooksEffects);
  });

  it("returns loadFailure on error", (done) => {
    api.getAll.and.returnValue(throwError(() => new Error("boom")));
    actions$ = of(BooksPageActions.opened());

    effects.loadBooks$.subscribe((action) => {
      expect(action).toEqual(BooksApiActions.loadFailure({ error: "boom" }));
      done();
    });
  });
});
```

### 236: How do you test a component that uses `selectSignal` with `MockStore`?

`overrideSelector` works with signals too:

```ts
beforeEach(() => {
  TestBed.configureTestingModule({
    imports: [BooksPage],
    providers: [provideMockStore()],
  });
  store = TestBed.inject(MockStore);
  store.overrideSelector(selectBooks, [book]);
  store.overrideSelector(selectLoading, false);
  fixture = TestBed.createComponent(BooksPage);
  fixture.detectChanges();
});

it("dispatches opened on init", () => {
  const spy = spyOn(store, "dispatch");
  fixture.componentInstance.ngOnInit();
  expect(spy).toHaveBeenCalledWith(BooksPageActions.opened());
});
```

### 237: When would you write an integration test with the real store?

When you want to check that actions, reducers, selectors and effects work together, for example "when the page opens, the list shows data from the API". Use the real `provideStore`, `provideState`, `provideEffects`, and only mock the HTTP layer with `provideHttpClientTesting()`.

```ts
TestBed.configureTestingModule({
  imports: [BooksPage],
  providers: [
    provideStore(),
    provideState(booksFeature),
    provideEffects(booksEffects),
    provideHttpClient(),
    provideHttpClientTesting(),
  ],
});
```

These tests catch wiring mistakes that unit tests miss.

### 238: What does `resetSelectors` do on `MockStore`?

It removes all selector overrides and clears their memoized results. Call it in `afterEach` so values don't leak from one test to another:

```ts
afterEach(() => {
  store.resetSelectors();
});
```

### 239: What are the main parts of the `ComponentStore` API?

```ts
interface MoviesState {
  movies: Movie[];
}

@Injectable()
export class MoviesStore extends ComponentStore<MoviesState> {
  private readonly api = inject(MoviesService);

  constructor() {
    super({ movies: [] });
  }

  readonly movies = this.selectSignal((s) => s.movies);

  readonly addMovie = this.updater((state, movie: Movie) => ({
    movies: [...state.movies, movie],
  }));

  readonly loadMovies = this.effect<void>((trigger$) =>
    trigger$.pipe(
      switchMap(() =>
        this.api.getAll().pipe(
          tapResponse({
            next: (movies) => this.patchState({ movies }),
            error: console.error,
          }),
        ),
      ),
    ),
  );
}
```

- `select` / `selectSignal` - read state.
- `updater` - update state.
- `effect` - side effects.
- `setState`, `patchState`, `get()` and the `state` signal.

### 240: How does ComponentStore compare to SignalStore?

|            | ComponentStore                      | SignalStore                        |
| ---------- | ----------------------------------- | ---------------------------------- |
| Based on   | RxJS (with signal helpers)          | Signals (RxJS optional)            |
| Defined as | Class that extends `ComponentStore` | Function composition with features |
| Reuse      | Inheritance                         | Custom features                    |
| Entities   | Use `@ngrx/entity` by hand          | `withEntities` built in            |
| Status     | Maintained, not the focus           | Recommended for new code           |

### 241: How does `*ngrxLet` handle errors and loading?

It exposes extra context values and supports a `suspense` template:

```html
<ng-container
  *ngrxLet="user$ as user; error as error; complete as complete; suspense: loading"
>
  @if (error) {
  <p>Could not load user</p>
  } @else {
  <p>{{ user.name }}</p>
  }
</ng-container>

<ng-template #loading><app-spinner /></ng-template>
```

The suspense template is shown until the observable emits its first value.

### 242: How is `ngrxPush` different from `async`?

- `async` calls `markForCheck` on each new value. In Zone.js apps that marks the view and the zone triggers change detection. In zoneless apps `markForCheck` also schedules change detection.
- `ngrxPush` was built before Angular had zoneless support. It schedules change detection itself, so it didn't depend on Zone.js.
- `ngrxPush` also accepts plain values, not only observables and promises, and it doesn't throw on `null` or `undefined` input.

With signals and Angular's built-in zoneless support, `selectSignal` is often simpler than both.

### 243: Does NgRx work with zoneless Angular?

Yes. With `provideZonelessChangeDetection()`, signals tell Angular when to update. `store.selectSignal` and SignalStore signals work out of the box. The `async` pipe also works in zoneless apps since it calls `markForCheck`, which schedules change detection. The `strictActionWithinNgZone` check has no meaning there, so leave it off.

### 244: Why do NgRx and `OnPush` work well together?

State is immutable, so when something changes you get a new reference. `OnPush` components only update when inputs change by reference, when an event happens in the component, or when a signal / `async` pipe in the template changes. Since selectors only produce new references when data really changed, `OnPush` components update exactly when they need to.

### 245: How would you organize NgRx files in a feature folder?

A common layout:

```
books/
  data-access/
    books.actions.ts
    books.reducer.ts      // or books.feature.ts with createFeature
    books.selectors.ts    // extra selectors if needed
    books.effects.ts
    books.service.ts
    books.models.ts
  feature/
    books-page.ts
  ui/
    book-card.ts
    book-list.ts
```

For SignalStore:

```
books/
  data-access/
    books.store.ts
    books.service.ts
```

The main point is that state code is grouped by feature, not by type across the whole app.

### 246: What naming conventions are common in NgRx code?

- Action groups: `BooksPageActions`, `BooksApiActions` (named by source).
- Action events: past tense, like `Opened`, `Query Changed`, `Load Success`.
- Selectors: start with `select`, like `selectBooks`. The `prefix-selectors-with-select` lint rule enforces this.
- Effects: named by what they do, like `loadBooks$` or `loadBooks`.
- Stores: `BooksStore`.
- Files: `books.actions.ts`, `books.feature.ts`, `books.effects.ts`, `books.store.ts`.

### 247: What is the facade pattern with NgRx and what are its pros and cons?

A facade is a service that hides the store behind simple methods and signals:

```ts
@Injectable({ providedIn: "root" })
export class BooksFacade {
  private readonly store = inject(Store);
  readonly books = this.store.selectSignal(selectBooks);
  readonly loading = this.store.selectSignal(selectLoading);

  open() {
    this.store.dispatch(BooksPageActions.opened());
  }
}
```

Pros:

- Components don't depend on NgRx directly.
- One place to change if the state setup changes.

Cons:

- It's another layer of code.
- It often turns events into commands, like `loadBooks()`, and if many components call the same method, you lose the "where did this come from" info in the action log.
- It can hide the flow that NgRx is meant to make visible.

If you use a facade, keep its methods named after events (`pageOpened()`), not commands.

### 248: What is the difference between event-style and command-style actions?

- Command style: `[Books] Load Books`, `[Books] Set Books`. The action says what to do.
- Event style: `[Books Page] Opened`, `[Books API] Load Success`. The action says what happened.

NgRx recommends event style. One event can be handled by several reducers and effects, components don't need to know what happens next, and the action log reads like a story of what the user did.

### 249: Why should you avoid dispatching several actions one after another?

```ts
// avoid
this.store.dispatch(loadUser());
this.store.dispatch(loadSettings());
this.store.dispatch(loadNotifications());
```

Each action runs all reducers and selectors, so you get extra work and extra renders in between. It also hides the real event. Dispatch one event instead and let reducers and effects react to it:

```ts
this.store.dispatch(DashboardPageActions.opened());
```

The `avoid-dispatching-multiple-actions-sequentially` lint rule checks for this.

### 250: What is an optimistic update and how do you do it with NgRx Store?

You update the state right away, as if the server call succeeded, and roll back if it fails.

```ts
// reducer
on(TodoActions.toggled, (state, { id }) =>
  adapter.mapOne({ id, map: (t) => ({ ...t, done: !t.done }) }, state)
),
on(TodoApiActions.toggleFailure, (state, { id }) =>
  adapter.mapOne({ id, map: (t) => ({ ...t, done: !t.done }) }, state)
),

// effect
export const toggle = createEffect(
  (actions$ = inject(Actions), api = inject(TodoService)) =>
    actions$.pipe(
      ofType(TodoActions.toggled),
      mergeMap(({ id }) =>
        api.toggle(id).pipe(
          map(() => TodoApiActions.toggleSuccess({ id })),
          catchError(() => of(TodoApiActions.toggleFailure({ id })))
        )
      )
    ),
  { functional: true }
);
```

The UI feels fast, but you need a clear rollback path and a way to tell the user it failed.

### 251: What is a pessimistic update?

You wait for the server to confirm before changing state. The reducer only reacts to the success action. It's simpler and always matches the server, but the user waits. Use it when failure is likely or when the change is important, like payments.

### 252: How do you handle a form submit with NgRx Store and show server errors?

```ts
// component
submit() {
  if (this.form.invalid) return;
  this.store.dispatch(ProfilePageActions.saveClicked({ profile: this.form.getRawValue() }));
}

// reducer
on(ProfilePageActions.saveClicked, (s) => ({ ...s, saving: true, error: null })),
on(ProfileApiActions.saveSuccess, (s, { profile }) => ({ ...s, profile, saving: false })),
on(ProfileApiActions.saveFailure, (s, { error }) => ({ ...s, saving: false, error })),

// effect uses concatMap + catchError
```

The component reads `saving` to disable the button and `error` to show a message. The form values stay in the form until the save succeeds.

### 253: How can you add and remove reducers at runtime?

Inject `ReducerManager`:

```ts
const reducerManager = inject(ReducerManager);

reducerManager.addReducer("reports", reportsReducer);
reducerManager.removeReducer("reports");
```

`provideState` does this for you in most cases. Manual use is rare, for example in plugin systems where features are loaded by name.

### 254: Which NgRx schematics commands are most useful?

```bash
ng generate @ngrx/schematics:store State --root --state-path store
ng generate @ngrx/schematics:feature books/Book --group --creators
ng generate @ngrx/schematics:action books/Book
ng generate @ngrx/schematics:reducer books/Book
ng generate @ngrx/schematics:effect books/Book
ng generate @ngrx/schematics:selector books/Book
ng generate @ngrx/schematics:entity books/Book
ng generate @ngrx/schematics:container books/BooksPage
ng generate @ngrx/schematics:component-store books/Books
```

`--group` puts files in `actions/`, `reducers/` and so on.

### 255: How do you make NgRx the default schematics collection?

`ng add @ngrx/schematics` does it, or you can set it yourself:

```bash
ng config cli.schematicCollections "[\"@ngrx/schematics\", \"@schematics/angular\"]"
```

Then `ng generate feature books/Book` works without the `@ngrx/schematics:` prefix.

### 256: Name some useful rules from `@ngrx/eslint-plugin`.

- `avoid-dispatching-multiple-actions-sequentially`
- `avoid-cyclic-effects` - effect output should not be the same action it listens to.
- `no-dispatch-in-effects` - return actions instead of calling `store.dispatch` in effects.
- `no-effects-in-providers` - effects should be registered with `provideEffects`, not as plain providers.
- `no-store-subscription` - use `async` / signals instead of `subscribe`.
- `no-typed-global-store`
- `prefer-action-creator-in-of-type`
- `prefer-concat-latest-from`
- `on-function-explicit-return-type`
- `good-action-hygiene`
- `prefix-selectors-with-select`

A flat config setup:

```js
// eslint.config.js
const ngrx = require("@ngrx/eslint-plugin/v9");

module.exports = [
  ...ngrx.configs.store,
  ...ngrx.configs.effects,
  ...ngrx.configs.signals,
];
```

### 257: What lint rules exist for `@ngrx/signals`?

- `prefer-protected-state` - warns when `protectedState: false` is used.
- `signal-state-no-arrays-at-root-level` - `signalState` must be an object, not an array.
- `with-state-no-arrays-at-root-level` - same for `withState`.
- `signal-store-feature-should-use-generic-type` - custom features with inputs should be generic so they work with any store.
- `enforce-type-call` - `type` must be called as `type<T>()`, not used as `type<T>`.

### 258: Why can't the root of SignalStore state be an array?

The state is a record whose keys become signals. An array at the root has no named keys, so it can't be turned into `store.someKey()` signals, and `patchState` merges objects. Wrap arrays in an object: `withState({ items: [] as Item[] })`.

### 259: How do you hide sensitive data in DevTools?

Use `actionSanitizer` and `stateSanitizer`:

```ts
provideStoreDevtools({
  maxAge: 25,
  logOnly: !isDevMode(),
  actionSanitizer: (action) =>
    action.type === AuthApiActions.loginSuccess.type
      ? { ...action, token: "***" }
      : action,
  stateSanitizer: (state: any) => ({
    ...state,
    auth: { ...state.auth, token: state.auth?.token ? "***" : null },
  }),
});
```

This only changes what DevTools shows, not the real state.

### 260: What does the `trace` option in DevTools do?

With `trace: true`, DevTools records a stack trace for each action, so you can see which line of code dispatched it. `traceLimit` sets the number of frames. It slows things down a bit, so turn it on only while debugging.

### 261: Should Store DevTools be enabled in production?

Common choices:

- Don't include it in production at all, by only adding the provider in dev builds.
- Include it with `logOnly: true`, so support staff can look at the action log if they have the extension.

Keep in mind that anyone with the extension can see your state in production if DevTools is enabled, so sanitize tokens and personal data.

### 262: Can you use Redux DevTools with SignalStore?

Not with `@ngrx/store-devtools`, which only works with the global store. The community package `@angular-architects/ngrx-toolkit` provides a `withDevtools('storeName')` feature that sends SignalStore state to Redux DevTools:

```ts
import { withDevtools } from "@angular-architects/ngrx-toolkit";

export const BooksStore = signalStore(
  withDevtools("books"),
  withState(initialState),
);
```

### 263: How do you avoid fetching data twice with SSR and NgRx Store?

The server already loaded data into the store. To avoid loading it again in the browser, you transfer state:

- Angular's HTTP transfer cache (on by default with `provideClientHydration()`) reuses GET responses made on the server, so the effect gets the cached response.
- For full control, write the store state into `TransferState` on the server and read it back in a meta-reducer on the client.

The first option is usually enough.

### 264: Where should the auth token live?

The token is often kept in the store so that guards, interceptors and the UI can read it, but think about:

- Sanitize it in DevTools.
- Don't persist it to `localStorage` if you can avoid it (XSS risk). An `HttpOnly` cookie set by the server is safer.
- Clear it on logout with a meta-reducer or reducer.

Many apps keep only `isAuthenticated` and the user profile in the store, and leave the token to cookies.

### 265: Why is putting a `Date` object in state a problem?

`Date` is not a plain serializable value. DevTools and `JSON.stringify` turn it into a string, so after time travel or persistence you get a string instead of a `Date`. It's also mutable, so code can change it in place. Store ISO strings or timestamps and format them in selectors or pipes.

### 266: How do you write a selector that uses data from two features?

Just use selectors from both features as inputs:

```ts
export const selectCartWithProducts = createSelector(
  cartFeature.selectItems,
  productsFeature.selectEntities,
  (items, products) =>
    items.map((item) => ({ ...item, product: products[item.productId] })),
);
```

Put this selector in a shared place or in the feature that needs it.

### 267: What are good rules for dependencies between features?

- A feature's reducer should only handle its own state.
- Reducers can listen to actions from other features (for example, cart clears on `OrderApiActions.placed`).
- Selectors can read other features' selectors, but avoid circular imports.
- A lazy feature shouldn't be required by the root state, because it may not be loaded yet.

### 268: How do you mix store signals with component-only state?

```ts
export class ProductsPage {
  private readonly store = inject(Store);
  readonly products = this.store.selectSignal(selectProducts);
  readonly search = signal("");

  readonly visible = computed(() => {
    const q = this.search().toLowerCase();
    return this.products().filter((p) => p.name.toLowerCase().includes(q));
  });
}
```

Global data comes from the store, the local search box stays in the component.

### 269: Can `store.dispatch` take a signal?

Yes, since NgRx 19 you can pass a function that returns an action. NgRx runs it inside an effect and dispatches again every time the signals it reads change:

```ts
export class BookDetails {
  private readonly store = inject(Store);
  readonly bookId = input.required<string>();

  constructor() {
    this.store.dispatch(() => BookDetailsActions.opened({ id: this.bookId() }));
  }
}
```

When `bookId` changes, a new action is dispatched.

### 270: What does `dispatch` return when you pass a function?

It returns an `EffectRef`. The effect is cleaned up automatically when the injection context (for example the component) is destroyed. You can call `ref.destroy()` to stop it earlier. If you call it outside an injection context, pass `{ injector }` as the second argument.

### 271: How do you use a component input with a factory selector?

A factory selector needs the id when it's created, but an input can change over time. The simplest way is to select the entity map once and look up by id in a `computed`:

```ts
export class BookCard {
  private readonly store = inject(Store);
  readonly id = input.required<string>();

  private readonly entities = this.store.selectSignal(selectBookEntities);
  readonly book = computed(() => this.entities()[this.id()]);
}
```

If the selector does heavy work per id, you can also create it with `selectBookById(this.id())` inside an observable pipeline (`toObservable(this.id).pipe(switchMap((id) => this.store.select(selectBookById(id))))`).

### 272: How do you use the store in a functional route guard?

```ts
export const authGuard: CanActivateFn = () => {
  const store = inject(Store);
  const router = inject(Router);
  return store.select(selectIsLoggedIn).pipe(
    take(1),
    map((loggedIn) => (loggedIn ? true : router.createUrlTree(["/login"]))),
  );
};
```

With signals: `return store.selectSignal(selectIsLoggedIn)() || router.createUrlTree(['/login']);`

### 273: How do you make sure data is loaded before a route activates?

Dispatch a load action and wait until the data is there:

```ts
export const booksLoadedGuard: CanActivateFn = () => {
  const store = inject(Store);
  return store.select(selectBooksLoaded).pipe(
    tap((loaded) => {
      if (!loaded) store.dispatch(BooksGuardActions.loadRequested());
    }),
    filter(Boolean),
    take(1),
  );
};
```

You should also handle the failure case, otherwise the guard can wait forever.

### 274: Should you load data when a component starts or on router navigation?

Both are common:

- **Component init**: dispatch `[Books Page] Opened` in the constructor or `ngOnInit`. Simple and easy to understand.
- **Router-driven**: an effect listens to `routerNavigatedAction` and loads data for certain URLs. The component has no loading logic, but the effect needs to know about URLs.

Component-driven loading is easier to follow, and the action log still shows where it came from. Router-driven fits apps where the URL fully describes what to show.

### 275: How do you keep an error per entity, for example per row?

Keep a map of id to status next to the entities:

```ts
export interface TodosState extends EntityState<Todo> {
  saving: Record<string, 'saving' | 'error' | undefined>;
}

on(TodoActions.saveClicked, (s, { id }) => ({ ...s, saving: { ...s.saving, [id]: 'saving' } })),
on(TodoApiActions.saveFailure, (s, { id }) => ({ ...s, saving: { ...s.saving, [id]: 'error' } })),
on(TodoApiActions.saveSuccess, (s, { todo }) => {
  const { [todo.id]: _, ...rest } = s.saving;
  return adapter.upsertOne(todo, { ...s, saving: rest });
}),
```

### 276: How would you model pagination state?

```ts
export interface ProductsState extends EntityState<Product> {
  page: number;
  pageSize: number;
  total: number;
  status: "idle" | "loading" | "error";
}

export const selectTotalPages = createSelector(
  productsFeature.selectTotal,
  productsFeature.selectPageSize,
  (total, size) => Math.ceil(total / size),
);
```

Page changes are actions like `[Products Page] Page Changed`. The effect reads `page` and `pageSize` with `concatLatestFrom` and loads that page. If the page should be in the URL, read it from router-store instead.

### 277: Where should filtering and sorting happen?

Keep the raw data and the filter/sort options in state, and compute the result in a selector:

```ts
export const selectVisibleProducts = createSelector(
  selectAllProducts,
  selectFilter,
  selectSort,
  (products, filter, sort) =>
    products
      .filter(
        (p) => p.category === filter.category || filter.category === "all",
      )
      .toSorted((a, b) =>
        sort === "price" ? a.price - b.price : a.name.localeCompare(b.name),
      ),
);
```

Don't store the filtered list in state, because then you have two copies of the same data to keep in sync. If filtering is done by the server, the server result is what you store.

### 278: How do you avoid fetching data that is already in the store?

Check in the effect before calling the API:

```ts
export const loadBooks = createEffect(
  (
    actions$ = inject(Actions),
    store = inject(Store),
    api = inject(BooksService),
  ) =>
    actions$.pipe(
      ofType(BooksPageActions.opened),
      concatLatestFrom(() => store.select(selectBooksLoaded)),
      filter(([, loaded]) => !loaded),
      exhaustMap(() =>
        api.getAll().pipe(
          map((books) => BooksApiActions.loadSuccess({ books })),
          catchError(() =>
            of(BooksApiActions.loadFailure({ error: "failed" })),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

You can also store a `loadedAt` timestamp and refetch when it's too old.

### 279: How do you clear a feature's state when the user leaves the page?

Dispatch a "left" action and reset in the reducer:

```ts
export class BooksPage {
  private readonly store = inject(Store);
  constructor() {
    inject(DestroyRef).onDestroy(() =>
      this.store.dispatch(BooksPageActions.left()),
    );
  }
}

on(BooksPageActions.left, () => initialState);
```

If the state is only needed by that page, a component-level SignalStore is often a better fit, since it's destroyed automatically.

### 280: Can a component listen to `Actions` directly, for example to close a dialog on success?

It can:

```ts
inject(Actions)
  .pipe(ofType(ProfileApiActions.saveSuccess), takeUntilDestroyed())
  .subscribe(() => this.dialogRef.close());
```

It works, but it moves logic into the component and depends on action timing. Alternatives are to keep a `saved` flag in state and react to it, or close the dialog in an effect with `dispatch: false`.

### 281: How do HTTP interceptors fit with NgRx effects?

Effects call services that use `HttpClient`, so interceptors run as normal. Interceptors are a good place for adding auth headers, retrying, or global error handling. Effects then only map success or failure to actions. Avoid dispatching actions from interceptors for every request, because it's hard to follow. A single action like `[Http] Unauthorized` on 401 is fine.

### 282: How do you retry a failed request in an effect?

Use `retry` on the inner observable before `catchError`:

```ts
switchMap(() =>
  api.getAll().pipe(
    retry({ count: 3, delay: (_, attempt) => timer(attempt * 1000) }),
    map((books) => BooksApiActions.loadSuccess({ books })),
    catchError((e) => of(BooksApiActions.loadFailure({ error: e.message }))),
  ),
);
```

Only retry safe requests (like GET), and don't retry on errors like 400 or 403 that won't change.

### 283: How do you cancel a request when the user navigates away?

```ts
switchMap(({ id }) =>
  api.getReport(id).pipe(
    map((report) => ReportApiActions.loaded({ report })),
    catchError(() => of(ReportApiActions.failed())),
    takeUntil(actions$.pipe(ofType(routerNavigationAction))),
  ),
);
```

Or listen to a page "left" action instead of every navigation.

### 284: How do you handle a WebSocket with effects?

```ts
export const liveQuotes = createEffect(
  (actions$ = inject(Actions), socket = inject(QuotesSocket)) =>
    actions$.pipe(
      ofType(QuotesPageActions.opened),
      switchMap(() =>
        socket.connect().pipe(
          map((quote) => QuotesSocketActions.quoteReceived({ quote })),
          catchError(() => of(QuotesSocketActions.connectionFailed())),
          takeUntil(actions$.pipe(ofType(QuotesPageActions.left))),
        ),
      ),
    ),
  { functional: true },
);
```

For very frequent messages, consider `bufferTime` and dispatch batches, to avoid running reducers hundreds of times a second.

### 285: Can `createAction` take a function instead of `props`?

Yes. The function receives arguments and returns the props. It's useful for adding default values:

```ts
export const todoAdded = createAction(
  "[Todo Page] Todo Added",
  (title: string, id = crypto.randomUUID()) => ({
    todo: { id, title, done: false },
  }),
);

store.dispatch(todoAdded("Buy milk"));
```

Generating the id in the action creator keeps the reducer pure.

### 286: Can `createActionGroup` events use creator functions too?

Yes, each event can be `props<...>()`, `emptyProps()` or a function:

```ts
export const TodoPageActions = createActionGroup({
  source: "Todo Page",
  events: {
    "Todo Added": (title: string) => ({
      todo: { id: crypto.randomUUID(), title, done: false },
    }),
    Opened: emptyProps(),
  },
});
```

### 287: Can you call `store.select` with a string key?

Yes, `store.select('books')` or `store.select('books', 'list')` still works, but it isn't type safe in a useful way and doesn't support memoized derived data. Use selector functions. The `prefer-selector-in-select` lint rule warns about strings.

### 288: What types do selectors have?

- `MemoizedSelector<State, Result>` - a selector made by `createSelector` or `createFeatureSelector`.
- `MemoizedSelectorWithProps` - old type for props selectors.
- `DefaultProjectorFn<Result>` - default projector type.

You rarely write them by hand, TypeScript infers them. They are useful when you write a function that takes a selector as a parameter:

```ts
function selectCount<T>(selectList: MemoizedSelector<object, T[]>) {
  return createSelector(selectList, (list) => list.length);
}
```

### 289: What makes a good state shape?

- Flat, not deeply nested.
- Normalized for collections (entities by id).
- Only raw data, no values you can compute with selectors.
- Serializable values only.
- Clear status fields (`'idle' | 'loading' | 'loaded' | 'error'`).
- Split by feature, with each feature owning its slice.

### 290: How would you add simple undo to a feature?

Keep past states and handle an undo action in a meta-reducer for that feature:

```ts
export function undoable<S>(
  reducer: ActionReducer<S>,
): ActionReducer<{ past: S[]; present: S }> {
  return (state, action) => {
    const current = state ?? { past: [], present: reducer(undefined, action) };
    if (action.type === EditorActions.undo.type) {
      const previous = current.past.at(-1);
      return previous
        ? { past: current.past.slice(0, -1), present: previous }
        : current;
    }
    const present = reducer(current.present, action);
    return present === current.present
      ? current
      : { past: [...current.past, current.present].slice(-50), present };
  };
}
```

The feature's selectors then read from `present`. Keep the history size limited.

### 291: How can one SignalStore use another SignalStore?

Inject it inside a feature factory. Its signals can then be used in computed signals and methods:

```ts
export const CartStore = signalStore(
  withState({ items: [] as CartItem[] }),
  withProps(() => ({ _auth: inject(AuthStore) })),
  withComputed(({ items, _auth }) => ({
    canCheckout: computed(() => _auth.isLoggedIn() && items().length > 0),
  })),
);
```

Be careful to not create a circular dependency (A injects B and B injects A).

### 292: How do you call one store method from another?

Methods defined in an earlier `withMethods` are on the `store` argument. To call a method from the same `withMethods` block, define it as a local function first:

```ts
withMethods((store, api = inject(BooksService)) => {
  async function load() {
    patchState(store, { books: await api.getAll() });
  }

  return {
    load,
    async remove(id: string) {
      await api.remove(id);
      await load();
    },
  };
});
```

Or split them into two `withMethods` calls.

### 293: Does the order of features in `signalStore` matter?

Yes. Each feature can only see members from features before it. If `withComputed` uses `books`, `withState` with `books` must come first. Hooks usually go last, since they often call methods. Later features can also override members with the same name, so watch out for name clashes.

### 294: How would you move from ComponentStore to SignalStore?

1. Move the state interface to `withState(initialState)`.
2. Turn selectors into `withComputed` with `computed`.
3. Turn `updater`s into methods that call `patchState`.
4. Turn `effect`s into `rxMethod` (the pipe usually stays the same).
5. Move constructor logic to `withHooks({ onInit })`.
6. Replace `this.select(...)` observable usage in templates with signal calls.

```ts
// before
readonly loadMovies = this.effect<void>((t$) => t$.pipe(switchMap(...)));

// after
loadMovies: rxMethod<void>(pipe(switchMap(...))),
```

You can migrate one store at a time, since both can live in the same app.

### 295: How do you migrate an NgModule-based NgRx setup to standalone providers?

| NgModule                                | Standalone                             |
| --------------------------------------- | -------------------------------------- |
| `StoreModule.forRoot(reducers, config)` | `provideStore(reducers, config)`       |
| `StoreModule.forFeature(feature)`       | `provideState(feature)`                |
| `EffectsModule.forRoot([A])`            | `provideEffects(A)`                    |
| `EffectsModule.forFeature([B])`         | `provideEffects(B)` in route providers |
| `StoreDevtoolsModule.instrument()`      | `provideStoreDevtools()`               |
| `StoreRouterConnectingModule.forRoot()` | `provideRouterStore()`                 |

The rest of the code (actions, reducers, selectors, effects) stays the same.

### 296: How do you share selectors between the global store and a SignalStore?

A SignalStore can inject `Store` and use `selectSignal`:

```ts
export const OrdersStore = signalStore(
  withState({ orders: [] as Order[] }),
  withProps(() => ({
    _userId: inject(Store).selectSignal(selectCurrentUserId),
  })),
  withMethods((store, api = inject(OrdersService)) => ({
    load: rxMethod<string | null>(
      pipe(
        filter(Boolean),
        switchMap((userId) =>
          api.getForUser(userId).pipe(
            tapResponse({
              next: (orders) => patchState(store, { orders }),
              error: console.error,
            }),
          ),
        ),
      ),
    ),
  })),
  withHooks({ onInit: (store) => store.load(store._userId) }),
);
```

This lets you keep shared state in the global store while features use SignalStore.

### 297: What should you check in a code review of an action file?

- Actions are named as events with a clear source.
- No generic "set" actions used from many places.
- Payloads are small and serializable.
- `createActionGroup` is used for related events.
- No duplicate types.

### 298: How do you keep a selector from re-running for big lists when only one item changes?

The selector will re-run, because the list reference changes. To keep the cost low:

- Select by id from the entity map for single items instead of searching the list.
- Split heavy work into smaller selectors, so only the affected parts recompute.
- Keep presentational components `OnPush` and use `track` by id in `@for`, so Angular only re-renders the changed row.

### 299: What's the difference between `setAll` / `setAllEntities` and `addMany` / `addEntities`?

- `setAll` / `setAllEntities` replace the whole collection. Items not in the new list are removed.
- `addMany` / `addEntities` add new items and keep existing ones. Items with ids that already exist are not changed.

Use `setAll` for a full reload and `addMany` for "load more" style paging.

### 300: How do you decide between NgRx Store, SignalStore, and a simple signal service for a new feature?

- **Simple service with `signal()`** - small, local state with little logic.
- **SignalStore** - feature or component state with computed values, async methods, entities, and reuse through custom features.
- **NgRx Store** - state shared across many parts of a big app, when the team wants an event log, strict separation of side effects, and full DevTools time travel.

Start simple and move up when the needs are clear. It's also fine to combine them in one app.

## Advanced Questions

### 301: How does NgRx Store work internally?

The main pieces are:

- **`ActionsSubject`** - a `BehaviorSubject` of actions. `store.dispatch` calls `next` on it.
- **`ReducerManager`** - holds all reducers (root and features), combines them with `combineReducers`, applies meta-reducers, and emits the combined reducer whenever features are added or removed.
- **`State`** - listens to `ActionsSubject` and the reducer stream, runs each action through the current reducer, and keeps the result in a `BehaviorSubject`. It also exposes the state as a signal.
- **`ScannedActionsSubject`** - after state is updated, the action is pushed here. Effects' `Actions` stream is built on it.
- **`Store`** - the public API. It's an observable of state with `dispatch`, `select` and `selectSignal`.

Roughly, `State` does this:

```ts
actions$
  .pipe(observeOn(queueScheduler))
  .pipe(withLatestFrom(reducer$))
  .pipe(
    scan(
      ({ state }, [action, reducer]) => ({
        state: reducer(state, action),
        action,
      }),
      seed,
    ),
  )
  .subscribe(({ state, action }) => {
    this.next(state);
    scannedActions.next(action);
  });
```

### 302: Why does `State` use `observeOn(queueScheduler)`?

If an action is dispatched while another action is still being reduced (for example from a subscriber reacting to the new state), the `queueScheduler` puts it in a queue instead of running it in the middle. Each action is fully reduced and published before the next one starts. This keeps state updates in order and avoids nested reductions.

### 303: Why do effects listen to `ScannedActionsSubject` and not `ActionsSubject`?

`ScannedActionsSubject` only emits an action after the reducers have handled it. If effects listened to `ActionsSubject`, they could see the action before the state was updated, and reading state in an effect would give old values. Using the scanned stream guarantees the order "reduce first, then effects".

### 304: How is `selectSignal` implemented?

The `State` service keeps the state in a signal (created from its observable). `selectSignal` is basically:

```ts
selectSignal<K>(selector: (state: T) => K, options?: SelectSignalOptions<K>): Signal<K> {
  return computed(() => selector(this.state()), options);
}
```

So it gets all the benefits of `computed`: lazy evaluation, caching, and glitch-free updates. Because NgRx selectors are also memoized, a projector doesn't run again unless its inputs changed, even when the `computed` re-evaluates.

### 305: How does `createSelector` memoization work in detail?

`createSelector` is built from `createSelectorFactory(defaultMemoize)`. It creates two memoized layers:

1. A memoized projector: it remembers the last arguments (the input selector results) and the last result.
2. A memoized selector: it remembers the last state argument, so calling it twice with the same state object returns the cached value without running the input selectors.

When the state changes, input selectors run, and if their results are the same by reference, the projector is skipped. `defaultMemoize` only keeps one previous call, so a selector shared by places that pass different states (or a factory selector shared with different ids) keeps missing the cache.

### 306: How does `resultMemoize` differ from the default memoization?

The default checks if the arguments changed. `resultMemoize` also runs the projector, but then compares the new result with the previous result using your comparison function, and returns the previous reference if they are equal. This is useful when inputs change often but the output usually stays the same in content:

```ts
const createArraySelector = createSelectorFactory((projector) =>
  resultMemoize(
    projector,
    (a: unknown[], b: unknown[]) =>
      a.length === b.length && a.every((x, i) => x === b[i]),
  ),
);
```

The projector still runs, so this saves rendering, not computation.

### 307: How do `select`'s `distinctUntilChanged` and selector memoization work together?

Memoization makes the selector return the same reference when nothing relevant changed. `store.select` then uses `distinctUntilChanged`, which compares by reference, so it doesn't emit a new value. If a selector returns a new object each time (because of a bad input selector), memoization fails and `distinctUntilChanged` can't help either, so subscribers get new values on every action.

### 308: How does `createActionGroup` build its types?

It uses TypeScript template literal types and mapped types. The event name `'Load Success'` is converted to the key `loadSuccess` at the type level, and the type string to `` `[${Source}] ${EventName}` ``. That's why a typo gives a compile error and why `.type` is a literal type.

It also adds compile-time checks: event names can't be empty, can't collide after camel casing, and can't contain characters that don't make valid keys.

### 309: Why does `createFeature` not allow optional properties at the root of the feature state?

`createFeature` creates a selector for each key in the initial state type. For an optional property, the key may not exist in the object at runtime, and the selector generation logic is based on the keys present in the initial state. To prevent selectors that silently don't exist, the types reject optional root properties. Use `T | null` instead of `T?`:

```ts
interface State {
  selectedId: string | null; // good
  // selectedId?: string;    // causes a type error with createFeature
}
```

### 310: Why is `on-function-explicit-return-type` recommended?

Without an explicit return type, TypeScript doesn't check for extra properties in the object the `on` handler returns. A typo like `{ ...state, laoding: true }` compiles, adds a new key, and the real `loading` never changes.

```ts
on(BooksPageActions.opened, (state): BooksState => ({
  ...state,
  loading: true,
}));
```

With the explicit return type, the typo becomes a compile error.

### 311: How are `on` handlers combined when several handle the same action?

`createReducer` builds a map from action type to handlers. If two `on` calls list the same action, both run in the order they appear, and the second one receives the state returned by the first. The `avoid-duplicate-actions-in-reducer` lint rule warns about this, because it's usually a mistake.

### 312: How does `combineReducers` handle features and what does `ActionReducerMap` mean?

`ActionReducerMap<T>` is an object type where each key of state `T` maps to a reducer for that key:

```ts
export interface AppState {
  auth: AuthState;
  settings: SettingsState;
}

export const reducers: ActionReducerMap<AppState> = {
  auth: authReducer,
  settings: settingsReducer,
};
```

`combineReducers` turns this into one reducer that calls each child reducer with its slice. If no slice changed (all children returned the same reference), it returns the original state object, which keeps memoization working at the root level.

### 313: How do effects get registered and run internally?

- `provideEffects` collects effect sources (classes or objects of functional effects) and passes them to `EffectSources`.
- `EffectSources` takes every property created with `createEffect`, merges them, applies the error handler, and handles `OnRunEffects`, `OnIdentifyEffects` and `OnInitEffects`.
- `EffectsRunner` subscribes to the merged stream and dispatches emitted actions to the store (unless `dispatch: false`).

Effect instances are deduplicated by their identifier, so the same class registered twice doesn't run twice.

### 314: What is `OnRunEffects` used for?

It lets an effects class control when its effects are active. `ngrxOnRunEffects` receives the merged effects stream and returns a new one:

```ts
@Injectable()
export class LiveDataEffects implements OnRunEffects {
  private readonly actions$ = inject(Actions);

  ngrxOnRunEffects(resolvedEffects$: Observable<EffectNotification>) {
    return this.actions$.pipe(
      ofType(AuthApiActions.loginSuccess),
      exhaustMap(() =>
        resolvedEffects$.pipe(
          takeUntil(this.actions$.pipe(ofType(AuthActions.logout))),
        ),
      ),
    );
  }
}
```

All effects in this class only run while the user is logged in.

### 315: What is `OnIdentifyEffects` for?

By default, NgRx treats every instance of the same effects class as the same, and only runs it once. If you really need several instances (for example one per tenant, created with different config), implement `ngrxOnIdentifyEffects()` and return a unique key per instance. It's rarely needed.

### 316: What happens if you provide the same effects class in two lazy routes?

Effects are deduplicated by class (or by identifier for functional effects within the same source object), so it runs once. This means you can safely list shared effects in several route providers. But note that effects are not stopped when a route's injector stays alive, so the effect keeps running even after you leave the route.

### 317: How do you handle errors in an effect without the default error handler?

Set `useEffectsErrorHandler: false` and handle resubscription yourself:

```ts
export const liveFeed = createEffect(
  (feed = inject(FeedService)) =>
    feed.connect().pipe(
      map((msg) => FeedActions.messageReceived({ msg })),
      retry({
        delay: (error, attempt) => timer(Math.min(30000, 1000 * 2 ** attempt)),
      }),
    ),
  { functional: true, useEffectsErrorHandler: false },
);
```

This gives you exponential backoff and no limit on retries, instead of the default 10 instant resubscriptions.

### 318: What can cause memory leaks in effects?

- Long-lived inner observables with `mergeMap` that never complete (websockets, intervals). Each new action adds another subscription.
- Effects in lazy features that keep listening after the feature is no longer used.
- Subscribing manually inside an effect (`tap(() => something$.subscribe())`).

Fixes: use `switchMap` or `exhaustMap` for long-lived streams, end them with `takeUntil` on a stop action, and never subscribe inside an operator.

### 319: How do you deal with race conditions when the same action is handled with different ids?

`switchMap` cancels requests for a different id, which is wrong when each id is independent. Group by id and use `switchMap` inside each group:

```ts
export const loadDetails = createEffect(
  (actions$ = inject(Actions), api = inject(ItemsService)) =>
    actions$.pipe(
      ofType(ItemActions.detailsRequested),
      groupBy(({ id }) => id),
      mergeMap((group$) =>
        group$.pipe(
          switchMap(({ id }) =>
            api.details(id).pipe(
              map((details) => ItemApiActions.detailsLoaded({ id, details })),
              catchError(() => of(ItemApiActions.detailsFailed({ id }))),
            ),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

Requests for the same id cancel each other, while different ids run in parallel. For many ids, add a `duration` to `groupBy` so groups are cleaned up.

### 320: How do you test effects with marble diagrams?

With RxJS `TestScheduler`:

```ts
import { TestScheduler } from "rxjs/testing";

let scheduler: TestScheduler;
beforeEach(() => {
  scheduler = new TestScheduler((actual, expected) =>
    expect(actual).toEqual(expected),
  );
});

it("maps opened to loadSuccess", () => {
  scheduler.run(({ hot, cold, expectObservable }) => {
    const actions$ = hot("-a", { a: BooksPageActions.opened() });
    const api = {
      getAll: () => cold("--b|", { b: [book] }),
    } as unknown as BooksService;

    expectObservable(loadBooks(actions$ as any, api)).toBe("---c", {
      c: BooksApiActions.loadSuccess({ books: [book] }),
    });
  });
});
```

Marble tests make timing and cancellation behavior easy to check.

### 321: How do you test a debounced effect with `TestScheduler`?

Inside `scheduler.run`, time-based operators like `debounceTime` use virtual time automatically:

```ts
scheduler.run(({ hot, cold, expectObservable }) => {
  const actions$ = hot("-a-b 300ms -", {
    a: BooksPageActions.queryChanged({ query: "n" }),
    b: BooksPageActions.queryChanged({ query: "ng" }),
  });
  const api = { search: (q: string) => cold("-r|", { r: [book] }) } as any;

  expectObservable(search(actions$ as any, api)).toBe("---- 299ms -s", {
    s: BooksApiActions.searchSuccess({ books: [book] }),
  });
});
```

Only the last query passes through the debounce, which is what you want to prove.

### 322: How would you test that `exhaustMap` ignores clicks while a request runs?

```ts
scheduler.run(({ hot, cold, expectObservable, expectSubscriptions }) => {
  const actions$ = hot("-a-a-a", {
    a: LoginPageActions.submitted({ credentials }),
  });
  const response = cold("---u|", { u: user });
  const auth = { login: () => response } as any;

  expectObservable(login(actions$ as any, auth)).toBe("----s-", {
    s: AuthApiActions.loginSuccess({ user }),
  });
  expectSubscriptions(response.subscriptions).toBe(["-^---!"]);
});
```

The second and third clicks happen while the first request is running, so they don't cause new subscriptions.

### 323: Do runtime checks affect production performance?

No. Runtime checks are only active in development mode (`isDevMode()`). In production builds they're skipped. In development, `strictStateImmutability` deep-freezes state and actions, which costs a bit of time on big states, but it finds mutation bugs early.

### 324: What problems can `strictStateImmutability` cause with third-party libraries?

The check freezes the state objects. If you pass state objects to a library that mutates its input (some charts, grids, or date libraries), you get `Cannot assign to read only property` errors in development. The fix is to give the library a copy (`structuredClone(data)` or `[...data]`), not to turn the check off.

### 325: How do you keep selectors fast in a store with a lot of state?

- Use narrow input selectors so projectors only depend on what they need.
- Keep selector chains shallow and reusable.
- Avoid selectors that take the whole state as input.
- For expensive work, make sure the inputs are stable references (normalized state helps).
- Use factory selectors with care, they create new memoization each time.
- Measure with the Angular DevTools profiler before optimizing.

### 326: How do you model relationships between entities?

Use separate entity collections that reference each other by id:

```ts
interface Post {
  id: string;
  authorId: string;
  title: string;
}
interface Comment {
  id: string;
  postId: string;
  text: string;
}

export interface BlogState {
  posts: EntityState<Post>;
  authors: EntityState<Author>;
  comments: EntityState<Comment>;
}
```

When the API returns nested data, split it in the effect or reducer before saving. Libraries like `normalizr` can help, or write a small function per endpoint.

### 327: How do you put related data back together for the UI?

Use selectors that combine collections:

```ts
export const selectPostsWithAuthors = createSelector(
  selectAllPosts,
  selectAuthorEntities,
  (posts, authors) => posts.map((p) => ({ ...p, author: authors[p.authorId] })),
);
```

This creates new objects each time posts or authors change, so keep it close to where it's used and use `track` by id in templates to keep rendering cheap.

### 328: How do you handle many-to-many relationships?

Store a join collection, or arrays of ids on one side:

```ts
interface Student {
  id: string;
  name: string;
}
interface Course {
  id: string;
  title: string;
}
interface Enrollment {
  id: string;
  studentId: string;
  courseId: string;
}

export const selectCoursesForStudent = (studentId: string) =>
  createSelector(
    selectAllEnrollments,
    selectCourseEntities,
    (enrollments, courses) =>
      enrollments
        .filter((e) => e.studentId === studentId)
        .map((e) => courses[e.courseId])
        .filter((c): c is Course => !!c),
  );
```

The join collection makes adding and removing links simple, since you only touch one entity.

### 329: How do you memoize a factory selector per id?

Cache the created selectors in a `Map`:

```ts
const cache = new Map<string, MemoizedSelector<object, Book | undefined>>();

export const selectBookById = (id: string) => {
  let selector = cache.get(id);
  if (!selector) {
    selector = createSelector(selectBookEntities, (entities) => entities[id]);
    cache.set(id, selector);
  }
  return selector;
};
```

Now every component asking for the same id shares one selector and one cache. For a large number of ids, use an LRU cache or call `release()` and remove unused entries.

### 330: How would you design state for a list with virtual scrolling and lazy loaded pages?

- Keep items in an entity collection.
- Keep a map of page number to page status (`'loading' | 'loaded' | 'error'`) and the ids for each page.
- When the viewport needs a range, dispatch an action with the page numbers. The effect loads pages that are not loaded or loading, with `mergeMap` (or grouped `switchMap`).
- A selector builds the visible slice from ids, with placeholders for pages still loading.

This keeps the data normalized and avoids loading the same page twice.

### 331: Why should you avoid calling functions in templates that compute from store data?

Template function calls run on every change detection cycle. If they filter or map lists, they repeat the work again and again. Use a memoized selector or a `computed` signal instead. Both only recompute when their inputs change.

```ts
// avoid: {{ getTotal(items()) }}
readonly total = computed(() => this.items().reduce((s, i) => s + i.price, 0));
```

### 332: What are batch actions and when are they useful?

A batch action carries several changes at once, like `[Sync] Changes Received` with a list of creates, updates and deletes. Benefits:

- Reducers run once for many changes.
- Selectors and components update once.

The downside is that the action log is less detailed. A meta-reducer that unpacks a generic "batch" action into many actions is possible, but usually a domain-specific batch event is cleaner.

### 333: How is NgRx related to event sourcing?

In event sourcing, you store a list of events and build the current state by replaying them. NgRx works in a similar way on the client: actions are events, reducers build state from them, and DevTools can replay them. The difference is that NgRx doesn't keep events after a refresh, and the state is the main thing you keep. Thinking of actions as events (not commands) brings you closer to this model and makes the action log useful.

### 334: Show a more complete undo/redo meta-reducer.

```ts
interface History<S> {
  past: S[];
  present: S;
  future: S[];
}

export function undoRedo<S>(
  reducer: ActionReducer<S>,
  limit = 100,
): ActionReducer<History<S>> {
  const initial: History<S> = {
    past: [],
    present: reducer(undefined, { type: "@@init" }),
    future: [],
  };

  return (state = initial, action) => {
    const { past, present, future } = state;

    switch (action.type) {
      case HistoryActions.undo.type: {
        if (!past.length) return state;
        return {
          past: past.slice(0, -1),
          present: past[past.length - 1],
          future: [present, ...future],
        };
      }
      case HistoryActions.redo.type: {
        if (!future.length) return state;
        return {
          past: [...past, present],
          present: future[0],
          future: future.slice(1),
        };
      }
      default: {
        const next = reducer(present, action);
        if (next === present) return state;
        return {
          past: [...past, present].slice(-limit),
          present: next,
          future: [],
        };
      }
    }
  };
}

provideState("editor", undoRedo(editorReducer));
```

Each history entry keeps structural sharing with the others, so memory use is lower than it looks. Still, keep the limit reasonable.

### 335: How do you sync state between browser tabs?

Use `BroadcastChannel` in effects:

```ts
const channel = new BroadcastChannel("cart");

export const broadcastCart = createEffect(
  (actions$ = inject(Actions)) =>
    actions$.pipe(
      ofType(CartActions.itemAdded, CartActions.itemRemoved),
      filter((action) => !(action as any).fromOtherTab),
      tap((action) => channel.postMessage(action)),
    ),
  { functional: true, dispatch: false },
);

export const receiveCart = createEffect(
  () =>
    fromEvent<MessageEvent>(channel, "message").pipe(
      map((event) => ({ ...event.data, fromOtherTab: true })),
    ),
  { functional: true },
);
```

The `fromOtherTab` flag stops the action bouncing back and forth. Only send serializable actions. Another option is listening to the `storage` event if you already save state in `localStorage`.

### 336: How do you transfer NgRx Store state from server to client with `TransferState`?

```ts
const STATE_KEY = makeStateKey<any>('ngrx-state');

// server: save state after rendering
export function provideServerStateTransfer() {
  return provideEnvironmentInitializer(() => {
    const transferState = inject(TransferState);
    const store = inject(Store);
    transferState.onSerialize(STATE_KEY, () => {
      let state;
      store.pipe(take(1)).subscribe((s) => (state = s));
      return state;
    });
  });
}

// browser: meta-reducer that loads the transferred state on init
export function hydrationMetaReducer(transferState: TransferState) {
  return (reducer: ActionReducer<any>): ActionReducer<any> => (state, action) => {
    if (action.type === INIT && transferState.hasKey(STATE_KEY)) {
      const saved = transferState.get(STATE_KEY, null);
      transferState.remove(STATE_KEY);
      return reducer(saved, action);
    }
    return reducer(state, action);
  };
}

// browser config
{
  provide: META_REDUCERS,
  deps: [TransferState],
  useFactory: hydrationMetaReducer,
  multi: true,
}
```

Make sure the state is serializable, and don't transfer secrets, since it ends up in the HTML.

### 337: How would you share NgRx state between micro-frontends?

Options:

- **Shared singleton store**: with Module Federation or Native Federation, share `@ngrx/store` as a singleton so all remotes use one `Store` instance. Each remote adds its own features with `provideState`. This needs strict version alignment.
- **Separate stores with events**: each micro-frontend has its own store, and they communicate through a small event bus (custom events, `BroadcastChannel`).
- **Shared data in the URL or backend**: avoid shared client state where possible.

Sharing one store couples the apps tightly. Separate stores keep teams independent but need clear contracts for events.

### 338: Can an app have more than one global `Store`?

It shouldn't. `provideStore` should be called once at the root. Calling it again in a lazy route creates a separate store in that injector, which is confusing and breaks DevTools. The `no-multiple-global-stores` lint rule catches injecting `Store` more than once in a class. For extra state containers, use `provideState` for features, or SignalStore for local state.

### 339: How does `provideState` work with lazy loaded routes behind the scenes?

`provideState` returns environment providers. When the route's environment injector is created, an initializer runs that calls `ReducerManager.addFeature` with the reducer. `ReducerManager` builds a new combined reducer and dispatches `@ngrx/store/update-reducers` with the new feature keys, so the new feature reducer sets its initial state. From then on the feature is part of the global state.

### 340: In what order should you register `provideState` and `provideEffects` for a lazy feature?

Put `provideState` before `provideEffects`:

```ts
providers: [provideState(booksFeature), provideEffects(booksEffects)];
```

If effects start first and react to an action right away (like `ngrxOnInitEffects`, or an action in the same tick), reading the feature state with selectors could fail or return `undefined` because the reducer isn't registered yet.

### 341: How do `provideStore` and the other `provide*` functions work in DI?

They return `EnvironmentProviders` created with `makeEnvironmentProviders`. This means they can only be used in environment injectors (application config and route `providers`), not in component `providers`. They register services like `Store`, `State`, `ReducerManager`, and use `provideEnvironmentInitializer` to set up features and effects when the injector is created.

### 342: How do you use NgRx inside an Angular library?

- Add `@ngrx/*` as `peerDependencies`, not `dependencies`, so the app controls the version and there's only one copy.
- Export a provider function from the library that the app calls:

```ts
export function provideNotifications(): EnvironmentProviders {
  return makeEnvironmentProviders([
    provideState(notificationsFeature),
    provideEffects(notificationsEffects),
  ]);
}
```

- Export public action groups and selectors from the library's public API, and keep internals private.
- For SignalStore based libraries, just export the store or a provider function.

### 343: How does `signalStore` build the store class?

`signalStore(...features)` returns a class. When Angular creates an instance:

1. It starts with an empty inner store: a state source, an empty `stateSignals`, `props`, `methods` and hooks.
2. It runs each feature in order. Each feature is a function that takes the inner store and returns a new inner store with more members.
3. At the end, it copies the public (non `_`) state signals, props and methods onto the class instance.
4. It runs the `onInit` hooks and registers `onDestroy` hooks with `DestroyRef`.

All of this happens in the injection context of the store, so features can call `inject()`.

### 344: What is `STATE_SOURCE` and how does `patchState` use it?

`STATE_SOURCE` is a symbol key on the store that points to the writable state behind it. The public state members are read-only signals derived from it. `patchState` takes the store, reads `STATE_SOURCE`, applies the partial updates and updaters, and writes the new values.

In current versions the state source holds a separate writable signal per root key, so updating one property doesn't notify signals that only depend on others. This is also what makes `withLinkedState` possible, since a linked signal can be one of those slots.

### 345: How are DeepSignals implemented?

A DeepSignal is the original signal wrapped in a `Proxy`. When you access a property like `state.user.name`, the proxy checks if the current value has that key and is a plain object, and if so lazily creates a `computed(() => source().name)` and caches it. That's why nested signals cost nothing until you read them.

### 346: Why are DeepSignals only created for plain objects?

For arrays, `Map`, `Set`, `Date` and class instances, turning properties into signals would be confusing or would clash with built-in members (like `array.length` or `map.get`). So only plain object records become deep signals. Arrays are just signals of arrays: `store.items()` works, but `store.items[0]` does not.

### 347: How does protected state work at the type and runtime level?

At the type level, the store's public type doesn't match `WritableStateSource`, so `patchState(store, ...)` from outside doesn't compile. Inside `withMethods`, the `store` argument is typed as writable.

The protection is mainly enforced by TypeScript. You could cast the store to `any` and force an update, but that defeats the whole point and the lint rules and code review should catch it. `unprotected()` from `@ngrx/signals/testing` is the supported way to get a writable view, and it's meant for tests only.

### 348: How do `getState` and `watchState` work?

- `getState(store)` reads the full state from the state source. Since it reads signals, it is tracked when called in a reactive context.
- `watchState(store, watcher)` registers the watcher with the state source. Every time `patchState` writes, the watchers are called synchronously with the new state. It's used for things like logging and persistence where you want to see every change.

`watchState` returns a `{ destroy }` object, and it's cleaned up when the injection context it was created in is destroyed.

### 349: When should you use `watchState` and when `effect`?

- `effect` runs asynchronously, after change detection-related scheduling, and only once for several synchronous changes. It sees the final value. Good for syncing to the DOM or to outside APIs where intermediate values don't matter.
- `watchState` runs synchronously for every `patchState` call. Good for logging every change, undo history, or DevTools style tracking.

If you write `patchState(store, {a: 1}); patchState(store, {b: 2});`, `watchState` fires twice and `effect` fires once.

### 350: Does SignalStore freeze state?

Yes, in development mode, state objects passed to `patchState` (and the initial state) are deep-frozen with `Object.freeze`. If you mutate state by mistake (like `store.items().push(x)`), you get an error in development instead of a silent bug. In production it's skipped for performance.

### 351: How do you type a custom feature that needs state, props and methods from the host store?

```ts
export function withAutoSave<State extends object>() {
  return signalStoreFeature(
    {
      state: type<State>(),
      props: type<{ _storageKey: string }>(),
      methods: type<{ onSaved(): void }>(),
    },
    withHooks({
      onInit(store) {
        watchState(store, (state) => {
          localStorage.setItem(store._storageKey, JSON.stringify(state));
          store.onSaved();
        });
      },
    }),
  );
}
```

The feature compiles only if it's used in a store that has `_storageKey` and `onSaved`. The `signal-store-feature-should-use-generic-type` lint rule asks for the `State` generic so the feature works with any state shape.

### 352: How do you write a custom feature that takes a config, like `withEntities` does?

```ts
export function withPagination(config: { pageSize: number }) {
  return signalStoreFeature(
    withState({ page: 1, pageSize: config.pageSize, total: 0 }),
    withComputed(({ page, pageSize, total }) => ({
      totalPages: computed(() => Math.max(1, Math.ceil(total() / pageSize()))),
      hasNext: computed(() => page() * pageSize() < total()),
    })),
    withMethods((store) => ({
      nextPage() {
        if (store.hasNext()) patchState(store, (s) => ({ page: s.page + 1 }));
      },
      setTotal(total: number) {
        patchState(store, { total });
      },
    })),
  );
}

export const ProductsStore = signalStore(withPagination({ pageSize: 20 }));
```

### 353: How do you make a custom feature with a named collection prefix?

Use template literal types to build member names from the collection name:

```ts
type NamedCallState<C extends string> = {
  [K in `${C}CallState`]: "init" | "loading" | "loaded" | { error: string };
};

export function withCallState<C extends string>(config: { collection: C }) {
  const key = `${config.collection}CallState` as const;

  return signalStoreFeature(
    withState({ [key]: "init" } as NamedCallState<C>),
    withComputed((store) => {
      const callState = (store as Record<string, Signal<unknown>>)[key];
      return {
        [`${config.collection}Loading`]: computed(
          () => callState() === "loading",
        ),
      } as { [K in `${C}Loading`]: Signal<boolean> };
    }),
  );
}

export const OrdersStore = signalStore(withCallState({ collection: "orders" }));
// store.ordersCallState(), store.ordersLoading()
```

You need a few type casts inside the feature, but the public API is fully typed.

### 354: How would you build an undo/redo feature for SignalStore?

A simple and predictable way is to save a snapshot before each change you want to be undoable. The feature keeps `_past` and `_future` stacks and gives the host store a private `_record()` method to call before it changes state:

```ts
export function withUndoRedo<State extends object>(maxHistory = 50) {
  return signalStoreFeature(
    { state: type<State>() },
    withState({ _past: [] as State[], _future: [] as State[] }),
    withComputed(({ _past, _future }) => ({
      canUndo: computed(() => _past().length > 0),
      canRedo: computed(() => _future().length > 0),
    })),
    withMethods((store) => {
      const snapshot = (): State => {
        const { _past, _future, ...rest } = getState(store);
        return rest as unknown as State;
      };

      return {
        _record() {
          const current = snapshot();
          patchState(store, (s) => ({
            _past: [...s._past, current].slice(-maxHistory),
            _future: [],
          }));
        },
        undo() {
          const previous = store._past().at(-1);
          if (!previous) return;
          const current = snapshot();
          patchState(store, (s) => ({
            ...previous,
            _past: s._past.slice(0, -1),
            _future: [current, ...s._future],
          }));
        },
        redo() {
          const next = store._future()[0];
          if (!next) return;
          const current = snapshot();
          patchState(store, (s) => ({
            ...next,
            _past: [...s._past, current],
            _future: s._future.slice(1),
          }));
        },
      };
    }),
  );
}

export const EditorStore = signalStore(
  withState({ text: "", fontSize: 14 }),
  withUndoRedo<{ text: string; fontSize: number }>(),
  withMethods((store) => ({
    setText(text: string) {
      store._record();
      patchState(store, { text });
    },
  })),
);
```

Snapshots share unchanged objects with each other (structural sharing), so memory use stays reasonable. An automatic version can use `watchState`, but then you have to skip the writes made by undo and redo themselves. The community `@angular-architects/ngrx-toolkit` has a ready-made `withUndoRedo` if you don't want to maintain your own.

### 355: How would you build a feature that syncs SignalStore state to `localStorage`?

```ts
export function withStorageSync<State extends object>(key: string) {
  return signalStoreFeature(
    { state: type<State>() },
    withHooks({
      onInit(store) {
        if (typeof localStorage === "undefined") return; // SSR
        const saved = localStorage.getItem(key);
        if (saved) {
          patchState(store, JSON.parse(saved) as Partial<State>);
        }
        watchState(store, (state) => {
          localStorage.setItem(key, JSON.stringify(state));
        });
      },
    }),
  );
}

export const SettingsStore = signalStore(
  { providedIn: "root" },
  withState({ theme: "light", language: "en" }),
  withStorageSync("settings"),
);
```

Check `isPlatformBrowser` instead of `typeof localStorage` if you want to follow Angular conventions. Also think about versioning saved data, since old saved shapes can break newer code.

### 356: Why does `withFeature` exist when `signalStoreFeature` already has inputs?

Inputs make a feature depend on specific member names in the host store (like `load()`), which makes it less reusable. `withFeature` lets the host pass what it has as normal arguments:

```ts
// generic feature, knows nothing about the host
export function withEntityLoader<E>(loader: (id: string) => Promise<E>) {
  return signalStoreFeature(
    withState({ entity: null as E | null }),
    withMethods((store) => ({
      async loadEntity(id: string) {
        patchState(store, { entity: await loader(id) });
      },
    })),
  );
}

// host
signalStore(
  withMethods((store, api = inject(UsersApi)) => ({
    fetchUser: (id: string) => api.get(id),
  })),
  withFeature((store) => withEntityLoader((id) => store.fetchUser(id))),
);
```

### 357: How does `withLinkedState` work with an explicit `linkedSignal`?

When you need the previous value, return a `linkedSignal` with `source` and `computation`:

```ts
withLinkedState(({ options }) => ({
  selectedOption: linkedSignal<Option[], Option | null>({
    source: options,
    computation: (newOptions, previous) => {
      // keep the current selection if it still exists
      const kept = newOptions.find((o) => o.id === previous?.value?.id);
      return kept ?? newOptions[0] ?? null;
    },
  }),
}));
```

The linked signal becomes part of the store state, so `patchState(store, { selectedOption })` and `getState` work with it.

### 358: What are the trade-offs of keeping a `resource` in SignalStore instead of state?

Pros:

- The resource tracks loading, error and value for you.
- It refetches when its params change, and cancels older requests.

Cons:

- The value is not in the state, so `getState`, `watchState`, DevTools features, and persistence don't see it.
- You can't update it with `patchState`. You use the resource's own `set` / `update` or `reload`.

A middle ground is to keep the resource private and copy its value into state when it changes, but then you have two sources. Pick one based on whether you need the state features.

### 359: What must you know about `rxMethod` lifetimes?

- `rxMethod` must be created in an injection context (store features are). It's cleaned up when that injector is destroyed.
- Each call with a signal or observable creates a subscription that lives until the store is destroyed, unless you stop it.
- When you call it with a signal or observable from a component inside its injection context, the subscription is tied to the caller's injector, so it ends when the component is destroyed even if the store lives on (for example a root store).
- Each call returns a ref with `destroy()` so you can stop just that call.

```ts
const ref = this.store.loadByQuery(this.query);
// later
ref.destroy();
```

### 360: How do you call `rxMethod` outside an injection context with a signal?

Pass the injector in the config:

```ts
export class BooksPage {
  private readonly store = inject(BooksStore);
  private readonly injector = inject(Injector);
  readonly query = signal("");

  ngOnInit() {
    this.store.loadByQuery(this.query, { injector: this.injector });
  }
}
```

Without it, NgRx can't tie the subscription to the component and warns that it may leak (the subscription would live as long as the store).

### 361: How do you keep an `rxMethod` alive after an error?

Handle errors inside the inner observable, the same as in effects:

```ts
load: rxMethod<string>(
  pipe(
    switchMap((id) =>
      api.get(id).pipe(
        tapResponse({
          next: (item) => patchState(store, { item }),
          error: (e: Error) => patchState(store, { error: e.message }),
        }),
      ),
    ),
  ),
);
```

If an error reaches the outer pipe, the `rxMethod` stream dies and future calls do nothing.

### 362: How do you choose the flattening operator inside `rxMethod`?

The same rules as effects:

- `switchMap` - search and load-by-id, where only the latest matters.
- `exhaustMap` - submit buttons and one-time loads.
- `concatMap` - ordered writes.
- `mergeMap` - independent parallel work.

Since `rxMethod` can be called many times, using the wrong one causes the same races as in effects.

### 363: When are Promise-based methods better than `rxMethod`, and when worse?

Better:

- Simple one-off actions, like "save" or "delete", with `async/await`.
- Easier for developers who don't know RxJS.
- Easy to await in components and tests.

Worse:

- No built-in cancellation, so an older slow request can overwrite a newer result.
- No debounce or other time operators.
- No reaction to a signal or observable input.

You can guard against races in Promise methods with a request counter, but at that point `rxMethod` with `switchMap` is often simpler.

### 364: What is the SignalStore events plugin?

`@ngrx/signals/events` adds an event-based flow to SignalStore, similar to actions, reducers and effects in the global store, but built on signals and without a global store:

- Events are defined with `event` or `eventGroup`.
- Components dispatch events with `injectDispatch` or the `Dispatcher` service.
- Stores update state from events with `withReducer` and `on`.
- Stores react to events with side effects in `withEventHandlers`, using the `Events` service.

It was added as experimental in NgRx 19.2 and has been extended in later versions. It's a good fit when you like the Redux event model but want SignalStore's structure.

### 365: How do you define events with `eventGroup`?

```ts
import { type } from "@ngrx/signals";
import { event, eventGroup } from "@ngrx/signals/events";

export const booksPageEvents = eventGroup({
  source: "Books Page",
  events: {
    opened: type<void>(),
    queryChanged: type<string>(),
  },
});

export const booksApiEvents = eventGroup({
  source: "Books API",
  events: {
    loadedSuccess: type<Book[]>(),
    loadedFailure: type<string>(),
  },
});

// a single event
export const appStarted = event("[App] Started");
```

Each event creator takes the payload as its argument: `booksPageEvents.queryChanged('ngrx')` creates `{ type: '[Books Page] queryChanged', payload: 'ngrx' }`.

### 366: How do you update state from events with `withReducer`?

```ts
import { on, withReducer } from "@ngrx/signals/events";

export const BooksStore = signalStore(
  withState({
    books: [] as Book[],
    query: "",
    isLoading: false,
    error: null as string | null,
  }),
  withReducer(
    on(booksPageEvents.opened, () => ({ isLoading: true })),
    on(booksPageEvents.queryChanged, ({ payload: query }) => ({ query })),
    on(booksApiEvents.loadedSuccess, ({ payload: books }) => ({
      books,
      isLoading: false,
    })),
    on(booksApiEvents.loadedFailure, ({ payload: error }) => ({
      error,
      isLoading: false,
    })),
  ),
);
```

Case reducers return a partial state, or a partial state updater, so you can reuse entity updaters:

```ts
on(booksApiEvents.loadedSuccess, ({ payload }) => setAllEntities(payload));
```

### 367: How do you handle side effects with `withEventHandlers`?

```ts
import { Events, withEventHandlers } from "@ngrx/signals/events";
import { mapResponse } from "@ngrx/operators";

export const BooksStore = signalStore(
  withState(initialState),
  withReducer(/* ... */),
  withEventHandlers(
    (store, events = inject(Events), api = inject(BooksService)) => ({
      loadBooks$: events.on(booksPageEvents.opened).pipe(
        exhaustMap(() =>
          api.getAll().pipe(
            mapResponse({
              next: (books) => booksApiEvents.loadedSuccess(books),
              error: (e: { message: string }) =>
                booksApiEvents.loadedFailure(e.message),
            }),
          ),
        ),
      ),
      logError$: events
        .on(booksApiEvents.loadedFailure)
        .pipe(tap(({ payload }) => console.error(payload))),
    }),
  ),
);
```

Each property is an observable. If it emits events, they're dispatched automatically. Other emitted values are ignored. In NgRx 21 this feature was renamed from `withEffects` to `withEventHandlers`, and `ng update` migrates the name.

### 368: How do components dispatch events in a SignalStore setup?

With `injectDispatch`, which returns typed functions for each event in a group:

```ts
@Component({
  providers: [BooksStore],
  template: `<input
    (input)="dispatch.queryChanged($any($event.target).value)"
  />`,
})
export class BooksPage {
  readonly store = inject(BooksStore);
  readonly dispatch = injectDispatch(booksPageEvents);

  constructor() {
    this.dispatch.opened();
  }
}
```

Or inject the `Dispatcher` service and call `dispatcher.dispatch(booksPageEvents.opened())`.

### 369: What are scoped events?

By default, events are global: every store listening anywhere in the app gets them. Scoped events, added in NgRx 21, let you create a local dispatcher with `provideDispatcher()` in a component's providers. Events dispatched in that part of the component tree stay in that scope, unless you ask to send them to the parent or global scope:

```ts
@Component({
  providers: [provideDispatcher(), TodoListStore],
})
export class TodoList {
  private readonly dispatcher = inject(Dispatcher);

  remove(id: string) {
    this.dispatcher.dispatch(todoListEvents.removed(id)); // local scope (default)
    this.dispatcher.dispatch(todoListEvents.removed(id), { scope: "parent" }); // parent scope
    this.dispatcher.dispatch(todoListEvents.removed(id), { scope: "global" }); // whole app
  }
}
```

`injectDispatch` supports the same scope option. This helps when the same component, with its own store, appears several times on a page and one instance's events shouldn't affect the others. The API is fairly new, so check the docs for the exact options in your version.

### 370: When should you use events instead of plain store methods?

Use plain methods when:

- One store owns the logic and there's one caller.
- You want the least amount of code.

Use events when:

- Several stores need to react to the same thing (for example `userLoggedOut` resets cart, orders and settings stores).
- You want the "what happened" vs "what to do about it" separation.
- You want components to not know which store handles their events.

### 371: How do several stores react to the same event?

Each store just adds its own `on` or event handler:

```ts
export const authEvents = eventGroup({
  source: "Auth",
  events: { loggedOut: type<void>() },
});

export const CartStore = signalStore(
  { providedIn: "root" },
  withState({ items: [] as CartItem[] }),
  withReducer(on(authEvents.loggedOut, () => ({ items: [] }))),
);

export const OrdersStore = signalStore(
  { providedIn: "root" },
  withEntities<Order>(),
  withReducer(on(authEvents.loggedOut, () => removeAllEntities())),
);
```

The component that logs out only dispatches `authEvents.loggedOut()` and doesn't know about these stores.

### 372: How do you test a store that uses the events plugin?

Dispatch events with the `Dispatcher` and check state:

```ts
it("stores books after success", () => {
  TestBed.configureTestingModule({
    providers: [
      BooksStore,
      { provide: BooksService, useValue: { getAll: () => of([book]) } },
    ],
  });
  const store = TestBed.inject(BooksStore);
  const dispatcher = TestBed.inject(Dispatcher);

  dispatcher.dispatch(booksPageEvents.opened());

  expect(store.books()).toEqual([book]);
  expect(store.isLoading()).toBe(false);
});
```

To check that events were dispatched, subscribe to `TestBed.inject(Events).on(booksApiEvents.loadedSuccess)` before dispatching.

### 373: How would you handle two entity collections with custom ids in one SignalStore?

```ts
const productConfig = entityConfig({
  entity: type<Product>(),
  collection: "product",
  selectId: (p) => p.sku,
});

const categoryConfig = entityConfig({
  entity: type<Category>(),
  collection: "category",
  selectId: (c) => c.slug,
});

export const CatalogStore = signalStore(
  withEntities(productConfig),
  withEntities(categoryConfig),
  withComputed(({ productEntities, categoryEntityMap }) => ({
    productsWithCategory: computed(() =>
      productEntities().map((p) => ({
        ...p,
        category: categoryEntityMap()[p.categorySlug],
      })),
    ),
  })),
  withMethods((store, api = inject(CatalogApi)) => ({
    async load() {
      const { products, categories } = await api.load();
      patchState(
        store,
        setAllEntities(products, productConfig),
        setAllEntities(categories, categoryConfig),
      );
    },
  })),
);
```

Several updaters in one `patchState` call means signals that read both collections only see one change.

### 374: How do you update several entities by a condition in SignalStore?

`updateEntities` and `removeEntities` accept a predicate instead of ids:

```ts
patchState(
  store,
  updateEntities({
    predicate: (todo) => todo.listId === listId,
    changes: (todo) => ({ archived: true, updatedAt: Date.now() }),
  }),
);

patchState(
  store,
  removeEntities((todo) => todo.archived),
);
```

`changes` can be an object or a function of the entity.

### 375: Should components read `entities()` or `entityMap()`?

- `entities()` is a computed array. It's recalculated whenever `ids` or `entityMap` change. Good for lists.
- `entityMap()` is the dictionary. Good for lookups by id.

For a detail view of one item, read from `entityMap()[id]` in a `computed`, instead of `entities().find(...)`, which is O(n) on every change. For lists, use `entities()` with `track item.id` in `@for`, so Angular only re-renders rows whose object reference changed.

### 376: What should you watch out for when using SignalStore with SSR?

- **Root stores are per request on the server.** Angular creates a new application per request, so a `providedIn: 'root'` store isn't shared between users. Don't keep data in module-level variables outside the store, those are shared.
- **Browser APIs.** `localStorage`, `window`, `document` don't exist on the server. Guard them with `isPlatformBrowser(inject(PLATFORM_ID))` or `afterNextRender`.
- **Never-ending work.** Polling, websockets and intervals started in `onInit` keep the server from finishing the render. Only start them in the browser.
- **Double fetching.** Use the HTTP transfer cache (on by default with `provideClientHydration()`), so requests made on the server aren't repeated in the browser.

### 377: How do you transfer SignalStore state from server to browser?

If the HTTP transfer cache isn't enough (for example the state comes from several sources), use `TransferState` in a hook:

```ts
const BOOKS_KEY = makeStateKey<BooksState>("books-store");

export function withTransferState<State extends object>(key: StateKey<State>) {
  return signalStoreFeature(
    { state: type<State>() },
    withHooks((store) => {
      const transferState = inject(TransferState);
      const isServer = isPlatformServer(inject(PLATFORM_ID));

      return {
        onInit() {
          if (isServer) {
            transferState.onSerialize(key, () => getState(store) as State);
          } else if (transferState.hasKey(key)) {
            patchState(store, transferState.get(key, getState(store) as State));
            transferState.remove(key);
          }
        },
      };
    }),
  );
}
```

On the server, the state is written into the HTML when rendering finishes. In the browser, the store picks it up before its first load call can run.

### 378: How long does a SignalStore provided in route `providers` live?

Route providers create an environment injector for that route the first time it's activated. That injector is not destroyed when you navigate away, so the store instance stays alive and keeps its state for the rest of the app session. If you want the store to be reset every time the page opens, provide it in the routed component's `providers` instead.

### 379: Can you extend a SignalStore class?

Not in a useful way. `signalStore` returns a class built at runtime from features, and the API is designed around composition. To share behavior, write a custom feature with `signalStoreFeature` and add it to each store. To share state between stores, inject one store into the other.

### 380: How do you get the type of a SignalStore instance?

Use `InstanceType`:

```ts
export const BooksStore = signalStore(
  withState(initialState),
  withMethods(/* ... */),
);
export type BooksStore = InstanceType<typeof BooksStore>;

function logBooks(store: BooksStore) {
  console.log(store.books());
}
```

Declaring a type with the same name as the const lets you write `BooksStore` in both value and type positions. For custom features, `SignalStoreFeature` and `EmptyFeatureResult` describe input and output types if you need to write them by hand.

### 381: How do you mock a SignalStore when testing a component?

Provide an object with the same shape, using signals and spies:

```ts
const mockStore = {
  books: signal<Book[]>([book]),
  isLoading: signal(false),
  loadAll: jasmine.createSpy("loadAll"),
};

TestBed.overrideComponent(BooksPage, {
  set: { providers: [{ provide: BooksStore, useValue: mockStore }] },
});
```

`overrideComponent` is needed when the store is listed in the component's own `providers`, because those take priority over `TestBed` providers. If the store is `providedIn: 'root'`, a normal `providers` entry in `configureTestingModule` is enough. Using writable signals lets you change values during the test: `mockStore.isLoading.set(true)`.

### 382: How do you test a custom SignalStore feature by itself?

Build a small test store that uses the feature:

```ts
describe("withPagination", () => {
  const TestStore = signalStore(withPagination({ pageSize: 10 }));

  it("moves to the next page if there is one", () => {
    TestBed.configureTestingModule({ providers: [TestStore] });
    const store = TestBed.inject(TestStore);

    store.setTotal(25);
    store.nextPage();
    store.nextPage();
    store.nextPage();

    expect(store.page()).toBe(3);
    expect(store.hasNext()).toBe(false);
  });
});
```

For features with inputs, add the required state and methods to the test store before the feature.

### 383: How do you test `onDestroy` hooks?

Destroy the injector that owns the store. For a root-like store in tests, call `TestBed.resetTestingModule()`. For a component-level store, destroy the component fixture:

```ts
it("stops polling on destroy", () => {
  const fixture = TestBed.createComponent(JobPage);
  const store = fixture.debugElement.injector.get(JobStore);
  const spy = spyOn(store, "stopPolling").and.callThrough();

  fixture.destroy();

  expect(spy).toHaveBeenCalled();
});
```

Here `onDestroy` calls `store.stopPolling()`. Often it's simpler to check the effect of destroying (like a service mock that was told to disconnect) than to spy on store methods.

### 384: How do you combine the global Store and SignalStore in one architecture?

A common split:

- **Global Store**: app-wide state used by many features, like auth, user profile, permissions, feature flags, and router state. It benefits from actions, DevTools and a clear event log.
- **SignalStore**: feature and page state, like a product list with filters, a checkout wizard, or an editor. Usually provided at the route or component level.

SignalStores read global state through `inject(Store).selectSignal(...)` and can dispatch global actions for things other features care about (like `[Checkout] Order Placed`). Global state should not depend on SignalStores.

### 385: How would you migrate a feature from NgRx Store to SignalStore?

1. Create the SignalStore with the same state shape (`withState` or `withEntities`).
2. Turn selectors into `withComputed`.
3. Turn reducers and effects into methods. For each action, decide if it becomes a method, or keep the event model with the events plugin (`withReducer`, `withEventHandlers`), which maps almost 1:1.
4. Keep publishing global actions that other features listen to, or switch those listeners to events.
5. Update components to inject the store instead of `Store` and selectors.
6. Remove the old feature state, effects and actions once nothing uses them.

Do one feature at a time and keep tests at the component level, so they keep passing across the migration.

### 386: What is the status of `@ngrx/data` and what should you use instead?

`@ngrx/data` is in maintenance mode: it gets fixes and version updates, but no new features, and it isn't recommended for new projects. It hides a lot of the store behind conventions, which is hard to customize. For new code, use `@ngrx/entity` with effects, or SignalStore with `withEntities` and a custom CRUD feature. Moving away from it can be done one entity type at a time.

### 387: How would you organize NgRx code in an Nx monorepo?

Common library types per domain:

- `data-access` - store, actions, effects, selectors, SignalStores, API services.
- `feature` - routed pages (containers) that use data-access.
- `ui` - presentational components, no NgRx.
- `util` - pure helpers and models.

With tags and `@nx/enforce-module-boundaries`:

- `ui` can't import `data-access`.
- A domain's `data-access` can't import another domain's internals, only its public API.
- `feature` libs can import `data-access` and `ui`.

This keeps state code from spreading into presentational components and makes ownership clear.

### 388: How do you keep feature state ownership clear in a big team?

- Each feature state has one owner (team or library), and only that library's reducer changes it.
- Other features interact through public actions/events and public selectors exported from the library's `index.ts`.
- Internal actions (like API result actions) are not exported.
- Shared concepts (like "user logged out") live in a shared library both sides can import.

This avoids features reaching into each other's state and makes refactors safer.

### 389: How would you write a facade with signals that doesn't lose the event log?

Keep the facade thin and name its methods after events:

```ts
@Injectable({ providedIn: "root" })
export class CheckoutFacade {
  private readonly store = inject(Store);

  readonly cart = this.store.selectSignal(selectCartViewModel);
  readonly placingOrder = this.store.selectSignal(selectPlacingOrder);

  checkoutPageOpened() {
    this.store.dispatch(CheckoutPageActions.opened());
  }
  placeOrderClicked(payment: PaymentInfo) {
    this.store.dispatch(CheckoutPageActions.placeOrderClicked({ payment }));
  }
}
```

If two different components need to trigger the same thing, give each its own event method (and action) instead of sharing a `loadCart()` command.

### 390: What is "action ping-pong" and why is it a problem?

It's when effects turn one action into another, which another effect turns into another, and so on:

```
[Page] Opened -> [Books] Load -> [Books] Load Started -> [Books API] Load Success -> [Books] Set Books
```

Each step is a full dispatch with reducers and selectors running, the flow is hard to follow, and the action log fills with noise. Usually only two are needed: `[Page] Opened` (the reducer sets loading, the effect calls the API) and `[Books API] Load Success` (the reducer saves books).

### 391: How do you handle long-running multi-step workflows with effects?

Write each step as a reaction to the previous step's result action, and keep a status in state so the UI knows where you are:

```ts
export const startUpload = createEffect(
  (actions$ = inject(Actions), api = inject(UploadApi)) =>
    actions$.pipe(
      ofType(UploadPageActions.fileChosen),
      concatMap(({ fileName }) =>
        api.createUploadUrl(fileName).pipe(
          map(({ url, uploadId }) =>
            UploadApiActions.urlCreated({ url, uploadId }),
          ),
          catchError(() => of(UploadApiActions.failed({ step: "url" }))),
        ),
      ),
    ),
  { functional: true },
);

export const sendFile = createEffect(
  (
    actions$ = inject(Actions),
    api = inject(UploadApi),
    files = inject(PendingFiles),
  ) =>
    actions$.pipe(
      ofType(UploadApiActions.urlCreated),
      concatMap(({ url, uploadId }) =>
        api.put(url, files.take(uploadId)).pipe(
          map(() => UploadApiActions.fileSent({ uploadId })),
          catchError(() => of(UploadApiActions.failed({ step: "send" }))),
        ),
      ),
    ),
  { functional: true },
);
```

The `File` object itself stays in a service (`PendingFiles`), because it isn't serializable. If the steps are always run together and no one else cares about the middle steps, it can be simpler to do the whole flow in one effect with chained `switchMap`s, and only dispatch the final result.

### 392: How would you build a multi-step wizard with SignalStore?

Provide a store at the wizard component, keep the step and the collected data in state, and validate in computed signals:

```ts
export const SignupWizardStore = signalStore(
  withState({
    step: 1 as 1 | 2 | 3,
    account: { email: "", password: "" },
    profile: { name: "", country: "" },
    status: "editing" as "editing" | "submitting" | "done" | "error",
  }),
  withComputed(({ account, profile }) => ({
    accountValid: computed(
      () => account.email().includes("@") && account.password().length >= 8,
    ),
    profileValid: computed(() => profile.name().length > 0),
  })),
  withMethods((store, api = inject(SignupApi)) => ({
    next() {
      patchState(store, (s) => ({
        step: Math.min(3, s.step + 1) as 1 | 2 | 3,
      }));
    },
    back() {
      patchState(store, (s) => ({
        step: Math.max(1, s.step - 1) as 1 | 2 | 3,
      }));
    },
    updateAccount(account: Partial<{ email: string; password: string }>) {
      patchState(store, (s) => ({ account: { ...s.account, ...account } }));
    },
    async submit() {
      patchState(store, { status: "submitting" });
      try {
        await api.signup(store.account(), store.profile());
        patchState(store, { status: "done" });
      } catch {
        patchState(store, { status: "error" });
      }
    },
  })),
);
```

The store is destroyed with the wizard, so there's nothing to reset by hand.

### 393: How would you queue writes while the user is offline?

- Keep a `pendingWrites` list in state (serializable descriptions of each change), and save it to storage.
- Apply changes optimistically to the main data.
- An effect (or `rxMethod`) listens to an online status stream. When online, it sends pending writes one by one with `concatMap`, removing each on success.
- On a conflict response from the server, dispatch an action that shows the user what happened and reloads the record.

```ts
export const flushQueue = createEffect(
  (
    store = inject(Store),
    api = inject(SyncApi),
    online = inject(OnlineStatus),
  ) =>
    online.isOnline$.pipe(
      filter(Boolean),
      concatLatestFrom(() => store.select(selectPendingWrites)),
      switchMap(([, writes]) =>
        from(writes).pipe(
          concatMap((write) =>
            api.send(write).pipe(
              map(() => SyncApiActions.writeSent({ id: write.id })),
              catchError((e) =>
                of(
                  SyncApiActions.writeFailed({
                    id: write.id,
                    status: e.status,
                  }),
                ),
              ),
            ),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

### 394: How would you write a WebSocket `rxMethod` that reconnects with backoff?

```ts
connect: rxMethod<void>(
  pipe(
    switchMap(() =>
      socket.messages$().pipe(
        tap({
          subscribe: () => patchState(store, { connection: 'connecting' }),
          next: (msg) => patchState(store, addEntity(msg), { connection: 'open' }),
        }),
        retry({
          delay: (_error, attempt) => {
            patchState(store, { connection: 'reconnecting' });
            const base = Math.min(30_000, 1000 * 2 ** attempt);
            return timer(base + Math.random() * 1000); // jitter
          },
          resetOnSuccess: true,
        })
      )
    )
  )
),
```

The jitter stops many clients from reconnecting at the exact same time after a server restart. `resetOnSuccess` resets the attempt counter after a working connection. Remember to only call this in the browser when using SSR.

### 395: How do you report errors from NgRx in one place?

Options that work well together:

- A meta-reducer that wraps reducers in `try/catch` and reports exceptions, then rethrows.
- One effect that listens to all failure actions and sends them to monitoring:

```ts
export const reportFailures = createEffect(
  (actions$ = inject(Actions), monitoring = inject(Monitoring)) =>
    actions$.pipe(
      filter((action) => action.type.endsWith("Failure")),
      tap((action) =>
        monitoring.captureMessage(action.type, { extra: action }),
      ),
    ),
  { functional: true, dispatch: false },
);
```

- A custom `EFFECTS_ERROR_HANDLER` for errors that escaped effects.
- Angular's `ErrorHandler` for everything else.

Matching by name suffix depends on a naming rule, so make sure the team follows it, or use an explicit list of action creators.

### 396: How do you find performance problems in an NgRx app?

- **Angular DevTools profiler**: see which components re-render and why.
- **Redux DevTools**: look for too many actions in a short time, or actions that change large parts of state.
- **Browser performance panel**: find slow reducers or selectors in flame charts.
- **Temporary logging** in projectors (`console.count('selectVisibleRows')`) to see how often they run.

Common causes are selectors that aren't memoized well, components that read too much state, high-frequency actions (scroll, mouse move, websocket ticks), and missing `track` in `@for`.

### 397: Is `selectSignal` faster than `select` with the `async` pipe?

In many cases it's a bit lighter: no subscription per binding, and Angular knows exactly which views read which signal, so with OnPush or zoneless only those views are checked. With `async`, each new value calls `markForCheck`, which marks the view and all its ancestors. The bigger wins usually come from good selectors and fewer actions, not from choosing between the two, but `selectSignal` is the better default today.

### 398: How is `computed` over selector signals different from `combineLatest` over `select` observables?

`combineLatest` emits once for each source that emits. If one action changes two selected values, you can get two emissions, and the first one has one new and one old value (a "glitch").

Signals are glitch-free. A `computed` that reads two selector signals only recalculates when you read it, and it always sees both new values:

```ts
readonly summary = computed(() => `${this.count()} items, ${this.total()} total`);
```

That's one reason why moving view models to `selectSignal` and `computed` often removes small bugs and extra renders.

### 399: What can you do when a selector is truly expensive?

- Make sure it only runs when needed (narrow inputs, stable references).
- Move the work into the reducer if the result is read often but the inputs change rarely. Then it's computed once per change instead of per read. The downside is derived data in state.
- Ask the server to do it (filtering, aggregation) if the data is large.
- For CPU-heavy work like parsing or big calculations, run it in a Web Worker from an effect and store the result.
- Use paging or virtualization so you compute only what's on screen.

### 400: What can cause high memory use from DevTools?

DevTools keeps a copy of the state for every action in its history. With large state and many actions (like a websocket feed), memory grows quickly. Fixes:

- Lower `maxAge`.
- Use `actionsBlocklist` to skip noisy actions.
- Use `stateSanitizer` to replace large parts with placeholders.
- Turn DevTools off in long-running production sessions.

```ts
provideStoreDevtools({
  maxAge: 20,
  actionsBlocklist: ["[Ticker] Price Received"],
  stateSanitizer: (state: any) => ({ ...state, ticker: "<<large data>>" }),
});
```

### 401: How expensive are immutable updates on large arrays?

Copying an array of 50,000 items on every change costs time and creates garbage for the GC. Ways to reduce it:

- Normalize: `entities` is an object, and updating one entity copies the object's keys, not every entity. `ids` doesn't change on update.
- Batch changes: apply 100 websocket updates in one reducer call instead of 100 calls.
- Don't sort on every change (`sortComparer`), sort in a selector.
- Keep huge read-only data (like a big lookup table) outside the store, in a service, and only keep ids or filters in state.

Thanks to structural sharing, the unchanged entity objects are not copied, only references are.

### 402: How do you type a meta-reducer that only reacts to some actions?

Type it with `ActionReducer` and compare against action creator `type`s:

```ts
export function resetFeatureOn<S>(...creators: ActionCreator[]) {
  const types = new Set(creators.map((c) => c.type));

  return (reducer: ActionReducer<S>): ActionReducer<S> =>
    (state, action) =>
      types.has(action.type)
        ? reducer(undefined, action)
        : reducer(state, action);
}

provideState("orders", ordersReducer, {
  metaReducers: [
    resetFeatureOn(AuthActions.logoutSuccess, AccountActions.switched),
  ],
});
```

Keep meta-reducers pure. They're plain functions without an injection context, so they can't `inject()` services, and side effects like sending audit logs belong in an effect that listens to the same actions.

### 403: How do you enforce NgRx architecture rules automatically?

- `@ngrx/eslint-plugin` with the `store`, `effects` and `signals` configs, plus stricter rules like `no-typed-global-store`, `prefer-concat-latest-from`, `good-action-hygiene` and `prefer-protected-state`.
- Nx module boundary rules (or `eslint-plugin-boundaries`) so UI libraries can't import data-access code.
- TypeScript `strict` mode, so action payloads and state are checked.
- Code owners per feature folder.
- A short written guide for naming actions and where state belongs, referenced in pull request templates.

### 404: How do you sync a form with NgRx without putting every keystroke in the store?

- Load the initial values from the store into the form once (or when the source record changes).
- Keep editing local to the form.
- Dispatch on meaningful events: submit, or a debounced "draft changed" if drafts should survive navigation.

```ts
export class ProfileForm {
  private readonly store = inject(Store);
  readonly profile = this.store.selectSignal(selectProfile);
  readonly form = inject(FormBuilder).nonNullable.group({ name: "", bio: "" });

  constructor() {
    effect(() => {
      const p = this.profile();
      if (p)
        this.form.reset({ name: p.name, bio: p.bio }, { emitEvent: false });
    });

    this.form.valueChanges
      .pipe(debounceTime(1000), takeUntilDestroyed())
      .subscribe((draft) =>
        this.store.dispatch(ProfileFormActions.draftChanged({ draft })),
      );
  }
}
```

Be careful with the `effect` that resets the form: if the profile updates while the user is typing, their input would be lost. Only reset when the record id changes, or when the form is not dirty.

### 405: How do you handle changes in the shape of persisted state between app versions?

Save a version number with the state and migrate when loading:

```ts
const CURRENT_VERSION = 3;

const migrations: Record<number, (s: any) => any> = {
  1: (s) => ({ ...s, settings: { theme: s.theme ?? "light" } }),
  2: (s) => ({ ...s, cart: { items: s.cartItems ?? [] } }),
};

function loadState(): Partial<AppState> | undefined {
  const raw = localStorage.getItem("app");
  if (!raw) return undefined;
  let { version, state } = JSON.parse(raw);
  while (version < CURRENT_VERSION) {
    state = migrations[version](state);
    version++;
  }
  return state;
}
```

If migration fails, drop the saved state rather than crash. And only persist what you really need, which keeps migrations small.

### 406: How do you handle switching accounts or tenants in an NgRx app?

Everything tied to the old account must be cleared, or data can leak between accounts:

- A meta-reducer that resets user-specific features on `[Auth] Account Switched`.
- SignalStores listen to the same event (events plugin) or are scoped below a component that's re-created per account (for example by using the account id in the route).
- Effects with long-lived streams (websockets, polling) stop on the switch and start again for the new account.
- Clear caches in services and the HTTP transfer cache if needed.

Write a test that switches accounts and checks that no old data is visible.

### 407: How would you store feature flags with NgRx?

Load them at startup and keep them in a small global feature:

```ts
export const flagsFeature = createFeature({
  name: "flags",
  reducer: createReducer(
    { flags: {} as Record<string, boolean>, loaded: false },
    on(FlagsApiActions.loaded, (s, { flags }) => ({
      ...s,
      flags,
      loaded: true,
    })),
  ),
  extraSelectors: ({ selectFlags }) => ({
    selectFlag: (name: string) =>
      createSelector(selectFlags, (flags) => flags[name] ?? false),
  }),
});
```

Use the flag selectors in components, guards and effects. If routes depend on flags, load the flags before the first navigation with `provideAppInitializer`.

### 408: What does "URL as the source of truth" mean in an NgRx app?

Things like the current page, filters, sorting and the selected item live in the URL, not only in the store. The store reads them through router-store selectors. Benefits: links can be shared, the back button works, and refresh restores the view.

```ts
export const selectProductFilters = createSelector(
  selectQueryParams,
  (params) => ({
    category: params["category"] ?? "all",
    page: Number(params["page"] ?? 1),
  }),
);
```

Changing a filter means navigating (`router.navigate([], { queryParams, queryParamsHandling: 'merge' })`), and an effect reacts to `routerNavigatedAction` to load data. Don't keep a copy of the same value in feature state, or the two will drift apart.

### 409: Why does `selectRouteParam` sometimes return `undefined` with nested routes?

The default router selectors read params from the deepest active route only. If the param is defined on a parent route (`/projects/:projectId/tasks/:taskId`), and you're on the child route, `projectId` isn't in the child's own params. Fixes:

- Write a custom serializer that merges params from all levels (see question 202).
- Or set `paramsInheritanceStrategy: 'always'` in `provideRouter(routes, withRouterConfig({ paramsInheritanceStrategy: 'always' }))`, so child routes inherit parent params.

### 410: An action is dispatched but the state doesn't change. How do you debug it?

1. Check Redux DevTools: did the action appear, with the right type and payload?
2. Is the feature registered? If it's lazy, the route with `provideState` may not have loaded yet, so the reducer doesn't exist.
3. Does the reducer's `on` use the same action creator? Two creators with the same type but from different files can be confusing, and a typo in an old string-based type won't match.
4. Does the handler return the new state, or does it return the old `state` by mistake?
5. Is the change happening, but the selector reads a different key?
6. Did a meta-reducer swallow it?

### 411: The state changes, but the component doesn't update. What do you check?

- Is the selector reading the right part of state? Test it with the projector.
- Is the state being mutated? Then the reference doesn't change and memoization returns the old result. Runtime checks usually catch this.
- In zone-based apps, was the action dispatched outside the Angular zone (from a third-party callback)? `strictActionWithinNgZone` helps find it.
- Is the component `OnPush` and reading state through a plain field that was set once, instead of a signal or `async` pipe?
- In a template, is the signal called (`books()` and not `books`)?

### 412: An effect runs twice for one action. What could be the cause?

- The effect is registered twice in different ways, for example as a class in `provideEffects` and also in a component's `providers` (which also creates a new instance). Deduplication only works for effects registered through NgRx.
- Two different effects listen to the same action and both call the API.
- The action is actually dispatched twice (check DevTools), for example from both `ngOnInit` and a constructor, or because the component is created twice.
- An `effect()` or reactive `dispatch(() => ...)` re-runs because it reads more signals than you expect.

### 413: How do you find and fix an infinite loop of actions?

Signs: the browser freezes and DevTools shows the same actions repeating. Causes:

- An effect returns the same action it listens to (`avoid-cyclic-effects` lint rule catches it).
- Effect A emits X, effect B turns X back into A's trigger.
- A component dispatches in reaction to state (in an `effect()` or a subscription), and that dispatch changes the same state.

Fix by making the flow one direction: an event comes in, reducers update, and effects only produce result actions that don't trigger the same flow again. For state-based reactions, add a guard (`distinctUntilChanged`, `filter` on status).

### 414: You get "Cannot assign to read only property" in development. What happened?

`strictStateImmutability` (or SignalStore's dev-mode freezing) froze the state, and some code tried to change it in place. Look at the stack trace, typical places are:

- `array.sort()` on state in a selector or component. Use `toSorted()` or `[...arr].sort()`.
- `push`/`splice` on an array from state.
- Two-way binding (`[(ngModel)]`) directly to a state object.
- A third-party library that changes the input you passed.

The fix is always to copy before changing, or to dispatch an action that creates the new state.

### 415: You call a SignalStore method and the UI doesn't update. Why?

Most often, the state was changed in place:

```ts
// bug: same array reference, signal doesn't notify
store.items().push(newItem);
patchState(store, { items: store.items() });

// fix
patchState(store, (s) => ({ items: [...s.items, newItem] }));
```

Other causes:

- Two different instances of the store: one in the component providers and one root instance. The component you're looking at reads the other one.
- The template reads a value copied into a plain field once, not the signal.
- An error was thrown inside an `rxMethod` and the stream died, so later calls do nothing.

### 416: What happens if `patchState` sets a value to the same reference?

Signals use `Object.is` equality by default. If you patch a property with the exact same value or reference, that property's signal doesn't notify, and computed signals depending on it don't re-run. This is good for performance, but it's also why in-place mutation followed by `patchState` with the same reference doesn't update the UI.

### 417: Why might `toSignal(store.select(...))` behave differently from `selectSignal`?

- `toSignal` needs an initial value or `requireSync: true`. The store emits synchronously, so `requireSync: true` works, but it's easy to forget and get `undefined`.
- `toSignal` creates a subscription that is tied to the injection context where it's called.
- `selectSignal` is a `computed` over the state signal. It's glitch-free and has no subscription.

Prefer `selectSignal`. Use `toSignal` when you need RxJS operators in between, like `debounceTime`.

### 418: What steps do you follow to upgrade NgRx in a large app?

1. Read the NgRx changelog and the migration guide for each major version you're crossing.
2. Upgrade Angular first, one major at a time (`ng update @angular/core @angular/cli`).
3. Run `ng update @ngrx/store` to update all NgRx packages and run their migrations.
4. Fix remaining type errors, mostly around deprecated APIs.
5. Run lint with the NgRx plugin, since rules often point at deprecated patterns.
6. Run unit, integration and e2e tests.
7. Upgrade one major version at a time, don't skip several at once.

### 419: What API changes in recent NgRx versions should you know about?

A short list of changes that often come up:

- **v16**: `selectSignal` added to Store and ComponentStore.
- **v17**: `@ngrx/signals` introduced in developer preview (`signalStore`, `signalState`, `withState`, `withComputed`, `withMethods`, `withHooks`, `rxMethod`, entities).
- **v18**: SignalStore became stable. `tapResponse` and `concatLatestFrom` moved to `@ngrx/operators`. SignalStore state became protected by default.
- **v19**: `withProps`, `signalMethod`, `store.dispatch` with a function (reactive dispatch), dev-mode freezing of SignalStore state, `rxMethod` tied to the caller's injector, and the experimental events plugin in 19.2.
- **v20**: `withLinkedState`, `withFeature`, and more work on the events plugin.
- **v21**: `withEffects` from the events plugin renamed to `withEventHandlers`, and scoped events.

Always check the official changelog, because minor releases also add features.

### 420: How big is NgRx in the bundle and how do you keep it small?

The packages are small and tree-shakable. A few things help:

- Only install what you use. `@ngrx/signals` alone is enough for many apps.
- Lazy load feature states and effects with route providers, so their code is in lazy chunks.
- Don't include Store DevTools code in production if you don't need it, for example with a file replacement for an environment-specific providers file.
- Avoid importing whole utility libraries (like all of lodash) in selectors.

### 421: How do you use the Store in a functional HTTP interceptor?

```ts
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(Store).selectSignal(selectToken)();
  return next(
    token
      ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
      : req,
  );
};

provideHttpClient(withInterceptors([authInterceptor]));
```

Reading a signal value is synchronous and simple. With observables, use `take(1)` and `switchMap` to pass the request on.

### 422: Why can injecting the Store in an interceptor cause a circular dependency, and how do you avoid it?

If an effect (or a service used by the store setup) injects `HttpClient`, and `HttpClient` needs the interceptor, and the interceptor injects `Store`, which needs effects to be ready, you can get a cycle during startup. With functional interceptors and `inject()` called inside the interceptor function (at request time, not at creation), this is rarely an issue. For class-based interceptors, inject `Injector` and get the store lazily inside `intercept`.

### 423: Why shouldn't services called from effects dispatch actions themselves?

If a service both calls the API and dispatches actions, the flow is split across two places, and the effect's result is no longer the full story. It's also harder to test and reuse the service. Keep services pure data access (return observables or promises), and let effects map results to actions. The `no-dispatch-in-effects` rule covers the effect side of this.

### 424: How would you design state for a real-time collaborative feature, like a shared board?

- Normalize items (cards, columns) as entities with a `version` or `updatedAt` field.
- Local changes are optimistic and carry a client-generated id.
- Server events come through a websocket effect or `rxMethod` and are applied with upserts. Drop events that are older than what you have (compare versions).
- When the server rejects a change, roll back to the server's version and tell the user.
- Batch incoming events with `bufferTime(50)` to keep rendering smooth.
- Keep "who is viewing" and cursors in a separate, frequently changing slice, so the main board selectors aren't affected.

### 425: How do you handle conflicts when two users edit the same record?

Use optimistic concurrency: each record has a version. The client sends the version it edited, and the server rejects the update if the version doesn't match (HTTP 409).

```ts
on(TaskApiActions.updateConflict, (state, { serverTask }) =>
  adapter.setOne(serverTask, {
    ...state,
    conflicts: { ...state.conflicts, [serverTask.id]: true },
  }),
);
```

The UI then shows "this task was changed by someone else" with the server version, and lets the user apply their change again.

### 426: How would you cache results per query?

Keep a map from a query key to the result ids and a timestamp:

```ts
export interface SearchState extends EntityState<Product> {
  queries: Record<string, { ids: string[]; loadedAt: number }>;
  currentQuery: string;
}

export const selectCurrentResults = createSelector(
  selectQueries,
  selectCurrentQuery,
  selectProductEntities,
  (queries, q, entities) => (queries[q]?.ids ?? []).map((id) => entities[id]!),
);
```

The effect skips the request if the query is cached and not too old. Products are stored once in the entity collection and shared between queries. Remove old queries now and then so the map doesn't grow forever.

### 427: How do you implement stale-while-revalidate with NgRx?

Show cached data right away and refresh in the background:

```ts
export const loadDashboard = createEffect(
  (
    actions$ = inject(Actions),
    store = inject(Store),
    api = inject(DashboardApi),
  ) =>
    actions$.pipe(
      ofType(DashboardPageActions.opened),
      concatLatestFrom(() => store.select(selectDashboardLoadedAt)),
      filter(([, loadedAt]) => !loadedAt || Date.now() - loadedAt > 30_000),
      switchMap(() =>
        api.get().pipe(
          map((data) =>
            DashboardApiActions.loaded({ data, loadedAt: Date.now() }),
          ),
          catchError(() => of(DashboardApiActions.refreshFailed())),
        ),
      ),
    ),
  { functional: true },
);
```

The reducer keeps showing the old data during the refresh (it sets a `refreshing` flag, not `loading`), and a refresh failure doesn't clear the data. `loadedAt` is created in the effect, not in the reducer, to keep the reducer pure.

### 428: Where should you normalize API responses, in the effect or the reducer?

Both work. Doing it in the effect (or a mapping function the effect calls) means actions carry data in the shape the store wants, and several reducers can use it directly. Doing it in the reducer keeps actions close to the API response, which can help debugging. A common rule: map API DTOs to app models in the service or effect, and let reducers only store data. That keeps the API's quirks out of the store.

### 429: How do you handle token refresh with NgRx?

The interceptor handles the 401 and the refresh call, because it has to retry the original request:

```ts
export const refreshInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  const store = inject(Store);

  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status !== 401 || req.url.includes("/auth/refresh"))
        return throwError(() => error);

      return auth.refreshOnce().pipe(
        tap((tokens) =>
          store.dispatch(AuthApiActions.tokenRefreshed({ tokens })),
        ),
        switchMap((tokens) =>
          next(
            req.clone({
              setHeaders: { Authorization: `Bearer ${tokens.access}` },
            }),
          ),
        ),
        catchError((refreshError) => {
          store.dispatch(AuthApiActions.sessionExpired());
          return throwError(() => refreshError);
        }),
      );
    }),
  );
};
```

`refreshOnce()` should share one refresh request between all requests that failed at the same time (for example with `shareReplay` in the service). The store only records the result, and an effect redirects to login on `sessionExpired`.

### 430: What is a good global error handling strategy with NgRx?

- Effects catch errors and turn them into specific failure actions, with a user-friendly message.
- Reducers save errors next to the data they belong to, so the UI can show them in the right place.
- One effect shows toasts for failures that need it, and one reports failures to monitoring.
- Interceptors handle cross-cutting cases like 401 and maintenance mode.
- Angular's `ErrorHandler` catches anything unexpected.

Don't keep one global `error` field for the whole app, because errors from unrelated requests overwrite each other.

### 431: How do you show one global loading bar for many parallel requests?

Count requests that are in flight instead of using a boolean:

```ts
export const loadingFeature = createFeature({
  name: "loading",
  reducer: createReducer(
    { pending: 0 },
    on(HttpActivityActions.started, (s) => ({ pending: s.pending + 1 })),
    on(HttpActivityActions.finished, (s) => ({
      pending: Math.max(0, s.pending - 1),
    })),
  ),
  extraSelectors: ({ selectPending }) => ({
    selectIsBusy: createSelector(selectPending, (n) => n > 0),
  }),
});
```

The started and finished actions can come from an interceptor (with `finalize` for finished). That adds two actions per request, so for very chatty apps a plain signal in a service is a lighter option for this kind of UI-only state.

### 432: How would you write a generic CRUD feature for SignalStore?

```ts
export interface CrudService<E> {
  getAll(): Promise<E[]>;
  create(entity: Omit<E, "id">): Promise<E>;
  update(id: string, changes: Partial<E>): Promise<E>;
  remove(id: string): Promise<void>;
}

export function withCrud<E extends { id: string }>(
  serviceToken: ProviderToken<CrudService<E>>,
) {
  return signalStoreFeature(
    withEntities<E>(),
    withState({ status: "idle" as "idle" | "loading" | "error" }),
    withMethods((store, api = inject(serviceToken)) => ({
      async loadAll() {
        patchState(store, { status: "loading" });
        try {
          patchState(store, setAllEntities(await api.getAll()), {
            status: "idle",
          });
        } catch {
          patchState(store, { status: "error" });
        }
      },
      async create(entity: Omit<E, "id">) {
        patchState(store, addEntity(await api.create(entity)));
      },
      async update(id: string, changes: Partial<E>) {
        patchState(store, setEntity(await api.update(id, changes)));
      },
      async remove(id: string) {
        await api.remove(id);
        patchState(store, removeEntity(id));
      },
    })),
  );
}

export const TodosStore = signalStore(withCrud<Todo>(TodosService));
```

Keep generic features small. When one entity type needs special behavior, add it in that store next to the shared feature, rather than adding options to the generic one for every case.

### 433: How do you avoid duplicate requests when several components ask for the same data?

- In NgRx Store: the effect checks a status in state (`loading` or `loaded`) and skips the request, or uses `exhaustMap` for the same action.
- In SignalStore: the method checks `store.status()` before starting, or the store is `providedIn: 'root'` with an `rxMethod` using `exhaustMap`.
- At the service level: share the in-flight observable with `shareReplay({ bufferSize: 1, refCount: true })` keyed by request.

The store-based check is the most visible one, because the UI can also use the same status.

### 434: How do parent and child SignalStores talk to each other?

A child store can inject the parent store, because DI looks up the component tree:

```ts
export const BoardStore = signalStore(
  withEntities<Column>(),
  withMethods(/* ... */),
);

export const ColumnStore = signalStore(
  withState({ columnId: "" }),
  withProps(() => ({ _board: inject(BoardStore) })),
  withComputed(({ columnId, _board }) => ({
    column: computed(() => _board.entityMap()[columnId()]),
  })),
  withMethods((store) => ({
    rename(title: string) {
      store._board.renameColumn(store.columnId(), title);
    },
  })),
);
```

The child calls parent methods, and the parent never knows about children. If siblings need to react to each other, put the shared state in the parent, or use events.

### 435: What happens if a component that provides a store also injects a parent's store of the same class?

`inject(BooksStore)` in a component that lists `BooksStore` in its own `providers` returns its own instance. To get the parent's instance, use `inject(BooksStore, { skipSelf: true })`. This is useful for nested trees (like nested comments), where each level has a store and needs to talk to the level above.

### 436: How do you stop polling or socket effects from running during SSR?

Check the platform before starting:

```ts
export const pollPrices = createEffect(
  (
    actions$ = inject(Actions),
    api = inject(PricesApi),
    platformId = inject(PLATFORM_ID),
  ) =>
    isPlatformBrowser(platformId)
      ? actions$.pipe(
          ofType(PricesPageActions.opened),
          switchMap(() =>
            timer(0, 10_000).pipe(
              switchMap(() =>
                api.get().pipe(
                  map((prices) => PricesApiActions.loaded({ prices })),
                  catchError(() => EMPTY),
                ),
              ),
              takeUntil(actions$.pipe(ofType(PricesPageActions.left))),
            ),
          ),
        )
      : EMPTY,
  { functional: true },
);
```

On the server, the app waits for pending work before it sends the HTML, so an interval that never ends would make the render hang until it times out.

### 437: How do `@defer` blocks and incremental hydration affect NgRx?

Components inside `@defer` are loaded later. If they provide their own SignalStore, it's created only when the block renders, which is fine and often what you want. If they rely on a lazy feature state, the feature has to be provided by the route, not by the deferred component, because `provideState` only works in environment injectors. With incremental hydration, server-rendered content may stay dehydrated until a trigger, so stores used by those components are created only when hydration happens. Code shouldn't assume all stores exist at startup.

### 438: How do you test code that uses Angular `effect` or `watchState` in a SignalStore?

`watchState` runs synchronously, so a normal test works. Angular `effect`s are scheduled, so you need to flush them. In recent Angular versions use `TestBed.tick()` (it replaced `TestBed.flushEffects()`):

```ts
it("saves settings to storage", () => {
  const store = TestBed.inject(SettingsStore);
  store.setTheme("dark");
  TestBed.tick();
  expect(localStorage.getItem("settings")).toContain("dark");
});
```

For `rxMethod` with time operators, use fake timers or `TestScheduler`.

### 439: How do you test a component with signal inputs that uses a selector based on the input?

Set the input with `fixture.componentRef.setInput` and override the selectors it uses:

```ts
it("shows the book from the store", () => {
  const store = TestBed.inject(MockStore);
  store.overrideSelector(selectBookEntities, {
    "1": { id: "1", title: "NgRx" } as Book,
  });

  const fixture = TestBed.createComponent(BookCard);
  fixture.componentRef.setInput("id", "1");
  fixture.detectChanges();

  expect(fixture.nativeElement.textContent).toContain("NgRx");
});
```

### 440: Is it OK to create a SignalStore for every row in a big list?

For tens of rows, yes. For thousands, it adds up: each instance runs all its features, creates its signals, computed signals and methods, and registers hooks. Often a better design is one store for the whole list (with entities), and row components that only get their item through an input and send events up. Keep per-row stores for rows with a lot of their own logic, like an inline editor.

### 441: How would you explain the trade-offs of NgRx Store to a team that says it's too much boilerplate?

- The modern APIs (`createActionGroup`, `createFeature`, functional effects, `selectSignal`) remove most of the old boilerplate.
- The extra structure pays off when many people work on the same state: every change is an event you can find, log and replay.
- Effects keep async logic out of components, which makes components simple to test.
- If the feature doesn't need that structure, SignalStore gives most of the benefits with much less code, and it's part of the same library.

So the choice isn't "NgRx or no NgRx", it's picking the right tool for each part of the app.

### 442: What do you look for when reviewing NgRx code?

- Actions are events with clear sources, not reused commands.
- Reducers are pure, have explicit return types, and don't mutate.
- Selectors are narrow and memoized, with no heavy work in components or templates.
- Effects use the right flattening operator, catch errors inside, and don't dispatch from inside.
- No manual store subscriptions in components.
- SignalStore state is protected, private members use `_`, and async methods handle errors and races.
- State is serializable and normalized where it makes sense.
- Tests cover reducers, selectors, effects or store methods.

### 443: What are common NgRx anti-patterns?

- Putting everything in the global store, including local UI state.
- Generic `set` actions dispatched from many places.
- Dispatching several actions in a row.
- Storing derived data in state instead of using selectors.
- Mutating state, especially sorting arrays in place.
- `switchMap` for writes.
- `catchError` on the outer effect stream.
- Subscribing to the store in components and copying values into fields.
- Selectors with props (old API) or selectors that take the whole state.
- Facades that hide every action behind command methods.
- Turning off `protectedState` in SignalStore to patch from components.

### 444: How would you structure state for a large enterprise Angular app?

- **Global NgRx Store** for cross-cutting state: auth, user, permissions, feature flags, router.
- **Lazy feature states or SignalStores** per domain, provided in route providers, owned by one team each.
- **Component-level SignalStores** for pages and complex widgets.
- **Plain signals** for simple UI state.
- **Clear public APIs** per domain library: exported events/actions and selectors only.
- **Shared conventions**: action naming, folder structure, lint rules, testing approach.
- **Monitoring**: failure actions reported in one place.

The goal is that most state is local and short-lived, and only real shared state is global.

### 445: How would you bring NgRx into an existing app that uses services with `BehaviorSubject`s?

Start where it helps most:

1. Pick one feature with shared state and bugs caused by it.
2. If the team is new to NgRx, start with SignalStore. It's the shortest step from a service with subjects: state becomes `withState`, getters become `withComputed`, methods stay methods.
3. Keep the old service API as a thin wrapper over the store for a while, so callers don't all change at once.
4. Add tests at the component level before the change.
5. Move more features once the team is comfortable. Add the global Store only for state that's truly app-wide.

### 446: How do you decide what goes into SignalStore state vs `withProps`?

- **State**: plain, serializable data that changes over time and should be visible through `getState`, `watchState` and persistence.
- **Props**: things that aren't data: services, observables, resources, config, helper objects, or values that don't need to be in a state snapshot.

If you find yourself wanting to persist or reset a prop, it probably belongs in state.

### 447: What does `withComputed` with private members let you do in custom features?

A feature can compute internal values (prefixed with `_`) that later features use, without exposing them:

```ts
export function withSearch<E extends { name: string }>() {
  return signalStoreFeature(
    {
      state: type<{ query: string }>(),
      props: type<{ entities: Signal<E[]> }>(),
    },
    withComputed(({ query }) => ({
      _normalizedQuery: computed(() => query().trim().toLowerCase()),
    })),
    withComputed(({ entities, _normalizedQuery }) => ({
      searchResults: computed(() =>
        entities().filter((e) =>
          e.name.toLowerCase().includes(_normalizedQuery()),
        ),
      ),
    })),
  );
}
```

The host store gets `searchResults`, and `_normalizedQuery` stays hidden. Note that `entities` from `withEntities` is a computed signal, so it's declared under `props` in the input.

### 448: How do you keep event handlers in SignalStore from reacting to events meant for other instances?

When several instances of the same store exist, a global event reaches all of them. Options:

- Include an id in the payload and filter in the handler: `events.on(itemEvents.saved).pipe(filter(({ payload }) => payload.id === store.id()))`.
- Use scoped events with `provideDispatcher()` at each instance's component, so events stay local.
- Use plain methods instead of events when the call is only for that one instance.

### 449: How do you keep NgRx code easy to change over time?

- Small features with clear ownership.
- Components depend on selectors or store signals, not on state shape.
- Events describe what happened, so new reactions can be added without touching the dispatching code.
- Shared behavior in custom SignalStore features instead of copy-paste.
- Tests that check behavior (given this action or method call, the selector or signal shows this) instead of implementation details.
- Regular upgrades, so you never fall far behind the current API.

### 450: What direction has NgRx taken in recent versions, and how does that affect new projects?

NgRx has moved toward signals. Recent versions added `selectSignal`, reactive `dispatch`, SignalStore with features like `withProps`, `withLinkedState` and `withFeature`, and the events plugin, which brings the Redux event model to SignalStore. The global Store and effects are still fully supported and widely used.

For a new project this usually means:

- Use signals in components (`selectSignal`, SignalStore).
- Start feature state with SignalStore.
- Use the global Store or the events plugin where the app benefits from an event-driven design across many features.
- Keep RxJS for what it's good at: async streams, timing and cancellation, through effects, `rxMethod` and event handlers.
