# RxJS Interview Questions and Answers

_Last updated: November 25, 2026_

450 RxJS interview questions with answers, split into 150 easy, 150 moderate and 150 advanced. The answers target RxJS 7.8, the current stable release, and use the modern APIs: operators imported from `rxjs`, `firstValueFrom` and `lastValueFrom` instead of `toPromise`, the config objects for `share`, `shareReplay`, `retry`, `repeat` and `timeout`, and `connectable` instead of `multicast`. Where Angular comes up, the examples use `takeUntilDestroyed`, `toSignal` and the other helpers from `@angular/core/rxjs-interop`.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is RxJS?](#1-what-is-rxjs)
- [2: What problem does RxJS solve?](#2-what-problem-does-rxjs-solve)
- [3: How do you install RxJS?](#3-how-do-you-install-rxjs)
- [4: What is the current stable version of RxJS?](#4-what-is-the-current-stable-version-of-rxjs)
- [5: What is an Observable?](#5-what-is-an-observable)
- [6: What is an Observer?](#6-what-is-an-observer)
- [7: What is a Subscription?](#7-what-is-a-subscription)
- [8: What does subscribe do?](#8-what-does-subscribe-do)
- [9: Why do you need to unsubscribe?](#9-why-do-you-need-to-unsubscribe)
- [10: What is the difference between an Observable and a Promise?](#10-what-is-the-difference-between-an-observable-and-a-promise)
- [11: What does it mean that Observables are lazy?](#11-what-does-it-mean-that-observables-are-lazy)
- [12: What are the three kinds of notifications an Observable can send?](#12-what-are-the-three-kinds-of-notifications-an-observable-can-send)
- [13: What is the Observable contract?](#13-what-is-the-observable-contract)
- [14: What is an operator in RxJS?](#14-what-is-an-operator-in-rxjs)
- [15: What is the pipe method?](#15-what-is-the-pipe-method)
- [16: What is the difference between a creation function and a pipeable operator?](#16-what-is-the-difference-between-a-creation-function-and-a-pipeable-operator)
- [17: Where do you import operators from in RxJS 7?](#17-where-do-you-import-operators-from-in-rxjs-7)
- [18: What does the dollar sign at the end of a variable name mean?](#18-what-does-the-dollar-sign-at-the-end-of-a-variable-name-mean)
- [19: What does the of function do?](#19-what-does-the-of-function-do)
- [20: What does the from function do?](#20-what-does-the-from-function-do)
- [21: What is the difference between of and from with an array?](#21-what-is-the-difference-between-of-and-from-with-an-array)
- [22: What does interval do?](#22-what-does-interval-do)
- [23: What does timer do?](#23-what-does-timer-do)
- [24: What does fromEvent do?](#24-what-does-fromevent-do)
- [25: What is EMPTY?](#25-what-is-empty)
- [26: What is NEVER?](#26-what-is-never)
- [27: How do you create an Observable that errors?](#27-how-do-you-create-an-observable-that-errors)
- [28: What does range do?](#28-what-does-range-do)
- [29: What does defer do?](#29-what-does-defer-do)
- [30: Why would you wrap a Promise in defer?](#30-why-would-you-wrap-a-promise-in-defer)
- [31: What does map do?](#31-what-does-map-do)
- [32: What does filter do?](#32-what-does-filter-do)
- [33: What does tap do?](#33-what-does-tap-do)
- [34: Why should you not change data inside map with side effects?](#34-why-should-you-not-change-data-inside-map-with-side-effects)
- [35: What does take do?](#35-what-does-take-do)
- [36: What does first do?](#36-what-does-first-do)
- [37: What is the difference between take(1) and first()?](#37-what-is-the-difference-between-take1-and-first)
- [38: What does last do?](#38-what-does-last-do)
- [39: What does skip do?](#39-what-does-skip-do)
- [40: What does distinctUntilChanged do?](#40-what-does-distinctuntilchanged-do)
- [41: What is the difference between distinct and distinctUntilChanged?](#41-what-is-the-difference-between-distinct-and-distinctuntilchanged)
- [42: What does debounceTime do?](#42-what-does-debouncetime-do)
- [43: What does throttleTime do?](#43-what-does-throttletime-do)
- [44: What does scan do?](#44-what-does-scan-do)
- [45: What is the difference between scan and reduce?](#45-what-is-the-difference-between-scan-and-reduce)
- [46: What does startWith do?](#46-what-does-startwith-do)
- [47: What does endWith do?](#47-what-does-endwith-do)
- [48: What does catchError do?](#48-what-does-catcherror-do)
- [49: What does finalize do?](#49-what-does-finalize-do)
- [50: What does delay do?](#50-what-does-delay-do)
- [51: What does toArray do?](#51-what-does-toarray-do)
- [52: What does count do?](#52-what-does-count-do)
- [53: What do max and min do?](#53-what-do-max-and-min-do)
- [54: What does pairwise do?](#54-what-does-pairwise-do)
- [55: What does takeWhile do?](#55-what-does-takewhile-do)
- [56: What does skipWhile do?](#56-what-does-skipwhile-do)
- [57: What does takeUntil do?](#57-what-does-takeuntil-do)
- [58: What does takeLast do?](#58-what-does-takelast-do)
- [59: What does skipLast do?](#59-what-does-skiplast-do)
- [60: What does elementAt do?](#60-what-does-elementat-do)
- [61: What do find and findIndex do?](#61-what-do-find-and-findindex-do)
- [62: What does every do?](#62-what-does-every-do)
- [63: What does isEmpty do?](#63-what-does-isempty-do)
- [64: What does defaultIfEmpty do?](#64-what-does-defaultifempty-do)
- [65: What does throwIfEmpty do?](#65-what-does-throwifempty-do)
- [66: What does ignoreElements do?](#66-what-does-ignoreelements-do)
- [67: What does single do?](#67-what-does-single-do)
- [68: What does distinctUntilKeyChanged do?](#68-what-does-distinctuntilkeychanged-do)
- [69: What is a Subject?](#69-what-is-a-subject)
- [70: What is a BehaviorSubject?](#70-what-is-a-behaviorsubject)
- [71: What is a ReplaySubject?](#71-what-is-a-replaysubject)
- [72: What is an AsyncSubject?](#72-what-is-an-asyncsubject)
- [73: What is the difference between Subject, BehaviorSubject and ReplaySubject?](#73-what-is-the-difference-between-subject-behaviorsubject-and-replaysubject)
- [74: What is a hot Observable?](#74-what-is-a-hot-observable)
- [75: What is a cold Observable?](#75-what-is-a-cold-observable)
- [76: How do you make a cold Observable hot?](#76-how-do-you-make-a-cold-observable-hot)
- [77: What is multicasting?](#77-what-is-multicasting)
- [78: What is a marble diagram?](#78-what-is-a-marble-diagram)
- [79: What is the difference between push and pull?](#79-what-is-the-difference-between-push-and-pull)
- [80: Can an Observable emit synchronously?](#80-can-an-observable-emit-synchronously)
- [81: How do you convert an Observable to a Promise?](#81-how-do-you-convert-an-observable-to-a-promise)
- [82: Why is toPromise deprecated?](#82-why-is-topromise-deprecated)
- [83: What happens if you call firstValueFrom on an Observable that never emits?](#83-what-happens-if-you-call-firstvaluefrom-on-an-observable-that-never-emits)
- [84: How do you handle errors inside subscribe?](#84-how-do-you-handle-errors-inside-subscribe)
- [85: Why is passing three separate callbacks to subscribe deprecated?](#85-why-is-passing-three-separate-callbacks-to-subscribe-deprecated)
- [86: What does merge do?](#86-what-does-merge-do)
- [87: What does concat do?](#87-what-does-concat-do)
- [88: What is the difference between merge and concat?](#88-what-is-the-difference-between-merge-and-concat)
- [89: What does combineLatest do?](#89-what-does-combinelatest-do)
- [90: Why does combineLatest not emit sometimes?](#90-why-does-combinelatest-not-emit-sometimes)
- [91: Can you pass an object to combineLatest?](#91-can-you-pass-an-object-to-combinelatest)
- [92: What does forkJoin do?](#92-what-does-forkjoin-do)
- [93: What happens with forkJoin if one source errors or completes empty?](#93-what-happens-with-forkjoin-if-one-source-errors-or-completes-empty)
- [94: What does zip do?](#94-what-does-zip-do)
- [95: What does race do?](#95-what-does-race-do)
- [96: What does withLatestFrom do?](#96-what-does-withlatestfrom-do)
- [97: What is the difference between combineLatest and withLatestFrom?](#97-what-is-the-difference-between-combinelatest-and-withlatestfrom)
- [98: What does switchMap do?](#98-what-does-switchmap-do)
- [99: What does mergeMap do?](#99-what-does-mergemap-do)
- [100: What does concatMap do?](#100-what-does-concatmap-do)
- [101: What does exhaustMap do?](#101-what-does-exhaustmap-do)
- [102: How do you choose between switchMap, mergeMap, concatMap and exhaustMap?](#102-how-do-you-choose-between-switchmap-mergemap-concatmap-and-exhaustmap)
- [103: What is a higher-order Observable?](#103-what-is-a-higher-order-observable)
- [104: What is the problem with nesting subscribe calls?](#104-what-is-the-problem-with-nesting-subscribe-calls)
- [105: What does mergeAll do?](#105-what-does-mergeall-do)
- [106: What is an ObservableInput?](#106-what-is-an-observableinput)
- [107: What does retry do?](#107-what-does-retry-do)
- [108: What does repeat do?](#108-what-does-repeat-do)
- [109: What does timeout do?](#109-what-does-timeout-do)
- [110: What does auditTime do?](#110-what-does-audittime-do)
- [111: What does sampleTime do?](#111-what-does-sampletime-do)
- [112: What is the difference between debounceTime and throttleTime?](#112-what-is-the-difference-between-debouncetime-and-throttletime)
- [113: What does bufferTime do?](#113-what-does-buffertime-do)
- [114: What does bufferCount do?](#114-what-does-buffercount-do)
- [115: What does buffer do?](#115-what-does-buffer-do)
- [116: What does the async pipe do in Angular?](#116-what-does-the-async-pipe-do-in-angular)
- [117: Does Angular HttpClient return a hot or cold Observable?](#117-does-angular-httpclient-return-a-hot-or-cold-observable)
- [118: Do you need to unsubscribe from Angular HttpClient calls?](#118-do-you-need-to-unsubscribe-from-angular-httpclient-calls)
- [119: What is takeUntilDestroyed in Angular?](#119-what-is-takeuntildestroyed-in-angular)
- [120: What is toSignal in Angular?](#120-what-is-tosignal-in-angular)
- [121: What is a Subscription's add method for?](#121-what-is-a-subscriptions-add-method-for)
- [122: What is teardown logic?](#122-what-is-teardown-logic)
- [123: What is the closed property of a Subscription?](#123-what-is-the-closed-property-of-a-subscription)
- [124: What happens if you subscribe to the same cold Observable twice?](#124-what-happens-if-you-subscribe-to-the-same-cold-observable-twice)
- [125: What is the difference between share and shareReplay?](#125-what-is-the-difference-between-share-and-sharereplay)
- [126: What does iif do?](#126-what-does-iif-do)
- [127: What does generate do?](#127-what-does-generate-do)
- [128: What does partition do?](#128-what-does-partition-do)
- [129: What does fromEventPattern do?](#129-what-does-fromeventpattern-do)
- [130: What is isObservable?](#130-what-is-isobservable)
- [131: What is the RxJS pipe function, separate from the pipe method?](#131-what-is-the-rxjs-pipe-function-separate-from-the-pipe-method)
- [132: What is a custom operator?](#132-what-is-a-custom-operator)
- [133: What are some common naming conventions in RxJS code?](#133-what-are-some-common-naming-conventions-in-rxjs-code)
- [134: What does asObservable do on a Subject?](#134-what-does-asobservable-do-on-a-subject)
- [135: How do you create an Observable from a callback-based API?](#135-how-do-you-create-an-observable-from-a-callback-based-api)
- [136: How do you make an HTTP request with RxJS outside Angular?](#136-how-do-you-make-an-http-request-with-rxjs-outside-angular)
- [137: What is the ajax function?](#137-what-is-the-ajax-function)
- [138: What is the webSocket function?](#138-what-is-the-websocket-function)
- [139: What does animationFrames do?](#139-what-does-animationframes-do)
- [140: What does EmptyError mean?](#140-what-does-emptyerror-mean)
- [141: What is the difference between a Subject and a plain event emitter?](#141-what-is-the-difference-between-a-subject-and-a-plain-event-emitter)
- [142: What happens when you call next on a completed Subject?](#142-what-happens-when-you-call-next-on-a-completed-subject)
- [143: What does mergeWith do?](#143-what-does-mergewith-do)
- [144: What does map with an index do?](#144-what-does-map-with-an-index-do)
- [145: How do you debug an RxJS pipeline?](#145-how-do-you-debug-an-rxjs-pipeline)
- [146: Can you reuse an Observable after it completes?](#146-can-you-reuse-an-observable-after-it-completes)
- [147: What are Observables good for in a UI?](#147-what-are-observables-good-for-in-a-ui)
- [148: Is RxJS only for Angular?](#148-is-rxjs-only-for-angular)
- [149: What does subscribe return if the Observable is synchronous?](#149-what-does-subscribe-return-if-the-observable-is-synchronous)
- [150: What is the scheduler in RxJS in simple words?](#150-what-is-the-scheduler-in-rxjs-in-simple-words)

### Moderate Questions (151-300)

- [151: How do you build a search-as-you-type feature with RxJS?](#151-how-do-you-build-a-search-as-you-type-feature-with-rxjs)
- [152: What goes wrong if you use mergeMap instead of switchMap for search?](#152-what-goes-wrong-if-you-use-mergemap-instead-of-switchmap-for-search)
- [153: Why should catchError usually go inside switchMap instead of at the end?](#153-why-should-catcherror-usually-go-inside-switchmap-instead-of-at-the-end)
- [154: How do you configure retry with a delay?](#154-how-do-you-configure-retry-with-a-delay)
- [155: How do you add exponential backoff to retries?](#155-how-do-you-add-exponential-backoff-to-retries)
- [156: How do you retry only for certain errors?](#156-how-do-you-retry-only-for-certain-errors)
- [157: Why are retryWhen and repeatWhen deprecated?](#157-why-are-retrywhen-and-repeatwhen-deprecated)
- [158: How do you poll an endpoint until a condition is met?](#158-how-do-you-poll-an-endpoint-until-a-condition-is-met)
- [159: What is the difference between polling with interval plus switchMap and with repeat?](#159-what-is-the-difference-between-polling-with-interval-plus-switchmap-and-with-repeat)
- [160: What options does the share operator have?](#160-what-options-does-the-share-operator-have)
- [161: What does refCount mean in shareReplay?](#161-what-does-refcount-mean-in-sharereplay)
- [162: How do you cache an HTTP response and refresh it on demand?](#162-how-do-you-cache-an-http-response-and-refresh-it-on-demand)
- [163: How do you cache a value only for a limited time?](#163-how-do-you-cache-a-value-only-for-a-limited-time)
- [164: What is connectable?](#164-what-is-connectable)
- [165: What does the connect operator do?](#165-what-does-the-connect-operator-do)
- [166: What replaces multicast, publish, publishReplay and refCount in RxJS 7?](#166-what-replaces-multicast-publish-publishreplay-and-refcount-in-rxjs-7)
- [167: How do you build a simple state store with BehaviorSubject?](#167-how-do-you-build-a-simple-state-store-with-behaviorsubject)
- [168: Why is it a bad idea to call getValue on a BehaviorSubject everywhere?](#168-why-is-it-a-bad-idea-to-call-getvalue-on-a-behaviorsubject-everywhere)
- [169: When do you use a Subject and when a BehaviorSubject?](#169-when-do-you-use-a-subject-and-when-a-behaviorsubject)
- [170: What happens if a function inside map throws an error?](#170-what-happens-if-a-function-inside-map-throws-an-error)
- [171: How do you keep a stream running after an error?](#171-how-do-you-keep-a-stream-running-after-an-error)
- [172: How do you rethrow a different error from catchError?](#172-how-do-you-rethrow-a-different-error-from-catcherror)
- [173: What is the second argument of the catchError callback?](#173-what-is-the-second-argument-of-the-catcherror-callback)
- [174: In what order do finalize callbacks run?](#174-in-what-order-do-finalize-callbacks-run)
- [175: What are the extra callbacks of tap in RxJS 7?](#175-what-are-the-extra-callbacks-of-tap-in-rxjs-7)
- [176: What options does the timeout config object have?](#176-what-options-does-the-timeout-config-object-have)
- [177: Where should takeUntil go in a pipe?](#177-where-should-takeuntil-go-in-a-pipe)
- [178: What is the destroy$ Subject pattern and what replaces it in Angular?](#178-what-is-the-destroy-subject-pattern-and-what-replaces-it-in-angular)
- [179: How do you use takeUntilDestroyed outside the constructor?](#179-how-do-you-use-takeuntildestroyed-outside-the-constructor)
- [180: What is toObservable in Angular?](#180-what-is-toobservable-in-angular)
- [181: What options does toSignal accept?](#181-what-options-does-tosignal-accept)
- [182: How do you combine Angular route params with an HTTP call?](#182-how-do-you-combine-angular-route-params-with-an-http-call)
- [183: How do you react to reactive form changes with RxJS?](#183-how-do-you-react-to-reactive-form-changes-with-rxjs)
- [184: How do you model loading, error and data in one stream?](#184-how-do-you-model-loading-error-and-data-in-one-stream)
- [185: How do you pause and resume a stream?](#185-how-do-you-pause-and-resume-a-stream)
- [186: How do you build a countdown timer?](#186-how-do-you-build-a-countdown-timer)
- [187: How do you implement drag and drop with RxJS?](#187-how-do-you-implement-drag-and-drop-with-rxjs)
- [188: How do you load more items on infinite scroll?](#188-how-do-you-load-more-items-on-infinite-scroll)
- [189: How do you auto-save a form without losing edits?](#189-how-do-you-auto-save-a-form-without-losing-edits)
- [190: What does groupBy do?](#190-what-does-groupby-do)
- [191: How do you stop groupBy from keeping groups forever?](#191-how-do-you-stop-groupby-from-keeping-groups-forever)
- [192: What does window do and how is it different from buffer?](#192-what-does-window-do-and-how-is-it-different-from-buffer)
- [193: What do bufferToggle and bufferWhen do?](#193-what-do-buffertoggle-and-bufferwhen-do)
- [194: What does expand do?](#194-what-does-expand-do)
- [195: What are mergeScan and switchScan?](#195-what-are-mergescan-and-switchscan)
- [196: What is the difference between debounce and debounceTime?](#196-what-is-the-difference-between-debounce-and-debouncetime)
- [197: How do the leading and trailing options of throttleTime work?](#197-how-do-the-leading-and-trailing-options-of-throttletime-work)
- [198: When do you use zip, combineLatest, forkJoin and withLatestFrom?](#198-when-do-you-use-zip-combinelatest-forkjoin-and-withlatestfrom)
- [199: Why does combineLatest emit values you don't want, and how do you fix it?](#199-why-does-combinelatest-emit-values-you-dont-want-and-how-do-you-fix-it)
- [200: What do materialize and dematerialize do?](#200-what-do-materialize-and-dematerialize-do)
- [201: What does onErrorResumeNextWith do?](#201-what-does-onerrorresumenextwith-do)
- [202: What does using do?](#202-what-does-using-do)
- [203: What does the scheduled function do?](#203-what-does-the-scheduled-function-do)
- [204: What do observeOn and subscribeOn do?](#204-what-do-observeon-and-subscribeon-do)
- [205: What are the main schedulers in RxJS?](#205-what-are-the-main-schedulers-in-rxjs)
- [206: What is the difference between asyncScheduler and asapScheduler?](#206-what-is-the-difference-between-asyncscheduler-and-asapscheduler)
- [207: How do you test RxJS code with the TestScheduler?](#207-how-do-you-test-rxjs-code-with-the-testscheduler)
- [208: What do the characters in a marble string mean?](#208-what-do-the-characters-in-a-marble-string-mean)
- [209: What is the difference between cold and hot in marble tests?](#209-what-is-the-difference-between-cold-and-hot-in-marble-tests)
- [210: How do you test debounceTime with marbles?](#210-how-do-you-test-debouncetime-with-marbles)
- [211: What is expectSubscriptions used for?](#211-what-is-expectsubscriptions-used-for)
- [212: How do you test Observable code without marbles?](#212-how-do-you-test-observable-code-without-marbles)
- [213: How do you write a custom operator from scratch?](#213-how-do-you-write-a-custom-operator-from-scratch)
- [214: What are OperatorFunction and MonoTypeOperatorFunction?](#214-what-are-operatorfunction-and-monotypeoperatorfunction)
- [215: How do you narrow types with filter?](#215-how-do-you-narrow-types-with-filter)
- [216: How do you type a Subject that emits no data?](#216-how-do-you-type-a-subject-that-emits-no-data)
- [217: How do you get partial results from forkJoin when some calls fail?](#217-how-do-you-get-partial-results-from-forkjoin-when-some-calls-fail)
- [218: How do you run many requests with a limit on concurrency?](#218-how-do-you-run-many-requests-with-a-limit-on-concurrency)
- [219: How do you run requests one after another where each needs the previous result?](#219-how-do-you-run-requests-one-after-another-where-each-needs-the-previous-result)
- [220: How does fromFetch cancel requests?](#220-how-does-fromfetch-cancel-requests)
- [221: How do you turn a Node.js EventEmitter into an Observable?](#221-how-do-you-turn-a-nodejs-eventemitter-into-an-observable)
- [222: Can you use async iterables and streams with RxJS?](#222-can-you-use-async-iterables-and-streams-with-rxjs)
- [223: How do you use RxJS in a React component?](#223-how-do-you-use-rxjs-in-a-react-component)
- [224: How do you connect a BehaviorSubject to useSyncExternalStore?](#224-how-do-you-connect-a-behaviorsubject-to-usesyncexternalstore)
- [225: What is redux-observable?](#225-what-is-redux-observable)
- [226: How does NgRx use RxJS?](#226-how-does-ngrx-use-rxjs)
- [227: When should you use Angular signals and when RxJS?](#227-when-should-you-use-angular-signals-and-when-rxjs)
- [228: What are common sources of memory leaks with RxJS?](#228-what-are-common-sources-of-memory-leaks-with-rxjs)
- [229: How do you find a subscription leak?](#229-how-do-you-find-a-subscription-leak)
- [230: What is config.onUnhandledError?](#230-what-is-configonunhandlederror)
- [231: What is config.onStoppedNotification?](#231-what-is-configonstoppednotification)
- [232: What is ObjectUnsubscribedError?](#232-what-is-objectunsubscribederror)
- [233: What does windowTime in ReplaySubject do?](#233-what-does-windowtime-in-replaysubject-do)
- [234: How do you compare objects in distinctUntilChanged?](#234-how-do-you-compare-objects-in-distinctuntilchanged)
- [235: How do you combine several filters that change over time?](#235-how-do-you-combine-several-filters-that-change-over-time)
- [236: What is the difference between exhaustMap and throttleTime for a submit button?](#236-what-is-the-difference-between-exhaustmap-and-throttletime-for-a-submit-button)
- [237: What is the risk with concatMap when the source is fast?](#237-what-is-the-risk-with-concatmap-when-the-source-is-fast)
- [238: What is the risk with mergeMap without a concurrency limit?](#238-what-is-the-risk-with-mergemap-without-a-concurrency-limit)
- [239: Why is switchMap risky for write operations?](#239-why-is-switchmap-risky-for-write-operations)
- [240: Why should services avoid subscribing themselves?](#240-why-should-services-avoid-subscribing-themselves)
- [241: What is the difference between declarative and imperative RxJS code?](#241-what-is-the-difference-between-declarative-and-imperative-rxjs-code)
- [242: How do you build a reducer-style state with scan?](#242-how-do-you-build-a-reducer-style-state-with-scan)
- [243: Should side effects go in tap or in subscribe?](#243-should-side-effects-go-in-tap-or-in-subscribe)
- [244: How do you share one WebSocket connection across the app?](#244-how-do-you-share-one-websocket-connection-across-the-app)
- [245: What does multiplex on a WebSocketSubject do?](#245-what-does-multiplex-on-a-websocketsubject-do)
- [246: How do you reconnect a WebSocket automatically?](#246-how-do-you-reconnect-a-websocket-automatically)
- [247: What options does the webSocket function take?](#247-what-options-does-the-websocket-function-take)
- [248: How do you get upload progress with rxjs/ajax?](#248-how-do-you-get-upload-progress-with-rxjsajax)
- [249: How do you fall back to a second server if the first is slow?](#249-how-do-you-fall-back-to-a-second-server-if-the-first-is-slow)
- [250: What is the difference between iif and defer for conditions?](#250-what-is-the-difference-between-iif-and-defer-for-conditions)
- [251: How does NestJS use RxJS?](#251-how-does-nestjs-use-rxjs)
- [252: How do you detect a double click with RxJS?](#252-how-do-you-detect-a-double-click-with-rxjs)
- [253: How do you track online and offline status?](#253-how-do-you-track-online-and-offline-status)
- [254: How do you pause polling while the browser tab is hidden?](#254-how-do-you-pause-polling-while-the-browser-tab-is-hidden)
- [255: How do you detect that a user is idle?](#255-how-do-you-detect-that-a-user-is-idle)
- [256: How do you retry a request when the browser comes back online?](#256-how-do-you-retry-a-request-when-the-browser-comes-back-online)
- [257: How do you limit calls to N per second?](#257-how-do-you-limit-calls-to-n-per-second)
- [258: How do you avoid sending the same request twice while one is in flight?](#258-how-do-you-avoid-sending-the-same-request-twice-while-one-is-in-flight)
- [259: How do you do an optimistic update with RxJS?](#259-how-do-you-do-an-optimistic-update-with-rxjs)
- [260: How do you show cached data first and then fresh data?](#260-how-do-you-show-cached-data-first-and-then-fresh-data)
- [261: How do you fall back to a cached value when a request fails?](#261-how-do-you-fall-back-to-a-cached-value-when-a-request-fails)
- [262: What lint rules help with RxJS?](#262-what-lint-rules-help-with-rxjs)
- [263: Why does TypeScript sometimes lose types after many operators in pipe?](#263-why-does-typescript-sometimes-lose-types-after-many-operators-in-pipe)
- [264: What were the main breaking changes from RxJS 6 to RxJS 7?](#264-what-were-the-main-breaking-changes-from-rxjs-6-to-rxjs-7)
- [265: How do you migrate an RxJS 6 project to RxJS 7?](#265-how-do-you-migrate-an-rxjs-6-project-to-rxjs-7)
- [266: How does RxJS tree shaking work?](#266-how-does-rxjs-tree-shaking-work)
- [267: How do you debounce per key, for example per input field?](#267-how-do-you-debounce-per-key-for-example-per-input-field)
- [268: How do you emit a value only after a user has held a key for some time?](#268-how-do-you-emit-a-value-only-after-a-user-has-held-a-key-for-some-time)
- [269: How do you detect a keyboard shortcut sequence?](#269-how-do-you-detect-a-keyboard-shortcut-sequence)
- [270: How do you trigger a reload of data from a button?](#270-how-do-you-trigger-a-reload-of-data-from-a-button)
- [271: Why does subscribing to a Subject inside the template cause issues with hot data?](#271-why-does-subscribing-to-a-subject-inside-the-template-cause-issues-with-hot-data)
- [272: What is the difference between ReplaySubject(1) and BehaviorSubject?](#272-what-is-the-difference-between-replaysubject1-and-behaviorsubject)
- [273: Can you use RxJS in a Web Worker or Node.js service?](#273-can-you-use-rxjs-in-a-web-worker-or-nodejs-service)
- [274: How do you run some code only when the first subscriber arrives?](#274-how-do-you-run-some-code-only-when-the-first-subscriber-arrives)
- [275: How do you merge several streams but know which one each value came from?](#275-how-do-you-merge-several-streams-but-know-which-one-each-value-came-from)
- [276: How do you handle errors from an inner Observable in mergeMap without stopping the others?](#276-how-do-you-handle-errors-from-an-inner-observable-in-mergemap-without-stopping-the-others)
- [277: What is a "trigger" stream and why is it useful?](#277-what-is-a-trigger-stream-and-why-is-it-useful)
- [278: How do you keep the previous results visible while new ones load?](#278-how-do-you-keep-the-previous-results-visible-while-new-ones-load)
- [279: How do you convert an Observable to a signal outside Angular?](#279-how-do-you-convert-an-observable-to-a-signal-outside-angular)
- [280: How do you make sure an Observable completes after a certain amount of time?](#280-how-do-you-make-sure-an-observable-completes-after-a-certain-amount-of-time)
- [281: How do you emit a value after a delay only if nothing else happened?](#281-how-do-you-emit-a-value-after-a-delay-only-if-nothing-else-happened)
- [282: How do you chain two streams where the second needs the first's last value?](#282-how-do-you-chain-two-streams-where-the-second-needs-the-firsts-last-value)
- [283: What is the difference between EMPTY and of() and NEVER?](#283-what-is-the-difference-between-empty-and-of-and-never)
- [284: How do you subscribe to an Observable only once, no matter how many places use it?](#284-how-do-you-subscribe-to-an-observable-only-once-no-matter-how-many-places-use-it)
- [285: How do you handle errors in a long-lived stream like NgRx effects?](#285-how-do-you-handle-errors-in-a-long-lived-stream-like-ngrx-effects)
- [286: How do you test code that uses a BehaviorSubject service?](#286-how-do-you-test-code-that-uses-a-behaviorsubject-service)
- [287: How do you test Angular code that uses debounceTime?](#287-how-do-you-test-angular-code-that-uses-debouncetime)
- [288: How do you use the time and flush helpers in TestScheduler run?](#288-how-do-you-use-the-time-and-flush-helpers-in-testscheduler-run)
- [289: What does the animate helper in TestScheduler do?](#289-what-does-the-animate-helper-in-testscheduler-do)
- [290: What is the difference between subscribe and forEach on an Observable?](#290-what-is-the-difference-between-subscribe-and-foreach-on-an-observable)
- [291: How do you keep only the latest N values in an array?](#291-how-do-you-keep-only-the-latest-n-values-in-an-array)
- [292: How do you build a typeahead that also shows "no results" and errors?](#292-how-do-you-build-a-typeahead-that-also-shows-no-results-and-errors)
- [293: Why do some people say "don't use Subjects", and when are they fine?](#293-why-do-some-people-say-dont-use-subjects-and-when-are-they-fine)
- [294: How do you prevent the async pipe from making duplicate requests?](#294-how-do-you-prevent-the-async-pipe-from-making-duplicate-requests)
- [295: What does subscribe with no arguments do?](#295-what-does-subscribe-with-no-arguments-do)
- [296: How do you combine an Observable and a Promise?](#296-how-do-you-combine-an-observable-and-a-promise)
- [297: How do you run a stream only while an element is visible on screen?](#297-how-do-you-run-a-stream-only-while-an-element-is-visible-on-screen)
- [298: How do you wrap ResizeObserver or MutationObserver in an Observable?](#298-how-do-you-wrap-resizeobserver-or-mutationobserver-in-an-observable)
- [299: How do you know when all values from a mergeMap are done?](#299-how-do-you-know-when-all-values-from-a-mergemap-are-done)
- [300: What is a good rule of thumb for where to subscribe?](#300-what-is-a-good-rule-of-thumb-for-where-to-subscribe)

### Advanced Questions (301-450)

- [301: What actually happens inside subscribe?](#301-what-actually-happens-inside-subscribe)
- [302: What does the Subscriber class guarantee?](#302-what-does-the-subscriber-class-guarantee)
- [303: How are pipeable operators implemented internally in RxJS 7?](#303-how-are-pipeable-operators-implemented-internally-in-rxjs-7)
- [304: What was Observable.lift and why should you not use it?](#304-what-was-observablelift-and-why-should-you-not-use-it)
- [305: How does unsubscription travel through an operator chain?](#305-how-does-unsubscription-travel-through-an-operator-chain)
- [306: How can take(1) stop a synchronous infinite source?](#306-how-can-take1-stop-a-synchronous-infinite-source)
- [307: Why is a teardown returned from a synchronous producer sometimes run late?](#307-why-is-a-teardown-returned-from-a-synchronous-producer-sometimes-run-late)
- [308: What happens when an observer's next callback throws?](#308-what-happens-when-an-observers-next-callback-throws)
- [309: What is reentrancy in RxJS and why does it matter?](#309-what-is-reentrancy-in-rxjs-and-why-does-it-matter)
- [310: How does a Subject deliver values to subscribers internally?](#310-how-does-a-subject-deliver-values-to-subscribers-internally)
- [311: What happens when you subscribe to a BehaviorSubject that has errored?](#311-what-happens-when-you-subscribe-to-a-behaviorsubject-that-has-errored)
- [312: What is the diamond problem in RxJS?](#312-what-is-the-diamond-problem-in-rxjs)
- [313: What does combineLatest emit with synchronous sources?](#313-what-does-combinelatest-emit-with-synchronous-sources)
- [314: How do schedulers work internally?](#314-how-do-schedulers-work-internally)
- [315: What is the queueScheduler good for?](#315-what-is-the-queuescheduler-good-for)
- [316: How does recursive scheduling with this.schedule work?](#316-how-does-recursive-scheduling-with-thisschedule-work)
- [317: How does TestScheduler run mode get virtual time into operators?](#317-how-does-testscheduler-run-mode-get-virtual-time-into-operators)
- [318: Why can Date.now or Promises break marble tests?](#318-why-can-datenow-or-promises-break-marble-tests)
- [319: What is backpressure and how does RxJS handle it?](#319-what-is-backpressure-and-how-does-rxjs-handle-it)
- [320: When would you use async iterators instead of Observables for backpressure?](#320-when-would-you-use-async-iterators-instead-of-observables-for-backpressure)
- [321: What does each operator cost at runtime?](#321-what-does-each-operator-cost-at-runtime)
- [322: How do RxJS timers affect Angular change detection with zone.js?](#322-how-do-rxjs-timers-affect-angular-change-detection-with-zonejs)
- [323: How does RxJS work with zoneless Angular?](#323-how-does-rxjs-work-with-zoneless-angular)
- [324: Why can shareReplay cause a leak even after components are destroyed?](#324-why-can-sharereplay-cause-a-leak-even-after-components-are-destroyed)
- [325: How does share behave after the source errors or completes?](#325-how-does-share-behave-after-the-source-errors-or-completes)
- [326: How do you keep a shared connection open for a short time after the last subscriber leaves?](#326-how-do-you-keep-a-shared-connection-open-for-a-short-time-after-the-last-subscriber-leaves)
- [327: What is the danger of using a Subject as an observer for several sources?](#327-what-is-the-danger-of-using-a-subject-as-an-observer-for-several-sources)
- [328: How should you structure error handling in a large app?](#328-how-should-you-structure-error-handling-in-a-large-app)
- [329: How do you type errors in RxJS?](#329-how-do-you-type-errors-in-rxjs)
- [330: What security issues should you watch for in RxJS code?](#330-what-security-issues-should-you-watch-for-in-rxjs-code)
- [331: How do you validate incoming WebSocket messages?](#331-how-do-you-validate-incoming-websocket-messages)
- [332: Does unsubscribing from an HTTP call stop the work on the server?](#332-does-unsubscribing-from-an-http-call-stop-the-work-on-the-server)
- [333: How do you connect an AbortSignal to RxJS?](#333-how-do-you-connect-an-abortsignal-to-rxjs)
- [334: How do you turn an Observable into an async iterable, and what is the catch?](#334-how-do-you-turn-an-observable-into-an-async-iterable-and-what-is-the-catch)
- [335: What is the native Observable API in browsers?](#335-what-is-the-native-observable-api-in-browsers)
- [336: What is Symbol.observable and why does it exist?](#336-what-is-symbolobservable-and-why-does-it-exist)
- [337: How would you build a small state store on top of RxJS?](#337-how-would-you-build-a-small-state-store-on-top-of-rxjs)
- [338: How do you avoid recalculating derived data for every subscriber?](#338-how-do-you-avoid-recalculating-derived-data-for-every-subscriber)
- [339: What is the difference between batching with debounceTime(0), auditTime(0) and asapScheduler?](#339-what-is-the-difference-between-batching-with-debouncetime0-audittime0-and-asapscheduler)
- [340: How do you drive smooth animations with RxJS?](#340-how-do-you-drive-smooth-animations-with-rxjs)
- [341: What are the problems with a global event bus built on a Subject?](#341-what-are-the-problems-with-a-global-event-bus-built-on-a-subject)
- [342: How do effects and component streams split the work in a well-designed app?](#342-how-do-effects-and-component-streams-split-the-work-in-a-well-designed-app)
- [343: How would you design a real-time dashboard stream?](#343-how-would-you-design-a-real-time-dashboard-stream)
- [344: How do you build a request queue with priorities?](#344-how-do-you-build-a-request-queue-with-priorities)
- [345: How do you implement stale-while-revalidate with RxJS?](#345-how-do-you-implement-stale-while-revalidate-with-rxjs)
- [346: How do you implement undo and redo with scan?](#346-how-do-you-implement-undo-and-redo-with-scan)
- [347: How would you implement a simple circuit breaker as an operator?](#347-how-would-you-implement-a-simple-circuit-breaker-as-an-operator)
- [348: How do you implement a token bucket rate limiter?](#348-how-do-you-implement-a-token-bucket-rate-limiter)
- [349: What happens if a switchMap inner Observable emits synchronously?](#349-what-happens-if-a-switchmap-inner-observable-emits-synchronously)
- [350: How do you avoid a stack overflow with recursive synchronous Observables?](#350-how-do-you-avoid-a-stack-overflow-with-recursive-synchronous-observables)
- [351: Why can a Subject with many subscribers get slow?](#351-why-can-a-subject-with-many-subscribers-get-slow)
- [352: When would you choose plain callbacks or Promises over RxJS?](#352-when-would-you-choose-plain-callbacks-or-promises-over-rxjs)
- [353: What is UnsubscriptionError?](#353-what-is-unsubscriptionerror)
- [354: Is it safe to unsubscribe from inside a next callback?](#354-is-it-safe-to-unsubscribe-from-inside-a-next-callback)
- [355: What happens with takeUntil if the notifier completes without emitting?](#355-what-happens-with-takeuntil-if-the-notifier-completes-without-emitting)
- [356: What happens if the takeUntil notifier emits synchronously on subscribe?](#356-what-happens-if-the-takeuntil-notifier-emits-synchronously-on-subscribe)
- [357: What is the "Zalgo" problem and how does it apply to Observables?](#357-what-is-the-zalgo-problem-and-how-does-it-apply-to-observables)
- [358: What ordering does merge give with synchronous sources?](#358-what-ordering-does-merge-give-with-synchronous-sources)
- [359: Why can concat lose values from a hot source?](#359-why-can-concat-lose-values-from-a-hot-source)
- [360: If one subscriber of a Subject throws, do other subscribers still get the value?](#360-if-one-subscriber-of-a-subject-throws-do-other-subscribers-still-get-the-value)
- [361: How do you test a service that exposes a hot Subject-based stream?](#361-how-do-you-test-a-service-that-exposes-a-hot-subject-based-stream)
- [362: How do you test a polling stream with TestScheduler?](#362-how-do-you-test-a-polling-stream-with-testscheduler)
- [363: How do you test retry with a delay using marbles?](#363-how-do-you-test-retry-with-a-delay-using-marbles)
- [364: What are common pitfalls in marble tests?](#364-what-are-common-pitfalls-in-marble-tests)
- [365: How do you write a custom operator that handles errors thrown by user callbacks?](#365-how-do-you-write-a-custom-operator-that-handles-errors-thrown-by-user-callbacks)
- [366: Why can state inside a custom operator leak between subscribers?](#366-why-can-state-inside-a-custom-operator-leak-between-subscribers)
- [367: How would you implement switchMap yourself?](#367-how-would-you-implement-switchmap-yourself)
- [368: How do you show a loading indicator only if a request takes longer than 300ms?](#368-how-do-you-show-a-loading-indicator-only-if-a-request-takes-longer-than-300ms)
- [369: How do you keep a spinner visible for a minimum time to avoid flicker?](#369-how-do-you-keep-a-spinner-visible-for-a-minimum-time-to-avoid-flicker)
- [370: How do you run requests in parallel but emit results in the original order?](#370-how-do-you-run-requests-in-parallel-but-emit-results-in-the-original-order)
- [371: How do RxJS subscriptions affect Angular SSR?](#371-how-do-rxjs-subscriptions-affect-angular-ssr)
- [372: What is pendingUntilEvent in Angular?](#372-what-is-pendinguntilevent-in-angular)
- [373: What are outputFromObservable and outputToObservable?](#373-what-are-outputfromobservable-and-outputtoobservable)
- [374: How is rxResource different from toSignal?](#374-how-is-rxresource-different-from-tosignal)
- [375: Why are signals glitch-free while RxJS is not?](#375-why-are-signals-glitch-free-while-rxjs-is-not)
- [376: When you migrate a BehaviorSubject service to signals, what should stay in RxJS?](#376-when-you-migrate-a-behaviorsubject-service-to-signals-what-should-stay-in-rxjs)
- [377: What goes wrong when an app has more than one copy of RxJS?](#377-what-goes-wrong-when-an-app-has-more-than-one-copy-of-rxjs)
- [378: How do you keep RxJS bundle cost low?](#378-how-do-you-keep-rxjs-bundle-cost-low)
- [379: How do you process a Node.js stream of jobs with limited concurrency?](#379-how-do-you-process-a-nodejs-stream-of-jobs-with-limited-concurrency)
- [380: How do you acknowledge queue messages only after processing?](#380-how-do-you-acknowledge-queue-messages-only-after-processing)
- [381: How do you shut down a Node.js service built on RxJS gracefully?](#381-how-do-you-shut-down-a-nodejs-service-built-on-rxjs-gracefully)
- [382: What are the trade-offs between Observables and async generators?](#382-what-are-the-trade-offs-between-observables-and-async-generators)
- [383: Why does RxJS not have a dedicated "state" type?](#383-why-does-rxjs-not-have-a-dedicated-state-type)
- [384: How do you protect a BehaviorSubject store from errors?](#384-how-do-you-protect-a-behaviorsubject-store-from-errors)
- [385: Should a library return Observables or Promises?](#385-should-a-library-return-observables-or-promises)
- [386: How do you write an API that accepts either a value or an Observable?](#386-how-do-you-write-an-api-that-accepts-either-a-value-or-an-observable)
- [387: How do you expose cancellation from a function that uses RxJS internally but returns a Promise?](#387-how-do-you-expose-cancellation-from-a-function-that-uses-rxjs-internally-but-returns-a-promise)
- [388: Why are RxJS stack traces hard to read, and what helps?](#388-why-are-rxjs-stack-traces-hard-to-read-and-what-helps)
- [389: How do you avoid many separate subscriptions in an Angular template?](#389-how-do-you-avoid-many-separate-subscriptions-in-an-angular-template)
- [390: How do you keep heavy work in map from freezing the UI?](#390-how-do-you-keep-heavy-work-in-map-from-freezing-the-ui)
- [391: How do you split a large synchronous job into chunks?](#391-how-do-you-split-a-large-synchronous-job-into-chunks)
- [392: Why does interval drift, and how do you build an accurate clock?](#392-why-does-interval-drift-and-how-do-you-build-an-accurate-clock)
- [393: How do background tabs affect RxJS timers?](#393-how-do-background-tabs-affect-rxjs-timers)
- [394: How do you make a countdown correct even if the user's clock is wrong?](#394-how-do-you-make-a-countdown-correct-even-if-the-users-clock-is-wrong)
- [395: Why must retried requests be idempotent?](#395-why-must-retried-requests-be-idempotent)
- [396: What is a retry storm and how do you prevent it?](#396-what-is-a-retry-storm-and-how-do-you-prevent-it)
- [397: How do you make sure a payment is submitted only once?](#397-how-do-you-make-sure-a-payment-is-submitted-only-once)
- [398: How do you stop navigation until pending saves finish?](#398-how-do-you-stop-navigation-until-pending-saves-finish)
- [399: How do you combine an initial HTTP snapshot with WebSocket updates without missing any?](#399-how-do-you-combine-an-initial-http-snapshot-with-websocket-updates-without-missing-any)
- [400: How do you drop stale updates when events can arrive out of order?](#400-how-do-you-drop-stale-updates-when-events-can-arrive-out-of-order)
- [401: How do you use mergeMap but ignore responses from old requests?](#401-how-do-you-use-mergemap-but-ignore-responses-from-old-requests)
- [402: What can go wrong with optimistic updates when edits overlap?](#402-what-can-go-wrong-with-optimistic-updates-when-edits-overlap)
- [403: How would you build an offline queue for writes?](#403-how-would-you-build-an-offline-queue-for-writes)
- [404: A search box sometimes shows results for an older query. How do you debug it?](#404-a-search-box-sometimes-shows-results-for-an-older-query-how-do-you-debug-it)
- [405: Memory keeps growing on a dashboard page that stays open for hours. What do you check?](#405-memory-keeps-growing-on-a-dashboard-page-that-stays-open-for-hours-what-do-you-check)
- [406: The network tab shows the same request twice. What are the usual causes?](#406-the-network-tab-shows-the-same-request-twice-what-are-the-usual-causes)
- [407: A stream works once and then stops reacting after one failed request. Why?](#407-a-stream-works-once-and-then-stops-reacting-after-one-failed-request-why)
- [408: combineLatest never emits. How do you find out why?](#408-combinelatest-never-emits-how-do-you-find-out-why)
- [409: A Jest test with debounceTime times out. What is happening?](#409-a-jest-test-with-debouncetime-times-out-what-is-happening)
- [410: A service pushes a value into a Subject in its constructor, but components never see it. Why?](#410-a-service-pushes-a-value-into-a-subject-in-its-constructor-but-components-never-see-it-why)
- [411: Why does a BehaviorSubject cause ExpressionChangedAfterItHasBeenChecked errors in Angular?](#411-why-does-a-behaviorsubject-cause-expressionchangedafterithasbeenchecked-errors-in-angular)
- [412: forkJoin on two form valueChanges streams never emits. Why?](#412-forkjoin-on-two-form-valuechanges-streams-never-emits-why)
- [413: await lastValueFrom(store.select(...)) hangs. Why?](#413-await-lastvaluefromstoreselect-hangs-why)
- [414: Users report that some of their edits were not saved. The code uses switchMap for saves. What happened?](#414-users-report-that-some-of-their-edits-were-not-saved-the-code-uses-switchmap-for-saves-what-happened)
- [415: How do you show toast notifications one at a time?](#415-how-do-you-show-toast-notifications-one-at-a-time)
- [416: In a chat app, messages sometimes appear twice or out of order. How do you fix it with RxJS?](#416-in-a-chat-app-messages-sometimes-appear-twice-or-out-of-order-how-do-you-fix-it-with-rxjs)
- [417: An autocomplete hits the API's rate limit. What would you change?](#417-an-autocomplete-hits-the-apis-rate-limit-what-would-you-change)
- [418: How do you migrate nested callback code to RxJS step by step?](#418-how-do-you-migrate-nested-callback-code-to-rxjs-step-by-step)
- [419: How would you design a file upload queue with progress, cancel and retry?](#419-how-would-you-design-a-file-upload-queue-with-progress-cancel-and-retry)
- [420: A stock ticker sends hundreds of updates per second and the page lags. How do you fix it?](#420-a-stock-ticker-sends-hundreds-of-updates-per-second-and-the-page-lags-how-do-you-fix-it)
- [421: How do you respect a 429 response with a Retry-After header?](#421-how-do-you-respect-a-429-response-with-a-retry-after-header)
- [422: Many requests fail with 401 at the same time. How do you refresh the token only once?](#422-many-requests-fail-with-401-at-the-same-time-how-do-you-refresh-the-token-only-once)
- [423: How do you write an Angular interceptor that refreshes the token and retries the request?](#423-how-do-you-write-an-angular-interceptor-that-refreshes-the-token-and-retries-the-request)
- [424: How do you cancel all pending requests when the user logs out?](#424-how-do-you-cancel-all-pending-requests-when-the-user-logs-out)
- [425: toSignal with requireSync throws an error. Why?](#425-tosignal-with-requiresync-throws-an-error-why)
- [426: How do you build dependent dropdowns, like country and then city?](#426-how-do-you-build-dependent-dropdowns-like-country-and-then-city)
- [427: How do you search several providers and show results as they arrive?](#427-how-do-you-search-several-providers-and-show-results-as-they-arrive)
- [428: How do you show a "new items available" banner instead of updating the list right away?](#428-how-do-you-show-a-new-items-available-banner-instead-of-updating-the-list-right-away)
- [429: How do you load configuration once at startup in Angular using an Observable?](#429-how-do-you-load-configuration-once-at-startup-in-angular-using-an-observable)
- [430: How do you wrap Server-Sent Events (EventSource) in an Observable?](#430-how-do-you-wrap-server-sent-events-eventsource-in-an-observable)
- [431: How do you show progress for a long server job with RxJS?](#431-how-do-you-show-progress-for-a-long-server-job-with-rxjs)
- [432: How do you sync state across browser tabs?](#432-how-do-you-sync-state-across-browser-tabs)
- [433: How do you batch outgoing changes in a collaborative editor?](#433-how-do-you-batch-outgoing-changes-in-a-collaborative-editor)
- [434: How do you switch implementation at runtime based on a feature flag stream?](#434-how-do-you-switch-implementation-at-runtime-based-on-a-feature-flag-stream)
- [435: Each row in a big list polls its own status. How do you make it cheaper?](#435-each-row-in-a-big-list-polls-its-own-status-how-do-you-make-it-cheaper)
- [436: How do you skip a request when inputs are invalid, and should you use filter or switchMap to EMPTY?](#436-how-do-you-skip-a-request-when-inputs-are-invalid-and-should-you-use-filter-or-switchmap-to-empty)
- [437: How do you implement debounce with a maximum wait?](#437-how-do-you-implement-debounce-with-a-maximum-wait)
- [438: How do you buffer values until a condition is true and then flush them?](#438-how-do-you-buffer-values-until-a-condition-is-true-and-then-flush-them)
- [439: How do you make RxJS code easy to test?](#439-how-do-you-make-rxjs-code-easy-to-test)
- [440: How do you share the current user with many components without many requests?](#440-how-do-you-share-the-current-user-with-many-components-without-many-requests)
- [441: What does it cost to convert between signals and Observables many times?](#441-what-does-it-cost-to-convert-between-signals-and-observables-many-times)
- [442: How do you design a typed action stream with an ofType helper?](#442-how-do-you-design-a-typed-action-stream-with-an-oftype-helper)
- [443: How do you keep side effects out of pure derived streams?](#443-how-do-you-keep-side-effects-out-of-pure-derived-streams)
- [444: What happens if you call subscribe inside a pipe operator callback?](#444-what-happens-if-you-call-subscribe-inside-a-pipe-operator-callback)
- [445: How do you keep a long-lived stream healthy over days of uptime?](#445-how-do-you-keep-a-long-lived-stream-healthy-over-days-of-uptime)
- [446: How do you add a watchdog that reconnects a silent WebSocket?](#446-how-do-you-add-a-watchdog-that-reconnects-a-silent-websocket)
- [447: What do you check in an RxJS code review?](#447-what-do-you-check-in-an-rxjs-code-review)
- [448: Is RxJS still worth learning now that Angular has signals?](#448-is-rxjs-still-worth-learning-now-that-angular-has-signals)
- [449: What is the future of RxJS?](#449-what-is-the-future-of-rxjs)
- [450: How would you introduce RxJS to a team that is new to it?](#450-how-would-you-introduce-rxjs-to-a-team-that-is-new-to-it)

---

# Easy Questions (1-150)

## 1: What is RxJS?

RxJS (Reactive Extensions for JavaScript) is a library for working with values that arrive over time, such as clicks, HTTP responses, timers or WebSocket messages. It gives you one type, the Observable, to represent any such source, and a large set of operators to transform, filter and combine them. Angular uses it heavily, but it works in any JavaScript project, in the browser or in Node.js.

## 2: What problem does RxJS solve?

Async code in JavaScript comes in many shapes: callbacks, events, promises, timers. Mixing them gets messy, especially when you need to cancel things, retry, debounce, or combine several sources. RxJS puts all of them behind the same Observable interface, so you can use the same operators for a click stream, a timer and an HTTP call, and cancel any of them by unsubscribing.

## 3: How do you install RxJS?

```bash
npm install rxjs
```

Everything you normally need is exported from the root `rxjs` package. There are also a few extra entry points: `rxjs/ajax`, `rxjs/fetch`, `rxjs/webSocket` and `rxjs/testing`.

## 4: What is the current stable version of RxJS?

The current stable line is RxJS 7, with 7.8.2 as the latest release on the `latest` npm tag. A new major version is being worked on and is published under the `next` tag as a beta, but production projects (including Angular) use 7.x. Version 7 brought smaller bundles, better TypeScript types, `firstValueFrom` and `lastValueFrom`, and config objects for operators like `share` and `retry`.

## 5: What is an Observable?

An Observable is a lazy source of values over time. It can emit zero or more values, and then either complete or error. Nothing happens until someone subscribes, and each subscription can be cancelled.

```ts
import { Observable } from "rxjs";

const numbers$ = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.complete();
});

numbers$.subscribe((n) => console.log(n)); // 1, 2
```

## 6: What is an Observer?

An Observer is the consumer of an Observable. It is an object with up to three callbacks: `next` for each value, `error` for a failure and `complete` for a normal end. You pass it to `subscribe`.

```ts
numbers$.subscribe({
  next: (value) => console.log("value", value),
  error: (err) => console.error("error", err),
  complete: () => console.log("done"),
});
```

## 7: What is a Subscription?

A Subscription is what `subscribe()` returns. It represents the running execution of an Observable, and its main method is `unsubscribe()`, which stops the execution and runs any cleanup code the Observable set up. You can also group subscriptions with `add()` so one `unsubscribe()` call cleans up all of them.

## 8: What does subscribe do?

Calling `subscribe` starts the Observable. For a cold Observable it runs the function you passed to `new Observable` (or the creation logic of `of`, `interval` and so on), connects it to your observer, and returns a Subscription. Without `subscribe`, an Observable is just a description of work that never runs.

## 9: Why do you need to unsubscribe?

If an Observable never completes on its own, like `interval` or `fromEvent`, it keeps running and keeps a reference to your callbacks. In a component that has been destroyed, that leads to memory leaks and code running on stale state. Unsubscribing stops the source and releases those references. Observables that complete by themselves (like a single HTTP request) clean up on completion.

## 10: What is the difference between an Observable and a Promise?

- A Promise resolves once with one value. An Observable can emit many values.
- A Promise starts working as soon as it is created. An Observable is lazy and starts on subscribe.
- A Promise cannot be cancelled. An Observable subscription can be cancelled with `unsubscribe()`.
- Promise callbacks always run asynchronously. An Observable can emit synchronously.
- Observables have operators like `retry`, `debounceTime` and `switchMap` built in.

## 11: What does it mean that Observables are lazy?

Creating an Observable does not run any code. The producer function runs only when you subscribe, and it runs again for each new subscriber. This is why you can build a pipeline once, store it in a variable, and decide later when (or if) to start it.

```ts
const obs$ = new Observable(() => console.log("started"));
// nothing logged yet
obs$.subscribe(); // "started"
```

## 12: What are the three kinds of notifications an Observable can send?

`next` carries a value and can happen any number of times. `error` carries an error and ends the Observable. `complete` carries nothing and also ends the Observable. After `error` or `complete`, no more notifications are delivered, even if the producer tries to send them.

## 13: What is the Observable contract?

It is the set of rules every Observable follows: zero or more `next` calls, then at most one `error` or `complete`, and nothing after that. Notifications are delivered one at a time, never in parallel. RxJS enforces the "nothing after the end" part for you, so a producer that calls `next` after `complete` is simply ignored.

## 14: What is an operator in RxJS?

An operator is a function that takes an Observable and returns a new Observable. It does not change the source. For example, `map` creates an Observable that emits each source value after passing it through your function. You chain operators with `pipe`.

## 15: What is the pipe method?

`pipe` is a method on every Observable that applies operators one after another and returns the final Observable. It makes the chain readable from top to bottom.

```ts
import { of, map, filter } from "rxjs";

of(1, 2, 3, 4)
  .pipe(
    filter((n) => n % 2 === 0),
    map((n) => n * 10),
  )
  .subscribe(console.log); // 20, 40
```

## 16: What is the difference between a creation function and a pipeable operator?

A creation function makes a new Observable from something else: `of`, `from`, `interval`, `fromEvent`, `combineLatest`. You call it on its own. A pipeable operator takes an existing Observable and returns a changed one: `map`, `filter`, `switchMap`. You pass it into `pipe`.

## 17: Where do you import operators from in RxJS 7?

Since RxJS 7.2 you can import everything, including pipeable operators, from `rxjs`. The older path `rxjs/operators` still works but is no longer needed.

```ts
import { of, map, filter, switchMap } from "rxjs";
```

## 18: What does the dollar sign at the end of a variable name mean?

It is just a naming convention that says "this variable holds an Observable", for example `user$` or `clicks$`. RxJS does not require it, but it helps readers tell a stream apart from a plain value, for example `user$` versus `user`.

## 19: What does the of function do?

`of` creates an Observable that emits the arguments you pass, one by one and synchronously, and then completes.

```ts
import { of } from "rxjs";

of("a", "b", "c").subscribe(console.log); // a, b, c
```

## 20: What does the from function do?

`from` turns something else into an Observable: an array, a Promise, an iterable, an async iterable, another Observable, or a `ReadableStream`. For an array it emits each item and then completes. For a Promise it emits the resolved value and completes, or errors if the Promise rejects.

```ts
import { from } from "rxjs";

from([10, 20, 30]).subscribe(console.log);
from(fetch("/api/user")).subscribe((res) => console.log(res.status));
```

## 21: What is the difference between of and from with an array?

`of([1, 2, 3])` emits the whole array once as a single value. `from([1, 2, 3])` emits `1`, `2` and `3` as three separate values.

## 22: What does interval do?

`interval(ms)` emits increasing numbers starting at 0, one every `ms` milliseconds, forever. You usually stop it with `take`, `takeUntil` or by unsubscribing.

```ts
import { interval, take } from "rxjs";

interval(1000).pipe(take(3)).subscribe(console.log); // 0, 1, 2
```

## 23: What does timer do?

`timer(due)` waits for `due` milliseconds (or until a `Date`), emits `0` and completes. With a second argument, `timer(due, period)`, it keeps emitting every `period` milliseconds after the first one, like an `interval` with a custom start delay.

```ts
import { timer } from "rxjs";

timer(2000).subscribe(() => console.log("two seconds later"));
timer(0, 5000).subscribe((n) => console.log("poll", n)); // starts right away
```

## 24: What does fromEvent do?

`fromEvent` creates an Observable from DOM events, Node.js `EventEmitter` events or similar targets. It adds the listener on subscribe and removes it on unsubscribe, so you don't have to call `removeEventListener` yourself.

```ts
import { fromEvent } from "rxjs";

const clicks$ = fromEvent<MouseEvent>(document, "click");
const sub = clicks$.subscribe((e) => console.log(e.clientX));
// later
sub.unsubscribe(); // listener removed
```

## 25: What is EMPTY?

`EMPTY` is a constant Observable that emits nothing and completes right away. It is handy when you need to return "no values" from a function that must return an Observable, for example inside `catchError` or `switchMap` when there is nothing to do.

## 26: What is NEVER?

`NEVER` is a constant Observable that never emits, never errors and never completes. It is mostly used in tests, or to keep something "open" on purpose.

## 27: How do you create an Observable that errors?

Use `throwError` with a factory function. The factory is called when someone subscribes, so a new error is created for each subscriber.

```ts
import { throwError } from "rxjs";

const failed$ = throwError(() => new Error("Something went wrong"));
failed$.subscribe({ error: (err) => console.error(err.message) });
```

The old form `throwError(error)` that takes the error value directly is deprecated.

## 28: What does range do?

`range(start, count)` emits `count` numbers in a row, starting at `start`, synchronously, then completes.

```ts
import { range } from "rxjs";

range(5, 3).subscribe(console.log); // 5, 6, 7
```

## 29: What does defer do?

`defer` takes a factory function and calls it each time someone subscribes. Whatever Observable (or Promise, or array) the factory returns is what that subscriber gets. It is the standard way to make work start on subscribe instead of when the code is first run.

```ts
import { defer } from "rxjs";

const now$ = defer(() => of(Date.now()));
// each subscriber gets the time of its own subscription
```

## 30: Why would you wrap a Promise in defer?

A Promise starts as soon as you create it. `from(fetch(url))` sends the request immediately, even if nobody subscribes, and every subscriber shares that one result. `defer(() => fetch(url))` sends the request only on subscribe and sends a new one for each subscriber, which also makes `retry` work, because retrying resubscribes and creates a new request.

## 31: What does map do?

`map` applies a function to each value and emits the result. It works like `Array.prototype.map`, but over time.

```ts
import { of, map } from "rxjs";

of(1, 2, 3)
  .pipe(map((n) => n * 2))
  .subscribe(console.log); // 2, 4, 6
```

## 32: What does filter do?

`filter` lets a value through only if your function returns `true` for it. Values that fail the check are dropped.

```ts
of(1, 2, 3, 4)
  .pipe(filter((n) => n > 2))
  .subscribe(console.log); // 3, 4
```

## 33: What does tap do?

`tap` runs a side effect for each notification without changing the stream. People use it for logging, debugging, or setting a loading flag. The value goes through unchanged.

```ts
import { of, tap, map } from "rxjs";

of(1, 2)
  .pipe(
    tap((n) => console.log("before", n)),
    map((n) => n * 10),
  )
  .subscribe();
```

## 34: Why should you not change data inside map with side effects?

`map` is meant to return a new value from an input. Putting side effects in it (like writing to a store or calling an API) makes the code harder to read and test, because a reader expects `map` to be pure. Put side effects in `tap` or in the `subscribe` callback, so it is clear where they happen.

## 35: What does take do?

`take(n)` emits the first `n` values and then completes, unsubscribing from the source. It is one of the simplest ways to make an endless stream finite.

```ts
interval(500).pipe(take(2)).subscribe(console.log); // 0, 1, then completes
```

## 36: What does first do?

`first()` emits the first value and completes. You can pass a predicate to get the first value that matches. If the source completes without any matching value, `first` errors with `EmptyError`, unless you pass a default value as the second argument.

```ts
import { of, first } from "rxjs";

of(1, 5, 8)
  .pipe(first((n) => n > 4))
  .subscribe(console.log); // 5
of().pipe(first(undefined, "none")).subscribe(console.log); // 'none'
```

## 37: What is the difference between take(1) and first()?

Both emit one value and complete. The difference is what happens if the source completes with no values: `take(1)` just completes quietly, while `first()` errors with `EmptyError`. Use `first()` when "no value" is a real bug you want to know about, and `take(1)` when an empty result is fine.

## 38: What does last do?

`last()` waits for the source to complete and then emits the last value (or the last value that matches a predicate). Like `first`, it errors with `EmptyError` if there was nothing to emit and no default value was given. It never emits if the source never completes.

## 39: What does skip do?

`skip(n)` ignores the first `n` values and emits everything after that.

```ts
of(1, 2, 3, 4).pipe(skip(2)).subscribe(console.log); // 3, 4
```

## 40: What does distinctUntilChanged do?

It drops a value if it is equal to the value right before it. By default it compares with `===`. You can pass your own compare function, or use `distinctUntilKeyChanged` to compare one property.

```ts
import { of, distinctUntilChanged } from "rxjs";

of(1, 1, 2, 2, 1).pipe(distinctUntilChanged()).subscribe(console.log); // 1, 2, 1
```

## 41: What is the difference between distinct and distinctUntilChanged?

`distinctUntilChanged` only compares with the previous value, so a value can appear again later. `distinct` remembers every value it has seen and never lets a repeat through. Because `distinct` keeps a growing set in memory, be careful using it on long-running streams. You can pass a `flushes` Observable as the second argument to clear that set.

## 42: What does debounceTime do?

`debounceTime(ms)` waits until the source has been quiet for `ms` milliseconds, then emits the latest value. If a new value arrives before the time is up, the timer restarts. It is the usual choice for search inputs, so you only search after the user stops typing.

```ts
import { fromEvent, map, debounceTime } from "rxjs";

fromEvent<InputEvent>(input, "input")
  .pipe(
    map((e) => (e.target as HTMLInputElement).value),
    debounceTime(300),
  )
  .subscribe((term) => console.log("search", term));
```

## 43: What does throttleTime do?

`throttleTime(ms)` emits a value, then ignores new values for `ms` milliseconds, then lets the next one through. By default it emits the first value of each window (leading). You can change that with `{ leading, trailing }`. It is good for things like scroll or resize handlers where you want regular updates, not every single event.

## 44: What does scan do?

`scan` works like `Array.prototype.reduce`, but it emits the running result after every value instead of only at the end. It is often used to keep state, like a counter or a list, inside a stream.

```ts
import { of, scan } from "rxjs";

of(1, 2, 3)
  .pipe(scan((total, n) => total + n, 0))
  .subscribe(console.log); // 1, 3, 6
```

## 45: What is the difference between scan and reduce?

`scan` emits the accumulated value after each source value. `reduce` keeps the accumulated value to itself and emits only once, when the source completes. So `reduce` never emits for a stream that never completes, while `scan` keeps working.

## 46: What does startWith do?

`startWith` emits one or more values right when you subscribe, before anything from the source. It is useful for giving a stream an initial value, for example an empty search term or a "loading" state.

```ts
import { fromEvent, map, startWith } from "rxjs";

const width$ = fromEvent(window, "resize").pipe(
  map(() => window.innerWidth),
  startWith(window.innerWidth),
);
```

## 47: What does endWith do?

`endWith` emits the values you give it after the source completes, and then completes. If the source errors or never completes, those values are never emitted.

## 48: What does catchError do?

`catchError` catches an error from the source and lets you replace it with another Observable. You can return a fallback value, return `EMPTY` to finish quietly, or throw a new error. The original source is done at that point; `catchError` does not keep it running.

```ts
import { catchError, of } from "rxjs";

http.get("/api/items").pipe(
  catchError((err) => {
    console.error(err);
    return of([]); // fall back to an empty list
  }),
);
```

## 49: What does finalize do?

`finalize` runs a callback when the subscription ends for any reason: the source completes, errors, or the subscriber unsubscribes. It is a good place to hide a loading spinner or release a resource.

```ts
import { finalize } from "rxjs";

loading = true;
http
  .get("/api/data")
  .pipe(finalize(() => (loading = false)))
  .subscribe();
```

## 50: What does delay do?

`delay(ms)` shifts every notification in time by `ms` milliseconds. You can also pass a `Date`, and then values are held until that time. Errors are not delayed; they go through right away.

## 51: What does toArray do?

`toArray` collects all values from the source into one array and emits that array when the source completes.

```ts
import { of, toArray } from "rxjs";

of(1, 2, 3).pipe(toArray()).subscribe(console.log); // [1, 2, 3]
```

## 52: What does count do?

`count` emits how many values the source emitted, once it completes. You can pass a predicate to count only values that match.

## 53: What do max and min do?

They wait for the source to complete and emit the largest or smallest value. For objects you pass a compare function, for example `max((a, b) => a.age - b.age)`.

## 54: What does pairwise do?

`pairwise` emits the previous and the current value together as a two-item array, starting from the second value. It is useful for comparing old and new values, like scroll direction.

```ts
import { of, pairwise } from "rxjs";

of(1, 4, 9).pipe(pairwise()).subscribe(console.log); // [1, 4], [4, 9]
```

## 55: What does takeWhile do?

`takeWhile` emits values while a condition is true, and completes as soon as a value fails it. Pass `true` as the second argument if you also want the value that failed to be emitted.

```ts
of(1, 2, 3, 1)
  .pipe(takeWhile((n) => n < 3))
  .subscribe(console.log); // 1, 2
```

## 56: What does skipWhile do?

`skipWhile` drops values while a condition is true. Once one value fails the condition, it lets that value and everything after it through, and never checks again.

## 57: What does takeUntil do?

`takeUntil(notifier$)` mirrors the source until `notifier$` emits a value, then completes. It is a common way to stop a stream when something happens, like a component being destroyed or a "cancel" button being clicked.

```ts
import { interval, fromEvent, takeUntil } from "rxjs";

const stop$ = fromEvent(stopButton, "click");
interval(1000).pipe(takeUntil(stop$)).subscribe(console.log);
```

## 58: What does takeLast do?

`takeLast(n)` waits for the source to complete and then emits the last `n` values. It keeps a buffer of `n` values in memory while waiting.

## 59: What does skipLast do?

`skipLast(n)` emits all values except the last `n`. To know which values are "last", it holds back `n` values at a time, so each value is emitted only after `n` more have arrived.

## 60: What does elementAt do?

`elementAt(index)` emits only the value at the given zero-based position and then completes. If the source completes before that position, it errors with `ArgumentOutOfRangeError`, unless you pass a default value.

## 61: What do find and findIndex do?

`find` emits the first value that matches a predicate and completes. `findIndex` emits the position of that value. If nothing matches, `find` emits `undefined` and `findIndex` emits `-1` when the source completes. Unlike `first`, they do not error on no match.

## 62: What does every do?

`every` emits `true` if all values pass a predicate, once the source completes. As soon as one value fails, it emits `false` and completes right away.

## 63: What does isEmpty do?

`isEmpty` emits `true` if the source completes without emitting anything, or `false` as soon as the source emits its first value.

## 64: What does defaultIfEmpty do?

If the source completes without emitting anything, `defaultIfEmpty(value)` emits `value` before completing. If the source does emit, it passes values through unchanged.

```ts
import { EMPTY, defaultIfEmpty } from "rxjs";

EMPTY.pipe(defaultIfEmpty("nothing here")).subscribe(console.log);
```

## 65: What does throwIfEmpty do?

It makes the stream error if the source completes without emitting anything. By default the error is `EmptyError`, and you can pass a factory for your own error.

## 66: What does ignoreElements do?

`ignoreElements` drops all `next` values but still passes through `error` and `complete`. Use it when you only care about when something finishes, not what it emits.

## 67: What does single do?

`single` expects the source to emit exactly one value (or exactly one value matching a predicate). If there are none it errors with `EmptyError`, and if there is more than one it errors with `SequenceError`. It is a strict check, useful when "more than one" would mean a bug.

## 68: What does distinctUntilKeyChanged do?

It is a shortcut for `distinctUntilChanged` that compares one property of each object.

```ts
import { of, distinctUntilKeyChanged } from "rxjs";

of({ id: 1 }, { id: 1 }, { id: 2 })
  .pipe(distinctUntilKeyChanged("id"))
  .subscribe(console.log); // { id: 1 }, { id: 2 }
```

## 69: What is a Subject?

A Subject is both an Observable and an Observer. You can subscribe to it, and you can also push values into it with `next()`, `error()` and `complete()`. Every value you push goes to all current subscribers, so a Subject is a simple way to share one stream with many listeners.

```ts
import { Subject } from "rxjs";

const messages = new Subject<string>();
messages.subscribe((m) => console.log("A", m));
messages.subscribe((m) => console.log("B", m));
messages.next("hello"); // A hello, B hello
```

## 70: What is a BehaviorSubject?

A `BehaviorSubject` is a Subject that always has a current value. You give it an initial value, and every new subscriber gets the current value right away, then the next ones. You can also read the value synchronously with `getValue()` or the `value` property.

```ts
import { BehaviorSubject } from "rxjs";

const count = new BehaviorSubject(0);
count.subscribe(console.log); // 0
count.next(1); // 1
console.log(count.value); // 1
```

## 71: What is a ReplaySubject?

A `ReplaySubject` records values and replays them to new subscribers. You choose how many values to keep (`bufferSize`) and optionally for how long (`windowTime`). Unlike `BehaviorSubject`, it has no initial value, so a new subscriber gets nothing until a value has been pushed.

```ts
import { ReplaySubject } from "rxjs";

const last2 = new ReplaySubject<number>(2);
last2.next(1);
last2.next(2);
last2.next(3);
last2.subscribe(console.log); // 2, 3
```

## 72: What is an AsyncSubject?

An `AsyncSubject` only emits the last value it received, and only when it completes. All subscribers, even late ones, get that one last value. It behaves a lot like a Promise and is rarely needed in modern code.

## 73: What is the difference between Subject, BehaviorSubject and ReplaySubject?

- `Subject` has no memory. Late subscribers miss earlier values.
- `BehaviorSubject` remembers the current value and needs an initial one. New subscribers get the current value right away.
- `ReplaySubject` remembers the last `n` values (or values from a time window) and replays them all to new subscribers. It has no initial value.

## 74: What is a hot Observable?

A hot Observable produces values whether or not anyone is subscribed, and all subscribers share the same values. Mouse events, a WebSocket that is already open, or a Subject are hot. If you subscribe late, you miss what was emitted before.

## 75: What is a cold Observable?

A cold Observable starts producing values only when you subscribe, and each subscriber gets its own separate run. `of`, `interval` and Angular's `HttpClient` calls are cold. Two subscribers to a cold HTTP Observable send two requests.

## 76: How do you make a cold Observable hot?

You share one execution between subscribers, usually with the `share` or `shareReplay` operator, or with a Subject. Then the first subscriber starts the source and later subscribers join the same run instead of starting a new one.

```ts
import { interval, share } from "rxjs";

const shared$ = interval(1000).pipe(share());
shared$.subscribe((n) => console.log("A", n));
shared$.subscribe((n) => console.log("B", n)); // same numbers as A
```

## 77: What is multicasting?

Multicasting means one source execution is delivered to many subscribers. A plain cold Observable is unicast: each subscriber gets its own execution. Subjects, `share`, `shareReplay` and `connectable` turn it into multicast, which avoids repeating work like HTTP requests.

## 78: What is a marble diagram?

A marble diagram is a drawing of a stream over time. A line is the time axis, circles (marbles) are emitted values, a vertical bar `|` is completion and an `X` is an error. The RxJS docs use them to show what each operator does, with the input stream on top and the output stream below. The same idea is used in text form for marble tests.

## 79: What is the difference between push and pull?

In a pull system the consumer asks for data when it wants it, like calling a function or `iterator.next()`. In a push system the producer decides when to send data and the consumer reacts, like event listeners. Promises and Observables are push systems: the Observable decides when to call `next`.

## 80: Can an Observable emit synchronously?

Yes. `of(1, 2, 3)` emits all three values during the `subscribe` call, before `subscribe` returns. Observables are only async when the source is async, like a timer, an event or an HTTP call. This is different from Promises, whose `then` callbacks are always async.

```ts
console.log("before");
of(1).subscribe((v) => console.log(v));
console.log("after");
// before, 1, after
```

## 81: How do you convert an Observable to a Promise?

Use `firstValueFrom` to get a Promise of the first value, or `lastValueFrom` to get a Promise of the last value when the source completes. `firstValueFrom` unsubscribes as soon as it has the first value.

```ts
import { firstValueFrom, lastValueFrom } from "rxjs";

const user = await firstValueFrom(user$);
const total = await lastValueFrom(numbers$.pipe(reduce((a, b) => a + b)));
```

## 82: Why is toPromise deprecated?

`toPromise()` resolved with the last value, and if the source completed with no values it resolved with `undefined`, which hid bugs. Its name also didn't say whether you got the first or last value. RxJS 7 replaced it with `firstValueFrom` and `lastValueFrom`, which say exactly what they do and reject with `EmptyError` if there was no value (unless you pass `{ defaultValue }`).

## 83: What happens if you call firstValueFrom on an Observable that never emits?

The Promise never settles, and the subscription stays open. With `interval` or `NEVER`, your `await` just hangs. If the source completes without emitting, the Promise rejects with `EmptyError`. Add a `timeout` or a `defaultValue` if a value may not come.

## 84: How do you handle errors inside subscribe?

Pass an observer object with an `error` callback. If you don't, an error that reaches the end of the chain is reported as an unhandled error (thrown asynchronously, so it appears in the console or your global error handler).

```ts
source$.subscribe({
  next: (v) => console.log(v),
  error: (err) => console.error("failed", err),
});
```

## 85: Why is passing three separate callbacks to subscribe deprecated?

`subscribe(next, error, complete)` with positional callbacks is deprecated because it is hard to read, especially when you need to pass `null` to skip one: `subscribe(null, null, () => ...)`. Use an observer object instead. Passing a single `next` function, `subscribe(v => ...)`, is still fine.

## 86: What does merge do?

`merge` subscribes to several Observables at once and emits values from all of them as they come, in the order they arrive. It completes when all of them complete, and errors as soon as any of them errors.

```ts
import { merge, fromEvent } from "rxjs";

const clicks$ = fromEvent(document, "click");
const keys$ = fromEvent(document, "keydown");
merge(clicks$, keys$).subscribe(() => console.log("user activity"));
```

## 87: What does concat do?

`concat` subscribes to Observables one at a time, in order. It waits for the first one to complete before subscribing to the next. The output is all values from the first, then all from the second, and so on.

```ts
import { concat, of, timer, map } from "rxjs";

concat(of("start"), timer(1000).pipe(map(() => "one second later"))).subscribe(
  console.log,
);
```

## 88: What is the difference between merge and concat?

`merge` runs all sources at the same time and mixes their values. `concat` runs them one after another and keeps their order. If the first source in `concat` never completes, the others never start.

## 89: What does combineLatest do?

`combineLatest` takes several Observables and, once each has emitted at least one value, emits an array (or object) with the latest value from each. After that it emits again every time any of them emits.

```ts
import { combineLatest } from "rxjs";

combineLatest([firstName$, lastName$]).subscribe(([first, last]) => {
  console.log(`${first} ${last}`);
});
```

## 90: Why does combineLatest not emit sometimes?

It waits until every input has emitted at least once. If one input never emits (for example a Subject that nobody has called `next` on yet), `combineLatest` never emits. The usual fix is to give that input a starting value with `startWith`, or to use a `BehaviorSubject`.

## 91: Can you pass an object to combineLatest?

Yes. Since RxJS 7 you can pass a dictionary of Observables, and it emits objects with the same keys. This reads better than an array when you combine many streams.

```ts
combineLatest({ user: user$, settings: settings$ }).subscribe(
  ({ user, settings }) => console.log(user.name, settings.theme),
);
```

## 92: What does forkJoin do?

`forkJoin` subscribes to several Observables in parallel, waits for all of them to complete, and then emits one array (or object) with the last value of each. It is the RxJS version of `Promise.all`, and fits well with HTTP calls, which emit once and complete.

```ts
import { forkJoin } from "rxjs";

forkJoin({
  user: http.get("/api/user"),
  orders: http.get("/api/orders"),
}).subscribe(({ user, orders }) => console.log(user, orders));
```

## 93: What happens with forkJoin if one source errors or completes empty?

If any source errors, `forkJoin` errors right away and unsubscribes from the rest; you lose the results that already came in. If any source completes without emitting, `forkJoin` completes without emitting anything. If you want the other results anyway, add `catchError` to each inner source to turn errors into a fallback value.

## 94: What does zip do?

`zip` pairs values by position: the first value of each source together, then the second of each, and so on. It waits until every source has a value at that position. It completes when any source completes and has no more buffered values to pair.

```ts
import { zip, of } from "rxjs";

zip(of("a", "b", "c"), of(1, 2)).subscribe(console.log); // ['a', 1], ['b', 2]
```

## 95: What does race do?

`race` subscribes to several Observables and mirrors whichever one emits first (or errors or completes first). It unsubscribes from all the others at that moment. It is useful for "whichever answers first" logic, like a request against a timeout.

## 96: What does withLatestFrom do?

`withLatestFrom(other$)` combines each value from the main source with the latest value from `other$`. Only the main source triggers emissions; changes in `other$` alone emit nothing. If `other$` has not emitted yet, values from the main source are dropped.

```ts
import { fromEvent, withLatestFrom } from "rxjs";

fromEvent(saveButton, "click")
  .pipe(withLatestFrom(form$))
  .subscribe(([, formValue]) => save(formValue));
```

## 97: What is the difference between combineLatest and withLatestFrom?

With `combineLatest`, any source emitting triggers an output. With `withLatestFrom`, only the main source triggers output, and the other source is just read for its latest value. Use `withLatestFrom` when one stream is the "action" and the others are only context.

## 98: What does switchMap do?

`switchMap` maps each value to an inner Observable and subscribes to it. When a new value arrives, it unsubscribes from the previous inner Observable and switches to the new one. That cancels old work, which is what you want for search-as-you-type or loading data for the selected item.

```ts
import { switchMap } from "rxjs";

searchTerm$
  .pipe(switchMap((term) => http.get(`/api/search?q=${term}`)))
  .subscribe((results) => console.log(results));
```

## 99: What does mergeMap do?

`mergeMap` (also called `flatMap` in older code) maps each value to an inner Observable and subscribes to all of them at the same time. Results come out in whatever order they finish. Nothing gets cancelled. You can pass a second argument to limit how many inner subscriptions run at once.

```ts
import { from, mergeMap } from "rxjs";

from(ids)
  .pipe(mergeMap((id) => http.get(`/api/items/${id}`), 3)) // at most 3 at a time
  .subscribe(console.log);
```

## 100: What does concatMap do?

`concatMap` maps each value to an inner Observable, but only subscribes to one at a time. The next inner Observable waits until the current one completes. Order is kept, and nothing is cancelled. It is a good fit when the order of requests matters, like saving edits one after another.

## 101: What does exhaustMap do?

`exhaustMap` maps a value to an inner Observable and, while that inner Observable is still running, ignores any new source values. When it completes, the next source value is accepted. This is the usual choice for a login or submit button, so double clicks don't send two requests.

```ts
import { fromEvent, exhaustMap } from "rxjs";

fromEvent(loginButton, "click")
  .pipe(exhaustMap(() => http.post("/api/login", credentials)))
  .subscribe();
```

## 102: How do you choose between switchMap, mergeMap, concatMap and exhaustMap?

Ask what should happen when a new value arrives while the previous inner work is still running:

- Cancel the old one and start the new one: `switchMap` (search, route params).
- Run both in parallel: `mergeMap` (independent deletes, logging).
- Queue the new one until the old one finishes: `concatMap` (ordered saves).
- Ignore the new one: `exhaustMap` (login, submit, refresh button).

## 103: What is a higher-order Observable?

It is an Observable whose values are themselves Observables. For example, `clicks$.pipe(map(() => http.get(url)))` emits an Observable per click, not the HTTP result. You "flatten" it with `switchMap`, `mergeMap`, `concatMap` or `exhaustMap` (or `switchAll`, `mergeAll`, `concatAll`, `exhaustAll`) to get the inner values.

## 104: What is the problem with nesting subscribe calls?

Code like `a$.subscribe(a => b$.subscribe(b => ...))` is hard to read, does not cancel the inner subscription when a new outer value comes, and leaks inner subscriptions because nobody keeps track of them. Errors in the inner stream are also easy to miss. Use a flattening operator like `switchMap` instead and subscribe once at the end.

## 105: What does mergeAll do?

`mergeAll` takes a higher-order Observable and subscribes to every inner Observable as it arrives, merging their values. `mergeMap(fn)` is the same as `map(fn)` followed by `mergeAll()`. `switchAll`, `concatAll` and `exhaustAll` do the same for the other strategies.

## 106: What is an ObservableInput?

`ObservableInput` is the type for anything RxJS can turn into an Observable: an Observable, a Promise, an array or array-like, an iterable, an async iterable, or a `ReadableStream`. Operators like `switchMap`, `mergeMap` and `from` accept any of these, so you can return a Promise from `switchMap` directly.

```ts
userId$.pipe(
  switchMap((id) => fetch(`/api/users/${id}`).then((r) => r.json())),
);
```

## 107: What does retry do?

`retry(n)` resubscribes to the source up to `n` times when it errors. If all attempts fail, the last error is passed on. Because it resubscribes, it only helps with cold sources that redo their work on subscribe, like an HTTP call.

```ts
import { retry } from "rxjs";

http.get("/api/data").pipe(retry(3)).subscribe();
```

## 108: What does repeat do?

`repeat(n)` resubscribes to the source after it completes, `n` times in total. Without an argument it repeats forever. With a config object you can add a delay between repeats, which makes simple polling easy.

```ts
import { repeat } from "rxjs";

http
  .get("/api/status")
  .pipe(repeat({ delay: 5000 }))
  .subscribe(console.log);
```

## 109: What does timeout do?

`timeout` errors with a `TimeoutError` if the source takes too long. `timeout(5000)` means "error if no value arrives within 5 seconds of subscribing or of the previous value". With a config object you can set different limits for the first value and for gaps between values, or switch to a fallback Observable instead of erroring.

```ts
import { timeout, of } from "rxjs";

http.get("/api/slow").pipe(timeout({ first: 5000, with: () => of(null) }));
```

## 110: What does auditTime do?

`auditTime(ms)` starts a timer when a value arrives and ignores further values until the timer ends, then emits the most recent value. It is like a throttle that emits the last value of each window instead of the first. It works well for things like mouse move where you want the latest position at a steady rate.

## 111: What does sampleTime do?

`sampleTime(ms)` checks the source every `ms` milliseconds and emits the latest value if a new one has arrived since the last check. The timing is driven by a fixed clock, not by when values arrive.

## 112: What is the difference between debounceTime and throttleTime?

`debounceTime` waits for silence and emits once the user stops, so a burst of events gives one value at the end. `throttleTime` emits at most once per time window during the burst, so you get regular values while events keep coming. Use debounce for "do it when they are done" (search box) and throttle for "do it now, but not too often" (scroll handler).

## 113: What does bufferTime do?

`bufferTime(ms)` collects values into an array and emits the array every `ms` milliseconds, even if it is empty. It is handy for batching, like sending analytics events in groups.

```ts
import { bufferTime, filter } from "rxjs";

events$
  .pipe(
    bufferTime(2000),
    filter((batch) => batch.length > 0),
  )
  .subscribe((batch) => sendToServer(batch));
```

## 114: What does bufferCount do?

`bufferCount(size)` collects values into arrays of `size` items and emits each array when it is full. When the source completes, any leftover values are emitted as a shorter array. A second argument, `startBufferEvery`, lets you make sliding windows.

## 115: What does buffer do?

`buffer(notifier$)` collects source values and emits them as an array each time `notifier$` emits. For example, you can collect clicks and emit them whenever a timer or another event fires.

## 116: What does the async pipe do in Angular?

The `async` pipe subscribes to an Observable in the template, shows its latest value, and unsubscribes automatically when the component is destroyed. It also marks the component for change detection when a new value comes in, so it works with `OnPush`.

```html
@if (user$ | async; as user) {
<p>{{ user.name }}</p>
}
```

## 117: Does Angular HttpClient return a hot or cold Observable?

Cold. The request is only sent when you subscribe, and every subscription sends a new request. If two parts of the template subscribe with two `async` pipes, you get two requests, unless you share the result with `shareReplay` or convert it to a signal once.

## 118: Do you need to unsubscribe from Angular HttpClient calls?

The Observable completes after the response, so it cleans itself up, and forgetting to unsubscribe does not leak. But unsubscribing still matters when a request may be slow and the user leaves the page: unsubscribing cancels the request and stops your callback from running on a destroyed component. Using `takeUntilDestroyed`, the `async` pipe, or `toSignal` handles this for you.

## 119: What is takeUntilDestroyed in Angular?

`takeUntilDestroyed` from `@angular/core/rxjs-interop` completes the stream when the component, directive or service is destroyed. Called in an injection context (like a constructor or field initializer) it finds the `DestroyRef` on its own. Outside one, you pass a `DestroyRef`.

```ts
import { Component, inject } from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";
import { interval } from "rxjs";

@Component({ selector: "app-clock", template: "" })
export class Clock {
  constructor() {
    interval(1000)
      .pipe(takeUntilDestroyed())
      .subscribe((n) => console.log(n));
  }
}
```

## 120: What is toSignal in Angular?

`toSignal` from `@angular/core/rxjs-interop` subscribes to an Observable and gives you a signal with its latest value. It unsubscribes when the injection context is destroyed. Because an Observable may not have a value right away, the signal is `undefined` until the first emission unless you pass `initialValue` or `requireSync: true`.

```ts
import { toSignal } from "@angular/core/rxjs-interop";

user = toSignal(this.http.get<User>("/api/user"), { initialValue: null });
```

## 121: What is a Subscription's add method for?

`add` attaches another Subscription, or a teardown function, to a parent Subscription. When the parent is unsubscribed, everything added to it is cleaned up too. It is a simple way to manage several subscriptions with one call.

```ts
const subs = new Subscription();
subs.add(a$.subscribe());
subs.add(b$.subscribe());
subs.add(() => console.log("cleanup"));
subs.unsubscribe(); // all three cleaned up
```

## 122: What is teardown logic?

Teardown logic is cleanup code that runs when a subscription ends. In `new Observable`, you return a function (or a Subscription) from the subscribe function, and RxJS calls it on unsubscribe, error or complete. It is where you clear timers, remove listeners or close sockets.

```ts
const ticks$ = new Observable<number>((subscriber) => {
  let i = 0;
  const id = setInterval(() => subscriber.next(i++), 1000);
  return () => clearInterval(id);
});
```

## 123: What is the closed property of a Subscription?

`closed` is `true` once the subscription has ended, either because you called `unsubscribe()` or because the source completed or errored. Inside `new Observable`, `subscriber.closed` tells your producer that nobody is listening anymore, so it can stop doing work, for example inside a loop.

## 124: What happens if you subscribe to the same cold Observable twice?

Each subscription runs the producer separately. Two subscriptions to `interval(1000)` give two independent timers, and two subscriptions to an HTTP Observable send two requests. If you want them to share one run, use `share` or `shareReplay`.

## 125: What is the difference between share and shareReplay?

Both share one source subscription between many subscribers. `share` gives late subscribers only the values emitted after they join. `shareReplay(n)` also replays the last `n` values to late subscribers, so it is the common choice for caching an HTTP result.

```ts
import { shareReplay } from "rxjs";

config$ = http
  .get("/api/config")
  .pipe(shareReplay({ bufferSize: 1, refCount: true }));
```

## 126: What does iif do?

`iif(condition, trueResult$, falseResult$)` decides at subscribe time which of two Observables to subscribe to, based on a function that returns a boolean. It is like a lazy `if` for streams.

```ts
import { iif, of } from "rxjs";

const data$ = iif(() => cache.has(key), of(cache.get(key)), http.get(url));
```

## 127: What does generate do?

`generate` creates an Observable using a loop-like setup: an initial state, a condition, an iterate step and an optional result selector. It emits synchronously, like a `for` loop.

```ts
import { generate } from "rxjs";

generate({
  initialState: 1,
  condition: (x) => x <= 16,
  iterate: (x) => x * 2,
}).subscribe(console.log); // 1, 2, 4, 8, 16
```

## 128: What does partition do?

`partition(source$, predicate)` splits one Observable into two: the first gets values that pass the predicate, the second gets values that fail it.

```ts
import { partition, of } from "rxjs";

const [evens$, odds$] = partition(of(1, 2, 3, 4), (n) => n % 2 === 0);
```

## 129: What does fromEventPattern do?

`fromEventPattern` makes an Observable from any API with add and remove handler functions, when `fromEvent` doesn't fit. You pass a function that adds the handler and a function that removes it.

```ts
import { fromEventPattern } from "rxjs";

const changes$ = fromEventPattern(
  (handler) => editor.on("change", handler),
  (handler) => editor.off("change", handler),
);
```

## 130: What is isObservable?

`isObservable(value)` returns `true` if the value is an RxJS Observable (or looks like one). It is useful in functions that accept either a plain value or an Observable.

## 131: What is the RxJS pipe function, separate from the pipe method?

`pipe` is also exported as a standalone function. It joins several operators into one reusable operator, which you can then use in many `.pipe()` calls.

```ts
import { pipe, filter, map } from "rxjs";

const evenTimesTen = pipe(
  filter((n: number) => n % 2 === 0),
  map((n) => n * 10),
);

of(1, 2, 3, 4).pipe(evenTimesTen).subscribe(console.log); // 20, 40
```

## 132: What is a custom operator?

It is your own function that takes an Observable and returns an Observable. The easiest way to write one is to combine existing operators with the `pipe` function. Custom operators keep repeated logic in one place and make pipelines shorter.

```ts
import { Observable, filter } from "rxjs";

function notNull<T>() {
  return (source: Observable<T | null | undefined>) =>
    source.pipe(filter((v): v is T => v != null));
}
```

## 133: What are some common naming conventions in RxJS code?

Observables end with `$` (`user$`). Subjects are often private, with a public read-only Observable exposed through `asObservable()`. Streams of user actions are often named after the action, like `save$` or `refresh$`. Streams of state are named after the data, like `items$` or `loading$`.

## 134: What does asObservable do on a Subject?

`asObservable()` returns an Observable that only lets you subscribe. It hides `next`, `error` and `complete`, so other code cannot push values into your Subject. It is the usual way to expose a Subject from a service.

```ts
private readonly itemsSubject = new BehaviorSubject<Item[]>([]);
readonly items$ = this.itemsSubject.asObservable();
```

## 135: How do you create an Observable from a callback-based API?

For Node-style callbacks (`(err, result)`), use `bindNodeCallback`. For plain callbacks, use `bindCallback`. For anything else, write `new Observable` and call `subscriber.next` from the callback.

```ts
import { bindNodeCallback } from "rxjs";
import { readFile } from "fs";

const readFile$ = bindNodeCallback(readFile);
readFile$("./data.txt", "utf8").subscribe((text) => console.log(text));
```

## 136: How do you make an HTTP request with RxJS outside Angular?

Use `fromFetch` from `rxjs/fetch`, which wraps the Fetch API and aborts the request on unsubscribe, or `ajax` from `rxjs/ajax`, which uses XMLHttpRequest.

```ts
import { fromFetch } from "rxjs/fetch";
import { switchMap } from "rxjs";

fromFetch("/api/users")
  .pipe(switchMap((res) => res.json()))
  .subscribe((users) => console.log(users));
```

## 137: What is the ajax function?

`ajax` from `rxjs/ajax` makes HTTP requests using XMLHttpRequest. It returns a cold Observable with an `AjaxResponse`, and has shortcuts like `ajax.getJSON(url)`. It also reports upload and download progress if you ask for it, and unsubscribing aborts the request.

```ts
import { ajax } from "rxjs/ajax";

ajax.getJSON<User[]>("/api/users").subscribe((users) => console.log(users));
```

## 138: What is the webSocket function?

`webSocket` from `rxjs/webSocket` creates a `WebSocketSubject`. You subscribe to it to receive messages and call `next` on it to send them. By default messages are parsed and sent as JSON. The socket opens on the first subscription and closes when everyone unsubscribes.

```ts
import { webSocket } from "rxjs/webSocket";

const socket = webSocket("wss://example.com/live");
socket.subscribe((msg) => console.log(msg));
socket.next({ type: "subscribe", channel: "prices" });
```

## 139: What does animationFrames do?

`animationFrames()` emits once per browser animation frame, with the timestamp and the elapsed time since you subscribed. It is a clean way to drive animations with RxJS.

```ts
import { animationFrames, takeWhile, map } from "rxjs";

animationFrames()
  .pipe(
    map(({ elapsed }) => elapsed / 1000),
    takeWhile((t) => t < 2),
  )
  .subscribe((t) => (box.style.left = `${t * 100}px`));
```

## 140: What does EmptyError mean?

`EmptyError` is thrown when an operator needed at least one value but the source completed with none. You see it from `first`, `last`, `single`, `firstValueFrom`, `lastValueFrom` and `throwIfEmpty`. The fix is either to add a default value or to make sure the source emits.

## 141: What is the difference between a Subject and a plain event emitter?

Both let you push events to many listeners. A Subject is also an Observable, so you can use all RxJS operators on it, combine it with other streams and cancel listening with `unsubscribe()`. A Subject also has the `error` and `complete` notifications, which an event emitter doesn't have.

## 142: What happens when you call next on a completed Subject?

Nothing. Once a Subject has completed or errored, calls to `next` are ignored. New subscribers get the `complete` (or `error`) notification right away. A `ReplaySubject` still replays its buffer to new subscribers before telling them it completed.

## 143: What does mergeWith do?

`mergeWith` is the pipeable version of `merge`. It merges the source with one or more other Observables.

```ts
import { mergeWith } from "rxjs";

clicks$.pipe(mergeWith(keys$, touches$)).subscribe(() => resetIdleTimer());
```

There are matching operators for the others: `concatWith`, `combineLatestWith`, `zipWith` and `raceWith`.

## 144: What does map with an index do?

The function you pass to `map`, `filter`, `tap` and many other operators also gets the index of the value as the second argument. The index counts from 0 for each subscription.

```ts
of("a", "b")
  .pipe(map((v, i) => `${i}: ${v}`))
  .subscribe(console.log); // 0: a, 1: b
```

## 145: How do you debug an RxJS pipeline?

The simplest way is to add `tap` with logging between operators, including the `error` and `complete` callbacks, so you see where values change or stop. Giving each tap a label helps when there are several.

```ts
source$.pipe(
  tap({
    next: (v) => console.log("[raw]", v),
    complete: () => console.log("[raw] done"),
  }),
  map(transform),
  tap((v) => console.log("[mapped]", v)),
);
```

## 146: Can you reuse an Observable after it completes?

Yes, for a cold Observable. Each subscription starts a new run, so subscribing again after completion runs it again. This is exactly what `retry` and `repeat` do. A completed Subject, though, cannot be restarted; you need a new Subject.

## 147: What are Observables good for in a UI?

They fit anything that changes over time: input events, route changes, live data from a server, timers, and state that many components read. You can describe "debounce the input, cancel the old request, show the latest result" as one short pipeline instead of scattered handlers and flags.

## 148: Is RxJS only for Angular?

No. RxJS is a plain JavaScript library. Angular depends on it and uses it in HttpClient, the router and forms, which is why many people meet it there. It is also used in Node.js services, NestJS microservices, Redux-Observable for React, and in editors and other tools that deal with many event streams.

## 149: What does subscribe return if the Observable is synchronous?

It still returns a Subscription. If the source already completed during the `subscribe` call, that Subscription is already closed, and calling `unsubscribe()` on it does nothing.

## 150: What is the scheduler in RxJS in simple words?

A scheduler controls when a piece of work runs: right now, as a microtask, on a timer, or on the next animation frame. Most operators pick a sensible scheduler on their own, so you rarely set one. Time-based operators like `delay` and `debounceTime` use `asyncScheduler`, and tests can swap in virtual time.

# Moderate Questions (151-300)

## 151: How do you build a search-as-you-type feature with RxJS?

Take the input events, map to the text, wait for a pause with `debounceTime`, skip repeats with `distinctUntilChanged`, and use `switchMap` so a new term cancels the old request. Catch errors inside the `switchMap` so one failed request doesn't end the whole stream.

```ts
import {
  fromEvent,
  map,
  debounceTime,
  distinctUntilChanged,
  filter,
  switchMap,
  catchError,
  of,
} from "rxjs";

const results$ = fromEvent<InputEvent>(searchInput, "input").pipe(
  map((e) => (e.target as HTMLInputElement).value.trim()),
  debounceTime(300),
  distinctUntilChanged(),
  filter((term) => term.length >= 2),
  switchMap((term) =>
    http
      .get<Result[]>(`/api/search?q=${encodeURIComponent(term)}`)
      .pipe(catchError(() => of([]))),
  ),
);
```

## 152: What goes wrong if you use mergeMap instead of switchMap for search?

All requests run and none are cancelled, so responses can come back out of order. If the user types "ca" and then "cat", and the "ca" response is slower, the screen ends up showing results for "ca" even though the box says "cat". `switchMap` drops the old request, so only the latest term can update the results.

## 153: Why should catchError usually go inside switchMap instead of at the end?

When an error reaches `catchError`, the source before it is already finished. If `catchError` is at the end of the outer chain, the first failed request ends the whole stream, and the input stops working. Putting `catchError` on the inner Observable inside `switchMap` handles the error for that one request, and the outer stream keeps listening.

```ts
// Bad: one error kills the search box
term$.pipe(
  switchMap((t) => search(t)),
  catchError(() => of([])),
);

// Good: each request handles its own error
term$.pipe(switchMap((t) => search(t).pipe(catchError(() => of([])))));
```

## 154: How do you configure retry with a delay?

Pass a config object. `count` is the max number of retries, `delay` is either milliseconds or a function that returns an Observable (the retry happens when it emits), and `resetOnSuccess` resets the counter after a successful value.

```ts
import { retry, timer } from "rxjs";

http.get("/api/data").pipe(
  retry({
    count: 3,
    delay: (error, retryCount) => timer(retryCount * 1000),
  }),
);
```

## 155: How do you add exponential backoff to retries?

Use the `delay` function of `retry` and grow the wait with each attempt. Adding a little random jitter stops many clients from retrying at the same moment.

```ts
import { retry, timer } from "rxjs";

function backoff(maxRetries = 5, baseMs = 500) {
  return retry({
    count: maxRetries,
    delay: (_err, attempt) =>
      timer(baseMs * 2 ** (attempt - 1) + Math.random() * 100),
  });
}

http.get("/api/data").pipe(backoff()).subscribe();
```

## 156: How do you retry only for certain errors?

In the `delay` function of `retry`, return `throwError` for errors that should not be retried. That error ends the retrying and goes to the subscriber.

```ts
import { retry, timer, throwError } from "rxjs";
import { HttpErrorResponse } from "@angular/common/http";

http.get("/api/data").pipe(
  retry({
    count: 3,
    delay: (err: HttpErrorResponse) =>
      err.status >= 500 || err.status === 0
        ? timer(1000)
        : throwError(() => err),
  }),
);
```

## 157: Why are retryWhen and repeatWhen deprecated?

Their logic was hard to follow: you received a stream of errors (or completions) and had to build a notifier from it, and getting the limits right was easy to break. In RxJS 7 the config objects on `retry` and `repeat` cover the same cases (count, delay, reset on success) with plain functions. `retryWhen` and `repeatWhen` still exist but are deprecated and planned for removal.

## 158: How do you poll an endpoint until a condition is met?

Use `timer` with `switchMap` (or `repeat` with a delay) to call the endpoint again and again, then stop with `takeWhile`. Pass `true` as the second argument to also emit the final value.

```ts
import { timer, switchMap, takeWhile } from "rxjs";

const job$ = timer(0, 2000).pipe(
  switchMap(() => http.get<Job>(`/api/jobs/${id}`)),
  takeWhile((job) => job.status !== "done", true),
);
```

## 159: What is the difference between polling with interval plus switchMap and with repeat?

With `timer(0, 2000).pipe(switchMap(...))`, a new request starts every 2 seconds no matter how long the previous one took, and a slow request gets cancelled by the next tick. With `request$.pipe(repeat({ delay: 2000 }))`, the next request starts 2 seconds after the previous one finished, so requests never overlap. The `repeat` version is usually kinder to the server.

## 160: What options does the share operator have?

`share` takes a config object:

- `connector`: a factory for the Subject used to multicast. Default is `() => new Subject()`. Pass `() => new ReplaySubject(1)` to replay.
- `resetOnError`: reset the inner Subject and source connection after an error. Default `true`.
- `resetOnComplete`: reset after the source completes. Default `true`.
- `resetOnRefCountZero`: reset when the number of subscribers drops to zero. Default `true`.

Each reset option can also be a function that returns an Observable, and the reset happens when it emits, which lets you delay the reset.

```ts
import { share, ReplaySubject, timer } from "rxjs";

const prices$ = source$.pipe(
  share({
    connector: () => new ReplaySubject(1),
    resetOnRefCountZero: () => timer(5000),
  }),
);
```

## 161: What does refCount mean in shareReplay?

With `shareReplay({ bufferSize: 1, refCount: true })`, the source subscription is closed when the subscriber count drops to zero, and the next subscriber starts it fresh. With `refCount: false` (the default, and what you get from `shareReplay(1)`), the source stays subscribed even after everyone leaves. For a one-off HTTP call that completes, either is fine. For a never-ending source like a WebSocket or `interval`, `refCount: false` keeps it running forever, which is a leak.

## 162: How do you cache an HTTP response and refresh it on demand?

Keep a refresh trigger, and build the cached stream from it with `switchMap` and `shareReplay`. Every subscriber gets the cached value, and calling `refresh()` fetches again.

```ts
import { BehaviorSubject, switchMap, shareReplay } from "rxjs";

@Injectable({ providedIn: "root" })
export class ProductsService {
  private http = inject(HttpClient);
  private refresh$ = new BehaviorSubject<void>(undefined);

  readonly products$ = this.refresh$.pipe(
    switchMap(() => this.http.get<Product[]>("/api/products")),
    shareReplay({ bufferSize: 1, refCount: true }),
  );

  refresh() {
    this.refresh$.next();
  }
}
```

## 163: How do you cache a value only for a limited time?

`shareReplay` takes a `windowTime` in milliseconds. Values older than that are not replayed. Keep in mind that the source isn't re-run just because the window passed; with `refCount: true` the next subscriber after everyone has left starts a new run.

```ts
config$ = http
  .get("/api/config")
  .pipe(shareReplay({ bufferSize: 1, windowTime: 60_000, refCount: true }));
```

## 164: What is connectable?

`connectable(source, config)` creates an Observable that does not subscribe to the source when someone subscribes to it. Instead, the source starts when you call `connect()`, and all subscribers share it. It replaces the deprecated `multicast` and `publish` operators.

```ts
import { connectable, interval, take, Subject } from "rxjs";

const shared = connectable(interval(1000).pipe(take(3)), {
  connector: () => new Subject<number>(),
});
shared.subscribe((v) => console.log("A", v));
shared.subscribe((v) => console.log("B", v));
const connection = shared.connect(); // start now
```

## 165: What does the connect operator do?

`connect` shares the source inside a function you provide, so you can split it into several branches without subscribing to the source more than once. It's useful when you need to run the same source through different operators and merge the results.

```ts
import { connect, merge, filter, map } from "rxjs";

source$.pipe(
  connect((shared$) =>
    merge(
      shared$.pipe(
        filter((n) => n % 2 === 0),
        map((n) => `even ${n}`),
      ),
      shared$.pipe(
        filter((n) => n % 2 !== 0),
        map((n) => `odd ${n}`),
      ),
    ),
  ),
);
```

## 166: What replaces multicast, publish, publishReplay and refCount in RxJS 7?

They are all deprecated. Use `share` for "share while there are subscribers" (it already includes ref counting), `shareReplay` for "share and replay", `connectable` when you want to choose the moment the source starts, and the `connect` operator for sharing inside a pipeline.

## 167: How do you build a simple state store with BehaviorSubject?

Keep the state in a private `BehaviorSubject`, expose it as an Observable, select slices with `map` and `distinctUntilChanged`, and update it through methods that build a new state object.

```ts
import { BehaviorSubject, map, distinctUntilChanged } from "rxjs";

interface TodoState {
  todos: Todo[];
  filter: "all" | "done";
}

export class TodoStore {
  private state = new BehaviorSubject<TodoState>({ todos: [], filter: "all" });

  readonly todos$ = this.state.pipe(
    map((s) => s.todos),
    distinctUntilChanged(),
  );

  add(todo: Todo) {
    const s = this.state.value;
    this.state.next({ ...s, todos: [...s.todos, todo] });
  }
}
```

## 168: Why is it a bad idea to call getValue on a BehaviorSubject everywhere?

Reading `.value` gives you a snapshot, and code that reads snapshots won't update when the value changes later. It pulls you back to imperative code and leads to bugs where the UI shows stale data. It is fine inside the store itself (for example to build the next state), but consumers should subscribe or use the `async` pipe or a signal.

## 169: When do you use a Subject and when a BehaviorSubject?

Use a plain `Subject` for events, where there is no "current value", like "save clicked" or "message received". Late subscribers should not get an old click. Use a `BehaviorSubject` for state, where there is always a current value and every new subscriber needs it right away, like the logged-in user or the current filter.

## 170: What happens if a function inside map throws an error?

RxJS catches it and sends it down the chain as an `error` notification, the same as if the source had errored. The subscription then ends. So you can handle it with `catchError` like any other error.

```ts
of('{"a":1}', "not json")
  .pipe(
    map((s) => JSON.parse(s)),
    catchError((err) => of({ parseError: err.message })),
  )
  .subscribe(console.log);
```

## 171: How do you keep a stream running after an error?

An Observable that errored is done, so you can't continue it. You can either catch the error closer to where it happens (inside a `switchMap`, `mergeMap` or `concatMap`, so only the inner stream ends), or use `retry` to subscribe to the source again. Which one you need depends on whether the failing part is one request or the whole source.

## 172: How do you rethrow a different error from catchError?

Return `throwError` with your new error, or simply `throw` inside the `catchError` callback. Both send an error notification downstream.

```ts
import { catchError, throwError } from "rxjs";

http
  .get("/api/user")
  .pipe(
    catchError((err) =>
      throwError(
        () => new UserLoadError("Could not load user", { cause: err }),
      ),
    ),
  );
```

## 173: What is the second argument of the catchError callback?

It is `caught`, the source Observable itself. Returning it makes `catchError` resubscribe to the source, like an endless retry. That is rarely what you want, because a source that always fails loops forever; use `retry` with a count instead.

## 174: In what order do finalize callbacks run?

They run when the subscription is torn down, after the `complete` or `error` notification has reached the subscriber. Since RxJS 7, `finalize` unsubscribes from its source before calling its callback, so several `finalize` operators in one chain run in the order they are written: the one closest to the source first. In RxJS 6 the order was reversed, which you may still see mentioned in old answers.

```ts
of(1)
  .pipe(
    finalize(() => console.log("first")),
    finalize(() => console.log("second")),
  )
  .subscribe(); // first, second
```

## 175: What are the extra callbacks of tap in RxJS 7?

Besides `next`, `error` and `complete`, the observer you pass to `tap` can have `subscribe` (when the subscription starts), `unsubscribe` (when the consumer unsubscribes before the source finished) and `finalize` (when it ends for any reason). They are handy for logging the life of a subscription.

```ts
source$.pipe(
  tap({
    subscribe: () => console.log("subscribed"),
    unsubscribe: () => console.log("unsubscribed early"),
    finalize: () => console.log("finished"),
  }),
);
```

## 176: What options does the timeout config object have?

- `each`: max time between values (and before the first one if `first` is not set).
- `first`: max time, or a `Date`, before the first value.
- `with`: a function that returns a fallback Observable to switch to instead of erroring.
- `meta`: any data you want attached to the `TimeoutError`.
- `scheduler`: the scheduler for the timers.

The `TimeoutError` has an `info` property with `meta`, `seen` (how many values arrived) and `lastValue`.

## 177: Where should takeUntil go in a pipe?

Usually last, or at least after any operator that starts its own inner subscriptions, like `switchMap`, `mergeMap`, `shareReplay` or `combineLatest`. If `takeUntil` comes before them, the notifier only stops the source part, and the inner subscriptions created later in the chain keep running. Lint rules like `no-unsafe-takeuntil` exist to catch this.

```ts
// Leaks the inner interval:
clicks$.pipe(
  takeUntil(destroy$),
  switchMap(() => interval(1000)),
);

// Correct:
clicks$.pipe(
  switchMap(() => interval(1000)),
  takeUntil(destroy$),
);
```

## 178: What is the destroy$ Subject pattern and what replaces it in Angular?

Before Angular 16, components often had a `private destroy$ = new Subject<void>()`, used `takeUntil(this.destroy$)` in every pipe, and called `this.destroy$.next()` and `complete()` in `ngOnDestroy`. Now `takeUntilDestroyed()` does the same with no boilerplate. You will still see the old pattern in existing projects.

## 179: How do you use takeUntilDestroyed outside the constructor?

Outside an injection context there is no way for it to find the current component, so you must pass a `DestroyRef` that you injected earlier.

```ts
export class UserPage implements OnInit {
  private destroyRef = inject(DestroyRef);

  ngOnInit() {
    this.route.paramMap
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe((params) => this.load(params.get("id")));
  }
}
```

## 180: What is toObservable in Angular?

`toObservable(signal)` from `@angular/core/rxjs-interop` turns a signal into an Observable. It uses an effect under the hood, so it needs an injection context (or an `injector` option), and it emits the latest value after the effect runs, not synchronously on every `set`. If a signal changes several times before the effect runs, only the last value is emitted.

```ts
query = signal("");
results$ = toObservable(this.query).pipe(
  debounceTime(300),
  switchMap((q) => this.api.search(q)),
);
```

## 181: What options does toSignal accept?

The main ones are `initialValue` (the value before the first emission), `requireSync: true` (when you know the Observable emits synchronously on subscribe, like a `BehaviorSubject`; then the type has no `undefined`), `manualCleanup` (don't unsubscribe on destroy), `injector` (to call it outside an injection context) and `equal` (a custom equality check). If the Observable errors, reading the signal throws that error.

## 182: How do you combine Angular route params with an HTTP call?

Read the param from `ActivatedRoute.paramMap`, then `switchMap` to the request. When the user moves from `/users/1` to `/users/2`, Angular reuses the component, the param stream emits again, and the old request gets cancelled.

```ts
private route = inject(ActivatedRoute);
private http = inject(HttpClient);

user$ = this.route.paramMap.pipe(
  map((params) => params.get('id')!),
  switchMap((id) => this.http.get<User>(`/api/users/${id}`)),
);
```

## 183: How do you react to reactive form changes with RxJS?

Every `FormControl` and `FormGroup` has a `valueChanges` Observable. Pipe it like any other stream, for example to debounce and save. Use `startWith(control.value)` if you also need the current value at the start, because `valueChanges` only emits on changes.

```ts
this.form.valueChanges
  .pipe(
    debounceTime(500),
    distinctUntilChanged((a, b) => JSON.stringify(a) === JSON.stringify(b)),
    switchMap((value) => this.api.saveDraft(value)),
    takeUntilDestroyed(this.destroyRef),
  )
  .subscribe();
```

## 184: How do you model loading, error and data in one stream?

Map the result to a state object, start with a loading state, and turn errors into an error state inside the same inner stream.

```ts
type State<T> =
  | { status: "loading" }
  | { status: "ok"; data: T }
  | { status: "error"; error: unknown };

const state$ = id$.pipe(
  switchMap((id) =>
    http.get<User>(`/api/users/${id}`).pipe(
      map((data): State<User> => ({ status: "ok", data })),
      startWith<State<User>>({ status: "loading" }),
      catchError((error) => of<State<User>>({ status: "error", error })),
    ),
  ),
);
```

## 185: How do you pause and resume a stream?

Use a `BehaviorSubject<boolean>` for the paused flag and `switchMap` to either the source or `EMPTY`. When paused, the source is unsubscribed; when resumed, it starts again.

```ts
import { BehaviorSubject, switchMap, interval, EMPTY } from "rxjs";

const paused$ = new BehaviorSubject(false);
const ticks$ = paused$.pipe(
  switchMap((paused) => (paused ? EMPTY : interval(1000))),
);
```

If you need to keep the count where it stopped, keep the counter in `scan` after the `switchMap`, not in the `interval` value.

## 186: How do you build a countdown timer?

Use `timer(0, 1000)`, turn the tick into the remaining seconds, and stop with `take`.

```ts
import { timer, map, take } from "rxjs";

const countdown$ = (seconds: number) =>
  timer(0, 1000).pipe(
    map((tick) => seconds - tick),
    take(seconds + 1),
  );

countdown$(10).subscribe((s) => console.log(s)); // 10 ... 0
```

## 187: How do you implement drag and drop with RxJS?

Start on `mousedown` (or `pointerdown`), then `switchMap` to `mousemove` events until `mouseup`. Each drag is a separate inner stream that ends when the button is released.

```ts
import { fromEvent, switchMap, map, takeUntil } from "rxjs";

const down$ = fromEvent<PointerEvent>(box, "pointerdown");
const move$ = fromEvent<PointerEvent>(document, "pointermove");
const up$ = fromEvent<PointerEvent>(document, "pointerup");

down$
  .pipe(
    switchMap((start) => {
      const offsetX = start.clientX - box.offsetLeft;
      const offsetY = start.clientY - box.offsetTop;
      return move$.pipe(
        map((e) => ({ x: e.clientX - offsetX, y: e.clientY - offsetY })),
        takeUntil(up$),
      );
    }),
  )
  .subscribe(({ x, y }) => {
    box.style.left = `${x}px`;
    box.style.top = `${y}px`;
  });
```

## 188: How do you load more items on infinite scroll?

Listen to scroll events, check when the user is near the bottom, and use `exhaustMap` so you don't start a second page request while one is still loading. Keep the page number and the list in `scan`.

```ts
const nearBottom$ = fromEvent(window, "scroll").pipe(
  throttleTime(200),
  filter(
    () =>
      window.innerHeight + window.scrollY > document.body.offsetHeight - 300,
  ),
);

const items$ = nearBottom$.pipe(
  startWith(null),
  exhaustMap((_, index) => api.getPage(index + 1)),
  scan((all, page) => [...all, ...page], [] as Item[]),
);
```

## 189: How do you auto-save a form without losing edits?

Debounce the changes, then use `concatMap` so saves run in order and none are dropped. If you only care about the latest version, `switchMap` is fine for reads, but for writes cancelling a request on the client doesn't stop the server, so ordering with `concatMap` is safer.

```ts
form.valueChanges
  .pipe(
    debounceTime(1000),
    concatMap((value) => api.save(value)),
  )
  .subscribe();
```

## 190: What does groupBy do?

`groupBy` splits a stream into several inner streams, one per key. It emits a `GroupedObservable` for each new key, with the key in its `key` property. You usually flatten it with `mergeMap`.

```ts
import { from, groupBy, mergeMap, toArray } from "rxjs";

from(people)
  .pipe(
    groupBy((p) => p.city),
    mergeMap((group$) =>
      group$.pipe(
        toArray(),
        map((list) => ({ city: group$.key, list })),
      ),
    ),
  )
  .subscribe(console.log);
```

## 191: How do you stop groupBy from keeping groups forever?

By default each group stays open until the source completes, so a long-running source with many keys keeps growing in memory. Pass a `duration` function in the config; when the Observable it returns emits, that group completes and is removed. A later value with the same key opens a new group.

```ts
events$.pipe(
  groupBy((e) => e.userId, {
    duration: (group$) => group$.pipe(debounceTime(30_000)),
  }),
);
```

## 192: What does window do and how is it different from buffer?

`window` and its variants (`windowTime`, `windowCount`, `windowToggle`, `windowWhen`) work like the `buffer` operators, but they emit Observables instead of arrays. Each window is a stream you can process as values arrive, instead of waiting for the whole batch. Use buffer when you need the whole batch at once, and window when you want to process each group as a stream.

## 193: What do bufferToggle and bufferWhen do?

`bufferToggle(openings$, closingSelector)` starts a new buffer each time `openings$` emits and closes it when the Observable from `closingSelector` emits. `bufferWhen(closingSelector)` keeps one buffer open at a time and closes it when the returned Observable emits, then starts a new one right away. They let you collect values over custom periods, like "while the mouse button is held".

## 194: What does expand do?

`expand` calls your function on every value, including the values it produces itself, and merges the results. It keeps going until your function returns `EMPTY`. It is a good fit for following paginated APIs where each response tells you the next page.

```ts
import { expand, EMPTY, map, reduce } from "rxjs";

const allItems$ = api.getPage(1).pipe(
  expand((page) => (page.next ? api.getPage(page.next) : EMPTY)),
  map((page) => page.items),
  reduce((all, items) => [...all, ...items], [] as Item[]),
);
```

## 195: What are mergeScan and switchScan?

They are like `scan`, but the accumulator returns an Observable instead of a plain value. `mergeScan` subscribes to each returned Observable and merges results (with an optional concurrency limit). `switchScan` cancels the previous one when a new source value comes in. They help when each step of a running state needs an async call.

## 196: What is the difference between debounce and debounceTime?

`debounceTime(ms)` uses a fixed wait. `debounce(fn)` calls `fn` with each value and waits until the Observable it returns emits. That lets the wait depend on the value, for example a shorter wait when the input is empty.

```ts
import { debounce, timer } from "rxjs";

term$.pipe(debounce((term) => timer(term.length === 0 ? 0 : 300)));
```

`throttle`, `audit` and `sample` are the same idea for `throttleTime`, `auditTime` and `sampleTime`.

## 197: How do the leading and trailing options of throttleTime work?

`throttleTime(ms, scheduler, { leading, trailing })` decides which values in each window get through. The default `{ leading: true, trailing: false }` emits the first value and drops the rest. `{ leading: false, trailing: true }` emits the last value at the end of the window. Both `true` emits the first one right away and the last one at the end, which is good for things like a resize handler where you want the final size too.

```ts
import { throttleTime, asyncScheduler } from "rxjs";

resize$.pipe(
  throttleTime(200, asyncScheduler, { leading: true, trailing: true }),
);
```

## 198: When do you use zip, combineLatest, forkJoin and withLatestFrom?

- `forkJoin`: several one-shot requests, you want all final results once.
- `combineLatest`: several values that change over time, and the result should update when any changes (filters plus data).
- `withLatestFrom`: one stream is the trigger and the others only give context (button click plus form value).
- `zip`: values belong together by position (request N with response N). It is the least common one.

## 199: Why does combineLatest emit values you don't want, and how do you fix it?

If two inputs come from the same source, a single change can make `combineLatest` emit twice: once with the new first value and the old second one, then again with both new. This is a "glitch". You can fix it by deriving both values in one `map` instead of two streams, by adding `debounceTime(0)` or `auditTime(0)` after `combineLatest` to merge emissions in the same tick, or by filtering out unchanged results with `distinctUntilChanged`.

## 200: What do materialize and dematerialize do?

`materialize` turns every notification (`next`, `error`, `complete`) into a plain value of type `ObservableNotification`, like `{ kind: 'N', value }` or `{ kind: 'E', error }`. The stream then completes normally even if the source errored. `dematerialize` does the opposite. They are useful for logging, testing, or passing errors through code that should not stop on them.

## 201: What does onErrorResumeNextWith do?

`onErrorResumeNextWith(...sources)` moves on to the next Observable when the current one errors or completes, ignoring the error. It is like `concat` that also swallows errors. Use it carefully, because errors disappear without a trace. The older `onErrorResumeNext` operator form is deprecated in favor of this one; the creation function `onErrorResumeNext` still exists.

## 202: What does using do?

`using(resourceFactory, observableFactory)` creates a resource when someone subscribes, gives it to the factory that builds the Observable, and calls the resource's `unsubscribe()` when the subscription ends. It ties the life of something like a connection to the life of the subscription.

```ts
import { using } from "rxjs";

const data$ = using(
  () => {
    const conn = openConnection();
    return { conn, unsubscribe: () => conn.close() };
  },
  (resource) =>
    fromEventPattern(
      (h) => resource!.conn.on("data", h),
      (h) => resource!.conn.off("data", h),
    ),
);
```

The resource only needs an `unsubscribe()` method, and the second factory receives it.

In practice, writing `new Observable` with a teardown function is often clearer than `using`.

## 203: What does the scheduled function do?

`scheduled(input, scheduler)` is like `from`, but it delivers values using the scheduler you pass. In RxJS 6 you could pass a scheduler as the last argument to `of` and `from`; that is deprecated in RxJS 7, and `scheduled` is the replacement.

```ts
import { scheduled, asapScheduler } from "rxjs";

scheduled([1, 2, 3], asapScheduler).subscribe(console.log); // emits as microtasks
```

## 204: What do observeOn and subscribeOn do?

`observeOn(scheduler)` delivers each notification from the source to later operators using that scheduler, so it moves the "emission" side to another time. `subscribeOn(scheduler)` delays the act of subscribing to the source itself. `observeOn(animationFrameScheduler)` is a typical use: process values on the next frame. Both are rarely needed in app code.

## 205: What are the main schedulers in RxJS?

- `asyncScheduler`: uses `setTimeout`/`setInterval`. The default for time-based operators.
- `asapScheduler`: runs as a microtask, like a resolved Promise, before the next macrotask.
- `queueScheduler`: runs right away, but queues recursive work so it does not grow the stack.
- `animationFrameScheduler`: runs on `requestAnimationFrame`, good for animations.

## 206: What is the difference between asyncScheduler and asapScheduler?

`asyncScheduler` schedules work as a macrotask with `setTimeout`, so it runs after the browser has a chance to handle other events and render. `asapScheduler` schedules it as a microtask, so it runs as soon as the current synchronous code finishes, before any timers and before rendering. Code that needs to run "right after this but before anything else" uses `asap`.

## 207: How do you test RxJS code with the TestScheduler?

Create a `TestScheduler` with an assertion function, then write your test inside `run()`. Inside, time is virtual, so `delay(1000)` or `debounceTime(300)` finish instantly. You describe inputs and the expected output with marble strings.

```ts
import { TestScheduler } from "rxjs/testing";
import { map } from "rxjs";

const testScheduler = new TestScheduler((actual, expected) => {
  expect(actual).toEqual(expected);
});

it("doubles values", () => {
  testScheduler.run(({ cold, expectObservable }) => {
    const source$ = cold("-a-b-|", { a: 1, b: 2 });
    expectObservable(source$.pipe(map((n) => n * 2))).toBe("-x-y-|", {
      x: 2,
      y: 4,
    });
  });
});
```

## 208: What do the characters in a marble string mean?

- `-`: one frame of time passing (1ms inside `run()`).
- A letter or number: a value emitted in that frame. Map letters to real values with the values object.
- `|`: completion.
- `#`: error. Pass the error as the third argument.
- `()`: values emitted in the same frame, like `(ab|)`.
- `^`: the subscription point, only in `hot()` Observables.
- `!`: the unsubscription point, in subscription marbles.
- A space is ignored, so you can line things up.
- `10ms`, `1.5s`, `2m`: time progression, a quick way to skip that much time.

## 209: What is the difference between cold and hot in marble tests?

`cold('--a--b|')` starts its timeline when the code under test subscribes, like a normal cold Observable. `hot('--a-^-b|')` has its own timeline that already runs; `^` marks the moment the test subscribes, and values before `^` are missed. Use `hot` for things like Subjects and DOM events, and `cold` for things like HTTP calls returned from a mock.

## 210: How do you test debounceTime with marbles?

Inside `run()`, time-based operators use virtual time, so you can write the timing with time progression syntax.

```ts
testScheduler.run(({ cold, expectObservable }) => {
  const input$ = cold("a 100ms b 299ms |");
  const expected = "  101ms - 299ms (b|)";
  expectObservable(input$.pipe(debounceTime(300))).toBe(expected);
});
```

Here `a` is dropped because `b` comes within 300ms. `b` would be emitted 300ms after it arrived, but the source completes first, so `debounceTime` emits `b` right away on completion, together with `|`.

## 211: What is expectSubscriptions used for?

It checks when a test Observable was subscribed and unsubscribed. It is how you test that an operator cancels things, for example that `switchMap` unsubscribed from the previous inner Observable.

```ts
testScheduler.run(({ cold, hot, expectObservable, expectSubscriptions }) => {
  const inner = cold("  --x--x|");
  const outer = hot("   -a--b------|");
  const innerSubs = ["  -^--!", "    ----^-----!"];

  expectObservable(outer.pipe(switchMap(() => inner))).toBe("---x--x--x-|");
  expectSubscriptions(inner.subscriptions).toBe(innerSubs);
});
```

## 212: How do you test Observable code without marbles?

For simple cases, subscribe and collect the values into an array, or turn the Observable into a Promise with `firstValueFrom` or `lastValueFrom` and `await` it. For timers you can use the fake timers of your test runner (Jest, Vitest) or Angular's `fakeAsync` and `tick`. Marbles are best for timing-heavy logic; plain collection is easier for most other code.

```ts
it("returns active users", async () => {
  const users = await firstValueFrom(service.activeUsers$);
  expect(users).toHaveLength(2);
});
```

## 213: How do you write a custom operator from scratch?

Return a function that takes the source and returns `new Observable`. Inside, subscribe to the source, forward or change notifications, and return the inner subscription so unsubscribing cleans it up.

```ts
import { Observable, OperatorFunction } from "rxjs";

function mapEvery<T, R>(
  n: number,
  fn: (v: T) => R,
): OperatorFunction<T, T | R> {
  return (source) =>
    new Observable<T | R>((subscriber) => {
      let i = 0;
      return source.subscribe({
        next: (v) => subscriber.next(++i % n === 0 ? fn(v) : v),
        error: (err) => subscriber.error(err),
        complete: () => subscriber.complete(),
      });
    });
}
```

Prefer building on existing operators when you can, since they already handle edge cases.

## 214: What are OperatorFunction and MonoTypeOperatorFunction?

They are the types for operators. `OperatorFunction<T, R>` is a function from `Observable<T>` to `Observable<R>`. `MonoTypeOperatorFunction<T>` is the case where input and output types are the same, like `filter` or `tap`. Use them as return types of your custom operators so TypeScript can check them inside `pipe`.

```ts
import { MonoTypeOperatorFunction, tap } from "rxjs";

function log<T>(label: string): MonoTypeOperatorFunction<T> {
  return tap((v) => console.log(label, v));
}
```

## 215: How do you narrow types with filter?

Pass a type guard as the predicate. Then the output type is narrowed, and later operators see the narrower type.

```ts
const user$: Observable<User | null> = getUser();

user$.pipe(
  filter((u): u is User => u !== null),
  map((u) => u.name), // u is User here
);
```

## 216: How do you type a Subject that emits no data?

Use `Subject<void>` and call `next()` with no arguments. It fits signals like "refresh" or "destroyed" where only the timing matters.

```ts
const refresh$ = new Subject<void>();
refresh$.next();
```

## 217: How do you get partial results from forkJoin when some calls fail?

Catch the error on each inner Observable and turn it into a value, so `forkJoin` always gets something.

```ts
const safe = <T>(obs$: Observable<T>) =>
  obs$.pipe(
    map((data) => ({ ok: true as const, data })),
    catchError((error) => of({ ok: false as const, error })),
  );

forkJoin([safe(api.a()), safe(api.b()), safe(api.c())]).subscribe((results) => {
  results.filter((r) => r.ok).forEach((r) => console.log(r));
});
```

## 218: How do you run many requests with a limit on concurrency?

Use `mergeMap` with its second argument, which caps how many inner Observables run at the same time. The rest wait in a queue.

```ts
import { from, mergeMap, toArray } from "rxjs";

from(fileIds)
  .pipe(
    mergeMap((id) => api.upload(id), 4),
    toArray(),
  )
  .subscribe(() => console.log("all uploaded"));
```

## 219: How do you run requests one after another where each needs the previous result?

Chain them with `switchMap` or `concatMap`. Each step gets the result of the step before.

```ts
api.getUser(id).pipe(
  switchMap((user) => api.getTeam(user.teamId)),
  switchMap((team) => api.getProjects(team.id)),
);
```

If you need earlier values at the end too, map to an object as you go, for example `switchMap(user => api.getTeam(user.teamId).pipe(map(team => ({ user, team }))))`.

## 220: How does fromFetch cancel requests?

`fromFetch` creates an `AbortController` for each subscription and passes its signal to `fetch`. If you unsubscribe before the response is done, it calls `abort()`, so the request is really cancelled. If you pass your own `signal` in the init object, it is linked too. You can also pass a `selector` to read the body inside the same cancellable work.

```ts
import { fromFetch } from "rxjs/fetch";

const user$ = fromFetch("/api/user", { selector: (res) => res.json() });
```

## 221: How do you turn a Node.js EventEmitter into an Observable?

`fromEvent` works with Node's `EventEmitter` too. It uses `addListener` and `removeListener`. For events with several arguments, the values are emitted as an array.

```ts
import { fromEvent, takeUntil } from "rxjs";

const data$ = fromEvent<Buffer>(socket, "data");
const end$ = fromEvent(socket, "end");

data$.pipe(takeUntil(end$)).subscribe((chunk) => console.log(chunk.length));
```

## 222: Can you use async iterables and streams with RxJS?

Yes. `from` accepts async iterables and `ReadableStream`, so things like Node readable streams (which are async iterable) or `response.body` from fetch can become Observables. The other way, RxJS does not ship a helper to turn an Observable into an async iterable, so you need a small wrapper or a library for that.

```ts
import { from } from "rxjs";
import { createReadStream } from "fs";

from(createReadStream("./big.log")).subscribe((chunk) =>
  console.log(chunk.length),
);
```

## 223: How do you use RxJS in a React component?

Subscribe in `useEffect` and return the unsubscribe function as the cleanup. Put the inputs in the dependency array so the subscription is rebuilt when they change.

```tsx
function Clock() {
  const [time, setTime] = useState(0);

  useEffect(() => {
    const sub = interval(1000).subscribe(setTime);
    return () => sub.unsubscribe();
  }, []);

  return <span>{time}</span>;
}
```

For shared state you can also connect a `BehaviorSubject` to `useSyncExternalStore`, which avoids tearing in concurrent rendering.

## 224: How do you connect a BehaviorSubject to useSyncExternalStore?

`useSyncExternalStore` needs a subscribe function and a function that returns the current value. A `BehaviorSubject` has both.

```tsx
const count$ = new BehaviorSubject(0);

function useCount() {
  return useSyncExternalStore(
    (onChange) => {
      const sub = count$.subscribe(onChange);
      return () => sub.unsubscribe();
    },
    () => count$.getValue(),
  );
}
```

## 225: What is redux-observable?

It is a Redux middleware where side effects are written as "epics": functions that take a stream of actions (and state) and return a stream of new actions. You use RxJS operators like `filter`, `switchMap` and `catchError` to react to actions. It is less common now than Redux Toolkit's thunks or RTK Query, but it is still in use in some React projects.

## 226: How does NgRx use RxJS?

NgRx is built on RxJS. The store is an Observable of state, selectors are read with `select` or `selectSignal`, and effects are streams that listen to actions and return new actions, usually with `ofType`, `switchMap` or `exhaustMap`, and `catchError`. In SignalStore, `rxMethod` lets you pass an Observable pipeline that reacts to signals or values.

## 227: When should you use Angular signals and when RxJS?

Signals are good for state: a current value that templates and computed values read synchronously. RxJS is good for events and async flows over time: debouncing, cancelling, retrying, combining several async sources, WebSockets. A common setup is RxJS for the async part and `toSignal` at the end so the template reads a signal.

## 228: What are common sources of memory leaks with RxJS?

- Subscribing to never-ending streams (`interval`, `fromEvent`, store selectors, Subjects) in components and never unsubscribing.
- `shareReplay` without `refCount: true` on a source that never completes.
- `takeUntil` placed before `switchMap` or `mergeMap`, so inner subscriptions survive.
- Nested `subscribe` calls whose inner subscriptions are never tracked.
- `groupBy` or `distinct` on long streams that keep every key in memory.

## 229: How do you find a subscription leak?

Add `tap({ subscribe, unsubscribe, finalize })` to log when subscriptions start and end, and check that they end when the component is destroyed. Take heap snapshots in Chrome DevTools before and after opening and closing a page a few times and look for growing numbers of your component instances or Subscribers. Lint rules that flag missing `takeUntil` or nested subscribes also catch many of these early.

## 230: What is config.onUnhandledError?

`config` is exported from `rxjs`, and `config.onUnhandledError` is a function called when an error reaches a subscriber that has no `error` handler. By default the error is rethrown asynchronously (so it shows up in the console or `window.onerror`). Setting it lets you send those errors to your logging service.

```ts
import { config } from "rxjs";

config.onUnhandledError = (err) => logger.error("Unhandled RxJS error", err);
```

## 231: What is config.onStoppedNotification?

It is called when a notification is sent to a subscriber that is already closed, for example a `next` after `complete`. These are normally ignored silently. Setting this hook helps find producers that break the Observable contract.

## 232: What is ObjectUnsubscribedError?

It is thrown when you call `next` on a Subject (or subscribe to it) after the Subject itself was closed with `subject.unsubscribe()`. Calling `unsubscribe()` on a Subject is different from `complete()`: it puts the Subject into a broken state. You almost never want to call `unsubscribe()` on a Subject; call `complete()` instead.

## 233: What does windowTime in ReplaySubject do?

`new ReplaySubject(bufferSize, windowTime)` keeps at most `bufferSize` values, and only values younger than `windowTime` milliseconds are replayed. For example, `new ReplaySubject(Infinity, 5000)` replays everything from the last 5 seconds to a new subscriber.

## 234: How do you compare objects in distinctUntilChanged?

By default it uses `===`, so two different objects with the same content count as a change. Pass a compare function. For shallow cases compare the fields you care about; for nested data you can use a deep-equal helper, but deep checks on every value cost time.

```ts
filters$.pipe(
  distinctUntilChanged((a, b) => a.page === b.page && a.query === b.query),
);
```

`distinctUntilChanged` also takes a key selector as a second argument, so `distinctUntilChanged(undefined, (f) => f.query)` compares only `query`.

## 235: How do you combine several filters that change over time?

Turn each filter into a stream with a starting value, combine them with `combineLatest`, and `switchMap` to the request. `startWith` makes sure `combineLatest` emits right away.

```ts
const query$ = queryControl.valueChanges.pipe(
  startWith(queryControl.value),
  debounceTime(300),
);
const sort$ = sortControl.valueChanges.pipe(startWith(sortControl.value));
const page$ = new BehaviorSubject(1);

const results$ = combineLatest({
  query: query$,
  sort: sort$,
  page: page$,
}).pipe(switchMap((params) => api.search(params)));
```

## 236: What is the difference between exhaustMap and throttleTime for a submit button?

`throttleTime(1000)` ignores clicks for a fixed time, whether the request is done or not. If the request takes 3 seconds, a click after 1 second gets through and sends a second request. `exhaustMap` ignores clicks for exactly as long as the request is running, which matches what you want. Use `exhaustMap` when the "busy" time depends on async work.

## 237: What is the risk with concatMap when the source is fast?

`concatMap` queues every value until the inner work for the previous one finishes. If values come in faster than the inner work completes, the queue grows without limit, using memory and adding delay. If you only care about the latest value, `switchMap` is better; if you can drop values while busy, `exhaustMap` is better.

## 238: What is the risk with mergeMap without a concurrency limit?

Every source value starts inner work right away. A burst of 1000 values starts 1000 requests at once, which can overload the server, hit browser connection limits, or cause rate limit errors. Pass a concurrency limit as the second argument, like `mergeMap(fn, 5)`.

## 239: Why is switchMap risky for write operations?

`switchMap` unsubscribes from the previous request when a new value arrives. For an HTTP call, that aborts it on the client, but the server may already have received it and may still process it. You can end up with writes that happened but whose results you never saw, or writes that apply in the wrong order. For saves, deletes and payments, use `concatMap`, `mergeMap` or `exhaustMap` instead.

## 240: Why should services avoid subscribing themselves?

If a service subscribes and stores the result in a field, the data flow becomes hidden and hard to cancel, and callers can't compose it or know when it is ready. It is usually better for a service to return Observables and let the caller (a component with `async`, `toSignal`, or an effect) decide when to subscribe. Long-lived stores that own their state are the exception.

## 241: What is the difference between declarative and imperative RxJS code?

Imperative RxJS subscribes early and copies values into fields: `this.http.get(url).subscribe(data => this.data = data)`. Declarative RxJS describes the data as a stream, `data$ = this.http.get(url)`, and lets the template or a single subscription at the edge consume it. Declarative code is easier to combine, cancels on its own, and avoids flags that get out of sync.

## 242: How do you build a reducer-style state with scan?

Turn every action into a stream, merge them, and fold them into state with `scan`. This is basically a tiny Redux in a few lines.

```ts
type Action = { type: "add"; item: string } | { type: "remove"; index: number };

const actions$ = new Subject<Action>();

const items$ = actions$.pipe(
  scan((items: string[], action) => {
    switch (action.type) {
      case "add":
        return [...items, action.item];
      case "remove":
        return items.filter((_, i) => i !== action.index);
    }
  }, []),
  startWith([] as string[]),
  shareReplay({ bufferSize: 1, refCount: true }),
);
```

## 243: Should side effects go in tap or in subscribe?

Both work. Put effects that are the reason you subscribed in `subscribe`, like rendering or saving. Use `tap` for side effects that are part of a reusable pipeline, like logging, setting a loading flag or writing to a cache, so that whoever subscribes later gets them too. Avoid putting heavy logic in `tap` that changes the flow; that belongs in operators.

## 244: How do you share one WebSocket connection across the app?

Create one `webSocket()` subject in a service and expose filtered streams from it. Since the `WebSocketSubject` itself is shared between subscribers, the socket opens on the first subscription and closes when the last one leaves.

```ts
@Injectable({ providedIn: "root" })
export class LiveService {
  private socket = webSocket<Message>("wss://example.com/live");

  prices$ = this.socket.pipe(filter((m) => m.type === "price"));
  news$ = this.socket.pipe(filter((m) => m.type === "news"));

  send(msg: Message) {
    this.socket.next(msg);
  }
}
```

## 245: What does multiplex on a WebSocketSubject do?

`multiplex(subMsg, unsubMsg, messageFilter)` creates an Observable for one "channel" on a shared socket. On subscribe it sends `subMsg()` to the server, on unsubscribe it sends `unsubMsg()`, and it only emits messages that pass `messageFilter`. Many channels can share one socket this way.

```ts
const btc$ = socket.multiplex(
  () => ({ subscribe: "BTC" }),
  () => ({ unsubscribe: "BTC" }),
  (msg: any) => msg.symbol === "BTC",
);
```

## 246: How do you reconnect a WebSocket automatically?

When the socket closes with an error, the `WebSocketSubject` errors. Add `retry` with a delay, so it resubscribes and opens a new connection. A clean close completes the stream instead, so add `repeat` too if you want to reconnect then as well.

```ts
const live$ = webSocket("wss://example.com/live").pipe(
  retry({
    delay: (_err, attempt) => timer(Math.min(30_000, 1000 * 2 ** attempt)),
  }),
);
```

Note that messages sent while disconnected are buffered by the subject until the socket opens again.

## 247: What options does the webSocket function take?

Besides a URL string you can pass a config object with `url`, `protocol`, `serializer` and `deserializer` (to change from JSON), `openObserver` and `closeObserver` (to know when the socket opens or closes), `closingObserver` (called just before it closes), `binaryType`, and `WebSocketCtor` (to pass a WebSocket implementation in Node).

## 248: How do you get upload progress with rxjs/ajax?

Set `includeUploadProgress: true` (and `includeDownloadProgress: true` if needed) in the ajax config. The Observable then emits an `AjaxResponse` for each progress event, with a `type` like `'upload_progress'`, and finally the `'download_load'` response.

```ts
import { ajax } from "rxjs/ajax";

ajax({
  url: "/api/upload",
  method: "POST",
  body: formData,
  includeUploadProgress: true,
}).subscribe((res) => {
  if (res.type === "upload_progress") {
    console.log(`${Math.round((res.loaded / res.total) * 100)}%`);
  }
});
```

## 249: How do you fall back to a second server if the first is slow?

Use `race` with a delayed fallback, or `timeout` with the `with` option. The `timeout` version only calls the backup if the first one is too slow.

```ts
const primary$ = http.get("/api/data");
const backup$ = http.get("https://backup.example.com/api/data");

primary$.pipe(timeout({ first: 2000, with: () => backup$ }));
```

## 250: What is the difference between iif and defer for conditions?

`iif(cond, a$, b$)` only lets you pick between two Observables that already exist as arguments. `defer(() => cond() ? a$ : b$)` can do anything, including building the Observable on the spot, picking from more than two, or using values only known at subscribe time. Since `iif` is just a wrapper around `defer`, many people use `defer` for everything.

## 251: How does NestJS use RxJS?

NestJS uses Observables in interceptors (where `next.handle()` returns an Observable of the response), in microservices transports (client proxies return Observables), and in some modules like `@nestjs/axios` whose `HttpService` returns Observables. Route handlers can also return an Observable, and Nest sends the last value when it completes. In plain service code, `firstValueFrom` and `lastValueFrom` are common to use these with `async/await`.

```ts
@Injectable()
export class TimingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<unknown> {
    const start = Date.now();
    return next
      .handle()
      .pipe(tap(() => console.log(`took ${Date.now() - start}ms`)));
  }
}
```

## 252: How do you detect a double click with RxJS?

Group clicks that are close together and count them. One way is `buffer` with a debounced copy of the same stream as the closing signal.

```ts
const clicks$ = fromEvent(button, "click").pipe(share());

const doubleClicks$ = clicks$.pipe(
  buffer(clicks$.pipe(debounceTime(250))),
  filter((clicks) => clicks.length === 2),
);
```

`share` is needed so both uses of `clicks$` listen to the same events.

## 253: How do you track online and offline status?

Merge the `online` and `offline` window events, map them to booleans and start with the current value of `navigator.onLine`.

```ts
const online$ = merge(
  fromEvent(window, "online").pipe(map(() => true)),
  fromEvent(window, "offline").pipe(map(() => false)),
).pipe(startWith(navigator.onLine), distinctUntilChanged());
```

## 254: How do you pause polling while the browser tab is hidden?

Turn `visibilitychange` into a stream of booleans and `switchMap` to the polling stream or to `EMPTY`.

```ts
const visible$ = fromEvent(document, "visibilitychange").pipe(
  map(() => document.visibilityState === "visible"),
  startWith(document.visibilityState === "visible"),
);

const data$ = visible$.pipe(
  switchMap((visible) =>
    visible ? timer(0, 10_000).pipe(switchMap(() => api.load())) : EMPTY,
  ),
);
```

## 255: How do you detect that a user is idle?

Merge activity events and `switchMap` each one to a timer. If the timer finishes without new activity, the user is idle.

```ts
const activity$ = merge(
  fromEvent(document, "mousemove"),
  fromEvent(document, "keydown"),
  fromEvent(document, "scroll"),
);

const idle$ = activity$.pipe(
  startWith(null),
  switchMap(() => timer(5 * 60_000)),
);

idle$.subscribe(() => logout());
```

## 256: How do you retry a request when the browser comes back online?

Use the `delay` function of `retry` to wait for the `online` event instead of a timer.

```ts
http.get("/api/data").pipe(
  retry({
    delay: () => (navigator.onLine ? timer(1000) : fromEvent(window, "online")),
  }),
);
```

## 257: How do you limit calls to N per second?

A simple way is `concatMap` with a small delay between items, which spaces calls evenly. For "at most N in each second", batch the items with `bufferTime` and send each batch.

```ts
// one call every 200ms = 5 per second
items$.pipe(concatMap((item) => api.send(item).pipe(delay(200))));
```

If the server's limit is about concurrent calls instead, `mergeMap(fn, N)` is the right tool.

## 258: How do you avoid sending the same request twice while one is in flight?

Cache the in-flight Observable per key with `shareReplay`, and remove it from the cache when it ends so the next call fetches fresh data.

```ts
private inFlight = new Map<string, Observable<User>>();

getUser(id: string) {
  if (!this.inFlight.has(id)) {
    const req$ = this.http.get<User>(`/api/users/${id}`).pipe(
      finalize(() => this.inFlight.delete(id)),
      shareReplay({ bufferSize: 1, refCount: true }),
    );
    this.inFlight.set(id, req$);
  }
  return this.inFlight.get(id)!;
}
```

## 259: How do you do an optimistic update with RxJS?

Update the local state right away, send the request, and roll back in `catchError` if it fails.

```ts
toggleDone(todo: Todo) {
  const before = this.state.value;
  this.state.next(before.map((t) => (t.id === todo.id ? { ...t, done: !t.done } : t)));

  return this.api.update(todo.id, { done: !todo.done }).pipe(
    catchError((err) => {
      this.state.next(before);
      return throwError(() => err);
    }),
  );
}
```

## 260: How do you show cached data first and then fresh data?

Start with the cached value (if there is one) and then emit the server value. `concat` keeps them in order, and `defer` reads the cache at subscribe time.

```ts
const products$ = concat(
  defer(() => (cache.has("products") ? of(cache.get("products")) : EMPTY)),
  http
    .get<Product[]>("/api/products")
    .pipe(tap((p) => cache.set("products", p))),
);
```

## 261: How do you fall back to a cached value when a request fails?

Use `catchError` and return the cached value, or rethrow if there is no cache.

```ts
http.get<Settings>("/api/settings").pipe(
  tap((s) => localStorage.setItem("settings", JSON.stringify(s))),
  catchError((err) => {
    const cached = localStorage.getItem("settings");
    return cached ? of(JSON.parse(cached) as Settings) : throwError(() => err);
  }),
);
```

## 262: What lint rules help with RxJS?

The `eslint-plugin-rxjs-x` package (a maintained fork of `eslint-plugin-rxjs`) has rules like `no-nested-subscribe`, `no-unsafe-takeuntil`, `no-ignored-observable`, `finnish` (the `$` suffix), `no-subject-value`, and rules that flag deprecated APIs. Angular projects often add `@angular-eslint` rules too. These catch leaks and misuse that type checks miss.

## 263: Why does TypeScript sometimes lose types after many operators in pipe?

`pipe` has typed overloads for up to nine operators. If you pass more, the result type falls back to `Observable<unknown>`. The fix is to split the chain into two `pipe` calls or group some operators into a custom operator.

## 264: What were the main breaking changes from RxJS 6 to RxJS 7?

- `toPromise` was deprecated in favor of `firstValueFrom` and `lastValueFrom`.
- Many signatures got stricter types; for example, `of(1, 'a')` now infers a union type.
- `subscribe` with several positional callbacks was deprecated.
- `throwError(value)` was deprecated in favor of `throwError(() => value)`.
- Multicasting operators (`multicast`, `publish`, `refCount` and friends) were deprecated in favor of `share`, `shareReplay`, `connectable` and `connect`.
- `combineLatest` and `forkJoin` with a result selector or spread arguments were deprecated in favor of arrays or objects.
- Scheduler arguments in `of`, `from` and others were deprecated in favor of `scheduled`.
- The library got smaller and faster, and `finalize` callback order changed.

## 265: How do you migrate an RxJS 6 project to RxJS 7?

Update the package, run the build, and fix type errors first, since stricter types are the main source of breaks. Then work through deprecation warnings: replace `toPromise`, change `throwError(x)` to `throwError(() => x)`, swap `publishReplay(1), refCount()` for `shareReplay`, and move from positional `subscribe` callbacks to an observer object. Lint rules for deprecated APIs help find them. For Angular, `ng update` handles the version bump together with Angular.

## 266: How does RxJS tree shaking work?

RxJS 7 ships ES modules and operators are plain functions, so bundlers only keep the operators you import. Because operators are used through `pipe` rather than added to `Observable.prototype`, there are no side-effect imports. This is why patching imports like `rxjs/add/operator/map` from RxJS 5 are gone.

## 267: How do you debounce per key, for example per input field?

Group the stream by key with `groupBy`, debounce each group on its own, and merge them back.

```ts
fieldChanges$.pipe(
  groupBy((change) => change.field),
  mergeMap((group$) => group$.pipe(debounceTime(500))),
  concatMap((change) => api.saveField(change)),
);
```

A plain `debounceTime` on the whole stream would drop a change in one field when another field changes right after.

## 268: How do you emit a value only after a user has held a key for some time?

Start a timer on `keydown` and cancel it on `keyup`. If the timer wins, the key was held long enough.

```ts
const down$ = fromEvent<KeyboardEvent>(document, "keydown").pipe(
  filter((e) => e.key === " " && !e.repeat),
);
const up$ = fromEvent<KeyboardEvent>(document, "keyup").pipe(
  filter((e) => e.key === " "),
);

const held$ = down$.pipe(switchMap(() => timer(1000).pipe(takeUntil(up$))));
```

## 269: How do you detect a keyboard shortcut sequence?

Keep the last N keys with `scan` (or `bufferCount(N, 1)`), and check if they match the sequence.

```ts
const code = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown"];

fromEvent<KeyboardEvent>(document, "keydown")
  .pipe(
    map((e) => e.key),
    bufferCount(code.length, 1),
    filter((keys) => keys.every((k, i) => k === code[i])),
  )
  .subscribe(() => console.log("sequence entered"));
```

## 270: How do you trigger a reload of data from a button?

Merge a refresh Subject (or button clicks) with an initial trigger and `switchMap` to the request. Every click loads again and cancels a request still running.

```ts
refresh$ = new Subject<void>();

data$ = this.refresh$.pipe(
  startWith(undefined),
  switchMap(() => this.api.load()),
);
```

## 271: Why does subscribing to a Subject inside the template cause issues with hot data?

A plain `Subject` doesn't remember anything, so if a value is pushed before the `async` pipe subscribes (for example during component setup), the template never sees it. Use a `BehaviorSubject` or `ReplaySubject(1)`, or share the stream with `shareReplay(1)`, when the template needs the latest value no matter when it subscribes.

## 272: What is the difference between ReplaySubject(1) and BehaviorSubject?

Both give new subscribers the latest value. `BehaviorSubject` needs an initial value and always has one, so a new subscriber gets something right away, and you can read `.value`. `ReplaySubject(1)` has no value until the first `next`, so subscribers wait for real data. Use `ReplaySubject(1)` when there is no sensible default, to avoid emitting a fake `null` first.

## 273: Can you use RxJS in a Web Worker or Node.js service?

Yes, RxJS has no DOM dependency except for helpers like `fromEvent` on DOM targets, `ajax`, `animationFrames` and `animationFrameScheduler`. In a worker, you can turn `message` events into a stream with `fromEvent(self, 'message')`. In Node.js it works with `EventEmitter`s, streams, and timers.

## 274: How do you run some code only when the first subscriber arrives?

Wrap it in `defer` and share the result. `defer` runs the setup on subscribe, and `share` or `shareReplay` makes sure later subscribers join the same run instead of running setup again.

```ts
const connection$ = defer(() => {
  console.log("connecting once");
  return openStream();
}).pipe(share());
```

## 275: How do you merge several streams but know which one each value came from?

Map each stream's values to an object that includes a source tag before merging.

```ts
const events$ = merge(
  clicks$.pipe(map((e) => ({ source: "click" as const, e }))),
  keys$.pipe(map((e) => ({ source: "key" as const, e }))),
);
```

## 276: How do you handle errors from an inner Observable in mergeMap without stopping the others?

Put `catchError` on each inner Observable, so a failing one turns into a fallback value (or `EMPTY`) and the other inner Observables and the outer stream keep running.

```ts
from(urls).pipe(
  mergeMap((url) =>
    http.get(url).pipe(
      catchError((err) => {
        console.warn("failed", url, err);
        return EMPTY;
      }),
    ),
  ),
);
```

## 277: What is a "trigger" stream and why is it useful?

A trigger stream carries no useful data; it only says "do it now". Examples are `refresh$`, `save$` or `retry$`. You `switchMap` (or `exhaustMap`) from it to the actual work. This keeps the work itself declarative while letting buttons and other events start it.

## 278: How do you keep the previous results visible while new ones load?

Don't reset the list on each new request. Emit a loading flag separately, or use `scan` to keep the last data while changing only the `loading` field.

```ts
const view$ = query$.pipe(
  switchMap((q) =>
    api.search(q).pipe(
      map((data) => ({ loading: false, data })),
      startWith({ loading: true }),
    ),
  ),
  scan((prev, next) => ({ ...prev, ...next }), {
    loading: false,
    data: [] as Result[],
  }),
);
```

## 279: How do you convert an Observable to a signal outside Angular?

Outside Angular you don't have `toSignal`. You subscribe and push each value into whatever reactive primitive your framework has: React state, a Vue `ref`, a Solid signal or a Preact signal, and unsubscribe on cleanup. Many frameworks have small helpers for this, for example `@vueuse/rxjs` for Vue.

## 280: How do you make sure an Observable completes after a certain amount of time?

Use `takeUntil(timer(ms))`. Unlike `timeout`, which errors, this just completes the stream when time is up.

```ts
liveUpdates$.pipe(takeUntil(timer(60_000))).subscribe();
```

## 281: How do you emit a value after a delay only if nothing else happened?

That is what `debounceTime` does. For a single fallback, you can also race the event against a timer.

```ts
const result$ = race(
  response$,
  timer(3000).pipe(map(() => "still waiting...")),
);
```

## 282: How do you chain two streams where the second needs the first's last value?

Use `last()` (or `takeLast(1)`) on the first and then `switchMap`, or use `concatMap` to run after it completes.

```ts
upload$.pipe(
  last(),
  switchMap((uploadResult) => api.confirm(uploadResult.id)),
);
```

## 283: What is the difference between EMPTY and of() and NEVER?

`EMPTY` and `of()` with no arguments both complete right away with no values. `NEVER` never completes. Returning `EMPTY` from a `switchMap` makes that inner step finish quietly, while returning `NEVER` keeps the outer stream from completing (for `concatMap`, it blocks the queue forever). So pick `EMPTY` for "skip this" in almost all cases.

## 284: How do you subscribe to an Observable only once, no matter how many places use it?

Share it. `share()` for live streams (events, sockets) where late subscribers don't need history, and `shareReplay({ bufferSize: 1, refCount: true })` for data that late subscribers should get. In Angular you can also convert it once with `toSignal` and read the signal in many places.

## 285: How do you handle errors in a long-lived stream like NgRx effects?

Put `catchError` inside the flattening operator, return an error action, and let the outer `actions$` stream keep running. If `catchError` is on the outer stream, the effect dies after the first error. NgRx also resubscribes effects that error a limited number of times by default, but you should not rely on that.

```ts
export const loadUsers = createEffect(
  (actions$ = inject(Actions), api = inject(UsersApi)) =>
    actions$.pipe(
      ofType(UsersActions.load),
      switchMap(() =>
        api.getAll().pipe(
          map((users) => UsersActions.loaded({ users })),
          catchError((error) => of(UsersActions.failed({ error }))),
        ),
      ),
    ),
  { functional: true },
);
```

The `inject` calls sit in default parameters, so they run while the effect is created, inside an injection context.

## 286: How do you test code that uses a BehaviorSubject service?

Use the real service with a fake API, or a stub with a `BehaviorSubject` you control. Push values with `next` and check what the code under test does. For values over time, collect them in an array.

```ts
it("shows the latest count", () => {
  const count$ = new BehaviorSubject(0);
  const seen: number[] = [];
  count$.pipe(map((n) => n * 2)).subscribe((v) => seen.push(v));
  count$.next(1);
  count$.next(2);
  expect(seen).toEqual([0, 2, 4]);
});
```

## 287: How do you test Angular code that uses debounceTime?

Either use the `TestScheduler`, or Angular's `fakeAsync` with `tick(ms)` to move time forward. Both avoid real waits. `fakeAsync` works because `debounceTime` uses `setTimeout` through `asyncScheduler`, which zone.js fakes. In zoneless tests, use your test runner's fake timers instead, for example `vi.useFakeTimers()` and `vi.advanceTimersByTime(300)` in Vitest.

## 288: How do you use the time and flush helpers in TestScheduler run?

`time('---|')` turns a marble string into a number of frames, which is handy to pass the same duration to the code under test. `flush()` runs all scheduled work right now, so you can make assertions in the middle of a test, for example on side effects in `tap`.

```ts
testScheduler.run(({ cold, expectObservable, time }) => {
  const t = time("---|"); // 3
  const source$ = cold("a|");
  expectObservable(source$.pipe(delay(t))).toBe("---(a|)");
});
```

## 289: What does the animate helper in TestScheduler do?

`animate(marbles)` lets you control when `animationFrames()` and `animationFrameScheduler` tick inside `run()`. Each value in the marble string is one animation frame, so you can test animation code with the same marble approach.

## 290: What is the difference between subscribe and forEach on an Observable?

`observable.forEach(fn)` subscribes and returns a Promise that resolves when the Observable completes and rejects if it errors. It is handy in `async` functions. You cannot unsubscribe from it, though, so don't use it with streams that may never complete. Most code uses `subscribe` or `lastValueFrom` instead.

## 291: How do you keep only the latest N values in an array?

Use `scan` and slice the array to N each time.

```ts
const lastFive$ = values$.pipe(
  scan((acc, v) => [...acc, v].slice(-5), [] as number[]),
);
```

## 292: How do you build a typeahead that also shows "no results" and errors?

Map to a view state per request: loading first, then results or an empty or error state.

```ts
const view$ = term$.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap((term) =>
    term.length < 2
      ? of({ kind: "idle" as const })
      : api.search(term).pipe(
          map((items) =>
            items.length
              ? { kind: "ok" as const, items }
              : { kind: "empty" as const },
          ),
          startWith({ kind: "loading" as const }),
          catchError(() => of({ kind: "error" as const })),
        ),
  ),
);
```

## 293: Why do some people say "don't use Subjects", and when are they fine?

Subjects are imperative: anyone with access can push values, and logic built around many `next` calls is harder to follow than a pipeline built from sources. Often a stream can come straight from events (`fromEvent`, `valueChanges`) without a Subject. Subjects are fine as the bridge between non-reactive code and RxJS, like a button handler calling `save$.next()`, or as private state in a service.

## 294: How do you prevent the async pipe from making duplicate requests?

Each `async` pipe subscribes separately, so two `| async` on the same cold HTTP Observable send two requests. Use one subscription with `@if (data$ | async; as data)` and read `data` inside, share the Observable with `shareReplay`, or convert it to a signal with `toSignal` and read the signal as many times as you want.

## 295: What does subscribe with no arguments do?

It starts the Observable and ignores all values. Errors still go to the unhandled error handler. It is used when the work is done in `tap` or by the source itself, like a save request. Many linters ask you to at least handle errors in that case.

## 296: How do you combine an Observable and a Promise?

Most operators and creation functions accept Promises as `ObservableInput`, so you can mix them directly. `from(promise)` converts one explicitly, and `switchMap(() => promise)` works too.

```ts
combineLatest([user$, from(loadConfig())]).subscribe(([user, config]) => {
  console.log(user, config);
});
```

## 297: How do you run a stream only while an element is visible on screen?

Wrap `IntersectionObserver` in an Observable, map to a visible flag, and `switchMap` to the work or `EMPTY`.

```ts
const visible$ = (el: Element) =>
  new Observable<boolean>((subscriber) => {
    const io = new IntersectionObserver(([entry]) =>
      subscriber.next(entry.isIntersecting),
    );
    io.observe(el);
    return () => io.disconnect();
  });

visible$(chart).pipe(
  distinctUntilChanged(),
  switchMap((v) =>
    v ? timer(0, 5000).pipe(switchMap(() => api.stats())) : EMPTY,
  ),
);
```

## 298: How do you wrap ResizeObserver or MutationObserver in an Observable?

Create the observer inside `new Observable`, push entries with `next`, and disconnect in the teardown function. Each subscriber gets its own observer.

```ts
const size$ = (el: Element) =>
  new Observable<DOMRectReadOnly>((subscriber) => {
    const ro = new ResizeObserver((entries) =>
      subscriber.next(entries[0].contentRect),
    );
    ro.observe(el);
    return () => ro.disconnect();
  });
```

## 299: How do you know when all values from a mergeMap are done?

The output of `mergeMap` completes when the source has completed and every inner Observable has completed. So `finalize`, `toArray`, `last` or the `complete` callback after the `mergeMap` run once all the work is done.

## 300: What is a good rule of thumb for where to subscribe?

Subscribe as late as possible, ideally in one place at the edge: the template with `async`, a `toSignal` call, an effect, or one `subscribe` at the top of a script. Everything before that should be pure pipeline code that returns Observables. This keeps cancellation automatic and makes the flow easy to test.

# Advanced Questions (301-450)

## 301: What actually happens inside subscribe?

`subscribe` wraps what you passed (a function or a partial observer) in a `Subscriber`. The `Subscriber` is both the object your producer calls `next` on and a `Subscription`. Then RxJS calls the Observable's subscribe function with that `Subscriber`, and adds whatever teardown the function returns to the `Subscriber`. The `Subscriber` is returned to you as the Subscription, so calling `unsubscribe()` on it runs the teardown.

## 302: What does the Subscriber class guarantee?

It enforces the Observable contract. Once `error` or `complete` has been called, or once it has been unsubscribed, it sets `closed` to `true` and ignores further notifications. It also runs teardown right after `error` or `complete`. Your callbacks are wrapped so an error thrown inside a `next` handler does not travel back up into the producer; in RxJS 7 it is reported as an unhandled error instead.

## 303: How are pipeable operators implemented internally in RxJS 7?

Most operators use an internal helper (`operate`) that creates a new Observable, and inside it they subscribe to the source with an internal `OperatorSubscriber` that has custom `next`, `error` and `complete` handlers. The operator subscriber forwards to the downstream subscriber and is chained to it, so unsubscribing downstream also unsubscribes from the source. These helpers are internal and not part of the public API.

## 304: What was Observable.lift and why should you not use it?

`lift` created a new Observable linked to the source with an "operator" object. RxJS 5 and 6 built every operator on it, and some libraries subclassed Observable and overrode `lift` to keep their subclass through `pipe`. In RxJS 7 `lift` is marked as internal and deprecated for public use. Write custom operators as functions that return `new Observable` or that compose existing operators.

## 305: How does unsubscription travel through an operator chain?

Each operator subscribes to the one before it and is added to the subscriber of the one after it. When you unsubscribe at the end, the outermost subscriber is closed, which runs its finalizers, which includes unsubscribing the operator subscriber above it, and so on up to the source, whose teardown function runs last. Inner subscriptions created by operators like `switchMap` are added the same way, so they are closed too.

## 306: How can take(1) stop a synchronous infinite source?

The producer can check `subscriber.closed`. When `take(1)` gets its first value, it completes and unsubscribes, which marks the subscriber as closed while the producer's loop is still running. A well-written synchronous producer checks `closed` and stops.

```ts
const naturals$ = new Observable<number>((subscriber) => {
  let i = 0;
  while (!subscriber.closed) subscriber.next(i++);
});

naturals$.pipe(take(3)).subscribe(console.log); // 0, 1, 2, then stops
```

Without the `closed` check the loop never ends, because teardown can only be returned after the loop is done.

## 307: Why is a teardown returned from a synchronous producer sometimes run late?

The teardown is returned at the end of the subscribe function. If the producer completes or gets unsubscribed during that function (for example `take(1)` on a synchronous source), RxJS can't call a teardown it hasn't received yet. Once the function returns, RxJS sees the subscriber is already closed and runs the teardown right away. That is correct, but it means resources created before the first `next` stay alive until the function returns, so check `closed` or add teardown early with `subscriber.add()`.

## 308: What happens when an observer's next callback throws?

In RxJS 7, the error does not propagate back to the producer and does not go to the observer's own `error` callback. It is reported through `reportUnhandledError`, which by default rethrows it in a `setTimeout`, or calls `config.onUnhandledError` if you set it. The producer and other subscribers keep working. The old RxJS 5 behavior, where errors were thrown synchronously, can be turned on with `config.useDeprecatedSynchronousErrorHandling`, but it is deprecated.

## 309: What is reentrancy in RxJS and why does it matter?

Reentrancy happens when calling `next` causes, during that same call, another `next` on the same Subject or source. For example, a subscriber of a Subject calls `subject.next` again. The nested value is delivered to all subscribers before the outer call finishes, so subscribers later in the list may see the second value before the first. This can make state look out of order. To avoid it, don't push into a Subject from its own subscribers, or schedule the push with `observeOn(asapScheduler)` or `queueScheduler`.

```ts
const s = new Subject<number>();
s.subscribe((v) => {
  if (v === 1) s.next(2);
  console.log("A", v);
});
s.subscribe((v) => console.log("B", v));
s.next(1);
// A 2, B 2, A 1, B 1
```

## 310: How does a Subject deliver values to subscribers internally?

A Subject keeps an array of current observers. On `next`, RxJS 7 copies the array first and then loops over the copy. That means an observer that subscribes during a `next` call does not get the value being delivered, and an observer that unsubscribes during it may still get it if it was already in the copy (it is closed, though, so it ignores it). Subjects also keep `hasError`, `thrownError` and `isStopped` so late subscribers get the terminal notification.

## 311: What happens when you subscribe to a BehaviorSubject that has errored?

The new subscriber gets the error right away and nothing else. Reading `.value` or calling `getValue()` throws the stored error. This is one reason a `BehaviorSubject` used as a store should never receive `error`: one error makes the whole store unusable for the rest of the app's life.

## 312: What is the diamond problem in RxJS?

If a stream `a$` feeds two derived streams `b$` and `c$`, and you combine `b$` and `c$` with `combineLatest`, one change in `a$` reaches the combination twice: first through `b$` (with `c$` still old), then through `c$`. The combined output briefly shows an inconsistent state that never really existed. Signals avoid this by design, but RxJS does not. Fixes include deriving both values in one `map`, batching with `auditTime(0)` or `debounceTime(0, asapScheduler)`, or modeling state as one object.

```ts
const a$ = new BehaviorSubject(1);
const b$ = a$.pipe(map((x) => x * 2));
const c$ = a$.pipe(map((x) => x * 3));
combineLatest([b$, c$]).subscribe(console.log);
a$.next(2); // [4, 3] (glitch) then [4, 6]
```

## 313: What does combineLatest emit with synchronous sources?

It subscribes to the sources in order. With `combineLatest([of(1, 2), of('a', 'b')])`, the first source emits `1` and `2` before the second source is subscribed, so only `2` is the latest when the second source starts. The output is `[2, 'a']` and `[2, 'b']`. This surprises people who expect `[1, 'a']`. Order and sync timing matter, which is why tests should use realistic timing.

## 314: How do schedulers work internally?

A scheduler creates actions. Calling `scheduler.schedule(work, delay, state)` creates a `SchedulerAction` that runs `work` later. `AsyncAction` uses `setInterval` under the hood and reuses the same interval when an action reschedules itself with the same delay, which makes `interval` cheap. `AsapAction` uses a microtask, `AnimationFrameAction` uses `requestAnimationFrame`, and `QueueAction` runs synchronously but puts nested work in a queue.

## 315: What is the queueScheduler good for?

It runs tasks synchronously, but if a task schedules another task while running, the new one is put in a queue and runs after the current one finishes, instead of running nested. This "trampoline" turns recursion into a loop, which prevents stack overflows and gives breadth-first order for recursive operators like `expand` when you need it.

```ts
queueScheduler.schedule(() => {
  queueScheduler.schedule(() => console.log("inner"));
  console.log("outer");
});
// outer, inner
```

## 316: How does recursive scheduling with this.schedule work?

Inside a scheduled function, `this` is the action, and calling `this.schedule(newState, delay)` reschedules the same action instead of creating a new one. This is how `interval` is built. It's cheaper than calling `scheduler.schedule` again, and for `asyncScheduler` with the same delay it keeps the same underlying `setInterval`.

```ts
asyncScheduler.schedule(function (count = 0) {
  console.log(count);
  if (count < 3) this.schedule(count + 1, 1000);
}, 1000);
```

## 317: How does TestScheduler run mode get virtual time into operators?

Inside `run()`, the `TestScheduler` sets itself as the delegate for the built-in schedulers and timestamp providers. So `asyncScheduler`, `asapScheduler`, `animationFrameScheduler`, the `Date`-based timestamp provider and the interval and timeout providers used by operators all go through virtual time. You don't have to pass a scheduler into every operator, as you did in RxJS 5.

## 318: Why can Date.now or Promises break marble tests?

Run mode only patches RxJS's own schedulers and providers. Your code calling `Date.now()` directly, `setTimeout` outside RxJS, or Promises (which use real microtasks) is not virtualized. A Promise inside `switchMap` resolves after `run()` has already finished checking, so the test fails or misses values. Use `asyncScheduler.now()` for time, keep Promises out of the code under test, or test those parts with `async/await` and fake timers instead of marbles.

## 319: What is backpressure and how does RxJS handle it?

Backpressure is what happens when the producer is faster than the consumer. RxJS is push-based and has no built-in way for a consumer to say "slow down". You handle it with operators: lossy ones drop values (`throttleTime`, `auditTime`, `sampleTime`, `debounceTime`, `exhaustMap`, `switchMap`), and lossless ones buffer or queue values (`bufferTime`, `bufferCount`, `concatMap`, `mergeMap` with a concurrency limit). Lossless strategies need a limit, or memory grows.

## 320: When would you use async iterators instead of Observables for backpressure?

Async iterators are pull-based: the consumer asks for the next value with `await`, so a slow consumer naturally slows the producer. That fits reading files, database cursors or paginated APIs where the producer can wait. Observables fit events you can't pause, like clicks or WebSocket messages. You can mix them: `from(asyncIterable)` pulls only as fast as RxJS processes synchronous work, but async work inside `mergeMap` still lets values pile up.

## 321: What does each operator cost at runtime?

Each operator in a chain adds a subscriber object per subscription and a function call per value. For normal UI streams this is tiny. It starts to matter when you create thousands of subscriptions (for example one per list row), when values come in at very high rates, or when you build new pipelines per value inside `mergeMap`. In those cases, share one stream, do work in one `map` instead of many small operators, or batch values.

## 322: How do RxJS timers affect Angular change detection with zone.js?

With zone.js, every `setTimeout` and `setInterval` that RxJS schedules is a task in the Angular zone, and when it finishes Angular runs change detection for the app. A fast `interval`, `animationFrames` or a busy `debounceTime` can trigger a lot of change detection. You can run such streams outside the zone with `NgZone.runOutsideAngular`, and only re-enter with `zone.run` when the UI must update.

## 323: How does RxJS work with zoneless Angular?

Without zone.js, Angular doesn't know when an RxJS callback changed something. Updates show up only if they go through something Angular tracks: setting a signal, the `async` pipe (which marks the view for check), `toSignal`, or calling `ChangeDetectorRef.markForCheck()`. So code that writes plain fields in a `subscribe` callback stops updating the view and should be moved to signals.

## 324: Why can shareReplay cause a leak even after components are destroyed?

With the default `refCount: false`, `shareReplay` keeps its subscription to the source alive after every subscriber leaves. If the source never completes (a store selector, a WebSocket, `interval`, a `valueChanges` stream), it keeps running forever, and its closures keep component state in memory. Use `shareReplay({ bufferSize: 1, refCount: true })` for such sources.

## 325: How does share behave after the source errors or completes?

With the defaults, `share` resets after an error or completion. The next subscriber subscribes to the source again from scratch. `shareReplay` is built on `share` with `resetOnError: true`, `resetOnComplete: false` and `resetOnRefCountZero` equal to `refCount`. So after an error `shareReplay` retries the source for the next subscriber, but after completion it keeps replaying the cached values forever.

## 326: How do you keep a shared connection open for a short time after the last subscriber leaves?

Use `share` with `resetOnRefCountZero` as a function that returns a timer. If a new subscriber comes before the timer fires, the connection is reused; otherwise it closes. This avoids reconnecting when users quickly switch between pages.

```ts
const live$ = webSocket("wss://example.com/live").pipe(
  share({
    connector: () => new ReplaySubject(1),
    resetOnRefCountZero: () => timer(10_000),
  }),
);
```

## 327: What is the danger of using a Subject as an observer for several sources?

If you do `a$.subscribe(subject)` and `b$.subscribe(subject)`, the first source that completes also completes the Subject, so values from the other one are ignored afterwards. The same goes for errors. If you want to forward several sources into one Subject, forward only `next`, or better, `merge` the sources and subscribe once.

```ts
a$.subscribe({ next: (v) => subject.next(v) });
```

## 328: How should you structure error handling in a large app?

Use layers. Handle expected errors (validation, 404, conflicts) close to where they happen, usually in `catchError` inside the flattening operator, and turn them into state. Retry transient errors (network, 5xx) in one shared place, like an HTTP interceptor with `retry` and backoff. Send unexpected errors to a global handler: Angular's `ErrorHandler` and `config.onUnhandledError`. Keep long-lived streams alive by never letting errors reach the outer chain.

## 329: How do you type errors in RxJS?

RxJS types errors as `any`, because anything can be thrown. In `catchError`, treat the error as `unknown` and narrow it with `instanceof` or type guards before using it. A common pattern is to turn errors into typed values early (a result union like `{ ok: false, error: AppError }`), so the rest of the pipeline is fully typed.

```ts
catchError((err: unknown) => {
  if (err instanceof HttpErrorResponse && err.status === 404) return of(null);
  return throwError(() => err);
});
```

## 330: What security issues should you watch for in RxJS code?

RxJS itself doesn't add security holes, but streams often carry untrusted data. Encode user input before putting it in URLs inside `switchMap`. Validate WebSocket and `postMessage` payloads before trusting them; `webSocket` parses JSON but does not check the shape. Limit buffers (`bufferTime`, `ReplaySubject(Infinity)`, `concatMap` queues, `distinct`) so a flood of messages can't exhaust memory. And make sure streams carrying user data are torn down on logout, so the next user doesn't see them.

## 331: How do you validate incoming WebSocket messages?

Parse and validate each message in a `map`, with a schema library like Zod or a hand-written type guard, and drop or log invalid ones. Don't let one bad message error the whole socket stream.

```ts
const Price = z.object({ symbol: z.string(), price: z.number() });

const prices$ = socket.pipe(
  mergeMap((raw) => {
    const result = Price.safeParse(raw);
    if (!result.success) console.warn("bad message", raw);
    return result.success ? [result.data] : [];
  }),
);
```

Returning an empty array from `mergeMap` drops the value, and the result stays typed as the parsed shape.

## 332: Does unsubscribing from an HTTP call stop the work on the server?

No. Unsubscribing aborts the request on the client, so the response is ignored and the connection may close, but the server may have already started or finished processing. If cancellation matters on the server (long reports, expensive queries), you need a server-side cancel endpoint, a job id you can cancel, or a server that reacts to closed connections. Design writes to be safe even if the client gave up.

## 333: How do you connect an AbortSignal to RxJS?

Turn the signal's `abort` event into a notifier and use `takeUntil`. Going the other way, create an `AbortController` inside `new Observable` and abort it in the teardown.

```ts
const untilAborted = <T>(signal: AbortSignal) =>
  takeUntil<T>(signal.aborted ? of(true) : fromEvent(signal, "abort"));

function fetchJson$<T>(url: string) {
  return new Observable<T>((subscriber) => {
    const ctrl = new AbortController();
    fetch(url, { signal: ctrl.signal })
      .then((r) => r.json())
      .then((data) => {
        subscriber.next(data);
        subscriber.complete();
      })
      .catch((err) => subscriber.error(err));
    return () => ctrl.abort();
  });
}
```

## 334: How do you turn an Observable into an async iterable, and what is the catch?

You subscribe, push values into a queue, and let the iterator pull from it, ending on complete and throwing on error. The catch is backpressure: the Observable keeps pushing while the consumer is busy awaiting, so the queue can grow without limit. You need to decide on a buffer size and what to do when it is full (drop oldest, drop newest, or error). Also make sure `return()` on the iterator unsubscribes when the `for await` loop exits early.

## 335: What is the native Observable API in browsers?

The WHATWG Observable proposal adds an `Observable` type to the web platform and a `when()` method on `EventTarget`, so `element.when('click')` returns an Observable of events. It has shipped in Chromium-based browsers, while other browsers have not shipped it yet. It differs from RxJS: you cancel with an `AbortSignal` passed to `subscribe` instead of a Subscription, some methods like `first()`, `toArray()` and `forEach()` return Promises, and the operator set is small. RxJS can still work with it as an input source.

## 336: What is Symbol.observable and why does it exist?

`Symbol.observable` is a well-known symbol (polyfilled by RxJS as the string `'@@observable'` when the symbol doesn't exist) for interop. An object with a `[Symbol.observable]()` method that returns something with `subscribe` is an `InteropObservable`, and RxJS's `from` accepts it. Libraries like Redux stores and some state libraries implement it, so you can do `from(store)` to get a stream of state.

## 337: How would you build a small state store on top of RxJS?

Keep state in a `BehaviorSubject`, change it only through methods that produce new objects, and expose selectors that `map` and `distinctUntilChanged` the state. Share each selector with `shareReplay({ bufferSize: 1, refCount: true })` if it's expensive. Never send `error` to the state Subject, and handle async work in effects that call update methods instead of putting it inside the store.

```ts
class Store<S extends object> {
  private state$ = new BehaviorSubject<S>(this.initial);
  constructor(private initial: S) {}

  select<R>(fn: (s: S) => R): Observable<R> {
    return this.state$.pipe(map(fn), distinctUntilChanged());
  }

  update(fn: (s: S) => S) {
    this.state$.next(fn(this.state$.value));
  }
}
```

## 338: How do you avoid recalculating derived data for every subscriber?

Derived streams are cold, so each subscriber runs `map` separately. For cheap mapping that doesn't matter. For expensive work (sorting large lists, heavy filtering), share the derived stream with `shareReplay({ bufferSize: 1, refCount: true })` so the work runs once per change, and use `distinctUntilChanged` on the inputs so it runs only when they really change.

## 339: What is the difference between batching with debounceTime(0), auditTime(0) and asapScheduler?

All three wait a little so that several synchronous emissions merge into one. `debounceTime(0)` and `auditTime(0)` use `asyncScheduler`, so the output waits for a macrotask (after rendering may have happened). `debounceTime(0, asapScheduler)` or `observeOn(asapScheduler)` with a debounce waits only for a microtask, so the result is ready before the browser paints. For UI state, the microtask version avoids a frame with stale data.

## 340: How do you drive smooth animations with RxJS?

Use `animationFrames()` or `interval(0, animationFrameScheduler)` so updates line up with the browser's paint. Compute positions from the elapsed time, not from the frame count, so the animation speed doesn't depend on frame rate. Stop with `takeWhile` or `takeUntil`, and do the DOM writes in the subscriber.

```ts
const tween = (ms: number) =>
  animationFrames().pipe(
    map(({ elapsed }) => Math.min(elapsed / ms, 1)),
    takeWhile((t) => t < 1, true),
  );

tween(500).subscribe((t) => (el.style.opacity = String(t)));
```

## 341: What are the problems with a global event bus built on a Subject?

Anyone can push anything, so it's hard to find who sends what, types are often loose, and the order of events becomes hard to reason about. Subscribers often forget to unsubscribe, and a single subscriber throwing used to break others in old versions. A bus also hides dependencies between features. Prefer explicit services with typed Observables, or a state library with defined actions, and keep any bus small and typed.

## 342: How do effects and component streams split the work in a well-designed app?

Component streams should be about view state: combine inputs, route params and store selections, and map them to what the template needs. Effects (or service methods) should own side effects: HTTP, storage, sockets, navigation. Components send intents (actions or method calls), effects react and update state, and components read the new state. This keeps async logic testable and out of templates.

## 343: How would you design a real-time dashboard stream?

Open one shared socket with `share` and reconnect with `retry` and backoff. Start with an HTTP snapshot, then apply updates from the socket, dropping updates older than the snapshot. Throttle the rendering with `auditTime` or `sampleTime` so 100 updates per second don't mean 100 renders. Pause when the tab is hidden, and use `refCount` so the socket closes when nobody is looking.

## 344: How do you build a request queue with priorities?

RxJS has no priority queue operator. Keep a sorted queue outside, and use a trigger stream that pulls the next item when a slot is free. A simple version uses a Subject for "slot free" events and `mergeMap` with a concurrency limit for the actual calls.

```ts
const queue: { priority: number; run: () => Observable<unknown> }[] = [];
const kick$ = new Subject<void>();

kick$
  .pipe(
    filter(() => queue.length > 0),
    map(() => queue.sort((a, b) => b.priority - a.priority).shift()!),
    mergeMap((job) => job.run().pipe(finalize(() => kick$.next())), 3),
  )
  .subscribe();

function enqueue(job: (typeof queue)[number]) {
  queue.push(job);
  kick$.next();
}
```

## 345: How do you implement stale-while-revalidate with RxJS?

Emit the cached value right away if there is one, fetch in the background, emit the fresh value when it comes back, and update the cache.

```ts
function swr<T>(key: string, fetch$: Observable<T>): Observable<T> {
  return defer(() => {
    const cached = cache.get(key) as T | undefined;
    const fresh$ = fetch$.pipe(tap((v) => cache.set(key, v)));
    return cached !== undefined ? concat(of(cached), fresh$) : fresh$;
  });
}
```

Add `distinctUntilChanged` with a deep compare if you don't want to emit when the fresh value equals the cached one.

## 346: How do you implement undo and redo with scan?

Keep a state with `past`, `present` and `future`, and handle three kinds of actions in `scan`.

```ts
type Cmd<T> = { type: "set"; value: T } | { type: "undo" } | { type: "redo" };
interface History<T> {
  past: T[];
  present: T;
  future: T[];
}

const history = <T>(initial: T) =>
  scan<Cmd<T>, History<T>>(
    (h, cmd) => {
      if (cmd.type === "set")
        return { past: [...h.past, h.present], present: cmd.value, future: [] };
      if (cmd.type === "undo" && h.past.length)
        return {
          past: h.past.slice(0, -1),
          present: h.past[h.past.length - 1],
          future: [h.present, ...h.future],
        };
      if (cmd.type === "redo" && h.future.length)
        return {
          past: [...h.past, h.present],
          present: h.future[0],
          future: h.future.slice(1),
        };
      return h;
    },
    { past: [], present: initial, future: [] },
  );

const text$ = commands$.pipe(
  history(""),
  map((h) => h.present),
);
```

Cap the `past` array length if the history can get long.

## 347: How would you implement a simple circuit breaker as an operator?

Count failures across subscriptions. When there are too many in a row, fail fast without calling the source for a cooldown period, then let one request through to test the service.

```ts
function circuitBreaker<T>(maxFailures = 3, cooldownMs = 10_000) {
  let failures = 0;
  let openUntil = 0;

  return (source: Observable<T>) =>
    defer(() => {
      if (Date.now() < openUntil)
        return throwError(() => new Error("Circuit open"));
      return source.pipe(
        tap({ next: () => (failures = 0) }),
        catchError((err) => {
          if (++failures >= maxFailures) openUntil = Date.now() + cooldownMs;
          return throwError(() => err);
        }),
      );
    });
}

const guarded = circuitBreaker<Data>();
const data$ = http.get<Data>("/api/data").pipe(guarded);
```

The state lives in the closure, so create the operator once and reuse it for all calls to the same service.

## 348: How do you implement a token bucket rate limiter?

Refill tokens on an interval and let a request through only when a token is available. With RxJS, you can model the tokens as a stream and `zip` each request with a token, so requests wait until one is free.

```ts
const perSecond = 5;
const tokens$ = timer(0, 1000 / perSecond);

const limited$ = zip(requests$, tokens$).pipe(
  mergeMap(([req]) => api.send(req)),
);
```

This version keeps buffering tokens while there are no requests, which allows bursts later. Real token buckets cap the number of saved tokens, so for strict limits keep a counter in a closure and a queue, or use a small library.

## 349: What happens if a switchMap inner Observable emits synchronously?

The value goes through right away, during the `switchMap` call. If the inner Observable is a Subject or something that triggers another outer value synchronously, you get reentrancy: the next outer value arrives while `switchMap` is still subscribing to the previous inner one. RxJS handles the unsubscribe correctly, but your side effects may run in a surprising order. Keeping inner Observables free of synchronous side effects on shared Subjects avoids this.

## 350: How do you avoid a stack overflow with recursive synchronous Observables?

Deep recursion through synchronous Observables (for example `expand` that returns `of(...)` a hundred thousand times) keeps growing the call stack until it overflows. Make each step start from a fresh stack by making it async, for example with `observeOn(asapScheduler)` on the inner Observable. The `scheduler` argument of `expand` used to be the way to do this, but it is deprecated in RxJS 7.

```ts
of(0).pipe(
  expand((n) =>
    n < 100_000 ? of(n + 1).pipe(observeOn(asapScheduler)) : EMPTY,
  ),
  last(),
);
```

## 351: Why can a Subject with many subscribers get slow?

Every `next` copies the observers array and calls each observer one after another, all synchronously. With thousands of subscribers (one per table row, for example) and frequent values, that is a lot of work per emission. Better designs subscribe once and fan out data in plain code (or through one `map` that builds a lookup), or let rows read from a shared signal or store instead of each having its own subscription.

## 352: When would you choose plain callbacks or Promises over RxJS?

For a single async value with no need to cancel, `async/await` is simpler and everyone on the team can read it. For one simple event listener, `addEventListener` is fine. RxJS starts paying off when you have several async sources, timing (debounce, throttle, timeout), cancellation, retries or long-lived streams. Pulling in RxJS for one HTTP call adds a concept the team must learn without much gain.

## 353: What is UnsubscriptionError?

When you unsubscribe, RxJS runs all teardown functions. If one or more of them throw, RxJS keeps running the others and then throws a single `UnsubscriptionError` that has an `errors` array with every error. Teardown should not throw, so seeing this error usually means a cleanup function is calling into something that was already destroyed.

## 354: Is it safe to unsubscribe from inside a next callback?

Yes. Calling `subscription.unsubscribe()` inside your own `next` callback marks the subscriber as closed and tears down the source, even if the source is still in the middle of emitting. The problem is getting the reference: with a synchronous source, `subscribe` hasn't returned yet, so the variable is still undefined. Operators like `take`, `takeWhile` and `first` are the safer way to stop from the inside.

## 355: What happens with takeUntil if the notifier completes without emitting?

Nothing. In RxJS 7, only a `next` from the notifier stops the source; a notifier that completes silently is ignored, and the source keeps going. A common bug is using an `EMPTY`-like notifier or a destroy Subject that is completed without calling `next()` first. That's why the old pattern was `destroy$.next(); destroy$.complete();`.

## 356: What happens if the takeUntil notifier emits synchronously on subscribe?

`takeUntil` subscribes to the notifier before it subscribes to the source. If the notifier emits right away (like a `BehaviorSubject` or `of(true)`), the output completes immediately and the source is never subscribed. That is useful as a "stop if already cancelled" check, but surprising when someone passes a `BehaviorSubject(false)` as the notifier.

## 357: What is the "Zalgo" problem and how does it apply to Observables?

"Releasing Zalgo" means an API that is sometimes synchronous and sometimes asynchronous, so code after the call can't know whether the callback already ran. Observables can do this: a cached `of(value)` emits synchronously while a fresh `http.get` emits later. Code that sets state after `subscribe` may run before or after the value arrives. Either make the behavior always async (for example `observeOn(asapScheduler)`) or write code that doesn't depend on the timing.

## 358: What ordering does merge give with synchronous sources?

`merge` subscribes to its sources one by one, in order. If they are synchronous, each one emits all its values before the next one is even subscribed, so `merge(of(1, 2), of(3, 4))` gives `1, 2, 3, 4`, the same as `concat`. Interleaving only happens with async sources. Tests that use synchronous mocks can hide ordering bugs that show up with real async data.

## 359: Why can concat lose values from a hot source?

`concat` subscribes to the second source only after the first completes. If the second source is hot, like a Subject or DOM events, any values it emitted while the first was still running are gone. If you need them, buffer the hot source with a `ReplaySubject`, `shareReplay`, or subscribe to it with `merge` from the start and handle ordering yourself.

## 360: If one subscriber of a Subject throws, do other subscribers still get the value?

Yes, in RxJS 7. The error thrown in one observer's `next` is caught and reported as an unhandled error asynchronously, and the loop continues to the other observers. That subscriber is not closed by the throw, either. In older versions with synchronous error handling, a throw could break delivery to the rest, which is one reason the behavior was changed.

## 361: How do you test a service that exposes a hot Subject-based stream?

In a marble test, replace the Subject's source with a `hot()` Observable, or call `next` on the Subject from scheduled work. The easiest is to inject a fake source, since the service then just pipes it.

```ts
testScheduler.run(({ hot, expectObservable }) => {
  const actions$ = hot("-a--b-a|", { a: "inc", b: "dec" });
  const service = new CounterService(actions$);
  expectObservable(service.count$).toBe("-x--y-x|", { x: 1, y: 0 });
});
```

Designing services so their input streams are injectable is what makes them easy to test like this.

## 362: How do you test a polling stream with TestScheduler?

Mock the API to return a `cold()` Observable, then use time progression to check that requests happen at the right times. `expectSubscriptions` on the cold mock shows each poll.

```ts
testScheduler.run(({ cold, expectObservable }) => {
  const api = { load: () => cold("--r|", { r: "data" }) };
  const poll$ = timer(0, 10).pipe(
    switchMap(() => api.load()),
    take(3),
  );
  expectObservable(poll$).toBe("--r 9ms r 9ms (r|)", { r: "data" });
});
```

The first request starts at frame 0 and emits at 2, the second starts at 10 and emits at 12, and the third emits at 22 and `take(3)` completes.

## 363: How do you test retry with a delay using marbles?

Use a cold Observable that errors, and check that the subscriptions happen at the expected times.

```ts
testScheduler.run(({ cold, expectObservable, expectSubscriptions }) => {
  const source = cold("--#");
  const result$ = source.pipe(retry({ count: 2, delay: 5 }));

  expectObservable(result$).toBe("16ms #");
  expectSubscriptions(source.subscriptions).toBe([
    "^-!",
    "-------^-!",
    "--------------^-!",
  ]);
});
```

Each attempt errors at frame 2 of its own timeline, and the next one subscribes 5 frames after the error: attempts start at 0, 7 and 14, so the final error comes at frame 16.

## 364: What are common pitfalls in marble tests?

- Forgetting that each character, including `|` and the parentheses in a group, takes time: `(ab)` takes 4 frames.
- Mixing up `hot` and `cold`, so the timing is off by the subscription point.
- Using real Promises or `Date.now()` in the code under test.
- Writing marbles outside `run()`, where one frame is 10 virtual ms and time-based operators need the scheduler passed in.
- Comparing objects with values that have functions or class instances that `toEqual` doesn't compare the way you expect.

## 365: How do you write a custom operator that handles errors thrown by user callbacks?

Wrap calls to user code in `try/catch` and forward the error to `subscriber.error`, so a throwing callback behaves like a source error. Also forward `error` and `complete` from the source, and return the source subscription for teardown.

```ts
function mapDefined<T, R>(fn: (v: T) => R | undefined): OperatorFunction<T, R> {
  return (source) =>
    new Observable<R>((subscriber) =>
      source.subscribe({
        next: (value) => {
          let result: R | undefined;
          try {
            result = fn(value);
          } catch (err) {
            subscriber.error(err);
            return;
          }
          if (result !== undefined) subscriber.next(result);
        },
        error: (err) => subscriber.error(err),
        complete: () => subscriber.complete(),
      }),
    );
}
```

## 366: Why can state inside a custom operator leak between subscribers?

If you declare a variable in the operator factory but outside the returned function's subscribe logic, every subscription shares it. Two subscribers would then share one counter or cache. Put per-subscription state inside `new Observable` or inside `defer`.

```ts
// Shared by all subscribers, which is usually a bug:
function countBad<T>() {
  let n = 0;
  return map((v: T) => ({ v, n: n++ }));
}

// One counter per subscription:
function countGood<T>(): OperatorFunction<T, { v: T; n: number }> {
  return (source) =>
    defer(() => {
      let n = 0;
      return source.pipe(map((v) => ({ v, n: n++ })));
    });
}
```

## 367: How would you implement switchMap yourself?

Keep a reference to the current inner subscription. On each outer value, unsubscribe the old one and subscribe to the new inner Observable. Complete only when the outer has completed and there is no active inner.

```ts
function mySwitchMap<T, R>(
  project: (v: T) => ObservableInput<R>,
): OperatorFunction<T, R> {
  return (source) =>
    new Observable<R>((subscriber) => {
      let inner: Subscription | null = null;
      let outerDone = false;

      const outer = source.subscribe({
        next: (value) => {
          inner?.unsubscribe();
          inner = from(project(value)).subscribe({
            next: (v) => subscriber.next(v),
            error: (err) => subscriber.error(err),
            complete: () => {
              inner = null;
              if (outerDone) subscriber.complete();
            },
          });
        },
        error: (err) => subscriber.error(err),
        complete: () => {
          outerDone = true;
          if (!inner) subscriber.complete();
        },
      });

      return () => {
        outer.unsubscribe();
        inner?.unsubscribe();
      };
    });
}
```

The real one also handles errors thrown by `project` and passes the index.

## 368: How do you show a loading indicator only if a request takes longer than 300ms?

Race the request against a timer. If the timer wins, emit a "loading" state and keep going; if the request wins, never show the spinner. A neat way is to merge a delayed loading flag that is cut off by the result.

```ts
const result$ = request$.pipe(share());

const view$ = merge(
  timer(300).pipe(
    map(() => ({ loading: true }) as const),
    takeUntil(result$),
  ),
  result$.pipe(map((data) => ({ loading: false, data }) as const)),
);
```

`share` makes both branches use the same request.

## 369: How do you keep a spinner visible for a minimum time to avoid flicker?

Once the spinner is shown, wait for both the result and a minimum timer before hiding it. `combineLatest` with a timer works for this.

```ts
const withMinDuration =
  <T>(ms: number) =>
  (source: Observable<T>) =>
    combineLatest([source, timer(ms)]).pipe(map(([value]) => value));
```

Combined with the 300ms delay trick, you get the common "show after 300ms, then keep for at least 500ms" behavior.

## 370: How do you run requests in parallel but emit results in the original order?

Start them all in parallel and then concatenate them in order. Since `concat` subscribes one by one, share each request first so it already started.

```ts
const ordered$ = defer(() => {
  const started = ids.map((id) => api.get(id).pipe(shareReplay(1)));
  started.forEach((obs$) => obs$.subscribe({ error: () => {} }));
  return concat(...started);
});
```

For a limited concurrency, keep `mergeMap` with an index, buffer results that arrive early, and emit them when the next expected index is ready. If you just need all results at the end, `forkJoin` already keeps order.

## 371: How do RxJS subscriptions affect Angular SSR?

During server rendering Angular waits for the app to become stable before it serializes the HTML. Pending HTTP calls and timers keep it unstable. A never-ending `interval` or a polling stream started on the server can delay or block the render until a timeout. Start such streams only in the browser, for example in `afterNextRender`, or check the platform, and keep server work to requests that complete.

## 372: What is pendingUntilEvent in Angular?

`pendingUntilEvent()` is an operator from `@angular/core/rxjs-interop` that marks the app as having pending work until the Observable emits, completes, errors or is unsubscribed. During SSR, Angular then waits for that stream before it considers the app stable. It is useful for async work that Angular doesn't track on its own, like a custom data source that should finish before the HTML is sent.

## 373: What are outputFromObservable and outputToObservable?

They connect component outputs and RxJS. `outputFromObservable(obs$)` creates a component output that emits whenever the Observable emits, so a component can expose a stream as an output without a manual `EventEmitter`. `outputToObservable(ref.output)` turns an output into an Observable you can pipe, which is handy when working with component refs in code.

## 374: How is rxResource different from toSignal?

`toSignal` subscribes once and gives you the latest value. `rxResource` from `@angular/core/rxjs-interop` takes reactive params (from signals) and a stream function that returns an Observable. Whenever the params change, it unsubscribes from the old Observable and starts a new one, like `switchMap`, and it gives you `value`, `status`, `error` and `isLoading` signals. It's a better fit for "load data based on these inputs" than wiring `toObservable`, `switchMap` and `toSignal` by hand.

```ts
userId = input.required<string>();

user = rxResource({
  params: () => ({ id: this.userId() }),
  stream: ({ params }) => this.http.get<User>(`/api/users/${params.id}`),
});
```

## 375: Why are signals glitch-free while RxJS is not?

Signals use push-pull: a change only marks dependents as dirty, and values are computed when read, after all sources have updated. So a `computed` never sees half-updated inputs. RxJS is pure push: each change is pushed down immediately, through each path separately, so combined streams can see in-between states. This is why derived UI state often fits signals better, while RxJS fits event flows.

## 376: When you migrate a BehaviorSubject service to signals, what should stay in RxJS?

State and derived values (`BehaviorSubject` plus `map` and `distinctUntilChanged`) map well to `signal` and `computed`. Keep RxJS for the parts that deal with time and async flows: debounced inputs, request cancellation, retries, polling, WebSockets and complex event combinations. Connect the two with `toSignal`, `toObservable` and `rxResource`, and avoid converting back and forth many times in the same flow.

## 377: What goes wrong when an app has more than one copy of RxJS?

Different packages may bring their own RxJS version, especially in micro-frontends or with mismatched peer dependencies. Then an Observable from one copy is not an `instanceof Observable` of the other, `instanceof Subject` checks fail, and TypeScript types from different copies may not match. RxJS uses duck typing in `from` and `isObservable`, so streams still mostly work together, but bundle size grows. Keep one version, share it as a singleton in module federation, and use `npm ls rxjs` to find duplicates.

## 378: How do you keep RxJS bundle cost low?

Import from `rxjs` and let tree shaking drop what you don't use. Avoid importing `rxjs/ajax` or `rxjs/webSocket` if you use `fetch` or Angular's `HttpClient` already. Check bundle analyzers for duplicate RxJS copies. Most apps only pay for the dozen operators they use, which is small, so duplicate versions are usually the bigger problem.

## 379: How do you process a Node.js stream of jobs with limited concurrency?

Turn the source into an Observable, process each job with `mergeMap` and a concurrency limit, and handle errors per job so one failure doesn't stop the rest.

```ts
from(createReadStream("jobs.ndjson").pipe(split2()))
  .pipe(
    map((line) => JSON.parse(line as string) as Job),
    mergeMap(
      (job) =>
        defer(() => runJob(job)).pipe(
          retry({ count: 2, delay: 1000 }),
          catchError((err) => {
            logger.error({ job, err });
            return EMPTY;
          }),
        ),
      10,
    ),
  )
  .subscribe({ complete: () => logger.info("all jobs done") });
```

Here `split2` is a small npm package that splits a stream into lines. Note that the file stream keeps reading even when the workers are busy, so lines can pile up in memory.

## 380: How do you acknowledge queue messages only after processing?

Process each message in order with `concatMap` (or `mergeMap` with a limit if order doesn't matter), and send the ack after the inner work succeeds. On error, nack or move the message to a dead-letter queue inside `catchError`, so the consumer stream keeps running.

```ts
messages$.pipe(
  concatMap((msg) =>
    defer(() => handle(msg.body)).pipe(
      tap(() => msg.ack()),
      catchError((err) => {
        msg.nack();
        logger.error(err);
        return EMPTY;
      }),
    ),
  ),
);
```

## 381: How do you shut down a Node.js service built on RxJS gracefully?

Create a `shutdown$` stream from `SIGTERM` and `SIGINT`, stop taking new input with `takeUntil(shutdown$)` on the source (before the processing step), and let in-flight work finish. Then wait for the pipeline to complete before exiting.

```ts
const shutdown$ = merge(
  fromEvent(process, "SIGTERM"),
  fromEvent(process, "SIGINT"),
).pipe(take(1));

const done = lastValueFrom(
  incoming$.pipe(
    takeUntil(shutdown$),
    mergeMap((job) => handleJob$(job), 5),
  ),
  { defaultValue: undefined },
);

done.then(() => process.exit(0));
```

Here `takeUntil` is intentionally before `mergeMap`: it stops new jobs but lets running ones complete.

## 382: What are the trade-offs between Observables and async generators?

Async generators are pull-based, built into the language, work with `for await`, and give natural backpressure, but they handle one consumer at a time and have no operators for time (debounce, throttle) or easy cancellation of in-flight work. Observables are push-based, can be multicast, have a big operator library and clean cancellation, but no built-in backpressure. Use generators for data you read at your own pace and Observables for events and UI flows.

## 383: Why does RxJS not have a dedicated "state" type?

RxJS models streams, and state is just "the latest value of a stream". `BehaviorSubject` and `shareReplay(1)` are the tools for that, but they are general stream tools with some sharp edges: an error kills a `BehaviorSubject`, derived streams are cold, and combining has glitches. This gap is part of why libraries like NgRx and Angular signals exist on top of or next to RxJS.

## 384: How do you protect a BehaviorSubject store from errors?

Never call `error` on it, and never subscribe it directly to another stream (that would forward errors and completion). Put async work outside the store and catch errors there, writing an error field into state instead. If you expose `update` methods, wrap user reducers in `try/catch` so a bug in one reducer doesn't throw through `next` into unrelated code.

## 385: Should a library return Observables or Promises?

Return Promises for single async results when most users write `async/await` and cancellation isn't needed. Return Observables when the API produces many values over time, needs cancellation, or is used inside apps that are already reactive, like Angular libraries. Some libraries offer both, or accept an `AbortSignal` with Promises. Forcing RxJS on users who don't use it adds a dependency and a learning cost.

## 386: How do you write an API that accepts either a value or an Observable?

Accept `T | Observable<T>` (or `ObservableInput<T>`), and normalize at the start with `isObservable` and `of`, or with `from` for any `ObservableInput`.

```ts
function toObs<T>(input: T | Observable<T>): Observable<T> {
  return isObservable(input) ? input : of(input);
}

function watchTitle(title: string | Observable<string>) {
  return toObs(title).pipe(map((t) => `${t} | My App`));
}
```

## 387: How do you expose cancellation from a function that uses RxJS internally but returns a Promise?

Accept an `AbortSignal` and use it to stop the stream, then convert to a Promise. When the signal aborts, the stream errors with an abort error so the Promise rejects.

```ts
function loadAll(signal?: AbortSignal): Promise<Item[]> {
  const abort$ = signal
    ? fromEvent(signal, "abort").pipe(
        mergeMap(() =>
          throwError(() => new DOMException("Aborted", "AbortError")),
        ),
      )
    : NEVER;

  return lastValueFrom(merge(pages$.pipe(toArray()), abort$).pipe(take(1)));
}
```

## 388: Why are RxJS stack traces hard to read, and what helps?

Errors pass through many internal subscriber frames, and with async sources the stack starts at a timer or event callback instead of your code. Helpful steps: add labeled `tap` logs near the problem, wrap errors with context in `catchError` (for example `new Error('loading orders failed', { cause: err })`), use source maps with "blackbox" or ignore-list settings in DevTools to hide `node_modules/rxjs` frames, and keep pipelines small and named so the operator in the stack trace tells you where you are.

## 389: How do you avoid many separate subscriptions in an Angular template?

Each `async` pipe is its own subscription. Ten `| async` on related streams means ten subscriptions and ten change detection triggers. Combine them into one view model stream with `combineLatest` and read it once, or convert the streams to signals with `toSignal` (or use `computed` on top), so the template reads values directly.

```ts
vm$ = combineLatest({ user: this.user$, cart: this.cart$, flags: this.flags$ });
```

```html
@if (vm$ | async; as vm) {
<app-header [user]="vm.user" [count]="vm.cart.length" />
}
```

## 390: How do you keep heavy work in map from freezing the UI?

All operators run on the main thread. If a `map` sorts 100,000 items on every keystroke, the UI freezes. Debounce the input first, move heavy work to a Web Worker and wrap the worker reply in an Observable, or split work into chunks scheduled with `asyncScheduler` so the browser can paint between chunks. `switchMap` to the worker call so old work is dropped when input changes.

## 391: How do you split a large synchronous job into chunks?

Break the data into batches and process each batch in its own macrotask, so the browser can handle events between batches.

```ts
const processInChunks = <T, R>(
  items: T[],
  size: number,
  fn: (batch: T[]) => R[],
) =>
  from(items).pipe(
    bufferCount(size),
    concatMap((batch) => timer(0).pipe(map(() => fn(batch)))),
    scan((all, part) => all.concat(part), [] as R[]),
  );
```

Each emission is the progress so far, which lets you show partial results.

## 392: Why does interval drift, and how do you build an accurate clock?

`interval` is built on `setInterval`, which only promises to wait at least the given time. Under load or in background tabs, ticks can be late or merged, so counting ticks drifts from real time. For clocks and countdowns, compute the displayed value from timestamps, like `Date.now() - start`, and use the interval only as a trigger to re-render.

```ts
const start = Date.now();
const elapsedSec$ = interval(250).pipe(
  map(() => Math.floor((Date.now() - start) / 1000)),
  distinctUntilChanged(),
);
```

## 393: How do background tabs affect RxJS timers?

Browsers throttle timers in hidden tabs, often to once per second or less, and `requestAnimationFrame` stops completely. So `interval(100)` may tick once a second, and `animationFrames()` pauses. Polling becomes slow, and animations jump when the tab comes back. Design streams to tolerate this: compute from timestamps, react to `visibilitychange`, and don't rely on exact tick counts.

## 394: How do you make a countdown correct even if the user's clock is wrong?

Get the server's time once along with the deadline, compute the offset between server and client clocks, and use it in every calculation. Then the countdown matches the server even if the device clock is off.

```ts
const countdown$ = (deadline: number, serverNow: number) => {
  const offset = serverNow - Date.now();
  return interval(500).pipe(
    startWith(0),
    map(() => Math.max(0, deadline - (Date.now() + offset))),
    takeWhile((left) => left > 0, true),
  );
};
```

## 395: Why must retried requests be idempotent?

`retry` resubscribes, which sends the request again. If the first try actually reached the server and only the response got lost, a retried `POST` might create a duplicate order or charge twice. Only retry automatically when the operation is safe to repeat (`GET`, `PUT` of the same state, `DELETE`), or send an idempotency key so the server can drop duplicates.

## 396: What is a retry storm and how do you prevent it?

When a server goes down, every client retries at the same moments, and when it comes back it gets hit by a wave of requests that knocks it down again. Prevent it with exponential backoff, random jitter on each delay, a cap on the number of retries, and by sharing one retry across all parts of the app that need the same data (for example with `shareReplay`) instead of having each component retry on its own. A circuit breaker on the client also helps.

## 397: How do you make sure a payment is submitted only once?

Use several layers. `exhaustMap` on the submit stream ignores clicks while a request is running. Disable the button from a `submitting` state as a visible hint. Send an idempotency key created once per payment attempt, so the server drops duplicates even if the client retries or the user refreshes. Never use `switchMap` here, since cancelling on the client does not cancel the charge.

```ts
submit$.pipe(
  exhaustMap(() => {
    const key = crypto.randomUUID();
    return api.pay(order, { headers: { "Idempotency-Key": key } }).pipe(
      retry({ count: 2, delay: 1000 }), // same key on every retry
    );
  }),
);
```

## 398: How do you stop navigation until pending saves finish?

Track pending saves in a counter or a `BehaviorSubject`, and use a `canDeactivate` guard that returns an Observable which waits until the count is zero, with a timeout so the user isn't stuck.

```ts
export const waitForSaves: CanDeactivateFn<unknown> = () =>
  inject(SaveTracker).pending$.pipe(
    filter((n) => n === 0),
    take(1),
    map(() => true),
    timeout({
      first: 5000,
      with: () => of(confirm("Changes are still saving. Leave anyway?")),
    }),
  );
```

## 399: How do you combine an initial HTTP snapshot with WebSocket updates without missing any?

Subscribe to the socket first and buffer its messages, then load the snapshot, then apply buffered and new updates that are newer than the snapshot. If you load the snapshot first, updates sent between the response and the socket subscription are lost.

```ts
const updates$ = socket$.pipe(shareReplay({ bufferSize: 100, refCount: true }));

const state$ = defer(() => {
  const keepOpen = updates$.subscribe(); // connect now so updates are buffered
  return api.snapshot().pipe(
    switchMap((snap) =>
      updates$.pipe(
        filter((u) => u.version > snap.version),
        scan((s, u) => applyUpdate(s, u), snap),
        startWith(snap),
      ),
    ),
    finalize(() => keepOpen.unsubscribe()),
  );
});
```

`shareReplay` keeps the last 100 updates, so the ones that arrived while the snapshot was loading are replayed when the inner subscription starts.

In practice it's simpler if the server supports "send me updates since version N", so you connect after the snapshot and ask for what you missed.

## 400: How do you drop stale updates when events can arrive out of order?

Give every event a version or sequence number and keep the highest one seen. Drop anything lower or equal. `scan` can keep the last version along with the state.

```ts
const latest$ = updates$.pipe(
  scan((acc, u) => (u.version > acc.version ? u : acc), {
    version: -1,
  } as Update),
  distinctUntilChanged(),
);
```

## 401: How do you use mergeMap but ignore responses from old requests?

Tag each request with an increasing id, and only accept a response if its id is the latest one sent. Unlike `switchMap`, the old requests still finish (useful when you can't cancel them, or want their side effects), but they can't overwrite newer results.

```ts
let latestId = 0;

const results$ = query$.pipe(
  mergeMap((q) => {
    const id = ++latestId;
    return api.search(q).pipe(map((data) => ({ id, data })));
  }),
  filter(({ id }) => id === latestId),
  map(({ data }) => data),
);
```

## 402: What can go wrong with optimistic updates when edits overlap?

If the user changes the same item twice quickly and the first request fails, rolling back to the state before the first edit also throws away the second edit. Roll back by undoing only that change (apply the inverse) rather than restoring a full snapshot, or queue writes per item with `concatMap` so they apply in order, and reload from the server after a failure to get the true state.

## 403: How would you build an offline queue for writes?

Store each write in a persistent queue (IndexedDB or `localStorage`) when the user makes it. A stream that starts when the app is online pulls items from the queue, sends them one by one with `concatMap`, and removes each one after the server confirms. On failure, stop and wait for the next `online` event or a backoff timer. Writes should be idempotent, since a write may be sent again after a crash.

```ts
const flush$ = online$.pipe(
  filter(Boolean),
  exhaustMap(() =>
    from(queue.readAll()).pipe(
      concatMap((items) => from(items)),
      concatMap((item) =>
        api.send(item).pipe(tap(() => queue.remove(item.id))),
      ),
      catchError(() => EMPTY), // try again next time we are online
    ),
  ),
);
```

## 404: A search box sometimes shows results for an older query. How do you debug it?

That is almost always out-of-order responses. Check which flattening operator is used: `mergeMap` or `concatMap` with a slow first request lets old results arrive last. Add `tap` logs with the query and a timestamp before and after the request to confirm. The fix is `switchMap` (or the request id approach), plus `distinctUntilChanged` so the same query isn't sent twice.

## 405: Memory keeps growing on a dashboard page that stays open for hours. What do you check?

Look for: `ReplaySubject` or `shareReplay` with no buffer limit, `scan` that keeps appending to an array forever, `groupBy` and `distinct` with no limit on keys, inner subscriptions created in `mergeMap` that never complete (like a socket per widget), and subscriptions created on each refresh but never closed. Take heap snapshots a few minutes apart and compare which objects grow, then cap buffers and make sure every long stream has an end.

## 406: The network tab shows the same request twice. What are the usual causes?

Two subscribers to the same cold Observable: two `async` pipes, a `subscribe` in code plus an `async` pipe, or a `combineLatest` that includes the same source twice. Another cause is a `retry` firing because of an error you didn't notice, or a `BehaviorSubject` trigger plus `startWith` both causing an initial load. Fix it by sharing with `shareReplay`, reading the stream once, or converting it to a signal.

## 407: A stream works once and then stops reacting after one failed request. Why?

The error reached the outer chain, which ended the whole stream, and `catchError` (if any) replaced it with a completed fallback. Move `catchError` inside the `switchMap` (or `mergeMap`, `concatMap`, `exhaustMap`), so only the inner request ends and the outer stream keeps listening.

## 408: combineLatest never emits. How do you find out why?

One of the inputs hasn't emitted yet. Add `tap` with a label to each input to see which one is silent. Typical culprits are a plain `Subject` that nobody has pushed to yet, `valueChanges` without `startWith`, or a filter that dropped every value. Give the silent input an initial value, or rethink whether `withLatestFrom` fits better.

## 409: A Jest test with debounceTime times out. What is happening?

The code waits for a real 300ms timer, and either the test finishes first or the test uses fake timers that nobody advanced. Fix it by using the `TestScheduler` in run mode, by advancing fake timers (`jest.advanceTimersByTime(300)` or Vitest's equivalent), or by using Angular's `fakeAsync` and `tick`. Also make sure the test waits for completion, for example by awaiting `firstValueFrom`.

## 410: A service pushes a value into a Subject in its constructor, but components never see it. Why?

A plain `Subject` doesn't keep values, and the components subscribe after the constructor ran. The value is gone by then. Use a `BehaviorSubject` or `ReplaySubject(1)`, or make the value part of a cold stream that runs on subscribe, for example with `defer` and `shareReplay`.

## 411: Why does a BehaviorSubject cause ExpressionChangedAfterItHasBeenChecked errors in Angular?

During a change detection pass, a child or a lifecycle hook calls `next` on a `BehaviorSubject` that the parent template already read in the same pass. In development mode Angular checks the bindings twice, sees the value changed, and throws. Fix the data flow so the value is set before the view is checked (for example in the parent, or in a service before render), avoid pushing state from `ngAfterViewInit`, or move the state to signals, which Angular handles in its scheduling.

## 412: forkJoin on two form valueChanges streams never emits. Why?

`forkJoin` waits for every source to complete, and `valueChanges` never completes. The same is true for store selectors, Subjects, router events and `interval`. Use `combineLatest` for streams that keep emitting, or add `take(1)` (or `first()`) to each source if you just want one value from each.

## 413: await lastValueFrom(store.select(...)) hangs. Why?

`lastValueFrom` waits for completion, and a store selection never completes. Use `firstValueFrom` to get the current value, which unsubscribes after the first emission. If the value may not be ready yet, add a `filter` for the ready state before it.

## 414: Users report that some of their edits were not saved. The code uses switchMap for saves. What happened?

Each new edit unsubscribed from the previous save. On the client, those requests were aborted; on the server, some were processed and some were not, depending on timing. The UI also never got their responses. Use `concatMap` so every save runs in order, or debounce first and use `concatMap` so you send fewer but complete saves.

## 415: How do you show toast notifications one at a time?

Push toasts into a Subject, then `concatMap` each one to a stream that shows it, waits, and hides it. New toasts wait in the queue until the current one is gone.

```ts
const toasts$ = new Subject<string>();

toasts$
  .pipe(
    concatMap((text) =>
      concat(
        of({ text, visible: true }),
        timer(3000).pipe(map(() => ({ text, visible: false }))),
        timer(300).pipe(ignoreElements()), // gap for the hide animation
      ),
    ),
  )
  .subscribe(renderToast);
```

## 416: In a chat app, messages sometimes appear twice or out of order. How do you fix it with RxJS?

Messages come from two paths: the optimistic local message and the server echo through the socket, plus history loaded over HTTP. Give every message a client-generated id, merge all sources, and keep a map of messages by id in `scan`, so the echo replaces the local one instead of adding a copy. Sort by server timestamp or sequence number when rendering, not by arrival order.

```ts
const messages$ = merge(local$, socket$, history$).pipe(
  scan(
    (byId, msg) =>
      new Map(byId).set(msg.clientId, { ...byId.get(msg.clientId), ...msg }),
    new Map<string, Msg>(),
  ),
  map((byId) => [...byId.values()].sort((a, b) => a.seq - b.seq)),
);
```

## 417: An autocomplete hits the API's rate limit. What would you change?

Increase `debounceTime`, add `distinctUntilChanged`, require a minimum term length with `filter`, and keep `switchMap` so stale requests are cancelled. Cache results per term (a `Map` of `shareReplay` streams) so going back to a term doesn't call the API again. If the API returns 429, back off with `retry` and its `Retry-After` header instead of hammering it.

## 418: How do you migrate nested callback code to RxJS step by step?

Wrap each callback API in an Observable first (`bindNodeCallback`, `fromEventPattern` or `new Observable`), without changing the logic. Then replace each level of nesting with a flattening operator, picking `concatMap`, `switchMap` or `mergeMap` based on what the old code did when new input arrived. Move error handling into `catchError` and cleanup into teardown or `finalize`. Keep the old tests running at each step.

## 419: How would you design a file upload queue with progress, cancel and retry?

Model each upload as its own Observable that emits progress events and completes on success. Run them through `mergeMap` with a concurrency limit. Give each upload a cancel Subject and use `takeUntil` on it. Retry each upload separately with backoff, and keep the per-file state (`queued`, `uploading`, `done`, `failed`, percent) in `scan` keyed by file id.

```ts
const uploads$ = files$.pipe(
  mergeMap(
    (file) =>
      uploadWithProgress(file).pipe(
        retry({ count: 2, delay: 2000 }),
        map((pct) => ({ id: file.id, status: "uploading" as const, pct })),
        endWith({ id: file.id, status: "done" as const, pct: 100 }),
        takeUntil(cancel$.pipe(filter((id) => id === file.id))),
        catchError(() =>
          of({ id: file.id, status: "failed" as const, pct: 0 }),
        ),
        startWith({ id: file.id, status: "queued" as const, pct: 0 }),
      ),
    3,
  ),
  scan((byId, s) => ({ ...byId, [s.id]: s }), {} as Record<string, FileState>),
);
```

`startWith` is applied when the inner stream is subscribed, which is when it gets a slot, so you'd add files to the state as `queued` when they are picked, separately, if you want them visible earlier.

## 420: A stock ticker sends hundreds of updates per second and the page lags. How do you fix it?

Don't render every update. Keep the latest price per symbol with `scan` into a map, and render at most once per frame with `auditTime(0, animationFrameScheduler)` or `sampleTime(100)`. Run the socket handling outside the Angular zone if you use zone.js, and update only the rows that changed (track by symbol) instead of re-rendering the whole table.

```ts
const view$ = ticks$.pipe(
  scan((prices, t) => prices.set(t.symbol, t.price), new Map<string, number>()),
  auditTime(0, animationFrameScheduler),
);
```

Note that this `scan` mutates one `Map`, so use `map(m => new Map(m))` after `auditTime` if the consumer needs a new reference to detect changes.

## 421: How do you respect a 429 response with a Retry-After header?

Read the header in the `delay` function of `retry` and wait that long. The header can be seconds or an HTTP date, so handle both, and fall back to a default.

```ts
retry({
  count: 5,
  delay: (err) => {
    if (!(err instanceof HttpErrorResponse) || err.status !== 429)
      return throwError(() => err);
    const header = err.headers.get("Retry-After") ?? "";
    const seconds = Number(header);
    const ms =
      Number.isFinite(seconds) && header !== ""
        ? seconds * 1000
        : Date.parse(header) - Date.now();
    return timer(ms > 0 ? ms : 1000);
  },
});
```

## 422: Many requests fail with 401 at the same time. How do you refresh the token only once?

Keep the in-progress refresh as a shared Observable. The first 401 starts it, and later ones subscribe to the same one. Clear it when it finishes so a later expiry starts a new refresh.

```ts
@Injectable({ providedIn: "root" })
export class AuthService {
  private http = inject(HttpClient);
  readonly token = signal<string>("");
  private refreshing$: Observable<string> | null = null;

  refreshToken(): Observable<string> {
    this.refreshing$ ??= this.http
      .post<{ token: string }>("/api/refresh", {})
      .pipe(
        map((r) => r.token),
        tap((t) => this.token.set(t)),
        finalize(() => (this.refreshing$ = null)),
        shareReplay(1),
      );
    return this.refreshing$;
  }
}
```

## 423: How do you write an Angular interceptor that refreshes the token and retries the request?

Catch 401 errors, call the shared refresh, then retry the original request with the new token. Skip the refresh endpoint itself so a failed refresh doesn't loop.

```ts
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  const withToken = (t: string) =>
    req.clone({ setHeaders: { Authorization: `Bearer ${t}` } });

  return next(withToken(auth.token())).pipe(
    catchError((err) => {
      if (
        err instanceof HttpErrorResponse &&
        err.status === 401 &&
        !req.url.endsWith("/api/refresh")
      ) {
        return auth.refreshToken().pipe(switchMap((t) => next(withToken(t))));
      }
      return throwError(() => err);
    }),
  );
};
```

## 424: How do you cancel all pending requests when the user logs out?

Expose a `logout$` stream from the auth service and add `takeUntil(logout$)` in an HTTP interceptor. Every request still in flight is unsubscribed (and aborted) when the user logs out, so late responses can't write the old user's data into the new session.

```ts
export const cancelOnLogout: HttpInterceptorFn = (req, next) =>
  next(req).pipe(takeUntil(inject(AuthService).logout$));
```

Also reset stores and shared caches (`shareReplay` streams) on logout, since they hold the old user's data.

## 425: toSignal with requireSync throws an error. Why?

`requireSync: true` tells Angular the Observable emits during `subscribe`. If it doesn't (for example an HTTP call, or a `ReplaySubject` with nothing in it yet), `toSignal` throws right away. Either use a source that really emits synchronously, like a `BehaviorSubject` or a stream with `startWith`, or drop `requireSync` and pass `initialValue`.

## 426: How do you build dependent dropdowns, like country and then city?

Use the country value to `switchMap` to the cities request. Reset the city field when the country changes, and start with an empty list so the UI is never stuck with the old cities.

```ts
cities$ = this.form.controls.country.valueChanges.pipe(
  tap(() => this.form.controls.city.reset()),
  switchMap((country) =>
    country ? this.api.cities(country).pipe(startWith([])) : of([]),
  ),
);
```

## 427: How do you search several providers and show results as they arrive?

Start all requests with `merge`, let each one fail on its own with `catchError`, and accumulate results with `scan`. Results appear as soon as any provider answers. Wrap it in `switchMap` so a new query cancels all of them.

```ts
const results$ = query$.pipe(
  switchMap((q) =>
    merge(
      ...providers.map((p) =>
        p.search(q).pipe(
          map((items) => ({ provider: p.name, items })),
          catchError(() => of({ provider: p.name, items: [] })),
        ),
      ),
    ).pipe(scan((all, r) => [...all, ...r.items], [] as Item[])),
  ),
);
```

## 428: How do you show a "new items available" banner instead of updating the list right away?

Keep two streams: the list the user sees, which only changes when they click, and the latest data from the server. Compare them to decide whether to show the banner.

```ts
const latest$ = timer(0, 30_000).pipe(
  switchMap(() => api.feed()),
  shareReplay({ bufferSize: 1, refCount: true }),
);
const shown$ = showNew$.pipe(
  startWith(null),
  switchMap(() => latest$.pipe(take(1))),
);

const hasNew$ = combineLatest([latest$, shown$]).pipe(
  map(([latest, shown]) => latest[0]?.id !== shown[0]?.id),
);
```

## 429: How do you load configuration once at startup in Angular using an Observable?

Use `provideAppInitializer` and return a Promise from `firstValueFrom`, so Angular waits for the config before bootstrapping. Store it in a service and read it synchronously afterwards.

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    provideAppInitializer(() => {
      const config = inject(ConfigService);
      return firstValueFrom(
        inject(HttpClient).get<Config>("/config.json"),
      ).then((c) => config.set(c));
    }),
  ],
};
```

## 430: How do you wrap Server-Sent Events (EventSource) in an Observable?

Create the `EventSource` in `new Observable`, forward messages, and close it in teardown. `EventSource` reconnects by itself on network errors, so only treat it as an error when it is fully closed.

```ts
const sse$ = <T>(url: string) =>
  new Observable<T>((subscriber) => {
    const es = new EventSource(url);
    es.onmessage = (e) => subscriber.next(JSON.parse(e.data));
    es.onerror = () => {
      if (es.readyState === EventSource.CLOSED)
        subscriber.error(new Error("SSE connection closed"));
    };
    return () => es.close();
  });
```

## 431: How do you show progress for a long server job with RxJS?

Start the job with a POST, then either poll the job status with `timer` and `switchMap` until it is done, or open an SSE or WebSocket stream for progress events. In both cases, map to a progress state, stop with `takeWhile(..., true)`, and use `takeUntil` on a cancel button that also calls a cancel endpoint, since closing the stream won't stop the job on the server.

## 432: How do you sync state across browser tabs?

`BroadcastChannel` is an `EventTarget`, so `fromEvent` works on it. Post changes to the channel and merge incoming messages into your local state stream. The `storage` event on `window` is an older option that works through `localStorage`.

```ts
const channel = new BroadcastChannel("cart");
const remote$ = fromEvent<MessageEvent<Cart>>(channel, "message").pipe(
  map((e) => e.data),
);

const cart$ = merge(
  localChanges$.pipe(tap((c) => channel.postMessage(c))),
  remote$,
);
```

## 433: How do you batch outgoing changes in a collaborative editor?

Collect changes for a short time with `bufferTime`, drop empty batches, and send batches in order with `concatMap`, so the server sees them in the same order the user made them.

```ts
changes$.pipe(
  bufferTime(200),
  filter((batch) => batch.length > 0),
  concatMap((batch) => api.sendChanges(batch)),
);
```

If the server is slow, batches queue up in `concatMap`, so you might merge waiting batches before sending.

## 434: How do you switch implementation at runtime based on a feature flag stream?

`switchMap` from the flag to one of the implementations. When the flag changes, the old implementation is unsubscribed and the new one starts.

```ts
const prices$ = flags$.pipe(
  map((f) => f.newPricing),
  distinctUntilChanged(),
  switchMap((useNew) => (useNew ? newPricing.stream() : oldPricing.stream())),
);
```

## 435: Each row in a big list polls its own status. How do you make it cheaper?

Hundreds of timers and requests are wasteful. Use one shared timer, collect the ids of visible rows, send one batch request per tick, and let each row select its own entry from the shared result.

```ts
const statuses$ = timer(0, 5000).pipe(
  withLatestFrom(visibleIds$),
  switchMap(([, ids]) => (ids.length ? api.statuses(ids) : of({}))),
  shareReplay({ bufferSize: 1, refCount: true }),
);

const rowStatus$ = (id: string) =>
  statuses$.pipe(
    map((all) => all[id]),
    distinctUntilChanged(),
  );
```

## 436: How do you skip a request when inputs are invalid, and should you use filter or switchMap to EMPTY?

`filter` drops invalid values before `switchMap`, so the previous request (and its old results) keeps running and stays on screen. `switchMap` returning `EMPTY` (or `of([])`) for invalid input cancels the running request and lets you clear the results. Pick based on what the UI should show when the input becomes invalid.

```ts
term$.pipe(switchMap((t) => (t.length < 2 ? of([]) : api.search(t))));
```

## 437: How do you implement debounce with a maximum wait?

`debounceTime` can delay forever if events never stop. To force an emission at least every `maxWait` ms, use `debounce` with a duration that shrinks as the burst gets older.

```ts
function debounceMaxWait<T>(
  wait: number,
  maxWait: number,
): MonoTypeOperatorFunction<T> {
  return (source) =>
    defer(() => {
      let burstStart: number | null = null;
      return source.pipe(
        debounce(() => {
          const now = Date.now();
          burstStart ??= now;
          return timer(
            Math.min(wait, Math.max(0, maxWait - (now - burstStart))),
          );
        }),
        tap(() => (burstStart = null)),
      );
    });
}
```

`defer` gives each subscriber its own `burstStart`. For marble tests, swap `Date.now()` for `asyncScheduler.now()`.

## 438: How do you buffer values until a condition is true and then flush them?

Use `bufferToggle` or `buffer` with a stream that emits when the condition turns true. For example, hold analytics events while offline and send them when back online.

```ts
const flushOnline$ = online$.pipe(filter(Boolean));

const sent$ = events$.pipe(
  buffer(
    merge(flushOnline$, timer(0, 10_000).pipe(filter(() => navigator.onLine))),
  ),
  filter((batch) => batch.length > 0),
  concatMap((batch) => api.track(batch)),
);
```

## 439: How do you make RxJS code easy to test?

Inject inputs instead of creating them inside: pass sources, APIs and schedulers (or rely on run mode for schedulers) through the constructor or function parameters. Keep logic in pure functions and operators that return Observables, and subscribe only at the edge. Then tests can pass `cold()` and `hot()` streams and check the output with marbles, without a real network or real time.

## 440: How do you share the current user with many components without many requests?

Load it once in a service and expose a shared stream (or a signal). Late subscribers get the cached value.

```ts
@Injectable({ providedIn: "root" })
export class CurrentUser {
  private http = inject(HttpClient);
  readonly user$ = this.http.get<User>("/api/me").pipe(shareReplay(1));
  readonly user = toSignal(this.user$);
}
```

Here `shareReplay(1)` without `refCount` is fine because the request completes, and you want the cache to survive when no component is subscribed. Reset it on logout.

## 441: What does it cost to convert between signals and Observables many times?

Each `toObservable` creates an effect, and each `toSignal` creates a subscription and a signal. Going back and forth inside a component tree adds async hops (`toObservable` emits after the effect runs), makes timing harder to follow and can cause extra change detection. Keep each piece of logic in one world: do the async flow in RxJS and convert once at the end, or keep state in signals and only drop into RxJS for the part that needs time operators.

## 442: How do you design a typed action stream with an ofType helper?

Use a discriminated union for actions and write a filter that narrows by the `type` field.

```ts
type Action =
  | { type: "load" }
  | { type: "loaded"; items: Item[] }
  | { type: "failed"; error: string };

const ofType = <K extends Action["type"]>(...types: K[]) =>
  filter((a: Action): a is Extract<Action, { type: K }> =>
    types.includes(a.type as K),
  );

actions$.pipe(ofType("loaded")).subscribe((a) => console.log(a.items)); // a is typed
```

## 443: How do you keep side effects out of pure derived streams?

Write derived streams (`map`, `filter`, `combineLatest`, `scan`) without side effects, so it doesn't matter how many times they run or who subscribes. Put side effects (HTTP, storage, analytics) in dedicated effect streams that are subscribed once. If a `tap` in a derived stream writes data, every extra subscriber runs it again, which leads to duplicate writes that are hard to track down.

## 444: What happens if you call subscribe inside a pipe operator callback?

You create a subscription that the outer stream doesn't know about. It isn't cancelled when the outer stream unsubscribes, its errors aren't passed down, and it may still be running after the component is gone. If you need the inner values, return the inner Observable from a flattening operator. If you just need a side effect, still use a flattening operator, so it stays cancellable.

## 445: How do you keep a long-lived stream healthy over days of uptime?

Make sure every buffer and cache has a limit, inner streams complete, reconnects use backoff, errors are caught inside so the outer stream never ends, and the stream exposes health signals (last message time, reconnect count). Add a watchdog with `timeout({ each: 60_000 })` on the socket stream to force a reconnect if it goes silent. Log subscription starts and ends in production at a low level, so you can see leaks.

## 446: How do you add a watchdog that reconnects a silent WebSocket?

Put `timeout` on the socket stream and `retry` after it. If no message arrives within the limit, `timeout` errors, `retry` resubscribes, and `webSocket` opens a new connection.

```ts
const live$ = webSocket<Msg>(url).pipe(
  timeout({ each: 30_000 }),
  retry({
    delay: (_e, n) => timer(Math.min(30_000, 1000 * 2 ** n)),
    resetOnSuccess: true,
  }),
  share(),
);
```

The server should send heartbeat messages so a quiet but healthy channel doesn't trigger a reconnect.

## 447: What do you check in an RxJS code review?

- Every subscription has a clear end (`async`, `toSignal`, `takeUntilDestroyed`, `take`, completion).
- No nested `subscribe` calls.
- The flattening operator fits the case, and `switchMap` isn't used for writes.
- `catchError` sits inside the flattening operator for long-lived streams.
- `takeUntil` is last, after operators that create inner subscriptions.
- `shareReplay` has `refCount: true` for sources that don't complete.
- Buffers and caches have limits.
- No deprecated APIs (`toPromise`, `throwError(value)`, positional `subscribe` callbacks, `multicast`).

## 448: Is RxJS still worth learning now that Angular has signals?

Yes. Signals replace RxJS for synchronous state in Angular, but they have no built-in way to debounce, cancel, retry or combine async events. Angular's HTTP client, router and forms still expose Observables, and NgRx effects and many libraries are built on RxJS. Outside Angular, RxJS is still used for complex event flows in many apps. What has changed is that you need it for fewer things, mainly async flows, not all state.

## 449: What is the future of RxJS?

RxJS 7.8 is the current stable release and gets fixes, while the next major version is published as a beta under the `next` npm tag. The team has been removing deprecated APIs, trimming size, and following the native Observable work on the web platform, which has shipped in Chromium-based browsers. If native Observables spread to all browsers, RxJS is likely to become more of an operator library on top of them. Code written with RxJS 7's non-deprecated APIs is the safest base for whatever comes next.

## 450: How would you introduce RxJS to a team that is new to it?

Start with the few ideas that matter most: Observables are lazy, subscriptions must end, and the four flattening operators differ in what happens on a new value. Teach a short list of operators first (`map`, `filter`, `tap`, `switchMap`, `concatMap`, `exhaustMap`, `catchError`, `debounceTime`, `distinctUntilChanged`, `shareReplay`, `takeUntilDestroyed`). Add lint rules for common mistakes, use marble diagrams in code reviews to explain timing, and keep pipelines short and named. Use plain Promises or signals where RxJS doesn't add value.
