# Angular Testing Interview Questions and Answers

_Last updated: November 25, 2026_

450 Angular testing interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Angular v21 and later, where new projects use Vitest through the `@angular/build:unit-test` builder, standalone components, signals and zoneless change detection. Karma, Jasmine, Zone.js helpers like `fakeAsync` and NgModule based setups are covered too, and marked as legacy where that applies, since many real projects still use them.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: Why do we write tests for Angular applications?](#1-why-do-we-write-tests-for-angular-applications)
- [2: What kinds of tests are common in an Angular project?](#2-what-kinds-of-tests-are-common-in-an-angular-project)
- [3: What is the testing pyramid?](#3-what-is-the-testing-pyramid)
- [4: Which test runner does a new Angular CLI project use?](#4-which-test-runner-does-a-new-angular-cli-project-use)
- [5: How do you run unit tests in an Angular project?](#5-how-do-you-run-unit-tests-in-an-angular-project)
- [6: What is a spec file?](#6-what-is-a-spec-file)
- [7: What do describe, it and expect do?](#7-what-do-describe-it-and-expect-do)
- [8: What are beforeEach and afterEach used for?](#8-what-are-beforeeach-and-aftereach-used-for)
- [9: What is TestBed?](#9-what-is-testbed)
- [10: What does TestBed.configureTestingModule do?](#10-what-does-testbedconfiguretestingmodule-do)
- [11: How do you test a standalone component with TestBed?](#11-how-do-you-test-a-standalone-component-with-testbed)
- [12: What is a ComponentFixture?](#12-what-is-a-componentfixture)
- [13: What does fixture.detectChanges() do?](#13-what-does-fixturedetectchanges-do)
- [14: What does fixture.whenStable() do?](#14-what-does-fixturewhenstable-do)
- [15: What is the difference between nativeElement and debugElement?](#15-what-is-the-difference-between-nativeelement-and-debugelement)
- [16: How do you read text from a component's template in a test?](#16-how-do-you-read-text-from-a-components-template-in-a-test)
- [17: How do you query elements with By.css?](#17-how-do-you-query-elements-with-bycss)
- [18: How do you test a simple service?](#18-how-do-you-test-a-simple-service)
- [19: What does TestBed.inject do?](#19-what-does-testbedinject-do)
- [20: Why can't you always create a service with new in a test?](#20-why-cant-you-always-create-a-service-with-new-in-a-test)
- [21: How do you test a pipe?](#21-how-do-you-test-a-pipe)
- [22: What is a mock?](#22-what-is-a-mock)
- [23: What is the difference between a mock, a stub and a spy?](#23-what-is-the-difference-between-a-mock-a-stub-and-a-spy)
- [24: How do you provide a fake service to a component in a test?](#24-how-do-you-provide-a-fake-service-to-a-component-in-a-test)
- [25: How do you create a spy in Vitest?](#25-how-do-you-create-a-spy-in-vitest)
- [26: How do you create a spy in Jasmine?](#26-how-do-you-create-a-spy-in-jasmine)
- [27: What is the difference between toBe and toEqual?](#27-what-is-the-difference-between-tobe-and-toequal)
- [28: What are some common matchers?](#28-what-are-some-common-matchers)
- [29: How do you check that a function throws an error?](#29-how-do-you-check-that-a-function-throws-an-error)
- [30: How do you test a component's @Input or signal input?](#30-how-do-you-test-a-components-input-or-signal-input)
- [31: How do you test a component output?](#31-how-do-you-test-a-component-output)
- [32: How do you simulate a button click in a test?](#32-how-do-you-simulate-a-button-click-in-a-test)
- [33: What does triggerEventHandler do?](#33-what-does-triggereventhandler-do)
- [34: How do you test an input field in a template?](#34-how-do-you-test-an-input-field-in-a-template)
- [35: What does the first detectChanges call trigger?](#35-what-does-the-first-detectchanges-call-trigger)
- [36: What does fixture.autoDetectChanges() do?](#36-what-does-fixtureautodetectchanges-do)
- [37: What is code coverage?](#37-what-is-code-coverage)
- [38: What is the tsconfig.spec.json file for?](#38-what-is-the-tsconfigspecjson-file-for)
- [39: How do you run a single test or a single describe block?](#39-how-do-you-run-a-single-test-or-a-single-describe-block)
- [40: How do you run tests for only some files?](#40-how-do-you-run-tests-for-only-some-files)
- [41: What is the difference between a unit test and an integration test in Angular?](#41-what-is-the-difference-between-a-unit-test-and-an-integration-test-in-angular)
- [42: What should a good unit test look like?](#42-what-should-a-good-unit-test-look-like)
- [43: What is the Arrange, Act, Assert pattern?](#43-what-is-the-arrange-act-assert-pattern)
- [44: How do you test a component that has no dependencies?](#44-how-do-you-test-a-component-that-has-no-dependencies)
- [45: What test does the CLI generate for a new component?](#45-what-test-does-the-cli-generate-for-a-new-component)
- [46: Why should each test be independent?](#46-why-should-each-test-be-independent)
- [47: What is compileComponents and do you still need it?](#47-what-is-compilecomponents-and-do-you-still-need-it)
- [48: How do you test a component that uses a service through inject()?](#48-how-do-you-test-a-component-that-uses-a-service-through-inject)
- [49: What is the difference between useValue and useClass in test providers?](#49-what-is-the-difference-between-usevalue-and-useclass-in-test-providers)
- [50: How do you check that a CSS class is applied to an element?](#50-how-do-you-check-that-a-css-class-is-applied-to-an-element)
- [51: How do you test that an element is shown or hidden with @if?](#51-how-do-you-test-that-an-element-is-shown-or-hidden-with-if)
- [52: How do you test a list rendered with @for?](#52-how-do-you-test-a-list-rendered-with-for)
- [53: How do you test a signal in a service?](#53-how-do-you-test-a-signal-in-a-service)
- [54: How do you test a computed signal?](#54-how-do-you-test-a-computed-signal)
- [55: How do you test a component that uses signals for state?](#55-how-do-you-test-a-component-that-uses-signals-for-state)
- [56: What is jsdom and why is it used in Angular tests?](#56-what-is-jsdom-and-why-is-it-used-in-angular-tests)
- [57: What is Karma?](#57-what-is-karma)
- [58: What is Jasmine?](#58-what-is-jasmine)
- [59: What is Vitest?](#59-what-is-vitest)
- [60: Where is the test configuration stored in an Angular project?](#60-where-is-the-test-configuration-stored-in-an-angular-project)
- [61: What does ng generate do for tests?](#61-what-does-ng-generate-do-for-tests)
- [62: How do you test a component method directly?](#62-how-do-you-test-a-component-method-directly)
- [63: What is a smoke test?](#63-what-is-a-smoke-test)
- [64: Why should you avoid testing private methods directly?](#64-why-should-you-avoid-testing-private-methods-directly)
- [65: How do you test a component with an ngOnInit that loads data?](#65-how-do-you-test-a-component-with-an-ngoninit-that-loads-data)
- [66: What is of() used for in tests?](#66-what-is-of-used-for-in-tests)
- [67: How do you fake an observable that fails?](#67-how-do-you-fake-an-observable-that-fails)
- [68: How do you test an observable returned by a service?](#68-how-do-you-test-an-observable-returned-by-a-service)
- [69: How do you use firstValueFrom in tests?](#69-how-do-you-use-firstvaluefrom-in-tests)
- [70: How do you write an async test?](#70-how-do-you-write-an-async-test)
- [71: What does the done callback do in tests?](#71-what-does-the-done-callback-do-in-tests)
- [72: How do you test a component with a template reference to a child component?](#72-how-do-you-test-a-component-with-a-template-reference-to-a-child-component)
- [73: What is By.directive used for?](#73-what-is-bydirective-used-for)
- [74: How do you test a simple attribute directive?](#74-how-do-you-test-a-simple-attribute-directive)
- [75: What is a test host component?](#75-what-is-a-test-host-component)
- [76: How do you check an element's attribute in a test?](#76-how-do-you-check-an-elements-attribute-in-a-test)
- [77: How do you check if a button is disabled?](#77-how-do-you-check-if-a-button-is-disabled)
- [78: How do you test a reactive form's validation?](#78-how-do-you-test-a-reactive-forms-validation)
- [79: How do you test a custom validator function?](#79-how-do-you-test-a-custom-validator-function)
- [80: What is HttpClientTestingModule and what replaces it?](#80-what-is-httpclienttestingmodule-and-what-replaces-it)
- [81: What is HttpTestingController?](#81-what-is-httptestingcontroller)
- [82: What does req.flush() do?](#82-what-does-reqflush-do)
- [83: What does httpMock.verify() do?](#83-what-does-httpmockverify-do)
- [84: Why does the order of provideHttpClient and provideHttpClientTesting matter?](#84-why-does-the-order-of-providehttpclient-and-providehttpclienttesting-matter)
- [85: How do you test a service that makes a POST request?](#85-how-do-you-test-a-service-that-makes-a-post-request)
- [86: How do you test an HTTP error in a service?](#86-how-do-you-test-an-http-error-in-a-service)
- [87: What is E2E testing?](#87-what-is-e2e-testing)
- [88: Which E2E tools are used with Angular today?](#88-which-e2e-tools-are-used-with-angular-today)
- [89: What was Protractor and why was it dropped?](#89-what-was-protractor-and-why-was-it-dropped)
- [90: What is the difference between toHaveBeenCalled and toHaveBeenCalledWith?](#90-what-is-the-difference-between-tohavebeencalled-and-tohavebeencalledwith)
- [91: How do you make a spy return a value in Vitest?](#91-how-do-you-make-a-spy-return-a-value-in-vitest)
- [92: How do you make a spy return a value in Jasmine?](#92-how-do-you-make-a-spy-return-a-value-in-jasmine)
- [93: How do you test a component that uses the async pipe?](#93-how-do-you-test-a-component-that-uses-the-async-pipe)
- [94: How do you use a Subject to control data in a test?](#94-how-do-you-use-a-subject-to-control-data-in-a-test)
- [95: How do you test a loading state?](#95-how-do-you-test-a-loading-state)
- [96: What is the point of testing what the user sees instead of internal state?](#96-what-is-the-point-of-testing-what-the-user-sees-instead-of-internal-state)
- [97: How do you name tests well?](#97-how-do-you-name-tests-well)
- [98: How do you test a component that uses the Router?](#98-how-do-you-test-a-component-that-uses-the-router)
- [99: What is RouterTestingModule and what replaces it?](#99-what-is-routertestingmodule-and-what-replaces-it)
- [100: How do you test a component that reads route parameters?](#100-how-do-you-test-a-component-that-reads-route-parameters)
- [101: How do you fake ActivatedRoute in a simple unit test?](#101-how-do-you-fake-activatedroute-in-a-simple-unit-test)
- [102: How do you test that a component navigates somewhere?](#102-how-do-you-test-that-a-component-navigates-somewhere)
- [103: How do you test a routerLink?](#103-how-do-you-test-a-routerlink)
- [104: What is the difference between shallow and deep component tests?](#104-what-is-the-difference-between-shallow-and-deep-component-tests)
- [105: How do you replace a child component with a stub?](#105-how-do-you-replace-a-child-component-with-a-stub)
- [106: What is NO_ERRORS_SCHEMA?](#106-what-is-no_errors_schema)
- [107: What is a test double?](#107-what-is-a-test-double)
- [108: How do you test a component with localStorage?](#108-how-do-you-test-a-component-with-localstorage)
- [109: How do you reset spies between tests in Vitest?](#109-how-do-you-reset-spies-between-tests-in-vitest)
- [110: Do Jasmine spies need to be reset between tests?](#110-do-jasmine-spies-need-to-be-reset-between-tests)
- [111: How do you test a component's ngOnDestroy?](#111-how-do-you-test-a-components-ngondestroy)
- [112: Does TestBed destroy components after each test?](#112-does-testbed-destroy-components-after-each-test)
- [113: How do you test text that comes from an interpolation?](#113-how-do-you-test-text-that-comes-from-an-interpolation)
- [114: Why do tests sometimes see old values in the DOM?](#114-why-do-tests-sometimes-see-old-values-in-the-dom)
- [115: How do you test a template-driven form?](#115-how-do-you-test-a-template-driven-form)
- [116: How do you test a select dropdown?](#116-how-do-you-test-a-select-dropdown)
- [117: How do you test a checkbox?](#117-how-do-you-test-a-checkbox)
- [118: How do you submit a form in a test?](#118-how-do-you-submit-a-form-in-a-test)
- [119: What does ng test --watch do?](#119-what-does-ng-test---watch-do)
- [120: How do you run Angular tests in CI?](#120-how-do-you-run-angular-tests-in-ci)
- [121: What does a test report show?](#121-what-does-a-test-report-show)
- [122: Why is a test that never fails useless?](#122-why-is-a-test-that-never-fails-useless)
- [123: How do you test a pure function used by a component?](#123-how-do-you-test-a-pure-function-used-by-a-component)
- [124: What is the providedIn: 'root' setting's effect on tests?](#124-what-is-the-providedin-root-settings-effect-on-tests)
- [125: How do you test a component that shows a date with the DatePipe?](#125-how-do-you-test-a-component-that-shows-a-date-with-the-datepipe)
- [126: How do you test something that uses the current date?](#126-how-do-you-test-something-that-uses-the-current-date)
- [127: What is a flaky test?](#127-what-is-a-flaky-test)
- [128: How do you test a component with content projection?](#128-how-do-you-test-a-component-with-content-projection)
- [129: How do you test a component's host binding?](#129-how-do-you-test-a-components-host-binding)
- [130: How do you test a host listener?](#130-how-do-you-test-a-host-listener)
- [131: How do you test a component that uses @ViewChild or viewChild()?](#131-how-do-you-test-a-component-that-uses-viewchild-or-viewchild)
- [132: How do you test that a method focuses an input?](#132-how-do-you-test-that-a-method-focuses-an-input)
- [133: How do you add global setup code that runs before every spec file?](#133-how-do-you-add-global-setup-code-that-runs-before-every-spec-file)
- [134: What is test.ts in older Angular projects?](#134-what-is-testts-in-older-angular-projects)
- [135: How do you check how many times a spy was called?](#135-how-do-you-check-how-many-times-a-spy-was-called)
- [136: How do you check the arguments of a specific call?](#136-how-do-you-check-the-arguments-of-a-specific-call)
- [137: What is expect.any() or jasmine.any() for?](#137-what-is-expectany-or-jasmineany-for)
- [138: How do you test a component that shows an error message from an HTTP call?](#138-how-do-you-test-a-component-that-shows-an-error-message-from-an-http-call)
- [139: Why should tests not call real APIs?](#139-why-should-tests-not-call-real-apis)
- [140: What is test data and how should you manage it?](#140-what-is-test-data-and-how-should-you-manage-it)
- [141: What is the benefit of keeping spec files next to the code?](#141-what-is-the-benefit-of-keeping-spec-files-next-to-the-code)
- [142: How do you test a component that uses the i18n $localize function?](#142-how-do-you-test-a-component-that-uses-the-i18n-localize-function)
- [143: How do you test a component that emits through an output when a form is valid?](#143-how-do-you-test-a-component-that-emits-through-an-output-when-a-form-is-valid)
- [144: How do you check an inline style in a test?](#144-how-do-you-check-an-inline-style-in-a-test)
- [145: What is the role of the polyfills option in test configuration?](#145-what-is-the-role-of-the-polyfills-option-in-test-configuration)
- [146: How do you test a standalone component that imports other standalone components?](#146-how-do-you-test-a-standalone-component-that-imports-other-standalone-components)
- [147: How do you test a component that was declared in an NgModule?](#147-how-do-you-test-a-component-that-was-declared-in-an-ngmodule)
- [148: What is a matcher like toBeCloseTo for?](#148-what-is-a-matcher-like-tobecloseto-for)
- [149: What does "should create" test actually catch?](#149-what-does-should-create-test-actually-catch)
- [150: How do you get started writing tests for an Angular app that has none?](#150-how-do-you-get-started-writing-tests-for-an-angular-app-that-has-none)

### Moderate Questions (151-300)

- [151: What are the main options of the @angular/build:unit-test builder?](#151-what-are-the-main-options-of-the-angularbuildunit-test-builder)
- [152: How does the Angular CLI run Vitest under the hood?](#152-how-does-the-angular-cli-run-vitest-under-the-hood)
- [153: How do you use your own Vitest config file with the Angular builder?](#153-how-do-you-use-your-own-vitest-config-file-with-the-angular-builder)
- [154: How do you migrate an existing project from Karma to Vitest?](#154-how-do-you-migrate-an-existing-project-from-karma-to-vitest)
- [155: Can you keep using Karma with the new unit-test builder?](#155-can-you-keep-using-karma-with-the-new-unit-test-builder)
- [156: What is Vitest browser mode and when do you use it?](#156-what-is-vitest-browser-mode-and-when-do-you-use-it)
- [157: How do you set coverage thresholds?](#157-how-do-you-set-coverage-thresholds)
- [158: How do you exclude files from coverage?](#158-how-do-you-exclude-files-from-coverage)
- [159: Is 100% code coverage a good goal?](#159-is-100-code-coverage-a-good-goal)
- [160: How do you test a functional route guard?](#160-how-do-you-test-a-functional-route-guard)
- [161: What does TestBed.runInInjectionContext do?](#161-what-does-testbedrunininjectioncontext-do)
- [162: How do you test a guard through real routing?](#162-how-do-you-test-a-guard-through-real-routing)
- [163: How do you test a resolver?](#163-how-do-you-test-a-resolver)
- [164: How do you test a functional HTTP interceptor?](#164-how-do-you-test-a-functional-http-interceptor)
- [165: How do you test an interceptor that retries or handles errors?](#165-how-do-you-test-an-interceptor-that-retries-or-handles-errors)
- [166: How do you test a class based interceptor?](#166-how-do-you-test-a-class-based-interceptor)
- [167: How do you match requests in HttpTestingController beyond the URL?](#167-how-do-you-match-requests-in-httptestingcontroller-beyond-the-url)
- [168: How do you test query params in an HTTP request?](#168-how-do-you-test-query-params-in-an-http-request)
- [169: How do you test httpResource?](#169-how-do-you-test-httpresource)
- [170: What does TestBed.tick() do?](#170-what-does-testbedtick-do)
- [171: How do you test an effect?](#171-how-do-you-test-an-effect)
- [172: How do you test a linkedSignal?](#172-how-do-you-test-a-linkedsignal)
- [173: How do you test the resource() API?](#173-how-do-you-test-the-resource-api)
- [174: How do you test a component that uses toSignal?](#174-how-do-you-test-a-component-that-uses-tosignal)
- [175: What does setInput do that direct assignment does not?](#175-what-does-setinput-do-that-direct-assignment-does-not)
- [176: How do you test input transforms?](#176-how-do-you-test-input-transforms)
- [177: How do you test a required signal input?](#177-how-do-you-test-a-required-signal-input)
- [178: How do you test model() two-way binding?](#178-how-do-you-test-model-two-way-binding)
- [179: What are binding helpers like inputBinding for in TestBed.createComponent?](#179-what-are-binding-helpers-like-inputbinding-for-in-testbedcreatecomponent)
- [180: When should you use a host component instead of setInput?](#180-when-should-you-use-a-host-component-instead-of-setinput)
- [181: How do you override a provider for a single test?](#181-how-do-you-override-a-provider-for-a-single-test)
- [182: How do you override a provider declared on a component?](#182-how-do-you-override-a-provider-declared-on-a-component)
- [183: What is the difference between set, add and remove in overrideComponent?](#183-what-is-the-difference-between-set-add-and-remove-in-overridecomponent)
- [184: How do you override a component's template in a test?](#184-how-do-you-override-a-components-template-in-a-test)
- [185: Why does TestBed throw "Cannot override ... after TestBed has been instantiated"?](#185-why-does-testbed-throw-cannot-override--after-testbed-has-been-instantiated)
- [186: How do you get a service from a component's own injector?](#186-how-do-you-get-a-service-from-a-components-own-injector)
- [187: How do you test a component that uses a component level store?](#187-how-do-you-test-a-component-that-uses-a-component-level-store)
- [188: How do you test InjectionTokens?](#188-how-do-you-test-injectiontokens)
- [189: How do you test a factory provider?](#189-how-do-you-test-a-factory-provider)
- [190: How do you test a component that uses DOCUMENT or window?](#190-how-do-you-test-a-component-that-uses-document-or-window)
- [191: What are component harnesses?](#191-what-are-component-harnesses)
- [192: How do you use a Material component harness?](#192-how-do-you-use-a-material-component-harness)
- [193: What is the difference between getHarness and getAllHarnesses?](#193-what-is-the-difference-between-getharness-and-getallharnesses)
- [194: How do you test a MatDialog opened by a component?](#194-how-do-you-test-a-matdialog-opened-by-a-component)
- [195: How do you test a component that opens a dialog and uses its result?](#195-how-do-you-test-a-component-that-opens-a-dialog-and-uses-its-result)
- [196: How do you test a component that uses a CDK overlay?](#196-how-do-you-test-a-component-that-uses-a-cdk-overlay)
- [197: What is @testing-library/angular?](#197-what-is-testing-libraryangular)
- [198: Why do people prefer role based queries?](#198-why-do-people-prefer-role-based-queries)
- [199: What is the difference between getBy, queryBy and findBy in Testing Library?](#199-what-is-the-difference-between-getby-queryby-and-findby-in-testing-library)
- [200: What is userEvent and how is it different from fireEvent?](#200-what-is-userevent-and-how-is-it-different-from-fireevent)
- [201: How do you pass inputs and providers with Testing Library's render?](#201-how-do-you-pass-inputs-and-providers-with-testing-librarys-render)
- [202: What are ng-mocks and Spectator?](#202-what-are-ng-mocks-and-spectator)
- [203: How do you mock a child component with ng-mocks?](#203-how-do-you-mock-a-child-component-with-ng-mocks)
- [204: How do you test a component with OnPush change detection?](#204-how-do-you-test-a-component-with-onpush-change-detection)
- [205: What does provideZonelessChangeDetection do in tests?](#205-what-does-providezonelesschangedetection-do-in-tests)
- [206: Why should tests use the same change detection mode as the app?](#206-why-should-tests-use-the-same-change-detection-mode-as-the-app)
- [207: What is ExpressionChangedAfterItHasBeenCheckedError and why do you see it in tests?](#207-what-is-expressionchangedafterithasbeencheckederror-and-why-do-you-see-it-in-tests)
- [208: What are fakeAsync and tick?](#208-what-are-fakeasync-and-tick)
- [209: How do you replace fakeAsync in zoneless or Vitest tests?](#209-how-do-you-replace-fakeasync-in-zoneless-or-vitest-tests)
- [210: What is waitForAsync?](#210-what-is-waitforasync)
- [211: How do you test code that uses setTimeout?](#211-how-do-you-test-code-that-uses-settimeout)
- [212: How do you test an RxJS debounceTime in a component?](#212-how-do-you-test-an-rxjs-debouncetime-in-a-component)
- [213: What is marble testing?](#213-what-is-marble-testing)
- [214: When is marble testing worth it?](#214-when-is-marble-testing-worth-it)
- [215: How do you test switchMap cancellation?](#215-how-do-you-test-switchmap-cancellation)
- [216: How do you test that a subscription is cleaned up on destroy?](#216-how-do-you-test-that-a-subscription-is-cleaned-up-on-destroy)
- [217: How do you test a service that wraps a third party library?](#217-how-do-you-test-a-service-that-wraps-a-third-party-library)
- [218: How do you test a component that uses a Web API missing in jsdom?](#218-how-do-you-test-a-component-that-uses-a-web-api-missing-in-jsdom)
- [219: How do you mock window.matchMedia in tests?](#219-how-do-you-mock-windowmatchmedia-in-tests)
- [220: How do you test a component that uses BreakpointObserver?](#220-how-do-you-test-a-component-that-uses-breakpointobserver)
- [221: How do you test @defer blocks?](#221-how-do-you-test-defer-blocks)
- [222: What is the difference between Manual and Playthrough defer behavior?](#222-what-is-the-difference-between-manual-and-playthrough-defer-behavior)
- [223: How do you test a pipe that depends on a service?](#223-how-do-you-test-a-pipe-that-depends-on-a-service)
- [224: How do you test an impure pipe?](#224-how-do-you-test-an-impure-pipe)
- [225: How do you test a structural directive?](#225-how-do-you-test-a-structural-directive)
- [226: How do you test a directive's inputs and outputs?](#226-how-do-you-test-a-directives-inputs-and-outputs)
- [227: How do you get a directive instance from the DOM in a test?](#227-how-do-you-get-a-directive-instance-from-the-dom-in-a-test)
- [228: How do you test a ControlValueAccessor?](#228-how-do-you-test-a-controlvalueaccessor)
- [229: How do you test an async validator?](#229-how-do-you-test-an-async-validator)
- [230: How do you test a cross-field validator?](#230-how-do-you-test-a-cross-field-validator)
- [231: How do you test that validation messages appear only after touch?](#231-how-do-you-test-that-validation-messages-appear-only-after-touch)
- [232: How do you test a FormArray in a component?](#232-how-do-you-test-a-formarray-in-a-component)
- [233: How do you test signal forms?](#233-how-do-you-test-signal-forms)
- [234: How do you test a component that uses NgRx Store?](#234-how-do-you-test-a-component-that-uses-ngrx-store)
- [235: How do you test NgRx reducers and selectors?](#235-how-do-you-test-ngrx-reducers-and-selectors)
- [236: How do you test NgRx effects?](#236-how-do-you-test-ngrx-effects)
- [237: How do you test an NgRx SignalStore?](#237-how-do-you-test-an-ngrx-signalstore)
- [238: How do you test a service that uses a BehaviorSubject for state?](#238-how-do-you-test-a-service-that-uses-a-behaviorsubject-for-state)
- [239: How do you test that a component calls a service with the right data?](#239-how-do-you-test-that-a-component-calls-a-service-with-the-right-data)
- [240: How do you type fake services safely in TypeScript?](#240-how-do-you-type-fake-services-safely-in-typescript)
- [241: What are Vitest's vi.mocked and Mocked types for?](#241-what-are-vitests-vimocked-and-mocked-types-for)
- [242: Should you use vi.mock to mock modules in Angular tests?](#242-should-you-use-vimock-to-mock-modules-in-angular-tests)
- [243: How do you test a component that uses the Title or Meta service?](#243-how-do-you-test-a-component-that-uses-the-title-or-meta-service)
- [244: How do you test a custom TitleStrategy?](#244-how-do-you-test-a-custom-titlestrategy)
- [245: How do you test lazy loaded routes?](#245-how-do-you-test-lazy-loaded-routes)
- [246: How do you test withComponentInputBinding?](#246-how-do-you-test-withcomponentinputbinding)
- [247: What does RouterTestingHarness.navigateByUrl return?](#247-what-does-routertestingharnessnavigatebyurl-return)
- [248: How do you test a canDeactivate guard?](#248-how-do-you-test-a-candeactivate-guard)
- [249: How do you test the Location service?](#249-how-do-you-test-the-location-service)
- [250: How do you test a component that listens to router events?](#250-how-do-you-test-a-component-that-listens-to-router-events)
- [251: How do you test a component that uses an ElementRef directly?](#251-how-do-you-test-a-component-that-uses-an-elementref-directly)
- [252: How do you test afterNextRender or afterEveryRender hooks?](#252-how-do-you-test-afternextrender-or-aftereveryrender-hooks)
- [253: How do you test a component that uses Renderer2?](#253-how-do-you-test-a-component-that-uses-renderer2)
- [254: How do you test dynamic components created with ViewContainerRef?](#254-how-do-you-test-dynamic-components-created-with-viewcontainerref)
- [255: How do you test NgComponentOutlet usage?](#255-how-do-you-test-ngcomponentoutlet-usage)
- [256: How do you test a component that uses createComponent outside a view?](#256-how-do-you-test-a-component-that-uses-createcomponent-outside-a-view)
- [257: How do you test animations in a component?](#257-how-do-you-test-animations-in-a-component)
- [258: What is the difference between provideNoopAnimations and provideAnimations in tests?](#258-what-is-the-difference-between-providenoopanimations-and-provideanimations-in-tests)
- [259: How do you test a component that uses a CDK drag and drop list?](#259-how-do-you-test-a-component-that-uses-a-cdk-drag-and-drop-list)
- [260: How do you test a component that uses virtual scrolling?](#260-how-do-you-test-a-component-that-uses-virtual-scrolling)
- [261: How do you test focus management and keyboard navigation?](#261-how-do-you-test-focus-management-and-keyboard-navigation)
- [262: How do you test accessibility in unit tests?](#262-how-do-you-test-accessibility-in-unit-tests)
- [263: How do you test a component's ARIA state?](#263-how-do-you-test-a-components-aria-state)
- [264: How do you write snapshot tests in Vitest?](#264-how-do-you-write-snapshot-tests-in-vitest)
- [265: What are the downsides of snapshot tests?](#265-what-are-the-downsides-of-snapshot-tests)
- [266: How do you test a component with ChangeDetectorRef.detectChanges inside it?](#266-how-do-you-test-a-component-with-changedetectorrefdetectchanges-inside-it)
- [267: How do you test a component that depends on PLATFORM_ID?](#267-how-do-you-test-a-component-that-depends-on-platform_id)
- [268: How do you test HTTP caching in a service?](#268-how-do-you-test-http-caching-in-a-service)
- [269: How do you test request progress or file uploads?](#269-how-do-you-test-request-progress-or-file-uploads)
- [270: How do you test headers in an HTTP response?](#270-how-do-you-test-headers-in-an-http-response)
- [271: How do you test the withFetch backend?](#271-how-do-you-test-the-withfetch-backend)
- [272: How do you test an HttpContext token used by an interceptor?](#272-how-do-you-test-an-httpcontext-token-used-by-an-interceptor)
- [273: How do you test the order of interceptors?](#273-how-do-you-test-the-order-of-interceptors)
- [274: How do you test a service that polls an API?](#274-how-do-you-test-a-service-that-polls-an-api)
- [275: How do you test WebSocket code?](#275-how-do-you-test-websocket-code)
- [276: How do you test a service worker or PWA logic?](#276-how-do-you-test-a-service-worker-or-pwa-logic)
- [277: How do you share setup between many spec files?](#277-how-do-you-share-setup-between-many-spec-files)
- [278: What is the page object pattern in component tests?](#278-what-is-the-page-object-pattern-in-component-tests)
- [279: How do you write your own component harness?](#279-how-do-you-write-your-own-component-harness)
- [280: How do you add filters to a custom harness?](#280-how-do-you-add-filters-to-a-custom-harness)
- [281: Can component harnesses be used in E2E tests too?](#281-can-component-harnesses-be-used-in-e2e-tests-too)
- [282: How do you test a component inside a Material table?](#282-how-do-you-test-a-component-inside-a-material-table)
- [283: How do you test a component that uses MatSnackBar?](#283-how-do-you-test-a-component-that-uses-matsnackbar)
- [284: How do you test a component that imports a large UI library?](#284-how-do-you-test-a-component-that-imports-a-large-ui-library)
- [285: How do you test a service with a hierarchical injector setup?](#285-how-do-you-test-a-service-with-a-hierarchical-injector-setup)
- [286: How do you test injection options like optional or self?](#286-how-do-you-test-injection-options-like-optional-or-self)
- [287: How do you test APP_INITIALIZER or provideAppInitializer?](#287-how-do-you-test-app_initializer-or-provideappinitializer)
- [288: How do you test environment specific config in tests?](#288-how-do-you-test-environment-specific-config-in-tests)
- [289: How do you test a feature flag in a component?](#289-how-do-you-test-a-feature-flag-in-a-component)
- [290: How do you test a component that uses inject(DestroyRef)?](#290-how-do-you-test-a-component-that-uses-injectdestroyref)
- [291: How do you test takeUntilDestroyed?](#291-how-do-you-test-takeuntildestroyed)
- [292: How do you test error handling with ErrorHandler?](#292-how-do-you-test-error-handling-with-errorhandler)
- [293: How do you check console errors in tests?](#293-how-do-you-check-console-errors-in-tests)
- [294: What are errorOnUnknownElements and errorOnUnknownProperties?](#294-what-are-erroronunknownelements-and-erroronunknownproperties)
- [295: How do you test a component with a template that uses @let?](#295-how-do-you-test-a-component-with-a-template-that-uses-let)
- [296: How do you test @switch blocks?](#296-how-do-you-test-switch-blocks)
- [297: How does it.each help with Angular tests?](#297-how-does-iteach-help-with-angular-tests)
- [298: How do you debug a failing Angular test?](#298-how-do-you-debug-a-failing-angular-test)
- [299: What does error NG0201 "No provider for X" mean in a test?](#299-what-does-error-ng0201-no-provider-for-x-mean-in-a-test)
- [300: How do you test that nothing happens, for example no request is sent?](#300-how-do-you-test-that-nothing-happens-for-example-no-request-is-sent)

### Advanced Questions (301-450)

- [301: How does TestBed work internally?](#301-how-does-testbed-work-internally)
- [302: What does initTestEnvironment do and when do you call it?](#302-what-does-inittestenvironment-do-and-when-do-you-call-it)
- [303: Why do overrides need TestBed to be "not instantiated" yet?](#303-why-do-overrides-need-testbed-to-be-not-instantiated-yet)
- [304: How does the zoneless TestBed decide when the fixture is stable?](#304-how-does-the-zoneless-testbed-decide-when-the-fixture-is-stable)
- [305: How do you make your own async work visible to whenStable?](#305-how-do-you-make-your-own-async-work-visible-to-whenstable)
- [306: What changes when you move a large test suite from Zone.js to zoneless?](#306-what-changes-when-you-move-a-large-test-suite-from-zonejs-to-zoneless)
- [307: Can you use fakeAsync in a zoneless app's tests?](#307-can-you-use-fakeasync-in-a-zoneless-apps-tests)
- [308: What are the pitfalls of Vitest fake timers with Angular?](#308-what-are-the-pitfalls-of-vitest-fake-timers-with-angular)
- [309: How do you test a race condition between two async calls?](#309-how-do-you-test-a-race-condition-between-two-async-calls)
- [310: How do you test memory leaks in components?](#310-how-do-you-test-memory-leaks-in-components)
- [311: How do you test a component's performance-sensitive behavior?](#311-how-do-you-test-a-components-performance-sensitive-behavior)
- [312: How do you test that @for track reuses DOM nodes?](#312-how-do-you-test-that-for-track-reuses-dom-nodes)
- [313: How do you test signal equality functions?](#313-how-do-you-test-signal-equality-functions)
- [314: How do you test code that reads signals with untracked?](#314-how-do-you-test-code-that-reads-signals-with-untracked)
- [315: How do you test an effect's cleanup function?](#315-how-do-you-test-an-effects-cleanup-function)
- [316: Why is testing effects directly often a smell?](#316-why-is-testing-effects-directly-often-a-smell)
- [317: How do you test the difference between root effects and component effects?](#317-how-do-you-test-the-difference-between-root-effects-and-component-effects)
- [318: How do you test a resource that reacts to signal params?](#318-how-do-you-test-a-resource-that-reacts-to-signal-params)
- [319: How do you test resource error and status states?](#319-how-do-you-test-resource-error-and-status-states)
- [320: How do you design Angular code so it's easy to test?](#320-how-do-you-design-angular-code-so-its-easy-to-test)
- [321: How do you inject time to make tests deterministic?](#321-how-do-you-inject-time-to-make-tests-deterministic)
- [322: How do you decide between mocking and using real dependencies?](#322-how-do-you-decide-between-mocking-and-using-real-dependencies)
- [323: What is the risk of mocking too much?](#323-what-is-the-risk-of-mocking-too-much)
- [324: What is contract testing and how does it relate to Angular apps?](#324-what-is-contract-testing-and-how-does-it-relate-to-angular-apps)
- [325: How do you keep HTTP mock data in sync with the real API?](#325-how-do-you-keep-http-mock-data-in-sync-with-the-real-api)
- [326: How do you use MSW with Angular tests?](#326-how-do-you-use-msw-with-angular-tests)
- [327: HttpTestingController or MSW: which is better?](#327-httptestingcontroller-or-msw-which-is-better)
- [328: How do you structure tests for a large Angular codebase?](#328-how-do-you-structure-tests-for-a-large-angular-codebase)
- [329: How do you only run tests affected by a change?](#329-how-do-you-only-run-tests-affected-by-a-change)
- [330: How do you make a slow test suite faster?](#330-how-do-you-make-a-slow-test-suite-faster)
- [331: What are the trade-offs of Vitest isolation and pools?](#331-what-are-the-trade-offs-of-vitest-isolation-and-pools)
- [332: How do you find tests that depend on order?](#332-how-do-you-find-tests-that-depend-on-order)
- [333: How do you deal with flaky tests in CI?](#333-how-do-you-deal-with-flaky-tests-in-ci)
- [334: Why do tests fail in CI but pass locally?](#334-why-do-tests-fail-in-ci-but-pass-locally)
- [335: How do you test locale-dependent formatting?](#335-how-do-you-test-locale-dependent-formatting)
- [336: How do you test the default ErrorHandler behavior in zoneless apps?](#336-how-do-you-test-the-default-errorhandler-behavior-in-zoneless-apps)
- [337: What is the rethrowApplicationErrors option?](#337-what-is-the-rethrowapplicationerrors-option)
- [338: How do you test a custom ErrorHandler?](#338-how-do-you-test-a-custom-errorhandler)
- [339: How do you test server-side rendering logic?](#339-how-do-you-test-server-side-rendering-logic)
- [340: How do you test hydration problems?](#340-how-do-you-test-hydration-problems)
- [341: How do you test TransferState or HTTP transfer cache behavior?](#341-how-do-you-test-transferstate-or-http-transfer-cache-behavior)
- [342: How do you test incremental hydration?](#342-how-do-you-test-incremental-hydration)
- [343: How do you test route-level render modes?](#343-how-do-you-test-route-level-render-modes)
- [344: How do you test a library of reusable components?](#344-how-do-you-test-a-library-of-reusable-components)
- [345: How do you test a component in both Zone.js and zoneless apps?](#345-how-do-you-test-a-component-in-both-zonejs-and-zoneless-apps)
- [346: How do you test a component that uses NgZone.runOutsideAngular?](#346-how-do-you-test-a-component-that-uses-ngzonerunoutsideangular)
- [347: How do you test a component that wraps a non-Angular widget library?](#347-how-do-you-test-a-component-that-wraps-a-non-angular-widget-library)
- [348: How do you test a custom element built with Angular Elements?](#348-how-do-you-test-a-custom-element-built-with-angular-elements)
- [349: How do you test a micro frontend setup?](#349-how-do-you-test-a-micro-frontend-setup)
- [350: How do you test security related code like a sanitizer bypass?](#350-how-do-you-test-security-related-code-like-a-sanitizer-bypass)
- [351: How do you test an auth flow with token refresh?](#351-how-do-you-test-an-auth-flow-with-token-refresh)
- [352: How do you test that only one refresh happens for parallel requests?](#352-how-do-you-test-that-only-one-refresh-happens-for-parallel-requests)
- [353: How do you test XSRF handling in HttpClient?](#353-how-do-you-test-xsrf-handling-in-httpclient)
- [354: How do you test role-based UI without duplicating tests?](#354-how-do-you-test-role-based-ui-without-duplicating-tests)
- [355: How do you test that sensitive data doesn't end up in logs?](#355-how-do-you-test-that-sensitive-data-doesnt-end-up-in-logs)
- [356: How do you test a CSP-compatible setup?](#356-how-do-you-test-a-csp-compatible-setup)
- [357: How do you design a test strategy for a new Angular feature?](#357-how-do-you-design-a-test-strategy-for-a-new-angular-feature)
- [358: What should not be tested in unit tests?](#358-what-should-not-be-tested-in-unit-tests)
- [359: What is mutation testing and how can it help Angular projects?](#359-what-is-mutation-testing-and-how-can-it-help-angular-projects)
- [360: How do you test a generic or reusable data table component?](#360-how-do-you-test-a-generic-or-reusable-data-table-component)
- [361: How do you test content queries like contentChildren()?](#361-how-do-you-test-content-queries-like-contentchildren)
- [362: How do you test a component that uses ng-template inputs (template outlets)?](#362-how-do-you-test-a-component-that-uses-ng-template-inputs-template-outlets)
- [363: How do you test host directives?](#363-how-do-you-test-host-directives)
- [364: How do you test a directive that uses inject() to read the host component?](#364-how-do-you-test-a-directive-that-uses-inject-to-read-the-host-component)
- [365: How do you test DI resolution modifiers like host or skipSelf?](#365-how-do-you-test-di-resolution-modifiers-like-host-or-skipself)
- [366: How do you test a service that should be a singleton across lazy routes?](#366-how-do-you-test-a-service-that-should-be-a-singleton-across-lazy-routes)
- [367: How do you test route-level providers?](#367-how-do-you-test-route-level-providers)
- [368: How do you test a router redirectTo function?](#368-how-do-you-test-a-router-redirectto-function)
- [369: How do you test navigation errors and the router's error handling?](#369-how-do-you-test-navigation-errors-and-the-routers-error-handling)
- [370: How do you test view transitions in the router?](#370-how-do-you-test-view-transitions-in-the-router)
- [371: How do you test a scroll restoration or anchor scrolling setup?](#371-how-do-you-test-a-scroll-restoration-or-anchor-scrolling-setup)
- [372: How do you test a component that reacts to element size?](#372-how-do-you-test-a-component-that-reacts-to-element-size)
- [373: When should you use Vitest browser mode instead of E2E tests?](#373-when-should-you-use-vitest-browser-mode-instead-of-e2e-tests)
- [374: How do you run the same component test in several browsers?](#374-how-do-you-run-the-same-component-test-in-several-browsers)
- [375: How do you test CSS that changes with a container query or media query?](#375-how-do-you-test-css-that-changes-with-a-container-query-or-media-query)
- [376: What is visual regression testing and how is it done for Angular?](#376-what-is-visual-regression-testing-and-how-is-it-done-for-angular)
- [377: How do you write a good Playwright E2E test for an Angular app?](#377-how-do-you-write-a-good-playwright-e2e-test-for-an-angular-app)
- [378: How do you mock the backend in Playwright E2E tests?](#378-how-do-you-mock-the-backend-in-playwright-e2e-tests)
- [379: How do you handle login in E2E tests efficiently?](#379-how-do-you-handle-login-in-e2e-tests-efficiently)
- [380: How do you test an Angular app with Cypress?](#380-how-do-you-test-an-angular-app-with-cypress)
- [381: How do you keep E2E tests from being flaky?](#381-how-do-you-keep-e2e-tests-from-being-flaky)
- [382: When should you use data-testid?](#382-when-should-you-use-data-testid)
- [383: How do you test the production build specifically?](#383-how-do-you-test-the-production-build-specifically)
- [384: What are dev mode checks and why do they matter in tests?](#384-what-are-dev-mode-checks-and-why-do-they-matter-in-tests)
- [385: How do you test that a component doesn't write signals during rendering?](#385-how-do-you-test-that-a-component-doesnt-write-signals-during-rendering)
- [386: How do you test an infinite change detection loop?](#386-how-do-you-test-an-infinite-change-detection-loop)
- [387: How do you test that OnPush children don't re-render unnecessarily?](#387-how-do-you-test-that-onpush-children-dont-re-render-unnecessarily)
- [388: How do you test a service that uses Web Workers?](#388-how-do-you-test-a-service-that-uses-web-workers)
- [389: How do you test code that uses IndexedDB?](#389-how-do-you-test-code-that-uses-indexeddb)
- [390: How do you test offline behavior?](#390-how-do-you-test-offline-behavior)
- [391: How do you test a component library's harness itself?](#391-how-do-you-test-a-component-librarys-harness-itself)
- [392: How does TestbedHarnessEnvironment handle change detection?](#392-how-does-testbedharnessenvironment-handle-change-detection)
- [393: What is TestElement in the CDK testing API?](#393-what-is-testelement-in-the-cdk-testing-api)
- [394: How do you test a component with a lot of inputs in combination?](#394-how-do-you-test-a-component-with-a-lot-of-inputs-in-combination)
- [395: What is property-based testing and where does it fit?](#395-what-is-property-based-testing-and-where-does-it-fit)
- [396: How do you test a complex multi-step form wizard?](#396-how-do-you-test-a-complex-multi-step-form-wizard)
- [397: How do you test optimistic updates?](#397-how-do-you-test-optimistic-updates)
- [398: How do you test undo and redo logic?](#398-how-do-you-test-undo-and-redo-logic)
- [399: How do you test pagination?](#399-how-do-you-test-pagination)
- [400: How do you test infinite scroll?](#400-how-do-you-test-infinite-scroll)
- [401: How do you test drag and drop with real pointer events?](#401-how-do-you-test-drag-and-drop-with-real-pointer-events)
- [402: How do you test a component that uses the Clipboard API?](#402-how-do-you-test-a-component-that-uses-the-clipboard-api)
- [403: How do you test file input and file reading?](#403-how-do-you-test-file-input-and-file-reading)
- [404: How do you test downloads triggered by the app?](#404-how-do-you-test-downloads-triggered-by-the-app)
- [405: How do you test i18n with multiple locales?](#405-how-do-you-test-i18n-with-multiple-locales)
- [406: How do you test that a component works with right-to-left layout?](#406-how-do-you-test-that-a-component-works-with-right-to-left-layout)
- [407: How do you test the TestBed teardown behavior itself?](#407-how-do-you-test-the-testbed-teardown-behavior-itself)
- [408: How do you fix tests that break when destroyAfterEach is enabled?](#408-how-do-you-fix-tests-that-break-when-destroyaftereach-is-enabled)
- [409: How do you share TestBed configuration across a big project?](#409-how-do-you-share-testbed-configuration-across-a-big-project)
- [410: How do you test a library's secondary entry point like my-lib/testing?](#410-how-do-you-test-a-librarys-secondary-entry-point-like-my-libtesting)
- [411: How do you write fakes that work with both Jasmine and Vitest?](#411-how-do-you-write-fakes-that-work-with-both-jasmine-and-vitest)
- [412: How do you test a component that uses a global CSS class from a design system?](#412-how-do-you-test-a-component-that-uses-a-global-css-class-from-a-design-system)
- [413: How do you test components with Storybook?](#413-how-do-you-test-components-with-storybook)
- [414: How do you measure the quality of a test suite beyond coverage?](#414-how-do-you-measure-the-quality-of-a-test-suite-beyond-coverage)
- [415: How do you test code that depends on random values?](#415-how-do-you-test-code-that-depends-on-random-values)
- [416: How do you test crypto.randomUUID usage?](#416-how-do-you-test-cryptorandomuuid-usage)
- [417: How do you test analytics tracking without coupling tests to it?](#417-how-do-you-test-analytics-tracking-without-coupling-tests-to-it)
- [418: How do you test a component that should be lazy loaded with @defer on viewport?](#418-how-do-you-test-a-component-that-should-be-lazy-loaded-with-defer-on-viewport)
- [419: How do you test that a lazy chunk isn't in the initial bundle?](#419-how-do-you-test-that-a-lazy-chunk-isnt-in-the-initial-bundle)
- [420: How do you test a custom RouteReuseStrategy?](#420-how-do-you-test-a-custom-routereusestrategy)
- [421: How do you test a custom UrlSerializer or UrlMatcher?](#421-how-do-you-test-a-custom-urlserializer-or-urlmatcher)
- [422: How do you test a long-running Observable stream that never completes?](#422-how-do-you-test-a-long-running-observable-stream-that-never-completes)
- [423: How do you test retry with backoff?](#423-how-do-you-test-retry-with-backoff)
- [424: How do you test an observable created with shareReplay?](#424-how-do-you-test-an-observable-created-with-sharereplay)
- [425: What makes a test "brittle" and how do you avoid it?](#425-what-makes-a-test-brittle-and-how-do-you-avoid-it)
- [426: How do you review tests in a pull request?](#426-how-do-you-review-tests-in-a-pull-request)
- [427: How do you test code that copies the implementation instead of checking it?](#427-how-do-you-test-code-that-copies-the-implementation-instead-of-checking-it)
- [428: How do you test Angular's built-in pipes in your templates without retesting the pipes?](#428-how-do-you-test-angulars-built-in-pipes-in-your-templates-without-retesting-the-pipes)
- [429: How do you approach testing legacy NgModule-based code before migrating to standalone?](#429-how-do-you-approach-testing-legacy-ngmodule-based-code-before-migrating-to-standalone)
- [430: How do you migrate old Jasmine tests to Vitest at scale?](#430-how-do-you-migrate-old-jasmine-tests-to-vitest-at-scale)
- [431: What are custom matchers and when do you write them?](#431-what-are-custom-matchers-and-when-do-you-write-them)
- [432: How do you test that a component cleans up DOM it added to document.body?](#432-how-do-you-test-that-a-component-cleans-up-dom-it-added-to-documentbody)
- [433: How do you test a signal-based store with async methods?](#433-how-do-you-test-a-signal-based-store-with-async-methods)
- [434: How do you test concurrency rules in an rxMethod or effect?](#434-how-do-you-test-concurrency-rules-in-an-rxmethod-or-effect)
- [435: How do you test that a component works with both default and custom injection tokens?](#435-how-do-you-test-that-a-component-works-with-both-default-and-custom-injection-tokens)
- [436: How do you test code that branches on isDevMode()?](#436-how-do-you-test-code-that-branches-on-isdevmode)
- [437: How do you test Angular schematics?](#437-how-do-you-test-angular-schematics)
- [438: How do you test custom builders?](#438-how-do-you-test-custom-builders)
- [439: How do you test a custom ESLint rule for Angular templates?](#439-how-do-you-test-a-custom-eslint-rule-for-angular-templates)
- [440: How do you balance test speed and confidence in CI?](#440-how-do-you-balance-test-speed-and-confidence-in-ci)
- [441: How do you test that deprecated APIs aren't used in tests?](#441-how-do-you-test-that-deprecated-apis-arent-used-in-tests)
- [442: How do you test with real Angular Material theming and density?](#442-how-do-you-test-with-real-angular-material-theming-and-density)
- [443: What is the role of TestBed in component tests versus plain class tests?](#443-what-is-the-role-of-testbed-in-component-tests-versus-plain-class-tests)
- [444: How do you test what happens when a required dependency throws during construction?](#444-how-do-you-test-what-happens-when-a-required-dependency-throws-during-construction)
- [445: How do you test multiple app-wide states like logged in, logged out and expired session?](#445-how-do-you-test-multiple-app-wide-states-like-logged-in-logged-out-and-expired-session)
- [446: How do you test that an app still boots with its real providers?](#446-how-do-you-test-that-an-app-still-boots-with-its-real-providers)
- [447: How would you test a dashboard page with many widgets that load in parallel?](#447-how-would-you-test-a-dashboard-page-with-many-widgets-that-load-in-parallel)
- [448: A test passes alone but fails when the whole suite runs. How do you investigate?](#448-a-test-passes-alone-but-fails-when-the-whole-suite-runs-how-do-you-investigate)
- [449: A component test is very slow. What do you check?](#449-a-component-test-is-very-slow-what-do-you-check)
- [450: How would you introduce testing standards to an Angular team?](#450-how-would-you-introduce-testing-standards-to-an-angular-team)

---

# Easy Questions (1-150)

## 1: Why do we write tests for Angular applications?

Tests check that the code does what you expect, and they keep checking it every time someone changes something. Without them, a small change in a service can break a page nobody looked at.

They also make refactoring safer, act as living documentation for how a component or service should behave, and catch bugs before they reach users.

## 2: What kinds of tests are common in an Angular project?

- **Unit tests:** test one class, function, pipe or component in isolation.
- **Integration tests:** test a few pieces together, for example a component with its child components and a real service.
- **End-to-end (E2E) tests:** run the whole app in a real browser and click through it like a user.

Most projects have many unit tests, fewer integration tests and a small number of E2E tests.

## 3: What is the testing pyramid?

The testing pyramid is a rule of thumb for how many tests of each kind to write. The wide base is unit tests (fast and cheap), the middle is integration tests, and the narrow top is E2E tests (slow and harder to maintain).

The idea is that most bugs can be caught cheaply at the lower levels, and E2E tests only cover the main user flows.

## 4: Which test runner does a new Angular CLI project use?

Since Angular v21, new projects use Vitest as the default unit test runner. The `test` target in `angular.json` uses the `@angular/build:unit-test` builder with `runner` set to `vitest`.

Older projects usually use Karma with Jasmine. That setup still works, and the same builder can run Karma with `runner: "karma"`, but Karma is no longer the default.

## 5: How do you run unit tests in an Angular project?

Run `ng test` (or `npm test`, which usually calls it).

```bash
ng test                # run in watch mode
ng test --no-watch     # run once, useful in CI
ng test --coverage     # also create a coverage report
```

## 6: What is a spec file?

A spec file is a file that contains tests. In Angular the name ends with `.spec.ts`, for example `user.service.spec.ts` next to `user.service.ts`.

The CLI creates a spec file automatically when you generate a component, service, pipe, directive, guard or interceptor. The test builder finds all files that match `**/*.spec.ts` by default.

## 7: What do describe, it and expect do?

- `describe` groups related tests, usually for one class or feature.
- `it` (or `test` in Vitest) defines one test case.
- `expect` makes an assertion about a value.

```ts
describe("add", () => {
  it("adds two numbers", () => {
    expect(add(2, 3)).toBe(5);
  });
});
```

These names are the same in Jasmine and Vitest, so most simple tests look the same in both.

## 8: What are beforeEach and afterEach used for?

`beforeEach` runs before every test in the `describe` block, and `afterEach` runs after every test. They are used to set up a fresh state (create the component, configure TestBed) and to clean up after it.

There are also `beforeAll` and `afterAll`, which run once for the whole block. Use them less often, because shared state between tests can make tests depend on each other.

## 9: What is TestBed?

`TestBed` is Angular's main testing utility. It creates a small Angular environment for your test, where you can register components, providers and imports, just like in a real app.

With TestBed you can create components, inject services, override providers and run change detection.

```ts
import { TestBed } from "@angular/core/testing";

TestBed.configureTestingModule({
  imports: [UserCardComponent],
  providers: [{ provide: UserService, useValue: fakeUserService }],
});
```

## 10: What does TestBed.configureTestingModule do?

It sets up the testing module for the current test. You pass it the same kind of metadata you would give an NgModule: `imports`, `providers`, and for older code `declarations`.

You usually call it in `beforeEach`. TestBed resets the module between tests, so each test starts clean.

## 11: How do you test a standalone component with TestBed?

Put the standalone component in `imports`, not `declarations`, then create it.

```ts
beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [GreetingComponent],
  }).compileComponents();
});

it("creates the component", () => {
  const fixture = TestBed.createComponent(GreetingComponent);
  expect(fixture.componentInstance).toBeTruthy();
});
```

Declaring a standalone component instead of importing it throws an error.

## 12: What is a ComponentFixture?

`ComponentFixture` is what `TestBed.createComponent()` returns. It wraps the created component and gives you access to:

- `componentInstance`: the component class instance
- `nativeElement`: the root DOM element
- `debugElement`: Angular's wrapper around the element
- `componentRef`: useful for `setInput()`
- `detectChanges()`, `whenStable()` and `autoDetectChanges()`

## 13: What does fixture.detectChanges() do?

It runs change detection on the component, so the template is updated with the current component state. The first call also runs `ngOnInit` and other lifecycle hooks.

If you change a plain field on the component and don't call `detectChanges()` (or wait for stability), the DOM in your test will still show the old value.

## 14: What does fixture.whenStable() do?

It returns a promise that resolves when the fixture has no pending work left, for example no pending change detection, timers or HTTP calls tracked by Angular.

In zoneless tests, `await fixture.whenStable()` is the recommended way to let Angular update the DOM after a state change, instead of calling `detectChanges()` by hand.

```ts
component.name.set("Ana");
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("Ana");
```

## 15: What is the difference between nativeElement and debugElement?

`nativeElement` is the real DOM element. You use normal DOM APIs on it like `querySelector` and `textContent`.

`debugElement` is an Angular wrapper around the element. It lets you query by directive, get the injector of an element, read properties and trigger Angular event handlers. You can get the DOM node from it with `debugElement.nativeElement`.

## 16: How do you read text from a component's template in a test?

Use `fixture.nativeElement` and normal DOM methods.

```ts
const el: HTMLElement = fixture.nativeElement;
expect(el.querySelector("h1")?.textContent).toContain("Welcome");
```

Make sure change detection ran first, otherwise the template may still be empty.

## 17: How do you query elements with By.css?

`By.css` is a predicate for `debugElement.query` and `queryAll`.

```ts
import { By } from "@angular/platform-browser";

const button = fixture.debugElement.query(By.css("button.save"));
const items = fixture.debugElement.queryAll(By.css("li"));
expect(items.length).toBe(3);
```

`query` returns the first match or `null`, and `queryAll` returns an array.

## 18: How do you test a simple service?

If the service has no dependencies, you can just create it with `new`. If it uses `inject()` or has dependencies, get it from TestBed.

```ts
describe("CartService", () => {
  let service: CartService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CartService);
  });

  it("starts empty", () => {
    expect(service.items()).toEqual([]);
  });
});
```

## 19: What does TestBed.inject do?

It returns an instance of a provider from the test injector, just like `inject()` does in app code.

```ts
const http = TestBed.inject(HttpTestingController);
const service = TestBed.inject(UserService);
```

It replaced the old `TestBed.get()`, which was removed. `TestBed.inject` is also type safe, so you don't need to cast the result.

## 20: Why can't you always create a service with new in a test?

Services that use the `inject()` function must be created inside an injection context. Calling `new MyService()` outside of one throws an error (NG0203).

Use `TestBed.inject(MyService)` instead, or wrap the call in `TestBed.runInInjectionContext()`.

## 21: How do you test a pipe?

A pure pipe is just a class with a `transform` method, so you can usually test it directly.

```ts
describe("TruncatePipe", () => {
  const pipe = new TruncatePipe();

  it("cuts long text", () => {
    expect(pipe.transform("Hello world", 5)).toBe("Hello...");
  });

  it("keeps short text", () => {
    expect(pipe.transform("Hi", 5)).toBe("Hi");
  });
});
```

If the pipe uses `inject()`, create it through `TestBed.runInInjectionContext(() => new TruncatePipe())`.

## 22: What is a mock?

A mock is a fake version of a dependency that you use in a test instead of the real one. For example, instead of a real `UserService` that calls an API, you give the component a fake one that returns fixed data.

Mocks keep tests fast, stop them from calling real servers, and let you test cases that are hard to trigger for real, like errors.

## 23: What is the difference between a mock, a stub and a spy?

- **Stub:** a fake that returns fixed values, with no checks.
- **Spy:** wraps or replaces a function and records how it was called.
- **Mock:** a fake object with expectations about how it should be used.

In daily Angular work people often say "mock" for all three. In practice you mostly use spies (`vi.fn()`, `vi.spyOn()`, `jasmine.createSpy()`) and simple fake objects.

## 24: How do you provide a fake service to a component in a test?

Use `providers` in `configureTestingModule` with `useValue` or `useClass`.

```ts
const userServiceStub = {
  getName: () => "Test User",
};

TestBed.configureTestingModule({
  imports: [ProfileComponent],
  providers: [{ provide: UserService, useValue: userServiceStub }],
});
```

The component now gets the stub when it injects `UserService`.

## 25: How do you create a spy in Vitest?

Use `vi.fn()` for a standalone fake function and `vi.spyOn()` to watch a method on an existing object.

```ts
import { vi } from "vitest";

const save = vi.fn().mockReturnValue(true);
save("a");
expect(save).toHaveBeenCalledWith("a");

const service = TestBed.inject(LoggerService);
const spy = vi.spyOn(service, "log");
service.log("hi");
expect(spy).toHaveBeenCalledTimes(1);
```

## 26: How do you create a spy in Jasmine?

Use `spyOn` on an existing object, or `jasmine.createSpy` and `jasmine.createSpyObj` for new fakes.

```ts
const service = jasmine.createSpyObj<UserService>("UserService", ["load"]);
service.load.and.returnValue(of([]));

spyOn(console, "error");
```

These are Jasmine APIs. In Vitest you use `vi.fn()` and `vi.spyOn()` instead.

## 27: What is the difference between toBe and toEqual?

`toBe` checks strict identity (`Object.is`), so two different objects with the same content are not equal. `toEqual` compares the content recursively.

```ts
expect(1 + 1).toBe(2);
expect({ id: 1 }).toEqual({ id: 1 }); // passes
expect({ id: 1 }).toBe({ id: 1 }); // fails
```

Use `toBe` for primitives and the same reference, `toEqual` for objects and arrays.

## 28: What are some common matchers?

- `toBe`, `toEqual`, `toStrictEqual`
- `toBeTruthy`, `toBeFalsy`, `toBeNull`, `toBeUndefined`, `toBeDefined`
- `toContain` for arrays and strings
- `toHaveLength`, `toMatch` for regex
- `toThrow` / `toThrowError`
- `toHaveBeenCalled`, `toHaveBeenCalledWith`, `toHaveBeenCalledTimes`

Use `.not` to flip any matcher, for example `expect(list).not.toContain('x')`.

## 29: How do you check that a function throws an error?

Pass a function to `expect`, not the result of calling it.

```ts
expect(() => parseAge("abc")).toThrow("Invalid age");
```

If you write `expect(parseAge('abc'))`, the error is thrown before `expect` runs and the test fails with that error.

## 30: How do you test a component's @Input or signal input?

Use `fixture.componentRef.setInput()`. It works for both signal inputs (`input()`) and old `@Input()` properties, and it marks the component for check like a real parent would.

```ts
const fixture = TestBed.createComponent(UserCardComponent);
fixture.componentRef.setInput("name", "Ana");
await fixture.whenStable();

expect(fixture.nativeElement.textContent).toContain("Ana");
```

You can't assign a signal input directly, because `input()` returns a read-only signal.

## 31: How do you test a component output?

Subscribe to the output and check what it emits. Both `output()` and `@Output()` EventEmitter have a `subscribe` method.

```ts
const fixture = TestBed.createComponent(LikeButtonComponent);
let emitted: number | undefined;
fixture.componentInstance.liked.subscribe((v) => (emitted = v));

fixture.nativeElement.querySelector("button").click();
expect(emitted).toBe(1);
```

## 32: How do you simulate a button click in a test?

The simplest way is to call `click()` on the DOM element.

```ts
const button: HTMLButtonElement = fixture.nativeElement.querySelector("button");
button.click();
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".count").textContent).toBe("1");
```

You can also use `debugElement.triggerEventHandler('click')`, but that only calls Angular's listener and skips real DOM behavior.

## 33: What does triggerEventHandler do?

`debugElement.triggerEventHandler(eventName, eventObj)` calls the event listeners that Angular registered for that event on the element. It does not create a real DOM event.

```ts
const input = fixture.debugElement.query(By.css("input"));
input.triggerEventHandler("keyup.enter", {});
```

It's handy for custom events or `(keyup.enter)`, but it won't trigger native browser behavior or listeners added outside the template.

## 34: How do you test an input field in a template?

Set the element's value and dispatch an `input` event, so Angular's form bindings see the change.

```ts
const input: HTMLInputElement = fixture.nativeElement.querySelector("input");
input.value = "hello";
input.dispatchEvent(new Event("input"));
await fixture.whenStable();

expect(fixture.componentInstance.form.value.search).toBe("hello");
```

Just setting `value` without the event does not update the model.

## 35: What does the first detectChanges call trigger?

The first `detectChanges()` call runs `ngOnInit` (and `ngOnChanges` if there are input changes made through `setInput`), then renders the template. Later calls run `ngDoCheck` and the after view hooks again as needed.

That's why many tests create the component, set inputs and only then call `detectChanges()`: so `ngOnInit` sees the inputs.

## 36: What does fixture.autoDetectChanges() do?

It makes the fixture run change detection automatically, like the real app does, instead of waiting for manual `detectChanges()` calls.

```ts
fixture.autoDetectChanges();
```

In zoneless tests, automatic change detection is the default behavior, so you mostly use `await fixture.whenStable()`. In Zone.js based tests it's off by default, and you can also turn it on with the `ComponentFixtureAutoDetect` provider.

## 37: What is code coverage?

Code coverage shows which lines, branches, functions and statements ran during your tests. Run `ng test --coverage` to get a report, usually in the `coverage/` folder.

High coverage doesn't prove the code is correct, it only shows the code ran. Low coverage does show you which parts have no tests at all.

## 38: What is the tsconfig.spec.json file for?

It's the TypeScript config used for tests. It usually extends the main `tsconfig.json`, includes `**/*.spec.ts` files and adds test types, for example `vitest/globals` or `jasmine`.

```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "types": ["vitest/globals"]
  },
  "include": ["src/**/*.spec.ts", "src/**/*.d.ts"]
}
```

## 39: How do you run a single test or a single describe block?

In both Vitest and Jasmine you can focus tests:

- Vitest: `it.only` and `describe.only`
- Jasmine: `fit` and `fdescribe`

To skip tests, use `it.skip` / `describe.skip` in Vitest, or `xit` / `xdescribe` in Jasmine. Don't commit focused tests, because they silently skip the rest of the suite.

## 40: How do you run tests for only some files?

Use the `--include` option of `ng test`.

```bash
ng test --include src/app/cart/**/*.spec.ts
ng test --include src/app/user.service.spec.ts
```

This is useful when you work on one feature and don't want to wait for the whole suite.

## 41: What is the difference between a unit test and an integration test in Angular?

A unit test checks one piece in isolation, with its dependencies replaced by fakes. For example, a component test where the service is a stub.

An integration test checks several real pieces together, for example a parent component with its real children and a real service, with only the HTTP layer faked. Integration tests catch problems in how pieces connect, but they're slower and harder to debug.

## 42: What should a good unit test look like?

A good unit test:

- Tests one behavior and has a clear name, like "shows an error when the email is empty"
- Is independent and doesn't rely on other tests running first
- Is fast and doesn't call real servers
- Checks what the user or caller sees, not private details
- Fails for one clear reason

## 43: What is the Arrange, Act, Assert pattern?

It's a simple way to structure a test in three parts:

1. **Arrange:** set up data, mocks and the component
2. **Act:** do the thing you're testing
3. **Assert:** check the result

```ts
it("adds an item", () => {
  const cart = TestBed.inject(CartService); // arrange
  cart.add({ id: 1, price: 10 }); // act
  expect(cart.total()).toBe(10); // assert
});
```

## 44: How do you test a component that has no dependencies?

Import it in TestBed, create it, run change detection and check the DOM.

```ts
it("shows the title", async () => {
  TestBed.configureTestingModule({ imports: [HeaderComponent] });
  const fixture = TestBed.createComponent(HeaderComponent);
  await fixture.whenStable();

  expect(fixture.nativeElement.querySelector("h1").textContent).toBe("My App");
});
```

## 45: What test does the CLI generate for a new component?

It generates a spec with a `beforeEach` that configures TestBed and creates the component, plus one test that checks the component was created.

```ts
it("should create", () => {
  expect(component).toBeTruthy();
});
```

This "should create" test is a smoke test. It only proves the component can be built, so you should add real tests for its behavior.

## 46: Why should each test be independent?

If tests share state, one test can pass or fail depending on which tests ran before it. That makes failures hard to understand and breaks when tests run in a different order or in parallel.

Create fresh objects in `beforeEach`, avoid module level variables that get changed, and reset spies and mocks between tests.

## 47: What is compileComponents and do you still need it?

`compileComponents()` compiles components that use external files (`templateUrl`, `styleUrl`) in environments that can't load them synchronously.

When you run tests with the Angular CLI, templates and styles are already compiled by the build, so it's usually not needed. It doesn't hurt to keep it, and the CLI generated specs often still include it with `await`.

## 48: How do you test a component that uses a service through inject()?

The same way as with constructor injection. Register a fake for the service in TestBed, and the component's `inject()` call will get it.

```ts
@Component({ selector: "app-hello", template: "{{ greeter.hello() }}" })
class HelloComponent {
  greeter = inject(GreeterService);
}

TestBed.configureTestingModule({
  imports: [HelloComponent],
  providers: [{ provide: GreeterService, useValue: { hello: () => "Hi!" } }],
});
```

## 49: What is the difference between useValue and useClass in test providers?

- `useValue` gives one fixed object, usually a simple stub you wrote in the test.
- `useClass` tells Angular to create an instance of another class, for example `FakeUserService`.

```ts
providers: [
  { provide: ApiService, useValue: { get: vi.fn() } },
  { provide: UserService, useClass: FakeUserService },
];
```

`useClass` is nice when the fake has its own logic or is reused across many spec files.

## 50: How do you check that a CSS class is applied to an element?

Use `classList` on the DOM element or `classes` on the debug element.

```ts
const el: HTMLElement = fixture.nativeElement.querySelector(".alert");
expect(el.classList.contains("alert-error")).toBe(true);

const de = fixture.debugElement.query(By.css(".alert"));
expect(de.classes["alert-error"]).toBe(true);
```

## 51: How do you test that an element is shown or hidden with @if?

Change the state that controls the `@if` block, let Angular update the view, and check whether the element exists.

```ts
it("shows the error only when there is one", async () => {
  const fixture = TestBed.createComponent(LoginComponent);
  await fixture.whenStable();
  expect(fixture.nativeElement.querySelector(".error")).toBeNull();

  fixture.componentInstance.error.set("Wrong password");
  await fixture.whenStable();
  expect(fixture.nativeElement.querySelector(".error").textContent).toContain(
    "Wrong password",
  );
});
```

## 52: How do you test a list rendered with @for?

Set the data, update the view and count the rendered elements.

```ts
fixture.componentRef.setInput("items", ["a", "b", "c"]);
await fixture.whenStable();

const rows = fixture.nativeElement.querySelectorAll("li");
expect(rows.length).toBe(3);
expect(rows[1].textContent).toContain("b");
```

Also test the `@empty` block if the template has one, by passing an empty array.

## 53: How do you test a signal in a service?

Signals are plain values you can read by calling them, so testing them is direct.

```ts
it("increments the counter", () => {
  const counter = TestBed.inject(CounterService);
  counter.increment();
  counter.increment();
  expect(counter.count()).toBe(2);
});
```

No change detection is needed when you only read signals in a service.

## 54: How do you test a computed signal?

Change the source signals and read the computed one. Computed signals update lazily when you read them.

```ts
const cart = TestBed.inject(CartService);
cart.add({ price: 10 });
cart.add({ price: 5 });
expect(cart.total()).toBe(15);
```

## 55: How do you test a component that uses signals for state?

Change the signal through the component or through user actions, wait for stability and check the DOM.

```ts
const fixture = TestBed.createComponent(CounterComponent);
fixture.nativeElement.querySelector("button").click();
await fixture.whenStable();
expect(fixture.nativeElement.querySelector("span").textContent).toBe("1");
```

Signals notify Angular when they change, so this works well in zoneless mode.

## 56: What is jsdom and why is it used in Angular tests?

jsdom is a JavaScript implementation of the DOM that runs in Node.js. With Vitest, Angular tests run in Node by default and use jsdom (or happy-dom) to give components a `document` and `window`.

It's fast, but it's not a real browser. Layout, CSS sizes, scrolling and some browser APIs don't work, so tests that need them should run in browser mode or as E2E tests.

## 57: What is Karma?

Karma is a test runner that starts real browsers, loads your tests into them and reports the results. For years it was the default for Angular projects, together with Jasmine.

It's now legacy in Angular. New projects use Vitest, but the `@angular/build:unit-test` builder can still run Karma with `runner: "karma"`, and older projects may use the older `@angular-devkit/build-angular:karma` builder.

## 58: What is Jasmine?

Jasmine is a testing framework that gives you `describe`, `it`, `expect`, matchers and spies (`spyOn`, `jasmine.createSpyObj`). It was the default framework for Angular tests together with Karma.

Many Angular tests are still written in Jasmine. Most of the syntax is the same in Vitest, but spies and clock helpers are different.

## 59: What is Vitest?

Vitest is a fast test framework built on Vite. It has a Jest-like API (`describe`, `it`, `expect`, `vi.fn()`, `vi.spyOn()`) and runs tests in Node with jsdom, or in a real browser with browser mode.

In Angular v21 and later, it's the default unit test runner. The Angular CLI compiles your code and passes it to Vitest through the `@angular/build:unit-test` builder.

## 60: Where is the test configuration stored in an Angular project?

In the `test` target of the project in `angular.json`.

```json
"test": {
  "builder": "@angular/build:unit-test",
  "options": {
    "runner": "vitest",
    "tsConfig": "tsconfig.spec.json"
  }
}
```

There's also `tsconfig.spec.json` for TypeScript settings, and optionally a Vitest config file if you need more control.

## 61: What does ng generate do for tests?

When you run `ng generate component`, `service`, `pipe`, `directive`, `guard` or `interceptor`, the CLI also creates a matching `.spec.ts` file with a basic test.

You can skip it with `--skip-tests`, or turn it off in `angular.json` schematics settings, but most teams keep it so every new file starts with a test.

## 62: How do you test a component method directly?

You can call the method on `componentInstance` and check the result or state.

```ts
const component = fixture.componentInstance;
component.addTodo("Buy milk");
expect(component.todos()).toContain("Buy milk");
```

This is fine for logic, but also test through the template for anything the user sees. Testing only methods can miss broken bindings in the HTML.

## 63: What is a smoke test?

A smoke test is a very basic test that checks something can start without crashing. In Angular the generated "should create" test is a smoke test.

It catches missing providers and broken imports, but it says nothing about whether the component works. Treat it as a starting point.

## 64: Why should you avoid testing private methods directly?

Private methods are details of how the code works. If you test them directly, your tests break every time you refactor, even when the behavior stays the same.

Test them through the public API instead: the inputs, outputs, DOM and public methods that use them.

## 65: How do you test a component with an ngOnInit that loads data?

Give the component a fake service, trigger `ngOnInit` with the first change detection, and check the result.

```ts
TestBed.configureTestingModule({
  imports: [UsersComponent],
  providers: [
    { provide: UserService, useValue: { getAll: () => of([{ name: "Ana" }]) } },
  ],
});

const fixture = TestBed.createComponent(UsersComponent);
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("Ana");
```

## 66: What is of() used for in tests?

`of()` from RxJS creates an observable that emits the given values and completes right away. It's the easiest way to fake a service method that returns an observable.

```ts
const service = {
  getUser: vi.fn().mockReturnValue(of({ id: 1, name: "Ana" })),
};
```

Because it emits synchronously, the data is there right after you subscribe.

## 67: How do you fake an observable that fails?

Use `throwError` from RxJS.

```ts
import { throwError } from "rxjs";

const service = {
  getUser: vi.fn().mockReturnValue(throwError(() => new Error("Not found"))),
};
```

Then check that the component shows the error message or handles it the way it should.

## 68: How do you test an observable returned by a service?

Subscribe to it in the test and check the emitted values.

```ts
it("returns active users", () => {
  const service = TestBed.inject(UserFilterService);
  let result: User[] = [];
  service.active$(of(users)).subscribe((r) => (result = r));
  expect(result.length).toBe(2);
});
```

For async observables, use `firstValueFrom` with `await`, or fake timers.

## 69: How do you use firstValueFrom in tests?

`firstValueFrom` turns an observable into a promise that resolves with the first value. It makes async tests easier to read.

```ts
import { firstValueFrom } from "rxjs";

it("loads the config", async () => {
  const config = await firstValueFrom(service.loadConfig());
  expect(config.theme).toBe("dark");
});
```

If the observable completes without emitting, the promise rejects.

## 70: How do you write an async test?

Make the test function `async` and `await` the things you're waiting for. The test runner waits for the returned promise.

```ts
it("saves the user", async () => {
  await service.save(user);
  expect(api.post).toHaveBeenCalled();
});
```

If you forget to `await`, the test may finish before the work is done and pass for the wrong reason.

## 71: What does the done callback do in tests?

Older tests use a `done` callback to tell the runner when an async test is finished.

```ts
it("emits a value", (done) => {
  service.value$.subscribe((v) => {
    expect(v).toBe(1);
    done();
  });
});
```

Jasmine supports it. Vitest does not support `done` in `it`, so in new code use `async`/`await` and convert observables with `firstValueFrom`.

## 72: How do you test a component with a template reference to a child component?

If the child is a standalone component imported by the parent, it gets created too. You can find it with `By.directive`.

```ts
const child = fixture.debugElement.query(By.directive(ChildComponent));
expect(child.componentInstance.title()).toBe("Hello");
```

This way you can check the inputs the parent passed to the child.

## 73: What is By.directive used for?

`By.directive(Type)` finds debug elements that have a given component or directive on them.

```ts
const tooltips = fixture.debugElement.queryAll(By.directive(TooltipDirective));
expect(tooltips.length).toBe(2);

const instance = tooltips[0].injector.get(TooltipDirective);
```

It's useful when there's no good CSS selector, or when you need the directive instance itself.

## 74: How do you test a simple attribute directive?

Create a small host component in the spec that uses the directive, then check the effect on the element.

```ts
@Component({
  imports: [HighlightDirective],
  template: '<p appHighlight="yellow">Text</p>',
})
class HostComponent {}

it("sets the background", async () => {
  const fixture = TestBed.createComponent(HostComponent);
  await fixture.whenStable();
  const p: HTMLElement = fixture.nativeElement.querySelector("p");
  expect(p.style.backgroundColor).toBe("yellow");
});
```

## 75: What is a test host component?

A test host component is a small component written only inside a spec file. It wraps the component or directive you want to test and uses it in a template, the same way real code would.

It's useful to test inputs and outputs through real bindings, content projection, and directives that need a host element.

## 76: How do you check an element's attribute in a test?

Use `getAttribute` on the DOM element, or `attributes` on the debug element.

```ts
const link: HTMLAnchorElement = fixture.nativeElement.querySelector("a");
expect(link.getAttribute("href")).toBe("/home");

const img = fixture.debugElement.query(By.css("img"));
expect(img.attributes["alt"]).toBe("Logo");
```

## 77: How do you check if a button is disabled?

Read the `disabled` property of the button element.

```ts
const button: HTMLButtonElement = fixture.nativeElement.querySelector(
  "button[type=submit]",
);
expect(button.disabled).toBe(true);

fixture.componentInstance.form.setValue({ email: "a@b.com" });
await fixture.whenStable();
expect(button.disabled).toBe(false);
```

## 78: How do you test a reactive form's validation?

Set values on the form controls and check `valid`, `invalid` and `errors`.

```ts
const form = fixture.componentInstance.form;
form.controls.email.setValue("wrong");
expect(form.controls.email.hasError("email")).toBe(true);

form.controls.email.setValue("ana@example.com");
expect(form.controls.email.valid).toBe(true);
```

Also test that the error message shows in the template when the control is touched and invalid.

## 79: How do you test a custom validator function?

A validator is a plain function that takes a control and returns errors or `null`, so test it directly.

```ts
import { FormControl } from "@angular/forms";

it("rejects spaces", () => {
  expect(noSpaces(new FormControl("a b"))).toEqual({ noSpaces: true });
  expect(noSpaces(new FormControl("ab"))).toBeNull();
});
```

## 80: What is HttpClientTestingModule and what replaces it?

`HttpClientTestingModule` was the old way to fake HTTP calls in tests. In modern Angular you use providers instead:

```ts
import { provideHttpClient } from "@angular/common/http";
import { provideHttpClientTesting } from "@angular/common/http/testing";

TestBed.configureTestingModule({
  providers: [provideHttpClient(), provideHttpClientTesting()],
});
```

`HttpClientTestingModule` is deprecated, but you'll still see it in older projects.

## 81: What is HttpTestingController?

`HttpTestingController` lets you check which HTTP requests were made and respond to them with fake data, without any real network calls.

```ts
const httpMock = TestBed.inject(HttpTestingController);
service.getUsers().subscribe((users) => expect(users.length).toBe(1));

const req = httpMock.expectOne("/api/users");
expect(req.request.method).toBe("GET");
req.flush([{ id: 1 }]);
```

## 82: What does req.flush() do?

`flush()` completes a fake HTTP request with the body you pass. The observable returned by `HttpClient` then emits that body and completes.

You can also pass status and headers:

```ts
req.flush({ message: "Not found" }, { status: 404, statusText: "Not Found" });
```

## 83: What does httpMock.verify() do?

`verify()` checks that there are no HTTP requests left that the test did not handle. If there are, it throws.

```ts
afterEach(() => {
  TestBed.inject(HttpTestingController).verify();
});
```

It catches bugs like a service sending an extra request or calling the wrong URL.

## 84: Why does the order of provideHttpClient and provideHttpClientTesting matter?

`provideHttpClientTesting()` replaces the real HTTP backend with a testing one. It must come after `provideHttpClient()`, otherwise the real backend setup may win.

```ts
providers: [provideHttpClient(), provideHttpClientTesting()];
```

The Angular docs show this order and recommend sticking to it.

## 85: How do you test a service that makes a POST request?

Call the service, find the request with `expectOne`, and check the method and body.

```ts
it("creates a user", () => {
  service.create({ name: "Ana" }).subscribe();

  const req = httpMock.expectOne("/api/users");
  expect(req.request.method).toBe("POST");
  expect(req.request.body).toEqual({ name: "Ana" });
  req.flush({ id: 1, name: "Ana" });
});
```

## 86: How do you test an HTTP error in a service?

Flush the request with an error status and check the error handling.

```ts
it("handles 500", () => {
  let error: HttpErrorResponse | undefined;
  service.getUsers().subscribe({ error: (e) => (error = e) });

  httpMock
    .expectOne("/api/users")
    .flush("Server error", { status: 500, statusText: "Error" });
  expect(error?.status).toBe(500);
});
```

For network errors, use `req.error(new ProgressEvent('error'))`.

## 87: What is E2E testing?

End-to-end testing runs the whole app in a real browser and checks full user flows, like signing up or placing an order. The test clicks buttons and types text like a real user.

E2E tests catch problems that unit tests miss, like wrong routes, broken API wiring or layout issues. They're slower and more fragile, so keep them for the most important flows.

## 88: Which E2E tools are used with Angular today?

Protractor was the old default, but it's deprecated and no longer maintained. Today teams use:

- Playwright
- Cypress
- WebdriverIO

Run `ng e2e` in a project without an E2E setup and the CLI asks you which package to add.

## 89: What was Protractor and why was it dropped?

Protractor was Angular's original E2E framework, built on WebDriver. It waited for Angular to be stable before each step.

The Angular team deprecated it because modern tools like Playwright and Cypress are faster, easier to debug and widely used. Protractor reached end of life, so old projects should move to another tool.

## 90: What is the difference between toHaveBeenCalled and toHaveBeenCalledWith?

`toHaveBeenCalled` only checks that the spy was called at least once. `toHaveBeenCalledWith` also checks the arguments of at least one call.

```ts
expect(logger.log).toHaveBeenCalled();
expect(logger.log).toHaveBeenCalledWith("saved", 42);
```

Checking arguments makes the test stronger, because a call with wrong data would still pass the first matcher.

## 91: How do you make a spy return a value in Vitest?

```ts
const getUser = vi.fn().mockReturnValue({ id: 1 });
const loadUser = vi.fn().mockResolvedValue({ id: 1 });
const failing = vi.fn().mockRejectedValue(new Error("fail"));
const once = vi.fn().mockReturnValueOnce("first").mockReturnValue("rest");
```

You can also give a full fake implementation with `mockImplementation((id) => ...)`.

## 92: How do you make a spy return a value in Jasmine?

Use the `and` property of the spy.

```ts
spy.and.returnValue(of(users));
spy.and.returnValues(1, 2, 3);
spy.and.callFake((id: number) => ({ id }));
spy.and.throwError("fail");
spy.and.callThrough();
```

`callThrough()` keeps the real method running while still recording calls.

## 93: How do you test a component that uses the async pipe?

Give the component a fake observable, wait for the view to update and check the DOM.

```ts
providers: [{ provide: NewsService, useValue: { latest$: of(["A", "B"]) } }];

const fixture = TestBed.createComponent(NewsComponent);
await fixture.whenStable();
expect(fixture.nativeElement.querySelectorAll("li").length).toBe(2);
```

When the value arrives later, use a `Subject` and call `next` from the test, then wait for stability again.

## 94: How do you use a Subject to control data in a test?

A `Subject` lets you decide when the fake service emits.

```ts
const users$ = new Subject<User[]>();
const fake = { users$ };

// ... create the component with this fake
users$.next([{ name: "Ana" }]);
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("Ana");
```

This is good for testing loading states, because you can check the view before and after the data arrives.

## 95: How do you test a loading state?

Create the component with data that hasn't arrived yet, check the loading view, then send the data and check again.

```ts
const data$ = new Subject<string[]>();
// provide a fake that returns data$
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".spinner")).not.toBeNull();

data$.next(["x"]);
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".spinner")).toBeNull();
```

## 96: What is the point of testing what the user sees instead of internal state?

Users and other code only care about the result: what shows on the screen and what gets emitted or saved. If you test internal fields, tests break when you rename or restructure things, even though the app still works.

Tests that check the DOM and public behavior give you more confidence and survive refactors better.

## 97: How do you name tests well?

Write the name as a sentence that describes behavior, so a failure tells you what broke.

- Good: "shows an error when the password is too short"
- Bad: "test1" or "should work"

Many teams use the pattern "should do X when Y". Group related cases under a `describe` named after the component or the method.

## 98: How do you test a component that uses the Router?

Provide the router with `provideRouter`. For simple cases where the component just uses `routerLink`, empty routes are enough.

```ts
import { provideRouter } from "@angular/router";

TestBed.configureTestingModule({
  imports: [NavComponent],
  providers: [provideRouter([])],
});
```

For components that read route params or need real navigation, use `RouterTestingHarness`.

## 99: What is RouterTestingModule and what replaces it?

`RouterTestingModule` was the old way to set up the router in tests. It's deprecated. Use `provideRouter(routes)` in providers, and `RouterTestingHarness` when you need to navigate and test routed components.

In standalone apps, `provideRouter` together with `provideLocationMocks()` covers what `RouterTestingModule` used to do.

## 100: How do you test a component that reads route parameters?

The modern way is `RouterTestingHarness`, which navigates to a real route.

```ts
import { RouterTestingHarness } from "@angular/router/testing";

TestBed.configureTestingModule({
  providers: [
    provideRouter([{ path: "users/:id", component: UserDetailComponent }]),
  ],
});

const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/users/7", UserDetailComponent);
expect(harness.routeNativeElement?.textContent).toContain("User 7");
```

The component reads the `id` from `ActivatedRoute` like it does in the real app, and the test only checks what it renders.

## 101: How do you fake ActivatedRoute in a simple unit test?

If you don't want a real router, you can provide a fake `ActivatedRoute` with only what the component uses.

```ts
import { ActivatedRoute, convertToParamMap } from "@angular/router";

providers: [
  {
    provide: ActivatedRoute,
    useValue: { paramMap: of(convertToParamMap({ id: "7" })) },
  },
];
```

This is quick, but it can drift from how the real router behaves. `RouterTestingHarness` is usually the safer choice.

## 102: How do you test that a component navigates somewhere?

Spy on the `Router` and check the call, or use `RouterTestingHarness` and check the URL.

```ts
const router = TestBed.inject(Router);
const spy = vi.spyOn(router, "navigate").mockResolvedValue(true);

fixture.componentInstance.goHome();
expect(spy).toHaveBeenCalledWith(["/home"]);
```

Spying is simple and fast. A real navigation test is closer to how users experience the app.

## 103: How do you test a routerLink?

Check the `href` attribute that Angular renders on the anchor.

```ts
TestBed.configureTestingModule({
  imports: [MenuComponent],
  providers: [provideRouter([])],
});

const fixture = TestBed.createComponent(MenuComponent);
await fixture.whenStable();
const link = fixture.nativeElement.querySelector("a");
expect(link.getAttribute("href")).toBe("/settings");
```

## 104: What is the difference between shallow and deep component tests?

A **deep** test renders the component with all its real child components. A **shallow** test replaces the children with stubs, so only the component under test is really rendered.

Shallow tests are more isolated and faster to set up when children have many dependencies. Deep tests catch problems in how parent and children work together.

## 105: How do you replace a child component with a stub?

Create a stub with the same selector and inputs, then swap it in with `overrideComponent`.

```ts
@Component({ selector: "app-chart", template: "" })
class ChartStub {
  data = input<number[]>([]);
}

TestBed.configureTestingModule({ imports: [DashboardComponent] });
TestBed.overrideComponent(DashboardComponent, {
  remove: { imports: [ChartComponent] },
  add: { imports: [ChartStub] },
});
```

## 106: What is NO_ERRORS_SCHEMA?

`NO_ERRORS_SCHEMA` tells Angular to ignore unknown elements and unknown properties in templates. Some older tests used it to avoid declaring child components.

It's risky, because typos in templates and missing imports stop causing errors, so the test can pass while the real app is broken. Prefer stubs or real children. `CUSTOM_ELEMENTS_SCHEMA` is narrower and is meant for real web components.

## 107: What is a test double?

"Test double" is the general name for anything that replaces a real dependency in a test: dummies, stubs, spies, mocks and fakes. The name comes from a stunt double in movies.

A **fake** is a double with a simple but working implementation, like an in memory version of a storage service.

## 108: How do you test a component with localStorage?

The cleanest way is to wrap `localStorage` in a service and fake the service. If the code uses `localStorage` directly, you can spy on it or clear it between tests.

```ts
beforeEach(() => localStorage.clear());

it("saves the theme", () => {
  service.setTheme("dark");
  expect(localStorage.getItem("theme")).toBe("dark");
});
```

jsdom has a working `localStorage`, so these tests run fine in Node.

## 109: How do you reset spies between tests in Vitest?

Use `vi.clearAllMocks()`, `vi.resetAllMocks()` or `vi.restoreAllMocks()` in `afterEach`, or turn the matching options on in the Vitest config.

- `clearAllMocks` clears recorded calls
- `resetAllMocks` also removes fake return values
- `restoreAllMocks` puts back the original methods for `vi.spyOn` spies

```ts
afterEach(() => vi.restoreAllMocks());
```

## 110: Do Jasmine spies need to be reset between tests?

Spies created with `spyOn` inside a test or `beforeEach` are removed automatically after each test. Spies stored in variables outside `beforeEach` keep their calls, so you should create them fresh in `beforeEach` or call `spy.calls.reset()`.

## 111: How do you test a component's ngOnDestroy?

Destroy the fixture and check the effect, for example that a subscription was cleaned up or a callback was called.

```ts
const spy = vi.spyOn(fixture.componentInstance, "stopPolling");
fixture.destroy();
expect(spy).toHaveBeenCalled();
```

If the component uses `DestroyRef` or `takeUntilDestroyed`, `fixture.destroy()` triggers that too.

## 112: Does TestBed destroy components after each test?

Yes. By default TestBed tears down the testing module after each test (`teardown: { destroyAfterEach: true }`). This destroys components and services, runs `ngOnDestroy`, and removes the DOM nodes.

This keeps tests isolated and stops memory leaks across a large test suite.

## 113: How do you test text that comes from an interpolation?

Set the data, update the view and check `textContent`.

```ts
fixture.componentRef.setInput("user", { firstName: "Ana", lastName: "Lee" });
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".name").textContent.trim()).toBe(
  "Ana Lee",
);
```

Using `trim()` or `toContain` avoids failures caused by whitespace in the template.

## 114: Why do tests sometimes see old values in the DOM?

Because Angular did not run change detection after the state changed. The test changed a value, but the template was never updated.

Fix it by awaiting `fixture.whenStable()` (or calling `fixture.detectChanges()` in Zone based tests) after the change and before the assertion.

## 115: How do you test a template-driven form?

Template-driven forms update asynchronously, so wait for stability after creating the component and after typing.

```ts
const fixture = TestBed.createComponent(ContactComponent);
await fixture.whenStable();

const input: HTMLInputElement =
  fixture.nativeElement.querySelector("input[name=email]");
input.value = "ana@example.com";
input.dispatchEvent(new Event("input"));
await fixture.whenStable();

expect(fixture.componentInstance.email).toBe("ana@example.com");
```

## 116: How do you test a select dropdown?

Set the selected value or index and dispatch a `change` event.

```ts
const select: HTMLSelectElement = fixture.nativeElement.querySelector("select");
select.value = select.options[2].value;
select.dispatchEvent(new Event("change"));
await fixture.whenStable();

expect(fixture.componentInstance.form.value.country).toBe("GE");
```

## 117: How do you test a checkbox?

Click it, or set `checked` and dispatch a `change` event.

```ts
const checkbox: HTMLInputElement = fixture.nativeElement.querySelector(
  "input[type=checkbox]",
);
checkbox.click();
await fixture.whenStable();
expect(fixture.componentInstance.form.value.terms).toBe(true);
```

`click()` is closer to real user behavior, since it toggles `checked` and fires the events.

## 118: How do you submit a form in a test?

Dispatch a `submit` event on the form, or click the submit button.

```ts
const form: HTMLFormElement = fixture.nativeElement.querySelector("form");
form.dispatchEvent(new Event("submit"));
await fixture.whenStable();

expect(saveSpy).toHaveBeenCalled();
```

Clicking the button also works and tests that the button is really a submit button inside the form.

## 119: What does ng test --watch do?

In watch mode, the runner stays open, watches your files and reruns tests when they change. It's the default when you run `ng test` locally.

Use `--no-watch` (or `--watch=false`) in CI, so the command runs once and exits with a pass or fail code.

## 120: How do you run Angular tests in CI?

Run the tests once, with coverage if you need it, and let the exit code fail the build.

```bash
npm ci
npx ng test --no-watch --coverage
```

With Vitest in Node, you don't need a browser installed. With Karma or Vitest browser mode, you need a headless browser like Chrome or Playwright's browsers.

## 121: What does a test report show?

It shows how many tests passed, failed or were skipped, the name of each failing test, the expected and actual values, and a stack trace pointing to the line.

Vitest and Karma can also write reports in other formats, like JUnit XML, that CI systems can show in their UI.

## 122: Why is a test that never fails useless?

A test is only useful if it fails when the code is broken. A test with a wrong assertion, a missing `await` or an `expect` that never runs will always pass.

A simple habit: break the code on purpose once and check that the test goes red.

## 123: How do you test a pure function used by a component?

Move it out of the component into its own file and test it as a plain function, with no TestBed at all.

```ts
export function fullName(u: { first: string; last: string }) {
  return `${u.first} ${u.last}`.trim();
}

it("joins names", () => {
  expect(fullName({ first: "Ana", last: "Lee" })).toBe("Ana Lee");
});
```

Plain functions are the fastest and simplest things to test.

## 124: What is the providedIn: 'root' setting's effect on tests?

A service with `providedIn: 'root'` is available in TestBed without adding it to `providers`. `TestBed.inject(MyService)` just works.

Because TestBed resets between tests, each test still gets a fresh root instance. You can override it with your own provider when you need a fake.

## 125: How do you test a component that shows a date with the DatePipe?

Use a fixed date in the test so the output is stable, and check the formatted text.

```ts
fixture.componentRef.setInput("createdAt", new Date(2026, 0, 15));
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("Jan 15, 2026");
```

Avoid `new Date()` without arguments in assertions, since the result changes every day. Also watch out for time zones in CI.

## 126: How do you test something that uses the current date?

Use fake timers and set the system time, so "now" is the same on every run.

```ts
beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(new Date("2026-01-15T10:00:00Z"));
});
afterEach(() => vi.useRealTimers());
```

In Jasmine, use `jasmine.clock().install()` and `jasmine.clock().mockDate(date)`.

## 127: What is a flaky test?

A flaky test sometimes passes and sometimes fails without any code change. Common causes are timing problems, shared state between tests, real dates and time zones, random data, and real network calls.

Flaky tests are harmful because people start ignoring red builds. Fix the cause instead of rerunning until it's green.

## 128: How do you test a component with content projection?

Use a test host component that puts content inside the component's tags.

```ts
@Component({
  imports: [CardComponent],
  template: '<app-card><p class="body">Hello</p></app-card>',
})
class HostComponent {}

it("projects content", async () => {
  const fixture = TestBed.createComponent(HostComponent);
  await fixture.whenStable();
  expect(
    fixture.nativeElement.querySelector("app-card .body").textContent,
  ).toBe("Hello");
});
```

## 129: How do you test a component's host binding?

Check the host element, which is `fixture.nativeElement` itself.

```ts
@Component({
  selector: "app-badge",
  template: "",
  host: { "[class.active]": "active()" },
})
class BadgeComponent {
  active = input(false);
}

fixture.componentRef.setInput("active", true);
await fixture.whenStable();
expect(fixture.nativeElement.classList).toContain("active");
```

## 130: How do you test a host listener?

Dispatch the event on the host element or on `window`/`document`, depending on what the listener targets.

```ts
// host: { '(window:resize)': 'onResize()' }
const spy = vi.spyOn(fixture.componentInstance, "onResize");
window.dispatchEvent(new Event("resize"));
expect(spy).toHaveBeenCalled();
```

## 131: How do you test a component that uses @ViewChild or viewChild()?

Render the template, then read the query result after the view is ready.

```ts
const fixture = TestBed.createComponent(SearchComponent);
await fixture.whenStable();

const input = fixture.componentInstance.searchInput();
expect(input?.nativeElement.tagName).toBe("INPUT");
```

For `viewChild()`, call the signal. For the older `@ViewChild` decorator, read the property after the first change detection.

## 132: How do you test that a method focuses an input?

Check `document.activeElement`. The fixture must be attached to the document, which TestBed does by default.

```ts
fixture.componentInstance.focusSearch();
expect(document.activeElement).toBe(
  fixture.nativeElement.querySelector("input"),
);
```

## 133: How do you add global setup code that runs before every spec file?

With the Vitest runner, use the `setupFiles` option of the `unit-test` builder in `angular.json`. For providers that every test needs, there is a `providersFile` option.

```json
"options": {
  "setupFiles": ["src/test-setup.ts"],
  "providersFile": "src/test-providers.ts"
}
```

In older Karma projects, this kind of code lived in `src/test.ts`.

## 134: What is test.ts in older Angular projects?

`src/test.ts` was the entry file for Karma tests. It initialized the test environment with `getTestBed().initTestEnvironment(...)` and used `require.context` to load all spec files.

New CLI builders handle this automatically, so most projects no longer have it. If you see it, the project uses the old webpack based Karma setup.

## 135: How do you check how many times a spy was called?

Use `toHaveBeenCalledTimes`.

```ts
expect(api.load).toHaveBeenCalledTimes(1);
```

This catches bugs like a component loading data twice because of a duplicate subscription or an effect that runs too often.

## 136: How do you check the arguments of a specific call?

In Vitest, use `toHaveBeenNthCalledWith` or read `mock.calls`. In Jasmine, use `calls.argsFor(index)`.

```ts
expect(log).toHaveBeenNthCalledWith(2, "second");
expect(log.mock.calls[0][0]).toBe("first"); // Vitest
expect(logSpy.calls.argsFor(0)).toEqual(["first"]); // Jasmine
```

## 137: What is expect.any() or jasmine.any() for?

They match any value of a given type, which is useful when you don't care about the exact value.

```ts
expect(api.save).toHaveBeenCalledWith(expect.any(Object), expect.any(Number)); // Vitest
expect(api.save).toHaveBeenCalledWith(jasmine.any(Object), jasmine.any(Number)); // Jasmine
```

For partial objects, use `expect.objectContaining({ id: 1 })` or `jasmine.objectContaining({ id: 1 })`.

## 138: How do you test a component that shows an error message from an HTTP call?

Fake the service to fail, then check the message in the DOM.

```ts
providers: [
  {
    provide: UserService,
    useValue: { load: () => throwError(() => new Error("fail")) },
  },
];

const fixture = TestBed.createComponent(UsersComponent);
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".error").textContent).toContain(
  "Could not load users",
);
```

## 139: Why should tests not call real APIs?

Real APIs make tests slow, flaky and dependent on network, data and other teams. A test might fail because the server is down, not because your code is wrong.

Use `HttpTestingController` or fake services in unit tests. Real backends belong in a few dedicated E2E or contract tests.

## 140: What is test data and how should you manage it?

Test data is the input you use in tests, like fake users or orders. Keep it small and focused on what the test needs.

A common trick is a small factory function with defaults you can override:

```ts
function makeUser(overrides: Partial<User> = {}): User {
  return { id: 1, name: "Ana", role: "user", ...overrides };
}

const admin = makeUser({ role: "admin" });
```

## 141: What is the benefit of keeping spec files next to the code?

When `user.service.spec.ts` sits next to `user.service.ts`, it's easy to find the tests, notice files without tests, and move or delete them together.

This is the default Angular CLI convention, and the test builder finds `*.spec.ts` files anywhere in the source folder.

## 142: How do you test a component that uses the i18n $localize function?

When the app uses Angular's built-in i18n, tests usually run with the source language, so `$localize` returns the original text. You need `@angular/localize/init` loaded, which the CLI adds to the test polyfills when localize is set up.

Then just check for the source language text in the DOM.

## 143: How do you test a component that emits through an output when a form is valid?

Fill the form, submit it and check the output.

```ts
const saved: unknown[] = [];
fixture.componentInstance.saved.subscribe((v) => saved.push(v));

fixture.componentInstance.form.setValue({ name: "Ana" });
fixture.nativeElement.querySelector("form").dispatchEvent(new Event("submit"));

expect(saved).toEqual([{ name: "Ana" }]);
```

Also test the case where the form is invalid and nothing is emitted.

## 144: How do you check an inline style in a test?

Read `style` from the DOM element, or `styles` from the debug element.

```ts
const bar: HTMLElement = fixture.nativeElement.querySelector(".progress");
expect(bar.style.width).toBe("40%");
```

jsdom doesn't compute layout, so you can read inline styles but not real sizes from CSS files.

## 145: What is the role of the polyfills option in test configuration?

It lists scripts loaded before your tests. In Zone.js based projects it usually includes `zone.js` and `zone.js/testing`, which are needed for `fakeAsync`, `waitForAsync` and Zone based change detection.

Zoneless projects don't need these polyfills. You might still add `@angular/localize/init` or other scripts your app needs.

## 146: How do you test a standalone component that imports other standalone components?

Import only the component under test. Its own `imports` (child components, pipes, directives) are pulled in automatically.

```ts
TestBed.configureTestingModule({ imports: [OrderPageComponent] });
```

You only add things to TestBed that the component gets through DI, like services or the router, which come from providers, not imports.

## 147: How do you test a component that was declared in an NgModule?

Older non-standalone components must be declared in the testing module, together with whatever the template needs.

```ts
TestBed.configureTestingModule({
  declarations: [LegacyListComponent],
  imports: [CommonModule, SharedModule],
});
```

This is the legacy way. Standalone components (the default since v19) just go in `imports`.

## 148: What is a matcher like toBeCloseTo for?

`toBeCloseTo` compares floating point numbers with some tolerance, because math like `0.1 + 0.2` isn't exactly `0.3`.

```ts
expect(0.1 + 0.2).toBeCloseTo(0.3);
expect(calcTax(19.99)).toBeCloseTo(3.6, 2);
```

The second argument is how many decimal places must match.

## 149: What does "should create" test actually catch?

It catches setup problems: a missing provider, a missing import in the component, a template that fails to compile, or a constructor that throws.

It doesn't check any behavior. If it's the only test in a spec file, the component has almost no real coverage.

## 150: How do you get started writing tests for an Angular app that has none?

Start with the code that matters most and is easiest to test:

1. Pure functions, pipes and validators
2. Services with business logic
3. Key components, testing what the user sees
4. A few E2E tests for the main flows, like login and checkout

Add a test every time you fix a bug, so the same bug can't come back without a failing test.

# Moderate Questions (151-300)

## 151: What are the main options of the @angular/build:unit-test builder?

Some options you'll use often:

- `runner`: `vitest` or `karma`
- `tsConfig`: usually `tsconfig.spec.json`
- `buildTarget`: which build config to compile tests with
- `include` / `exclude`: which spec files to run
- `setupFiles` and `providersFile`: global setup
- `coverage`, `coverageReporters`, `coverageThresholds`
- `browsers`: run in real browsers instead of jsdom
- `watch`, `reporters`, `runnerConfig`

Check `ng test --help` for the exact list in your version.

## 152: How does the Angular CLI run Vitest under the hood?

The `unit-test` builder first builds your spec files with the same esbuild based build system the app uses, so templates, styles and TypeScript are compiled the Angular way. Then it hands the built files to Vitest, which runs them in Node with jsdom or in a browser.

This is why you don't need Vite plugins for Angular when you use the CLI builder. It also means some Vitest features that depend on Vite's own transform, like `vi.mock` of a module path, may behave differently. Check the Angular docs for current limits.

## 153: How do you use your own Vitest config file with the Angular builder?

Set the `runnerConfig` option. With `true`, the builder looks for a `vitest-base.config.*` file in the project or workspace. You can also give a path.

```json
"test": {
  "builder": "@angular/build:unit-test",
  "options": { "runnerConfig": "vitest-base.config.ts" }
}
```

Some options are controlled by the builder (like the test files and build), so not every Vitest setting will take effect. Use it for things like reporters, pool settings or mock reset behavior.

## 154: How do you migrate an existing project from Karma to Vitest?

Roughly:

1. Install `vitest` and `jsdom` (or another DOM library).
2. Change the `test` builder to `@angular/build:unit-test` with `runner: "vitest"`.
3. Remove `karma.conf.js`, `src/test.ts` and Karma packages.
4. Update `tsconfig.spec.json` types from `jasmine` to `vitest/globals`.
5. Convert Jasmine specific code: `spyOn` to `vi.spyOn`, `jasmine.createSpyObj` to objects with `vi.fn()`, `and.returnValue` to `mockReturnValue`, `jasmine.clock()` to `vi.useFakeTimers()`.

The Angular CLI has an experimental schematic, `ng g @schematics/angular:refactor-jasmine-vitest`, that does a lot of step 5 for you. Check the "Migrating to Vitest" guide for your version.

## 155: Can you keep using Karma with the new unit-test builder?

Yes. Set `runner: "karma"` in the `@angular/build:unit-test` builder. It uses the new build system with Karma as the runner, so you can move off the old webpack based builder first and switch the runner later.

This is useful for large suites full of Jasmine code, where switching everything at once is too much work.

## 156: What is Vitest browser mode and when do you use it?

Browser mode runs your tests in a real browser (through Playwright or WebdriverIO) instead of Node with jsdom. With the Angular builder you turn it on with the `browsers` option.

```bash
npm i -D @vitest/browser-playwright playwright
ng test --browsers=chromium
```

Use it when tests depend on real browser behavior: layout, `ResizeObserver`, focus handling, CSS, or APIs jsdom doesn't support. It's slower than jsdom.

## 157: How do you set coverage thresholds?

With the Vitest runner, use the `coverageThresholds` option so the run fails if coverage drops below the limits.

```json
"options": {
  "coverageThresholds": {
    "statements": 80,
    "branches": 70,
    "functions": 80,
    "lines": 80
  }
}
```

In Karma projects, thresholds go in the `check` section of the coverage reporter config in `karma.conf.js`.

## 158: How do you exclude files from coverage?

Use the `coverageExclude` option in the builder (or the Vitest config), for example to skip generated code, `main.ts` or test helpers.

```json
"coverageExclude": ["src/main.ts", "src/**/*.mock.ts"]
```

Don't exclude real logic just to make the number look better.

## 159: Is 100% code coverage a good goal?

Usually not. Getting the last few percent often means writing tests that only exist to touch lines, which adds maintenance without catching bugs.

Coverage is a hint for finding untested code, not a quality score. Focus on testing important behavior, edge cases and bug fixes. Many teams pick a reasonable threshold like 70-80% and look at what's missing in changed files.

## 160: How do you test a functional route guard?

Functional guards use `inject()`, so call them inside `TestBed.runInInjectionContext`.

```ts
it("blocks logged out users", () => {
  TestBed.configureTestingModule({
    providers: [
      { provide: AuthService, useValue: { isLoggedIn: () => false } },
    ],
  });

  const result = TestBed.runInInjectionContext(() =>
    authGuard({} as ActivatedRouteSnapshot, {} as RouterStateSnapshot),
  );

  expect(result).toEqual(TestBed.inject(Router).parseUrl("/login"));
});
```

## 161: What does TestBed.runInInjectionContext do?

It runs a function inside the TestBed injector's context, so `inject()` calls inside it work.

```ts
const value = TestBed.runInInjectionContext(() => inject(API_URL));
```

You use it for functional guards, resolvers, interceptors, `inject` based factory functions and anything else that must call `inject()` outside a class constructor.

## 162: How do you test a guard through real routing?

Set up routes with the guard and navigate with `RouterTestingHarness`, then check where you ended up.

```ts
TestBed.configureTestingModule({
  providers: [
    { provide: AuthService, useValue: { isLoggedIn: () => false } },
    provideRouter([
      { path: "admin", component: AdminComponent, canActivate: [authGuard] },
      { path: "login", component: LoginComponent },
    ]),
  ],
});

const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/admin");
expect(TestBed.inject(Router).url).toBe("/login");
```

This tests the guard and the route config together.

## 163: How do you test a resolver?

Like a guard: call the resolver function in an injection context and check the returned value.

```ts
it("loads the product", async () => {
  TestBed.configureTestingModule({
    providers: [
      {
        provide: ProductService,
        useValue: { get: (id: string) => of({ id }) },
      },
    ],
  });

  const route = {
    paramMap: convertToParamMap({ id: "5" }),
  } as ActivatedRouteSnapshot;
  const result$ = TestBed.runInInjectionContext(() =>
    productResolver(route, {} as RouterStateSnapshot),
  ) as Observable<Product>;

  expect(await firstValueFrom(result$)).toEqual({ id: "5" });
});
```

## 164: How do you test a functional HTTP interceptor?

Register it with `withInterceptors`, make a request and check the request in `HttpTestingController`.

```ts
TestBed.configureTestingModule({
  providers: [
    { provide: AuthService, useValue: { token: () => "abc" } },
    provideHttpClient(withInterceptors([authInterceptor])),
    provideHttpClientTesting(),
  ],
});

TestBed.inject(HttpClient).get("/api/me").subscribe();
const req = TestBed.inject(HttpTestingController).expectOne("/api/me");
expect(req.request.headers.get("Authorization")).toBe("Bearer abc");
```

## 165: How do you test an interceptor that retries or handles errors?

Flush an error response and check what happens next: another request, a redirect, or a transformed error.

```ts
http.get("/api/data").subscribe({ error: (e) => (error = e) });

httpMock
  .expectOne("/api/data")
  .flush(null, { status: 401, statusText: "Unauthorized" });
expect(router.navigate).toHaveBeenCalledWith(["/login"]);
```

For a retry interceptor, expect the same URL again after the first error, and flush the second request with success.

## 166: How do you test a class based interceptor?

Register it with `withInterceptorsFromDi()` and the `HTTP_INTERCEPTORS` token, which is how older code wires them.

```ts
providers: [
  provideHttpClient(withInterceptorsFromDi()),
  { provide: HTTP_INTERCEPTORS, useClass: LoggingInterceptor, multi: true },
  provideHttpClientTesting(),
];
```

Class based interceptors are still supported, but functional interceptors are the recommended style today.

## 167: How do you match requests in HttpTestingController beyond the URL?

`expectOne` and `match` accept a URL, an object with `method` and `url`, or a function.

```ts
httpMock.expectOne({ method: "DELETE", url: "/api/users/1" });

httpMock.expectOne(
  (req) => req.url === "/api/search" && req.params.get("q") === "ng",
);

const reqs = httpMock.match("/api/items");
expect(reqs.length).toBe(2);
```

Use `expectNone` to make sure a request was not sent.

## 168: How do you test query params in an HTTP request?

Match with a function or check `req.request.params`.

```ts
service.search("angular", 2).subscribe();
const req = httpMock.expectOne((r) => r.url === "/api/search");
expect(req.request.params.get("q")).toBe("angular");
expect(req.request.params.get("page")).toBe("2");
```

A plain string in `expectOne` is compared with the full URL including params (`urlWithParams`), so `expectOne('/api/search')` won't match a request that has params. Use a function like above, or the full URL `'/api/search?q=angular&page=2'`.

## 169: How do you test httpResource?

`httpResource` sends its request through `HttpClient`, so you test it with `HttpTestingController`. Create the resource in an injection context, let Angular start the request, flush it, then wait for stability.

```ts
TestBed.configureTestingModule({
  providers: [provideHttpClient(), provideHttpClientTesting()],
});

const user = TestBed.runInInjectionContext(() =>
  httpResource<User>(() => "/api/user/1"),
);
TestBed.tick();

TestBed.inject(HttpTestingController).expectOne("/api/user/1").flush({ id: 1 });
await TestBed.inject(ApplicationRef).whenStable();

expect(user.value()).toEqual({ id: 1 });
```

## 170: What does TestBed.tick() do?

`TestBed.tick()` runs Angular's synchronization step: it flushes pending effects and runs change detection for the app, like what happens after a real event.

It was added in v20 and replaces `TestBed.flushEffects()`, which is deprecated. Use it when you need effects or resources to run before you check something.

## 171: How do you test an effect?

Create the effect in an injection context (usually through a service or component), change the signal it reads, then run `TestBed.tick()`.

```ts
it("saves the theme when it changes", () => {
  const storage = { set: vi.fn() };
  TestBed.configureTestingModule({
    providers: [{ provide: StorageService, useValue: storage }],
  });

  const settings = TestBed.inject(SettingsService); // creates the effect
  settings.theme.set("dark");
  TestBed.tick();

  expect(storage.set).toHaveBeenCalledWith("theme", "dark");
});
```

Effects don't run synchronously when a signal changes, so without `tick()` the spy isn't called yet.

## 172: How do you test a linkedSignal?

Change the source signal and check that the linked signal resets, and also check that you can still set it by hand.

```ts
const options = signal(["a", "b"]);
const selected = linkedSignal(() => options()[0]);

selected.set("b");
expect(selected()).toBe("b");

options.set(["x", "y"]);
expect(selected()).toBe("x");
```

Plain signal code like this doesn't need TestBed unless it uses `inject()`.

## 173: How do you test the resource() API?

Create the resource in an injection context with a fake loader, then wait for it to resolve.

```ts
const id = signal(1);
const res = TestBed.runInInjectionContext(() =>
  resource({
    params: () => ({ id: id() }),
    loader: async ({ params }) => ({ id: params.id, name: "Ana" }),
  }),
);

await TestBed.inject(ApplicationRef).whenStable();
expect(res.value()).toEqual({ id: 1, name: "Ana" });
```

Also test `isLoading()`, `error()` and what happens when `id` changes.

## 174: How do you test a component that uses toSignal?

`toSignal` subscribes to an observable inside an injection context. In a test, give the component a fake observable and check the rendered value.

```ts
const price$ = new BehaviorSubject(10);
providers: [{ provide: PriceService, useValue: { price$ } }];

await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("10");

price$.next(20);
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("20");
```

## 175: What does setInput do that direct assignment does not?

`fixture.componentRef.setInput('name', value)`:

- Works with signal inputs, which are read-only from outside
- Calls `ngOnChanges` with proper `SimpleChanges`
- Marks OnPush components for check
- Uses the input's public alias if it has one
- Runs input transforms

Assigning `component.name = 'x'` skips all of this and doesn't even work for `input()`.

## 176: How do you test input transforms?

Pass a raw value through `setInput` and check what the component sees.

```ts
@Component({ selector: "app-toggle", template: "" })
class ToggleComponent {
  disabled = input(false, { transform: booleanAttribute });
}

fixture.componentRef.setInput("disabled", "");
expect(fixture.componentInstance.disabled()).toBe(true);
```

## 177: How do you test a required signal input?

You must set it before Angular reads it, or Angular throws NG0950. Set it right after creating the component and before the first change detection.

```ts
const fixture = TestBed.createComponent(ProductCardComponent);
fixture.componentRef.setInput("product", { id: 1, name: "Pen" });
await fixture.whenStable();
```

A test that forgets this fails, which is what you want, since the real parent must also pass it.

## 178: How do you test model() two-way binding?

Use a host component with `[(value)]`, or set the input and listen to the `valueChange` output.

```ts
@Component({
  imports: [RatingComponent],
  template: '<app-rating [(value)]="rating" />',
})
class HostComponent {
  rating = signal(2);
}

const fixture = TestBed.createComponent(HostComponent);
await fixture.whenStable();
fixture.nativeElement.querySelectorAll("button")[4].click();
expect(fixture.componentInstance.rating()).toBe(5);
```

## 179: What are binding helpers like inputBinding for in TestBed.createComponent?

Since v20, `TestBed.createComponent` accepts a `bindings` option. You can bind inputs to signals and listen to outputs without writing a host component.

```ts
import { inputBinding, outputBinding, signal } from "@angular/core";

const name = signal("Ana");
const clicks: string[] = [];

const fixture = TestBed.createComponent(GreetingComponent, {
  bindings: [
    inputBinding("name", name),
    outputBinding<string>("greeted", (v) => clicks.push(v)),
  ],
});

name.set("Bo");
await fixture.whenStable();
```

There's also `twoWayBinding` for `model()` inputs.

## 180: When should you use a host component instead of setInput?

Use a host component when the test is about how the component is used in a template:

- Content projection
- Several inputs changing together through real bindings
- Directives that need a host element
- Structural directives or template references
- Checking how outputs update parent state

For simple input and output tests, `setInput` or binding helpers are shorter.

## 181: How do you override a provider for a single test?

Call `TestBed.overrideProvider` before the component or service is created.

```ts
it("shows admin menu for admins", async () => {
  TestBed.overrideProvider(AuthService, { useValue: { role: () => "admin" } });
  const fixture = TestBed.createComponent(MenuComponent);
  await fixture.whenStable();
  expect(fixture.nativeElement.querySelector(".admin")).not.toBeNull();
});
```

After the first `createComponent` or `inject`, TestBed is locked and override calls throw.

## 182: How do you override a provider declared on a component?

Providers in a component's `providers` array aren't replaced by TestBed providers. Use `overrideComponent` with `set` or `add`.

```ts
TestBed.overrideComponent(CheckoutComponent, {
  set: { providers: [{ provide: CartStore, useValue: fakeStore }] },
});
```

Then get the fake from the component's injector: `fixture.debugElement.injector.get(CartStore)`.

## 183: What is the difference between set, add and remove in overrideComponent?

- `set` replaces the metadata field fully, for example the whole `providers` or `imports` array.
- `add` adds items to the existing array.
- `remove` removes specific items.

```ts
TestBed.overrideComponent(PageComponent, {
  remove: { imports: [HeavyChartComponent] },
  add: { imports: [ChartStubComponent] },
});
```

## 184: How do you override a component's template in a test?

Use `TestBed.overrideTemplate` or `overrideComponent` with `set: { template }`.

```ts
TestBed.overrideTemplate(BigComponent, "<span>{{ title() }}</span>");
```

This is rarely a good idea, because then you're not testing the real template. It can help when testing logic in a component whose template pulls in something you can't load in tests.

## 185: Why does TestBed throw "Cannot override ... after TestBed has been instantiated"?

TestBed compiles the testing module the first time you call `createComponent` or `inject`. After that, its config is fixed. Calling `overrideProvider`, `overrideComponent` or `configureTestingModule` afterwards throws.

Move overrides above any `inject` or `createComponent` call, including ones hidden in `beforeEach`.

## 186: How do you get a service from a component's own injector?

Use the debug element's injector. This returns the component level instance if the component provides the service itself.

```ts
const store = fixture.debugElement.injector.get(CartStore);
```

`TestBed.inject(CartStore)` would return the root instance instead, which is a different object.

## 187: How do you test a component that uses a component level store?

Get the store from the component's injector and check its state, or replace it with `overrideComponent`.

```ts
const fixture = TestBed.createComponent(TodoPageComponent);
const store = fixture.debugElement.injector.get(TodoStore);

store.add("Write tests");
await fixture.whenStable();
expect(fixture.nativeElement.querySelectorAll("li").length).toBe(1);
```

## 188: How do you test InjectionTokens?

Provide a value for the token in TestBed and check that code uses it.

```ts
export const API_URL = new InjectionToken<string>("API_URL");

TestBed.configureTestingModule({
  providers: [{ provide: API_URL, useValue: "https://test.local" }],
});

service.load().subscribe();
httpMock.expectOne("https://test.local/items");
```

If the token has a `factory`, you can also test the default value by not providing it.

## 189: How do you test a factory provider?

Inject the token and check the created value. Override its dependencies to test different branches.

```ts
providers: [
  { provide: ENV, useValue: "prod" },
  {
    provide: Logger,
    useFactory: () =>
      inject(ENV) === "prod" ? new SilentLogger() : new ConsoleLogger(),
  },
];

expect(TestBed.inject(Logger)).toBeInstanceOf(SilentLogger);
```

## 190: How do you test a component that uses DOCUMENT or window?

Inject `DOCUMENT` in the code instead of using the global, then provide a fake if needed. For `window`, wrap it in an injection token.

```ts
export const WINDOW = new InjectionToken<Window>("WINDOW", {
  factory: () => inject(DOCUMENT).defaultView!,
});

providers: [{ provide: WINDOW, useValue: { innerWidth: 500 } as Window }];
```

This makes the code work in SSR too, not just in tests.

## 191: What are component harnesses?

Component harnesses are classes from the Angular CDK (`@angular/cdk/testing`) that give tests a clean API to interact with a component, like `await button.click()` or `await input.setValue('x')`.

They hide the DOM details, so when the component's internal markup changes, only the harness has to change, not every test. Angular Material ships harnesses for its components.

## 192: How do you use a Material component harness?

Create a loader from the fixture and get the harness.

```ts
import { TestbedHarnessEnvironment } from "@angular/cdk/testing/testbed";
import { MatButtonHarness } from "@angular/material/button/testing";

const loader = TestbedHarnessEnvironment.loader(fixture);
const save = await loader.getHarness(MatButtonHarness.with({ text: "Save" }));

expect(await save.isDisabled()).toBe(false);
await save.click();
```

Harness methods are async, and they run change detection and wait for stability for you.

## 193: What is the difference between getHarness and getAllHarnesses?

`getHarness` returns the first matching harness and throws if none is found. `getAllHarnesses` returns an array, which can be empty.

```ts
const rows = await loader.getAllHarnesses(MatRowHarness);
expect(rows.length).toBe(3);
```

There's also `getHarnessOrNull` and `hasHarness` when the element might not exist.

## 194: How do you test a MatDialog opened by a component?

Use the dialog harness with a document root loader, since dialogs render outside the component.

```ts
import { MatDialogHarness } from "@angular/material/dialog/testing";

const rootLoader = TestbedHarnessEnvironment.documentRootLoader(fixture);
fixture.nativeElement.querySelector("button.delete").click();

const dialogs = await rootLoader.getAllHarnesses(MatDialogHarness);
expect(dialogs.length).toBe(1);
```

For a unit test of the component alone, you can also fake `MatDialog` and check that `open` was called with the right component and data.

## 195: How do you test a component that opens a dialog and uses its result?

Fake `MatDialog` so `open` returns an object whose `afterClosed()` emits the result you want.

```ts
const dialog = {
  open: vi.fn().mockReturnValue({ afterClosed: () => of(true) }),
};
providers: [{ provide: MatDialog, useValue: dialog }];

fixture.componentInstance.delete(5);
expect(dialog.open).toHaveBeenCalled();
expect(api.delete).toHaveBeenCalledWith(5);
```

Test the "cancelled" case too by returning `of(false)`.

## 196: How do you test a component that uses a CDK overlay?

Overlay content is attached to an overlay container at the end of `document.body`, not inside the fixture. Query the document instead of the fixture, or use `documentRootLoader` with harnesses.

```ts
fixture.nativeElement.querySelector(".open-menu").click();
await fixture.whenStable();
expect(
  document.querySelector(".cdk-overlay-container .menu-item"),
).not.toBeNull();
```

TestBed cleans up overlays when the module is torn down.

## 197: What is @testing-library/angular?

Angular Testing Library is a community library built on DOM Testing Library. It lets you render components and query them the way users find things: by role, label or text.

```ts
import { render, screen } from "@testing-library/angular";
import userEvent from "@testing-library/user-event";

it("increments", async () => {
  await render(CounterComponent);
  await userEvent.click(screen.getByRole("button", { name: "Add" }));
  expect(screen.getByText("Count: 1")).toBeTruthy();
});
```

It wraps TestBed, so you can still pass `providers` and `inputs`.

## 198: Why do people prefer role based queries?

Queries like `getByRole('button', { name: 'Save' })` find elements the same way users and screen readers do. If the button is missing an accessible name, the test fails, which also checks basic accessibility.

They are also less tied to CSS classes and markup, so tests break less often after styling changes.

## 199: What is the difference between getBy, queryBy and findBy in Testing Library?

- `getBy...` returns the element or throws if not found.
- `queryBy...` returns the element or `null`, which is good for checking something is absent.
- `findBy...` returns a promise and waits until the element appears, for async UI.

Each has an `All` version that returns arrays.

## 200: What is userEvent and how is it different from fireEvent?

`fireEvent` dispatches a single DOM event. `userEvent` simulates what a real user does, which is usually several events in order. Typing fires keydown, keypress, input and keyup for each character, and a click includes pointer and mouse events and focus.

Use `userEvent` by default. It catches bugs that a single synthetic event can hide.

## 201: How do you pass inputs and providers with Testing Library's render?

`render` takes the component and an options object.

```ts
await render(UserCardComponent, {
  inputs: { user: { name: "Ana" } },
  on: { selected: (u: User) => selectedSpy(u) },
  providers: [{ provide: UserService, useValue: fakeUserService }],
});
```

The exact option names (`inputs`, `on`, `componentProperties`) depend on the library version, so check its docs. `inputs` and `on` are the current ones for signal inputs and outputs.

## 202: What are ng-mocks and Spectator?

Both are community libraries that reduce TestBed boilerplate.

- **ng-mocks** creates mocks of components, directives, pipes, services and modules automatically (`MockComponent`, `MockProvider`, `MockBuilder`, `MockRender`). It's popular for shallow tests.
- **Spectator** wraps TestBed with a simpler API (`createComponentFactory`, `spectator.click()`, `spectator.query()`) and helpers for services, directives and HTTP.

They're optional. Plain TestBed with harnesses or Testing Library covers most needs.

## 203: How do you mock a child component with ng-mocks?

Use `MockComponent` or `MockBuilder`, which keep the selector, inputs and outputs but render nothing.

```ts
import { MockBuilder, MockRender, ngMocks } from "ng-mocks";

beforeEach(() => MockBuilder(DashboardComponent).mock(ChartComponent));

it("passes data to the chart", () => {
  MockRender(DashboardComponent);
  const chart = ngMocks.findInstance(ChartComponent);
  expect(chart.data()).toEqual([1, 2, 3]);
});
```

## 204: How do you test a component with OnPush change detection?

With `setInput` or signal updates, OnPush works fine. The common mistake is changing a plain field on `componentInstance` and calling `detectChanges()`. OnPush ignores it because nothing marked the component dirty.

Fix it by using `setInput`, signals, or user events. As a last resort, use `fixture.componentRef.injector.get(ChangeDetectorRef).markForCheck()`.

## 205: What does provideZonelessChangeDetection do in tests?

It makes TestBed run without Zone.js, the same way a zoneless app runs. Since v21, new apps are zoneless by default, and TestBed is zoneless when Zone.js isn't loaded.

```ts
TestBed.configureTestingModule({
  providers: [provideZonelessChangeDetection()],
});
```

You add it explicitly when Zone.js is still loaded (for example for old tests) but you want a test to run zoneless.

## 206: Why should tests use the same change detection mode as the app?

If the app is zoneless but the tests run with Zone.js, Zone triggers change detection after every async task and can hide bugs. For example, a component that changes a plain field in a `setTimeout` works in the test but never updates in the real app.

Running tests zoneless catches those cases, because only signals, inputs, events and `markForCheck` will update the view, like in production.

## 207: What is ExpressionChangedAfterItHasBeenCheckedError and why do you see it in tests?

Angular checks bindings twice in dev mode (and in tests). If a value changes between the first and second check, it throws this error. It usually means code changes state during change detection, for example in `ngAfterViewInit` or a getter that returns new values.

In zoneless tests TestBed also throws it when a template value changed without Angular being notified. Fix the root cause, for example by using signals, instead of hiding it.

## 208: What are fakeAsync and tick?

`fakeAsync` runs a test in a special Zone where time is fake. `tick(ms)` moves the fake clock forward and runs timers that are due. `flush()` runs all pending timers, and `flushMicrotasks()` runs pending promises.

```ts
it("debounces", fakeAsync(() => {
  component.search("a");
  tick(300);
  expect(api.search).toHaveBeenCalledWith("a");
}));
```

They need Zone.js (`zone.js/testing`), so they're a legacy tool in zoneless projects.

## 209: How do you replace fakeAsync in zoneless or Vitest tests?

Use the test framework's fake timers.

```ts
it("debounces search", async () => {
  vi.useFakeTimers();
  component.query.set("ng");
  await vi.advanceTimersByTimeAsync(300);
  expect(api.search).toHaveBeenCalledWith("ng");
  vi.useRealTimers();
});
```

The async version (`advanceTimersByTimeAsync`) also lets promises run between timers. In Jasmine, use `jasmine.clock()`.

## 210: What is waitForAsync?

`waitForAsync` (formerly `async`) wraps a test in a Zone that waits for all async tasks started in the test to finish before the test ends. It was used in old `beforeEach` blocks around `compileComponents()`.

It's legacy now. Use a normal `async` function with `await` instead. It also needs Zone.js.

## 211: How do you test code that uses setTimeout?

Use fake timers and move time forward.

```ts
it("hides the toast after 3s", async () => {
  vi.useFakeTimers();
  toast.show("Saved");
  expect(toast.visible()).toBe(true);

  await vi.advanceTimersByTimeAsync(3000);
  expect(toast.visible()).toBe(false);
  vi.useRealTimers();
});
```

Without fake timers you would have to really wait 3 seconds, which slows the suite down.

## 212: How do you test an RxJS debounceTime in a component?

RxJS uses `setTimeout` under the hood, so fake timers work.

```ts
vi.useFakeTimers();
input.value = "ang";
input.dispatchEvent(new Event("input"));

await vi.advanceTimersByTimeAsync(299);
expect(api.search).not.toHaveBeenCalled();

await vi.advanceTimersByTimeAsync(1);
expect(api.search).toHaveBeenCalledWith("ang");
```

Testing just before and just after the debounce time proves the delay is right.

## 213: What is marble testing?

Marble testing describes observables as strings over time, like `'-a--b|'`. RxJS's `TestScheduler` runs them in virtual time, so you can test complex timing without waiting.

```ts
import { TestScheduler } from "rxjs/testing";

const scheduler = new TestScheduler((actual, expected) =>
  expect(actual).toEqual(expected),
);

scheduler.run(({ cold, expectObservable }) => {
  const source = cold("a-b-c|");
  expectObservable(source.pipe(map((x) => x.toUpperCase()))).toBe("A-B-C|");
});
```

## 214: When is marble testing worth it?

It's worth it for RxJS heavy code with timing: debounce, throttle, retry with delay, `switchMap` cancellation or race conditions in effects. It makes those cases precise and fast.

For simple streams like "service returns users", `of()` plus a subscribe or `firstValueFrom` is easier to read.

## 215: How do you test switchMap cancellation?

Make two requests and check that the first one is cancelled when the second starts.

```ts
component.search("a");
component.search("ab");

const reqs = httpMock.match((r) => r.url === "/api/search");
expect(reqs[0].cancelled).toBe(true);
reqs[1].flush(["ab result"]);
```

`TestRequest.cancelled` tells you if the subscriber unsubscribed before the response came.

## 216: How do you test that a subscription is cleaned up on destroy?

Use a `Subject` and check it has no observers after destroy, or check that later emissions don't affect the component.

```ts
const events$ = new Subject<string>();
// provide a fake that exposes events$
const fixture = TestBed.createComponent(FeedComponent);
await fixture.whenStable();
expect(events$.observed).toBe(true);

fixture.destroy();
expect(events$.observed).toBe(false);
```

## 217: How do you test a service that wraps a third party library?

Don't test the library itself. Fake it at the boundary, ideally behind an injection token, and test that your service calls it correctly and handles its results.

```ts
export const MAPS_SDK = new InjectionToken<MapsSdk>("MAPS_SDK");

providers: [
  {
    provide: MAPS_SDK,
    useValue: { geocode: vi.fn().mockResolvedValue({ lat: 1, lng: 2 }) },
  },
];
```

Then a small number of integration or E2E tests check that the real library works with your code.

## 218: How do you test a component that uses a Web API missing in jsdom?

jsdom doesn't implement things like `IntersectionObserver`, `ResizeObserver` or `matchMedia`. You can:

- Wrap the API in a service and fake the service
- Add a small stub in a setup file
- Run those tests in Vitest browser mode

```ts
// test-setup.ts
globalThis.ResizeObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
};
```

## 219: How do you mock window.matchMedia in tests?

Stub it in the test or in a setup file, returning whatever the component needs.

```ts
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: vi.fn().mockImplementation((query: string) => ({
    matches: query.includes("dark"),
    media: query,
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
  })),
});
```

The CDK `BreakpointObserver` uses `matchMedia`, so this also affects components that use it.

## 220: How do you test a component that uses BreakpointObserver?

Fake `BreakpointObserver` and control what it emits.

```ts
const state$ = new BehaviorSubject<BreakpointState>({
  matches: true,
  breakpoints: {},
});
providers: [
  { provide: BreakpointObserver, useValue: { observe: () => state$ } },
];

await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".mobile-menu")).not.toBeNull();

state$.next({ matches: false, breakpoints: {} });
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".mobile-menu")).toBeNull();
```

## 221: How do you test @defer blocks?

By default TestBed renders defer blocks with "playthrough" behavior. You can switch to manual control and move a block through its states.

```ts
import { DeferBlockBehavior, DeferBlockState } from "@angular/core/testing";

TestBed.configureTestingModule({
  deferBlockBehavior: DeferBlockBehavior.Manual,
});

const fixture = TestBed.createComponent(ProductPageComponent);
const [reviews] = await fixture.getDeferBlocks();

await reviews.render(DeferBlockState.Placeholder);
expect(fixture.nativeElement.textContent).toContain("Loading reviews");

await reviews.render(DeferBlockState.Complete);
expect(fixture.nativeElement.querySelector("app-reviews")).not.toBeNull();
```

## 222: What is the difference between Manual and Playthrough defer behavior?

- **Playthrough** (default): blocks behave like in the real app. Triggers fire, dependencies load, and the block moves from placeholder to loading to complete on its own.
- **Manual**: blocks stay where they are until the test calls `render(DeferBlockState.X)`.

Manual is good for checking each state (placeholder, loading, error). Playthrough is good for testing the real trigger flow.

## 223: How do you test a pipe that depends on a service?

Create it inside an injection context so its `inject()` calls work, or test it through a host component.

```ts
TestBed.configureTestingModule({
  providers: [{ provide: CurrencyService, useValue: { rate: () => 2 } }],
});

const pipe = TestBed.runInInjectionContext(() => new ConvertPipe());
expect(pipe.transform(10)).toBe(20);
```

## 224: How do you test an impure pipe?

An impure pipe runs on every change detection, so test it through a host template and check that the output updates when the data changes in place.

```ts
@Component({
  imports: [FilterActivePipe],
  template: "{{ (items | filterActive).length }}",
})
class HostComponent {
  items = [{ active: true }];
}

fixture.componentInstance.items.push({ active: true });
fixture.detectChanges();
expect(fixture.nativeElement.textContent).toBe("2");
```

`detectChanges()` is used here on purpose: the array was changed in place, so nothing notified Angular.

## 225: How do you test a structural directive?

Use a host component with an `ng-template` or the `*` syntax, change the condition, and check the DOM.

```ts
@Component({
  imports: [IfRoleDirective],
  template: "<button *appIfRole=\"'admin'\">Delete</button>",
})
class HostComponent {}

providers: [{ provide: AuthService, useValue: { role: signal("user") } }];

await fixture.whenStable();
expect(fixture.nativeElement.querySelector("button")).toBeNull();
```

Then change the role to `admin`, wait for stability, and expect the button to exist.

## 226: How do you test a directive's inputs and outputs?

Bind them in a host component and check the effect and emitted values.

```ts
@Component({
  imports: [ClickOutsideDirective],
  template: '<div (appClickOutside)="closed = closed + 1">menu</div>',
})
class HostComponent {
  closed = 0;
}

document.body.click();
expect(fixture.componentInstance.closed).toBe(1);
```

## 227: How do you get a directive instance from the DOM in a test?

Query by directive and read it from the element's injector.

```ts
const de = fixture.debugElement.query(By.directive(TooltipDirective));
const tooltip = de.injector.get(TooltipDirective);
expect(tooltip.text()).toBe("Help");
```

## 228: How do you test a ControlValueAccessor?

Test both directions with a host component and a `FormControl`:

1. Set the control value and check the component shows it (`writeValue`).
2. Interact with the component and check the control value changes (`onChange`).
3. Disable the control and check the component is disabled (`setDisabledState`).

```ts
@Component({
  imports: [ReactiveFormsModule, StarRatingComponent],
  template: '<app-star-rating [formControl]="ctrl" />',
})
class HostComponent {
  ctrl = new FormControl(3);
}

fixture.componentInstance.ctrl.setValue(5);
await fixture.whenStable();
expect(fixture.nativeElement.querySelectorAll(".star.filled").length).toBe(5);
```

## 229: How do you test an async validator?

Return a promise or observable from a fake service, set the value, wait, and check the control's status and errors.

```ts
const ctrl = new FormControl("ana", {
  asyncValidators: [usernameTaken(fakeApi)],
});
expect(ctrl.status).toBe("PENDING");

await firstValueFrom(ctrl.statusChanges.pipe(filter((s) => s !== "PENDING")));
expect(ctrl.hasError("taken")).toBe(true);
```

If the validator uses a debounce, use fake timers.

## 230: How do you test a cross-field validator?

Apply it to a `FormGroup` and check the group's errors.

```ts
const form = new FormGroup(
  { password: new FormControl("a1"), confirm: new FormControl("b2") },
  { validators: matchPasswords },
);

expect(form.hasError("mismatch")).toBe(true);
form.controls.confirm.setValue("a1");
expect(form.valid).toBe(true);
```

## 231: How do you test that validation messages appear only after touch?

Check the DOM before and after blurring the field.

```ts
const input: HTMLInputElement = fixture.nativeElement.querySelector("#email");
expect(fixture.nativeElement.querySelector(".error")).toBeNull();

input.dispatchEvent(new Event("blur"));
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".error").textContent).toContain(
  "required",
);
```

`blur` marks the control as touched for reactive and template-driven forms.

## 232: How do you test a FormArray in a component?

Click the add and remove buttons and check the array length and rendered rows.

```ts
fixture.nativeElement.querySelector(".add-phone").click();
fixture.nativeElement.querySelector(".add-phone").click();
await fixture.whenStable();

expect(fixture.componentInstance.form.controls.phones.length).toBe(2);
expect(fixture.nativeElement.querySelectorAll(".phone-row").length).toBe(2);
```

## 233: How do you test signal forms?

Signal forms (`@angular/forms/signals`) are newer and still marked experimental in recent versions. The model is a signal, so you can set it and read field state directly, and also test through the template with `[field]` bindings.

The general approach is the same as other forms: set values, check validity and errors, and check the DOM. Check the current API names in the Angular docs for your version, since they may still change.

## 234: How do you test a component that uses NgRx Store?

Use `provideMockStore` with an initial state, and override selectors when you need specific values.

```ts
import { provideMockStore, MockStore } from "@ngrx/store/testing";

TestBed.configureTestingModule({
  imports: [CartBadgeComponent],
  providers: [provideMockStore({ initialState: { cart: { items: [] } } })],
});

const store = TestBed.inject(MockStore);
store.overrideSelector(selectCartCount, 3);
store.refreshState();
```

Check dispatched actions with a spy on `store.dispatch`.

## 235: How do you test NgRx reducers and selectors?

Reducers and selectors are pure functions, so test them without TestBed.

```ts
it("adds an item", () => {
  const state = cartReducer(initialState, addItem({ id: 1 }));
  expect(state.items).toEqual([{ id: 1 }]);
});

it("counts items", () => {
  expect(selectCartCount.projector([{ id: 1 }, { id: 2 }])).toBe(2);
});
```

`projector` lets you test the selector's logic without building the whole state.

## 236: How do you test NgRx effects?

Provide the effect with `provideMockActions` and a fake service, then subscribe to the effect.

```ts
let actions$: Observable<Action>;

TestBed.configureTestingModule({
  providers: [
    UserEffects,
    provideMockActions(() => actions$),
    { provide: UserApi, useValue: { load: () => of([{ id: 1 }]) } },
  ],
});

actions$ = of(loadUsers());
const effects = TestBed.inject(UserEffects);
const result = await firstValueFrom(effects.load$);
expect(result).toEqual(loadUsersSuccess({ users: [{ id: 1 }] }));
```

Marble tests are common for effects with timing.

## 237: How do you test an NgRx SignalStore?

Provide the store in TestBed, call its methods and read its signals.

```ts
TestBed.configureTestingModule({
  providers: [
    TodoStore,
    { provide: TodoApi, useValue: { load: () => of([{ id: 1, title: "A" }]) } },
  ],
});

const store = TestBed.inject(TodoStore);
store.loadAll();
expect(store.todos()).toEqual([{ id: 1, title: "A" }]);
```

For stores with `rxMethod` and debouncing, use fake timers. `@ngrx/signals/testing` also has helpers like `unprotected` for setting state directly in tests.

## 238: How do you test a service that uses a BehaviorSubject for state?

Call the methods and read the current value or subscribe.

```ts
const store = TestBed.inject(AuthStore);
store.login({ name: "Ana" });

expect(await firstValueFrom(store.user$)).toEqual({ name: "Ana" });
```

Because `BehaviorSubject` replays the latest value, `firstValueFrom` gets it right away.

## 239: How do you test that a component calls a service with the right data?

Spy on the service and check the arguments after the user action.

```ts
const api = { save: vi.fn().mockReturnValue(of({})) };
providers: [{ provide: ProfileApi, useValue: api }];

fixture.componentInstance.form.setValue({ name: "Ana", age: 30 });
fixture.nativeElement.querySelector("form").dispatchEvent(new Event("submit"));

expect(api.save).toHaveBeenCalledWith({ name: "Ana", age: 30 });
```

## 240: How do you type fake services safely in TypeScript?

Use `Partial<T>` or `Pick<T, ...>` and cast only once, so you get type checking on the parts you implement.

```ts
const fakeUsers: Pick<UserService, "getAll" | "getById"> = {
  getAll: vi.fn(() => of([])),
  getById: vi.fn(() => of(undefined)),
};

providers: [{ provide: UserService, useValue: fakeUsers }];
```

If the real method signature changes, the fake stops compiling, which is better than a silent mismatch.

## 241: What are Vitest's vi.mocked and Mocked types for?

`vi.mocked(fn)` tells TypeScript that a function is a mock, so you can call `mockReturnValue` without casting. `Mocked<T>` types a whole object of mocks.

```ts
import type { Mocked } from "vitest";

const api = { load: vi.fn() } as unknown as Mocked<UserApi>;
api.load.mockReturnValue(of([]));
```

## 242: Should you use vi.mock to mock modules in Angular tests?

Prefer DI. Angular's dependency injection already lets you swap any service or token for a fake, and it works the same in Vitest and Karma.

Module mocking with `vi.mock` replaces imports at the module level. It can be handy for plain utility modules, but with the Angular CLI builder it may not work the same as in a plain Vite project, because the CLI builds the code first. Check the Angular docs for current support before relying on it.

## 243: How do you test a component that uses the Title or Meta service?

Inject the real services and check what they set, since they work in jsdom.

```ts
const fixture = TestBed.createComponent(ArticleComponent);
fixture.componentRef.setInput("article", { title: "Hello" });
await fixture.whenStable();

expect(TestBed.inject(Title).getTitle()).toBe("Hello | Blog");
```

If the title comes from the route `title` property, test it through `RouterTestingHarness` and a custom `TitleStrategy`.

## 244: How do you test a custom TitleStrategy?

Navigate to a route with a `title` and check `document.title` or the `Title` service.

```ts
TestBed.configureTestingModule({
  providers: [
    provideRouter([
      { path: "about", title: "About", component: AboutComponent },
    ]),
    { provide: TitleStrategy, useClass: AppTitleStrategy },
  ],
});

const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/about");
expect(TestBed.inject(Title).getTitle()).toBe("About | My App");
```

## 245: How do you test lazy loaded routes?

`provideRouter` with `loadComponent` or `loadChildren` works in TestBed. Navigate and wait, and the router loads the lazy code.

```ts
TestBed.configureTestingModule({
  providers: [
    provideRouter([
      {
        path: "admin",
        loadComponent: () =>
          import("./admin.component").then((m) => m.AdminComponent),
      },
    ]),
  ],
});

const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/admin");
expect(harness.routeNativeElement?.querySelector("h1")?.textContent).toBe(
  "Admin",
);
```

## 246: How do you test withComponentInputBinding?

Add the feature to `provideRouter` and check that route params end up in inputs.

```ts
providers: [
  provideRouter(
    [{ path: "users/:id", component: UserComponent }],
    withComponentInputBinding(),
  ),
];

const harness = await RouterTestingHarness.create();
const user = await harness.navigateByUrl("/users/42", UserComponent);
expect(user.id()).toBe("42");
```

## 247: What does RouterTestingHarness.navigateByUrl return?

It navigates and returns the activated component instance. If you pass the expected component type as the second argument, it checks that the routed component is that type and returns it typed.

The harness also gives you `routeNativeElement` and `routeDebugElement` for checking the rendered DOM, and `detectChanges()` and `fixture` for more control.

## 248: How do you test a canDeactivate guard?

Call the guard with a fake component and check the result.

```ts
it("asks before leaving with unsaved changes", () => {
  const component = { hasUnsavedChanges: () => true } as EditComponent;
  vi.spyOn(window, "confirm").mockReturnValue(false);

  const result = TestBed.runInInjectionContext(() =>
    unsavedChangesGuard(
      component,
      {} as ActivatedRouteSnapshot,
      {} as RouterStateSnapshot,
      {} as RouterStateSnapshot,
    ),
  );

  expect(result).toBe(false);
});
```

## 249: How do you test the Location service?

Use `provideLocationMocks()`, which gives a `SpyLocation`. Then you can check the current path and simulate back navigation.

```ts
import { Location } from "@angular/common";
import { provideLocationMocks } from "@angular/common/testing";

providers: [provideRouter(routes), provideLocationMocks()];

const location = TestBed.inject(Location);
await harness.navigateByUrl("/a");
await harness.navigateByUrl("/b");
location.back();
await harness.fixture.whenStable();
expect(location.path()).toBe("/a");
```

## 250: How do you test a component that listens to router events?

Do a real navigation and check the effect, rather than faking `Router.events`.

```ts
const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/products");
expect(TestBed.inject(Analytics).track).toHaveBeenCalledWith(
  "page_view",
  "/products",
);
```

Faking the router's events stream is possible, but the real router is easy to set up and catches more bugs.

## 251: How do you test a component that uses an ElementRef directly?

Check the effect on the real DOM. Don't fake `ElementRef`, because the component gets the real host element in the test.

```ts
@Component({ selector: "app-autofocus", template: "<input />" })
class AutofocusComponent {
  private el = inject(ElementRef<HTMLElement>);
  ngAfterViewInit() {
    this.el.nativeElement.querySelector("input")?.focus();
  }
}

await fixture.whenStable();
expect(document.activeElement?.tagName).toBe("INPUT");
```

## 252: How do you test afterNextRender or afterEveryRender hooks?

These hooks run after Angular renders, so wait for the fixture to be stable and then check their effect.

```ts
const fixture = TestBed.createComponent(ChartComponent);
await fixture.whenStable();
expect(fixture.componentInstance.chartReady()).toBe(true);
```

They don't run on the server, so if you test SSR behavior, make sure the code works without them. `afterRender` was renamed to `afterEveryRender` in v20.

## 253: How do you test a component that uses Renderer2?

Test the outcome in the DOM. Renderer2 changes real elements in the test, so checking classes, attributes and children is enough.

```ts
fixture.componentInstance.addBadge("New");
expect(fixture.nativeElement.querySelector(".badge").textContent).toBe("New");
```

Spying on Renderer2 methods ties the test to implementation details and isn't needed.

## 254: How do you test dynamic components created with ViewContainerRef?

Trigger the code that creates them and check that the component appears in the DOM.

```ts
fixture.componentInstance.open(AlertComponent, { message: "Hi" });
await fixture.whenStable();
expect(fixture.nativeElement.querySelector("app-alert").textContent).toContain(
  "Hi",
);
```

If inputs are set with `ComponentRef.setInput`, also test that later input changes update the view.

## 255: How do you test NgComponentOutlet usage?

Render the host with a component type and inputs, and check the result. Then change the type and check that the view switches.

```ts
fixture.componentInstance.widget.set(ChartWidgetComponent);
await fixture.whenStable();
expect(fixture.nativeElement.querySelector("app-chart-widget")).not.toBeNull();
```

## 256: How do you test a component that uses createComponent outside a view?

When code uses `createComponent()` with `ApplicationRef.attachView()` (for example a toast service), the component lands in `document.body`, not inside a fixture. Query the document and remember to clean up.

```ts
const toast = TestBed.inject(ToastService);
toast.show("Saved");
TestBed.tick();

expect(document.body.querySelector("app-toast")?.textContent).toContain(
  "Saved",
);
```

TestBed teardown destroys the app and should remove the views it attached.

## 257: How do you test animations in a component?

For new code using `animate.enter` and `animate.leave`, the classes are added and removed by Angular, and in tests the animation durations don't block anything. Check that elements appear and disappear.

For legacy `@angular/animations` code, add `provideNoopAnimations()` so animations finish instantly. The `@angular/animations` package is deprecated since v20.2, so new code should move to native CSS animations with `animate.enter` and `animate.leave`.

## 258: What is the difference between provideNoopAnimations and provideAnimations in tests?

`provideNoopAnimations()` runs animation callbacks but skips the actual animation, so tests don't wait for timing. `provideAnimations()` runs real animations, which is slower and can make tests flaky.

Both are part of the legacy `@angular/animations` setup. If the component has no `animations` metadata, you need neither.

## 259: How do you test a component that uses a CDK drag and drop list?

You can call the drop handler directly with a fake `CdkDragDrop` event, which tests your logic.

```ts
fixture.componentInstance.drop({
  previousIndex: 0,
  currentIndex: 2,
} as CdkDragDrop<string[]>);
expect(fixture.componentInstance.items()).toEqual(["b", "c", "a"]);
```

Real dragging needs pointer events and layout, which jsdom doesn't support well, so leave that to browser mode or E2E tests.

## 260: How do you test a component that uses virtual scrolling?

CDK virtual scroll needs real element sizes to decide what to render, and jsdom has no layout, so very little gets rendered. Run those tests in Vitest browser mode, or give the viewport a fixed size and test in a real browser.

For pure logic around the list (sorting, filtering), test the component's data instead of the rendered rows.

## 261: How do you test focus management and keyboard navigation?

Dispatch keyboard events and check `document.activeElement`.

```ts
const items = fixture.nativeElement.querySelectorAll("[role=option]");
items[0].focus();
items[0].dispatchEvent(
  new KeyboardEvent("keydown", { key: "ArrowDown", bubbles: true }),
);
await fixture.whenStable();

expect(document.activeElement).toBe(items[1]);
```

`userEvent.keyboard('{ArrowDown}')` from Testing Library is a more realistic alternative.

## 262: How do you test accessibility in unit tests?

A few useful checks:

- Use role and label queries, so missing labels fail tests
- Check ARIA attributes like `aria-expanded` after interactions
- Run axe on the rendered DOM with a library like `axe-core`

```ts
import axe from "axe-core";

it("has no a11y violations", async () => {
  await fixture.whenStable();
  const results = await axe.run(fixture.nativeElement);
  expect(results.violations).toEqual([]);
});
```

jsdom can't check color contrast, so also run accessibility checks in E2E tests.

## 263: How do you test a component's ARIA state?

Check the attribute values before and after the interaction.

```ts
const toggle = fixture.nativeElement.querySelector(
  "button[aria-controls=menu]",
);
expect(toggle.getAttribute("aria-expanded")).toBe("false");

toggle.click();
await fixture.whenStable();
expect(toggle.getAttribute("aria-expanded")).toBe("true");
```

## 264: How do you write snapshot tests in Vitest?

Use `toMatchSnapshot` or `toMatchInlineSnapshot`. The first run saves the output, and later runs compare against it.

```ts
it("renders the card", async () => {
  await fixture.whenStable();
  expect(fixture.nativeElement.innerHTML).toMatchSnapshot();
});
```

Update snapshots on purpose with the `-u` flag of Vitest.

## 265: What are the downsides of snapshot tests?

- Large snapshots are hard to review, so people approve changes without reading them
- They break on harmless markup changes, like a new class or comment
- Angular adds generated attributes (`_ngcontent-...`) that may change
- They don't say what behavior is important

Keep snapshots small and focused, or prefer explicit assertions about what matters.

## 266: How do you test a component with ChangeDetectorRef.detectChanges inside it?

Test the outcome normally. If the component calls `detectChanges()` itself after an async callback, the view should update even without `whenStable`. Your test still needs to wait for the async callback to run, for example with fake timers or an `await`.

If you need to spy on it, get it from the component's injector: `fixture.componentRef.injector.get(ChangeDetectorRef)`.

## 267: How do you test a component that depends on PLATFORM_ID?

Provide the platform you want to test and create the component.

```ts
import { PLATFORM_ID } from "@angular/core";

TestBed.configureTestingModule({
  imports: [MapComponent],
  providers: [{ provide: PLATFORM_ID, useValue: "server" }],
});

const fixture = TestBed.createComponent(MapComponent);
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".map-placeholder")).not.toBeNull();
```

This tests the `isPlatformBrowser` branch without running a real server.

## 268: How do you test HTTP caching in a service?

Call the method twice and expect only one request.

```ts
service.getConfig().subscribe();
httpMock.expectOne("/api/config").flush({ theme: "dark" });

let second: Config | undefined;
service.getConfig().subscribe((c) => (second = c));
httpMock.expectNone("/api/config");
expect(second).toEqual({ theme: "dark" });
```

## 269: How do you test request progress or file uploads?

Use `TestRequest.event()` to send progress events, then `flush` the final response.

```ts
import { HttpEventType } from "@angular/common/http";

const req = httpMock.expectOne("/api/upload");
req.event({ type: HttpEventType.UploadProgress, loaded: 50, total: 100 });
expect(component.progress()).toBe(50);

req.flush({ ok: true });
```

## 270: How do you test headers in an HTTP response?

Pass headers to `flush` and check the service reads them.

```ts
const req = httpMock.expectOne("/api/items?page=1");
req.flush([{ id: 1 }], { headers: { "X-Total-Count": "42" } });

expect(result.total).toBe(42);
```

The service must use `observe: 'response'` to read headers.

## 271: How do you test the withFetch backend?

You don't need to. `provideHttpClientTesting()` replaces the backend, whether the app uses the default backend or `withFetch()`, so your tests don't change.

If you want to test fetch specific behavior, like streaming or `keepalive`, that's better done with integration or E2E tests against a real server.

## 272: How do you test an HttpContext token used by an interceptor?

Send a request with the context and check how the interceptor treats it.

```ts
export const SKIP_AUTH = new HttpContextToken(() => false);

http
  .get("/api/public", { context: new HttpContext().set(SKIP_AUTH, true) })
  .subscribe();
const req = httpMock.expectOne("/api/public");
expect(req.request.headers.has("Authorization")).toBe(false);
```

## 273: How do you test the order of interceptors?

Register several interceptors and check the final request headers or a log of calls.

```ts
const calls: string[] = [];
const a: HttpInterceptorFn = (req, next) => {
  calls.push("a");
  return next(req);
};
const b: HttpInterceptorFn = (req, next) => {
  calls.push("b");
  return next(req);
};

providers: [
  provideHttpClient(withInterceptors([a, b])),
  provideHttpClientTesting(),
];

http.get("/x").subscribe();
httpMock.expectOne("/x").flush({});
expect(calls).toEqual(["a", "b"]);
```

## 274: How do you test a service that polls an API?

Use fake timers and handle each request as it comes.

```ts
vi.useFakeTimers();
service.startPolling();

await vi.advanceTimersByTimeAsync(0);
httpMock.expectOne("/api/status").flush({ ok: true });

await vi.advanceTimersByTimeAsync(5000);
httpMock.expectOne("/api/status").flush({ ok: false });

service.stopPolling();
vi.useRealTimers();
```

Also check that polling stops and no more requests are sent.

## 275: How do you test WebSocket code?

Wrap the WebSocket in a service and fake it. With RxJS `webSocket`, inject a factory so tests can pass a `Subject` instead.

```ts
const socket$ = new Subject<Message>();
providers: [{ provide: SOCKET_FACTORY, useValue: () => socket$ }];

socket$.next({ type: "chat", text: "hi" });
await fixture.whenStable();
expect(fixture.nativeElement.textContent).toContain("hi");
```

## 276: How do you test a service worker or PWA logic?

For logic around `SwUpdate`, fake the service and emit its events.

```ts
const versionUpdates = new Subject<VersionEvent>();
providers: [
  {
    provide: SwUpdate,
    useValue: { isEnabled: true, versionUpdates, activateUpdate: vi.fn() },
  },
];

versionUpdates.next({ type: "VERSION_READY" } as VersionReadyEvent);
expect(fixture.nativeElement.textContent).toContain("New version available");
```

Real service worker caching can only be tested in a browser with a production build.

## 277: How do you share setup between many spec files?

Put common setup in helper functions, not big shared base classes.

```ts
export function setupUserPage(overrides: Partial<UserService> = {}) {
  TestBed.configureTestingModule({
    imports: [UserPageComponent],
    providers: [
      { provide: UserService, useValue: { ...defaultUserFake, ...overrides } },
    ],
  });
  return TestBed.createComponent(UserPageComponent);
}
```

Each test calls the helper with only the differences it cares about, which keeps tests short and readable.

## 278: What is the page object pattern in component tests?

A page object is a small class that wraps queries and actions for a component, so tests read like user steps.

```ts
class LoginPage {
  constructor(private fixture: ComponentFixture<LoginComponent>) {}
  get error() {
    return this.fixture.nativeElement.querySelector(".error");
  }
  async login(email: string, password: string) {
    this.type("#email", email);
    this.type("#password", password);
    this.fixture.nativeElement
      .querySelector("form")
      .dispatchEvent(new Event("submit"));
    await this.fixture.whenStable();
  }
  private type(sel: string, v: string) {
    const el = this.fixture.nativeElement.querySelector(sel);
    el.value = v;
    el.dispatchEvent(new Event("input"));
  }
}
```

Component harnesses are the CDK's official version of this idea.

## 279: How do you write your own component harness?

Extend `ComponentHarness`, set `hostSelector`, and add async methods that use locators.

```ts
import { ComponentHarness } from "@angular/cdk/testing";

export class CounterHarness extends ComponentHarness {
  static hostSelector = "app-counter";

  private button = this.locatorFor("button");
  private value = this.locatorFor(".value");

  async increment() {
    return (await this.button()).click();
  }
  async getValue() {
    return Number(await (await this.value()).text());
  }
}
```

Tests then use `loader.getHarness(CounterHarness)`.

## 280: How do you add filters to a custom harness?

Add a static `with()` method that returns a `HarnessPredicate`.

```ts
static with(options: BaseHarnessFilters & { label?: string } = {}) {
  return new HarnessPredicate(CounterHarness, options).addOption(
    'label',
    options.label,
    (harness, label) => HarnessPredicate.stringMatches(harness.getLabel(), label),
  );
}
```

Now tests can write `loader.getHarness(CounterHarness.with({ label: 'Likes' }))`.

## 281: Can component harnesses be used in E2E tests too?

Yes, that's one of their goals. The same harness class works with different environments: `TestbedHarnessEnvironment` for unit tests, and other environments for E2E tools. The CDK ships one for Selenium WebDriver, and the community has ones for tools like Playwright and Cypress.

This lets you reuse the same interaction code at both levels.

## 282: How do you test a component inside a Material table?

Use `MatTableHarness` to read rows and cells.

```ts
const table = await loader.getHarness(MatTableHarness);
const rows = await table.getRows();
expect(rows.length).toBe(2);

const cells = await rows[0].getCellTextByColumnName();
expect(cells["name"]).toBe("Ana");
```

This is easier and more stable than counting `tr` elements by hand.

## 283: How do you test a component that uses MatSnackBar?

Either fake `MatSnackBar` and check `open` was called, or use `MatSnackBarHarness` with a document root loader.

```ts
const snackBar = { open: vi.fn() };
providers: [{ provide: MatSnackBar, useValue: snackBar }];

fixture.componentInstance.save();
expect(snackBar.open).toHaveBeenCalledWith(
  "Saved",
  "Close",
  expect.any(Object),
);
```

## 284: How do you test a component that imports a large UI library?

Usually just import it, since standalone components only pull in what they use. If a dependency is slow or needs browser features jsdom lacks, replace that one component with a stub through `overrideComponent`.

Keep real Material or CDK components when you test interactions, and use their harnesses.

## 285: How do you test a service with a hierarchical injector setup?

Build the same hierarchy in the test, with a parent component that provides the service and a child that injects it, and check the child gets the parent's instance.

```ts
@Component({
  imports: [ChildComponent],
  providers: [FormStateService],
  template: "<app-child />",
})
class ParentComponent {}

const fixture = TestBed.createComponent(ParentComponent);
const parentState = fixture.debugElement.injector.get(FormStateService);
const child = fixture.debugElement.query(By.directive(ChildComponent));
expect(child.injector.get(FormStateService)).toBe(parentState);
```

## 286: How do you test injection options like optional or self?

Set up providers with and without the dependency and check the result.

```ts
@Injectable({ providedIn: "root" })
class Tracker {
  private analytics = inject(Analytics, { optional: true });
  track(e: string) {
    this.analytics?.send(e);
    return this.analytics !== null;
  }
}

it("works without analytics", () => {
  expect(TestBed.inject(Tracker).track("x")).toBe(false);
});
```

## 287: How do you test APP_INITIALIZER or provideAppInitializer?

Add the initializer to TestBed providers and inject `ApplicationInitStatus` to wait for it.

```ts
import {
  ApplicationInitStatus,
  provideAppInitializer,
  inject,
} from "@angular/core";

TestBed.configureTestingModule({
  providers: [
    { provide: ConfigService, useValue: fakeConfig },
    provideAppInitializer(() => inject(ConfigService).load()),
  ],
});

await TestBed.inject(ApplicationInitStatus).donePromise;
expect(fakeConfig.load).toHaveBeenCalled();
```

`APP_INITIALIZER` is the older token. `provideAppInitializer` is the current API.

## 288: How do you test environment specific config in tests?

Don't import `environment.ts` directly in services. Provide config through an injection token, so tests can pass any values.

```ts
export const APP_CONFIG = new InjectionToken<AppConfig>("APP_CONFIG");

providers: [
  { provide: APP_CONFIG, useValue: { apiUrl: "/test-api", featureX: true } },
];
```

This also makes it easy to test both sides of a feature flag.

## 289: How do you test a feature flag in a component?

Provide the flag service with different values in different tests.

```ts
function setup(enabled: boolean) {
  TestBed.configureTestingModule({
    imports: [CheckoutComponent],
    providers: [{ provide: FeatureFlags, useValue: { isOn: () => enabled } }],
  });
  return TestBed.createComponent(CheckoutComponent);
}

it("shows the new button when enabled", async () => {
  const fixture = setup(true);
  await fixture.whenStable();
  expect(fixture.nativeElement.querySelector(".pay-v2")).not.toBeNull();
});
```

## 290: How do you test a component that uses inject(DestroyRef)?

Destroy the fixture and check the cleanup ran.

```ts
const fixture = TestBed.createComponent(TimerComponent);
await fixture.whenStable();
const clearSpy = vi.spyOn(globalThis, "clearInterval");

fixture.destroy();
expect(clearSpy).toHaveBeenCalled();
```

For services, `TestBed.resetTestingModule()` destroys the environment injector and runs `DestroyRef.onDestroy` callbacks.

## 291: How do you test takeUntilDestroyed?

Check that the subscription stops after the component is destroyed.

```ts
const ticks$ = new Subject<number>();
// component subscribes with takeUntilDestroyed()
const fixture = TestBed.createComponent(TickerComponent);
fixture.destroy();

ticks$.next(1);
expect(fixture.componentInstance.last()).toBeUndefined();
expect(ticks$.observed).toBe(false);
```

## 292: How do you test error handling with ErrorHandler?

Provide a fake `ErrorHandler` and trigger an error.

```ts
const errorHandler = { handleError: vi.fn() };
providers: [{ provide: ErrorHandler, useValue: errorHandler }];

fixture.nativeElement.querySelector(".crash").click();
expect(errorHandler.handleError).toHaveBeenCalledWith(expect.any(Error));
```

Errors thrown in event listeners are passed to `ErrorHandler`. Some errors during change detection are rethrown in tests, so you can also assert with `toThrow`.

## 293: How do you check console errors in tests?

Spy on `console.error` and assert it wasn't called. Some teams fail any test that logs an error.

```ts
let errorSpy: ReturnType<typeof vi.spyOn>;
beforeEach(
  () => (errorSpy = vi.spyOn(console, "error").mockImplementation(() => {})),
);
afterEach(() => expect(errorSpy).not.toHaveBeenCalled());
```

This catches Angular warnings and errors that don't fail tests on their own.

## 294: What are errorOnUnknownElements and errorOnUnknownProperties?

TestBed options that make unknown elements and unknown property bindings in templates throw errors instead of only logging them.

```ts
TestBed.configureTestingModule({
  imports: [MyComponent],
  errorOnUnknownElements: true,
  errorOnUnknownProperties: true,
});
```

You can also set them globally in `initTestEnvironment`. They catch missing imports, which otherwise show only as console errors.

## 295: How do you test a component with a template that uses @let?

`@let` is just local template state, so test what it renders, not the variable itself.

```ts
// template: @let total = price() * qty(); <span>{{ total }}</span>
fixture.componentRef.setInput("price", 5);
fixture.componentRef.setInput("qty", 3);
await fixture.whenStable();
expect(fixture.nativeElement.querySelector("span").textContent).toBe("15");
```

## 296: How do you test @switch blocks?

Set each case and check the matching view, plus the `@default` case.

```ts
for (const [status, cls] of [
  ["ok", ".ok"],
  ["error", ".error"],
  ["other", ".unknown"],
]) {
  fixture.componentRef.setInput("status", status);
  await fixture.whenStable();
  expect(fixture.nativeElement.querySelector(cls)).not.toBeNull();
}
```

Using `it.each` gives each case its own test name, which reads better in reports.

## 297: How does it.each help with Angular tests?

`it.each` runs the same test with different inputs and gives each run its own name. It's useful for pipes, validators and components with many input states.

```ts
it.each([
  [0, "Free"],
  [9.5, "$9.50"],
  [1000, "$1,000.00"],
])("formats %s as %s", (value, expected) => {
  expect(pipe.transform(value)).toBe(expected);
});
```

## 298: How do you debug a failing Angular test?

- Run only that test with `it.only` or `--include`
- Print the DOM: `console.log(fixture.nativeElement.innerHTML)`
- Check that change detection ran before the assertion
- Check providers and overrides are set before `createComponent`
- Use the debugger: Vitest supports `--inspect`, and browser mode and Karma let you use browser devtools
- Read the full error, since Angular error codes (like NG0201 for a missing provider) link to docs

## 299: What does error NG0201 "No provider for X" mean in a test?

The component or service tried to inject `X`, but nothing in the test injector provides it. Common causes: a service without `providedIn: 'root'`, a missing `provideHttpClient()`, `provideRouter()` or a token.

Fix it by adding the provider (or a fake) in `configureTestingModule`. Don't add the real thing if it would make real network calls.

## 300: How do you test that nothing happens, for example no request is sent?

Use negative assertions: `expectNone` for HTTP, `not.toHaveBeenCalled` for spies, `toBeNull` for elements.

```ts
fixture.componentInstance.form.setValue({ email: "" });
fixture.nativeElement.querySelector("form").dispatchEvent(new Event("submit"));

httpMock.expectNone("/api/subscribe");
expect(fixture.nativeElement.querySelector(".success")).toBeNull();
```

Make sure the test would fail if the thing did happen, otherwise a negative assertion proves little.

# Advanced Questions (301-450)

## 301: How does TestBed work internally?

TestBed builds a dynamic testing module from what you pass to `configureTestingModule`, applies overrides, and creates an environment injector on top of a test platform (`platformBrowserTesting`). When you call `createComponent`, it creates the component with that injector and attaches it to a fixture root element in the document.

Overrides are applied by changing the compiled metadata of components before they're used, which is why they must happen before the first `inject` or `createComponent`. After each test, TestBed resets the module and, with `destroyAfterEach`, destroys the injector and DOM.

## 302: What does initTestEnvironment do and when do you call it?

It sets up the test platform once for the whole run. The CLI builders call it for you. If you set things up by hand, it looks like this:

```ts
import { getTestBed } from "@angular/core/testing";
import {
  BrowserTestingModule,
  platformBrowserTesting,
} from "@angular/platform-browser/testing";

getTestBed().initTestEnvironment(
  BrowserTestingModule,
  platformBrowserTesting(),
  {
    errorOnUnknownElements: true,
    errorOnUnknownProperties: true,
  },
);
```

Older setups used `BrowserDynamicTestingModule` and `platformBrowserDynamicTesting` from `@angular/platform-browser-dynamic/testing`, which are deprecated.

## 303: Why do overrides need TestBed to be "not instantiated" yet?

Once TestBed creates the injector and compiles the components, the providers and metadata are fixed for that injector. Changing them afterwards would leave already created instances using the old setup, and the state would be inconsistent.

So TestBed throws on late overrides instead of silently doing nothing. Structure tests so overrides come first, often by moving `createComponent` out of `beforeEach` into a setup helper called after overrides.

## 304: How does the zoneless TestBed decide when the fixture is stable?

Without Zone.js, Angular tracks pending work through the `PendingTasks` service and the change detection scheduler. `whenStable()` resolves when there's no scheduled change detection and no pending tasks. `HttpClient` and the router register pending tasks, so stability waits for them.

Your own async work (a plain `setTimeout` or a third party promise) isn't tracked unless you register it with `PendingTasks`, so `whenStable` won't wait for it.

## 305: How do you make your own async work visible to whenStable?

Use `PendingTasks` in the app code. Its `run` method marks a task as pending until the promise settles.

```ts
import { PendingTasks } from "@angular/core";

export class ReportService {
  private pending = inject(PendingTasks);

  load() {
    return this.pending.run(() => fetchReport());
  }
}
```

Now `fixture.whenStable()` waits for the report to load. This also helps SSR, which waits for pending tasks before serializing the page.

## 306: What changes when you move a large test suite from Zone.js to zoneless?

- `fakeAsync`, `tick`, `flush` and `waitForAsync` stop working without `zone.js/testing`. Replace them with fake timers and `async`/`await`.
- Tests that changed plain fields and relied on Zone to update the view will see old DOM or `ExpressionChanged` errors. Use signals, `setInput` or `markForCheck`.
- `fixture.detectChanges()` still works, but `await fixture.whenStable()` is the better default.
- Fixtures auto detect changes by default.

Do it gradually: add `provideZonelessChangeDetection()` to some spec files first, fix them, then flip the default.

## 307: Can you use fakeAsync in a zoneless app's tests?

Only if Zone.js and `zone.js/testing` are still loaded in the test polyfills. `fakeAsync` uses Zone to control time, and it works even if the TestBed uses `provideZonelessChangeDetection()`.

It's a transition tool. Keeping Zone.js only for tests means tests run in a different environment than the app, so plan to move to framework fake timers.

## 308: What are the pitfalls of Vitest fake timers with Angular?

- Use the async versions (`advanceTimersByTimeAsync`, `runAllTimersAsync`). The sync ones don't let promises in between run, so Angular's async scheduling may get stuck.
- Angular's zoneless scheduler uses timers and `requestAnimationFrame`. Make sure your fake timers config doesn't break it. If `whenStable()` hangs, try advancing timers instead of awaiting stability.
- Always call `vi.useRealTimers()` after, or use an `afterEach`, so one test doesn't leak fake time into the next.
- `vi.setSystemTime` changes `Date`, which can affect date pipes.

## 309: How do you test a race condition between two async calls?

Control the order of responses by hand and check the final state.

```ts
component.load("a");
component.load("b");

const [reqA, reqB] = httpMock.match((r) => r.url.startsWith("/api/item"));
reqB.flush({ id: "b" });
reqA.flush({ id: "a" }); // old, slow response arrives last

await fixture.whenStable();
expect(component.item()?.id).toBe("b");
```

This test fits code that doesn't cancel old requests, for example one that uses `mergeMap`, where it shows the stale data bug. With `switchMap`, `reqA` is cancelled instead, and flushing a cancelled request throws, so check `reqA.cancelled` there.

## 310: How do you test memory leaks in components?

Unit tests can't measure real memory well, but you can check the usual causes:

- Subscriptions closed on destroy (`subject.observed` is false)
- Event listeners removed (spy on `removeEventListener`)
- Timers cleared (spy on `clearInterval`)
- No references kept in root services after destroy

For real leak checks, use browser devtools heap snapshots or E2E tooling that measures memory across repeated navigation.

## 311: How do you test a component's performance-sensitive behavior?

Count work instead of timing it. Timing in unit tests is noisy and depends on the machine.

```ts
const renderSpy = vi.fn();
// component calls renderSpy in afterEveryRender, or count computed runs
fixture.componentRef.setInput("items", sameItems);
await fixture.whenStable();
expect(heavyCalc).toHaveBeenCalledTimes(1);
```

For example, check that a `computed` doesn't run again when an unrelated signal changes, or that `track` in `@for` keeps DOM nodes instead of recreating them.

## 312: How do you test that @for track reuses DOM nodes?

Keep a reference to a DOM node, update the list with new objects that have the same ids, and check the node is the same.

```ts
fixture.componentRef.setInput("items", [{ id: 1, name: "A" }]);
await fixture.whenStable();
const before = fixture.nativeElement.querySelector("li");

fixture.componentRef.setInput("items", [{ id: 1, name: "A2" }]);
await fixture.whenStable();
const after = fixture.nativeElement.querySelector("li");

expect(after).toBe(before);
expect(after.textContent).toContain("A2");
```

With `track $index` or a wrong key, this test would catch the extra DOM work.

## 313: How do you test signal equality functions?

Set a value that's "equal" by your custom function and check dependents don't update.

```ts
const user = signal({ id: 1, name: "Ana" }, { equal: (a, b) => a.id === b.id });
const runs = vi.fn();
const label = computed(() => {
  runs();
  return user().name;
});

label();
user.set({ id: 1, name: "Changed" });
label();

expect(runs).toHaveBeenCalledTimes(1);
```

This also shows a trap: the name changed but the computed didn't update, because the equality function said the values were equal.

## 314: How do you test code that reads signals with untracked?

Check that changing the untracked signal does not cause a recompute or an effect run.

```ts
const a = signal(1);
const b = signal(10);
const sum = computed(() => a() + untracked(b));

expect(sum()).toBe(11);
b.set(20);
expect(sum()).toBe(11); // not recomputed
a.set(2);
expect(sum()).toBe(22);
```

## 315: How do you test an effect's cleanup function?

Make the effect register `onCleanup`, then trigger a rerun and a destroy, and check cleanup ran both times.

```ts
const cleanup = vi.fn();
const id = signal(1);

TestBed.runInInjectionContext(() =>
  effect((onCleanup) => {
    id();
    onCleanup(cleanup);
  }),
);

TestBed.tick();
id.set(2);
TestBed.tick();
expect(cleanup).toHaveBeenCalledTimes(1);

TestBed.resetTestingModule();
expect(cleanup).toHaveBeenCalledTimes(2);
```

## 316: Why is testing effects directly often a smell?

Effects are for side effects like syncing to storage, logging or calling non-Angular APIs. If you find yourself testing an effect that sets other signals, the code probably should use `computed` or `linkedSignal` instead, which are easier to test and avoid extra change detection rounds.

Test effects through their visible side effect (a spy on the storage service), not through their internals.

## 317: How do you test the difference between root effects and component effects?

Effects created in a service run as root effects, before change detection. Effects created in a component run during change detection, as part of that component's view tree.

In tests, root effects run on `TestBed.tick()`, and component effects run when the fixture is checked. If an effect seems not to run, check where it was created, and make sure the fixture is attached and checked, for example with `await fixture.whenStable()`.

## 318: How do you test a resource that reacts to signal params?

Change the params signal and check that a new request is sent and the old one is aborted.

```ts
const id = signal(1);
const user = TestBed.runInInjectionContext(() =>
  httpResource<User>(() => `/api/users/${id()}`),
);
TestBed.tick();
const first = httpMock.expectOne("/api/users/1");

id.set(2);
TestBed.tick();
expect(first.cancelled).toBe(true);

httpMock.expectOne("/api/users/2").flush({ id: 2 });
await TestBed.inject(ApplicationRef).whenStable();
expect(user.value()?.id).toBe(2);
```

## 319: How do you test resource error and status states?

Make the loader fail and check `status()`, `error()` and that reading `value()` behaves as expected.

```ts
const res = TestBed.runInInjectionContext(() =>
  resource({ loader: () => Promise.reject(new Error("boom")) }),
);

await TestBed.inject(ApplicationRef).whenStable();
expect(res.status()).toBe("error");
expect(res.error()?.message).toBe("boom");
```

Reading `value()` on a resource in error state throws in recent versions, so check `hasValue()` first in templates and tests.

## 320: How do you design Angular code so it's easy to test?

- Keep logic in plain functions and services, not in templates or components
- Use DI for everything external: HTTP, storage, time, window, third party SDKs
- Use signals and `computed` for derived state
- Keep components small, with clear inputs and outputs
- Avoid static singletons and global state outside DI
- Inject a clock or time provider when logic depends on time

Code that's hard to test is often hard to change too, so test pain is useful design feedback.

## 321: How do you inject time to make tests deterministic?

Wrap `Date.now()` in a token or service.

```ts
export const NOW = new InjectionToken<() => number>("NOW", {
  factory: () => () => Date.now(),
});

@Injectable({ providedIn: "root" })
export class SessionService {
  private now = inject(NOW);
  isExpired(expiresAt: number) {
    return this.now() > expiresAt;
  }
}

// test
providers: [{ provide: NOW, useValue: () => 1_000 }];
expect(TestBed.inject(SessionService).isExpired(500)).toBe(true);
```

This avoids global fake timers when you only need "now".

## 322: How do you decide between mocking and using real dependencies?

Use the real thing when it's fast, deterministic and owned by you, like a pure helper service or a store. Mock things that are slow, random or external: HTTP, storage, timers, analytics, third party SDKs.

Over-mocking makes tests pass while the real pieces don't fit together. Under-mocking makes tests slow and flaky. A good default is to mock at the edges of your app and keep the middle real.

## 323: What is the risk of mocking too much?

Each fake is a copy of how you think the real code behaves. When the real service changes, the fake doesn't, so tests keep passing while the app breaks. Heavily mocked tests also tend to check calls instead of results, which ties them to implementation.

Use typed fakes, keep them small, and add some integration tests that use real services with only HTTP faked.

## 324: What is contract testing and how does it relate to Angular apps?

Contract testing checks that the frontend and backend agree on the API shape. The frontend side records what requests it makes and what responses it expects (for example with Pact), and the backend runs those contracts against its real code.

It fills the gap between unit tests with fake HTTP (which can drift from the real API) and slow full E2E tests. Generated API clients from OpenAPI specs also reduce drift.

## 325: How do you keep HTTP mock data in sync with the real API?

- Generate TypeScript types or clients from the OpenAPI spec and type fake data with them
- Store example responses as fixtures and check them against the schema
- Use contract tests
- Use MSW (Mock Service Worker) handlers shared between tests and local development

Typed fakes alone catch many mismatches at compile time.

## 326: How do you use MSW with Angular tests?

MSW intercepts requests at the network level. In Node it patches `fetch` and other request modules, and in the browser it uses a service worker. Your Angular code runs unchanged, including interceptors.

```ts
import { setupServer } from "msw/node";
import { http, HttpResponse } from "msw";

const server = setupServer(
  http.get("/api/users", () => HttpResponse.json([{ id: 1 }])),
);
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

In Node, use `provideHttpClient(withFetch())` so requests go through `fetch`, which MSW can intercept. In the browser, MSW's service worker handles both `fetch` and XHR. Don't add `provideHttpClientTesting()`, since that would replace the backend entirely.

## 327: HttpTestingController or MSW: which is better?

`HttpTestingController` is built in, synchronous and very precise: you can check every request and control timing. It's great for service and interceptor tests.

MSW tests a bit more of the real stack and can share handlers with local dev and E2E. Responses are async, so tests need `await`. Many teams use `HttpTestingController` for unit tests and MSW for integration tests.

## 328: How do you structure tests for a large Angular codebase?

- Unit tests next to the code (`*.spec.ts`)
- Shared test helpers and fakes in a `testing/` folder per library or feature, exported for other specs
- Integration tests for feature pages with real children and fake HTTP
- E2E tests in their own project or folder, organized by user flow
- Lint rules that block focused tests and imports of test code from app code

In Nx or multi project workspaces, each library has its own test target, so CI can run only affected tests.

## 329: How do you only run tests affected by a change?

Use a tool that knows the dependency graph. Nx has `nx affected -t test`. Vitest also supports `--changed` to run tests related to changed files in plain projects.

In CI, combine affected runs on pull requests with a full run on the main branch, so nothing slips through due to graph mistakes.

## 330: How do you make a slow test suite faster?

- Switch from Karma to Vitest with jsdom, which avoids starting browsers
- Run tests in parallel (Vitest does this by default with workers)
- Avoid real timers and waits, use fake timers
- Stub heavy child components and large libraries in unit tests
- Remove duplicated tests that cover the same thing at several levels
- Run only affected tests in CI
- Check for slow setup, like huge fixtures or repeated module configuration

Measure first: Vitest's reporter shows slow files and tests.

## 331: What are the trade-offs of Vitest isolation and pools?

By default Vitest runs each test file in an isolated environment, using worker threads or child processes. This prevents global state leaking between files but costs time to set up each environment.

Turning isolation off (`isolate: false`) can speed things up a lot, but then module level state and globals (like stubs on `window`) are shared between files, which can cause random failures. Only do it when tests are carefully cleaned up.

## 332: How do you find tests that depend on order?

Run tests in random order. Jasmine randomizes by default. Vitest has `sequence.shuffle`.

```ts
// vitest config
export default defineConfig({ test: { sequence: { shuffle: true } } });
```

When a test fails only in some orders, look for shared state: module variables, singletons outside DI, globals, fake timers left on, or spies not restored.

## 333: How do you deal with flaky tests in CI?

1. Track them, for example with a test report that shows failures over time.
2. Reproduce: run the test many times in a loop, with shuffle on.
3. Find the cause: real timers, unawaited promises, shared state, time zones, network.
4. Fix it, or quarantine it with a ticket if it blocks everyone.

Automatic retries hide the problem. If you use them, still report which tests needed a retry.

## 334: Why do tests fail in CI but pass locally?

Common reasons:

- Different time zone or locale, affecting dates and number formats
- Slower machines, exposing timing bugs
- Different test order or parallelism
- Missing environment variables or files
- Different browser versions in browser mode or E2E
- Locally cached data or a running dev server

Set `TZ=UTC` in CI and test setup, and avoid real timers.

## 335: How do you test locale-dependent formatting?

Register the locale data and provide `LOCALE_ID` in the test.

```ts
import { registerLocaleData } from "@angular/common";
import localeDe from "@angular/common/locales/de";

registerLocaleData(localeDe);

TestBed.configureTestingModule({
  imports: [PriceComponent],
  providers: [{ provide: LOCALE_ID, useValue: "de" }],
});
```

Then `1234.5` with the currency pipe should show something like `1.234,50 €`. Check the exact characters, since some locales use non-breaking spaces.

## 336: How do you test the default ErrorHandler behavior in zoneless apps?

In zoneless apps, errors from event listeners and some async work are reported to `ErrorHandler`. With `provideBrowserGlobalErrorListeners()` (added to new apps since v20), uncaught errors and unhandled promise rejections on `window` are sent there too.

In tests, provide a fake `ErrorHandler` and trigger the error. TestBed also has a `rethrowApplicationErrors` option, true by default in recent versions, which rethrows errors that reach the handler so tests fail instead of passing silently.

## 337: What is the rethrowApplicationErrors option?

It's a TestBed option that makes errors caught by Angular (for example in event handlers or effects) be rethrown in the test, so they fail it. It's on by default.

If you're testing your own error handling flow and expect an error to be handled, set it to `false` for that test.

```ts
TestBed.configureTestingModule({ rethrowApplicationErrors: false });
```

## 338: How do you test a custom ErrorHandler?

Test it as a service. Inject it and call `handleError` with different errors.

```ts
TestBed.configureTestingModule({
  providers: [
    { provide: ErrorHandler, useClass: AppErrorHandler },
    { provide: Monitoring, useValue: { report: vi.fn() } },
  ],
});

const handler = TestBed.inject(ErrorHandler);
handler.handleError(new HttpErrorResponse({ status: 500 }));

expect(TestBed.inject(Monitoring).report).toHaveBeenCalled();
```

## 339: How do you test server-side rendering logic?

Unit test SSR branches by providing `PLATFORM_ID: 'server'` and checking that browser-only code isn't called. For the real render, use `renderApplication` from `@angular/platform-server` in a Node test, or start the built server and request pages.

```ts
import { renderApplication } from "@angular/platform-server";

const html = await renderApplication(bootstrap, {
  document: "<app-root></app-root>",
  url: "/products/1",
});
expect(html).toContain("<h1>Product 1</h1>");
```

`bootstrap` is the function from `main.server.ts`. Check its exact signature for your Angular version.

## 340: How do you test hydration problems?

Hydration mismatches show up as console errors (NG05xx codes) when the client DOM doesn't match the server HTML. They're hard to catch in unit tests.

Use E2E tests against the SSR build: load pages, collect console messages, and fail on hydration errors. Also check `ngSkipHydration` usage in code review, since it hides problems.

## 341: How do you test TransferState or HTTP transfer cache behavior?

For unit tests, provide `TransferState`, set a key, and check the service reads it instead of calling HTTP.

```ts
const state = TestBed.inject(TransferState);
state.set(makeStateKey<Product[]>("products"), [{ id: 1 }]);

service.load().subscribe();
httpMock.expectNone("/api/products");
```

The built-in HTTP transfer cache (`withHttpTransferCacheOptions`) is best checked in E2E against the SSR build, by counting network calls after hydration.

## 342: How do you test incremental hydration?

Incremental hydration uses `@defer` with `hydrate` triggers. In unit tests, defer blocks behave like normal client defer blocks, so you test states with `getDeferBlocks()`.

To test the actual hydration timing (that a block hydrates on interaction), use an E2E test against the SSR build and check that events before hydration are replayed after it.

## 343: How do you test route-level render modes?

Server route configs (`ServerRoute` with `RenderMode.Prerender`, `Server` or `Client`) only take effect in the server build. Test them by building and checking the output:

- Prerendered routes have HTML files in the build output
- Server routes return full HTML from the server
- Client routes return the shell

Small scripts or E2E tests that fetch each route and inspect the HTML work well.

## 344: How do you test a library of reusable components?

- Unit test each component through its public API: inputs, outputs, projected content
- Ship component harnesses so consumers can test their usage
- Use Storybook stories with interaction tests for visual states
- Add accessibility checks
- Test with OnPush hosts and zoneless setup, so it works in any app

Treat the public API like a contract. Breaking a selector or input name should break a test.

## 345: How do you test a component in both Zone.js and zoneless apps?

Run the same specs twice with different setup, for example two test targets: one with `zone.js` in polyfills, one with `provideZonelessChangeDetection()` through a providers file.

A component that works zoneless with signals and `markForCheck` works with Zone.js too. The reverse isn't true, so zoneless is the stricter test.

## 346: How do you test a component that uses NgZone.runOutsideAngular?

Code outside Angular's zone doesn't trigger change detection in Zone apps. Test that the view only updates when the component brings the change back into Angular (with a signal, `markForCheck` or `ngZone.run`).

```ts
fixture.componentInstance.startTracking(); // adds a mousemove listener outside the zone
document.dispatchEvent(new MouseEvent("mousemove", { clientX: 100 }));
await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".x").textContent).toBe("100");
```

In zoneless apps, `NgZone` is a no-op version, so this code still works, but `runOutsideAngular` no longer changes anything.

## 347: How do you test a component that wraps a non-Angular widget library?

Treat the widget as an external dependency:

- Inject a factory for the widget so unit tests can pass a fake
- Check that your component creates it with the right options, forwards input changes as API calls, and maps widget events to outputs
- Check `destroy()` is called on component destroy

Run a few tests in browser mode or E2E with the real widget, since it probably needs real layout.

## 348: How do you test a custom element built with Angular Elements?

Register the element with `createCustomElement` and `customElements.define`, then use it like plain DOM.

```ts
const app = await createApplication({ providers: [] });
const El = createCustomElement(RatingComponent, { injector: app.injector });
customElements.define("x-rating", El);

const el = document.createElement("x-rating") as HTMLElement & {
  value: number;
};
document.body.append(el);
el.value = 4;
await app.whenStable();
expect(el.querySelectorAll(".star.filled").length).toBe(4);
```

Each tag name can be defined only once per page, so do it in `beforeAll` or a guard.

## 349: How do you test a micro frontend setup?

Test each micro frontend on its own with unit and integration tests. For the shell, fake the remote loading (for example the function that calls `loadRemoteModule`) and check routing and error handling when a remote fails.

The real integration (shell loading remotes at runtime) needs E2E tests against deployed or locally served apps, with checks for shared dependency versions and fallback UIs.

## 350: How do you test security related code like a sanitizer bypass?

Check that untrusted input is sanitized and that your code only bypasses sanitization for trusted values.

```ts
fixture.componentRef.setInput(
  "html",
  '<img src=x onerror="alert(1)"><b>ok</b>',
);
await fixture.whenStable();

const host: HTMLElement = fixture.nativeElement.querySelector(".content");
expect(host.querySelector("img")?.getAttribute("onerror")).toBeNull();
expect(host.querySelector("b")?.textContent).toBe("ok");
```

Add tests for any `bypassSecurityTrust...` call to prove the input really is safe at that point.

## 351: How do you test an auth flow with token refresh?

In an interceptor test, return 401 for the first request, expect a refresh request, flush it with a new token, and expect the original request to be retried with the new token.

```ts
http.get("/api/me").subscribe((r) => (result = r));

httpMock
  .expectOne("/api/me")
  .flush(null, { status: 401, statusText: "Unauthorized" });
httpMock.expectOne("/api/refresh").flush({ token: "new" });

const retry = httpMock.expectOne("/api/me");
expect(retry.request.headers.get("Authorization")).toBe("Bearer new");
retry.flush({ id: 1 });
```

Also test two parallel 401s trigger only one refresh request.

## 352: How do you test that only one refresh happens for parallel requests?

Send two requests, fail both with 401, and expect a single refresh call.

```ts
http.get("/api/a").subscribe();
http.get("/api/b").subscribe();

httpMock.expectOne("/api/a").flush(null, { status: 401, statusText: "" });
httpMock.expectOne("/api/b").flush(null, { status: 401, statusText: "" });

const refresh = httpMock.match("/api/refresh");
expect(refresh.length).toBe(1);
refresh[0].flush({ token: "t2" });

expect(httpMock.match((r) => /\/api\/[ab]$/.test(r.url)).length).toBe(2);
```

The last line checks that both original requests were retried after the refresh.

## 353: How do you test XSRF handling in HttpClient?

Set the XSRF cookie and check that mutating requests to same origin URLs get the header.

```ts
document.cookie = "XSRF-TOKEN=abc";
TestBed.configureTestingModule({
  providers: [
    provideHttpClient(withXsrfConfiguration({})),
    provideHttpClientTesting(),
  ],
});

TestBed.inject(HttpClient).post("/api/save", {}).subscribe();
const req = httpMock.expectOne("/api/save");
expect(req.request.headers.get("X-XSRF-TOKEN")).toBe("abc");
```

Also test that absolute URLs to other domains don't get the header. Clean the cookie in `afterEach`.

## 354: How do you test role-based UI without duplicating tests?

Use a table of roles and expected visible elements.

```ts
it.each([
  ["admin", [".edit", ".delete"]],
  ["editor", [".edit"]],
  ["viewer", []],
])("%s sees the right actions", async (role, visible) => {
  const fixture = setup({ role });
  await fixture.whenStable();
  for (const sel of [".edit", ".delete"]) {
    expect(!!fixture.nativeElement.querySelector(sel)).toBe(
      visible.includes(sel),
    );
  }
});
```

Remember UI checks don't replace server side authorization tests.

## 355: How do you test that sensitive data doesn't end up in logs?

Spy on the logger or `console` and check the arguments don't contain secrets.

```ts
const log = vi.spyOn(console, "log");
service.login({ email: "a@b.com", password: "secret123" });

const output = JSON.stringify(log.mock.calls);
expect(output).not.toContain("secret123");
```

Do the same for error reporting services and analytics events.

## 356: How do you test a CSP-compatible setup?

Unit tests can't check CSP. Run E2E tests against a build served with the real `Content-Security-Policy` header and fail on CSP violation console messages or `securitypolicyviolation` events.

For Angular specifics, check that inline styles use the nonce (`ngCspNonce` or `CSP_NONCE`) and that nothing uses `eval`-like features.

## 357: How do you design a test strategy for a new Angular feature?

1. List the behaviors and edge cases from the requirements.
2. Put pure logic in functions and services, and unit test them heavily.
3. Write component tests for each user facing state: loading, empty, error, success, permissions.
4. Write integration tests for the feature page with real children and fake HTTP.
5. Add one or two E2E tests for the main happy path.
6. Add accessibility checks.

Write the test plan in the PR so reviewers see what's covered.

## 358: What should not be tested in unit tests?

- Angular itself (that `@if` works, that `HttpClient` sends requests)
- Third party libraries' internals
- Private methods and internal fields directly
- Exact CSS layout and pixels (use visual tests)
- Trivial getters with no logic

Focus on your logic and how your code uses the framework and libraries.

## 359: What is mutation testing and how can it help Angular projects?

Mutation testing changes your code in small ways (flipping `>` to `>=`, removing a line) and reruns tests. If tests still pass, that "mutant survived", which means the tests didn't really check that code.

Stryker supports TypeScript and can run with Vitest or Karma. It's slow, so run it on critical modules or nightly, not on every commit.

## 360: How do you test a generic or reusable data table component?

- Test with different column configs and data shapes
- Test sorting, paging and filtering through the UI and through outputs
- Test custom cell templates passed with `ng-template` and content queries
- Test empty and loading states
- Test that `track` works with changing data
- Provide a harness for consumers

Use a test host with a typed row type to make sure generic types work in templates.

## 361: How do you test content queries like contentChildren()?

Use a host that projects items, then check the component sees them and reacts when they change.

```ts
@Component({
  imports: [TabsComponent, TabComponent],
  template: `
    <app-tabs>
      @for (t of tabs(); track t) {
        <app-tab [label]="t" />
      }
    </app-tabs>
  `,
})
class HostComponent {
  tabs = signal(["A", "B"]);
}

const fixture = TestBed.createComponent(HostComponent);
await fixture.whenStable();
fixture.componentInstance.tabs.set(["A", "B", "C"]);
await fixture.whenStable();
expect(fixture.nativeElement.querySelectorAll(".tab-header").length).toBe(3);
```

## 362: How do you test a component that uses ng-template inputs (template outlets)?

Pass a template from the host and check it's rendered with the right context.

```ts
@Component({
  imports: [ListComponent],
  template: `
    <app-list [items]="['a', 'b']" [itemTemplate]="tpl" />
    <ng-template #tpl let-item let-i="index"
      ><span class="row">{{ i }}:{{ item }}</span></ng-template
    >
  `,
})
class HostComponent {}

await fixture.whenStable();
const rows = [...fixture.nativeElement.querySelectorAll(".row")].map(
  (r: Element) => r.textContent,
);
expect(rows).toEqual(["0:a", "1:b"]);
```

## 363: How do you test host directives?

Test the component that uses `hostDirectives` and check the directive's effect, plus any inputs or outputs it exposes.

```ts
@Component({
  selector: "app-menu-item",
  template: "Item",
  hostDirectives: [{ directive: FocusableDirective, inputs: ["disabled"] }],
})
class MenuItemComponent {}

fixture.componentRef.setInput("disabled", true);
await fixture.whenStable();
expect(fixture.nativeElement.getAttribute("tabindex")).toBe("-1");
```

`setInput` works for host directive inputs that are exposed on the component.

## 364: How do you test a directive that uses inject() to read the host component?

Create a host template where the directive is on that component, and check the directive got the right instance.

```ts
@Component({
  imports: [DatepickerComponent, AutoTodayDirective],
  template: "<app-datepicker appAutoToday />",
})
class HostComponent {}

const fixture = TestBed.createComponent(HostComponent);
await fixture.whenStable();
const picker = fixture.debugElement.query(
  By.directive(DatepickerComponent),
).componentInstance;
expect(picker.value()).toEqual(today);
```

## 365: How do you test DI resolution modifiers like host or skipSelf?

Build component trees where the provider is at different levels and check which instance is injected, or that injection fails.

```ts
// child injects Parent with { host: true, optional: true }
const child = fixture.debugElement
  .query(By.directive(ChildDirective))
  .injector.get(ChildDirective);
expect(child.parent).toBeNull();
```

These tests document tricky DI behavior that's easy to break during refactors.

## 366: How do you test a service that should be a singleton across lazy routes?

Navigate to two lazy routes with `RouterTestingHarness` and compare instances from each routed component's injector.

```ts
await harness.navigateByUrl("/a");
const sa = harness.routeDebugElement!.injector.get(CartService);
await harness.navigateByUrl("/b");
const sb = harness.routeDebugElement!.injector.get(CartService);
expect(sa).toBe(sb);
```

If a route's `providers` array accidentally provides the service again, the test fails.

## 367: How do you test route-level providers?

Add `providers` to a route and check that components under that route get the route's instance, and components outside don't.

```ts
provideRouter([
  {
    path: "admin",
    providers: [{ provide: Theme, useValue: "dark" }],
    component: AdminComponent,
  },
  { path: "home", component: HomeComponent },
]);

await harness.navigateByUrl("/admin");
expect(harness.routeDebugElement!.injector.get(Theme)).toBe("dark");
```

## 368: How do you test a router redirectTo function?

Redirect functions can use `inject()`, so test them through navigation.

```ts
provideRouter([
  {
    path: "",
    pathMatch: "full",
    redirectTo: () => (inject(Auth).isAdmin() ? "/admin" : "/home"),
  },
  { path: "admin", component: AdminComponent },
  { path: "home", component: HomeComponent },
]);

const harness = await RouterTestingHarness.create("/");
expect(TestBed.inject(Router).url).toBe("/home");
```

## 369: How do you test navigation errors and the router's error handling?

Use `withNavigationErrorHandler` or listen to `NavigationError`, then navigate to a route whose guard or resolver throws.

```ts
const errors: unknown[] = [];
provideRouter(
  routes,
  withNavigationErrorHandler((e) => errors.push(e.error)),
);

const harness = await RouterTestingHarness.create();
await harness.navigateByUrl("/broken").catch(() => {});
expect(errors.length).toBe(1);
```

## 370: How do you test view transitions in the router?

`withViewTransitions()` uses `document.startViewTransition`, which jsdom doesn't have. The router skips view transitions when the API is missing, so navigation still works in unit tests.

Test the callback logic (`onViewTransitionCreated`) by calling it with a fake transition, and check the visual result in a real browser.

## 371: How do you test a scroll restoration or anchor scrolling setup?

jsdom doesn't do layout or real scrolling, so unit tests can only check that `ViewportScroller` methods were called.

```ts
const scroller = {
  scrollToPosition: vi.fn(),
  scrollToAnchor: vi.fn(),
  setOffset: vi.fn(),
};
providers: [{ provide: ViewportScroller, useValue: scroller }];
```

Real scroll positions should be checked in E2E tests.

## 372: How do you test a component that reacts to element size?

Wrap `ResizeObserver` in a service or directive that emits sizes, then fake it in tests.

```ts
const size$ = new Subject<number>();
providers: [{ provide: ElementSize, useValue: { width$: () => size$ } }];

size$.next(300);
await fixture.whenStable();
expect(fixture.nativeElement.classList).toContain("compact");
```

Test the real observer wiring once in browser mode.

## 373: When should you use Vitest browser mode instead of E2E tests?

Browser mode still tests one component or service in isolation, with full control over providers and fakes, but in a real browser engine. Use it for components that need real layout, focus, CSS or browser APIs.

E2E tests run the whole built app with routing and backend. Use them for full user flows and integration with the server.

## 374: How do you run the same component test in several browsers?

With Vitest browser mode, list several browsers.

```bash
ng test --browsers=chromium,firefox,webkit
```

With Playwright as the provider this covers Chromium, Firefox and WebKit. It's slower, so many teams run one browser on every PR and all browsers nightly.

## 375: How do you test CSS that changes with a container query or media query?

jsdom ignores layout and doesn't evaluate media or container queries. Use Vitest browser mode and check `getComputedStyle`. For a container query, change the width of the container element:

```ts
// in browser mode
fixture.nativeElement.style.width = "400px";
await fixture.whenStable();
const style = getComputedStyle(fixture.nativeElement.querySelector(".menu"));
expect(style.display).toBe("none");
```

For media queries you need to change the viewport itself, which Vitest's browser API supports through `page.viewport(width, height)`. Visual regression tests are another good fit for CSS behavior.

## 376: What is visual regression testing and how is it done for Angular?

Visual regression testing takes screenshots of components or pages and compares them with approved ones. Small unexpected pixel differences fail the test.

Common tools: Playwright's `toHaveScreenshot`, Storybook with Chromatic, and Vitest browser mode screenshots. Keep fonts, data, animations and viewport fixed, or the screenshots will differ on every run.

## 377: How do you write a good Playwright E2E test for an Angular app?

- Use role and label locators (`getByRole`, `getByLabel`), not CSS paths
- Let Playwright's auto-waiting do the work, don't add fixed `waitForTimeout`
- Mock or seed the backend so data is predictable
- Keep each test independent, with its own login and data
- Test user flows, not every edge case

```ts
import { test, expect } from "@playwright/test";

test("user can add a todo", async ({ page }) => {
  await page.goto("/");
  await page.getByLabel("New todo").fill("Write tests");
  await page.getByRole("button", { name: "Add" }).click();
  await expect(page.getByRole("listitem")).toHaveText(["Write tests"]);
});
```

## 378: How do you mock the backend in Playwright E2E tests?

Use `page.route` to intercept requests and return fixed responses.

```ts
await page.route("**/api/products", (route) =>
  route.fulfill({ json: [{ id: 1, name: "Pen" }] }),
);
await page.goto("/products");
await expect(page.getByText("Pen")).toBeVisible();
```

Mocked E2E tests are fast and stable. Keep a smaller set of tests against a real backend to catch integration problems.

## 379: How do you handle login in E2E tests efficiently?

Log in once in a setup step, save the browser storage state, and reuse it in tests.

```ts
// auth.setup.ts
test("login", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill("test@example.com");
  await page.getByLabel("Password").fill(process.env.E2E_PASSWORD!);
  await page.getByRole("button", { name: "Sign in" }).click();
  await page.context().storageState({ path: ".auth/user.json" });
});
```

Then set `storageState: '.auth/user.json'` in the Playwright project config. Have one test that covers the real login UI.

## 380: How do you test an Angular app with Cypress?

Cypress runs E2E tests and also has component testing for Angular, where it mounts a single component in a real browser.

```ts
import { mount } from "cypress/angular";

it("increments", () => {
  mount(CounterComponent);
  cy.contains("button", "Add").click();
  cy.contains("Count: 1");
});
```

Check that the Cypress version you use supports your Angular version, since the component testing adapter follows Angular releases.

## 381: How do you keep E2E tests from being flaky?

- Wait for conditions, not time (web-first assertions like `toBeVisible`)
- Control data: seed or mock it
- Avoid tests that depend on each other
- Use stable locators (roles, labels, `data-testid`)
- Turn off or speed up animations
- Run in a clean browser context per test
- Use traces and videos to debug failures in CI

## 382: When should you use data-testid?

Use it when there's no good accessible way to find an element, for example a chart canvas or a layout wrapper. For buttons, inputs and links, prefer role and label queries, since they also check accessibility.

Don't put `data-testid` on everything. It adds noise to the markup and lets tests ignore how users actually find things.

## 383: How do you test the production build specifically?

Run E2E or smoke tests against `ng build` output served by a static server or your real SSR server. The production build has optimizations (minification, tree shaking, no dev mode checks) that can expose bugs unit tests won't catch, like code relying on class names that get minified.

Many teams run E2E against a preview deployment for each PR.

## 384: What are dev mode checks and why do they matter in tests?

In dev mode (which tests use), Angular runs extra checks: the second change detection pass for `ExpressionChanged...` errors, signal write checks, and more helpful error messages. These are removed in production builds.

They're good in tests because they catch bugs early. But it also means a test passing in dev mode doesn't fully prove prod behavior, which is why a few E2E tests on the prod build are useful.

## 385: How do you test that a component doesn't write signals during rendering?

Angular throws an error if you write to a signal inside a template or `computed`. Just render the component in a test, and the error fails it.

```ts
it("renders without signal write errors", async () => {
  const fixture = TestBed.createComponent(SummaryComponent);
  await fixture.whenStable(); // fails the test if a signal is written during rendering
});
```

Any normal render test already covers this, since TestBed rethrows the error.

## 386: How do you test an infinite change detection loop?

Angular stops after too many change detection rounds in zoneless mode and reports an error (NG0103 in recent versions). A test that renders the buggy component fails with that error.

Typical causes are effects or `afterEveryRender` callbacks that write signals read by the template. Fix by moving the logic to `computed` or `linkedSignal`.

## 387: How do you test that OnPush children don't re-render unnecessarily?

Count something that happens on render, like a pipe or method call, then change unrelated state.

```ts
const spy = vi.spyOn(ChildComponent.prototype, "format");
await fixture.whenStable();
spy.mockClear();

fixture.componentInstance.unrelated.set("x");
await fixture.whenStable();
expect(spy).not.toHaveBeenCalled();
```

Calling methods from templates is itself a smell, so this test is more useful as a guard after a performance fix.

## 388: How do you test a service that uses Web Workers?

jsdom doesn't support real workers. Split the work:

- Put the worker's logic in a plain function and unit test it directly
- In the service, inject a worker factory and fake it in tests, simulating `postMessage` and `onmessage`
- Test the real worker in browser mode or E2E

```ts
const fakeWorker = {
  postMessage: vi.fn(),
  onmessage: null as ((e: MessageEvent) => void) | null,
  terminate: vi.fn(),
};
providers: [{ provide: WORKER_FACTORY, useValue: () => fakeWorker }];
```

## 389: How do you test code that uses IndexedDB?

Use `fake-indexeddb` in Node, which gives a working in-memory IndexedDB, or wrap storage behind a service and fake it.

```ts
// test-setup.ts
import "fake-indexeddb/auto";
```

Clear the database between tests, since it lives for the whole test file.

## 390: How do you test offline behavior?

In unit tests, fake the network status service and HTTP errors (`req.error(new ProgressEvent('error'))`). In E2E, Playwright can set the context offline.

```ts
await context.setOffline(true);
await page.getByRole("button", { name: "Save" }).click();
await expect(page.getByText("You are offline")).toBeVisible();
```

## 391: How do you test a component library's harness itself?

Write tests for the harness using a host component, so you know it works before consumers rely on it.

```ts
it("reads and sets value", async () => {
  const fixture = TestBed.createComponent(HostWithCounterComponent);
  const counter =
    await TestbedHarnessEnvironment.loader(fixture).getHarness(CounterHarness);

  await counter.increment();
  expect(await counter.getValue()).toBe(1);
});
```

Harness tests are part of the library's public API tests.

## 392: How does TestbedHarnessEnvironment handle change detection?

Before each harness read and after each action, it runs change detection and waits for the fixture to be stable. That's why harness methods are async.

You can batch actions with `manualChangeDetection` and `parallel` from `@angular/cdk/testing` to avoid extra rounds when reading many values.

```ts
import { parallel } from "@angular/cdk/testing";

const [a, b] = await parallel(() => [harnessA.getText(), harnessB.getText()]);
```

## 393: What is TestElement in the CDK testing API?

`TestElement` is an abstraction over a DOM element that works in any harness environment. It has async methods like `click()`, `sendKeys()`, `text()`, `getAttribute()`, `hasClass()` and `getCssValue()`.

Harnesses get `TestElement`s through locators, which keeps them free of direct DOM access, so they can work in unit and E2E environments.

## 394: How do you test a component with a lot of inputs in combination?

Avoid writing every combination by hand. Pick:

- Each input's important values on its own
- Known risky combinations from bugs or requirements
- A small table driven test (`it.each`) for combinations that matter

For really complex input spaces, property-based testing with `fast-check` can generate many combinations for pure logic.

## 395: What is property-based testing and where does it fit?

Property-based testing generates many random inputs and checks that a rule always holds, for example "sorting twice is the same as sorting once". When it finds a failing input, it shrinks it to the smallest case.

```ts
import fc from "fast-check";

it("slugify never returns spaces", () => {
  fc.assert(fc.property(fc.string(), (s) => !slugify(s).includes(" ")));
});
```

It fits pure functions like parsers, validators and formatters, not DOM heavy components.

## 396: How do you test a complex multi-step form wizard?

- Unit test step validation and navigation logic in a service or store
- Component test each step on its own
- One integration test that goes through all steps with fake HTTP
- Test going back keeps data, and invalid steps block "Next"
- Test resume after reload if state is persisted

```ts
await wizard.fillStep1({ name: "Ana" });
await wizard.next();
await wizard.back();
expect(await wizard.getName()).toBe("Ana");
```

A custom harness or page object makes these tests readable.

## 397: How do you test optimistic updates?

Check the UI updates before the server answers, then check rollback when the request fails.

```ts
fixture.nativeElement.querySelector(".like").click();
await fixture.whenStable();
expect(likes()).toBe(11); // updated right away

httpMock
  .expectOne("/api/like")
  .flush(null, { status: 500, statusText: "Error" });
await fixture.whenStable();
expect(likes()).toBe(10); // rolled back
```

## 398: How do you test undo and redo logic?

Keep it in a store or service and test sequences of actions.

```ts
const store = TestBed.inject(EditorStore);
store.type("a");
store.type("b");
store.undo();
expect(store.text()).toBe("a");
store.redo();
expect(store.text()).toBe("ab");
store.undo();
store.type("c");
store.redo(); // redo stack cleared
expect(store.text()).toBe("ac");
```

## 399: How do you test pagination?

Check the request params for each page and the UI controls.

```ts
fixture.nativeElement.querySelector(".next").click();
const req = httpMock.expectOne((r) => r.url === "/api/items");
expect(req.request.params.get("page")).toBe("2");
req.flush({ items: [], total: 40 });

await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".next").disabled).toBe(true);
```

Test the edges: first page, last page, empty results and a total that changes.

## 400: How do you test infinite scroll?

The logic (load next page when a sentinel is visible) depends on `IntersectionObserver`. Wrap it in a directive that emits an event, fake or trigger that event in tests, and check that the next page is requested only once while loading.

```ts
const sentinel = fixture.debugElement.query(By.directive(InViewDirective));
sentinel.triggerEventHandler("inView", true);
sentinel.triggerEventHandler("inView", true);
expect(httpMock.match("/api/feed?page=2").length).toBe(1);
```

Test real scrolling in E2E.

## 401: How do you test drag and drop with real pointer events?

In browser mode or E2E, use the tool's built-in drag helpers.

```ts
// Playwright
await page.getByText("Task A").dragTo(page.getByTestId("done-column"));
await expect(page.getByTestId("done-column")).toContainText("Task A");
```

CDK drag and drop listens to mouse and touch events with real coordinates, so jsdom can't simulate it well.

## 402: How do you test a component that uses the Clipboard API?

Fake the CDK `Clipboard` service or `navigator.clipboard`.

```ts
const clipboard = { copy: vi.fn().mockReturnValue(true) };
providers: [{ provide: Clipboard, useValue: clipboard }];

fixture.nativeElement.querySelector(".copy").click();
expect(clipboard.copy).toHaveBeenCalledWith("https://example.com/invite/abc");
```

The real clipboard needs permissions and focus, so leave it to E2E.

## 403: How do you test file input and file reading?

Create a `File`, set it on the input with a `DataTransfer` or by defining `files`, and dispatch `change`.

```ts
const file = new File(["name,age\nAna,30"], "people.csv", { type: "text/csv" });
const input: HTMLInputElement =
  fixture.nativeElement.querySelector("input[type=file]");
Object.defineProperty(input, "files", { value: [file] });
input.dispatchEvent(new Event("change"));

await vi.waitFor(() => expect(fixture.componentInstance.rows().length).toBe(1));
```

`vi.waitFor` retries the check until it passes, which helps with `FileReader` being async.

## 404: How do you test downloads triggered by the app?

In unit tests, fake the parts: spy on `URL.createObjectURL` and check that an anchor with `download` was clicked.

```ts
URL.createObjectURL = vi.fn(() => "blob:1");
const click = vi
  .spyOn(HTMLAnchorElement.prototype, "click")
  .mockImplementation(() => {});

service.downloadCsv([{ a: 1 }]);
expect(click).toHaveBeenCalled();
```

In Playwright E2E, use `page.waitForEvent('download')` and check the file name and content.

## 405: How do you test i18n with multiple locales?

Built-in Angular i18n builds a separate app per locale, so unit tests usually run in the source locale. For translations, run E2E tests against each localized build, or at least check that all translation files have every ID (the extractor and build fail on missing translations if configured).

With runtime libraries like Transloco or ngx-translate, provide a testing loader with fixed translations in unit tests.

## 406: How do you test that a component works with right-to-left layout?

Provide the `Directionality` with `rtl` (CDK) or set `dir="rtl"` on a host element, and check the component reacts.

```ts
providers: [
  { provide: Directionality, useValue: { value: "rtl", change: of("rtl") } },
];

await fixture.whenStable();
expect(fixture.nativeElement.querySelector(".arrow").classList).toContain(
  "arrow-left",
);
```

Real visual RTL checks belong in screenshot tests.

## 407: How do you test the TestBed teardown behavior itself?

You rarely need to, but you can check that resources are released, for example that `ngOnDestroy` runs after a test. With `destroyAfterEach: false`, components stay alive and DOM nodes pile up, which can cause leaks and cross-test effects.

If an old suite set `destroyAfterEach: false` to avoid errors, turning it back on often reveals components that throw in `ngOnDestroy` or tests that rely on leftovers.

## 408: How do you fix tests that break when destroyAfterEach is enabled?

Common causes:

- `ngOnDestroy` throws because something was never initialized
- Tests use a fixture created in a previous test
- Global listeners or intervals aren't cleaned
- Third party libraries attach to `document.body` and expect it to persist

Fix the component cleanup (guard against undefined), create fixtures per test, and clean globals in `afterEach`. Turn it off for specific specs only as a temporary step.

## 409: How do you share TestBed configuration across a big project?

- A `providersFile` or setup file for providers every test needs (for example `provideZonelessChangeDetection()` or locale)
- Small helper functions per feature (`setupCheckoutPage()`)
- Shared fake classes in a `testing` entry point for each library
- Avoid a giant "TestingModule" that imports everything, since it makes tests slow and hides what each one needs

## 410: How do you test a library's secondary entry point like my-lib/testing?

Libraries often ship a `testing` entry point with harnesses and fakes. Test that entry point like any code, and make sure it doesn't depend on the test runner (no `vi` or `jasmine` imports), so consumers using either runner can use it.

```ts
// my-lib/testing/fake-auth.ts
export class FakeAuthService implements Pick<AuthService, "user" | "login"> {
  user = signal<User | null>(null);
  login(u: User) {
    this.user.set(u);
  }
}
```

## 411: How do you write fakes that work with both Jasmine and Vitest?

Write fakes as plain classes or functions with real logic, not spies. Tests then wrap methods with their own runner's spy if they need call tracking.

```ts
const fake = new FakeAuthService();
vi.spyOn(fake, "login"); // Vitest
// spyOn(fake, 'login').and.callThrough(); // Jasmine
```

This keeps shared testing code independent of the test framework.

## 412: How do you test a component that uses a global CSS class from a design system?

Unit tests don't load global styles by default, so you check classes, not looks. If you need styles in browser mode, add them through the builder's styles setting or import the CSS in a setup file.

Visual checks for design system usage are better done in Storybook or screenshot tests.

## 413: How do you test components with Storybook?

Write stories for each component state, then add interaction tests with the `play` function. Storybook's test runner or its Vitest integration runs them as tests.

```ts
export const Filled: Story = {
  args: { value: "Ana" },
  play: async ({ canvas, userEvent }) => {
    await userEvent.clear(canvas.getByRole("textbox"));
    await expect(canvas.getByText("Required")).toBeInTheDocument();
  },
};
```

Stories double as documentation and visual test cases.

## 414: How do you measure the quality of a test suite beyond coverage?

- Mutation score (how many mutants tests kill)
- Number of bugs that reached production without a failing test
- Flaky test rate
- Suite run time
- How often tests break on refactors without real bugs

A good suite catches real bugs, runs fast, and rarely fails for no reason.

## 415: How do you test code that depends on random values?

Inject the random source, or mock `Math.random`.

```ts
vi.spyOn(Math, "random").mockReturnValue(0.5);
expect(pickColor(["red", "green", "blue"])).toBe("green");
```

For IDs, inject an ID generator and use a counter in tests, so outputs and snapshots are stable.

## 416: How do you test crypto.randomUUID usage?

Wrap it, or stub it per test.

```ts
vi.spyOn(crypto, "randomUUID").mockReturnValue(
  "00000000-0000-0000-0000-000000000001",
);
store.add("Task");
expect(store.items()[0].id).toBe("00000000-0000-0000-0000-000000000001");
```

## 417: How do you test analytics tracking without coupling tests to it?

Put tracking behind a service and fake it. Test only the important events, with a helper that checks event name and key fields.

```ts
expect(analytics.track).toHaveBeenCalledWith(
  "checkout_completed",
  expect.objectContaining({ total: 50 }),
);
```

Avoid asserting every analytics call in every component test, or simple UI changes will break many tests.

## 418: How do you test a component that should be lazy loaded with @defer on viewport?

In unit tests, use manual defer behavior to check placeholder and complete states. The `on viewport` trigger depends on `IntersectionObserver`, so with playthrough in jsdom it may never fire.

Check the real trigger in browser mode or E2E, including that the chunk isn't loaded before scrolling (watch network requests in Playwright).

## 419: How do you test that a lazy chunk isn't in the initial bundle?

That's a build concern, not a unit test. Check it with:

- `ng build --stats-json` and a bundle analyzer
- Bundle budgets in `angular.json`
- E2E tests that record network requests and check the chunk loads only after the trigger

Budgets fail the build when bundles grow, which guards against someone importing a lazy feature eagerly.

## 420: How do you test a custom RouteReuseStrategy?

Test the class methods directly with fake snapshots, then add a navigation test that checks a component instance is reused.

```ts
await harness.navigateByUrl("/list");
const first = harness.routeDebugElement!.componentInstance;
await harness.navigateByUrl("/detail/1");
await harness.navigateByUrl("/list");
expect(harness.routeDebugElement!.componentInstance).toBe(first);
```

## 421: How do you test a custom UrlSerializer or UrlMatcher?

Both are plain functions or classes, so test them directly with sample URLs, then add a routing test.

```ts
const matcher: UrlMatcher = (segments) =>
  segments.length === 1 && segments[0].path.startsWith("@")
    ? {
        consumed: segments,
        posParams: { user: new UrlSegment(segments[0].path.slice(1), {}) },
      }
    : null;

expect(
  matcher([new UrlSegment("@ana", {})], {} as UrlSegmentGroup, {} as Route)
    ?.posParams?.["user"].path,
).toBe("ana");
```

## 422: How do you test a long-running Observable stream that never completes?

Don't wait for completion. Take the values you need or check after each emission.

```ts
const values: number[] = [];
const sub = service.ticks$.subscribe((v) => values.push(v));

vi.useFakeTimers();
await vi.advanceTimersByTimeAsync(3000);
sub.unsubscribe();

expect(values).toEqual([0, 1, 2]);
```

`firstValueFrom` with `take(n)` is another option.

## 423: How do you test retry with backoff?

Use fake timers and fail requests a few times, checking the delay between retries.

```ts
vi.useFakeTimers();
service.load().subscribe();

httpMock.expectOne("/api/data").flush(null, { status: 503, statusText: "" });
await vi.advanceTimersByTimeAsync(999);
httpMock.expectNone("/api/data");
await vi.advanceTimersByTimeAsync(1);
httpMock.expectOne("/api/data").flush({ ok: true });
```

Marble tests are also a good fit for backoff logic.

## 424: How do you test an observable created with shareReplay?

Check that multiple subscribers share one request, and decide whether errors and late subscribers behave as you want.

```ts
const data$ = service.config$;
data$.subscribe();
data$.subscribe();
httpMock.expectOne("/api/config").flush({ a: 1 });

let late: unknown;
data$.subscribe((v) => (late = v));
expect(late).toEqual({ a: 1 });
```

Also test `refCount` behavior if you use it, since it decides whether the request repeats after everyone unsubscribes.

## 425: What makes a test "brittle" and how do you avoid it?

A brittle test fails after changes that don't change behavior. Causes:

- Deep CSS selectors tied to markup
- Asserting exact call counts on internal methods
- Large snapshots
- Testing private fields
- Hard-coded order of unrelated items

Prefer user-facing queries, assert results not steps, and keep each test focused on one behavior.

## 426: How do you review tests in a pull request?

Check that:

- The tests fail without the change (or at least would)
- Names describe behavior
- Edge cases and error paths are covered
- No focused or skipped tests left
- Fakes match the real API types
- No real timers, network calls or random data
- Tests aren't just copying the implementation logic

## 427: How do you test code that copies the implementation instead of checking it?

That's a test smell: the test computes the expected value with the same formula as the code, so a wrong formula passes both.

```ts
// bad
expect(tax(100)).toBe(100 * TAX_RATE);
// good
expect(tax(100)).toBe(18);
```

Use concrete expected values that you worked out by hand.

## 428: How do you test Angular's built-in pipes in your templates without retesting the pipes?

Don't test that `DatePipe` formats dates. Test that your template uses the right pipe and format, by checking the output for one known input.

One assertion per formatting choice is enough, and it catches someone changing `'short'` to `'medium'` by mistake.

## 429: How do you approach testing legacy NgModule-based code before migrating to standalone?

Add characterization tests first: tests that record what the current code does, even if it's odd. Use `declarations` and module imports to set up TestBed like the real module.

Then migrate with `ng g @angular/core:standalone`, and run the same tests. Most tests only need to move components from `declarations` to `imports`.

## 430: How do you migrate old Jasmine tests to Vitest at scale?

1. Run the Angular schematic `refactor-jasmine-vitest` to convert most syntax.
2. Fix leftovers by hand: custom matchers, `jasmine.clock`, `done` callbacks, `fakeAsync`.
3. Decide on zoneless or keep `zone.js/testing` for now.
4. Compare test counts before and after, to be sure no specs were skipped.
5. Migrate per library or folder if the project is big, keeping both runners until done.

## 431: What are custom matchers and when do you write them?

Custom matchers wrap common checks in a clear name, like `toHaveText` or `toBeValidEmail`. In Vitest you add them with `expect.extend`.

```ts
expect.extend({
  toHaveText(el: Element, text: string) {
    const actual = el.textContent?.trim();
    return {
      pass: actual === text,
      message: () => `expected "${actual}" to be "${text}"`,
    };
  },
});
```

Add a TypeScript declaration so the matcher is typed. `@testing-library/jest-dom` gives many DOM matchers ready made and works with Vitest.

## 432: How do you test that a component cleans up DOM it added to document.body?

Count nodes before creating and after destroying.

```ts
const before = document.body.children.length;
const fixture = TestBed.createComponent(PopoverComponent);
fixture.componentInstance.open();
await fixture.whenStable();

fixture.destroy();
expect(document.body.children.length).toBe(before);
```

## 433: How do you test a signal-based store with async methods?

Call the method, resolve the fake, then check the state at each step.

```ts
const api = { load: vi.fn() };
let resolve!: (v: Item[]) => void;
api.load.mockReturnValue(new Promise<Item[]>((r) => (resolve = r)));

const store = TestBed.inject(ItemStore);
const done = store.load();
expect(store.loading()).toBe(true);

resolve([{ id: 1 }]);
await done;
expect(store.loading()).toBe(false);
expect(store.items()).toEqual([{ id: 1 }]);
```

## 434: How do you test concurrency rules in an rxMethod or effect?

Fire several triggers quickly and check which requests were kept. For `switchMap`, earlier ones are cancelled. For `exhaustMap`, later ones are ignored while one is running.

```ts
store.save(a);
store.save(b);
expect(httpMock.match("/api/save").length).toBe(1); // exhaustMap ignores the second
```

These tests document an important design choice that's easy to change by accident.

## 435: How do you test that a component works with both default and custom injection tokens?

Write one test without providing the token (uses its factory default), and one with an override.

```ts
it("uses default page size", () => {
  expect(TestBed.inject(PAGE_SIZE)).toBe(20);
});

it("uses custom page size", () => {
  TestBed.overrideProvider(PAGE_SIZE, { useValue: 50 });
  expect(TestBed.inject(PAGE_SIZE)).toBe(50);
});
```

## 436: How do you test code that branches on isDevMode()?

`isDevMode()` is true in tests. To test the production branch, inject a flag instead of calling `isDevMode()` directly.

```ts
export const IS_DEV = new InjectionToken<boolean>("IS_DEV", {
  factory: () => isDevMode(),
});

providers: [{ provide: IS_DEV, useValue: false }];
```

This keeps both branches testable without a production build.

## 437: How do you test Angular schematics?

Use `SchematicTestRunner` from `@angular-devkit/schematics/testing`, run the schematic on a virtual tree, and check the files.

```ts
const runner = new SchematicTestRunner(
  "my-lib",
  require.resolve("../collection.json"),
);
const tree = await runner.runSchematic("ng-add", { project: "app" }, appTree);

expect(tree.readContent("/angular.json")).toContain("my-lib");
```

`appTree` is usually created by running Angular's own `workspace` and `application` schematics first.

## 438: How do you test custom builders?

Use `@angular-devkit/architect/testing` with a test architect host, or keep the builder logic in plain functions and test those. Integration test by running `ng run project:target` on a small fixture workspace in CI.

Builders are rare in app code, so most teams only need this in tooling libraries.

## 439: How do you test a custom ESLint rule for Angular templates?

`angular-eslint` rules can be tested with ESLint's `RuleTester` (or `@angular-eslint/test-utils`), giving valid and invalid code samples.

```ts
ruleTester.run("no-inline-styles", rule, {
  valid: [{ code: '<div class="a"></div>' }],
  invalid: [
    {
      code: '<div style="color:red"></div>',
      errors: [{ messageId: "noInline" }],
    },
  ],
});
```

Template rules need the template parser set in the tester config.

## 440: How do you balance test speed and confidence in CI?

A common setup:

- On every commit: lint, type check, unit tests in jsdom, affected only
- On pull requests: plus integration tests and a small E2E smoke suite
- On main or nightly: full E2E in all browsers, visual tests, mutation tests

Fail fast with the cheapest checks first, and keep the PR pipeline under about 10-15 minutes.

## 441: How do you test that deprecated APIs aren't used in tests?

Use lint rules, for example `@typescript-eslint/no-deprecated` or `eslint-plugin-deprecation`, which flag deprecated imports like `HttpClientTestingModule` or `RouterTestingModule`.

Running `ng update` also applies migrations for many deprecated test APIs, so keep the project updated.

## 442: How do you test with real Angular Material theming and density?

Unit tests normally run without theme CSS. For theming, use browser mode with the theme styles loaded, or Storybook with visual tests.

Check computed values (`getComputedStyle`) of a few key tokens rather than many pixel checks, and use screenshots for overall look.

## 443: What is the role of TestBed in component tests versus plain class tests?

TestBed gives you the real Angular runtime: DI, templates, change detection, lifecycle hooks and DOM. Plain class tests (`new MyComponent()`) skip all of that.

Plain class tests are fast but miss template bugs and fail if the class uses `inject()`. For components, use TestBed. For pure logic, extract functions and test them without TestBed.

## 444: How do you test what happens when a required dependency throws during construction?

Provide a fake that throws and check that creating the component fails in the expected way, or that an error boundary-like fallback shows.

```ts
providers: [
  {
    provide: Config,
    useFactory: () => {
      throw new Error("No config");
    },
  },
];

expect(() => TestBed.createComponent(AppShellComponent)).toThrow("No config");
```

## 445: How do you test multiple app-wide states like logged in, logged out and expired session?

Create a setup helper that builds TestBed with a given auth state, and run the same behavior checks for each.

```ts
type AuthState = "in" | "out" | "expired";

function setup(state: AuthState) {
  TestBed.configureTestingModule({
    imports: [HeaderComponent],
    providers: [
      { provide: Auth, useValue: fakeAuth(state) },
      provideRouter([]),
    ],
  });
  return TestBed.createComponent(HeaderComponent);
}
```

Combine it with `it.each` to keep the cases visible.

## 446: How do you test that an app still boots with its real providers?

Write a test that uses the real `appConfig`, with only HTTP faked, and renders the root component.

```ts
TestBed.configureTestingModule({
  imports: [AppComponent],
  providers: [
    ...appConfig.providers,
    provideHttpClientTesting(),
    provideLocationMocks(),
  ],
});

const harness = await RouterTestingHarness.create("/");
expect(harness.routeNativeElement).not.toBeNull();
```

It catches provider mistakes in `app.config.ts` that unit tests with fakes would miss.

## 447: How would you test a dashboard page with many widgets that load in parallel?

- Fake each widget's data source separately
- Test that each widget shows its own loading, error and empty state
- Test that one failing widget doesn't break the page
- Use `@defer` manual behavior if widgets are deferred
- One integration test with all HTTP calls flushed in random order

```ts
httpMock.expectOne("/api/sales").flush(sales);
httpMock.expectOne("/api/users").flush(null, { status: 500, statusText: "" });
await fixture.whenStable();
expect(page.salesChart).toBeTruthy();
expect(page.usersError.textContent).toContain("Could not load");
```

## 448: A test passes alone but fails when the whole suite runs. How do you investigate?

1. Run the file alone, then with the file that runs before it, to find the culprit.
2. Turn on shuffle to see if it's order related.
3. Look for state that survives tests: module variables, singletons outside DI, globals on `window`, `localStorage`, cookies, fake timers, spies not restored, `customElements.define`.
4. Check `destroyAfterEach` isn't turned off.
5. Fix cleanup in the polluting test, not just the failing one.

## 449: A component test is very slow. What do you check?

- Real timers or `await` on long delays
- Heavy child components or libraries that could be stubbed
- Large fixtures or deep object graphs created in `beforeEach`
- Unneeded `compileComponents` with external resources in non-CLI setups
- Many tests each creating the full page when a smaller unit would do
- Harness calls in loops instead of `parallel`

Profile with Vitest's per-test timings to find the worst offenders first.

## 450: How would you introduce testing standards to an Angular team?

- Agree on the tools: Vitest, TestBed, harnesses or Testing Library, Playwright for E2E
- Write a short testing guide with examples for common cases: services, HTTP, forms, routing, signals
- Provide shared helpers and typed fakes
- Add lint rules against focused tests and deprecated testing APIs
- Set coverage thresholds as a floor, not a goal
- Require tests for bug fixes
- Review tests in PRs like production code

Start small and improve the guide as the team finds new patterns.
