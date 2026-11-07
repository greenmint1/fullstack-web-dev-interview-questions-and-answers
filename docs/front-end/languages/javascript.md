# JavaScript Interview Questions and Answers

_Last updated: October 28, 2026_

450 JavaScript interview questions with answers and code examples, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers follow current JavaScript (ES2025 and newer), and mention when a feature is new or not supported everywhere yet.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is JavaScript?](#1-what-is-javascript)
- [2: What is the difference between JavaScript and ECMAScript?](#2-what-is-the-difference-between-javascript-and-ecmascript)
- [3: What are the data types in JavaScript?](#3-what-are-the-data-types-in-javascript)
- [4: What is the difference between primitive and reference types?](#4-what-is-the-difference-between-primitive-and-reference-types)
- [5: What are the ways to declare a variable in JavaScript?](#5-what-are-the-ways-to-declare-a-variable-in-javascript)
- [6: What is the difference between var, let and const?](#6-what-is-the-difference-between-var-let-and-const)
- [7: Can you change the contents of an object declared with const?](#7-can-you-change-the-contents-of-an-object-declared-with-const)
- [8: What is the difference between null and undefined?](#8-what-is-the-difference-between-null-and-undefined)
- [9: What is the difference between == and ===?](#9-what-is-the-difference-between--and-)
- [10: What is NaN?](#10-what-is-nan)
- [11: How do you check if a value is NaN?](#11-how-do-you-check-if-a-value-is-nan)
- [12: What is the typeof operator?](#12-what-is-the-typeof-operator)
- [13: How do you check if a value is an array?](#13-how-do-you-check-if-a-value-is-an-array)
- [14: What is a function in JavaScript?](#14-what-is-a-function-in-javascript)
- [15: What are the different ways to define a function?](#15-what-are-the-different-ways-to-define-a-function)
- [16: What is an arrow function?](#16-what-is-an-arrow-function)
- [17: What is the difference between a function declaration and a function expression?](#17-what-is-the-difference-between-a-function-declaration-and-a-function-expression)
- [18: What are template literals?](#18-what-are-template-literals)
- [19: What is the difference between let and var inside a for loop?](#19-what-is-the-difference-between-let-and-var-inside-a-for-loop)
- [20: What is an object in JavaScript?](#20-what-is-an-object-in-javascript)
- [21: What are the different ways to create an object?](#21-what-are-the-different-ways-to-create-an-object)
- [22: What is the difference between dot notation and bracket notation?](#22-what-is-the-difference-between-dot-notation-and-bracket-notation)
- [23: How do you check if an object has a property?](#23-how-do-you-check-if-an-object-has-a-property)
- [24: How do you loop over an object?](#24-how-do-you-loop-over-an-object)
- [25: How do you delete a property from an object?](#25-how-do-you-delete-a-property-from-an-object)
- [26: What is an array?](#26-what-is-an-array)
- [27: What is the difference between push, pop, shift and unshift?](#27-what-is-the-difference-between-push-pop-shift-and-unshift)
- [28: What is the difference between slice and splice?](#28-what-is-the-difference-between-slice-and-splice)
- [29: What does the map method do?](#29-what-does-the-map-method-do)
- [30: What does the filter method do?](#30-what-does-the-filter-method-do)
- [31: What does the reduce method do?](#31-what-does-the-reduce-method-do)
- [32: What is the difference between forEach and map?](#32-what-is-the-difference-between-foreach-and-map)
- [33: What does the find method do?](#33-what-does-the-find-method-do)
- [34: What is the difference between includes and indexOf?](#34-what-is-the-difference-between-includes-and-indexof)
- [35: What do some and every do?](#35-what-do-some-and-every-do)
- [36: How do you sort an array?](#36-how-do-you-sort-an-array)
- [37: How do you join an array into a string and split a string into an array?](#37-how-do-you-join-an-array-into-a-string-and-split-a-string-into-an-array)
- [38: How do you get the last item of an array?](#38-how-do-you-get-the-last-item-of-an-array)
- [39: What is the spread operator?](#39-what-is-the-spread-operator)
- [40: What are rest parameters?](#40-what-are-rest-parameters)
- [41: What is destructuring?](#41-what-is-destructuring)
- [42: What are default parameters?](#42-what-are-default-parameters)
- [43: What are truthy and falsy values?](#43-what-are-truthy-and-falsy-values)
- [44: What does the !! operator do?](#44-what-does-the--operator-do)
- [45: What is the ternary operator?](#45-what-is-the-ternary-operator)
- [46: What is the nullish coalescing operator (??)?](#46-what-is-the-nullish-coalescing-operator-)
- [47: What is optional chaining (?.)?](#47-what-is-optional-chaining-)
- [48: What are logical assignment operators?](#48-what-are-logical-assignment-operators)
- [49: What is the difference between a for loop, for...in and for...of?](#49-what-is-the-difference-between-a-for-loop-forin-and-forof)
- [50: What is the difference between break and continue?](#50-what-is-the-difference-between-break-and-continue)
- [51: What is a switch statement?](#51-what-is-a-switch-statement)
- [52: What is the difference between while and do...while?](#52-what-is-the-difference-between-while-and-dowhile)
- [53: What is a string in JavaScript and are strings mutable?](#53-what-is-a-string-in-javascript-and-are-strings-mutable)
- [54: What are some common string methods?](#54-what-are-some-common-string-methods)
- [55: What is the difference between substring, substr and slice?](#55-what-is-the-difference-between-substring-substr-and-slice)
- [56: How do you convert a string to a number?](#56-how-do-you-convert-a-string-to-a-number)
- [57: How do you convert a number to a string?](#57-how-do-you-convert-a-number-to-a-string)
- [58: What is type coercion?](#58-what-is-type-coercion)
- [59: What is the difference between implicit and explicit type conversion?](#59-what-is-the-difference-between-implicit-and-explicit-type-conversion)
- [60: What is scope in JavaScript?](#60-what-is-scope-in-javascript)
- [61: What is hoisting?](#61-what-is-hoisting)
- [62: What is the temporal dead zone (TDZ)?](#62-what-is-the-temporal-dead-zone-tdz)
- [63: What is a callback function?](#63-what-is-a-callback-function)
- [64: What is the DOM?](#64-what-is-the-dom)
- [65: How do you select elements in the DOM?](#65-how-do-you-select-elements-in-the-dom)
- [66: How do you create and add an element to the page?](#66-how-do-you-create-and-add-an-element-to-the-page)
- [67: What is the difference between innerHTML, textContent and innerText?](#67-what-is-the-difference-between-innerhtml-textcontent-and-innertext)
- [68: How do you add an event listener?](#68-how-do-you-add-an-event-listener)
- [69: What is the event object?](#69-what-is-the-event-object)
- [70: What does preventDefault do?](#70-what-does-preventdefault-do)
- [71: What is the difference between alert, confirm and prompt?](#71-what-is-the-difference-between-alert-confirm-and-prompt)
- [72: What is console.log and what other console methods exist?](#72-what-is-consolelog-and-what-other-console-methods-exist)
- [73: What is the difference between setTimeout and setInterval?](#73-what-is-the-difference-between-settimeout-and-setinterval)
- [74: What does setTimeout with 0 delay do?](#74-what-does-settimeout-with-0-delay-do)
- [75: What is JSON?](#75-what-is-json)
- [76: How do you convert between JSON and JavaScript objects?](#76-how-do-you-convert-between-json-and-javascript-objects)
- [77: What is the Math object?](#77-what-is-the-math-object)
- [78: How do you generate a random integer in a range?](#78-how-do-you-generate-a-random-integer-in-a-range)
- [79: What is the exponentiation operator?](#79-what-is-the-exponentiation-operator)
- [80: What is the modulo (%) operator?](#80-what-is-the-modulo--operator)
- [81: What is the difference between i++ and ++i?](#81-what-is-the-difference-between-i-and-i)
- [82: What is a Date object and how do you use it?](#82-what-is-a-date-object-and-how-do-you-use-it)
- [83: How do you format a date for display?](#83-how-do-you-format-a-date-for-display)
- [84: What are comments in JavaScript?](#84-what-are-comments-in-javascript)
- [85: What is "use strict"?](#85-what-is-use-strict)
- [86: What is the global object?](#86-what-is-the-global-object)
- [87: What is the difference between an argument and a parameter?](#87-what-is-the-difference-between-an-argument-and-a-parameter)
- [88: What happens if you call a function with fewer or more arguments than parameters?](#88-what-happens-if-you-call-a-function-with-fewer-or-more-arguments-than-parameters)
- [89: What does a function return if there is no return statement?](#89-what-does-a-function-return-if-there-is-no-return-statement)
- [90: What is the arguments object?](#90-what-is-the-arguments-object)
- [91: What is an IIFE?](#91-what-is-an-iife)
- [92: What is a method?](#92-what-is-a-method)
- [93: What is the "this" keyword (basic idea)?](#93-what-is-the-this-keyword-basic-idea)
- [94: What is an array-like object?](#94-what-is-an-array-like-object)
- [95: How do you copy an array?](#95-how-do-you-copy-an-array)
- [96: How do you merge two arrays?](#96-how-do-you-merge-two-arrays)
- [97: How do you remove duplicates from an array?](#97-how-do-you-remove-duplicates-from-an-array)
- [98: How do you check if a string contains another string?](#98-how-do-you-check-if-a-string-contains-another-string)
- [99: How do you reverse a string?](#99-how-do-you-reverse-a-string)
- [100: What is the difference between let x; and let x = null;?](#100-what-is-the-difference-between-let-x-and-let-x--null)
- [101: What is a Promise (basic idea)?](#101-what-is-a-promise-basic-idea)
- [102: What are async and await?](#102-what-are-async-and-await)
- [103: How do you make an HTTP request in JavaScript?](#103-how-do-you-make-an-http-request-in-javascript)
- [104: What is try...catch...finally?](#104-what-is-trycatchfinally)
- [105: How do you throw an error?](#105-how-do-you-throw-an-error)
- [106: What are the built-in error types?](#106-what-are-the-built-in-error-types)
- [107: What is the difference between a SyntaxError and a runtime error?](#107-what-is-the-difference-between-a-syntaxerror-and-a-runtime-error)
- [108: What is a Set?](#108-what-is-a-set)
- [109: What is a Map?](#109-what-is-a-map)
- [110: What is the difference between a Map and an object?](#110-what-is-the-difference-between-a-map-and-an-object)
- [111: What is a Symbol?](#111-what-is-a-symbol)
- [112: What is BigInt?](#112-what-is-bigint)
- [113: What is Number.MAX_SAFE_INTEGER?](#113-what-is-numbermax_safe_integer)
- [114: Why does 0.1 + 0.2 not equal 0.3?](#114-why-does-01--02-not-equal-03)
- [115: What is Infinity?](#115-what-is-infinity)
- [116: How do you check if a value is an integer?](#116-how-do-you-check-if-a-value-is-an-integer)
- [117: What is the difference between Number.isFinite and the global isFinite?](#117-what-is-the-difference-between-numberisfinite-and-the-global-isfinite)
- [118: How do you format numbers for display?](#118-how-do-you-format-numbers-for-display)
- [119: What are labels in JavaScript?](#119-what-are-labels-in-javascript)
- [120: What is a class in JavaScript?](#120-what-is-a-class-in-javascript)
- [121: What is a constructor?](#121-what-is-a-constructor)
- [122: What is inheritance with classes?](#122-what-is-inheritance-with-classes)
- [123: What does super do?](#123-what-does-super-do)
- [124: What are static methods?](#124-what-are-static-methods)
- [125: What are getters and setters?](#125-what-are-getters-and-setters)
- [126: What is the instanceof operator?](#126-what-is-the-instanceof-operator)
- [127: What are ES modules?](#127-what-are-es-modules)
- [128: What is the difference between named and default exports?](#128-what-is-the-difference-between-named-and-default-exports)
- [129: What is localStorage?](#129-what-is-localstorage)
- [130: What is the difference between localStorage, sessionStorage and cookies?](#130-what-is-the-difference-between-localstorage-sessionstorage-and-cookies)
- [131: What is event bubbling?](#131-what-is-event-bubbling)
- [132: How do you stop event bubbling?](#132-how-do-you-stop-event-bubbling)
- [133: What is the difference between == null and === null?](#133-what-is-the-difference-between--null-and--null)
- [134: What is the comma operator?](#134-what-is-the-comma-operator)
- [135: What is the void operator?](#135-what-is-the-void-operator)
- [136: What is the difference between Object.keys and Object.entries?](#136-what-is-the-difference-between-objectkeys-and-objectentries)
- [137: How do you merge objects?](#137-how-do-you-merge-objects)
- [138: What is Object.freeze?](#138-what-is-objectfreeze)
- [139: What is the difference between Object.freeze and Object.seal?](#139-what-is-the-difference-between-objectfreeze-and-objectseal)
- [140: What is a pure function?](#140-what-is-a-pure-function)
- [141: What is the difference between mutable and immutable operations on arrays?](#141-what-is-the-difference-between-mutable-and-immutable-operations-on-arrays)
- [142: How do you fill an array with values?](#142-how-do-you-fill-an-array-with-values)
- [143: What does Array.from do?](#143-what-does-arrayfrom-do)
- [144: What does Array.of do?](#144-what-does-arrayof-do)
- [145: What does flat do?](#145-what-does-flat-do)
- [146: How do you empty an array?](#146-how-do-you-empty-an-array)
- [147: What is a NodeList and how is it different from an array?](#147-what-is-a-nodelist-and-how-is-it-different-from-an-array)
- [148: What is the difference between an attribute and a property in the DOM?](#148-what-is-the-difference-between-an-attribute-and-a-property-in-the-dom)
- [149: What are data attributes?](#149-what-are-data-attributes)
- [150: What are the main differences between JavaScript and TypeScript?](#150-what-are-the-main-differences-between-javascript-and-typescript)

### Moderate Questions (151-300)

- [151: What is a closure?](#151-what-is-a-closure)
- [152: What are some practical uses of closures?](#152-what-are-some-practical-uses-of-closures)
- [153: What is lexical scope?](#153-what-is-lexical-scope)
- [154: What is the scope chain?](#154-what-is-the-scope-chain)
- [155: How does "this" work in different situations?](#155-how-does-this-work-in-different-situations)
- [156: What is the difference between call, apply and bind?](#156-what-is-the-difference-between-call-apply-and-bind)
- [157: Why do you lose "this" when passing a method as a callback?](#157-why-do-you-lose-this-when-passing-a-method-as-a-callback)
- [158: Can you change "this" in an arrow function using call or bind?](#158-can-you-change-this-in-an-arrow-function-using-call-or-bind)
- [159: When should you not use an arrow function?](#159-when-should-you-not-use-an-arrow-function)
- [160: What is a prototype?](#160-what-is-a-prototype)
- [161: What is the prototype chain?](#161-what-is-the-prototype-chain)
- [162: What is the difference between `__proto__` and prototype?](#162-what-is-the-difference-between-__proto__-and-prototype)
- [163: How do classes relate to prototypes?](#163-how-do-classes-relate-to-prototypes)
- [164: What does the new keyword do?](#164-what-does-the-new-keyword-do)
- [165: What is Object.create used for?](#165-what-is-objectcreate-used-for)
- [166: What are private class fields and methods?](#166-what-are-private-class-fields-and-methods)
- [167: How do you check if an object has a private field?](#167-how-do-you-check-if-an-object-has-a-private-field)
- [168: What are class fields?](#168-what-are-class-fields)
- [169: What is a static initialization block?](#169-what-is-a-static-initialization-block)
- [170: What is the event loop?](#170-what-is-the-event-loop)
- [171: What is the difference between microtasks and macrotasks?](#171-what-is-the-difference-between-microtasks-and-macrotasks)
- [172: What is the call stack?](#172-what-is-the-call-stack)
- [173: What is promise chaining?](#173-what-is-promise-chaining)
- [174: What is the difference between Promise.all, Promise.allSettled, Promise.race and Promise.any?](#174-what-is-the-difference-between-promiseall-promiseallsettled-promiserace-and-promiseany)
- [175: How do you run async operations in parallel vs one after another?](#175-how-do-you-run-async-operations-in-parallel-vs-one-after-another)
- [176: How do you handle errors with async/await?](#176-how-do-you-handle-errors-with-asyncawait)
- [177: What happens if you don't handle a rejected promise?](#177-what-happens-if-you-dont-handle-a-rejected-promise)
- [178: What does an async function return?](#178-what-does-an-async-function-return)
- [179: Can you use await outside of an async function?](#179-can-you-use-await-outside-of-an-async-function)
- [180: How do you create a sleep or delay function?](#180-how-do-you-create-a-sleep-or-delay-function)
- [181: What is Promise.withResolvers?](#181-what-is-promisewithresolvers)
- [182: What is Promise.try?](#182-what-is-promisetry)
- [183: How do you convert a callback-based function into a promise?](#183-how-do-you-convert-a-callback-based-function-into-a-promise)
- [184: What is callback hell and how do you avoid it?](#184-what-is-callback-hell-and-how-do-you-avoid-it)
- [185: What is debouncing?](#185-what-is-debouncing)
- [186: What is throttling?](#186-what-is-throttling)
- [187: What is a higher-order function?](#187-what-is-a-higher-order-function)
- [188: What is currying?](#188-what-is-currying)
- [189: What is partial application?](#189-what-is-partial-application)
- [190: What is memoization?](#190-what-is-memoization)
- [191: What is function composition?](#191-what-is-function-composition)
- [192: What is recursion?](#192-what-is-recursion)
- [193: What is the difference between a shallow copy and a deep copy?](#193-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy)
- [194: What is structuredClone?](#194-what-is-structuredclone)
- [195: Why is JSON.parse(JSON.stringify(obj)) not a good deep copy?](#195-why-is-jsonparsejsonstringifyobj-not-a-good-deep-copy)
- [196: What is event delegation?](#196-what-is-event-delegation)
- [197: What are the three phases of event propagation?](#197-what-are-the-three-phases-of-event-propagation)
- [198: What is the difference between event.target and event.currentTarget?](#198-what-is-the-difference-between-eventtarget-and-eventcurrenttarget)
- [199: How do you create and dispatch a custom event?](#199-how-do-you-create-and-dispatch-a-custom-event)
- [200: What are passive event listeners?](#200-what-are-passive-event-listeners)
- [201: What is the difference between DOMContentLoaded and load?](#201-what-is-the-difference-between-domcontentloaded-and-load)
- [202: What is the difference between async and defer on script tags?](#202-what-is-the-difference-between-async-and-defer-on-script-tags)
- [203: What is a generator function?](#203-what-is-a-generator-function)
- [204: What are iterables and iterators?](#204-what-are-iterables-and-iterators)
- [205: How do you make an object iterable with a generator?](#205-how-do-you-make-an-object-iterable-with-a-generator)
- [206: What are iterator helpers?](#206-what-are-iterator-helpers)
- [207: What are the new Set methods?](#207-what-are-the-new-set-methods)
- [208: What are Object.groupBy and Map.groupBy?](#208-what-are-objectgroupby-and-mapgroupby)
- [209: What are toSorted, toReversed, toSpliced and with?](#209-what-are-tosorted-toreversed-tospliced-and-with)
- [210: What are findLast and findLastIndex?](#210-what-are-findlast-and-findlastindex)
- [211: What is Array.fromAsync?](#211-what-is-arrayfromasync)
- [212: What is for await...of?](#212-what-is-for-awaitof)
- [213: What is an async generator?](#213-what-is-an-async-generator)
- [214: What is a WeakMap?](#214-what-is-a-weakmap)
- [215: What is a WeakSet?](#215-what-is-a-weakset)
- [216: What is the difference between Map and WeakMap?](#216-what-is-the-difference-between-map-and-weakmap)
- [217: What is a tagged template literal?](#217-what-is-a-tagged-template-literal)
- [218: What is String.raw?](#218-what-is-stringraw)
- [219: What is a regular expression and how do you create one?](#219-what-is-a-regular-expression-and-how-do-you-create-one)
- [220: What are named capture groups?](#220-what-are-named-capture-groups)
- [221: What is the difference between match and matchAll?](#221-what-is-the-difference-between-match-and-matchall)
- [222: What are lookahead and lookbehind in regex?](#222-what-are-lookahead-and-lookbehind-in-regex)
- [223: What is RegExp.escape?](#223-what-is-regexpescape)
- [224: What is Object.defineProperty?](#224-what-is-objectdefineproperty)
- [225: What are property descriptors?](#225-what-are-property-descriptors)
- [226: What is the difference between enumerable and non-enumerable properties?](#226-what-is-the-difference-between-enumerable-and-non-enumerable-properties)
- [227: What is Object.is?](#227-what-is-objectis)
- [228: How do you compare two objects or arrays for equality?](#228-how-do-you-compare-two-objects-or-arrays-for-equality)
- [229: What is short-circuit evaluation?](#229-what-is-short-circuit-evaluation)
- [230: What is an Error cause?](#230-what-is-an-error-cause)
- [231: How do you create a custom error class?](#231-how-do-you-create-a-custom-error-class)
- [232: What is AggregateError?](#232-what-is-aggregateerror)
- [233: What is AbortController?](#233-what-is-abortcontroller)
- [234: How do you add a timeout to fetch?](#234-how-do-you-add-a-timeout-to-fetch)
- [235: What are URL and URLSearchParams?](#235-what-are-url-and-urlsearchparams)
- [236: What is FormData?](#236-what-is-formdata)
- [237: What is the difference between dynamic import and static import?](#237-what-is-the-difference-between-dynamic-import-and-static-import)
- [238: What is the difference between CommonJS and ES modules?](#238-what-is-the-difference-between-commonjs-and-es-modules)
- [239: What are import attributes?](#239-what-are-import-attributes)
- [240: What is tree shaking?](#240-what-is-tree-shaking)
- [241: What is the difference between a polyfill and a transpiler?](#241-what-is-the-difference-between-a-polyfill-and-a-transpiler)
- [242: What is requestAnimationFrame?](#242-what-is-requestanimationframe)
- [243: What is IntersectionObserver?](#243-what-is-intersectionobserver)
- [244: What is MutationObserver?](#244-what-is-mutationobserver)
- [245: What is ResizeObserver?](#245-what-is-resizeobserver)
- [246: What is the difference between reflow and repaint?](#246-what-is-the-difference-between-reflow-and-repaint)
- [247: What is a Web Worker?](#247-what-is-a-web-worker)
- [248: What is a Service Worker?](#248-what-is-a-service-worker)
- [249: What is CORS?](#249-what-is-cors)
- [250: What is the same-origin policy?](#250-what-is-the-same-origin-policy)
- [251: What is the difference between null-prototype objects and normal objects?](#251-what-is-the-difference-between-null-prototype-objects-and-normal-objects)
- [252: What is prototype pollution?](#252-what-is-prototype-pollution)
- [253: What is the difference between Object.keys, Object.getOwnPropertyNames and Reflect.ownKeys?](#253-what-is-the-difference-between-objectkeys-objectgetownpropertynames-and-reflectownkeys)
- [254: In what order are object keys returned?](#254-in-what-order-are-object-keys-returned)
- [255: How do you implement a simple observer (pub/sub) pattern?](#255-how-do-you-implement-a-simple-observer-pubsub-pattern)
- [256: What is the module pattern?](#256-what-is-the-module-pattern)
- [257: How do you implement a singleton in JavaScript?](#257-how-do-you-implement-a-singleton-in-javascript)
- [258: What is a mixin?](#258-what-is-a-mixin)
- [259: What is method chaining?](#259-what-is-method-chaining)
- [260: What is the difference between composition and inheritance?](#260-what-is-the-difference-between-composition-and-inheritance)
- [261: What is the difference between an expression and a statement?](#261-what-is-the-difference-between-an-expression-and-a-statement)
- [262: What is automatic semicolon insertion (ASI)?](#262-what-is-automatic-semicolon-insertion-asi)
- [263: What is the difference between function.length and arguments.length?](#263-what-is-the-difference-between-functionlength-and-argumentslength)
- [264: What are sparse arrays?](#264-what-are-sparse-arrays)
- [265: What happens when you use delete on an array element?](#265-what-happens-when-you-use-delete-on-an-array-element)
- [266: How does Array.prototype.sort work with strings and accents?](#266-how-does-arrayprototypesort-work-with-strings-and-accents)
- [267: How do you sort an array of objects by multiple fields?](#267-how-do-you-sort-an-array-of-objects-by-multiple-fields)
- [268: What is the Intl object?](#268-what-is-the-intl-object)
- [269: Why does "😀".length return 2?](#269-why-does-length-return-2)
- [270: What is string normalization?](#270-what-is-string-normalization)
- [271: What are isWellFormed and toWellFormed?](#271-what-are-iswellformed-and-towellformed)
- [272: What are the main problems with the Date object?](#272-what-are-the-main-problems-with-the-date-object)
- [273: What is the Temporal API?](#273-what-is-the-temporal-api)
- [274: How do you compute the difference between two dates with Date?](#274-how-do-you-compute-the-difference-between-two-dates-with-date)
- [275: What does the "in" operator do?](#275-what-does-the-in-operator-do)
- [276: What are bitwise operators and when are they used?](#276-what-are-bitwise-operators-and-when-are-they-used)
- [277: What is the difference between Object.entries and Object.fromEntries?](#277-what-is-the-difference-between-objectentries-and-objectfromentries)
- [278: How do you flatten a nested object?](#278-how-do-you-flatten-a-nested-object)
- [279: How do you safely access a deeply nested value by a path string?](#279-how-do-you-safely-access-a-deeply-nested-value-by-a-path-string)
- [280: How do you chunk an array into groups of a given size?](#280-how-do-you-chunk-an-array-into-groups-of-a-given-size)
- [281: How do you find the intersection and difference of two arrays?](#281-how-do-you-find-the-intersection-and-difference-of-two-arrays)
- [282: How do you count occurrences of items in an array?](#282-how-do-you-count-occurrences-of-items-in-an-array)
- [283: How do you shuffle an array correctly?](#283-how-do-you-shuffle-an-array-correctly)
- [284: How do you check if a string is a palindrome?](#284-how-do-you-check-if-a-string-is-a-palindrome)
- [285: How do you capitalize the first letter of each word?](#285-how-do-you-capitalize-the-first-letter-of-each-word)
- [286: How do you convert between camelCase, snake_case and kebab-case?](#286-how-do-you-convert-between-camelcase-snake_case-and-kebab-case)
- [287: What is a pure vs impure array method example in React state updates?](#287-what-is-a-pure-vs-impure-array-method-example-in-react-state-updates)
- [288: What is the difference between Object.assign and spread for copying?](#288-what-is-the-difference-between-objectassign-and-spread-for-copying)
- [289: How does garbage collection work in JavaScript?](#289-how-does-garbage-collection-work-in-javascript)
- [290: What are common causes of memory leaks in JavaScript?](#290-what-are-common-causes-of-memory-leaks-in-javascript)
- [291: What does Function.prototype.toString return?](#291-what-does-functionprototypetostring-return)
- [292: What is the name property of a function?](#292-what-is-the-name-property-of-a-function)
- [293: What is a getter on an object literal and when is it useful?](#293-what-is-a-getter-on-an-object-literal-and-when-is-it-useful)
- [294: What is the difference between a library and a framework?](#294-what-is-the-difference-between-a-library-and-a-framework)
- [295: What is the difference between client-side and server-side rendering?](#295-what-is-the-difference-between-client-side-and-server-side-rendering)
- [296: What is hydration?](#296-what-is-hydration)
- [297: What does the debugger statement do?](#297-what-does-the-debugger-statement-do)
- [298: What is the difference between console.log of an object and its actual value at that time?](#298-what-is-the-difference-between-consolelog-of-an-object-and-its-actual-value-at-that-time)
- [299: What is the Clipboard API?](#299-what-is-the-clipboard-api)
- [300: What is the History API?](#300-what-is-the-history-api)

### Advanced Questions (301-450)

- [301: What is an execution context?](#301-what-is-an-execution-context)
- [302: How does closure work at the engine level?](#302-how-does-closure-work-at-the-engine-level)
- [303: Explain the abstract equality (==) algorithm.](#303-explain-the-abstract-equality--algorithm)
- [304: Why is [] == ![] true?](#304-why-is----true)
- [305: How does ToPrimitive work and what is Symbol.toPrimitive?](#305-how-does-toprimitive-work-and-what-is-symboltoprimitive)
- [306: What are the results of these expressions: [] + {}, {} + [], [] + [], {} + {}?](#306-what-are-the-results-of-these-expressions------------)
- [307: What is a Proxy?](#307-what-is-a-proxy)
- [308: What traps are available on a Proxy?](#308-what-traps-are-available-on-a-proxy)
- [309: What are proxy invariants?](#309-what-are-proxy-invariants)
- [310: What is Reflect and why use it with Proxy?](#310-what-is-reflect-and-why-use-it-with-proxy)
- [311: Why do private fields not work through a Proxy?](#311-why-do-private-fields-not-work-through-a-proxy)
- [312: How would you build a simple reactive system with Proxy?](#312-how-would-you-build-a-simple-reactive-system-with-proxy)
- [313: What are well-known symbols?](#313-what-are-well-known-symbols)
- [314: What is Symbol.species?](#314-what-is-symbolspecies)
- [315: What is new.target?](#315-what-is-newtarget)
- [316: How do you extend built-in classes like Array or Error, and what are the pitfalls?](#316-how-do-you-extend-built-in-classes-like-array-or-error-and-what-are-the-pitfalls)
- [317: What is a "home object" and how does super work in object literals?](#317-what-is-a-home-object-and-how-does-super-work-in-object-literals)
- [318: What happens when you assign to a property that exists on the prototype?](#318-what-happens-when-you-assign-to-a-property-that-exists-on-the-prototype)
- [319: What are WeakRef and FinalizationRegistry?](#319-what-are-weakref-and-finalizationregistry)
- [320: What is explicit resource management (using and await using)?](#320-what-is-explicit-resource-management-using-and-await-using)
- [321: What are DisposableStack and AsyncDisposableStack?](#321-what-are-disposablestack-and-asyncdisposablestack)
- [322: What are decorators in JavaScript?](#322-what-are-decorators-in-javascript)
- [323: What is the accessor keyword?](#323-what-is-the-accessor-keyword)
- [324: How would you implement Promise from scratch?](#324-how-would-you-implement-promise-from-scratch)
- [325: How would you implement Promise.all?](#325-how-would-you-implement-promiseall)
- [326: How would you implement Promise.allSettled and Promise.any?](#326-how-would-you-implement-promiseallsettled-and-promiseany)
- [327: How do you limit the number of concurrent async operations?](#327-how-do-you-limit-the-number-of-concurrent-async-operations)
- [328: How do you implement retry with exponential backoff?](#328-how-do-you-implement-retry-with-exponential-backoff)
- [329: How do you handle race conditions in async UI code?](#329-how-do-you-handle-race-conditions-in-async-ui-code)
- [330: How would you implement a debounce with leading, trailing and cancel options?](#330-how-would-you-implement-a-debounce-with-leading-trailing-and-cancel-options)
- [331: How would you implement an LRU cache?](#331-how-would-you-implement-an-lru-cache)
- [332: How would you write a deep clone function that handles circular references?](#332-how-would-you-write-a-deep-clone-function-that-handles-circular-references)
- [333: How do you deep freeze an object?](#333-how-do-you-deep-freeze-an-object)
- [334: How would you implement Function.prototype.bind?](#334-how-would-you-implement-functionprototypebind)
- [335: How would you implement call and apply?](#335-how-would-you-implement-call-and-apply)
- [336: How would you implement instanceof?](#336-how-would-you-implement-instanceof)
- [337: How do live bindings work in ES modules?](#337-how-do-live-bindings-work-in-es-modules)
- [338: What happens with circular dependencies in ES modules?](#338-what-happens-with-circular-dependencies-in-es-modules)
- [339: In what order are ES modules evaluated?](#339-in-what-order-are-es-modules-evaluated)
- [340: What is import.meta?](#340-what-is-importmeta)
- [341: What are import maps?](#341-what-are-import-maps)
- [342: What is the difference between process.nextTick, queueMicrotask, setImmediate and setTimeout in Node.js?](#342-what-is-the-difference-between-processnexttick-queuemicrotask-setimmediate-and-settimeout-in-nodejs)
- [343: What are the phases of the Node.js event loop?](#343-what-are-the-phases-of-the-nodejs-event-loop)
- [344: What is backpressure in streams?](#344-what-is-backpressure-in-streams)
- [345: How do Web Streams work?](#345-how-do-web-streams-work)
- [346: How do you create your own ReadableStream?](#346-how-do-you-create-your-own-readablestream)
- [347: What is SharedArrayBuffer and Atomics?](#347-what-is-sharedarraybuffer-and-atomics)
- [348: What are typed arrays and when should you use them?](#348-what-are-typed-arrays-and-when-should-you-use-them)
- [349: What is DataView?](#349-what-is-dataview)
- [350: What are resizable ArrayBuffers and ArrayBuffer.transfer?](#350-what-are-resizable-arraybuffers-and-arraybuffertransfer)
- [351: What are transferable objects?](#351-what-are-transferable-objects)
- [352: What are MessageChannel and BroadcastChannel?](#352-what-are-messagechannel-and-broadcastchannel)
- [353: How do you communicate safely with an iframe using postMessage?](#353-how-do-you-communicate-safely-with-an-iframe-using-postmessage)
- [354: How does JavaScript engine optimization work (JIT compilation)?](#354-how-does-javascript-engine-optimization-work-jit-compilation)
- [355: What are hidden classes (shapes) and inline caches?](#355-what-are-hidden-classes-shapes-and-inline-caches)
- [356: What are "elements kinds" in V8 and why do they matter for arrays?](#356-what-are-elements-kinds-in-v8-and-why-do-they-matter-for-arrays)
- [357: How do you measure performance in JavaScript?](#357-how-do-you-measure-performance-in-javascript)
- [358: What are Core Web Vitals and how does JavaScript affect them?](#358-what-are-core-web-vitals-and-how-does-javascript-affect-them)
- [359: What is a long task and how do you break it up?](#359-what-is-a-long-task-and-how-do-you-break-it-up)
- [360: What is the Scheduler API (scheduler.postTask and scheduler.yield)?](#360-what-is-the-scheduler-api-schedulerposttask-and-scheduleryield)
- [361: What is requestIdleCallback?](#361-what-is-requestidlecallback)
- [362: In what order do rendering steps, requestAnimationFrame and tasks run in the browser?](#362-in-what-order-do-rendering-steps-requestanimationframe-and-tasks-run-in-the-browser)
- [363: What does "don't release Zalgo" mean?](#363-what-does-dont-release-zalgo-mean)
- [364: What is a thenable?](#364-what-is-a-thenable)
- [365: Predict the output of this async ordering puzzle.](#365-predict-the-output-of-this-async-ordering-puzzle)
- [366: Why does returning a promise from an async function or then add extra ticks?](#366-why-does-returning-a-promise-from-an-async-function-or-then-add-extra-ticks)
- [367: What is the difference between return await and return in an async function?](#367-what-is-the-difference-between-return-await-and-return-in-an-async-function)
- [368: How do you cancel a promise-based operation?](#368-how-do-you-cancel-a-promise-based-operation)
- [369: How do generators work as two-way communication (next, return, throw)?](#369-how-do-generators-work-as-two-way-communication-next-return-throw)
- [370: How can generators be used to implement async/await-like behavior?](#370-how-can-generators-be-used-to-implement-asyncawait-like-behavior)
- [371: What happens to an iterator when you break out of a for...of loop?](#371-what-happens-to-an-iterator-when-you-break-out-of-a-forof-loop)
- [372: What is a trampoline and why is it used?](#372-what-is-a-trampoline-and-why-is-it-used)
- [373: What is the difference between eval and new Function?](#373-what-is-the-difference-between-eval-and-new-function)
- [374: How does block-level function declaration behave in sloppy mode?](#374-how-does-block-level-function-declaration-behave-in-sloppy-mode)
- [375: What is the difference between a realm and a context, and why does instanceof fail across iframes?](#375-what-is-the-difference-between-a-realm-and-a-context-and-why-does-instanceof-fail-across-iframes)
- [376: What is Error.isError?](#376-what-is-erroriserror)
- [377: How do you get better stack traces in JavaScript?](#377-how-do-you-get-better-stack-traces-in-javascript)
- [378: What is the JSON.stringify replacer, space and toJSON?](#378-what-is-the-jsonstringify-replacer-space-and-tojson)
- [379: How do you use a JSON.parse reviver?](#379-how-do-you-use-a-jsonparse-reviver)
- [380: How do you safely parse numbers that are too large for JavaScript?](#380-how-do-you-safely-parse-numbers-that-are-too-large-for-javascript)
- [381: What is Math.sumPrecise?](#381-what-is-mathsumprecise)
- [382: How do you convert between Uint8Array and base64 or hex?](#382-how-do-you-convert-between-uint8array-and-base64-or-hex)
- [383: What is the RegExp v flag?](#383-what-is-the-regexp-v-flag)
- [384: What are regex modifiers?](#384-what-are-regex-modifiers)
- [385: What does the regex d flag (hasIndices) do?](#385-what-does-the-regex-d-flag-hasindices-do)
- [386: How do you write a simple tokenizer using the sticky (y) flag?](#386-how-do-you-write-a-simple-tokenizer-using-the-sticky-y-flag)
- [387: What is catastrophic backtracking (ReDoS)?](#387-what-is-catastrophic-backtracking-redos)
- [388: Why are tagged template strings arrays cached?](#388-why-are-tagged-template-strings-arrays-cached)
- [389: What are Web Components?](#389-what-are-web-components)
- [390: What is the difference between open and closed shadow roots?](#390-what-is-the-difference-between-open-and-closed-shadow-roots)
- [391: How do you prevent XSS in JavaScript applications?](#391-how-do-you-prevent-xss-in-javascript-applications)
- [392: What is Content Security Policy (CSP)?](#392-what-is-content-security-policy-csp)
- [393: What are Trusted Types?](#393-what-are-trusted-types)
- [394: What is CSRF and how do you protect against it?](#394-what-is-csrf-and-how-do-you-protect-against-it)
- [395: Where should you store authentication tokens in the browser?](#395-where-should-you-store-authentication-tokens-in-the-browser)
- [396: What is IndexedDB?](#396-what-is-indexeddb)
- [397: What is the Cache API and how is it different from HTTP cache?](#397-what-is-the-cache-api-and-how-is-it-different-from-http-cache)
- [398: What is the difference between WebSocket, Server-Sent Events and long polling?](#398-what-is-the-difference-between-websocket-server-sent-events-and-long-polling)
- [399: How do you stream a response from a server with fetch?](#399-how-do-you-stream-a-response-from-a-server-with-fetch)
- [400: What is the difference between structuredClone and postMessage serialization?](#400-what-is-the-difference-between-structuredclone-and-postmessage-serialization)
- [401: What is AsyncLocalStorage in Node.js?](#401-what-is-asynclocalstorage-in-nodejs)
- [402: What is the difference between worker_threads, child_process and cluster in Node.js?](#402-what-is-the-difference-between-worker_threads-child_process-and-cluster-in-nodejs)
- [403: What is the "exports" field in package.json?](#403-what-is-the-exports-field-in-packagejson)
- [404: What is the dual package hazard?](#404-what-is-the-dual-package-hazard)
- [405: How do you test code that uses timers?](#405-how-do-you-test-code-that-uses-timers)
- [406: What are signals and how would you implement a basic one?](#406-what-are-signals-and-how-would-you-implement-a-basic-one)
- [407: How would you implement a minimal Redux-style store?](#407-how-would-you-implement-a-minimal-redux-style-store)
- [408: How does a virtual DOM and diffing work?](#408-how-does-a-virtual-dom-and-diffing-work)
- [409: What is list virtualization?](#409-what-is-list-virtualization)
- [410: What is a stale closure?](#410-what-is-a-stale-closure)
- [411: How do you memoize a function with multiple object arguments without leaking memory?](#411-how-do-you-memoize-a-function-with-multiple-object-arguments-without-leaking-memory)
- [412: How would you implement a mutex or semaphore for async code?](#412-how-would-you-implement-a-mutex-or-semaphore-for-async-code)
- [413: How would you add a timeout to any promise?](#413-how-would-you-add-a-timeout-to-any-promise)
- [414: How would you implement a deep merge?](#414-how-would-you-implement-a-deep-merge)
- [415: How would you write polyfills for map and reduce?](#415-how-would-you-write-polyfills-for-map-and-reduce)
- [416: How would you flatten a deeply nested array without recursion?](#416-how-would-you-flatten-a-deeply-nested-array-without-recursion)
- [417: How would you implement promisify?](#417-how-would-you-implement-promisify)
- [418: How would you implement an EventEmitter with once and error handling?](#418-how-would-you-implement-an-eventemitter-with-once-and-error-handling)
- [419: How would you write a tag function that safely escapes HTML?](#419-how-would-you-write-a-tag-function-that-safely-escapes-html)
- [420: How would you compose async functions into a pipeline?](#420-how-would-you-compose-async-functions-into-a-pipeline)
- [421: What is Proxy.revocable?](#421-what-is-proxyrevocable)
- [422: How would you use a Proxy to support negative array indexes?](#422-how-would-you-use-a-proxy-to-support-negative-array-indexes)
- [423: Can symbols be used as WeakMap keys?](#423-can-symbols-be-used-as-weakmap-keys)
- [424: What is negative zero and where does it show up?](#424-what-is-negative-zero-and-where-does-it-show-up)
- [425: What are Math.imul, Math.clz32 and Math.fround used for?](#425-what-are-mathimul-mathclz32-and-mathfround-used-for)
- [426: How is the arguments object linked to parameters in sloppy mode?](#426-how-is-the-arguments-object-linked-to-parameters-in-sloppy-mode)
- [427: What is the with statement and why is it not allowed in strict mode?](#427-what-is-the-with-statement-and-why-is-it-not-allowed-in-strict-mode)
- [428: What is a self-replacing (lazy) getter?](#428-what-is-a-self-replacing-lazy-getter)
- [429: How do you count words or characters correctly in any language?](#429-how-do-you-count-words-or-characters-correctly-in-any-language)
- [430: When are iterator helpers better than array methods?](#430-when-are-iterator-helpers-better-than-array-methods)
- [431: How would you merge several async iterables into one as values arrive?](#431-how-would-you-merge-several-async-iterables-into-one-as-values-arrive)
- [432: How does JavaScript work with WebAssembly?](#432-how-does-javascript-work-with-webassembly)
- [433: What is the difference between a dedicated worker, a shared worker and a service worker?](#433-what-is-the-difference-between-a-dedicated-worker-a-shared-worker-and-a-service-worker)
- [434: What is OffscreenCanvas?](#434-what-is-offscreencanvas)
- [435: What is the View Transitions API?](#435-what-is-the-view-transitions-api)
- [436: What are source maps?](#436-what-are-source-maps)
- [437: What techniques do you use to reduce JavaScript bundle size?](#437-what-techniques-do-you-use-to-reduce-javascript-bundle-size)
- [438: What are preload, prefetch, modulepreload and fetchpriority?](#438-what-are-preload-prefetch-modulepreload-and-fetchpriority)
- [439: How do you find and fix memory leaks in a web app?](#439-how-do-you-find-and-fix-memory-leaks-in-a-web-app)
- [440: How do you detect and avoid blocking the event loop in Node.js?](#440-how-do-you-detect-and-avoid-blocking-the-event-loop-in-nodejs)
- [441: What is cross-origin isolation (COOP and COEP)?](#441-what-is-cross-origin-isolation-coop-and-coep)
- [442: How can you run untrusted JavaScript code more safely?](#442-how-can-you-run-untrusted-javascript-code-more-safely)
- [443: How do you do dependency injection in JavaScript?](#443-how-do-you-do-dependency-injection-in-javascript)
- [444: How would you use the strategy pattern in JavaScript?](#444-how-would-you-use-the-strategy-pattern-in-javascript)
- [445: What is structural sharing and how does Immer work?](#445-what-is-structural-sharing-and-how-does-immer-work)
- [446: What are the TC39 stages for new JavaScript features?](#446-what-are-the-tc39-stages-for-new-javascript-features)
- [447: What features were added in recent ECMAScript versions?](#447-what-features-were-added-in-recent-ecmascript-versions)
- [448: How do you write a function that works with both sync and async iterables?](#448-how-do-you-write-a-function-that-works-with-both-sync-and-async-iterables)
- [449: How would you design an autocomplete search input?](#449-how-would-you-design-an-autocomplete-search-input)
- [450: How would you explain the full lifecycle of a click in a browser, from the user to the screen update?](#450-how-would-you-explain-the-full-lifecycle-of-a-click-in-a-browser-from-the-user-to-the-screen-update)

---

# Easy Questions (1-150)

### 1: What is JavaScript?

JavaScript is a programming language mainly used to make web pages interactive. It runs in every modern browser, and it also runs on servers and other places through runtimes like Node.js, Deno and Bun.

It is dynamically typed, single-threaded (with an event loop for async work), and supports object-oriented, functional and procedural styles. The language itself is standardized as ECMAScript, and a new version comes out every year (ES2015, ES2016 ... ES2025 and so on).

### 2: What is the difference between JavaScript and ECMAScript?

ECMAScript is the specification. It is written by a committee called TC39 and published by Ecma International. JavaScript is the most popular implementation of that specification.

Things like `Array.prototype.map` or `Promise` are part of ECMAScript. Things like `document`, `fetch` or `setTimeout` are not. They come from the environment (browser or Node.js), not from the language itself.

### 3: What are the data types in JavaScript?

There are 8 data types. Seven of them are primitive types:

- `string`
- `number`
- `bigint`
- `boolean`
- `undefined`
- `null`
- `symbol`

And one non-primitive type:

- `object` (this includes arrays, functions, dates, maps, sets and so on)

```js
typeof "hello"; // "string"
typeof 42; // "number"
typeof 42n; // "bigint"
typeof true; // "boolean"
typeof undefined; // "undefined"
typeof Symbol(); // "symbol"
typeof {}; // "object"
typeof null; // "object" (a known old bug)
```

### 4: What is the difference between primitive and reference types?

Primitive values (string, number, boolean, etc.) are stored and copied by value. When you assign one to another variable, you get a separate copy.

Objects are reference types. A variable holds a reference to the object, so copying the variable copies the reference, not the object.

```js
let a = 10;
let b = a;
b = 20;
console.log(a); // 10

const obj1 = { name: "Ann" };
const obj2 = obj1;
obj2.name = "Bob";
console.log(obj1.name); // "Bob"
```

### 5: What are the ways to declare a variable in JavaScript?

There are three keywords: `var`, `let` and `const`.

- `var` is function-scoped and can be redeclared. It is the old way and is mostly avoided today.
- `let` is block-scoped and can be reassigned.
- `const` is block-scoped and cannot be reassigned.

```js
var x = 1;
let y = 2;
const z = 3;

y = 5; // ok
z = 10; // TypeError: Assignment to constant variable.
```

The general rule today is: use `const` by default and use `let` when you need to reassign.

### 6: What is the difference between var, let and const?

|                                   | `var`                           | `let`                          | `const`                        |
| --------------------------------- | ------------------------------- | ------------------------------ | ------------------------------ |
| Scope                             | Function                        | Block                          | Block                          |
| Redeclare in same scope           | Yes                             | No                             | No                             |
| Reassign                          | Yes                             | Yes                            | No                             |
| Hoisted                           | Yes, initialized as `undefined` | Yes, but in temporal dead zone | Yes, but in temporal dead zone |
| Creates property on global object | Yes (at top level of a script)  | No                             | No                             |

```js
if (true) {
  var a = 1;
  let b = 2;
}
console.log(a); // 1
console.log(b); // ReferenceError
```

### 7: Can you change the contents of an object declared with const?

Yes. `const` only means the variable cannot point to something else. The object itself can still be changed.

```js
const user = { name: "Ann" };
user.name = "Bob"; // works
user.age = 30; // works

user = {}; // TypeError
```

If you want to stop changes to the object, use `Object.freeze(user)`.

### 8: What is the difference between null and undefined?

`undefined` means a value was not assigned. JavaScript itself gives this value to variables that are declared but not set, missing function arguments, and missing object properties.

`null` is a value you assign on purpose to say "there is no value here".

```js
let a;
console.log(a); // undefined

let b = null;
console.log(b); // null

null == undefined; // true
null === undefined; // false
typeof null; // "object"
typeof undefined; // "undefined"
```

### 9: What is the difference between == and ===?

`==` is loose equality. It converts the values to the same type before comparing.

`===` is strict equality. It compares both the value and the type, without conversion.

```js
5 == "5"; // true
5 === "5"; // false
0 == false; // true
0 === false; // false
null == undefined; // true
null === undefined; // false
```

In most code you should use `===`, because the conversion rules of `==` are easy to get wrong.

### 10: What is NaN?

`NaN` means "Not a Number". It is the result of a math operation that does not give a valid number. Its type is still `"number"`.

```js
const result = "abc" * 2;
console.log(result); // NaN
console.log(typeof NaN); // "number"
console.log(NaN === NaN); // false
```

`NaN` is the only value in JavaScript that is not equal to itself.

### 11: How do you check if a value is NaN?

Use `Number.isNaN()`. It returns `true` only if the value is actually `NaN`.

```js
Number.isNaN(NaN); // true
Number.isNaN("hello"); // false

isNaN("hello"); // true (old global version converts the value first)
```

The global `isNaN()` converts the value to a number first, so it gives confusing results. `Object.is(value, NaN)` also works.

### 12: What is the typeof operator?

`typeof` returns a string that tells you the type of a value.

```js
typeof "text"; // "string"
typeof 10; // "number"
typeof true; // "boolean"
typeof undefined; // "undefined"
typeof {}; // "object"
typeof []; // "object"
typeof null; // "object"
typeof function () {}; // "function"
typeof Symbol("id"); // "symbol"
typeof 10n; // "bigint"
```

Note that arrays and `null` both return `"object"`. To check for an array use `Array.isArray()`.

### 13: How do you check if a value is an array?

Use `Array.isArray()`.

```js
Array.isArray([1, 2, 3]); // true
Array.isArray("abc"); // false
Array.isArray({ length: 0 }); // false
```

`value instanceof Array` also works in most cases, but it can fail when the array comes from another frame or realm. `Array.isArray` does not have this problem.

### 14: What is a function in JavaScript?

A function is a block of code that you can call by name, pass values into, and get a value back from. In JavaScript functions are also objects, so you can store them in variables, pass them to other functions and return them.

```js
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
```

### 15: What are the different ways to define a function?

```js
// Function declaration
function greet(name) {
  return `Hello, ${name}`;
}

// Function expression
const greet2 = function (name) {
  return `Hello, ${name}`;
};

// Arrow function
const greet3 = (name) => `Hello, ${name}`;

// Method in an object
const obj = {
  greet(name) {
    return `Hello, ${name}`;
  },
};

// Function constructor (rarely used)
const greet4 = new Function("name", "return 'Hello, ' + name");
```

There are also generator functions (`function*`), async functions (`async function`) and async generators (`async function*`).

### 16: What is an arrow function?

An arrow function is a shorter way to write a function.

```js
const square = (x) => x * x;

const sum = (a, b) => {
  const result = a + b;
  return result;
};

const makeUser = () => ({ name: "Ann" }); // wrap object in () to return it
```

Arrow functions are not just shorter. They also:

- do not have their own `this`, they use `this` from the outer scope
- do not have their own `arguments` object
- cannot be used with `new`
- do not have a `prototype` property

### 17: What is the difference between a function declaration and a function expression?

A function declaration is hoisted completely, so you can call it before the line where it is defined. A function expression is assigned to a variable, so it can only be used after that line runs.

```js
sayHi(); // works

function sayHi() {
  console.log("Hi");
}

sayBye(); // ReferenceError (because of const)

const sayBye = function () {
  console.log("Bye");
};
```

### 18: What are template literals?

Template literals are strings written with backticks. They let you put expressions inside `${}` and write multi-line strings.

```js
const name = "Ann";
const age = 25;

const text = `My name is ${name} and I am ${age} years old.`;

const multiLine = `Line one
Line two
Line three`;
```

### 19: What is the difference between let and var inside a for loop?

With `var` there is one variable shared by every iteration. With `let` each iteration gets its own copy.

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i));
}
// 3, 3, 3

for (let j = 0; j < 3; j++) {
  setTimeout(() => console.log(j));
}
// 0, 1, 2
```

### 20: What is an object in JavaScript?

An object is a collection of key-value pairs. Keys are strings or symbols, and values can be anything, including other objects and functions.

```js
const user = {
  name: "Ann",
  age: 25,
  greet() {
    return `Hi, I'm ${this.name}`;
  },
};

console.log(user.name); // "Ann"
console.log(user["age"]); // 25
console.log(user.greet()); // "Hi, I'm Ann"
```

### 21: What are the different ways to create an object?

```js
// Object literal
const a = { x: 1 };

// Object constructor
const b = new Object();
b.x = 1;

// Object.create (sets the prototype)
const c = Object.create(null);

// Constructor function
function Person(name) {
  this.name = name;
}
const d = new Person("Ann");

// Class
class Car {
  constructor(brand) {
    this.brand = brand;
  }
}
const e = new Car("Toyota");

// From entries
const f = Object.fromEntries([
  ["x", 1],
  ["y", 2],
]);
```

### 22: What is the difference between dot notation and bracket notation?

Both are used to read or write object properties.

Dot notation is shorter, but the key must be a valid identifier. Bracket notation accepts any string, a variable, or a symbol.

```js
const user = { name: "Ann", "first-name": "Ann" };

user.name; // "Ann"
user["first-name"]; // "Ann"

const key = "name";
user[key]; // "Ann"
user.key; // undefined (looks for a property called "key")
```

### 23: How do you check if an object has a property?

There are a few ways:

```js
const user = { name: "Ann" };

"name" in user; // true (also checks prototype chain)
Object.hasOwn(user, "name"); // true (only own properties)
user.hasOwnProperty("name"); // true (older way)
user.name !== undefined; // true, but fails if value is undefined
```

`Object.hasOwn()` is the recommended modern way. It also works for objects created with `Object.create(null)`, which do not have `hasOwnProperty`.

### 24: How do you loop over an object?

```js
const user = { name: "Ann", age: 25 };

for (const key in user) {
  console.log(key, user[key]);
}

Object.keys(user); // ["name", "age"]
Object.values(user); // ["Ann", 25]
Object.entries(user); // [["name", "Ann"], ["age", 25]]

for (const [key, value] of Object.entries(user)) {
  console.log(key, value);
}
```

Note that `for...in` also goes over inherited enumerable properties. `Object.keys/values/entries` only return own properties.

### 25: How do you delete a property from an object?

Use the `delete` operator.

```js
const user = { name: "Ann", age: 25 };
delete user.age;
console.log(user); // { name: "Ann" }
```

If you don't want to change the original object, use rest destructuring:

```js
const { age, ...rest } = { name: "Ann", age: 25 };
console.log(rest); // { name: "Ann" }
```

### 26: What is an array?

An array is an ordered list of values. Values can be of any type, and the array can grow or shrink.

```js
const fruits = ["apple", "banana", "cherry"];

fruits[0]; // "apple"
fruits.length; // 3
fruits.at(-1); // "cherry"
fruits.push("kiwi");
```

In JavaScript arrays are objects with numeric keys and a special `length` property.

### 27: What is the difference between push, pop, shift and unshift?

- `push()` adds items to the end
- `pop()` removes the last item
- `unshift()` adds items to the start
- `shift()` removes the first item

```js
const arr = [2, 3];
arr.push(4); // [2, 3, 4]
arr.pop(); // [2, 3]
arr.unshift(1); // [1, 2, 3]
arr.shift(); // [2, 3]
```

All four change the original array. `push` and `unshift` return the new length. `pop` and `shift` return the removed item.

### 28: What is the difference between slice and splice?

`slice(start, end)` returns a new array with part of the original. It does not change the original.

`splice(start, deleteCount, ...items)` removes or adds items in place and changes the original array. It returns the removed items.

```js
const arr = [1, 2, 3, 4, 5];

arr.slice(1, 3); // [2, 3], arr is unchanged

const removed = arr.splice(1, 2, "a", "b");
console.log(removed); // [2, 3]
console.log(arr); // [1, "a", "b", 4, 5]
```

If you want splice behavior without changing the original, use `toSpliced()` (ES2023).

### 29: What does the map method do?

`map()` creates a new array by calling a function on every item of the original array.

```js
const numbers = [1, 2, 3];
const doubled = numbers.map((n) => n * 2);
console.log(doubled); // [2, 4, 6]
```

It does not change the original array. The callback gets three arguments: the item, the index and the array.

### 30: What does the filter method do?

`filter()` returns a new array with only the items for which the callback returns a truthy value.

```js
const numbers = [1, 2, 3, 4, 5, 6];
const even = numbers.filter((n) => n % 2 === 0);
console.log(even); // [2, 4, 6]
```

### 31: What does the reduce method do?

`reduce()` goes through the array and combines all items into a single value.

```js
const numbers = [1, 2, 3, 4];

const sum = numbers.reduce((total, n) => total + n, 0);
console.log(sum); // 10

const countByLength = ["a", "bb", "cc"].reduce((acc, word) => {
  acc[word.length] = (acc[word.length] ?? 0) + 1;
  return acc;
}, {});
// { 1: 1, 2: 2 }
```

The second argument is the starting value. If you leave it out, the first item is used and the loop starts from the second item. Calling `reduce` on an empty array without a starting value throws a TypeError.

### 32: What is the difference between forEach and map?

`forEach()` just runs a function for each item and returns `undefined`. `map()` returns a new array with the results.

```js
const nums = [1, 2, 3];

nums.forEach((n) => console.log(n)); // logs 1, 2, 3

const squares = nums.map((n) => n * n); // [1, 4, 9]
```

Use `map` when you need a new array. Use `forEach` when you only need side effects like logging. You cannot `break` out of `forEach`; use `for...of` if you need that.

### 33: What does the find method do?

`find()` returns the first item that matches the condition, or `undefined` if nothing matches. `findIndex()` returns the index instead (or `-1`).

```js
const users = [
  { id: 1, name: "Ann" },
  { id: 2, name: "Bob" },
];

users.find((u) => u.id === 2); // { id: 2, name: "Bob" }
users.findIndex((u) => u.id === 2); // 1
users.find((u) => u.id === 5); // undefined
```

There are also `findLast()` and `findLastIndex()` that search from the end.

### 34: What is the difference between includes and indexOf?

Both check if a value is in an array (or string). `includes()` returns a boolean, `indexOf()` returns the index or `-1`.

```js
const arr = [1, 2, NaN];

arr.includes(2); // true
arr.indexOf(2); // 1

arr.includes(NaN); // true
arr.indexOf(NaN); // -1
```

`includes` can find `NaN`, while `indexOf` cannot, because `indexOf` uses `===`.

### 35: What do some and every do?

`some()` returns `true` if at least one item passes the test. `every()` returns `true` if all items pass.

```js
const ages = [12, 18, 25];

ages.some((age) => age >= 18); // true
ages.every((age) => age >= 18); // false
```

Both stop as soon as they know the answer. On an empty array, `some` returns `false` and `every` returns `true`.

### 36: How do you sort an array?

Use `sort()`. By default it converts items to strings and sorts them alphabetically, which gives wrong results for numbers. Pass a compare function to fix that.

```js
[10, 1, 5, 100].sort(); // [1, 10, 100, 5]
[10, 1, 5, 100].sort((a, b) => a - b); // [1, 5, 10, 100]
[10, 1, 5, 100].sort((a, b) => b - a); // [100, 10, 5, 1]
```

`sort()` changes the original array. If you want a sorted copy, use `toSorted()`:

```js
const nums = [3, 1, 2];
const sorted = nums.toSorted((a, b) => a - b);
console.log(nums); // [3, 1, 2]
console.log(sorted); // [1, 2, 3]
```

### 37: How do you join an array into a string and split a string into an array?

```js
["a", "b", "c"].join("-"); // "a-b-c"
["a", "b", "c"].join(); // "a,b,c"

"a-b-c".split("-"); // ["a", "b", "c"]
"hello".split(""); // ["h", "e", "l", "l", "o"]
```

For strings with emoji or other special characters, `[..."text"]` or `Array.from("text")` is safer than `split("")`, because they split by code points.

### 38: How do you get the last item of an array?

```js
const arr = [10, 20, 30];

arr[arr.length - 1]; // 30
arr.at(-1); // 30
```

`at()` accepts negative numbers and counts from the end. It also works on strings and typed arrays.

### 39: What is the spread operator?

The spread operator `...` expands an array, string or object into separate items.

```js
const a = [1, 2];
const b = [...a, 3, 4]; // [1, 2, 3, 4]

const obj1 = { x: 1 };
const obj2 = { ...obj1, y: 2 }; // { x: 1, y: 2 }

Math.max(...[5, 9, 2]); // 9

const chars = [..."hi"]; // ["h", "i"]
```

It makes a shallow copy. Nested objects are still shared.

### 40: What are rest parameters?

Rest parameters collect the remaining arguments of a function into an array.

```js
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3); // 6

function log(level, ...messages) {
  console.log(level, messages);
}

log("info", "a", "b"); // "info" ["a", "b"]
```

The rest parameter must be the last one. Spread and rest look the same (`...`), but spread expands values, while rest collects them.

### 41: What is destructuring?

Destructuring lets you pull values out of arrays or objects into variables.

```js
// Array destructuring
const [first, second, ...others] = [1, 2, 3, 4];
// first = 1, second = 2, others = [3, 4]

// Object destructuring
const { name, age } = { name: "Ann", age: 25 };

// Rename and default value
const { name: userName, role = "user" } = { name: "Bob" };
// userName = "Bob", role = "user"

// Swap variables
let x = 1,
  y = 2;
[x, y] = [y, x];
```

### 42: What are default parameters?

Default parameters let you set a value for a parameter when the argument is `undefined` or missing.

```js
function greet(name = "guest") {
  return `Hello, ${name}`;
}

greet(); // "Hello, guest"
greet("Ann"); // "Hello, Ann"
greet(undefined); // "Hello, guest"
greet(null); // "Hello, null"
```

Note that `null` does not trigger the default, only `undefined` does.

### 43: What are truthy and falsy values?

When a value is used in a boolean context (like an `if`), it is converted to `true` or `false`.

Falsy values are:

- `false`
- `0`, `-0`, `0n`
- `""` (empty string)
- `null`
- `undefined`
- `NaN`

Everything else is truthy, including `"0"`, `"false"`, `[]`, `{}` and functions.

```js
if ([]) console.log("empty array is truthy"); // runs
if ("") console.log("never runs");
```

### 44: What does the !! operator do?

`!!` converts a value to a boolean. The first `!` converts it to the opposite boolean, and the second `!` flips it back.

```js
!!"hello"; // true
!!""; // false
!!0; // false
!!{}; // true
```

It does the same thing as `Boolean(value)`.

### 45: What is the ternary operator?

It is a short way to write an if/else that returns a value.

```js
const age = 20;
const status = age >= 18 ? "adult" : "minor";
```

Format: `condition ? valueIfTrue : valueIfFalse`. You can chain them, but more than two levels becomes hard to read.

### 46: What is the nullish coalescing operator (??)?

`??` returns the right side only when the left side is `null` or `undefined`.

```js
const count = 0;

count || 10; // 10 (0 is falsy)
count ?? 10; // 0  (0 is not null/undefined)

null ?? "default"; // "default"
undefined ?? "default"; // "default"
"" ?? "default"; // ""
```

Use `??` when `0`, `""` or `false` are valid values that you want to keep.

### 47: What is optional chaining (?.)?

Optional chaining lets you read a nested property without crashing when something in the middle is `null` or `undefined`. It returns `undefined` instead.

```js
const user = { profile: null };

user.profile.name; // TypeError
user.profile?.name; // undefined

user.getName?.(); // undefined, method does not exist
const arr = null;
arr?.[0]; // undefined
```

### 48: What are logical assignment operators?

They combine a logical operator with assignment.

```js
let a = null;
a ??= 5; // a = 5 (assign if null/undefined)

let b = 0;
b ||= 10; // b = 10 (assign if falsy)

let c = 1;
c &&= 2; // c = 2 (assign if truthy)
```

`x ??= y` is the same as `x ?? (x = y)`. The assignment only happens when needed.

### 49: What is the difference between a for loop, for...in and for...of?

- `for` is the classic loop with a counter.
- `for...in` loops over the enumerable property keys of an object (including inherited ones).
- `for...of` loops over the values of an iterable (array, string, Map, Set, etc.).

```js
const arr = ["a", "b"];

for (let i = 0; i < arr.length; i++) console.log(arr[i]); // a, b
for (const key in arr) console.log(key); // "0", "1"
for (const value of arr) console.log(value); // a, b
```

Don't use `for...in` on arrays. Use `for...of` or array methods.

### 50: What is the difference between break and continue?

`break` stops the loop completely. `continue` skips the rest of the current iteration and goes to the next one.

```js
for (let i = 0; i < 5; i++) {
  if (i === 1) continue;
  if (i === 3) break;
  console.log(i);
}
// 0, 2
```

### 51: What is a switch statement?

`switch` compares a value against several `case` values using strict equality (`===`) and runs the matching block.

```js
const day = "sat";

switch (day) {
  case "sat":
  case "sun":
    console.log("Weekend");
    break;
  case "mon":
    console.log("Start of week");
    break;
  default:
    console.log("Weekday");
}
```

Without `break`, execution "falls through" to the next case. This is sometimes used on purpose, like with `"sat"` and `"sun"` above.

### 52: What is the difference between while and do...while?

`while` checks the condition before each run, so it may run zero times. `do...while` checks after, so it runs at least once.

```js
let i = 5;

while (i < 3) {
  console.log("while", i); // never runs
}

do {
  console.log("do...while", i); // runs once
} while (i < 3);
```

### 53: What is a string in JavaScript and are strings mutable?

A string is a sequence of UTF-16 code units used to store text. Strings are immutable. Methods like `toUpperCase()` return a new string and never change the original.

```js
let str = "hello";
str[0] = "H";
console.log(str); // "hello"

str = str.toUpperCase();
console.log(str); // "HELLO"
```

### 54: What are some common string methods?

```js
const s = "  Hello World  ";

s.length; // 15
s.trim(); // "Hello World"
s.trimStart(); // "Hello World  "
s.toUpperCase(); // "  HELLO WORLD  "
s.includes("World"); // true
s.startsWith("  He"); // true
s.endsWith("  "); // true
s.indexOf("o"); // 6
s.slice(2, 7); // "Hello"
s.replace("World", "JS"); // "  Hello JS  "
s.replaceAll("l", "L"); // "  HeLLo WorLd  "
s.split(" "); // ["", "", "Hello", "World", "", ""]
"ab".repeat(3); // "ababab"
"5".padStart(3, "0"); // "005"
"abc".at(-1); // "c"
```

### 55: What is the difference between substring, substr and slice?

- `slice(start, end)` accepts negative numbers (counted from the end).
- `substring(start, end)` treats negative numbers as 0 and swaps the arguments if start is bigger than end.
- `substr(start, length)` is deprecated. Don't use it in new code.

```js
const s = "JavaScript";

s.slice(0, 4); // "Java"
s.slice(-6); // "Script"
s.substring(4, 0); // "Java"
s.substring(-3); // "JavaScript"
```

### 56: How do you convert a string to a number?

```js
Number("42"); // 42
Number("42px"); // NaN
parseInt("42px"); // 42
parseInt("101", 2); // 5 (binary)
parseFloat("3.14m"); // 3.14
+"42"; // 42
Number(""); // 0
Number(" 12 "); // 12
```

`Number()` and unary `+` need the whole string to be a valid number. `parseInt` and `parseFloat` read as much as they can from the start. Always pass a radix to `parseInt`.

### 57: How do you convert a number to a string?

```js
const n = 255;

String(n); // "255"
n.toString(); // "255"
n.toString(16); // "ff"
n.toString(2); // "11111111"
`${n}`; // "255"
(3.14159).toFixed(2); // "3.14"
```

### 58: What is type coercion?

Type coercion is when JavaScript converts a value from one type to another automatically.

```js
"5" + 1; // "51" (number becomes string)
"5" - 1; // 4    (string becomes number)
"5" * "2"; // 10
true + 1; // 2
[] + []; // ""
[] + {}; // "[object Object]"
null + 1; // 1
undefined + 1; // NaN
```

The `+` operator prefers strings: if one side is a string, it joins them. The other math operators convert both sides to numbers.

### 59: What is the difference between implicit and explicit type conversion?

Explicit conversion is when you convert the value yourself. Implicit conversion (coercion) is when JavaScript does it for you.

```js
// Explicit
Number("10");
String(10);
Boolean(0);

// Implicit
"10" * 1; // 10
10 + ""; // "10"
if ("text") {
} // converted to true
```

Explicit conversion makes the code easier to understand.

### 60: What is scope in JavaScript?

Scope decides where a variable can be accessed. JavaScript has:

- **Global scope**: available everywhere.
- **Module scope**: top-level variables in an ES module are only visible in that module.
- **Function scope**: variables declared inside a function.
- **Block scope**: variables declared with `let` or `const` inside `{ }`.

```js
const globalVar = "global";

function test() {
  const fnVar = "function";
  if (true) {
    const blockVar = "block";
    console.log(globalVar, fnVar, blockVar); // all work
  }
  console.log(blockVar); // ReferenceError
}
```

### 61: What is hoisting?

Hoisting means that declarations are processed before the code runs, so it looks like they were moved to the top of their scope.

- Function declarations are fully hoisted (you can call them early).
- `var` is hoisted and set to `undefined`.
- `let`, `const` and `class` are hoisted but stay uninitialized until their line runs (temporal dead zone).

```js
console.log(a); // undefined
var a = 5;

hello(); // "hi"
function hello() {
  console.log("hi");
}

console.log(b); // ReferenceError
let b = 10;
```

### 62: What is the temporal dead zone (TDZ)?

The TDZ is the time between entering a scope and the line where a `let`, `const` or `class` is declared. Accessing the variable during this time throws a `ReferenceError`.

```js
{
  // TDZ for "name" starts here
  console.log(name); // ReferenceError
  const name = "Ann"; // TDZ ends here
  console.log(name); // "Ann"
}
```

### 63: What is a callback function?

A callback is a function passed to another function, to be called later.

```js
function fetchData(callback) {
  setTimeout(() => {
    callback("data loaded");
  }, 1000);
}

fetchData((result) => console.log(result));

[1, 2, 3].forEach((n) => console.log(n)); // also a callback
```

### 64: What is the DOM?

The DOM (Document Object Model) is a tree of objects that represents the HTML page. The browser builds it from the HTML, and JavaScript can use it to read and change the page.

```js
const title = document.querySelector("h1");
title.textContent = "New title";
title.classList.add("active");
```

The DOM is a browser API, not part of the JavaScript language.

### 65: How do you select elements in the DOM?

```js
document.getElementById("main");
document.querySelector(".card"); // first match
document.querySelectorAll(".card"); // all matches (static NodeList)
document.getElementsByClassName("card"); // live HTMLCollection
document.getElementsByTagName("p"); // live HTMLCollection
```

`querySelector` and `querySelectorAll` accept any CSS selector and are the most common choice today.

### 66: How do you create and add an element to the page?

```js
const li = document.createElement("li");
li.textContent = "New item";
li.className = "item";

const list = document.querySelector("ul");
list.append(li); // add at the end
list.prepend(li); // add at the start
list.before(li); // before the list
li.remove(); // remove it
```

`append` and `prepend` can take several nodes or strings at once.

### 67: What is the difference between innerHTML, textContent and innerText?

- `innerHTML` reads or sets the HTML inside an element. Setting it with user input is a security risk (XSS).
- `textContent` reads or sets plain text, including hidden elements. It is fast and safe.
- `innerText` returns only the visible text and is affected by CSS. It is slower because it needs layout information.

```js
el.innerHTML = "<b>Bold</b>"; // renders bold text
el.textContent = "<b>Bold</b>"; // shows the tags as text
```

### 68: How do you add an event listener?

```js
const button = document.querySelector("button");

function handleClick(event) {
  console.log("Clicked", event.target);
}

button.addEventListener("click", handleClick);

// Remove it later
button.removeEventListener("click", handleClick);

// Run only once
button.addEventListener("click", handleClick, { once: true });
```

To remove a listener you must pass the same function reference that was added.

### 69: What is the event object?

When an event happens, the listener receives an event object with information about it.

```js
document.addEventListener("click", (event) => {
  console.log(event.type); // "click"
  console.log(event.target); // element that was clicked
  console.log(event.currentTarget); // element the listener is on
  console.log(event.clientX, event.clientY);
});
```

### 70: What does preventDefault do?

`event.preventDefault()` stops the browser's default action for that event, like submitting a form or following a link.

```js
form.addEventListener("submit", (event) => {
  event.preventDefault();
  // handle form with JavaScript instead
});
```

It does not stop the event from bubbling. For that you use `stopPropagation()`.

### 71: What is the difference between alert, confirm and prompt?

They are browser dialog functions.

```js
alert("Saved!"); // shows a message
const ok = confirm("Delete this item?"); // returns true or false
const name = prompt("Your name?", ""); // returns string or null
```

They block the page until the user responds, so they are rarely used in real apps.

### 72: What is console.log and what other console methods exist?

`console.log` prints values to the developer console. Other useful methods:

```js
console.error("Something failed");
console.warn("Be careful");
console.info("Info");
console.table([{ a: 1 }, { a: 2 }]);
console.group("Group");
console.log("inside group");
console.groupEnd();
console.time("loop");
// ... code ...
console.timeEnd("loop");
console.count("clicks");
console.assert(1 === 2, "Not equal");
```

### 73: What is the difference between setTimeout and setInterval?

`setTimeout` runs a function once after a delay. `setInterval` runs it again and again with a delay between runs.

```js
const t = setTimeout(() => console.log("once"), 1000);
clearTimeout(t);

const i = setInterval(() => console.log("every second"), 1000);
clearInterval(i);
```

The delay is a minimum, not an exact time. The callback runs only when the call stack is empty.

### 74: What does setTimeout with 0 delay do?

It runs the callback as soon as possible, but only after the current code and all microtasks (like resolved promises) finish.

```js
console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// 1, 4, 3, 2
```

### 75: What is JSON?

JSON (JavaScript Object Notation) is a text format for storing and sending data. It looks like JavaScript objects but has stricter rules: keys must be in double quotes, and it cannot contain functions, `undefined`, comments or trailing commas.

```json
{
  "name": "Ann",
  "age": 25,
  "skills": ["js", "css"],
  "active": true,
  "manager": null
}
```

### 76: How do you convert between JSON and JavaScript objects?

```js
const user = { name: "Ann", age: 25 };

const json = JSON.stringify(user);
// '{"name":"Ann","age":25}'

const pretty = JSON.stringify(user, null, 2); // indented output

const parsed = JSON.parse(json);
// { name: "Ann", age: 25 }
```

`JSON.stringify` skips functions, `undefined` and symbols in objects. It throws on `BigInt` and on circular references. `JSON.parse` throws a `SyntaxError` on invalid JSON.

### 77: What is the Math object?

`Math` is a built-in object with math constants and functions.

```js
Math.PI; // 3.141592653589793
Math.round(4.5); // 5
Math.floor(4.9); // 4
Math.ceil(4.1); // 5
Math.trunc(-4.9); // -4
Math.abs(-7); // 7
Math.max(1, 5, 3); // 5
Math.min(1, 5, 3); // 1
Math.pow(2, 3); // 8 (same as 2 ** 3)
Math.sqrt(16); // 4
Math.random(); // number from 0 (inclusive) to 1 (exclusive)
```

### 78: How do you generate a random integer in a range?

```js
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

randomInt(1, 6); // 1 to 6, like a dice
```

`Math.random()` is not secure. For tokens or passwords use `crypto.getRandomValues()` or `crypto.randomUUID()`.

### 79: What is the exponentiation operator?

`**` raises a number to a power. It does the same thing as `Math.pow()`.

```js
2 ** 3; // 8
2 ** -1; // 0.5
(-2) ** 2; // 4

let x = 3;
x **= 2; // 9
```

You need parentheses for a negative base: `-2 ** 2` is a SyntaxError.

### 80: What is the modulo (%) operator?

`%` returns the remainder of a division.

```js
10 % 3; // 1
10 % 2; // 0
-10 % 3; // -1 (sign follows the left side)
```

A common use is checking if a number is even: `n % 2 === 0`.

### 81: What is the difference between i++ and ++i?

Both add 1 to `i`. `i++` returns the old value, `++i` returns the new value.

```js
let i = 5;
console.log(i++); // 5, i is now 6
console.log(++i); // 7, i is now 7
```

### 82: What is a Date object and how do you use it?

`Date` stores a point in time as milliseconds since January 1, 1970 UTC.

```js
const now = new Date();
const d = new Date("2025-03-15T10:30:00Z");
const d2 = new Date(2025, 2, 15); // months start from 0, so 2 is March

d.getFullYear(); // 2025
d.getMonth(); // 2
d.getDate(); // 15
d.getDay(); // day of week, 0 is Sunday
d.toISOString(); // "2025-03-15T10:30:00.000Z"
Date.now(); // current timestamp in ms
```

`Date` has many known problems (mutable, confusing month numbers, weak time zone support). The newer `Temporal` API fixes these and is now shipping in modern browsers.

### 83: How do you format a date for display?

Use `toLocaleDateString` or `Intl.DateTimeFormat`.

```js
const d = new Date("2025-03-15");

d.toLocaleDateString("en-US"); // "3/15/2025"
d.toLocaleDateString("de-DE"); // "15.3.2025"

new Intl.DateTimeFormat("en-GB", {
  dateStyle: "long",
}).format(d); // "15 March 2025"
```

### 84: What are comments in JavaScript?

```js
// single-line comment

/*
  multi-line
  comment
*/

/**
 * JSDoc comment, used to describe functions and types
 * @param {number} a
 * @returns {number}
 */
function double(a) {
  return a * 2;
}
```

### 85: What is "use strict"?

`"use strict"` turns on strict mode. Strict mode makes some silent errors throw, and blocks some unsafe features.

```js
"use strict";

x = 10; // ReferenceError: x is not defined
delete Object.prototype; // TypeError
function f(a, a) {} // SyntaxError
```

Other changes: `this` is `undefined` in plain function calls instead of the global object, and `with` is not allowed.

ES modules and class bodies are always in strict mode, so you don't need to write it there.

### 86: What is the global object?

The global object holds global variables and built-ins. Its name depends on the environment:

- Browser: `window` (or `self` in workers)
- Node.js: `global`

`globalThis` works in all environments.

```js
globalThis.setTimeout === setTimeout; // true
```

### 87: What is the difference between an argument and a parameter?

Parameters are the names in the function definition. Arguments are the actual values passed when you call it.

```js
function add(a, b) {
  // a and b are parameters
  return a + b;
}

add(2, 3); // 2 and 3 are arguments
```

### 88: What happens if you call a function with fewer or more arguments than parameters?

Missing parameters become `undefined`. Extra arguments are ignored, but you can still access them with rest parameters or `arguments`.

```js
function show(a, b) {
  console.log(a, b);
}

show(1); // 1 undefined
show(1, 2, 3); // 1 2
```

### 89: What does a function return if there is no return statement?

It returns `undefined`.

```js
function noReturn() {
  const x = 1;
}

console.log(noReturn()); // undefined
```

Be careful: if you put a value on the line after `return`, automatic semicolon insertion makes the function return `undefined`.

```js
function bad() {
  return;
  {
    ok: true;
  }
}
bad(); // undefined
```

### 90: What is the arguments object?

`arguments` is an array-like object available inside regular functions (not arrow functions). It holds all the arguments passed.

```js
function show() {
  console.log(arguments.length);
  console.log(arguments[0]);
}

show("a", "b"); // 2, "a"
```

It is not a real array, so it has no `map` or `filter`. In modern code use rest parameters (`...args`) instead.

### 91: What is an IIFE?

An IIFE (Immediately Invoked Function Expression) is a function that runs right after it is defined.

```js
(function () {
  const secret = "hidden";
  console.log("runs now");
})();

(() => {
  console.log("arrow IIFE");
})();
```

It was used a lot to create a private scope before `let`, `const` and modules existed. Today modules usually replace it.

### 92: What is a method?

A method is a function stored as a property of an object.

```js
const counter = {
  count: 0,
  increment() {
    this.count++;
  },
};

counter.increment();
console.log(counter.count); // 1
```

### 93: What is the "this" keyword (basic idea)?

`this` refers to the object that is calling the function. Its value depends on how the function is called, not where it is written.

```js
const user = {
  name: "Ann",
  sayName() {
    console.log(this.name);
  },
};

user.sayName(); // "Ann"

const fn = user.sayName;
fn(); // undefined (this is lost)
```

Arrow functions don't have their own `this`. They use the `this` from where they were created.

### 94: What is an array-like object?

It is an object that has numeric keys and a `length` property, but is not a real array. Examples are `arguments`, `NodeList` and strings.

```js
const arrayLike = { 0: "a", 1: "b", length: 2 };

Array.from(arrayLike); // ["a", "b"]
Array.prototype.map.call(arrayLike, (x) => x.toUpperCase()); // ["A", "B"]
```

### 95: How do you copy an array?

```js
const arr = [1, 2, 3];

const a = [...arr];
const b = arr.slice();
const c = Array.from(arr);
const d = structuredClone(arr); // deep copy
```

The first three create shallow copies. If the array contains objects, the objects are shared. Use `structuredClone` for a deep copy.

### 96: How do you merge two arrays?

```js
const a = [1, 2];
const b = [3, 4];

const merged = [...a, ...b]; // [1, 2, 3, 4]
const merged2 = a.concat(b); // [1, 2, 3, 4]
```

Both return a new array. `push(...b)` adds to `a` in place.

### 97: How do you remove duplicates from an array?

```js
const nums = [1, 2, 2, 3, 3, 3];

const unique = [...new Set(nums)]; // [1, 2, 3]

const unique2 = nums.filter((n, i) => nums.indexOf(n) === i);
```

For arrays of objects, you can use a `Map` keyed by an id:

```js
const users = [{ id: 1 }, { id: 1 }, { id: 2 }];
const uniqueUsers = [...new Map(users.map((u) => [u.id, u])).values()];
```

### 98: How do you check if a string contains another string?

```js
const text = "I love JavaScript";

text.includes("Java"); // true
text.indexOf("Java") !== -1; // true
/java/i.test(text); // true (case-insensitive)
text.toLowerCase().includes("java"); // true
```

### 99: How do you reverse a string?

```js
const str = "hello";

str.split("").reverse().join(""); // "olleh"
[...str].reverse().join(""); // "olleh"
[...str].toReversed().join(""); // "olleh"
```

`[...str]` handles most emoji better than `split("")`.

### 100: What is the difference between let x; and let x = null;?

`let x;` leaves the variable `undefined`, meaning it has not been given a value. `let x = null;` gives it an empty value on purpose.

```js
let a;
let b = null;

typeof a; // "undefined"
typeof b; // "object"
```

A common convention: let JavaScript use `undefined`, and use `null` yourself when you want to say "no value".

### 101: What is a Promise (basic idea)?

A Promise is an object that represents a value that will be available later, usually from an async operation like a network request.

A promise has three states:

- `pending`: still waiting
- `fulfilled`: finished with a value
- `rejected`: failed with an error

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("done"), 1000);
});

promise
  .then((value) => console.log(value))
  .catch((error) => console.error(error))
  .finally(() => console.log("finished"));
```

### 102: What are async and await?

`async` and `await` let you write promise-based code that looks like normal step-by-step code.

- An `async` function always returns a promise.
- `await` pauses the async function until the promise settles, then gives you the value.

```js
async function loadUser() {
  try {
    const response = await fetch("/api/user");
    const user = await response.json();
    console.log(user);
  } catch (error) {
    console.error("Failed:", error);
  }
}
```

### 103: How do you make an HTTP request in JavaScript?

The standard way is the `fetch` API. It is available in browsers, Node.js 18+, Deno and Bun.

```js
// GET
const res = await fetch("https://api.example.com/users");
if (!res.ok) throw new Error(`HTTP ${res.status}`);
const users = await res.json();

// POST
await fetch("https://api.example.com/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Ann" }),
});
```

`fetch` only rejects on network errors. A 404 or 500 response does not reject, so you need to check `res.ok`.

### 104: What is try...catch...finally?

It is used to handle errors.

```js
try {
  JSON.parse("invalid json");
} catch (error) {
  console.log("Error:", error.message);
} finally {
  console.log("always runs");
}
```

- `try` holds code that might throw.
- `catch` runs if an error is thrown.
- `finally` runs no matter what.

Since ES2019 you can leave out the error variable: `catch { ... }`.

### 105: How do you throw an error?

Use `throw`. You can throw any value, but it is best to throw an `Error` object because it includes a stack trace.

```js
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

try {
  divide(1, 0);
} catch (e) {
  console.log(e.message); // "Cannot divide by zero"
}
```

### 106: What are the built-in error types?

- `Error`: the base type
- `SyntaxError`: invalid code or invalid JSON
- `ReferenceError`: using a variable that does not exist
- `TypeError`: wrong type, like calling something that is not a function
- `RangeError`: value out of range, like `new Array(-1)`
- `URIError`: bad use of `decodeURI` and similar functions
- `EvalError`: kept for compatibility
- `AggregateError`: holds several errors, used by `Promise.any`

```js
null.foo; // TypeError
undefinedVariable; // ReferenceError
new Array(-1); // RangeError
```

### 107: What is the difference between a SyntaxError and a runtime error?

A `SyntaxError` happens when the code is parsed, before it runs. The whole script fails to start. A runtime error (like `TypeError`) happens while the code is running, and only stops the code at that point.

```js
// SyntaxError: nothing in this file runs
const x = ;

// Runtime error: code before this line already ran
const obj = null;
obj.name; // TypeError
```

### 108: What is a Set?

A `Set` is a collection of unique values. It keeps insertion order.

```js
const set = new Set([1, 2, 2, 3]);

set.add(4);
set.has(2); // true
set.delete(1);
set.size; // 3

for (const value of set) {
  console.log(value);
}
```

### 109: What is a Map?

A `Map` is a collection of key-value pairs where keys can be any type, including objects. It keeps insertion order and has a `size` property.

```js
const map = new Map();

map.set("name", "Ann");
map.set(42, "number key");
const objKey = {};
map.set(objKey, "object key");

map.get("name"); // "Ann"
map.has(42); // true
map.size; // 3
map.delete(42);

for (const [key, value] of map) {
  console.log(key, value);
}
```

### 110: What is the difference between a Map and an object?

|              | Object                                              | Map                            |
| ------------ | --------------------------------------------------- | ------------------------------ |
| Key types    | strings and symbols                                 | any value                      |
| Size         | `Object.keys(obj).length`                           | `map.size`                     |
| Order        | mostly insertion order, but integer keys come first | always insertion order         |
| Default keys | has prototype keys                                  | none                           |
| Iteration    | needs `Object.entries`                              | iterable directly              |
| JSON support | yes                                                 | no, needs conversion           |
| Performance  | good for fixed shape records                        | better for frequent add/remove |

Use objects for structured records and Maps for dynamic collections or non-string keys.

### 111: What is a Symbol?

A `Symbol` is a primitive value that is always unique. It is often used as an object key that won't clash with other keys.

```js
const id = Symbol("id");
const id2 = Symbol("id");

id === id2; // false

const user = { name: "Ann", [id]: 123 };
user[id]; // 123
Object.keys(user); // ["name"] (symbols are skipped)
```

`Symbol.for("key")` returns a shared symbol from a global registry.

### 112: What is BigInt?

`BigInt` is a type for integers of any size. Normal numbers are only accurate up to `Number.MAX_SAFE_INTEGER` (2^53 - 1).

```js
const big = 9007199254740993n;
const big2 = BigInt("9007199254740993");

big + 1n; // 9007199254740994n
10n / 3n; // 3n (no decimals)

10n + 1; // TypeError: cannot mix BigInt and Number
typeof 10n; // "bigint"
```

### 113: What is Number.MAX_SAFE_INTEGER?

It is the largest integer that can be safely stored in a JavaScript number: `9007199254740991` (2^53 - 1). Above this, numbers lose precision.

```js
Number.MAX_SAFE_INTEGER; // 9007199254740991
9007199254740992 === 9007199254740993; // true
Number.isSafeInteger(2 ** 53); // false
```

### 114: Why does 0.1 + 0.2 not equal 0.3?

JavaScript numbers use 64-bit binary floating point (IEEE 754). Some decimal numbers like 0.1 can't be stored exactly in binary, so small rounding errors appear.

```js
0.1 + 0.2; // 0.30000000000000004
0.1 + 0.2 === 0.3; // false

Math.abs(0.1 + 0.2 - 0.3) < Number.EPSILON; // true
```

For money, store values in cents as integers, or use a decimal library.

### 115: What is Infinity?

`Infinity` is a number value larger than any other number. You get it from dividing by zero or from overflow.

```js
1 / 0; // Infinity
-1 / 0; // -Infinity
Number.MAX_VALUE * 2; // Infinity
Number.isFinite(Infinity); // false
```

### 116: How do you check if a value is an integer?

```js
Number.isInteger(5); // true
Number.isInteger(5.0); // true
Number.isInteger(5.5); // false
Number.isInteger("5"); // false
```

### 117: What is the difference between Number.isFinite and the global isFinite?

The global `isFinite` converts the value to a number first. `Number.isFinite` does not.

```js
isFinite("42"); // true
Number.isFinite("42"); // false
Number.isFinite(42); // true
```

### 118: How do you format numbers for display?

```js
const n = 1234567.891;

n.toFixed(2); // "1234567.89"
n.toLocaleString("en-US"); // "1,234,567.891"

new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
}).format(n); // "$1,234,567.89"

new Intl.NumberFormat("en", { notation: "compact" }).format(n); // "1.2M"
```

### 119: What are labels in JavaScript?

A label names a loop so you can `break` or `continue` an outer loop from an inner one.

```js
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (j === 1) continue outer;
    if (i === 2) break outer;
    console.log(i, j);
  }
}
// 0 0
// 1 0
```

They are rarely used, but good to know.

### 120: What is a class in JavaScript?

A class is a template for creating objects. It is syntax built on top of prototypes.

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hi, I'm ${this.name}`;
  }
}

const ann = new Person("Ann");
ann.greet(); // "Hi, I'm Ann"
```

### 121: What is a constructor?

A constructor is a special method that runs when you create an object with `new`. It sets up the initial state.

```js
class Car {
  constructor(brand, year) {
    this.brand = brand;
    this.year = year;
  }
}

const car = new Car("Toyota", 2024);
```

Before classes, regular functions were used as constructors:

```js
function Car(brand) {
  this.brand = brand;
}
const car2 = new Car("Honda");
```

### 122: What is inheritance with classes?

A class can extend another class using `extends`. It gets the parent's methods and can add or override them. `super` calls the parent.

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
    return `${this.name} barks`;
  }
}

new Dog("Rex").speak(); // "Rex barks"
```

### 123: What does super do?

`super` is used inside a class to call the parent class.

- `super(...)` calls the parent constructor. In a child constructor you must call it before using `this`.
- `super.method()` calls a parent method.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  describe() {
    return `Animal: ${this.name}`;
  }
}

class Cat extends Animal {
  constructor(name, color) {
    super(name);
    this.color = color;
  }
  describe() {
    return `${super.describe()}, color: ${this.color}`;
  }
}
```

### 124: What are static methods?

Static methods belong to the class itself, not to its instances.

```js
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

MathUtils.add(1, 2); // 3

const m = new MathUtils();
m.add; // undefined
```

Built-in examples are `Array.isArray`, `Object.keys` and `Promise.all`.

### 125: What are getters and setters?

Getters and setters let you run code when a property is read or written.

```js
class User {
  constructor(first, last) {
    this.first = first;
    this.last = last;
  }

  get fullName() {
    return `${this.first} ${this.last}`;
  }

  set fullName(value) {
    [this.first, this.last] = value.split(" ");
  }
}

const u = new User("Ann", "Lee");
u.fullName; // "Ann Lee"
u.fullName = "Bob Ray";
u.first; // "Bob"
```

### 126: What is the instanceof operator?

`instanceof` checks if an object has a constructor's prototype somewhere in its prototype chain.

```js
class Animal {}
class Dog extends Animal {}

const d = new Dog();

d instanceof Dog; // true
d instanceof Animal; // true
d instanceof Object; // true
[] instanceof Array; // true
```

### 127: What are ES modules?

ES modules are the standard way to split JavaScript into files. Each file has its own scope, and you share code with `export` and `import`.

```js
// math.js
export function add(a, b) {
  return a + b;
}
export const PI = 3.14;
export default function multiply(a, b) {
  return a * b;
}

// app.js
import multiply, { add, PI } from "./math.js";
```

In the browser you load them with `<script type="module">`.

### 128: What is the difference between named and default exports?

A module can have many named exports and only one default export.

```js
// named
export const a = 1;
import { a } from "./mod.js";
import { a as alias } from "./mod.js";

// default
export default function () {}
import anyName from "./mod.js";

// import everything
import * as mod from "./mod.js";
```

Named exports must be imported with the exact name (or renamed with `as`). The default export can be imported with any name.

### 129: What is localStorage?

`localStorage` is a browser API that stores string key-value pairs. The data stays even after the browser is closed.

```js
localStorage.setItem("theme", "dark");
localStorage.getItem("theme"); // "dark"
localStorage.removeItem("theme");
localStorage.clear();

// store objects as JSON
localStorage.setItem("user", JSON.stringify({ name: "Ann" }));
const user = JSON.parse(localStorage.getItem("user"));
```

It is synchronous, limited to about 5 MB per origin, and readable by any script on the page, so never store tokens or secrets there.

### 130: What is the difference between localStorage, sessionStorage and cookies?

|                | localStorage  | sessionStorage      | Cookies                 |
| -------------- | ------------- | ------------------- | ----------------------- |
| Lifetime       | until cleared | until tab is closed | set by expiry date      |
| Size           | ~5 MB         | ~5 MB               | ~4 KB each              |
| Sent to server | no            | no                  | yes, with every request |
| Scope          | origin        | origin and tab      | domain and path         |
| Access from JS | yes           | yes                 | yes, unless `HttpOnly`  |

### 131: What is event bubbling?

When an event happens on an element, it first runs on that element and then moves up to its parent, grandparent and so on up to `document`. This is called bubbling.

```html
<div id="parent">
  <button id="child">Click</button>
</div>
```

```js
parent.addEventListener("click", () => console.log("parent"));
child.addEventListener("click", () => console.log("child"));
// clicking the button logs: "child", then "parent"
```

### 132: How do you stop event bubbling?

Call `event.stopPropagation()`.

```js
child.addEventListener("click", (event) => {
  event.stopPropagation();
  console.log("child only");
});
```

`stopImmediatePropagation()` also stops other listeners on the same element.

### 133: What is the difference between == null and === null?

`value == null` is true for both `null` and `undefined`. `value === null` is true only for `null`.

```js
let a;
a == null; // true
a === null; // false
```

`x == null` is one of the few places where many developers accept `==`, because it is a short way to check for both.

### 134: What is the comma operator?

The comma operator runs each expression from left to right and returns the last one.

```js
const x = (1, 2, 3);
console.log(x); // 3

for (let i = 0, j = 10; i < j; i++, j--) {}
```

It is mostly seen in `for` loops and minified code.

### 135: What is the void operator?

`void` runs an expression and returns `undefined`.

```js
void 0; // undefined
void "hello"; // undefined
```

You may see `void 0` in older or minified code as a safe way to get `undefined`, or `href="javascript:void(0)"` in old HTML.

### 136: What is the difference between Object.keys and Object.entries?

`Object.keys` returns the own enumerable keys. `Object.entries` returns `[key, value]` pairs.

```js
const user = { name: "Ann", age: 25 };

Object.keys(user); // ["name", "age"]
Object.entries(user); // [["name", "Ann"], ["age", 25]]
```

### 137: How do you merge objects?

```js
const a = { x: 1, y: 2 };
const b = { y: 3, z: 4 };

const merged = { ...a, ...b }; // { x: 1, y: 3, z: 4 }
const merged2 = Object.assign({}, a, b);
```

When keys repeat, the later object wins. Both are shallow merges.

### 138: What is Object.freeze?

`Object.freeze` makes an object read-only. You can't add, remove or change its properties. It is shallow, so nested objects can still be changed.

```js
const config = Object.freeze({ port: 3000, db: { host: "x" } });

config.port = 4000; // ignored (TypeError in strict mode)
config.db.host = "y"; // works, nested object is not frozen
Object.isFrozen(config); // true
```

### 139: What is the difference between Object.freeze and Object.seal?

- `Object.freeze`: can't add, remove or change properties.
- `Object.seal`: can't add or remove properties, but can change existing values.
- `Object.preventExtensions`: can't add properties, but can remove and change.

```js
const sealed = Object.seal({ a: 1 });
sealed.a = 2; // works
sealed.b = 3; // ignored
delete sealed.a; // ignored
```

### 140: What is a pure function?

A pure function always returns the same result for the same inputs and has no side effects (it does not change anything outside of itself).

```js
// pure
function add(a, b) {
  return a + b;
}

// not pure: changes outside state
let total = 0;
function addToTotal(n) {
  total += n;
}

// not pure: result changes each call
function now() {
  return Date.now();
}
```

Pure functions are easy to test and reason about.

### 141: What is the difference between mutable and immutable operations on arrays?

Mutable methods change the original array. Immutable ones return a new array.

| Mutates                           | Returns new array    |
| --------------------------------- | -------------------- |
| `push`, `pop`, `shift`, `unshift` | `concat`, spread     |
| `sort`                            | `toSorted`           |
| `reverse`                         | `toReversed`         |
| `splice`                          | `toSpliced`, `slice` |
| `arr[i] = x`                      | `with(i, x)`         |
| `fill`, `copyWithin`              | `map`, `filter`      |

```js
const arr = [3, 1, 2];
const changed = arr.with(0, 9); // [9, 1, 2]
console.log(arr); // [3, 1, 2]
```

### 142: How do you fill an array with values?

```js
new Array(3).fill(0); // [0, 0, 0]
Array.from({ length: 3 }, (_, i) => i); // [0, 1, 2]
Array.from({ length: 3 }, () => []); // [[], [], []]
```

Be careful: `new Array(3).fill([])` puts the same array in every slot.

### 143: What does Array.from do?

`Array.from` creates a new array from an iterable or array-like object. It can take a map function as a second argument.

```js
Array.from("abc"); // ["a", "b", "c"]
Array.from(new Set([1, 2, 2])); // [1, 2]
Array.from({ length: 3 }, (_, i) => i * 2); // [0, 2, 4]
Array.from(document.querySelectorAll("p"));
```

### 144: What does Array.of do?

`Array.of` creates an array from its arguments. It fixes a problem with `new Array` when you pass a single number.

```js
new Array(3); // [ <3 empty items> ]
Array.of(3); // [3]
Array.of(1, 2); // [1, 2]
```

### 145: What does flat do?

`flat()` flattens nested arrays. The default depth is 1.

```js
[1, [2, [3, [4]]]].flat(); // [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat(2); // [1, 2, 3, [4]]
[1, [2, [3, [4]]]].flat(Infinity); // [1, 2, 3, 4]
```

`flatMap()` maps each item and then flattens one level:

```js
["a b", "c"].flatMap((s) => s.split(" ")); // ["a", "b", "c"]
```

### 146: How do you empty an array?

```js
let arr = [1, 2, 3];

arr.length = 0; // clears the array in place
arr.splice(0); // also in place
arr = []; // new empty array (other references keep the old one)
```

### 147: What is a NodeList and how is it different from an array?

A `NodeList` is what `querySelectorAll` returns. It looks like an array and has `forEach` and `length`, but it does not have `map`, `filter` and other array methods.

```js
const items = document.querySelectorAll("li");

items.forEach((li) => console.log(li.textContent)); // works
items.map; // undefined

const arr = [...items];
arr.map((li) => li.textContent);
```

### 148: What is the difference between an attribute and a property in the DOM?

Attributes are written in HTML. Properties are on the DOM object in JavaScript. They are often linked, but not always the same.

```html
<input id="name" value="Ann" />
```

```js
const input = document.getElementById("name");
input.value = "Bob";

input.value; // "Bob" (current property)
input.getAttribute("value"); // "Ann" (original attribute)
```

### 149: What are data attributes?

Data attributes let you store custom data on HTML elements. In JavaScript you read them with `dataset`.

```html
<button data-user-id="42" data-role="admin">Edit</button>
```

```js
const btn = document.querySelector("button");
btn.dataset.userId; // "42" (kebab-case becomes camelCase)
btn.dataset.role; // "admin"
btn.dataset.active = "true"; // adds data-active="true"
```

### 150: What are the main differences between JavaScript and TypeScript?

TypeScript is JavaScript with static types added. It is compiled (or stripped) to plain JavaScript before running.

- TypeScript catches type errors before the code runs.
- JavaScript checks types only while the code runs.
- Types do not exist at runtime.

```ts
function add(a: number, b: number): number {
  return a + b;
}

add(1, "2"); // compile-time error in TypeScript
```

Recent Node.js versions can run `.ts` files directly by removing type annotations, but they don't type-check them. You still use `tsc` for checking.

---

# Moderate Questions (151-300)

### 151: What is a closure?

A closure is a function that remembers the variables from the scope where it was created, even after that outer function has finished running.

```js
function makeCounter() {
  let count = 0;
  return function () {
    count++;
    return count;
  };
}

const counter = makeCounter();
counter(); // 1
counter(); // 2

const other = makeCounter();
other(); // 1 (separate count)
```

`count` can't be reached from outside, but the returned function still has access to it.

### 152: What are some practical uses of closures?

- Private state (counters, caches)
- Function factories
- Event handlers that remember data
- Memoization
- Debounce and throttle
- Partial application and currying

```js
function createGreeter(greeting) {
  return (name) => `${greeting}, ${name}!`;
}

const sayHello = createGreeter("Hello");
const sayHi = createGreeter("Hi");

sayHello("Ann"); // "Hello, Ann!"
sayHi("Bob"); // "Hi, Bob!"
```

### 153: What is lexical scope?

Lexical scope means a function's access to variables is decided by where the function is written in the code, not where it is called from.

```js
const name = "global";

function outer() {
  const name = "outer";
  function inner() {
    console.log(name);
  }
  return inner;
}

const fn = outer();
fn(); // "outer"
```

`inner` was written inside `outer`, so it sees `outer`'s `name`, no matter where it's called.

### 154: What is the scope chain?

When you use a variable, JavaScript looks for it in the current scope. If it's not there, it looks in the outer scope, then the next outer one, until it reaches the global scope. If it is not found anywhere, you get a `ReferenceError`. This lookup path is the scope chain.

```js
const a = 1;
function first() {
  const b = 2;
  function second() {
    const c = 3;
    console.log(a + b + c); // 6, finds a and b in outer scopes
  }
  second();
}
first();
```

### 155: How does "this" work in different situations?

The value of `this` depends on how the function is called.

```js
// 1. Method call: this is the object before the dot
const obj = {
  name: "Ann",
  show() {
    return this.name;
  },
};
obj.show(); // "Ann"

// 2. Plain function call: undefined in strict mode, globalThis otherwise
function plain() {
  return this;
}
plain(); // undefined (in strict mode / modules)

// 3. With new: this is the new object
function User(name) {
  this.name = name;
}
new User("Bob");

// 4. call, apply, bind: this is set explicitly
plain.call({ x: 1 }); // { x: 1 }

// 5. Arrow function: uses this from the surrounding scope
const obj2 = {
  name: "Cid",
  show() {
    return [1].map(() => this.name);
  },
};
obj2.show(); // ["Cid"]

// 6. Event listener (regular function): this is the element
button.addEventListener("click", function () {
  console.log(this); // button
});
```

### 156: What is the difference between call, apply and bind?

All three set `this` for a function.

- `call(thisArg, a, b)` calls the function now with arguments one by one.
- `apply(thisArg, [a, b])` calls the function now with arguments as an array.
- `bind(thisArg, a, b)` returns a new function with `this` fixed. It does not call it.

```js
function intro(greeting, punctuation) {
  return `${greeting}, I'm ${this.name}${punctuation}`;
}

const user = { name: "Ann" };

intro.call(user, "Hi", "!"); // "Hi, I'm Ann!"
intro.apply(user, ["Hello", "."]); // "Hello, I'm Ann."

const bound = intro.bind(user, "Hey");
bound("?"); // "Hey, I'm Ann?"
```

### 157: Why do you lose "this" when passing a method as a callback?

When you pass `obj.method` somewhere, you only pass the function. The connection to `obj` is lost, so when it's called later as a plain function, `this` is `undefined`.

```js
class Timer {
  seconds = 0;
  tick() {
    this.seconds++;
  }
}

const t = new Timer();
setTimeout(t.tick, 1000); // TypeError: Cannot read properties of undefined
```

Fixes:

```js
setTimeout(() => t.tick(), 1000);
setTimeout(t.tick.bind(t), 1000);

// or define it as an arrow function class field
class Timer2 {
  seconds = 0;
  tick = () => {
    this.seconds++;
  };
}
```

### 158: Can you change "this" in an arrow function using call or bind?

No. Arrow functions take `this` from the surrounding scope when they are created. `call`, `apply` and `bind` can pass arguments, but they ignore the `this` argument.

```js
const arrow = () => this;
arrow.call({ x: 1 }); // still the outer this, not { x: 1 }
```

### 159: When should you not use an arrow function?

- As object methods that need `this` to be the object.
- As constructors (they can't be used with `new`).
- As event handlers when you need `this` to be the element.
- When you need the `arguments` object.
- As prototype methods.

```js
const user = {
  name: "Ann",
  greet: () => `Hi ${this.name}`, // this is not user
};
user.greet(); // "Hi undefined"
```

### 160: What is a prototype?

Every JavaScript object has a hidden link to another object called its prototype. When you read a property that the object doesn't have, JavaScript looks at the prototype, then the prototype's prototype, and so on.

```js
const animal = {
  eats: true,
};

const dog = Object.create(animal);
dog.barks = true;

dog.barks; // true (own property)
dog.eats; // true (from prototype)
Object.getPrototypeOf(dog) === animal; // true
```

This is how methods like `[].map` work. `map` lives on `Array.prototype`, not on each array.

### 161: What is the prototype chain?

The prototype chain is the series of linked prototypes that JavaScript walks through when looking up a property. It ends at `null`.

```js
const arr = [];

Object.getPrototypeOf(arr) === Array.prototype; // true
Object.getPrototypeOf(Array.prototype) === Object.prototype; // true
Object.getPrototypeOf(Object.prototype); // null
```

So `arr.toString` comes from `Array.prototype`, and `arr.hasOwnProperty` comes from `Object.prototype`.

### 162: What is the difference between `__proto__` and prototype?

- `prototype` is a property of constructor functions and classes. It is the object that will become the prototype of instances created with `new`.
- `__proto__` is an old accessor on objects that points to the object's actual prototype. It is deprecated. Use `Object.getPrototypeOf` and `Object.setPrototypeOf` instead.

```js
function User() {}
const u = new User();

User.prototype; // object used as prototype
Object.getPrototypeOf(u) === User.prototype; // true
u.__proto__ === User.prototype; // true, but avoid __proto__
```

### 163: How do classes relate to prototypes?

Classes are mostly a nicer syntax over prototypes. Methods defined in a class go on `ClassName.prototype`.

```js
class User {
  constructor(name) {
    this.name = name;
  }
  hi() {
    return "hi";
  }
}

typeof User; // "function"
User.prototype.hi; // function
Object.hasOwn(new User("a"), "hi"); // false
```

There are some differences from plain constructor functions: classes must be called with `new`, their code is always strict, they are not hoisted in a usable way, and they support private fields and `static` blocks.

### 164: What does the new keyword do?

When you call a function with `new`, JavaScript:

1. Creates a new empty object.
2. Sets its prototype to the function's `prototype` property.
3. Calls the function with `this` set to the new object.
4. Returns the new object, unless the function returns another object.

```js
function myNew(Constructor, ...args) {
  const obj = Object.create(Constructor.prototype);
  const result = Constructor.apply(obj, args);
  return result !== null && typeof result === "object" ? result : obj;
}
```

### 165: What is Object.create used for?

`Object.create(proto)` creates a new object with the given prototype. You can pass `null` to create an object with no prototype at all.

```js
const base = {
  greet() {
    return "hi";
  },
};
const obj = Object.create(base);
obj.greet(); // "hi"

const dict = Object.create(null);
dict.toString; // undefined, no inherited keys
```

Objects with a `null` prototype are useful as plain dictionaries because they have no inherited keys like `constructor` or `toString`.

### 166: What are private class fields and methods?

Fields and methods that start with `#` are private. They can only be used inside the class body.

```js
class BankAccount {
  #balance = 0;

  deposit(amount) {
    this.#validate(amount);
    this.#balance += amount;
  }

  #validate(amount) {
    if (amount <= 0) throw new Error("Invalid amount");
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

Unlike the old `_name` convention, these are really private and enforced by the language.

### 167: How do you check if an object has a private field?

Use `#field in obj`. It returns `true` if the object was created by the class that defines that private field.

```js
class User {
  #id;
  static isUser(obj) {
    return #id in obj;
  }
}

User.isUser(new User()); // true
User.isUser({}); // false
```

This is safer than `instanceof`, which can be faked by changing prototypes.

### 168: What are class fields?

Class fields let you declare instance properties directly in the class body instead of inside the constructor.

```js
class Counter {
  count = 0;
  step = 1;
  static instances = 0;

  increment() {
    this.count += this.step;
  }
}
```

Fields are created on each instance when it is constructed, before the constructor body runs (in a subclass, right after `super()` returns).

### 169: What is a static initialization block?

A `static { }` block runs once when the class is defined. It is used for setup logic that is more than a single assignment.

```js
class Config {
  static settings;

  static {
    const env = globalThis.process?.env?.NODE_ENV ?? "development";
    Config.settings = { env, debug: env !== "production" };
  }
}
```

Code in a static block can also access private static fields.

### 170: What is the event loop?

JavaScript runs on a single thread, so it can only do one thing at a time. The event loop is what lets it handle async work.

Simple version of how it works:

1. Run all synchronous code on the call stack.
2. When the stack is empty, run all microtasks (promise callbacks, `queueMicrotask`).
3. Run one macrotask (timer callback, I/O, events).
4. In browsers, render if needed.
5. Repeat.

```js
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
// A, D, C, B
```

### 171: What is the difference between microtasks and macrotasks?

Microtasks have higher priority. After each macrotask, the whole microtask queue is emptied before moving on.

- Microtasks: `.then/.catch/.finally` callbacks, code after `await`, `queueMicrotask`, `MutationObserver`.
- Macrotasks (tasks): `setTimeout`, `setInterval`, I/O, UI events, `MessageChannel`.

```js
setTimeout(() => console.log("timeout"), 0);

queueMicrotask(() => console.log("micro 1"));
Promise.resolve().then(() => {
  console.log("micro 2");
  queueMicrotask(() => console.log("micro 3"));
});
// micro 1, micro 2, micro 3, timeout
```

If microtasks keep adding more microtasks forever, timers and rendering never get a chance to run.

### 172: What is the call stack?

The call stack keeps track of which function is running. When a function is called, it is pushed onto the stack. When it returns, it is popped off.

```js
function a() {
  b();
}
function b() {
  c();
}
function c() {
  console.trace();
}
a();
// stack: c -> b -> a -> (global)
```

If functions keep calling themselves without stopping, the stack gets too big and you get `RangeError: Maximum call stack size exceeded`.

### 173: What is promise chaining?

Each `.then()` returns a new promise, so you can chain them. Whatever you return from a `.then` becomes the value for the next one. If you return a promise, the chain waits for it.

```js
fetch("/api/user")
  .then((res) => res.json())
  .then((user) => fetch(`/api/posts?user=${user.id}`))
  .then((res) => res.json())
  .then((posts) => console.log(posts))
  .catch((err) => console.error(err));
```

A common mistake is forgetting to `return` inside `.then`, which breaks the chain.

### 174: What is the difference between Promise.all, Promise.allSettled, Promise.race and Promise.any?

| Method               | Resolves when                                  | Rejects when                  |
| -------------------- | ---------------------------------------------- | ----------------------------- |
| `Promise.all`        | all fulfill (array of values)                  | any one rejects               |
| `Promise.allSettled` | all settle (array of `{status, value/reason}`) | never                         |
| `Promise.race`       | first one settles (fulfills)                   | first one settles (rejects)   |
| `Promise.any`        | first one fulfills                             | all reject (`AggregateError`) |

```js
const p1 = Promise.resolve(1);
const p2 = Promise.reject(new Error("fail"));
const p3 = new Promise((r) => setTimeout(() => r(3), 100));

await Promise.all([p1, p3]); // [1, 3]
await Promise.allSettled([p1, p2]);
// [{ status: "fulfilled", value: 1 }, { status: "rejected", reason: Error }]
await Promise.race([p1, p3]); // 1
await Promise.any([p2, p3]); // 3
```

### 175: How do you run async operations in parallel vs one after another?

Awaiting inside a loop runs them one by one. To run them at the same time, start them all and use `Promise.all`.

```js
const ids = [1, 2, 3];

// Sequential: slow, total time = sum of all requests
for (const id of ids) {
  const user = await getUser(id);
}

// Parallel: total time = slowest request
const users = await Promise.all(ids.map((id) => getUser(id)));
```

Use sequential when each step depends on the previous one, or when you need to limit load on a server.

### 176: How do you handle errors with async/await?

Use `try...catch` around the `await`, or attach `.catch()` to the promise.

```js
async function load() {
  try {
    const res = await fetch("/api/data");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (error) {
    console.error("Load failed:", error);
    return null;
  }
}

// or
const data = await fetch("/api/data").catch(() => null);
```

Note the `return await` inside `try`. Without `await`, a rejected promise would skip the `catch` block.

### 177: What happens if you don't handle a rejected promise?

You get an "unhandled promise rejection". In browsers, it shows an error in the console and fires the `unhandledrejection` event. In Node.js (version 15 and later), the process crashes by default.

```js
Promise.reject(new Error("oops")); // unhandled

window.addEventListener("unhandledrejection", (event) => {
  console.log("Unhandled:", event.reason);
});

process.on("unhandledRejection", (reason) => {
  console.log("Unhandled:", reason);
});
```

### 178: What does an async function return?

It always returns a promise. If you return a value, the promise fulfills with it. If you throw, the promise rejects.

```js
async function a() {
  return 5;
}
a(); // Promise { 5 }

async function b() {
  throw new Error("fail");
}
b().catch((e) => console.log(e.message)); // "fail"
```

### 179: Can you use await outside of an async function?

Yes, at the top level of an ES module. This is called top-level await.

```js
// config.mjs
const res = await fetch("/config.json");
export const config = await res.json();
```

Modules that import this one will wait until it finishes. It does not work in classic scripts or in CommonJS files.

### 180: How do you create a sleep or delay function?

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function run() {
  console.log("start");
  await sleep(1000);
  console.log("one second later");
}
```

In Node.js you can also use `import { setTimeout } from "node:timers/promises"`.

### 181: What is Promise.withResolvers?

`Promise.withResolvers()` (ES2024) creates a promise and gives you its `resolve` and `reject` functions, so you don't have to grab them inside the constructor.

```js
// old way
let resolve, reject;
const promise = new Promise((res, rej) => {
  resolve = res;
  reject = rej;
});

// new way
const { promise: p, resolve: done, reject: fail } = Promise.withResolvers();

button.addEventListener("click", () => done("clicked"), { once: true });
await p;
```

### 182: What is Promise.try?

`Promise.try(fn)` (ES2025) calls a function and always gives you a promise back. If the function throws synchronously, you get a rejected promise instead of an exception.

```js
function maybeSync(id) {
  if (!id) throw new Error("No id");
  return fetch(`/api/${id}`);
}

Promise.try(() => maybeSync(null))
  .then((res) => console.log(res))
  .catch((err) => console.log("caught:", err.message)); // "caught: No id"
```

This means you can handle sync and async errors in one `.catch`.

### 183: How do you convert a callback-based function into a promise?

Wrap it in `new Promise`. In Node.js you can also use `util.promisify`.

```js
function readFileAsync(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

// Node.js
import { promisify } from "node:util";
const readFile = promisify(fs.readFile);

// or just use the built-in promise API
import { readFile as rf } from "node:fs/promises";
```

### 184: What is callback hell and how do you avoid it?

Callback hell is deeply nested callbacks that are hard to read and handle errors in.

```js
getUser(id, (err, user) => {
  getPosts(user.id, (err, posts) => {
    getComments(posts[0].id, (err, comments) => {
      // ...
    });
  });
});
```

You avoid it with promises and `async/await`:

```js
const user = await getUser(id);
const posts = await getPosts(user.id);
const comments = await getComments(posts[0].id);
```

### 185: What is debouncing?

Debouncing delays a function until some time has passed without it being called again. It is useful for search inputs and window resize.

```js
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const onSearch = debounce((e) => {
  console.log("Search for:", e.target.value);
}, 300);

input.addEventListener("input", onSearch);
```

### 186: What is throttling?

Throttling makes sure a function runs at most once in a given time period, no matter how many times it is triggered. It is useful for scroll and mousemove events.

```js
function throttle(fn, limit) {
  let waiting = false;
  return function (...args) {
    if (waiting) return;
    fn.apply(this, args);
    waiting = true;
    setTimeout(() => {
      waiting = false;
    }, limit);
  };
}

window.addEventListener(
  "scroll",
  throttle(() => {
    console.log("scrolling");
  }, 200),
);
```

Debounce waits until the calls stop. Throttle runs at a steady rate while the calls continue.

### 187: What is a higher-order function?

A higher-order function either takes a function as an argument, returns a function, or both.

```js
// takes a function
[1, 2, 3].map((n) => n * 2);

// returns a function
function multiplier(factor) {
  return (n) => n * factor;
}
const triple = multiplier(3);
triple(5); // 15
```

### 188: What is currying?

Currying turns a function with many arguments into a chain of functions that each take one argument.

```js
// normal
const add = (a, b, c) => a + b + c;

// curried
const curriedAdd = (a) => (b) => (c) => a + b + c;
curriedAdd(1)(2)(3); // 6

// generic curry helper
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    }
    return (...next) => curried.apply(this, [...args, ...next]);
  };
}

const c = curry(add);
c(1)(2)(3); // 6
c(1, 2)(3); // 6
```

### 189: What is partial application?

Partial application means fixing some arguments of a function and getting back a new function that takes the rest.

```js
function log(level, message) {
  console.log(`[${level}] ${message}`);
}

const error = log.bind(null, "ERROR");
error("Disk full"); // [ERROR] Disk full

const partial =
  (fn, ...preset) =>
  (...rest) =>
    fn(...preset, ...rest);
const warn = partial(log, "WARN");
warn("Low memory");
```

The difference from currying: currying always produces one-argument functions, partial application can fix any number of arguments at once.

### 190: What is memoization?

Memoization caches the result of a function call so the same input doesn't need to be computed again.

```js
function memoize(fn) {
  const cache = new Map();
  return function (arg) {
    if (cache.has(arg)) return cache.get(arg);
    const result = fn(arg);
    cache.set(arg, result);
    return result;
  };
}

const slowSquare = (n) => {
  // pretend this is expensive
  return n * n;
};

const fastSquare = memoize(slowSquare);
fastSquare(9); // computed
fastSquare(9); // from cache
```

It only makes sense for pure functions.

### 191: What is function composition?

Composition means combining small functions so the output of one becomes the input of the next.

```js
const compose =
  (...fns) =>
  (x) =>
    fns.reduceRight((acc, fn) => fn(acc), x);
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);

const trim = (s) => s.trim();
const lower = (s) => s.toLowerCase();
const exclaim = (s) => `${s}!`;

const shout = pipe(trim, lower, exclaim);
shout("  HELLO "); // "hello!"
```

`compose` runs right-to-left, `pipe` runs left-to-right.

### 192: What is recursion?

Recursion is when a function calls itself. Every recursive function needs a base case that stops it.

```js
function factorial(n) {
  if (n <= 1) return 1; // base case
  return n * factorial(n - 1); // recursive case
}

factorial(5); // 120

function sumNested(arr) {
  return arr.reduce(
    (total, item) => total + (Array.isArray(item) ? sumNested(item) : item),
    0,
  );
}

sumNested([1, [2, [3, 4]]]); // 10
```

Very deep recursion can overflow the call stack. JavaScript engines (except Safari) do not do tail call optimization, so for very deep data a loop is safer.

### 193: What is the difference between a shallow copy and a deep copy?

A shallow copy copies only the top level. Nested objects are still shared. A deep copy copies everything, so nothing is shared.

```js
const original = { name: "Ann", address: { city: "Paris" } };

const shallow = { ...original };
shallow.address.city = "Rome";
original.address.city; // "Rome" (shared)

const deep = structuredClone(original);
deep.address.city = "Oslo";
original.address.city; // "Rome" (not affected)
```

### 194: What is structuredClone?

`structuredClone()` is a built-in function that makes a deep copy. It is available in browsers and Node.js 17+.

```js
const data = {
  date: new Date(),
  set: new Set([1, 2]),
  map: new Map([["a", 1]]),
  nested: { list: [1, 2, 3] },
};
data.self = data; // circular reference

const copy = structuredClone(data);
copy.date instanceof Date; // true
copy.self === copy; // true
```

It supports Dates, Maps, Sets, typed arrays, circular references and more. It does not support functions, DOM nodes, or class prototypes (class instances become plain objects).

### 195: Why is JSON.parse(JSON.stringify(obj)) not a good deep copy?

It works only for simple data. It has many problems:

- `Date` becomes a string
- `Map`, `Set` become `{}`
- `undefined`, functions and symbols are removed
- `NaN` and `Infinity` become `null`
- circular references throw
- `BigInt` throws

```js
const obj = { d: new Date(), u: undefined, n: NaN };
JSON.parse(JSON.stringify(obj));
// { d: "2025-...", n: null }
```

Use `structuredClone` instead.

### 196: What is event delegation?

Event delegation means adding one listener to a parent element instead of one to each child. It works because events bubble up.

```js
const list = document.querySelector("#todo-list");

list.addEventListener("click", (event) => {
  const item = event.target.closest("li");
  if (!item || !list.contains(item)) return;
  console.log("Clicked:", item.dataset.id);
});
```

Benefits: fewer listeners, and it works for items added later.

### 197: What are the three phases of event propagation?

1. **Capturing phase**: the event goes from `window` down to the target.
2. **Target phase**: the event reaches the target element.
3. **Bubbling phase**: the event goes back up to `window`.

By default listeners run in the bubbling phase. Pass `{ capture: true }` to run in the capturing phase.

```js
parent.addEventListener("click", () => console.log("capture"), {
  capture: true,
});
parent.addEventListener("click", () => console.log("bubble"));
child.addEventListener("click", () => console.log("target"));
// click on child: capture, target, bubble
```

Some events like `focus` and `blur` do not bubble. `focusin` and `focusout` do.

### 198: What is the difference between event.target and event.currentTarget?

- `event.target` is the element where the event started (what was actually clicked).
- `event.currentTarget` is the element the listener is attached to.

```js
ul.addEventListener("click", (e) => {
  e.target; // the <li> that was clicked
  e.currentTarget; // the <ul>
});
```

### 199: How do you create and dispatch a custom event?

```js
const event = new CustomEvent("user:login", {
  detail: { userId: 42 },
  bubbles: true,
});

document.addEventListener("user:login", (e) => {
  console.log("Logged in:", e.detail.userId);
});

document.body.dispatchEvent(event);
```

You can also extend `EventTarget` to make your own event-emitting classes, even outside the DOM.

```js
class Store extends EventTarget {
  update(data) {
    this.dispatchEvent(new CustomEvent("change", { detail: data }));
  }
}
```

### 200: What are passive event listeners?

A passive listener tells the browser it will never call `preventDefault()`. The browser can then scroll right away without waiting for the listener, which makes scrolling smoother.

```js
window.addEventListener("touchstart", onTouch, { passive: true });
```

Browsers already treat `touchstart`, `touchmove` and `wheel` listeners on `window`, `document` and `body` as passive by default.

### 201: What is the difference between DOMContentLoaded and load?

- `DOMContentLoaded` fires when the HTML is fully parsed and the DOM is built. It does not wait for images, stylesheets or iframes.
- `load` fires when the whole page is loaded, including all images and other resources.

```js
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM ready");
});

window.addEventListener("load", () => {
  console.log("Everything loaded");
});
```

### 202: What is the difference between async and defer on script tags?

- Normal `<script>`: stops HTML parsing, downloads and runs the script, then continues.
- `async`: downloads in parallel and runs as soon as it's ready. Order between scripts is not guaranteed.
- `defer`: downloads in parallel and runs after the HTML is parsed, in the order the scripts appear.

```html
<script src="analytics.js" async></script>
<script src="app.js" defer></script>
<script type="module" src="main.js"></script>
<!-- deferred by default -->
```

Use `defer` (or `type="module"`) for app code. Use `async` for independent scripts like analytics.

### 203: What is a generator function?

A generator function (`function*`) can pause with `yield` and continue later. Calling it returns an iterator.

```js
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const ids = idGenerator();
ids.next().value; // 1
ids.next().value; // 2
ids.next().value; // 3

function* range(start, end) {
  for (let i = start; i < end; i++) yield i;
}

[...range(0, 5)]; // [0, 1, 2, 3, 4]
```

### 204: What are iterables and iterators?

- An **iterator** is an object with a `next()` method that returns `{ value, done }`.
- An **iterable** is an object with a `[Symbol.iterator]()` method that returns an iterator.

Arrays, strings, Maps, Sets and NodeLists are iterables. They work with `for...of`, spread and destructuring.

```js
const range = {
  from: 1,
  to: 3,
  [Symbol.iterator]() {
    let current = this.from;
    const last = this.to;
    return {
      next() {
        return current <= last
          ? { value: current++, done: false }
          : { value: undefined, done: true };
      },
    };
  },
};

for (const n of range) console.log(n); // 1, 2, 3
[...range]; // [1, 2, 3]
```

### 205: How do you make an object iterable with a generator?

It's simpler to write `[Symbol.iterator]` as a generator method.

```js
class Playlist {
  #songs = [];
  add(song) {
    this.#songs.push(song);
    return this;
  }
  *[Symbol.iterator]() {
    yield* this.#songs;
  }
}

const list = new Playlist().add("A").add("B");
for (const song of list) console.log(song); // A, B
```

`yield*` hands off to another iterable.

### 206: What are iterator helpers?

Iterator helpers (ES2025) add methods like `map`, `filter`, `take`, `drop`, `flatMap`, `reduce`, `toArray`, `forEach`, `some`, `every` and `find` directly to iterators. They are lazy, so they process one value at a time and don't build intermediate arrays.

```js
function* naturals() {
  let n = 1;
  while (true) yield n++;
}

const result = naturals()
  .filter((n) => n % 2 === 0)
  .map((n) => n * n)
  .take(3)
  .toArray();

console.log(result); // [4, 16, 36]

// works on Map and Set iterators too
const map = new Map([
  ["a", 1],
  ["b", 2],
]);
map
  .values()
  .map((v) => v * 10)
  .toArray(); // [10, 20]
```

`Iterator.from(obj)` wraps any iterable or iterator-like object so you can use these methods.

### 207: What are the new Set methods?

ES2025 added set operations to `Set.prototype`:

```js
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

a.union(b); // Set {1, 2, 3, 4}
a.intersection(b); // Set {2, 3}
a.difference(b); // Set {1}
a.symmetricDifference(b); // Set {1, 4}

a.isSubsetOf(new Set([1, 2, 3, 4])); // true
a.isSupersetOf(new Set([1, 2])); // true
a.isDisjointFrom(new Set([7, 8])); // true
```

They return new Sets and don't change the originals. The argument can be any set-like object (something with `size`, `has` and `keys`), like a `Map`.

### 208: What are Object.groupBy and Map.groupBy?

They (ES2024) group items of an iterable by a key returned from a callback.

```js
const people = [
  { name: "Ann", age: 17 },
  { name: "Bob", age: 25 },
  { name: "Cid", age: 30 },
];

const byGroup = Object.groupBy(people, (p) =>
  p.age >= 18 ? "adult" : "minor",
);
// { minor: [{ name: "Ann", ... }], adult: [{ Bob }, { Cid }] }

const byAgeBucket = Map.groupBy(people, (p) => Math.floor(p.age / 10) * 10);
// Map { 10 => [Ann], 20 => [Bob], 30 => [Cid] }
```

`Object.groupBy` returns a null-prototype object with string keys. `Map.groupBy` returns a Map and can use any value (like objects) as keys.

### 209: What are toSorted, toReversed, toSpliced and with?

They are non-mutating versions of existing array methods (ES2023). They return a new array and leave the original unchanged.

```js
const nums = [3, 1, 2];

nums.toSorted(); // [1, 2, 3]
nums.toReversed(); // [2, 1, 3]
nums.toSpliced(0, 1); // [1, 2]
nums.with(1, 99); // [3, 99, 2]

console.log(nums); // [3, 1, 2]
```

They are very useful in React and other places where you must not mutate state.

### 210: What are findLast and findLastIndex?

They work like `find` and `findIndex`, but search from the end of the array.

```js
const logs = [
  { level: "info", msg: "a" },
  { level: "error", msg: "b" },
  { level: "error", msg: "c" },
];

logs.findLast((l) => l.level === "error"); // { level: "error", msg: "c" }
logs.findLastIndex((l) => l.level === "error"); // 2
```

### 211: What is Array.fromAsync?

`Array.fromAsync` is like `Array.from`, but works with async iterables and promises. It returns a promise of an array.

```js
async function* fetchPages() {
  yield "page 1";
  yield "page 2";
}

const pages = await Array.fromAsync(fetchPages());
// ["page 1", "page 2"]

const values = await Array.fromAsync([Promise.resolve(1), 2]);
// [1, 2]
```

### 212: What is for await...of?

`for await...of` loops over async iterables, waiting for each value. It also works with an array of promises.

```js
async function* countdown(n) {
  while (n > 0) {
    await new Promise((r) => setTimeout(r, 500));
    yield n--;
  }
}

for await (const n of countdown(3)) {
  console.log(n); // 3, 2, 1 with a delay
}

// Reading a stream in chunks
const res = await fetch("/big-file");
for await (const chunk of res.body) {
  console.log(chunk.length);
}
```

Async iteration of `ReadableStream` works in Node.js, Deno, Firefox and Chrome. Check support before relying on it in all browsers.

### 213: What is an async generator?

An async generator (`async function*`) can both `await` and `yield`. It returns an async iterator.

```js
async function* paginate(url) {
  let next = url;
  while (next) {
    const res = await fetch(next);
    const data = await res.json();
    yield data.items;
    next = data.nextPage;
  }
}

for await (const items of paginate("/api/items")) {
  console.log(items);
}
```

### 214: What is a WeakMap?

A `WeakMap` is like a `Map`, but keys must be objects (or non-registered symbols), and the keys are held weakly. If nothing else refers to a key object, it can be garbage collected along with its value.

```js
const metadata = new WeakMap();

function track(element) {
  metadata.set(element, { clicks: 0 });
}

let el = document.createElement("div");
track(el);
el = null; // the entry can now be cleaned up
```

WeakMaps are not iterable and have no `size`, because entries can disappear at any time. They are good for attaching private data to objects without causing memory leaks.

### 215: What is a WeakSet?

A `WeakSet` stores objects weakly. It only has `add`, `has` and `delete`.

```js
const visited = new WeakSet();

function visit(node) {
  if (visited.has(node)) return;
  visited.add(node);
  // ...
}
```

It is useful for marking objects (like "already processed") without keeping them alive.

### 216: What is the difference between Map and WeakMap?

|                  | Map      | WeakMap                            |
| ---------------- | -------- | ---------------------------------- |
| Key types        | anything | objects and non-registered symbols |
| Keeps keys alive | yes      | no                                 |
| Iterable         | yes      | no                                 |
| `size`           | yes      | no                                 |
| `clear()`        | yes      | no                                 |

Use `WeakMap` for caches or metadata tied to an object's lifetime.

### 217: What is a tagged template literal?

A tagged template is a template literal with a function name in front. The function receives the string parts and the values separately.

```js
function highlight(strings, ...values) {
  return strings.reduce(
    (result, str, i) =>
      result + str + (i < values.length ? `<b>${values[i]}</b>` : ""),
    "",
  );
}

const name = "Ann";
const age = 25;
highlight`Name: ${name}, age: ${age}`;
// "Name: <b>Ann</b>, age: <b>25</b>"
```

Libraries use this for things like CSS-in-JS, GraphQL queries, and safe SQL queries.

### 218: What is String.raw?

`String.raw` is a built-in tag that returns the string without processing escape sequences.

```js
String.raw`C:\new\folder`; // "C:\\new\\folder" (backslashes kept)
`C:\new\folder`; // "C:" + newline + "ew" + form feed + "older"
```

It is handy for Windows paths and regular expressions.

### 219: What is a regular expression and how do you create one?

A regular expression (regex) is a pattern used to match text.

```js
const re1 = /hello/i; // literal
const re2 = new RegExp("hello", "i"); // constructor (useful for dynamic patterns)

re1.test("Hello world"); // true
"Hello world".match(/o/g); // ["o", "o"]
"2025-03-15".replace(/-/g, "/"); // "2025/03/15"
```

Common flags:

- `g`: global, find all matches
- `i`: case-insensitive
- `m`: multiline, `^` and `$` match at line breaks
- `s`: dotAll, `.` matches newlines
- `u`: unicode
- `v`: unicode sets (newer, more features than `u`)
- `y`: sticky, match only at `lastIndex`
- `d`: include start and end indices of matches

### 220: What are named capture groups?

Named groups let you name parts of a match with `(?<name>...)` and read them from `match.groups`.

```js
const re = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const { year, month, day } = "2025-03-15".match(re).groups;
// year = "2025", month = "03", day = "15"

"2025-03-15".replace(re, "$<day>/$<month>/$<year>"); // "15/03/2025"
```

Since ES2025, the same group name can be used in different alternatives: `/(?<y>\d{4})-\d{2}|\d{2}\/(?<y>\d{4})/`.

### 221: What is the difference between match and matchAll?

With the `g` flag, `match` returns only the matched strings. `matchAll` returns an iterator of full match objects, including groups and indices.

```js
const text = "a1 b2 c3";
const re = /(?<letter>[a-z])(?<digit>\d)/g;

text.match(re); // ["a1", "b2", "c3"]

for (const m of text.matchAll(re)) {
  console.log(m.groups.letter, m.groups.digit, m.index);
}
// a 1 0
// b 2 3
// c 3 6
```

`matchAll` requires the `g` flag, otherwise it throws.

### 222: What are lookahead and lookbehind in regex?

They check if something is (or isn't) before or after the match, without including it in the match.

```js
// Positive lookahead: digits followed by "px"
"10px 20em".match(/\d+(?=px)/g); // ["10"]

// Negative lookahead: digits not followed by "px"
"10px 20em".match(/\d+(?!px|\d)/g); // ["20"]

// Positive lookbehind: digits after "$"
"$30 and 40".match(/(?<=\$)\d+/g); // ["30"]

// Negative lookbehind: digits not after "$"
"$30 and 40".match(/(?<!\$|\d)\d+/g); // ["40"]
```

### 223: What is RegExp.escape?

`RegExp.escape` (ES2025) escapes special regex characters in a string, so you can safely put user input into a regex.

```js
const userInput = "1.5+2";

new RegExp(userInput); // . and + are treated as regex syntax
new RegExp(RegExp.escape(userInput)); // matches the literal text "1.5+2"

"Price: 1.5+2".replace(new RegExp(RegExp.escape(userInput), "g"), "X");
// "Price: X"
```

Before this, everyone wrote their own escape function, and many of them had bugs.

### 224: What is Object.defineProperty?

It adds or changes a property with fine control over its behavior through a property descriptor.

```js
const user = {};

Object.defineProperty(user, "id", {
  value: 1,
  writable: false, // can't change value
  enumerable: false, // hidden from Object.keys and for...in
  configurable: false, // can't delete or redefine
});

user.id = 2; // ignored (TypeError in strict mode)
Object.keys(user); // []
```

When you use `defineProperty`, flags you don't set default to `false`. With normal assignment they are all `true`.

### 225: What are property descriptors?

A property descriptor describes how a property behaves. There are two kinds:

- **Data descriptor**: `value`, `writable`, `enumerable`, `configurable`
- **Accessor descriptor**: `get`, `set`, `enumerable`, `configurable`

```js
const obj = { a: 1 };
Object.getOwnPropertyDescriptor(obj, "a");
// { value: 1, writable: true, enumerable: true, configurable: true }

Object.defineProperty(obj, "double", {
  get() {
    return this.a * 2;
  },
  enumerable: true,
});
obj.double; // 2
```

### 226: What is the difference between enumerable and non-enumerable properties?

Enumerable properties appear in `for...in`, `Object.keys`, `Object.entries`, spread and `JSON.stringify`. Non-enumerable ones don't, but can still be accessed directly.

```js
const arr = [1, 2];
Object.keys(arr); // ["0", "1"] (length is non-enumerable)
Object.getOwnPropertyNames(arr); // ["0", "1", "length"]
```

Built-in methods like `Array.prototype.map` are non-enumerable, which is why they don't show up in `for...in`.

### 227: What is Object.is?

`Object.is` compares two values like `===`, but handles two special cases differently.

```js
NaN === NaN; // false
Object.is(NaN, NaN); // true

0 === -0; // true
Object.is(0, -0); // false

Object.is("a", "a"); // true
```

React uses `Object.is` to check if state has changed.

### 228: How do you compare two objects or arrays for equality?

`===` only checks if both sides are the same reference.

```js
[1, 2] === [1, 2]; // false
const a = [1, 2];
a === a; // true
```

To compare contents you need a deep equality function:

```js
function deepEqual(a, b) {
  if (Object.is(a, b)) return true;
  if (
    typeof a !== "object" ||
    typeof b !== "object" ||
    a === null ||
    b === null
  ) {
    return false;
  }
  if (Array.isArray(a) !== Array.isArray(b)) return false;

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;

  return keysA.every(
    (key) => Object.hasOwn(b, key) && deepEqual(a[key], b[key]),
  );
}

deepEqual({ x: [1, 2] }, { x: [1, 2] }); // true
```

In Node.js you can use `util.isDeepStrictEqual`. In tests, use `expect(a).toEqual(b)`.

### 229: What is short-circuit evaluation?

`&&` and `||` stop as soon as they know the result and return the last value they checked (not always a boolean).

```js
true || anything(); // anything() is not called
false && anything(); // anything() is not called

"a" || "b"; // "a"
"" || "b"; // "b"
"a" && "b"; // "b"
0 && "b"; // 0

isLoggedIn && showDashboard(); // run only if logged in
```

### 230: What is an Error cause?

Since ES2022, you can pass a `cause` when creating an error. This lets you wrap a low-level error with a clearer message without losing the original.

```js
async function loadConfig() {
  try {
    return JSON.parse(await readFile("config.json", "utf8"));
  } catch (err) {
    throw new Error("Could not load config", { cause: err });
  }
}

try {
  await loadConfig();
} catch (e) {
  console.log(e.message); // "Could not load config"
  console.log(e.cause.message); // original error message
}
```

### 231: How do you create a custom error class?

Extend `Error`.

```js
class ValidationError extends Error {
  constructor(field, message, options) {
    super(message, options);
    this.name = "ValidationError";
    this.field = field;
  }
}

try {
  throw new ValidationError("email", "Email is invalid");
} catch (e) {
  if (e instanceof ValidationError) {
    console.log(e.field, e.message); // "email" "Email is invalid"
  }
}
```

Setting `this.name` makes the stack trace and logs show the right error type.

### 232: What is AggregateError?

`AggregateError` holds several errors in its `errors` array. `Promise.any` throws it when all promises reject.

```js
try {
  await Promise.any([
    Promise.reject(new Error("A")),
    Promise.reject(new Error("B")),
  ]);
} catch (e) {
  e instanceof AggregateError; // true
  e.errors.map((err) => err.message); // ["A", "B"]
}

throw new AggregateError([new Error("x"), new Error("y")], "Several failures");
```

### 233: What is AbortController?

`AbortController` lets you cancel async operations like `fetch`, event listeners and streams.

```js
const controller = new AbortController();

fetch("/api/data", { signal: controller.signal })
  .then((res) => res.json())
  .catch((err) => {
    if (err.name === "AbortError") console.log("Request cancelled");
  });

controller.abort();
```

It is also used to remove event listeners:

```js
const ac = new AbortController();
window.addEventListener("resize", onResize, { signal: ac.signal });
window.addEventListener("scroll", onScroll, { signal: ac.signal });
ac.abort(); // removes both listeners
```

### 234: How do you add a timeout to fetch?

Use `AbortSignal.timeout()`.

```js
try {
  const res = await fetch("/api/slow", { signal: AbortSignal.timeout(5000) });
  const data = await res.json();
} catch (err) {
  if (err.name === "TimeoutError") {
    console.log("Took too long");
  }
}
```

To combine a timeout with a manual cancel signal, use `AbortSignal.any`:

```js
const controller = new AbortController();
const signal = AbortSignal.any([controller.signal, AbortSignal.timeout(5000)]);
fetch("/api", { signal });
```

### 235: What are URL and URLSearchParams?

They are built-in classes for working with URLs safely instead of building strings by hand.

```js
const url = new URL("https://example.com/search?q=js&page=2");

url.hostname; // "example.com"
url.pathname; // "/search"
url.searchParams.get("q"); // "js"
url.searchParams.set("page", "3");
url.searchParams.append("sort", "new");
url.toString(); // "https://example.com/search?q=js&page=3&sort=new"

const params = new URLSearchParams({ name: "Ann Lee", city: "NY" });
params.toString(); // "name=Ann+Lee&city=NY"

URL.canParse("not a url"); // false
```

### 236: What is FormData?

`FormData` collects form fields as key-value pairs. You can send it directly with `fetch`.

```js
const form = document.querySelector("form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = new FormData(form);

  data.get("email");
  Object.fromEntries(data); // plain object (only last value for repeated keys)

  await fetch("/api/signup", { method: "POST", body: data });
});
```

When you send `FormData`, don't set the `Content-Type` header yourself. The browser adds it with the correct boundary.

### 237: What is the difference between dynamic import and static import?

Static `import` is at the top of the file and is loaded before the code runs. Dynamic `import()` is a function-like expression that loads a module at runtime and returns a promise.

```js
// static
import { format } from "./utils.js";

// dynamic
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});
```

Dynamic imports are used for code splitting and lazy loading. They also work in CommonJS files.

### 238: What is the difference between CommonJS and ES modules?

|                     | CommonJS                    | ES modules                     |
| ------------------- | --------------------------- | ------------------------------ |
| Syntax              | `require`, `module.exports` | `import`, `export`             |
| Loading             | synchronous                 | asynchronous                   |
| When resolved       | at runtime                  | parsed before running (static) |
| Top-level await     | no                          | yes                            |
| `this` at top level | `module.exports`            | `undefined`                    |
| Tree-shaking        | hard                        | easy                           |
| Used in             | older Node.js code          | browsers, modern Node.js       |

```js
// CommonJS
const fs = require("fs");
module.exports = { read };

// ESM
import fs from "node:fs";
export { read };
```

Modern Node.js can also `require()` an ES module (as long as it doesn't use top-level await).

### 239: What are import attributes?

Import attributes (ES2025) give extra information about a module you import. The main use is importing JSON.

```js
import config from "./config.json" with { type: "json" };

const data = await import("./data.json", { with: { type: "json" } });
```

The `type: "json"` is required so the browser knows it's not loading JavaScript, which is a security measure. CSS module scripts (`with { type: "css" }`) also use this syntax in some browsers.

### 240: What is tree shaking?

Tree shaking is when a bundler (like Vite, Rollup, esbuild or webpack) removes code that is exported but never imported. It works best with ES modules because imports and exports are static.

```js
// utils.js
export function used() {}
export function unused() {}

// app.js
import { used } from "./utils.js";
// "unused" is removed from the final bundle
```

Side effects at the top level of modules can stop tree shaking. Package authors mark files as side-effect free with `"sideEffects": false` in `package.json`.

### 241: What is the difference between a polyfill and a transpiler?

- A **polyfill** adds missing features (functions, methods) at runtime. Example: adding `Array.prototype.toSorted` in an old browser.
- A **transpiler** (like Babel, SWC or TypeScript) rewrites new syntax into older syntax at build time. Example: turning `?.` into older code.

Syntax can't be polyfilled, it has to be transpiled. New APIs can be polyfilled.

```js
// simple polyfill
if (!Array.prototype.last) {
  Object.defineProperty(Array.prototype, "last", {
    value() {
      return this[this.length - 1];
    },
  });
}
```

### 242: What is requestAnimationFrame?

`requestAnimationFrame(callback)` runs your function right before the browser's next repaint, usually 60 times a second (or matching the screen refresh rate). It is the right way to run animations in JavaScript.

```js
const box = document.querySelector(".box");
let x = 0;

function animate() {
  x += 2;
  box.style.transform = `translateX(${x}px)`;
  if (x < 300) requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

It pauses in background tabs, which saves battery. `cancelAnimationFrame(id)` stops it.

### 243: What is IntersectionObserver?

`IntersectionObserver` tells you when an element enters or leaves the viewport (or another element). It is used for lazy loading, infinite scroll and animations on scroll.

```js
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.src = entry.target.dataset.src;
        observer.unobserve(entry.target);
      }
    }
  },
  { rootMargin: "200px" },
);

document
  .querySelectorAll("img[data-src]")
  .forEach((img) => observer.observe(img));
```

It is much cheaper than listening to the `scroll` event and measuring elements.

### 244: What is MutationObserver?

`MutationObserver` watches for changes in the DOM, like added or removed nodes, or changed attributes.

```js
const observer = new MutationObserver((mutations) => {
  for (const m of mutations) {
    console.log(m.type, m.addedNodes, m.attributeName);
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
  attributes: true,
});

observer.disconnect();
```

### 245: What is ResizeObserver?

`ResizeObserver` tells you when an element's size changes, not just the window.

```js
const ro = new ResizeObserver((entries) => {
  for (const entry of entries) {
    const { width } = entry.contentRect;
    entry.target.classList.toggle("compact", width < 400);
  }
});

ro.observe(document.querySelector(".card"));
```

### 246: What is the difference between reflow and repaint?

- **Reflow (layout)**: the browser recalculates sizes and positions of elements. Caused by changes to width, height, font size, adding elements, etc. It's expensive.
- **Repaint**: the browser redraws pixels without changing layout, like changing `color` or `background`.

Reading layout values (like `offsetHeight`) right after writing styles forces a sync reflow. Doing this in a loop is called layout thrashing.

```js
// bad: read and write in a loop
items.forEach((el) => {
  el.style.height = el.offsetHeight + 10 + "px";
});

// better: read all, then write all
const heights = items.map((el) => el.offsetHeight);
items.forEach((el, i) => {
  el.style.height = heights[i] + 10 + "px";
});
```

Animating `transform` and `opacity` avoids reflow.

### 247: What is a Web Worker?

A Web Worker runs JavaScript in a background thread, so heavy work does not freeze the page. Workers can't access the DOM. They talk to the main thread with messages.

```js
// main.js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
worker.postMessage({ numbers: [1, 2, 3] });
worker.onmessage = (e) => console.log("Result:", e.data);

// worker.js
self.onmessage = (e) => {
  const sum = e.data.numbers.reduce((a, b) => a + b, 0);
  self.postMessage(sum);
};
```

### 248: What is a Service Worker?

A Service Worker is a script that runs in the background, separate from the page. It sits between the app and the network, so it can cache responses, make the app work offline, and handle push notifications.

```js
// register
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/sw.js");
}

// sw.js
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches
      .match(event.request)
      .then((cached) => cached ?? fetch(event.request)),
  );
});
```

Service Workers require HTTPS (except on localhost). They are the base of Progressive Web Apps (PWAs).

### 249: What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser security rule. By default, a page can't read responses from a different origin (protocol + domain + port). The server must allow it with headers like `Access-Control-Allow-Origin`.

```
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type
```

For "non-simple" requests (like `PUT`, or JSON with custom headers), the browser first sends an `OPTIONS` preflight request to check permission.

CORS is enforced by the browser. Server-to-server requests are not affected. You fix CORS errors on the server, not in the frontend code.

### 250: What is the same-origin policy?

The same-origin policy is a browser rule that stops scripts on one origin from reading data from another origin. Two URLs have the same origin only if the protocol, host and port all match.

```
https://site.com/a  and  https://site.com/b      -> same origin
https://site.com    and  http://site.com         -> different (protocol)
https://site.com    and  https://api.site.com    -> different (host)
https://site.com    and  https://site.com:8080   -> different (port)
```

CORS is the controlled way to relax this rule.

### 251: What is the difference between null-prototype objects and normal objects?

A normal object `{}` inherits from `Object.prototype`, so it has keys like `toString`, `constructor` and `hasOwnProperty`. An object made with `Object.create(null)` has none of these.

```js
const normal = {};
"toString" in normal; // true

const bare = Object.create(null);
"toString" in bare; // false
```

Null-prototype objects are safer when you use them as a dictionary with keys from user input, because a key like `"constructor"` or `"__proto__"` won't clash with inherited properties.

### 252: What is prototype pollution?

Prototype pollution is a security bug where an attacker changes `Object.prototype` (usually through a key like `__proto__` in user input), which affects every object in the app.

```js
function unsafeMerge(target, source) {
  for (const key in source) {
    if (typeof source[key] === "object") {
      target[key] ??= {};
      unsafeMerge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
}

unsafeMerge({}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
({}).isAdmin; // true !!
```

How to prevent it:

- Skip `__proto__`, `constructor` and `prototype` keys when merging.
- Use `Map` or `Object.create(null)` for user-controlled keys.
- Use `Object.hasOwn` checks.
- Freeze `Object.prototype` in sensitive environments.

### 253: What is the difference between Object.keys, Object.getOwnPropertyNames and Reflect.ownKeys?

- `Object.keys`: own, enumerable, string keys.
- `Object.getOwnPropertyNames`: own string keys, enumerable or not.
- `Object.getOwnPropertySymbols`: own symbol keys.
- `Reflect.ownKeys`: all own keys, strings and symbols, enumerable or not.

```js
const sym = Symbol("s");
const obj = { a: 1, [sym]: 2 };
Object.defineProperty(obj, "hidden", { value: 3, enumerable: false });

Object.keys(obj); // ["a"]
Object.getOwnPropertyNames(obj); // ["a", "hidden"]
Reflect.ownKeys(obj); // ["a", "hidden", Symbol(s)]
```

### 254: In what order are object keys returned?

For own properties the order is:

1. Integer-like keys in ascending numeric order.
2. String keys in the order they were added.
3. Symbol keys in the order they were added (only for methods that include symbols).

```js
const obj = { b: 1, 2: "x", a: 2, 1: "y" };
Object.keys(obj); // ["1", "2", "b", "a"]
```

If you need a guaranteed insertion order for all keys, use a `Map`.

### 255: How do you implement a simple observer (pub/sub) pattern?

```js
class EventEmitter {
  #listeners = new Map();

  on(event, fn) {
    if (!this.#listeners.has(event)) this.#listeners.set(event, new Set());
    this.#listeners.get(event).add(fn);
    return () => this.off(event, fn); // return unsubscribe function
  }

  off(event, fn) {
    this.#listeners.get(event)?.delete(fn);
  }

  emit(event, ...args) {
    for (const fn of this.#listeners.get(event) ?? []) {
      fn(...args);
    }
  }
}

const bus = new EventEmitter();
const unsubscribe = bus.on("save", (doc) => console.log("Saved", doc));
bus.emit("save", { id: 1 });
unsubscribe();
```

### 256: What is the module pattern?

The module pattern uses a closure (usually an IIFE) to create private state and expose only a public API. It was very common before ES modules.

```js
const Counter = (function () {
  let count = 0;

  function change(by) {
    count += by;
  }

  return {
    increment: () => change(1),
    decrement: () => change(-1),
    value: () => count,
  };
})();

Counter.increment();
Counter.value(); // 1
Counter.count; // undefined
```

Today ES modules give you the same privacy: anything not exported stays private to the file.

### 257: How do you implement a singleton in JavaScript?

The simplest singleton is a module that exports one instance, because modules are only evaluated once.

```js
// db.js
class Database {
  constructor() {
    this.connected = false;
  }
  connect() {
    this.connected = true;
  }
}

export const db = new Database();
```

With a class:

```js
class Config {
  static #instance;

  static getInstance() {
    return (Config.#instance ??= new Config());
  }
}

Config.getInstance() === Config.getInstance(); // true
```

### 258: What is a mixin?

A mixin is a way to add methods from several sources to a class, since JavaScript only supports single inheritance.

```js
const CanFly = (Base) =>
  class extends Base {
    fly() {
      return `${this.name} is flying`;
    }
  };

const CanSwim = (Base) =>
  class extends Base {
    swim() {
      return `${this.name} is swimming`;
    }
  };

class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Duck extends CanSwim(CanFly(Animal)) {}

const d = new Duck("Donald");
d.fly(); // "Donald is flying"
d.swim(); // "Donald is swimming"
```

### 259: What is method chaining?

Method chaining is calling several methods one after another on the same object. Each method returns an object (often `this`) so the next one can be called.

```js
class QueryBuilder {
  #parts = [];
  select(fields) {
    this.#parts.push(`SELECT ${fields}`);
    return this;
  }
  from(table) {
    this.#parts.push(`FROM ${table}`);
    return this;
  }
  where(cond) {
    this.#parts.push(`WHERE ${cond}`);
    return this;
  }
  build() {
    return this.#parts.join(" ");
  }
}

new QueryBuilder().select("*").from("users").where("age > 18").build();
// "SELECT * FROM users WHERE age > 18"
```

Array methods like `filter().map().slice()` are also chaining.

### 260: What is the difference between composition and inheritance?

- **Inheritance**: a class gets behavior from a parent class ("is a"). Deep inheritance trees become hard to change.
- **Composition**: an object is built from smaller pieces of behavior ("has a"). It's usually more flexible.

```js
// composition
const canEat = (state) => ({
  eat: () => console.log(`${state.name} eats`),
});
const canWalk = (state) => ({
  walk: () => console.log(`${state.name} walks`),
});

function createPerson(name) {
  const state = { name };
  return { ...canEat(state), ...canWalk(state) };
}

createPerson("Ann").walk(); // "Ann walks"
```

A common piece of advice is "favor composition over inheritance".

### 261: What is the difference between an expression and a statement?

An expression produces a value. A statement performs an action.

```js
// expressions
5 + 3;
user.name;
isValid ? "yes" : "no";
fn();

// statements
if (x) {
}
for (;;) {}
let y = 5;
return x;
```

This matters in places that only accept expressions, like template literal `${}` or an arrow function body without braces. That's why you use a ternary instead of `if` there.

### 262: What is automatic semicolon insertion (ASI)?

When you leave out semicolons, the JavaScript parser adds them in some places. Usually this works, but there are a few traps.

```js
// 1. return on its own line
function get() {
  return;
  {
    ok: true;
  }
}
get(); // undefined

// 2. line starting with ( or [
const a = 1;
const b = a[(1, 2)].forEach((n) => console.log(n));
// read as: const b = a[1, 2].forEach(...) -> TypeError
```

If you don't use semicolons, put one at the start of lines that begin with `(`, `[` or `` ` ``. Using a formatter like Prettier also avoids these issues.

### 263: What is the difference between function.length and arguments.length?

`fn.length` is the number of parameters the function declares (before the first default or rest parameter). `arguments.length` is how many arguments were actually passed.

```js
function f(a, b, c = 1, ...rest) {
  return arguments.length;
}

f.length; // 2
f(1, 2, 3, 4); // 4
```

### 264: What are sparse arrays?

A sparse array has "holes": indexes with no value at all (not even `undefined`).

```js
const arr = [1, , 3];
arr.length; // 3
1 in arr; // false (hole)

const arr2 = new Array(3); // [ <3 empty items> ]
arr2[5] = "x"; // indexes 3 and 4 are holes
```

Methods treat holes differently. `forEach`, `map`, `filter` skip them. `for...of`, spread, `Array.from` and the new `toSorted`/`with` treat them as `undefined`. It's best to avoid creating sparse arrays.

### 265: What happens when you use delete on an array element?

It removes the value but leaves a hole. The length doesn't change.

```js
const arr = [1, 2, 3];
delete arr[1];
arr; // [1, <1 empty item>, 3]
arr.length; // 3
```

Use `splice` (or `toSpliced`/`filter`) to actually remove an item.

### 266: How does Array.prototype.sort work with strings and accents?

The default sort compares UTF-16 code units, which gives wrong results for uppercase vs lowercase and accented letters. Use `localeCompare` or `Intl.Collator`.

```js
["b", "a", "C", "é"].sort();
// ["C", "a", "b", "é"]

["b", "a", "C", "é"].sort((x, y) => x.localeCompare(y));
// ["a", "b", "C", "é"]

const collator = new Intl.Collator("en", {
  numeric: true,
  sensitivity: "base",
});
["item10", "item2", "Item1"].sort(collator.compare);
// ["Item1", "item2", "item10"]
```

Since ES2019, `sort` is guaranteed to be stable: items that compare equal keep their original order.

### 267: How do you sort an array of objects by multiple fields?

```js
const users = [
  { name: "Bob", age: 30 },
  { name: "Ann", age: 25 },
  { name: "Cid", age: 25 },
];

const sorted = users.toSorted(
  (a, b) => a.age - b.age || a.name.localeCompare(b.name),
);
// Ann 25, Cid 25, Bob 30
```

If the first comparison returns `0`, `||` moves on to the next one.

### 268: What is the Intl object?

`Intl` is the built-in internationalization API. It formats numbers, dates, lists and more for different languages and regions.

```js
new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(
  1234.5,
);
// "1.234,50 €"

new Intl.DateTimeFormat("ja-JP", { dateStyle: "full" }).format(new Date());

new Intl.RelativeTimeFormat("en", { numeric: "auto" }).format(-1, "day");
// "yesterday"

new Intl.ListFormat("en", { type: "conjunction" }).format(["A", "B", "C"]);
// "A, B, and C"

new Intl.PluralRules("en").select(1); // "one"

new Intl.DisplayNames(["en"], { type: "region" }).of("JP"); // "Japan"
```

### 269: Why does "😀".length return 2?

JavaScript strings are UTF-16. Characters outside the Basic Multilingual Plane (like most emoji) use two code units (a surrogate pair), so `length` counts them as 2.

```js
"😀".length; // 2
[..."😀"].length; // 1 (code points)
"👨‍👩‍👧".length; // 8
[..."👨‍👩‍👧"].length; // 5 (several code points joined)
```

To count what a user sees as one character (grapheme), use `Intl.Segmenter`:

```js
const seg = new Intl.Segmenter("en", { granularity: "grapheme" });
[...seg.segment("👨‍👩‍👧")].length; // 1
```

### 270: What is string normalization?

Some characters can be written in more than one way in Unicode. For example, "é" can be one code point or "e" plus a combining accent. They look the same but are not equal.

```js
const a = "é"; // é
const b = "é"; // e + combining accent

a === b; // false
a.normalize() === b.normalize(); // true
```

Normalize strings before comparing or storing user input.

### 271: What are isWellFormed and toWellFormed?

They (ES2024) check and fix strings that have lone surrogates (broken UTF-16), which can cause errors in functions like `encodeURIComponent`.

```js
const bad = "abc\uD800";

bad.isWellFormed(); // false
bad.toWellFormed(); // "abc�" (replaced with �)

encodeURIComponent(bad); // URIError
encodeURIComponent(bad.toWellFormed()); // works
```

### 272: What are the main problems with the Date object?

- Months start at 0, days start at 1.
- Date objects are mutable, so passing them around can cause bugs.
- Parsing strings is inconsistent: `"2025-03-15"` is parsed as UTC but `"2025/03/15"` as local time.
- Only local time and UTC are supported, no other time zones.
- No separate types for "just a date" or "just a time".
- Date math (like adding a month) is awkward.

```js
const d = new Date(2025, 0, 31);
d.setMonth(1); // February 31 doesn't exist
d.toDateString(); // "Mon Mar 03 2025"
```

### 273: What is the Temporal API?

`Temporal` is the modern replacement for `Date`. It has immutable objects, clear types, full time zone support and correct date math. It is now available in recent versions of Firefox and Chrome. For other environments you can use a polyfill.

```js
const today = Temporal.Now.plainDateISO(); // 2025-03-15
const nextMonth = today.add({ months: 1 });

const meeting = Temporal.ZonedDateTime.from(
  "2025-03-15T10:00[America/New_York]",
);
meeting.withTimeZone("Europe/Paris").toString();

const d1 = Temporal.PlainDate.from("2025-01-01");
const d2 = Temporal.PlainDate.from("2025-03-15");
d1.until(d2).days; // 73

Temporal.PlainDate.from("2025-01-31").add({ months: 1 }).toString();
// "2025-02-28" (clamped, not overflowed)
```

Main types: `PlainDate`, `PlainTime`, `PlainDateTime`, `ZonedDateTime`, `Instant`, `Duration`.

### 274: How do you compute the difference between two dates with Date?

Subtract them. You get milliseconds.

```js
const start = new Date("2025-01-01");
const end = new Date("2025-03-15");

const ms = end - start;
const days = Math.round(ms / (1000 * 60 * 60 * 24)); // 73
```

Be careful with daylight saving time when working in local time. A "day" is not always 24 hours. `Temporal` handles this correctly.

### 275: What does the "in" operator do?

`in` checks if a property exists in an object or its prototype chain.

```js
const car = { brand: "Toyota" };

"brand" in car; // true
"toString" in car; // true (inherited)
"model" in car; // false

const arr = ["a"];
0 in arr; // true
1 in arr; // false
```

### 276: What are bitwise operators and when are they used?

Bitwise operators work on the 32-bit integer form of numbers.

```js
5 & 3; // 1  (AND)
5 | 3; // 7  (OR)
5 ^ 3; // 6  (XOR)
~5; // -6 (NOT)
5 << 1; // 10 (left shift)
5 >> 1; // 2  (right shift)
-5 >>> 0; // 4294967291 (unsigned right shift)
```

A common use is flags:

```js
const READ = 1,
  WRITE = 2,
  EXEC = 4;
let perms = READ | WRITE;
(perms & WRITE) !== 0; // true
perms &= ~WRITE; // remove WRITE
```

### 277: What is the difference between Object.entries and Object.fromEntries?

They are opposites. `Object.entries` turns an object into `[key, value]` pairs. `Object.fromEntries` turns pairs (or a Map) back into an object.

```js
const prices = { apple: 1, banana: 2 };

const doubled = Object.fromEntries(
  Object.entries(prices).map(([k, v]) => [k, v * 2]),
);
// { apple: 2, banana: 4 }

Object.fromEntries(new Map([["a", 1]])); // { a: 1 }
Object.fromEntries(new URLSearchParams("x=1&y=2")); // { x: "1", y: "2" }
```

### 278: How do you flatten a nested object?

```js
function flatten(obj, prefix = "", result = {}) {
  for (const [key, value] of Object.entries(obj)) {
    const path = prefix ? `${prefix}.${key}` : key;
    if (value && typeof value === "object" && !Array.isArray(value)) {
      flatten(value, path, result);
    } else {
      result[path] = value;
    }
  }
  return result;
}

flatten({ a: 1, b: { c: 2, d: { e: 3 } } });
// { a: 1, "b.c": 2, "b.d.e": 3 }
```

### 279: How do you safely access a deeply nested value by a path string?

```js
function get(obj, path, defaultValue) {
  const result = path.split(".").reduce((acc, key) => acc?.[key], obj);
  return result ?? defaultValue;
}

const data = { user: { address: { city: "Paris" } } };
get(data, "user.address.city"); // "Paris"
get(data, "user.phone.number", "none"); // "none"
```

### 280: How do you chunk an array into groups of a given size?

```js
function chunk(arr, size) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]

// Using Array.from
const chunk2 = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
    arr.slice(i * size, i * size + size),
  );
```

### 281: How do you find the intersection and difference of two arrays?

```js
const a = [1, 2, 3, 4];
const b = [3, 4, 5];

// using Set methods (ES2025)
[...new Set(a).intersection(new Set(b))]; // [3, 4]
[...new Set(a).difference(new Set(b))]; // [1, 2]

// using filter
const setB = new Set(b);
a.filter((x) => setB.has(x)); // [3, 4]
a.filter((x) => !setB.has(x)); // [1, 2]
```

Converting to a `Set` first makes lookups O(1) instead of O(n).

### 282: How do you count occurrences of items in an array?

```js
const words = ["a", "b", "a", "c", "a", "b"];

const counts = words.reduce((acc, w) => {
  acc[w] = (acc[w] ?? 0) + 1;
  return acc;
}, {});
// { a: 3, b: 2, c: 1 }

const countMap = new Map();
for (const w of words) countMap.set(w, (countMap.get(w) ?? 0) + 1);

// with groupBy
Object.fromEntries(
  Object.entries(Object.groupBy(words, (w) => w)).map(([k, v]) => [
    k,
    v.length,
  ]),
);
```

### 283: How do you shuffle an array correctly?

Use the Fisher-Yates algorithm. The common `sort(() => Math.random() - 0.5)` trick does not give a fair shuffle.

```js
function shuffle(arr) {
  const result = [...arr];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

shuffle([1, 2, 3, 4, 5]);
```

### 284: How do you check if a string is a palindrome?

```js
function isPalindrome(str) {
  const clean = str.toLowerCase().replace(/[^a-z0-9]/g, "");
  return clean === [...clean].reverse().join("");
}

isPalindrome("A man, a plan, a canal: Panama"); // true
isPalindrome("hello"); // false
```

### 285: How do you capitalize the first letter of each word?

```js
const titleCase = (str) =>
  str
    .toLowerCase()
    .split(" ")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");

titleCase("hello wORLD from js"); // "Hello World From Js"

// with regex
"hello world".replace(/\b\w/g, (c) => c.toUpperCase()); // "Hello World"
```

### 286: How do you convert between camelCase, snake_case and kebab-case?

```js
const toKebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
const toSnake = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1_$2").toLowerCase();
const toCamel = (s) => s.replace(/[-_](\w)/g, (_, c) => c.toUpperCase());

toKebab("backgroundColor"); // "background-color"
toSnake("userId"); // "user_id"
toCamel("font-size"); // "fontSize"
toCamel("created_at"); // "createdAt"
```

### 287: What is a pure vs impure array method example in React state updates?

React needs a new array or object reference to detect changes, so you must not mutate state directly.

```js
// wrong: mutates state
todos.push(newTodo);
setTodos(todos);

// right
setTodos([...todos, newTodo]);
setTodos(todos.filter((t) => t.id !== id));
setTodos(todos.map((t) => (t.id === id ? { ...t, done: true } : t)));
setTodos(todos.toSorted((a, b) => a.date - b.date));
```

The same idea applies to Redux, Vue's `shallowRef`, and other state libraries that compare by reference.

### 288: What is the difference between Object.assign and spread for copying?

Both make shallow copies, but there are small differences:

- `Object.assign(target, ...)` changes `target` and calls setters on it.
- Spread `{ ...obj }` always creates a new object and defines properties (no setters called).

```js
const target = {
  set name(v) {
    console.log("setter called with", v);
  },
};

Object.assign(target, { name: "Ann" }); // "setter called with Ann"
const copy = { ...target, name: "Ann" }; // no setter call, name becomes a plain property
```

Both copy only own enumerable properties, and both run getters on the source.

### 289: How does garbage collection work in JavaScript?

JavaScript manages memory automatically. Engines use a "mark and sweep" approach: starting from roots (global object, current call stack), they mark everything that can be reached. Anything not marked is unreachable and gets freed.

```js
let user = { name: "Ann" };
user = null; // the object is now unreachable and can be collected
```

Modern engines like V8 use a generational collector: new objects are checked often (most die young), and long-lived objects are checked less often.

### 290: What are common causes of memory leaks in JavaScript?

- Event listeners that are never removed
- Timers (`setInterval`) that are never cleared
- Global variables that keep growing
- Closures that hold on to large objects
- Detached DOM nodes still referenced from JavaScript
- Caches (Maps) that grow forever

```js
// leak: listener holds a reference to bigData forever
function setup() {
  const bigData = new Array(1e6).fill("x");
  window.addEventListener("resize", () => console.log(bigData.length));
}

// fix: remove the listener when done
function setupFixed() {
  const bigData = new Array(1e6).fill("x");
  const ac = new AbortController();
  window.addEventListener("resize", () => console.log(bigData.length), {
    signal: ac.signal,
  });
  return () => ac.abort();
}
```

Use the Memory tab in Chrome DevTools (heap snapshots) to find leaks.

### 291: What does Function.prototype.toString return?

It returns the source code of the function as a string.

```js
function add(a, b) {
  return a + b;
}

add.toString();
// "function add(a, b) {\n  return a + b;\n}"

Math.max.toString(); // "function max() { [native code] }"
```

### 292: What is the name property of a function?

Functions have a `name` property. For anonymous functions assigned to variables, JavaScript infers the name.

```js
function foo() {}
foo.name; // "foo"

const bar = () => {};
bar.name; // "bar"

const obj = { baz() {} };
obj.baz.name; // "baz"

foo.bind(null).name; // "bound foo"
```

It is useful in stack traces and debugging.

### 293: What is a getter on an object literal and when is it useful?

A getter computes a value when the property is read.

```js
const cart = {
  items: [{ price: 10 }, { price: 15 }],
  get total() {
    return this.items.reduce((sum, i) => sum + i.price, 0);
  },
};

cart.total; // 25
cart.items.push({ price: 5 });
cart.total; // 30
```

It is useful for derived values that should always be up to date.

### 294: What is the difference between a library and a framework?

- With a **library**, your code calls the library when you need it (for example, lodash or date-fns).
- With a **framework**, the framework calls your code. It controls the structure and flow (for example, Angular or Next.js).

This idea is called "inversion of control". React calls itself a library, but in practice it controls rendering, so it sits somewhere in between.

### 295: What is the difference between client-side and server-side rendering?

- **Client-side rendering (CSR)**: the server sends a mostly empty HTML page and JavaScript builds the UI in the browser. Fast navigation after load, but slower first paint and weaker SEO.
- **Server-side rendering (SSR)**: the server sends ready HTML for each request. Faster first paint and better SEO. JavaScript then "hydrates" the page to make it interactive.
- **Static site generation (SSG)**: HTML is built once at build time and served from a CDN.

Frameworks like Next.js, Nuxt, SvelteKit and Astro let you mix these per page.

### 296: What is hydration?

Hydration is the step where client-side JavaScript takes server-rendered HTML and attaches event listeners and state to it, making it interactive.

If the HTML that the client would render doesn't match the server HTML, you get a "hydration mismatch" error. Common causes are using `Date.now()`, `Math.random()` or `window` during render.

Newer approaches like partial hydration (islands) and resumability try to reduce how much JavaScript runs during hydration.

### 297: What does the debugger statement do?

`debugger` pauses code execution at that line if developer tools are open, like a breakpoint.

```js
function calculate(a, b) {
  debugger;
  return a * b;
}
```

If dev tools are closed, it does nothing. Remove it before shipping code.

### 298: What is the difference between console.log of an object and its actual value at that time?

In browser consoles, logged objects are shown "live". When you expand the object, it shows the current state, not the state at the time of logging.

```js
const obj = { count: 1 };
console.log(obj);
obj.count = 2;
// expanding the logged object may show count: 2
```

To log a snapshot use `console.log(structuredClone(obj))` or `console.log(JSON.stringify(obj))`.

### 299: What is the Clipboard API?

The async Clipboard API lets you read and write the clipboard. It requires a secure context (HTTPS) and usually a user action.

```js
button.addEventListener("click", async () => {
  await navigator.clipboard.writeText("Copied text");
});

const text = await navigator.clipboard.readText(); // asks for permission
```

The old `document.execCommand("copy")` is deprecated.

### 300: What is the History API?

The History API lets single-page apps change the URL without reloading the page.

```js
history.pushState({ page: 2 }, "", "/page/2"); // adds an entry
history.replaceState({ page: 3 }, "", "/page/3"); // replaces current entry

window.addEventListener("popstate", (event) => {
  console.log("Back/forward to", location.pathname, event.state);
});

history.back();
history.forward();
```

Modern browsers are also adding the newer Navigation API (`navigation.navigate`, `navigate` event), which is easier to use for client-side routing.

---

# Advanced Questions (301-450)

### 301: What is an execution context?

An execution context is the environment where a piece of code runs. There are three kinds: the global context, a function context (one for each call), and an `eval` context.

Each context has:

- a **lexical environment** (where `let`, `const`, functions and classes live, plus a link to the outer environment)
- a **variable environment** (where `var` declarations live)
- a `this` binding

Creating a context has two phases:

1. **Creation**: declarations are registered. Functions are fully set up, `var` gets `undefined`, `let`/`const`/`class` are left uninitialized (TDZ).
2. **Execution**: the code runs line by line and values are assigned.

This two-phase setup is the reason hoisting exists.

### 302: How does closure work at the engine level?

When a function is created, it keeps a hidden reference (called `[[Environment]]` in the spec) to the lexical environment it was created in. When the function runs, its new environment points to that saved environment as its outer scope.

As long as the function is reachable, the environment it points to is also kept in memory.

```js
function outer() {
  const big = new Array(1_000_000).fill(0);
  const small = 1;
  return () => small;
}

const fn = outer();
```

In theory `big` is part of the same environment. In practice V8 only keeps variables that inner functions actually use, so `big` can be collected here. But if any closure from the same scope uses `big` (for example, a second inner function or an `eval`), it stays alive for all closures created in that scope. This is a common source of hidden memory leaks.

### 303: Explain the abstract equality (==) algorithm.

Simplified rules for `x == y`:

1. If both have the same type, compare like `===`.
2. `null == undefined` is `true`. They are not equal to anything else.
3. Number and string: convert the string to a number.
4. BigInt and string: convert the string to a BigInt.
5. If one side is a boolean, convert it to a number first, then compare again.
6. If one side is an object and the other is a primitive, convert the object to a primitive (`ToPrimitive`) and compare again.
7. BigInt and number: compare their math values.

```js
"1" == 1; // "1" -> 1, true
true == "1"; // true -> 1, then "1" -> 1, true
[1] == 1; // [1] -> "1" -> 1, true
null == 0; // false (null only equals undefined)
[] == ![]; // see next question
```

### 304: Why is [] == ![] true?

Step by step:

1. `![]`: an array is truthy, so `![]` is `false`.
2. Now we have `[] == false`.
3. Boolean is converted to a number: `[] == 0`.
4. The object is converted to a primitive: `[].toString()` is `""`, so `"" == 0`.
5. String is converted to a number: `0 == 0`.
6. Result: `true`.

This is a good example of why `===` is recommended.

### 305: How does ToPrimitive work and what is Symbol.toPrimitive?

When an object needs to become a primitive (in `+`, `==`, template literals, etc.), JavaScript calls `ToPrimitive` with a "hint": `"string"`, `"number"` or `"default"`.

1. If the object has `[Symbol.toPrimitive]`, it is called with the hint.
2. Otherwise, for the `"string"` hint, it tries `toString()` and then `valueOf()`.
3. For `"number"` and `"default"`, it tries `valueOf()` first and then `toString()`.

```js
const money = {
  amount: 42,
  currency: "USD",
  [Symbol.toPrimitive](hint) {
    if (hint === "number") return this.amount;
    if (hint === "string") return `${this.amount} ${this.currency}`;
    return `${this.amount} ${this.currency}`; // default
  },
};

+money; // 42
`${money}`; // "42 USD"
money + ""; // "42 USD" (default hint)
money * 2; // 84
```

`Date` is a special case. Its default hint behaves like `"string"`, which is why `new Date() + 1` gives a string.

### 306: What are the results of these expressions: [] + {}, {} + [], [] + [], {} + {}?

```js
[] + {}; // "[object Object]"  ("" + "[object Object]")
[] + []; // ""                 ("" + "")
({}) + []; // "[object Object]"
({}) + {}; // "[object Object][object Object]"
```

If you type `{} + []` at the start of a line in a console, the `{}` may be parsed as an empty block, so the result is `+[]`, which is `0`. Wrapping in parentheses forces it to be an expression.

### 307: What is a Proxy?

A `Proxy` wraps an object and lets you intercept operations on it, like reading, writing, deleting properties or calling a function. The functions that intercept are called "traps".

```js
const user = { name: "Ann", age: 25 };

const validated = new Proxy(user, {
  get(target, prop, receiver) {
    if (!(prop in target)) {
      throw new Error(`Property "${String(prop)}" does not exist`);
    }
    return Reflect.get(target, prop, receiver);
  },
  set(target, prop, value, receiver) {
    if (prop === "age" && !Number.isInteger(value)) {
      throw new TypeError("Age must be an integer");
    }
    return Reflect.set(target, prop, value, receiver);
  },
});

validated.age = 30; // ok
validated.age = "old"; // TypeError
validated.email; // Error
```

Vue 3 uses proxies for its reactivity system. MobX and Immer also use them.

### 308: What traps are available on a Proxy?

There are 13 traps, one for each internal object operation:

- `get`, `set`, `has` (`in`), `deleteProperty`
- `ownKeys` (`Object.keys`, `for...in`, `Reflect.ownKeys`)
- `getOwnPropertyDescriptor`, `defineProperty`
- `getPrototypeOf`, `setPrototypeOf`
- `isExtensible`, `preventExtensions`
- `apply` (calling a function)
- `construct` (`new`)

```js
const logged = new Proxy(
  function sum(a, b) {
    return a + b;
  },
  {
    apply(target, thisArg, args) {
      console.log("called with", args);
      return Reflect.apply(target, thisArg, args);
    },
  },
);

logged(1, 2); // logs "called with [1, 2]", returns 3
```

### 309: What are proxy invariants?

Invariants are rules a trap must follow so the proxy can't lie about the target in ways that break the language. If a trap breaks an invariant, a `TypeError` is thrown.

Examples:

- `get` must return the real value for a non-writable, non-configurable property.
- `has` can't hide a non-configurable property.
- `ownKeys` must include all non-configurable keys.
- `getPrototypeOf` must return the real prototype if the target is non-extensible.

```js
const target = {};
Object.defineProperty(target, "id", {
  value: 1,
  writable: false,
  configurable: false,
});

const p = new Proxy(target, { get: () => 2 });
p.id; // TypeError: proxy must report the same value for non-writable property
```

### 310: What is Reflect and why use it with Proxy?

`Reflect` is an object with methods that match the proxy traps one to one: `Reflect.get`, `Reflect.set`, `Reflect.has`, `Reflect.ownKeys`, `Reflect.apply`, `Reflect.construct` and so on.

Inside traps, `Reflect` methods do the default behavior correctly, including passing the `receiver` so getters and setters get the right `this`.

```js
const parent = {
  _name: "parent",
  get name() {
    return this._name;
  },
};

const proxy = new Proxy(parent, {
  get(target, prop, receiver) {
    return Reflect.get(target, prop, receiver); // keeps the right "this"
  },
});

const child = Object.create(proxy);
child._name = "child";
child.name; // "child" (would be "parent" if we used target[prop])
```

`Reflect` methods also return booleans instead of throwing in some cases (like `Reflect.defineProperty`), which makes them easier to use.

### 311: Why do private fields not work through a Proxy?

Private fields are stored on the actual object, not looked up through properties. When a method is called on a proxy, `this` is the proxy, and the proxy does not have the private field, so you get a `TypeError`.

```js
class Counter {
  #count = 0;
  inc() {
    return ++this.#count;
  }
}

const p = new Proxy(new Counter(), {});
p.inc(); // TypeError: Cannot read private member #count from an object whose class did not declare it
```

A common fix is to bind methods to the original target in the `get` trap:

```js
const p2 = new Proxy(new Counter(), {
  get(target, prop) {
    const value = Reflect.get(target, prop);
    return typeof value === "function" ? value.bind(target) : value;
  },
});
p2.inc(); // 1
```

The same problem exists with built-ins that use internal slots, like `Map`, `Set` and `Date`.

### 312: How would you build a simple reactive system with Proxy?

```js
let activeEffect = null;
const deps = new WeakMap();

function track(target, key) {
  if (!activeEffect) return;
  let map = deps.get(target);
  if (!map) deps.set(target, (map = new Map()));
  let set = map.get(key);
  if (!set) map.set(key, (set = new Set()));
  set.add(activeEffect);
}

function trigger(target, key) {
  deps
    .get(target)
    ?.get(key)
    ?.forEach((fn) => fn());
}

function reactive(obj) {
  return new Proxy(obj, {
    get(target, key, receiver) {
      track(target, key);
      return Reflect.get(target, key, receiver);
    },
    set(target, key, value, receiver) {
      const ok = Reflect.set(target, key, value, receiver);
      trigger(target, key);
      return ok;
    },
  });
}

function effect(fn) {
  activeEffect = fn;
  fn();
  activeEffect = null;
}

const state = reactive({ count: 0 });
effect(() => console.log("count is", state.count)); // "count is 0"
state.count++; // "count is 1"
```

This is the basic idea behind Vue's reactivity.

### 313: What are well-known symbols?

Well-known symbols are built-in symbols that let you customize how objects behave with language features.

| Symbol                                                   | Used by                                |
| -------------------------------------------------------- | -------------------------------------- |
| `Symbol.iterator`                                        | `for...of`, spread, destructuring      |
| `Symbol.asyncIterator`                                   | `for await...of`                       |
| `Symbol.toPrimitive`                                     | type conversion                        |
| `Symbol.toStringTag`                                     | `Object.prototype.toString`            |
| `Symbol.hasInstance`                                     | `instanceof`                           |
| `Symbol.species`                                         | which constructor derived objects use  |
| `Symbol.isConcatSpreadable`                              | `Array.prototype.concat`               |
| `Symbol.match`, `replace`, `search`, `split`, `matchAll` | string methods with regex-like objects |
| `Symbol.unscopables`                                     | `with` statement                       |
| `Symbol.dispose`, `Symbol.asyncDispose`                  | `using` declarations                   |

```js
class Temperature {
  get [Symbol.toStringTag]() {
    return "Temperature";
  }
  static [Symbol.hasInstance](value) {
    return typeof value?.celsius === "number";
  }
}

Object.prototype.toString.call(new Temperature()); // "[object Temperature]"
({ celsius: 20 }) instanceof Temperature; // true
```

### 314: What is Symbol.species?

`Symbol.species` tells built-in methods which constructor to use when they create a new derived object, for example `map` or `filter` on an array subclass.

```js
class MyArray extends Array {
  static get [Symbol.species]() {
    return Array; // map/filter return plain arrays
  }
}

const arr = MyArray.from([1, 2, 3]);
const mapped = arr.map((x) => x * 2);

arr instanceof MyArray; // true
mapped instanceof MyArray; // false
mapped instanceof Array; // true
```

`Symbol.species` has caused security and performance problems in engines, and the newer array methods like `toSorted` and `with` don't use it. They always return plain arrays.

### 315: What is new.target?

`new.target` tells you whether a function or constructor was called with `new`, and which class was used.

```js
function User(name) {
  if (!new.target) {
    return new User(name); // allow calling without new
  }
  this.name = name;
}

class Shape {
  constructor() {
    if (new.target === Shape) {
      throw new TypeError("Shape is abstract and can't be created directly");
    }
  }
}

class Circle extends Shape {}
new Circle(); // ok
new Shape(); // TypeError
```

### 316: How do you extend built-in classes like Array or Error, and what are the pitfalls?

With `class extends` you can subclass built-ins properly, because the built-in constructor creates the object with the right internal slots.

```js
class Stack extends Array {
  peek() {
    return this.at(-1);
  }
}

const s = new Stack();
s.push(1, 2);
s.peek(); // 2
s.length; // 2
Array.isArray(s); // true
```

Pitfalls:

- `new Stack(3)` creates an empty array of length 3, because the `Array` constructor treats a single number as length.
- Methods like `map` and `filter` return a `Stack` (through `Symbol.species`), which can call your constructor with unexpected arguments.
- When compiling to ES5 (old Babel/TypeScript targets), subclassing built-ins breaks.

### 317: What is a "home object" and how does super work in object literals?

Methods defined with the method shorthand get a hidden `[[HomeObject]]` that points to the object they were defined in. `super` uses it to find the parent prototype.

```js
const animal = {
  speak() {
    return "generic sound";
  },
};

const dog = {
  __proto__: animal,
  speak() {
    return `${super.speak()} -> woof`;
  },
};

dog.speak(); // "generic sound -> woof"
```

The home object is fixed when the method is created. If you copy the method to another object, `super` still refers to the original object's prototype. Methods written as `speak: function () {}` don't have a home object, so `super` causes a SyntaxError there.

### 318: What happens when you assign to a property that exists on the prototype?

It depends on the property on the prototype:

- **Normal data property**: a new own property is created on the object (shadowing). The prototype is not changed.
- **Non-writable data property**: the assignment fails (silently, or with a TypeError in strict mode).
- **Setter**: the setter on the prototype is called with `this` set to the object. No own property is created.

```js
"use strict";
const proto = {};
Object.defineProperty(proto, "id", { value: 1, writable: false });
Object.defineProperty(proto, "name", {
  set(v) {
    this._name = v.toUpperCase();
  },
});

const obj = Object.create(proto);
obj.name = "ann";
obj._name; // "ANN"
Object.hasOwn(obj, "name"); // false

obj.id = 2; // TypeError: Cannot assign to read only property
```

If you really need an own property in these cases, use `Object.defineProperty(obj, ...)`.

### 319: What are WeakRef and FinalizationRegistry?

- `WeakRef` holds a weak reference to an object. You call `deref()` to get the object, which returns `undefined` if it has been garbage collected.
- `FinalizationRegistry` lets you register a callback that may run after an object is collected.

```js
const cache = new Map();
const registry = new FinalizationRegistry((key) => {
  const ref = cache.get(key);
  if (ref && !ref.deref()) cache.delete(key);
});

function getImage(url) {
  const cached = cache.get(url)?.deref();
  if (cached) return cached;

  const img = loadBigImage(url);
  cache.set(url, new WeakRef(img));
  registry.register(img, url);
  return img;
}
```

Use them carefully. Garbage collection timing is not predictable, finalizers may never run, and the behavior can differ between engines. Don't use them for required cleanup logic like closing files.

### 320: What is explicit resource management (using and await using)?

The `using` declaration makes sure a resource is cleaned up when the block ends, even if an error is thrown. The object must have a `[Symbol.dispose]()` method (or `[Symbol.asyncDispose]()` for `await using`). It's supported in recent Chrome, Firefox, Node.js and TypeScript 5.2+.

```js
class FileHandle {
  constructor(path) {
    this.path = path;
    console.log("open", path);
  }
  [Symbol.dispose]() {
    console.log("close", this.path);
  }
}

function readConfig() {
  using file = new FileHandle("config.json");
  // work with file
  return "data";
} // "close config.json" runs here automatically

async function query() {
  await using conn = await db.connect(); // needs [Symbol.asyncDispose]
  return conn.query("SELECT 1");
}
```

Resources are disposed in reverse order of declaration. It replaces many `try...finally` blocks.

### 321: What are DisposableStack and AsyncDisposableStack?

They collect several cleanup actions and run them together, in reverse order, when the stack is disposed. This is useful when resources are created conditionally or when you work with APIs that don't have `Symbol.dispose`.

```js
function setup() {
  using stack = new DisposableStack();

  const timer = setInterval(tick, 1000);
  stack.defer(() => clearInterval(timer));

  const ac = new AbortController();
  window.addEventListener("resize", onResize, { signal: ac.signal });
  stack.defer(() => ac.abort());

  const conn = stack.use(openConnection()); // must have Symbol.dispose

  // to keep resources alive past this block:
  return stack.move();
}
```

`stack.move()` transfers ownership to a new stack, so the resources are not disposed at the end of `setup`.

### 322: What are decorators in JavaScript?

Decorators are functions that change or wrap classes and their members. They are a Stage 3 TC39 proposal, supported by TypeScript 5.0+ and Babel. Native support in engines is still in progress.

```js
function logged(value, context) {
  if (context.kind === "method") {
    return function (...args) {
      console.log(`Calling ${String(context.name)} with`, args);
      return value.call(this, ...args);
    };
  }
}

function bound(value, context) {
  context.addInitializer(function () {
    this[context.name] = this[context.name].bind(this);
  });
}

class Calculator {
  @logged
  @bound
  add(a, b) {
    return a + b;
  }
}
```

A decorator gets the decorated value and a `context` object with `kind`, `name`, `static`, `private`, `access` and `addInitializer`. These standard decorators are different from TypeScript's older `experimentalDecorators`.

### 323: What is the accessor keyword?

`accessor` (part of the decorators proposal) creates a private storage field plus a public getter and setter in one line. It is mainly used together with decorators.

```js
class User {
  accessor name = "Ann";
}

// roughly the same as:
class User2 {
  #name = "Ann";
  get name() {
    return this.#name;
  }
  set name(v) {
    this.#name = v;
  }
}
```

Decorators on accessors can intercept reads and writes, which is how libraries implement observable or validated fields.

### 324: How would you implement Promise from scratch?

A minimal version that supports `then`, chaining, thenable adoption and async callbacks:

```js
class MyPromise {
  #state = "pending";
  #value;
  #handlers = [];

  constructor(executor) {
    const resolve = (value) => this.#resolve(value);
    const reject = (reason) => this.#settle("rejected", reason);
    try {
      executor(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  #resolve(value) {
    if (this.#state !== "pending") return;
    if (value === this) return this.#settle("rejected", new TypeError("Cycle"));
    if (value && (typeof value === "object" || typeof value === "function")) {
      let then;
      try {
        then = value.then;
      } catch (err) {
        return this.#settle("rejected", err);
      }
      if (typeof then === "function") {
        let called = false;
        try {
          then.call(
            value,
            (v) => {
              if (!called) {
                called = true;
                this.#resolve(v);
              }
            },
            (r) => {
              if (!called) {
                called = true;
                this.#settle("rejected", r);
              }
            },
          );
        } catch (err) {
          if (!called) this.#settle("rejected", err);
        }
        return;
      }
    }
    this.#settle("fulfilled", value);
  }

  #settle(state, value) {
    if (this.#state !== "pending") return;
    this.#state = state;
    this.#value = value;
    this.#handlers.forEach((h) => this.#run(h));
    this.#handlers = [];
  }

  #run({ onFulfilled, onRejected, resolve, reject }) {
    queueMicrotask(() => {
      const cb = this.#state === "fulfilled" ? onFulfilled : onRejected;
      if (typeof cb !== "function") {
        return this.#state === "fulfilled"
          ? resolve(this.#value)
          : reject(this.#value);
      }
      try {
        resolve(cb(this.#value));
      } catch (err) {
        reject(err);
      }
    });
  }

  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {
      const handler = { onFulfilled, onRejected, resolve, reject };
      if (this.#state === "pending") this.#handlers.push(handler);
      else this.#run(handler);
    });
  }

  catch(onRejected) {
    return this.then(undefined, onRejected);
  }

  finally(fn) {
    return this.then(
      (v) => MyPromise.resolve(fn()).then(() => v),
      (r) =>
        MyPromise.resolve(fn()).then(() => {
          throw r;
        }),
    );
  }

  static resolve(v) {
    return v instanceof MyPromise ? v : new MyPromise((res) => res(v));
  }

  static reject(r) {
    return new MyPromise((_, rej) => rej(r));
  }
}
```

Key points an interviewer looks for: state can change only once, callbacks always run asynchronously (microtasks), `then` returns a new promise, and returned promises or thenables are unwrapped.

### 325: How would you implement Promise.all?

```js
function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const items = Array.from(iterable);
    const results = new Array(items.length);
    let remaining = items.length;

    if (remaining === 0) return resolve([]);

    items.forEach((item, index) => {
      Promise.resolve(item).then((value) => {
        results[index] = value;
        remaining--;
        if (remaining === 0) resolve(results);
      }, reject);
    });
  });
}

await promiseAll([1, Promise.resolve(2), fetchThing()]);
```

Important details: keep results in the original order, handle non-promise values with `Promise.resolve`, resolve immediately for an empty input, and reject on the first failure.

### 326: How would you implement Promise.allSettled and Promise.any?

```js
function allSettled(iterable) {
  return Promise.all(
    Array.from(iterable, (p) =>
      Promise.resolve(p).then(
        (value) => ({ status: "fulfilled", value }),
        (reason) => ({ status: "rejected", reason }),
      ),
    ),
  );
}

function any(iterable) {
  return new Promise((resolve, reject) => {
    const items = Array.from(iterable);
    const errors = new Array(items.length);
    let remaining = items.length;

    if (remaining === 0) {
      return reject(new AggregateError([], "All promises were rejected"));
    }

    items.forEach((item, i) => {
      Promise.resolve(item).then(resolve, (err) => {
        errors[i] = err;
        if (--remaining === 0) {
          reject(new AggregateError(errors, "All promises were rejected"));
        }
      });
    });
  });
}
```

### 327: How do you limit the number of concurrent async operations?

Run a fixed number of "workers" that pull tasks from a shared list.

```js
async function mapWithLimit(items, limit, fn) {
  const results = new Array(items.length);
  let next = 0;

  async function worker() {
    while (next < items.length) {
      const index = next++;
      results[index] = await fn(items[index], index);
    }
  }

  const workers = Array.from({ length: Math.min(limit, items.length) }, worker);
  await Promise.all(workers);
  return results;
}

const urls = Array.from({ length: 50 }, (_, i) => `/api/item/${i}`);
const data = await mapWithLimit(urls, 5, (url) =>
  fetch(url).then((r) => r.json()),
);
```

Because JavaScript is single-threaded, `next++` can't be hit by two workers at the same time, so there's no race on the index.

### 328: How do you implement retry with exponential backoff?

```js
async function retry(fn, { retries = 3, baseDelay = 300, signal } = {}) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn(attempt);
    } catch (err) {
      if (attempt >= retries || signal?.aborted) throw err;

      const delay = baseDelay * 2 ** attempt;
      const jitter = Math.random() * delay * 0.3;
      await new Promise((r) => setTimeout(r, delay + jitter));
    }
  }
}

const data = await retry(
  async () => {
    const res = await fetch("/api/unstable");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  },
  { retries: 4 },
);
```

The random jitter stops many clients from retrying at exactly the same time. In real code you should only retry errors that make sense to retry (network errors, 429, 503), not things like 400 or 401.

### 329: How do you handle race conditions in async UI code?

A typical example: the user types fast, several search requests go out, and an older response arrives after a newer one, showing wrong results.

Fix 1: cancel the old request with `AbortController`.

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

Fix 2: ignore responses that are not the latest.

```js
let latestId = 0;

async function search2(query) {
  const id = ++latestId;
  const data = await fetchResults(query);
  if (id !== latestId) return; // stale
  render(data);
}
```

### 330: How would you implement a debounce with leading, trailing and cancel options?

```js
function debounce(fn, wait, { leading = false, trailing = true } = {}) {
  let timer = null;
  let lastArgs;
  let lastThis;

  function invoke() {
    fn.apply(lastThis, lastArgs);
    lastArgs = lastThis = undefined;
  }

  function debounced(...args) {
    lastArgs = args;
    lastThis = this;
    const isFirstCall = timer === null;

    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = null;
      if (trailing && lastArgs) invoke();
    }, wait);

    if (leading && isFirstCall) invoke();
  }

  debounced.cancel = () => {
    clearTimeout(timer);
    timer = null;
    lastArgs = lastThis = undefined;
  };

  debounced.flush = () => {
    if (timer !== null && lastArgs) {
      clearTimeout(timer);
      timer = null;
      invoke();
    }
  };

  return debounced;
}
```

When `leading` is used, the call that runs right away clears `lastArgs`, so the trailing call only happens if more calls came in during the wait.

### 331: How would you implement an LRU cache?

A `Map` keeps insertion order, so you can move an item to the end on every access and remove from the start when the cache is full.

```js
class LRUCache {
  #max;
  #map = new Map();

  constructor(max) {
    this.#max = max;
  }

  get(key) {
    if (!this.#map.has(key)) return undefined;
    const value = this.#map.get(key);
    this.#map.delete(key);
    this.#map.set(key, value); // move to most recent
    return value;
  }

  set(key, value) {
    this.#map.delete(key);
    this.#map.set(key, value);
    if (this.#map.size > this.#max) {
      const oldest = this.#map.keys().next().value;
      this.#map.delete(oldest);
    }
  }
}

const cache = new LRUCache(2);
cache.set("a", 1);
cache.set("b", 2);
cache.get("a"); // 1, "a" is now most recent
cache.set("c", 3); // removes "b"
cache.get("b"); // undefined
```

All operations are O(1).

### 332: How would you write a deep clone function that handles circular references?

```js
function deepClone(value, seen = new WeakMap()) {
  if (value === null || typeof value !== "object") return value;
  if (seen.has(value)) return seen.get(value);

  if (value instanceof Date) return new Date(value);
  if (value instanceof RegExp) return new RegExp(value.source, value.flags);

  if (value instanceof Map) {
    const result = new Map();
    seen.set(value, result);
    value.forEach((v, k) => result.set(deepClone(k, seen), deepClone(v, seen)));
    return result;
  }

  if (value instanceof Set) {
    const result = new Set();
    seen.set(value, result);
    value.forEach((v) => result.add(deepClone(v, seen)));
    return result;
  }

  const result = Array.isArray(value)
    ? []
    : Object.create(Object.getPrototypeOf(value));
  seen.set(value, result);

  for (const key of Reflect.ownKeys(value)) {
    result[key] = deepClone(value[key], seen);
  }
  return result;
}

const a = { name: "a", list: [1, 2] };
a.self = a;
const b = deepClone(a);
b.self === b; // true
b.list !== a.list; // true
```

Unlike `structuredClone`, this keeps the prototype and copies symbol keys. In practice, prefer `structuredClone` unless you need these extras.

### 333: How do you deep freeze an object?

```js
function deepFreeze(obj, seen = new WeakSet()) {
  if (obj === null || typeof obj !== "object" || seen.has(obj)) return obj;
  seen.add(obj);

  for (const key of Reflect.ownKeys(obj)) {
    deepFreeze(obj[key], seen);
  }
  return Object.freeze(obj);
}

const config = deepFreeze({ db: { host: "localhost", ports: [5432] } });
config.db.ports.push(1); // TypeError: Cannot add property 1, object is not extensible
```

Note that freezing doesn't stop changes inside a `Map`, `Set` or `Date`, because their data lives in internal slots, not properties.

### 334: How would you implement Function.prototype.bind?

```js
Function.prototype.myBind = function (thisArg, ...boundArgs) {
  const target = this;
  if (typeof target !== "function") {
    throw new TypeError("Bind must be called on a function");
  }

  function bound(...args) {
    // when called with new, ignore thisArg
    if (new.target) {
      return Reflect.construct(target, [...boundArgs, ...args], new.target);
    }
    return target.apply(thisArg, [...boundArgs, ...args]);
  }

  if (target.prototype) {
    bound.prototype = Object.create(target.prototype);
  }
  return bound;
};

function greet(greeting, name) {
  return `${greeting}, ${name}. I am ${this.me}`;
}

const g = greet.myBind({ me: "bot" }, "Hello");
g("Ann"); // "Hello, Ann. I am bot"
```

The `new` handling is the part most people forget: a bound function used as a constructor ignores the bound `this`.

### 335: How would you implement call and apply?

```js
Function.prototype.myCall = function (thisArg, ...args) {
  thisArg = thisArg == null ? globalThis : Object(thisArg);
  const key = Symbol("fn");
  thisArg[key] = this;
  try {
    return thisArg[key](...args);
  } finally {
    delete thisArg[key];
  }
};

Function.prototype.myApply = function (thisArg, args = []) {
  return this.myCall(thisArg, ...args);
};

function show(x) {
  return `${this.name} ${x}`;
}
show.myCall({ name: "Ann" }, 1); // "Ann 1"
show.myApply({ name: "Bob" }, [2]); // "Bob 2"
```

Using a `Symbol` as the temporary key avoids overwriting an existing property. This version follows sloppy-mode rules (`null` becomes `globalThis`, primitives get boxed). A real `call` passes `thisArg` through unchanged to strict functions.

### 336: How would you implement instanceof?

```js
function myInstanceOf(obj, Constructor) {
  if (typeof Constructor !== "function") {
    throw new TypeError("Right side must be callable");
  }
  if (
    typeof Constructor[Symbol.hasInstance] === "function" &&
    Constructor[Symbol.hasInstance] !== Function.prototype[Symbol.hasInstance]
  ) {
    return Boolean(Constructor[Symbol.hasInstance](obj));
  }
  if (obj === null || (typeof obj !== "object" && typeof obj !== "function")) {
    return false;
  }

  const target = Constructor.prototype;
  let proto = Object.getPrototypeOf(obj);
  while (proto !== null) {
    if (proto === target) return true;
    proto = Object.getPrototypeOf(proto);
  }
  return false;
}

myInstanceOf([], Array); // true
myInstanceOf([], Object); // true
myInstanceOf(1, Number); // false
```

### 337: How do live bindings work in ES modules?

Imported names are live references to the exported variables, not copies. If the exporting module changes the variable, importers see the new value. Importers can't assign to them.

```js
// counter.js
export let count = 0;
export function increment() {
  count++;
}

// main.js
import { count, increment } from "./counter.js";
console.log(count); // 0
increment();
console.log(count); // 1
count = 5; // TypeError: Assignment to constant variable
```

In CommonJS, `const { count } = require("./counter")` copies the value at that moment, so it doesn't update.

### 338: What happens with circular dependencies in ES modules?

ES modules handle cycles because bindings are created before any module code runs. But if a module reads an import from a module that hasn't finished running yet, it can hit the TDZ.

```js
// a.js
import { b } from "./b.js";
export const a = "A";
console.log("a sees", b);

// b.js
import { a } from "./a.js";
export const b = "B";
console.log("b sees", a); // ReferenceError: Cannot access 'a' before initialization
```

If `main.js` imports `a.js`, then `b.js` runs first (it's a dependency of `a`), and at that point `a` hasn't been initialized.

Ways to fix it:

- Move shared code into a third module.
- Only access imports inside functions that run later, not at the top level.
- Use function declarations, which are hoisted and ready even during a cycle.

### 339: In what order are ES modules evaluated?

The module graph is loaded and linked first. Then modules are evaluated depth-first, in post-order: a module's dependencies run before the module itself, in the order of the `import` statements. Each module runs only once, no matter how many times it's imported.

```js
// main.js
import "./a.js";
import "./b.js";
console.log("main");

// a.js
import "./c.js";
console.log("a");

// b.js
import "./c.js";
console.log("b");

// c.js
console.log("c");

// Output: c, a, b, main
```

With top-level await, a module that awaits pauses its dependents, but sibling modules that don't depend on it can still run.

### 340: What is import.meta?

`import.meta` is an object with information about the current module. What's in it depends on the environment.

```js
import.meta.url; // "file:///project/src/app.js" or "https://site.com/app.js"

// load a file next to this module
const data = new URL("./data.json", import.meta.url);

// resolve a module specifier
import.meta.resolve("./utils.js");

// Node.js 20.11+
import.meta.dirname; // "/project/src"
import.meta.filename; // "/project/src/app.js"

// Vite
import.meta.env.MODE;
```

`import.meta.dirname` and `filename` replace `__dirname` and `__filename`, which don't exist in ES modules.

### 341: What are import maps?

Import maps let the browser resolve bare module names (like `"lodash"`) to URLs without a bundler.

```html
<script type="importmap">
  {
    "imports": {
      "lodash/": "https://cdn.jsdelivr.net/npm/lodash-es@4.17.21/",
      "app/": "/js/"
    }
  }
</script>

<script type="module">
  import debounce from "lodash/debounce.js";
  import { start } from "app/main.js";
</script>
```

They also support `scopes` (different mappings for different parts of the app) and `integrity` for subresource integrity checks.

### 342: What is the difference between process.nextTick, queueMicrotask, setImmediate and setTimeout in Node.js?

- `process.nextTick(cb)`: runs before other microtasks, right after the current operation. Overusing it can block the event loop.
- `queueMicrotask(cb)` / promise callbacks: run in the microtask queue, after `nextTick` callbacks.
- `setImmediate(cb)`: runs in the "check" phase of the event loop, after I/O callbacks.
- `setTimeout(cb, 0)`: runs in the "timers" phase, after at least 1 ms.

```js
setTimeout(() => console.log("timeout"), 0);
setImmediate(() => console.log("immediate"));
Promise.resolve().then(() => console.log("promise"));
process.nextTick(() => console.log("nextTick"));
console.log("sync");

// sync, nextTick, promise, then timeout/immediate (order of these two can vary)
```

Inside an I/O callback, `setImmediate` always runs before `setTimeout(0)`.

### 343: What are the phases of the Node.js event loop?

Node.js uses libuv. Each loop iteration goes through these phases:

1. **timers**: callbacks from `setTimeout` and `setInterval` that are due.
2. **pending callbacks**: some system-level I/O callbacks.
3. **idle, prepare**: internal use.
4. **poll**: get new I/O events and run their callbacks. The loop may wait here.
5. **check**: `setImmediate` callbacks.
6. **close callbacks**: like `socket.on("close")`.

Between each callback, Node runs all `process.nextTick` callbacks and then all microtasks.

### 344: What is backpressure in streams?

Backpressure happens when data is produced faster than it can be consumed. Without handling it, data piles up in memory.

In Node.js streams, `write()` returns `false` when the internal buffer is full. You should stop writing until the `drain` event fires. `pipe()` and `pipeline()` handle this for you.

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("big.log"),
  createGzip(),
  createWriteStream("big.log.gz"),
);
```

Web Streams (`ReadableStream`, `WritableStream`) handle backpressure through a queue and `highWaterMark`. `pipeTo` and `pipeThrough` respect it automatically.

### 345: How do Web Streams work?

Web Streams are a standard API (browsers, Node.js, Deno, Bun) for processing data in chunks.

- `ReadableStream`: a source of data
- `WritableStream`: a destination
- `TransformStream`: changes data as it passes through

```js
const res = await fetch("/large.txt");

const upper = new TransformStream({
  transform(chunk, controller) {
    controller.enqueue(chunk.toUpperCase());
  },
});

const reader = res.body
  .pipeThrough(new TextDecoderStream())
  .pipeThrough(upper)
  .getReader();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  console.log(value);
}
```

There are built-in transforms too, like `TextDecoderStream`, `TextEncoderStream`, `CompressionStream` and `DecompressionStream`.

### 346: How do you create your own ReadableStream?

```js
function numberStream(max) {
  let i = 0;
  return new ReadableStream({
    pull(controller) {
      if (i >= max) {
        controller.close();
        return;
      }
      controller.enqueue(i++);
    },
    cancel(reason) {
      console.log("cancelled:", reason);
    },
  });
}

for await (const n of numberStream(3)) {
  console.log(n); // 0, 1, 2
}

// or from any iterable
const stream = ReadableStream.from(["a", "b", "c"]);
```

`pull` is called only when the consumer wants more data, which gives you backpressure for free.

### 347: What is SharedArrayBuffer and Atomics?

`SharedArrayBuffer` is memory that can be shared between the main thread and workers. Without it, data sent with `postMessage` is copied (or transferred).

Because several threads can access it at once, you use `Atomics` to read and write safely and to wait for or wake other threads.

```js
// main.js
const shared = new SharedArrayBuffer(4);
const counter = new Int32Array(shared);
worker.postMessage(shared);

Atomics.add(counter, 0, 1);
Atomics.notify(counter, 0);

// worker.js
self.onmessage = ({ data }) => {
  const counter = new Int32Array(data);
  Atomics.wait(counter, 0, 0); // block until value is not 0 (not allowed on main thread)
  console.log("value:", Atomics.load(counter, 0));
};
```

Browsers only allow `SharedArrayBuffer` on cross-origin isolated pages (using `COOP` and `COEP` headers), because of Spectre-style attacks. `Atomics.waitAsync` is a non-blocking version that returns a promise and can be used on the main thread.

### 348: What are typed arrays and when should you use them?

Typed arrays are array-like views over raw binary data in an `ArrayBuffer`. Each one has a fixed number type.

```js
const buffer = new ArrayBuffer(8);
const bytes = new Uint8Array(buffer);
const ints = new Int32Array(buffer);

ints[0] = 258;
bytes; // Uint8Array [2, 1, 0, 0, 0, 0, 0, 0] (little-endian)

new Float32Array([1.5, 2.5]);
new Float16Array([1.5]); // ES2025
new BigInt64Array([1n]);

const clamped = new Uint8ClampedArray([300, -5]); // [255, 0]
```

Use them for binary files, WebGL/WebGPU, audio, images, network protocols and WebAssembly memory. They are fixed length and much faster than normal arrays for numeric work.

### 349: What is DataView?

`DataView` lets you read and write different number types at any byte offset in an `ArrayBuffer`, and choose the byte order (endianness). This is useful for parsing binary formats.

```js
const buffer = new ArrayBuffer(6);
const view = new DataView(buffer);

view.setUint16(0, 0xcafe); // big-endian by default
view.setUint32(2, 1234, true); // little-endian

view.getUint16(0).toString(16); // "cafe"
view.getUint32(2, true); // 1234
```

Typed arrays always use the machine's byte order (almost always little-endian), so use `DataView` when the format defines a specific order, like network protocols.

### 350: What are resizable ArrayBuffers and ArrayBuffer.transfer?

Since ES2024, an `ArrayBuffer` can be created as resizable, and buffers can be transferred (ownership moved, old buffer becomes detached).

```js
const buf = new ArrayBuffer(8, { maxByteLength: 64 });
buf.resizable; // true
buf.resize(32);
buf.byteLength; // 32

const view = new Uint8Array(buf); // length-tracking view grows with the buffer

const moved = buf.transfer(); // new buffer with the same memory
buf.detached; // true
buf.byteLength; // 0
moved.byteLength; // 32

const fixedCopy = moved.transferToFixedLength();
```

Transferring avoids copying large data, and detaching the old buffer prevents accidental use of memory that now belongs to someone else.

### 351: What are transferable objects?

Transferable objects can be moved between threads (with `postMessage` or `structuredClone`) instead of copied. After the transfer, the sender can no longer use them.

Examples: `ArrayBuffer`, `MessagePort`, `ImageBitmap`, `OffscreenCanvas`, `ReadableStream`, `WritableStream`, `TransformStream`.

```js
const buffer = new ArrayBuffer(100_000_000); // 100 MB

worker.postMessage({ buffer }, [buffer]); // transfer list
buffer.byteLength; // 0, it's detached now

const copy = structuredClone(buffer2, { transfer: [buffer2] });
```

Transferring a large buffer is almost instant, while copying it takes time and doubles memory use.

### 352: What are MessageChannel and BroadcastChannel?

- `MessageChannel` creates two connected ports. Messages sent on one port arrive at the other. It is used for private communication, for example between an iframe and its parent, or between workers.
- `BroadcastChannel` sends messages to every browsing context (tabs, iframes, workers) of the same origin that joined the same channel name.

```js
// MessageChannel
const { port1, port2 } = new MessageChannel();
port1.onmessage = (e) => console.log("got", e.data);
port2.postMessage("hello");

// BroadcastChannel: sync logout across tabs
const channel = new BroadcastChannel("auth");
channel.postMessage({ type: "logout" });
channel.onmessage = (e) => {
  if (e.data.type === "logout") location.href = "/login";
};
```

`MessageChannel` is also used by some libraries (including React's scheduler) to queue macrotasks without the minimum delay of `setTimeout`.

### 353: How do you communicate safely with an iframe using postMessage?

Always set the target origin when sending, and always check `event.origin` when receiving.

```js
// parent page
const frame = document.querySelector("iframe");
frame.contentWindow.postMessage(
  { type: "init", token },
  "https://widget.example.com",
);

// inside the iframe
window.addEventListener("message", (event) => {
  if (event.origin !== "https://app.example.com") return; // ignore others
  if (event.data?.type === "init") {
    // ...
  }
});
```

Using `"*"` as the target origin can leak data to whatever page is loaded in the frame. Not checking `event.origin` lets any site send you commands.

### 354: How does JavaScript engine optimization work (JIT compilation)?

Modern engines (V8, SpiderMonkey, JavaScriptCore) don't just interpret code. In V8, roughly:

1. **Ignition** (interpreter) turns the code into bytecode and runs it, collecting type feedback.
2. **Sparkplug** quickly compiles bytecode to machine code without optimization.
3. **Maglev** (mid-tier optimizer) makes reasonably fast code using the feedback.
4. **TurboFan** (top-tier optimizer) makes highly optimized machine code for hot functions, based on assumptions like "this argument is always a small integer".

If an assumption turns out wrong (for example a function suddenly gets a string), the engine **deoptimizes** and falls back to slower code.

The practical lesson: functions that always receive the same types of values run faster.

### 355: What are hidden classes (shapes) and inline caches?

Engines give each object a hidden "shape" that describes its properties and their memory offsets. Objects created the same way share a shape, so property access becomes a quick offset lookup.

An **inline cache** remembers the shape seen at a property access site. If the next object has the same shape, the lookup is very fast.

- **Monomorphic**: one shape seen. Fastest.
- **Polymorphic**: a few shapes (up to 4 in V8). Still OK.
- **Megamorphic**: many shapes. Slow, the cache gives up.

```js
// same shape: good
function Point(x, y) {
  this.x = x;
  this.y = y;
}

// different shapes because of property order and additions
const a = { x: 1, y: 2 };
const b = { y: 2, x: 1 }; // different order -> different shape
const c = { x: 1 };
c.y = 2; // shape transition
```

Tips: initialize all properties in the constructor, in the same order, and avoid `delete` on hot objects.

### 356: What are "elements kinds" in V8 and why do they matter for arrays?

V8 tracks what kind of values an array holds to store it efficiently. From most to least efficient:

- `PACKED_SMI_ELEMENTS`: only small integers, no holes
- `PACKED_DOUBLE_ELEMENTS`: numbers including decimals
- `PACKED_ELEMENTS`: any values
- and `HOLEY_` versions of each when the array has holes

Transitions only go one way (to more general kinds). An array never goes back to a more specific kind.

```js
const arr = [1, 2, 3]; // PACKED_SMI
arr.push(4.5); // PACKED_DOUBLE
arr.push("x"); // PACKED_ELEMENTS
arr[10] = 1; // HOLEY_ELEMENTS
```

Tips: avoid holes, don't read past the end of arrays, and keep arrays of one type when performance matters.

### 357: How do you measure performance in JavaScript?

```js
// High-resolution time
const t0 = performance.now();
doWork();
console.log(`took ${performance.now() - t0} ms`);

// User Timing marks, visible in DevTools Performance panel
performance.mark("parse-start");
parse();
performance.mark("parse-end");
performance.measure("parse", "parse-start", "parse-end");

// Observe long tasks and other entries
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log(entry.name, entry.duration);
  }
}).observe({ type: "longtask", buffered: true });
```

For real decisions, use the DevTools Performance and Memory panels, Lighthouse, and real-user data (Core Web Vitals). Micro-benchmarks are often misleading because of JIT warm-up and dead-code elimination.

### 358: What are Core Web Vitals and how does JavaScript affect them?

Core Web Vitals are Google's main metrics for user experience:

- **LCP (Largest Contentful Paint)**: how fast the main content shows. Good: under 2.5 s. Hurt by render-blocking JS and large bundles.
- **INP (Interaction to Next Paint)**: how fast the page responds to clicks and key presses, across the whole visit. Good: under 200 ms. Hurt by long tasks on the main thread. INP replaced FID in 2024.
- **CLS (Cumulative Layout Shift)**: how much content jumps around. Good: under 0.1. Hurt by injecting content without reserved space.

You can measure them with the `web-vitals` library or `PerformanceObserver`.

### 359: What is a long task and how do you break it up?

A long task is any main-thread work that takes more than 50 ms. While it runs, the page can't respond to input or render.

Break it into smaller pieces and yield to the browser between them:

```js
async function processAll(items) {
  for (let i = 0; i < items.length; i++) {
    process(items[i]);

    if (i % 100 === 0) {
      await yieldToMain();
    }
  }
}

function yieldToMain() {
  if (globalThis.scheduler?.yield) {
    return scheduler.yield(); // keeps priority, resumes before other tasks
  }
  return new Promise((resolve) => setTimeout(resolve, 0));
}
```

For truly heavy work, move it to a Web Worker.

### 360: What is the Scheduler API (scheduler.postTask and scheduler.yield)?

The Prioritized Task Scheduling API lets you queue tasks with a priority and yield to the browser in a smarter way.

```js
scheduler.postTask(() => sendAnalytics(), { priority: "background" });
scheduler.postTask(() => updateUI(), { priority: "user-blocking" });

const controller = new TaskController({ priority: "user-visible" });
scheduler.postTask(doWork, { signal: controller.signal });
controller.setPriority("background");
controller.abort();

async function longJob() {
  for (const chunk of chunks) {
    handle(chunk);
    await scheduler.yield();
  }
}
```

Priorities are `"user-blocking"`, `"user-visible"` (default) and `"background"`. It's supported in Chromium and Firefox. Always feature-detect.

### 361: What is requestIdleCallback?

`requestIdleCallback` runs a callback when the browser is idle, so low-priority work doesn't slow down important work.

```js
const tasks = [/* small pieces of work */];

function work(deadline) {
  while (deadline.timeRemaining() > 0 && tasks.length) {
    runTask(tasks.shift());
  }
  if (tasks.length) requestIdleCallback(work, { timeout: 2000 });
}

requestIdleCallback(work, { timeout: 2000 });
```

The `timeout` option forces the callback to run even if the browser never becomes idle. Safari added support recently, so check before relying on it.

### 362: In what order do rendering steps, requestAnimationFrame and tasks run in the browser?

A simplified browser event loop iteration:

1. Run one task (macrotask), like a click handler or timer.
2. Run all microtasks.
3. If it's time to render (usually every ~16 ms):
   - run `resize` and `scroll` events
   - run `requestAnimationFrame` callbacks
   - recalculate styles and layout
   - run `ResizeObserver` callbacks
   - paint
4. If there's spare time, run `requestIdleCallback` callbacks.

```js
setTimeout(() => console.log("timeout"));
requestAnimationFrame(() => console.log("raf"));
Promise.resolve().then(() => console.log("micro"));
// micro is always first. "timeout" and "raf" order depends on when the next frame is.
```

### 363: What does "don't release Zalgo" mean?

It means a function should be either always synchronous or always asynchronous, never sometimes one and sometimes the other. Mixed behavior causes bugs that depend on timing.

```js
// bad: sync when cached, async otherwise
function getUser(id, cb) {
  if (cache.has(id)) return cb(cache.get(id));
  fetchUser(id).then(cb);
}

let ready = false;
getUser(1, () => console.log(ready)); // true or false depending on cache
ready = true;

// good: always async
function getUserFixed(id) {
  if (cache.has(id)) return Promise.resolve(cache.get(id));
  return fetchUser(id);
}
```

Promises solve this by design: `.then` callbacks always run asynchronously.

### 364: What is a thenable?

A thenable is any object with a `then` method. Promises and `await` treat thenables like promises: they call `then` to get the value.

```js
const thenable = {
  then(resolve, reject) {
    setTimeout(() => resolve("from thenable"), 100);
  },
};

const value = await thenable; // "from thenable"
Promise.resolve(thenable).then(console.log); // "from thenable"
```

This is how promises from different libraries work together. It also means an object with a `then` method that isn't a promise can confuse `await`. For example, returning such an object from an async function makes the engine call its `then`.

### 365: Predict the output of this async ordering puzzle.

```js
async function a1() {
  console.log("a1 start");
  await a2();
  console.log("a1 end");
}

async function a2() {
  console.log("a2");
}

console.log("script start");

setTimeout(() => console.log("setTimeout"), 0);

a1();

new Promise((resolve) => {
  console.log("promise executor");
  resolve();
})
  .then(() => console.log("then 1"))
  .then(() => console.log("then 2"));

console.log("script end");
```

Output:

```
script start
a1 start
a2
promise executor
script end
a1 end
then 1
then 2
setTimeout
```

Why:

- Sync code runs first. `a2()` and the promise executor run synchronously.
- `await a2()` waits for an already-fulfilled promise, so "a1 end" is queued as a microtask before "then 1".
- "then 2" is queued only after "then 1" runs.
- `setTimeout` is a macrotask, so it runs last.

### 366: Why does returning a promise from an async function or then add extra ticks?

When a `.then` callback or an async function returns a promise (or thenable), the outer promise has to "adopt" its state. The spec does this through an extra job (`NewPromiseResolveThenableJob`), which then calls `.then` on the inner promise. That costs two extra microtask ticks.

```js
async function direct() {
  return 1;
}

async function wrapped() {
  return Promise.resolve(1);
}

wrapped().then(() => console.log("wrapped"));
direct().then(() => console.log("direct"));
Promise.resolve()
  .then(() => console.log("tick 1"))
  .then(() => console.log("tick 2"))
  .then(() => console.log("tick 3"));

// direct, tick 1, tick 2, wrapped, tick 3
```

`await somePromise` is cheaper. Since ES2019, `await` on a native promise takes only one tick.

### 367: What is the difference between return await and return in an async function?

In most places they behave the same, but inside `try...catch` they are different:

```js
async function withoutAwait() {
  try {
    return mightReject(); // rejection is NOT caught here
  } catch {
    return "fallback";
  }
}

async function withAwait() {
  try {
    return await mightReject(); // rejection IS caught here
  } catch {
    return "fallback";
  }
}
```

`return await` also keeps the current function in async stack traces. So it's good practice to use `return await` inside `try` blocks. Outside of `try`, it doesn't matter much.

### 368: How do you cancel a promise-based operation?

Promises can't be cancelled by themselves. The standard way is to pass an `AbortSignal` and let the operation check it.

```js
function wait(ms, { signal } = {}) {
  return new Promise((resolve, reject) => {
    signal?.throwIfAborted();

    const id = setTimeout(resolve, ms);
    signal?.addEventListener(
      "abort",
      () => {
        clearTimeout(id);
        reject(signal.reason);
      },
      { once: true },
    );
  });
}

const controller = new AbortController();
wait(5000, { signal: controller.signal }).catch((e) => console.log(e.name)); // "AbortError"
controller.abort();
```

Good practice: reject with `signal.reason`, clean up resources, and check the signal at the start.

### 369: How do generators work as two-way communication (next, return, throw)?

Generators can receive values. The value passed to `next(value)` becomes the result of the `yield` expression that paused the generator.

```js
function* conversation() {
  const name = yield "What is your name?";
  const age = yield `Hi ${name}, how old are you?`;
  return `${name} is ${age}`;
}

const gen = conversation();
gen.next().value; // "What is your name?"
gen.next("Ann").value; // "Hi Ann, how old are you?"
gen.next(30); // { value: "Ann is 30", done: true }
```

- `gen.return(value)` finishes the generator, running any `finally` blocks.
- `gen.throw(error)` throws the error at the paused `yield`, so the generator can catch it.

```js
function* safe() {
  try {
    yield 1;
  } catch (e) {
    console.log("caught", e.message);
    yield "recovered";
  } finally {
    console.log("cleanup");
  }
}

const g = safe();
g.next(); // { value: 1 }
g.throw(new Error("boom")); // logs "caught boom", { value: "recovered" }
g.return("done"); // logs "cleanup", { value: "done", done: true }
```

### 370: How can generators be used to implement async/await-like behavior?

Before `async/await`, libraries like `co` used generators. Each `yield` gives a promise to a runner, which waits for it and sends the result back with `next()`.

```js
function run(generatorFn) {
  return new Promise((resolve, reject) => {
    const gen = generatorFn();

    function step(method, arg) {
      let result;
      try {
        result = gen[method](arg);
      } catch (err) {
        return reject(err);
      }
      if (result.done) return resolve(result.value);
      Promise.resolve(result.value).then(
        (val) => step("next", val),
        (err) => step("throw", err),
      );
    }

    step("next");
  });
}

run(function* () {
  const res = yield fetch("/api/user");
  const user = yield res.json();
  return user.name;
}).then(console.log);
```

This is basically what `async/await` does inside the engine.

### 371: What happens to an iterator when you break out of a for...of loop?

If you `break`, `return` or throw out of a `for...of` loop, JavaScript calls the iterator's `return()` method (if it has one). For generators, this runs `finally` blocks, so cleanup still happens.

```js
function* readLines() {
  console.log("open file");
  try {
    yield "line 1";
    yield "line 2";
    yield "line 3";
  } finally {
    console.log("close file");
  }
}

for (const line of readLines()) {
  console.log(line);
  break;
}
// open file
// line 1
// close file
```

The same applies to `for await...of` with async iterators. This is also why reusing a generator after a `break` gives nothing, because it's already finished.

### 372: What is a trampoline and why is it used?

A trampoline turns deep recursion into a loop to avoid stack overflow. The recursive function returns a function (the next step) instead of calling itself, and the trampoline keeps calling until it gets a value.

```js
function trampoline(fn) {
  return (...args) => {
    let result = fn(...args);
    while (typeof result === "function") {
      result = result();
    }
    return result;
  };
}

const sumTo = trampoline(function inner(n, acc = 0) {
  if (n === 0) return acc;
  return () => inner(n - 1, acc + n);
});

sumTo(1_000_000); // 500000500000, no stack overflow
```

It's needed because most engines don't implement proper tail calls, even though ES2015 includes them in the spec. Only Safari's JavaScriptCore does.

### 373: What is the difference between eval and new Function?

- `eval(code)` runs code in the current scope. It can read and change local variables.
- `new Function(args, body)` creates a function that only sees the global scope.

```js
const x = "global";

function test() {
  const x = "local";
  eval("console.log(x)"); // "local"
  new Function("console.log(x)")(); // "global"
  (0, eval)("console.log(typeof x)"); // indirect eval runs in global scope
}
```

Both are risky with untrusted input (code injection), they make code harder to optimize, and they are usually blocked by a strict Content Security Policy unless you allow `'unsafe-eval'`.

### 374: How does block-level function declaration behave in sloppy mode?

In strict mode, a function declared inside a block is scoped to that block. In sloppy mode, for web compatibility (Annex B of the spec), it's also copied to the function scope as a `var` when the declaration is evaluated.

```js
// sloppy mode
console.log(typeof f); // "undefined" (var-like binding exists but not set yet)
{
  function f() {}
}
console.log(typeof f); // "function"

// strict mode
("use strict");
{
  function g() {}
}
typeof g; // "undefined"
```

Because these rules are confusing, avoid declaring functions in blocks unless you're in strict mode (or a module). Use `const g = () => {}` instead.

### 375: What is the difference between a realm and a context, and why does instanceof fail across iframes?

A realm is a complete JavaScript environment with its own global object and its own set of built-ins (`Array`, `Object`, `Array.prototype` and so on). Each iframe, worker and Node.js `vm` context has its own realm.

An array created in an iframe has the iframe's `Array.prototype`, so `instanceof Array` in the parent returns `false`.

```js
const iframe = document.createElement("iframe");
document.body.append(iframe);
const IframeArray = iframe.contentWindow.Array;

const arr = new IframeArray(1, 2);
arr instanceof Array; // false
Array.isArray(arr); // true
```

That's why there are realm-safe checks like `Array.isArray`, `Error.isError` and private-field brand checks.

### 376: What is Error.isError?

`Error.isError(value)` (ES2026) checks whether a value is a real error object. It works across realms and can't be fooled by changing prototypes, unlike `instanceof Error`.

```js
Error.isError(new TypeError("x")); // true
Error.isError({ message: "fake", name: "Error" }); // false
Error.isError(Object.create(Error.prototype)); // false
Error.isError(iframeWindow.eval("new Error()")); // true
```

This is useful in logging and error-handling libraries that receive values from other realms or workers.

### 377: How do you get better stack traces in JavaScript?

- Throw `Error` objects, not strings.
- Use `cause` to keep the original error when wrapping.
- In V8, `Error.captureStackTrace(obj, fn)` adds a stack to any object and can hide internal frames.
- `Error.stackTraceLimit` controls how many frames are kept (default 10 in V8).
- Async stack traces in DevTools and Node.js show where an `await` chain started, but only when you use `await` (not `.then` chains created elsewhere).

```js
class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.name = "HttpError";
    this.status = status;
    Error.captureStackTrace?.(this, HttpError); // hide the constructor frame
  }
}

Error.stackTraceLimit = 50;
```

### 378: What is the JSON.stringify replacer, space and toJSON?

```js
const user = {
  name: "Ann",
  password: "secret",
  createdAt: new Date("2025-01-01"),
  tags: new Set(["a", "b"]),
};

// replacer function: called for every key/value
JSON.stringify(user, (key, value) => {
  if (key === "password") return undefined; // skip
  if (value instanceof Set) return [...value];
  return value;
});
// '{"name":"Ann","createdAt":"2025-01-01T00:00:00.000Z","tags":["a","b"]}'

// replacer array: whitelist of keys
JSON.stringify(user, ["name"]); // '{"name":"Ann"}'

// space: indentation
JSON.stringify({ a: 1 }, null, 2);

// toJSON: object controls its own output
class Money {
  constructor(cents) {
    this.cents = cents;
  }
  toJSON() {
    return (this.cents / 100).toFixed(2);
  }
}
JSON.stringify({ price: new Money(1999) }); // '{"price":"19.99"}'
```

`Date` uses `toJSON` internally, which is why dates become ISO strings. Note that `toJSON` runs before the replacer, so in the replacer the `createdAt` value is already a string.

### 379: How do you use a JSON.parse reviver?

The reviver is called for every key/value from the deepest level up, and can transform values while parsing.

```js
const json =
  '{"name":"Ann","createdAt":"2025-01-01T00:00:00.000Z","id":"12345678901234567890"}';

const data = JSON.parse(json, (key, value) => {
  if (key === "createdAt") return new Date(value);
  if (key === "id") return BigInt(value);
  return value;
});

data.createdAt instanceof Date; // true
typeof data.id; // "bigint"
```

Large numbers in JSON (not as strings) lose precision before the reviver sees them. Newer engines pass a third `context` argument with `context.source` (the original text of the value) to fix this. Check support before relying on it.

### 380: How do you safely parse numbers that are too large for JavaScript?

Numbers above `Number.MAX_SAFE_INTEGER` lose precision when parsed.

```js
JSON.parse('{"id": 9007199254740993}').id; // 9007199254740992 (wrong)
```

Options:

1. Ask the API to send big IDs as strings (most common, used by Twitter/X, Discord and others).
2. Use the reviver's `context.source` (in engines that support it):

```js
JSON.parse('{"id": 9007199254740993}', (key, value, context) =>
  key === "id" ? BigInt(context.source) : value,
); // { id: 9007199254740993n }
```

3. Use a library like `json-bigint`.

### 381: What is Math.sumPrecise?

`Math.sumPrecise` (ES2026) adds an iterable of numbers without the rounding errors that pile up in a normal loop.

```js
const values = [1e20, 0.1, -1e20];

values.reduce((a, b) => a + b, 0); // 0
Math.sumPrecise(values); // 0.1

Math.sumPrecise([0.1, 0.2]); // 0.30000000000000004 (each number is still a float)
```

It computes the exact mathematical sum of the given floats and rounds only once at the end. It doesn't fix the fact that `0.1` itself is not exact in binary.

It's a new addition, so not every engine has it yet. Check support (for example, Node.js 24 does not have it).

### 382: How do you convert between Uint8Array and base64 or hex?

New built-in methods (ES2026) make this simple and avoid the old `btoa`/`atob` tricks, which only work with Latin-1 strings.

```js
const bytes = new TextEncoder().encode("Hello 👋");

bytes.toBase64(); // "SGVsbG8g8J+Riw=="
bytes.toBase64({ alphabet: "base64url", omitPadding: true });
bytes.toHex(); // "48656c6c6f20f09f918b"

Uint8Array.fromBase64("SGVsbG8g8J+Riw==");
Uint8Array.fromHex("48656c6c6f");

const target = new Uint8Array(16);
target.setFromBase64("SGVsbG8="); // { read: 8, written: 5 }
```

These methods are new, so check support first (for example, Node.js 24 does not have them). For older environments, you'd use `btoa(String.fromCharCode(...bytes))` (fails on large arrays) or `Buffer` in Node.js.

### 383: What is the RegExp v flag?

The `v` flag (ES2024) is an upgraded version of `u`. It adds set operations inside character classes and support for Unicode string properties.

```js
// difference: Greek letters except alpha
/[\p{Script=Greek}--[αΑ]]/v.test("β"); // true

// intersection: ASCII digits only
/[\p{Decimal_Number}&&[0-9]]/v.test("٣"); // false (Arabic-Indic digit)

// emoji that are made of several code points
/^\p{RGI_Emoji}$/v.test("👨‍👩‍👧"); // true

// nested classes
/[[a-z]--[aeiou]]/v.test("b"); // true (consonants)
```

You can't use `u` and `v` together. `v` is stricter about escaping some characters inside classes.

### 384: What are regex modifiers?

Regex modifiers (ES2025) let you turn flags `i`, `m` and `s` on or off for only part of a pattern.

```js
// "hello" is case-insensitive, "WORLD" is case-sensitive
const re = /(?i:hello) WORLD/;

re.test("HeLLo WORLD"); // true
re.test("hello world"); // false

// turn a flag off for a group
/(?-i:A)b/i.test("aB"); // false, A must be uppercase
/(?-i:A)b/i.test("AB"); // true
```

This is useful when you combine patterns from different sources.

### 385: What does the regex d flag (hasIndices) do?

With the `d` flag, match results include an `indices` array with the start and end positions of the full match and each group.

```js
const m = /(?<key>\w+)=(?<val>\w+)/d.exec("color=red");

m.indices[0]; // [0, 9]
m.indices.groups.key; // [0, 5]
m.indices.groups.val; // [6, 9]
```

It's useful for editors, syntax highlighters and error messages that need exact positions.

### 386: How do you write a simple tokenizer using the sticky (y) flag?

The `y` flag makes the regex match only at `lastIndex`, which is perfect for scanning text piece by piece.

```js
function tokenize(input) {
  const rules = [
    ["number", /\d+(?:\.\d+)?/y],
    ["ident", /[a-zA-Z_]\w*/y],
    ["op", /[+\-*/()=]/y],
    ["space", /\s+/y],
  ];

  const tokens = [];
  let pos = 0;

  while (pos < input.length) {
    let matched = false;
    for (const [type, re] of rules) {
      re.lastIndex = pos;
      const m = re.exec(input);
      if (m) {
        if (type !== "space") tokens.push({ type, value: m[0] });
        pos = re.lastIndex;
        matched = true;
        break;
      }
    }
    if (!matched) throw new SyntaxError(`Unexpected "${input[pos]}" at ${pos}`);
  }
  return tokens;
}

tokenize("x = 3.5 * (y + 2)");
```

### 387: What is catastrophic backtracking (ReDoS)?

Some regex patterns take exponential time on certain inputs because the engine tries a huge number of ways to match. Attackers can use this to freeze a server (Regular expression Denial of Service).

```js
const bad = /^(a+)+$/;
bad.test("a".repeat(30) + "!"); // can take a very long time
```

Patterns with nested quantifiers (`(a+)+`, `(a|a)*`, `(\w+\s?)*`) are the usual problem.

How to avoid it:

- Avoid nested quantifiers on overlapping patterns.
- Limit input length before matching.
- Use linting tools that detect unsafe regex.
- In Node.js, consider the non-backtracking engine option (`--enable-experimental-regexp-engine` with the `l` flag) or a library like `re2`.

### 388: Why are tagged template strings arrays cached?

For each tagged template in the source code, the `strings` array passed to the tag function is created once and reused every time that code runs. It is also frozen.

```js
const seen = new Set();
function tag(strings) {
  seen.add(strings);
  return strings;
}

for (let i = 0; i < 3; i++) tag`hello ${i}`;
seen.size; // 1

Object.isFrozen(tag`x`); // true
```

Libraries like `lit-html` use this identity as a cache key, so the template is parsed only once.

### 389: What are Web Components?

Web Components are browser-native, reusable UI elements. They are made of:

- **Custom Elements**: define your own HTML tags.
- **Shadow DOM**: an isolated DOM and CSS scope inside an element.
- **HTML templates and slots**: reusable markup and content placeholders.

```js
class UserCard extends HTMLElement {
  static observedAttributes = ["name"];

  constructor() {
    super();
    this.attachShadow({ mode: "open" }).innerHTML = `
      <style>p { color: steelblue; }</style>
      <p>Hello, <span></span>!</p>
      <slot></slot>
    `;
  }

  attributeChangedCallback(name, oldValue, newValue) {
    this.shadowRoot.querySelector("span").textContent = newValue;
  }

  connectedCallback() {
    console.log("added to page");
  }

  disconnectedCallback() {
    console.log("removed from page");
  }
}

customElements.define("user-card", UserCard);
```

```html
<user-card name="Ann">Extra content</user-card>
```

### 390: What is the difference between open and closed shadow roots?

- `mode: "open"`: outside code can reach the shadow root through `element.shadowRoot`.
- `mode: "closed"`: `element.shadowRoot` returns `null`. Only the component keeps a reference.

```js
const host = document.createElement("div");
const root = host.attachShadow({ mode: "closed" });
host.shadowRoot; // null
```

Closed mode is not real security. Scripts on the page can still patch `attachShadow` before it's called. Most libraries use `open`.

Declarative Shadow DOM lets you create shadow roots in HTML for server rendering:

```html
<my-el>
  <template shadowrootmode="open">
    <p>Rendered on the server</p>
  </template>
</my-el>
```

### 391: How do you prevent XSS in JavaScript applications?

XSS (Cross-Site Scripting) happens when untrusted input is run as code in the page.

Main rules:

- Use `textContent` instead of `innerHTML` for user content.
- Let frameworks escape output (React, Vue, Angular do by default). Be careful with `dangerouslySetInnerHTML`, `v-html` and `[innerHTML]`.
- Sanitize HTML with a library like DOMPurify, or the built-in `setHTML()` from the Sanitizer API where it's supported.
- Validate URLs before using them in `href` or `src` (block `javascript:`).
- Use a strict Content Security Policy.
- Use Trusted Types to block unsafe DOM sinks.
- Set cookies as `HttpOnly` so scripts can't read them.

```js
// unsafe
el.innerHTML = `<p>${userComment}</p>`;

// safe
const p = document.createElement("p");
p.textContent = userComment;
el.append(p);

// safe HTML with sanitizing
el.setHTML(userHtml); // removes scripts and event handlers
```

### 392: What is Content Security Policy (CSP)?

CSP is an HTTP header that tells the browser which sources of scripts, styles, images and so on are allowed. It's a strong second line of defense against XSS.

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-r4nd0m' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';
  frame-ancestors 'none';
```

- Inline scripts are blocked unless they have the right nonce or hash.
- `eval` and `new Function` are blocked unless `'unsafe-eval'` is allowed.
- `frame-ancestors` prevents clickjacking.

Use `Content-Security-Policy-Report-Only` to test a policy without breaking the site.

### 393: What are Trusted Types?

Trusted Types is a browser feature that blocks passing plain strings to dangerous DOM APIs (like `innerHTML`, `eval`, `script.src`). Only special typed objects, created by a policy you define, are accepted.

```
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-policy
```

```js
const policy = trustedTypes.createPolicy("app-policy", {
  createHTML: (input) => DOMPurify.sanitize(input),
});

el.innerHTML = userInput; // TypeError, blocked
el.innerHTML = policy.createHTML(userInput); // allowed, sanitized
```

This moves all the risky HTML handling into a few reviewed places.

### 394: What is CSRF and how do you protect against it?

CSRF (Cross-Site Request Forgery) tricks a logged-in user's browser into sending a request to your site from another site. The browser attaches cookies automatically, so the request looks real.

Protection:

- `SameSite=Lax` or `SameSite=Strict` cookies (Lax is the default in modern browsers).
- CSRF tokens in forms or headers that the attacker can't read.
- Check `Origin` or `Sec-Fetch-Site` headers on the server.
- Don't change state with `GET` requests.

```js
await fetch("/api/transfer", {
  method: "POST",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json",
    "X-CSRF-Token": document.querySelector('meta[name="csrf"]').content,
  },
  body: JSON.stringify({ amount: 100 }),
});
```

### 395: Where should you store authentication tokens in the browser?

There's no perfect answer, but here are the trade-offs:

- **localStorage / sessionStorage**: easy, but any XSS can read the token.
- **In memory (a variable)**: XSS can't read it after the fact as easily, but it's lost on reload.
- **HttpOnly, Secure, SameSite cookie**: JavaScript can't read it, so XSS can't steal it directly. You need CSRF protection.

The common recommendation is to use HttpOnly cookies for session or refresh tokens, and keep short-lived access tokens in memory if you need them. Above all, preventing XSS matters most, because XSS can make requests as the user no matter where the token is stored.

### 396: What is IndexedDB?

IndexedDB is a browser database for storing large amounts of structured data, including files and blobs. It's asynchronous, transactional, supports indexes, and works in workers.

```js
const request = indexedDB.open("app-db", 1);

request.onupgradeneeded = () => {
  const db = request.result;
  const store = db.createObjectStore("notes", { keyPath: "id" });
  store.createIndex("byDate", "createdAt");
};

request.onsuccess = () => {
  const db = request.result;
  const tx = db.transaction("notes", "readwrite");
  tx.objectStore("notes").put({ id: 1, text: "Hello", createdAt: Date.now() });
  tx.oncomplete = () => console.log("saved");
};
```

The raw API is event-based and verbose, so most people use a small wrapper like `idb` or Dexie.

### 397: What is the Cache API and how is it different from HTTP cache?

The Cache API (`caches`) lets your code store and get `Request`/`Response` pairs directly. It's mostly used in Service Workers for offline support.

```js
const cache = await caches.open("v1");
await cache.addAll(["/", "/app.js", "/styles.css"]);

const cached = await cache.match("/app.js");
await caches.delete("old-v0");
```

The HTTP cache is controlled by the browser through headers like `Cache-Control`. You can't read it directly from code. The Cache API is fully under your control: nothing expires unless you delete it.

### 398: What is the difference between WebSocket, Server-Sent Events and long polling?

|                | WebSocket                  | Server-Sent Events                            | Long polling            |
| -------------- | -------------------------- | --------------------------------------------- | ----------------------- |
| Direction      | both ways                  | server to client                              | client asks repeatedly  |
| Protocol       | `ws://`, `wss://`          | normal HTTP                                   | normal HTTP             |
| Auto reconnect | no, you write it           | yes                                           | you write it            |
| Binary data    | yes                        | text only                                     | yes                     |
| Good for       | chat, games, collaboration | notifications, live feeds, AI token streaming | fallback for old setups |

```js
// SSE
const events = new EventSource("/api/stream");
events.onmessage = (e) => console.log(JSON.parse(e.data));

// WebSocket
const ws = new WebSocket("wss://example.com/chat");
ws.onopen = () => ws.send(JSON.stringify({ type: "join" }));
ws.onmessage = (e) => console.log(e.data);
```

WebTransport (over HTTP/3) is a newer option for low-latency two-way communication, mainly in Chromium and Firefox.

### 399: How do you stream a response from a server with fetch?

`response.body` is a `ReadableStream`, so you can process data as it arrives instead of waiting for the whole response. This is how chat apps show AI responses word by word.

```js
const res = await fetch("/api/chat", {
  method: "POST",
  body: JSON.stringify({ prompt: "Hi" }),
  headers: { "Content-Type": "application/json" },
});

const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();

let text = "";
while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  text += value;
  output.textContent = text;
}
```

### 400: What is the difference between structuredClone and postMessage serialization?

They use the same algorithm (the structured clone algorithm). `postMessage` sends the copy to another context (worker, iframe, window), while `structuredClone` makes the copy in the same context.

What can be cloned: primitives (except symbols), plain objects, arrays, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, typed arrays, `Blob`, `File`, `ImageData`, errors, and circular references.

What can't: functions, DOM nodes, symbols, `WeakMap`, `WeakSet`, getters (only the value is copied), class prototypes, and private fields.

```js
structuredClone({ fn() {} }); // DataCloneError
structuredClone(
  new (class A {
    x = 1;
  })(),
); // { x: 1 }, plain object
```

### 401: What is AsyncLocalStorage in Node.js?

`AsyncLocalStorage` stores data that follows an async call chain, like a request ID, without passing it through every function. It works across `await`, timers and callbacks.

```js
import { AsyncLocalStorage } from "node:async_hooks";
import { randomUUID } from "node:crypto";

const requestContext = new AsyncLocalStorage();

function log(message) {
  const ctx = requestContext.getStore();
  console.log(`[${ctx?.requestId ?? "-"}] ${message}`);
}

async function handleRequest(req, res) {
  await requestContext.run({ requestId: randomUUID() }, async () => {
    log("start");
    await loadUser();
    log("done");
  });
}

async function loadUser() {
  await new Promise((r) => setTimeout(r, 10));
  log("loading user"); // still has the same requestId
}
```

Frameworks use it for logging, tracing (OpenTelemetry) and per-request state. A similar feature, `AsyncContext`, is being proposed for the language itself.

### 402: What is the difference between worker_threads, child_process and cluster in Node.js?

- **worker_threads**: threads inside the same process. They can share memory (`SharedArrayBuffer`) and transfer data cheaply. Good for CPU-heavy JavaScript like image processing or parsing.
- **child_process**: starts a separate OS process (`spawn`, `exec`, `fork`). Good for running other programs or isolating crashes.
- **cluster**: forks several Node processes that share the same server port. Used to use all CPU cores for an HTTP server. Today, many teams use a process manager or containers for this instead.

```js
// worker_threads
import {
  Worker,
  isMainThread,
  parentPort,
  workerData,
} from "node:worker_threads";

if (isMainThread) {
  const worker = new Worker(new URL(import.meta.url), { workerData: 40 });
  worker.on("message", (result) => console.log("fib:", result));
} else {
  const fib = (n) => (n < 2 ? n : fib(n - 1) + fib(n - 2));
  parentPort.postMessage(fib(workerData));
}
```

### 403: What is the "exports" field in package.json?

`exports` defines the public entry points of a package. Anything not listed can't be imported from outside. It also supports conditions, so you can serve different files for `import` vs `require`, or for Node vs browsers.

```json
{
  "name": "my-lib",
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./utils": "./dist/utils.js",
    "./package.json": "./package.json"
  },
  "imports": {
    "#internal/*": "./src/internal/*.js"
  }
}
```

Conditions are checked in order, so put `types` first. The `imports` field defines private aliases (starting with `#`) that only work inside the package.

### 404: What is the dual package hazard?

When a package ships both an ESM and a CommonJS build, an app might load both versions at the same time (one through `import`, another through `require`). Then you get two copies of the module state: two singletons, two class definitions, and `instanceof` checks fail between them.

Ways to avoid it:

- Ship ESM only (now possible because modern Node can `require()` ES modules).
- Make the ESM build a thin wrapper that re-exports the CommonJS build, so there's only one real copy.
- Keep state in a separate shared module, or on `globalThis` with a `Symbol.for` key.

### 405: How do you test code that uses timers?

Use fake timers so tests don't actually wait.

```js
// Vitest / Jest
import { vi, test, expect } from "vitest";

test("debounce calls once", () => {
  vi.useFakeTimers();
  const fn = vi.fn();
  const debounced = debounce(fn, 300);

  debounced();
  debounced();
  vi.advanceTimersByTime(299);
  expect(fn).not.toHaveBeenCalled();

  vi.advanceTimersByTime(1);
  expect(fn).toHaveBeenCalledTimes(1);

  vi.useRealTimers();
});
```

Node.js has a built-in test runner with timer mocking too:

```js
import { test, mock } from "node:test";
import assert from "node:assert/strict";

test("timeout fires", () => {
  mock.timers.enable({ apis: ["setTimeout"] });
  const fn = mock.fn();
  setTimeout(fn, 1000);
  mock.timers.tick(1000);
  assert.equal(fn.mock.callCount(), 1);
  mock.timers.reset();
});
```

With promises involved, use the async versions (`vi.advanceTimersByTimeAsync`) so microtasks also get flushed.

### 406: What are signals and how would you implement a basic one?

A signal is a reactive value. When it changes, anything that depends on it (computed values, effects) updates automatically. Solid, Preact, Angular, Vue (refs) and Svelte 5 (runes) all use this idea, and there's a TC39 proposal to add signals to the language (still at an early stage).

```js
let currentObserver = null;

function signal(initial) {
  let value = initial;
  const subscribers = new Set();
  return {
    get() {
      if (currentObserver) subscribers.add(currentObserver);
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
    const prev = currentObserver;
    currentObserver = run;
    try {
      fn();
    } finally {
      currentObserver = prev;
    }
  };
  run();
}

function computed(fn) {
  const s = signal();
  effect(() => s.set(fn()));
  return { get: s.get };
}

const count = signal(1);
const double = computed(() => count.get() * 2);
effect(() => console.log("double is", double.get())); // "double is 2"
count.set(5); // "double is 10"
```

Real libraries add dependency cleanup, batching, lazy evaluation and glitch-free updates.

### 407: How would you implement a minimal Redux-style store?

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

function todos(state = [], action) {
  switch (action.type) {
    case "add":
      return [
        ...state,
        { id: crypto.randomUUID(), text: action.text, done: false },
      ];
    case "toggle":
      return state.map((t) =>
        t.id === action.id ? { ...t, done: !t.done } : t,
      );
    default:
      return state;
  }
}

const store = createStore(todos, []);
store.subscribe(() => console.log(store.getState()));
store.dispatch({ type: "add", text: "Learn JS" });
```

The key ideas: state is read-only, changes happen only through actions, and reducers are pure functions that return new state.

### 408: How does a virtual DOM and diffing work?

A virtual DOM is a lightweight JavaScript object tree that describes the UI. When state changes, a new tree is created and compared ("diffed") with the old one, and only the differences are applied to the real DOM.

```js
const h = (type, props = {}, ...children) => ({
  type,
  props,
  children: children.flat(),
});

function createEl(node) {
  if (typeof node === "string") return document.createTextNode(node);
  const el = document.createElement(node.type);
  for (const [k, v] of Object.entries(node.props)) el.setAttribute(k, v);
  node.children.forEach((c) => el.append(createEl(c)));
  return el;
}

function patch(parent, newNode, oldNode, index = 0) {
  const el = parent.childNodes[index];
  if (oldNode === undefined) return parent.append(createEl(newNode));
  if (newNode === undefined) return el.remove();
  if (
    typeof newNode !== typeof oldNode ||
    (typeof newNode === "string" && newNode !== oldNode) ||
    newNode.type !== oldNode.type
  ) {
    return el.replaceWith(createEl(newNode));
  }
  if (typeof newNode !== "string") {
    const max = Math.max(newNode.children.length, oldNode.children.length);
    for (let i = max - 1; i >= 0; i--) {
      patch(el, newNode.children[i], oldNode.children[i], i);
    }
  }
}
```

Real frameworks also diff props and use `key`s to match list items that moved. Some newer frameworks (Svelte, Solid) skip the virtual DOM and update the DOM directly through compiled code or signals.

### 409: What is list virtualization?

Virtualization (or windowing) renders only the items visible on screen, plus a small buffer, instead of thousands of DOM nodes.

```js
function renderVisible(container, items, rowHeight) {
  const { scrollTop, clientHeight } = container;
  const start = Math.floor(scrollTop / rowHeight);
  const end = Math.min(
    items.length,
    Math.ceil((scrollTop + clientHeight) / rowHeight) + 5,
  );

  inner.style.height = `${items.length * rowHeight}px`; // full scroll height
  inner.replaceChildren(
    ...items.slice(start, end).map((item, i) => {
      const row = document.createElement("div");
      row.className = "row";
      row.style.transform = `translateY(${(start + i) * rowHeight}px)`;
      row.textContent = item;
      return row;
    }),
  );
}

container.addEventListener("scroll", () =>
  requestAnimationFrame(() => renderVisible(container, items, 32)),
);
```

Libraries like TanStack Virtual handle variable heights and other details. CSS `content-visibility: auto` is a simpler alternative in some cases.

### 410: What is a stale closure?

A stale closure is a function that captured an old value of a variable and keeps using it after the value has changed. It's very common in React hooks.

```js
function createCounter() {
  let count = 0;
  const logLater = () => {
    const snapshot = count;
    setTimeout(() => console.log(snapshot), 1000);
  };
  return { inc: () => count++, logLater };
}

// React example
function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // always uses count from the first render (0)
    }, 1000);
    return () => clearInterval(id);
  }, []);

  // fix: setCount((c) => c + 1)
}
```

Fixes: use functional updates, add the value to the dependency array, or read the latest value from a ref.

### 411: How do you memoize a function with multiple object arguments without leaking memory?

Use a tree of `WeakMap`s (for object arguments) and `Map`s (for primitives), one level per argument. When an object argument is garbage collected, its cache entries go away too.

```js
function createNode() {
  return {
    weak: new WeakMap(),
    strong: new Map(),
    hasResult: false,
    result: undefined,
  };
}

function memoizeArgs(fn) {
  const root = createNode();
  return function (...args) {
    let node = root;
    for (const arg of args) {
      const store =
        (typeof arg === "object" && arg !== null) || typeof arg === "function"
          ? node.weak
          : node.strong;
      let next = store.get(arg);
      if (!next) store.set(arg, (next = createNode()));
      node = next;
    }
    if (!node.hasResult) {
      node.result = fn.apply(this, args);
      node.hasResult = true;
    }
    return node.result;
  };
}

const area = memoizeArgs((rect, scale) => rect.w * rect.h * scale);
const r = { w: 2, h: 3 };
area(r, 2); // computed
area(r, 2); // cached
```

This is the same idea used by libraries like `reselect` (weakMapMemoize).

### 412: How would you implement a mutex or semaphore for async code?

Even though JavaScript is single-threaded, async code can interleave at each `await`. A semaphore limits how many async sections run at once. A mutex is a semaphore with a limit of 1.

```js
class Semaphore {
  #available;
  #waiting = [];

  constructor(count) {
    this.#available = count;
  }

  async acquire() {
    if (this.#available > 0) {
      this.#available--;
      return;
    }
    const { promise, resolve } = Promise.withResolvers();
    this.#waiting.push(resolve);
    await promise;
  }

  release() {
    const next = this.#waiting.shift();
    if (next) next();
    else this.#available++;
  }

  async run(fn) {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }
}

const mutex = new Semaphore(1);

async function updateBalance(amount) {
  return mutex.run(async () => {
    const balance = await readBalance();
    await writeBalance(balance + amount); // no other update runs in between
  });
}
```

In browsers, the Web Locks API (`navigator.locks.request`) gives you a lock that also works across tabs.

### 413: How would you add a timeout to any promise?

```js
function withTimeout(promise, ms, message = "Timed out") {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(message)), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}

await withTimeout(fetch("/api/slow"), 3000);
```

This only stops waiting. The original operation keeps running. If the operation supports cancellation, pass an `AbortSignal` (for example `AbortSignal.timeout(ms)`) so it actually stops.

### 414: How would you implement a deep merge?

```js
function isPlainObject(v) {
  if (v === null || typeof v !== "object") return false;
  const proto = Object.getPrototypeOf(v);
  return proto === Object.prototype || proto === null;
}

function deepMerge(target, ...sources) {
  const result = { ...target };
  for (const source of sources) {
    for (const [key, value] of Object.entries(source ?? {})) {
      if (key === "__proto__" || key === "constructor" || key === "prototype")
        continue;

      if (isPlainObject(value) && isPlainObject(result[key])) {
        result[key] = deepMerge(result[key], value);
      } else if (Array.isArray(value)) {
        result[key] = [...value]; // arrays are replaced, not merged
      } else {
        result[key] = value;
      }
    }
  }
  return result;
}

deepMerge(
  { db: { host: "localhost", port: 5432 }, debug: false },
  { db: { port: 6543 }, debug: true },
);
// { db: { host: "localhost", port: 6543 }, debug: true }
```

Important details: don't mutate inputs, decide how arrays are handled, and skip dangerous keys to prevent prototype pollution.

### 415: How would you write polyfills for map and reduce?

```js
Array.prototype.myMap = function (callback, thisArg) {
  if (typeof callback !== "function")
    throw new TypeError(`${callback} is not a function`);
  const result = new Array(this.length);
  for (let i = 0; i < this.length; i++) {
    if (i in this) {
      // skip holes like the real map
      result[i] = callback.call(thisArg, this[i], i, this);
    }
  }
  return result;
};

Array.prototype.myReduce = function (callback, ...init) {
  if (typeof callback !== "function")
    throw new TypeError(`${callback} is not a function`);
  let i = 0;
  let acc;

  if (init.length > 0) {
    acc = init[0];
  } else {
    while (i < this.length && !(i in this)) i++;
    if (i >= this.length)
      throw new TypeError("Reduce of empty array with no initial value");
    acc = this[i++];
  }

  for (; i < this.length; i++) {
    if (i in this) acc = callback(acc, this[i], i, this);
  }
  return acc;
};

[1, 2, 3].myMap((x) => x * 2); // [2, 4, 6]
[1, 2, 3].myReduce((a, b) => a + b); // 6
```

Using `...init` lets you tell the difference between "no initial value" and an initial value of `undefined`.

### 416: How would you flatten a deeply nested array without recursion?

Use a stack.

```js
function flatten(arr) {
  const stack = [...arr];
  const result = [];

  while (stack.length) {
    const item = stack.pop();
    if (Array.isArray(item)) {
      stack.push(...item);
    } else {
      result.push(item);
    }
  }
  return result.reverse();
}

flatten([1, [2, [3, [4, [5]]]], 6]); // [1, 2, 3, 4, 5, 6]
```

This avoids stack overflow on extremely deep arrays. With a generator you can also flatten lazily:

```js
function* flattenLazy(arr) {
  for (const item of arr) {
    if (Array.isArray(item)) yield* flattenLazy(item);
    else yield item;
  }
}
```

### 417: How would you implement promisify?

```js
function promisify(fn) {
  return function (...args) {
    return new Promise((resolve, reject) => {
      fn.call(this, ...args, (err, ...results) => {
        if (err) return reject(err);
        resolve(results.length > 1 ? results : results[0]);
      });
    });
  };
}

// error-first callback API
function readConfig(path, cb) {
  setTimeout(() => cb(null, { path, ok: true }), 10);
}

const readConfigAsync = promisify(readConfig);
const config = await readConfigAsync("app.json");
```

Node's `util.promisify` also supports a custom `util.promisify.custom` symbol for functions with non-standard callbacks.

### 418: How would you implement an EventEmitter with once and error handling?

```js
class Emitter {
  #events = new Map();

  on(name, fn) {
    (this.#events.get(name) ?? this.#events.set(name, []).get(name)).push(fn);
    return this;
  }

  once(name, fn) {
    const wrapper = (...args) => {
      this.off(name, wrapper);
      fn.apply(this, args);
    };
    wrapper.original = fn;
    return this.on(name, wrapper);
  }

  off(name, fn) {
    const list = this.#events.get(name);
    if (!list) return this;
    this.#events.set(
      name,
      list.filter((l) => l !== fn && l.original !== fn),
    );
    return this;
  }

  emit(name, ...args) {
    const list = this.#events.get(name);
    if (!list?.length) {
      if (name === "error") throw args[0]; // like Node: unhandled error events throw
      return false;
    }
    for (const fn of [...list]) fn.apply(this, args); // copy so off() during emit is safe
    return true;
  }
}

const e = new Emitter();
e.once("ready", () => console.log("ready!"));
e.emit("ready"); // "ready!"
e.emit("ready"); // nothing
```

Details interviewers look for: copying the listener list before calling, letting `off` remove a `once` listener by its original function, and treating unhandled `error` events specially.

### 419: How would you write a tag function that safely escapes HTML?

```js
const escapeMap = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;",
};
const escapeHtml = (s) => String(s).replace(/[&<>"']/g, (c) => escapeMap[c]);

class SafeHtml {
  constructor(value) {
    this.value = value;
  }
  toString() {
    return this.value;
  }
}

function html(strings, ...values) {
  const out = strings.reduce((acc, str, i) => {
    const v = values[i - 1];
    const safe =
      v instanceof SafeHtml
        ? v.value
        : Array.isArray(v)
          ? v
              .map((x) => (x instanceof SafeHtml ? x.value : escapeHtml(x)))
              .join("")
          : escapeHtml(v ?? "");
    return acc + safe + str;
  });
  return new SafeHtml(out);
}

const name = '<img src=x onerror="alert(1)">';
const items = ["a", "<b>"];

html`<p>Hello ${name}</p>
  <ul>
    ${items.map((i) => html`<li>${i}</li>`)}
  </ul>`.toString();
// <p>Hello &lt;img src=x onerror=&quot;alert(1)&quot;&gt;</p><ul><li>a</li><li>&lt;b&gt;</li></ul>
```

Escaping text is not enough for every context. Values inside `href`, `<script>` or CSS need different handling.

### 420: How would you compose async functions into a pipeline?

```js
const pipeAsync =
  (...fns) =>
  (input) =>
    fns.reduce((acc, fn) => acc.then(fn), Promise.resolve(input));

const fetchUser = async (id) => ({ id, name: "ann" });
const addPosts = async (user) => ({ ...user, posts: [1, 2] });
const formatName = (user) => ({ ...user, name: user.name.toUpperCase() });

const loadProfile = pipeAsync(fetchUser, addPosts, formatName);
await loadProfile(1); // { id: 1, name: "ANN", posts: [1, 2] }
```

Because `then` accepts both sync and async functions, the pipeline can mix them.

### 421: What is Proxy.revocable?

`Proxy.revocable` creates a proxy that you can turn off later. After `revoke()`, any operation on the proxy throws a `TypeError`. It's useful for giving temporary access to an object.

```js
const { proxy, revoke } = Proxy.revocable({ secret: 42 }, {});

proxy.secret; // 42
revoke();
proxy.secret; // TypeError: Cannot perform 'get' on a proxy that has been revoked
```

A typical case is passing an object to a plugin and revoking access when the plugin is unloaded.

### 422: How would you use a Proxy to support negative array indexes?

```js
function negativeArray(arr) {
  return new Proxy(arr, {
    get(target, prop, receiver) {
      if (typeof prop === "string" && /^-\d+$/.test(prop)) {
        prop = String(target.length + Number(prop));
      }
      return Reflect.get(target, prop, receiver);
    },
    set(target, prop, value, receiver) {
      if (typeof prop === "string" && /^-\d+$/.test(prop)) {
        prop = String(target.length + Number(prop));
      }
      return Reflect.set(target, prop, value, receiver);
    },
  });
}

const arr = negativeArray([1, 2, 3]);
arr[-1]; // 3
arr[-2] = 9; // [1, 9, 3]
```

Property keys reach traps as strings (or symbols), so `-1` arrives as `"-1"`. Today `arr.at(-1)` covers the read case without a proxy.

### 423: Can symbols be used as WeakMap keys?

Yes, since ES2023, non-registered symbols can be WeakMap keys (and WeakSet values, WeakRef targets). Registered symbols from `Symbol.for()` can't, because they live forever and would never be collected.

```js
const wm = new WeakMap();
const key = Symbol("session");

wm.set(key, { user: "Ann" }); // ok
wm.set(Symbol.for("x"), 1); // TypeError
```

This is useful when you want a unique, non-object token as a key with weak semantics.

### 424: What is negative zero and where does it show up?

JavaScript numbers have both `+0` and `-0`. They are equal with `===`, but behave differently in some operations.

```js
-0 === 0; // true
Object.is(-0, 0); // false
1 / -0; // -Infinity
Math.sign(-0); // -0
Math.round(-0.4); // -0
(-0).toString(); // "0"
JSON.stringify(-0); // "0"
[-0].includes(0); // true
new Set([0, -0]).size; // 1

Math.min(0, -0); // -0
```

It can matter for things like direction of movement (a value that reached 0 while going left), or when using `Object.is` for comparisons, as React does.

### 425: What are Math.imul, Math.clz32 and Math.fround used for?

They expose low-level number operations, mostly useful for performance code, hashing and code generated from other languages (like asm.js or WebAssembly glue code).

```js
Math.imul(0xffffffff, 5); // -5, real 32-bit integer multiplication
0xffffffff * 5; // 21474836475 (normal float math)

Math.clz32(1); // 31 (count leading zero bits in 32-bit form)
Math.clz32(0); // 32

Math.fround(5.5); // 5.5
Math.fround(5.05); // 5.050000190734863 (nearest 32-bit float)
Math.f16round(5.05); // 5.05078125 (nearest 16-bit float, ES2025)
```

A typical use of `Math.imul` is a fast string hash:

```js
function hash(str) {
  let h = 0;
  for (let i = 0; i < str.length; i++) {
    h = (Math.imul(31, h) + str.charCodeAt(i)) | 0;
  }
  return h >>> 0;
}
```

### 426: How is the arguments object linked to parameters in sloppy mode?

In sloppy mode functions with simple parameter lists, `arguments` and named parameters are linked: changing one changes the other. In strict mode, or when the function uses default, rest or destructured parameters, they are separate.

```js
function sloppy(a) {
  arguments[0] = 99;
  return a;
}
sloppy(1); // 99

function strict(a) {
  "use strict";
  arguments[0] = 99;
  return a;
}
strict(1); // 1

function withDefault(a = 0) {
  arguments[0] = 99;
  return a;
}
withDefault(1); // 1
```

This linking makes optimization harder, which is one more reason to use rest parameters instead of `arguments`.

### 427: What is the with statement and why is it not allowed in strict mode?

`with` adds an object's properties to the scope chain for a block.

```js
const point = { x: 1, y: 2 };
with (point) {
  console.log(x + y); // 3
}
```

The problem is that you can't tell from the code whether `x` means `point.x` or an outer variable. It depends on the object at runtime. That makes code confusing, breaks static analysis, and stops engines from optimizing variable lookups. So it's a SyntaxError in strict mode, which includes all modules and classes.

### 428: What is a self-replacing (lazy) getter?

A lazy getter computes an expensive value the first time it's read, then replaces itself with a plain data property so later reads are fast.

```js
const config = {
  get parsed() {
    const value = JSON.parse(largeJsonString); // expensive
    Object.defineProperty(this, "parsed", {
      value,
      writable: false,
      enumerable: true,
    });
    return value;
  },
};

config.parsed; // computed
config.parsed; // plain property now
```

In classes, the getter is on the prototype, so define the cached value on the instance:

```js
class Report {
  get summary() {
    const value = this.#buildSummary();
    Object.defineProperty(this, "summary", { value });
    return value;
  }
  #buildSummary() {
    return { total: 100 };
  }
}
```

### 429: How do you count words or characters correctly in any language?

Splitting on spaces doesn't work for languages like Japanese or Thai, and `length` doesn't count user-visible characters correctly. `Intl.Segmenter` handles both.

```js
const text = "Hello 👋🏽 world! 今日は良い天気です。";

const words = new Intl.Segmenter("ja", { granularity: "word" });
const wordCount = [...words.segment(text)].filter((s) => s.isWordLike).length;

const graphemes = new Intl.Segmenter("en", { granularity: "grapheme" });
const charCount = [...graphemes.segment(text)].length;

const sentences = new Intl.Segmenter("en", { granularity: "sentence" });
[...sentences.segment("Hi there. How are you?")].map((s) => s.segment);
// ["Hi there. ", "How are you?"]
```

### 430: When are iterator helpers better than array methods?

Array methods create a new full array at every step. Iterator helpers are lazy: each value goes through the whole chain before the next one is read, and nothing extra is stored.

```js
// Array: builds 1,000,000 items, then another array, then another
const firstFive = hugeArray.map(expensiveTransform).filter(isValid).slice(0, 5);

// Iterator: stops after finding 5 valid items
const firstFive2 = hugeArray
  .values()
  .map(expensiveTransform)
  .filter(isValid)
  .take(5)
  .toArray();
```

Iterator helpers are better for large or infinite sources, early exits, and streaming data. Arrays are still simpler (and often faster) for small data, and when you need random access, sorting or multiple passes.

You can also make your own iterator class get the helpers by extending `Iterator`:

```js
class Countdown extends Iterator {
  #n;
  constructor(n) {
    super();
    this.#n = n;
  }
  next() {
    return this.#n > 0
      ? { value: this.#n--, done: false }
      : { value: undefined, done: true };
  }
}

new Countdown(5).filter((n) => n % 2).toArray(); // [5, 3, 1]
```

### 431: How would you merge several async iterables into one as values arrive?

```js
async function* mergeAsync(...iterables) {
  const iterators = iterables.map((it) => it[Symbol.asyncIterator]());
  const pending = new Map();

  const nextOf = (it, index) => it.next().then((result) => ({ result, index }));

  iterators.forEach((it, i) => pending.set(i, nextOf(it, i)));

  try {
    while (pending.size) {
      const { result, index } = await Promise.race(pending.values());
      if (result.done) {
        pending.delete(index);
      } else {
        pending.set(index, nextOf(iterators[index], index));
        yield result.value;
      }
    }
  } finally {
    // close the rest if the consumer breaks early
    await Promise.all([...pending.keys()].map((i) => iterators[i].return?.()));
  }
}

async function* ticker(name, ms, count) {
  for (let i = 0; i < count; i++) {
    await new Promise((r) => setTimeout(r, ms));
    yield `${name}${i}`;
  }
}

for await (const v of mergeAsync(ticker("a", 100, 3), ticker("b", 150, 2))) {
  console.log(v); // a0, b0, a1, a2, b1 (by timing)
}
```

### 432: How does JavaScript work with WebAssembly?

WebAssembly (Wasm) is a binary format that runs at near-native speed in the same engine as JavaScript. You load a module from JavaScript, pass imports in, and call its exports.

```js
const { instance } = await WebAssembly.instantiateStreaming(
  fetch("/math.wasm"),
  {
    env: {
      log: (n) => console.log("from wasm:", n),
    },
  },
);

instance.exports.add(2, 3); // 5

// share memory
const memory = instance.exports.memory;
const bytes = new Uint8Array(memory.buffer);
```

JavaScript and Wasm pass numbers directly. For strings and objects you copy data through the shared memory, usually with generated glue code from tools like `wasm-bindgen` (Rust) or Emscripten (C/C++). Use Wasm for CPU-heavy work like image/video processing, compression, games, or reusing existing native libraries.

### 433: What is the difference between a dedicated worker, a shared worker and a service worker?

|               | Dedicated Worker    | Shared Worker                           | Service Worker                      |
| ------------- | ------------------- | --------------------------------------- | ----------------------------------- |
| Owned by      | one page            | several pages of the same origin        | the origin (all pages in its scope) |
| Main use      | heavy computation   | shared connection or state between tabs | network proxy, offline, push        |
| Lifetime      | as long as the page | while any page uses it                  | started and stopped by the browser  |
| Communication | `postMessage`       | `port.postMessage`                      | `postMessage`, fetch events         |
| DOM access    | no                  | no                                      | no                                  |

```js
// Shared worker
const shared = new SharedWorker("/shared.js");
shared.port.postMessage("hello");
shared.port.onmessage = (e) => console.log(e.data);

// shared.js
onconnect = (e) => {
  const port = e.ports[0];
  port.onmessage = (msg) => port.postMessage(`echo: ${msg.data}`);
};
```

### 434: What is OffscreenCanvas?

`OffscreenCanvas` lets you draw on a canvas from a Web Worker, so heavy rendering doesn't block the main thread.

```js
// main.js
const canvas = document.querySelector("canvas");
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker("render.js");
worker.postMessage({ canvas: offscreen }, [offscreen]);

// render.js
self.onmessage = ({ data }) => {
  const ctx = data.canvas.getContext("2d");
  function frame(t) {
    ctx.clearRect(0, 0, 300, 150);
    ctx.fillRect(150 + Math.sin(t / 300) * 100, 60, 30, 30);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
};
```

The worker draws, and the result shows on the page's canvas automatically.

### 435: What is the View Transitions API?

The View Transitions API animates between two states of the page. The browser takes a snapshot before and after a DOM change and animates between them with CSS.

```js
function showDetails(item) {
  if (!document.startViewTransition) {
    renderDetails(item);
    return;
  }
  document.startViewTransition(() => renderDetails(item));
}
```

```css
.thumbnail {
  view-transition-name: hero-image;
}

::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
}
```

Elements with the same `view-transition-name` before and after are animated from one position to the other. Cross-document transitions (between page loads) work with the CSS rule `@view-transition { navigation: auto; }`.

### 436: What are source maps?

A source map is a file that connects the minified or compiled code back to your original source. DevTools and error trackers use it to show the original file names, lines and variable names.

```js
// at the end of the bundle
//# sourceMappingURL=app.min.js.map
```

The `.map` file is JSON with `sources`, `names` and a `mappings` string (encoded with Base64 VLQ).

Points to know:

- In production, many teams upload source maps to their error tracking service and don't serve them publicly.
- Node.js can use them with `--enable-source-maps`.
- Wrong or missing source maps are a common reason for unreadable stack traces.

### 437: What techniques do you use to reduce JavaScript bundle size?

- Code splitting with dynamic `import()` per route or feature.
- Tree shaking: use ES modules and side-effect-free packages.
- Replace heavy libraries (Moment.js with `Intl` or Temporal, lodash with native methods).
- Don't ship polyfills modern browsers don't need. Set a modern browser target.
- Analyze bundles with tools like `rollup-plugin-visualizer` or `webpack-bundle-analyzer`.
- Lazy load below-the-fold components and third-party scripts.
- Minify and compress (Brotli or gzip) on the server.
- Move rarely changing vendor code to separate chunks for better caching.

```js
const routes = {
  "/": () => import("./pages/home.js"),
  "/settings": () => import("./pages/settings.js"),
};

async function navigate(path) {
  const page = await routes[path]();
  page.render();
}
```

### 438: What are preload, prefetch, modulepreload and fetchpriority?

They are resource hints that help the browser load things at the right time.

```html
<!-- needed for this page, load early -->
<link
  rel="preload"
  href="/fonts/inter.woff2"
  as="font"
  type="font/woff2"
  crossorigin
/>

<!-- ES module and its dependencies, load and parse early -->
<link rel="modulepreload" href="/js/app.js" />

<!-- probably needed on the next page, low priority -->
<link rel="prefetch" href="/js/checkout.js" />

<!-- connect to another origin early -->
<link rel="preconnect" href="https://api.example.com" />

<!-- raise priority of the LCP image -->
<img src="/hero.jpg" fetchpriority="high" alt="" />
```

You can also use `fetchpriority` from JavaScript: `fetch(url, { priority: "low" })`. The Speculation Rules API can prefetch or prerender whole pages in Chromium browsers.

### 439: How do you find and fix memory leaks in a web app?

1. Reproduce: repeat an action (open and close a modal, change routes) many times.
2. Watch the Memory panel or `performance.memory` (Chrome only) for steady growth.
3. Take heap snapshots before and after, and compare them. Look for objects whose count keeps growing.
4. Filter for "Detached" to find DOM nodes that were removed from the page but are still referenced.
5. Look at the retainers path to see what is keeping the object alive.

Typical fixes:

```js
// clean up everything a component sets up
function mount(el) {
  const ac = new AbortController();
  const { signal } = ac;

  window.addEventListener("resize", onResize, { signal });
  const id = setInterval(poll, 5000);
  const ro = new ResizeObserver(onSize);
  ro.observe(el);

  return function unmount() {
    ac.abort();
    clearInterval(id);
    ro.disconnect();
  };
}
```

Other common causes: growing caches without limits, closures that hold large data, and global stores that keep references to removed components.

### 440: How do you detect and avoid blocking the event loop in Node.js?

The Node.js event loop handles all requests on one thread. A slow synchronous operation (big JSON parse, sync file reads, heavy regex, CPU loops) blocks every other request.

Detect it:

```js
import { monitorEventLoopDelay } from "node:perf_hooks";

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();

setInterval(() => {
  console.log("p99 delay (ms):", h.percentile(99) / 1e6);
  h.reset();
}, 5000);
```

Avoid it:

- Use async APIs (`fs/promises` instead of `readFileSync` in request handlers).
- Move CPU-heavy work to `worker_threads` or a separate service.
- Break long loops into chunks with `setImmediate`.
- Stream large data instead of loading it all into memory.
- Limit input size and avoid unsafe regex.

### 441: What is cross-origin isolation (COOP and COEP)?

Cross-origin isolation puts a page in its own process group so it can safely use powerful features like `SharedArrayBuffer` and precise timers, which could otherwise be abused for Spectre-style attacks.

You enable it with two headers:

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

- **COOP** stops other origins' windows from keeping a reference to your window.
- **COEP** only allows loading cross-origin resources that explicitly allow it (with CORS or `Cross-Origin-Resource-Policy`). `COEP: credentialless` is an easier alternative.

```js
if (crossOriginIsolated) {
  const shared = new SharedArrayBuffer(1024);
}
```

### 442: How can you run untrusted JavaScript code more safely?

Never run untrusted code with `eval` or `new Function` in your main page. Options, from weakest to strongest isolation:

- **Sandboxed iframe**: `<iframe sandbox="allow-scripts">` with a different origin. Talk to it only through `postMessage`.
- **Web Worker**: no DOM access, but still the same origin, so it can make requests with your cookies.
- **SES / Hardened JavaScript** (`lockdown()` and `Compartment`): freezes built-ins and limits what code can reach.
- **ShadowRealm** (a TC39 proposal): a new realm with its own globals, but no automatic access to yours.
- **Server-side**: separate processes, containers or V8 isolates (like `isolated-vm`). Node's `vm` module is not a security boundary.

```html
<iframe
  sandbox="allow-scripts"
  src="https://sandbox.example-usercontent.com/runner.html"
>
</iframe>
```

### 443: How do you do dependency injection in JavaScript?

Dependency injection means a module receives the things it depends on instead of creating them itself. This makes code easier to test and change.

```js
// without DI: hard to test
class OrderService {
  constructor() {
    this.db = new PostgresClient();
    this.mailer = new SmtpMailer();
  }
}

// with DI
class OrderService2 {
  constructor({ db, mailer, clock = () => new Date() }) {
    this.db = db;
    this.mailer = mailer;
    this.clock = clock;
  }

  async place(order) {
    const saved = await this.db.insert("orders", {
      ...order,
      createdAt: this.clock(),
    });
    await this.mailer.send(order.email, "Order received");
    return saved;
  }
}

// in tests
const service = new OrderService2({
  db: { insert: async (_, row) => ({ id: 1, ...row }) },
  mailer: { send: async () => {} },
  clock: () => new Date("2025-01-01"),
});
```

In JavaScript, plain function parameters or factory functions are usually enough. Frameworks like Angular and NestJS have DI containers built in.

### 444: How would you use the strategy pattern in JavaScript?

The strategy pattern picks an algorithm at runtime from a set of interchangeable ones. In JavaScript, an object map of functions is often all you need, and it replaces long `if/else` or `switch` chains.

```js
const shippingStrategies = {
  standard: (order) => 5,
  express: (order) => 15,
  free: (order) => 0,
  weight: (order) => order.weightKg * 2,
};

function shippingCost(order) {
  const strategy = shippingStrategies[order.shipping];
  if (!strategy) throw new Error(`Unknown shipping: ${order.shipping}`);
  return strategy(order);
}

shippingCost({ shipping: "weight", weightKg: 3 }); // 6
```

New strategies can be added without changing `shippingCost`.

### 445: What is structural sharing and how does Immer work?

Structural sharing means when you "change" immutable data, you create new objects only along the changed path, and reuse everything else. This keeps updates cheap and lets you compare by reference.

```js
const state = {
  user: { name: "Ann" },
  todos: [
    { id: 1, done: false },
    { id: 2, done: false },
  ],
};

const next = {
  ...state,
  todos: state.todos.map((t) => (t.id === 2 ? { ...t, done: true } : t)),
};

next.user === state.user; // true (shared)
next.todos[0] === state.todos[0]; // true (shared)
next.todos[1] === state.todos[1]; // false (changed)
```

Immer lets you write normal "mutating" code on a draft. It uses a Proxy to record changes and then builds a new state with structural sharing:

```js
import { produce } from "immer";

const next2 = produce(state, (draft) => {
  draft.todos[1].done = true;
});
```

### 446: What are the TC39 stages for new JavaScript features?

New features go through stages before they become part of the standard:

- **Stage 0**: an idea.
- **Stage 1**: the committee agrees the problem is worth solving.
- **Stage 2**: a draft spec text exists, the design is mostly chosen.
- **Stage 2.7**: the spec is complete and approved, waiting for tests and implementation feedback.
- **Stage 3**: recommended for implementation. Engines start shipping it.
- **Stage 4**: finished. At least two engines have shipped it and tests exist. It goes into the next yearly edition.

Proposals are public on GitHub (`tc39/proposals`). This is why you sometimes see features in browsers or TypeScript before they're in the official ECMAScript edition.

### 447: What features were added in recent ECMAScript versions?

**ES2022**: class fields, private methods, `#x in obj`, static blocks, top-level await, `.at()`, `Object.hasOwn`, error `cause`, regex `d` flag.

**ES2023**: `toSorted`, `toReversed`, `toSpliced`, `with`, `findLast`, `findLastIndex`, hashbang (`#!`) support, symbols as WeakMap keys.

**ES2024**: `Object.groupBy`, `Map.groupBy`, `Promise.withResolvers`, regex `v` flag, resizable `ArrayBuffer` and `transfer`, `String.prototype.isWellFormed`/`toWellFormed`, `Atomics.waitAsync`.

**ES2025**: iterator helpers, new `Set` methods (`union`, `intersection`, etc.), `Promise.try`, `RegExp.escape`, regex modifiers, duplicate named capture groups, import attributes and JSON modules, `Float16Array` and `Math.f16round`.

**ES2026**: `Error.isError`, `Math.sumPrecise`, `Uint8Array` base64/hex methods, `Array.fromAsync`, and more.

Also worth knowing: `Temporal` and explicit resource management (`using`) are already shipping in major engines.

### 448: How do you write a function that works with both sync and async iterables?

Check for `Symbol.asyncIterator` first, and fall back to `Symbol.iterator`. `for await...of` already does this, so the simplest option is to use it.

```js
async function collect(source, limit = Infinity) {
  const out = [];
  for await (const item of source) {
    // works with sync and async iterables
    out.push(item);
    if (out.length >= limit) break;
  }
  return out;
}

await collect([1, 2, 3]); // [1, 2, 3]
await collect(new Set(["a"])); // ["a"]
await collect(
  (async function* () {
    yield 1;
    yield 2;
  })(),
); // [1, 2]
await collect([Promise.resolve(1), 2]); // [1, 2] (promises are awaited)
```

One difference: with a sync iterable of promises, `for await` awaits each value. If one of them rejects, the loop throws.

### 449: How would you design an autocomplete search input?

This is a common frontend system design question. A good answer covers:

1. **Input handling**: debounce the input (around 200–300 ms) and skip empty or very short queries.
2. **Request management**: cancel the previous request with `AbortController` so old responses can't overwrite new ones.
3. **Caching**: keep a small LRU cache of query -> results to avoid repeated requests.
4. **Rendering**: highlight matches safely (no `innerHTML` with raw input), and virtualize long lists.
5. **Accessibility**: use the ARIA combobox pattern (`role="combobox"`, `aria-expanded`, `aria-activedescendant`, `role="listbox"`), with keyboard support for arrows, Enter and Escape.
6. **States**: loading, empty, error, and offline.

```js
function createAutocomplete(input, renderResults) {
  const cache = new Map();
  let controller;

  const search = debounce(async (query) => {
    if (query.length < 2) return renderResults([]);
    if (cache.has(query)) return renderResults(cache.get(query));

    controller?.abort();
    controller = new AbortController();

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`, {
        signal: controller.signal,
      });
      const results = await res.json();
      cache.set(query, results);
      if (cache.size > 50) cache.delete(cache.keys().next().value);
      renderResults(results);
    } catch (err) {
      if (err.name !== "AbortError") renderResults([], err);
    }
  }, 250);

  input.addEventListener("input", (e) => search(e.target.value.trim()));
}
```

### 450: How would you explain the full lifecycle of a click in a browser, from the user to the screen update?

1. The OS sends the input to the browser, and the browser finds the target element with hit testing.
2. A `pointerdown`/`mousedown`, `pointerup`/`mouseup` and `click` event are queued as tasks.
3. When the main thread is free, the event goes through the capture, target and bubble phases, running listeners.
4. Your handler runs synchronously. It may change state, change the DOM, or start a `fetch`.
5. After the handler finishes, all microtasks run (promise callbacks, `queueMicrotask`, `MutationObserver`).
6. If a frame is due, the browser runs `requestAnimationFrame` callbacks, then recalculates styles and layout, runs `ResizeObserver` callbacks, paints, and composites layers on the GPU.
7. The new frame is shown. The time from the click to this frame is what INP measures.
8. Later, when the `fetch` response arrives, its callback runs as another task followed by microtasks, and another render happens.

```js
button.addEventListener("click", async () => {
  button.disabled = true; // step 4: sync DOM change
  await scheduler?.yield?.(); // let the browser paint the disabled state
  const data = await fetch("/api/save"); // step 8 happens later
  status.textContent = "Saved";
  button.disabled = false;
});
```

Knowing this flow explains most performance advice: keep handlers short, yield to the browser before heavy work, avoid forced layouts, and move heavy work off the main thread.
