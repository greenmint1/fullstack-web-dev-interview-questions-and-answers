# Angular Interview Questions and Answers

_Last updated: October 28, 2026_

450 Angular interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers use modern Angular (v20, v21 and later): standalone components, signals, the built-in control flow (`@if`, `@for`, `@switch`, `@defer`), `inject()`, zoneless change detection, `httpResource`, the new SSR APIs and signal forms. Older APIs (NgModules, `@Input()`, `*ngIf`, Zone.js) are mentioned where they still matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Angular?](#1-what-is-angular)
- [2: What is the difference between AngularJS and Angular?](#2-what-is-the-difference-between-angularjs-and-angular)
- [3: How often is Angular released and how long is a version supported?](#3-how-often-is-angular-released-and-how-long-is-a-version-supported)
- [4: Why does Angular use TypeScript?](#4-why-does-angular-use-typescript)
- [5: How do you install the Angular CLI and create a new project?](#5-how-do-you-install-the-angular-cli-and-create-a-new-project)
- [6: What is the Angular CLI?](#6-what-is-the-angular-cli)
- [7: What are the main files in a new Angular project?](#7-what-are-the-main-files-in-a-new-angular-project)
- [8: What is a component?](#8-what-is-a-component)
- [9: How do you generate a component with the CLI?](#9-how-do-you-generate-a-component-with-the-cli)
- [10: What are the main properties of the @Component decorator?](#10-what-are-the-main-properties-of-the-component-decorator)
- [11: What is a standalone component?](#11-what-is-a-standalone-component)
- [12: Are components standalone by default?](#12-are-components-standalone-by-default)
- [13: What is a template?](#13-what-is-a-template)
- [14: What is the difference between an inline template and an external template?](#14-what-is-the-difference-between-an-inline-template-and-an-external-template)
- [15: What is data binding and what types exist in Angular?](#15-what-is-data-binding-and-what-types-exist-in-angular)
- [16: What is interpolation?](#16-what-is-interpolation)
- [17: What is property binding?](#17-what-is-property-binding)
- [18: What is event binding?](#18-what-is-event-binding)
- [19: What is two-way binding?](#19-what-is-two-way-binding)
- [20: What is attribute binding and when do you need it?](#20-what-is-attribute-binding-and-when-do-you-need-it)
- [21: How does class binding work?](#21-how-does-class-binding-work)
- [22: How does style binding work?](#22-how-does-style-binding-work)
- [23: What is a directive and what types of directives exist?](#23-what-is-a-directive-and-what-types-of-directives-exist)
- [24: What is the difference between a component and a directive?](#24-what-is-the-difference-between-a-component-and-a-directive)
- [25: How does the @if block work?](#25-how-does-the-if-block-work)
- [26: How does the @for block work?](#26-how-does-the-for-block-work)
- [27: What implicit variables are available inside @for?](#27-what-implicit-variables-are-available-inside-for)
- [28: What is the @empty block?](#28-what-is-the-empty-block)
- [29: How does the @switch block work?](#29-how-does-the-switch-block-work)
- [30: What happened to *ngIf, *ngFor and \*ngSwitch?](#30-what-happened-to-ngif-ngfor-and-ngswitch)
- [31: What is ng-template?](#31-what-is-ng-template)
- [32: What is ng-container?](#32-what-is-ng-container)
- [33: What is @let in templates?](#33-what-is-let-in-templates)
- [34: What is a template reference variable?](#34-what-is-a-template-reference-variable)
- [35: What is a pipe?](#35-what-is-a-pipe)
- [36: What built-in pipes does Angular have?](#36-what-built-in-pipes-does-angular-have)
- [37: How do you pass parameters to a pipe and chain pipes?](#37-how-do-you-pass-parameters-to-a-pipe-and-chain-pipes)
- [38: How do you create a custom pipe?](#38-how-do-you-create-a-custom-pipe)
- [39: What is the async pipe?](#39-what-is-the-async-pipe)
- [40: What is a service?](#40-what-is-a-service)
- [41: How do you create a service with the CLI?](#41-how-do-you-create-a-service-with-the-cli)
- [42: What is dependency injection?](#42-what-is-dependency-injection)
- [43: What does providedIn: 'root' mean?](#43-what-does-providedin-root-mean)
- [44: What is the inject() function?](#44-what-is-the-inject-function)
- [45: What is the difference between constructor injection and inject()?](#45-what-is-the-difference-between-constructor-injection-and-inject)
- [46: What is an NgModule and do you still need it?](#46-what-is-an-ngmodule-and-do-you-still-need-it)
- [47: What does main.ts do?](#47-what-does-maints-do)
- [48: What is app.config.ts?](#48-what-is-appconfigts)
- [49: What is the root component?](#49-what-is-the-root-component)
- [50: What are lifecycle hooks?](#50-what-are-lifecycle-hooks)
- [51: What is the difference between the constructor and ngOnInit?](#51-what-is-the-difference-between-the-constructor-and-ngoninit)
- [52: What is ngOnDestroy used for?](#52-what-is-ngondestroy-used-for)
- [53: What is ngOnChanges?](#53-what-is-ngonchanges)
- [54: What is a signal?](#54-what-is-a-signal)
- [55: How do you read and change a signal?](#55-how-do-you-read-and-change-a-signal)
- [56: What is computed()?](#56-what-is-computed)
- [57: What is effect()?](#57-what-is-effect)
- [58: What is input()?](#58-what-is-input)
- [59: How do you make an input required?](#59-how-do-you-make-an-input-required)
- [60: What is output()?](#60-what-is-output)
- [61: How does a parent component pass data to a child?](#61-how-does-a-parent-component-pass-data-to-a-child)
- [62: How does a child component send data to a parent?](#62-how-does-a-child-component-send-data-to-a-parent)
- [63: What is model()?](#63-what-is-model)
- [64: Are @Input() and @Output() decorators still supported?](#64-are-input-and-output-decorators-still-supported)
- [65: How do you give an input or output a different public name?](#65-how-do-you-give-an-input-or-output-a-different-public-name)
- [66: What is routing in Angular?](#66-what-is-routing-in-angular)
- [67: How do you define routes?](#67-how-do-you-define-routes)
- [68: What is router-outlet?](#68-what-is-router-outlet)
- [69: What is routerLink?](#69-what-is-routerlink)
- [70: What is routerLinkActive?](#70-what-is-routerlinkactive)
- [71: How do you navigate from code?](#71-how-do-you-navigate-from-code)
- [72: How do you read route parameters?](#72-how-do-you-read-route-parameters)
- [73: How do you read query parameters?](#73-how-do-you-read-query-parameters)
- [74: How do you create a "page not found" route?](#74-how-do-you-create-a-page-not-found-route)
- [75: How do redirects and pathMatch work?](#75-how-do-redirects-and-pathmatch-work)
- [76: What are child routes?](#76-what-are-child-routes)
- [77: What is lazy loading?](#77-what-is-lazy-loading)
- [78: What is HttpClient?](#78-what-is-httpclient)
- [79: How do you set up HttpClient?](#79-how-do-you-set-up-httpclient)
- [80: How do you make a GET request?](#80-how-do-you-make-a-get-request)
- [81: How do you make POST, PUT and DELETE requests?](#81-how-do-you-make-post-put-and-delete-requests)
- [82: What is an Observable?](#82-what-is-an-observable)
- [83: What is the difference between an Observable and a Promise?](#83-what-is-the-difference-between-an-observable-and-a-promise)
- [84: What is RxJS?](#84-what-is-rxjs)
- [85: Do you need to unsubscribe from Observables?](#85-do-you-need-to-unsubscribe-from-observables)
- [86: What kinds of forms does Angular support?](#86-what-kinds-of-forms-does-angular-support)
- [87: What is a template-driven form?](#87-what-is-a-template-driven-form)
- [88: What is ngModel?](#88-what-is-ngmodel)
- [89: What is a reactive form?](#89-what-is-a-reactive-form)
- [90: What is a FormControl?](#90-what-is-a-formcontrol)
- [91: What is a FormGroup?](#91-what-is-a-formgroup)
- [92: What is FormBuilder?](#92-what-is-formbuilder)
- [93: What built-in validators are there?](#93-what-built-in-validators-are-there)
- [94: How do you show validation errors in the template?](#94-how-do-you-show-validation-errors-in-the-template)
- [95: What are the states of a form control?](#95-what-are-the-states-of-a-form-control)
- [96: What are signal forms?](#96-what-are-signal-forms)
- [97: What is view encapsulation?](#97-what-is-view-encapsulation)
- [98: What is the :host selector?](#98-what-is-the-host-selector)
- [99: How do you add global styles?](#99-how-do-you-add-global-styles)
- [100: What is content projection?](#100-what-is-content-projection)
- [101: How do you project content into multiple slots?](#101-how-do-you-project-content-into-multiple-slots)
- [102: What is change detection?](#102-what-is-change-detection)
- [103: What is Zone.js?](#103-what-is-zonejs)
- [104: What is zoneless change detection?](#104-what-is-zoneless-change-detection)
- [105: What is AOT compilation?](#105-what-is-aot-compilation)
- [106: What is the difference between JIT and AOT?](#106-what-is-the-difference-between-jit-and-aot)
- [107: What is Ivy?](#107-what-is-ivy)
- [108: What is angular.json?](#108-what-is-angularjson)
- [109: What are the most common Angular CLI commands?](#109-what-are-the-most-common-angular-cli-commands)
- [110: What does ng serve do?](#110-what-does-ng-serve-do)
- [111: What does ng build do?](#111-what-does-ng-build-do)
- [112: How do you use environment files?](#112-how-do-you-use-environment-files)
- [113: What does ng add do?](#113-what-does-ng-add-do)
- [114: What does ng update do?](#114-what-does-ng-update-do)
- [115: What are decorators in Angular?](#115-what-are-decorators-in-angular)
- [116: What kinds of selectors can a component or directive have?](#116-what-kinds-of-selectors-can-a-component-or-directive-have)
- [117: How do you use one component inside another?](#117-how-do-you-use-one-component-inside-another)
- [118: What can go in a standalone component's imports array?](#118-what-can-go-in-a-standalone-components-imports-array)
- [119: What is the host element?](#119-what-is-the-host-element)
- [120: What is the safe navigation operator?](#120-what-is-the-safe-navigation-operator)
- [121: What is the non-null assertion operator in templates?](#121-what-is-the-non-null-assertion-operator-in-templates)
- [122: What can you write in a template expression?](#122-what-can-you-write-in-a-template-expression)
- [123: What is $event?](#123-what-is-event)
- [124: How do you listen to a specific key?](#124-how-do-you-listen-to-a-specific-key)
- [125: How do you create a custom attribute directive?](#125-how-do-you-create-a-custom-attribute-directive)
- [126: What is a structural directive?](#126-what-is-a-structural-directive)
- [127: Should you use NgClass or class bindings?](#127-should-you-use-ngclass-or-class-bindings)
- [128: Should you use NgStyle or style bindings?](#128-should-you-use-ngstyle-or-style-bindings)
- [129: How do you show a numbered list of items?](#129-how-do-you-show-a-numbered-list-of-items)
- [130: How do you add a class only when a condition is true?](#130-how-do-you-add-a-class-only-when-a-condition-is-true)
- [131: How do you handle form submission?](#131-how-do-you-handle-form-submission)
- [132: Where do you put static files like images and fonts?](#132-where-do-you-put-static-files-like-images-and-fonts)
- [133: What is NgOptimizedImage?](#133-what-is-ngoptimizedimage)
- [134: What is a single-page application (SPA)?](#134-what-is-a-single-page-application-spa)
- [135: What is a route guard?](#135-what-is-a-route-guard)
- [136: What is a route resolver?](#136-what-is-a-route-resolver)
- [137: What is index.html in an Angular app?](#137-what-is-indexhtml-in-an-angular-app)
- [138: How do you run unit tests in Angular?](#138-how-do-you-run-unit-tests-in-angular)
- [139: What is a spec file?](#139-what-is-a-spec-file)
- [140: What are declarations, imports, exports and providers in an NgModule?](#140-what-are-declarations-imports-exports-and-providers-in-an-ngmodule)
- [141: What is Angular DevTools?](#141-what-is-angular-devtools)
- [142: What is the difference between interpolation and property binding?](#142-what-is-the-difference-between-interpolation-and-property-binding)
- [143: Where should you load data in a component?](#143-where-should-you-load-data-in-a-component)
- [144: How do you set the page title?](#144-how-do-you-set-the-page-title)
- [145: What is the difference between path-based and hash-based URLs?](#145-what-is-the-difference-between-path-based-and-hash-based-urls)
- [146: What is the json pipe used for?](#146-what-is-the-json-pipe-used-for)
- [147: How do you format dates with the date pipe?](#147-how-do-you-format-dates-with-the-date-pipe)
- [148: How do you give an input a default value?](#148-how-do-you-give-an-input-a-default-value)
- [149: What is the @defer block?](#149-what-is-the-defer-block)
- [150: What are Angular Material and the CDK?](#150-what-are-angular-material-and-the-cdk)

### Moderate Questions (151-300)

- [151: How does a signal decide that its value has changed?](#151-how-does-a-signal-decide-that-its-value-has-changed)
- [152: What is untracked()?](#152-what-is-untracked)
- [153: How do you run cleanup code in an effect?](#153-how-do-you-run-cleanup-code-in-an-effect)
- [154: When should you avoid effect()?](#154-when-should-you-avoid-effect)
- [155: What is linkedSignal()?](#155-what-is-linkedsignal)
- [156: What is toSignal()?](#156-what-is-tosignal)
- [157: What is toObservable()?](#157-what-is-toobservable)
- [158: What is resource()?](#158-what-is-resource)
- [159: What is rxResource()?](#159-what-is-rxresource)
- [160: What is httpResource()?](#160-what-is-httpresource)
- [161: What are viewChild() and viewChildren()?](#161-what-are-viewchild-and-viewchildren)
- [162: What are contentChild() and contentChildren()?](#162-what-are-contentchild-and-contentchildren)
- [163: What are input transforms?](#163-what-are-input-transforms)
- [164: How do you expose a signal from a service as read-only?](#164-how-do-you-expose-a-signal-from-a-service-as-read-only)
- [165: How do you build a simple state service with signals?](#165-how-do-you-build-a-simple-state-service-with-signals)
- [166: When do you use computed(), linkedSignal() or effect()?](#166-when-do-you-use-computed-linkedsignal-or-effect)
- [167: What are outputFromObservable() and outputToObservable()?](#167-what-are-outputfromobservable-and-outputtoobservable)
- [168: How do you update nested objects or arrays inside a signal?](#168-how-do-you-update-nested-objects-or-arrays-inside-a-signal)
- [169: What is the OnPush change detection strategy?](#169-what-is-the-onpush-change-detection-strategy)
- [170: When is an OnPush component checked?](#170-when-is-an-onpush-component-checked)
- [171: What is the difference between markForCheck() and detectChanges()?](#171-what-is-the-difference-between-markforcheck-and-detectchanges)
- [172: What is the ExpressionChangedAfterItHasBeenCheckedError?](#172-what-is-the-expressionchangedafterithasbeencheckederror)
- [173: How do you switch an existing app to zoneless change detection?](#173-how-do-you-switch-an-existing-app-to-zoneless-change-detection)
- [174: What is NgZone.runOutsideAngular()?](#174-what-is-ngzonerunoutsideangular)
- [175: What are detach() and reattach()?](#175-what-are-detach-and-reattach)
- [176: How do signals work with OnPush?](#176-how-do-signals-work-with-onpush)
- [177: How do hierarchical injectors work?](#177-how-do-hierarchical-injectors-work)
- [178: What is the difference between providers and viewProviders?](#178-what-is-the-difference-between-providers-and-viewproviders)
- [179: What are useClass, useValue, useFactory and useExisting?](#179-what-are-useclass-usevalue-usefactory-and-useexisting)
- [180: What is an InjectionToken?](#180-what-is-an-injectiontoken)
- [181: What options can you pass to inject()?](#181-what-options-can-you-pass-to-inject)
- [182: What are multi providers?](#182-what-are-multi-providers)
- [183: Why would you provide a service at the component level?](#183-why-would-you-provide-a-service-at-the-component-level)
- [184: How do route-level providers work?](#184-how-do-route-level-providers-work)
- [185: What is an injection context?](#185-what-is-an-injection-context)
- [186: What is DestroyRef?](#186-what-is-destroyref)
- [187: What is takeUntilDestroyed()?](#187-what-is-takeuntildestroyed)
- [188: What is provideAppInitializer()?](#188-what-is-provideappinitializer)
- [189: Why use an abstract class as a DI token?](#189-why-use-an-abstract-class-as-a-di-token)
- [190: What does NullInjectorError mean?](#190-what-does-nullinjectorerror-mean)
- [191: What is importProvidersFrom()?](#191-what-is-importprovidersfrom)
- [192: What is the difference between functional guards and class-based guards?](#192-what-is-the-difference-between-functional-guards-and-class-based-guards)
- [193: How do you warn the user about unsaved changes before leaving a page?](#193-how-do-you-warn-the-user-about-unsaved-changes-before-leaving-a-page)
- [194: What is canMatch?](#194-what-is-canmatch)
- [195: What is canActivateChild?](#195-what-is-canactivatechild)
- [196: How do you handle errors in a resolver?](#196-how-do-you-handle-errors-in-a-resolver)
- [197: How do you pass static data to a route?](#197-how-do-you-pass-static-data-to-a-route)
- [198: What are preloading strategies?](#198-what-are-preloading-strategies)
- [199: How do you lazy load a group of routes?](#199-how-do-you-lazy-load-a-group-of-routes)
- [200: What are named outlets?](#200-what-are-named-outlets)
- [201: How do you show a loading bar during navigation?](#201-how-do-you-show-a-loading-bar-during-navigation)
- [202: Can redirectTo be a function?](#202-can-redirectto-be-a-function)
- [203: What can a guard return?](#203-what-can-a-guard-return)
- [204: How do you restore scroll position and support anchor links?](#204-how-do-you-restore-scroll-position-and-support-anchor-links)
- [205: What are view transitions in the router?](#205-what-are-view-transitions-in-the-router)
- [206: How do you navigate relative to the current route?](#206-how-do-you-navigate-relative-to-the-current-route)
- [207: What is an HTTP interceptor and how do you write one?](#207-what-is-an-http-interceptor-and-how-do-you-write-one)
- [208: How do you handle HTTP errors?](#208-how-do-you-handle-http-errors)
- [209: How do you retry a failed HTTP request?](#209-how-do-you-retry-a-failed-http-request)
- [210: How do you use HttpParams and HttpHeaders?](#210-how-do-you-use-httpparams-and-httpheaders)
- [211: What is HttpContext?](#211-what-is-httpcontext)
- [212: What does withFetch() do?](#212-what-does-withfetch-do)
- [213: How do you get the full HTTP response, not just the body?](#213-how-do-you-get-the-full-http-response-not-just-the-body)
- [214: How do you track upload progress?](#214-how-do-you-track-upload-progress)
- [215: How do you cancel an HTTP request?](#215-how-do-you-cancel-an-http-request)
- [216: How does Angular protect against XSRF/CSRF?](#216-how-does-angular-protect-against-xsrfcsrf)
- [217: How do you show a global loading indicator for HTTP requests?](#217-how-do-you-show-a-global-loading-indicator-for-http-requests)
- [218: What is the difference between switchMap, mergeMap, concatMap and exhaustMap?](#218-what-is-the-difference-between-switchmap-mergemap-concatmap-and-exhaustmap)
- [219: What types of Subjects are there?](#219-what-types-of-subjects-are-there)
- [220: Should you use BehaviorSubject or signals for state in services?](#220-should-you-use-behaviorsubject-or-signals-for-state-in-services)
- [221: What does shareReplay do?](#221-what-does-sharereplay-do)
- [222: How do you build a search box that waits for the user to stop typing?](#222-how-do-you-build-a-search-box-that-waits-for-the-user-to-stop-typing)
- [223: What is the difference between combineLatest, forkJoin and zip?](#223-what-is-the-difference-between-combinelatest-forkjoin-and-zip)
- [224: What is the difference between hot and cold Observables?](#224-what-is-the-difference-between-hot-and-cold-observables)
- [225: When should you use signals and when RxJS?](#225-when-should-you-use-signals-and-when-rxjs)
- [226: How do you write a custom validator for reactive forms?](#226-how-do-you-write-a-custom-validator-for-reactive-forms)
- [227: How do you write an async validator?](#227-how-do-you-write-an-async-validator)
- [228: How do you validate two fields together, like password and confirm password?](#228-how-do-you-validate-two-fields-together-like-password-and-confirm-password)
- [229: How do you use FormArray for dynamic fields?](#229-how-do-you-use-formarray-for-dynamic-fields)
- [230: What are typed reactive forms?](#230-what-are-typed-reactive-forms)
- [231: What does nonNullable do on a form control?](#231-what-does-nonnullable-do-on-a-form-control)
- [232: What is FormRecord?](#232-what-is-formrecord)
- [233: What is the difference between setValue() and patchValue()?](#233-what-is-the-difference-between-setvalue-and-patchvalue)
- [234: How do you react to form value and status changes?](#234-how-do-you-react-to-form-value-and-status-changes)
- [235: What is updateOn in forms?](#235-what-is-updateon-in-forms)
- [236: What is ControlValueAccessor?](#236-what-is-controlvalueaccessor)
- [237: How do you disable a reactive form control?](#237-how-do-you-disable-a-reactive-form-control)
- [238: When do you choose template-driven forms vs reactive forms?](#238-when-do-you-choose-template-driven-forms-vs-reactive-forms)
- [239: How do you validate and submit with signal forms?](#239-how-do-you-validate-and-submit-with-signal-forms)
- [240: How do you show all validation errors when the user clicks submit?](#240-how-do-you-show-all-validation-errors-when-the-user-clicks-submit)
- [241: How do you use ngTemplateOutlet with a context?](#241-how-do-you-use-ngtemplateoutlet-with-a-context)
- [242: How do you create a component dynamically?](#242-how-do-you-create-a-component-dynamically)
- [243: What is NgComponentOutlet?](#243-what-is-ngcomponentoutlet)
- [244: What is the host property and how is it different from @HostBinding and @HostListener?](#244-what-is-the-host-property-and-how-is-it-different-from-hostbinding-and-hostlistener)
- [245: How do you access the DOM safely with ElementRef and Renderer2?](#245-how-do-you-access-the-dom-safely-with-elementref-and-renderer2)
- [246: In what order do parent and child lifecycle hooks run?](#246-in-what-order-do-parent-and-child-lifecycle-hooks-run)
- [247: When is a view query available?](#247-when-is-a-view-query-available)
- [248: What are afterNextRender() and afterEveryRender()?](#248-what-are-afternextrender-and-aftereveryrender)
- [249: How do components communicate through a service?](#249-how-do-components-communicate-through-a-service)
- [250: How do default content and ngProjectAs work with ng-content?](#250-how-do-default-content-and-ngprojectas-work-with-ng-content)
- [251: What triggers can @defer use?](#251-what-triggers-can-defer-use)
- [252: What is prefetching in @defer?](#252-what-is-prefetching-in-defer)
- [253: What are the rules for code to be lazy loaded with @defer?](#253-what-are-the-rules-for-code-to-be-lazy-loaded-with-defer)
- [254: What is the difference between pure and impure pipes?](#254-what-is-the-difference-between-pure-and-impure-pipes)
- [255: Why is calling a method in a template a problem?](#255-why-is-calling-a-method-in-a-template-a-problem)
- [256: How do you create a directive with inputs, outputs and exportAs?](#256-how-do-you-create-a-directive-with-inputs-outputs-and-exportas)
- [257: How do you write a custom structural directive?](#257-how-do-you-write-a-custom-structural-directive)
- [258: What are smart and presentational components?](#258-what-are-smart-and-presentational-components)
- [259: Why does track matter in @for?](#259-why-does-track-matter-in-for)
- [260: What is the read option in queries?](#260-what-is-the-read-option-in-queries)
- [261: How do you test a component that has inputs?](#261-how-do-you-test-a-component-that-has-inputs)
- [262: How do you test a service that uses HttpClient?](#262-how-do-you-test-a-service-that-uses-httpclient)
- [263: How do you mock a dependency in a test?](#263-how-do-you-mock-a-dependency-in-a-test)
- [264: What is the difference between fixture.detectChanges() and fixture.whenStable()?](#264-what-is-the-difference-between-fixturedetectchanges-and-fixturewhenstable)
- [265: How do you test routing?](#265-how-do-you-test-routing)
- [266: What are component harnesses?](#266-what-are-component-harnesses)
- [267: How do you test a service that uses signals?](#267-how-do-you-test-a-service-that-uses-signals)
- [268: What changed with Vitest becoming the default test runner?](#268-what-changed-with-vitest-becoming-the-default-test-runner)
- [269: How do you test an output?](#269-how-do-you-test-an-output)
- [270: How do you test a directive?](#270-how-do-you-test-a-directive)
- [271: What is the application builder?](#271-what-is-the-application-builder)
- [272: What are budgets in angular.json?](#272-what-are-budgets-in-angularjson)
- [273: How do you proxy API calls during development?](#273-how-do-you-proxy-api-calls-during-development)
- [274: How do you load configuration at runtime instead of at build time?](#274-how-do-you-load-configuration-at-runtime-instead-of-at-build-time)
- [275: How do you add linting to an Angular project?](#275-how-do-you-add-linting-to-an-angular-project)
- [276: What automatic migrations does Angular provide?](#276-what-automatic-migrations-does-angular-provide)
- [277: What is server-side rendering (SSR) and how do you add it?](#277-what-is-server-side-rendering-ssr-and-how-do-you-add-it)
- [278: What is hydration?](#278-what-is-hydration)
- [279: How do you safely use browser-only APIs in an SSR app?](#279-how-do-you-safely-use-browser-only-apis-in-an-ssr-app)
- [280: Why inject DOCUMENT instead of using the global document?](#280-why-inject-document-instead-of-using-the-global-document)
- [281: How does internationalization (i18n) work in Angular?](#281-how-does-internationalization-i18n-work-in-angular)
- [282: How do you animate elements entering and leaving the DOM?](#282-how-do-you-animate-elements-entering-and-leaving-the-dom)
- [283: What is the status of the @angular/animations package?](#283-what-is-the-status-of-the-angularanimations-package)
- [284: What are the more advanced options of NgOptimizedImage?](#284-what-are-the-more-advanced-options-of-ngoptimizedimage)
- [285: How does Angular protect against XSS?](#285-how-does-angular-protect-against-xss)
- [286: When is it OK to use DomSanitizer.bypassSecurityTrust?](#286-when-is-it-ok-to-use-domsanitizerbypasssecuritytrust)
- [287: How do you migrate an NgModule app to standalone?](#287-how-do-you-migrate-an-ngmodule-app-to-standalone)
- [288: What are Angular Elements?](#288-what-are-angular-elements)
- [289: How do you handle errors globally?](#289-how-do-you-handle-errors-globally)
- [290: How do you use a Content Security Policy with Angular?](#290-how-do-you-use-a-content-security-policy-with-angular)
- [291: How do you debug a production build?](#291-how-do-you-debug-a-production-build)
- [292: How do you deploy an Angular app?](#292-how-do-you-deploy-an-angular-app)
- [293: What are strict mode and strictTemplates?](#293-what-are-strict-mode-and-stricttemplates)
- [294: How do you set up path aliases for imports?](#294-how-do-you-set-up-path-aliases-for-imports)
- [295: What is virtual scrolling?](#295-what-is-virtual-scrolling)
- [296: How do you set meta tags for SEO?](#296-how-do-you-set-meta-tags-for-seo)
- [297: What does Angular offer for accessibility?](#297-what-does-angular-offer-for-accessibility)
- [298: How do you add drag and drop?](#298-how-do-you-add-drag-and-drop)
- [299: What is prerendering (static site generation)?](#299-what-is-prerendering-static-site-generation)
- [300: How do you create a library inside an Angular workspace?](#300-how-do-you-create-a-library-inside-an-angular-workspace)

### Advanced Questions (301-450)

- [301: How does Angular compile a component template?](#301-how-does-angular-compile-a-component-template)
- [302: What are LView and TView?](#302-what-are-lview-and-tview)
- [303: What is the locality principle in Ivy?](#303-what-is-the-locality-principle-in-ivy)
- [304: How does Angular type check templates?](#304-how-does-angular-type-check-templates)
- [305: How does change detection walk the component tree?](#305-how-does-change-detection-walk-the-component-tree)
- [306: How do signals make change detection more targeted?](#306-how-do-signals-make-change-detection-more-targeted)
- [307: How does the zoneless scheduler decide when to run change detection?](#307-how-does-the-zoneless-scheduler-decide-when-to-run-change-detection)
- [308: What does ApplicationRef.tick() do?](#308-what-does-applicationreftick-do)
- [309: What is PendingTasks and why does it matter?](#309-what-is-pendingtasks-and-why-does-it-matter)
- [310: What is exhaustive checkNoChanges?](#310-what-is-exhaustive-checknochanges)
- [311: What is event coalescing in Zone.js apps?](#311-what-is-event-coalescing-in-zonejs-apps)
- [312: How does Zone.js work?](#312-how-does-zonejs-work)
- [313: How do you find code that breaks in a zoneless app?](#313-how-do-you-find-code-that-breaks-in-a-zoneless-app)
- [314: What happens if a signal changes during change detection?](#314-what-happens-if-a-signal-changes-during-change-detection)
- [315: How are effects scheduled?](#315-how-are-effects-scheduled)
- [316: How does the signal dependency graph work?](#316-how-does-the-signal-dependency-graph-work)
- [317: What does "glitch-free" mean for signals?](#317-what-does-glitch-free-mean-for-signals)
- [318: What happens when a computed throws an error?](#318-what-happens-when-a-computed-throws-an-error)
- [319: When is linkedSignal better than computed plus a writable signal?](#319-when-is-linkedsignal-better-than-computed-plus-a-writable-signal)
- [320: What are the possible states of a resource?](#320-what-are-the-possible-states-of-a-resource)
- [321: What is a streaming resource?](#321-what-is-a-streaming-resource)
- [322: How do you validate an httpResource response?](#322-how-do-you-validate-an-httpresource-response)
- [323: How do you debounce a resource?](#323-how-do-you-debounce-a-resource)
- [324: What is afterRenderEffect()?](#324-what-is-afterrendereffect)
- [325: How do you build a component that works both controlled and uncontrolled?](#325-how-do-you-build-a-component-that-works-both-controlled-and-uncontrolled)
- [326: What is NgRx SignalStore?](#326-what-is-ngrx-signalstore)
- [327: How do you choose between signal services, SignalStore and NgRx Store?](#327-how-do-you-choose-between-signal-services-signalstore-and-ngrx-store)
- [328: How do you avoid infinite loops with effects?](#328-how-do-you-avoid-infinite-loops-with-effects)
- [329: How does the host flag work with element injectors?](#329-how-does-the-host-flag-work-with-element-injectors)
- [330: How do you write your own provideX() function?](#330-how-do-you-write-your-own-providex-function)
- [331: How do you create an injector at runtime?](#331-how-do-you-create-an-injector-at-runtime)
- [332: What is forwardRef() and when do you need it?](#332-what-is-forwardref-and-when-do-you-need-it)
- [333: What is providedIn: 'platform'?](#333-what-is-providedin-platform)
- [334: What is provideEnvironmentInitializer()?](#334-what-is-provideenvironmentinitializer)
- [335: How do you fix a circular dependency error (NG0200)?](#335-how-do-you-fix-a-circular-dependency-error-ng0200)
- [336: Where does code for a providedIn: 'root' service end up in the bundles?](#336-where-does-code-for-a-providedin-root-service-end-up-in-the-bundles)
- [337: How long do route-level injectors live?](#337-how-long-do-route-level-injectors-live)
- [338: How do you override providers in tests?](#338-how-do-you-override-providers-in-tests)
- [339: What are the pitfalls of using inject() in helper functions?](#339-what-are-the-pitfalls-of-using-inject-in-helper-functions)
- [340: How do you switch implementations based on runtime config?](#340-how-do-you-switch-implementations-based-on-runtime-config)
- [341: What is a RouteReuseStrategy?](#341-what-is-a-routereusestrategy)
- [342: How do you write a custom TitleStrategy?](#342-how-do-you-write-a-custom-titlestrategy)
- [343: What is a UrlMatcher?](#343-what-is-a-urlmatcher)
- [344: How do you customize how URLs are parsed and serialized?](#344-how-do-you-customize-how-urls-are-parsed-and-serialized)
- [345: In what order do guards and resolvers run?](#345-in-what-order-do-guards-and-resolvers-run)
- [346: What does paramsInheritanceStrategy do?](#346-what-does-paramsinheritancestrategy-do)
- [347: How do you reload the current route?](#347-how-do-you-reload-the-current-route)
- [348: How do you handle navigation errors globally?](#348-how-do-you-handle-navigation-errors-globally)
- [349: How do you handle stale chunks after a new deployment?](#349-how-do-you-handle-stale-chunks-after-a-new-deployment)
- [350: How do you implement token refresh in an interceptor?](#350-how-do-you-implement-token-refresh-in-an-interceptor)
- [351: When should you use the route snapshot vs observables?](#351-when-should-you-use-the-route-snapshot-vs-observables)
- [352: How would you build a smarter preloading strategy?](#352-how-would-you-build-a-smarter-preloading-strategy)
- [353: How does the SSR server (server.ts) work?](#353-how-does-the-ssr-server-serverts-work)
- [354: What render modes can each route use?](#354-what-render-modes-can-each-route-use)
- [355: What is incremental hydration?](#355-what-is-incremental-hydration)
- [356: What hydration triggers are available?](#356-what-hydration-triggers-are-available)
- [357: What causes hydration mismatch errors and how do you fix them?](#357-what-causes-hydration-mismatch-errors-and-how-do-you-fix-them)
- [358: What is the HTTP transfer cache?](#358-what-is-the-http-transfer-cache)
- [359: How do you use TransferState manually?](#359-how-do-you-use-transferstate-manually)
- [360: How do you access the request on the server?](#360-how-do-you-access-the-request-on-the-server)
- [361: How do you return a 404 status from SSR?](#361-how-do-you-return-a-404-status-from-ssr)
- [362: How do you cache SSR pages?](#362-how-do-you-cache-ssr-pages)
- [363: How do you provide different services on the server and in the browser?](#363-how-do-you-provide-different-services-on-the-server-and-in-the-browser)
- [364: Why might an SSR render never finish or time out?](#364-why-might-an-ssr-render-never-finish-or-time-out)
- [365: How do you handle authentication with SSR?](#365-how-do-you-handle-authentication-with-ssr)
- [366: Can Angular SSR run outside Node.js?](#366-can-angular-ssr-run-outside-nodejs)
- [367: How does event replay work?](#367-how-does-event-replay-work)
- [368: How does i18n work with SSR?](#368-how-does-i18n-work-with-ssr)
- [369: How do you analyze bundle size?](#369-how-do-you-analyze-bundle-size)
- [370: How do you profile an Angular app?](#370-how-do-you-profile-an-angular-app)
- [371: How do you speed up a slow list or table?](#371-how-do-you-speed-up-a-slow-list-or-table)
- [372: How do you make the initial bundle smaller?](#372-how-do-you-make-the-initial-bundle-smaller)
- [373: How do you find memory leaks in an Angular app?](#373-how-do-you-find-memory-leaks-in-an-angular-app)
- [374: How do you use Web Workers in Angular?](#374-how-do-you-use-web-workers-in-angular)
- [375: How do you improve Core Web Vitals in Angular?](#375-how-do-you-improve-core-web-vitals-in-angular)
- [376: What is layout thrashing and how do you avoid it?](#376-what-is-layout-thrashing-and-how-do-you-avoid-it)
- [377: How do you cache HTTP data on the client?](#377-how-do-you-cache-http-data-on-the-client)
- [378: How do you keep large reactive forms fast?](#378-how-do-you-keep-large-reactive-forms-fast)
- [379: What is zone pollution?](#379-what-is-zone-pollution)
- [380: How do you structure a large Angular application?](#380-how-do-you-structure-a-large-angular-application)
- [381: What is Nx and why would you use it with Angular?](#381-what-is-nx-and-why-would-you-use-it-with-angular)
- [382: How do micro frontends work with Angular?](#382-how-do-micro-frontends-work-with-angular)
- [383: What is the facade pattern in Angular?](#383-what-is-the-facade-pattern-in-angular)
- [384: How would you design error handling across an Angular app?](#384-how-would-you-design-error-handling-across-an-angular-app)
- [385: Where should you store auth tokens in the browser?](#385-where-should-you-store-auth-tokens-in-the-browser)
- [386: What are Trusted Types and how does Angular support them?](#386-what-are-trusted-types-and-how-does-angular-support-them)
- [387: What security risks should you look for in an Angular code review?](#387-what-security-risks-should-you-look-for-in-an-angular-code-review)
- [388: How do you implement feature flags?](#388-how-do-you-implement-feature-flags)
- [389: What are secondary entry points in a library?](#389-what-are-secondary-entry-points-in-a-library)
- [390: How do you share state between micro frontends?](#390-how-do-you-share-state-between-micro-frontends)
- [391: How do you plan Angular upgrades in a large app?](#391-how-do-you-plan-angular-upgrades-in-a-large-app)
- [392: How do you add monitoring and logging to an Angular app?](#392-how-do-you-add-monitoring-and-logging-to-an-angular-app)
- [393: How do you support multiple themes or tenants?](#393-how-do-you-support-multiple-themes-or-tenants)
- [394: How do you make an Angular app work offline (PWA)?](#394-how-do-you-make-an-angular-app-work-offline-pwa)
- [395: How do you handle real-time data with websockets and signals?](#395-how-do-you-handle-real-time-data-with-websockets-and-signals)
- [396: How do you make a ControlValueAccessor validate itself?](#396-how-do-you-make-a-controlvalueaccessor-validate-itself)
- [397: How do you build a dynamic form from a JSON config?](#397-how-do-you-build-a-dynamic-form-from-a-json-config)
- [398: How do you reuse validation logic in signal forms?](#398-how-do-you-reuse-validation-logic-in-signal-forms)
- [399: How does async validation work in signal forms?](#399-how-does-async-validation-work-in-signal-forms)
- [400: How do you create a custom control for signal forms?](#400-how-do-you-create-a-custom-control-for-signal-forms)
- [401: How do you add conditional logic in signal forms?](#401-how-do-you-add-conditional-logic-in-signal-forms)
- [402: How do you use reactive forms together with signals?](#402-how-do-you-use-reactive-forms-together-with-signals)
- [403: How do you type a FormArray of FormGroups?](#403-how-do-you-type-a-formarray-of-formgroups)
- [404: How do you avoid race conditions with async validators?](#404-how-do-you-avoid-race-conditions-with-async-validators)
- [405: How do you keep form data when the user navigates away and comes back?](#405-how-do-you-keep-form-data-when-the-user-navigates-away-and-comes-back)
- [406: What are host directives?](#406-what-are-host-directives)
- [407: What should you know about host directive limitations?](#407-what-should-you-know-about-host-directive-limitations)
- [408: How do you type the context of an ng-template in a custom directive?](#408-how-do-you-type-the-context-of-an-ng-template-in-a-custom-directive)
- [409: How do generic components work?](#409-how-do-generic-components-work)
- [410: How do content queries behave with nested components?](#410-how-do-content-queries-behave-with-nested-components)
- [411: What is the difference between embedded views and host views?](#411-what-is-the-difference-between-embedded-views-and-host-views)
- [412: How do CDK Portals and Overlays work?](#412-how-do-cdk-portals-and-overlays-work)
- [413: How do you build a service that opens components (like a dialog) outside the current template?](#413-how-do-you-build-a-service-that-opens-components-like-a-dialog-outside-the-current-template)
- [414: How do you build compound components that talk to each other?](#414-how-do-you-build-compound-components-that-talk-to-each-other)
- [415: What are the pitfalls of component inheritance?](#415-what-are-the-pitfalls-of-component-inheritance)
- [416: What replaced ngAcceptInputType?](#416-what-replaced-ngacceptinputtype)
- [417: How do Angular Elements work with Shadow DOM and slots?](#417-how-do-angular-elements-work-with-shadow-dom-and-slots)
- [418: When do you use @defer vs lazy routes vs dynamic import()?](#418-when-do-you-use-defer-vs-lazy-routes-vs-dynamic-import)
- [419: How do you build a recursive component, like a tree?](#419-how-do-you-build-a-recursive-component-like-a-tree)
- [420: Why doesn't conditional ng-content work as expected?](#420-why-doesnt-conditional-ng-content-work-as-expected)
- [421: What are the differences between signal queries and decorator queries?](#421-what-are-the-differences-between-signal-queries-and-decorator-queries)
- [422: What is partial compilation and the Angular Package Format?](#422-what-is-partial-compilation-and-the-angular-package-format)
- [423: How do you write a custom schematic?](#423-how-do-you-write-a-custom-schematic)
- [424: What is a custom builder?](#424-what-is-a-custom-builder)
- [425: How does hot module replacement work in Angular?](#425-how-does-hot-module-replacement-work-in-angular)
- [426: What are extended diagnostics?](#426-what-are-extended-diagnostics)
- [427: How do you load translations at runtime with $localize?](#427-how-do-you-load-translations-at-runtime-with-localize)
- [428: What are ICU expressions?](#428-what-are-icu-expressions)
- [429: What is the Angular CLI MCP server?](#429-what-is-the-angular-cli-mcp-server)
- [430: How do you inject build-time constants?](#430-how-do-you-inject-build-time-constants)
- [431: What are the loader and externalDependencies build options?](#431-what-are-the-loader-and-externaldependencies-build-options)
- [432: What output modes does the application builder have?](#432-what-output-modes-does-the-application-builder-have)
- [433: How do you set the locale for pipes like date and currency?](#433-how-do-you-set-the-locale-for-pipes-like-date-and-currency)
- [434: How do you test code that uses effects?](#434-how-do-you-test-code-that-uses-effects)
- [435: How do you test httpResource?](#435-how-do-you-test-httpresource)
- [436: How do you test a functional guard?](#436-how-do-you-test-a-functional-guard)
- [437: How do you test an HTTP interceptor?](#437-how-do-you-test-an-http-interceptor)
- [438: How do you write your own component harness?](#438-how-do-you-write-your-own-component-harness)
- [439: How do you test timers in a zoneless app?](#439-how-do-you-test-timers-in-a-zoneless-app)
- [440: How do you do end-to-end testing in Angular?](#440-how-do-you-do-end-to-end-testing-in-angular)
- [441: How do you test @defer blocks?](#441-how-do-you-test-defer-blocks)
- [442: How do you test a custom form control?](#442-how-do-you-test-a-custom-form-control)
- [443: Why can a test pass but the real OnPush or zoneless component not update?](#443-why-can-a-test-pass-but-the-real-onpush-or-zoneless-component-not-update)
- [444: What common Angular runtime error codes should you know?](#444-what-common-angular-runtime-error-codes-should-you-know)
- [445: What do experimental, developer preview and stable mean for Angular APIs?](#445-what-do-experimental-developer-preview-and-stable-mean-for-angular-apis)
- [446: How does @for update the DOM when the list changes?](#446-how-does-for-update-the-dom-when-the-list-changes)
- [447: Why should you avoid Angular's private APIs (the ɵ prefix)?](#447-why-should-you-avoid-angulars-private-apis-the-ɵ-prefix)
- [448: How do you use non-Angular web components in an Angular template?](#448-how-do-you-use-non-angular-web-components-in-an-angular-template)
- [449: How do you design a good API for a reusable component library?](#449-how-do-you-design-a-good-api-for-a-reusable-component-library)
- [450: What is HttpBackend and when would you use it?](#450-what-is-httpbackend-and-when-would-you-use-it)

---

# Easy Questions (1-150)

## 1: What is Angular?

Angular is a front-end framework from Google for building web applications. You write your app in TypeScript, split it into components, and Angular takes care of rendering, updating the DOM, routing, forms, HTTP calls and more.

It is a full framework, not just a view library. Out of the box you get:

- Components and templates
- Signals for reactive state
- Dependency injection
- A router
- Forms (template-driven, reactive and the newer signal forms)
- An HTTP client
- A CLI for creating, building, testing and updating projects
- Server-side rendering support

## 2: What is the difference between AngularJS and Angular?

AngularJS (version 1.x) is the old framework released in 2010. It is written in JavaScript, uses controllers and `$scope`, and relies on a digest cycle for change detection. It reached end of life in January 2022.

Angular (version 2 and above) is a full rewrite. It uses TypeScript, a component-based architecture, ahead-of-time compilation, dependency injection with classes, and today uses signals for reactivity. The two are not compatible. Moving from AngularJS to Angular is a migration, not an upgrade.

## 3: How often is Angular released and how long is a version supported?

Angular releases a new major version about every six months, with minor releases and patches in between. Each major version is supported for 18 months:

- 6 months of active support (regular updates and patches)
- 12 months of long-term support (only critical fixes and security patches)

You can check the current version and support dates at `angular.dev/reference/releases`. This guide is written against the modern APIs (Angular 20, 21 and later): standalone components, signals, the new control flow, zoneless change detection and so on.

## 4: Why does Angular use TypeScript?

TypeScript is JavaScript with static types. Angular uses it because:

- Type errors are caught at build time instead of in the browser.
- Editors can give good autocomplete and refactoring.
- Decorators and classes make components and services easy to describe.
- The Angular compiler uses type information to check your templates (with `strictTemplates`).

```ts
interface User {
  id: number;
  name: string;
}

function greet(user: User): string {
  return `Hello, ${user.name}`;
}
```

## 5: How do you install the Angular CLI and create a new project?

Install the CLI globally with npm, then use `ng new`:

```bash
npm install -g @angular/cli
ng new my-app
cd my-app
ng serve
```

`ng new` asks a few questions (stylesheet format, SSR, etc.). After `ng serve`, the app runs at `http://localhost:4200`.

You can also skip the global install:

```bash
npx @angular/cli@latest new my-app
```

## 6: What is the Angular CLI?

The Angular CLI (`ng`) is a command line tool for working with Angular projects. It can:

- Create projects (`ng new`)
- Generate code (`ng generate component`, `ng generate service`, ...)
- Run a dev server (`ng serve`)
- Build for production (`ng build`)
- Run tests (`ng test`)
- Add libraries with setup (`ng add`)
- Update Angular and run migrations (`ng update`)

It hides most of the build configuration so you don't have to set up a bundler yourself.

## 7: What are the main files in a new Angular project?

A new project created with a recent CLI looks roughly like this:

```
my-app/
  angular.json          # workspace and build configuration
  package.json          # dependencies and npm scripts
  tsconfig.json         # TypeScript settings
  public/               # static files copied as-is (favicon, images)
  src/
    index.html          # main HTML page
    main.ts             # entry point, bootstraps the app
    styles.css          # global styles
    app/
      app.ts            # root component
      app.html          # root component template
      app.css           # root component styles
      app.config.ts     # application-wide providers
      app.routes.ts     # route definitions
```

Since Angular 20 the CLI does not add the `.component` suffix by default, so the root component file is `app.ts` and the class is `App`.

## 8: What is a component?

A component is a building block of the UI. It is a TypeScript class with the `@Component` decorator, plus a template (HTML) and optional styles. Every Angular app is a tree of components.

```ts
import { Component } from "@angular/core";

@Component({
  selector: "app-hello",
  template: `<h1>Hello, {{ name }}!</h1>`,
  styles: `
    h1 {
      color: teal;
    }
  `,
})
export class Hello {
  name = "Angular";
}
```

You use it in another template with `<app-hello />`.

## 9: How do you generate a component with the CLI?

```bash
ng generate component user-profile
# short form
ng g c user-profile
```

This creates a folder with:

```
user-profile/
  user-profile.ts
  user-profile.html
  user-profile.css
  user-profile.spec.ts
```

Useful options:

- `--inline-template` / `--inline-style` to keep template and styles in the `.ts` file
- `--skip-tests` to skip the spec file
- `--type=component` if you want the old `user-profile.component.ts` file naming

## 10: What are the main properties of the @Component decorator?

The most used ones are:

- `selector`: the tag or attribute used to place the component (`'app-user'`)
- `template` or `templateUrl`: the HTML
- `styles` or `styleUrl` / `styleUrls`: the CSS
- `imports`: other components, directives and pipes used in the template
- `changeDetection`: `ChangeDetectionStrategy.OnPush` or `Default`
- `providers`: services that are scoped to this component
- `host`: bindings on the host element
- `encapsulation`: how styles are scoped

```ts
@Component({
  selector: "app-user-card",
  imports: [DatePipe],
  templateUrl: "./user-card.html",
  styleUrl: "./user-card.css",
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UserCard {}
```

## 11: What is a standalone component?

A standalone component is a component that does not belong to an `NgModule`. It lists what it needs directly in its own `imports` array.

```ts
@Component({
  selector: "app-todo-list",
  imports: [TodoItem, UpperCasePipe],
  template: `
    @for (todo of todos; track todo.id) {
      <app-todo-item [todo]="todo" />
    }
  `,
})
export class TodoList {
  todos = [{ id: 1, title: "Learn Angular" }];
}
```

This makes each component self-contained and easier to lazy load and test.

## 12: Are components standalone by default?

Yes. Since Angular 19, `standalone: true` is the default for components, directives and pipes, so you don't write it anymore. If you still need a component to be declared in an `NgModule`, you set `standalone: false`.

```ts
@Component({
  selector: "app-legacy",
  standalone: false, // only needed for NgModule-based code
  template: `...`,
})
export class Legacy {}
```

## 13: What is a template?

A template is the HTML of a component. Besides plain HTML, it can contain Angular syntax:

- Interpolation: `{{ value }}`
- Bindings: `[property]`, `(event)`, `[(twoWay)]`
- Control flow: `@if`, `@for`, `@switch`, `@defer`
- Local variables: `@let`, `#ref`
- Pipes: `{{ price | currency }}`
- Other components and directives

```html
<h2>{{ title }}</h2>
@if (items.length > 0) {
<ul>
  @for (item of items; track item.id) {
  <li>{{ item.name }}</li>
  }
</ul>
}
```

## 14: What is the difference between an inline template and an external template?

An inline template is written in the `template` property inside the TypeScript file. An external template is a separate `.html` file referenced with `templateUrl`.

```ts
// inline
@Component({
  selector: "app-badge",
  template: `<span class="badge">{{ text }}</span>`,
})
export class Badge {
  text = "New";
}

// external
@Component({
  selector: "app-profile",
  templateUrl: "./profile.html",
})
export class Profile {}
```

Inline is fine for small components. Use external files when the template gets longer than a few lines. There is no runtime difference, both are compiled the same way.

## 15: What is data binding and what types exist in Angular?

Data binding connects the component class with the template. Angular has:

| Type              | Syntax                      | Direction     |
| ----------------- | --------------------------- | ------------- |
| Interpolation     | `{{ value }}`               | class to view |
| Property binding  | `[src]="url"`               | class to view |
| Event binding     | `(click)="save()"`          | view to class |
| Two-way binding   | `[(ngModel)]="name"`        | both          |
| Attribute binding | `[attr.aria-label]="label"` | class to view |
| Class binding     | `[class.active]="isActive"` | class to view |
| Style binding     | `[style.width.px]="width"`  | class to view |

## 16: What is interpolation?

Interpolation puts the value of an expression into the text of the template using double curly braces. Angular converts the result to a string.

```ts
@Component({
  selector: "app-greeting",
  template: `
    <p>Hello, {{ name() }}</p>
    <p>2 + 2 = {{ 2 + 2 }}</p>
    <p>Total: {{ price * quantity }}</p>
  `,
})
export class Greeting {
  name = signal("Sara");
  price = 10;
  quantity = 3;
}
```

## 17: What is property binding?

Property binding sets a DOM property (or a component input) to the value of an expression. You wrap the property name in square brackets.

```html
<img [src]="imageUrl" [alt]="imageAlt" />
<button [disabled]="isSaving()">Save</button>
<app-user-card [user]="selectedUser()" />
```

Note that it binds to DOM **properties**, not HTML attributes. For example `[disabled]` sets `button.disabled = true/false`.

## 18: What is event binding?

Event binding listens to DOM events (or component outputs) and runs a statement when they happen. You wrap the event name in parentheses.

```ts
@Component({
  selector: "app-counter",
  template: `
    <p>Count: {{ count() }}</p>
    <button (click)="increment()">+1</button>
    <input (input)="onInput($event)" />
  `,
})
export class Counter {
  count = signal(0);

  increment() {
    this.count.update((c) => c + 1);
  }

  onInput(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    console.log(value);
  }
}
```

## 19: What is two-way binding?

Two-way binding keeps a value in the class and a value in the view in sync. The syntax `[( )]` is called "banana in a box". It is a shortcut for a property binding plus an event binding.

```html
<!-- with forms -->
<input [(ngModel)]="username" />

<!-- with your own component that has a model() input -->
<app-rating [(value)]="rating" />
```

`[(value)]="rating"` is the same as:

```html
<app-rating [value]="rating" (valueChange)="rating = $event" />
```

You can bind a signal directly: `[(value)]="ratingSignal"`.

## 20: What is attribute binding and when do you need it?

Some HTML attributes don't have a matching DOM property, for example `aria-*`, `colspan` on some elements, or SVG attributes. For those you use `attr.`:

```html
<button [attr.aria-label]="closeLabel">X</button>
<td [attr.colspan]="columns">...</td>
<svg><circle [attr.r]="radius" /></svg>
```

If the value is `null` or `undefined`, Angular removes the attribute.

## 21: How does class binding work?

You can toggle one class or bind many classes at once.

```html
<!-- single class -->
<div [class.active]="isActive()">...</div>

<!-- string -->
<div [class]="'card shadow'">...</div>

<!-- object: key is class, value is condition -->
<div [class]="{ active: isActive(), disabled: isDisabled() }">...</div>

<!-- array -->
<div [class]="['card', theme()]">...</div>
```

The Angular team recommends using `[class]` bindings instead of the `NgClass` directive.

## 22: How does style binding work?

```html
<!-- single style -->
<div [style.color]="textColor">...</div>

<!-- with a unit -->
<div [style.width.px]="width">...</div>
<div [style.font-size.rem]="1.2">...</div>

<!-- many styles at once -->
<div [style]="{ color: textColor, 'background-color': bg }">...</div>
```

Like class binding, plain `[style]` bindings are recommended over the `NgStyle` directive.

## 23: What is a directive and what types of directives exist?

A directive is a class that adds behavior to elements in the template. There are three kinds:

1. **Components**: directives with a template.
2. **Attribute directives**: change the look or behavior of an element (for example `NgClass`, `NgModel`, or your own `appHighlight`).
3. **Structural directives**: change the DOM layout by adding or removing elements (for example the old `*ngIf` and `*ngFor`). In modern Angular, most of this is done with the built-in control flow blocks (`@if`, `@for`, `@switch`) instead.

## 24: What is the difference between a component and a directive?

A component is a directive with its own template. A directive has no template, it only works on an existing element.

```ts
// Directive: adds behavior to an existing element
@Directive({
  selector: "[appAutofocus]",
})
export class Autofocus {
  private el = inject(ElementRef<HTMLElement>);

  constructor() {
    afterNextRender(() => this.el.nativeElement.focus());
  }
}

// Component: has its own template
@Component({
  selector: "app-search",
  imports: [Autofocus],
  template: `<input appAutofocus placeholder="Search..." />`,
})
export class Search {}
```

An element can have only one component, but it can have many directives.

## 25: How does the @if block work?

`@if` shows or hides a part of the template based on a condition. You can add `@else if` and `@else`.

```html
@if (user(); as u) {
<p>Welcome, {{ u.name }}</p>
} @else if (isLoading()) {
<p>Loading...</p>
} @else {
<button (click)="login()">Log in</button>
}
```

The `as` part saves the result of the expression in a local variable. Content inside a false branch is not in the DOM at all.

## 26: How does the @for block work?

`@for` repeats a block for each item in a collection. The `track` expression is required. It tells Angular how to identify each item so it can reuse DOM nodes when the list changes.

```html
<ul>
  @for (product of products(); track product.id) {
  <li>{{ product.name }} - {{ product.price | currency }}</li>
  }
</ul>
```

Use a unique id for `track` when you have one. If items are primitive values and unique, `track item` works. Use `track $index` only when the list never reorders.

## 27: What implicit variables are available inside @for?

| Variable | Meaning                   |
| -------- | ------------------------- |
| `$index` | index of the current item |
| `$count` | number of items           |
| `$first` | true for the first item   |
| `$last`  | true for the last item    |
| `$even`  | true for even indexes     |
| `$odd`   | true for odd indexes      |

```html
@for (item of items; track item.id; let i = $index, last = $last) {
<span>{{ i + 1 }}. {{ item.name }}</span>
@if (!last) { <span>, </span> } }
```

## 28: What is the @empty block?

`@empty` is an optional block after `@for`. It is shown when the collection has no items.

```html
@for (order of orders(); track order.id) {
<app-order-row [order]="order" />
} @empty {
<p>You have no orders yet.</p>
}
```

## 29: How does the @switch block work?

`@switch` picks one block based on a value. It uses `===` to compare. There is no fall-through, so you don't need `break`.

```html
@switch (status()) { @case ('active') {
<span class="green">Active</span>
} @case ('blocked') {
<span class="red">Blocked</span>
} @default {
<span>Unknown</span>
} }
```

## 30: What happened to *ngIf, *ngFor and \*ngSwitch?

They still work, but they were deprecated in Angular 20 in favor of the built-in control flow (`@if`, `@for`, `@switch`). The built-in blocks:

- Don't need any import
- Have better type checking
- Are faster, especially `@for`
- Make `track` required, which avoids a common performance mistake

You can migrate a project automatically:

```bash
ng generate @angular/core:control-flow
```

## 31: What is ng-template?

`<ng-template>` defines a piece of template that is **not** rendered by default. It is rendered only when something asks for it, like `ngTemplateOutlet`, a structural directive, or code using `ViewContainerRef`.

```html
<ng-template #loading>
  <p>Loading...</p>
</ng-template>

@if (data()) {
<app-table [rows]="data()" />
} @else {
<ng-container [ngTemplateOutlet]="loading" />
}
```

## 32: What is ng-container?

`<ng-container>` is a grouping element that does not create any DOM element of its own. It is useful when you need a place to attach a directive without adding an extra `<div>`.

```html
<ul>
  @for (group of groups; track group.id) {
  <ng-container>
    <li class="header">{{ group.title }}</li>
    @for (item of group.items; track item.id) {
    <li>{{ item.name }}</li>
    }
  </ng-container>
  }
</ul>

<ng-container *ngTemplateOutlet="tpl" />
```

## 33: What is @let in templates?

`@let` declares a local, read-only variable inside a template. It is handy for avoiding repeated expressions or async pipes.

```html
@let user = user$ | async; @let fullName = user?.firstName + ' ' +
user?.lastName;

<h1>{{ fullName }}</h1>
<p>{{ user?.email }}</p>
```

The variable is available after its declaration in the same view and its children. You cannot reassign it from the template.

## 34: What is a template reference variable?

A template reference variable gives a name to an element, component or directive in the template using `#`. You can then use it elsewhere in the same template.

```html
<input #email type="email" />
<button (click)="subscribe(email.value)">Subscribe</button>

<app-video-player #player />
<button (click)="player.play()">Play</button>
```

On a plain element, the variable is the DOM element. On a component, it is the component instance.

## 35: What is a pipe?

A pipe transforms a value in the template for display. You use the `|` character.

```html
<p>{{ birthday | date: 'longDate' }}</p>
<p>{{ price | currency: 'EUR' }}</p>
<p>{{ name | uppercase }}</p>
```

Pipes don't change the original value, they only change how it is shown. You need to add the pipe to the component's `imports`:

```ts
@Component({
  selector: "app-invoice",
  imports: [DatePipe, CurrencyPipe, UpperCasePipe],
  templateUrl: "./invoice.html",
})
export class Invoice {}
```

## 36: What built-in pipes does Angular have?

From `@angular/common`:

- `DatePipe` (`date`)
- `UpperCasePipe`, `LowerCasePipe`, `TitleCasePipe`
- `CurrencyPipe`, `DecimalPipe` (`number`), `PercentPipe`
- `JsonPipe` (`json`)
- `SlicePipe` (`slice`)
- `AsyncPipe` (`async`)
- `KeyValuePipe` (`keyvalue`)
- `I18nPluralPipe`, `I18nSelectPipe`

```html
{{ 0.256 | percent: '1.0-1' }}
<!-- 25.6% -->
{{ 3.14159 | number: '1.2-2' }}
<!-- 3.14 -->
{{ items | slice: 0 : 3 }} @for (entry of config | keyvalue; track entry.key) {
{{ entry.key }}: {{ entry.value }} }
```

## 37: How do you pass parameters to a pipe and chain pipes?

Parameters go after a colon. You can chain pipes, and they run left to right.

```html
<!-- parameters -->
{{ today | date: 'dd/MM/yyyy' : 'UTC' }}

<!-- chaining -->
{{ today | date: 'fullDate' | uppercase }}
```

## 38: How do you create a custom pipe?

Create a class with `@Pipe` that implements `PipeTransform`.

```bash
ng generate pipe truncate
```

```ts
import { Pipe, PipeTransform } from "@angular/core";

@Pipe({ name: "truncate" })
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20, suffix = "..."): string {
    if (!value || value.length <= limit) {
      return value;
    }
    return value.slice(0, limit) + suffix;
  }
}
```

```html
<p>{{ article.body | truncate: 50 }}</p>
```

Remember to add `TruncatePipe` to the component's `imports`.

## 39: What is the async pipe?

The `async` pipe subscribes to an Observable (or waits for a Promise) and returns the latest value. When the component is destroyed, it unsubscribes automatically.

```ts
@Component({
  selector: "app-users",
  imports: [AsyncPipe],
  template: `
    @if (users$ | async; as users) {
      @for (user of users; track user.id) {
        <p>{{ user.name }}</p>
      }
    }
  `,
})
export class Users {
  users$ = inject(HttpClient).get<User[]>("/api/users");
}
```

In new code you will often convert Observables to signals with `toSignal()` instead, but the async pipe is still common and fully supported.

## 40: What is a service?

A service is a class that holds logic or data that is not tied to one view: API calls, shared state, logging, etc. Components get services through dependency injection.

```ts
import { Injectable, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({ providedIn: "root" })
export class ProductService {
  private http = inject(HttpClient);

  getProducts() {
    return this.http.get<Product[]>("/api/products");
  }
}
```

Keeping this logic in services keeps components small and focused on the UI.

## 41: How do you create a service with the CLI?

```bash
ng generate service cart
# short form
ng g s cart
```

With the current CLI defaults this creates `cart.ts` with a class named `Cart`. Many teams prefer the old naming, which you get with:

```bash
ng g s cart --type=service
# creates cart.service.ts with class CartService
```

The generated class has `@Injectable({ providedIn: 'root' })`, so it is ready to inject anywhere.

## 42: What is dependency injection?

Dependency injection (DI) is a pattern where a class does not create its dependencies itself. Instead, it asks for them and the framework gives them. In Angular, the injector creates and stores the instances.

```ts
@Component({
  selector: "app-cart",
  template: `...`,
})
export class Cart {
  // Angular gives us the instance, we don't call new CartService()
  private cartService = inject(CartService);
}
```

Benefits:

- Easier testing (you can swap a real service for a fake one)
- One shared instance where needed
- Less coupling between classes

## 43: What does providedIn: 'root' mean?

It registers the service with the root (application-level) injector. That means:

- There is one instance for the whole app (a singleton).
- The service is tree-shakable: if nobody injects it, it is removed from the bundle.
- You don't need to add it to any `providers` array.

```ts
@Injectable({ providedIn: "root" })
export class AuthService {}
```

## 44: What is the inject() function?

`inject()` gets a dependency from the current injector. It is the recommended way to get dependencies in modern Angular.

```ts
@Component({ selector: "app-home", template: `...` })
export class Home {
  private router = inject(Router);
  private auth = inject(AuthService);
  private config = inject(APP_CONFIG);
}
```

It only works in an "injection context": field initializers, constructors, factory functions, and functions like guards, resolvers and interceptors. Calling it in a method that runs later (like a click handler) throws an error.

## 45: What is the difference between constructor injection and inject()?

Both give you the same instance. The difference is syntax and flexibility.

```ts
// constructor injection
export class Profile {
  constructor(private userService: UserService) {}
}

// inject()
export class Profile {
  private userService = inject(UserService);
}
```

Reasons to prefer `inject()`:

- Works in plain functions (guards, interceptors, resolvers), not just classes.
- Easier to use with inheritance, no need to pass deps to `super()`.
- Better typing for injection tokens.
- Works well with the `useDefineForClassFields` TypeScript setting.

There is an automatic migration: `ng generate @angular/core:inject`.

## 46: What is an NgModule and do you still need it?

`NgModule` was the way to group components, directives, pipes and providers before standalone components existed.

```ts
@NgModule({
  declarations: [AppComponent, HeaderComponent],
  imports: [BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

New apps don't need NgModules. Components are standalone by default and the app starts with `bootstrapApplication()`. NgModules are still supported, and you will see them in older projects and some libraries.

## 47: What does main.ts do?

`main.ts` is the entry point. It starts (bootstraps) the application by rendering the root component with the app config.

```ts
import { bootstrapApplication } from "@angular/platform-browser";
import { appConfig } from "./app/app.config";
import { App } from "./app/app";

bootstrapApplication(App, appConfig).catch((err) => console.error(err));
```

## 48: What is app.config.ts?

It exports an `ApplicationConfig` object with the providers for the whole application, like the router, HTTP client, hydration or animations.

```ts
import {
  ApplicationConfig,
  provideBrowserGlobalErrorListeners,
} from "@angular/core";
import { provideRouter } from "@angular/router";
import { provideHttpClient, withFetch } from "@angular/common/http";
import { routes } from "./app.routes";

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
    provideHttpClient(withFetch()),
  ],
};
```

It replaces what used to go in the `imports` and `providers` of `AppModule`.

## 49: What is the root component?

The root component is the first component Angular renders, usually called `App` with selector `app-root`. Its selector matches a tag in `index.html`.

```html
<!-- index.html -->
<body>
  <app-root></app-root>
</body>
```

```ts
@Component({
  selector: "app-root",
  imports: [RouterOutlet, Header],
  template: `
    <app-header />
    <router-outlet />
  `,
})
export class App {}
```

## 50: What are lifecycle hooks?

Lifecycle hooks are methods Angular calls at certain moments in a component's life. In order:

1. `constructor` (not a hook, but runs first)
2. `ngOnChanges`: when an input changes (before `ngOnInit` too, if there are inputs)
3. `ngOnInit`: once, after the first inputs are set
4. `ngDoCheck`: on every change detection run
5. `ngAfterContentInit`: once, after projected content is initialized
6. `ngAfterContentChecked`: after each check of projected content
7. `ngAfterViewInit`: once, after the component's view and child views are created
8. `ngAfterViewChecked`: after each check of the view
9. `ngOnDestroy`: right before the component is destroyed

There are also `afterNextRender` and `afterEveryRender` functions for running code after the DOM is rendered.

## 51: What is the difference between the constructor and ngOnInit?

- The **constructor** runs when the class is created. Inputs are not set yet (for decorator inputs). Use it (or field initializers) for injecting dependencies and simple setup.
- **ngOnInit** runs once after Angular has set the inputs for the first time. Use it for logic that depends on input values.

```ts
export class UserDetails implements OnInit {
  @Input() userId!: number;
  private userService = inject(UserService);

  constructor() {
    console.log(this.userId); // undefined
  }

  ngOnInit() {
    console.log(this.userId); // has the value from the parent
  }
}
```

With signal inputs (`input()`), you can often skip `ngOnInit` and use `computed()` or `resource()` that react to the input instead.

## 52: What is ngOnDestroy used for?

It runs right before Angular destroys the component, directive, pipe or service. Use it for cleanup:

- Stop timers (`clearInterval`)
- Remove manual event listeners
- Unsubscribe from Observables that are not handled by the async pipe or `takeUntilDestroyed`

```ts
export class Clock implements OnDestroy {
  time = signal(new Date());
  private timerId = setInterval(() => this.time.set(new Date()), 1000);

  ngOnDestroy() {
    clearInterval(this.timerId);
  }
}
```

A modern alternative is `inject(DestroyRef).onDestroy(() => ...)`.

## 53: What is ngOnChanges?

`ngOnChanges` runs when one or more decorator-based `@Input()` values change. It gets a `SimpleChanges` object with the previous and current values.

```ts
export class Chart implements OnChanges {
  @Input() data: number[] = [];

  ngOnChanges(changes: SimpleChanges) {
    if (changes["data"]) {
      console.log("old", changes["data"].previousValue);
      console.log("new", changes["data"].currentValue);
      this.redraw();
    }
  }

  redraw() {}
}
```

With signal inputs you usually don't need it, because you can use `computed()` or `effect()` on the input signal.

## 54: What is a signal?

A signal is a wrapper around a value that tells Angular when the value changes. When a template reads a signal, Angular knows exactly which parts of the UI depend on it and updates them when the signal changes.

```ts
import { signal } from "@angular/core";

const count = signal(0);

console.log(count()); // read: 0
count.set(5); // replace
count.update((v) => v + 1); // update based on current value
console.log(count()); // 6
```

Signals are the core of Angular's reactivity model today.

## 55: How do you read and change a signal?

- Read: call it like a function, `count()`.
- `set(value)`: replace the value.
- `update(fn)`: compute a new value from the current one.

```ts
@Component({
  selector: "app-todo",
  template: `
    <p>{{ todos().length }} todos</p>
    <button (click)="add('New task')">Add</button>
  `,
})
export class Todo {
  todos = signal<string[]>([]);

  add(title: string) {
    // create a new array, don't push into the old one
    this.todos.update((list) => [...list, title]);
  }

  clear() {
    this.todos.set([]);
  }
}
```

Always create new objects or arrays when updating. Mutating them in place doesn't change the reference, so Angular won't see a change.

## 56: What is computed()?

`computed()` creates a read-only signal whose value is derived from other signals. It recalculates only when one of the signals it reads changes, and the result is cached.

```ts
export class Cart {
  items = signal<CartItem[]>([]);

  total = computed(() =>
    this.items().reduce((sum, item) => sum + item.price * item.qty, 0),
  );

  isEmpty = computed(() => this.items().length === 0);
}
```

```html
<p>Total: {{ total() | currency }}</p>
```

You can't call `set()` on a computed signal.

## 57: What is effect()?

`effect()` runs a function whenever the signals it reads change. It is for side effects, things that happen outside of Angular's rendering, such as saving to `localStorage`, logging, or calling a third-party library.

```ts
export class Settings {
  theme = signal<"light" | "dark">("light");

  constructor() {
    effect(() => {
      localStorage.setItem("theme", this.theme());
    });
  }
}
```

Effects run at least once. They must be created in an injection context (constructor or field initializer), and they are cleaned up automatically when the component is destroyed. Don't use effects to copy data from one signal to another, use `computed()` or `linkedSignal()` for that.

## 58: What is input()?

`input()` declares a signal-based input. The parent passes the value with property binding, and inside the component you read it as a signal.

```ts
@Component({
  selector: "app-avatar",
  template: `<img [src]="url()" [width]="size()" />`,
})
export class Avatar {
  url = input<string>(""); // optional with default
  size = input(48); // type inferred as number
}
```

```html
<app-avatar [url]="user.photo" [size]="64" />
```

Signal inputs are read-only inside the component. You can use them in `computed()` and `effect()`.

## 59: How do you make an input required?

Use `input.required()`. If the parent forgets to pass it, you get a compile error.

```ts
export class ProductCard {
  product = input.required<Product>();
  showPrice = input(true);
}
```

```html
<app-product-card [product]="p" />
```

Reading a required input before Angular sets it (for example in the constructor) throws an error.

## 60: What is output()?

`output()` declares an event that a component can emit to its parent.

```ts
@Component({
  selector: "app-delete-button",
  template: `<button (click)="confirm()">Delete</button>`,
})
export class DeleteButton {
  deleted = output<number>();
  itemId = input.required<number>();

  confirm() {
    this.deleted.emit(this.itemId());
  }
}
```

```html
<app-delete-button [itemId]="item.id" (deleted)="removeItem($event)" />
```

`output()` replaces `@Output() deleted = new EventEmitter<number>()`.

## 61: How does a parent component pass data to a child?

Through inputs. The child declares an input, and the parent binds to it.

```ts
// child
@Component({
  selector: "app-user-name",
  template: `<span>{{ user().firstName }} {{ user().lastName }}</span>`,
})
export class UserName {
  user = input.required<User>();
}

// parent
@Component({
  selector: "app-user-list",
  imports: [UserName],
  template: `
    @for (u of users(); track u.id) {
      <app-user-name [user]="u" />
    }
  `,
})
export class UserList {
  users = signal<User[]>([]);
}
```

## 62: How does a child component send data to a parent?

Through outputs. The child emits an event and the parent listens with event binding.

```ts
// child
@Component({
  selector: "app-search-box",
  template: `<input #q (keyup.enter)="search.emit(q.value)" />`,
})
export class SearchBox {
  search = output<string>();
}

// parent
@Component({
  selector: "app-page",
  imports: [SearchBox],
  template: `<app-search-box (search)="onSearch($event)" />`,
})
export class Page {
  onSearch(term: string) {
    console.log("Searching for", term);
  }
}
```

Other options are a shared service or the parent reading the child with `viewChild()`.

## 63: What is model()?

`model()` creates a writable input that supports two-way binding. The child can change it with `set()` or `update()`, and the parent's value updates too.

```ts
@Component({
  selector: "app-toggle",
  template: `
    <button (click)="checked.set(!checked())">
      {{ checked() ? "ON" : "OFF" }}
    </button>
  `,
})
export class Toggle {
  checked = model(false);
}
```

```ts
@Component({
  selector: "app-settings",
  imports: [Toggle],
  template: `
    <app-toggle [(checked)]="notifications" />
    <p>Notifications: {{ notifications() }}</p>
  `,
})
export class Settings {
  notifications = signal(true);
}
```

Behind the scenes, `model()` creates an input `checked` and an output `checkedChange`.

## 64: Are @Input() and @Output() decorators still supported?

Yes. They are fully supported and you will see them in a lot of code.

```ts
export class OldStyle {
  @Input() title = "";
  @Input({ required: true }) id!: number;
  @Output() saved = new EventEmitter<string>();
}
```

For new code, the signal-based `input()`, `output()` and `model()` are recommended. The CLI has migrations:

```bash
ng generate @angular/core:signal-input-migration
ng generate @angular/core:output-migration
```

## 65: How do you give an input or output a different public name?

Use the `alias` option. Inside the class you use one name, outside the parent uses another.

```ts
export class Tooltip {
  text = input("", { alias: "appTooltip" });
  closed = output<void>({ alias: "tooltipClosed" });
}
```

```html
<button appTooltip="Save changes" (tooltipClosed)="log()">Save</button>
```

Use aliases sparingly. They are most useful in attribute directives where the input has the same name as the selector.

## 66: What is routing in Angular?

Routing lets you show different components based on the URL, without reloading the page. The Angular Router:

- Maps URL paths to components
- Reads route and query parameters
- Supports lazy loading
- Protects routes with guards
- Loads data before showing a page with resolvers
- Manages browser history (back and forward buttons)

## 67: How do you define routes?

Routes go in an array of `Route` objects, usually in `app.routes.ts`, and are registered with `provideRouter()`.

```ts
// app.routes.ts
import { Routes } from "@angular/router";

export const routes: Routes = [
  { path: "", component: Home, title: "Home" },
  { path: "about", component: About, title: "About us" },
  { path: "products/:id", component: ProductDetails },
  { path: "**", component: NotFound },
];
```

```ts
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};
```

The `title` property sets the browser tab title for that route.

## 68: What is router-outlet?

`<router-outlet />` is a placeholder where the router renders the component for the current route.

```ts
@Component({
  selector: "app-root",
  imports: [RouterOutlet, RouterLink],
  template: `
    <nav>
      <a routerLink="/">Home</a>
      <a routerLink="/about">About</a>
    </nav>
    <main>
      <router-outlet />
    </main>
  `,
})
export class App {}
```

## 69: What is routerLink?

`routerLink` creates navigation links that work with the router, without a full page reload.

```html
<a routerLink="/about">About</a>

<!-- with parameters -->
<a [routerLink]="['/products', product.id]">{{ product.name }}</a>

<!-- with query params and fragment -->
<a
  routerLink="/search"
  [queryParams]="{ q: 'shoes', page: 2 }"
  fragment="results"
>
  Search
</a>
```

Using a plain `href` would reload the whole app, so always use `routerLink` for internal links.

## 70: What is routerLinkActive?

It adds CSS classes to an element when its link matches the current URL.

```html
<nav>
  <a
    routerLink="/"
    routerLinkActive="active"
    [routerLinkActiveOptions]="{ exact: true }"
  >
    Home
  </a>
  <a
    routerLink="/products"
    routerLinkActive="active"
    ariaCurrentWhenActive="page"
  >
    Products
  </a>
</nav>
```

`exact: true` is useful for the root link, otherwise it would be active on every page. `ariaCurrentWhenActive` sets `aria-current` for accessibility.

## 71: How do you navigate from code?

Inject `Router` and use `navigate()` or `navigateByUrl()`.

```ts
export class Login {
  private router = inject(Router);

  onLoginSuccess() {
    this.router.navigate(["/dashboard"]);
  }

  openProduct(id: number) {
    this.router.navigate(["/products", id], {
      queryParams: { tab: "reviews" },
    });
  }

  goHome() {
    this.router.navigateByUrl("/");
  }
}
```

Both return a Promise that resolves to `true` if navigation succeeded.

## 72: How do you read route parameters?

There are a few ways. The simplest in modern Angular is to bind route params to component inputs.

```ts
// app.config.ts
provideRouter(routes, withComponentInputBinding());

// route
{ path: 'products/:id', component: ProductDetails }

// component
export class ProductDetails {
  id = input.required<string>(); // filled from :id
}
```

Or use `ActivatedRoute`:

```ts
export class ProductDetails {
  private route = inject(ActivatedRoute);

  // snapshot: read once
  id = this.route.snapshot.paramMap.get("id");

  // observable: updates if the param changes while the component stays
  id$ = this.route.paramMap.pipe(map((p) => p.get("id")));
}
```

## 73: How do you read query parameters?

Query parameters are the `?key=value` part of the URL.

```ts
// URL: /search?q=laptop&page=2
export class Search {
  private route = inject(ActivatedRoute);

  query = toSignal(
    this.route.queryParamMap.pipe(map((p) => p.get("q") ?? "")),
    { initialValue: "" },
  );
}
```

With `withComponentInputBinding()`, query params are also bound to inputs with the same name:

```ts
export class Search {
  q = input<string>();
  page = input<string>();
}
```

## 74: How do you create a "page not found" route?

Use the wildcard path `**`. It matches any URL that didn't match an earlier route, so it must be the **last** route.

```ts
export const routes: Routes = [
  { path: "", component: Home },
  { path: "about", component: About },
  { path: "**", component: NotFound },
];
```

## 75: How do redirects and pathMatch work?

`redirectTo` sends the user to another path. `pathMatch` controls how the path is matched:

- `'prefix'` (default): matches if the URL starts with the path.
- `'full'`: matches only if the whole URL equals the path.

```ts
export const routes: Routes = [
  { path: "", redirectTo: "home", pathMatch: "full" },
  { path: "home", component: Home },
  { path: "old-blog", redirectTo: "blog" },
];
```

A redirect from an empty path must use `pathMatch: 'full'`, otherwise every URL would match.

## 76: What are child routes?

Child routes are routes nested under a parent route. The parent component has its own `<router-outlet />` where the child is rendered.

```ts
export const routes: Routes = [
  {
    path: "settings",
    component: SettingsLayout,
    children: [
      { path: "", redirectTo: "profile", pathMatch: "full" },
      { path: "profile", component: ProfileSettings },
      { path: "security", component: SecuritySettings },
    ],
  },
];
```

```html
<!-- settings-layout.html -->
<aside>
  <a routerLink="profile">Profile</a>
  <a routerLink="security">Security</a>
</aside>
<section>
  <router-outlet />
</section>
```

## 77: What is lazy loading?

Lazy loading means a part of the app is downloaded only when the user navigates to it, instead of in the initial bundle. This makes the first load faster.

```ts
export const routes: Routes = [
  { path: "", component: Home },
  {
    path: "admin",
    loadComponent: () => import("./admin/admin").then((m) => m.Admin),
  },
  {
    path: "shop",
    loadChildren: () => import("./shop/shop.routes").then((m) => m.SHOP_ROUTES),
  },
];
```

If the file uses a default export, you can write `loadComponent: () => import('./admin/admin')`.

## 78: What is HttpClient?

`HttpClient` is Angular's service for making HTTP requests. It:

- Returns Observables
- Parses JSON responses automatically
- Supports typed responses
- Supports interceptors for things like auth headers and error handling
- Has testing utilities

```ts
@Injectable({ providedIn: "root" })
export class TodoService {
  private http = inject(HttpClient);

  getTodos() {
    return this.http.get<Todo[]>("/api/todos");
  }
}
```

## 79: How do you set up HttpClient?

Call `provideHttpClient()` in your app config. This is where you add features like interceptors or the fetch backend.

```ts
import {
  provideHttpClient,
  withFetch,
  withInterceptors,
} from "@angular/common/http";

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(withFetch(), withInterceptors([authInterceptor])),
  ],
};
```

Starting with Angular 21, `HttpClient` is available by default even without `provideHttpClient()`. You still call it when you want to configure features. In older NgModule apps you would import `HttpClientModule`, which is now deprecated.

## 80: How do you make a GET request?

```ts
@Injectable({ providedIn: "root" })
export class UserService {
  private http = inject(HttpClient);

  getUsers() {
    return this.http.get<User[]>("/api/users");
  }

  getUser(id: number) {
    return this.http.get<User>(`/api/users/${id}`);
  }

  search(term: string) {
    return this.http.get<User[]>("/api/users", {
      params: { q: term, limit: 10 },
    });
  }
}
```

The request is only sent when something subscribes to the Observable (a `subscribe()` call, the async pipe, `toSignal()`, etc.).

## 81: How do you make POST, PUT and DELETE requests?

```ts
@Injectable({ providedIn: "root" })
export class TaskService {
  private http = inject(HttpClient);
  private url = "/api/tasks";

  create(task: NewTask) {
    return this.http.post<Task>(this.url, task);
  }

  update(task: Task) {
    return this.http.put<Task>(`${this.url}/${task.id}`, task);
  }

  patchTitle(id: number, title: string) {
    return this.http.patch<Task>(`${this.url}/${id}`, { title });
  }

  delete(id: number) {
    return this.http.delete<void>(`${this.url}/${id}`);
  }
}
```

```ts
// in a component
this.taskService.create({ title: "Buy milk" }).subscribe((task) => {
  this.tasks.update((list) => [...list, task]);
});
```

## 82: What is an Observable?

An Observable is a stream of values over time, from the RxJS library. You subscribe to it to receive values. It can emit zero, one or many values, and then complete or error.

```ts
import { Observable } from "rxjs";

const numbers$ = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  subscriber.complete();
});

numbers$.subscribe({
  next: (value) => console.log(value),
  error: (err) => console.error(err),
  complete: () => console.log("done"),
});
```

Angular uses Observables for HTTP, router events, reactive form value changes, and more. The `$` suffix is a common naming convention.

## 83: What is the difference between an Observable and a Promise?

| Observable                                     | Promise                                |
| ---------------------------------------------- | -------------------------------------- |
| Can emit many values                           | Resolves once                          |
| Lazy: nothing happens until you subscribe      | Eager: starts as soon as it is created |
| Can be cancelled (unsubscribe)                 | Can't be cancelled                     |
| Has many operators (map, filter, switchMap...) | Only `then`, `catch`, `finally`        |

You can convert between them with `firstValueFrom(obs$)` / `lastValueFrom(obs$)` and `from(promise)`.

## 84: What is RxJS?

RxJS is a library for working with asynchronous data as streams (Observables). Angular uses it in `HttpClient`, the router and reactive forms. It provides operators to transform and combine streams.

```ts
import { fromEvent, debounceTime, map, distinctUntilChanged } from "rxjs";

const input = document.querySelector("input")!;

fromEvent(input, "input")
  .pipe(
    map((e) => (e.target as HTMLInputElement).value),
    debounceTime(300),
    distinctUntilChanged(),
  )
  .subscribe((value) => console.log(value));
```

Today signals handle most component state, while RxJS is still useful for events over time, like search inputs, websockets and complex async flows.

## 85: Do you need to unsubscribe from Observables?

It depends on the Observable:

- **HTTP requests** complete after one response, so you usually don't need to unsubscribe. Unsubscribing early cancels the request, which can still be useful.
- **Long-lived streams** (intervals, `valueChanges`, router events, websockets, store selectors) keep running. If you subscribe manually, you must unsubscribe, or you get memory leaks.

Easy ways to handle it:

```ts
export class Ticker {
  constructor() {
    // 1. takeUntilDestroyed: unsubscribes when the component is destroyed
    interval(1000)
      .pipe(takeUntilDestroyed())
      .subscribe((n) => console.log(n));
  }

  // 2. toSignal: also unsubscribes automatically
  seconds = toSignal(interval(1000), { initialValue: 0 });
}
```

The `async` pipe in templates also unsubscribes for you.

## 86: What kinds of forms does Angular support?

1. **Template-driven forms**: the form is described in the template with `ngModel`. Good for simple forms. Import `FormsModule`.
2. **Reactive forms**: the form model is built in TypeScript with `FormControl`, `FormGroup` and `FormArray`. Better for complex forms, dynamic fields and testing. Import `ReactiveFormsModule`.
3. **Signal forms**: a newer, signal-based API added in Angular 21 (`@angular/forms/signals`). It is still experimental, so the API may change.

## 87: What is a template-driven form?

In a template-driven form you add `ngModel` to inputs and Angular creates the form controls for you.

```ts
@Component({
  selector: "app-contact",
  imports: [FormsModule],
  template: `
    <form #f="ngForm" (ngSubmit)="send(f.value)">
      <input name="email" [(ngModel)]="email" required email />
      <textarea name="message" [(ngModel)]="message" required></textarea>
      <button [disabled]="f.invalid">Send</button>
    </form>
  `,
})
export class Contact {
  email = "";
  message = "";

  send(value: { email: string; message: string }) {
    console.log(value);
  }
}
```

Each input with `ngModel` inside a `<form>` needs a `name` attribute.

## 88: What is ngModel?

`ngModel` is a directive from `FormsModule` that binds a form input to a value in the component. With `[(ngModel)]` you get two-way binding.

```ts
@Component({
  selector: "app-name-editor",
  imports: [FormsModule],
  template: `
    <input [(ngModel)]="name" />
    <p>Hello {{ name() }}</p>
  `,
})
export class NameEditor {
  name = signal("");
}
```

`ngModel` works with signals, so `[(ngModel)]="name"` with a writable signal is fine. It also tracks state like `touched`, `dirty` and `valid`.

## 89: What is a reactive form?

In a reactive form, you create the form structure in the component class and connect it to the template with directives like `[formGroup]` and `formControlName`.

```ts
@Component({
  selector: "app-login",
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input formControlName="email" type="email" />
      <input formControlName="password" type="password" />
      <button [disabled]="form.invalid">Log in</button>
    </form>
  `,
})
export class Login {
  form = new FormGroup({
    email: new FormControl("", {
      nonNullable: true,
      validators: [Validators.required, Validators.email],
    }),
    password: new FormControl("", {
      nonNullable: true,
      validators: Validators.required,
    }),
  });

  submit() {
    console.log(this.form.getRawValue());
  }
}
```

Reactive forms are synchronous, strongly typed and easy to unit test.

## 90: What is a FormControl?

`FormControl` tracks the value and validation state of a single input.

```ts
@Component({
  selector: "app-search",
  imports: [ReactiveFormsModule],
  template: `<input [formControl]="query" />`,
})
export class Search {
  query = new FormControl("", { nonNullable: true });

  constructor() {
    this.query.valueChanges
      .pipe(debounceTime(300), takeUntilDestroyed())
      .subscribe((v) => console.log(v));
  }
}
```

Useful members: `value`, `setValue()`, `reset()`, `valid`, `errors`, `touched`, `dirty`, `disable()`, `enable()`.

## 91: What is a FormGroup?

`FormGroup` groups several controls into one object. Its value is an object with a key per control, and it is valid only when all its controls are valid.

```ts
address = new FormGroup({
  street: new FormControl(""),
  city: new FormControl(""),
  zip: new FormControl(""),
});

// value: { street: '', city: '', zip: '' }
```

Groups can be nested:

```html
<form [formGroup]="profile">
  <input formControlName="name" />
  <div formGroupName="address">
    <input formControlName="street" />
    <input formControlName="city" />
  </div>
</form>
```

## 92: What is FormBuilder?

`FormBuilder` is a helper service that makes creating forms shorter.

```ts
export class Register {
  private fb = inject(NonNullableFormBuilder);

  form = this.fb.group({
    name: ["", Validators.required],
    email: ["", [Validators.required, Validators.email]],
    address: this.fb.group({
      city: [""],
      zip: [""],
    }),
  });
}
```

`NonNullableFormBuilder` (or `inject(FormBuilder).nonNullable`) makes all controls non-nullable, so `reset()` goes back to the initial value instead of `null`.

## 93: What built-in validators are there?

The `Validators` class has:

- `Validators.required`
- `Validators.requiredTrue` (for checkboxes)
- `Validators.email`
- `Validators.minLength(n)` / `Validators.maxLength(n)`
- `Validators.min(n)` / `Validators.max(n)`
- `Validators.pattern(regex)`
- `Validators.nullValidator`
- `Validators.compose([...])`

```ts
password = new FormControl("", [
  Validators.required,
  Validators.minLength(8),
  Validators.pattern(/[0-9]/),
]);
```

In template-driven forms you use the matching attributes: `required`, `email`, `minlength`, `maxlength`, `min`, `max`, `pattern`.

## 94: How do you show validation errors in the template?

Check the control's `errors` and state like `touched` so errors don't show before the user interacts.

```ts
export class Signup {
  email = new FormControl("", [Validators.required, Validators.email]);
}
```

```html
<input [formControl]="email" />

@if (email.invalid && email.touched) { @if (email.hasError('required')) {
<small>Email is required.</small>
} @if (email.hasError('email')) {
<small>Please enter a valid email.</small>
} }
```

## 95: What are the states of a form control?

| State                   | Meaning                                                         |
| ----------------------- | --------------------------------------------------------------- |
| `valid` / `invalid`     | passes or fails validation                                      |
| `pending`               | async validation is running                                     |
| `pristine` / `dirty`    | value has not / has been changed by the user                    |
| `untouched` / `touched` | the input has not / has lost focus                              |
| `enabled` / `disabled`  | disabled controls are excluded from validation and from `value` |

Angular also adds CSS classes to the input: `ng-valid`, `ng-invalid`, `ng-pending`, `ng-pristine`, `ng-dirty`, `ng-touched`, `ng-untouched`.

```css
input.ng-invalid.ng-touched {
  border-color: red;
}
```

## 96: What are signal forms?

Signal forms are a new forms API built on signals, added in Angular 21 as **experimental**. You keep your form data in a signal and call `form()` to create a field tree with value, validation and state as signals.

```ts
import { form, FormField, required, email } from "@angular/forms/signals";

@Component({
  selector: "app-newsletter",
  imports: [FormField],
  template: `
    <input [formField]="signupForm.email" />
    @if (signupForm.email().invalid() && signupForm.email().touched()) {
      <small>{{ signupForm.email().errors()[0].message }}</small>
    }
  `,
})
export class Newsletter {
  model = signal({ email: "" });

  signupForm = form(this.model, (path) => {
    required(path.email, { message: "Email is required" });
    email(path.email, { message: "Invalid email" });
  });
}
```

Because the API is experimental, some names have already changed between releases (for example the binding directive was first `[field]` and later `[formField]`). Check the docs for the version you use.

## 97: What is view encapsulation?

View encapsulation decides whether a component's styles stay inside the component or leak out. Options in `ViewEncapsulation`:

- `Emulated` (default): Angular adds unique attributes to elements and rewrites CSS selectors so styles only apply to this component.
- `ShadowDom`: uses the browser's native Shadow DOM.
- `None`: styles are global.

```ts
@Component({
  selector: "app-alert",
  template: `<p class="message">Warning!</p>`,
  styles: `
    .message {
      color: red;
    }
  `,
  encapsulation: ViewEncapsulation.Emulated,
})
export class Alert {}
```

With `Emulated`, `.message` in another component is not affected.

## 98: What is the :host selector?

`:host` targets the component's own host element (the `<app-card>` tag itself) from inside its styles.

```css
:host {
  display: block;
  padding: 1rem;
  border: 1px solid #ddd;
}

:host(.highlighted) {
  border-color: gold;
}
```

Custom element tags are `display: inline` by default, so setting `display: block` on `:host` is a common fix for layout issues.

## 99: How do you add global styles?

Put them in `src/styles.css` (or `.scss`), which is listed in `angular.json` under `styles`. These styles apply to the whole app.

```json
"styles": ["src/styles.css", "node_modules/some-lib/theme.css"]
```

You can also use `ViewEncapsulation.None` on a component, but that makes its styles global too, which is easy to forget, so prefer `styles.css`.

## 100: What is content projection?

Content projection lets a parent pass HTML into a child component. The child marks where it goes with `<ng-content>`.

```ts
@Component({
  selector: "app-card",
  template: `
    <div class="card">
      <ng-content />
    </div>
  `,
})
export class Card {}
```

```html
<app-card>
  <h2>Title</h2>
  <p>Any content can go here.</p>
</app-card>
```

This is how you build reusable wrappers like cards, dialogs and layouts.

## 101: How do you project content into multiple slots?

Use the `select` attribute on `<ng-content>` with a CSS selector.

```ts
@Component({
  selector: "app-dialog",
  template: `
    <header><ng-content select="[dialog-title]" /></header>
    <section><ng-content /></section>
    <footer><ng-content select="[dialog-actions]" /></footer>
  `,
})
export class Dialog {}
```

```html
<app-dialog>
  <h2 dialog-title>Delete file?</h2>
  <p>This can't be undone.</p>
  <div dialog-actions>
    <button>Cancel</button>
    <button>Delete</button>
  </div>
</app-dialog>
```

The `<ng-content />` without `select` gets everything that didn't match another slot. You can also put fallback content inside `<ng-content>`, shown when nothing is projected.

## 102: What is change detection?

Change detection is how Angular keeps the DOM in sync with your data. When something changes, Angular checks the bindings in the templates and updates the DOM where the values are different.

What tells Angular that something might have changed:

- A signal read in a template changes
- An event handler in the template runs
- An `async` pipe receives a new value
- `markForCheck()` is called
- In apps that use Zone.js: any async task finishes (timer, HTTP response, promise)

## 103: What is Zone.js?

Zone.js is a library that patches browser async APIs (`setTimeout`, promises, DOM events, XHR...) so Angular knows when async work finishes and can run change detection automatically.

It was required for many years. Today it's optional. Since Angular 21, new projects are created **without** Zone.js (zoneless) and rely on signals and template events instead.

## 104: What is zoneless change detection?

Zoneless means the app runs without Zone.js. Angular runs change detection only when it gets a clear signal that something changed:

- A signal read in a template is updated
- A template event listener runs
- `markForCheck()` is called (the `async` pipe does this)
- `ComponentRef.setInput()` is called

Benefits: smaller bundle, faster startup, cleaner stack traces, and fewer unnecessary checks.

```ts
// app.config.ts (new projects in Angular 21 are zoneless by default)
export const appConfig: ApplicationConfig = {
  providers: [provideZonelessChangeDetection(), provideRouter(routes)],
};
```

## 105: What is AOT compilation?

AOT (ahead-of-time) compilation means Angular compiles your templates and decorators into JavaScript during the build, not in the browser. AOT is the default for both `ng serve` and `ng build`.

Benefits:

- Faster rendering, the browser doesn't need to compile templates
- Smaller bundles, the compiler is not shipped
- Template errors are found at build time
- Better security, templates are not evaluated from strings at runtime

## 106: What is the difference between JIT and AOT?

| JIT (just-in-time)                 | AOT (ahead-of-time)                   |
| ---------------------------------- | ------------------------------------- |
| Compiles in the browser at runtime | Compiles at build time                |
| Ships the compiler to the browser  | Doesn't ship the compiler             |
| Slower startup                     | Faster startup                        |
| Template errors show up at runtime | Template errors show up at build time |

JIT is mostly a thing of the past. AOT has been the default since Angular 9.

## 107: What is Ivy?

Ivy is Angular's compilation and rendering engine, used since Angular 9 (it replaced View Engine). It compiles each component into a set of instructions that create and update the DOM.

What Ivy brought:

- Smaller bundles thanks to better tree shaking
- Faster builds since each component compiles on its own
- Better template type checking and error messages
- The base for standalone components, signals and the new control flow

## 108: What is angular.json?

`angular.json` is the workspace configuration file. It describes the projects in the workspace and how to build, serve and test them.

```json
{
  "projects": {
    "my-app": {
      "architect": {
        "build": {
          "builder": "@angular/build:application",
          "options": {
            "browser": "src/main.ts",
            "styles": ["src/styles.css"],
            "assets": [{ "glob": "**/*", "input": "public" }]
          },
          "configurations": {
            "production": { "budgets": [] },
            "development": { "optimization": false, "sourceMap": true }
          }
        },
        "serve": { "builder": "@angular/build:dev-server" }
      }
    }
  }
}
```

You configure things like global styles, assets, budgets, file replacements and build options here.

## 109: What are the most common Angular CLI commands?

| Command                    | What it does                               |
| -------------------------- | ------------------------------------------ |
| `ng new app-name`          | create a new project                       |
| `ng serve`                 | run the dev server                         |
| `ng build`                 | build for production                       |
| `ng test`                  | run unit tests                             |
| `ng e2e`                   | run end-to-end tests (after adding a tool) |
| `ng generate component x`  | generate a component (`ng g c x`)          |
| `ng generate service x`    | generate a service                         |
| `ng add @angular/material` | install and set up a library               |
| `ng update`                | update Angular and run migrations          |
| `ng lint`                  | lint the project (after adding ESLint)     |
| `ng version`               | show versions                              |

## 110: What does ng serve do?

`ng serve` builds the app in memory and starts a local dev server (by default at `http://localhost:4200`). It watches files and reloads the browser when you save. For styles and templates it can do hot module replacement without a full reload.

```bash
ng serve
ng serve --port 4300 --open
ng serve --configuration production
```

The dev server is built on Vite with esbuild. It's for development only, never use it in production.

## 111: What does ng build do?

`ng build` compiles the app for deployment. By default it uses the production configuration: AOT, minification, tree shaking and hashed file names.

```bash
ng build
```

The output goes to `dist/<project-name>/browser`. Those static files can be deployed to any web server or CDN. If SSR is enabled, there is also a `server` folder.

## 112: How do you use environment files?

Environment files let you use different values (like API URLs) for development and production. Generate them with:

```bash
ng generate environments
```

```ts
// src/environments/environment.ts (production)
export const environment = {
  apiUrl: "https://api.example.com",
};

// src/environments/environment.development.ts
export const environment = {
  apiUrl: "http://localhost:3000",
};
```

```ts
import { environment } from "../environments/environment";

http.get(`${environment.apiUrl}/users`);
```

The CLI adds `fileReplacements` to `angular.json` so the right file is used for each configuration. Don't put secrets in these files, they end up in the browser bundle.

## 113: What does ng add do?

`ng add` installs a package and runs its setup schematic, which can update config files, add providers and import styles for you.

```bash
ng add @angular/material
ng add @angular/ssr
ng add @angular-eslint/schematics
```

It saves you from doing the setup steps by hand.

## 114: What does ng update do?

`ng update` updates Angular packages and runs automatic migrations that change your code for breaking changes.

```bash
ng update                         # shows what can be updated
ng update @angular/core @angular/cli
ng update @angular/material
```

Update one major version at a time (for example 19 to 20, then 20 to 21). The site `angular.dev/update-guide` lists the steps for each version.

## 115: What are decorators in Angular?

Decorators are functions that add metadata to classes and class members. Angular reads this metadata to know how to create and use your classes.

Common class decorators:

- `@Component`
- `@Directive`
- `@Pipe`
- `@Injectable`
- `@NgModule`

Common member decorators (older style, still supported):

- `@Input`, `@Output`
- `@ViewChild`, `@ContentChild`
- `@HostListener`, `@HostBinding`

Many member decorators now have signal-based function equivalents (`input()`, `output()`, `viewChild()`...).

## 116: What kinds of selectors can a component or directive have?

```ts
// element selector (most common for components)
@Component({ selector: 'app-user' })      // <app-user />

// attribute selector (most common for directives)
@Directive({ selector: '[appHighlight]' }) // <p appHighlight>

// class selector (rare)
@Directive({ selector: '.app-box' })      // <div class="app-box">

// combinations
@Component({ selector: 'button[app-button]' }) // <button app-button>
```

Use a prefix like `app-` to avoid clashes with native HTML elements and other libraries.

## 117: How do you use one component inside another?

Add the child component to the `imports` array of the parent and use its selector in the template.

```ts
@Component({
  selector: "app-header",
  template: `<header>My Store</header>`,
})
export class Header {}

@Component({
  selector: "app-root",
  imports: [Header],
  template: `
    <app-header />
    <main>...</main>
  `,
})
export class App {}
```

If you forget the import, the build fails with an error saying the element is not known.

## 118: What can go in a standalone component's imports array?

Anything the template uses:

- Other standalone components, directives and pipes
- NgModules (for example `ReactiveFormsModule`, or an older library's module)

```ts
@Component({
  selector: "app-order-form",
  imports: [ReactiveFormsModule, CurrencyPipe, RouterLink, AddressForm],
  templateUrl: "./order-form.html",
})
export class OrderForm {}
```

Services are not added here. They are provided with `providedIn: 'root'` or in a `providers` array.

## 119: What is the host element?

The host element is the DOM element that matches the component's selector. For `<app-user-card>`, that tag is the host. The component's template is rendered inside it.

You can add classes, attributes and listeners to it with the `host` property:

```ts
@Component({
  selector: "app-chip",
  template: `<ng-content />`,
  host: {
    class: "chip",
    role: "button",
    "[class.selected]": "selected()",
    "(click)": "toggle()",
  },
})
export class Chip {
  selected = signal(false);
  toggle() {
    this.selected.update((v) => !v);
  }
}
```

## 120: What is the safe navigation operator?

The `?.` operator returns `undefined` instead of throwing an error when the left side is `null` or `undefined`.

```html
<p>{{ user?.address?.city }}</p>
```

If `user` is `null`, the expression gives `undefined` and nothing is shown. You can combine it with `??` to show a fallback:

```html
<p>{{ user?.address?.city ?? 'No city' }}</p>
```

## 121: What is the non-null assertion operator in templates?

`!` tells the type checker that a value is not `null` or `undefined`. It doesn't do anything at runtime.

```html
<p>{{ user!.name }}</p>
```

Use it only when you are sure. A better option is often to narrow the type with `@if`:

```html
@if (user(); as u) {
<p>{{ u.name }}</p>
}
```

## 122: What can you write in a template expression?

Template expressions look like JavaScript, with some limits.

Allowed:

- Property access, method calls, signal reads: `user().name`, `format(date)`
- Math and comparison operators, including `**`
- Ternary `a ? b : c`, `??`, `?.`, `!`
- Object and array literals
- Template literals: ``{{ `Hello ${name()}` }}``
- `typeof`, `in`, `void`
- Pipes with `|`

Not allowed:

- Assignments like `=` or `+=` (except in event bindings)
- `new`, `++`, `--`
- Bitwise operators `|` and `&`
- Accessing globals like `window` or `console` directly

Keep expressions simple and fast. Move complex logic to `computed()` signals.

## 123: What is $event?

In an event binding, `$event` holds the event payload. For DOM events it's the native event object. For component outputs it's the emitted value.

```html
<!-- DOM event -->
<input (input)="onInput($event)" />
<div (mousemove)="track($event.clientX, $event.clientY)"></div>

<!-- component output -->
<app-color-picker (colorChange)="color.set($event)" />
```

```ts
onInput(event: Event) {
  const value = (event.target as HTMLInputElement).value;
}
```

## 124: How do you listen to a specific key?

Angular supports key names in keyboard event bindings.

```html
<input (keyup.enter)="search()" />
<input (keydown.escape)="clear()" />
<input (keydown.shift.enter)="newLine()" />
<input (keydown.control.s)="save($event)" />
```

This saves you from checking `event.key` manually.

## 125: How do you create a custom attribute directive?

```bash
ng generate directive highlight
```

```ts
import { Directive, input } from "@angular/core";

@Directive({
  selector: "[appHighlight]",
  host: {
    "[style.backgroundColor]": "active ? color() : null",
    "(mouseenter)": "active = true",
    "(mouseleave)": "active = false",
  },
})
export class Highlight {
  color = input("yellow", { alias: "appHighlight" });
  active = false;
}
```

```html
<p appHighlight="lightblue">Hover over me</p>
```

Add `Highlight` to the `imports` of the component that uses it.

## 126: What is a structural directive?

A structural directive changes the structure of the DOM, usually by adding or removing elements based on a template. The `*` prefix is shorthand for wrapping the element in an `<ng-template>`.

```html
<p *ngIf="loggedIn">Welcome!</p>

<!-- is the same as -->
<ng-template [ngIf]="loggedIn">
  <p>Welcome!</p>
</ng-template>
```

For conditions and loops, use the built-in `@if`, `@for` and `@switch`. Custom structural directives are still useful for other cases, like showing content based on user permissions.

## 127: Should you use NgClass or class bindings?

Prefer class bindings. They do the same job, need no import, and are a bit faster.

```html
<!-- NgClass (works, but not recommended for new code) -->
<div [ngClass]="{ active: isActive, error: hasError }"></div>

<!-- class binding (recommended) -->
<div [class]="{ active: isActive, error: hasError }"></div>
<div [class.active]="isActive" [class.error]="hasError"></div>
```

## 128: Should you use NgStyle or style bindings?

Same as classes: prefer style bindings.

```html
<!-- NgStyle -->
<div [ngStyle]="{ 'font-size.px': size, color: color }"></div>

<!-- style binding (recommended) -->
<div [style]="{ 'font-size': size + 'px', color: color }"></div>
<div [style.font-size.px]="size" [style.color]="color"></div>
```

## 129: How do you show a numbered list of items?

Use `@for` with `$index`.

```html
<ol>
  @for (task of tasks(); track task.id) {
  <li>{{ $index + 1 }}. {{ task.title }}</li>
  }
</ol>
```

Or with an alias:

```html
@for (task of tasks(); track task.id; let i = $index) {
<p>Task {{ i + 1 }}: {{ task.title }}</p>
}
```

## 130: How do you add a class only when a condition is true?

```html
<li [class.done]="task.completed">{{ task.title }}</li>

<button [class.btn-primary]="isPrimary" [class.btn-secondary]="!isPrimary">
  OK
</button>
```

You can also use a ternary with `[class]`:

```html
<span [class]="score() >= 50 ? 'pass' : 'fail'">{{ score() }}</span>
```

## 131: How do you handle form submission?

Use the `(ngSubmit)` event on the `<form>`. It works with both template-driven and reactive forms, and Angular prevents the page reload for you.

```html
<form [formGroup]="form" (ngSubmit)="save()">
  <input formControlName="title" />
  <button type="submit">Save</button>
</form>
```

```ts
save() {
  if (this.form.invalid) {
    this.form.markAllAsTouched(); // show all errors
    return;
  }
  this.api.save(this.form.getRawValue()).subscribe();
}
```

## 132: Where do you put static files like images and fonts?

In new projects, put them in the `public/` folder at the project root. Files there are copied to the build output as they are.

```
public/
  favicon.ico
  images/logo.png
```

```html
<img src="images/logo.png" alt="Logo" />
```

Older projects use `src/assets/`, and the path is then `assets/images/logo.png`. Which folders are copied is set in `angular.json` under `assets`.

## 133: What is NgOptimizedImage?

`NgOptimizedImage` is a directive that applies image loading best practices for you. You use `ngSrc` instead of `src`.

```ts
@Component({
  selector: "app-hero",
  imports: [NgOptimizedImage],
  template: `
    <img
      ngSrc="images/hero.jpg"
      width="1200"
      height="600"
      priority
      alt="Hero"
    />
    <img ngSrc="images/thumb.jpg" width="200" height="200" alt="Thumb" />
  `,
})
export class Hero {}
```

What it does:

- Lazy loads images by default
- `priority` marks important images (like the main banner) to load first
- Requires `width` and `height` (or `fill`) to avoid layout shift
- Can generate `srcset` when used with an image CDN loader
- Warns in development about common mistakes

## 134: What is a single-page application (SPA)?

An SPA loads one HTML page and then updates the content with JavaScript as the user moves around, without full page reloads. Angular apps are SPAs by default.

Pros: fast navigation after the first load, app-like feel.
Cons: slower first load and weaker SEO unless you use server-side rendering or prerendering. Angular supports both through `@angular/ssr`.

## 135: What is a route guard?

A route guard is a function that decides whether navigation to or away from a route is allowed. For example, only logged-in users can open the dashboard.

```ts
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isLoggedIn() ? true : router.parseUrl("/login");
};

export const routes: Routes = [
  { path: "dashboard", component: Dashboard, canActivate: [authGuard] },
];
```

Returning a `UrlTree` (like `router.parseUrl('/login')`) redirects the user.

## 136: What is a route resolver?

A resolver loads data before the route is activated. The component gets the data when it's created.

```ts
export const productResolver: ResolveFn<Product> = (route) => {
  return inject(ProductService).getById(route.paramMap.get("id")!);
};

export const routes: Routes = [
  {
    path: "products/:id",
    component: ProductDetails,
    resolve: { product: productResolver },
  },
];
```

```ts
// with withComponentInputBinding()
export class ProductDetails {
  product = input.required<Product>();
}
```

The downside is that the user waits on the old page until the data arrives, so show a loading indicator or consider loading data in the component instead.

## 137: What is index.html in an Angular app?

It's the single HTML page the browser loads. Angular renders the app inside the root component's tag.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>MyApp</title>
    <base href="/" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  <body>
    <app-root></app-root>
  </body>
</html>
```

The build adds the script and style tags automatically. `<base href="/">` is needed for the router to build URLs correctly.

## 138: How do you run unit tests in Angular?

Run:

```bash
ng test
```

Since Angular 21, new projects use **Vitest** as the default test runner. Older projects use Karma with Jasmine (Karma is deprecated). Tests use `TestBed` to set up components and services.

```ts
import { TestBed } from "@angular/core/testing";

describe("Counter", () => {
  it("should increment", async () => {
    const fixture = TestBed.createComponent(Counter);
    await fixture.whenStable();

    fixture.nativeElement.querySelector("button").click();
    await fixture.whenStable();

    expect(fixture.nativeElement.textContent).toContain("Count: 1");
  });
});
```

## 139: What is a spec file?

A spec file (`*.spec.ts`) contains unit tests for a class. The CLI creates one next to each generated component, service, pipe, etc.

```ts
// truncate.pipe.spec.ts
describe("TruncatePipe", () => {
  const pipe = new TruncatePipe();

  it("keeps short text as is", () => {
    expect(pipe.transform("hi", 10)).toBe("hi");
  });

  it("cuts long text", () => {
    expect(pipe.transform("hello world", 5)).toBe("hello...");
  });
});
```

## 140: What are declarations, imports, exports and providers in an NgModule?

- `declarations`: components, directives and pipes that belong to this module (only non-standalone ones).
- `imports`: other modules (or standalone components) this module's templates need.
- `exports`: what this module makes available to modules that import it.
- `providers`: services available through this module's injector.
- `bootstrap`: the root component (only in the root module).

```ts
@NgModule({
  declarations: [ProductList, ProductCard],
  imports: [CommonModule, RouterModule],
  exports: [ProductList],
  providers: [ProductService],
})
export class ProductsModule {}
```

## 141: What is Angular DevTools?

Angular DevTools is a browser extension for Chrome and Firefox. It lets you:

- Browse the component tree and see inputs, outputs, signals and state
- Edit values live
- Profile change detection to find slow components
- Look at the injector tree and providers
- See the router tree and signal graphs

It works with apps running in development mode.

## 142: What is the difference between interpolation and property binding?

Interpolation is shorthand for property binding to text content, and it always converts the value to a string.

```html
<!-- these two are the same -->
<img src="{{ imageUrl }}" />
<img [src]="imageUrl" />
```

Use property binding when the value is not a string, like booleans, objects or arrays:

```html
<!-- works -->
<button [disabled]="isSaving">Save</button>
<app-chart [data]="points" />

<!-- wrong: becomes the string "false", which still disables the button -->
<button disabled="{{ isSaving }}">Save</button>
```

## 143: Where should you load data in a component?

Common options:

1. **In `ngOnInit`** with a subscription (older style).
2. **With `toSignal()`** on an HTTP Observable in a field initializer.
3. **With `httpResource()` or `resource()`**, which react to signal changes and track loading and error state.

```ts
export class UserPage {
  id = input.required<string>();

  user = httpResource<User>(() => `/api/users/${this.id()}`);
}
```

```html
@if (user.isLoading()) {
<p>Loading...</p>
} @else if (user.error()) {
<p>Could not load user.</p>
} @else if (user.hasValue()) {
<h1>{{ user.value().name }}</h1>
}
```

Avoid loading data in the constructor if it depends on inputs, because decorator inputs are not set yet at that point.

## 144: How do you set the page title?

The easiest way is the `title` property on routes:

```ts
export const routes: Routes = [
  { path: "", component: Home, title: "Home | My Shop" },
  { path: "cart", component: Cart, title: "Your cart" },
];
```

You can also set it from code with the `Title` service:

```ts
export class Product {
  private title = inject(Title);

  setTitle(name: string) {
    this.title.setTitle(`${name} | My Shop`);
  }
}
```

## 145: What is the difference between path-based and hash-based URLs?

- Path-based (default): `https://site.com/products/5`. Clean URLs, but the server must send `index.html` for every app route.
- Hash-based: `https://site.com/#/products/5`. Works on any static host without server config, since the part after `#` is never sent to the server.

```ts
provideRouter(routes, withHashLocation());
```

Use path-based URLs unless your hosting can't do the rewrite.

## 146: What is the json pipe used for?

The `json` pipe turns an object into a formatted JSON string. It is mostly for debugging.

```html
<pre>{{ form.value | json }}</pre>
<pre>{{ user() | json }}</pre>
```

## 147: How do you format dates with the date pipe?

```html
{{ order.createdAt | date }}
<!-- Oct 23, 2026 -->
{{ order.createdAt | date: 'short' }}
<!-- 10/23/26, 3:05 PM -->
{{ order.createdAt | date: 'dd.MM.yyyy HH:mm' }} {{ order.createdAt | date:
'fullDate' : 'UTC' }}
```

The input can be a `Date`, a timestamp number or an ISO string. You can change the default format and timezone for the app with the `DATE_PIPE_DEFAULT_OPTIONS` token.

## 148: How do you give an input a default value?

Pass it as the first argument of `input()`.

```ts
export class Button {
  variant = input<"primary" | "secondary">("primary");
  size = input("medium");
  disabled = input(false);
}
```

If the parent doesn't bind the input, the default is used. If the parent binds `undefined`, the value becomes `undefined`, not the default.

## 149: What is the @defer block?

`@defer` lazy loads a part of a template. The components, directives and pipes inside it are split into a separate JavaScript chunk and loaded later.

```html
@defer (on viewport) {
<app-comments [postId]="post.id" />
} @placeholder {
<p>Comments will load when you scroll here.</p>
} @loading (minimum 300ms) {
<app-spinner />
} @error {
<p>Could not load comments.</p>
}
```

Without a trigger, it loads when the browser is idle (`on idle`). This is a simple way to make the first page load lighter.

## 150: What are Angular Material and the CDK?

- **Angular Material** is the official UI component library from the Angular team, based on Material Design. It includes buttons, form fields, tables, dialogs, date pickers and more.
- **The CDK (Component Dev Kit)** is a set of lower-level tools without styling: drag and drop, overlays, virtual scrolling, accessibility helpers, layout breakpoints, and more. You can use it to build your own components.

```bash
ng add @angular/material
```

```ts
@Component({
  selector: "app-actions",
  imports: [MatButtonModule],
  template: `<button mat-flat-button>Save</button>`,
})
export class Actions {}
```

---

# Moderate Questions (151-300)

## 151: How does a signal decide that its value has changed?

By default a signal uses `Object.is()` to compare the old and new value. If they are equal, nothing is notified. For objects and arrays this means the **reference** must change.

```ts
const user = signal({ name: "Ann" });

user().name = "Bob"; // mutation: no notification, UI won't update
user.set({ name: "Bob" }); // new object: notifies
```

You can pass your own `equal` function:

```ts
const filters = signal(
  { page: 1, query: "" },
  { equal: (a, b) => a.page === b.page && a.query === b.query },
);

filters.set({ page: 1, query: "" }); // considered equal, no update
```

The same `equal` option exists on `computed()` and `linkedSignal()`.

## 152: What is untracked()?

`untracked()` reads a signal without making it a dependency of the current `computed()` or `effect()`.

```ts
export class Logger {
  currentUser = signal("Ann");
  page = signal("home");

  constructor() {
    effect(() => {
      // re-run only when page changes, not when currentUser changes
      const page = this.page();
      const user = untracked(() => this.currentUser());
      console.log(`${user} opened ${page}`);
    });
  }
}
```

It's also useful when an effect calls a function that might read signals internally, and you don't want those reads to become dependencies.

## 153: How do you run cleanup code in an effect?

The effect function receives an `onCleanup` callback. The cleanup runs before the next execution of the effect and when the effect is destroyed.

```ts
export class LiveClock {
  intervalMs = input(1000);
  now = signal(new Date());

  constructor() {
    effect((onCleanup) => {
      const id = setInterval(() => this.now.set(new Date()), this.intervalMs());
      onCleanup(() => clearInterval(id));
    });
  }
}
```

If you need to stop an effect early, keep the `EffectRef` and call `destroy()`:

```ts
const ref = effect(() => console.log(this.count()));
ref.destroy();
```

## 154: When should you avoid effect()?

Avoid effects for state that can be derived. Common mistakes:

```ts
// bad: syncing signals with an effect
fullName = signal('');
constructor() {
  effect(() => this.fullName.set(`${this.first()} ${this.last()}`));
}

// good: computed
fullName = computed(() => `${this.first()} ${this.last()}`);
```

Effects that write to signals can cause extra change detection cycles, confusing timing and even loops. Use:

- `computed()` for derived values
- `linkedSignal()` for a value that is derived but can also be overwritten
- `resource()` / `httpResource()` for async data based on signals

Use `effect()` for real side effects: logging, `localStorage`, analytics, calling a non-Angular library, or drawing on a canvas.

## 155: What is linkedSignal()?

`linkedSignal()` is a writable signal whose value resets when a source signal changes. It's useful for "selected item" style state that should reset when a list changes, but can still be set by the user.

```ts
export class ShippingPicker {
  options = input.required<ShippingOption[]>();

  // defaults to the first option, resets when options change
  selected = linkedSignal(() => this.options()[0]);

  choose(option: ShippingOption) {
    this.selected.set(option);
  }
}
```

The longer form gives you the previous value, so you can keep the selection if it's still in the new list:

```ts
selected = linkedSignal<ShippingOption[], ShippingOption>({
  source: this.options,
  computation: (newOptions, previous) =>
    newOptions.find((o) => o.id === previous?.value.id) ?? newOptions[0],
});
```

## 156: What is toSignal()?

`toSignal()` from `@angular/core/rxjs-interop` turns an Observable into a signal. It subscribes right away and unsubscribes when the injection context (for example the component) is destroyed.

```ts
export class Dashboard {
  private route = inject(ActivatedRoute);
  private http = inject(HttpClient);

  // undefined until the first value
  stats = toSignal(this.http.get<Stats>("/api/stats"));

  // with an initial value
  tab = toSignal(
    this.route.queryParamMap.pipe(map((p) => p.get("tab") ?? "overview")),
    { initialValue: "overview" },
  );
}
```

Options:

- `initialValue`: value before the Observable emits.
- `requireSync: true`: for Observables that emit synchronously (like a `BehaviorSubject`). Removes `undefined` from the type.
- `injector`: if you call it outside an injection context.

If the Observable errors, reading the signal throws that error.

## 157: What is toObservable()?

`toObservable()` turns a signal into an Observable. It uses an effect internally, so values are emitted asynchronously, and only the latest value is emitted if the signal changes several times in a row.

```ts
export class ProductSearch {
  private http = inject(HttpClient);
  query = signal("");

  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((q) => this.http.get<Product[]>(`/api/products?q=${q}`)),
    ),
    { initialValue: [] },
  );
}
```

This is the usual bridge when you need RxJS operators like `debounceTime` on signal changes.

## 158: What is resource()?

`resource()` loads async data based on signals. When the `params` change, it calls the `loader` again and cancels the previous request through an `AbortSignal`.

```ts
export class WeatherWidget {
  city = input.required<string>();

  weather = resource({
    params: () => ({ city: this.city() }),
    loader: async ({ params, abortSignal }) => {
      const res = await fetch(`/api/weather?city=${params.city}`, {
        signal: abortSignal,
      });
      if (!res.ok) throw new Error("Failed to load weather");
      return (await res.json()) as Weather;
    },
  });
}
```

```html
@if (weather.isLoading()) {
<p>Loading...</p>
} @else if (weather.error()) {
<p>Error: {{ weather.error()?.message }}</p>
} @else if (weather.hasValue()) {
<p>{{ weather.value().temp }}°C</p>
}
```

The resource gives you `value()`, `status()`, `error()`, `isLoading()`, `hasValue()`, `reload()`, `set()` and `update()`. If `params` returns `undefined`, the loader doesn't run and the resource stays idle.

## 159: What is rxResource()?

`rxResource()` is the same idea as `resource()`, but the loader returns an Observable. It's in `@angular/core/rxjs-interop`, and the loader function is called `stream`.

```ts
export class OrderDetails {
  private orders = inject(OrderService);
  id = input.required<number>();

  order = rxResource({
    params: () => this.id(),
    stream: ({ params: id }) => this.orders.getById(id),
  });
}
```

When `id` changes, the previous Observable is unsubscribed and a new one starts, similar to `switchMap`.

## 160: What is httpResource()?

`httpResource()` is a resource built on top of `HttpClient`. You give it a function that returns a URL (or a request object), and it refetches when the signals used in that function change.

```ts
export class UserProfile {
  userId = input.required<string>();

  user = httpResource<User>(() => `/api/users/${this.userId()}`);

  posts = httpResource<Post[]>(
    () => ({
      url: "/api/posts",
      params: { author: this.userId(), limit: 10 },
      headers: { "X-Client": "web" },
    }),
    { defaultValue: [] },
  );
}
```

Because it uses `HttpClient`, your interceptors run as usual. There are variants for other response types: `httpResource.text()`, `httpResource.blob()` and `httpResource.arrayBuffer()`. It's meant for reading data. For POST/PUT/DELETE calls, use `HttpClient` directly.

## 161: What are viewChild() and viewChildren()?

They are signal-based queries for elements, components or directives in the component's own template.

```ts
@Component({
  selector: "app-video-page",
  imports: [VideoPlayer],
  template: `
    <input #search />
    <app-video-player />
    @for (c of chapters; track c) {
      <app-chapter [title]="c" />
    }
  `,
})
export class VideoPage {
  searchInput = viewChild<ElementRef<HTMLInputElement>>("search");
  player = viewChild.required(VideoPlayer);
  chapterList = viewChildren(Chapter);

  focusSearch() {
    this.searchInput()?.nativeElement.focus();
  }

  play() {
    this.player().play();
  }
}
```

They update automatically when the view changes (for example when an `@if` adds or removes the element). They replace `@ViewChild` and `@ViewChildren`.

## 162: What are contentChild() and contentChildren()?

They query elements that were **projected** into the component through `<ng-content>`, not the component's own template.

```ts
@Component({
  selector: "app-tabs",
  template: `
    <div class="tab-headers">
      @for (tab of tabs(); track tab) {
        <button (click)="active.set($index)">{{ tab.label() }}</button>
      }
    </div>
    <ng-content />
  `,
})
export class Tabs {
  tabs = contentChildren(Tab);
  active = signal(0);
}
```

```html
<app-tabs>
  <app-tab label="Info">...</app-tab>
  <app-tab label="Reviews">...</app-tab>
</app-tabs>
```

By default `contentChildren` only finds direct children. Use `{ descendants: true }` to search deeper.

## 163: What are input transforms?

A transform converts the value passed by the parent before it is stored in the input. Angular ships `booleanAttribute` and `numberAttribute`.

```ts
export class Panel {
  collapsible = input(false, { transform: booleanAttribute });
  maxItems = input(10, { transform: numberAttribute });
}
```

```html
<!-- without the transform, "collapsible" would be an empty string -->
<app-panel collapsible maxItems="5" />
```

You can write your own transform function too:

```ts
tags = input([], {
  transform: (value: string | string[]) =>
    Array.isArray(value) ? value : value.split(","),
});
```

Transforms must be pure functions.

## 164: How do you expose a signal from a service as read-only?

Keep the writable signal private and expose it with `asReadonly()` or a `computed()`. This way only the service can change the state.

```ts
@Injectable({ providedIn: "root" })
export class CartStore {
  private readonly _items = signal<CartItem[]>([]);

  readonly items = this._items.asReadonly();
  readonly count = computed(() => this._items().length);

  add(item: CartItem) {
    this._items.update((items) => [...items, item]);
  }

  remove(id: number) {
    this._items.update((items) => items.filter((i) => i.id !== id));
  }
}
```

Components can read `cart.items()` but can't call `set()` on it.

## 165: How do you build a simple state service with signals?

A common pattern is one private state signal, public computed selectors, and methods to change state.

```ts
interface TodoState {
  todos: Todo[];
  filter: "all" | "active" | "done";
  loading: boolean;
}

@Injectable({ providedIn: "root" })
export class TodoStore {
  private http = inject(HttpClient);
  private state = signal<TodoState>({
    todos: [],
    filter: "all",
    loading: false,
  });

  readonly loading = computed(() => this.state().loading);
  readonly filter = computed(() => this.state().filter);
  readonly visibleTodos = computed(() => {
    const { todos, filter } = this.state();
    if (filter === "active") return todos.filter((t) => !t.done);
    if (filter === "done") return todos.filter((t) => t.done);
    return todos;
  });

  setFilter(filter: TodoState["filter"]) {
    this.state.update((s) => ({ ...s, filter }));
  }

  load() {
    this.state.update((s) => ({ ...s, loading: true }));
    this.http.get<Todo[]>("/api/todos").subscribe((todos) => {
      this.state.update((s) => ({ ...s, todos, loading: false }));
    });
  }
}
```

For bigger apps, libraries like NgRx SignalStore give you the same pattern with more structure.

## 166: When do you use computed(), linkedSignal() or effect()?

| Need                                                | Use                                            |
| --------------------------------------------------- | ---------------------------------------------- |
| A value fully derived from other signals            | `computed()`                                   |
| A derived default that the user can also change     | `linkedSignal()`                               |
| Async data based on signals                         | `resource()`, `rxResource()`, `httpResource()` |
| Doing something outside Angular when signals change | `effect()`                                     |
| Working with the DOM after render                   | `afterRenderEffect()` / `afterNextRender()`    |

A quick rule: if you are about to call `.set()` inside an `effect()`, you probably want one of the first three instead.

## 167: What are outputFromObservable() and outputToObservable()?

They connect the `output()` API with RxJS.

```ts
import {
  outputFromObservable,
  outputToObservable,
} from "@angular/core/rxjs-interop";

// turn an Observable into an output
export class Timer {
  tick = outputFromObservable(interval(1000));
}

// turn a child's output into an Observable
export class Parent {
  child = viewChild.required(Timer);

  constructor() {
    afterNextRender(() => {
      outputToObservable(this.child().tick)
        .pipe(filter((n) => n % 5 === 0))
        .subscribe((n) => console.log("every 5 seconds", n));
    });
  }
}
```

## 168: How do you update nested objects or arrays inside a signal?

Create new objects along the path you change. Don't mutate in place.

```ts
const profile = signal({
  name: "Ann",
  address: { city: "Tbilisi", zip: "0100" },
  tags: ["admin"],
});

// update nested field
profile.update((p) => ({
  ...p,
  address: { ...p.address, city: "Batumi" },
}));

// add to array
profile.update((p) => ({ ...p, tags: [...p.tags, "editor"] }));

// update one item in an array
todos.update((list) =>
  list.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
);
```

If you mutate the object and then call `set()` with the same reference, `Object.is` returns true and nothing updates.

## 169: What is the OnPush change detection strategy?

With `ChangeDetectionStrategy.OnPush`, Angular skips checking the component unless it has a reason to. This makes change detection much cheaper in large apps.

```ts
@Component({
  selector: "app-product-card",
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<h3>{{ product().name }}</h3>`,
})
export class ProductCard {
  product = input.required<Product>();
}
```

Using OnPush everywhere together with signals is the recommended setup for new code. It also works well with zoneless apps.

## 170: When is an OnPush component checked?

An OnPush component is checked when:

1. One of its inputs gets a new value (compared by reference).
2. An event handler in its template (or a host listener) runs.
3. A signal read in its template changes.
4. The `async` pipe in its template receives a new value.
5. `ChangeDetectorRef.markForCheck()` is called.

A common bug: mutating an array passed as an input. The reference is the same, so the OnPush child doesn't update.

```ts
// bad: same array reference, OnPush child won't update
this.items.push(newItem);

// good
this.items = [...this.items, newItem];
```

## 171: What is the difference between markForCheck() and detectChanges()?

Both are on `ChangeDetectorRef`.

- `markForCheck()` marks the component and its ancestors as dirty, so they will be checked in the **next** change detection run. It doesn't run anything itself.
- `detectChanges()` runs change detection **right now** for this component and its children.

```ts
export class LegacyWidget {
  private cdr = inject(ChangeDetectorRef);
  data: string[] = [];

  onDataFromThirdPartyLib(data: string[]) {
    this.data = data;
    this.cdr.markForCheck(); // safe default
  }
}
```

Prefer `markForCheck()`. Use `detectChanges()` only in special cases, like when you need the DOM updated before running more code. With signals you rarely need either.

## 172: What is the ExpressionChangedAfterItHasBeenCheckedError?

In development mode, after each change detection run, Angular checks the bindings again to make sure they didn't change. If a value changed during that time, you get this error (code `NG0100`).

Typical causes:

- Changing a value in `ngAfterViewInit` that the parent template already rendered
- A getter that returns a new value each time (like `new Date()` or `Math.random()`)
- A child updating a parent's state during rendering

```ts
// causes the error
ngAfterViewInit() {
  this.title = 'Loaded'; // template already rendered the old title
}
```

Fixes:

- Compute the value earlier (`ngOnInit`, `computed()`)
- Make the change in response to an event
- Use signals, because Angular can schedule another render when a signal changes during rendering

Don't hide it with `setTimeout`, it usually points to a data flow problem.

## 173: How do you switch an existing app to zoneless change detection?

1. Make sure components update through signals, events, `async` pipe or `markForCheck()`. Using OnPush everywhere is a good check, since OnPush components already follow these rules.
2. Add the provider and remove the Zone-based one:

```ts
export const appConfig: ApplicationConfig = {
  providers: [provideZonelessChangeDetection(), provideRouter(routes)],
};
```

3. Remove `zone.js` from the `polyfills` in `angular.json` (both build and test targets), then uninstall it.
4. Replace `NgZone.onStable` / `onMicrotaskEmpty` logic with `afterNextRender` or `afterEveryRender`.
5. Run tests. In tests, `fakeAsync` needs Zone.js, so use real async, `fixture.whenStable()`, or your test runner's fake timers.

Code that changes plain class fields from a `setTimeout` or a third-party callback will stop updating the UI until you switch it to signals or call `markForCheck()`.

## 174: What is NgZone.runOutsideAngular()?

In apps that use Zone.js, every async task triggers change detection. For frequent events (mousemove, scroll, animation frames, websockets) that can be slow. `runOutsideAngular()` runs code without triggering change detection.

```ts
export class Canvas {
  private zone = inject(NgZone);
  private host = inject(ElementRef<HTMLElement>);
  position = signal({ x: 0, y: 0 });

  constructor() {
    this.zone.runOutsideAngular(() => {
      this.host.nativeElement.addEventListener("mousemove", (e: MouseEvent) => {
        this.draw(e.clientX, e.clientY); // no change detection here
      });
    });
  }

  draw(x: number, y: number) {}
}
```

If you then need to update the UI, use `zone.run(() => ...)` or set a signal. In zoneless apps this API isn't needed.

## 175: What are detach() and reattach()?

`ChangeDetectorRef.detach()` removes the component from the change detection tree. Angular won't check it until you call `reattach()` or manually call `detectChanges()`.

```ts
export class StockTicker {
  private cdr = inject(ChangeDetectorRef);
  price = 0;

  constructor() {
    this.cdr.detach();
    setInterval(() => {
      this.price = this.fetchPrice();
      this.cdr.detectChanges(); // update only every few seconds
    }, 5000);
  }

  fetchPrice() {
    return Math.random() * 100;
  }
}
```

This is a manual optimization and is rarely needed now that signals and OnPush exist.

## 176: How do signals work with OnPush?

When a template reads a signal, the component's view becomes a consumer of that signal. When the signal changes, Angular marks that view for refresh. With OnPush, only the views that read the changed signal (and the path to them) get refreshed, not the whole tree.

```ts
@Component({
  selector: "app-counter",
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `<p>{{ count() }}</p>`,
})
export class Counter {
  count = signal(0);

  constructor() {
    setInterval(() => this.count.update((c) => c + 1), 1000);
  }
}
```

This works even without Zone.js and without calling `markForCheck()`.

## 177: How do hierarchical injectors work?

Angular has two injector trees:

1. **Environment injectors**: the root injector (`providedIn: 'root'` and `appConfig.providers`), plus child injectors created for lazy-loaded routes with `providers`.
2. **Element injectors**: created for components and directives that have `providers` or `viewProviders`.

When something calls `inject(X)`, Angular looks:

1. In the element injector of the current element, then its parent elements up to the root component.
2. If not found, in the environment injector of that place (route injector, then root).
3. Then the platform injector.
4. If still not found, it throws `NullInjectorError` (unless `optional: true`).

The first provider found wins. This lets you override a service for one part of the app.

## 178: What is the difference between providers and viewProviders?

Both create a service instance per component. The difference is who can see it:

- `providers`: visible to the component, its view children **and** content projected into it.
- `viewProviders`: visible to the component and its view children, but **not** to projected content.

```ts
@Component({
  selector: "app-form-section",
  viewProviders: [SectionState],
  template: `<app-field /> <ng-content />`,
})
export class FormSection {}
```

Here `<app-field>` (in the template) gets `SectionState`, but a component projected through `<ng-content>` doesn't. This is useful for library components that want to keep services private.

## 179: What are useClass, useValue, useFactory and useExisting?

They define how a provider creates the value for a token.

```ts
providers: [
  // use a different class
  { provide: Logger, useClass: ConsoleLogger },

  // use a fixed value
  { provide: API_URL, useValue: "https://api.example.com" },

  // use a factory function
  {
    provide: StorageService,
    useFactory: () => {
      const platformId = inject(PLATFORM_ID);
      return isPlatformBrowser(platformId)
        ? new LocalStorageService()
        : new MemoryStorageService();
    },
  },

  // alias: both tokens return the same instance
  { provide: OldLogger, useExisting: Logger },
];
```

Writing just `providers: [Logger]` is short for `{ provide: Logger, useClass: Logger }`.

## 180: What is an InjectionToken?

An `InjectionToken` is a key for values that are not classes, like strings, config objects or functions. Interfaces don't exist at runtime, so they can't be used as tokens.

```ts
export interface AppConfig {
  apiUrl: string;
  featureFlags: Record<string, boolean>;
}

export const APP_CONFIG = new InjectionToken<AppConfig>("APP_CONFIG");

// provide
providers: [
  { provide: APP_CONFIG, useValue: { apiUrl: "/api", featureFlags: {} } },
];

// use
export class Api {
  private config = inject(APP_CONFIG);
}
```

A token can also have its own default with a factory, which makes it tree-shakable:

```ts
export const WINDOW = new InjectionToken<Window>("WINDOW", {
  providedIn: "root",
  factory: () => inject(DOCUMENT).defaultView!,
});
```

## 181: What options can you pass to inject()?

```ts
// returns null instead of throwing if not found
const logger = inject(Logger, { optional: true });

// only look in the current element's injector
const ctrl = inject(NgControl, { self: true, optional: true });

// start looking in the parent, skip the current element
const parentMenu = inject(Menu, { skipSelf: true, optional: true });

// stop at the host component's injector
const form = inject(FormContainer, { host: true });
```

These replace the old `@Optional()`, `@Self()`, `@SkipSelf()` and `@Host()` parameter decorators.

## 182: What are multi providers?

With `multi: true`, several providers can add values to the same token. Injecting the token returns an array of all of them.

```ts
export const VALIDATION_RULES = new InjectionToken<Rule[]>("VALIDATION_RULES");

providers: [
  { provide: VALIDATION_RULES, useClass: RequiredRule, multi: true },
  { provide: VALIDATION_RULES, useClass: EmailRule, multi: true },
];

export class Validator {
  private rules = inject(VALIDATION_RULES); // [RequiredRule, EmailRule]
}
```

Angular uses this pattern for things like `NG_VALIDATORS`, `NG_VALUE_ACCESSOR` and the older `HTTP_INTERCEPTORS`.

## 183: Why would you provide a service at the component level?

Providing a service in a component's `providers` creates a **new instance for each instance of that component**. The instance is shared with its children and destroyed with the component.

```ts
@Injectable()
export class WizardState {
  step = signal(1);
  data = signal<Partial<Order>>({});
}

@Component({
  selector: "app-checkout-wizard",
  providers: [WizardState],
  template: `<app-step-address /> <app-step-payment />`,
})
export class CheckoutWizard {}
```

Good uses: state for one widget instance, like a wizard, an editable table row, or a dialog. Note the service uses `@Injectable()` without `providedIn`.

## 184: How do route-level providers work?

You can add `providers` to a route. Angular creates an environment injector for that route and its children. For lazy-loaded routes this keeps the service out of the main bundle.

```ts
export const ADMIN_ROUTES: Routes = [
  {
    path: "",
    providers: [AdminApi, { provide: PAGE_SIZE, useValue: 50 }],
    children: [
      { path: "users", component: AdminUsers },
      { path: "reports", component: AdminReports },
    ],
  },
];
```

Both `AdminUsers` and `AdminReports` share one `AdminApi` instance. Note: the route injector is not destroyed when you navigate away. It lives as long as the app.

## 185: What is an injection context?

An injection context is a place where `inject()` can be called. These are:

- Class constructors and field initializers of classes created by DI (components, directives, services, pipes)
- Factory functions in providers (`useFactory`, `InjectionToken` factory)
- Functional guards, resolvers and interceptors
- Code run with `runInInjectionContext()`

```ts
export class Report {
  private injector = inject(Injector);

  exportLater() {
    // inject() here would throw NG0203
    runInInjectionContext(this.injector, () => {
      const exporter = inject(ExportService);
      exporter.run();
    });
  }
}
```

You can check it in your own helpers with `assertInInjectionContext(myHelper)`.

## 186: What is DestroyRef?

`DestroyRef` lets you register cleanup callbacks for when the current component, directive or injector is destroyed. It is an alternative to `ngOnDestroy` that works well in reusable functions.

```ts
export function useInterval(ms: number, fn: () => void) {
  const id = setInterval(fn, ms);
  inject(DestroyRef).onDestroy(() => clearInterval(id));
}

export class Dashboard {
  constructor() {
    useInterval(10_000, () => this.refresh());
  }
  refresh() {}
}
```

`DestroyRef` also has a `destroyed` property to check if it was already destroyed.

## 187: What is takeUntilDestroyed()?

`takeUntilDestroyed()` is an RxJS operator from `@angular/core/rxjs-interop` that completes the Observable when the component (or other context) is destroyed.

```ts
export class Notifications {
  private socket = inject(SocketService);
  messages = signal<string[]>([]);

  constructor() {
    this.socket.messages$
      .pipe(takeUntilDestroyed())
      .subscribe((m) => this.messages.update((list) => [...list, m]));
  }
}
```

Outside an injection context, pass a `DestroyRef`:

```ts
private destroyRef = inject(DestroyRef);

ngOnInit() {
  this.form.valueChanges
    .pipe(takeUntilDestroyed(this.destroyRef))
    .subscribe(...);
}
```

Put it last in the `pipe` so that operators before it are also cleaned up.

## 188: What is provideAppInitializer()?

`provideAppInitializer()` runs a function during app startup. If it returns a Promise or Observable, Angular waits for it before rendering. It's used for loading config, restoring a session, etc.

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideAppInitializer(() => {
      const config = inject(ConfigService);
      return config.load(); // Promise<void>
    }),
  ],
};
```

It replaces the older `APP_INITIALIZER` token, which is deprecated. Keep initializers fast, because the user sees nothing until they finish.

## 189: Why use an abstract class as a DI token?

An abstract class works as both a type and a runtime token, so you can inject by the abstraction and swap the implementation.

```ts
export abstract class PaymentGateway {
  abstract charge(amount: number): Promise<void>;
}

@Injectable()
export class StripeGateway extends PaymentGateway {
  async charge(amount: number) {
    /* ... */
  }
}

// app.config.ts
providers: [{ provide: PaymentGateway, useClass: StripeGateway }];

// usage
export class Checkout {
  private payments = inject(PaymentGateway);
}
```

In tests you can provide a fake implementation easily. An interface can't do this because it disappears after compilation.

## 190: What does NullInjectorError mean?

`NullInjectorError: No provider for X!` means Angular went through all injectors and found no provider for the token.

Common causes:

- The service has `@Injectable()` without `providedIn: 'root'` and isn't in any `providers` array.
- A feature like `provideRouter()` or `provideHttpClient()` (in older versions) wasn't added to `appConfig`.
- In tests, the dependency wasn't added to `TestBed.configureTestingModule({ providers })`.
- An InjectionToken was used but never provided.

Read the error carefully, it shows the chain of dependencies, for example `R3InjectorError(Standalone[App])[UserService -> ApiClient -> ApiClient]`.

## 191: What is importProvidersFrom()?

It takes the providers out of NgModules so you can use them in a standalone app config. This is useful for libraries that still only offer NgModules.

```ts
export const appConfig: ApplicationConfig = {
  providers: [importProvidersFrom(SomeLegacyModule.forRoot({ key: "abc" }))],
};
```

When a library offers a `provideXxx()` function, use that instead.

## 192: What is the difference between functional guards and class-based guards?

Functional guards are plain functions that use `inject()`. Class guards implement interfaces like `CanActivate`. Class guards still work, but the class interfaces are deprecated, and functional guards are the recommended style.

```ts
// functional
export const adminGuard: CanActivateFn = () => {
  return inject(AuthService).hasRole("admin");
};

// class-based (older)
@Injectable({ providedIn: "root" })
export class AdminGuard implements CanActivate {
  private auth = inject(AuthService);
  canActivate() {
    return this.auth.hasRole("admin");
  }
}
```

Functional guards are shorter, easy to compose and can take parameters through a factory:

```ts
export const roleGuard = (role: string): CanActivateFn => () =>
  inject(AuthService).hasRole(role);

{ path: 'admin', component: Admin, canActivate: [roleGuard('admin')] }
```

## 193: How do you warn the user about unsaved changes before leaving a page?

Use a `canDeactivate` guard.

```ts
export interface HasUnsavedChanges {
  hasUnsavedChanges(): boolean;
}

export const unsavedChangesGuard: CanDeactivateFn<HasUnsavedChanges> = (
  component,
) => {
  return component.hasUnsavedChanges()
    ? confirm("You have unsaved changes. Leave anyway?")
    : true;
};
```

```ts
{
  path: 'profile/edit',
  component: EditProfile,
  canDeactivate: [unsavedChangesGuard],
}

export class EditProfile implements HasUnsavedChanges {
  form = inject(FormBuilder).group({ name: [''] });

  hasUnsavedChanges() {
    return this.form.dirty;
  }
}
```

The guard doesn't cover closing the tab or reloading. For that, also listen to the `beforeunload` window event.

## 194: What is canMatch?

`canMatch` decides if a route can be **matched** at all. If it returns `false`, the router keeps trying the next routes with the same path. Lazy-loaded code for a route that doesn't match is not downloaded.

```ts
export const routes: Routes = [
  {
    path: "dashboard",
    canMatch: [() => inject(AuthService).isAdmin()],
    loadComponent: () => import("./admin-dashboard"),
  },
  {
    path: "dashboard",
    loadComponent: () => import("./user-dashboard"),
  },
];
```

This is great for showing different components on the same URL based on role or feature flags. `canActivate` can't do that, it only allows or blocks.

## 195: What is canActivateChild?

`canActivateChild` runs before any child route of a route is activated. It saves you from adding the same guard to every child.

```ts
{
  path: 'admin',
  component: AdminLayout,
  canActivateChild: [adminGuard],
  children: [
    { path: 'users', component: Users },
    { path: 'settings', component: Settings },
  ],
}
```

It runs on every navigation between children, while a `canActivate` on the parent only runs when entering the parent.

## 196: How do you handle errors in a resolver?

If a resolver errors, the navigation is cancelled. Usually you catch the error and either return a fallback or redirect.

```ts
export const productResolver: ResolveFn<Product | RedirectCommand> = (
  route,
) => {
  const router = inject(Router);
  return inject(ProductService)
    .getById(route.paramMap.get("id")!)
    .pipe(
      catchError(() => of(new RedirectCommand(router.parseUrl("/not-found")))),
    );
};
```

Returning a `RedirectCommand` from a resolver tells the router to redirect instead of continuing.

## 197: How do you pass static data to a route?

Use the `data` property. The component can read it from `ActivatedRoute` or as an input with `withComponentInputBinding()`.

```ts
{
  path: 'reports',
  component: Reports,
  data: { breadcrumb: 'Reports', requiredRole: 'manager' },
}
```

```ts
export class Reports {
  // with withComponentInputBinding()
  breadcrumb = input<string>();

  // or
  private route = inject(ActivatedRoute);
  role = this.route.snapshot.data["requiredRole"];
}
```

Guards also get the route, so they can read `route.data['requiredRole']`.

## 198: What are preloading strategies?

Preloading loads lazy routes in the background after the app has started, so they are ready when the user navigates.

```ts
provideRouter(routes, withPreloading(PreloadAllModules));
```

Built-in options:

- `NoPreloading` (default)
- `PreloadAllModules`

You can write your own, for example only preloading routes marked with `data: { preload: true }`:

```ts
@Injectable({ providedIn: "root" })
export class SelectivePreloading implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>) {
    return route.data?.["preload"] ? load() : of(null);
  }
}

provideRouter(routes, withPreloading(SelectivePreloading));
```

## 199: How do you lazy load a group of routes?

Put the child routes in their own file and use `loadChildren`.

```ts
// shop/shop.routes.ts
export default [
  { path: "", component: ProductList },
  { path: ":id", component: ProductDetails },
  { path: "cart", loadComponent: () => import("./cart/cart") },
] satisfies Routes;
```

```ts
// app.routes.ts
export const routes: Routes = [
  { path: "shop", loadChildren: () => import("./shop/shop.routes") },
];
```

All components in `shop.routes.ts` go into a separate chunk that loads when the user first visits `/shop`.

## 200: What are named outlets?

A named outlet is a second `<router-outlet>` with a `name`. It lets you show a different route in another area of the page at the same time, like a side panel or a chat window.

```html
<router-outlet /> <router-outlet name="sidebar" />
```

```ts
export const routes: Routes = [
  { path: "inbox", component: Inbox },
  { path: "help", component: HelpPanel, outlet: "sidebar" },
];
```

```html
<a [routerLink]="[{ outlets: { sidebar: ['help'] } }]">Open help</a>
<a [routerLink]="[{ outlets: { sidebar: null } }]">Close help</a>
```

The URL then looks like `/inbox(sidebar:help)`.

## 201: How do you show a loading bar during navigation?

Listen to router events. A simple version with signals:

```ts
@Component({
  selector: "app-root",
  imports: [RouterOutlet],
  template: `
    @if (navigating()) {
      <div class="loading-bar"></div>
    }
    <router-outlet />
  `,
})
export class App {
  private router = inject(Router);

  navigating = toSignal(
    this.router.events.pipe(
      filter(
        (e) =>
          e instanceof NavigationStart ||
          e instanceof NavigationEnd ||
          e instanceof NavigationCancel ||
          e instanceof NavigationError,
      ),
      map((e) => e instanceof NavigationStart),
    ),
    { initialValue: false },
  );
}
```

Other useful events are `RouteConfigLoadStart` / `RouteConfigLoadEnd` (lazy chunk loading) and `ResolveStart` / `ResolveEnd`.

## 202: Can redirectTo be a function?

Yes. Since Angular 18, `redirectTo` can be a function that returns a string or a `UrlTree`. It runs in an injection context, so you can use `inject()`.

```ts
{
  path: 'legacy-user/:id',
  redirectTo: ({ params, queryParams }) => {
    const auth = inject(AuthService);
    return auth.isLoggedIn() ? `/users/${params['id']}` : '/login';
  },
}
```

## 203: What can a guard return?

A guard can return:

- `true`: allow navigation
- `false`: block navigation
- A `UrlTree`: cancel and redirect
- A `RedirectCommand`: redirect with navigation options
- An Observable or Promise of any of the above

```ts
export const authGuard: CanActivateFn = (route, state) => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.isLoggedIn()) return true;

  return new RedirectCommand(
    router.createUrlTree(["/login"], { queryParams: { returnUrl: state.url } }),
    { skipLocationChange: true },
  );
};
```

Returning a `UrlTree` is better than calling `router.navigate()` inside the guard, because the router handles it as part of the same navigation.

## 204: How do you restore scroll position and support anchor links?

Use `withInMemoryScrolling()`.

```ts
provideRouter(
  routes,
  withInMemoryScrolling({
    scrollPositionRestoration: "enabled", // top on new pages, restore on back
    anchorScrolling: "enabled", // scroll to #fragment
  }),
);
```

```html
<a routerLink="/docs" fragment="installation">Installation</a>
```

## 205: What are view transitions in the router?

The router can use the browser's View Transitions API to animate between pages.

```ts
provideRouter(routes, withViewTransitions());
```

```css
/* styles.css */
::view-transition-old(root) {
  animation: fade-out 150ms ease-in;
}
::view-transition-new(root) {
  animation: fade-in 150ms ease-out;
}
```

In browsers that don't support the API, navigation just works without the animation.

## 206: How do you navigate relative to the current route?

Use the `relativeTo` option with `ActivatedRoute`, or relative paths in `routerLink`.

```ts
export class ProductList {
  private router = inject(Router);
  private route = inject(ActivatedRoute);

  open(id: number) {
    // from /shop to /shop/42
    this.router.navigate([id], { relativeTo: this.route });
  }

  back() {
    this.router.navigate([".."], { relativeTo: this.route });
  }
}
```

In templates, `routerLink` is already relative to the current route:

```html
<a routerLink="details">Details</a>
<!-- child -->
<a routerLink="../reviews">Reviews</a>
<!-- sibling -->
<a routerLink="/home">Home</a>
<!-- absolute -->
```

## 207: What is an HTTP interceptor and how do you write one?

An interceptor is a function that runs for every request made with `HttpClient`. It can change the request, handle the response, or handle errors. Modern interceptors are plain functions of type `HttpInterceptorFn`.

```ts
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).token();

  if (!token) {
    return next(req);
  }

  const authReq = req.clone({
    setHeaders: { Authorization: `Bearer ${token}` },
  });
  return next(authReq);
};
```

```ts
provideHttpClient(withInterceptors([authInterceptor, loggingInterceptor]));
```

Interceptors run in the order they are listed for the request, and in reverse order for the response. Requests are immutable, so you always use `clone()` to change them.

## 208: How do you handle HTTP errors?

Use the `catchError` operator. You can handle errors in the service, in the component, or globally in an interceptor.

```ts
@Injectable({ providedIn: "root" })
export class ProductService {
  private http = inject(HttpClient);

  getProducts() {
    return this.http.get<Product[]>("/api/products").pipe(
      catchError((err: HttpErrorResponse) => {
        if (err.status === 0) {
          console.error("Network error", err.error);
        } else {
          console.error(`Server returned ${err.status}`, err.error);
        }
        return of([]); // fallback value
      }),
    );
  }
}
```

A global error interceptor:

```ts
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  const router = inject(Router);
  const toast = inject(ToastService);

  return next(req).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status === 401) router.navigate(["/login"]);
      else if (err.status >= 500)
        toast.show("Something went wrong on the server");
      return throwError(() => err);
    }),
  );
};
```

## 209: How do you retry a failed HTTP request?

Use the `retry` operator. You can set a count and a delay.

```ts
this.http.get<Data>("/api/data").pipe(
  retry({ count: 3, delay: 1000 }),
  catchError(() => of(null)),
);
```

For exponential backoff, `delay` can be a function:

```ts
retry({
  count: 3,
  delay: (error, retryCount) => timer(2 ** retryCount * 500),
});
```

Only retry requests that are safe to repeat (like GET). Retrying a POST could create duplicates.

## 210: How do you use HttpParams and HttpHeaders?

Both are immutable. Each `set()` or `append()` returns a new object.

```ts
const params = new HttpParams()
  .set("page", 2)
  .set("sort", "name")
  .append("tag", "new")
  .append("tag", "sale"); // ?page=2&sort=name&tag=new&tag=sale

const headers = new HttpHeaders()
  .set("Accept-Language", "en")
  .set("X-Request-Id", crypto.randomUUID());

this.http.get<Product[]>("/api/products", { params, headers });
```

For simple cases you can pass plain objects:

```ts
this.http.get("/api/products", {
  params: { page: 2, sort: "name" },
  headers: { "Accept-Language": "en" },
});
```

## 211: What is HttpContext?

`HttpContext` lets you attach metadata to a request that interceptors can read. It is not sent to the server.

```ts
export const SKIP_AUTH = new HttpContextToken<boolean>(() => false);

// mark a request
this.http.get("/api/public/news", {
  context: new HttpContext().set(SKIP_AUTH, true),
});

// read it in an interceptor
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  if (req.context.get(SKIP_AUTH)) {
    return next(req);
  }
  // add the token...
  return next(req);
};
```

Typical uses: skipping auth, disabling the global spinner, or setting a custom retry count for one request.

## 212: What does withFetch() do?

By default `HttpClient` uses `XMLHttpRequest`. `withFetch()` makes it use the browser's `fetch` API instead.

```ts
provideHttpClient(withFetch());
```

Reasons to use it:

- It is recommended for SSR, because `fetch` works natively in Node.js and other server runtimes.
- It is the modern API.

One difference: with `fetch`, upload progress events are not available. If you need upload progress, keep the default XHR backend for those requests.

## 213: How do you get the full HTTP response, not just the body?

Use `observe: 'response'`. You get an `HttpResponse` with status, headers and body.

```ts
this.http
  .get<User[]>("/api/users", { observe: "response" })
  .subscribe((res) => {
    const total = Number(res.headers.get("X-Total-Count"));
    const users = res.body ?? [];
    console.log(res.status, total, users);
  });
```

You can also set `responseType` to `'text'`, `'blob'` or `'arraybuffer'` for non-JSON responses:

```ts
this.http.get("/api/report.pdf", { responseType: "blob" });
```

## 214: How do you track upload progress?

Use `reportProgress: true` and `observe: 'events'`, then check the event type.

```ts
upload(file: File) {
  const formData = new FormData();
  formData.append('file', file);

  return this.http
    .post('/api/upload', formData, { reportProgress: true, observe: 'events' })
    .pipe(
      map((event) => {
        if (event.type === HttpEventType.UploadProgress && event.total) {
          return Math.round((100 * event.loaded) / event.total);
        }
        if (event.type === HttpEventType.Response) {
          return 100;
        }
        return 0;
      }),
    );
}
```

Upload progress needs the default XHR backend, not `withFetch()`.

## 215: How do you cancel an HTTP request?

Unsubscribing from the Observable cancels the request. In practice you rarely do it by hand:

- `switchMap` cancels the previous request when a new value arrives.
- `takeUntilDestroyed()` cancels when the component is destroyed.
- `rxResource` and `httpResource` cancel the old request when params change.

```ts
// typeahead: only the latest request matters
results = toSignal(
  toObservable(this.query).pipe(
    debounceTime(300),
    switchMap((q) => this.http.get<Item[]>("/api/search", { params: { q } })),
  ),
  { initialValue: [] },
);
```

## 216: How does Angular protect against XSRF/CSRF?

`HttpClient` has built-in support. If the server sets a cookie named `XSRF-TOKEN`, Angular reads it and sends it back in the `X-XSRF-TOKEN` header on mutating requests (POST, PUT, PATCH, DELETE) to relative URLs. The server then checks they match.

```ts
provideHttpClient(
  withXsrfConfiguration({
    cookieName: "MY-XSRF-COOKIE",
    headerName: "X-MY-XSRF-HEADER",
  }),
);
```

You can turn it off with `withNoXsrfProtection()`. The server side still has to generate and verify the token.

## 217: How do you show a global loading indicator for HTTP requests?

Use an interceptor that counts active requests and a service with a signal.

```ts
@Injectable({ providedIn: "root" })
export class LoadingService {
  private active = signal(0);
  readonly isLoading = computed(() => this.active() > 0);

  start() {
    this.active.update((n) => n + 1);
  }
  stop() {
    this.active.update((n) => Math.max(0, n - 1));
  }
}

export const loadingInterceptor: HttpInterceptorFn = (req, next) => {
  const loading = inject(LoadingService);
  loading.start();
  return next(req).pipe(finalize(() => loading.stop()));
};
```

```html
@if (loading.isLoading()) { <app-spinner /> }
```

`finalize` runs on success, error and cancel, so the counter stays correct.

## 218: What is the difference between switchMap, mergeMap, concatMap and exhaustMap?

All four map each value to an inner Observable. They differ in what happens when a new value arrives while the previous inner Observable is still running.

| Operator     | Behavior                                      | Typical use                                       |
| ------------ | --------------------------------------------- | ------------------------------------------------- |
| `switchMap`  | cancels the previous, starts the new          | search typeahead, route param changes             |
| `mergeMap`   | runs all in parallel                          | independent requests, e.g. deleting several items |
| `concatMap`  | queues, runs one after another in order       | saving changes in order                           |
| `exhaustMap` | ignores new values until the current finishes | login or submit button (avoid double submit)      |

```ts
// avoid double-submit
this.submit$
  .pipe(exhaustMap(() => this.api.save(this.form.getRawValue())))
  .subscribe();
```

## 219: What types of Subjects are there?

A Subject is both an Observable and an Observer. You can push values into it with `next()`.

- `Subject`: no initial value, subscribers only get values emitted after they subscribe.
- `BehaviorSubject`: has a current value, new subscribers get the latest value right away.
- `ReplaySubject(n)`: replays the last `n` values to new subscribers.
- `AsyncSubject`: emits only the last value, when it completes.

```ts
const user$ = new BehaviorSubject<User | null>(null);
user$.subscribe((u) => console.log("A", u)); // A null
user$.next({ id: 1, name: "Ann" }); // A {id:1...}
user$.subscribe((u) => console.log("B", u)); // B {id:1...}
console.log(user$.value);
```

## 220: Should you use BehaviorSubject or signals for state in services?

For synchronous state that the UI reads, signals are now the better default:

- No subscriptions to manage
- Reading is just `state()`
- Works with OnPush and zoneless automatically
- `computed()` is simpler than `combineLatest` + `map`

```ts
// before
private userSubject = new BehaviorSubject<User | null>(null);
user$ = this.userSubject.asObservable();
isLoggedIn$ = this.user$.pipe(map((u) => !!u));

// after
private _user = signal<User | null>(null);
user = this._user.asReadonly();
isLoggedIn = computed(() => !!this._user());
```

Keep RxJS for streams of events over time: websockets, debounced input, polling, complex async coordination.

## 221: What does shareReplay do?

`shareReplay` shares one subscription to the source between many subscribers and replays the last value(s) to new subscribers. It's often used to cache an HTTP call.

```ts
@Injectable({ providedIn: "root" })
export class CountryService {
  private http = inject(HttpClient);

  readonly countries$ = this.http
    .get<Country[]>("/api/countries")
    .pipe(shareReplay({ bufferSize: 1, refCount: true }));
}
```

Without it, each `subscribe()` or `async` pipe would send a new request. With `refCount: true`, the source is unsubscribed when nobody is listening. With `refCount: false`, the cached value stays forever (which is fine for static data, but can leak for long-lived streams).

## 222: How do you build a search box that waits for the user to stop typing?

```ts
@Component({
  selector: "app-user-search",
  imports: [ReactiveFormsModule],
  template: `
    <input [formControl]="query" placeholder="Search users" />
    @for (user of results(); track user.id) {
      <p>{{ user.name }}</p>
    }
  `,
})
export class UserSearch {
  private http = inject(HttpClient);
  query = new FormControl("", { nonNullable: true });

  results = toSignal(
    this.query.valueChanges.pipe(
      debounceTime(300),
      map((q) => q.trim()),
      distinctUntilChanged(),
      switchMap((q) =>
        q.length < 2
          ? of([])
          : this.http
              .get<User[]>("/api/users", { params: { q } })
              .pipe(catchError(() => of([]))),
      ),
    ),
    { initialValue: [] },
  );
}
```

`debounceTime` waits for a pause, `distinctUntilChanged` skips repeats, `switchMap` cancels old requests, and `catchError` inside `switchMap` keeps the stream alive after an error.

## 223: What is the difference between combineLatest, forkJoin and zip?

- `forkJoin`: waits for all Observables to **complete**, then emits one array/object with their last values. Good for running several HTTP calls in parallel.
- `combineLatest`: emits every time any source emits (after all have emitted once), with the latest value of each. Good for combining filters.
- `zip`: pairs values by index: first with first, second with second.

```ts
// parallel requests
forkJoin({
  user: this.http.get<User>("/api/me"),
  settings: this.http.get<Settings>("/api/settings"),
}).subscribe(({ user, settings }) => {
  /* ... */
});

// react to several streams
combineLatest([this.category$, this.sort$]).pipe(
  switchMap(([category, sort]) => this.api.getProducts(category, sort)),
);
```

If one source in `forkJoin` errors, the whole thing errors. If one never completes, `forkJoin` never emits.

## 224: What is the difference between hot and cold Observables?

- **Cold**: the producer starts for each subscriber. Every subscriber gets its own run. `HttpClient` calls are cold, two subscriptions mean two requests.
- **Hot**: the producer runs independently of subscribers and they all share it. DOM events, Subjects and websockets are hot.

```ts
const req$ = this.http.get("/api/data");
req$.subscribe(); // request 1
req$.subscribe(); // request 2

const shared$ = req$.pipe(shareReplay(1));
shared$.subscribe(); // request
shared$.subscribe(); // reuses the result
```

## 225: When should you use signals and when RxJS?

Use **signals** for:

- Component and service state
- Derived values
- Anything the template reads

Use **RxJS** for:

- Events over time (typing, scrolling, websockets)
- Time-based operators (debounce, throttle, interval)
- Complex async flows (cancellation, retry, race)

Bridge them with `toSignal()`, `toObservable()`, `rxResource()`, `outputFromObservable()` and `takeUntilDestroyed()`. A common pattern is: RxJS for the pipeline, `toSignal()` at the end for the template.

## 226: How do you write a custom validator for reactive forms?

A validator is a function that takes a control and returns `null` if valid, or an error object if not.

```ts
export function forbiddenName(name: string): ValidatorFn {
  return (control: AbstractControl): ValidationErrors | null => {
    const forbidden = control.value?.toLowerCase() === name.toLowerCase();
    return forbidden ? { forbiddenName: { value: control.value } } : null;
  };
}

export function noWhitespace(
  control: AbstractControl,
): ValidationErrors | null {
  return (control.value ?? "").trim().length === 0
    ? { whitespace: true }
    : null;
}
```

```ts
username = new FormControl("", [
  Validators.required,
  noWhitespace,
  forbiddenName("admin"),
]);
```

```html
@if (username.hasError('forbiddenName')) {
<small>"{{ username.getError('forbiddenName').value }}" is not allowed.</small>
}
```

## 227: How do you write an async validator?

An async validator returns an Observable or Promise of `ValidationErrors | null`. It runs only after all sync validators pass.

```ts
export function usernameTaken(): AsyncValidatorFn {
  const http = inject(HttpClient);
  return (control) =>
    timer(400).pipe(
      switchMap(() =>
        http.get<{ taken: boolean }>("/api/username-check", {
          params: { name: control.value },
        }),
      ),
      map((res) => (res.taken ? { usernameTaken: true } : null)),
      catchError(() => of(null)),
    );
}
```

```ts
export class Signup {
  username = new FormControl("", {
    validators: [Validators.required],
    asyncValidators: [usernameTaken()],
    updateOn: "blur",
  });
}
```

While it runs, the control's status is `PENDING`. The `timer` debounces calls, because each new value cancels the previous Observable.

## 228: How do you validate two fields together, like password and confirm password?

Put the validator on the `FormGroup` that contains both controls.

```ts
export const passwordsMatch: ValidatorFn = (group: AbstractControl) => {
  const password = group.get("password")?.value;
  const confirm = group.get("confirm")?.value;
  return password === confirm ? null : { passwordsMismatch: true };
};

export class ChangePassword {
  form = inject(NonNullableFormBuilder).group(
    {
      password: ["", [Validators.required, Validators.minLength(8)]],
      confirm: ["", Validators.required],
    },
    { validators: passwordsMatch },
  );
}
```

```html
@if (form.hasError('passwordsMismatch') && form.controls.confirm.touched) {
<small>Passwords don't match.</small>
}
```

## 229: How do you use FormArray for dynamic fields?

`FormArray` holds a list of controls or groups, so the user can add and remove items.

```ts
@Component({
  selector: "app-invoice-form",
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <div formArrayName="lines">
        @for (line of lines.controls; track line; let i = $index) {
          <div [formGroupName]="i">
            <input formControlName="description" />
            <input formControlName="amount" type="number" />
            <button type="button" (click)="lines.removeAt(i)">Remove</button>
          </div>
        }
      </div>
      <button type="button" (click)="addLine()">Add line</button>
    </form>
  `,
})
export class InvoiceForm {
  private fb = inject(NonNullableFormBuilder);

  form = this.fb.group({
    lines: this.fb.array([this.createLine()]),
  });

  get lines() {
    return this.form.controls.lines;
  }

  createLine() {
    return this.fb.group({
      description: ["", Validators.required],
      amount: [0, Validators.min(0)],
    });
  }

  addLine() {
    this.lines.push(this.createLine());
  }
}
```

## 230: What are typed reactive forms?

Since Angular 14, reactive forms are strongly typed. The type is inferred from the initial values.

```ts
const form = new FormGroup({
  name: new FormControl(""), // FormControl<string | null>
  age: new FormControl(0, { nonNullable: true }), // FormControl<number>
});

form.value; // Partial<{ name: string | null; age: number }>
form.getRawValue(); // { name: string | null; age: number }
form.controls.age.setValue("x"); // compile error
```

Notes:

- `value` is `Partial` because disabled controls are left out.
- Controls are nullable by default because `reset()` sets them to `null`. Use `nonNullable: true` or `NonNullableFormBuilder` to avoid that.
- `UntypedFormGroup` / `UntypedFormControl` exist for old code that needs `any`.

## 231: What does nonNullable do on a form control?

It makes `reset()` return the control to its **initial value** instead of `null`, and removes `null` from the type.

```ts
const qty = new FormControl(1, { nonNullable: true });
qty.setValue(5);
qty.reset();
console.log(qty.value); // 1, not null
```

With `FormBuilder`:

```ts
private fb = inject(FormBuilder);
form = this.fb.nonNullable.group({ qty: 1, note: '' });

// or
private nfb = inject(NonNullableFormBuilder);
form2 = this.nfb.group({ qty: 1, note: '' });
```

## 232: What is FormRecord?

`FormRecord` is a typed group where the keys are not known in advance, but all controls have the same type.

```ts
const permissions = new FormRecord<FormControl<boolean>>({});

for (const perm of ["read", "write", "delete"]) {
  permissions.addControl(perm, new FormControl(false, { nonNullable: true }));
}

permissions.value; // { read?: boolean; write?: boolean; delete?: boolean }
```

Use `FormGroup` when you know the keys, and `FormRecord` for dynamic keys like settings maps.

## 233: What is the difference between setValue() and patchValue()?

- `setValue()` needs a value for **every** control in the group. Missing or extra keys throw an error.
- `patchValue()` updates only the controls you pass and ignores the rest.

```ts
form = new FormGroup({
  name: new FormControl(""),
  email: new FormControl(""),
});

this.form.setValue({ name: "Ann", email: "ann@mail.com" }); // ok
this.form.setValue({ name: "Ann" }); // error
this.form.patchValue({ name: "Ann" }); // ok
```

Both accept `{ emitEvent: false }` if you don't want `valueChanges` to fire.

## 234: How do you react to form value and status changes?

Use `valueChanges`, `statusChanges`, or the unified `events` Observable (added in Angular 18).

```ts
export class Profile {
  form = inject(NonNullableFormBuilder).group({ name: [""], country: [""] });

  constructor() {
    this.form.controls.country.valueChanges
      .pipe(takeUntilDestroyed())
      .subscribe((country) => this.loadCities(country));

    this.form.events.pipe(takeUntilDestroyed()).subscribe((event) => {
      if (event instanceof TouchedChangeEvent)
        console.log("touched", event.touched);
      if (event instanceof PristineChangeEvent)
        console.log("pristine", event.pristine);
      if (event instanceof FormSubmittedEvent) console.log("submitted");
      if (event instanceof FormResetEvent) console.log("reset");
    });
  }

  loadCities(country: string) {}
}
```

`events` lets you react to touched and pristine changes, which `valueChanges` and `statusChanges` don't cover.

## 235: What is updateOn in forms?

`updateOn` sets when a control updates its value and runs validation:

- `'change'` (default): on every keystroke
- `'blur'`: when the input loses focus
- `'submit'`: when the form is submitted

```ts
email = new FormControl("", {
  validators: [Validators.email],
  updateOn: "blur",
});

form = new FormGroup({/* ... */}, { updateOn: "submit" });
```

In template-driven forms: `[ngModelOptions]="{ updateOn: 'blur' }"`. Using `'blur'` is a good choice for expensive async validators.

## 236: What is ControlValueAccessor?

`ControlValueAccessor` is an interface that lets your custom component work with `formControl`, `formControlName` and `ngModel`, like a native input.

```ts
@Component({
  selector: "app-star-rating",
  template: `
    @for (star of [1, 2, 3, 4, 5]; track star) {
      <button type="button" [disabled]="disabled()" (click)="select(star)">
        {{ star <= value() ? "★" : "☆" }}
      </button>
    }
  `,
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => StarRating),
      multi: true,
    },
  ],
})
export class StarRating implements ControlValueAccessor {
  value = signal(0);
  disabled = signal(false);
  private onChange: (v: number) => void = () => {};
  private onTouched: () => void = () => {};

  writeValue(value: number): void {
    this.value.set(value ?? 0);
  }
  registerOnChange(fn: (v: number) => void): void {
    this.onChange = fn;
  }
  registerOnTouched(fn: () => void): void {
    this.onTouched = fn;
  }
  setDisabledState(isDisabled: boolean): void {
    this.disabled.set(isDisabled);
  }

  select(star: number) {
    this.value.set(star);
    this.onChange(star);
    this.onTouched();
  }
}
```

```html
<app-star-rating formControlName="rating" />
```

## 237: How do you disable a reactive form control?

Use `disable()` / `enable()` in code, or set `disabled` when creating the control. Don't use the `[disabled]` attribute together with `formControlName`, Angular warns about it.

```ts
form = new FormGroup({
  email: new FormControl({ value: '', disabled: true }),
  newsletter: new FormControl(false),
});

constructor() {
  this.form.controls.newsletter.valueChanges
    .pipe(takeUntilDestroyed())
    .subscribe((on) => {
      on ? this.form.controls.email.enable() : this.form.controls.email.disable();
    });
}
```

Disabled controls are skipped by validation and left out of `form.value`. Use `form.getRawValue()` to include them.

## 238: When do you choose template-driven forms vs reactive forms?

|                | Template-driven                              | Reactive                             |
| -------------- | -------------------------------------------- | ------------------------------------ |
| Form model     | created by directives in the template        | created in TypeScript                |
| Data flow      | async (model updates after change detection) | sync                                 |
| Typing         | weak                                         | strong (typed forms)                 |
| Dynamic fields | harder                                       | easy with `FormArray` / `FormRecord` |
| Testing        | needs rendering                              | can test the model without the DOM   |
| Best for       | small, simple forms                          | complex forms, dynamic validation    |

Signal forms are a third option for new code, but they are experimental in Angular 21.

## 239: How do you validate and submit with signal forms?

Validation rules go in the schema function passed to `form()`. Use `validate()` for custom rules and `submit()` to handle submission.

```ts
import {
  form,
  FormField,
  required,
  minLength,
  validate,
  submit,
} from "@angular/forms/signals";

interface Signup {
  email: string;
  password: string;
  confirm: string;
}

@Component({
  selector: "app-signup",
  imports: [FormField],
  template: `
    <form (submit)="onSubmit($event)">
      <input [formField]="f.email" type="email" />
      <input [formField]="f.password" type="password" />
      <input [formField]="f.confirm" type="password" />
      @for (err of f.confirm().errors(); track err.kind) {
        <small>{{ err.message }}</small>
      }
      <button [disabled]="f().invalid()">Sign up</button>
    </form>
  `,
})
export class SignupForm {
  private api = inject(AuthApi);
  model = signal<Signup>({ email: "", password: "", confirm: "" });

  f = form(this.model, (p) => {
    required(p.email);
    required(p.password);
    minLength(p.password, 8, { message: "At least 8 characters" });
    validate(p.confirm, ({ value, valueOf }) =>
      value() === valueOf(p.password)
        ? null
        : { kind: "mismatch", message: "Passwords must match" },
    );
  });

  onSubmit(event: Event) {
    event.preventDefault();
    submit(this.f, async () => {
      await this.api.signup(this.model());
    });
  }
}
```

The form's data lives in your `model` signal, and each field gives you state signals like `value()`, `valid()`, `errors()`, `touched()` and `dirty()`. The API is experimental, so check the docs for your exact version.

## 240: How do you show all validation errors when the user clicks submit?

Call `markAllAsTouched()` so every control shows its errors, then stop if the form is invalid.

```ts
save() {
  if (this.form.invalid) {
    this.form.markAllAsTouched();
    return;
  }
  this.api.save(this.form.getRawValue()).subscribe();
}
```

You can also check `form.submitted` (or `ngForm.submitted` for template-driven forms) in the template, and show errors when `control.touched || form.submitted`.

## 241: How do you use ngTemplateOutlet with a context?

`ngTemplateOutlet` renders an `ng-template` and can pass data to it through a context object. `$implicit` is the default value.

```ts
@Component({
  selector: "app-list",
  imports: [NgTemplateOutlet],
  template: `
    @for (item of items(); track item.id) {
      <ng-container
        [ngTemplateOutlet]="itemTemplate() ?? defaultTpl"
        [ngTemplateOutletContext]="{ $implicit: item, index: $index }"
      />
    }
    <ng-template #defaultTpl let-item>{{ item.name }}</ng-template>
  `,
})
export class List<T extends { id: number; name: string }> {
  items = input.required<T[]>();
  itemTemplate = input<TemplateRef<{ $implicit: T; index: number }>>();
}
```

```html
<app-list [items]="users" [itemTemplate]="userTpl" />

<ng-template #userTpl let-user let-i="index">
  <strong>{{ i + 1 }}.</strong> {{ user.name }} ({{ user.email }})
</ng-template>
```

This lets the parent decide how each item looks while the child handles the logic.

## 242: How do you create a component dynamically?

Use `ViewContainerRef.createComponent()`. Since Angular 20 you can pass `bindings` for inputs and outputs.

```ts
@Component({
  selector: "app-alert-host",
  template: `<ng-container #host />`,
})
export class AlertHost {
  private vcr = viewChild.required("host", { read: ViewContainerRef });
  message = signal("Saved!");

  show() {
    this.vcr().clear();
    this.vcr().createComponent(Alert, {
      bindings: [
        inputBinding("message", this.message),
        inputBinding("type", () => "success"),
        outputBinding("closed", () => this.vcr().clear()),
      ],
    });
  }
}
```

The older way still works:

```ts
const ref = this.vcr().createComponent(Alert);
ref.setInput("message", "Saved!");
ref.instance.closed.subscribe(() => ref.destroy());
```

Use `ref.setInput()` rather than setting `ref.instance.message` directly, so change detection is triggered correctly.

## 243: What is NgComponentOutlet?

`NgComponentOutlet` renders a component chosen at runtime, from the template.

```ts
@Component({
  selector: "app-widget-area",
  imports: [NgComponentOutlet],
  template: `
    @for (w of widgets(); track w.id) {
      <ng-container *ngComponentOutlet="w.component; inputs: w.inputs" />
    }
  `,
})
export class WidgetArea {
  widgets = signal([
    { id: 1, component: WeatherWidget, inputs: { city: "Tbilisi" } },
    { id: 2, component: NewsWidget, inputs: { count: 5 } },
  ]);
}
```

Combined with `import()`, you can lazy load the component class too.

## 244: What is the host property and how is it different from @HostBinding and @HostListener?

The `host` property in `@Component` or `@Directive` is the recommended way to bind to the host element. `@HostBinding` and `@HostListener` still work but are kept mainly for backward compatibility.

```ts
// recommended
@Directive({
  selector: "[appDropzone]",
  host: {
    class: "dropzone",
    "[class.over]": "isOver()",
    "[attr.aria-dropeffect]": '"copy"',
    "(dragover)": "onDragOver($event)",
    "(dragleave)": "isOver.set(false)",
    "(window:resize)": "onResize()",
  },
})
export class Dropzone {
  isOver = signal(false);
  onDragOver(e: DragEvent) {
    e.preventDefault();
    this.isOver.set(true);
  }
  onResize() {}
}

// older style
@Directive({ selector: "[appDropzoneOld]" })
export class DropzoneOld {
  @HostBinding("class.over") isOver = false;
  @HostListener("dragover", ["$event"]) onDragOver(e: DragEvent) {}
}
```

You can listen to global targets with `window:`, `document:` and `body:` prefixes.

## 245: How do you access the DOM safely with ElementRef and Renderer2?

`ElementRef` gives you the host's native element. `Renderer2` changes the DOM through an abstraction that also works on the server.

```ts
@Directive({ selector: "[appAutoResize]" })
export class AutoResize {
  private el = inject<ElementRef<HTMLTextAreaElement>>(ElementRef);
  private renderer = inject(Renderer2);

  constructor() {
    this.renderer.listen(this.el.nativeElement, "input", () => this.resize());
  }

  private resize() {
    const ta = this.el.nativeElement;
    this.renderer.setStyle(ta, "height", "auto");
    this.renderer.setStyle(ta, "height", `${ta.scrollHeight}px`);
  }
}
```

Tips:

- Prefer template bindings and the `host` property over DOM access.
- If you must touch the DOM, do it in `afterNextRender()` / `afterEveryRender()` so it only runs in the browser after rendering.
- Never insert user content with `innerHTML` directly through `nativeElement`, it skips Angular's sanitization.

## 246: In what order do parent and child lifecycle hooks run?

For a parent with one child in its template, on first render:

1. Parent `constructor`
2. Parent `ngOnChanges` (if it has inputs)
3. Parent `ngOnInit`
4. Parent `ngDoCheck`
5. Parent `ngAfterContentInit`, `ngAfterContentChecked`
6. Child `constructor`
7. Child `ngOnChanges`, `ngOnInit`, `ngDoCheck`
8. Child `ngAfterContentInit`, `ngAfterContentChecked`
9. Child `ngAfterViewInit`, `ngAfterViewChecked`
10. Parent `ngAfterViewInit`, `ngAfterViewChecked`

So the parent's view hooks run only after all children's view hooks. On destroy, children's `ngOnDestroy` runs before the parent's.

## 247: When is a view query available?

A view query result is ready after the view is created, which means in `ngAfterViewInit` (or later). In the constructor and `ngOnInit` it's usually not available yet.

With signal queries you don't need to care much about timing, because the signal updates when the result changes:

```ts
export class ChartHost {
  canvas = viewChild.required<ElementRef<HTMLCanvasElement>>("canvas");
  data = input.required<number[]>();

  constructor() {
    afterRenderEffect(() => {
      drawChart(this.canvas().nativeElement, this.data());
    });
  }
}
```

With the old `@ViewChild`, you could set `{ static: true }` to have it available in `ngOnInit`, but only if the element is not inside a conditional block.

## 248: What are afterNextRender() and afterEveryRender()?

They register callbacks that run after Angular has rendered the DOM. They only run in the browser, never during server-side rendering.

- `afterNextRender()`: runs once, after the next render. Good for one-time setup like starting a chart library.
- `afterEveryRender()`: runs after every render. Use carefully, it can hurt performance.

```ts
export class MapView {
  private el = inject(ElementRef<HTMLElement>);
  private map?: ThirdPartyMap;

  constructor() {
    afterNextRender({
      write: () => {
        this.map = new ThirdPartyMap(this.el.nativeElement);
      },
    });
  }
}
```

You can split work into phases (`earlyRead`, `write`, `mixedReadWrite`, `read`) to avoid layout thrashing. `afterEveryRender` was called `afterRender` before Angular 20. There's also `afterRenderEffect()`, which reruns only when the signals it reads change.

## 249: How do components communicate through a service?

When two components are not parent and child, a shared service is the cleanest way.

```ts
@Injectable({ providedIn: "root" })
export class SelectionService {
  private _selectedId = signal<number | null>(null);
  readonly selectedId = this._selectedId.asReadonly();

  select(id: number) {
    this._selectedId.set(id);
  }
}

// in a list component
export class ProductList {
  selection = inject(SelectionService);
}
// template: (click)="selection.select(p.id)"

// in a details panel somewhere else
export class ProductPanel {
  private selection = inject(SelectionService);
  private http = inject(HttpClient);

  product = httpResource<Product>(() => {
    const id = this.selection.selectedId();
    return id ? `/api/products/${id}` : undefined;
  });
}
```

Returning `undefined` from the request function keeps the resource idle.

## 250: How do default content and ngProjectAs work with ng-content?

Since Angular 18 you can put fallback content inside `<ng-content>`. It's shown if nothing matches that slot.

```html
<!-- card.html -->
<header>
  <ng-content select="[card-title]">Untitled</ng-content>
</header>
<ng-content />
```

`ngProjectAs` lets an element match a slot it wouldn't normally match, usually when you wrap content in `ng-container`:

```html
<app-card>
  <ng-container ngProjectAs="[card-title]">
    @if (user()) {
    <h2>{{ user()!.name }}</h2>
    }
  </ng-container>
  <p>Body text</p>
</app-card>
```

## 251: What triggers can @defer use?

| Trigger             | Loads when                                                                  |
| ------------------- | --------------------------------------------------------------------------- |
| `on idle` (default) | the browser is idle (`requestIdleCallback`)                                 |
| `on viewport`       | the placeholder (or a referenced element) enters the viewport               |
| `on interaction`    | the user clicks or presses a key on the placeholder or a referenced element |
| `on hover`          | the user hovers or focuses the placeholder or a referenced element          |
| `on immediate`      | right after the rest of the page renders                                    |
| `on timer(2s)`      | after the given time                                                        |
| `when condition`    | the expression becomes true (one time)                                      |

```html
<button #loadBtn>Show comments</button>

@defer (on interaction(loadBtn); on timer(10s)) {
<app-comments />
} @placeholder {
<p>Comments are hidden</p>
}
```

Multiple triggers are combined with OR.

## 252: What is prefetching in @defer?

Prefetching downloads the deferred code earlier than it's rendered, so it shows instantly when the main trigger fires.

```html
@defer (on interaction; prefetch on idle) {
<app-rich-editor />
} @placeholder {
<div class="editor-placeholder">Click to edit</div>
}
```

Here the code downloads when the browser is idle, but the editor is only created when the user interacts with the placeholder.

## 253: What are the rules for code to be lazy loaded with @defer?

For a dependency inside `@defer` to go into a separate chunk:

- It must be standalone (component, directive or pipe).
- It must not be referenced anywhere outside `@defer` blocks in the same file, for example not used in a `viewChild()` query or imported for another reason.

If these rules aren't met, the code is still loaded eagerly and the block only delays rendering.

Other details:

- `@placeholder` and `@loading` accept `minimum` to avoid flicker: `@loading (after 100ms; minimum 1s)`.
- Their content is loaded eagerly, so keep it light.
- During SSR, `@defer` blocks render their placeholder (unless you use incremental hydration).

## 254: What is the difference between pure and impure pipes?

- **Pure** (default): runs only when the input value changes (by reference for objects). Cheap.
- **Impure** (`pure: false`): runs on every change detection cycle. Can be slow.

```ts
@Pipe({ name: "filterActive", pure: false })
export class FilterActivePipe implements PipeTransform {
  transform(items: Item[]) {
    return items.filter((i) => i.active);
  }
}
```

Avoid impure pipes. Usually you can keep the pipe pure and update data immutably, or replace the pipe with a `computed()` signal. The `async` pipe is a built-in impure pipe.

## 255: Why is calling a method in a template a problem?

A method call in a binding runs on every change detection check of that component. If it's expensive, the app gets slow.

```html
<!-- runs on every check -->
<p>{{ calculateTotal(items) }}</p>
```

Better options:

```ts
// computed: runs only when items change
total = computed(() => this.items().reduce((s, i) => s + i.price, 0));
```

```html
<p>{{ total() }}</p>
```

Or use a pure pipe. Reading a signal (`total()`) in the template is fine, because it just returns a cached value.

## 256: How do you create a directive with inputs, outputs and exportAs?

```ts
@Directive({
  selector: "[appCopy]",
  exportAs: "appCopy",
  host: { "(click)": "copy()" },
})
export class CopyToClipboard {
  text = input.required<string>({ alias: "appCopy" });
  copied = output<string>();
  done = signal(false);

  async copy() {
    await navigator.clipboard.writeText(this.text());
    this.done.set(true);
    this.copied.emit(this.text());
  }
}
```

```html
<button [appCopy]="apiKey" #c="appCopy" (copied)="log($event)">
  {{ c.done() ? 'Copied!' : 'Copy' }}
</button>
```

`exportAs` lets the template get a reference to the directive instance.

## 257: How do you write a custom structural directive?

Inject `TemplateRef` and `ViewContainerRef`, then create or clear the view.

```ts
@Directive({ selector: "[appHasRole]" })
export class HasRole {
  private tpl = inject(TemplateRef<unknown>);
  private vcr = inject(ViewContainerRef);
  private auth = inject(AuthService);

  role = input.required<string>({ alias: "appHasRole" });

  constructor() {
    effect(() => {
      this.vcr.clear();
      if (this.auth.roles().includes(this.role())) {
        this.vcr.createEmbeddedView(this.tpl);
      }
    });
  }
}
```

```html
<button *appHasRole="'admin'">Delete user</button>
```

This hides the element from the UI, but it's not security. The server must still check permissions.

## 258: What are smart and presentational components?

- **Smart (container) components**: know about services and state. They load data, handle actions and pass data down.
- **Presentational (dumb) components**: only get data through inputs and report actions through outputs. No services, easy to reuse and test.

```ts
// presentational
@Component({
  selector: "app-user-table",
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `...`,
})
export class UserTable {
  users = input.required<User[]>();
  delete = output<number>();
}

// smart
@Component({
  selector: "app-users-page",
  imports: [UserTable],
  template: `<app-user-table
    [users]="store.users()"
    (delete)="store.remove($event)"
  />`,
})
export class UsersPage {
  store = inject(UserStore);
}
```

## 259: Why does track matter in @for?

`track` tells Angular how to match items between renders. With a good key, Angular moves or reuses existing DOM nodes instead of destroying and recreating them.

```html
<!-- good: stable id -->
@for (user of users(); track user.id) { <app-user-row [user]="user" /> }

<!-- risky: index -->
@for (user of users(); track $index) { ... }

<!-- bad when data is reloaded: new objects every time -->
@for (user of users(); track user) { ... }
```

If you track by object identity and reload the list from the API, every object is new, so Angular rebuilds all the rows. This loses focus, scroll position and component state, and is slow for big lists.

## 260: What is the read option in queries?

By default a query on a template variable returns the component instance (if it's a component) or the `ElementRef`. The `read` option lets you ask for something else from the same element.

```ts
export class Toolbar {
  // the component instance
  menu = viewChild.required(Menu);

  // the host element of that component
  menuEl = viewChild.required(Menu, { read: ElementRef });

  // a ViewContainerRef at that spot, to insert views
  slot = viewChild.required("slot", { read: ViewContainerRef });

  // a directive on the same element
  tooltip = viewChild.required("btn", { read: Tooltip });
}
```

## 261: How do you test a component that has inputs?

Create it with `TestBed.createComponent()` and set inputs with `fixture.componentRef.setInput()`. This works for both signal inputs and decorator inputs.

```ts
describe("PriceTag", () => {
  it("shows the formatted price", async () => {
    const fixture = TestBed.createComponent(PriceTag);
    fixture.componentRef.setInput("amount", 19.5);
    fixture.componentRef.setInput("currency", "EUR");
    await fixture.whenStable();

    expect(fixture.nativeElement.textContent).toContain("€19.50");
  });
});
```

You can't set a signal input with `component.amount = ...`, because it's read-only.

## 262: How do you test a service that uses HttpClient?

Use `provideHttpClient()` together with `provideHttpClientTesting()` and `HttpTestingController`.

```ts
describe("UserService", () => {
  let service: UserService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient(), provideHttpClientTesting()],
    });
    service = TestBed.inject(UserService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => httpMock.verify()); // no unexpected requests

  it("loads users", () => {
    let result: User[] = [];
    service.getUsers().subscribe((users) => (result = users));

    const req = httpMock.expectOne("/api/users");
    expect(req.request.method).toBe("GET");
    req.flush([{ id: 1, name: "Ann" }]);

    expect(result.length).toBe(1);
  });

  it("handles errors", () => {
    service.getUsers().subscribe({ error: (e) => expect(e.status).toBe(500) });
    httpMock
      .expectOne("/api/users")
      .flush("fail", { status: 500, statusText: "Server Error" });
  });
});
```

`provideHttpClient()` must come before `provideHttpClientTesting()`.

## 263: How do you mock a dependency in a test?

Provide a fake with `useValue` or `useClass` in `TestBed`.

```ts
describe("Profile", () => {
  const userServiceMock = {
    currentUser: signal<User | null>({ id: 1, name: "Ann" }),
    logout: vi.fn(),
  };

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [{ provide: UserService, useValue: userServiceMock }],
    });
  });

  it("logs out on click", async () => {
    const fixture = TestBed.createComponent(Profile);
    await fixture.whenStable();

    fixture.nativeElement.querySelector("[data-test=logout]").click();
    expect(userServiceMock.logout).toHaveBeenCalled();
  });
});
```

`vi.fn()` is Vitest. With Jasmine you would use `jasmine.createSpy()` or `jasmine.createSpyObj()`. To replace a dependency of one component only, use `TestBed.overrideComponent()` or `overrideProvider()`.

## 264: What is the difference between fixture.detectChanges() and fixture.whenStable()?

- `fixture.detectChanges()` runs change detection synchronously, right now.
- `await fixture.whenStable()` waits until Angular has no pending work (scheduled change detection, pending HTTP requests tracked by Angular, etc.).

In zoneless apps (the default for new projects), the recommended style is to let Angular schedule change detection the same way it does in the real app, and wait with `whenStable()`:

```ts
component.count.set(5);
await fixture.whenStable();
expect(el.textContent).toContain("5");
```

This catches bugs where the UI only updates because the test called `detectChanges()`, but wouldn't update in the real app.

## 265: How do you test routing?

Use `RouterTestingHarness`. It sets up a real router and lets you navigate to a URL and check the result.

```ts
describe("routes", () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        provideRouter(
          [
            { path: "users/:id", component: UserDetails },
            { path: "admin", component: Admin, canActivate: [() => false] },
          ],
          withComponentInputBinding(),
        ),
      ],
    });
  });

  it("shows user details", async () => {
    const harness = await RouterTestingHarness.create();
    const component = await harness.navigateByUrl("/users/7", UserDetails);
    expect(component.id()).toBe("7");
  });

  it("blocks admin", async () => {
    const harness = await RouterTestingHarness.create();
    await harness.navigateByUrl("/admin");
    expect(TestBed.inject(Router).url).toBe("/");
  });
});
```

`RouterTestingModule` is deprecated; use `provideRouter()` in tests.

## 266: What are component harnesses?

Harnesses (from `@angular/cdk/testing`) are test helpers that interact with a component through a stable API instead of CSS selectors. Angular Material ships harnesses for all its components.

```ts
it("submits when the button is clicked", async () => {
  const fixture = TestBed.createComponent(LoginForm);
  const loader = TestbedHarnessEnvironment.loader(fixture);

  const email = await loader.getHarness(
    MatInputHarness.with({ selector: "#email" }),
  );
  await email.setValue("ann@mail.com");

  const button = await loader.getHarness(
    MatButtonHarness.with({ text: "Log in" }),
  );
  await button.click();

  expect(fixture.componentInstance.submitted()).toBe(true);
});
```

If the component's internal DOM changes, only the harness has to be updated, not every test.

## 267: How do you test a service that uses signals?

Signals are just values, so testing is direct: call methods and read the signals.

```ts
describe("CartStore", () => {
  let store: CartStore;

  beforeEach(() => {
    store = TestBed.inject(CartStore);
  });

  it("adds items and updates count", () => {
    store.add({ id: 1, name: "Pen", price: 2 });
    store.add({ id: 2, name: "Book", price: 10 });

    expect(store.count()).toBe(2);
    expect(store.total()).toBe(12);
  });
});
```

Computed signals update right away when read. Effects are scheduled, so to test them call `TestBed.tick()` (which runs pending effects and change detection) or `await fixture.whenStable()`.

## 268: What changed with Vitest becoming the default test runner?

Since Angular 21, `ng new` sets up **Vitest** through the `@angular/build:unit-test` builder. Before that, projects used Karma with Jasmine, and Karma is deprecated.

What stays the same:

- `TestBed`, `ComponentFixture`, `HttpTestingController` and harnesses work the same way.
- You still run `ng test`.

What changes:

- Mocks use `vi.fn()` / `vi.spyOn()` instead of `jasmine.createSpy()`.
- Fake timers use `vi.useFakeTimers()` instead of `fakeAsync` / `tick` (which need Zone.js).
- Tests run in Node with jsdom (or happy-dom) by default, or in a real browser if configured.

Existing projects can keep Karma/Jasmine. The CLI has a schematic to help move Jasmine tests to Vitest, but expect some manual work.

## 269: How do you test an output?

Subscribe to the output from the component instance, trigger the action, then check what was emitted.

```ts
it("emits the selected rating", async () => {
  const fixture = TestBed.createComponent(StarRating);
  await fixture.whenStable();

  const emitted: number[] = [];
  fixture.componentInstance.rated.subscribe((v) => emitted.push(v));

  const stars = fixture.nativeElement.querySelectorAll("button");
  stars[3].click();

  expect(emitted).toEqual([4]);
});
```

`OutputEmitterRef` from `output()` has a `subscribe()` method, so this works without RxJS.

## 270: How do you test a directive?

Create a small test host component that uses the directive, then check the DOM.

```ts
@Component({
  imports: [Highlight],
  template: `<p appHighlight="yellow">Text</p>`,
})
class TestHost {}

describe("Highlight", () => {
  it("sets the background on hover", async () => {
    const fixture = TestBed.createComponent(TestHost);
    await fixture.whenStable();

    const p: HTMLElement = fixture.nativeElement.querySelector("p");
    p.dispatchEvent(new Event("mouseenter"));
    await fixture.whenStable();

    expect(p.style.backgroundColor).toBe("yellow");
  });
});
```

Testing through a host is closer to how the directive is really used.

## 271: What is the application builder?

The application builder (`@angular/build:application`) is the default build system since Angular 17. It uses **esbuild** for bundling and **Vite** for the dev server.

Compared to the old webpack-based builder it:

- Builds much faster
- Supports SSR and prerendering in the same build
- Supports hot module replacement for styles and templates

```json
"build": {
  "builder": "@angular/build:application",
  "options": {
    "browser": "src/main.ts",
    "server": "src/main.server.ts",
    "outputMode": "server"
  }
}
```

Older projects can switch with `ng update @angular/cli --name use-application-builder`. Custom webpack configs don't carry over, so those need another solution.

## 272: What are budgets in angular.json?

Budgets set size limits for your bundles. The build warns or fails when a limit is passed. This helps you notice when someone adds a heavy dependency.

```json
"configurations": {
  "production": {
    "budgets": [
      { "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" },
      { "type": "anyComponentStyle", "maximumWarning": "4kB", "maximumError": "8kB" }
    ]
  }
}
```

Types include `initial`, `allScript`, `all`, `anyScript`, `any`, `anyComponentStyle` and `bundle` (for a named bundle).

## 273: How do you proxy API calls during development?

Create a proxy config to avoid CORS issues when the API runs on another port.

```json
// proxy.conf.json
{
  "/api": {
    "target": "http://localhost:3000",
    "secure": false,
    "changeOrigin": true
  }
}
```

```json
// angular.json
"serve": {
  "builder": "@angular/build:dev-server",
  "options": { "proxyConfig": "proxy.conf.json" }
}
```

Now `http.get('/api/users')` from `localhost:4200` is forwarded to `localhost:3000/api/users`. This only affects `ng serve`.

## 274: How do you load configuration at runtime instead of at build time?

Environment files are baked into the build, so changing an API URL means rebuilding. To use one build for many environments, load a JSON file at startup.

```ts
// public/config.json  (replaced per environment during deployment)
// { "apiUrl": "https://api.staging.example.com" }

@Injectable({ providedIn: "root" })
export class AppConfigService {
  private http = inject(HttpClient);
  private config = signal<{ apiUrl: string } | null>(null);

  get apiUrl() {
    return this.config()!.apiUrl;
  }

  async load() {
    this.config.set(
      await firstValueFrom(this.http.get<{ apiUrl: string }>("/config.json")),
    );
  }
}

export const appConfig: ApplicationConfig = {
  providers: [provideAppInitializer(() => inject(AppConfigService).load())],
};
```

Be careful with interceptors that read the config: the request for `config.json` itself also goes through them.

## 275: How do you add linting to an Angular project?

The CLI doesn't include a linter by default. Add `angular-eslint`:

```bash
ng add angular-eslint
ng lint
```

It sets up ESLint with Angular rules for TypeScript and templates, for example:

- `@angular-eslint/prefer-on-push-component-change-detection`
- `@angular-eslint/template/prefer-control-flow`
- `@angular-eslint/prefer-signals`
- `@angular-eslint/template/no-call-expression`

TSLint is long gone, so old `tslint.json` files can be removed.

## 276: What automatic migrations does Angular provide?

Besides the migrations that run during `ng update`, you can run some on demand:

```bash
ng generate @angular/core:standalone              # NgModules to standalone
ng generate @angular/core:control-flow            # *ngIf/*ngFor to @if/@for
ng generate @angular/core:inject                  # constructor DI to inject()
ng generate @angular/core:signal-input-migration  # @Input to input()
ng generate @angular/core:output-migration        # @Output to output()
ng generate @angular/core:signal-queries-migration # @ViewChild etc. to viewChild()
ng generate @angular/core:route-lazy-loading      # eager routes to lazy routes
ng generate @angular/core:self-closing-tag        # <app-x></app-x> to <app-x />
ng generate @angular/core:cleanup-unused-imports  # remove unused imports
```

Run them on a clean git branch and review the diff before committing.

## 277: What is server-side rendering (SSR) and how do you add it?

With SSR, the server renders the HTML for a page and sends it to the browser, then Angular takes over in the browser (hydration).

Benefits:

- Faster first content paint
- Better SEO and link previews
- Content is visible before JavaScript loads

Add it to a new or existing project:

```bash
ng new my-app --ssr
# or
ng add @angular/ssr
```

This creates `main.server.ts`, `app.config.server.ts`, `app.routes.server.ts` and `server.ts` (an Express server). The build then produces a `browser` folder and a `server` folder.

## 278: What is hydration?

Hydration is the process where Angular in the browser reuses the DOM that the server rendered instead of destroying and recreating it. It attaches event listeners and connects the existing DOM to the components.

```ts
export const appConfig: ApplicationConfig = {
  providers: [provideClientHydration(withEventReplay())],
};
```

Without hydration, the page would flicker because Angular would throw away the server HTML. `withEventReplay()` records clicks that happen before hydration finishes and replays them afterwards, so early clicks aren't lost.

## 279: How do you safely use browser-only APIs in an SSR app?

`window`, `document`, `localStorage` and similar APIs don't exist on the server. Options:

```ts
// 1. run only in the browser, after render
constructor() {
  afterNextRender(() => {
    const saved = localStorage.getItem('theme');
    if (saved) this.theme.set(saved);
  });
}

// 2. check the platform
private platformId = inject(PLATFORM_ID);

save() {
  if (isPlatformBrowser(this.platformId)) {
    localStorage.setItem('theme', this.theme());
  }
}

// 3. use Angular abstractions
private document = inject(DOCUMENT);
```

`afterNextRender` is usually the cleanest choice for DOM work, because it never runs on the server.

## 280: Why inject DOCUMENT instead of using the global document?

`DOCUMENT` is an injection token for the document object. On the server Angular gives you a server-side document, while the global `document` doesn't exist there. It also makes testing easier.

```ts
import { DOCUMENT } from "@angular/core";

@Injectable({ providedIn: "root" })
export class ThemeService {
  private document = inject(DOCUMENT);

  setDark(dark: boolean) {
    this.document.documentElement.classList.toggle("dark", dark);
  }
}
```

`DOCUMENT` used to be imported from `@angular/common`. Since Angular 20 it's also exported from `@angular/core`.

## 281: How does internationalization (i18n) work in Angular?

Angular's built-in i18n works at build time:

1. Mark text with the `i18n` attribute or `$localize` in code.
2. Extract messages with `ng extract-i18n`.
3. Translate the generated files (XLIFF, JSON, etc.).
4. Build one version of the app per language.

```bash
ng add @angular/localize
```

```html
<h1 i18n="@@welcomeTitle">Welcome to our store</h1>
<img [src]="logo" i18n-alt alt="Company logo" />
<span i18n
  >{count, plural, =0 {no items} =1 {one item} other {{{count}} items}}</span
>
```

```ts
const msg = $localize`:@@saveSuccess:Your changes were saved`;
```

```json
"i18n": {
  "sourceLocale": "en",
  "locales": { "ka": "src/locale/messages.ka.xlf", "de": "src/locale/messages.de.xlf" }
}
```

Because each language is a separate build, switching language means loading a different URL like `/de/`. If you need to switch languages at runtime without reloading, libraries like Transloco are common.

## 282: How do you animate elements entering and leaving the DOM?

Since Angular 20.2 you can use `animate.enter` and `animate.leave`. They add CSS classes when an element is added or about to be removed, and Angular waits for the animation to finish before removing it.

```ts
@Component({
  selector: "app-toast",
  template: `
    @if (visible()) {
      <div class="toast" animate.enter="fade-in" animate.leave="fade-out">
        Saved!
      </div>
    }
  `,
  styles: `
    .fade-in {
      animation: fade-in 200ms ease-out;
    }
    .fade-out {
      animation: fade-out 200ms ease-in;
    }
    @keyframes fade-in {
      from {
        opacity: 0;
        transform: translateY(8px);
      }
    }
    @keyframes fade-out {
      to {
        opacity: 0;
      }
    }
  `,
})
export class Toast {
  visible = signal(true);
}
```

You can also bind them to a function, `(animate.leave)="onLeave($event)"`, to use a JavaScript animation library.

## 283: What is the status of the @angular/animations package?

`@angular/animations` (with `trigger()`, `state()`, `transition()`, `animate()` and `provideAnimationsAsync()`) was deprecated in Angular 20.2. The recommended approach now is:

- Native CSS animations and transitions
- `animate.enter` / `animate.leave` for elements added or removed
- The View Transitions API for route changes (`withViewTransitions()`)

The old package still works for now and is planned for removal in a later major version, so new code should not depend on it.

## 284: What are the more advanced options of NgOptimizedImage?

```html
<!-- fill the parent instead of fixed width/height -->
<div class="banner" style="position: relative; height: 300px">
  <img ngSrc="banner.jpg" fill priority alt="Banner" />
</div>

<!-- responsive sizes, srcset is generated with a loader -->
<img
  ngSrc="product.jpg"
  width="800"
  height="600"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt=""
/>

<!-- low quality placeholder -->
<img ngSrc="photo.jpg" width="400" height="300" placeholder alt="" />
```

Image CDN loaders generate the right URLs for each size:

```ts
providers: [provideImgixLoader("https://my-site.imgix.net/")];
// also: provideCloudinaryLoader, provideCloudflareLoader, provideImageKitLoader, provideNetlifyLoader
```

`priority` also adds a preload hint, which helps your Largest Contentful Paint (LCP) score.

## 285: How does Angular protect against XSS?

Angular treats all values bound in templates as untrusted by default:

- Interpolation `{{ }}` always escapes HTML.
- Binding to `[innerHTML]` sanitizes the value, removing scripts and dangerous attributes.
- URLs bound to `[href]` or `[src]` are checked, and `javascript:` URLs are blocked.
- Style values are sanitized.

```ts
comment = '<img src=x onerror="alert(1)"><b>Hello</b>';
```

```html
<p>{{ comment }}</p>
<!-- shows the raw text -->
<p [innerHTML]="comment"></p>
<!-- renders <b>Hello</b>, removes onerror -->
```

Things that bypass this protection: using `ElementRef.nativeElement.innerHTML` directly, `bypassSecurityTrust*` methods, and building templates from user input.

## 286: When is it OK to use DomSanitizer.bypassSecurityTrust?

Only when you are sure the content is safe, for example HTML or URLs that you control or that you sanitized on the server.

```ts
export class VideoEmbed {
  private sanitizer = inject(DomSanitizer);
  videoId = input.required<string>();

  url = computed(() =>
    this.sanitizer.bypassSecurityTrustResourceUrl(
      `https://www.youtube.com/embed/${encodeURIComponent(this.videoId())}`,
    ),
  );
}
```

```html
<iframe [src]="url()"></iframe>
```

Methods: `bypassSecurityTrustHtml`, `bypassSecurityTrustStyle`, `bypassSecurityTrustScript`, `bypassSecurityTrustUrl`, `bypassSecurityTrustResourceUrl`. Never pass user input to them directly, that opens an XSS hole.

## 287: How do you migrate an NgModule app to standalone?

Run the schematic and follow its three steps:

```bash
ng generate @angular/core:standalone
```

1. Convert all components, directives and pipes to standalone.
2. Remove NgModules that are no longer needed.
3. Switch to `bootstrapApplication()`.

After that, replace module-based providers with provider functions:

| Before                         | After                            |
| ------------------------------ | -------------------------------- |
| `RouterModule.forRoot(routes)` | `provideRouter(routes)`          |
| `HttpClientModule`             | `provideHttpClient()`            |
| `BrowserAnimationsModule`      | CSS animations / `animate.enter` |
| `StoreModule.forRoot()`        | `provideStore()`                 |

Commit after each step and run tests in between.

## 288: What are Angular Elements?

Angular Elements (`@angular/elements`) turns an Angular component into a native custom element (web component) that can be used in any HTML page or in other frameworks.

```ts
import { createApplication } from "@angular/platform-browser";
import { createCustomElement } from "@angular/elements";

(async () => {
  const app = await createApplication({ providers: [] });
  const element = createCustomElement(RatingWidget, { injector: app.injector });
  customElements.define("rating-widget", element);
})();
```

```html
<rating-widget value="4"></rating-widget>
```

Inputs become attributes/properties, and outputs become DOM `CustomEvent`s. It's useful for embedding widgets in non-Angular sites or for gradual migrations.

## 289: How do you handle errors globally?

Provide your own `ErrorHandler`. Angular calls it for uncaught errors in components, effects, event handlers and so on.

```ts
@Injectable()
export class GlobalErrorHandler implements ErrorHandler {
  private logger = inject(LoggingService);

  handleError(error: unknown): void {
    this.logger.log(error);
    console.error(error);
  }
}

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    { provide: ErrorHandler, useClass: GlobalErrorHandler },
  ],
};
```

`provideBrowserGlobalErrorListeners()` (added in Angular 20) also sends errors from the window's `error` and `unhandledrejection` events to the `ErrorHandler`. HTTP errors are best handled in an interceptor.

## 290: How do you use a Content Security Policy with Angular?

A CSP limits which scripts and styles a page can run. Angular supports it in two ways:

1. **autoCsp** (Angular 19+): the build generates a hash-based CSP for inline scripts and adds it as a `<meta>` tag.

```json
"security": { "autoCsp": true }
```

2. **Nonces**: if your server generates a nonce per request, add it to the root element so Angular uses it for its inline styles.

```html
<app-root ngCspNonce="random-nonce-from-server"></app-root>
```

Or provide it with the `CSP_NONCE` token. You can also enable Trusted Types for stronger DOM XSS protection.

## 291: How do you debug a production build?

- Enable source maps in the production config, optionally hidden so they're not linked from the JS files:

```json
"sourceMap": { "scripts": true, "styles": true, "hidden": true }
```

- Upload hidden source maps to your error tracking tool (Sentry etc.) instead of serving them publicly.
- Use `ng build --configuration development` locally to reproduce issues without minification.
- Angular error codes like `NG0100` link to explanations at `angular.dev/errors`.

## 292: How do you deploy an Angular app?

For a client-only app:

1. Run `ng build`.
2. Upload `dist/<app>/browser` to any static host (Nginx, S3, Netlify, Firebase Hosting, etc.).
3. Configure the server to return `index.html` for unknown paths, so deep links like `/products/5` work on reload.

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

For SSR, run the Node server from `dist/<app>/server/server.mjs` (or deploy it to a platform that supports it). `ng deploy` works with builders like `@angular/fire` to deploy in one command.

Static assets with hashed file names can be cached for a long time. `index.html` should not be cached, or users may load old bundles.

## 293: What are strict mode and strictTemplates?

New projects are created in strict mode. It turns on:

- TypeScript `strict` checks (`strictNullChecks`, `noImplicitAny`, etc.)
- `strictTemplates` in `angularCompilerOptions`: full type checking of templates
- `strictInjectionParameters` and `strictInputAccessModifiers`

```json
"angularCompilerOptions": {
  "strictTemplates": true,
  "strictInjectionParameters": true,
  "extendedDiagnostics": {
    "checks": { "optionalChainNotNullable": "warning" }
  }
}
```

With `strictTemplates`, passing a `string` to an input that expects a `number` fails the build, and `$event` gets its correct type.

## 294: How do you set up path aliases for imports?

Add `paths` to `tsconfig.json`. The Angular build picks them up automatically.

```json
{
  "compilerOptions": {
    "paths": {
      "@core/*": ["src/app/core/*"],
      "@shared/*": ["src/app/shared/*"],
      "@env": ["src/environments/environment"]
    }
  }
}
```

```ts
import { AuthService } from "@core/auth/auth.service";
import { environment } from "@env";
```

This avoids long `../../../` paths and makes moving files easier.

## 295: What is virtual scrolling?

Virtual scrolling renders only the items visible on screen, instead of all items in a big list. The CDK provides it.

```ts
@Component({
  selector: "app-log-viewer",
  imports: [ScrollingModule],
  template: `
    <cdk-virtual-scroll-viewport itemSize="32" class="viewport">
      <div *cdkVirtualFor="let line of lines(); trackBy: trackById" class="row">
        {{ line.text }}
      </div>
    </cdk-virtual-scroll-viewport>
  `,
  styles: `
    .viewport {
      height: 500px;
    }
    .row {
      height: 32px;
    }
  `,
})
export class LogViewer {
  lines = signal<LogLine[]>([]);
  trackById = (_: number, l: LogLine) => l.id;
}
```

A list of 50,000 rows then only has a few dozen DOM elements at a time.

## 296: How do you set meta tags for SEO?

Use the `Meta` and `Title` services. With SSR, these tags end up in the HTML that crawlers see.

```ts
export class ArticlePage {
  private meta = inject(Meta);
  private title = inject(Title);
  article = input.required<Article>();

  constructor() {
    effect(() => {
      const a = this.article();
      this.title.setTitle(a.title);
      this.meta.updateTag({ name: "description", content: a.summary });
      this.meta.updateTag({ property: "og:title", content: a.title });
      this.meta.updateTag({ property: "og:image", content: a.coverUrl });
    });
  }
}
```

Without SSR or prerendering, many crawlers and link preview bots won't see these tags.

## 297: What does Angular offer for accessibility?

- Templates support all ARIA attributes with `[attr.aria-*]` bindings.
- `routerLinkActive` can set `aria-current` with `ariaCurrentWhenActive`.
- The CDK `a11y` package has `FocusTrap`, `LiveAnnouncer`, `FocusMonitor` and `ListKeyManager`.
- Angular Material components follow WAI-ARIA patterns.
- **Angular Aria** (`@angular/aria`, added in Angular 21 as developer preview) gives headless, accessible building blocks like listbox, tabs, menu, combobox, tree and grid, which you style yourself.

```ts
export class SaveButton {
  private announcer = inject(LiveAnnouncer);

  async save() {
    // ...
    this.announcer.announce("Profile saved", "polite");
  }
}
```

Angular's ESLint plugin also has template accessibility rules.

## 298: How do you add drag and drop?

Use the CDK `DragDropModule`.

```ts
@Component({
  selector: "app-task-list",
  imports: [CdkDropList, CdkDrag],
  template: `
    <div cdkDropList (cdkDropListDropped)="drop($event)">
      @for (task of tasks(); track task.id) {
        <div cdkDrag>{{ task.title }}</div>
      }
    </div>
  `,
})
export class TaskList {
  tasks = signal<Task[]>([]);

  drop(event: CdkDragDrop<Task[]>) {
    this.tasks.update((list) => {
      const copy = [...list];
      moveItemInArray(copy, event.previousIndex, event.currentIndex);
      return copy;
    });
  }
}
```

`transferArrayItem` moves items between two connected lists.

## 299: What is prerendering (static site generation)?

Prerendering renders pages to HTML files at **build time**. They can be served from a static host or CDN like a normal website, which is very fast.

```ts
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  { path: "", renderMode: RenderMode.Prerender },
  { path: "about", renderMode: RenderMode.Prerender },
  { path: "account/**", renderMode: RenderMode.Client },
  { path: "**", renderMode: RenderMode.Server },
];
```

Use prerendering for pages that are the same for every user (marketing pages, docs, blog posts). Use `Server` rendering for personalized or frequently changing pages.

## 300: How do you create a library inside an Angular workspace?

```bash
ng new my-workspace --no-create-application
cd my-workspace
ng generate application shop
ng generate library ui-kit
```

The library gets its own folder in `projects/ui-kit`, with a `public-api.ts` that lists what it exports.

```ts
// projects/ui-kit/src/public-api.ts
export * from "./lib/button/button";
export * from "./lib/card/card";
```

Build it with `ng build ui-kit`. The output in `dist/ui-kit` uses the Angular Package Format and can be published to npm. Inside the workspace, the app imports it through a `paths` entry in `tsconfig.json`.

---

# Advanced Questions (301-450)

## 301: How does Angular compile a component template?

The Angular compiler turns each template into a **template function** made of instructions. The function runs in two modes:

- **Creation mode**: runs once, creates DOM elements, sets up listeners and directives.
- **Update mode**: runs on every check of that view, reads bindings and updates only what changed.

Simplified output for `<h1>{{ title }}</h1><button (click)="save()">Save</button>`:

```js
function App_Template(rf, ctx) {
  if (rf & 1) {
    // create
    ɵɵelementStart(0, "h1");
    ɵɵtext(1);
    ɵɵelementEnd();
    ɵɵelementStart(2, "button");
    ɵɵlistener("click", () => ctx.save());
    ɵɵtext(3, "Save");
    ɵɵelementEnd();
  }
  if (rf & 2) {
    // update
    ɵɵadvance(1);
    ɵɵtextInterpolate(ctx.title);
  }
}
```

The static parts of the template are handled once, and the update pass only compares binding values with the previous ones stored in the view. Because instructions are plain functions, unused ones are removed by tree shaking.

## 302: What are LView and TView?

They are the internal data structures Ivy uses for each view:

- **TView** (template view): shared, static information about a template. There is one per component template (or `ng-template`), no matter how many instances exist. It holds things like the list of directives, binding counts, and the compiled template function.
- **LView** (logical view): the data for one instance of a view. It is an array holding DOM nodes, binding values from the last check, directive instances, the context, flags (dirty, attached, etc.), and links to parent and child views.

So ten `<app-row>` instances share one TView but have ten LViews. Change detection walks LViews, compares current binding values with the ones stored in the LView, and updates the DOM when they differ.

## 303: What is the locality principle in Ivy?

Locality means each component is compiled using only its own information (its decorator metadata and the metadata of things it directly imports). The compiler doesn't need to analyze the whole app to compile one component.

Results:

- Faster incremental builds, since changing one file only recompiles what depends on it
- Libraries can ship partially compiled code
- Standalone components work naturally, because each component lists its own dependencies
- Lazy loading of components without a module wrapper

## 304: How does Angular type check templates?

The compiler (`ngtsc`) generates **type-check blocks (TCBs)**: hidden TypeScript code that mirrors your template. TypeScript then checks that code, and errors are mapped back to the template.

For example, `<app-user [user]="selected" (saved)="onSave($event)">` becomes roughly:

```ts
function tcb(ctx: UsersPage) {
  const dir = null! as UserCard;
  dir.user = ctx.selected; // type error if types don't match
  dir.saved.subscribe(($event) => ctx.onSave($event));
}
```

How strict this is depends on settings:

- `strictTemplates: true` enables full checking (input types, `$event` types, null checks, DOM events).
- `@if (x; as y)` narrows types inside the block.
- Generic components infer their type parameters from inputs.
- Extended diagnostics add extra checks, like a missing `()` when reading a signal.

## 305: How does change detection walk the component tree?

Angular starts at the root view(s) and goes down the tree. For each view:

1. If the view is detached, skip it.
2. If it's `Default` strategy, check it. If it's `OnPush`, check it only if it's marked dirty (or has signals that changed).
3. Run the template's update function, compare binding values, update the DOM.
4. Run lifecycle hooks (`ngDoCheck`, `ngAfterViewChecked`, ...).
5. Continue with child views, including embedded views from `@if`, `@for` and projected content.

`markForCheck()` (called by events, the async pipe, `setInput`, etc.) marks the view **and all its ancestors** dirty, so the path from the root to that view gets checked. In development mode, a second pass (`checkNoChanges`) verifies that nothing changed during the first pass.

## 306: How do signals make change detection more targeted?

When a template reads a signal, the component's LView becomes a **reactive consumer** of that signal. When the signal changes:

1. The LView gets a `RefreshView` flag.
2. Its ancestors get a `HasChildViewsToRefresh` flag, **not** marked dirty.
3. Angular schedules change detection.

During the next run, Angular passes through OnPush ancestors that only have `HasChildViewsToRefresh` without re-checking their own bindings, and refreshes only the views that read the changed signal. This is sometimes called local or targeted change detection.

```
App (OnPush)                  -> traversed, not checked
  Sidebar (OnPush)            -> skipped
  Dashboard (OnPush)          -> traversed, not checked
    Counter (OnPush, reads count()) -> refreshed
```

With `Default` strategy components this benefit is reduced, because a `Default` component in the path is always checked.

## 307: How does the zoneless scheduler decide when to run change detection?

Without Zone.js, Angular has a `ChangeDetectionScheduler`. Things that notify it:

- A signal read by a template changes
- `markForCheck()` (called by template listeners, `async` pipe, `ComponentRef.setInput()`)
- A view is attached or removed
- `ApplicationRef.tick()` is called directly

When notified, it schedules one `ApplicationRef.tick()` using a race between `setTimeout` and `requestAnimationFrame`, so several changes in the same task are batched into one run.

Things that **don't** trigger it anymore: a plain field changed inside a `setTimeout`, a third-party library callback, or an `HttpClient` response that only writes a plain class field. That code needs to write to a signal or call `markForCheck()`.

## 308: What does ApplicationRef.tick() do?

`tick()` runs change detection for all root views attached to the application (and in dev mode, the `checkNoChanges` pass). It also runs `afterRender` callbacks and can loop a few times if those callbacks or effects mark views dirty again.

```ts
const appRef = inject(ApplicationRef);
appRef.tick();
```

You rarely call it yourself. It's used by:

- Zone.js integration, after the zone becomes stable
- The zoneless scheduler
- Views created manually and attached with `appRef.attachView()`

Calling `tick()` from inside change detection throws an error (`NG0101: ApplicationRef.tick is called recursively`).

## 309: What is PendingTasks and why does it matter?

`PendingTasks` tells Angular that some async work is still running, so the app is not "stable" yet. Stability is used by:

- SSR, which waits for the app to be stable before serialising HTML
- `fixture.whenStable()` in tests
- Hydration and some router behavior

`HttpClient`, the router and resources register their work automatically. For your own async work, register it:

```ts
export class Prices {
  private tasks = inject(PendingTasks);
  prices = signal<Price[]>([]);

  constructor() {
    this.tasks.run(async () => {
      const res = await fetch("/api/prices");
      this.prices.set(await res.json());
    });
  }
}
```

There's also `pendingUntilEvent()` from `@angular/core/rxjs-interop` for Observables. Without this, a server render might finish before the data arrives and send an empty page.

## 310: What is exhaustive checkNoChanges?

In development, Angular normally runs `checkNoChanges` only on the views it just checked. With OnPush and signals, a binding that changed in a skipped view might go unnoticed. Exhaustive mode checks all views, even OnPush ones that weren't dirty.

```ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection(),
    provideCheckNoChangesConfig({ exhaustive: true, interval: 1000 }),
  ],
};
```

`interval` runs the check periodically. This is useful when migrating to zoneless: it finds places where state changes without notifying Angular (a plain field updated in a callback). Only enable it in development, it is slow.

## 311: What is event coalescing in Zone.js apps?

When an event bubbles through nested elements with listeners, each listener can trigger a separate change detection run. With event coalescing, Angular waits and runs change detection once for the group.

```ts
provideZoneChangeDetection({ eventCoalescing: true, runCoalescing: true });
```

- `eventCoalescing`: one run for events that fire together (like a click handled by parent and child).
- `runCoalescing`: also coalesces multiple `NgZone.run()` calls.

New Zone-based projects have `eventCoalescing: true`. Zoneless apps get this kind of batching from the scheduler automatically.

## 312: How does Zone.js work?

A zone is an execution context that persists across async tasks. Zone.js monkey-patches async browser APIs (`setTimeout`, `Promise.then`, `addEventListener`, `XMLHttpRequest`, `fetch`, etc.) so that callbacks run inside the same zone they were scheduled from.

Angular creates its own zone (`NgZone`) and hooks into it:

- `onMicrotaskEmpty`: when there are no more microtasks, Angular runs `ApplicationRef.tick()`.
- `onStable`: the zone has no pending work.
- `onUnstable`, `onError`.

```ts
const zone = Zone.current.fork({
  name: "logging",
  onInvokeTask(parent, current, target, task, applyThis, args) {
    console.log("task started", task.source);
    return parent.invokeTask(target, task, applyThis, args);
  },
});
zone.run(() => setTimeout(() => {}, 100));
```

Downsides: it can't patch native `async/await` (that's why Angular downlevels async/await when Zone.js is used), it adds bundle size, and change detection runs more than needed.

## 313: How do you find code that breaks in a zoneless app?

Code that changes state without telling Angular will stop updating the UI. To find it:

1. Turn on exhaustive checks in development:

```ts
provideCheckNoChangesConfig({ exhaustive: true, interval: 500 });
```

You get `NG0100` errors pointing to bindings that changed without notification.

2. Search for patterns:
   - `setTimeout` / `setInterval` / `Promise.then` that set plain fields
   - Subscriptions in components that assign to plain fields instead of signals
   - Third-party library callbacks (maps, charts, websockets)
   - `NgZone.onStable`, `onMicrotaskEmpty`, `isStable` usage

3. Fix by converting state to signals, using `toSignal()`, the `async` pipe, or `markForCheck()`.

Setting every component to OnPush before switching is a good preparation, because OnPush has the same "you must notify" rules.

## 314: What happens if a signal changes during change detection?

If a signal that a template already read is set during the same change detection pass (for example in `ngAfterViewInit` of a child), Angular doesn't throw like it would for a plain field. It marks the view for refresh and the `tick()` loop runs again (with a limit to avoid infinite loops).

```ts
export class Child implements AfterViewInit {
  private parentState = inject(ParentState);
  ngAfterViewInit() {
    this.parentState.childReady.set(true); // parent re-renders in the same tick
  }
}
```

This is more forgiving than plain fields, but it's still extra work. If it happens in a loop, you get an error about too many re-render passes. Writing to signals from `computed()` is not allowed at all and throws.

## 315: How are effects scheduled?

Since Angular 19 there are two kinds of effects:

- **Component (view) effects**: created inside a component or directive. They run as part of change detection for that view, before its template is checked. This makes them see a consistent state and lets them run in tree order.
- **Root effects**: created in services or outside a component tree. They run as microtasks before change detection of the whole app.

```ts
@Component({ selector: "app-x", template: "" })
export class X {
  constructor() {
    effect(() => console.log("view effect", this.value())); // runs with this view's check
  }
  value = input(0);
}

@Injectable({ providedIn: "root" })
export class Analytics {
  constructor() {
    effect(() => track(this.page())); // root effect
  }
  page = signal("/");
}
```

Effects always run asynchronously after the signal changes, never synchronously inside `set()`. Multiple changes before the effect runs result in one execution.

## 316: How does the signal dependency graph work?

Signals use a **push-pull** model:

- **Producers**: writable signals and computeds.
- **Consumers**: computeds, effects and templates.

When a consumer runs, every signal it reads is recorded as a dependency. When a producer changes:

1. **Push**: it notifies its consumers that they might be dirty. Nothing is recomputed yet, it only marks them.
2. **Pull**: when a dirty consumer is read (or an effect/template is scheduled), it checks whether any dependency actually changed (by comparing version numbers) and only then recomputes.

Dependencies are recalculated on every run, so they can be dynamic:

```ts
const showDetails = signal(false);
const details = signal("...");
const view = computed(() => (showDetails() ? details() : "hidden"));
// when showDetails is false, changes to details don't make view recompute
```

## 317: What does "glitch-free" mean for signals?

A glitch is when a derived value is computed from a mix of old and new values during an update. Angular signals avoid this because computeds are evaluated lazily (pull), only when read, after all writes have happened.

```ts
const first = signal("Ann");
const last = signal("Lee");
const full = computed(() => `${first()} ${last()}`);

effect(() => console.log(full()));

first.set("Bob");
last.set("Ray");
// the effect logs "Bob Ray" once, never "Bob Lee"
```

Since effects are scheduled and not run on each `set()`, they see the final consistent state.

## 318: What happens when a computed throws an error?

The error is cached like a value. Reading the computed rethrows the same error until one of its dependencies changes, then it tries again.

```ts
const raw = signal('{"a":1}');
const parsed = computed(() => JSON.parse(raw()));

raw.set("not json");
try {
  parsed();
} catch (e) {
  /* SyntaxError */
}
try {
  parsed();
} catch (e) {
  /* same error, not recomputed */
}

raw.set('{"b":2}');
parsed(); // works again
```

If a template reads a computed that throws, the error goes to the `ErrorHandler`. For values that may fail, it's often cleaner to return a result object (`{ ok: false, error }`) instead of throwing.

Also note: computeds can't write to signals. Doing so throws an error.

## 319: When is linkedSignal better than computed plus a writable signal?

Use `linkedSignal` when a value has a default that comes from other state, but the user can also override it, and the override should reset (or adapt) when the source changes.

```ts
export class Pagination {
  filter = input.required<string>();
  pageSize = input(20);

  // reset to page 1 whenever filter or page size changes, but user can move pages
  page = linkedSignal({
    source: () => ({ filter: this.filter(), size: this.pageSize() }),
    computation: () => 1,
  });

  next() {
    this.page.update((p) => p + 1);
  }
}
```

Without `linkedSignal`, you'd need an effect that writes to `page`, which runs later and can show an inconsistent state for one render. `linkedSignal` updates synchronously when read.

## 320: What are the possible states of a resource?

`resource.status()` returns one of:

| Status        | Meaning                                                            |
| ------------- | ------------------------------------------------------------------ |
| `'idle'`      | no valid params (`params` returned `undefined`), loader didn't run |
| `'loading'`   | loading for the first time or after params changed                 |
| `'reloading'` | `reload()` was called, previous value is still shown               |
| `'resolved'`  | loaded successfully                                                |
| `'error'`     | the loader failed                                                  |
| `'local'`     | the value was set manually with `set()` or `update()`              |

Key behavior:

- When `params` change, the previous request gets its `abortSignal` aborted.
- During `'loading'` after a params change, `value()` goes back to the default value. During `'reloading'` it keeps the old value.
- In the `'error'` state, reading `value()` throws, so check `hasValue()` or `error()` first.

```ts
user = resource({
  params: () => this.id(),
  loader: ({ params, abortSignal }) => fetchUser(params, abortSignal),
  defaultValue: null,
});

rename(name: string) {
  this.user.update((u) => (u ? { ...u, name } : u)); // status becomes 'local'
}
```

## 321: What is a streaming resource?

The `stream` option of `resource()` lets the loader return a signal that can emit many values over time, for example from a websocket or a chunked response.

```ts
chat = resource({
  params: () => this.roomId(),
  stream: async ({ params, abortSignal }) => {
    const messages = signal<{ value: Message[] }>({ value: [] });
    const socket = new WebSocket(`/ws/rooms/${params}`);

    socket.onmessage = (e) =>
      messages.update((m) => ({ value: [...m.value, JSON.parse(e.data)] }));
    socket.onerror = () =>
      messages.set({ error: new Error("connection lost") } as any);
    abortSignal.addEventListener("abort", () => socket.close());

    return messages;
  },
});
```

`rxResource` with a `stream` that returns a multi-value Observable works the same way. When params change, the abort signal fires so you can close the old connection.

## 322: How do you validate an httpResource response?

Use the `parse` option. It runs on the raw response, and whatever it returns becomes the value. A schema library like Zod works well here.

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
  email: z.string().email(),
});

export class UserView {
  id = input.required<number>();

  user = httpResource(() => `/api/users/${this.id()}`, {
    parse: UserSchema.parse,
  });
}
```

If `parse` throws, the resource goes to the `'error'` state. The type of `user.value()` is inferred from the parser, so you don't need to write the generic manually.

Other options include `defaultValue`, `equal` and `injector`.

## 323: How do you debounce a resource?

`resource` refetches as soon as `params` change, so debounce the signal that feeds it. One way is to go through RxJS:

```ts
export class Search {
  query = signal("");

  private debouncedQuery = toSignal(
    toObservable(this.query).pipe(debounceTime(300), distinctUntilChanged()),
    { initialValue: "" },
  );

  results = httpResource<Item[]>(
    () => {
      const q = this.debouncedQuery();
      return q.length >= 2 ? { url: "/api/search", params: { q } } : undefined;
    },
    { defaultValue: [] },
  );
}
```

Alternatively, use `rxResource` and put `debounceTime` inside the `stream` Observable, or write a small `debounced()` signal helper with `setTimeout` and `DestroyRef`.

## 324: What is afterRenderEffect()?

`afterRenderEffect()` is like `effect()` but runs after rendering, and only when the signals it reads change. It's meant for DOM work that depends on signals.

```ts
export class ChartComponent {
  data = input.required<number[]>();
  canvas = viewChild.required<ElementRef<HTMLCanvasElement>>("canvas");

  constructor() {
    afterRenderEffect({
      earlyRead: () => this.canvas().nativeElement.clientWidth,
      write: (width) => {
        drawChart(this.canvas().nativeElement, this.data(), width());
      },
    });
  }
}
```

Phases run in order: `earlyRead`, `write`, `mixedReadWrite`, `read`. The value returned from one phase is passed to the next as a signal. Grouping all reads and all writes avoids forcing the browser to recalculate layout many times. Like `afterNextRender`, it never runs on the server.

## 325: How do you build a component that works both controlled and uncontrolled?

Use `model()`. If the parent binds `[(value)]`, the parent controls it. If it doesn't, the component keeps its own internal state.

```ts
@Component({
  selector: "app-accordion-item",
  template: `
    <button (click)="toggle()" [attr.aria-expanded]="open()">
      {{ title() }}
    </button>
    @if (open()) {
      <div><ng-content /></div>
    }
  `,
})
export class AccordionItem {
  title = input.required<string>();
  open = model(false);

  toggle() {
    this.open.update((v) => !v);
  }
}
```

```html
<!-- uncontrolled: component manages it -->
<app-accordion-item title="FAQ 1">...</app-accordion-item>

<!-- controlled: parent owns the state -->
<app-accordion-item title="FAQ 2" [(open)]="faqOpen">...</app-accordion-item>
```

For a read-only input that also needs local overrides, use `linkedSignal(() => this.inputValue())`.

## 326: What is NgRx SignalStore?

SignalStore (`@ngrx/signals`) is a lightweight state management library built on signals. You build a store from features.

```ts
export const TodoStore = signalStore(
  { providedIn: "root" },
  withState({ todos: [] as Todo[], filter: "all" as "all" | "done" }),
  withComputed(({ todos, filter }) => ({
    visible: computed(() =>
      filter() === "done" ? todos().filter((t) => t.done) : todos(),
    ),
  })),
  withMethods((store, api = inject(TodoApi)) => ({
    setFilter(filter: "all" | "done") {
      patchState(store, { filter });
    },
    load: rxMethod<void>(
      pipe(
        switchMap(() => api.getAll()),
        tap((todos) => patchState(store, { todos })),
      ),
    ),
  })),
  withHooks({ onInit: (store) => store.load() }),
);
```

```ts
export class TodoPage {
  store = inject(TodoStore);
}
// template: @for (t of store.visible(); track t.id) { ... }
```

It sits between plain signal services and the full Redux-style NgRx Store.

## 327: How do you choose between signal services, SignalStore and NgRx Store?

- **Plain services with signals**: small to medium apps, or local feature state. No extra library, easy to understand.
- **NgRx SignalStore**: when you want a consistent pattern across many features, reusable store features (entities, loading state, devtools), and less boilerplate than Redux.
- **NgRx Store (Redux pattern)**: large apps with many teams, complex event flows, strict unidirectional data flow, action logs and time-travel debugging, or where many features react to the same events.

Good questions to ask: How many developers touch the state? Do you need an audit trail of actions? Is the state shared across many features or mostly local? Starting simple and moving to a store when it hurts is often fine, as long as components read state through a service API and not directly.

## 328: How do you avoid infinite loops with effects?

An effect that reads and writes the same signal can loop:

```ts
// bad: reads count and writes count
effect(() => {
  this.count.set(this.count() + 1);
});
```

Ways to avoid it:

- Use `computed()` for derived values instead of writing in effects.
- Read the value you write with `untracked()` if you truly need it:

```ts
effect(() => {
  const user = this.user(); // dependency
  untracked(() => this.history.update((h) => [...h, user]));
});
```

- Use `linkedSignal()` for "reset when X changes".
- Keep effects small and focused on side effects outside the signal graph.

Angular detects some of these cases and reports errors, but it's better not to rely on that.

## 329: How does the host flag work with element injectors?

`inject(X, { host: true })` limits the lookup to the current component's element injector tree up to its **host element**. It won't go beyond the component that owns the template where the directive is used.

```ts
@Directive({ selector: "[appFormField]" })
export class FormFieldDirective {
  // find the form container in the same component's template, don't look further up
  container = inject(FormContainer, { host: true, optional: true });
}
```

This matters for directives that should only work with something in the same component, and for content projection: a projected component's host is the component where it was declared, not the one it's projected into. Together with `viewProviders`, it gives library authors control over which services can be seen from outside.

## 330: How do you write your own provideX() function?

Use `makeEnvironmentProviders()`. It returns `EnvironmentProviders`, which can only be used in environment injectors (app config, route providers), not in component `providers`. This prevents misuse.

```ts
export interface AnalyticsConfig {
  trackingId: string;
  debug?: boolean;
}

export const ANALYTICS_CONFIG = new InjectionToken<AnalyticsConfig>(
  "ANALYTICS_CONFIG",
);

export function provideAnalytics(
  config: AnalyticsConfig,
): EnvironmentProviders {
  return makeEnvironmentProviders([
    { provide: ANALYTICS_CONFIG, useValue: config },
    AnalyticsService,
    provideEnvironmentInitializer(() => inject(AnalyticsService).init()),
  ]);
}
```

```ts
export const appConfig: ApplicationConfig = {
  providers: [provideAnalytics({ trackingId: "UA-123" })],
};
```

For optional features, follow Angular's pattern: `provideAnalytics(withDebug(), withRouterTracking())`, where each `withX()` returns a feature object.

## 331: How do you create an injector at runtime?

Use `createEnvironmentInjector()` for environment-level providers, or `Injector.create()` for a simple injector.

```ts
@Injectable({ providedIn: "root" })
export class PluginLoader {
  private parent = inject(EnvironmentInjector);

  async load(name: string) {
    const plugin = await import(`./plugins/${name}.ts`);
    const injector = createEnvironmentInjector(
      plugin.providers,
      this.parent,
      name,
    );
    return { component: plugin.PluginComponent, injector };
  }
}
```

```ts
const injector = Injector.create({
  providers: [{ provide: DIALOG_DATA, useValue: { id: 5 } }],
  parent: this.injector,
});
this.vcr.createComponent(EditDialog, { injector });
```

Remember to call `injector.destroy()` on environment injectors when you're done, so `ngOnDestroy` of their services runs.

## 332: What is forwardRef() and when do you need it?

`forwardRef()` lets you refer to a class that isn't defined yet at that point in the file. It's mostly needed in decorator metadata, which runs when the class is defined.

```ts
@Component({
  selector: "app-color-input",
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => ColorInput), // ColorInput isn't defined yet here
      multi: true,
    },
  ],
  template: `...`,
})
export class ColorInput implements ControlValueAccessor {
  /* ... */
}
```

It's also used for circular imports between two components that use each other (like a recursive tree). With `inject()` in field initializers, the injected class is already defined at runtime, so you need `forwardRef` less often than before.

## 333: What is providedIn: 'platform'?

`providedIn: 'platform'` puts the service in the platform injector, which sits above the application root injector. It's shared between all Angular applications bootstrapped on the same page.

```ts
@Injectable({ providedIn: "platform" })
export class SharedEventBus {}
```

This is rare. It can be used when several Angular apps (for example micro frontends or Angular Elements) run on one page and need to share one instance. Note that it doesn't help if each app ships its own copy of Angular, since then they don't share a platform. There's also `providedIn: 'any'`, which is deprecated.

## 334: What is provideEnvironmentInitializer()?

It runs a function when an environment injector is created. For the root injector, that's app startup. For a route's injector, it's the first time the route's injector is created.

```ts
export const ADMIN_ROUTES: Routes = [
  {
    path: "",
    providers: [
      AdminTelemetry,
      provideEnvironmentInitializer(() => inject(AdminTelemetry).start()),
    ],
    children: [/* ... */],
  },
];
```

Unlike `provideAppInitializer`, it doesn't wait for async work. It replaces the deprecated `ENVIRONMENT_INITIALIZER` multi token.

## 335: How do you fix a circular dependency error (NG0200)?

`NG0200: Circular dependency in DI detected` means service A needs B and B needs A (directly or through a chain).

Options:

1. **Refactor**: move the shared logic into a third service that both use. This is usually the right fix.
2. **Use events or signals** instead of direct calls, so one side just reacts to state.
3. **Lazy injection** with `Injector` (last resort):

```ts
@Injectable({ providedIn: "root" })
export class AuthService {
  private injector = inject(Injector);

  logout() {
    // get it only when needed, not at construction time
    this.injector.get(SessionStore).clear();
  }
}
```

A common real case is an HTTP interceptor that injects `AuthService`, which injects `HttpClient`, which runs the interceptor. Here it helps to inject `HttpBackend` and create a separate `HttpClient` for the auth calls, or to inject lazily.

## 336: Where does code for a providedIn: 'root' service end up in the bundles?

With `providedIn: 'root'`, the service is tree-shakable. The bundler puts the code in the chunk where it's used:

- Used only by a lazy-loaded route: the service code goes into that lazy chunk, but the instance is still created in the root injector and shared app-wide.
- Used by several lazy chunks: the bundler moves it to a shared chunk.
- Used in the main bundle: it's in the main bundle.

If you instead list a service in a lazy route's `providers`, you get a separate instance for that route. If you also have it as `providedIn: 'root'`, there are two instances, which is a common source of "my state is lost" bugs.

## 337: How long do route-level injectors live?

A route's environment injector is created the first time the route is activated and is **not** destroyed when you navigate away. It lives until the app is destroyed. So services provided on a route keep their state across visits.

If you need state that resets on each visit, provide the service in the routed component instead:

```ts
@Component({
  selector: "app-checkout",
  providers: [CheckoutState], // new instance each time the component is created
  template: `...`,
})
export class Checkout {}
```

Or reset it explicitly in a guard or resolver. Knowing this difference is important for things like wizard state or forms that should start fresh.

## 338: How do you override providers in tests?

There are several levels:

```ts
// 1. app-level
TestBed.configureTestingModule({
  providers: [{ provide: PaymentApi, useValue: fakePaymentApi }],
});

// 2. replace a provider everywhere, including inside components
TestBed.overrideProvider(PaymentApi, { useValue: fakePaymentApi });

// 3. replace what a specific component provides itself
TestBed.overrideComponent(CheckoutWizard, {
  set: { providers: [{ provide: WizardState, useValue: fakeWizardState }] },
});

// 4. replace a component's imports, for example a heavy child
TestBed.overrideComponent(Dashboard, {
  remove: { imports: [HeavyChart] },
  add: { imports: [FakeChart] },
});
```

`overrideComponent` is needed when the component has its own `providers`, because those take priority over the TestBed root providers.

## 339: What are the pitfalls of using inject() in helper functions?

Helper functions that call `inject()` (sometimes called "inject functions" or composables) are powerful, but:

1. They only work in an injection context. Calling them in a click handler throws `NG0203`.
2. They hide dependencies. A reader can't see what the class depends on from its constructor.
3. Testing needs `TestBed` or `runInInjectionContext`.
4. They capture the injector where they're called, which might not be the one you expect (for example, a root effect vs a component effect).

```ts
export function injectRouteParam(name: string) {
  assertInInjectionContext(injectRouteParam);
  const route = inject(ActivatedRoute);
  return toSignal(route.paramMap.pipe(map((p) => p.get(name))), {
    initialValue: null,
  });
}

export class OrderPage {
  orderId = injectRouteParam("id"); // fine, field initializer
}
```

Using `assertInInjectionContext` gives a clear error message when someone calls it in the wrong place.

## 340: How do you switch implementations based on runtime config?

Use a factory provider that reads config and returns the right implementation.

```ts
export abstract class StorageBackend {
  abstract get(key: string): string | null;
  abstract set(key: string, value: string): void;
}

export const appConfig: ApplicationConfig = {
  providers: [
    {
      provide: StorageBackend,
      useFactory: () => {
        const config = inject(APP_CONFIG);
        const platformId = inject(PLATFORM_ID);
        if (!isPlatformBrowser(platformId)) return new MemoryStorage();
        return config.useSessionStorage
          ? new SessionStorage()
          : new LocalStorage();
      },
    },
  ],
};
```

The factory runs once, the first time the token is injected. If the config is loaded asynchronously, make sure it's loaded in `provideAppInitializer` before anything injects `StorageBackend`.

## 341: What is a RouteReuseStrategy?

By default, the router destroys a component when you navigate away and creates a new one when you come back. A custom `RouteReuseStrategy` can store and reuse component instances, keeping their state (like scroll position or filled filters).

```ts
@Injectable()
export class KeepAliveStrategy extends BaseRouteReuseStrategy {
  private stored = new Map<string, DetachedRouteHandle>();

  override shouldDetach(route: ActivatedRouteSnapshot) {
    return route.data["keepAlive"] === true;
  }
  override store(
    route: ActivatedRouteSnapshot,
    handle: DetachedRouteHandle | null,
  ) {
    if (handle) this.stored.set(route.routeConfig!.path!, handle);
  }
  override shouldAttach(route: ActivatedRouteSnapshot) {
    return this.stored.has(route.routeConfig?.path ?? "");
  }
  override retrieve(route: ActivatedRouteSnapshot) {
    return this.stored.get(route.routeConfig?.path ?? "") ?? null;
  }
}

providers: [{ provide: RouteReuseStrategy, useClass: KeepAliveStrategy }];
```

Be careful: stored components stay in memory and keep their subscriptions, and they don't get `ngOnInit` again when reattached.

## 342: How do you write a custom TitleStrategy?

A `TitleStrategy` builds the page title from the route's `title` after each navigation. A custom one can add a suffix or translate titles.

```ts
@Injectable({ providedIn: "root" })
export class AppTitleStrategy extends TitleStrategy {
  private title = inject(Title);

  override updateTitle(snapshot: RouterStateSnapshot) {
    const pageTitle = this.buildTitle(snapshot);
    this.title.setTitle(pageTitle ? `${pageTitle} | My Shop` : "My Shop");
  }
}

providers: [
  provideRouter(routes),
  { provide: TitleStrategy, useClass: AppTitleStrategy },
];
```

`title` on a route can also be a `ResolveFn<string>` for dynamic titles like a product name.

## 343: What is a UrlMatcher?

A `UrlMatcher` is a function that replaces the normal `path` matching when you need custom rules, such as matching usernames that start with `@`.

```ts
export function atUsernameMatcher(
  segments: UrlSegment[],
): UrlMatchResult | null {
  if (segments.length === 1 && /^@\w+$/.test(segments[0].path)) {
    return {
      consumed: segments,
      posParams: { username: new UrlSegment(segments[0].path.slice(1), {}) },
    };
  }
  return null;
}

export const routes: Routes = [
  { matcher: atUsernameMatcher, component: UserProfile },
];
// /@ann -> UserProfile with username = 'ann'
```

A route can have either `path` or `matcher`, not both.

## 344: How do you customize how URLs are parsed and serialized?

Provide your own `UrlSerializer`. A common reason is to make URLs case-insensitive or to handle special characters.

```ts
@Injectable()
export class LowerCaseUrlSerializer extends DefaultUrlSerializer {
  override parse(url: string): UrlTree {
    const [path, query] = url.split("?");
    return super.parse(path.toLowerCase() + (query ? `?${query}` : ""));
  }
}

providers: [{ provide: UrlSerializer, useClass: LowerCaseUrlSerializer }];
```

Only lowercase the path, not query params, since their values might be case sensitive.

## 345: In what order do guards and resolvers run?

For a navigation, the router:

1. Matches routes, running `canMatch` guards (and loading lazy route configs).
2. Runs `canDeactivate` on routes being left, from the deepest child up.
3. Runs `canActivateChild` and `canActivate` from the top parent down.
4. If all pass, runs resolvers.
5. Activates components.

Multiple guards in one array run in parallel, but the router waits for them in order of priority: if an earlier guard in the array returns a redirect, that wins even if a later one finished first.

`runGuardsAndResolvers` controls when they rerun for the **same** route:

```ts
{
  path: 'list',
  component: List,
  resolve: { items: itemsResolver },
  runGuardsAndResolvers: 'paramsOrQueryParamsChange',
}
```

Options include `'paramsChange'` (default), `'pathParamsChange'`, `'paramsOrQueryParamsChange'`, `'always'` or a custom function.

## 346: What does paramsInheritanceStrategy do?

By default, a child route only inherits params and data from its parent in some cases (when the parent is componentless or has an empty path). With `'always'`, children always inherit everything from parents.

```ts
provideRouter(
  routes,
  withRouterConfig({ paramsInheritanceStrategy: "always" }),
  withComponentInputBinding(),
);
```

```ts
// route: projects/:projectId -> tasks/:taskId
export class TaskDetails {
  projectId = input.required<string>(); // from the parent route
  taskId = input.required<string>();
}
```

This is especially handy with `withComponentInputBinding()`, so deeply nested components can get parent params as inputs.

## 347: How do you reload the current route?

Navigating to the same URL does nothing by default. To make it rerun guards and resolvers:

```ts
provideRouter(routes, withRouterConfig({ onSameUrlNavigation: "reload" }));
```

```ts
{ path: 'feed', component: Feed, resolve: { posts: postsResolver }, runGuardsAndResolvers: 'always' }

this.router.navigateByUrl('/feed', { onSameUrlNavigation: 'reload' });
```

Note that this reruns guards and resolvers, but the component is reused, not recreated. If you need fresh component state, it's often simpler to reload data through a service (or `resource.reload()`) instead of going through the router.

## 348: How do you handle navigation errors globally?

Use `withNavigationErrorHandler()`. It runs in an injection context and can return a `RedirectCommand`.

```ts
provideRouter(
  routes,
  withNavigationErrorHandler((error) => {
    const router = inject(Router);
    inject(ErrorLogger).log(error.error);

    if (
      error.error instanceof HttpErrorResponse &&
      error.error.status === 404
    ) {
      return new RedirectCommand(router.parseUrl("/not-found"));
    }
    return new RedirectCommand(router.parseUrl("/error"));
  }),
);
```

Navigation errors include failed lazy loading (often after a new deploy, when old chunk files are gone), resolver errors and guard errors.

## 349: How do you handle stale chunks after a new deployment?

After a deploy, users with the old app open may try to lazy load a chunk that no longer exists, and navigation fails with a "Failed to fetch dynamically imported module" error.

Solutions:

- Keep old chunk files on the server for a while after deploy.
- Catch the error and reload the page:

```ts
withNavigationErrorHandler(({ error }) => {
  if (
    error instanceof Error &&
    /dynamically imported module|Loading chunk/i.test(error.message)
  ) {
    location.reload();
  }
});
```

- With a service worker (`@angular/pwa`), use `SwUpdate` to detect new versions and ask the user to reload.

## 350: How do you implement token refresh in an interceptor?

When a request fails with 401, refresh the token once, then retry. If several requests fail at the same time, they should wait for the same refresh instead of each starting one.

```ts
@Injectable({ providedIn: "root" })
export class TokenRefresher {
  private auth = inject(AuthService);
  private refresh$: Observable<string> | null = null;

  refresh(): Observable<string> {
    this.refresh$ ??= this.auth.refreshToken().pipe(
      finalize(() => (this.refresh$ = null)),
      shareReplay(1),
    );
    return this.refresh$;
  }
}

export const refreshInterceptor: HttpInterceptorFn = (req, next) => {
  const refresher = inject(TokenRefresher);
  const auth = inject(AuthService);

  if (req.url.includes("/auth/refresh")) return next(req);

  return next(withToken(req, auth.accessToken())).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status !== 401) return throwError(() => err);
      return refresher.refresh().pipe(
        switchMap((token) => next(withToken(req, token))),
        catchError((refreshErr) => {
          auth.logout();
          return throwError(() => refreshErr);
        }),
      );
    }),
  );
};

function withToken(req: HttpRequest<unknown>, token: string | null) {
  return token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;
}
```

Skip the refresh endpoint itself, or a failing refresh would loop.

## 351: When should you use the route snapshot vs observables?

`ActivatedRoute.snapshot` is the route state at the moment you read it. If the router **reuses** the component (for example navigating from `/products/1` to `/products/2`), the constructor and `ngOnInit` don't run again, so a snapshot read there becomes stale.

```ts
// stale when navigating between products
id = this.route.snapshot.paramMap.get("id");

// always current
id = toSignal(this.route.paramMap.pipe(map((p) => p.get("id"))));

// or with withComponentInputBinding(), the input updates on each navigation
id = input.required<string>();
```

Snapshots are fine in guards and resolvers, where you get a fresh snapshot for each navigation, or when you're sure the component is never reused with different params.

## 352: How would you build a smarter preloading strategy?

Preload only what is likely to be used and only on good connections. For example, preload routes that have links visible on the screen, and skip preloading on slow networks.

```ts
@Injectable({ providedIn: "root" })
export class NetworkAwarePreloading implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<unknown>): Observable<unknown> {
    const conn = (navigator as any).connection;
    const slow = conn?.saveData || /2g/.test(conn?.effectiveType ?? "");
    if (slow || !route.data?.["preload"]) {
      return of(null);
    }
    return timer(2000).pipe(switchMap(() => load())); // wait until the app has settled
  }
}
```

The `ngx-quicklink` library does the "preload visible links" idea for you. `@defer` with `prefetch on idle` / `prefetch on hover` is the same idea at the template level.

## 353: How does the SSR server (server.ts) work?

`ng add @angular/ssr` creates a `server.ts` that uses Express with Angular's `AngularNodeAppEngine`.

```ts
import {
  AngularNodeAppEngine,
  createNodeRequestHandler,
  isMainModule,
  writeResponseToNodeResponse,
} from "@angular/ssr/node";
import express from "express";
import { join } from "node:path";

const browserDistFolder = join(import.meta.dirname, "../browser");
const app = express();
const angularApp = new AngularNodeAppEngine();

// your own API routes can go here: app.get('/api/...', ...)

app.use(
  express.static(browserDistFolder, {
    maxAge: "1y",
    index: false,
    redirect: false,
  }),
);

app.use((req, res, next) => {
  angularApp
    .handle(req)
    .then((response) =>
      response ? writeResponseToNodeResponse(response, res) : next(),
    )
    .catch(next);
});

if (isMainModule(import.meta.url)) {
  app.listen(process.env["PORT"] || 4000);
}

export const reqHandler = createNodeRequestHandler(app);
```

Static files are served first. Everything else goes to `angularApp.handle()`, which matches the URL against the server routes and either serves a prerendered file, renders the page, or returns `null`. `reqHandler` is used by the dev server and by some hosting platforms.

## 354: What render modes can each route use?

In `app.routes.server.ts`, each route can have its own render mode:

- `RenderMode.Server`: rendered on the server for each request.
- `RenderMode.Prerender`: rendered at build time to a static HTML file.
- `RenderMode.Client`: not rendered on the server, the browser renders it like a normal SPA.

```ts
export const serverRoutes: ServerRoute[] = [
  { path: "", renderMode: RenderMode.Prerender },
  {
    path: "blog/:slug",
    renderMode: RenderMode.Prerender,
    async getPrerenderParams() {
      const posts = inject(PostService);
      const slugs = await posts.getAllSlugs();
      return slugs.map((slug) => ({ slug }));
    },
    fallback: PrerenderFallback.Server, // unknown slugs are rendered on demand
  },
  { path: "dashboard/**", renderMode: RenderMode.Client },
  { path: "**", renderMode: RenderMode.Server },
];
```

```ts
// app.config.server.ts
const serverConfig: ApplicationConfig = {
  providers: [provideServerRendering(withRoutes(serverRoutes))],
};
export const config = mergeApplicationConfig(appConfig, serverConfig);
```

`getPrerenderParams` tells the build which parameter values to prerender for a dynamic route.

## 355: What is incremental hydration?

With full hydration, the whole page is hydrated as soon as the JavaScript loads. With incremental hydration, parts of the page inside `@defer` blocks stay as static server HTML, and their code isn't even downloaded until a trigger fires.

```ts
provideClientHydration(withIncrementalHydration());
```

```html
<app-header />

@defer (hydrate on viewport) {
<app-product-reviews [productId]="id()" />
} @placeholder {
<div>Reviews</div>
} @defer (hydrate on interaction) {
<app-size-picker />
} @defer (hydrate never) {
<app-static-footer />
}
```

The user sees the server-rendered reviews immediately. The JavaScript for `ProductReviews` loads and hydrates only when it scrolls into view. Event replay makes sure a click on a not-yet-hydrated block is replayed after hydration.

## 356: What hydration triggers are available?

The `hydrate` triggers mirror the normal `@defer` triggers:

- `hydrate on idle`
- `hydrate on viewport`
- `hydrate on interaction`
- `hydrate on hover`
- `hydrate on immediate`
- `hydrate on timer(500ms)`
- `hydrate when condition`
- `hydrate never`: stays static HTML forever (still rendered on the server)

You can combine normal triggers and hydration triggers:

```html
@defer (on viewport; hydrate on interaction) {
<app-chat-widget />
}
```

`on viewport` is used on a client-side navigation (no server HTML), `hydrate on interaction` is used when the page came from the server. Nested deferred blocks hydrate from the top down: hydrating a child also hydrates its parent blocks first.

## 357: What causes hydration mismatch errors and how do you fix them?

Hydration expects the DOM in the browser to match what Angular would render. Errors like `NG0500` happen when it doesn't.

Common causes:

- **Invalid HTML** that the browser fixes on its own, like a `<div>` inside a `<p>` or a `<table>` without `<tbody>`.
- **Direct DOM manipulation** with `nativeElement.innerHTML`, `appendChild`, or third-party libraries that change the DOM before hydration.
- **Different data** on server and client, like `new Date()`, random IDs, or browser-only values rendered in the template.
- CDN or proxy tools that modify HTML (some "optimization" features strip comment nodes Angular needs).

Fixes:

- Fix the HTML structure.
- Move DOM manipulation into `afterNextRender`.
- Make server and client produce the same data (transfer it with `TransferState` / HTTP transfer cache).
- As a last resort, skip hydration for one component:

```html
<app-legacy-chart ngSkipHydration />
```

`ngSkipHydration` makes Angular throw away and re-render that component in the browser.

## 358: What is the HTTP transfer cache?

When SSR is used, requests made on the server are cached and sent to the browser inside the HTML. During hydration, the same requests in the browser are served from that cache, so the API isn't called twice and the page doesn't flicker.

It's on by default with `provideClientHydration()`. You can configure it:

```ts
provideClientHydration(
  withHttpTransferCacheOptions({
    includePostRequests: true,
    includeHeaders: ["ETag"],
    filter: (req) => !req.url.includes("/api/user/"),
  }),
);
```

You can also disable it per request:

```ts
this.http.get("/api/stock", { transferCache: false });
```

By default, only GET and HEAD requests without `Authorization` headers are cached. Be careful not to cache private user data into HTML that might be cached by a CDN.

## 359: How do you use TransferState manually?

For data that doesn't come from `HttpClient` (like a direct database call or `fetch` with a custom client), store it in `TransferState` on the server and read it in the browser.

```ts
const PRODUCTS_KEY = makeStateKey<Product[]>("products");

@Injectable({ providedIn: "root" })
export class ProductStore {
  private state = inject(TransferState);
  private platformId = inject(PLATFORM_ID);

  async getProducts(): Promise<Product[]> {
    const cached = this.state.get(PRODUCTS_KEY, null);
    if (cached) {
      this.state.remove(PRODUCTS_KEY);
      return cached;
    }

    const products = await loadProductsSomehow();
    if (isPlatformServer(this.platformId)) {
      this.state.set(PRODUCTS_KEY, products);
    }
    return products;
  }
}
```

The data is serialized into a `<script>` tag as JSON, so only put serializable data there.

## 360: How do you access the request on the server?

Angular provides injection tokens from `@angular/core`:

- `REQUEST`: the incoming `Request` (Fetch API object)
- `RESPONSE_INIT`: a `ResponseInit` you can change (status, headers)
- `REQUEST_CONTEXT`: any extra context passed from the server code

They are `null` in the browser and during prerendering, so inject them as optional.

```ts
export class LocaleService {
  private request = inject(REQUEST, { optional: true });

  preferredLanguage(): string {
    return (
      this.request?.headers.get("accept-language")?.split(",")[0] ??
      navigator.language
    );
  }
}
```

```ts
// server.ts: passing context
angularApp.handle(req, { tenantId: req.headers["x-tenant"] });

// in Angular
const ctx = inject(REQUEST_CONTEXT, { optional: true }) as {
  tenantId?: string;
} | null;
```

## 361: How do you return a 404 status from SSR?

Set the status on `RESPONSE_INIT` from the not-found component, or set it in the server route config.

```ts
@Component({
  selector: "app-not-found",
  template: `<h1>Page not found</h1>`,
})
export class NotFound {
  constructor() {
    const responseInit = inject(RESPONSE_INIT, { optional: true });
    if (responseInit) {
      responseInit.status = 404;
    }
  }
}
```

```ts
export const serverRoutes: ServerRoute[] = [
  {
    path: "**",
    renderMode: RenderMode.Server,
    status: 404,
    headers: { "Cache-Control": "no-store" },
  },
];
```

Without this, search engines see a `200 OK` for missing pages ("soft 404"). Redirects defined with `redirectTo` in routes are sent as real HTTP redirects by the server.

## 362: How do you cache SSR pages?

Rendering on every request costs CPU. Common strategies:

1. **Prerender** pages that are the same for everyone.
2. **HTTP cache headers** so a CDN caches rendered pages:

```ts
{ path: 'products/:id', renderMode: RenderMode.Server, headers: { 'Cache-Control': 'public, max-age=60, stale-while-revalidate=300' } }
```

3. **Application-level cache** in `server.ts` (for example an in-memory LRU or Redis keyed by URL) for public pages.

Never cache pages that contain user-specific data in a shared cache. Separate public pages (cacheable) from personalized ones (`no-store`, or `RenderMode.Client`).

## 363: How do you provide different services on the server and in the browser?

Put browser providers in `app.config.ts` and override them in `app.config.server.ts`. The server config is merged on top.

```ts
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [{ provide: StorageBackend, useClass: LocalStorageBackend }],
};

// app.config.server.ts
const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(withRoutes(serverRoutes)),
    { provide: StorageBackend, useClass: NoopStorageBackend },
  ],
};
export const config = mergeApplicationConfig(appConfig, serverConfig);
```

This keeps `isPlatformBrowser` checks out of your business logic.

## 364: Why might an SSR render never finish or time out?

The server waits until the app is stable before sending the HTML. The app never becomes stable if there's always pending work:

- `setInterval` or polling started on the server
- A long-lived Observable registered as a pending task (`pendingUntilEvent` on something that never emits)
- An `HttpClient` request to an API that doesn't respond (no timeout)
- Websocket connections opened on the server

Fixes:

```ts
constructor() {
  // start polling only in the browser
  afterNextRender(() => {
    this.pollId = setInterval(() => this.refresh(), 5000);
  });
}
```

Also add timeouts to server-side HTTP calls (`timeout()` operator) so a slow API doesn't block rendering.

## 365: How do you handle authentication with SSR?

The server renders on behalf of the user, so it needs the user's credentials. Since `localStorage` doesn't exist on the server, cookies are the usual choice.

- Store the session in an `HttpOnly`, `Secure`, `SameSite` cookie.
- On the server, read the cookie from the `REQUEST` token and forward it to API calls with an interceptor:

```ts
export const forwardCookiesInterceptor: HttpInterceptorFn = (req, next) => {
  const request = inject(REQUEST, { optional: true });
  const cookie = request?.headers.get("cookie");
  if (cookie && req.url.startsWith(inject(API_URL))) {
    req = req.clone({ setHeaders: { cookie } });
  }
  return next(req);
};
```

- Don't let personalized pages be cached by a CDN.
- Don't put the auth token in `TransferState` or the transfer cache.

If the logged-in part of the app doesn't need SEO, rendering it with `RenderMode.Client` is often simpler.

## 366: Can Angular SSR run outside Node.js?

Yes. `AngularAppEngine` (from `@angular/ssr`) works with the standard Fetch API `Request` and `Response`, so it can run on edge and serverless platforms like Cloudflare Workers, Deno or Netlify Edge.

```ts
import { AngularAppEngine, createRequestHandler } from "@angular/ssr";

const angularApp = new AngularAppEngine();

export const reqHandler = createRequestHandler(async (req: Request) => {
  const res = await angularApp.handle(req);
  return res ?? new Response("Not found", { status: 404 });
});
```

`AngularNodeAppEngine` is the Node-specific wrapper. Code that uses Node APIs (like `fs`) won't work on edge runtimes.

## 367: How does event replay work?

Between the moment server HTML appears and the moment hydration finishes, the page is visible but not interactive. Event replay (`withEventReplay()`) solves this:

1. The server adds a tiny inline script and marks elements that have event listeners.
2. The script captures events like `click`, `input` and `keydown` at the document level and stores them.
3. After hydration (or after a deferred block hydrates), Angular replays the stored events on the right elements, in order.

This uses the same library Google built for its own products (JSAction). Event replay is enabled by default in new SSR projects.

## 368: How does i18n work with SSR?

With build-time i18n, the build produces one app per locale (`dist/app/browser/en`, `dist/app/browser/de`, ...), and the server bundle includes all of them. `AngularNodeAppEngine` picks the right locale based on the URL prefix, using the `baseHref` / `subPath` of each locale.

```json
"i18n": {
  "sourceLocale": "en-US",
  "locales": {
    "de": { "translation": "src/locale/messages.de.xlf", "subPath": "de" }
  }
},
"options": { "localize": true }
```

`/de/products` renders the German version. You still need to handle redirects from `/` to the user's preferred locale yourself (for example from the `Accept-Language` header in `server.ts`).

## 369: How do you analyze bundle size?

1. Build with stats:

```bash
ng build --stats-json
```

2. Open `dist/<app>/stats.json` in the esbuild bundle analyzer (esbuild.github.io/analyze) or a tool like `source-map-explorer` (build with source maps).

3. Check the CLI output: it lists initial and lazy chunks with their sizes, and warns when budgets are exceeded.

Things to look for:

- Large libraries in the initial bundle that could be lazy loaded
- Duplicate copies of a library
- CommonJS dependencies (the CLI warns, because they can't be tree-shaken well)
- Whole libraries imported when only one function is used (`lodash` vs `lodash-es` functions)
- Locale data or icon sets that are bigger than needed

## 370: How do you profile an Angular app?

- **Angular DevTools Profiler**: records change detection cycles, shows which components were checked and how long each took. It also shows whether a cycle came from a signal, event, etc.
- **Chrome DevTools Performance panel**: since Angular 20 there's a custom Angular track. Run `ng.enableProfiling()` in the console (dev mode), then record. You see component rendering, change detection and lifecycle hooks next to the browser's own timeline.
- **Lighthouse / Web Vitals** for real-world metrics (LCP, CLS, INP).

Look for components that are checked very often, expensive template expressions, long tasks during scroll or typing, and repeated change detection cycles from timers or third-party code.

## 371: How do you speed up a slow list or table?

1. Make sure `@for` has a good `track` key (a stable id).
2. Use OnPush and signals for rows, so a change in one row doesn't recheck all.
3. Move per-row computations out of the template (precompute in a `computed()` or in the data).
4. Paginate or use virtual scrolling (`cdk-virtual-scroll-viewport`) for thousands of rows.
5. Defer rendering below-the-fold parts with `@defer (on viewport)`.
6. Avoid heavy components in every row (like a full menu component per row, create one shared menu instead).
7. Debounce filters and sorting inputs.

Measure with the DevTools profiler before and after, so you know which change helped.

## 372: How do you make the initial bundle smaller?

- Lazy load routes with `loadComponent` / `loadChildren`.
- Use `@defer` for heavy parts of a page (charts, editors, maps, comments).
- Remove unused dependencies and polyfills. Zoneless apps don't need `zone.js`.
- Prefer ES module libraries over CommonJS ones.
- Import only what you use (`import { debounce } from 'lodash-es'`).
- Avoid "barrel" files with side effects that pull in unrelated code.
- Make sure services use `providedIn: 'root'` (tree-shakable) instead of being listed in app-wide `providers` when not needed.
- Keep `@placeholder` content small, since it's in the main chunk.
- Set budgets so the build warns when the size grows.

## 373: How do you find memory leaks in an Angular app?

Typical causes:

- Subscriptions not cleaned up (`interval`, store selectors, `fromEvent`)
- Event listeners added manually and never removed
- Timers not cleared
- Detached DOM nodes kept by references in services
- Services holding big caches with no limit
- Third-party libraries not destroyed (charts, maps)

How to find them:

1. In Chrome DevTools, take a heap snapshot, navigate to a page and back several times, take another snapshot, and compare. Search for your component class names. If the count keeps growing, something holds them.
2. Look for "Detached" DOM trees.

Fixes: `takeUntilDestroyed()`, `DestroyRef.onDestroy()`, `toSignal()`, `async` pipe, effect `onCleanup`, and calling `destroy()` on third-party instances.

## 374: How do you use Web Workers in Angular?

Web Workers run code on a separate thread, so heavy computations don't block the UI.

```bash
ng generate web-worker image-processor
```

```ts
// image-processor.worker.ts
addEventListener("message", ({ data }) => {
  const result = applyFilters(data.pixels, data.filters);
  postMessage(result);
});
```

```ts
export class Editor {
  result = signal<ImageData | null>(null);
  private worker = new Worker(
    new URL("./image-processor.worker", import.meta.url),
    {
      type: "module",
    },
  );

  constructor() {
    this.worker.onmessage = ({ data }) => this.result.set(data);
    inject(DestroyRef).onDestroy(() => this.worker.terminate());
  }

  process(pixels: ImageData) {
    this.worker.postMessage({ pixels, filters: ["blur"] });
  }
}
```

Workers can't access the DOM. Setting a signal from `onmessage` updates the UI, also in zoneless apps. Workers don't run during SSR, so create them in the browser only.

## 375: How do you improve Core Web Vitals in Angular?

**LCP (Largest Contentful Paint):**

- Use SSR or prerendering
- Mark the hero image with `priority` in `NgOptimizedImage`
- Keep the initial bundle small, lazy load the rest

**CLS (Cumulative Layout Shift):**

- Always give images `width`/`height` (`NgOptimizedImage` enforces it)
- Use `@placeholder` blocks with the same size as the deferred content
- Avoid hydration mismatches that re-render parts of the page

**INP (Interaction to Next Paint):**

- Keep event handlers fast; move heavy work to Web Workers
- Use OnPush, signals and zoneless to reduce change detection work
- Use incremental hydration so less JavaScript runs at startup
- Debounce expensive handlers (search, resize)

## 376: What is layout thrashing and how do you avoid it?

Layout thrashing happens when code reads layout (like `offsetHeight`) and writes styles in a loop. Each read after a write forces the browser to recalculate layout.

```ts
// bad: read, write, read, write...
for (const el of items) {
  el.style.height = el.scrollHeight + "px";
}
```

Group reads and writes. Angular's render hooks have phases for this:

```ts
afterNextRender({
  earlyRead: () => items.map((el) => el.scrollHeight),
  write: (heights) =>
    items.forEach((el, i) => (el.style.height = heights[i] + "px")),
});
```

When many components use these phases, Angular runs all `earlyRead` callbacks, then all `write` callbacks, and so on, which keeps the browser from recalculating layout between them.

## 377: How do you cache HTTP data on the client?

Options, from simple to more complete:

1. **Keep data in a signal service**: load once, return the cached value next time.

```ts
@Injectable({ providedIn: "root" })
export class CategoryStore {
  private http = inject(HttpClient);
  readonly categories = httpResource<Category[]>(() => "/api/categories", {
    defaultValue: [],
  });
}
```

Since the store is a root singleton, the resource loads once and every component reads the same value.

2. **`shareReplay(1)`** on an Observable for static data.
3. **An interceptor cache** keyed by URL, with a time-to-live, for GET requests.
4. **A library** like TanStack Query for Angular, which handles stale times, background refetching and invalidation.
5. **HTTP caching** (`Cache-Control`, `ETag`) from the server, which the browser handles for free.

Always think about invalidation: after a POST that changes data, clear or update the cache.

## 378: How do you keep large reactive forms fast?

- Use `updateOn: 'blur'` for controls with expensive validators.
- Debounce `valueChanges` subscriptions that do heavy work.
- Pass `{ emitEvent: false }` when setting values in code if nobody needs the event.
- Avoid one huge form re-rendering everything: split it into child components with OnPush, each owning a part of the form.
- Use `@defer` or tabs/steps so not all sections render at once.
- For long `FormArray`s, track by a stable id and consider virtual scrolling.
- Don't call methods like `getErrors(control)` in templates for every field; compute error messages once per change.

## 379: What is zone pollution?

In Zone.js apps, zone pollution is when code inside the Angular zone triggers a lot of unnecessary change detection runs. Typical sources are third-party libraries with their own `requestAnimationFrame` loops, `setInterval`s, or frequent events (mousemove, scroll).

Angular DevTools' profiler shows many change detection cycles with no visible changes, which is a sign of this.

Fixes:

```ts
private zone = inject(NgZone);

constructor() {
  afterNextRender(() => {
    this.zone.runOutsideAngular(() => {
      this.chart = new HeavyChartLib(this.el.nativeElement); // its timers won't trigger CD
    });
  });
}
```

Moving to zoneless removes this whole class of problems.

## 380: How do you structure a large Angular application?

A common approach is to group by feature (domain), not by type.

```
src/app/
  core/            # app-wide singletons: auth, http interceptors, error handler, layout shell
  shared/          # reusable UI components, pipes, directives (no business logic)
  features/
    orders/
      data/        # services, stores, API clients, models
      ui/          # presentational components
      feature/     # routed smart components
      orders.routes.ts
    customers/
      ...
  app.routes.ts
  app.config.ts
```

Guidelines:

- Each feature is lazy loaded through its routes file.
- Features don't import from each other's internals, only through public APIs.
- Shared UI doesn't know about features.
- Enforce boundaries with lint rules (for example Nx module boundaries or `eslint-plugin-boundaries`).
- Use path aliases for clean imports.

## 381: What is Nx and why would you use it with Angular?

Nx is a build system and monorepo tool. With Angular it's often used for large codebases with several apps and many libraries.

Features:

- Splitting code into many small libraries with clear boundaries
- Module boundary lint rules (for example, "feature libs can't import other feature libs")
- "Affected" commands: only build and test projects changed by a commit
- Local and remote caching of builds and tests
- Generators similar to Angular schematics
- Dependency graph visualization

```bash
npx create-nx-workspace@latest my-org --preset=angular-monorepo
nx affected -t test
nx graph
```

The Angular CLI alone also supports multiple projects in one workspace, but without these extra tools.

## 382: How do micro frontends work with Angular?

Micro frontends split one product into separately built and deployed apps. In Angular the common tool is **Native Federation** (`@angular-architects/native-federation`), which works with the esbuild-based builder. Older webpack setups use Module Federation.

```ts
// shell: load a remote's routes at runtime
export const routes: Routes = [
  {
    path: "orders",
    loadChildren: () =>
      loadRemoteModule("orders", "./routes").then((m) => m.ORDER_ROUTES),
  },
];
```

Things to plan for:

- Shared dependencies (Angular itself, RxJS) must be compatible between apps.
- Communication between micro frontends (URL, custom events, a small shared library).
- Consistent design system across teams.
- More complex local development and testing.

Micro frontends solve team and deployment scaling problems. For a single team, a well-structured monorepo is usually simpler.

## 383: What is the facade pattern in Angular?

A facade is a service that gives components a simple API and hides where the data comes from (HTTP, store, cache).

```ts
@Injectable({ providedIn: "root" })
export class OrdersFacade {
  private store = inject(OrdersStore);
  private api = inject(OrdersApi);

  readonly orders = this.store.orders;
  readonly loading = this.store.loading;

  load() {
    this.store.setLoading(true);
    this.api.getOrders().subscribe((orders) => this.store.setOrders(orders));
  }

  cancel(id: number) {
    this.api.cancel(id).subscribe(() => this.store.markCancelled(id));
  }
}
```

Components only use the facade. You can later replace the store implementation (signal service, SignalStore, NgRx) without touching components.

## 384: How would you design error handling across an Angular app?

Handle errors at the right level:

1. **HTTP layer** (interceptor): retries for safe requests, redirect on 401, show a generic message for 5xx, map server errors to a consistent shape.
2. **Feature/service layer**: turn errors into state (`error` signal, resource `error()`), with fallback values where that makes sense.
3. **Component layer**: show error UI (inline messages, empty states, retry buttons). `@defer` has an `@error` block for loading failures.
4. **Global** `ErrorHandler`: log unexpected errors to a monitoring service. Add `provideBrowserGlobalErrorListeners()`.
5. **Router**: `withNavigationErrorHandler()` for failed navigations and chunk loading.

Also: don't swallow errors silently, include context (user action, URL) in logs, and show users something they can act on.

## 385: Where should you store auth tokens in the browser?

There's no perfect answer, only tradeoffs:

- **`HttpOnly` cookie**: JavaScript can't read it, so XSS can't steal it. Needs CSRF protection (SameSite cookies plus the XSRF token mechanism). Works with SSR. Usually the safest choice.
- **Memory (a signal in a service)**: not readable after the page reloads, so you need a refresh mechanism (often an `HttpOnly` refresh cookie). XSS can still use it while the page is open.
- **`localStorage` / `sessionStorage`**: simple, but any XSS can read it.

Whatever you choose: keep access tokens short-lived, never log tokens, and focus on preventing XSS in the first place (no `bypassSecurityTrust` with user data, a strict CSP, Trusted Types).

## 386: What are Trusted Types and how does Angular support them?

Trusted Types is a browser feature that blocks dangerous DOM sinks (like `innerHTML` or `script.src`) unless the value is a special "trusted" object created by an approved policy. It stops many DOM-based XSS attacks.

Angular supports it: its sanitizer and internal code create values through Angular policies. You enable it with a CSP header:

```
Content-Security-Policy: trusted-types angular angular#bundler; require-trusted-types-for 'script';
```

Policy names you may need:

- `angular`: for Angular's sanitized values
- `angular#unsafe-bypass`: if your app uses `bypassSecurityTrust*`
- `angular#unsafe-jit`: if you use the JIT compiler
- `angular#bundler`: for lazy loaded chunks

Third-party libraries that write to `innerHTML` directly will break, which shows where your risks are.

## 387: What security risks should you look for in an Angular code review?

- `bypassSecurityTrust*` used with data that could come from users
- Direct DOM access: `nativeElement.innerHTML`, `insertAdjacentHTML`, `document.write`
- Building templates or components from user strings (JIT compile at runtime)
- `[href]` bound to user-controlled URLs without validation (Angular blocks `javascript:` but not phishing links)
- Secrets (API keys, private tokens) in `environment.ts`, which end up in the bundle
- Tokens or personal data in `TransferState` or the HTTP transfer cache
- SSR pages with user data cached by a CDN
- Missing server-side checks, relying only on guards (guards are UX, not security)
- Outdated Angular versions or dependencies with known vulnerabilities (`npm audit`)
- Open redirects using a `returnUrl` query param without checking it's internal

## 388: How do you implement feature flags?

Load flags at startup and expose them as signals. Use them in routes, templates and services.

```ts
@Injectable({ providedIn: "root" })
export class FeatureFlags {
  private http = inject(HttpClient);
  private flags = signal<Record<string, boolean>>({});

  isOn(name: string) {
    return computed(() => this.flags()[name] === true);
  }

  async load() {
    this.flags.set(
      await firstValueFrom(
        this.http.get<Record<string, boolean>>("/api/flags"),
      ),
    );
  }
}

export const featureGuard =
  (flag: string): CanMatchFn =>
  () =>
    inject(FeatureFlags).isOn(flag)();
```

```ts
providers: [provideAppInitializer(() => inject(FeatureFlags).load())];

{ path: 'beta-reports', canMatch: [featureGuard('newReports')], loadComponent: () => import('./new-reports') }
```

Using `canMatch` means users without the flag don't download the code. Flags are UI switches, so the server must still enforce access.

## 389: What are secondary entry points in a library?

A secondary entry point is a sub-path of a library with its own public API, like `@my-org/ui/button` and `@my-org/ui/table`. Each is built as its own module.

```
projects/ui/
  src/public-api.ts            # @my-org/ui
  button/
    ng-package.json
    src/public-api.ts          # @my-org/ui/button
  table/
    ng-package.json
    src/public-api.ts          # @my-org/ui/table
```

```json
// button/ng-package.json
{ "lib": { "entryFile": "src/public-api.ts" } }
```

Benefits: consumers import only what they need, entry points can have different dependencies (the table can depend on the CDK while the button doesn't), and builds stay clear. Angular Material uses this pattern (`@angular/material/button`).

## 390: How do you share state between micro frontends?

Keep it minimal. Options:

- **URL**: route and query params are the simplest shared state.
- **Custom DOM events** on `window` for loose messages:

```ts
window.dispatchEvent(new CustomEvent("cart:updated", { detail: { count: 3 } }));
window.addEventListener("cart:updated", (e) =>
  this.count.set((e as CustomEvent).detail.count),
);
```

- **A small shared library** (shared as a singleton in the federation config) with a service holding signals.
- **Backend as the source of truth**, each app fetches what it needs.

Avoid sharing a big global store between independently deployed apps, it couples their releases.

## 391: How do you plan Angular upgrades in a large app?

- Upgrade regularly, one major version at a time. Skipping versions makes it harder.
- Read the update guide (`angular.dev/update-guide`) for your from/to versions.
- Update the CLI and core together: `ng update @angular/core @angular/cli`, then Material/CDK, then third-party libraries.
- Make sure third-party libraries support the new version first.
- Fix deprecation warnings before they become removals.
- Commit after each migration step so it's easy to review.
- Run the full test suite and a manual smoke test.
- In monorepos, upgrade everything together, since Angular packages must share the same version.

Staying within the supported versions also keeps you getting security fixes.

## 392: How do you add monitoring and logging to an Angular app?

- **Error tracking** (Sentry, Datadog, etc.): a custom `ErrorHandler` sends errors with context. Upload hidden source maps so stack traces are readable.
- **HTTP logging** in an interceptor: request duration, failures, correlation IDs (add an `X-Request-Id` header that the backend logs too).
- **Performance**: report Web Vitals from the browser (`web-vitals` library) to analytics.
- **Router events** for page views.

```ts
@Injectable()
export class MonitoringErrorHandler implements ErrorHandler {
  private router = inject(Router);

  handleError(error: unknown) {
    Sentry.captureException(error, { extra: { url: this.router.url } });
    console.error(error);
  }
}
```

Be careful not to send personal data or tokens in logs.

## 393: How do you support multiple themes or tenants?

Use CSS custom properties for design tokens and switch them at runtime.

```css
:root {
  --color-primary: #1565c0;
  --radius: 4px;
}
:root.theme-dark {
  --color-primary: #90caf9;
}
.btn {
  background: var(--color-primary);
  border-radius: var(--radius);
}
```

```ts
@Injectable({ providedIn: "root" })
export class ThemeService {
  private doc = inject(DOCUMENT);
  theme = signal<"light" | "dark">("light");

  constructor() {
    effect(() => {
      this.doc.documentElement.classList.toggle(
        "theme-dark",
        this.theme() === "dark",
      );
    });
  }

  applyTenant(tokens: Record<string, string>) {
    for (const [key, value] of Object.entries(tokens)) {
      this.doc.documentElement.style.setProperty(`--${key}`, value);
    }
  }
}
```

Angular Material themes are also built on CSS variables, so they can be changed the same way.

## 394: How do you make an Angular app work offline (PWA)?

Add the service worker package:

```bash
ng add @angular/pwa
```

This adds a web manifest, icons, `ngsw-config.json` and the provider:

```ts
provideServiceWorker("ngsw-worker.js", {
  enabled: !isDevMode(),
  registrationStrategy: "registerWhenStable:30000",
});
```

`ngsw-config.json` defines what to cache: app files (prefetched) and data groups (API responses with `freshness` or `performance` strategies).

Use `SwUpdate` to handle new versions:

```ts
export class UpdateNotifier {
  constructor() {
    inject(SwUpdate)
      .versionUpdates.pipe(
        filter((e) => e.type === "VERSION_READY"),
        takeUntilDestroyed(),
      )
      .subscribe(() => {
        if (confirm("A new version is available. Reload?")) location.reload();
      });
  }
}
```

The service worker only works over HTTPS (or localhost) and in production builds.

## 395: How do you handle real-time data with websockets and signals?

Wrap the websocket in a service, use RxJS for the connection, and expose signals to components.

```ts
@Injectable({ providedIn: "root" })
export class PriceFeed {
  private socket = webSocket<PriceUpdate>("wss://example.com/prices");
  private _prices = signal<Record<string, number>>({});
  readonly prices = this._prices.asReadonly();

  constructor() {
    this.socket
      .pipe(
        retry({
          delay: (_, attempt) => timer(Math.min(30_000, 1000 * 2 ** attempt)),
        }),
        takeUntilDestroyed(),
      )
      .subscribe((u) =>
        this._prices.update((p) => ({ ...p, [u.symbol]: u.price })),
      );
  }

  price(symbol: string) {
    return computed(() => this._prices()[symbol]);
  }
}
```

Tips: reconnect with backoff, only open the socket in the browser (not during SSR), and throttle very frequent updates (`bufferTime` or `auditTime`) before writing to signals.

## 396: How do you make a ControlValueAccessor validate itself?

Implement the `Validator` interface and provide `NG_VALIDATORS`. Then the parent form gets the component's validation errors automatically.

```ts
@Component({
  selector: "app-phone-input",
  template: `<input
    [value]="value()"
    (input)="onInput($event)"
    (blur)="onTouched()"
  />`,
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => PhoneInput),
      multi: true,
    },
    {
      provide: NG_VALIDATORS,
      useExisting: forwardRef(() => PhoneInput),
      multi: true,
    },
  ],
})
export class PhoneInput implements ControlValueAccessor, Validator {
  value = signal("");
  onChange: (v: string) => void = () => {};
  onTouched: () => void = () => {};

  writeValue(v: string) {
    this.value.set(v ?? "");
  }
  registerOnChange(fn: (v: string) => void) {
    this.onChange = fn;
  }
  registerOnTouched(fn: () => void) {
    this.onTouched = fn;
  }

  onInput(e: Event) {
    const v = (e.target as HTMLInputElement).value;
    this.value.set(v);
    this.onChange(v);
  }

  validate(control: AbstractControl): ValidationErrors | null {
    const v: string = control.value ?? "";
    return v === "" || /^\+?[0-9 ]{7,15}$/.test(v) ? null : { phone: true };
  }
}
```

If the validation rules can change (for example based on an input), call the function passed to `registerOnValidatorChange` so the form re-validates.

## 397: How do you build a dynamic form from a JSON config?

Describe fields in data, build the `FormGroup` from it, and render the right input per type.

```ts
interface FieldConfig {
  key: string;
  label: string;
  type: "text" | "number" | "select";
  required?: boolean;
  options?: { value: string; label: string }[];
}

@Component({
  selector: "app-dynamic-form",
  imports: [ReactiveFormsModule],
  template: `
    <form
      [formGroup]="form()"
      (ngSubmit)="submitted.emit(form().getRawValue())"
    >
      @for (field of fields(); track field.key) {
        <label>{{ field.label }}</label>
        @switch (field.type) {
          @case ("select") {
            <select [formControlName]="field.key">
              @for (o of field.options; track o.value) {
                <option [value]="o.value">{{ o.label }}</option>
              }
            </select>
          }
          @default {
            <input [type]="field.type" [formControlName]="field.key" />
          }
        }
      }
      <button>Submit</button>
    </form>
  `,
})
export class DynamicForm {
  fields = input.required<FieldConfig[]>();
  submitted = output<Record<string, unknown>>();

  form = computed(() => {
    const controls: Record<string, FormControl> = {};
    for (const f of this.fields()) {
      controls[f.key] = new FormControl(
        "",
        f.required ? Validators.required : null,
      );
    }
    return new FormGroup(controls);
  });
}
```

For bigger needs, libraries like Formly handle layouts, conditional fields and custom field types.

## 398: How do you reuse validation logic in signal forms?

Write a `schema()` once and apply it with `apply()` for nested objects or `applyEach()` for arrays.

```ts
import {
  schema,
  apply,
  applyEach,
  required,
  pattern,
  form,
} from "@angular/forms/signals";

interface Address {
  street: string;
  city: string;
  zip: string;
}
interface Order {
  billing: Address;
  shipping: Address;
  items: { sku: string; qty: number }[];
}

const addressSchema = schema<Address>((a) => {
  required(a.street);
  required(a.city);
  pattern(a.zip, /^\d{4,5}$/);
});

export class OrderForm {
  model = signal<Order>({
    billing: emptyAddress(),
    shipping: emptyAddress(),
    items: [],
  });

  f = form(this.model, (o) => {
    apply(o.billing, addressSchema);
    apply(o.shipping, addressSchema);
    applyEach(o.items, (item) => {
      required(item.sku);
    });
  });
}
```

This keeps rules close to the data shape and avoids repeating them for each address. Signal forms are experimental, so names may change in future versions.

## 399: How does async validation work in signal forms?

Signal forms have async validation functions that run after the sync rules pass, for example `validateHttp()` for HTTP-based checks. While a check runs, the field's `pending()` signal is `true`.

```ts
f = form(this.model, (p) => {
  required(p.username);
  validateHttp(p.username, {
    request: ({ value }) => `/api/username-available?name=${value()}`,
    onSuccess: (res: { available: boolean }) =>
      res.available ? null : { kind: "taken", message: "Username is taken" },
    onError: () => ({
      kind: "checkFailed",
      message: "Could not check username",
    }),
  });
});
```

```html
@if (f.username().pending()) { <small>Checking...</small> }
```

Because it's built on resources, a new value cancels the previous request. This part of the API is still experimental, so check the exact option names for your Angular version.

## 400: How do you create a custom control for signal forms?

A custom control implements `FormValueControl<T>`, which mainly means having a `value` model. The `[formField]` directive then binds the field to it. You don't need `ControlValueAccessor` or providers.

```ts
@Component({
  selector: "app-quantity",
  template: `
    <button type="button" (click)="change(-1)" [disabled]="disabled()">
      -
    </button>
    <span>{{ value() }}</span>
    <button type="button" (click)="change(1)" [disabled]="disabled()">+</button>
  `,
})
export class Quantity implements FormValueControl<number> {
  value = model(0);
  disabled = input(false);
  touched = model(false);

  change(delta: number) {
    this.value.update((v) => Math.max(0, v + delta));
    this.touched.set(true);
  }
}
```

```html
<app-quantity [formField]="orderForm.qty" />
```

The form passes state like `disabled`, `required`, `errors` to inputs with matching names if the control declares them. There is also `FormCheckboxControl` for boolean controls with a `checked` model.

## 401: How do you add conditional logic in signal forms?

Rules can depend on other field values through functions.

```ts
f = form(this.model, (p) => {
  // disable company name unless the account type is business
  disabled(
    p.companyName,
    ({ valueOf }) => valueOf(p.accountType) !== "business",
  );

  // hide VAT field for private accounts
  hidden(p.vatNumber, ({ valueOf }) => valueOf(p.accountType) === "private");

  // apply a whole set of rules only when a condition is true
  applyWhen(
    p,
    ({ value }) => value().accountType === "business",
    (b) => {
      required(b.companyName);
      required(b.vatNumber);
    },
  );

  readonly(p.email, () => this.isVerified());
});
```

Since everything is signal-based, the field states update automatically when the related values change. Hidden fields are skipped for validation, but you still decide in the template whether to render them.

## 402: How do you use reactive forms together with signals?

Reactive forms are Observable-based, but you can bridge them:

```ts
export class Filters {
  form = inject(NonNullableFormBuilder).group({
    query: [""],
    category: ["all"],
  });

  // the form value as a signal
  value = toSignal(this.form.valueChanges, {
    initialValue: this.form.getRawValue(),
  });

  // validity as a signal
  valid = toSignal(this.form.statusChanges.pipe(map((s) => s === "VALID")), {
    initialValue: this.form.valid,
  });

  // derived data
  results = httpResource<Item[]>(() => ({
    url: "/api/items",
    params: {
      q: this.value().query ?? "",
      category: this.value().category ?? "all",
    },
  }));
}
```

Use `form.events` if you also need touched/pristine changes. For the opposite direction (signal to form), use an `effect()` that calls `patchValue(..., { emitEvent: false })`.

## 403: How do you type a FormArray of FormGroups?

Describe the control types with an interface and let TypeScript check the rest.

```ts
interface LineItemForm {
  product: FormControl<string>;
  qty: FormControl<number>;
  price: FormControl<number>;
}

type InvoiceForm = FormGroup<{
  customer: FormControl<string>;
  lines: FormArray<FormGroup<LineItemForm>>;
}>;

export class InvoiceEditor {
  private fb = inject(NonNullableFormBuilder);

  form: InvoiceForm = this.fb.group({
    customer: [""],
    lines: this.fb.array<FormGroup<LineItemForm>>([]),
  });

  addLine(item?: Partial<{ product: string; qty: number; price: number }>) {
    this.form.controls.lines.push(
      this.fb.group({
        product: [item?.product ?? "", Validators.required],
        qty: [item?.qty ?? 1, Validators.min(1)],
        price: [item?.price ?? 0],
      }),
    );
  }

  total() {
    return this.form.controls.lines.controls.reduce(
      (sum, g) => sum + g.controls.qty.value * g.controls.price.value,
      0,
    );
  }
}
```

## 404: How do you avoid race conditions with async validators?

Problems to watch for:

- Old responses arriving after new ones and setting the wrong error
- Too many requests while typing
- The validator running when the value hasn't changed

Angular's async validators already cancel the previous Observable when the value changes (because the Observable is unsubscribed), so returning an Observable from `HttpClient` is safe. Returning a Promise is **not** cancellable, so an old result could still arrive. Prefer Observables.

Add a debounce inside the validator and use `updateOn: 'blur'` for expensive checks:

```ts
return (control) =>
  timer(400).pipe(
    switchMap(() => api.check(control.value)),
    map((ok) => (ok ? null : { taken: true })),
    first(),
  );
```

`first()` makes sure the Observable completes, which the form needs to leave the `PENDING` state.

## 405: How do you keep form data when the user navigates away and comes back?

Options:

- **Store form state in a service** (a signal), and patch the form on init. Save on `valueChanges` (debounced).
- **Save drafts to `sessionStorage` / `localStorage`** for longer persistence.
- **Use a `canDeactivate` guard** to warn instead of keeping data.
- **A custom `RouteReuseStrategy`** to keep the whole component alive (heavier).

```ts
@Injectable({ providedIn: "root" })
export class DraftStore {
  draft = signal<Partial<Profile> | null>(null);
}

export class EditProfile {
  private drafts = inject(DraftStore);
  form = inject(NonNullableFormBuilder).group({ name: [""], bio: [""] });

  constructor() {
    const draft = this.drafts.draft();
    if (draft) this.form.patchValue(draft);

    this.form.valueChanges
      .pipe(debounceTime(500), takeUntilDestroyed())
      .subscribe((v) => this.drafts.draft.set(v));
  }
}
```

With signal forms this is even simpler, since the model is already a signal you can keep in a service.

## 406: What are host directives?

Host directives let a component or directive apply other directives to its own host element, as part of its definition. It's composition instead of inheritance.

```ts
@Directive({
  selector: "[appFocusRing]",
  host: { "[class.focus-ring]": "true" },
})
export class FocusRing {}

@Directive({
  selector: "[appTooltip]",
  host: { "(mouseenter)": "show()", "(mouseleave)": "hide()" },
})
export class Tooltip {
  text = input("");
  show() {}
  hide() {}
}

@Component({
  selector: "app-icon-button",
  hostDirectives: [
    FocusRing,
    { directive: Tooltip, inputs: ["text: tooltip"] },
  ],
  template: `<ng-content />`,
})
export class IconButton {}
```

```html
<app-icon-button tooltip="Delete">🗑</app-icon-button>
```

The host directives' inputs and outputs are not exposed unless you list them, and you can rename them as above.

## 407: What should you know about host directive limitations?

- Host directives must be standalone.
- They are applied at compile time; you can't add them conditionally.
- Their inputs and outputs are private unless listed in `inputs` / `outputs`.
- They run **before** the host component/directive: constructors, lifecycle hooks and host bindings of host directives come first.
- The host can inject its host directives (and vice versa) because they share the same element injector.
- If the same directive is applied twice (once as a host directive and once in the template), Angular throws an error.

```ts
@Component({
  selector: "app-menu-item",
  hostDirectives: [CdkMenuItem],
  template: `<ng-content />`,
})
export class MenuItem {
  private cdkItem = inject(CdkMenuItem); // works: same element
}
```

## 408: How do you type the context of an ng-template in a custom directive?

Add a static `ngTemplateContextGuard` method. The template type checker then knows the types of `let-` variables.

```ts
interface LetContext<T> {
  $implicit: T;
  appLet: T;
}

@Directive({ selector: "[appLet]" })
export class LetDirective<T> {
  appLet = input.required<T>();
  private vcr = inject(ViewContainerRef);
  private tpl = inject<TemplateRef<LetContext<T>>>(TemplateRef);
  private ref?: EmbeddedViewRef<LetContext<T>>;

  constructor() {
    effect(() => {
      const value = this.appLet();
      if (!this.ref) {
        this.ref = this.vcr.createEmbeddedView(this.tpl, {
          $implicit: value,
          appLet: value,
        });
      } else {
        this.ref.context.$implicit = value;
        this.ref.context.appLet = value;
        this.ref.markForCheck();
      }
    });
  }

  static ngTemplateContextGuard<T>(
    dir: LetDirective<T>,
    ctx: unknown,
  ): ctx is LetContext<T> {
    return true;
  }
}
```

```html
<div *appLet="user() as u">{{ u.name }}</div>
<!-- u is typed as User -->
```

You can also add a static `ngTemplateGuard_<input>` to narrow types like `NgIf` does.

## 409: How do generic components work?

A component class can have type parameters, and Angular infers them from inputs in the template, with `strictTemplates`.

```ts
@Component({
  selector: "app-select",
  template: `
    <select (change)="onChange($event)">
      @for (opt of options(); track $index) {
        <option [value]="$index" [selected]="opt === selected()">
          {{ label()(opt) }}
        </option>
      }
    </select>
  `,
})
export class Select<T> {
  options = input.required<T[]>();
  label = input<(item: T) => string>((item) => String(item));
  selected = model<T | null>(null);

  onChange(e: Event) {
    const i = Number((e.target as HTMLSelectElement).value);
    this.selected.set(this.options()[i]);
  }
}
```

```html
<!-- T is inferred as Country, so label gets (c: Country) => string -->
<app-select
  [options]="countries"
  [label]="countryName"
  [(selected)]="country"
/>
```

If you bind a `label` function for a different type, the build fails, which catches bugs early.

## 410: How do content queries behave with nested components?

- `contentChildren(X)` without options only matches **direct** projected children of the host, not elements nested inside other elements in the projected content. Use `{ descendants: true }` to include those.
- Content queries never look into the templates of other components. If `<app-tab>` is inside the template of `<app-tab-group-wrapper>`, a query in an outer component won't find it unless it is projected content.
- Content inside `<ng-template>` is only found once the template is rendered.

```ts
export class Menu {
  items = contentChildren(MenuItem, { descendants: true });
}
```

```html
<app-menu>
  <app-menu-item>Home</app-menu-item>
  <div class="group">
    <app-menu-item>Settings</app-menu-item>
    <!-- found only with descendants: true -->
  </div>
</app-menu>
```

Signal queries update when the projected content changes (for example an `@if` inside the content).

## 411: What is the difference between embedded views and host views?

- **Embedded view**: created from an `<ng-template>` (`TemplateRef.createEmbeddedView` or `ViewContainerRef.createEmbeddedView`). It uses the context of the template where it was declared, plus any context object you pass. `@if` and `@for` create embedded views.
- **Host view**: created when a component is instantiated dynamically (`ViewContainerRef.createComponent` or `createComponent()`). It contains the component's host element and its view.

Both are `ViewRef`s and can be inserted into a `ViewContainerRef`, moved, detached and destroyed.

```ts
const embedded = this.vcr.createEmbeddedView(this.rowTpl, { $implicit: row });
const host = this.vcr.createComponent(RowEditor);

this.vcr.move(embedded, 0);
this.vcr.detach(this.vcr.indexOf(host.hostView));
```

A key point: an embedded view keeps the change detection and injector of the place where its template was **declared**, not where it's inserted.

## 412: How do CDK Portals and Overlays work?

A **Portal** is a piece of UI (component or template) that can be rendered somewhere else, in a **PortalOutlet**. An **Overlay** is a floating container attached to the body, with positioning and scroll strategies. Menus, tooltips and dialogs use them.

```ts
export class Dropdown {
  private overlay = inject(Overlay);
  private vcr = inject(ViewContainerRef);
  private ref?: OverlayRef;
  trigger = viewChild.required<ElementRef>("trigger");
  panel = viewChild.required<TemplateRef<unknown>>("panel");

  open() {
    this.ref = this.overlay.create({
      positionStrategy: this.overlay
        .position()
        .flexibleConnectedTo(this.trigger())
        .withPositions([
          {
            originX: "start",
            originY: "bottom",
            overlayX: "start",
            overlayY: "top",
          },
        ]),
      scrollStrategy: this.overlay.scrollStrategies.reposition(),
      hasBackdrop: true,
    });
    this.ref.attach(new TemplatePortal(this.panel(), this.vcr));
    this.ref.backdropClick().subscribe(() => this.ref?.dispose());
  }
}
```

Rendering in an overlay solves `overflow: hidden` and `z-index` problems, because the content is outside the component's DOM tree. The CDK also has a ready-made `Dialog` service built on this.

## 413: How do you build a service that opens components (like a dialog) outside the current template?

Create the component with `createComponent()`, attach its host view to `ApplicationRef` so it gets change detection, and add its element to the body.

```ts
@Injectable({ providedIn: "root" })
export class DialogService {
  private appRef = inject(ApplicationRef);
  private injector = inject(EnvironmentInjector);
  private document = inject(DOCUMENT);

  open<T>(component: Type<T>, inputs: Record<string, unknown> = {}) {
    const ref = createComponent(component, {
      environmentInjector: this.injector,
    });
    for (const [key, value] of Object.entries(inputs)) {
      ref.setInput(key, value);
    }

    this.appRef.attachView(ref.hostView);
    this.document.body.appendChild(ref.location.nativeElement);

    return {
      ref,
      close: () => {
        this.appRef.detachView(ref.hostView);
        ref.destroy();
      },
    };
  }
}
```

Remember to destroy the component when it closes, or it will leak. For production use, the CDK `Dialog` or Material `MatDialog` already handle focus trapping, ESC key, backdrops and accessibility.

## 414: How do you build compound components that talk to each other?

Child components inject the parent through DI. This creates a clear API like `<app-tabs>` + `<app-tab>`.

```ts
@Component({
  selector: "app-accordion",
  template: `<ng-content />`,
})
export class Accordion {
  multi = input(false);
  openIds = signal<Set<string>>(new Set());

  toggle(id: string) {
    this.openIds.update((set) => {
      const next = new Set(this.multi() ? set : []);
      set.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  }
}

@Component({
  selector: "app-accordion-panel",
  template: `
    <button (click)="accordion.toggle(id())">{{ title() }}</button>
    @if (isOpen()) {
      <ng-content />
    }
  `,
})
export class AccordionPanel {
  accordion = inject(Accordion);
  id = input.required<string>();
  title = input.required<string>();
  isOpen = computed(() => this.accordion.openIds().has(this.id()));
}
```

To decouple them, provide an `InjectionToken` or abstract class from the parent instead of the concrete class: `providers: [{ provide: ACCORDION, useExisting: Accordion }]`.

## 415: What are the pitfalls of component inheritance?

- Decorator metadata (`selector`, `template`, `providers`) is **not** inherited. Only class members, lifecycle hooks, inputs/outputs and host bindings declared on the base class are.
- A base class with Angular features must have `@Directive()` (with no selector) so the compiler processes it.
- Deep hierarchies make it hard to know where behavior comes from.
- With constructor injection, subclasses must repeat dependencies in `super(...)`. `inject()` avoids this.

```ts
@Directive()
export abstract class BaseList<T> {
  protected http = inject(HttpClient);
  items = signal<T[]>([]);
  abstract url: string;

  load() {
    this.http.get<T[]>(this.url).subscribe((i) => this.items.set(i));
  }
}

@Component({ selector: "app-users", template: `...` })
export class Users extends BaseList<User> {
  url = "/api/users";
}
```

Prefer composition: services, host directives, and small helper functions that use `inject()`.

## 416: What replaced ngAcceptInputType?

Before input transforms existed, a component that accepted `''` as `true` (like `<app-x disabled>`) had to declare a static `ngAcceptInputType_disabled` to tell the type checker that strings were allowed, plus a setter to convert the value.

```ts
// old
export class OldButton {
  static ngAcceptInputType_disabled: boolean | "";
  private _disabled = false;
  @Input() set disabled(v: boolean) {
    this._disabled = coerceBooleanProperty(v);
  }
  get disabled() {
    return this._disabled;
  }
}

// now
export class Button {
  disabled = input(false, { transform: booleanAttribute });
}
```

With `transform`, the accepted type is taken from the transform function's parameter type, so the template type checker knows `<app-button disabled>` is fine. `ngAcceptInputType_` is no longer needed.

## 417: How do Angular Elements work with Shadow DOM and slots?

If the component uses `ViewEncapsulation.ShadowDom`, the custom element gets a real shadow root. Styles are isolated, and content projection maps to native `<slot>`s.

```ts
@Component({
  selector: "app-fancy-card",
  encapsulation: ViewEncapsulation.ShadowDom,
  template: `
    <header part="header"><slot name="title"></slot></header>
    <slot></slot>
  `,
  styles: `
    :host {
      display: block;
      border: 1px solid #ccc;
    }
  `,
})
export class FancyCard {}
```

```html
<fancy-card>
  <h2 slot="title">Hello</h2>
  <p>Body</p>
</fancy-card>

<style>
  fancy-card::part(header) {
    background: gold;
  }
</style>
```

Outside styles can't reach inside except through CSS variables and `::part()`. With the default emulated encapsulation, `<ng-content>` is used instead of slots, and content projection happens only once when the element is created.

## 418: When do you use @defer vs lazy routes vs dynamic import()?

- **Lazy routes** (`loadComponent`, `loadChildren`): split code by page. Use for every feature route.
- **`@defer`**: split code inside a page, declared in the template. Use for heavy parts (charts, editors, comments, below-the-fold content). Handles placeholder, loading and error states, and works with SSR and incremental hydration.
- **Dynamic `import()` + `createComponent`/`NgComponentOutlet`**: when the component to load is decided at runtime (plugins, CMS-driven widgets).

```ts
async openEditor() {
  const { RichEditor } = await import('./rich-editor');
  this.vcr.createComponent(RichEditor);
}
```

`@defer` is usually the simplest option when you know the component at build time.

## 419: How do you build a recursive component, like a tree?

A component can use itself in its own template. Since it's standalone, it can import itself through `forwardRef` or simply reference its own class.

```ts
interface TreeNode {
  id: string;
  label: string;
  children?: TreeNode[];
}

@Component({
  selector: "app-tree-node",
  imports: [forwardRef(() => TreeNodeView)],
  template: `
    <div (click)="expanded.set(!expanded())">{{ node().label }}</div>
    @if (expanded() && node().children?.length) {
      <ul>
        @for (child of node().children; track child.id) {
          <li><app-tree-node [node]="child" /></li>
        }
      </ul>
    }
  `,
})
export class TreeNodeView {
  node = input.required<TreeNode>();
  expanded = signal(false);
}
```

For large trees, render children only when expanded (as above), or use the CDK tree with virtual scrolling.

## 420: Why doesn't conditional ng-content work as expected?

Content projection happens once, when the parent creates the child. The projected nodes are always created, even if the child puts `<ng-content>` inside a false `@if`. Also, you can't project the same content twice.

```html
<!-- child template -->
@if (open()) {
<ng-content />
<!-- content is still created and its components initialized -->
}
```

If you need content to be created only when shown (or shown several times), accept a template instead:

```ts
@Component({
  selector: "app-expander",
  imports: [NgTemplateOutlet],
  template: `
    <button (click)="open.set(!open())">Toggle</button>
    @if (open()) {
      <ng-container [ngTemplateOutlet]="body()" />
    }
  `,
})
export class Expander {
  open = signal(false);
  body = contentChild.required(TemplateRef);
}
```

```html
<app-expander>
  <ng-template><app-heavy-report /></ng-template>
</app-expander>
```

Now `HeavyReport` is created only when the panel opens.

## 421: What are the differences between signal queries and decorator queries?

|                            | Decorator (`@ViewChild`)                                         | Signal (`viewChild()`)                                |
| -------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| Result                     | plain property                                                   | signal                                                |
| Timing                     | set before `ngAfterViewInit` (or `ngOnInit` with `static: true`) | always up to date, can be read in `computed`/`effect` |
| `static` option            | yes                                                              | no                                                    |
| Changes notification       | `QueryList.changes` Observable                                   | signal updates                                        |
| Required queries           | no                                                               | `viewChild.required()` gives a non-undefined type     |
| Works with OnPush/zoneless | needs manual care                                                | yes                                                   |

```ts
// decorator
@ViewChildren(Item) items!: QueryList<Item>;
ngAfterViewInit() {
  this.items.changes.subscribe(() => this.update());
}

// signal
items = viewChildren(Item);
count = computed(() => this.items().length);
```

Reading a required signal query before the view is created throws an error (`NG0951`).

## 422: What is partial compilation and the Angular Package Format?

When you build a library with `ng build my-lib`, it is compiled in **partial** mode. The output contains Angular metadata in a stable, version-independent form (`ɵɵngDeclareComponent` calls), not final Ivy instructions. When an app uses the library, the Angular linker finishes the compilation for the app's Angular version.

This means a library built with Angular N works in apps using later Angular versions (within the supported range), without being recompiled.

The **Angular Package Format (APF)** is the layout of published packages:

- ES2022 modules (`fesm2022/*.mjs`), one flat file per entry point
- `.d.ts` typings
- `package.json` with `exports` for each entry point
- Secondary entry points as sub-paths

`ng-packagr` (used by `ng build` for libraries) produces this format.

## 423: How do you write a custom schematic?

Schematics are code generators and migration scripts that run on a virtual file tree. Angular libraries use them for `ng add`, `ng generate` and `ng update`.

```bash
npm install -g @angular-devkit/schematics-cli
schematics blank --name=my-schematics
```

```ts
import {
  Rule,
  Tree,
  SchematicContext,
  apply,
  url,
  template,
  move,
  mergeWith,
} from "@angular-devkit/schematics";
import { strings } from "@angular-devkit/core";

export function feature(options: { name: string; path: string }): Rule {
  return (tree: Tree, context: SchematicContext) => {
    context.logger.info(`Creating feature ${options.name}`);
    const source = apply(url("./files"), [
      template({ ...strings, ...options }),
      move(options.path),
    ]);
    return mergeWith(source);
  };
}
```

Files in `./files` are templates like `__name@dasherize__.ts.template`. Register schematics in `collection.json`, and `ng update` migrations in `migration.json`. Changes are only written to disk if the whole schematic succeeds.

## 424: What is a custom builder?

A builder is what runs behind `ng build`, `ng serve`, `ng test` and other targets in `angular.json`. You can write your own to plug custom tasks into the CLI.

```ts
import {
  createBuilder,
  BuilderContext,
  BuilderOutput,
} from "@angular-devkit/architect";
import { execSync } from "node:child_process";

interface Options {
  command: string;
}

export default createBuilder(
  async (options: Options, context: BuilderContext): Promise<BuilderOutput> => {
    context.logger.info(`Running ${options.command}`);
    try {
      execSync(options.command, { stdio: "inherit" });
      return { success: true };
    } catch {
      return { success: false };
    }
  },
);
```

```json
"architect": {
  "generate-api": {
    "builder": "./builders:run-command",
    "options": { "command": "openapi-generator-cli generate -i api.yaml -g typescript-angular -o src/api" }
  }
}
```

```bash
ng run my-app:generate-api
```

Often an npm script is enough. Builders are useful when you want to reuse CLI config, compose other targets (`context.scheduleTarget`), or publish the tool for other projects.

## 425: How does hot module replacement work in Angular?

With the esbuild/Vite-based dev server, `ng serve`:

- Replaces **styles** without a reload.
- Replaces **component templates** (and styles) without a reload since Angular 19.1. The component is re-rendered with the new template, and the app state (signals, services) is kept.

Changes to TypeScript code still trigger a full page reload. HMR is on by default; you can disable it with `ng serve --no-hmr`. This makes UI work much faster because you don't lose state like opened dialogs or filled forms after each template change.

## 426: What are extended diagnostics?

Extended diagnostics are extra compiler checks for code that is valid but probably wrong. Examples:

- `interpolatedSignalNotInvoked`: `{{ count }}` instead of `{{ count() }}`
- `invalidBananaInBox`: `([value])` instead of `[(value)]`
- `nullishCoalescingNotNullable`: `??` on a value that can't be null
- `optionalChainNotNullable`: `?.` on a non-null value
- `missingControlFlowDirective`: using `*ngIf` without importing `NgIf`
- `textAttributeNotBinding`: `class.active="cond"` without brackets
- `uninvokedFunctionInEventBinding`: `(click)="save"` instead of `(click)="save()"`
- `unusedStandaloneImports`: something in `imports` that the template doesn't use

```json
"angularCompilerOptions": {
  "extendedDiagnostics": {
    "defaultCategory": "error",
    "checks": { "nullishCoalescingNotNullable": "suppress" }
  }
}
```

## 427: How do you load translations at runtime with $localize?

Angular's i18n is normally build-time, but `$localize` can also use translations loaded at runtime, before the app starts. You have one build and pick the language at startup.

```ts
// main.ts
import { loadTranslations } from "@angular/localize";

async function start() {
  const lang = localStorage.getItem("lang") ?? "en";
  if (lang !== "en") {
    const res = await fetch(`/i18n/${lang}.json`);
    const { translations } = await res.json();
    loadTranslations(translations);
  }
  const { bootstrapApplication } = await import("@angular/platform-browser");
  const { App } = await import("./app/app");
  const { appConfig } = await import("./app/app.config");
  await bootstrapApplication(App, appConfig);
}
start();
```

Translations must be loaded **before** any code using `$localize` runs, which is why the app is imported dynamically. Changing language still needs a reload. You also need to set `LOCALE_ID` and register locale data for pipes like `date` and `currency`.

## 428: What are ICU expressions?

ICU expressions handle plurals and selections in translated text, because different languages have different plural rules.

```html
<!-- plural -->
<span i18n>
  {itemCount, plural, =0 {Your cart is empty} =1 {You have one item} other {You
  have {{ itemCount }} items} }
</span>

<!-- select -->
<span i18n>
  {gender, select, male {He} female {She} other {They}} liked your post
</span>

<!-- nested -->
<span i18n>
  {count, plural, =1 {{{ name }} commented} other {{{ name }} and {{ count - 1
  }} others commented}}
</span>
```

Translators get the whole ICU message and can add plural categories their language needs (like `few` or `many`).

## 429: What is the Angular CLI MCP server?

The Angular CLI includes a Model Context Protocol (MCP) server, so AI coding assistants can get Angular-specific context and tools instead of guessing from old training data.

```bash
ng mcp
```

This prints the configuration to add to your editor or AI tool. The server gives tools like searching the official docs, getting current best practices, listing projects in the workspace and running modernization migrations. It helps assistants generate code that matches current Angular APIs (signals, control flow, standalone).

## 430: How do you inject build-time constants?

The application builder has a `define` option that replaces global identifiers at build time.

```json
"configurations": {
  "production": {
    "define": {
      "BUILD_VERSION": "'1.4.2'",
      "ENABLE_DEBUG_PANEL": "false"
    }
  }
}
```

```ts
declare const BUILD_VERSION: string;
declare const ENABLE_DEBUG_PANEL: boolean;

console.log("version", BUILD_VERSION);

if (ENABLE_DEBUG_PANEL) {
  // removed entirely from the production bundle
}
```

The value must be a string containing a JavaScript expression, so strings need inner quotes. You can also set them from the command line: `ng build --define BUILD_VERSION="'1.4.3'"`.

## 431: What are the loader and externalDependencies build options?

**`loader`** tells esbuild how to import files with certain extensions:

```json
"loader": { ".svg": "text", ".txt": "text", ".png": "file" }
```

```ts
import logoSvg from "./logo.svg"; // string content of the SVG
```

You can also set it per import: `import data from './file.bin' with { loader: 'binary' };`

**`externalDependencies`** keeps listed packages out of the bundle, leaving the `import` as is. It's used when something else provides those modules at runtime (for example an import map in a micro frontend setup).

```json
"externalDependencies": ["@my-org/shared-runtime"]
```

## 432: What output modes does the application builder have?

The `outputMode` option controls what the build produces when SSR is configured:

- `"static"`: no server. Pages with `RenderMode.Prerender` are generated as HTML, and others fall back to client rendering. Deploy to any static host.
- `"server"`: produces a server bundle for `RenderMode.Server` routes, plus prerendered files. Needs a Node (or edge) server.

```json
"options": {
  "outputMode": "server",
  "server": "src/main.server.ts",
  "ssr": { "entry": "src/server.ts" }
}
```

Without SSR config, the build is a plain client-side app.

## 433: How do you set the locale for pipes like date and currency?

Angular includes `en-US` locale data by default. For other locales:

```ts
import { registerLocaleData } from "@angular/common";
import localeDe from "@angular/common/locales/de";

registerLocaleData(localeDe);

export const appConfig: ApplicationConfig = {
  providers: [
    { provide: LOCALE_ID, useValue: "de-DE" },
    { provide: DEFAULT_CURRENCY_CODE, useValue: "EUR" },
  ],
};
```

```html
{{ 1234.5 | currency }}
<!-- 1.234,50 € -->
{{ today | date }}
<!-- 23.10.2026 -->
```

When you build with `localize` in `angular.json`, the CLI sets `LOCALE_ID` and includes the locale data for each build automatically.

## 434: How do you test code that uses effects?

Effects are scheduled, not run immediately. In tests, use `TestBed.tick()` to run pending effects and change detection, or `await fixture.whenStable()` in component tests.

```ts
@Injectable({ providedIn: "root" })
export class ThemeStore {
  theme = signal<"light" | "dark">("light");
  constructor() {
    effect(() => localStorage.setItem("theme", this.theme()));
  }
}

it("saves the theme", () => {
  const store = TestBed.inject(ThemeStore);
  store.theme.set("dark");
  TestBed.tick();
  expect(localStorage.getItem("theme")).toBe("dark");
});
```

`TestBed.tick()` replaced the earlier `TestBed.flushEffects()` in Angular 20. Ideally, test the result (what was saved, what is shown) rather than the effect itself.

## 435: How do you test httpResource?

`httpResource` uses `HttpClient`, so `HttpTestingController` works. Because resources are signal-based, you need to let Angular run the request with `TestBed.tick()` and then flush it.

```ts
@Injectable({ providedIn: "root" })
export class ProfileStore {
  userId = signal(1);
  user = httpResource<User>(() => `/api/users/${this.userId()}`);
}

it("loads the user", async () => {
  TestBed.configureTestingModule({
    providers: [provideHttpClient(), provideHttpClientTesting()],
  });
  const store = TestBed.inject(ProfileStore);
  const http = TestBed.inject(HttpTestingController);

  TestBed.tick(); // triggers the request
  http.expectOne("/api/users/1").flush({ id: 1, name: "Ann" });

  await TestBed.inject(ApplicationRef).whenStable();
  expect(store.user.value()?.name).toBe("Ann");
});
```

For `resource()` with `fetch`, mock `fetch` or put the loader in a service you can replace.

## 436: How do you test a functional guard?

Call it inside `TestBed.runInInjectionContext()`, since it uses `inject()`.

```ts
describe("authGuard", () => {
  const auth = { isLoggedIn: signal(false) };

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideRouter([]), { provide: AuthService, useValue: auth }],
    });
  });

  it("redirects to login when logged out", () => {
    const result = TestBed.runInInjectionContext(() =>
      authGuard(
        {} as ActivatedRouteSnapshot,
        { url: "/admin" } as RouterStateSnapshot,
      ),
    );
    expect(result).toBeInstanceOf(RedirectCommand);
  });

  it("allows when logged in", () => {
    auth.isLoggedIn.set(true);
    const result = TestBed.runInInjectionContext(() =>
      authGuard(
        {} as ActivatedRouteSnapshot,
        { url: "/admin" } as RouterStateSnapshot,
      ),
    );
    expect(result).toBe(true);
  });
});
```

For a full integration test, use `RouterTestingHarness` and navigate to the guarded URL.

## 437: How do you test an HTTP interceptor?

Register it with `withInterceptors()` and check the outgoing request with `HttpTestingController`.

```ts
describe("authInterceptor", () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        { provide: AuthService, useValue: { token: () => "abc" } },
        provideHttpClient(withInterceptors([authInterceptor])),
        provideHttpClientTesting(),
      ],
    });
  });

  it("adds the Authorization header", () => {
    TestBed.inject(HttpClient).get("/api/data").subscribe();

    const req = TestBed.inject(HttpTestingController).expectOne("/api/data");
    expect(req.request.headers.get("Authorization")).toBe("Bearer abc");
    req.flush({});
  });
});
```

To test error handling, flush with an error status (`req.flush(null, { status: 401, statusText: 'Unauthorized' })`) and check the result.

## 438: How do you write your own component harness?

Extend `ComponentHarness`, set the `hostSelector`, and use locators to find inner elements.

```ts
export class CounterHarness extends ComponentHarness {
  static hostSelector = "app-counter";

  private incrementButton = this.locatorFor("button.increment");
  private display = this.locatorFor(".count");

  async increment() {
    await (await this.incrementButton()).click();
  }

  async getCount(): Promise<number> {
    return Number(await (await this.display()).text());
  }

  static with(options: BaseHarnessFilters & { count?: number } = {}) {
    return new HarnessPredicate(CounterHarness, options).addOption(
      "count",
      options.count,
      async (h, count) => (await h.getCount()) === count,
    );
  }
}
```

```ts
const counter = await loader.getHarness(CounterHarness);
await counter.increment();
expect(await counter.getCount()).toBe(1);
```

Harness methods are async and automatically wait for the app to be stable after each action. The same harness works in unit tests and in e2e tests (with the right environment).

## 439: How do you test timers in a zoneless app?

`fakeAsync()` and `tick()` depend on Zone.js, so they don't work without it. Use your test runner's fake timers instead.

```ts
// Vitest
describe("AutoSave", () => {
  beforeEach(() => vi.useFakeTimers());
  afterEach(() => vi.useRealTimers());

  it("saves after 2 seconds", async () => {
    const api = { save: vi.fn() };
    TestBed.configureTestingModule({
      providers: [{ provide: DraftApi, useValue: api }],
    });
    const fixture = TestBed.createComponent(AutoSave);

    fixture.componentInstance.text.set("hello");
    await vi.advanceTimersByTimeAsync(2000);

    expect(api.save).toHaveBeenCalledWith("hello");
  });
});
```

Jasmine has `jasmine.clock()` for the same purpose. Be aware that Angular's own scheduler uses timers too, so advancing time also runs change detection.

## 440: How do you do end-to-end testing in Angular?

Angular doesn't ship an e2e tool anymore (Protractor was removed). Popular choices:

- **Playwright**: fast, multiple browsers, good tooling.
- **Cypress**: interactive runner, also supports component testing.

```bash
ng e2e  # asks which tool to add if none is set up
```

```ts
// Playwright
import { test, expect } from "@playwright/test";

test("user can log in", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill("ann@mail.com");
  await page.getByLabel("Password").fill("secret123");
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
});
```

Use role and label based selectors, which are more stable than CSS classes and also check accessibility.

## 441: How do you test @defer blocks?

By default, `@defer` blocks in tests render in "playthrough" mode: they behave like in the app. To control their state manually, use `DeferBlockBehavior.Manual`.

```ts
beforeEach(() => {
  TestBed.configureTestingModule({
    deferBlockBehavior: DeferBlockBehavior.Manual,
  });
});

it("shows the placeholder, then the content", async () => {
  const fixture = TestBed.createComponent(ArticlePage);
  await fixture.whenStable();

  const [commentsBlock] = await fixture.getDeferBlocks();

  await commentsBlock.render(DeferBlockState.Placeholder);
  expect(fixture.nativeElement.textContent).toContain("Comments will load");

  await commentsBlock.render(DeferBlockState.Complete);
  expect(fixture.nativeElement.querySelector("app-comments")).toBeTruthy();
});
```

You can render each state: `Placeholder`, `Loading`, `Complete` and `Error`.

## 442: How do you test a custom form control?

Test it the way it's used: inside a host component with a real form.

```ts
@Component({
  imports: [ReactiveFormsModule, StarRating],
  template: `<app-star-rating [formControl]="rating" />`,
})
class Host {
  rating = new FormControl(2);
}

describe("StarRating as a form control", () => {
  it("reads and writes the form value", async () => {
    const fixture = TestBed.createComponent(Host);
    await fixture.whenStable();
    const buttons = fixture.nativeElement.querySelectorAll("button");

    // form -> component
    expect(buttons[1].textContent).toContain("★");

    // component -> form
    buttons[4].click();
    expect(fixture.componentInstance.rating.value).toBe(5);
    expect(fixture.componentInstance.rating.touched).toBe(true);
  });

  it("respects disabled", async () => {
    const fixture = TestBed.createComponent(Host);
    fixture.componentInstance.rating.disable();
    await fixture.whenStable();
    expect(fixture.nativeElement.querySelector("button").disabled).toBe(true);
  });
});
```

## 443: Why can a test pass but the real OnPush or zoneless component not update?

Calling `fixture.detectChanges()` forces a check of the component, even if nothing told Angular that it changed. So a test can pass while the real app doesn't update, for example when a plain field is changed inside a subscription.

To avoid this:

- Use `await fixture.whenStable()` instead of `detectChanges()`, so updates only happen when Angular itself would schedule them.
- Run tests zoneless if the app is zoneless (`provideZonelessChangeDetection()` in the test providers, which is the default setup for new projects).
- Set inputs with `fixture.componentRef.setInput()`, not by assigning to the instance.

```ts
// bad: hides missing notifications
fixture.componentInstance.items = newItems;
fixture.detectChanges();

// good
fixture.componentRef.setInput("items", newItems);
await fixture.whenStable();
```

## 444: What common Angular runtime error codes should you know?

| Code     | Meaning                                                              |
| -------- | -------------------------------------------------------------------- |
| `NG0100` | Expression changed after it was checked                              |
| `NG0200` | Circular dependency in DI                                            |
| `NG0201` | No provider found for a token                                        |
| `NG0203` | `inject()` called outside an injection context                       |
| `NG0300` | Two components match the same element                                |
| `NG0303` | Can't bind to a property that isn't known (missing import or typo)   |
| `NG0500` | Hydration mismatch                                                   |
| `NG0904` | Unsafe value used in a resource URL context                          |
| `NG0950` | A required input was read before it had a value                      |
| `NG0951` | A required query had no result                                       |
| `NG0955` | `@for` track expression produced duplicate keys                      |
| `NG0956` | `@for` track expression recreated the whole collection (bad `track`) |

Every error links to a page at `angular.dev/errors/<code>` with causes and fixes. Compile-time errors use codes like `NG8001` (unknown element).

## 445: What do experimental, developer preview and stable mean for Angular APIs?

- **Experimental**: an early version to get feedback. It can change a lot or be removed, even in minor releases. Signal forms in Angular 21 are an example.
- **Developer preview**: the API is mostly complete and usable, but it can still change in minor releases without the normal deprecation period.
- **Stable**: follows semantic versioning. Breaking changes only in major versions, after a deprecation period (usually at least two major versions).
- **Deprecated**: still works, but will be removed in a future major version. The docs say what to use instead.

The API reference on angular.dev shows the status of each API. Using non-stable APIs in production is fine if you're ready to update your code when they change.

## 446: How does @for update the DOM when the list changes?

When the collection changes, Angular compares the old and new lists using the `track` keys:

1. Items with the same key at the same position are kept, and only their bindings update.
2. Items whose key is gone are removed (their views destroyed).
3. New keys get new views.
4. Items that moved are moved in the DOM, not recreated. Angular uses an algorithm that tries to minimize the number of moves.

Because `track` is required and is a simple expression (not a function you have to write like `trackBy`), the compiler can optimize it. If the track key is not unique, you get `NG0955`. If it changes for every item on every update (like tracking a new object from an API response), you get `NG0956` in dev mode, since the whole list is rebuilt.

## 447: Why should you avoid Angular's private APIs (the ɵ prefix)?

Symbols starting with `ɵ` (like `ɵɵdefineComponent` or `ɵgetLContext`) are internal. They are exported only because the compiler-generated code or other Angular packages need them.

They can change or disappear in any release, even a patch, with no deprecation. Code that depends on them will break during upgrades, and migrations won't fix it.

If you need something only a private API provides, check if there's a public alternative, open a feature request, or isolate the usage in one place so it's easy to update later.

## 448: How do you use non-Angular web components in an Angular template?

By default, Angular reports an error for unknown elements and properties. Add `CUSTOM_ELEMENTS_SCHEMA` to the component that uses them:

```ts
@Component({
  selector: "app-checkout",
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `
    <payment-widget
      [amount]="total()"
      (payment-complete)="onPaid($event)"
    ></payment-widget>
  `,
})
export class Checkout {
  total = signal(49.99);
  onPaid(e: Event) {
    console.log((e as CustomEvent).detail);
  }
}
```

Property bindings set DOM properties on the element and event bindings listen to its DOM events, so it works with most web components. The downside: the schema turns off checking for unknown elements in that template, so typos in other element names won't be caught. Keep the schema on small wrapper components.

## 449: How do you design a good API for a reusable component library?

Some guidelines:

- **Small, clear inputs** with good defaults. Use `input.required()` only for what's truly needed.
- **Boolean attributes** with `booleanAttribute` (`<app-button disabled>`).
- **`model()`** for values users may want to bind both ways.
- **Content projection** for flexible content instead of many string inputs (`<app-card><h2 card-title>...</h2></app-card>`).
- **Template inputs** (`TemplateRef`) for customizing repeated parts like list items.
- **CSS custom properties** for theming, not deep selectors or `::ng-deep`.
- **Accessibility built in**: roles, keyboard support, focus management (or build on Angular Aria / CDK).
- **Host directives** to share behavior between components.
- **OnPush** and signals everywhere, so the library works in zoneless apps.
- **Secondary entry points** so apps only bundle what they use.
- **Harnesses** shipped with the library so consumers can test easily.
- **Clear deprecation** before breaking changes, with schematics for migrations where possible.

## 450: What is HttpBackend and when would you use it?

`HttpBackend` is the last step in the `HttpClient` chain: it actually sends the request (with XHR or fetch). Interceptors sit in front of it. If you create an `HttpClient` directly from `HttpBackend`, requests made with it **skip all interceptors**.

```ts
@Injectable({ providedIn: "root" })
export class ConfigLoader {
  // this client ignores interceptors
  private http = new HttpClient(inject(HttpBackend));

  load() {
    return firstValueFrom(this.http.get<AppConfig>("/config.json"));
  }
}
```

Typical uses:

- Loading runtime config before interceptors that depend on that config can work
- Calling a token refresh endpoint from inside an auth interceptor without causing a circular dependency or an interceptor loop
- Calling third-party APIs that must not get your auth headers

Use it sparingly. Requests made this way also skip logging, error handling and other cross-cutting logic you put in interceptors.
