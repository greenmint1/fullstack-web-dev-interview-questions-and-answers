# JavaScript Design Patterns Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions about design patterns in JavaScript, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers use modern JavaScript (ES2022 and newer): classes with private fields, ES modules, `Proxy`, `Reflect`, `WeakMap`, generators and async/await. Older styles like IIFE modules and constructor functions are covered too, since you will still see them in real code.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a design pattern?](#1-what-is-a-design-pattern)
- [2: Why should a JavaScript developer learn design patterns?](#2-why-should-a-javascript-developer-learn-design-patterns)
- [3: What is the "Gang of Four" book?](#3-what-is-the-gang-of-four-book)
- [4: What are the three main categories of design patterns?](#4-what-are-the-three-main-categories-of-design-patterns)
- [5: What is an anti-pattern?](#5-what-is-an-anti-pattern)
- [6: Are design patterns specific to one language?](#6-are-design-patterns-specific-to-one-language)
- [7: Can using design patterns make code worse?](#7-can-using-design-patterns-make-code-worse)
- [8: What is the Module pattern?](#8-what-is-the-module-pattern)
- [9: What is an IIFE?](#9-what-is-an-iife)
- [10: What is the Revealing Module pattern?](#10-what-is-the-revealing-module-pattern)
- [11: How do ES modules relate to the Module pattern?](#11-how-do-es-modules-relate-to-the-module-pattern)
- [12: What is the Singleton pattern?](#12-what-is-the-singleton-pattern)
- [13: What is the simplest way to create a singleton in modern JavaScript?](#13-what-is-the-simplest-way-to-create-a-singleton-in-modern-javascript)
- [14: Why do many people call the Singleton an anti-pattern?](#14-why-do-many-people-call-the-singleton-an-anti-pattern)
- [15: What is the Factory pattern?](#15-what-is-the-factory-pattern)
- [16: What is a factory function in JavaScript?](#16-what-is-a-factory-function-in-javascript)
- [17: What is the difference between a factory function and a class?](#17-what-is-the-difference-between-a-factory-function-and-a-class)
- [18: What is the Constructor pattern?](#18-what-is-the-constructor-pattern)
- [19: What is the Prototype pattern?](#19-what-is-the-prototype-pattern)
- [20: What does Object.create() do?](#20-what-does-objectcreate-do)
- [21: What is the Observer pattern?](#21-what-is-the-observer-pattern)
- [22: Where do you see the Observer pattern in the browser?](#22-where-do-you-see-the-observer-pattern-in-the-browser)
- [23: What is the Publish/Subscribe (Pub/Sub) pattern?](#23-what-is-the-publishsubscribe-pubsub-pattern)
- [24: What is the difference between Observer and Pub/Sub?](#24-what-is-the-difference-between-observer-and-pubsub)
- [25: What is the Decorator pattern?](#25-what-is-the-decorator-pattern)
- [26: What is the Facade pattern?](#26-what-is-the-facade-pattern)
- [27: What is the Adapter pattern?](#27-what-is-the-adapter-pattern)
- [28: What is the Proxy pattern?](#28-what-is-the-proxy-pattern)
- [29: What is the Strategy pattern?](#29-what-is-the-strategy-pattern)
- [30: What is the Command pattern?](#30-what-is-the-command-pattern)
- [31: What is the Iterator pattern?](#31-what-is-the-iterator-pattern)
- [32: How do you make an object iterable?](#32-how-do-you-make-an-object-iterable)
- [33: What is the State pattern?](#33-what-is-the-state-pattern)
- [34: What is the Mediator pattern?](#34-what-is-the-mediator-pattern)
- [35: What is the Chain of Responsibility pattern?](#35-what-is-the-chain-of-responsibility-pattern)
- [36: What is the Template Method pattern?](#36-what-is-the-template-method-pattern)
- [37: What is the Builder pattern?](#37-what-is-the-builder-pattern)
- [38: What is the Composite pattern?](#38-what-is-the-composite-pattern)
- [39: What is the Flyweight pattern?](#39-what-is-the-flyweight-pattern)
- [40: What is the Memento pattern?](#40-what-is-the-memento-pattern)
- [41: What is the Mixin pattern?](#41-what-is-the-mixin-pattern)
- [42: What is "composition over inheritance"?](#42-what-is-composition-over-inheritance)
- [43: What is the MVC pattern?](#43-what-is-the-mvc-pattern)
- [44: What is the MVVM pattern?](#44-what-is-the-mvvm-pattern)
- [45: What is the difference between MVC and MVP?](#45-what-is-the-difference-between-mvc-and-mvp)
- [46: What is dependency injection?](#46-what-is-dependency-injection)
- [47: Why is dependency injection useful?](#47-why-is-dependency-injection-useful)
- [48: What is the Null Object pattern?](#48-what-is-the-null-object-pattern)
- [49: What is method chaining?](#49-what-is-method-chaining)
- [50: How do you make your own class support method chaining?](#50-how-do-you-make-your-own-class-support-method-chaining)
- [51: How do closures help with design patterns?](#51-how-do-closures-help-with-design-patterns)
- [52: How do you create private data in a class?](#52-how-do-you-create-private-data-in-a-class)
- [53: What are getters and setters used for in patterns?](#53-what-are-getters-and-setters-used-for-in-patterns)
- [54: What is the Namespace pattern?](#54-what-is-the-namespace-pattern)
- [55: What is the Options Object (configuration object) pattern?](#55-what-is-the-options-object-configuration-object-pattern)
- [56: What is memoization?](#56-what-is-memoization)
- [57: What is debouncing?](#57-what-is-debouncing)
- [58: What is throttling?](#58-what-is-throttling)
- [59: What is the difference between debounce and throttle?](#59-what-is-the-difference-between-debounce-and-throttle)
- [60: What is currying?](#60-what-is-currying)
- [61: What is partial application?](#61-what-is-partial-application)
- [62: What is a higher-order function?](#62-what-is-a-higher-order-function)
- [63: What is the callback pattern?](#63-what-is-the-callback-pattern)
- [64: What are error-first callbacks?](#64-what-are-error-first-callbacks)
- [65: What is "callback hell"?](#65-what-is-callback-hell)
- [66: How are Promises a design pattern?](#66-how-are-promises-a-design-pattern)
- [67: How do you run several async tasks in parallel?](#67-how-do-you-run-several-async-tasks-in-parallel)
- [68: What is the EventEmitter in Node.js?](#68-what-is-the-eventemitter-in-nodejs)
- [69: How do you create custom events in the browser?](#69-how-do-you-create-custom-events-in-the-browser)
- [70: What is lazy initialization?](#70-what-is-lazy-initialization)
- [71: How do you create an enum in JavaScript?](#71-how-do-you-create-an-enum-in-javascript)
- [72: What does Object.freeze() do?](#72-what-does-objectfreeze-do)
- [73: What is the Abstract Factory pattern?](#73-what-is-the-abstract-factory-pattern)
- [74: What is the Bridge pattern?](#74-what-is-the-bridge-pattern)
- [75: What is the Visitor pattern?](#75-what-is-the-visitor-pattern)
- [76: What is the Interpreter pattern?](#76-what-is-the-interpreter-pattern)
- [77: What is a higher-order component (HOC) in React?](#77-what-is-a-higher-order-component-hoc-in-react)
- [78: What is the render props pattern?](#78-what-is-the-render-props-pattern)
- [79: What is the hooks pattern in React?](#79-what-is-the-hooks-pattern-in-react)
- [80: What is the Container/Presentational pattern?](#80-what-is-the-containerpresentational-pattern)
- [81: What is the Provider pattern?](#81-what-is-the-provider-pattern)
- [82: What is Flux?](#82-what-is-flux)
- [83: What is unidirectional data flow?](#83-what-is-unidirectional-data-flow)
- [84: Which patterns does Redux use?](#84-which-patterns-does-redux-use)
- [85: What is a pure function?](#85-what-is-a-pure-function)
- [86: Why is immutability important in some patterns?](#86-why-is-immutability-important-in-some-patterns)
- [87: What does SOLID stand for?](#87-what-does-solid-stand-for)
- [88: What is the Single Responsibility Principle in practice?](#88-what-is-the-single-responsibility-principle-in-practice)
- [89: What is the Open/Closed Principle in JavaScript?](#89-what-is-the-openclosed-principle-in-javascript)
- [90: What are DRY, KISS and YAGNI?](#90-what-are-dry-kiss-and-yagni)
- [91: What is separation of concerns?](#91-what-is-separation-of-concerns)
- [92: What is the difference between coupling and cohesion?](#92-what-is-the-difference-between-coupling-and-cohesion)
- [93: What is a guard clause?](#93-what-is-a-guard-clause)
- [94: How can you replace a long switch statement with an object?](#94-how-can-you-replace-a-long-switch-statement-with-an-object)
- [95: What is the Registry pattern?](#95-what-is-the-registry-pattern)
- [96: What is the Plugin pattern?](#96-what-is-the-plugin-pattern)
- [97: What is the Middleware pattern?](#97-what-is-the-middleware-pattern)
- [98: What is "polluting the global scope" and why is it bad?](#98-what-is-polluting-the-global-scope-and-why-is-it-bad)
- [99: What is a "god object"?](#99-what-is-a-god-object)
- [100: Why is extending built-in prototypes considered bad practice?](#100-why-is-extending-built-in-prototypes-considered-bad-practice)
- [101: Are JavaScript classes real classes like in Java?](#101-are-javascript-classes-real-classes-like-in-java)
- [102: How does inheritance work with extends?](#102-how-does-inheritance-work-with-extends)
- [103: What is a static method and how is it used in patterns?](#103-what-is-a-static-method-and-how-is-it-used-in-patterns)
- [104: What is the Factory Method pattern?](#104-what-is-the-factory-method-pattern)
- [105: What is the prototype chain?](#105-what-is-the-prototype-chain)
- [106: How do you copy an object in JavaScript?](#106-how-do-you-copy-an-object-in-javascript)
- [107: What is event delegation?](#107-what-is-event-delegation)
- [108: What is an Observable?](#108-what-is-an-observable)
- [109: What is a signal in front-end frameworks?](#109-what-is-a-signal-in-front-end-frameworks)
- [110: What is two-way data binding?](#110-what-is-two-way-data-binding)
- [111: What is the Repository pattern?](#111-what-is-the-repository-pattern)
- [112: What is a service layer?](#112-what-is-a-service-layer)
- [113: What is a DTO (Data Transfer Object)?](#113-what-is-a-dto-data-transfer-object)
- [114: What is a Value Object?](#114-what-is-a-value-object)
- [115: What is duck typing?](#115-what-is-duck-typing)
- [116: How do you define an "interface" in JavaScript?](#116-how-do-you-define-an-interface-in-javascript)
- [117: What is the difference between an iterable and an iterator?](#117-what-is-the-difference-between-an-iterable-and-an-iterator)
- [118: What is a generator function?](#118-what-is-a-generator-function)
- [119: What are async iterators?](#119-what-are-async-iterators)
- [120: What is a thunk?](#120-what-is-a-thunk)
- [121: What is function composition?](#121-what-is-function-composition)
- [122: What is inversion of control?](#122-what-is-inversion-of-control)
- [123: What is the Law of Demeter?](#123-what-is-the-law-of-demeter)
- [124: What does "tell, don't ask" mean?](#124-what-does-tell-dont-ask-mean)
- [125: What is the Object Pool pattern?](#125-what-is-the-object-pool-pattern)
- [126: What is feature detection?](#126-what-is-feature-detection)
- [127: How is a polyfill related to design patterns?](#127-how-is-a-polyfill-related-to-design-patterns)
- [128: What is init-time branching?](#128-what-is-init-time-branching)
- [129: What is the Event Bus pattern?](#129-what-is-the-event-bus-pattern)
- [130: What is the Producer/Consumer pattern?](#130-what-is-the-producerconsumer-pattern)
- [131: How do you load code only when it is needed?](#131-how-do-you-load-code-only-when-it-is-needed)
- [132: What are rendering patterns on the web?](#132-what-are-rendering-patterns-on-the-web)
- [133: What is a barrel file?](#133-what-is-a-barrel-file)
- [134: How do you cancel an async operation?](#134-how-do-you-cancel-an-async-operation)
- [135: How do you model loading, success and error states in UI code?](#135-how-do-you-model-loading-success-and-error-states-in-ui-code)
- [136: What is a Web Component and which patterns does it use?](#136-what-is-a-web-component-and-which-patterns-does-it-use)
- [137: What is the Object Literal pattern?](#137-what-is-the-object-literal-pattern)
- [138: Which objects in the browser are effectively singletons?](#138-which-objects-in-the-browser-are-effectively-singletons)
- [139: What is the Retry pattern?](#139-what-is-the-retry-pattern)
- [140: What is a wrapper, and is it a design pattern?](#140-what-is-a-wrapper-and-is-it-a-design-pattern)
- [141: What is a "thenable"?](#141-what-is-a-thenable)
- [142: What is the difference between a class and an object literal for creating objects?](#142-what-is-the-difference-between-a-class-and-an-object-literal-for-creating-objects)
- [143: How do you use WeakMap for private data?](#143-how-do-you-use-weakmap-for-private-data)
- [144: What are Symbols used for in patterns?](#144-what-are-symbols-used-for-in-patterns)
- [145: What is the difference between a library and a framework?](#145-what-is-the-difference-between-a-library-and-a-framework)
- [146: What is the Compound Components pattern?](#146-what-is-the-compound-components-pattern)
- [147: What are controlled and uncontrolled components?](#147-what-are-controlled-and-uncontrolled-components)
- [148: What is "configuration over code"?](#148-what-is-configuration-over-code)
- [149: What is the difference between design patterns and architectural patterns?](#149-what-is-the-difference-between-design-patterns-and-architectural-patterns)
- [150: How do you pick the right design pattern for a problem?](#150-how-do-you-pick-the-right-design-pattern-for-a-problem)

### Moderate Questions (151-300)

- [151: What is the difference between Proxy, Decorator and Adapter?](#151-what-is-the-difference-between-proxy-decorator-and-adapter)
- [152: What is the difference between Facade and Adapter?](#152-what-is-the-difference-between-facade-and-adapter)
- [153: What is the difference between Strategy and State?](#153-what-is-the-difference-between-strategy-and-state)
- [154: How can the Observer pattern cause memory leaks?](#154-how-can-the-observer-pattern-cause-memory-leaks)
- [155: How would you implement a small event emitter with on, off, once and emit?](#155-how-would-you-implement-a-small-event-emitter-with-on-off-once-and-emit)
- [156: Why should an emitter catch errors thrown by one listener?](#156-why-should-an-emitter-catch-errors-thrown-by-one-listener)
- [157: How do you test code that uses a singleton?](#157-how-do-you-test-code-that-uses-a-singleton)
- [158: Is a module-level singleton always one instance in Node.js?](#158-is-a-module-level-singleton-always-one-instance-in-nodejs)
- [159: How do you create a singleton that needs async setup?](#159-how-do-you-create-a-singleton-that-needs-async-setup)
- [160: How do you make a factory open for extension without editing it?](#160-how-do-you-make-a-factory-open-for-extension-without-editing-it)
- [161: When should you use a Builder instead of an options object?](#161-when-should-you-use-a-builder-instead-of-an-options-object)
- [162: How do you validate in a Builder?](#162-how-do-you-validate-in-a-builder)
- [163: How do you write an immutable fluent API?](#163-how-do-you-write-an-immutable-fluent-api)
- [164: How do you use Object.create with property descriptors?](#164-how-do-you-use-objectcreate-with-property-descriptors)
- [165: How do you write class-based mixins?](#165-how-do-you-write-class-based-mixins)
- [166: What are the problems with mixins?](#166-what-are-the-problems-with-mixins)
- [167: How do you memoize an async function?](#167-how-do-you-memoize-an-async-function)
- [168: How do you decorate a class method without decorator syntax?](#168-how-do-you-decorate-a-class-method-without-decorator-syntax)
- [169: What is the decorator syntax (@) in JavaScript?](#169-what-is-the-decorator-syntax--in-javascript)
- [170: How do you use a Proxy for validation?](#170-how-do-you-use-a-proxy-for-validation)
- [171: How can a Proxy provide default values for missing properties?](#171-how-can-a-proxy-provide-default-values-for-missing-properties)
- [172: Why use Reflect inside Proxy traps?](#172-why-use-reflect-inside-proxy-traps)
- [173: What is a virtual proxy?](#173-what-is-a-virtual-proxy)
- [174: How would you build a caching proxy for an API client?](#174-how-would-you-build-a-caching-proxy-for-an-api-client)
- [175: What is a revocable proxy?](#175-what-is-a-revocable-proxy)
- [176: How do you implement undo and redo with the Command pattern?](#176-how-do-you-implement-undo-and-redo-with-the-command-pattern)
- [177: What is a macro command?](#177-what-is-a-macro-command)
- [178: How do you implement Chain of Responsibility for validation?](#178-how-do-you-implement-chain-of-responsibility-for-validation)
- [179: How would you implement a middleware runner like Koa's?](#179-how-would-you-implement-a-middleware-runner-like-koas)
- [180: What is the difference between Mediator and Observer?](#180-what-is-the-difference-between-mediator-and-observer)
- [181: Can you give a practical example of the Mediator pattern in a UI?](#181-can-you-give-a-practical-example-of-the-mediator-pattern-in-a-ui)
- [182: How do you build a lazy data pipeline with generators?](#182-how-do-you-build-a-lazy-data-pipeline-with-generators)
- [183: What are iterator helpers?](#183-what-are-iterator-helpers)
- [184: What do return() and throw() do on a generator?](#184-what-do-return-and-throw-do-on-a-generator)
- [185: How do you implement the Composite pattern for a file tree?](#185-how-do-you-implement-the-composite-pattern-for-a-file-tree)
- [186: How would you implement a Flyweight with a factory?](#186-how-would-you-implement-a-flyweight-with-a-factory)
- [187: What is the difference between Template Method and Strategy?](#187-what-is-the-difference-between-template-method-and-strategy)
- [188: How do you implement a finite state machine with a transition table?](#188-how-do-you-implement-a-finite-state-machine-with-a-transition-table)
- [189: How do you implement undo with Memento using immutable state?](#189-how-do-you-implement-undo-with-memento-using-immutable-state)
- [190: How can a Repository add caching without changing its callers?](#190-how-can-a-repository-add-caching-without-changing-its-callers)
- [191: What is a composition root?](#191-what-is-a-composition-root)
- [192: How would you build a small dependency injection container?](#192-how-would-you-build-a-small-dependency-injection-container)
- [193: What is the difference between a Service Locator and dependency injection?](#193-what-is-the-difference-between-a-service-locator-and-dependency-injection)
- [194: How does dependency injection make testing easier?](#194-how-does-dependency-injection-make-testing-easier)
- [195: How do you send messages between browser tabs?](#195-how-do-you-send-messages-between-browser-tabs)
- [196: How do you communicate between a page and an iframe or worker?](#196-how-do-you-communicate-between-a-page-and-an-iframe-or-worker)
- [197: How would you add cancel and flush to a debounce function?](#197-how-would-you-add-cancel-and-flush-to-a-debounce-function)
- [198: How do you throttle with requestAnimationFrame?](#198-how-do-you-throttle-with-requestanimationframe)
- [199: What problems come up when memoizing functions with several arguments?](#199-what-problems-come-up-when-memoizing-functions-with-several-arguments)
- [200: How do you memoize a function that takes objects without leaking memory?](#200-how-do-you-memoize-a-function-that-takes-objects-without-leaking-memory)
- [201: How do you implement an LRU cache in JavaScript?](#201-how-do-you-implement-an-lru-cache-in-javascript)
- [202: How do you retry with exponential backoff and jitter?](#202-how-do-you-retry-with-exponential-backoff-and-jitter)
- [203: How do you add a timeout to an async operation?](#203-how-do-you-add-a-timeout-to-an-async-operation)
- [204: How do you limit how many async tasks run at the same time?](#204-how-do-you-limit-how-many-async-tasks-run-at-the-same-time)
- [205: How do you run async tasks one after another?](#205-how-do-you-run-async-tasks-one-after-another)
- [206: When do you use Promise.all, allSettled, race and any?](#206-when-do-you-use-promiseall-allsettled-race-and-any)
- [207: What is a deferred, and how does Promise.withResolvers help?](#207-what-is-a-deferred-and-how-does-promisewithresolvers-help)
- [208: How do you make sure async tasks run one at a time, in order?](#208-how-do-you-make-sure-async-tasks-run-one-at-a-time-in-order)
- [209: What is the Result pattern for error handling?](#209-what-is-the-result-pattern-for-error-handling)
- [210: How do you design custom error classes?](#210-how-do-you-design-custom-error-classes)
- [211: When should you use the Null Object pattern instead of optional chaining?](#211-when-should-you-use-the-null-object-pattern-instead-of-optional-chaining)
- [212: Why wrap a third-party library in your own adapter?](#212-why-wrap-a-third-party-library-in-your-own-adapter)
- [213: What is an anti-corruption layer?](#213-what-is-an-anti-corruption-layer)
- [214: How would you build a facade over browser storage?](#214-how-would-you-build-a-facade-over-browser-storage)
- [215: What are live bindings in ES modules?](#215-what-are-live-bindings-in-es-modules)
- [216: How do circular dependencies between modules cause problems, and how do you fix them?](#216-how-do-circular-dependencies-between-modules-cause-problems-and-how-do-you-fix-them)
- [217: How does the Module pattern differ between CommonJS and ES modules?](#217-how-does-the-module-pattern-differ-between-commonjs-and-es-modules)
- [218: What is a downside of the Revealing Module pattern?](#218-what-is-a-downside-of-the-revealing-module-pattern)
- [219: Why do methods lose this when used as callbacks, and how do you fix it?](#219-why-do-methods-lose-this-when-used-as-callbacks-and-how-do-you-fix-it)
- [220: What is the cost of using arrow functions as class fields?](#220-what-is-the-cost-of-using-arrow-functions-as-class-fields)
- [221: How would you structure a small vanilla JavaScript app with MVC?](#221-how-would-you-structure-a-small-vanilla-javascript-app-with-mvc)
- [222: How could you build simple data binding with a Proxy?](#222-how-could-you-build-simple-data-binding-with-a-proxy)
- [223: How would you write a minimal store like Redux?](#223-how-would-you-write-a-minimal-store-like-redux)
- [224: How do you connect an external store to React?](#224-how-do-you-connect-an-external-store-to-react)
- [225: What is a selector and why memoize it?](#225-what-is-a-selector-and-why-memoize-it)
- [226: What is reducer composition?](#226-what-is-reducer-composition)
- [227: What does a Redux middleware look like?](#227-what-does-a-redux-middleware-look-like)
- [228: What is the difference between commands and events in action naming?](#228-what-is-the-difference-between-commands-and-events-in-action-naming)
- [229: What is optimistic UI, and how do you implement it?](#229-what-is-optimistic-ui-and-how-do-you-implement-it)
- [230: What is stale-while-revalidate?](#230-what-is-stale-while-revalidate)
- [231: How do you avoid sending the same request twice at the same time?](#231-how-do-you-avoid-sending-the-same-request-twice-at-the-same-time)
- [232: What makes a good custom hook?](#232-what-makes-a-good-custom-hook)
- [233: How do HOCs, render props and hooks compare?](#233-how-do-hocs-render-props-and-hooks-compare)
- [234: Why can the Provider pattern cause performance problems?](#234-why-can-the-provider-pattern-cause-performance-problems)
- [235: How do you implement compound components in React?](#235-how-do-you-implement-compound-components-in-react)
- [236: What is a headless component?](#236-what-is-a-headless-component)
- [237: What is the Slot pattern?](#237-what-is-the-slot-pattern)
- [238: What is the prop getters pattern?](#238-what-is-the-prop-getters-pattern)
- [239: What is the state reducer pattern?](#239-what-is-the-state-reducer-pattern)
- [240: What is an error boundary?](#240-what-is-an-error-boundary)
- [241: What is the Portal pattern?](#241-what-is-the-portal-pattern)
- [242: How do you lazy load images with IntersectionObserver?](#242-how-do-you-lazy-load-images-with-intersectionobserver)
- [243: What is list virtualization (windowing)?](#243-what-is-list-virtualization-windowing)
- [244: How do you handle many different actions with one delegated listener?](#244-how-do-you-handle-many-different-actions-with-one-delegated-listener)
- [245: How does a Web Component react to attribute changes?](#245-how-does-a-web-component-react-to-attribute-changes)
- [246: How do you implement feature flags in a clean way?](#246-how-do-you-implement-feature-flags-in-a-clean-way)
- [247: How would you combine Factory and Strategy for payment providers?](#247-how-would-you-combine-factory-and-strategy-for-payment-providers)
- [248: How do you design a plugin system with hooks?](#248-how-do-you-design-a-plugin-system-with-hooks)
- [249: How do you write the Template Method pattern without classes?](#249-how-do-you-write-the-template-method-pattern-without-classes)
- [250: How would you implement a simple Visitor for a syntax tree?](#250-how-would-you-implement-a-simple-visitor-for-a-syntax-tree)
- [251: How would you write a tiny expression evaluator with the Interpreter pattern?](#251-how-would-you-write-a-tiny-expression-evaluator-with-the-interpreter-pattern)
- [252: Can you show the Bridge pattern with a real example?](#252-can-you-show-the-bridge-pattern-with-a-real-example)
- [253: When is an Abstract Factory useful in front-end code?](#253-when-is-an-abstract-factory-useful-in-front-end-code)
- [254: How would you implement an object pool?](#254-how-would-you-implement-an-object-pool)
- [255: What is the difference between dirty checking and the Observer approach to change detection?](#255-what-is-the-difference-between-dirty-checking-and-the-observer-approach-to-change-detection)
- [256: What is the h() or createElement factory pattern?](#256-what-is-the-h-or-createelement-factory-pattern)
- [257: How are tagged template literals used as a pattern?](#257-how-are-tagged-template-literals-used-as-a-pattern)
- [258: How do you build a pipeline with async steps?](#258-how-do-you-build-a-pipeline-with-async-steps)
- [259: How would you write a generic curry function?](#259-how-would-you-write-a-generic-curry-function)
- [260: What is point-free style?](#260-what-is-point-free-style)
- [261: How do you deep freeze an object?](#261-how-do-you-deep-freeze-an-object)
- [262: How does Immer let you "mutate" state immutably?](#262-how-does-immer-let-you-mutate-state-immutably)
- [263: Why does reference equality matter for many patterns?](#263-why-does-reference-equality-matter-for-many-patterns)
- [264: How do you test code that uses the Observer pattern?](#264-how-do-you-test-code-that-uses-the-observer-pattern)
- [265: How do you test debounced or throttled functions?](#265-how-do-you-test-debounced-or-throttled-functions)
- [266: When should you mock a module and when should you use dependency injection?](#266-when-should-you-mock-a-module-and-when-should-you-use-dependency-injection)
- [267: What is a layered architecture in a front-end app?](#267-what-is-a-layered-architecture-in-a-front-end-app)
- [268: What is a feature-based folder structure?](#268-what-is-a-feature-based-folder-structure)
- [269: How do you keep a feature module's internals private?](#269-how-do-you-keep-a-feature-modules-internals-private)
- [270: How do polling, long polling and push compare as update patterns?](#270-how-do-polling-long-polling-and-push-compare-as-update-patterns)
- [271: How do you write a WebSocket client that reconnects?](#271-how-do-you-write-a-websocket-client-that-reconnects)
- [272: What is the heartbeat pattern?](#272-what-is-the-heartbeat-pattern)
- [273: How would you implement keyboard shortcuts with the Command pattern?](#273-how-would-you-implement-keyboard-shortcuts-with-the-command-pattern)
- [274: Snapshots or patches: how should you store undo history?](#274-snapshots-or-patches-how-should-you-store-undo-history)
- [275: Can you give a JavaScript example of dependency inversion?](#275-can-you-give-a-javascript-example-of-dependency-inversion)
- [276: What does the Liskov Substitution Principle look like in JavaScript?](#276-what-does-the-liskov-substitution-principle-look-like-in-javascript)
- [277: What does Interface Segregation mean when JavaScript has no interfaces?](#277-what-does-interface-segregation-mean-when-javascript-has-no-interfaces)
- [278: What is the Delegation pattern?](#278-what-is-the-delegation-pattern)
- [279: What is OLOO, and how is it different from classes?](#279-what-is-oloo-and-how-is-it-different-from-classes)
- [280: Which ways to make data private exist, and how do they compare?](#280-which-ways-to-make-data-private-exist-and-how-do-they-compare)
- [281: How do you use Object.defineProperty in patterns?](#281-how-do-you-use-objectdefineproperty-in-patterns)
- [282: How would you build a very small signals implementation?](#282-how-would-you-build-a-very-small-signals-implementation)
- [283: What is derived state, and how should you handle it?](#283-what-is-derived-state-and-how-should-you-handle-it)
- [284: What does normalizing state mean?](#284-what-does-normalizing-state-mean)
- [285: How would you use a Facade to simplify a checkout flow?](#285-how-would-you-use-a-facade-to-simplify-a-checkout-flow)
- [286: How do you build an API client with interceptors?](#286-how-do-you-build-an-api-client-with-interceptors)
- [287: What is graceful degradation?](#287-what-is-graceful-degradation)
- [288: What is progressive enhancement?](#288-what-is-progressive-enhancement)
- [289: Which design patterns can you spot in Express?](#289-which-design-patterns-can-you-spot-in-express)
- [290: Which design patterns can you spot in React?](#290-which-design-patterns-can-you-spot-in-react)
- [291: What is the Specification pattern?](#291-what-is-the-specification-pattern)
- [292: What is the Strangler Fig pattern?](#292-what-is-the-strangler-fig-pattern)
- [293: What is the Backend for Frontend (BFF) pattern?](#293-what-is-the-backend-for-frontend-bff-pattern)
- [294: What is the Saga pattern in front-end state management?](#294-what-is-the-saga-pattern-in-front-end-state-management)
- [295: What is the Unit of Work pattern?](#295-what-is-the-unit-of-work-pattern)
- [296: How does request batching work, like in DataLoader?](#296-how-does-request-batching-work-like-in-dataloader)
- [297: What is event-driven architecture?](#297-what-is-event-driven-architecture)
- [298: How do you schedule work so it doesn't block the UI?](#298-how-do-you-schedule-work-so-it-doesnt-block-the-ui)
- [299: How do you split a long task into chunks?](#299-how-do-you-split-a-long-task-into-chunks)
- [300: How do you refactor existing code toward a design pattern safely?](#300-how-do-you-refactor-existing-code-toward-a-design-pattern-safely)

### Advanced Questions (301-450)

- [301: Why does an ES module behave like a singleton, and where does that stop being true?](#301-why-does-an-es-module-behave-like-a-singleton-and-where-does-that-stop-being-true)
- [302: What problems do multiple realms cause for patterns that use instanceof?](#302-what-problems-do-multiple-realms-cause-for-patterns-that-use-instanceof)
- [303: How can you share a singleton across separately bundled code?](#303-how-can-you-share-a-singleton-across-separately-bundled-code)
- [304: Why can instanceof break with duplicated packages, and how do libraries deal with it?](#304-why-can-instanceof-break-with-duplicated-packages-and-how-do-libraries-deal-with-it)
- [305: What is Symbol.hasInstance, and when would you use it?](#305-what-is-symbolhasinstance-and-when-would-you-use-it)
- [306: What are Proxy invariants?](#306-what-are-proxy-invariants)
- [307: What is the performance cost of Proxy?](#307-what-is-the-performance-cost-of-proxy)
- [308: What identity problems come with proxies?](#308-what-identity-problems-come-with-proxies)
- [309: Why do private class fields not work through a Proxy?](#309-why-do-private-class-fields-not-work-through-a-proxy)
- [310: Why is proxying Map, Set or Date tricky?](#310-why-is-proxying-map-set-or-date-tricky)
- [311: What is the membrane pattern?](#311-what-is-the-membrane-pattern)
- [312: How does a deep reactive system avoid wrapping the whole object tree up front?](#312-how-does-a-deep-reactive-system-avoid-wrapping-the-whole-object-tree-up-front)
- [313: What is the "diamond problem" or glitch in reactive systems?](#313-what-is-the-diamond-problem-or-glitch-in-reactive-systems)
- [314: What is the difference between push, pull and push-pull reactivity?](#314-what-is-the-difference-between-push-pull-and-push-pull-reactivity)
- [315: How do you batch notifications in an observer-based store?](#315-how-do-you-batch-notifications-in-an-observer-based-store)
- [316: What happens if a subscriber emits a new event while the subject is still notifying?](#316-what-happens-if-a-subscriber-emits-a-new-event-while-the-subject-is-still-notifying)
- [317: Should observer notifications be sync or async?](#317-should-observer-notifications-be-sync-or-async)
- [318: What does "don't release Zalgo" mean?](#318-what-does-dont-release-zalgo-mean)
- [319: Can WeakRef and FinalizationRegistry be used to build weak observers?](#319-can-weakref-and-finalizationregistry-be-used-to-build-weak-observers)
- [320: How do you find memory leaks caused by patterns like Observer or caches in a single-page app?](#320-how-do-you-find-memory-leaks-caused-by-patterns-like-observer-or-caches-in-a-single-page-app)
- [321: How can closures cause memory leaks?](#321-how-can-closures-cause-memory-leaks)
- [322: Do factory functions or classes perform better in V8?](#322-do-factory-functions-or-classes-perform-better-in-v8)
- [323: What are hidden classes, and how do patterns affect them?](#323-what-are-hidden-classes-and-how-do-patterns-affect-them)
- [324: What is a megamorphic call site, and can Strategy or polymorphism cause it?](#324-what-is-a-megamorphic-call-site-and-can-strategy-or-polymorphism-cause-it)
- [325: When does object pooling hurt instead of help in JavaScript?](#325-when-does-object-pooling-hurt-instead-of-help-in-javascript)
- [326: How do persistent data structures support immutable patterns at scale?](#326-how-do-persistent-data-structures-support-immutable-patterns-at-scale)
- [327: When is it fine to mutate inside an "immutable" codebase?](#327-when-is-it-fine-to-mutate-inside-an-immutable-codebase)
- [328: How can recursive promise patterns starve the event loop?](#328-how-can-recursive-promise-patterns-starve-the-event-loop)
- [329: How do you handle backpressure in a producer/consumer pipeline?](#329-how-do-you-handle-backpressure-in-a-producerconsumer-pipeline)
- [330: How do you build a processing pipeline with Web Streams?](#330-how-do-you-build-a-processing-pipeline-with-web-streams)
- [331: How do you combine several cancellation reasons into one signal?](#331-how-do-you-combine-several-cancellation-reasons-into-one-signal)
- [332: What is explicit resource management (using and Symbol.dispose)?](#332-what-is-explicit-resource-management-using-and-symboldispose)
- [333: What is the Circuit Breaker pattern?](#333-what-is-the-circuit-breaker-pattern)
- [334: What is the Bulkhead pattern?](#334-what-is-the-bulkhead-pattern)
- [335: How would you implement a client-side rate limiter?](#335-how-would-you-implement-a-client-side-rate-limiter)
- [336: Why are idempotency keys important when combining retries with writes?](#336-why-are-idempotency-keys-important-when-combining-retries-with-writes)
- [337: How do you avoid out-of-order responses in a search-as-you-type feature?](#337-how-do-you-avoid-out-of-order-responses-in-a-search-as-you-type-feature)
- [338: What is the stale closure problem in React hooks?](#338-what-is-the-stale-closure-problem-in-react-hooks)
- [339: How do you implement a mutex in JavaScript?](#339-how-do-you-implement-a-mutex-in-javascript)
- [340: How do you implement a semaphore?](#340-how-do-you-implement-a-semaphore)
- [341: How do you make sure only one tab does a job, like polling or refreshing a token?](#341-how-do-you-make-sure-only-one-tab-does-a-job-like-polling-or-refreshing-a-token)
- [342: How can the Actor model be used with Web Workers?](#342-how-can-the-actor-model-be-used-with-web-workers)
- [343: When would you use SharedArrayBuffer and Atomics instead of message passing?](#343-when-would-you-use-sharedarraybuffer-and-atomics-instead-of-message-passing)
- [344: What is Event Sourcing, and does it make sense in a front end?](#344-what-is-event-sourcing-and-does-it-make-sense-in-a-front-end)
- [345: What is CQRS, and how does it relate to front-end code?](#345-what-is-cqrs-and-how-does-it-relate-to-front-end-code)
- [346: How do CRDTs and Operational Transformation compare for collaborative apps?](#346-how-do-crdts-and-operational-transformation-compare-for-collaborative-apps)
- [347: How can micro-frontends be composed?](#347-how-can-micro-frontends-be-composed)
- [348: What problems come with shared dependencies in Module Federation?](#348-what-problems-come-with-shared-dependencies-in-module-federation)
- [349: How do you isolate untrusted plugins in a web app?](#349-how-do-you-isolate-untrusted-plugins-in-a-web-app)
- [350: How do hierarchical injectors work, as in Angular?](#350-how-do-hierarchical-injectors-work-as-in-angular)
- [351: What are dependency lifetimes, and what is a captive dependency?](#351-what-are-dependency-lifetimes-and-what-is-a-captive-dependency)
- [352: How do you handle circular dependencies in a DI container?](#352-how-do-you-handle-circular-dependencies-in-a-di-container)
- [353: How can the new decorators and Symbol.metadata support dependency injection?](#353-how-can-the-new-decorators-and-symbolmetadata-support-dependency-injection)
- [354: What is the accessor keyword in the decorators proposal?](#354-what-is-the-accessor-keyword-in-the-decorators-proposal)
- [355: How do singletons and registries interact with tree shaking?](#355-how-do-singletons-and-registries-interact-with-tree-shaking)
- [356: What goes wrong with "self-registering" modules?](#356-what-goes-wrong-with-self-registering-modules)
- [357: What is the dual package hazard, and how do you avoid it?](#357-what-is-the-dual-package-hazard-and-how-do-you-avoid-it)
- [358: How do you choose a lazy loading and preloading strategy?](#358-how-do-you-choose-a-lazy-loading-and-preloading-strategy)
- [359: How can the Strategy pattern work with code splitting?](#359-how-can-the-strategy-pattern-work-with-code-splitting)
- [360: What is the composition pattern for mixing server and client components in React?](#360-what-is-the-composition-pattern-for-mixing-server-and-client-components-in-react)
- [361: What is the islands architecture?](#361-what-is-the-islands-architecture)
- [362: What is resumability, and how is it different from hydration?](#362-what-is-resumability-and-how-is-it-different-from-hydration)
- [363: How do fine-grained signals and a virtual DOM differ as architectures?](#363-how-do-fine-grained-signals-and-a-virtual-dom-differ-as-architectures)
- [364: What are statecharts, and what do they add to state machines?](#364-what-are-statecharts-and-what-do-they-add-to-state-machines)
- [365: How does XState use the Actor model?](#365-how-does-xstate-use-the-actor-model)
- [366: How do you make impossible states impossible?](#366-how-do-you-make-impossible-states-impossible)
- [367: What are branded types, and how do they relate to Value Objects?](#367-what-are-branded-types-and-how-do-they-relate-to-value-objects)
- [368: How do you make a Builder that only allows build() when required fields are set?](#368-how-do-you-make-a-builder-that-only-allows-build-when-required-fields-are-set)
- [369: Why does JavaScript not need double dispatch for the Visitor pattern?](#369-why-does-javascript-not-need-double-dispatch-for-the-visitor-pattern)
- [370: Why is eval or new Function a bad way to implement an Interpreter for user input?](#370-why-is-eval-or-new-function-a-bad-way-to-implement-an-interpreter-for-user-input)
- [371: What is the fragile base class problem?](#371-what-is-the-fragile-base-class-problem)
- [372: How can overriding a sync method with an async one break Liskov substitution?](#372-how-can-overriding-a-sync-method-with-an-async-one-break-liskov-substitution)
- [373: How should errors be translated between layers?](#373-how-should-errors-be-translated-between-layers)
- [374: How do you set up global error handling in a browser app?](#374-how-do-you-set-up-global-error-handling-in-a-browser-app)
- [375: What details do wrapper functions (decorators) often get wrong?](#375-what-details-do-wrapper-functions-decorators-often-get-wrong)
- [376: What are the common pitfalls of memoization in production code?](#376-what-are-the-common-pitfalls-of-memoization-in-production-code)
- [377: What client-side cache invalidation strategies are there?](#377-what-client-side-cache-invalidation-strategies-are-there)
- [378: How does a normalized client cache work, as in Apollo Client?](#378-how-does-a-normalized-client-cache-work-as-in-apollo-client)
- [379: How do you handle optimistic updates when several mutations overlap?](#379-how-do-you-handle-optimistic-updates-when-several-mutations-overlap)
- [380: How does the outbox pattern support offline-first apps?](#380-how-does-the-outbox-pattern-support-offline-first-apps)
- [381: What caching strategies can a service worker use?](#381-what-caching-strategies-can-a-service-worker-use)
- [382: What is Background Sync, and what are its limits?](#382-what-is-background-sync-and-what-are-its-limits)
- [383: How can a deep merge or "extend" utility cause prototype pollution?](#383-how-can-a-deep-merge-or-extend-utility-cause-prototype-pollution)
- [384: Why is it risky to read properties from untrusted objects more than once?](#384-why-is-it-risky-to-read-properties-from-untrusted-objects-more-than-once)
- [385: What does "hardened JavaScript" (SES lockdown) do?](#385-what-does-hardened-javascript-ses-lockdown-do)
- [386: How do Trusted Types relate to the Factory pattern?](#386-how-do-trusted-types-relate-to-the-factory-pattern)
- [387: Why should a dynamic factory or loader never use raw user input as a module path?](#387-why-should-a-dynamic-factory-or-loader-never-use-raw-user-input-as-a-module-path)
- [388: How do you keep an event bus manageable in a large app?](#388-how-do-you-keep-an-event-bus-manageable-in-a-large-app)
- [389: What should you think about when designing the API of a reusable JavaScript library?](#389-what-should-you-think-about-when-designing-the-api-of-a-reusable-javascript-library)
- [390: How do you change a library's API without breaking users?](#390-how-do-you-change-a-librarys-api-without-breaking-users)
- [391: What are contract tests, and why are they useful for adapters?](#391-what-are-contract-tests-and-why-are-they-useful-for-adapters)
- [392: What is hexagonal architecture (ports and adapters)?](#392-what-is-hexagonal-architecture-ports-and-adapters)
- [393: What is a use case (interactor) in clean architecture, and how does it look in JavaScript?](#393-what-is-a-use-case-interactor-in-clean-architecture-and-how-does-it-look-in-javascript)
- [394: How can Domain-Driven Design ideas help a front-end codebase?](#394-how-can-domain-driven-design-ideas-help-a-front-end-codebase)
- [395: What is an anemic domain model?](#395-what-is-an-anemic-domain-model)
- [396: What is Feature-Sliced Design?](#396-what-is-feature-sliced-design)
- [397: How do you enforce module boundaries in a monorepo?](#397-how-do-you-enforce-module-boundaries-in-a-monorepo)
- [398: How does AsyncLocalStorage help with request context in Node.js?](#398-how-does-asynclocalstorage-help-with-request-context-in-nodejs)
- [399: What is the AsyncContext proposal?](#399-what-is-the-asynccontext-proposal)
- [400: How do generators relate to async/await?](#400-how-do-generators-relate-to-asyncawait)
- [401: What is trampolining?](#401-what-is-trampolining)
- [402: What is continuation-passing style (CPS)?](#402-what-is-continuation-passing-style-cps)
- [403: Are Promises monads, and what is a Maybe?](#403-are-promises-monads-and-what-is-a-maybe)
- [404: What is railway-oriented programming?](#404-what-is-railway-oriented-programming)
- [405: What is a lens?](#405-what-is-a-lens)
- [406: What are transducers?](#406-what-are-transducers)
- [407: How does Shadow DOM affect event delegation?](#407-how-does-shadow-dom-affect-event-delegation)
- [408: What are scoped custom element registries, and why do they matter?](#408-what-are-scoped-custom-element-registries-and-why-do-they-matter)
- [409: What are form-associated custom elements?](#409-what-are-form-associated-custom-elements)
- [410: What are the trade-offs of Proxy-based RPC clients like tRPC?](#410-what-are-the-trade-offs-of-proxy-based-rpc-clients-like-trpc)
- [411: Design an undo/redo system for a drawing app.](#411-design-an-undoredo-system-for-a-drawing-app)
- [412: Design an in-app notification system.](#412-design-an-in-app-notification-system)
- [413: Design a small form library. Which patterns would you use?](#413-design-a-small-form-library-which-patterns-would-you-use)
- [414: Design a data-fetching cache library like TanStack Query.](#414-design-a-data-fetching-cache-library-like-tanstack-query)
- [415: Design the plugin architecture for a rich text editor.](#415-design-the-plugin-architecture-for-a-rich-text-editor)
- [416: Design an analytics layer that supports several providers.](#416-design-an-analytics-layer-that-supports-several-providers)
- [417: How would you implement A/B experiments on top of feature flags?](#417-how-would-you-implement-ab-experiments-on-top-of-feature-flags)
- [418: Design a real-time collaborative to-do list.](#418-design-a-real-time-collaborative-to-do-list)
- [419: Design a modal manager for an app with nested dialogs.](#419-design-a-modal-manager-for-an-app-with-nested-dialogs)
- [420: Design a toast queue.](#420-design-a-toast-queue)
- [421: How would you build a minimal client-side router?](#421-how-would-you-build-a-minimal-client-side-router)
- [422: Design an internationalization (i18n) system.](#422-design-an-internationalization-i18n-system)
- [423: Design a permissions system for a front end.](#423-design-a-permissions-system-for-a-front-end)
- [424: Design a multi-step checkout wizard.](#424-design-a-multi-step-checkout-wizard)
- [425: Design an autocomplete component.](#425-design-an-autocomplete-component)
- [426: Design infinite scroll for a feed.](#426-design-infinite-scroll-for-a-feed)
- [427: Design a drag-and-drop system for a kanban board.](#427-design-a-drag-and-drop-system-for-a-kanban-board)
- [428: Design a theming system for a component library.](#428-design-a-theming-system-for-a-component-library)
- [429: Design a JavaScript SDK that third-party websites embed.](#429-design-a-javascript-sdk-that-third-party-websites-embed)
- [430: What is the command queue stub pattern used by analytics snippets?](#430-what-is-the-command-queue-stub-pattern-used-by-analytics-snippets)
- [431: How would you migrate a large app from a global event bus to a store?](#431-how-would-you-migrate-a-large-app-from-a-global-event-bus-to-a-store)
- [432: How would you move a jQuery app to a modern framework without a rewrite?](#432-how-would-you-move-a-jquery-app-to-a-modern-framework-without-a-rewrite)
- [433: Tests pass alone but fail when run together. A singleton is suspected. How do you fix it?](#433-tests-pass-alone-but-fail-when-run-together-a-singleton-is-suspected-how-do-you-fix-it)
- [434: Fifty dashboard widgets poll the same endpoint. How do you improve this?](#434-fifty-dashboard-widgets-poll-the-same-endpoint-how-do-you-improve-this)
- [435: How do you share one expensive subscription between many consumers?](#435-how-do-you-share-one-expensive-subscription-between-many-consumers)
- [436: In what order should you stack decorators like auth, retry, timeout and cache around an HTTP call?](#436-in-what-order-should-you-stack-decorators-like-auth-retry-timeout-and-cache-around-an-http-call)
- [437: How do you spot over-engineering with design patterns?](#437-how-do-you-spot-over-engineering-with-design-patterns)
- [438: When should you remove a pattern from a codebase?](#438-when-should-you-remove-a-pattern-from-a-codebase)
- [439: How do Node.js streams use patterns, and how should you connect them?](#439-how-do-nodejs-streams-use-patterns-and-how-should-you-connect-them)
- [440: How do you keep an Observer-based store fast with thousands of subscribers?](#440-how-do-you-keep-an-observer-based-store-fast-with-thousands-of-subscribers)
- [441: When should consumers subscribe by topic and when by selector?](#441-when-should-consumers-subscribe-by-topic-and-when-by-selector)
- [442: Why is equality for value objects awkward in JavaScript, and what can you do?](#442-why-is-equality-for-value-objects-awkward-in-javascript-and-what-can-you-do)
- [443: How might the pattern matching proposal change State and Strategy code?](#443-how-might-the-pattern-matching-proposal-change-state-and-strategy-code)
- [444: Why do Redux and similar tools require actions and state to be serializable?](#444-why-do-redux-and-similar-tools-require-actions-and-state-to-be-serializable)
- [445: What does time-travel debugging need from an app's architecture?](#445-what-does-time-travel-debugging-need-from-an-apps-architecture)
- [446: What are the risks of schema-driven (config-driven) UIs at scale?](#446-what-are-the-risks-of-schema-driven-config-driven-uis-at-scale)
- [447: How does error handling work in middleware chains?](#447-how-does-error-handling-work-in-middleware-chains)
- [448: How can you do dependency injection in React?](#448-how-can-you-do-dependency-injection-in-react)
- [449: How does TypeScript change the way you use design patterns in JavaScript?](#449-how-does-typescript-change-the-way-you-use-design-patterns-in-javascript)
- [450: How do you explain a pattern choice in a system design interview?](#450-how-do-you-explain-a-pattern-choice-in-a-system-design-interview)

---

# Easy Questions (1-150)

## 1: What is a design pattern?

A design pattern is a common, reusable solution to a problem that keeps coming up in software design. It is not a library or a piece of code you copy. It is more like a template that describes how to structure objects and functions to solve a certain kind of problem. You still have to write the code yourself and adapt it to your case.

## 2: Why should a JavaScript developer learn design patterns?

Patterns give you ready answers to problems other people have already solved many times, so you don't have to invent everything from scratch. They also give the team a shared vocabulary: saying "this is an observer" or "use a factory here" is faster than explaining the whole idea. And they help you read existing code, because frameworks and libraries use these patterns all the time.

## 3: What is the "Gang of Four" book?

"Design Patterns: Elements of Reusable Object-Oriented Software" was published in 1994 by Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides. People call the authors the Gang of Four (GoF). The book describes 23 patterns, written with C++ and Smalltalk examples. Most of them still apply to JavaScript, but some look very different or become much simpler because JavaScript has first-class functions and dynamic objects.

## 4: What are the three main categories of design patterns?

- **Creational** patterns deal with how objects are created (Factory, Abstract Factory, Builder, Prototype, Singleton).
- **Structural** patterns deal with how objects are put together (Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy).
- **Behavioral** patterns deal with how objects talk to each other and share work (Observer, Strategy, Command, Iterator, State, Mediator, Chain of Responsibility, Template Method, Memento, Visitor, Interpreter).

## 5: What is an anti-pattern?

An anti-pattern is a common solution that looks fine at first but causes problems later. Examples in JavaScript are polluting the global scope, "callback hell", god objects that do everything, and extending built-in prototypes like `Array.prototype`. Knowing anti-patterns is as useful as knowing patterns, because it helps you spot bad code during reviews.

## 6: Are design patterns specific to one language?

No. The ideas are language independent, but the way you implement them depends on the language. In Java you might need several classes and interfaces for a Strategy pattern. In JavaScript you can often just pass a function. So some patterns become almost invisible in JavaScript, while others (like Module or Mixin) are more common in JavaScript than in classic OOP languages.

## 7: Can using design patterns make code worse?

Yes. If you add a pattern where the problem doesn't need it, you get extra layers, more files and code that is harder to follow. A common mistake is wrapping a simple function call in a factory, a strategy and an adapter "just in case". Use a pattern when you actually have the problem it solves, not because it looks professional.

## 8: What is the Module pattern?

The Module pattern groups related code together and hides private details, exposing only a public API. Before ES modules, it was built with a closure, usually an IIFE:

```js
const counter = (function () {
  let count = 0; // private

  return {
    increment() {
      count++;
      return count;
    },
    reset() {
      count = 0;
    },
  };
})();

counter.increment(); // 1
counter.count; // undefined
```

Today ES modules give you the same thing at the file level.

## 9: What is an IIFE?

An IIFE (Immediately Invoked Function Expression) is a function that runs as soon as it is defined. It creates its own scope, so variables inside it don't leak into the global scope.

```js
(function () {
  const secret = "hidden";
  console.log("runs right away");
})();
```

IIFEs were the main way to build modules before ES modules. You still see them in older code and in some bundler output.

## 10: What is the Revealing Module pattern?

It is a version of the Module pattern where you write all functions as private ones and then return an object that "reveals" the ones you want public. This makes it easy to see the public API in one place at the bottom.

```js
const userStore = (function () {
  const users = [];

  function add(user) {
    users.push(user);
  }

  function getAll() {
    return [...users];
  }

  return { add, getAll };
})();
```

## 11: How do ES modules relate to the Module pattern?

ES modules (`import` / `export`) are the built-in version of the Module pattern. Every file has its own scope. Anything you don't export stays private to that file.

```js
// counter.js
let count = 0;

export function increment() {
  return ++count;
}
```

You don't need IIFEs or closures for privacy anymore. The module system handles it for you.

## 12: What is the Singleton pattern?

A Singleton makes sure a class has only one instance and gives a single place to access it. Common examples are a config object, a logger, or a connection to a database.

```js
class Config {
  static #instance;

  static getInstance() {
    if (!Config.#instance) {
      Config.#instance = new Config();
    }
    return Config.#instance;
  }
}

Config.getInstance() === Config.getInstance(); // true
```

## 13: What is the simplest way to create a singleton in modern JavaScript?

Export an instance from an ES module. A module is evaluated only once, and every file that imports it gets the same object.

```js
// logger.js
class Logger {
  log(msg) {
    console.log(`[app] ${msg}`);
  }
}

export const logger = new Logger();
```

Any file that does `import { logger } from "./logger.js"` gets the same instance.

## 14: Why do many people call the Singleton an anti-pattern?

A singleton is basically global state with a nicer name. It makes hidden dependencies (code reaches for it instead of receiving it), it is hard to replace in tests, and state can leak between tests because the instance survives. It is fine for things that really are one per app, like a logger, but it is often overused.

## 15: What is the Factory pattern?

A Factory is a function or method that creates objects for you, so the calling code doesn't need to know which class to use or how to set it up.

```js
function createUser(type, name) {
  if (type === "admin") return new Admin(name);
  if (type === "guest") return new Guest(name);
  return new User(name);
}

const u = createUser("admin", "Ana");
```

## 16: What is a factory function in JavaScript?

A factory function is any regular function that returns a new object. It doesn't use `new` or `this`.

```js
function createPoint(x, y) {
  return {
    x,
    y,
    distanceTo(other) {
      return Math.hypot(other.x - x, other.y - y);
    },
  };
}

const p = createPoint(0, 0);
```

It is very common in JavaScript because it is simple and can use closures for private data.

## 17: What is the difference between a factory function and a class?

A class is called with `new`, uses `this`, and shares methods through the prototype. A factory function is called like a normal function, can hide data in a closure, and has no `this` problems. Classes use less memory when you create many objects, because methods live on the prototype. Factories are more flexible: they can return different kinds of objects, cached objects, or plain objects.

## 18: What is the Constructor pattern?

It is the pattern of using a function (or class) with the `new` keyword to create and set up objects. Before ES6 classes, you wrote constructor functions:

```js
function Car(model) {
  this.model = model;
}

Car.prototype.drive = function () {
  return `${this.model} is driving`;
};

const car = new Car("Civic");
```

Today you would write the same thing with `class`, which is mostly syntax over this same mechanism.

## 19: What is the Prototype pattern?

The Prototype pattern creates new objects by copying or linking to an existing object instead of building them from a class. JavaScript is built on this idea: every object has a prototype it inherits from.

```js
const animal = {
  speak() {
    return `${this.name} makes a sound`;
  },
};

const dog = Object.create(animal);
dog.name = "Rex";
dog.speak(); // "Rex makes a sound"
```

## 20: What does Object.create() do?

`Object.create(proto)` makes a new empty object whose prototype is `proto`. It is the most direct way to use prototypal inheritance without classes or constructor functions. `Object.create(null)` creates an object with no prototype at all, which is useful for simple dictionaries that should not inherit things like `toString`.

## 21: What is the Observer pattern?

In the Observer pattern, an object (the subject) keeps a list of other objects or functions (observers) and notifies them when something changes. Observers can subscribe and unsubscribe.

```js
class Subject {
  #observers = new Set();

  subscribe(fn) {
    this.#observers.add(fn);
    return () => this.#observers.delete(fn);
  }

  notify(data) {
    this.#observers.forEach((fn) => fn(data));
  }
}

const s = new Subject();
const unsubscribe = s.subscribe((d) => console.log("got", d));
s.notify(42);
unsubscribe();
```

## 22: Where do you see the Observer pattern in the browser?

DOM events are the most common example. `addEventListener` subscribes a function, and the element notifies it when the event fires. `removeEventListener` unsubscribes. Other examples are `MutationObserver`, `IntersectionObserver`, `ResizeObserver` and `EventTarget` in general.

## 23: What is the Publish/Subscribe (Pub/Sub) pattern?

Pub/Sub is similar to Observer, but publishers and subscribers don't know about each other. They both talk to a middle piece (an event bus or broker) using topic names.

```js
const bus = {
  topics: {},
  subscribe(topic, fn) {
    (this.topics[topic] ??= []).push(fn);
  },
  publish(topic, data) {
    (this.topics[topic] ?? []).forEach((fn) => fn(data));
  },
};

bus.subscribe("user:login", (u) => console.log("welcome", u.name));
bus.publish("user:login", { name: "Ana" });
```

## 24: What is the difference between Observer and Pub/Sub?

In Observer, the subject holds direct references to its observers and calls them itself. In Pub/Sub, there is a channel or broker between them, so the publisher doesn't know who listens and the subscriber doesn't know who publishes. Pub/Sub gives looser coupling but makes the flow harder to trace, because you can't see from the code who reacts to a message.

## 25: What is the Decorator pattern?

The Decorator pattern adds new behavior to an object or function by wrapping it, without changing the original code.

```js
function withLogging(fn) {
  return function (...args) {
    console.log("calling with", args);
    return fn.apply(this, args);
  };
}

const add = (a, b) => a + b;
const loggedAdd = withLogging(add);
loggedAdd(2, 3); // logs, then returns 5
```

## 26: What is the Facade pattern?

A Facade gives a simple interface to a more complex system. The caller uses one easy function instead of dealing with many lower-level calls.

```js
const api = {
  async getUser(id) {
    const res = await fetch(`/api/users/${id}`, {
      headers: { Accept: "application/json" },
    });
    if (!res.ok) throw new Error(`Request failed: ${res.status}`);
    return res.json();
  },
};

const user = await api.getUser(1);
```

jQuery is a famous facade over the DOM APIs of its time.

## 27: What is the Adapter pattern?

An Adapter converts one interface into another one that the calling code expects. It lets two pieces of code work together without changing either of them.

```js
// old API returns { first_name, last_name }
function adaptUser(apiUser) {
  return {
    firstName: apiUser.first_name,
    lastName: apiUser.last_name,
  };
}
```

You use adapters a lot when you wrap third-party libraries or backend responses.

## 28: What is the Proxy pattern?

A Proxy is an object that stands in front of another object and controls access to it. It can add checks, caching, logging or lazy loading while the caller thinks it is talking to the real object. JavaScript has a built-in `Proxy` class for this:

```js
const user = { name: "Ana" };

const logged = new Proxy(user, {
  get(target, prop, receiver) {
    console.log(`reading ${String(prop)}`);
    return Reflect.get(target, prop, receiver);
  },
});

logged.name; // logs "reading name"
```

## 29: What is the Strategy pattern?

Strategy lets you pick an algorithm at runtime. You define a group of interchangeable functions and pass the one you need.

```js
const shipping = {
  standard: (weight) => weight * 1.5,
  express: (weight) => weight * 3,
  free: () => 0,
};

function shippingCost(method, weight) {
  return shipping[method](weight);
}

shippingCost("express", 2); // 6
```

In JavaScript a strategy is usually just a function.

## 30: What is the Command pattern?

The Command pattern turns a request into an object. That object holds everything needed to run the action later, so you can queue it, log it, or undo it.

```js
const commands = [];

function addItem(list, item) {
  return {
    execute: () => list.push(item),
    undo: () => list.pop(),
  };
}

const list = [];
const cmd = addItem(list, "milk");
cmd.execute();
commands.push(cmd);
commands.pop().undo(); // list is empty again
```

## 31: What is the Iterator pattern?

The Iterator pattern gives a way to go through the items of a collection one by one, without exposing how the collection is stored. In JavaScript it is built into the language through the iteration protocol: any object with a `[Symbol.iterator]()` method can be used with `for...of`, spread and destructuring.

## 32: How do you make an object iterable?

Add a `[Symbol.iterator]` method that returns an iterator. A generator is the easiest way:

```js
class Range {
  constructor(from, to) {
    this.from = from;
    this.to = to;
  }

  *[Symbol.iterator]() {
    for (let i = this.from; i <= this.to; i++) yield i;
  }
}

[...new Range(1, 3)]; // [1, 2, 3]
```

## 33: What is the State pattern?

The State pattern lets an object change its behavior when its internal state changes. Instead of big `if` or `switch` blocks, each state is its own object with its own behavior.

```js
const states = {
  idle: { start: () => "loading" },
  loading: { succeed: () => "done", fail: () => "error" },
  done: {},
  error: { retry: () => "loading" },
};

let current = "idle";

function send(event) {
  const next = states[current][event]?.();
  if (next) current = next;
}

send("start"); // current = "loading"
```

## 34: What is the Mediator pattern?

A Mediator is a central object that handles communication between other objects, so they don't talk to each other directly. Instead of every component knowing about every other component, they all only know the mediator. A chat room where users send messages through the room, not to each other, is the classic example.

## 35: What is the Chain of Responsibility pattern?

A request is passed along a chain of handlers. Each handler decides to process it, pass it to the next one, or both. Express middleware is a well-known example:

```js
app.use((req, res, next) => {
  console.log(req.method, req.url);
  next(); // pass to the next handler
});
```

## 36: What is the Template Method pattern?

A base class defines the steps of an algorithm in one method and lets subclasses fill in some of those steps.

```js
class Report {
  generate() {
    return [this.header(), this.body(), this.footer()].join("\n");
  }
  header() {
    return "REPORT";
  }
  footer() {
    return "END";
  }
}

class SalesReport extends Report {
  body() {
    return "Sales: 100";
  }
}

new SalesReport().generate();
```

## 37: What is the Builder pattern?

A Builder creates a complex object step by step, usually with chained method calls, and returns the final object at the end with a `build()` call.

```js
class RequestBuilder {
  #config = { method: "GET", headers: {} };

  url(u) {
    this.#config.url = u;
    return this;
  }
  method(m) {
    this.#config.method = m;
    return this;
  }
  header(k, v) {
    this.#config.headers[k] = v;
    return this;
  }
  build() {
    return { ...this.#config };
  }
}

const req = new RequestBuilder().url("/api").method("POST").build();
```

## 38: What is the Composite pattern?

Composite lets you treat a single object and a group of objects the same way. It is used for tree structures, where a node can be a leaf or a container of other nodes. The DOM is a composite: an element can contain other elements, and you call the same methods on both.

## 39: What is the Flyweight pattern?

Flyweight saves memory by sharing data between many similar objects instead of storing a copy in each one. For example, in a text editor every letter "a" can share one object with the font data, and only the position is stored per character.

## 40: What is the Memento pattern?

Memento saves a snapshot of an object's state so you can restore it later, without exposing the object's internals. It is the base for undo features.

```js
class Editor {
  #text = "";
  type(t) {
    this.#text += t;
  }
  save() {
    return { text: this.#text };
  }
  restore(memento) {
    this.#text = memento.text;
  }
}
```

## 41: What is the Mixin pattern?

A mixin is an object with methods that you copy into another class or object to add behavior, without using inheritance.

```js
const canFly = {
  fly() {
    return `${this.name} flies`;
  },
};

class Bird {
  constructor(name) {
    this.name = name;
  }
}

Object.assign(Bird.prototype, canFly);
new Bird("Tweety").fly();
```

## 42: What is "composition over inheritance"?

It means building objects by combining small pieces of behavior instead of creating deep class hierarchies. With inheritance, a change in a base class can break many subclasses, and you can only extend one class. With composition, you pick the exact behaviors you need and combine them. Most JavaScript code (and React since hooks) prefers composition.

## 43: What is the MVC pattern?

MVC (Model-View-Controller) splits an app into three parts:

- **Model**: the data and business rules.
- **View**: what the user sees.
- **Controller**: handles user input and updates the model and view.

The goal is to keep data logic separate from UI code. Many back-end frameworks (like Express apps organized into controllers) and older front-end frameworks (like Backbone) follow it.

## 44: What is the MVVM pattern?

MVVM (Model-View-ViewModel) is like MVC, but the ViewModel exposes data and commands that the View binds to directly. When the ViewModel changes, the View updates automatically through data binding. Vue, Knockout and Angular templates are close to this model.

## 45: What is the difference between MVC and MVP?

In MVP (Model-View-Presenter), the View is passive: it doesn't read the model, and the Presenter updates it directly through a View interface. In MVC, the View can read from the Model and the Controller mainly handles input. MVP makes the View easier to swap and the Presenter easier to test, since the Presenter talks to an interface, not real UI.

## 46: What is dependency injection?

Dependency injection means a function or class receives the things it needs (its dependencies) from outside instead of creating them itself.

```js
class UserService {
  constructor(httpClient) {
    this.http = httpClient;
  }

  getUser(id) {
    return this.http.get(`/users/${id}`);
  }
}

const service = new UserService(fakeHttpClient); // easy to test
```

## 47: Why is dependency injection useful?

It makes code easier to test, because you can pass fake versions of dependencies. It also makes code more flexible: you can switch from one HTTP client or storage to another without changing the class. And it makes dependencies visible, since you can see everything a class needs by looking at its constructor.

## 48: What is the Null Object pattern?

Instead of returning `null` and checking for it everywhere, you return an object with the same interface that does nothing.

```js
const nullLogger = {
  log() {},
  error() {},
};

function createService(logger = nullLogger) {
  return {
    run() {
      logger.log("running"); // no need for "if (logger)"
    },
  };
}
```

## 49: What is method chaining?

Method chaining is when each method returns an object (often `this`) so you can call another method right after it on the same line.

```js
const result = [5, 1, 4]
  .filter((n) => n > 1)
  .map((n) => n * 2)
  .sort((a, b) => a - b);
```

Array methods, jQuery, Promises and builders all use chaining.

## 50: How do you make your own class support method chaining?

Return `this` from every method that changes the object.

```js
class Calculator {
  #value = 0;

  add(n) {
    this.#value += n;
    return this;
  }
  multiply(n) {
    this.#value *= n;
    return this;
  }
  get result() {
    return this.#value;
  }
}

new Calculator().add(2).multiply(5).result; // 10
```

## 51: How do closures help with design patterns?

A closure is a function that remembers the variables from the scope where it was created. Many patterns depend on this: the Module pattern uses it for private state, factory functions use it to hide data, decorators use it to keep a reference to the wrapped function, and memoization uses it to keep a cache.

```js
function createCounter() {
  let count = 0;
  return () => ++count;
}

const next = createCounter();
next(); // 1
next(); // 2
```

## 52: How do you create private data in a class?

Use private fields and methods with the `#` prefix. They can only be accessed inside the class body.

```js
class BankAccount {
  #balance = 0;

  deposit(amount) {
    this.#balance += amount;
  }

  get balance() {
    return this.#balance;
  }
}

const acc = new BankAccount();
acc.deposit(100);
acc.balance; // 100
acc.#balance; // SyntaxError
```

Before private fields, people used closures, `WeakMap`s, or the `_name` naming convention (which is not really private).

## 53: What are getters and setters used for in patterns?

Getters and setters let you run code when a property is read or written, while the caller still uses normal property syntax. You use them to compute values, validate input, or notify observers when a value changes.

```js
class Temperature {
  #celsius = 0;

  get fahrenheit() {
    return this.#celsius * 1.8 + 32;
  }

  set celsius(value) {
    if (typeof value !== "number") throw new TypeError("Not a number");
    this.#celsius = value;
  }
}
```

## 54: What is the Namespace pattern?

Before modules, people grouped code under one global object to avoid name collisions:

```js
var MyApp = MyApp || {};
MyApp.utils = {
  formatDate(d) {
    /* ... */
  },
};
MyApp.models = {};
```

Only `MyApp` lives in the global scope. This is a legacy pattern. With ES modules you don't need it, but you will still see it in old codebases and in libraries that ship a browser global (like `window.Sentry`).

## 55: What is the Options Object (configuration object) pattern?

Instead of a long list of positional arguments, a function takes one object with named options.

```js
function createModal({ title, width = 400, closable = true } = {}) {
  return { title, width, closable };
}

createModal({ title: "Hello", closable: false });
```

The call is easier to read, the order of options doesn't matter, and you can add new options later without breaking existing callers.

## 56: What is memoization?

Memoization caches the result of a function for a given input, so the next call with the same input returns the cached result instead of doing the work again.

```js
function memoize(fn) {
  const cache = new Map();
  return (arg) => {
    if (!cache.has(arg)) cache.set(arg, fn(arg));
    return cache.get(arg);
  };
}

const slowSquare = (n) => n * n;
const fastSquare = memoize(slowSquare);
```

It only works correctly for pure functions, where the same input always gives the same output.

## 57: What is debouncing?

Debouncing delays a function call until some time has passed since the last call. If the function is called again before that, the timer restarts. It is used for things like search inputs, where you only want to send a request after the user stops typing.

```js
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

input.addEventListener("input", debounce(search, 300));
```

## 58: What is throttling?

Throttling makes sure a function runs at most once in a given time window, no matter how often it is called. It is used for scroll, resize or mousemove handlers.

```js
function throttle(fn, wait) {
  let last = 0;
  return function (...args) {
    const now = Date.now();
    if (now - last >= wait) {
      last = now;
      fn.apply(this, args);
    }
  };
}

window.addEventListener("scroll", throttle(updateHeader, 100));
```

## 59: What is the difference between debounce and throttle?

Debounce waits until calls stop, then runs once. Throttle runs regularly while calls keep coming, but not more often than the limit. For a search box you want debounce (run after typing stops). For tracking scroll position you want throttle (update every 100 ms while scrolling).

## 60: What is currying?

Currying turns a function that takes several arguments into a chain of functions that each take one argument.

```js
const add = (a) => (b) => (c) => a + b + c;

add(1)(2)(3); // 6

const addTen = add(10);
addTen(5)(1); // 16
```

It is useful for creating specialized functions from general ones.

## 61: What is partial application?

Partial application fixes some arguments of a function and returns a new function that takes the rest. Unlike currying, the new function can take several arguments at once.

```js
function greet(greeting, name) {
  return `${greeting}, ${name}!`;
}

const sayHello = greet.bind(null, "Hello");
sayHello("Ana"); // "Hello, Ana!"
```

## 62: What is a higher-order function?

A higher-order function either takes a function as an argument, returns a function, or both. `map`, `filter`, `reduce`, `setTimeout` and `addEventListener` take functions. Decorators, `debounce` and `memoize` return functions. Higher-order functions are the reason many OOP patterns are so short in JavaScript.

## 63: What is the callback pattern?

A callback is a function you pass to another function so it can be called later, usually when some work is done.

```js
function loadData(callback) {
  setTimeout(() => callback({ id: 1 }), 100);
}

loadData((data) => console.log(data));
```

Callbacks were the main way to handle async code before Promises.

## 64: What are error-first callbacks?

It is a Node.js convention where the first argument of a callback is an error (or `null`), and the result comes after it.

```js
import fs from "node:fs";

fs.readFile("data.txt", "utf8", (err, text) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(text);
});
```

Modern Node.js code usually uses the promise versions instead, like `fs/promises`.

## 65: What is "callback hell"?

Callback hell is when async callbacks are nested inside each other many levels deep. The code drifts to the right, is hard to read, and error handling is repeated at every level. Promises and async/await fix this by letting you write async steps one after another.

## 66: How are Promises a design pattern?

A Promise is an object that stands for a value that will be available later. It follows a simple state machine (pending, then fulfilled or rejected, and it can only settle once) and supports chaining with `.then()`. It replaces nested callbacks with a flat chain and gives one place for error handling with `.catch()`.

## 67: How do you run several async tasks in parallel?

Start them all, then wait with `Promise.all`:

```js
const [user, posts] = await Promise.all([
  fetch("/api/user").then((r) => r.json()),
  fetch("/api/posts").then((r) => r.json()),
]);
```

`Promise.all` rejects as soon as one promise fails. Use `Promise.allSettled` if you want all results, including failures.

## 68: What is the EventEmitter in Node.js?

`EventEmitter` from `node:events` is Node's built-in Observer implementation. Many core objects, like streams and HTTP servers, extend it.

```js
import { EventEmitter } from "node:events";

class Order extends EventEmitter {}

const order = new Order();
order.on("paid", (amount) => console.log("paid", amount));
order.emit("paid", 50);
```

## 69: How do you create custom events in the browser?

Use `EventTarget` and `CustomEvent`. You can even extend `EventTarget` in your own classes.

```js
class Cart extends EventTarget {
  add(item) {
    this.dispatchEvent(new CustomEvent("added", { detail: item }));
  }
}

const cart = new Cart();
cart.addEventListener("added", (e) => console.log(e.detail));
cart.add({ id: 1 });
```

## 70: What is lazy initialization?

Lazy initialization delays creating an object or computing a value until it is first needed. This saves time and memory when the value might never be used.

```js
class Report {
  #data;

  get data() {
    this.#data ??= expensiveCalculation();
    return this.#data;
  }
}
```

## 71: How do you create an enum in JavaScript?

JavaScript has no built-in enum, so you use a frozen object:

```js
const Status = Object.freeze({
  ACTIVE: "active",
  INACTIVE: "inactive",
  BANNED: "banned",
});

if (user.status === Status.ACTIVE) {
  /* ... */
}
```

`Object.freeze` stops anyone from adding or changing values. Some people use `Symbol` values so that each enum value is unique.

## 72: What does Object.freeze() do?

It makes an object read-only: you can't add, remove or change its properties. In strict mode (which includes ES modules and classes), trying to change it throws a `TypeError`. In sloppy mode the change is silently ignored. Freezing is shallow: nested objects are still mutable unless you freeze them too.

## 73: What is the Abstract Factory pattern?

An Abstract Factory creates families of related objects without naming their concrete classes. For example, a UI theme factory might create a button, an input and a modal that all match the same theme.

```js
const darkTheme = {
  createButton: () => ({ color: "white", bg: "black" }),
  createInput: () => ({ border: "gray" }),
};

const lightTheme = {
  createButton: () => ({ color: "black", bg: "white" }),
  createInput: () => ({ border: "silver" }),
};

function renderForm(factory) {
  return [factory.createInput(), factory.createButton()];
}
```

## 74: What is the Bridge pattern?

Bridge splits a large piece of code into two separate parts, the abstraction and the implementation, so you can change each one on its own. For example, a `Notification` (abstraction) can be sent through an `EmailSender` or an `SmsSender` (implementation). Without the bridge you would need classes like `UrgentEmailNotification`, `UrgentSmsNotification` and so on for every combination.

## 75: What is the Visitor pattern?

Visitor lets you add new operations to a set of objects without changing those objects. The operation lives in a separate "visitor" object that has a method for each type of node. It is common in compilers and tools like Babel and ESLint, where plugins visit nodes of a syntax tree.

```js
const visitor = {
  Identifier(node) {
    console.log("found identifier", node.name);
  },
};
```

## 76: What is the Interpreter pattern?

Interpreter defines a grammar for a small language and a way to evaluate sentences in it. Each grammar rule becomes an object or function that knows how to evaluate itself. Template engines, query languages and math expression evaluators use it. You don't write this often in front-end work, but it is good to know what it means.

## 77: What is a higher-order component (HOC) in React?

A HOC is a function that takes a component and returns a new component with extra behavior. It is the Decorator pattern applied to components.

```jsx
function withLoading(Component) {
  return function WithLoading({ isLoading, ...props }) {
    if (isLoading) return <p>Loading...</p>;
    return <Component {...props} />;
  };
}

const UserListWithLoading = withLoading(UserList);
```

Today custom hooks are usually preferred, but you still see HOCs in older code and some libraries.

## 78: What is the render props pattern?

A component receives a function as a prop and calls it to decide what to render. This lets the component share logic while the caller controls the markup.

```jsx
function MouseTracker({ render }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return (
    <div onMouseMove={(e) => setPos({ x: e.clientX, y: e.clientY })}>
      {render(pos)}
    </div>
  );
}

<MouseTracker
  render={({ x, y }) => (
    <p>
      {x}, {y}
    </p>
  )}
/>;
```

Like HOCs, it has mostly been replaced by custom hooks.

## 79: What is the hooks pattern in React?

Hooks are functions like `useState` and `useEffect` that let function components use state and side effects. Custom hooks let you pull reusable logic out of components:

```jsx
function useOnlineStatus() {
  const [online, setOnline] = useState(navigator.onLine);
  useEffect(() => {
    const on = () => setOnline(true);
    const off = () => setOnline(false);
    window.addEventListener("online", on);
    window.addEventListener("offline", off);
    return () => {
      window.removeEventListener("online", on);
      window.removeEventListener("offline", off);
    };
  }, []);
  return online;
}
```

Hooks are composition: you build behavior by calling small functions together.

## 80: What is the Container/Presentational pattern?

It splits components into two kinds:

- **Container** components fetch data and manage state.
- **Presentational** components only receive props and render UI.

This keeps UI components simple and reusable. With hooks, the logic is often moved into a custom hook instead of a separate container component, but the idea of separating data from display is still useful.

## 81: What is the Provider pattern?

The Provider pattern makes data available to many components in a tree without passing props through every level. In React it is done with Context:

```jsx
const ThemeContext = createContext("light");

function App() {
  return (
    <ThemeContext value="dark">
      <Toolbar />
    </ThemeContext>
  );
}

function Button() {
  const theme = use(ThemeContext);
  return <button className={theme}>OK</button>;
}
```

In React 19 you can render the context itself as a provider and read it with `use` or `useContext`. Older code uses `<ThemeContext.Provider>`.

## 82: What is Flux?

Flux is an architecture Facebook introduced for React apps. Data flows in one direction: actions go to a dispatcher, the dispatcher updates stores, and stores notify views, which can create new actions. Redux and many other state libraries are based on this idea.

## 83: What is unidirectional data flow?

It means data moves in one direction through the app. State lives in one place, the UI renders from that state, and the UI can only change the state by sending events or actions. This makes it easier to understand why something changed, compared with two-way binding where any part can change any other part.

## 84: Which patterns does Redux use?

- **Singleton-like store**: one store for the app state.
- **Observer**: components subscribe to store changes.
- **Command**: actions are plain objects describing what happened.
- **Reducer** (a pure function): computes the next state from the current state and an action.
- **Middleware** (Chain of Responsibility): every action passes through a chain before reaching the reducer.

## 85: What is a pure function?

A pure function always returns the same output for the same input and has no side effects (it doesn't change outside variables, the DOM, or make network calls).

```js
// pure
const add = (a, b) => a + b;

// impure
let total = 0;
const addToTotal = (n) => (total += n);
```

Pure functions are easy to test, cache and reason about.

## 86: Why is immutability important in some patterns?

When you never change data in place and create new objects instead, you can tell if something changed by comparing references (`a !== b`). This is how React, Redux and many memoization tools detect changes quickly. It also prevents bugs where one part of the code changes an object another part still uses.

```js
const next = { ...state, count: state.count + 1 };
```

## 87: What does SOLID stand for?

- **S**ingle Responsibility: a module should have one reason to change.
- **O**pen/Closed: code should be open for extension but closed for modification.
- **L**iskov Substitution: a subtype should work anywhere its base type is expected.
- **I**nterface Segregation: don't force code to depend on methods it doesn't use.
- **D**ependency Inversion: depend on abstractions, not on concrete details.

## 88: What is the Single Responsibility Principle in practice?

Each function, class or module should do one job. For example, a function that fetches users, filters them and renders HTML has three reasons to change. Splitting it into `fetchUsers`, `filterActive` and `renderUsers` makes each part easier to test and reuse.

## 89: What is the Open/Closed Principle in JavaScript?

You should be able to add new behavior without editing existing, working code. A lookup of strategies is a simple example:

```js
const formatters = {
  json: (data) => JSON.stringify(data),
  csv: (data) => data.map((row) => row.join(",")).join("\n"),
};

function exportData(format, data) {
  return formatters[format](data);
}

// adding XML means adding a new entry, not changing exportData
formatters.xml = (data) => toXml(data);
```

## 90: What are DRY, KISS and YAGNI?

- **DRY** (Don't Repeat Yourself): keep each piece of knowledge in one place.
- **KISS** (Keep It Simple, Stupid): choose the simplest solution that works.
- **YAGNI** (You Aren't Gonna Need It): don't build features or abstractions until you actually need them.

YAGNI and KISS are good reminders not to add design patterns too early.

## 91: What is separation of concerns?

It means splitting a program into parts where each part handles one area, like data access, business logic and UI. HTML/CSS/JS, MVC layers, and services vs components are all examples. It makes code easier to change, because a change in one area doesn't spread everywhere.

## 92: What is the difference between coupling and cohesion?

Coupling is how much one module depends on another. Cohesion is how closely the code inside one module belongs together. You want **low coupling** (modules can change without breaking each other) and **high cohesion** (each module has a clear, focused purpose). Most design patterns aim for one or both.

## 93: What is a guard clause?

A guard clause checks for a bad case at the start of a function and returns early, so the main logic doesn't sit inside nested `if` blocks.

```js
function getDiscount(user) {
  if (!user) return 0;
  if (!user.isMember) return 0;
  return user.years > 5 ? 0.2 : 0.1;
}
```

## 94: How can you replace a long switch statement with an object?

Use an object (or `Map`) as a lookup table:

```js
const handlers = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
};

function calculate(op, a, b) {
  const handler = handlers[op];
  if (!handler) throw new Error(`Unknown operation: ${op}`);
  return handler(a, b);
}
```

This is a simple form of the Strategy pattern and makes adding new cases easy.

## 95: What is the Registry pattern?

A registry is a central place where you register things by name and look them up later. Plugins, components, commands and validators are often stored this way.

```js
const validators = new Map();

function registerValidator(name, fn) {
  validators.set(name, fn);
}

registerValidator("email", (v) => v.includes("@"));
validators.get("email")("a@b.com"); // true
```

`customElements.define()` for Web Components is a registry built into the browser.

## 96: What is the Plugin pattern?

A plugin system lets other code add features to your app or library without changing its core. The core exposes hooks or an API, and plugins register themselves with it. Vite, Rollup, Babel, ESLint and webpack are all built around plugins.

```js
class App {
  #plugins = [];
  use(plugin) {
    plugin.install(this);
    this.#plugins.push(plugin);
    return this;
  }
}
```

## 97: What is the Middleware pattern?

Middleware is a chain of functions that each get a request (or action), can do something with it, and then pass it to the next function. It is a form of Chain of Responsibility. Express, Koa, Redux and many HTTP clients use middleware for logging, auth, error handling and similar shared tasks.

## 98: What is "polluting the global scope" and why is it bad?

It means creating variables on the global object (`window` in browsers) by accident, for example by forgetting `let`/`const` in sloppy mode or declaring top-level `var` in a classic script. Different scripts can then overwrite each other's variables, which causes hard-to-find bugs. Modules, IIFEs and strict mode all help prevent this.

## 99: What is a "god object"?

A god object is a class or module that knows too much and does too much: it handles data, UI, network calls and business rules all at once. It is hard to test, hard to change and becomes a bottleneck for the team. The fix is to split it into smaller pieces with single responsibilities.

## 100: Why is extending built-in prototypes considered bad practice?

Adding methods to `Array.prototype`, `String.prototype` and similar objects affects every piece of code on the page, including libraries. If a future JavaScript version adds a method with the same name but different behavior, your code or other code can break. This has actually happened: `Array.prototype.flatten` was renamed to `flat` because an old library (MooTools) had added a conflicting `flatten`.

## 101: Are JavaScript classes real classes like in Java?

Not exactly. A JavaScript class is mostly syntax on top of constructor functions and prototypes. Methods are still stored on the prototype object, and instances still inherit through the prototype chain. Classes do add real features though: private fields (`#x`), static blocks, `super`, and they throw if you call them without `new`.

```js
class User {}
typeof User; // "function"
```

## 102: How does inheritance work with extends?

`extends` sets up the prototype chain so the child class inherits methods from the parent. In the child constructor you must call `super()` before using `this`.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  speak() {
    return `${super.speak()} (woof)`;
  }
}

new Dog("Rex").speak(); // "Rex makes a sound (woof)"
```

## 103: What is a static method and how is it used in patterns?

A static method belongs to the class itself, not to its instances. It is often used for factory methods, singletons and helper functions related to the class.

```js
class Color {
  constructor(r, g, b) {
    Object.assign(this, { r, g, b });
  }

  static fromHex(hex) {
    const n = parseInt(hex.slice(1), 16);
    return new Color((n >> 16) & 255, (n >> 8) & 255, n & 255);
  }
}

Color.fromHex("#ff0000");
```

## 104: What is the Factory Method pattern?

In the GoF version, a base class defines a method for creating an object, and subclasses override it to decide which object to create. In JavaScript the term is also used for static methods that create instances in different ways, like `Array.from()`, `Array.of()`, `Object.fromEntries()` or `Promise.resolve()`. They give the creation a clear name and can hide extra setup.

## 105: What is the prototype chain?

Every object has an internal link to another object, its prototype. When you read a property that the object doesn't have, JavaScript looks it up on the prototype, then the prototype's prototype, and so on until it reaches `null`.

```js
const arr = [];
// arr -> Array.prototype -> Object.prototype -> null
arr.hasOwnProperty("length"); // found on Object.prototype
```

This chain is how inheritance, mixins and the Prototype pattern work in JavaScript.

## 106: How do you copy an object in JavaScript?

- Spread or `Object.assign` for a shallow copy: `const copy = { ...obj }`.
- `structuredClone(obj)` for a deep copy of plain data (it supports dates, maps, sets and circular references, but not functions, DOM nodes or class prototypes).

```js
const original = { user: { name: "Ana" }, tags: new Set(["a"]) };
const deep = structuredClone(original);
deep.user.name = "Bob";
original.user.name; // still "Ana"
```

Copying is the basic step in the Prototype pattern and in immutable updates.

## 107: What is event delegation?

Event delegation means attaching one listener to a parent element instead of one listener per child. The event bubbles up from the child, and you check `event.target` to see which child was clicked.

```js
document.querySelector("#list").addEventListener("click", (e) => {
  const item = e.target.closest("li");
  if (item) console.log("clicked", item.dataset.id);
});
```

It uses less memory and works for children that are added later.

## 108: What is an Observable?

An Observable (popularized by RxJS) represents a stream of values over time. You subscribe to it and get notified on each new value, on error and on completion. It is the Observer pattern plus the Iterator pattern: values are pushed to you one by one, and you can transform the stream with operators like `map`, `filter` and `debounceTime`.

```js
import { fromEvent, map } from "rxjs";

fromEvent(document, "click")
  .pipe(map((e) => e.clientX))
  .subscribe((x) => console.log(x));
```

## 109: What is a signal in front-end frameworks?

A signal is a value container that tracks who reads it and notifies them when it changes. Solid, Angular, Vue (refs), Preact and Svelte 5 (runes) all use this idea. It is a fine-grained version of the Observer pattern: only the code that read a signal reruns when that signal changes. There is also a TC39 proposal to add signals to JavaScript, but it is still at an early stage.

## 110: What is two-way data binding?

With two-way binding, the UI and the data stay in sync automatically in both directions: when the data changes, the input updates, and when the user types, the data updates. Angular (`[(ngModel)]`) and Vue (`v-model`) support it. It saves code for forms, but in large apps it can make it harder to know who changed what.

## 111: What is the Repository pattern?

A Repository hides how data is stored and gives the rest of the app simple methods to work with it, like `findById`, `save` and `delete`. The calling code doesn't care if data comes from a REST API, IndexedDB or a mock.

```js
class UserRepository {
  constructor(http) {
    this.http = http;
  }
  findById(id) {
    return this.http.get(`/users/${id}`);
  }
  save(user) {
    return this.http.put(`/users/${user.id}`, user);
  }
}
```

## 112: What is a service layer?

A service layer is a set of modules or classes that hold business logic, separate from UI components and data access. Components call services, and services call repositories or APIs. This keeps components small and lets you reuse the same logic in different places. Angular services and NestJS providers are typical examples.

## 113: What is a DTO (Data Transfer Object)?

A DTO is a simple object that only carries data between layers or over the network, with no behavior. For example, the JSON your API sends or receives. Keeping DTOs separate from your internal models lets the API shape and your app's shape change independently, with a mapper or adapter in between.

## 114: What is a Value Object?

A Value Object is a small object defined only by its values, not by an identity. Two value objects with the same values are equal. They are usually immutable. Money, dates, coordinates and colors are typical examples.

```js
class Money {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
    Object.freeze(this);
  }
  equals(other) {
    return this.amount === other.amount && this.currency === other.currency;
  }
}
```

## 115: What is duck typing?

Duck typing means you care about what an object can do, not what class it is: "if it walks like a duck and quacks like a duck, it's a duck". JavaScript has no interfaces, so patterns rely on duck typing. A strategy just needs to be a function, an iterable just needs `[Symbol.iterator]`, and a "thenable" just needs a `then` method.

## 116: How do you define an "interface" in JavaScript?

JavaScript has no `interface` keyword, so an interface is just an agreement about which methods an object must have. You can document it with JSDoc, check it at runtime, or use TypeScript to check it at build time.

```js
/**
 * @typedef {Object} Storage
 * @property {(key: string) => Promise<string | null>} get
 * @property {(key: string, value: string) => Promise<void>} set
 */
```

## 117: What is the difference between an iterable and an iterator?

An **iterable** is an object that has a `[Symbol.iterator]()` method (arrays, strings, maps, sets). An **iterator** is the object that method returns. It has a `next()` method that returns `{ value, done }`.

```js
const it = [10, 20][Symbol.iterator]();
it.next(); // { value: 10, done: false }
it.next(); // { value: 20, done: false }
it.next(); // { value: undefined, done: true }
```

## 118: What is a generator function?

A generator function (`function*`) can pause with `yield` and continue later. Calling it returns an iterator. Generators make it easy to write iterators and lazy sequences.

```js
function* ids() {
  let id = 1;
  while (true) yield id++;
}

const gen = ids();
gen.next().value; // 1
gen.next().value; // 2
```

## 119: What are async iterators?

Async iterators are like normal iterators, but `next()` returns a promise. You loop over them with `for await...of`. They are good for paginated APIs, streams and reading files in chunks.

```js
async function* fetchPages(url) {
  let next = url;
  while (next) {
    const res = await fetch(next);
    const data = await res.json();
    yield data.items;
    next = data.nextPage;
  }
}

for await (const items of fetchPages("/api/items")) {
  console.log(items.length);
}
```

## 120: What is a thunk?

A thunk is a function that wraps an expression so it can be run later. In Redux, a "thunk" is a function you dispatch instead of an action object, and it gets `dispatch` and `getState` so it can do async work.

```js
const fetchUser = (id) => async (dispatch) => {
  const user = await api.getUser(id);
  dispatch({ type: "user/loaded", payload: user });
};
```

## 121: What is function composition?

Function composition combines small functions into a new one, where the output of one becomes the input of the next.

```js
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);

const slugify = pipe(
  (s) => s.trim(),
  (s) => s.toLowerCase(),
  (s) => s.replace(/\s+/g, "-"),
);

slugify("  Hello World "); // "hello-world"
```

`pipe` runs left to right. `compose` does the same but right to left.

## 122: What is inversion of control?

Inversion of control means your code doesn't control the flow; a framework or another piece of code calls your code when needed. It is sometimes called the "Hollywood principle": don't call us, we'll call you. Event handlers, React components, and dependency injection containers are all examples. It is also the main difference between a library (you call it) and a framework (it calls you).

## 123: What is the Law of Demeter?

Also called "the principle of least knowledge": an object should only talk to its direct friends, not to friends of friends. Code like `order.customer.address.city.name` breaks it, because it depends on the internal structure of many objects. If one of those changes, this line breaks. A method like `order.getShippingCity()` hides that structure.

## 124: What does "tell, don't ask" mean?

Instead of asking an object for its data and then making decisions about it outside, you tell the object what to do and let it decide.

```js
// ask
if (account.balance >= amount) account.balance -= amount;

// tell
account.withdraw(amount); // the account checks its own balance
```

This keeps logic next to the data it uses.

## 125: What is the Object Pool pattern?

An Object Pool keeps a set of ready-to-use objects and reuses them instead of creating and destroying them over and over. It helps when creating objects is expensive or when creating many short-lived objects causes garbage collection pauses, such as particles in a game or database connections on a server.

## 126: What is feature detection?

Feature detection checks if the browser supports something before using it, instead of checking the browser name.

```js
if ("IntersectionObserver" in window) {
  lazyLoadImages();
} else {
  loadAllImages();
}
```

It is more reliable than user-agent sniffing and is often combined with polyfills or fallbacks.

## 127: How is a polyfill related to design patterns?

A polyfill adds a missing API to older environments so your code can use the modern interface everywhere. It is close to the Adapter pattern: it makes the old environment match the interface your code expects. A "ponyfill" does the same thing but exports a function instead of patching globals, which is safer.

## 128: What is init-time branching?

Init-time branching means you check the environment once, when the code loads, and pick the right implementation, instead of checking every time the function runs.

```js
const storage =
  typeof localStorage !== "undefined"
    ? { get: (k) => localStorage.getItem(k) }
    : { get: () => null };
```

This avoids repeating the same check on every call.

## 129: What is the Event Bus pattern?

An event bus is a shared object that parts of the app use to send and receive events without knowing about each other. It is a Pub/Sub implementation. It is handy for small apps or for communication between independent widgets, but in large apps it can make the flow hard to follow, so many teams prefer a state management library.

## 130: What is the Producer/Consumer pattern?

Producers create work items and put them in a queue. Consumers take items from the queue and process them. The two sides can run at different speeds. In JavaScript you see it in job queues (like BullMQ), message brokers (like RabbitMQ), Web Workers that process tasks, and streams.

## 131: How do you load code only when it is needed?

Use dynamic `import()`, which returns a promise for the module. Bundlers split this into a separate file.

```js
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});
```

This is lazy loading applied to code, and it keeps the initial bundle smaller.

## 132: What are rendering patterns on the web?

Rendering patterns describe where and when HTML is created:

- **CSR** (client-side rendering): the browser builds the page with JavaScript.
- **SSR** (server-side rendering): the server builds HTML on each request.
- **SSG** (static site generation): HTML is built at build time.
- **ISR** (incremental static regeneration): static pages are rebuilt in the background after some time.
- **Streaming SSR** and **islands**: send HTML in parts and only hydrate the interactive pieces.

## 133: What is a barrel file?

A barrel file is an `index.js` that re-exports things from several files so other code can import from one path.

```js
// components/index.js
export { Button } from "./Button.js";
export { Modal } from "./Modal.js";
```

It makes imports shorter, but large barrels can slow down dev servers and tests and make tree shaking harder, because importing one thing may load every file in the barrel.

## 134: How do you cancel an async operation?

Use `AbortController`. You pass its `signal` to the operation and call `abort()` to cancel.

```js
const controller = new AbortController();

fetch("/api/search?q=js", { signal: controller.signal })
  .then((r) => r.json())
  .catch((err) => {
    if (err.name === "AbortError") console.log("cancelled");
  });

controller.abort();
```

`addEventListener` also accepts a `signal`, which removes the listener when you abort.

## 135: How do you model loading, success and error states in UI code?

Use one status value instead of several booleans like `isLoading` and `hasError` that can get out of sync.

```js
const state = { status: "idle", data: null, error: null };
// status: "idle" | "loading" | "success" | "error"

function render(state) {
  switch (state.status) {
    case "loading":
      return "Loading...";
    case "error":
      return `Error: ${state.error.message}`;
    case "success":
      return state.data.title;
    default:
      return "";
  }
}
```

This is a small state machine and avoids impossible states like "loading and error at the same time".

## 136: What is a Web Component and which patterns does it use?

A Web Component is a custom HTML element built with browser APIs: Custom Elements, Shadow DOM and templates. It uses:

- **Registry**: `customElements.define("my-button", MyButton)`.
- **Template Method / lifecycle hooks**: `connectedCallback`, `disconnectedCallback`, `attributeChangedCallback`.
- **Encapsulation**: Shadow DOM hides internal markup and styles, like the Module pattern does for code.

## 137: What is the Object Literal pattern?

It means grouping related data and functions in a plain object literal. It is the simplest way to organize code and is fine when you only need one instance.

```js
const cart = {
  items: [],
  add(item) {
    this.items.push(item);
  },
  total() {
    return this.items.reduce((sum, i) => sum + i.price, 0);
  },
};
```

There is no privacy, though: anything can change `cart.items` directly.

## 138: Which objects in the browser are effectively singletons?

`window`, `document`, `navigator`, `localStorage`, `history` and `location` exist only once per page (or per tab). You don't create them, you just use the existing instance. Inside an iframe or a worker you get a different set, so they are one per browsing context, not one per browser.

## 139: What is the Retry pattern?

The Retry pattern repeats a failed operation a few times before giving up, because some failures (like a network blip) are temporary.

```js
async function retry(fn, attempts = 3) {
  for (let i = 1; i <= attempts; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === attempts) throw err;
    }
  }
}

const data = await retry(() => fetch("/api").then((r) => r.json()));
```

In real code you also wait between attempts (backoff) and only retry errors that are worth retrying.

## 140: What is a wrapper, and is it a design pattern?

"Wrapper" is a general word for an object or function that sits around another one. Adapter, Decorator, Facade and Proxy are all wrappers, and they differ in why they wrap: Adapter changes the interface, Decorator adds behavior, Facade simplifies, and Proxy controls access. When someone says "wrapper" in an interview, it's good to ask or say which of these they mean.

## 141: What is a "thenable"?

A thenable is any object with a `then(onFulfilled, onRejected)` method. `await` and `Promise.resolve()` treat thenables like promises. This is duck typing in action and is how libraries with their own promise-like objects (like old jQuery deferreds) work with native promises.

```js
const thenable = {
  then(resolve) {
    resolve(42);
  },
};

await thenable; // 42
```

## 142: What is the difference between a class and an object literal for creating objects?

An object literal creates a single object right away. A class is a blueprint you use with `new` to create many objects that share methods through the prototype. Use a literal for one-off config or a simple module, and a class (or factory function) when you need many instances with the same shape.

## 143: How do you use WeakMap for private data?

Before `#private` fields, you could store private data in a `WeakMap` keyed by the instance. When the instance is garbage collected, its entry goes away too.

```js
const privateData = new WeakMap();

class Person {
  constructor(name) {
    privateData.set(this, { name });
  }
  getName() {
    return privateData.get(this).name;
  }
}
```

You will still see this pattern in older libraries.

## 144: What are Symbols used for in patterns?

Symbols create unique property keys that can't clash with other keys. JavaScript uses "well-known symbols" to let you hook into language behavior: `Symbol.iterator` (Iterator pattern), `Symbol.asyncIterator`, `Symbol.toPrimitive` and `Symbol.hasInstance`. You can also use your own symbols as hidden-ish keys for metadata or as unique enum values.

## 145: What is the difference between a library and a framework?

With a library, your code is in control and calls the library when it needs it (like lodash or date-fns). With a framework, the framework is in control and calls your code at the right time (like Angular or Next.js). This is inversion of control. React is often called a library, but in practice it controls rendering and calls your components, so it behaves more like a framework.

## 146: What is the Compound Components pattern?

Compound components are a set of components that work together and share state through a parent, like `<select>` and `<option>` in HTML.

```jsx
<Tabs defaultValue="a">
  <Tabs.List>
    <Tabs.Trigger value="a">A</Tabs.Trigger>
    <Tabs.Trigger value="b">B</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Panel value="a">Content A</Tabs.Panel>
</Tabs>
```

The parent (`Tabs`) shares state with its children through context, and the user decides the layout. Many headless UI libraries use it.

## 147: What are controlled and uncontrolled components?

A **controlled** component gets its value from props and reports changes through callbacks, so the parent owns the state. An **uncontrolled** component keeps its own state internally, and the parent reads it when needed (for example, with a ref or form data). Many good components support both: they use the prop if given, and fall back to internal state otherwise.

## 148: What is "configuration over code"?

It means describing behavior with data (config objects, JSON, routes tables) instead of writing custom code for each case. For example, a form builder that renders fields from a schema, or a router configured with an array of route objects. It makes adding cases easy but can get hard to debug if the config grows into its own little language.

## 149: What is the difference between design patterns and architectural patterns?

Design patterns solve problems inside a part of the code, like how to create an object or how two objects communicate (Factory, Observer). Architectural patterns describe how the whole application is organized, like MVC, Flux, micro-frontends, layered architecture or event-driven architecture. An architectural pattern usually uses several design patterns inside it.

## 150: How do you pick the right design pattern for a problem?

Start from the problem, not the pattern. Ask what is actually hard: creating objects with many options (Builder, Factory), reacting to changes (Observer), switching between behaviors (Strategy, State), hiding a messy API (Facade, Adapter) or adding cross-cutting behavior (Decorator, Middleware). Pick the simplest option that solves it. In JavaScript that is often just a function, a closure or a plain object, not a full class-based pattern.

# Moderate Questions (151-300)

## 151: What is the difference between Proxy, Decorator and Adapter?

All three wrap another object, but for different reasons:

- **Adapter** changes the interface so the object fits what the caller expects.
- **Decorator** keeps the same interface and adds new behavior (logging, caching, retries).
- **Proxy** keeps the same interface and controls access (lazy loading, permission checks, remote calls).

The code can look almost the same. The difference is the intent, and that is what interviewers usually want you to explain.

## 152: What is the difference between Facade and Adapter?

An Adapter makes one existing interface look like another existing interface, usually one-to-one. A Facade creates a new, simpler interface on top of one or many objects to make them easier to use. Adapter is about compatibility. Facade is about simplicity.

## 153: What is the difference between Strategy and State?

Both swap behavior by switching objects, and the code can look similar. In **Strategy**, the caller picks the algorithm, and strategies don't know about each other. In **State**, the object switches its own state as things happen, and states usually know which state comes next. Payment method selection is Strategy. A traffic light or an order going from "pending" to "shipped" is State.

## 154: How can the Observer pattern cause memory leaks?

The subject holds a reference to every observer. If an observer is no longer needed but never unsubscribes, it can't be garbage collected, and neither can anything it references (like a DOM node or a component). It also keeps getting called. Always return an unsubscribe function and call it on cleanup:

```js
useEffect(() => {
  const unsubscribe = store.subscribe(render);
  return unsubscribe;
}, []);
```

## 155: How would you implement a small event emitter with on, off, once and emit?

```js
class Emitter {
  #events = new Map();

  on(name, fn) {
    if (!this.#events.has(name)) this.#events.set(name, new Set());
    this.#events.get(name).add(fn);
    return () => this.off(name, fn);
  }

  off(name, fn) {
    this.#events.get(name)?.delete(fn);
  }

  once(name, fn) {
    const wrapper = (...args) => {
      this.off(name, wrapper);
      fn(...args);
    };
    return this.on(name, wrapper);
  }

  emit(name, ...args) {
    for (const fn of [...(this.#events.get(name) ?? [])]) fn(...args);
  }
}
```

Copying the set before looping in `emit` avoids problems when a listener removes itself during the loop.

## 156: Why should an emitter catch errors thrown by one listener?

If one listener throws inside a plain loop, the remaining listeners never run, and the error goes back to whoever called `emit`. Depending on your needs, you can catch errors per listener and report them, so one broken subscriber doesn't break the others:

```js
for (const fn of listeners) {
  try {
    fn(data);
  } catch (err) {
    reportError(err);
  }
}
```

`reportError()` is a global in browsers and Deno that reports the error the same way an uncaught error would be reported. Node's `EventEmitter` does not catch for you, so a throwing listener stops the rest.

## 157: How do you test code that uses a singleton?

Singletons make tests harder because state stays between tests. Options:

- Don't import the singleton inside the code under test. Pass it in as a dependency so tests can give a fake.
- Export the class as well as the instance, so tests can create fresh instances.
- Add a reset method used only in tests.
- Mock the module with your test runner (`vi.mock` or `jest.mock`).

The first option is the cleanest because it fixes the design, not just the test.

## 158: Is a module-level singleton always one instance in Node.js?

Usually, because modules are cached after the first load. But you can get more than one instance when:

- Two copies of the same package are installed (different versions in `node_modules`).
- The same file is loaded as both CommonJS and ESM (the "dual package hazard").
- The cache key differs, for example with different paths to the same file (symlinks, different casing on case-insensitive file systems in CommonJS).
- Code runs in separate workers or processes.

If something must be truly global, like a registry shared across packages, some libraries store it on `globalThis` with a `Symbol.for()` key.

## 159: How do you create a singleton that needs async setup?

Cache the promise, not the result. Then every caller that comes in before setup finishes gets the same promise.

```js
let dbPromise;

export function getDb() {
  dbPromise ??= connectToDatabase();
  return dbPromise;
}

const db = await getDb();
```

If you cache the result after `await`, two early callers can both start a connection. If setup can fail, clear `dbPromise` on error so the next call can try again.

## 160: How do you make a factory open for extension without editing it?

Use a registry instead of a hard-coded `if`/`switch`:

```js
const registry = new Map();

export function registerShape(type, creator) {
  registry.set(type, creator);
}

export function createShape(type, options) {
  const creator = registry.get(type);
  if (!creator) throw new Error(`Unknown shape: ${type}`);
  return creator(options);
}

registerShape("circle", ({ r }) => ({ area: () => Math.PI * r * r }));
```

New types are added by registering them, so the factory code never changes.

## 161: When should you use a Builder instead of an options object?

In JavaScript, an options object covers most cases. A Builder is worth it when:

- The object is built in many steps, maybe in different places in the code.
- Some steps depend on others or must happen in a certain order.
- You want to validate the whole object once at the end.
- The building reads better as a sentence, like query builders (`db.select().from("users").where(...)`).

For a function with a few optional settings, just use an options object.

## 162: How do you validate in a Builder?

Validate in `build()`, where you have the full picture, and return an immutable result.

```js
class EmailBuilder {
  #email = { to: [], subject: "", body: "" };

  to(address) {
    this.#email.to.push(address);
    return this;
  }
  subject(s) {
    this.#email.subject = s;
    return this;
  }
  body(b) {
    this.#email.body = b;
    return this;
  }
  build() {
    if (this.#email.to.length === 0) throw new Error("No recipients");
    if (!this.#email.subject) throw new Error("Subject is required");
    return Object.freeze({ ...this.#email, to: [...this.#email.to] });
  }
}
```

## 163: How do you write an immutable fluent API?

Each method returns a new object instead of changing `this`. This way a partially built object can be reused safely.

```js
class Query {
  constructor(parts = {}) {
    this.parts = Object.freeze(parts);
  }
  where(cond) {
    return new Query({ ...this.parts, where: cond });
  }
  limit(n) {
    return new Query({ ...this.parts, limit: n });
  }
}

const base = new Query().where("active = true");
const firstTen = base.limit(10);
const firstFive = base.limit(5); // base is unchanged
```

## 164: How do you use Object.create with property descriptors?

The second argument of `Object.create` lets you define properties with full control over whether they are writable, enumerable or configurable.

```js
const proto = {
  greet() {
    return `Hi, ${this.name}`;
  },
};

const user = Object.create(proto, {
  name: { value: "Ana", writable: false, enumerable: true },
  id: { value: 1, enumerable: false },
});

user.greet(); // "Hi, Ana"
Object.keys(user); // ["name"]
```

## 165: How do you write class-based mixins?

Use functions that take a base class and return a class that extends it. You can chain several of them.

```js
const Serializable = (Base) =>
  class extends Base {
    toJSON() {
      return { ...this };
    }
  };

const Timestamped = (Base) =>
  class extends Base {
    createdAt = new Date();
  };

class User {
  constructor(name) {
    this.name = name;
  }
}

class Model extends Serializable(Timestamped(User)) {}
```

This keeps `super` working and plays well with `instanceof` on the base class.

## 166: What are the problems with mixins?

- **Name collisions**: two mixins can define the same method, and the last one silently wins.
- **Hidden dependencies**: a mixin may expect `this.name` or another method to exist, and nothing checks that.
- **Hard to trace**: it is not obvious where a method comes from.

React removed mixins from its old `createClass` API for these reasons. Composition (holding helper objects as fields) or plain functions are usually easier to follow.

## 167: How do you memoize an async function?

Cache the promise, so parallel calls with the same key share one request. Remove the entry if the promise rejects, so errors are not cached forever.

```js
function memoizeAsync(fn) {
  const cache = new Map();
  return (key) => {
    if (!cache.has(key)) {
      const promise = fn(key).catch((err) => {
        cache.delete(key);
        throw err;
      });
      cache.set(key, promise);
    }
    return cache.get(key);
  };
}

const getUser = memoizeAsync((id) =>
  fetch(`/api/users/${id}`).then((r) => r.json()),
);
```

## 168: How do you decorate a class method without decorator syntax?

Replace the method on the prototype with a wrapped version:

```js
function logMethod(Class, name) {
  const original = Class.prototype[name];
  Class.prototype[name] = function (...args) {
    console.log(`${name} called with`, args);
    return original.apply(this, args);
  };
}

class Api {
  save(data) {
    return data;
  }
}

logMethod(Api, "save");
```

Use `apply(this, ...)` so the original method keeps the right `this`.

## 169: What is the decorator syntax (@) in JavaScript?

The `@decorator` syntax is a TC39 proposal at stage 3. Browsers don't fully support it yet, so you use it today through TypeScript 5+ or Babel. A method decorator is a function that receives the method and a context object and can return a replacement:

```js
function logged(method, context) {
  return function (...args) {
    console.log(`calling ${String(context.name)}`);
    return method.apply(this, args);
  };
}

class Api {
  @logged
  save(data) {
    return data;
  }
}
```

The older "experimental decorators" from TypeScript and Angular use a different signature, so code written for one doesn't work with the other.

## 170: How do you use a Proxy for validation?

Use the `set` trap and throw on invalid values.

```js
function createValidated(target, rules) {
  return new Proxy(target, {
    set(obj, prop, value, receiver) {
      const rule = rules[prop];
      if (rule && !rule(value)) {
        throw new TypeError(`Invalid value for ${String(prop)}`);
      }
      return Reflect.set(obj, prop, value, receiver);
    },
  });
}

const user = createValidated({}, { age: (v) => Number.isInteger(v) && v >= 0 });
user.age = 30; // ok
user.age = -1; // TypeError
```

## 171: How can a Proxy provide default values for missing properties?

Use the `get` trap and check if the property exists:

```js
const withDefault = (obj, fallback) =>
  new Proxy(obj, {
    get(target, prop, receiver) {
      return prop in target ? Reflect.get(target, prop, receiver) : fallback;
    },
  });

const counts = withDefault({}, 0);
counts.apples; // 0
```

## 172: Why use Reflect inside Proxy traps?

`Reflect` has one method for every proxy trap (`Reflect.get`, `Reflect.set`, `Reflect.has` and so on) that does the default behavior. Using it makes sure you forward the operation correctly, including the `receiver`, which matters for getters and inheritance. Writing `target[prop]` instead can break getters that use `this`, because `this` would be the target instead of the proxy.

## 173: What is a virtual proxy?

A virtual proxy delays creating an expensive object until it is actually used. The caller holds the proxy and doesn't know the real object doesn't exist yet.

```js
function lazy(factory) {
  let instance;
  return new Proxy(
    {},
    {
      get(_, prop) {
        instance ??= factory();
        const value = instance[prop];
        return typeof value === "function" ? value.bind(instance) : value;
      },
    },
  );
}

const chart = lazy(() => new HeavyChart()); // not created yet
chart.render(); // created now
```

## 174: How would you build a caching proxy for an API client?

Wrap the client and cache results of read methods:

```js
function withCache(api, ttl = 60_000) {
  const cache = new Map();
  return new Proxy(api, {
    get(target, prop, receiver) {
      const value = Reflect.get(target, prop, receiver);
      if (typeof value !== "function" || !String(prop).startsWith("get")) {
        return value;
      }
      return (...args) => {
        const key = `${String(prop)}:${JSON.stringify(args)}`;
        const hit = cache.get(key);
        if (hit && Date.now() - hit.time < ttl) return hit.value;
        const result = value.apply(target, args);
        cache.set(key, { value: result, time: Date.now() });
        return result;
      };
    },
  });
}
```

The calling code uses the same API and doesn't know caching happens.

## 175: What is a revocable proxy?

`Proxy.revocable()` returns a proxy and a `revoke` function. After you call `revoke()`, any use of the proxy throws a `TypeError`. It is useful when you give an object to code you don't fully trust and want to cut off access later.

```js
const { proxy, revoke } = Proxy.revocable({ secret: 1 }, {});
proxy.secret; // 1
revoke();
proxy.secret; // TypeError
```

## 176: How do you implement undo and redo with the Command pattern?

Keep two stacks. Running a command pushes it to the undo stack and clears the redo stack.

```js
class History {
  #undo = [];
  #redo = [];

  run(command) {
    command.execute();
    this.#undo.push(command);
    this.#redo = [];
  }

  undo() {
    const cmd = this.#undo.pop();
    if (!cmd) return;
    cmd.undo();
    this.#redo.push(cmd);
  }

  redo() {
    const cmd = this.#redo.pop();
    if (!cmd) return;
    cmd.execute();
    this.#undo.push(cmd);
  }
}
```

## 177: What is a macro command?

A macro command is a command made of other commands. Running it runs all of them, and undoing it undoes them in reverse order.

```js
function macro(commands) {
  return {
    execute: () => commands.forEach((c) => c.execute()),
    undo: () => [...commands].reverse().forEach((c) => c.undo()),
  };
}
```

It is the Composite pattern applied to commands, and is useful for "apply all changes" or batch operations.

## 178: How do you implement Chain of Responsibility for validation?

Each handler checks one rule and either returns an error or passes to the next.

```js
const rules = [
  (v) => (v.trim() ? null : "Required"),
  (v) => (v.length >= 8 ? null : "Too short"),
  (v) => (/\d/.test(v) ? null : "Must contain a number"),
];

function validate(value) {
  for (const rule of rules) {
    const error = rule(value);
    if (error) return error;
  }
  return null;
}

validate("abc"); // "Too short"
```

You can add, remove or reorder rules without touching `validate`.

## 179: How would you implement a middleware runner like Koa's?

Each middleware gets a context and a `next` function that runs the rest of the chain. Because `next` returns a promise, code after `await next()` runs on the way back out.

```js
function compose(middlewares) {
  return (ctx) => {
    const dispatch = (i) => {
      const fn = middlewares[i];
      if (!fn) return Promise.resolve();
      return Promise.resolve(fn(ctx, () => dispatch(i + 1)));
    };
    return dispatch(0);
  };
}

const run = compose([
  async (ctx, next) => {
    const start = Date.now();
    await next();
    ctx.time = Date.now() - start;
  },
  async (ctx) => {
    ctx.body = "Hello";
  },
]);
```

The real Koa version also throws if `next()` is called twice in one middleware.

## 180: What is the difference between Mediator and Observer?

With Observer, the subject broadcasts changes and doesn't care who listens or what they do. With Mediator, one central object contains the coordination logic: it receives messages from components and decides what other components should do. Observer spreads the logic among listeners. Mediator puts it in one place. In practice a mediator often uses events internally.

## 181: Can you give a practical example of the Mediator pattern in a UI?

A form where fields affect each other. Instead of the "country" field knowing about the "state" and "zip" fields, every field reports changes to the form, and the form decides what happens.

```js
class CheckoutForm {
  constructor(fields) {
    this.fields = fields;
    for (const field of Object.values(fields)) field.mediator = this;
  }

  changed(field) {
    if (field === this.fields.country) {
      this.fields.state.setOptions(statesFor(field.value));
      this.fields.zip.setRequired(field.value === "US");
    }
  }
}
```

Fields stay simple and reusable, and all the rules live in one place.

## 182: How do you build a lazy data pipeline with generators?

Each step is a generator that takes an iterable and yields results one by one. Nothing runs until someone asks for values, and you can stop early.

```js
function* map(iter, fn) {
  for (const x of iter) yield fn(x);
}
function* filter(iter, fn) {
  for (const x of iter) if (fn(x)) yield x;
}
function* take(iter, n) {
  if (n <= 0) return;
  for (const x of iter) {
    yield x;
    if (--n === 0) return;
  }
}

function* naturals() {
  let n = 1;
  while (true) yield n++;
}

[
  ...take(
    filter(
      map(naturals(), (n) => n * n),
      (n) => n % 2,
    ),
    3,
  ),
]; // [1, 9, 25]
```

This works even with infinite sequences.

## 183: What are iterator helpers?

Iterator helpers (added in ES2025) are methods like `map`, `filter`, `take`, `drop`, `flatMap`, `reduce`, `some`, `every`, `find` and `toArray` that live on `Iterator.prototype`. They give you lazy pipelines without writing your own generators.

```js
function* naturals() {
  let n = 1;
  while (true) yield n++;
}

naturals()
  .map((n) => n * n)
  .filter((n) => n % 2)
  .take(3)
  .toArray(); // [1, 9, 25]
```

`Iterator.from()` wraps any iterable or iterator-like object so you can use these helpers on it.

## 184: What do return() and throw() do on a generator?

`gen.return(value)` finishes the generator early, as if a `return` happened at the current `yield`. Any `finally` blocks inside still run, so cleanup code works. `gen.throw(error)` throws the error at the current `yield`, and the generator can catch it. `for...of` calls `return()` automatically when you `break` out of the loop, which is how iterators get a chance to clean up.

## 185: How do you implement the Composite pattern for a file tree?

Give leaves and containers the same interface. Containers call the method on their children.

```js
class File {
  constructor(name, size) {
    this.name = name;
    this.size = size;
  }
  getSize() {
    return this.size;
  }
}

class Folder {
  constructor(name, children = []) {
    this.name = name;
    this.children = children;
  }
  getSize() {
    return this.children.reduce((sum, c) => sum + c.getSize(), 0);
  }
}

const root = new Folder("root", [
  new File("a.txt", 10),
  new Folder("img", [new File("b.png", 50)]),
]);
root.getSize(); // 60
```

The calling code just calls `getSize()` without checking whether it has a file or a folder.

## 186: How would you implement a Flyweight with a factory?

Keep a cache of shared objects keyed by their shared data, and store only the unique data per instance.

```js
const iconCache = new Map();

function getIcon(name) {
  if (!iconCache.has(name)) {
    iconCache.set(name, { name, svg: loadSvg(name) }); // shared, heavy
  }
  return iconCache.get(name);
}

const markers = points.map((p) => ({
  x: p.x, // unique
  y: p.y, // unique
  icon: getIcon(p.type), // shared
}));
```

A thousand markers of type "pin" share one icon object instead of a thousand copies.

## 187: What is the difference between Template Method and Strategy?

Template Method uses inheritance: the base class defines the algorithm and subclasses override some steps. Strategy uses composition: the object receives a whole algorithm (often a function) from outside. Strategy is more flexible, because you can change it at runtime and don't need a class hierarchy. In JavaScript, a "template method" is often written as a function that takes hook functions as options, which is really a mix of both.

## 188: How do you implement a finite state machine with a transition table?

Define states, allowed events in each state, and the next state. Unknown events are ignored.

```js
const machine = {
  initial: "idle",
  states: {
    idle: { on: { FETCH: "loading" } },
    loading: { on: { RESOLVE: "success", REJECT: "failure" } },
    success: { on: { FETCH: "loading" } },
    failure: { on: { RETRY: "loading" } },
  },
};

function transition(state, event) {
  return machine.states[state].on[event] ?? state;
}

transition("idle", "FETCH"); // "loading"
transition("idle", "RESOLVE"); // "idle" (not allowed)
```

Libraries like XState add guards, actions, nested states and visual tools on top of this idea.

## 189: How do you implement undo with Memento using immutable state?

If state is immutable, each version is already a snapshot. Keep a list of past and future states.

```js
const history = { past: [], present: { text: "" }, future: [] };

function update(h, next) {
  return { past: [...h.past, h.present], present: next, future: [] };
}

function undo(h) {
  if (h.past.length === 0) return h;
  return {
    past: h.past.slice(0, -1),
    present: h.past.at(-1),
    future: [h.present, ...h.future],
  };
}
```

Because unchanged parts are shared between versions, this costs less memory than it looks. Limit the history length for large states.

## 190: How can a Repository add caching without changing its callers?

Wrap the repository with another object that has the same methods (a decorator):

```js
function cachedRepository(repo) {
  const cache = new Map();
  return {
    async findById(id) {
      if (!cache.has(id)) cache.set(id, await repo.findById(id));
      return cache.get(id);
    },
    async save(entity) {
      await repo.save(entity);
      cache.set(entity.id, entity);
    },
  };
}

const users = cachedRepository(new UserRepository(http));
```

## 191: What is a composition root?

A composition root is the one place, usually near the app entry point, where you create all your objects and wire their dependencies together. Everything else receives its dependencies instead of creating them.

```js
// main.js
const http = createHttpClient({ baseUrl: "/api" });
const userRepo = new UserRepository(http);
const userService = new UserService(userRepo, logger);
startApp({ userService });
```

This is dependency injection without a library. For most front-end apps it is enough.

## 192: How would you build a small dependency injection container?

Register factories by name, and resolve them lazily, caching singletons.

```js
class Container {
  #factories = new Map();
  #instances = new Map();

  register(name, factory) {
    this.#factories.set(name, factory);
  }

  resolve(name) {
    if (!this.#instances.has(name)) {
      const factory = this.#factories.get(name);
      if (!factory) throw new Error(`No provider for ${name}`);
      this.#instances.set(name, factory(this));
    }
    return this.#instances.get(name);
  }
}

const c = new Container();
c.register("http", () => createHttpClient());
c.register("users", (c) => new UserService(c.resolve("http")));
c.resolve("users");
```

## 193: What is the difference between a Service Locator and dependency injection?

With a service locator, the class asks a global registry for what it needs: `locator.get("http")`. With dependency injection, the class receives what it needs through its constructor or parameters. A service locator hides dependencies inside the code, so you can't see them from the outside, and tests must set up the global locator. DI makes dependencies explicit. Many people consider the service locator an anti-pattern for this reason.

## 194: How does dependency injection make testing easier?

You pass simple fakes instead of real network clients, databases or timers.

```js
test("returns full name", async () => {
  const fakeRepo = { findById: async () => ({ first: "Ana", last: "Lee" }) };
  const service = new UserService(fakeRepo);

  expect(await service.getFullName(1)).toBe("Ana Lee");
});
```

No module mocking is needed, and the test is fast and isolated.

## 195: How do you send messages between browser tabs?

Use `BroadcastChannel`. It is Pub/Sub across tabs, windows, iframes and workers from the same origin.

```js
const channel = new BroadcastChannel("auth");

channel.postMessage({ type: "logout" });

channel.onmessage = (e) => {
  if (e.data.type === "logout") redirectToLogin();
};
```

The `storage` event on `window` is an older way: it fires in other tabs when `localStorage` changes.

## 196: How do you communicate between a page and an iframe or worker?

Use `postMessage` and listen for `message` events. For iframes, always pass a target origin and check `event.origin` when receiving, otherwise any site could send you messages.

```js
iframe.contentWindow.postMessage(
  { type: "resize" },
  "https://widget.example.com",
);

window.addEventListener("message", (e) => {
  if (e.origin !== "https://widget.example.com") return;
  handle(e.data);
});
```

For workers, `worker.postMessage()` and `worker.onmessage` work the same way. `MessageChannel` gives you a dedicated two-way pipe.

## 197: How would you add cancel and flush to a debounce function?

```js
function debounce(fn, delay) {
  let timer;
  let lastArgs;
  let lastThis;

  function debounced(...args) {
    lastArgs = args;
    lastThis = this;
    clearTimeout(timer);
    timer = setTimeout(() => debounced.flush(), delay);
  }

  debounced.cancel = () => {
    clearTimeout(timer);
    lastArgs = undefined;
  };

  debounced.flush = () => {
    clearTimeout(timer);
    if (lastArgs) {
      const args = lastArgs;
      lastArgs = undefined;
      fn.apply(lastThis, args);
    }
  };

  return debounced;
}
```

`cancel` is useful when a component unmounts. `flush` is useful when you want to save pending input right away, for example before navigation.

## 198: How do you throttle with requestAnimationFrame?

For visual updates, run at most once per frame:

```js
function rafThrottle(fn) {
  let scheduled = false;
  let lastArgs;
  return (...args) => {
    lastArgs = args;
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      fn(...lastArgs);
    });
  };
}

window.addEventListener("scroll", rafThrottle(updateParallax), {
  passive: true,
});
```

It matches the screen refresh rate and pauses in background tabs.

## 199: What problems come up when memoizing functions with several arguments?

You need a cache key. `JSON.stringify(args)` is common but has issues: it is slow for big objects, two objects with the same content but different identity get the same key, property order changes the key, and values like `undefined`, functions, `Map` and `Set` are not serialized correctly. Alternatives are nested `Map`s per argument, a custom key function, or caching only the last call (like `memoize-one` and React's `useMemo`).

## 200: How do you memoize a function that takes objects without leaking memory?

Use a `WeakMap` keyed by the object. When the object is no longer used anywhere else, its cache entry can be garbage collected.

```js
function memoizeByObject(fn) {
  const cache = new WeakMap();
  return (obj) => {
    if (!cache.has(obj)) cache.set(obj, fn(obj));
    return cache.get(obj);
  };
}

const getTotals = memoizeByObject((order) =>
  order.items.reduce((s, i) => s + i.price, 0),
);
```

This only works if the object is not mutated after it is cached.

## 201: How do you implement an LRU cache in JavaScript?

A `Map` keeps insertion order, so you can move an item to the end when it is used and delete the first item when the cache is full.

```js
class LRUCache {
  #map = new Map();

  constructor(limit) {
    this.limit = limit;
  }

  get(key) {
    if (!this.#map.has(key)) return undefined;
    const value = this.#map.get(key);
    this.#map.delete(key);
    this.#map.set(key, value); // move to the end (most recent)
    return value;
  }

  set(key, value) {
    this.#map.delete(key);
    this.#map.set(key, value);
    if (this.#map.size > this.limit) {
      const oldest = this.#map.keys().next().value;
      this.#map.delete(oldest);
    }
  }
}
```

Both operations are O(1).

## 202: How do you retry with exponential backoff and jitter?

Wait longer after each failure (backoff) and add some randomness (jitter) so many clients don't retry at the same moment.

```js
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function retry(fn, { attempts = 5, base = 200, max = 5000 } = {}) {
  for (let i = 0; ; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i >= attempts - 1 || !isRetryable(err)) throw err;
      const delay = Math.min(max, base * 2 ** i);
      await sleep(Math.random() * delay); // "full jitter"
    }
  }
}

const isRetryable = (err) =>
  err.status === undefined || err.status >= 500 || err.status === 429;
```

Don't retry errors that will fail again, like 400 or 401.

## 203: How do you add a timeout to an async operation?

For `fetch` and other APIs that accept a signal, use `AbortSignal.timeout()`:

```js
const res = await fetch("/api/report", { signal: AbortSignal.timeout(5000) });
```

For any promise, race it against a timer:

```js
function withTimeout(promise, ms) {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error("Timed out")), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}
```

Note that `Promise.race` doesn't stop the original work, it only stops waiting for it. Only a signal can actually cancel it.

## 204: How do you limit how many async tasks run at the same time?

Use a small pool: start N workers, and each worker takes the next task when it finishes one.

```js
async function mapWithLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;

  async function worker() {
    while (next < items.length) {
      const i = next++;
      results[i] = await fn(items[i], i);
    }
  }

  await Promise.all(
    Array.from({ length: Math.min(limit, items.length) }, worker),
  );
  return results;
}

await mapWithLimit(urls, 3, (url) => fetch(url));
```

`next++` is safe here because JavaScript runs this code on one thread. Libraries like `p-limit` do the same thing.

## 205: How do you run async tasks one after another?

Use a `for...of` loop with `await`:

```js
for (const file of files) {
  await upload(file); // waits before starting the next one
}
```

Don't use `forEach` with an async callback: it doesn't wait, so all uploads start at once and errors are not caught by the surrounding code. The `reduce` trick (`files.reduce((p, f) => p.then(() => upload(f)), Promise.resolve())`) also works but is harder to read.

## 206: When do you use Promise.all, allSettled, race and any?

- `Promise.all`: you need every result, and one failure should fail the whole thing.
- `Promise.allSettled`: you want every result, including failures (for example, a batch where some items may fail).
- `Promise.race`: you want whatever settles first, success or failure (timeouts).
- `Promise.any`: you want the first success and only fail if all of them fail (try several mirrors or servers).

## 207: What is a deferred, and how does Promise.withResolvers help?

A deferred is a promise whose `resolve` and `reject` are available outside the constructor, so another part of the code can settle it later. `Promise.withResolvers()` (ES2024) gives you exactly that:

```js
const { promise, resolve, reject } = Promise.withResolvers();

socket.addEventListener("open", resolve, { once: true });
socket.addEventListener("error", reject, { once: true });

await promise;
```

Before it existed, you had to copy `resolve` and `reject` into outer variables from inside `new Promise(...)`.

## 208: How do you make sure async tasks run one at a time, in order?

Chain each new task onto the previous one with a promise queue:

```js
class SerialQueue {
  #last = Promise.resolve();

  add(task) {
    const result = this.#last.then(() => task());
    this.#last = result.catch(() => {}); // a failure must not block the queue
    return result;
  }
}

const queue = new SerialQueue();
queue.add(() => save(draft1));
queue.add(() => save(draft2)); // waits for draft1
```

It is useful for saves that must not overlap, or writes to the same resource.

## 209: What is the Result pattern for error handling?

Instead of throwing, a function returns an object that says if it worked, with either the value or the error. This makes failure part of the return type, so callers can't forget about it.

```js
async function safeFetchJson(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) return { ok: false, error: new Error(`HTTP ${res.status}`) };
    return { ok: true, value: await res.json() };
  } catch (error) {
    return { ok: false, error };
  }
}

const result = await safeFetchJson("/api/user");
if (!result.ok) showError(result.error);
```

It works well for expected failures. Real bugs should still throw.

## 210: How do you design custom error classes?

Extend `Error`, set `name`, add useful fields, and use `cause` to keep the original error.

```js
class HttpError extends Error {
  constructor(status, message, options) {
    super(message, options);
    this.name = "HttpError";
    this.status = status;
  }
}

class NotFoundError extends HttpError {
  constructor(resource, options) {
    super(404, `${resource} not found`, options);
    this.name = "NotFoundError";
  }
}

try {
  await loadUser();
} catch (err) {
  throw new NotFoundError("User", { cause: err });
}
```

Callers can then use `instanceof` to handle each type differently.

## 211: When should you use the Null Object pattern instead of optional chaining?

Optional chaining (`logger?.log("x")`) is fine for one or two places. When the same "maybe missing" object is used in many places, a null object is cleaner: you check once, at creation time, and the rest of the code just calls methods. Null objects also work for return values, like an empty list or a "guest" user with safe defaults, so the caller doesn't need any checks.

## 212: Why wrap a third-party library in your own adapter?

If you call a library directly from 200 files, replacing or upgrading it means changing 200 files. With a thin adapter, only one file knows about the library.

```js
// analytics.js
import posthog from "posthog-js";

export const analytics = {
  track(event, props) {
    posthog.capture(event, props);
  },
  identify(userId) {
    posthog.identify(userId);
  },
};
```

It also makes testing easier and lets you shape the API the way your app needs it. Don't do this for every small utility though, only for libraries that are likely to change or that touch many parts of the app.

## 213: What is an anti-corruption layer?

It is a layer of adapters at the edge of your app that translates data from an outside system (a legacy backend, a third-party API) into your own clean models. It stops the outside system's naming, quirks and structure from leaking all over your code.

```js
function toOrder(dto) {
  return {
    id: String(dto.ORDER_ID),
    total: dto.TOT_AMT_CENTS / 100,
    createdAt: new Date(dto.CRT_TS),
  };
}
```

If the backend changes, you update the translation, not every component.

## 214: How would you build a facade over browser storage?

Hide JSON handling, errors and missing storage behind a small API:

```js
export const storage = {
  get(key, fallback = null) {
    try {
      const raw = localStorage.getItem(key);
      return raw === null ? fallback : JSON.parse(raw);
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // storage full or blocked (for example, in some private modes)
    }
  },
  remove(key) {
    try {
      localStorage.removeItem(key);
    } catch {}
  },
};
```

Callers don't need to know about `JSON.parse` errors or quota errors, and you can later switch to IndexedDB behind the same API.

## 215: What are live bindings in ES modules?

An imported name is a live link to the exported variable, not a copy. If the module changes the variable, importers see the new value. Importers can't reassign it, though.

```js
// counter.js
export let count = 0;
export function increment() {
  count++;
}

// main.js
import { count, increment } from "./counter.js";
increment();
console.log(count); // 1
```

CommonJS works differently: `require` gives you the value of `module.exports` at that moment, so a reassigned primitive is not seen.

## 216: How do circular dependencies between modules cause problems, and how do you fix them?

If `a.js` imports `b.js` and `b.js` imports `a.js`, one of them runs first and sees the other half-initialized. With ESM you can get `ReferenceError: Cannot access 'x' before initialization`. With CommonJS you get an incomplete `exports` object. Fixes:

- Move the shared code into a third module that both import.
- Pass the dependency in (dependency injection) instead of importing it.
- Delay access by using it inside functions, not at the top level.

Tools like `madge` or ESLint's `import/no-cycle` rule can find cycles.

## 217: How does the Module pattern differ between CommonJS and ES modules?

CommonJS (`require`, `module.exports`) loads modules synchronously at runtime, and exports are a normal object you can build dynamically. ES modules (`import`, `export`) are static: imports and exports are known before the code runs, which allows tree shaking and live bindings, and they support top-level `await`. Both cache modules, so a module's top-level code runs once and its exports act like a singleton.

## 218: What is a downside of the Revealing Module pattern?

Private functions call each other directly, not through the returned object. So if someone overrides a public method on the returned object, the internal code still uses the original function.

```js
const mod = (function () {
  function greet() {
    return "hi";
  }
  function welcome() {
    return greet() + "!";
  }
  return { greet, welcome };
})();

mod.greet = () => "hello";
mod.welcome(); // still "hi!"
```

This makes the module hard to extend or patch, for example in tests.

## 219: Why do methods lose this when used as callbacks, and how do you fix it?

`this` depends on how a function is called, not where it is defined. Passing `obj.method` as a callback passes just the function, so `this` is `undefined` (in strict mode) when it runs.

```js
class Counter {
  count = 0;
  increment() {
    this.count++;
  }
}

const c = new Counter();
button.addEventListener("click", c.increment); // this is not c
```

Fixes: `c.increment.bind(c)`, an arrow wrapper `() => c.increment()`, or define the method as an arrow class field `increment = () => { this.count++; }`.

## 220: What is the cost of using arrow functions as class fields?

An arrow function class field is created for every instance, not shared on the prototype. With many instances that uses more memory. It also can't be overridden with `super.method()` in a subclass in the usual way, and it doesn't show up on the prototype for mocking with `vi.spyOn(Class.prototype, "method")`. For a few UI components it doesn't matter. For thousands of objects, prefer prototype methods and bind where needed.

## 221: How would you structure a small vanilla JavaScript app with MVC?

```js
class TodoModel extends EventTarget {
  #todos = [];
  add(text) {
    this.#todos.push({ id: crypto.randomUUID(), text, done: false });
    this.dispatchEvent(new Event("change"));
  }
  get all() {
    return [...this.#todos];
  }
}

class TodoView {
  constructor(root) {
    this.root = root;
  }
  render(todos) {
    this.root.replaceChildren(
      ...todos.map((t) =>
        Object.assign(document.createElement("li"), { textContent: t.text }),
      ),
    );
  }
}

class TodoController {
  constructor(model, view, form) {
    model.addEventListener("change", () => view.render(model.all));
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      model.add(form.elements.text.value);
      form.reset();
    });
  }
}
```

The model knows nothing about the DOM, the view only renders, and the controller wires user input to the model.

## 222: How could you build simple data binding with a Proxy?

Wrap the state in a proxy that re-renders when a property is set:

```js
function reactive(state, onChange) {
  return new Proxy(state, {
    set(target, prop, value, receiver) {
      const ok = Reflect.set(target, prop, value, receiver);
      onChange(prop, value);
      return ok;
    },
  });
}

const state = reactive({ name: "" }, (prop, value) => {
  document.querySelector(`[data-bind="${prop}"]`).textContent = value;
});

input.addEventListener("input", (e) => (state.name = e.target.value));
```

Vue 3's reactivity system is built on this same idea, with dependency tracking added on top.

## 223: How would you write a minimal store like Redux?

```js
function createStore(reducer, initialState) {
  let state = initialState;
  const listeners = new Set();

  return {
    getState: () => state,
    dispatch(action) {
      state = reducer(state, action);
      listeners.forEach((l) => l());
      return action;
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
```

It combines a reducer (pure function), the Observer pattern (subscribe) and the Command pattern (actions).

## 224: How do you connect an external store to React?

Use `useSyncExternalStore`, which subscribes to the store and reads a snapshot safely during concurrent rendering.

```jsx
import { useSyncExternalStore } from "react";

function useStore(store, selector) {
  return useSyncExternalStore(store.subscribe, () =>
    selector(store.getState()),
  );
}

function Counter() {
  const count = useStore(store, (s) => s.count);
  return <p>{count}</p>;
}
```

The selector must return a stable value (the same reference when nothing changed), otherwise React will re-render in a loop.

## 225: What is a selector and why memoize it?

A selector is a function that reads or derives data from state: `const selectTotal = (state) => ...`. It keeps components from knowing the shape of the state. If a selector creates a new array or object every time (`filter`, `map`), components that compare by reference will re-render every time. A memoized selector (like Reselect's `createSelector`) returns the cached result while its inputs haven't changed.

```js
import { createSelector } from "reselect";

const selectTodos = (s) => s.todos;
const selectDone = createSelector([selectTodos], (todos) =>
  todos.filter((t) => t.done),
);
```

## 226: What is reducer composition?

You split a big reducer into small reducers that each handle one part of the state, then combine them.

```js
function combineReducers(reducers) {
  return (state = {}, action) => {
    const next = {};
    for (const key of Object.keys(reducers)) {
      next[key] = reducers[key](state[key], action);
    }
    return next;
  };
}

const rootReducer = combineReducers({ user: userReducer, cart: cartReducer });
```

Each reducer only cares about its own slice, which keeps them small and testable.

## 227: What does a Redux middleware look like?

A middleware is a curried function: `store => next => action => result`. It can log, change, delay or stop actions before they reach the reducer.

```js
const logger = (store) => (next) => (action) => {
  console.log("dispatching", action.type);
  const result = next(action);
  console.log("next state", store.getState());
  return result;
};
```

The curried shape lets Redux build the chain once and reuse it for every dispatch.

## 228: What is the difference between commands and events in action naming?

A command says what should happen: `"addTodo"`, `"sendEmail"`. An event says what already happened: `"todoAdded"`, `"emailSent"`. The Redux style guide recommends naming actions as events, because many reducers can react to one event, and it describes what the user did rather than telling the store how to change. Message-based back ends use the same distinction.

## 229: What is optimistic UI, and how do you implement it?

You update the UI right away as if the request succeeded, then roll back if it fails.

```js
async function toggleLike(post) {
  const previous = post.liked;
  setLiked(post.id, !previous); // update UI now

  try {
    await api.setLike(post.id, !previous);
  } catch (err) {
    setLiked(post.id, previous); // undo on failure
    showToast("Could not save your like");
  }
}
```

It makes the app feel fast. It works best for actions that almost always succeed. React 19 has `useOptimistic` for this.

## 230: What is stale-while-revalidate?

You show cached data right away, even if it might be old, and fetch fresh data in the background. When fresh data arrives, you update the cache and the UI. It started as an HTTP `Cache-Control` directive, and libraries like SWR and TanStack Query use the same idea in the app.

```js
async function getWithSwr(key, fetcher, onUpdate) {
  const cached = cache.get(key);
  fetcher().then((fresh) => {
    cache.set(key, fresh);
    onUpdate(fresh);
  });
  return cached;
}
```

## 231: How do you avoid sending the same request twice at the same time?

Keep a map of in-flight requests by key. If a request with the same key is already running, return its promise.

```js
const inFlight = new Map();

function dedupedFetch(url) {
  if (!inFlight.has(url)) {
    const p = fetch(url)
      .then((r) => r.json())
      .finally(() => inFlight.delete(url));
    inFlight.set(url, p);
  }
  return inFlight.get(url);
}
```

Unlike a cache, the entry is removed as soon as the request finishes.

## 232: What makes a good custom hook?

- It starts with `use` so linters can check the rules of hooks.
- It does one thing (`useDebounce`, `useLocalStorage`), and bigger hooks are built by combining smaller ones.
- It returns what the caller needs, not internal details.
- It cleans up its effects (listeners, timers, subscriptions).
- It doesn't hide expensive work or surprising side effects.

Custom hooks share logic, not state: two components that call the same hook each get their own state.

## 233: How do HOCs, render props and hooks compare?

All three share logic between components.

- **HOCs** wrap components. Problems: wrapper hell in DevTools, prop name collisions, and it's unclear which HOC added which prop.
- **Render props** give more control over rendering but lead to nested callbacks in JSX.
- **Hooks** share logic without adding components to the tree, compose easily, and make data flow explicit.

Hooks are the default today. HOCs are still useful for wrapping a component from outside, for example to add an error boundary or auth check.

## 234: Why can the Provider pattern cause performance problems?

When a context value changes, every component that reads that context re-renders. If you put many unrelated values in one context, or create a new object on every render (`value={{ user, setUser }}`), lots of components re-render for no reason. Fixes:

- Split contexts by how often they change.
- Memoize the value with `useMemo`.
- Put state and setters in separate contexts.
- For frequently changing global state, use a store with selectors instead of context.

## 235: How do you implement compound components in React?

The parent holds state in a context, and the children read it.

```jsx
const TabsContext = createContext(null);

function Tabs({ defaultValue, children }) {
  const [value, setValue] = useState(defaultValue);
  return <TabsContext value={{ value, setValue }}>{children}</TabsContext>;
}

function Trigger({ value, children }) {
  const ctx = use(TabsContext);
  return (
    <button
      aria-selected={ctx.value === value}
      onClick={() => ctx.setValue(value)}
    >
      {children}
    </button>
  );
}

function Panel({ value, children }) {
  const ctx = use(TabsContext);
  return ctx.value === value ? <div>{children}</div> : null;
}

Tabs.Trigger = Trigger;
Tabs.Panel = Panel;
```

## 236: What is a headless component?

A headless component (or hook) handles behavior and state, like opening, closing, keyboard navigation and accessibility attributes, but renders no styles or markup of its own. The user brings the UI. Radix UI, Headless UI, React Aria and TanStack Table work this way. It separates logic from presentation, so the same component works with any design system.

## 237: What is the Slot pattern?

Slots let the caller pass pieces of UI into named places inside a component. In React you use `children` and extra props for named slots. Web Components and Vue have a built-in `<slot>` element.

```jsx
function Card({ header, footer, children }) {
  return (
    <section className="card">
      <header>{header}</header>
      <div>{children}</div>
      <footer>{footer}</footer>
    </section>
  );
}

<Card header={<h2>Title</h2>} footer={<button>OK</button>}>
  Body
</Card>;
```

## 238: What is the prop getters pattern?

A hook returns functions that build the props an element needs. The caller spreads them and can add its own props, which the getter merges safely.

```jsx
function useToggle() {
  const [on, setOn] = useState(false);
  const getButtonProps = ({ onClick, ...rest } = {}) => ({
    "aria-pressed": on,
    onClick: (e) => {
      onClick?.(e);
      setOn((o) => !o);
    },
    ...rest,
  });
  return { on, getButtonProps };
}

const { getButtonProps } = useToggle();
<button {...getButtonProps({ onClick: track })}>Toggle</button>;
```

Downshift popularized it. It avoids the caller accidentally overwriting important handlers.

## 239: What is the state reducer pattern?

A component lets the caller pass a reducer that can change how state updates happen. The component computes its normal next state, then gives the caller a chance to adjust it.

```js
function defaultReducer(state, action) {
  if (action.type === "toggle") return { on: !state.on };
  return state;
}

function useToggle({ reducer = (state, action) => action.changes } = {}) {
  const [state, dispatch] = useReducer(
    (state, action) =>
      reducer(state, { ...action, changes: defaultReducer(state, action) }),
    { on: false },
  );
  return { on: state.on, toggle: () => dispatch({ type: "toggle" }) };
}
```

For example, the caller can block toggling after 3 clicks without forking the component. It is inversion of control applied to state.

## 240: What is an error boundary?

An error boundary is a React component that catches errors thrown while rendering its children and shows a fallback UI instead of crashing the whole app. It is still written as a class component with `static getDerivedStateFromError` and `componentDidCatch`, or with a library like `react-error-boundary`. It doesn't catch errors in event handlers or async code; you handle those with `try/catch`.

## 241: What is the Portal pattern?

A portal renders part of a component into a different place in the DOM, usually at the end of `document.body`, while keeping it in the same place in the component tree. It is used for modals, tooltips and dropdowns that would otherwise be clipped by `overflow: hidden` or a stacking context.

```jsx
import { createPortal } from "react-dom";

function Modal({ children }) {
  return createPortal(<div className="modal">{children}</div>, document.body);
}
```

Events still bubble through the React tree, not the DOM tree. The native `<dialog>` element and the Popover API now solve many of the same problems without a portal.

## 242: How do you lazy load images with IntersectionObserver?

```js
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      const img = entry.target;
      img.src = img.dataset.src;
      observer.unobserve(img);
    }
  },
  { rootMargin: "200px" },
);

document
  .querySelectorAll("img[data-src]")
  .forEach((img) => observer.observe(img));
```

For simple cases, the native `loading="lazy"` attribute on `<img>` does this for you. The observer approach is still useful for custom behavior, like infinite scroll or loading components.

## 243: What is list virtualization (windowing)?

Instead of rendering 10,000 rows, you render only the rows visible in the viewport plus a few extra, and use padding or a tall spacer to keep the scrollbar right. As the user scrolls, you swap which rows are rendered. Libraries like TanStack Virtual and react-window do this. It is a mix of the Flyweight idea (reuse a small set of DOM nodes) and lazy rendering.

## 244: How do you handle many different actions with one delegated listener?

Put an action name in a data attribute and map names to handlers:

```js
const actions = {
  delete: (id) => removeItem(id),
  edit: (id) => openEditor(id),
  archive: (id) => archiveItem(id),
};

list.addEventListener("click", (e) => {
  const btn = e.target.closest("[data-action]");
  if (!btn || !list.contains(btn)) return;
  actions[btn.dataset.action]?.(btn.dataset.id);
});
```

```html
<button data-action="delete" data-id="42">Delete</button>
```

This combines event delegation, the Command pattern and a lookup table.

## 245: How does a Web Component react to attribute changes?

List the attributes in `static observedAttributes`, and the browser calls `attributeChangedCallback` when they change. This is the Observer pattern built into the platform.

```js
class UserBadge extends HTMLElement {
  static observedAttributes = ["name"];

  attributeChangedCallback(attr, oldValue, newValue) {
    if (attr === "name") this.textContent = `Hello, ${newValue}`;
  }
}

customElements.define("user-badge", UserBadge);
```

## 246: How do you implement feature flags in a clean way?

Keep flags behind one small module, so the rest of the code doesn't care where they come from (config file, remote service, query string).

```js
// flags.js
const defaults = { newCheckout: false, darkMode: true };
let flags = { ...defaults };

export async function loadFlags() {
  const remote = await fetch("/api/flags")
    .then((r) => r.json())
    .catch(() => ({}));
  flags = { ...defaults, ...remote };
}

export const isEnabled = (name) => Boolean(flags[name]);
```

Then use a strategy per flag at the boundary (`isEnabled("newCheckout") ? NewCheckout : OldCheckout`), not deep inside many functions. Remove flags when a feature is fully released, or they turn into dead code.

## 247: How would you combine Factory and Strategy for payment providers?

Each provider is a strategy with the same methods, and a factory picks one based on config or user choice.

```js
const providers = {
  stripe: () => ({ pay: (order) => stripeClient.charge(order.total) }),
  paypal: () => ({ pay: (order) => paypalClient.createPayment(order.total) }),
};

function getPaymentProvider(name) {
  const create = providers[name];
  if (!create) throw new Error(`Unsupported provider: ${name}`);
  return create();
}

await getPaymentProvider(user.paymentMethod).pay(order);
```

Checkout code only knows about `pay()`, so adding a provider doesn't touch it.

## 248: How do you design a plugin system with hooks?

The core defines named hook points. Plugins register handlers, and the core calls them at the right time.

```js
class Builder {
  hooks = { beforeBuild: [], transform: [], afterBuild: [] };

  use(plugin) {
    plugin(this);
    return this;
  }

  async build(files) {
    for (const fn of this.hooks.beforeBuild) await fn();
    let output = files;
    for (const fn of this.hooks.transform) output = await fn(output);
    for (const fn of this.hooks.afterBuild) await fn(output);
    return output;
  }
}

const minify = (b) => b.hooks.transform.push((files) => files.map(minifyFile));
new Builder().use(minify).build(files);
```

webpack's `tapable` and Rollup/Vite plugin hooks are more complete versions of this.

## 249: How do you write the Template Method pattern without classes?

Write a function that defines the steps and takes the variable parts as options:

```js
async function importData({ read, parse, validate = (rows) => rows, save }) {
  const raw = await read();
  const rows = parse(raw);
  const valid = validate(rows);
  await save(valid);
  return valid.length;
}

await importData({
  read: () => fs.readFile("users.csv", "utf8"),
  parse: parseCsv,
  save: (rows) => db.users.insertMany(rows),
});
```

The order of steps is fixed in one place, and callers only supply the parts that differ. Optional steps get defaults.

## 250: How would you implement a simple Visitor for a syntax tree?

Walk the tree and call the visitor method that matches each node type:

```js
function traverse(node, visitor) {
  visitor[node.type]?.(node);
  for (const child of node.children ?? []) traverse(child, visitor);
}

const ast = {
  type: "Program",
  children: [
    { type: "Call", name: "log", children: [{ type: "Number", value: 1 }] },
    { type: "Call", name: "alert", children: [] },
  ],
};

const calls = [];
traverse(ast, { Call: (node) => calls.push(node.name) });
calls; // ["log", "alert"]
```

New operations (counting, collecting, transforming) are new visitors. The tree and `traverse` stay the same.

## 251: How would you write a tiny expression evaluator with the Interpreter pattern?

Represent the expression as a tree of nodes. Each node type knows how to evaluate itself.

```js
const evaluate = (node, vars) => {
  switch (node.type) {
    case "num":
      return node.value;
    case "var":
      return vars[node.name];
    case "add":
      return evaluate(node.left, vars) + evaluate(node.right, vars);
    case "mul":
      return evaluate(node.left, vars) * evaluate(node.right, vars);
    default:
      throw new Error(`Unknown node: ${node.type}`);
  }
};

// (price * qty) + 5
const expr = {
  type: "add",
  left: {
    type: "mul",
    left: { type: "var", name: "price" },
    right: { type: "var", name: "qty" },
  },
  right: { type: "num", value: 5 },
};

evaluate(expr, { price: 10, qty: 2 }); // 25
```

This is a safe way to let users write simple formulas without using `eval`. You would add a parser to turn text into this tree.

## 252: Can you show the Bridge pattern with a real example?

Shapes (abstraction) draw themselves through a renderer (implementation). You can add new shapes and new renderers independently.

```js
const canvasRenderer = (ctx) => ({
  circle: (x, y, r) => {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
  },
});

const svgRenderer = (svg) => ({
  circle: (x, y, r) => {
    svg.insertAdjacentHTML(
      "beforeend",
      `<circle cx="${x}" cy="${y}" r="${r}" />`,
    );
  },
});

class Circle {
  constructor(renderer, x, y, r) {
    Object.assign(this, { renderer, x, y, r });
  }
  draw() {
    this.renderer.circle(this.x, this.y, this.r);
  }
}
```

Without the bridge you would need `CanvasCircle`, `SvgCircle`, `CanvasSquare`, `SvgSquare` and so on.

## 253: When is an Abstract Factory useful in front-end code?

When you need a group of objects that must match each other and the group can change as a whole. Examples:

- Different UI kits per platform (web, React Native) behind the same component names.
- Storage, network and logger implementations for browser vs server vs tests.
- Theme families where buttons, inputs and icons must match.

```js
const serverEnv = {
  createStorage: () => new MemoryStorage(),
  createLogger: () => pinoLogger,
};
const browserEnv = {
  createStorage: () => new LocalStorage(),
  createLogger: () => consoleLogger,
};

function createApp(env) {
  return { storage: env.createStorage(), logger: env.createLogger() };
}
```

## 254: How would you implement an object pool?

```js
class Pool {
  #free = [];

  constructor(create, reset) {
    this.create = create;
    this.reset = reset;
  }

  acquire() {
    return this.#free.pop() ?? this.create();
  }

  release(obj) {
    this.reset(obj);
    this.#free.push(obj);
  }
}

const particles = new Pool(
  () => ({ x: 0, y: 0, vx: 0, vy: 0 }),
  (p) => Object.assign(p, { x: 0, y: 0, vx: 0, vy: 0 }),
);

const p = particles.acquire();
// ... use it ...
particles.release(p);
```

The main bug risk is using an object after releasing it, since someone else may now own it.

## 255: What is the difference between dirty checking and the Observer approach to change detection?

With **dirty checking**, the framework doesn't know what changed, so after events it compares current values with old ones across the app (AngularJS's digest cycle, and Angular's Zone.js-based change detection is related). With **observers or signals**, data notifies only the code that depends on it, so the framework knows exactly what to update. Observers are faster for large apps but need special wrappers for state (signals, proxies, setters). Dirty checking works with plain objects but does more work.

## 256: What is the h() or createElement factory pattern?

A small factory function that creates DOM elements (or virtual DOM nodes) from a tag, props and children. JSX compiles to calls like this.

```js
function h(tag, props = {}, ...children) {
  const el = document.createElement(tag);
  for (const [key, value] of Object.entries(props)) {
    if (key.startsWith("on"))
      el.addEventListener(key.slice(2).toLowerCase(), value);
    else el.setAttribute(key, value);
  }
  el.append(...children);
  return el;
}

document.body.append(
  h("button", { class: "primary", onClick: () => alert("hi") }, "Click me"),
);
```

`append` treats string children as text, so this is safe from HTML injection.

## 257: How are tagged template literals used as a pattern?

A tag function receives the string parts and the values separately, so it can process the values before joining them. Libraries use this for safe HTML (lit's `html`), CSS-in-JS (`styled-components`), SQL with parameters, and GraphQL queries.

```js
function sql(strings, ...values) {
  return {
    text: strings.reduce((acc, s, i) => acc + "$" + i + s),
    values,
  };
}

sql`SELECT * FROM users WHERE id = ${id} AND role = ${role}`;
// { text: "SELECT * FROM users WHERE id = $1 AND role = $2", values: [id, role] }
```

The values are never pasted into the string, which protects against injection.

## 258: How do you build a pipeline with async steps?

```js
const pipeAsync =
  (...fns) =>
  (input) =>
    fns.reduce((promise, fn) => promise.then(fn), Promise.resolve(input));

const processUpload = pipeAsync(
  validateFile,
  resizeImage,
  uploadToStorage,
  saveMetadata,
);

await processUpload(file);
```

Each step takes the previous result and can be sync or async. If any step throws, the rest are skipped and the returned promise rejects.

## 259: How would you write a generic curry function?

Collect arguments until you have as many as the function expects (`fn.length`), then call it.

```js
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) return fn.apply(this, args);
    return (...more) => curried.apply(this, [...args, ...more]);
  };
}

const volume = curry((l, w, h) => l * w * h);
volume(2)(3)(4); // 24
volume(2, 3)(4); // 24
```

It doesn't work with rest parameters or default values, because `fn.length` doesn't count them.

## 260: What is point-free style?

Point-free style defines functions by combining other functions, without naming the arguments.

```js
// with arguments
const getActiveNames = (users) =>
  users.filter((u) => u.active).map((u) => u.name);

// point-free style
const prop = (key) => (obj) => obj[key];
const filter = (fn) => (arr) => arr.filter(fn);
const map = (fn) => (arr) => arr.map(fn);
const getActiveNames2 = pipe(filter(prop("active")), map(prop("name")));
```

It can be clean for small utilities, but too much of it makes code hard to read and debug.

## 261: How do you deep freeze an object?

`Object.freeze` is shallow, so freeze nested objects recursively:

```js
function deepFreeze(obj) {
  for (const value of Object.values(obj)) {
    if (value && typeof value === "object" && !Object.isFrozen(value)) {
      deepFreeze(value);
    }
  }
  return Object.freeze(obj);
}

const config = deepFreeze({ api: { url: "/api" } });
config.api.url = "x"; // throws in strict mode
```

Some teams use it in development only, to catch accidental mutations, and skip it in production because it costs time.

## 262: How does Immer let you "mutate" state immutably?

Immer gives your function a draft, which is a Proxy around the current state. When you change the draft, Immer records which parts changed. At the end, it builds a new state that copies only the changed parts and reuses the unchanged ones (structural sharing). It also freezes the result by default.

```js
import { produce } from "immer";

const next = produce(state, (draft) => {
  draft.todos[0].done = true;
});

next === state; // false
next.todos[1] === state.todos[1]; // true, unchanged parts are shared
```

Redux Toolkit uses Immer inside `createSlice`.

## 263: Why does reference equality matter for many patterns?

Memoization, React re-renders, selectors, `Set` and `Map` keys all compare objects by reference, not by content. `{ a: 1 } === { a: 1 }` is `false`. So if you create a new object or array on every call, caches miss and components re-render even when the data looks the same. On the other hand, if you mutate an object in place, the reference stays the same and change detection misses the update. Immutable updates with stable references for unchanged data solve both problems.

## 264: How do you test code that uses the Observer pattern?

Subscribe a spy (mock function), trigger the change, and check the calls. Also test that unsubscribing works.

```js
import { test, expect, vi } from "vitest";

test("notifies subscribers and stops after unsubscribe", () => {
  const store = createStore((s, a) => s + a.by, 0);
  const listener = vi.fn();

  const unsubscribe = store.subscribe(listener);
  store.dispatch({ by: 1 });
  unsubscribe();
  store.dispatch({ by: 1 });

  expect(listener).toHaveBeenCalledTimes(1);
});
```

## 265: How do you test debounced or throttled functions?

Use fake timers so you don't actually wait.

```js
import { test, expect, vi } from "vitest";

test("debounce calls once after the delay", () => {
  vi.useFakeTimers();
  const fn = vi.fn();
  const debounced = debounce(fn, 300);

  debounced("a");
  debounced("b");
  vi.advanceTimersByTime(299);
  expect(fn).not.toHaveBeenCalled();

  vi.advanceTimersByTime(1);
  expect(fn).toHaveBeenCalledWith("b");
  vi.useRealTimers();
});
```

Jest has the same API under `jest.useFakeTimers()` and `jest.advanceTimersByTime()`.

## 266: When should you mock a module and when should you use dependency injection?

Module mocking (`vi.mock("./api.js")`) is handy for code you can't easily change, like a third-party import, or for quick tests of existing code. But it ties the test to file paths and can leak between tests if not reset. Dependency injection makes the dependency a normal parameter, so tests just pass a fake, with no magic. For new code, prefer DI for things like API clients, storage and clocks. Use module mocks as a fallback.

## 267: What is a layered architecture in a front-end app?

You split code into layers that only depend on the layer below:

- **UI**: components and pages.
- **Application / state**: hooks, stores, use cases.
- **Domain**: business rules and models, with no framework code.
- **Infrastructure**: API clients, storage, analytics adapters.

The UI never calls `fetch` directly, and domain code never imports React. This keeps business rules testable and lets you change the UI framework or API without rewriting everything.

## 268: What is a feature-based folder structure?

Instead of grouping files by type (`components/`, `hooks/`, `services/`), you group them by feature:

```
src/
  features/
    cart/
      CartPage.jsx
      useCart.js
      cartApi.js
      index.js
    auth/
      ...
  shared/
    ui/
    lib/
```

Everything for a feature lives together, so changes stay local and features can be moved or deleted easily. It is the Module pattern applied to folders.

## 269: How do you keep a feature module's internals private?

Give each feature one `index.js` that exports its public API, and only allow imports through it.

```js
// features/cart/index.js
export { CartPage } from "./CartPage.jsx";
export { useCartCount } from "./useCartCount.js";
```

Other features import `features/cart`, never `features/cart/internal/...`. You can enforce this with ESLint rules (`no-restricted-imports`, `eslint-plugin-boundaries`) or with `exports` in a package's `package.json` in a monorepo.

## 270: How do polling, long polling and push compare as update patterns?

- **Polling**: the client asks every N seconds. Simple, but wasteful and slow to notice changes.
- **Long polling**: the client asks, and the server holds the request open until there is news. Fewer empty responses, but more complex.
- **Push** (WebSocket, Server-Sent Events): the server sends updates when they happen. This is the Observer pattern over the network. It is the fastest, but needs reconnect logic and server support.

For simple dashboards polling is often fine. For chat or live collaboration use push.

## 271: How do you write a WebSocket client that reconnects?

Wrap the socket and reconnect with backoff on close. Expose events so the rest of the app doesn't deal with the raw socket.

```js
class ReconnectingSocket extends EventTarget {
  #attempt = 0;
  #closed = false;

  constructor(url) {
    super();
    this.url = url;
    this.#connect();
  }

  #connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.#attempt = 0;
    };
    this.ws.onmessage = (e) =>
      this.dispatchEvent(new MessageEvent("message", { data: e.data }));
    this.ws.onclose = () => {
      if (this.#closed) return;
      const delay = Math.min(30_000, 1000 * 2 ** this.#attempt++);
      setTimeout(() => this.#connect(), delay);
    };
  }

  send(data) {
    if (this.ws.readyState === WebSocket.OPEN) this.ws.send(data);
  }

  close() {
    this.#closed = true;
    this.ws.close();
  }
}
```

In real apps you also queue messages while disconnected and resubscribe to topics after reconnecting.

## 272: What is the heartbeat pattern?

The client and server send small "ping" and "pong" messages at a regular interval. If one side doesn't hear back in time, it assumes the connection is dead and closes or reconnects. It is needed because a network can drop a connection silently, and the socket may still look open. WebSocket has ping/pong frames at the protocol level, but browsers don't expose them, so apps often send their own heartbeat messages.

## 273: How would you implement keyboard shortcuts with the Command pattern?

Map key combinations to command objects, so the same command can be triggered from a shortcut, a menu or a button.

```js
const commands = {
  save: { label: "Save", run: () => saveDocument() },
  undo: { label: "Undo", run: () => history.undo() },
};

const keymap = { "ctrl+s": "save", "ctrl+z": "undo" };

window.addEventListener("keydown", (e) => {
  const combo = `${e.ctrlKey || e.metaKey ? "ctrl+" : ""}${e.key.toLowerCase()}`;
  const name = keymap[combo];
  if (!name) return;
  e.preventDefault();
  commands[name].run();
});
```

Users can rebind keys by changing `keymap`, and a command palette can list everything in `commands`.

## 274: Snapshots or patches: how should you store undo history?

**Snapshots** store the whole state after each change. They are simple and with immutable data and structural sharing they are cheaper than they look. **Patches** (or inverse commands) store only what changed and how to undo it. They use less memory for large documents and can be sent over the network for collaboration. Immer can generate patches with `produceWithPatches`. Use snapshots for forms and small apps, and patches for large editors.

## 275: Can you give a JavaScript example of dependency inversion?

High-level code should depend on an abstraction it defines, and low-level code should implement it.

```js
// high level: only needs "something with save(key, value)"
class DraftService {
  constructor(store) {
    this.store = store;
  }
  saveDraft(id, text) {
    return this.store.save(`draft:${id}`, text);
  }
}

// low level implementations
const localStore = { save: async (k, v) => localStorage.setItem(k, v) };
const apiStore = {
  save: (k, v) => fetch(`/api/kv/${k}`, { method: "PUT", body: v }),
};

new DraftService(localStore);
new DraftService(apiStore);
```

`DraftService` doesn't import `localStorage` or `fetch`, so it doesn't change when storage changes.

## 276: What does the Liskov Substitution Principle look like in JavaScript?

A subclass (or any object that claims to follow an interface) must work wherever the original works, without surprises. The classic violation:

```js
class Rectangle {
  setWidth(w) {
    this.width = w;
  }
  setHeight(h) {
    this.height = h;
  }
  area() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  setWidth(w) {
    this.width = this.height = w;
  }
  setHeight(h) {
    this.width = this.height = h;
  }
}

const r = new Square();
r.setWidth(2);
r.setHeight(3);
r.area(); // 9, but code written for Rectangle expects 6
```

In JavaScript the same idea applies to duck typing: a fake or adapter must behave like the real thing, including errors and return types, not just have the same method names.

## 277: What does Interface Segregation mean when JavaScript has no interfaces?

Don't make code depend on a big object when it only needs a small part of it. For example, a function that only needs to read the current user shouldn't receive the whole `store` with `dispatch`, `subscribe` and everything else.

```js
// too much
function renderHeader(store) {
  return store.getState().user.name;
}

// only what it needs
function renderHeader(userName) {
  return userName;
}
```

Smaller dependencies make code easier to test and reuse, and in React they also mean fewer re-renders.

## 278: What is the Delegation pattern?

An object hands off work to another object it holds, instead of inheriting from it. The outer object exposes methods that forward to the inner one.

```js
class Logger {
  log(msg) {
    console.log(msg);
  }
}

class UserService {
  #logger = new Logger();

  log(msg) {
    this.#logger.log(`[users] ${msg}`); // delegate
  }
}
```

It is how you get "composition over inheritance": you can replace the delegate, and you only expose what you want.

## 279: What is OLOO, and how is it different from classes?

OLOO (Objects Linked to Other Objects), a name from Kyle Simpson, is a style that uses `Object.create` to link plain objects together instead of using classes or constructors.

```js
const Widget = {
  init(width) {
    this.width = width;
    return this;
  },
  describe() {
    return `Widget ${this.width}px`;
  },
};

const Button = Object.create(Widget);
Button.setup = function (width, label) {
  this.init(width);
  this.label = label;
  return this;
};

const btn = Object.create(Button).setup(100, "OK");
btn.describe(); // "Widget 100px"
```

It shows prototypes as they really are (delegation between objects). Classes are more common today because tools, types and teammates expect them.

## 280: Which ways to make data private exist, and how do they compare?

- **`#private` fields**: real privacy, enforced by the language, fast. Only for classes.
- **Closures**: real privacy, work with factory functions, but methods are created per object.
- **`WeakMap`**: real privacy, works with classes, but more code. Mostly legacy now.
- **Symbols**: hidden from normal loops and `JSON.stringify`, but still reachable with `Object.getOwnPropertySymbols`.
- **`_underscore` convention**: not private at all, only a hint.

Use `#private` in classes and closures in factory functions.

## 281: How do you use Object.defineProperty in patterns?

It gives fine control over a property: read-only, hidden from loops, or computed with a getter.

```js
const user = { first: "Ana", last: "Lee" };

Object.defineProperty(user, "fullName", {
  get() {
    return `${this.first} ${this.last}`;
  },
  enumerable: false,
});

Object.defineProperty(user, "id", { value: 7, writable: false });

user.fullName; // "Ana Lee"
Object.keys(user); // ["first", "last"]
```

Vue 2 used it to make reactive objects, before Vue 3 switched to `Proxy`.

## 282: How would you build a very small signals implementation?

A signal tracks which effect is currently running when it is read, and reruns those effects when it is written.

```js
let currentEffect = null;

function signal(value) {
  const subscribers = new Set();
  return {
    get() {
      if (currentEffect) subscribers.add(currentEffect);
      return value;
    },
    set(next) {
      if (Object.is(next, value)) return;
      value = next;
      [...subscribers].forEach((fn) => fn());
    },
  };
}

function effect(fn) {
  const run = () => {
    currentEffect = run;
    try {
      fn();
    } finally {
      currentEffect = null;
    }
  };
  run();
}

const count = signal(0);
effect(() => console.log("count is", count.get()));
count.set(1); // logs "count is 1"
```

Real libraries also handle nested effects, cleanup, batching and computed values.

## 283: What is derived state, and how should you handle it?

Derived state is data you can calculate from other state, like a filtered list or a cart total. Don't store it separately, because then you have to keep two things in sync. Compute it when needed, and memoize the calculation if it is expensive.

```js
// avoid: storing total and updating it by hand
// prefer:
const getTotal = (cart) => cart.items.reduce((s, i) => s + i.price * i.qty, 0);
```

Computed signals, memoized selectors and `useMemo` are all tools for this.

## 284: What does normalizing state mean?

It means storing each entity once, in a lookup by id, and referring to it by id elsewhere, like tables in a database.

```js
const state = {
  users: {
    byId: { u1: { id: "u1", name: "Ana" } },
    allIds: ["u1"],
  },
  posts: {
    byId: { p1: { id: "p1", title: "Hi", authorId: "u1" } },
    allIds: ["p1"],
  },
};
```

Updating a user then changes one place instead of every post that embeds the user. Redux Toolkit's `createEntityAdapter` helps you manage this shape.

## 285: How would you use a Facade to simplify a checkout flow?

The page calls one function, and the facade coordinates several services:

```js
export async function placeOrder(cart, paymentDetails) {
  const stock = await inventory.reserve(cart.items);
  try {
    const payment = await payments.charge(cart.total, paymentDetails);
    const order = await orders.create({ cart, paymentId: payment.id });
    analytics.track("order_placed", { total: cart.total });
    return order;
  } catch (err) {
    await inventory.release(stock.reservationId);
    throw err;
  }
}
```

The UI doesn't need to know the order of calls or how to roll back. The facade is also a good place for logging and error handling.

## 286: How do you build an API client with interceptors?

Keep a list of request and response handlers and run them around each call. This is Chain of Responsibility.

```js
function createClient(baseUrl) {
  const requestInterceptors = [];
  const responseInterceptors = [];

  async function request(path, init = {}) {
    let config = { ...init, headers: new Headers(init.headers) };
    for (const fn of requestInterceptors) config = await fn(config);

    let res = await fetch(baseUrl + path, config);
    for (const fn of responseInterceptors) res = await fn(res, config);
    return res;
  }

  return {
    request,
    onRequest: (fn) => requestInterceptors.push(fn),
    onResponse: (fn) => responseInterceptors.push(fn),
  };
}

const api = createClient("/api");
api.onRequest((config) => {
  config.headers.set("Authorization", `Bearer ${getToken()}`);
  return config;
});
```

Axios, ky and Angular's `HttpClient` all have built-in versions of this.

## 287: What is graceful degradation?

You build the full experience for modern environments and make sure the app still works, maybe with fewer features, when something is missing or fails. For example, if the recommendations API is down, you show the product page without recommendations instead of an error page. In code this often means fallbacks around optional features:

```js
const recommendations = await getRecommendations(id).catch(() => []);
```

## 288: What is progressive enhancement?

It is the opposite direction from graceful degradation: you start with a basic version that works everywhere (plain HTML forms and links), then add JavaScript to make it better when it is available. A form that posts to the server normally but uses `fetch` and shows inline errors when JS has loaded is a typical example. Frameworks like Remix (now React Router) and SvelteKit encourage it.

## 289: Which design patterns can you spot in Express?

- **Chain of Responsibility / Middleware**: `app.use` and `next()`.
- **Facade**: `res.json()`, `res.redirect()` hide the raw Node.js `http` API.
- **Decorator-like extension**: Express adds methods to `req` and `res`.
- **Router as Composite**: routers can be mounted inside other routers.
- **Factory**: `express()` and `express.Router()` create the objects.
- **Observer**: the underlying server is an `EventEmitter`.

## 290: Which design patterns can you spot in React?

- **Composite**: components contain components, forming a tree.
- **Observer**: state and context updates notify the components that use them.
- **Provider**: Context.
- **Decorator**: HOCs.
- **Strategy**: passing render functions or components as props.
- **Command**: `useReducer` actions.
- **Flyweight-like reuse**: React reuses DOM nodes during reconciliation instead of creating new ones.
- **Inversion of control**: React calls your components and effects, you don't.

## 291: What is the Specification pattern?

A specification is an object (or function) that answers "does this item meet the rule?". Specifications can be combined with `and`, `or` and `not` to build complex rules from small ones.

```js
const spec = (test) => ({
  test,
  and: (other) => spec((x) => test(x) && other.test(x)),
  or: (other) => spec((x) => test(x) || other.test(x)),
  not: () => spec((x) => !test(x)),
});

const isAdult = spec((u) => u.age >= 18);
const isActive = spec((u) => u.active);
const canVote = isAdult.and(isActive);

users.filter(canVote.test);
```

It is useful for filters, permissions and validation rules that users can configure.

## 292: What is the Strangler Fig pattern?

It is a way to replace an old system piece by piece instead of rewriting it all at once. You put a layer in front (a router, proxy or shell app) that sends some routes or features to the new code and the rest to the old code. Over time more traffic goes to the new code until the old one can be removed. In front-end work it is often used to move from AngularJS or jQuery to a modern framework one page at a time.

## 293: What is the Backend for Frontend (BFF) pattern?

A BFF is a small server built specifically for one client (web, mobile). It calls the general back-end services, combines and reshapes the data, and returns exactly what that client needs. It is a Facade and an Adapter at the architecture level. It reduces the number of requests from the browser and can keep secrets (API keys, tokens) on the server. Next.js route handlers and server actions are often used as a BFF.

## 294: What is the Saga pattern in front-end state management?

A saga is a long-running process that listens for actions and runs a sequence of side effects in response, like "when the user logs in, load the profile, then the settings, then start polling notifications". redux-saga implements it with generators, which makes async flows easy to test step by step. Today simpler tools like thunks, RTK listener middleware or TanStack Query cover most of these cases, but you will see sagas in existing apps.

## 295: What is the Unit of Work pattern?

A Unit of Work keeps track of all changes made during a business operation and saves them together at the end, ideally in one transaction or one request. In the front end, it can look like collecting form edits across several tabs and sending them in one batch when the user clicks "Save", instead of saving each field separately. ORMs like MikroORM use it on the server.

## 296: How does request batching work, like in DataLoader?

Instead of sending one request per item, you collect all requests made in the same tick and send them as one batch.

```js
function createBatcher(batchFn) {
  let queue = [];

  return (key) => {
    const { promise, resolve, reject } = Promise.withResolvers();
    queue.push({ key, resolve, reject });

    if (queue.length === 1) {
      queueMicrotask(async () => {
        const batch = queue;
        queue = [];
        try {
          const results = await batchFn(batch.map((b) => b.key));
          batch.forEach((b, i) => b.resolve(results[i]));
        } catch (err) {
          batch.forEach((b) => b.reject(err));
        }
      });
    }
    return promise;
  };
}

const loadUser = createBatcher((ids) => api.getUsers(ids));
await Promise.all([loadUser(1), loadUser(2)]); // one request
```

This is a common fix for the N+1 problem in GraphQL resolvers.

## 297: What is event-driven architecture?

In an event-driven system, parts of the app communicate by publishing events ("orderPlaced") instead of calling each other directly. Other parts subscribe and react. It is Pub/Sub at the architecture level. It makes parts loosely coupled and easy to extend, but the flow is harder to follow and debug, and you need to think about event order, duplicates and failures. In the browser you see it with custom events and event buses; on the back end with message brokers like Kafka or RabbitMQ.

## 298: How do you schedule work so it doesn't block the UI?

Pick the right queue for the job:

- `queueMicrotask` / `Promise.then`: run right after the current task, before rendering. Good for batching, but long work here still blocks.
- `setTimeout(fn, 0)`: run in a later task, letting the browser render in between.
- `requestAnimationFrame`: run before the next paint, for visual updates.
- `requestIdleCallback`: run when the browser is idle, for low-priority work.
- `scheduler.postTask()` and `scheduler.yield()`: newer APIs with priorities, supported in Chromium-based browsers (check support before relying on them).

For long tasks, split the work into chunks and yield between them.

## 299: How do you split a long task into chunks?

Process part of the work, then give control back to the browser before continuing.

```js
const yieldToMain = () =>
  globalThis.scheduler?.yield?.() ?? new Promise((r) => setTimeout(r, 0));

async function processAll(items, handle) {
  let last = performance.now();
  for (const item of items) {
    handle(item);
    if (performance.now() - last > 50) {
      await yieldToMain();
      last = performance.now();
    }
  }
}
```

This keeps the page responsive to clicks and typing during heavy work and helps the INP metric.

## 300: How do you refactor existing code toward a design pattern safely?

1. Make sure there are tests around the behavior you will change, or add some first.
2. Find the actual pain: repeated `switch` blocks, copy-pasted code, hard-to-test dependencies.
3. Change in small steps. For example, first pull each `case` into a function, then move them into a lookup object, then let callers register new ones.
4. Run tests after each step and keep the public API the same.
5. Stop when the code is clear enough. You don't need the "full" textbook version of the pattern.

# Advanced Questions (301-450)

## 301: Why does an ES module behave like a singleton, and where does that stop being true?

The host keeps a module map keyed by the resolved URL (or file path in Node). The first `import` loads, links and evaluates the module, and every later import of the same URL gets the same module record and the same exported objects. It stops being true when the key is different: `./a.js?v=1` and `./a.js?v=2` are two modules, a package installed twice is two modules, and each realm (iframe, worker, Node `vm` context) has its own module map. So a "singleton" is really "one per module map", not one per app.

## 302: What problems do multiple realms cause for patterns that use instanceof?

Each realm (window, iframe, worker) has its own set of built-ins. An array created in an iframe is not `instanceof Array` in the parent, because its prototype is the iframe's `Array.prototype`.

```js
const iframeArray = iframe.contentWindow.Array;
const arr = new iframeArray();
arr instanceof Array; // false
Array.isArray(arr); // true
```

Patterns that check types with `instanceof` (error handling, factories, visitors) can fail across realms or across duplicated packages. Prefer brand checks like `Array.isArray`, `Error.isError` where available, a `Symbol.for()` brand, or duck typing.

## 303: How can you share a singleton across separately bundled code?

Store it on `globalThis` under a key from the global symbol registry. `Symbol.for(key)` returns the same symbol everywhere in the same realm, even across bundles.

```js
const KEY = Symbol.for("my-lib.registry");

export const registry = (globalThis[KEY] ??= new Map());
```

Libraries like React DevTools hooks and some state libraries use this. Use it with care: it is global state, and versions of your library must agree on the shape of what is stored there.

## 304: Why can instanceof break with duplicated packages, and how do libraries deal with it?

If two versions of a library are installed, each has its own class. An error created by version A is not `instanceof` the class from version B, so `catch (e) { if (e instanceof HttpError) ... }` silently fails. Libraries fix this with brand checks:

```js
const BRAND = Symbol.for("my-lib.HttpError");

class HttpError extends Error {
  [BRAND] = true;
  static isHttpError(value) {
    return Boolean(value?.[BRAND]);
  }
}
```

Axios uses `axios.isAxiosError()` and Redux Toolkit uses `.match()` on action creators for similar reasons.

## 305: What is Symbol.hasInstance, and when would you use it?

It lets a class decide what `instanceof` returns. You can use it to make `instanceof` work by duck typing or by a brand:

```js
class Iterable {
  static [Symbol.hasInstance](value) {
    return value != null && typeof value[Symbol.iterator] === "function";
  }
}

[] instanceof Iterable; // true
"abc" instanceof Iterable; // true
```

It is rarely needed, and it can confuse readers, so use it only when a brand check really should look like `instanceof`.

## 306: What are Proxy invariants?

Invariants are rules a proxy trap is not allowed to break, so proxies can't lie about certain facts of the target. For example, if the target has a non-configurable, non-writable property, the `get` trap must return its real value. If the target is not extensible, `ownKeys` must report exactly its keys. Breaking an invariant throws a `TypeError`. This matters when you proxy frozen objects: you can't make a frozen object's property look different through a proxy.

```js
const frozen = Object.freeze({ a: 1 });
const p = new Proxy(frozen, { get: () => 2 });
p.a; // TypeError: invariant violated
```

## 307: What is the performance cost of Proxy?

Every operation on a proxy goes through a trap function, so property access is much slower than on a plain object, and engines can't optimize it as well. For state objects that are read a few times per render this doesn't matter. In hot loops (processing big arrays, game loops) it does. Vue and MobX reduce the cost by only proxying objects that are actually used, caching proxies, and letting you mark large data as non-reactive (`markRaw`, `shallowRef`).

## 308: What identity problems come with proxies?

A proxy is a different object from its target: `proxy !== target`. This causes bugs when:

- Code stores the target in a `Set`, `Map` or `WeakMap` and later looks it up with the proxy, or the other way around.
- Two different proxies are created for the same target, so equality checks fail.
- Methods are called with `this` set to the proxy and use internal slots or private fields.

Libraries keep a `WeakMap` from target to proxy so the same target always gets the same proxy, and provide a "toRaw" function to get the original back.

## 309: Why do private class fields not work through a Proxy?

Private fields are stored on the exact object instance, not looked up through `get`. When a method runs with `this` set to the proxy, `this.#x` looks for the field on the proxy, which doesn't have it, and throws.

```js
class Counter {
  #count = 0;
  inc() {
    return ++this.#count;
  }
}

const p = new Proxy(new Counter(), {});
p.inc(); // TypeError: Cannot read private member
```

Fix it by binding methods to the target in the `get` trap, or don't proxy classes that use private fields.

## 310: Why is proxying Map, Set or Date tricky?

Their methods read internal slots (like `[[MapData]]`) on `this`. When you call `proxy.get(key)`, the method gets the proxy as `this`, which has no internal slot, so it throws `TypeError: Method Map.prototype.get called on incompatible receiver`. You have to wrap methods in the `get` trap:

```js
const reactiveMap = (map, onChange) =>
  new Proxy(map, {
    get(target, prop) {
      const value = Reflect.get(target, prop, target); // receiver = target
      if (typeof value !== "function") return value;
      return (...args) => {
        const result = value.apply(target, args);
        if (prop === "set" || prop === "delete" || prop === "clear") onChange();
        return result;
      };
    },
  });
```

Vue has special "collection handlers" for this reason.

## 311: What is the membrane pattern?

A membrane wraps an object graph so that everything you get from it is also wrapped. If you read a property that is an object, you get a proxy of it, and functions you pass in get wrapped on the way in. This lets you control or revoke access to a whole graph, not just the top object. It is used for sandboxing untrusted code, for read-only views of state, and in deep reactive systems. Keeping identity right (the same object always gets the same proxy) is the hard part, so membranes keep `WeakMap`s in both directions.

## 312: How does a deep reactive system avoid wrapping the whole object tree up front?

It wraps lazily. The top-level proxy's `get` trap checks if the value is an object, and only then wraps it, and caches the wrapper in a `WeakMap` so it is created once.

```js
const cache = new WeakMap();

function reactive(obj) {
  if (cache.has(obj)) return cache.get(obj);
  const proxy = new Proxy(obj, {
    get(target, key, receiver) {
      track(target, key);
      const value = Reflect.get(target, key, receiver);
      return value !== null && typeof value === "object"
        ? reactive(value)
        : value;
    },
    set(target, key, value, receiver) {
      const result = Reflect.set(target, key, value, receiver);
      trigger(target, key);
      return result;
    },
  });
  cache.set(obj, proxy);
  return proxy;
}
```

This is close to how Vue 3 works. Large objects that are never read in detail never get wrapped.

## 313: What is the "diamond problem" or glitch in reactive systems?

If `c` depends on `a` and `b`, and both `a` and `b` depend on `source`, a naive push-based observer system updates `c` twice when `source` changes, and the first time with one new and one old input. That temporary wrong value is a glitch.

```
     source
     /    \
    a      b
     \    /
       c
```

Glitch-free systems (modern signal libraries) first mark everything downstream as dirty, then recompute in dependency order, or compute lazily when the value is read, so `c` runs once with consistent inputs.

## 314: What is the difference between push, pull and push-pull reactivity?

- **Push**: the source sends new values to subscribers right away (classic Observer, RxJS). Simple, but can cause glitches and wasted work.
- **Pull**: consumers ask for the current value when they need it (polling, plain getters). Always consistent, but you don't know when to ask.
- **Push-pull**: the source pushes a "something changed" notification, and values are recomputed lazily when read. Most signal libraries (Solid, Preact Signals, Angular signals, the TC39 proposal) work this way. You get consistency and avoid computing things nobody reads.

## 315: How do you batch notifications in an observer-based store?

Delay notifications until a batch of changes is done, and notify each subscriber once.

```js
let depth = 0;
const pending = new Set();

function batch(fn) {
  depth++;
  try {
    fn();
  } finally {
    if (--depth === 0) {
      const toRun = [...pending];
      pending.clear();
      toRun.forEach((sub) => sub());
    }
  }
}

function notify(subscribers) {
  for (const sub of subscribers) {
    if (depth > 0) pending.add(sub);
    else sub();
  }
}
```

React batches state updates automatically since React 18, and most signal libraries offer a `batch` function.

## 316: What happens if a subscriber emits a new event while the subject is still notifying?

This is re-entrancy. If the subject loops over listeners and a listener triggers another `emit`, the second notification runs in the middle of the first. Some listeners then see events out of order, or see the second state before the first. Fixes:

- Queue events and drain the queue in a loop, so each event finishes before the next starts.
- Copy the listener list before looping, so adding or removing listeners doesn't affect the current loop.
- Detect and limit recursion depth to avoid infinite loops.

```js
const queue = [];
let draining = false;

function emit(event) {
  queue.push(event);
  if (draining) return;
  draining = true;
  try {
    while (queue.length) {
      const e = queue.shift();
      for (const l of [...listeners]) l(e);
    }
  } finally {
    draining = false;
  }
}
```

## 317: Should observer notifications be sync or async?

**Sync** notifications are predictable and easy to debug (stack traces show the cause), and subscribers see the change right away. But a slow subscriber blocks the emitter, and re-entrancy problems are more likely. **Async** notifications (microtask or later) isolate the emitter from subscribers and allow batching, but the state may change again before subscribers run, and stack traces get split. DOM events are sync when you call `dispatchEvent`. `MutationObserver` delivers in a microtask with all changes batched. Pick one and document it.

## 318: What does "don't release Zalgo" mean?

It means a function that takes a callback should be either always sync or always async, never sometimes one and sometimes the other.

```js
// bad: sync when cached, async otherwise
function getUser(id, cb) {
  if (cache.has(id)) return cb(cache.get(id));
  fetchUser(id).then(cb);
}

// good: always async
function getUser(id, cb) {
  if (cache.has(id)) return queueMicrotask(() => cb(cache.get(id)));
  fetchUser(id).then(cb);
}
```

Mixed behavior causes bugs where code after the call runs before or after the callback depending on the cache. Promises solve this by design, because `.then` callbacks always run asynchronously.

## 319: Can WeakRef and FinalizationRegistry be used to build weak observers?

Technically yes: the subject can hold `WeakRef`s to listeners and drop them once they are garbage collected. But garbage collection timing is not predictable. A dead component may keep receiving events for a while, or forever if something else still references it. Engines also don't promise that finalization callbacks run at all. TC39 itself recommends avoiding these APIs for program logic. Use explicit unsubscribe (or `AbortSignal` with `addEventListener`) for correctness, and use weak references only as an extra safety net or for caches.

## 320: How do you find memory leaks caused by patterns like Observer or caches in a single-page app?

1. Repeat an action that should free memory (open and close a modal 20 times, navigate back and forth).
2. Take heap snapshots in Chrome DevTools before and after, and compare them.
3. Look for growing counts of your components, "Detached" DOM nodes, listeners and closures.
4. Follow the retainers path to see who holds the reference: often a global event bus, a module-level cache, a `setInterval`, or a listener on `window`.

The usual fixes are unsubscribing on cleanup, using `AbortController` for listeners, limiting cache size, and using `WeakMap` for per-object data.

## 321: How can closures cause memory leaks?

A closure keeps alive the variables it uses. Engines usually only keep what the closure actually references, but closures created in the same scope can share one context, so a small closure can keep a large object alive because a sibling closure uses it.

```js
function setup() {
  const bigData = new Array(1_000_000).fill("x");
  const unused = () => bigData.length; // keeps bigData in the shared context
  return () => console.log("tick"); // may keep bigData alive too in some engines
}

setInterval(setup(), 1000);
```

When a long-lived callback (timer, global listener) is created inside a function that also handles big data, move the callback out or clear references (`bigData = null`) when done.

## 322: Do factory functions or classes perform better in V8?

For many instances, classes are usually better: methods live once on the prototype, while factory functions that return object literals with methods create new function objects per instance. Both produce objects with stable "shapes" (hidden classes) if you always add the same properties in the same order. Performance problems come more from changing shapes (adding properties later, deleting properties) than from class vs factory. For a few hundred objects the difference doesn't matter. Choose based on readability unless profiling says otherwise.

## 323: What are hidden classes, and how do patterns affect them?

V8 gives objects internal "shapes" (hidden classes) based on which properties they have and in what order. Code that always sees objects with the same shape can be optimized with inline caches. Patterns that hurt this:

- Mixins that add methods to instances at different times.
- Decorators or builders that add properties conditionally.
- `delete obj.prop`, which often moves the object to a slower dictionary mode.

Initialize all fields in the constructor (class fields help with that), even with `null`, and avoid adding or deleting properties later on hot objects.

## 324: What is a megamorphic call site, and can Strategy or polymorphism cause it?

A call site like `shape.area()` is monomorphic if it always sees one object shape, polymorphic if it sees a few (V8 handles up to 4 well), and megamorphic if it sees many. Megamorphic sites lose fast inline caches and use a slower generic lookup. A Strategy or Visitor loop that calls methods on dozens of different object types can become megamorphic. Usually it doesn't matter, but in hot paths (rendering engines, parsers) you can keep shapes uniform, for example by storing strategies as functions on objects of one shape.

## 325: When does object pooling hurt instead of help in JavaScript?

Modern garbage collectors are generational: short-lived objects are cheap to allocate and cheap to collect in the young generation. Pooled objects live long, get promoted to the old generation, and can make major collections more expensive. Pools also add bugs (using an object after release) and code complexity. Pooling helps when objects are expensive to set up (WebGL buffers, canvas, DOM nodes in virtual lists, workers, connections) or when you must avoid GC pauses at 60fps. For plain small objects, measure before pooling.

## 326: How do persistent data structures support immutable patterns at scale?

Copying a whole array or object on every change is O(n). Persistent data structures (like the hash array mapped tries used in Immutable.js) store data in a tree, so an update copies only the path from the root to the changed leaf, which is O(log n), and shares everything else with the previous version. Every old version stays valid, which is great for undo and time travel. The cost is a different API from plain objects and conversions at the edges. Immer gives you structural sharing with plain objects instead, which is why most apps use it now.

## 327: When is it fine to mutate inside an "immutable" codebase?

Mutating a value nobody else can see yet is safe. For example, building a new array inside a function with `push` in a loop and returning it is faster than repeated spreading, and the outside world still only sees an immutable result.

```js
function toLookup(items) {
  const result = {};
  for (const item of items) result[item.id] = item; // local mutation
  return result; // treated as immutable from now on
}
```

The rule is: no one should observe the mutation. Immer drafts and "transient" builders in persistent libraries use the same idea.

## 328: How can recursive promise patterns starve the event loop?

Microtasks run until the microtask queue is empty, before the browser can render or handle input. If each `.then` schedules another microtask without ever waiting for a real task (timer, I/O), the page freezes even though the code is "async".

```js
async function loop() {
  while (true) {
    await null; // only a microtask, never yields to rendering
    doWork();
  }
}
```

Yield to the task queue (`setTimeout`, `scheduler.yield()`, `MessageChannel`) in long-running async loops.

## 329: How do you handle backpressure in a producer/consumer pipeline?

Backpressure means a slow consumer can tell a fast producer to slow down, so data doesn't pile up in memory. Web Streams have it built in: a `ReadableStream` with a `pull` method only produces when the consumer asks for more, and `highWaterMark` sets how much can be buffered.

```js
const numbers = new ReadableStream({
  start() {
    this.n = 0;
  },
  pull(controller) {
    controller.enqueue(this.n++); // called only when there is room
    if (this.n > 1000) controller.close();
  },
});
```

Async generators also have natural backpressure: the producer pauses at `yield` until the consumer calls `next()`.

## 330: How do you build a processing pipeline with Web Streams?

Chain `TransformStream`s with `pipeThrough` and finish with `pipeTo`. Each stage handles one job, and backpressure works through the whole chain.

```js
const res = await fetch("/logs.ndjson");

await res.body
  .pipeThrough(new TextDecoderStream())
  .pipeThrough(splitLines())
  .pipeThrough(
    new TransformStream({
      transform(line, controller) {
        if (line) controller.enqueue(JSON.parse(line));
      },
    }),
  )
  .pipeTo(new WritableStream({ write: (entry) => render(entry) }));

function splitLines() {
  let buffer = "";
  return new TransformStream({
    transform(chunk, controller) {
      buffer += chunk;
      const lines = buffer.split("\n");
      buffer = lines.pop();
      lines.forEach((l) => controller.enqueue(l));
    },
    flush(controller) {
      if (buffer) controller.enqueue(buffer);
    },
  });
}
```

This processes a large response without loading all of it into memory.

## 331: How do you combine several cancellation reasons into one signal?

Use `AbortSignal.any()`. It returns a signal that aborts when any of the given signals abort.

```js
async function load(url, { signal } = {}) {
  const combined = AbortSignal.any(
    [signal, AbortSignal.timeout(10_000)].filter(Boolean),
  );
  return fetch(url, { signal: combined });
}

const controller = new AbortController();
load("/api/data", { signal: controller.signal });
// cancelled by the user OR by the timeout, whichever happens first
```

Accepting a `signal` option in your own async functions and passing it down is the standard cancellation pattern in modern JavaScript.

## 332: What is explicit resource management (using and Symbol.dispose)?

It is a newer language feature for cleanup. An object with a `[Symbol.dispose]()` method (or `[Symbol.asyncDispose]()`) can be declared with `using` (or `await using`), and it is disposed automatically when the block ends, even if an error is thrown.

```js
function openTempFile() {
  const handle = createHandle();
  return {
    handle,
    [Symbol.dispose]() {
      handle.close();
    },
  };
}

{
  using file = openTempFile();
  write(file.handle);
} // file is disposed here
```

`DisposableStack` helps collect several cleanups. It is supported in recent Chromium browsers, Firefox and Node.js 24+, and TypeScript 5.2+ can compile it. Check support for your targets before relying on it. It replaces many `try/finally` cleanup patterns.

## 333: What is the Circuit Breaker pattern?

A circuit breaker stops calling a failing service for a while, so you fail fast instead of piling up slow requests. It has three states: **closed** (calls go through), **open** (calls fail immediately), and **half-open** (after a cooldown, one test call is allowed; success closes it, failure opens it again).

```js
function circuitBreaker(fn, { threshold = 5, cooldown = 10_000 } = {}) {
  let failures = 0;
  let openedAt = 0;

  return async (...args) => {
    if (failures >= threshold && Date.now() - openedAt < cooldown) {
      throw new Error("Circuit open");
    }
    try {
      const result = await fn(...args);
      failures = 0;
      return result;
    } catch (err) {
      failures++;
      if (failures >= threshold) openedAt = Date.now();
      throw err;
    }
  };
}
```

It is mostly a back-end pattern, but it is also useful in front ends that call flaky third-party APIs.

## 334: What is the Bulkhead pattern?

Bulkhead splits resources into separate pools, so a problem in one area can't use up everything. For example, give image uploads their own concurrency limit of 2 and API calls their own limit of 6. If uploads hang, API calls still work. In Node.js it can mean separate connection pools or worker pools per downstream service. The name comes from ship compartments that keep one leak from sinking the whole ship.

## 335: How would you implement a client-side rate limiter?

A token bucket allows short bursts but limits the average rate.

```js
function tokenBucket({ capacity, refillPerSecond }) {
  let tokens = capacity;
  let last = Date.now();

  return function tryTake() {
    const now = Date.now();
    tokens = Math.min(
      capacity,
      tokens + ((now - last) / 1000) * refillPerSecond,
    );
    last = now;
    if (tokens < 1) return false;
    tokens -= 1;
    return true;
  };
}

const canSend = tokenBucket({ capacity: 10, refillPerSecond: 2 });
if (canSend()) sendEvent();
```

Client-side limits protect the server and your quota, but they are not security: the server must enforce its own limits.

## 336: Why are idempotency keys important when combining retries with writes?

If a POST times out, you don't know if the server processed it. Retrying may charge a card twice. With an idempotency key, the client generates a unique id per logical operation and sends it with every attempt. The server stores results by key and returns the same result for repeats instead of doing the work again.

```js
const key = crypto.randomUUID();
await retry(() =>
  fetch("/api/payments", {
    method: "POST",
    headers: { "Idempotency-Key": key },
    body: JSON.stringify(payment),
  }),
);
```

Generate the key once per user action, not per attempt.

## 337: How do you avoid out-of-order responses in a search-as-you-type feature?

Requests can finish in a different order than they were sent, so an old response can overwrite a newer one. Options:

- Abort the previous request when starting a new one (`AbortController`).
- Keep a request id and ignore responses that are not the latest.
- Use RxJS `switchMap`, which does both.

```js
let controller;

async function search(query) {
  controller?.abort();
  controller = new AbortController();
  try {
    const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: controller.signal,
    });
    render(await res.json());
  } catch (err) {
    if (err.name !== "AbortError") throw err;
  }
}
```

## 338: What is the stale closure problem in React hooks?

A callback created during one render captures the props and state of that render. If it runs later (in an interval, a subscription or a memoized handler with missing dependencies), it sees old values.

```jsx
function Timer() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setCount(count + 1), 1000); // count is always 0
    return () => clearInterval(id);
  }, []);
}
```

Fixes: use the updater form `setCount((c) => c + 1)`, include correct dependencies, keep the latest value in a ref, or use `useEffectEvent` for event-like logic inside effects (stable in React 19.2). It is a general closure issue, not just React.

## 339: How do you implement a mutex in JavaScript?

JavaScript runs your code on one thread, but async functions can interleave at `await` points. A mutex makes sure only one async section runs at a time.

```js
class Mutex {
  #last = Promise.resolve();

  async lock() {
    let release;
    const next = new Promise((r) => (release = r));
    const previous = this.#last;
    this.#last = previous.then(() => next);
    await previous;
    return release;
  }
}

const mutex = new Mutex();

async function refreshToken() {
  const release = await mutex.lock();
  try {
    if (!isExpired()) return;
    await doRefresh();
  } finally {
    release();
  }
}
```

Across tabs, use the Web Locks API: `navigator.locks.request("token-refresh", async () => { ... })`.

## 340: How do you implement a semaphore?

A semaphore allows up to N tasks at once and makes others wait.

```js
class Semaphore {
  #waiting = [];

  constructor(max) {
    this.available = max;
  }

  async acquire() {
    if (this.available > 0) {
      this.available--;
      return;
    }
    await new Promise((resolve) => this.#waiting.push(resolve));
  }

  release() {
    const next = this.#waiting.shift();
    if (next) next();
    else this.available++;
  }
}

const sem = new Semaphore(3);

async function limited(task) {
  await sem.acquire();
  try {
    return await task();
  } finally {
    sem.release();
  }
}
```

When releasing, the slot is passed straight to a waiting task, so `available` doesn't go up and down for nothing.

## 341: How do you make sure only one tab does a job, like polling or refreshing a token?

Use leader election with the Web Locks API. Every tab requests the same lock. Only one gets it and becomes the leader. When that tab closes, the lock is released and another tab takes over.

```js
navigator.locks.request("leader", () => {
  startPolling(); // only the leader runs this
  return new Promise(() => {}); // hold the lock while this tab is open
});
```

The leader shares results with the other tabs through `BroadcastChannel`. This combines a mutex with Pub/Sub.

## 342: How can the Actor model be used with Web Workers?

In the Actor model, each actor has private state and only communicates by messages. A Web Worker fits this: it has its own memory and talks through `postMessage`. You move heavy work (parsing, image processing, search indexes) into a worker actor and keep the main thread free. Libraries like Comlink hide the messaging behind a Proxy, so calling the worker looks like calling an async function:

```js
// worker.js
import * as Comlink from "comlink";
Comlink.expose({
  heavySum: (n) => {
    let s = 0;
    for (let i = 0; i < n; i++) s += i;
    return s;
  },
});

// main.js
const api = Comlink.wrap(
  new Worker(new URL("./worker.js", import.meta.url), { type: "module" }),
);
await api.heavySum(1e9);
```

## 343: When would you use SharedArrayBuffer and Atomics instead of message passing?

`postMessage` copies data (or transfers ownership of buffers), which is safe but adds overhead for very frequent communication. `SharedArrayBuffer` lets workers read and write the same memory, and `Atomics` gives safe operations and `wait`/`notify` for locking. It is useful for things like audio processing, emulators and WebAssembly threads. It requires cross-origin isolation (COOP and COEP headers), and it brings real data races, so most apps should stick to message passing.

## 344: What is Event Sourcing, and does it make sense in a front end?

Event sourcing stores the list of events that happened ("itemAdded", "itemRemoved") instead of only the current state. The current state is computed by replaying events through a reducer. Redux is close to this, which is why time-travel debugging works. In front ends it is useful for offline sync (send the events later), collaborative editing, audit logs and undo. The costs are growing event logs (you need snapshots), migrating old event formats, and more complex code. For a normal CRUD screen, it is overkill.

## 345: What is CQRS, and how does it relate to front-end code?

CQRS (Command Query Responsibility Segregation) means using different models for writing data (commands) and reading data (queries). On the server, writes might go to a normalized database while reads come from a denormalized view. In the front end, the idea shows up in libraries like TanStack Query (queries vs mutations) and in BFFs that return read-optimized view models. It helps when read and write needs are very different, but it adds complexity and usually eventual consistency.

## 346: How do CRDTs and Operational Transformation compare for collaborative apps?

Both let several users edit the same data at once and end up with the same result.

- **Operational Transformation (OT)** sends operations to a central server, which transforms concurrent operations against each other. Google Docs used it. It needs a server to decide order, and the transform functions are hard to get right.
- **CRDTs** (Conflict-free Replicated Data Types) are data structures designed so that changes can be merged in any order and still converge. They work peer-to-peer and offline. Yjs and Automerge are popular libraries.

For new projects, CRDT libraries are usually the easier choice.

## 347: How can micro-frontends be composed?

- **Build-time**: each micro-frontend is a package installed in a shell app. Simple, but you lose independent deploys.
- **Run-time with JavaScript**: the shell loads remote bundles at runtime (Module Federation, import maps, or `import()` from a URL) and mounts them.
- **Iframes**: strong isolation, but harder to share styles, routing and communication.
- **Web Components**: each team ships custom elements; framework-agnostic.
- **Server-side composition**: the server or edge stitches HTML fragments together.

Communication between them should go through a small contract (custom events, URL, a shared event bus) rather than shared global state.

## 348: What problems come with shared dependencies in Module Federation?

Frameworks like React must be loaded only once, because two copies cause errors (for example, hooks failing because context or the dispatcher comes from another copy). Module Federation lets you mark them as `shared` with `singleton: true` and a `requiredVersion`. Problems still appear when micro-frontends need incompatible versions, when the shared version is decided at runtime by load order, or when one team upgrades and breaks the others. Teams usually agree on a version policy and treat shared dependencies as a platform contract.

## 349: How do you isolate untrusted plugins in a web app?

Running third-party code in your page gives it full access to the DOM, cookies and user data. Options, from strongest to weakest isolation:

- A sandboxed `<iframe>` on a different origin, talking through `postMessage` with a strict message schema (Figma and VS Code web extensions use separate contexts like this).
- A Web Worker with no DOM access, given only the APIs you pass through messages.
- In-page sandboxes like SES (`lockdown()` and `Compartment`), which freeze built-ins and run code with limited globals.

The `ShadowRealm` proposal would add a built-in separate global environment, but it is not ready for production use yet.

## 350: How do hierarchical injectors work, as in Angular?

Injectors form a tree that mirrors the app (root, routes, components). When code asks for a dependency, the nearest injector that provides it answers; if none does, the request goes up to the parent. This lets you provide one instance app-wide (`providedIn: "root"`) or a separate instance per feature or per component by adding it to that level's `providers`. It is useful for things like a form state service per form. The downside is that the same token can resolve to different instances depending on where you ask, which can surprise people.

## 351: What are dependency lifetimes, and what is a captive dependency?

DI containers usually support three lifetimes:

- **Singleton**: one instance for the whole app.
- **Scoped**: one instance per scope, such as per HTTP request on the server or per component subtree.
- **Transient**: a new instance every time it is requested.

A captive dependency is when a longer-lived object holds a shorter-lived one, for example a singleton that receives a request-scoped service in its constructor. The singleton keeps the first request's instance forever, which can leak one user's data into another user's request. NestJS and .NET containers warn about or prevent this. The fix is to inject a factory or resolve the scoped dependency when needed.

## 352: How do you handle circular dependencies in a DI container?

If `A` needs `B` and `B` needs `A`, the container can't create either first. Options:

- Redesign: extract the shared part into a third service, or have one side emit events instead of calling the other.
- Inject lazily: pass a getter or factory (`() => container.resolve("A")`) and resolve only when a method runs.
- Use setter or property injection for one side after both are created.

Frameworks give tools for the second option (NestJS `forwardRef`, Angular's `inject()` inside methods), but a cycle is usually a sign the responsibilities are split badly.

## 353: How can the new decorators and Symbol.metadata support dependency injection?

The stage 3 decorators proposal comes with a companion metadata proposal. Each decorator's context gets a `metadata` object, and the class gets it as `Class[Symbol.metadata]`. A DI library can record what each class needs:

```js
function inject(token) {
  return (_value, context) => {
    (context.metadata.deps ??= {})[context.name] = token;
  };
}

class OrderService {
  @inject("http") accessor http;
  @inject("logger") accessor logger;
}

// a container reads OrderService[Symbol.metadata].deps
```

This replaces the old `reflect-metadata` approach that relied on TypeScript's `emitDecoratorMetadata`. TypeScript 5.2+ supports `Symbol.metadata`, but you may need a polyfill for `Symbol.metadata` at runtime.

## 354: What is the accessor keyword in the decorators proposal?

`accessor` declares a class field that is backed by a private storage slot and exposed through a getter and setter. Decorators can wrap that getter and setter, which is how you build observable or validated fields with the new decorator design.

```js
function observed({ get, set }, context) {
  return {
    set(value) {
      console.log(`${String(context.name)} changed to`, value);
      set.call(this, value);
    },
    get() {
      return get.call(this);
    },
  };
}

class Settings {
  @observed accessor theme = "light";
}
```

Plain field decorators can only change the initial value, not intercept later reads and writes, so `accessor` fills that gap.

## 355: How do singletons and registries interact with tree shaking?

Bundlers remove unused exports, but they keep any module code that might have side effects. A module that creates a singleton or registers itself in a global registry at load time has side effects, so the bundler can't drop it even if nothing uses it. To keep code tree-shakeable:

- Create instances lazily inside functions instead of at module top level.
- Avoid top-level registration; let the app register what it uses.
- Mark pure calls with `/* @__PURE__ */` and set `"sideEffects": false` (or a list of files) in `package.json` when it is true.

If you set `sideEffects: false` on a package that does have side effects (like a CSS import or a polyfill), the bundler will drop them and break your app.

## 356: What goes wrong with "self-registering" modules?

A common pattern is for each plugin file to call `registry.register(...)` when imported, and the app imports a folder to register everything. Problems:

- Something must import each file, or it never registers. Tree shaking or lazy loading can silently drop registrations.
- Order of imports decides registration order, which is fragile.
- Tests that import only part of the code see a partly filled registry.

Explicit registration in one place (`registry.register(pluginA, pluginB)`) is easier to follow. If you want automatic discovery, use a build-time feature like Vite's `import.meta.glob` so the list is generated, not implied.

## 357: What is the dual package hazard, and how do you avoid it?

When a package ships both CommonJS and ESM builds, an app may load both (one via `require`, one via `import`). Then there are two copies of every class and every module-level singleton, so `instanceof` fails and state is split. Fixes:

- Ship ESM only. Since Node.js 22.12 and 20.19, `require()` can load ESM modules without a flag, which makes ESM-only packages much easier to consume.
- Make one build a thin wrapper that re-exports the other.
- Keep state in a place both copies share (for example `globalThis` with a `Symbol.for` key).

## 358: How do you choose a lazy loading and preloading strategy?

Load code on demand to keep the first load small, but start loading before the user needs it so they don't wait:

- **Route-based splitting**: each page is a separate chunk.
- **Interaction-based**: load a heavy editor when the user hovers or focuses the button, before they click.
- **Viewport-based**: load a widget when it is about to scroll into view (IntersectionObserver).
- **Idle preloading**: fetch likely-next chunks in `requestIdleCallback`.
- **Hints**: `<link rel="modulepreload">` or `<link rel="prefetch">`.

Measure: too many small chunks add request overhead, and preloading everything defeats the purpose.

## 359: How can the Strategy pattern work with code splitting?

Store strategy loaders instead of strategies, and load only the one you need.

```js
const exporters = {
  pdf: () => import("./exporters/pdf.js"),
  xlsx: () => import("./exporters/xlsx.js"),
  csv: () => import("./exporters/csv.js"),
};

export async function exportReport(format, data) {
  const load = exporters[format];
  if (!load) throw new Error(`Unknown format: ${format}`);
  const { default: exporter } = await load();
  return exporter(data);
}
```

Heavy libraries like a PDF generator are only downloaded when a user exports a PDF. Bundlers can analyze these static `import()` paths and create a chunk for each.

## 360: What is the composition pattern for mixing server and client components in React?

A Client Component can't import a Server Component, because everything it imports becomes client code. But a Server Component can pass another Server Component to a Client Component as `children` or another prop. The server renders it, and the client component just places it.

```jsx
// Page.jsx (server)
import Tabs from "./Tabs"; // "use client"
import ServerStats from "./ServerStats"; // server-only data access

export default function Page() {
  return (
    <Tabs>
      <ServerStats />
    </Tabs>
  );
}
```

This keeps the interactive shell small on the client while data-heavy parts stay on the server. It is the Slot pattern applied across the server/client boundary.

## 361: What is the islands architecture?

The page is mostly static HTML rendered on the server, with small interactive "islands" that are hydrated on their own. Each island loads only its own JavaScript, and can hydrate at different times (on load, when visible, when idle). Astro is the best-known framework built around it. It works very well for content sites, because most of the page ships no JavaScript. It is harder for app-like pages where everything is interactive and shares state.

## 362: What is resumability, and how is it different from hydration?

Hydration runs the component code again in the browser to rebuild state and attach event listeners, so the browser does work the server already did. Resumability, used by Qwik, serializes the state and listener locations into the HTML, so the browser can continue where the server stopped. Code for an event handler is only downloaded when that event happens. It gives a very small startup cost, but requires a framework designed for it and a compiler that splits code into many small pieces.

## 363: How do fine-grained signals and a virtual DOM differ as architectures?

With a virtual DOM (React), a state change reruns the component function, builds a new virtual tree, compares it to the old one and patches the DOM. It is simple to reason about (UI is a function of state) but does extra work. With fine-grained signals (Solid, Svelte 5, Angular), the compiler or runtime connects each signal directly to the DOM nodes or computations that use it, so only those update. It does less work per change, but you have to follow rules about where reactivity is tracked. React's compiler narrows the gap by memoizing automatically.

## 364: What are statecharts, and what do they add to state machines?

Statecharts (from David Harel) extend finite state machines with:

- **Hierarchical (nested) states**: "editing" can contain "valid" and "invalid".
- **Parallel states**: "playback" and "volume" can each have their own state at the same time.
- **History states**: return to the last sub-state you were in.
- **Guards, actions and delayed transitions**.

These features stop the number of states from exploding in real UIs. XState implements statecharts in JavaScript and can visualize them, which helps when talking with designers and product people.

## 365: How does XState use the Actor model?

In XState v5 everything running is an actor: a machine, a promise, a callback or an observable. Actors have their own state, receive events, and can spawn child actors and send messages to them and to their parent. A form machine can spawn a validation actor for each field, and a page machine can spawn a fetch actor and stop it when the user leaves. This gives a clear model for concurrency and cleanup, because stopping a parent stops its children.

## 366: How do you make impossible states impossible?

Instead of several independent flags, model state as one value where each variant has only the fields that make sense for it. In TypeScript this is a discriminated union:

```ts
type RequestState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };
```

You can't have `data` while loading or an `error` with `success`, and the compiler forces you to handle each case. In plain JavaScript, the same idea is a single `status` field and a state machine that only allows valid transitions.

## 367: What are branded types, and how do they relate to Value Objects?

TypeScript types are structural, so a `UserId` that is just a `string` can be mixed up with an `OrderId`. A brand makes them different types without runtime cost:

```ts
type UserId = string & { readonly __brand: "UserId" };

function toUserId(raw: string): UserId {
  if (!/^u_\w+$/.test(raw)) throw new Error("Invalid user id");
  return raw as UserId;
}

function loadUser(id: UserId) {
  /* ... */
}

loadUser("u_123"); // error: plain string
loadUser(toUserId("u_123")); // ok
```

It is a lightweight Value Object: validation happens once at the boundary, and the type carries the guarantee after that.

## 368: How do you make a Builder that only allows build() when required fields are set?

In TypeScript you can track which steps were done in the builder's type parameter:

```ts
class Req<Has extends string = never> {
  private constructor(private cfg: { url?: string; method?: string }) {}

  static create() {
    return new Req({});
  }
  url(u: string): Req<Has | "url"> {
    return new Req({ ...this.cfg, url: u });
  }
  method(m: string): Req<Has | "method"> {
    return new Req({ ...this.cfg, method: m });
  }
  build(this: Req<"url" | "method">) {
    return this.cfg as { url: string; method: string };
  }
}

Req.create().url("/a").method("GET").build(); // ok
Req.create().url("/a").build(); // compile error
```

It moves "missing field" errors from runtime to compile time. It is clever, so use it for widely used APIs where the safety pays off.

## 369: Why does JavaScript not need double dispatch for the Visitor pattern?

In Java, method overloading is resolved at compile time, so the classic Visitor uses double dispatch: each node calls `visitor.visitX(this)` to get the right method. In JavaScript you can just look up the handler by the node's type at runtime: `visitor[node.type](node)`. That's why Babel and ESLint visitors are plain objects keyed by node type names. The downside is that nothing checks you handled every node type, unless you add TypeScript with exhaustiveness checks.

## 370: Why is eval or new Function a bad way to implement an Interpreter for user input?

`eval` and `new Function` run the input as full JavaScript with access to globals, cookies, the DOM and network. Any user-provided formula then becomes an XSS or code-injection hole. They are also blocked by a strict Content Security Policy without `'unsafe-eval'`. Write a small parser for a limited grammar that produces a tree, and evaluate only the operations you allow. Libraries like `expr-eval` or `jsep` do this. You also get better error messages and can limit running time.

## 371: What is the fragile base class problem?

When subclasses depend on how a base class works internally, a change in the base class can break subclasses even if the public API didn't change. For example, a base class `addAll()` that starts calling `add()` internally will make a subclass that counts items in both methods count twice. Template Method and deep inheritance hierarchies are prone to this. Prefer composition, keep base classes small, and document which methods are meant to be overridden.

## 372: How can overriding a sync method with an async one break Liskov substitution?

If the base class has `getName()` returning a string and a subclass overrides it with `async getName()`, callers that do `user.getName().toUpperCase()` break, because they now get a promise. Errors also change from thrown exceptions to rejected promises, and ordering changes. In JavaScript nothing stops you from doing this, so it shows up in mocks and adapters too. Keep the same sync or async contract in all implementations; if one implementation needs to be async, make the interface async for all of them.

## 373: How should errors be translated between layers?

Each layer should throw errors that make sense at its level. The API client turns HTTP responses into `HttpError` with status. The repository turns a 404 into `NotFoundError("User")`. The UI maps domain errors to messages. Keep the original error as `cause` so you don't lose debugging info.

```js
try {
  return await http.get(`/users/${id}`);
} catch (err) {
  if (err instanceof HttpError && err.status === 404) {
    throw new UserNotFoundError(id, { cause: err });
  }
  throw err;
}
```

This stops HTTP details from leaking into components and lets you change the transport later.

## 374: How do you set up global error handling in a browser app?

Combine local handling with global safety nets:

- `window.addEventListener("error", ...)` for uncaught errors and failed resource loads.
- `window.addEventListener("unhandledrejection", ...)` for promises nobody handled.
- Framework boundaries: React error boundaries, Angular `ErrorHandler`, Vue `app.config.errorHandler`.
- A single `reportError`-style function that sends errors to your monitoring service with context (user, route, release).

Global handlers should report and maybe show a generic message. They are not a replacement for handling expected errors where they happen.

## 375: What details do wrapper functions (decorators) often get wrong?

- **`this`**: use a regular function and `fn.apply(this, args)`, not an arrow that loses the caller's `this`.
- **Async**: if the wrapped function returns a promise, logging "done" right after the call is wrong; await it or chain on it.
- **Errors**: rethrow after logging, don't swallow them.
- **Return values**: return what the original returned.
- **Metadata**: `name` and `length` change, which affects debugging and code that checks `fn.length` (like curry helpers).

```js
function timed(fn) {
  const wrapper = async function (...args) {
    const start = performance.now();
    try {
      return await fn.apply(this, args);
    } finally {
      console.log(`${fn.name} took ${performance.now() - start}ms`);
    }
  };
  Object.defineProperty(wrapper, "name", { value: `timed(${fn.name})` });
  return wrapper;
}
```

## 376: What are the common pitfalls of memoization in production code?

- **Unbounded growth**: a `Map` cache keyed by user input grows forever. Use LRU, TTL or `WeakMap`.
- **Stale data**: cached results don't know the underlying data changed. You need invalidation.
- **Impure functions**: memoizing something that reads time, random values or global state returns wrong results.
- **Mutated inputs**: if an object key is mutated, the cached result no longer matches it.
- **Cost of the key**: hashing big arguments can cost more than the computation.
- **Cached errors**: caching rejected promises makes temporary errors permanent.

Measure first; many functions are faster to recompute than to cache.

## 377: What client-side cache invalidation strategies are there?

- **Time-based (TTL)**: data expires after N seconds. Simple, but may show stale data or refetch too often.
- **Key-based**: after a mutation, invalidate the queries with matching keys (`queryClient.invalidateQueries({ queryKey: ["todos"] })`).
- **Tag-based**: queries provide tags and mutations invalidate tags (RTK Query's `providesTags` / `invalidatesTags`).
- **Write-through**: the mutation response updates the cache directly, no refetch.
- **Server push**: the server tells clients what changed over WebSocket or SSE.

Most apps combine a short TTL with key or tag invalidation after their own mutations.

## 378: How does a normalized client cache work, as in Apollo Client?

The cache splits query results into entities keyed by type and id (`User:42`) and stores each once. Query results become references to those entities. When any query or mutation returns `User:42` with new fields, every query that references it sees the update without refetching. It is the Identity Map pattern: one object per identity. The cost is complexity: you need stable ids, custom merge logic for lists and pagination, and you must handle objects without ids. Document caches (like TanStack Query) are simpler and rely on invalidation instead.

## 379: How do you handle optimistic updates when several mutations overlap?

If a user clicks "like" then "unlike" quickly, and the first request fails after the second succeeded, a naive rollback restores an old state and overwrites the newer change. Approaches:

- Cancel in-flight refetches for that data before applying the optimistic update, so they don't overwrite it.
- Roll back by reapplying the confirmed server state plus remaining pending mutations, not by restoring a snapshot.
- Serialize mutations to the same entity with a queue.
- After all mutations settle, refetch to get the true server state.

TanStack Query's `onMutate` / `onError` / `onSettled` and `useOptimistic` in React are built around these steps.

## 380: How does the outbox pattern support offline-first apps?

User actions are written to a local outbox (usually IndexedDB) first, and the UI updates from local data right away. A sync process sends outbox items to the server in order when the network is available, removes them on success, and retries on failure. Each item carries an idempotency key so retries are safe. Conflicts (the server data changed meanwhile) need a rule: last write wins, merge per field, or ask the user. It is the Command pattern plus a durable queue.

## 381: What caching strategies can a service worker use?

- **Cache first**: serve from cache, fall back to network. Good for versioned static assets.
- **Network first**: try the network, fall back to cache when offline. Good for HTML and API data that should be fresh.
- **Stale-while-revalidate**: serve from cache and update the cache in the background. Good for avatars, non-critical data.
- **Network only / cache only**: for things that must be live, or for precached app shell files.

```js
self.addEventListener("fetch", (event) => {
  if (event.request.destination !== "image") return;
  event.respondWith(
    caches.open("images").then(async (cache) => {
      const cached = await cache.match(event.request);
      const network = fetch(event.request).then((res) => {
        cache.put(event.request, res.clone());
        return res;
      });
      return cached ?? network;
    }),
  );
});
```

The service worker is a Proxy between the page and the network. Workbox packages these strategies.

## 382: What is Background Sync, and what are its limits?

The Background Sync API lets a service worker retry a task (like sending queued messages) when connectivity comes back, even if the user closed the tab. You register a tag with `registration.sync.register("outbox")` and handle the `sync` event in the service worker. It is supported in Chromium-based browsers but not in Firefox or Safari, so you still need a fallback that syncs when the app is open (on `online` events or on startup). Design the outbox so either path can process it.

## 383: How can a deep merge or "extend" utility cause prototype pollution?

A naive recursive merge copies keys from user input into an object. If the input contains `__proto__`, the merge writes into `Object.prototype`, and every object in the app gets the new property.

```js
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
naiveMerge({}, payload);
({}).isAdmin; // true, for every object
```

Fixes: skip `__proto__`, `constructor` and `prototype` keys, use `Object.create(null)` or `Map` for dictionaries, validate input with a schema, prefer `structuredClone` for copying data, and keep libraries like lodash up to date. Config objects and options patterns that merge user input are the usual place this happens.

## 384: Why is it risky to read properties from untrusted objects more than once?

A getter or Proxy can return different values each time. If you check a value and then use it later, an attacker can return a safe value for the check and a dangerous one for the use (a time-of-check to time-of-use bug).

```js
function safeOpen(options) {
  if (!options.url.startsWith("https://")) throw new Error("Unsafe");
  window.open(options.url); // reads url again, may now be "javascript:..."
}
```

Copy values into local variables once, validate the copy, and use the copy. This matters for libraries and plugin APIs that receive objects from code you don't control.

## 385: What does "hardened JavaScript" (SES lockdown) do?

SES (Secure ECMAScript) is a library and a set of TC39 ideas. `lockdown()` freezes all built-in objects and prototypes, so no code can change `Array.prototype` or `Object.prototype` after that. `harden(obj)` deep-freezes an object you want to share. `Compartment` runs code with its own globals and only the capabilities you pass in. MetaMask Snaps and Agoric use it. It enforces the "don't modify built-ins" rule and makes the Module and Facade patterns real security boundaries instead of just conventions.

## 386: How do Trusted Types relate to the Factory pattern?

Trusted Types is a browser feature (enabled by a CSP header) that blocks passing plain strings to dangerous sinks like `innerHTML`, `outerHTML` and `script.src`. Only objects created by a policy are accepted. The policy is a factory that is the single place where sanitizing happens:

```js
const policy = trustedTypes.createPolicy("app", {
  createHTML: (input) => DOMPurify.sanitize(input),
});

element.innerHTML = policy.createHTML(userContent);
element.innerHTML = userContent; // blocked by the browser
```

Security reviews only need to check the policies, not every `innerHTML` in the codebase. Check browser support for your targets; Chromium supports it and other browsers have been adding it.

## 387: Why should a dynamic factory or loader never use raw user input as a module path?

Code like ``import(`./plugins/${name}.js`)`` with `name` from the URL lets users load files you didn't intend, and with absolute URLs it could load code from another server. Always map input to an allowlist:

```js
const plugins = {
  chart: () => import("./plugins/chart.js"),
  map: () => import("./plugins/map.js"),
};

const load = plugins[new URLSearchParams(location.search).get("plugin")];
if (load) await load();
```

The same rule applies to factories that pick a class or function by name from user input: use a fixed map, and check with `Object.hasOwn` so names like `constructor` don't match inherited properties.

## 388: How do you keep an event bus manageable in a large app?

- **Name events clearly** with a namespace (`cart:itemAdded`) and keep a central list of event names and payload shapes.
- **Type the events** (TypeScript map of event name to payload) so typos and wrong payloads fail at build time.
- **Limit who can emit** certain events, for example by exporting typed emit functions instead of the raw bus.
- **Add tooling**: a debug mode that logs every event with its source.
- **Clean up** listeners tied to components or routes.
- **Don't use it for state**: if many parts need the current value, a store is a better fit than events.

## 389: What should you think about when designing the API of a reusable JavaScript library?

- A small public surface: export only what users need. Everything exported is a promise you must keep.
- Options objects for configuration, with safe defaults.
- Consistent naming and consistent sync/async behavior.
- No global side effects on import, so it tree-shakes well.
- Clear errors with actionable messages.
- Ways to extend (plugins, hooks, adapters) instead of making users fork it.
- Types (TypeScript or JSDoc) shipped with the package.
- A versioning and deprecation policy that follows semver.

## 390: How do you change a library's API without breaking users?

Use Adapter and deprecation in steps:

1. Add the new API next to the old one.
2. Make the old API a thin adapter that calls the new one, and log a deprecation warning once (only in development).
3. Provide a codemod if the change is mechanical.
4. Remove the old API in the next major version.

```js
let warned = false;
export function fetchUser(id, cb) {
  if (!warned && process.env.NODE_ENV !== "production") {
    console.warn(
      "fetchUser(id, cb) is deprecated. Use getUser(id) which returns a promise.",
    );
    warned = true;
  }
  getUser(id).then((u) => cb(null, u), cb);
}
```

## 391: What are contract tests, and why are they useful for adapters?

A contract test is a shared test suite that every implementation of an interface must pass. If you have an `InMemoryStorage` for tests and an `IndexedDbStorage` for production, run the same suite against both. This makes sure your fake really behaves like the real thing, so tests using the fake can be trusted.

```js
export function storageContract(createStorage) {
  test("returns what was saved", async () => {
    const s = await createStorage();
    await s.set("a", 1);
    expect(await s.get("a")).toBe(1);
  });

  test("returns undefined for missing keys", async () => {
    const s = await createStorage();
    expect(await s.get("missing")).toBeUndefined();
  });
}

storageContract(() => new InMemoryStorage());
storageContract(() => new IndexedDbStorage("test-db"));
```

## 392: What is hexagonal architecture (ports and adapters)?

The core of the app (business logic) sits in the middle and talks to the outside world only through ports, which are interfaces the core defines (`OrderRepository`, `PaymentGateway`, `Notifier`). Adapters implement those ports for real technologies (REST, IndexedDB, Stripe) or for tests. The core never imports framework or infrastructure code. In front-end apps it helps keep business rules testable and lets you swap APIs or run the same logic in a browser, a worker and a Node script.

## 393: What is a use case (interactor) in clean architecture, and how does it look in JavaScript?

A use case is one application action, like "place order", written as a function or class that coordinates domain objects and ports. It doesn't know about React or HTTP.

```js
export function makePlaceOrder({ orders, payments, clock }) {
  return async function placeOrder(cart, paymentInfo) {
    if (cart.items.length === 0) throw new EmptyCartError();
    const payment = await payments.charge(cart.total, paymentInfo);
    return orders.save({
      items: cart.items,
      paymentId: payment.id,
      placedAt: clock.now(),
    });
  };
}
```

The UI calls `placeOrder`, and tests pass in fakes. For small apps this is too much ceremony; it pays off when business rules are complex or shared across several UIs.

## 394: How can Domain-Driven Design ideas help a front-end codebase?

You don't need the full DDD toolbox, but some ideas help:

- **Ubiquitous language**: name code with the same words the business uses (`Invoice`, `Settle`), not generic names (`Item`, `process`).
- **Bounded contexts**: "Customer" in billing and "Customer" in support can be different models; don't force one shared model across features.
- **Value objects**: `Money`, `DateRange` with validation and behavior.
- **Anti-corruption layers** at the API boundary.

Feature folders often line up with bounded contexts, which keeps teams from stepping on each other.

## 395: What is an anemic domain model?

It is a model where objects only hold data (getters and setters) and all logic lives in separate service functions. It is common in JavaScript, where data is usually plain JSON. It isn't always wrong: plain data is easy to serialize, store in state libraries and send over the network. But if the same rules (like "an order can't be cancelled after shipping") are repeated in several services and components, it is better to put them in one place: domain functions like `canCancel(order)` or methods on a class.

## 396: What is Feature-Sliced Design?

Feature-Sliced Design is a methodology for organizing front-end code into layers (from top to bottom: `app`, `pages`, `widgets`, `features`, `entities`, `shared`) and slices inside layers (by business area). Each slice has segments like `ui`, `model`, `api` and a public `index`. A module may only import from layers below it, and slices on the same layer don't import each other. It combines the Layered architecture with the Module pattern and gives a standard structure for large teams. ESLint plugins (like Steiger) can enforce the rules.

## 397: How do you enforce module boundaries in a monorepo?

- Make each package declare its public API with the `exports` field in `package.json`, so deep imports fail.
- Declare dependencies between packages explicitly, so a package can only import what it lists.
- Use tags and lint rules (Nx `enforce-module-boundaries`, `eslint-plugin-boundaries`, dependency-cruiser) to block imports like "ui package must not import data-access package".
- Run these checks in CI.

Without enforcement, boundaries drawn in a diagram erode quickly.

## 398: How does AsyncLocalStorage help with request context in Node.js?

`AsyncLocalStorage` from `node:async_hooks` keeps a value available through all async calls started within a function, without passing it as a parameter. It is used for request ids, the current user, and transactions.

```js
import { AsyncLocalStorage } from "node:async_hooks";

export const requestContext = new AsyncLocalStorage();

app.use((req, res, next) => {
  requestContext.run({ requestId: crypto.randomUUID() }, next);
});

export function log(msg) {
  const ctx = requestContext.getStore();
  console.log(`[${ctx?.requestId}] ${msg}`);
}
```

It is a scoped version of a singleton: global access, but a separate value per request. Overusing it hides dependencies, so keep it for cross-cutting data like logging and tracing.

## 399: What is the AsyncContext proposal?

AsyncContext is a TC39 proposal to bring something like `AsyncLocalStorage` into the language, so it works in browsers too. It provides `AsyncContext.Variable` (a value that follows async flow) and `AsyncContext.Snapshot` (capture and restore all current values). It would help front-end tracing, framework context for async code, and scheduling libraries. It is still a proposal, so check its stage before using a polyfill in production.

## 400: How do generators relate to async/await?

Before async/await, libraries like `co` used generators as coroutines: the generator `yield`s a promise, a runner waits for it and resumes the generator with the result. async/await is basically this pattern built into the language.

```js
function run(genFn) {
  return new Promise((resolve, reject) => {
    const gen = genFn();
    function step(method, arg) {
      let result;
      try {
        result = gen[method](arg);
      } catch (err) {
        return reject(err);
      }
      if (result.done) return resolve(result.value);
      Promise.resolve(result.value).then(
        (v) => step("next", v),
        (e) => step("throw", e),
      );
    }
    step("next");
  });
}

run(function* () {
  const user = yield fetch("/api/user").then((r) => r.json());
  return user.name;
});
```

redux-saga still uses generators this way, because a generator can yield plain objects describing effects, which makes testing easy.

## 401: What is trampolining?

JavaScript engines (except Safari) don't do tail call optimization, so deep recursion throws `RangeError: Maximum call stack size exceeded`. A trampoline runs a recursive algorithm in a loop: the function returns a thunk for the next step instead of calling itself, and the trampoline keeps calling thunks until it gets a value.

```js
const trampoline =
  (fn) =>
  (...args) => {
    let result = fn(...args);
    while (typeof result === "function") result = result();
    return result;
  };

const sumTo = trampoline(function go(n, acc = 0) {
  return n === 0 ? acc : () => go(n - 1, acc + n);
});

sumTo(1_000_000); // works, no stack overflow
```

In practice, rewriting the recursion as a loop with an explicit stack is often simpler.

## 402: What is continuation-passing style (CPS)?

In CPS a function doesn't return its result; it passes the result to a "continuation" function it received. Node-style callbacks are CPS. It makes control flow explicit, which compilers and some async libraries use, but written by hand it leads to deep nesting (callback hell). Promises and async/await give you the same power with normal-looking code. Knowing CPS helps you understand how async code works under the hood and why callbacks compose poorly.

## 403: Are Promises monads, and what is a Maybe?

A monad is roughly a wrapper type with a way to put a value in (`of`) and a way to chain functions that return wrapped values (`flatMap` / `chain`). Promises are close: `Promise.resolve` wraps, `.then` chains and flattens. They are not strict monads, because `.then` always flattens nested promises and treats any thenable specially. A `Maybe` wraps a value that might be missing, so you can chain without null checks:

```js
const Maybe = (value) => ({
  map: (fn) => (value == null ? Maybe(null) : Maybe(fn(value))),
  getOrElse: (fallback) => (value == null ? fallback : value),
});

Maybe(user)
  .map((u) => u.address)
  .map((a) => a.city)
  .getOrElse("Unknown");
```

Optional chaining (`user?.address?.city ?? "Unknown"`) covers most of this in modern JavaScript.

## 404: What is railway-oriented programming?

Each step returns either a success or a failure (a Result). Steps are chained so that once a failure happens, the rest are skipped and the failure goes straight to the end, like a train switching to a second track.

```js
const ok = (value) => ({ ok: true, value });
const err = (error) => ({ ok: false, error });
const chain = (result, fn) => (result.ok ? fn(result.value) : result);

const parse = (s) => (s ? ok(JSON.parse(s)) : err("empty"));
const validate = (o) => (o.email ? ok(o) : err("missing email"));

const result = [validate].reduce(chain, parse(input));
```

It makes error paths explicit without `try/catch` everywhere. In JavaScript it fits best in validation and data-processing code; for most async app code, exceptions with clear error types are more natural.

## 405: What is a lens?

A lens is a pair of functions, a getter and an immutable setter, focused on one part of a nested structure. Lenses compose, so you can build a lens for `user.address.city` and use it to read or update immutably.

```js
const lens = (get, set) => ({ get, set });
const prop = (k) =>
  lens(
    (o) => o[k],
    (v, o) => ({ ...o, [k]: v }),
  );
const compose = (a, b) =>
  lens(
    (o) => b.get(a.get(o)),
    (v, o) => a.set(b.set(v, a.get(o)), o),
  );

const city = compose(prop("address"), prop("city"));
city.get(user);
const moved = city.set("Paris", user);
```

Immer made lenses less common in app code, but they still show up in functional libraries like Ramda and optics libraries.

## 406: What are transducers?

A transducer is a composable transformation (map, filter, take) that is independent of the data source and doesn't create intermediate arrays. `arr.map(f).filter(g)` creates a temporary array after `map`. A transducer combines `f` and `g` into one reducing step and runs it in a single pass. They are useful for very large collections or streams. In modern JavaScript, iterator helpers and generator pipelines give similar single-pass laziness with a simpler API, so transducers are rarely needed in app code.

## 407: How does Shadow DOM affect event delegation?

When an event crosses a shadow root, it is retargeted: listeners outside see `event.target` as the host element, not the inner element. So a delegated listener on `document` can't see which button inside a component was clicked. Options:

- Use `event.composedPath()` to see the full path (for open shadow roots).
- Have the component dispatch its own meaningful custom event with `composed: true` and `bubbles: true`.

```js
this.dispatchEvent(
  new CustomEvent("item-select", {
    detail: { id },
    bubbles: true,
    composed: true,
  }),
);
```

The second option is better design: the component exposes an event API instead of its internals. Also, some events (like `focus`) don't bubble, and custom events don't cross shadow boundaries unless `composed` is true.

## 408: What are scoped custom element registries, and why do they matter?

The global `customElements` registry allows each tag name once per page. If two micro-frontends ship different versions of `<ui-button>`, the second `define` throws. Scoped custom element registries let you create a `new CustomElementRegistry()` and attach it to a shadow root, so each part of the page can define its own elements. It fixes a real limit of the Registry pattern on the platform. Browser support has been rolling out recently, so check your targets; a polyfill exists.

## 409: What are form-associated custom elements?

By setting `static formAssociated = true` and calling `this.attachInternals()`, a custom element can take part in forms like a native input: it has a form value, validity, labels and reset behavior.

```js
class RatingInput extends HTMLElement {
  static formAssociated = true;
  #internals = this.attachInternals();

  set value(v) {
    this.#internals.setFormValue(String(v));
    this.#internals.setValidity(
      v ? {} : { valueMissing: true },
      "Pick a rating",
    );
  }
}

customElements.define("rating-input", RatingInput);
```

It is a good example of composition with platform APIs: you get form behavior from `ElementInternals` instead of extending `HTMLInputElement` (which customized built-ins don't support in Safari).

## 410: What are the trade-offs of Proxy-based RPC clients like tRPC?

The client is a Proxy, so `api.user.byId.query(1)` builds the path from the property chain and sends a request. With TypeScript, types flow from the server router, so you get end-to-end type safety without code generation. Trade-offs:

- Tight coupling between client and server code, best for monorepos with one team.
- The network call looks like a function call, which can hide latency and failure modes.
- Not a public API format; other clients need REST or OpenAPI anyway.
- Debugging goes through Proxy magic.

It is the Proxy pattern used as a remote proxy.

## 411: Design an undo/redo system for a drawing app.

- Model every user change as a command object: `{ type: "moveShape", id, from, to }` with `apply` and `invert` functions, or as Immer patches with inverse patches.
- Keep `undo` and `redo` stacks. New commands clear the redo stack.
- Group continuous actions (dragging) into one command by merging commands with the same target within a short time, or by committing on pointer up.
- Keep selection and viewport changes out of history, or handle them separately.
- Limit history size, or store periodic snapshots plus commands to save memory.
- For collaboration, undo should only revert the local user's operations, which means transforming them against remote changes (OT) or using a CRDT library's undo manager (Yjs has one).

## 412: Design an in-app notification system.

- **Source**: notifications come from the server via WebSocket or SSE, plus local ones from the app.
- **Store**: a normalized store (`byId`, `order`, `unreadCount`) that components subscribe to with selectors.
- **API**: a small facade like `notify.success(msg)`, `notify.error(msg, { action })` used by the whole app.
- **Display strategies**: toasts, a bell list, browser notifications. Each is a separate subscriber, so you can add one without changing producers.
- **Rules**: deduplicate by id, group similar items, rate-limit noisy sources, respect user preferences.
- **Cross-tab**: use `BroadcastChannel` so marking as read in one tab updates the others.

The core pattern is Pub/Sub with a store in the middle.

## 413: Design a small form library. Which patterns would you use?

- **Observer/store**: form state (values, errors, touched, submitting) in one store; fields subscribe only to their own slice to avoid re-rendering the whole form.
- **Strategy**: validators as functions or a schema adapter (Zod, Valibot) behind one interface.
- **Chain of Responsibility**: run field validators in order and stop at the first error, or collect all.
- **Registry**: fields register on mount and unregister on unmount.
- **Prop getters**: `register("email")` returns `{ name, value, onChange, onBlur, ref }`.
- **Command / async**: submit handling with cancellation of stale async validation.
- **Controlled and uncontrolled** support, since uncontrolled inputs are faster for large forms.

React Hook Form and TanStack Form are good references for these choices.

## 414: Design a data-fetching cache library like TanStack Query.

- **Cache keyed by query key** (serialized array) holding data, error, status and timestamps.
- **Observer**: each `useQuery` is an observer of a cache entry; many components share one entry.
- **Request deduplication**: one in-flight promise per key.
- **Stale-while-revalidate** with `staleTime` and background refetch on window focus or reconnect.
- **Garbage collection**: remove entries with no observers after a timeout.
- **Mutations** with optimistic updates and invalidation by key prefix.
- **Retry with backoff** and cancellation via `AbortSignal`.
- **Framework adapters**: a framework-agnostic core with thin adapters for React, Vue, Solid (Adapter pattern).

## 415: Design the plugin architecture for a rich text editor.

- The core holds the document model and a transaction system (every change is a transaction, which gives undo, collaboration and plugin hooks).
- Plugins register: schema extensions (new node types), commands, keyboard shortcuts, input rules, toolbar items and view decorations.
- Commands are the only way to change the document, so features are testable without the DOM.
- Plugins can filter or append to transactions (Chain of Responsibility).
- Plugin state is stored per plugin key, isolated from others.
- Dependencies between plugins are declared, and the core orders them.

ProseMirror, Tiptap and Lexical all follow versions of this design.

## 416: Design an analytics layer that supports several providers.

- **Facade**: the app calls `analytics.track(event, props)` and `analytics.identify(user)` only.
- **Adapter per provider** (Google Analytics, PostHog, Segment), each mapping events to the provider's format.
- **Typed event catalog**: event names and payloads defined in one place.
- **Queue**: buffer events until consent is given and providers have loaded, then flush.
- **Consent strategy**: each adapter declares which consent category it needs.
- **Middleware**: enrich events (page, session, app version), drop PII, sample noisy events.
- **Failure isolation**: a crashing provider must never break the app, so wrap each adapter call in `try/catch`.

## 417: How would you implement A/B experiments on top of feature flags?

- A flag evaluator returns a variant (`"control"`, `"B"`) based on a stable hash of the user id and the experiment key, so the same user always gets the same variant.
- Evaluate on the server when possible to avoid flicker, and pass the result to the client.
- Use the Strategy pattern at the UI boundary: `variants[variant]` picks the component.
- Track an exposure event the first time the user actually sees the variant, not on every evaluation.
- Keep experiment code isolated in one module, and remove the losing branch quickly after the experiment ends.

## 418: Design a real-time collaborative to-do list.

- **Data model**: use a CRDT (for example a Yjs array of maps) so concurrent inserts, edits and reorders merge without conflicts.
- **Transport**: WebSocket provider for live sync plus IndexedDB persistence for offline.
- **Presence**: who is online and what they are editing, sent as ephemeral state (not stored in the document).
- **UI binding**: an observer on the shared document that updates a local store, which components read with selectors.
- **Undo**: per-user undo manager that only reverts that user's changes.
- **Server**: relays updates, stores snapshots, checks permissions on each update.

If you don't need offline or peer-to-peer editing, a simpler server-authoritative design with optimistic updates and server events also works.

## 419: Design a modal manager for an app with nested dialogs.

- Keep a **stack** of open modals in a store; the top one is active.
- Open modals through a **facade** (`modals.open(ConfirmDialog, props)`) that returns a promise resolving with the user's choice. That makes "await confirm" flows easy.
- Render all modals in one **portal** container, ordered by stack position.
- Handle focus: trap focus in the top modal and restore it to the trigger when closed.
- `Escape` closes only the top modal.
- Lock body scroll while the stack isn't empty.
- Consider the native `<dialog>` element with `showModal()`, which gives a top layer and an inert background for free.

## 420: Design a toast queue.

- A **producer API** (`toast.show(message, { type, duration })`) that any code can call, even outside components.
- A **queue** with a max number visible at once; extra toasts wait.
- **Deduplication**: the same message within a short time updates a counter instead of stacking.
- **Timers** that pause on hover and when the tab is hidden.
- **Priority**: errors can jump ahead of info messages.
- **Accessibility**: an `aria-live` region so screen readers announce toasts.
- **Observer**: the toast container subscribes to the queue store.

It is Producer/Consumer plus Observer, with a small state machine per toast (entering, visible, leaving).

## 421: How would you build a minimal client-side router?

- Listen to navigation: the Navigation API (`navigation.addEventListener("navigate", ...)`) where supported, otherwise intercept link clicks and use `history.pushState` plus `popstate`.
- Match the URL against a route table (`URLPattern` can parse patterns like `/users/:id`).
- Load the route's component lazily with `import()` (Strategy + code splitting).
- Notify subscribers of route changes (Observer) so the UI re-renders.
- Run guards and loaders before showing a route (Chain of Responsibility).
- Restore scroll position and manage focus after navigation for accessibility.

```js
const routes = [
  {
    pattern: new URLPattern({ pathname: "/users/:id" }),
    load: () => import("./user.js"),
  },
];

async function resolve(url) {
  for (const r of routes) {
    const match = r.pattern.exec(url);
    if (match) return { module: await r.load(), params: match.pathname.groups };
  }
}
```

Check support for `URLPattern` and the Navigation API in your target browsers; both are newer APIs.

## 422: Design an internationalization (i18n) system.

- **Message catalogs** per locale and per feature, loaded lazily with `import()` so users only download their language.
- **Fallback chain**: `de-AT` → `de` → `en` (Chain of Responsibility).
- **Formatting** with the built-in `Intl` APIs (`Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.PluralRules`, `Intl.RelativeTimeFormat`), with formatter instances cached because they are expensive to create.
- **ICU message format** for plurals and gender, not string concatenation.
- **Facade**: `t("cart.items", { count })` used everywhere.
- **Observer**: components re-render when the locale changes.
- **Server rendering**: decide the locale on the server and send only that catalog.

## 423: Design a permissions system for a front end.

- Represent permissions as **policies** (Specification pattern): `can(user, "edit", document)` evaluates rules like "owner or admin, and document not locked".
- Keep all rules in one module shared by UI checks and, if possible, by the server (the server must enforce them anyway).
- Components ask `can(...)` instead of checking roles directly, so role changes don't spread through the code.
- Provide helpers: `<Can action="edit" subject={doc}>` or a `useCan` hook.
- Load the user's permissions once and update them through the store when they change.

Libraries like CASL implement this. Remember that hiding a button is UX, not security.

## 424: Design a multi-step checkout wizard.

- Model steps as a **state machine**: `shipping → payment → review → done`, with guards (can't go to payment without a valid address) and allowed back transitions.
- Keep form data for all steps in one store, so going back doesn't lose input, and persist it to `sessionStorage` to survive reloads.
- Each step is a component that receives its slice of data and reports changes (Mediator: the wizard coordinates steps).
- Sync the current step with the URL so the back button works.
- Validate per step on "Next", and run full validation before submit.
- Submit with an idempotency key so a double click doesn't create two orders.

## 425: Design an autocomplete component.

- **Debounce** input (around 200-300 ms) before searching.
- **Cancel** stale requests with `AbortController`, or ignore out-of-order responses.
- **Cache** results per query (LRU) so backspacing is instant.
- **State machine**: idle, loading, results, empty, error.
- **Headless logic** in a hook (`useCombobox`) with prop getters, so styling is up to the caller.
- **Keyboard and accessibility**: follow the ARIA combobox pattern, with arrow keys, `Enter`, `Escape` and `aria-activedescendant`.
- **Minimum query length** and rate limiting to protect the API.

## 426: Design infinite scroll for a feed.

- Use **cursor-based pagination** from the API (not page numbers, which shift when new items arrive).
- Trigger loading with an **IntersectionObserver** on a sentinel element near the bottom.
- Guard against duplicate loads with a state machine (`idle`, `loading`, `error`, `end`).
- **Deduplicate** items by id when pages overlap.
- **Virtualize** the list once it grows large.
- Restore scroll position when the user comes back from a detail page (keep the cache and the scroll offset).
- Offer a "Load more" button as a fallback and for keyboard users, and keep the footer reachable.

## 427: Design a drag-and-drop system for a kanban board.

- A **Mediator** (drag manager) owns the drag state: what is being dragged, the pointer position and the current drop target. Draggables and drop zones register with it.
- Use **Pointer Events** with pointer capture so mouse, touch and pen work the same way.
- **Strategies** for collision detection (closest center, pointer within) and for sorting.
- Apply the change as a **command** on drop, with optimistic update and rollback if the API fails.
- **Accessibility**: keyboard dragging (space to pick up, arrows to move) and live-region announcements.
- Use `transform` for movement and `requestAnimationFrame` for smooth updates.

dnd-kit is a good example of this architecture.

## 428: Design a theming system for a component library.

- Define **design tokens** (colors, spacing, radii) as data, and output them as CSS custom properties.
- Components only use tokens (`var(--color-primary)`), never raw values.
- Themes are sets of token values (Abstract Factory idea: a theme produces a matching family of values), switched by a class or `data-theme` attribute on a root element.
- Support light and dark with `prefers-color-scheme` and a user override.
- Allow nested themes by setting variables on subtrees.
- Keep the theme out of JavaScript state when possible, so switching doesn't re-render the app; CSS variables update the page by themselves.

## 429: Design a JavaScript SDK that third-party websites embed.

- **Tiny loader snippet** that creates a stub and loads the real script async, so it never blocks the host page.
- **Command queue stub**: calls made before the SDK loads are queued and replayed later (see the next question).
- **Namespace**: one global (`window.Acme`) and nothing else; no changes to built-ins.
- **Isolation**: render UI in an iframe or Shadow DOM so host CSS doesn't break it and yours doesn't leak.
- **Defensive code**: don't trust host-page globals (they may be patched), catch all errors, and never throw into the host page.
- **Versioning**: a stable public API, with the loader picking the version.
- **Privacy and size**: small bundle, consent-aware, no third-party cookies dependence.

## 430: What is the command queue stub pattern used by analytics snippets?

Before the real library loads, the page defines a tiny stub that just records calls in an array. When the library loads, it processes the recorded calls and replaces the stub with the real implementation. Google's `dataLayer` and `gtag` work this way.

```js
// inline snippet, runs immediately
window.acme =
  window.acme ||
  function (...args) {
    (window.acme.q = window.acme.q || []).push(args);
  };
acme("init", { key: "abc" });
acme("track", "page_view");

// inside the real SDK, once loaded
const commands = { init: setup, track: sendEvent };
const queued = window.acme.q || [];
window.acme = (cmd, ...args) => commands[cmd](...args);
queued.forEach(([cmd, ...args]) => commands[cmd](...args));
```

It is the Command pattern plus lazy loading: the page never has to wait for the SDK.

## 431: How would you migrate a large app from a global event bus to a store?

1. **Inventory** events: who emits each one, who listens, and what data they carry. Add logging to the bus to find runtime usage.
2. **Classify**: events that really represent state ("userChanged", "cartUpdated") move to the store; real one-off events ("toastRequested") can stay as events.
3. **Bridge**: make the store emit the old bus events when state changes (Adapter), so old listeners keep working.
4. **Migrate listeners** feature by feature to store selectors.
5. **Migrate emitters** to store actions, and have the bus forward old events to actions until all emitters are moved.
6. **Remove** the bridge and the old events once usage reaches zero.

Small steps, each shippable, is the Strangler Fig pattern applied inside the app.

## 432: How would you move a jQuery app to a modern framework without a rewrite?

- Use the **Strangler Fig** approach: new features and rewritten pages use the new framework; old pages keep working.
- Mount new components into existing pages (`createRoot(el).render(...)`), or wrap them as **Web Components** so old code can use them as tags.
- Build **adapters** for shared things: auth, API client, global state, events, so both worlds use the same source of truth.
- Route-level switching: let the server or a shell decide per route which app renders.
- Share styles through CSS variables or a design-token package.
- Delete old code as soon as a page is fully moved, and track progress with a simple metric (number of jQuery files left).

## 433: Tests pass alone but fail when run together. A singleton is suspected. How do you fix it?

The singleton keeps state between tests, so test order changes the result. Short-term:

- Reset its state in `beforeEach` (expose a test-only reset or create a fresh instance).
- Use `vi.resetModules()` / `jest.resetModules()` and re-import the module in each test so it is evaluated again.
- Make sure fake timers, mocks and listeners are restored after each test.

Long-term, fix the design: inject the dependency so each test creates its own instance, and keep the module-level singleton only in the composition root of the real app. Running tests in random order (Vitest `sequence.shuffle`) helps find such leaks.

## 434: Fifty dashboard widgets poll the same endpoint. How do you improve this?

- **Share one subscription** per resource: a store or query cache with deduplication, so all widgets read from one cached result and one request runs per interval.
- **Reference counting**: start polling when the first widget subscribes and stop when the last one unsubscribes.
- **Pause** polling when the tab is hidden (`document.visibilityState`) and resume on focus.
- **Batch** different resources into one request if the API supports it.
- **Push instead of poll** if updates are frequent: one WebSocket or SSE connection feeding the store.
- **Leader tab** with Web Locks so only one tab polls and broadcasts to the others.

## 435: How do you share one expensive subscription between many consumers?

Count subscribers. Start the underlying source when the count goes from 0 to 1, and stop it when it goes back to 0.

```js
function shared(start) {
  let stop = null;
  let count = 0;
  const listeners = new Set();

  return function subscribe(listener) {
    listeners.add(listener);
    if (count++ === 0)
      stop = start((value) => listeners.forEach((l) => l(value)));
    return () => {
      listeners.delete(listener);
      if (--count === 0) {
        stop();
        stop = null;
      }
    };
  };
}

const subscribePrices = shared((emit) => {
  const ws = new WebSocket("wss://example.com/prices");
  ws.onmessage = (e) => emit(JSON.parse(e.data));
  return () => ws.close();
});
```

RxJS has this built in with `share()`. A short delay before stopping helps when one consumer unsubscribes and another subscribes right after, like during route changes.

## 436: In what order should you stack decorators like auth, retry, timeout and cache around an HTTP call?

Order changes behavior, so decide on purpose. A common order from outside to inside:

1. **Cache**: return early if there is a fresh cached value, so no other layer runs.
2. **Dedupe**: share in-flight requests.
3. **Retry**: retries the inner layers as a whole.
4. **Timeout**: applies per attempt (inside retry), not to all attempts together, unless you want an overall deadline too.
5. **Auth**: adds the token per attempt, so a retry after a token refresh uses the new token.
6. **Transport**: the actual `fetch`.

```js
const get = withCache(
  withDedupe(withRetry(withTimeout(withAuth(fetchJson), 5000))),
);
```

Putting timeout outside retry would give all attempts a single 5-second budget. Putting cache inside retry would retry cache misses unnecessarily.

## 437: How do you spot over-engineering with design patterns?

Signs:

- Interfaces or factories with exactly one implementation and no real plan for a second.
- More files for abstractions than for the actual logic.
- You need to jump through four layers to find where a value is computed.
- Names like `AbstractUserServiceFactoryProvider`.
- Generic "frameworks" inside the app for problems that occur once.
- New team members can't make simple changes without help.

The cure is to inline abstractions that don't pay for themselves, and add them back only when a second real use case appears (the "rule of three").

## 438: When should you remove a pattern from a codebase?

When the problem it solved is gone or the cost is higher than the benefit. Examples: an adapter around a library you'll never replace and that now just copies its API, an event bus with two events left, a DI container in an app small enough for a composition root, or a HOC that a hook replaced. Remove it the same way you added it: small steps with tests. Deleting unneeded abstraction is as valuable as adding needed abstraction.

## 439: How do Node.js streams use patterns, and how should you connect them?

Streams combine Observer (they are `EventEmitter`s), Iterator (readable streams are async iterable) and Pipeline (Chain of Responsibility through `pipe`). Use `pipeline` from `node:stream/promises` instead of `.pipe()`, because `pipe` doesn't forward errors or clean up the other streams when one fails.

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("access.log"),
  createGzip(),
  createWriteStream("access.log.gz"),
);
```

You can also put async generator functions in a `pipeline` as transform steps.

## 440: How do you keep an Observer-based store fast with thousands of subscribers?

Notifying everyone on every change and letting each one compare its selected value costs O(subscribers) per update, which adds up.

- **Keyed subscriptions**: subscribers register for a specific key or entity id, and an update only notifies that key's subscribers.
- **Selector memoization**: make the comparison cheap and avoid re-renders when the selected value is the same.
- **Batching**: combine many updates into one notification pass.
- **Fine-grained signals**: dependency tracking means only true dependents run.
- **Virtualization**: fewer mounted components means fewer subscribers.

Profile first; often the expensive part is re-rendering, not the notification loop.

## 441: When should consumers subscribe by topic and when by selector?

**Topic subscriptions** (Pub/Sub) suit events where you care about the message itself: "orderPlaced", "socket reconnected". **Selector subscriptions** suit state, where you care about the current value and want to be notified only when your part changes: `useStore((s) => s.cart.count)`. Mixing them up causes bugs: with topics for state, late subscribers miss the current value; with selectors for events, two identical events in a row look like "no change". Many apps use both: a store for state and a small event channel for one-off events.

## 442: Why is equality for value objects awkward in JavaScript, and what can you do?

JavaScript compares objects by reference, and there is no operator overloading, so two `Money(10, "EUR")` objects are never `===`, and they don't work as `Map` keys by value. The Records and Tuples proposal that would have added deeply immutable value types was withdrawn. Workarounds:

- An `equals` method and helper functions for comparison.
- Normalize to a primitive key (`"10:EUR"`) for maps and sets.
- Intern instances through a flyweight cache so equal values share one object, which makes `===` work.

```js
const cache = new Map();
function money(amount, currency) {
  const key = `${amount}:${currency}`;
  if (!cache.has(key)) cache.set(key, Object.freeze({ amount, currency }));
  return cache.get(key);
}

money(10, "EUR") === money(10, "EUR"); // true
```

Interning needs care with memory (it grows unless you limit it).

## 443: How might the pattern matching proposal change State and Strategy code?

The TC39 pattern matching proposal (still in progress, not usable natively yet) would add a `match` expression that checks the shape of a value and picks a branch, similar to `switch` but for structures. Code that picks behavior by `state.status` or action shape could become shorter and safer, with destructuring built in. Until then, discriminated unions in TypeScript with exhaustive `switch` statements, or lookup objects keyed by status, give similar results. It's useful to mention it but not to rely on it in an interview answer as if it exists.

## 444: Why do Redux and similar tools require actions and state to be serializable?

Serializable state and actions (plain objects, arrays, primitives) let you:

- Log and replay actions for debugging and time travel.
- Persist state to storage and restore it.
- Send state from server to client for SSR.
- Sync state between tabs or with a server.
- Compare state easily.

Class instances, functions, promises and `Map`s break some of these. Redux Toolkit's middleware warns about non-serializable values. It is a constraint that turns the Command pattern into something you can store and send over the network.

## 445: What does time-travel debugging need from an app's architecture?

- All state changes go through one place (dispatch), so they can be recorded.
- Reducers are pure, so replaying the same actions gives the same state.
- State is immutable, so old snapshots stay valid.
- Side effects (API calls, timers) live outside reducers, so replay doesn't repeat them.
- State and actions are serializable.

If any of these is missing, replaying actions gives different results or triggers real side effects. These same properties also make the app easier to test.

## 446: What are the risks of schema-driven (config-driven) UIs at scale?

A schema that describes forms or pages, interpreted at runtime, is the Interpreter pattern. Risks:

- The schema slowly becomes a programming language (conditions, loops, expressions) without a real debugger, types or tests.
- Errors show up at runtime instead of build time.
- Performance suffers when every render interprets a large schema.
- Security issues if schemas come from users and can reference arbitrary components or expressions.

Keep the schema language small, validate schemas with a JSON Schema or Zod, map components through an allowlist registry, and allow escape hatches to real code for complex cases.

## 447: How does error handling work in middleware chains?

In Express, an error middleware has four parameters `(err, req, res, next)`. Calling `next(err)` or throwing (Express 5 also catches rejected promises from async handlers) skips normal middleware and jumps to error middleware. In Koa, you wrap `await next()` in `try/catch` in an early middleware, because errors bubble back up the promise chain. In Redux, a middleware can catch errors from `next(action)`. The general rules: put error handlers at the right end of the chain, always either respond or pass the error on, and make sure a middleware that short-circuits (doesn't call `next`) does so on purpose.

## 448: How can you do dependency injection in React?

Context is React's built-in DI mechanism. Provide services at the top and read them in components or hooks:

```jsx
const ServicesContext = createContext(null);

export function ServicesProvider({ services, children }) {
  return <ServicesContext value={services}>{children}</ServicesContext>;
}

export function useServices() {
  const services = use(ServicesContext);
  if (!services)
    throw new Error("useServices must be used inside ServicesProvider");
  return services;
}

// in tests
render(
  <ServicesProvider services={{ api: fakeApi, clock: fakeClock }}>
    <OrderPage />
  </ServicesProvider>,
);
```

Since the services object rarely changes, it doesn't cause re-render problems. Keep services stable (create them once), and keep fast-changing state out of this context.

## 449: How does TypeScript change the way you use design patterns in JavaScript?

- **Interfaces become real contracts**: Strategy, Adapter and Repository implementations are checked at build time.
- **Discriminated unions** make State, Command and Result patterns safer with exhaustive checks.
- **Generics** let you write typed factories, builders, event emitters and stores once.
- **Some patterns become types only**: branded types instead of runtime value wrappers, `readonly` instead of freezing in many places.
- **Decorators and DI** frameworks (Angular, NestJS) lean on TypeScript.

Types also make over-engineering more expensive to read, so the "keep it simple" rule matters even more.

## 450: How do you explain a pattern choice in a system design interview?

Walk through it in this order:

1. **The problem**: what changes often, what must stay stable, what hurts today.
2. **The options**: two or three realistic choices, including "no pattern, just a function".
3. **Trade-offs**: complexity, testability, performance, team familiarity, how easy it is to undo.
4. **The decision**: pick one and say why it fits this case.
5. **Limits**: when you would revisit it (team size, scale, new requirements).

Interviewers care less about naming the pattern correctly and more about whether you understand why it helps here, what it costs, and when you would not use it.
