# React Testing Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions with answers about testing React apps, split into three levels: 150 easy, 150 moderate and 150 advanced. They cover unit tests, integration tests and end-to-end tests.

The answers are based on the tools most teams use today: React 19, Vitest 4 and Jest 30 as test runners, React Testing Library 16 with user-event 14 and jest-dom, Mock Service Worker (MSW) 2 for API mocking, and Playwright and Cypress 15 for end-to-end tests. Older tools like Enzyme and react-test-renderer are mentioned where you may still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: Why do we write tests for a React app?](#1-why-do-we-write-tests-for-a-react-app)
- [2: What is the testing pyramid?](#2-what-is-the-testing-pyramid)
- [3: What is the testing trophy?](#3-what-is-the-testing-trophy)
- [4: What is the difference between unit, integration and end-to-end tests?](#4-what-is-the-difference-between-unit-integration-and-end-to-end-tests)
- [5: What does a unit test look like in a React project?](#5-what-does-a-unit-test-look-like-in-a-react-project)
- [6: What does an integration test look like in a React project?](#6-what-does-an-integration-test-look-like-in-a-react-project)
- [7: What is an end-to-end test?](#7-what-is-an-end-to-end-test)
- [8: Why are TypeScript and ESLint called "static tests"?](#8-why-are-typescript-and-eslint-called-static-tests)
- [9: What tools are commonly used to test React apps today?](#9-what-tools-are-commonly-used-to-test-react-apps-today)
- [10: What is a test runner?](#10-what-is-a-test-runner)
- [11: What is Jest?](#11-what-is-jest)
- [12: What is Vitest?](#12-what-is-vitest)
- [13: How do you choose between Jest and Vitest?](#13-how-do-you-choose-between-jest-and-vitest)
- [14: What is React Testing Library?](#14-what-is-react-testing-library)
- [15: What is the main idea behind React Testing Library?](#15-what-is-the-main-idea-behind-react-testing-library)
- [16: What is jsdom?](#16-what-is-jsdom)
- [17: What is happy-dom?](#17-what-is-happy-dom)
- [18: Why do you need a DOM environment to test React components?](#18-why-do-you-need-a-dom-environment-to-test-react-components)
- [19: How do you set up Vitest and React Testing Library in a Vite React project?](#19-how-do-you-set-up-vitest-and-react-testing-library-in-a-vite-react-project)
- [20: How do you set up Jest for a React project with TypeScript?](#20-how-do-you-set-up-jest-for-a-react-project-with-typescript)
- [21: What is a setup file in Vitest or Jest?](#21-what-is-a-setup-file-in-vitest-or-jest)
- [22: What is @testing-library/jest-dom?](#22-what-is-testing-libraryjest-dom)
- [23: How should test files be named?](#23-how-should-test-files-be-named)
- [24: Where should you put test files?](#24-where-should-you-put-test-files)
- [25: What is the basic structure of a test?](#25-what-is-the-basic-structure-of-a-test)
- [26: What is the difference between test and it?](#26-what-is-the-difference-between-test-and-it)
- [27: What is an assertion?](#27-what-is-an-assertion)
- [28: What is the difference between toBe and toEqual?](#28-what-is-the-difference-between-tobe-and-toequal)
- [29: What is the difference between toEqual and toStrictEqual?](#29-what-is-the-difference-between-toequal-and-tostrictequal)
- [30: What are some common matchers in Vitest and Jest?](#30-what-are-some-common-matchers-in-vitest-and-jest)
- [31: How do you check that something is NOT true?](#31-how-do-you-check-that-something-is-not-true)
- [32: What is the Arrange, Act, Assert pattern?](#32-what-is-the-arrange-act-assert-pattern)
- [33: How do you render a component with React Testing Library?](#33-how-do-you-render-a-component-with-react-testing-library)
- [34: What does render return?](#34-what-does-render-return)
- [35: What is screen and why should you use it?](#35-what-is-screen-and-why-should-you-use-it)
- [36: What are queries in React Testing Library?](#36-what-are-queries-in-react-testing-library)
- [37: What is the difference between getBy, queryBy and findBy?](#37-what-is-the-difference-between-getby-queryby-and-findby)
- [38: What do the "All" queries do?](#38-what-do-the-all-queries-do)
- [39: In what order should you prefer the queries?](#39-in-what-order-should-you-prefer-the-queries)
- [40: How does getByRole work?](#40-how-does-getbyrole-work)
- [41: What does the name option in getByRole do?](#41-what-does-the-name-option-in-getbyrole-do)
- [42: When should you use getByLabelText?](#42-when-should-you-use-getbylabeltext)
- [43: When should you use getByPlaceholderText?](#43-when-should-you-use-getbyplaceholdertext)
- [44: When should you use getByText?](#44-when-should-you-use-getbytext)
- [45: What does getByDisplayValue do?](#45-what-does-getbydisplayvalue-do)
- [46: What are getByAltText and getByTitle used for?](#46-what-are-getbyalttext-and-getbytitle-used-for)
- [47: What is getByTestId and when should you use it?](#47-what-is-getbytestid-and-when-should-you-use-it)
- [48: How do you check that an element is not on the page?](#48-how-do-you-check-that-an-element-is-not-on-the-page)
- [49: What does toBeInTheDocument check?](#49-what-does-tobeinthedocument-check)
- [50: What is the difference between toBeVisible and toBeInTheDocument?](#50-what-is-the-difference-between-tobevisible-and-tobeinthedocument)
- [51: How do you check the text of an element?](#51-how-do-you-check-the-text-of-an-element)
- [52: How do you check the value of an input or whether a checkbox is checked?](#52-how-do-you-check-the-value-of-an-input-or-whether-a-checkbox-is-checked)
- [53: How do you check if a button is disabled?](#53-how-do-you-check-if-a-button-is-disabled)
- [54: How do you check attributes and CSS classes?](#54-how-do-you-check-attributes-and-css-classes)
- [55: What is @testing-library/user-event?](#55-what-is-testing-libraryuser-event)
- [56: What is the difference between fireEvent and user-event?](#56-what-is-the-difference-between-fireevent-and-user-event)
- [57: How do you set up user-event?](#57-how-do-you-set-up-user-event)
- [58: Why are user-event methods async?](#58-why-are-user-event-methods-async)
- [59: How do you simulate typing in an input?](#59-how-do-you-simulate-typing-in-an-input)
- [60: How do you simulate a click?](#60-how-do-you-simulate-a-click)
- [61: How do you clear an input?](#61-how-do-you-clear-an-input)
- [62: How do you select an option from a dropdown?](#62-how-do-you-select-an-option-from-a-dropdown)
- [63: How do you simulate keyboard keys?](#63-how-do-you-simulate-keyboard-keys)
- [64: How do you test hover effects like tooltips?](#64-how-do-you-test-hover-effects-like-tooltips)
- [65: How do you test a file upload?](#65-how-do-you-test-a-file-upload)
- [66: How would you test a simple counter component?](#66-how-would-you-test-a-simple-counter-component)
- [67: How do you test that a component renders its props correctly?](#67-how-do-you-test-that-a-component-renders-its-props-correctly)
- [68: How do you test conditional rendering?](#68-how-do-you-test-conditional-rendering)
- [69: How do you test that a list renders correctly?](#69-how-do-you-test-that-a-list-renders-correctly)
- [70: How do you test that a form calls onSubmit with the right data?](#70-how-do-you-test-that-a-form-calls-onsubmit-with-the-right-data)
- [71: What is a mock?](#71-what-is-a-mock)
- [72: What is the difference between a mock, a stub, a spy and a fake?](#72-what-is-the-difference-between-a-mock-a-stub-a-spy-and-a-fake)
- [73: How do you create a mock function?](#73-how-do-you-create-a-mock-function)
- [74: How do you check how a mock function was called?](#74-how-do-you-check-how-a-mock-function-was-called)
- [75: How do you make a mock function return a value?](#75-how-do-you-make-a-mock-function-return-a-value)
- [76: What is vi.spyOn and when do you use it?](#76-what-is-vispyon-and-when-do-you-use-it)
- [77: How do you mock a whole module?](#77-how-do-you-mock-a-whole-module)
- [78: What is the difference between clearing, resetting and restoring mocks?](#78-what-is-the-difference-between-clearing-resetting-and-restoring-mocks)
- [79: What are beforeEach, afterEach, beforeAll and afterAll?](#79-what-are-beforeeach-aftereach-beforeall-and-afterall)
- [80: Does React Testing Library clean up after each test?](#80-does-react-testing-library-clean-up-after-each-test)
- [81: What do test.only, test.skip and test.todo do?](#81-what-do-testonly-testskip-and-testtodo-do)
- [82: What is test.each?](#82-what-is-testeach)
- [83: How do you run tests in watch mode?](#83-how-do-you-run-tests-in-watch-mode)
- [84: How do you run only one test file or one test?](#84-how-do-you-run-only-one-test-file-or-one-test)
- [85: What is code coverage?](#85-what-is-code-coverage)
- [86: How do you generate a coverage report?](#86-how-do-you-generate-a-coverage-report)
- [87: What are the different coverage metrics?](#87-what-are-the-different-coverage-metrics)
- [88: Is 100% code coverage a good goal?](#88-is-100-code-coverage-a-good-goal)
- [89: What is snapshot testing?](#89-what-is-snapshot-testing)
- [90: How do you update snapshots when the change is intentional?](#90-how-do-you-update-snapshots-when-the-change-is-intentional)
- [91: What are inline snapshots?](#91-what-are-inline-snapshots)
- [92: When are snapshot tests a bad idea?](#92-when-are-snapshot-tests-a-bad-idea)
- [93: How do you see what the DOM looks like inside a test?](#93-how-do-you-see-what-the-dom-looks-like-inside-a-test)
- [94: What are logRoles and Testing Playground?](#94-what-are-logroles-and-testing-playground)
- [95: What does act() do?](#95-what-does-act-do)
- [96: Do you need to call act yourself when using React Testing Library?](#96-do-you-need-to-call-act-yourself-when-using-react-testing-library)
- [97: How do you test async behavior with waitFor?](#97-how-do-you-test-async-behavior-with-waitfor)
- [98: What is the difference between findBy and waitFor?](#98-what-is-the-difference-between-findby-and-waitfor)
- [99: How do you wait for something to disappear?](#99-how-do-you-wait-for-something-to-disappear)
- [100: How would you test a component that loads data when it mounts?](#100-how-would-you-test-a-component-that-loads-data-when-it-mounts)
- [101: Why shouldn't you test implementation details?](#101-why-shouldnt-you-test-implementation-details)
- [102: What are some examples of implementation details in React tests?](#102-what-are-some-examples-of-implementation-details-in-react-tests)
- [103: What is a flaky test?](#103-what-is-a-flaky-test)
- [104: What makes a good test?](#104-what-makes-a-good-test)
- [105: What is test isolation and why does it matter?](#105-what-is-test-isolation-and-why-does-it-matter)
- [106: What is TDD?](#106-what-is-tdd)
- [107: What is BDD?](#107-what-is-bdd)
- [108: What is regression testing?](#108-what-is-regression-testing)
- [109: What is a smoke test?](#109-what-is-a-smoke-test)
- [110: What is Playwright?](#110-what-is-playwright)
- [111: What is Cypress?](#111-what-is-cypress)
- [112: What are the main differences between Playwright and Cypress?](#112-what-are-the-main-differences-between-playwright-and-cypress)
- [113: How do you add Playwright to a project?](#113-how-do-you-add-playwright-to-a-project)
- [114: What does a basic Playwright test look like?](#114-what-does-a-basic-playwright-test-look-like)
- [115: What is the page object in Playwright?](#115-what-is-the-page-object-in-playwright)
- [116: What are locators in Playwright?](#116-what-are-locators-in-playwright)
- [117: What is auto-waiting in Playwright?](#117-what-is-auto-waiting-in-playwright)
- [118: What are web-first assertions?](#118-what-are-web-first-assertions)
- [119: How do you run Playwright tests in headed mode or debug them?](#119-how-do-you-run-playwright-tests-in-headed-mode-or-debug-them)
- [120: What is Playwright codegen?](#120-what-is-playwright-codegen)
- [121: What does a basic Cypress test look like?](#121-what-does-a-basic-cypress-test-look-like)
- [122: How can you use Testing Library queries in Cypress?](#122-how-can-you-use-testing-library-queries-in-cypress)
- [123: What is component testing in Cypress?](#123-what-is-component-testing-in-cypress)
- [124: What are baseURL and webServer in the Playwright config?](#124-what-are-baseurl-and-webserver-in-the-playwright-config)
- [125: Which browsers can Playwright test?](#125-which-browsers-can-playwright-test)
- [126: What is headless mode?](#126-what-is-headless-mode)
- [127: What is a test fixture?](#127-what-is-a-test-fixture)
- [128: What are test data factories?](#128-what-are-test-data-factories)
- [129: What is MSW (Mock Service Worker)?](#129-what-is-msw-mock-service-worker)
- [130: Why use MSW instead of mocking fetch or axios directly?](#130-why-use-msw-instead-of-mocking-fetch-or-axios-directly)
- [131: What is a custom render function and why use it?](#131-what-is-a-custom-render-function-and-why-use-it)
- [132: How do you test a component that uses context?](#132-how-do-you-test-a-component-that-uses-context)
- [133: How do you test a component that uses React Router?](#133-how-do-you-test-a-component-that-uses-react-router)
- [134: How do you test a custom hook?](#134-how-do-you-test-a-custom-hook)
- [135: What does rerender do?](#135-what-does-rerender-do)
- [136: When would you use unmount in a test?](#136-when-would-you-use-unmount-in-a-test)
- [137: How do you test code that uses setTimeout?](#137-how-do-you-test-code-that-uses-settimeout)
- [138: What is container and why should you avoid using it for queries?](#138-what-is-container-and-why-should-you-avoid-using-it-for-queries)
- [139: What is within and when do you use it?](#139-what-is-within-and-when-do-you-use-it)
- [140: How does React Testing Library help with accessibility?](#140-how-does-react-testing-library-help-with-accessibility)
- [141: What are jest-axe and vitest-axe?](#141-what-are-jest-axe-and-vitest-axe)
- [142: How do you test form validation errors?](#142-how-do-you-test-form-validation-errors)
- [143: How do you test a loading state?](#143-how-do-you-test-a-loading-state)
- [144: How do you check which element has focus?](#144-how-do-you-check-which-element-has-focus)
- [145: What does the globals option do in Vitest?](#145-what-does-the-globals-option-do-in-vitest)
- [146: How do you use TypeScript in tests?](#146-how-do-you-use-typescript-in-tests)
- [147: What ESLint plugins help with writing tests?](#147-what-eslint-plugins-help-with-writing-tests)
- [148: Why should tests run in CI?](#148-why-should-tests-run-in-ci)
- [149: How do you run tests in CI mode?](#149-how-do-you-run-tests-in-ci-mode)
- [150: What happened to Enzyme and react-test-renderer?](#150-what-happened-to-enzyme-and-react-test-renderer)

### Moderate Questions (151-300)

- [151: How do you organize tests for a feature?](#151-how-do-you-organize-tests-for-a-feature)
- [152: How does the wrapper option of render work?](#152-how-does-the-wrapper-option-of-render-work)
- [153: How do you test components connected to a Redux Toolkit store?](#153-how-do-you-test-components-connected-to-a-redux-toolkit-store)
- [154: How do you test components that use a Zustand store?](#154-how-do-you-test-components-that-use-a-zustand-store)
- [155: How do you test components that use TanStack Query (React Query)?](#155-how-do-you-test-components-that-use-tanstack-query-react-query)
- [156: How do you test a component that depends on routes and route params?](#156-how-do-you-test-a-component-that-depends-on-routes-and-route-params)
- [157: How do you test that clicking something navigates to another page?](#157-how-do-you-test-that-clicking-something-navigates-to-another-page)
- [158: How do you set up MSW for Vitest or Jest?](#158-how-do-you-set-up-msw-for-vitest-or-jest)
- [159: How do you change an MSW response for just one test?](#159-how-do-you-change-an-msw-response-for-just-one-test)
- [160: How do you test error responses with MSW?](#160-how-do-you-test-error-responses-with-msw)
- [161: What does onUnhandledRequest: "error" do in MSW?](#161-what-does-onunhandledrequest-error-do-in-msw)
- [162: How do you check what request body a component sent?](#162-how-do-you-check-what-request-body-a-component-sent)
- [163: How do you mock fetch without MSW?](#163-how-do-you-mock-fetch-without-msw)
- [164: How do you mock axios?](#164-how-do-you-mock-axios)
- [165: Why does vi.mock get hoisted and what is vi.hoisted for?](#165-why-does-vimock-get-hoisted-and-what-is-vihoisted-for)
- [166: How do you mock only part of a module?](#166-how-do-you-mock-only-part-of-a-module)
- [167: How do you mock a default export?](#167-how-do-you-mock-a-default-export)
- [168: What is the `__mocks__` folder?](#168-what-is-the-__mocks__-folder)
- [169: When does it make sense to mock a child component?](#169-when-does-it-make-sense-to-mock-a-child-component)
- [170: What does vi.mocked do?](#170-what-does-vimocked-do)
- [171: How do you mock environment variables in tests?](#171-how-do-you-mock-environment-variables-in-tests)
- [172: How do you mock global objects and browser APIs?](#172-how-do-you-mock-global-objects-and-browser-apis)
- [173: How do you deal with matchMedia, ResizeObserver and IntersectionObserver missing in jsdom?](#173-how-do-you-deal-with-matchmedia-resizeobserver-and-intersectionobserver-missing-in-jsdom)
- [174: How do you set a fixed date in tests?](#174-how-do-you-set-a-fixed-date-in-tests)
- [175: How do you use fake timers together with user-event?](#175-how-do-you-use-fake-timers-together-with-user-event)
- [176: How do you test a debounced search input?](#176-how-do-you-test-a-debounced-search-input)
- [177: How do you test polling with setInterval?](#177-how-do-you-test-polling-with-setinterval)
- [178: How do you test that an effect cleans up after itself?](#178-how-do-you-test-that-an-effect-cleans-up-after-itself)
- [179: How do you test a custom hook that needs a provider?](#179-how-do-you-test-a-custom-hook-that-needs-a-provider)
- [180: When should you test a hook directly instead of through a component?](#180-when-should-you-test-a-hook-directly-instead-of-through-a-component)
- [181: How do you test a context provider itself?](#181-how-do-you-test-a-context-provider-itself)
- [182: How do you test a form built with React Hook Form?](#182-how-do-you-test-a-form-built-with-react-hook-form)
- [183: How do you test validation logic written with Zod?](#183-how-do-you-test-validation-logic-written-with-zod)
- [184: How do you test a form that uses React 19 actions and useActionState?](#184-how-do-you-test-a-form-that-uses-react-19-actions-and-useactionstate)
- [185: How do you test useOptimistic?](#185-how-do-you-test-useoptimistic)
- [186: How do you test lazy-loaded components with Suspense?](#186-how-do-you-test-lazy-loaded-components-with-suspense)
- [187: How do you test a component that uses the use() API with a promise?](#187-how-do-you-test-a-component-that-uses-the-use-api-with-a-promise)
- [188: How do you test an error boundary?](#188-how-do-you-test-an-error-boundary)
- [189: How do you test a modal that uses a portal?](#189-how-do-you-test-a-modal-that-uses-a-portal)
- [190: How do you test a custom select or combobox component?](#190-how-do-you-test-a-custom-select-or-combobox-component)
- [191: How do you test a data table?](#191-how-do-you-test-a-data-table)
- [192: How do you test keyboard navigation and tab order?](#192-how-do-you-test-keyboard-navigation-and-tab-order)
- [193: How do you test keyboard shortcuts?](#193-how-do-you-test-keyboard-shortcuts)
- [194: How do you test drag and drop?](#194-how-do-you-test-drag-and-drop)
- [195: What are the limits of testing CSS and layout in jsdom?](#195-what-are-the-limits-of-testing-css-and-layout-in-jsdom)
- [196: How do you handle CSS, image and other asset imports in Jest?](#196-how-do-you-handle-css-image-and-other-asset-imports-in-jest)
- [197: How do you configure path aliases like @/components in tests?](#197-how-do-you-configure-path-aliases-like-components-in-tests)
- [198: Why do you get "SyntaxError: Cannot use import statement outside a module" in Jest?](#198-why-do-you-get-syntaxerror-cannot-use-import-statement-outside-a-module-in-jest)
- [199: How do you use different test environments for different files?](#199-how-do-you-use-different-test-environments-for-different-files)
- [200: What are Vitest projects?](#200-what-are-vitest-projects)
- [201: How do you test client components in a Next.js app?](#201-how-do-you-test-client-components-in-a-nextjs-app)
- [202: How do you test React Server Components?](#202-how-do-you-test-react-server-components)
- [203: How do you test Server Actions?](#203-how-do-you-test-server-actions)
- [204: How do you test code that uses localStorage?](#204-how-do-you-test-code-that-uses-localstorage)
- [205: How do you test code that reads or changes window.location?](#205-how-do-you-test-code-that-reads-or-changes-windowlocation)
- [206: How do you test components that use translations (i18n)?](#206-how-do-you-test-components-that-use-translations-i18n)
- [207: What does the "not wrapped in act(...)" warning mean and how do you fix it?](#207-what-does-the-not-wrapped-in-act-warning-mean-and-how-do-you-fix-it)
- [208: What are the most common mistakes people make with React Testing Library?](#208-what-are-the-most-common-mistakes-people-make-with-react-testing-library)
- [209: Why shouldn't you put side effects inside waitFor?](#209-why-shouldnt-you-put-side-effects-inside-waitfor)
- [210: Why should you keep only one assertion in a waitFor callback?](#210-why-should-you-keep-only-one-assertion-in-a-waitfor-callback)
- [211: Why shouldn't you wrap render or user-event calls in act?](#211-why-shouldnt-you-wrap-render-or-user-event-calls-in-act)
- [212: How do you find elements that are hidden from the accessibility tree?](#212-how-do-you-find-elements-that-are-hidden-from-the-accessibility-tree)
- [213: How do you write a custom matcher?](#213-how-do-you-write-a-custom-matcher)
- [214: What are asymmetric matchers?](#214-what-are-asymmetric-matchers)
- [215: How do you test that a function throws or a promise rejects?](#215-how-do-you-test-that-a-function-throws-or-a-promise-rejects)
- [216: What do expect.assertions and expect.hasAssertions do?](#216-what-do-expectassertions-and-expecthasassertions-do)
- [217: How do you test that a component logs a warning?](#217-how-do-you-test-that-a-component-logs-a-warning)
- [218: What are property matchers in snapshots?](#218-what-are-property-matchers-in-snapshots)
- [219: How do you use Faker in tests without making them random?](#219-how-do-you-use-faker-in-tests-without-making-them-random)
- [220: What does a good integration test for a filtered list look like?](#220-what-does-a-good-integration-test-for-a-filtered-list-look-like)
- [221: What should you mock and what should you keep real in an integration test?](#221-what-should-you-mock-and-what-should-you-keep-real-in-an-integration-test)
- [222: What is the difference between shallow rendering and full rendering?](#222-what-is-the-difference-between-shallow-rendering-and-full-rendering)
- [223: How do you set coverage thresholds?](#223-how-do-you-set-coverage-thresholds)
- [224: What is the difference between v8 and istanbul coverage?](#224-what-is-the-difference-between-v8-and-istanbul-coverage)
- [225: How do Vitest and Jest run tests in parallel?](#225-how-do-vitest-and-jest-run-tests-in-parallel)
- [226: How do you split a big test suite across several CI machines?](#226-how-do-you-split-a-big-test-suite-across-several-ci-machines)
- [227: How do you run only the tests affected by your changes?](#227-how-do-you-run-only-the-tests-affected-by-your-changes)
- [228: What is the Vitest UI?](#228-what-is-the-vitest-ui)
- [229: How do you debug a failing test?](#229-how-do-you-debug-a-failing-test)
- [230: How do you test TypeScript types?](#230-how-do-you-test-typescript-types)
- [231: How can Storybook stories be used as tests?](#231-how-can-storybook-stories-be-used-as-tests)
- [232: What is visual regression testing?](#232-what-is-visual-regression-testing)
- [233: How do you run accessibility checks in Playwright?](#233-how-do-you-run-accessibility-checks-in-playwright)
- [234: What are the most important settings in playwright.config.ts?](#234-what-are-the-most-important-settings-in-playwrightconfigts)
- [235: How do you filter and chain locators in Playwright?](#235-how-do-you-filter-and-chain-locators-in-playwright)
- [236: What is strict mode for locators in Playwright?](#236-what-is-strict-mode-for-locators-in-playwright)
- [237: What are expect.poll and toPass in Playwright?](#237-what-are-expectpoll-and-topass-in-playwright)
- [238: What are soft assertions?](#238-what-are-soft-assertions)
- [239: What built-in fixtures does Playwright give you?](#239-what-built-in-fixtures-does-playwright-give-you)
- [240: How do you create a custom fixture in Playwright?](#240-how-do-you-create-a-custom-fixture-in-playwright)
- [241: What is the Page Object Model?](#241-what-is-the-page-object-model)
- [242: How do you avoid logging in through the UI in every Playwright test?](#242-how-do-you-avoid-logging-in-through-the-ui-in-every-playwright-test)
- [243: How do you mock API responses in Playwright?](#243-how-do-you-mock-api-responses-in-playwright)
- [244: How do you change a real API response in Playwright?](#244-how-do-you-change-a-real-api-response-in-playwright)
- [245: What is HAR replay in Playwright?](#245-what-is-har-replay-in-playwright)
- [246: How do you test APIs with Playwright?](#246-how-do-you-test-apis-with-playwright)
- [247: How do you prepare test data for an e2e test?](#247-how-do-you-prepare-test-data-for-an-e2e-test)
- [248: How do you handle browser dialogs and new tabs in Playwright?](#248-how-do-you-handle-browser-dialogs-and-new-tabs-in-playwright)
- [249: How do you test file upload and download in Playwright?](#249-how-do-you-test-file-upload-and-download-in-playwright)
- [250: How do you work with iframes in Playwright?](#250-how-do-you-work-with-iframes-in-playwright)
- [251: How do screenshot comparisons work in Playwright?](#251-how-do-screenshot-comparisons-work-in-playwright)
- [252: What is the Playwright trace viewer?](#252-what-is-the-playwright-trace-viewer)
- [253: How should you handle flaky tests in Playwright?](#253-how-should-you-handle-flaky-tests-in-playwright)
- [254: How does parallelism work in Playwright?](#254-how-does-parallelism-work-in-playwright)
- [255: How do you tag tests and run only some of them?](#255-how-do-you-tag-tests-and-run-only-some-of-them)
- [256: What is test.step in Playwright?](#256-what-is-teststep-in-playwright)
- [257: What annotations does Playwright support?](#257-what-annotations-does-playwright-support)
- [258: How do you emulate different devices, locales and settings in Playwright?](#258-how-do-you-emulate-different-devices-locales-and-settings-in-playwright)
- [259: What timeouts does Playwright have?](#259-what-timeouts-does-playwright-have)
- [260: How do you run Playwright tests in GitHub Actions?](#260-how-do-you-run-playwright-tests-in-github-actions)
- [261: What reporters does Playwright have?](#261-what-reporters-does-playwright-have)
- [262: How does the Cypress command chain work?](#262-how-does-the-cypress-command-chain-work)
- [263: How do you mock network requests in Cypress?](#263-how-do-you-mock-network-requests-in-cypress)
- [264: What are fixtures in Cypress?](#264-what-are-fixtures-in-cypress)
- [265: How do you create custom commands in Cypress?](#265-how-do-you-create-custom-commands-in-cypress)
- [266: What is cy.session?](#266-what-is-cysession)
- [267: How does retry-ability work in Cypress?](#267-how-does-retry-ability-work-in-cypress)
- [268: How do you control time in Cypress?](#268-how-do-you-control-time-in-cypress)
- [269: What are aliases in Cypress and how do you wait on a request?](#269-what-are-aliases-in-cypress-and-how-do-you-wait-on-a-request)
- [270: Why shouldn't you use cy.wait with a number?](#270-why-shouldnt-you-use-cywait-with-a-number)
- [271: What selectors should you use in e2e tests?](#271-what-selectors-should-you-use-in-e2e-tests)
- [272: What should end-to-end tests cover?](#272-what-should-end-to-end-tests-cover)
- [273: Which environment should e2e tests run against?](#273-which-environment-should-e2e-tests-run-against)
- [274: How do you manage test data in e2e tests?](#274-how-do-you-manage-test-data-in-e2e-tests)
- [275: How do you test flows that send emails?](#275-how-do-you-test-flows-that-send-emails)
- [276: How do you test payment flows?](#276-how-do-you-test-payment-flows)
- [277: What is contract testing?](#277-what-is-contract-testing)
- [278: How do you test responsive layouts?](#278-how-do-you-test-responsive-layouts)
- [279: How do you test features behind feature flags?](#279-how-do-you-test-features-behind-feature-flags)
- [280: How do you test that analytics events are sent?](#280-how-do-you-test-that-analytics-events-are-sent)
- [281: How do you test components that use WebSockets?](#281-how-do-you-test-components-that-use-websockets)
- [282: How do you deal with animations in tests?](#282-how-do-you-deal-with-animations-in-tests)
- [283: How do you stop third-party scripts from affecting e2e tests?](#283-how-do-you-stop-third-party-scripts-from-affecting-e2e-tests)
- [284: Should you run tests in a pre-commit hook?](#284-should-you-run-tests-in-a-pre-commit-hook)
- [285: How should you name tests?](#285-how-should-you-name-tests)
- [286: What do you look for when reviewing tests in a pull request?](#286-what-do-you-look-for-when-reviewing-tests-in-a-pull-request)
- [287: How do you fix a bug in a test-driven way?](#287-how-do-you-fix-a-bug-in-a-test-driven-way)
- [288: How do you catch JavaScript errors in the page during e2e tests?](#288-how-do-you-catch-javascript-errors-in-the-page-during-e2e-tests)
- [289: What is Vitest Browser Mode?](#289-what-is-vitest-browser-mode)
- [290: How do you write a component test with vitest-browser-react?](#290-how-do-you-write-a-component-test-with-vitest-browser-react)
- [291: What is component testing in Playwright?](#291-what-is-component-testing-in-playwright)
- [292: When would you choose jsdom and when a real browser for component tests?](#292-when-would-you-choose-jsdom-and-when-a-real-browser-for-component-tests)
- [293: How do you mock GraphQL requests with MSW?](#293-how-do-you-mock-graphql-requests-with-msw)
- [294: How do you test reducers and selectors?](#294-how-do-you-test-reducers-and-selectors)
- [295: How do you test copying to the clipboard?](#295-how-do-you-test-copying-to-the-clipboard)
- [296: How do you check an element's accessible name and description?](#296-how-do-you-check-an-elements-accessible-name-and-description)
- [297: How do you test a protected route?](#297-how-do-you-test-a-protected-route)
- [298: How do you test a component that reads and updates URL search params?](#298-how-do-you-test-a-component-that-reads-and-updates-url-search-params)
- [299: How do you keep MSW handlers organized in a big app?](#299-how-do-you-keep-msw-handlers-organized-in-a-big-app)
- [300: What is the difference between using MSW and page.route for mocking in e2e tests?](#300-what-is-the-difference-between-using-msw-and-pageroute-for-mocking-in-e2e-tests)

### Advanced Questions (301-450)

- [301: What does React Testing Library's render actually do under the hood?](#301-what-does-react-testing-librarys-render-actually-do-under-the-hood)
- [302: How does act work in React 19, and what is IS_REACT_ACT_ENVIRONMENT?](#302-how-does-act-work-in-react-19-and-what-is-is_react_act_environment)
- [303: How do waitFor and findBy work internally?](#303-how-do-waitfor-and-findby-work-internally)
- [304: How does user-event simulate interactions?](#304-how-does-user-event-simulate-interactions)
- [305: What browser features are missing or different in jsdom?](#305-what-browser-features-are-missing-or-different-in-jsdom)
- [306: Why can a test pass in jsdom but the feature still be broken in the browser?](#306-why-can-a-test-pass-in-jsdom-but-the-feature-still-be-broken-in-the-browser)
- [307: How does module mocking work in Vitest?](#307-how-does-module-mocking-work-in-vitest)
- [308: How does Jest's module registry work, and what are resetModules and isolateModules?](#308-how-does-jests-module-registry-work-and-what-are-resetmodules-and-isolatemodules)
- [309: How do you mock ES modules in Jest?](#309-how-do-you-mock-es-modules-in-jest)
- [310: What are the different pools in Vitest?](#310-what-are-the-different-pools-in-vitest)
- [311: What are the typical ways state leaks between tests?](#311-what-are-the-typical-ways-state-leaks-between-tests)
- [312: How do fake timers work?](#312-how-do-fake-timers-work)
- [313: Why can waitFor or findBy hang when fake timers are on, and how do you fix it?](#313-why-can-waitfor-or-findby-hang-when-fake-timers-are-on-and-how-do-you-fix-it)
- [314: How do you track down a flaky unit test?](#314-how-do-you-track-down-a-flaky-unit-test)
- [315: How do you track down a flaky e2e test?](#315-how-do-you-track-down-a-flaky-e2e-test)
- [316: What problems do floating promises cause in tests?](#316-what-problems-do-floating-promises-cause-in-tests)
- [317: How do you find memory leaks or open handles in a test suite?](#317-how-do-you-find-memory-leaks-or-open-handles-in-a-test-suite)
- [318: How do you speed up a slow Jest suite?](#318-how-do-you-speed-up-a-slow-jest-suite)
- [319: How do you speed up a slow Vitest suite?](#319-how-do-you-speed-up-a-slow-vitest-suite)
- [320: How would you migrate a project from Jest to Vitest?](#320-how-would-you-migrate-a-project-from-jest-to-vitest)
- [321: How would you migrate a large Enzyme test suite to React Testing Library?](#321-how-would-you-migrate-a-large-enzyme-test-suite-to-react-testing-library)
- [322: What would you consider when moving an e2e suite from Cypress to Playwright?](#322-what-would-you-consider-when-moving-an-e2e-suite-from-cypress-to-playwright)
- [323: How would you design a testing strategy for a large React application?](#323-how-would-you-design-a-testing-strategy-for-a-large-react-application)
- [324: How do you decide whether something needs a unit, integration or e2e test?](#324-how-do-you-decide-whether-something-needs-a-unit-integration-or-e2e-test)
- [325: Where should the mocking boundary be in front-end tests?](#325-where-should-the-mocking-boundary-be-in-front-end-tests)
- [326: How do you organize tests in a monorepo?](#326-how-do-you-organize-tests-in-a-monorepo)
- [327: How would you design a shared test utilities package?](#327-how-would-you-design-a-shared-test-utilities-package)
- [328: How does consumer-driven contract testing with Pact work in a React project?](#328-how-does-consumer-driven-contract-testing-with-pact-work-in-a-react-project)
- [329: How do you keep API mocks in sync with the real API?](#329-how-do-you-keep-api-mocks-in-sync-with-the-real-api)
- [330: How do you write type-safe mocks?](#330-how-do-you-write-type-safe-mocks)
- [331: How do you test components that use useTransition or useDeferredValue?](#331-how-do-you-test-components-that-use-usetransition-or-usedeferredvalue)
- [332: How do you test streaming SSR and Server Components?](#332-how-do-you-test-streaming-ssr-and-server-components)
- [333: How do you catch hydration mismatches in tests?](#333-how-do-you-catch-hydration-mismatches-in-tests)
- [334: How do you test server-rendered HTML output?](#334-how-do-you-test-server-rendered-html-output)
- [335: How are render errors reported in React 19 and how does that affect tests?](#335-how-are-render-errors-reported-in-react-19-and-how-does-that-affect-tests)
- [336: Does the React Compiler change how you write tests?](#336-does-the-react-compiler-change-how-you-write-tests)
- [337: Should you test how many times a component re-renders?](#337-should-you-test-how-many-times-a-component-re-renders)
- [338: How do you include performance checks in automated testing?](#338-how-do-you-include-performance-checks-in-automated-testing)
- [339: How do you test that a component handles out-of-order responses correctly?](#339-how-do-you-test-that-a-component-handles-out-of-order-responses-correctly)
- [340: How do you test that a request is cancelled with AbortController?](#340-how-do-you-test-that-a-request-is-cancelled-with-abortcontroller)
- [341: How do you test retry logic?](#341-how-do-you-test-retry-logic)
- [342: How do you test RTK Query endpoints?](#342-how-do-you-test-rtk-query-endpoints)
- [343: How do you test infinite scrolling?](#343-how-do-you-test-infinite-scrolling)
- [344: How do you test virtualized lists?](#344-how-do-you-test-virtualized-lists)
- [345: How do you test charts and canvas-based components?](#345-how-do-you-test-charts-and-canvas-based-components)
- [346: How do you test a component that wraps a rich text editor?](#346-how-do-you-test-a-component-that-wraps-a-rich-text-editor)
- [347: What problems do you hit when testing components built with third-party UI libraries?](#347-what-problems-do-you-hit-when-testing-components-built-with-third-party-ui-libraries)
- [348: How do you test code that uses Web Workers?](#348-how-do-you-test-code-that-uses-web-workers)
- [349: How do you test offline behavior and service workers?](#349-how-do-you-test-offline-behavior-and-service-workers)
- [350: How do you test login with an external OAuth provider in e2e tests?](#350-how-do-you-test-login-with-an-external-oauth-provider-in-e2e-tests)
- [351: How do you test a scenario with two users in Playwright?](#351-how-do-you-test-a-scenario-with-two-users-in-playwright)
- [352: How would you test real-time collaboration features?](#352-how-would-you-test-real-time-collaboration-features)
- [353: How does Playwright control browsers?](#353-how-does-playwright-control-browsers)
- [354: What is a browser context and why is it cheap?](#354-what-is-a-browser-context-and-why-is-it-cheap)
- [355: What are worker-scoped fixtures and when do you use them?](#355-what-are-worker-scoped-fixtures-and-when-do-you-use-them)
- [356: How do you run e2e tests in parallel against one shared backend without conflicts?](#356-how-do-you-run-e2e-tests-in-parallel-against-one-shared-backend-without-conflicts)
- [357: How do you run a big Playwright suite across many CI machines and get one report?](#357-how-do-you-run-a-big-playwright-suite-across-many-ci-machines-and-get-one-report)
- [358: What is test quarantine and how should it work?](#358-what-is-test-quarantine-and-how-should-it-work)
- [359: How does Cypress work internally and what limits does that cause?](#359-how-does-cypress-work-internally-and-what-limits-does-that-cause)
- [360: How would you choose an e2e tool for a new React project?](#360-how-would-you-choose-an-e2e-tool-for-a-new-react-project)
- [361: How do you make visual regression testing work at scale?](#361-how-do-you-make-visual-regression-testing-work-at-scale)
- [362: What are ARIA snapshots in Playwright?](#362-what-are-aria-snapshots-in-playwright)
- [363: What does a good accessibility testing strategy look like, and what can't automation catch?](#363-what-does-a-good-accessibility-testing-strategy-look-like-and-what-cant-automation-catch)
- [364: How do you test focus management in a modal dialog?](#364-how-do-you-test-focus-management-in-a-modal-dialog)
- [365: How can tests help with front-end security?](#365-how-can-tests-help-with-front-end-security)
- [366: How do you test security headers and Content Security Policy?](#366-how-do-you-test-security-headers-and-content-security-policy)
- [367: What is mutation testing?](#367-what-is-mutation-testing)
- [368: What is property-based testing and where is it useful in front-end code?](#368-what-is-property-based-testing-and-where-is-it-useful-in-front-end-code)
- [369: How do you measure test quality beyond coverage?](#369-how-do-you-measure-test-quality-beyond-coverage)
- [370: Can you combine coverage from unit tests and e2e tests?](#370-can-you-combine-coverage-from-unit-tests-and-e2e-tests)
- [371: What is synthetic monitoring?](#371-what-is-synthetic-monitoring)
- [372: How do you test micro-frontends?](#372-how-do-you-test-micro-frontends)
- [373: How do you test a design system component library?](#373-how-do-you-test-a-design-system-component-library)
- [374: How do Storybook interaction tests and the Vitest addon work together?](#374-how-do-storybook-interaction-tests-and-the-vitest-addon-work-together)
- [375: How do you test right-to-left layouts and translation edge cases?](#375-how-do-you-test-right-to-left-layouts-and-translation-edge-cases)
- [376: How do you make tests independent of the machine's time zone?](#376-how-do-you-make-tests-independent-of-the-machines-time-zone)
- [377: Why can Intl formatting give different results in tests and in the browser?](#377-why-can-intl-formatting-give-different-results-in-tests-and-in-the-browser)
- [378: How do you test a date picker?](#378-how-do-you-test-a-date-picker)
- [379: How do you write a custom query in React Testing Library?](#379-how-do-you-write-a-custom-query-in-react-testing-library)
- [380: What can you change with RTL's configure function?](#380-what-can-you-change-with-rtls-configure-function)
- [381: How do you type a custom render function with extra options?](#381-how-do-you-type-a-custom-render-function-with-extra-options)
- [382: How do you test a hook built on useSyncExternalStore?](#382-how-do-you-test-a-hook-built-on-usesyncexternalstore)
- [383: How do you test a component that exposes methods with useImperativeHandle?](#383-how-do-you-test-a-component-that-exposes-methods-with-useimperativehandle)
- [384: How do you test code that calls scrollIntoView or scrolls the page?](#384-how-do-you-test-code-that-calls-scrollintoview-or-scrolls-the-page)
- [385: How do you test a feature that downloads a generated file in a unit test?](#385-how-do-you-test-a-feature-that-downloads-a-generated-file-in-a-unit-test)
- [386: How do you test features that need browser permissions in Playwright?](#386-how-do-you-test-features-that-need-browser-permissions-in-playwright)
- [387: How do you test video and audio components?](#387-how-do-you-test-video-and-audio-components)
- [388: How do you test error tracking and global error handling?](#388-how-do-you-test-error-tracking-and-global-error-handling)
- [389: How do you make tests fail on unexpected console errors?](#389-how-do-you-make-tests-fail-on-unexpected-console-errors)
- [390: What happens with unhandled promise rejections in tests?](#390-what-happens-with-unhandled-promise-rejections-in-tests)
- [391: How do you investigate a test that hangs until it times out?](#391-how-do-you-investigate-a-test-that-hangs-until-it-times-out)
- [392: How do you test code that uses random values like crypto.randomUUID or Math.random?](#392-how-do-you-test-code-that-uses-random-values-like-cryptorandomuuid-or-mathrandom)
- [393: Why can useId or generated IDs break snapshot tests?](#393-why-can-useid-or-generated-ids-break-snapshot-tests)
- [394: A test passes locally but fails in CI. How do you debug it?](#394-a-test-passes-locally-but-fails-in-ci-how-do-you-debug-it)
- [395: Your e2e suite takes 40 minutes. How do you make it faster?](#395-your-e2e-suite-takes-40-minutes-how-do-you-make-it-faster)
- [396: Your team has hundreds of large snapshot tests that everybody just updates. What do you do?](#396-your-team-has-hundreds-of-large-snapshot-tests-that-everybody-just-updates-what-do-you-do)
- [397: You join a project with a large React app and no tests. Where do you start?](#397-you-join-a-project-with-a-large-react-app-and-no-tests-where-do-you-start)
- [398: A component is very hard to test. What does that tell you and how do you fix it?](#398-a-component-is-very-hard-to-test-what-does-that-tell-you-and-how-do-you-fix-it)
- [399: All tests pass, but the app is broken in production. What went wrong and how do you prevent it?](#399-all-tests-pass-but-the-app-is-broken-in-production-what-went-wrong-and-how-do-you-prevent-it)
- [400: How would you test a checkout flow end to end?](#400-how-would-you-test-a-checkout-flow-end-to-end)
- [401: How would you test a search autocomplete component?](#401-how-would-you-test-a-search-autocomplete-component)
- [402: How would you test a multi-step form wizard?](#402-how-would-you-test-a-multi-step-form-wizard)
- [403: How would you test UI that depends on user roles and permissions?](#403-how-would-you-test-ui-that-depends-on-user-roles-and-permissions)
- [404: How would you test a dashboard with charts and filters?](#404-how-would-you-test-a-dashboard-with-charts-and-filters)
- [405: How would you test a file upload with a progress bar?](#405-how-would-you-test-a-file-upload-with-a-progress-bar)
- [406: How would you test a table with server-side sorting and pagination?](#406-how-would-you-test-a-table-with-server-side-sorting-and-pagination)
- [407: How would you test toast notifications that disappear automatically?](#407-how-would-you-test-toast-notifications-that-disappear-automatically)
- [408: How would you test a component that uses a third-party map SDK?](#408-how-would-you-test-a-component-that-uses-a-third-party-map-sdk)
- [409: How would you test a countdown timer?](#409-how-would-you-test-a-countdown-timer)
- [410: How would you test an undo and redo feature?](#410-how-would-you-test-an-undo-and-redo-feature)
- [411: How do you make React components easier to test with dependency injection?](#411-how-do-you-make-react-components-easier-to-test-with-dependency-injection)
- [412: Should e2e tests use a real backend or a mocked one?](#412-should-e2e-tests-use-a-real-backend-or-a-mocked-one)
- [413: How do you give each e2e run its own backend environment?](#413-how-do-you-give-each-e2e-run-its-own-backend-environment)
- [414: How do you reset the database between e2e tests?](#414-how-do-you-reset-the-database-between-e2e-tests)
- [415: What are global setup and teardown in Playwright and Vitest?](#415-what-are-global-setup-and-teardown-in-playwright-and-vitest)
- [416: How do you run the same Playwright suite against different environments?](#416-how-do-you-run-the-same-playwright-suite-against-different-environments)
- [417: How should you handle secrets in e2e tests?](#417-how-should-you-handle-secrets-in-e2e-tests)
- [418: What is the difference between page.route and context.route, and which route wins when several match?](#418-what-is-the-difference-between-pageroute-and-contextroute-and-which-route-wins-when-several-match)
- [419: How do you control time in Playwright tests?](#419-how-do-you-control-time-in-playwright-tests)
- [420: How would you test session expiry and token refresh?](#420-how-would-you-test-session-expiry-and-token-refresh)
- [421: How do you test what happens when a lazy-loaded chunk fails to load?](#421-how-do-you-test-what-happens-when-a-lazy-loaded-chunk-fails-to-load)
- [422: Can AI tools write and fix your e2e tests?](#422-can-ai-tools-write-and-fix-your-e2e-tests)
- [423: What are common problems with unit tests written by AI assistants?](#423-what-are-common-problems-with-unit-tests-written-by-ai-assistants)
- [424: How do you track test health over time?](#424-how-do-you-track-test-health-over-time)
- [425: In what order should checks run in a CI pipeline?](#425-in-what-order-should-checks-run-in-a-ci-pipeline)
- [426: How do you run e2e tests against pull request preview deployments?](#426-how-do-you-run-e2e-tests-against-pull-request-preview-deployments)
- [427: How do you decide which browsers to run e2e tests on?](#427-how-do-you-decide-which-browsers-to-run-e2e-tests-on)
- [428: Is mobile emulation in Playwright enough to test mobile users?](#428-is-mobile-emulation-in-playwright-enough-to-test-mobile-users)
- [429: How do you test web components used inside React?](#429-how-do-you-test-web-components-used-inside-react)
- [430: How can state machines help with testing?](#430-how-can-state-machines-help-with-testing)
- [431: How do you test that a TanStack Query mutation updates or invalidates the right data?](#431-how-do-you-test-that-a-tanstack-query-mutation-updates-or-invalidates-the-right-data)
- [432: For an Apollo Client app, should you use MockedProvider or MSW?](#432-for-an-apollo-client-app-should-you-use-mockedprovider-or-msw)
- [433: How do you test inputs from third-party libraries like masked inputs or custom number fields?](#433-how-do-you-test-inputs-from-third-party-libraries-like-masked-inputs-or-custom-number-fields)
- [434: How can you split tests across CI machines more evenly?](#434-how-can-you-split-tests-across-ci-machines-more-evenly)
- [435: How do you keep a test suite maintainable over several years?](#435-how-do-you-keep-a-test-suite-maintainable-over-several-years)
- [436: When should you delete a test?](#436-when-should-you-delete-a-test)
- [437: How would you convince a team to invest more in testing?](#437-how-would-you-convince-a-team-to-invest-more-in-testing)
- [438: How do you test theming and dark mode?](#438-how-do-you-test-theming-and-dark-mode)
- [439: How do you test page titles and meta tags?](#439-how-do-you-test-page-titles-and-meta-tags)
- [440: Why should e2e tests run against a production build instead of the dev server?](#440-why-should-e2e-tests-run-against-a-production-build-instead-of-the-dev-server)
- [441: How does React StrictMode affect your tests?](#441-how-does-react-strictmode-affect-your-tests)
- [442: How can you catch memory leaks in a React app with automated tests?](#442-how-can-you-catch-memory-leaks-in-a-react-app-with-automated-tests)
- [443: How do you test error handling in components that use Suspense for data?](#443-how-do-you-test-error-handling-in-components-that-use-suspense-for-data)
- [444: How do you test a form that sends multipart data with a file to the API?](#444-how-do-you-test-a-form-that-sends-multipart-data-with-a-file-to-the-api)
- [445: How do you test React Router loaders and actions?](#445-how-do-you-test-react-router-loaders-and-actions)
- [446: How do you test a feature with many combinations of options without writing hundreds of tests?](#446-how-do-you-test-a-feature-with-many-combinations-of-options-without-writing-hundreds-of-tests)
- [447: How do you test a feature that is still changing a lot?](#447-how-do-you-test-a-feature-that-is-still-changing-a-lot)
- [448: How is testing a reusable library component different from testing an app component?](#448-how-is-testing-a-reusable-library-component-different-from-testing-an-app-component)
- [449: How do you test screen reader announcements with aria-live?](#449-how-do-you-test-screen-reader-announcements-with-aria-live)
- [450: Walk me through how you would test a new feature from start to finish.](#450-walk-me-through-how-you-would-test-a-new-feature-from-start-to-finish)

---

## Easy Questions (1-150)

### 1: Why do we write tests for a React app?

Tests let you change code without being afraid of breaking something. If you refactor a component, update a library or fix a bug, the tests tell you quickly if something that used to work is now broken.

They also act as documentation. A good test shows how a component is supposed to be used and what it should do. And they save time in the long run, because catching a bug on your machine is much cheaper than catching it in production.

### 2: What is the testing pyramid?

The testing pyramid is an old and well known way to think about how many tests of each type you should have:

- Lots of **unit tests** at the bottom. They are fast and cheap.
- Fewer **integration tests** in the middle.
- A small number of **end-to-end tests** at the top. They are slow and more expensive to maintain.

The idea is that the higher you go, the slower and more fragile the tests get, so you keep fewer of them.

### 3: What is the testing trophy?

The testing trophy is an idea from Kent C. Dodds, the author of React Testing Library. From bottom to top it has:

1. **Static** checks (TypeScript, ESLint)
2. **Unit** tests
3. **Integration** tests (the biggest part)
4. **End-to-end** tests

The main difference from the pyramid is that integration tests get the most attention. For front-end code, testing several components together the way a user uses them gives you a lot of confidence for a reasonable cost.

### 4: What is the difference between unit, integration and end-to-end tests?

- **Unit test**: tests one small piece in isolation, like a utility function, a hook or a single component. Its dependencies are usually mocked.
- **Integration test**: tests several pieces working together, like a page component with its child components, context and a mocked API.
- **End-to-end (e2e) test**: tests the whole app in a real browser, usually with a real or close to real backend, by clicking and typing like a user.

As you move from unit to e2e, tests become slower and harder to debug, but they give you more confidence that the real app works.

### 5: What does a unit test look like in a React project?

In React a unit test usually checks a pure function, a custom hook or a small component on its own.

```ts
// formatPrice.ts
export function formatPrice(cents: number) {
  return `$${(cents / 100).toFixed(2)}`;
}

// formatPrice.test.ts
import { expect, test } from "vitest";
import { formatPrice } from "./formatPrice";

test("formats cents as dollars", () => {
  expect(formatPrice(1999)).toBe("$19.99");
});
```

It runs in milliseconds and does not need a browser, a server or other components.

### 6: What does an integration test look like in a React project?

An integration test renders a bigger part of the UI, for example a whole form or page, with its real child components, and only mocks the edges like the network.

```tsx
test("shows the user after login", async () => {
  const user = userEvent.setup();
  render(<LoginPage />); // real form, real inputs, real validation

  await user.type(screen.getByLabelText(/email/i), "anna@test.com");
  await user.type(screen.getByLabelText(/password/i), "secret123");
  await user.click(screen.getByRole("button", { name: /log in/i }));

  expect(await screen.findByText(/welcome, anna/i)).toBeInTheDocument();
});
```

The API call is answered by a mock (for example MSW), but everything inside React runs for real.

### 7: What is an end-to-end test?

An e2e test runs your real app in a real browser and goes through a full user flow, like signing up, adding a product to the cart and paying. Tools like Playwright and Cypress open the browser, click buttons, fill inputs and check what shows up on the page.

E2E tests catch problems that other tests miss, like broken routing, wrong environment config, CORS errors or a backend that changed its response. The downside is that they are slower and can be flaky if they are not written carefully.

### 8: Why are TypeScript and ESLint called "static tests"?

They find bugs without running the code. TypeScript catches things like passing a string where a number is expected or forgetting a required prop. ESLint catches things like missing hook dependencies, unused variables or calling hooks inside conditions.

They are the cheapest kind of check you can have, because they run in your editor while you type. They don't replace tests, but they remove a whole class of bugs you would otherwise need tests for.

### 9: What tools are commonly used to test React apps today?

- **Test runners**: Vitest (very common in Vite projects) and Jest.
- **Component testing**: React Testing Library together with `@testing-library/user-event` and `@testing-library/jest-dom`.
- **DOM environment**: jsdom or happy-dom, or a real browser with Vitest Browser Mode.
- **API mocking**: Mock Service Worker (MSW).
- **E2E**: Playwright and Cypress.
- **Others**: Storybook for component stories and interaction tests, axe for accessibility checks.

Enzyme used to be popular but it's no longer maintained and doesn't support modern React.

### 10: What is a test runner?

A test runner is the tool that finds your test files, runs them and reports which tests passed or failed. It usually also gives you `describe`, `test`, `expect`, mocking helpers, watch mode and code coverage.

Jest and Vitest are the two main test runners for React unit and integration tests. Playwright and Cypress have their own runners for e2e tests.

### 11: What is Jest?

Jest is a JavaScript test runner created by Facebook (Meta). For years it was the default choice for React because Create React App shipped with it. It includes everything in one package: the runner, assertions (`expect`), mocks, fake timers, snapshot testing and coverage.

The current major version is Jest 30. Jest is still widely used, especially in older projects and in React Native, but many new web projects now use Vitest.

### 12: What is Vitest?

Vitest is a test runner built on top of Vite. It uses the same config and plugins as your Vite app, so things like TypeScript, JSX, path aliases and CSS imports just work without extra setup.

Its API is almost the same as Jest (`describe`, `test`, `expect`, `vi.fn()` instead of `jest.fn()`), so it is easy to switch. It is fast, supports ESM out of the box and, since Vitest 4, has a stable Browser Mode that runs tests in a real browser.

### 13: How do you choose between Jest and Vitest?

- If the project uses **Vite** (or a framework built on Vite), Vitest is the natural choice. You reuse the same config and avoid a second build setup.
- If the project already has a **large Jest suite** that works fine, there is often no strong reason to migrate.
- **React Native** projects usually stay on Jest because the tooling is built around it.
- If you have **ESM-heavy dependencies**, Vitest is usually less painful, because ESM support in Jest still needs extra config.

For a new React web project in 2026, most people pick Vitest.

### 14: What is React Testing Library?

React Testing Library (RTL), the `@testing-library/react` package, is a set of helpers for rendering React components in tests and finding elements on the page. It is built on top of `@testing-library/dom`.

It doesn't give you access to component state or instance methods. Instead you find elements the way a user would, by their role, label or text, and you check what the user would see. The current major version is 16, which supports React 18 and 19.

### 15: What is the main idea behind React Testing Library?

The guiding principle is: "The more your tests resemble the way your software is used, the more confidence they can give you."

In practice this means you test behavior, not implementation. You don't check that `useState` was called or that a prop has some value. You click a button and check that the right text shows up. Because of this, you can refactor a component (for example, switch from `useState` to `useReducer`) and the tests still pass as long as the behavior is the same.

### 16: What is jsdom?

jsdom is a JavaScript implementation of the DOM and many browser APIs that runs in Node.js. It lets you render React components and query the DOM in tests without opening a real browser.

It's not a real browser, though. It doesn't do layout or rendering, so things like `getBoundingClientRect`, CSS media queries, scrolling and `IntersectionObserver` either return fake values or are missing. You set it with `environment: "jsdom"` in Vitest or `testEnvironment: "jsdom"` in Jest.

### 17: What is happy-dom?

happy-dom is another DOM implementation for Node.js, like jsdom. It is usually faster than jsdom but covers fewer browser APIs and behaves slightly differently in some edge cases.

In Vitest you can switch to it with `environment: "happy-dom"`. Many teams try it to speed up their suite, and switch back to jsdom if they hit a missing API or a difference that breaks their tests.

### 18: Why do you need a DOM environment to test React components?

React DOM renders components into real DOM nodes using `document.createElement`, `appendChild` and so on. Node.js doesn't have a `document` or `window`, so without a DOM environment the render would fail.

jsdom or happy-dom add these globals. Tests for pure functions or reducers don't need them and can run in the plain `node` environment, which is faster.

### 19: How do you set up Vitest and React Testing Library in a Vite React project?

Install the packages:

```bash
npm install -D vitest jsdom @testing-library/react @testing-library/dom @testing-library/user-event @testing-library/jest-dom
```

Add a `test` section to the Vite config:

```ts
// vite.config.ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: "./src/setupTests.ts",
  },
});
```

```ts
// src/setupTests.ts
import "@testing-library/jest-dom/vitest";
```

Then add `"test": "vitest"` to your `package.json` scripts. Note that RTL 16 needs `@testing-library/dom` installed separately as a peer dependency.

### 20: How do you set up Jest for a React project with TypeScript?

You need Jest, a jsdom environment and something to transform TS and JSX (Babel, `ts-jest` or `@swc/jest`).

```bash
npm install -D jest jest-environment-jsdom @swc/jest @testing-library/react @testing-library/dom @testing-library/user-event @testing-library/jest-dom
```

```js
// jest.config.js
module.exports = {
  testEnvironment: "jsdom",
  transform: { "^.+\\.(t|j)sx?$": "@swc/jest" },
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
  moduleNameMapper: {
    "\\.(css|scss)$": "identity-obj-proxy",
  },
};
```

```ts
// jest.setup.ts
import "@testing-library/jest-dom";
```

Since Jest 28, `jest-environment-jsdom` is not bundled, so you have to install it yourself.

### 21: What is a setup file in Vitest or Jest?

A setup file is code that runs before each test file. You use it for global things every test needs, like:

- importing jest-dom matchers
- starting the MSW server
- adding polyfills or mocks for browser APIs jsdom doesn't have (`matchMedia`, `ResizeObserver`)
- global `afterEach` cleanup

In Vitest it's `test.setupFiles`. In Jest there are two options: `setupFiles` runs before the test framework is installed, and `setupFilesAfterEnv` runs after it, so you can use `expect` and `beforeEach` there. Most setup goes in `setupFilesAfterEnv`.

### 22: What is @testing-library/jest-dom?

It's a package of extra matchers for checking DOM elements, like `toBeInTheDocument()`, `toBeVisible()`, `toHaveTextContent()`, `toBeDisabled()` and `toHaveValue()`.

Without it you would write things like `expect(button.disabled).toBe(true)`. With it you write `expect(button).toBeDisabled()`, which reads better and gives clearer error messages. Despite the name, it works with Vitest too. You import `@testing-library/jest-dom/vitest` in the Vitest setup file.

### 23: How should test files be named?

The usual convention is to put `.test.` or `.spec.` before the extension: `Button.test.tsx`, `useCart.test.ts`, `checkout.spec.ts`. Vitest and Jest find these files automatically.

Many teams use `.test.` for unit and integration tests and `.spec.` for Playwright e2e tests, so the two runners don't pick up each other's files. Whatever you choose, keep it the same across the project.

### 24: Where should you put test files?

There are two common options:

- **Next to the code**: `Button.tsx` and `Button.test.tsx` in the same folder. It's easy to find the test and you notice right away when a component has no test.
- **In a `__tests__` folder** inside each feature folder.

For React components, most teams put tests next to the code. E2E tests usually go in a separate top-level folder like `e2e/` or `tests/`, because they test the whole app and not one file.

### 25: What is the basic structure of a test?

```ts
import { describe, test, expect } from "vitest";

describe("sum", () => {
  test("adds two numbers", () => {
    expect(sum(1, 2)).toBe(3);
  });

  test("returns 0 for no numbers", () => {
    expect(sum()).toBe(0);
  });
});
```

- `describe` groups related tests.
- `test` (or `it`) defines one test case with a name and a function.
- `expect` makes an assertion. If it fails, the test fails.

### 26: What is the difference between test and it?

There is no difference. `it` is an alias for `test`. Some people use `it` because the name reads like a sentence: `it("renders the title")`. Others use `test` because it is clearer. Pick one and use it everywhere in the project.

### 27: What is an assertion?

An assertion is a check that a value is what you expect. If the check fails, it throws an error and the test fails.

```ts
expect(total).toBe(30);
expect(screen.getByRole("alert")).toHaveTextContent("Required");
```

A test without assertions only checks that the code doesn't throw, which is rarely enough.

### 28: What is the difference between toBe and toEqual?

`toBe` checks with `Object.is`, which means for objects and arrays it checks that both values are the **same reference**. `toEqual` checks that the values have the **same content**, recursively.

```ts
expect(2 + 2).toBe(4); // ok

const a = { id: 1 };
expect(a).toBe({ id: 1 }); // fails, different objects
expect(a).toEqual({ id: 1 }); // passes
```

Use `toBe` for primitives and `toEqual` for objects and arrays.

### 29: What is the difference between toEqual and toStrictEqual?

`toStrictEqual` is stricter:

- it fails if one object has a key with `undefined` and the other doesn't have the key at all
- it checks that class instances have the same type
- it treats sparse arrays differently (`[, 1]` is not equal to `[undefined, 1]`)

```ts
expect({ a: 1, b: undefined }).toEqual({ a: 1 }); // passes
expect({ a: 1, b: undefined }).toStrictEqual({ a: 1 }); // fails
```

### 30: What are some common matchers in Vitest and Jest?

- `toBe`, `toEqual`, `toStrictEqual` for equality
- `toBeTruthy`, `toBeFalsy`, `toBeNull`, `toBeUndefined`, `toBeDefined`
- `toBeGreaterThan`, `toBeLessThanOrEqual`, `toBeCloseTo` (for floats)
- `toContain` (item in array or substring), `toHaveLength`, `toHaveProperty`
- `toMatch` (regex or substring)
- `toThrow` (for functions that throw)
- `toHaveBeenCalled`, `toHaveBeenCalledWith`, `toHaveBeenCalledTimes` (for mocks)
- `resolves` and `rejects` (for promises)

### 31: How do you check that something is NOT true?

Put `.not` before the matcher:

```ts
expect(items).not.toContain("banana");
expect(onSubmit).not.toHaveBeenCalled();
expect(screen.queryByText("Error")).not.toBeInTheDocument();
```

### 32: What is the Arrange, Act, Assert pattern?

It's a simple way to structure a test in three parts:

1. **Arrange**: set up the data and render the component.
2. **Act**: do something, like click a button.
3. **Assert**: check the result.

```tsx
test("adds an item to the list", async () => {
  // Arrange
  const user = userEvent.setup();
  render(<TodoList />);

  // Act
  await user.type(screen.getByRole("textbox"), "Buy milk");
  await user.click(screen.getByRole("button", { name: "Add" }));

  // Assert
  expect(screen.getByRole("listitem")).toHaveTextContent("Buy milk");
});
```

It makes tests easy to read because everyone knows where to look for each part.

### 33: How do you render a component with React Testing Library?

Call `render` with JSX:

```tsx
import { render, screen } from "@testing-library/react";
import { Greeting } from "./Greeting";

test("shows the name", () => {
  render(<Greeting name="Anna" />);
  expect(screen.getByText("Hello, Anna")).toBeInTheDocument();
});
```

`render` creates a `div`, adds it to `document.body` and renders your component into it using `createRoot`. It wraps everything in `act` so effects run before your assertions.

### 34: What does render return?

It returns an object with:

- query functions bound to the container (`getByText`, `getByRole`, etc.)
- `container`: the `div` your component was rendered into
- `baseElement`: by default `document.body`
- `rerender(ui)`: render again with new props
- `unmount()`: unmount the component
- `debug()`: print the DOM
- `asFragment()`: a `DocumentFragment` you can snapshot

Most of the time you only need `rerender` or `unmount` from it and use `screen` for queries.

### 35: What is screen and why should you use it?

`screen` is an object exported from React Testing Library that has all the queries bound to `document.body`.

```tsx
render(<LoginForm />);
screen.getByRole("button", { name: /log in/i });
```

The Testing Library docs recommend `screen` over destructuring queries from `render`. You don't have to update the destructuring every time you need a new query, and it also finds things rendered in portals (like modals) that are outside the component's container.

### 36: What are queries in React Testing Library?

Queries are functions for finding elements on the page. Each query is a combination of:

- a **type**: `getBy`, `queryBy`, `findBy` and their `All` versions
- a **what to search by**: `Role`, `LabelText`, `PlaceholderText`, `Text`, `DisplayValue`, `AltText`, `Title`, `TestId`

So you get names like `getByRole`, `queryByText` or `findAllByLabelText`.

### 37: What is the difference between getBy, queryBy and findBy?

| Query     | No match       | 1 match         | More than 1 match | Async |
| --------- | -------------- | --------------- | ----------------- | ----- |
| `getBy`   | throws         | returns element | throws            | no    |
| `queryBy` | returns `null` | returns element | throws            | no    |
| `findBy`  | rejects        | resolves        | rejects           | yes   |

- Use `getBy` when the element should be there right now.
- Use `queryBy` when you want to check that something is **not** there.
- Use `findBy` when the element shows up later, for example after a fetch.

### 38: What do the "All" queries do?

`getAllBy`, `queryAllBy` and `findAllBy` return an array of all matching elements instead of one.

```tsx
const items = screen.getAllByRole("listitem");
expect(items).toHaveLength(3);
expect(items[0]).toHaveTextContent("Milk");
```

`getAllBy` throws if nothing matches. `queryAllBy` returns an empty array. `findAllBy` waits until at least one element matches.

### 39: In what order should you prefer the queries?

The Testing Library docs give this order:

1. **Queries everyone can use**: `getByRole`, `getByLabelText`, `getByPlaceholderText`, `getByText`, `getByDisplayValue`
2. **Semantic queries**: `getByAltText`, `getByTitle`
3. **Test IDs**: `getByTestId`

`getByRole` should be your default. It matches how users and screen readers see the page, and it pushes you to write accessible markup. Use `getByTestId` only when nothing else works.

### 40: How does getByRole work?

It finds elements by their ARIA role. Many HTML elements have a role by default: `<button>` is `button`, `<a href>` is `link`, `<input type="text">` is `textbox`, `<input type="checkbox">` is `checkbox`, `<h1>` is `heading`, `<ul>` is `list`, `<li>` is `listitem`.

```tsx
screen.getByRole("button", { name: "Save" });
screen.getByRole("heading", { level: 1 });
screen.getByRole("checkbox", { checked: true });
screen.getByRole("link", { name: /terms/i });
```

You can also filter by state with options like `checked`, `pressed`, `expanded`, `selected` and `level`.

### 41: What does the name option in getByRole do?

`name` filters elements by their **accessible name**, which is what a screen reader would read out. For a button it's usually the text inside it. For an input it's the text of its `<label>`. It can also come from `aria-label` or `aria-labelledby`.

```tsx
// <button aria-label="Close dialog">×</button>
screen.getByRole("button", { name: "Close dialog" });

// <label>Email <input /></label>
screen.getByRole("textbox", { name: "Email" });
```

You can pass a string (exact match) or a regex like `/close/i` for a partial, case-insensitive match.

### 42: When should you use getByLabelText?

Use it for form fields. It finds the input linked to a label, which is how users find a field.

```tsx
// <label htmlFor="email">Email</label>
// <input id="email" />
const input = screen.getByLabelText("Email");
```

It works with `htmlFor`/`id`, with an input wrapped inside `<label>`, and with `aria-labelledby` and `aria-label`. If this query can't find your input, it often means the field is not properly labeled, which is also an accessibility bug.

### 43: When should you use getByPlaceholderText?

Only when the input has no label. A placeholder is not a replacement for a label, because it disappears when the user types and some screen readers don't read it. So if you need this query, think about adding a real label first.

```tsx
screen.getByPlaceholderText("Search...");
```

### 44: When should you use getByText?

Use it for elements that are not interactive, like paragraphs, headings (though `getByRole("heading")` is often better), error messages or labels.

```tsx
screen.getByText("No results found");
screen.getByText(/total: \$20/i);
```

By default it matches the full text of an element, trimmed and with whitespace collapsed. Use a regex or `{ exact: false }` for a partial match. If the text is split across several elements, you can pass a function matcher.

### 45: What does getByDisplayValue do?

It finds `input`, `textarea` or `select` elements by their current value. It's useful when a form is filled with existing data, like an edit profile page.

```tsx
render(<EditProfile user={{ name: "Anna" }} />);
expect(screen.getByDisplayValue("Anna")).toBeInTheDocument();
```

### 46: What are getByAltText and getByTitle used for?

`getByAltText` finds elements with an `alt` attribute, which means images, `<area>` and `<input type="image">`:

```tsx
screen.getByAltText("Company logo");
```

`getByTitle` finds elements by their `title` attribute, or SVGs by their `<title>` element. Titles are not read reliably by screen readers, so this query is lower in the priority list.

### 47: What is getByTestId and when should you use it?

It finds elements by the `data-testid` attribute:

```tsx
// <div data-testid="price-chart" />
screen.getByTestId("price-chart");
```

Users can't see test IDs, so this query doesn't test anything about what the user experiences. Use it as a last option, for example for a chart canvas, a container with no text or role, or when the text is dynamic and there's no better way to find it.

### 48: How do you check that an element is not on the page?

Use a `queryBy` query, because it returns `null` instead of throwing:

```tsx
expect(screen.queryByText("Loading...")).not.toBeInTheDocument();
expect(screen.queryByRole("alert")).toBeNull();
```

If you used `getByText` here, the test would throw before the assertion and you would get a less clear error.

### 49: What does toBeInTheDocument check?

It checks that the element is attached to the document. It's mostly used to make tests read better:

```tsx
expect(screen.getByText("Saved")).toBeInTheDocument();
```

Technically `getByText` already throws if the element doesn't exist, so the assertion is a bit redundant in that case. But it makes the intent clear, and combined with `queryBy` and `.not` it's the standard way to check something is missing.

### 50: What is the difference between toBeVisible and toBeInTheDocument?

`toBeInTheDocument` only checks that the element exists in the DOM. `toBeVisible` also checks that the user can actually see it. It fails if the element or any of its parents has `display: none`, `visibility: hidden`, `opacity: 0`, the `hidden` attribute, or is inside a closed `<details>`.

```tsx
expect(screen.getByText("Details")).toBeInTheDocument(); // exists
expect(screen.getByText("Details")).not.toBeVisible(); // but hidden
```

Note that jsdom doesn't load your CSS files, so `toBeVisible` only knows about inline styles and styles you add in the test.

### 51: How do you check the text of an element?

Use `toHaveTextContent`:

```tsx
expect(screen.getByRole("status")).toHaveTextContent("3 items");
expect(screen.getByRole("status")).toHaveTextContent(/3 items/);
```

With a string it checks that the text **contains** that value. With a regex it checks that the text matches. If you need an exact match, use a regex with `^` and `$` or compare `element.textContent` directly.

### 52: How do you check the value of an input or whether a checkbox is checked?

```tsx
expect(screen.getByLabelText("Email")).toHaveValue("anna@test.com");
expect(screen.getByLabelText("Age")).toHaveValue(30); // number input
expect(screen.getByRole("checkbox", { name: "Remember me" })).toBeChecked();
expect(screen.getByRole("combobox")).toHaveDisplayValue("Germany");
```

`toHaveValue` works for inputs, selects and textareas. `toHaveDisplayValue` checks what the user sees, which for a `<select>` is the text of the selected option, not its `value`.

### 53: How do you check if a button is disabled?

```tsx
expect(screen.getByRole("button", { name: "Submit" })).toBeDisabled();
expect(screen.getByRole("button", { name: "Submit" })).toBeEnabled();
```

`toBeDisabled` checks the `disabled` attribute and also handles elements inside a disabled `<fieldset>`. It doesn't treat `aria-disabled="true"` as disabled. For that, check the attribute with `toHaveAttribute("aria-disabled", "true")`.

### 54: How do you check attributes and CSS classes?

```tsx
const link = screen.getByRole("link", { name: "Docs" });
expect(link).toHaveAttribute("href", "/docs");
expect(link).toHaveAttribute("target", "_blank");

const tab = screen.getByRole("tab", { name: "Settings" });
expect(tab).toHaveClass("active");
expect(tab).toHaveAttribute("aria-selected", "true");
```

Be careful with class checks. A class name is usually an implementation detail. If the class means something to the user (like "selected"), it's often better to check an ARIA attribute or use a role query option like `{ selected: true }`.

### 55: What is @testing-library/user-event?

It's a library that simulates real user interactions, like typing, clicking, tabbing, selecting options and pasting. It fires the full sequence of events a browser would fire. For example, a click triggers `pointerdown`, `mousedown`, `focus`, `pointerup`, `mouseup` and `click`.

The current major version is 14. It's the recommended way to interact with components in React Testing Library tests.

### 56: What is the difference between fireEvent and user-event?

`fireEvent` dispatches **one** DOM event. `user-event` simulates what a **user** does, which is usually many events in a row.

```tsx
fireEvent.change(input, { target: { value: "hello" } }); // one change event
await user.type(input, "hello"); // focus, then keydown/keypress/input/keyup for each letter
```

`user-event` also checks things a real browser would. It won't click an element with `pointer-events: none`, and it won't type into a disabled input. Because of that, it catches more bugs. Use `fireEvent` only for events `user-event` doesn't support, like `scroll` or custom events.

### 57: How do you set up user-event?

Call `userEvent.setup()` at the start of the test, **before** rendering, and use the returned `user` object:

```tsx
import userEvent from "@testing-library/user-event";

test("toggles the menu", async () => {
  const user = userEvent.setup();
  render(<Menu />);

  await user.click(screen.getByRole("button", { name: "Menu" }));
  expect(screen.getByRole("menu")).toBeVisible();
});
```

You can still call `userEvent.click()` directly, but `setup()` is the recommended way. It shares keyboard and pointer state between calls, like a real user who is holding a key down.

### 58: Why are user-event methods async?

In v14 every method returns a promise, so you must `await` them. A real interaction is not instant. Between events the browser can run other code, and some features like the `delay` option or `advanceTimers` rely on that.

If you forget the `await`, the test may check the DOM before the events finish and fail randomly, or React will warn about updates not wrapped in `act`.

### 59: How do you simulate typing in an input?

```tsx
const user = userEvent.setup();
render(<SearchBox />);

const input = screen.getByRole("searchbox");
await user.type(input, "react testing");
expect(input).toHaveValue("react testing");
```

`type` clicks the element first and then types each character. You can also send special keys inside braces: `await user.type(input, "hello{Enter}")`.

### 60: How do you simulate a click?

```tsx
await user.click(screen.getByRole("button", { name: "Save" }));
await user.dblClick(screen.getByText("Edit me"));
await user.tripleClick(input); // selects all the text
```

For right click you can use `await user.pointer({ keys: "[MouseRight]", target: element })`.

### 61: How do you clear an input?

```tsx
const input = screen.getByLabelText("Name");
await user.clear(input);
await user.type(input, "New name");
```

`clear` focuses the input, selects all the text and deletes it. It's the usual way to replace a pre-filled value.

### 62: How do you select an option from a dropdown?

For a native `<select>`, use `selectOptions`:

```tsx
await user.selectOptions(
  screen.getByRole("combobox", { name: "Country" }),
  "Germany",
);
expect(screen.getByRole("option", { name: "Germany" }).selected).toBe(true);
```

You can pass the option's value, its text, or the option element itself. For custom dropdowns built with divs (like many UI libraries), `selectOptions` won't work. You click the trigger and then click the option, just like a user would.

### 63: How do you simulate keyboard keys?

Use `user.keyboard` with key names in braces:

```tsx
await user.keyboard("{Escape}");
await user.keyboard("{Enter}");
await user.keyboard("{ArrowDown}{ArrowDown}{Enter}");
await user.keyboard("{Shift>}A{/Shift}"); // hold Shift, press A, release Shift
await user.keyboard("{Control>}a{/Control}"); // select all
```

`keyboard` types into whatever element has focus right now. To move focus with Tab, use `await user.tab()`.

### 64: How do you test hover effects like tooltips?

```tsx
test("shows a tooltip on hover", async () => {
  const user = userEvent.setup();
  render(<IconButton label="Delete" />);

  await user.hover(screen.getByRole("button", { name: "Delete" }));
  expect(await screen.findByRole("tooltip")).toHaveTextContent("Delete");

  await user.unhover(screen.getByRole("button", { name: "Delete" }));
  await waitFor(() =>
    expect(screen.queryByRole("tooltip")).not.toBeInTheDocument(),
  );
});
```

This works when the tooltip is shown with JavaScript (`onMouseEnter`). A tooltip shown only with CSS `:hover` can't be tested in jsdom, because jsdom doesn't apply hover styles. Use an e2e or browser test for that.

### 65: How do you test a file upload?

Use `user.upload` with a `File` object:

```tsx
test("uploads an avatar", async () => {
  const user = userEvent.setup();
  render(<AvatarUpload />);

  const file = new File(["fake image"], "me.png", { type: "image/png" });
  const input = screen.getByLabelText(/upload avatar/i);
  await user.upload(input, file);

  expect(input.files?.[0]).toBe(file);
  expect(screen.getByText("me.png")).toBeInTheDocument();
});
```

By default `upload` respects the `accept` attribute, so a file with the wrong type is ignored. You can turn that off with `userEvent.setup({ applyAccept: false })`.

### 66: How would you test a simple counter component?

```tsx
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <>
      <p>Count: {count}</p>
      <button onClick={() => setCount((c) => c + 1)}>Increment</button>
    </>
  );
}

test("increments the count", async () => {
  const user = userEvent.setup();
  render(<Counter />);

  expect(screen.getByText("Count: 0")).toBeInTheDocument();
  await user.click(screen.getByRole("button", { name: "Increment" }));
  expect(screen.getByText("Count: 1")).toBeInTheDocument();
});
```

We don't check the state value directly. We check the text the user sees after clicking.

### 67: How do you test that a component renders its props correctly?

Render it with different props and check the output:

```tsx
test("shows the product name and price", () => {
  render(<ProductCard name="Laptop" price={999} />);

  expect(screen.getByRole("heading", { name: "Laptop" })).toBeInTheDocument();
  expect(screen.getByText("$999")).toBeInTheDocument();
});
```

If a prop changes what's shown in several ways (like a `variant`), write one test per meaningful case instead of trying to check every class name.

### 68: How do you test conditional rendering?

Render the component in each state and check what's visible or missing:

```tsx
test("shows the error when there is one", () => {
  render(<Field error="Required" />);
  expect(screen.getByRole("alert")).toHaveTextContent("Required");
});

test("shows no error by default", () => {
  render(<Field />);
  expect(screen.queryByRole("alert")).not.toBeInTheDocument();
});
```

### 69: How do you test that a list renders correctly?

```tsx
test("renders all todos", () => {
  const todos = [
    { id: 1, title: "Buy milk" },
    { id: 2, title: "Walk the dog" },
  ];
  render(<TodoList todos={todos} />);

  const items = screen.getAllByRole("listitem");
  expect(items).toHaveLength(2);
  expect(items[0]).toHaveTextContent("Buy milk");
  expect(items[1]).toHaveTextContent("Walk the dog");
});

test("shows an empty message", () => {
  render(<TodoList todos={[]} />);
  expect(screen.getByText("Nothing to do")).toBeInTheDocument();
});
```

Always test the empty case too. It's one of the most common places for bugs.

### 70: How do you test that a form calls onSubmit with the right data?

Pass a mock function and check how it was called:

```tsx
test("submits the form data", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();
  render(<ContactForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText("Name"), "Anna");
  await user.type(screen.getByLabelText("Email"), "anna@test.com");
  await user.click(screen.getByRole("button", { name: "Send" }));

  expect(onSubmit).toHaveBeenCalledTimes(1);
  expect(onSubmit).toHaveBeenCalledWith({
    name: "Anna",
    email: "anna@test.com",
  });
});
```

### 71: What is a mock?

A mock is a fake version of something your code depends on, like a function, a module or an API. You use mocks to:

- avoid slow or unreliable things (network, timers, random values)
- control what a dependency returns, so you can test different cases
- check that your code called a dependency with the right arguments

The risk is mocking too much. If you mock everything, your test only checks that your mocks work, not that the real app works.

### 72: What is the difference between a mock, a stub, a spy and a fake?

These words are often mixed up, but the usual meanings are:

- **Stub**: replaces a function and returns a fixed value. It doesn't care how it was called.
- **Spy**: wraps a real function and records how it was called, but still runs the real code (unless you change it).
- **Mock**: a fake that records calls, so you can assert on them, and can also return values.
- **Fake**: a working but simplified implementation, like an in-memory database or an MSW handler instead of a real API.

In Vitest and Jest, `vi.fn()` / `jest.fn()` and `vi.spyOn()` can act as any of the first three.

### 73: How do you create a mock function?

```ts
import { vi } from "vitest";

const onClick = vi.fn(); // Vitest
// const onClick = jest.fn(); // Jest

onClick("a");
onClick("b");

expect(onClick).toHaveBeenCalledTimes(2);
expect(onClick.mock.calls).toEqual([["a"], ["b"]]);
```

A mock function records every call, its arguments and its return values. By default it returns `undefined`.

### 74: How do you check how a mock function was called?

```ts
expect(fn).toHaveBeenCalled();
expect(fn).toHaveBeenCalledTimes(2);
expect(fn).toHaveBeenCalledWith("anna", { admin: true });
expect(fn).toHaveBeenLastCalledWith("bob", { admin: false });
expect(fn).toHaveBeenNthCalledWith(1, "anna", { admin: true });
expect(fn).not.toHaveBeenCalled();
```

In Jest 30 the old short names like `toBeCalled` and `toBeCalledWith` were removed, so use the `toHaveBeen...` versions.

### 75: How do you make a mock function return a value?

```ts
const getUser = vi.fn();

getUser.mockReturnValue({ id: 1 }); // every call
getUser.mockReturnValueOnce({ id: 2 }); // only the next call

const fetchUser = vi.fn();
fetchUser.mockResolvedValue({ id: 1 }); // returns Promise.resolve(...)
fetchUser.mockRejectedValueOnce(new Error("Network error"));

const calc = vi.fn().mockImplementation((a: number, b: number) => a + b);
```

`mockImplementation` gives you full control when the return value depends on the arguments.

### 76: What is vi.spyOn and when do you use it?

`vi.spyOn` (or `jest.spyOn`) replaces a method on an existing object with a mock and keeps track of calls. By default it still calls the original method.

```ts
const logSpy = vi.spyOn(console, "error").mockImplementation(() => {});

doSomethingThatLogs();
expect(logSpy).toHaveBeenCalledWith(expect.stringContaining("failed"));

logSpy.mockRestore(); // put the real console.error back
```

Use it when you want to watch or replace one method of an object (like `console`, `window`, `localStorage` or a service object) without mocking the whole module.

### 77: How do you mock a whole module?

Use `vi.mock` (Vitest) or `jest.mock` (Jest) with the module path:

```ts
import { vi, test, expect } from "vitest";
import { getUsers } from "./api";
import { loadUserNames } from "./users";

vi.mock("./api", () => ({
  getUsers: vi.fn(),
}));

test("returns user names", async () => {
  vi.mocked(getUsers).mockResolvedValue([{ name: "Anna" }]);
  expect(await loadUserNames()).toEqual(["Anna"]);
});
```

The call is moved (hoisted) to the top of the file, so it runs before the imports. Every file that imports `./api` in this test gets the mocked version.

### 78: What is the difference between clearing, resetting and restoring mocks?

- **`mockClear()`**: removes the recorded calls and results. The implementation stays.
- **`mockReset()`**: does what clear does and also removes the implementation and return values you set.
- **`mockRestore()`**: for spies, puts the original method back.

There are global versions: `vi.clearAllMocks()`, `vi.resetAllMocks()` and `vi.restoreAllMocks()`. You can also turn on `clearMocks`, `mockReset` or `restoreMocks` in the config so it happens before every test automatically. This keeps tests from affecting each other.

### 79: What are beforeEach, afterEach, beforeAll and afterAll?

They are hooks that run code around your tests:

- `beforeAll`: once before all tests in the file or `describe` block
- `beforeEach`: before every test
- `afterEach`: after every test
- `afterAll`: once after all tests

```ts
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

Use `beforeEach` for setup that every test needs fresh. Use `beforeAll` for expensive setup that can safely be shared, like starting a mock server.

### 80: Does React Testing Library clean up after each test?

Yes, if your test runner has a global `afterEach`. RTL registers an `afterEach` that calls `cleanup()`, which unmounts every rendered component and removes the containers from `document.body`.

Jest has global `afterEach` by default. In Vitest, globals are off unless you set `globals: true`. If they're off, add cleanup in your setup file yourself:

```ts
import { afterEach } from "vitest";
import { cleanup } from "@testing-library/react";

afterEach(() => cleanup());
```

Without cleanup, components from earlier tests stay in the DOM and queries start finding duplicate elements.

### 81: What do test.only, test.skip and test.todo do?

- `test.only`: runs only this test (and other `.only` tests) in the file. Useful while debugging.
- `test.skip`: skips this test.
- `test.todo("should handle empty input")`: marks a test you plan to write. It shows up in the report.

The same works on `describe`. Don't commit `.only` by mistake, because it silently skips the rest of the file. The ESLint plugins for Vitest and Jest have a rule for this (`no-focused-tests`), and in CI Vitest fails on `.only` by default (`allowOnly` is false when `CI` is set).

### 82: What is test.each?

It lets you run the same test with different inputs:

```ts
test.each([
  [1, 1, 2],
  [2, 3, 5],
  [-1, 1, 0],
])("sum(%i, %i) = %i", (a, b, expected) => {
  expect(sum(a, b)).toBe(expected);
});

test.each([
  { input: "", error: "Required" },
  { input: "abc", error: "Invalid email" },
])("shows '$error' for '$input'", ({ input, error }) => {
  expect(validateEmail(input)).toBe(error);
});
```

It's great for validation rules, formatters and anything with a table of input and output values. Vitest also has `test.for`, which works the same but doesn't spread array items into separate arguments.

### 83: How do you run tests in watch mode?

- Vitest runs in watch mode by default when you run `vitest` in a terminal. `vitest run` runs once.
- Jest uses `jest --watch` (only files changed since the last commit) or `jest --watchAll`.

In watch mode the runner re-runs only the tests affected by the files you changed. It's the normal way to work while writing code.

### 84: How do you run only one test file or one test?

```bash
# one file (or files matching a pattern)
npx vitest run src/components/Button.test.tsx
npx jest Button

# tests whose name matches a pattern
npx vitest run -t "shows an error"
npx jest -t "shows an error"
```

You can also add `.only` to a test temporarily, or use the filter options in watch mode (press `p` for file name, `t` for test name).

### 85: What is code coverage?

Code coverage shows how much of your code ran during the tests. A coverage report lists every file and highlights lines that were never executed.

It's useful for finding parts of the code that no test touches. But it only tells you the code **ran**, not that the tests checked the result. A test with no assertions can still give you 100% coverage.

### 86: How do you generate a coverage report?

```bash
npx vitest run --coverage
npx jest --coverage
```

Vitest needs a coverage provider installed, usually `@vitest/coverage-v8` (the default) or `@vitest/coverage-istanbul`. You can configure it:

```ts
test: {
  coverage: {
    provider: "v8",
    reporter: ["text", "html", "lcov"],
    include: ["src/**/*.{ts,tsx}"],
    exclude: ["src/**/*.stories.tsx", "src/main.tsx"],
  },
}
```

The `html` reporter creates a folder you can open in the browser to see covered and uncovered lines.

### 87: What are the different coverage metrics?

- **Statements**: how many statements ran.
- **Lines**: how many lines ran.
- **Functions**: how many functions were called at least once.
- **Branches**: how many branches of `if`, `else`, ternaries, `&&`, `??` and `switch` ran.

Branch coverage is usually the most useful one. You can have 100% line coverage and still never test the `else` path of a condition written on one line.

### 88: Is 100% code coverage a good goal?

Usually not. Getting the last 10-20% often means writing tests for trivial code or tests that only exist to touch lines. Those tests cost time to write and maintain and add little value.

A better approach is to set a reasonable threshold (like 70-80%) so coverage doesn't drop silently, and to focus on testing important behavior and risky logic. High coverage of the checkout flow matters more than high coverage of a static "About" page.

### 89: What is snapshot testing?

A snapshot test saves the output of something (like rendered HTML or an object) to a file the first time it runs. On later runs it compares the new output with the saved one and fails if they differ.

```tsx
test("matches snapshot", () => {
  const { asFragment } = render(<Badge type="success">Paid</Badge>);
  expect(asFragment()).toMatchSnapshot();
});
```

The snapshot files are stored in a `__snapshots__` folder and should be committed to git.

### 90: How do you update snapshots when the change is intentional?

```bash
npx vitest run -u
npx jest -u
```

In watch mode you can press `u`. Before updating, always look at the diff and make sure the change is what you expected. If people get used to pressing `u` without looking, snapshot tests stop catching anything.

### 91: What are inline snapshots?

Inline snapshots are saved directly in the test file instead of a separate file:

```ts
test("formats the user", () => {
  expect(formatUser({ first: "Anna", last: "Smith" })).toMatchInlineSnapshot(
    `"Smith, Anna"`,
  );
});
```

The first time you run it, the runner writes the value into the test for you. They are easier to review because the expected value is right next to the test. They work best for small outputs.

### 92: When are snapshot tests a bad idea?

- When the snapshot is very big, like a whole page. Nobody reads a 300-line diff carefully, so people just update it.
- When the output changes often for reasons that don't matter, like class names from CSS-in-JS or generated IDs.
- When you could write a clear assertion instead. `expect(button).toBeDisabled()` explains the intent much better than a snapshot.

Snapshots work best for small, stable outputs, like a formatted string, an error message or a small serialized object.

### 93: How do you see what the DOM looks like inside a test?

Use `screen.debug()`:

```tsx
render(<Cart />);
screen.debug(); // whole document.body
screen.debug(screen.getByRole("list")); // one element
```

It prints the HTML in a readable format. Long output is cut after 7000 characters by default. You can change that with the `DEBUG_PRINT_LIMIT` environment variable.

### 94: What are logRoles and Testing Playground?

`logRoles` prints every element with its ARIA role and accessible name, which helps when you don't know which role or name to use in `getByRole`:

```tsx
import { logRoles } from "@testing-library/react";

const { container } = render(<Nav />);
logRoles(container);
```

`screen.logTestingPlaygroundURL()` prints a link to testing-playground.com with your current DOM loaded. There you can click an element and it suggests the best query for it.

### 95: What does act() do?

`act` makes sure all React updates (state changes, effects, rendering) caused by some code are finished before you make assertions. In React 19 you import it from `react`:

```tsx
import { act } from "react";

await act(async () => {
  root.render(<App />);
});
```

Without it, you might check the DOM before React has applied an update, and React would show the warning "An update to X inside a test was not wrapped in act(...)".

### 96: Do you need to call act yourself when using React Testing Library?

Rarely. RTL already wraps `render`, `rerender`, `unmount`, `fireEvent`, and the async utilities (`waitFor`, `findBy`) in `act`. `user-event` calls go through these wrappers too.

You might need `act` directly when something outside of these helpers changes React state, for example when you advance fake timers manually or call a function returned by `renderHook`:

```tsx
act(() => {
  result.current.increment();
});
```

If you see an act warning, it usually means something async finished after the test ended, and you need to wait for it with `findBy` or `waitFor`.

### 97: How do you test async behavior with waitFor?

`waitFor` keeps calling your callback until it stops throwing or the timeout (1000 ms by default) is reached:

```tsx
test("shows saved message", async () => {
  const user = userEvent.setup();
  render(<Settings />);

  await user.click(screen.getByRole("button", { name: "Save" }));

  await waitFor(() => {
    expect(screen.getByText("Settings saved")).toBeInTheDocument();
  });
});
```

It checks again every 50 ms and also whenever the DOM changes.

### 98: What is the difference between findBy and waitFor?

`findBy` is a shortcut for `waitFor` + `getBy`. These two lines do the same thing:

```tsx
await screen.findByText("Settings saved");

await waitFor(() => screen.getByText("Settings saved"));
```

Use `findBy` when you're waiting for an element to appear. Use `waitFor` when you're waiting for something else, like a mock to be called or an element to change its text:

```tsx
await waitFor(() => expect(onSave).toHaveBeenCalledTimes(1));
```

### 99: How do you wait for something to disappear?

Use `waitForElementToBeRemoved`:

```tsx
render(<UserList />);
await waitForElementToBeRemoved(() => screen.queryByText("Loading..."));
expect(screen.getAllByRole("listitem")).toHaveLength(3);
```

Pass a callback that uses `queryBy`, not `getBy`. The element must be in the DOM when you call it, otherwise it throws right away. You can also use `waitFor` with `.not.toBeInTheDocument()`.

### 100: How would you test a component that loads data when it mounts?

Mock the network (MSW is the most common choice), render the component, and wait for the data to show up:

```tsx
import { http, HttpResponse } from "msw";
import { server } from "../mocks/server";

test("shows the list of users", async () => {
  server.use(
    http.get("/api/users", () => HttpResponse.json([{ id: 1, name: "Anna" }])),
  );

  render(<UserList />);

  expect(screen.getByText("Loading...")).toBeInTheDocument();
  expect(await screen.findByText("Anna")).toBeInTheDocument();
});
```

Also test the error state and the empty state, not only the happy path.

### 101: Why shouldn't you test implementation details?

Tests that check implementation details break when you refactor, even if the app still works. That gives you false failures. They can also pass when the app is broken, because they check internal values instead of what the user sees. That gives you false passes.

For example, if a test checks that `isOpen` state is `true`, it breaks when you rename the state. A test that clicks the button and checks that the menu is visible keeps working no matter how you store that state.

### 102: What are some examples of implementation details in React tests?

- Checking a component's internal state or calling its internal functions.
- Checking which hooks were called or how many times a component rendered.
- Finding elements by CSS class or component name.
- Testing that a child component received certain props (shallow rendering).
- Mocking your own child components without a good reason.
- Checking the exact HTML structure (`div > span > p`).

The two "users" of a component are the person using the app and the developer rendering it with props. Test from their point of view.

### 103: What is a flaky test?

A flaky test sometimes passes and sometimes fails without any code change. Common causes:

- not waiting for async work to finish
- depending on the order tests run in, or on state left from another test
- real timers, real dates or random values
- real network calls
- in e2e tests, waiting a fixed time instead of waiting for a condition, animations, or shared test data

Flaky tests are worse than they look. Once people stop trusting the test suite, they ignore real failures too.

### 104: What makes a good test?

- **Tests behavior** the user or caller cares about.
- **Readable**: a clear name and a clear arrange, act and assert structure.
- **Isolated**: doesn't depend on other tests or on the order they run in.
- **Deterministic**: same result every time.
- **Fast**, so people actually run it.
- **Fails for one clear reason**, with a helpful error message.
- **Resistant to refactoring**: doesn't break when you change the code without changing behavior.

### 105: What is test isolation and why does it matter?

Test isolation means each test runs as if it were the only test. It sets up its own data, and it doesn't rely on anything another test left behind.

Without isolation you get tests that pass alone and fail together, or fail only when run in a certain order. In React tests, the common leaks are DOM that wasn't cleaned up, mocks that weren't reset, MSW handlers left over from a previous test, shared store instances (Redux, Zustand, React Query cache) and `localStorage`.

### 106: What is TDD?

Test-driven development is a way of working in short cycles:

1. **Red**: write a small test that fails.
2. **Green**: write the simplest code that makes it pass.
3. **Refactor**: clean up the code while the tests stay green.

It forces you to think about how the code will be used before you write it, and you end up with tests for everything. It works especially well for logic like reducers, validation and utility functions, and for bug fixes.

### 107: What is BDD?

Behavior-driven development focuses on describing behavior in plain language, usually as "Given, When, Then":

- **Given** I am logged in and have an item in my cart
- **When** I click "Checkout"
- **Then** I see the payment page

Some teams write these scenarios in Gherkin files and run them with tools like Cucumber. In React projects, BDD more often just means naming tests by behavior, like `"shows an error when the email is invalid"`.

### 108: What is regression testing?

Regression testing makes sure that something that used to work still works after a change. Every automated test you keep in your suite becomes a regression test.

A good habit is to add a test for every bug you fix. If the bug comes back later, the test catches it.

### 109: What is a smoke test?

A smoke test is a small set of quick checks that the most important parts of the app work at all: the home page loads, the user can log in, the main page renders without errors.

Teams often run smoke tests right after a deploy. If they fail, there's no point running the full suite, because something basic is broken.

### 110: What is Playwright?

Playwright is an end-to-end testing framework from Microsoft. It controls Chromium, Firefox and WebKit (the engine behind Safari) through one API.

It has its own test runner (`@playwright/test`) with auto-waiting, web-first assertions, parallel runs, fixtures, network mocking, a trace viewer, a UI mode for debugging and code generation. It supports TypeScript out of the box and has become the most popular choice for new e2e test suites.

### 111: What is Cypress?

Cypress is an end-to-end and component testing framework. Your tests run inside the browser next to your app, and you get an interactive runner where you can see each step, hover over commands and inspect the DOM at that moment.

It has a chain-based API (`cy.get(...).click()`), automatic retries, network stubbing with `cy.intercept` and a paid cloud service for recording and parallel runs. The current major version is Cypress 15.

### 112: What are the main differences between Playwright and Cypress?

|                           | Playwright                                 | Cypress                                               |
| ------------------------- | ------------------------------------------ | ----------------------------------------------------- |
| How it runs               | Controls the browser from outside, in Node | Runs inside the browser                               |
| Browsers                  | Chromium, Firefox, WebKit                  | Chrome-family, Firefox, Edge (WebKit is experimental) |
| Multiple tabs and domains | Supported                                  | Limited (`cy.origin` for other domains)               |
| Parallel runs             | Built in and free                          | Through Cypress Cloud or third-party tools            |
| API style                 | `async`/`await`                            | Command chain                                         |
| Debugging                 | Trace viewer, UI mode                      | Interactive time-travel runner                        |

Both are good. Playwright is more common in new projects because of WebKit support, free parallelism and multi-tab support. Cypress is still loved for its developer experience.

### 113: How do you add Playwright to a project?

```bash
npm init playwright@latest
```

This installs `@playwright/test`, downloads the browsers, creates a `playwright.config.ts` and an example test. Then you run:

```bash
npx playwright test           # run all tests
npx playwright test --ui      # interactive UI mode
npx playwright show-report    # open the HTML report
```

### 114: What does a basic Playwright test look like?

```ts
import { test, expect } from "@playwright/test";

test("user can search for a product", async ({ page }) => {
  await page.goto("/");

  await page.getByRole("searchbox", { name: "Search" }).fill("laptop");
  await page.getByRole("button", { name: "Search" }).click();

  await expect(
    page.getByRole("heading", { name: /results for "laptop"/i }),
  ).toBeVisible();
  await expect(page.getByRole("article")).toHaveCount(10);
});
```

The `page` object is a fresh browser tab that Playwright gives every test.

### 115: What is the page object in Playwright?

`page` represents one browser tab. It's a built-in fixture, so every test gets a new one inside a new, isolated browser context (like a fresh incognito window).

You use it to navigate (`page.goto`), find elements (`page.getByRole`), listen to events (`page.on("console")`), mock the network (`page.route`) and take screenshots.

### 116: What are locators in Playwright?

A locator is a way to find elements on the page. It doesn't search right away. It searches every time you use it, so it always works with the current DOM.

```ts
const submit = page.getByRole("button", { name: "Submit" });
await submit.click();
await expect(submit).toBeDisabled();
```

The recommended locators are almost the same as Testing Library queries: `getByRole`, `getByLabel`, `getByPlaceholder`, `getByText`, `getByAltText`, `getByTitle` and `getByTestId`. You can also use `page.locator("css or xpath")`, but it's more fragile.

### 117: What is auto-waiting in Playwright?

Before an action like `click()` or `fill()`, Playwright waits for the element to be ready. For a click, it waits until the element is attached, visible, stable (not animating), enabled and able to receive events (not covered by another element).

Because of this you almost never need manual waits. If the element never becomes ready, the action fails after the timeout with a clear message.

### 118: What are web-first assertions?

They are assertions that keep retrying until the condition is true or the timeout is reached (5 seconds by default):

```ts
await expect(page.getByText("Order placed")).toBeVisible();
await expect(page.getByRole("listitem")).toHaveCount(3);
await expect(page).toHaveURL(/\/orders\/\d+/);
await expect(page.getByLabel("Email")).toHaveValue("anna@test.com");
```

Compare that with `expect(await locator.isVisible()).toBe(true)`, which checks only once and fails if the element shows up a moment later. Always prefer the `await expect(locator)` form.

### 119: How do you run Playwright tests in headed mode or debug them?

```bash
npx playwright test --headed          # show the browser window
npx playwright test --ui              # UI mode: watch, time travel, pick tests
npx playwright test --debug           # step through with the inspector
npx playwright test --project=chromium
npx playwright test checkout.spec.ts -g "guest checkout"
```

You can also put `await page.pause()` in a test to stop there and open the inspector.

### 120: What is Playwright codegen?

Codegen opens a browser and records what you do as Playwright code:

```bash
npx playwright codegen http://localhost:5173
```

It picks good locators like `getByRole` automatically. It's useful for getting started or finding a locator quickly. The generated code usually needs cleanup, though. You still need to add real assertions and give tests good structure.

### 121: What does a basic Cypress test look like?

```ts
describe("search", () => {
  it("finds a product", () => {
    cy.visit("/");
    cy.get("[data-cy=search-input]").type("laptop");
    cy.contains("button", "Search").click();
    cy.get("[data-cy=product-card]").should("have.length", 10);
    cy.url().should("include", "q=laptop");
  });
});
```

Notice there's no `async`/`await`. Cypress commands are put in a queue and run one after another. `should` assertions retry until they pass or time out.

### 122: How can you use Testing Library queries in Cypress?

Install `@testing-library/cypress` and import it in the support file:

```ts
// cypress/support/commands.ts
import "@testing-library/cypress/add-commands";
```

Then you can use the same queries as in unit tests:

```ts
cy.findByRole("button", { name: /add to cart/i }).click();
cy.findByLabelText("Email").type("anna@test.com");
```

This keeps your selector style the same across unit and e2e tests and avoids fragile CSS selectors.

### 123: What is component testing in Cypress?

Cypress can mount a single React component in a real browser, without running the whole app:

```tsx
import { mount } from "cypress/react";
import { Counter } from "./Counter";

it("increments", () => {
  mount(<Counter />);
  cy.contains("button", "Increment").click();
  cy.contains("Count: 1").should("be.visible");
});
```

It's like a React Testing Library test, but the component runs in a real browser with real CSS and layout. Usually you register `mount` as a custom command (`cy.mount`) in the component support file.

### 124: What are baseURL and webServer in the Playwright config?

`baseURL` lets you use short paths like `page.goto("/login")`. `webServer` tells Playwright how to start your app before the tests run:

```ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  use: {
    baseURL: "http://localhost:5173",
  },
  webServer: {
    command: "npm run dev",
    url: "http://localhost:5173",
    reuseExistingServer: !process.env.CI,
  },
});
```

With `reuseExistingServer`, if your dev server is already running locally, Playwright uses it. In CI it always starts a fresh one.

### 125: Which browsers can Playwright test?

Playwright supports **Chromium**, **Firefox** and **WebKit**. It can also run branded Chrome and Microsoft Edge with the `channel` option. You set them up as projects in the config:

```ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "webkit", use: { ...devices["Desktop Safari"] } },
    { name: "mobile", use: { ...devices["iPhone 15"] } },
  ],
});
```

Mobile "devices" are emulation (viewport, user agent, touch). They're not real phones.

### 126: What is headless mode?

Headless mode runs the browser without showing a window. It's faster and is what you use in CI, where there's no screen. Playwright runs headless by default. You switch to headed mode with `--headed` or `use: { headless: false }`. Cypress runs headless with `cypress run` and opens a window with `cypress open`.

### 127: What is a test fixture?

The word is used for two things:

1. **Test data**: files like `users.json` that tests load. Cypress uses "fixtures" in this sense (`cy.fixture("users.json")`).
2. **Setup provided to a test**: something prepared before the test and cleaned up after. Playwright uses fixtures in this sense. `page`, `context` and `request` are fixtures, and you can create your own, like a logged-in page.

In an interview, it's worth mentioning both meanings.

### 128: What are test data factories?

A factory is a function that creates test objects with sensible defaults, and lets you override only the fields that matter for the test:

```ts
let nextId = 1;

export function buildUser(overrides: Partial<User> = {}): User {
  return {
    id: nextId++,
    name: "Test User",
    email: `user${nextId}@test.com`,
    role: "member",
    ...overrides,
  };
}

const admin = buildUser({ role: "admin" });
```

This keeps tests short and focused. A reader sees only `role: "admin"` and knows that's what this test is about.

### 129: What is MSW (Mock Service Worker)?

MSW is a library for mocking network requests. You describe your API with request handlers:

```ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/user", () => HttpResponse.json({ id: 1, name: "Anna" })),
  http.post("/api/login", () => new HttpResponse(null, { status: 204 })),
];
```

In the browser it uses a Service Worker to catch requests. In Node (Vitest or Jest) it intercepts requests at the network module level with `setupServer`. The same handlers can be used in tests, in Storybook and during local development.

### 130: Why use MSW instead of mocking fetch or axios directly?

- Your component code runs exactly as in production. It calls `fetch` or `axios` for real, and only the network layer is faked.
- Tests don't break when you switch from `fetch` to `axios` or to React Query.
- You can test headers, query params, request bodies, status codes and delays.
- The same handlers work in unit tests, Storybook and the browser.

Mocking `fetch` directly is quicker for one small test, but it ties the test to how the request is made.

### 131: What is a custom render function and why use it?

Most components need providers to work: a router, a theme, a query client, a store, i18n. Instead of adding them in every test, you write your own `render`:

```tsx
// test-utils.tsx
import { render, type RenderOptions } from "@testing-library/react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { MemoryRouter } from "react-router";

function renderWithProviders(ui: React.ReactElement, options?: RenderOptions) {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });

  function Wrapper({ children }: { children: React.ReactNode }) {
    return (
      <QueryClientProvider client={queryClient}>
        <MemoryRouter>{children}</MemoryRouter>
      </QueryClientProvider>
    );
  }

  return render(ui, { wrapper: Wrapper, ...options });
}

export * from "@testing-library/react";
export { renderWithProviders as render };
```

Tests then import `render` and `screen` from `test-utils` instead of `@testing-library/react`.

### 132: How do you test a component that uses context?

Wrap it in the real provider, with the value you need for the test:

```tsx
test("shows the user's name", () => {
  render(
    <AuthContext.Provider value={{ user: { name: "Anna" }, logout: vi.fn() }}>
      <Header />
    </AuthContext.Provider>,
  );

  expect(screen.getByText("Hi, Anna")).toBeInTheDocument();
});
```

If the provider has its own logic (like loading the user), it's often better to render the real provider and mock the network, so you test them together.

### 133: How do you test a component that uses React Router?

Render it inside a `MemoryRouter`, which keeps the history in memory instead of using the browser URL:

```tsx
import { MemoryRouter } from "react-router";

test("highlights the active link", () => {
  render(
    <MemoryRouter initialEntries={["/settings"]}>
      <Sidebar />
    </MemoryRouter>,
  );

  expect(screen.getByRole("link", { name: "Settings" })).toHaveAttribute(
    "aria-current",
    "page",
  );
});
```

Without a router, components that use `Link`, `useNavigate` or `useParams` throw an error.

### 134: How do you test a custom hook?

Use `renderHook` from React Testing Library:

```tsx
import { renderHook, act } from "@testing-library/react";
import { useCounter } from "./useCounter";

test("increments", () => {
  const { result } = renderHook(() => useCounter(5));

  expect(result.current.count).toBe(5);

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(6);
});
```

`result.current` always holds the latest return value. The old `@testing-library/react-hooks` package is deprecated. `renderHook` is now part of `@testing-library/react`.

### 135: What does rerender do?

`rerender` renders the same component again with new props, without unmounting it. Use it to test how a component reacts to prop changes:

```tsx
test("updates when the count prop changes", () => {
  const { rerender } = render(<Badge count={1} />);
  expect(screen.getByText("1")).toBeInTheDocument();

  rerender(<Badge count={5} />);
  expect(screen.getByText("5")).toBeInTheDocument();
});
```

State is kept between renders, just like when a parent re-renders in the real app.

### 136: When would you use unmount in a test?

To check what happens when a component is removed, usually that cleanup code runs:

```tsx
test("removes the resize listener on unmount", () => {
  const removeSpy = vi.spyOn(window, "removeEventListener");
  const { unmount } = render(<WindowSize />);

  unmount();

  expect(removeSpy).toHaveBeenCalledWith("resize", expect.any(Function));
});
```

You don't need `unmount` for normal cleanup between tests. RTL does that automatically.

### 137: How do you test code that uses setTimeout?

Use fake timers, so you don't actually wait:

```tsx
beforeEach(() => vi.useFakeTimers());
afterEach(() => vi.useRealTimers());

test("hides the toast after 3 seconds", () => {
  render(<Toast message="Saved" />);
  expect(screen.getByText("Saved")).toBeInTheDocument();

  act(() => {
    vi.advanceTimersByTime(3000);
  });

  expect(screen.queryByText("Saved")).not.toBeInTheDocument();
});
```

In Jest it's `jest.useFakeTimers()` and `jest.advanceTimersByTime()`. Wrap the timer call in `act` because it causes a React state update.

### 138: What is container and why should you avoid using it for queries?

`container` is the `div` your component was rendered into. You can query it with normal DOM methods:

```tsx
const { container } = render(<Card />);
container.querySelector(".card-title"); // works, but not recommended
```

Using `querySelector` with class names or tag names ties the test to the markup, which is an implementation detail. It also ignores accessibility. Prefer `screen` queries. `container` is still fine for things like `logRoles(container)` or checking `container.firstChild` is empty when a component renders nothing.

### 139: What is within and when do you use it?

`within` limits queries to one part of the page:

```tsx
import { within } from "@testing-library/react";

const row = screen.getByRole("row", { name: /anna/i });
await user.click(within(row).getByRole("button", { name: "Delete" }));

const dialog = screen.getByRole("dialog");
expect(within(dialog).getByText("Are you sure?")).toBeInTheDocument();
```

Use it when the same text or button appears several times, like a "Delete" button on every table row.

### 140: How does React Testing Library help with accessibility?

When you use `getByRole` and `getByLabelText`, your tests only pass if the elements have proper roles and labels. If a button is a `<div onClick>`, `getByRole("button")` won't find it. If an input has no label, `getByLabelText` fails.

So writing tests in the recommended way makes you fix many accessibility problems as you go. It doesn't replace a full accessibility audit, but it's a good start.

### 141: What are jest-axe and vitest-axe?

They run the axe-core accessibility checker on rendered HTML and fail the test if there are violations:

```tsx
import { axe } from "vitest-axe";

test("has no accessibility violations", async () => {
  const { container } = render(<SignupForm />);
  expect(await axe(container)).toHaveNoViolations();
});
```

You need to register the matcher in the setup file. In jsdom some checks can't run, especially color contrast, because there's no real rendering. For those, run axe in a real browser, for example with `@axe-core/playwright`.

### 142: How do you test form validation errors?

Do what the user does, then look for the error message:

```tsx
test("shows an error for an invalid email", async () => {
  const user = userEvent.setup();
  render(<SignupForm />);

  await user.type(screen.getByLabelText("Email"), "not-an-email");
  await user.click(screen.getByRole("button", { name: "Sign up" }));

  expect(
    await screen.findByText("Please enter a valid email"),
  ).toBeInTheDocument();
  expect(screen.getByLabelText("Email")).toHaveAttribute(
    "aria-invalid",
    "true",
  );
});
```

Use `findBy` because many form libraries validate asynchronously. Also check that the form is not submitted when it's invalid.

### 143: How do you test a loading state?

Check the loading indicator right after rendering, then wait for it to go away:

```tsx
test("shows a spinner while loading", async () => {
  render(<Orders />);

  expect(screen.getByRole("progressbar")).toBeInTheDocument();
  expect(await screen.findByText("Order #1001")).toBeInTheDocument();
  expect(screen.queryByRole("progressbar")).not.toBeInTheDocument();
});
```

If the response comes back too fast to see the loading state, you can add a delay in the MSW handler with `await delay(100)`.

### 144: How do you check which element has focus?

Use `toHaveFocus`:

```tsx
test("focuses the input when the dialog opens", async () => {
  const user = userEvent.setup();
  render(<RenameDialog />);

  await user.click(screen.getByRole("button", { name: "Rename" }));
  expect(screen.getByLabelText("New name")).toHaveFocus();
});
```

You can also check `document.activeElement`. Focus is important for keyboard and screen reader users, so it's worth testing in dialogs, menus and forms.

### 145: What does the globals option do in Vitest?

By default, Vitest doesn't add `describe`, `test`, `expect` and `vi` as global variables. You import them:

```ts
import { describe, test, expect, vi } from "vitest";
```

With `test: { globals: true }` they're available globally, like in Jest. This makes migrating from Jest easier, and it also lets React Testing Library find the global `afterEach` to clean up automatically. For TypeScript, add `"types": ["vitest/globals"]` to `tsconfig.json`.

### 146: How do you use TypeScript in tests?

Vitest supports TypeScript out of the box through Vite. Jest needs a transformer like `ts-jest`, Babel with the TypeScript preset, or `@swc/jest`.

Keep in mind that Vitest, Babel and SWC only strip types and don't type-check. A test can pass even with type errors. Run `tsc --noEmit` separately (in CI or a pre-commit hook) so type errors in test files are caught too. Make sure your `tsconfig` includes the test files and the types for jest-dom and the runner globals.

### 147: What ESLint plugins help with writing tests?

- **eslint-plugin-testing-library**: catches common mistakes, like not awaiting `findBy`, using `container.querySelector`, or wrapping things in `act` without reason.
- **eslint-plugin-jest-dom**: suggests better jest-dom matchers, like `toBeDisabled()` instead of `toHaveAttribute("disabled")`.
- **@vitest/eslint-plugin** or **eslint-plugin-jest**: rules like no focused tests, no disabled tests and valid `expect` usage.
- **eslint-plugin-playwright**: rules for Playwright, like requiring `await` on web-first assertions.

### 148: Why should tests run in CI?

CI (continuous integration) runs the tests on every push or pull request, on a clean machine. This makes sure:

- nobody merges code that breaks tests, even if they forgot to run them locally
- tests don't depend on something that only exists on one developer's machine
- the team sees the results in the pull request before reviewing

Usually the pipeline runs lint and type checks first, then unit and integration tests, then e2e tests, and blocks the merge if anything fails.

### 149: How do you run tests in CI mode?

Run them once instead of in watch mode:

```bash
npx vitest run
npx jest --ci
npx playwright test
```

Vitest detects the `CI` environment variable and doesn't start watch mode. `jest --ci` makes Jest fail when a snapshot is missing instead of writing a new one. For Playwright, the config usually sets `retries`, `workers` and `forbidOnly` based on `process.env.CI`.

### 150: What happened to Enzyme and react-test-renderer?

**Enzyme** was a popular library from Airbnb that let you shallow render components and read their state and props. It was never updated for React 18 or 19, so it's effectively dead. Projects that still use it are stuck and need to move to React Testing Library.

**react-test-renderer** renders components to a plain JavaScript object instead of the DOM. It's deprecated as of React 19, and the React team recommends React Testing Library instead. Also, `react-dom/test-utils` lost most of its exports in React 19. Only `act` remained there, and it now lives in `react` itself.

## Moderate Questions (151-300)

### 151: How do you organize tests for a feature?

A common setup for a feature like "cart":

- **Unit tests** for pure logic next to the code: `cartTotals.test.ts`, `cartReducer.test.ts`.
- **Hook tests** for custom hooks that have real logic: `useCart.test.tsx`.
- **Integration tests** for the main components with their children and mocked API: `CartPage.test.tsx`.
- **One or two e2e tests** for the most important flow: `e2e/checkout.spec.ts`.

Inside a test file, use `describe` blocks for scenarios ("when the cart is empty", "when the user is a guest"), and name tests by behavior.

### 152: How does the wrapper option of render work?

`wrapper` is a component that RTL wraps around your UI. It also wraps it again on `rerender`, which you wouldn't get if you wrote the providers inline in JSX:

```tsx
function Providers({ children }: { children: React.ReactNode }) {
  return <ThemeProvider theme="dark">{children}</ThemeProvider>;
}

const { rerender } = render(<Button />, { wrapper: Providers });
rerender(<Button disabled />); // still inside ThemeProvider
```

`renderHook` accepts the same `wrapper` option, which is how you give hooks access to context.

### 153: How do you test components connected to a Redux Toolkit store?

The Redux docs recommend using a **real store** instead of mocking `useSelector`. Create a `setupStore` function and a custom render:

```tsx
// store.ts
export function setupStore(preloadedState?: Partial<RootState>) {
  return configureStore({ reducer: rootReducer, preloadedState });
}

// test-utils.tsx
export function renderWithStore(
  ui: React.ReactElement,
  { preloadedState = {}, store = setupStore(preloadedState) } = {},
) {
  return {
    store,
    ...render(<Provider store={store}>{ui}</Provider>),
  };
}

// CartBadge.test.tsx
test("shows the item count", () => {
  renderWithStore(<CartBadge />, {
    preloadedState: { cart: { items: [{ id: 1, qty: 2 }] } },
  });
  expect(screen.getByText("2")).toBeInTheDocument();
});
```

Each test gets a fresh store, so state doesn't leak between tests. API calls made by thunks or RTK Query are mocked with MSW.

### 154: How do you test components that use a Zustand store?

Zustand stores are module-level singletons, so state stays between tests unless you reset it. The simplest way is to save the initial state and reset it after each test:

```ts
import { useCartStore } from "./cartStore";

const initialState = useCartStore.getState();

afterEach(() => {
  useCartStore.setState(initialState, true); // true = replace, not merge
});

test("adds an item", async () => {
  const user = userEvent.setup();
  render(<AddToCartButton productId={1} />);

  await user.click(screen.getByRole("button", { name: "Add to cart" }));
  expect(useCartStore.getState().items).toHaveLength(1);
});
```

You can also set state before rendering with `useCartStore.setState({ items: [...] })`. The Zustand docs also show a `__mocks__/zustand.ts` approach that resets all stores automatically.

### 155: How do you test components that use TanStack Query (React Query)?

Create a **new `QueryClient` for each test** and turn off retries:

```tsx
function createWrapper() {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });
  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  );
}

test("shows the todos", async () => {
  server.use(
    http.get("/api/todos", () => HttpResponse.json([{ id: 1, title: "Test" }])),
  );

  render(<Todos />, { wrapper: createWrapper() });
  expect(await screen.findByText("Test")).toBeInTheDocument();
});
```

A shared client would keep the cache between tests. Leaving retries on makes error tests slow, because the query retries 3 times with a growing delay before it shows the error.

### 156: How do you test a component that depends on routes and route params?

Use `createMemoryRouter` with the same route shape as your app:

```tsx
import { createMemoryRouter, RouterProvider } from "react-router";

test("loads the product from the URL", async () => {
  const router = createMemoryRouter(
    [{ path: "/products/:id", element: <ProductPage /> }],
    { initialEntries: ["/products/42"] },
  );

  render(<RouterProvider router={router} />);

  expect(
    await screen.findByRole("heading", { name: "Product 42" }),
  ).toBeInTheDocument();
});
```

This also works with loaders and actions if your routes use them. For simple components, `<MemoryRouter initialEntries={[...]}>` with `<Routes>` is enough.

### 157: How do you test that clicking something navigates to another page?

Render a small route setup with the target page, then check that the new page is shown:

```tsx
test("goes to the details page", async () => {
  const user = userEvent.setup();
  render(
    <MemoryRouter initialEntries={["/products"]}>
      <Routes>
        <Route path="/products" element={<ProductList />} />
        <Route path="/products/:id" element={<h1>Details page</h1>} />
      </Routes>
    </MemoryRouter>,
  );

  await user.click(screen.getByRole("link", { name: "Laptop" }));
  expect(
    screen.getByRole("heading", { name: "Details page" }),
  ).toBeInTheDocument();
});
```

This is better than mocking `useNavigate` and checking it was called, because it also catches wrong paths.

### 158: How do you set up MSW for Vitest or Jest?

Create the handlers, a server, and start it in the setup file:

```ts
// src/mocks/handlers.ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/user", () => HttpResponse.json({ name: "Anna" })),
];

// src/mocks/server.ts
import { setupServer } from "msw/node";
import { handlers } from "./handlers";

export const server = setupServer(...handlers);

// src/setupTests.ts
import { server } from "./mocks/server";

beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

`resetHandlers` removes handlers added inside tests, so each test starts with the default handlers.

### 159: How do you change an MSW response for just one test?

Use `server.use()` inside the test. Handlers added this way take priority over the default ones until `resetHandlers()` runs:

```ts
test("shows an empty state", async () => {
  server.use(http.get("/api/orders", () => HttpResponse.json([])));

  render(<Orders />);
  expect(await screen.findByText("You have no orders yet")).toBeInTheDocument();
});
```

Keep the happy path in the default handlers and override only for special cases like errors, empty lists or slow responses.

### 160: How do you test error responses with MSW?

Return an error status or a network error:

```ts
test("shows an error message when the request fails", async () => {
  server.use(
    http.get("/api/orders", () =>
      HttpResponse.json({ message: "Server error" }, { status: 500 })
    )
  );

  render(<Orders />);
  expect(await screen.findByRole("alert")).toHaveTextContent(/something went wrong/i);
});

test("shows an offline message on network error", async () => {
  server.use(http.get("/api/orders", () => HttpResponse.error()));

  render(<Orders />);
  expect(await screen.findByText(/check your connection/i)).toBeInTheDocument();
});
```

`HttpResponse.error()` makes `fetch` reject, like when the user is offline. A 500 status doesn't make `fetch` reject, so your code has to check `response.ok`.

### 161: What does onUnhandledRequest: "error" do in MSW?

It makes MSW print an error when a request is made that no handler matches. In Vitest or Jest this means you find out right away when a component calls an endpoint you forgot to mock, instead of the request silently failing or going to the real network.

The default is `"warn"`. Many teams set `"error"` in tests, so missing mocks can't go unnoticed.

### 162: How do you check what request body a component sent?

Read the request inside the handler, and either save it or check it:

```ts
test("sends the new todo to the API", async () => {
  let sentBody: unknown;
  server.use(
    http.post("/api/todos", async ({ request }) => {
      sentBody = await request.json();
      return HttpResponse.json({ id: 1, title: "Buy milk" }, { status: 201 });
    })
  );

  const user = userEvent.setup();
  render(<NewTodo />);
  await user.type(screen.getByLabelText("Title"), "Buy milk");
  await user.click(screen.getByRole("button", { name: "Add" }));

  await waitFor(() => expect(sentBody).toEqual({ title: "Buy milk" }));
});
```

Usually it's enough to check what the user sees after the request. Check the body when the exact data sent to the server matters, like for a payment or settings form.

### 163: How do you mock fetch without MSW?

Spy on the global `fetch`:

```ts
test("loads the user", async () => {
  const fetchSpy = vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(JSON.stringify({ name: "Anna" }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    })
  );

  render(<Profile />);

  expect(await screen.findByText("Anna")).toBeInTheDocument();
  expect(fetchSpy).toHaveBeenCalledWith("/api/user", expect.anything());
});
```

Restore it after the test with `mockRestore()` or the `restoreMocks` config option. This works for small cases, but it gets messy when a component makes several requests, which is where MSW is easier.

### 164: How do you mock axios?

You can mock the module:

```ts
import axios from "axios";
vi.mock("axios");

test("loads products", async () => {
  vi.mocked(axios.get).mockResolvedValue({ data: [{ id: 1, name: "Laptop" }] });

  render(<Products />);
  expect(await screen.findByText("Laptop")).toBeInTheDocument();
});
```

This breaks if the code uses `axios.create()` instances or interceptors, because those aren't mocked the same way. MSW avoids the problem completely, because axios makes a real request that MSW intercepts. That's why MSW is usually the better choice.

### 165: Why does vi.mock get hoisted and what is vi.hoisted for?

`vi.mock` (and `jest.mock`) calls are moved to the top of the file, before the imports. This is needed because the module must be mocked before anything imports it.

The side effect is that the mock factory can't use variables declared in the file, because they don't exist yet when it runs. `vi.hoisted` solves that by hoisting a variable too:

```ts
const { mockNavigate } = vi.hoisted(() => ({ mockNavigate: vi.fn() }));

vi.mock("react-router", async (importOriginal) => ({
  ...(await importOriginal<typeof import("react-router")>()),
  useNavigate: () => mockNavigate,
}));
```

In Jest, variables used in a `jest.mock` factory must have names starting with `mock`, which is Jest's rule for allowing lazy access.

### 166: How do you mock only part of a module?

Import the original module inside the factory and override only what you need:

```ts
// Vitest
vi.mock(import("./utils"), async (importOriginal) => {
  const actual = await importOriginal();
  return {
    ...actual,
    getToday: vi.fn(() => new Date("2026-01-15")),
  };
});

// Jest
jest.mock("./utils", () => ({
  ...jest.requireActual("./utils"),
  getToday: jest.fn(() => new Date("2026-01-15")),
}));
```

Passing `import("./utils")` to `vi.mock` instead of a string gives you type checking for the factory's return value.

### 167: How do you mock a default export?

Return an object with a `default` key from the factory:

```ts
vi.mock("./Chart", () => ({
  default: () => <div data-testid="chart-mock" />,
}));
```

For modules with both default and named exports, include both. In Jest with ES modules compiled by Babel or SWC, you sometimes also need `__esModule: true` in the factory, so the default import picks up `default` correctly.

### 168: What is the `__mocks__` folder?

It's a folder where you put manual mock implementations. When you call `vi.mock("./api")` or `jest.mock("./api")` without a factory, the runner looks for `__mocks__/api.ts` next to the module and uses it.

For node modules (like `axios` or `zustand`), the `__mocks__` folder goes in the project root (next to `node_modules`) for Jest, and in Jest those mocks are applied automatically. In Vitest the root `__mocks__` folder is also used, but you still have to call `vi.mock("axios")`.

### 169: When does it make sense to mock a child component?

Usually you shouldn't, because then you're not testing how the components work together. But it can make sense when the child:

- is very heavy or slow (maps, charts, rich text editors, video players)
- needs browser APIs jsdom doesn't have (canvas, WebGL)
- loads a third-party script or SDK
- is already well tested on its own and only makes the setup much harder

```tsx
vi.mock("./MapView", () => ({
  MapView: ({ markers }: { markers: unknown[] }) => (
    <div data-testid="map">{markers.length} markers</div>
  ),
}));
```

Keep the mock simple and still render something you can check, like the data it received.

### 170: What does vi.mocked do?

It's a TypeScript helper. It doesn't change anything at runtime. It tells TypeScript that the imported function is a mock, so you can call mock methods on it without type errors:

```ts
import { fetchUser } from "./api";
vi.mock("./api");

vi.mocked(fetchUser).mockResolvedValue({ id: 1, name: "Anna" });
```

Without it, TypeScript would say `mockResolvedValue` doesn't exist on `fetchUser`. In Jest the equivalent is `jest.mocked()`.

### 171: How do you mock environment variables in tests?

In Vitest, use `vi.stubEnv`:

```ts
afterEach(() => vi.unstubAllEnvs());

test("shows the beta banner when the flag is on", () => {
  vi.stubEnv("VITE_SHOW_BETA", "true");
  render(<App />);
  expect(screen.getByText(/beta/i)).toBeInTheDocument();
});
```

It updates both `process.env` and `import.meta.env`. In Jest you set `process.env.X` directly and restore the original value after the test. If the variable is read when a module loads (at the top of the file), you need to set it before importing that module, for example with `vi.resetModules()` and a dynamic import.

### 172: How do you mock global objects and browser APIs?

Use `vi.stubGlobal`, which also lets you restore everything easily:

```ts
afterEach(() => vi.unstubAllGlobals());

test("uses the Geolocation API", () => {
  vi.stubGlobal("navigator", {
    ...navigator,
    geolocation: {
      getCurrentPosition: vi.fn((success) =>
        success({ coords: { latitude: 52.5, longitude: 13.4 } })
      ),
    },
  });

  render(<NearbyStores />);
  // ...
});
```

In Jest, you can use `Object.defineProperty` or `jest.replaceProperty(object, "key", value)`.

### 173: How do you deal with matchMedia, ResizeObserver and IntersectionObserver missing in jsdom?

jsdom doesn't implement them, so components that use them crash. Add simple mocks in the setup file:

```ts
// setupTests.ts
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: vi.fn().mockImplementation((query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    addListener: vi.fn(),
    removeListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

class ResizeObserverMock {
  observe = vi.fn();
  unobserve = vi.fn();
  disconnect = vi.fn();
}
vi.stubGlobal("ResizeObserver", ResizeObserverMock);
```

These mocks only stop the crash. If a test depends on what these APIs report (like a breakpoint or an element becoming visible), make the mock controllable or test it in a real browser.

### 174: How do you set a fixed date in tests?

Use fake timers and set the system time:

```ts
beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(new Date("2026-03-15T10:00:00Z"));
});

afterEach(() => vi.useRealTimers());

test("shows 'today' for today's date", () => {
  render(<RelativeDate date={new Date("2026-03-15T08:00:00Z")} />);
  expect(screen.getByText("Today")).toBeInTheDocument();
});
```

In Jest: `jest.useFakeTimers({ now: new Date("2026-03-15") })` or `jest.setSystemTime()`. Without a fixed date, tests that depend on "today" break when the calendar moves forward.

### 175: How do you use fake timers together with user-event?

user-event waits between events using timers. With fake timers those waits never end, so the test hangs. Pass `advanceTimers` to `setup`:

```ts
beforeEach(() => vi.useFakeTimers());
afterEach(() => vi.useRealTimers());

test("works with fake timers", async () => {
  const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime });
  render(<Search />);

  await user.type(screen.getByRole("searchbox"), "react");
  // ...
});
```

In Jest you pass `jest.advanceTimersByTime`. Another option is `userEvent.setup({ delay: null })`, which skips the waits completely.

### 176: How do you test a debounced search input?

Use fake timers and advance time past the debounce delay:

```tsx
test("searches 300ms after the user stops typing", async () => {
  vi.useFakeTimers();
  const onSearch = vi.fn();
  const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime });
  render(<SearchInput onSearch={onSearch} />);

  await user.type(screen.getByRole("searchbox"), "rea");
  expect(onSearch).not.toHaveBeenCalled();

  await act(() => vi.advanceTimersByTimeAsync(300));

  expect(onSearch).toHaveBeenCalledTimes(1);
  expect(onSearch).toHaveBeenCalledWith("rea");
  vi.useRealTimers();
});
```

You check two things: nothing happens while typing, and exactly one call happens after the delay with the final value.

### 177: How do you test polling with setInterval?

```tsx
test("refreshes the status every 5 seconds", async () => {
  vi.useFakeTimers();
  let calls = 0;
  server.use(
    http.get("/api/status", () =>
      HttpResponse.json({ status: ++calls === 1 ? "pending" : "done" }),
    ),
  );

  render(<JobStatus />);
  await act(() => vi.advanceTimersByTimeAsync(0));
  expect(screen.getByText("pending")).toBeInTheDocument();

  await act(() => vi.advanceTimersByTimeAsync(5000));
  expect(screen.getByText("done")).toBeInTheDocument();
  vi.useRealTimers();
});
```

Use the async versions (`advanceTimersByTimeAsync`) because the timer callback starts a fetch, and its promise has to resolve too. Also test that polling stops after unmount.

### 178: How do you test that an effect cleans up after itself?

Check that the cleanup actually happens after `unmount`. For a subscription:

```tsx
test("unsubscribes on unmount", () => {
  const unsubscribe = vi.fn();
  const subscribe = vi.fn(() => unsubscribe);

  const { unmount } = render(<LivePrice subscribe={subscribe} />);
  expect(subscribe).toHaveBeenCalledTimes(1);

  unmount();
  expect(unsubscribe).toHaveBeenCalledTimes(1);
});
```

For timers, you can check that `vi.getTimerCount()` is 0 after unmount. Missing cleanup is a common cause of memory leaks and "state update on unmounted component" style bugs.

### 179: How do you test a custom hook that needs a provider?

Pass a `wrapper` to `renderHook`:

```tsx
test("returns the current user", async () => {
  const wrapper = ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={new QueryClient()}>
      {children}
    </QueryClientProvider>
  );

  const { result } = renderHook(() => useCurrentUser(), { wrapper });

  await waitFor(() => expect(result.current.isSuccess).toBe(true));
  expect(result.current.data?.name).toBe("Anna");
});
```

You can also pass `initialProps` and use `rerender(newProps)` to test how the hook reacts to changing arguments.

### 180: When should you test a hook directly instead of through a component?

Test a hook directly when it's a **reusable hook** with its own logic, like `useDebounce`, `usePagination` or `useLocalStorage`. It's used in many places, and testing it through every component would be repetitive.

If a hook is only used in one component and was extracted just to keep the component small, test it through the component. That way you can refactor the hook freely, and the test checks what the user actually sees.

### 181: How do you test a context provider itself?

Render the provider with a small test component that uses the context and shows its values:

```tsx
function TestConsumer() {
  const { theme, toggleTheme } = useTheme();
  return <button onClick={toggleTheme}>Theme: {theme}</button>;
}

test("toggles between light and dark", async () => {
  const user = userEvent.setup();
  render(
    <ThemeProvider>
      <TestConsumer />
    </ThemeProvider>,
  );

  const button = screen.getByRole("button");
  expect(button).toHaveTextContent("Theme: light");
  await user.click(button);
  expect(button).toHaveTextContent("Theme: dark");
});
```

Also test that the hook throws a helpful error when used outside the provider, if it's written to do that.

### 182: How do you test a form built with React Hook Form?

Test it like any other form. React Hook Form is an implementation detail. The only thing to remember is that validation is async, so use `findBy` or `waitFor`:

```tsx
test("submits valid data", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();
  render(<ProfileForm onSubmit={onSubmit} />);

  await user.type(screen.getByLabelText("Name"), "Anna");
  await user.click(screen.getByRole("button", { name: "Save" }));

  await waitFor(() => expect(onSubmit).toHaveBeenCalledWith({ name: "Anna" }));
});

test("does not submit when name is empty", async () => {
  const user = userEvent.setup();
  const onSubmit = vi.fn();
  render(<ProfileForm onSubmit={onSubmit} />);

  await user.click(screen.getByRole("button", { name: "Save" }));

  expect(await screen.findByText("Name is required")).toBeInTheDocument();
  expect(onSubmit).not.toHaveBeenCalled();
});
```

### 183: How do you test validation logic written with Zod?

Test the schema as plain code, separately from the form. It's fast and you can cover many cases:

```ts
import { signupSchema } from "./signupSchema";

test.each([
  ["", "Email is required"],
  ["abc", "Invalid email"],
])("email '%s' gives '%s'", (email, message) => {
  const result = signupSchema.safeParse({ email, password: "secret123" });
  expect(result.success).toBe(false);
  expect(result.error?.issues[0].message).toBe(message);
});

test("accepts valid data", () => {
  expect(
    signupSchema.safeParse({ email: "a@b.com", password: "secret123" }).success,
  ).toBe(true);
});
```

Then write just one or two form tests to check the errors show up in the UI.

### 184: How do you test a form that uses React 19 actions and useActionState?

Test it from the outside, like any form. Type, submit, then wait for the result. The action runs inside a transition, so use `findBy`:

```tsx
test("shows the result of the action", async () => {
  const user = userEvent.setup();
  render(<SubscribeForm />);

  await user.type(screen.getByLabelText("Email"), "anna@test.com");
  await user.click(screen.getByRole("button", { name: "Subscribe" }));

  expect(screen.getByRole("button", { name: /subscribing/i })).toBeDisabled();
  expect(
    await screen.findByText("Thanks for subscribing!"),
  ).toBeInTheDocument();
});
```

If the action calls an API, mock it with MSW. If it's a Server Action in Next.js, you usually test the action function separately and test the full flow with an e2e test.

### 185: How do you test useOptimistic?

Check that the UI updates right away, before the server answers, and that it rolls back if the request fails. Use an MSW handler with a delay so you can see the optimistic state:

```tsx
test("shows the message immediately and keeps it after saving", async () => {
  server.use(
    http.post("/api/messages", async () => {
      await delay(200);
      return HttpResponse.json({ id: 1, text: "Hi" });
    }),
  );
  const user = userEvent.setup();
  render(<Chat />);

  await user.type(screen.getByRole("textbox"), "Hi");
  await user.click(screen.getByRole("button", { name: "Send" }));

  expect(screen.getByText("Hi")).toBeInTheDocument(); // optimistic
  expect(screen.getByText("Sending...")).toBeInTheDocument();
  await waitForElementToBeRemoved(() => screen.queryByText("Sending..."));
  expect(screen.getByText("Hi")).toBeInTheDocument(); // confirmed
});
```

Write a second test where the handler returns an error and check that the message disappears and an error shows.

### 186: How do you test lazy-loaded components with Suspense?

Render the component inside `Suspense` and wait for the lazy content:

```tsx
const Settings = lazy(() => import("./Settings"));

test("loads the settings page", async () => {
  render(
    <Suspense fallback={<p>Loading...</p>}>
      <Settings />
    </Suspense>,
  );

  expect(screen.getByText("Loading...")).toBeInTheDocument();
  expect(
    await screen.findByRole("heading", { name: "Settings" }),
  ).toBeInTheDocument();
});
```

The dynamic import resolves quickly in tests, but still asynchronously, so `findBy` is needed.

### 187: How do you test a component that uses the use() API with a promise?

Pass a promise and render inside `Suspense`. With React 19 and RTL, wrap the render in an async `act` so React can handle the suspended promise:

```tsx
function UserName({ userPromise }: { userPromise: Promise<{ name: string }> }) {
  const user = use(userPromise);
  return <p>{user.name}</p>;
}

test("shows the user after the promise resolves", async () => {
  const promise = Promise.resolve({ name: "Anna" });

  await act(async () => {
    render(
      <Suspense fallback={<p>Loading...</p>}>
        <UserName userPromise={promise} />
      </Suspense>,
    );
  });

  expect(screen.getByText("Anna")).toBeInTheDocument();
});
```

Create the promise outside the component (in the test), the same way the real app creates it in a parent or a loader. A promise created during render would be new on every render and never settle.

### 188: How do you test an error boundary?

Render a child that throws, and check the fallback UI. React logs the error to the console, so silence `console.error` for this test:

```tsx
function Broken(): never {
  throw new Error("Boom");
}

test("shows the fallback when a child throws", () => {
  const spy = vi.spyOn(console, "error").mockImplementation(() => {});

  render(
    <ErrorBoundary fallback={<p>Something went wrong</p>}>
      <Broken />
    </ErrorBoundary>,
  );

  expect(screen.getByText("Something went wrong")).toBeInTheDocument();
  spy.mockRestore();
});
```

If the boundary has a "Try again" button, also test that clicking it renders the children again once the error is gone.

### 189: How do you test a modal that uses a portal?

Use `screen`, which searches the whole `document.body`, so it finds content rendered into a portal:

```tsx
test("opens and closes the confirm dialog", async () => {
  const user = userEvent.setup();
  render(<DeleteButton />);

  await user.click(screen.getByRole("button", { name: "Delete" }));

  const dialog = screen.getByRole("dialog", { name: "Delete item?" });
  expect(dialog).toBeInTheDocument();

  await user.click(within(dialog).getByRole("button", { name: "Cancel" }));
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

The queries returned by `render` are bound to `baseElement`, which is also `document.body` by default, so they would work too. `screen` just makes it obvious that you're searching the whole page. But `container.querySelector` would not find the dialog, because the portal content is outside the container. If the portal target is a custom element like `#modal-root`, create it in the test or setup file before rendering.

### 190: How do you test a custom select or combobox component?

Use the ARIA roles the component should have: `combobox`, `listbox`, `option`:

```tsx
test("selects a country", async () => {
  const user = userEvent.setup();
  render(<CountrySelect />);

  await user.click(screen.getByRole("combobox", { name: "Country" }));
  await user.click(await screen.findByRole("option", { name: "Germany" }));

  expect(screen.getByRole("combobox", { name: "Country" })).toHaveTextContent(
    "Germany",
  );
});

test("can be used with the keyboard", async () => {
  const user = userEvent.setup();
  render(<CountrySelect />);

  await user.tab();
  await user.keyboard("{ArrowDown}{ArrowDown}{Enter}");
  expect(screen.getByRole("combobox")).toHaveTextContent("France");
});
```

If `getByRole("option")` can't find anything, the component may be missing ARIA roles, which is a real accessibility bug.

### 191: How do you test a data table?

Use table roles: `table`, `row`, `columnheader`, `cell`. Find a row by its content and then look inside it with `within`:

```tsx
test("sorts by price when the header is clicked", async () => {
  const user = userEvent.setup();
  render(<ProductTable products={products} />);

  await user.click(screen.getByRole("columnheader", { name: /price/i }));

  const rows = screen.getAllByRole("row").slice(1); // skip header row
  expect(within(rows[0]).getAllByRole("cell")[1]).toHaveTextContent("$5");
  expect(screen.getByRole("columnheader", { name: /price/i })).toHaveAttribute(
    "aria-sort",
    "ascending",
  );
});
```

### 192: How do you test keyboard navigation and tab order?

Use `user.tab()` and check focus:

```tsx
test("moves focus through the form in order", async () => {
  const user = userEvent.setup();
  render(<LoginForm />);

  await user.tab();
  expect(screen.getByLabelText("Email")).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText("Password")).toHaveFocus();

  await user.tab();
  expect(screen.getByRole("button", { name: "Log in" })).toHaveFocus();

  await user.tab({ shift: true });
  expect(screen.getByLabelText("Password")).toHaveFocus();
});
```

This catches things like a custom button that can't be focused, or a wrong `tabIndex`.

### 193: How do you test keyboard shortcuts?

Send the key combination with `user.keyboard` and check the result:

```tsx
test("opens the command palette with Ctrl+K", async () => {
  const user = userEvent.setup();
  render(<App />);

  await user.keyboard("{Control>}k{/Control}");
  expect(
    screen.getByRole("dialog", { name: "Command palette" }),
  ).toBeInTheDocument();

  await user.keyboard("{Escape}");
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

If the shortcut listens on `document`, this works without focusing anything first, because events go to `document.body` when nothing is focused.

### 194: How do you test drag and drop?

In jsdom it's hard. There's no layout, so coordinates and drop targets don't work like in a browser, and many drag-and-drop libraries rely on pointer positions or the HTML5 drag API.

Options:

- If the library supports keyboard dragging (like dnd-kit), test that in RTL: focus, press Space, use arrow keys, press Space again.
- Test the logic (like a `moveItem(list, from, to)` function) separately.
- Test the real drag in Playwright with `locator.dragTo(target)` or manual mouse moves.

```ts
await page.getByText("Task A").dragTo(page.getByTestId("column-done"));
await expect(page.getByTestId("column-done")).toContainText("Task A");
```

### 195: What are the limits of testing CSS and layout in jsdom?

jsdom doesn't load your stylesheets, doesn't calculate layout and doesn't paint. So:

- `getBoundingClientRect()`, `offsetWidth` and similar return 0
- media queries don't apply
- `:hover`, transitions and animations don't run
- `toBeVisible` only knows about inline styles and styles you inject in the test

So you can't test things like "the sidebar collapses on mobile" or "the text is truncated" in jsdom. Use Vitest Browser Mode, Playwright or visual regression tests for that.

### 196: How do you handle CSS, image and other asset imports in Jest?

Jest runs files through Node, which doesn't know how to import `.css` or `.png` files. Map them with `moduleNameMapper`:

```js
// jest.config.js
module.exports = {
  moduleNameMapper: {
    "\\.module\\.(css|scss)$": "identity-obj-proxy",
    "\\.(css|scss)$": "<rootDir>/test/styleMock.js",
    "\\.(png|jpg|svg|webp)$": "<rootDir>/test/fileMock.js",
  },
};
```

`identity-obj-proxy` returns the class name as the value, so `styles.button` becomes `"button"`. Vitest handles all of this through Vite, so you don't need extra config there. CSS processing can even be turned off with `test.css` options to make tests faster.

### 197: How do you configure path aliases like @/components in tests?

In Vitest, aliases from `resolve.alias` in the Vite config work automatically, because tests use the same config. If you define aliases in `tsconfig.json` paths, add the `vite-tsconfig-paths` plugin so Vite (and Vitest) read them.

In Jest, add them to `moduleNameMapper`:

```js
moduleNameMapper: {
  "^@/(.*)$": "<rootDir>/src/$1",
},
```

If you forget this, tests fail with "Cannot find module '@/components/Button'" even though the app builds fine.

### 198: Why do you get "SyntaxError: Cannot use import statement outside a module" in Jest?

By default Jest doesn't transform files in `node_modules`, and Jest's ESM support is still experimental. When a dependency only ships ES modules, Jest tries to run `import` statements as CommonJS and fails.

Fixes:

- Tell Jest to transform that package:

```js
transformIgnorePatterns: ["/node_modules/(?!(nanoid|some-esm-lib)/)"],
```

- Map the package to a CommonJS build with `moduleNameMapper`, if it has one.
- Move to Vitest, which handles ESM natively.

### 199: How do you use different test environments for different files?

In Vitest you can set the environment per file with a comment at the top:

```ts
// @vitest-environment node
import { hashPassword } from "./crypto";
```

In Jest:

```ts
/**
 * @jest-environment node
 */
```

This is useful when most tests need jsdom, but some files test Node-only code, or when you want pure logic tests to run in the faster `node` environment.

### 200: What are Vitest projects?

Projects let you run several test configurations in one Vitest run. For example, unit tests in Node, component tests in jsdom and browser tests in Chromium:

```ts
export default defineConfig({
  test: {
    projects: [
      {
        extends: true,
        test: {
          name: "unit",
          include: ["src/**/*.unit.test.ts"],
          environment: "node",
        },
      },
      {
        extends: true,
        test: {
          name: "dom",
          include: ["src/**/*.test.tsx"],
          environment: "jsdom",
        },
      },
    ],
  },
});
```

`extends: true` makes the project inherit the root config (plugins, aliases). In a monorepo you can also point `projects` to package folders, like `["packages/*"]`. This replaced the older `workspace` option, which was removed in Vitest 4.

### 201: How do you test client components in a Next.js app?

Use Vitest or Jest with React Testing Library, like any React app. Next.js has official setup guides for both (`next/jest` for Jest, and `@vitejs/plugin-react` with jsdom for Vitest).

Hooks from `next/navigation` need the Next.js router, which doesn't exist in tests, so you mock them:

```tsx
const push = vi.fn();
vi.mock("next/navigation", () => ({
  useRouter: () => ({
    push,
    replace: vi.fn(),
    back: vi.fn(),
    refresh: vi.fn(),
    prefetch: vi.fn(),
  }),
  usePathname: () => "/dashboard",
  useSearchParams: () => new URLSearchParams("tab=billing"),
}));

test("goes to settings", async () => {
  const user = userEvent.setup();
  render(<DashboardNav />);
  await user.click(screen.getByRole("button", { name: "Settings" }));
  expect(push).toHaveBeenCalledWith("/settings");
});
```

### 202: How do you test React Server Components?

Async Server Components are hard to unit test. React Testing Library and jsdom are built for client rendering, and the Next.js docs say Vitest doesn't currently support async Server Components. They recommend e2e tests for them.

What works well in practice:

- Move data fetching and logic into plain functions and unit test those.
- Keep the presentational part as a normal (sync) component that takes data as props, and test it with RTL.
- Test the page as a whole with Playwright, where the server renders everything for real.

Synchronous Server Components that don't use server-only APIs can be rendered with RTL like normal components.

### 203: How do you test Server Actions?

A Server Action is an async function, so you can call it directly in a unit test and mock its dependencies (database, `revalidatePath`, `cookies`):

```ts
vi.mock("next/cache", () => ({ revalidatePath: vi.fn() }));
vi.mock("@/lib/db", () => ({ db: { todo: { create: vi.fn() } } }));

test("creates a todo and revalidates the list", async () => {
  const formData = new FormData();
  formData.set("title", "Buy milk");

  const result = await createTodo(null, formData);

  expect(db.todo.create).toHaveBeenCalledWith({ data: { title: "Buy milk" } });
  expect(revalidatePath).toHaveBeenCalledWith("/todos");
  expect(result).toEqual({ ok: true });
});
```

Also test validation (bad form data returns an error, not a throw) and auth checks. Then cover the full flow, from submitting the form to seeing the result, with one e2e test.

### 204: How do you test code that uses localStorage?

jsdom has a working `localStorage`, so you can use it directly. Just clear it between tests:

```ts
afterEach(() => localStorage.clear());

test("remembers the selected theme", async () => {
  const user = userEvent.setup();
  render(<ThemeToggle />);

  await user.click(screen.getByRole("button", { name: /dark mode/i }));
  expect(localStorage.getItem("theme")).toBe("dark");
});

test("reads the saved theme", () => {
  localStorage.setItem("theme", "dark");
  render(<ThemeToggle />);
  expect(screen.getByRole("button", { name: /light mode/i })).toBeInTheDocument();
});
```

To test error cases, like storage being full or blocked, spy on `Storage.prototype.setItem` and make it throw.

### 205: How do you test code that reads or changes window.location?

In jsdom, changing `window.location.href` to another page doesn't work. It logs a "not implemented: navigation" error. And `window.location` can't be reassigned directly.

Options:

- Set the URL for reading with `window.history.pushState({}, "", "/products?page=2")`.
- Wrap navigation in your own small function (like `redirectTo(url)`) and mock that in tests.
- Replace `location` for the test:

```ts
const assign = vi.fn();
vi.stubGlobal("location", { ...window.location, assign });

// ... trigger the redirect
expect(assign).toHaveBeenCalledWith("https://payments.example.com/checkout");
vi.unstubAllGlobals();
```

Full page redirects are often better checked in e2e tests.

### 206: How do you test components that use translations (i18n)?

Two common approaches:

1. **Use the real i18n setup** with the real translation files (for example, initialize i18next with English resources in the setup file). Tests look for real English text, which is what the user sees, and they catch missing keys.
2. **Mock the translation function** to return the key. This is simpler, but tests then look for keys like `"cart.empty"` and won't catch missing translations.

The first approach is closer to real usage and usually better. Make sure the language is fixed in tests, so the browser language of the machine running them doesn't matter.

### 207: What does the "not wrapped in act(...)" warning mean and how do you fix it?

React shows it when a state update happens in a test and React didn't expect it, usually because it came from something async that finished **after** your test stopped waiting.

Common causes and fixes:

- A fetch resolves after the last assertion. Wait for the final UI with `await screen.findBy...`.
- A `user-event` call wasn't awaited. Add `await`.
- A timer fires a state update. Wrap `vi.advanceTimersByTime` in `act`.
- A component keeps updating after the test is over. Make sure the test waits for loading to finish.

Don't fix it by wrapping things in `act` at random. Find what's updating and wait for its result in the UI.

### 208: What are the most common mistakes people make with React Testing Library?

- Using `getByTestId` or `container.querySelector` when `getByRole` would work.
- Using `fireEvent` instead of `user-event`.
- Forgetting to `await` `findBy`, `waitFor` or `user-event` calls.
- Using `waitFor(() => getBy...)` instead of `findBy`.
- Putting side effects (like clicks) inside `waitFor`.
- Using `queryBy` for things that should exist. Use `getBy`, which gives a better error.
- Wrapping `render` or `fireEvent` in `act`. They're already wrapped.
- Calling `cleanup` manually when it already runs automatically.
- Using `expect(el).toBeTruthy()` instead of a jest-dom matcher like `toBeInTheDocument()`.

### 209: Why shouldn't you put side effects inside waitFor?

`waitFor` can call its callback many times, so any side effect inside it runs many times too:

```tsx
// Bad: may click several times
await waitFor(async () => {
  await user.click(button);
  expect(screen.getByText("Saved")).toBeInTheDocument();
});

// Good: act once, then wait for the result
await user.click(button);
await waitFor(() => expect(screen.getByText("Saved")).toBeInTheDocument());
```

Put only assertions inside `waitFor`.

### 210: Why should you keep only one assertion in a waitFor callback?

If the callback has several assertions, and the first one fails, `waitFor` keeps retrying until the timeout. You then wait the full timeout before you see the error, and the error message is less clear.

```tsx
// Better
await waitFor(() => expect(onSubmit).toHaveBeenCalledTimes(1));
expect(onSubmit).toHaveBeenCalledWith({ name: "Anna" });
```

Wait for the one thing that tells you the async work is done, then do the other assertions outside.

### 211: Why shouldn't you wrap render or user-event calls in act?

They're already wrapped. Wrapping them again adds noise and doesn't fix anything:

```tsx
// Not needed
act(() => {
  render(<App />);
});

// Just do this
render(<App />);
```

People often add `act` to silence the act warning, but the warning usually comes from async work that finished later. The real fix is to wait for the result with `findBy` or `waitFor`.

### 212: How do you find elements that are hidden from the accessibility tree?

By default, `getByRole` ignores elements that are hidden from assistive technology (`display: none`, `aria-hidden="true"`, the `hidden` attribute and so on). If you need them, pass `hidden: true`:

```tsx
screen.getByRole("dialog", { hidden: true });
```

This is rarely needed. If you find yourself using it a lot, check whether your test should actually be asserting that the element is hidden.

### 213: How do you write a custom matcher?

Use `expect.extend`:

```ts
expect.extend({
  toBeWithinRange(received: number, floor: number, ceiling: number) {
    const pass = received >= floor && received <= ceiling;
    return {
      pass,
      message: () =>
        `expected ${received} ${pass ? "not " : ""}to be within ${floor} - ${ceiling}`,
    };
  },
});

expect(score).toBeWithinRange(0, 100);
```

For TypeScript in Vitest, declare the matcher in a `.d.ts` file by extending the `Assertion` and `AsymmetricMatchersContaining` interfaces from `vitest`. Custom matchers are worth it when the same complex check appears in many tests.

### 214: What are asymmetric matchers?

They let you match part of a value instead of the exact value:

```ts
expect(onSubmit).toHaveBeenCalledWith(
  expect.objectContaining({
    email: "anna@test.com",
    createdAt: expect.any(Date),
    id: expect.any(String),
  }),
);

expect(tags).toEqual(expect.arrayContaining(["react", "testing"]));
expect(message).toEqual(expect.stringMatching(/^Order #\d+ placed$/));
```

They're useful when part of the data is random or not relevant to the test, like IDs and timestamps.

### 215: How do you test that a function throws or a promise rejects?

For sync code, pass a function to `expect`:

```ts
expect(() => parsePrice("abc")).toThrow("Invalid price");
expect(() => parsePrice("abc")).toThrow(ValidationError);
```

For async code, use `rejects` and `await` it:

```ts
await expect(fetchUser(999)).rejects.toThrow("User not found");
```

If you write `expect(parsePrice("abc"))` without the arrow function, the error is thrown before `expect` can catch it, and the test fails.

### 216: What do expect.assertions and expect.hasAssertions do?

They make sure the assertions you wrote actually ran. This matters in callbacks and `try`/`catch` blocks, where a test can pass without checking anything:

```ts
test("calls the callback with an error", async () => {
  expect.assertions(1);

  try {
    await loadData();
  } catch (e) {
    expect(e).toBeInstanceOf(NetworkError);
  }
});
```

If `loadData` doesn't throw, the `catch` never runs and the test fails because 0 assertions ran. Usually `await expect(...).rejects` is cleaner and you don't need this.

### 217: How do you test that a component logs a warning?

Spy on the console method and check the call:

```ts
test("warns when both value and defaultValue are passed", () => {
  const warn = vi.spyOn(console, "warn").mockImplementation(() => {});

  render(<Input value="a" defaultValue="b" onChange={() => {}} />);

  expect(warn).toHaveBeenCalledWith(expect.stringContaining("value and defaultValue"));
  warn.mockRestore();
});
```

`mockImplementation(() => {})` keeps the warning out of the test output.

### 218: What are property matchers in snapshots?

When an object has values that change every run, like IDs or dates, you can tell the snapshot to only check their type:

```ts
expect(createOrder()).toMatchSnapshot({
  id: expect.any(String),
  createdAt: expect.any(Date),
});
```

The snapshot stores `Any<String>` and `Any<Date>` for those fields and compares the rest exactly. This stops snapshots from failing on every run.

### 219: How do you use Faker in tests without making them random?

Random data can make a test fail only sometimes, which is hard to debug. Set a fixed seed:

```ts
import { faker } from "@faker-js/faker";

beforeEach(() => {
  faker.seed(123);
});

const user = { name: faker.person.fullName(), email: faker.internet.email() };
```

With a seed, Faker gives the same values every run. Also, don't write assertions that depend on the exact generated values. Use the data you pass in: `screen.getByText(user.name)`.

### 220: What does a good integration test for a filtered list look like?

It renders the real page, uses MSW for the API, and checks what the user sees after interacting:

```tsx
test("filters products by category", async () => {
  server.use(
    http.get("/api/products", ({ request }) => {
      const category = new URL(request.url).searchParams.get("category");
      const all = [
        { id: 1, name: "Laptop", category: "tech" },
        { id: 2, name: "Chair", category: "home" },
      ];
      return HttpResponse.json(
        category ? all.filter((p) => p.category === category) : all,
      );
    }),
  );
  const user = userEvent.setup();
  render(<ProductsPage />);

  expect(await screen.findByText("Laptop")).toBeInTheDocument();
  expect(screen.getByText("Chair")).toBeInTheDocument();

  await user.selectOptions(
    screen.getByRole("combobox", { name: "Category" }),
    "home",
  );

  await waitFor(() =>
    expect(screen.queryByText("Laptop")).not.toBeInTheDocument(),
  );
  expect(screen.getByText("Chair")).toBeInTheDocument();
});
```

It tests the select, the state, the request with the right query param and the rendering, all at once.

### 221: What should you mock and what should you keep real in an integration test?

**Keep real**: your own components, hooks, context providers, state management (Redux, Zustand, React Query), routing and form libraries.

**Mock**:

- the network (with MSW)
- browser APIs jsdom doesn't support
- time, when it matters
- third-party services and heavy widgets (payment SDKs, maps, analytics)

The rule of thumb is to mock at the edges of your app, not in the middle. Every mock you add is a place where your test and production can behave differently.

### 222: What is the difference between shallow rendering and full rendering?

**Shallow rendering** (from Enzyme or the old `react-test-renderer/shallow`) renders only one level. Child components are not rendered, so you see `<UserCard />` instead of its HTML.

**Full rendering** (what React Testing Library does) renders the whole tree into the DOM, down to real HTML elements.

React Testing Library doesn't support shallow rendering on purpose. Shallow tests check how components are wired together, not what the user gets, and they break on refactors. If a child is truly heavy, you mock that one module instead.

### 223: How do you set coverage thresholds?

```ts
// vitest.config.ts
test: {
  coverage: {
    provider: "v8",
    thresholds: {
      lines: 80,
      branches: 75,
      functions: 80,
      statements: 80,
    },
  },
},
```

If coverage falls below a threshold, the run fails. In Jest the option is `coverageThreshold.global`. You can also set thresholds for specific folders, for example higher ones for `src/lib/**` where the business logic lives. Vitest also has `thresholds.autoUpdate`, which raises the numbers in your config as coverage goes up.

### 224: What is the difference between v8 and istanbul coverage?

- **v8** uses the coverage data that the V8 JavaScript engine collects while the code runs. It doesn't need to change your code first, so it's fast. Since Vitest 4, v8 coverage uses AST-based remapping by default, so its results are about as accurate as Istanbul's. It's the default in Vitest.
- **istanbul** adds counters to your code before it runs (instrumentation). It works in any JavaScript runtime, not only V8, but it's slower.

Jest uses Babel-based Istanbul by default and has `coverageProvider: "v8"` as an option.

### 225: How do Vitest and Jest run tests in parallel?

Both run **test files** in parallel, in separate workers (threads or child processes). Tests **inside** a file run one after another by default.

Each file gets its own module registry, so module-level state (like a Zustand store) doesn't leak between files. It can still leak between tests in the same file. Vitest also has `describe.concurrent` / `test.concurrent` to run tests in the same file in parallel. That only makes sense for async tests that don't share state or the DOM, so it's rarely used for component tests.

### 226: How do you split a big test suite across several CI machines?

Use sharding:

```bash
# Vitest
npx vitest run --shard=1/4
npx vitest run --shard=2/4

# Jest
npx jest --shard=1/4
```

Each machine runs a quarter of the test files. In GitHub Actions you usually use a matrix to start the 4 jobs. To combine coverage or reports from the shards, Vitest has the `blob` reporter and `vitest --merge-reports`.

### 227: How do you run only the tests affected by your changes?

```bash
npx vitest related src/components/Cart.tsx --run   # tests that import this file
npx vitest --changed                                # tests affected by uncommitted changes
npx vitest --changed origin/main                    # affected since a branch

npx jest --onlyChanged
npx jest --findRelatedTests src/components/Cart.tsx
```

`related` is popular in pre-commit hooks with lint-staged. In CI it's usually safer to run everything, or use your monorepo tool (Nx, Turborepo) to find affected projects.

### 228: What is the Vitest UI?

It's a web interface for Vitest:

```bash
npm i -D @vitest/ui
npx vitest --ui
```

It shows all test files and their results, lets you filter and re-run tests, shows the console output and errors per test, displays the module graph and the coverage report. It's handy when you work with a big suite and the terminal output gets hard to read.

### 229: How do you debug a failing test?

1. Read the error. RTL prints the current DOM when a query fails.
2. Add `screen.debug()` before the failing line to see the DOM at that moment.
3. Use `logRoles` or `screen.logTestingPlaygroundURL()` when you can't find the right query.
4. Run only that test with `.only` or `-t "name"`.
5. Use a real debugger: in VS Code, the Vitest extension lets you set breakpoints and debug a single test. For Jest, use a JavaScript Debug Terminal or `node --inspect-brk node_modules/.bin/jest --runInBand`.
6. If it only fails together with other tests, look for shared state that isn't reset.

### 230: How do you test TypeScript types?

Vitest has type tests with `expectTypeOf` and `assertType`. They're checked by the TypeScript compiler, not at runtime:

```ts
// utils.test-d.ts
import { expectTypeOf, test } from "vitest";
import { pick } from "./utils";

test("pick returns only the picked keys", () => {
  const result = pick({ a: 1, b: "x", c: true }, ["a", "b"]);
  expectTypeOf(result).toEqualTypeOf<{ a: number; b: string }>();
});
```

Run them with `vitest --typecheck`. This is useful for libraries and shared utilities with complex generic types, like a typed `useForm` or an API client.

### 231: How can Storybook stories be used as tests?

Stories already describe a component in different states, so you can reuse them in tests.

- **Portable stories**: import stories into Vitest or Jest with `composeStories` and render them with RTL.

```tsx
import { composeStories } from "@storybook/react-vite";
import * as stories from "./Button.stories";

const { Primary, Disabled } = composeStories(stories);

test("disabled button cannot be clicked", () => {
  render(<Disabled />);
  expect(screen.getByRole("button")).toBeDisabled();
});
```

- **Play functions**: write interactions inside the story itself. The Storybook Vitest addon (`@storybook/addon-vitest`) runs all stories and their play functions as tests in a real browser using Vitest Browser Mode.

This means you write the setup once and use it for docs, manual checks and automated tests.

### 232: What is visual regression testing?

Visual regression testing takes screenshots of pages or components and compares them with approved "baseline" screenshots. If pixels differ more than a set threshold, the test fails and shows you a diff image.

It catches things other tests can't, like broken CSS, wrong colors, overlapping elements or a layout that broke on mobile. Tools: Playwright's `toHaveScreenshot`, Vitest Browser Mode's `toMatchScreenshot`, and services like Chromatic or Percy. The main challenge is keeping screenshots stable, because fonts, animations and dynamic data cause false failures.

### 233: How do you run accessibility checks in Playwright?

Use `@axe-core/playwright`:

```ts
import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("checkout page has no detectable a11y issues", async ({ page }) => {
  await page.goto("/checkout");

  const results = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa"])
    .exclude("#third-party-chat")
    .analyze();

  expect(results.violations).toEqual([]);
});
```

In a real browser axe can also check color contrast, which jsdom can't. Automated checks find only part of the problems (often quoted as around a third to a half), so they don't replace manual testing with a keyboard and screen reader.

### 234: What are the most important settings in playwright.config.ts?

```ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: process.env.CI ? [["html"], ["github"]] : "list",
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "webkit", use: { ...devices["Desktop Safari"] } },
  ],
  webServer: {
    command: "npm run build && npm run start",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
});
```

`forbidOnly` fails the run if someone committed `test.only`. `trace: "on-first-retry"` records a trace only when a test fails and is retried, which keeps CI fast.

### 235: How do you filter and chain locators in Playwright?

```ts
// a list item that contains "Laptop", then the button inside it
await page
  .getByRole("listitem")
  .filter({ hasText: "Laptop" })
  .getByRole("button", { name: "Add to cart" })
  .click();

// a row that contains a specific cell
const row = page.getByRole("row").filter({
  has: page.getByRole("cell", { name: "anna@test.com" }),
});
await row.getByRole("button", { name: "Edit" }).click();

// items that do NOT contain some text
page.getByRole("listitem").filter({ hasNotText: "Out of stock" });
```

You can also use `.first()`, `.last()` and `.nth(i)`, but it's better to filter by content, so the test doesn't depend on order.

### 236: What is strict mode for locators in Playwright?

Actions like `click()` and `fill()` fail if the locator matches more than one element:

```
Error: strict mode violation: getByRole('button', { name: 'Delete' }) resolved to 3 elements
```

This is good. It stops your test from clicking the wrong element by accident. Fix it by making the locator more specific (with `filter` or by chaining from a parent), not by adding `.first()` everywhere.

### 237: What are expect.poll and toPass in Playwright?

They let you retry things that aren't locators.

`expect.poll` calls a function until its result matches:

```ts
await expect
  .poll(
    async () => {
      const res = await page.request.get("/api/jobs/42");
      return (await res.json()).status;
    },
    { timeout: 30_000 },
  )
  .toBe("done");
```

`toPass` retries a whole block of code until it stops throwing:

```ts
await expect(async () => {
  await page.getByRole("button", { name: "Refresh" }).click();
  await expect(page.getByText("Report ready")).toBeVisible({ timeout: 1000 });
}).toPass({ timeout: 20_000 });
```

Use them for things like background jobs, emails or anything that becomes ready later.

### 238: What are soft assertions?

A soft assertion records a failure but doesn't stop the test:

```ts
await expect.soft(page.getByTestId("total")).toHaveText("$120.00");
await expect.soft(page.getByTestId("tax")).toHaveText("$20.00");
await page.getByRole("button", { name: "Pay" }).click();
```

At the end the test is still marked as failed, and you see all failed checks at once instead of only the first one. They're useful for pages where you check many independent values.

### 239: What built-in fixtures does Playwright give you?

- `page`: a new tab in a new, isolated browser context
- `context`: the browser context (cookies, storage, permissions) the page belongs to
- `browser`: the browser instance, shared across tests in a worker
- `browserName`: `"chromium"`, `"firefox"` or `"webkit"`
- `request`: an `APIRequestContext` for making HTTP calls without a page

```ts
test("api and ui", async ({ page, request, browserName }) => {
  test.skip(browserName === "webkit", "Feature not supported in Safari yet");
  await request.post("/api/reset");
  await page.goto("/");
});
```

Playwright only sets up the fixtures your test actually asks for.

### 240: How do you create a custom fixture in Playwright?

Extend the base `test` with `test.extend`:

```ts
// fixtures.ts
import { test as base } from "@playwright/test";
import { TodoPage } from "./pages/TodoPage";

type Fixtures = { todoPage: TodoPage };

export const test = base.extend<Fixtures>({
  todoPage: async ({ page }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.goto();
    await todoPage.addTodo("First todo");
    await use(todoPage); // the test runs here
    await todoPage.removeAll(); // cleanup after the test
  },
});

export { expect } from "@playwright/test";
```

```ts
import { test, expect } from "./fixtures";

test("can complete a todo", async ({ todoPage }) => {
  await todoPage.complete("First todo");
  await expect(todoPage.completedItems).toHaveCount(1);
});
```

Everything before `use` is setup, everything after is teardown. Fixtures can depend on other fixtures.

### 241: What is the Page Object Model?

It's a pattern where each page (or big section) of the app gets a class that contains its locators and actions. Tests use these methods instead of raw locators:

```ts
export class LoginPage {
  constructor(private page: Page) {}

  readonly email = this.page.getByLabel("Email");
  readonly password = this.page.getByLabel("Password");
  readonly submit = this.page.getByRole("button", { name: "Log in" });

  async goto() {
    await this.page.goto("/login");
  }

  async login(email: string, password: string) {
    await this.email.fill(email);
    await this.password.fill(password);
    await this.submit.click();
  }
}
```

When the UI changes, you update one class instead of many tests. Keep assertions mostly in the tests, and don't build deep class hierarchies. Simple page objects work best.

### 242: How do you avoid logging in through the UI in every Playwright test?

Log in once in a setup project, save the browser state, and reuse it:

```ts
// e2e/auth.setup.ts
import { test as setup, expect } from "@playwright/test";

const authFile = "playwright/.auth/user.json";

setup("authenticate", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill(process.env.E2E_USER!);
  await page.getByLabel("Password").fill(process.env.E2E_PASSWORD!);
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByText("Dashboard")).toBeVisible();
  await page.context().storageState({ path: authFile });
});
```

```ts
// playwright.config.ts
projects: [
  { name: "setup", testMatch: /.*\.setup\.ts/ },
  {
    name: "chromium",
    use: { ...devices["Desktop Chrome"], storageState: "playwright/.auth/user.json" },
    dependencies: ["setup"],
  },
],
```

`storageState` saves cookies and localStorage (and IndexedDB if you pass `indexedDB: true`). Add `playwright/.auth` to `.gitignore`.

### 243: How do you mock API responses in Playwright?

Use `page.route`:

```ts
test("shows an empty state", async ({ page }) => {
  await page.route("**/api/orders", (route) => route.fulfill({ json: [] }));

  await page.goto("/orders");
  await expect(page.getByText("You have no orders yet")).toBeVisible();
});

test("shows an error", async ({ page }) => {
  await page.route("**/api/orders", (route) =>
    route.fulfill({ status: 500, json: { message: "Server error" } }),
  );
  await page.goto("/orders");
  await expect(page.getByRole("alert")).toBeVisible();
});
```

Set up routes **before** the page makes the request, usually before `goto`. You can also block requests with `route.abort()`. Mocking in e2e is useful for edge cases that are hard to create with a real backend.

### 244: How do you change a real API response in Playwright?

Fetch the real response with `route.fetch()`, change it and return it:

```ts
await page.route("**/api/user", async (route) => {
  const response = await route.fetch();
  const json = await response.json();
  json.plan = "enterprise";
  await route.fulfill({ response, json });
});
```

This keeps the real backend in the loop but lets you force a specific case, like a feature only enterprise users see.

### 245: What is HAR replay in Playwright?

A HAR file is a recording of network traffic. Playwright can record one and later replay responses from it:

```ts
// record (run once)
await page.routeFromHAR("e2e/hars/products.har", {
  url: "**/api/**",
  update: true,
});

// replay
await page.routeFromHAR("e2e/hars/products.har", { url: "**/api/**" });
```

This gives you realistic responses without a running backend. The downside is that HAR files go stale when the API changes, so you need to re-record them from time to time.

### 246: How do you test APIs with Playwright?

Use the `request` fixture. It shares the `baseURL` and can share cookies with the browser:

```ts
test("creates a todo through the API", async ({ request }) => {
  const res = await request.post("/api/todos", { data: { title: "Buy milk" } });
  expect(res.ok()).toBeTruthy();

  const todo = await res.json();
  expect(todo).toMatchObject({ title: "Buy milk", done: false });
});
```

It's useful for testing your backend directly, and for preparing data before a UI test.

### 247: How do you prepare test data for an e2e test?

Create it through the API, not through the UI. It's much faster and less flaky:

```ts
test("user can rename a project", async ({ page, request }) => {
  const res = await request.post("/api/projects", {
    data: { name: `Project ${Date.now()}` },
  });
  const project = await res.json();

  await page.goto(`/projects/${project.id}`);
  await page.getByRole("button", { name: "Rename" }).click();
  await page.getByLabel("Name").fill("Renamed");
  await page.getByRole("button", { name: "Save" }).click();

  await expect(page.getByRole("heading", { name: "Renamed" })).toBeVisible();

  await request.delete(`/api/projects/${project.id}`);
});
```

Use unique names so parallel tests don't clash. Put the setup and cleanup in a fixture if many tests need it.

### 248: How do you handle browser dialogs and new tabs in Playwright?

**Dialogs** (`alert`, `confirm`, `prompt`) are dismissed automatically by default. To accept one, add a handler before triggering it:

```ts
page.once("dialog", (dialog) => dialog.accept());
await page.getByRole("button", { name: "Delete account" }).click();
```

**New tabs** opened by links with `target="_blank"`:

```ts
const popupPromise = page.waitForEvent("popup");
await page.getByRole("link", { name: "Open docs" }).click();
const popup = await popupPromise;
await expect(popup).toHaveURL(/docs/);
```

Start waiting for the event **before** the click, otherwise you can miss it.

### 249: How do you test file upload and download in Playwright?

Upload:

```ts
await page.getByLabel("Upload CSV").setInputFiles("e2e/fixtures/users.csv");

// or from memory
await page.getByLabel("Upload CSV").setInputFiles({
  name: "users.csv",
  mimeType: "text/csv",
  buffer: Buffer.from("name,email\nAnna,anna@test.com"),
});
```

Download:

```ts
const downloadPromise = page.waitForEvent("download");
await page.getByRole("button", { name: "Export" }).click();
const download = await downloadPromise;

expect(download.suggestedFilename()).toBe("report.csv");
await download.saveAs(test.info().outputPath("report.csv"));
```

### 250: How do you work with iframes in Playwright?

Use `frameLocator`, or `contentFrame()` on a locator for the iframe:

```ts
const payment = page.frameLocator("iframe[title='Secure payment input']");
await payment.getByLabel("Card number").fill("4242 4242 4242 4242");

// same thing
const frame = page
  .locator("iframe[title='Secure payment input']")
  .contentFrame();
await frame.getByLabel("Expiry").fill("12/30");
```

Locators inside the frame auto-wait like normal ones. This is common for payment forms and embedded widgets.

### 251: How do screenshot comparisons work in Playwright?

```ts
test("pricing page looks right", async ({ page }) => {
  await page.goto("/pricing");
  await expect(page).toHaveScreenshot("pricing.png", {
    fullPage: true,
    mask: [page.getByTestId("live-chat")],
    maxDiffPixelRatio: 0.01,
  });
});
```

The first run saves the baseline image and fails (because there was nothing to compare). Later runs compare against it. Update baselines with `npx playwright test --update-snapshots`.

Baselines are saved per browser and per OS, because fonts and rendering differ. That's why most teams generate and compare screenshots inside the same Docker image (the official Playwright image) in CI and locally.

### 252: What is the Playwright trace viewer?

A trace is a recording of a test run. It includes every action, a DOM snapshot before and after each action, screenshots, console logs, network requests and the source code line.

```ts
use: {
  trace: "on-first-retry";
}
```

Open it with `npx playwright show-trace trace.zip`, from the HTML report, or at trace.playwright.dev. It's the best tool for debugging tests that fail only in CI, because you can see exactly what the page looked like when the failure happened.

### 253: How should you handle flaky tests in Playwright?

- Turn on `retries` in CI so one random failure doesn't block everyone. Playwright marks tests that passed on retry as **flaky** in the report.
- Record traces on retry to see what went wrong.
- Fix the cause. It's usually a missing web-first assertion, a race with the network, shared test data or an animation.
- Use `failOnFlakyTests: true` in the config if you want flaky tests to fail the run, so they can't be ignored.
- If a fix takes time, mark the test with `test.fixme` and create a ticket, instead of letting it fail randomly for everyone.

Retries hide the problem. They don't solve it.

### 254: How does parallelism work in Playwright?

Playwright runs test files in parallel using worker processes. Each worker has its own browser. With `fullyParallel: true`, even tests inside one file run in parallel.

```ts
export default defineConfig({
  fullyParallel: true,
  workers: process.env.CI ? 4 : undefined, // undefined = half of CPU cores
});
```

If tests in a file must run in order (for example, they depend on each other), use:

```ts
test.describe.configure({ mode: "serial" });
```

Serial tests are usually a sign of tests that depend on each other, so try to avoid them.

### 255: How do you tag tests and run only some of them?

```ts
test("guest checkout", { tag: ["@smoke", "@checkout"] }, async ({ page }) => {
  // ...
});

test.describe("admin", { tag: "@admin" }, () => {
  // ...
});
```

```bash
npx playwright test --grep @smoke
npx playwright test --grep-invert @slow
npx playwright test --grep "@smoke|@checkout"
```

A common setup is to run `@smoke` tests on every pull request and the full suite nightly or before a release.

### 256: What is test.step in Playwright?

It groups actions into named steps that show up in the report and trace:

```ts
test("checkout", async ({ page }) => {
  await test.step("add item to cart", async () => {
    await page.goto("/products/1");
    await page.getByRole("button", { name: "Add to cart" }).click();
  });

  await test.step("pay", async () => {
    await page.goto("/checkout");
    await page.getByRole("button", { name: "Pay" }).click();
  });
});
```

When a long test fails, you see right away which step failed. Page object methods can use `test.step` too.

### 257: What annotations does Playwright support?

- `test.skip()`: don't run the test (can be conditional)
- `test.fixme()`: skip it and mark it as something to fix
- `test.fail()`: the test is expected to fail. If it passes, Playwright reports that.
- `test.slow()`: triple the timeout
- `test.only()`: run only this test

```ts
test("upload large file", async ({ page, browserName }) => {
  test.skip(browserName === "firefox", "Known bug in Firefox, see #1234");
  test.slow();
  // ...
});
```

You can also add custom annotations with `test.info().annotations.push({ type: "issue", description: "..." })`.

### 258: How do you emulate different devices, locales and settings in Playwright?

Through the `use` options, globally, per project or per test file:

```ts
test.use({
  viewport: { width: 390, height: 844 },
  locale: "de-DE",
  timezoneId: "Europe/Berlin",
  colorScheme: "dark",
  geolocation: { latitude: 52.52, longitude: 13.405 },
  permissions: ["geolocation"],
});

test("shows prices in euro", async ({ page }) => {
  await page.goto("/pricing");
  await expect(page.getByText("9,99 €")).toBeVisible();
});
```

You can also use presets from `devices`, like `devices["Pixel 7"]`.

### 259: What timeouts does Playwright have?

- **Test timeout**: 30 seconds by default for the whole test, including fixtures (`timeout` in config, `test.setTimeout()` in a test).
- **Expect timeout**: 5 seconds by default for web-first assertions (`expect: { timeout }`).
- **Action and navigation timeouts**: no limit by default (they're bounded by the test timeout). You can set `actionTimeout` and `navigationTimeout` in `use`.
- **Global timeout**: a limit for the whole run (`globalTimeout`), useful in CI.

If tests time out often, increasing the timeout is rarely the right fix. Find out what's slow first.

### 260: How do you run Playwright tests in GitHub Actions?

```yaml
name: e2e
on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 14
```

`--with-deps` installs the system libraries the browsers need. Uploading the report lets you open the HTML report and traces for failed tests. `npm init playwright` can generate this workflow for you.

### 261: What reporters does Playwright have?

- `list`, `line`, `dot`: terminal output
- `html`: an interactive report with traces and screenshots
- `junit`: XML for CI systems that read JUnit results
- `json`: raw results
- `github`: adds annotations for failures in GitHub pull requests
- `blob`: used with sharding. Each shard writes a blob, and you merge them into one report with `npx playwright merge-reports`.

You can use several at once: `reporter: [["html"], ["junit", { outputFile: "results.xml" }]]`.

### 262: How does the Cypress command chain work?

Cypress commands don't run right away and don't return promises. Each `cy.*` call adds a command to a queue. Cypress runs the queue after your test function finishes:

```ts
cy.get("[data-cy=email]").type("anna@test.com");
cy.get("[data-cy=submit]").click();
```

That's why this doesn't work:

```ts
const text = cy.get("h1").invoke("text"); // not a string, it's a chainable
```

You get values with `.then()` or aliases:

```ts
cy.get("h1")
  .invoke("text")
  .then((text) => {
    expect(text).to.contain("Welcome");
  });
```

You also can't use `async`/`await` with Cypress commands.

### 263: How do you mock network requests in Cypress?

Use `cy.intercept`:

```ts
it("shows the orders", () => {
  cy.intercept("GET", "/api/orders", { fixture: "orders.json" }).as(
    "getOrders",
  );

  cy.visit("/orders");
  cy.wait("@getOrders");
  cy.findAllByRole("row").should("have.length", 4);
});

it("shows an error", () => {
  cy.intercept("GET", "/api/orders", {
    statusCode: 500,
    body: { message: "fail" },
  });
  cy.visit("/orders");
  cy.findByRole("alert").should("be.visible");
});
```

`cy.intercept` can also just watch requests without changing them, or change the real response with `req.continue((res) => { ... })`.

### 264: What are fixtures in Cypress?

Fixtures are static data files, usually JSON, in the `cypress/fixtures` folder:

```ts
cy.intercept("GET", "/api/user", { fixture: "user.json" });

cy.fixture("user.json").then((user) => {
  cy.get("[data-cy=name]").should("have.text", user.name);
});
```

They keep test data out of the test code. Be careful that fixture files don't drift away from what the real API returns. Some teams generate them from the API schema.

### 265: How do you create custom commands in Cypress?

```ts
// cypress/support/commands.ts
Cypress.Commands.add("login", (email: string, password: string) => {
  cy.request("POST", "/api/login", { email, password });
});

declare global {
  namespace Cypress {
    interface Chainable {
      login(email: string, password: string): Chainable<void>;
    }
  }
}
```

```ts
beforeEach(() => {
  cy.login("anna@test.com", "secret123");
  cy.visit("/dashboard");
});
```

Custom commands are good for actions you repeat a lot, like logging in or seeding data. Don't put whole test flows in them, or tests become hard to follow.

### 266: What is cy.session?

`cy.session` caches the browser session (cookies, localStorage, sessionStorage) so you log in once and reuse it in other tests:

```ts
Cypress.Commands.add("login", (email: string, password: string) => {
  cy.session(
    [email],
    () => {
      cy.visit("/login");
      cy.findByLabelText("Email").type(email);
      cy.findByLabelText("Password").type(password, { log: false });
      cy.findByRole("button", { name: "Log in" }).click();
      cy.url().should("include", "/dashboard");
    },
    {
      validate() {
        cy.request("/api/me").its("status").should("eq", 200);
      },
    },
  );
});
```

The first call runs the setup function. Later calls with the same ID restore the saved session. `validate` checks that the session is still valid, and redoes the login if not.

### 267: How does retry-ability work in Cypress?

Queries like `cy.get`, `cy.find` and `cy.contains` and the assertions after them are retried until the assertion passes or the timeout (4 seconds by default) runs out:

```ts
cy.get("[data-cy=status]").should("have.text", "Done");
```

Actions like `.click()` and `.type()` are **not** retried. They wait for the element to be actionable once and then run. That's why it's important to put an assertion before an action when the page is still changing. You can change the timeout per command with `{ timeout: 10000 }` or globally with `defaultCommandTimeout`.

### 268: How do you control time in Cypress?

Use `cy.clock` and `cy.tick`:

```ts
it("logs the user out after 15 minutes of inactivity", () => {
  cy.clock();
  cy.visit("/dashboard");

  cy.tick(15 * 60 * 1000);

  cy.contains("You have been logged out").should("be.visible");
});
```

`cy.clock()` replaces `setTimeout`, `setInterval` and `Date` in the app. You can also pass a fixed date: `cy.clock(new Date(2026, 0, 1))`.

### 269: What are aliases in Cypress and how do you wait on a request?

`.as()` gives a name to an element, an intercepted request or a value:

```ts
cy.intercept("POST", "/api/comments").as("createComment");

cy.findByRole("textbox").type("Nice post!");
cy.findByRole("button", { name: "Comment" }).click();

cy.wait("@createComment")
  .its("request.body")
  .should("deep.equal", { text: "Nice post!" });
cy.wait("@createComment").its("response.statusCode").should("eq", 201);
```

Waiting on a request alias makes the test wait exactly as long as the request takes, and lets you check the request and response.

### 270: Why shouldn't you use cy.wait with a number?

`cy.wait(3000)` always waits 3 seconds. If the app is faster, you waste time. If it's slower (like on a busy CI machine), the test fails anyway. Multiply that by hundreds of tests and the suite gets slow and flaky.

Instead, wait for something specific: an element with an assertion (`should("be.visible")`) or a request (`cy.wait("@alias")`). The same rule applies to `page.waitForTimeout()` in Playwright.

### 271: What selectors should you use in e2e tests?

In order of preference:

1. **Role and accessible name**: `getByRole("button", { name: "Save" })`. Stable and tests accessibility too.
2. **Label or text**: `getByLabel("Email")`, `getByText("Welcome back")`.
3. **Test IDs**: `data-testid` or `data-cy`, for elements with no good role or text.

Avoid CSS classes (they change when styles change, especially with Tailwind or CSS modules), long CSS paths and XPath. If your app has several languages, text selectors can be a problem. Then test in one fixed language, or use test IDs for the elements whose text changes.

### 272: What should end-to-end tests cover?

Focus on the flows that would hurt most if they broke:

- sign up, log in, log out, password reset
- the main thing users come for (search, checkout, booking, creating a post)
- payments and anything involving money
- flows that cross several pages or services

Don't try to cover every validation message or edge case in e2e. That's what unit and integration tests are for. A small, stable e2e suite is much more useful than a large, flaky one.

### 273: Which environment should e2e tests run against?

Common options:

- **Local build in CI**: start the app (and maybe the backend with Docker Compose) inside the CI job. Fully controlled and repeatable.
- **Preview deployments**: run against the preview URL that Vercel, Netlify or a similar platform creates for each pull request.
- **Staging**: closest to production, but shared, so tests can clash with each other and with manual testers.
- **Production**: only a few safe smoke tests, usually with special test accounts.

For pull requests, a local build or a preview deploy is usually best, because each run has its own environment.

### 274: How do you manage test data in e2e tests?

- Create the data each test needs at the start (through the API or directly in the database) instead of depending on data that "is already there".
- Use unique values (`user-${Date.now()}@test.com` or a random ID), so tests running in parallel don't clash.
- Clean up after the test, or reset the database before the run.
- Keep a small set of stable seed data for things every test needs, like the test user account.

Tests that depend on data created by other tests fail as soon as the order changes or one test fails.

### 275: How do you test flows that send emails?

Don't use real inboxes. Options:

- Use an email testing service or a local SMTP catcher like Mailpit or MailHog. The app sends the email there, and the test reads it through an API.
- Use a test-only API endpoint that returns the latest email or token for a user.
- For unit tests, mock the email service and check it was called with the right data.

```ts
await page.getByRole("button", { name: "Send reset link" }).click();

const email = await getLatestEmail("anna@test.com"); // your helper, calling Mailpit's API
const link = email.html.match(/href="([^"]+reset[^"]+)"/)![1];
await page.goto(link);
```

### 276: How do you test payment flows?

- Use the provider's **test mode** with test cards. For Stripe, for example, `4242 4242 4242 4242` succeeds, and there are other numbers for declines and 3D Secure.
- In e2e tests, the payment form is often inside an iframe, so use `frameLocator`.
- Test webhooks separately. Most providers have a CLI or dashboard to send test webhook events.
- In unit and integration tests, mock the payment SDK and test how your UI handles success, decline and errors.

Never run automated tests against live payment keys.

### 277: What is contract testing?

Contract testing checks that the frontend and backend agree on the API format, without running them together.

With consumer-driven contracts (for example, Pact), the frontend tests record what requests they make and what responses they expect. This becomes a contract file. The backend then runs a verification against that contract in its own CI. If the backend changes a field the frontend uses, the backend build fails before deploy.

It's useful when frontend and backend are developed by different teams and deployed separately. A lighter option is to generate types and mocks from an OpenAPI schema, so a schema change breaks the frontend type check.

### 278: How do you test responsive layouts?

In jsdom you can't, because there's no layout. In a real browser:

```ts
test.describe("mobile", () => {
  test.use({ viewport: { width: 375, height: 667 } });

  test("shows the burger menu", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("button", { name: "Open menu" })).toBeVisible();
    await expect(
      page.getByRole("navigation").getByRole("link", { name: "Pricing" }),
    ).toBeHidden();
  });
});
```

Visual regression screenshots at a few widths (mobile, tablet, desktop) also catch layout problems that are hard to assert on.

### 279: How do you test features behind feature flags?

In unit and integration tests, control the flag directly. Wrap the flag provider in your custom render, or mock the hook:

```tsx
render(<Checkout />, { flags: { newCheckout: true } }); // your custom render option
```

Test both the on and off states while both exist. In e2e tests, set flags through the flag service's API, a URL parameter or a cookie that your app reads in test environments. When a flag is removed, delete the tests for the old path too.

### 280: How do you test that analytics events are sent?

In unit tests, mock your analytics wrapper and check the calls:

```tsx
vi.mock("@/lib/analytics", () => ({ track: vi.fn() }));

test("tracks the signup click", async () => {
  const user = userEvent.setup();
  render(<Pricing />);

  await user.click(screen.getByRole("button", { name: "Start free trial" }));
  expect(track).toHaveBeenCalledWith("trial_started", { plan: "pro" });
});
```

This is easier if your code calls your own `track()` function instead of the vendor SDK directly. In e2e tests you can catch the requests to the analytics endpoint with `page.route` or `page.waitForRequest` and check the payload. Block them in other tests, so test runs don't pollute your real analytics data.

### 281: How do you test components that use WebSockets?

- **MSW** supports WebSockets with `ws.link()`:

```ts
import { ws } from "msw";

const chat = ws.link("wss://api.example.com/chat");

server.use(
  chat.addEventListener("connection", ({ client }) => {
    client.send(JSON.stringify({ type: "message", text: "Hello from server" }));
  }),
);
```

- **Playwright** can mock or watch WebSockets with `page.routeWebSocket()`, or listen to real ones with `page.on("websocket")`.
- For unit tests, you can also inject a fake socket object into your component or hook.

Test the important cases: a message arrives and shows up, the connection drops and reconnects, and the socket closes on unmount.

### 282: How do you deal with animations in tests?

Animations cause flaky tests and changing screenshots. Options:

- Make the app respect `prefers-reduced-motion`, then emulate it in tests: `test.use({ reducedMotion: "reduce" })` in Playwright.
- Disable animations in screenshot tests: `toHaveScreenshot({ animations: "disabled" })`.
- In jsdom, CSS animations don't run anyway. For JS animation libraries, some have a global switch to turn animations off (for example, `MotionGlobalConfig.skipAnimations = true` in Motion).
- Wait for the end state with web-first assertions, not with fixed timeouts.

### 283: How do you stop third-party scripts from affecting e2e tests?

Block them with routing:

```ts
test.beforeEach(async ({ context }) => {
  await context.route(
    /(google-analytics|hotjar|intercom|doubleclick)/,
    (route) => route.abort(),
  );
});
```

Third-party scripts make tests slower, can be flaky, send fake data to real dashboards, and can show popups (chat widgets, cookie banners) that cover your buttons. For cookie consent banners, set the consent cookie before the test, so the banner doesn't show.

### 284: Should you run tests in a pre-commit hook?

Only fast ones. A common setup with Husky and lint-staged:

```json
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "vitest related --run"]
  }
}
```

`vitest related` runs only the tests that import the changed files. Running the full suite or e2e tests on every commit is too slow, and people start skipping the hook with `--no-verify`. Leave the full suite to CI.

### 285: How should you name tests?

Describe the behavior and the condition, so a failing test explains itself:

- Bad: `"test 1"`, `"works"`, `"handleClick"`
- Good: `"shows an error when the email is invalid"`
- Good: `"disables the submit button while saving"`

Using `describe` for the context helps:

```ts
describe("when the cart is empty", () => {
  test("shows the empty message", () => {});
  test("hides the checkout button", () => {});
});
```

When a test fails in CI, its name is often the first thing you see.

### 286: What do you look for when reviewing tests in a pull request?

- Do the tests check **behavior**, or implementation details?
- Is the new code tested at the **right level** (unit, integration or e2e)?
- Are the **edge cases** covered: empty state, error state, loading, permissions?
- Would the test **fail if the feature broke**? Sometimes it's worth breaking the code locally to check.
- Is it **readable**: clear names, no huge setup, no copy-paste?
- Any signs of **flakiness**: fixed waits, real dates, shared state, missing `await`?
- Are new **snapshots** small and meaningful?
- Too much **mocking**?

### 287: How do you fix a bug in a test-driven way?

1. Write a test that reproduces the bug. It should fail.
2. Fix the code.
3. Watch the test pass.
4. Keep the test, so the bug can't come back.

Writing the test first proves you understood the bug, and that the fix actually fixes it. If you write the test after, it's easy to end up with a test that would have passed even before the fix.

### 288: How do you catch JavaScript errors in the page during e2e tests?

Listen for page errors and console errors, and fail the test if any appear:

```ts
// fixtures.ts
export const test = base.extend<{ failOnErrors: void }>({
  failOnErrors: [
    async ({ page }, use) => {
      const errors: string[] = [];
      page.on("pageerror", (err) => errors.push(err.message));
      page.on("console", (msg) => {
        if (msg.type() === "error") errors.push(msg.text());
      });

      await use();

      expect(errors, "Page had JavaScript errors").toEqual([]);
    },
    { auto: true },
  ],
});
```

`auto: true` makes the fixture run for every test without asking for it. This catches errors that don't break the visible UI right away but are still bugs.

### 289: What is Vitest Browser Mode?

Browser Mode runs your Vitest tests in a real browser (Chromium, Firefox or WebKit through Playwright, or through WebdriverIO) instead of jsdom. It became stable in Vitest 4.

```bash
npm i -D @vitest/browser-playwright vitest-browser-react
```

```ts
// vitest.config.ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import { playwright } from "@vitest/browser-playwright";

export default defineConfig({
  plugins: [react()],
  test: {
    browser: {
      enabled: true,
      provider: playwright(),
      instances: [{ browser: "chromium" }],
    },
  },
});
```

You get real CSS, layout, events and browser APIs, so you don't need mocks for things like `ResizeObserver`. It's slower to start than jsdom, but tests are closer to reality.

### 290: How do you write a component test with vitest-browser-react?

```tsx
import { expect, test } from "vitest";
import { render } from "vitest-browser-react";
import { Counter } from "./Counter";

test("increments the count", async () => {
  const screen = await render(<Counter />);

  await screen.getByRole("button", { name: "Increment" }).click();

  await expect.element(screen.getByText("Count: 1")).toBeInTheDocument();
});
```

It looks a lot like React Testing Library, but the queries return **locators** (like in Playwright), interactions go through the real browser, and `expect.element` retries until the assertion passes. You can also import `page` and `userEvent` from `vitest/browser`.

### 291: What is component testing in Playwright?

Playwright has an experimental package, `@playwright/experimental-ct-react`, that mounts a single React component in a real browser and tests it with the normal Playwright API:

```tsx
import { test, expect } from "@playwright/experimental-ct-react";
import { Button } from "./Button";

test("calls onClick", async ({ mount }) => {
  let clicked = false;
  const component = await mount(
    <Button onClick={() => (clicked = true)}>Save</Button>,
  );

  await component.click();
  expect(clicked).toBe(true);
});
```

It has some limits: the test runs in Node and the component in the browser, so you can't pass complex objects or class instances as props easily. It's still marked experimental. For component tests in a real browser, many teams now use Vitest Browser Mode or Storybook with the Vitest addon instead.

### 292: When would you choose jsdom and when a real browser for component tests?

**jsdom (or happy-dom)**:

- very fast startup, good for thousands of tests
- fine for logic, state, forms, rendering and most interactions
- needs mocks for missing APIs and can't test layout or CSS

**Real browser (Vitest Browser Mode, Storybook, Playwright CT)**:

- real events, focus, CSS, layout, scrolling, `IntersectionObserver`, canvas
- slower, needs browsers installed in CI

A practical mix: most component tests in jsdom, and a real browser for components that depend on layout or browser behavior (design system components, virtualized lists, drag and drop, rich editors).

### 293: How do you mock GraphQL requests with MSW?

Use the `graphql` namespace and match by operation name:

```ts
import { graphql, HttpResponse } from "msw";

export const handlers = [
  graphql.query("GetUser", ({ variables }) => {
    return HttpResponse.json({
      data: { user: { id: variables.id, name: "Anna" } },
    });
  }),

  graphql.mutation("UpdateUser", () => {
    return HttpResponse.json({
      errors: [{ message: "Not allowed" }],
    });
  }),
];
```

This works with any GraphQL client (Apollo, urql, graphql-request), because MSW intercepts the HTTP request. You can use `graphql.link("https://api.example.com/graphql")` if your app talks to several GraphQL endpoints.

### 294: How do you test reducers and selectors?

They're pure functions, so test them directly, without rendering anything:

```ts
import { cartReducer, addItem, removeItem, selectCartTotal } from "./cartSlice";

test("adds an item", () => {
  const state = cartReducer(
    { items: [] },
    addItem({ id: 1, price: 10, qty: 1 }),
  );
  expect(state.items).toEqual([{ id: 1, price: 10, qty: 1 }]);
});

test("calculates the total", () => {
  const state = {
    cart: {
      items: [
        { id: 1, price: 10, qty: 2 },
        { id: 2, price: 5, qty: 1 },
      ],
    },
  };
  expect(selectCartTotal(state)).toBe(25);
});
```

These tests are fast and good for complex logic. But the Redux docs suggest focusing more on integration tests through components, and testing reducers directly only when their logic is complicated.

### 295: How do you test copying to the clipboard?

`user-event` replaces the clipboard with a fake one when you call `userEvent.setup()`, so you can read what was copied:

```tsx
test("copies the invite link", async () => {
  const user = userEvent.setup();
  render(<InviteLink url="https://app.test/invite/abc" />);

  await user.click(screen.getByRole("button", { name: "Copy link" }));

  expect(await navigator.clipboard.readText()).toBe(
    "https://app.test/invite/abc",
  );
  expect(screen.getByText("Copied!")).toBeInTheDocument();
});
```

In Playwright, grant permissions first: `context.grantPermissions(["clipboard-read", "clipboard-write"])`. Clipboard permissions work differently in each browser, so these tests are often limited to Chromium.

### 296: How do you check an element's accessible name and description?

jest-dom has matchers for that:

```tsx
expect(screen.getByRole("button", { name: /close/i })).toHaveAccessibleName(
  "Close dialog",
);
expect(screen.getByLabelText("Password")).toHaveAccessibleDescription(
  "At least 8 characters",
);
expect(screen.getByLabelText("Email")).toHaveAccessibleErrorMessage(
  "Email is required",
);
```

They're useful for icon buttons, inputs with help text (`aria-describedby`) and error messages (`aria-errormessage`), where what a screen reader announces matters.

### 297: How do you test a protected route?

Test both cases: not logged in (redirects) and logged in (shows the page):

```tsx
function renderAt(path: string, user: User | null) {
  render(
    <AuthContext.Provider value={{ user }}>
      <MemoryRouter initialEntries={[path]}>
        <Routes>
          <Route path="/login" element={<h1>Login page</h1>} />
          <Route element={<RequireAuth />}>
            <Route path="/account" element={<h1>Account page</h1>} />
          </Route>
        </Routes>
      </MemoryRouter>
    </AuthContext.Provider>,
  );
}

test("redirects guests to login", () => {
  renderAt("/account", null);
  expect(
    screen.getByRole("heading", { name: "Login page" }),
  ).toBeInTheDocument();
});

test("shows the page to logged-in users", () => {
  renderAt("/account", { id: 1, name: "Anna" });
  expect(
    screen.getByRole("heading", { name: "Account page" }),
  ).toBeInTheDocument();
});
```

Remember that client-side route guards are only for user experience. The real protection must be on the server, which you test in backend tests or e2e.

### 298: How do you test a component that reads and updates URL search params?

Start the router at a URL with params, interact, and check the UI. To check the URL itself, render a small component that prints the location:

```tsx
function LocationDisplay() {
  const location = useLocation();
  return (
    <div data-testid="location">{location.pathname + location.search}</div>
  );
}

test("updates the page param", async () => {
  const user = userEvent.setup();
  render(
    <MemoryRouter initialEntries={["/products?page=1"]}>
      <ProductList />
      <LocationDisplay />
    </MemoryRouter>,
  );

  await user.click(screen.getByRole("button", { name: "Next page" }));
  expect(screen.getByTestId("location")).toHaveTextContent("/products?page=2");
});
```

### 299: How do you keep MSW handlers organized in a big app?

- Split handlers by domain: `mocks/handlers/users.ts`, `mocks/handlers/orders.ts`, then combine them in one array.
- Keep only the **happy path** in default handlers. Put error and edge cases in the tests with `server.use()`.
- Use factories for response data, so handlers and tests share the same shapes.
- Type the responses with your API types (MSW handlers accept generics for request body and response body), so a type change shows up in the mocks.
- If you have an OpenAPI spec, consider generating handlers from it.
- Reuse the same handlers in Storybook and local development with `setupWorker`.

### 300: What is the difference between using MSW and page.route for mocking in e2e tests?

`page.route` is built into Playwright. It works per test, needs no changes in the app, and catches requests made by the browser.

MSW in the browser needs the app to start the Service Worker (usually only in a special test or dev mode). It's useful when you already have MSW handlers for unit tests and Storybook and want to reuse them, so the mock data is the same everywhere.

For true e2e tests you usually don't mock the API at all. When you do, `page.route` is simpler. Mocked "e2e" runs are closer to front-end-only integration tests in a real browser.

## Advanced Questions (301-450)

### 301: What does React Testing Library's render actually do under the hood?

Roughly:

1. Creates a `div` (the container) and appends it to `document.body` (the `baseElement`), unless you pass your own.
2. Creates a React root with `createRoot(container)`, or uses `hydrateRoot` if you pass `hydrate: true`.
3. Wraps your UI in the `wrapper` component if you gave one.
4. Calls `root.render(ui)` inside `act()`, so React finishes rendering and runs effects before `render` returns.
5. Saves the root and container in a list, so `cleanup()` can unmount and remove them later.
6. Returns queries bound to `baseElement`, plus `rerender`, `unmount`, `debug` and `asFragment`.

Because of step 4, state set in a `useEffect` on mount is already visible right after `render`. But anything that waits for a promise (like a fetch) isn't, and that's why you need `findBy`.

### 302: How does act work in React 19, and what is IS_REACT_ACT_ENVIRONMENT?

`act` creates a scope where React queues all updates and effects instead of scheduling them for later. When the scope ends, React runs everything in the queue right away. The async version (`await act(async () => ...)`) also waits for promises inside it and keeps flushing until there's nothing left.

React only shows the "not wrapped in act" warning when the global `IS_REACT_ACT_ENVIRONMENT` is `true`. RTL sets it to `true` when it loads, and turns it off temporarily inside its async utilities like `waitFor`, because there the waiting itself handles the updates.

In React 19, `act` is exported from `react`. The old `ReactDOMTestUtils.act` is deprecated. If you write your own test helpers without RTL, you need to set `globalThis.IS_REACT_ACT_ENVIRONMENT = true` yourself.

### 303: How do waitFor and findBy work internally?

`waitFor(callback)`:

1. Runs the callback right away. If it doesn't throw, it resolves.
2. Otherwise it checks again on an interval (50 ms by default) **and** whenever a `MutationObserver` on the container sees a DOM change.
3. If the timeout (1000 ms by default) passes, it rejects with the last error, and for query errors it adds the current DOM to the message.

RTL runs all of this inside its async wrapper, which turns off the act environment while waiting and flushes React work at the end.

`findBy*` is just `waitFor(() => getBy*(...))`. You can change the defaults with `configure({ asyncUtilTimeout: 2000 })` or per call: `findByText("x", {}, { timeout: 3000 })`.

### 304: How does user-event simulate interactions?

`user-event` doesn't just dispatch one event. For `user.click(el)` it runs a pointer sequence: `pointerover`, `pointerenter`, `mouseover`, `pointermove`, `pointerdown`, `mousedown`, focus change, `pointerup`, `mouseup`, `click`. For `user.type`, each character goes through `keydown`, `keypress`, `beforeinput`, then the value is changed through the element's native value setter, then `input` and `keyup`.

Changing the value through the native setter matters for React. React tracks input values internally, and setting `input.value = "x"` directly would make React miss the change.

It also does checks a real browser does. For example, it won't click an element that has `pointer-events: none` (computed from styles available in jsdom) and throws an error instead. You can turn that off with `pointerEventsCheck: PointerEventsCheckLevel.Never` when a library sets that style in a way jsdom can't calculate correctly.

### 305: What browser features are missing or different in jsdom?

- **Layout and rendering**: sizes and positions are 0, no scrolling, no CSS media queries, no `:hover`.
- **Observers**: `IntersectionObserver`, `ResizeObserver` don't exist. `MutationObserver` does.
- **`window.matchMedia`**: missing.
- **Navigation**: changing `location.href` to another page doesn't work.
- **Canvas and WebGL**: missing (unless you install the `canvas` package, which only covers 2D).
- **Media**: `HTMLMediaElement.play()` and `pause()` aren't implemented.
- **Some newer APIs**: things like `<dialog>` `showModal()`, the Popover API or `scrollIntoView` may be missing or incomplete, depending on the jsdom version.
- **Pointer capture, drag and drop**: limited.

When a test needs many of these, that's a sign it belongs in a real browser.

### 306: Why can a test pass in jsdom but the feature still be broken in the browser?

Because jsdom only checks the DOM structure and JavaScript logic. A test can pass while:

- the button is covered by another element, so a real user can't click it
- CSS hides the element or puts it off screen
- the layout breaks on small screens
- a browser API behaves differently from your mock
- the code uses a feature that isn't supported in Safari
- the real API returns a different shape than your MSW mock

It also works the other way. A test can fail in jsdom because of a missing API, while the real app is fine. That's why you combine jsdom tests with some real-browser and e2e tests.

### 307: How does module mocking work in Vitest?

Vitest uses a Vite plugin that transforms your test file:

1. It finds `vi.mock()` calls (and `vi.hoisted()`) and moves them to the top of the file.
2. It rewrites static imports into dynamic imports that run **after** the mocks are registered.

When a module is imported, Vitest's module runner checks whether that path is mocked. If it is, it returns the factory's result (or an automock, or a file from `__mocks__`) instead of the real module.

Each test file has its own module graph, so mocks in one file don't affect others. Inside a file, `vi.mock` applies to the whole file. For a different mock per test, use `vi.doMock` (not hoisted) together with `vi.resetModules()` and a dynamic `import()`.

### 308: How does Jest's module registry work, and what are resetModules and isolateModules?

Jest has its own module system (not Node's). Each test file gets a fresh registry, and inside a file, a module is loaded once and cached.

- `jest.resetModules()` clears the cache, so the next `require` loads a fresh copy. Useful when a module reads environment variables or keeps state when it loads.
- `jest.isolateModules(fn)` gives the function its own registry, so modules loaded inside it don't share state with the rest of the file.

```ts
test("reads the API url from env", () => {
  process.env.API_URL = "https://staging.example.com";
  jest.isolateModules(() => {
    const { config } = require("./config");
    expect(config.apiUrl).toBe("https://staging.example.com");
  });
});
```

Vitest has `vi.resetModules()` for the same purpose.

### 309: How do you mock ES modules in Jest?

When Jest runs real ES modules (with `--experimental-vm-modules`), `jest.mock` hoisting doesn't work, because static imports are resolved before any code runs. You need `jest.unstable_mockModule` and dynamic imports:

```ts
import { jest } from "@jest/globals";

jest.unstable_mockModule("./api.js", () => ({
  getUser: jest.fn(async () => ({ name: "Anna" })),
}));

const { getUser } = await import("./api.js");
const { loadProfile } = await import("./profile.js");

test("loads the profile", async () => {
  expect(await loadProfile()).toEqual({ name: "Anna" });
});
```

As the name says, it's still unstable. Most Jest projects avoid this by compiling ESM to CommonJS with Babel or SWC. This pain is one of the main reasons teams move to Vitest.

### 310: What are the different pools in Vitest?

The pool decides how Vitest runs test files in parallel:

- **`forks`** (the default): each worker is a child process. The most compatible option, works with native modules and code that uses `process` APIs.
- **`threads`**: worker threads. Can be faster, but some libraries don't work in worker threads.
- **`vmThreads`** / **`vmForks`**: run each file in a separate VM context inside a reused worker. Faster startup, but more risk of memory leaks and some differences in how globals behave.

There's also `isolate: true` (the default), which gives each test file a fresh environment. Turning it off with `isolate: false` can make the suite much faster, but then state can leak between files, so only do it if your tests clean up properly.

### 311: What are the typical ways state leaks between tests?

- **Module-level state**: singletons, stores (Zustand, Redux store created at module level), caches, React Query clients created once.
- **The DOM**: components not unmounted, portals or elements added to `body` manually.
- **Mocks**: implementations or call counts not reset, spies not restored.
- **Globals**: `vi.stubGlobal`, changed `window` properties, polyfills patched by one test.
- **Storage**: `localStorage`, `sessionStorage`, cookies, IndexedDB.
- **Timers**: fake timers not turned off, intervals still running.
- **MSW**: handlers added with `server.use()` not reset.

The fix is resetting all of these in `afterEach` (or with config options like `restoreMocks`, `unstubGlobals`, `unstubEnvs`) and avoiding module-level state that can't be reset.

### 312: How do fake timers work?

Vitest and Jest use `@sinonjs/fake-timers`. It replaces the global timer functions (`setTimeout`, `setInterval`, `setImmediate`, `Date`, `performance.now`, `requestAnimationFrame` and so on) with fake versions that keep a list of scheduled callbacks and a fake clock. Time only moves when you call `advanceTimersByTime`, `runAllTimers` or `runOnlyPendingTimers`.

Things to know:

- Promises are not timers. If a timer callback starts a promise, you need the async versions (`advanceTimersByTimeAsync`, `runAllTimersAsync`) so promise callbacks run in between.
- You can choose what to fake with `toFake`. For example, faking `queueMicrotask` or `nextTick` can break libraries that depend on them.
- `runAllTimers` with an interval that keeps creating timers loops until a safety limit and then throws.
- `shouldAdvanceTime: true` makes the fake clock move with real time, which helps with code that waits on its own.

### 313: Why can waitFor or findBy hang when fake timers are on, and how do you fix it?

`waitFor` uses `setTimeout` for its overall timeout and `setInterval` to retry. With fake timers, those never fire unless someone advances time.

RTL handles this for **Jest**: it checks for the global `jest` object and fake timers, and if both are there it advances them while it waits. In **Vitest** there's no `jest` global, so RTL doesn't advance the timers. `waitFor` then only rechecks when the DOM changes, and if the condition depends on a timer, it can hang until the test timeout.

Fixes:

- Advance timers yourself before the assertion: `await act(() => vi.advanceTimersByTimeAsync(1000))`, then use `getBy`.
- Use `vi.useFakeTimers({ shouldAdvanceTime: true })`, so time moves on its own.
- Only fake the timers you need, and use real timers in tests that rely heavily on `findBy`.

### 314: How do you track down a flaky unit test?

1. **Reproduce it**: run the test many times (`vitest --repeat 50` or a loop), alone and together with the rest of the file.
2. **Check order dependence**: run with random order (`sequence.shuffle: true` in Vitest, `--randomize` in Jest) to see if it depends on other tests.
3. **Look for async issues**: missing `await`, a fetch finishing after the test, `findBy` with too short a timeout on a slow CI machine, act warnings in the output.
4. **Look for shared state**: stores, mocks, storage, MSW handlers not reset.
5. **Look for time and randomness**: `new Date()`, `Math.random()`, `crypto.randomUUID()`, time zones.
6. **Compare environments**: CI might use another Node version, time zone, locale or fewer CPU cores, which makes timing worse.

Fix the cause. Raising timeouts or adding retries just hides the problem.

### 315: How do you track down a flaky e2e test?

- **Open the trace** for the failed run and look at the DOM snapshot at the moment it failed. Was the element there? Covered by something? Was a request still pending?
- **Look for non-retrying checks**: `expect(await locator.textContent())` instead of `await expect(locator).toHaveText()`, or `isVisible()` used as an assertion.
- **Look for fixed waits** and missing waits for network responses.
- **Check test data**: two tests using the same user or record in parallel, or data left from a previous run.
- **Check the environment**: a slow backend in CI, cold starts, rate limits, third-party scripts, animations.
- **Run it many times** locally: `npx playwright test --repeat-each=20 --workers=4`.

Then mark it with `test.fixme` and a ticket if you can't fix it right away, instead of leaving it to fail at random.

### 316: What problems do floating promises cause in tests?

A floating promise is a promise nobody awaits. In tests that means:

- The test finishes before the work does, so the assertion runs too early, or an error happens after the test is reported as passed.
- The leftover work runs during the **next** test and breaks it, so the error shows up in the wrong place.
- You get act warnings that point at the wrong test.

```ts
// Bug: missing await, the test passes even when the text never shows up
test("shows the result", () => {
  render(<Search />);
  user.type(screen.getByRole("searchbox"), "abc");
  screen.findByText("3 results");
});
```

The `@typescript-eslint/no-floating-promises` rule and the `await-async-queries` / `await-async-events` rules in `eslint-plugin-testing-library` catch these.

### 317: How do you find memory leaks or open handles in a test suite?

Symptoms: the suite gets slower over time, workers crash with "heap out of memory", or Jest says "Jest did not exit one second after the test run has completed."

Tools:

- `jest --logHeapUsage` shows memory after each file. If it keeps growing, something leaks.
- `jest --detectOpenHandles` shows timers, sockets or servers left open.
- Vitest has `--logHeapUsage` too. A run that never exits is often an open handle, like a server or timer.
- Use `node --inspect` and take heap snapshots in Chrome DevTools to see what's growing.

Common causes: MSW server or database connections not closed, intervals not cleared, global event listeners not removed, big module-level caches, and, in Jest, some libraries that keep references between test files.

### 318: How do you speed up a slow Jest suite?

- Use a faster transformer: `@swc/jest` or esbuild-based transforms instead of `ts-jest` or Babel.
- Use `testEnvironment: "node"` for files that don't need the DOM.
- Make sure Jest's cache is on (and persisted in CI).
- Avoid importing huge barrel files (`index.ts` re-exporting everything) in tests. Jest loads all of it for every file.
- Mock heavy modules (icon libraries, charts) that you don't need to test.
- Find the slowest files (`--verbose`, or reporters that show durations) and look at them first.
- Check `maxWorkers` for your CI machine. Too many workers can be slower than fewer.
- Shard across CI machines.
- Consider moving to Vitest, which is often faster, especially for ESM projects.

### 319: How do you speed up a slow Vitest suite?

- Use `environment: "node"` (or the per-file comment) for tests that don't need the DOM. Try `happy-dom` instead of `jsdom`.
- Turn off CSS processing unless you need it (`test.css: false` is the default for non-module CSS).
- Avoid deep barrel imports. Vite has to transform every module in the import graph.
- Try `pool: "threads"` instead of `forks`, if your dependencies support it.
- If your tests clean up properly, `isolate: false` can give a big speed boost.
- Use `--shard` in CI, and `vitest related` / `--changed` locally.
- Look at the reported durations: `transform`, `setup`, `collect`, `environment` and `tests` times show you where the time goes. A big `setup` time often means a heavy setup file.

### 320: How would you migrate a project from Jest to Vitest?

1. Install Vitest and set up `test` in the Vite config with the same environment (jsdom) and setup files.
2. Turn on `globals: true` at first, so existing tests work without adding imports.
3. Replace `jest.` with `vi.`: `jest.fn` to `vi.fn`, `jest.mock` to `vi.mock`, `jest.spyOn` to `vi.spyOn`, timers and so on.
4. Fix the differences:
   - `jest.requireActual` becomes `await vi.importActual()` or `importOriginal` in the factory.
   - Mock factories for default exports need a `default` key.
   - `mockReset` behaves a bit differently (in Vitest it resets to the original implementation passed to `vi.fn(impl)`).
   - Snapshot formatting is slightly different, so update snapshots after checking the diffs.
5. Replace `moduleNameMapper` and transforms with Vite config (aliases, plugins).
6. Update coverage config, CI scripts and ESLint plugin.

Do it in steps on a big project. You can run both runners side by side for a while using different file patterns.

### 321: How would you migrate a large Enzyme test suite to React Testing Library?

You can't convert Enzyme tests one-to-one, because they test different things. Enzyme tests usually check state, props and component instances, which RTL doesn't let you access.

A practical plan:

1. Add RTL next to Enzyme. New tests are written only in RTL.
2. Prioritize: blocked React upgrades usually force you to migrate first the tests for components that break on the new React version.
3. Rewrite tests by **behavior**: read the Enzyme test, figure out what the user-facing behavior is, and write an RTL test for that. Delete Enzyme tests that only check internals.
4. Replace many small shallow tests with fewer integration tests per feature.
5. Track progress (number of Enzyme files left) and remove Enzyme when it reaches zero.

The rewrite often finds tests that were never testing anything useful.

### 322: What would you consider when moving an e2e suite from Cypress to Playwright?

- **Why**: need for WebKit, multiple tabs or domains, free parallelism, or speed. If the Cypress suite works well, migration has a real cost.
- **API style**: Cypress chains become `async`/`await`. `cy.get().should()` becomes `await expect(locator)`.
- **Retries**: both retry assertions, but the rules differ. Playwright actions auto-wait, Cypress queries retry.
- **Network mocks**: `cy.intercept` becomes `page.route`. Waiting on aliases becomes `page.waitForResponse`.
- **Auth**: `cy.session` becomes a setup project with `storageState`.
- **Custom commands** become fixtures or page object methods.
- **CI**: replace Cypress Cloud parallelism with Playwright sharding and merged reports.

Migrate feature by feature, run both suites for a while, and remove Cypress tests once the Playwright version is stable.

### 323: How would you design a testing strategy for a large React application?

- **Static checks everywhere**: strict TypeScript, ESLint with hooks, testing-library and jsx-a11y rules.
- **Unit tests** for business logic, utilities, reducers, complex hooks and schemas.
- **Integration tests as the main layer**: feature-level component tests with RTL, real providers and MSW. Most new tests go here.
- **Component tests in a real browser** for the design system and layout-heavy widgets, with visual and a11y checks (Storybook + Vitest Browser Mode, for example).
- **A small e2e suite** (Playwright) for critical flows against a real backend, with smoke tests after each deploy.
- **Contract tests or schema-generated types** between frontend and backend.
- **CI rules**: everything runs on pull requests, flaky tests get tracked and fixed, coverage can't drop.

And write it down, so everyone knows what kind of test to write for what kind of change.

### 324: How do you decide whether something needs a unit, integration or e2e test?

Ask: **what's the cheapest test that would catch this bug?**

- Complex logic with many cases (price rules, date math, validation)? **Unit** test. Cheap to cover all cases.
- How components, state and the API work together for one feature? **Integration** test.
- Depends on real browser behavior, layout, routing between real pages, the real backend, auth cookies or third-party services? **E2E** test.

Also think about the cost of a bug. Checkout and login deserve an e2e test even if they're also covered lower down. A settings toggle probably doesn't.

### 325: Where should the mocking boundary be in front-end tests?

As far out as you can while keeping tests fast and reliable. For most React apps, that's the **network**: mock HTTP with MSW and keep everything inside the app real.

Reasons:

- The network is the edge you don't control in front-end tests anyway.
- Everything inside (components, hooks, stores, data-fetching libraries) is tested together, like in production.
- Refactoring the inside (switching from `useEffect` fetching to React Query, for example) doesn't break tests.

Other good boundaries are things that are slow or random: time, `Math.random`, browser APIs that jsdom lacks, and third-party SDKs.

### 326: How do you organize tests in a monorepo?

- Each package has its own tests and test config, which extends a shared base config.
- Use **Vitest projects** (or Jest projects) at the root so one command can run everything, while each package keeps its own environment.
- Use the monorepo tool (Nx, Turborepo) to run only tests for **affected** packages on pull requests, with remote caching so unchanged packages don't run again.
- Put shared test helpers (custom render, factories, MSW handlers) in an internal package like `@acme/test-utils`.
- Keep e2e tests in their own package or app, since they test deployed apps, not single packages.

### 327: How would you design a shared test utilities package?

It could contain:

- a custom `render` with all app providers, with options to override things like the user, feature flags, route or initial store state
- re-exports of `@testing-library/react` and `user-event`, so tests import from one place
- data factories for domain objects (users, orders, products)
- default MSW handlers and helpers to override them
- polyfills and mocks for browser APIs
- custom matchers

Keep it small and well documented. If it gets too clever (for example, a `render` that hides lots of magic setup), tests become hard to understand. Make the defaults sensible and the overrides obvious.

### 328: How does consumer-driven contract testing with Pact work in a React project?

1. **Consumer test (frontend)**: you describe the interaction: "given user 1 exists, a GET to `/api/users/1` returns `{ id: number, name: string }`". Pact starts a mock server that answers exactly that. Your API client code runs against it, and if it works, Pact writes a contract file (the "pact").
2. **Publish**: the contract goes to a Pact Broker (or PactFlow).
3. **Provider verification (backend)**: the backend's CI downloads the contracts and replays the requests against the real backend, using "provider states" to set up data. If the responses don't match, the build fails.
4. **can-i-deploy**: before deploying either side, a check asks the broker whether the versions are compatible.

It's most useful when teams deploy independently. The downside is extra setup and maintenance, so small teams with one repo often use shared OpenAPI types instead.

### 329: How do you keep API mocks in sync with the real API?

If mocks drift from reality, tests pass while the app breaks. Ways to prevent it:

- **Generate types from the API schema** (OpenAPI, GraphQL schema) and type your MSW handlers and factories with them. A breaking change becomes a type error.
- **Generate mocks** from the schema (tools exist for OpenAPI to MSW and for GraphQL).
- **Validate mock responses against the schema** in tests.
- **Contract tests** between frontend and backend.
- Keep a few **e2e tests against the real backend**, which catch any remaining drift.

### 330: How do you write type-safe mocks?

- Use `vi.mocked(fn)` (or `jest.mocked`) so mock methods are typed.
- Use `vi.mock(import("./module"), ...)`, so the factory's return value is checked against the real module.
- Type `vi.fn` with the function type: `vi.fn<typeof fetchUser>()`.
- Type MSW handlers with generics: `http.get<never, never, User>("/api/user", ...)`.
- Make factories return full domain types, so missing fields fail type checks.
- Avoid `as any` in mocks. For partial objects, use `Partial<T>` only where the code really doesn't need the rest, and prefer building the full object with a factory.

### 331: How do you test components that use useTransition or useDeferredValue?

Test the user-visible result, not the scheduling. RTL wraps updates in `act`, which flushes transitions, so usually you just check the final state:

```tsx
test("filters the list while keeping the input responsive", async () => {
  const user = userEvent.setup();
  render(<BigFilterableList />);

  await user.type(screen.getByRole("searchbox"), "apple");

  expect(screen.getByRole("searchbox")).toHaveValue("apple");
  expect(await screen.findAllByRole("listitem")).toHaveLength(3);
});
```

If you want to check a pending state (like a dimmed list while `isPending` is true), the transition needs to be slow enough to see it. For example, use an async action with an MSW delay. You can't reliably test how fast React actually renders in jsdom. That's a job for performance profiling in a real browser.

### 332: How do you test streaming SSR and Server Components?

Mostly with e2e tests against the running app (like `next build && next start`):

```ts
test("shows the shell first and the slow section later", async ({ page }) => {
  await page.goto("/dashboard");

  await expect(page.getByRole("heading", { name: "Dashboard" })).toBeVisible();
  await expect(page.getByText("Loading recommendations...")).toBeVisible();
  await expect(
    page.getByRole("region", { name: "Recommendations" }),
  ).toBeVisible();
});
```

To make the streaming order testable, you can slow down the backend for that data, for example with a delayed mock API server. You can also check the raw HTML response with `request.get("/dashboard")` to make sure important content is server-rendered (good for SEO) and not only added by JavaScript.

### 333: How do you catch hydration mismatches in tests?

A hydration mismatch happens when the HTML from the server is different from what React renders on the client the first time, for example because of `Date.now()`, `Math.random()`, `typeof window` checks or browser extensions.

Ways to catch them:

- **E2E**: listen to `console` errors in Playwright and fail on messages about hydration (React 19 logs one clear error with a diff).
- **Unit**: render to a string with `renderToString`, put it in a container, then call RTL's `render(ui, { container, hydrate: true })` and fail the test if `console.error` was called.
- **React 19 root option**: `onRecoverableError` on `hydrateRoot` is called for hydration errors, which you can hook into in tests or monitoring.

Then fix the cause: move client-only values into `useEffect`, or use `useSyncExternalStore` with a server snapshot.

### 334: How do you test server-rendered HTML output?

Use React's server APIs directly:

```tsx
import { renderToString } from "react-dom/server";

test("renders the product name on the server", () => {
  const html = renderToString(
    <ProductPage product={{ name: "Laptop", price: 999 }} />,
  );
  expect(html).toContain("<h1>Laptop</h1>");
});
```

For streaming and Suspense, `renderToString` doesn't wait for data. Use `prerender` from `react-dom/static` (which waits for all Suspense content) or `renderToReadableStream` and read the stream to the end. Run these tests in the `node` environment. For full framework pages (Next.js), it's simpler to test the HTML with Playwright's `request.get()`.

### 335: How are render errors reported in React 19 and how does that affect tests?

In React 19, errors are no longer thrown again and logged twice:

- Errors **caught** by an error boundary are reported with `console.error`.
- Errors **not caught** by any boundary are reported with `window.reportError`, and React removes the whole tree.
- `createRoot` and `hydrateRoot` accept `onCaughtError`, `onUncaughtError` and `onRecoverableError` to handle these.

For tests:

- Error boundary tests still need to silence `console.error`, because the caught error is logged there.
- Inside `act`, React collects uncaught render errors and throws them again when the `act` scope ends, so `expect(() => render(<Broken />)).toThrow()` still works.
- RTL 16.1 and later let you pass `onCaughtError` and `onRecoverableError` as `render` options when you need to check errors directly.

### 336: Does the React Compiler change how you write tests?

Not much, if your tests check behavior. The compiler adds automatic memoization. A component that behaves correctly without it should behave the same with it.

Things to watch:

- Code that broke the Rules of React (mutating props, reading refs during render) can behave differently after compiling. Tests that only passed because of that bad behavior may start failing. That's a good thing, it shows real bugs.
- Tests that count renders will see different numbers. That's another reason not to write those tests.
- Make sure the test setup compiles code the same way as the app (same Babel plugin or Vite plugin in the test config), otherwise you're testing different code than you ship.

### 337: Should you test how many times a component re-renders?

Usually no. Render counts are an implementation detail. They change when you refactor, upgrade React, or turn on the React Compiler, even though the app works the same. And a lower count in jsdom doesn't prove the app is fast.

Exceptions where it can make sense:

- A library whose main promise is avoiding re-renders (like a state management library or a virtualized list). There, the render count is part of the public behavior.
- A regression test for a real performance bug, using the `<Profiler>` API's `onRender` callback.

For app performance, measure in a real browser: React DevTools Profiler, Chrome performance traces, or Web Vitals in e2e or lab tests.

### 338: How do you include performance checks in automated testing?

- **Lighthouse CI**: run Lighthouse on key pages in CI and fail if scores or metrics (LCP, CLS, Total Blocking Time) go past a budget.
- **Bundle size checks**: tools like size-limit fail the build when a bundle grows too much.
- **Playwright**: measure things through `page.evaluate` with the Performance API, or collect Web Vitals with the `web-vitals` library and check thresholds. Use Chrome DevTools Protocol to throttle CPU and network for realistic numbers.
- **Real user monitoring** in production, which is the final source of truth.

Lab numbers are noisy, so use generous budgets, run several times and look at trends instead of single runs.

### 339: How do you test that a component handles out-of-order responses correctly?

This is a classic race condition. The user types "ab", then "abc", and the response for "ab" arrives last and overwrites the correct results. Make the first request slower in MSW:

```tsx
test("shows results for the latest query only", async () => {
  server.use(
    http.get("/api/search", async ({ request }) => {
      const q = new URL(request.url).searchParams.get("q");
      if (q === "ab") await delay(300); // old request is slow
      return HttpResponse.json([{ id: q, title: `Result for ${q}` }]);
    }),
  );
  const user = userEvent.setup();
  render(<Search />);

  await user.type(screen.getByRole("searchbox"), "ab");
  await user.type(screen.getByRole("searchbox"), "c");

  expect(await screen.findByText("Result for abc")).toBeInTheDocument();
  await new Promise((r) => setTimeout(r, 400)); // let the slow response arrive
  expect(screen.queryByText("Result for ab")).not.toBeInTheDocument();
});
```

The fix in the component is usually ignoring stale responses in the effect cleanup, using an `AbortController`, or using a data-fetching library that handles it.

### 340: How do you test that a request is cancelled with AbortController?

Check that the signal was aborted, for example when the component unmounts:

```tsx
test("aborts the request on unmount", async () => {
  let signal: AbortSignal | undefined;
  server.use(
    http.get("/api/report", async ({ request }) => {
      signal = request.signal;
      await delay("infinite");
    }),
  );

  const { unmount } = render(<Report />);
  await waitFor(() => expect(signal).toBeDefined());

  unmount();
  expect(signal!.aborted).toBe(true);
});
```

`delay("infinite")` keeps the request pending forever. You can also spy on `fetch` and check the `signal` passed in its options.

### 341: How do you test retry logic?

Make the first requests fail and a later one succeed. MSW's `once` option is useful here:

```tsx
test("retries after a failed request", async () => {
  server.use(
    http.get("/api/data", () => new HttpResponse(null, { status: 503 }), {
      once: true,
    }),
    http.get("/api/data", () => HttpResponse.json({ items: ["ok"] })),
  );

  render(<DataView />);
  expect(await screen.findByText("ok")).toBeInTheDocument();
});
```

MSW checks handlers in order, so the 503 handler answers the first request and is then used up. The next request falls through to the success handler. If the retry waits with backoff, use fake timers or set a short delay in tests. Also test the case where all retries fail.

### 342: How do you test RTK Query endpoints?

Test them through components or hooks with a real store and MSW, not by mocking RTK Query:

```tsx
function setupApiStore() {
  return configureStore({
    reducer: { [api.reducerPath]: api.reducer },
    middleware: (gDM) => gDM().concat(api.middleware),
  });
}

test("loads posts", async () => {
  const store = setupApiStore();
  const { result } = renderHook(() => useGetPostsQuery(), {
    wrapper: ({ children }) => <Provider store={store}>{children}</Provider>,
  });

  await waitFor(() => expect(result.current.isSuccess).toBe(true));
  expect(result.current.data).toHaveLength(2);
});
```

Create a new store per test, so the cache doesn't leak. Things worth testing: cache invalidation (a mutation with `invalidatesTags` refetches the list), error handling, and conditional fetching with `skip`.

### 343: How do you test infinite scrolling?

In jsdom, `IntersectionObserver` doesn't exist, so you control a mock and trigger it yourself:

```tsx
let trigger: (entries: Partial<IntersectionObserverEntry>[]) => void;

beforeEach(() => {
  vi.stubGlobal(
    "IntersectionObserver",
    class {
      constructor(cb: IntersectionObserverCallback) {
        trigger = (entries) =>
          cb(entries as IntersectionObserverEntry[], this as any);
      }
      observe() {}
      unobserve() {}
      disconnect() {}
    },
  );
});

test("loads the next page when the sentinel becomes visible", async () => {
  render(<Feed />);
  expect(await screen.findAllByRole("article")).toHaveLength(10);

  act(() => trigger([{ isIntersecting: true }]));

  await waitFor(() => expect(screen.getAllByRole("article")).toHaveLength(20));
});
```

For real scrolling behavior, also add one e2e test that scrolls with `page.mouse.wheel` or `locator.scrollIntoViewIfNeeded()` and checks that more items load.

### 344: How do you test virtualized lists?

Virtualized lists (react-window, TanStack Virtual) only render the items that fit in the viewport, based on measured sizes. In jsdom all sizes are 0, so they often render nothing or only a few items.

Options:

- Mock the element sizes. Many libraries let you pass a fixed size or an initial rect in tests, or you can stub `getBoundingClientRect` / `offsetHeight`.
- Mock the virtualization so it renders everything in tests. This is simple, but you no longer test the virtualization.
- Test in a real browser (Vitest Browser Mode or Playwright), where scrolling and sizes work. This is the most reliable option for checking that scrolling brings in new rows.

Keep the logic around the list (filtering, selection) in jsdom tests, and test the scrolling itself in a browser.

### 345: How do you test charts and canvas-based components?

Canvas content isn't in the DOM, so you can't query it.

- **Test the data, not the pixels**: move data preparation (grouping, totals, scales) into functions and unit test them.
- **Accessible alternatives**: a good chart has a text summary, an `aria-label` or a hidden data table. Test that, and it helps users too.
- **SVG charts** (like Recharts) render real DOM elements, so you can check labels and legends. But in jsdom they often need a fixed size, because responsive containers measure 0.
- **Visual regression** in a real browser for how the chart looks.
- In jsdom you may need `vitest-canvas-mock` or `jest-canvas-mock` just to stop canvas calls from crashing.

### 346: How do you test a component that wraps a rich text editor?

Rich text editors (Lexical, Tiptap, Slate, ProseMirror) depend a lot on `contenteditable`, selection and input events, which jsdom only partly supports.

- Test **your** logic around the editor: toolbar buttons that call editor commands, converting content to and from your storage format, validation, character limits. Often you can drive the editor through its API in the test instead of typing.
- Test real typing, selecting and formatting in a **real browser** (Playwright or Vitest Browser Mode). Use `locator.pressSequentially()` or `page.keyboard` in Playwright, and check the resulting HTML or the saved data.
- Don't try to test the editor library itself. That's the maintainers' job.

### 347: What problems do you hit when testing components built with third-party UI libraries?

- **Portals**: menus and dialogs render in `document.body`. Use `screen` and `within(screen.getByRole("dialog"))`.
- **pointer-events checks**: some libraries set `pointer-events: none` on `body` while a modal is open, and `user-event` refuses to click. Set `pointerEventsCheck: PointerEventsCheckLevel.Never` in `userEvent.setup()` for those tests.
- **Missing browser APIs**: Radix and others use `ResizeObserver`, `DOMRect`, `hasPointerCapture` or `scrollIntoView`. Add polyfills in the setup file.
- **Animations and delays**: components appear after a transition. Use `findBy`.
- **Different DOM structure**: always query by role and name, never by the library's class names, which change between versions.

If tests for a library component get very complicated, cover that part with browser tests instead.

### 348: How do you test code that uses Web Workers?

jsdom doesn't support `Worker`. Options:

- **Separate the logic**: put the actual work in a plain module and unit test it directly. The worker file is just a thin wrapper that receives messages and calls it.
- **Mock the worker** in component tests with a fake class that answers `postMessage` the way your worker would:

```ts
class FakeWorker {
  onmessage: ((e: MessageEvent) => void) | null = null;
  postMessage(data: { numbers: number[] }) {
    const sum = data.numbers.reduce((a, b) => a + b, 0);
    queueMicrotask(() => this.onmessage?.({ data: { sum } } as MessageEvent));
  }
  terminate() {}
}
vi.stubGlobal("Worker", FakeWorker);
```

- **Real browser tests** (Vitest Browser Mode or Playwright) for the real worker.

Libraries like Comlink make this easier, because you can test the exposed object without a worker at all.

### 349: How do you test offline behavior and service workers?

In Playwright:

```ts
test("shows the offline banner and queues the message", async ({
  page,
  context,
}) => {
  await page.goto("/chat");
  await context.setOffline(true);

  await page.getByRole("textbox").fill("Hello");
  await page.getByRole("button", { name: "Send" }).click();
  await expect(page.getByText("You are offline")).toBeVisible();

  await context.setOffline(false);
  await expect(page.getByText("Sent")).toBeVisible();
});
```

For service workers, run against a production build (they usually aren't active in dev), and check caching by going offline and reloading. Playwright can access service workers through `context.serviceWorkers()`. Requests made by a service worker don't always go through `page.route`, so mocks can be skipped. When a service worker gets in the way of your mocks in other tests, set `serviceWorkers: "block"` in the config.

### 350: How do you test login with an external OAuth provider in e2e tests?

Logging in through the real Google or GitHub page in tests is fragile. Those pages change, have bot detection, CAPTCHAs and 2FA, and you shouldn't automate them.

Better options:

- Use a **test identity provider** in test environments (a mock OAuth server, or a Keycloak or Auth0 test tenant with test users).
- Add a **test-only login endpoint**, enabled only outside production, that creates a session for a test user. Then save it with `storageState`.
- Test the **callback handling** separately by calling your callback URL with a mocked token exchange.

Keep one manual or monitored check that the real provider integration works in staging.

### 351: How do you test a scenario with two users in Playwright?

Create two browser contexts. Each one is like a separate browser profile with its own cookies and storage:

```ts
test("admin sees the request a member just sent", async ({ browser }) => {
  const memberContext = await browser.newContext({
    storageState: "playwright/.auth/member.json",
  });
  const adminContext = await browser.newContext({
    storageState: "playwright/.auth/admin.json",
  });
  const member = await memberContext.newPage();
  const admin = await adminContext.newPage();

  await member.goto("/requests/new");
  await member.getByLabel("Reason").fill("Need access to billing");
  await member.getByRole("button", { name: "Send request" }).click();

  await admin.goto("/admin/requests");
  await expect(admin.getByText("Need access to billing")).toBeVisible();

  await memberContext.close();
  await adminContext.close();
});
```

This is useful for chat, sharing, permissions and approval flows. You can wrap the second user in a fixture to keep tests short.

### 352: How would you test real-time collaboration features?

- **Unit level**: test the merge or sync logic (operational transforms, CRDT updates, conflict rules) as pure functions with many cases. Property-based tests work well here.
- **Integration level**: use a fake transport (a fake WebSocket or MSW `ws`) to push remote changes into the component and check the UI updates, shows presence and resolves conflicts.
- **E2E level**: two browser contexts editing the same document against a real backend. Check that both see each other's changes, and test going offline and coming back with `context.setOffline`.

Use web-first assertions with enough timeout for sync delays, and give each test its own document, so parallel runs don't interfere.

### 353: How does Playwright control browsers?

The test runner runs in Node. It talks to the browser over a protocol connection (a WebSocket or pipe). For Chromium it uses the Chrome DevTools Protocol, and for Firefox and WebKit it uses patched browser builds that Playwright ships, which support its own protocol.

Because the test code runs **outside** the browser:

- it can control several pages, contexts and even browsers at once
- it can intercept network traffic at the browser level
- it isn't limited by the same-origin policy
- every action is a message to the browser, which is why every call is `async`

This is the opposite of Cypress, where the test code runs inside the browser next to the app.

### 354: What is a browser context and why is it cheap?

A browser context is an isolated session inside one browser process, like an incognito window. It has its own cookies, storage, cache and permissions.

Starting a new browser for every test would be slow. Creating a context only takes milliseconds. So Playwright starts one browser per worker and gives every test a fresh context. You get full isolation between tests without paying the browser startup cost each time.

### 355: What are worker-scoped fixtures and when do you use them?

By default, fixtures are created for every test. A worker-scoped fixture is created once per worker process and shared by all tests that worker runs:

```ts
export const test = base.extend<
  {},
  { dbUser: { email: string; password: string } }
>({
  dbUser: [
    async ({}, use, workerInfo) => {
      const user = await createUser(`worker${workerInfo.workerIndex}@test.com`);
      await use(user);
      await deleteUser(user.email);
    },
    { scope: "worker" },
  ],
});
```

Use them for expensive things that are safe to share within a worker, like a test account, a seeded tenant or a database connection. Using `workerIndex` gives each worker its own account, so parallel workers don't clash.

### 356: How do you run e2e tests in parallel against one shared backend without conflicts?

- **Separate data per test or per worker**: each test creates its own records with unique names, or each worker gets its own account or tenant.
- **Don't depend on global counts**: instead of "the list has 3 items", check that "my item is in the list".
- **Avoid shared global settings**: if a test changes a global setting, run it in its own project with one worker, or reset it carefully.
- **Clean up** in fixture teardown, plus a periodic cleanup job for leftovers from crashed runs.
- **Separate environments**: for complete isolation, spin up a backend and database per CI run (Docker Compose, Testcontainers or preview environments).

### 357: How do you run a big Playwright suite across many CI machines and get one report?

Shard the tests and merge the blob reports:

```yaml
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        shard: [1/4, 2/4, 3/4, 4/4]
    steps:
      # ... checkout, install
      - run: npx playwright test --shard=${{ matrix.shard }} --reporter=blob
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: blob-report-${{ strategy.job-index }}
          path: blob-report

  merge:
    needs: test
    if: ${{ !cancelled() }}
    steps:
      # ... checkout, install
      - uses: actions/download-artifact@v4
        with:
          path: all-blob-reports
          pattern: blob-report-*
          merge-multiple: true
      - run: npx playwright merge-reports --reporter html ./all-blob-reports
```

With `fullyParallel: true`, Playwright splits by individual tests, so the shards are more even. Otherwise it splits by files.

### 358: What is test quarantine and how should it work?

Quarantine means moving a known flaky test out of the blocking test run, while still running and tracking it, until it's fixed.

A good process:

1. A test is detected as flaky (it passed on retry, or a flaky-test dashboard flags it).
2. It gets tagged (for example `@quarantine`) and a ticket with an owner.
3. CI runs quarantined tests in a separate, non-blocking job, so you can see whether the fix worked.
4. After it's fixed and stable for a while, the tag is removed.
5. If nobody fixes it within a set time, delete it or rewrite it.

Without a time limit, quarantine becomes a place where tests go to be forgotten.

### 359: How does Cypress work internally and what limits does that cause?

Cypress runs your test code inside the browser, in an iframe next to your app's iframe, and a Node server process handles things like network proxying and file access.

Benefits: direct access to the app's `window`, fast DOM access, and the interactive time-travel runner.

Limits that come from this design:

- **One tab only**. You can't control a second tab or window.
- **Cross-origin navigation** needs `cy.origin()`.
- **Code running in Node** (database access, file system) has to go through `cy.task()`.
- **The command queue** instead of `async`/`await`, which confuses many developers.
- **Iframes** need extra work.

### 360: How would you choose an e2e tool for a new React project?

Questions to ask:

- **Which browsers do we need?** Need Safari coverage? Playwright supports WebKit.
- **Multi-tab, multi-user, multiple domains?** Easier in Playwright.
- **Team experience?** If the team knows Cypress well, that matters.
- **Budget for parallel runs?** Playwright sharding is free. Cypress parallelism usually needs Cypress Cloud or a third-party service.
- **Debugging style?** Cypress's interactive runner is great. Playwright's UI mode and trace viewer are also very strong.
- **Component testing?** Cypress component testing is mature. Playwright's is still experimental, and Vitest Browser Mode is another option.
- **Language?** Playwright also has Python, Java and .NET versions, which helps if QA engineers use those.

For most new projects today, Playwright is the default choice, but neither is a wrong choice.

### 361: How do you make visual regression testing work at scale?

- **Same rendering environment**: run screenshots in the same Docker image locally and in CI, so fonts and anti-aliasing match.
- **Stable content**: mock dates, use fixed seed data, hide or mask dynamic parts (`mask` option), disable animations, wait for fonts and images.
- **Small targets**: screenshot components or sections, not huge full pages, so diffs point at the real problem.
- **Thresholds**: allow tiny pixel differences (`maxDiffPixelRatio`), but not so much that real changes slip through.
- **Review flow**: make updating baselines a deliberate step with someone reviewing the diff images. Services like Chromatic or Percy give you a review UI.
- **Limit browsers and viewports** to the ones that matter, because every combination multiplies the number of baselines.

### 362: What are ARIA snapshots in Playwright?

An ARIA snapshot compares the accessibility tree of an element (roles, names and structure) with a YAML template, instead of comparing HTML or pixels:

```ts
await expect(page.getByRole("navigation")).toMatchAriaSnapshot(`
  - navigation:
    - link "Home"
    - link "Pricing"
    - link "Docs"
    - button "Sign in"
`);
```

It's more stable than an HTML snapshot (class names and wrapper divs don't matter) and checks what assistive technology sees. You can use regular expressions for dynamic text, and Playwright can generate or update the templates with `--update-snapshots`.

### 363: What does a good accessibility testing strategy look like, and what can't automation catch?

**Automated layers**:

- ESLint `jsx-a11y` rules while coding
- role-based queries in RTL, which fail when roles and labels are missing
- axe checks in component tests and on key pages in Playwright
- keyboard navigation tests for important widgets
- ARIA snapshots for complex components

**What automation misses**: whether alt text actually describes the image, whether the focus order makes sense, whether screen reader announcements are understandable, whether error messages are clear, whether custom widgets behave like users expect, and many contrast issues over images.

So you still need manual checks with a keyboard and at least one screen reader (VoiceOver, NVDA) for important flows, and ideally feedback from real users with disabilities.

### 364: How do you test focus management in a modal dialog?

A good modal moves focus into the dialog when it opens, keeps Tab inside it, closes on Escape and returns focus to the button that opened it:

```tsx
test("manages focus correctly", async () => {
  const user = userEvent.setup();
  render(<DeleteProject />);

  const openButton = screen.getByRole("button", { name: "Delete project" });
  await user.click(openButton);

  const dialog = screen.getByRole("dialog");
  const cancel = within(dialog).getByRole("button", { name: "Cancel" });
  const confirm = within(dialog).getByRole("button", { name: "Delete" });

  expect(cancel).toHaveFocus();
  await user.tab();
  expect(confirm).toHaveFocus();
  await user.tab();
  expect(cancel).toHaveFocus(); // focus wraps, stays inside

  await user.keyboard("{Escape}");
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  expect(openButton).toHaveFocus();
});
```

If you use the native `<dialog>` element with `showModal()`, check that your jsdom version supports it, or test this in a real browser.

### 365: How can tests help with front-end security?

- **XSS**: render user content containing `<img src=x onerror=alert(1)>` or `<script>` and check it shows up as text, or is sanitized if you use `dangerouslySetInnerHTML`. Unit test the sanitizer function with known attack strings.
- **URLs**: test that links built from user input reject `javascript:` URLs.
- **Auth and permissions**: e2e tests that a user can't see or open another user's data, and that protected pages redirect when logged out. Also test the API directly, because hiding a button in the UI isn't protection.
- **Sensitive data**: check that tokens aren't stored in `localStorage` if your policy forbids it, and that errors don't show stack traces.
- **Dependencies**: `npm audit` or similar in CI.

Tests don't replace security reviews or scanners, but they stop known problems from coming back.

### 366: How do you test security headers and Content Security Policy?

Check the response headers in Playwright:

```ts
test("sends security headers", async ({ page }) => {
  const response = await page.goto("/");
  const headers = response!.headers();

  expect(headers["content-security-policy"]).toContain("default-src 'self'");
  expect(headers["x-content-type-options"]).toBe("nosniff");
  expect(headers["strict-transport-security"]).toBeDefined();
});
```

And check that the CSP doesn't break the app, by failing on CSP violation errors in the console:

```ts
page.on("console", (msg) => {
  if (
    msg.type() === "error" &&
    msg.text().includes("Content Security Policy")
  ) {
    throw new Error(`CSP violation: ${msg.text()}`);
  }
});
```

Run this against a production-like build, since dev servers often send different headers.

### 367: What is mutation testing?

Mutation testing checks how good your tests are. A tool (for JavaScript, Stryker) changes your code in small ways, called mutants: it flips `>` to `>=`, removes a function call, replaces `true` with `false`. Then it runs your tests against each mutant.

- If a test fails, the mutant is **killed**. Good, your tests noticed the change.
- If all tests pass, the mutant **survived**. Your tests don't really check that code.

The result is a mutation score. It's much more honest than code coverage, because covering a line isn't enough; you have to actually check its result. It's slow, so teams usually run it on important modules or only on changed files, not on every commit.

### 368: What is property-based testing and where is it useful in front-end code?

Instead of picking example inputs yourself, you describe what's always true and a library generates hundreds of random inputs to try to break it. In JavaScript the common library is `fast-check`:

```ts
import fc from "fast-check";

test("formatting and parsing a price gives back the same number", () => {
  fc.assert(
    fc.property(fc.integer({ min: 0, max: 10_000_000 }), (cents) => {
      expect(parsePrice(formatPrice(cents))).toBe(cents);
    }),
  );
});
```

When it finds a failing input, it shrinks it to the smallest case that still fails. It's useful for parsers, formatters, serializers, sorting and filtering, date math, undo/redo and sync logic, where hand-picked examples easily miss edge cases.

### 369: How do you measure test quality beyond coverage?

- **Mutation score**: do tests fail when the code is broken on purpose?
- **Escaped bugs**: how many production bugs had no test that should have caught them? Look at each one.
- **Flakiness rate**: how often tests fail without a code change.
- **Speed**: how long the suite takes locally and in CI. Slow suites get skipped.
- **Maintenance cost**: how often tests need fixing after changes that didn't change behavior. That shows tests coupled to implementation details.
- **Confidence**: does the team feel safe deploying when the tests are green? If people still test everything manually, the suite isn't doing its job.

### 370: Can you combine coverage from unit tests and e2e tests?

Yes, but it takes work. For e2e coverage, the app has to be built with instrumentation (for example with `vite-plugin-istanbul` or `babel-plugin-istanbul`). Then you collect `window.__coverage__` after each test (Cypress has `@cypress/code-coverage`, in Playwright you collect it yourself in a fixture, or use the Chromium-only `page.coverage` API). Then you merge it with the unit test coverage using `nyc merge` or similar.

It's useful to find features no test touches at any level. But it's slow and complex to keep running, so many teams only look at unit coverage and use e2e tests for critical flows without measuring their coverage.

### 371: What is synthetic monitoring?

Synthetic monitoring runs a few e2e-style tests against **production** on a schedule, for example every 5 minutes from several regions. If login or checkout breaks, you get an alert, even if no user has reported it yet.

You can reuse Playwright tests for this (some monitoring services run Playwright scripts directly, like Checkly). Use dedicated test accounts, don't create real orders or payments (or use a special test mode), and keep the checks read-only or self-cleaning where possible.

### 372: How do you test micro-frontends?

- **Each micro-frontend** has its own unit and integration tests and its own e2e tests, with the shell and other remotes mocked or stubbed.
- **Contracts between them**: shared events, props or a shared state API should be typed and versioned, and tested with contract-style tests (for example, a test that the event a remote sends matches the schema the shell expects).
- **Integration e2e**: a small set of tests runs the shell with the real deployed remotes to check they load and work together, including version mismatches and a remote failing to load (the shell should show a fallback).
- **Shared dependencies**: test that duplicate React copies don't break hooks, which is a common Module Federation problem.

### 373: How do you test a design system component library?

- **Unit and interaction tests** for every component: keyboard support, ARIA attributes, controlled and uncontrolled modes, events.
- **Real browser tests**, because components depend on CSS, focus and layout. Storybook with the Vitest addon or Vitest Browser Mode work well.
- **Visual regression** for every story, in light and dark themes and at a few viewports.
- **Accessibility checks** with axe on every story.
- **Cross-browser** runs, including WebKit.
- **Type tests** for complex prop types (polymorphic `as` props, generics).
- **Consumer tests**: check the published package works in a sample app (ESM and CJS imports, SSR, tree shaking).

A bug in the design system shows up in every app that uses it, so it's worth testing more thoroughly than app code.

### 374: How do Storybook interaction tests and the Vitest addon work together?

A story can have a `play` function that runs after the story renders:

```tsx
import type { Meta, StoryObj } from "@storybook/react-vite";
import { expect, fn } from "storybook/test";
import { LoginForm } from "./LoginForm";

const meta = { component: LoginForm, args: { onSubmit: fn() } } satisfies Meta<
  typeof LoginForm
>;
export default meta;

export const FilledForm: StoryObj<typeof meta> = {
  play: async ({ args, canvas, userEvent }) => {
    await userEvent.type(canvas.getByLabelText("Email"), "anna@test.com");
    await userEvent.type(canvas.getByLabelText("Password"), "secret123");
    await userEvent.click(canvas.getByRole("button", { name: "Log in" }));
    await expect(args.onSubmit).toHaveBeenCalled();
  },
};
```

The `@storybook/addon-vitest` addon turns every story into a Vitest test running in a real browser through Vitest Browser Mode. Stories without a `play` function become smoke tests (they must render without errors), and stories with one become interaction tests. You can also add a11y checks. So one file serves as docs, visual review and tests.

### 375: How do you test right-to-left layouts and translation edge cases?

- **Pluralization**: test counts like 0, 1, 2, 5 and 21 in languages with complex plural rules (Polish, Arabic, Russian), since `count === 1 ? "item" : "items"` is wrong for many languages. Unit test your message formatting with each locale.
- **Missing keys**: a test or build step that fails when a translation key is missing in any locale.
- **Long text**: German and Finnish strings can be much longer. Visual tests with a "pseudo-locale" (longer, accented text) catch truncated buttons.
- **RTL**: set `dir="rtl"` and run visual tests in Arabic or Hebrew to catch icons, margins and arrows facing the wrong way. Use CSS logical properties (`margin-inline-start`) to avoid most of these bugs.
- **Formatting**: dates, numbers and currencies with `Intl` per locale.

### 376: How do you make tests independent of the machine's time zone?

Tests that format dates can pass on a laptop in Berlin and fail in CI running in UTC.

- Set the time zone for the test process: `TZ=UTC vitest run` in the npm script, or set `process.env.TZ = "UTC"` in a global setup file (it must be set before any date code runs).
- Pass the time zone explicitly in code where it matters (`Intl.DateTimeFormat(locale, { timeZone })`), so you can test several zones in one run.
- In Playwright, set `timezoneId` and `locale` in `use`, so the browser behaves the same everywhere.
- Test tricky dates on purpose: daylight saving changes, end of month, end of year, Feb 29.

### 377: Why can Intl formatting give different results in tests and in the browser?

Node and browsers can have different versions of ICU, the library behind `Intl`, and different locale data. So the same call can produce slightly different output, for example a regular space vs a narrow no-break space (U+202F) before AM/PM, or different currency symbols placement.

Tests with exact string matches on formatted dates and prices then break after a Node or browser upgrade. Ways to handle it:

- Build expected values with the same `Intl` call in the test, instead of hardcoding them.
- Normalize whitespace before comparing.
- Use regular expressions that allow both kinds of spaces.
- Pin the Node version in CI (`.nvmrc`) so upgrades happen on purpose.

### 378: How do you test a date picker?

- **Fix "today"** with fake timers and `setSystemTime`, so the visible month is always the same.
- **Use roles**: a good date picker uses `grid` and `gridcell` (or buttons with full date labels like "Monday, March 16, 2026"), so you can select a day by its accessible name.
- **Test keyboard support**: arrow keys move between days, Page Up/Down changes months, Enter selects, Escape closes.
- **Test edge cases**: min and max dates, disabled days, month and year boundaries, different locales (week starting on Monday or Sunday).
- **Typed input**: if users can type a date, test valid and invalid formats.

If the picker comes from a library, test your integration (the value you get and how you show it), not every feature of the library.

### 379: How do you write a custom query in React Testing Library?

Use `buildQueries` from `@testing-library/react` (re-exported from `@testing-library/dom`) and add the result to your custom render:

```ts
import {
  buildQueries,
  queryHelpers,
  type Matcher,
} from "@testing-library/react";

const queryAllByDataCy = (container: HTMLElement, id: Matcher) =>
  queryHelpers.queryAllByAttribute("data-cy", container, id);

const getMultipleError = (_c: Element | null, id: Matcher) =>
  `Found multiple elements with data-cy="${id}"`;
const getMissingError = (_c: Element | null, id: Matcher) =>
  `Unable to find an element with data-cy="${id}"`;

export const [
  queryByDataCy,
  getAllByDataCy,
  getByDataCy,
  findAllByDataCy,
  findByDataCy,
] = buildQueries(queryAllByDataCy, getMultipleError, getMissingError);
```

`buildQueries` creates all the `get`, `query` and `find` variants from one `queryAll` function. If you only need a different test ID attribute, `configure({ testIdAttribute: "data-cy" })` is simpler.

### 380: What can you change with RTL's configure function?

```ts
import { configure } from "@testing-library/react";

configure({
  testIdAttribute: "data-qa", // attribute used by getByTestId
  asyncUtilTimeout: 2000, // default timeout for waitFor and findBy
  throwSuggestions: true, // fail when a better query exists (good for learning)
  getElementError: (message, container) =>
    new Error(message ?? "Element not found"),
  reactStrictMode: true, // render inside StrictMode by default
});
```

`getElementError` is often used to shorten the huge DOM dumps in error messages on CI. `reactStrictMode: true` makes tests behave like development mode with StrictMode, which finds effects that don't clean up properly. Put `configure` in the setup file so it applies everywhere.

### 381: How do you type a custom render function with extra options?

Extend RTL's `RenderOptions` and return the normal result plus any extras:

```tsx
import { render, type RenderOptions } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

type ExtraOptions = {
  route?: string;
  currentUser?: User | null;
  preloadedState?: Partial<RootState>;
};

export function renderApp(
  ui: React.ReactElement,
  {
    route = "/",
    currentUser = null,
    preloadedState,
    ...options
  }: ExtraOptions & Omit<RenderOptions, "wrapper"> = {},
) {
  const store = setupStore(preloadedState);

  const Wrapper = ({ children }: { children: React.ReactNode }) => (
    <Provider store={store}>
      <AuthContext.Provider value={{ user: currentUser }}>
        <MemoryRouter initialEntries={[route]}>{children}</MemoryRouter>
      </AuthContext.Provider>
    </Provider>
  );

  return {
    store,
    user: userEvent.setup(),
    ...render(ui, { wrapper: Wrapper, ...options }),
  };
}
```

The option is called `currentUser` so it doesn't clash with `user`, the user-event instance in the return value. Returning that instance from the render helper saves a line in every test:

```tsx
const { user } = renderApp(<AccountPage />, {
  route: "/account",
  currentUser: buildUser(),
});
await user.click(screen.getByRole("button", { name: "Edit" }));
```

### 382: How do you test a hook built on useSyncExternalStore?

Use the real store, change it from outside React inside `act`, and check the hook's result:

```tsx
test("reflects changes to the online status", () => {
  const { result } = renderHook(() => useOnlineStatus());
  expect(result.current).toBe(true);

  act(() => {
    Object.defineProperty(navigator, "onLine", {
      value: false,
      configurable: true,
    });
    window.dispatchEvent(new Event("offline"));
  });

  expect(result.current).toBe(false);
});
```

For your own stores, also test that the hook unsubscribes on unmount, that the snapshot function returns the same value when nothing changed (otherwise React re-renders forever, and in dev it warns), and the server snapshot if the app uses SSR.

### 383: How do you test a component that exposes methods with useImperativeHandle?

Pass a ref in the test and call the methods inside `act`:

```tsx
test("focus() focuses the inner input", () => {
  const ref = createRef<{ focus: () => void; clear: () => void }>();
  render(<FancyInput ref={ref} defaultValue="hello" />);

  act(() => ref.current!.focus());
  expect(screen.getByRole("textbox")).toHaveFocus();

  act(() => ref.current!.clear());
  expect(screen.getByRole("textbox")).toHaveValue("");
});
```

In React 19, `ref` is a normal prop for function components, so you don't need `forwardRef`. The imperative methods are part of the component's public API, so testing them directly is fine.

### 384: How do you test code that calls scrollIntoView or scrolls the page?

jsdom doesn't implement `scrollIntoView`, and `window.scrollTo` only logs a "not implemented" error. Mock them and check they were called:

```ts
// setupTests.ts
Element.prototype.scrollIntoView = vi.fn();
window.scrollTo = vi.fn() as unknown as typeof window.scrollTo;
```

```tsx
test("scrolls to the first error on submit", async () => {
  const user = userEvent.setup();
  render(<LongForm />);

  await user.click(screen.getByRole("button", { name: "Submit" }));
  expect(screen.getByLabelText("Email").scrollIntoView).toHaveBeenCalled();
});
```

This only checks the call. To check the page actually scrolled to the right place, use Playwright and `expect(locator).toBeInViewport()`.

### 385: How do you test a feature that downloads a generated file in a unit test?

When code creates a Blob and downloads it through a temporary link, mock the parts jsdom doesn't support:

```tsx
test("exports the table as CSV", async () => {
  const createObjectURL = vi.fn(() => "blob:fake-url");
  const revokeObjectURL = vi.fn();
  vi.stubGlobal("URL", { ...URL, createObjectURL, revokeObjectURL });
  const click = vi
    .spyOn(HTMLAnchorElement.prototype, "click")
    .mockImplementation(() => {});

  const user = userEvent.setup();
  render(<UsersTable users={[{ name: "Anna", email: "anna@test.com" }]} />);
  await user.click(screen.getByRole("button", { name: "Export CSV" }));

  const blob = createObjectURL.mock.calls[0][0] as unknown as Blob;
  expect(await blob.text()).toBe("name,email\nAnna,anna@test.com");
  expect(click).toHaveBeenCalled();
  expect(revokeObjectURL).toHaveBeenCalledWith("blob:fake-url");
});
```

It's often simpler to move the CSV building into a function and unit test that, then check the real download once in Playwright.

### 386: How do you test features that need browser permissions in Playwright?

Grant them on the context and set any fake values:

```ts
test.use({
  permissions: ["geolocation", "notifications"],
  geolocation: { latitude: 48.8566, longitude: 2.3522 },
});

test("shows stores near the user", async ({ page }) => {
  await page.goto("/stores");
  await page.getByRole("button", { name: "Use my location" }).click();
  await expect(page.getByText("Paris")).toBeVisible();
});

test("handles a denied permission", async ({ browser }) => {
  const context = await browser.newContext({ permissions: [] });
  const page = await context.newPage();
  await page.goto("/stores");
  await page.getByRole("button", { name: "Use my location" }).click();
  await expect(page.getByText(/enter your city/i)).toBeVisible();
  await context.close();
});
```

Always test the denied case too, since many users will say no. Support for some permissions differs by browser.

### 387: How do you test video and audio components?

jsdom doesn't implement media playback. `play()`, `pause()` and `load()` aren't implemented. Mock them for unit tests:

```ts
beforeEach(() => {
  vi.spyOn(HTMLMediaElement.prototype, "play").mockResolvedValue(undefined);
  vi.spyOn(HTMLMediaElement.prototype, "pause").mockImplementation(() => {});
});

test("plays the video when the play button is clicked", async () => {
  const user = userEvent.setup();
  render(<VideoPlayer src="/intro.mp4" />);

  await user.click(screen.getByRole("button", { name: "Play" }));
  expect(HTMLMediaElement.prototype.play).toHaveBeenCalled();
  expect(screen.getByRole("button", { name: "Pause" })).toBeInTheDocument();
});
```

To simulate playback events, fire them: `fireEvent(video, new Event("ended"))`. Real playback, autoplay rules and codecs can only be checked in real browsers, and they differ a lot between Chromium and WebKit.

### 388: How do you test error tracking and global error handling?

- **Wrap the SDK**: call your own `reportError(error, context)` instead of the Sentry (or similar) SDK directly. In tests, mock that module and check it gets called with the right data when something fails.
- **Error boundaries**: test that the boundary reports the error and shows the fallback.
- **Global handlers**: test `window.onerror` / `unhandledrejection` handlers by dispatching the events: `window.dispatchEvent(new PromiseRejectionEvent("unhandledrejection", { promise, reason }))` (check jsdom support, or test in a browser).
- **E2E**: block the real error tracking endpoint with `page.route` and check that a request was sent when you trigger an error, without filling your real dashboard with test errors.

### 389: How do you make tests fail on unexpected console errors?

Add a check in the setup file:

```ts
// setupTests.ts
let consoleErrors: unknown[][] = [];

beforeEach(() => {
  consoleErrors = [];
  vi.spyOn(console, "error").mockImplementation((...args) => {
    consoleErrors.push(args);
  });
});

afterEach(() => {
  if (consoleErrors.length > 0) {
    const messages = consoleErrors.map((args) => args.join(" ")).join("\n");
    throw new Error(`Unexpected console.error calls:\n${messages}`);
  }
});
```

This catches React warnings (act warnings, missing keys, invalid DOM nesting) that are easy to ignore in a long output. Tests that expect an error can clear the list or mock `console.error` themselves. There are also ready-made packages for this, like `jest-fail-on-console` and `vitest-fail-on-console`.

### 390: What happens with unhandled promise rejections in tests?

Vitest catches unhandled rejections and errors that happen during the run. It reports them and marks the run as failed, even if all tests passed, and tells you which test was running when it happened. That's useful, because it usually points at a floating promise.

Jest's behavior depends on the version and Node. Some unhandled rejections are only printed or lost if they happen after the test file finished.

Either way, treat them as bugs: find the promise that nobody awaited, or the async work that outlived its test, and fix it. Don't hide them with `dangerouslyIgnoreUnhandledErrors` (Vitest) unless you really have no other option.

### 391: How do you investigate a test that hangs until it times out?

Common causes:

- **A `findBy` or `waitFor` waiting for something that never appears**. Look at the DOM in the error output. Often the request wasn't mocked, or an error happened silently.
- **A promise that never resolves**: a mock without a return value (`vi.fn()` returns `undefined`, not a promise), or an MSW handler that doesn't return a response.
- **Fake timers**: code waiting for a timer that's never advanced, including `user-event` without `advanceTimers`.
- **An infinite loop**: a `useEffect` that sets state on every render.

Debug by adding `screen.debug()` before the wait, logging inside handlers, turning on `onUnhandledRequest: "error"` in MSW, and running the test alone with a short timeout so you get feedback quickly.

### 392: How do you test code that uses random values like crypto.randomUUID or Math.random?

Make the randomness controllable:

```ts
test("assigns an id to a new todo", async () => {
  vi.spyOn(crypto, "randomUUID").mockReturnValue("11111111-1111-1111-1111-111111111111");

  const user = userEvent.setup();
  render(<Todos />);
  await user.type(screen.getByRole("textbox"), "Buy milk{Enter}");

  expect(screen.getByRole("listitem")).toHaveAttribute(
    "data-id",
    "11111111-1111-1111-1111-111111111111"
  );
});

test("picks a random tip", () => {
  vi.spyOn(Math, "random").mockReturnValue(0.5);
  render(<TipOfTheDay tips={["a", "b", "c", "d"]} />);
  expect(screen.getByText("c")).toBeInTheDocument();
});
```

A cleaner option is to pass a random or ID generator into the code (as a parameter or through context), so tests can give a fixed one without spying on globals.

### 393: Why can useId or generated IDs break snapshot tests?

`useId` creates IDs based on the component's position in the tree, like `«r0»` (the exact format changed between React versions). They're stable between server and client, but they change when the tree shape changes or when React is upgraded. If you snapshot HTML that contains them, the snapshots break for reasons that have nothing to do with your change. Libraries that generate their own IDs cause the same issue.

Fixes:

- Don't snapshot large HTML trees. Assert on behavior instead.
- If you must, use a snapshot serializer that replaces IDs with stable placeholders.
- Never query by these IDs in tests. Query by role and label. RTL follows `aria-labelledby` and `htmlFor` for you.

### 394: A test passes locally but fails in CI. How do you debug it?

Look at what's different between the two:

- **Time zone, locale and time**: CI often runs in UTC with `en-US`.
- **Speed**: CI machines are slower and run more workers, so timing issues and short timeouts show up.
- **Test order and parallelism**: CI may run files in a different order or with more workers. Run locally with the same settings and with random order.
- **Environment variables and config**: missing env vars, a different `NODE_ENV`, a different `.env` file.
- **Versions**: different Node version, or a lockfile not being respected (use `npm ci`).
- **OS differences**: file path case sensitivity (Linux), fonts (for screenshots), line endings.
- **Leftover local state**: your machine has a cache, a built file or a database record CI doesn't.

For e2e, download the trace and report. For unit tests, reproduce with `CI=true` and the same worker count.

### 395: Your e2e suite takes 40 minutes. How do you make it faster?

1. **Measure first**: find the slowest tests and the slowest steps in them.
2. **Stop logging in through the UI**: use `storageState` and setup projects.
3. **Create data through the API**, not through the UI.
4. **Remove fixed waits** and long timeouts that hide slow polling.
5. **Run in parallel**: `fullyParallel: true`, more workers, sharding across machines.
6. **Move tests down**: many e2e tests check things an integration test could check in milliseconds (validation messages, empty states). Keep e2e for real end-to-end flows.
7. **Split the suite**: a fast smoke set on every pull request, the full suite on merge or nightly.
8. **Reduce browser matrix** on pull requests: Chromium only, with all browsers nightly.
9. **Make the app faster to start** in CI: prebuilt production build instead of a dev server.

### 396: Your team has hundreds of large snapshot tests that everybody just updates. What do you do?

Those snapshots aren't catching bugs anymore, they're only slowing people down.

1. Find the snapshots that are updated most often (git history), and the biggest ones.
2. For each, ask what it was supposed to protect. Replace it with a few clear assertions about that behavior.
3. Delete the ones that don't protect anything meaningful.
4. Keep snapshots only for small, stable output (formatted strings, serialized configs, error messages), and prefer inline snapshots.
5. Add a lint rule limiting snapshot size (`no-large-snapshots` in the Jest/Vitest ESLint plugins).
6. Make it a review rule that snapshot diffs have to be read, not just accepted.

For checking how things look, use visual regression tests instead of HTML snapshots.

### 397: You join a project with a large React app and no tests. Where do you start?

1. **Set up the tools** and CI first (Vitest, RTL, MSW, Playwright), with one example test of each kind, so writing tests is easy.
2. **Add a few e2e smoke tests** for the most important flows (login, the main feature, checkout). They give the most safety for the least effort when you know nothing about the code.
3. **Add tests where you change code**: every bug fix gets a test, every new feature gets tests. Don't try to backfill everything at once.
4. **Test risky business logic** next: pricing, permissions, data transformations.
5. **Refactor carefully**: before changing a messy component, write a characterization test that captures its current behavior.
6. **Track progress** loosely (coverage trend, number of flows covered), but don't set a big coverage target on day one.

### 398: A component is very hard to test. What does that tell you and how do you fix it?

Usually it means the component does too much, or is tightly coupled to things you can't control. Typical signs: you need to mock ten modules, the setup is longer than the test, or you need to reach into internals.

Refactoring ideas:

- **Split logic from UI**: move calculations into pure functions or a custom hook.
- **Split container and presentation**: a component that fetches data and a component that just renders props.
- **Inject dependencies**: pass the API client, clock or feature flags through props or context instead of importing singletons.
- **Avoid module-level side effects**: code that runs when a file is imported is hard to control in tests.
- **Use standard patterns**: data-fetching libraries and form libraries are easier to test (through MSW and the UI) than hand-made effect chains.

"Hard to test" is often the first warning that code is hard to change too.

### 399: All tests pass, but the app is broken in production. What went wrong and how do you prevent it?

Common causes:

- **Too much mocking**: modules mocked so heavily that the tests only tested the mocks. The real API, library or browser behaved differently.
- **Mocks out of date**: the backend changed the response format and the MSW handlers didn't.
- **Testing implementation, not behavior**: tests checked that functions were called, not that the user saw the right result.
- **Missing levels**: no e2e tests, so routing, config, build issues or environment variables were never tested together.
- **Environment differences**: production-only config, CDN, CSP headers, feature flags.

Prevention: mock only at the edges, keep mocks synced with the API (types or contract tests), add a few e2e tests against a real backend, run smoke tests after every deploy, and write a test for each production bug once you find it.

### 400: How would you test a checkout flow end to end?

```ts
test("guest can buy a product with a card", async ({ page, request }) => {
  const product = await (
    await request.post("/api/test/products", {
      data: { name: `Test product ${Date.now()}`, price: 2500, stock: 5 },
    })
  ).json();

  await page.goto(`/products/${product.id}`);
  await page.getByRole("button", { name: "Add to cart" }).click();
  await page.getByRole("link", { name: /cart \(1\)/i }).click();
  await expect(page.getByText("$25.00")).toBeVisible();
  await page.getByRole("button", { name: "Checkout" }).click();

  await test.step("shipping", async () => {
    await page.getByLabel("Email").fill("guest@test.com");
    await page.getByLabel("Address").fill("Main Street 1");
    await page.getByRole("button", { name: "Continue to payment" }).click();
  });

  await test.step("payment", async () => {
    const card = page.frameLocator("iframe[title*='card']");
    await card.getByPlaceholder("Card number").fill("4242424242424242");
    await card.getByPlaceholder("MM / YY").fill("12/34");
    await card.getByPlaceholder("CVC").fill("123");
    await page.getByRole("button", { name: "Pay $25.00" }).click();
  });

  await expect(
    page.getByRole("heading", { name: "Thank you for your order" }),
  ).toBeVisible();
});
```

Besides the happy path, add tests for a declined card, an out-of-stock product and a discount code. Use the payment provider's test mode, create products through a test API, and give each run unique data.

### 401: How would you test a search autocomplete component?

Cover these cases, mostly with RTL and MSW:

- **Debounce**: typing quickly sends one request, not one per letter (fake timers or a request counter in the handler).
- **Results**: suggestions show up in a `listbox` with `option` roles, and the matching part may be highlighted.
- **Keyboard**: arrow keys move the active option (`aria-activedescendant` or `aria-selected`), Enter selects it, Escape closes the list.
- **Selection**: choosing an option fills the input and calls `onSelect`.
- **Edge cases**: empty results message, minimum characters before searching, error from the API, clearing the input closes the list.
- **Race conditions**: an old slow response must not replace newer results (see question 339).

```tsx
test("selects a suggestion with the keyboard", async () => {
  const user = userEvent.setup();
  const onSelect = vi.fn();
  render(<CityAutocomplete onSelect={onSelect} />);

  await user.type(screen.getByRole("combobox", { name: "City" }), "ber");
  await screen.findByRole("option", { name: "Berlin" });

  await user.keyboard("{ArrowDown}{Enter}");

  expect(onSelect).toHaveBeenCalledWith(
    expect.objectContaining({ name: "Berlin" }),
  );
  expect(screen.queryByRole("listbox")).not.toBeInTheDocument();
});
```

### 402: How would you test a multi-step form wizard?

- **Integration tests** for each step's validation: you can't go to the next step with invalid data, errors show on the right fields.
- **Navigation**: Back keeps the entered data, step indicators show the current step (`aria-current="step"`), and you can't skip ahead to a later step by URL if that's not allowed.
- **Final submit**: one test that fills all steps and checks the full payload sent to the API (MSW captures the body).
- **Persistence**: if the wizard saves progress (localStorage or server drafts), test reloading in the middle.
- **One e2e test** for the full happy path against the real backend.

A helper per step (`fillPersonalDetails(user)`, `fillAddress(user)`) keeps the tests readable and avoids repeating the same typing in every test.

### 403: How would you test UI that depends on user roles and permissions?

Use a table of roles and expected results with `test.each`:

```tsx
const cases = [
  { role: "viewer", canEdit: false, canDelete: false },
  { role: "editor", canEdit: true, canDelete: false },
  { role: "admin", canEdit: true, canDelete: true },
] as const;

test.each(cases)(
  "$role: edit=$canEdit, delete=$canDelete",
  ({ role, canEdit, canDelete }) => {
    renderApp(<ProjectPage />, { currentUser: buildUser({ role }) });

    expect(!!screen.queryByRole("button", { name: "Edit" })).toBe(canEdit);
    expect(!!screen.queryByRole("button", { name: "Delete" })).toBe(canDelete);
  },
);
```

That covers the UI. The real security is on the server, so also have API or e2e tests that check a viewer gets a 403 when calling the delete endpoint directly. A hidden button is not a permission check.

### 404: How would you test a dashboard with charts and filters?

- **Unit tests** for data transformation: grouping by day, totals, percentage changes, empty and partial data.
- **Integration tests** for filters: changing the date range or segment sends the right query params (check them in the MSW handler) and updates the summary numbers. Test loading and error states per widget, so one failing widget doesn't break the whole page.
- **Charts**: check the accessible summary or the data table fallback in jsdom, and the visual result with screenshot tests in a real browser using fixed data.
- **URL state**: filters saved in the URL survive a reload and can be shared.
- **E2E**: one test that loads the dashboard with seeded data and changes a filter.

### 405: How would you test a file upload with a progress bar?

`fetch` doesn't report upload progress, so these components often use `XMLHttpRequest` or a library. In unit tests, put the upload behind a function you can mock and control:

```tsx
test("shows progress and then success", async () => {
  let reportProgress!: (percent: number) => void;
  let finish!: () => void;
  vi.mocked(uploadFile).mockImplementation((_file, onProgress) => {
    reportProgress = onProgress;
    return new Promise<void>((resolve) => (finish = resolve));
  });

  const user = userEvent.setup();
  render(<Uploader />);
  await user.upload(
    screen.getByLabelText("Upload"),
    new File(["x"], "a.pdf", { type: "application/pdf" }),
  );

  act(() => reportProgress(40));
  expect(screen.getByRole("progressbar")).toHaveAttribute(
    "aria-valuenow",
    "40",
  );

  await act(async () => finish());
  expect(screen.getByText("a.pdf uploaded")).toBeInTheDocument();
});
```

Also test file size or type rejected before upload, an upload error with a retry button, and cancelling. Test the real upload once in Playwright with `setInputFiles`.

### 406: How would you test a table with server-side sorting and pagination?

The important part is that the UI sends the right request and shows what comes back. In the MSW handler, read the query params and return data based on them:

```tsx
server.use(
  http.get("/api/users", ({ request }) => {
    const url = new URL(request.url);
    const page = Number(url.searchParams.get("page") ?? 1);
    const sort = url.searchParams.get("sort");
    return HttpResponse.json({
      items: [{ id: page, name: `${sort ?? "default"} page ${page}` }],
      total: 50,
    });
  }),
);
```

Then test: clicking a column header requests `sort=name` and then `sort=-name`, "Next" requests `page=2`, the "Next" button is disabled on the last page, changing the sort goes back to page 1, and the page and sort are kept in the URL if the app does that. You don't need to implement real sorting in the mock. Just echo the params back so you can see they were sent.

### 407: How would you test toast notifications that disappear automatically?

```tsx
test("shows a toast and hides it after 5 seconds", async () => {
  vi.useFakeTimers();
  const user = userEvent.setup({ advanceTimers: vi.advanceTimersByTime });
  render(<App />);

  await user.click(screen.getByRole("button", { name: "Save" }));
  expect(await screen.findByRole("status")).toHaveTextContent("Saved");

  act(() => vi.advanceTimersByTime(5000));
  expect(screen.queryByRole("status")).not.toBeInTheDocument();
  vi.useRealTimers();
});
```

Also test that hovering or focusing the toast pauses the timer (if it does), that the close button works, and that error toasts use `role="alert"` while normal ones use `role="status"`, so screen readers announce them correctly.

### 408: How would you test a component that uses a third-party map SDK?

The map SDK (Google Maps, Mapbox, Leaflet) needs a real browser, WebGL, network access and API keys, so don't load it in jsdom tests.

- **Wrap the SDK** in your own `Map` component with a simple prop API (`markers`, `onMarkerClick`, `center`).
- **Mock that wrapper** in tests of pages that use the map. The mock renders the markers as buttons, so you can test "click a marker, see the details panel".
- **Test the wrapper itself** in a real browser, with the SDK's test or development mode, or with a small number of e2e tests.
- **Test logic** like clustering, bounds calculation or distance sorting as plain functions.

### 409: How would you test a countdown timer?

```tsx
beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(new Date("2026-06-01T12:00:00Z"));
});
afterEach(() => vi.useRealTimers());

test("counts down and shows a message at zero", () => {
  render(<Countdown until={new Date("2026-06-01T12:00:10Z")} />);
  expect(screen.getByText("00:10")).toBeInTheDocument();

  act(() => vi.advanceTimersByTime(3000));
  expect(screen.getByText("00:07")).toBeInTheDocument();

  act(() => vi.advanceTimersByTime(7000));
  expect(screen.getByText("Offer ended")).toBeInTheDocument();
});
```

Fake timers also move the faked `Date`, so a countdown that calculates the remaining time from the clock stays correct. Also test that the interval is cleared on unmount and when it reaches zero, and what happens when the tab was in the background (time jumped forward a lot at once).

### 410: How would you test an undo and redo feature?

The logic is the important part, so test the history logic (usually a reducer or a store) directly with sequences of actions:

```ts
test("undo and redo restore previous states", () => {
  let state = createHistory({ text: "" });
  state = apply(state, { type: "type", text: "a" });
  state = apply(state, { type: "type", text: "ab" });

  state = undo(state);
  expect(state.present.text).toBe("a");

  state = redo(state);
  expect(state.present.text).toBe("ab");

  state = undo(state);
  state = apply(state, { type: "type", text: "ax" });
  expect(canRedo(state)).toBe(false); // a new change clears the redo stack
});
```

Property-based tests fit well too, for example "applying N actions and then N undos always gives back the start state". Then add a few component tests for the buttons and keyboard shortcuts (Ctrl+Z, Ctrl+Shift+Z), including disabled states when there's nothing to undo.

### 411: How do you make React components easier to test with dependency injection?

Instead of importing a singleton (an API client, analytics, a clock) directly inside a component, provide it through context or props:

```tsx
const ServicesContext = createContext<Services>(defaultServices);

export function useServices() {
  return useContext(ServicesContext);
}

function OrderButton() {
  const { api, analytics } = useServices();
  // ...
}

// in tests
render(
  <ServicesContext.Provider
    value={{ api: fakeApi, analytics: { track: vi.fn() } }}
  >
    <OrderButton />
  </ServicesContext.Provider>,
);
```

Tests don't need `vi.mock` and its hoisting rules, and different tests can easily use different fakes. Don't overdo it, though. For HTTP, MSW usually makes this unnecessary, and injecting everything makes the app code harder to read.

### 412: Should e2e tests use a real backend or a mocked one?

**Real backend (full stack)**:

- tests the real integration, including the database, auth and API contracts
- slower, needs test data management, can fail because of backend problems

**Mocked backend (`page.route`, MSW, HAR)**:

- fast, stable, easy to create edge cases
- doesn't catch API changes or backend bugs, so it's closer to a front-end integration test in a real browser

Many teams do both: a mocked suite for lots of UI scenarios in a real browser, and a smaller full-stack suite for the critical flows. Just be clear about which is which, and don't call the mocked suite "e2e" in a way that gives false confidence.

### 413: How do you give each e2e run its own backend environment?

- **Docker Compose in CI**: start the API, database and other services in the CI job, run migrations and seed data, then run Playwright against them.
- **Testcontainers**: start containers from code in a global setup, which works the same locally and in CI.
- **Preview environments**: the platform creates a full stack per pull request (frontend and backend), and tests run against its URL.
- **Database branching**: some hosted databases can create a copy (branch) of the database per pull request.

Each run having its own environment removes a big source of flakiness: tests from different branches fighting over the same shared staging data.

### 414: How do you reset the database between e2e tests?

Options, from most to least isolated:

- **Fresh database per run**: migrate and seed at the start of the run (global setup). Simple, but data from earlier tests in the run stays.
- **Unique data per test**: each test creates its own records and never touches others. This works well with parallel workers and is the most common approach.
- **Transactions**: wrap each test in a transaction that's rolled back. Usually doesn't work for e2e, because the app server uses its own connections.
- **Reset endpoint**: a test-only API that truncates tables and reseeds. Easy, but forces tests to run one at a time, because a reset in one test breaks others running in parallel.
- **Snapshot restore**: restore a database snapshot or template database, which is fast in Postgres with `CREATE DATABASE ... TEMPLATE`.

Combining "fresh database per run" with "unique data per test" is usually the best mix of speed and isolation.

### 415: What are global setup and teardown in Playwright and Vitest?

They run once for the whole test run, not per test file.

**Playwright**: the recommended way is a setup project with `dependencies` (it shows up in the report and trace and can use fixtures). There's also `globalSetup` / `globalTeardown` in the config, which are plain functions:

```ts
// playwright.config.ts
export default defineConfig({
  globalSetup: "./e2e/global-setup.ts",
  globalTeardown: "./e2e/global-teardown.ts",
});
```

**Vitest**: `test.globalSetup` points to a file that exports `setup` and `teardown` (or a setup function that returns a teardown). It runs in the main process, so you can't share variables with tests directly. Use `provide` in the setup and `inject` in tests to pass serializable values like a server URL.

Use global setup for things like starting a database container, running migrations or creating a shared auth state.

### 416: How do you run the same Playwright suite against different environments?

Read the target from environment variables in the config:

```ts
const env = process.env.TEST_ENV ?? "local";

const baseURLs: Record<string, string> = {
  local: "http://localhost:3000",
  staging: "https://staging.example.com",
  production: "https://www.example.com",
};

export default defineConfig({
  use: { baseURL: process.env.BASE_URL ?? baseURLs[env] },
  webServer:
    env === "local"
      ? { command: "npm run start", url: baseURLs.local }
      : undefined,
  grep: env === "production" ? /@smoke/ : undefined,
});
```

Only start the local web server for local runs, and only run safe `@smoke` tests against production. Keep credentials per environment in CI secrets.

### 417: How should you handle secrets in e2e tests?

- Never commit passwords, API keys or tokens to the repo. Read them from environment variables, filled from CI secrets (and a local `.env` that's in `.gitignore`).
- Use dedicated **test accounts** with minimal permissions, not real users or admins.
- Don't log secrets: in Cypress use `{ log: false }` on `type`. In Playwright, remember that traces, videos and screenshots can capture typed passwords and tokens, so be careful where reports are uploaded and who can see them.
- The saved auth state files (`playwright/.auth`) contain session cookies. Keep them out of git and out of public artifacts.
- Rotate test account passwords from time to time.

### 418: What is the difference between page.route and context.route, and which route wins when several match?

`page.route` only affects one page. `context.route` affects every page in the context, including popups and new tabs opened later. If your test opens a new tab, mocks set on the original page won't apply to it, so use `context.route` for mocks that should apply everywhere.

When several routes match a request, the one registered **last** runs first. A handler can pass the request on to the next matching handler with `route.fallback()`, or send it to the network with `route.continue()`:

```ts
await context.route("**/api/**", (route) => route.continue()); // base: pass everything through
await page.route("**/api/user", (route) =>
  route.fulfill({ json: { name: "Mock" } }),
); // more specific, registered later
```

Page routes run before context routes. You can remove routes with `page.unroute()` or `page.unrouteAll()`.

### 419: How do you control time in Playwright tests?

Use the Clock API:

```ts
test("shows the session expiry warning", async ({ page }) => {
  await page.clock.install({ time: new Date("2026-05-01T09:00:00") });
  await page.goto("/dashboard");

  await page.clock.fastForward("25:00"); // 25 minutes
  await expect(
    page.getByRole("alertdialog", { name: /session expires soon/i }),
  ).toBeVisible();
});

test("shows the date in the header", async ({ page }) => {
  await page.clock.setFixedTime(new Date("2026-12-24T10:00:00"));
  await page.goto("/");
  await expect(page.getByText("December 24")).toBeVisible();
});
```

`install` fakes timers and `Date` in the page. `fastForward` jumps ahead and fires due timers once, `runFor` advances time and fires every timer along the way, and `pauseAt` stops time at a given moment. This only affects the browser, not your backend's clock.

### 420: How would you test session expiry and token refresh?

At the unit or integration level, with MSW:

- First request returns 401, the refresh endpoint returns a new token, the original request is retried and succeeds. The user sees the data and nothing else.
- Several requests fail with 401 at the same time: only **one** refresh request is sent (count calls in the refresh handler).
- The refresh itself fails: the user is sent to the login page with a message, and cached private data is cleared.

```ts
let refreshCalls = 0;
server.use(
  http.get("/api/me", ({ request }) =>
    request.headers.get("Authorization") === "Bearer new-token"
      ? HttpResponse.json({ name: "Anna" })
      : new HttpResponse(null, { status: 401 }),
  ),
  http.post("/api/refresh", () => {
    refreshCalls++;
    return HttpResponse.json({ accessToken: "new-token" });
  }),
);
```

At the e2e level, use `page.clock` to jump past the token lifetime, or set an expired cookie, and check the user stays logged in (or is correctly logged out).

### 421: How do you test what happens when a lazy-loaded chunk fails to load?

After a deploy, users with an old tab open can request JavaScript chunks that no longer exist. The app should show a message or reload, not crash.

In Playwright, block the chunk request:

```ts
test("shows a reload prompt when a chunk fails to load", async ({ page }) => {
  await page.goto("/");
  await page.route("**/assets/Settings-*.js", (route) => route.abort());

  await page.getByRole("link", { name: "Settings" }).click();

  await expect(page.getByText(/a new version is available/i)).toBeVisible();
  await expect(page.getByRole("button", { name: "Reload" })).toBeVisible();
});
```

In a unit test, you can mock the lazy import to reject and check that the error boundary around the lazy route shows the right fallback. Run the e2e version against a production build, since chunk names differ in dev.

### 422: Can AI tools write and fix your e2e tests?

They can help. Playwright now ships agents (planner, generator and healer) and an MCP server, so AI coding assistants can explore the app in a real browser, write tests with good locators and suggest fixes for failing tests. Codegen-style generation is much better than it used to be.

But you still need to review everything:

- Generated tests often check too little, like "the page loaded", instead of the real outcome.
- A "healer" can make a failing test pass by changing the assertion, even when the failure was a real bug.
- Generated tests can repeat the same setup instead of using fixtures and page objects.

Treat AI-generated tests like code from a new team member: useful, but it goes through review, and someone has to understand what each test proves.

### 423: What are common problems with unit tests written by AI assistants?

- **Testing the implementation**: mocking every import and asserting that internal functions were called, which breaks on any refactor.
- **Tautological tests**: the expected value is calculated with the same logic as the code under test, so the test can't fail.
- **Copying bugs**: the AI writes tests that match what the code currently does, including its bugs, instead of what it should do.
- **Wrong or outdated APIs**: `fireEvent` instead of `user-event`, `react-test-renderer`, Enzyme patterns, missing `await`, wrong imports.
- **Too many shallow tests**: lots of "renders without crashing" tests that add coverage but no confidence.
- **Unneeded `act` and `waitFor`** sprinkled everywhere.

Giving the assistant your testing conventions (custom render, MSW setup, examples of good tests) and reviewing every test for "would this fail if the feature broke?" helps a lot.

### 424: How do you track test health over time?

- **Store results**: JUnit or JSON reports from every CI run, sent to a dashboard (CI built-in test analytics, Currents, Datadog, Allure, or a simple database).
- **Track flaky tests**: tests that pass on retry, and how often. Rank them by how many runs they affected.
- **Track duration**: slowest tests and how the total time changes over weeks.
- **Track failures by cause**: real bugs vs flakiness vs environment problems.
- **Make it visible**: a weekly summary in the team channel, and owners for the worst offenders.

Without data, people only remember "the tests are flaky" and lose trust in the whole suite. With data, you can fix the five tests causing most of the pain.

### 425: In what order should checks run in a CI pipeline?

Fast and cheap first, slow and expensive last, so developers get feedback quickly:

1. Install dependencies (with caching).
2. Lint, format check and type check (can run in parallel).
3. Unit and integration tests (sharded if the suite is large), with coverage.
4. Build the app.
5. E2E tests against the built app (sharded), visual and a11y checks.
6. After merge or deploy: smoke tests against the deployed environment.

Running steps 2 and 3 in parallel jobs instead of one after another is usually worth it. If the build is needed for e2e, build once and pass it as an artifact instead of building again in every shard.

### 426: How do you run e2e tests against pull request preview deployments?

Platforms like Vercel and Netlify create a preview URL for each pull request. The CI workflow waits for the deployment to be ready, then runs Playwright with that URL as `baseURL`:

```yaml
- name: Run e2e against preview
  run: npx playwright test
  env:
    BASE_URL: ${{ steps.wait-for-preview.outputs.url }}
```

Things to handle: preview deployments may be protected by auth (use a bypass token that the platform provides), they may point at a shared staging backend (watch out for data conflicts), and the wait step must time out properly if the deploy fails.

### 427: How do you decide which browsers to run e2e tests on?

Look at your analytics: which browsers and devices your users actually use, and how important they are to the business.

A common setup:

- **Every pull request**: Chromium only, to keep it fast.
- **Nightly or before release**: Chromium, Firefox and WebKit, plus mobile viewports.
- **Visual tests**: the main browser only, because every extra browser doubles the baselines.

WebKit is worth including at least nightly if you have many iPhone users, because Safari bugs are common and every browser on iOS uses WebKit. Keep in mind that Playwright's WebKit build is close to Safari but not identical, so real-device testing services are still useful for important releases.

### 428: Is mobile emulation in Playwright enough to test mobile users?

It covers a lot: viewport size, device pixel ratio, user agent, touch events (`hasTouch`) and `isMobile` behavior. That's enough to catch most responsive layout bugs and touch-only UI issues.

It doesn't cover: real mobile Safari or Chrome quirks (on-screen keyboard pushing the layout, `100vh` and safe areas, iOS date pickers), real device performance and memory, real network conditions and gestures like pinch zoom.

For those, use real devices manually or through cloud device services for key flows before big releases. Emulation is for everyday regression testing, and real devices are for the last check.

### 429: How do you test web components used inside React?

React 19 has full support for custom elements: it sets properties instead of attributes when the element defines them, and supports custom events with `on` + event name props.

In tests:

- jsdom supports custom elements (`customElements.define`), but make sure the web component's code is loaded in the test (import the module that defines it).
- Shadow DOM is a problem for Testing Library queries, because `screen` doesn't look inside shadow roots. You may need helper libraries (like `shadow-dom-testing-library`) or query `element.shadowRoot` directly.
- For custom events, dispatch them on the element and check your React handler ran: `fireEvent(el, new CustomEvent("value-change", { detail: 5 }))`.

For anything layout- or focus-related inside shadow DOM, Playwright handles it well: its locators pierce open shadow roots by default.

### 430: How can state machines help with testing?

If a complex UI flow (checkout, onboarding, media player) is modeled as a state machine, for example with XState, you can:

- **Unit test the machine** without React: send events and check the next state and context. This is fast and covers all the transitions.
- **Generate test paths**: model-based testing tools can walk through the machine's graph and give you every path from the start state to each state. You then run each path against the real UI, which covers combinations people wouldn't think of writing by hand.
- **Visualize** the machine to spot missing transitions (like "what happens if the user cancels during payment?").

```ts
import { createActor } from "xstate";

test("goes to error state when payment fails", () => {
  const actor = createActor(checkoutMachine).start();
  actor.send({ type: "SUBMIT_SHIPPING", address: validAddress });
  actor.send({ type: "PAYMENT_FAILED", reason: "card_declined" });

  expect(actor.getSnapshot().value).toBe("paymentError");
  expect(actor.getSnapshot().context.error).toBe("card_declined");
});
```

### 431: How do you test that a TanStack Query mutation updates or invalidates the right data?

Render the list and the mutation UI together, with a real `QueryClient` and MSW handlers that keep simple in-memory state:

```tsx
test("adding a todo refreshes the list", async () => {
  const todos = [{ id: 1, title: "Existing" }];
  server.use(
    http.get("/api/todos", () => HttpResponse.json(todos)),
    http.post("/api/todos", async ({ request }) => {
      const body = (await request.json()) as { title: string };
      const todo = { id: todos.length + 1, title: body.title };
      todos.push(todo);
      return HttpResponse.json(todo, { status: 201 });
    }),
  );

  const user = userEvent.setup();
  render(<TodoPage />, { wrapper: createWrapper() });
  await screen.findByText("Existing");

  await user.type(screen.getByLabelText("New todo"), "Buy milk");
  await user.click(screen.getByRole("button", { name: "Add" }));

  expect(await screen.findByText("Buy milk")).toBeInTheDocument();
});
```

If invalidation is wrong (wrong query key), the list won't refetch and the test fails. For optimistic updates, delay the POST response and check the item appears before it resolves, and test rollback with an error response.

### 432: For an Apollo Client app, should you use MockedProvider or MSW?

**MockedProvider** (from Apollo) lets you list exact queries, variables and results. It's built in, but:

- the query and variables in the mock must match exactly, or you get "No more mocked responses" errors
- it ties tests to Apollo, so switching clients means rewriting tests
- it skips the HTTP layer, so things like headers and links (auth, error links) aren't tested

**MSW with `graphql.query` / `graphql.mutation`** mocks at the network level. The real Apollo Client, cache and links run, handlers match by operation name, and the same handlers work in Storybook and the browser.

MSW is usually the better default. MockedProvider is fine for small, isolated component tests if the team already uses it.

### 433: How do you test inputs from third-party libraries like masked inputs or custom number fields?

These inputs often handle keystrokes themselves (to format phone numbers, cards, currencies), so `user.type` may behave differently from a plain input.

- Use `user.type`, not `fireEvent.change`, so the library gets real key events. Then check the **displayed** value with `toHaveDisplayValue` and the **submitted** value through your `onSubmit` mock, since they're often different ("(555) 123-4567" vs "5551234567").
- Test the cases users actually hit: pasting (`user.paste`), deleting in the middle, typing invalid characters.
- If the library uses selection APIs that jsdom doesn't fully support, cover the typing in a real browser test and keep jsdom tests focused on the value your form receives.

### 434: How can you split tests across CI machines more evenly?

Simple sharding splits by file count, so one shard can get all the slow files and take much longer than the others.

Better options:

- **Playwright with `fullyParallel: true`** splits by individual tests, not files.
- **Timing-based splitting**: save how long each file took in previous runs, then assign files to shards so each shard gets about the same total time. Many CI providers and some third-party tools can do this.
- **Split big slow files** into smaller ones.
- **Separate slow tests** into their own job with more machines.

The goal is that all shards finish at about the same time, because the pipeline is only as fast as the slowest shard.

### 435: How do you keep a test suite maintainable over several years?

- **Shared helpers**: a custom render, factories and page objects, so a change in providers or a page is fixed in one place.
- **Behavior-focused tests**: they survive refactors and library upgrades.
- **Clear conventions**, written down: where tests go, what level to test at, how to mock.
- **Fix or remove flaky tests quickly**: a flaky test that stays for months teaches everyone to ignore failures.
- **Delete tests** for removed features and duplicated coverage.
- **Upgrade tools regularly**: small upgrades are easy, jumping three major versions is painful.
- **Treat test code like production code**: reviewed, refactored and readable.

### 436: When should you delete a test?

- The feature it tests was removed.
- It's a duplicate: another test already checks the same behavior at the same or better level.
- It only tests implementation details and keeps breaking on refactors without ever catching a real bug.
- It's been flaky for a long time, nobody can fix it, and the behavior is covered elsewhere (or replace it with a better test).
- It tests a third-party library rather than your code.

Deleting tests feels wrong to many developers, but every test has a cost: run time, maintenance and noise. A test that doesn't give confidence isn't worth that cost.

### 437: How would you convince a team to invest more in testing?

Use their own problems, not general arguments:

- **Show the cost of bugs**: list recent production incidents and how many would have been caught by a simple test. Show the time spent on hotfixes and manual regression testing before releases.
- **Start small**: add tests to the area that breaks most often, and show the result after a few weeks.
- **Make it easy**: set up the tools, a custom render, MSW and examples, so writing the first test takes minutes, not a day.
- **Make it fast**: a slow, flaky suite turns people against testing. Fast, reliable tests win people over.
- **Make it part of the process**: tests required for bug fixes, test examples in pull request reviews.
- **Lead by example**: write good tests yourself in your own pull requests.

### 438: How do you test theming and dark mode?

- **Logic**: test the theme provider. It reads the saved preference, falls back to the system setting (`matchMedia("(prefers-color-scheme: dark)")`, mocked in jsdom), and toggling saves the new value and updates the `data-theme` attribute or class on the root.
- **Look**: use visual regression tests in a real browser in both themes. In Playwright, `colorScheme: "dark"` emulates the system setting.
- **Contrast**: run axe in a real browser for both themes, because dark themes often have contrast problems.
- **No flash**: an e2e test that loads the page with dark mode saved and checks the first screenshot or the root attribute before hydration, to catch a "flash of light theme".

### 439: How do you test page titles and meta tags?

In React 19 you can render `<title>` and `<meta>` inside components, and React moves them into `<head>`. In a jsdom test you can check `document.title`:

```tsx
test("sets the page title", () => {
  render(<ProductPage product={{ name: "Laptop" }} />);
  expect(document.title).toBe("Laptop | My Shop");
});
```

For SEO, what matters is the HTML the server sends, so also check it with Playwright's `request` fixture or `page`:

```ts
test("product page has SEO tags in the server HTML", async ({ request }) => {
  const html = await (await request.get("/products/laptop")).text();
  expect(html).toContain("<title>Laptop | My Shop</title>");
  expect(html).toMatch(/<meta name="description" content="[^"]+"/);
  expect(html).toContain(
    '<link rel="canonical" href="https://shop.example.com/products/laptop"',
  );
});
```

### 440: Why should e2e tests run against a production build instead of the dev server?

The dev server and the production build behave differently:

- the dev server compiles on demand, so the first page load is slow and timing is different
- production has minification, tree shaking and code splitting, which can break code that works in dev (for example, code relying on function names)
- environment variables, feature flags, source maps and CSP headers can differ
- React dev mode adds extra checks and double-invokes effects in StrictMode, while production doesn't
- service workers and caching usually only work in production builds

Use `npm run build && npm run start` (or `vite preview`) as the `webServer` command in CI. The dev server is fine for writing tests locally.

### 441: How does React StrictMode affect your tests?

In development, StrictMode renders components twice and runs effects twice (mount, unmount, mount again) to find impure code and missing cleanup. Tests usually render without StrictMode unless you add it.

Turning it on in tests with `configure({ reactStrictMode: true })` or in your custom render helps catch bugs like:

- an effect that subscribes twice because it doesn't clean up
- a request sent twice and a counter incremented twice
- code that depends on an effect running only once

If a test that counts calls (like `toHaveBeenCalledTimes(1)` on a fetch) fails only with StrictMode, that's usually a real bug in the cleanup. Fix the effect rather than turning StrictMode off.

### 442: How can you catch memory leaks in a React app with automated tests?

Memory leaks (listeners not removed, timers not cleared, growing caches) usually show up after a lot of navigation. One approach with Playwright and Chromium:

1. Open the page and do the action many times, like opening and closing a modal or navigating between two pages 20 times.
2. Measure heap usage before and after with the Chrome DevTools Protocol (`HeapProfiler.collectGarbage` and `Runtime.getHeapUsage` through `context.newCDPSession(page)`), or with `performance.memory` in Chromium.
3. Fail if memory keeps growing past a limit.

Tools like Meta's `memlab` automate this and also show which objects are leaking. Memory numbers are noisy, so use big margins and many repetitions. At the unit level, testing that effects clean up on `unmount` prevents many leaks early.

### 443: How do you test error handling in components that use Suspense for data?

When data loading throws inside Suspense, the nearest error boundary catches it. Test the whole chain:

```tsx
test("shows an error with a retry button, and retry works", async () => {
  server.use(
    http.get("/api/profile", () => new HttpResponse(null, { status: 500 }), {
      once: true,
    }),
    http.get("/api/profile", () => HttpResponse.json({ name: "Anna" })),
  );
  vi.spyOn(console, "error").mockImplementation(() => {});
  const user = userEvent.setup();

  render(<ProfileRoute />, { wrapper: createWrapper() }); // ErrorBoundary + Suspense + useSuspenseQuery inside

  expect(
    await screen.findByText(/couldn't load your profile/i),
  ).toBeInTheDocument();

  await user.click(screen.getByRole("button", { name: "Try again" }));
  expect(await screen.findByText("Anna")).toBeInTheDocument();
});
```

For this to work, the retry button must reset both the error boundary and the data cache (for TanStack Query, `QueryErrorResetBoundary` or `reset` from `useQueryErrorResetBoundary`). Testing retry catches the common bug where the boundary resets but the cached error is thrown again right away.

### 444: How do you test a form that sends multipart data with a file to the API?

Read the form data in the MSW handler and check its fields:

```tsx
test("sends the title and the file", async () => {
  let received: FormData | undefined;
  server.use(
    http.post("/api/documents", async ({ request }) => {
      received = await request.formData();
      return HttpResponse.json({ id: 1 }, { status: 201 });
    }),
  );
  const user = userEvent.setup();
  render(<NewDocumentForm />);

  await user.type(screen.getByLabelText("Title"), "Contract");
  await user.upload(
    screen.getByLabelText("File"),
    new File(["%PDF-1.4"], "contract.pdf", { type: "application/pdf" }),
  );
  await user.click(screen.getByRole("button", { name: "Upload" }));

  await screen.findByText("Document uploaded");
  expect(received?.get("title")).toBe("Contract");
  expect((received?.get("file") as File).name).toBe("contract.pdf");
});
```

If the component sets the `Content-Type` header manually for multipart requests, that's a common bug (the boundary is missing), and a real browser e2e test against the real API catches it best.

### 445: How do you test React Router loaders and actions?

Loaders and actions are plain async functions that receive a request and params, so you can unit test them directly:

```ts
test("loader returns the project", async () => {
  server.use(
    http.get("/api/projects/7", () =>
      HttpResponse.json({ id: 7, name: "Apollo" }),
    ),
  );

  const result = await projectLoader({
    request: new Request("http://localhost/projects/7"),
    params: { id: "7" },
    context: {},
  } as any);

  expect(result).toEqual({ project: { id: 7, name: "Apollo" } });
});
```

Then test the route with `createMemoryRouter` and the real loader, to check the UI shows the data, the pending state and the error element. Actions can be tested the same way, by building a `Request` with `method: "POST"` and a `FormData` body. For framework mode (React Router as a framework), there are also testing helpers like `createRoutesStub` for rendering routes with stubbed loaders and actions.

### 446: How do you test a feature with many combinations of options without writing hundreds of tests?

- **Separate logic from UI**: put the rules (pricing, permissions, availability) in a function and test it with `test.each` tables. Table tests are cheap even with hundreds of rows.
- **Pairwise testing**: instead of every combination, choose a set where each **pair** of option values appears at least once. Most bugs come from the interaction of two settings, and this cuts the number of cases a lot. Tools can generate pairwise sets.
- **Property-based tests**: describe rules that must always hold (the total is never negative, an admin can always see everything) and let the tool generate combinations.
- **UI tests for a few representative cases**: the UI tests then only check that the result of the logic is displayed correctly.

### 447: How do you test a feature that is still changing a lot?

- Write **higher-level tests first** (integration or e2e) that check the main user outcome. They survive changes in the details.
- **Hold off on detailed unit tests** for parts that will probably be rewritten next week, but do test any tricky logic as soon as it's stable.
- Use **todo tests** (`test.todo`) to keep track of cases you still need to cover.
- Keep tests **cheap to change**: shared helpers, page objects, no big snapshots.
- Agree with the team that tests are part of the definition of done once the feature stabilizes, so it doesn't ship untested.

### 448: How is testing a reusable library component different from testing an app component?

For an **app component**, you test it through user behavior in the context of the app. Mocks for the network, real providers, and only the cases the app actually uses.

For a **library component** (design system, shared package), the API **is** the product, so you test more:

- every prop, variant and combination that's documented
- controlled and uncontrolled usage, ref forwarding, event handlers, `className` and style merging
- accessibility in detail (keyboard support, ARIA attributes) for every state
- different React versions and SSR if the library supports them
- type tests for its public types
- real browsers and visual tests, because consumers depend on how it looks

Breaking changes in a library affect many apps, so its tests act as a contract with all of them.

### 449: How do you test screen reader announcements with aria-live?

You can't test what a screen reader actually says in jsdom, but you can test that the right message goes into a live region:

```tsx
test("announces the number of results", async () => {
  const user = userEvent.setup();
  render(<ProductSearch />);

  await user.type(screen.getByRole("searchbox"), "lamp");

  expect(await screen.findByRole("status")).toHaveTextContent(
    "12 results found",
  );
});
```

Things to check: the live region (`role="status"`, `role="alert"` or `aria-live`) exists in the DOM **before** the message is added (many screen readers ignore regions that appear together with their content), the message is short and useful, and urgent errors use `alert`. For the real experience, test manually with VoiceOver or NVDA. There are also tools like Guidepup that automate real screen readers, but they're complex to run in CI.

### 450: Walk me through how you would test a new feature from start to finish.

Take a "share a document with a teammate" feature as an example:

1. **Before coding**: list the behaviors and edge cases with the team: share by email, invalid email, already shared, permission levels, the invited person gets access, removing access.
2. **Logic first**: unit test the pure parts as you write them, like email validation and the rules for who can share with which permission.
3. **API mocks**: add MSW handlers for the new endpoints, typed with the API types.
4. **Integration tests** for the share dialog with RTL and `user-event`: open the dialog, type an email, pick a permission, submit, see the person in the list. Add error cases (invalid email, 409 already shared, 500), loading state, keyboard use and focus handling, plus an axe check.
5. **Real browser checks** if the dialog depends on layout, with a visual test in light and dark themes.
6. **E2E**: one Playwright test with two browser contexts. The owner shares the document, and the teammate opens it and sees it. Data is created through the API, and the test cleans up after itself.
7. **CI**: everything runs on the pull request, the e2e test gets a `@smoke` tag if sharing is critical.
8. **After release**: watch errors in monitoring, and if a bug shows up, write a failing test for it first, then fix it.

The idea is to put most of the tests where they're cheap and stable (unit and integration), and use e2e only for proving the full flow works together.
