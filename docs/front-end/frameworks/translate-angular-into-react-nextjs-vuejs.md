# Translate Angular into React, Next.js and Vue.js Interview Questions and Answers

_Last updated: November 24, 2026_

450 interview questions about translating Angular code into React, Next.js and Vue.js, split into three levels: 150 easy, 150 moderate and 150 advanced. Every answer shows the same idea in each framework, in this order: Angular, React, Next.js, Vue.js.

The answers target modern versions: Angular 20+ (standalone components, signals, `inject()`, built-in control flow, zoneless change detection, signal forms), React 19, Next.js 16 with the App Router, and Vue 3.5+ with `<script setup>`. When an answer has no Next.js block, the React code works the same way in Next.js. Just put it in a client component (add `"use client"` at the top of the file) if it uses state, effects or event handlers.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What does it mean to translate an Angular app into React, Next.js or Vue.js?](#1-what-does-it-mean-to-translate-an-angular-app-into-react-nextjs-or-vuejs)
- [2: How are Angular, React, Next.js and Vue.js different in nature?](#2-how-are-angular-react-nextjs-and-vuejs-different-in-nature)
- [3: How do you create a new project in each framework?](#3-how-do-you-create-a-new-project-in-each-framework)
- [4: How does the project structure differ?](#4-how-does-the-project-structure-differ)
- [5: How is the app bootstrapped in each framework?](#5-how-is-the-app-bootstrapped-in-each-framework)
- [6: How do you write the simplest component?](#6-how-do-you-write-the-simplest-component)
- [7: How do Angular templates compare to JSX and Vue templates?](#7-how-do-angular-templates-compare-to-jsx-and-vue-templates)
- [8: How do you translate text interpolation?](#8-how-do-you-translate-text-interpolation)
- [9: How do you translate property binding?](#9-how-do-you-translate-property-binding)
- [10: How do you translate attribute binding like attr.aria-label?](#10-how-do-you-translate-attribute-binding-like-attraria-label)
- [11: How do you translate class binding?](#11-how-do-you-translate-class-binding)
- [12: How do you translate style binding?](#12-how-do-you-translate-style-binding)
- [13: How do you translate event binding?](#13-how-do-you-translate-event-binding)
- [14: How do you access the event object?](#14-how-do-you-access-the-event-object)
- [15: How do you translate two-way binding on an input?](#15-how-do-you-translate-two-way-binding-on-an-input)
- [16: How do you translate @if?](#16-how-do-you-translate-if)
- [17: How do you translate @if with @else?](#17-how-do-you-translate-if-with-else)
- [18: How do you translate @switch?](#18-how-do-you-translate-switch)
- [19: How do you translate @for?](#19-how-do-you-translate-for)
- [20: How does track in Angular compare to key in React and Vue?](#20-how-does-track-in-angular-compare-to-key-in-react-and-vue)
- [21: How do you translate @empty in a @for loop?](#21-how-do-you-translate-empty-in-a-for-loop)
- [22: How do you translate loop variables like $index, $first and $last?](#22-how-do-you-translate-loop-variables-like-index-first-and-last)
- [23: How do template reference variables translate?](#23-how-do-template-reference-variables-translate)
- [24: How do you translate component inputs?](#24-how-do-you-translate-component-inputs)
- [25: How do you translate required inputs?](#25-how-do-you-translate-required-inputs)
- [26: How do you translate default values for inputs?](#26-how-do-you-translate-default-values-for-inputs)
- [27: How do you translate input transforms like booleanAttribute?](#27-how-do-you-translate-input-transforms-like-booleanattribute)
- [28: How do you translate component outputs?](#28-how-do-you-translate-component-outputs)
- [29: How do you translate model() two-way component binding?](#29-how-do-you-translate-model-two-way-component-binding)
- [30: How do you translate content projection with ng-content?](#30-how-do-you-translate-content-projection-with-ng-content)
- [31: How do you translate multi-slot projection with select?](#31-how-do-you-translate-multi-slot-projection-with-select)
- [32: How do you translate local component state from signal()?](#32-how-do-you-translate-local-component-state-from-signal)
- [33: How do you translate signal.set() and signal.update()?](#33-how-do-you-translate-signalset-and-signalupdate)
- [34: How do you translate computed()?](#34-how-do-you-translate-computed)
- [35: How do you translate effect()?](#35-how-do-you-translate-effect)
- [36: How do you update objects and arrays in state?](#36-how-do-you-update-objects-and-arrays-in-state)
- [37: What replaces ngOnInit in React and Vue?](#37-what-replaces-ngoninit-in-react-and-vue)
- [38: What replaces ngOnDestroy and DestroyRef?](#38-what-replaces-ngondestroy-and-destroyref)
- [39: What replaces ngOnChanges?](#39-what-replaces-ngonchanges)
- [40: What replaces ngAfterViewInit and afterNextRender?](#40-what-replaces-ngafterviewinit-and-afternextrender)
- [41: How do you translate viewChild()?](#41-how-do-you-translate-viewchild)
- [42: How do you focus an input when the component appears?](#42-how-do-you-focus-an-input-when-the-component-appears)
- [43: How do you translate an Angular service?](#43-how-do-you-translate-an-angular-service)
- [44: What replaces inject()?](#44-what-replaces-inject)
- [45: How do you share state between components like a root service?](#45-how-do-you-share-state-between-components-like-a-root-service)
- [46: What replaces Angular pipes?](#46-what-replaces-angular-pipes)
- [47: How do you translate the date and currency pipes?](#47-how-do-you-translate-the-date-and-currency-pipes)
- [48: How do you translate the json pipe used for debugging?](#48-how-do-you-translate-the-json-pipe-used-for-debugging)
- [49: What replaces the async pipe?](#49-what-replaces-the-async-pipe)
- [50: How do you translate a custom pipe?](#50-how-do-you-translate-a-custom-pipe)
- [51: How do you translate an attribute directive?](#51-how-do-you-translate-an-attribute-directive)
- [52: What replaces @HostListener or host event bindings?](#52-what-replaces-hostlistener-or-host-event-bindings)
- [53: How do you translate ngClass?](#53-how-do-you-translate-ngclass)
- [54: How do you translate ngStyle?](#54-how-do-you-translate-ngstyle)
- [55: How do component styles translate?](#55-how-do-component-styles-translate)
- [56: What replaces the :host selector?](#56-what-replaces-the-host-selector)
- [57: How do you add global styles?](#57-how-do-you-add-global-styles)
- [58: How do you set up routing?](#58-how-do-you-set-up-routing)
- [59: How do you translate routerLink?](#59-how-do-you-translate-routerlink)
- [60: How do you translate routerLinkActive?](#60-how-do-you-translate-routerlinkactive)
- [61: How do you read route parameters?](#61-how-do-you-read-route-parameters)
- [62: How do you read query parameters?](#62-how-do-you-read-query-parameters)
- [63: How do you navigate from code?](#63-how-do-you-navigate-from-code)
- [64: How do you translate nested routes and router-outlet?](#64-how-do-you-translate-nested-routes-and-router-outlet)
- [65: How do you translate a wildcard 404 route?](#65-how-do-you-translate-a-wildcard-404-route)
- [66: How do you translate route redirects?](#66-how-do-you-translate-route-redirects)
- [67: How do you translate lazy-loaded routes?](#67-how-do-you-translate-lazy-loaded-routes)
- [68: How do you translate an HTTP GET with HttpClient?](#68-how-do-you-translate-an-http-get-with-httpclient)
- [69: How do you translate an HTTP POST?](#69-how-do-you-translate-an-http-post)
- [70: How do you show loading and error states for a request?](#70-how-do-you-show-loading-and-error-states-for-a-request)
- [71: How do environment files translate?](#71-how-do-environment-files-translate)
- [72: How do you translate a template-driven form field?](#72-how-do-you-translate-a-template-driven-form-field)
- [73: How do you bind a checkbox?](#73-how-do-you-bind-a-checkbox)
- [74: How do you bind a select dropdown?](#74-how-do-you-bind-a-select-dropdown)
- [75: How do you bind radio buttons?](#75-how-do-you-bind-radio-buttons)
- [76: How do you handle form submit?](#76-how-do-you-handle-form-submit)
- [77: How do you prevent default and stop propagation?](#77-how-do-you-prevent-default-and-stop-propagation)
- [78: How do you translate key event filtering like keyup.enter?](#78-how-do-you-translate-key-event-filtering-like-keyupenter)
- [79: How do you translate the required validator?](#79-how-do-you-translate-the-required-validator)
- [80: How do you show validation errors?](#80-how-do-you-show-validation-errors)
- [81: How do you translate a simple reactive form?](#81-how-do-you-translate-a-simple-reactive-form)
- [82: How do you disable a button based on state?](#82-how-do-you-disable-a-button-based-on-state)
- [83: How do you render raw HTML?](#83-how-do-you-render-raw-html)
- [84: What replaces ng-container?](#84-what-replaces-ng-container)
- [85: How do you translate ng-template with ngTemplateOutlet?](#85-how-do-you-translate-ng-template-with-ngtemplateoutlet)
- [86: How do you render a component chosen at runtime?](#86-how-do-you-render-a-component-chosen-at-runtime)
- [87: How do you show and hide an element without removing it?](#87-how-do-you-show-and-hide-an-element-without-removing-it)
- [88: How does the safe navigation operator translate?](#88-how-does-the-safe-navigation-operator-translate)
- [89: How do you translate @let in templates?](#89-how-do-you-translate-let-in-templates)
- [90: How do you import and use a child component?](#90-how-do-you-import-and-use-a-child-component)
- [91: How do naming conventions differ?](#91-how-do-naming-conventions-differ)
- [92: How do NgModules map to React and Vue?](#92-how-do-ngmodules-map-to-react-and-vue)
- [93: How do you pass data through many levels without passing props at every level?](#93-how-do-you-pass-data-through-many-levels-without-passing-props-at-every-level)
- [94: How does a child send data to its parent?](#94-how-does-a-child-send-data-to-its-parent)
- [95: How do sibling components communicate?](#95-how-do-sibling-components-communicate)
- [96: How do you type component props?](#96-how-do-you-type-component-props)
- [97: How do you type component events?](#97-how-do-you-type-component-events)
- [98: How do you write a generic component?](#98-how-do-you-write-a-generic-component)
- [99: How do dev and build commands compare?](#99-how-do-dev-and-build-commands-compare)
- [100: What test tools replace the Angular ones?](#100-what-test-tools-replace-the-angular-ones)
- [101: How do you write the same simple component test?](#101-how-do-you-write-the-same-simple-component-test)
- [102: How do you set up linting?](#102-how-do-you-set-up-linting)
- [103: What browser DevTools replace Angular DevTools?](#103-what-browser-devtools-replace-angular-devtools)
- [104: How do you serve static assets like images?](#104-how-do-you-serve-static-assets-like-images)
- [105: How do you set the page title?](#105-how-do-you-set-the-page-title)
- [106: How do you set meta tags?](#106-how-do-you-set-meta-tags)
- [107: How do you load web fonts?](#107-how-do-you-load-web-fonts)
- [108: How do you translate a timer with setInterval?](#108-how-do-you-translate-a-timer-with-setinterval)
- [109: How do you listen to window resize?](#109-how-do-you-listen-to-window-resize)
- [110: How do you debounce a search input?](#110-how-do-you-debounce-a-search-input)
- [111: How do you save state to localStorage?](#111-how-do-you-save-state-to-localstorage)
- [112: How do you fetch data again when a route parameter changes?](#112-how-do-you-fetch-data-again-when-a-route-parameter-changes)
- [113: How do you translate a counter component end to end?](#113-how-do-you-translate-a-counter-component-end-to-end)
- [114: How do you translate a todo list end to end?](#114-how-do-you-translate-a-todo-list-end-to-end)
- [115: How do you translate a toggle (show more / show less)?](#115-how-do-you-translate-a-toggle-show-more--show-less)
- [116: How do you translate a simple modal dialog?](#116-how-do-you-translate-a-simple-modal-dialog)
- [117: How do you translate a tabs component?](#117-how-do-you-translate-a-tabs-component)
- [118: How do you translate client-side pagination?](#118-how-do-you-translate-client-side-pagination)
- [119: How do you translate a list with a search filter?](#119-how-do-you-translate-a-list-with-a-search-filter)
- [120: How do you translate an accordion?](#120-how-do-you-translate-an-accordion)
- [121: How do you give projected content a fallback?](#121-how-do-you-give-projected-content-a-fallback)
- [122: How do you bind a textarea and a number input?](#122-how-do-you-bind-a-textarea-and-a-number-input)
- [123: How do you translate (ngModelChange)?](#123-how-do-you-translate-ngmodelchange)
- [124: How do you handle a file input?](#124-how-do-you-handle-a-file-input)
- [125: How do you connect a label to an input?](#125-how-do-you-connect-a-label-to-an-input)
- [126: How do you render inline SVG icons?](#126-how-do-you-render-inline-svg-icons)
- [127: How do you add simple enter and leave animations?](#127-how-do-you-add-simple-enter-and-leave-animations)
- [128: How do you translate a global error handler?](#128-how-do-you-translate-a-global-error-handler)
- [129: How do you translate an InjectionToken for config values?](#129-how-do-you-translate-an-injectiontoken-for-config-values)
- [130: Where do app-wide providers go?](#130-where-do-app-wide-providers-go)
- [131: Which UI component libraries replace Angular Material?](#131-which-ui-component-libraries-replace-angular-material)
- [132: Which state management libraries replace NgRx?](#132-which-state-management-libraries-replace-ngrx)
- [133: How do Angular lifecycle hooks map to React and Vue?](#133-how-do-angular-lifecycle-hooks-map-to-react-and-vue)
- [134: What is a quick cheat sheet of template syntax?](#134-what-is-a-quick-cheat-sheet-of-template-syntax)
- [135: What is React Strict Mode and why does my effect run twice?](#135-what-is-react-strict-mode-and-why-does-my-effect-run-twice)
- [136: What does a production build produce in each?](#136-what-does-a-production-build-produce-in-each)
- [137: How do you deploy a static single-page app?](#137-how-do-you-deploy-a-static-single-page-app)
- [138: Which ones render on the server by default?](#138-which-ones-render-on-the-server-by-default)
- [139: What is hydration?](#139-what-is-hydration)
- [140: What is the difference between Server and Client Components in Next.js?](#140-what-is-the-difference-between-server-and-client-components-in-nextjs)
- [141: When is Next.js the wrong target for an Angular app?](#141-when-is-nextjs-the-wrong-target-for-an-angular-app)
- [142: What is a common mistake with state when coming from Angular?](#142-what-is-a-common-mistake-with-state-when-coming-from-angular)
- [143: Why does reading state right after setting it show the old value in React?](#143-why-does-reading-state-right-after-setting-it-show-the-old-value-in-react)
- [144: How do you keep a component's state when hiding it?](#144-how-do-you-keep-a-components-state-when-hiding-it)
- [145: How do you reset a component's state when an input changes?](#145-how-do-you-reset-a-components-state-when-an-input-changes)
- [146: What files do you create first when translating a small Angular component?](#146-what-files-do-you-create-first-when-translating-a-small-angular-component)
- [147: How do you translate this in class methods?](#147-how-do-you-translate-this-in-class-methods)
- [148: How do you translate a component that only displays data?](#148-how-do-you-translate-a-component-that-only-displays-data)
- [149: How does conditional rendering of a whole component translate?](#149-how-does-conditional-rendering-of-a-whole-component-translate)
- [150: What are the main things to remember when starting an Angular to React, Next.js or Vue translation?](#150-what-are-the-main-things-to-remember-when-starting-an-angular-to-react-nextjs-or-vue-translation)

### Moderate Questions (151-300)

- [151: Should you rewrite an Angular app at once or migrate it step by step?](#151-should-you-rewrite-an-angular-app-at-once-or-migrate-it-step-by-step)
- [152: How do you embed a React component inside an Angular app during migration?](#152-how-do-you-embed-a-react-component-inside-an-angular-app-during-migration)
- [153: How do Angular Elements help a migration?](#153-how-do-angular-elements-help-a-migration)
- [154: How do you translate a data-access service into hooks or composables?](#154-how-do-you-translate-a-data-access-service-into-hooks-or-composables)
- [155: How do you use RxJS observables in React?](#155-how-do-you-use-rxjs-observables-in-react)
- [156: How do you translate a BehaviorSubject-based store?](#156-how-do-you-translate-a-behaviorsubject-based-store)
- [157: How do you translate a switchMap typeahead?](#157-how-do-you-translate-a-switchmap-typeahead)
- [158: How do you translate combineLatest?](#158-how-do-you-translate-combinelatest)
- [159: How do you translate an HTTP interceptor?](#159-how-do-you-translate-an-http-interceptor)
- [160: How do you translate an error interceptor that redirects on 401?](#160-how-do-you-translate-an-error-interceptor-that-redirects-on-401)
- [161: How do you translate retry logic?](#161-how-do-you-translate-retry-logic)
- [162: How do you translate a canActivate route guard?](#162-how-do-you-translate-a-canactivate-route-guard)
- [163: How do you translate canDeactivate (unsaved changes warning)?](#163-how-do-you-translate-candeactivate-unsaved-changes-warning)
- [164: How do you translate a route resolver?](#164-how-do-you-translate-a-route-resolver)
- [165: How do you pass static data and titles through routes?](#165-how-do-you-pass-static-data-and-titles-through-routes)
- [166: How do you translate @defer?](#166-how-do-you-translate-defer)
- [167: How do you load a component only when it scrolls into view?](#167-how-do-you-load-a-component-only-when-it-scrolls-into-view)
- [168: How do you translate route preloading strategies?](#168-how-do-you-translate-route-preloading-strategies)
- [169: How do you translate a reactive form with nested groups?](#169-how-do-you-translate-a-reactive-form-with-nested-groups)
- [170: How do you translate FormArray?](#170-how-do-you-translate-formarray)
- [171: How do you translate a custom validator?](#171-how-do-you-translate-a-custom-validator)
- [172: How do you translate an async validator?](#172-how-do-you-translate-an-async-validator)
- [173: How do you translate cross-field validation?](#173-how-do-you-translate-cross-field-validation)
- [174: How do you translate Angular signal forms?](#174-how-do-you-translate-angular-signal-forms)
- [175: How do you translate a ControlValueAccessor custom input?](#175-how-do-you-translate-a-controlvalueaccessor-custom-input)
- [176: How do you translate dirty, touched and pristine state?](#176-how-do-you-translate-dirty-touched-and-pristine-state)
- [177: How do you reset a form to new values?](#177-how-do-you-reset-a-form-to-new-values)
- [178: How do you translate a form submit to a Next.js Server Action?](#178-how-do-you-translate-a-form-submit-to-a-nextjs-server-action)
- [179: What are useActionState and useFormStatus, and what is the Angular equivalent?](#179-what-are-useactionstate-and-useformstatus-and-what-is-the-angular-equivalent)
- [180: How do you translate optimistic updates?](#180-how-do-you-translate-optimistic-updates)
- [181: How do you translate resource() and httpResource()?](#181-how-do-you-translate-resource-and-httpresource)
- [182: How do you cache API data on the client?](#182-how-do-you-cache-api-data-on-the-client)
- [183: How do you translate infinite scrolling of a paged API?](#183-how-do-you-translate-infinite-scrolling-of-a-paged-api)
- [184: How do you refresh a list after creating an item?](#184-how-do-you-refresh-a-list-after-creating-an-item)
- [185: How do you translate linkedSignal?](#185-how-do-you-translate-linkedsignal)
- [186: How do you translate untracked()?](#186-how-do-you-translate-untracked)
- [187: How do you translate effect cleanup with onCleanup?](#187-how-do-you-translate-effect-cleanup-with-oncleanup)
- [188: How do you translate signal equality functions?](#188-how-do-you-translate-signal-equality-functions)
- [189: How does OnPush change detection translate?](#189-how-does-onpush-change-detection-translate)
- [190: How do you provide a service at the component level?](#190-how-do-you-provide-a-service-at-the-component-level)
- [191: How do you translate factory providers?](#191-how-do-you-translate-factory-providers)
- [192: How do you translate APP_INITIALIZER or provideAppInitializer?](#192-how-do-you-translate-app_initializer-or-provideappinitializer)
- [193: How do you translate a tooltip directive?](#193-how-do-you-translate-a-tooltip-directive)
- [194: How do you translate host directives?](#194-how-do-you-translate-host-directives)
- [195: How do you translate a custom structural directive?](#195-how-do-you-translate-a-custom-structural-directive)
- [196: How do you translate i18n?](#196-how-do-you-translate-i18n)
- [197: How do you translate CDK Overlay or portals?](#197-how-do-you-translate-cdk-overlay-or-portals)
- [198: How do error boundaries compare to Angular error handling?](#198-how-do-error-boundaries-compare-to-angular-error-handling)
- [199: How do Next.js error.tsx and not-found.tsx work?](#199-how-do-nextjs-errortsx-and-not-foundtsx-work)
- [200: How do Next.js loading.tsx and Suspense relate to Angular loading states?](#200-how-do-nextjs-loadingtsx-and-suspense-relate-to-angular-loading-states)
- [201: How do you give different sections different layouts?](#201-how-do-you-give-different-sections-different-layouts)
- [202: How do you prerender pages with dynamic params?](#202-how-do-you-prerender-pages-with-dynamic-params)
- [203: How do you set metadata from loaded data?](#203-how-do-you-set-metadata-from-loaded-data)
- [204: How do Next.js Route Handlers relate to the Angular app's backend?](#204-how-do-nextjs-route-handlers-relate-to-the-angular-apps-backend)
- [205: How do you translate the dev server proxy config?](#205-how-do-you-translate-the-dev-server-proxy-config)
- [206: How do you read and write cookies?](#206-how-do-you-read-and-write-cookies)
- [207: How does SSR compare across Angular, Next.js and Nuxt?](#207-how-does-ssr-compare-across-angular-nextjs-and-nuxt)
- [208: How do you fix a hydration mismatch?](#208-how-do-you-fix-a-hydration-mismatch)
- [209: How do you run code only in the browser?](#209-how-do-you-run-code-only-in-the-browser)
- [210: How does TransferState translate?](#210-how-does-transferstate-translate)
- [211: How do you translate static prerendering (SSG)?](#211-how-do-you-translate-static-prerendering-ssg)
- [212: How does Angular incremental hydration compare to React and Vue?](#212-how-does-angular-incremental-hydration-compare-to-react-and-vue)
- [213: How do you test a hook or composable that replaced a service?](#213-how-do-you-test-a-hook-or-composable-that-replaced-a-service)
- [214: How do you replace HttpTestingController in tests?](#214-how-do-you-replace-httptestingcontroller-in-tests)
- [215: How do you test components that use the router?](#215-how-do-you-test-components-that-use-the-router)
- [216: How do you test form input and submit?](#216-how-do-you-test-form-input-and-submit)
- [217: How do you mock dependencies that were injected in Angular?](#217-how-do-you-mock-dependencies-that-were-injected-in-angular)
- [218: What replaces Angular CDK component harnesses in tests?](#218-what-replaces-angular-cdk-component-harnesses-in-tests)
- [219: What replaces Angular CDK and Angular Aria for accessible widgets?](#219-what-replaces-angular-cdk-and-angular-aria-for-accessible-widgets)
- [220: How do you translate a CDK focus trap?](#220-how-do-you-translate-a-cdk-focus-trap)
- [221: How do you translate LiveAnnouncer for screen readers?](#221-how-do-you-translate-liveannouncer-for-screen-readers)
- [222: How do you translate CDK virtual scrolling?](#222-how-do-you-translate-cdk-virtual-scrolling)
- [223: How do you translate CDK drag and drop?](#223-how-do-you-translate-cdk-drag-and-drop)
- [224: How do you translate a Material table with sorting and paging?](#224-how-do-you-translate-a-material-table-with-sorting-and-paging)
- [225: How do you translate theming with CSS variables?](#225-how-do-you-translate-theming-with-css-variables)
- [226: How do you translate ::ng-deep?](#226-how-do-you-translate-ng-deep)
- [227: How do you set up Tailwind CSS in each?](#227-how-do-you-set-up-tailwind-css-in-each)
- [228: How do you translate a Subject-based event bus?](#228-how-do-you-translate-a-subject-based-event-bus)
- [229: How do you translate contentChildren for a tabs component?](#229-how-do-you-translate-contentchildren-for-a-tabs-component)
- [230: How does a parent call a method on a child component?](#230-how-does-a-parent-call-a-method-on-a-child-component)
- [231: How do you translate ViewContainerRef.createComponent?](#231-how-do-you-translate-viewcontainerrefcreatecomponent)
- [232: How do you translate a MatDialog-style dialog service?](#232-how-do-you-translate-a-matdialog-style-dialog-service)
- [233: How do you translate a toast notification service?](#233-how-do-you-translate-a-toast-notification-service)
- [234: How do you translate RxJS interval and timer?](#234-how-do-you-translate-rxjs-interval-and-timer)
- [235: How do you translate a WebSocket service?](#235-how-do-you-translate-a-websocket-service)
- [236: How do you translate Server-Sent Events?](#236-how-do-you-translate-server-sent-events)
- [237: How do you use Web Workers in each?](#237-how-do-you-use-web-workers-in-each)
- [238: How do you translate NgRx Store to Redux Toolkit?](#238-how-do-you-translate-ngrx-store-to-redux-toolkit)
- [239: How do you translate NgRx effects?](#239-how-do-you-translate-ngrx-effects)
- [240: How do you translate NgRx selectors?](#240-how-do-you-translate-ngrx-selectors)
- [241: How do you translate NgRx SignalStore?](#241-how-do-you-translate-ngrx-signalstore)
- [242: How do you translate the NgRx entity adapter?](#242-how-do-you-translate-the-ngrx-entity-adapter)
- [243: How do you persist a store to localStorage?](#243-how-do-you-persist-a-store-to-localstorage)
- [244: How do you keep filter state in the URL?](#244-how-do-you-keep-filter-state-in-the-url)
- [245: How does scroll restoration translate?](#245-how-does-scroll-restoration-translate)
- [246: How do you show a progress bar during navigation?](#246-how-do-you-show-a-progress-bar-during-navigation)
- [247: How do you translate a login and session flow?](#247-how-do-you-translate-a-login-and-session-flow)
- [248: How do you translate feature flags?](#248-how-do-you-translate-feature-flags)
- [249: How do you track page views on route change?](#249-how-do-you-track-page-views-on-route-change)
- [250: How do you translate TypeScript path aliases?](#250-how-do-you-translate-typescript-path-aliases)
- [251: How do you translate legacy @Input() and @Output() decorators?](#251-how-do-you-translate-legacy-input-and-output-decorators)
- [252: How do you translate ngOnChanges with previous values?](#252-how-do-you-translate-ngonchanges-with-previous-values)
- [253: How do you translate takeUntilDestroyed and manual subscriptions?](#253-how-do-you-translate-takeuntildestroyed-and-manual-subscriptions)
- [254: How do you translate the keyvalue and slice pipes?](#254-how-do-you-translate-the-keyvalue-and-slice-pipes)
- [255: How do you translate plural and percent formatting?](#255-how-do-you-translate-plural-and-percent-formatting)
- [256: How do you translate legacy *ngIf with else and *ngFor with trackBy?](#256-how-do-you-translate-legacy-ngif-with-else-and-ngfor-with-trackby)
- [257: How do you translate Renderer2 and ElementRef DOM changes?](#257-how-do-you-translate-renderer2-and-elementref-dom-changes)
- [258: How do you translate ChangeDetectorRef.detectChanges?](#258-how-do-you-translate-changedetectorrefdetectchanges)
- [259: How do you translate NgZone.runOutsideAngular?](#259-how-do-you-translate-ngzonerunoutsideangular)
- [260: How do you translate a dynamic form built from a config?](#260-how-do-you-translate-a-dynamic-form-built-from-a-config)
- [261: How do you translate keyboard shortcuts?](#261-how-do-you-translate-keyboard-shortcuts)
- [262: How do you translate the CDK Clipboard?](#262-how-do-you-translate-the-cdk-clipboard)
- [263: How do you translate an IntersectionObserver directive?](#263-how-do-you-translate-an-intersectionobserver-directive)
- [264: How do you translate a ResizeObserver directive?](#264-how-do-you-translate-a-resizeobserver-directive)
- [265: How do you translate a click-outside directive?](#265-how-do-you-translate-a-click-outside-directive)
- [266: How do you translate an infinite scroll directive?](#266-how-do-you-translate-an-infinite-scroll-directive)
- [267: Why does my translated React component show stale values?](#267-why-does-my-translated-react-component-show-stale-values)
- [268: Why does a translated Vue component stop updating?](#268-why-does-a-translated-vue-component-stop-updating)
- [269: Why does my useEffect run too often?](#269-why-does-my-useeffect-run-too-often)
- [270: How do you translate data loading that ran in ngOnInit when moving to Next.js?](#270-how-do-you-translate-data-loading-that-ran-in-ngoninit-when-moving-to-nextjs)
- [271: How do you translate a switch over an enum?](#271-how-do-you-translate-a-switch-over-an-enum)
- [272: When should you split a large Angular template while translating?](#272-when-should-you-split-a-large-angular-template-while-translating)
- [273: What should you check when reviewing a translated component?](#273-what-should-you-check-when-reviewing-a-translated-component)
- [274: How do you estimate the effort of a migration?](#274-how-do-you-estimate-the-effort-of-a-migration)
- [275: How do you share code between Angular and the new app during migration?](#275-how-do-you-share-code-between-angular-and-the-new-app-during-migration)
- [276: How do you replace Angular-specific date or utility libraries?](#276-how-do-you-replace-angular-specific-date-or-utility-libraries)
- [277: How do the build tools compare?](#277-how-do-the-build-tools-compare)
- [278: How do you analyze bundle size after translating?](#278-how-do-you-analyze-bundle-size-after-translating)
- [279: How do you translate a PWA setup?](#279-how-do-you-translate-a-pwa-setup)
- [280: How do you translate typed reactive forms into a schema-first form?](#280-how-do-you-translate-typed-reactive-forms-into-a-schema-first-form)
- [281: How do you translate a global loading indicator for HTTP calls?](#281-how-do-you-translate-a-global-loading-indicator-for-http-calls)
- [282: How do you translate a service that caches with shareReplay?](#282-how-do-you-translate-a-service-that-caches-with-sharereplay)
- [283: How do you translate polling an API every few seconds?](#283-how-do-you-translate-polling-an-api-every-few-seconds)
- [284: How do you translate a component that wraps a third-party jQuery-style widget?](#284-how-do-you-translate-a-component-that-wraps-a-third-party-jquery-style-widget)
- [285: How do you translate a component that uses @Attribute or static host attributes?](#285-how-do-you-translate-a-component-that-uses-attribute-or-static-host-attributes)
- [286: How do you pass through extra attributes and events to an inner element?](#286-how-do-you-pass-through-extra-attributes-and-events-to-an-inner-element)
- [287: How do you translate an Angular component with multiple selectors or attribute selector?](#287-how-do-you-translate-an-angular-component-with-multiple-selectors-or-attribute-selector)
- [288: How do you translate Angular's @Optional and @Self injection flags?](#288-how-do-you-translate-angulars-optional-and-self-injection-flags)
- [289: How do you translate a service that depends on another service?](#289-how-do-you-translate-a-service-that-depends-on-another-service)
- [290: How do you translate an abstract class used as a DI token for swappable implementations?](#290-how-do-you-translate-an-abstract-class-used-as-a-di-token-for-swappable-implementations)
- [291: How do you translate route-level providers?](#291-how-do-you-translate-route-level-providers)
- [292: How do you translate a component library's global configuration?](#292-how-do-you-translate-a-component-librarys-global-configuration)
- [293: How do you translate an Angular app shell with a sidebar and header?](#293-how-do-you-translate-an-angular-app-shell-with-a-sidebar-and-header)
- [294: How do you translate a "master-detail" layout with child routes?](#294-how-do-you-translate-a-master-detail-layout-with-child-routes)
- [295: How do you translate named or auxiliary router outlets?](#295-how-do-you-translate-named-or-auxiliary-router-outlets)
- [296: How do you translate a modal that has its own URL?](#296-how-do-you-translate-a-modal-that-has-its-own-url)
- [297: How do you translate an Angular app with many small NgModules into folders?](#297-how-do-you-translate-an-angular-app-with-many-small-ngmodules-into-folders)
- [298: How do you avoid prop drilling when translating deep Angular component trees?](#298-how-do-you-avoid-prop-drilling-when-translating-deep-angular-component-trees)
- [299: How do you handle "this" binding issues when moving class methods to React?](#299-how-do-you-handle-this-binding-issues-when-moving-class-methods-to-react)
- [300: What order should you translate an Angular feature in?](#300-what-order-should-you-translate-an-angular-feature-in)

### Advanced Questions (301-450)

- [301: How do the rendering models of Angular, React and Vue differ under the hood?](#301-how-do-the-rendering-models-of-angular-react-and-vue-differ-under-the-hood)
- [302: How does zoneless change detection compare with React and Vue scheduling?](#302-how-does-zoneless-change-detection-compare-with-react-and-vue-scheduling)
- [303: How do you translate code that must run after the DOM updates?](#303-how-do-you-translate-code-that-must-run-after-the-dom-updates)
- [304: How does memoization differ between signals, the React Compiler and Vue computed?](#304-how-does-memoization-differ-between-signals-the-react-compiler-and-vue-computed)
- [305: How do you keep large lists fast after translating to React?](#305-how-do-you-keep-large-lists-fast-after-translating-to-react)
- [306: Why can React context hurt performance compared with Angular services?](#306-why-can-react-context-hurt-performance-compared-with-angular-services)
- [307: How do you build a signal-like store for React with useSyncExternalStore?](#307-how-do-you-build-a-signal-like-store-for-react-with-usesyncexternalstore)
- [308: How do you bridge Angular signals and React during an incremental migration?](#308-how-do-you-bridge-angular-signals-and-react-during-an-incremental-migration)
- [309: How do you run Angular and React apps side by side with Module Federation?](#309-how-do-you-run-angular-and-react-apps-side-by-side-with-module-federation)
- [310: How do you share state between microfrontends written in different frameworks?](#310-how-do-you-share-state-between-microfrontends-written-in-different-frameworks)
- [311: How do you coordinate routing between an Angular shell and a React or Vue microfrontend?](#311-how-do-you-coordinate-routing-between-an-angular-shell-and-a-react-or-vue-microfrontend)
- [312: How does React 19 support custom elements, and why does it matter for migration?](#312-how-does-react-19-support-custom-elements-and-why-does-it-matter-for-migration)
- [313: How do you build Vue components as custom elements to embed in an Angular app?](#313-how-do-you-build-vue-components-as-custom-elements-to-embed-in-an-angular-app)
- [314: How does Angular's hierarchical injector differ from React context?](#314-how-does-angulars-hierarchical-injector-differ-from-react-context)
- [315: How do you keep testability without DI in React and Vue?](#315-how-do-you-keep-testability-without-di-in-react-and-vue)
- [316: How should an Angular developer think about React Server Components?](#316-how-should-an-angular-developer-think-about-react-server-components)
- [317: What can and cannot cross the server/client boundary in Next.js?](#317-what-can-and-cannot-cross-the-serverclient-boundary-in-nextjs)
- [318: What security risks come with Server Actions?](#318-what-security-risks-come-with-server-actions)
- [319: How do you avoid request waterfalls when translating resolvers to Next.js?](#319-how-do-you-avoid-request-waterfalls-when-translating-resolvers-to-nextjs)
- [320: How does streaming SSR compare across Angular, Next.js and Nuxt?](#320-how-does-streaming-ssr-compare-across-angular-nextjs-and-nuxt)
- [321: How does Next.js 16 caching compare with Angular's HTTP transfer cache?](#321-how-does-nextjs-16-caching-compare-with-angulars-http-transfer-cache)
- [322: How do you invalidate cached data after a mutation in Next.js 16?](#322-how-do-you-invalidate-cached-data-after-a-mutation-in-nextjs-16)
- [323: What are Cache Components and partial prerendering, and how do they compare to Angular render modes?](#323-what-are-cache-components-and-partial-prerendering-and-how-do-they-compare-to-angular-render-modes)
- [324: What does proxy.ts replace from an Angular SSR server.ts?](#324-what-does-proxyts-replace-from-an-angular-ssr-serverts)
- [325: How do you translate Angular SSR route render modes to Next.js and Nuxt?](#325-how-do-you-translate-angular-ssr-route-render-modes-to-nextjs-and-nuxt)
- [326: How do you protect a page on the server without leaking data?](#326-how-do-you-protect-a-page-on-the-server-without-leaking-data)
- [327: How does XSS protection differ between Angular, React and Vue?](#327-how-does-xss-protection-differ-between-angular-react-and-vue)
- [328: How do you safely render user-provided URLs?](#328-how-do-you-safely-render-user-provided-urls)
- [329: How does CSRF protection change when moving to Next.js?](#329-how-does-csrf-protection-change-when-moving-to-nextjs)
- [330: How do you set up a Content Security Policy with nonces in each?](#330-how-do-you-set-up-a-content-security-policy-with-nonces-in-each)
- [331: How do Trusted Types work in each framework?](#331-how-do-trusted-types-work-in-each-framework)
- [332: How do you prevent secrets from leaking into the client bundle?](#332-how-do-you-prevent-secrets-from-leaking-into-the-client-bundle)
- [333: How do you design error handling that spans server and client in Next.js?](#333-how-do-you-design-error-handling-that-spans-server-and-client-in-nextjs)
- [334: How do you report Core Web Vitals in each?](#334-how-do-you-report-core-web-vitals-in-each)
- [335: How do you set performance budgets like Angular's budgets config?](#335-how-do-you-set-performance-budgets-like-angulars-budgets-config)
- [336: How do you get fine-grained code splitting like @defer in React and Vue?](#336-how-do-you-get-fine-grained-code-splitting-like-defer-in-react-and-vue)
- [337: How do you translate Angular's tree-shakable providers concept?](#337-how-do-you-translate-angulars-tree-shakable-providers-concept)
- [338: What causes hard-to-find hydration errors after translating to Next.js?](#338-what-causes-hard-to-find-hydration-errors-after-translating-to-nextjs)
- [339: How does Angular event replay compare with React's hydration of events?](#339-how-does-angular-event-replay-compare-with-reacts-hydration-of-events)
- [340: How do you translate a slow filter to stay responsive while typing?](#340-how-do-you-translate-a-slow-filter-to-stay-responsive-while-typing)
- [341: How does React Suspense for data compare with Angular's resource API?](#341-how-does-react-suspense-for-data-compare-with-angulars-resource-api)
- [342: How do you avoid race conditions when parameters change quickly?](#342-how-do-you-avoid-race-conditions-when-parameters-change-quickly)
- [343: How do you translate an RxJS pipeline with exponential backoff and polling until done?](#343-how-do-you-translate-an-rxjs-pipeline-with-exponential-backoff-and-polling-until-done)
- [344: How do you pause polling when the tab is hidden?](#344-how-do-you-pause-polling-when-the-tab-is-hidden)
- [345: How do you translate undo and redo state?](#345-how-do-you-translate-undo-and-redo-state)
- [346: How do you translate an offline-first data layer?](#346-how-do-you-translate-an-offline-first-data-layer)
- [347: How do you translate real-time collaborative updates into query caches?](#347-how-do-you-translate-real-time-collaborative-updates-into-query-caches)
- [348: Why can large forms feel slow after translating to React, and how do you fix it?](#348-why-can-large-forms-feel-slow-after-translating-to-react-and-how-do-you-fix-it)
- [349: How do you choose a form architecture when translating complex Angular forms?](#349-how-do-you-choose-a-form-architecture-when-translating-complex-angular-forms)
- [350: How do you translate validators whose rules change at runtime?](#350-how-do-you-translate-validators-whose-rules-change-at-runtime)
- [351: How do you keep forms accessible after translating?](#351-how-do-you-keep-forms-accessible-after-translating)
- [352: How do you translate a recursive tree component?](#352-how-do-you-translate-a-recursive-tree-component)
- [353: How do you translate a component that receives a template with typed context?](#353-how-do-you-translate-a-component-that-receives-a-template-with-typed-context)
- [354: How do you translate a polymorphic component (render as another element)?](#354-how-do-you-translate-a-polymorphic-component-render-as-another-element)
- [355: How do directives compare with higher-order components and hooks?](#355-how-do-directives-compare-with-higher-order-components-and-hooks)
- [356: What is the headless component pattern, and how does it map from Angular?](#356-what-is-the-headless-component-pattern-and-how-does-it-map-from-angular)
- [357: How do you design components that work both controlled and uncontrolled?](#357-how-do-you-design-components-that-work-both-controlled-and-uncontrolled)
- [358: How do refs to child components and DOM nodes differ in React 19, Angular and Vue?](#358-how-do-refs-to-child-components-and-dom-nodes-differ-in-react-19-angular-and-vue)
- [359: How do you translate route transitions using the View Transitions API?](#359-how-do-you-translate-route-transitions-using-the-view-transitions-api)
- [360: How do you translate list enter, leave and move animations?](#360-how-do-you-translate-list-enter-leave-and-move-animations)
- [361: How do you translate locale-prefixed routing with SSR?](#361-how-do-you-translate-locale-prefixed-routing-with-ssr)
- [362: How do you handle right-to-left languages in each?](#362-how-do-you-handle-right-to-left-languages-in-each)
- [363: How do you avoid a theme flash on first load with SSR?](#363-how-do-you-avoid-a-theme-flash-on-first-load-with-ssr)
- [364: How do you port a shared Angular design system to React and Vue?](#364-how-do-you-port-a-shared-angular-design-system-to-react-and-vue)
- [365: How do you use Storybook to compare old and new components?](#365-how-do-you-use-storybook-to-compare-old-and-new-components)
- [366: How do you use visual regression testing during migration?](#366-how-do-you-use-visual-regression-testing-during-migration)
- [367: How do you prove the translated app behaves the same?](#367-how-do-you-prove-the-translated-app-behaves-the-same)
- [368: How do you test that both apps call the API the same way?](#368-how-do-you-test-that-both-apps-call-the-api-the-same-way)
- [369: How do you test async UI behavior consistently across frameworks?](#369-how-do-you-test-async-ui-behavior-consistently-across-frameworks)
- [370: How do you test Next.js Server Components and Server Actions?](#370-how-do-you-test-nextjs-server-components-and-server-actions)
- [371: Which profiling tools do you use in each framework?](#371-which-profiling-tools-do-you-use-in-each-framework)
- [372: How do memory leaks differ between Angular, React and Vue?](#372-how-do-memory-leaks-differ-between-angular-react-and-vue)
- [373: How do you virtualize lists with dynamic row heights?](#373-how-do-you-virtualize-lists-with-dynamic-row-heights)
- [374: How do you move heavy work to a Web Worker with a nice API?](#374-how-do-you-move-heavy-work-to-a-web-worker-with-a-nice-api)
- [375: How do you break up long tasks to keep INP low?](#375-how-do-you-break-up-long-tasks-to-keep-inp-low)
- [376: How do framework runtime sizes compare, and does it matter?](#376-how-do-framework-runtime-sizes-compare-and-does-it-matter)
- [377: When can you ship zero JavaScript for parts of a translated app?](#377-when-can-you-ship-zero-javascript-for-parts-of-a-translated-app)
- [378: How do you protect SEO when migrating URLs?](#378-how-do-you-protect-seo-when-migrating-urls)
- [379: How do you migrate route by route behind one domain?](#379-how-do-you-migrate-route-by-route-behind-one-domain)
- [380: How do you keep analytics consistent across the old and new apps?](#380-how-do-you-keep-analytics-consistent-across-the-old-and-new-apps)
- [381: How do you roll out a translated app safely?](#381-how-do-you-roll-out-a-translated-app-safely)
- [382: How do you help an Angular team learn React, Next.js or Vue?](#382-how-do-you-help-an-angular-team-learn-react-nextjs-or-vue)
- [383: How do you enforce architecture boundaries after translating?](#383-how-do-you-enforce-architecture-boundaries-after-translating)
- [384: How does type checking of templates compare?](#384-how-does-type-checking-of-templates-compare)
- [385: How do you get type-safe routing like Angular's typed routes?](#385-how-do-you-get-type-safe-routing-like-angulars-typed-routes)
- [386: How do you share a type-safe API client between the old and new apps?](#386-how-do-you-share-a-type-safe-api-client-between-the-old-and-new-apps)
- [387: How do the Angular, React and Vue compilers differ?](#387-how-do-the-angular-react-and-vue-compilers-differ)
- [388: How does Vue reactivity compare with Angular signals internally?](#388-how-does-vue-reactivity-compare-with-angular-signals-internally)
- [389: Should you use signals in React to make the translation easier?](#389-should-you-use-signals-in-react-to-make-the-translation-easier)
- [390: When should you use shallowRef or markRaw in translated Vue code?](#390-when-should-you-use-shallowref-or-markraw-in-translated-vue-code)
- [391: Why is using effects to derive state an anti-pattern in all three?](#391-why-is-using-effects-to-derive-state-an-anti-pattern-in-all-three)
- [392: What causes infinite loops in effects, and how do they differ?](#392-what-causes-infinite-loops-in-effects-and-how-do-they-differ)
- [393: In what order do parent and child effects run?](#393-in-what-order-do-parent-and-child-effects-run)
- [394: What do React error boundaries not catch, and how do you handle those errors?](#394-what-do-react-error-boundaries-not-catch-and-how-do-you-handle-those-errors)
- [395: How do you handle unhandled promise rejections globally?](#395-how-do-you-handle-unhandled-promise-rejections-globally)
- [396: Scenario: how would you translate a dashboard with several independent widgets?](#396-scenario-how-would-you-translate-a-dashboard-with-several-independent-widgets)
- [397: Scenario: how would you translate an authenticated admin area?](#397-scenario-how-would-you-translate-an-authenticated-admin-area)
- [398: Scenario: how would you translate a multi-step wizard?](#398-scenario-how-would-you-translate-a-multi-step-wizard)
- [399: Scenario: how would you translate a data grid with server-side paging, sorting and filters?](#399-scenario-how-would-you-translate-a-data-grid-with-server-side-paging-sorting-and-filters)
- [400: Scenario: how would you translate a real-time chat?](#400-scenario-how-would-you-translate-a-real-time-chat)
- [401: Scenario: how would you translate a shopping cart that survives reloads?](#401-scenario-how-would-you-translate-a-shopping-cart-that-survives-reloads)
- [402: Scenario: how would you translate an infinite feed that also needs SEO?](#402-scenario-how-would-you-translate-an-infinite-feed-that-also-needs-seo)
- [403: Scenario: how would you translate a file upload with a progress bar?](#403-scenario-how-would-you-translate-a-file-upload-with-a-progress-bar)
- [404: Scenario: how would you translate lazy-loaded translations per feature?](#404-scenario-how-would-you-translate-lazy-loaded-translations-per-feature)
- [405: Scenario: how would you translate a complex permission system?](#405-scenario-how-would-you-translate-a-complex-permission-system)
- [406: Scenario: how would you translate a plugin system that loads components at runtime?](#406-scenario-how-would-you-translate-a-plugin-system-that-loads-components-at-runtime)
- [407: Scenario: how would you move an SEO-focused Angular SSR site to Next.js?](#407-scenario-how-would-you-move-an-seo-focused-angular-ssr-site-to-nextjs)
- [408: Scenario: how would you translate an app built heavily on NgRx?](#408-scenario-how-would-you-translate-an-app-built-heavily-on-ngrx)
- [409: Scenario: how would you convert an internal Angular component library for React and Vue teams?](#409-scenario-how-would-you-convert-an-internal-angular-component-library-for-react-and-vue-teams)
- [410: How do you package a component library for React and Vue compared with ng-packagr?](#410-how-do-you-package-a-component-library-for-react-and-vue-compared-with-ng-packagr)
- [411: Why must React and Vue be peer dependencies in shared libraries?](#411-why-must-react-and-vue-be-peer-dependencies-in-shared-libraries)
- [412: How do you choose between React, Next.js and Vue as the target for an Angular app?](#412-how-do-you-choose-between-react-nextjs-and-vue-as-the-target-for-an-angular-app)
- [413: What do you gain and lose moving from an Angular SPA to the Next.js App Router?](#413-what-do-you-gain-and-lose-moving-from-an-angular-spa-to-the-nextjs-app-router)
- [414: What are the limits of Next.js static export?](#414-what-are-the-limits-of-nextjs-static-export)
- [415: When should a Vue migration use Nuxt instead of plain Vue with Vite?](#415-when-should-a-vue-migration-use-nuxt-instead-of-plain-vue-with-vite)
- [416: How does deployment differ between the four?](#416-how-does-deployment-differ-between-the-four)
- [417: How do you write a Dockerfile for each?](#417-how-do-you-write-a-dockerfile-for-each)
- [418: How do you handle runtime configuration that changes per environment without rebuilding?](#418-how-do-you-handle-runtime-configuration-that-changes-per-environment-without-rebuilding)
- [419: What changes in the CI pipeline after migrating?](#419-what-changes-in-the-ci-pipeline-after-migrating)
- [420: How do you set security headers in each?](#420-how-do-you-set-security-headers-in-each)
- [421: How do you rate limit Server Actions and Route Handlers?](#421-how-do-you-rate-limit-server-actions-and-route-handlers)
- [422: How do you translate a file download from an API?](#422-how-do-you-translate-a-file-download-from-an-api)
- [423: How do you load third-party scripts like chat widgets or tag managers?](#423-how-do-you-load-third-party-scripts-like-chat-widgets-or-tag-managers)
- [424: How do you translate a D3 chart component?](#424-how-do-you-translate-a-d3-chart-component)
- [425: How do you translate a canvas animation loop?](#425-how-do-you-translate-a-canvas-animation-loop)
- [426: How do you check accessibility after the migration?](#426-how-do-you-check-accessibility-after-the-migration)
- [427: How do you measure whether the translated app is actually faster?](#427-how-do-you-measure-whether-the-translated-app-is-actually-faster)
- [428: What are common anti-patterns when translating Angular code literally?](#428-what-are-common-anti-patterns-when-translating-angular-code-literally)
- [429: How do you handle fixes and features while both apps are live?](#429-how-do-you-handle-fixes-and-features-while-both-apps-are-live)
- [430: How do the rules of hooks compare with Angular's injection context and Vue's setup rules?](#430-how-do-the-rules-of-hooks-compare-with-angulars-injection-context-and-vues-setup-rules)
- [431: Why must React render functions be pure, and how does that differ from Angular constructors?](#431-why-must-react-render-functions-be-pure-and-how-does-that-differ-from-angular-constructors)
- [432: How do Angular outputs, React callbacks and Vue emits differ from DOM events?](#432-how-do-angular-outputs-react-callbacks-and-vue-emits-differ-from-dom-events)
- [433: How do events from portals bubble differently in React and Vue?](#433-how-do-events-from-portals-bubble-differently-in-react-and-vue)
- [434: How does component identity decide whether state is kept?](#434-how-does-component-identity-decide-whether-state-is-kept)
- [435: How do you handle per-request state on the server in Next.js compared with Angular SSR?](#435-how-do-you-handle-per-request-state-on-the-server-in-nextjs-compared-with-angular-ssr)
- [436: How do you avoid cross-request state pollution in Nuxt?](#436-how-do-you-avoid-cross-request-state-pollution-in-nuxt)
- [437: When should you use Server Actions, Route Handlers, or a separate API in Next.js?](#437-when-should-you-use-server-actions-route-handlers-or-a-separate-api-in-nextjs)
- [438: How do you run work after the response is sent in Next.js?](#438-how-do-you-run-work-after-the-response-is-sent-in-nextjs)
- [439: Should translated Next.js code run on the Edge runtime or Node.js?](#439-should-translated-nextjs-code-run-on-the-edge-runtime-or-nodejs)
- [440: Which auth libraries replace Angular auth libraries?](#440-which-auth-libraries-replace-angular-auth-libraries)
- [441: Can you automate parts of the translation?](#441-can-you-automate-parts-of-the-translation)
- [442: How do you translate an Angular component that relies on ngDoCheck or custom change detection?](#442-how-do-you-translate-an-angular-component-that-relies-on-ngdocheck-or-custom-change-detection)
- [443: How do you translate an Angular component that uses ViewEncapsulation.ShadowDom?](#443-how-do-you-translate-an-angular-component-that-uses-viewencapsulationshadowdom)
- [444: How do you translate Angular's i18n ICU messages?](#444-how-do-you-translate-angulars-i18n-icu-messages)
- [445: How do you translate lazy-loaded feature routes with their own providers and state?](#445-how-do-you-translate-lazy-loaded-feature-routes-with-their-own-providers-and-state)
- [446: How do you translate Angular's APP_BASE_HREF and deploying under a sub-path?](#446-how-do-you-translate-angulars-app_base_href-and-deploying-under-a-sub-path)
- [447: How do you translate Angular's Location and history state?](#447-how-do-you-translate-angulars-location-and-history-state)
- [448: How do you make sure the translated code follows each framework's current best practices?](#448-how-do-you-make-sure-the-translated-code-follows-each-frameworks-current-best-practices)
- [449: What does a final migration checklist look like?](#449-what-does-a-final-migration-checklist-look-like)
- [450: What are the key lessons from translating Angular apps to React, Next.js and Vue?](#450-what-are-the-key-lessons-from-translating-angular-apps-to-react-nextjs-and-vue)

---

# Easy Questions (1-150)

## 1: What does it mean to translate an Angular app into React, Next.js or Vue.js?

It means rebuilding the same features, screens and behavior with another framework's building blocks. You map each Angular concept to its closest match: components stay components, signals become state, services become hooks or composables, pipes become plain functions, and the Angular router becomes React Router, the Next.js `app/` folder, or Vue Router.

A good translation keeps the user-facing behavior the same and changes only the code underneath. Most of the work is not syntax, it is learning where each framework expects state, side effects and data loading to live.

| Angular              | React                    | Next.js                    | Vue.js                      |
| -------------------- | ------------------------ | -------------------------- | --------------------------- |
| Component + template | Function component + JSX | Server or client component | Single File Component (SFC) |
| `signal()`           | `useState`               | `useState` (client)        | `ref()`                     |
| Service + `inject()` | Hook / context           | Hook / server function     | Composable / `provide`      |
| Router               | React Router             | File-based `app/` router   | Vue Router                  |

## 2: How are Angular, React, Next.js and Vue.js different in nature?

- **Angular** is a full framework. Router, forms, HTTP client, DI and a CLI come in the box, and the project structure is opinionated.
- **React** is a UI library. It renders components. Routing, data fetching and forms come from other libraries you choose.
- **Next.js** is a framework built on top of React. It adds file-based routing, server rendering, Server Components, data caching and a build system.
- **Vue.js** is a progressive framework. The core renders components, and official add-ons (Vue Router, Pinia) fill in the rest. Nuxt is to Vue what Next.js is to React.

So "Angular to React" means picking extra libraries, while "Angular to Next.js" or "Angular to Vue" gives you more built-in pieces.

## 3: How do you create a new project in each framework?

**Angular**

```bash
npm install -g @angular/cli
ng new my-app
```

**React**

```bash
npm create vite@latest my-app -- --template react-ts
```

**Next.js**

```bash
npx create-next-app@latest my-app
```

**Vue.js**

```bash
npm create vue@latest
```

All four give you TypeScript, a dev server and a production build. Create React App is deprecated, so Vite is the usual choice for a plain React SPA.

## 4: How does the project structure differ?

**Angular**

```text
src/
  main.ts            # bootstrapApplication
  app/
    app.ts           # root component
    app.config.ts    # providers
    app.routes.ts    # routes
    users/user-list.ts
```

**React**

```text
src/
  main.tsx           # createRoot
  App.tsx            # root component
  routes/            # your choice
  components/
```

**Next.js**

```text
app/
  layout.tsx         # root layout
  page.tsx           # "/" route
  users/page.tsx     # "/users" route
components/
```

**Vue.js**

```text
src/
  main.ts            # createApp
  App.vue
  router/index.ts
  components/UserList.vue
```

Angular and Vue have a fixed entry point and a router config file. React leaves structure to you. Next.js uses folders inside `app/` as the routes.

## 5: How is the app bootstrapped in each framework?

**Angular**

```ts
// main.ts
import { bootstrapApplication } from "@angular/platform-browser";
import { App } from "./app/app";
import { appConfig } from "./app/app.config";

bootstrapApplication(App, appConfig);
```

**React**

```tsx
// main.tsx
import { createRoot } from "react-dom/client";
import App from "./App";

createRoot(document.getElementById("root")!).render(<App />);
```

**Next.js**

```tsx
// app/layout.tsx (Next.js renders it for you, there is no main file)
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

**Vue.js**

```ts
// main.ts
import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
```

## 6: How do you write the simplest component?

**Angular**

```ts
import { Component } from "@angular/core";

@Component({
  selector: "app-hello",
  template: `<h1>Hello, world</h1>`,
})
export class Hello {}
```

**React**

```tsx
export function Hello() {
  return <h1>Hello, world</h1>;
}
```

**Vue.js**

```vue
<template>
  <h1>Hello, world</h1>
</template>
```

An Angular component is a decorated class. A React component is a function that returns JSX. A Vue component is a `.vue` file with a template, and a script block is optional.

## 7: How do Angular templates compare to JSX and Vue templates?

Angular templates are HTML with Angular syntax (`{{ }}`, `[prop]`, `(event)`, `@if`). Vue templates are also HTML with directives (`{{ }}`, `:prop`, `@event`, `v-if`). React has no template language. JSX is JavaScript, so you use normal JS for logic: ternaries, `&&` and `.map()`.

That is why Angular to Vue usually feels like a line-by-line rewrite of the template, while Angular to React means turning template syntax into JavaScript expressions.

**Angular**

```html
@if (user()) {
<p>{{ user().name }}</p>
}
```

**React**

```tsx
{
  user && <p>{user.name}</p>;
}
```

**Vue.js**

```vue
<p v-if="user">{{ user.name }}</p>
```

## 8: How do you translate text interpolation?

**Angular**

```ts
@Component({
  selector: "app-greeting",
  template: `<p>Hello, {{ name() }}! You have {{ count() * 2 }} points.</p>`,
})
export class Greeting {
  name = signal("Ana");
  count = signal(5);
}
```

**React**

```tsx
export function Greeting() {
  const [name] = useState("Ana");
  const [count] = useState(5);
  return (
    <p>
      Hello, {name}! You have {count * 2} points.
    </p>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { ref } from "vue";
const name = ref("Ana");
const count = ref(5);
</script>

<template>
  <p>Hello, {{ name }}! You have {{ count * 2 }} points.</p>
</template>
```

Note that Angular signals are read by calling them (`name()`), and Vue refs are unwrapped automatically in the template (no `.value`).

## 9: How do you translate property binding?

**Angular**

```html
<img [src]="avatarUrl()" [alt]="userName()" />
<button [disabled]="isSaving()">Save</button>
```

**React**

```tsx
<img src={avatarUrl} alt={userName} />
<button disabled={isSaving}>Save</button>
```

**Vue.js**

```vue
<img :src="avatarUrl" :alt="userName" />
<button :disabled="isSaving">Save</button>
```

`[prop]="x"` becomes `prop={x}` in JSX and `:prop="x"` (short for `v-bind:prop`) in Vue.

## 10: How do you translate attribute binding like attr.aria-label?

Angular separates DOM properties from HTML attributes, so you need `[attr.x]` for things that are not properties. React and Vue figure it out for you.

**Angular**

```html
<button [attr.aria-label]="label()" [attr.data-id]="id()">X</button>
```

**React**

```tsx
<button aria-label={label} data-id={id}>
  X
</button>
```

**Vue.js**

```vue
<button :aria-label="label" :data-id="id">X</button>
```

In React, `aria-*` and `data-*` keep their dashes. Other attributes use camelCase, like `tabIndex` and `htmlFor`.

## 11: How do you translate class binding?

**Angular**

```html
<li
  [class.active]="isActive()"
  [class]="{ done: isDone(), urgent: isUrgent() }"
>
  Task
</li>
```

**React**

```tsx
<li
  className={[isActive && "active", isDone && "done", isUrgent && "urgent"]
    .filter(Boolean)
    .join(" ")}
>
  Task
</li>
```

**Vue.js**

```vue
<li :class="{ active: isActive, done: isDone, urgent: isUrgent }">Task</li>
```

React uses `className` and takes a string. Many teams use the small `clsx` package: `className={clsx({ active: isActive, done: isDone })}`. Vue accepts objects and arrays like Angular.

## 12: How do you translate style binding?

**Angular**

```html
<div [style.width.px]="width()" [style.background-color]="color()">Box</div>
```

**React**

```tsx
<div style={{ width: width, backgroundColor: color }}>Box</div>
```

**Vue.js**

```vue
<div :style="{ width: width + 'px', backgroundColor: color }">Box</div>
```

React takes a style object with camelCase keys. A plain number for a size property like `width` is treated as pixels. Vue takes an object too and accepts both `backgroundColor` and `'background-color'`.

## 13: How do you translate event binding?

**Angular**

```ts
@Component({
  selector: "app-like",
  template: `<button (click)="like()">Like ({{ likes() }})</button>`,
})
export class Like {
  likes = signal(0);
  like() {
    this.likes.update((n) => n + 1);
  }
}
```

**React**

```tsx
export function Like() {
  const [likes, setLikes] = useState(0);
  return <button onClick={() => setLikes((n) => n + 1)}>Like ({likes})</button>;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { ref } from "vue";
const likes = ref(0);
</script>

<template>
  <button @click="likes++">Like ({{ likes }})</button>
</template>
```

`(click)` becomes `onClick` in React (camelCase, a function is passed) and `@click` in Vue.

## 14: How do you access the event object?

**Angular**

```html
<input (input)="onInput($event)" />
```

```ts
onInput(event: Event) {
  this.text.set((event.target as HTMLInputElement).value);
}
```

**React**

```tsx
<input onChange={(e) => setText(e.target.value)} />
```

**Vue.js**

```vue
<input @input="onInput($event)" />
<!-- or simply @input="onInput", the event is passed as the first argument -->
```

React gives you a typed synthetic event, so `e.target.value` works without a cast. Note that React's `onChange` fires on every keystroke, like the native `input` event.

## 15: How do you translate two-way binding on an input?

**Angular**

```ts
@Component({
  imports: [FormsModule],
  template: `<input [(ngModel)]="name" />
    <p>{{ name }}</p>`,
})
export class NameInput {
  name = "";
}
```

**React**

```tsx
export function NameInput() {
  const [name, setName] = useState("");
  return (
    <>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <p>{name}</p>
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { ref } from "vue";
const name = ref("");
</script>

<template>
  <input v-model="name" />
  <p>{{ name }}</p>
</template>
```

React has no two-way binding. You pass `value` and update state in `onChange` (a "controlled input"). Vue's `v-model` is the direct match for `[(ngModel)]`.

## 16: How do you translate @if?

**Angular**

```html
@if (isLoggedIn()) {
<p>Welcome back!</p>
}
```

**React**

```tsx
{
  isLoggedIn && <p>Welcome back!</p>;
}
```

**Vue.js**

```vue
<p v-if="isLoggedIn">Welcome back!</p>
```

Watch out for `&&` with numbers in React: `{count && <p>...</p>}` renders `0` when `count` is 0. Use `count > 0 &&` instead.

## 17: How do you translate @if with @else?

**Angular**

```html
@if (user()) {
<p>Hi {{ user()!.name }}</p>
} @else if (loading()) {
<p>Loading...</p>
} @else {
<button (click)="login()">Log in</button>
}
```

**React**

```tsx
{
  user ? (
    <p>Hi {user.name}</p>
  ) : loading ? (
    <p>Loading...</p>
  ) : (
    <button onClick={login}>Log in</button>
  );
}
```

**Vue.js**

```vue
<p v-if="user">Hi {{ user.name }}</p>
<p v-else-if="loading">Loading...</p>
<button v-else @click="login">Log in</button>
```

For more than two branches in React, nested ternaries get hard to read. Use early returns or a small helper function instead.

## 18: How do you translate @switch?

**Angular**

```html
@switch (status()) { @case ("loading") {
<p>Loading...</p>
} @case ("error") {
<p>Something went wrong</p>
} @default {
<p>Done</p>
} }
```

**React**

```tsx
function StatusView({ status }: { status: "loading" | "error" | "done" }) {
  switch (status) {
    case "loading":
      return <p>Loading...</p>;
    case "error":
      return <p>Something went wrong</p>;
    default:
      return <p>Done</p>;
  }
}
```

**Vue.js**

```vue
<p v-if="status === 'loading'">Loading...</p>
<p v-else-if="status === 'error'">Something went wrong</p>
<p v-else>Done</p>
```

Vue has no switch directive, so you chain `v-if`/`v-else-if`. In React you can also use a lookup object: `const views = { loading: <Spinner />, error: <ErrorBox /> }`.

## 19: How do you translate @for?

**Angular**

```html
<ul>
  @for (item of items(); track item.id) {
  <li>{{ item.name }}</li>
  }
</ul>
```

**React**

```tsx
<ul>
  {items.map((item) => (
    <li key={item.id}>{item.name}</li>
  ))}
</ul>
```

**Vue.js**

```vue
<ul>
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</ul>
```

## 20: How does track in Angular compare to key in React and Vue?

They solve the same problem. They tell the framework which item is which, so it can reuse DOM nodes when the list changes instead of recreating them. `track item.id` maps to `key={item.id}` in React and `:key="item.id"` in Vue.

Angular makes `track` required. React warns in the console if `key` is missing. Vue lint rules require `:key` with `v-for` on components. In all three, avoid the index as the key when items can be reordered, inserted or removed, because state and focus will stick to the wrong item.

## 21: How do you translate @empty in a @for loop?

**Angular**

```html
@for (todo of todos(); track todo.id) {
<li>{{ todo.title }}</li>
} @empty {
<li>No todos yet</li>
}
```

**React**

```tsx
{
  todos.length === 0 ? (
    <li>No todos yet</li>
  ) : (
    todos.map((todo) => <li key={todo.id}>{todo.title}</li>)
  );
}
```

**Vue.js**

```vue
<li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
<li v-if="todos.length === 0">No todos yet</li>
```

## 22: How do you translate loop variables like $index, $first and $last?

**Angular**

```html
@for (user of users(); track user.id; let i = $index, last = $last) {
<span>{{ i + 1 }}. {{ user.name }}@if (!last) {, }</span>
}
```

**React**

```tsx
{
  users.map((user, i) => (
    <span key={user.id}>
      {i + 1}. {user.name}
      {i < users.length - 1 && ", "}
    </span>
  ));
}
```

**Vue.js**

```vue
<span v-for="(user, i) in users" :key="user.id">
  {{ i + 1 }}. {{ user.name }}<template v-if="i < users.length - 1">, </template>
</span>
```

React and Vue only give you the index. You compute `first`, `last`, `even` and `odd` yourself from the index and the length.

## 23: How do template reference variables translate?

Angular's `#name` gives the template direct access to an element. React uses `useRef`. Vue uses a `ref` attribute with `useTemplateRef` (Vue 3.5+).

**Angular**

```html
<input #search /> <button (click)="find(search.value)">Find</button>
```

**React**

```tsx
const searchRef = useRef<HTMLInputElement>(null);
return (
  <>
    <input ref={searchRef} />
    <button onClick={() => find(searchRef.current!.value)}>Find</button>
  </>
);
```

**Vue.js**

```vue
<script setup lang="ts">
import { useTemplateRef } from "vue";
const search = useTemplateRef<HTMLInputElement>("search");
</script>

<template>
  <input ref="search" />
  <button @click="find(search!.value)">Find</button>
</template>
```

## 24: How do you translate component inputs?

**Angular**

```ts
@Component({
  selector: "app-user-card",
  template: `<h3>{{ name() }}</h3>
    <p>{{ email() }}</p>`,
})
export class UserCard {
  name = input("");
  email = input("");
}
// usage: <app-user-card [name]="u.name" [email]="u.email" />
```

**React**

```tsx
type Props = { name: string; email: string };

export function UserCard({ name, email }: Props) {
  return (
    <>
      <h3>{name}</h3>
      <p>{email}</p>
    </>
  );
}
// usage: <UserCard name={u.name} email={u.email} />
```

**Vue.js**

```vue
<script setup lang="ts">
defineProps<{ name: string; email: string }>();
</script>

<template>
  <h3>{{ name }}</h3>
  <p>{{ email }}</p>
</template>
<!-- usage: <UserCard :name="u.name" :email="u.email" /> -->
```

## 25: How do you translate required inputs?

**Angular**

```ts
export class Product {
  productId = input.required<number>();
}
```

**React**

```tsx
type Props = { productId: number }; // required: no "?"
export function Product({ productId }: Props) {
  /* ... */
}
```

**Vue.js**

```vue
<script setup lang="ts">
defineProps<{ productId: number }>(); // required: no "?"
</script>
```

In React and Vue, a prop is required when its type has no `?`. TypeScript reports a missing required prop at build time, and Vue also warns at runtime in dev mode.

## 26: How do you translate default values for inputs?

**Angular**

```ts
export class Badge {
  color = input("gray");
  size = input<"sm" | "lg">("sm");
}
```

**React**

```tsx
type Props = { color?: string; size?: "sm" | "lg" };

export function Badge({ color = "gray", size = "sm" }: Props) {
  return <span className={`badge ${size}`} style={{ color }} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const { color = "gray", size = "sm" } = defineProps<{
  color?: string;
  size?: "sm" | "lg";
}>();
</script>
```

Vue 3.5+ supports defaults in the destructured `defineProps`, and the destructured values stay reactive. In older Vue code you will see `withDefaults(defineProps<...>(), { color: "gray" })`.

## 27: How do you translate input transforms like booleanAttribute?

**Angular**

```ts
import { booleanAttribute, numberAttribute, input } from "@angular/core";

export class Panel {
  collapsed = input(false, { transform: booleanAttribute });
  delay = input(0, { transform: numberAttribute });
}
// <app-panel collapsed delay="300" />
```

**React**

```tsx
type Props = { collapsed?: boolean; delay?: number };
// <Panel collapsed delay={300} />  -> JSX passes real types already
```

**Vue.js**

```vue
<script setup lang="ts">
defineProps<{ collapsed?: boolean; delay?: number }>();
</script>
<!-- <Panel collapsed :delay="300" />  Vue casts a bare boolean prop to true -->
```

JSX passes real JavaScript values, so you rarely need transforms. Vue casts boolean props for you. For other transforms, compute the value inside the component (`const ms = Number(delay)`).

## 28: How do you translate component outputs?

**Angular**

```ts
@Component({
  selector: "app-delete-button",
  template: `<button (click)="deleted.emit(id())">Delete</button>`,
})
export class DeleteButton {
  id = input.required<number>();
  deleted = output<number>();
}
// <app-delete-button [id]="1" (deleted)="remove($event)" />
```

**React**

```tsx
type Props = { id: number; onDeleted: (id: number) => void };

export function DeleteButton({ id, onDeleted }: Props) {
  return <button onClick={() => onDeleted(id)}>Delete</button>;
}
// <DeleteButton id={1} onDeleted={remove} />
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ id: number }>();
const emit = defineEmits<{ deleted: [id: number] }>();
</script>

<template>
  <button @click="emit('deleted', props.id)">Delete</button>
</template>
<!-- <DeleteButton :id="1" @deleted="remove" /> -->
```

React has no event system for components. The parent passes a callback prop, by convention named `onSomething`.

## 29: How do you translate model() two-way component binding?

**Angular**

```ts
@Component({
  selector: "app-rating",
  template: `@for (s of stars; track s) {
    <button (click)="value.set(s)">{{ s <= value() ? "★" : "☆" }}</button>
  }`,
})
export class Rating {
  value = model(0);
  stars = [1, 2, 3, 4, 5];
}
// <app-rating [(value)]="score" />
```

**React**

```tsx
type Props = { value: number; onChange: (v: number) => void };

export function Rating({ value, onChange }: Props) {
  return [1, 2, 3, 4, 5].map((s) => (
    <button key={s} onClick={() => onChange(s)}>
      {s <= value ? "★" : "☆"}
    </button>
  ));
}
// <Rating value={score} onChange={setScore} />
```

**Vue.js**

```vue
<script setup lang="ts">
const value = defineModel<number>({ default: 0 });
</script>

<template>
  <button v-for="s in 5" :key="s" @click="value = s">
    {{ s <= value ? "★" : "☆" }}
  </button>
</template>
<!-- <Rating v-model="score" /> -->
```

`model()` and `defineModel()` are almost the same idea. In React, the pair `value` + `onChange` is the standard pattern.

## 30: How do you translate content projection with ng-content?

**Angular**

```ts
@Component({
  selector: "app-card",
  template: `<div class="card"><ng-content /></div>`,
})
export class Card {}
// <app-card><p>Body text</p></app-card>
```

**React**

```tsx
export function Card({ children }: { children: React.ReactNode }) {
  return <div className="card">{children}</div>;
}
// <Card><p>Body text</p></Card>
```

**Vue.js**

```vue
<template>
  <div class="card"><slot /></div>
</template>
<!-- <Card><p>Body text</p></Card> -->
```

`<ng-content />` becomes the `children` prop in React and `<slot />` in Vue.

## 31: How do you translate multi-slot projection with select?

**Angular**

```ts
@Component({
  selector: "app-dialog",
  template: `
    <header><ng-content select="[dialog-title]" /></header>
    <main><ng-content /></main>
    <footer><ng-content select="[dialog-actions]" /></footer>
  `,
})
export class Dialog {}
```

**React**

```tsx
type Props = {
  title: React.ReactNode;
  actions: React.ReactNode;
  children: React.ReactNode;
};

export function Dialog({ title, actions, children }: Props) {
  return (
    <>
      <header>{title}</header>
      <main>{children}</main>
      <footer>{actions}</footer>
    </>
  );
}
// <Dialog title={<h2>Delete?</h2>} actions={<button>OK</button>}>Sure?</Dialog>
```

**Vue.js**

```vue
<template>
  <header><slot name="title" /></header>
  <main><slot /></main>
  <footer><slot name="actions" /></footer>
</template>
<!--
<Dialog>
  <template #title><h2>Delete?</h2></template>
  Sure?
  <template #actions><button>OK</button></template>
</Dialog>
-->
```

React passes extra JSX through normal props. Vue uses named slots.

## 32: How do you translate local component state from signal()?

**Angular**

```ts
export class Counter {
  count = signal(0);
}
```

**React**

```tsx
const [count, setCount] = useState(0);
```

**Vue.js**

```ts
const count = ref(0);
```

All three hold a value and update the UI when it changes. Angular reads with `count()`, React reads the variable `count` (a snapshot for this render), and Vue reads `count.value` in script and `count` in the template.

## 33: How do you translate signal.set() and signal.update()?

**Angular**

```ts
count.set(10);
count.update((n) => n + 1);
```

**React**

```tsx
setCount(10);
setCount((n) => n + 1);
```

**Vue.js**

```ts
count.value = 10;
count.value++;
```

In React, use the function form (`setCount(n => n + 1)`) whenever the new value depends on the old one, because state updates are batched and `count` is a snapshot.

## 34: How do you translate computed()?

**Angular**

```ts
export class Cart {
  items = signal<{ price: number; qty: number }[]>([]);
  total = computed(() =>
    this.items().reduce((sum, i) => sum + i.price * i.qty, 0),
  );
}
```

**React**

```tsx
const [items, setItems] = useState<{ price: number; qty: number }[]>([]);
const total = items.reduce((sum, i) => sum + i.price * i.qty, 0);
// or, if it is expensive:
const totalMemo = useMemo(
  () => items.reduce((s, i) => s + i.price * i.qty, 0),
  [items],
);
```

**Vue.js**

```ts
const items = ref<{ price: number; qty: number }[]>([]);
const total = computed(() =>
  items.value.reduce((sum, i) => sum + i.price * i.qty, 0),
);
```

In React, derived values are usually just variables computed during render. `useMemo` caches them when the calculation is slow. The React Compiler can add this memoization automatically.

## 35: How do you translate effect()?

**Angular**

```ts
export class Search {
  query = signal("");
  constructor() {
    effect(() => {
      localStorage.setItem("query", this.query());
    });
  }
}
```

**React**

```tsx
const [query, setQuery] = useState("");
useEffect(() => {
  localStorage.setItem("query", query);
}, [query]);
```

**Vue.js**

```ts
const query = ref("");
watchEffect(() => {
  localStorage.setItem("query", query.value);
});
```

Angular's `effect` and Vue's `watchEffect` track dependencies automatically. React's `useEffect` needs a dependency array that you write yourself (the ESLint hooks plugin checks it).

## 36: How do you update objects and arrays in state?

**Angular**

```ts
todos = signal<Todo[]>([]);

add(title: string) {
  this.todos.update((list) => [...list, { id: Date.now(), title, done: false }]);
}
toggle(id: number) {
  this.todos.update((list) => list.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
}
```

**React**

```tsx
const [todos, setTodos] = useState<Todo[]>([]);

const add = (title: string) =>
  setTodos((list) => [...list, { id: Date.now(), title, done: false }]);
const toggle = (id: number) =>
  setTodos((list) =>
    list.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
  );
```

**Vue.js**

```ts
const todos = ref<Todo[]>([]);

const add = (title: string) =>
  todos.value.push({ id: Date.now(), title, done: false });
const toggle = (id: number) => {
  const t = todos.value.find((t) => t.id === id);
  if (t) t.done = !t.done;
};
```

Angular signals and React state need new references (immutable updates). Vue's reactivity uses proxies, so mutating the array or object directly works.

## 37: What replaces ngOnInit in React and Vue?

**Angular**

```ts
export class Profile implements OnInit {
  ngOnInit() {
    this.loadProfile();
  }
}
```

**React**

```tsx
useEffect(() => {
  loadProfile();
}, []); // empty array: run once after the first render
```

**Next.js**

```tsx
// Server Component: fetch while rendering, no lifecycle hook needed
export default async function ProfilePage() {
  const profile = await getProfile();
  return <h1>{profile.name}</h1>;
}
```

**Vue.js**

```ts
onMounted(() => {
  loadProfile();
});
// or just call loadProfile() at the top of <script setup>, which runs once on creation
```

In Angular, much of what used to go into `ngOnInit` now goes into the constructor, field initializers or `resource()`. Inputs are available as signals there, so `ngOnInit` is less needed than before.

## 38: What replaces ngOnDestroy and DestroyRef?

**Angular**

```ts
export class Clock {
  constructor() {
    const id = setInterval(() => this.tick(), 1000);
    inject(DestroyRef).onDestroy(() => clearInterval(id));
  }
}
```

**React**

```tsx
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id); // cleanup on unmount
}, []);
```

**Vue.js**

```ts
const id = setInterval(tick, 1000);
onUnmounted(() => clearInterval(id));
```

In React the cleanup function returned from `useEffect` also runs before the effect runs again, not only on unmount.

## 39: What replaces ngOnChanges?

**Angular**

```ts
export class Chart {
  data = input<number[]>([]);
  constructor() {
    effect(() => this.redraw(this.data())); // modern: react to input signal
  }
  // legacy: ngOnChanges(changes: SimpleChanges) { if (changes['data']) this.redraw(); }
}
```

**React**

```tsx
function Chart({ data }: { data: number[] }) {
  useEffect(() => {
    redraw(data);
  }, [data]);
}
```

**Vue.js**

```ts
const props = defineProps<{ data: number[] }>();
watch(
  () => props.data,
  (newData, oldData) => redraw(newData),
);
```

If the "change" only affects what is shown, you do not need any of these. Compute it directly with `computed()` or during render.

## 40: What replaces ngAfterViewInit and afterNextRender?

**Angular**

```ts
export class Map {
  container = viewChild.required<ElementRef<HTMLDivElement>>("container");
  constructor() {
    afterNextRender(() => initMap(this.container().nativeElement));
  }
}
```

**React**

```tsx
function Map() {
  const container = useRef<HTMLDivElement>(null);
  useEffect(() => {
    initMap(container.current!);
  }, []);
  return <div ref={container} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { onMounted, useTemplateRef } from "vue";
const container = useTemplateRef<HTMLDivElement>("container");
onMounted(() => initMap(container.value!));
</script>

<template><div ref="container" /></template>
```

Use `useLayoutEffect` in React only when you must measure or change the DOM before the browser paints.

## 41: How do you translate viewChild()?

**Angular**

```ts
export class Player {
  video = viewChild<ElementRef<HTMLVideoElement>>("video");
  play() {
    this.video()?.nativeElement.play();
  }
}
// template: <video #video src="movie.mp4"></video>
```

**React**

```tsx
function Player() {
  const video = useRef<HTMLVideoElement>(null);
  return (
    <>
      <video ref={video} src="movie.mp4" />
      <button onClick={() => video.current?.play()}>Play</button>
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { useTemplateRef } from "vue";
const video = useTemplateRef<HTMLVideoElement>("video");
</script>

<template>
  <video ref="video" src="movie.mp4" />
  <button @click="video?.play()">Play</button>
</template>
```

## 42: How do you focus an input when the component appears?

**Angular**

```ts
@Component({ template: `<input #box />` })
export class AutoFocus {
  box = viewChild.required<ElementRef<HTMLInputElement>>("box");
  constructor() {
    afterNextRender(() => this.box().nativeElement.focus());
  }
}
```

**React**

```tsx
function AutoFocus() {
  const box = useRef<HTMLInputElement>(null);
  useEffect(() => box.current?.focus(), []);
  return <input ref={box} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { onMounted, useTemplateRef } from "vue";
const box = useTemplateRef<HTMLInputElement>("box");
onMounted(() => box.value?.focus());
</script>

<template><input ref="box" /></template>
```

For the simple case, the HTML `autoFocus` (React) or `autofocus` attribute is enough in all of them.

## 43: How do you translate an Angular service?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class CounterService {
  readonly count = signal(0);
  increment() {
    this.count.update((n) => n + 1);
  }
}
```

**React**

```tsx
// A custom hook for logic that is local to each component that uses it
export function useCounter() {
  const [count, setCount] = useState(0);
  return { count, increment: () => setCount((n) => n + 1) };
}
```

**Vue.js**

```ts
// A composable
export function useCounter() {
  const count = ref(0);
  return { count, increment: () => count.value++ };
}
```

Careful: a root Angular service is a singleton, so every component sees the same `count`. A hook or composable like the above creates new state per call. For shared state, see the next questions (context, a store, or module-level state).

## 44: What replaces inject()?

**Angular**

```ts
export class Header {
  private auth = inject(AuthService);
}
```

**React**

```tsx
const AuthContext = createContext<AuthApi | null>(null);

function Header() {
  const auth = useContext(AuthContext); // or use(AuthContext) in React 19
}
```

**Vue.js**

```ts
// In a parent: provide(AuthKey, authApi)
const auth = inject(AuthKey);
```

React context and Vue `provide`/`inject` give you DI-like lookups up the component tree. For simple singletons, many React and Vue apps just import a module or a store (`useAuthStore()`) instead.

## 45: How do you share state between components like a root service?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class CartStore {
  readonly items = signal<string[]>([]);
  add(item: string) {
    this.items.update((list) => [...list, item]);
  }
}
```

**React**

```tsx
// with Zustand (a small store library)
import { create } from "zustand";

export const useCartStore = create<{
  items: string[];
  add: (i: string) => void;
}>((set) => ({
  items: [],
  add: (item) => set((s) => ({ items: [...s.items, item] })),
}));
// const items = useCartStore((s) => s.items);
```

**Vue.js**

```ts
// with Pinia (the official store)
import { defineStore } from "pinia";

export const useCartStore = defineStore("cart", () => {
  const items = ref<string[]>([]);
  const add = (item: string) => items.value.push(item);
  return { items, add };
});
```

Pinia setup stores look very close to an Angular signal service. In React you can also use context plus `useState` for small cases.

## 46: What replaces Angular pipes?

Plain functions. React and Vue have no pipe concept. Vue 2 had filters, but they were removed in Vue 3.

**Angular**

```html
<p>{{ title() | uppercase }}</p>
```

**React**

```tsx
<p>{title.toUpperCase()}</p>
```

**Vue.js**

```vue
<p>{{ title.toUpperCase() }}</p>
```

For reused formatting, write a helper like `formatPrice(value)` in a `utils` file and import it.

## 47: How do you translate the date and currency pipes?

**Angular**

```html
<p>{{ order().createdAt | date: "mediumDate" }}</p>
<p>{{ order().total | currency: "EUR" }}</p>
```

**React**

```tsx
const dateFmt = new Intl.DateTimeFormat("en-US", { dateStyle: "medium" });
const eur = new Intl.NumberFormat("en-US", { style: "currency", currency: "EUR" });

<p>{dateFmt.format(new Date(order.createdAt))}</p>
<p>{eur.format(order.total)}</p>
```

**Vue.js**

```vue
<script setup lang="ts">
const dateFmt = new Intl.DateTimeFormat("en-US", { dateStyle: "medium" });
const eur = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "EUR",
});
</script>

<template>
  <p>{{ dateFmt.format(new Date(order.createdAt)) }}</p>
  <p>{{ eur.format(order.total) }}</p>
</template>
```

The built-in `Intl` API does what Angular's pipes do. Create the formatter once (outside the component or in a module) because creating it is slow.

## 48: How do you translate the json pipe used for debugging?

**Angular**

```html
<pre>{{ user() | json }}</pre>
```

**React**

```tsx
<pre>{JSON.stringify(user, null, 2)}</pre>
```

**Vue.js**

```vue
<pre>{{ user }}</pre>
```

Vue prints objects as formatted JSON by default when you interpolate them. React would throw if you render a plain object, so you must stringify it.

## 49: What replaces the async pipe?

**Angular**

```ts
@Component({
  imports: [AsyncPipe],
  template: `@if (user$ | async; as user) {
    <p>{{ user.name }}</p>
  }`,
})
export class UserView {
  user$ = inject(UserService).getUser();
}
```

**React**

```tsx
function UserView() {
  const [user, setUser] = useState<User | null>(null);
  useEffect(() => {
    const sub = userService.getUser().subscribe(setUser);
    return () => sub.unsubscribe();
  }, []);
  return user && <p>{user.name}</p>;
}
```

**Vue.js**

```ts
// with VueUse: import { useObservable } from "@vueuse/rxjs";
const user = useObservable(userService.getUser());
```

Most translated code drops observables and uses promises with a data library (TanStack Query in React, or `fetch` in a composable in Vue). In Angular itself, `toSignal()` is the modern replacement for the async pipe.

## 50: How do you translate a custom pipe?

**Angular**

```ts
@Pipe({ name: "truncate" })
export class TruncatePipe implements PipeTransform {
  transform(value: string, max = 20) {
    return value.length > max ? value.slice(0, max) + "..." : value;
  }
}
// {{ text | truncate: 10 }}
```

**React**

```tsx
export const truncate = (value: string, max = 20) =>
  value.length > max ? value.slice(0, max) + "..." : value;
// <p>{truncate(text, 10)}</p>
```

**Vue.js**

```vue
<script setup lang="ts">
import { truncate } from "@/utils/text";
</script>

<template>
  <p>{{ truncate(text, 10) }}</p>
</template>
```

Pure pipes are cached by Angular. If the function is slow, wrap the call in `useMemo` (React) or a `computed` (Vue).

## 51: How do you translate an attribute directive?

**Angular**

```ts
@Directive({
  selector: "[appHighlight]",
  host: { "[style.backgroundColor]": "color()" },
})
export class Highlight {
  color = input("yellow", { alias: "appHighlight" });
}
// <p appHighlight="lightblue">Text</p>
```

**React**

```tsx
// No directives in React. Use a wrapper component or a hook that returns props.
function Highlight({
  color = "yellow",
  children,
}: {
  color?: string;
  children: React.ReactNode;
}) {
  return <p style={{ backgroundColor: color }}>{children}</p>;
}
```

**Vue.js**

```ts
// Vue has custom directives
const vHighlight = {
  mounted: (el: HTMLElement, binding: { value?: string }) => {
    el.style.backgroundColor = binding.value ?? "yellow";
  },
  updated: (el: HTMLElement, binding: { value?: string }) => {
    el.style.backgroundColor = binding.value ?? "yellow";
  },
};
// <p v-highlight="'lightblue'">Text</p>
```

Vue directives are only for low-level DOM work. In React, behavior is shared with components and hooks.

## 52: What replaces @HostListener or host event bindings?

**Angular**

```ts
@Directive({
  selector: "[appTrackClicks]",
  host: { "(click)": "onClick()" },
})
export class TrackClicks {
  onClick() {
    console.log("clicked");
  }
}
```

**React**

```tsx
// Put the handler on the element itself
<button onClick={() => console.log("clicked")}>Buy</button>
```

**Vue.js**

```vue
<button @click="console.log('clicked')">Buy</button>
```

In Angular, `host: {}` in the decorator is the modern form and `@HostListener` is the older one. In React and Vue you put the listener on the root element of the component.

## 53: How do you translate ngClass?

**Angular**

```html
<!-- legacy NgClass, still common -->
<div [ngClass]="{ 'is-open': open(), 'is-dark': theme() === 'dark' }"></div>
<!-- modern: [class] accepts the same object -->
<div [class]="{ 'is-open': open(), 'is-dark': theme() === 'dark' }"></div>
```

**React**

```tsx
import clsx from "clsx";
<div className={clsx({ "is-open": open, "is-dark": theme === "dark" })} />;
```

**Vue.js**

```vue
<div :class="{ 'is-open': open, 'is-dark': theme === 'dark' }" />
```

## 54: How do you translate ngStyle?

**Angular**

```html
<div [style]="{ 'font-size.px': size(), color: color() }"></div>
<div [ngStyle]="{ 'font-size.px': size(), color: color() }"></div>
```

**React**

```tsx
<div style={{ fontSize: size, color }} />
```

**Vue.js**

```vue
<div :style="{ fontSize: size + 'px', color }" />
```

The Angular unit suffix (`.px`) has no match in React or Vue. React adds `px` to numeric values for most properties, and in Vue you add the unit yourself.

## 55: How do component styles translate?

Angular scopes styles to the component by default (emulated encapsulation). Vue has `<style scoped>`, which works almost the same way. React has no built-in scoping, so you use CSS Modules, Tailwind or a CSS-in-JS library. Next.js supports CSS Modules out of the box.

**Angular**

```ts
@Component({
  selector: "app-alert",
  template: `<div class="box">Warning</div>`,
  styles: `
    .box {
      color: red;
    }
  `,
})
export class Alert {}
```

**React**

```tsx
// Alert.module.css -> .box { color: red; }
import styles from "./Alert.module.css";

export function Alert() {
  return <div className={styles.box}>Warning</div>;
}
```

**Vue.js**

```vue
<template><div class="box">Warning</div></template>

<style scoped>
.box {
  color: red;
}
</style>
```

## 56: What replaces the :host selector?

**Angular**

```css
:host {
  display: block;
  padding: 1rem;
}
:host(.compact) {
  padding: 0.25rem;
}
```

**React**

```css
/* Card.module.css: style the root element with its own class */
.root {
  display: block;
  padding: 1rem;
}
.compact {
  padding: 0.25rem;
}
```

**Vue.js**

```vue
<template>
  <div class="root" :class="{ compact }"><slot /></div>
</template>

<style scoped>
.root {
  display: block;
  padding: 1rem;
}
.root.compact {
  padding: 0.25rem;
}
</style>
```

React and Vue components have no host element. The component's outer element plays that role, so you give it a class.

## 57: How do you add global styles?

**Angular**

```json
// angular.json -> "styles": ["src/styles.css"]
```

**React**

```tsx
// main.tsx
import "./index.css";
```

**Next.js**

```tsx
// app/layout.tsx (global CSS can be imported in any file inside app/, usually the root layout)
import "./globals.css";
```

**Vue.js**

```ts
// main.ts
import "./assets/main.css";
```

## 58: How do you set up routing?

**Angular**

```ts
// app.routes.ts
export const routes: Routes = [
  { path: "", component: Home },
  { path: "about", component: About },
];
// app.config.ts
export const appConfig = { providers: [provideRouter(routes)] };
// app.html: <router-outlet />
```

**React**

```tsx
// React Router (v7, "data" or "declarative" mode)
import { createBrowserRouter, RouterProvider } from "react-router";

const router = createBrowserRouter([
  { path: "/", element: <Home /> },
  { path: "/about", element: <About /> },
]);

createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router} />,
);
```

**Next.js**

```text
app/page.tsx        -> "/"
app/about/page.tsx  -> "/about"
```

**Vue.js**

```ts
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/about", component: About },
  ],
});
createApp(App).use(router).mount("#app");
// App.vue: <RouterView />
```

## 59: How do you translate routerLink?

**Angular**

```html
<a routerLink="/about">About</a>
<a [routerLink]="['/users', user.id]">Profile</a>
```

**React**

```tsx
import { Link } from "react-router";
<Link to="/about">About</Link>
<Link to={`/users/${user.id}`}>Profile</Link>
```

**Next.js**

```tsx
import Link from "next/link";
<Link href="/about">About</Link>
<Link href={`/users/${user.id}`}>Profile</Link>
```

**Vue.js**

```vue
<RouterLink to="/about">About</RouterLink>
<RouterLink :to="{ name: 'user', params: { id: user.id } }">Profile</RouterLink>
```

## 60: How do you translate routerLinkActive?

**Angular**

```html
<a routerLink="/inbox" routerLinkActive="active">Inbox</a>
```

**React**

```tsx
import { NavLink } from "react-router";
<NavLink to="/inbox" className={({ isActive }) => (isActive ? "active" : "")}>
  Inbox
</NavLink>;
```

**Next.js**

```tsx
"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

export function NavItem() {
  const pathname = usePathname();
  return (
    <Link
      href="/inbox"
      className={pathname.startsWith("/inbox") ? "active" : ""}
    >
      Inbox
    </Link>
  );
}
```

**Vue.js**

```vue
<!-- RouterLink adds "router-link-active" automatically, or set your own class -->
<RouterLink to="/inbox" active-class="active">Inbox</RouterLink>
```

## 61: How do you read route parameters?

**Angular**

```ts
// route: { path: "users/:id", component: UserDetail }
export class UserDetail {
  private route = inject(ActivatedRoute);
  id = toSignal(this.route.paramMap.pipe(map((p) => p.get("id"))));
  // or with withComponentInputBinding(): id = input<string>();
}
```

**React**

```tsx
import { useParams } from "react-router";

function UserDetail() {
  const { id } = useParams();
  return <h1>User {id}</h1>;
}
```

**Next.js**

```tsx
// app/users/[id]/page.tsx
export default async function UserDetail({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <h1>User {id}</h1>;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { useRoute } from "vue-router";
const route = useRoute();
</script>

<template>
  <h1>User {{ route.params.id }}</h1>
</template>
```

In Next.js 15 and later, `params` is a Promise, so you `await` it (or use React's `use()` in a client component).

## 62: How do you read query parameters?

**Angular**

```ts
private route = inject(ActivatedRoute);
page = toSignal(this.route.queryParamMap.pipe(map((q) => Number(q.get("page") ?? 1))));
```

**React**

```tsx
import { useSearchParams } from "react-router";
const [searchParams] = useSearchParams();
const page = Number(searchParams.get("page") ?? 1);
```

**Next.js**

```tsx
// Server Component page
export default async function List({
  searchParams,
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const page = Number((await searchParams).page ?? 1);
}
// Client Component: const page = useSearchParams().get("page");
```

**Vue.js**

```ts
const route = useRoute();
const page = computed(() => Number(route.query.page ?? 1));
```

## 63: How do you navigate from code?

**Angular**

```ts
private router = inject(Router);
save() {
  this.router.navigate(["/users", this.id()], { queryParams: { tab: "info" } });
}
```

**React**

```tsx
import { useNavigate } from "react-router";
const navigate = useNavigate();
const save = () => navigate(`/users/${id}?tab=info`);
```

**Next.js**

```tsx
"use client";
import { useRouter } from "next/navigation";
const router = useRouter();
const save = () => router.push(`/users/${id}?tab=info`);
// in a Server Action or Server Component: redirect(`/users/${id}`) from "next/navigation"
```

**Vue.js**

```ts
const router = useRouter();
const save = () =>
  router.push({ path: `/users/${id}`, query: { tab: "info" } });
```

## 64: How do you translate nested routes and router-outlet?

**Angular**

```ts
{
  path: "settings",
  component: SettingsShell, // template has <router-outlet />
  children: [
    { path: "profile", component: Profile },
    { path: "security", component: Security },
  ],
}
```

**React**

```tsx
import { Outlet } from "react-router";

const routes = [
  {
    path: "/settings",
    element: <SettingsShell />,
    children: [
      { path: "profile", element: <Profile /> },
      { path: "security", element: <Security /> },
    ],
  },
];

function SettingsShell() {
  return (
    <div>
      <nav>...</nav>
      <Outlet />
    </div>
  );
}
```

**Next.js**

```tsx
// app/settings/layout.tsx wraps app/settings/profile/page.tsx and app/settings/security/page.tsx
export default function SettingsLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <nav>...</nav>
      {children}
    </div>
  );
}
```

**Vue.js**

```ts
{
  path: "/settings",
  component: SettingsShell, // template has <RouterView />
  children: [
    { path: "profile", component: Profile },
    { path: "security", component: Security },
  ],
}
```

## 65: How do you translate a wildcard 404 route?

**Angular**

```ts
{ path: "**", component: NotFound }
```

**React**

```tsx
{ path: "*", element: <NotFound /> }
```

**Next.js**

```tsx
// app/not-found.tsx
export default function NotFound() {
  return <h1>Page not found</h1>;
}
// Call notFound() from "next/navigation" inside a page to show it on purpose.
```

**Vue.js**

```ts
{ path: "/:pathMatch(.*)*", name: "not-found", component: NotFound }
```

## 66: How do you translate route redirects?

**Angular**

```ts
{ path: "", redirectTo: "dashboard", pathMatch: "full" }
```

**React**

```tsx
import { Navigate } from "react-router";
{ index: true, element: <Navigate to="/dashboard" replace /> }
```

**Next.js**

```ts
// next.config.ts
const nextConfig = {
  async redirects() {
    return [{ source: "/", destination: "/dashboard", permanent: false }];
  },
};
export default nextConfig;
```

**Vue.js**

```ts
{ path: "/", redirect: "/dashboard" }
```

## 67: How do you translate lazy-loaded routes?

**Angular**

```ts
{
  path: "admin",
  loadComponent: () => import("./admin/admin").then((m) => m.Admin),
}
// or loadChildren: () => import("./admin/admin.routes").then((m) => m.ADMIN_ROUTES)
```

**React**

```tsx
{
  path: "admin",
  lazy: async () => {
    const { Admin } = await import("./admin/Admin");
    return { Component: Admin };
  },
}
```

**Next.js**

Every route in `app/` is code-split automatically. You do nothing.

**Vue.js**

```ts
{ path: "/admin", component: () => import("./views/AdminView.vue") }
```

## 68: How do you translate an HTTP GET with HttpClient?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class UserApi {
  private http = inject(HttpClient);
  getUsers() {
    return this.http.get<User[]>("/api/users");
  }
}
```

**React**

```tsx
export async function getUsers(): Promise<User[]> {
  const res = await fetch("/api/users");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

**Next.js**

```tsx
// app/users/page.tsx (Server Component, runs on the server)
export default async function UsersPage() {
  const res = await fetch("https://api.example.com/users");
  const users: User[] = await res.json();
  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li>
      ))}
    </ul>
  );
}
```

**Vue.js**

```ts
export async function getUsers(): Promise<User[]> {
  const res = await fetch("/api/users");
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

Unlike `HttpClient`, `fetch` does not throw on 4xx/5xx and does not parse JSON for you, so check `res.ok` yourself. Some teams use `axios` or `ky` to get closer to `HttpClient`.

## 69: How do you translate an HTTP POST?

**Angular**

```ts
createUser(user: NewUser) {
  return this.http.post<User>("/api/users", user);
}
```

**React**

```tsx
export async function createUser(user: NewUser): Promise<User> {
  const res = await fetch("/api/users", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

**Next.js**

```tsx
// app/users/actions.ts
"use server";
export async function createUser(formData: FormData) {
  await db.user.create({ data: { name: String(formData.get("name")) } });
}
// <form action={createUser}>...</form>
```

**Vue.js**

Same `fetch` code as React.

## 70: How do you show loading and error states for a request?

**Angular**

```ts
@Component({
  template: `
    @if (users.isLoading()) {
      <p>Loading...</p>
    } @else if (users.error()) {
      <p>Error!</p>
    } @else {
      @for (u of users.value(); track u.id) {
        <p>{{ u.name }}</p>
      }
    }
  `,
})
export class Users {
  users = httpResource<User[]>(() => "/api/users", { defaultValue: [] });
}
```

**React**

```tsx
import { useQuery } from "@tanstack/react-query";

function Users() {
  const { data, isPending, error } = useQuery({
    queryKey: ["users"],
    queryFn: getUsers,
  });
  if (isPending) return <p>Loading...</p>;
  if (error) return <p>Error!</p>;
  return data.map((u) => <p key={u.id}>{u.name}</p>);
}
```

**Next.js**

```tsx
// app/users/loading.tsx shows while page.tsx awaits data
export default function Loading() {
  return <p>Loading...</p>;
}
// app/users/error.tsx ("use client") shows if page.tsx throws
```

**Vue.js**

```vue
<script setup lang="ts">
import { useQuery } from "@tanstack/vue-query";
const { data, isPending, error } = useQuery({
  queryKey: ["users"],
  queryFn: getUsers,
});
</script>

<template>
  <p v-if="isPending">Loading...</p>
  <p v-else-if="error">Error!</p>
  <p v-else v-for="u in data" :key="u.id">{{ u.name }}</p>
</template>
```

## 71: How do environment files translate?

**Angular**

```ts
// src/environments/environment.ts (swapped by fileReplacements in angular.json)
export const environment = { apiUrl: "http://localhost:3000" };
```

**React**

```ts
// .env -> VITE_API_URL=http://localhost:3000
const apiUrl = import.meta.env.VITE_API_URL;
```

**Next.js**

```ts
// .env.local -> NEXT_PUBLIC_API_URL=...  (visible in the browser)
//               DB_PASSWORD=...           (server only)
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
```

**Vue.js**

```ts
// Vite: .env -> VITE_API_URL=...
const apiUrl = import.meta.env.VITE_API_URL;
```

Only prefixed variables (`VITE_`, `NEXT_PUBLIC_`) reach browser code. Everything in Angular's `environment.ts` is shipped to the browser, so never put secrets there.

## 72: How do you translate a template-driven form field?

**Angular**

```ts
@Component({
  imports: [FormsModule],
  template: `<input name="email" [(ngModel)]="email" required email />`,
})
export class Signup {
  email = "";
}
```

**React**

```tsx
const [email, setEmail] = useState("");
<input
  name="email"
  type="email"
  required
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>;
```

**Vue.js**

```vue
<input v-model="email" name="email" type="email" required />
```

## 73: How do you bind a checkbox?

**Angular**

```html
<input type="checkbox" [(ngModel)]="agree" />
```

**React**

```tsx
<input
  type="checkbox"
  checked={agree}
  onChange={(e) => setAgree(e.target.checked)}
/>
```

**Vue.js**

```vue
<input v-model="agree" type="checkbox" />
<!-- with an array ref, v-model collects the checked values -->
<input v-model="colors" type="checkbox" value="red" />
```

In React, use `checked` and `e.target.checked`, not `value`.

## 74: How do you bind a select dropdown?

**Angular**

```html
<select [(ngModel)]="country">
  @for (c of countries; track c.code) {
  <option [value]="c.code">{{ c.name }}</option>
  }
</select>
```

**React**

```tsx
<select value={country} onChange={(e) => setCountry(e.target.value)}>
  {countries.map((c) => (
    <option key={c.code} value={c.code}>
      {c.name}
    </option>
  ))}
</select>
```

**Vue.js**

```vue
<select v-model="country">
  <option v-for="c in countries" :key="c.code" :value="c.code">{{ c.name }}</option>
</select>
```

React sets the selected option with `value` on the `<select>`, not with `selected` on the `<option>`.

## 75: How do you bind radio buttons?

**Angular**

```html
<label
  ><input type="radio" name="size" value="s" [(ngModel)]="size" /> Small</label
>
<label
  ><input type="radio" name="size" value="l" [(ngModel)]="size" /> Large</label
>
```

**React**

```tsx
{
  ["s", "l"].map((v) => (
    <label key={v}>
      <input
        type="radio"
        name="size"
        value={v}
        checked={size === v}
        onChange={() => setSize(v)}
      />
      {v === "s" ? "Small" : "Large"}
    </label>
  ));
}
```

**Vue.js**

```vue
<label><input v-model="size" type="radio" value="s" /> Small</label>
<label><input v-model="size" type="radio" value="l" /> Large</label>
```

## 76: How do you handle form submit?

**Angular**

```html
<form (ngSubmit)="save()">
  <input name="title" [(ngModel)]="title" />
  <button type="submit">Save</button>
</form>
```

**React**

```tsx
<form
  onSubmit={(e) => {
    e.preventDefault();
    save();
  }}
>
  <input value={title} onChange={(e) => setTitle(e.target.value)} />
  <button type="submit">Save</button>
</form>
```

**Next.js**

```tsx
// Server Action, no preventDefault needed, works without JavaScript too
<form action={saveTitle}>
  <input name="title" />
  <button type="submit">Save</button>
</form>
```

**Vue.js**

```vue
<form @submit.prevent="save">
  <input v-model="title" />
  <button type="submit">Save</button>
</form>
```

Angular's `ngSubmit` prevents the page reload for you. In React you call `e.preventDefault()`. In Vue the `.prevent` modifier does it. React 19 also accepts a function in `<form action={fn}>` on the client.

## 77: How do you prevent default and stop propagation?

**Angular**

```html
<a href="#" (click)="$event.preventDefault(); open()">Open</a>
<div (click)="$event.stopPropagation()">...</div>
```

**React**

```tsx
<a href="#" onClick={(e) => { e.preventDefault(); open(); }}>Open</a>
<div onClick={(e) => e.stopPropagation()}>...</div>
```

**Vue.js**

```vue
<a href="#" @click.prevent="open">Open</a>
<div @click.stop>...</div>
```

## 78: How do you translate key event filtering like keyup.enter?

**Angular**

```html
<input (keyup.enter)="search()" (keydown.escape)="clear()" />
```

**React**

```tsx
<input
  onKeyUp={(e) => e.key === "Enter" && search()}
  onKeyDown={(e) => e.key === "Escape" && clear()}
/>
```

**Vue.js**

```vue
<input @keyup.enter="search" @keydown.esc="clear" />
```

Vue key modifiers match Angular's pseudo-events closely. React needs a check on `e.key`.

## 79: How do you translate the required validator?

**Angular**

```ts
form = new FormGroup({
  name: new FormControl("", {
    nonNullable: true,
    validators: [Validators.required],
  }),
});
```

**React**

```tsx
// with React Hook Form
const {
  register,
  formState: { errors },
} = useForm<{ name: string }>();
<input {...register("name", { required: "Name is required" })} />;
```

**Vue.js**

```vue
<!-- with VeeValidate -->
<script setup lang="ts">
import { useField } from "vee-validate";
const { value: name, errorMessage } = useField<string>(
  "name",
  (v) => !!v || "Name is required",
);
</script>

<template>
  <input v-model="name" />
  <span>{{ errorMessage }}</span>
</template>
```

For tiny forms you can skip libraries and use the native `required` attribute in all of them.

## 80: How do you show validation errors?

**Angular**

```html
<input [formControl]="form.controls.email" />
@if (form.controls.email.touched && form.controls.email.hasError("required")) {
<small>Email is required</small>
}
```

**React**

```tsx
<input {...register("email", { required: "Email is required" })} />;
{
  errors.email && <small>{errors.email.message}</small>;
}
```

**Vue.js**

```vue
<input v-model="email" @blur="handleBlur" />
<small v-if="errorMessage">{{ errorMessage }}</small>
```

## 81: How do you translate a simple reactive form?

**Angular**

```ts
@Component({
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()">
      <input formControlName="email" />
      <input formControlName="password" type="password" />
      <button [disabled]="form.invalid">Log in</button>
    </form>
  `,
})
export class Login {
  form = inject(FormBuilder).nonNullable.group({
    email: ["", [Validators.required, Validators.email]],
    password: ["", Validators.required],
  });
  submit() {
    console.log(this.form.getRawValue());
  }
}
```

**React**

```tsx
import { useForm } from "react-hook-form";

type LoginForm = { email: string; password: string };

export function Login() {
  const { register, handleSubmit, formState } = useForm<LoginForm>({
    mode: "onChange",
  });
  return (
    <form onSubmit={handleSubmit((v) => console.log(v))}>
      <input {...register("email", { required: true, pattern: /\S+@\S+/ })} />
      <input type="password" {...register("password", { required: true })} />
      <button disabled={!formState.isValid}>Log in</button>
    </form>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/zod";
import { z } from "zod";

const { defineField, handleSubmit, meta } = useForm({
  validationSchema: toTypedSchema(
    z.object({ email: z.string().email(), password: z.string().min(1) }),
  ),
});
const [email] = defineField("email");
const [password] = defineField("password");
const submit = handleSubmit((v) => console.log(v));
</script>

<template>
  <form @submit="submit">
    <input v-model="email" />
    <input v-model="password" type="password" />
    <button :disabled="!meta.valid">Log in</button>
  </form>
</template>
```

## 82: How do you disable a button based on state?

**Angular**

```html
<button [disabled]="!canSave()">Save</button>
```

**React**

```tsx
<button disabled={!canSave}>Save</button>
```

**Vue.js**

```vue
<button :disabled="!canSave">Save</button>
```

In Vue, `:disabled="false"` removes the attribute. In React, `disabled={false}` does too.

## 83: How do you render raw HTML?

**Angular**

```html
<div [innerHTML]="article().body"></div>
```

**React**

```tsx
<div dangerouslySetInnerHTML={{ __html: article.body }} />
```

**Vue.js**

```vue
<div v-html="article.body" />
```

Angular sanitizes `[innerHTML]` by default. React and Vue do not sanitize, so you must clean untrusted HTML yourself, for example with DOMPurify.

## 84: What replaces ng-container?

**Angular**

```html
<ng-container>
  <dt>{{ term }}</dt>
  <dd>{{ definition }}</dd>
</ng-container>
```

**React**

```tsx
<>
  <dt>{term}</dt>
  <dd>{definition}</dd>
</>
// with a key in lists: <Fragment key={id}>...</Fragment>
```

**Vue.js**

```vue
<template v-if="show">
  <dt>{{ term }}</dt>
  <dd>{{ definition }}</dd>
</template>
```

With Angular's control flow blocks (`@if`, `@for`), you need `ng-container` much less often, since the blocks do not add elements.

## 85: How do you translate ng-template with ngTemplateOutlet?

**Angular**

```ts
@Component({
  selector: "app-list",
  imports: [NgTemplateOutlet],
  template: `@for (item of items(); track item.id) {
    <ng-container *ngTemplateOutlet="itemTpl(); context: { $implicit: item }" />
  }`,
})
export class List<T extends { id: number }> {
  items = input<T[]>([]);
  itemTpl = input.required<TemplateRef<{ $implicit: T }>>();
}
// <app-list [items]="users" [itemTpl]="row" />
// <ng-template #row let-user><b>{{ user.name }}</b></ng-template>
```

**React**

```tsx
type Props<T> = { items: T[]; renderItem: (item: T) => React.ReactNode };

function List<T extends { id: number }>({ items, renderItem }: Props<T>) {
  return items.map((item) => (
    <Fragment key={item.id}>{renderItem(item)}</Fragment>
  ));
}
// <List items={users} renderItem={(user) => <b>{user.name}</b>} />
```

**Vue.js**

```vue
<script setup lang="ts" generic="T extends { id: number }">
defineProps<{ items: T[] }>();
</script>

<template>
  <template v-for="item in items" :key="item.id">
    <slot name="item" :item="item" />
  </template>
</template>
<!-- <List :items="users"><template #item="{ item }"><b>{{ item.name }}</b></template></List> -->
```

A template passed in becomes a "render prop" function in React and a "scoped slot" in Vue.

## 86: How do you render a component chosen at runtime?

**Angular**

```ts
@Component({
  imports: [NgComponentOutlet],
  template: `<ng-container
    *ngComponentOutlet="widget(); inputs: { title: 'Sales' }"
  />`,
})
export class Dashboard {
  widget = signal<Type<unknown>>(ChartWidget);
}
```

**React**

```tsx
const widgets = { chart: ChartWidget, table: TableWidget };

function Dashboard({ kind }: { kind: keyof typeof widgets }) {
  const Widget = widgets[kind]; // must start with a capital letter
  return <Widget title="Sales" />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { shallowRef } from "vue";
const widget = shallowRef(ChartWidget);
</script>

<template>
  <component :is="widget" title="Sales" />
</template>
```

Use `shallowRef` in Vue for component objects, so Vue does not make the whole component definition deeply reactive.

## 87: How do you show and hide an element without removing it?

**Angular**

```html
<div [hidden]="!showDetails()">Details</div>
```

**React**

```tsx
<div hidden={!showDetails}>Details</div>
// or style={{ display: showDetails ? undefined : "none" }}
```

**Vue.js**

```vue
<div v-show="showDetails">Details</div>
```

`v-show` toggles `display: none`. Unlike `v-if` or `@if`, the element and its state stay alive.

## 88: How does the safe navigation operator translate?

Angular templates support `?.`, and so does plain JavaScript. So the code is nearly identical.

**Angular**

```html
<p>{{ user()?.address?.city ?? "Unknown" }}</p>
```

**React**

```tsx
<p>{user?.address?.city ?? "Unknown"}</p>
```

**Vue.js**

```vue
<p>{{ user?.address?.city ?? "Unknown" }}</p>
```

## 89: How do you translate @let in templates?

**Angular**

```html
@let fullName = user().first + " " + user().last;
<h1>{{ fullName }}</h1>
<img [alt]="fullName" [src]="user().avatar" />
```

**React**

```tsx
function Header({ user }: { user: User }) {
  const fullName = `${user.first} ${user.last}`;
  return (
    <>
      <h1>{fullName}</h1>
      <img alt={fullName} src={user.avatar} />
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ user: User }>();
const fullName = computed(() => `${props.user.first} ${props.user.last}`);
</script>

<template>
  <h1>{{ fullName }}</h1>
  <img :alt="fullName" :src="user.avatar" />
</template>
```

In React, a `const` inside the function body is the natural place for template variables.

## 90: How do you import and use a child component?

**Angular**

```ts
import { UserCard } from "./user-card";

@Component({
  selector: "app-users",
  imports: [UserCard],
  template: `<app-user-card name="Ana" />`,
})
export class Users {}
```

**React**

```tsx
import { UserCard } from "./UserCard";

export function Users() {
  return <UserCard name="Ana" />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
import UserCard from "./UserCard.vue";
</script>

<template>
  <UserCard name="Ana" />
</template>
```

Angular needs the import in both the TypeScript file and the `imports` array. React and Vue only need the normal ES import. You use the component by its name, not by a selector.

## 91: How do naming conventions differ?

- **Angular:** kebab-case files (`user-card.ts`), PascalCase classes (`UserCard`), and a selector with a prefix (`app-user-card`). Since Angular 20 the style guide drops the `Component` suffix.
- **React:** PascalCase component files and names (`UserCard.tsx`). Hooks start with `use` (`useUser`). Event props start with `on`.
- **Next.js:** route files have fixed names (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`). Folder names become URL segments.
- **Vue.js:** PascalCase SFC files (`UserCard.vue`). Composables start with `use`. In templates you can write `<UserCard>` or `<user-card>`.

## 92: How do NgModules map to React and Vue?

They do not map to anything. NgModules grouped components and providers. Since Angular 19 standalone is the default, so modern Angular has the same idea as React and Vue: each component imports what it uses.

If the legacy app has modules, use them as a guide for folder structure. A `UsersModule` usually becomes a `features/users/` folder. Providers from a module become a context provider, a store, or a plain module export.

## 93: How do you pass data through many levels without passing props at every level?

**Angular**

```ts
// Parent provides a service; any child can inject it
@Component({ providers: [ThemeService], template: `<app-toolbar />` })
export class Shell {}

export class DeepButton {
  theme = inject(ThemeService);
}
```

**React**

```tsx
const ThemeContext = createContext<"light" | "dark">("light");

function Shell() {
  return (
    <ThemeContext value="dark">
      <Toolbar />
    </ThemeContext>
  );
}

function DeepButton() {
  const theme = use(ThemeContext);
  return <button className={theme}>OK</button>;
}
```

**Vue.js**

```ts
// Shell.vue
provide("theme", ref("dark"));
// DeepButton.vue
const theme = inject("theme");
```

React 19 lets you render `<ThemeContext value=...>` directly. Older code uses `<ThemeContext.Provider value=...>`.

## 94: How does a child send data to its parent?

**Angular**

```ts
export class SearchBox {
  search = output<string>();
}
// parent: <app-search-box (search)="onSearch($event)" />
```

**React**

```tsx
function SearchBox({ onSearch }: { onSearch: (q: string) => void }) {
  return (
    <input
      onKeyDown={(e) => e.key === "Enter" && onSearch(e.currentTarget.value)}
    />
  );
}
// parent: <SearchBox onSearch={handleSearch} />
```

**Vue.js**

```vue
<script setup lang="ts">
const emit = defineEmits<{ search: [q: string] }>();
</script>
<template>
  <input
    @keydown.enter="emit('search', ($event.target as HTMLInputElement).value)"
  />
</template>
<!-- parent: <SearchBox @search="handleSearch" /> -->
```

## 95: How do sibling components communicate?

In all four, you lift the state up to the closest common parent, or put it in a shared service or store.

**Angular**

```ts
@Component({
  template: `<app-filter [(value)]="filter" />
    <app-results [filter]="filter()" />`,
})
export class Page {
  filter = signal("");
}
```

**React**

```tsx
function Page() {
  const [filter, setFilter] = useState("");
  return (
    <>
      <Filter value={filter} onChange={setFilter} />
      <Results filter={filter} />
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const filter = ref("");
</script>

<template>
  <Filter v-model="filter" />
  <Results :filter="filter" />
</template>
```

## 96: How do you type component props?

**Angular**

```ts
export class Avatar {
  src = input.required<string>();
  size = input<number>(32);
  shape = input<"circle" | "square">("circle");
}
```

**React**

```tsx
interface AvatarProps {
  src: string;
  size?: number;
  shape?: "circle" | "square";
}

export function Avatar({ src, size = 32, shape = "circle" }: AvatarProps) {
  return <img src={src} width={size} className={shape} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const {
  src,
  size = 32,
  shape = "circle",
} = defineProps<{
  src: string;
  size?: number;
  shape?: "circle" | "square";
}>();
</script>
```

## 97: How do you type component events?

**Angular**

```ts
selected = output<{ id: number; label: string }>();
```

**React**

```tsx
type Props = { onSelected: (item: { id: number; label: string }) => void };
```

**Vue.js**

```ts
const emit = defineEmits<{
  selected: [item: { id: number; label: string }];
}>();
```

## 98: How do you write a generic component?

**Angular**

```ts
@Component({
  selector: "app-select",
  template: `@for (o of options(); track $index) {
    <button (click)="picked.emit(o)">{{ label()(o) }}</button>
  }`,
})
export class Select<T> {
  options = input.required<T[]>();
  label = input.required<(o: T) => string>();
  picked = output<T>();
}
```

**React**

```tsx
type Props<T> = {
  options: T[];
  label: (o: T) => string;
  onPicked: (o: T) => void;
};

export function Select<T>({ options, label, onPicked }: Props<T>) {
  return options.map((o, i) => (
    <button key={i} onClick={() => onPicked(o)}>
      {label(o)}
    </button>
  ));
}
```

**Vue.js**

```vue
<script setup lang="ts" generic="T">
defineProps<{ options: T[]; label: (o: T) => string }>();
const emit = defineEmits<{ picked: [o: T] }>();
</script>

<template>
  <button v-for="(o, i) in options" :key="i" @click="emit('picked', o)">
    {{ label(o) }}
  </button>
</template>
```

## 99: How do dev and build commands compare?

| Task          | Angular       | React (Vite)    | Next.js         | Vue.js (Vite)   |
| ------------- | ------------- | --------------- | --------------- | --------------- |
| Dev server    | `ng serve`    | `npm run dev`   | `next dev`      | `npm run dev`   |
| Prod build    | `ng build`    | `npm run build` | `next build`    | `npm run build` |
| Run prod      | static files  | static files    | `next start`    | static files    |
| Unit tests    | `ng test`     | `vitest`        | `vitest`/`jest` | `vitest`        |
| Generate code | `ng generate` | none            | none            | none            |

Angular's CLI generates files and runs migrations (`ng update`). React and Vue rely on templates and editor snippets instead.

## 100: What test tools replace the Angular ones?

- **Angular:** Vitest (default in new projects since v21) or Jasmine/Karma in older ones, with `TestBed`.
- **React:** Vitest or Jest with React Testing Library.
- **Next.js:** Vitest or Jest with React Testing Library for components. Async Server Components are best tested with end-to-end tests.
- **Vue.js:** Vitest with Vue Test Utils or Vue Testing Library.

End-to-end tools (Playwright, Cypress) do not care about the framework, so those tests can stay as they are during a migration and prove the new app behaves the same.

## 101: How do you write the same simple component test?

**Angular**

```ts
it("increments", async () => {
  const fixture = TestBed.createComponent(Counter);
  await fixture.whenStable();
  fixture.nativeElement.querySelector("button").click();
  await fixture.whenStable();
  expect(fixture.nativeElement.textContent).toContain("1");
});
```

**React**

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

it("increments", async () => {
  render(<Counter />);
  await userEvent.click(screen.getByRole("button"));
  expect(screen.getByText(/1/)).toBeInTheDocument();
});
```

**Vue.js**

```ts
import { mount } from "@vue/test-utils";

it("increments", async () => {
  const wrapper = mount(Counter);
  await wrapper.get("button").trigger("click");
  expect(wrapper.text()).toContain("1");
});
```

## 102: How do you set up linting?

- **Angular:** `ng add @angular-eslint/schematics`, which adds template lint rules too.
- **React:** ESLint with `eslint-plugin-react-hooks` (catches wrong dependency arrays and hook rules) and `eslint-plugin-react`.
- **Next.js:** ESLint with `eslint-config-next` (or Biome). Next.js 16 removed the `next lint` command, so you run `eslint` directly.
- **Vue.js:** ESLint with `eslint-plugin-vue`. The `create-vue` scaffold sets it up.

The React hooks plugin is the most important one to add after a migration, because missing effect dependencies are the most common bug for developers coming from Angular.

## 103: What browser DevTools replace Angular DevTools?

- **Angular:** Angular DevTools extension (component tree, signals graph, profiler).
- **React and Next.js:** React Developer Tools (Components and Profiler tabs). Next.js also shows an in-browser dev overlay with errors and route info.
- **Vue.js:** Vue DevTools extension or the Vite plugin `vite-plugin-vue-devtools` (components, Pinia, router, timeline).

## 104: How do you serve static assets like images?

**Angular**

```html
<!-- files in public/ are served from "/" -->
<img ngSrc="/logo.png" width="120" height="40" />
```

**React**

```tsx
<img src="/logo.png" width={120} height={40} />
// or import logo from "./logo.png"; <img src={logo} />
```

**Next.js**

```tsx
import Image from "next/image";
<Image src="/logo.png" alt="Logo" width={120} height={40} />;
```

**Vue.js**

```vue
<img src="/logo.png" width="120" height="40" />
<!-- or a relative path, which Vite processes: <img src="./assets/logo.png" /> -->
```

Angular's `NgOptimizedImage` (`ngSrc`) maps best to Next.js's `<Image>`. Both enforce sizes, lazy loading and priority hints.

## 105: How do you set the page title?

**Angular**

```ts
// in routes
{ path: "about", component: About, title: "About us" }
// or from code: inject(Title).setTitle("About us");
```

**React**

```tsx
// React 19 hoists <title> into <head>
function About() {
  return (
    <>
      <title>About us</title>
      <h1>About</h1>
    </>
  );
}
```

**Next.js**

```tsx
// app/about/page.tsx
export const metadata = { title: "About us" };
```

**Vue.js**

```ts
// in route meta, applied in a guard
router.afterEach((to) => {
  document.title = (to.meta.title as string) ?? "My App";
});
// or useHead({ title: "About us" }) from @unhead/vue
```

## 106: How do you set meta tags?

**Angular**

```ts
inject(Meta).updateTag({ name: "description", content: "Our story" });
```

**React**

```tsx
<meta name="description" content="Our story" />
// React 19 hoists it into <head>
```

**Next.js**

```tsx
export const metadata = {
  description: "Our story",
  openGraph: { title: "About us", images: ["/og.png"] },
};
```

**Vue.js**

```ts
import { useHead } from "@unhead/vue";
useHead({ meta: [{ name: "description", content: "Our story" }] });
```

## 107: How do you load web fonts?

**Angular**

```css
/* styles.css */
@import url("https://fonts.googleapis.com/css2?family=Inter&display=swap");
body {
  font-family: "Inter", sans-serif;
}
```

**React**

```tsx
// npm i @fontsource/inter
import "@fontsource/inter";
```

**Next.js**

```tsx
import { Inter } from "next/font/google";
const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

**Vue.js**

```ts
// main.ts
import "@fontsource/inter";
```

`next/font` downloads and self-hosts fonts at build time, so there is no request to Google at runtime and less layout shift.

## 108: How do you translate a timer with setInterval?

**Angular**

```ts
export class Clock {
  now = signal(new Date());
  constructor() {
    const id = setInterval(() => this.now.set(new Date()), 1000);
    inject(DestroyRef).onDestroy(() => clearInterval(id));
  }
}
```

**React**

```tsx
function Clock() {
  const [now, setNow] = useState(new Date());
  useEffect(() => {
    const id = setInterval(() => setNow(new Date()), 1000);
    return () => clearInterval(id);
  }, []);
  return <time>{now.toLocaleTimeString()}</time>;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const now = ref(new Date());
const id = setInterval(() => (now.value = new Date()), 1000);
onUnmounted(() => clearInterval(id));
</script>

<template>
  <time>{{ now.toLocaleTimeString() }}</time>
</template>
```

## 109: How do you listen to window resize?

**Angular**

```ts
@Component({
  host: { "(window:resize)": "onResize()" },
  template: `{{ width() }}px`,
})
export class Width {
  width = signal(window.innerWidth);
  onResize() {
    this.width.set(window.innerWidth);
  }
}
```

**React**

```tsx
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);
  return width;
}
```

**Vue.js**

```ts
// VueUse: const { width } = useWindowSize();
const width = ref(window.innerWidth);
const onResize = () => (width.value = window.innerWidth);
onMounted(() => window.addEventListener("resize", onResize));
onUnmounted(() => window.removeEventListener("resize", onResize));
```

Angular removes `host` listeners for you. In React and Vue, you remove them in cleanup. In Next.js, read `window` only inside `useEffect`, because the first render also runs on the server.

## 110: How do you debounce a search input?

**Angular**

```ts
export class Search {
  query = signal("");
  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      switchMap((q) => this.api.search(q)),
    ),
    { initialValue: [] },
  );
}
```

**React**

```tsx
function useDebounced<T>(value: T, ms = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), ms);
    return () => clearTimeout(id);
  }, [value, ms]);
  return debounced;
}

const [query, setQuery] = useState("");
const debouncedQuery = useDebounced(query);
const { data } = useQuery({
  queryKey: ["search", debouncedQuery],
  queryFn: () => search(debouncedQuery),
});
```

**Vue.js**

```ts
import { refDebounced } from "@vueuse/core";

const query = ref("");
const debouncedQuery = refDebounced(query, 300);
watch(debouncedQuery, async (q) => (results.value = await search(q)));
```

## 111: How do you save state to localStorage?

**Angular**

```ts
export class Settings {
  theme = signal(localStorage.getItem("theme") ?? "light");
  constructor() {
    effect(() => localStorage.setItem("theme", this.theme()));
  }
}
```

**React**

```tsx
const [theme, setTheme] = useState(
  () => localStorage.getItem("theme") ?? "light",
);
useEffect(() => localStorage.setItem("theme", theme), [theme]);
```

**Vue.js**

```ts
import { useLocalStorage } from "@vueuse/core";
const theme = useLocalStorage("theme", "light");
```

Pass a function to `useState` so React reads `localStorage` only once, on the first render. In Next.js, `localStorage` does not exist on the server, so read it in an effect or in a client-only component.

## 112: How do you fetch data again when a route parameter changes?

**Angular**

```ts
export class Product {
  id = input.required<string>(); // with withComponentInputBinding()
  product = httpResource<Product>(() => `/api/products/${this.id()}`);
}
```

**React**

```tsx
function ProductPage() {
  const { id } = useParams();
  const { data } = useQuery({
    queryKey: ["product", id],
    queryFn: () => getProduct(id!),
  });
}
```

**Next.js**

```tsx
// a new id renders the page again on the server
export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const product = await getProduct((await params).id);
}
```

**Vue.js**

```ts
const route = useRoute();
const product = ref<Product>();
watch(
  () => route.params.id,
  async (id) => (product.value = await getProduct(id as string)),
  { immediate: true },
);
```

A common bug in Vue and React Router apps: the same component instance is reused when only the param changes, so code that runs "once on mount" does not run again. Watch the param, or key the data on it.

## 113: How do you translate a counter component end to end?

**Angular**

```ts
@Component({
  selector: "app-counter",
  template: `
    <button (click)="count.update((n) => n - 1)">-</button>
    <span>{{ count() }} (double: {{ double() }})</span>
    <button (click)="count.update((n) => n + 1)">+</button>
  `,
})
export class Counter {
  count = signal(0);
  double = computed(() => this.count() * 2);
}
```

**React**

```tsx
export function Counter() {
  const [count, setCount] = useState(0);
  const double = count * 2;
  return (
    <>
      <button onClick={() => setCount((n) => n - 1)}>-</button>
      <span>
        {count} (double: {double})
      </span>
      <button onClick={() => setCount((n) => n + 1)}>+</button>
    </>
  );
}
```

**Next.js**

```tsx
"use client"; // needed because the component has state and click handlers
// ...same code as React
```

**Vue.js**

```vue
<script setup lang="ts">
import { computed, ref } from "vue";
const count = ref(0);
const double = computed(() => count.value * 2);
</script>

<template>
  <button @click="count--">-</button>
  <span>{{ count }} (double: {{ double }})</span>
  <button @click="count++">+</button>
</template>
```

## 114: How do you translate a todo list end to end?

**Angular**

```ts
@Component({
  selector: "app-todos",
  imports: [FormsModule],
  template: `
    <input [(ngModel)]="text" (keyup.enter)="add()" />
    <ul>
      @for (t of todos(); track t.id) {
        <li [class.done]="t.done" (click)="toggle(t.id)">{{ t.title }}</li>
      }
    </ul>
  `,
})
export class Todos {
  text = "";
  todos = signal<{ id: number; title: string; done: boolean }[]>([]);
  add() {
    this.todos.update((l) => [
      ...l,
      { id: Date.now(), title: this.text, done: false },
    ]);
    this.text = "";
  }
  toggle(id: number) {
    this.todos.update((l) =>
      l.map((t) => (t.id === id ? { ...t, done: !t.done } : t)),
    );
  }
}
```

**React**

```tsx
export function Todos() {
  const [text, setText] = useState("");
  const [todos, setTodos] = useState<
    { id: number; title: string; done: boolean }[]
  >([]);

  const add = () => {
    setTodos((l) => [...l, { id: Date.now(), title: text, done: false }]);
    setText("");
  };
  const toggle = (id: number) =>
    setTodos((l) => l.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));

  return (
    <>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyUp={(e) => e.key === "Enter" && add()}
      />
      <ul>
        {todos.map((t) => (
          <li
            key={t.id}
            className={t.done ? "done" : ""}
            onClick={() => toggle(t.id)}
          >
            {t.title}
          </li>
        ))}
      </ul>
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { ref } from "vue";
const text = ref("");
const todos = ref<{ id: number; title: string; done: boolean }[]>([]);
function add() {
  todos.value.push({ id: Date.now(), title: text.value, done: false });
  text.value = "";
}
</script>

<template>
  <input v-model="text" @keyup.enter="add" />
  <ul>
    <li
      v-for="t in todos"
      :key="t.id"
      :class="{ done: t.done }"
      @click="t.done = !t.done"
    >
      {{ t.title }}
    </li>
  </ul>
</template>
```

## 115: How do you translate a toggle (show more / show less)?

**Angular**

```ts
@Component({
  selector: "app-more",
  template: `
    <button (click)="open.set(!open())">
      {{ open() ? "Show less" : "Show more" }}
    </button>
    @if (open()) {
      <ng-content />
    }
  `,
})
export class More {
  open = signal(false);
}
```

**React**

```tsx
export function More({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button onClick={() => setOpen((o) => !o)}>
        {open ? "Show less" : "Show more"}
      </button>
      {open && children}
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const open = ref(false);
</script>

<template>
  <button @click="open = !open">{{ open ? "Show less" : "Show more" }}</button>
  <slot v-if="open" />
</template>
```

One difference: Angular's `<ng-content>` content is always created by the parent, even when `@if` hides it. React `children` and Vue slots are only rendered when shown.

## 116: How do you translate a simple modal dialog?

**Angular**

```ts
@Component({
  selector: "app-modal",
  template: `
    @if (open()) {
      <div class="backdrop" (click)="open.set(false)">
        <div
          class="modal"
          role="dialog"
          aria-modal="true"
          (click)="$event.stopPropagation()"
        >
          <ng-content />
          <button (click)="open.set(false)">Close</button>
        </div>
      </div>
    }
  `,
})
export class Modal {
  open = model(false);
}
```

**React**

```tsx
import { createPortal } from "react-dom";

export function Modal({
  open,
  onClose,
  children,
}: {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
}) {
  if (!open) return null;
  return createPortal(
    <div className="backdrop" onClick={onClose}>
      <div
        className="modal"
        role="dialog"
        aria-modal="true"
        onClick={(e) => e.stopPropagation()}
      >
        {children}
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.body,
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const open = defineModel<boolean>({ default: false });
</script>

<template>
  <Teleport to="body">
    <div v-if="open" class="backdrop" @click="open = false">
      <div class="modal" role="dialog" aria-modal="true" @click.stop>
        <slot />
        <button @click="open = false">Close</button>
      </div>
    </div>
  </Teleport>
</template>
```

The native `<dialog>` element with `showModal()` is another option in all four, and it handles focus and the Escape key for you.

## 117: How do you translate a tabs component?

**Angular**

```ts
@Component({
  selector: "app-tabs",
  template: `
    @for (t of tabs(); track t) {
      <button [class.active]="t === active()" (click)="active.set(t)">
        {{ t }}
      </button>
    }
    <section>Content of {{ active() }}</section>
  `,
})
export class Tabs {
  tabs = input.required<string[]>();
  active = model<string>("");
}
```

**React**

```tsx
export function Tabs({ tabs }: { tabs: string[] }) {
  const [active, setActive] = useState(tabs[0]);
  return (
    <>
      {tabs.map((t) => (
        <button
          key={t}
          className={t === active ? "active" : ""}
          onClick={() => setActive(t)}
        >
          {t}
        </button>
      ))}
      <section>Content of {active}</section>
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ tabs: string[] }>();
const active = ref(props.tabs[0]);
</script>

<template>
  <button
    v-for="t in tabs"
    :key="t"
    :class="{ active: t === active }"
    @click="active = t"
  >
    {{ t }}
  </button>
  <section>Content of {{ active }}</section>
</template>
```

## 118: How do you translate client-side pagination?

**Angular**

```ts
export class Paged {
  items = input.required<string[]>();
  page = signal(1);
  pageSize = 10;
  pageItems = computed(() =>
    this.items().slice(
      (this.page() - 1) * this.pageSize,
      this.page() * this.pageSize,
    ),
  );
  pages = computed(() => Math.ceil(this.items().length / this.pageSize));
}
```

**React**

```tsx
function Paged({ items }: { items: string[] }) {
  const [page, setPage] = useState(1);
  const pageSize = 10;
  const pageItems = items.slice((page - 1) * pageSize, page * pageSize);
  const pages = Math.ceil(items.length / pageSize);
  // render pageItems and buttons that call setPage
}
```

**Vue.js**

```ts
const props = defineProps<{ items: string[] }>();
const page = ref(1);
const pageSize = 10;
const pageItems = computed(() =>
  props.items.slice((page.value - 1) * pageSize, page.value * pageSize),
);
const pages = computed(() => Math.ceil(props.items.length / pageSize));
```

## 119: How do you translate a list with a search filter?

**Angular**

```ts
@Component({
  selector: "app-people",
  template: `
    <input
      [value]="q()"
      (input)="q.set($any($event.target).value)"
      placeholder="Search"
    />
    @for (p of filtered(); track p) {
      <p>{{ p }}</p>
    }
  `,
})
export class People {
  people = input.required<string[]>();
  q = signal("");
  filtered = computed(() =>
    this.people().filter((p) =>
      p.toLowerCase().includes(this.q().toLowerCase()),
    ),
  );
}
```

**React**

```tsx
function People({ people }: { people: string[] }) {
  const [q, setQ] = useState("");
  const filtered = people.filter((p) =>
    p.toLowerCase().includes(q.toLowerCase()),
  );
  return (
    <>
      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        placeholder="Search"
      />
      {filtered.map((p) => (
        <p key={p}>{p}</p>
      ))}
    </>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ people: string[] }>();
const q = ref("");
const filtered = computed(() =>
  props.people.filter((p) => p.toLowerCase().includes(q.value.toLowerCase())),
);
</script>

<template>
  <input v-model="q" placeholder="Search" />
  <p v-for="p in filtered" :key="p">{{ p }}</p>
</template>
```

## 120: How do you translate an accordion?

**Angular**

```ts
@Component({
  selector: "app-faq",
  template: `
    @for (item of items(); track item.q; let i = $index) {
      <button
        (click)="openIndex.set(openIndex() === i ? -1 : i)"
        [attr.aria-expanded]="openIndex() === i"
      >
        {{ item.q }}
      </button>
      @if (openIndex() === i) {
        <p>{{ item.a }}</p>
      }
    }
  `,
})
export class Faq {
  items = input.required<{ q: string; a: string }[]>();
  openIndex = signal(-1);
}
```

**React**

```tsx
function Faq({ items }: { items: { q: string; a: string }[] }) {
  const [openIndex, setOpenIndex] = useState(-1);
  return items.map((item, i) => (
    <Fragment key={item.q}>
      <button
        aria-expanded={openIndex === i}
        onClick={() => setOpenIndex(openIndex === i ? -1 : i)}
      >
        {item.q}
      </button>
      {openIndex === i && <p>{item.a}</p>}
    </Fragment>
  ));
}
```

**Vue.js**

```vue
<script setup lang="ts">
defineProps<{ items: { q: string; a: string }[] }>();
const openIndex = ref(-1);
</script>

<template>
  <template v-for="(item, i) in items" :key="item.q">
    <button
      :aria-expanded="openIndex === i"
      @click="openIndex = openIndex === i ? -1 : i"
    >
      {{ item.q }}
    </button>
    <p v-if="openIndex === i">{{ item.a }}</p>
  </template>
</template>
```

The native `<details>`/`<summary>` element is a no-JavaScript option in all of them.

## 121: How do you give projected content a fallback?

**Angular**

```html
<!-- Angular 18+: content inside ng-content is the fallback -->
<button><ng-content>Click me</ng-content></button>
```

**React**

```tsx
function Btn({ children = "Click me" }: { children?: React.ReactNode }) {
  return <button>{children}</button>;
}
```

**Vue.js**

```vue
<button><slot>Click me</slot></button>
```

## 122: How do you bind a textarea and a number input?

**Angular**

```html
<textarea [(ngModel)]="bio"></textarea>
<input type="number" [(ngModel)]="age" />
```

**React**

```tsx
<textarea value={bio} onChange={(e) => setBio(e.target.value)} />
<input type="number" value={age} onChange={(e) => setAge(e.target.valueAsNumber)} />
```

**Vue.js**

```vue
<textarea v-model="bio" />
<input v-model.number="age" type="number" />
```

In React, `<textarea>` uses a `value` prop, not child text. Vue's `.number` modifier and React's `valueAsNumber` both turn the text into a number. Vue also has `.trim` and `.lazy` (update on `change` instead of `input`).

## 123: How do you translate (ngModelChange)?

**Angular**

```html
<input [ngModel]="name()" (ngModelChange)="onNameChange($event)" />
```

**React**

```tsx
<input value={name} onChange={(e) => onNameChange(e.target.value)} />
```

**Vue.js**

```vue
<input
  :value="name"
  @input="onNameChange(($event.target as HTMLInputElement).value)"
/>
<!-- or v-model="name" plus watch(name, onNameChange) -->
```

React's controlled inputs already split "value in" and "change out", which is exactly what `[ngModel]` plus `(ngModelChange)` does.

## 124: How do you handle a file input?

**Angular**

```html
<input type="file" (change)="onFile($event)" />
```

```ts
onFile(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0];
  if (file) this.upload(file);
}
```

**React**

```tsx
<input
  type="file"
  onChange={(e) => e.target.files?.[0] && upload(e.target.files[0])}
/>
```

**Vue.js**

```vue
<input type="file" @change="onFile" />
```

File inputs are uncontrolled in all three frameworks. You read the file in the change handler, you cannot set the value from code.

## 125: How do you connect a label to an input?

**Angular**

```html
<label for="email">Email</label> <input id="email" />
```

**React**

```tsx
const id = useId();
<label htmlFor={id}>Email</label>
<input id={id} />
```

**Vue.js**

```vue
<script setup lang="ts">
import { useId } from "vue";
const id = useId();
</script>

<template>
  <label :for="id">Email</label>
  <input :id="id" />
</template>
```

React uses `htmlFor` because `for` is a JavaScript keyword. `useId` (React 18+, Vue 3.5+) makes IDs that are unique and stable between server and client rendering.

## 126: How do you render inline SVG icons?

**Angular**

```ts
@Component({
  selector: "app-icon-check",
  template: `<svg
    viewBox="0 0 24 24"
    [attr.width]="size()"
    [attr.height]="size()"
  >
    <path d="M5 12l5 5L20 7" />
  </svg>`,
})
export class IconCheck {
  size = input(24);
}
```

**React**

```tsx
export const IconCheck = ({ size = 24 }: { size?: number }) => (
  <svg viewBox="0 0 24 24" width={size} height={size} strokeWidth={2}>
    <path d="M5 12l5 5L20 7" />
  </svg>
);
```

**Vue.js**

```vue
<script setup lang="ts">
const { size = 24 } = defineProps<{ size?: number }>();
</script>

<template>
  <svg viewBox="0 0 24 24" :width="size" :height="size" stroke-width="2">
    <path d="M5 12l5 5L20 7" />
  </svg>
</template>
```

In JSX, SVG attributes with dashes become camelCase (`strokeWidth`). Icon libraries exist for all of them (for example, Lucide has `lucide-angular`, `lucide-react` and `lucide-vue-next`).

## 127: How do you add simple enter and leave animations?

**Angular**

```html
<!-- Angular 20.2+ -->
@if (visible()) {
<div animate.enter="fade-in" animate.leave="fade-out">Saved!</div>
}
```

**React**

```tsx
// React has no built-in leave animation. Use CSS for enter, a library for leave.
import { AnimatePresence, motion } from "motion/react";

<AnimatePresence>
  {visible && (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      Saved!
    </motion.div>
  )}
</AnimatePresence>;
```

**Vue.js**

```vue
<Transition name="fade">
  <div v-if="visible">Saved!</div>
</Transition>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

Vue's `<Transition>` is the closest match to Angular's `animate.enter`/`animate.leave`. Both wait for the CSS animation before removing the element.

## 128: How do you translate a global error handler?

**Angular**

```ts
export class MyErrorHandler implements ErrorHandler {
  handleError(error: unknown) {
    reportToServer(error);
  }
}
// providers: [{ provide: ErrorHandler, useClass: MyErrorHandler }]
```

**React**

```tsx
createRoot(document.getElementById("root")!, {
  onUncaughtError: (error) => reportToServer(error),
  onCaughtError: (error) => reportToServer(error),
}).render(<App />);
```

**Next.js**

```tsx
// app/global-error.tsx catches errors in the root layout
"use client";
export default function GlobalError({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <html>
      <body>
        <h2>Something went wrong</h2>
        <button onClick={reset}>Try again</button>
      </body>
    </html>
  );
}
```

**Vue.js**

```ts
const app = createApp(App);
app.config.errorHandler = (err) => reportToServer(err);
```

## 129: How do you translate an InjectionToken for config values?

**Angular**

```ts
export const API_URL = new InjectionToken<string>("API_URL");
// providers: [{ provide: API_URL, useValue: "https://api.example.com" }]
export class Api {
  private url = inject(API_URL);
}
```

**React**

```tsx
// For static config, a module is enough
export const config = { apiUrl: import.meta.env.VITE_API_URL };

// For config that differs per subtree or in tests, use context
const ConfigContext = createContext({ apiUrl: "" });
```

**Vue.js**

```ts
import type { InjectionKey } from "vue";
export const ApiUrlKey: InjectionKey<string> = Symbol("ApiUrl");
// main.ts: app.provide(ApiUrlKey, "https://api.example.com");
const url = inject(ApiUrlKey);
```

Vue's typed `InjectionKey` is the closest match to `InjectionToken`.

## 130: Where do app-wide providers go?

**Angular**

```ts
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withInterceptors([authInterceptor])),
  ],
};
```

**React**

```tsx
// main.tsx: wrap the app in providers
const queryClient = new QueryClient();
createRoot(document.getElementById("root")!).render(
  <QueryClientProvider client={queryClient}>
    <RouterProvider router={router} />
  </QueryClientProvider>,
);
```

**Next.js**

```tsx
// app/providers.tsx
"use client";
export function Providers({ children }: { children: React.ReactNode }) {
  const [client] = useState(() => new QueryClient());
  return <QueryClientProvider client={client}>{children}</QueryClientProvider>;
}
// app/layout.tsx: <body><Providers>{children}</Providers></body>
```

**Vue.js**

```ts
// main.ts: plugins
createApp(App).use(createPinia()).use(router).use(VueQueryPlugin).mount("#app");
```

## 131: Which UI component libraries replace Angular Material?

- **Angular:** Angular Material and CDK, PrimeNG, Spartan (shadcn style).
- **React and Next.js:** MUI (Material design), shadcn/ui (copy-in components on Radix or Base UI), Mantine, Chakra UI, React Aria.
- **Vue.js:** Vuetify (Material design), PrimeVue, shadcn-vue (on Reka UI), Quasar, Naive UI.

If the Angular app uses PrimeNG, PrimeReact and PrimeVue keep the same look with similar component names. If it uses Material, MUI or Vuetify keep the same design language.

## 132: Which state management libraries replace NgRx?

- **Angular:** NgRx Store, NgRx SignalStore, or plain signal services.
- **React and Next.js:** Redux Toolkit (closest to NgRx Store), Zustand (closest to a small signal service), Jotai, plus TanStack Query for server data.
- **Vue.js:** Pinia (the official store), plus TanStack Vue Query for server data.

Before picking one, separate server state (data from APIs) from client state (UI state). Often most of an NgRx store is cached API data, and a query library replaces it with far less code.

## 133: How do Angular lifecycle hooks map to React and Vue?

| Angular                      | React                           | Vue.js                       |
| ---------------------------- | ------------------------------- | ---------------------------- |
| `constructor` / field init   | function body (every render)    | `<script setup>` body (once) |
| `ngOnInit`                   | `useEffect(fn, [])`             | `onMounted` or setup body    |
| `ngOnChanges`                | `useEffect(fn, [prop])`         | `watch(() => props.x)`       |
| `ngDoCheck`                  | none (render runs every time)   | `onBeforeUpdate`             |
| `ngAfterViewInit`            | `useEffect` / `useLayoutEffect` | `onMounted`                  |
| `ngAfterViewChecked`         | `useEffect` with no deps array  | `onUpdated`                  |
| `afterNextRender`            | `useEffect(fn, [])`             | `onMounted` / `nextTick`     |
| `ngOnDestroy` / `DestroyRef` | `useEffect` cleanup             | `onUnmounted`                |

The biggest mental shift: a React function component runs again on every render, so it is not a constructor. Vue's `<script setup>` runs once, like an Angular constructor.

## 134: What is a quick cheat sheet of template syntax?

| Angular                        | React (JSX)                   | Vue.js                       |
| ------------------------------ | ----------------------------- | ---------------------------- |
| `{{ x }}`                      | `{x}`                         | `{{ x }}`                    |
| `[prop]="x"`                   | `prop={x}`                    | `:prop="x"`                  |
| `(click)="f()"`                | `onClick={f}`                 | `@click="f"`                 |
| `[(ngModel)]="x"`              | `value` + `onChange`          | `v-model="x"`                |
| `@if (a) {} @else {}`          | `a ? ... : ...`               | `v-if` / `v-else`            |
| `@for (i of l; track i.id) {}` | `l.map(i => <X key={i.id}/>)` | `v-for="i in l" :key="i.id"` |
| `<ng-content />`               | `{children}`                  | `<slot />`                   |
| `#ref`                         | `ref={useRef()}`              | `ref="name"`                 |
| `[class.a]="x"`                | `className={x ? "a" : ""}`    | `:class="{ a: x }"`          |
| `[innerHTML]`                  | `dangerouslySetInnerHTML`     | `v-html`                     |

## 135: What is React Strict Mode and why does my effect run twice?

In development, `<StrictMode>` mounts each component, unmounts it, and mounts it again. So an effect runs, cleans up, and runs again. This finds effects with missing cleanup. It does not happen in production.

Angular has no similar feature, so developers coming from Angular often see two network requests and think something is broken. The fix is to write effects that clean up correctly (abort fetches, clear timers), or use a data library that dedupes requests. Next.js enables Strict Mode by default in the App Router. Vue has no double-mount behavior.

## 136: What does a production build produce in each?

- **Angular:** `ng build` writes static files (or browser plus server bundles with SSR) to `dist/<project>/`.
- **React (Vite):** `npm run build` writes static files to `dist/`.
- **Next.js:** `next build` writes to `.next/`. You run it with `next start`, or use `output: "standalone"` for a small Node.js server, or `output: "export"` for static files only.
- **Vue.js (Vite):** `npm run build` writes static files to `dist/`.

So an Angular SPA moves to React or Vue with the same hosting (any static host plus a fallback to `index.html`). Moving to Next.js usually means running a Node server or using a platform that supports Next.js.

## 137: How do you deploy a static single-page app?

The same way for Angular, React (Vite) and Vue (Vite): upload the build folder to a static host (S3 + CloudFront, Netlify, GitHub Pages, Nginx) and add a rewrite so unknown paths serve `index.html`. Without that rewrite, refreshing `/users/5` returns 404.

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

Next.js is different. With `output: "export"` it is also static, but features that need a server (Server Actions, `cookies()`, dynamic rendering, ISR) do not work in that mode.

## 138: Which ones render on the server by default?

- **Angular:** client-side by default. `ng new --ssr` or `ng add @angular/ssr` adds server rendering.
- **React (Vite):** client-side only. You need a framework (Next.js, React Router framework mode) for SSR.
- **Next.js:** server rendering by default. Every component in `app/` is a Server Component unless marked `"use client"`.
- **Vue.js (Vite):** client-side by default. Nuxt adds SSR.

## 139: What is hydration?

Hydration is when the browser takes HTML that was rendered on the server and attaches event listeners and state to it, instead of building the DOM again. Angular (`provideClientHydration()`), Next.js, and Nuxt all do it.

In all of them, the server HTML and the first client render must match. Reading `window`, `Date.now()` or `Math.random()` during render causes "hydration mismatch" warnings in every framework.

## 140: What is the difference between Server and Client Components in Next.js?

Server Components (the default) run only on the server. They can be `async`, read the database, and use secrets. Their JavaScript is not sent to the browser. They cannot use state, effects or event handlers.

Client Components start with `"use client"`. They render on the server for the first HTML and then hydrate in the browser, so they can use hooks and events. Every Angular component you translate that has signals, event bindings or lifecycle hooks becomes a Client Component in Next.js. Static parts and data loading can stay in Server Components.

```tsx
// app/products/page.tsx (Server Component)
import { AddToCart } from "./AddToCart"; // has "use client"

export default async function Products() {
  const products = await db.product.findMany();
  return products.map((p) => (
    <div key={p.id}>
      {p.name} <AddToCart id={p.id} />
    </div>
  ));
}
```

## 141: When is Next.js the wrong target for an Angular app?

When the Angular app is a pure client-side SPA behind a login (an admin panel, an internal tool) with no SEO needs, and it talks to an existing backend. Server rendering, Server Components and Server Actions add little there, but you still pay for a Node server and a more complex mental model. A Vite + React app (or Vite + Vue) is a closer and simpler match.

Next.js is a good target when the app has public pages that need SEO, fast first load, or when you want to move some backend logic (API routes, server data access) into the same project.

## 142: What is a common mistake with state when coming from Angular?

Mutating state directly. In Angular with a plain class field, `this.user.name = "x"` updated the view (with Zone.js). With signals or React state, mutation does nothing visible.

**Angular**

```ts
this.user().name = "x"; // signal does not notice
this.user.update((u) => ({ ...u, name: "x" })); // correct
```

**React**

```tsx
user.name = "x"; // no re-render
setUser({ ...user, name: "x" }); // correct
```

**Vue.js**

```ts
user.value.name = "x"; // works, Vue tracks the property
```

## 143: Why does reading state right after setting it show the old value in React?

In React, `count` is a constant for the current render. Calling `setCount` schedules a new render. It does not change the variable you already have.

**Angular**

```ts
this.count.set(5);
console.log(this.count()); // 5, signals update right away
```

**React**

```tsx
setCount(5);
console.log(count); // still the old value
```

**Vue.js**

```ts
count.value = 5;
console.log(count.value); // 5, refs update right away (the DOM updates later)
```

If you need the new value, compute it first: `const next = 5; setCount(next); use(next);`.

## 144: How do you keep a component's state when hiding it?

**Angular**

```html
<!-- @if destroys state; [hidden] keeps it -->
<app-editor [hidden]="tab() !== 'editor'" />
```

**React**

```tsx
// React 19.2: <Activity> hides the UI but keeps its state
import { Activity } from "react";
<Activity mode={tab === "editor" ? "visible" : "hidden"}>
  <Editor />
</Activity>;
```

**Vue.js**

```vue
<KeepAlive>
  <component :is="currentTab" />
</KeepAlive>
<!-- or v-show="tab === 'editor'" -->
```

## 145: How do you reset a component's state when an input changes?

**Angular**

```ts
// linkedSignal resets when its source changes
export class Comment {
  postId = input.required<number>();
  draft = linkedSignal({ source: this.postId, computation: () => "" });
}
```

**React**

```tsx
// Give the component a key; a new key mounts a fresh instance
<CommentBox key={postId} postId={postId} />
```

**Vue.js**

```vue
<CommentBox :key="postId" :post-id="postId" />
```

The `key` trick works in both React and Vue. In React it is the officially recommended way to reset state.

## 146: What files do you create first when translating a small Angular component?

Take the `.ts`, `.html` and `.css` files of one Angular component:

1. Create one file: `UserCard.tsx` (React/Next.js) or `UserCard.vue` (Vue).
2. Turn `input()`s into typed props and `output()`s into `onX` callback props (React) or `defineEmits` (Vue).
3. Turn signals into `useState`/`ref`, `computed` into derived values/`computed`.
4. Rewrite the template: control flow, bindings and events.
5. Move styles into a CSS Module (React) or `<style scoped>` (Vue).
6. Replace injected services with hooks, composables, or imports.
7. Port the unit test and run it.

## 147: How do you translate this in class methods?

Angular components are classes, so code uses `this.x`. React function components and Vue `<script setup>` have no `this`. Variables and functions are in the closure.

**Angular**

```ts
export class Greeter {
  name = signal("Ana");
  greet() {
    alert(`Hi ${this.name()}`);
  }
}
```

**React**

```tsx
function Greeter() {
  const [name] = useState("Ana");
  const greet = () => alert(`Hi ${name}`);
  return <button onClick={greet}>Greet</button>;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const name = ref("Ana");
const greet = () => alert(`Hi ${name.value}`);
</script>
```

## 148: How do you translate a component that only displays data?

Pure display components translate almost one to one. In Next.js they can stay Server Components (no `"use client"`), so they add no JavaScript to the browser bundle.

**Angular**

```ts
@Component({
  selector: "app-price",
  template: `<span class="price">{{ amount() | currency: currency() }}</span>`,
  imports: [CurrencyPipe],
})
export class Price {
  amount = input.required<number>();
  currency = input("USD");
}
```

**React**

```tsx
export function Price({
  amount,
  currency = "USD",
}: {
  amount: number;
  currency?: string;
}) {
  return (
    <span className="price">
      {new Intl.NumberFormat("en-US", { style: "currency", currency }).format(
        amount,
      )}
    </span>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const { amount, currency = "USD" } = defineProps<{
  amount: number;
  currency?: string;
}>();
</script>

<template>
  <span class="price">{{
    new Intl.NumberFormat("en-US", { style: "currency", currency }).format(
      amount,
    )
  }}</span>
</template>
```

## 149: How does conditional rendering of a whole component translate?

**Angular**

```ts
@Component({
  selector: "app-banner",
  template: `@if (message()) {
    <div class="banner">{{ message() }}</div>
  }`,
})
export class Banner {
  message = input<string>();
}
```

**React**

```tsx
function Banner({ message }: { message?: string }) {
  if (!message) return null; // render nothing
  return <div className="banner">{message}</div>;
}
```

**Vue.js**

```vue
<template>
  <div v-if="message" class="banner">{{ message }}</div>
</template>
```

Returning `null` is the React way for a component to render nothing.

## 150: What are the main things to remember when starting an Angular to React, Next.js or Vue translation?

- Templates become JSX (React, Next.js) or a very similar template syntax (Vue).
- Signals become `useState`/`ref`, `computed` stays `computed` in Vue and becomes plain derived values in React.
- Services become hooks, composables, stores or plain modules.
- DI becomes context (React) or `provide`/`inject` (Vue), or imports.
- Pipes become functions. Directives become components, hooks or Vue directives.
- The router becomes React Router, the `app/` folder in Next.js, or Vue Router.
- RxJS is optional in the target. Most HTTP code becomes `fetch` plus a query library.
- In Next.js, decide early what runs on the server and what runs in the browser.

# Moderate Questions (151-300)

## 151: Should you rewrite an Angular app at once or migrate it step by step?

For anything bigger than a few screens, migrate step by step. A big-bang rewrite freezes features for months, and you only find gaps in behavior at the end.

Common step-by-step approaches:

- **Route by route:** a reverse proxy sends some URLs to the new app and the rest to the old Angular app. Next.js `rewrites` can act as that proxy.
- **Widget by widget:** wrap new React or Vue components as Web Components and drop them into Angular screens, or the other way around with Angular Elements.
- **Microfrontends:** Module Federation lets the Angular shell load remote React or Vue apps.

A full rewrite only makes sense for small apps, or when the old code is so poor that porting is slower than writing fresh.

## 152: How do you embed a React component inside an Angular app during migration?

**Angular**

```ts
@Component({
  selector: "app-react-host",
  template: `<div #host></div>`,
})
export class ReactHost {
  host = viewChild.required<ElementRef<HTMLDivElement>>("host");
  userId = input.required<string>();
  private root?: Root;

  constructor() {
    afterNextRender(() => (this.root = createRoot(this.host().nativeElement)));
    effect(() =>
      this.root?.render(createElement(UserProfile, { userId: this.userId() })),
    );
    inject(DestroyRef).onDestroy(() => this.root?.unmount());
  }
}
```

**React**

```tsx
// The React component is a normal component, it does not know about Angular
export function UserProfile({ userId }: { userId: string }) {
  return <h2>User {userId}</h2>;
}
```

**Vue.js**

```ts
// Same idea for Vue inside Angular
const app = createApp(UserProfile, { userId: "42" });
app.mount(hostElement);
// on destroy: app.unmount();
```

Each framework mounts into a plain DOM element, so the Angular wrapper only needs to create, update and destroy the root.

## 153: How do Angular Elements help a migration?

`@angular/elements` turns an Angular component into a standard Custom Element (Web Component). A new React, Next.js or Vue app can then use the old Angular component while it is still being rewritten.

**Angular**

```ts
// main.ts of an "elements" build
const app = await createApplication({ providers: [provideHttpClient()] });
const el = createCustomElement(LegacyChart, { injector: app.injector });
customElements.define("legacy-chart", el);
```

**React**

```tsx
// React 19 sets properties on custom elements and supports custom events
<legacy-chart
  data={points}
  onpointclick={(e: CustomEvent) => select(e.detail)}
/>
```

**Next.js**

```tsx
"use client"; // custom elements need the browser
// load the script with next/script, then use <legacy-chart> in a client component
```

**Vue.js**

```vue
<legacy-chart :data.prop="points" @pointclick="select($event.detail)" />
<!-- tell Vue it is a custom element: compilerOptions.isCustomElement = (tag) => tag.startsWith("legacy-") -->
```

The cost is that each Angular element bundles part of the Angular runtime, so use it as a temporary bridge.

## 154: How do you translate a data-access service into hooks or composables?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class ProductService {
  private http = inject(HttpClient);
  list(category: string) {
    return this.http.get<Product[]>("/api/products", { params: { category } });
  }
}
```

**React**

```tsx
// api/products.ts: plain functions, no framework
export const listProducts = (category: string) =>
  fetch(`/api/products?category=${encodeURIComponent(category)}`).then(
    (r) => r.json() as Promise<Product[]>,
  );

// hooks/useProducts.ts
export const useProducts = (category: string) =>
  useQuery({
    queryKey: ["products", category],
    queryFn: () => listProducts(category),
  });
```

**Next.js**

```ts
// lib/products.ts: called directly from Server Components
import "server-only";
export async function listProducts(category: string) {
  return db.product.findMany({ where: { category } });
}
```

**Vue.js**

```ts
// composables/useProducts.ts
export const useProducts = (category: MaybeRefOrGetter<string>) =>
  useQuery({
    queryKey: ["products", category],
    queryFn: () => listProducts(toValue(category)),
  });
```

Split the service in two: a framework-free API module and a thin hook or composable on top. The API module is easy to test and share.

## 155: How do you use RxJS observables in React?

You can keep RxJS during a migration and subscribe in a hook. `useSyncExternalStore` is the correct way for a hot, shared stream with a current value.

**Angular**

```ts
user = toSignal(this.userService.user$, { initialValue: null });
```

**React**

```tsx
function useObservable<T>(source$: Observable<T>, initial: T): T {
  const [value, setValue] = useState(initial);
  useEffect(() => {
    const sub = source$.subscribe(setValue);
    return () => sub.unsubscribe();
  }, [source$]);
  return value;
}

// for a BehaviorSubject store:
function useBehaviorSubject<T>(subject: BehaviorSubject<T>) {
  return useSyncExternalStore(
    (onChange) => {
      const sub = subject.subscribe(onChange);
      return () => sub.unsubscribe();
    },
    () => subject.getValue(),
  );
}
```

**Vue.js**

```ts
import { useObservable, useSubscription } from "@vueuse/rxjs";
const user = useObservable(userService.user$);
```

Make sure the observable reference is stable in React (create it outside the component or with `useMemo`), or the effect will resubscribe on every render.

## 156: How do you translate a BehaviorSubject-based store?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class AuthStore {
  private user$$ = new BehaviorSubject<User | null>(null);
  readonly user$ = this.user$$.asObservable();
  login(user: User) {
    this.user$$.next(user);
  }
}
```

**React**

```tsx
import { create } from "zustand";

export const useAuthStore = create<{
  user: User | null;
  login: (u: User) => void;
}>((set) => ({
  user: null,
  login: (user) => set({ user }),
}));
// const user = useAuthStore((s) => s.user);
```

**Vue.js**

```ts
export const useAuthStore = defineStore("auth", () => {
  const user = ref<User | null>(null);
  const login = (u: User) => (user.value = u);
  return { user, login };
});
```

Modern Angular code would use a `signal` instead of a `BehaviorSubject`. Either way, the target is a small store with state plus methods.

## 157: How do you translate a switchMap typeahead?

**Angular**

```ts
export class Typeahead {
  private api = inject(SearchApi);
  query = signal("");
  results = toSignal(
    toObservable(this.query).pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap((q) => (q ? this.api.search(q) : of([]))),
    ),
    { initialValue: [] },
  );
}
```

**React**

```tsx
function Typeahead() {
  const [query, setQuery] = useState("");
  const debounced = useDebounced(query, 300);
  const { data = [] } = useQuery({
    queryKey: ["search", debounced],
    queryFn: ({ signal }) =>
      fetch(`/api/search?q=${debounced}`, { signal }).then((r) => r.json()),
    enabled: debounced.length > 0,
  });
  // render input + data
}
```

**Vue.js**

```ts
const query = ref("");
const debounced = refDebounced(query, 300);
const { data } = useQuery({
  queryKey: ["search", debounced],
  queryFn: ({ signal }) =>
    fetch(`/api/search?q=${debounced.value}`, { signal }).then((r) => r.json()),
  enabled: () => debounced.value.length > 0,
});
```

`switchMap` cancels the old request. TanStack Query does the same: when the key changes, it ignores the old result and aborts it if you pass `signal` to `fetch`.

## 158: How do you translate combineLatest?

**Angular**

```ts
vm$ = combineLatest([this.user$, this.settings$]).pipe(
  map(([user, settings]) => ({ name: user.name, theme: settings.theme })),
);
// modern: vm = computed(() => ({ name: this.user().name, theme: this.settings().theme }));
```

**React**

```tsx
const user = useUser();
const settings = useSettings();
const vm = { name: user.name, theme: settings.theme };
```

**Vue.js**

```ts
const vm = computed(() => ({
  name: user.value.name,
  theme: settings.value.theme,
}));
```

Most `combineLatest` + `map` pipelines were only deriving state. In React and Vue that is just a derived value.

## 159: How do you translate an HTTP interceptor?

**Angular**

```ts
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthStore).token();
  return next(
    token
      ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
      : req,
  );
};
// provideHttpClient(withInterceptors([authInterceptor]))
```

**React**

```ts
// api/client.ts: one fetch wrapper used by all API calls
export async function apiFetch<T>(
  url: string,
  init: RequestInit = {},
): Promise<T> {
  const token = useAuthStore.getState().token;
  const res = await fetch(url, {
    ...init,
    headers: {
      ...init.headers,
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
// or axios: axios.interceptors.request.use((config) => { ... })
```

**Next.js**

```ts
// Server side: read the token from cookies in the server helper
import { cookies } from "next/headers";
export async function apiFetch<T>(path: string): Promise<T> {
  const token = (await cookies()).get("token")?.value;
  const res = await fetch(`${process.env.API_URL}${path}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}
```

**Vue.js**

```ts
// with ofetch
import { ofetch } from "ofetch";
export const api = ofetch.create({
  onRequest({ options }) {
    const token = useAuthStore().token;
    if (token) options.headers.set("Authorization", `Bearer ${token}`);
  },
});
```

## 160: How do you translate an error interceptor that redirects on 401?

**Angular**

```ts
export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  const router = inject(Router);
  return next(req).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status === 401) router.navigate(["/login"]);
      return throwError(() => err);
    }),
  );
};
```

**React**

```ts
export async function apiFetch<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, init);
  if (res.status === 401) {
    window.location.assign("/login"); // or call router.navigate from your router instance
    throw new Error("Unauthorized");
  }
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
```

**Next.js**

```ts
// in a Server Component or Server Action
import { redirect } from "next/navigation";
if (res.status === 401) redirect("/login");
```

**Vue.js**

```ts
export const api = ofetch.create({
  onResponseError({ response }) {
    if (response.status === 401) router.push("/login");
  },
});
```

Outside components, React hooks like `useNavigate` cannot be called. Use the router instance (`router.navigate()` from `createBrowserRouter`) or a full page redirect.

## 161: How do you translate retry logic?

**Angular**

```ts
this.http.get("/api/data").pipe(retry({ count: 3, delay: 1000 }));
```

**React**

```tsx
useQuery({
  queryKey: ["data"],
  queryFn: getData,
  retry: 3,
  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30_000),
});
```

**Vue.js**

```ts
useQuery({ queryKey: ["data"], queryFn: getData, retry: 3 });
```

TanStack Query retries failed queries 3 times by default on the client, with exponential backoff.

## 162: How do you translate a canActivate route guard?

**Angular**

```ts
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthStore);
  return auth.isLoggedIn() ? true : inject(Router).createUrlTree(["/login"]);
};
// { path: "admin", component: Admin, canActivate: [authGuard] }
```

**React**

```tsx
// React Router data mode: a loader that redirects
import { redirect } from "react-router";

{
  path: "admin",
  loader: () => {
    if (!useAuthStore.getState().user) throw redirect("/login");
    return null;
  },
  Component: Admin,
}
// or a wrapper: function RequireAuth({ children }) { return user ? children : <Navigate to="/login" />; }
```

**Next.js**

```tsx
// app/admin/layout.tsx (server side check)
import { redirect } from "next/navigation";

export default async function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getSession();
  if (!session) redirect("/login");
  return children;
}
```

**Vue.js**

```ts
router.beforeEach((to) => {
  if (to.meta.requiresAuth && !useAuthStore().user) return "/login";
});
// { path: "/admin", component: Admin, meta: { requiresAuth: true } }
```

In Next.js you can also check a cookie in `proxy.ts` for a fast redirect, but always check again where the data is read, because the proxy alone is not enough to protect data.

## 163: How do you translate canDeactivate (unsaved changes warning)?

**Angular**

```ts
export const unsavedGuard: CanDeactivateFn<EditPage> = (component) =>
  component.dirty() ? confirm("Discard changes?") : true;
```

**React**

```tsx
import { useBlocker } from "react-router";

function EditPage() {
  const [dirty, setDirty] = useState(false);
  const blocker = useBlocker(dirty);
  useEffect(() => {
    if (blocker.state === "blocked") {
      confirm("Discard changes?") ? blocker.proceed() : blocker.reset();
    }
  }, [blocker]);
}
```

**Next.js**

```tsx
"use client";
// The App Router has no built-in navigation blocker. A common approach is
// a beforeunload listener for reloads/closing the tab, plus a confirm on your own links.
useEffect(() => {
  if (!dirty) return;
  const onBeforeUnload = (e: BeforeUnloadEvent) => e.preventDefault();
  window.addEventListener("beforeunload", onBeforeUnload);
  return () => window.removeEventListener("beforeunload", onBeforeUnload);
}, [dirty]);
```

**Vue.js**

```ts
import { onBeforeRouteLeave } from "vue-router";
onBeforeRouteLeave(() => {
  if (dirty.value && !confirm("Discard changes?")) return false;
});
```

## 164: How do you translate a route resolver?

**Angular**

```ts
export const productResolver: ResolveFn<Product> = (route) =>
  inject(ProductService).get(route.paramMap.get("id")!);
// { path: "products/:id", component: ProductPage, resolve: { product: productResolver } }
// in the component (with withComponentInputBinding): product = input.required<Product>();
```

**React**

```tsx
// React Router loader
{
  path: "products/:id",
  loader: ({ params }) => getProduct(params.id!),
  Component: ProductPage,
}
function ProductPage() {
  const product = useLoaderData() as Product;
}
```

**Next.js**

```tsx
// The page itself loads the data on the server before rendering
export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const product = await getProduct((await params).id);
  return <h1>{product.name}</h1>;
}
```

**Vue.js**

```ts
// Option 1: load in the component with a loading state (most common)
// Option 2: a per-route guard that fetches first
{
  path: "/products/:id",
  component: ProductPage,
  beforeEnter: async (to) => {
    to.meta.product = await getProduct(to.params.id as string);
  },
}
```

## 165: How do you pass static data and titles through routes?

**Angular**

```ts
{ path: "reports", component: Reports, title: "Reports", data: { roles: ["admin"] } }
// read: inject(ActivatedRoute).snapshot.data["roles"]
```

**React**

```tsx
{ path: "reports", Component: Reports, handle: { title: "Reports", roles: ["admin"] } }
// read: useMatches().at(-1)?.handle
```

**Next.js**

```tsx
// app/reports/page.tsx: static data is just code in the route file
export const metadata = { title: "Reports" };
```

**Vue.js**

```ts
{ path: "/reports", component: Reports, meta: { title: "Reports", roles: ["admin"] } }
// read: useRoute().meta.roles
```

## 166: How do you translate @defer?

**Angular**

```html
@defer (on viewport) {
<app-comments />
} @placeholder {
<p>Comments</p>
} @loading (minimum 300ms) {
<p>Loading...</p>
}
```

**React**

```tsx
const Comments = lazy(() => import("./Comments"));

<Suspense fallback={<p>Loading...</p>}>
  <Comments />
</Suspense>;
```

**Next.js**

```tsx
import dynamic from "next/dynamic";
const Comments = dynamic(() => import("./Comments"), {
  loading: () => <p>Loading...</p>,
});
```

**Vue.js**

```ts
import { defineAsyncComponent } from "vue";
const Comments = defineAsyncComponent({
  loader: () => import("./Comments.vue"),
  loadingComponent: Loading,
  delay: 200,
});
```

`lazy` and `defineAsyncComponent` load the code when the component first renders. To load only on viewport like `@defer (on viewport)`, combine them with an IntersectionObserver (next question).

## 167: How do you load a component only when it scrolls into view?

**Angular**

```html
@defer (on viewport) {
<app-heavy-chart />
} @placeholder {
<div style="height: 300px"></div>
}
```

**React**

```tsx
const HeavyChart = lazy(() => import("./HeavyChart"));

function LazyOnView() {
  const ref = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const io = new IntersectionObserver(
      ([e]) => e.isIntersecting && setVisible(true),
    );
    io.observe(ref.current!);
    return () => io.disconnect();
  }, []);
  return (
    <div ref={ref} style={{ minHeight: 300 }}>
      {visible && (
        <Suspense fallback={null}>
          <HeavyChart />
        </Suspense>
      )}
    </div>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
import { useElementVisibility } from "@vueuse/core";
const HeavyChart = defineAsyncComponent(() => import("./HeavyChart.vue"));
const box = useTemplateRef<HTMLDivElement>("box");
const visible = useElementVisibility(box);
const shown = ref(false);
watch(visible, (v) => v && (shown.value = true));
</script>

<template>
  <div ref="box" style="min-height: 300px"><HeavyChart v-if="shown" /></div>
</template>
```

## 168: How do you translate route preloading strategies?

**Angular**

```ts
provideRouter(routes, withPreloading(PreloadAllModules));
```

**React**

```tsx
// React Router: prefetch on hover/viewport with the Link prop (framework mode)
<Link to="/reports" prefetch="intent">Reports</Link>
// in plain SPA mode: call the dynamic import on hover
<Link to="/reports" onMouseEnter={() => import("./routes/Reports")}>Reports</Link>
```

**Next.js**

```tsx
// <Link> prefetches routes in the viewport automatically in production
<Link href="/reports">Reports</Link>
<Link href="/huge" prefetch={false}>Huge page</Link>
```

**Vue.js**

```vue
<RouterLink
  to="/reports"
  @mouseenter="import('./views/Reports.vue')"
>Reports</RouterLink>
```

## 169: How do you translate a reactive form with nested groups?

**Angular**

```ts
form = inject(FormBuilder).nonNullable.group({
  name: ["", Validators.required],
  address: this.fb.nonNullable.group({
    street: [""],
    city: ["", Validators.required],
  }),
});
// <div formGroupName="address"><input formControlName="city" /></div>
```

**React**

```tsx
type FormValues = { name: string; address: { street: string; city: string } };
const { register } = useForm<FormValues>();
<input {...register("name", { required: true })} />
<input {...register("address.city", { required: true })} />
```

**Vue.js**

```ts
const { defineField } = useForm<{
  name: string;
  address: { street: string; city: string };
}>();
const [city] = defineField("address.city");
```

Both React Hook Form and VeeValidate use dot paths for nested fields.

## 170: How do you translate FormArray?

**Angular**

```ts
form = this.fb.group({ phones: this.fb.array([this.fb.control("")]) });
get phones() {
  return this.form.controls.phones;
}
addPhone() {
  this.phones.push(this.fb.control(""));
}
// @for (c of phones.controls; track $index) { <input [formControl]="c" /> }
```

**React**

```tsx
const { control, register } = useForm<{ phones: { value: string }[] }>({
  defaultValues: { phones: [{ value: "" }] },
});
const { fields, append, remove } = useFieldArray({ control, name: "phones" });

return fields.map((f, i) => (
  <div key={f.id}>
    <input {...register(`phones.${i}.value`)} />
    <button type="button" onClick={() => remove(i)}>
      x
    </button>
  </div>
));
```

**Vue.js**

```ts
import { useFieldArray } from "vee-validate";
const { fields, push, remove } = useFieldArray<string>("phones");
// <input v-for="(f, i) in fields" :key="f.key" v-model="f.value" />
```

## 171: How do you translate a custom validator?

**Angular**

```ts
export const noSpaces: ValidatorFn = (control) =>
  /\s/.test(control.value) ? { noSpaces: true } : null;
// username: ["", [Validators.required, noSpaces]]
```

**React**

```tsx
<input
  {...register("username", {
    required: "Required",
    validate: (v) => !/\s/.test(v) || "No spaces allowed",
  })}
/>
// or with Zod: z.string().regex(/^\S+$/, "No spaces allowed")
```

**Vue.js**

```ts
const schema = toTypedSchema(
  z.object({ username: z.string().regex(/^\S+$/, "No spaces allowed") }),
);
```

Zod (or Valibot) schemas are a good shared target: the same schema works with React Hook Form (`zodResolver`), VeeValidate, and on the server in Next.js Server Actions.

## 172: How do you translate an async validator?

**Angular**

```ts
export const uniqueEmail =
  (api: UserApi): AsyncValidatorFn =>
  (control) =>
    api
      .emailExists(control.value)
      .pipe(map((exists) => (exists ? { taken: true } : null)));
// email: ["", { asyncValidators: [uniqueEmail(api)], updateOn: "blur" }]
```

**React**

```tsx
<input
  {...register("email", {
    validate: async (v) => !(await emailExists(v)) || "Email is taken",
  })}
/>
// useForm({ mode: "onBlur" }) to validate on blur like updateOn: "blur"
```

**Vue.js**

```ts
z.string()
  .email()
  .refine(async (v) => !(await emailExists(v)), "Email is taken");
```

## 173: How do you translate cross-field validation?

**Angular**

```ts
export const passwordsMatch: ValidatorFn = (group) =>
  group.get("password")?.value === group.get("confirm")?.value
    ? null
    : { mismatch: true };
// this.fb.group({ password: [""], confirm: [""] }, { validators: passwordsMatch })
```

**React**

```tsx
const schema = z
  .object({ password: z.string().min(8), confirm: z.string() })
  .refine((d) => d.password === d.confirm, {
    message: "Passwords do not match",
    path: ["confirm"],
  });

const { register } = useForm({ resolver: zodResolver(schema) });
```

**Vue.js**

```ts
const { defineField } = useForm({ validationSchema: toTypedSchema(schema) }); // same Zod schema
```

## 174: How do you translate Angular signal forms?

**Angular**

```ts
import { form, FormField, required, email } from "@angular/forms/signals";

@Component({
  imports: [FormField],
  template: `
    <input [formField]="f.email" />
    @if (f.email().invalid() && f.email().touched()) {
      <small>Invalid email</small>
    }
  `,
})
export class Signup {
  model = signal({ email: "" });
  f = form(this.model, (p) => {
    required(p.email);
    email(p.email);
  });
}
```

**React**

```tsx
const schema = z.object({ email: z.string().email() });
const {
  register,
  formState: { errors, touchedFields },
} = useForm({ resolver: zodResolver(schema), mode: "onBlur" });

<input {...register("email")} />;
{
  touchedFields.email && errors.email && <small>Invalid email</small>;
}
```

**Vue.js**

```ts
const { defineField, errors } = useForm({
  validationSchema: toTypedSchema(z.object({ email: z.string().email() })),
});
const [email, emailAttrs] = defineField("email");
// <input v-model="email" v-bind="emailAttrs" /> <small v-if="errors.email">Invalid email</small>
```

Signal forms keep the data in a plain signal model with a schema of rules. That maps well to a Zod schema plus a form library.

## 175: How do you translate a ControlValueAccessor custom input?

**Angular**

```ts
// Modern: a FormValueControl for signal forms, or model() for simple two-way binding
@Component({
  selector: "app-toggle",
  template: `<button (click)="value.set(!value())">
    {{ value() ? "On" : "Off" }}
  </button>`,
})
export class Toggle implements FormValueControl<boolean> {
  value = model(false);
}
// Legacy reactive forms: implement ControlValueAccessor (writeValue, registerOnChange, ...)
```

**React**

```tsx
function Toggle({
  value,
  onChange,
}: {
  value: boolean;
  onChange: (v: boolean) => void;
}) {
  return (
    <button type="button" onClick={() => onChange(!value)}>
      {value ? "On" : "Off"}
    </button>
  );
}

// with React Hook Form:
<Controller
  name="enabled"
  control={control}
  render={({ field }) => (
    <Toggle value={field.value} onChange={field.onChange} />
  )}
/>;
```

**Vue.js**

```vue
<script setup lang="ts">
const value = defineModel<boolean>({ default: false });
</script>

<template>
  <button type="button" @click="value = !value">
    {{ value ? "On" : "Off" }}
  </button>
</template>
<!-- works with v-model and with VeeValidate's useField -->
```

In React and Vue, any component with a "value in, change out" contract works as a form control. No special interface is needed.

## 176: How do you translate dirty, touched and pristine state?

**Angular**

```ts
form.dirty;
form.touched;
form.controls.name.pristine;
// signal forms: f().dirty(), f.name().touched()
```

**React**

```tsx
const {
  formState: { isDirty, dirtyFields, touchedFields },
} = useForm();
```

**Vue.js**

```ts
const { meta } = useForm(); // meta.value.dirty, meta.value.touched
const { meta: nameMeta } = useField("name"); // nameMeta.touched
```

## 177: How do you reset a form to new values?

**Angular**

```ts
this.form.reset({ name: user.name, email: user.email });
```

**React**

```tsx
const { reset } = useForm<UserForm>();
useEffect(() => {
  if (user) reset({ name: user.name, email: user.email });
}, [user, reset]);
```

**Vue.js**

```ts
const { resetForm } = useForm();
watch(
  user,
  (u) => u && resetForm({ values: { name: u.name, email: u.email } }),
);
```

## 178: How do you translate a form submit to a Next.js Server Action?

**Angular**

```ts
submit() {
  this.http.post("/api/contact", this.form.getRawValue()).subscribe(() => this.sent.set(true));
}
```

**React**

```tsx
async function submit(data: ContactForm) {
  await fetch("/api/contact", {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  });
  setSent(true);
}
```

**Next.js**

```tsx
// app/contact/actions.ts
"use server";
import { z } from "zod";

const schema = z.object({
  email: z.string().email(),
  message: z.string().min(1),
});

export async function sendContact(
  _prev: { error?: string } | null,
  formData: FormData,
) {
  const parsed = schema.safeParse(Object.fromEntries(formData));
  if (!parsed.success) return { error: "Please check the fields" };
  await saveMessage(parsed.data);
  return { error: undefined };
}
```

```tsx
// app/contact/ContactForm.tsx
"use client";
import { useActionState } from "react";
import { sendContact } from "./actions";

export function ContactForm() {
  const [state, action, pending] = useActionState(sendContact, null);
  return (
    <form action={action}>
      <input name="email" />
      <textarea name="message" />
      <button disabled={pending}>Send</button>
      {state?.error && <p>{state.error}</p>}
    </form>
  );
}
```

**Vue.js**

```ts
const submit = handleSubmit(async (data) => {
  await api("/api/contact", { method: "POST", body: data });
  sent.value = true;
});
```

## 179: What are useActionState and useFormStatus, and what is the Angular equivalent?

`useActionState` runs an async action from a form and keeps its result and pending state. `useFormStatus` lets a child of a `<form>` (like a submit button) read whether the form is submitting. Angular has no direct equivalent. You track a `saving` signal yourself, or use `resource()` for the async part.

**Angular**

```ts
saving = signal(false);
async save() {
  this.saving.set(true);
  try { await firstValueFrom(this.api.save(this.form.value)); } finally { this.saving.set(false); }
}
```

**React**

```tsx
import { useFormStatus } from "react-dom";

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? "Saving..." : "Save"}</button>;
}
```

**Vue.js**

```ts
const { isSubmitting } = useForm(); // VeeValidate tracks it
```

## 180: How do you translate optimistic updates?

**Angular**

```ts
like(post: Post) {
  this.posts.update((l) => l.map((p) => (p.id === post.id ? { ...p, likes: p.likes + 1 } : p)));
  this.api.like(post.id).subscribe({
    error: () => this.posts.update((l) => l.map((p) => (p.id === post.id ? post : p))),
  });
}
```

**React**

```tsx
function LikeButton({ likes, postId }: { likes: number; postId: string }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(
    likes,
    (n, delta: number) => n + delta,
  );
  return (
    <form
      action={async () => {
        addOptimistic(1);
        await likePost(postId); // when it finishes, React shows the real value again
      }}
    >
      <button>{optimisticLikes} likes</button>
    </form>
  );
}
```

**Vue.js**

```ts
const { mutate } = useMutation({
  mutationFn: likePost,
  onMutate: async (id) => {
    const prev = queryClient.getQueryData<Post[]>(["posts"]);
    queryClient.setQueryData<Post[]>(["posts"], (l) =>
      l?.map((p) => (p.id === id ? { ...p, likes: p.likes + 1 } : p)),
    );
    return { prev };
  },
  onError: (_e, _id, ctx) => queryClient.setQueryData(["posts"], ctx?.prev),
});
```

The TanStack Query pattern above also works in React.

## 181: How do you translate resource() and httpResource()?

**Angular**

```ts
export class UserPage {
  id = input.required<string>();
  user = httpResource<User>(() => `/api/users/${this.id()}`);
  // template: user.value(), user.isLoading(), user.error(), user.reload()
}
```

**React**

```tsx
function UserPage({ id }: { id: string }) {
  const user = useQuery({ queryKey: ["user", id], queryFn: () => getUser(id) });
  // user.data, user.isPending, user.error, user.refetch()
}
```

**Next.js**

```tsx
// Server Component: just await
export default async function UserPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const user = await getUser((await params).id);
}
```

**Vue.js**

```ts
const props = defineProps<{ id: string }>();
const user = useQuery({
  queryKey: ["user", () => props.id],
  queryFn: () => getUser(props.id),
});
```

`httpResource` and `useQuery` share the same idea: a reactive key (the URL or query key) plus a loader, with loading, error and reload built in.

## 182: How do you cache API data on the client?

**Angular**

```ts
// No built-in client cache across components. A common pattern:
@Injectable({ providedIn: "root" })
export class CountryService {
  readonly countries = httpResource<Country[]>(() => "/api/countries"); // loaded once, shared
}
```

**React**

```tsx
useQuery({
  queryKey: ["countries"],
  queryFn: getCountries,
  staleTime: 60 * 60 * 1000,
});
// every component using this key shares one cached request
```

**Next.js**

```tsx
// Server-side cache with Cache Components enabled
async function getCountries() {
  "use cache";
  cacheLife("hours");
  return fetch("https://api.example.com/countries").then((r) => r.json());
}
```

**Vue.js**

```ts
useQuery({
  queryKey: ["countries"],
  queryFn: getCountries,
  staleTime: 60 * 60 * 1000,
});
```

## 183: How do you translate infinite scrolling of a paged API?

**Angular**

```ts
export class Feed {
  items = signal<Post[]>([]);
  page = 0;
  loadMore() {
    this.api
      .page(++this.page)
      .subscribe((p) => this.items.update((l) => [...l, ...p]));
  }
}
```

**React**

```tsx
const { data, fetchNextPage, hasNextPage, isFetchingNextPage } =
  useInfiniteQuery({
    queryKey: ["feed"],
    queryFn: ({ pageParam }) => getPage(pageParam),
    initialPageParam: 1,
    getNextPageParam: (last, all) => (last.length ? all.length + 1 : undefined),
  });
const items = data?.pages.flat() ?? [];
```

**Vue.js**

```ts
const { data, fetchNextPage, hasNextPage } = useInfiniteQuery({
  queryKey: ["feed"],
  queryFn: ({ pageParam }) => getPage(pageParam),
  initialPageParam: 1,
  getNextPageParam: (last, all) => (last.length ? all.length + 1 : undefined),
});
```

## 184: How do you refresh a list after creating an item?

**Angular**

```ts
todos = httpResource<Todo[]>(() => "/api/todos");
add(title: string) {
  this.http.post("/api/todos", { title }).subscribe(() => this.todos.reload());
}
```

**React**

```tsx
const queryClient = useQueryClient();
const add = useMutation({
  mutationFn: createTodo,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});
```

**Next.js**

```ts
"use server";
import { revalidatePath } from "next/cache";

export async function addTodo(formData: FormData) {
  await db.todo.create({ data: { title: String(formData.get("title")) } });
  revalidatePath("/todos"); // re-render the page with fresh data
}
```

**Vue.js**

```ts
const queryClient = useQueryClient();
const { mutate: add } = useMutation({
  mutationFn: createTodo,
  onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] }),
});
```

## 185: How do you translate linkedSignal?

**Angular**

```ts
export class ShippingPicker {
  options = input.required<string[]>();
  selected = linkedSignal(() => this.options()[0]); // resets when options change, still writable
}
```

**React**

```tsx
function ShippingPicker({ options }: { options: string[] }) {
  const [selected, setSelected] = useState(options[0]);
  const [prevOptions, setPrevOptions] = useState(options);
  if (options !== prevOptions) {
    // adjust state during render when a prop changes (recommended over an effect)
    setPrevOptions(options);
    setSelected(options[0]);
  }
}
// simpler: <ShippingPicker key={options.join()} options={options} />
```

**Vue.js**

```ts
const props = defineProps<{ options: string[] }>();
const selected = ref(props.options[0]);
watch(
  () => props.options,
  (o) => (selected.value = o[0]),
);
// Vue 3.4+: a writable computed is another option
```

## 186: How do you translate untracked()?

`untracked` reads a signal inside an effect or computed without making it a dependency.

**Angular**

```ts
effect(() => {
  const q = this.query(); // tracked
  const user = untracked(this.user); // not tracked
  log(q, user.id);
});
```

**React**

```tsx
// React 19.2: useEffectEvent reads the latest values without being a dependency
const onLog = useEffectEvent((q: string) => log(q, user.id));
useEffect(() => {
  onLog(query);
}, [query]);
```

**Vue.js**

```ts
// watch tracks only the source, not what the callback reads
watch(query, (q) => log(q, user.value.id));
```

## 187: How do you translate effect cleanup with onCleanup?

**Angular**

```ts
effect((onCleanup) => {
  const id = this.roomId();
  const socket = connect(id);
  onCleanup(() => socket.close());
});
```

**React**

```tsx
useEffect(() => {
  const socket = connect(roomId);
  return () => socket.close();
}, [roomId]);
```

**Vue.js**

```ts
watchEffect((onCleanup) => {
  const socket = connect(roomId.value);
  onCleanup(() => socket.close());
});
// Vue 3.5+: onWatcherCleanup(() => socket.close()) from "vue"
```

## 188: How do you translate signal equality functions?

**Angular**

```ts
point = signal({ x: 0, y: 0 }, { equal: (a, b) => a.x === b.x && a.y === b.y });
```

**React**

```tsx
// React compares with Object.is. Skip the update yourself if nothing changed.
setPoint((p) => (p.x === x && p.y === y ? p : { x, y }));
```

**Vue.js**

```ts
// a computed only triggers dependents when its value changes (Object.is),
// so for custom equality return the old object:
const point = computed((old) => {
  const next = { x: x.value, y: y.value };
  return old && old.x === next.x && old.y === next.y ? old : next;
}); // Vue 3.4+: computed receives the previous value
```

## 189: How does OnPush change detection translate?

Angular's `OnPush` skips checking a component unless its inputs change by reference, an event fires inside it, or a signal it reads changes. With signals and zoneless Angular, this is the normal way to work.

- **React:** a component re-renders when its parent re-renders. `React.memo` skips that when props are shallow-equal. The React Compiler can add this memoization automatically.
- **Vue.js:** Vue tracks which reactive values each component reads, so it only re-renders components whose dependencies changed. You get OnPush-like behavior without doing anything.

**React**

```tsx
const Row = memo(function Row({ item }: { item: Item }) {
  return <li>{item.name}</li>;
});
```

## 190: How do you provide a service at the component level?

**Angular**

```ts
@Component({
  selector: "app-wizard",
  providers: [WizardState], // every wizard instance gets its own state
  template: `<app-step-one /><app-step-two />`,
})
export class Wizard {}
```

**React**

```tsx
const WizardContext = createContext<ReturnType<typeof useWizardState> | null>(
  null,
);

function Wizard() {
  const state = useWizardState(); // new state per Wizard instance
  return (
    <WizardContext value={state}>
      <StepOne />
      <StepTwo />
    </WizardContext>
  );
}
```

**Vue.js**

```ts
// Wizard.vue
const state = useWizardState();
provide(WizardKey, state);
// StepOne.vue: const state = inject(WizardKey)!;
```

## 191: How do you translate factory providers?

**Angular**

```ts
providers: [
  {
    provide: LOGGER,
    useFactory: () =>
      inject(ENV).production ? new RemoteLogger() : new ConsoleLogger(),
  },
];
```

**React**

```tsx
const logger = import.meta.env.PROD ? new RemoteLogger() : new ConsoleLogger();
export const LoggerContext = createContext<Logger>(logger);
```

**Vue.js**

```ts
app.provide(
  LoggerKey,
  import.meta.env.PROD ? new RemoteLogger() : new ConsoleLogger(),
);
```

## 192: How do you translate APP_INITIALIZER or provideAppInitializer?

**Angular**

```ts
providers: [
  provideAppInitializer(() => inject(ConfigService).load()), // app waits for the promise
];
```

**React**

```tsx
// main.tsx
const config = await loadConfig(); // top-level await in ES modules
createRoot(document.getElementById("root")!).render(
  <ConfigContext value={config}>
    <App />
  </ConfigContext>,
);
```

**Next.js**

```ts
// Server startup code: instrumentation.ts
export async function register() {
  await initTelemetry();
}
// Per-request config: load it in the root layout (Server Component)
```

**Vue.js**

```ts
const config = await loadConfig();
createApp(App).provide(ConfigKey, config).mount("#app");
```

## 193: How do you translate a tooltip directive?

**Angular**

```ts
@Directive({
  selector: "[appTooltip]",
  host: { "(mouseenter)": "show()", "(mouseleave)": "hide()" },
})
export class Tooltip {
  text = input.required<string>({ alias: "appTooltip" });
  private el = inject(ElementRef);
  private tip?: HTMLElement;
  show() {
    this.tip = Object.assign(document.createElement("div"), {
      className: "tip",
      textContent: this.text(),
    });
    this.el.nativeElement.append(this.tip);
  }
  hide() {
    this.tip?.remove();
  }
}
// <button appTooltip="Save the file">Save</button>
```

**React**

```tsx
function Tooltip({
  text,
  children,
}: {
  text: string;
  children: React.ReactNode;
}) {
  const [open, setOpen] = useState(false);
  return (
    <span
      className="tip-wrap"
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
    >
      {children}
      {open && (
        <div role="tooltip" className="tip">
          {text}
        </div>
      )}
    </span>
  );
}
// <Tooltip text="Save the file"><button>Save</button></Tooltip>
```

**Vue.js**

```ts
const vTooltip: Directive<HTMLElement, string> = {
  mounted(el, { value }) {
    const tip = Object.assign(document.createElement("div"), {
      className: "tip",
      textContent: value,
    });
    el.addEventListener("mouseenter", () => el.append(tip));
    el.addEventListener("mouseleave", () => tip.remove());
  },
};
// <button v-tooltip="'Save the file'">Save</button>
```

For real apps, use a positioning library (Floating UI has React and Vue packages) or a headless UI kit.

## 194: How do you translate host directives?

Host directives let one Angular component reuse directive behavior. React uses hooks for this, and Vue uses composables.

**Angular**

```ts
@Component({
  selector: "app-menu-item",
  hostDirectives: [{ directive: Focusable, inputs: ["disabled"] }, Ripple],
  template: `<ng-content />`,
})
export class MenuItem {}
```

**React**

```tsx
function MenuItem({
  disabled,
  children,
}: {
  disabled?: boolean;
  children: React.ReactNode;
}) {
  const focusProps = useFocusable({ disabled });
  const rippleProps = useRipple();
  return (
    <div {...focusProps} {...rippleProps}>
      {children}
    </div>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ disabled?: boolean }>();
const el = useTemplateRef<HTMLElement>("el");
useFocusable(el, () => props.disabled);
useRipple(el);
</script>

<template>
  <div ref="el"><slot /></div>
</template>
```

## 195: How do you translate a custom structural directive?

**Angular**

```ts
@Directive({ selector: "[appHasRole]" })
export class HasRole {
  private tpl = inject(TemplateRef);
  private vcr = inject(ViewContainerRef);
  private auth = inject(AuthStore);
  role = input.required<string>({ alias: "appHasRole" });
  constructor() {
    effect(() => {
      this.vcr.clear();
      if (this.auth.roles().includes(this.role()))
        this.vcr.createEmbeddedView(this.tpl);
    });
  }
}
// <button *appHasRole="'admin'">Delete</button>
```

**React**

```tsx
function HasRole({
  role,
  children,
}: {
  role: string;
  children: React.ReactNode;
}) {
  const roles = useAuthStore((s) => s.roles);
  return roles.includes(role) ? children : null;
}
// <HasRole role="admin"><button>Delete</button></HasRole>
```

**Vue.js**

```vue
<!-- a component with a slot, or simply v-if with a composable -->
<button v-if="hasRole('admin')">Delete</button>
```

## 196: How do you translate i18n?

**Angular**

```html
<!-- @angular/localize (build-time) -->
<h1 i18n>Welcome</h1>
<!-- or Transloco (runtime) -->
<h1>{{ "home.welcome" | transloco }}</h1>
```

**React**

```tsx
import { useTranslation } from "react-i18next";
const { t } = useTranslation();
<h1>{t("home.welcome")}</h1>;
```

**Next.js**

```tsx
// next-intl, works in Server Components too
import { getTranslations } from "next-intl/server";
const t = await getTranslations("home");
<h1>{t("welcome")}</h1>;
```

**Vue.js**

```vue
<script setup lang="ts">
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>

<template>
  <h1>{{ t("home.welcome") }}</h1>
</template>
```

Runtime libraries (Transloco, react-i18next, next-intl, vue-i18n) all load JSON files, so translation files can often be reused with small key changes. `@angular/localize` uses XLIFF files and builds one bundle per locale, which needs a conversion step.

## 197: How do you translate CDK Overlay or portals?

**Angular**

```ts
// CDK Portal / Overlay attaches content to the body
const overlayRef = inject(Overlay).create();
overlayRef.attach(new ComponentPortal(Popup));
```

**React**

```tsx
import { createPortal } from "react-dom";
{
  open && createPortal(<Popup />, document.body);
}
```

**Vue.js**

```vue
<Teleport to="body">
  <Popup v-if="open" />
</Teleport>
```

The CDK also handles positioning and scroll strategies. For those, use Floating UI or a UI kit (Radix, Reka UI). The browser's Popover API (`popover` attribute) is another option that works the same in all frameworks.

## 198: How do error boundaries compare to Angular error handling?

Angular has one global `ErrorHandler`. An error in a template does not remove the component from the screen, it logs the error (and in newer versions may stop that part of the app from updating).

React unmounts the whole tree on an uncaught render error, unless an error boundary catches it. Vue keeps rendering and reports to `app.config.errorHandler`. Vue's `onErrorCaptured` in a parent can show a fallback for a failing child.

**React**

```tsx
import { ErrorBoundary } from "react-error-boundary";
<ErrorBoundary fallback={<p>Widget failed</p>}>
  <RiskyWidget />
</ErrorBoundary>;
```

**Vue.js**

```ts
const failed = ref(false);
onErrorCaptured(() => {
  failed.value = true;
  return false; // stop the error from going further up
});
```

So when translating to React, add error boundaries around independent parts of the page, or one error will blank the whole screen.

## 199: How do Next.js error.tsx and not-found.tsx work?

They are route-level error boundaries. `error.tsx` catches errors thrown while rendering that route segment (and below) and shows a fallback with a `reset` button. `not-found.tsx` renders when you call `notFound()`. Angular's closest equivalents are a wildcard route and the global `ErrorHandler` navigating to an error page.

```tsx
// app/products/[id]/error.tsx
"use client";
export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <p>Could not load the product.</p>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```

```tsx
// app/products/[id]/page.tsx
import { notFound } from "next/navigation";
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const product = await getProduct((await params).id);
  if (!product) notFound();
  return <h1>{product.name}</h1>;
}
```

## 200: How do Next.js loading.tsx and Suspense relate to Angular loading states?

`loading.tsx` wraps the page in a `<Suspense>` boundary. While the async Server Component is waiting for data, the user sees the loading UI, and the real page streams in when ready. In Angular you usually show a spinner with `@if (resource.isLoading())` or use `@defer` placeholders.

You can also add smaller `<Suspense>` boundaries inside a page so slow parts do not block fast parts:

```tsx
export default function Dashboard() {
  return (
    <>
      <Header />
      <Suspense fallback={<p>Loading sales...</p>}>
        <SalesChart /> {/* async Server Component */}
      </Suspense>
    </>
  );
}
```

## 201: How do you give different sections different layouts?

**Angular**

```ts
export const routes: Routes = [
  {
    path: "",
    component: MarketingShell,
    children: [{ path: "", component: Home }],
  },
  {
    path: "app",
    component: AppShell,
    canActivate: [authGuard],
    children: [{ path: "", component: Dashboard }],
  },
];
```

**React**

```tsx
const router = createBrowserRouter([
  { Component: MarketingShell, children: [{ path: "/", Component: Home }] },
  {
    path: "/app",
    Component: AppShell,
    children: [{ index: true, Component: Dashboard }],
  },
]);
// a route without a path is a "layout route"
```

**Next.js**

```text
app/
  (marketing)/layout.tsx   # marketing shell
  (marketing)/page.tsx     # "/"
  (app)/layout.tsx         # app shell
  (app)/app/page.tsx       # "/app"
```

**Vue.js**

```ts
const routes = [
  {
    path: "/",
    component: MarketingShell,
    children: [{ path: "", component: Home }],
  },
  {
    path: "/app",
    component: AppShell,
    children: [{ path: "", component: Dashboard }],
  },
];
```

Folders in parentheses are Next.js "route groups". They group routes under a layout without adding to the URL.

## 202: How do you prerender pages with dynamic params?

**Angular**

```ts
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  {
    path: "blog/:slug",
    renderMode: RenderMode.Prerender,
    async getPrerenderParams() {
      const posts = await inject(PostService).allSlugs();
      return posts.map((slug) => ({ slug }));
    },
  },
];
```

**React**

```tsx
// Plain Vite React has no prerendering. Use a framework (Next.js, React Router framework mode)
// or a tool like vite-plugin-ssg style prerenderers.
```

**Next.js**

```tsx
// app/blog/[slug]/page.tsx
export async function generateStaticParams() {
  const slugs = await getAllSlugs();
  return slugs.map((slug) => ({ slug }));
}
```

**Vue.js**

```ts
// Nuxt: nuxt.config.ts
export default defineNuxtConfig({
  nitro: { prerender: { routes: ["/blog/a", "/blog/b"], crawlLinks: true } },
});
```

## 203: How do you set metadata from loaded data?

**Angular**

```ts
export class ProductPage {
  product = input.required<Product>(); // from a resolver
  constructor() {
    const title = inject(Title);
    const meta = inject(Meta);
    effect(() => {
      title.setTitle(this.product().name);
      meta.updateTag({ name: "description", content: this.product().summary });
    });
  }
}
```

**React**

```tsx
function ProductPage({ product }: { product: Product }) {
  return (
    <>
      <title>{product.name}</title>
      <meta name="description" content={product.summary} />
      <h1>{product.name}</h1>
    </>
  );
}
```

**Next.js**

```tsx
export async function generateMetadata({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const product = await getProduct((await params).id); // fetch is deduped with the page's call
  return { title: product.name, description: product.summary };
}
```

**Vue.js**

```ts
useHead({
  title: () => product.value?.name,
  meta: [{ name: "description", content: () => product.value?.summary }],
});
```

## 204: How do Next.js Route Handlers relate to the Angular app's backend?

An Angular app always calls a separate backend. Next.js can host API endpoints in the same project with Route Handlers (`route.ts`). This is handy for a "backend for frontend": hiding API keys, combining calls, or handling webhooks.

**Angular**

```ts
this.http.get<Weather>("/api/weather?city=Paris"); // served by a separate backend
```

**React**

```tsx
// Vite React also needs a separate backend
fetch("/api/weather?city=Paris");
```

**Next.js**

```ts
// app/api/weather/route.ts
export async function GET(request: Request) {
  const city = new URL(request.url).searchParams.get("city");
  const res = await fetch(
    `https://weather.example.com?q=${city}&key=${process.env.WEATHER_KEY}`,
  );
  return Response.json(await res.json());
}
```

**Vue.js**

```ts
// Nuxt: server/api/weather.get.ts
export default defineEventHandler(async (event) => {
  const { city } = getQuery(event);
  return $fetch(
    `https://weather.example.com?q=${city}&key=${process.env.WEATHER_KEY}`,
  );
});
```

You don't need Route Handlers for your own pages. Server Components can read data directly, and Server Actions handle mutations.

## 205: How do you translate the dev server proxy config?

**Angular**

```json
// proxy.conf.json, used by "ng serve --proxy-config proxy.conf.json"
{ "/api": { "target": "http://localhost:3000", "secure": false } }
```

**React**

```ts
// vite.config.ts
export default defineConfig({
  server: { proxy: { "/api": "http://localhost:3000" } },
});
```

**Next.js**

```ts
// next.config.ts (works in dev and production)
const nextConfig = {
  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://localhost:3000/api/:path*",
      },
    ];
  },
};
export default nextConfig;
```

**Vue.js**

Same `vite.config.ts` as React.

## 206: How do you read and write cookies?

**Angular**

```ts
// Browser: document.cookie or a library like ngx-cookie-service
// SSR: inject(REQUEST)?.headers.get("cookie")
```

**React**

```ts
// Browser only: document.cookie or the js-cookie library
Cookies.set("theme", "dark", { expires: 365 });
```

**Next.js**

```ts
import { cookies } from "next/headers";

// read in a Server Component
const theme = (await cookies()).get("theme")?.value ?? "light";

// write in a Server Action or Route Handler
("use server");
export async function setTheme(theme: string) {
  (await cookies()).set("theme", theme, {
    httpOnly: false,
    maxAge: 60 * 60 * 24 * 365,
  });
}
```

**Vue.js**

```ts
// Vite Vue: js-cookie or useCookies from @vueuse/integrations
// Nuxt: const theme = useCookie("theme"); works on server and client
```

Using `cookies()` makes a Next.js route render dynamically (per request) instead of statically.

## 207: How does SSR compare across Angular, Next.js and Nuxt?

- **Angular:** `@angular/ssr` renders on a Node (Express) server. Route render modes in `app.routes.server.ts` choose server, client or prerender per route. All components run on both server and client.
- **Next.js:** SSR is built in. Server Components run only on the server and ship no JS. Client Components render on both. Static vs dynamic is decided per route by what APIs it uses and by caching.
- **Nuxt (Vue):** SSR is built in. All components run on both sides (no Server Components by default, though Nuxt has experimental server components and islands). `routeRules` choose SSR, prerender, SWR or client-only per route.

Angular SSR and Nuxt are closer to each other. Next.js's split between server and client code is the biggest new idea for an Angular team.

## 208: How do you fix a hydration mismatch?

The server HTML must match the first client render. Values that differ (time, random numbers, `window` size, `localStorage`) must be set after hydration.

**Angular**

```ts
export class Clock {
  now = signal<string | null>(null);
  constructor() {
    afterNextRender(() => this.now.set(new Date().toLocaleTimeString())); // browser only
  }
}
```

**React**

```tsx
function Clock() {
  const [now, setNow] = useState<string | null>(null);
  useEffect(() => setNow(new Date().toLocaleTimeString()), []); // runs only in the browser
  return <span>{now ?? "--:--"}</span>;
}
```

**Vue.js**

```ts
const now = ref<string | null>(null);
onMounted(() => (now.value = new Date().toLocaleTimeString())); // onMounted does not run on the server
```

For a single attribute you know will differ, React has `suppressHydrationWarning` and Angular has `ngSkipHydration`, but use them only as a last resort.

## 209: How do you run code only in the browser?

**Angular**

```ts
export class Chart {
  constructor() {
    afterNextRender(() => new ChartLib(document.getElementById("chart")!)); // never on the server
  }
  // older: if (isPlatformBrowser(inject(PLATFORM_ID))) { ... }
}
```

**React**

```tsx
useEffect(() => {
  new ChartLib(ref.current!); // effects never run on the server
}, []);
```

**Next.js**

```tsx
// load a browser-only component without SSR (only allowed inside a Client Component)
"use client";
import dynamic from "next/dynamic";
const Map = dynamic(() => import("./Map"), { ssr: false });
```

**Vue.js**

```vue
<!-- Nuxt: <ClientOnly><Map /></ClientOnly> -->
<script setup lang="ts">
onMounted(() => new ChartLib(el.value!)); // onMounted runs only in the browser
</script>
```

## 210: How does TransferState translate?

Angular's HTTP transfer cache stores responses fetched during SSR in the HTML, so the browser does not fetch them again during hydration.

- **Next.js:** Server Components fetch on the server and send the rendered result (the RSC payload). The client never refetches. If you pass data to a Client Component as props, it is serialized for you.
- **React with TanStack Query:** prefetch on the server, `dehydrate` the cache into the HTML, and wrap the tree in `HydrationBoundary`.
- **Nuxt:** `useFetch` and `useAsyncData` put the server result into the payload and reuse it on the client.

**Angular**

```ts
provideClientHydration(
  withHttpTransferCacheOptions({ includePostRequests: false }),
);
```

**Next.js**

```tsx
// Server Component passes data down; nothing is fetched twice
const user = await getUser(id);
return <ProfileEditor user={user} />; // ProfileEditor is a Client Component
```

**Vue.js**

```ts
// Nuxt
const { data: user } = await useFetch(`/api/users/${id}`);
```

## 211: How do you translate static prerendering (SSG)?

**Angular**

```ts
// app.routes.server.ts
export const serverRoutes: ServerRoute[] = [
  { path: "about", renderMode: RenderMode.Prerender },
  { path: "**", renderMode: RenderMode.Server },
];
```

**React**

```tsx
// Vite React: no SSG built in. Use Next.js, React Router framework mode with prerender, or Astro.
```

**Next.js**

```tsx
// A page with no dynamic APIs (cookies, headers, searchParams) is prerendered at build time.
// app/about/page.tsx
export default function About() {
  return <h1>About us</h1>;
}
```

**Vue.js**

```ts
// Nuxt: nuxt.config.ts
export default defineNuxtConfig({
  routeRules: { "/about": { prerender: true } },
});
```

## 212: How does Angular incremental hydration compare to React and Vue?

**Angular**

```html
@defer (hydrate on viewport) {
<app-reviews />
}
<!-- provideClientHydration(withIncrementalHydration()) -->
```

**React**

```tsx
// React hydrates Suspense boundaries one by one (selective hydration)
// and gives priority to the part the user interacts with first.
<Suspense fallback={<ReviewsSkeleton />}>
  <Reviews />
</Suspense>
```

**Next.js**

```tsx
// Server Components never hydrate at all, only Client Components do.
// Keeping interactive parts small is the main way to cut hydration cost.
```

**Vue.js**

```ts
// Vue 3.5+: lazy hydration strategies for async components
import { defineAsyncComponent, hydrateOnVisible } from "vue";
const Reviews = defineAsyncComponent({
  loader: () => import("./Reviews.vue"),
  hydrate: hydrateOnVisible(),
});
```

Vue's `hydrateOnVisible`, `hydrateOnIdle` and `hydrateOnInteraction` are the closest match to Angular's `hydrate on` triggers.

## 213: How do you test a hook or composable that replaced a service?

**Angular**

```ts
it("increments", () => {
  const service = TestBed.inject(CounterService);
  service.increment();
  expect(service.count()).toBe(1);
});
```

**React**

```tsx
import { renderHook, act } from "@testing-library/react";

it("increments", () => {
  const { result } = renderHook(() => useCounter());
  act(() => result.current.increment());
  expect(result.current.count).toBe(1);
});
```

**Vue.js**

```ts
it("increments", () => {
  const { count, increment } = useCounter(); // composables without lifecycle hooks can be called directly
  increment();
  expect(count.value).toBe(1);
});
```

If a Vue composable uses `onMounted` or `inject`, mount a small test component that calls it.

## 214: How do you replace HttpTestingController in tests?

Use Mock Service Worker (MSW). It intercepts `fetch` at the network level, so the same mocks work for React, Next.js client components, Vue and even Angular.

**Angular**

```ts
const http = TestBed.inject(HttpTestingController);
service.getUsers().subscribe((u) => expect(u.length).toBe(1));
http.expectOne("/api/users").flush([{ id: 1, name: "Ana" }]);
```

**React**

```ts
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";

const server = setupServer(http.get("/api/users", () => HttpResponse.json([{ id: 1, name: "Ana" }])));
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

it("shows users", async () => {
  render(<Users />, { wrapper: QueryWrapper });
  expect(await screen.findByText("Ana")).toBeInTheDocument();
});
```

**Vue.js**

Same MSW setup. Mount the component with Vue Testing Library and use `findByText`.

## 215: How do you test components that use the router?

**Angular**

```ts
TestBed.configureTestingModule({
  providers: [provideRouter([{ path: "users/:id", component: UserPage }])],
});
const harness = await RouterTestingHarness.create("/users/5");
expect(harness.routeNativeElement?.textContent).toContain("User 5");
```

**React**

```tsx
import { createMemoryRouter, RouterProvider } from "react-router";

const router = createMemoryRouter(
  [{ path: "/users/:id", element: <UserPage /> }],
  {
    initialEntries: ["/users/5"],
  },
);
render(<RouterProvider router={router} />);
expect(await screen.findByText("User 5")).toBeInTheDocument();
```

**Next.js**

```tsx
// Mock next/navigation hooks in unit tests
vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: vi.fn() }),
  usePathname: () => "/users/5",
}));
```

**Vue.js**

```ts
const router = createRouter({
  history: createMemoryHistory(),
  routes: [{ path: "/users/:id", component: UserPage }],
});
router.push("/users/5");
await router.isReady();
const wrapper = mount(UserPage, { global: { plugins: [router] } });
```

## 216: How do you test form input and submit?

**Angular**

```ts
const input: HTMLInputElement = fixture.nativeElement.querySelector("input");
input.value = "ana@test.com";
input.dispatchEvent(new Event("input"));
fixture.nativeElement.querySelector("form").dispatchEvent(new Event("submit"));
```

**React**

```tsx
const user = userEvent.setup();
const onSubmit = vi.fn();
render(<LoginForm onSubmit={onSubmit} />);
await user.type(screen.getByLabelText("Email"), "ana@test.com");
await user.click(screen.getByRole("button", { name: "Log in" }));
expect(onSubmit).toHaveBeenCalledWith(
  expect.objectContaining({ email: "ana@test.com" }),
);
```

**Vue.js**

```ts
const wrapper = mount(LoginForm);
await wrapper.get("input[type=email]").setValue("ana@test.com");
await wrapper.get("form").trigger("submit");
expect(wrapper.emitted("submit")?.[0]).toEqual([{ email: "ana@test.com" }]);
```

## 217: How do you mock dependencies that were injected in Angular?

**Angular**

```ts
TestBed.configureTestingModule({
  providers: [
    { provide: UserApi, useValue: { getUser: () => of({ name: "Ana" }) } },
  ],
});
```

**React**

```tsx
// Option 1: mock the module
vi.mock("../api/users", () => ({
  getUser: vi.fn().mockResolvedValue({ name: "Ana" }),
}));

// Option 2: wrap with a context provider that holds a fake
render(
  <UserApiContext value={{ getUser: async () => ({ name: "Ana" }) }}>
    <Profile />
  </UserApiContext>,
);
```

**Vue.js**

```ts
mount(Profile, {
  global: {
    provide: {
      [UserApiKey as symbol]: { getUser: async () => ({ name: "Ana" }) },
    },
  },
});
// or vi.mock("@/api/users", ...)
```

Module mocking is the most common approach in React and Vue, since most code imports dependencies directly instead of injecting them.

## 218: What replaces Angular CDK component harnesses in tests?

Testing Library queries. Harnesses hide DOM details behind methods like `button.click()` or `select.open()`. Testing Library does the same by querying the accessible role and name, which also checks your accessibility.

**Angular**

```ts
const loader = TestbedHarnessEnvironment.loader(fixture);
const button = await loader.getHarness(MatButtonHarness.with({ text: "Save" }));
await button.click();
```

**React**

```tsx
await userEvent.click(screen.getByRole("button", { name: "Save" }));
```

**Vue.js**

```ts
// @testing-library/vue
await fireEvent.click(screen.getByRole("button", { name: "Save" }));
```

## 219: What replaces Angular CDK and Angular Aria for accessible widgets?

Headless UI libraries that give behavior and ARIA attributes without styles:

- **Angular:** CDK (a11y, listbox, menu) and Angular Aria (headless accessible primitives).
- **React and Next.js:** Radix UI, Base UI, React Aria Components, Headless UI.
- **Vue.js:** Reka UI (formerly Radix Vue), Headless UI for Vue.

**Angular**

```html
<ul cdkListbox [(ngModel)]="selected">
  <li cdkOption="apple">Apple</li>
  <li cdkOption="pear">Pear</li>
</ul>
```

**React**

```tsx
import * as Select from "@radix-ui/react-select";
<Select.Root value={selected} onValueChange={setSelected}>
  <Select.Trigger>
    <Select.Value />
  </Select.Trigger>
  <Select.Content>
    <Select.Item value="apple">
      <Select.ItemText>Apple</Select.ItemText>
    </Select.Item>
  </Select.Content>
</Select.Root>;
```

**Vue.js**

```vue
<SelectRoot v-model="selected">
  <SelectTrigger><SelectValue /></SelectTrigger>
  <SelectContent>
    <SelectItem value="apple"><SelectItemText>Apple</SelectItemText></SelectItem>
  </SelectContent>
</SelectRoot>
```

## 220: How do you translate a CDK focus trap?

**Angular**

```html
<div cdkTrapFocus cdkTrapFocusAutoCapture><input /> <button>OK</button></div>
```

**React**

```tsx
import { FocusTrap } from "focus-trap-react";
<FocusTrap>
  <div>
    <input /> <button>OK</button>
  </div>
</FocusTrap>;
```

**Vue.js**

```vue
<script setup lang="ts">
import { useFocusTrap } from "@vueuse/integrations/useFocusTrap";
const target = useTemplateRef<HTMLElement>("target");
const { activate } = useFocusTrap(target, { immediate: true });
</script>

<template>
  <div ref="target"><input /> <button>OK</button></div>
</template>
```

A native `<dialog>` opened with `showModal()` traps focus by itself in all of them.

## 221: How do you translate LiveAnnouncer for screen readers?

**Angular**

```ts
inject(LiveAnnouncer).announce("3 results found", "polite");
```

**React**

```tsx
function Results({ count }: { count: number }) {
  return (
    <div aria-live="polite" className="sr-only">
      {count} results found
    </div>
  );
}
```

**Vue.js**

```vue
<div aria-live="polite" class="sr-only">{{ count }} results found</div>
```

A live region must exist in the DOM before its text changes, or screen readers may not announce it. Render it once and update only the text.

## 222: How do you translate CDK virtual scrolling?

**Angular**

```html
<cdk-virtual-scroll-viewport itemSize="40" style="height: 400px">
  <div *cdkVirtualFor="let row of rows()">{{ row.name }}</div>
</cdk-virtual-scroll-viewport>
```

**React**

```tsx
import { useVirtualizer } from "@tanstack/react-virtual";

function List({ rows }: { rows: Row[] }) {
  const parentRef = useRef<HTMLDivElement>(null);
  const v = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 40,
  });
  return (
    <div ref={parentRef} style={{ height: 400, overflow: "auto" }}>
      <div style={{ height: v.getTotalSize(), position: "relative" }}>
        {v.getVirtualItems().map((item) => (
          <div
            key={item.key}
            style={{ position: "absolute", top: item.start, height: 40 }}
          >
            {rows[item.index].name}
          </div>
        ))}
      </div>
    </div>
  );
}
```

**Vue.js**

```ts
import { useVirtualizer } from "@tanstack/vue-virtual";
// same options; in Vue: getScrollElement: () => parentRef.value
```

## 223: How do you translate CDK drag and drop?

**Angular**

```html
<ul cdkDropList (cdkDropListDropped)="drop($event)">
  @for (t of tasks(); track t.id) {
  <li cdkDrag>{{ t.title }}</li>
  }
</ul>
```

```ts
drop(e: CdkDragDrop<Task[]>) {
  this.tasks.update((l) => { const c = [...l]; moveItemInArray(c, e.previousIndex, e.currentIndex); return c; });
}
```

**React**

```tsx
import { DndContext, closestCenter } from "@dnd-kit/core";
import { SortableContext, arrayMove } from "@dnd-kit/sortable";

<DndContext
  collisionDetection={closestCenter}
  onDragEnd={({ active, over }) => {
    if (!over || active.id === over.id) return;
    setTasks((l) =>
      arrayMove(
        l,
        l.findIndex((t) => t.id === active.id),
        l.findIndex((t) => t.id === over.id),
      ),
    );
  }}
>
  <SortableContext items={tasks}>
    {tasks.map((t) => (
      <SortableItem key={t.id} task={t} />
    ))}
  </SortableContext>
</DndContext>;
```

**Vue.js**

```vue
<!-- vue-draggable-plus -->
<VueDraggable v-model="tasks" tag="ul">
  <li v-for="t in tasks" :key="t.id">{{ t.title }}</li>
</VueDraggable>
```

## 224: How do you translate a Material table with sorting and paging?

**Angular**

```html
<table mat-table [dataSource]="dataSource" matSort>
  <ng-container matColumnDef="name">
    <th mat-header-cell *matHeaderCellDef mat-sort-header>Name</th>
    <td mat-cell *matCellDef="let row">{{ row.name }}</td>
  </ng-container>
  <tr mat-header-row *matHeaderRowDef="['name']"></tr>
  <tr mat-row *matRowDef="let row; columns: ['name']"></tr>
</table>
<mat-paginator [pageSize]="10" />
```

**React**

```tsx
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  flexRender,
} from "@tanstack/react-table";

const table = useReactTable({
  data,
  columns: [{ accessorKey: "name", header: "Name" }],
  getCoreRowModel: getCoreRowModel(),
  getSortedRowModel: getSortedRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
});
// render table.getHeaderGroups() and table.getRowModel().rows with flexRender
```

**Vue.js**

```ts
import { useVueTable, getCoreRowModel } from "@tanstack/vue-table";
// same options and the same rendering idea; or use Vuetify's <v-data-table>
```

TanStack Table is headless: it gives sorting, paging and filtering logic, and you write the markup.

## 225: How do you translate theming with CSS variables?

CSS custom properties work the same way in every framework, so the CSS can be copied. Only the toggle code changes.

**Angular**

```ts
export class ThemeToggle {
  dark = signal(false);
  constructor() {
    effect(() =>
      document.documentElement.classList.toggle("dark", this.dark()),
    );
  }
}
```

**React**

```tsx
const [dark, setDark] = useState(false);
useEffect(() => {
  document.documentElement.classList.toggle("dark", dark);
}, [dark]);
```

**Next.js**

```tsx
// next-themes avoids a flash of the wrong theme during SSR
import { ThemeProvider } from "next-themes";
// <html suppressHydrationWarning><body><ThemeProvider attribute="class">{children}</ThemeProvider></body></html>
```

**Vue.js**

```ts
import { useDark, useToggle } from "@vueuse/core";
const isDark = useDark();
const toggle = useToggle(isDark);
```

## 226: How do you translate ::ng-deep?

**Angular**

```css
:host ::ng-deep .mat-mdc-button {
  border-radius: 0;
}
```

**React**

```css
/* Card.module.css */
.card :global(.mui-button) {
  border-radius: 0;
}
```

**Vue.js**

```vue
<style scoped>
.card :deep(.v-btn) {
  border-radius: 0;
}
</style>
```

`::ng-deep` is deprecated. `:global` (CSS Modules) and `:deep` (Vue scoped styles) are the supported ways to reach into child components.

## 227: How do you set up Tailwind CSS in each?

Tailwind v4 needs only one import in the main CSS file plus a build integration.

**Angular**

```css
/* src/styles.css, with @tailwindcss/postcss in .postcssrc.json */
@import "tailwindcss";
```

**React**

```ts
// vite.config.ts
import tailwindcss from "@tailwindcss/vite";
export default defineConfig({ plugins: [react(), tailwindcss()] });
// index.css: @import "tailwindcss";
```

**Next.js**

```css
/* app/globals.css, with @tailwindcss/postcss in postcss.config.mjs */
@import "tailwindcss";
```

**Vue.js**

```ts
// vite.config.ts
export default defineConfig({ plugins: [vue(), tailwindcss()] });
```

Class names in templates copy over unchanged. Only `class` becomes `className` in JSX.

## 228: How do you translate a Subject-based event bus?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class EventBus {
  private events = new Subject<{ type: string; payload?: unknown }>();
  events$ = this.events.asObservable();
  emit(type: string, payload?: unknown) {
    this.events.next({ type, payload });
  }
}
```

**React**

```ts
import mitt from "mitt";
type Events = { saved: { id: string }; logout: void };
export const bus = mitt<Events>();

// in a component
useEffect(() => {
  const onSaved = (e: { id: string }) => toast(`Saved ${e.id}`);
  bus.on("saved", onSaved);
  return () => bus.off("saved", onSaved);
}, []);
```

**Vue.js**

```ts
// same mitt bus; Vue 3 removed $on/$off
onMounted(() => bus.on("saved", onSaved));
onUnmounted(() => bus.off("saved", onSaved));
```

Use an event bus only for truly global, fire-and-forget events. For shared data, a store is easier to follow.

## 229: How do you translate contentChildren for a tabs component?

**Angular**

```ts
@Component({
  selector: "app-tab",
  template: `@if (active()) {
    <ng-content />
  }`,
})
export class Tab {
  label = input.required<string>();
  active = signal(false);
}

@Component({
  selector: "app-tabs",
  template: `
    @for (t of tabs(); track t) {
      <button (click)="select(t)">{{ t.label() }}</button>
    }
    <ng-content />
  `,
})
export class Tabs {
  tabs = contentChildren(Tab);
  select(tab: Tab) {
    this.tabs().forEach((t) => t.active.set(t === tab));
  }
}
```

**React**

```tsx
// Compound components with context
const TabsCtx = createContext<{
  active: string;
  setActive: (l: string) => void;
} | null>(null);

function Tabs({
  labels,
  children,
}: {
  labels: string[];
  children: React.ReactNode;
}) {
  const [active, setActive] = useState(labels[0]);
  return (
    <TabsCtx value={{ active, setActive }}>
      {labels.map((l) => (
        <button key={l} onClick={() => setActive(l)}>
          {l}
        </button>
      ))}
      {children}
    </TabsCtx>
  );
}

function Tab({
  label,
  children,
}: {
  label: string;
  children: React.ReactNode;
}) {
  return use(TabsCtx)!.active === label ? children : null;
}
```

**Vue.js**

```ts
// Tabs.vue
const active = ref(props.labels[0]);
provide(TabsKey, { active });
// Tab.vue
const { active } = inject(TabsKey)!;
// <slot v-if="active === label" />
```

Querying children is rare in React and Vue. Children register through context or `provide`, or the parent gets the list as data.

## 230: How does a parent call a method on a child component?

**Angular**

```ts
@Component({
  template: `<app-video #player />
    <button (click)="player.play()">Play</button>`,
})
export class Page {}
// or: player = viewChild.required(VideoPlayer); this.player().play();
```

**React**

```tsx
type PlayerHandle = { play: () => void };

function VideoPlayer({ ref }: { ref: React.Ref<PlayerHandle> }) {
  const video = useRef<HTMLVideoElement>(null);
  useImperativeHandle(ref, () => ({ play: () => video.current?.play() }));
  return <video ref={video} src="movie.mp4" />;
}

function Page() {
  const player = useRef<PlayerHandle>(null);
  return (
    <>
      <VideoPlayer ref={player} />
      <button onClick={() => player.current?.play()}>Play</button>
    </>
  );
}
```

**Vue.js**

```vue
<!-- VideoPlayer.vue -->
<script setup lang="ts">
const video = useTemplateRef<HTMLVideoElement>("video");
defineExpose({ play: () => video.value?.play() });
</script>

<!-- Page.vue: <VideoPlayer ref="player" /> then player.value?.play() -->
```

In React 19, `ref` is a normal prop for function components, so `forwardRef` is no longer needed. Vue `<script setup>` components are closed by default, so you must list public methods with `defineExpose`.

## 231: How do you translate ViewContainerRef.createComponent?

**Angular**

```ts
export class Host {
  private vcr = inject(ViewContainerRef);
  addAlert(message: string) {
    const ref = this.vcr.createComponent(Alert);
    ref.setInput("message", message);
  }
}
```

**React**

```tsx
// Keep a list in state and render it
function Host() {
  const [alerts, setAlerts] = useState<{ id: number; message: string }[]>([]);
  const addAlert = (message: string) =>
    setAlerts((a) => [...a, { id: Date.now(), message }]);
  return alerts.map((a) => <Alert key={a.id} message={a.message} />);
}
```

**Vue.js**

```vue
<script setup lang="ts">
const alerts = ref<{ id: number; message: string }[]>([]);
const addAlert = (message: string) =>
  alerts.value.push({ id: Date.now(), message });
</script>

<template>
  <Alert v-for="a in alerts" :key="a.id" :message="a.message" />
</template>
```

In React and Vue you almost never create components from code. You change the data and let the template render them.

## 232: How do you translate a MatDialog-style dialog service?

**Angular**

```ts
const ref = inject(MatDialog).open(ConfirmDialog, {
  data: { text: "Delete?" },
});
ref.afterClosed().subscribe((ok) => ok && this.delete());
```

**React**

```tsx
const DialogCtx = createContext<(text: string) => Promise<boolean>>(
  async () => false,
);

function DialogProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<{
    text: string;
    resolve: (ok: boolean) => void;
  } | null>(null);
  const confirm = (text: string) =>
    new Promise<boolean>((resolve) => setState({ text, resolve }));
  const close = (ok: boolean) => {
    state?.resolve(ok);
    setState(null);
  };
  return (
    <DialogCtx value={confirm}>
      {children}
      {state && <ConfirmDialog text={state.text} onClose={close} />}
    </DialogCtx>
  );
}

// usage
const confirm = use(DialogCtx);
if (await confirm("Delete?")) remove();
```

**Vue.js**

```ts
// composables/useConfirm.ts: module-level state shared by all callers
const state = ref<{ text: string; resolve: (ok: boolean) => void } | null>(
  null,
);
export function useConfirm() {
  const confirm = (text: string) =>
    new Promise<boolean>((resolve) => (state.value = { text, resolve }));
  return { state, confirm };
}
// App.vue renders <ConfirmDialog v-if="state" ...> inside <Teleport to="body">
```

## 233: How do you translate a toast notification service?

**Angular**

```ts
inject(MatSnackBar).open("Saved", "Close", { duration: 3000 });
```

**React**

```tsx
import { Toaster, toast } from "sonner";
// once in the root: <Toaster />
toast.success("Saved");
```

**Vue.js**

```ts
// vue-sonner has the same API
import { toast } from "vue-sonner";
toast.success("Saved");
```

Both libraries keep their state in a module, so you can call `toast()` from anywhere, even outside components, like a root Angular service.

## 234: How do you translate RxJS interval and timer?

**Angular**

```ts
seconds = toSignal(interval(1000), { initialValue: 0 });
```

**React**

```tsx
function useInterval(callback: () => void, ms: number | null) {
  const saved = useRef(callback);
  useEffect(() => {
    saved.current = callback;
  });
  useEffect(() => {
    if (ms === null) return;
    const id = setInterval(() => saved.current(), ms);
    return () => clearInterval(id);
  }, [ms]);
}

const [seconds, setSeconds] = useState(0);
useInterval(() => setSeconds((s) => s + 1), 1000);
```

**Vue.js**

```ts
import { useInterval } from "@vueuse/core";
const seconds = useInterval(1000); // a ref counting up
```

The ref in `useInterval` keeps the latest callback without restarting the timer on every render, which avoids stale closures.

## 235: How do you translate a WebSocket service?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class PriceSocket {
  private socket = webSocket<Price>("wss://example.com/prices");
  prices = toSignal(this.socket.pipe(retry({ delay: 2000 })));
}
```

**React**

```tsx
function usePrices() {
  const [price, setPrice] = useState<Price | null>(null);
  useEffect(() => {
    const ws = new WebSocket("wss://example.com/prices");
    ws.onmessage = (e) => setPrice(JSON.parse(e.data));
    return () => ws.close();
  }, []);
  return price;
}
```

**Vue.js**

```ts
import { useWebSocket } from "@vueuse/core";
const { data } = useWebSocket("wss://example.com/prices", {
  autoReconnect: { delay: 2000 },
});
const price = computed(() => (data.value ? JSON.parse(data.value) : null));
```

A root Angular service keeps one connection for the whole app. A React hook opens one per component that uses it, so for shared sockets put the connection in a module or store and let components subscribe.

## 236: How do you translate Server-Sent Events?

**Angular**

```ts
messages = signal<string[]>([]);
constructor() {
  const es = new EventSource("/api/stream");
  es.onmessage = (e) => this.messages.update((m) => [...m, e.data]);
  inject(DestroyRef).onDestroy(() => es.close());
}
```

**React**

```tsx
useEffect(() => {
  const es = new EventSource("/api/stream");
  es.onmessage = (e) => setMessages((m) => [...m, e.data]);
  return () => es.close();
}, []);
```

**Next.js**

```ts
// app/api/stream/route.ts: a streaming Route Handler
export async function GET() {
  const stream = new ReadableStream({
    start(controller) {
      const id = setInterval(
        () => controller.enqueue(`data: ${Date.now()}\n\n`),
        1000,
      );
      setTimeout(() => {
        clearInterval(id);
        controller.close();
      }, 10_000);
    },
  });
  return new Response(stream.pipeThrough(new TextEncoderStream()), {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
    },
  });
}
```

**Vue.js**

```ts
import { useEventSource } from "@vueuse/core";
const { data } = useEventSource("/api/stream");
```

## 237: How do you use Web Workers in each?

The worker file itself is plain TypeScript in all of them. Only the creation code is slightly different, and all bundlers support the `new URL(..., import.meta.url)` pattern.

**Angular**

```ts
// ng generate web-worker app
const worker = new Worker(new URL("./app.worker", import.meta.url), {
  type: "module",
});
worker.onmessage = ({ data }) => this.result.set(data);
worker.postMessage(bigArray);
```

**React**

```tsx
useEffect(() => {
  const worker = new Worker(new URL("./sum.worker.ts", import.meta.url), {
    type: "module",
  });
  worker.onmessage = (e) => setResult(e.data);
  worker.postMessage(bigArray);
  return () => worker.terminate();
}, [bigArray]);
```

**Vue.js**

```ts
// Vite also supports: import SumWorker from "./sum.worker?worker"; const worker = new SumWorker();
import { useWebWorkerFn } from "@vueuse/core";
const { workerFn } = useWebWorkerFn((nums: number[]) =>
  nums.reduce((a, b) => a + b, 0),
);
const sum = await workerFn(bigArray);
```

## 238: How do you translate NgRx Store to Redux Toolkit?

**Angular**

```ts
export const add = createAction("[Cart] Add", props<{ item: string }>());
export const cartReducer = createReducer(
  { items: [] as string[] },
  on(add, (state, { item }) => ({ ...state, items: [...state.items, item] })),
);
// this.store.dispatch(add({ item: "apple" }));
// items = this.store.selectSignal(selectItems);
```

**React**

```tsx
const cartSlice = createSlice({
  name: "cart",
  initialState: { items: [] as string[] },
  reducers: {
    add: (state, action: PayloadAction<string>) => {
      state.items.push(action.payload); // Immer makes this immutable
    },
  },
});
export const { add } = cartSlice.actions;
// dispatch(add("apple"));  const items = useSelector((s: RootState) => s.cart.items);
```

**Vue.js**

```ts
export const useCartStore = defineStore("cart", {
  state: () => ({ items: [] as string[] }),
  actions: {
    add(item: string) {
      this.items.push(item);
    },
  },
});
```

The Redux DevTools extension works with both NgRx and Redux Toolkit, and Vue DevTools shows Pinia state.

## 239: How do you translate NgRx effects?

**Angular**

```ts
loadUsers$ = createEffect(() =>
  inject(Actions).pipe(
    ofType(loadUsers),
    switchMap(() =>
      inject(UserApi)
        .list()
        .pipe(
          map((users) => loadUsersSuccess({ users })),
          catchError(() => of(loadUsersFailure())),
        ),
    ),
  ),
);
```

**React**

```tsx
// Redux Toolkit thunk
export const loadUsers = createAsyncThunk("users/load", () => api.listUsers());
// extraReducers handle loadUsers.pending / fulfilled / rejected
// More often: replace the whole effect + reducer with useQuery(["users"], api.listUsers)
```

**Vue.js**

```ts
// Pinia: async logic is just an async action
actions: {
  async loadUsers() {
    this.loading = true;
    try { this.users = await api.listUsers(); } finally { this.loading = false; }
  },
},
```

## 240: How do you translate NgRx selectors?

**Angular**

```ts
export const selectCart = createFeatureSelector<CartState>("cart");
export const selectTotal = createSelector(selectCart, (c) =>
  c.items.reduce((s, i) => s + i.price, 0),
);
// total = this.store.selectSignal(selectTotal);
```

**React**

```tsx
import { createSelector } from "@reduxjs/toolkit";
const selectItems = (s: RootState) => s.cart.items;
export const selectTotal = createSelector([selectItems], (items) =>
  items.reduce((s, i) => s + i.price, 0),
);
// const total = useSelector(selectTotal);
```

**Vue.js**

```ts
// Pinia getters are cached computed values
getters: {
  total: (state) => state.items.reduce((s, i) => s + i.price, 0),
},
```

## 241: How do you translate NgRx SignalStore?

**Angular**

```ts
export const TodoStore = signalStore(
  { providedIn: "root" },
  withState({ todos: [] as Todo[], filter: "all" as Filter }),
  withComputed(({ todos, filter }) => ({
    visible: computed(() =>
      todos().filter(
        (t) => filter() === "all" || (filter() === "done") === t.done,
      ),
    ),
  })),
  withMethods((store) => ({
    add(title: string) {
      patchState(store, {
        todos: [...store.todos(), { id: Date.now(), title, done: false }],
      });
    },
  })),
);
```

**React**

```tsx
export const useTodoStore = create<{
  todos: Todo[];
  filter: Filter;
  add: (title: string) => void;
}>((set) => ({
  todos: [],
  filter: "all",
  add: (title) =>
    set((s) => ({
      todos: [...s.todos, { id: Date.now(), title, done: false }],
    })),
}));
// derived value in a selector:
const visible = useTodoStore(
  useShallow((s) =>
    s.todos.filter(
      (t) => s.filter === "all" || (s.filter === "done") === t.done,
    ),
  ),
);
```

**Vue.js**

```ts
export const useTodoStore = defineStore("todos", () => {
  const todos = ref<Todo[]>([]);
  const filter = ref<Filter>("all");
  const visible = computed(() =>
    todos.value.filter(
      (t) => filter.value === "all" || (filter.value === "done") === t.done,
    ),
  );
  const add = (title: string) =>
    todos.value.push({ id: Date.now(), title, done: false });
  return { todos, filter, visible, add };
});
```

The Pinia setup store is almost a line-by-line match for SignalStore.

## 242: How do you translate the NgRx entity adapter?

**Angular**

```ts
const adapter = createEntityAdapter<User>();
on(usersLoaded, (state, { users }) => adapter.setAll(users, state));
```

**React**

```tsx
const usersAdapter = createEntityAdapter<User>();
const usersSlice = createSlice({
  name: "users",
  initialState: usersAdapter.getInitialState(),
  reducers: { usersLoaded: usersAdapter.setAll },
});
export const { selectAll: selectAllUsers } = usersAdapter.getSelectors(
  (s: RootState) => s.users,
);
```

**Vue.js**

```ts
// Pinia has no adapter; a Map keyed by id does the same job
const byId = ref(new Map<number, User>());
const all = computed(() => [...byId.value.values()]);
const setAll = (users: User[]) =>
  (byId.value = new Map(users.map((u) => [u.id, u])));
```

Redux Toolkit's `createEntityAdapter` has nearly the same API as NgRx's.

## 243: How do you persist a store to localStorage?

**Angular**

```ts
// SignalStore with a hook
withHooks({
  onInit(store) {
    effect(() => localStorage.setItem("cart", JSON.stringify(getState(store))));
  },
});
```

**React**

```tsx
import { persist } from "zustand/middleware";
export const useCartStore = create(
  persist<{ items: string[]; add: (i: string) => void }>(
    (set) => ({
      items: [],
      add: (i) => set((s) => ({ items: [...s.items, i] })),
    }),
    { name: "cart" },
  ),
);
```

**Vue.js**

```ts
// pinia-plugin-persistedstate
export const useCartStore = defineStore(
  "cart",
  () => {
    /* ... */
  },
  { persist: true },
);
```

## 244: How do you keep filter state in the URL?

**Angular**

```ts
export class Products {
  private router = inject(Router);
  category = input<string>(); // query param bound with withComponentInputBinding()
  setCategory(c: string) {
    this.router.navigate([], {
      queryParams: { category: c },
      queryParamsHandling: "merge",
    });
  }
}
```

**React**

```tsx
const [params, setParams] = useSearchParams();
const category = params.get("category") ?? "all";
const setCategory = (c: string) =>
  setParams((p) => {
    p.set("category", c);
    return p;
  });
```

**Next.js**

```tsx
"use client";
const router = useRouter();
const pathname = usePathname();
const params = useSearchParams();
const setCategory = (c: string) => {
  const next = new URLSearchParams(params);
  next.set("category", c);
  router.replace(`${pathname}?${next}`);
};
// or the nuqs library: const [category, setCategory] = useQueryState("category");
```

**Vue.js**

```ts
import { useRouteQuery } from "@vueuse/router";
const category = useRouteQuery("category", "all"); // a ref synced to ?category=
```

## 245: How does scroll restoration translate?

**Angular**

```ts
provideRouter(
  routes,
  withInMemoryScrolling({
    scrollPositionRestoration: "enabled",
    anchorScrolling: "enabled",
  }),
);
```

**React**

```tsx
import { ScrollRestoration } from "react-router";
// inside the root layout route:
<ScrollRestoration />;
```

**Next.js**

Next.js scrolls to the top on navigation and restores the position on back/forward by default. Pass `scroll={false}` to `<Link>` to keep the position.

**Vue.js**

```ts
createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior: (to, from, saved) =>
    saved ?? (to.hash ? { el: to.hash } : { top: 0 }),
});
```

## 246: How do you show a progress bar during navigation?

**Angular**

```ts
loading = toSignal(
  inject(Router).events.pipe(
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
```

**React**

```tsx
import { useNavigation } from "react-router";
const navigation = useNavigation(); // data router
const loading = navigation.state !== "idle";
```

**Next.js**

```tsx
// useLinkStatus (Next.js 15.3+) inside a <Link> shows pending state for that link
"use client";
import { useLinkStatus } from "next/link";
function Hint() {
  const { pending } = useLinkStatus();
  return pending ? <span className="spinner" /> : null;
}
// <Link href="/reports">Reports <Hint /></Link>
```

**Vue.js**

```ts
const loading = ref(false);
router.beforeEach(() => {
  loading.value = true;
});
router.afterEach(() => {
  loading.value = false;
});
router.onError(() => {
  loading.value = false;
});
```

## 247: How do you translate a login and session flow?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class AuthService {
  private http = inject(HttpClient);
  user = signal<User | null>(null);
  login(email: string, password: string) {
    return this.http
      .post<User>("/api/login", { email, password })
      .pipe(tap((u) => this.user.set(u)));
  }
}
```

**React**

```tsx
export const useAuth = create<{
  user: User | null;
  login: (e: string, p: string) => Promise<void>;
}>((set) => ({
  user: null,
  login: async (email, password) => {
    const res = await fetch("/api/login", {
      method: "POST",
      body: JSON.stringify({ email, password }),
      headers: { "Content-Type": "application/json" },
    });
    if (!res.ok) throw new Error("Invalid credentials");
    set({ user: await res.json() });
  },
}));
```

**Next.js**

```ts
// app/login/actions.ts: set an httpOnly session cookie on the server
"use server";
export async function login(_: unknown, formData: FormData) {
  const user = await verifyPassword(
    String(formData.get("email")),
    String(formData.get("password")),
  );
  if (!user) return { error: "Invalid credentials" };
  (await cookies()).set("session", await createSession(user.id), {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
  });
  redirect("/dashboard");
}
// Libraries like Auth.js or Better Auth handle this for you.
```

**Vue.js**

```ts
export const useAuth = defineStore("auth", () => {
  const user = ref<User | null>(null);
  async function login(email: string, password: string) {
    user.value = await api<User>("/api/login", {
      method: "POST",
      body: { email, password },
    });
  }
  return { user, login };
});
```

## 248: How do you translate feature flags?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class Flags {
  private flags = httpResource<Record<string, boolean>>(() => "/api/flags", {
    defaultValue: {},
  });
  isOn = (name: string) => computed(() => this.flags.value()[name] ?? false);
}
// @if (flags.isOn("newCheckout")()) { <app-new-checkout /> }
```

**React**

```tsx
function useFlag(name: string) {
  const { data } = useQuery({
    queryKey: ["flags"],
    queryFn: getFlags,
    staleTime: Infinity,
  });
  return data?.[name] ?? false;
}
// {useFlag("newCheckout") ? <NewCheckout /> : <OldCheckout />}
```

**Next.js**

```tsx
// Evaluate flags on the server so the client never downloads the hidden variant
export default async function CheckoutPage() {
  const flags = await getFlags();
  return flags.newCheckout ? <NewCheckout /> : <OldCheckout />;
}
```

**Vue.js**

```ts
export function useFlag(name: string) {
  const { data } = useQuery({
    queryKey: ["flags"],
    queryFn: getFlags,
    staleTime: Infinity,
  });
  return computed(() => data.value?.[name] ?? false);
}
```

## 249: How do you track page views on route change?

**Angular**

```ts
inject(Router)
  .events.pipe(filter((e) => e instanceof NavigationEnd))
  .subscribe((e) => analytics.page(e.urlAfterRedirects));
```

**React**

```tsx
function PageViews() {
  const location = useLocation();
  useEffect(() => {
    analytics.page(location.pathname + location.search);
  }, [location]);
  return null;
}
```

**Next.js**

```tsx
"use client";
export function PageViews() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  useEffect(() => {
    analytics.page(`${pathname}?${searchParams}`);
  }, [pathname, searchParams]);
  return null;
}
// wrap it in <Suspense> in the layout, because useSearchParams needs one
```

**Vue.js**

```ts
router.afterEach((to) => analytics.page(to.fullPath));
```

## 250: How do you translate TypeScript path aliases?

**Angular**

```json
// tsconfig.json
{ "compilerOptions": { "paths": { "@app/*": ["src/app/*"] } } }
```

**React**

```ts
// tsconfig.json has the same "paths"; Vite needs to know too
// vite.config.ts
export default defineConfig({ resolve: { alias: { "@": "/src" } } });
// or use the vite-tsconfig-paths plugin
```

**Next.js**

```json
// tsconfig.json only; Next.js reads "paths" automatically
{ "compilerOptions": { "paths": { "@/*": ["./src/*"] } } }
```

**Vue.js**

```ts
// create-vue sets up "@" -> src in both tsconfig and vite.config.ts
resolve: { alias: { "@": fileURLToPath(new URL("./src", import.meta.url)) } }
```

## 251: How do you translate legacy @Input() and @Output() decorators?

Legacy code still uses decorators. Translate them the same way as `input()` and `output()`.

**Angular**

```ts
export class Pager {
  @Input() page = 1;
  @Input({ required: true }) total!: number;
  @Output() pageChange = new EventEmitter<number>();
}
```

**React**

```tsx
type Props = {
  page?: number;
  total: number;
  onPageChange: (p: number) => void;
};
export function Pager({ page = 1, total, onPageChange }: Props) {
  /* ... */
}
```

**Vue.js**

```ts
const { page = 1, total } = defineProps<{ page?: number; total: number }>();
const emit = defineEmits<{ "update:page": [p: number] }>();
// "update:page" lets the parent use v-model:page="current"
```

An Angular `foo` input plus `fooChange` output is the "banana in a box" pair `[(foo)]`. In Vue it becomes `v-model:foo` (or `defineModel("foo")`), and in React a `foo`/`onFooChange` prop pair.

## 252: How do you translate ngOnChanges with previous values?

**Angular**

```ts
ngOnChanges(changes: SimpleChanges) {
  const c = changes["status"];
  if (c && !c.firstChange && c.previousValue === "pending" && c.currentValue === "done") {
    this.celebrate();
  }
}
```

**React**

```tsx
function Order({ status }: { status: string }) {
  const prev = useRef(status);
  useEffect(() => {
    if (prev.current === "pending" && status === "done") celebrate();
    prev.current = status;
  }, [status]);
}
```

**Vue.js**

```ts
watch(
  () => props.status,
  (now, before) => {
    if (before === "pending" && now === "done") celebrate();
  },
);
```

Vue's `watch` gives the old value for free. In React you keep it in a ref.

## 253: How do you translate takeUntilDestroyed and manual subscriptions?

**Angular**

```ts
constructor() {
  inject(SocketService).messages$.pipe(takeUntilDestroyed()).subscribe((m) => this.handle(m));
}
```

**React**

```tsx
useEffect(() => {
  const sub = socketService.messages$.subscribe(handle);
  return () => sub.unsubscribe();
}, []);
```

**Vue.js**

```ts
const sub = socketService.messages$.subscribe(handle);
onUnmounted(() => sub.unsubscribe());
// or useSubscription(socketService.messages$.subscribe(handle)) from @vueuse/rxjs
```

The rule is the same everywhere: anything you subscribe to, you must unsubscribe from when the component goes away.

## 254: How do you translate the keyvalue and slice pipes?

**Angular**

```html
@for (entry of settings() | keyvalue; track entry.key) {
<p>{{ entry.key }}: {{ entry.value }}</p>
} @for (item of items() | slice: 0 : 5; track item.id) {
<li>{{ item.name }}</li>
}
```

**React**

```tsx
{
  Object.entries(settings).map(([key, value]) => (
    <p key={key}>
      {key}: {String(value)}
    </p>
  ));
}
{
  items.slice(0, 5).map((item) => <li key={item.id}>{item.name}</li>);
}
```

**Vue.js**

```vue
<p v-for="(value, key) in settings" :key="key">{{ key }}: {{ value }}</p>
<li v-for="item in items.slice(0, 5)" :key="item.id">{{ item.name }}</li>
```

Note that Angular's `keyvalue` pipe sorts by key by default. `Object.entries` and Vue's object `v-for` keep insertion order, so add `.sort()` if the order matters.

## 255: How do you translate plural and percent formatting?

**Angular**

```html
<span
  >{{ count() | i18nPlural: { "=0": "No items", "=1": "1 item", other: "# items"
  } }}</span
>
<span>{{ ratio() | percent: "1.0-1" }}</span>
```

**React**

```tsx
const plural = new Intl.PluralRules("en-US");
const label = (n: number) => (n === 0 ? "No items" : plural.select(n) === "one" ? "1 item" : `${n} items`);
const pct = new Intl.NumberFormat("en-US", { style: "percent", maximumFractionDigits: 1 });

<span>{label(count)}</span>
<span>{pct.format(ratio)}</span>
```

**Vue.js**

```vue
<span>{{ label(count) }}</span>
<span>{{ pct.format(ratio) }}</span>
<!-- vue-i18n: {{ t("items", count) }} with "No items | 1 item | {n} items" -->
```

## 256: How do you translate legacy *ngIf with else and *ngFor with trackBy?

**Angular**

```html
<div *ngIf="user$ | async as user; else loading">{{ user.name }}</div>
<ng-template #loading><spinner /></ng-template>

<li *ngFor="let item of items; trackBy: trackById; let i = index">
  {{ i }} {{ item.name }}
</li>
```

**React**

```tsx
{
  user ? <div>{user.name}</div> : <Spinner />;
}
{
  items.map((item, i) => (
    <li key={item.id}>
      {i} {item.name}
    </li>
  ));
}
```

**Vue.js**

```vue
<div v-if="user">{{ user.name }}</div>
<Spinner v-else />
<li v-for="(item, i) in items" :key="item.id">{{ i }} {{ item.name }}</li>
```

The Angular CLI has a migration (`ng generate @angular/core:control-flow`) to turn these into `@if`/`@for` first, which makes the template closer to the target.

## 257: How do you translate Renderer2 and ElementRef DOM changes?

**Angular**

```ts
export class AutoGrow {
  private el = inject(ElementRef<HTMLTextAreaElement>);
  private renderer = inject(Renderer2);
  resize() {
    const t = this.el.nativeElement;
    this.renderer.setStyle(t, "height", "auto");
    this.renderer.setStyle(t, "height", `${t.scrollHeight}px`);
  }
}
```

**React**

```tsx
function AutoGrow() {
  const ref = useRef<HTMLTextAreaElement>(null);
  const resize = () => {
    const t = ref.current!;
    t.style.height = "auto";
    t.style.height = `${t.scrollHeight}px`;
  };
  return <textarea ref={ref} onInput={resize} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const t = useTemplateRef<HTMLTextAreaElement>("t");
function resize() {
  t.value!.style.height = "auto";
  t.value!.style.height = `${t.value!.scrollHeight}px`;
}
</script>

<template><textarea ref="t" @input="resize" /></template>
```

`Renderer2` existed to abstract the DOM for server and worker rendering. React and Vue refs give the real element, and since this code only runs in event handlers, it never runs on the server.

## 258: How do you translate ChangeDetectorRef.detectChanges?

You rarely need it in any of them. It forces the DOM to update right now, usually so you can measure it.

**Angular**

```ts
this.items.update((l) => [...l, newItem]);
this.cdr.detectChanges(); // DOM now has the new row
this.list().nativeElement.lastElementChild?.scrollIntoView();
```

**React**

```tsx
import { flushSync } from "react-dom";
flushSync(() => setItems((l) => [...l, newItem]));
listRef.current?.lastElementChild?.scrollIntoView();
```

**Vue.js**

```ts
items.value.push(newItem);
await nextTick(); // wait for the DOM update
list.value?.lastElementChild?.scrollIntoView();
```

## 259: How do you translate NgZone.runOutsideAngular?

**Angular**

```ts
// Zone.js apps: avoid change detection on every mousemove
this.zone.runOutsideAngular(() => {
  window.addEventListener("mousemove", (e) => this.track(e));
});
```

**React**

```tsx
// Nothing to escape from: events added with addEventListener never trigger renders.
// Only setState causes a render, so throttle state updates instead.
useEffect(() => {
  const onMove = (e: MouseEvent) => track(e);
  window.addEventListener("mousemove", onMove);
  return () => window.removeEventListener("mousemove", onMove);
}, []);
```

**Vue.js**

```ts
// Same as React: only reactive state changes cause renders.
useEventListener(window, "mousemove", track);
```

Zoneless Angular (the default for new apps since v21) also does not need it. If the legacy app has many `runOutsideAngular` calls, the code inside can usually be translated as plain event listeners.

## 260: How do you translate a dynamic form built from a config?

**Angular**

```ts
fields =
  input.required<{ name: string; label: string; type: "text" | "number" }[]>();
form = computed(
  () =>
    new FormGroup(
      Object.fromEntries(
        this.fields().map((f) => [f.name, new FormControl("")]),
      ),
    ),
);
// @for (f of fields(); track f.name) { <label>{{ f.label }} <input [type]="f.type" [formControl]="form().controls[f.name]" /></label> }
```

**React**

```tsx
function DynamicForm({
  fields,
  onSubmit,
}: {
  fields: Field[];
  onSubmit: (v: Record<string, string>) => void;
}) {
  const { register, handleSubmit } = useForm<Record<string, string>>();
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {fields.map((f) => (
        <label key={f.name}>
          {f.label} <input type={f.type} {...register(f.name)} />
        </label>
      ))}
      <button>Save</button>
    </form>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ fields: Field[] }>();
const values = reactive<Record<string, string>>({});
</script>

<template>
  <label v-for="f in fields" :key="f.name">
    {{ f.label }} <input v-model="values[f.name]" :type="f.type" />
  </label>
</template>
```

## 261: How do you translate keyboard shortcuts?

**Angular**

```ts
@Component({
  host: { "(document:keydown.control.k)": "openSearch($event)" },
})
export class Shell {
  openSearch(e: KeyboardEvent) {
    e.preventDefault();
    this.searchOpen.set(true);
  }
}
```

**React**

```tsx
useEffect(() => {
  const onKey = (e: KeyboardEvent) => {
    if (e.ctrlKey && e.key === "k") {
      e.preventDefault();
      setSearchOpen(true);
    }
  };
  document.addEventListener("keydown", onKey);
  return () => document.removeEventListener("keydown", onKey);
}, []);
// or the react-hotkeys-hook library: useHotkeys("ctrl+k", () => setSearchOpen(true));
```

**Vue.js**

```ts
import { onKeyStroke } from "@vueuse/core";
onKeyStroke("k", (e) => {
  if (!e.ctrlKey) return;
  e.preventDefault();
  searchOpen.value = true;
});
```

## 262: How do you translate the CDK Clipboard?

**Angular**

```html
<button [cdkCopyToClipboard]="link()">Copy link</button>
```

**React**

```tsx
<button onClick={() => navigator.clipboard.writeText(link)}>Copy link</button>
```

**Vue.js**

```ts
import { useClipboard } from "@vueuse/core";
const { copy, copied } = useClipboard();
// <button @click="copy(link)">{{ copied ? "Copied!" : "Copy link" }}</button>
```

## 263: How do you translate an IntersectionObserver directive?

**Angular**

```ts
@Directive({ selector: "[appInView]" })
export class InView {
  inView = output<boolean>();
  constructor() {
    const el = inject(ElementRef).nativeElement;
    const io = new IntersectionObserver(([e]) =>
      this.inView.emit(e.isIntersecting),
    );
    afterNextRender(() => io.observe(el));
    inject(DestroyRef).onDestroy(() => io.disconnect());
  }
}
```

**React**

```tsx
function useInView<T extends Element>() {
  const ref = useRef<T>(null);
  const [inView, setInView] = useState(false);
  useEffect(() => {
    const io = new IntersectionObserver(([e]) => setInView(e.isIntersecting));
    if (ref.current) io.observe(ref.current);
    return () => io.disconnect();
  }, []);
  return [ref, inView] as const;
}
// const [ref, inView] = useInView<HTMLDivElement>(); <div ref={ref} />
```

**Vue.js**

```ts
import { useIntersectionObserver } from "@vueuse/core";
const target = useTemplateRef<HTMLElement>("target");
const inView = ref(false);
useIntersectionObserver(target, ([e]) => (inView.value = e.isIntersecting));
```

An Angular directive that attaches behavior to an element becomes a hook that returns a ref (React) or a composable that takes a ref (Vue).

## 264: How do you translate a ResizeObserver directive?

**Angular**

```ts
export class Panel {
  host = inject(ElementRef<HTMLElement>);
  width = signal(0);
  constructor() {
    const ro = new ResizeObserver(([e]) => this.width.set(e.contentRect.width));
    afterNextRender(() => ro.observe(this.host.nativeElement));
    inject(DestroyRef).onDestroy(() => ro.disconnect());
  }
}
```

**React**

```tsx
function useWidth<T extends Element>(ref: React.RefObject<T | null>) {
  const [width, setWidth] = useState(0);
  useEffect(() => {
    const ro = new ResizeObserver(([e]) => setWidth(e.contentRect.width));
    if (ref.current) ro.observe(ref.current);
    return () => ro.disconnect();
  }, [ref]);
  return width;
}
```

**Vue.js**

```ts
import { useElementSize } from "@vueuse/core";
const el = useTemplateRef<HTMLElement>("el");
const { width } = useElementSize(el);
```

## 265: How do you translate a click-outside directive?

**Angular**

```ts
@Directive({
  selector: "[appClickOutside]",
  host: { "(document:click)": "onDocClick($event)" },
})
export class ClickOutside {
  clickOutside = output<void>({ alias: "appClickOutside" });
  private el = inject(ElementRef);
  onDocClick(e: MouseEvent) {
    if (!this.el.nativeElement.contains(e.target)) this.clickOutside.emit();
  }
}
```

**React**

```tsx
function useClickOutside(
  ref: React.RefObject<HTMLElement | null>,
  handler: () => void,
) {
  useEffect(() => {
    const onDown = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) handler();
    };
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [ref, handler]);
}
```

**Vue.js**

```ts
import { onClickOutside } from "@vueuse/core";
const menu = useTemplateRef<HTMLElement>("menu");
onClickOutside(menu, () => (open.value = false));
```

## 266: How do you translate an infinite scroll directive?

**Angular**

```html
<ul>
  @for (p of posts(); track p.id) {
  <li>{{ p.title }}</li>
  }
</ul>
<div appInView (inView)="$event && loadMore()"></div>
```

**React**

```tsx
function Feed() {
  const { data, fetchNextPage, hasNextPage } = useInfiniteQuery(/* ... */);
  const [sentinel, inView] = useInView<HTMLDivElement>();
  useEffect(() => {
    if (inView && hasNextPage) fetchNextPage();
  }, [inView, hasNextPage, fetchNextPage]);
  return (
    <>
      <ul>
        {data?.pages.flat().map((p) => (
          <li key={p.id}>{p.title}</li>
        ))}
      </ul>
      <div ref={sentinel} />
    </>
  );
}
```

**Vue.js**

```ts
import { useInfiniteScroll } from "@vueuse/core";
const list = useTemplateRef<HTMLElement>("list");
useInfiniteScroll(list, () => fetchNextPage(), {
  distance: 100,
  canLoadMore: () => hasNextPage.value,
});
```

## 267: Why does my translated React component show stale values?

A function inside a component "captures" the state from the render that created it. If it runs later (in a timer, an event listener added once, or a memoized callback), it sees the old value. Angular signals and Vue refs are always read live, so this bug is new to Angular developers.

**React**

```tsx
// Bug: count is always 0 inside the interval
useEffect(() => {
  const id = setInterval(() => console.log(count), 1000);
  return () => clearInterval(id);
}, []);

// Fix 1: include it in deps (restarts the interval)
}, [count]);

// Fix 2: use the updater form for state changes
setCount((c) => c + 1);

// Fix 3: React 19.2 useEffectEvent for "read latest" logic
const logCount = useEffectEvent(() => console.log(count));
```

**Angular**

```ts
setInterval(() => console.log(this.count()), 1000); // always current
```

**Vue.js**

```ts
setInterval(() => console.log(count.value), 1000); // always current
```

## 268: Why does a translated Vue component stop updating?

The most common cause is losing reactivity by copying a value out of a ref or reactive object.

**Vue.js**

```ts
const state = reactive({ count: 0 });
let { count } = state; // plain number, no longer reactive
const props = defineProps<{ user: User }>();
const name = props.user.name; // read once in setup, never updates

// Fixes
const { count: countRef } = toRefs(state);
const name2 = computed(() => props.user.name);
const { user } = defineProps<{ user: User }>(); // Vue 3.5+: destructured props stay reactive (compiler rewrites them)
```

**Angular**

```ts
const name = this.user().name; // same trap: a plain value; use computed(() => this.user().name)
```

**React**

```tsx
// No such trap: the whole function runs again on every render, so values are always fresh.
const name = user.name;
```

The rule: in Angular and Vue, setup code runs once, so derived values must be `computed`. In React, render code runs every time.

## 269: Why does my useEffect run too often?

Usually because a dependency is a new object or function on every render.

**React**

```tsx
// Bug: options is a new object each render, so the effect runs every render
const options = { userId };
useEffect(() => {
  fetchData(options);
}, [options]);

// Fix: depend on primitive values
useEffect(() => {
  fetchData({ userId });
}, [userId]);

// Or memoize the object
const stableOptions = useMemo(() => ({ userId }), [userId]);
```

**Angular**

```ts
// Signals compare values on set(), and effect only reruns when a read signal changes
effect(() => this.fetchData({ userId: this.userId() }));
```

**Vue.js**

```ts
watch(
  () => props.userId,
  (id) => fetchData({ userId: id }),
);
```

## 270: How do you translate data loading that ran in ngOnInit when moving to Next.js?

Move it to the server. In Next.js, a page or layout can be an `async` Server Component that awaits the data directly. There is no loading flicker for the first render, and no client-side request.

**Angular**

```ts
export class OrdersPage implements OnInit {
  orders = signal<Order[]>([]);
  ngOnInit() {
    this.api.getOrders().subscribe((o) => this.orders.set(o));
  }
}
```

**React**

```tsx
function OrdersPage() {
  const { data: orders = [] } = useQuery({
    queryKey: ["orders"],
    queryFn: getOrders,
  });
  return <OrderTable orders={orders} />;
}
```

**Next.js**

```tsx
// app/orders/page.tsx
export default async function OrdersPage() {
  const orders = await getOrders(); // runs on the server
  return <OrderTable orders={orders} />; // OrderTable can be a Client Component if interactive
}
```

**Vue.js**

```ts
const orders = ref<Order[]>([]);
onMounted(async () => (orders.value = await getOrders()));
// Nuxt: const { data: orders } = await useFetch("/api/orders");
```

## 271: How do you translate a switch over an enum?

**Angular**

```ts
export enum Status {
  Draft,
  Published,
  Archived,
}

@Component({
  template: `@switch (status()) {
    @case (Status.Draft) {
      <span class="gray">Draft</span>
    }
    @case (Status.Published) {
      <span class="green">Live</span>
    }
    @default {
      <span>Archived</span>
    }
  }`,
})
export class StatusBadge {
  protected readonly Status = Status; // expose the enum to the template
  status = input.required<Status>();
}
```

**React**

```tsx
const badge: Record<Status, React.ReactNode> = {
  [Status.Draft]: <span className="gray">Draft</span>,
  [Status.Published]: <span className="green">Live</span>,
  [Status.Archived]: <span>Archived</span>,
};

export const StatusBadge = ({ status }: { status: Status }) => badge[status];
```

**Vue.js**

```vue
<script setup lang="ts">
import { Status } from "./status"; // imports are usable in the template directly
defineProps<{ status: Status }>();
</script>

<template>
  <span v-if="status === Status.Draft" class="gray">Draft</span>
  <span v-else-if="status === Status.Published" class="green">Live</span>
  <span v-else>Archived</span>
</template>
```

Angular templates only see class members, so enums must be exposed as a field. In Vue `<script setup>`, every import is available in the template. A `Record<Status, ...>` in TypeScript fails to compile if you forget a case.

## 272: When should you split a large Angular template while translating?

Split it when the template has several independent sections, deep nesting of `@if`/`@for`, or repeated chunks. In React this matters more, because big JSX trees with nested ternaries are hard to read and every state change re-renders the whole function.

A good rule: one component per section that has its own state or its own data. Pull repeated markup into small presentational components. In Next.js, also split along the server/client line: keep static parts in Server Components and pull only interactive pieces into small `"use client"` components.

## 273: What should you check when reviewing a translated component?

- Same inputs and outputs (props and callbacks/emits), with the same defaults.
- Same visible behavior: loading, empty and error states, disabled states, focus handling.
- Every subscription, timer and listener has cleanup.
- No mutation of React state. In Vue, no lost reactivity from destructuring.
- React effect dependency arrays are complete (lint passes), and there are no effects that only derive state.
- Keys on list items are stable IDs, not indexes.
- Raw HTML is sanitized (Angular did it for you before).
- Accessibility: labels, roles and keyboard behavior match the original.
- In Next.js, `"use client"` is only where needed and no secrets reach client code.
- The ported tests pass, ideally with the same end-to-end tests as the Angular app.

## 274: How do you estimate the effort of a migration?

Inventory the Angular app first: count components, services, routes, forms, directives, pipes, and third-party Angular libraries. Then group them by difficulty:

- **Easy:** presentational components, pure pipes, simple services. These go fast and could be partly automated with codemods or AI assistance plus review.
- **Medium:** forms (especially custom `ControlValueAccessor`s), route guards and resolvers, RxJS-heavy services.
- **Hard:** Angular-specific libraries (Material, CDK overlays, NgRx effects) that need a new library, custom structural directives, and anything relying on DI hierarchy tricks.

Add time for the new test setup, CI, design system parity, and SEO checks if moving to Next.js. Do one feature end to end first and use its real time to calibrate the estimate.

## 275: How do you share code between Angular and the new app during migration?

Put framework-free code in shared packages in a monorepo (Nx, Turborepo or pnpm workspaces): TypeScript models, API clients based on `fetch`, validation schemas (Zod), utilities, and design tokens. Both the Angular app and the React or Vue app import them.

```text
packages/
  models/       # interfaces, enums
  api-client/   # fetch-based functions, no HttpClient
  validation/   # Zod schemas
  tokens/       # CSS variables
apps/
  legacy-angular/
  web-next/
```

To make Angular services shareable, first refactor them so the HTTP logic lives in plain functions and the Angular service is a thin wrapper.

## 276: How do you replace Angular-specific date or utility libraries?

Libraries tied to Angular (for example `ngx-*` wrappers) usually wrap a framework-free core. Use that core directly or pick a common library:

- Dates: `date-fns`, `dayjs`, or `Temporal` where supported, instead of `DatePipe` or Moment wrappers.
- Charts: Chart.js, ECharts or D3 directly, or their React/Vue wrappers (`react-chartjs-2`, `vue-chartjs`, `echarts-for-react`, `vue-echarts`).
- Rich text: Tiptap has `@tiptap/react` and `@tiptap/vue-3`.
- Maps: Leaflet or MapLibre directly, or `react-leaflet` / `vue-leaflet`.

Keeping the same core library means the visual output stays the same, which makes testing the migration easier.

## 277: How do the build tools compare?

- **Angular:** the CLI's `@angular/build` uses esbuild for production builds and Vite as the dev server.
- **React:** Vite (esbuild/Rolldown for dev, Rollup/Rolldown for builds).
- **Next.js:** Turbopack is the default for both dev and build since Next.js 16. Webpack is still available with a flag.
- **Vue.js:** Vite.

Angular's builder is closed (custom changes need special builders), while Vite and Next.js expose plugin and config hooks. If the Angular app has a custom webpack config (`@angular-builders/custom-webpack`), list what each customization does and find the Vite or Next.js equivalent.

## 278: How do you analyze bundle size after translating?

**Angular**

```bash
ng build --stats-json
npx esbuild-visualizer --metadata dist/my-app/stats.json
```

**React**

```ts
// vite.config.ts
import { visualizer } from "rollup-plugin-visualizer";
export default defineConfig({ plugins: [react(), visualizer({ open: true })] });
```

**Next.js**

```bash
# Next.js 16.1+ has a built-in analyzer for Turbopack builds
npx next experimental-analyze
# with webpack builds: @next/bundle-analyzer
```

**Vue.js**

Same `rollup-plugin-visualizer` setup as React.

Compare the main entry and the largest route chunks with the Angular numbers. Watch for whole libraries imported for one function, like full `lodash` or icon sets.

## 279: How do you translate a PWA setup?

**Angular**

```bash
ng add @angular/pwa   # adds ngsw-config.json and the service worker
```

**React**

```ts
// vite-plugin-pwa
import { VitePWA } from "vite-plugin-pwa";
export default defineConfig({
  plugins: [react(), VitePWA({ registerType: "autoUpdate" })],
});
```

**Next.js**

```ts
// app/manifest.ts gives the web app manifest; Serwist (@serwist/next) adds a service worker
export default function manifest() {
  return {
    name: "My App",
    short_name: "App",
    start_url: "/",
    display: "standalone",
    icons: [],
  };
}
```

**Vue.js**

Same `vite-plugin-pwa` setup as React.

Angular's `ngsw-config.json` caching groups map to Workbox runtime caching rules in `vite-plugin-pwa` and Serwist.

## 280: How do you translate typed reactive forms into a schema-first form?

**Angular**

```ts
form = this.fb.nonNullable.group({
  name: ["", [Validators.required, Validators.maxLength(50)]],
  age: [18, [Validators.min(18)]],
});
type Value = ReturnType<typeof this.form.getRawValue>;
```

**React**

```tsx
const schema = z.object({
  name: z.string().min(1, "Required").max(50),
  age: z.number().min(18),
});
type Value = z.infer<typeof schema>;
const { register } = useForm<Value>({
  resolver: zodResolver(schema),
  defaultValues: { name: "", age: 18 },
});
<input type="number" {...register("age", { valueAsNumber: true })} />;
```

**Next.js**

```ts
// Reuse the same schema on the server in the Server Action
"use server";
export async function saveProfile(formData: FormData) {
  const data = schema.parse({
    name: formData.get("name"),
    age: Number(formData.get("age")),
  });
}
```

**Vue.js**

```ts
const { defineField } = useForm({
  validationSchema: toTypedSchema(schema),
  initialValues: { name: "", age: 18 },
});
```

A schema gives you the TypeScript type, client validation and server validation from one source.

## 281: How do you translate a global loading indicator for HTTP calls?

**Angular**

```ts
export const loadingInterceptor: HttpInterceptorFn = (req, next) => {
  const loading = inject(LoadingService);
  loading.start();
  return next(req).pipe(finalize(() => loading.stop()));
};
```

**React**

```tsx
import { useIsFetching, useIsMutating } from "@tanstack/react-query";
function GlobalSpinner() {
  const busy = useIsFetching() + useIsMutating() > 0;
  return busy ? <div className="top-bar-spinner" /> : null;
}
```

**Vue.js**

```ts
import { useIsFetching } from "@tanstack/vue-query";
const fetching = useIsFetching(); // a ref with the number of running queries
```

## 282: How do you translate a service that caches with shareReplay?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class ConfigService {
  readonly config$ = inject(HttpClient)
    .get<Config>("/api/config")
    .pipe(shareReplay(1));
}
```

**React**

```ts
// a module-level promise is fetched once and reused
let configPromise: Promise<Config> | undefined;
export const getConfig = () =>
  (configPromise ??= fetch("/api/config").then((r) => r.json()));

// in a component with Suspense:
const config = use(getConfig());
```

**Next.js**

```ts
import { cache } from "react";
// dedupes calls within one server request
export const getConfig = cache(
  async () =>
    (await fetch(`${process.env.API}/config`)).json() as Promise<Config>,
);
```

**Vue.js**

```ts
let configPromise: Promise<Config> | undefined;
export const getConfig = () =>
  (configPromise ??= fetch("/api/config").then((r) => r.json()));
```

With React's `use()`, the promise must be stable across renders (created outside the component or cached), or React will suspend forever.

## 283: How do you translate polling an API every few seconds?

**Angular**

```ts
status = toSignal(timer(0, 5000).pipe(switchMap(() => this.api.status())));
```

**React**

```tsx
useQuery({ queryKey: ["status"], queryFn: getStatus, refetchInterval: 5000 });
```

**Next.js**

```tsx
"use client";
// refresh the Server Component data on an interval
const router = useRouter();
useEffect(() => {
  const id = setInterval(() => router.refresh(), 5000);
  return () => clearInterval(id);
}, [router]);
```

**Vue.js**

```ts
useQuery({ queryKey: ["status"], queryFn: getStatus, refetchInterval: 5000 });
```

## 284: How do you translate a component that wraps a third-party jQuery-style widget?

**Angular**

```ts
export class DatePicker {
  host = viewChild.required<ElementRef<HTMLInputElement>>("host");
  value = model<string>("");
  constructor() {
    let picker: Picker;
    afterNextRender(() => {
      picker = new Picker(this.host().nativeElement, {
        onSelect: (d: string) => this.value.set(d),
      });
    });
    inject(DestroyRef).onDestroy(() => picker?.destroy());
  }
}
```

**React**

```tsx
function DatePicker({
  value,
  onChange,
}: {
  value: string;
  onChange: (d: string) => void;
}) {
  const ref = useRef<HTMLInputElement>(null);
  const onChangeRef = useRef(onChange);
  onChangeRef.current = onChange;
  useEffect(() => {
    const picker = new Picker(ref.current!, {
      onSelect: (d: string) => onChangeRef.current(d),
    });
    return () => picker.destroy();
  }, []);
  useEffect(() => {
    if (ref.current) ref.current.value = value;
  }, [value]);
  return <input ref={ref} defaultValue={value} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const value = defineModel<string>({ default: "" });
const host = useTemplateRef<HTMLInputElement>("host");
let picker: Picker | undefined;
onMounted(
  () =>
    (picker = new Picker(host.value!, {
      onSelect: (d: string) => (value.value = d),
    })),
);
onBeforeUnmount(() => picker?.destroy());
</script>

<template><input ref="host" :value="value" /></template>
```

The pattern is identical: create the widget after mount, destroy it on unmount, and sync values in both directions.

## 285: How do you translate a component that uses @Attribute or static host attributes?

**Angular**

```ts
@Component({
  selector: "app-icon-button",
  host: { role: "button", tabindex: "0", class: "icon-btn" },
  template: `<ng-content />`,
})
export class IconButton {}
```

**React**

```tsx
function IconButton({ children, ...rest }: React.ComponentProps<"span">) {
  return (
    <span role="button" tabIndex={0} className="icon-btn" {...rest}>
      {children}
    </span>
  );
}
```

**Vue.js**

```vue
<template>
  <span role="button" tabindex="0" class="icon-btn"><slot /></span>
</template>
<!-- extra attributes from the parent (class, id, @click) fall through to the root automatically -->
```

Vue's "fallthrough attributes" pass unknown attributes to the root element, which is close to how attributes on an Angular host element just work. In React you spread `...rest` yourself.

## 286: How do you pass through extra attributes and events to an inner element?

**Angular**

```ts
// Attributes on <app-input class="x" data-test="y"> land on the host element,
// not on the inner <input>. You must add explicit inputs for each one.
```

**React**

```tsx
function TextInput({
  label,
  ...inputProps
}: { label: string } & React.ComponentProps<"input">) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}
// <TextInput label="Name" placeholder="Ana" onBlur={...} />
```

**Vue.js**

```vue
<script setup lang="ts">
defineOptions({ inheritAttrs: false });
defineProps<{ label: string }>();
</script>

<template>
  <label>
    {{ label }}
    <input v-bind="$attrs" />
  </label>
</template>
```

This is a place where React and Vue are easier than Angular. A wrapper component can forward every native attribute without listing them.

## 287: How do you translate an Angular component with multiple selectors or attribute selector?

**Angular**

```ts
@Component({
  selector: "button[appPrimary]",
  template: `<ng-content />`,
  host: { class: "btn btn-primary" },
})
export class PrimaryButton {}
// <button appPrimary (click)="save()">Save</button>
```

**React**

```tsx
function PrimaryButton(props: React.ComponentProps<"button">) {
  return (
    <button {...props} className={`btn btn-primary ${props.className ?? ""}`} />
  );
}
// <PrimaryButton onClick={save}>Save</PrimaryButton>
```

**Vue.js**

```vue
<template>
  <button class="btn btn-primary"><slot /></button>
</template>
<!-- class and listeners from the parent are merged onto the button -->
```

Attribute selectors let Angular components keep the native element (good for accessibility). In React and Vue, the component renders the native element itself and forwards its props.

## 288: How do you translate Angular's @Optional and @Self injection flags?

**Angular**

```ts
private logger = inject(Logger, { optional: true }); // null if no provider
private form = inject(FormGroupDirective, { self: true }); // only this element's injector
```

**React**

```tsx
const LoggerContext = createContext<Logger | null>(null); // default null = "optional"
const logger = use(LoggerContext); // may be null
```

**Vue.js**

```ts
const logger = inject(LoggerKey, null); // second argument is the default
```

React context always has a default value, and Vue `inject` accepts one, so "optional" is built in. There is no `self`/`skipSelf` because React and Vue have only one tree of providers (components), not separate element and environment injectors.

## 289: How do you translate a service that depends on another service?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class OrderService {
  private http = inject(HttpClient);
  private auth = inject(AuthService);
  myOrders() {
    return this.http.get<Order[]>(`/api/users/${this.auth.user()?.id}/orders`);
  }
}
```

**React**

```tsx
export function useMyOrders() {
  const userId = useAuth((s) => s.user?.id);
  return useQuery({
    queryKey: ["orders", userId],
    queryFn: () => apiFetch<Order[]>(`/api/users/${userId}/orders`),
    enabled: !!userId,
  });
}
```

**Vue.js**

```ts
export function useMyOrders() {
  const auth = useAuthStore();
  return useQuery({
    queryKey: ["orders", () => auth.user?.id],
    queryFn: () => api<Order[]>(`/api/users/${auth.user?.id}/orders`),
    enabled: () => !!auth.user,
  });
}
```

Hooks and composables call other hooks and composables. That is how dependencies are composed instead of constructor injection.

## 290: How do you translate an abstract class used as a DI token for swappable implementations?

**Angular**

```ts
export abstract class Storage {
  abstract get(key: string): string | null;
}
providers: [
  {
    provide: Storage,
    useClass: environment.ssr ? MemoryStorage : LocalStorage,
  },
];
```

**React**

```tsx
interface Storage {
  get(key: string): string | null;
}
const StorageContext = createContext<Storage>(new LocalStorage());
// tests or SSR: <StorageContext value={new MemoryStorage()}>...</StorageContext>
```

**Vue.js**

```ts
export const StorageKey: InjectionKey<Storage> = Symbol("Storage");
app.provide(
  StorageKey,
  import.meta.env.SSR ? new MemoryStorage() : new LocalStorage(),
);
```

Use an interface as the type, and context or `provide` as the swap point. Most of the time, a simple module that picks the implementation at import time is enough.

## 291: How do you translate route-level providers?

**Angular**

```ts
{
  path: "admin",
  providers: [AdminApi, provideState(adminFeature)],
  loadChildren: () => import("./admin.routes"),
}
```

**React**

```tsx
{
  path: "admin",
  element: (
    <AdminApiProvider>
      <Outlet />
    </AdminApiProvider>
  ),
  children: adminRoutes,
}
```

**Next.js**

```tsx
// app/admin/layout.tsx
export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <AdminApiProvider>{children}</AdminApiProvider>; // AdminApiProvider is a Client Component
}
```

**Vue.js**

```ts
// AdminShell.vue (the route component that renders <RouterView />)
provide(AdminApiKey, createAdminApi());
```

The layout or parent route component that wraps all child routes is the natural home for route-scoped providers.

## 292: How do you translate a component library's global configuration?

**Angular**

```ts
providers: [
  {
    provide: MAT_FORM_FIELD_DEFAULT_OPTIONS,
    useValue: { appearance: "outline" },
  },
  provideAnimationsAsync(),
];
```

**React**

```tsx
import { ThemeProvider, createTheme } from "@mui/material/styles";
const theme = createTheme({
  components: { MuiTextField: { defaultProps: { variant: "outlined" } } },
});
<ThemeProvider theme={theme}>
  <App />
</ThemeProvider>;
```

**Vue.js**

```ts
import { createVuetify } from "vuetify";
app.use(createVuetify({ defaults: { VTextField: { variant: "outlined" } } }));
```

## 293: How do you translate an Angular app shell with a sidebar and header?

**Angular**

```ts
@Component({
  selector: "app-root",
  imports: [RouterOutlet, Sidebar, Header],
  template: `
    <app-header />
    <div class="layout">
      <app-sidebar />
      <main><router-outlet /></main>
    </div>
  `,
})
export class App {}
```

**React**

```tsx
function RootLayout() {
  return (
    <>
      <Header />
      <div className="layout">
        <Sidebar />
        <main>
          <Outlet />
        </main>
      </div>
    </>
  );
}
```

**Next.js**

```tsx
// app/layout.tsx: the layout stays mounted across navigations, like the Angular shell
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <div className="layout">
          <Sidebar />
          <main>{children}</main>
        </div>
      </body>
    </html>
  );
}
```

**Vue.js**

```vue
<template>
  <Header />
  <div class="layout">
    <Sidebar />
    <main><RouterView /></main>
  </div>
</template>
```

## 294: How do you translate a "master-detail" layout with child routes?

**Angular**

```ts
{
  path: "mail",
  component: MailList, // template: list + <router-outlet />
  children: [{ path: ":id", component: MailDetail }],
}
```

**React**

```tsx
{
  path: "mail",
  element: <MailList />, // renders the list and <Outlet />
  children: [{ path: ":id", element: <MailDetail /> }],
}
```

**Next.js**

```text
app/mail/layout.tsx      # list on the left + {children}
app/mail/page.tsx        # "Select a message"
app/mail/[id]/page.tsx   # the detail
```

**Vue.js**

```ts
{ path: "/mail", component: MailList, children: [{ path: ":id", component: MailDetail }] }
```

In Next.js the list lives in the layout, so it does not re-render or lose scroll when you open another message.

## 295: How do you translate named or auxiliary router outlets?

**Angular**

```ts
{ path: "chat", component: ChatPanel, outlet: "side" }
// <router-outlet name="side" />  and  <a [routerLink]="[{ outlets: { side: ['chat'] } }]">Chat</a>
```

**React**

```tsx
// React Router has no named outlets. Render the panel from a search param instead.
const [params] = useSearchParams();
{
  params.get("panel") === "chat" && <ChatPanel />;
}
```

**Next.js**

```text
app/layout.tsx         # receives { children, side }
app/@side/chat/page.tsx
app/@side/default.tsx  # fallback when no side route matches
```

**Vue.js**

```ts
{ path: "/inbox", components: { default: Inbox, side: ChatPanel } }
// <RouterView /> and <RouterView name="side" />
```

Next.js "parallel routes" (`@folder`) and Vue Router's named views are the closest match.

## 296: How do you translate a modal that has its own URL?

**Angular**

```ts
// Often done with an auxiliary outlet: /photos(modal:photo/5)
```

**React**

```tsx
// Pass the background location in state and render two route trees
<Link to={`/photo/${id}`} state={{ background: location }}>
  Open
</Link>
```

**Next.js**

```text
app/@modal/(.)photo/[id]/page.tsx   # intercepted route: shows as a modal on client navigation
app/photo/[id]/page.tsx             # full page on direct visit or refresh
app/@modal/default.tsx              # returns null
```

**Vue.js**

```ts
// Render the modal from route meta or a query param, e.g. /photos?photo=5
const route = useRoute();
const photoId = computed(() => route.query.photo);
```

Next.js "intercepting routes" are built for this: a link opens a modal, and the same URL opened directly shows a full page.

## 297: How do you translate an Angular app with many small NgModules into folders?

Group by feature, not by type. Each Angular feature module (`OrdersModule`, `UsersModule`) becomes a feature folder with its components, hooks or composables, API functions and tests together.

```text
src/features/orders/
  components/OrderTable.tsx   (or .vue)
  hooks/useOrders.ts          (composables/useOrders.ts in Vue)
  api.ts
  routes.tsx
  index.ts                    # public exports only
```

Shared modules (`SharedModule` with buttons, pipes) become `src/components/ui/` and `src/lib/`. In Next.js, route folders live in `app/` and feature code can sit in `src/features/` or in private folders (`_components`) next to the route.

## 298: How do you avoid prop drilling when translating deep Angular component trees?

Angular code often injects a service deep in the tree, so there is no drilling. When translating, do not replace that with props passed through five levels.

- Use context (React) or `provide`/`inject` (Vue) for values scoped to a subtree.
- Use a store (Zustand, Redux Toolkit, Pinia) for app-wide client state.
- Use a query library for server data, so each component can ask for the data it needs by key.
- Use composition: pass components as `children` or slots, so intermediate components don't need to know about the data.

```tsx
// Composition instead of drilling `user` through Layout
<Layout sidebar={<UserMenu user={user} />}>
  <Content />
</Layout>
```

## 299: How do you handle "this" binding issues when moving class methods to React?

Angular binds template handlers to the component instance automatically. React function components have no `this`, so the problem disappears. But if you translate to a React class component (legacy) or pass a method of a class instance (like a service object) as a callback, `this` can be lost.

**React**

```tsx
class Api {
  base = "/api";
  load() {
    return fetch(this.base + "/x");
  }
}
const api = new Api();
<button onClick={api.load} />; // bug: this is undefined
<button onClick={() => api.load()} />; // fix
```

**Vue.js**

```ts
// same issue when passing a class method as a callback; use an arrow function
```

Prefer plain functions and closures over classes in React and Vue code.

## 300: What order should you translate an Angular feature in?

1. **Models and API functions** first: framework-free and easy to test.
2. **Data hooks or composables** (or server data functions in Next.js) on top of the API.
3. **Leaf presentational components**: buttons, cards, tables. Port their tests.
4. **Container components and pages** that combine data and leaf components.
5. **Routes, guards and layouts**.
6. **Forms and validation**.
7. **Cross-cutting concerns**: error handling, i18n, analytics.
8. **End-to-end tests** against both apps to confirm the same behavior.

Working bottom-up means every step can be tested on its own, and pages come together at the end with fewer surprises.

# Advanced Questions (301-450)

## 301: How do the rendering models of Angular, React and Vue differ under the hood?

- **Angular** compiles templates into instructions that create and update DOM nodes directly. With signals, it knows which views read which signals and refreshes only those views (OnPush/zoneless). There is no virtual DOM.
- **React** runs the component function to produce a new virtual tree, compares it with the old one (reconciliation), and applies the differences. A state change re-renders the component and, by default, all its children.
- **Vue** compiles templates into render functions that produce a virtual DOM, but the compiler marks static parts and dynamic bindings ("patch flags"), so diffing is cheap. Reactivity tracks dependencies per component, so only components that read changed state re-render. Vue 3.6's Vapor Mode (still opt-in) compiles to direct DOM updates without a virtual DOM, close to Angular's and Solid's approach.

This affects translation: code that was cheap in Angular (a big template with many bindings) can be slower in React if a parent re-renders often, so you may need component splitting or memoization.

## 302: How does zoneless change detection compare with React and Vue scheduling?

In zoneless Angular, a signal write, an event from a template listener, or `markForCheck` schedules change detection. Angular then refreshes only the views marked dirty.

React batches all `setState` calls in an event or microtask into one render. Updates have priorities (urgent for input, lower for transitions), and the renderer can pause and resume work.

Vue batches reactive changes into a queue and flushes it in a microtask. `nextTick()` waits for that flush.

**Angular**

```ts
this.a.set(1);
this.b.set(2); // one refresh later, not two
```

**React**

```tsx
setA(1);
setB(2); // one render (automatic batching)
```

**Vue.js**

```ts
a.value = 1;
b.value = 2; // one update in the next microtask
await nextTick(); // DOM is updated now
```

All three batch, so translating several writes in a row is safe. Code that relied on Zone.js (for example, updating a plain field in a `setTimeout`) must use state or refs in the target.

## 303: How do you translate code that must run after the DOM updates?

**Angular**

```ts
this.messages.update((m) => [...m, msg]);
afterNextRender(
  { write: () => this.list().nativeElement.scrollTo({ top: 1e9 }) },
  { injector: this.injector },
);
// or afterRenderEffect(() => { this.messages(); scrollToBottom(); });
```

**React**

```tsx
useLayoutEffect(() => {
  listRef.current?.scrollTo({ top: 1e9 });
}, [messages]); // runs after DOM changes, before paint
```

**Vue.js**

```ts
watch(messages, () => list.value?.scrollTo({ top: 1e9 }), {
  flush: "post",
  deep: true,
});
// or: await nextTick(); list.value?.scrollTo(...)
```

`afterRenderEffect` and Vue's `flush: "post"` watchers are both "effect after render" tools. React's `useLayoutEffect` runs before the browser paints, so measurements don't flicker.

## 304: How does memoization differ between signals, the React Compiler and Vue computed?

- **Angular `computed`** caches its value and recomputes only when a signal it read changes. It is lazy: if nobody reads it, it does not run.
- **Vue `computed`** works the same way: cached and lazy, with automatic dependency tracking.
- **React** recomputes everything on every render unless you memoize with `useMemo`, `useCallback` or `memo`. The React Compiler (stable since v1.0) analyzes components at build time and inserts this memoization for you, keyed on the values used.

When translating, Angular `computed` maps naturally to Vue `computed`. In React, start with plain derived values. Enable the React Compiler rather than sprinkling `useMemo` everywhere, and only hand-memoize where profiling shows it matters.

## 305: How do you keep large lists fast after translating to React?

**Angular**

```ts
// Signals + OnPush: only rows whose input changes are refreshed
@for (row of rows(); track row.id) { <app-row [row]="row" /> }
```

**React**

```tsx
const Row = memo(function Row({
  row,
  onSelect,
}: {
  row: RowData;
  onSelect: (id: string) => void;
}) {
  return (
    <tr onClick={() => onSelect(row.id)}>
      <td>{row.name}</td>
    </tr>
  );
});

function Table({ rows }: { rows: RowData[] }) {
  const [selected, setSelected] = useState<string | null>(null);
  const onSelect = useCallback((id: string) => setSelected(id), []); // stable, so memo works
  return (
    <tbody>
      {rows.map((r) => (
        <Row key={r.id} row={r} onSelect={onSelect} />
      ))}
    </tbody>
  );
}
```

**Vue.js**

```vue
<!-- Vue only re-renders rows whose props changed; v-memo can skip even more work -->
<tr v-for="row in rows" :key="row.id" v-memo="[row.name, row.id === selected]">
  <td>{{ row.name }}</td>
</tr>
```

For thousands of rows, use virtualization in all of them. In React, also keep row objects immutable and stable, otherwise `memo` cannot help.

## 306: Why can React context hurt performance compared with Angular services?

When a context value changes, every component that reads that context re-renders, even if it only uses one field. An Angular service with several signals only refreshes views that read the specific signal that changed. Vue's `provide` of reactive objects is also fine-grained.

**React**

```tsx
// Bad: one big context with user + theme + cart; any change re-renders all readers
// Better: split contexts, or use a store with selectors
const cartCount = useCartStore((s) => s.items.length); // re-renders only when the count changes
```

**Angular**

```ts
// Fine-grained already
readonly user = signal<User | null>(null);
readonly cart = signal<Item[]>([]);
```

**Vue.js**

```ts
provide(AppStateKey, reactive({ user: null, cart: [] })); // components track only the fields they read
```

Use context for values that change rarely (theme, locale, auth user). Use a store with selectors for frequently changing shared state.

## 307: How do you build a signal-like store for React with useSyncExternalStore?

**Angular**

```ts
export const count = signal(0);
// any component: count(), count.set(...)
```

**React**

```tsx
function createStore<T>(initial: T) {
  let value = initial;
  const listeners = new Set<() => void>();
  return {
    get: () => value,
    set: (next: T) => {
      value = next;
      listeners.forEach((l) => l());
    },
    subscribe: (l: () => void) => {
      listeners.add(l);
      return () => listeners.delete(l);
    },
  };
}

export const countStore = createStore(0);
export const useCount = () =>
  useSyncExternalStore(countStore.subscribe, countStore.get, countStore.get);
```

**Vue.js**

```ts
// a module-level ref is already a shared reactive store
export const count = ref(0);
```

`useSyncExternalStore` is how Zustand and Redux connect to React. It is safe with concurrent rendering, and the third argument gives the value during server rendering.

## 308: How do you bridge Angular signals and React during an incremental migration?

Expose the Angular state through a framework-neutral subscribe API, and read it in React with `useSyncExternalStore`.

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class CartStore {
  readonly items = signal<Item[]>([]);

  // Bridge for non-Angular consumers
  subscribe(listener: () => void) {
    const ref = effect(
      () => {
        this.items();
        listener();
      },
      { injector: this.injector },
    );
    return () => ref.destroy();
  }
  private injector = inject(Injector);
}
// expose the instance: (window as any).cartStore = inject(CartStore) in an app initializer
```

**React**

```tsx
function useCartItems(store: CartStore) {
  return useSyncExternalStore(
    (cb) => store.subscribe(cb),
    () => store.items(),
  );
}
```

**Vue.js**

```ts
// mirror into a ref
const items = shallowRef(store.items());
const stop = store.subscribe(() => (items.value = store.items()));
onUnmounted(stop);
```

Angular effects run asynchronously, so the listener fires shortly after the write. That is fine for UI, but keep it in mind for tests. Long term, move the state into a neutral store (Zustand vanilla, or a tiny custom store) that both apps read.

## 309: How do you run Angular and React apps side by side with Module Federation?

A host app loads remote apps at runtime. Each remote exposes a `mount(element, props)` function instead of a framework component, so the host does not care which framework the remote uses.

**Angular**

```ts
// Angular host (Native Federation or Module Federation)
const { mount } = await loadRemoteModule({
  remoteName: "orders",
  exposedModule: "./mount",
});
afterNextRender(() => {
  const unmount = mount(this.host().nativeElement, { userId: this.userId() });
  this.destroyRef.onDestroy(unmount);
});
```

**React**

```tsx
// remote: expose ./mount
export function mount(el: HTMLElement, props: { userId: string }) {
  const root = createRoot(el);
  root.render(<OrdersApp {...props} />);
  return () => root.unmount();
}
```

**Vue.js**

```ts
export function mount(el: HTMLElement, props: { userId: string }) {
  const app = createApp(OrdersApp, props);
  app.mount(el);
  return () => app.unmount();
}
```

Next.js App Router does not officially support Module Federation, so for Next.js, route-level splitting (different apps on different paths behind a proxy, or Next.js multi-zones) is the usual choice.

## 310: How do you share state between microfrontends written in different frameworks?

Keep shared state small and outside any framework:

- **URL:** the most robust shared state. Every app reads the route.
- **Custom events** on `window` for notifications (`cart:updated`).
- **A tiny shared store** (vanilla Zustand, or a module that exposes `get`/`set`/`subscribe`) loaded once as a shared dependency.
- **Server state:** each app fetches from the same API, and caching makes it cheap.

```ts
// shared/cart-events.ts
export const emitCartUpdated = (count: number) =>
  window.dispatchEvent(new CustomEvent("cart:updated", { detail: { count } }));
```

```tsx
// React listener
useEffect(() => {
  const on = (e: Event) =>
    setCount((e as CustomEvent<{ count: number }>).detail.count);
  window.addEventListener("cart:updated", on);
  return () => window.removeEventListener("cart:updated", on);
}, []);
```

Avoid sharing framework objects (an Angular service instance, a React context) across apps, because it couples their versions and lifecycles.

## 311: How do you coordinate routing between an Angular shell and a React or Vue microfrontend?

Let the shell own the top-level URL and give each microfrontend a base path. The remote uses its own router with that base path, and both listen to the browser history.

- **React:** `createBrowserRouter(routes, { basename: "/orders" })`.
- **Vue:** `createWebHistory("/orders/")`.
- **Angular shell:** a wildcard child route `orders/**` that renders the host component for the remote.

Problems to watch: two routers both reacting to `popstate`, and links between apps. Use full-page-path links (`/billing/...`) and let each router ignore paths outside its base. Some teams dispatch a custom `navigate` event so the shell does the navigation.

## 312: How does React 19 support custom elements, and why does it matter for migration?

React 19 passes props to custom elements as properties when the element defines a matching property, otherwise as attributes. It also supports custom events through `on` + event name props. Before React 19, objects and arrays could not be passed to web components without refs.

**Angular**

```ts
// Angular Element exposes inputs as properties and outputs as CustomEvents
customElements.define(
  "order-summary",
  createCustomElement(OrderSummary, { injector }),
);
```

**React**

```tsx
<order-summary
  order={order}
  onorderconfirmed={(e: CustomEvent<Order>) => confirm(e.detail)}
/>
```

**Vue.js**

```vue
<order-summary :order.prop="order" @order-confirmed="confirm($event.detail)" />
```

For TypeScript in React, declare the element in `JSX.IntrinsicElements` (via `declare module "react"`). Angular Elements output names keep their case, so check the exact event name the element dispatches.

## 313: How do you build Vue components as custom elements to embed in an Angular app?

**Vue.js**

```ts
import { defineCustomElement } from "vue";
import OrderSummary from "./OrderSummary.ce.vue"; // .ce.vue inlines styles into the shadow root

customElements.define("order-summary", defineCustomElement(OrderSummary));
```

**Angular**

```ts
@Component({
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `<order-summary
    [order]="order()"
    (confirmed)="onConfirmed($event)"
  />`,
})
export class Checkout {}
```

**React**

```tsx
// React components need a wrapper library (for example, @r2wc/react-to-web-component)
customElements.define(
  "order-summary",
  r2wc(OrderSummary, { props: { order: "json" } }),
);
```

Vue has first-class support for this, which makes Vue a smooth target for a "replace leaf components first" migration.

## 314: How does Angular's hierarchical injector differ from React context?

Angular has two injector trees: environment injectors (app, routes, lazy chunks) and element injectors (components and directives). Lookup goes up the element tree, then to the environment tree. Providers can be scoped with `providers` vs `viewProviders`, and lookup can be limited with `self`, `skipSelf` and `host`. Services are created lazily when first injected and destroyed with their injector.

React context is simpler: a value flows down the component tree, and readers get the nearest provider's value. React does not create anything for you. Whatever object you put in `value` is what children get, and its lifetime is the provider component's state.

Vue's `provide`/`inject` is like React context, but values can be reactive objects or refs, so updates are fine-grained.

When translating:

- `providedIn: "root"` becomes a module singleton or a store.
- Component `providers` become a provider component that creates the object with `useState(() => new X())` or a hook.
- `viewProviders`, `host` and `skipSelf` usually have no equivalent and are not needed. Redesign around explicit providers.

## 315: How do you keep testability without DI in React and Vue?

Angular code is testable because dependencies are injected and can be swapped in `TestBed`. In React and Vue, the main seams are:

- **Module mocking** (`vi.mock`) for API modules and utilities.
- **Network mocking** (MSW) so data code runs for real against fake endpoints.
- **Context or provide** for dependencies you want to swap per test or per environment.
- **Props** for callbacks and data, which keeps components pure.

```tsx
// production
<ApiContext value={realApi}>
  <App />
</ApiContext>;
// test
render(
  <ApiContext value={fakeApi}>
    <Orders />
  </ApiContext>,
);
```

Prefer MSW over mocking your own modules. It tests more real code, and the same handlers work for the Angular and the new app during the migration.

## 316: How should an Angular developer think about React Server Components?

Think of a Server Component as an Angular component that renders on the server and never hydrates: its code, imports and data stay on the server, and only the resulting UI is sent to the browser. It can be `async` and read databases or secrets directly. Client Components are the "normal" interactive components and are shipped to the browser.

The tree can mix them: a Server Component can render Client Components and pass them serializable props or Server Component children. A Client Component cannot import a Server Component, but it can receive one as `children`.

```tsx
// Server Component
export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const product = await db.product.find((await params).id);
  return (
    <Tabs>
      {" "}
      {/* Client Component (state) */}
      <Description text={product.description} />{" "}
      {/* Server Component passed as children */}
    </Tabs>
  );
}
```

Angular SSR has no equivalent split: every Angular component renders on the server and then hydrates in the browser.

## 317: What can and cannot cross the server/client boundary in Next.js?

Props from a Server Component to a Client Component must be serializable by React: primitives, plain objects and arrays, `Date`, `Map`, `Set`, `BigInt`, typed arrays, Promises, JSX, and Server Functions (Server Actions). Class instances, regular functions, and objects with methods cannot cross.

```tsx
// Server Component
const user = await getUser(); // a plain object from the DB
return <ProfileEditor user={user} onSave={saveProfile} />; // saveProfile is a Server Action: OK

// Not allowed:
<ProfileEditor formatter={(d) => d.toISOString()} />; // plain function: error
<ProfileEditor user={new UserModel(user)} />; // class instance: methods are lost
```

Angular apps often use model classes with methods. When moving to Next.js, convert them to plain data types plus helper functions, or rebuild the class on the client.

## 318: What security risks come with Server Actions?

A Server Action is a public HTTP endpoint. Anyone can call it with any arguments, even if the button that uses it is hidden. Angular developers may treat it like a private service method, which is the main risk.

```ts
"use server";
export async function deleteProject(projectId: string) {
  const id = z.string().uuid().parse(projectId); // 1. validate input
  const session = await getSession();
  if (!session) throw new Error("Unauthorized"); // 2. authenticate
  const project = await db.project.find(id);
  if (project?.ownerId !== session.userId) throw new Error("Forbidden"); // 3. authorize
  await db.project.delete(id);
  updateTag(`projects-${session.userId}`);
}
```

Also: don't return more data than the client needs, don't trust closure variables that come from the client, and keep secrets in server-only modules. Next.js encrypts closed-over values and uses unguessable action IDs, but that is not a replacement for checks.

## 319: How do you avoid request waterfalls when translating resolvers to Next.js?

Angular resolvers for one route run in parallel. In Next.js, sequential `await`s in a component, or nested async components that each fetch, can create waterfalls.

**Angular**

```ts
resolve: { user: userResolver, orders: ordersResolver } // run in parallel
```

**Next.js**

```tsx
// Waterfall: orders waits for user
const user = await getUser(id);
const orders = await getOrders(id);

// Parallel
const [user, orders] = await Promise.all([getUser(id), getOrders(id)]);

// Or stream: start both, await the fast one, let the slow one stream in
const ordersPromise = getOrders(id);
const user = await getUser(id);
return (
  <>
    <Profile user={user} />
    <Suspense fallback={<p>Loading orders...</p>}>
      <Orders promise={ordersPromise} />{" "}
      {/* client component calls use(promise) */}
    </Suspense>
  </>
);
```

**React**

```tsx
// React Router loader: start both in parallel
loader: async ({ params }) => {
  const [user, orders] = await Promise.all([
    getUser(params.id!),
    getOrders(params.id!),
  ]);
  return { user, orders };
};
```

**Vue.js**

```ts
// Nuxt: both useFetch calls start before awaiting
const [{ data: user }, { data: orders }] = await Promise.all([
  useFetch(`/api/u/${id}`),
  useFetch(`/api/o/${id}`),
]);
```

## 320: How does streaming SSR compare across Angular, Next.js and Nuxt?

- **Next.js:** streams HTML by default. Each `<Suspense>` boundary (and `loading.tsx`) sends a fallback first, then the real content in the same response when its data is ready. Time to first byte is fast even with slow data.
- **Angular SSR:** renders the full page and waits for the app to become stable (pending HTTP calls finish) before sending HTML. Incremental hydration and `@defer` reduce JavaScript cost on the client, but HTML is not streamed per section in the same way.
- **Nuxt:** renders the full page after `await`ed data in `setup`. It has payload extraction, lazy hydration, and server components/islands, and streaming support is limited compared to Next.js.

When translating a slow Angular SSR page to Next.js, move slow data behind `<Suspense>` so the shell is sent right away.

## 321: How does Next.js 16 caching compare with Angular's HTTP transfer cache?

Angular's transfer cache only avoids refetching during hydration. It is not a shared cache between users or requests.

Next.js has a server cache. With Cache Components enabled (`cacheComponents: true`), you mark functions or components with `"use cache"`, set a lifetime with `cacheLife`, and tag entries with `cacheTag` to invalidate them later. Data that is not cached is fetched on each request, and uncached parts must sit inside `<Suspense>`.

```ts
import { cacheLife, cacheTag } from "next/cache";

export async function getProducts(category: string) {
  "use cache";
  cacheLife("hours");
  cacheTag(`products-${category}`);
  return db.product.findMany({ where: { category } });
}
```

This is closer to a CDN or Redis cache in front of an API than to anything in Angular. Be careful not to cache per-user data under a shared key.

## 322: How do you invalidate cached data after a mutation in Next.js 16?

- `updateTag(tag)`: only in Server Actions. It expires the tag and the next read waits for fresh data, so the user sees their own change right away ("read your writes").
- `revalidateTag(tag, profile)`: marks the tag stale with stale-while-revalidate behavior. In Next.js 16, the second argument (a `cacheLife` profile like `"max"`) is required.
- `revalidatePath(path)`: refreshes everything for a route.
- `refresh()`: refreshes uncached data on the client router from a Server Action.

```ts
"use server";
import { updateTag } from "next/cache";

export async function renameProduct(id: string, name: string) {
  await db.product.update({ where: { id }, data: { name } });
  updateTag(`product-${id}`);
}
```

The Angular equivalent was usually `resource.reload()` or refetching in a service, which only affects the current browser tab. In React and Vue SPAs, `queryClient.invalidateQueries` plays that role.

## 323: What are Cache Components and partial prerendering, and how do they compare to Angular render modes?

With Cache Components, one route can mix static and dynamic parts. At build time, Next.js prerenders a static shell (everything cached or not depending on request data). Parts that need request data (cookies, headers, uncached fetches) sit inside `<Suspense>` and stream in per request. This is the evolved form of "partial prerendering".

Angular's render modes (`RenderMode.Prerender`, `Server`, `Client`) choose one mode per route. Nuxt's `routeRules` are similar to Angular's. Next.js goes finer: per component within a route.

```tsx
export default function ProductPage() {
  return (
    <>
      <ProductInfo /> {/* "use cache": part of the static shell */}
      <Suspense fallback={<CartSkeleton />}>
        <PersonalizedCart /> {/* reads cookies(): rendered per request */}
      </Suspense>
    </>
  );
}
```

## 324: What does proxy.ts replace from an Angular SSR server.ts?

In Angular SSR, `server.ts` is an Express (or other Node) server you control. You can add middleware for redirects, auth checks, headers or API proxying.

In Next.js you do not own the server. `proxy.ts` (called `middleware.ts` before Next.js 16) runs before routes and can redirect, rewrite, set headers and cookies, or return a response. It runs on the Node.js runtime in Next.js 16.

```ts
// proxy.ts
import { NextResponse, type NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  if (
    !request.cookies.has("session") &&
    request.nextUrl.pathname.startsWith("/app")
  ) {
    return NextResponse.redirect(new URL("/login", request.url));
  }
  return NextResponse.next();
}

export const config = { matcher: ["/app/:path*"] };
```

API proxying from `server.ts` becomes `rewrites` in `next.config.ts` or Route Handlers. Express middleware that is not request filtering (for example, compression) is handled by Next.js or the hosting platform.

## 325: How do you translate Angular SSR route render modes to Next.js and Nuxt?

**Angular**

```ts
export const serverRoutes: ServerRoute[] = [
  { path: "", renderMode: RenderMode.Prerender },
  { path: "dashboard/**", renderMode: RenderMode.Client },
  { path: "**", renderMode: RenderMode.Server },
];
```

**Next.js**

```tsx
// "" -> a page with no request data is static automatically
// dashboard -> a Client Component page, or skip SSR for a widget with dynamic(..., { ssr: false })
// other -> pages reading cookies()/headers() or uncached data are dynamic
```

**Vue.js**

```ts
// Nuxt
export default defineNuxtConfig({
  routeRules: {
    "/": { prerender: true },
    "/dashboard/**": { ssr: false },
    "/blog/**": { swr: 3600 },
  },
});
```

**React**

```tsx
// React Router framework mode: prerender() in react-router.config.ts and ssr: true/false
```

## 326: How do you protect a page on the server without leaking data?

**Angular**

```ts
// Guards run in the browser (and during SSR). The API must still check permissions.
canActivate: [adminGuard];
```

**React**

```tsx
// SPA: a route guard only hides UI. The API must enforce access.
```

**Next.js**

```tsx
// app/admin/page.tsx
import "server-only";
export default async function AdminPage() {
  const session = await verifySession(); // reads the cookie and checks it
  if (session?.role !== "admin") notFound(); // or redirect("/login")
  const stats = await getAdminStats(); // only reached after the check
  return <Stats data={stats} />;
}
```

**Vue.js**

```ts
// Nuxt: server/api endpoints must check the session; route middleware only guards navigation
export default defineEventHandler(async (event) => {
  const session = await requireUserSession(event);
  if (session.user.role !== "admin") throw createError({ statusCode: 403 });
});
```

Put checks in a data access layer that every page and action uses, not only in layouts or the proxy. Layouts do not re-render on every client navigation, so a check only in a layout can be skipped.

## 327: How does XSS protection differ between Angular, React and Vue?

- **Angular** escapes interpolations and sanitizes values bound to `[innerHTML]`, `[href]`, `[src]` and styles. You must call `DomSanitizer.bypassSecurityTrust...` to opt out.
- **React** escapes text in JSX. `dangerouslySetInnerHTML` inserts raw HTML without sanitizing. React 19 blocks `javascript:` URLs in `href` and `src` by replacing them with a URL that throws, but it does not check other protocols.
- **Vue** escapes `{{ }}` interpolation. `v-html` inserts raw HTML without sanitizing. Vue does not sanitize URLs in `:href`.

So when you translate `[innerHTML]` or user-provided links, add sanitizing yourself.

**React**

```tsx
import DOMPurify from "dompurify";
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(html) }} />;
```

**Vue.js**

```vue
<div v-html="DOMPurify.sanitize(html)" />
```

In Next.js Server Components, use a server-safe sanitizer like `isomorphic-dompurify` or `sanitize-html`.

## 328: How do you safely render user-provided URLs?

**Angular**

```html
<a [href]="user().website">Website</a>
<!-- Angular sanitizes "javascript:" URLs to "unsafe:javascript:..." -->
```

**React**

```tsx
const safeUrl = (url: string) => {
  try {
    const u = new URL(url);
    return ["http:", "https:", "mailto:"].includes(u.protocol)
      ? u.href
      : undefined;
  } catch {
    return undefined;
  }
};
<a href={safeUrl(user.website)} rel="noopener noreferrer" target="_blank">
  Website
</a>;
```

**Vue.js**

```vue
<a
  :href="safeUrl(user.website)"
  rel="noopener noreferrer"
  target="_blank"
>Website</a>
```

Use an allow-list of protocols. Do not rely on framework behavior for URLs.

## 329: How does CSRF protection change when moving to Next.js?

Angular's `HttpClient` has built-in XSRF support: it reads a cookie (`XSRF-TOKEN`) and sends it as a header (`X-XSRF-TOKEN`) on mutating requests, if the backend sets the cookie.

Next.js Server Actions only accept `POST`, and Next.js compares the `Origin` header with the `Host` header, rejecting requests from other origins. Combined with `SameSite=Lax` (or `Strict`) cookies, this covers most CSRF risk. If you put Next.js behind a proxy that changes the host, configure `serverActions.allowedOrigins`.

Custom Route Handlers do not get this check automatically. For cookie-authenticated `POST`/`PUT`/`DELETE` Route Handlers, check `Origin` or use a CSRF token yourself. A React or Vue SPA calling an API needs the same protection the Angular app had: same-site cookies plus a token or header check on the backend.

## 330: How do you set up a Content Security Policy with nonces in each?

**Angular**

```html
<!-- index.html: Angular uses the nonce for its inline styles -->
<app-root ngCspNonce="RANDOM_NONCE"></app-root>
<!-- or provide CSP_NONCE; with SSR, generate a nonce per request in server.ts -->
```

**React**

```tsx
// Vite SPA: no per-request HTML, so use a static CSP with hashes or 'self' scripts only
```

**Next.js**

```ts
// proxy.ts: create a nonce per request; Next.js applies it to its scripts
export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString("base64");
  const csp = `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'; object-src 'none'; base-uri 'none';`;
  const headers = new Headers(request.headers);
  headers.set("x-nonce", nonce);
  headers.set("Content-Security-Policy", csp);
  const res = NextResponse.next({ request: { headers } });
  res.headers.set("Content-Security-Policy", csp);
  return res;
}
```

**Vue.js**

```ts
// Vite: html.cspNonce option adds a placeholder nonce to generated tags; the server must replace it per request
export default defineConfig({ html: { cspNonce: "NONCE_PLACEHOLDER" } });
```

Nonce-based CSP forces dynamic rendering in Next.js, because every response needs a new nonce.

## 331: How do Trusted Types work in each framework?

Trusted Types is a browser feature that blocks raw strings from reaching dangerous DOM sinks like `innerHTML`, unless they come from an approved policy.

- **Angular** supports Trusted Types out of the box. Its sanitizer creates trusted values through an `angular` policy, so you enable the CSP header `require-trusted-types-for 'script'; trusted-types angular`.
- **React** does not create policies itself. With Trusted Types enforced, `dangerouslySetInnerHTML` must receive a `TrustedHTML` value from your own policy (for example, one that wraps DOMPurify).
- **Vue** has the same situation: `v-html` needs a trusted value, and you create the policy.

```ts
const policy = window.trustedTypes?.createPolicy("app", {
  createHTML: (s) => DOMPurify.sanitize(s),
});
// React: <div dangerouslySetInnerHTML={{ __html: policy.createHTML(html) as unknown as string }} />
```

If the Angular app relied on enforced Trusted Types, plan this work early, because third-party React and Vue libraries may write to `innerHTML` without a policy.

## 332: How do you prevent secrets from leaking into the client bundle?

**Angular**

```ts
// Everything in environment.ts is bundled. Secrets must stay on the backend.
```

**React**

```ts
// Vite only exposes VITE_ variables. Never prefix a secret with VITE_.
```

**Next.js**

```ts
// lib/payments.ts
import "server-only"; // build error if a Client Component imports this file
export async function charge(amount: number) {
  return stripe.charges.create(
    { amount },
    { apiKey: process.env.STRIPE_SECRET_KEY },
  );
}
```

**Vue.js**

```ts
// Nuxt: runtimeConfig keys are server-only unless under "public"
export default defineNuxtConfig({
  runtimeConfig: { stripeKey: "", public: { apiBase: "" } },
});
```

In Next.js, also check that Server Components don't pass secret values as props to Client Components, since props are sent to the browser. React has experimental `taintObjectReference`/`taintUniqueValue` APIs to block this by mistake.

## 333: How do you design error handling that spans server and client in Next.js?

- **Expected errors** (validation, "not found", permission): return them as values from Server Actions (`{ error: "..." }`) and show them with `useActionState`. Use `notFound()` and `forbidden()`/`unauthorized()` (experimental `authInterrupts`) for HTTP-like cases.
- **Unexpected errors:** let them throw. `error.tsx` boundaries show a fallback per route segment. In production, server error messages are replaced with a generic message plus a `digest` you can look up in server logs.
- **Logging:** use `instrumentation.ts` with `onRequestError` to report server errors, and an error tracker on the client.

```ts
// instrumentation.ts
export async function onRequestError(
  error: unknown,
  request: { path: string },
) {
  await reportError(error, { path: request.path });
}
```

Angular's single `ErrorHandler` becomes three places: boundaries for UI, return values for expected failures, and instrumentation for reporting.

## 334: How do you report Core Web Vitals in each?

**Angular**

```ts
import { onCLS, onINP, onLCP } from "web-vitals";
onCLS(send);
onINP(send);
onLCP(send);
```

**React**

```tsx
// same web-vitals library in main.tsx
```

**Next.js**

```tsx
"use client";
import { useReportWebVitals } from "next/web-vitals";
export function WebVitals() {
  useReportWebVitals((metric) =>
    navigator.sendBeacon("/analytics", JSON.stringify(metric)),
  );
  return null;
}
```

**Vue.js**

```ts
// same web-vitals library in main.ts
```

Collect the same metrics from the Angular app before switching, so you can compare real-user numbers before and after the migration.

## 335: How do you set performance budgets like Angular's budgets config?

**Angular**

```json
"budgets": [
  { "type": "initial", "maximumWarning": "500kB", "maximumError": "1MB" },
  { "type": "anyComponentStyle", "maximumWarning": "4kB" }
]
```

**React**

```ts
// Vite has only a warning threshold; enforce limits in CI with size-limit
// vite.config.ts
export default defineConfig({ build: { chunkSizeWarningLimit: 500 } });
// package.json: "size-limit": [{ "path": "dist/assets/index-*.js", "limit": "200 kB" }]
```

**Next.js**

```bash
# next build prints per-route sizes; use size-limit or a Lighthouse CI budget to fail the build
npx lhci autorun
```

**Vue.js**

Same as React: `chunkSizeWarningLimit` plus `size-limit` or Lighthouse CI.

Angular is the only one that fails the build on budget by default, so add this check to CI explicitly after migrating.

## 336: How do you get fine-grained code splitting like @defer in React and Vue?

**Angular**

```html
@defer (on interaction) { <app-editor /> } @placeholder {
<button>Edit</button> }
```

**React**

```tsx
const Editor = lazy(() => import("./Editor"));

function EditSection() {
  const [show, setShow] = useState(false);
  return show ? (
    <Suspense fallback={<p>Loading editor...</p>}>
      <Editor />
    </Suspense>
  ) : (
    <button
      onClick={() => setShow(true)}
      onMouseEnter={() => import("./Editor")}
    >
      Edit
    </button>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
const Editor = defineAsyncComponent(() => import("./Editor.vue"));
const show = ref(false);
</script>

<template>
  <Editor v-if="show" />
  <button v-else @click="show = true">Edit</button>
</template>
```

`@defer` is a compiler feature that handles triggers, prefetch and placeholders in one block. React and Vue need a small wrapper, but you can build a reusable `<DeferOnInteraction>` or `<LazyOnView>` component once.

## 337: How do you translate Angular's tree-shakable providers concept?

`providedIn: "root"` means a service is only bundled if something injects it. In React and Vue, ES modules give the same effect: a module that nobody imports is not bundled.

The trap is barrel files (`index.ts` that re-exports everything) and modules with side effects (like registering a store at import time). They can pull in code that is not used. Keep `"sideEffects": false` in internal package `package.json` files, avoid huge barrels in feature folders, and in Next.js use `optimizePackageImports` for large libraries.

## 338: What causes hard-to-find hydration errors after translating to Next.js?

- Invalid HTML nesting: `<div>` inside `<p>`, `<a>` inside `<a>`. The browser fixes the server HTML, so it no longer matches React's tree. Angular templates may have had this nesting without errors.
- Browser extensions that change the DOM (password managers, translators).
- Locale and time zone differences in `toLocaleString()` between server and browser.
- Reading `localStorage`, `window.matchMedia` or `navigator` during render.
- Conditional rendering on `typeof window !== "undefined"`.

**React**

```tsx
// Wrong: different on server and client
const isMobile = typeof window !== "undefined" && window.innerWidth < 768;

// Right: same first render, then update
const [isMobile, setIsMobile] = useState(false);
useEffect(() => setIsMobile(window.innerWidth < 768), []);
```

For time zones, format dates on the server with an explicit `timeZone`, or render them in a client-only component.

## 339: How does Angular event replay compare with React's hydration of events?

Angular's event replay (on by default with hydration since v19) records clicks and other events that happen before the app hydrates, then replays them once the handlers are ready. So a click on a server-rendered button is not lost.

React also captures and replays discrete events during hydration. If a user clicks inside a `<Suspense>` boundary that is not hydrated yet, React raises the priority of that boundary, hydrates it, and then replays the event (selective hydration).

Vue has no built-in event replay. Lazy hydration strategies like `hydrateOnInteraction` hydrate on the first interaction and then re-dispatch that event.

When moving from Angular SSR to Next.js, you get similar behavior for free. Moving to Nuxt, test fast clicks on slow devices.

## 340: How do you translate a slow filter to stay responsive while typing?

**Angular**

```ts
// Typically debounced with RxJS or done in a worker
results = computed(() => heavyFilter(this.items(), this.query()));
```

**React**

```tsx
function Search({ items }: { items: Item[] }) {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query); // input stays fast, list updates when it can
  const results = useMemo(
    () => heavyFilter(items, deferredQuery),
    [items, deferredQuery],
  );
  return (
    <>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <ResultList results={results} stale={query !== deferredQuery} />
    </>
  );
}
```

**Vue.js**

```ts
const query = ref("");
const debounced = refDebounced(query, 150);
const results = computed(() => heavyFilter(props.items, debounced.value));
```

`useDeferredValue` is React's concurrent rendering: the slow re-render can be interrupted by new keystrokes. Angular and Vue don't have interruptible rendering, so debounce or move work to a worker.

## 341: How does React Suspense for data compare with Angular's resource API?

Angular's `resource()` exposes status signals (`isLoading`, `error`, `value`), and the template decides what to show. React Suspense inverts this: a component "suspends" by reading a pending promise with `use()`, and the nearest `<Suspense>` boundary shows the fallback. Errors go to the nearest error boundary.

**Angular**

```ts
user = resource({
  params: () => ({ id: this.id() }),
  loader: ({ params }) => fetchUser(params.id),
});
// @if (user.isLoading()) { <spinner /> } @else if (user.error()) { ... } @else { {{ user.value()?.name }} }
```

**React**

```tsx
function UserName({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise);
  return <span>{user.name}</span>;
}

<ErrorBoundary fallback={<p>Failed</p>}>
  <Suspense fallback={<Spinner />}>
    <UserName userPromise={userPromise} />
  </Suspense>
</ErrorBoundary>;
```

**Vue.js**

```vue
<!-- <Suspense> is still experimental in Vue; a component with top-level await in setup suspends -->
<Suspense>
  <UserName :id="id" />
  <template #fallback><Spinner /></template>
</Suspense>
```

With Suspense, loading UI is placed by layout, not by each component. That makes coordinated loading states easier, but you must create promises outside render (in a loader, a Server Component, or a cache).

## 342: How do you avoid race conditions when parameters change quickly?

When a user clicks from item 1 to item 2 quickly, the response for item 1 may arrive last and overwrite item 2.

**Angular**

```ts
// resource() and switchMap cancel or ignore stale requests automatically
product = httpResource<Product>(() => `/api/products/${this.id()}`);
```

**React**

```tsx
useEffect(() => {
  const controller = new AbortController();
  fetch(`/api/products/${id}`, { signal: controller.signal })
    .then((r) => r.json())
    .then(setProduct)
    .catch((e) => {
      if (e.name !== "AbortError") setError(e);
    });
  return () => controller.abort(); // cancel the old request when id changes
}, [id]);
```

**Vue.js**

```ts
watch(
  () => props.id,
  async (id, _old, onCleanup) => {
    const controller = new AbortController();
    onCleanup(() => controller.abort());
    product.value = await fetch(`/api/products/${id}`, {
      signal: controller.signal,
    }).then((r) => r.json());
  },
  { immediate: true },
);
```

Query libraries do this for you, which is one of the best reasons to use them when translating RxJS-heavy code.

## 343: How do you translate an RxJS pipeline with exponential backoff and polling until done?

**Angular**

```ts
jobStatus$ = (id: string) =>
  timer(0, 2000).pipe(
    switchMap(() =>
      this.api
        .status(id)
        .pipe(retry({ count: 3, delay: (_, n) => timer(2 ** n * 500) })),
    ),
    takeWhile((s) => s.state !== "done", true),
  );
```

**React**

```tsx
const { data } = useQuery({
  queryKey: ["job", id],
  queryFn: () => getStatus(id),
  retry: 3,
  retryDelay: (n) => 2 ** n * 500,
  refetchInterval: (query) =>
    query.state.data?.state === "done" ? false : 2000,
});
```

**Vue.js**

```ts
const { data } = useQuery({
  queryKey: ["job", id],
  queryFn: () => getStatus(id),
  retry: 3,
  retryDelay: (n) => 2 ** n * 500,
  refetchInterval: (query) =>
    query.state.data?.state === "done" ? false : 2000,
});
```

Many RxJS pipelines are really "fetch, retry, poll, cancel". A query library covers that with options. Keep RxJS only for true event streams (WebSocket messages, complex UI gestures).

## 344: How do you pause polling when the tab is hidden?

**Angular**

```ts
const visible$ = fromEvent(document, "visibilitychange").pipe(
  startWith(null),
  map(() => !document.hidden),
);
status$ = visible$.pipe(
  switchMap((v) =>
    v ? timer(0, 5000).pipe(switchMap(() => this.api.status())) : EMPTY,
  ),
);
```

**React**

```tsx
// TanStack Query pauses refetchInterval in background tabs by default
useQuery({
  queryKey: ["status"],
  queryFn: getStatus,
  refetchInterval: 5000,
  refetchIntervalInBackground: false,
});
```

**Vue.js**

```ts
import { useDocumentVisibility, useIntervalFn } from "@vueuse/core";
const visibility = useDocumentVisibility();
const { pause, resume } = useIntervalFn(refresh, 5000);
watch(visibility, (v) => (v === "visible" ? resume() : pause()));
```

## 345: How do you translate undo and redo state?

**Angular**

```ts
export class Editor {
  private past = signal<Doc[]>([]);
  private future = signal<Doc[]>([]);
  doc = signal<Doc>(emptyDoc);
  apply(next: Doc) {
    this.past.update((p) => [...p, this.doc()]);
    this.future.set([]);
    this.doc.set(next);
  }
  undo() {
    const prev = this.past().at(-1);
    if (!prev) return;
    this.past.update((p) => p.slice(0, -1));
    this.future.update((f) => [this.doc(), ...f]);
    this.doc.set(prev);
  }
}
```

**React**

```tsx
type History = { past: Doc[]; present: Doc; future: Doc[] };
function reducer(
  h: History,
  a: { type: "apply"; doc: Doc } | { type: "undo" } | { type: "redo" },
): History {
  switch (a.type) {
    case "apply":
      return { past: [...h.past, h.present], present: a.doc, future: [] };
    case "undo":
      return h.past.length
        ? {
            past: h.past.slice(0, -1),
            present: h.past.at(-1)!,
            future: [h.present, ...h.future],
          }
        : h;
    case "redo":
      return h.future.length
        ? {
            past: [...h.past, h.present],
            present: h.future[0],
            future: h.future.slice(1),
          }
        : h;
  }
}
const [history, dispatch] = useReducer(reducer, {
  past: [],
  present: emptyDoc,
  future: [],
});
```

**Vue.js**

```ts
import { useRefHistory } from "@vueuse/core";
const doc = ref<Doc>(emptyDoc);
const { undo, redo, canUndo, canRedo } = useRefHistory(doc, {
  deep: true,
  capacity: 50,
});
```

`useReducer` is a good fit for state with many related transitions. Immutable updates make history cheap, since unchanged parts are shared.

## 346: How do you translate an offline-first data layer?

The idea stays the same: write to a local store first (IndexedDB), show it immediately, and sync to the server in the background with retries.

- **Angular:** often a service with signals backed by IndexedDB (Dexie) and the Angular service worker for asset caching.
- **React and Next.js:** TanStack Query with `networkMode: "offlineFirst"` and a persister (`@tanstack/query-async-storage-persister` or IndexedDB), or a sync engine (Dexie, RxDB, Replicache-style tools). Paused mutations resume when online.
- **Vue.js:** the same TanStack Vue Query setup, or Dexie's `liveQuery` wrapped with `useObservable`.

**React**

```tsx
const persister = createAsyncStoragePersister({ storage: idbStorage });
<PersistQueryClientProvider client={queryClient} persistOptions={{ persister }}>
  <App />
</PersistQueryClientProvider>;
```

For Next.js, offline mode applies to Client Components only. Server Components need the network, so offline screens must be client-rendered and cached by the service worker.

## 347: How do you translate real-time collaborative updates into query caches?

**Angular**

```ts
constructor() {
  this.socket.on("task:updated", (task: Task) =>
    this.tasks.update((l) => l.map((t) => (t.id === task.id ? task : t))),
  );
}
```

**React**

```tsx
const queryClient = useQueryClient();
useEffect(() => {
  const onUpdate = (task: Task) =>
    queryClient.setQueryData<Task[]>(["tasks"], (l) =>
      l?.map((t) => (t.id === task.id ? task : t)),
    );
  socket.on("task:updated", onUpdate);
  return () => {
    socket.off("task:updated", onUpdate);
  };
}, [queryClient]);
```

**Next.js**

```tsx
// If the list comes from a Server Component, refresh it on events
"use client";
useEffect(() => {
  const onUpdate = () => router.refresh();
  socket.on("task:updated", onUpdate);
  return () => {
    socket.off("task:updated", onUpdate);
  };
}, [router]);
```

**Vue.js**

```ts
socket.on("task:updated", (task: Task) =>
  queryClient.setQueryData<Task[]>(["tasks"], (l) =>
    l?.map((t) => (t.id === task.id ? task : t)),
  ),
);
```

For true multi-user editing (same document, same field), use a CRDT library like Yjs, which has bindings for all three frameworks.

## 348: Why can large forms feel slow after translating to React, and how do you fix it?

With controlled inputs, every keystroke calls `setState` in the form component, which re-renders the whole form with all its fields. Angular reactive forms update only the control that changed.

Fixes:

- Use React Hook Form, which uses uncontrolled inputs and refs, so typing does not re-render the form.
- Subscribe to specific fields with `useWatch` instead of `watch()` at the top.
- Split the form into memoized sections that receive only `control`.
- Let the React Compiler memoize field components.

```tsx
function PriceSummary({ control }: { control: Control<OrderForm> }) {
  const qty = useWatch({ control, name: "qty" }); // only this component re-renders on qty changes
  return <p>Total: {qty * 9.99}</p>;
}
```

Vue's `v-model` with a `reactive` form object updates only the bindings that read the changed field, so large forms usually stay fast without extra work.

## 349: How do you choose a form architecture when translating complex Angular forms?

Map by the type of Angular form:

- **Template-driven (`ngModel`)**: React `useState` plus native validation, or Vue `v-model`. Fine for small forms.
- **Reactive forms**: React Hook Form plus a schema (Zod/Valibot), or VeeValidate in Vue. These have field arrays, dirty/touched state, async validation and submit handling.
- **Signal forms**: the model-first approach maps well to TanStack Form (React and Vue) or a schema plus form library, since both keep data in a model and attach rules by path.
- **Forms posting to the server in Next.js**: Server Actions with `useActionState`, validating with the same schema on the server. Add React Hook Form on top only if you need rich client validation.

Keep the schema as the single source of truth for types and rules, and test validation with unit tests on the schema, not only through the UI.

## 350: How do you translate validators whose rules change at runtime?

**Angular**

```ts
constructor() {
  effect(() => {
    const vat = this.form.controls.vatNumber;
    if (this.isCompany()) vat.setValidators([Validators.required, vatPattern]);
    else vat.clearValidators();
    vat.updateValueAndValidity();
  });
}
```

**React**

```tsx
const schema = z.discriminatedUnion("type", [
  z.object({ type: z.literal("person"), name: z.string().min(1) }),
  z.object({
    type: z.literal("company"),
    name: z.string().min(1),
    vatNumber: z.string().regex(/^[A-Z]{2}\d+$/),
  }),
]);
useForm({ resolver: zodResolver(schema) });
```

**Vue.js**

```ts
const schema = computed(() =>
  toTypedSchema(
    z.object({
      name: z.string().min(1),
      vatNumber: isCompany.value
        ? z.string().regex(/^[A-Z]{2}\d+$/)
        : z.string().optional(),
    }),
  ),
);
useForm({ validationSchema: schema }); // VeeValidate accepts a reactive schema
```

Express conditional rules in the schema instead of adding and removing validators imperatively. It is easier to read and to test.

## 351: How do you keep forms accessible after translating?

Angular Material form fields wire up `aria-describedby`, `aria-invalid` and labels for you. When moving to plain inputs or a different library, you must do it yourself:

**React**

```tsx
function Field({
  label,
  error,
  ...props
}: { label: string; error?: string } & React.ComponentProps<"input">) {
  const id = useId();
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        aria-invalid={!!error}
        aria-describedby={error ? `${id}-err` : undefined}
        {...props}
      />
      {error && (
        <p id={`${id}-err`} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

**Vue.js**

```vue
<script setup lang="ts">
defineProps<{ label: string; error?: string }>();
const id = useId();
</script>

<template>
  <label :for="id">{{ label }}</label>
  <input
    :id="id"
    :aria-invalid="!!error"
    :aria-describedby="error ? `${id}-err` : undefined"
    v-bind="$attrs"
  />
  <p v-if="error" :id="`${id}-err`" role="alert">{{ error }}</p>
</template>
```

Also move focus to the first invalid field on submit (React Hook Form does this by default with `shouldFocusError`).

## 352: How do you translate a recursive tree component?

**Angular**

```ts
@Component({
  selector: "app-tree",
  template: `
    <ul>
      @for (node of nodes(); track node.id) {
        <li>
          {{ node.name }}
          @if (node.children?.length) {
            <app-tree [nodes]="node.children!" />
          }
        </li>
      }
    </ul>
  `,
})
export class Tree {
  nodes = input.required<TreeNode[]>();
}
```

**React**

```tsx
function Tree({ nodes }: { nodes: TreeNode[] }) {
  return (
    <ul>
      {nodes.map((node) => (
        <li key={node.id}>
          {node.name}
          {node.children?.length ? <Tree nodes={node.children} /> : null}
        </li>
      ))}
    </ul>
  );
}
```

**Vue.js**

```vue
<!-- Tree.vue: an SFC can refer to itself by its file name -->
<script setup lang="ts">
defineProps<{ nodes: TreeNode[] }>();
</script>

<template>
  <ul>
    <li v-for="node in nodes" :key="node.id">
      {{ node.name }}
      <Tree v-if="node.children?.length" :nodes="node.children" />
    </li>
  </ul>
</template>
```

For very large trees, flatten the visible nodes into a list and virtualize it instead of rendering nested components.

## 353: How do you translate a component that receives a template with typed context?

**Angular**

```ts
@Directive({ selector: "ng-template[appRow]" })
export class RowTemplate<T> {
  appRowOf = input.required<T[]>();
  static ngTemplateContextGuard<T>(
    _dir: RowTemplate<T>,
    ctx: unknown,
  ): ctx is { $implicit: T; index: number } {
    return true;
  }
}
// <ng-template appRow [appRowOf]="users" let-user let-i="index">{{ i }} {{ user.name }}</ng-template>
```

**React**

```tsx
type TableProps<T> = {
  rows: T[];
  children: (row: T, index: number) => React.ReactNode;
};
function Table<T>({ rows, children }: TableProps<T>) {
  return (
    <tbody>
      {rows.map((r, i) => (
        <tr key={i}>{children(r, i)}</tr>
      ))}
    </tbody>
  );
}
// <Table rows={users}>{(user, i) => <td>{i} {user.name}</td>}</Table>  -> user is typed
```

**Vue.js**

```vue
<script setup lang="ts" generic="T">
defineProps<{ rows: T[] }>();
defineSlots<{ default(props: { row: T; index: number }): any }>();
</script>

<template>
  <tr v-for="(row, index) in rows" :key="index">
    <slot :row="row" :index="index" />
  </tr>
</template>
```

Angular needs `ngTemplateContextGuard` to type template context. React render props and Vue `defineSlots` with `generic` give full type inference with less code.

## 354: How do you translate a polymorphic component (render as another element)?

**Angular**

```ts
// Usually done with an attribute selector so the user picks the element
@Component({
  selector: "a[appButton], button[appButton]",
  template: `<ng-content />`,
  host: { class: "btn" },
})
export class AppButton {}
```

**React**

```tsx
type ButtonProps<C extends React.ElementType> = { as?: C } & Omit<
  React.ComponentProps<C>,
  "as"
>;

function Button<C extends React.ElementType = "button">({
  as,
  className,
  ...rest
}: ButtonProps<C>) {
  const Comp = as ?? "button";
  return <Comp className={`btn ${className ?? ""}`} {...rest} />;
}
// <Button as="a" href="/home">Home</Button>   <Button as={Link} to="/home">Home</Button>
```

**Vue.js**

```vue
<script setup lang="ts">
withDefaults(defineProps<{ as?: string | object }>(), { as: "button" });
</script>

<template>
  <component :is="as" class="btn"><slot /></component>
</template>
```

An alternative popular in Radix and Reka UI is the `asChild` prop: the component merges its props onto its only child element.

## 355: How do directives compare with higher-order components and hooks?

Angular directives add behavior to an element without changing its type. React used to do this with higher-order components (HOCs): functions that take a component and return a wrapped one. Today hooks have mostly replaced HOCs, because they compose without wrapper layers and without prop name collisions.

**Angular**

```html
<input appAutofocus appTrim [(ngModel)]="name" />
```

**React**

```tsx
// HOC (older style)
const withAutofocus =
  <P,>(Comp: React.ComponentType<P>) =>
  (props: P) => {
    /* ... */ return <Comp {...props} />;
  };

// Hook (modern)
const ref = useAutofocus<HTMLInputElement>();
const trimmed = useTrimmedInput(name, setName);
<input ref={ref} {...trimmed} />;
```

**Vue.js**

```vue
<!-- Vue still has element directives for DOM behavior -->
<input v-autofocus v-model.trim="name" />
```

## 356: What is the headless component pattern, and how does it map from Angular?

A headless component provides behavior, state and accessibility, but no markup or styles. Angular CDK and Angular Aria are headless. In React, headless libraries expose hooks (`useCombobox` from Downshift, `useSelect` from React Aria) or unstyled components (Radix, Base UI). In Vue, Reka UI and Headless UI give unstyled components with slots.

**React**

```tsx
import { useCombobox } from "downshift";
function Combo({ items }: { items: string[] }) {
  const { getInputProps, getMenuProps, getItemProps, isOpen } = useCombobox({
    items,
  });
  return (
    <>
      <input {...getInputProps()} />
      <ul {...getMenuProps()}>
        {isOpen &&
          items.map((item, index) => (
            <li key={item} {...getItemProps({ item, index })}>
              {item}
            </li>
          ))}
      </ul>
    </>
  );
}
```

**Vue.js**

```vue
<ComboboxRoot v-model="value">
  <ComboboxInput />
  <ComboboxContent>
    <ComboboxItem v-for="item in items" :key="item" :value="item">{{ item }}</ComboboxItem>
  </ComboboxContent>
</ComboboxRoot>
```

If the Angular app built its own design system on the CDK, rebuild it on a headless library in the target, so you keep full control over markup and styles.

## 357: How do you design components that work both controlled and uncontrolled?

Angular's `model()` handles this: if the parent binds `[(value)]`, the parent owns it, otherwise the component keeps its own value. In React you implement it yourself. Vue's `defineModel` does it automatically.

**React**

```tsx
function useControllable<T>(
  value: T | undefined,
  defaultValue: T,
  onChange?: (v: T) => void,
) {
  const [inner, setInner] = useState(defaultValue);
  const isControlled = value !== undefined;
  const current = isControlled ? value : inner;
  const set = (next: T) => {
    if (!isControlled) setInner(next);
    onChange?.(next);
  };
  return [current, set] as const;
}

function Switch(props: {
  checked?: boolean;
  defaultChecked?: boolean;
  onCheckedChange?: (v: boolean) => void;
}) {
  const [checked, setChecked] = useControllable(
    props.checked,
    props.defaultChecked ?? false,
    props.onCheckedChange,
  );
  return (
    <button
      role="switch"
      aria-checked={checked}
      onClick={() => setChecked(!checked)}
    />
  );
}
```

**Vue.js**

```ts
// defineModel keeps local state when the parent does not use v-model
const checked = defineModel<boolean>({ default: false });
```

## 358: How do refs to child components and DOM nodes differ in React 19, Angular and Vue?

- **Angular:** `viewChild(ChildComponent)` gives the component instance with all public members. `viewChild("ref", { read: ElementRef })` gives the DOM element.
- **React 19:** `ref` is a regular prop for function components. Pass it to a DOM element to expose that element, or use `useImperativeHandle` to expose a small custom API. Ref callbacks can return a cleanup function.
- **Vue:** a template ref on a component gives the instance, but `<script setup>` components only expose what `defineExpose` lists. On an element it gives the DOM node.

**React**

```tsx
function Input({ ref, ...props }: React.ComponentProps<"input">) {
  return <input ref={ref} {...props} />; // no forwardRef needed in React 19
}

<div
  ref={(node) => {
    const ro = new ResizeObserver(() => {});
    if (node) ro.observe(node);
    return () => ro.disconnect(); // React 19 ref cleanup
  }}
/>;
```

Angular gives the most access by default, React and Vue the least, which pushes translated code toward explicit public APIs.

## 359: How do you translate route transitions using the View Transitions API?

**Angular**

```ts
provideRouter(routes, withViewTransitions());
```

**React**

```tsx
// React Router: opt in per link or navigation
<Link to="/photos/2" viewTransition>
  Next
</Link>
// React also has an experimental <ViewTransition> component in canary releases
```

**Next.js**

```ts
// next.config.ts (experimental): integrates React's <ViewTransition>
const nextConfig = { experimental: { viewTransition: true } };
```

**Vue.js**

```ts
router.beforeResolve(() => {
  if (!document.startViewTransition) return;
  return new Promise<void>((resolve) => {
    document.startViewTransition(async () => {
      resolve();
      await nextTick();
    });
  });
});
```

The CSS (`::view-transition-old`, `view-transition-name`) is the same everywhere, because it is a browser feature.

## 360: How do you translate list enter, leave and move animations?

**Angular**

```html
@for (item of items(); track item.id) {
<li animate.enter="slide-in" animate.leave="slide-out">{{ item.name }}</li>
}
```

**React**

```tsx
import { AnimatePresence, motion } from "motion/react";
<ul>
  <AnimatePresence>
    {items.map((item) => (
      <motion.li
        key={item.id}
        layout
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0 }}
      >
        {item.name}
      </motion.li>
    ))}
  </AnimatePresence>
</ul>;
```

**Vue.js**

```vue
<TransitionGroup name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.name }}</li>
</TransitionGroup>

<style>
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.3s;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}
.list-leave-active {
  position: absolute;
}
</style>
```

Vue's `<TransitionGroup>` handles move animations with the `-move` class. Angular's `animate.enter/leave` does not animate reordering, so you would add FLIP logic or a library. In React, `motion`'s `layout` prop does it.

## 361: How do you translate locale-prefixed routing with SSR?

**Angular**

```ts
// @angular/localize builds one app per locale, served from /en/, /de/ ...
// angular.json: "i18n": { "sourceLocale": "en", "locales": { "de": "src/locale/messages.de.xlf" } }
```

**React**

```tsx
// SPA: a :lang param at the top of the route tree
{ path: "/:lang", Component: LocaleLayout, children: appRoutes }
```

**Next.js**

```tsx
// app/[locale]/layout.tsx with next-intl; proxy.ts redirects "/" to the best locale
export function generateStaticParams() {
  return [{ locale: "en" }, { locale: "de" }];
}
export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  return (
    <html lang={locale}>
      <body>{children}</body>
    </html>
  );
}
```

**Vue.js**

```ts
// Nuxt: @nuxtjs/i18n with strategy "prefix_except_default"
export default defineNuxtConfig({
  modules: ["@nuxtjs/i18n"],
  i18n: { locales: ["en", "de"], defaultLocale: "en" },
});
```

Angular's per-locale builds have zero runtime cost but need one deployment per language. Runtime libraries in the targets use one build and load messages per request, which makes switching language without reload possible.

## 362: How do you handle right-to-left languages in each?

**Angular**

```ts
// CDK Directionality reads dir from <html> or a dir attribute
const dir = inject(Directionality).value; // "ltr" | "rtl"
```

**React**

```tsx
// Set dir on <html>; components read it from context or CSS
<html lang={locale} dir={locale === "ar" ? "rtl" : "ltr"}>
// Radix: <DirectionProvider dir="rtl">
```

**Vue.js**

```ts
watch(
  locale,
  (l) =>
    document.documentElement.setAttribute("dir", l === "ar" ? "rtl" : "ltr"),
  { immediate: true },
);
```

The biggest work is in CSS, not the framework. Replace `margin-left`/`padding-right` with logical properties (`margin-inline-start`, `padding-inline-end`), which flip automatically with `dir`.

## 363: How do you avoid a theme flash on first load with SSR?

The server does not know the user's saved theme (in `localStorage`) or system preference, so the first HTML may use the wrong theme.

**Angular**

```html
<!-- index.html: a tiny inline script before the app loads -->
<script>
  document.documentElement.classList.toggle(
    "dark",
    localStorage.theme === "dark" ||
      (!localStorage.theme &&
        matchMedia("(prefers-color-scheme: dark)").matches),
  );
</script>
```

**Next.js**

```tsx
// Option 1: next-themes injects the same kind of script
// Option 2: store the theme in a cookie and read it on the server
export default async function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const theme = (await cookies()).get("theme")?.value ?? "light";
  return (
    <html className={theme}>
      <body>{children}</body>
    </html>
  );
}
```

**Vue.js**

```ts
// Nuxt: @nuxtjs/color-mode handles the script and the cookie
```

For a Vite SPA (React or Vue), the inline script in `index.html` is enough, exactly like in Angular.

## 364: How do you port a shared Angular design system to React and Vue?

1. **Extract tokens** (colors, spacing, typography) into CSS custom properties or a token package (Style Dictionary). These are framework-free.
2. **Keep CSS framework-free** where possible (plain CSS classes or Tailwind), so markup in any framework can reuse it.
3. **Rebuild behavior** on headless primitives (Radix/React Aria for React, Reka UI for Vue), matching the Angular component APIs where it makes sense.
4. **Keep the same component names and props** (`<Button variant="primary">`) to make page translation mechanical.
5. **Document in Storybook** for each framework, and use visual regression tests to compare with the Angular stories.

An alternative is to build the design system as Web Components (Lit or Stencil) once and wrap them for each framework, which is how several large companies support Angular, React and Vue at the same time.

## 365: How do you use Storybook to compare old and new components?

Storybook supports Angular, React, Next.js and Vue. Write the same stories (same names and args) in both:

**Angular**

```ts
const meta: Meta<Badge> = { component: Badge };
export default meta;
export const Warning: StoryObj<Badge> = {
  args: { label: "Low stock", tone: "warning" },
};
```

**React**

```tsx
const meta: Meta<typeof Badge> = { component: Badge };
export default meta;
export const Warning: StoryObj<typeof Badge> = {
  args: { label: "Low stock", tone: "warning" },
};
```

**Vue.js**

```ts
const meta: Meta<typeof Badge> = { component: Badge };
export default meta;
export const Warning: StoryObj<typeof Badge> = {
  args: { label: "Low stock", tone: "warning" },
};
```

Storybook Composition can show both Storybooks in one UI, so designers can review the old and new versions side by side.

## 366: How do you use visual regression testing during migration?

Take screenshots of the Angular pages or stories as the baseline, then render the same pages in the new app and compare. Differences show missing styles, spacing changes or wrong states.

```ts
// Playwright, run against both apps with different base URLs
test("product page looks the same", async ({ page }) => {
  await page.goto("/products/42");
  await expect(page).toHaveScreenshot("product-42.png", {
    maxDiffPixelRatio: 0.01,
  });
});
```

Use the Angular app to create the baseline images (`--update-snapshots`), then run the same test against the new app. Fix fonts, data and animations (stub dates, disable transitions) so only real differences show up.

## 367: How do you prove the translated app behaves the same?

- **End-to-end tests** with Playwright or Cypress, written against roles and text, not framework-specific selectors. Run the same suite against both apps.
- **Contract tests** for the API layer: both apps must send the same requests. MSW handlers or recorded HAR files help.
- **Visual regression** for layout.
- **Analytics comparison**: conversion and error rates during a gradual rollout.

```ts
// playwright.config.ts: two projects, one suite
projects: [
  { name: "angular", use: { baseURL: "http://localhost:4200" } },
  { name: "next", use: { baseURL: "http://localhost:3000" } },
],
```

Use `getByRole` and `getByLabel` locators. They work on both apps if the accessibility tree is the same, which is also a good check that accessibility did not regress.

## 368: How do you test that both apps call the API the same way?

Record the requests the Angular app makes for a user flow, then assert the new app makes equivalent requests.

```ts
test("checkout sends the same order payload", async ({ page }) => {
  const requests: unknown[] = [];
  page.on("request", (req) => {
    if (req.url().includes("/api/orders") && req.method() === "POST")
      requests.push(req.postDataJSON());
  });
  await runCheckoutFlow(page);
  expect(requests).toEqual([expectedOrderPayload]);
});
```

In Next.js, some calls move from the browser to the server (Server Components, Server Actions). Then browser-level checks are not enough. Test the server data layer directly, or check the backend logs in a staging environment.

## 369: How do you test async UI behavior consistently across frameworks?

Use Testing Library's async queries (`findBy...`, `waitFor`) instead of framework-specific helpers like `fixture.whenStable()`, `act()` or `flushPromises()`. The test reads the same in each framework.

**Angular**

```ts
await render(UserList, { providers: [provideHttpClient()] }); // @testing-library/angular
expect(await screen.findByText("Ana")).toBeTruthy();
```

**React**

```tsx
render(<UserList />, { wrapper: QueryWrapper });
expect(await screen.findByText("Ana")).toBeInTheDocument();
```

**Vue.js**

```ts
render(UserList, { global: { plugins: [[VueQueryPlugin, { queryClient }]] } });
expect(await screen.findByText("Ana")).toBeInTheDocument();
```

With MSW for the network, these tests can be ported almost line by line, which lowers the risk of the migration.

## 370: How do you test Next.js Server Components and Server Actions?

- **Server Actions** are async functions. Unit test them directly by calling them with a `FormData`, after mocking `next/headers` (cookies) and `next/cache` (revalidation).
- **Sync Server Components** can be rendered with React Testing Library like any component.
- **Async Server Components** are not well supported by unit test renderers yet. Test them with end-to-end tests (Playwright), or test the data functions they call and keep the component thin.

```ts
vi.mock("next/cache", () => ({ updateTag: vi.fn(), revalidatePath: vi.fn() }));
vi.mock("next/headers", () => ({
  cookies: async () => ({ get: () => ({ value: "session-token" }) }),
}));

it("rejects an empty title", async () => {
  const fd = new FormData();
  fd.set("title", "");
  expect(await createTodo(null, fd)).toEqual({ error: "Title is required" });
});
```

## 371: Which profiling tools do you use in each framework?

- **Angular:** Angular DevTools profiler (change detection cycles per component), signal graph view, and the Chrome Performance panel with Angular custom tracks.
- **React and Next.js:** React DevTools Profiler (which components rendered and why), and React Performance Tracks in the Chrome Performance panel (React 19.2+) showing scheduler priorities and component work. Next.js adds build output and the bundle analyzer.
- **Vue.js:** Vue DevTools performance timeline (component render and patch times) and `app.config.performance = true` to add marks to the browser profiler.

When comparing before and after, use the same scenario and the browser's Performance panel, since that measures what users feel (long tasks, INP), regardless of framework.

## 372: How do memory leaks differ between Angular, React and Vue?

The leaks are the same kind (listeners, timers, subscriptions that outlive the component), but where they hide differs:

- **Angular:** RxJS subscriptions without `takeUntilDestroyed`, and root services that hold references to destroyed components.
- **React:** effects without cleanup, closures in long-lived listeners holding old state, and module-level caches that grow forever.
- **Vue:** `watch` or listeners created asynchronously (after an `await` in setup) are not bound to the component and are not stopped on unmount.

**Vue.js**

```ts
// Leak: a watcher created in a later callback is not bound to the component
setTimeout(() => watch(source, handler), 0);

// Fix: create watchers synchronously in setup, or stop them yourself
const stop = watch(source, handler);
onUnmounted(stop); // register lifecycle hooks before any await in setup
```

**React**

```tsx
useEffect(() => {
  const id = setInterval(poll, 1000);
  return () => clearInterval(id); // forgetting this leaks per mount (twice in Strict Mode)
}, []);
```

Use Chrome's heap snapshots and "Detached elements" panel to find leaked DOM nodes.

## 373: How do you virtualize lists with dynamic row heights?

**Angular**

```html
<!-- CDK supports fixed item size; for dynamic heights use the experimental autosize strategy or a library -->
<cdk-virtual-scroll-viewport autosize> ... </cdk-virtual-scroll-viewport>
```

**React**

```tsx
const v = useVirtualizer({
  count: rows.length,
  getScrollElement: () => parentRef.current,
  estimateSize: () => 60,
  measureElement: (el) => el.getBoundingClientRect().height,
});
// each item: <div key={item.key} data-index={item.index} ref={v.measureElement} style={{ transform: `translateY(${item.start}px)` }}>
```

**Vue.js**

```ts
// @tanstack/vue-virtual with measureElement, or vue-virtual-scroller's DynamicScroller
```

Measuring rows after render is required for dynamic heights. Keep the estimate close to the average to avoid jumping scrollbars.

## 374: How do you move heavy work to a Web Worker with a nice API?

Comlink turns a worker into an async object, so the code looks like calling a service. It works the same in all frameworks.

```ts
// report.worker.ts
import * as Comlink from "comlink";
const api = { buildReport: (rows: Row[]) => heavyAggregate(rows) };
Comlink.expose(api);
export type ReportApi = typeof api;
```

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class ReportWorker {
  private api = Comlink.wrap<ReportApi>(
    new Worker(new URL("./report.worker", import.meta.url), { type: "module" }),
  );
  build = (rows: Row[]) => this.api.buildReport(rows);
}
```

**React**

```tsx
const reportApi = Comlink.wrap<ReportApi>(
  new Worker(new URL("./report.worker.ts", import.meta.url), {
    type: "module",
  }),
);
const { data } = useQuery({
  queryKey: ["report", rowsVersion],
  queryFn: () => reportApi.buildReport(rows),
});
```

**Vue.js**

```ts
const reportApi = Comlink.wrap<ReportApi>(
  new Worker(new URL("./report.worker.ts", import.meta.url), {
    type: "module",
  }),
);
const report = computedAsync(() => reportApi.buildReport(rows.value)); // VueUse
```

In Next.js, create the worker only in a Client Component, inside an effect or lazily, since `Worker` does not exist on the server.

## 375: How do you break up long tasks to keep INP low?

Long synchronous work (more than about 50ms) blocks input. The fix is the same in every framework: split the work and yield to the browser.

```ts
async function processAll(items: Item[]) {
  for (let i = 0; i < items.length; i++) {
    process(items[i]);
    if (i % 200 === 0) {
      await (globalThis.scheduler?.yield?.() ??
        new Promise((r) => setTimeout(r)));
    }
  }
}
```

React adds `startTransition`: state updates inside it are rendered at low priority and can be interrupted by typing or clicks. Angular and Vue do not have interruptible rendering, so splitting work and virtualizing big lists matter more there.

**React**

```tsx
const [isPending, startTransition] = useTransition();
const onTab = (t: string) => startTransition(() => setTab(t)); // heavy tab render won't block clicks
```

## 376: How do framework runtime sizes compare, and does it matter?

Rough minified and compressed sizes for a "hello world":

- **Angular** (zoneless, standalone): around 30-40 kB for core, more with router, forms and HTTP. Zone.js added about 13 kB before zoneless became default.
- **React + ReactDOM:** around 55-60 kB.
- **Next.js:** framework client runtime plus React is larger (often 90-110 kB on first load), but Server Components ship zero JS for non-interactive parts.
- **Vue:** around 25-35 kB with router, and Vapor Mode reduces the runtime further.

These numbers change between versions, so measure your own build. In real apps, your code and libraries usually outweigh the framework. The bigger wins come from code splitting, fewer dependencies, and (in Next.js) keeping components on the server.

## 377: When can you ship zero JavaScript for parts of a translated app?

- **Next.js:** Server Components send HTML and no component JS. A marketing page made only of Server Components needs just the small React runtime for navigation.
- **Angular:** every component that is rendered on the server also hydrates. `@defer` with hydrate triggers postpones JS but does not remove it.
- **Nuxt:** server components (`.server.vue`) and `<NuxtIsland>` render on the server only.
- **Astro** (outside these four) can host React or Vue components as islands, with zero JS by default.

So for content-heavy Angular apps (docs, blogs, catalogs), moving to Next.js Server Components or Nuxt islands can cut JavaScript a lot.

## 378: How do you protect SEO when migrating URLs?

- Keep every public URL the same if you can. Next.js file routes and Vue Router can match any Angular path.
- If a URL must change, add a permanent redirect (301/308) from the old one. In Next.js, use `redirects()` in `next.config.ts`. For many redirects, a lookup in `proxy.ts`.
- Keep titles, meta descriptions, canonical tags, `hreflang` and structured data the same or better.
- Generate `sitemap.xml` and `robots.txt` (Next.js: `app/sitemap.ts` and `app/robots.ts`).
- Compare server HTML before and after: an Angular SPA without SSR rendered content in the browser, while Next.js renders it in HTML, which is usually an SEO improvement.

```ts
// app/sitemap.ts
export default async function sitemap() {
  const products = await getAllProducts();
  return products.map((p) => ({
    url: `https://shop.example.com/products/${p.slug}`,
    lastModified: p.updatedAt,
  }));
}
```

## 379: How do you migrate route by route behind one domain?

Put a reverse proxy (or the new app itself) in front of both apps and move paths one at a time.

**Next.js**

```ts
// next.config.ts: Next.js serves migrated routes and forwards the rest to the Angular app
const nextConfig = {
  async rewrites() {
    return {
      fallback: [
        { source: "/:path*", destination: "https://legacy.example.com/:path*" },
      ],
    };
  },
};
```

**React / Vue.js**

```nginx
# nginx in front of two static apps
location /orders/ { try_files $uri /orders/index.html; root /srv/new-app; }
location / { try_files $uri /index.html; root /srv/angular-app; }
```

`fallback` rewrites in Next.js only apply when no Next.js page matches, so each new page automatically takes over its path. Share login cookies across both apps (same domain) so users don't notice the switch. Navigation between apps is a full page load, so migrate tightly linked routes together.

## 380: How do you keep analytics consistent across the old and new apps?

- Keep the same event names and properties. Put them in a shared, typed module (`trackEvent("checkout_started", {...})`) used by both apps.
- Fire page views on the same moment (after route change completes) in both.
- Tag events with an `app_version: "angular" | "next"` property, so you can compare funnels during rollout.
- In Next.js, load the analytics script with `next/script` (`strategy="afterInteractive"`), and track client-side navigations with a component that watches `usePathname`.

```tsx
import Script from "next/script";
<Script src="https://analytics.example.com/a.js" strategy="afterInteractive" />;
```

## 381: How do you roll out a translated app safely?

- **Feature flags per route or feature:** route a percentage of users to the new app (at the proxy or CDN) and keep an instant switch back.
- **Internal users first:** staff, then beta users, then a small share of everyone.
- **Compare metrics:** error rate, Core Web Vitals, conversion and support tickets for both versions.
- **Keep the old app deployable** until the new one has been at 100% for a while.
- **Sticky assignment:** keep a user on the same version (cookie) so they don't bounce between apps.

```ts
// proxy.ts in Next.js: send 10% of users to the new checkout
export function proxy(req: NextRequest) {
  let bucket = req.cookies.get("ab")?.value;
  if (!bucket) bucket = Math.random() < 0.1 ? "new" : "old";
  const res =
    bucket === "new"
      ? NextResponse.next()
      : NextResponse.rewrite(
          new URL(req.nextUrl.pathname, "https://legacy.example.com"),
        );
  res.cookies.set("ab", bucket, { maxAge: 60 * 60 * 24 * 30 });
  return res;
}
```

## 382: How do you help an Angular team learn React, Next.js or Vue?

- Start with a concept map (like the tables in this file) so people translate ideas, not just syntax.
- Do a pilot feature with pair programming between people who know each framework.
- Write a short internal guide: folder structure, state rules (when local, context, store, query), data fetching rules, testing rules.
- Turn on strict lint rules early (`react-hooks`, `eslint-plugin-vue`), since they teach the framework's rules while coding.
- Review the first PRs closely for common mistakes: effects used to derive state, mutated state, missing cleanup, and lost Vue reactivity.

Angular developers usually find Vue's mental model closest (templates, `computed`, `watch`, `provide`/`inject`). React needs the biggest shift: "the component function runs on every render".

## 383: How do you enforce architecture boundaries after translating?

Angular's NgModules and Nx tags often enforced "features cannot import other features". In the new app, use lint rules:

```js
// eslint.config.js with eslint-plugin-boundaries
export default [
  {
    settings: {
      "boundaries/elements": [
        { type: "app", pattern: "src/app/*" },
        { type: "feature", pattern: "src/features/*" },
        { type: "shared", pattern: "src/shared/*" },
      ],
    },
    rules: {
      "boundaries/element-types": [
        "error",
        {
          default: "disallow",
          rules: [
            { from: "app", allow: ["feature", "shared"] },
            { from: "feature", allow: ["shared"] },
            { from: "shared", allow: ["shared"] },
          ],
        },
      ],
    },
  },
];
```

In an Nx monorepo, `@nx/enforce-module-boundaries` with project tags works the same for Angular, React, Next.js and Vue projects. In Next.js, also enforce `server-only` imports so server code cannot end up in client bundles.

## 384: How does type checking of templates compare?

- **Angular:** templates are type-checked by the Angular compiler. With `strictTemplates`, bindings, inputs, outputs and `$event` types are checked during `ng build`.
- **React and Next.js:** JSX is TypeScript, so `tsc` checks everything. No extra tool is needed. Next.js runs type checking during `next build`.
- **Vue:** templates are checked by `vue-tsc` (Vue Language Tools). Vite does not type check during dev or build, so add `vue-tsc --noEmit` to CI.

```json
// package.json (Vue)
{
  "scripts": {
    "type-check": "vue-tsc --build",
    "build": "run-p type-check build-only"
  }
}
```

A typical surprise when moving from Angular to Vite-based apps: the build succeeds with type errors. Make type checking a separate required CI step.

## 385: How do you get type-safe routing like Angular's typed routes?

Angular routes are not strongly typed. Route params are strings read from `paramMap`, and `withComponentInputBinding` only helps partly. The targets have better options:

**React**

```tsx
// TanStack Router: params and search are typed from the route definition
const productRoute = createRoute({
  getParentRoute: () => rootRoute,
  path: "/products/$id",
});
const { id } = productRoute.useParams(); // typed
<Link to="/products/$id" params={{ id: "42" }}>
  Product
</Link>; // checked at compile time
```

**Next.js**

```ts
// next.config.ts: typedRoutes checks <Link href> strings against app/ routes
const nextConfig = { typedRoutes: true };
// PageProps<"/products/[id]"> types the params of a page
```

**Vue.js**

```ts
// Vue Router 4.4+ with unplugin-vue-router (file-based) generates typed route names and params
router.push({ name: "/products/[id]", params: { id: "42" } });
```

## 386: How do you share a type-safe API client between the old and new apps?

Generate the client from the backend's OpenAPI spec into a framework-free package. Both apps then use the same functions and types.

```ts
// with openapi-typescript + openapi-fetch
import createClient from "openapi-fetch";
import type { paths } from "./schema"; // generated

export const api = createClient<paths>({ baseUrl: "/api" });
const { data, error } = await api.GET("/products/{id}", {
  params: { path: { id: "42" } },
});
```

**Angular**

```ts
product = resource({
  params: () => this.id(),
  loader: ({ params }) =>
    api.GET("/products/{id}", { params: { path: { id: params } } }),
});
```

**React**

```tsx
// openapi-react-query wraps the same client for TanStack Query
const { data } = $api.useQuery("get", "/products/{id}", {
  params: { path: { id } },
});
```

**Vue.js**

```ts
const { data } = useQuery({
  queryKey: ["product", id],
  queryFn: () =>
    api.GET("/products/{id}", { params: { path: { id: id.value } } }),
});
```

If the backend is also TypeScript (and you are moving to Next.js), Server Actions or tRPC give end-to-end types without code generation.

## 387: How do the Angular, React and Vue compilers differ?

- **Angular (Ivy):** compiles each component's template ahead of time into create/update instruction functions. Decorators become static fields (`ɵcmp`). The compiler also does type checking and tree-shaking of unused features.
- **React:** JSX is compiled to `jsx()` function calls, which is a simple syntax transform. The optional React Compiler (a Babel/SWC plugin) is a separate step that adds automatic memoization.
- **Vue:** the SFC compiler turns templates into optimized render functions with static hoisting, patch flags and block trees, so diffing skips static content. `<script setup>` macros (`defineProps`, `defineModel`) are compiled away. Vapor Mode compiles templates to direct DOM operations.

The practical result: Angular and Vue understand the template and optimize it. Plain React gives the runtime a description of the UI and relies on reconciliation, which is why the React Compiler exists.

## 388: How does Vue reactivity compare with Angular signals internally?

Both track dependencies automatically while a computation runs, and both are push-pull: writes mark dependents dirty, and values are recomputed lazily on read.

Differences:

- Angular signals are functions with explicit `set`/`update`. Objects inside a signal are not tracked, so you replace them immutably.
- Vue `ref` and `reactive` use JavaScript Proxies, so nested properties and array methods (`push`, `splice`) are tracked automatically. That is why mutation works in Vue.
- Vue 3.6 rewrote the reactivity core based on the alien-signals approach for better speed and memory, getting closer to signal libraries internally.

```ts
// Angular: immutable updates
items.update((l) => [...l, x]);
// Vue: mutation is tracked
items.value.push(x);
// Vue opt-out of deep tracking, which behaves like a signal
const big = shallowRef(hugeArray);
big.value = [...big.value, x]; // only replacing .value triggers
```

## 389: Should you use signals in React to make the translation easier?

Libraries like `@preact/signals-react` exist, and there is a TC39 proposal for native signals. But for most teams, the answer is no.

- React's model (state, render, effects) is what the docs, libraries and hiring pool expect.
- Signals libraries for React patch React internals or need a Babel transform, which can break with React updates and the React Compiler.
- Translating to signals in React gives code that looks like Angular but behaves differently around rendering and concurrency.

If you want signal-style fine-grained reactivity, Vue (or Solid) is a more natural target than React. In React, use stores with selectors (Zustand, Jotai atoms) for shared state, which give similar targeted updates.

## 390: When should you use shallowRef or markRaw in translated Vue code?

Vue makes objects deeply reactive by default. For large or foreign objects, that costs memory and can break them.

- `shallowRef`: large immutable data (API responses with thousands of rows) that you replace, not mutate. This matches how Angular signals treat objects.
- `markRaw`: third-party instances (map objects, chart instances, class instances from SDKs) that must not be wrapped in a Proxy.

```ts
const rows = shallowRef<Row[]>([]);
rows.value = await fetchRows(); // fast, no deep proxies

const map = shallowRef<maplibregl.Map>();
onMounted(
  () => (map.value = markRaw(new maplibregl.Map({ container: el.value! }))),
);
```

A common bug after translating: putting a chart or map instance in `ref()` causes errors because the library compares objects by identity and gets a Proxy instead.

## 391: Why is using effects to derive state an anti-pattern in all three?

Effects for derived values cause an extra render pass, can show inconsistent UI for a moment, and can create loops. All three frameworks have a better tool.

**Angular**

```ts
// Bad
effect(() => this.fullName.set(`${this.first()} ${this.last()}`));
// Good
fullName = computed(() => `${this.first()} ${this.last()}`);
```

**React**

```tsx
// Bad
const [fullName, setFullName] = useState("");
useEffect(() => setFullName(`${first} ${last}`), [first, last]);
// Good
const fullName = `${first} ${last}`;
```

**Vue.js**

```ts
// Bad
watchEffect(() => (fullName.value = `${first.value} ${last.value}`));
// Good
const fullName = computed(() => `${first.value} ${last.value}`);
```

Effects are for syncing with things outside the framework: the DOM, network, storage, timers, third-party widgets.

## 392: What causes infinite loops in effects, and how do they differ?

**Angular**

```ts
// Writing to a signal you also read in the same effect can loop
effect(() => this.count.set(this.count() + 1)); // keeps re-running
```

**React**

```tsx
// Setting state in an effect that depends on that state
useEffect(() => setItems([...items, x]), [items]); // loops
// An object dependency that is recreated each render also loops
useEffect(() => setData(transform(obj)), [obj]);
```

**Vue.js**

```ts
watch(items, () => items.value.push(x), { deep: true }); // the mutation triggers the watcher again
```

Fixes: compute instead of storing, depend on primitives, use the updater form (`setItems(l => ...)`) without listing the state as a dependency, or use `untracked` (Angular) to read without subscribing.

## 393: In what order do parent and child effects run?

- **React:** effects run children first, then parents (bottom-up), after the DOM commit. Cleanups run before the next effects. So a parent's effect can rely on children having done their effect setup.
- **Vue:** `onMounted` runs children first, then the parent. `watch` callbacks by default run before the component updates (`flush: "pre"`).
- **Angular:** component `effect`s run during change detection, top-down through the view tree, before the view refreshes. `afterRenderEffect` and `afterNextRender` run after the whole app has rendered.

**React**

```tsx
function Parent() {
  useEffect(() => console.log("parent"));
  return <Child />;
}
function Child() {
  useEffect(() => console.log("child"));
  return null;
}
// logs: child, parent
```

Code that relied on Angular's top-down order (a parent setting up a service in `ngOnInit` before children use it) must be restructured in React: create the shared thing during render (in state or context), not in an effect.

## 394: What do React error boundaries not catch, and how do you handle those errors?

Error boundaries catch errors during rendering, in lifecycle methods and in constructors of the tree below. They do not catch errors in event handlers, in async code (`setTimeout`, promise callbacks), in server-side rendering, or in the boundary itself.

**React**

```tsx
function SaveButton() {
  const [error, setError] = useState<Error | null>(null);
  if (error) throw error; // rethrow during render so the nearest boundary shows it

  return (
    <button
      onClick={async () => {
        try {
          await save();
        } catch (e) {
          setError(e as Error);
        }
      }}
    >
      Save
    </button>
  );
}
```

React 19 Actions help: errors thrown inside a transition or form action are sent to the nearest error boundary automatically.

**Angular**

```ts
// The global ErrorHandler receives errors from event handlers and from async tasks it knows about
```

**Vue.js**

```ts
// app.config.errorHandler catches errors in handlers, watchers and lifecycle hooks, including async ones returned as promises
```

## 395: How do you handle unhandled promise rejections globally?

**Angular**

```ts
// provideBrowserGlobalErrorListeners() (Angular 20+) sends window errors and unhandled rejections to ErrorHandler
providers: [
  provideBrowserGlobalErrorListeners(),
  { provide: ErrorHandler, useClass: ReportingErrorHandler },
];
```

**React**

```tsx
window.addEventListener("unhandledrejection", (e) => report(e.reason));
window.addEventListener("error", (e) => report(e.error));
```

**Next.js**

```ts
// instrumentation-client.ts runs before the app in the browser
window.addEventListener("unhandledrejection", (e) => report(e.reason));
// server side: onRequestError in instrumentation.ts
```

**Vue.js**

```ts
app.config.errorHandler = (err) => report(err);
window.addEventListener("unhandledrejection", (e) => report(e.reason));
```

## 396: Scenario: how would you translate a dashboard with several independent widgets?

In Angular, a dashboard often has one container that injects several services and passes data down, with a spinner per widget.

**Angular**

```ts
@Component({
  template: `
    <app-sales-widget [data]="sales.value()" [loading]="sales.isLoading()" />
    <app-users-widget [data]="users.value()" [loading]="users.isLoading()" />
  `,
})
export class Dashboard {
  sales = httpResource<Sales>(() => "/api/sales");
  users = httpResource<UserStats>(() => "/api/users/stats");
}
```

**React**

```tsx
// Each widget fetches its own data; an error in one does not break the others
function Dashboard() {
  return (
    <div className="grid">
      <ErrorBoundary fallback={<WidgetError />}>
        <SalesWidget />
      </ErrorBoundary>
      <ErrorBoundary fallback={<WidgetError />}>
        <UsersWidget />
      </ErrorBoundary>
    </div>
  );
}
function SalesWidget() {
  const { data, isPending } = useQuery({
    queryKey: ["sales"],
    queryFn: getSales,
  });
  return isPending ? <Skeleton /> : <SalesChart data={data} />;
}
```

**Next.js**

```tsx
// Server Components stream each widget when its data is ready
export default function Dashboard() {
  return (
    <div className="grid">
      <Suspense fallback={<Skeleton />}>
        <SalesWidget />
      </Suspense>
      <Suspense fallback={<Skeleton />}>
        <UsersWidget />
      </Suspense>
    </div>
  );
}
async function SalesWidget() {
  const sales = await getSales();
  return <SalesChart data={sales} />; // SalesChart is a Client Component if it is interactive
}
```

**Vue.js**

```vue
<template>
  <div class="grid">
    <SalesWidget />
    <UsersWidget />
  </div>
</template>
<!-- each widget uses useQuery and onErrorCaptured to show its own error -->
```

## 397: Scenario: how would you translate an authenticated admin area?

Angular pieces: a login page, an `AuthService` with the current user, an `authInterceptor`, a `canActivate`/`canMatch` guard on the admin routes, and role checks in templates.

- **React (SPA):** a Zustand or context auth store; a fetch wrapper adding the token; a protected layout route (loader that redirects); a `<RequireRole>` component. The API must enforce roles.
- **Next.js:** sessions in httpOnly cookies; a quick cookie check in `proxy.ts` for redirects; a `verifySession()` data access helper called in every admin page, layout and Server Action; role checks in Server Components so non-admin UI never renders; Auth.js or Better Auth to handle providers.
- **Vue.js:** a Pinia auth store; an `ofetch` instance with an `onRequest` hook; `router.beforeEach` with `meta.requiresAuth` and `meta.roles`; a `hasRole()` helper used with `v-if`.

The Angular `canMatch` guard (which stops lazy code from even loading) maps to Next.js server checks most naturally, since admin code then never reaches non-admin browsers.

## 398: Scenario: how would you translate a multi-step wizard?

**Angular**

```ts
// a component-level WizardState service shared by step components, steps as child routes
@Injectable()
export class WizardState {
  data = signal<Partial<Order>>({});
  patch(p: Partial<Order>) {
    this.data.update((d) => ({ ...d, ...p }));
  }
}
```

**React**

```tsx
function Wizard() {
  const [step, setStep] = useState(0);
  const form = useForm<Order>({
    resolver: zodResolver(orderSchema),
    mode: "onTouched",
  });
  const steps = [<Shipping key="s" />, <Payment key="p" />, <Review key="r" />];
  const next = async () => {
    const ok = await form.trigger(stepFields[step]); // validate only this step
    if (ok) setStep((s) => s + 1);
  };
  return (
    <FormProvider {...form}>
      {steps[step]}
      <button onClick={next}>Next</button>
    </FormProvider>
  );
}
```

**Next.js**

```tsx
// Option: each step is a route (/checkout/shipping, /checkout/payment) and data is kept
// in a client store (Zustand with sessionStorage) or saved per step with a Server Action.
```

**Vue.js**

```ts
// Wizard.vue: one useForm, steps as child components that use useField
const { validateField } = useForm({
  validationSchema: toTypedSchema(orderSchema),
});
provide(WizardKey, { step, next });
```

Decide early if each step needs its own URL (back button, deep links). If yes, use routes plus a store. If not, a single component with step state is simpler.

## 399: Scenario: how would you translate a data grid with server-side paging, sorting and filters?

Keep the grid state in the URL, so links and the back button work, and derive the query from it.

**Angular**

```ts
export class Orders {
  page = input(1, { transform: numberAttribute }); // from ?page=
  sort = input("date");
  orders = httpResource<Paged<Order>>(() => ({
    url: "/api/orders",
    params: { page: this.page(), sort: this.sort() },
  }));
}
```

**React**

```tsx
function Orders() {
  const [params, setParams] = useSearchParams();
  const page = Number(params.get("page") ?? 1);
  const sort = params.get("sort") ?? "date";
  const { data, isPlaceholderData } = useQuery({
    queryKey: ["orders", { page, sort }],
    queryFn: () => getOrders({ page, sort }),
    placeholderData: keepPreviousData, // keep old rows while the next page loads
  });
}
```

**Next.js**

```tsx
export default async function Orders({
  searchParams,
}: {
  searchParams: Promise<{ page?: string; sort?: string }>;
}) {
  const { page = "1", sort = "date" } = await searchParams;
  const orders = await getOrders({ page: Number(page), sort });
  return <OrdersTable orders={orders} />; // Client Component updates the URL with router.replace
}
```

**Vue.js**

```ts
const page = useRouteQuery("page", "1", { transform: Number });
const sort = useRouteQuery("sort", "date");
const { data } = useQuery({
  queryKey: ["orders", { page, sort }],
  queryFn: () => getOrders({ page: page.value, sort: sort.value }),
  placeholderData: keepPreviousData,
});
```

## 400: Scenario: how would you translate a real-time chat?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class ChatService {
  private socket = webSocket<Message>("wss://chat.example.com");
  messages = signal<Message[]>([]);
  constructor() {
    this.socket
      .pipe(takeUntilDestroyed())
      .subscribe((m) => this.messages.update((l) => [...l, m]));
  }
  send(text: string) {
    this.socket.next({ text } as Message);
  }
}
```

**React**

```tsx
// A module-level connection with a tiny store, so one socket serves the whole app
const useChat = create<{ messages: Message[]; add: (m: Message) => void }>(
  (set) => ({
    messages: [],
    add: (m) => set((s) => ({ messages: [...s.messages, m] })),
  }),
);
const socket = new WebSocket("wss://chat.example.com");
socket.onmessage = (e) => useChat.getState().add(JSON.parse(e.data));
export const send = (text: string) => socket.send(JSON.stringify({ text }));
```

**Next.js**

```tsx
// Next.js Route Handlers are not meant for long-lived WebSocket servers. Use a separate
// socket service (or a hosted one) and connect from a Client Component as in React.
// Load history in the Server Component and pass it as initial messages.
```

**Vue.js**

```ts
export const useChat = defineStore("chat", () => {
  const { data, send } = useWebSocket("wss://chat.example.com", {
    autoReconnect: true,
  });
  const messages = ref<Message[]>([]);
  watch(data, (raw) => raw && messages.value.push(JSON.parse(raw)));
  return { messages, send: (text: string) => send(JSON.stringify({ text })) };
});
```

For long chat histories, virtualize the message list and keep the scroll pinned to the bottom only when the user is already at the bottom.

## 401: Scenario: how would you translate a shopping cart that survives reloads?

**Angular**

```ts
@Injectable({ providedIn: "root" })
export class Cart {
  items = signal<CartItem[]>(JSON.parse(localStorage.getItem("cart") ?? "[]"));
  total = computed(() => this.items().reduce((s, i) => s + i.price * i.qty, 0));
  constructor() {
    effect(() => localStorage.setItem("cart", JSON.stringify(this.items())));
  }
}
```

**React**

```tsx
export const useCart = create(
  persist<{ items: CartItem[]; add: (i: CartItem) => void }>(
    (set) => ({
      items: [],
      add: (i) => set((s) => ({ items: [...s.items, i] })),
    }),
    { name: "cart" },
  ),
);
const total = useCart((s) =>
  s.items.reduce((sum, i) => sum + i.price * i.qty, 0),
);
```

**Next.js**

```ts
// Store the cart on the server (cookie with cart id + DB). Server Components can render
// the cart count in the header without client JS, and nothing breaks across devices.
"use server";
export async function addToCart(productId: string) {
  const cartId = (await cookies()).get("cartId")?.value ?? (await createCart());
  await db.cartItem.upsert({/* ... */});
  updateTag(`cart-${cartId}`);
}
```

**Vue.js**

```ts
export const useCart = defineStore("cart", () => {
  const items = useLocalStorage<CartItem[]>("cart", []);
  const total = computed(() =>
    items.value.reduce((s, i) => s + i.price * i.qty, 0),
  );
  return { items, total };
});
```

With SSR, a `localStorage` cart is empty on the server, so the header count can flicker. A server-side cart (or rendering the count only on the client) avoids hydration mismatches.

## 402: Scenario: how would you translate an infinite feed that also needs SEO?

Render the first page on the server for crawlers and fast first paint, then load more pages on the client.

**Angular**

```ts
// SSR renders page 1 via httpResource; the transfer cache avoids refetch; loadMore appends on scroll
```

**React**

```tsx
// Vite SPA cannot do this for SEO without a framework; consider Next.js or React Router framework mode.
```

**Next.js**

```tsx
// app/feed/page.tsx
export default async function Feed() {
  const firstPage = await getPosts({ page: 1 });
  return <FeedList initialPosts={firstPage} />; // Client Component with useInfiniteQuery
}

// FeedList.tsx
("use client");
export function FeedList({ initialPosts }: { initialPosts: Post[] }) {
  const { data, fetchNextPage } = useInfiniteQuery({
    queryKey: ["feed"],
    queryFn: ({ pageParam }) =>
      fetch(`/api/posts?page=${pageParam}`).then((r) => r.json()),
    initialPageParam: 1,
    initialData: { pages: [initialPosts], pageParams: [1] },
    getNextPageParam: (_last, all) => all.length + 1,
  });
}
```

**Vue.js**

```ts
// Nuxt: const { data: firstPage } = await useFetch("/api/posts?page=1"); then load more on the client
```

Also render real pagination links (`?page=2`) so crawlers can reach older posts, since they do not scroll.

## 403: Scenario: how would you translate a file upload with a progress bar?

Angular's `HttpClient` reports upload progress. `fetch` does not, so use `XMLHttpRequest` (or axios) in the targets.

**Angular**

```ts
upload(file: File) {
  const body = new FormData();
  body.append("file", file);
  this.http.post("/api/upload", body, { reportProgress: true, observe: "events" }).subscribe((e) => {
    if (e.type === HttpEventType.UploadProgress && e.total) this.progress.set(Math.round((100 * e.loaded) / e.total));
  });
}
```

**React**

```tsx
function uploadWithProgress(file: File, onProgress: (p: number) => void) {
  return new Promise<void>((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.upload.onprogress = (e) =>
      e.lengthComputable && onProgress(Math.round((100 * e.loaded) / e.total));
    xhr.onload = () =>
      xhr.status < 400 ? resolve() : reject(new Error(String(xhr.status)));
    xhr.onerror = () => reject(new Error("Network error"));
    const body = new FormData();
    body.append("file", file);
    xhr.open("POST", "/api/upload");
    xhr.send(body);
  });
}
// const [progress, setProgress] = useState(0); await uploadWithProgress(file, setProgress);
```

**Next.js**

```ts
// For large files, upload straight from the browser to object storage with a presigned URL
// created in a Server Action, instead of streaming the file through the Next.js server.
"use server";
export async function getUploadUrl(name: string) {
  return createPresignedPutUrl(`uploads/${crypto.randomUUID()}-${name}`);
}
```

**Vue.js**

```ts
const progress = ref(0);
await uploadWithProgress(file, (p) => (progress.value = p)); // same helper
```

## 404: Scenario: how would you translate lazy-loaded translations per feature?

**Angular**

```ts
// Transloco: scoped translations load with the lazy route
{ path: "billing", loadChildren: () => import("./billing.routes"), providers: [provideTranslocoScope("billing")] }
```

**React**

```tsx
// i18next with a backend plugin loads namespaces on demand
const { t } = useTranslation("billing"); // suspends until billing.json for the language is loaded
```

**Next.js**

```tsx
// next-intl: load only the namespaces a page needs on the server; pass a subset to client components
import { NextIntlClientProvider } from "next-intl";
import { getMessages } from "next-intl/server";
const messages = await getMessages();
<NextIntlClientProvider messages={{ billing: messages.billing }}>
  {children}
</NextIntlClientProvider>;
```

**Vue.js**

```ts
// vue-i18n: add messages when the route loads
router.beforeEach(async (to) => {
  if (to.meta.i18n && !i18n.global.availableLocales.includes(locale)) {
    const messages = await import(`./locales/${to.meta.i18n}/${locale}.json`);
    i18n.global.mergeLocaleMessage(locale, messages.default);
  }
});
```

## 405: Scenario: how would you translate a complex permission system?

Move permission logic into one framework-free function, then wrap it for each UI.

```ts
// shared/permissions.ts
export type Action = "read" | "update" | "delete";
export function can(
  user: User,
  action: Action,
  resource: { ownerId: string; type: string },
) {
  if (user.roles.includes("admin")) return true;
  if (action === "read") return true;
  return resource.ownerId === user.id;
}
```

**Angular**

```ts
// a structural directive: <button *appCan="'delete'; on: project">Delete</button>
```

**React**

```tsx
function Can({
  action,
  on,
  children,
}: {
  action: Action;
  on: Resource;
  children: React.ReactNode;
}) {
  const user = useAuth((s) => s.user);
  return user && can(user, action, on) ? children : null;
}
```

**Next.js**

```tsx
// Use the same can() on the server, in pages and in Server Actions
if (!can(session.user, "delete", project)) throw new Error("Forbidden");
```

**Vue.js**

```ts
const auth = useAuthStore();
const canDo = (action: Action, on: Resource) =>
  !!auth.user && can(auth.user, action, on);
// <button v-if="canDo('delete', project)">Delete</button>
```

Libraries like CASL provide `@casl/angular`, `@casl/react` and `@casl/vue`, which makes this kind of migration very direct.

## 406: Scenario: how would you translate a plugin system that loads components at runtime?

**Angular**

```ts
// Load a remote module and render its component
const { Widget } = await loadRemoteModule({
  remoteEntry: plugin.url,
  exposedModule: "./Widget",
});
this.vcr.createComponent(Widget);
```

**React**

```tsx
const registry = new Map<
  string,
  React.LazyExoticComponent<React.ComponentType<PluginProps>>
>();
function getPlugin(url: string) {
  if (!registry.has(url))
    registry.set(
      url,
      lazy(() => import(/* @vite-ignore */ url)),
    );
  return registry.get(url)!;
}
function PluginSlot({ url, ...props }: { url: string } & PluginProps) {
  const Plugin = getPlugin(url);
  return (
    <Suspense fallback={<Spinner />}>
      <Plugin {...props} />
    </Suspense>
  );
}
```

**Vue.js**

```ts
const Plugin = defineAsyncComponent(
  () => import(/* @vite-ignore */ plugin.url),
);
// <component :is="Plugin" v-bind="props" />
```

Plugins must use the same framework version (or be Web Components). Never load plugin code from untrusted sources: it runs with full access to your app. Keep the `lazy` component cached outside render, otherwise React remounts it on every render.

## 407: Scenario: how would you move an SEO-focused Angular SSR site to Next.js?

1. **Inventory routes and render modes** from `app.routes.ts` and `app.routes.server.ts`. Map prerendered routes to static pages (`generateStaticParams`), server routes to dynamic pages, and client routes to Client Components.
2. **Move resolvers and `ngOnInit` data loading** into async Server Components.
3. **Translate `Title`/`Meta` service calls** to `metadata` and `generateMetadata`.
4. **Replace `TransferState`** with server-rendered props; delete client refetching.
5. **Move `server.ts` logic** (redirects, headers) to `next.config.ts` and `proxy.ts`.
6. **Keep URLs, canonical tags, sitemap and structured data** identical, and check with Search Console.
7. **Compare HTML output** of key pages before and after (title, headings, links, JSON-LD), and compare Core Web Vitals.

The main gain is less JavaScript, since content components become Server Components and never hydrate.

## 408: Scenario: how would you translate an app built heavily on NgRx?

1. **Classify the store:** most slices are usually cached server data (entities loaded by effects). Others are true client state (UI, wizard progress, preferences).
2. **Replace server-data slices** with TanStack Query (React/Vue) or Server Components (Next.js). Effects, actions and reducers for "load X / load X success / load X failure" disappear.
3. **Move client-state slices** to Redux Toolkit (closest to NgRx, same DevTools), Zustand, or Pinia.
4. **Keep selectors' logic** as plain functions so they can be unit-tested and reused.
5. **Port effects with real side effects** (analytics, sockets, navigation) to listener middleware (RTK `createListenerMiddleware`), store subscriptions, or Pinia `$onAction`.

Migrating slice by slice is possible by running both stores and syncing a few values, but it is usually easier to migrate a whole feature (store slice plus its screens) at once.

## 409: Scenario: how would you convert an internal Angular component library for React and Vue teams?

Options:

- **Rewrite per framework:** best developer experience and SSR support, but two codebases. Share tokens, CSS and headless logic in framework-free packages.
- **Web Components (Lit or Stencil):** one implementation consumed everywhere. Stencil can generate React and Vue wrapper packages. SSR and form integration take extra work.
- **Angular Elements:** reuse the Angular code, but each element bundles Angular runtime parts, so it is heavier.
- **Mitosis or similar:** write components once in a JSX-like format and compile to Angular, React and Vue. Works best for simple components.

For a long-lived design system shared by many teams, Web Components plus generated wrappers is a common choice. For a library mostly used by one product being migrated, rewriting in the target framework is usually simpler.

## 410: How do you package a component library for React and Vue compared with ng-packagr?

**Angular**

```bash
ng generate library ui   # builds with ng-packagr into Angular Package Format (APF)
ng build ui
```

**React**

```ts
// vite.config.ts in library mode (or tsup / tsdown)
export default defineConfig({
  plugins: [react(), dts()],
  build: {
    lib: { entry: "src/index.ts", formats: ["es"] },
    rollupOptions: { external: ["react", "react-dom", "react/jsx-runtime"] },
  },
});
```

**Next.js**

```ts
// Consumer side: if the library ships untranspiled TS or uses "use client", mark it
const nextConfig = { transpilePackages: ["@acme/ui"] };
// Library side: add "use client" to the top of interactive component files (bundlers may need a plugin to keep it)
```

**Vue.js**

```ts
export default defineConfig({
  plugins: [vue(), dts()],
  build: {
    lib: { entry: "src/index.ts", formats: ["es"] },
    rollupOptions: { external: ["vue"] },
  },
});
```

Always mark the framework as a `peerDependency` and as external, or apps end up with two copies of React or Vue, which breaks hooks and reactivity.

## 411: Why must React and Vue be peer dependencies in shared libraries?

If a library bundles or depends on its own copy of React, the app has two React instances. Hooks then throw "Invalid hook call" because the hook dispatcher belongs to the other copy. Context from the app is not visible to the library. Vue has similar issues: two Vue copies have separate reactivity systems and `inject` cannot see the app's `provide`.

Angular has the same issue with `@angular/core` (two copies break DI), which is why Angular libraries list it as a peer dependency too.

```json
{
  "peerDependencies": {
    "react": "^18.3.0 || ^19.0.0",
    "react-dom": "^18.3.0 || ^19.0.0"
  },
  "devDependencies": { "react": "^19.2.0", "react-dom": "^19.2.0" }
}
```

In monorepos, check with `npm ls react` (or `pnpm why react`) that only one version is installed.

## 412: How do you choose between React, Next.js and Vue as the target for an Angular app?

Consider:

- **App type:** internal SPA behind login → React (Vite) or Vue. Public site with SEO and content → Next.js or Nuxt.
- **Team background:** Angular developers usually find Vue's templates and reactivity the easiest step. React has the largest ecosystem and hiring pool.
- **Backend:** a separate API makes any target fine. If you want to merge some backend logic into the frontend project, Next.js (or Nuxt) fits.
- **Ecosystem needs:** check that your key libraries (grids, charts, editors, design system) exist for the target.
- **Hosting:** static hosting works for React/Vue SPAs. Next.js needs Node or a platform that supports it, or static export with limits.
- **Long-term structure:** Angular teams who liked opinionated structure may prefer Next.js or Nuxt conventions over assembling a React stack.

There is no single right answer. Pick based on the app's rendering needs first, then the team.

## 413: What do you gain and lose moving from an Angular SPA to the Next.js App Router?

Gains:

- Server rendering and streaming by default, better SEO and first load.
- Server Components that ship no JS and can read data directly.
- File-based routing with layouts, loading and error states built in.
- Server Actions for mutations without writing API endpoints.
- Image, font and script optimizations.

Losses or costs:

- A server to run (or platform lock-in), unless you use static export.
- A new mental model: server vs client code, serialization rules, caching rules.
- Some client-only libraries need wrappers (`"use client"`, `dynamic(..., { ssr: false })`).
- Debugging spans two environments (browser and server).

If the app does not benefit from server rendering, these costs may outweigh the gains, and Vite + React is a simpler target.

## 414: What are the limits of Next.js static export?

With `output: "export"`, `next build` writes static HTML, CSS and JS to `out/`, which any static host can serve, like an Angular SPA build. But features that need a server are not available:

- Server Actions, cookies/headers in Server Components, `proxy.ts`, rewrites, redirects and headers in `next.config.ts`.
- Dynamic routes without `generateStaticParams` (unknown IDs at build time).
- ISR and on-demand revalidation.
- Default image optimization (use `unoptimized: true` or a custom loader).

Server Components still work, but they run at build time only. For an Angular SPA with dynamic IDs (`/orders/:id`), static export needs client-side data loading for those pages, which makes it close to a Vite React app anyway.

## 415: When should a Vue migration use Nuxt instead of plain Vue with Vite?

Use **Nuxt** when you need SSR or prerendering (SEO, fast first paint), file-based routing with layouts, server API routes in the same project, or conventions similar to Angular CLI projects (auto imports, modules). Nuxt is to Vue what Next.js is to React, and it maps well from Angular SSR apps.

Use **plain Vue + Vite** when the Angular app is a client-only SPA, the backend is separate, and you want the smallest and simplest setup. You add Vue Router and Pinia yourself, which is little work.

Nuxt also has route rules for hybrid rendering, which match Angular's per-route render modes closely.

## 416: How does deployment differ between the four?

- **Angular SPA, React (Vite), Vue (Vite):** static files on any static host or CDN, with a fallback to `index.html`. Angular SSR needs a Node server (or a platform adapter).
- **Next.js:** `next start` on Node, `output: "standalone"` in Docker, or a platform with Next.js support (Vercel, Netlify, Cloudflare via OpenNext, AWS Amplify). Next.js 16 adds a stable adapters API so platforms can integrate officially. Caching, ISR and image optimization need storage that works with multiple instances (a custom cache handler for self-hosting at scale).
- **Nuxt:** Nitro builds for many targets (Node, serverless, edge, static) with presets.

When moving from an Angular SPA on S3/CloudFront to Next.js, the hosting change is often the biggest operational task. Plan it early.

## 417: How do you write a Dockerfile for each?

**Angular**

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npx ng build

FROM nginx:alpine
COPY --from=build /app/dist/my-app/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
```

**React**

```dockerfile
# same two stages; copy /app/dist to nginx
```

**Next.js**

```dockerfile
# next.config.ts: output: "standalone"
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/.next/standalone ./
COPY --from=build /app/.next/static ./.next/static
COPY --from=build /app/public ./public
EXPOSE 3000
CMD ["node", "server.js"]
```

**Vue.js**

```dockerfile
# same as React: build, then serve /app/dist with nginx
```

## 418: How do you handle runtime configuration that changes per environment without rebuilding?

Angular `environment.ts`, Vite `import.meta.env` and Next.js `NEXT_PUBLIC_*` are all inlined at build time. To deploy one build to several environments:

**Angular**

```ts
// load /config.json at startup
provideAppInitializer(async () =>
  inject(ConfigStore).set(await (await fetch("/config.json")).json()),
);
```

**React**

```tsx
const config = await fetch("/config.json").then((r) => r.json());
createRoot(root).render(
  <ConfigContext value={config}>
    <App />
  </ConfigContext>,
);
```

**Next.js**

```tsx
// Server code reads process.env at runtime (in dynamic rendering).
// Pass values to the client from a Server Component:
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const config = { apiUrl: process.env.API_URL! }; // read on the server per request
  return (
    <html>
      <body>
        <ConfigProvider config={config}>{children}</ConfigProvider>
      </body>
    </html>
  );
}
```

**Vue.js**

```ts
const config = await fetch("/config.json").then((r) => r.json());
createApp(App).provide(ConfigKey, config).mount("#app");
// Nuxt: runtimeConfig, overridable with NUXT_PUBLIC_* env vars at runtime
```

In Next.js, reading `process.env` inside a statically prerendered page bakes the value in at build time. Make the reading component dynamic (for example, `await connection()`) if the value must come from runtime.

## 419: What changes in the CI pipeline after migrating?

- **Install and cache:** same package manager, but cache `.next/cache` for Next.js builds.
- **Lint:** add `eslint-plugin-react-hooks` or `eslint-plugin-vue` rules; remove `@angular-eslint`.
- **Type check:** Vite projects need a separate `tsc --noEmit` or `vue-tsc` step. Next.js type checks during build.
- **Unit tests:** Vitest for all targets.
- **E2E tests:** keep the same Playwright suite.
- **Bundle budgets:** add `size-limit` or Lighthouse CI, since there is no built-in `budgets` like Angular.
- **Preview deployments:** useful for reviewing translated screens side by side with the Angular app.

```yaml
- run: npm ci
- run: npm run lint
- run: npx tsc --noEmit # or vue-tsc --build
- run: npx vitest run
- run: npm run build
- run: npx playwright test
```

## 420: How do you set security headers in each?

**Angular**

```ts
// SSR: in server.ts (Express) with helmet; SPA: on the web server or CDN
app.use(helmet());
```

**React**

```nginx
# static hosting: set headers on the server or CDN
add_header X-Content-Type-Options nosniff;
add_header Referrer-Policy strict-origin-when-cross-origin;
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
```

**Next.js**

```ts
// next.config.ts
const nextConfig = {
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          {
            key: "Strict-Transport-Security",
            value: "max-age=63072000; includeSubDomains",
          },
        ],
      },
    ];
  },
  poweredByHeader: false,
};
```

**Vue.js**

```ts
// Nuxt: routeRules: { "/**": { headers: { "X-Content-Type-Options": "nosniff" } } }, or the nuxt-security module
```

## 421: How do you rate limit Server Actions and Route Handlers?

Angular apps rely on the backend for rate limiting. When Next.js takes over backend work through Server Actions and Route Handlers, you must add it there. There is no built-in limiter, so use a shared store (Redis) because the app may run on several instances.

```ts
"use server";
import { headers } from "next/headers";
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";

const limiter = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, "1 m"),
});

export async function sendMessage(formData: FormData) {
  const ip =
    (await headers()).get("x-forwarded-for")?.split(",")[0] ?? "unknown";
  const { success } = await limiter.limit(`contact:${ip}`);
  if (!success) return { error: "Too many requests, try again later" };
  // ...
}
```

Rate limit by user ID when the user is logged in, and by IP otherwise. Also rate limit at the CDN or WAF level for heavy abuse.

## 422: How do you translate a file download from an API?

**Angular**

```ts
download() {
  this.http.get("/api/report.csv", { responseType: "blob" }).subscribe((blob) => {
    const url = URL.createObjectURL(blob);
    const a = Object.assign(document.createElement("a"), { href: url, download: "report.csv" });
    a.click();
    URL.revokeObjectURL(url);
  });
}
```

**React**

```tsx
async function download() {
  const blob = await fetch("/api/report.csv").then((r) => r.blob());
  const url = URL.createObjectURL(blob);
  const a = Object.assign(document.createElement("a"), {
    href: url,
    download: "report.csv",
  });
  a.click();
  URL.revokeObjectURL(url);
}
```

**Next.js**

```ts
// app/api/report/route.ts: stream the file from the server; the link is a plain <a href download>
export async function GET() {
  const csv = await buildCsv();
  return new Response(csv, {
    headers: {
      "Content-Type": "text/csv",
      "Content-Disposition": 'attachment; filename="report.csv"',
    },
  });
}
```

**Vue.js**

Same `fetch` + blob code as React.

If the endpoint can set `Content-Disposition`, a plain `<a href="/api/report.csv">` is simplest in all frameworks and handles large files without loading them into memory.

## 423: How do you load third-party scripts like chat widgets or tag managers?

**Angular**

```ts
// added to index.html, or loaded in a service with a <script> element
const s = Object.assign(document.createElement("script"), {
  src: "https://widget.example.com/w.js",
  async: true,
});
document.body.append(s);
```

**React**

```tsx
useEffect(() => {
  const s = Object.assign(document.createElement("script"), {
    src: "https://widget.example.com/w.js",
    async: true,
  });
  document.body.append(s);
  return () => s.remove();
}, []);
// React 19 also dedupes <script async src="..."> rendered anywhere in the tree
```

**Next.js**

```tsx
import Script from "next/script";
<Script
  src="https://widget.example.com/w.js"
  strategy="lazyOnload"
  onLoad={() => window.Widget?.init()}
/>;
```

**Vue.js**

```ts
import { useScriptTag } from "@vueuse/core";
useScriptTag("https://widget.example.com/w.js", () => window.Widget?.init());
// Nuxt: useScript() from @nuxt/scripts
```

`next/script` strategies (`beforeInteractive`, `afterInteractive`, `lazyOnload`, `worker`) give control over loading order that you had to build by hand in Angular.

## 424: How do you translate a D3 chart component?

Let D3 own the SVG inside one element, and let the framework own the data. Re-run the D3 code when data changes.

**Angular**

```ts
export class BarChart {
  data = input.required<number[]>();
  svg = viewChild.required<ElementRef<SVGSVGElement>>("svg");
  constructor() {
    afterRenderEffect(() => draw(this.svg().nativeElement, this.data()));
  }
}
```

**React**

```tsx
function BarChart({ data }: { data: number[] }) {
  const ref = useRef<SVGSVGElement>(null);
  useEffect(() => {
    draw(ref.current!, data);
  }, [data]);
  return <svg ref={ref} width={400} height={200} />;
}
```

**Vue.js**

```vue
<script setup lang="ts">
const props = defineProps<{ data: number[] }>();
const svg = useTemplateRef<SVGSVGElement>("svg");
watch(
  () => props.data,
  (d) => draw(svg.value!, d),
  { flush: "post" },
);
onMounted(() => draw(svg.value!, props.data));
</script>

<template><svg ref="svg" width="400" height="200" /></template>
```

```ts
// draw.ts: shared, framework-free
import * as d3 from "d3";
export function draw(el: SVGSVGElement, data: number[]) {
  const svg = d3.select(el);
  svg
    .selectAll("rect")
    .data(data)
    .join("rect")
    .attr("x", (_, i) => i * 22)
    .attr("width", 20)
    .attr("y", (d) => 200 - d)
    .attr("height", (d) => d);
}
```

An alternative is to use D3 only for math (scales, shapes) and render the SVG elements with JSX or a Vue template.

## 425: How do you translate a canvas animation loop?

**Angular**

```ts
export class Particles {
  canvas = viewChild.required<ElementRef<HTMLCanvasElement>>("c");
  constructor() {
    let frame = 0;
    afterNextRender(() => {
      const ctx = this.canvas().nativeElement.getContext("2d")!;
      const loop = () => {
        drawFrame(ctx);
        frame = requestAnimationFrame(loop);
      };
      loop();
    });
    inject(DestroyRef).onDestroy(() => cancelAnimationFrame(frame));
  }
}
```

**React**

```tsx
function Particles() {
  const ref = useRef<HTMLCanvasElement>(null);
  useEffect(() => {
    const ctx = ref.current!.getContext("2d")!;
    let frame = 0;
    const loop = () => {
      drawFrame(ctx);
      frame = requestAnimationFrame(loop);
    };
    loop();
    return () => cancelAnimationFrame(frame);
  }, []);
  return <canvas ref={ref} width={600} height={400} />;
}
```

**Vue.js**

```ts
import { useRafFn } from "@vueuse/core";
const c = useTemplateRef<HTMLCanvasElement>("c");
useRafFn(() => c.value && drawFrame(c.value.getContext("2d")!));
```

Keep per-frame values (positions, velocities) in plain variables or refs, not in React state or Vue reactive objects. Updating framework state 60 times per second causes needless re-renders. For 3D, React Three Fiber and TresJS give declarative wrappers around Three.js.

## 426: How do you check accessibility after the migration?

- **Automated:** run axe on key pages in Playwright (`@axe-core/playwright`) for both apps and compare violations. Add `eslint-plugin-jsx-a11y` (React) or `eslint-plugin-vuejs-accessibility` (Vue).
- **Keyboard:** tab through every flow. Check focus order, visible focus, Escape to close dialogs, focus returning to the trigger.
- **Screen readers:** test key flows with NVDA/VoiceOver. Angular Material and CDK did a lot automatically (live announcer, focus traps, ARIA on form fields), and these are the first things lost in a translation.
- **Route changes:** SPAs must move focus or announce new pages. Next.js announces route changes with a built-in route announcer, while React Router and Vue Router apps need it added.

```ts
import AxeBuilder from "@axe-core/playwright";
test("checkout has no a11y violations", async ({ page }) => {
  await page.goto("/checkout");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

## 427: How do you measure whether the translated app is actually faster?

- **Lab:** Lighthouse or WebPageTest on the same pages, same device profile and network, several runs, median values.
- **Field:** real-user Core Web Vitals (LCP, INP, CLS) from the `web-vitals` library or CrUX, split by app version during rollout.
- **Bundle:** total JS on first load per route, and how much is framework vs app code.
- **Interactions:** use the Performance panel to record the same interaction (filter a big table, open a dialog) and compare long tasks.
- **Server:** for Next.js, time to first byte and server CPU, since work moved from the browser to the server.

Decide the success metrics before the migration starts. "Faster" should mean specific numbers on specific pages, not a general feeling.

## 428: What are common anti-patterns when translating Angular code literally?

- **A "service" for everything:** wrapping every piece of logic in context providers in React. Plain functions and modules are fine.
- **Effects for derived values:** `useEffect` + `setState` instead of computing during render.
- **One giant context** holding all app state, causing re-renders everywhere.
- **Classes and `this`:** porting component classes as React class components or Vue Options API.
- **Keeping RxJS everywhere** in React or Vue, with manual subscriptions in every component.
- **Imperative DOM work** with refs where a state change and re-render would do.
- **Everything `"use client"`** in Next.js, which turns it into an SPA with extra overhead.
- **Translating `ngOnInit` to `useEffect(fn, [])`** for data loading, instead of a query library or Server Components.

Translate the intent of the code, not its structure.

## 429: How do you handle fixes and features while both apps are live?

- **Freeze or limit new features in the Angular app** for areas already migrated or being migrated.
- **For bug fixes in shared logic**, move the logic into a shared framework-free package first, then fix it once.
- **Track ownership per route:** a table of which app serves each route and who owns it.
- **Same backend contract:** version API changes so both apps keep working.
- **Shared E2E tests** that run against whichever app serves a route, so behavior stays aligned.
- **Set an end date** for the Angular app. Long coexistence periods are the most expensive part of incremental migrations.

## 430: How do the rules of hooks compare with Angular's injection context and Vue's setup rules?

All three have "call this only in the right place" rules:

- **Angular:** `inject()`, `effect()`, `toSignal()` and other DI-based functions must run in an injection context (constructor, field initializer, factory, or `runInInjectionContext`). Otherwise you get `NG0203`.
- **React:** hooks must be called at the top level of a component or custom hook, in the same order every render. No hooks in loops, conditions, or callbacks. (`use()` is the exception and can be called conditionally.)
- **Vue:** `inject()`, lifecycle hooks and composables that use them must be called synchronously in `setup()`, before any `await`. Otherwise they are not linked to the component.

**Angular**

```ts
onClick() {
  const api = inject(Api); // error: not in an injection context
}
```

**React**

```tsx
if (isAdmin) {
  const data = useQuery(/* ... */); // breaks hook order
}
```

**Vue.js**

```ts
const data = await load();
onMounted(() => {}); // warning: lifecycle hook registered after await, not linked to the instance
```

The fix in all three: get dependencies first, at the top, then use them in callbacks.

## 431: Why must React render functions be pure, and how does that differ from Angular constructors?

An Angular constructor runs once per instance, so side effects there (starting a timer, logging, subscribing) run once. A React component function can run many times: on every update, twice in Strict Mode, and React may start a render and throw it away in concurrent mode. Side effects during render then run an unknown number of times.

**Angular**

```ts
constructor() {
  analytics.track("widget_shown"); // runs once per instance
}
```

**React**

```tsx
function Widget() {
  analytics.track("widget_shown"); // wrong: runs on every render
  useEffect(() => analytics.track("widget_shown"), []); // right: runs after mount
  return <div />;
}
```

**Vue.js**

```ts
// <script setup> runs once per instance, like a constructor, so this is fine
analytics.track("widget_shown");
```

The React Compiler also assumes purity. Impure render code may behave differently once it is enabled.

## 432: How do Angular outputs, React callbacks and Vue emits differ from DOM events?

None of the component-level events bubble like DOM events.

- **Angular `output()`:** only the direct parent that binds `(event)` receives it. No bubbling.
- **React callback props:** just function calls. No bubbling, no event object unless you pass one.
- **Vue `emit`:** only the direct parent receives it.

Native DOM events inside the component still bubble as usual. In React, they bubble through the React tree, which can differ from the DOM tree (see portals in the next question). If the Angular app used `dispatchEvent(new CustomEvent(..., { bubbles: true }))` from a host element to reach far ancestors, use context or a store in the target instead, since there is no host element to dispatch from.

## 433: How do events from portals bubble differently in React and Vue?

In React, an event inside a portal bubbles to the React parent components, even though the DOM node lives elsewhere (like `document.body`). In Vue (`<Teleport>`) and Angular (CDK portals), native events bubble through the real DOM tree only.

**React**

```tsx
<div onClick={() => console.log("parent got it")}>
  {createPortal(<button>Inside modal</button>, document.body)}
</div>
// clicking the button logs "parent got it"
```

**Vue.js**

```vue
<div @click="log('parent got it')">
  <Teleport to="body"><button>Inside modal</button></Teleport>
</div>
<!-- the div does not receive the click: the button is not its DOM descendant -->
```

**Angular**

```ts
// Same as Vue: overlay content attached to the body does not bubble to the opener's elements
```

This matters when translating "click outside to close" logic or parent click handlers. In React, a click inside a modal can trigger handlers on the component that opened it, so stop propagation in the portal root if needed.

## 434: How does component identity decide whether state is kept?

- **React:** a component keeps its state while the same component type renders at the same position in the tree with the same key. Switching `{a ? <Form /> : <Form />}` keeps the state (same type, same position). A different key resets it.
- **Vue:** similar rules with `:key`. The same component in the same `v-if`/`v-else` branch position can be reused, unless keys differ.
- **Angular:** `@if` blocks create and destroy views. Two branches with the same component are two different views, so state resets when switching. `@for` keeps views by `track`.

**React**

```tsx
// Both branches are <ProfileForm> at the same position: state is shared by mistake
{
  isAdmin ? <ProfileForm user={admin} /> : <ProfileForm user={guest} />;
}
// Fix: give each a key
{
  isAdmin ? (
    <ProfileForm key="admin" user={admin} />
  ) : (
    <ProfileForm key="guest" user={guest} />
  );
}
```

A translated `@if/@else` with the same component in both branches may suddenly keep state in React or Vue. Add keys where the Angular behavior (reset) is expected.

## 435: How do you handle per-request state on the server in Next.js compared with Angular SSR?

Angular SSR creates a new application (and a new root injector) for every request, so root services are per request by default. Next.js does not: module-level variables are shared by every request on that server process. A module-level store that held "the current user" in a translated service would leak data between users.

```ts
// Dangerous in Next.js server code: shared between all requests
let currentUser: User | null = null;

// Safe: per-request memoization with React's cache()
import { cache } from "react";
export const getCurrentUser = cache(async () => {
  const session = (await cookies()).get("session")?.value;
  return session ? findUserBySession(session) : null;
});
```

`cache()` memoizes per server request, so several Server Components can call `getCurrentUser()` and only one lookup happens. Client stores (Zustand) created at module level have the same risk when rendered on the server. Create them per request inside a provider instead.

## 436: How do you avoid cross-request state pollution in Nuxt?

Nuxt also runs one server process for many requests. Module-level `ref`s in composables are shared between users on the server.

```ts
// Dangerous in Nuxt (and any Vue SSR): shared across requests
const user = ref<User | null>(null);
export const useUser = () => user;

// Safe: Nuxt's useState is per request on the server and hydrated on the client
export const useUser = () => useState<User | null>("user", () => null);
```

Pinia is safe because Nuxt creates a new Pinia instance per request. The rule is the same as in Next.js: keep request data in request-scoped containers (Pinia, `useState`, React `cache()`), never in module variables.

## 437: When should you use Server Actions, Route Handlers, or a separate API in Next.js?

- **Server Actions:** mutations triggered from your own UI (forms, buttons). Typed, progressive enhancement, integrated with revalidation. Not ideal for public APIs or for fetching data in Client Components.
- **Route Handlers:** HTTP endpoints for others: webhooks, mobile apps, third-party integrations, file downloads, streaming responses, and `GET` data for Client Components.
- **Separate backend API:** when the backend already exists, is shared by many clients, or is written in another language. Next.js then calls it from Server Components and Actions.

In an Angular-to-Next.js migration with an existing backend, keep the backend. Call it from Server Components for reads and from Server Actions for writes, where the action forwards the user's session. Move logic into Next.js only when it is truly frontend-specific.

## 438: How do you run work after the response is sent in Next.js?

Next.js has `after()`: code that runs after the response has been streamed, without making the user wait. Typical uses are logging, analytics and cache warming. An Angular app would fire these from the browser or the backend.

```ts
import { after } from "next/server";

export async function placeOrder(formData: FormData) {
  "use server";
  const order = await createOrder(formData);
  after(async () => {
    await sendConfirmationEmail(order.id);
    await trackServerEvent("order_placed", { id: order.id });
  });
  return { id: order.id };
}
```

For long jobs (video processing, reports), use a real job queue. `after()` still runs inside the request's server function lifetime and is not a background worker.

## 439: Should translated Next.js code run on the Edge runtime or Node.js?

Use the Node.js runtime by default. It supports all Node APIs and npm packages, and in Next.js 16 `proxy.ts` runs on Node.js too. The Edge runtime has a smaller API surface (no `fs`, limited packages) and is mainly useful for very latency-sensitive, simple logic close to users.

Angular SSR runs on Node (or a compatible runtime via adapters), so moving to the Node runtime in Next.js keeps the same capabilities. Choose Edge only for specific routes after measuring a benefit, by setting `export const runtime = "edge"` in a route segment, and check that every dependency works there.

## 440: Which auth libraries replace Angular auth libraries?

- **Angular:** `angular-auth-oidc-client`, `@auth0/auth0-angular`, MSAL Angular, Keycloak Angular.
- **React (SPA):** `react-oidc-context`, `@auth0/auth0-react`, MSAL React. These keep tokens in the browser like the Angular libraries.
- **Next.js:** Auth.js (NextAuth), Better Auth, Clerk, Auth0's `@auth0/nextjs-auth0`, MSAL with a server flow. These use server-side sessions in httpOnly cookies, which is safer than tokens in browser storage.
- **Vue.js:** `oidc-client-ts` with a Pinia store, `@auth0/auth0-vue`, MSAL with a small wrapper. Nuxt: `nuxt-auth-utils`, Sidebase Nuxt Auth, or Better Auth.

When moving to Next.js or Nuxt, switch from the "SPA with access token in the browser" model to the "backend-for-frontend with session cookie" model. The server holds tokens and calls APIs on the user's behalf.

## 441: Can you automate parts of the translation?

Partly. Useful tools and methods:

- **Angular migrations first:** run `ng generate @angular/core:control-flow`, `signal-input-migration`, `output-migration`, `inject-migration` and `standalone` to modernize the Angular code. Modern Angular is much closer to React and Vue than NgModule plus decorator code.
- **Codemods** (jscodeshift, ts-morph) for repeated patterns in TypeScript, like converting service methods to plain functions.
- **AI coding assistants** for first drafts of components, especially presentational ones, followed by human review and tests.
- **Templates and generators** (Plop, Nx generators) so new React or Vue files follow team conventions.

Automation works best for leaf components and pure logic. Data flow, state architecture and server/client decisions need human design. Always keep tests as the safety net for generated code.

## 442: How do you translate an Angular component that relies on ngDoCheck or custom change detection?

`ngDoCheck` runs on every change detection pass and is usually used to detect mutations inside objects (since `ngOnChanges` only sees reference changes). It often signals that the data is mutated instead of replaced.

**Angular**

```ts
ngDoCheck() {
  const changes = this.differ.diff(this.items);
  if (changes) this.recalculate();
}
```

**React**

```tsx
// Fix the data flow: parents pass new arrays, so a dependency check is enough
const totals = useMemo(() => recalculate(items), [items]);
```

**Vue.js**

```ts
// Vue tracks nested mutations, so a deep watcher or computed sees them
const totals = computed(() => recalculate(props.items));
```

When translating to React, change the parents to update immutably rather than adding a deep comparison. In Vue, mutation tracking makes `ngDoCheck` unnecessary.

## 443: How do you translate an Angular component that uses ViewEncapsulation.ShadowDom?

**Angular**

```ts
@Component({
  selector: "app-widget",
  encapsulation: ViewEncapsulation.ShadowDom,
  styles: `
    p {
      color: teal;
    }
  `,
  template: `<p>Isolated</p>
    <slot></slot>`,
})
export class Widget {}
```

**React**

```tsx
// No built-in Shadow DOM support for components; attach a shadow root and render into it
function ShadowHost({ children }: { children: React.ReactNode }) {
  const [root, setRoot] = useState<ShadowRoot | null>(null);
  return (
    <div
      ref={(el) => {
        if (el && !el.shadowRoot) setRoot(el.attachShadow({ mode: "open" }));
      }}
    >
      {root &&
        createPortal(
          <>
            <style>{"p { color: teal; }"}</style>
            {children}
          </>,
          root,
        )}
    </div>
  );
}
```

**Vue.js**

```ts
// defineCustomElement with a .ce.vue file renders into a shadow root with its styles
customElements.define("app-widget", defineCustomElement(Widget));
```

Shadow DOM is mainly useful when embedding widgets into pages you don't control. Inside one app, CSS Modules or scoped styles are usually enough.

## 444: How do you translate Angular's i18n ICU messages?

**Angular**

```html
<span i18n
  >{count, plural, =0 {No messages} =1 {One message} other {{{count}}
  messages}}</span
>
```

**React**

```tsx
// react-intl (FormatJS) uses the same ICU syntax
<FormattedMessage
  id="inbox.count"
  defaultMessage="{count, plural, =0 {No messages} =1 {One message} other {# messages}}"
  values={{ count }}
/>
```

**Next.js**

```tsx
// next-intl also uses ICU: messages/en.json -> "count": "{count, plural, =0 {No messages} =1 {One message} other {# messages}}"
const t = useTranslations("inbox");
<span>{t("count", { count })}</span>;
```

**Vue.js**

```ts
// vue-i18n uses its own pipe syntax: "No messages | One message | {count} messages"
t("inbox.count", count);
```

Libraries that use ICU (FormatJS, next-intl, i18next with the ICU plugin) let you reuse Angular messages after converting XLIFF to JSON. vue-i18n needs the plural messages rewritten.

## 445: How do you translate lazy-loaded feature routes with their own providers and state?

**Angular**

```ts
// admin.routes.ts
export const ADMIN_ROUTES: Routes = [
  {
    path: "",
    providers: [AdminStore],
    component: AdminShell,
    children: [{ path: "users", loadComponent: () => import("./users") }],
  },
];
```

**React**

```tsx
// The lazy route module brings its own store and provider
{
  path: "admin",
  lazy: () => import("./admin/route"), // exports Component (AdminShell with <AdminStoreProvider>) and children
}
```

**Next.js**

```tsx
// app/admin/layout.tsx wraps all admin pages; code under app/admin is split per route automatically
export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <AdminStoreProvider>{children}</AdminStoreProvider>;
}
```

**Vue.js**

```ts
// Pinia stores are created lazily the first time useAdminStore() is called,
// so importing them only from admin components keeps them in the admin chunk
{ path: "/admin", component: () => import("./admin/AdminShell.vue"), children: adminRoutes }
```

## 446: How do you translate Angular's APP_BASE_HREF and deploying under a sub-path?

**Angular**

```bash
ng build --base-href /shop/
```

**React**

```ts
// vite.config.ts
export default defineConfig({ base: "/shop/" });
// router: createBrowserRouter(routes, { basename: "/shop" })
```

**Next.js**

```ts
// next.config.ts
const nextConfig = { basePath: "/shop" };
// <Link href="/cart"> becomes /shop/cart automatically
```

**Vue.js**

```ts
export default defineConfig({ base: "/shop/" });
createRouter({ history: createWebHistory(import.meta.env.BASE_URL), routes });
```

This matters during route-by-route migrations, where the new app often lives under a sub-path at first.

## 447: How do you translate Angular's Location and history state?

**Angular**

```ts
private location = inject(Location);
back() { this.location.back(); }
// pass state: router.navigate(["/done"], { state: { orderId: 42 } }); read: router.getCurrentNavigation()?.extras.state
```

**React**

```tsx
const navigate = useNavigate();
navigate(-1); // back
navigate("/done", { state: { orderId: 42 } });
const { state } = useLocation(); // state.orderId
```

**Next.js**

```tsx
const router = useRouter();
router.back();
// No history state API in the App Router: pass data in the URL (/done?order=42) or a store
```

**Vue.js**

```ts
router.back();
router.push({ path: "/done", state: { orderId: 42 } });
const orderId = history.state.orderId;
```

History state is lost on reload or when the link is shared, so prefer URL params for anything the next page truly needs.

## 448: How do you make sure the translated code follows each framework's current best practices?

- **React:** function components only, hooks, the React Compiler, Actions and `useActionState` for forms, `use()` for promises and context, no `forwardRef` in React 19, a query library for client data fetching.
- **Next.js:** App Router (not Pages Router) for new code, Server Components by default, `"use client"` at the leaves, Server Actions with validation and auth checks, Cache Components with `"use cache"` where caching is needed, `proxy.ts` instead of `middleware.ts`.
- **Vue:** Composition API with `<script setup lang="ts">`, `defineModel`, reactive props destructure, `useTemplateRef`, Pinia (not Vuex), VueUse for browser APIs.

Run the official lint configs, read the "what's new" posts for the current majors, and avoid copying old tutorials that still use class components, Options API, `getServerSideProps` or Vuex.

## 449: What does a final migration checklist look like?

- [ ] Every Angular route has a matching route (or a redirect) in the new app.
- [ ] Auth, roles and guards are enforced on the server or API, not only in the UI.
- [ ] Forms have the same validation rules, messages and accessibility.
- [ ] All `[innerHTML]` and URL bindings are sanitized in the new code.
- [ ] Error and loading states exist for every data-driven view.
- [ ] i18n messages, plurals and RTL work in all locales.
- [ ] SEO metadata, sitemap, canonical URLs and structured data match or improve.
- [ ] Analytics events are the same and tagged with the app version.
- [ ] Bundle size and Core Web Vitals meet the agreed targets.
- [ ] Unit, E2E, visual and accessibility tests pass on the new app.
- [ ] Hosting, monitoring, logging and alerts are set up and tested.
- [ ] A rollback plan exists until the Angular app is retired.

## 450: What are the key lessons from translating Angular apps to React, Next.js and Vue?

- **Translate concepts, not syntax.** Signals, services, DI and pipes all have counterparts, but the idiomatic shape of the code differs.
- **Modernize the Angular code first.** Standalone components, signals and the new control flow make the translation much more direct.
- **Separate server data from client state.** Query libraries or Server Components replace most service and store code.
- **Respect each framework's model.** React re-runs render, Vue tracks mutations, Next.js splits server and client.
- **Migrate incrementally** with shared packages, a proxy, and end-to-end tests that run against both apps.
- **Watch the things Angular did for you:** sanitization, form accessibility, CDK behaviors, budgets and strict template checks.
- **Measure before and after** so the migration's value is visible.

A successful migration ends with code that looks like it was written for the new framework from the start, not like Angular written in another syntax.
