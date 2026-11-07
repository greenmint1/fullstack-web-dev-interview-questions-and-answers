# Cypress Interview Questions and Answers

_Last updated: October 29, 2026_

450 Cypress interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Cypress 16 (16.2 at the time of writing). They use the current APIs: `cy.env()` and `Cypress.expose()` instead of the removed `Cypress.env()`, `cy.task()` instead of the removed `cy.exec()`, `cy.session()`, `cy.origin()`, `cy.press()`, `cy.getByRole()` and the newer AI features like `cy.prompt()`. Older APIs are mentioned where they still matter, since you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Cypress?](#1-what-is-cypress)
- [2: What types of tests can you write with Cypress?](#2-what-types-of-tests-can-you-write-with-cypress)
- [3: How is Cypress different from Selenium?](#3-how-is-cypress-different-from-selenium)
- [4: How does Cypress run your tests?](#4-how-does-cypress-run-your-tests)
- [5: Which browsers does Cypress support?](#5-which-browsers-does-cypress-support)
- [6: How do you install Cypress?](#6-how-do-you-install-cypress)
- [7: How do you open Cypress for the first time?](#7-how-do-you-open-cypress-for-the-first-time)
- [8: What is the difference between cypress open and cypress run?](#8-what-is-the-difference-between-cypress-open-and-cypress-run)
- [9: What is the default folder structure of a Cypress project?](#9-what-is-the-default-folder-structure-of-a-cypress-project)
- [10: What is cypress.config.js?](#10-what-is-cypressconfigjs)
- [11: Why do you use defineConfig?](#11-why-do-you-use-defineconfig)
- [12: What is the difference between the e2e and component sections in the config?](#12-what-is-the-difference-between-the-e2e-and-component-sections-in-the-config)
- [13: What is a spec file?](#13-what-is-a-spec-file)
- [14: What is the default naming pattern for spec files?](#14-what-is-the-default-naming-pattern-for-spec-files)
- [15: What libraries does Cypress use for writing tests?](#15-what-libraries-does-cypress-use-for-writing-tests)
- [16: What are describe and it?](#16-what-are-describe-and-it)
- [17: What are context and specify?](#17-what-are-context-and-specify)
- [18: What hooks are available in Cypress tests?](#18-what-hooks-are-available-in-cypress-tests)
- [19: How do you run only one test or skip a test?](#19-how-do-you-run-only-one-test-or-skip-a-test)
- [20: What is the Command Log?](#20-what-is-the-command-log)
- [21: What is the cy object?](#21-what-is-the-cy-object)
- [22: How do you open a page with cy.visit?](#22-how-do-you-open-a-page-with-cyvisit)
- [23: What is baseUrl and why should you set it?](#23-what-is-baseurl-and-why-should-you-set-it)
- [24: What does cy.get do?](#24-what-does-cyget-do)
- [25: What does cy.contains do?](#25-what-does-cycontains-do)
- [26: What is the recommended way to select elements?](#26-what-is-the-recommended-way-to-select-elements)
- [27: What is the difference between cy.get and .find?](#27-what-is-the-difference-between-cyget-and-find)
- [28: What does .within do?](#28-what-does-within-do)
- [29: How do you click an element?](#29-how-do-you-click-an-element)
- [30: How do you type into an input?](#30-how-do-you-type-into-an-input)
- [31: How do you type special keys like Enter or Escape?](#31-how-do-you-type-special-keys-like-enter-or-escape)
- [32: What is cy.press?](#32-what-is-cypress)
- [33: How do you clear an input?](#33-how-do-you-clear-an-input)
- [34: How do you check and uncheck checkboxes and radio buttons?](#34-how-do-you-check-and-uncheck-checkboxes-and-radio-buttons)
- [35: How do you choose an option in a select element?](#35-how-do-you-choose-an-option-in-a-select-element)
- [36: How do you upload a file?](#36-how-do-you-upload-a-file)
- [37: How do you double-click or right-click?](#37-how-do-you-double-click-or-right-click)
- [38: What does .trigger do?](#38-what-does-trigger-do)
- [39: How do you focus or blur an element?](#39-how-do-you-focus-or-blur-an-element)
- [40: How do you scroll in Cypress?](#40-how-do-you-scroll-in-cypress)
- [41: What does .should do?](#41-what-does-should-do)
- [42: What is .and used for?](#42-what-is-and-used-for)
- [43: What are some common assertions you use?](#43-what-are-some-common-assertions-you-use)
- [44: How do you write a negative assertion?](#44-how-do-you-write-a-negative-assertion)
- [45: What is the difference between should and expect?](#45-what-is-the-difference-between-should-and-expect)
- [46: What assertion libraries are available in Cypress?](#46-what-assertion-libraries-are-available-in-cypress)
- [47: What is the default timeout for commands?](#47-what-is-the-default-timeout-for-commands)
- [48: What is retry-ability in Cypress?](#48-what-is-retry-ability-in-cypress)
- [49: Are Cypress commands synchronous?](#49-are-cypress-commands-synchronous)
- [50: Why can't you store the result of cy.get in a variable?](#50-why-cant-you-store-the-result-of-cyget-in-a-variable)
- [51: What does .then do?](#51-what-does-then-do)
- [52: What does cy.wrap do?](#52-what-does-cywrap-do)
- [53: What are aliases in Cypress?](#53-what-are-aliases-in-cypress)
- [54: How do you use an alias for an element?](#54-how-do-you-use-an-alias-for-an-element)
- [55: Why should you avoid cy.wait with a fixed number?](#55-why-should-you-avoid-cywait-with-a-fixed-number)
- [56: How do you wait for a network request to finish?](#56-how-do-you-wait-for-a-network-request-to-finish)
- [57: How do you check the current URL?](#57-how-do-you-check-the-current-url)
- [58: How do you check the page title?](#58-how-do-you-check-the-page-title)
- [59: How do you go back, go forward or reload the page?](#59-how-do-you-go-back-go-forward-or-reload-the-page)
- [60: How do you change the viewport size?](#60-how-do-you-change-the-viewport-size)
- [61: What are fixtures?](#61-what-are-fixtures)
- [62: How do you load a fixture?](#62-how-do-you-load-a-fixture)
- [63: What is cy.request?](#63-what-is-cyrequest)
- [64: What is cy.intercept?](#64-what-is-cyintercept)
- [65: How do you stub a response with a fixture file?](#65-how-do-you-stub-a-response-with-a-fixture-file)
- [66: What does .its do?](#66-what-does-its-do)
- [67: What does .invoke do?](#67-what-does-invoke-do)
- [68: How do you pick a specific element from a list?](#68-how-do-you-pick-a-specific-element-from-a-list)
- [69: How do you move up and down the DOM tree?](#69-how-do-you-move-up-and-down-the-dom-tree)
- [70: What do .filter and .not do?](#70-what-do-filter-and-not-do)
- [71: How do you loop over elements?](#71-how-do-you-loop-over-elements)
- [72: How do you print a message in the Command Log?](#72-how-do-you-print-a-message-in-the-command-log)
- [73: How do you pause or debug a test?](#73-how-do-you-pause-or-debug-a-test)
- [74: What is time travel in Cypress?](#74-what-is-time-travel-in-cypress)
- [75: How do screenshots work in Cypress?](#75-how-do-screenshots-work-in-cypress)
- [76: Does Cypress record videos?](#76-does-cypress-record-videos)
- [77: How do you run tests headed or headless?](#77-how-do-you-run-tests-headed-or-headless)
- [78: How do you run tests in a specific browser?](#78-how-do-you-run-tests-in-a-specific-browser)
- [79: How do you run only some spec files from the command line?](#79-how-do-you-run-only-some-spec-files-from-the-command-line)
- [80: How do you run a single spec in open mode?](#80-how-do-you-run-a-single-spec-in-open-mode)
- [81: What is the support file?](#81-what-is-the-support-file)
- [82: How do you create a custom command?](#82-how-do-you-create-a-custom-command)
- [83: Where should you put custom commands?](#83-where-should-you-put-custom-commands)
- [84: Can you write Cypress tests in TypeScript?](#84-can-you-write-cypress-tests-in-typescript)
- [85: How do you set up tsconfig for Cypress?](#85-how-do-you-set-up-tsconfig-for-cypress)
- [86: How do you work with cookies in Cypress?](#86-how-do-you-work-with-cookies-in-cypress)
- [87: How do you read or set localStorage in a test?](#87-how-do-you-read-or-set-localstorage-in-a-test)
- [88: What is test isolation?](#88-what-is-test-isolation)
- [89: How do you access the window and document objects?](#89-how-do-you-access-the-window-and-document-objects)
- [90: How do you read and write files in a test?](#90-how-do-you-read-and-write-files-in-a-test)
- [91: What is cy.task?](#91-what-is-cytask)
- [92: What is setupNodeEvents?](#92-what-is-setupnodeevents)
- [93: How do you read environment variables in a test?](#93-how-do-you-read-environment-variables-in-a-test)
- [94: What is Cypress.expose?](#94-what-is-cypressexpose)
- [95: What happened to Cypress.env?](#95-what-happened-to-cypressenv)
- [96: How do you pass environment variables from the system or CI?](#96-how-do-you-pass-environment-variables-from-the-system-or-ci)
- [97: How do you override config values from the command line?](#97-how-do-you-override-config-values-from-the-command-line)
- [98: How do you change the timeout of a single command?](#98-how-do-you-change-the-timeout-of-a-single-command)
- [99: What is pageLoadTimeout?](#99-what-is-pageloadtimeout)
- [100: What is actionability?](#100-what-is-actionability)
- [101: What does force: true do?](#101-what-does-force-true-do)
- [102: What does the error "element is not visible" mean?](#102-what-does-the-error-element-is-not-visible-mean)
- [103: What does cy.focused return?](#103-what-does-cyfocused-return)
- [104: How do you check the value of an input?](#104-how-do-you-check-the-value-of-an-input)
- [105: What is the difference between have.text, contain and cy.contains?](#105-what-is-the-difference-between-havetext-contain-and-cycontains)
- [106: How do you check how many elements are on the page?](#106-how-do-you-check-how-many-elements-are-on-the-page)
- [107: What is the difference between not.exist and not.be.visible?](#107-what-is-the-difference-between-notexist-and-notbevisible)
- [108: What is Cypress Cloud?](#108-what-is-cypress-cloud)
- [109: What is Cypress Studio?](#109-what-is-cypress-studio)
- [110: What is cy.prompt?](#110-what-is-cyprompt)
- [111: What is cy.getByRole?](#111-what-is-cygetbyrole)
- [112: What is component testing in Cypress?](#112-what-is-component-testing-in-cypress)
- [113: What is cy.mount?](#113-what-is-cymount)
- [114: Which frameworks does Cypress component testing support?](#114-which-frameworks-does-cypress-component-testing-support)
- [115: What reporter does Cypress use by default?](#115-what-reporter-does-cypress-use-by-default)
- [116: Can Cypress test multiple browser tabs?](#116-can-cypress-test-multiple-browser-tabs)
- [117: Can Cypress control two browsers at the same time?](#117-can-cypress-control-two-browsers-at-the-same-time)
- [118: What are the main limitations of Cypress?](#118-what-are-the-main-limitations-of-cypress)
- [119: How does Cypress compare to Playwright?](#119-how-does-cypress-compare-to-playwright)
- [120: How is Cypress different from Jest?](#120-how-is-cypress-different-from-jest)
- [121: How do you turn on test retries?](#121-how-do-you-turn-on-test-retries)
- [122: What exit code does cypress run return?](#122-what-exit-code-does-cypress-run-return)
- [123: How do you add Cypress scripts to package.json?](#123-how-do-you-add-cypress-scripts-to-packagejson)
- [124: How do you check if Cypress is installed correctly?](#124-how-do-you-check-if-cypress-is-installed-correctly)
- [125: What is the Cypress binary cache?](#125-what-is-the-cypress-binary-cache)
- [126: How can you skip downloading the Cypress binary?](#126-how-can-you-skip-downloading-the-cypress-binary)
- [127: What system requirements does Cypress have?](#127-what-system-requirements-does-cypress-have)
- [128: What are the official Cypress Docker images?](#128-what-are-the-official-cypress-docker-images)
- [129: What is eslint-plugin-cypress?](#129-what-is-eslint-plugin-cypress)
- [130: What is Cypress._?](#130-what-is-cypress_)
- [131: What is Cypress.$?](#131-what-is-cypress)
- [132: How do you check which browser or OS the test runs on?](#132-how-do-you-check-which-browser-or-os-the-test-runs-on)
- [133: How do you get information about the current spec or test?](#133-how-do-you-get-information-about-the-current-spec-or-test)
- [134: What are cy.clock and cy.tick?](#134-what-are-cyclock-and-cytick)
- [135: What is cy.stub?](#135-what-is-cystub)
- [136: What is cy.spy?](#136-what-is-cyspy)
- [137: What is the difference between a stub and a spy?](#137-what-is-the-difference-between-a-stub-and-a-spy)
- [138: How do you use a callback function in should?](#138-how-do-you-use-a-callback-function-in-should)
- [139: What types of Cypress commands are there?](#139-what-types-of-cypress-commands-are-there)
- [140: What is a query command?](#140-what-is-a-query-command)
- [141: What happens when a test fails in Cypress?](#141-what-happens-when-a-test-fails-in-cypress)
- [142: Can you write a simple first test?](#142-can-you-write-a-simple-first-test)
- [143: How should you name and organize spec files?](#143-how-should-you-name-and-organize-spec-files)
- [144: How do you test a hover effect?](#144-how-do-you-test-a-hover-effect)
- [145: How do you check that an element has a CSS property?](#145-how-do-you-check-that-an-element-has-a-css-property)
- [146: How do you check an attribute value?](#146-how-do-you-check-an-attribute-value)
- [147: How do you check that a button is disabled or enabled?](#147-how-do-you-check-that-a-button-is-disabled-or-enabled)
- [148: How do you assert on a value you got from a command?](#148-how-do-you-assert-on-a-value-you-got-from-a-command)
- [149: What is the ElementSelector (Selector Playground)?](#149-what-is-the-elementselector-selector-playground)
- [150: What are the main benefits of Cypress?](#150-what-are-the-main-benefits-of-cypress)

### Moderate Questions (151-300)

- [151: How exactly does retry work for a chain of commands?](#151-how-exactly-does-retry-work-for-a-chain-of-commands)
- [152: Why shouldn't you chain more commands after an action?](#152-why-shouldnt-you-chain-more-commands-after-an-action)
- [153: How do you create a custom command that works on a subject?](#153-how-do-you-create-a-custom-command-that-works-on-a-subject)
- [154: What is Cypress.Commands.addQuery?](#154-what-is-cypresscommandsaddquery)
- [155: How do you overwrite an existing command?](#155-how-do-you-overwrite-an-existing-command)
- [156: How do you add TypeScript types for custom commands?](#156-how-do-you-add-typescript-types-for-custom-commands)
- [157: How do you log in without using the UI in every test?](#157-how-do-you-log-in-without-using-the-ui-in-every-test)
- [158: What is cy.session?](#158-what-is-cysession)
- [159: What is the validate option of cy.session?](#159-what-is-the-validate-option-of-cysession)
- [160: What does cacheAcrossSpecs do in cy.session?](#160-what-does-cacheacrossspecs-do-in-cysession)
- [161: What happens when you set testIsolation to false?](#161-what-happens-when-you-set-testisolation-to-false)
- [162: How do you match requests in cy.intercept?](#162-how-do-you-match-requests-in-cyintercept)
- [163: How do you change request headers with cy.intercept?](#163-how-do-you-change-request-headers-with-cyintercept)
- [164: How do you send a dynamic response from an intercept?](#164-how-do-you-send-a-dynamic-response-from-an-intercept)
- [165: How do you change a real response from the server?](#165-how-do-you-change-a-real-response-from-the-server)
- [166: How do you simulate a network error?](#166-how-do-you-simulate-a-network-error)
- [167: How do you simulate a slow network response?](#167-how-do-you-simulate-a-slow-network-response)
- [168: How do you check what the app sent in a request?](#168-how-do-you-check-what-the-app-sent-in-a-request)
- [169: How do you wait for the same request several times?](#169-how-do-you-wait-for-the-same-request-several-times)
- [170: How do you make an intercept match only a limited number of times?](#170-how-do-you-make-an-intercept-match-only-a-limited-number-of-times)
- [171: How do you intercept GraphQL requests?](#171-how-do-you-intercept-graphql-requests)
- [172: In what order are intercepts matched?](#172-in-what-order-are-intercepts-matched)
- [173: What is the difference between requestTimeout and responseTimeout in cy.wait?](#173-what-is-the-difference-between-requesttimeout-and-responsetimeout-in-cywait)
- [174: Should you stub every network request?](#174-should-you-stub-every-network-request)
- [175: How do you use fixtures with this context in hooks?](#175-how-do-you-use-fixtures-with-this-context-in-hooks)
- [176: How do aliases work with the this context?](#176-how-do-aliases-work-with-the-this-context)
- [177: What is the difference between query aliases and static aliases?](#177-what-is-the-difference-between-query-aliases-and-static-aliases)
- [178: Should tests share data with each other?](#178-should-tests-share-data-with-each-other)
- [179: How do you seed the database before a test?](#179-how-do-you-seed-the-database-before-a-test)
- [180: Why should you clean state before tests and not after?](#180-why-should-you-clean-state-before-tests-and-not-after)
- [181: What options does cy.request support?](#181-what-options-does-cyrequest-support)
- [182: How do you test an API with Cypress?](#182-how-do-you-test-an-api-with-cypress)
- [183: Does cy.request use the browser's cookies?](#183-does-cyrequest-use-the-browsers-cookies)
- [184: What is cy.origin?](#184-what-is-cyorigin)
- [185: How do you pass values into cy.origin?](#185-how-do-you-pass-values-into-cyorigin)
- [186: What is injectDocumentDomain?](#186-what-is-injectdocumentdomain)
- [187: What does chromeWebSecurity: false do?](#187-what-does-chromewebsecurity-false-do)
- [188: How do you work with iframes?](#188-how-do-you-work-with-iframes)
- [189: How do you work with Shadow DOM?](#189-how-do-you-work-with-shadow-dom)
- [190: How do you test a file download?](#190-how-do-you-test-a-file-download)
- [191: What options does selectFile have?](#191-what-options-does-selectfile-have)
- [192: How do you test code that opens a new window with window.open?](#192-how-do-you-test-code-that-opens-a-new-window-with-windowopen)
- [193: How do you handle alert and confirm dialogs?](#193-how-do-you-handle-alert-and-confirm-dialogs)
- [194: How do you handle uncaught exceptions from the app?](#194-how-do-you-handle-uncaught-exceptions-from-the-app)
- [195: What is the difference between cy.on and Cypress.on?](#195-what-is-the-difference-between-cyon-and-cypresson)
- [196: What Cypress events can you listen to in the browser?](#196-what-cypress-events-can-you-listen-to-in-the-browser)
- [197: How do you change things in the app before it loads?](#197-how-do-you-change-things-in-the-app-before-it-loads)
- [198: How do you control dates with cy.clock?](#198-how-do-you-control-dates-with-cyclock)
- [199: How do you check stub calls with arguments?](#199-how-do-you-check-stub-calls-with-arguments)
- [200: How do you stub a method on an object the app uses?](#200-how-do-you-stub-a-method-on-an-object-the-app-uses)
- [201: How do you spy on console errors during a test?](#201-how-do-you-spy-on-console-errors-during-a-test)
- [202: How do test retries work in detail?](#202-how-do-test-retries-work-in-detail)
- [203: What are the common causes of flaky Cypress tests?](#203-what-are-the-common-causes-of-flaky-cypress-tests)
- [204: How do you fix a flaky test?](#204-how-do-you-fix-a-flaky-test)
- [205: What is conditional testing and why is it a problem?](#205-what-is-conditional-testing-and-why-is-it-a-problem)
- [206: When is conditional testing acceptable, and how do you do it safely?](#206-when-is-conditional-testing-acceptable-and-how-do-you-do-it-safely)
- [207: What does the "detached from the DOM" error mean?](#207-what-does-the-detached-from-the-dom-error-mean)
- [208: What does the error "element is being covered by another element" mean?](#208-what-does-the-error-element-is-being-covered-by-another-element-mean)
- [209: How does Cypress handle animations?](#209-how-does-cypress-handle-animations)
- [210: What is scrollBehavior?](#210-what-is-scrollbehavior)
- [211: How do you test a responsive design on several screen sizes?](#211-how-do-you-test-a-responsive-design-on-several-screen-sizes)
- [212: How do you write data-driven tests?](#212-how-do-you-write-data-driven-tests)
- [213: How do you use the Page Object Model in Cypress?](#213-how-do-you-use-the-page-object-model-in-cypress)
- [214: What are app actions and how do they compare to page objects?](#214-what-are-app-actions-and-how-do-they-compare-to-page-objects)
- [215: When should you use a custom command and when a plain function?](#215-when-should-you-use-a-custom-command-and-when-a-plain-function)
- [216: How do you run tests against different environments?](#216-how-do-you-run-tests-against-different-environments)
- [217: Can you have more than one config file?](#217-can-you-have-more-than-one-config-file)
- [218: How do you change the config inside setupNodeEvents?](#218-how-do-you-change-the-config-inside-setupnodeevents)
- [219: How do you change config for one test or one suite?](#219-how-do-you-change-config-for-one-test-or-one-suite)
- [220: Can you change config while a test runs?](#220-can-you-change-config-while-a-test-runs)
- [221: How do you use a .env file with Cypress?](#221-how-do-you-use-a-env-file-with-cypress)
- [222: Why is cy.env asynchronous and what does that change?](#222-why-is-cyenv-asynchronous-and-what-does-that-change)
- [223: What Node events can you listen to in setupNodeEvents?](#223-what-node-events-can-you-listen-to-in-setupnodeevents)
- [224: How do you change browser launch options?](#224-how-do-you-change-browser-launch-options)
- [225: What is a preprocessor in Cypress?](#225-what-is-a-preprocessor-in-cypress)
- [226: How do you collect code coverage from Cypress tests?](#226-how-do-you-collect-code-coverage-from-cypress-tests)
- [227: How do you generate HTML or JUnit reports?](#227-how-do-you-generate-html-or-junit-reports)
- [228: How do you use more than one reporter at once?](#228-how-do-you-use-more-than-one-reporter-at-once)
- [229: How do you run Cypress in CI?](#229-how-do-you-run-cypress-in-ci)
- [230: How do you run Cypress with GitHub Actions?](#230-how-do-you-run-cypress-with-github-actions)
- [231: Why and how do you cache the Cypress binary in CI?](#231-why-and-how-do-you-cache-the-cypress-binary-in-ci)
- [232: How do you run tests in parallel with Cypress Cloud?](#232-how-do-you-run-tests-in-parallel-with-cypress-cloud)
- [233: How can you run tests in parallel without Cypress Cloud?](#233-how-can-you-run-tests-in-parallel-without-cypress-cloud)
- [234: What are --group and --tag used for?](#234-what-are---group-and---tag-used-for)
- [235: What features does Cypress Cloud offer?](#235-what-features-does-cypress-cloud-offer)
- [236: What is Test Replay?](#236-what-is-test-replay)
- [237: How do you run only tests with a certain tag?](#237-how-do-you-run-only-tests-with-a-certain-tag)
- [238: How do you configure screenshots?](#238-how-do-you-configure-screenshots)
- [239: How do you configure video recording?](#239-how-do-you-configure-video-recording)
- [240: How do you do visual regression testing with Cypress?](#240-how-do-you-do-visual-regression-testing-with-cypress)
- [241: How do you check accessibility with Cypress?](#241-how-do-you-check-accessibility-with-cypress)
- [242: How do you set up component testing?](#242-how-do-you-set-up-component-testing)
- [243: How do you pass props and test events in a React component test?](#243-how-do-you-pass-props-and-test-events-in-a-react-component-test)
- [244: How do you mount a component that needs providers?](#244-how-do-you-mount-a-component-that-needs-providers)
- [245: How do you write a Vue component test?](#245-how-do-you-write-a-vue-component-test)
- [246: How do you write an Angular component test?](#246-how-do-you-write-an-angular-component-test)
- [247: Can you use cy.intercept in component tests?](#247-can-you-use-cyintercept-in-component-tests)
- [248: When should you use component tests and when E2E tests?](#248-when-should-you-use-component-tests-and-when-e2e-tests)
- [249: How do Cypress component tests compare to Jest with Testing Library?](#249-how-do-cypress-component-tests-compare-to-jest-with-testing-library)
- [250: How do you load global styles in component tests?](#250-how-do-you-load-global-styles-in-component-tests)
- [251: How do you debug a failing test in the Cypress app?](#251-how-do-you-debug-a-failing-test-in-the-cypress-app)
- [252: How do you use debugger in a Cypress test?](#252-how-do-you-use-debugger-in-a-cypress-test)
- [253: How do you see Cypress's own debug logs?](#253-how-do-you-see-cypresss-own-debug-logs)
- [254: How do you control typing speed?](#254-how-do-you-control-typing-speed)
- [255: How do you type text that contains curly braces?](#255-how-do-you-type-text-that-contains-curly-braces)
- [256: How do you type into a contenteditable element?](#256-how-do-you-type-into-a-contenteditable-element)
- [257: What options does .click accept?](#257-what-options-does-click-accept)
- [258: How do you test drag and drop?](#258-how-do-you-test-drag-and-drop)
- [259: How do you test a hover menu that opens with JavaScript?](#259-how-do-you-test-a-hover-menu-that-opens-with-javascript)
- [260: How do you test a specific cell in a table?](#260-how-do-you-test-a-specific-cell-in-a-table)
- [261: How do you compare a value before and after an action?](#261-how-do-you-compare-a-value-before-and-after-an-action)
- [262: How do you check that a list is sorted?](#262-how-do-you-check-that-a-list-is-sorted)
- [263: What is the difference between should(callback) and then(callback)?](#263-what-is-the-difference-between-shouldcallback-and-thencallback)
- [264: How do you add custom Chai assertions?](#264-how-do-you-add-custom-chai-assertions)
- [265: Can you write the Cypress config as an ES module or in TypeScript?](#265-can-you-write-the-cypress-config-as-an-es-module-or-in-typescript)
- [266: How do you run Cypress in a monorepo?](#266-how-do-you-run-cypress-in-a-monorepo)
- [267: How do you test login with a third-party provider like Google or Auth0?](#267-how-do-you-test-login-with-a-third-party-provider-like-google-or-auth0)
- [268: How do you test an email flow, like a password reset?](#268-how-do-you-test-an-email-flow-like-a-password-reset)
- [269: How do you wait for a loading spinner to go away?](#269-how-do-you-wait-for-a-loading-spinner-to-go-away)
- [270: How do you know the page is ready before testing it?](#270-how-do-you-know-the-page-is-ready-before-testing-it)
- [271: How do you clear all browser state manually?](#271-how-do-you-clear-all-browser-state-manually)
- [272: What changed for cookie commands in Cypress 16?](#272-what-changed-for-cookie-commands-in-cypress-16)
- [273: How do you run a shell command now that cy.exec is removed?](#273-how-do-you-run-a-shell-command-now-that-cyexec-is-removed)
- [274: Can you import Node modules like fs in a spec file?](#274-can-you-import-node-modules-like-fs-in-a-spec-file)
- [275: How do you generate random test data?](#275-how-do-you-generate-random-test-data)
- [276: What are some popular Cypress plugins?](#276-what-are-some-popular-cypress-plugins)
- [277: How do you test time zones and locales?](#277-how-do-you-test-time-zones-and-locales)
- [278: How do you fake the user's location?](#278-how-do-you-fake-the-users-location)
- [279: Should you stub window.fetch or use cy.intercept?](#279-should-you-stub-windowfetch-or-use-cyintercept)
- [280: How do you test WebSockets in Cypress?](#280-how-do-you-test-websockets-in-cypress)
- [281: How do you test a redirect?](#281-how-do-you-test-a-redirect)
- [282: How do you visit a page protected with basic auth?](#282-how-do-you-visit-a-page-protected-with-basic-auth)
- [283: How do you visit a page that returns an error status?](#283-how-do-you-visit-a-page-that-returns-an-error-status)
- [284: How do you test how the UI handles different server responses?](#284-how-do-you-test-how-the-ui-handles-different-server-responses)
- [285: Should you use cy.getByRole, data-cy attributes or Testing Library?](#285-should-you-use-cygetbyrole-data-cy-attributes-or-testing-library)
- [286: How do you use Testing Library with Cypress?](#286-how-do-you-use-testing-library-with-cypress)
- [287: How do you use Cypress Studio in practice?](#287-how-do-you-use-cypress-studio-in-practice)
- [288: How does cy.prompt handle sensitive data and changes in the app?](#288-how-does-cyprompt-handle-sensitive-data-and-changes-in-the-app)
- [289: How do you exclude some files from running as specs?](#289-how-do-you-exclude-some-files-from-running-as-specs)
- [290: What do watchForFileChanges and numTestsKeptInMemory do?](#290-what-do-watchforfilechanges-and-numtestskeptinmemory-do)
- [291: How do you run all specs at once in open mode?](#291-how-do-you-run-all-specs-at-once-in-open-mode)
- [292: How do you test a form validation message from the browser?](#292-how-do-you-test-a-form-validation-message-from-the-browser)
- [293: How do you test a page that polls the server?](#293-how-do-you-test-a-page-that-polls-the-server)
- [294: How do you test infinite scroll?](#294-how-do-you-test-infinite-scroll)
- [295: How do you check that something was copied to the clipboard?](#295-how-do-you-check-that-something-was-copied-to-the-clipboard)
- [296: How do you test print or other browser features that open native dialogs?](#296-how-do-you-test-print-or-other-browser-features-that-open-native-dialogs)
- [297: How do you check that no request was made?](#297-how-do-you-check-that-no-request-was-made)
- [298: How do you count how many times a request was made?](#298-how-do-you-count-how-many-times-a-request-was-made)
- [299: How do you block third-party scripts during tests?](#299-how-do-you-block-third-party-scripts-during-tests)
- [300: How do you test a feature behind a feature flag?](#300-how-do-you-test-a-feature-behind-a-feature-flag)

### Advanced Questions (301-450)

- [301: What is the architecture of Cypress?](#301-what-is-the-architecture-of-cypress)
- [302: Why does Cypress run the app inside an iframe?](#302-why-does-cypress-run-the-app-inside-an-iframe)
- [303: How does Cypress intercept network traffic?](#303-how-does-cypress-intercept-network-traffic)
- [304: How does the command queue work internally?](#304-how-does-the-command-queue-work-internally)
- [305: Why does mixing async/await with Cypress commands not work?](#305-why-does-mixing-asyncawait-with-cypress-commands-not-work)
- [306: Can you return a promise from .then()?](#306-can-you-return-a-promise-from-then)
- [307: How does Cypress know when a command is done?](#307-how-does-cypress-know-when-a-command-is-done)
- [308: What makes an assertion able to retry the chain before it?](#308-what-makes-an-assertion-able-to-retry-the-chain-before-it)
- [309: How do you write a custom query that retries correctly?](#309-how-do-you-write-a-custom-query-that-retries-correctly)
- [310: What exactly does Cypress check before an action?](#310-what-exactly-does-cypress-check-before-an-action)
- [311: How does Cypress decide if an element is visible?](#311-how-does-cypress-decide-if-an-element-is-visible)
- [312: Are Cypress events the same as real user events?](#312-are-cypress-events-the-same-as-real-user-events)
- [313: How does cy.type work internally?](#313-how-does-cytype-work-internally)
- [314: Why does cy.origin need serializable arguments?](#314-why-does-cyorigin-need-serializable-arguments)
- [315: What are the risks of setting chromeWebSecurity to false?](#315-what-are-the-risks-of-setting-chromewebsecurity-to-false)
- [316: What does modifyObstructiveCode do?](#316-what-does-modifyobstructivecode-do)
- [317: What is removeSRIAttributes?](#317-what-is-removesriattributes)
- [318: How does Cypress manage browser memory during long runs?](#318-how-does-cypress-manage-browser-memory-during-long-runs)
- [319: What do you do when the browser crashes during a run in CI?](#319-what-do-you-do-when-the-browser-crashes-during-a-run-in-ci)
- [320: How do you add Chromium flags in Docker to avoid shared memory problems?](#320-how-do-you-add-chromium-flags-in-docker-to-avoid-shared-memory-problems)
- [321: How big should a spec file be?](#321-how-big-should-a-spec-file-be)
- [322: How does Cypress Cloud decide which spec runs on which machine?](#322-how-does-cypress-cloud-decide-which-spec-runs-on-which-machine)
- [323: Are there alternatives to Cypress Cloud for recording and parallel runs?](#323-are-there-alternatives-to-cypress-cloud-for-recording-and-parallel-runs)
- [324: What exactly happens between tests when testIsolation is on?](#324-what-exactly-happens-between-tests-when-testisolation-is-on)
- [325: How does cy.session cache and restore state?](#325-how-does-cysession-cache-and-restore-state)
- [326: How do you use cy.session with logins across several origins?](#326-how-do-you-use-cysession-with-logins-across-several-origins)
- [327: How do you design test data so tests can run in parallel?](#327-how-do-you-design-test-data-so-tests-can-run-in-parallel)
- [328: How do you test against a shared environment like staging?](#328-how-do-you-test-against-a-shared-environment-like-staging)
- [329: What is a good strategy for mixing stubbed and real network tests?](#329-what-is-a-good-strategy-for-mixing-stubbed-and-real-network-tests)
- [330: How do you keep fixtures in sync with the real API?](#330-how-do-you-keep-fixtures-in-sync-with-the-real-api)
- [331: What request and response events can you use inside cy.intercept?](#331-what-request-and-response-events-can-you-use-inside-cyintercept)
- [332: How do you add a header to every request in all tests?](#332-how-do-you-add-a-header-to-every-request-in-all-tests)
- [333: Do intercepts carry over between tests?](#333-do-intercepts-carry-over-between-tests)
- [334: How do you match requests by query parameters correctly?](#334-how-do-you-match-requests-by-query-parameters-correctly)
- [335: What are common mistakes with URL patterns in cy.intercept?](#335-what-are-common-mistakes-with-url-patterns-in-cyintercept)
- [336: Can cy.wait('@alias') catch a request that happened before the wait?](#336-can-cywaitalias-catch-a-request-that-happened-before-the-wait)
- [337: How do you test a race condition, like two responses arriving in the wrong order?](#337-how-do-you-test-a-race-condition-like-two-responses-arriving-in-the-wrong-order)
- [338: How do cy.clock and network requests interact?](#338-how-do-cyclock-and-network-requests-interact)
- [339: What are the limits of cy.clock?](#339-what-are-the-limits-of-cyclock)
- [340: How do you stub something the app uses as soon as it starts?](#340-how-do-you-stub-something-the-app-uses-as-soon-as-it-starts)
- [341: How do you stop third-party scripts from affecting your tests?](#341-how-do-you-stop-third-party-scripts-from-affecting-your-tests)
- [342: How do you test a feature flag service that uses streaming?](#342-how-do-you-test-a-feature-flag-service-that-uses-streaming)
- [343: How do you test OAuth or OIDC login flows?](#343-how-do-you-test-oauth-or-oidc-login-flows)
- [344: How do you test two-factor authentication with one-time codes?](#344-how-do-you-test-two-factor-authentication-with-one-time-codes)
- [345: How do you deal with CAPTCHA in tests?](#345-how-do-you-deal-with-captcha-in-tests)
- [346: How do you test a payment form that lives in a cross-origin iframe?](#346-how-do-you-test-a-payment-form-that-lives-in-a-cross-origin-iframe)
- [347: How do you run tests across several browsers in CI?](#347-how-do-you-run-tests-across-several-browsers-in-ci)
- [348: What is the experimental WebKit support?](#348-what-is-the-experimental-webkit-support)
- [349: What does the deprecation of Electron as a test browser mean for you?](#349-what-does-the-deprecation-of-electron-as-a-test-browser-mean-for-you)
- [350: What are the differences between headed and headless runs?](#350-what-are-the-differences-between-headed-and-headless-runs)
- [351: How do you run Cypress from a Node script?](#351-how-do-you-run-cypress-from-a-node-script)
- [352: When would you use the Module API instead of the CLI?](#352-when-would-you-use-the-module-api-instead-of-the-cli)
- [353: How do you write a custom reporter?](#353-how-do-you-write-a-custom-reporter)
- [354: What happens if two plugins register the same Node event?](#354-what-happens-if-two-plugins-register-the-same-node-event)
- [355: How do you build a reusable Cypress plugin for your company?](#355-how-do-you-build-a-reusable-cypress-plugin-for-your-company)
- [356: What are good rules for designing custom commands?](#356-what-are-good-rules-for-designing-custom-commands)
- [357: How do you write a custom command with a good Command Log entry?](#357-how-do-you-write-a-custom-command-with-a-good-command-log-entry)
- [358: How do you hide passwords and tokens from the Command Log?](#358-how-do-you-hide-passwords-and-tokens-from-the-command-log)
- [359: How do you handle secrets in Cypress tests in CI?](#359-how-do-you-handle-secrets-in-cypress-tests-in-ci)
- [360: Why was Cypress.env removed in Cypress 16?](#360-why-was-cypressenv-removed-in-cypress-16)
- [361: How do you migrate a project from Cypress.env to the new APIs?](#361-how-do-you-migrate-a-project-from-cypressenv-to-the-new-apis)
- [362: What is your checklist for upgrading to Cypress 16?](#362-what-is-your-checklist-for-upgrading-to-cypress-16)
- [363: What were the main breaking changes in Cypress 14 and 15?](#363-what-were-the-main-breaking-changes-in-cypress-14-and-15)
- [364: How do you plan the upgrade of a big Cypress suite?](#364-how-do-you-plan-the-upgrade-of-a-big-cypress-suite)
- [365: How would you move a test suite from Selenium to Cypress?](#365-how-would-you-move-a-test-suite-from-selenium-to-cypress)
- [366: When would you pick Playwright over Cypress?](#366-when-would-you-pick-playwright-over-cypress)
- [367: Which metrics do you track for a Cypress suite?](#367-which-metrics-do-you-track-for-a-cypress-suite)
- [368: How do you handle flaky tests across a team?](#368-how-do-you-handle-flaky-tests-across-a-team)
- [369: How do you make a slow Cypress suite faster?](#369-how-do-you-make-a-slow-cypress-suite-faster)
- [370: Why shouldn't tests depend on the order they run in?](#370-why-shouldnt-tests-depend-on-the-order-they-run-in)
- [371: What should you know about hooks in the support file?](#371-what-should-you-know-about-hooks-in-the-support-file)
- [372: How do you run setup only once for the whole run?](#372-how-do-you-run-setup-only-once-for-the-whole-run)
- [373: How do hooks behave when a test is retried?](#373-how-do-hooks-behave-when-a-test-is-retried)
- [374: How do you use Cypress.currentRetry?](#374-how-do-you-use-cypresscurrentretry)
- [375: How do you debug tests that fail only in CI?](#375-how-do-you-debug-tests-that-fail-only-in-ci)
- [376: What is the difference between Test Replay, videos and screenshots for debugging?](#376-what-is-the-difference-between-test-replay-videos-and-screenshots-for-debugging)
- [377: How do you test an app in several languages?](#377-how-do-you-test-an-app-in-several-languages)
- [378: Can you measure performance with Cypress?](#378-can-you-measure-performance-with-cypress)
- [379: Can Cypress be used for load testing?](#379-can-cypress-be-used-for-load-testing)
- [380: How do you test code that runs in a web worker?](#380-how-do-you-test-code-that-runs-in-a-web-worker)
- [381: How do you test a canvas or WebGL app?](#381-how-do-you-test-a-canvas-or-webgl-app)
- [382: How do you test virtualized lists?](#382-how-do-you-test-virtualized-lists)
- [383: How do you wait for a condition that no query can check, like a background job?](#383-how-do-you-wait-for-a-condition-that-no-query-can-check-like-a-background-job)
- [384: How do you make tests with CSS animations stable?](#384-how-do-you-make-tests-with-css-animations-stable)
- [385: What should you know about Shadow DOM when testing web components?](#385-what-should-you-know-about-shadow-dom-when-testing-web-components)
- [386: How do you test a micro frontend application?](#386-how-do-you-test-a-micro-frontend-application)
- [387: What should you watch out for when testing server-rendered apps like Next.js?](#387-what-should-you-watch-out-for-when-testing-server-rendered-apps-like-nextjs)
- [388: What are the limits of component testing with Next.js?](#388-what-are-the-limits-of-component-testing-with-nextjs)
- [389: What changed for Angular component testing in Cypress 16?](#389-what-changed-for-angular-component-testing-in-cypress-16)
- [390: How do you customize the dev server for component tests?](#390-how-do-you-customize-the-dev-server-for-component-tests)
- [391: How does component testing work under the hood?](#391-how-does-component-testing-work-under-the-hood)
- [392: How do you provide a store like Redux or Pinia in component tests?](#392-how-do-you-provide-a-store-like-redux-or-pinia-in-component-tests)
- [393: How do you test routing in a component test?](#393-how-do-you-test-routing-in-a-component-test)
- [394: How do you test a custom React hook or Vue composable with Cypress?](#394-how-do-you-test-a-custom-react-hook-or-vue-composable-with-cypress)
- [395: How do you combine coverage from E2E, component and unit tests?](#395-how-do-you-combine-coverage-from-e2e-component-and-unit-tests)
- [396: How do you instrument a Vite app for Cypress coverage?](#396-how-do-you-instrument-a-vite-app-for-cypress-coverage)
- [397: What are the limits of code coverage from E2E tests?](#397-what-are-the-limits-of-code-coverage-from-e2e-tests)
- [398: Can Cypress be used for security testing?](#398-can-cypress-be-used-for-security-testing)
- [399: How do you test for Content Security Policy violations?](#399-how-do-you-test-for-content-security-policy-violations)
- [400: How do you test an app that uses a self-signed certificate or client certificates?](#400-how-do-you-test-an-app-that-uses-a-self-signed-certificate-or-client-certificates)
- [401: How do you run Cypress behind a corporate proxy?](#401-how-do-you-run-cypress-behind-a-corporate-proxy)
- [402: What is the hosts option used for?](#402-what-is-the-hosts-option-used-for)
- [403: Can Cypress test mobile behavior?](#403-can-cypress-test-mobile-behavior)
- [404: How do you test touch gestures like swipe?](#404-how-do-you-test-touch-gestures-like-swipe)
- [405: How do you test what the app does when the user goes offline?](#405-how-do-you-test-what-the-app-does-when-the-user-goes-offline)
- [406: How do you use the Chrome DevTools Protocol from a Cypress test?](#406-how-do-you-use-the-chrome-devtools-protocol-from-a-cypress-test)
- [407: What is cypress-real-events and when do you need it?](#407-what-is-cypress-real-events-and-when-do-you-need-it)
- [408: How does Cypress fit into a test pyramid?](#408-how-does-cypress-fit-into-a-test-pyramid)
- [409: How do you decide if a check belongs in a unit, component or E2E test?](#409-how-do-you-decide-if-a-check-belongs-in-a-unit-component-or-e2e-test)
- [410: How do you test keyboard navigation and focus order?](#410-how-do-you-test-keyboard-navigation-and-focus-order)
- [411: How do you test focus handling in a modal dialog?](#411-how-do-you-test-focus-handling-in-a-modal-dialog)
- [412: How would you structure a large Cypress project?](#412-how-would-you-structure-a-large-cypress-project)
- [413: What is a test data factory and why use one?](#413-what-is-a-test-data-factory-and-why-use-one)
- [414: How do you clean up data created by tests?](#414-how-do-you-clean-up-data-created-by-tests)
- [415: How do you run only the specs affected by a pull request?](#415-how-do-you-run-only-the-specs-affected-by-a-pull-request)
- [416: How do you run E2E tests against preview deployments for each pull request?](#416-how-do-you-run-e2e-tests-against-preview-deployments-for-each-pull-request)
- [417: What is the difference between a smoke suite and a regression suite?](#417-what-is-the-difference-between-a-smoke-suite-and-a-regression-suite)
- [418: How do you check that a new test is not flaky before merging?](#418-how-do-you-check-that-a-new-test-is-not-flaky-before-merging)
- [419: How do you share Cypress setup across many projects?](#419-how-do-you-share-cypress-setup-across-many-projects)
- [420: Does cy.session with cacheAcrossSpecs share sessions between parallel machines?](#420-does-cysession-with-cacheacrossspecs-share-sessions-between-parallel-machines)
- [421: How do you add extra information to failure messages?](#421-how-do-you-add-extra-information-to-failure-messages)
- [422: How do you test your own custom commands?](#422-how-do-you-test-your-own-custom-commands)
- [423: Scenario: your E2E suite takes two hours. What do you do?](#423-scenario-your-e2e-suite-takes-two-hours-what-do-you-do)
- [424: Scenario: tests pass in Chrome but fail in Firefox. How do you approach it?](#424-scenario-tests-pass-in-chrome-but-fail-in-firefox-how-do-you-approach-it)
- [425: Scenario: after a framework upgrade, many tests fail with detached element errors. What do you do?](#425-scenario-after-a-framework-upgrade-many-tests-fail-with-detached-element-errors-what-do-you-do)
- [426: Scenario: logging in takes 10 seconds and every test logs in. How do you fix it?](#426-scenario-logging-in-takes-10-seconds-and-every-test-logs-in-how-do-you-fix-it)
- [427: Scenario: checkout redirects to a third-party domain and back. How do you test it?](#427-scenario-checkout-redirects-to-a-third-party-domain-and-back-how-do-you-test-it)
- [428: Scenario: the frontend calls ten microservices. How do you stub them in a clean way?](#428-scenario-the-frontend-calls-ten-microservices-how-do-you-stub-them-in-a-clean-way)
- [429: Scenario: you need to check the content of an exported Excel or PDF file. How?](#429-scenario-you-need-to-check-the-content-of-an-exported-excel-or-pdf-file-how)
- [430: Scenario: your test needs data from a service owned by another team. What do you do?](#430-scenario-your-test-needs-data-from-a-service-owned-by-another-team-what-do-you-do)
- [431: Scenario: the team uses cy.wait(5000) everywhere. How do you fix it?](#431-scenario-the-team-uses-cywait5000-everywhere-how-do-you-fix-it)
- [432: Scenario: a promo banner appears only for some users and blocks clicks. How do you handle it?](#432-scenario-a-promo-banner-appears-only-for-some-users-and-blocks-clicks-how-do-you-handle-it)
- [433: Scenario: CI runs crash with out of memory errors in one big spec. How do you fix it?](#433-scenario-ci-runs-crash-with-out-of-memory-errors-in-one-big-spec-how-do-you-fix-it)
- [434: Scenario: you must test sign-up with email confirmation from start to end. How?](#434-scenario-you-must-test-sign-up-with-email-confirmation-from-start-to-end-how)
- [435: Scenario: selectors break with every UI redesign. What do you change?](#435-scenario-selectors-break-with-every-ui-redesign-what-do-you-change)
- [436: Scenario: the team starts using cy.prompt and Studio to write tests. What do you watch for?](#436-scenario-the-team-starts-using-cyprompt-and-studio-to-write-tests-what-do-you-watch-for)
- [437: Scenario: you want to upgrade to Cypress 16, but a plugin you need doesn't support it yet. What do you do?](#437-scenario-you-want-to-upgrade-to-cypress-16-but-a-plugin-you-need-doesnt-support-it-yet-what-do-you-do)
- [438: Scenario: after upgrading to Cypress 16, some intercept tests fail in Chrome. Why could that be?](#438-scenario-after-upgrading-to-cypress-16-some-intercept-tests-fail-in-chrome-why-could-that-be)
- [439: Scenario: cy.wait('@alias') sometimes times out with "no request ever occurred". What do you check?](#439-scenario-cywaitalias-sometimes-times-out-with-no-request-ever-occurred-what-do-you-check)
- [440: Scenario: a feature behaves differently around midnight. How do you test it?](#440-scenario-a-feature-behaves-differently-around-midnight-how-do-you-test-it)
- [441: Scenario: tests pass on developers' laptops but fail in CI because CI runs in UTC. What do you do?](#441-scenario-tests-pass-on-developers-laptops-but-fail-in-ci-because-ci-runs-in-utc-what-do-you-do)
- [442: Scenario: a spec passes alone but fails when the whole suite runs. Why?](#442-scenario-a-spec-passes-alone-but-fails-when-the-whole-suite-runs-why)
- [443: Scenario: parallel CI machines overwrite each other's data. How do you fix it?](#443-scenario-parallel-ci-machines-overwrite-each-others-data-how-do-you-fix-it)
- [444: Scenario: Cypress Cloud costs are growing too fast. What can you do?](#444-scenario-cypress-cloud-costs-are-growing-too-fast-what-can-you-do)
- [445: Scenario: you want every test to fail on any console error or 5xx response. How do you set it up?](#445-scenario-you-want-every-test-to-fail-on-any-console-error-or-5xx-response-how-do-you-set-it-up)
- [446: Scenario: you need to test a flow with two users, like an approval process. How?](#446-scenario-you-need-to-test-a-flow-with-two-users-like-an-approval-process-how)
- [447: Scenario: a new team member writes tests that check implementation details. How do you guide them?](#447-scenario-a-new-team-member-writes-tests-that-check-implementation-details-how-do-you-guide-them)
- [448: What makes a good Cypress test?](#448-what-makes-a-good-cypress-test)
- [449: How do you decide what to stub in an E2E test?](#449-how-do-you-decide-what-to-stub-in-an-e2e-test)
- [450: What do you check when reviewing a pull request with Cypress tests?](#450-what-do-you-check-when-reviewing-a-pull-request-with-cypress-tests)

---

# Easy Questions (1-150)

## 1: What is Cypress?

Cypress is a JavaScript testing tool for web applications. It runs your tests inside a real browser, next to your app, so it can see and control the DOM, network requests, timers and storage.

You can use it for end-to-end tests (the whole app in a browser) and for component tests (a single React, Vue, Angular or Svelte component mounted in the browser). Tests are written in JavaScript or TypeScript.

## 2: What types of tests can you write with Cypress?

- **End-to-end (E2E) tests**: open the real app in a browser and go through user flows like sign up, checkout or search.
- **Component tests**: mount one UI component in the browser and test it on its own.
- **API tests**: send HTTP requests with `cy.request()` and check the responses.

People also use Cypress for accessibility checks and visual tests with the help of plugins, but those are add-ons, not core features.

## 3: How is Cypress different from Selenium?

Selenium controls the browser from outside, through the WebDriver protocol. Your test code runs in a separate process and sends commands over the network to the browser.

Cypress runs the test code inside the browser, in the same run loop as your app. Because of that it can:

- Wait for elements and assertions automatically, without explicit waits
- Stub network requests and timers directly
- Show a time travel view of every command

The trade-offs: Cypress supports only JavaScript or TypeScript for tests, has limited multi-tab support, and supports fewer browsers than Selenium.

## 4: How does Cypress run your tests?

When you start Cypress, it launches a Node.js process and a browser. The browser loads the Cypress app, which has two parts: your spec code and your application, loaded in an iframe.

Your test code runs in the browser. Anything that needs Node.js (files, databases, shell commands) is done by sending a message to the Node.js process, for example with `cy.task()`. Cypress also sits between the browser and the network, so it can see and change requests.

## 5: Which browsers does Cypress support?

- Chrome and other Chromium browsers (Chromium, Edge)
- Firefox
- Electron, which ships with Cypress

In Cypress 16, Electron is deprecated as a test browser, so you should pick a real browser with `--browser` or the `defaultBrowser` option. WebKit (Safari's engine) has experimental support through the `experimentalWebKitSupport` option.

## 6: How do you install Cypress?

Install it as a dev dependency with your package manager:

```bash
npm install cypress --save-dev
# or
yarn add cypress --dev
# or
pnpm add -D cypress
```

The npm package downloads the Cypress binary (the app itself) into a global cache folder on install.

## 7: How do you open Cypress for the first time?

```bash
npx cypress open
```

This opens the Cypress app. The first time, it asks if you want E2E or component testing, creates `cypress.config.js`, a `cypress` folder and some example files, then lets you pick a browser and a spec to run.

## 8: What is the difference between cypress open and cypress run?

- `cypress open` starts the interactive app. You pick specs in a UI, see the browser, and tests rerun when you save a file. It is used while writing tests.
- `cypress run` runs all specs from the command line, headless by default, prints results to the terminal and exits. It is used in CI.

```bash
npx cypress open
npx cypress run
```

## 9: What is the default folder structure of a Cypress project?

```
cypress/
  e2e/            # E2E spec files
  fixtures/       # static test data (JSON and others)
  support/
    e2e.js        # runs before every E2E spec
    component.js  # runs before every component spec
    commands.js   # custom commands
  downloads/      # files downloaded during tests
  screenshots/    # created on failures
  videos/         # created if video is turned on
cypress.config.js
```

All of these paths can be changed in the config file.

## 10: What is cypress.config.js?

It is the main configuration file of a Cypress project, placed at the project root. It holds settings like `baseUrl`, timeouts, viewport size, where specs live and Node event handlers.

```js
const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "http://localhost:3000",
    viewportWidth: 1280,
    viewportHeight: 800,
  },
});
```

You can also use `cypress.config.ts`, `cypress.config.mjs` or `cypress.config.cjs`.

## 11: Why do you use defineConfig?

`defineConfig` is a helper that just returns the object you pass in. Its value is in the types: your editor gets autocomplete and type checking for every config option, even in a plain JavaScript file.

```js
import { defineConfig } from "cypress";

export default defineConfig({
  e2e: { baseUrl: "http://localhost:5173" },
});
```

## 12: What is the difference between the e2e and component sections in the config?

Options at the top level apply to both testing types. Options inside `e2e` apply only to E2E tests, and options inside `component` apply only to component tests.

```js
module.exports = defineConfig({
  viewportWidth: 1280,
  e2e: {
    baseUrl: "http://localhost:3000",
  },
  component: {
    devServer: { framework: "react", bundler: "vite" },
  },
});
```

Some options only make sense in one place, for example `baseUrl` for E2E and `devServer` for component tests.

## 13: What is a spec file?

A spec file is a file with tests. Each spec usually covers one page or one feature, like `login.cy.js` or `cart.cy.ts`.

In run mode, Cypress runs spec files one after another. Each spec starts with a fresh page, so specs do not share state.

## 14: What is the default naming pattern for spec files?

For E2E tests the default `specPattern` is `cypress/e2e/**/*.cy.{js,jsx,ts,tsx}`. For component tests it is `**/*.cy.{js,jsx,ts,tsx}`, so component specs usually sit next to the component.

You can change it:

```js
e2e: {
  specPattern: 'tests/e2e/**/*.spec.ts',
}
```

## 15: What libraries does Cypress use for writing tests?

Cypress bundles several libraries so you don't have to install them:

- **Mocha** for the test structure: `describe`, `it`, hooks
- **Chai** for assertions: `expect`, `should`
- **Chai-jQuery** for DOM assertions like `have.class`
- **Sinon** for stubs, spies and fake timers
- **Sinon-Chai** for assertions like `have.been.calledWith`
- **jQuery** and **Lodash**, available as `Cypress.$` and `Cypress._`

## 16: What are describe and it?

They come from Mocha. `describe` groups related tests, and `it` defines a single test.

```js
describe("Login page", () => {
  it("shows an error for a wrong password", () => {
    cy.visit("/login");
    cy.get("[data-cy=email]").type("user@example.com");
    cy.get("[data-cy=password]").type("wrong");
    cy.get("[data-cy=submit]").click();
    cy.contains("Invalid email or password").should("be.visible");
  });
});
```

You can nest `describe` blocks to group tests further.

## 17: What are context and specify?

They are aliases. `context` works the same as `describe`, and `specify` works the same as `it`. Some teams use them because they read better in certain sentences, for example `context('when the user is logged out', ...)`.

## 18: What hooks are available in Cypress tests?

Mocha gives four hooks:

- `before`: runs once before all tests in the block
- `beforeEach`: runs before every test in the block
- `afterEach`: runs after every test in the block
- `after`: runs once after all tests in the block

```js
describe("Todo list", () => {
  beforeEach(() => {
    cy.visit("/todos");
  });

  it("adds a todo", () => {
    cy.get("[data-cy=new-todo]").type("Buy milk{enter}");
    cy.get("[data-cy=todo-item]").should("have.length", 1);
  });
});
```

Cypress recommends doing setup in `beforeEach` and cleaning state before tests, not after them.

## 19: How do you run only one test or skip a test?

Add `.only` to run only that test or block, and `.skip` to skip it.

```js
it.only("runs only this test", () => {});
it.skip("this test is skipped", () => {});
describe.skip("skipped block", () => {});
```

Don't commit `.only` to the main branch. A lint rule from `eslint-plugin-cypress` or `eslint-plugin-mocha` can catch it.

## 20: What is the Command Log?

The Command Log is the panel on the left side of the Cypress app. It lists every command and assertion that ran in a test, in order, with its status.

You can hover or click an entry to see the page as it was at that moment (time travel), and the browser console shows details like the found element or the request and response.

## 21: What is the cy object?

`cy` is the global object you use to call Cypress commands like `cy.visit()`, `cy.get()` and `cy.request()`. Every command you call on it is added to a queue and run later, in order.

There is also the global `Cypress` object (capital C). It holds utilities and settings, like `Cypress.config()`, `Cypress.Commands` and `Cypress.browser`. Those run right away and are not queued.

## 22: How do you open a page with cy.visit?

```js
cy.visit("https://example.com");
cy.visit("/dashboard"); // uses baseUrl
cy.visit("/search", { qs: { q: "shoes" } }); // /search?q=shoes
```

`cy.visit()` waits until the page fires its `load` event. If the page doesn't load within `pageLoadTimeout` (60 seconds by default), or the server returns a non-2xx status, the test fails.

## 23: What is baseUrl and why should you set it?

`baseUrl` is the URL of your app, set in the config. When it is set, `cy.visit()` and `cy.request()` accept relative paths.

```js
e2e: {
  baseUrl: 'http://localhost:3000',
}
```

Benefits:

- You can point tests at another environment just by changing one value
- Cypress loads the app at the right origin from the start, which avoids an extra page reload on the first `cy.visit()`
- When you start `cypress run`, Cypress checks that the server at `baseUrl` is up and warns you if it isn't

## 24: What does cy.get do?

`cy.get()` finds elements by a CSS selector (or an alias). It keeps retrying until the elements are found or the timeout runs out.

```js
cy.get("button");
cy.get(".card .title");
cy.get("[data-cy=save-button]");
cy.get('input[name="email"]');
```

It always searches from the root of the document, even if you chain it after another command. To search inside an element, use `.find()` or `.within()`.

## 25: What does cy.contains do?

`cy.contains()` finds an element by its text. You can also limit it to a selector.

```js
cy.contains("Sign in");
cy.contains("button", "Sign in");
cy.contains(/total: \$\d+/i);
cy.contains("sign in", { matchCase: false });
```

It returns the deepest element that has the text. With a selector, it returns the matching element that contains the text. It is useful when the text is what the user sees and is unlikely to change.

## 26: What is the recommended way to select elements?

Use attributes that exist only for testing, like `data-cy` or `data-test`, because they don't change when someone renames a CSS class or rewrites a text.

```html
<button data-cy="submit-order" class="btn btn-primary">Place order</button>
```

```js
cy.get("[data-cy=submit-order]").click();
```

Avoid selectors based on styling classes, tag order (`div > div:nth-child(3)`) or generated IDs. Selecting by role and accessible name with `cy.getByRole()` or by visible text with `cy.contains()` is also a good choice, since it matches how users find things.

## 27: What is the difference between cy.get and .find?

`cy.get()` always searches the whole document. `.find()` searches only inside the previous subject.

```js
cy.get("[data-cy=user-card]").find(".name"); // .name inside the card
cy.get("[data-cy=user-card]").get(".name"); // .name anywhere on the page
```

The second line is a common mistake. Use `.find()` when you want to stay inside an element.

## 28: What does .within do?

`.within()` runs a group of commands with the previous element as the root. Every `cy.get()` and `cy.contains()` inside the callback searches only inside that element.

```js
cy.get("[data-cy=login-form]").within(() => {
  cy.get("input[name=email]").type("user@example.com");
  cy.get("input[name=password]").type("secret");
  cy.get("button").click();
});
```

This is handy for forms, table rows and modals.

## 29: How do you click an element?

```js
cy.get("[data-cy=save]").click();
cy.get("[data-cy=menu]").rightclick();
cy.get("[data-cy=row]").dblclick();
```

Before clicking, Cypress checks that the element is visible, not disabled, not covered by another element and not moving. It also scrolls the element into view. If any check fails, it keeps retrying until the timeout.

## 30: How do you type into an input?

```js
cy.get("input[name=email]").type("user@example.com");
cy.get("input[name=search]").type("laptop{enter}");
```

`.type()` clicks into the element first, then types one character at a time and fires the keyboard and input events your app would get from a real user.

## 31: How do you type special keys like Enter or Escape?

Use special character sequences in curly braces:

```js
cy.get("input").type("hello{enter}");
cy.get("input").type("{selectall}{backspace}");
cy.get("input").type("{ctrl}a"); // key combination
cy.get("textarea").type("line one{enter}line two");
```

Common ones are `{enter}`, `{esc}`, `{backspace}`, `{del}`, `{selectall}`, `{uparrow}`, `{downarrow}`, `{leftarrow}`, `{rightarrow}`, `{home}`, `{end}`, and the modifiers `{ctrl}`, `{alt}`, `{shift}`, `{meta}`.

## 32: What is cy.press?

`cy.press()` presses a single key on the page, without typing into a specific element. It is useful to test keyboard navigation, like moving focus with Tab or closing a dialog with Escape.

```js
cy.get("input[name=email]").type("user@example.com");
cy.press(Cypress.Keyboard.Keys.TAB);
cy.get("input[name=password]").should("have.focus");
```

It was added in Cypress 14.3. Before that, testing Tab key focus needed a plugin.

## 33: How do you clear an input?

```js
cy.get("input[name=title]").clear();
cy.get("input[name=title]").clear().type("New title");
```

`.clear()` is a shortcut for `.type('{selectall}{del}')`.

## 34: How do you check and uncheck checkboxes and radio buttons?

```js
cy.get("[data-cy=terms]").check();
cy.get("[data-cy=newsletter]").uncheck();
cy.get("[type=radio]").check("express"); // by value
cy.get("[type=checkbox]").check(["red", "blue"]); // several by value
```

To assert the state:

```js
cy.get("[data-cy=terms]").should("be.checked");
```

## 35: How do you choose an option in a select element?

```js
cy.get("select[name=country]").select("Germany"); // by text
cy.get("select[name=country]").select("de"); // by value
cy.get("select[name=country]").select(2); // by index
cy.get("select[name=tags]").select(["js", "css"]); // multi-select
```

Then check the result:

```js
cy.get("select[name=country]").should("have.value", "de");
```

`.select()` only works with native `<select>` elements. Custom dropdowns from UI libraries need clicks on the elements they render.

## 36: How do you upload a file?

Use `.selectFile()` on a file input:

```js
cy.get("input[type=file]").selectFile("cypress/fixtures/avatar.png");
cy.get("input[type=file]").selectFile([
  "cypress/fixtures/a.pdf",
  "cypress/fixtures/b.pdf",
]);
```

To test a drop zone, pass `{ action: 'drag-drop' }`:

```js
cy.get("[data-cy=dropzone]").selectFile("cypress/fixtures/report.csv", {
  action: "drag-drop",
});
```

## 37: How do you double-click or right-click?

```js
cy.get("[data-cy=file-name]").dblclick();
cy.get("[data-cy=file-row]").rightclick();
```

Both fire the same mouse events a browser would fire, so `dblclick` handlers and `contextmenu` handlers in your app will run.

## 38: What does .trigger do?

`.trigger()` fires any DOM event on an element. You use it for events Cypress has no special command for.

```js
cy.get("[data-cy=menu]").trigger("mouseover");
cy.get("[data-cy=slider]").trigger("input");
cy.get("[data-cy=box]").trigger("mousedown", { button: 0 });
```

You can pass event properties like `clientX`, `which` or `key` in the options object.

## 39: How do you focus or blur an element?

```js
cy.get("input[name=email]").focus();
cy.get("input[name=email]").blur();
cy.focused().should("have.attr", "name", "email");
```

`cy.focused()` returns the element that currently has focus. You can also assert with `.should('have.focus')`.

## 40: How do you scroll in Cypress?

```js
cy.get("[data-cy=footer]").scrollIntoView();
cy.scrollTo("bottom");
cy.scrollTo(0, 500);
cy.get("[data-cy=list]").scrollTo("bottom"); // scroll inside an element
```

Most of the time you don't need to scroll yourself, because actions like `.click()` scroll the element into view first. Manual scrolling is useful for lazy loading and infinite scroll.

## 41: What does .should do?

`.should()` adds an assertion to the previous subject. Cypress retries the command before it and the assertion until the assertion passes or the timeout runs out.

```js
cy.get("[data-cy=message]").should("be.visible");
cy.get("[data-cy=message]").should("have.text", "Saved");
cy.get("[data-cy=items] li").should("have.length", 3);
```

This retry is what lets you skip manual waits for things like a request finishing or an animation ending.

## 42: What is .and used for?

`.and()` is the same as `.should()`. It just reads better when you chain several assertions on one subject.

```js
cy.get("[data-cy=submit]")
  .should("be.visible")
  .and("not.be.disabled")
  .and("have.text", "Save");
```

## 43: What are some common assertions you use?

```js
.should('exist')
.should('be.visible')
.should('have.text', 'Hello')        // exact text
.should('contain', 'Hello')          // part of the text
.should('have.value', 'abc')         // input value
.should('have.length', 5)
.should('have.class', 'active')
.should('have.attr', 'href', '/about')
.should('have.css', 'display', 'none')
.should('be.disabled')
.should('be.checked')
.should('have.focus')
```

These come from Chai and Chai-jQuery. You can put `not.` in front of most of them.

## 44: How do you write a negative assertion?

Add `not.` before the assertion:

```js
cy.get("[data-cy=error]").should("not.exist");
cy.get("[data-cy=spinner]").should("not.be.visible");
cy.get("[data-cy=save]").should("not.be.disabled");
cy.get("li").should("not.have.class", "selected");
```

Be careful with negative assertions. A test can pass because the page hasn't loaded yet. It is better to first assert something positive (the page is ready), then assert the negative one.

## 45: What is the difference between should and expect?

`.should()` is chained on a Cypress command and retries. `expect` is the plain Chai BDD style and runs once.

```js
cy.get("[data-cy=total]").should("have.text", "$20");

cy.get("[data-cy=total]").then(($el) => {
  expect($el.text()).to.equal("$20"); // runs once, no retry
});
```

Use `.should()` for things on the page that may still change. Use `expect` inside `.then()` or a `.should()` callback for checks on values you already have.

## 46: What assertion libraries are available in Cypress?

Cypress includes:

- **Chai** for general assertions: `expect(x).to.equal(1)`, `.should('eq', 1)`
- **Chai-jQuery** for DOM: `have.class`, `have.attr`, `be.visible`, `have.css`
- **Sinon-Chai** for stubs and spies: `have.been.called`, `have.been.calledWith`

You can add more Chai plugins with `chai.use()` in a support file.

## 47: What is the default timeout for commands?

`defaultCommandTimeout` is 4000 ms. It is used by commands that query the DOM, like `cy.get()` and `cy.contains()`, and by assertions.

Other timeouts:

- `pageLoadTimeout`: 60000 ms for `cy.visit()` and page loads
- `requestTimeout`: 5000 ms to wait for a request to go out in `cy.wait('@alias')`
- `responseTimeout`: 30000 ms for `cy.request()` and for the response in `cy.wait('@alias')`
- `taskTimeout`: 60000 ms for `cy.task()`

## 48: What is retry-ability in Cypress?

Retry-ability means Cypress keeps running a query and its assertions again and again until the assertions pass or the timeout runs out.

```js
cy.get("[data-cy=todo]").should("have.length", 3);
```

If the list has only 2 items when this runs, Cypress doesn't fail right away. It queries the DOM again and again for up to 4 seconds. This handles slow API responses and re-renders without manual waits.

Only queries (like `get`, `find`, `contains`) and assertions retry. Actions like `.click()` don't run twice.

## 49: Are Cypress commands synchronous?

No. When your test function runs, each `cy.*` call only adds a command to a queue and returns right away. After the test function ends, Cypress runs the queued commands one by one.

```js
it("example", () => {
  console.log("1");
  cy.visit("/");
  cy.get("h1").then(() => console.log("3"));
  console.log("2");
});
// logs 1, 2, 3
```

This is why you can't use the return value of a command like a normal variable.

## 50: Why can't you store the result of cy.get in a variable?

Because `cy.get()` doesn't return the element. It returns a chainable object that refers to a command in the queue, and the command hasn't run yet.

```js
// wrong
const button = cy.get("button");
button.click(); // works by accident, but button is not an element

// right: use the value inside .then()
cy.get("[data-cy=price]").then(($price) => {
  const price = parseFloat($price.text());
  expect(price).to.be.greaterThan(0);
});
```

To use a value later, use `.then()`, an alias with `.as()`, or chain the commands.

## 51: What does .then do?

`.then()` gives you the subject of the previous command as a normal value, so you can work with it in plain JavaScript.

```js
cy.get("[data-cy=username]").then(($el) => {
  const name = $el.text().trim();
  cy.get("[data-cy=greeting]").should("contain", name);
});
```

It does not retry. If you return a value from `.then()`, that value becomes the new subject. If you return nothing, the subject stays the same.

## 52: What does cy.wrap do?

`cy.wrap()` turns any value (an object, a jQuery element, a promise) into a Cypress subject, so you can chain Cypress commands and assertions on it.

```js
cy.wrap({ name: "Ana" }).its("name").should("eq", "Ana");

cy.get("li").then(($items) => {
  cy.wrap($items.first()).click();
});

cy.wrap(fetchToken()).then((token) => {
  // waits for the promise to resolve
});
```

## 53: What are aliases in Cypress?

An alias is a name you give to an element, a value, a route or a stub with `.as()`. You use it later with the `@` prefix.

```js
cy.get("[data-cy=search]").as("searchInput");
cy.get("@searchInput").type("shoes");

cy.intercept("GET", "/api/products*").as("getProducts");
cy.wait("@getProducts");
```

Aliases make tests easier to read and let you refer to the same thing in different places of a test.

## 54: How do you use an alias for an element?

```js
cy.get("[data-cy=cart-count]").as("cartCount");
cy.get("[data-cy=add-to-cart]").click();
cy.get("@cartCount").should("have.text", "1");
```

By default, an element alias stores the query, not the element. When you call `cy.get('@cartCount')`, Cypress runs the query again, so you always get the current element, even if the app re-rendered it.

## 55: Why should you avoid cy.wait with a fixed number?

```js
cy.wait(3000); // avoid
```

A fixed wait makes tests slow when the app is fast, and flaky when the app is slower than the number you picked. Cypress already retries queries and assertions, so most of the time you can wait on something real instead:

```js
cy.get("[data-cy=results]").should("have.length.greaterThan", 0);
cy.wait("@searchRequest");
```

## 56: How do you wait for a network request to finish?

Define an intercept with an alias, then wait on the alias:

```js
cy.intercept("POST", "/api/orders").as("createOrder");
cy.get("[data-cy=place-order]").click();
cy.wait("@createOrder").its("response.statusCode").should("eq", 201);
```

`cy.wait('@alias')` waits for the request to go out and for the response to come back. It also gives you the request and response objects to assert on.

## 57: How do you check the current URL?

```js
cy.url().should("include", "/dashboard");
cy.url().should("eq", "http://localhost:3000/dashboard");

cy.location("pathname").should("eq", "/dashboard");
cy.location("search").should("eq", "?tab=settings");
cy.location().its("hash").should("eq", "#billing");
```

`cy.location()` gives you parts of the URL, which is often cleaner than matching the full URL string.

## 58: How do you check the page title?

```js
cy.title().should("eq", "Dashboard | My App");
cy.title().should("include", "Dashboard");
```

## 59: How do you go back, go forward or reload the page?

```js
cy.go("back");
cy.go("forward");
cy.go(-1);
cy.reload();
cy.reload(true); // reload without cache
```

## 60: How do you change the viewport size?

```js
cy.viewport(375, 667); // width, height
cy.viewport("iphone-x"); // preset
cy.viewport("macbook-15");
cy.viewport("ipad-2", "landscape");
```

The default viewport is 1000 x 660 pixels. You can change it for all tests with `viewportWidth` and `viewportHeight` in the config. Note that this only changes the size of the app frame, not the user agent or touch support.

## 61: What are fixtures?

Fixtures are files with static test data, stored in `cypress/fixtures`. They are usually JSON, but can be any file type.

```js
cy.fixture("user.json").then((user) => {
  cy.get("[data-cy=email]").type(user.email);
});
```

You often use them as stubbed API responses or as input data for forms.

## 62: How do you load a fixture?

```js
cy.fixture("products").then((products) => {
  expect(products).to.have.length(3);
});

cy.fixture("images/logo.png", "base64").then((logo) => {
  // logo is a base64 string
});
```

The `.json` extension can be left out. Cypress looks for `.json`, then other extensions, inside the fixtures folder.

## 63: What is cy.request?

`cy.request()` sends an HTTP request from the Cypress Node process, not from the app. It is useful to call your API directly, for example to log in, seed data or test an endpoint.

```js
cy.request("POST", "/api/login", {
  email: "user@example.com",
  password: "secret",
}).then((response) => {
  expect(response.status).to.eq(200);
  expect(response.body).to.have.property("token");
});
```

Since the request doesn't go through the browser page, there are no CORS limits. Cookies set by the response are saved in the browser.

## 64: What is cy.intercept?

`cy.intercept()` lets you watch, change or fake network requests made by the app.

```js
// watch a request
cy.intercept("GET", "/api/users").as("getUsers");

// fake a response
cy.intercept("GET", "/api/users", {
  statusCode: 200,
  body: [{ id: 1, name: "Ana" }],
}).as("getUsers");
```

It works for `fetch`, `XMLHttpRequest` and other requests the browser makes, like images and scripts. It must be set up before the request happens, usually before `cy.visit()` or before the click that triggers the call.

## 65: How do you stub a response with a fixture file?

```js
cy.intercept("GET", "/api/products", { fixture: "products.json" }).as(
  "getProducts",
);
cy.visit("/products");
cy.wait("@getProducts");
cy.get("[data-cy=product]").should("have.length", 3);
```

This makes the test independent of the backend data, so it is faster and stable.

## 66: What does .its do?

`.its()` gets a property from the subject. It supports nested paths with dots.

```js
cy.wrap({ user: { name: "Ana" } })
  .its("user.name")
  .should("eq", "Ana");
cy.get("li").its("length").should("eq", 5);
cy.window().its("localStorage.token").should("exist");
cy.wait("@login").its("response.body.token").should("be.a", "string");
```

It is a query, so it retries until the property exists and the assertion passes.

## 67: What does .invoke do?

`.invoke()` calls a method on the subject and yields the return value.

```js
cy.get("[data-cy=title]").invoke("text").should("eq", "Welcome");
cy.get("input").invoke("val", "hello"); // jQuery .val('hello')
cy.get("[data-cy=menu]").invoke("show"); // jQuery show()
cy.get("a").invoke("removeAttr", "target");
```

It is a query too, which means the method may be called more than once while Cypress retries. Avoid using it with methods that have side effects you can't repeat.

## 68: How do you pick a specific element from a list?

```js
cy.get("li").first();
cy.get("li").last();
cy.get("li").eq(2); // third item, zero-based
cy.get("li").eq(-1); // last item
```

## 69: How do you move up and down the DOM tree?

Cypress has jQuery-style traversal commands:

```js
cy.get("[data-cy=price]").parent();
cy.get("[data-cy=price]").parents("[data-cy=card]");
cy.get("[data-cy=price]").closest("[data-cy=card]");
cy.get("ul").children("li");
cy.get("[data-cy=active]").siblings();
cy.get("[data-cy=active]").next();
cy.get("[data-cy=active]").prev();
```

`.closest()` is the one you use most: find the nearest parent that matches a selector.

## 70: What do .filter and .not do?

`.filter()` keeps only elements that match a selector. `.not()` removes elements that match it.

```js
cy.get("li").filter(".done").should("have.length", 2);
cy.get("li").not(".done").should("have.length", 3);
cy.get("li").filter(':contains("Milk")').click();
```

## 71: How do you loop over elements?

Use `.each()`:

```js
cy.get("[data-cy=product-price]").each(($price) => {
  const value = parseFloat($price.text().replace("$", ""));
  expect(value).to.be.greaterThan(0);
});
```

You can also run Cypress commands inside the callback, for example `cy.wrap($el).click()`. Inside `.each()`, return `false` to stop the loop early.

## 72: How do you print a message in the Command Log?

```js
cy.log("Creating a new user");
cy.log("Order id", orderId);
```

The message shows up in the Command Log and in the terminal output of some reporters. Unlike `console.log`, it is queued like other commands, so it appears in the right order.

## 73: How do you pause or debug a test?

```js
cy.get("[data-cy=form]").debug(); // pauses in DevTools if open
cy.pause(); // stops the test, you continue with a button
```

`cy.pause()` lets you go through commands one at a time in open mode. `.debug()` triggers a `debugger` statement and logs the subject to the console. Both are ignored in `cypress run`.

## 74: What is time travel in Cypress?

During a test, Cypress takes a DOM snapshot before and after each command. In open mode you can hover over or click a command in the Command Log to see the page as it was at that point.

Some commands, like `.click()`, show a before and after state. This makes it easy to see what the page looked like when something went wrong.

## 75: How do screenshots work in Cypress?

In `cypress run`, Cypress takes a screenshot automatically when a test fails. You can also take one yourself:

```js
cy.screenshot();
cy.screenshot("checkout-page");
cy.get("[data-cy=chart]").screenshot("chart"); // only this element
```

Screenshots are saved in `cypress/screenshots`. You can turn off the automatic screenshot with `screenshotOnRunFailure: false`.

## 76: Does Cypress record videos?

Only if you turn it on. Since Cypress 13, `video` is `false` by default.

```js
module.exports = defineConfig({
  video: true,
});
```

Videos are recorded per spec during `cypress run` and saved in `cypress/videos`. Many teams use Test Replay in Cypress Cloud instead, which records the DOM and network so you can inspect it later.

## 77: How do you run tests headed or headless?

`cypress run` runs headless by default. To watch the browser, pass `--headed`:

```bash
npx cypress run              # headless
npx cypress run --headed     # visible browser
npx cypress run --headless   # explicit
```

`cypress open` always shows the browser.

## 78: How do you run tests in a specific browser?

```bash
npx cypress run --browser chrome
npx cypress run --browser firefox
npx cypress run --browser edge
npx cypress open --e2e --browser chrome
```

You can also give a path to a browser binary. To set a default in the config, use `defaultBrowser`.

## 79: How do you run only some spec files from the command line?

Use `--spec`:

```bash
npx cypress run --spec "cypress/e2e/login.cy.js"
npx cypress run --spec "cypress/e2e/checkout/**/*.cy.js"
npx cypress run --spec "cypress/e2e/a.cy.js,cypress/e2e/b.cy.js"
```

Put globs in quotes so the shell doesn't expand them.

## 80: How do you run a single spec in open mode?

Start `cypress open`, choose the testing type and browser, then click the spec in the specs list. Cypress runs it and reruns it every time you save the spec or a file it imports.

You can also skip the first screens:

```bash
npx cypress open --e2e --browser chrome
```

## 81: What is the support file?

The support file runs before every spec file. By default it is `cypress/support/e2e.js` for E2E and `cypress/support/component.js` for component tests.

You use it for things every spec needs: importing custom commands, global hooks, plugin setup and global event handlers.

```js
// cypress/support/e2e.js
import "./commands";

beforeEach(() => {
  cy.intercept("GET", "/api/analytics/*", { statusCode: 204 });
});
```

## 82: How do you create a custom command?

Use `Cypress.Commands.add()`:

```js
// cypress/support/commands.js
Cypress.Commands.add("login", (email, password) => {
  cy.request("POST", "/api/login", { email, password });
});
```

```js
// in a test
cy.login("user@example.com", "secret");
cy.visit("/dashboard");
```

Custom commands are good for actions you repeat in many specs, like logging in or creating test data.

## 83: Where should you put custom commands?

Put them in `cypress/support/commands.js` (or `.ts`) and import that file in the support file. For a big project, split them into several files by area, like `commands/auth.js` and `commands/cart.js`, and import all of them in the support file.

This way every spec can use them without importing anything.

## 84: Can you write Cypress tests in TypeScript?

Yes. Cypress supports TypeScript out of the box. Name your files `.cy.ts` and, if you want, use `cypress.config.ts`. Cypress compiles them for you.

```ts
describe("Search", () => {
  it("shows results", () => {
    cy.visit("/");
    cy.get("[data-cy=search]").type("laptop{enter}");
    cy.get("[data-cy=result]").should("have.length.greaterThan", 0);
  });
});
```

You only need the `typescript` package installed in your project.

## 85: How do you set up tsconfig for Cypress?

Add a `tsconfig.json` inside the `cypress` folder, so Cypress types don't mix with your app's types (for example, Jest and Cypress both define `expect`).

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM"],
    "types": ["cypress", "node"]
  },
  "include": ["**/*.ts"]
}
```

## 86: How do you work with cookies in Cypress?

```js
cy.setCookie("session_id", "abc123");
cy.getCookie("session_id").should("have.property", "value", "abc123");
cy.getCookies().should("have.length", 1);
cy.clearCookie("session_id");
cy.clearCookies();
cy.clearAllCookies(); // all domains
```

In Cypress 16, `cy.getCookie()`, `cy.getCookies()` and `cy.getAllCookies()` are queries, so the assertions chained after them retry.

## 87: How do you read or set localStorage in a test?

```js
cy.window().then((win) => {
  win.localStorage.setItem("theme", "dark");
});

cy.window().its("localStorage").invoke("getItem", "theme").should("eq", "dark");

cy.getAllLocalStorage().then((storage) => {
  // { 'http://localhost:3000': { theme: 'dark' } }
});

cy.clearLocalStorage("theme");
cy.clearAllLocalStorage();
```

To set values before the app reads them, use the `onBeforeLoad` option of `cy.visit()`.

## 88: What is test isolation?

Test isolation means each test starts from a clean state. With `testIsolation: true` (the default), Cypress clears the page, cookies, localStorage and sessionStorage before every test.

So a test can't depend on what the previous test did. You usually log in or visit the page again in `beforeEach`. To keep login fast, use `cy.session()`.

## 89: How do you access the window and document objects?

```js
cy.window().then((win) => {
  expect(win.innerWidth).to.eq(1000);
});

cy.window()
  .its("appStore")
  .invoke("getState")
  .its("user.name")
  .should("eq", "Ana");

cy.document().its("readyState").should("eq", "complete");
cy.document().its("cookie").should("include", "session");
```

These give you the window and document of the app under test, not of the Cypress runner.

## 90: How do you read and write files in a test?

```js
cy.readFile("cypress/fixtures/user.json").its("name").should("eq", "Ana");
cy.readFile("cypress/downloads/report.csv").should("contain", "Total");

cy.writeFile("cypress/fixtures/temp.json", { id: 1, name: "Test" });
cy.writeFile("logs/run.txt", "done\n", { flag: "a+" }); // append
```

`cy.readFile()` retries until the file exists and assertions pass, so it works well for checking downloads. Paths are relative to the project root.

## 91: What is cy.task?

`cy.task()` runs code in the Node.js process that runs Cypress. You use it for things the browser can't do: talk to a database, read files outside the project, run shell commands or call Node libraries.

```js
// cypress.config.js
setupNodeEvents(on) {
  on('task', {
    resetDb() {
      return db.reset() // must return a value, a promise, or null
    },
  })
}
```

```js
// in a test
cy.task("resetDb");
```

A task must return something other than `undefined`. If there is nothing to return, return `null`.

## 92: What is setupNodeEvents?

`setupNodeEvents` is a function in the config file that runs in Node.js. It is where you register tasks, plugins and handlers for events like `before:browser:launch` or `after:spec`.

```js
module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      on("task", {
        log(message) {
          console.log(message);
          return null;
        },
      });
      return config;
    },
  },
});
```

If you return a changed `config` object, Cypress uses that config for the run.

## 93: How do you read environment variables in a test?

For sensitive values like API keys and passwords, use `cy.env()`. It is a command, so it is used inside the command chain:

```js
cy.env(["apiKey"]).then(({ apiKey }) => {
  cy.request({
    url: "/api/admin",
    headers: { Authorization: `Bearer ${apiKey}` },
  });
});
```

The values come from the `env` block in the config, or from `CYPRESS_*` system environment variables. `cy.env()` returns only the keys you ask for.

## 94: What is Cypress.expose?

`Cypress.expose()` reads and sets public, non-secret values, like an API version or a feature flag name. It is synchronous, so you can call it anywhere.

```js
// cypress.config.js
module.exports = defineConfig({
  expose: {
    apiVersion: 2,
    featureFlag: true,
  },
});
```

```js
Cypress.expose("apiVersion"); // 2
Cypress.expose("featureFlag", false); // set for the rest of this spec
```

From the command line you can pass values with `--expose` (or `-x`): `npx cypress run --expose apiVersion=3`.

## 95: What happened to Cypress.env?

`Cypress.env()` was removed in Cypress 16. The problem with it was that all env values were available in the browser, so your app code, third-party scripts and browser extensions could read secrets.

It was split into two APIs:

- `cy.env()` for secrets, read only when you ask for them, inside the command chain
- `Cypress.expose()` for public values you need to read synchronously

You will still see `Cypress.env('something')` in older projects and blog posts.

## 96: How do you pass environment variables from the system or CI?

Prefix system variables with `CYPRESS_`, and Cypress adds them to the `env` values without the prefix:

```bash
CYPRESS_API_KEY=abc123 npx cypress run
```

```js
cy.env(["API_KEY"]).then(({ API_KEY }) => {
  // 'abc123'
});
```

`CYPRESS_*` variables only fill `env`, not `expose`. Public values are passed with `--expose`.

## 97: How do you override config values from the command line?

Use `--config`:

```bash
npx cypress run --config baseUrl=https://staging.example.com
npx cypress run --config viewportWidth=1280,viewportHeight=800
```

You can also use `CYPRESS_` system variables for config options, for example `CYPRESS_BASE_URL=https://staging.example.com`, or point to a different file with `--config-file`.

## 98: How do you change the timeout of a single command?

Pass a `timeout` option:

```js
cy.get("[data-cy=report]", { timeout: 15000 }).should("be.visible");
cy.wait("@export", { responseTimeout: 60000 });
cy.request({ url: "/api/slow", timeout: 60000 });
```

The timeout set on a query also applies to the assertions chained right after it. This is better than raising `defaultCommandTimeout` for the whole project.

## 99: What is pageLoadTimeout?

It is how long Cypress waits for a page to fire its `load` event, after `cy.visit()`, `cy.reload()`, `cy.go()` or a click that navigates. The default is 60000 ms.

If a page often takes longer because of slow third-party scripts, it is better to block or stub those scripts than to raise the timeout.

## 100: What is actionability?

Before Cypress runs an action like `.click()` or `.type()`, it checks that a real user could do it. The element must:

- Be attached to the DOM
- Be visible
- Not be disabled
- Not be read-only (for typing)
- Not be animating
- Not be covered by another element

Cypress also scrolls it into view. If a check fails, it retries until the timeout, then fails with a message that says which check didn't pass.

## 101: What does force: true do?

`{ force: true }` skips the actionability checks. Cypress fires the events even if the element is hidden, covered or disabled.

```js
cy.get("input[type=file]").selectFile("cypress/fixtures/a.png", {
  force: true,
});
cy.get("[data-cy=hidden-checkbox]").check({ force: true });
```

Use it only when you have a good reason, like a styled checkbox where the real input is hidden. Using it to make a failing test pass can hide a real bug that users would hit.

## 102: What does the error "element is not visible" mean?

It means Cypress found the element but thinks a user can't see it, so it refuses to act on it. Common reasons:

- It has `display: none`, `visibility: hidden` or zero size
- A parent hides it with `overflow: hidden`
- It is outside the viewport inside a container that can't be scrolled

Fix it by doing what a user would do first, like opening the menu that shows the element. Using `force: true` should be the last option.

## 103: What does cy.focused return?

It returns the element that currently has focus on the page.

```js
cy.get("[data-cy=open-dialog]").click();
cy.focused().should("have.attr", "data-cy", "dialog-close");
```

It is useful for testing accessibility rules like moving focus into a modal when it opens.

## 104: How do you check the value of an input?

```js
cy.get("input[name=email]").should("have.value", "user@example.com");
cy.get("input[name=email]").invoke("val").should("include", "@");
```

Don't use `have.text` for inputs. Their value is not part of the text content.

## 105: What is the difference between have.text, contain and cy.contains?

- `have.text` checks that the element's full text is exactly the given string.
- `contain` (or `contain.text`) checks that the text includes the string.
- `cy.contains()` finds an element by its text.

```js
cy.get("h1").should("have.text", "Welcome back, Ana");
cy.get("h1").should("contain", "Welcome back");
cy.contains("h1", "Welcome back");
```

`have.text` is strict about spaces and line breaks, so `contain` is often easier when the HTML has extra whitespace.

## 106: How do you check how many elements are on the page?

```js
cy.get("[data-cy=row]").should("have.length", 10);
cy.get("[data-cy=row]").should("have.length.greaterThan", 0);
cy.get("[data-cy=row]").should("have.length.at.most", 20);
cy.get("[data-cy=row]").its("length").should("be.gte", 5);
```

## 107: What is the difference between not.exist and not.be.visible?

- `not.exist` passes when the element is not in the DOM at all.
- `not.be.visible` passes when the element is in the DOM but hidden.

```js
cy.get("[data-cy=modal]").should("not.exist"); // removed from DOM
cy.get("[data-cy=tooltip]").should("not.be.visible"); // still in DOM, hidden
```

Pick the one that matches how your app hides the element. Since Cypress 6, `not.be.visible` fails if the element is not in the DOM at all, so for removed elements you must use `not.exist`.

## 108: What is Cypress Cloud?

Cypress Cloud is a paid service (with a free tier) from the Cypress team. When you run tests with `--record`, results are sent to Cloud, where you get:

- Test results, screenshots and Test Replay for every run
- Parallel runs across several CI machines with load balancing
- Flaky test detection and analytics
- Integrations with GitHub, GitLab, Slack and Jira

It was called the Cypress Dashboard in older versions.

## 109: What is Cypress Studio?

Cypress Studio lets you create tests by using your app. In open mode you start Studio on a test, click and type in your app, and Cypress writes the matching commands into the spec file. You can also add assertions by right-clicking elements.

It works only for E2E tests. The base Studio doesn't need Cypress Cloud. Studio AI, which suggests assertions, is in beta and needs a Cloud account.

## 110: What is cy.prompt?

`cy.prompt()` takes steps in plain English and uses AI to turn them into Cypress commands at run time.

```js
cy.prompt(
  [
    "visit the login page",
    'type "user@example.com" in the email field',
    "type {{password}} in the password field",
    "click the login button",
    "verify the dashboard heading is visible",
  ],
  {
    placeholders: { password: "secret" },
  },
);
```

It was added in Cypress 15.4 and is in beta. It needs a Cypress Cloud account, works only in E2E tests and only in Chromium-based browsers. Placeholders keep sensitive values out of the AI request. You can also export the generated code and keep it as normal Cypress code.

## 111: What is cy.getByRole?

`cy.getByRole()` finds elements by their ARIA role and accessible name, the same way a screen reader sees them.

```js
cy.getByRole("button", { name: "Save changes" }).click();
cy.getByRole("heading", { name: /order summary/i }).should("be.visible");
cy.getByRole("textbox", { name: "Email" }).type("user@example.com");
```

It was added in Cypress 16.2. Before that, teams used the `@testing-library/cypress` plugin and its `cy.findByRole()` command. Using roles makes tests closer to how users find things and pushes the app to have proper accessibility.

## 112: What is component testing in Cypress?

Component testing mounts a single component (React, Vue, Angular or Svelte) in a real browser, without running the whole app. You can pass props, click and type in it, and check what it renders.

It uses your project's dev server (Vite or webpack) to build the component, so it renders the same way it does in the app. It is faster than E2E tests and gives a more realistic result than tests in a fake DOM like jsdom.

## 113: What is cy.mount?

`cy.mount()` renders a component in the component test page. It is not built in: Cypress adds it to the support file when you set up component testing, using the mount function of your framework.

```js
// cypress/support/component.js
import { mount } from "cypress/react";

Cypress.Commands.add("mount", mount);
```

```jsx
// Button.cy.jsx
import Button from "./Button";

it("renders the label", () => {
  cy.mount(<Button label="Save" />);
  cy.get("button").should("have.text", "Save");
});
```

## 114: Which frameworks does Cypress component testing support?

Officially supported: React, Vue, Angular and Svelte, with Vite or webpack as the bundler. Next.js is supported with some limits (for example, no server components).

Cypress 16 raised the minimums: Angular 21 or newer, Vite 8 or newer, and Next.js 15.0.4 or newer. Other frameworks can be used through community mount adapters.

## 115: What reporter does Cypress use by default?

The default reporter is Mocha's `spec` reporter, which prints each test with a pass or fail mark in the terminal.

You can change it with the `reporter` option, for example to `junit` for CI systems that read JUnit XML, or install a custom one like `mochawesome` for HTML reports.

```js
module.exports = defineConfig({
  reporter: "junit",
  reporterOptions: {
    mochaFile: "results/junit-[hash].xml",
  },
});
```

## 116: Can Cypress test multiple browser tabs?

No. Cypress runs your app inside one tab and can't control a second tab or window. This is a known limit.

To test a link that opens a new tab, you usually check its `href` and `target` attributes, or remove `target="_blank"` and click it so it opens in the same tab.

```js
cy.get("[data-cy=docs-link]")
  .should("have.attr", "target", "_blank")
  .invoke("removeAttr", "target")
  .click();
cy.url().should("include", "/docs");
```

## 117: Can Cypress control two browsers at the same time?

No. A Cypress test controls one browser. If you need to test something like a chat between two users, you can act as one user in the browser and as the other through `cy.request()` or `cy.task()`.

## 118: What are the main limitations of Cypress?

- Tests are written only in JavaScript or TypeScript
- No support for multiple tabs, and only one browser per test
- Cross-origin pages need `cy.origin()`
- Fewer browsers than Selenium (Safari is only through experimental WebKit)
- Free parallel runs need some work; the built-in load balancing needs Cypress Cloud
- Not made for load testing or native mobile apps

## 119: How does Cypress compare to Playwright?

Both are modern tools with auto waiting and good debugging. The main differences:

- Cypress runs tests inside the browser. Playwright controls the browser from Node.js through browser protocols.
- Playwright supports multiple tabs, multiple browser contexts and WebKit out of the box.
- Playwright has free parallel runs built in. Cypress needs Cloud or a custom setup for load balancing.
- Cypress has a strong interactive app with time travel and a large plugin ecosystem.
- Cypress uses a command queue with chained commands. Playwright uses normal `async`/`await`.

## 120: How is Cypress different from Jest?

Jest is a unit test runner that runs in Node.js, usually with a fake DOM (jsdom). Cypress runs in a real browser.

You use Jest for fast tests of functions, hooks and small components. You use Cypress for E2E flows and for component tests where real browser behavior (layout, CSS, focus, real events) matters. Many projects use both.

## 121: How do you turn on test retries?

Use the `retries` option:

```js
module.exports = defineConfig({
  retries: {
    runMode: 2, // cypress run
    openMode: 0, // cypress open
  },
});
```

You can also set it for a single test:

```js
it("loads the report", { retries: 3 }, () => {
  // ...
});
```

Retries hide flaky tests, so you should still fix the root cause.

## 122: What exit code does cypress run return?

It returns the number of failed tests. `0` means all tests passed. If Cypress itself fails to run (for example, a bad config), it exits with `1`.

CI systems use this exit code to mark the job as failed.

## 123: How do you add Cypress scripts to package.json?

```json
{
  "scripts": {
    "cy:open": "cypress open",
    "cy:run": "cypress run",
    "cy:run:chrome": "cypress run --browser chrome",
    "test:component": "cypress run --component"
  }
}
```

Then run `npm run cy:open`. `cypress run` runs E2E tests by default. Use `--component` for component tests.

## 124: How do you check if Cypress is installed correctly?

```bash
npx cypress verify   # checks that the binary works
npx cypress version  # prints package and binary versions
npx cypress info     # prints found browsers, cache path, OS info
```

`cypress info` is helpful when a browser is not found or when you report a bug.

## 125: What is the Cypress binary cache?

When you install the npm package, it downloads the Cypress app (the binary) into a global cache folder, so several projects can share it.

```bash
npx cypress cache path    # show the folder
npx cypress cache list    # show installed versions
npx cypress cache prune   # remove all but the current version
npx cypress cache clear   # remove everything
```

You can change the folder with the `CYPRESS_CACHE_FOLDER` variable, which is common in CI.

## 126: How can you skip downloading the Cypress binary?

Set `CYPRESS_INSTALL_BINARY=0` when you install packages:

```bash
CYPRESS_INSTALL_BINARY=0 npm ci
```

This is useful in CI jobs that don't run Cypress, like a lint or build job, to save time and disk space.

## 127: What system requirements does Cypress have?

- Node.js 22, 24 or 26+ for Cypress 16
- macOS, Windows (64-bit) or Linux (64-bit)
- On Linux, some system libraries like `libgtk`, `libnss3` and `xvfb`

The easiest way to get everything on Linux CI is to use the official Docker images, like `cypress/browsers` or `cypress/included`.

## 128: What are the official Cypress Docker images?

- `cypress/base`: Node.js and the Linux dependencies, no browsers
- `cypress/browsers`: the same plus Chrome, Firefox and Edge
- `cypress/included`: everything plus a specific Cypress version installed

```bash
docker run -it -v $PWD:/e2e -w /e2e cypress/included:16.2.0
```

`cypress/included` runs `cypress run` by default, which makes it simple to run tests without installing anything locally.

## 129: What is eslint-plugin-cypress?

It is an ESLint plugin with rules for Cypress code. It knows the Cypress globals and catches common mistakes, for example:

- `no-unnecessary-waiting`: flags `cy.wait(5000)`
- `no-assigning-return-values`: flags `const btn = cy.get('button')`
- `unsafe-to-chain-command`: flags chaining after actions
- `no-force`: flags `{ force: true }`

```js
// eslint.config.js
import pluginCypress from "eslint-plugin-cypress";

export default [pluginCypress.configs.recommended];
```

## 130: What is Cypress._?

`Cypress._` is the Lodash library, bundled with Cypress. You can use it without installing anything.

```js
const users = Cypress._.times(5, (i) => ({ id: i, name: `User ${i}` }));
const sorted = Cypress._.sortBy(prices);
Cypress._.each(list, (item) => {});
```

It is common for generating test data and for comparing lists.

## 131: What is Cypress.$?

`Cypress.$` is jQuery, bundled with Cypress. Elements yielded by commands like `cy.get()` are jQuery objects, so you can use jQuery methods on them.

```js
cy.get("li").then(($items) => {
  const texts = $items.toArray().map((el) => Cypress.$(el).text());
  expect(texts).to.deep.equal(["a", "b", "c"]);
});
```

Note that `Cypress.$('button')` searches the document right away, with no retry and no waiting. Use `cy.get()` for normal queries.

## 132: How do you check which browser or OS the test runs on?

```js
Cypress.browser.name; // 'chrome', 'firefox', 'edge', 'electron'
Cypress.browser.family; // 'chromium' or 'firefox'
Cypress.browser.isHeadless;
Cypress.platform; // 'darwin', 'win32', 'linux'
Cypress.isBrowser("firefox");
```

You can also limit a test to some browsers:

```js
it("uses the clipboard API", { browser: "chrome" }, () => {});
```

## 133: How do you get information about the current spec or test?

```js
Cypress.spec.name; // 'login.cy.js'
Cypress.spec.relative; // 'cypress/e2e/login.cy.js'
Cypress.currentTest.title; // 'logs in with valid user'
Cypress.currentTest.titlePath;
Cypress.currentRetry; // 0 on the first attempt
Cypress.version; // '16.2.0'
```

This is useful for naming test data or screenshots after the current test.

## 134: What are cy.clock and cy.tick?

`cy.clock()` replaces the app's timers (`setTimeout`, `setInterval`, `Date`) with fake ones. `cy.tick()` moves the fake time forward.

```js
cy.clock();
cy.visit("/session");
cy.tick(30 * 60 * 1000); // 30 minutes
cy.contains("Your session has expired").should("be.visible");
```

This lets you test timeouts, countdowns and dates without waiting in real time.

## 135: What is cy.stub?

`cy.stub()` replaces a function with a fake one that records calls and can return whatever you want. It uses Sinon under the hood.

```js
cy.window().then((win) => {
  cy.stub(win, "confirm").returns(true).as("confirm");
});
cy.get("[data-cy=delete]").click();
cy.get("@confirm").should("have.been.calledOnce");
```

Stubs are removed automatically after each test.

## 136: What is cy.spy?

`cy.spy()` wraps a function so you can see how it was called, but the real function still runs.

```js
cy.visit("/", {
  onBeforeLoad(win) {
    cy.spy(win.console, "error").as("consoleError");
  },
});
cy.get("@consoleError").should("not.have.been.called");
```

## 137: What is the difference between a stub and a spy?

A spy only records calls. The original function still runs as usual.

A stub replaces the function. The original code doesn't run, and you decide what the stub returns or does.

Use a spy when you want to check that something happened. Use a stub when you also need to control the result, for example to skip a real `window.confirm` dialog.

## 138: How do you use a callback function in should?

Pass a function to `.should()`. Cypress retries it until no assertion inside throws, or until the timeout.

```js
cy.get("[data-cy=price]").should(($el) => {
  const price = parseFloat($el.text().replace("$", ""));
  expect(price).to.be.within(10, 100);
});
```

Don't put Cypress commands inside the callback, and don't change anything there, because it can run many times.

## 139: What types of Cypress commands are there?

- **Queries** read state and retry: `cy.get()`, `.find()`, `cy.contains()`, `.its()`, `.invoke()`, `.first()`
- **Assertions** check a subject and retry with the queries before them: `.should()`, `.and()`
- **Actions** change the page, like a user would: `.click()`, `.type()`, `.check()`, `.select()`
- **Other commands** like `cy.visit()`, `cy.request()`, `cy.wait()`, `cy.task()`, `.then()`

Knowing the type tells you if a command retries and if it is safe to chain more commands after it.

## 140: What is a query command?

A query is a command that only reads state and doesn't change anything, like `cy.get()` or `.find()`. Because it has no side effects, Cypress can run it again and again while it waits for the assertions to pass.

When a chain has several queries in a row, Cypress retries the whole chain of queries, not just the last one. That is why `cy.get('ul').find('li').should('have.length', 3)` works even if the `ul` is re-rendered.

## 141: What happens when a test fails in Cypress?

- The test stops at the first failing command or assertion
- Cypress shows the error in the Command Log with the code frame and stack trace
- In run mode, it takes a screenshot (unless turned off)
- `afterEach` and `after` hooks still run
- If retries are set, the test runs again
- The other tests in the spec keep running

If a `before` or `beforeEach` hook fails, Cypress skips the tests that depend on it.

## 142: Can you write a simple first test?

```js
describe("Home page", () => {
  it("shows the main heading and goes to the about page", () => {
    cy.visit("/");
    cy.get("h1").should("contain", "Welcome");
    cy.contains("a", "About").click();
    cy.location("pathname").should("eq", "/about");
    cy.get("h1").should("have.text", "About us");
  });
});
```

It opens the home page, checks the heading, clicks a link and checks that the URL and page changed.

## 143: How should you name and organize spec files?

- Use the `.cy.js` or `.cy.ts` suffix so Cypress finds them
- Group specs by feature or page: `cypress/e2e/auth/login.cy.js`, `cypress/e2e/cart/checkout.cy.js`
- Keep each spec focused on one feature, so it runs fast and failures are easy to find
- Put component specs next to the component: `src/components/Button.cy.jsx`

Smaller specs also work better with parallel runs.

## 144: How do you test a hover effect?

Cypress can't trigger the CSS `:hover` state, because it fires JavaScript events, not real mouse movements from the OS. You have options:

```js
// if your app reacts to mouse events in JavaScript
cy.get("[data-cy=menu]").trigger("mouseover");
cy.get("[data-cy=submenu]").should("be.visible");

// if the submenu is shown only with CSS :hover
cy.get("[data-cy=submenu]").invoke("show");
```

The `cypress-real-events` plugin can trigger a real hover in Chromium browsers with `.realHover()`.

## 145: How do you check that an element has a CSS property?

```js
cy.get("[data-cy=error]").should("have.css", "color", "rgb(220, 38, 38)");
cy.get("[data-cy=sidebar]").should("have.css", "display", "none");
cy.get("[data-cy=card]").should("have.css", "border-radius", "8px");
```

The value is the computed style, so colors come back as `rgb()` and sizes in pixels.

## 146: How do you check an attribute value?

```js
cy.get("a[data-cy=profile]").should("have.attr", "href", "/profile");
cy.get("img").should("have.attr", "alt").and("not.be.empty");
cy.get("button").should("have.attr", "aria-expanded", "true");
```

When you pass only the attribute name, the subject changes to the attribute value, so you can chain more assertions on it.

## 147: How do you check that a button is disabled or enabled?

```js
cy.get("[data-cy=submit]").should("be.disabled");
cy.get("[data-cy=email]").type("user@example.com");
cy.get("[data-cy=submit]").should("be.enabled");
```

For custom buttons that use `aria-disabled` instead of the `disabled` attribute, check the attribute: `.should('have.attr', 'aria-disabled', 'true')`.

## 148: How do you assert on a value you got from a command?

Chain an assertion with `.should()` directly, or use `.then()` and `expect`:

```js
cy.get("[data-cy=count]").invoke("text").then(Number).should("be.gt", 0);

cy.get("[data-cy=count]")
  .invoke("text")
  .then((text) => {
    expect(Number(text)).to.be.gt(0);
  });
```

Both forms check the value once. `.then()` is not a query, so an assertion after it can't make Cypress run `cy.get()` and `.invoke()` again. If the number may still change, put the conversion inside a `.should()` callback, which does retry:

```js
cy.get("[data-cy=count]").should(($el) => {
  expect(Number($el.text())).to.be.gt(0);
});
```

## 149: What is the ElementSelector (Selector Playground)?

It is a tool in the Cypress app that helps you find a selector for an element. You click the crosshair button, then click an element in your app, and Cypress shows a selector and a ready-to-copy `cy.get()` command.

It prefers attributes like `data-cy`, `data-test` and `data-testid`. In Cypress 15 it was renamed from Selector Playground, and its API changed from `Cypress.SelectorPlayground` to `Cypress.ElementSelector`.

## 150: What are the main benefits of Cypress?

- Easy setup: one npm package with everything included
- Automatic waiting and retries, so fewer manual waits
- Time travel, readable errors and DevTools access for debugging
- Network control with `cy.intercept()`
- Both E2E and component testing in one tool
- Good docs and a large plugin ecosystem

It is especially good for front-end developers, since tests are written in the same language as the app and run in the same browser.

# Moderate Questions (151-300)

## 151: How exactly does retry work for a chain of commands?

Cypress retries the chain of queries that comes right before an assertion. Actions and other commands are not retried.

```js
cy.get("[data-cy=list]") // query
  .find("li") // query
  .first() // query
  .should("have.text", "Milk");
```

If the assertion fails, Cypress runs `get`, `find` and `first` again from the start, then checks the assertion again. This continues until it passes or the timeout of the first query runs out.

## 152: Why shouldn't you chain more commands after an action?

Actions like `.click()` and `.type()` can change the page. If the element is re-rendered after the click, the subject the action yields can be an old, detached element.

```js
// risky
cy.get("[data-cy=add]").click().should("have.class", "active");

// better: query again after the action
cy.get("[data-cy=add]").click();
cy.get("[data-cy=add]").should("have.class", "active");
```

The `unsafe-to-chain-command` ESLint rule warns about this. A good habit is to end a chain after an action and start a new one with a query.

## 153: How do you create a custom command that works on a subject?

Use the `prevSubject` option:

```js
Cypress.Commands.add("shouldBeError", { prevSubject: "element" }, (subject) => {
  cy.wrap(subject)
    .should("have.class", "error")
    .and("have.attr", "aria-invalid", "true");
});

cy.get("[data-cy=email]").shouldBeError();
```

`prevSubject` can be:

- `false` (default): a parent command, called as `cy.myCommand()`
- `true`: needs a subject of any type
- `'optional'`: works both ways
- `'element'`, `'document'` or `'window'`: needs a subject of that type

## 154: What is Cypress.Commands.addQuery?

`addQuery` creates a custom query, a command that retries like `cy.get()`. The outer function runs once and sets things up. The inner function it returns runs on every retry and must not have side effects.

```js
Cypress.Commands.addQuery("getByTestId", function (id) {
  return () => Cypress.$(`[data-testid="${id}"]`);
});

cy.getByTestId("cart-total").should("have.text", "$42");
```

Use `addQuery` when your command only reads state. Use `Commands.add` when it changes something, like logging in.

## 155: How do you overwrite an existing command?

Use `Cypress.Commands.overwrite()`. The first argument of your function is the original command.

```js
Cypress.Commands.overwrite("visit", (originalFn, url, options) => {
  cy.log(`Visiting ${url}`);
  return originalFn(url, { ...options, failOnStatusCode: false });
});
```

For query commands like `get`, `contains`, and in Cypress 16 also `getCookie` and `getCookies`, use `Cypress.Commands.overwriteQuery()` instead.

## 156: How do you add TypeScript types for custom commands?

Extend the `Cypress.Chainable` interface in a declaration file:

```ts
// cypress/support/index.d.ts or commands.ts
declare global {
  namespace Cypress {
    interface Chainable {
      login(email: string, password: string): Chainable<void>;
      getByTestId(id: string): Chainable<JQuery<HTMLElement>>;
    }
  }
}

export {};
```

Make sure the file is included by the `tsconfig.json` in the `cypress` folder.

## 157: How do you log in without using the UI in every test?

Log in through the UI in one test that checks the login page. In all other tests, log in through the API with `cy.request()`, which is much faster.

```js
Cypress.Commands.add("loginByApi", (email, password) => {
  cy.request("POST", "/api/auth/login", { email, password });
  // cookies from the response are stored automatically
});

beforeEach(() => {
  cy.loginByApi("user@example.com", "secret");
  cy.visit("/dashboard");
});
```

If your app stores a token in localStorage instead of a cookie, save the token from the response yourself.

## 158: What is cy.session?

`cy.session()` caches the browser state (cookies, localStorage and sessionStorage) after a setup function runs, and restores it in later tests instead of running the setup again.

```js
Cypress.Commands.add("login", (email, password) => {
  cy.session([email], () => {
    cy.visit("/login");
    cy.get("[data-cy=email]").type(email);
    cy.get("[data-cy=password]").type(password, { log: false });
    cy.get("[data-cy=submit]").click();
    cy.location("pathname").should("eq", "/dashboard");
  });
});
```

The first test that calls it runs the login. The next ones restore the saved state, which takes milliseconds. After restoring, the page is blank, so you still need `cy.visit()`.

## 159: What is the validate option of cy.session?

`validate` is a function that checks if a restored session still works. If it fails, Cypress runs the setup again.

```js
cy.session(
  email,
  () => {
    cy.request("POST", "/api/login", { email, password });
  },
  {
    validate() {
      cy.request("/api/me").its("status").should("eq", 200);
    },
  },
);
```

Without it, an expired token on the server would make every later test fail in a confusing way.

## 160: What does cacheAcrossSpecs do in cy.session?

By default, a session is cached only for the current spec file. With `cacheAcrossSpecs: true`, it is shared by all specs in the run.

```js
cy.session("admin", loginAsAdmin, {
  validate: checkAdminSession,
  cacheAcrossSpecs: true,
});
```

This saves even more time in big suites. Use it with `validate`, since a session created early in the run may expire before later specs.

## 161: What happens when you set testIsolation to false?

Cypress stops clearing the page, cookies and storage between tests. Each test continues where the previous one stopped.

```js
describe("Long wizard", { testIsolation: false }, () => {
  it("step 1", () => {});
  it("step 2", () => {}); // starts on the page left by step 1
});
```

It can make some flows faster to write, but tests now depend on order. You can't run one of them alone with `.only`, and a failure in one test breaks the rest. Most teams keep it on and use `cy.session()` for speed.

## 162: How do you match requests in cy.intercept?

You can match by method and URL, or with a route matcher object:

```js
cy.intercept("GET", "/api/users"); // exact path
cy.intercept("/api/users/*"); // glob, any method
cy.intercept(/\/api\/users\/\d+$/); // regex

cy.intercept({
  method: "GET",
  pathname: "/api/products",
  query: { category: "shoes" },
  headers: { "x-tenant": "acme" },
});
```

Glob patterns use minimatch. Note that `/api/users` with a string does not match `/api/users?page=2` unless you use a glob like `/api/users*` or match on `pathname`.

## 163: How do you change request headers with cy.intercept?

Pass a handler function and edit `req.headers`:

```js
cy.intercept("/api/**", (req) => {
  req.headers["x-test-run"] = "true";
  req.headers["authorization"] = "Bearer test-token";
});
```

The request goes to the server with the new headers. This is useful for feature flags, tracing headers or auth in test environments.

## 164: How do you send a dynamic response from an intercept?

Use `req.reply()` inside a handler:

```js
cy.intercept("POST", "/api/todos", (req) => {
  req.reply({
    statusCode: 201,
    body: { id: 99, title: req.body.title, done: false },
  });
});
```

The response is built from the request data, so the app sees its own input reflected back. The request never reaches the server.

## 165: How do you change a real response from the server?

Call `req.continue()` with a callback. The request goes to the server, and you can change the response before the app gets it.

```js
cy.intercept("GET", "/api/user", (req) => {
  req.continue((res) => {
    res.body.plan = "premium";
    res.send();
  });
});
```

This is a mix of real and fake data: the server still runs, but you control one field. You can use `res.send()` with no arguments to send the edited response.

## 166: How do you simulate a network error?

```js
cy.intercept("GET", "/api/products", { forceNetworkError: true }).as(
  "getProducts",
);
cy.visit("/products");
cy.wait("@getProducts");
cy.contains("Could not load products").should("be.visible");
```

To test server errors instead, return a status code:

```js
cy.intercept("GET", "/api/products", {
  statusCode: 500,
  body: { error: "Server error" },
});
```

## 167: How do you simulate a slow network response?

Use `delay` or `throttleKbps` in a static response:

```js
cy.intercept("GET", "/api/report", {
  fixture: "report.json",
  delay: 2000,
}).as("getReport");

cy.visit("/report");
cy.get("[data-cy=spinner]").should("be.visible");
cy.wait("@getReport");
cy.get("[data-cy=spinner]").should("not.exist");
```

For a real response, use `res.setDelay(2000)` or `res.setThrottle(100)` inside `req.continue()` or `req.on('response')`.

## 168: How do you check what the app sent in a request?

Wait on the alias and look at the request object:

```js
cy.intercept("POST", "/api/orders").as("createOrder");
cy.get("[data-cy=place-order]").click();

cy.wait("@createOrder").then(({ request, response }) => {
  expect(request.body).to.deep.include({ productId: 7, quantity: 2 });
  expect(request.headers).to.have.property("authorization");
  expect(response.statusCode).to.eq(201);
});
```

You can also write `cy.wait('@createOrder').its('request.body.quantity').should('eq', 2)`.

## 169: How do you wait for the same request several times?

Every call to `cy.wait('@alias')` waits for the next matching request:

```js
cy.intercept("GET", "/api/search*").as("search");
cy.get("[data-cy=search]").type("lap");
cy.wait("@search");
cy.get("[data-cy=search]").type("top");
cy.wait("@search").its("request.url").should("include", "q=laptop");
```

To wait for several different requests at once, pass an array: `cy.wait(['@getUser', '@getOrders'])`.

## 170: How do you make an intercept match only a limited number of times?

Use the `times` option in the route matcher:

```js
cy.intercept(
  { method: "GET", url: "/api/status", times: 1 },
  { body: { ready: false } },
);
cy.intercept("GET", "/api/status", { body: { ready: true } });
```

The first request gets `ready: false`, and the next ones get `ready: true`. This is good for testing retries, polling or "try again" buttons.

## 171: How do you intercept GraphQL requests?

All GraphQL requests usually go to the same URL, so you match on the operation name in the request body:

```js
cy.intercept("POST", "/graphql", (req) => {
  if (req.body.operationName === "GetUser") {
    req.alias = "getUser";
    req.reply({ data: { user: { id: "1", name: "Ana" } } });
  }
});

cy.visit("/profile");
cy.wait("@getUser");
```

Setting `req.alias` inside the handler gives each operation its own alias.

## 172: In what order are intercepts matched?

When several intercepts match the same request, the one defined last runs first. This lets a test override a default intercept from `beforeEach`.

```js
beforeEach(() => {
  cy.intercept("GET", "/api/user", { fixture: "user.json" });
});

it("shows an error when the user call fails", () => {
  cy.intercept("GET", "/api/user", { statusCode: 500 }); // this one wins
  cy.visit("/");
});
```

Intercepts with `middleware: true` are an exception: they always run first, in the order they were defined, and they don't end the request. They are good for global things like adding headers.

## 173: What is the difference between requestTimeout and responseTimeout in cy.wait?

`cy.wait('@alias')` waits in two steps:

- `requestTimeout` (default 5000 ms): how long to wait for the app to send a matching request
- `responseTimeout` (default 30000 ms): how long to wait for the response after that

```js
cy.wait("@upload", { requestTimeout: 10000, responseTimeout: 120000 });
```

If the error says no request ever went out, the problem is usually a wrong URL pattern or an intercept defined too late.

## 174: Should you stub every network request?

Not always. You can just spy on requests and let them go to the real server:

```js
cy.intercept("GET", "/api/orders").as("getOrders"); // no response given
```

Stubbing gives fast and stable tests and lets you test edge cases like errors. Real requests test the whole system, including the backend. A common approach is a few real E2E tests for main flows and stubbed tests for UI states and edge cases.

## 175: How do you use fixtures with this context in hooks?

Alias the fixture in `beforeEach`, then read it with `this` in tests that use `function` instead of arrow functions:

```js
describe("Profile", () => {
  beforeEach(() => {
    cy.fixture("user").as("user");
  });

  it("shows the user name", function () {
    cy.visit("/profile");
    cy.contains(this.user.name);
  });
});
```

With an arrow function, `this` is not the Mocha context, so `this.user` is undefined. You can also use `cy.get('@user')` with any function type.

## 176: How do aliases work with the this context?

When you call `.as('name')` on a value, Cypress also puts it on the Mocha context, so you can read it as `this.name` in later hooks and the test. Aliases are reset before each test, so values from one test don't leak into the next one.

```js
beforeEach(() => {
  cy.request("/api/settings").its("body").as("settings");
});

it("uses settings", function () {
  expect(this.settings.currency).to.eq("EUR");
});
```

It only works for values that are ready by the time the test function runs, which is the case for values aliased in hooks.

## 177: What is the difference between query aliases and static aliases?

By default, an alias created with `.as()` is a query alias. When you call `cy.get('@name')`, Cypress runs the query chain again, so you get a fresh element.

A static alias stores the value once and returns that same value later:

```js
cy.get("[data-cy=price]").invoke("text").as("oldPrice", { type: "static" });
cy.get("[data-cy=apply-coupon]").click();
cy.get("@oldPrice").then((oldPrice) => {
  cy.get("[data-cy=price]").should("not.have.text", oldPrice);
});
```

Use a static alias when you want to remember a value from an earlier moment.

## 178: Should tests share data with each other?

No. Each test should create the data it needs and should pass when run alone. Sharing data (for example, test 1 creates a user and test 2 uses it) makes tests depend on order, breaks `.only`, breaks retries and makes parallel runs unreliable.

If setup is slow, make it faster with API calls, `cy.task()` for database seeding or `cy.session()`, but keep it in each test or in `beforeEach`.

## 179: How do you seed the database before a test?

There are three common ways:

```js
// 1. Call a test-only API endpoint
cy.request("POST", "/api/test/seed", { users: 3 });

// 2. Use a task that talks to the database from Node
cy.task("db:seed", { users: 3 });

// 3. Run a script through a task
cy.task("runScript", "npm run db:reset");
```

The task approach needs the database to be reachable from the machine running Cypress. Test-only endpoints must be turned off in production.

## 180: Why should you clean state before tests and not after?

If you clean up in `after` or `afterEach`, the cleanup doesn't run when you stop a test in the middle (for example, while debugging in open mode) or when the runner crashes. The next run then starts with dirty data.

Cleaning in `beforeEach` means every test starts from a known state, no matter how the previous run ended. You can also look at the data in the app after a failed test, since nothing deleted it.

## 181: What options does cy.request support?

```js
cy.request({
  method: "POST",
  url: "/api/orders",
  body: { productId: 1 },
  headers: { "x-api-version": "2" },
  qs: { dryRun: true },
  auth: { bearer: "token123" },
  failOnStatusCode: false,
  followRedirect: false,
  timeout: 10000,
  form: false,
});
```

By default, `cy.request()` fails the test for any status code that is not 2xx or 3xx. Set `failOnStatusCode: false` when you want to test error responses.

## 182: How do you test an API with Cypress?

Use `cy.request()` and assert on the response:

```js
describe("Users API", () => {
  it("returns 404 for a missing user", () => {
    cy.request({ url: "/api/users/9999", failOnStatusCode: false }).then(
      (res) => {
        expect(res.status).to.eq(404);
        expect(res.body.error).to.eq("User not found");
      },
    );
  });

  it("creates a user", () => {
    cy.request("POST", "/api/users", { name: "Ana" })
      .its("body")
      .should("include", { name: "Ana" });
  });
});
```

Plugins like `cypress-plugin-api` show request and response details in the app, which makes API tests easier to debug.

## 183: Does cy.request use the browser's cookies?

Yes. `cy.request()` sends the cookies the browser has for that domain, and cookies set by the response are saved in the browser. So you can log in with `cy.request()` and then `cy.visit()` a page as a logged-in user.

It doesn't send headers your app adds itself, like an `Authorization` header from localStorage. You have to add those yourself.

## 184: What is cy.origin?

`cy.origin()` runs commands on a page with a different origin than the one you started on. Cypress needs it because the test code can only run inside one origin at a time.

```js
cy.visit("/login");
cy.get("[data-cy=login-with-provider]").click();

cy.origin("https://auth.example.com", () => {
  cy.get("input[name=username]").type("ana");
  cy.get("input[name=password]").type("secret");
  cy.get("button[type=submit]").click();
});

cy.location("pathname").should("eq", "/dashboard");
```

Since Cypress 14, any other origin (even a subdomain like `auth.myapp.com` vs `app.myapp.com`) needs `cy.origin()`.

## 185: How do you pass values into cy.origin?

The callback runs in a different page, so it can't see variables from the test. Pass them with the `args` option:

```js
const user = { name: "ana", password: "secret" };

cy.origin("https://auth.example.com", { args: user }, ({ name, password }) => {
  cy.get("#username").type(name);
  cy.get("#password").type(password);
});
```

Values must be serializable (plain objects, strings, numbers). Functions and DOM elements can't be passed.

## 186: What is injectDocumentDomain?

Before Cypress 14, Cypress set `document.domain` on pages so it could work across subdomains of the same site. Browsers are removing support for `document.domain`, so Cypress stopped doing it by default in version 14.

`injectDocumentDomain: true` brings back the old behavior. It is deprecated and only meant as a temporary fix while you move to `cy.origin()`.

## 187: What does chromeWebSecurity: false do?

It turns off some web security checks in Chromium browsers, like same-origin rules for iframes, which can let you reach into cross-origin iframes or skip some cross-origin limits.

```js
module.exports = defineConfig({
  chromeWebSecurity: false,
});
```

It works only in Chromium browsers, so tests may behave differently in Firefox. It can also hide real problems, like CORS errors users would get. Prefer `cy.origin()` or stubbing when you can.

## 188: How do you work with iframes?

Get the iframe's body and wrap it:

```js
cy.get("iframe[data-cy=editor]")
  .its("0.contentDocument.body")
  .should("not.be.empty")
  .then(cy.wrap)
  .find("p")
  .type("Hello");
```

This works only for same-origin iframes. The `.should('not.be.empty')` waits until the iframe has loaded. Plugins like `cypress-iframe` wrap this into commands. Cross-origin iframes, like payment forms, can't be reached this way.

## 189: How do you work with Shadow DOM?

Use `.shadow()` to enter a shadow root, or turn on `includeShadowDom` so queries look inside shadow roots automatically:

```js
cy.get("my-date-picker").shadow().find("button.next").click();

cy.get("button.next", { includeShadowDom: true }).click();
```

```js
// for the whole project
module.exports = defineConfig({
  includeShadowDom: true,
});
```

Only open shadow roots can be reached. Closed shadow roots are not accessible from outside by design.

## 190: How do you test a file download?

Click the download button, then read the file from the downloads folder:

```js
cy.get("[data-cy=export-csv]").click();

const file = `${Cypress.config("downloadsFolder")}/orders.csv`;
cy.readFile(file).should("contain", "Order ID,Total");
```

`cy.readFile()` retries until the file exists. The downloads folder is cleared before each run when `trashAssetsBeforeRuns` is on (the default).

## 191: What options does selectFile have?

```js
// file from disk
cy.get("input[type=file]").selectFile("cypress/fixtures/photo.jpg");

// drag and drop onto an element
cy.get("[data-cy=dropzone]").selectFile("cypress/fixtures/photo.jpg", {
  action: "drag-drop",
});

// file made in the test
cy.get("input[type=file]").selectFile({
  contents: Cypress.Buffer.from("name,age\nAna,30"),
  fileName: "people.csv",
  mimeType: "text/csv",
});

// fixture alias
cy.fixture("photo.jpg", null).as("photo");
cy.get("input[type=file]").selectFile("@photo");
```

Pass `null` as the encoding in `cy.fixture()` to get a Buffer for binary files.

## 192: How do you test code that opens a new window with window.open?

Stub `window.open` and check that it was called:

```js
cy.visit("/", {
  onBeforeLoad(win) {
    cy.stub(win, "open").as("windowOpen");
  },
});

cy.get("[data-cy=open-help]").click();
cy.get("@windowOpen").should("have.been.calledWith", "/help", "_blank");
```

Then visit that URL in the same tab if you want to test the page itself.

## 193: How do you handle alert and confirm dialogs?

Cypress accepts alerts and confirms automatically. To check them or change the answer, listen to the events:

```js
cy.on("window:alert", (text) => {
  expect(text).to.eq("Saved!");
});

cy.on("window:confirm", (text) => {
  expect(text).to.eq("Delete this item?");
  return false; // click "Cancel"
});
```

For `window.prompt`, stub it: `cy.window().then((win) => cy.stub(win, 'prompt').returns('my answer'))`.

## 194: How do you handle uncaught exceptions from the app?

By default, an uncaught error in your app fails the test. If the error is expected or comes from a third-party script you can't fix, you can ignore it:

```js
Cypress.on("uncaught:exception", (err) => {
  if (err.message.includes("ResizeObserver loop")) {
    return false; // don't fail the test
  }
});
```

Only ignore specific errors. Returning `false` for every error hides real bugs.

## 195: What is the difference between cy.on and Cypress.on?

- `cy.on()` adds a listener for the current test only. It is removed after the test ends.
- `Cypress.on()` adds a listener for all tests. It is usually put in the support file.

```js
// support file: for every test
Cypress.on("uncaught:exception", handleKnownErrors);

// inside one test
cy.on("window:confirm", () => false);
```

## 196: What Cypress events can you listen to in the browser?

Some useful ones:

- `window:before:load`: before the app's scripts run, good for stubbing
- `window:load`: after the page loaded
- `window:alert`, `window:confirm`: dialogs
- `uncaught:exception`: errors from the app
- `url:changed`: when the URL changes
- `fail`: when a test fails, to add more info or handle the error
- `test:before:run`, `test:after:run`: around each test

```js
Cypress.on("window:before:load", (win) => {
  win.__TEST__ = true;
});
```

## 197: How do you change things in the app before it loads?

Use `onBeforeLoad` in `cy.visit()`. It runs after the window is created but before the app's code runs.

```js
cy.visit("/", {
  onBeforeLoad(win) {
    win.localStorage.setItem("onboardingDone", "true");
    cy.stub(win.navigator.geolocation, "getCurrentPosition").callsFake((cb) => {
      cb({ coords: { latitude: 52.52, longitude: 13.4 } });
    });
  },
});
```

This is the right place to set storage, stub browser APIs or turn on test flags.

## 198: How do you control dates with cy.clock?

Pass a timestamp to freeze `Date` at that moment:

```js
const now = new Date(2026, 0, 15, 10, 0).getTime();
cy.clock(now);
cy.visit("/calendar");
cy.contains("January 2026").should("be.visible");
```

If you only want to fake `Date` and keep real timers, pass the functions to replace: `cy.clock(now, ['Date'])`. To change the time later, use `cy.tick()` or `clock.setSystemTime()`:

```js
cy.clock().then((clock) => {
  clock.setSystemTime(new Date(2026, 5, 1));
});
```

## 199: How do you check stub calls with arguments?

Use Sinon-Chai assertions on the alias:

```js
const onSave = cy.stub().as("onSave");
cy.mount(<Form onSave={onSave} />);
cy.get("input[name=title]").type("Report");
cy.get("button[type=submit]").click();

cy.get("@onSave").should("have.been.calledOnce");
cy.get("@onSave").should("have.been.calledWith", { title: "Report" });
cy.get("@onSave").should("have.been.calledWithMatch", {
  title: Cypress.sinon.match.string,
});
```

`Cypress.sinon.match` helps when you only care about part of the arguments.

## 200: How do you stub a method on an object the app uses?

If the app exposes the object on `window`, you can stub it from the test:

```js
cy.visit("/");
cy.window().then((win) => {
  cy.stub(win.analytics, "track").as("track");
});
cy.get("[data-cy=buy]").click();
cy.get("@track").should("have.been.calledWith", "purchase");
```

For things the app reads during startup, stub them in `onBeforeLoad` instead. Modules imported inside the app bundle can't be stubbed this way in E2E tests, but in component tests you can stub exported objects that the component uses.

## 201: How do you spy on console errors during a test?

```js
beforeEach(() => {
  cy.visit("/", {
    onBeforeLoad(win) {
      cy.spy(win.console, "error").as("consoleError");
    },
  });
});

it("has no console errors on load", () => {
  cy.get("[data-cy=app]").should("be.visible");
  cy.get("@consoleError").should("not.have.been.called");
});
```

Some teams do this in the support file for every test, so any new console error fails the suite.

## 202: How do test retries work in detail?

When a test fails and retries are set, Cypress runs the test again, including its `beforeEach` and `afterEach` hooks. The test passes if any attempt passes. Screenshots are taken for each failed attempt.

```js
module.exports = defineConfig({
  retries: { runMode: 2, openMode: 0 },
});
```

There is also an experimental strategy that runs a test several times to detect flakiness:

```js
retries: {
  experimentalStrategy: 'detect-flake-and-pass-on-threshold',
  experimentalOptions: { maxRetries: 3, passesRequired: 2 },
  openMode: false,
  runMode: true,
}
```

Cypress Cloud marks tests that passed only after a retry as flaky.

## 203: What are the common causes of flaky Cypress tests?

- Fixed waits like `cy.wait(2000)` instead of waiting on real conditions
- Tests that depend on other tests or shared data
- Asserting before the app finished loading or re-rendering
- Chaining after actions on elements that re-render
- Real backend calls to slow or unstable services
- Animations and transitions
- Random data or dates that change between runs
- Not enough CPU or memory in CI

## 204: How do you fix a flaky test?

1. Reproduce it: run the spec many times locally, or look at Test Replay or screenshots from CI.
2. Find what the test waits for, and make it wait on a real signal: an aliased request, an element state or a URL change.
3. Remove dependencies on other tests and on unstable data.
4. Stub third-party services and slow endpoints.
5. Check that you don't act on elements that are re-rendered after the action.

Retries are a safety net, not a fix. Track flaky tests and fix them one by one.

## 205: What is conditional testing and why is it a problem?

Conditional testing means doing different things depending on what the page shows:

```js
// avoid
cy.get("body").then(($body) => {
  if ($body.find("[data-cy=cookie-banner]").length) {
    cy.get("[data-cy=accept-cookies]").click();
  }
});
```

The problem: the page may still be changing. The banner may appear 100 ms after your check, so the test takes a different path each run. The test becomes flaky.

A better way is to control the state, for example by setting the cookie that hides the banner before the visit.

## 206: When is conditional testing acceptable, and how do you do it safely?

Sometimes you don't control the state, for example an A/B test on a shared environment. Then base the condition on something stable that is already settled:

- A value from the server, read with `cy.request()`
- A cookie, URL or flag set before the page loaded
- An element you already waited for, like the page's main container

```js
cy.request("/api/experiments")
  .its("body.newCheckout")
  .then((isNew) => {
    if (isNew) {
      cy.get("[data-cy=new-checkout]").click();
    } else {
      cy.get("[data-cy=old-checkout]").click();
    }
  });
```

## 207: What does the "detached from the DOM" error mean?

It means Cypress had a reference to an element, but the app removed it and rendered a new one in its place, so Cypress can't act on the old one. It is common in React, Vue and Angular apps that re-render.

Since Cypress 12, queries are retried from the start, so most of these errors are gone. They can still happen if you:

- Chain an action after another action on a re-rendered element
- Keep an element from `.then()` and use it later with `cy.wrap()`

The fix is to query the element again right before you use it, and to wait for the re-render (for example, on a request alias) first.

## 208: What does the error "element is being covered by another element" mean?

Cypress checks that the center of the element (or the point you click) is not covered by something else, like a modal overlay, a sticky header, a toast or a loading spinner. If it is, the user couldn't click it either.

Fixes:

- Wait for the overlay or spinner to go away: `cy.get('[data-cy=spinner]').should('not.exist')`
- Close the toast or banner first
- Scroll so a sticky header doesn't cover it, or click another position like `.click('top')`

Only use `force: true` if you are sure a user could still reach the element.

## 209: How does Cypress handle animations?

Before an action, Cypress checks that the element has stopped moving. It compares the element's position over time. The settings are:

- `waitForAnimations` (default `true`): turn the check on or off
- `animationDistanceThreshold` (default `5` pixels): how far an element may move and still count as standing still

Many teams turn off CSS animations in the test environment to make tests faster and more stable:

```js
cy.visit("/", {
  onLoad(win) {
    const style = win.document.createElement("style");
    style.innerHTML =
      "*, *::before, *::after { transition: none !important; animation: none !important; }";
    win.document.head.appendChild(style);
  },
});
```

## 210: What is scrollBehavior?

`scrollBehavior` controls where Cypress scrolls an element before an action. The values are `'top'` (default), `'bottom'`, `'center'`, `'nearest'` or `false` to not scroll.

```js
cy.get("[data-cy=buy]").click({ scrollBehavior: "center" });
```

Using `'center'` often fixes "element is covered" errors caused by sticky headers at the top of the page.

## 211: How do you test a responsive design on several screen sizes?

Loop over the viewports you care about:

```js
const sizes = ["iphone-x", "ipad-2", [1440, 900]];

sizes.forEach((size) => {
  it(`shows the menu correctly on ${size}`, () => {
    if (Array.isArray(size)) {
      cy.viewport(size[0], size[1]);
    } else {
      cy.viewport(size);
    }
    cy.visit("/");
    cy.get("[data-cy=nav]").should("be.visible");
  });
});
```

Remember that `cy.viewport()` doesn't change the user agent or touch support, so mobile-only code based on those won't run.

## 212: How do you write data-driven tests?

Generate tests from an array or a fixture:

```js
const cases = [
  { email: "", error: "Email is required" },
  { email: "abc", error: "Email is invalid" },
  { email: "a@b.co", error: null },
];

describe("Email validation", () => {
  cases.forEach(({ email, error }) => {
    it(`handles "${email}"`, () => {
      cy.visit("/signup");
      if (email) cy.get("[data-cy=email]").type(email);
      cy.get("[data-cy=submit]").click();
      if (error) {
        cy.contains(error).should("be.visible");
      } else {
        cy.get("[data-cy=email-error]").should("not.exist");
      }
    });
  });
});
```

The array must be available when the spec loads. To use a JSON fixture, `import` it at the top of the file instead of `cy.fixture()`.

## 213: How do you use the Page Object Model in Cypress?

Create a class or object per page with selectors and actions, and use it from tests:

```js
// cypress/pages/LoginPage.js
export const loginPage = {
  visit() {
    cy.visit("/login");
  },
  fillEmail(email) {
    cy.get("[data-cy=email]").type(email);
  },
  fillPassword(password) {
    cy.get("[data-cy=password]").type(password, { log: false });
  },
  submit() {
    cy.get("[data-cy=submit]").click();
  },
};
```

```js
loginPage.visit();
loginPage.fillEmail("user@example.com");
loginPage.fillPassword("secret");
loginPage.submit();
```

It keeps selectors in one place. Don't store elements in the page object, only selectors and functions that call Cypress commands.

## 214: What are app actions and how do they compare to page objects?

App actions call your app's code directly instead of going through the UI, for example dispatching a store action that the app exposes on `window` in test mode.

```js
// app code, only in test builds
if (window.Cypress) {
  window.store = store;
}
```

```js
cy.window()
  .its("store")
  .invoke("dispatch", { type: "cart/add", payload: { id: 1 } });
```

They are faster than clicking through the UI and don't break when the UI changes. The downside is that they couple tests to app internals. A common approach is to test each UI flow once through the UI and use app actions or API calls for setup in other tests.

## 215: When should you use a custom command and when a plain function?

Use a custom command when:

- It is used in many specs and you want it on `cy` without imports
- It needs to work in a chain, on a subject

Use a plain function (imported from a helper file) when:

- It is used in only a few places
- It doesn't need to be chained

```js
// helpers.js
export const fillAddress = (address) => {
  cy.get("[data-cy=street]").type(address.street);
  cy.get("[data-cy=city]").type(address.city);
};
```

Plain functions are easier to find with "go to definition" and don't need type declarations.

## 216: How do you run tests against different environments?

The simplest way is to change `baseUrl` from the command line:

```bash
npx cypress run --config baseUrl=https://staging.example.com
```

For more than the URL, you can read an environment name in `setupNodeEvents` and load settings for it:

```js
setupNodeEvents(on, config) {
  const envName = process.env.TEST_ENV || 'local'
  const settings = require(`./cypress/config/${envName}.json`)
  return { ...config, ...settings, env: { ...config.env, ...settings.env } }
}
```

## 217: Can you have more than one config file?

Yes. Use `--config-file` to pick one:

```bash
npx cypress run --config-file cypress.staging.config.js
```

A common pattern is a base config that other files extend:

```js
// cypress.staging.config.js
const { defineConfig } = require("cypress");
const base = require("./cypress.config");

module.exports = defineConfig({
  ...base,
  e2e: { ...base.e2e, baseUrl: "https://staging.example.com" },
});
```

## 218: How do you change the config inside setupNodeEvents?

Change the `config` object and return it:

```js
setupNodeEvents(on, config) {
  if (config.isTextTerminal) {
    // cypress run
    config.defaultCommandTimeout = 10000
  }
  config.env.DB_URL = process.env.DB_URL
  return config
}
```

Whatever you return is used for the run. If you don't return anything, Cypress uses the config as it was.

## 219: How do you change config for one test or one suite?

Pass a config object as the second argument:

```js
describe("Slow reports", { defaultCommandTimeout: 15000 }, () => {
  it("loads the yearly report", { retries: 2 }, () => {
    cy.visit("/reports/yearly");
  });
});
```

The values are only used for that block or test and go back to normal afterwards. In Cypress 16 you can also pass `expose` values here, but not `env`.

## 220: Can you change config while a test runs?

You can read config at any time with `Cypress.config()`, and change some options:

```js
Cypress.config("defaultCommandTimeout", 10000);
Cypress.config("baseUrl"); // read
```

Changes last until the end of the spec file. In Cypress 16, `viewportWidth`, `viewportHeight` and `blockHosts` can no longer be set this way during a test. Use `cy.viewport()` or the test config object instead.

## 221: How do you use a .env file with Cypress?

Load it with `dotenv` in the config file and copy the values you need:

```js
require("dotenv").config();
const { defineConfig } = require("cypress");

module.exports = defineConfig({
  env: {
    ADMIN_PASSWORD: process.env.ADMIN_PASSWORD,
  },
  e2e: {
    baseUrl: process.env.APP_URL,
  },
});
```

```js
cy.env(["ADMIN_PASSWORD"]).then(({ ADMIN_PASSWORD }) => {
  // ...
});
```

Don't commit the `.env` file. In CI, set the values as secret environment variables.

## 222: Why is cy.env asynchronous and what does that change?

`cy.env()` is a command, so it runs in the command queue and you get the values in `.then()`. This keeps secrets out of the browser until a test asks for them.

It means helpers that used to return a secret right away must become commands:

```js
// before (Cypress 15 and older)
const getToken = () => Cypress.env("API_TOKEN");

// after
Cypress.Commands.add("apiRequest", (url) => {
  cy.env(["API_TOKEN"]).then(({ API_TOKEN }) => {
    cy.request({ url, headers: { Authorization: `Bearer ${API_TOKEN}` } });
  });
});
```

`cy.env()` has its own timeout of 4000 ms, which doesn't follow `defaultCommandTimeout`. Pass `{ timeout }` if you need more.

## 223: What Node events can you listen to in setupNodeEvents?

```js
setupNodeEvents(on, config) {
  on('before:run', (details) => {})       // once, before all specs
  on('after:run', (results) => {})        // once, after all specs
  on('before:spec', (spec) => {})         // before each spec
  on('after:spec', (spec, results) => {}) // after each spec
  on('before:browser:launch', (browser, launchOptions) => launchOptions)
  on('after:screenshot', (details) => {})
  on('file:preprocessor', preprocessor)
  on('task', { /* tasks */ })
}
```

`before:run`, `after:run`, `before:spec` and `after:spec` fire in `cypress run`. In open mode they only fire with `experimentalInteractiveRunEvents: true`.

## 224: How do you change browser launch options?

Use the `before:browser:launch` event:

```js
on("before:browser:launch", (browser, launchOptions) => {
  if (browser.family === "chromium" && browser.name !== "electron") {
    launchOptions.args.push("--window-size=1920,1080");
    launchOptions.args.push("--lang=de-DE");
  }
  if (browser.family === "firefox") {
    launchOptions.preferences["intl.accept_languages"] = "de-DE";
  }
  return launchOptions;
});
```

You can also load browser extensions with `launchOptions.extensions.push(pathToExtension)`.

## 225: What is a preprocessor in Cypress?

A preprocessor bundles your spec files before they run in the browser. It handles imports, TypeScript and modern syntax. Cypress uses a webpack preprocessor by default, so it works without setup.

You can replace it, for example with esbuild or Vite, to match your app's build or to make bundling faster:

```js
const createBundler = require('@bahmutov/cypress-esbuild-preprocessor')

setupNodeEvents(on) {
  on('file:preprocessor', createBundler())
}
```

Component tests don't use the preprocessor. They use the dev server from the `devServer` config.

## 226: How do you collect code coverage from Cypress tests?

1. Instrument the app code with Istanbul (for example `babel-plugin-istanbul` or `vite-plugin-istanbul`), only in test builds.
2. Install `@cypress/code-coverage` and register it:

```js
// cypress.config.js
setupNodeEvents(on, config) {
  require('@cypress/code-coverage/task')(on, config)
  return config
}
```

```js
// cypress/support/e2e.js
import "@cypress/code-coverage/support";
```

After the run you get a report in the `coverage` folder. The app must be instrumented, otherwise there is no data to collect.

## 227: How do you generate HTML or JUnit reports?

For JUnit, use the built-in Mocha reporter:

```js
reporter: 'junit',
reporterOptions: {
  mochaFile: 'results/test-results-[hash].xml',
},
```

For HTML, a common choice is `cypress-mochawesome-reporter`, which makes a single HTML report with screenshots. Most report plugins need a small setup in `setupNodeEvents` and the support file.

The `[hash]` in the file name matters, because each spec writes its own file and would overwrite the others.

## 228: How do you use more than one reporter at once?

Use `cypress-multi-reporters`:

```js
reporter: 'cypress-multi-reporters',
reporterOptions: {
  reporterEnabled: 'spec, mocha-junit-reporter',
  mochaJunitReporterReporterOptions: {
    mochaFile: 'results/junit-[hash].xml',
  },
},
```

This prints readable output in the terminal and writes JUnit files for the CI system at the same time.

## 229: How do you run Cypress in CI?

The basic steps are:

1. Install dependencies (with the Cypress binary cache restored)
2. Build and start the app
3. Wait for the app to respond
4. Run `cypress run`
5. Save screenshots, videos and reports as artifacts

`start-server-and-test` handles steps 2 to 4 in one script:

```json
{
  "scripts": {
    "start": "vite preview --port 4173",
    "cy:run": "cypress run",
    "test:e2e": "start-server-and-test start http://localhost:4173 cy:run"
  }
}
```

It starts the server, waits for the URL, runs the tests and stops the server.

## 230: How do you run Cypress with GitHub Actions?

The official action installs dependencies, caches the binary, starts the app and runs the tests:

```yaml
name: E2E
on: [push]
jobs:
  cypress:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: cypress-io/github-action@v7
        with:
          build: npm run build
          start: npm run preview
          wait-on: "http://localhost:4173"
          browser: chrome
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: screenshots
          path: cypress/screenshots
```

## 231: Why and how do you cache the Cypress binary in CI?

The binary is a few hundred MB. Downloading it on every run is slow. Cache the folder where it lives, keyed by the lock file:

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/Cypress
    key: cypress-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
```

You can set a custom location with `CYPRESS_CACHE_FOLDER` to make caching easier on some CI systems. The official GitHub Action and the `cypress/included` Docker image handle this for you.

## 232: How do you run tests in parallel with Cypress Cloud?

Start the same command on several CI machines with `--record` and `--parallel`:

```bash
npx cypress run --record --key $CYPRESS_RECORD_KEY --parallel --ci-build-id $BUILD_ID --group e2e-chrome
```

Cypress Cloud gives each machine the next spec to run, based on how long specs took in earlier runs. The run ends when all specs are done. `--ci-build-id` ties the machines together. Most CI providers are detected automatically, so you often don't need it.

## 233: How can you run tests in parallel without Cypress Cloud?

Split the spec files between CI jobs yourself:

```bash
# job 1
npx cypress run --spec "cypress/e2e/auth/**/*"
# job 2
npx cypress run --spec "cypress/e2e/checkout/**/*"
```

Or use a plugin like `cypress-split`, which spreads specs across jobs from environment variables like `SPLIT` and `SPLIT_INDEX`. There are also third-party dashboards like Currents that give load balancing for Cypress.

Without timing data, splits can be uneven, so one job may take much longer than the others.

## 234: What are --group and --tag used for?

They label runs in Cypress Cloud.

- `--group` names a set of specs inside one run, for example per browser or per test type. You need it when you run the same specs more than once in a single run.
- `--tag` adds labels to the whole run, like `nightly` or `staging`, to filter runs later.

```bash
npx cypress run --record --group firefox --browser firefox --tag nightly,staging
```

## 235: What features does Cypress Cloud offer?

- Run history with errors, screenshots, videos and Test Replay
- Parallel runs with load balancing
- Spec prioritization: run specs that failed last time first
- Auto cancellation: stop a run after a number of failures
- Flake detection and flaky test analytics
- Branch review: compare test results between branches
- Accessibility and UI coverage reports (paid add-ons)
- Integrations with GitHub, GitLab, Bitbucket, Slack, Jira and Microsoft Teams

## 236: What is Test Replay?

Test Replay is a Cypress Cloud feature that records a test run so you can debug it later in the browser, as if you ran it in open mode. You can step through commands, look at the DOM at each step, and see network requests and console logs.

It is much more useful than a video for CI-only failures, because you can inspect elements instead of only watching. It is turned on for recorded runs in supported browsers.

## 237: How do you run only tests with a certain tag?

Cypress has no built-in tags for tests, but the `@cypress/grep` plugin adds them:

```js
it("logs in", { tags: ["@smoke", "@auth"] }, () => {});
```

After setting up the plugin in the support file and config, you pass the tags to run at run time, and only matching tests run. It can also filter specs before they are opened, so specs with no matching tests don't start at all. The exact way to pass options depends on the plugin version, so check its README.

## 238: How do you configure screenshots?

```js
module.exports = defineConfig({
  screenshotOnRunFailure: true,
  screenshotsFolder: "cypress/screenshots",
  trashAssetsBeforeRuns: true,
});
```

```js
cy.screenshot("settings-page", {
  capture: "fullPage", // 'viewport', 'fullPage' or 'runner'
  blackout: ["[data-cy=user-email]"],
  overwrite: true,
});
```

`blackout` hides elements with black boxes, which is useful for personal data and for things that change on every run, like timestamps.

## 239: How do you configure video recording?

```js
module.exports = defineConfig({
  video: true,
  videoCompression: 32, // false or a value from 0 to 51
  videosFolder: "cypress/videos",
});
```

Videos are recorded per spec in `cypress run`. They take extra time and disk space, so many teams keep `video: false` and only upload screenshots, or use Test Replay. You can delete videos of passing specs in an `after:spec` handler to save space.

## 240: How do you do visual regression testing with Cypress?

Cypress has no built-in screenshot comparison. Options:

- Open source plugins like `cypress-image-diff-js` that compare screenshots to saved base images
- Hosted services like Percy, Applitools or Chromatic, which handle storage, review and browser differences

```js
cy.visit("/pricing");
cy.get("[data-cy=pricing-table]").should("be.visible");
cy.percySnapshot("Pricing page");
```

Visual tests are sensitive to fonts, OS and animations, so run them in a fixed environment like Docker, and stub data that changes.

## 241: How do you check accessibility with Cypress?

The most common way is `cypress-axe`, which runs the axe-core engine on the page:

```js
import "cypress-axe"; // in the support file

it("has no accessibility violations", () => {
  cy.visit("/");
  cy.injectAxe();
  cy.checkA11y();
  cy.checkA11y("[data-cy=main-nav]", {
    runOnly: { type: "tag", values: ["wcag2a", "wcag2aa"] },
  });
});
```

Cypress Cloud also has an accessibility add-on that reports issues from your recorded runs without extra test code. Automated checks catch only part of the problems, so manual checks are still needed.

## 242: How do you set up component testing?

Run `npx cypress open`, choose Component Testing, and Cypress detects your framework and bundler. It writes the config for you:

```js
module.exports = defineConfig({
  component: {
    devServer: {
      framework: "react", // 'vue', 'angular', 'svelte', 'next'
      bundler: "vite", // or 'webpack'
    },
  },
});
```

It also creates `cypress/support/component.js` with the `mount` command and `cypress/support/component-index.html`, the page components are mounted into.

## 243: How do you pass props and test events in a React component test?

```jsx
import Counter from "./Counter";

it("calls onChange with the new value", () => {
  const onChange = cy.spy().as("onChange");
  cy.mount(<Counter initial={5} onChange={onChange} />);

  cy.get("[data-cy=increment]").click();
  cy.get("[data-cy=value]").should("have.text", "6");
  cy.get("@onChange").should("have.been.calledWith", 6);
});
```

Spies and stubs passed as props let you check what the component tells its parent.

## 244: How do you mount a component that needs providers?

Wrap the component in a custom mount command:

```jsx
// cypress/support/component.jsx
import { mount } from "cypress/react";
import { MemoryRouter } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

Cypress.Commands.add("mount", (component, options = {}) => {
  const { route = "/", ...mountOptions } = options;
  const queryClient = new QueryClient();
  return mount(
    <QueryClientProvider client={queryClient}>
      <MemoryRouter initialEntries={[route]}>{component}</MemoryRouter>
    </QueryClientProvider>,
    mountOptions,
  );
});
```

Create a new store or client per mount, so tests don't share state.

## 245: How do you write a Vue component test?

```js
import { mount } from "cypress/vue";
import TodoItem from "./TodoItem.vue";

it("emits toggle when clicked", () => {
  const onToggle = cy.spy().as("onToggle");
  mount(TodoItem, {
    props: { title: "Buy milk", done: false, onToggle },
  });

  cy.contains("Buy milk").click();
  cy.get("@onToggle").should("have.been.calledOnce");
});
```

The options object is passed to Vue Test Utils, so you can also give `slots` and `global` plugins like Pinia or the router.

## 246: How do you write an Angular component test?

```ts
import { GreetingComponent } from "./greeting.component";

it("shows the name", () => {
  cy.mount(GreetingComponent, {
    componentProperties: { name: "Ana" },
  });
  cy.contains("Hello, Ana").should("be.visible");
});
```

`cy.mount` comes from `cypress/angular`. You can pass `providers` and `imports` in the options, like in a TestBed setup. Since Cypress 16, the zoneless setup is the default and `zone.js` is no longer needed.

## 247: Can you use cy.intercept in component tests?

Yes. Requests from the component go through the browser, so `cy.intercept()` works the same way as in E2E tests:

```jsx
it("shows users from the API", () => {
  cy.intercept("GET", "/api/users", { fixture: "users.json" }).as("getUsers");
  cy.mount(<UserList />);
  cy.wait("@getUsers");
  cy.get("[data-cy=user]").should("have.length", 3);
});
```

## 248: When should you use component tests and when E2E tests?

Use component tests for:

- All the states of a component: empty, loading, error, many items
- Edge cases of inputs, forms and validation
- Components shared in a design system

Use E2E tests for:

- Important user flows across pages: sign up, checkout, search
- Things that need the real backend, routing and auth together

Component tests are faster and easier to set up for edge cases. E2E tests give more confidence that the whole system works.

## 249: How do Cypress component tests compare to Jest with Testing Library?

Cypress component tests run in a real browser, so CSS, layout, scrolling, focus and real events behave as in the app. You can see the component and debug it with DevTools.

Jest with Testing Library runs in jsdom, which is faster to start and good for logic, but it doesn't do real layout, so things like visibility or element size can't be tested properly.

Many teams use Jest or Vitest for logic and hooks, and Cypress for components where the browser behavior matters.

## 250: How do you load global styles in component tests?

Import them in the component support file, so they apply to every mounted component:

```js
// cypress/support/component.js
import "../../src/styles/global.css";
import { mount } from "cypress/react";

Cypress.Commands.add("mount", mount);
```

You can also add fonts or other `<link>` tags to `cypress/support/component-index.html`. Without global styles, components can look and behave differently than in the app.

## 251: How do you debug a failing test in the Cypress app?

1. Read the error in the Command Log. It shows the failing command, the code frame and often a hint.
2. Click the failing command and the commands before it to see the page at each step (time travel).
3. Open DevTools. Clicking a command prints its details, like the found element or the request and response, to the console.
4. Add `cy.pause()` before the problem and step through commands.
5. Use `.debug()` or a `debugger` statement inside `.then()` to stop with the values in scope.

## 252: How do you use debugger in a Cypress test?

`debugger` must run when the command runs, not when the test function builds the queue. So put it inside `.then()`:

```js
cy.get("[data-cy=cart]").then(($cart) => {
  debugger; // DevTools stops here, $cart is the real element
});
```

If you put `debugger` directly in the test body, it stops before any command ran, and the page is still empty.

## 253: How do you see Cypress's own debug logs?

Set the `DEBUG` environment variable before running Cypress:

```bash
DEBUG=cypress:* npx cypress run
DEBUG=cypress:server:* npx cypress run
DEBUG=cypress:launcher npx cypress open
```

This prints internal logs from the Node process: config loading, browser launch, proxy and plugins. It is useful when Cypress itself fails, for example when a browser doesn't start in CI.

## 254: How do you control typing speed?

`keystrokeDelay` sets the delay between key presses. In Cypress 16 the default is `0`. Before, it was `10` ms.

```js
cy.get("input").type("slow text", { delay: 50 }); // one command

module.exports = defineConfig({ keystrokeDelay: 10 }); // whole project

Cypress.Keyboard.defaults({ keystrokeDelay: 10 }); // in the support file
```

Some apps with debounced search or masked inputs need a delay to behave like with a real user.

## 255: How do you type text that contains curly braces?

By default, text inside `{}` is read as a special key. Turn that off with `parseSpecialCharSequences: false`:

```js
cy.get("[data-cy=code-editor]").type("const a = { b: 1 }", {
  parseSpecialCharSequences: false,
});
```

You can also type `{{}` to get a single `{`.

## 256: How do you type into a contenteditable element?

`.type()` works on elements with `contenteditable`, like rich text editors:

```js
cy.get("[contenteditable=true]").type("Hello world");
cy.get("[contenteditable=true]").type("{selectall}{backspace}New text");
cy.get("[contenteditable=true]").should("have.text", "New text");
```

Some editors (like ones built on ProseMirror or Slate) listen to events Cypress doesn't fully simulate. For those, you may need the editor's own API through `cy.window()` or a plugin like `cypress-real-events`.

## 257: What options does .click accept?

```js
cy.get("[data-cy=canvas]").click("topLeft"); // position
cy.get("[data-cy=canvas]").click(15, 40); // x, y inside the element
cy.get("[data-cy=item]").click({ multiple: true }); // click all matches
cy.get("[data-cy=row]").click({ ctrlKey: true }); // with modifier
cy.get("[data-cy=btn]").click({ force: true });
cy.get("[data-cy=btn]").click({ scrollBehavior: "center" });
```

Positions are `topLeft`, `top`, `topRight`, `left`, `center`, `right`, `bottomLeft`, `bottom` and `bottomRight`.

## 258: How do you test drag and drop?

It depends on how the app implements it.

For libraries that use mouse or pointer events:

```js
cy.get("[data-cy=card-1]")
  .trigger("mousedown", { button: 0 })
  .trigger("mousemove", { clientX: 400, clientY: 200 });
cy.get("[data-cy=column-done]")
  .trigger("mousemove")
  .trigger("mouseup", { force: true });
```

For native HTML5 drag and drop, you need a `DataTransfer` object:

```js
const dataTransfer = new DataTransfer();
cy.get("[data-cy=card-1]").trigger("dragstart", { dataTransfer });
cy.get("[data-cy=column-done]").trigger("drop", { dataTransfer });
```

Plugins like `@4tw/cypress-drag-drop` wrap these steps in a `.drag()` command.

## 259: How do you test a hover menu that opens with JavaScript?

```js
cy.get("[data-cy=account-menu]").trigger("mouseover");
cy.get("[data-cy=account-dropdown]").should("be.visible");
cy.get("[data-cy=logout]").click();
```

If the app uses `mouseenter` or pointer events, trigger those instead. Look at the app's event handlers in DevTools to see which events it listens to.

## 260: How do you test a specific cell in a table?

Find the row by something unique, then look inside it:

```js
cy.contains("tr", "ana@example.com").within(() => {
  cy.get("td").eq(2).should("have.text", "Admin");
  cy.get("[data-cy=edit]").click();
});
```

`cy.contains('tr', text)` gives you the row that has that text, which is more stable than using a row index.

## 261: How do you compare a value before and after an action?

Save the first value, then compare in a later step:

```js
cy.get("[data-cy=cart-count]")
  .invoke("text")
  .then(Number)
  .then((before) => {
    cy.get("[data-cy=add-to-cart]").click();
    cy.get("[data-cy=cart-count]").should("have.text", String(before + 1));
  });
```

The second check uses `.should()`, so it retries until the count updates.

## 262: How do you check that a list is sorted?

Read all values, then compare them with a sorted copy:

```js
cy.get("[data-cy=sort-by-price]").click();

cy.get("[data-cy=price]").should(($prices) => {
  const values = $prices
    .toArray()
    .map((el) => parseFloat(el.innerText.replace("$", "")));
  const sorted = [...values].sort((a, b) => a - b);
  expect(values).to.deep.equal(sorted);
});
```

Using a `.should()` callback means the check retries while the list is still being re-sorted.

## 263: What is the difference between should(callback) and then(callback)?

- `.should(callback)` is retried until no assertion inside it throws. It must not have side effects, and the subject stays the same.
- `.then(callback)` runs once. It can run Cypress commands and change the subject by returning a value.

```js
cy.get("[data-cy=status]").should(($el) => {
  expect($el.text()).to.match(/done/i); // retried
});

cy.get("[data-cy=status]").then(($el) => {
  cy.log($el.text()); // runs once
});
```

## 264: How do you add custom Chai assertions?

Use `chai.use()` in the support file:

```js
// cypress/support/e2e.js
chai.use((_chai) => {
  _chai.Assertion.addMethod("validEmail", function () {
    const value = this._obj;
    this.assert(
      /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(value),
      "expected #{this} to be a valid email",
      "expected #{this} not to be a valid email",
    );
  });
});
```

```js
cy.get("[data-cy=email]").invoke("val").should("be.validEmail");
```

You can also add existing plugins, like `chai-sorted` or `chai-json-schema`, the same way.

## 265: Can you write the Cypress config as an ES module or in TypeScript?

Yes. Cypress supports `cypress.config.js` (CommonJS or ESM, based on your `package.json` `type`), `cypress.config.mjs`, `cypress.config.cjs` and `cypress.config.ts`.

```ts
// cypress.config.ts
import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    baseUrl: "http://localhost:5173",
    setupNodeEvents(on, config) {
      return config;
    },
  },
});
```

## 266: How do you run Cypress in a monorepo?

Each app can have its own Cypress folder and config. Run them with `--project`:

```bash
npx cypress run --project ./apps/web
npx cypress run --project ./apps/admin
```

Install Cypress once at the root to share the binary. Tools like Nx and Turborepo have Cypress targets that run only the affected apps.

## 267: How do you test login with a third-party provider like Google or Auth0?

Options, from best to worst for most teams:

1. Log in through the provider's API with `cy.request()` (many providers have a test or password grant for this), then set the session in the app.
2. Use `cy.origin()` to fill in the provider's login form, only if the provider allows automated logins.
3. In test environments, use a fake identity provider or a bypass that your backend trusts.

Wrap whichever you choose in `cy.session()`. Big providers like Google block automated logins, so testing their real UI is usually not possible or allowed.

## 268: How do you test an email flow, like a password reset?

Send emails to a test inbox that has an API, then read the email in a task:

```js
// cypress.config.js
on("task", {
  async getLastEmail(to) {
    const res = await fetch(
      `http://localhost:8025/api/v2/search?kind=to&query=${to}`,
    );
    const data = await res.json();
    return data.items[0] ?? null;
  },
});
```

```js
cy.get("[data-cy=forgot-password]").click();
cy.get("[data-cy=email]").type("ana@test.local{enter}");
cy.task("getLastEmail", "ana@test.local").then((email) => {
  const link = email.Content.Body.match(/https?:\/\/\S+reset\S+/)[0];
  cy.visit(link);
});
```

Local tools like Mailpit or MailHog, or services like Mailosaur, work well for this.

## 269: How do you wait for a loading spinner to go away?

Assert that it's gone before you continue:

```js
cy.visit("/orders");
cy.get("[data-cy=spinner]").should("not.exist");
cy.get("[data-cy=order]").should("have.length.greaterThan", 0);
```

Even better is to wait for the data itself (the second line) or the request alias. A spinner check alone can pass too early if the spinner hasn't appeared yet.

## 270: How do you know the page is ready before testing it?

Wait for something that only appears when the page is ready, not for time:

```js
cy.intercept("GET", "/api/dashboard").as("dashboard");
cy.visit("/dashboard");
cy.wait("@dashboard");
cy.get("[data-cy=dashboard-ready]").should("exist");
```

Some teams add a `data-ready="true"` attribute to the root element when the app finished its first load, so tests have one clear signal to wait for.

## 271: How do you clear all browser state manually?

```js
cy.clearAllCookies();
cy.clearAllLocalStorage();
cy.clearAllSessionStorage();
```

The `All` versions clear every domain, not just the current one. With test isolation turned on, Cypress already does this before each test, so you mostly need these when isolation is off or in the middle of a test.

## 272: What changed for cookie commands in Cypress 16?

`cy.getCookie()`, `cy.getCookies()`, `cy.getAllCookies()`, `cy.getAllLocalStorage()` and `cy.getAllSessionStorage()` became queries. Assertions chained after them now retry, and their timeout follows `defaultCommandTimeout`.

```js
// now retries until the cookie appears
cy.getCookie("session").should("exist");

// this still runs only once
cy.getCookie("session").then((cookie) => {
  expect(cookie).to.exist;
});
```

So chain `.should()` directly. If you overwrite one of these commands, use `Cypress.Commands.overwriteQuery()`.

## 273: How do you run a shell command now that cy.exec is removed?

Use a task with `execFileSync` or `execSync` from Node:

```js
// cypress.config.js
const { execFileSync } = require('node:child_process')

setupNodeEvents(on) {
  on('task', {
    runScript({ file, args = [] }) {
      const stdout = execFileSync(file, args, { encoding: 'utf8' })
      return { stdout }
    },
  })
}
```

```js
cy.task("runScript", { file: "npm", args: ["run", "db:seed"] })
  .its("stdout")
  .should("contain", "Seeded");
```

`execFileSync` with an array of arguments doesn't use a shell, which avoids injection problems. Remove `execTimeout` from your config and use `taskTimeout` if you need more time.

## 274: Can you import Node modules like fs in a spec file?

No. Spec files run in the browser, so Node-only modules like `fs`, `child_process` or a database driver won't work there. Put that code in a task in `setupNodeEvents` and call it with `cy.task()`.

Libraries that work in browsers, like `dayjs` or `@faker-js/faker`, can be imported in specs as usual.

## 275: How do you generate random test data?

Use a library like `@faker-js/faker`:

```js
import { faker } from "@faker-js/faker";

it("signs up a new user", () => {
  const user = {
    name: faker.person.fullName(),
    email: faker.internet.email(),
    password: faker.internet.password({ length: 12 }),
  };
  cy.visit("/signup");
  cy.get("[data-cy=name]").type(user.name);
  cy.get("[data-cy=email]").type(user.email);
  cy.get("[data-cy=password]").type(user.password, { log: false });
  cy.get("[data-cy=submit]").click();
});
```

Unique emails help tests run in parallel without conflicts. If a test fails, log the data so you can reproduce it, or set a fixed seed with `faker.seed()`.

## 276: What are some popular Cypress plugins?

- `@cypress/grep`: run tests by tag or title
- `@cypress/code-coverage`: code coverage
- `cypress-axe`: accessibility checks
- `cypress-real-events`: real hover, key presses and touch in Chromium
- `@testing-library/cypress`: Testing Library queries
- `cypress-split`: split specs across CI machines without Cloud
- `cypress-recurse`: retry any sequence of commands
- `cypress-mochawesome-reporter`: HTML reports
- `cypress-plugin-api`: show API request details in the app

## 277: How do you test time zones and locales?

The browser takes its time zone from the `TZ` environment variable of the process on most systems:

```bash
TZ=America/New_York npx cypress run
```

For the language, you can change browser launch arguments or preferences in `before:browser:launch` (for example `--lang=de-DE` in Chromium) and set the `Accept-Language` header with an intercept if the server uses it.

## 278: How do you fake the user's location?

Stub the geolocation API before the app loads:

```js
cy.visit("/stores", {
  onBeforeLoad(win) {
    cy.stub(win.navigator.geolocation, "getCurrentPosition").callsFake(
      (success) => {
        success({
          coords: { latitude: 48.8566, longitude: 2.3522, accuracy: 10 },
        });
      },
    );
  },
});
cy.contains("Stores near Paris").should("be.visible");
```

To test the "permission denied" path, call the error callback instead.

## 279: Should you stub window.fetch or use cy.intercept?

Use `cy.intercept()`. It works at the network level, so it catches `fetch`, `XMLHttpRequest`, requests from libraries and images, without knowing how the app makes the call.

Stubbing `window.fetch` only works for code that calls `fetch` on that window, and it skips real response parsing. It was a workaround in old Cypress versions before network stubbing supported `fetch`.

## 280: How do you test WebSockets in Cypress?

`cy.intercept()` doesn't handle WebSocket messages. Options:

- Test the UI against a real WebSocket server in the test environment, and trigger events from the server side with `cy.task()` or `cy.request()`
- Stub the app's socket client through `window` in test builds
- Use a plugin that mocks WebSocket in the browser, like `cypress-mock-websocket` or Mock Socket

```js
cy.visit("/chat");
cy.task("sendChatMessage", { from: "bot", text: "Hello" });
cy.contains("[data-cy=message]", "Hello").should("be.visible");
```

## 281: How do you test a redirect?

In the browser, just check where you end up:

```js
cy.visit("/old-pricing");
cy.location("pathname").should("eq", "/pricing");
```

To check the redirect response itself, use `cy.request()` without following it:

```js
cy.request({ url: "/old-pricing", followRedirect: false }).then((res) => {
  expect(res.status).to.eq(301);
  expect(res.redirectedToUrl).to.include("/pricing");
});
```

## 282: How do you visit a page protected with basic auth?

```js
cy.visit("https://staging.example.com", {
  auth: { username: "staging", password: "secret" },
});
```

Cypress sends the credentials with the request, so the browser's login popup doesn't appear. You can also put them in the URL, but that is easy to leak in logs.

## 283: How do you visit a page that returns an error status?

`cy.visit()` fails on 4xx and 5xx responses by default. To test your error pages, turn that off:

```js
cy.visit("/this-page-does-not-exist", { failOnStatusCode: false });
cy.contains("Page not found").should("be.visible");
```

## 284: How do you test how the UI handles different server responses?

Use one test per response, with an intercept for each:

```js
const cases = [
  { status: 401, message: "Please log in again" },
  { status: 403, message: "You do not have access" },
  { status: 500, message: "Something went wrong" },
];

cases.forEach(({ status, message }) => {
  it(`shows a message for ${status}`, () => {
    cy.intercept("GET", "/api/orders", { statusCode: status }).as("orders");
    cy.visit("/orders");
    cy.wait("@orders");
    cy.contains(message).should("be.visible");
  });
});
```

## 285: Should you use cy.getByRole, data-cy attributes or Testing Library?

All three are good. A simple rule:

- Use `cy.getByRole()` for elements with a clear role and name, like buttons, links, headings and form fields. It also checks accessibility a little.
- Use `data-cy` for elements without a good role or name, like a container, a chart or a list item.
- `@testing-library/cypress` gives `findByRole`, `findByLabelText` and others. Teams that already use Testing Library in unit tests often like it. With `cy.getByRole()` built in since 16.2, you may not need the plugin just for roles.

Pick one main style per project, so tests look the same.

## 286: How do you use Testing Library with Cypress?

```bash
npm install --save-dev @testing-library/cypress
```

```js
// cypress/support/e2e.js
import "@testing-library/cypress/add-commands";
```

```js
cy.findByRole("button", { name: /save/i }).click();
cy.findByLabelText("Email").type("ana@example.com");
cy.findByText("Profile saved").should("be.visible");
cy.findAllByRole("listitem").should("have.length", 3);
```

The `findBy` commands retry like Cypress queries.

## 287: How do you use Cypress Studio in practice?

1. Open the app with `cypress open` and run a spec.
2. Click the Studio button on a test, or create a new test with Studio.
3. Use your app: Cypress records clicks, typing and selects as commands.
4. Right-click an element to add an assertion, like "be visible" or "have text".
5. Save. Cypress writes the commands into the spec file.

Studio is a good start, but review the code it writes: rename selectors if needed, remove extra steps and add waits on aliases where your app makes requests.

## 288: How does cy.prompt handle sensitive data and changes in the app?

Use `placeholders` for values that must not be sent to the AI service, like passwords. You write `{{name}}` in the step and pass the real value in the options. The AI only sees the placeholder.

```js
cy.env(["ADMIN_PASSWORD"]).then(({ ADMIN_PASSWORD }) => {
  cy.prompt(["type {{password}} into the password field"], {
    placeholders: { password: ADMIN_PASSWORD },
  });
});
```

Generated commands are cached, so the AI isn't called on every run. If the app changes and the cached commands no longer work, Cypress can generate them again. Many teams use `cy.prompt()` to draft tests and then save the generated code as normal Cypress commands.

## 289: How do you exclude some files from running as specs?

Use `excludeSpecPattern`:

```js
e2e: {
  specPattern: 'cypress/e2e/**/*.cy.{js,ts}',
  excludeSpecPattern: ['**/examples/*', '**/__snapshots__/*'],
}
```

The default is `*.hot-update.js`. This is useful for example specs from the scaffold or shared helper files that match the spec pattern.

## 290: What do watchForFileChanges and numTestsKeptInMemory do?

- `watchForFileChanges` (default `true`): in open mode, Cypress reruns the spec when you save a spec or a file it imports. Turn it off if reruns on every save are annoying.
- `numTestsKeptInMemory` (default `50`): how many tests keep their snapshots and command data for time travel in open mode. Lower it if the browser uses too much memory in long specs.

## 291: How do you run all specs at once in open mode?

Turn on `experimentalRunAllSpecs`:

```js
e2e: {
  experimentalRunAllSpecs: true,
}
```

A "Run all specs" button appears in the specs list. Cypress then runs them all in one browser tab, one after the other. It is handy for quick checks, but `cypress run` is still closer to CI behavior, where each spec starts fresh.

## 292: How do you test a form validation message from the browser?

Native HTML validation (`required`, `type="email"`) shows browser popups that Cypress can't see in the DOM. Check the element's validity instead:

```js
cy.get("[data-cy=submit]").click();
cy.get("input[name=email]").then(($input) => {
  expect($input[0].checkValidity()).to.be.false;
  expect($input[0].validationMessage).to.not.be.empty;
});
cy.get("input[name=email]:invalid").should("have.length", 1);
```

The exact message depends on the browser and its language, so avoid matching the full text.

## 293: How do you test a page that polls the server?

Use `times` to return different responses, then wait for the final state:

```js
cy.intercept(
  { method: "GET", url: "/api/job/42", times: 2 },
  { body: { status: "running" } },
);
cy.intercept("GET", "/api/job/42", { body: { status: "done" } }).as("jobDone");

cy.visit("/jobs/42");
cy.wait("@jobDone");
cy.contains("Job finished").should("be.visible");
```

If the app polls every 5 seconds, use `cy.clock()` and `cy.tick()` so the test doesn't wait in real time.

## 294: How do you test infinite scroll?

Scroll to the bottom and check that more items load:

```js
cy.intercept("GET", "/api/posts?page=2*").as("page2");
cy.visit("/feed");
cy.get("[data-cy=post]").should("have.length", 20);
cy.scrollTo("bottom");
cy.wait("@page2");
cy.get("[data-cy=post]").should("have.length", 40);
```

If the list scrolls inside a container, call `.scrollTo('bottom')` on that element.

## 295: How do you check that something was copied to the clipboard?

Stub the clipboard API and check the call:

```js
cy.visit("/share", {
  onBeforeLoad(win) {
    cy.stub(win.navigator.clipboard, "writeText").resolves().as("copy");
  },
});
cy.get("[data-cy=copy-link]").click();
cy.get("@copy").should("have.been.calledWithMatch", /\/share\/\w+/);
```

Reading the real clipboard needs permissions, which is hard to set up in CI, so stubbing is more reliable.

## 296: How do you test print or other browser features that open native dialogs?

Cypress can't control native browser dialogs like print, file pickers or permission prompts. Stub the API that opens them:

```js
cy.window().then((win) => {
  cy.stub(win, "print").as("print");
});
cy.get("[data-cy=print-invoice]").click();
cy.get("@print").should("have.been.calledOnce");
```

For file pickers, use `.selectFile()` on the input instead of clicking the button that opens the picker.

## 297: How do you check that no request was made?

Count the calls on an intercept alias after the action:

```js
cy.intercept("POST", "/api/subscribe", cy.spy().as("subscribe"));
cy.get("[data-cy=email]").type("not-an-email");
cy.get("[data-cy=submit]").click();
cy.contains("Email is invalid").should("be.visible");
cy.get("@subscribe").should("not.have.been.called");
```

Passing a spy as the handler records each matching request without changing it.

## 298: How do you count how many times a request was made?

Use `@alias.all` to get all matched calls:

```js
cy.intercept("GET", "/api/notifications").as("notifications");
cy.visit("/");
cy.get("[data-cy=refresh]").click();
cy.get("@notifications.all").should("have.length", 2);
```

This is useful to catch duplicate requests, for example from a component that fetches data twice.

## 299: How do you block third-party scripts during tests?

Use `blockHosts` to make requests to some hosts fail fast:

```js
module.exports = defineConfig({
  blockHosts: ["*.google-analytics.com", "*.hotjar.com", "cdn.segment.com"],
});
```

Or stub them with an intercept to return an empty response:

```js
cy.intercept("https://www.googletagmanager.com/**", { statusCode: 204 });
```

This makes tests faster, avoids polluting analytics with test traffic and removes a source of flakiness.

## 300: How do you test a feature behind a feature flag?

Control the flag in the test instead of depending on the environment:

```js
cy.intercept("GET", "/api/flags", {
  body: { newCheckout: true, darkMode: false },
}).as("flags");
cy.visit("/checkout");
cy.wait("@flags");
cy.get("[data-cy=new-checkout]").should("be.visible");
```

For flag services with SDKs (like LaunchDarkly), stub their network calls the same way or use their test or local mode. Test both the on and off states of a flag that is still being rolled out.

# Advanced Questions (301-450)

## 301: What is the architecture of Cypress?

Cypress has two main parts:

- **A Node.js server** that loads the config, runs `setupNodeEvents`, bundles specs, launches the browser, handles tasks, files and screenshots, and talks to Cypress Cloud.
- **The browser**, where the Cypress app runs. Your spec code and the app under test both run in the same browser tab, in separate iframes.

The two talk over a WebSocket connection. Cypress also uses browser automation APIs (Chrome DevTools Protocol for Chromium, WebDriver BiDi for Firefox) for things the page can't do itself, like cookies, screenshots and network control.

## 302: Why does Cypress run the app inside an iframe?

The Cypress app page contains the Command Log and an iframe with your application. Running the spec in the same tab lets Cypress reach directly into the app's `window` and `document`: it can read the DOM, call functions, stub objects and fire events synchronously.

The cost is that the app runs inside a frame. Some apps check `window.top !== window.self` to block framing. Cypress changes such code on the fly with the `modifyObstructiveCode` option, which is on by default.

## 303: How does Cypress intercept network traffic?

In older versions, all browser traffic went through a proxy inside the Cypress Node server, which could see and change every request and response.

Since Cypress 16, Chrome, Chromium and Edge intercept traffic on the browser's own network layer, using the browser's automation protocol. This is closer to real browser behavior: HTTP/2 works as in production, and some details changed, like `req.httpVersion` no longer being reported and compression headers missing on intercepted responses.

The `forceHttp1` option brings back the old proxy path for Chromium. It is deprecated and only meant to buy time while you update tests.

## 304: How does the command queue work internally?

When a test function runs, each `cy.*` call creates a command object and adds it to a queue, then returns a chainer. Nothing is executed yet.

After the test function returns, Cypress runs the queue one command at a time. Each command:

1. Gets the subject from the previous command
2. Runs (queries retry until their assertions pass)
3. Passes its result as the subject to the next command

Commands added inside `.then()` or a custom command are inserted right after the current command, so the order stays correct.

## 305: Why does mixing async/await with Cypress commands not work?

Cypress commands are not promises. They return chainers, and they run later from the queue. If you `await` a chainer, you don't get the subject, and the order of your code and the queue get mixed up.

```js
// doesn't work as expected
it("test", async () => {
  const el = await cy.get("h1"); // not the element
});
```

Write tests in the chained style, and use `.then()` when you need a value. Inside a `.then()`, you can still use normal `async` functions that don't call Cypress commands.

## 306: Can you return a promise from .then()?

Yes. If a `.then()` callback returns a promise, Cypress waits for it to resolve and uses the result as the new subject.

```js
cy.wrap(null)
  .then(() => {
    return fetch("/api/health").then((res) => res.json());
  })
  .should("have.property", "ok", true);
```

But you can't mix the two: if a `.then()` callback both calls Cypress commands and returns a different promise, Cypress throws an error. Either queue commands or return a promise.

## 307: How does Cypress know when a command is done?

Each command decides when it is done:

- Queries resolve when the value they found makes the next assertions pass
- `cy.visit()` waits for the `load` event
- Actions like `.click()` are done after the events are fired, and then Cypress also waits for a page load if the action started one
- `cy.wait('@alias')` resolves when the matching response arrives
- `cy.task()` and `cy.request()` wait for the Node side to answer

If a command doesn't finish within its timeout, the test fails with that command's error.

## 308: What makes an assertion able to retry the chain before it?

Since Cypress 12, query commands return a function that Cypress can call again. When an assertion fails, Cypress reruns the query functions in the chain, from the first query after the last non-query command, with the latest DOM. Then it runs the assertions again.

Non-query commands (`.then()`, `.click()`, `cy.request()`) break the chain. Assertions after them can only re-check the same value, not get a new one. That's why `cy.get().then().should()` doesn't retry the `cy.get()`.

## 309: How do you write a custom query that retries correctly?

The outer function runs once when the command is added, so it does setup like logging and timeout. The returned inner function runs on every retry and must only read state.

```js
Cypress.Commands.addQuery("getStoreValue", function (path, options = {}) {
  this.set("timeout", options.timeout);
  Cypress.log({ name: "getStoreValue", message: path });

  return () => {
    const store = cy.state("window").appStore;
    return Cypress._.get(store.getState(), path);
  };
});

cy.getStoreValue("cart.items.length").should("eq", 2);
```

Don't call other Cypress commands inside the inner function, and don't change anything there. `cy.state('window')` is an internal API used here to get the app's window, so check it against your Cypress version.

## 310: What exactly does Cypress check before an action?

The actionability steps for a command like `.click()` are:

1. Scroll the element into view (based on `scrollBehavior`)
2. Check it is attached to the DOM
3. Check it is visible
4. Check it isn't disabled (and isn't `readonly` for typing)
5. Check it isn't animating (based on `waitForAnimations`)
6. Check the target point isn't covered, using `document.elementFromPoint()`
7. Fire the events at the target coordinates

If a step fails, Cypress waits and tries again until the command timeout. The error message names the step that failed.

## 311: How does Cypress decide if an element is visible?

An element is not visible if, for example:

- It or a parent has `display: none`, `visibility: hidden`, or it has zero width or height
- It is hidden by a parent's `overflow: hidden` and lies outside the parent's box
- It has `position: fixed` and is covered by another element
- It is an `<option>` in a hidden `<select>`, or a `<details>` child while closed

In Cypress 16 the `visibilityStrategy` option controls the algorithm. The default `'modern'` strategy is faster and closer to what the browser actually renders. `'legacy'` keeps the old rules and is deprecated, meant only to help during upgrades.

## 312: Are Cypress events the same as real user events?

Not exactly. Cypress fires DOM events from JavaScript, in the same order a browser would for a real user. Most apps can't tell the difference.

But these events have `isTrusted: false`, and some browser behavior only happens with real input: CSS `:hover`, native drag and drop in some cases, the file picker, some keyboard shortcuts and certain security checks. For those cases you can use the browser's automation protocol, for example with `cypress-real-events`, which sends real input events in Chromium browsers.

## 313: How does cy.type work internally?

For each character, Cypress fires the events a browser fires for a real key press: `keydown`, `keypress`, `beforeinput`, `textInput`, `input` and `keyup`. It updates the value and the caret position itself, and respects `maxlength`, `readonly` and whether `preventDefault()` was called on `keydown`.

It focuses the element first with a click (unless it already has focus). Because Cypress updates the value itself, some inputs that depend on real key events, like certain masked inputs or editors, may need extra handling.

## 314: Why does cy.origin need serializable arguments?

The `cy.origin()` callback doesn't run in the test's page. Cypress turns the function into a string and sends it, with the `args`, to a spec bridge running in the other origin. The function is rebuilt there.

That means:

- The callback can't use variables from outside its own scope
- `args` must be data that can be copied with structured cloning
- Custom commands from your support file are not automatically available inside the callback unless you define or load them there
- Values you want back must be yielded from the callback

```js
cy.origin("https://auth.example.com", { args: { user: "ana" } }, ({ user }) => {
  cy.get("#user").type(user);
  return cy.get("#welcome").invoke("text");
}).then((text) => {
  // text from the other origin
});
```

## 315: What are the risks of setting chromeWebSecurity to false?

It turns off same-origin checks in Chromium. Tests can then:

- Pass while the real app would fail because of CORS or mixed content
- Reach into cross-origin iframes in ways users' browsers would block
- Behave differently in Firefox, where the option has no effect

It is also a sign the test design might be wrong: you are often better off using `cy.origin()`, stubbing the third party, or testing that part at the API level. Use it only when there is no other option, and document why.

## 316: What does modifyObstructiveCode do?

Some apps have code that tries to detect if they are framed or automated, like `if (window.top !== window.self)` to break out of an iframe. That would break Cypress, so Cypress rewrites such code in the HTML and JavaScript responses, by default.

```js
module.exports = defineConfig({
  modifyObstructiveCode: true, // default
});
```

If the rewriting causes problems (rare), you can turn it off, but then framebusting code in your app or a third party may break the test runner.

## 317: What is removeSRIAttributes?

Subresource Integrity (SRI) attributes (`integrity="sha384-..."`) make the browser check that a script or stylesheet matches a known hash. If Cypress or an intercept changes that file, the hash no longer matches and the browser refuses to load it.

The `removeSRIAttributes` option, added in Cypress 15.18, removes these attributes from the page so changed resources still load. Use it only in tests where you change scripts that have SRI. It doesn't affect your production build.

## 318: How does Cypress manage browser memory during long runs?

Long specs keep DOM snapshots, command data and logs in memory, and Chromium browsers can run out of memory and crash, especially in CI.

In Cypress 16, `manageBrowserMemory` (formerly `experimentalMemoryManagement`) is on by default. Cypress watches the browser's memory and forces garbage collection when needed. You can also:

- Lower `numTestsKeptInMemory` (it mostly matters in open mode)
- Split very large spec files
- Give the CI container more memory and shared memory

If you had `experimentalMemoryManagement: false`, set `manageBrowserMemory: false` instead, since removing the old option now turns the feature on.

## 319: What do you do when the browser crashes during a run in CI?

Crashes like "the renderer process crashed" are usually memory problems. Steps:

1. In Docker, give Chromium enough shared memory: `--shm-size=2g` or `--ipc=host`, or launch Chrome with `--disable-dev-shm-usage`
2. Make sure `manageBrowserMemory` is on
3. Split specs that have many tests or that render huge pages
4. Check for memory leaks in the app, like timers or listeners that never get cleaned up
5. Give the CI machine more RAM

In most cases, Cypress fails the spec that crashed and moves on to the next spec.

## 320: How do you add Chromium flags in Docker to avoid shared memory problems?

```js
on("before:browser:launch", (browser, launchOptions) => {
  if (browser.family === "chromium" && browser.name !== "electron") {
    launchOptions.args.push("--disable-dev-shm-usage");
  }
  return launchOptions;
});
```

By default Docker gives containers only 64 MB of `/dev/shm`, which Chrome uses heavily. This flag makes Chrome use `/tmp` instead. Running the container with a bigger `--shm-size` also works.

## 321: How big should a spec file be?

Smaller specs work better:

- Parallel runs balance by spec, so one huge spec can make one machine run much longer than the others
- Each spec starts fresh, so a crash or memory problem affects fewer tests
- Failures are easier to find

But each spec has some startup cost (bundling, page load), so thousands of tiny specs also slow things down. A good target is specs that take from under a minute to a few minutes and cover one feature.

## 322: How does Cypress Cloud decide which spec runs on which machine?

When machines join a parallel run, each one asks Cloud for the next spec. Cloud uses the durations from earlier runs to start the longest specs first, so all machines finish at about the same time.

New specs with no history are given out based on default rules. Because the balancing happens per spec, one very long spec sets the lower limit for the run time.

## 323: Are there alternatives to Cypress Cloud for recording and parallel runs?

Yes, third-party services and tools exist. Currents is a paid service that works with Cypress and gives parallel runs, history and analytics. Some teams build their own split with `cypress-split` and timing data stored in CI.

When you pick one, check that it is compatible with your Cypress version, since the recording APIs are not an official public standard. Older self-hosted options like sorry-cypress may not support the newest Cypress versions.

## 324: What exactly happens between tests when testIsolation is on?

Before each test, Cypress:

1. Navigates the app frame to `about:blank`, which removes the old page and stops its scripts
2. Clears cookies in all domains
3. Clears localStorage and sessionStorage in all domains
4. Resets intercepts, aliases, stubs, spies and clocks from the previous test

Things outside the browser are not reset: your database, server state and files. You still need to handle those with seeding or API calls.

## 325: How does cy.session cache and restore state?

The first time `cy.session(id, setup)` runs with a new `id`:

1. Cypress clears the page and all browser state
2. It runs `setup`
3. It saves cookies, localStorage and sessionStorage from all domains under that `id`
4. It runs `validate`, if given

Next time, Cypress clears the page, restores the saved state and runs `validate`. If validation fails, it runs `setup` again and saves new data.

The page is left blank after `cy.session()` in both cases, so you need `cy.visit()` after it. The `id` must include everything that changes the session, like the user and role, or two different logins will share one cache entry.

## 326: How do you use cy.session with logins across several origins?

`cy.session()` stores cookies and storage for all domains, so a login that went through another origin is restored too.

```js
cy.session(
  ["sso", username],
  () => {
    cy.visit("/login");
    cy.get("[data-cy=sso-login]").click();
    cy.origin(
      "https://sso.example.com",
      { args: { username } },
      ({ username }) => {
        cy.get("#username").type(username);
        cy.get("#password").type("secret");
        cy.get("button[type=submit]").click();
      },
    );
    cy.location("pathname").should("eq", "/home");
  },
  {
    validate() {
      cy.request("/api/me").its("status").should("eq", 200);
    },
  },
);
```

## 327: How do you design test data so tests can run in parallel?

- Each test creates its own data with unique values, like `ana+${Date.now()}@test.local` or a random ID
- Never depend on a fixed shared record that other tests may change or delete
- Use separate accounts or tenants per CI machine if the app has global settings
- Clean or reset only the data the test owns, not the whole database, when tests share a database
- For read-only reference data (countries, product catalog), seed it once and don't change it in tests

## 328: How do you test against a shared environment like staging?

Shared environments add problems: other people change data, deploys happen during runs and third parties are real.

- Create unique data per run and clean it up by a run ID
- Don't depend on data you didn't create
- Use separate test accounts with known permissions
- Check that the environment is healthy before the run (a `before:run` hook or a smoke spec)
- Stub third-party calls that cost money or send emails, if the environment allows it
- Keep the suite on staging small: a set of smoke tests for critical flows

## 329: What is a good strategy for mixing stubbed and real network tests?

A common split:

- **Stubbed UI tests** (most tests): stub the API with fixtures to test UI states, errors and edge cases. They are fast and stable.
- **Real E2E tests** (fewer): the main user flows against a real backend and database, to prove the parts work together.
- **API tests**: test the backend directly with `cy.request()` or a separate API test tool.

The danger of stubbing is that fixtures get out of date with the real API. You need something to keep them in sync.

## 330: How do you keep fixtures in sync with the real API?

- Generate fixture types from the API schema (OpenAPI or GraphQL) and type the fixtures, so a changed schema breaks the build
- Validate fixtures against the schema in a test or a script
- Record fixtures from real responses with a script, and refresh them regularly
- Run a smaller set of tests against the real API to catch differences
- Use contract tests (for example Pact) between the frontend and backend

The goal is that a change in the API breaks something before users see the bug.

## 331: What request and response events can you use inside cy.intercept?

Inside a handler, `req.on()` lets you hook into the response:

```js
cy.intercept("/api/**", (req) => {
  req.on("before:response", (res) => {
    // runs before the response goes to the browser, even if the request was stubbed
    res.headers["cache-control"] = "no-store";
  });

  req.on("response", (res) => {
    // runs when the real response arrives, you can change it
    res.setDelay(500);
  });

  req.on("after:response", (res) => {
    // runs after the response was sent to the browser, read only
    console.log(res.statusCode);
  });
});
```

`req.continue(callback)` is a shortcut for the `response` event that also ends the handler chain.

## 332: How do you add a header to every request in all tests?

Use a middleware intercept in the support file:

```js
// cypress/support/e2e.js
beforeEach(() => {
  cy.intercept({ url: "/api/**", middleware: true }, (req) => {
    req.headers["x-test-run-id"] = Cypress.expose("runId") ?? "local";
  });
});
```

Middleware intercepts run before normal ones and don't stop the request from reaching other handlers. So tests can still define their own stubs on the same URLs.

## 333: Do intercepts carry over between tests?

No. All intercepts are cleared before each test. That is why shared intercepts go in a `beforeEach` (in the spec or the support file), not a `before`.

Inside a test, intercepts stay until the test ends. To change a stub halfway through a test, define a new intercept for the same route. The newer one wins because handlers run from the last defined to the first.

## 334: How do you match requests by query parameters correctly?

Match with `pathname` and `query` instead of the full URL string:

```js
cy.intercept({
  method: "GET",
  pathname: "/api/products",
  query: { category: "shoes", page: "2" },
}).as("shoesPage2");
```

Query values are compared as strings. Extra query parameters in the real request don't stop the match. This is more reliable than globs, where the order of parameters matters.

## 335: What are common mistakes with URL patterns in cy.intercept?

- `cy.intercept('/api/users')` doesn't match `/api/users?page=2`. Use `/api/users*` or `pathname`.
- `*` in a glob doesn't cross `/`. `/api/*` matches `/api/users` but not `/api/users/1`. Use `**` for that.
- A regex without anchors can match more than you want: `/users/` also matches `/api/users-settings`.
- Defining the intercept after `cy.visit()` misses requests made on page load.
- An earlier intercept with a static response stops the request, so a later spy-only intercept on the same URL may not see it in the order you expect.

Check the "Routes" section of the Command Log to see which intercepts matched.

## 336: Can cy.wait('@alias') catch a request that happened before the wait?

Yes. An intercept records every matching request from the moment it is defined. `cy.wait('@alias')` resolves with the first matching request that hasn't been waited on yet, even if it finished before `cy.wait()` was called.

So this is fine:

```js
cy.intercept("GET", "/api/user").as("user");
cy.visit("/"); // request happens here
cy.wait("@user"); // still resolves
```

What matters is that the intercept was defined before the request was sent.

## 337: How do you test a race condition, like two responses arriving in the wrong order?

Delay responses differently so the slow one arrives last:

```js
cy.intercept(
  { method: "GET", url: "/api/search?q=lap*", times: 1 },
  {
    body: { results: ["old result"] },
    delay: 1500,
  },
).as("slow");
cy.intercept(
  { method: "GET", url: "/api/search?q=laptop*", times: 1 },
  {
    body: { results: ["laptop"] },
  },
).as("fast");

cy.visit("/search");
cy.get("[data-cy=search]").type("lap");
cy.get("[data-cy=search]").type("top");
cy.wait(["@fast", "@slow"]);
cy.get("[data-cy=result]").should("have.length", 1).and("have.text", "laptop");
```

If the app shows "old result", it doesn't cancel or ignore outdated requests.

## 338: How do cy.clock and network requests interact?

`cy.clock()` only fakes timers in the app window. Network requests still happen in real time, and `delay` in an intercept uses real time too.

So if the app uses `setTimeout` to schedule a fetch, you need `cy.tick()` to start it. Then the response arrives at real speed. A common pattern:

```js
cy.clock();
cy.intercept("GET", "/api/notifications").as("poll");
cy.visit("/");
cy.tick(30000); // the app's 30 second polling timer fires
cy.wait("@poll");
```

## 339: What are the limits of cy.clock?

- It must be called before the code that uses timers runs. Call it before `cy.visit()` to control timers from page load.
- It replaces `setTimeout`, `setInterval`, `Date` and related functions only in the app window, not in iframes or web workers.
- Animations based on `requestAnimationFrame` are not faked unless you include it in the list.
- When the clock is frozen, things like debounce and animation libraries wait forever until you call `cy.tick()`.
- `cy.clock()` is reset after each test. You can also call `clock.restore()` to go back to real timers in the middle of a test.

## 340: How do you stub something the app uses as soon as it starts?

Use the `window:before:load` event or `onBeforeLoad`, which run after the window is created but before the app's scripts run:

```js
Cypress.on("window:before:load", (win) => {
  win.__APP_CONFIG__ = { apiUrl: "/api", featureX: true };
  cy.stub(win, "IntersectionObserver").callsFake(function (cb) {
    this.observe = () => cb([{ isIntersecting: true }]);
    this.disconnect = () => {};
  });
});
```

If you use `Cypress.on` in the support file, it applies to every page load in every test.

## 341: How do you stop third-party scripts from affecting your tests?

- Block them with `blockHosts`
- Stub them with `cy.intercept()` to return an empty script or a fake one
- Stub their global objects (`window.ga`, `window.Intercom`) in `onBeforeLoad`
- Load them in the app only when not under test, for example `if (!window.Cypress)`

Third-party scripts make tests slower, add random errors (`uncaught:exception`) and send test traffic to real services. A fake script also lets you check that the app calls them correctly.

## 342: How do you test a feature flag service that uses streaming?

Many flag services open a streaming connection (SSE) for live updates, which `cy.intercept()` can't fully control. Approaches:

- Stub the initial flag request and block the streaming endpoint, so the SDK falls back to the initial values
- Use the SDK's test or offline mode in test builds, with flags set through `window` or a config object
- Expose a small hook in test builds to change flags at runtime

The aim is that each test decides its flags, instead of reading whatever is live in a shared environment.

## 343: How do you test OAuth or OIDC login flows?

Testing the provider's login UI every time is slow and often blocked. Better options:

1. Get tokens through the provider's token endpoint with `cy.request()` (for test users, if the provider allows a password or client credentials grant), then give them to the app the same way the app stores them (cookie or storage).
2. Use a local OIDC provider in test environments, for example a test Keycloak instance or a mock OIDC server, where you control users.
3. Have one E2E test that goes through the real redirect flow with `cy.origin()`, to make sure the integration works.

Always wrap the login in `cy.session()`.

## 344: How do you test two-factor authentication with one-time codes?

Generate the code in a task from the user's shared secret:

```js
// cypress.config.js
const { authenticator } = require("otplib");

on("task", {
  generateOtp(secret) {
    return authenticator.generate(secret);
  },
});
```

```js
cy.env(["OTP_SECRET"]).then(({ OTP_SECRET }) => {
  cy.task("generateOtp", OTP_SECRET).then((code) => {
    cy.get("[data-cy=otp]").type(code);
  });
});
```

For SMS codes, use a test phone number service with an API, or a backend switch that accepts a fixed code for test users only.

## 345: How do you deal with CAPTCHA in tests?

You shouldn't try to solve a real CAPTCHA, since its whole purpose is to stop automation. Instead:

- Turn it off in test environments, or use the provider's test keys (for example, reCAPTCHA and hCaptcha have test site keys that always pass)
- Let the backend skip verification for a test header or test users, only in non-production environments
- Stub the CAPTCHA script and its verify call

## 346: How do you test a payment form that lives in a cross-origin iframe?

Payment providers like Stripe put card fields in iframes from their own domain on purpose, so other scripts can't read card data. Options:

- Use the provider's test mode and test cards, and fill the iframe fields with `chromeWebSecurity: false` in Chromium, accepting the downsides
- Stub the provider's JS SDK and test only your app's part, then test the real integration manually or with the provider's own tools
- Test the backend side (webhooks, order creation) with API calls using test tokens

Many teams combine a stubbed UI test with an API-level test of the payment flow.

## 347: How do you run tests across several browsers in CI?

Use a CI matrix, one job per browser:

```yaml
strategy:
  matrix:
    browser: [chrome, firefox, edge]
steps:
  - uses: cypress-io/github-action@v7
    with:
      browser: ${{ matrix.browser }}
      start: npm start
      wait-on: "http://localhost:3000"
```

Running everything in every browser is expensive. A common choice: the full suite in Chrome, and a smaller smoke set in Firefox and others, maybe nightly. Note that Cypress 15 and later drive Firefox only through WebDriver BiDi, so you need a recent Firefox version.

## 348: What is the experimental WebKit support?

Cypress can run tests in WebKit, the engine behind Safari, using Playwright's WebKit build:

```js
module.exports = defineConfig({
  experimentalWebKitSupport: true,
});
```

```bash
npm install --save-dev playwright-webkit
npx cypress run --browser webkit
```

It is experimental and has known gaps, so it is not the same as testing in real Safari on macOS or iOS. It is useful to catch WebKit-specific CSS and JavaScript bugs early.

## 349: What does the deprecation of Electron as a test browser mean for you?

Electron is the default browser that ships with Cypress. In Cypress 16 it is deprecated as a test browser, so a future version may stop supporting it.

What to do:

- Set `defaultBrowser: 'chrome'` (or another browser) in the config, or always pass `--browser`
- Install Chrome or use the `cypress/browsers` image in CI
- Check tests that relied on Electron-only behavior, like how downloads or certain flags worked

It also makes CI closer to what users run, since few users use Electron as a browser.

## 350: What are the differences between headed and headless runs?

In headless mode the browser has no visible window. Possible differences:

- Default window and screen size can differ, which changes layouts and visibility
- GPU and font rendering can differ, which matters for screenshots
- Focus behavior: in a headed run, if you click outside the browser, focus events may change
- Some features, like certain media or clipboard APIs, behave differently

If a test passes headed but fails headless, set the window size explicitly with launch flags and check the screenshots and Test Replay of the headless run.

## 351: How do you run Cypress from a Node script?

Use the Module API:

```js
// scripts/run-e2e.js
const cypress = require("cypress");

async function main() {
  const results = await cypress.run({
    browser: "chrome",
    spec: "cypress/e2e/smoke/**/*.cy.js",
    config: { baseUrl: process.env.APP_URL },
  });

  if (results.status === "failed") {
    console.error("Cypress could not run:", results.message);
    process.exit(1);
  }

  console.log(`Passed: ${results.totalPassed}, failed: ${results.totalFailed}`);
  process.exit(results.totalFailed > 0 ? 1 : 0);
}

main();
```

`cypress.run()` takes the same options as the CLI and returns the results as an object. There is also `cypress.open()`.

## 352: When would you use the Module API instead of the CLI?

- To run different sets of specs one after another with different configs, and merge the results
- To send results to Slack, a database or a custom dashboard
- To rerun only the failed specs once more at the end
- To choose specs at run time, for example based on changed files in a pull request

The `after:run` event in `setupNodeEvents` can also handle some of these without a separate script.

## 353: How do you write a custom reporter?

Cypress uses Mocha reporters, so a custom reporter is a Mocha reporter class:

```js
// reporters/simple.js
const Mocha = require("mocha");
const { EVENT_TEST_PASS, EVENT_TEST_FAIL, EVENT_RUN_END } =
  Mocha.Runner.constants;

class SimpleReporter {
  constructor(runner) {
    const stats = { passed: 0, failed: 0 };
    runner.on(EVENT_TEST_PASS, () => stats.passed++);
    runner.on(EVENT_TEST_FAIL, (test, err) => {
      stats.failed++;
      console.log(`FAIL: ${test.fullTitle()} - ${err.message}`);
    });
    runner.on(EVENT_RUN_END, () => console.log(stats));
  }
}

module.exports = SimpleReporter;
```

```js
reporter: 'reporters/simple.js',
```

The reporter runs once per spec, so totals for the whole run need to be merged afterwards, for example in `after:run`.

## 354: What happens if two plugins register the same Node event?

For most events (`before:run`, `after:run`, `after:spec`, `before:browser:launch` and others), only the last registered handler is used. If two plugins both call `on('after:spec', ...)`, one of them silently stops working.

`task` is different: multiple `on('task', {...})` calls are merged, as long as task names don't clash.

Solutions:

- Write one handler yourself and call each plugin's logic inside it
- Use a helper like `cypress-on-fix`, which wraps `on` so several handlers for the same event all run

## 355: How do you build a reusable Cypress plugin for your company?

A plugin is usually an npm package with two entry points:

```js
// my-plugin/node.js - used in setupNodeEvents
module.exports = function registerMyPlugin(on, config) {
  on("task", {
    "myPlugin:seed"(data) {
      return seed(data);
    },
  });
  return config;
};
```

```js
// my-plugin/support.js - imported in the support file
Cypress.Commands.add("seed", (data) => cy.task("myPlugin:seed", data));
```

Also ship TypeScript declarations for the commands, prefix task and command names to avoid clashes, list `cypress` as a peer dependency, and test the plugin against the Cypress versions you support.

## 356: What are good rules for designing custom commands?

- Keep them small and focused, like `cy.login()` or `cy.createProject()`
- Don't hide assertions that tests should state themselves
- Don't make one command that does a whole user flow, since failures become hard to read
- Prefer `addQuery` for commands that only read state, so they retry
- Add `Cypress.log()` with useful `consoleProps` so they are easy to debug
- Add types, so editors show the parameters
- Use plain helper functions when the code doesn't need to be on `cy`

## 357: How do you write a custom command with a good Command Log entry?

Turn off the logs of inner commands and create your own log:

```js
Cypress.Commands.add("createUser", (user) => {
  const log = Cypress.log({
    name: "createUser",
    message: user.email,
    autoEnd: false,
    consoleProps: () => ({ user }),
  });

  cy.request({ method: "POST", url: "/api/users", body: user, log: false })
    .its("body", { log: false })
    .then((created) => {
      log.set("consoleProps", () => ({ user, created }));
      log.end();
      return created;
    });
});
```

The Command Log then shows one clean `createUser` line, and clicking it prints both the input and the result to the console.

## 358: How do you hide passwords and tokens from the Command Log?

Pass `{ log: false }` to the commands that would show them:

```js
cy.get("[data-cy=password]").type(password, { log: false });
cy.request({
  url: "/api/admin",
  headers: { Authorization: `Bearer ${token}` },
  log: false,
});
```

You can also overwrite `type` to hide the value for sensitive fields:

```js
Cypress.Commands.overwrite("type", (originalFn, element, text, options) => {
  if (options?.sensitive) {
    options.log = false;
    Cypress.log({
      $el: element,
      name: "type",
      message: "*".repeat(text.length),
    });
  }
  return originalFn(element, text, options);
});

cy.get("[data-cy=password]").type("secret", { sensitive: true });
```

Remember screenshots, videos and Test Replay can still show the page, so blackout or mask sensitive UI where needed.

## 359: How do you handle secrets in Cypress tests in CI?

- Store them in the CI secret store, not in the repo or `cypress.config.js`
- Pass them as `CYPRESS_*` environment variables, which fill `env`
- Read them with `cy.env()` only where needed
- Never put them in `expose`, which is readable from the browser
- Hide them in logs with `{ log: false }`
- Use test-only accounts with limited permissions, so a leaked secret can do little harm
- Be careful with Test Replay and videos if secrets are visible on screen

## 360: Why was Cypress.env removed in Cypress 16?

`Cypress.env()` loaded all env values into the browser at the start of each spec. Any script on the page, including the app, third-party code and browser extensions, could read them through the `Cypress` object. Secrets like API keys were exposed more than needed.

The new model separates two needs:

- `Cypress.expose()` for public values, still available synchronously
- `cy.env()` for secrets, sent to the browser only when a test asks for specific keys

There was a period in Cypress 15 where both existed and an `allowCypressEnv` option controlled the old API. That option was removed in 16.

## 361: How do you migrate a project from Cypress.env to the new APIs?

1. List every `Cypress.env()` call and decide if each value is secret or public.
2. Move public values to the `expose` block in the config and change the calls to `Cypress.expose('key')`.
3. Keep secrets in `env` and change the calls to `cy.env(['key']).then(...)`.
4. Turn sync helpers that returned secrets into custom commands.
5. Replace `env` in per-test config overrides with `expose`.
6. Replace `--env` CLI flags for public values with `--expose`.
7. Check plugins: older plugins that read `Cypress.env()` need updated versions. If a plugin reads public values from `CYPRESS_*` variables, copy them into `config.expose` in `setupNodeEvents`.
8. Remove `allowCypressEnv` from the config.

## 362: What is your checklist for upgrading to Cypress 16?

- Use Node 22, 24 or 26+
- Replace `Cypress.env()` with `cy.env()` and `Cypress.expose()`
- Replace `cy.exec()` with `cy.task()`, and remove `execTimeout`
- Remove `.end()` calls
- Rename `experimentalMemoryManagement` to `manageBrowserMemory`
- Remove `experimentalFastVisibility` and test with the new `visibilityStrategy: 'modern'`
- Check tests that depended on the old 10 ms `keystrokeDelay`
- Chain `.should()` directly after cookie and storage queries
- Stop setting viewport size and `blockHosts` through `Cypress.config()` in tests
- For component tests: Angular 21+, Vite 8+, Next.js 15.0.4+; change `cypress/angular-zoneless` imports to `cypress/angular`
- Pick a browser other than Electron
- Check intercepts that read `req.httpVersion` or compression headers

## 363: What were the main breaking changes in Cypress 14 and 15?

Cypress 14:

- `cy.origin()` needed for any other origin, including subdomains (no more `document.domain` injection by default)
- `cypress/react18` merged into `cypress/react`, and older React and Vue 2 support removed in component testing

Cypress 15:

- Node 18 and 23 dropped
- `cy.exec()` result's `code` renamed to `exitCode` (before `cy.exec()` was removed in 16)
- Three-argument `cy.stub(obj, 'name', fn)` removed, use `.callsFake(fn)`
- Firefox driven only through WebDriver BiDi
- Webpack 4 and Vite 4 dropped, `@cypress/vite-dev-server` became ESM only
- `Cypress.SelectorPlayground` renamed to `Cypress.ElementSelector`

## 364: How do you plan the upgrade of a big Cypress suite?

1. Read the migration guide for every major version between yours and the target.
2. Upgrade one major version at a time if you are far behind.
3. Create a branch, upgrade, and run the full suite in CI. Fix config errors first, then test failures.
4. Search the code for removed APIs with grep or a codemod.
5. Update plugins together with Cypress, since many need new versions.
6. If the suite is huge, run old and new versions side by side for a while, or move spec folders in steps.
7. Watch the flake rate for a few days after merging, since timing changes (like `keystrokeDelay`) can show up as new flakiness.

## 365: How would you move a test suite from Selenium to Cypress?

- Don't translate tests line by line. Selenium tests often have explicit waits and page objects that store elements, which don't fit Cypress.
- Start with the most valuable flows and write them the Cypress way: retrying queries, `cy.intercept()` waits, API setup instead of UI setup.
- Replace multi-tab and multi-browser tests with other approaches, or keep them in another tool.
- Run both suites side by side until the Cypress suite covers the same risks, then remove the old tests.
- Add `data-cy` attributes to the app as you go.

## 366: When would you pick Playwright over Cypress?

- You need multiple tabs, multiple users in separate browser contexts, or several origins in one test without special APIs
- You need real WebKit/Safari coverage
- You want free built-in parallelism and sharding without a paid service
- You want tests in other languages (Python, Java, .NET)
- Your team prefers plain `async`/`await` code

Cypress is a good pick when the team values its interactive app and time travel, already has Cypress knowledge and plugins, or wants E2E and component testing in the same tool with strong network stubbing.

## 367: Which metrics do you track for a Cypress suite?

- Total run time and run time per spec
- Pass rate on the main branch
- Flake rate: tests that passed only after a retry
- Most failing and slowest tests
- Time from failure to fix
- Number of tests skipped or quarantined

Cypress Cloud shows most of these. Without it, you can collect them from JUnit reports or the `after:run` results. The goal is that people trust a red build, since a suite people ignore has little value.

## 368: How do you handle flaky tests across a team?

1. Detect them: retries plus reporting of tests that passed on retry, or Cloud flake detection.
2. Quarantine: move a known flaky test out of the blocking suite (with a tag or a separate run) so it doesn't block everyone, but keep it running.
3. Assign: create a ticket with an owner and a deadline.
4. Fix the cause, then bring it back to the main suite.
5. Review new tests for known flaky patterns, like `cy.wait(ms)` or conditional testing.

Quarantine without follow-up becomes a pile of dead tests, so track the number and keep it small.

## 369: How do you make a slow Cypress suite faster?

- Log in with `cy.session()` and API calls instead of the UI
- Create test data through APIs or tasks instead of the UI
- Stub slow and third-party requests
- Remove `cy.wait(ms)` calls
- Move edge cases to component tests
- Run specs in parallel across machines
- Balance spec sizes
- Turn off video if you don't use it
- Cache dependencies and the Cypress binary in CI
- Run only the affected specs on pull requests, and the full suite on main or nightly

## 370: Why shouldn't tests depend on the order they run in?

Order-dependent tests break when:

- You run one test with `.only`
- A test is retried and the earlier test's state is gone
- Specs are split differently across parallel machines
- Someone adds a test in the middle

With test isolation on (the default), Cypress already clears browser state between tests, which shows these problems early. Each test should set up its own state and work alone.

## 371: What should you know about hooks in the support file?

Hooks at the top level of the support file are root-level hooks. They run for every test in every spec:

```js
// cypress/support/e2e.js
beforeEach(() => {
  cy.intercept(
    { url: "**/analytics/**", middleware: true },
    { statusCode: 204 },
  );
});
```

A root-level `before` runs once per spec file, not once per run, because each spec is loaded on its own with the support file. For something that should run once per whole run, use the `before:run` Node event.

## 372: How do you run setup only once for the whole run?

Use `before:run` in `setupNodeEvents`. It runs in Node once before any spec starts:

```js
setupNodeEvents(on, config) {
  on('before:run', async () => {
    await resetDatabase()
    await seedReferenceData()
  })
}
```

It fires in `cypress run`. In open mode, it only fires with `experimentalInteractiveRunEvents: true`. With parallel runs on several machines, each machine runs it, so the setup must be safe to run more than once at the same time.

## 373: How do hooks behave when a test is retried?

When a test is retried, its `beforeEach` and `afterEach` hooks run again for the new attempt. `before` hooks don't run again for the retry.

With test isolation on, the page and storage are cleared before the retry. So if a `before` hook visited the page or set state in the browser, the retry starts without it and fails in a confusing way. This is one more reason to put browser setup in `beforeEach`.

## 374: How do you use Cypress.currentRetry?

`Cypress.currentRetry` is `0` on the first attempt and goes up with each retry. You can use it to get more data when a flaky test is retried:

```js
beforeEach(() => {
  if (Cypress.currentRetry > 0) {
    cy.log(`Retry number ${Cypress.currentRetry}`);
    cy.task("logServerState");
  }
});
```

Don't use it to change what the test does on a retry, like skipping a step. That would hide the bug instead of finding it.

## 375: How do you debug tests that fail only in CI?

1. Look at Test Replay, screenshots and videos from the failing run.
2. Compare environments: browser and version, viewport, headless mode, CPU, memory, time zone, locale.
3. Check for timing problems: CI machines are slower, so look for missing waits on requests.
4. Check the data: does CI start with a clean database? Do parallel machines share data?
5. Run the same Docker image locally: `docker run -it -v $PWD:/e2e -w /e2e cypress/included:16.2.0`.
6. Add logs from the server or the app with `cy.task()` around the failing part.
7. Run the spec many times in CI to see how often it fails.

## 376: What is the difference between Test Replay, videos and screenshots for debugging?

- **Screenshots** show one moment, the failure. Cheap, but often not enough context.
- **Videos** show the whole spec as a recording. You can watch it, but you can't inspect elements, see network details or console logs.
- **Test Replay** records the DOM, network and console, and lets you step through commands like in open mode, inspecting elements at each step.

For CI failures, Test Replay usually finds the problem fastest. Without Cloud, a combination of screenshots and logs from the app and server is the next best option.

## 377: How do you test an app in several languages?

- Make the language a test input: set it with the `Accept-Language` header, a cookie or a URL parameter
- Don't hard-code texts in selectors. Use `data-cy` or roles and check the translated text only where it matters
- Load expected texts from the app's translation files, so tests don't drift from the app

```js
import de from "../../src/locales/de.json";

it("shows the German title", () => {
  cy.visit("/?lang=de");
  cy.get("h1").should("have.text", de.home.title);
});
```

Also check things that break in other languages: long words that overflow, right-to-left layout and date and number formats.

## 378: Can you measure performance with Cypress?

You can collect some numbers, but Cypress is not a performance tool. The test runner itself adds load, so results are rough.

```js
cy.visit("/");
cy.window().then((win) => {
  const [nav] = win.performance.getEntriesByType("navigation");
  expect(nav.domContentLoadedEventEnd).to.be.lessThan(3000);
});
```

Plugins like `cypress-audit` run Lighthouse checks from Cypress. For real performance tests, use Lighthouse CI, WebPageTest, or real user monitoring, and use Cypress at most for simple regressions, like a page that suddenly makes 50 requests.

## 379: Can Cypress be used for load testing?

No. Cypress runs one browser and one test at a time per process, and each test is heavy. Running many Cypress instances to create load costs a lot of resources and doesn't give realistic numbers.

Use tools made for this, like k6, Artillery, Gatling or JMeter, that send many requests at the API level. Cypress can check that the UI still works while a load test runs.

## 380: How do you test code that runs in a web worker?

`cy.stub()` and `cy.clock()` can't reach into workers. Options:

- Test the visible result in the UI and stub the network calls the worker makes (requests from dedicated workers are usually seen by `cy.intercept()`, but test it in your setup)
- Move the worker's logic into plain functions and test them with unit tests
- In test builds, add a way to run the logic on the main thread

Service workers have extra limits: they can cache responses and change network behavior, so many teams turn them off in E2E test builds.

## 381: How do you test a canvas or WebGL app?

The DOM doesn't show what is drawn on a canvas, so normal queries don't help much. Options:

- Check the app's state through `window` (for example a map's center or a chart's data)
- Click at coordinates: `cy.get('canvas').click(200, 150)`
- Compare screenshots with visual testing tools
- Read pixel data from the canvas in a `.then()` for simple checks

```js
cy.get("canvas").then(($canvas) => {
  const ctx = $canvas[0].getContext("2d");
  const [r, g, b] = ctx.getImageData(10, 10, 1, 1).data;
  expect([r, g, b]).to.deep.equal([255, 0, 0]);
});
```

## 382: How do you test virtualized lists?

Virtualized lists only render the rows on screen, so the DOM doesn't have all items.

- Don't count all items with `.should('have.length', 1000)`
- Scroll the container to bring a row into the DOM, then check it
- Check the data instead, for example through the request that loaded it

```js
cy.get("[data-cy=virtual-list]").scrollTo("bottom");
cy.contains("[data-cy=row]", "Item 999").should("be.visible");
```

Cypress only sees what is rendered, the same as a user.

## 383: How do you wait for a condition that no query can check, like a background job?

Write a recursive function that checks, waits and tries again a limited number of times:

```js
function waitForJob(id, attempts = 20) {
  if (attempts === 0) {
    throw new Error(`Job ${id} did not finish`);
  }
  cy.request(`/api/jobs/${id}`).then(({ body }) => {
    if (body.status !== "done") {
      cy.wait(1000);
      waitForJob(id, attempts - 1);
    }
  });
}

waitForJob(42);
```

`cy.wait(1000)` is fine here because it is a polling interval, not a guess about when the job is done. The `cypress-recurse` plugin gives a ready-made `recurse()` function for this.

## 384: How do you make tests with CSS animations stable?

- Turn off animations and transitions in test builds, through a CSS class, a `prefers-reduced-motion` style or a style tag injected in `onLoad`
- Wait for the final state, for example `.should('have.class', 'open')` or a visible element, not for time
- Keep `waitForAnimations` on, so Cypress waits for elements to stop moving before acting

Turning animations off also makes the suite faster and screenshots consistent.

## 385: What should you know about Shadow DOM when testing web components?

- `includeShadowDom: true` lets every query look inside open shadow roots, which is easier than calling `.shadow()` everywhere, but makes queries a bit slower
- `cy.contains()` also searches shadow roots when the option is on
- Closed shadow roots can't be reached
- Some events need `composed: true` to cross the shadow boundary, which matters when you `.trigger()` custom events

```js
cy.get("my-select").shadow().find("[part=option]").contains("Blue").click();
```

## 386: How do you test a micro frontend application?

- Test each micro frontend alone with component tests or E2E tests against its own dev server
- Have a smaller set of E2E tests on the composed app to check that the parts load and talk to each other
- Stub remote entry files with `cy.intercept()` to test what happens when one part fails to load
- If parts are on different origins, the pages they render are still one document, but navigation across origins needs `cy.origin()`

The main risks are version mismatches and shared state between parts, so test those paths on the composed app.

## 387: What should you watch out for when testing server-rendered apps like Next.js?

- The HTML may be visible before the app is hydrated, so clicks can be lost. Wait for a sign of hydration, like an element that only renders on the client or a `data-hydrated` attribute.
- Data fetched on the server doesn't go through the browser, so `cy.intercept()` can't stub it. Use a mock server for the backend in tests, or control data through the database.
- Client-side navigation after load does go through the browser, so it can be intercepted.

## 388: What are the limits of component testing with Next.js?

Cypress component tests run components in the browser through a dev server. That means:

- Async React Server Components can't be mounted, since they need a server
- Next.js specific features like server actions, middleware, and some data fetching functions don't run in a component test
- Components that use the router need it to be mocked or provided

Use component tests for client components, and E2E tests for pages that depend on server rendering. Cypress 16 supports Next.js 15.0.4+ and Next.js 16 for component testing.

## 389: What changed for Angular component testing in Cypress 16?

- The minimum version is Angular 21. Angular 22 is supported.
- The zoneless harness is the default in `cypress/angular`. Apps no longer need `zone.js` for component tests.
- The separate `@cypress/angular-zoneless` package was merged, so imports from `cypress/angular-zoneless` must change to `cypress/angular`.

If a component depends on Zone.js to trigger change detection, the test may need signals, explicit change detection or a Zone-based setup, so it is a good moment to move components to signals.

## 390: How do you customize the dev server for component tests?

Pass your own Vite or webpack config:

```js
import { defineConfig } from "cypress";
import viteConfig from "./vite.config";

export default defineConfig({
  component: {
    devServer: {
      framework: "react",
      bundler: "vite",
      viteConfig: {
        ...viteConfig,
        server: { port: 5174 },
      },
    },
  },
});
```

For webpack, use `webpackConfig`. You can also pass a function that returns the config. By default Cypress finds your project's config file, so you only need this when the test build must differ, like adding instrumentation for coverage.

## 391: How does component testing work under the hood?

Cypress starts your project's dev server (Vite or webpack) with a special entry. When you open a component spec, the dev server bundles the spec and everything it imports, including the component and its CSS. The bundle is loaded into an iframe with `component-index.html` as the page.

`cy.mount()` renders the component into a root element in that page, using the framework's own render function. There is no app routing or backend unless you provide them, and all Cypress commands work as usual, since it is still a real browser page.

## 392: How do you provide a store like Redux or Pinia in component tests?

Create a fresh store for every mount and allow tests to pass initial state:

```jsx
import { mount } from "cypress/react";
import { Provider } from "react-redux";
import { makeStore } from "../../src/store";

Cypress.Commands.add(
  "mount",
  (component, { preloadedState, ...options } = {}) => {
    const store = makeStore(preloadedState);
    return mount(<Provider store={store}>{component}</Provider>, options).then(
      (result) => ({
        ...result,
        store,
      }),
    );
  },
);
```

```jsx
cy.mount(<CartBadge />, { preloadedState: { cart: { items: [{ id: 1 }] } } });
cy.get("[data-cy=badge]").should("have.text", "1");
```

Returning the store lets tests dispatch actions or read state.

## 393: How do you test routing in a component test?

Wrap the component in a memory router and set the start URL:

```jsx
import { MemoryRouter, Routes, Route } from "react-router-dom";

it("goes to the details page", () => {
  cy.mount(
    <MemoryRouter initialEntries={["/products"]}>
      <Routes>
        <Route path="/products" element={<ProductList />} />
        <Route path="/products/:id" element={<h1>Details</h1>} />
      </Routes>
    </MemoryRouter>,
  );
  cy.contains("a", "Laptop").click();
  cy.contains("h1", "Details").should("be.visible");
});
```

For Vue and Angular, use their router testing setups in the mount options.

## 394: How do you test a custom React hook or Vue composable with Cypress?

Mount a small test component that uses it and renders the result:

```jsx
import { useCounter } from "./useCounter";

function HookHost() {
  const { count, increment } = useCounter(2);
  return (
    <button data-cy="btn" onClick={increment}>
      {count}
    </button>
  );
}

it("increments", () => {
  cy.mount(<HookHost />);
  cy.get("[data-cy=btn]").click().should("have.text", "3");
});
```

For pure logic hooks, a unit test runner is often simpler. Cypress is useful when the hook depends on browser behavior like resize, scroll or focus.

## 395: How do you combine coverage from E2E, component and unit tests?

1. Instrument code with Istanbul in all test types, using the same source paths.
2. Have each test run write its coverage JSON (`.nyc_output` or a custom folder).
3. Merge and report:

```bash
npx nyc merge coverage-parts .nyc_output/out.json
npx nyc report --reporter=lcov --reporter=text-summary
```

The merged report shows which code no test touches at all. When parallel CI jobs each produce coverage, collect the files as artifacts and merge them in a final job.

## 396: How do you instrument a Vite app for Cypress coverage?

Use `vite-plugin-istanbul` only when a test flag is set:

```js
// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import istanbul from "vite-plugin-istanbul";

export default defineConfig({
  plugins: [
    react(),
    istanbul({
      include: "src/*",
      exclude: ["node_modules", "cypress"],
      requireEnv: true, // only when VITE_COVERAGE=true
    }),
  ],
});
```

Then start the app with `VITE_COVERAGE=true` for E2E runs. The instrumented code puts data on `window.__coverage__`, which `@cypress/code-coverage` collects after each test.

## 397: What are the limits of code coverage from E2E tests?

- It shows which lines ran, not whether the result was checked. A test with no assertions can still give high coverage.
- Instrumented code is slower, so test runs take longer.
- Server code needs its own instrumentation and a way to send coverage back.
- Chasing 100% leads to tests that run code without testing behavior.

Use E2E coverage to find big untested areas, like whole pages or features no test visits, not as a strict number to hit.

## 398: Can Cypress be used for security testing?

Only for some checks. Cypress can:

- Verify access control: a normal user gets 403 or is redirected from admin pages and API endpoints
- Check that security headers are present with `cy.request()`
- Check that user input is escaped in the page (for example, `<script>` typed in a form is shown as text)
- Check that cookies have `HttpOnly`, `Secure` and `SameSite`

It is not a security scanner. Use tools like OWASP ZAP, Burp or dependency scanners for real security testing, and use Cypress for regressions on rules you already know.

## 399: How do you test for Content Security Policy violations?

Listen for the `securitypolicyviolation` event in the app window:

```js
cy.visit("/", {
  onBeforeLoad(win) {
    win.__cspViolations = [];
    win.document.addEventListener("securitypolicyviolation", (e) => {
      win.__cspViolations.push(e.violatedDirective + " " + e.blockedURI);
    });
  },
});
cy.get("[data-cy=app]").should("be.visible");
cy.window().its("__cspViolations").should("have.length", 0);
```

Make sure stubs and Cypress itself don't change the CSP headers in a way that hides problems. Cypress may need to relax the CSP to inject its own scripts.

## 400: How do you test an app that uses a self-signed certificate or client certificates?

For self-signed HTTPS certificates, Cypress accepts them by default for the app under test. Cypress 16.1 added `trustedCertificates`, which lets Chrome treat such origins as trusted, so things like caching work like with a real certificate.

For servers that require a client certificate (mutual TLS), use `clientCertificates`:

```js
module.exports = defineConfig({
  clientCertificates: [
    {
      url: "https://api.internal.example.com/**",
      certs: [{ cert: "certs/client.crt", key: "certs/client.key" }],
    },
  ],
});
```

Keep the key files out of the repo and load them from CI secrets.

## 401: How do you run Cypress behind a corporate proxy?

Cypress reads the standard proxy environment variables, for downloading the binary and for traffic from the browser and `cy.request()`:

```bash
export HTTP_PROXY=http://proxy.company.local:8080
export HTTPS_PROXY=http://proxy.company.local:8080
export NO_PROXY=localhost,127.0.0.1,.company.local
npx cypress run
```

Put your app's host in `NO_PROXY` if it runs locally, or every request to it goes through the proxy. If the proxy uses its own certificate, you may also need to set `NODE_EXTRA_CA_CERTS` for the Node side.

## 402: What is the hosts option used for?

`hosts` maps host names to IP addresses for the browser, like an `/etc/hosts` file, but only during the test run:

```js
module.exports = defineConfig({
  hosts: {
    "app.local.test": "127.0.0.1",
    "*.tenant.local.test": "127.0.0.1",
  },
});
```

It is useful for multi-tenant apps that use subdomains, or for testing with production-like domains against a local server, without changing the machine's settings.

## 403: Can Cypress test mobile behavior?

Only partly. You can:

- Change the viewport size with `cy.viewport()`
- Set a mobile user agent with the `userAgent` config option or in `cy.visit()` headers
- Fire touch events with `.trigger()`

But it still runs a desktop browser. There is no real touch input, mobile browser engine, device sensors or native app. For mobile web, test real devices with services like BrowserStack or Sauce Labs. For native mobile apps, use tools like Appium, Detox or Maestro.

## 404: How do you test touch gestures like swipe?

Fire touch events with coordinates:

```js
cy.get("[data-cy=carousel]")
  .trigger("touchstart", { touches: [{ clientX: 300, clientY: 100 }] })
  .trigger("touchmove", { touches: [{ clientX: 50, clientY: 100 }] })
  .trigger("touchend", { changedTouches: [{ clientX: 50, clientY: 100 }] });

cy.get("[data-cy=slide-2]").should("be.visible");
```

If the app uses pointer events, trigger `pointerdown`, `pointermove` and `pointerup` with `pointerType: 'touch'`. `cypress-real-events` also has `.realTouch()` and `.realSwipe()` in Chromium.

## 405: How do you test what the app does when the user goes offline?

`cy.intercept()` with `forceNetworkError` is enough to test failed requests. To make the browser itself go offline (so `navigator.onLine` is `false` and the `offline` event fires), Chromium users often use the DevTools Protocol:

```js
const goOffline = () =>
  cy.wrap(
    Cypress.automation("remote:debugger:protocol", {
      command: "Network.emulateNetworkConditions",
      params: {
        offline: true,
        latency: 0,
        downloadThroughput: 0,
        uploadThroughput: 0,
      },
    }),
  );

cy.visit("/");
cy.wrap(
  Cypress.automation("remote:debugger:protocol", { command: "Network.enable" }),
);
goOffline();
cy.contains("You are offline").should("be.visible");
```

`Cypress.automation` is not an official documented API and only works in Chromium, so keep it in one helper and check it after upgrades.

## 406: How do you use the Chrome DevTools Protocol from a Cypress test?

There are two ways:

- From the browser side, through `Cypress.automation('remote:debugger:protocol', { command, params })`, which plugins like `cypress-real-events` use. It is not officially documented.
- From the Node side, by connecting to the browser's debugging port in `before:browser:launch` with a CDP client library and exposing tasks.

With CDP you can emulate network conditions, CPU slowdown, geolocation, media features like dark mode, and send real input events. It only works in Chromium browsers, so tests that depend on it can't run in Firefox.

## 407: What is cypress-real-events and when do you need it?

`cypress-real-events` sends input through the DevTools Protocol, so the browser treats it as real user input (`isTrusted: true`). It adds commands like:

```js
import "cypress-real-events"; // in the support file

cy.get("[data-cy=menu]").realHover();
cy.get("[data-cy=input]").realClick();
cy.realPress("Tab");
cy.realPress(["Shift", "Tab"]);
cy.get("[data-cy=card]").realTouch();
```

You need it for CSS `:hover` styles, features that check `isTrusted`, and some keyboard or clipboard behavior. Since Cypress 14.3, `cy.press()` covers simple key presses like Tab without the plugin. It only works in Chromium browsers.

## 408: How does Cypress fit into a test pyramid?

A common setup for a web app:

- **Many unit tests** (Jest or Vitest) for functions, hooks, reducers and utilities
- **A good number of component tests** (Cypress or another tool) for UI components and their states
- **Fewer E2E tests** (Cypress) for the main flows across pages, with a real or stubbed backend
- **A small smoke suite** run against staging or production after deploys

E2E tests give the most confidence but are the slowest and hardest to keep stable, so you want them on the flows that matter most, not on every edge case.

## 409: How do you decide if a check belongs in a unit, component or E2E test?

Ask: what is the smallest test that can catch this bug?

- A calculation or a formatter: unit test
- How a component looks and behaves in its different states: component test
- That the login page sends the right request and goes to the dashboard: E2E with a stubbed API
- That a user can really buy something with the real backend and payment test mode: full E2E

If a bug in one layer can only be seen when layers work together, it needs a higher-level test.

## 410: How do you test keyboard navigation and focus order?

Use `cy.press()` to move focus and check where it lands:

```js
cy.visit("/signup");
cy.get("[data-cy=name]").focus();
cy.press(Cypress.Keyboard.Keys.TAB);
cy.focused().should("have.attr", "data-cy", "email");
cy.press(Cypress.Keyboard.Keys.TAB);
cy.focused().should("have.attr", "data-cy", "password");
```

For Shift+Tab and other key combinations, use `cypress-real-events` with `cy.realPress(['Shift', 'Tab'])`. Also check that focus is visible, for example with a `have.css` check on the outline.

## 411: How do you test focus handling in a modal dialog?

Check that focus moves into the dialog, stays there, and goes back when it closes:

```js
cy.get("[data-cy=open-dialog]").click();
cy.getByRole("dialog").should("be.visible");
cy.focused().should("have.attr", "data-cy", "dialog-title-input");

cy.press(Cypress.Keyboard.Keys.ESC);
cy.getByRole("dialog").should("not.exist");
cy.focused().should("have.attr", "data-cy", "open-dialog");
```

To test the focus trap, press Tab from the last element in the dialog and check that focus goes to the first one, not to the page behind.

## 412: How would you structure a large Cypress project?

```
cypress/
  e2e/
    auth/
    checkout/
    admin/
  component/          # or next to components in src/
  fixtures/
    api/              # stubbed API responses
  support/
    e2e.ts
    component.tsx
    commands/
      auth.ts
      data.ts
    index.d.ts
  pages/              # page objects or selector maps
  factories/          # test data builders
  tasks/              # Node tasks used in setupNodeEvents
cypress.config.ts
```

Keep Node code (tasks) apart from browser code, keep selectors in one place per page, and agree on naming. Write a short guide for the team so new tests follow the same style.

## 413: What is a test data factory and why use one?

A factory is a function that builds valid test data with defaults, so each test only states what matters to it:

```ts
import { faker } from "@faker-js/faker";

export const buildUser = (overrides: Partial<User> = {}): User => ({
  id: faker.string.uuid(),
  name: faker.person.fullName(),
  email: faker.internet.email(),
  role: "member",
  ...overrides,
});
```

```ts
const admin = buildUser({ role: "admin" });
cy.intercept("GET", "/api/me", { body: admin });
```

When the data model changes, you update one function instead of dozens of fixtures.

## 414: How do you clean up data created by tests?

- Tag all created records with a run ID (for example in the name or a metadata field), passed through `expose`
- Delete them in bulk by that run ID in an `after:run` handler, or a separate cleanup job
- Also clean old leftovers from failed runs, for example records older than one day with the test prefix
- Don't depend on cleanup for correctness: tests should still create their own data first

```js
on("after:run", async () => {
  await api.delete(`/test-data?runId=${process.env.RUN_ID}`);
});
```

## 415: How do you run only the specs affected by a pull request?

Pick specs from the changed files, then pass them to `--spec`:

```bash
CHANGED=$(git diff --name-only origin/main...HEAD | grep '\.cy\.ts$' | paste -sd, -)
if [ -n "$CHANGED" ]; then
  npx cypress run --spec "$CHANGED"
fi
```

This only catches changed spec files. To also map app code to specs, you need a mapping file, tags per feature, or tools like Nx that know the dependency graph. Always run the full suite on the main branch to catch what the selection missed.

## 416: How do you run E2E tests against preview deployments for each pull request?

1. Deploy each pull request to a preview URL (Vercel, Netlify, a review app).
2. Wait for the deployment to be ready in CI.
3. Run Cypress with that URL:

```bash
npx cypress run --config baseUrl=$PREVIEW_URL
```

Things to handle: the preview may need auth (basic auth or a bypass token), the backend for previews may be shared, so create unique data, and the deployment URL often arrives through a webhook or a CI event, not at a fixed time.

## 417: What is the difference between a smoke suite and a regression suite?

- A **smoke suite** is a small set of fast tests for the most important paths: the app loads, login works, the main action works. It runs after every deploy, even to production, and should finish in a few minutes.
- A **regression suite** is the full set of tests. It runs on pull requests or the main branch, or nightly if it is long.

Tag smoke tests (for example with `@cypress/grep`) so you can run them alone.

## 418: How do you check that a new test is not flaky before merging?

Run it many times in a row. One way is to repeat the test in a loop:

```js
Cypress._.times(20, (i) => {
  it(`creates an order (run ${i + 1})`, () => {
    // test body
  });
});
```

Some teams have a CI job that finds new or changed specs in the pull request and runs them several times, often called burn-in. Cypress Cloud's flake detection helps after the test is merged.

## 419: How do you share Cypress setup across many projects?

Make an internal npm package with:

- A base config function that projects extend
- Shared custom commands and their types
- Shared tasks and plugin setup
- Lint rules for Cypress code

```js
// cypress.config.js in a project
const { defineConfig } = require("cypress");
const { withCompanyDefaults } = require("@company/cypress-preset");

module.exports = defineConfig(
  withCompanyDefaults({
    e2e: { baseUrl: "http://localhost:3000" },
  }),
);
```

Version it carefully, since a change in the preset affects every project's tests.

## 420: Does cy.session with cacheAcrossSpecs share sessions between parallel machines?

No. Sessions are cached in the memory of one Cypress run on one machine. Each parallel machine creates its own sessions the first time they are needed.

This is fine in most cases, but if logins are limited (for example, a provider that rate-limits logins or allows only one active session per user), use different test users per machine or space out the logins.

## 421: How do you add extra information to failure messages?

Use the `fail` event. Change the error and throw it again:

```js
Cypress.on("fail", (err, runnable) => {
  err.message += `\n\nTest: ${runnable.fullTitle()}\nURL: ${window.location.href}`;
  throw err;
});
```

You must throw the error again, otherwise the test passes. You can also collect app logs through `cy.task()` in an `afterEach` when `this.currentTest.state === 'failed'`.

## 422: How do you test your own custom commands?

Write specs for them like for any code, often against a small HTML page or a component:

```js
describe("cy.getByTestId", () => {
  beforeEach(() => {
    cy.visit("cypress/fixtures/test-page.html");
  });

  it("finds an element added later", () => {
    cy.window().then((win) => {
      setTimeout(() => {
        win.document.body.insertAdjacentHTML(
          "beforeend",
          '<p data-testid="late">ok</p>',
        );
      }, 500);
    });
    cy.getByTestId("late").should("have.text", "ok");
  });
});
```

To check that a command fails in the right way, listen to `fail` with `cy.on('fail', ...)` and assert on the error message.

## 423: Scenario: your E2E suite takes two hours. What do you do?

1. Measure first: find the slowest specs and the most common slow steps (often UI logins and UI data setup).
2. Replace UI logins with `cy.session()` and API logins.
3. Create data through APIs or tasks.
4. Remove fixed waits and stub slow third-party calls.
5. Move edge case tests to component tests.
6. Split huge specs and run them in parallel across machines.
7. Run a fast subset on pull requests and the full suite on main or nightly.

Each step can be measured, so you can show the time going down.

## 424: Scenario: tests pass in Chrome but fail in Firefox. How do you approach it?

- Check if the failure is a real app bug in Firefox. Try the flow manually in Firefox.
- Look for Chromium-only things in the tests: `chromeWebSecurity: false`, CDP-based plugins like `cypress-real-events`, `Cypress.automation` calls.
- Check differences in how Firefox handles focus, scrolling, dates, fonts and file downloads.
- Make sure the Firefox version is recent, since Cypress drives it through WebDriver BiDi.

If a test can't work in Firefox by design, limit it with `{ browser: 'chromium' }` and note why.

## 425: Scenario: after a framework upgrade, many tests fail with detached element errors. What do you do?

The new version probably re-renders more often or at different times. Steps:

- Look for chains that continue after an action, and split them so the next command starts with a fresh query
- Look for elements saved in `.then()` and used later with `cy.wrap()`, and query them again instead
- Wait for the data load (request alias or a ready element) before acting, so the re-render happens first
- Check that the app doesn't unmount and remount large parts of the page without reason, which can also be a performance bug

## 426: Scenario: logging in takes 10 seconds and every test logs in. How do you fix it?

Wrap the login in `cy.session()` so it runs once per user per spec, or once per run with `cacheAcrossSpecs: true`. Switch from UI login to `cy.request()` login where possible.

```js
Cypress.Commands.add("login", (role = "member") => {
  cy.session(
    [role],
    () => {
      cy.env([`${role}Password`]).then((env) => {
        cy.request("POST", "/api/login", {
          username: role,
          password: env[`${role}Password`],
        });
      });
    },
    {
      validate: () => cy.request("/api/me").its("status").should("eq", 200),
      cacheAcrossSpecs: true,
    },
  );
});
```

Keep one test that logs in through the UI, so the login page itself is still tested.

## 427: Scenario: checkout redirects to a third-party domain and back. How do you test it?

Decide what you need to prove:

- To test your app's handling of success and failure, stub the redirect: intercept the call that starts the redirect, and visit your return URL directly with the parameters the provider would send.
- To test the full flow once, use the provider's test mode and `cy.origin()` for the provider's page:

```js
cy.get("[data-cy=pay]").click();
cy.origin("https://checkout.provider.test", () => {
  cy.get("[data-cy=card-number]").type("4242424242424242");
  cy.get("[data-cy=submit]").click();
});
cy.location("pathname").should("eq", "/order/confirmation");
```

Keep the full flow test small, since it depends on an outside service you don't control.

## 428: Scenario: the frontend calls ten microservices. How do you stub them in a clean way?

- Create one fixture set per service, with a default "happy" response for each endpoint
- Put default intercepts in a custom command, like `cy.stubDefaultApis()`, used in `beforeEach`
- Let each test override only the endpoints it cares about, since later intercepts win
- Build responses with factories instead of huge static JSON files
- Keep a few E2E tests that don't stub, to check the real services work together

```js
beforeEach(() => {
  cy.stubDefaultApis();
});

it("shows an error when pricing is down", () => {
  cy.intercept("GET", "/pricing/api/**", { statusCode: 503 });
  cy.visit("/product/1");
  cy.contains("Prices are not available").should("be.visible");
});
```

## 429: Scenario: you need to check the content of an exported Excel or PDF file. How?

Download the file, then parse it in Node with a task:

```js
// cypress.config.js
const XLSX = require("xlsx");
const { PDFParse } = require("pdf-parse");
const fs = require("node:fs");

on("task", {
  readExcel(path) {
    const workbook = XLSX.readFile(path);
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    return XLSX.utils.sheet_to_json(sheet);
  },
  async readPdf(path) {
    const parser = new PDFParse({ data: fs.readFileSync(path) });
    const result = await parser.getText();
    return result.text;
  },
});
```

```js
cy.get("[data-cy=export-xlsx]").click();
cy.readFile(`${Cypress.config("downloadsFolder")}/report.xlsx`, null).should(
  "exist",
);
cy.task("readExcel", `${Cypress.config("downloadsFolder")}/report.xlsx`).should(
  "have.length",
  10,
);
```

Check the API of the parsing libraries for the version you install, as they change between major versions.

## 430: Scenario: your test needs data from a service owned by another team. What do you do?

- Don't depend on whatever data happens to be in their test environment
- Ask for a test API or seed script you can call from `cy.task()` or `cy.request()`
- If that is not possible, stub their service in most tests and keep a small number of real integration tests that create their own data
- Agree on a contract (OpenAPI or contract tests) so you know when their API changes
- Make failures clear: a `before` check that their service is reachable, with a clear error, saves debugging time

## 431: Scenario: the team uses cy.wait(5000) everywhere. How do you fix it?

1. Turn on the `cypress/no-unnecessary-waiting` lint rule so no new ones are added.
2. For each wait, find what it is waiting for: a request, an element, an animation, a redirect.
3. Replace it with the right wait: `cy.wait('@alias')`, `.should('be.visible')`, `cy.location().should(...)`.
4. Remove waits that wait for nothing (many are left over from debugging).
5. Measure the suite time before and after to show the gain.

Explain why in a short team guide, since the habit usually comes from tools without automatic waiting.

## 432: Scenario: a promo banner appears only for some users and blocks clicks. How do you handle it?

Don't write `if banner exists, close it`. Control the condition instead:

- Set the cookie or localStorage key that marks the banner as dismissed, in `onBeforeLoad` or with `cy.setCookie()` before the visit
- Stub the request that decides whether to show the banner
- Use a test user who is not in the promo group

Then write one separate test for the banner itself with the condition turned on.

## 433: Scenario: CI runs crash with out of memory errors in one big spec. How do you fix it?

- Check that `manageBrowserMemory` is on (default in Cypress 16)
- Split the spec into smaller ones
- In Docker, raise shared memory (`--shm-size`) or add `--disable-dev-shm-usage`
- Turn off video if it's not needed
- Look for app memory leaks: heap snapshots in DevTools while running the spec in open mode can show growing listeners or detached DOM
- Avoid keeping huge objects in aliases or closures across many tests

## 434: Scenario: you must test sign-up with email confirmation from start to end. How?

```js
it("signs up and confirms the email", () => {
  const email = `signup+${Date.now()}@test.local`;

  cy.visit("/signup");
  cy.get("[data-cy=email]").type(email);
  cy.get("[data-cy=password]").type("Str0ngPass!", { log: false });
  cy.get("[data-cy=submit]").click();
  cy.contains("Check your email").should("be.visible");

  cy.task("waitForEmail", { to: email, subject: "Confirm your account" }).then(
    (mail) => {
      const link = mail.html.match(/href="([^"]+confirm[^"]+)"/)[1];
      cy.visit(link);
    },
  );

  cy.contains("Your email is confirmed").should("be.visible");
});
```

`waitForEmail` is a task that polls a test mail server (like Mailpit) until the email arrives or a timeout passes. Unique emails let this run in parallel.

## 435: Scenario: selectors break with every UI redesign. What do you change?

- Add `data-cy` attributes to important elements and agree that changing them is a breaking change for tests
- Use `cy.getByRole()` with accessible names for buttons, links and fields, which change less than CSS
- Keep selectors in one place (page objects or selector maps), so one change fixes many tests
- Don't use selectors based on layout, like `div > div:nth-child(2)`
- Add a lint rule or review checklist against class-based selectors

## 436: Scenario: the team starts using cy.prompt and Studio to write tests. What do you watch for?

- Review generated tests like any code: clear names, good selectors, real assertions, no extra steps
- Make sure each test checks the outcome, not only that steps ran without errors
- Keep secrets out of prompts with placeholders, and don't put real user data in prompts
- Decide when to keep `cy.prompt()` steps and when to export them as normal Cypress code (code is easier to review and doesn't need Cloud or AI calls)
- Watch CI time and cost, since AI generation adds time the first time and after cache misses
- Remember it works only for E2E tests in Chromium browsers

## 437: Scenario: you want to upgrade to Cypress 16, but a plugin you need doesn't support it yet. What do you do?

- Check the plugin's issues and pull requests, often a fix is waiting
- Test it anyway: many plugins work fine if they don't use removed APIs like `Cypress.env()` or `cy.exec()`
- If it breaks on a small thing, use `patch-package` to fix it locally and send the fix upstream
- Look for a maintained fork or an alternative
- If none of that works, stay on the last 15.x version for now, and plan the upgrade with a date

Don't hold the whole project on an old Cypress version for months because of one plugin.

## 438: Scenario: after upgrading to Cypress 16, some intercept tests fail in Chrome. Why could that be?

Cypress 16 moved Chromium network interception to the browser's own network layer. Tests may fail if they:

- Read `req.httpVersion`, which is no longer reported
- Check compression headers like `content-encoding` on intercepted responses
- Depended on HTTP/1.1 behavior, while the browser now uses HTTP/2 where the server supports it

Fix the tests to not depend on those details. `forceHttp1` can bring back the old behavior for a while, but it is deprecated, so use it only to unblock the upgrade.

## 439: Scenario: cy.wait('@alias') sometimes times out with "no request ever occurred". What do you check?

- The intercept is defined after the action that sends the request. Move it before `cy.visit()` or the click.
- The URL pattern doesn't match every time, for example because of a query string, a trailing slash, or a different host.
- The app sometimes uses cached data and skips the request. Check service workers, HTTP caching and app caches like React Query.
- An earlier `cy.wait('@alias')` already used the request, and the app only makes it once.
- The method is different (a `POST` where you intercept `GET`).

Open the run in Test Replay or open mode and look at the network list and the "Routes" table in the Command Log.

## 440: Scenario: a feature behaves differently around midnight. How do you test it?

Freeze time with `cy.clock()` close to the boundary, then move it forward:

```js
const justBeforeMidnight = new Date(2026, 2, 31, 23, 59, 50).getTime();
cy.clock(justBeforeMidnight, ["Date", "setTimeout", "setInterval"]);
cy.visit("/daily-deals");
cy.contains("Deals for March 31").should("be.visible");

cy.tick(15 * 1000);
cy.contains("Deals for April 1").should("be.visible");
```

If the server also uses the date, you need a way to control server time in test environments too, or stub the API response for both days.

## 441: Scenario: tests pass on developers' laptops but fail in CI because CI runs in UTC. What do you do?

Make time zone part of the test setup instead of the machine:

- Run CI and local tests in the same time zone with `TZ=...`, or better, run both in UTC
- Freeze `Date` with `cy.clock()` in tests that show dates
- Build expected values with the same formatting library and time zone the app uses, not with hard-coded strings
- Add a few tests that set a specific time zone on purpose, to check that conversion works

## 442: Scenario: a spec passes alone but fails when the whole suite runs. Why?

Common reasons:

- Data left by another spec: a shared user changed by another test, a record with the same unique name
- Server or database state that isn't reset between specs
- Sessions with `cacheAcrossSpecs` that are invalid in this spec
- Memory or resource exhaustion late in the run
- Root hooks in the support file that behave differently based on what ran before

Run the spec together with the one before it to reproduce, then remove the shared state.

## 443: Scenario: parallel CI machines overwrite each other's data. How do you fix it?

- Create unique data per test (random IDs, emails with timestamps)
- Use different test accounts per machine, picked from an index like `SPLIT_INDEX` or the CI node number passed through `expose`
- Don't reset the whole database in `before:run` when machines share it. Reset only the data one machine owns, or give each machine its own database or tenant
- Avoid tests that change global settings, or run them in a separate serial job

## 444: Scenario: Cypress Cloud costs are growing too fast. What can you do?

Cloud is usually billed by recorded test results. Options:

- Record only the runs you need history for (main branch, release branches), and run pull request jobs without `--record` or with a smaller set
- Remove duplicate tests that cover the same thing
- Move edge cases to component or unit tests
- Use auto cancellation so runs with many failures stop early
- Run the full matrix of browsers less often

Compare the cost with what it saves: faster debugging with Test Replay and shorter CI times from load balancing.

## 445: Scenario: you want every test to fail on any console error or 5xx response. How do you set it up?

In the support file:

```js
beforeEach(() => {
  cy.intercept({ url: "/api/**", middleware: true }, (req) => {
    req.on("response", (res) => {
      if (res.statusCode >= 500) {
        throw new Error(
          `Server error ${res.statusCode} on ${req.method} ${req.url}`,
        );
      }
    });
  });
});

Cypress.on("window:before:load", (win) => {
  cy.spy(win.console, "error").as("consoleError");
});

afterEach(() => {
  cy.get("@consoleError").should("not.have.been.called");
});
```

Tests that expect errors on purpose need a way to opt out, for example a test config value read with `Cypress.expose()` or a tag. Throwing inside the response handler fails the test at that point. Check how this behaves in your Cypress version and adjust if you want a softer failure.

## 446: Scenario: you need to test a flow with two users, like an approval process. How?

Cypress controls one browser, so act as one user in the UI and as the other through the API:

```js
it("manager approves a request", () => {
  cy.login("employee");
  cy.visit("/requests/new");
  cy.get("[data-cy=amount]").type("500");
  cy.get("[data-cy=submit]").click();
  cy.get("[data-cy=request-id]")
    .invoke("text")
    .then((id) => {
      // manager approves through the API
      cy.loginByApi("manager");
      cy.request("POST", `/api/requests/${id}/approve`);

      // back to the employee in the UI
      cy.login("employee");
      cy.visit(`/requests/${id}`);
      cy.contains("Approved").should("be.visible");
    });
});
```

Also write a separate test for the manager's UI, starting from a request created through the API.

## 447: Scenario: a new team member writes tests that check implementation details. How do you guide them?

Explain that a test should check what a user sees and can do, so it survives refactors. Examples:

- Instead of checking a component's internal state, check the text or element it renders
- Instead of selecting by CSS class, select by role, text or `data-cy`
- Instead of asserting the exact order of internal API calls, assert the final result on the page and only the requests that matter to the user (like the order being created)

Pair on a couple of tests and add the rules to the team's test guide and review checklist.

## 448: What makes a good Cypress test?

- It tests one behavior and has a clear name that says what is expected
- It sets up its own state and passes when run alone
- It waits on real signals, never on fixed times
- It uses stable selectors: roles, text or `data-cy`
- It uses the UI only for what it tests, and APIs for setup
- It has clear assertions on the outcome, not only steps
- It runs fast and gives the same result every time
- When it fails, the error tells you what went wrong

## 449: How do you decide what to stub in an E2E test?

Stub what you don't control or don't want to test right now:

- Third-party services: payments, analytics, maps, chat widgets
- Slow or flaky dependencies
- States that are hard to produce for real: errors, empty lists, timeouts, rare data

Don't stub what the test is meant to prove. If a test is called "user can create an order", at least one version of it should hit the real order API. The more you stub, the more your tests check the frontend alone, which is fine if you know that's what you are doing.

## 450: What do you check when reviewing a pull request with Cypress tests?

- Do the tests check the behavior the pull request changes?
- Can each test run alone, and in any order?
- No `cy.wait(ms)`, no `.only`, no `force: true` without a reason
- Selectors use `data-cy`, roles or text, not CSS classes
- Intercepts are defined before the actions that trigger them
- Setup uses APIs, tasks or `cy.session()`, not long UI flows
- No secrets in code, and sensitive values have `{ log: false }`
- Assertions check outcomes, and negative assertions come after a positive one
- New custom commands are needed, typed and named clearly
- The new specs passed several times in CI, not just once
