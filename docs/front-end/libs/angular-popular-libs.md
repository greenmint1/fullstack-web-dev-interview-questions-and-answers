# Angular Popular Libraries Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about the libraries people use most with Angular, split into three levels: 150 easy, 150 moderate and 150 advanced.

The questions cover UI kits (Angular Material, CDK, PrimeNG, NG-ZORRO, ng-bootstrap, Taiga UI, Spartan, Ionic), state management (NgRx, NGXS, Elf, TanStack Query), i18n (ngx-translate, Transloco, `@angular/localize`), forms, tables, charts, auth, testing (Spectator, ng-mocks, Angular Testing Library, Jest, Vitest, Cypress, Playwright), tooling (Nx, angular-eslint, Storybook, Native Federation) and small utility libraries. The examples use modern Angular (v20 and later): standalone components, signals, `inject()` and `provideXxx()` functions. Old setups based on NgModules are mentioned where you will still see them in real projects.

## Table of Contents

### Easy Questions (1-150)

- [1: What do people usually mean by "Angular libraries"?](#1-what-do-people-usually-mean-by-angular-libraries)
- [2: What is Angular Material?](#2-what-is-angular-material)
- [3: How do you add Angular Material to a project?](#3-how-do-you-add-angular-material-to-a-project)
- [4: How do you use an Angular Material component in a standalone component?](#4-how-do-you-use-an-angular-material-component-in-a-standalone-component)
- [5: What is the Angular CDK?](#5-what-is-the-angular-cdk)
- [6: What is the difference between Angular Material and the CDK?](#6-what-is-the-difference-between-angular-material-and-the-cdk)
- [7: What is PrimeNG?](#7-what-is-primeng)
- [8: What is NG-ZORRO?](#8-what-is-ng-zorro)
- [9: What is ng-bootstrap?](#9-what-is-ng-bootstrap)
- [10: What is the difference between ng-bootstrap and ngx-bootstrap?](#10-what-is-the-difference-between-ng-bootstrap-and-ngx-bootstrap)
- [11: What is Taiga UI?](#11-what-is-taiga-ui)
- [12: What is Spartan UI?](#12-what-is-spartan-ui)
- [13: What is Ionic for Angular?](#13-what-is-ionic-for-angular)
- [14: What is NgRx?](#14-what-is-ngrx)
- [15: What is NgRx SignalStore?](#15-what-is-ngrx-signalstore)
- [16: What is NGXS?](#16-what-is-ngxs)
- [17: What is Akita and is it still used?](#17-what-is-akita-and-is-it-still-used)
- [18: What is Elf?](#18-what-is-elf)
- [19: What is TanStack Query for Angular?](#19-what-is-tanstack-query-for-angular)
- [20: What is ngx-translate?](#20-what-is-ngx-translate)
- [21: What is Transloco?](#21-what-is-transloco)
- [22: What is @angular/localize?](#22-what-is-angularlocalize)
- [23: What is the main difference between @angular/localize and runtime i18n libraries?](#23-what-is-the-main-difference-between-angularlocalize-and-runtime-i18n-libraries)
- [24: What is Apollo Angular?](#24-what-is-apollo-angular)
- [25: What is AngularFire?](#25-what-is-angularfire)
- [26: What is AG Grid?](#26-what-is-ag-grid)
- [27: Which libraries are popular for charts in Angular?](#27-which-libraries-are-popular-for-charts-in-angular)
- [28: What is Formly?](#28-what-is-formly)
- [29: What is ngx-mask?](#29-what-is-ngx-mask)
- [30: What is ng-select?](#30-what-is-ng-select)
- [31: What is ngx-toastr?](#31-what-is-ngx-toastr)
- [32: What is Angular Material's MatSnackBar?](#32-what-is-angular-materials-matsnackbar)
- [33: What is Spectator?](#33-what-is-spectator)
- [34: What is ng-mocks?](#34-what-is-ng-mocks)
- [35: What is Angular Testing Library?](#35-what-is-angular-testing-library)
- [36: Which test runners are used with Angular?](#36-which-test-runners-are-used-with-angular)
- [37: What is Cypress?](#37-what-is-cypress)
- [38: What is Playwright?](#38-what-is-playwright)
- [39: What happened to Protractor?](#39-what-happened-to-protractor)
- [40: What is Nx?](#40-what-is-nx)
- [41: What is angular-eslint?](#41-what-is-angular-eslint)
- [42: What is Storybook used for in Angular?](#42-what-is-storybook-used-for-in-angular)
- [43: What is Analog?](#43-what-is-analog)
- [44: What is Native Federation?](#44-what-is-native-federation)
- [45: What is ngxtension?](#45-what-is-ngxtension)
- [46: What is RxAngular?](#46-what-is-rxangular)
- [47: What is ngx-infinite-scroll?](#47-what-is-ngx-infinite-scroll)
- [48: What is ngx-cookie-service?](#48-what-is-ngx-cookie-service)
- [49: What is ngx-markdown?](#49-what-is-ngx-markdown)
- [50: What is @angular/google-maps?](#50-what-is-angulargoogle-maps)
- [51: What is @angular/youtube-player?](#51-what-is-angularyoutube-player)
- [52: What is the purpose of `ng add` for libraries?](#52-what-is-the-purpose-of-ng-add-for-libraries)
- [53: What does `ng update` do for libraries?](#53-what-does-ng-update-do-for-libraries)
- [54: What is a provider function like provideXxx()?](#54-what-is-a-provider-function-like-providexxx)
- [55: What do you do if a library only has an NgModule with forRoot()?](#55-what-do-you-do-if-a-library-only-has-an-ngmodule-with-forroot)
- [56: How do you add a Material icon?](#56-how-do-you-add-a-material-icon)
- [57: How do you open a dialog with Angular Material?](#57-how-do-you-open-a-dialog-with-angular-material)
- [58: How do you read data passed into a Material dialog?](#58-how-do-you-read-data-passed-into-a-material-dialog)
- [59: What is mat-form-field?](#59-what-is-mat-form-field)
- [60: What is mat-table?](#60-what-is-mat-table)
- [61: How do you add sorting and pagination to mat-table?](#61-how-do-you-add-sorting-and-pagination-to-mat-table)
- [62: How do you use the Material date picker?](#62-how-do-you-use-the-material-date-picker)
- [63: What is the CDK drag and drop module?](#63-what-is-the-cdk-drag-and-drop-module)
- [64: What is virtual scrolling in the CDK?](#64-what-is-virtual-scrolling-in-the-cdk)
- [65: What is BreakpointObserver?](#65-what-is-breakpointobserver)
- [66: What does the CDK Clipboard do?](#66-what-does-the-cdk-clipboard-do)
- [67: What is cdkTextareaAutosize?](#67-what-is-cdktextareaautosize)
- [68: What is a theme in Angular Material?](#68-what-is-a-theme-in-angular-material)
- [69: How do you install PrimeNG?](#69-how-do-you-install-primeng)
- [70: How do you use a PrimeNG component?](#70-how-do-you-use-a-primeng-component)
- [71: What is ng-bootstrap's NgbModal?](#71-what-is-ng-bootstraps-ngbmodal)
- [72: Do you need Bootstrap's JavaScript when you use ng-bootstrap?](#72-do-you-need-bootstraps-javascript-when-you-use-ng-bootstrap)
- [73: How do you install ngx-translate in a standalone app?](#73-how-do-you-install-ngx-translate-in-a-standalone-app)
- [74: How do you translate text with ngx-translate?](#74-how-do-you-translate-text-with-ngx-translate)
- [75: How do you change the language with ngx-translate?](#75-how-do-you-change-the-language-with-ngx-translate)
- [76: How do you install Transloco?](#76-how-do-you-install-transloco)
- [77: How do you translate in a template with Transloco?](#77-how-do-you-translate-in-a-template-with-transloco)
- [78: How do you translate in TypeScript with Transloco?](#78-how-do-you-translate-in-typescript-with-transloco)
- [79: How do you add an NgRx store to a standalone app?](#79-how-do-you-add-an-ngrx-store-to-a-standalone-app)
- [80: What are Redux DevTools and how do they help with NgRx?](#80-what-are-redux-devtools-and-how-do-they-help-with-ngrx)
- [81: How do you install NGXS?](#81-how-do-you-install-ngxs)
- [82: What does a basic NGXS state look like?](#82-what-does-a-basic-ngxs-state-look-like)
- [83: How do you set up TanStack Query in Angular?](#83-how-do-you-set-up-tanstack-query-in-angular)
- [84: How do you fetch data with injectQuery?](#84-how-do-you-fetch-data-with-injectquery)
- [85: How do you install Apollo Angular?](#85-how-do-you-install-apollo-angular)
- [86: How do you run a GraphQL query with Apollo Angular?](#86-how-do-you-run-a-graphql-query-with-apollo-angular)
- [87: How do you set up AngularFire?](#87-how-do-you-set-up-angularfire)
- [88: How do you read a Firestore collection with AngularFire?](#88-how-do-you-read-a-firestore-collection-with-angularfire)
- [89: How do you show a basic AG Grid table?](#89-how-do-you-show-a-basic-ag-grid-table)
- [90: How do you show a chart with ng2-charts?](#90-how-do-you-show-a-chart-with-ng2-charts)
- [91: How do you set up ngx-echarts?](#91-how-do-you-set-up-ngx-echarts)
- [92: What is @swimlane/ngx-charts?](#92-what-is-swimlanengx-charts)
- [93: How do you define a simple Formly form?](#93-how-do-you-define-a-simple-formly-form)
- [94: How do you set up ngx-mask in a standalone app?](#94-how-do-you-set-up-ngx-mask-in-a-standalone-app)
- [95: Which libraries help with authentication in Angular?](#95-which-libraries-help-with-authentication-in-angular)
- [96: What is angular-oauth2-oidc?](#96-what-is-angular-oauth2-oidc)
- [97: What is MSAL Angular?](#97-what-is-msal-angular)
- [98: What is the Auth0 Angular SDK?](#98-what-is-the-auth0-angular-sdk)
- [99: What is @auth0/angular-jwt?](#99-what-is-auth0angular-jwt)
- [100: What is Sentry for Angular?](#100-what-is-sentry-for-angular)
- [101: What is Lodash and do you still need it in Angular?](#101-what-is-lodash-and-do-you-still-need-it-in-angular)
- [102: Which date libraries are common in Angular apps?](#102-which-date-libraries-are-common-in-angular-apps)
- [103: What is ngx-skeleton-loader?](#103-what-is-ngx-skeleton-loader)
- [104: What is ngx-spinner?](#104-what-is-ngx-spinner)
- [105: What is @ngx-loading-bar?](#105-what-is-ngx-loading-bar)
- [106: What is ngx-image-cropper?](#106-what-is-ngx-image-cropper)
- [107: What is ngx-extended-pdf-viewer?](#107-what-is-ngx-extended-pdf-viewer)
- [108: What libraries do people use for rich text editing in Angular?](#108-what-libraries-do-people-use-for-rich-text-editing-in-angular)
- [109: How do you use ngx-quill with a reactive form?](#109-how-do-you-use-ngx-quill-with-a-reactive-form)
- [110: What is ngx-file-drop?](#110-what-is-ngx-file-drop)
- [111: What is ngx-logger?](#111-what-is-ngx-logger)
- [112: What is Tailwind CSS and how is it used with Angular?](#112-what-is-tailwind-css-and-how-is-it-used-with-angular)
- [113: What is Bootstrap and how do you add it without a wrapper library?](#113-what-is-bootstrap-and-how-do-you-add-it-without-a-wrapper-library)
- [114: What is Font Awesome for Angular?](#114-what-is-font-awesome-for-angular)
- [115: What other icon libraries are common in Angular?](#115-what-other-icon-libraries-are-common-in-angular)
- [116: What is Compodoc?](#116-what-is-compodoc)
- [117: What is source-map-explorer used for?](#117-what-is-source-map-explorer-used-for)
- [118: What is Angular DevTools?](#118-what-is-angular-devtools)
- [119: What is Prettier and how is it used in Angular projects?](#119-what-is-prettier-and-how-is-it-used-in-angular-projects)
- [120: What are Husky and lint-staged?](#120-what-are-husky-and-lint-staged)
- [121: What is MSW (Mock Service Worker)?](#121-what-is-msw-mock-service-worker)
- [122: What is json-server?](#122-what-is-json-server)
- [123: What is the Angular CDK Overlay?](#123-what-is-the-angular-cdk-overlay)
- [124: What is the CDK Portal?](#124-what-is-the-cdk-portal)
- [125: What is the CDK a11y package?](#125-what-is-the-cdk-a11y-package)
- [126: How do you announce a message to screen readers with the CDK?](#126-how-do-you-announce-a-message-to-screen-readers-with-the-cdk)
- [127: What is SelectionModel in the CDK?](#127-what-is-selectionmodel-in-the-cdk)
- [128: What is the CDK stepper?](#128-what-is-the-cdk-stepper)
- [129: What is Angular Aria?](#129-what-is-angular-aria)
- [130: What is Ionic Capacitor?](#130-what-is-ionic-capacitor)
- [131: How do you add Ionic to a standalone Angular app?](#131-how-do-you-add-ionic-to-a-standalone-angular-app)
- [132: What is NgRx Entity?](#132-what-is-ngrx-entity)
- [133: What is NgRx Router Store?](#133-what-is-ngrx-router-store)
- [134: What is ngrx-immer?](#134-what-is-ngrx-immer)
- [135: What is the ngrx-toolkit from Angular Architects?](#135-what-is-the-ngrx-toolkit-from-angular-architects)
- [136: Which libraries are used for Web Sockets in Angular?](#136-which-libraries-are-used-for-web-sockets-in-angular)
- [137: How do you use RxJS webSocket in a service?](#137-how-do-you-use-rxjs-websocket-in-a-service)
- [138: What is @microsoft/signalr used for in Angular?](#138-what-is-microsoftsignalr-used-for-in-angular)
- [139: What is the Angular service worker package?](#139-what-is-the-angular-service-worker-package)
- [140: What is Workbox and how does it compare to the Angular service worker?](#140-what-is-workbox-and-how-does-it-compare-to-the-angular-service-worker)
- [141: What does peerDependencies mean for an Angular library?](#141-what-does-peerdependencies-mean-for-an-angular-library)
- [142: What does it mean when a library "supports Angular 20"?](#142-what-does-it-mean-when-a-library-supports-angular-20)
- [143: Why should you avoid using `--legacy-peer-deps` or `--force` as a habit?](#143-why-should-you-avoid-using---legacy-peer-deps-or---force-as-a-habit)
- [144: What should you check before adding a third-party Angular library?](#144-what-should-you-check-before-adding-a-third-party-angular-library)
- [145: What is the license difference between AG Grid Community and Enterprise?](#145-what-is-the-license-difference-between-ag-grid-community-and-enterprise)
- [146: What are some commercial Angular UI suites?](#146-what-are-some-commercial-angular-ui-suites)
- [147: What is Clarity Design System?](#147-what-is-clarity-design-system)
- [148: What is ngx-pagination?](#148-what-is-ngx-pagination)
- [149: What is ngx-color-picker?](#149-what-is-ngx-color-picker)
- [150: What is the `@angular/cdk/testing` package?](#150-what-is-the-angularcdktesting-package)

### Moderate Questions (151-300)

- [151: How do you customize the colors of a single Angular Material component?](#151-how-do-you-customize-the-colors-of-a-single-angular-material-component)
- [152: How do you use Material system tokens in your own components?](#152-how-do-you-use-material-system-tokens-in-your-own-components)
- [153: How do you support dark mode with Angular Material?](#153-how-do-you-support-dark-mode-with-angular-material)
- [154: How do you create a custom Material palette from your brand color?](#154-how-do-you-create-a-custom-material-palette-from-your-brand-color)
- [155: How do you change density in Angular Material?](#155-how-do-you-change-density-in-angular-material)
- [156: How do you set global defaults for Material components?](#156-how-do-you-set-global-defaults-for-material-components)
- [157: How do you show custom error messages with mat-form-field and reactive forms?](#157-how-do-you-show-custom-error-messages-with-mat-form-field-and-reactive-forms)
- [158: What is an ErrorStateMatcher?](#158-what-is-an-errorstatematcher)
- [159: How do you write a custom form field control for mat-form-field?](#159-how-do-you-write-a-custom-form-field-control-for-mat-form-field)
- [160: How do you use mat-autocomplete with server-side search?](#160-how-do-you-use-mat-autocomplete-with-server-side-search)
- [161: How do you use objects as values in mat-autocomplete?](#161-how-do-you-use-objects-as-values-in-mat-autocomplete)
- [162: How do you load data from the server for mat-table with paging and sorting?](#162-how-do-you-load-data-from-the-server-for-mat-table-with-paging-and-sorting)
- [163: How do you add row selection with checkboxes to mat-table?](#163-how-do-you-add-row-selection-with-checkboxes-to-mat-table)
- [164: How do you filter a MatTableDataSource?](#164-how-do-you-filter-a-mattabledatasource)
- [165: How do you make sticky headers and columns in mat-table?](#165-how-do-you-make-sticky-headers-and-columns-in-mat-table)
- [166: How do you open a menu from a button in Angular Material?](#166-how-do-you-open-a-menu-from-a-button-in-angular-material)
- [167: How do you return a typed result from a Material dialog?](#167-how-do-you-return-a-typed-result-from-a-material-dialog)
- [168: When would you use the CDK Dialog instead of MatDialog?](#168-when-would-you-use-the-cdk-dialog-instead-of-matdialog)
- [169: How do you create a tooltip-like popup with the CDK Overlay?](#169-how-do-you-create-a-tooltip-like-popup-with-the-cdk-overlay)
- [170: What are the CDK overlay scroll strategies?](#170-what-are-the-cdk-overlay-scroll-strategies)
- [171: How do you drag items between two lists with the CDK?](#171-how-do-you-drag-items-between-two-lists-with-the-cdk)
- [172: How do you restrict drag and drop in the CDK?](#172-how-do-you-restrict-drag-and-drop-in-the-cdk)
- [173: Why does virtual scroll need a fixed item size, and what if items have different heights?](#173-why-does-virtual-scroll-need-a-fixed-item-size-and-what-if-items-have-different-heights)
- [174: How do you use virtual scroll with an infinite list?](#174-how-do-you-use-virtual-scroll-with-an-infinite-list)
- [175: How do you make a responsive sidenav layout with Angular Material?](#175-how-do-you-make-a-responsive-sidenav-layout-with-angular-material)
- [176: What schematics does Angular Material provide?](#176-what-schematics-does-angular-material-provide)
- [177: How do you test a component that uses Material with harnesses?](#177-how-do-you-test-a-component-that-uses-material-with-harnesses)
- [178: How do you test a component that opens a MatDialog?](#178-how-do-you-test-a-component-that-opens-a-matdialog)
- [179: How do you register custom SVG icons in Angular Material?](#179-how-do-you-register-custom-svg-icons-in-angular-material)
- [180: How do you use Material Symbols instead of the old Material Icons font?](#180-how-do-you-use-material-symbols-instead-of-the-old-material-icons-font)
- [181: How do you use a PrimeNG table with lazy loading?](#181-how-do-you-use-a-primeng-table-with-lazy-loading)
- [182: How do you customize a PrimeNG theme preset?](#182-how-do-you-customize-a-primeng-theme-preset)
- [183: What is PrimeNG unstyled mode?](#183-what-is-primeng-unstyled-mode)
- [184: What is the pass-through (pt) API in PrimeNG?](#184-what-is-the-pass-through-pt-api-in-primeng)
- [185: How do you show a confirmation dialog with PrimeNG?](#185-how-do-you-show-a-confirmation-dialog-with-primeng)
- [186: How do you use NG-ZORRO in a standalone app?](#186-how-do-you-use-ng-zorro-in-a-standalone-app)
- [187: How do you use the ng-bootstrap typeahead?](#187-how-do-you-use-the-ng-bootstrap-typeahead)
- [188: How do you set global defaults in ng-bootstrap?](#188-how-do-you-set-global-defaults-in-ng-bootstrap)
- [189: How do you lazy load translations per feature with Transloco?](#189-how-do-you-lazy-load-translations-per-feature-with-transloco)
- [190: What Transloco plugins are commonly used?](#190-what-transloco-plugins-are-commonly-used)
- [191: How do you handle plurals with ngx-translate or Transloco?](#191-how-do-you-handle-plurals-with-ngx-translate-or-transloco)
- [192: How do you make translations type-safe?](#192-how-do-you-make-translations-type-safe)
- [193: How do you handle missing translations?](#193-how-do-you-handle-missing-translations)
- [194: How do you load the user's preferred language at startup?](#194-how-do-you-load-the-users-preferred-language-at-startup)
- [195: How do you write a classic NgRx effect with HTTP?](#195-how-do-you-write-a-classic-ngrx-effect-with-http)
- [196: How do you read NgRx store state as a signal?](#196-how-do-you-read-ngrx-store-state-as-a-signal)
- [197: How do you load data in a SignalStore?](#197-how-do-you-load-data-in-a-signalstore)
- [198: How do you manage a list of records in a SignalStore?](#198-how-do-you-manage-a-list-of-records-in-a-signalstore)
- [199: What are lifecycle hooks in SignalStore?](#199-what-are-lifecycle-hooks-in-signalstore)
- [200: When would you provide a SignalStore at component level instead of root?](#200-when-would-you-provide-a-signalstore-at-component-level-instead-of-root)
- [201: How do you handle async work in NGXS?](#201-how-do-you-handle-async-work-in-ngxs)
- [202: What NGXS plugins are commonly used?](#202-what-ngxs-plugins-are-commonly-used)
- [203: How do you persist state to localStorage with NGXS?](#203-how-do-you-persist-state-to-localstorage-with-ngxs)
- [204: How do you compare NgRx Store, NgRx SignalStore and NGXS?](#204-how-do-you-compare-ngrx-store-ngrx-signalstore-and-ngxs)
- [205: How do you use mutations in TanStack Query for Angular?](#205-how-do-you-use-mutations-in-tanstack-query-for-angular)
- [206: How do you make a TanStack query depend on a signal?](#206-how-do-you-make-a-tanstack-query-depend-on-a-signal)
- [207: What is staleTime vs gcTime in TanStack Query?](#207-what-is-staletime-vs-gctime-in-tanstack-query)
- [208: When would you use TanStack Query instead of NgRx?](#208-when-would-you-use-tanstack-query-instead-of-ngrx)
- [209: How does Angular's httpResource compare to TanStack Query?](#209-how-does-angulars-httpresource-compare-to-tanstack-query)
- [210: How do you do a mutation with Apollo Angular and update the cache?](#210-how-do-you-do-a-mutation-with-apollo-angular-and-update-the-cache)
- [211: How do you add an auth header to Apollo Angular requests?](#211-how-do-you-add-an-auth-header-to-apollo-angular-requests)
- [212: What is GraphQL Code Generator and why use it with Apollo Angular?](#212-what-is-graphql-code-generator-and-why-use-it-with-apollo-angular)
- [213: How do you protect routes with AngularFire Auth?](#213-how-do-you-protect-routes-with-angularfire-auth)
- [214: How do you add a custom cell renderer in AG Grid?](#214-how-do-you-add-a-custom-cell-renderer-in-ag-grid)
- [215: How do you access the AG Grid API?](#215-how-do-you-access-the-ag-grid-api)
- [216: Why should you set getRowId in AG Grid?](#216-why-should-you-set-getrowid-in-ag-grid)
- [217: What row models does AG Grid have?](#217-what-row-models-does-ag-grid-have)
- [218: How do you update a chart in ng2-charts when data changes?](#218-how-do-you-update-a-chart-in-ng2-charts-when-data-changes)
- [219: How do you make Formly use custom field types?](#219-how-do-you-make-formly-use-custom-field-types)
- [220: How do you show or hide Formly fields based on other values?](#220-how-do-you-show-or-hide-formly-fields-based-on-other-values)
- [221: How do you add custom validation in Formly?](#221-how-do-you-add-custom-validation-in-formly)
- [222: When should you not use Formly?](#222-when-should-you-not-use-formly)
- [223: How do you use ng-select with async search?](#223-how-do-you-use-ng-select-with-async-search)
- [224: How do you show a custom option template in ng-select?](#224-how-do-you-show-a-custom-option-template-in-ng-select)
- [225: How do you set up ngx-toastr in a standalone app?](#225-how-do-you-set-up-ngx-toastr-in-a-standalone-app)
- [226: How do you show error toasts for every failed HTTP request?](#226-how-do-you-show-error-toasts-for-every-failed-http-request)
- [227: How do you set up angular-oauth2-oidc in a standalone app?](#227-how-do-you-set-up-angular-oauth2-oidc-in-a-standalone-app)
- [228: How do you refresh tokens automatically with angular-oauth2-oidc?](#228-how-do-you-refresh-tokens-automatically-with-angular-oauth2-oidc)
- [229: How do you protect routes and API calls with MSAL Angular?](#229-how-do-you-protect-routes-and-api-calls-with-msal-angular)
- [230: How do you add the Auth0 access token to API calls?](#230-how-do-you-add-the-auth0-access-token-to-api-calls)
- [231: How do you use keycloak-angular in a standalone app?](#231-how-do-you-use-keycloak-angular-in-a-standalone-app)
- [232: How do you set up Sentry in an Angular app?](#232-how-do-you-set-up-sentry-in-an-angular-app)
- [233: How do you configure Jest for an Angular project?](#233-how-do-you-configure-jest-for-an-angular-project)
- [234: How do you use Vitest with the Angular CLI?](#234-how-do-you-use-vitest-with-the-angular-cli)
- [235: How do you migrate tests from Jasmine to Jest or Vitest?](#235-how-do-you-migrate-tests-from-jasmine-to-jest-or-vitest)
- [236: How do you test a service with Spectator?](#236-how-do-you-test-a-service-with-spectator)
- [237: How do you test HTTP calls with Spectator?](#237-how-do-you-test-http-calls-with-spectator)
- [238: How do you set inputs and listen to outputs with Spectator?](#238-how-do-you-set-inputs-and-listen-to-outputs-with-spectator)
- [239: What is MockBuilder in ng-mocks?](#239-what-is-mockbuilder-in-ng-mocks)
- [240: What is the difference between shallow and deep component tests?](#240-what-is-the-difference-between-shallow-and-deep-component-tests)
- [241: How do you query elements the right way in Angular Testing Library?](#241-how-do-you-query-elements-the-right-way-in-angular-testing-library)
- [242: How do you provide mocks in Angular Testing Library's render?](#242-how-do-you-provide-mocks-in-angular-testing-librarys-render)
- [243: How do you set up Cypress component testing in Angular?](#243-how-do-you-set-up-cypress-component-testing-in-angular)
- [244: How do you add Playwright to an Angular project?](#244-how-do-you-add-playwright-to-an-angular-project)
- [245: How do you mock API responses in Playwright?](#245-how-do-you-mock-api-responses-in-playwright)
- [246: How do you use Storybook with Angular components that need providers?](#246-how-do-you-use-storybook-with-angular-components-that-need-providers)
- [247: How do you set up Nx for an existing Angular CLI project?](#247-how-do-you-set-up-nx-for-an-existing-angular-cli-project)
- [248: What is `nx affected` and why is it useful?](#248-what-is-nx-affected-and-why-is-it-useful)
- [249: What are Nx module boundary rules?](#249-what-are-nx-module-boundary-rules)
- [250: How do you configure angular-eslint with the flat config?](#250-how-do-you-configure-angular-eslint-with-the-flat-config)
- [251: Which angular-eslint template rules are worth turning on?](#251-which-angular-eslint-template-rules-are-worth-turning-on)
- [252: How do you set up Native Federation for a host and a remote?](#252-how-do-you-set-up-native-federation-for-a-host-and-a-remote)
- [253: What is the difference between Module Federation and Native Federation for Angular?](#253-what-is-the-difference-between-module-federation-and-native-federation-for-angular)
- [254: How do you get route params as signals with ngxtension?](#254-how-do-you-get-route-params-as-signals-with-ngxtension)
- [255: What does derivedAsync in ngxtension do?](#255-what-does-derivedasync-in-ngxtension-do)
- [256: What is RxAngular's rxLet and when would you use it?](#256-what-is-rxangulars-rxlet-and-when-would-you-use-it)
- [257: What replaced @ngneat/until-destroy?](#257-what-replaced-ngneatuntil-destroy)
- [258: How do you choose between ngx-cookie-service and localStorage?](#258-how-do-you-choose-between-ngx-cookie-service-and-localstorage)
- [259: How do you add syntax highlighting to ngx-markdown?](#259-how-do-you-add-syntax-highlighting-to-ngx-markdown)
- [260: How do you use @angular/google-maps with markers from data?](#260-how-do-you-use-angulargoogle-maps-with-markers-from-data)
- [261: Which libraries are used for maps besides Google Maps?](#261-which-libraries-are-used-for-maps-besides-google-maps)
- [262: How do you wrap a plain JavaScript library in an Angular component?](#262-how-do-you-wrap-a-plain-javascript-library-in-an-angular-component)
- [263: How do you lazy load a heavy library only when needed?](#263-how-do-you-lazy-load-a-heavy-library-only-when-needed)
- [264: How do you use @defer with a heavy chart component?](#264-how-do-you-use-defer-with-a-heavy-chart-component)
- [265: How do you check how much a library adds to your bundle?](#265-how-do-you-check-how-much-a-library-adds-to-your-bundle)
- [266: Why does the CLI warn about CommonJS dependencies?](#266-why-does-the-cli-warn-about-commonjs-dependencies)
- [267: How do you use a library that touches `window` or `document` with SSR?](#267-how-do-you-use-a-library-that-touches-window-or-document-with-ssr)
- [268: How do you make Material or CDK components work with SSR and hydration?](#268-how-do-you-make-material-or-cdk-components-work-with-ssr-and-hydration)
- [269: How do you replace Moment.js in an Angular Material project?](#269-how-do-you-replace-momentjs-in-an-angular-material-project)
- [270: How do you customize the date format of the Material date picker?](#270-how-do-you-customize-the-date-format-of-the-material-date-picker)
- [271: How do you use Tailwind together with Angular Material?](#271-how-do-you-use-tailwind-together-with-angular-material)
- [272: How do you choose between Angular Material, PrimeNG and NG-ZORRO for a new project?](#272-how-do-you-choose-between-angular-material-primeng-and-ng-zorro-for-a-new-project)
- [273: What is the Spartan helm CLI workflow?](#273-what-is-the-spartan-helm-cli-workflow)
- [274: How do you handle forms in Ionic Angular apps?](#274-how-do-you-handle-forms-in-ionic-angular-apps)
- [275: How do you navigate in Ionic Angular?](#275-how-do-you-navigate-in-ionic-angular)
- [276: How do you build a dynamic form from a server schema without Formly?](#276-how-do-you-build-a-dynamic-form-from-a-server-schema-without-formly)
- [277: What is @ngneat/reactive-forms and is it still needed?](#277-what-is-ngneatreactive-forms-and-is-it-still-needed)
- [278: How do you use the CDK listbox and menu?](#278-how-do-you-use-the-cdk-listbox-and-menu)
- [279: How do you trap focus inside a custom modal?](#279-how-do-you-trap-focus-inside-a-custom-modal)
- [280: How do you style keyboard focus only (not mouse focus) with the CDK?](#280-how-do-you-style-keyboard-focus-only-not-mouse-focus-with-the-cdk)
- [281: How do you use Lucide icons in Angular?](#281-how-do-you-use-lucide-icons-in-angular)
- [282: How do you show a global loading bar for HTTP requests yourself?](#282-how-do-you-show-a-global-loading-bar-for-http-requests-yourself)
- [283: How do you run Storybook interaction tests for Angular?](#283-how-do-you-run-storybook-interaction-tests-for-angular)
- [284: What is Chromatic?](#284-what-is-chromatic)
- [285: How do you use Analog's Vitest plugin in an Angular CLI or Nx project?](#285-how-do-you-use-analogs-vitest-plugin-in-an-angular-cli-or-nx-project)
- [286: How do you create file-based routes in Analog?](#286-how-do-you-create-file-based-routes-in-analog)
- [287: How do you share Angular code between apps with an Nx library?](#287-how-do-you-share-angular-code-between-apps-with-an-nx-library)
- [288: How do you build your own reusable Angular library?](#288-how-do-you-build-your-own-reusable-angular-library)
- [289: What are secondary entry points in a library?](#289-what-are-secondary-entry-points-in-a-library)
- [290: How do you add an `ng add` schematic to your own library?](#290-how-do-you-add-an-ng-add-schematic-to-your-own-library)
- [291: What is the Angular Package Format?](#291-what-is-the-angular-package-format)
- [292: What is partial compilation and why do libraries use it?](#292-what-is-partial-compilation-and-why-do-libraries-use-it)
- [293: How do you set up Sentry performance tracing for Angular routes?](#293-how-do-you-set-up-sentry-performance-tracing-for-angular-routes)
- [294: How do you use an Angular library that is not compatible with your Angular version yet?](#294-how-do-you-use-an-angular-library-that-is-not-compatible-with-your-angular-version-yet)
- [295: How do you upgrade Angular when you use many third-party libraries?](#295-how-do-you-upgrade-angular-when-you-use-many-third-party-libraries)
- [296: How do you use @angular/localize with runtime language loading?](#296-how-do-you-use-angularlocalize-with-runtime-language-loading)
- [297: How do you extract and merge translations with @angular/localize?](#297-how-do-you-extract-and-merge-translations-with-angularlocalize)
- [298: How do you show a PDF or Excel export from a table?](#298-how-do-you-show-a-pdf-or-excel-export-from-a-table)
- [299: How do you use ngx-infinite-scroll inside a scrollable container?](#299-how-do-you-use-ngx-infinite-scroll-inside-a-scrollable-container)
- [300: How do you show a skeleton for each item in a @defer or loading state?](#300-how-do-you-show-a-skeleton-for-each-item-in-a-defer-or-loading-state)

### Advanced Questions (301-450)

- [301: How does the CDK Overlay position panels and handle running out of space?](#301-how-does-the-cdk-overlay-position-panels-and-handle-running-out-of-space)
- [302: How does Angular Material's theming system work under the hood in M3?](#302-how-does-angular-materials-theming-system-work-under-the-hood-in-m3)
- [303: How do you build a design system on top of Angular Material without fighting it?](#303-how-do-you-build-a-design-system-on-top-of-angular-material-without-fighting-it)
- [304: Why did Angular Material switch to MDC-based components and what did it break?](#304-why-did-angular-material-switch-to-mdc-based-components-and-what-did-it-break)
- [305: How do component test harnesses work internally?](#305-how-do-component-test-harnesses-work-internally)
- [306: How do you write your own component harness?](#306-how-do-you-write-your-own-component-harness)
- [307: How does CDK virtual scroll work and what are its limits?](#307-how-does-cdk-virtual-scroll-work-and-what-are-its-limits)
- [308: How would you make a mat-table with 50,000 rows fast?](#308-how-would-you-make-a-mat-table-with-50000-rows-fast)
- [309: How does AG Grid stay fast with large data sets?](#309-how-does-ag-grid-stay-fast-with-large-data-sets)
- [310: How do you handle live updates (for example prices every 100ms) in AG Grid?](#310-how-do-you-handle-live-updates-for-example-prices-every-100ms-in-ag-grid)
- [311: How does the AG Grid Server-Side Row Model work?](#311-how-does-the-ag-grid-server-side-row-model-work)
- [312: How does NgRx SignalStore work internally?](#312-how-does-ngrx-signalstore-work-internally)
- [313: How do you write a reusable custom feature for SignalStore?](#313-how-do-you-write-a-reusable-custom-feature-for-signalstore)
- [314: How do you test a SignalStore?](#314-how-do-you-test-a-signalstore)
- [315: What is state protection in SignalStore?](#315-what-is-state-protection-in-signalstore)
- [316: What is the NgRx Signals events plugin?](#316-what-is-the-ngrx-signals-events-plugin)
- [317: How do classic NgRx selectors memoize, and when does memoization break?](#317-how-do-classic-ngrx-selectors-memoize-and-when-does-memoization-break)
- [318: How do you avoid memory leaks with factory selectors in NgRx?](#318-how-do-you-avoid-memory-leaks-with-factory-selectors-in-ngrx)
- [319: How do you handle race conditions in NgRx effects?](#319-how-do-you-handle-race-conditions-in-ngrx-effects)
- [320: How do you do optimistic updates with NgRx or SignalStore?](#320-how-do-you-do-optimistic-updates-with-ngrx-or-signalstore)
- [321: How would you migrate a large app from classic NgRx Store to SignalStore?](#321-how-would-you-migrate-a-large-app-from-classic-ngrx-store-to-signalstore)
- [322: How does TanStack Query for Angular integrate with signals?](#322-how-does-tanstack-query-for-angular-integrate-with-signals)
- [323: How do you prefetch data with TanStack Query on route navigation?](#323-how-do-you-prefetch-data-with-tanstack-query-on-route-navigation)
- [324: How do you do optimistic updates with TanStack Query?](#324-how-do-you-do-optimistic-updates-with-tanstack-query)
- [325: How do you use TanStack Query with SSR in Angular?](#325-how-do-you-use-tanstack-query-with-ssr-in-angular)
- [326: How does Apollo's normalized cache work and when does it cause problems?](#326-how-does-apollos-normalized-cache-work-and-when-does-it-cause-problems)
- [327: How do you implement cursor pagination with Apollo Angular?](#327-how-do-you-implement-cursor-pagination-with-apollo-angular)
- [328: How do you handle GraphQL subscriptions in Apollo Angular?](#328-how-do-you-handle-graphql-subscriptions-in-apollo-angular)
- [329: How do runtime i18n libraries affect performance compared to @angular/localize?](#329-how-do-runtime-i18n-libraries-affect-performance-compared-to-angularlocalize)
- [330: How does ngx-translate's pipe update when the language changes, and why can it be slow?](#330-how-does-ngx-translates-pipe-update-when-the-language-changes-and-why-can-it-be-slow)
- [331: How would you organize translations for a large app with many teams?](#331-how-would-you-organize-translations-for-a-large-app-with-many-teams)
- [332: How do you translate route titles, page meta tags and validation messages?](#332-how-do-you-translate-route-titles-page-meta-tags-and-validation-messages)
- [333: How do you make Transloco or ngx-translate work with SSR?](#333-how-do-you-make-transloco-or-ngx-translate-work-with-ssr)
- [334: How does Formly render a form internally and what are its performance traps?](#334-how-does-formly-render-a-form-internally-and-what-are-its-performance-traps)
- [335: How do you build a component library that supports both Material and a custom theme?](#335-how-do-you-build-a-component-library-that-supports-both-material-and-a-custom-theme)
- [336: How do PrimeNG design tokens and CSS layers work, and how do you avoid style conflicts?](#336-how-do-primeng-design-tokens-and-css-layers-work-and-how-do-you-avoid-style-conflicts)
- [337: How do you handle a breaking change in a UI library across a big codebase?](#337-how-do-you-handle-a-breaking-change-in-a-ui-library-across-a-big-codebase)
- [338: Should you wrap third-party UI components in your own components?](#338-should-you-wrap-third-party-ui-components-in-your-own-components)
- [339: How do you design a notification service that can switch between ngx-toastr and MatSnackBar?](#339-how-do-you-design-a-notification-service-that-can-switch-between-ngx-toastr-and-matsnackbar)
- [340: How do Angular libraries stay compatible with zoneless change detection?](#340-how-do-angular-libraries-stay-compatible-with-zoneless-change-detection)
- [341: Why can a third-party library make your app slow with Zone.js?](#341-why-can-a-third-party-library-make-your-app-slow-with-zonejs)
- [342: How do you profile which library is causing slow change detection?](#342-how-do-you-profile-which-library-is-causing-slow-change-detection)
- [343: How do you integrate a library that uses its own DOM rendering (like a map or editor) with Angular change detection?](#343-how-do-you-integrate-a-library-that-uses-its-own-dom-rendering-like-a-map-or-editor-with-angular-change-detection)
- [344: How do you render Angular components inside a third-party library (for example a popup in a Leaflet map)?](#344-how-do-you-render-angular-components-inside-a-third-party-library-for-example-a-popup-in-a-leaflet-map)
- [345: How do you avoid memory leaks with third-party libraries in Angular?](#345-how-do-you-avoid-memory-leaks-with-third-party-libraries-in-angular)
- [346: How do you secure rich text from editors like Quill or TinyMCE?](#346-how-do-you-secure-rich-text-from-editors-like-quill-or-tinymce)
- [347: What security risks come with ngx-markdown and similar renderers?](#347-what-security-risks-come-with-ngx-markdown-and-similar-renderers)
- [348: How do you keep third-party dependencies safe in an Angular project?](#348-how-do-you-keep-third-party-dependencies-safe-in-an-angular-project)
- [349: How do OIDC libraries protect against token theft, and what are the trade-offs of storing tokens in the browser?](#349-how-do-oidc-libraries-protect-against-token-theft-and-what-are-the-trade-offs-of-storing-tokens-in-the-browser)
- [350: How does the MSAL Angular interceptor decide which token to attach, and what can go wrong?](#350-how-does-the-msal-angular-interceptor-decide-which-token-to-attach-and-what-can-go-wrong)
- [351: How do you implement token refresh with a functional interceptor without firing many refresh requests?](#351-how-do-you-implement-token-refresh-with-a-functional-interceptor-without-firing-many-refresh-requests)
- [352: How do you handle authentication in an app with micro frontends (Native Federation)?](#352-how-do-you-handle-authentication-in-an-app-with-micro-frontends-native-federation)
- [353: How does Native Federation share dependencies, and what goes wrong with Angular?](#353-how-does-native-federation-share-dependencies-and-what-goes-wrong-with-angular)
- [354: When would you use web components (Angular Elements) instead of Native Federation for micro frontends?](#354-when-would-you-use-web-components-angular-elements-instead-of-native-federation-for-micro-frontends)
- [355: How does Nx caching work and how do you make sure it's correct?](#355-how-does-nx-caching-work-and-how-do-you-make-sure-its-correct)
- [356: How would you structure a large Angular Nx monorepo?](#356-how-would-you-structure-a-large-angular-nx-monorepo)
- [357: How do Nx generators and executors differ from Angular CLI schematics and builders?](#357-how-do-nx-generators-and-executors-differ-from-angular-cli-schematics-and-builders)
- [358: How does Storybook build Angular stories, and why do some components fail to render?](#358-how-does-storybook-build-angular-stories-and-why-do-some-components-fail-to-render)
- [359: How do you run Angular unit tests in a real browser and why would you?](#359-how-do-you-run-angular-unit-tests-in-a-real-browser-and-why-would-you)
- [360: How do you test code that uses Material dialogs, overlays or snack bars in jsdom?](#360-how-do-you-test-code-that-uses-material-dialogs-overlays-or-snack-bars-in-jsdom)
- [361: Why do tests with Spectator or ng-mocks become flaky, and how do you fix them?](#361-why-do-tests-with-spectator-or-ng-mocks-become-flaky-and-how-do-you-fix-them)
- [362: How do you test a component that uses @defer?](#362-how-do-you-test-a-component-that-uses-defer)
- [363: How would you test a component that uses AG Grid?](#363-how-would-you-test-a-component-that-uses-ag-grid)
- [364: How do you mock a GraphQL API in Apollo Angular tests?](#364-how-do-you-mock-a-graphql-api-in-apollo-angular-tests)
- [365: How do you test effects in classic NgRx?](#365-how-do-you-test-effects-in-classic-ngrx)
- [366: How do you use `provideMockStore` to test components that use NgRx?](#366-how-do-you-use-providemockstore-to-test-components-that-use-ngrx)
- [367: How do you design E2E tests so they don't break when UI libraries change?](#367-how-do-you-design-e2e-tests-so-they-dont-break-when-ui-libraries-change)
- [368: How does Playwright's auto-waiting help with Angular apps?](#368-how-does-playwrights-auto-waiting-help-with-angular-apps)
- [369: How do you speed up Angular CI with Nx Cloud or similar tools?](#369-how-do-you-speed-up-angular-ci-with-nx-cloud-or-similar-tools)
- [370: How do you pick a state management solution for a new large Angular app?](#370-how-do-you-pick-a-state-management-solution-for-a-new-large-angular-app)
- [371: How do you handle forms state together with a store like NgRx?](#371-how-do-you-handle-forms-state-together-with-a-store-like-ngrx)
- [372: How do you design a SignalStore that handles pagination, filtering and caching?](#372-how-do-you-design-a-signalstore-that-handles-pagination-filtering-and-caching)
- [373: How do you persist and rehydrate store state safely?](#373-how-do-you-persist-and-rehydrate-store-state-safely)
- [374: What is a meta-reducer in NgRx and what libraries use them?](#374-what-is-a-meta-reducer-in-ngrx-and-what-libraries-use-them)
- [375: How do you reset all store state on logout?](#375-how-do-you-reset-all-store-state-on-logout)
- [376: How do you combine TanStack Query with NgRx or SignalStore without duplicating state?](#376-how-do-you-combine-tanstack-query-with-ngrx-or-signalstore-without-duplicating-state)
- [377: How do you build an accessible custom select on top of the CDK or Angular Aria instead of using a library?](#377-how-do-you-build-an-accessible-custom-select-on-top-of-the-cdk-or-angular-aria-instead-of-using-a-library)
- [378: How does the CDK ListKeyManager work, and how would you use it?](#378-how-does-the-cdk-listkeymanager-work-and-how-would-you-use-it)
- [379: How would you evaluate if a UI library is accessible enough?](#379-how-would-you-evaluate-if-a-ui-library-is-accessible-enough)
- [380: How do you add automated accessibility checks for library components in CI?](#380-how-do-you-add-automated-accessibility-checks-for-library-components-in-ci)
- [381: How does Ionic's page caching affect Angular lifecycle and memory?](#381-how-does-ionics-page-caching-affect-angular-lifecycle-and-memory)
- [382: What are the main performance tips for Ionic Angular apps?](#382-what-are-the-main-performance-tips-for-ionic-angular-apps)
- [383: How do you share code between an Ionic mobile app and an Angular web app?](#383-how-do-you-share-code-between-an-ionic-mobile-app-and-an-angular-web-app)
- [384: How does @angular/localize work at build time?](#384-how-does-angularlocalize-work-at-build-time)
- [385: What are the pitfalls of @angular/localize's message IDs?](#385-what-are-the-pitfalls-of-angularlocalizes-message-ids)
- [386: How do you translate text inside third-party components that don't support i18n?](#386-how-do-you-translate-text-inside-third-party-components-that-dont-support-i18n)
- [387: How do you set Angular's LOCALE_ID together with a runtime i18n library?](#387-how-do-you-set-angulars-locale_id-together-with-a-runtime-i18n-library)
- [388: How do you make charts handle large data sets in Angular?](#388-how-do-you-make-charts-handle-large-data-sets-in-angular)
- [389: How do you make ECharts tree-shakable in Angular?](#389-how-do-you-make-echarts-tree-shakable-in-angular)
- [390: How do you build a reusable chart wrapper that works with signals?](#390-how-do-you-build-a-reusable-chart-wrapper-that-works-with-signals)
- [391: How would you handle a slow, very large form built with Formly or reactive forms?](#391-how-would-you-handle-a-slow-very-large-form-built-with-formly-or-reactive-forms)
- [392: How do you integrate ng-select or other custom inputs with signal forms?](#392-how-do-you-integrate-ng-select-or-other-custom-inputs-with-signal-forms)
- [393: How do you choose between ngx-mask and writing your own masking directive?](#393-how-do-you-choose-between-ngx-mask-and-writing-your-own-masking-directive)
- [394: How do you handle time zones correctly with Material date pickers?](#394-how-do-you-handle-time-zones-correctly-with-material-date-pickers)
- [395: How do you prevent layout shift when UI library components load?](#395-how-do-you-prevent-layout-shift-when-ui-library-components-load)
- [396: How do Material icon fonts affect performance, and how can you improve it?](#396-how-do-material-icon-fonts-affect-performance-and-how-can-you-improve-it)
- [397: How do you reduce the bundle size of an app that uses many libraries?](#397-how-do-you-reduce-the-bundle-size-of-an-app-that-uses-many-libraries)
- [398: Why can barrel files (index.ts) hurt tree-shaking with libraries?](#398-why-can-barrel-files-indexts-hurt-tree-shaking-with-libraries)
- [399: How does `sideEffects` in package.json affect Angular libraries?](#399-how-does-sideeffects-in-packagejson-affect-angular-libraries)
- [400: How do you load a library from a CDN instead of the bundle, and when is it a good idea?](#400-how-do-you-load-a-library-from-a-cdn-instead-of-the-bundle-and-when-is-it-a-good-idea)
- [401: How do you handle a library that registers global styles that conflict with yours?](#401-how-do-you-handle-a-library-that-registers-global-styles-that-conflict-with-yours)
- [402: How do UI libraries handle styles with Angular's view encapsulation?](#402-how-do-ui-libraries-handle-styles-with-angulars-view-encapsulation)
- [403: How do you customize Material components without ::ng-deep?](#403-how-do-you-customize-material-components-without-ng-deep)
- [404: How does PrimeNG inject styles at runtime and what does that mean for CSP?](#404-how-does-primeng-inject-styles-at-runtime-and-what-does-that-mean-for-csp)
- [405: How do you use a strict Content Security Policy with Angular and common libraries?](#405-how-do-you-use-a-strict-content-security-policy-with-angular-and-common-libraries)
- [406: How do Trusted Types work with Angular and third-party libraries?](#406-how-do-trusted-types-work-with-angular-and-third-party-libraries)
- [407: What risks come with postinstall scripts in npm packages, and how do you reduce them?](#407-what-risks-come-with-postinstall-scripts-in-npm-packages-and-how-do-you-reduce-them)
- [408: How do you keep many Angular libraries up to date without breaking things?](#408-how-do-you-keep-many-angular-libraries-up-to-date-without-breaking-things)
- [409: How do you decide whether to build a component yourself or use a library?](#409-how-do-you-decide-whether-to-build-a-component-yourself-or-use-a-library)
- [410: What would you do if a library you depend on is abandoned?](#410-what-would-you-do-if-a-library-you-depend-on-is-abandoned)
- [411: How do you migrate from Karma/Jasmine to Vitest in a big Angular project?](#411-how-do-you-migrate-from-karmajasmine-to-vitest-in-a-big-angular-project)
- [412: Why might a Jest setup break after an Angular upgrade?](#412-why-might-a-jest-setup-break-after-an-angular-upgrade)
- [413: How does ng-mocks create mocks of components and what are the limits?](#413-how-does-ng-mocks-create-mocks-of-components-and-what-are-the-limits)
- [414: How do you test a component that uses TanStack Query?](#414-how-do-you-test-a-component-that-uses-tanstack-query)
- [415: How do you share a configured Storybook decorator for all stories (theme, translations, router)?](#415-how-do-you-share-a-configured-storybook-decorator-for-all-stories-theme-translations-router)
- [416: How would you set up visual regression testing for an Angular component library?](#416-how-would-you-set-up-visual-regression-testing-for-an-angular-component-library)
- [417: How do you build an Angular library that supports several major Angular versions?](#417-how-do-you-build-an-angular-library-that-supports-several-major-angular-versions)
- [418: How do you design a library's public API so it can grow without breaking users?](#418-how-do-you-design-a-librarys-public-api-so-it-can-grow-without-breaking-users)
- [419: How do you write a provider function with features, like `provideHttpClient(withInterceptors())`?](#419-how-do-you-write-a-provider-function-with-features-like-providehttpclientwithinterceptors)
- [420: How do you let library users provide their own implementation of a service?](#420-how-do-you-let-library-users-provide-their-own-implementation-of-a-service)
- [421: How do you make your library tree-shakable?](#421-how-do-you-make-your-library-tree-shakable)
- [422: How do you handle styles and theming in your own Angular library?](#422-how-do-you-handle-styles-and-theming-in-your-own-angular-library)
- [423: How do Angular CDK and Material keep up with Angular releases, and what can libraries learn from it?](#423-how-do-angular-cdk-and-material-keep-up-with-angular-releases-and-what-can-libraries-learn-from-it)
- [424: How do you debug "NullInjectorError: No provider for X" coming from a library?](#424-how-do-you-debug-nullinjectorerror-no-provider-for-x-coming-from-a-library)
- [425: How do you debug "NG0203: inject() must be called from an injection context" when using libraries?](#425-how-do-you-debug-ng0203-inject-must-be-called-from-an-injection-context-when-using-libraries)
- [426: Why do you get two copies of Angular when linking a local library, and how do you fix it?](#426-why-do-you-get-two-copies-of-angular-when-linking-a-local-library-and-how-do-you-fix-it)
- [427: How does ng-packagr build a library and what does it produce?](#427-how-does-ng-packagr-build-a-library-and-what-does-it-produce)
- [428: How do you choose between NgRx Store devtools and Angular DevTools for debugging state?](#428-how-do-you-choose-between-ngrx-store-devtools-and-angular-devtools-for-debugging-state)
- [429: How does the ngrx-toolkit's withDevtools work with SignalStore?](#429-how-does-the-ngrx-toolkits-withdevtools-work-with-signalstore)
- [430: Scenario: your Angular app's initial bundle grew from 400 KB to 1.2 MB after adding a few libraries. What do you do?](#430-scenario-your-angular-apps-initial-bundle-grew-from-400-kb-to-12-mb-after-adding-a-few-libraries-what-do-you-do)
- [431: Scenario: a PrimeNG table with 5,000 rows and custom cell templates is slow. How do you improve it?](#431-scenario-a-primeng-table-with-5000-rows-and-custom-cell-templates-is-slow-how-do-you-improve-it)
- [432: Scenario: after upgrading Angular, a third-party date picker stops updating the UI until you click elsewhere. What is likely happening?](#432-scenario-after-upgrading-angular-a-third-party-date-picker-stops-updating-the-ui-until-you-click-elsewhere-what-is-likely-happening)
- [433: Scenario: users see raw translation keys for a moment when the app loads. How do you fix it?](#433-scenario-users-see-raw-translation-keys-for-a-moment-when-the-app-loads-how-do-you-fix-it)
- [434: Scenario: your NgRx effects start firing twice. What could cause it?](#434-scenario-your-ngrx-effects-start-firing-twice-what-could-cause-it)
- [435: Scenario: a Material dialog opened from a lazy-loaded route can't find a service provided in that route. Why?](#435-scenario-a-material-dialog-opened-from-a-lazy-loaded-route-cant-find-a-service-provided-in-that-route-why)
- [436: Scenario: you need to build an admin app quickly with lots of tables, forms and charts. Which libraries would you pick and why?](#436-scenario-you-need-to-build-an-admin-app-quickly-with-lots-of-tables-forms-and-charts-which-libraries-would-you-pick-and-why)
- [437: Scenario: your design team wants a custom look that doesn't match Material or PrimeNG. How do you build the UI layer?](#437-scenario-your-design-team-wants-a-custom-look-that-doesnt-match-material-or-primeng-how-do-you-build-the-ui-layer)
- [438: Scenario: you must support offline use for a field service app built with Angular. Which libraries help?](#438-scenario-you-must-support-offline-use-for-a-field-service-app-built-with-angular-which-libraries-help)
- [439: Scenario: a page with an embedded rich text editor leaks memory each time users navigate to it. How do you find and fix it?](#439-scenario-a-page-with-an-embedded-rich-text-editor-leaks-memory-each-time-users-navigate-to-it-how-do-you-find-and-fix-it)
- [440: Scenario: you need SSR for SEO, but a key library (a carousel) breaks on the server. What are your options?](#440-scenario-you-need-ssr-for-seo-but-a-key-library-a-carousel-breaks-on-the-server-what-are-your-options)
- [441: Scenario: your team uses both ngx-translate and @angular/localize in different parts of the app. Is that a problem?](#441-scenario-your-team-uses-both-ngx-translate-and-angularlocalize-in-different-parts-of-the-app-is-that-a-problem)
- [442: Scenario: a micro frontend built with an older Angular version must run inside a shell with a newer version. How do you approach it?](#442-scenario-a-micro-frontend-built-with-an-older-angular-version-must-run-inside-a-shell-with-a-newer-version-how-do-you-approach-it)
- [443: Scenario: you need to show 100,000 points on a map. Which approach would you use?](#443-scenario-you-need-to-show-100000-points-on-a-map-which-approach-would-you-use)
- [444: Scenario: your app uses Moment.js, lodash, jQuery and an old jQuery date picker. How would you plan modernization?](#444-scenario-your-app-uses-momentjs-lodash-jquery-and-an-old-jquery-date-picker-how-would-you-plan-modernization)
- [445: Scenario: two teams in a monorepo use different UI kits and the main app looks inconsistent. What do you do?](#445-scenario-two-teams-in-a-monorepo-use-different-ui-kits-and-the-main-app-looks-inconsistent-what-do-you-do)
- [446: Scenario: Lighthouse shows high Total Blocking Time after adding a charting library to the dashboard. How do you fix it?](#446-scenario-lighthouse-shows-high-total-blocking-time-after-adding-a-charting-library-to-the-dashboard-how-do-you-fix-it)
- [447: Scenario: you want to add analytics and A/B testing to an Angular app. What should you watch out for with these libraries?](#447-scenario-you-want-to-add-analytics-and-ab-testing-to-an-angular-app-what-should-you-watch-out-for-with-these-libraries)
- [448: Scenario: you are asked to make an existing Angular Material app work well for right-to-left languages. What is involved?](#448-scenario-you-are-asked-to-make-an-existing-angular-material-app-work-well-for-right-to-left-languages-what-is-involved)
- [449: Scenario: a third-party component library exposes only NgModules, and your app is fully standalone and zoneless. Can you still use it?](#449-scenario-a-third-party-component-library-exposes-only-ngmodules-and-your-app-is-fully-standalone-and-zoneless-can-you-still-use-it)
- [450: What does a healthy library strategy look like for a long-lived Angular project?](#450-what-does-a-healthy-library-strategy-look-like-for-a-long-lived-angular-project)

---

# Easy Questions (1-150)

## 1: What do people usually mean by "Angular libraries"?

Angular itself ships a lot of things in the box: router, forms, HTTP client, animations, i18n, service worker. "Angular libraries" usually means the extra npm packages people add on top of that: UI component kits, state management, translation, charts, data grids, auth clients, testing helpers and build tools.

Some of them are made by the Angular team (Angular Material, CDK, `@angular/google-maps`, `@angular/youtube-player`), and most are community or company projects (PrimeNG, NgRx, Transloco, AG Grid and so on).

## 2: What is Angular Material?

Angular Material is the official UI component library from the Angular team. It implements Google's Material Design (version 3 in current releases) and gives you ready components like buttons, inputs, selects, dialogs, tables, date pickers, menus, tabs and snack bars.

It is published as `@angular/material`, follows the same version numbers as Angular, and is updated together with Angular, so `ng update` handles both.

## 3: How do you add Angular Material to a project?

The easiest way is the `ng add` schematic:

```bash
ng add @angular/material
```

It installs `@angular/material` and `@angular/cdk`, asks you to pick a theme, adds the global styles and the Roboto font and Material Icons links to `index.html`. After that you import the components you need directly into your standalone components.

## 4: How do you use an Angular Material component in a standalone component?

You import the component (or its module) into the `imports` array of your component:

```ts
import { Component } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";

@Component({
  selector: "app-save-bar",
  imports: [MatButtonModule],
  template: `<button matButton="filled" (click)="save()">Save</button>`,
})
export class SaveBar {
  save() {
    console.log("saved");
  }
}
```

Each component lives in its own entry point (`@angular/material/button`, `@angular/material/dialog`, etc.), so you only ship what you import.

## 5: What is the Angular CDK?

The Component Dev Kit (`@angular/cdk`) is a set of low-level tools without any Material styling. Angular Material is built on top of it, but you can use it on its own to build your own components.

Common parts of the CDK:

- `overlay` for floating panels (dropdowns, tooltips, popups)
- `drag-drop` for drag and drop lists
- `scrolling` for virtual scrolling
- `a11y` for focus trapping, focus monitoring and screen reader announcements
- `layout` for `BreakpointObserver`
- `portal`, `table`, `stepper`, `menu`, `listbox`, `dialog`, `clipboard`

## 6: What is the difference between Angular Material and the CDK?

Angular Material gives you finished components with Material Design look and feel. The CDK gives you behavior only: positioning, keyboard handling, accessibility, drag and drop, virtual scroll. It has almost no styles.

If your design does not look like Material, a common approach is to use the CDK for the hard parts and write your own templates and CSS on top.

## 7: What is PrimeNG?

PrimeNG is a large open source UI library for Angular from PrimeTek. It has 80+ components, including many that Angular Material does not have, like a rich data table, tree table, charts, editor, file upload, organization chart, timeline and more.

It supports theming through design tokens and presets (Aura, Lara, Nora, Material) and also has an unstyled mode, so you can style it yourself with Tailwind or your own CSS.

## 8: What is NG-ZORRO?

NG-ZORRO (`ng-zorro-antd`) is the Angular version of the Ant Design system from Alibaba. It is popular for admin panels and enterprise dashboards. It has a big set of components (tables, forms, tree select, cascader, upload, etc.) and its version numbers track Angular versions.

You add it with `ng add ng-zorro-antd`.

## 9: What is ng-bootstrap?

ng-bootstrap (`@ng-bootstrap/ng-bootstrap`) provides Bootstrap components written as native Angular components and directives. It does not use Bootstrap's JavaScript or jQuery. You still include Bootstrap's CSS, and ng-bootstrap gives you things like modals, dropdowns, datepickers, tooltips, typeahead and accordions.

## 10: What is the difference between ng-bootstrap and ngx-bootstrap?

Both give you Bootstrap components for Angular without jQuery. They are separate projects with different teams and APIs:

- **ng-bootstrap** focuses on the latest Bootstrap version and is built around standalone components and services like `NgbModal`.
- **ngx-bootstrap** (from Valor Software) has supported several Bootstrap versions over time and has its own component set and API.

Pick one based on which Bootstrap version you use and which API your team prefers. Do not mix both in one app.

## 11: What is Taiga UI?

Taiga UI is an open source Angular UI kit made by T-Bank (formerly Tinkoff). It has a large set of components, a strong focus on customization and accessibility, and it is split into packages like `@taiga-ui/core`, `@taiga-ui/kit`, `@taiga-ui/cdk` and add-ons for charts, tables and more.

## 12: What is Spartan UI?

Spartan is an Angular UI library inspired by shadcn/ui from the React world. It is split into two layers:

- **brain**: unstyled, accessible building blocks (`@spartan-ng/brain`)
- **helm**: styled components built with Tailwind CSS that are copied into your project, so you own and can change the code

It is a good fit if you use Tailwind and want full control over markup and styles.

## 13: What is Ionic for Angular?

Ionic (`@ionic/angular`) is a UI toolkit for building mobile and desktop apps with web technologies. It gives you mobile-style components (tabs, lists, modals, action sheets, gestures) that adapt to iOS and Android styles. Combined with Capacitor, you can package the Angular app as a native iOS or Android app and use device APIs like the camera.

## 14: What is NgRx?

NgRx is the most popular state management library for Angular. It has several packages:

- `@ngrx/store`: a Redux-style global store with actions, reducers and selectors
- `@ngrx/effects`: side effects such as HTTP calls in response to actions
- `@ngrx/entity`: helpers for collections of records
- `@ngrx/signals`: SignalStore, a lighter signal-based store
- `@ngrx/router-store`, `@ngrx/store-devtools`, `@ngrx/operators`

## 15: What is NgRx SignalStore?

SignalStore (`@ngrx/signals`) is a newer, lighter store from the NgRx team built on Angular signals. You create a store with `signalStore()` and add features like state, computed values and methods. It needs much less boilerplate than the classic Store.

```ts
import { computed } from "@angular/core";
import {
  signalStore,
  withState,
  withComputed,
  withMethods,
  patchState,
} from "@ngrx/signals";

export const CounterStore = signalStore(
  { providedIn: "root" },
  withState({ count: 0 }),
  withComputed(({ count }) => ({
    double: computed(() => count() * 2),
  })),
  withMethods((store) => ({
    increment() {
      patchState(store, { count: store.count() + 1 });
    },
  })),
);
```

## 16: What is NGXS?

NGXS is another state management library for Angular. It uses classes and decorators: a state class with `@State`, methods decorated with `@Action`, and static selectors with `@Selector`. Many people find it shorter than classic NgRx because there are no separate reducer and effect files. Async work is done right inside the action handler.

## 17: What is Akita and is it still used?

Akita was a state management library from Datorama (Salesforce) based on stores and queries. It is no longer actively developed and its authors recommend moving to Elf or other options. You may still see it in older codebases, but you should not pick it for new projects.

## 18: What is Elf?

Elf (`@ngneat/elf`) is a small reactive state management library built on RxJS. It is framework agnostic but popular in Angular. You create a store with `createStore()` and add features like `withProps`, `withEntities` or `withRequestsStatus`, and you read data as observables.

```ts
import { createStore, withProps, select } from "@ngneat/elf";

interface AuthProps {
  user: { name: string } | null;
}

const authStore = createStore(
  { name: "auth" },
  withProps<AuthProps>({ user: null }),
);

export const user$ = authStore.pipe(select((state) => state.user));

export function setUser(user: AuthProps["user"]) {
  authStore.update((state) => ({ ...state, user }));
}
```

## 19: What is TanStack Query for Angular?

TanStack Query (formerly React Query) has an Angular adapter, `@tanstack/angular-query-experimental`. It handles server state: fetching, caching, background refetching, retries and invalidation. Results are exposed as signals, which fits modern Angular well.

As the package name says, it is still marked experimental, so breaking changes can happen in minor versions. Pin the version if you use it in production.

## 20: What is ngx-translate?

ngx-translate (`@ngx-translate/core`) is one of the oldest and most used runtime translation libraries for Angular. You keep translations in JSON files, load them at runtime, and switch language without reloading the page. You translate with the `translate` pipe, the `translate` directive or the `TranslateService`.

## 21: What is Transloco?

Transloco (`@jsverse/transloco`) is a modern runtime i18n library for Angular. Like ngx-translate, it loads JSON translations at runtime and lets you switch language on the fly. It also has extra features like lazy loaded translation scopes, a structural directive that gives you a `t()` function in templates, plugins for message format, locale formatting and persisting the chosen language.

## 22: What is @angular/localize?

`@angular/localize` is Angular's built-in i18n solution. You mark text with the `i18n` attribute in templates or with `$localize` in code, extract it with `ng extract-i18n`, translate the files (XLIFF, JSON and others), and build one version of the app per language.

```html
<h1 i18n="@@welcomeTitle">Welcome!</h1>
```

```ts
const message = $localize`:@@saved:Saved successfully`;
```

## 23: What is the main difference between @angular/localize and runtime i18n libraries?

`@angular/localize` translates at build time. Each language is a separate build, which gives the best runtime speed, but switching language means loading another build (another URL).

ngx-translate and Transloco translate at runtime. You have one build, translations are loaded as JSON, and you can switch language instantly without a reload. The cost is a small runtime overhead and keys in your templates instead of plain text.

## 24: What is Apollo Angular?

Apollo Angular (`apollo-angular`) is the Angular integration of Apollo Client for GraphQL. It gives you an `Apollo` service to run queries, mutations and subscriptions, a normalized cache (`InMemoryCache`) and an `HttpLink` that uses Angular's `HttpClient`, so your interceptors still work.

## 25: What is AngularFire?

AngularFire (`@angular/fire`) is the official Angular library for Firebase. It wraps the Firebase JS SDK and gives you providers like `provideFirebaseApp`, `provideAuth`, `provideFirestore`, `provideStorage` and helpers that return observables, such as `collectionData` and `authState`.

## 26: What is AG Grid?

AG Grid is a feature-rich JavaScript data grid with a first-class Angular component (`ag-grid-angular`). It handles sorting, filtering, pagination, row grouping, cell editing, virtual rows and columns, and can show hundreds of thousands of rows smoothly.

There is a free Community edition (MIT) and a paid Enterprise edition with features like row grouping with aggregation, pivoting, Excel export and server-side row model.

## 27: Which libraries are popular for charts in Angular?

- **ng2-charts**: Angular wrapper around Chart.js
- **ngx-echarts**: wrapper around Apache ECharts, good for big and complex charts
- **@swimlane/ngx-charts**: charts built with Angular and D3, rendered as SVG
- **highcharts-angular**: official wrapper for Highcharts (commercial license for business use)
- **PrimeNG Chart**: a Chart.js based component if you already use PrimeNG
- **AG Charts**: from the AG Grid team

## 28: What is Formly?

Formly (`@ngx-formly/core`) builds Angular reactive forms from a JSON-like configuration. Instead of writing every input in the template, you describe fields as an array of objects with type, key, label and validators, and Formly renders them. It has UI packages for Material, Bootstrap, PrimeNG, NG-ZORRO and others.

It is useful for dynamic forms, for example when the form structure comes from the server.

## 29: What is ngx-mask?

ngx-mask is a directive and pipe for input masks, for example phone numbers, dates, credit cards or postal codes. You set a pattern like `(000) 000-0000` and the input formats what the user types.

```html
<input type="text" mask="(000) 000-0000" [formControl]="phone" />
```

## 30: What is ng-select?

`@ng-select/ng-select` is a select/autocomplete component. It supports search, multi-select, tags, grouping, virtual scroll, custom templates and async loading. It works with both reactive and template-driven forms.

```html
<ng-select
  [items]="cities"
  bindLabel="name"
  bindValue="id"
  [multiple]="true"
  [(ngModel)]="selectedCityIds"
/>
```

## 31: What is ngx-toastr?

ngx-toastr shows toast notifications (small pop-up messages) for success, error, info and warning. You register it with `provideToastr()` and `provideAnimations()` (or the newer animation setup), then inject `ToastrService`:

```ts
import { inject } from "@angular/core";
import { ToastrService } from "ngx-toastr";

export class ProfilePage {
  private toastr = inject(ToastrService);

  onSaved() {
    this.toastr.success("Profile updated", "Done");
  }
}
```

## 32: What is Angular Material's MatSnackBar?

`MatSnackBar` is Material's built-in way to show short messages at the bottom (or top) of the screen. You inject the service and call `open()`:

```ts
import { inject } from "@angular/core";
import { MatSnackBar } from "@angular/material/snack-bar";

export class OrdersPage {
  private snackBar = inject(MatSnackBar);

  showSaved() {
    this.snackBar.open("Order saved", "Undo", { duration: 3000 });
  }
}
```

If you already use Material, you usually do not need a separate toast library.

## 33: What is Spectator?

Spectator (`@ngneat/spectator`) is a testing library that removes a lot of `TestBed` boilerplate. You create a factory once, and it gives you a `spectator` object with helpers to query elements, trigger events, set inputs and get services.

```ts
import { createComponentFactory, Spectator } from "@ngneat/spectator/jest";
import { Counter } from "./counter";

describe("Counter", () => {
  let spectator: Spectator<Counter>;
  const createComponent = createComponentFactory(Counter);

  beforeEach(() => (spectator = createComponent()));

  it("increments on click", () => {
    spectator.click("button");
    expect(spectator.query("span")).toHaveText("1");
  });
});
```

## 34: What is ng-mocks?

ng-mocks is a testing library that creates mocks of components, directives, pipes, services and modules. It helps you test a component in isolation without rendering its real children. The main helpers are `MockComponent`, `MockProvider`, `MockBuilder`, `MockRender` and `ngMocks`.

## 35: What is Angular Testing Library?

Angular Testing Library (`@testing-library/angular`) is the Angular version of Testing Library. Its idea is to test components the way a user uses them: find elements by role, label or text, click and type, and check what is on the screen, instead of checking internal component state.

```ts
import { render, screen } from "@testing-library/angular";
import userEvent from "@testing-library/user-event";
import { Counter } from "./counter";

it("shows the new count after click", async () => {
  await render(Counter);
  await userEvent.click(screen.getByRole("button", { name: /increment/i }));
  expect(screen.getByText("Count: 1")).toBeTruthy();
});
```

## 36: Which test runners are used with Angular?

- **Vitest**: the default for new projects in recent Angular CLI versions, run through the `@angular/build:unit-test` builder
- **Jasmine + Karma**: the old default. Karma is deprecated, but many existing projects still use it
- **Jest**: very popular, usually set up with `jest-preset-angular` or through Nx
- **Web Test Runner**: an experimental option in the CLI

For end-to-end tests, Cypress and Playwright are the common choices.

## 37: What is Cypress?

Cypress is a testing tool for end-to-end and component tests that runs in a real browser. In Angular you can add it with `ng add @cypress/schematic`. It is popular because of its interactive runner, time-travel debugging and simple API (`cy.visit`, `cy.get`, `cy.contains`).

## 38: What is Playwright?

Playwright is an end-to-end testing framework from Microsoft. It drives Chromium, Firefox and WebKit, runs tests in parallel, waits for elements automatically, and has tools like trace viewer and codegen. Many Angular teams moved from Protractor (now removed) to Playwright or Cypress.

## 39: What happened to Protractor?

Protractor was Angular's original end-to-end test tool. It reached end of life in 2023 and is no longer maintained. New projects do not get an e2e setup by default. You choose one yourself, usually Playwright or Cypress, both of which have Angular schematics.

## 40: What is Nx?

Nx is a build system and monorepo tool from Nrwl. It is very popular in Angular projects. It lets you keep many apps and libraries in one repository, runs only the tasks affected by a change, caches build and test results (locally and remotely), and enforces module boundaries between libraries. It also has generators for Angular, NgRx, Jest, Cypress, Storybook and more.

## 41: What is angular-eslint?

angular-eslint is the set of ESLint plugins and tools for Angular projects. It gives you Angular-specific lint rules for TypeScript (like using the right selector prefix or not using lifecycle methods wrongly) and for templates (like accessibility rules). TSLint is long gone, so this is the standard linter.

```bash
ng add angular-eslint
ng lint
```

## 42: What is Storybook used for in Angular?

Storybook (`@storybook/angular`) lets you build and view components in isolation, outside your app. Each "story" shows a component in a specific state (for example a disabled button or an empty table). Teams use it for design systems, visual review, documentation and visual regression tests.

## 43: What is Analog?

Analog (`@analogjs/platform`) is a meta-framework for Angular, similar to what Next.js is for React. It uses Vite, gives you file-based routing, API routes, server-side rendering and static site generation, and also supports Markdown content. Its Vitest integration is used even in projects that are not built with Analog.

## 44: What is Native Federation?

Native Federation (`@angular-architects/native-federation`) is a library for micro frontends in Angular. It follows the ideas of Webpack Module Federation, but works with any bundler, including the esbuild-based Angular CLI builder, using browser-native features like import maps and ES modules. It lets a shell app load remote apps at runtime.

## 45: What is ngxtension?

ngxtension is a community collection of small utilities for modern Angular. It has helpers like `injectParams`, `injectQueryParams`, `derivedAsync`, `connect`, `signalSlice`, `injectLocalStorage`, `createInjectionToken` and many more. Each utility is a separate entry point, so you only bundle what you import.

## 46: What is RxAngular?

RxAngular (`@rx-angular/*`) is a set of libraries focused on performance and reactive code:

- `@rx-angular/template`: directives like `rxLet`, `rxFor` and `rxIf` that render observables or signals with fine-grained updates
- `@rx-angular/state`: a small reactive component state helper
- `@rx-angular/cdk`: tools like render strategies and a concurrent scheduler

It was popular for zone-less and high-performance apps before Angular had signals and built-in zoneless support.

## 47: What is ngx-infinite-scroll?

ngx-infinite-scroll is a directive that emits an event when the user scrolls close to the end of a list, so you can load the next page.

```html
<div infiniteScroll [infiniteScrollDistance]="2" (scrolled)="loadMore()">
  @for (item of items(); track item.id) {
  <app-item [item]="item" />
  }
</div>
```

## 48: What is ngx-cookie-service?

ngx-cookie-service gives you a `CookieService` to read, set and delete browser cookies with a simple API:

```ts
const cookies = inject(CookieService);
cookies.set("theme", "dark", { expires: 30, path: "/" });
const theme = cookies.get("theme");
cookies.delete("theme", "/");
```

It also has an SSR version (`ngx-cookie-service-ssr`) that reads cookies from the server request.

## 49: What is ngx-markdown?

ngx-markdown renders Markdown in Angular using marked. It can load Markdown from a string or a file, and optionally adds syntax highlighting (Prism), math (KaTeX), diagrams (Mermaid) and emoji.

```html
<markdown [data]="readme" /> <markdown src="assets/docs/intro.md" />
```

## 50: What is @angular/google-maps?

`@angular/google-maps` is an official Angular component package (from the Angular components team) that wraps the Google Maps JavaScript API. You get components like `<google-map>`, `<map-advanced-marker>`, `<map-info-window>`, `<map-polyline>` and others.

```html
<google-map height="400px" width="100%" [center]="center" [zoom]="12">
  <map-advanced-marker [position]="center" title="Office" />
</google-map>
```

You still need to load the Google Maps script with your API key.

## 51: What is @angular/youtube-player?

`@angular/youtube-player` is an official component that wraps the YouTube IFrame API. You pass a video ID and get a player with inputs for size and player options, plus outputs for events like `stateChange` and `ready`.

```html
<youtube-player videoId="dQw4w9WgXcQ" [width]="640" [height]="360" />
```

## 52: What is the purpose of `ng add` for libraries?

`ng add <package>` installs a library and runs its setup schematic if the library has one. The schematic can add providers to `app.config.ts`, add styles to `angular.json`, update `index.html` and so on. For example, `ng add @angular/material`, `ng add @ngrx/store`, `ng add @jsverse/transloco`.

If a library has no schematic, `ng add` just installs it, the same as `npm install`.

## 53: What does `ng update` do for libraries?

`ng update` updates Angular packages and also libraries that support it. Libraries can ship migration schematics that rewrite your code when an API changes. For example:

```bash
ng update @angular/core @angular/cli @angular/material
ng update @ngrx/store
```

Running `ng update` with no arguments lists the packages that have updates available.

## 54: What is a provider function like provideXxx()?

In standalone Angular, libraries expose functions such as `provideStore()`, `provideToastr()`, `provideTransloco()` or `provideCharts()` that return the providers the library needs. You add them to the `providers` array in `app.config.ts`.

```ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient } from "@angular/common/http";
import { provideToastr } from "ngx-toastr";

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient(), provideToastr({ timeOut: 3000 })],
};
```

This replaced the older `SomeModule.forRoot()` pattern.

## 55: What do you do if a library only has an NgModule with forRoot()?

You can still use it in a standalone app with `importProvidersFrom()`:

```ts
import { ApplicationConfig, importProvidersFrom } from "@angular/core";
import { FormlyModule } from "@ngx-formly/core";

export const appConfig: ApplicationConfig = {
  providers: [importProvidersFrom(FormlyModule.forRoot())],
};
```

For components and directives from such a library, you import the NgModule into the `imports` array of your standalone component.

## 56: How do you add a Material icon?

Import `MatIconModule` and use `<mat-icon>` with the icon name. By default it uses the Material Icons font, which `ng add` links in `index.html`.

```html
<mat-icon>home</mat-icon>
<mat-icon fontSet="material-symbols-outlined">settings</mat-icon>
```

You can also register your own SVG icons with `MatIconRegistry`.

## 57: How do you open a dialog with Angular Material?

Inject `MatDialog` and call `open()` with the component you want to show:

```ts
import { Component, inject } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { ConfirmDialog } from "./confirm-dialog";

@Component({
  selector: "app-user-row",
  template: `<button (click)="remove()">Delete</button>`,
})
export class UserRow {
  private dialog = inject(MatDialog);

  remove() {
    const ref = this.dialog.open(ConfirmDialog, { data: { name: "Anna" } });
    ref.afterClosed().subscribe((confirmed) => {
      if (confirmed) {
        console.log("deleting");
      }
    });
  }
}
```

## 58: How do you read data passed into a Material dialog?

Inject `MAT_DIALOG_DATA` inside the dialog component, and `MatDialogRef` to close it with a result:

```ts
import { Component, inject } from "@angular/core";
import {
  MAT_DIALOG_DATA,
  MatDialogModule,
  MatDialogRef,
} from "@angular/material/dialog";

@Component({
  selector: "app-confirm-dialog",
  imports: [MatDialogModule],
  template: `
    <h2 mat-dialog-title>Delete {{ data.name }}?</h2>
    <mat-dialog-actions>
      <button mat-dialog-close>Cancel</button>
      <button (click)="ref.close(true)">Delete</button>
    </mat-dialog-actions>
  `,
})
export class ConfirmDialog {
  data = inject<{ name: string }>(MAT_DIALOG_DATA);
  ref = inject(MatDialogRef<ConfirmDialog, boolean>);
}
```

## 59: What is mat-form-field?

`<mat-form-field>` is a wrapper around an input that adds a label, hint, error messages, prefix and suffix, and the Material look (fill or outline appearance).

```html
<mat-form-field appearance="outline">
  <mat-label>Email</mat-label>
  <input matInput type="email" [formControl]="email" />
  <mat-hint>We never share it</mat-hint>
  @if (email.hasError('required')) {
  <mat-error>Email is required</mat-error>
  }
</mat-form-field>
```

## 60: What is mat-table?

`mat-table` is Material's data table. You give it a data source and define each column with `matColumnDef`, then list which columns to show in the header and row definitions.

```html
<table mat-table [dataSource]="users">
  <ng-container matColumnDef="name">
    <th mat-header-cell *matHeaderCellDef>Name</th>
    <td mat-cell *matCellDef="let user">{{ user.name }}</td>
  </ng-container>

  <ng-container matColumnDef="email">
    <th mat-header-cell *matHeaderCellDef>Email</th>
    <td mat-cell *matCellDef="let user">{{ user.email }}</td>
  </ng-container>

  <tr mat-header-row *matHeaderRowDef="['name', 'email']"></tr>
  <tr mat-row *matRowDef="let row; columns: ['name', 'email']"></tr>
</table>
```

## 61: How do you add sorting and pagination to mat-table?

Use `MatTableDataSource` together with `MatSort` and `MatPaginator`:

```ts
import { Component, viewChild, effect } from "@angular/core";
import { MatTableDataSource, MatTableModule } from "@angular/material/table";
import { MatSort, MatSortModule } from "@angular/material/sort";
import { MatPaginator, MatPaginatorModule } from "@angular/material/paginator";

@Component({
  selector: "app-users-table",
  imports: [MatTableModule, MatSortModule, MatPaginatorModule],
  templateUrl: "./users-table.html",
})
export class UsersTable {
  dataSource = new MatTableDataSource<{ name: string; age: number }>([]);
  sort = viewChild.required(MatSort);
  paginator = viewChild.required(MatPaginator);

  constructor() {
    effect(() => {
      this.dataSource.sort = this.sort();
      this.dataSource.paginator = this.paginator();
    });
  }
}
```

In the template you add `matSort` on the table, `mat-sort-header` on header cells and `<mat-paginator [pageSizeOptions]="[10, 25, 50]" />` below it. This works on the client. For server-side paging you listen to the `sortChange` and `page` events and load data yourself.

## 62: How do you use the Material date picker?

You need a date adapter. The simplest is the native one:

```ts
import { provideNativeDateAdapter } from "@angular/material/core";

export const appConfig = {
  providers: [provideNativeDateAdapter()],
};
```

```html
<mat-form-field>
  <mat-label>Birthday</mat-label>
  <input matInput [matDatepicker]="picker" [formControl]="birthday" />
  <mat-datepicker-toggle matIconSuffix [for]="picker" />
  <mat-datepicker #picker />
</mat-form-field>
```

There are also adapters for date-fns, Luxon and Moment if you need better parsing and locale support.

## 63: What is the CDK drag and drop module?

`@angular/cdk/drag-drop` lets you make elements draggable and reorder lists. You put `cdkDropList` on the container, `cdkDrag` on each item, and handle the `cdkDropListDropped` event.

```ts
import { Component, signal } from "@angular/core";
import {
  CdkDrag,
  CdkDragDrop,
  CdkDropList,
  moveItemInArray,
} from "@angular/cdk/drag-drop";

@Component({
  selector: "app-todo-list",
  imports: [CdkDropList, CdkDrag],
  template: `
    <ul cdkDropList (cdkDropListDropped)="drop($event)">
      @for (task of tasks(); track task) {
        <li cdkDrag>{{ task }}</li>
      }
    </ul>
  `,
})
export class TodoList {
  tasks = signal(["Write tests", "Review PR", "Deploy"]);

  drop(event: CdkDragDrop<string[]>) {
    this.tasks.update((list) => {
      const copy = [...list];
      moveItemInArray(copy, event.previousIndex, event.currentIndex);
      return copy;
    });
  }
}
```

## 64: What is virtual scrolling in the CDK?

Virtual scrolling renders only the items that are visible on the screen, instead of all of them. This keeps the DOM small even with thousands of items.

```html
<cdk-virtual-scroll-viewport itemSize="48" class="h-[400px]">
  <div *cdkVirtualFor="let user of users" class="row">{{ user.name }}</div>
</cdk-virtual-scroll-viewport>
```

`itemSize` is the height of one row in pixels. The viewport needs a fixed height.

## 65: What is BreakpointObserver?

`BreakpointObserver` from `@angular/cdk/layout` tells you when media queries match, so you can change layout in code. It has predefined breakpoints in `Breakpoints`.

```ts
import { inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { BreakpointObserver, Breakpoints } from "@angular/cdk/layout";
import { map } from "rxjs";

export class Shell {
  private bo = inject(BreakpointObserver);

  isHandset = toSignal(
    this.bo.observe(Breakpoints.Handset).pipe(map((result) => result.matches)),
    { initialValue: false },
  );
}
```

## 66: What does the CDK Clipboard do?

`@angular/cdk/clipboard` copies text to the clipboard. You can use the `cdkCopyToClipboard` directive or the `Clipboard` service.

```html
<button [cdkCopyToClipboard]="apiKey">Copy key</button>
```

```ts
const clipboard = inject(Clipboard);
clipboard.copy("some text");
```

## 67: What is cdkTextareaAutosize?

It is a directive from `@angular/cdk/text-field` that makes a `<textarea>` grow and shrink with its content.

```html
<textarea
  cdkTextareaAutosize
  cdkAutosizeMinRows="2"
  cdkAutosizeMaxRows="8"
></textarea>
```

## 68: What is a theme in Angular Material?

A theme defines the colors, typography and density used by all Material components. In current versions you define it with the `mat.theme` Sass mixin, which outputs CSS variables (system tokens like `--mat-sys-primary`):

```scss
@use "@angular/material" as mat;

html {
  color-scheme: light dark;
  @include mat.theme(
    (
      color: mat.$violet-palette,
      typography: Roboto,
      density: 0,
    )
  );
}
```

With `color-scheme: light dark`, the theme follows the user's OS light or dark mode.

## 69: How do you install PrimeNG?

Install PrimeNG and a theme package, then register it with `providePrimeNG`:

```bash
npm install primeng @primeuix/themes
```

```ts
import { ApplicationConfig } from "@angular/core";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";
import { providePrimeNG } from "primeng/config";
import Aura from "@primeuix/themes/aura";

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimationsAsync(),
    providePrimeNG({ theme: { preset: Aura } }),
  ],
};
```

Older PrimeNG versions used CSS theme files and later `@primeng/themes`. You will see both in existing projects.

## 70: How do you use a PrimeNG component?

Import the component from its entry point and use it in the template:

```ts
import { Component } from "@angular/core";
import { ButtonModule } from "primeng/button";
import { InputTextModule } from "primeng/inputtext";

@Component({
  selector: "app-search",
  imports: [ButtonModule, InputTextModule],
  template: `
    <input pInputText placeholder="Search" />
    <p-button label="Go" icon="pi pi-search" />
  `,
})
export class Search {}
```

Icons come from the `primeicons` package.

## 71: What is ng-bootstrap's NgbModal?

`NgbModal` is a service for opening modal windows:

```ts
import { inject } from "@angular/core";
import { NgbModal } from "@ng-bootstrap/ng-bootstrap";
import { EditUserModal } from "./edit-user-modal";

export class UsersPage {
  private modal = inject(NgbModal);

  edit() {
    const ref = this.modal.open(EditUserModal, { size: "lg" });
    ref.componentInstance.userId = 42;
    ref.result.then(
      (result) => console.log("closed", result),
      () => console.log("dismissed"),
    );
  }
}
```

Inside the modal component you inject `NgbActiveModal` and call `close()` or `dismiss()`.

## 72: Do you need Bootstrap's JavaScript when you use ng-bootstrap?

No. ng-bootstrap rewrites all interactive parts (modals, dropdowns, collapse, tooltips) as Angular code. You only need Bootstrap's CSS. Adding `bootstrap.bundle.js` as well can cause conflicts, like a dropdown toggled twice.

## 73: How do you install ngx-translate in a standalone app?

```bash
npm install @ngx-translate/core @ngx-translate/http-loader
```

```ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient } from "@angular/common/http";
import { provideTranslateService } from "@ngx-translate/core";
import { provideTranslateHttpLoader } from "@ngx-translate/http-loader";

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    provideTranslateService({
      loader: provideTranslateHttpLoader({ prefix: "/i18n/", suffix: ".json" }),
      fallbackLang: "en",
    }),
  ],
};
```

Translation files then live in `public/i18n/en.json`, `public/i18n/de.json` and so on. Older versions used `TranslateModule.forRoot()` with a loader factory.

## 74: How do you translate text with ngx-translate?

With the pipe, the directive or the service:

```html
<h1>{{ 'home.title' | translate }}</h1>
<p>{{ 'home.greeting' | translate: { name: user.name } }}</p>
<span [translate]="'home.subtitle'"></span>
```

```ts
const translate = inject(TranslateService);
const label = translate.instant("home.title");
translate.get("home.title").subscribe((text) => console.log(text));
```

You need to import `TranslatePipe` (or `TranslateDirective`) in the component.

## 75: How do you change the language with ngx-translate?

Call `use()` on `TranslateService`. It loads the file if needed and updates all `translate` pipes.

```ts
const translate = inject(TranslateService);
translate.use("de");
```

## 76: How do you install Transloco?

The easiest way is the schematic:

```bash
ng add @jsverse/transloco
```

It creates a loader and adds the config:

```ts
import { provideTransloco } from "@jsverse/transloco";
import { TranslocoHttpLoader } from "./transloco-loader";

export const appConfig = {
  providers: [
    provideHttpClient(),
    provideTransloco({
      config: {
        availableLangs: ["en", "es"],
        defaultLang: "en",
        reRenderOnLangChange: true,
        prodMode: !isDevMode(),
      },
      loader: TranslocoHttpLoader,
    }),
  ],
};
```

Older code imports from `@ngneat/transloco`. The package moved to `@jsverse/transloco`.

## 77: How do you translate in a template with Transloco?

Transloco has three options. The structural directive is the recommended one because it creates one subscription for the whole block:

```html
<ng-container *transloco="let t">
  <h1>{{ t('home.title') }}</h1>
  <p>{{ t('home.greeting', { name: userName }) }}</p>
</ng-container>

<span>{{ 'home.title' | transloco }}</span>
<span transloco="home.title"></span>
```

Import `TranslocoDirective` or `TranslocoPipe` in the component.

## 78: How do you translate in TypeScript with Transloco?

Inject `TranslocoService`:

```ts
const transloco = inject(TranslocoService);

// sync, works only if the language file is already loaded
const title = transloco.translate("home.title");

// async, waits for the file
transloco.selectTranslate("home.title").subscribe((text) => console.log(text));

// switch language
transloco.setActiveLang("es");
```

## 79: How do you add an NgRx store to a standalone app?

```bash
ng add @ngrx/store
ng add @ngrx/effects
ng add @ngrx/store-devtools
```

```ts
import { ApplicationConfig, isDevMode } from "@angular/core";
import { provideStore, provideState } from "@ngrx/store";
import { provideEffects } from "@ngrx/effects";
import { provideStoreDevtools } from "@ngrx/store-devtools";
import { booksFeature } from "./books/books.feature";
import * as booksEffects from "./books/books.effects";

export const appConfig: ApplicationConfig = {
  providers: [
    provideStore(),
    provideState(booksFeature),
    provideEffects(booksEffects),
    provideStoreDevtools({ maxAge: 25, logOnly: !isDevMode() }),
  ],
};
```

## 80: What are Redux DevTools and how do they help with NgRx?

Redux DevTools is a browser extension that shows every dispatched action, the state before and after it, and a diff. You can jump back to an earlier state ("time travel") and export or import state. NgRx connects to it through `provideStoreDevtools()`. NGXS and Elf also have devtools plugins.

## 81: How do you install NGXS?

```bash
ng add @ngxs/store
```

```ts
import { provideStore } from "@ngxs/store";
import { withNgxsReduxDevtoolsPlugin } from "@ngxs/devtools-plugin";
import { TodosState } from "./todos.state";

export const appConfig = {
  providers: [provideStore([TodosState], withNgxsReduxDevtoolsPlugin())],
};
```

Note that both NgRx and NGXS export a function named `provideStore`. They come from different packages and are not related.

## 82: What does a basic NGXS state look like?

```ts
import { Injectable } from "@angular/core";
import { Action, Selector, State, StateContext } from "@ngxs/store";

export class AddTodo {
  static readonly type = "[Todos] Add";
  constructor(public title: string) {}
}

export interface TodosModel {
  items: string[];
}

@State<TodosModel>({ name: "todos", defaults: { items: [] } })
@Injectable()
export class TodosState {
  @Selector()
  static items(state: TodosModel) {
    return state.items;
  }

  @Action(AddTodo)
  add(ctx: StateContext<TodosModel>, action: AddTodo) {
    ctx.setState({ items: [...ctx.getState().items, action.title] });
  }
}
```

In a component you call `store.dispatch(new AddTodo('Buy milk'))` and read with `store.selectSignal(TodosState.items)`.

## 83: How do you set up TanStack Query in Angular?

```bash
npm install @tanstack/angular-query-experimental
```

```ts
import { ApplicationConfig } from "@angular/core";
import { provideHttpClient } from "@angular/common/http";
import {
  provideTanStackQuery,
  QueryClient,
} from "@tanstack/angular-query-experimental";

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient(), provideTanStackQuery(new QueryClient())],
};
```

## 84: How do you fetch data with injectQuery?

```ts
import { Component, inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { injectQuery } from "@tanstack/angular-query-experimental";
import { lastValueFrom } from "rxjs";

interface Todo {
  id: number;
  title: string;
}

@Component({
  selector: "app-todos",
  template: `
    @if (todos.isPending()) {
      <p>Loading...</p>
    } @else if (todos.isError()) {
      <p>Error: {{ todos.error()?.message }}</p>
    } @else {
      @for (todo of todos.data(); track todo.id) {
        <p>{{ todo.title }}</p>
      }
    }
  `,
})
export class Todos {
  private http = inject(HttpClient);

  todos = injectQuery(() => ({
    queryKey: ["todos"],
    queryFn: () => lastValueFrom(this.http.get<Todo[]>("/api/todos")),
  }));
}
```

All fields like `data`, `isPending` and `error` are signals.

## 85: How do you install Apollo Angular?

```bash
ng add apollo-angular
```

This installs `apollo-angular`, `@apollo/client` and `graphql`, and creates a config like this:

```ts
import { inject } from "@angular/core";
import { provideHttpClient } from "@angular/common/http";
import { provideApollo } from "apollo-angular";
import { HttpLink } from "apollo-angular/http";
import { InMemoryCache } from "@apollo/client/core";

export const appConfig = {
  providers: [
    provideHttpClient(),
    provideApollo(() => {
      const httpLink = inject(HttpLink);
      return {
        link: httpLink.create({ uri: "/graphql" }),
        cache: new InMemoryCache(),
      };
    }),
  ],
};
```

## 86: How do you run a GraphQL query with Apollo Angular?

```ts
import { Component, inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { Apollo, gql } from "apollo-angular";
import { map } from "rxjs";

const GET_BOOKS = gql`
  query GetBooks {
    books {
      id
      title
    }
  }
`;

@Component({
  selector: "app-books",
  template: `
    @for (book of books(); track book.id) {
      <p>{{ book.title }}</p>
    }
  `,
})
export class Books {
  private apollo = inject(Apollo);

  books = toSignal(
    this.apollo
      .watchQuery<{ books: { id: string; title: string }[] }>({
        query: GET_BOOKS,
      })
      .valueChanges.pipe(map((result) => result.data.books)),
    { initialValue: [] },
  );
}
```

`watchQuery` keeps listening to the cache. Use `query()` if you need the result only once.

## 87: How do you set up AngularFire?

```bash
ng add @angular/fire
```

```ts
import { provideFirebaseApp, initializeApp } from "@angular/fire/app";
import { provideAuth, getAuth } from "@angular/fire/auth";
import { provideFirestore, getFirestore } from "@angular/fire/firestore";
import { environment } from "../environments/environment";

export const appConfig = {
  providers: [
    provideFirebaseApp(() => initializeApp(environment.firebase)),
    provideAuth(() => getAuth()),
    provideFirestore(() => getFirestore()),
  ],
};
```

## 88: How do you read a Firestore collection with AngularFire?

```ts
import { Component, inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { Firestore, collection, collectionData } from "@angular/fire/firestore";

interface Note {
  id: string;
  text: string;
}

@Component({
  selector: "app-notes",
  template: `
    @for (note of notes(); track note.id) {
      <p>{{ note.text }}</p>
    }
  `,
})
export class Notes {
  private firestore = inject(Firestore);

  notes = toSignal(
    collectionData(collection(this.firestore, "notes"), { idField: "id" }),
    { initialValue: [] as Note[] },
  );
}
```

The observable emits a new array every time the collection changes on the server.

## 89: How do you show a basic AG Grid table?

```ts
import { Component } from "@angular/core";
import { AgGridAngular } from "ag-grid-angular";
import { AllCommunityModule, ColDef, ModuleRegistry } from "ag-grid-community";

ModuleRegistry.registerModules([AllCommunityModule]);

interface Car {
  make: string;
  model: string;
  price: number;
}

@Component({
  selector: "app-cars",
  imports: [AgGridAngular],
  template: `
    <ag-grid-angular
      style="height: 400px"
      [rowData]="rowData"
      [columnDefs]="colDefs"
    />
  `,
})
export class Cars {
  rowData: Car[] = [
    { make: "Tesla", model: "Model Y", price: 64950 },
    { make: "Ford", model: "F-Series", price: 33850 },
  ];

  colDefs: ColDef<Car>[] = [
    { field: "make", filter: true },
    { field: "model" },
    { field: "price", sortable: true },
  ];
}
```

Recent AG Grid versions require you to register modules. `AllCommunityModule` is the simplest option, but registering only the modules you use makes the bundle smaller.

## 90: How do you show a chart with ng2-charts?

```ts
import { ApplicationConfig } from "@angular/core";
import { provideCharts, withDefaultRegisterables } from "ng2-charts";

export const appConfig: ApplicationConfig = {
  providers: [provideCharts(withDefaultRegisterables())],
};
```

```ts
import { Component } from "@angular/core";
import { BaseChartDirective } from "ng2-charts";
import { ChartData } from "chart.js";

@Component({
  selector: "app-sales-chart",
  imports: [BaseChartDirective],
  template: `<canvas baseChart type="bar" [data]="data"></canvas>`,
})
export class SalesChart {
  data: ChartData<"bar"> = {
    labels: ["Jan", "Feb", "Mar"],
    datasets: [{ label: "Sales", data: [120, 150, 90] }],
  };
}
```

`withDefaultRegisterables()` registers all Chart.js parts. You can register only the ones you need to save bundle size.

## 91: How do you set up ngx-echarts?

```bash
npm install echarts ngx-echarts
```

```ts
import { provideEchartsCore } from "ngx-echarts";

export const appConfig = {
  providers: [provideEchartsCore({ echarts: () => import("echarts") })],
};
```

```html
<div echarts [options]="chartOptions" class="h-80"></div>
```

Passing a function that imports `echarts` lazy loads the library, which is large. Import `NgxEchartsDirective` in the component.

## 92: What is @swimlane/ngx-charts?

ngx-charts is a chart library that uses Angular for rendering SVG and D3 only for math (scales, shapes). It has bar, line, area, pie, gauge, heat map, tree map and other charts. Because it renders with Angular, charts are easy to style with CSS, but it can be slower than canvas-based libraries with a lot of data points.

## 93: How do you define a simple Formly form?

```ts
import { Component } from "@angular/core";
import { FormGroup, ReactiveFormsModule } from "@angular/forms";
import { FormlyFieldConfig, FormlyModule } from "@ngx-formly/core";

@Component({
  selector: "app-signup",
  imports: [ReactiveFormsModule, FormlyModule],
  template: `
    <form [formGroup]="form" (ngSubmit)="submit()">
      <formly-form [form]="form" [fields]="fields" [model]="model" />
      <button type="submit">Submit</button>
    </form>
  `,
})
export class Signup {
  form = new FormGroup({});
  model = { email: "" };
  fields: FormlyFieldConfig[] = [
    {
      key: "email",
      type: "input",
      props: { label: "Email", type: "email", required: true },
    },
  ];

  submit() {
    console.log(this.model);
  }
}
```

You also need to register Formly and a UI package (for example `FormlyMaterialModule` or the Bootstrap one) in the app providers.

## 94: How do you set up ngx-mask in a standalone app?

```ts
import { provideNgxMask } from "ngx-mask";

export const appConfig = {
  providers: [provideNgxMask()],
};
```

```ts
import { Component } from "@angular/core";
import { ReactiveFormsModule, FormControl } from "@angular/forms";
import { NgxMaskDirective } from "ngx-mask";

@Component({
  selector: "app-phone",
  imports: [ReactiveFormsModule, NgxMaskDirective],
  template: `<input mask="(000) 000-0000" [formControl]="phone" />`,
})
export class Phone {
  phone = new FormControl("");
}
```

By default the form value is saved without the special characters (`5551234567`). Use `[dropSpecialCharacters]="false"` if you want them kept.

## 95: Which libraries help with authentication in Angular?

- **angular-oauth2-oidc**: OAuth 2 and OpenID Connect client (code flow with PKCE)
- **angular-auth-oidc-client**: another certified OIDC client
- **@azure/msal-angular**: Microsoft Entra ID (Azure AD)
- **@auth0/auth0-angular**: Auth0 SDK
- **keycloak-angular**: Keycloak integration
- **@angular/fire/auth**: Firebase Authentication

## 96: What is angular-oauth2-oidc?

It is a library for logging in with OAuth 2 and OpenID Connect providers (Keycloak, IdentityServer, Auth0, Okta, Azure and others). It handles the redirect to the login page, the code flow with PKCE, storing tokens, refreshing them, and adding the access token to HTTP calls.

```ts
const oauth = inject(OAuthService);
oauth.configure({
  issuer: "https://login.example.com",
  clientId: "spa",
  redirectUri: window.location.origin,
  responseType: "code",
  scope: "openid profile email offline_access",
});
await oauth.loadDiscoveryDocumentAndTryLogin();
if (!oauth.hasValidAccessToken()) {
  oauth.initCodeFlow();
}
```

## 97: What is MSAL Angular?

`@azure/msal-angular` is Microsoft's library for signing users in with Microsoft Entra ID (Azure AD) and Azure AD B2C. It gives you `MsalService` for login and tokens, `MsalGuard` for protecting routes, and `MsalInterceptor` for adding access tokens to HTTP calls to protected APIs. It is built on `@azure/msal-browser`.

## 98: What is the Auth0 Angular SDK?

`@auth0/auth0-angular` connects an Angular app to Auth0. You register it with `provideAuth0({ domain, clientId, authorizationParams })`, then use `AuthService` for `loginWithRedirect()`, `logout()`, `isAuthenticated$` and `user$`. It also has `authGuardFn` for routes and `authHttpInterceptorFn` for adding tokens to API calls.

## 99: What is @auth0/angular-jwt?

It is a small helper library (despite the name, it is not tied to Auth0 login) that:

- adds a JWT to outgoing HTTP requests for allowed domains through an interceptor
- gives you `JwtHelperService` to decode a token and check if it has expired

```ts
const helper = new JwtHelperService();
const expired = helper.isTokenExpired(token);
const payload = helper.decodeToken(token);
```

## 100: What is Sentry for Angular?

`@sentry/angular` sends errors and performance data from your Angular app to Sentry. You call `Sentry.init()` in `main.ts`, replace Angular's `ErrorHandler` with `Sentry.createErrorHandler()`, and optionally add `Sentry.TraceService` for route performance tracing. You get stack traces (with uploaded source maps), breadcrumbs and info about the user's browser.

## 101: What is Lodash and do you still need it in Angular?

Lodash is a utility library with functions like `debounce`, `groupBy`, `cloneDeep`, `orderBy` and `isEqual`. Many Angular projects still use it, but modern JavaScript covers a lot of it now (`structuredClone`, `Object.groupBy`, `Array.prototype.toSorted`, optional chaining).

If you use it, install `lodash-es` and import single functions, so the bundler can tree-shake the rest:

```ts
import { debounce } from "lodash-es";
```

## 102: Which date libraries are common in Angular apps?

- **date-fns**: small, functional and tree-shakable
- **Luxon**: good time zone and locale support, uses `Intl`
- **Day.js**: tiny, Moment-like API
- **Moment.js**: old and in maintenance mode, not recommended for new code

Angular Material has adapters for date-fns (`@angular/material-date-fns-adapter`), Luxon (`@angular/material-luxon-adapter`) and Moment (`@angular/material-moment-adapter`). For simple formatting, Angular's built-in `DatePipe` is often enough.

## 103: What is ngx-skeleton-loader?

It shows grey placeholder shapes (skeletons) while content is loading, which feels faster to users than a spinner.

```html
@if (loading()) {
<ngx-skeleton-loader count="5" appearance="line" />
} @else {
<app-user-list [users]="users()" />
}
```

## 104: What is ngx-spinner?

ngx-spinner shows loading spinners with many built-in animations. You place `<ngx-spinner>` in a template and control it with `NgxSpinnerService.show()` and `hide()`. It is often combined with an HTTP interceptor to show a global loader.

## 105: What is @ngx-loading-bar?

`@ngx-loading-bar` shows a thin progress bar at the top of the page, like on YouTube or GitHub. It has packages that start the bar automatically on HTTP requests (`@ngx-loading-bar/http-client`) and route changes (`@ngx-loading-bar/router`).

## 106: What is ngx-image-cropper?

ngx-image-cropper is a component that lets users crop an image before upload, for example a profile picture. You give it a file input event or an image URL, set an aspect ratio, and it emits the cropped image (as a blob or base64).

```html
<input type="file" (change)="fileEvent = $event" />
<image-cropper
  [imageChangedEvent]="fileEvent"
  [aspectRatio]="1"
  [maintainAspectRatio]="true"
  format="png"
  (imageCropped)="onCropped($event)"
/>
```

## 107: What is ngx-extended-pdf-viewer?

It is a PDF viewer component built on Mozilla's pdf.js. It gives you a full viewer UI inside your app: zoom, search, thumbnails, printing, form filling and annotations.

```html
<ngx-extended-pdf-viewer [src]="'assets/invoice.pdf'" [height]="'80vh'" />
```

## 108: What libraries do people use for rich text editing in Angular?

- **ngx-quill**: wrapper for the Quill editor
- **ngx-editor**: built on ProseMirror
- **TinyMCE Angular** (`@tinymce/tinymce-angular`): official wrapper for TinyMCE
- **CKEditor 5 Angular** (`@ckeditor/ckeditor5-angular`)
- **PrimeNG Editor**: uses Quill under the hood
- **Tiptap**: through community wrappers like `ngx-tiptap`

## 109: How do you use ngx-quill with a reactive form?

```ts
import { Component } from "@angular/core";
import { FormControl, ReactiveFormsModule } from "@angular/forms";
import { QuillEditorComponent } from "ngx-quill";

@Component({
  selector: "app-post-editor",
  imports: [ReactiveFormsModule, QuillEditorComponent],
  template: `<quill-editor [formControl]="content" />`,
})
export class PostEditor {
  content = new FormControl("");
}
```

Remember to add the Quill theme CSS (for example `quill/dist/quill.snow.css`) to your global styles. Always sanitize HTML from an editor on the server before you show it to other users.

## 110: What is ngx-file-drop?

ngx-file-drop is a component that gives you a drag-and-drop area for file uploads. It emits the dropped files and folders, and you upload them yourself with `HttpClient`. Alternatives include `ngx-dropzone` and the file upload components in PrimeNG and NG-ZORRO.

## 111: What is ngx-logger?

ngx-logger is a logging library with log levels (`trace`, `debug`, `info`, `warn`, `error`), optional sending of logs to a server endpoint, and different levels per environment. It helps you avoid `console.log` everywhere and turn off debug logs in production.

## 112: What is Tailwind CSS and how is it used with Angular?

Tailwind is a utility-first CSS framework: you style elements with small classes like `p-4`, `flex` and `text-gray-700` right in the template. The Angular CLI supports it directly. In current versions you install `tailwindcss` and `@tailwindcss/postcss`, add a PostCSS config, and import Tailwind in `styles.css`:

```css
@import "tailwindcss";
```

Many Angular UI libraries (Spartan, PrimeNG unstyled mode) are built to work with Tailwind.

## 113: What is Bootstrap and how do you add it without a wrapper library?

Bootstrap is a CSS framework with a grid system and ready styles for buttons, forms, cards and so on. You can use only its CSS:

```bash
npm install bootstrap
```

```json
"styles": ["node_modules/bootstrap/dist/css/bootstrap.min.css", "src/styles.css"]
```

For interactive parts (modals, dropdowns) use ng-bootstrap or ngx-bootstrap instead of Bootstrap's own JS, so they work with Angular's rendering.

## 114: What is Font Awesome for Angular?

`@fortawesome/angular-fontawesome` is the official component for Font Awesome icons. You import `FaIconComponent` and pass an icon object, so only the icons you use end up in the bundle:

```ts
import { Component } from "@angular/core";
import { FaIconComponent } from "@fortawesome/angular-fontawesome";
import { faCoffee } from "@fortawesome/free-solid-svg-icons";

@Component({
  selector: "app-break",
  imports: [FaIconComponent],
  template: `<fa-icon [icon]="coffee" />`,
})
export class Break {
  coffee = faCoffee;
}
```

## 115: What other icon libraries are common in Angular?

- Material Icons and Material Symbols (with `mat-icon`)
- PrimeIcons (with PrimeNG)
- Font Awesome (`@fortawesome/angular-fontawesome`)
- Lucide (`lucide-angular`)
- `@ng-icons/core`, which bundles many icon sets (Heroicons, Bootstrap Icons, Tabler and more) behind one API

## 116: What is Compodoc?

Compodoc is a documentation generator for Angular projects. It reads your code and creates a static website with all components, services, modules, routes, inputs, outputs and a documentation coverage report.

```bash
npx @compodoc/compodoc -p tsconfig.json -s
```

It is also used by Storybook to show component docs.

## 117: What is source-map-explorer used for?

source-map-explorer analyzes your production bundle using source maps and shows a tree map of which files and libraries take the most space. It helps you find large libraries you did not expect.

```bash
ng build --source-map
npx source-map-explorer dist/my-app/browser/*.js
```

Another option with the esbuild builder is `ng build --stats-json` and loading the stats file into a tool like esbuild's bundle analyzer.

## 118: What is Angular DevTools?

Angular DevTools is a browser extension from the Angular team (not an npm library) for Chrome and Firefox. It shows the component tree, the inputs, outputs and signals of each component, the injector tree, and has a profiler to see how long change detection takes. It is useful for debugging any of the libraries in this list too, since their components appear in the tree.

## 119: What is Prettier and how is it used in Angular projects?

Prettier is a code formatter. It formats TypeScript, HTML templates, SCSS and JSON with consistent rules, so code reviews don't argue about spaces and quotes. Teams usually run it on save in the editor and in a pre-commit hook. It understands Angular control flow syntax (`@if`, `@for`) in templates.

## 120: What are Husky and lint-staged?

Husky runs scripts on Git hooks like `pre-commit` and `pre-push`. lint-staged runs commands only on the files that are staged for commit. Together they are used to run Prettier and ESLint on changed files before every commit, so bad formatting never reaches the repository.

```json
"lint-staged": {
  "*.{ts,html}": ["eslint --fix", "prettier --write"],
  "*.{scss,json,md}": "prettier --write"
}
```

## 121: What is MSW (Mock Service Worker)?

MSW intercepts HTTP requests at the network level (with a service worker in the browser or a request interceptor in Node) and returns mocked responses. In Angular it is used in tests, in Storybook and during development when the backend is not ready yet. Since it works at the network level, your `HttpClient` code and interceptors run unchanged.

## 122: What is json-server?

json-server creates a fake REST API from a JSON file in seconds. It is handy for prototypes and demos:

```bash
npx json-server db.json
```

With `db.json` containing `{ "users": [] }`, you get `GET/POST/PUT/DELETE /users` endpoints at `http://localhost:3000`.

## 123: What is the Angular CDK Overlay?

The Overlay lets you show content in a floating panel on top of the page, positioned relative to an element or to the viewport. Menus, tooltips, autocompletes, selects and dialogs in Material are all built on it. It handles positioning, scroll behavior and a backdrop.

## 124: What is the CDK Portal?

A portal is a piece of UI (a component or a template) that can be rendered somewhere else in the DOM at runtime. You create a `ComponentPortal` or `TemplatePortal` and attach it to a `PortalOutlet`, such as an overlay. It is the base for dialogs and other dynamic content.

## 125: What is the CDK a11y package?

`@angular/cdk/a11y` has tools for accessibility:

- `cdkTrapFocus`: keeps keyboard focus inside a container (useful in modals)
- `LiveAnnouncer`: sends messages to screen readers through an `aria-live` region
- `FocusMonitor`: tells you if an element was focused by mouse, keyboard, touch or code
- `ListKeyManager`: arrow-key navigation in lists
- `cdkAriaLive`, `InteractivityChecker` and high contrast mode detection

## 126: How do you announce a message to screen readers with the CDK?

```ts
import { inject } from "@angular/core";
import { LiveAnnouncer } from "@angular/cdk/a11y";

export class Cart {
  private announcer = inject(LiveAnnouncer);

  addItem() {
    // ...add to cart
    this.announcer.announce("Item added to cart", "polite");
  }
}
```

## 127: What is SelectionModel in the CDK?

`SelectionModel` from `@angular/cdk/collections` keeps track of selected items. It supports single or multiple selection and emits changes. It is often used with `mat-table` checkboxes.

```ts
import { SelectionModel } from "@angular/cdk/collections";

const selection = new SelectionModel<number>(true, []);
selection.select(1, 2);
selection.toggle(2);
selection.isSelected(1); // true
selection.selected; // [1]
```

## 128: What is the CDK stepper?

`CdkStepper` gives you the logic for multi-step flows (wizards): current step, next/previous, linear mode where you can't skip invalid steps. Angular Material's `mat-stepper` is built on it, and you can build your own styled stepper by extending it.

## 129: What is Angular Aria?

Angular Aria (`@angular/aria`) is a newer package from the Angular team with headless, accessible building blocks for common patterns like accordion, tabs, menu, listbox, combobox, tree, grid and toolbar. It handles keyboard navigation, focus and ARIA attributes, and leaves all styling to you. It is a good choice when you build your own design system and do not want Material's look.

## 130: What is Ionic Capacitor?

Capacitor is a native runtime from the Ionic team. It wraps a web app (Angular or any other) in a native iOS or Android shell and gives you JavaScript APIs to device features like camera, file system, geolocation and push notifications. It replaced Cordova in most new Ionic projects.

## 131: How do you add Ionic to a standalone Angular app?

```ts
import { ApplicationConfig } from "@angular/core";
import { provideIonicAngular } from "@ionic/angular/standalone";

export const appConfig: ApplicationConfig = {
  providers: [provideIonicAngular()],
};
```

Then import each Ionic component from `@ionic/angular/standalone` into your components:

```ts
import {
  IonButton,
  IonContent,
  IonHeader,
  IonTitle,
  IonToolbar,
} from "@ionic/angular/standalone";
```

Importing single components lets the bundler drop the ones you don't use.

## 132: What is NgRx Entity?

`@ngrx/entity` helps you store collections of records in a normalized way: an `ids` array and an `entities` dictionary. `createEntityAdapter()` gives you functions like `addOne`, `setAll`, `updateOne`, `removeOne` and ready selectors like `selectAll` and `selectTotal`.

```ts
import { createEntityAdapter, EntityState } from "@ngrx/entity";

interface Book {
  id: string;
  title: string;
}

export const adapter = createEntityAdapter<Book>();
export interface BooksState extends EntityState<Book> {
  loading: boolean;
}
export const initialState: BooksState = adapter.getInitialState({
  loading: false,
});
```

## 133: What is NgRx Router Store?

`@ngrx/router-store` puts the router state (URL, params, query params, data) into the NgRx store and dispatches actions on navigation. You can then write selectors like `selectRouteParam('id')` and combine them with other selectors.

```ts
providers: [provideStore({ router: routerReducer }), provideRouterStore()];
```

## 134: What is ngrx-immer?

`ngrx-immer` is a small community library that lets you write NgRx reducers (and SignalStore updates) with Immer. You write code that looks like mutation, and Immer creates a new immutable state for you.

```ts
import { on } from "@ngrx/store";
import { immerOn } from "ngrx-immer/store";

// plain NgRx
on(addTodo, (state, { title }) => ({
  ...state,
  todos: [...state.todos, { title, done: false }],
}));

// with ngrx-immer
immerOn(addTodo, (state, { title }) => {
  state.todos.push({ title, done: false });
});
```

## 135: What is the ngrx-toolkit from Angular Architects?

`@angular-architects/ngrx-toolkit` is a community package with extra features for NgRx SignalStore, such as `withDevtools` (Redux DevTools support), `withStorageSync` (sync state with localStorage), `withUndoRedo`, `withDataService` and `withRedux`. It fills gaps that the core `@ngrx/signals` package does not cover.

## 136: Which libraries are used for Web Sockets in Angular?

- RxJS `webSocket()` from `rxjs/webSocket`, which needs no extra library
- `ngx-socket-io`, an Angular wrapper for the Socket.IO client
- `@microsoft/signalr` for ASP.NET Core SignalR backends
- Apollo subscriptions with `graphql-ws` for GraphQL
- AngularFire for Firestore real-time updates

## 137: How do you use RxJS webSocket in a service?

```ts
import { Injectable } from "@angular/core";
import { webSocket } from "rxjs/webSocket";

interface ChatMessage {
  user: string;
  text: string;
}

@Injectable({ providedIn: "root" })
export class ChatService {
  private socket = webSocket<ChatMessage>("wss://example.com/chat");

  messages$ = this.socket.asObservable();

  send(message: ChatMessage) {
    this.socket.next(message);
  }
}
```

The connection opens when the first subscriber subscribes and closes when the last one unsubscribes.

## 138: What is @microsoft/signalr used for in Angular?

It is the JavaScript client for ASP.NET Core SignalR. Angular apps with a .NET backend use it for real-time features like notifications, chat or live dashboards. You build a `HubConnection`, start it, and listen to server methods with `on()`. It usually lives in an Angular service that exposes the events as observables or signals.

## 139: What is the Angular service worker package?

`@angular/service-worker` is Angular's built-in package for turning an app into a PWA. You add it with `ng add @angular/pwa`. It caches the app files and selected API responses based on `ngsw-config.json`, makes the app work offline, and lets you check for new versions with `SwUpdate` and receive push notifications with `SwPush`.

## 140: What is Workbox and how does it compare to the Angular service worker?

Workbox is Google's library for writing service workers. It gives you full control over caching strategies, routing and background sync. The Angular service worker is simpler and config-based but less flexible. Teams with special offline needs sometimes replace the Angular service worker with a custom Workbox one.

## 141: What does peerDependencies mean for an Angular library?

A library lists Angular packages in `peerDependencies` instead of `dependencies`, which means "I need this, but use the version the app already has". This keeps only one copy of `@angular/core` in the app. If your Angular version is outside the library's peer range, npm shows a peer dependency error. That usually means the library does not support your Angular version yet.

## 142: What does it mean when a library "supports Angular 20"?

It means the library was built and tested against that Angular version and its `peerDependencies` allow it. Many libraries release a new major version for each Angular major version (Angular Material, NG-ZORRO, NgRx, PrimeNG often follow this). Before you upgrade Angular, check that every library you use has a compatible release.

## 143: Why should you avoid using `--legacy-peer-deps` or `--force` as a habit?

These flags tell npm to ignore peer dependency conflicts. The install succeeds, but the library may not actually work with your Angular version, and you find out at runtime. Use them only as a short, known workaround (for example a library that works fine but hasn't updated its peer range yet), and remove them once the library is updated.

## 144: What should you check before adding a third-party Angular library?

- Is it actively maintained (recent commits, releases, answered issues)?
- Does it support your Angular version, standalone components and SSR?
- What is its bundle size and does it tree-shake?
- What license does it use (MIT, Apache, or commercial)?
- How many people use it (npm downloads, GitHub stars)?
- Is the documentation good?
- Can you replace it later, or will it spread through the whole codebase?
- Could Angular's built-in features or a few lines of your own code do the job?

## 145: What is the license difference between AG Grid Community and Enterprise?

AG Grid Community is MIT licensed and free, including for commercial use. AG Grid Enterprise is a paid product. You can try it without a license key, but it shows a watermark and console warnings, and using it in production requires a paid license. The same pattern applies to some other libraries, like Highcharts, Kendo UI and Syncfusion.

## 146: What are some commercial Angular UI suites?

- **Kendo UI for Angular** (Progress Telerik)
- **DevExtreme** (DevExpress)
- **Syncfusion Essential JS 2 for Angular**
- **Ignite UI for Angular** (Infragistics)
- **AG Grid Enterprise** and **Highcharts**

They have very complete data grids, schedulers, charts, Gantt charts and spreadsheets, plus paid support, which is why big companies use them.

## 147: What is Clarity Design System?

Clarity is an open source design system from VMware with Angular components (`@clr/angular`) and web components. It was used in many enterprise tools. The Angular package is now community maintained and gets less activity than before, so check its state before using it in a new project.

## 148: What is ngx-pagination?

ngx-pagination gives you a `paginate` pipe and a `<pagination-controls>` component for simple client-side or server-side paging of lists.

```html
@for (item of items | paginate: { itemsPerPage: 10, currentPage: page }; track
item.id) {
<p>{{ item.name }}</p>
}
<pagination-controls (pageChange)="page = $event" />
```

## 149: What is ngx-color-picker?

ngx-color-picker is a directive that opens a color picker popup on an input or any element. It supports HEX, RGB and HSL formats, an alpha channel and preset colors.

```html
<input [(colorPicker)]="color" [style.background]="color" />
```

## 150: What is the `@angular/cdk/testing` package?

It provides component test harnesses: classes that let tests interact with a component through a clear API instead of querying its DOM directly. Angular Material ships a harness for every component, for example `MatButtonHarness` and `MatSelectHarness`. If the component's internal DOM changes in a new version, your tests keep working because they talk to the harness.

```ts
const loader = TestbedHarnessEnvironment.loader(fixture);
const button = await loader.getHarness(MatButtonHarness.with({ text: "Save" }));
await button.click();
```

# Moderate Questions (151-300)

## 151: How do you customize the colors of a single Angular Material component?

Each component has an overrides mixin that changes its design tokens without touching internal CSS classes:

```scss
@use "@angular/material" as mat;

.danger-zone {
  @include mat.button-overrides(
    (
      filled-container-color: #b00020,
      filled-label-text-color: white,
    )
  );
}
```

The token names are listed in the "Styling" tab of each component's docs. This is the supported way. Overriding internal classes like `.mdc-button__label` can break on the next update.

## 152: How do you use Material system tokens in your own components?

`mat.theme` outputs CSS variables like `--mat-sys-primary`, `--mat-sys-surface`, `--mat-sys-on-surface` and typography ones like `--mat-sys-body-medium`. You can use them in your own styles, so custom components match the theme and follow dark mode:

```css
.card {
  background: var(--mat-sys-surface-container);
  color: var(--mat-sys-on-surface);
  border-radius: var(--mat-sys-corner-medium);
  font: var(--mat-sys-body-medium);
}
```

## 153: How do you support dark mode with Angular Material?

Set `color-scheme` on the element where you include the theme. With `light dark`, it follows the OS setting. To let users choose, switch the value with a class:

```scss
html {
  color-scheme: light;
  @include mat.theme(
    (
      color: mat.$azure-palette,
      typography: Roboto,
      density: 0,
    )
  );
}

html.dark {
  color-scheme: dark;
}
```

The system tokens use the CSS `light-dark()` function, so you don't need a second theme.

## 154: How do you create a custom Material palette from your brand color?

Use the schematic, which generates M3 palettes from one or more colors:

```bash
ng generate @angular/material:theme-color
```

It creates a Sass file with `$primary-palette` and `$tertiary-palette` maps that you pass into `mat.theme`. This replaces the old `mat.define-palette` approach from M2 themes, which you will still see in older projects.

## 155: How do you change density in Angular Material?

Density makes components more compact. Pass a number from `0` (default) down to `-5`:

```scss
.data-heavy-page {
  @include mat.theme(
    (
      density: -2,
    )
  );
}
```

This is useful for admin screens with many fields and tables.

## 156: How do you set global defaults for Material components?

Most components have an injection token for default options. For example:

```ts
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from "@angular/material/form-field";
import { MAT_SNACK_BAR_DEFAULT_OPTIONS } from "@angular/material/snack-bar";

export const appConfig = {
  providers: [
    {
      provide: MAT_FORM_FIELD_DEFAULT_OPTIONS,
      useValue: { appearance: "outline" },
    },
    { provide: MAT_SNACK_BAR_DEFAULT_OPTIONS, useValue: { duration: 3000 } },
  ],
};
```

## 157: How do you show custom error messages with mat-form-field and reactive forms?

`<mat-error>` is shown when the control is invalid and the error state matcher says so (by default, invalid and touched or the form submitted):

```html
<mat-form-field>
  <mat-label>Password</mat-label>
  <input matInput type="password" [formControl]="password" />
  @if (password.hasError('required')) {
  <mat-error>Password is required</mat-error>
  } @else if (password.hasError('minlength')) {
  <mat-error
    >At least {{ password.getError('minlength').requiredLength }}
    characters</mat-error
  >
  }
</mat-form-field>
```

## 158: What is an ErrorStateMatcher?

It decides when a Material input shows its error state. The default shows errors when the control is invalid and touched (or the parent form was submitted). You can write your own, for example to show errors while typing:

```ts
import { FormControl, FormGroupDirective, NgForm } from "@angular/forms";
import { ErrorStateMatcher } from "@angular/material/core";

export class InstantErrorMatcher implements ErrorStateMatcher {
  isErrorState(
    control: FormControl | null,
    form: FormGroupDirective | NgForm | null,
  ): boolean {
    return !!(control && control.invalid && (control.dirty || control.touched));
  }
}
```

Use it per input with `[errorStateMatcher]` or globally by providing `ErrorStateMatcher`.

## 159: How do you write a custom form field control for mat-form-field?

You implement the `MatFormFieldControl<T>` interface and provide your component as that token. The interface has members like `value`, `stateChanges`, `focused`, `empty`, `shouldLabelFloat`, `required`, `disabled`, `errorState` and `setDescribedByIds()`. Usually you also implement `ControlValueAccessor` so it works with forms.

This is how you build things like a phone input with country code that looks and behaves like a native Material input with a floating label and errors.

## 160: How do you use mat-autocomplete with server-side search?

Listen to the input, debounce it, call the API with `switchMap`, and show results in `<mat-autocomplete>`:

```ts
import { Component, inject } from "@angular/core";
import { toSignal } from "@angular/core/rxjs-interop";
import { FormControl, ReactiveFormsModule } from "@angular/forms";
import { MatAutocompleteModule } from "@angular/material/autocomplete";
import { MatInputModule } from "@angular/material/input";
import { debounceTime, distinctUntilChanged, switchMap, filter } from "rxjs";
import { CityApi } from "./city-api";

@Component({
  selector: "app-city-search",
  imports: [ReactiveFormsModule, MatAutocompleteModule, MatInputModule],
  template: `
    <mat-form-field>
      <input matInput [formControl]="query" [matAutocomplete]="auto" />
      <mat-autocomplete #auto>
        @for (city of cities(); track city) {
          <mat-option [value]="city">{{ city }}</mat-option>
        }
      </mat-autocomplete>
    </mat-form-field>
  `,
})
export class CitySearch {
  private api = inject(CityApi);
  query = new FormControl("", { nonNullable: true });

  cities = toSignal(
    this.query.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      filter((q) => q.length > 1),
      switchMap((q) => this.api.search(q)),
    ),
    { initialValue: [] as string[] },
  );
}
```

`switchMap` cancels the previous request when the user keeps typing.

## 161: How do you use objects as values in mat-autocomplete?

Set the option value to the object and give `displayWith` a function that turns it into text:

```html
<mat-autocomplete #auto [displayWith]="displayUser">
  @for (user of users(); track user.id) {
  <mat-option [value]="user">{{ user.name }}</mat-option>
  }
</mat-autocomplete>
```

```ts
displayUser = (user: User | null) => (user ? user.name : "");
```

Note that while the user is typing, the form control value is a string, and after they select an option it is the object. Handle both cases.

## 162: How do you load data from the server for mat-table with paging and sorting?

Don't use `MatTableDataSource` for this. Instead, combine the sort and page events and fetch data:

```ts
import {
  Component,
  inject,
  viewChild,
  AfterViewInit,
  signal,
} from "@angular/core";
import { MatPaginator } from "@angular/material/paginator";
import { MatSort } from "@angular/material/sort";
import { merge, startWith, switchMap } from "rxjs";
import { OrdersApi, Order } from "./orders-api";

@Component({ selector: "app-orders", templateUrl: "./orders.html" })
export class Orders implements AfterViewInit {
  private api = inject(OrdersApi);
  sort = viewChild.required(MatSort);
  paginator = viewChild.required(MatPaginator);
  rows = signal<Order[]>([]);
  total = signal(0);

  ngAfterViewInit() {
    this.sort().sortChange.subscribe(() => (this.paginator().pageIndex = 0));

    merge(this.sort().sortChange, this.paginator().page)
      .pipe(
        startWith({}),
        switchMap(() =>
          this.api.list({
            sort: this.sort().active,
            dir: this.sort().direction,
            page: this.paginator().pageIndex,
            size: this.paginator().pageSize,
          }),
        ),
      )
      .subscribe((res) => {
        this.rows.set(res.items);
        this.total.set(res.total);
      });
  }
}
```

In the template, set `[length]="total()"` on the paginator. Clean up the subscriptions with `takeUntilDestroyed` in a real app.

## 163: How do you add row selection with checkboxes to mat-table?

Use `SelectionModel` and add a select column:

```html
<ng-container matColumnDef="select">
  <th mat-header-cell *matHeaderCellDef>
    <mat-checkbox
      [checked]="selection.hasValue() && allSelected()"
      [indeterminate]="selection.hasValue() && !allSelected()"
      (change)="toggleAll()"
    />
  </th>
  <td mat-cell *matCellDef="let row">
    <mat-checkbox
      [checked]="selection.isSelected(row)"
      (change)="selection.toggle(row)"
    />
  </td>
</ng-container>
```

```ts
selection = new SelectionModel<User>(true, []);

allSelected() {
  return this.selection.selected.length === this.dataSource.data.length;
}

toggleAll() {
  this.allSelected() ? this.selection.clear() : this.selection.select(...this.dataSource.data);
}
```

## 164: How do you filter a MatTableDataSource?

Set `filter` to a string. By default it checks if any column contains the text. Use `filterPredicate` for custom logic:

```ts
this.dataSource.filterPredicate = (row, filter) => row.name.toLowerCase().includes(filter);

applyFilter(value: string) {
  this.dataSource.filter = value.trim().toLowerCase();
  this.dataSource.paginator?.firstPage();
}
```

## 165: How do you make sticky headers and columns in mat-table?

Add `sticky` on header/footer row definitions and on column definitions:

```html
<ng-container matColumnDef="name" sticky>...</ng-container>
<ng-container matColumnDef="actions" stickyEnd>...</ng-container>

<tr mat-header-row *matHeaderRowDef="columns; sticky: true"></tr>
```

The table must be inside a scrolling container with a fixed height for sticky headers to work.

## 166: How do you open a menu from a button in Angular Material?

```html
<button matIconButton [matMenuTriggerFor]="menu" aria-label="Actions">
  <mat-icon>more_vert</mat-icon>
</button>
<mat-menu #menu>
  <button mat-menu-item (click)="edit()">Edit</button>
  <button mat-menu-item [matMenuTriggerFor]="moveMenu">Move to</button>
</mat-menu>
<mat-menu #moveMenu>
  <button mat-menu-item>Archive</button>
</mat-menu>
```

Nesting a `matMenuTriggerFor` inside a menu item creates a sub menu.

## 167: How do you return a typed result from a Material dialog?

Use the generic types of `MatDialog.open` and `MatDialogRef`:

```ts
const ref = this.dialog.open<EditUserDialog, EditUserData, User | undefined>(
  EditUserDialog,
  {
    data: { id: 5 },
    width: "480px",
    disableClose: true,
  },
);

ref.afterClosed().subscribe((user) => {
  if (user) {
    this.save(user);
  }
});
```

Inside the dialog, `inject(MatDialogRef<EditUserDialog, User>)` and call `close(user)`.

## 168: When would you use the CDK Dialog instead of MatDialog?

`Dialog` from `@angular/cdk/dialog` has the same features (focus trap, backdrop, ESC to close, data passing, ARIA roles) but no Material styling. Use it when your app has its own design system and you want a dialog behavior without fighting Material's styles.

```ts
import { Dialog } from "@angular/cdk/dialog";

const dialog = inject(Dialog);
dialog.open(MyDialog, { data: { id: 1 }, panelClass: "my-dialog" });
```

## 169: How do you create a tooltip-like popup with the CDK Overlay?

```ts
import {
  Directive,
  ElementRef,
  HostListener,
  inject,
  input,
  TemplateRef,
  ViewContainerRef,
} from "@angular/core";
import { Overlay, OverlayRef } from "@angular/cdk/overlay";
import { TemplatePortal } from "@angular/cdk/portal";

@Directive({ selector: "[appPopover]" })
export class Popover {
  content = input.required<TemplateRef<unknown>>({ alias: "appPopover" });
  private overlay = inject(Overlay);
  private el = inject(ElementRef);
  private vcr = inject(ViewContainerRef);
  private ref?: OverlayRef;

  @HostListener("mouseenter")
  show() {
    const positionStrategy = this.overlay
      .position()
      .flexibleConnectedTo(this.el)
      .withPositions([
        {
          originX: "center",
          originY: "bottom",
          overlayX: "center",
          overlayY: "top",
          offsetY: 8,
        },
      ]);

    this.ref = this.overlay.create({
      positionStrategy,
      scrollStrategy: this.overlay.scrollStrategies.reposition(),
    });
    this.ref.attach(new TemplatePortal(this.content(), this.vcr));
  }

  @HostListener("mouseleave")
  hide() {
    this.ref?.dispose();
  }
}
```

You also need the CDK overlay styles (`@angular/cdk/overlay-prebuilt.css`) if you are not using a Material theme.

## 170: What are the CDK overlay scroll strategies?

They decide what happens to an open overlay when the page scrolls:

- `noop`: do nothing
- `close`: close the overlay
- `block`: block page scrolling while the overlay is open (used by dialogs)
- `reposition`: move the overlay so it stays next to its origin (used by menus and selects)

## 171: How do you drag items between two lists with the CDK?

Connect the lists with `cdkDropListConnectedTo` (or put them in a `cdkDropListGroup`) and use `transferArrayItem` when an item moves to another list:

```ts
import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

drop(event: CdkDragDrop<string[]>) {
  if (event.previousContainer === event.container) {
    moveItemInArray(event.container.data, event.previousIndex, event.currentIndex);
  } else {
    transferArrayItem(
      event.previousContainer.data,
      event.container.data,
      event.previousIndex,
      event.currentIndex,
    );
  }
}
```

```html
<div cdkDropListGroup>
  <ul cdkDropList [cdkDropListData]="todo" (cdkDropListDropped)="drop($event)">
    ...
  </ul>
  <ul cdkDropList [cdkDropListData]="done" (cdkDropListDropped)="drop($event)">
    ...
  </ul>
</div>
```

This is the usual way to build a Kanban board. Note these helpers mutate the arrays, so if you keep data in signals, update the signal afterwards with new array references.

## 172: How do you restrict drag and drop in the CDK?

- `cdkDragLockAxis="y"` lets an item move only vertically
- `cdkDragBoundary=".container"` keeps it inside an element
- `cdkDragDisabled` disables dragging for one item
- `cdkDragHandle` on a child element makes only that part draggable
- `cdkDropListEnterPredicate` decides which items can enter a list
- `cdkDropListSortingDisabled` allows dropping but not reordering

## 173: Why does virtual scroll need a fixed item size, and what if items have different heights?

`cdk-virtual-scroll-viewport` with `itemSize` uses a fixed-size strategy: it calculates which items are visible from the scroll position and the item height. With different heights, the math is wrong and items jump.

Options for variable heights:

- `autosize` virtual scroll from `@angular/cdk-experimental/scrolling`, which measures items but is experimental
- make all rows the same height (often the simplest)
- use another library with variable size support, or PrimeNG/AG Grid virtual scrolling

## 174: How do you use virtual scroll with an infinite list?

Listen to `scrolledIndexChange` on the viewport and load more data when the user is near the end:

```html
<cdk-virtual-scroll-viewport
  itemSize="56"
  class="list"
  (scrolledIndexChange)="onScroll($event)"
>
  <div *cdkVirtualFor="let item of items(); trackBy: trackById" class="row">
    {{ item.name }}
  </div>
</cdk-virtual-scroll-viewport>
```

```ts
viewport = viewChild.required(CdkVirtualScrollViewport);

onScroll(index: number) {
  const end = this.viewport().getRenderedRange().end;
  if (end >= this.items().length - 5 && !this.loading()) {
    this.loadNextPage();
  }
}
```

## 175: How do you make a responsive sidenav layout with Angular Material?

Use `mat-sidenav-container` and switch the mode based on `BreakpointObserver`:

```html
<mat-sidenav-container class="h-full">
  <mat-sidenav
    [mode]="isHandset() ? 'over' : 'side'"
    [opened]="!isHandset()"
    #drawer
  >
    <app-nav-links (navigate)="isHandset() && drawer.close()" />
  </mat-sidenav>
  <mat-sidenav-content>
    <mat-toolbar>
      @if (isHandset()) {
      <button matIconButton (click)="drawer.toggle()">
        <mat-icon>menu</mat-icon>
      </button>
      } My App
    </mat-toolbar>
    <router-outlet />
  </mat-sidenav-content>
</mat-sidenav-container>
```

`ng generate @angular/material:navigation` creates this layout for you.

## 176: What schematics does Angular Material provide?

- `ng g @angular/material:navigation <name>`: responsive toolbar and sidenav
- `ng g @angular/material:dashboard <name>`: grid of cards
- `ng g @angular/material:table <name>`: table with sort and paginator
- `ng g @angular/material:tree <name>`: tree view
- `ng g @angular/material:address-form <name>`: form example
- `ng g @angular/material:theme-color`: generate palettes from colors

There are also migration schematics run by `ng update`.

## 177: How do you test a component that uses Material with harnesses?

```ts
import { TestBed } from "@angular/core/testing";
import { TestbedHarnessEnvironment } from "@angular/cdk/testing/testbed";
import { MatSelectHarness } from "@angular/material/select/testing";
import { MatButtonHarness } from "@angular/material/button/testing";
import { Filters } from "./filters";

it("applies the selected status", async () => {
  const fixture = TestBed.createComponent(Filters);
  const loader = TestbedHarnessEnvironment.loader(fixture);

  const select = await loader.getHarness(MatSelectHarness);
  await select.open();
  await select.clickOptions({ text: "Active" });

  const apply = await loader.getHarness(
    MatButtonHarness.with({ text: "Apply" }),
  );
  await apply.click();

  expect(fixture.componentInstance.status()).toBe("active");
});
```

Harnesses wait for the component to be stable, so you don't need `fixture.detectChanges()` everywhere.

## 178: How do you test a component that opens a MatDialog?

For a dialog that is opened in an overlay, use `TestbedHarnessEnvironment.documentRootLoader(fixture)` because the dialog is not inside the component's DOM:

```ts
const rootLoader = TestbedHarnessEnvironment.documentRootLoader(fixture);
const dialog = await rootLoader.getHarness(MatDialogHarness);
expect(await dialog.getTitleText()).toBe("Delete Anna?");
await dialog.close();
```

Another option is to mock `MatDialog` and check that `open` was called with the right component and data.

## 179: How do you register custom SVG icons in Angular Material?

Use `MatIconRegistry` with `DomSanitizer`, usually in an app initializer:

```ts
import { inject, provideAppInitializer } from "@angular/core";
import { MatIconRegistry } from "@angular/material/icon";
import { DomSanitizer } from "@angular/platform-browser";

export const appConfig = {
  providers: [
    provideAppInitializer(() => {
      const registry = inject(MatIconRegistry);
      const sanitizer = inject(DomSanitizer);
      registry.addSvgIconSet(
        sanitizer.bypassSecurityTrustResourceUrl("/icons/sprite.svg"),
      );
      registry.addSvgIcon(
        "logo",
        sanitizer.bypassSecurityTrustResourceUrl("/icons/logo.svg"),
      );
    }),
  ],
};
```

```html
<mat-icon svgIcon="logo" />
```

Only trust URLs you control.

## 180: How do you use Material Symbols instead of the old Material Icons font?

Load the Material Symbols font in `index.html` and set it as the default font set:

```ts
import { inject, provideAppInitializer } from "@angular/core";
import { MatIconRegistry } from "@angular/material/icon";

provideAppInitializer(() => {
  inject(MatIconRegistry).setDefaultFontSetClass("material-symbols-outlined");
});
```

Now `<mat-icon>delete</mat-icon>` uses Material Symbols. You can control fill and weight through the font's variation settings in CSS.

## 181: How do you use a PrimeNG table with lazy loading?

```html
<p-table
  [value]="customers()"
  [lazy]="true"
  [paginator]="true"
  [rows]="10"
  [totalRecords]="total()"
  [loading]="loading()"
  (onLazyLoad)="load($event)"
>
  <ng-template #header>
    <tr>
      <th pSortableColumn="name">Name <p-sortIcon field="name" /></th>
      <th>Country</th>
    </tr>
  </ng-template>
  <ng-template #body let-customer>
    <tr>
      <td>{{ customer.name }}</td>
      <td>{{ customer.country }}</td>
    </tr>
  </ng-template>
</p-table>
```

```ts
load(event: TableLazyLoadEvent) {
  this.loading.set(true);
  this.api
    .list({ first: event.first, rows: event.rows, sortField: event.sortField, sortOrder: event.sortOrder })
    .subscribe((res) => {
      this.customers.set(res.items);
      this.total.set(res.total);
      this.loading.set(false);
    });
}
```

Recent PrimeNG versions use template reference names like `#header` and `#body`. Older ones used `pTemplate="header"`, which you will see a lot in existing code.

## 182: How do you customize a PrimeNG theme preset?

Use `definePreset` to extend a built-in preset and change design tokens:

```ts
import { definePreset } from "@primeuix/themes";
import Aura from "@primeuix/themes/aura";

const MyPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: "{indigo.50}",
      500: "{indigo.500}",
      900: "{indigo.900}",
    },
  },
});

providePrimeNG({
  theme: { preset: MyPreset, options: { darkModeSelector: ".app-dark" } },
});
```

`darkModeSelector` sets which class turns on dark mode. Tokens have three levels: primitive (raw colors), semantic (primary, surface) and component tokens.

## 183: What is PrimeNG unstyled mode?

In unstyled mode, PrimeNG components render without their theme styles, only the behavior and structure. You add your own classes, often with Tailwind, through the `pt` (pass-through) API or global pass-through config. It is useful when your design is very different from the built-in presets.

```ts
providePrimeNG({ unstyled: true });
```

## 184: What is the pass-through (pt) API in PrimeNG?

Pass-through lets you add attributes and classes to the inner elements of a component that you can't reach from the template:

```html
<p-panel
  header="Details"
  [pt]="{
    root: { class: 'rounded-xl border' },
    header: { class: 'bg-gray-50 font-semibold' }
  }"
>
  Content
</p-panel>
```

You can also set it globally in `providePrimeNG({ pt: { ... } })`.

## 185: How do you show a confirmation dialog with PrimeNG?

Use `ConfirmationService` with the `<p-confirmdialog>` component:

```ts
import { Component, inject } from "@angular/core";
import { ConfirmationService } from "primeng/api";
import { ConfirmDialog } from "primeng/confirmdialog";

@Component({
  selector: "app-account",
  imports: [ConfirmDialog],
  providers: [ConfirmationService],
  template: `
    <p-confirmdialog />
    <button (click)="deleteAccount()">Delete account</button>
  `,
})
export class Account {
  private confirm = inject(ConfirmationService);

  deleteAccount() {
    this.confirm.confirm({
      message: "This cannot be undone. Continue?",
      header: "Delete account",
      accept: () => this.doDelete(),
    });
  }

  doDelete() {}
}
```

`MessageService` with `<p-toast>` works the same way for toasts.

## 186: How do you use NG-ZORRO in a standalone app?

After `ng add ng-zorro-antd`, import components from their entry points and provide the locale and icons:

```ts
import { provideNzI18n, en_US } from "ng-zorro-antd/i18n";
import { provideNzIcons } from "ng-zorro-antd/icon";
import { UserOutline, LockOutline } from "@ant-design/icons-angular/icons";

export const appConfig = {
  providers: [provideNzI18n(en_US), provideNzIcons([UserOutline, LockOutline])],
};
```

```ts
import { NzButtonModule } from "ng-zorro-antd/button";
import { NzTableModule } from "ng-zorro-antd/table";
```

Registering only the icons you use keeps the bundle small. If you load all icons, NG-ZORRO adds every icon file.

## 187: How do you use the ng-bootstrap typeahead?

`ngbTypeahead` takes a function that receives an observable of search text and returns an observable of results:

```ts
import { Component } from "@angular/core";
import { NgbTypeahead } from "@ng-bootstrap/ng-bootstrap";
import { Observable, debounceTime, distinctUntilChanged, map } from "rxjs";

const states = ["Alabama", "Alaska", "Arizona", "California", "Colorado"];

@Component({
  selector: "app-state-picker",
  imports: [NgbTypeahead],
  template: `<input class="form-control" [ngbTypeahead]="search" />`,
})
export class StatePicker {
  search = (text$: Observable<string>) =>
    text$.pipe(
      debounceTime(200),
      distinctUntilChanged(),
      map((term) =>
        term.length < 2
          ? []
          : states
              .filter((s) => s.toLowerCase().includes(term.toLowerCase()))
              .slice(0, 10),
      ),
    );
}
```

## 188: How do you set global defaults in ng-bootstrap?

Each component has a config service you can inject and change, for example in an app initializer or in the root component:

```ts
const tooltipConfig = inject(NgbTooltipConfig);
tooltipConfig.placement = "bottom";
tooltipConfig.container = "body";

const modalConfig = inject(NgbModalConfig);
modalConfig.backdrop = "static";
modalConfig.keyboard = false;
```

## 189: How do you lazy load translations per feature with Transloco?

Use scopes. Put translations in a folder like `i18n/admin/en.json`, and provide the scope on the lazy route:

```ts
import { provideTranslocoScope } from "@jsverse/transloco";

export const routes: Routes = [
  {
    path: "admin",
    providers: [provideTranslocoScope("admin")],
    loadComponent: () => import("./admin/admin-page").then((m) => m.AdminPage),
  },
];
```

```html
<ng-container *transloco="let t; prefix: 'admin'">
  <h1>{{ t('title') }}</h1>
</ng-container>
```

The admin translations are loaded only when the user opens that route.

## 190: What Transloco plugins are commonly used?

- `@jsverse/transloco-messageformat`: ICU message format for plurals and gender
- `@jsverse/transloco-locale`: locale-aware date, number and currency pipes
- `@jsverse/transloco-persist-lang`: remember the selected language in storage
- `@jsverse/transloco-persist-translations`: cache translation files in storage
- `@jsverse/transloco-preload-langs`: preload other languages in the background
- `@jsverse/transloco-keys-manager`: find and extract keys from your code

## 191: How do you handle plurals with ngx-translate or Transloco?

Neither handles ICU plurals out of the box. You add a message format plugin:

- ngx-translate: `ngx-translate-messageformat-compiler`
- Transloco: `@jsverse/transloco-messageformat`

Then a translation can look like this:

```json
{
  "cart.items": "{count, plural, =0 {Your cart is empty} one {1 item} other {# items}}"
}
```

```html
{{ t('cart.items', { count: items().length }) }}
```

`@angular/localize` supports ICU plurals natively in templates.

## 192: How do you make translations type-safe?

Options:

- Transloco Keys Manager can find missing and unused keys in CI.
- Generate TypeScript types from your default JSON file (for example with a small script or a tool like `i18next-parser`-style generators) and type your translate function.
- With `@angular/localize`, the compiler checks `i18n` markers at build time and extraction finds every message.

Without one of these, a typo in a key only shows as an untranslated key at runtime.

## 193: How do you handle missing translations?

- ngx-translate: provide a custom `MissingTranslationHandler` that logs the key and returns a fallback.
- Transloco: set `missingHandler` in the config (for example `logMissingKey`, `useFallbackTranslation`) or provide a custom `TRANSLOCO_MISSING_HANDLER`.
- Both support a fallback language that is used when a key is missing in the active one.

Logging missing keys in development and sending them to monitoring in production helps you find gaps early.

## 194: How do you load the user's preferred language at startup?

Read the language from storage, the URL, or `navigator.language`, check it is supported, and set it before the first render. With Transloco:

```ts
import { inject, provideAppInitializer } from "@angular/core";
import { TranslocoService } from "@jsverse/transloco";
import { firstValueFrom } from "rxjs";

provideAppInitializer(() => {
  const transloco = inject(TranslocoService);
  const saved = localStorage.getItem("lang");
  const browser = navigator.language.split("-")[0];
  const lang = [saved, browser].find((l) => l && transloco.isLang(l)) ?? "en";
  transloco.setActiveLang(lang);
  return firstValueFrom(transloco.load(lang));
});
```

Waiting for the file avoids a flash of raw keys. Guard `localStorage` and `navigator` if you use SSR.

## 195: How do you write a classic NgRx effect with HTTP?

```ts
import { inject } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { catchError, exhaustMap, map, of } from "rxjs";
import { BooksApi } from "./books-api";
import { BooksPageActions, BooksApiActions } from "./books.actions";

export const loadBooks = createEffect(
  (actions$ = inject(Actions), api = inject(BooksApi)) =>
    actions$.pipe(
      ofType(BooksPageActions.opened),
      exhaustMap(() =>
        api.getAll().pipe(
          map((books) => BooksApiActions.loadSuccess({ books })),
          catchError((error) =>
            of(BooksApiActions.loadFailure({ error: error.message })),
          ),
        ),
      ),
    ),
  { functional: true },
);
```

`catchError` is inside the inner observable, so one failed request does not kill the effect.

## 196: How do you read NgRx store state as a signal?

Use `selectSignal`:

```ts
import { Component, inject } from "@angular/core";
import { Store } from "@ngrx/store";
import { booksFeature } from "./books.feature";

@Component({
  selector: "app-book-list",
  template: `
    @for (book of books(); track book.id) {
      <p>{{ book.title }}</p>
    }
  `,
})
export class BookList {
  private store = inject(Store);
  books = this.store.selectSignal(booksFeature.selectBooks);
}
```

## 197: How do you load data in a SignalStore?

Use `rxMethod` from `@ngrx/signals/rxjs-interop` for RxJS-based loading, or a plain async method:

```ts
import { inject } from "@angular/core";
import { signalStore, withState, withMethods, patchState } from "@ngrx/signals";
import { rxMethod } from "@ngrx/signals/rxjs-interop";
import { tapResponse } from "@ngrx/operators";
import { pipe, switchMap, tap, debounceTime } from "rxjs";
import { BooksApi, Book } from "./books-api";

export const BooksStore = signalStore(
  withState({ books: [] as Book[], loading: false }),
  withMethods((store, api = inject(BooksApi)) => ({
    search: rxMethod<string>(
      pipe(
        debounceTime(300),
        tap(() => patchState(store, { loading: true })),
        switchMap((query) =>
          api.search(query).pipe(
            tapResponse({
              next: (books) => patchState(store, { books, loading: false }),
              error: () => patchState(store, { loading: false }),
            }),
          ),
        ),
      ),
    ),
  })),
);
```

`rxMethod` accepts a plain value, an observable or a signal. If you pass a signal, it runs every time the signal changes.

## 198: How do you manage a list of records in a SignalStore?

Use `withEntities` from `@ngrx/signals/entities`:

```ts
import { signalStore, withMethods, patchState } from "@ngrx/signals";
import {
  withEntities,
  addEntity,
  removeEntity,
  updateEntity,
} from "@ngrx/signals/entities";

interface Todo {
  id: number;
  title: string;
  done: boolean;
}

export const TodosStore = signalStore(
  withEntities<Todo>(),
  withMethods((store) => ({
    add(todo: Todo) {
      patchState(store, addEntity(todo));
    },
    toggle(id: number) {
      patchState(
        store,
        updateEntity({ id, changes: (t) => ({ done: !t.done }) }),
      );
    },
    remove(id: number) {
      patchState(store, removeEntity(id));
    },
  })),
);
```

The store gets `entities()`, `ids()` and `entityMap()` signals.

## 199: What are lifecycle hooks in SignalStore?

`withHooks` lets you run code when the store is created or destroyed, for example to load data:

```ts
import { withHooks } from "@ngrx/signals";

export const BooksStore = signalStore(
  withState({ books: [] as Book[] }),
  withMethods(/* ... */),
  withHooks({
    onInit(store) {
      store.loadAll();
    },
    onDestroy() {
      console.log("store destroyed");
    },
  }),
);
```

If the store is provided in a component, it is created and destroyed with that component.

## 200: When would you provide a SignalStore at component level instead of root?

Provide it at root (`{ providedIn: 'root' }`) for app-wide state like the current user or cart. Provide it in a component (`providers: [BooksStore]`) when the state belongs to one screen or widget, for example a search page or a wizard. Each component instance then gets its own store, and the state is cleaned up when the component is destroyed. That avoids stale state when the user comes back to the page.

## 201: How do you handle async work in NGXS?

Return an observable or a promise from the `@Action` handler. NGXS waits for it, and the dispatch observable completes when the work finishes:

```ts
@Action(LoadBooks)
load(ctx: StateContext<BooksModel>) {
  ctx.patchState({ loading: true });
  return this.api.getAll().pipe(
    tap((books) => ctx.patchState({ books, loading: false })),
    catchError((err) => {
      ctx.patchState({ loading: false, error: err.message });
      return EMPTY;
    }),
  );
}
```

```ts
this.store.dispatch(new LoadBooks()).subscribe(() => console.log("loaded"));
```

## 202: What NGXS plugins are commonly used?

- `@ngxs/storage-plugin`: saves selected states to localStorage or sessionStorage
- `@ngxs/devtools-plugin`: Redux DevTools support
- `@ngxs/logger-plugin`: logs actions and state to the console
- `@ngxs/router-plugin`: keeps router state in the store and lets you navigate with actions
- `@ngxs/form-plugin`: syncs reactive forms with the store
- `@ngxs/websocket-plugin`: sends and receives WebSocket messages as actions

## 203: How do you persist state to localStorage with NGXS?

```ts
import { provideStore } from "@ngxs/store";
import { withNgxsStoragePlugin } from "@ngxs/storage-plugin";

export const appConfig = {
  providers: [
    provideStore(
      [AuthState, SettingsState],
      withNgxsStoragePlugin({ keys: ["settings"] }),
    ),
  ],
};
```

Only the `settings` state is saved. Be careful with what you persist: never store sensitive data in localStorage, and handle schema changes with the plugin's migrations option.

## 204: How do you compare NgRx Store, NgRx SignalStore and NGXS?

- **NgRx Store**: strict Redux pattern, actions, reducers, effects and selectors in separate pieces. Very predictable and great tooling, but more code. Good for large apps with many developers.
- **NgRx SignalStore**: signal-based, functional, much less code, easy to scope to a component. Good default for new apps.
- **NGXS**: class-and-decorator based, actions handled in one place with async inside. Less code than NgRx Store, popular with teams that like an OOP style.

All three are actively maintained. The choice often depends on team preference and existing code.

## 205: How do you use mutations in TanStack Query for Angular?

```ts
import { inject } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import {
  injectMutation,
  QueryClient,
} from "@tanstack/angular-query-experimental";
import { lastValueFrom } from "rxjs";

export class AddTodo {
  private http = inject(HttpClient);
  private queryClient = inject(QueryClient);

  addTodo = injectMutation(() => ({
    mutationFn: (title: string) =>
      lastValueFrom(this.http.post("/api/todos", { title })),
    onSuccess: () =>
      this.queryClient.invalidateQueries({ queryKey: ["todos"] }),
  }));

  save(title: string) {
    this.addTodo.mutate(title);
  }
}
```

After the mutation succeeds, invalidating the `todos` query makes every component that uses it refetch. Older code uses `injectQueryClient()`, which is deprecated in favor of `inject(QueryClient)`.

## 206: How do you make a TanStack query depend on a signal?

Read the signal inside the options function. The query reruns when the signal changes, and the signal value is part of the query key:

```ts
userId = input.required<number>();

user = injectQuery(() => ({
  queryKey: ["user", this.userId()],
  queryFn: () =>
    lastValueFrom(this.http.get<User>(`/api/users/${this.userId()}`)),
  enabled: this.userId() > 0,
}));
```

`enabled` lets you skip the request until you have a valid value.

## 207: What is staleTime vs gcTime in TanStack Query?

- `staleTime`: how long fetched data is considered fresh. While fresh, the query will not refetch on mount or window focus. Default is `0`, so data is stale right away.
- `gcTime` (formerly `cacheTime`): how long unused data stays in the cache after no component is using it. Default is 5 minutes.

For data that rarely changes, like a list of countries, set a long `staleTime`.

## 208: When would you use TanStack Query instead of NgRx?

TanStack Query is for server state: data that lives on the server and you fetch, cache and refresh. It handles loading states, caching, deduplication, retries and refetching with very little code.

NgRx (or another store) is better for client state: UI state, multi-step flows, complex business logic, and state shared by many parts of the app that doesn't come from one API call. Many apps use both, or use TanStack Query plus signals for the little client state they have.

## 209: How does Angular's httpResource compare to TanStack Query?

`httpResource` (and `resource`) is built into Angular. It fetches data reactively based on signals and gives you `value()`, `isLoading()`, `error()` and `reload()`. It is simple and has no extra dependency.

TanStack Query adds a shared cache across components, deduplication, background refetching, stale times, retries, pagination helpers, optimistic updates and devtools. If you only need "load data for this component", `httpResource` is enough. If many components share and refresh the same server data, TanStack Query does more for you.

## 210: How do you do a mutation with Apollo Angular and update the cache?

```ts
const ADD_TODO = gql`
  mutation AddTodo($title: String!) {
    addTodo(title: $title) {
      id
      title
    }
  }
`;

this.apollo
  .mutate<{ addTodo: Todo }>({
    mutation: ADD_TODO,
    variables: { title },
    refetchQueries: ["GetTodos"],
  })
  .subscribe();
```

If the mutation returns an object with `id` and `__typename` that is already in the cache, Apollo updates it automatically. For new items, use `refetchQueries` or the `update` function to write into the cache yourself.

## 211: How do you add an auth header to Apollo Angular requests?

Since `HttpLink` uses `HttpClient`, the easiest way is an Angular HTTP interceptor. You can also use `setContext` from Apollo:

```ts
import { setContext } from "@apollo/client/link/context";
import { ApolloLink, InMemoryCache } from "@apollo/client/core";

provideApollo(() => {
  const httpLink = inject(HttpLink);
  const auth = inject(AuthService);

  const authLink = setContext(() => ({
    headers: { Authorization: `Bearer ${auth.token()}` },
  }));

  return {
    link: ApolloLink.from([authLink, httpLink.create({ uri: "/graphql" })]),
    cache: new InMemoryCache(),
  };
});
```

## 212: What is GraphQL Code Generator and why use it with Apollo Angular?

GraphQL Code Generator (`@graphql-codegen/cli`) reads your schema and `.graphql` files and generates TypeScript types. With the `typescript-apollo-angular` plugin it also generates injectable services for each query and mutation:

```ts
// generated
@Injectable({ providedIn: 'root' })
export class GetBooksGQL extends Query<GetBooksQuery> { ... }
```

```ts
books = inject(GetBooksGQL).watch().valueChanges;
```

This gives you full type safety for variables and results.

## 213: How do you protect routes with AngularFire Auth?

AngularFire ships guards in `@angular/fire/auth-guard`:

```ts
import { AuthGuard, redirectUnauthorizedTo } from "@angular/fire/auth-guard";

const redirectToLogin = () => redirectUnauthorizedTo(["login"]);

export const routes: Routes = [
  {
    path: "account",
    loadComponent: () => import("./account").then((m) => m.Account),
    canActivate: [AuthGuard],
    data: { authGuardPipe: redirectToLogin },
  },
];
```

You can also write your own functional guard that reads `authState(inject(Auth))`.

## 214: How do you add a custom cell renderer in AG Grid?

Write a component that implements `ICellRendererAngularComp` and set it as `cellRenderer` in the column definition:

```ts
import { Component } from "@angular/core";
import { ICellRendererAngularComp } from "ag-grid-angular";
import { ICellRendererParams } from "ag-grid-community";

@Component({
  selector: "app-status-cell",
  template: `<span [class]="'badge badge-' + value">{{ value }}</span>`,
})
export class StatusCell implements ICellRendererAngularComp {
  value = "";

  agInit(params: ICellRendererParams): void {
    this.value = params.value;
  }

  refresh(params: ICellRendererParams): boolean {
    this.value = params.value;
    return true;
  }
}
```

```ts
colDefs: ColDef[] = [{ field: 'status', cellRenderer: StatusCell }];
```

For simple formatting, use `valueFormatter` instead of a component. It is much cheaper.

## 215: How do you access the AG Grid API?

Use the `gridReady` event, which gives you the `GridApi`:

```ts
private gridApi!: GridApi<Car>;

onGridReady(event: GridReadyEvent<Car>) {
  this.gridApi = event.api;
}

exportCsv() {
  this.gridApi.exportDataAsCsv();
}

clearFilters() {
  this.gridApi.setFilterModel(null);
}
```

```html
<ag-grid-angular
  [rowData]="rows"
  [columnDefs]="cols"
  (gridReady)="onGridReady($event)"
/>
```

## 216: Why should you set getRowId in AG Grid?

`getRowId` tells the grid how to identify each row (usually by your database ID). Without it, when you give the grid a new `rowData` array, it treats all rows as new and re-renders them, which loses selection and scroll position and is slower. With it, AG Grid updates only changed rows.

```ts
getRowId = (params: GetRowIdParams<Car>) => String(params.data.id);
```

## 217: What row models does AG Grid have?

- **Client-Side**: all data is loaded into the grid. The default. Good up to roughly hundreds of thousands of rows.
- **Infinite**: loads blocks of rows as you scroll. Free.
- **Server-Side** (Enterprise): loads data lazily with server-side grouping, sorting and filtering, for very large data sets.
- **Viewport** (Enterprise): the server decides which rows are in view, for live data like trading screens.

## 218: How do you update a chart in ng2-charts when data changes?

The chart redraws when you pass a new `data` object. If you mutate the existing object, call `update()` on the `BaseChartDirective`:

```ts
chart = viewChild(BaseChartDirective);

addPoint(value: number) {
  this.data.datasets[0].data.push(value);
  this.data.labels?.push(`Day ${this.data.labels.length + 1}`);
  this.chart()?.update();
}
```

Creating a new object (`this.data = { ...newData }`) is the cleaner option and works well with signals.

## 219: How do you make Formly use custom field types?

Create a component that extends `FieldType` and register it:

```ts
import { Component } from "@angular/core";
import { ReactiveFormsModule } from "@angular/forms";
import { FieldType, FieldTypeConfig, FormlyModule } from "@ngx-formly/core";

@Component({
  selector: "app-formly-color",
  imports: [ReactiveFormsModule, FormlyModule],
  template: `<input
    type="color"
    [formControl]="formControl"
    [formlyAttributes]="field"
  />`,
})
export class FormlyColorField extends FieldType<FieldTypeConfig> {}
```

```ts
importProvidersFrom(
  FormlyModule.forRoot({
    types: [{ name: "color", component: FormlyColorField }],
  }),
);
```

Now `{ key: 'brandColor', type: 'color' }` renders your component.

## 220: How do you show or hide Formly fields based on other values?

Use `expressions` (named `expressionProperties` and `hideExpression` in older versions):

```ts
fields: FormlyFieldConfig[] = [
  { key: 'hasCompany', type: 'checkbox', props: { label: 'I represent a company' } },
  {
    key: 'companyName',
    type: 'input',
    props: { label: 'Company name' },
    expressions: {
      hide: '!model.hasCompany',
      'props.required': 'model.hasCompany',
    },
  },
];
```

Expressions can be strings or functions that receive the field.

## 221: How do you add custom validation in Formly?

Register a validator globally and reference it by name, or put a validator function directly on the field:

```ts
export function ipValidator(control: AbstractControl): ValidationErrors | null {
  return /^(\d{1,3}\.){3}\d{1,3}$/.test(control.value) ? null : { ip: true };
}

FormlyModule.forRoot({
  validators: [{ name: "ip", validation: ipValidator }],
  validationMessages: [{ name: "ip", message: "Not a valid IP address" }],
});
```

```ts
{ key: 'ip', type: 'input', validators: { validation: ['ip'] } }
```

## 222: When should you not use Formly?

Formly is great when forms are generated from data or when you have many similar forms. It is less helpful when:

- you have a few hand-designed forms with special layouts
- the team doesn't know Formly and the config hides what is happening
- you need behavior that would require many custom types and wrappers

In those cases plain reactive forms (or the new signal forms) are easier to read and debug.

## 223: How do you use ng-select with async search?

```ts
import { Component, inject } from "@angular/core";
import { NgSelectComponent } from "@ng-select/ng-select";
import { FormsModule } from "@angular/forms";
import { Subject, debounceTime, switchMap, concat, of } from "rxjs";
import { UsersApi, User } from "./users-api";

@Component({
  selector: "app-user-picker",
  imports: [NgSelectComponent, FormsModule],
  template: `
    <ng-select
      [items]="users$ | async"
      bindLabel="name"
      [typeahead]="search$"
      [loading]="false"
      [(ngModel)]="selected"
    />
  `,
})
export class UserPicker {
  private api = inject(UsersApi);
  search$ = new Subject<string>();
  selected: User | null = null;

  users$ = concat(
    of([] as User[]),
    this.search$.pipe(
      debounceTime(300),
      switchMap((term) => this.api.search(term)),
    ),
  );
}
```

Add `AsyncPipe` to imports. `[typeahead]` turns off local filtering and sends every typed term to the subject.

## 224: How do you show a custom option template in ng-select?

```html
<ng-select [items]="users" bindLabel="name" [(ngModel)]="selected">
  <ng-template ng-option-tmp let-item="item">
    <img [src]="item.avatar" width="20" /> {{ item.name }}
    <small>{{ item.email }}</small>
  </ng-template>
  <ng-template ng-label-tmp let-item="item">{{ item.name }}</ng-template>
</ng-select>
```

## 225: How do you set up ngx-toastr in a standalone app?

```ts
import { provideAnimations } from "@angular/platform-browser/animations";
import { provideToastr } from "ngx-toastr";

export const appConfig = {
  providers: [
    provideAnimations(),
    provideToastr({
      timeOut: 4000,
      positionClass: "toast-bottom-right",
      preventDuplicates: true,
    }),
  ],
};
```

Also add `node_modules/ngx-toastr/toastr.css` to the styles in `angular.json`.

## 226: How do you show error toasts for every failed HTTP request?

Use a functional interceptor:

```ts
import { HttpErrorResponse, HttpInterceptorFn } from "@angular/common/http";
import { inject } from "@angular/core";
import { ToastrService } from "ngx-toastr";
import { catchError, throwError } from "rxjs";

export const errorToastInterceptor: HttpInterceptorFn = (req, next) => {
  const toastr = inject(ToastrService);
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status !== 401) {
        toastr.error(error.error?.message ?? "Something went wrong");
      }
      return throwError(() => error);
    }),
  );
};
```

```ts
provideHttpClient(withInterceptors([errorToastInterceptor]));
```

Rethrow the error so the calling code can still react to it.

## 227: How do you set up angular-oauth2-oidc in a standalone app?

```ts
import { provideHttpClient } from "@angular/common/http";
import { provideOAuthClient } from "angular-oauth2-oidc";

export const appConfig = {
  providers: [
    provideHttpClient(),
    provideOAuthClient({
      resourceServer: {
        allowedUrls: ["https://api.example.com"],
        sendAccessToken: true,
      },
    }),
  ],
};
```

With `sendAccessToken: true`, the library's interceptor adds the token to requests that go to the allowed URLs. Make sure `HttpClient` is set up to use DI-based interceptors (`withInterceptorsFromDi()`) if the library registers a class-based interceptor.

## 228: How do you refresh tokens automatically with angular-oauth2-oidc?

Request the `offline_access` scope (if your provider uses refresh tokens) and turn on automatic refresh:

```ts
oauth.configure(authConfig);
oauth.setupAutomaticSilentRefresh();
await oauth.loadDiscoveryDocumentAndTryLogin();
```

The library refreshes the token shortly before it expires. With the code flow it uses the refresh token. Listen to `oauth.events` to react to `token_refresh_error` and send the user to log in again.

## 229: How do you protect routes and API calls with MSAL Angular?

Register `MsalGuard` on routes and `MsalInterceptor` for APIs, with a `protectedResourceMap` that says which scopes each API needs:

```ts
{
  provide: MSAL_INTERCEPTOR_CONFIG,
  useValue: {
    interactionType: InteractionType.Redirect,
    protectedResourceMap: new Map([
      ['https://graph.microsoft.com/v1.0/me', ['user.read']],
      ['https://api.example.com/', ['api://my-api/access']],
    ]),
  },
}
```

```ts
{ path: 'profile', component: Profile, canActivate: [MsalGuard] }
```

You also need to handle the redirect result, usually with `MsalRedirectComponent` or `handleRedirectObservable()` at startup.

## 230: How do you add the Auth0 access token to API calls?

```ts
import { provideHttpClient, withInterceptors } from "@angular/common/http";
import { provideAuth0, authHttpInterceptorFn } from "@auth0/auth0-angular";

export const appConfig = {
  providers: [
    provideHttpClient(withInterceptors([authHttpInterceptorFn])),
    provideAuth0({
      domain: "my-tenant.eu.auth0.com",
      clientId: "abc123",
      authorizationParams: {
        redirect_uri: window.location.origin,
        audience: "https://api.example.com",
      },
      httpInterceptor: {
        allowedList: ["https://api.example.com/*"],
      },
    }),
  ],
};
```

Only requests matching `allowedList` get the token, so you don't leak it to third-party APIs.

## 231: How do you use keycloak-angular in a standalone app?

Recent versions use `provideKeycloak`:

```ts
import { provideKeycloak } from "keycloak-angular";

export const appConfig = {
  providers: [
    provideKeycloak({
      config: {
        url: "https://auth.example.com",
        realm: "demo",
        clientId: "spa",
      },
      initOptions: {
        onLoad: "check-sso",
        silentCheckSsoRedirectUri:
          window.location.origin + "/silent-check-sso.html",
      },
    }),
  ],
};
```

Then you can inject `Keycloak` (from `keycloak-js`) to get tokens and user info, and use the library's helpers to build role-based guards and a bearer token interceptor. Older versions used `KeycloakService` and `APP_INITIALIZER`.

## 232: How do you set up Sentry in an Angular app?

```ts
// main.ts
import * as Sentry from "@sentry/angular";

Sentry.init({
  dsn: "https://key@o0.ingest.sentry.io/0",
  integrations: [Sentry.browserTracingIntegration()],
  tracesSampleRate: 0.2,
  environment: "production",
});
```

```ts
// app.config.ts
import { ErrorHandler } from "@angular/core";
import * as Sentry from "@sentry/angular";

export const appConfig = {
  providers: [{ provide: ErrorHandler, useValue: Sentry.createErrorHandler() }],
};
```

Upload source maps in CI (with `@sentry/cli` or the Sentry wizard) so stack traces show your TypeScript code. Don't deploy the source maps publicly unless you want to.

## 233: How do you configure Jest for an Angular project?

The common setup uses `jest-preset-angular`:

```bash
npm install -D jest jest-preset-angular @types/jest
```

```ts
// jest.config.ts
import type { Config } from "jest";

const config: Config = {
  preset: "jest-preset-angular",
  setupFilesAfterEnv: ["<rootDir>/setup-jest.ts"],
  testPathIgnorePatterns: ["/node_modules/", "/dist/"],
};

export default config;
```

```ts
// setup-jest.ts
import { setupZonelessTestEnv } from "jest-preset-angular/setup-env/zoneless";

setupZonelessTestEnv();
```

Use `setupZoneTestEnv` instead if the app still uses Zone.js. In Nx workspaces this is generated for you.

## 234: How do you use Vitest with the Angular CLI?

In recent Angular versions, new projects use Vitest by default through the `@angular/build:unit-test` builder:

```json
"test": {
  "builder": "@angular/build:unit-test"
}
```

```bash
ng test
ng test --watch=false --coverage
```

Tests use `describe`, `it` and `expect` from Vitest, and `TestBed` works as usual. Tests run in jsdom (or happy-dom) by default, and you can run them in a real browser with Vitest browser mode. Analog's `@analogjs/vitest-angular` is another way to set it up, often used in Nx and older projects.

## 235: How do you migrate tests from Jasmine to Jest or Vitest?

Most code stays the same since all use `describe`, `it`, `beforeEach` and `expect`. The changes are mainly:

- `jasmine.createSpy()` and `spyOn` become `jest.fn()`/`vi.fn()` and `jest.spyOn`/`vi.spyOn`
- `and.returnValue(x)` becomes `mockReturnValue(x)`
- `toHaveBeenCalledOnceWith` and some matchers have different names
- `jasmine.clock()` becomes fake timers (`vi.useFakeTimers()`)

Angular has a schematic for moving to Vitest that rewrites many of these, and there are community codemods for Jest.

## 236: How do you test a service with Spectator?

```ts
import {
  createServiceFactory,
  SpectatorService,
  mockProvider,
} from "@ngneat/spectator/vitest";
import { of } from "rxjs";
import { CartService } from "./cart.service";
import { PricesApi } from "./prices-api";

describe("CartService", () => {
  let spectator: SpectatorService<CartService>;
  const createService = createServiceFactory({
    service: CartService,
    providers: [mockProvider(PricesApi, { getPrice: () => of(10) })],
  });

  beforeEach(() => (spectator = createService()));

  it("calculates the total", () => {
    spectator.service.add("apple", 3);
    expect(spectator.service.total()).toBe(30);
  });
});
```

Spectator has entry points for Jasmine, Jest (`/jest`) and Vitest (`/vitest`), so spies match your runner.

## 237: How do you test HTTP calls with Spectator?

Use `createHttpFactory`:

```ts
import {
  createHttpFactory,
  HttpMethod,
  SpectatorHttp,
} from "@ngneat/spectator/jest";
import { TodosApi } from "./todos-api";

describe("TodosApi", () => {
  let spectator: SpectatorHttp<TodosApi>;
  const createHttp = createHttpFactory(TodosApi);

  beforeEach(() => (spectator = createHttp()));

  it("loads todos", () => {
    spectator.service.getAll().subscribe();
    const req = spectator.expectOne("/api/todos", HttpMethod.GET);
    req.flush([{ id: 1, title: "Test" }]);
  });
});
```

It uses `HttpTestingController` under the hood.

## 238: How do you set inputs and listen to outputs with Spectator?

```ts
const createComponent = createComponentFactory(Rating);

it("emits the selected value", () => {
  const spectator = createComponent({ props: { max: 5 } });
  let selected = 0;
  spectator.output("rated").subscribe((value) => (selected = value as number));

  spectator.setInput("max", 3);
  spectator.click('[data-star="2"]');

  expect(selected).toBe(2);
});
```

`setInput` works with signal inputs too.

## 239: What is MockBuilder in ng-mocks?

`MockBuilder` sets up the testing module for you: it keeps the thing you test real and mocks everything else it depends on.

```ts
import { MockBuilder, MockRender, ngMocks } from "ng-mocks";
import { ProfilePage } from "./profile-page";
import { UserService } from "./user.service";

describe("ProfilePage", () => {
  beforeEach(() =>
    MockBuilder(ProfilePage).mock(UserService, {
      current: () => ({ name: "Anna" }),
    }),
  );

  it("shows the user name", () => {
    MockRender(ProfilePage);
    expect(ngMocks.formatText(ngMocks.find("h1"))).toBe("Anna");
  });
});
```

Child components used by `ProfilePage` are automatically replaced with empty mocks.

## 240: What is the difference between shallow and deep component tests?

- **Shallow**: only the component under test is real. Children are mocked (ng-mocks, Spectator's `shallow: true`). Tests are fast and focused but can miss problems in how components work together.
- **Deep**: real children are rendered. Tests are closer to real usage (the Testing Library style) but slower and more fragile when children change.

A common mix is shallow tests for complex logic and deep tests for important user flows.

## 241: How do you query elements the right way in Angular Testing Library?

Prefer queries that match how users find things, in this order:

1. `getByRole` (with `name`), for example `getByRole('button', { name: /save/i })`
2. `getByLabelText` for form fields
3. `getByPlaceholderText`, `getByText`
4. `getByTestId` only when nothing else works

`getBy*` throws if not found, `queryBy*` returns `null` (good for checking something is absent), and `findBy*` waits for the element (good after async actions).

## 242: How do you provide mocks in Angular Testing Library's render?

`render` takes the same options as `TestBed`, plus inputs:

```ts
await render(OrderSummary, {
  inputs: { orderId: 42 },
  providers: [{ provide: OrdersApi, useValue: { get: () => of(mockOrder) } }],
});

expect(await screen.findByText("Total: $30.00")).toBeTruthy();
```

## 243: How do you set up Cypress component testing in Angular?

Run Cypress and pick component testing, which detects the Angular CLI and creates the config. Then:

```ts
import { Counter } from "./counter";

describe("Counter", () => {
  it("increments", () => {
    cy.mount(Counter, { componentProperties: { start: 5 } });
    cy.contains("button", "+").click();
    cy.contains("6");
  });
});
```

The component runs in a real browser, which is useful for things jsdom can't do well, like layout, drag and drop or canvas.

## 244: How do you add Playwright to an Angular project?

```bash
npm init playwright@latest
```

Point `baseURL` and `webServer` at your dev server:

```ts
// playwright.config.ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  use: { baseURL: "http://localhost:4200" },
  webServer: {
    command: "npm start",
    url: "http://localhost:4200",
    reuseExistingServer: true,
  },
});
```

```ts
import { test, expect } from "@playwright/test";

test("user can log in", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill("anna@example.com");
  await page.getByLabel("Password").fill("secret");
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
});
```

## 245: How do you mock API responses in Playwright?

Use `page.route`:

```ts
test("shows empty state", async ({ page }) => {
  await page.route("**/api/orders", (route) => route.fulfill({ json: [] }));
  await page.goto("/orders");
  await expect(page.getByText("No orders yet")).toBeVisible();
});
```

This makes e2e tests independent from the real backend. Keep a few tests against a real backend too, to catch contract problems.

## 246: How do you use Storybook with Angular components that need providers?

Use `applicationConfig` for app-level providers and `moduleMetadata` for imports:

```ts
import type { Meta, StoryObj } from "@storybook/angular";
import { applicationConfig } from "@storybook/angular";
import { provideHttpClient } from "@angular/common/http";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";
import { UserCard } from "./user-card";

const meta: Meta<UserCard> = {
  component: UserCard,
  decorators: [
    applicationConfig({
      providers: [provideHttpClient(), provideAnimationsAsync()],
    }),
  ],
};
export default meta;

export const Default: StoryObj<UserCard> = {
  args: { name: "Anna", role: "Admin" },
};
```

## 247: How do you set up Nx for an existing Angular CLI project?

```bash
npx nx@latest init
```

This adds Nx on top of your workspace and keeps `angular.json` working. You get caching and `nx affected` right away. Later you can split the app into libraries with Nx generators and add module boundary rules. For new projects you can start with `npx create-nx-workspace --preset=angular-monorepo`.

## 248: What is `nx affected` and why is it useful?

`nx affected -t test` runs a target only for projects affected by the changes since a base commit (usually `main`). Nx knows the dependency graph between your apps and libraries, so if you change one library it runs tests only for that library and the projects that use it. In a big monorepo, this cuts CI time a lot.

## 249: What are Nx module boundary rules?

You tag projects (for example `type:feature`, `type:ui`, `type:data-access`, `scope:admin`) and then set rules in ESLint (`@nx/enforce-module-boundaries`) about which tags can import which:

```json
{
  "depConstraints": [
    {
      "sourceTag": "type:ui",
      "onlyDependOnLibsWithTags": ["type:ui", "type:util"]
    },
    {
      "sourceTag": "scope:admin",
      "onlyDependOnLibsWithTags": ["scope:admin", "scope:shared"]
    }
  ]
}
```

Lint fails if someone imports a feature library from a UI library, which keeps the architecture clean as the repo grows.

## 250: How do you configure angular-eslint with the flat config?

`ng add angular-eslint` creates an `eslint.config.js` similar to this:

```js
const eslint = require("@eslint/js");
const tseslint = require("typescript-eslint");
const angular = require("angular-eslint");

module.exports = tseslint.config(
  {
    files: ["**/*.ts"],
    extends: [
      eslint.configs.recommended,
      ...tseslint.configs.recommended,
      ...angular.configs.tsRecommended,
    ],
    processor: angular.processInlineTemplates,
    rules: {
      "@angular-eslint/component-selector": [
        "error",
        { type: "element", prefix: "app", style: "kebab-case" },
      ],
    },
  },
  {
    files: ["**/*.html"],
    extends: [
      ...angular.configs.templateRecommended,
      ...angular.configs.templateAccessibility,
    ],
    rules: {},
  },
);
```

`processInlineTemplates` lets ESLint lint templates written inside the `.ts` file.

## 251: Which angular-eslint template rules are worth turning on?

Some useful ones beyond the recommended set:

- `@angular-eslint/template/prefer-control-flow`: use `@if`/`@for` instead of `*ngIf`/`*ngFor`
- `@angular-eslint/template/prefer-self-closing-tags`
- `@angular-eslint/template/no-call-expression`: avoid calling methods in templates (signals are allowed)
- `@angular-eslint/template/use-track-by-function` for old `*ngFor`
- the accessibility set: `alt-text`, `label-has-associated-control`, `click-events-have-key-events`, `interactive-supports-focus`
- `@angular-eslint/prefer-on-push-component-change-detection` and `@angular-eslint/prefer-signals` on the TypeScript side

## 252: How do you set up Native Federation for a host and a remote?

```bash
ng add @angular-architects/native-federation --project shell --type dynamic-host --port 4200
ng add @angular-architects/native-federation --project mfe1 --type remote --port 4201
```

The remote exposes files in `federation.config.js`:

```js
const {
  withNativeFederation,
  shareAll,
} = require("@angular-architects/native-federation/config");

module.exports = withNativeFederation({
  name: "mfe1",
  exposes: { "./routes": "./projects/mfe1/src/app/app.routes.ts" },
  shared: {
    ...shareAll({
      singleton: true,
      strictVersion: true,
      requiredVersion: "auto",
    }),
  },
});
```

The host loads it in a route:

```ts
import { loadRemoteModule } from "@angular-architects/native-federation";

export const routes: Routes = [
  {
    path: "flights",
    loadChildren: () =>
      loadRemoteModule("mfe1", "./routes").then((m) => m.routes),
  },
];
```

The host's `main.ts` calls `initFederation('/federation.manifest.json')` before bootstrapping, and the manifest lists where each remote lives.

## 253: What is the difference between Module Federation and Native Federation for Angular?

- **Module Federation** (`@angular-architects/module-federation`) is a Webpack feature. It needs the Webpack-based builder, which the Angular CLI no longer uses by default.
- **Native Federation** gives the same mental model (remotes, exposes, shared dependencies) but works with the esbuild-based `@angular/build` and any bundler. It uses import maps and ES modules at runtime.

For new Angular projects, Native Federation is the usual recommendation. Older micro frontend setups still use Module Federation with a custom Webpack builder.

## 254: How do you get route params as signals with ngxtension?

```ts
import { Component, computed } from "@angular/core";
import { injectParams } from "ngxtension/inject-params";
import { injectQueryParams } from "ngxtension/inject-query-params";

@Component({
  selector: "app-product",
  template: `Product {{ id() }}, tab {{ tab() }}`,
})
export class Product {
  id = injectParams("id");
  tab = injectQueryParams("tab");
  numericId = computed(() => Number(this.id()));
}
```

Angular can also bind route params to signal inputs with `withComponentInputBinding()`, which covers many of the same cases without a library.

## 255: What does derivedAsync in ngxtension do?

`derivedAsync` creates a signal from an async source (observable or promise) that depends on other signals. When the signals change, it runs again and cancels the previous one, similar to `switchMap`:

```ts
import { derivedAsync } from "ngxtension/derived-async";

userId = input.required<number>();
user = derivedAsync(() => this.api.getUser(this.userId()));
```

Today Angular's `resource()` and `rxResource()` solve the same problem in the framework itself.

## 256: What is RxAngular's rxLet and when would you use it?

`*rxLet` renders the value of an observable (or signal) and updates only that part of the template when it emits, without running change detection for the whole component. It also has templates for suspense, error and complete states.

```html
<ng-container *rxLet="price$; let price; suspense: loading"
  >{{ price | currency }}</ng-container
>
<ng-template #loading>Loading...</ng-template>
```

It's useful for very frequent updates, like live prices. With signals and zoneless Angular, the built-in solution covers most cases, so new apps need it less.

## 257: What replaced @ngneat/until-destroy?

`@ngneat/until-destroy` added a decorator and an `untilDestroyed(this)` operator to unsubscribe when a component is destroyed. Angular now has this built in:

```ts
import { DestroyRef, inject } from "@angular/core";
import { takeUntilDestroyed } from "@angular/core/rxjs-interop";

export class Clock {
  constructor() {
    interval(1000)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.tick());
  }

  tick() {}
}
```

Outside the injection context, pass a `DestroyRef`: `takeUntilDestroyed(this.destroyRef)`. You can remove the library in modern apps.

## 258: How do you choose between ngx-cookie-service and localStorage?

Use cookies when the server needs the value (the browser sends cookies with requests), or you need expiry dates and domain/path rules. Use `localStorage` for bigger client-only data that the server doesn't need, like UI preferences.

Auth tokens are best kept in `HttpOnly` cookies set by the server, which JavaScript can't read at all. ngx-cookie-service can't create `HttpOnly` cookies, because that is only possible from the server.

## 259: How do you add syntax highlighting to ngx-markdown?

Install Prism and enable it:

```ts
import { provideMarkdown } from "ngx-markdown";

export const appConfig = {
  providers: [provideHttpClient(), provideMarkdown()],
};
```

```json
"scripts": ["node_modules/prismjs/prism.js", "node_modules/prismjs/components/prism-typescript.min.js"],
"styles": ["node_modules/prismjs/themes/prism-okaidia.css"]
```

```html
<markdown [data]="content" />
```

ngx-markdown sanitizes the HTML by default. Don't turn sanitization off for user-written Markdown.

## 260: How do you use @angular/google-maps with markers from data?

```ts
import { Component, input } from "@angular/core";
import {
  GoogleMap,
  MapAdvancedMarker,
  MapInfoWindow,
} from "@angular/google-maps";

interface Store {
  id: number;
  name: string;
  position: google.maps.LatLngLiteral;
}

@Component({
  selector: "app-store-map",
  imports: [GoogleMap, MapAdvancedMarker],
  template: `
    <google-map
      height="500px"
      width="100%"
      [center]="{ lat: 52.52, lng: 13.4 }"
      [zoom]="11"
      mapId="DEMO_MAP_ID"
    >
      @for (store of stores(); track store.id) {
        <map-advanced-marker [position]="store.position" [title]="store.name" />
      }
    </google-map>
  `,
})
export class StoreMap {
  stores = input.required<Store[]>();
}
```

Advanced markers need a `mapId`. The older `map-marker` uses the deprecated `google.maps.Marker`.

## 261: Which libraries are used for maps besides Google Maps?

- **Leaflet** with `@bluehalo/ngx-leaflet` (formerly `@asymmetrik/ngx-leaflet`): open source, works with OpenStreetMap tiles
- **MapLibre/Mapbox GL** with `@maplibre/ngx-maplibre-gl` or `ngx-mapbox-gl`: vector maps, 3D
- **OpenLayers**: very powerful for GIS apps, usually used directly or with small wrappers

Many teams use Leaflet or OpenLayers directly in a component, since the wrappers are thin.

## 262: How do you wrap a plain JavaScript library in an Angular component?

Create the library instance after the view is ready, pass inputs through, and destroy it on cleanup. For example with a chart or map library:

```ts
import {
  Component,
  ElementRef,
  afterNextRender,
  effect,
  inject,
  input,
  DestroyRef,
} from "@angular/core";
import { Chart, ChartConfiguration } from "chart.js/auto";

@Component({ selector: "app-line-chart", template: `<canvas></canvas>` })
export class LineChart {
  config = input.required<ChartConfiguration>();
  private host = inject(ElementRef<HTMLElement>);
  private chart?: Chart;

  constructor() {
    afterNextRender(() => {
      const canvas = this.host.nativeElement.querySelector("canvas")!;
      this.chart = new Chart(canvas, this.config());
    });

    effect(() => {
      const cfg = this.config();
      if (this.chart) {
        this.chart.data = cfg.data;
        this.chart.update();
      }
    });

    inject(DestroyRef).onDestroy(() => this.chart?.destroy());
  }
}
```

`afterNextRender` runs only in the browser, so it is also SSR safe.

## 263: How do you lazy load a heavy library only when needed?

Use a dynamic `import()` so the bundler puts it in a separate chunk:

```ts
async exportToExcel(rows: Row[]) {
  const XLSX = await import('xlsx');
  const sheet = XLSX.utils.json_to_sheet(rows);
  const book = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(book, sheet, 'Data');
  XLSX.writeFile(book, 'export.xlsx');
}
```

For components that use a heavy library, wrap them in `@defer` in the template so their code loads only when shown.

## 264: How do you use @defer with a heavy chart component?

```html
@defer (on viewport) {
<app-sales-chart [data]="sales()" />
} @placeholder {
<div class="chart-placeholder">Chart</div>
} @loading (minimum 300ms) {
<app-spinner />
}
```

The chart component, and libraries like ECharts or Chart.js that only it imports, go into a separate chunk loaded when the placeholder scrolls into view. The deferred component must be standalone and not referenced anywhere else in the same file.

## 265: How do you check how much a library adds to your bundle?

- Look at the build output from `ng build`, which lists chunk sizes.
- Use `ng build --stats-json` and open `stats.json` in esbuild's bundle analyzer, or use `source-map-explorer` with source maps.
- Check the package on bundlephobia or pkg-size before installing.
- Set `budgets` in `angular.json` so the build warns or fails when bundles grow too much.

## 266: Why does the CLI warn about CommonJS dependencies?

Angular builds work best with ES modules, which can be tree-shaken. When a library is published only as CommonJS, the bundler can't remove unused code well, and the CLI prints a warning. Options:

- find an ESM version (`lodash-es` instead of `lodash`)
- replace the library
- if you accept it, add it to `allowedCommonJsDependencies` in `angular.json` to hide the warning

## 267: How do you use a library that touches `window` or `document` with SSR?

On the server there is no `window`. Options:

- Run browser-only code in `afterNextRender` or `afterEveryRender`, which run only in the browser.
- Check `isPlatformBrowser(inject(PLATFORM_ID))` before using it.
- Load the library with a dynamic `import()` inside browser-only code, so it is not even evaluated on the server.
- Wrap the component in `@defer` so it renders only on the client.

```ts
afterNextRender(async () => {
  const { default: Swiper } = await import("swiper");
  new Swiper(this.el.nativeElement);
});
```

## 268: How do you make Material or CDK components work with SSR and hydration?

Angular Material and the CDK support SSR and hydration out of the box. Things to watch:

- `BreakpointObserver` can't know the screen size on the server, so the server render uses the default value. Pick a sensible default to avoid layout jumps.
- Overlays, dialogs and snack bars are opened in response to user actions, so they only appear in the browser anyway.
- Don't read DOM sizes in constructors. Use `afterNextRender`.

## 269: How do you replace Moment.js in an Angular Material project?

1. Install date-fns (or Luxon) and the matching adapter: `@angular/material-date-fns-adapter`.
2. Replace the Moment adapter provider:

```ts
import { provideDateFnsAdapter } from "@angular/material-date-fns-adapter";
import { MAT_DATE_LOCALE } from "@angular/material/core";
import { enUS } from "date-fns/locale";

providers: [
  provideDateFnsAdapter(),
  { provide: MAT_DATE_LOCALE, useValue: enUS },
];
```

3. Replace `moment()` calls with date-fns functions (`format`, `addDays`, `parseISO`).
4. Note that the form control values become `Date` objects instead of Moment objects.

## 270: How do you customize the date format of the Material date picker?

Provide `MAT_DATE_FORMATS` (with the adapter you use):

```ts
import { MAT_DATE_FORMATS } from "@angular/material/core";

export const MY_FORMATS = {
  parse: { dateInput: "dd.MM.yyyy" },
  display: {
    dateInput: "dd.MM.yyyy",
    monthYearLabel: "MMM yyyy",
    dateA11yLabel: "PP",
    monthYearA11yLabel: "MMMM yyyy",
  },
};

providers: [provideDateFnsAdapter(MY_FORMATS)];
```

The format tokens depend on the adapter (date-fns tokens here). The native adapter can't parse custom formats, which is a common reason to switch adapters.

## 271: How do you use Tailwind together with Angular Material?

They can live together, but watch for:

- Tailwind's base styles (preflight) reset some element styles, which can affect Material components. Check buttons and inputs after adding it.
- Use Tailwind for layout and spacing, and Material tokens and override mixins for component styling.
- Map Material system tokens into your Tailwind theme so both use the same colors:

```css
@import "tailwindcss";

@theme {
  --color-primary: var(--mat-sys-primary);
  --color-surface: var(--mat-sys-surface);
}
```

## 272: How do you choose between Angular Material, PrimeNG and NG-ZORRO for a new project?

- **Angular Material**: official, best long-term support, follows Angular releases exactly, great accessibility. Smaller component set and Material look.
- **PrimeNG**: very big component set (advanced table, tree table, charts, editor), flexible themes, unstyled mode. Updates sometimes bring breaking changes.
- **NG-ZORRO**: Ant Design look, many components for data-heavy admin apps, good docs.

Pick based on the design you need, the components you need, and how much you want to depend on a third party.

## 273: What is the Spartan helm CLI workflow?

You add Spartan with its Nx or Angular CLI generators. When you want a component, you run a generator that copies the helm (styled) code into your project, for example a button or dialog. The helm code imports the brain primitives from `@spartan-ng/brain`. Since the helm code is now in your repo, you change it freely, and updates to brain come through npm. This "copy the UI code, install the logic" model is the same as shadcn/ui.

## 274: How do you handle forms in Ionic Angular apps?

Ionic inputs (`ion-input`, `ion-select`, `ion-checkbox`, `ion-toggle`) have value accessors, so they work with reactive forms and `ngModel`:

```html
<form [formGroup]="form">
  <ion-input
    label="Email"
    labelPlacement="floating"
    formControlName="email"
    type="email"
  />
  <ion-toggle formControlName="newsletter">Newsletter</ion-toggle>
</form>
```

With the standalone build, import `IonInput`, `IonToggle` and `ReactiveFormsModule` in the component.

## 275: How do you navigate in Ionic Angular?

Ionic uses the Angular router with `ion-router-outlet`, which adds mobile-style page transitions and keeps previous pages in memory. `NavController` adds direction-aware navigation:

```ts
const nav = inject(NavController);
nav.navigateForward("/details/1");
nav.navigateBack("/list");
nav.navigateRoot("/home");
```

Because pages stay alive in the stack, use Ionic's `ionViewWillEnter`/`ionViewDidEnter` hooks for code that should run every time a page is shown, since `ngOnInit` runs only once.

## 276: How do you build a dynamic form from a server schema without Formly?

Loop over the field definitions and build a `FormGroup`, then render with `@switch`:

```ts
interface FieldDef {
  key: string;
  label: string;
  type: 'text' | 'number' | 'select';
  required?: boolean;
  options?: string[];
}

buildForm(fields: FieldDef[]) {
  const group: Record<string, FormControl> = {};
  for (const f of fields) {
    group[f.key] = new FormControl('', f.required ? Validators.required : null);
  }
  return new FormGroup(group);
}
```

```html
@for (f of fields(); track f.key) { @switch (f.type) { @case ('select') {
<select [formControlName]="f.key">
  @for (o of f.options; track o) {
  <option [value]="o">{{ o }}</option>
  }
</select>
} @default {
<input [type]="f.type" [formControlName]="f.key" [placeholder]="f.label" />
} } }
```

For a few field types this is easier to own than Formly.

## 277: What is @ngneat/reactive-forms and is it still needed?

`@ngneat/reactive-forms` added strong typing to Angular reactive forms. Angular got typed reactive forms in version 14, so you no longer need it. Signal forms are the next step in Angular itself. You may still see it in older projects, where it can be replaced gradually.

## 278: How do you use the CDK listbox and menu?

`@angular/cdk/listbox` and `@angular/cdk/menu` give you accessible behavior without styles:

```html
<ul
  cdkListbox
  [cdkListboxValue]="['red']"
  (cdkListboxValueChange)="onChange($event)"
>
  <li cdkOption="red">Red</li>
  <li cdkOption="green">Green</li>
</ul>

<button [cdkMenuTriggerFor]="menu">Options</button>
<ng-template #menu>
  <div cdkMenu>
    <button cdkMenuItem (cdkMenuItemTriggered)="rename()">Rename</button>
    <button cdkMenuItem (cdkMenuItemTriggered)="remove()">Delete</button>
  </div>
</ng-template>
```

Keyboard navigation, focus and ARIA roles are handled for you. Newer projects can also look at Angular Aria for the same kind of headless patterns.

## 279: How do you trap focus inside a custom modal?

```html
<div
  class="modal"
  role="dialog"
  aria-modal="true"
  cdkTrapFocus
  [cdkTrapFocusAutoCapture]="true"
>
  <h2>Settings</h2>
  <input />
  <button (click)="close()">Close</button>
</div>
```

`cdkTrapFocusAutoCapture` moves focus into the modal when it opens and gives it back to the previously focused element when it closes. Import `A11yModule` or `CdkTrapFocus`.

## 280: How do you style keyboard focus only (not mouse focus) with the CDK?

`FocusMonitor` (and the `cdkMonitorElementFocus` directive) adds classes like `cdk-keyboard-focused`, `cdk-mouse-focused` and `cdk-program-focused`:

```html
<button cdkMonitorElementFocus class="btn">Save</button>
```

```css
.btn.cdk-keyboard-focused {
  outline: 2px solid var(--mat-sys-primary);
}
```

Today the CSS `:focus-visible` selector solves most of this without JavaScript.

## 281: How do you use Lucide icons in Angular?

```ts
import { Component } from "@angular/core";
import { LucideAngularModule, Trash2 } from "lucide-angular";

@Component({
  selector: "app-delete-button",
  imports: [LucideAngularModule],
  template: `<button><lucide-icon [img]="trash" size="16" /> Delete</button>`,
})
export class DeleteButton {
  trash = Trash2;
}
```

Passing the icon object means only that icon is bundled.

## 282: How do you show a global loading bar for HTTP requests yourself?

A small interceptor and a signal is often enough instead of a library:

```ts
import { Injectable, computed, signal, inject } from "@angular/core";
import { HttpInterceptorFn } from "@angular/common/http";
import { finalize } from "rxjs";

@Injectable({ providedIn: "root" })
export class LoadingService {
  private active = signal(0);
  loading = computed(() => this.active() > 0);
  start() {
    this.active.update((n) => n + 1);
  }
  stop() {
    this.active.update((n) => n - 1);
  }
}

export const loadingInterceptor: HttpInterceptorFn = (req, next) => {
  const loading = inject(LoadingService);
  loading.start();
  return next(req).pipe(finalize(() => loading.stop()));
};
```

```html
@if (loading.loading()) {
<mat-progress-bar mode="indeterminate" />
}
```

## 283: How do you run Storybook interaction tests for Angular?

Add a `play` function to a story. It runs after the story renders and uses Testing Library style queries:

```ts
import { expect, userEvent, within } from "storybook/test";

export const SubmitsForm: StoryObj<LoginForm> = {
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    await userEvent.type(canvas.getByLabelText("Email"), "anna@example.com");
    await userEvent.click(canvas.getByRole("button", { name: "Log in" }));
    await expect(canvas.getByText("Welcome")).toBeInTheDocument();
  },
};
```

Recent Storybook versions can run these stories as tests with the Vitest addon, so they run in CI.

## 284: What is Chromatic?

Chromatic is a hosted service from the Storybook team. It publishes your Storybook, takes screenshots of every story, and compares them on each pull request to show visual changes (visual regression testing). Reviewers approve or reject changes in the UI. Alternatives are Percy, Playwright screenshot tests and Lost Pixel.

## 285: How do you use Analog's Vitest plugin in an Angular CLI or Nx project?

```bash
npm install -D @analogjs/vite-plugin-angular @analogjs/vitest-angular vitest jsdom
```

```ts
// vite.config.mts
import { defineConfig } from "vite";
import angular from "@analogjs/vite-plugin-angular";

export default defineConfig({
  plugins: [angular()],
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: ["src/test-setup.ts"],
  },
});
```

```ts
// src/test-setup.ts
import "@angular/compiler";
import "@analogjs/vitest-angular/setup-zone";
import { getTestBed } from "@angular/core/testing";
import {
  BrowserTestingModule,
  platformBrowserTesting,
} from "@angular/platform-browser/testing";

getTestBed().initTestEnvironment(
  BrowserTestingModule,
  platformBrowserTesting(),
);
```

Now that the CLI has its own Vitest builder, many projects use that instead, but Analog's plugin gives you full control over the Vite config.

## 286: How do you create file-based routes in Analog?

Pages live in `src/app/pages`. The file name is the route:

```text
src/app/pages/
  index.page.ts          ->  /
  about.page.ts          ->  /about
  products/[id].page.ts  ->  /products/:id
  (auth)/login.page.ts   ->  /login (folder in parentheses is not in the URL)
```

Each file default-exports a standalone component. Analog also supports `.server.ts` load functions and API routes in `src/server/routes`.

## 287: How do you share Angular code between apps with an Nx library?

```bash
nx g @nx/angular:library --name=ui-buttons --directory=libs/shared/ui-buttons
```

Nx adds a path alias to `tsconfig.base.json`, for example `@myorg/shared/ui-buttons`. Apps import from it like a package:

```ts
import { PrimaryButton } from "@myorg/shared/ui-buttons";
```

Only the library's `index.ts` is the public API. Importing deep files is blocked by lint rules.

## 288: How do you build your own reusable Angular library?

```bash
ng generate library my-lib
ng build my-lib
```

The CLI uses ng-packagr to build the library in the Angular Package Format (APF), with partial Ivy compilation so it works with any app on a compatible Angular version. You define the public API in `public-api.ts`, put Angular in `peerDependencies`, and publish the `dist/my-lib` folder with `npm publish`.

## 289: What are secondary entry points in a library?

A secondary entry point is a sub-path of a package, like `@angular/material/button` or `my-lib/forms`. Each one has its own `ng-package.json` and `public-api.ts` and is built separately. They:

- make tree-shaking easier and keep imports clear
- let parts of the library have different dependencies (for example, only `my-lib/charts` needs Chart.js)

```text
projects/my-lib/
  src/public-api.ts           -> my-lib
  charts/ng-package.json      -> my-lib/charts
  charts/src/public-api.ts
```

## 290: How do you add an `ng add` schematic to your own library?

Create a `schematics` folder with a `collection.json` that has an `ng-add` schematic, and point to it from `package.json`:

```json
{
  "name": "my-lib",
  "schematics": "./schematics/collection.json",
  "ng-add": { "save": "dependencies" }
}
```

The schematic is a function that returns a `Rule` and can, for example, add a provider to `app.config.ts` or a style file to `angular.json`. You need to build the schematics with `tsc` and copy them into `dist` as part of your library build.

## 291: What is the Angular Package Format?

APF is the standard structure for Angular npm packages. It defines how a package is laid out: FESM bundles (flattened ES modules), type definitions, `package.json` `exports` for each entry point, and partially compiled Ivy code. Following it (which ng-packagr does for you) makes sure the package works with the CLI, tree-shakes well and supports secondary entry points.

## 292: What is partial compilation and why do libraries use it?

Libraries are published with "partial" Ivy compilation (`compilationMode: 'partial'`). The code contains a stable intermediate format instead of the final instructions. When an app builds, the Angular linker finishes the compilation for the app's Angular version.

This lets a library built with one Angular version work with apps on later versions in its supported range. Full compilation would tie the library to an exact Angular version. The old View Engine format and `ngcc` are gone.

## 293: How do you set up Sentry performance tracing for Angular routes?

```ts
import { inject, provideAppInitializer } from "@angular/core";
import * as Sentry from "@sentry/angular";

export const appConfig = {
  providers: [
    { provide: Sentry.TraceService, deps: [Router] },
    provideAppInitializer(() => {
      inject(Sentry.TraceService);
    }),
  ],
};
```

With `browserTracingIntegration()` in `Sentry.init`, Sentry records route changes and HTTP calls as spans. Keep `tracesSampleRate` low in production to control cost.

## 294: How do you use an Angular library that is not compatible with your Angular version yet?

Options, from best to worst:

1. Check for a beta or "next" release that supports your version.
2. Look for a maintained fork or a replacement library.
3. If the library actually works, override the peer range with npm `overrides` and test well.
4. Fork it and maintain your own patched version (or use `patch-package` for small fixes).
5. Delay the Angular upgrade until the library catches up.

Write down which libraries block upgrades, so the team knows the risk.

## 295: How do you upgrade Angular when you use many third-party libraries?

1. Upgrade one major version at a time.
2. Check the Angular update guide (`angular.dev/update-guide`) and each library's changelog.
3. Run `ng update @angular/core @angular/cli`, then `ng update` for libraries that support it (Material, NgRx, Nx).
4. Update the rest manually to versions that support the new Angular.
5. Fix build errors, run all tests, and test key pages by hand, especially those with complex third-party components.

Keeping libraries few and up to date makes this much easier.

## 296: How do you use @angular/localize with runtime language loading?

Normally `@angular/localize` builds one app per language. You can load translations at runtime instead with `loadTranslations()` before bootstrap:

```ts
// main.ts
import { loadTranslations } from "@angular/localize";
import { bootstrapApplication } from "@angular/platform-browser";
import { App } from "./app/app";
import { appConfig } from "./app/app.config";

const lang = localStorage.getItem("lang") ?? "en";
const translations = await fetch(`/i18n/${lang}.json`).then((r) => r.json());
loadTranslations(translations.translations);

bootstrapApplication(App, appConfig);
```

You still can't switch language without reloading the page, because translations are applied when the app starts.

## 297: How do you extract and merge translations with @angular/localize?

```bash
ng extract-i18n --output-path src/locale --format json
```

This creates the source file. Translators make copies like `messages.de.json`. Then configure locales in `angular.json`:

```json
"i18n": {
  "sourceLocale": "en",
  "locales": { "de": "src/locale/messages.de.json" }
},
"options": { "localize": true }
```

`ng build` now outputs `dist/app/browser/en` and `dist/app/browser/de`. Tools like `ng-extract-i18n-merge` keep translation files in sync when messages change.

## 298: How do you show a PDF or Excel export from a table?

Common libraries:

- **SheetJS (`xlsx`)** or **ExcelJS** for Excel files
- **jsPDF** with **jspdf-autotable** for PDFs with tables
- **pdfmake** for PDFs from a document definition
- AG Grid's built-in CSV export (Community) and Excel export (Enterprise)

All are large, so load them with dynamic `import()` only when the user clicks export. For big reports, generating files on the server is usually better.

## 299: How do you use ngx-infinite-scroll inside a scrollable container?

By default it listens to window scroll. For a container, set `scrollWindow` to false and give the element a fixed height with overflow:

```html
<div
  class="h-96 overflow-y-auto"
  infiniteScroll
  [scrollWindow]="false"
  [infiniteScrollDistance]="1"
  [infiniteScrollThrottle]="150"
  (scrolled)="loadMore()"
>
  @for (item of items(); track item.id) {
  <app-row [item]="item" />
  }
</div>
```

Make sure `loadMore()` ignores calls while a request is already running, and stops when there are no more pages.

## 300: How do you show a skeleton for each item in a @defer or loading state?

```html
@if (products.isLoading()) { @for (i of [1, 2, 3, 4]; track i) {
<ngx-skeleton-loader [theme]="{ height: '120px', 'border-radius': '8px' }" />
} } @else { @for (p of products.value(); track p.id) {
<app-product-card [product]="p" />
} }
```

Showing skeletons with the same size as the real cards prevents layout shift (CLS) when data arrives.

# Advanced Questions (301-450)

## 301: How does the CDK Overlay position panels and handle running out of space?

`FlexibleConnectedPositionStrategy` takes a list of preferred positions. Each says which point of the origin element (for example bottom-left) connects to which point of the overlay (top-left), with optional offsets. When the overlay opens or the page scrolls, it tries each position in order and picks the first one that fits in the viewport. If none fit, it picks the one with the most visible area, and with `withFlexibleDimensions` and `withPush` it can shrink the panel or push it into view.

It also emits `positionChanges`, which Material uses to flip the arrow of a tooltip or the animation origin of a menu.

## 302: How does Angular Material's theming system work under the hood in M3?

`mat.theme` takes your palettes and generates CSS custom properties called system tokens (`--mat-sys-*`) for colors, typography, shape and elevation. Each component's styles don't use hard-coded values. They read component tokens (like `--mat-button-filled-container-color`), whose default values point to system tokens.

So the chain is: palette → system tokens → component tokens → component CSS. Override mixins (`mat.button-overrides`) just set component token variables on a selector. Because everything is CSS variables, theme changes and dark mode work at runtime without recompiling Sass, and the `light-dark()` function picks the right value for the color scheme.

## 303: How do you build a design system on top of Angular Material without fighting it?

- Use only the official customization points: `mat.theme`, system tokens, component override mixins, and default option tokens.
- Never style internal classes like `.mdc-*` or `.mat-mdc-*`. They are not public API and change between versions.
- Wrap Material components in your own components (`<ds-button>`) only when you need to limit options or add behavior. Avoid wrapping everything.
- Put your tokens in one Sass file and document them in Storybook.
- If the design differs a lot from Material, use the CDK or Angular Aria instead of Material for those parts.

## 304: Why did Angular Material switch to MDC-based components and what did it break?

Around version 15, Angular Material rebuilt its components on top of the official Material Design Components for Web (MDC) styles, to match the Material spec more closely and get better accessibility. The internal DOM and CSS class names changed (`.mat-` to `.mat-mdc-`), default sizes and spacing changed, and some APIs changed (for example form field appearances `legacy` and `standard` were removed).

Apps that styled internal classes or relied on pixel sizes broke. The lesson: only use the public token and mixin APIs, and use component harnesses in tests so DOM changes don't break them.

## 305: How do component test harnesses work internally?

A harness extends `ComponentHarness` and has a static `hostSelector`. It finds elements through a `locatorFor` API, which gets a `TestElement` abstraction instead of a real DOM element. The harness environment (`TestbedHarnessEnvironment` for unit tests, `SeleniumWebDriverHarnessEnvironment` or a Playwright one for e2e) implements `TestElement` for its platform and waits for the app to be stable (`whenStable`) after each action.

Because harness code never touches the DOM directly, the same harness works in unit tests and e2e tests, and component authors can change internals without breaking consumers.

## 306: How do you write your own component harness?

```ts
import {
  ComponentHarness,
  BaseHarnessFilters,
  HarnessPredicate,
} from "@angular/cdk/testing";

export interface RatingHarnessFilters extends BaseHarnessFilters {
  value?: number;
}

export class RatingHarness extends ComponentHarness {
  static hostSelector = "app-rating";

  private stars = this.locatorForAll("[data-star]");

  static with(options: RatingHarnessFilters = {}) {
    return new HarnessPredicate(RatingHarness, options).addOption(
      "value",
      options.value,
      async (h, v) => (await h.getValue()) === v,
    );
  }

  async getValue(): Promise<number> {
    const host = await this.host();
    return Number(await host.getAttribute("data-value"));
  }

  async rate(value: number): Promise<void> {
    const stars = await this.stars();
    await stars[value - 1].click();
  }
}
```

Ship harnesses in a `testing` secondary entry point of your library, like Material does.

## 307: How does CDK virtual scroll work and what are its limits?

The viewport listens to scroll events (outside Angular's change detection), asks the scroll strategy which index range is visible, and tells `*cdkVirtualFor` to render only that range plus a buffer (`minBufferPx`/`maxBufferPx`). A spacer element with the total content height keeps the scrollbar correct, and rendered items are moved with a CSS transform. `*cdkVirtualFor` recycles views from a template cache to avoid creating new ones.

Limits: fixed item height by default, no built-in sticky headers inside the list, browser find (Ctrl+F) can't find items that aren't rendered, and screen readers see only rendered items. Tables with virtual scroll need extra work.

## 308: How would you make a mat-table with 50,000 rows fast?

Options, depending on needs:

- Server-side paging, sorting and filtering, so the client shows 25-100 rows at a time. Usually the best answer.
- Virtual scrolling with the CDK table: there is no official virtual scroll for `mat-table`, so teams use community solutions or render rows with `cdk-virtual-scroll-viewport` and a CSS grid layout.
- Switch to a grid built for this (AG Grid, PrimeNG table with `virtualScroll`), which virtualizes rows and columns.
- Use `trackBy` with a stable ID, `OnPush`, and simple cell templates without method calls or heavy pipes.

## 309: How does AG Grid stay fast with large data sets?

- Row and column virtualization: only visible cells are in the DOM.
- It renders cells with plain DOM operations, not Angular templates, unless you use Angular cell renderers.
- Transaction updates (`applyTransaction`, `applyTransactionAsync`) update only changed rows. Async transactions batch many updates into one render.
- `getRowId` lets it match rows by ID instead of rebuilding them.
- Value getters and formatters are cached and run only for visible cells.

Using many Angular cell renderers reduces this benefit, since each one is a component with change detection. Prefer `valueFormatter` and CSS classes for simple cells.

## 310: How do you handle live updates (for example prices every 100ms) in AG Grid?

Don't replace `rowData` on every tick. Use async transactions:

```ts
this.socket.prices$.subscribe((updates) => {
  this.gridApi.applyTransactionAsync({ update: updates });
});
```

AG Grid batches these and applies them every `asyncTransactionWaitMillis` (default 50ms). Turn on `enableCellChangeFlash` to highlight changes. Make sure the subscription doesn't trigger Angular change detection for the whole app: with zoneless Angular this is automatic, and with Zone.js you can run it outside the zone.

## 311: How does the AG Grid Server-Side Row Model work?

The grid asks a datasource for blocks of rows with a request that includes start and end row, sort model, filter model, and the group keys if rows are grouped. Your server does the query and returns the rows and the total count (or `lastRow`). When the user expands a group, the grid requests the children of that group. Blocks are cached and purged with `maxBlocksInCache`.

```ts
const datasource: IServerSideDatasource = {
  getRows: (params) => {
    this.api.query(params.request).subscribe({
      next: (res) => params.success({ rowData: res.rows, rowCount: res.total }),
      error: () => params.fail(),
    });
  },
};
```

It is an Enterprise feature. Your backend must be able to turn the grid's filter and sort models into efficient database queries.

## 312: How does NgRx SignalStore work internally?

`signalStore()` returns an injectable class. Each `with*` feature is a function that receives the store built so far (its state signals, computed signals and methods) and returns new members. They run in order, so later features can use earlier ones.

State is kept in a single `WritableSignal` (internally a state source). `withState` creates `DeepSignal`s for each property, which are computed signals that read from that state and give you nested signals lazily (`store.user.address.city()`). `patchState` updates the state source with new immutable objects, and computed signals update only if their part changed. Methods are plain functions closed over the store.

## 313: How do you write a reusable custom feature for SignalStore?

Use `signalStoreFeature`:

```ts
import { computed } from "@angular/core";
import {
  signalStoreFeature,
  withState,
  withComputed,
  withMethods,
  patchState,
} from "@ngrx/signals";

export type RequestStatus =
  "idle" | "pending" | "fulfilled" | { error: string };

export function withRequestStatus() {
  return signalStoreFeature(
    withState<{ requestStatus: RequestStatus }>({ requestStatus: "idle" }),
    withComputed(({ requestStatus }) => ({
      isPending: computed(() => requestStatus() === "pending"),
      error: computed(() => {
        const s = requestStatus();
        return typeof s === "object" ? s.error : null;
      }),
    })),
    withMethods((store) => ({
      setPending: () => patchState(store, { requestStatus: "pending" }),
      setFulfilled: () => patchState(store, { requestStatus: "fulfilled" }),
      setError: (error: string) =>
        patchState(store, { requestStatus: { error } }),
    })),
  );
}
```

Any store can now add `withRequestStatus()`. You can also require that a store already has some state with the `type<>()` input option of `signalStoreFeature`.

## 314: How do you test a SignalStore?

Provide it in `TestBed` with mocked dependencies and call its methods:

```ts
import { TestBed } from "@angular/core/testing";
import { of } from "rxjs";
import { BooksStore } from "./books.store";
import { BooksApi } from "./books-api";

describe("BooksStore", () => {
  it("loads books", () => {
    TestBed.configureTestingModule({
      providers: [
        BooksStore,
        {
          provide: BooksApi,
          useValue: { search: () => of([{ id: 1, title: "Dune" }]) },
        },
      ],
    });
    const store = TestBed.inject(BooksStore);

    store.search("dune");
    // rxMethod with debounceTime: use fake timers
    vi.advanceTimersByTime(300);

    expect(store.books()).toEqual([{ id: 1, title: "Dune" }]);
  });
});
```

`@ngrx/signals/testing` has `unprotected(store)`, which lets tests set state directly even when the store is protected. Call `vi.useFakeTimers()` before the test when the store uses time-based operators.

## 315: What is state protection in SignalStore?

By default (`protectedState: true`), state can only be changed from inside the store, through its own methods. Components that inject the store can read signals but can't call `patchState` on it. This keeps all updates in one place. You can turn it off with `signalStore({ protectedState: false }, ...)`, but it's better to keep it and use `unprotected()` in tests.

## 316: What is the NgRx Signals events plugin?

`@ngrx/signals/events` brings Redux-style events to SignalStore. You define event groups with `eventGroup`, handle them in the store with `withReducer` (pure state changes) and `withEffects` (side effects), and dispatch them with `injectDispatch` or the `Dispatcher` service. Events are global, so several stores can react to the same event.

This gives you the decoupling of classic NgRx (components say "what happened", stores decide what to do) while keeping SignalStore's small API. It's useful when stores need to react to each other without importing each other.

## 317: How do classic NgRx selectors memoize, and when does memoization break?

`createSelector` remembers the last input values and the last result. If the inputs are the same by reference (`===`), it returns the cached result without running the projector. This only works if reducers keep unchanged parts of the state as the same objects.

It breaks when:

- a reducer creates new objects even when nothing changed (for example `{ ...state }` on every action)
- a selector with props is used with different arguments in many places, since there is only one cache slot. Use a factory selector (`selectById(id)`) that creates one selector per argument.
- the projector returns a new array every time (like `filter`) and the inputs changed for unrelated reasons, which makes downstream selectors and components update too

## 318: How do you avoid memory leaks with factory selectors in NgRx?

A factory function like `selectBookById = (id: string) => createSelector(...)` creates a new memoized selector on each call. If you call it in a template or on every change, you create many selectors, which hold onto old state. Create it once per component (for example in a field or `computed`), and call `selector.release()` if you need to free its cache. With `selectSignal`, create the signal once and not inside other functions that run often.

## 319: How do you handle race conditions in NgRx effects?

Pick the flattening operator that matches the behavior you want:

- `switchMap`: cancel the previous request when a new action comes. Good for search and loading the current page.
- `concatMap`: queue requests in order. Good for saves that must happen in sequence.
- `mergeMap`: run in parallel. Good for independent deletes.
- `exhaustMap`: ignore new actions while one is running. Good for login or "submit" buttons.

Using `switchMap` for writes is a common bug, since it can cancel a save the server has already received, leaving the client and server out of sync.

## 320: How do you do optimistic updates with NgRx or SignalStore?

Update the state immediately, call the server, and roll back on error:

```ts
remove: rxMethod<number>(
  pipe(
    concatMap((id) => {
      const previous = store.entities();
      patchState(store, removeEntity(id));
      return api.delete(id).pipe(
        tapResponse({
          next: () => {},
          error: () => {
            patchState(store, setAllEntities(previous));
            toastr.error('Could not delete');
          },
        }),
      );
    }),
  ),
),
```

Keep the snapshot small or store only what is needed to undo (the removed entity), and think about what happens if two optimistic actions overlap.

## 321: How would you migrate a large app from classic NgRx Store to SignalStore?

Do it gradually, feature by feature:

1. Start with new features in SignalStore.
2. Pick a feature with little cross-feature traffic and move its reducer, selectors and effects into one SignalStore. Keep the old actions if other features dispatch them, and react to them with the events plugin or by listening to `Actions` in a store method.
3. Replace `store.select` in components with store signals.
4. Remove the old feature state once nothing reads it.

Global state used everywhere (auth, router state) can stay in the classic Store for a long time. Both can live in the same app without problems.

## 322: How does TanStack Query for Angular integrate with signals?

`injectQuery` takes a function that returns the options. The adapter runs it inside a `computed`, so any signal read inside makes the options reactive. When the options change, the adapter updates the `QueryObserver` with the new key, which fetches new data or uses the cache. The observer's result is put into a signal, and the returned object exposes each field (`data`, `status`, `isFetching`) as a signal created from it.

Because it relies on the injection context, `injectQuery` must be called in a constructor or field initializer (or with an explicit injector), and its subscriptions are cleaned up with `DestroyRef`.

## 323: How do you prefetch data with TanStack Query on route navigation?

Use a resolver or a guard that calls `prefetchQuery` (or `ensureQueryData`), then use the same query key in the component:

```ts
import { ResolveFn } from "@angular/router";
import { inject } from "@angular/core";
import { QueryClient } from "@tanstack/angular-query-experimental";

export const productResolver: ResolveFn<unknown> = (route) => {
  const queryClient = inject(QueryClient);
  const api = inject(ProductsApi);
  const id = route.paramMap.get("id")!;
  return queryClient.ensureQueryData({
    queryKey: ["product", id],
    queryFn: () => lastValueFrom(api.get(id)),
  });
};
```

The component's `injectQuery` with key `['product', id]` gets the data from cache instantly. You can also prefetch on hover over a link.

## 324: How do you do optimistic updates with TanStack Query?

```ts
toggleTodo = injectMutation(() => ({
  mutationFn: (todo: Todo) =>
    lastValueFrom(
      this.http.patch(`/api/todos/${todo.id}`, { done: !todo.done }),
    ),
  onMutate: async (todo) => {
    await this.queryClient.cancelQueries({ queryKey: ["todos"] });
    const previous = this.queryClient.getQueryData<Todo[]>(["todos"]);
    this.queryClient.setQueryData<Todo[]>(["todos"], (old = []) =>
      old.map((t) => (t.id === todo.id ? { ...t, done: !t.done } : t)),
    );
    return { previous };
  },
  onError: (_err, _todo, context) => {
    this.queryClient.setQueryData(["todos"], context?.previous);
  },
  onSettled: () => this.queryClient.invalidateQueries({ queryKey: ["todos"] }),
}));
```

`cancelQueries` stops an in-flight refetch from overwriting the optimistic data.

## 325: How do you use TanStack Query with SSR in Angular?

On the server you need a fresh `QueryClient` per request, so data doesn't leak between users. Provide it inside the app config (which runs per request) instead of a module-level singleton. Then use Angular's `TransferState` (or the hydration helpers the adapter provides) to send the server cache to the client, so the browser doesn't fetch again. Set `staleTime` above zero, or the client will refetch right after hydration. Check the current adapter docs, since SSR support is one of the areas still evolving in the experimental package.

## 326: How does Apollo's normalized cache work and when does it cause problems?

`InMemoryCache` splits query results into objects and stores each by a cache ID, by default `__typename:id`. Queries are stored as references to those objects. When any query or mutation returns the same object with new fields, every query that references it updates.

Problems:

- Types without `id` are stored inside their parent and are not shared. Configure `keyFields` in `typePolicies`.
- Lists are not updated automatically when you add or remove items. Use `update` functions, `refetchQueries`, or `merge` functions.
- Paginated fields need a field policy (`keyArgs`, `merge`), or each page replaces the previous one.
- Very large caches use memory. Use `cache.evict` and `cache.gc`.

## 327: How do you implement cursor pagination with Apollo Angular?

Define a field policy so pages merge, then call `fetchMore`:

```ts
new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        feed: {
          keyArgs: ["filter"],
          merge(existing = { items: [] }, incoming) {
            return {
              ...incoming,
              items: [...existing.items, ...incoming.items],
            };
          },
        },
      },
    },
  },
});
```

```ts
loadMore() {
  this.feedQuery.fetchMore({ variables: { after: this.endCursor() } });
}
```

`keyArgs` says which arguments create separate lists (here, each filter has its own list, but `after` does not).

## 328: How do you handle GraphQL subscriptions in Apollo Angular?

Add a WebSocket link with `graphql-ws` and split traffic between HTTP and WS:

```ts
import { split } from "@apollo/client/core";
import { GraphQLWsLink } from "@apollo/client/link/subscriptions";
import { getMainDefinition } from "@apollo/client/utilities";
import { createClient } from "graphql-ws";

const ws = new GraphQLWsLink(
  createClient({ url: "wss://api.example.com/graphql" }),
);
const http = httpLink.create({ uri: "/graphql" });

const link = split(
  ({ query }) => {
    const def = getMainDefinition(query);
    return (
      def.kind === "OperationDefinition" && def.operation === "subscription"
    );
  },
  ws,
  http,
);
```

Then use `apollo.subscribe({ query })` or `subscribeToMore` on a watch query to merge events into an existing list. Create the WebSocket client only in the browser when using SSR.

## 329: How do runtime i18n libraries affect performance compared to @angular/localize?

With ngx-translate or Transloco:

- Translation JSON files are extra HTTP requests and the first render may wait for them.
- Every translated string is a pipe or a function call that looks up a key at runtime and must update when the language changes.
- Templates have keys, so the compiler can't check them.

With `@angular/localize`, the text is baked into the JavaScript at build time, so there is no lookup and no extra request. The cost is a build per language and a reload to switch. For most apps the runtime cost is small. It matters on very large pages or low-end devices.

## 330: How does ngx-translate's pipe update when the language changes, and why can it be slow?

The `translate` pipe is impure. It subscribes to language change events and calls `markForCheck` when they fire. Being impure, Angular calls its `transform` on every change detection run for that view. The pipe caches the last key and params to avoid lookups, but it still runs a comparison each time. With hundreds of pipes on a page and frequent change detection, that adds up.

Transloco's structural directive (`*transloco="let t"`) creates one subscription per block instead of one per string, which is lighter. With signals and OnPush/zoneless, change detection runs less often, which also helps.

## 331: How would you organize translations for a large app with many teams?

- Split by feature using scopes (Transloco) or separate files per feature with a custom loader (ngx-translate), loaded lazily with the feature's routes.
- Use a key naming convention like `feature.section.key`.
- Have one source language file as the source of truth, and use a translation management system (Lokalise, Crowdin, Phrase, Tolgee) that syncs with the repo through CI.
- Check for missing and unused keys in CI (Transloco Keys Manager or custom scripts).
- Keep shared strings (buttons like "Save", "Cancel") in a common scope.

## 332: How do you translate route titles, page meta tags and validation messages?

- Route titles: write a custom `TitleStrategy` that takes the route `title` as a key and translates it.
- Meta tags: set them with `Meta` service after translations load, usually in a resolver or with `selectTranslate`.
- Validation messages: map error keys to translation keys in one place (a pipe or component that shows errors), instead of hard-coding messages in every form.

```ts
@Injectable({ providedIn: "root" })
export class TranslatedTitleStrategy extends TitleStrategy {
  private title = inject(Title);
  private transloco = inject(TranslocoService);

  override updateTitle(snapshot: RouterStateSnapshot) {
    const key = this.buildTitle(snapshot);
    if (key) {
      this.transloco
        .selectTranslate(key)
        .pipe(take(1))
        .subscribe((t) => this.title.setTitle(t));
    }
  }
}
```

## 333: How do you make Transloco or ngx-translate work with SSR?

The HTTP loader uses relative URLs like `/i18n/en.json`, which don't work on the server. Options:

- On the server, use a loader that reads files from disk, or make the URL absolute using the request host.
- Use `TransferState` (Transloco has docs for this) so the server sends loaded translations to the client, avoiding a second request and a flash of keys.
- Decide the language on the server from the URL, a cookie or `Accept-Language`, not from `localStorage`.

## 334: How does Formly render a form internally and what are its performance traps?

Formly walks the field config tree, creates form controls for each `key`, and renders each field type component dynamically through `formly-field`. Wrappers (like a form field wrapper with label and errors) wrap the field component. Expressions (`expressions`, `hide`) are evaluated on every check of the form, and Formly runs a "check expressions" cycle when values change.

Traps:

- Hundreds of fields with many function expressions get slow. Prefer simple expressions and fewer watchers.
- Replacing the `fields` array causes a full rebuild. Mutate or keep references stable.
- Heavy custom types with default change detection make every keystroke expensive. Use OnPush in custom types.

## 335: How do you build a component library that supports both Material and a custom theme?

Separate behavior from look:

- Put logic in headless directives or services (or use the CDK/Angular Aria).
- Make styling depend on CSS custom properties with your own names (`--ds-button-bg`), not on Material classes.
- Provide a "Material theme" stylesheet that maps your variables to Material system tokens, and a "custom theme" stylesheet that maps them to brand values.
- Use content projection and templates for anything that differs in markup.

Consumers switch themes by including a different stylesheet, and the components stay the same.

## 336: How do PrimeNG design tokens and CSS layers work, and how do you avoid style conflicts?

PrimeNG's styled mode generates CSS variables from the preset (primitive, semantic and component tokens) and injects component styles at runtime. You can tell PrimeNG to put its styles in a CSS cascade layer:

```ts
providePrimeNG({
  theme: {
    preset: Aura,
    options: {
      cssLayer: { name: "primeng", order: "theme, base, primeng, utilities" },
    },
  },
});
```

With layers, your own styles or Tailwind utilities in a later layer always win, without `!important` or high specificity. This is the main tool to avoid fights between PrimeNG and Tailwind.

## 337: How do you handle a breaking change in a UI library across a big codebase?

- Read the migration guide and check if there's an `ng update` schematic.
- If not, write a codemod (with `ts-morph`, jscodeshift, or an Angular schematic) for mechanical changes like renamed inputs.
- Wrap the library behind your own components in the places where it's used a lot, so the next breaking change affects one file.
- Use component harnesses or Testing Library in tests, so tests don't break because of DOM changes.
- Roll out behind a feature branch, run visual regression tests (Chromatic, Playwright screenshots).

## 338: Should you wrap third-party UI components in your own components?

It depends on how widely they are used and how likely you are to replace them.

Pros of wrapping: one place to change when the library changes, a smaller API for your team, consistent defaults, and you can switch libraries later.

Cons: more code, you have to forward inputs, outputs and templates, and you lose features unless you expose them. Wrappers that just pass everything through add little value.

A practical rule: wrap basic building blocks used everywhere (button, input, dialog service, toast service) and use complex components (data grid, editor) directly with a thin config layer.

## 339: How do you design a notification service that can switch between ngx-toastr and MatSnackBar?

Define an abstract class as the DI token and provide an implementation:

```ts
export abstract class Notifier {
  abstract success(message: string): void;
  abstract error(message: string): void;
}

@Injectable()
export class SnackBarNotifier extends Notifier {
  private snackBar = inject(MatSnackBar);
  success(message: string) {
    this.snackBar.open(message, undefined, {
      duration: 3000,
      panelClass: "success",
    });
  }
  error(message: string) {
    this.snackBar.open(message, "Close", { panelClass: "error" });
  }
}

export const appConfig = {
  providers: [{ provide: Notifier, useClass: SnackBarNotifier }],
};
```

Components inject `Notifier`. Switching to ngx-toastr means writing `ToastrNotifier` and changing one provider. It also makes tests simpler.

## 340: How do Angular libraries stay compatible with zoneless change detection?

A library is zoneless-safe if it doesn't rely on Zone.js to trigger change detection after async work. That means:

- updating state through signals, or calling `markForCheck()`/`ChangeDetectorRef` when non-signal state changes after a timer, event listener or promise
- not using `NgZone.onStable` or `onMicrotaskEmpty` to wait for rendering. Use `afterNextRender` instead
- not depending on `zone.js` being loaded

Angular Material, CDK and most big libraries support zoneless now. With older libraries, you may see the UI not updating until the next click. The fix is usually updating the library, or calling `markForCheck` in your code after its callbacks.

## 341: Why can a third-party library make your app slow with Zone.js?

With Zone.js, every async event (timers, `requestAnimationFrame`, scroll, mousemove, WebSocket messages) triggers change detection for the whole app. Libraries like charting, maps, editors or animation libraries can fire these many times per second, even if nothing in Angular changed.

Fixes:

- create the library instance with `ngZone.runOutsideAngular(() => ...)` and re-enter with `ngZone.run()` only when Angular state changes
- use OnPush components so less of the tree is checked
- move to zoneless change detection, where only signals and explicit marks trigger change detection

## 342: How do you profile which library is causing slow change detection?

- Use the Angular DevTools profiler: record, then look at which components take the most time in each change detection cycle and what triggered it.
- Use the Chrome Performance panel to see long tasks and which functions (library code) run during them.
- Temporarily remove or `@defer` suspect components and compare.
- With Zone.js, check how often change detection runs (the profiler shows cycles). A cycle on every mousemove usually means a library listener is running inside the zone.

## 343: How do you integrate a library that uses its own DOM rendering (like a map or editor) with Angular change detection?

Treat it as an island:

- Create it after render (`afterNextRender`) on a host element that Angular doesn't put children into.
- Push inputs into it with `effect()` or `ngOnChanges`, using its API, not by changing the DOM Angular renders.
- Listen to its events and update Angular state through signals, which schedules change detection.
- With Zone.js, create it outside the Angular zone.
- Destroy it in `DestroyRef.onDestroy` to remove listeners and avoid leaks.

Never let Angular and the library both control the same DOM nodes.

## 344: How do you render Angular components inside a third-party library (for example a popup in a Leaflet map)?

Create the component dynamically and attach its host element to the library:

```ts
import { ApplicationRef, EnvironmentInjector, createComponent, inject } from '@angular/core';

private appRef = inject(ApplicationRef);
private injector = inject(EnvironmentInjector);

openPopup(store: Store, latLng: L.LatLng) {
  const ref = createComponent(StorePopup, { environmentInjector: this.injector });
  ref.setInput('store', store);
  this.appRef.attachView(ref.hostView);

  L.popup()
    .setLatLng(latLng)
    .setContent(ref.location.nativeElement)
    .on('remove', () => {
      this.appRef.detachView(ref.hostView);
      ref.destroy();
    })
    .openOn(this.map);
}
```

`attachView` makes the component part of change detection. Destroying it when the popup closes avoids leaks.

## 345: How do you avoid memory leaks with third-party libraries in Angular?

- Call the library's destroy method (`chart.destroy()`, `map.remove()`, `editor.destroy()`) in `DestroyRef.onDestroy`.
- Remove global event listeners the library or your code added to `window` or `document`.
- Unsubscribe from long-lived observables (`takeUntilDestroyed`).
- Detach and destroy dynamically created components.
- Close overlays and dialogs when the owner component is destroyed.

Check with the Chrome Memory panel: take heap snapshots before and after opening and closing a page a few times, and look for detached DOM nodes and growing counts of your component classes.

## 346: How do you secure rich text from editors like Quill or TinyMCE?

HTML from an editor is user input and can contain scripts or dangerous attributes.

- Sanitize it on the server before saving or before showing it to others (for example with DOMPurify on Node, or a backend sanitizer like OWASP Java HTML Sanitizer).
- When showing it with `[innerHTML]`, Angular's built-in sanitizer removes scripts and event handlers. Don't use `bypassSecurityTrustHtml` on user content.
- If you need more control on the client, run DOMPurify before binding.
- Set a Content Security Policy to limit damage if something gets through.

## 347: What security risks come with ngx-markdown and similar renderers?

Markdown can contain raw HTML. If you render user Markdown and turn off sanitization, users can inject `<script>`, `<img onerror>` or `javascript:` links (XSS). Also, loading Markdown from a URL (`src`) that users control can load content from any domain.

Keep ngx-markdown's sanitization on (it uses Angular's `DomSanitizer` by default), don't allow user-controlled `src`, and if you add plugins like Mermaid or KaTeX, check that they don't open new ways to run code.

## 348: How do you keep third-party dependencies safe in an Angular project?

- Run `npm audit` and tools like Snyk, Dependabot or Renovate to find and update vulnerable packages.
- Commit the lock file and use `npm ci` in CI so builds use exact versions.
- Check new packages before adding them: maintainers, downloads, install scripts, recent ownership changes.
- Prefer fewer dependencies. Every package and its sub-dependencies is code you run.
- Consider disabling install scripts (`--ignore-scripts`) in CI where possible, and use npm provenance for your own packages.
- Use a CSP and Trusted Types to limit what injected scripts can do.

## 349: How do OIDC libraries protect against token theft, and what are the trade-offs of storing tokens in the browser?

Libraries like angular-oauth2-oidc and angular-auth-oidc-client use the authorization code flow with PKCE, so no token is in the URL, and they validate the ID token signature, issuer, audience and nonce.

But they still keep tokens in JavaScript-readable storage (memory, sessionStorage or localStorage). If an attacker gets XSS on your app, they can read them. Options:

- keep tokens in memory only and use short-lived access tokens with refresh token rotation
- use the Backend-for-Frontend (BFF) pattern: the server does the OAuth flow and gives the browser an `HttpOnly`, `Secure`, `SameSite` cookie. The SPA never sees tokens. This is the current recommendation for high-security apps.

## 350: How does the MSAL Angular interceptor decide which token to attach, and what can go wrong?

`MsalInterceptor` matches the request URL against `protectedResourceMap`. For a match, it calls `acquireTokenSilent` with the listed scopes, using cached tokens or the refresh token. If silent acquisition fails (consent needed, session expired), it falls back to interactive login (popup or redirect).

Common problems:

- URLs that don't match the map, so no token is sent and the API returns 401.
- Too broad a pattern, which sends tokens to the wrong API.
- Multiple APIs needing different scopes, causing extra consent prompts.
- Calling APIs before MSAL has finished handling the redirect, which leads to interaction errors. Wait for `inProgress$` to be `None`.

## 351: How do you implement token refresh with a functional interceptor without firing many refresh requests?

Share one refresh request between all requests that failed with 401:

```ts
import {
  HttpErrorResponse,
  HttpInterceptorFn,
  HttpRequest,
} from "@angular/common/http";
import { inject } from "@angular/core";
import {
  Observable,
  catchError,
  finalize,
  shareReplay,
  switchMap,
  throwError,
} from "rxjs";
import { AuthService } from "./auth.service";

let refresh$: Observable<string> | null = null;

const withToken = (req: HttpRequest<unknown>, token: string) =>
  req.clone({ setHeaders: { Authorization: `Bearer ${token}` } });

export const refreshInterceptor: HttpInterceptorFn = (req, next) => {
  const auth = inject(AuthService);
  if (req.url.includes("/auth/refresh")) {
    return next(req);
  }

  return next(withToken(req, auth.accessToken())).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status !== 401) {
        return throwError(() => err);
      }
      refresh$ ??= auth.refresh().pipe(
        shareReplay(1),
        finalize(() => (refresh$ = null)),
      );
      return refresh$.pipe(switchMap((token) => next(withToken(req, token))));
    }),
  );
};
```

If the refresh fails, log the user out. OIDC libraries do this for you, which is one reason to use them instead of writing your own.

## 352: How do you handle authentication in an app with micro frontends (Native Federation)?

- Share the auth library as a singleton in `federation.config.js`, so host and remotes use the same instance and token cache.
- Let only the shell do the login flow. Remotes get the current user and tokens from a shared service in a shared library, not by logging in themselves.
- Keep interceptor setup consistent: if remotes create their own `HttpClient` providers, the shell's interceptors won't apply. Remotes that are loaded as routes into the shell share the shell's root injector, which avoids this.
- Make sure versions match, or `strictVersion` will load a second copy of the library.

## 353: How does Native Federation share dependencies, and what goes wrong with Angular?

At build time, each shared package is built into a separate bundle, and the build writes metadata about versions. At runtime, `initFederation` reads the manifests of the host and remotes, picks one version of each shared package (based on `singleton`, `strictVersion` and `requiredVersion`), and creates an import map so all apps load the same file.

Problems with Angular:

- Angular packages must be singletons. Two copies of `@angular/core` break DI ("NG0203" and other errors).
- Different Angular major versions in host and remotes don't work well together. Keep versions aligned or use web components as a boundary.
- Sharing too much (`shareAll`) increases startup requests. Use `skip` to exclude packages that don't need sharing.
- Libraries with secondary entry points need all entry points shared consistently.

## 354: When would you use web components (Angular Elements) instead of Native Federation for micro frontends?

Use Angular Elements (`@angular/elements`, `createCustomElement`) when:

- micro frontends use different frameworks or different Angular major versions
- you need strong isolation, and each part brings its own runtime
- you embed widgets in non-Angular pages (CMS, legacy apps)

The cost is bigger bundles (each element includes its own Angular, unless you carefully share), weaker integration (communication only through attributes, properties and DOM events), and harder routing. Native Federation is better when all parts use the same Angular version and you want them to feel like one app.

## 355: How does Nx caching work and how do you make sure it's correct?

Before running a task, Nx computes a hash from the task's inputs: source files of the project and its dependencies, config files, environment variables you declare, the command, and the lock file. If the hash is in the local or remote cache, it replays the output and files instead of running the task.

To keep it correct:

- declare `inputs` and `outputs` for custom targets in `nx.json` or `project.json`
- add environment variables that affect the build to `inputs` (`{ "env": "API_URL" }`)
- don't let tasks read files outside their declared inputs
- use `namedInputs` like `production` to exclude test files from build hashes

Wrong inputs give you stale cached results, which are hard to debug.

## 356: How would you structure a large Angular Nx monorepo?

A common structure:

```text
apps/
  shop/
  admin/
libs/
  shop/
    feature-cart/        (smart components, routes)
    data-access-cart/    (stores, API services)
    ui-cart/             (presentational components)
  shared/
    ui/                  (design system)
    util/                (pure functions)
    data-access-auth/
```

Tag projects by `type` and `scope`, and use module boundary rules: features can use data-access, ui and util; ui can use only ui and util; scopes can use only their own scope and `shared`. Keep apps thin: mostly routing and config, with features in libraries. This makes `nx affected` effective and keeps teams from stepping on each other.

## 357: How do Nx generators and executors differ from Angular CLI schematics and builders?

They are the same ideas with different names. Generators create or change code (like schematics), and executors run tasks like build, test and serve (like builders). Nx can run Angular schematics and builders directly, and many Nx Angular executors wrap the official builders. Nx adds its own features on top: task graph, caching, affected detection, and executors for tools the CLI doesn't cover (Jest, Vitest, Playwright, Storybook, Node apps).

You can write local generators in your workspace to enforce your own conventions, for example a generator that creates a feature library with a SignalStore and routes already set up.

## 358: How does Storybook build Angular stories, and why do some components fail to render?

Storybook's Angular framework uses the Angular builder to compile stories and renders each story by bootstrapping a small Angular app around the component. Components fail when:

- they need providers that aren't in the story (router, HTTP, a store, translations). Add them with `applicationConfig`
- they depend on global styles or fonts that aren't in Storybook's config. Add them in `angular.json` under the Storybook target
- they use services that call real APIs. Mock them or use MSW
- they need a parent component (for example content projection). Use a `render` function with a template

## 359: How do you run Angular unit tests in a real browser and why would you?

jsdom doesn't do layout, real focus, or many browser APIs (IntersectionObserver, ResizeObserver, canvas). Tests for drag and drop, virtual scroll, overlays or charts can pass in jsdom and fail in real life, or need many mocks.

Options:

- Vitest browser mode with Playwright as the provider, which the Angular unit test builder supports through its `browsers` option
- Karma with Chrome (deprecated but still working)
- Cypress or Playwright component testing

Browser tests are slower, so many teams run most tests in jsdom and only the layout-dependent ones in a browser.

## 360: How do you test code that uses Material dialogs, overlays or snack bars in jsdom?

- Use harnesses with `documentRootLoader`, since overlays render under `document.body`.
- Animations can make tests wait. Use `provideNoopAnimations()` (or the animation disabling setup for your Angular version) in tests.
- Overlays need a container. `OverlayContainer` is created automatically but may leak between tests; reset `TestBed` or call `overlayContainer.ngOnDestroy()` in `afterEach`.
- For snack bars with `duration`, use fake timers to move time forward.

## 361: Why do tests with Spectator or ng-mocks become flaky, and how do you fix them?

Common causes:

- Async work not awaited: HTTP calls, timers, `@defer` blocks or resources that resolve after the assertion. Use `await fixture.whenStable()`, fake timers, or `findBy*` queries.
- Shared state between tests: root services, singletons, or global mocks not reset. ng-mocks has `ngMocks.autoSpy` and `MockInstance` with scoped resets.
- Test order dependency through module-level variables.
- Real timers with small timeouts (debounce) that depend on machine speed.

Run tests in random order (Jasmine does by default, Vitest with `sequence.shuffle`) to find order problems.

## 362: How do you test a component that uses @defer?

By default, `TestBed` uses `DeferBlockBehavior.Playthrough` in recent versions, which renders defer blocks like in the browser. To control it manually:

```ts
TestBed.configureTestingModule({
  deferBlockBehavior: DeferBlockBehavior.Manual,
});
const fixture = TestBed.createComponent(Dashboard);

const [chartBlock] = await fixture.getDeferBlocks();
await chartBlock.render(DeferBlockState.Placeholder);
expect(fixture.nativeElement.textContent).toContain("Chart");

await chartBlock.render(DeferBlockState.Complete);
expect(fixture.nativeElement.querySelector("app-sales-chart")).toBeTruthy();
```

This lets you test placeholder, loading, error and complete states without real lazy loading.

## 363: How would you test a component that uses AG Grid?

AG Grid renders asynchronously and uses its own DOM. Options:

- Unit test the configuration (column defs, value formatters, getters) as plain functions, without rendering the grid.
- For component tests, wait for `gridReady`, then use the grid API (`api.getDisplayedRowCount()`, `api.getCellValue`) rather than querying DOM cells.
- Test cell renderers as standalone components with fake `params`.
- Cover real interactions (sorting, filtering, editing) in e2e tests with Playwright, using the grid's stable attributes like `row-index` and `col-id`.

## 364: How do you mock a GraphQL API in Apollo Angular tests?

Use `ApolloTestingModule` and `ApolloTestingController`:

```ts
import { TestBed } from "@angular/core/testing";
import {
  ApolloTestingController,
  ApolloTestingModule,
} from "apollo-angular/testing";

beforeEach(() => {
  TestBed.configureTestingModule({ imports: [ApolloTestingModule] });
});

it("shows books", () => {
  const fixture = TestBed.createComponent(Books);
  const controller = TestBed.inject(ApolloTestingController);
  fixture.detectChanges();

  const op = controller.expectOne(GET_BOOKS);
  op.flush({
    data: { books: [{ id: "1", title: "Dune", __typename: "Book" }] },
  });
  fixture.detectChanges();

  expect(fixture.nativeElement.textContent).toContain("Dune");
  controller.verify();
});
```

Include `__typename` in mock data, or the cache can't normalize it.

## 365: How do you test effects in classic NgRx?

Use `provideMockActions` and a fake API:

```ts
import { TestBed } from "@angular/core/testing";
import { provideMockActions } from "@ngrx/effects/testing";
import { Observable, of, throwError, firstValueFrom } from "rxjs";
import { Action } from "@ngrx/store";
import { loadBooks } from "./books.effects";

it("maps an error to loadFailure", async () => {
  let actions$: Observable<Action> = of(BooksPageActions.opened());
  TestBed.configureTestingModule({
    providers: [
      provideMockActions(() => actions$),
      {
        provide: BooksApi,
        useValue: { getAll: () => throwError(() => new Error("boom")) },
      },
    ],
  });

  const result = await TestBed.runInInjectionContext(() =>
    firstValueFrom(loadBooks()),
  );
  expect(result).toEqual(BooksApiActions.loadFailure({ error: "boom" }));
});
```

For timing-based effects (debounce), use RxJS marble tests with `TestScheduler`.

## 366: How do you use `provideMockStore` to test components that use NgRx?

```ts
import { provideMockStore, MockStore } from "@ngrx/store/testing";

beforeEach(() => {
  TestBed.configureTestingModule({
    providers: [
      provideMockStore({
        selectors: [
          {
            selector: booksFeature.selectBooks,
            value: [{ id: "1", title: "Dune" }],
          },
        ],
      }),
    ],
  });
});

it("dispatches opened on init", () => {
  const store = TestBed.inject(MockStore);
  const dispatch = vi.spyOn(store, "dispatch");
  TestBed.createComponent(BookList).detectChanges();
  expect(dispatch).toHaveBeenCalledWith(BooksPageActions.opened());
});
```

Use `store.overrideSelector()` and `store.refreshState()` to change values during a test.

## 367: How do you design E2E tests so they don't break when UI libraries change?

- Use role and label locators (`getByRole('button', { name: 'Save' })`) instead of CSS classes from the UI library.
- Add `data-testid` only where accessible locators are not possible.
- Use the Page Object pattern so selectors live in one place.
- For complex library components (date pickers, grids), write small helper functions or harnesses that hide their DOM details.
- Mock network calls for most tests, and keep a few smoke tests against a real backend.

## 368: How does Playwright's auto-waiting help with Angular apps?

Playwright waits for elements to be attached, visible, stable (not animating), enabled and able to receive events before acting. Its `expect` assertions retry until they pass or time out. This handles Angular's async rendering, animations from Material, and data loading without manual `sleep`s or Angular-specific waits (which Protractor needed).

You still need to wait for the right signal, for example `await expect(page.getByText('Saved')).toBeVisible()` after a save, not just clicking and moving on.

## 369: How do you speed up Angular CI with Nx Cloud or similar tools?

- Remote caching: if a commit's build or tests were already run by someone else or a previous pipeline, CI downloads the results.
- `nx affected`: only run tasks for changed projects.
- Distributed task execution: split tasks across several CI machines based on the task graph.
- Split e2e tests by file across agents (Nx Atomizer or Playwright sharding).

Make sure cached tasks are deterministic and declare their inputs correctly, or you will get stale results.

## 370: How do you pick a state management solution for a new large Angular app?

Questions to ask:

- How much state is server data vs real client state? If most is server data, TanStack Query or `httpResource` plus small signal stores may be enough.
- How many teams and features? Many teams benefit from a clear pattern (NgRx Store or SignalStore with events).
- Do you need devtools, time travel, undo or persisted state?
- What does the team already know?

A common modern choice: signals in components, SignalStore for shared feature state, and a server-state tool or resources for API data. Avoid putting everything into one global store "just in case".

## 371: How do you handle forms state together with a store like NgRx?

Usually, keep form state in the form (reactive forms or signal forms) and only send the result to the store on submit. Syncing every keystroke into the store adds actions and complexity and rarely helps.

Exceptions: draft saving, multi-step wizards spread over routes, or forms that many components read. Then you can sync with `valueChanges` and `debounceTime`, or use a dedicated helper (NGXS form plugin, or ngrx-forms for classic NgRx). Keep the store as the source for initial values and the form as the source while editing.

## 372: How do you design a SignalStore that handles pagination, filtering and caching?

```ts
export const ProductsStore = signalStore(
  withState({ page: 1, pageSize: 20, query: "", total: 0 }),
  withEntities<Product>(),
  withRequestStatus(),
  withMethods((store, api = inject(ProductsApi)) => ({
    setQuery(query: string) {
      patchState(store, { query, page: 1 });
    },
    setPage(page: number) {
      patchState(store, { page });
    },
    load: rxMethod<{ page: number; pageSize: number; query: string }>(
      pipe(
        debounceTime(250),
        tap(() => store.setPending()),
        switchMap((params) =>
          api.list(params).pipe(
            tapResponse({
              next: (res) => {
                patchState(store, setAllEntities(res.items), {
                  total: res.total,
                });
                store.setFulfilled();
              },
              error: (e: Error) => store.setError(e.message),
            }),
          ),
        ),
      ),
    ),
  })),
  withHooks({
    onInit(store) {
      store.load(
        computed(() => ({
          page: store.page(),
          pageSize: store.pageSize(),
          query: store.query(),
        })),
      );
    },
  }),
);
```

Passing a computed signal to `rxMethod` reloads automatically when page or query changes, and `switchMap` cancels old requests. For caching pages, keep a map of results keyed by params, or use TanStack Query for that part.

## 373: How do you persist and rehydrate store state safely?

- Persist only what's needed (preferences, cart), not server data that can go stale or sensitive data.
- Store a version number with the data and migrate or drop old versions when the shape changes.
- Validate the loaded data (for example with Zod) before putting it into the store, since users can edit localStorage.
- Debounce writes so you don't write on every change.
- Guard storage access for SSR and private browsing (where `localStorage` may throw).

For NgRx, a meta-reducer or `ngrx-store-localstorage` handles it. For SignalStore, `withStorageSync` from the ngrx-toolkit or your own `withHooks` + `effect`. For NGXS, the storage plugin with `migrations`.

## 374: What is a meta-reducer in NgRx and what libraries use them?

A meta-reducer wraps the root reducer: it receives every action and the state before the real reducer runs, and can change either. It's like middleware for reducers.

```ts
export function logger(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) => {
    const next = reducer(state, action);
    console.log(action.type, next);
    return next;
  };
}

provideStore({}, { metaReducers: [logger] });
```

Uses: logging, resetting all state on logout, undo/redo, and persisting state (libraries like `ngrx-store-localstorage` work as meta-reducers).

## 375: How do you reset all store state on logout?

With classic NgRx, a meta-reducer that returns `undefined` state on logout, so every reducer goes back to its initial state:

```ts
export function clearOnLogout(reducer: ActionReducer<any>): ActionReducer<any> {
  return (state, action) =>
    reducer(
      action.type === AuthActions.logout.type ? undefined : state,
      action,
    );
}
```

With SignalStore, root stores need a `reset()` method (or the events plugin with a global `logout` event that each store handles). Component-level stores disappear by themselves. Also clear TanStack Query or Apollo caches (`queryClient.clear()`, `apollo.client.resetStore()`) so the next user doesn't see old data.

## 376: How do you combine TanStack Query with NgRx or SignalStore without duplicating state?

Keep server data only in TanStack Query's cache, and keep only client state (selected IDs, filters, UI flags) in the store. Components read the selected ID from the store and pass it into the query function:

```ts
selectedId = this.store.selectedProductId;

product = injectQuery(() => ({
  queryKey: ["product", this.selectedId()],
  queryFn: () => lastValueFrom(this.api.get(this.selectedId()!)),
  enabled: this.selectedId() !== null,
}));
```

Don't copy query results into the store, since then you have two sources of truth that can get out of sync.

## 377: How do you build an accessible custom select on top of the CDK or Angular Aria instead of using a library?

Use the headless pieces for the hard parts:

- `cdkListbox` or Angular Aria's listbox/combobox for keyboard navigation, selection and ARIA roles
- `CdkConnectedOverlay` for the dropdown panel and positioning
- `ControlValueAccessor` so it works with forms
- `aria-expanded`, `aria-controls` and `aria-activedescendant` on the trigger

Then test with a keyboard only and a screen reader (VoiceOver, NVDA). Building selects from scratch with plain divs usually misses things like typeahead, Home/End keys and announcements, which is why using these primitives is safer.

## 378: How does the CDK ListKeyManager work, and how would you use it?

`ListKeyManager` (and its subclasses `ActiveDescendantKeyManager` and `FocusKeyManager`) tracks an active item in a list and handles keys: arrow up/down (or left/right), Home/End, typeahead by letter, and wrapping. You give it a `QueryList` of items and forward keydown events to it.

```ts
items = viewChildren(OptionItem);
private keyManager?: ActiveDescendantKeyManager<OptionItem>;

constructor() {
  afterNextRender(() => {
    this.keyManager = new ActiveDescendantKeyManager(this.items, this.injector).withWrap().withTypeAhead();
  });
}

onKeydown(event: KeyboardEvent) {
  this.keyManager?.onKeydown(event);
}
```

`FocusKeyManager` moves real focus, while `ActiveDescendantKeyManager` keeps focus on the input and highlights items (for comboboxes). Recent versions accept a signal of items plus an injector.

## 379: How would you evaluate if a UI library is accessible enough?

- Check its docs for WCAG and ARIA patterns, and look for open accessibility issues.
- Test key components with keyboard only: tab order, focus visible, Escape closes, arrows work.
- Test with a screen reader on at least one platform.
- Run axe (browser extension, `@axe-core/playwright`, or Storybook's a11y addon) on pages using it.
- Check color contrast with the theme you will actually use.

Angular Material and Angular Aria put a lot of work into accessibility. Some smaller libraries look nice but miss basic keyboard support.

## 380: How do you add automated accessibility checks for library components in CI?

- Storybook a11y addon (axe) on every story, run with the Storybook test runner or Vitest addon.
- `@axe-core/playwright` in e2e tests:

```ts
import AxeBuilder from "@axe-core/playwright";

test("checkout has no a11y violations", async ({ page }) => {
  await page.goto("/checkout");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

- angular-eslint template accessibility rules for static checks.

Automated tools catch maybe a third of problems, so manual testing is still needed.

## 381: How does Ionic's page caching affect Angular lifecycle and memory?

`ion-router-outlet` keeps previous pages in the DOM when you navigate forward, so going back is instant and keeps scroll position. That means `ngOnDestroy` doesn't run when you navigate forward, only when the page is popped. Subscriptions and timers keep running in hidden pages.

Use `ionViewWillEnter`/`ionViewWillLeave` to start and stop work when a page is shown or hidden, and be careful with deep stacks of heavy pages. `navigateRoot` clears the stack.

## 382: What are the main performance tips for Ionic Angular apps?

- Import standalone components from `@ionic/angular/standalone` so unused ones are tree-shaken.
- Use virtual scrolling for long lists (CDK virtual scroll works inside `ion-content` with some setup), or paginate.
- Lazy load pages with `loadComponent`.
- Avoid heavy work in `ionViewWillEnter`, which runs during the transition animation.
- Use OnPush or zoneless change detection.
- Test on a real low-end Android device, not only in the desktop browser.

## 383: How do you share code between an Ionic mobile app and an Angular web app?

Put shared code in libraries (Nx or Angular CLI libraries): data access, stores, models, utilities, and even presentational components if they don't depend on Ionic. Keep UI that depends on Ionic or on the web UI kit in app-specific libraries. Use DI to provide platform-specific services (for example a `StorageService` that uses Capacitor Preferences on mobile and localStorage on web).

## 384: How does @angular/localize work at build time?

The compiler turns `i18n` attributes in templates into `$localize` tagged template calls. At build time, the localize step finds every `$localize` call in the output bundles and replaces it with the translated string for each locale, creating one output per locale. Messages are matched by ID: a custom ID (`@@myId`) or a hash of the text and meaning.

Because this happens after bundling, building many locales is fast: the app is built once and then translated many times.

## 385: What are the pitfalls of @angular/localize's message IDs?

Without custom IDs, the ID is a hash of the text and meaning. If you fix a typo in the source text, the ID changes and all translations of that message are lost until retranslated. Two identical texts with different meanings need a meaning (`i18n="noun|Label for a file@@..."`) or they share a translation.

Use custom IDs (`@@checkout.payButton`) for stable messages, or use a merge tool that keeps translations when IDs change.

## 386: How do you translate text inside third-party components that don't support i18n?

- Many libraries have their own i18n APIs: Angular Material's `MatPaginatorIntl`, `MAT_DATE_LOCALE` and `DateAdapter.setLocale`; PrimeNG's `PrimeNG.setTranslation()`; NG-ZORRO's `NzI18nService.setLocale()`.
- Connect those to your translation library, for example extend `MatPaginatorIntl` and fill it from Transloco, calling `changes.next()` when the language changes.

```ts
@Injectable()
export class TranslatedPaginatorIntl extends MatPaginatorIntl {
  private transloco = inject(TranslocoService);

  constructor() {
    super();
    this.transloco.langChanges$.subscribe(() => {
      this.itemsPerPageLabel = this.transloco.translate(
        "paginator.itemsPerPage",
      );
      this.nextPageLabel = this.transloco.translate("paginator.next");
      this.changes.next();
    });
  }
}
```

## 387: How do you set Angular's LOCALE_ID together with a runtime i18n library?

`LOCALE_ID` affects built-in pipes (`DatePipe`, `CurrencyPipe`, `DecimalPipe`) and is fixed when the app starts. You must register locale data (`registerLocaleData`) for each locale.

Options with runtime i18n:

- Reload the app when the language changes and set `LOCALE_ID` from storage at startup.
- Pass the locale to pipes explicitly (`{{ price | currency: 'EUR' : 'symbol' : '' : locale() }}`).
- Use Transloco's locale plugin pipes, which follow the active language.

This mismatch (translated text but English number formats) is a common bug in runtime i18n setups.

## 388: How do you make charts handle large data sets in Angular?

- Use a canvas-based library (ECharts, Chart.js) instead of SVG for thousands of points. ECharts also has `large` mode and progressive rendering.
- Reduce data before drawing: downsample (LTTB algorithm) or aggregate on the server.
- Turn off animations for big data sets.
- Create the chart outside the Angular zone (if using Zone.js) and update with the library's API instead of recreating it.
- Load the chart library lazily with `@defer`.

## 389: How do you make ECharts tree-shakable in Angular?

Import only the parts you use from `echarts/core`:

```ts
import * as echarts from "echarts/core";
import { BarChart, LineChart } from "echarts/charts";
import {
  GridComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([
  BarChart,
  LineChart,
  GridComponent,
  TooltipComponent,
  LegendComponent,
  CanvasRenderer,
]);

export const appConfig = {
  providers: [provideEchartsCore({ echarts })],
};
```

Importing the full `echarts` package adds around 1 MB of JavaScript. The core approach can cut it to a fraction of that.

## 390: How do you build a reusable chart wrapper that works with signals?

```ts
import {
  Component,
  ElementRef,
  afterNextRender,
  effect,
  inject,
  input,
  DestroyRef,
} from "@angular/core";
import type { ECharts, EChartsCoreOption } from "echarts/core";

@Component({
  selector: "app-echart",
  template: "",
  styles: ":host { display: block; height: 320px; }",
})
export class EChart {
  options = input.required<EChartsCoreOption>();
  private el = inject(ElementRef<HTMLElement>);
  private destroyRef = inject(DestroyRef);
  private chart?: ECharts;

  constructor() {
    afterNextRender(async () => {
      const echarts = await import("./echarts-setup").then((m) => m.echarts);
      this.chart = echarts.init(this.el.nativeElement);
      this.chart.setOption(this.options());
      const observer = new ResizeObserver(() => this.chart?.resize());
      observer.observe(this.el.nativeElement);
      this.destroyRef.onDestroy(() => {
        observer.disconnect();
        this.chart?.dispose();
      });
    });

    effect(() => {
      const opts = this.options();
      this.chart?.setOption(opts, { notMerge: true });
    });
  }
}
```

The effect updates the chart whenever the options signal changes, the `ResizeObserver` handles container resizing, and the library loads lazily in the browser only.

## 391: How would you handle a slow, very large form built with Formly or reactive forms?

- Split it into steps or tabs, and only create controls for the visible part (or use `@defer` for sections).
- Use `updateOn: 'blur'` for expensive validators.
- Use OnPush in custom field components.
- Avoid valueChanges subscriptions on the whole form that recompute everything. Listen to specific controls.
- Move cross-field validation into one group validator instead of many expressions.
- Consider signal forms, where only the fields that depend on a change are recomputed.

## 392: How do you integrate ng-select or other custom inputs with signal forms?

Signal forms bind to controls through the `[field]` directive (named `[control]` or `[formField]` in some versions, check yours). Native inputs work out of the box. Custom components need to implement the signal forms control interface (a `value` model signal and optional state inputs like `disabled`, `errors`, `touched`). Libraries that only implement `ControlValueAccessor` work through a compatibility layer in recent versions, or you write a small wrapper component.

Since signal forms are still new and experimental, check each UI library's support before using them together in a big app.

## 393: How do you choose between ngx-mask and writing your own masking directive?

ngx-mask handles many edge cases: cursor position when inserting in the middle, paste, deletion of separators, special characters, prefixes and suffixes, number separators. Writing your own seems easy but these cases are tricky, and bugs make forms frustrating.

Write your own only for one simple fixed format, or when you need behavior ngx-mask can't do. Another option is `maskito` (from the Taiga UI team), which is framework agnostic and very configurable.

## 394: How do you handle time zones correctly with Material date pickers?

The Material datepicker with the native adapter creates `Date` objects at local midnight. When you send that to the server with `toISOString()`, it converts to UTC, which can move the date to the previous day for users east of UTC.

Fixes:

- For date-only values (birthdays), send a string like `2026-10-28` (format it without time zone conversion), and parse it as local.
- Use the Luxon or date-fns adapter with UTC options (the Luxon adapter has `useUtc`).
- For date-time values, store UTC on the server and convert to the user's zone only for display.

## 395: How do you prevent layout shift when UI library components load?

- Reserve space for lazy components (`@defer` placeholders with the same size).
- Load icon fonts with `font-display: block` or use SVG icons, so icon names don't flash as text ("home", "menu").
- Include library CSS in the initial bundle if components are above the fold, instead of loading it later.
- For PrimeNG styled mode, styles are injected at runtime; with SSR, make sure they are included in the server HTML.
- Give images and charts fixed dimensions or aspect ratios.

## 396: How do Material icon fonts affect performance, and how can you improve it?

The Material Icons and Symbols fonts are big (Symbols with all variations is several MB). Loading them from Google Fonts adds a request and a render delay, and icons show as text until the font loads.

Improvements:

- Load only the variant you use, and use the `text=` parameter of Google Fonts to subset to your icon names.
- Self-host a subset of the font.
- Switch to SVG icons registered in `MatIconRegistry`, or an icon library that bundles only used icons (like `@ng-icons`).

## 397: How do you reduce the bundle size of an app that uses many libraries?

- Measure first (`--stats-json`, source-map-explorer).
- Replace large libraries with smaller ones (Moment → date-fns, lodash → lodash-es or native, full ECharts → core imports).
- Import from secondary entry points and single components, not barrels that pull everything.
- Lazy load routes and use `@defer` for heavy components.
- Load rarely used libraries (Excel export, PDF) with dynamic `import()`.
- Remove unused libraries (`npx depcheck`).
- Set budgets in `angular.json` so growth is noticed in CI.

## 398: Why can barrel files (index.ts) hurt tree-shaking with libraries?

A barrel re-exports many things from one entry point. If any of the re-exported modules has side effects (top-level code, or the bundler can't prove it has none), the bundler keeps them even if you only use one export. In a monorepo, a big shared `index.ts` can pull large parts of the code into every chunk, and it also slows down builds and tests.

Use secondary entry points or smaller libraries, mark packages `"sideEffects": false` when true, and avoid side effects at module level.

## 399: How does `sideEffects` in package.json affect Angular libraries?

`"sideEffects": false` tells the bundler that importing a file only matters for its exports. If nothing from the file is used, it can be removed. Angular packages built with ng-packagr set this. If a library has files that must run on import (polyfills, global CSS imports, `registerLocaleData`), it should list them: `"sideEffects": ["*.css", "./polyfills.js"]`.

A library that wrongly sets `false` can lose needed code, and a library that doesn't set it may not tree-shake well.

## 400: How do you load a library from a CDN instead of the bundle, and when is it a good idea?

You can add a `<script>` tag (or load it dynamically) and declare types with `declare const`. For example, the Google Maps API must be loaded this way.

It's rarely a good idea for normal libraries: you lose tree-shaking and type-checked imports, browsers no longer share caches across sites (cache partitioning), and you add a third-party dependency for availability and security (use Subresource Integrity if you do it). It makes sense for libraries that are designed to be loaded from their own servers (maps, payment SDKs like Stripe.js, analytics).

## 401: How do you handle a library that registers global styles that conflict with yours?

- Load its styles first and yours after, or put the library in a lower CSS cascade layer (`@layer vendor`), so your rules win without `!important`.
- Import only the parts of its CSS you need, if it offers split files.
- Scope your global styles with a class instead of styling bare elements.
- If the library uses Shadow DOM or CSS variables, customize through those.
- For Tailwind preflight conflicts, you can turn off parts of preflight or reset specific components.

## 402: How do UI libraries handle styles with Angular's view encapsulation?

Library components usually use `ViewEncapsulation.None` and global class names (Material's `.mat-mdc-*`, PrimeNG's `.p-*`), with theme styles included globally. That's why you can't style them from your component's CSS by default: your styles get the `_ngcontent` attribute and don't match the library's elements.

Options: use the library's theming API, put overrides in global styles scoped by a parent class, or (last resort) use `::ng-deep`, which is deprecated in spirit and leaks styles if not scoped under `:host`.

## 403: How do you customize Material components without ::ng-deep?

- Override mixins (`mat.form-field-overrides`, `mat.button-overrides`) scoped to a class in global styles or in the component's styles with `:host`:

```scss
@use "@angular/material" as mat;

:host {
  @include mat.form-field-overrides(
    (
      outlined-outline-color: var(--mat-sys-outline-variant),
      container-height: 40px,
    )
  );
}
```

Since tokens are CSS variables, they cascade into child components even with emulated encapsulation. This is the reason Material moved to tokens.

- `panelClass` options for overlays (dialogs, menus, selects), which add your class to the overlay panel, then style that class globally.

## 404: How does PrimeNG inject styles at runtime and what does that mean for CSP?

In styled mode, PrimeNG generates CSS from design tokens in JavaScript and adds `<style>` elements to the document. A strict Content Security Policy that blocks inline styles (`style-src 'self'` without `'unsafe-inline'`) blocks those. PrimeNG supports a CSP nonce through its config (`csp: { nonce: '...' }`), and Angular has `CSP_NONCE` (or the `ngCspNonce` attribute) for its own styles. Use the same nonce from the server for both.

Angular Material uses static CSS, so it doesn't have this issue.

## 405: How do you use a strict Content Security Policy with Angular and common libraries?

- Angular: set `ngCspNonce` on the root element or provide `CSP_NONCE`, and turn on `autoCsp` in the build (newer Angular versions) for hashes of inline scripts.
- Google Maps, Stripe, analytics: allow their domains in `script-src`, `connect-src`, `img-src` and `frame-src`.
- Libraries that use `eval` or `new Function` (some template engines, older charting code) need `'unsafe-eval'`, which you should avoid. Check for this before adding a library.
- Libraries that inject inline styles need a nonce or `'unsafe-inline'` for styles.
- Use Trusted Types (`require-trusted-types-for 'script'`); Angular supports them, but some libraries break with them.

## 406: How do Trusted Types work with Angular and third-party libraries?

Trusted Types is a browser feature that blocks assigning plain strings to dangerous DOM sinks like `innerHTML` and `script.src`. Angular supports it: its sanitizer creates trusted values through an `angular` policy.

Third-party libraries that set `innerHTML` with strings will throw errors when Trusted Types is enforced. Options: check if the library has Trusted Types support, create a policy for it (named and allowed in the CSP), or replace it. Start with `Content-Security-Policy-Report-Only` to find violations before enforcing.

## 407: What risks come with postinstall scripts in npm packages, and how do you reduce them?

Install scripts run any code on the developer's machine or CI with their permissions. A compromised package (or a typosquatted name) can steal tokens, SSH keys or environment variables.

Reduce the risk by:

- installing with `--ignore-scripts` in CI where possible, and allowing scripts only for packages that need them
- using lock files and `npm ci`
- reviewing new dependencies and using tools that flag suspicious packages (Socket, Snyk)
- keeping CI secrets scoped and short-lived
- using a private registry or proxy with policies in companies

## 408: How do you keep many Angular libraries up to date without breaking things?

- Use Renovate or Dependabot with grouping (all Angular packages in one PR, all NgRx packages in one PR).
- Auto-merge patch updates if tests pass.
- Do major updates one at a time, reading changelogs.
- Have good test coverage on critical flows and visual regression tests for UI libraries.
- Schedule a regular "dependency day" instead of letting updates pile up for a year.

## 409: How do you decide whether to build a component yourself or use a library?

Build it yourself when:

- it's simple (a badge, a card) or core to your product's identity
- library options don't match your design or accessibility needs
- the library would be large for what you use

Use a library when:

- it's complex and well-solved (data grid, date picker, rich text editor, virtual scroll)
- accessibility and edge cases would take weeks to get right
- the library is well maintained and fits your stack

Also consider the long-term cost: a library you don't control can block upgrades, while your own code needs maintenance.

## 410: What would you do if a library you depend on is abandoned?

1. Check for a maintained fork or a community takeover.
2. Measure how widely it's used in your code.
3. If usage is small, replace it now.
4. If usage is large, wrap it behind your own API first, then replace the implementation.
5. As a short-term fix, fork it into your organization, apply Angular compatibility patches, and publish to your private registry.

Examples from the past: `@ngneat/until-destroy` (replaced by `takeUntilDestroyed`), Akita (to Elf or NgRx), Protractor (to Playwright/Cypress), `ngx-build-plus` (to esbuild builders).

## 411: How do you migrate from Karma/Jasmine to Vitest in a big Angular project?

1. Run the Angular CLI's migration schematic if available for your version, which updates `angular.json` to the `@angular/build:unit-test` builder and rewrites common Jasmine APIs.
2. Fix remaining Jasmine-specific code: `jasmine.createSpyObj`, custom matchers, `jasmine.clock`, `done` callbacks.
3. Check tests that depend on a real browser (layout, focus) and either run them in Vitest browser mode or rewrite them.
4. Update libraries: Spectator has a Vitest entry point; ng-mocks works with Vitest with `ngMocks.autoSpy('vi')` or similar setup.
5. Migrate in steps if needed: Nx and multi-project workspaces can run different runners per project.

## 412: Why might a Jest setup break after an Angular upgrade?

- `jest-preset-angular` needs a version compatible with the new Angular and TypeScript.
- Angular packages are ESM only, so `transformIgnorePatterns` must allow transforming `@angular`, `rxjs` and other ESM libraries (`node_modules/(?!.*\\.mjs$)` style patterns).
- Zone setup changed (`setupZoneTestEnv` vs `setupZonelessTestEnv`).
- New Angular features (like `@defer`, signal inputs) may need newer preset versions.

This maintenance cost is one reason many teams are moving to the official Vitest builder.

## 413: How does ng-mocks create mocks of components and what are the limits?

ng-mocks reads the Angular metadata of a component (selector, inputs, outputs, exportAs, content queries) and generates a new class with the same metadata but an empty template (or one that renders projected content and templates if you ask). Inputs accept values, outputs are real `EventEmitter`/output refs you can trigger, and methods become spies with `autoSpy`.

Limits: mocked components don't behave like the real ones, so tests can pass while integration is broken. Signal-based APIs (`input()`, `model()`, `viewChild()`) are supported in recent versions, but always use the latest ng-mocks with new Angular releases.

## 414: How do you test a component that uses TanStack Query?

Provide a fresh `QueryClient` per test with retries off, and mock the HTTP layer:

```ts
import {
  provideTanStackQuery,
  QueryClient,
} from "@tanstack/angular-query-experimental";
import { provideHttpClient } from "@angular/common/http";
import {
  provideHttpClientTesting,
  HttpTestingController,
} from "@angular/common/http/testing";

beforeEach(() => {
  TestBed.configureTestingModule({
    providers: [
      provideHttpClient(),
      provideHttpClientTesting(),
      provideTanStackQuery(
        new QueryClient({ defaultOptions: { queries: { retry: false } } }),
      ),
    ],
  });
});

it("shows todos", async () => {
  const fixture = TestBed.createComponent(Todos);
  const http = TestBed.inject(HttpTestingController);
  fixture.detectChanges();

  http.expectOne("/api/todos").flush([{ id: 1, title: "Write tests" }]);
  await fixture.whenStable();

  expect(fixture.nativeElement.textContent).toContain("Write tests");
});
```

Sharing one `QueryClient` between tests leaks cached data from one test to another.

## 415: How do you share a configured Storybook decorator for all stories (theme, translations, router)?

Put it in `.storybook/preview.ts`:

```ts
import type { Preview } from "@storybook/angular";
import { applicationConfig } from "@storybook/angular";
import { provideRouter } from "@angular/router";
import { provideAnimationsAsync } from "@angular/platform-browser/animations/async";
import { provideTransloco } from "@jsverse/transloco";
import { provideHttpClient } from "@angular/common/http";
import { StorybookTranslocoLoader } from "./transloco-loader";

const preview: Preview = {
  decorators: [
    applicationConfig({
      providers: [
        provideRouter([]),
        provideAnimationsAsync(),
        provideHttpClient(),
        provideTransloco({
          config: { availableLangs: ["en"], defaultLang: "en" },
          loader: StorybookTranslocoLoader,
        }),
      ],
    }),
  ],
};

export default preview;
```

Add a toolbar global (Storybook `globalTypes`) to switch theme or language across stories.

## 416: How would you set up visual regression testing for an Angular component library?

- Write stories for each component state in Storybook.
- Use Chromatic, or the Storybook test runner/Vitest addon with Playwright screenshots stored in the repo.
- Run in CI on every PR and require approval for visual changes.
- Use fixed fonts, disable animations, and mock dates and random data, so screenshots are stable.
- Test both light and dark themes, and a couple of viewport sizes.

## 417: How do you build an Angular library that supports several major Angular versions?

- Compile with the lowest Angular version you support, using partial compilation.
- Set `peerDependencies` to a range like `"@angular/core": ">=19.0.0 <22.0.0"`.
- Avoid APIs that don't exist in the lowest version (or feature-detect carefully).
- Run your test suite against each supported version in CI (a matrix that installs different Angular versions).
- Many libraries instead release one major per Angular major, which is simpler to maintain but makes users update in lockstep.

## 418: How do you design a library's public API so it can grow without breaking users?

- Export only what users need from `public-api.ts`. Everything else is internal.
- Prefer provider functions with option objects (`provideMyLib({ ... })`) over many separate tokens, so you can add options without breaking.
- Use injection tokens with factory defaults for configuration.
- Mark experimental APIs clearly.
- Provide `ng update` migrations for breaking changes.
- Follow semantic versioning and keep a changelog.

## 419: How do you write a provider function with features, like `provideHttpClient(withInterceptors())`?

```ts
import {
  EnvironmentProviders,
  InjectionToken,
  makeEnvironmentProviders,
  Provider,
} from "@angular/core";

export interface NotifyConfig {
  duration: number;
}

export const NOTIFY_SOUND = new InjectionToken<string>("NOTIFY_SOUND");

export const NOTIFY_CONFIG = new InjectionToken<NotifyConfig>("NOTIFY_CONFIG", {
  factory: () => ({ duration: 3000 }),
});

export interface NotifyFeature {
  kind: "sound" | "position";
  providers: Provider[];
}

export function withSound(src: string): NotifyFeature {
  return {
    kind: "sound",
    providers: [{ provide: NOTIFY_SOUND, useValue: src }],
  };
}

export function provideNotify(
  config: Partial<NotifyConfig> = {},
  ...features: NotifyFeature[]
): EnvironmentProviders {
  return makeEnvironmentProviders([
    { provide: NOTIFY_CONFIG, useValue: { duration: 3000, ...config } },
    ...features.flatMap((f) => f.providers),
  ]);
}
```

`makeEnvironmentProviders` makes sure these providers can only be used at the environment level (app config or routes), not in a component's `providers`.

## 420: How do you let library users provide their own implementation of a service?

Define the contract as an interface or abstract class, and expose it through an injection token with a `factory` default:

```ts
export interface StorageAdapter {
  get(key: string): string | null;
  set(key: string, value: string): void;
}

export class LocalStorageAdapter implements StorageAdapter {
  get(key: string) {
    return localStorage.getItem(key);
  }
  set(key: string, value: string) {
    localStorage.setItem(key, value);
  }
}

export const STORAGE = new InjectionToken<StorageAdapter>("STORAGE", {
  providedIn: "root",
  factory: () => new LocalStorageAdapter(),
});
```

Users override it with `{ provide: STORAGE, useClass: CapacitorStorageAdapter }`. This is how Material lets you replace `DateAdapter`, `ErrorStateMatcher` and `MatPaginatorIntl`.

## 421: How do you make your library tree-shakable?

- Use `providedIn: 'root'` services or tokens with factories, so unused services are removed.
- Split features into secondary entry points.
- Avoid top-level side effects (registering things on import).
- Don't export everything from one big NgModule. Export standalone components individually.
- Set `"sideEffects": false` (ng-packagr does this) and make sure it's true.
- Check by building a sample app that imports one thing and inspecting the bundle.

## 422: How do you handle styles and theming in your own Angular library?

- Ship component styles with the components (in `styles`), using CSS variables for anything users may change.
- Provide a Sass or CSS theme file as an asset (`ng-package.json` `assets`), plus mixins if users use Sass.
- Export it through `package.json` `exports` (for example `"./theming": { "sass": "./_index.scss" }`) so users can `@use 'my-lib/theming'`.
- Document every CSS variable as public API.
- If you build on Material, follow its token naming and read Material system tokens as defaults.

## 423: How do Angular CDK and Material keep up with Angular releases, and what can libraries learn from it?

They release a major version together with each Angular major, use the same version numbers, run their tests against Angular's latest code, and provide `ng update` schematics for every breaking change, including automatic code changes. Deprecated APIs get at least two major versions of warning.

Lessons for library authors: align releases with Angular, deprecate before removing, give migrations, and test against Angular prereleases so you're ready on release day.

## 424: How do you debug "NullInjectorError: No provider for X" coming from a library?

- Check that you added the library's provider function (`provideToastr()`, `provideNgxMask()`, `provideAnimationsAsync()`) to the app config or the right route.
- For standalone components, check you imported the component/directive, not just installed the package.
- If the library uses an NgModule with `forRoot()`, use `importProvidersFrom(X.forRoot())`.
- If it happens only in tests, add the providers to `TestBed`.
- If two copies of the library or of Angular are installed (`npm ls @angular/core`), tokens from one copy don't match the other.
- Angular DevTools' injector tree shows where each provider is available.

## 425: How do you debug "NG0203: inject() must be called from an injection context" when using libraries?

Library functions like `injectQuery`, `injectParams`, `rxMethod` (when created), `toSignal` and `takeUntilDestroyed()` call `inject()` internally, so they must run in a constructor, a field initializer or a factory.

Fixes:

- Move the call to a field initializer.
- Pass an injector explicitly if the function supports it (`toSignal(obs, { injector })`, `injectQuery(fn, injector)`).
- Wrap in `runInInjectionContext(injector, () => ...)`.

It can also happen if two copies of `@angular/core` are loaded, for example with linked local packages or wrong micro frontend sharing.

## 426: Why do you get two copies of Angular when linking a local library, and how do you fix it?

With `npm link` or a file dependency, the linked library may resolve `@angular/core` from its own `node_modules`, so the app has two copies. DI tokens and classes don't match, which causes strange errors (NG0203, NullInjectorError, "not a known element").

Fixes:

- Use a monorepo with path mappings (Nx or Angular CLI library in the same workspace) instead of linking.
- If you must link, set `"preserveSymlinks": true` in `angular.json` and make sure the library doesn't have Angular installed in its own `node_modules`.
- Use `npm pack` and install the tarball to test like a real package.

## 427: How does ng-packagr build a library and what does it produce?

ng-packagr reads `ng-package.json`, compiles each entry point with the Angular compiler in partial mode, bundles the result into FESM2022 files with Rollup, generates `.d.ts` files (bundled per entry point), processes styles and assets, and writes a `package.json` with an `exports` map for every entry point. It checks entry points build in dependency order and that external dependencies are declared in `dependencies` or `peerDependencies` (or allowed in `allowedNonPeerDependencies`).

## 428: How do you choose between NgRx Store devtools and Angular DevTools for debugging state?

- Redux DevTools (with NgRx Store, NGXS, or SignalStore with `withDevtools`) show actions over time, state diffs, and time travel. Best for "why did the state change?".
- Angular DevTools shows components, their signals and inputs, the injector tree and a profiler, and in recent versions a signal graph showing how signals depend on each other. Best for "why did this component render?" and "where does this value come from?".

You often use both: Redux DevTools for store flows, Angular DevTools for rendering and DI issues.

## 429: How does the ngrx-toolkit's withDevtools work with SignalStore?

`withDevtools('books')` connects a SignalStore to Redux DevTools. It watches the store's state signal and sends a snapshot to the extension whenever it changes, under the store's name. Since SignalStore has no actions, entries are labeled generically unless you use `updateState(store, 'action name', ...)` from the toolkit instead of `patchState`, which gives each change a name.

It's for development only. Make sure it's removed or disabled in production builds (the toolkit has a no-op version for that).

## 430: Scenario: your Angular app's initial bundle grew from 400 KB to 1.2 MB after adding a few libraries. What do you do?

1. Build with `--stats-json` and look at what's in the main chunk.
2. Common causes: importing a full library (all of ECharts, all icons, `lodash` instead of `lodash-es`), a CommonJS library that doesn't tree-shake, a heavy library imported in the root component or a root service, or locale data for many languages (date-fns, Moment locales).
3. Fixes: switch to modular imports, move usage behind `@defer` or a lazy route, replace heavy libraries, load optional features with dynamic `import()`.
4. Add budgets to fail CI when the initial bundle passes a limit, so it doesn't happen again.

## 431: Scenario: a PrimeNG table with 5,000 rows and custom cell templates is slow. How do you improve it?

- Turn on `[virtualScroll]="true"` with a fixed `[virtualScrollItemSize]`, so only visible rows render.
- Or use lazy loading with server-side paging.
- Remove function calls and impure pipes from cell templates. Precompute display values (a `computed` that maps rows to view models).
- Use `dataKey` so PrimeNG tracks rows by ID.
- Use OnPush on the host component, and avoid replacing the whole array when one row changes.
- If you need grouping, pivoting and huge data sets, consider AG Grid.

## 432: Scenario: after upgrading Angular, a third-party date picker stops updating the UI until you click elsewhere. What is likely happening?

Most likely the app moved to zoneless change detection (default in new Angular versions or enabled during upgrade), and the library updates its internal state in callbacks (timers, DOM events it adds itself) without signals or `markForCheck()`. Before, Zone.js triggered change detection after those callbacks.

Fixes: update the library to a zoneless-compatible version; in your wrapper, call `ChangeDetectorRef.markForCheck()` (or set a signal) in the library's change callbacks; or, as a temporary step, keep Zone.js with `provideZoneChangeDetection()`.

## 433: Scenario: users see raw translation keys for a moment when the app loads. How do you fix it?

The first render happens before the translation file is loaded. Fixes:

- Preload the active language in `provideAppInitializer` and return the load promise, so bootstrap waits.
- With Transloco, use the structural directive, which doesn't render its content until translations are loaded.
- With SSR, send translations via `TransferState` so the client has them immediately.
- Cache translation files (service worker or HTTP cache headers) and put the default language inline in the bundle if it's small.

## 434: Scenario: your NgRx effects start firing twice. What could cause it?

- The effect is registered twice: `provideEffects` in both app config and a lazy route, or the same effect file listed twice.
- Two copies of `@ngrx/effects` are loaded (micro frontends or linked library).
- The action is dispatched twice (check Redux DevTools).
- An effect dispatches an action that it listens to itself, or two effects ping-pong.
- An effect is not functional and is also provided as a class.

Redux DevTools and logging inside the effect usually show which one it is.

## 435: Scenario: a Material dialog opened from a lazy-loaded route can't find a service provided in that route. Why?

`MatDialog` uses the injector of where it was provided (usually root) to create the dialog component, unless you pass one. Services provided in the lazy route's `providers` are in a child environment injector, which the root `MatDialog` doesn't see.

Fixes: pass `injector` in the dialog config (`this.dialog.open(MyDialog, { injector: this.injector })`), or provide `MatDialog` in the route's providers so it uses that injector, or pass the data/service instance through `data`.

## 436: Scenario: you need to build an admin app quickly with lots of tables, forms and charts. Which libraries would you pick and why?

A practical stack:

- UI: PrimeNG or NG-ZORRO for the large set of ready components (data table with filters, tree, date pickers, file upload), or Angular Material plus AG Grid if you prefer the official kit.
- Data grid: AG Grid Community for big tables, or the UI kit's table if needs are simple.
- Forms: reactive forms; Formly if many forms are driven by configuration.
- Charts: ngx-echarts or the UI kit's chart component.
- State: signals and a few SignalStores; TanStack Query or `httpResource` for API data.
- Auth: an OIDC library matching your identity provider.
- Testing: Vitest with Angular Testing Library, Playwright for e2e.

Keep the number of UI kits to one, to avoid fighting two theming systems.

## 437: Scenario: your design team wants a custom look that doesn't match Material or PrimeNG. How do you build the UI layer?

- Use headless primitives for behavior: Angular CDK, Angular Aria, or Spartan's brain package.
- Style with Tailwind or your own CSS variables based on the design tokens from the designers.
- Build a small set of your own components in a library, document them in Storybook, test with harnesses or Testing Library, and run visual regression tests.
- For a few complex widgets (date picker, data grid) use an unstyled or highly themeable library (PrimeNG unstyled mode, AG Grid themes) instead of building them.

## 438: Scenario: you must support offline use for a field service app built with Angular. Which libraries help?

- `@angular/service-worker` (or Workbox) to cache the app shell and API responses.
- IndexedDB through a wrapper like Dexie.js or `idb` for local data, since localStorage is too small and synchronous.
- A sync strategy: queue changes locally and send them when online (Background Sync where supported, or your own retry queue).
- Capacitor plugins if it's packaged as a mobile app (file system, network status).
- TanStack Query's persisters can keep query caches in storage, and its `networkMode` handles offline states.

Design conflict handling with the backend early, since two users can change the same record offline.

## 439: Scenario: a page with an embedded rich text editor leaks memory each time users navigate to it. How do you find and fix it?

1. In Chrome DevTools Memory, take a heap snapshot, navigate to the page and away several times, take another snapshot, and compare. Look for detached DOM trees and growing counts of the editor's classes or your component.
2. Common causes: the editor is never destroyed, it registered global listeners (window resize, document selectionchange), or your code subscribed to its events without cleanup.
3. Fix: call the editor's `destroy()` in `DestroyRef.onDestroy`, remove listeners, and unsubscribe with `takeUntilDestroyed`. If you use a wrapper library (ngx-quill, TinyMCE Angular), make sure it's up to date and that you don't keep references to the editor instance in a root service.

## 440: Scenario: you need SSR for SEO, but a key library (a carousel) breaks on the server. What are your options?

- Render it only in the browser with `@defer (on idle)` or `@defer (on viewport)`. The server renders the placeholder, which can include the first slide as plain HTML for SEO.
- Load the library with dynamic `import()` inside `afterNextRender`.
- Check if a newer version or another library supports SSR (many CSS-scroll-snap based carousels need very little JS).
- As a last resort, provide a server-side mock of the library through DI.

Make sure the server HTML has the important content (titles, text, links) even if the interactive part loads later.

## 441: Scenario: your team uses both ngx-translate and @angular/localize in different parts of the app. Is that a problem?

It works technically but causes problems: two workflows for translators, two sets of files, text formatted differently, and features like language switching that only work in part of the app. `LOCALE_ID` follows the localize build, while ngx-translate follows its own active language, so dates and text can disagree.

Pick one approach for the app. If you migrate, do it feature by feature, with a shared language source (for example a cookie) that both read during the transition.

## 442: Scenario: a micro frontend built with an older Angular version must run inside a shell with a newer version. How do you approach it?

Native Federation sharing doesn't work well across Angular major versions, since `@angular/core` can't be shared. Options:

- Wrap the older app as web components with Angular Elements, each bringing its own Angular runtime (bigger bundles, but isolated).
- Load it in an iframe for full isolation (simplest, but harder communication and styling).
- Upgrade the older app so versions match, which is best long term.

Pass data through custom events, a small shared event bus on `window`, or URL state, and avoid sharing Angular services across the boundary.

## 443: Scenario: you need to show 100,000 points on a map. Which approach would you use?

- Don't create 100,000 DOM markers or Angular components. Use a map library that renders on canvas or WebGL (MapLibre GL layers, Leaflet with canvas renderer or a WebGL plugin, deck.gl).
- Cluster points (Supercluster) so only a few hundred markers show at a time.
- Load points by viewport and zoom from the server (vector tiles or bbox queries).
- Keep data outside Angular change detection; update the map source directly when data changes.
- Show details in a single popup component created on click.

## 444: Scenario: your app uses Moment.js, lodash, jQuery and an old jQuery date picker. How would you plan modernization?

1. Measure their bundle impact and where they are used.
2. Replace jQuery plugins first, since they fight Angular's DOM control: swap the date picker for a Material/PrimeNG/ng-bootstrap one or the native `<input type="date">`.
3. Replace Moment with date-fns or Luxon, file by file, using a thin date utility module so the change is in one place.
4. Replace lodash calls with native methods or `lodash-es` imports.
5. Remove jQuery once nothing uses it.
6. Add lint rules (`no-restricted-imports`) to stop new usage of the old libraries during the migration.

## 445: Scenario: two teams in a monorepo use different UI kits and the main app looks inconsistent. What do you do?

- Agree on one design system and one main UI kit, with a written decision (ADR).
- Create a shared UI library in the monorepo with wrappers or own components, and a theme that maps tokens for that kit.
- Use Nx module boundary rules or `no-restricted-imports` to stop new imports of the other kit.
- Migrate screens gradually, starting with the most visible ones.
- Add Storybook and visual tests for the shared components so both teams see the same reference.

## 446: Scenario: Lighthouse shows high Total Blocking Time after adding a charting library to the dashboard. How do you fix it?

- Lazy load the chart library with `@defer (on viewport)` or `(on idle)`, so it's not parsed during startup.
- Use modular imports (ECharts core, Chart.js registered parts).
- Turn off initial animations, which run on the main thread.
- Reduce data points (aggregate on the server, downsample on the client).
- Render charts one at a time (stagger with `@defer (on idle)` per chart) instead of all at once.
- Move heavy data processing to a Web Worker (`ng generate web-worker`).

## 447: Scenario: you want to add analytics and A/B testing to an Angular app. What should you watch out for with these libraries?

- They add third-party scripts that can slow down the page. Load them after the app is interactive (or with `@defer (on idle)` for components that need them).
- Track route changes with Router events, since SPAs don't do full page loads.
- Respect consent (GDPR): don't load trackers until the user agrees. Use a consent management library and load scripts only after consent.
- A/B testing libraries that change the DOM can conflict with Angular rendering. Prefer feature flags read in Angular code (LaunchDarkly, Unleash, GrowthBook SDKs) over DOM-editing scripts.
- Update CSP to allow their domains, and never send personal data in URLs or events.

## 448: Scenario: you are asked to make an existing Angular Material app work well for right-to-left languages. What is involved?

- Set `dir="rtl"` on `<html>` (or a container) when the language is Arabic, Hebrew or Persian. The CDK's `Directionality` service (from `@angular/cdk/bidi`) reads it, and Material components (menus, sidenav, sliders, overlays) flip automatically.
- Use CSS logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`) in your own styles instead of left/right.
- Flip directional icons (arrows, chevrons) with a class or `transform: scaleX(-1)` in RTL.
- Check third-party libraries: PrimeNG, NG-ZORRO and AG Grid have RTL options, but some smaller libraries don't.
- Test charts, date pickers and number formatting in the RTL locale.

## 449: Scenario: a third-party component library exposes only NgModules, and your app is fully standalone and zoneless. Can you still use it?

Usually yes:

- Import the library's NgModule into your standalone component's `imports` for its components and directives.
- Use `importProvidersFrom(LibModule.forRoot())` in the app config for its root providers.
- For zoneless, test carefully: if the library relies on Zone.js to update the UI, you may need `markForCheck()` in callbacks or a wrapper component.

If the library also depends on removed APIs (like `ComponentFactoryResolver` patterns that are deprecated, or `ngcc`-era builds), it may not work at all on new Angular. Then look for an updated version or replacement.

## 450: What does a healthy library strategy look like for a long-lived Angular project?

- Keep the dependency list short. Every library must earn its place.
- Prefer the Angular team's packages and well-maintained, widely used libraries for core needs.
- Wrap libraries that are used everywhere behind your own small API, so they can be replaced.
- Document why each major library was chosen (ADRs) and who owns it.
- Update often, in small steps, with automated tools and good tests.
- Watch bundle size and performance budgets in CI.
- Review dependencies once or twice a year: remove unused ones, replace abandoned ones, and check that each one still supports your Angular version.

This keeps upgrades from turning into big projects every time Angular releases a new major version.
