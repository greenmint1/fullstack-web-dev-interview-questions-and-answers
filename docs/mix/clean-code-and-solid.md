# Clean Code and SOLID Interview Questions and Answers

_Last updated: November 18, 2026_

450 interview questions about clean code and the SOLID principles, split into three levels: 150 easy, 150 moderate and 150 advanced.

The ideas here don't depend on one language, but the code examples use TypeScript (and sometimes React or Node.js), since that's what most full stack web developers write today. The answers try to stay practical: what the rule is, why it exists, and when it's fine to break it.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is clean code?](#1-what-is-clean-code)
- [2: Why does clean code matter if the code already works?](#2-why-does-clean-code-matter-if-the-code-already-works)
- [3: Who is Robert C. Martin and why is he linked to clean code?](#3-who-is-robert-c-martin-and-why-is-he-linked-to-clean-code)
- [4: What does SOLID stand for?](#4-what-does-solid-stand-for)
- [5: What is the Single Responsibility Principle?](#5-what-is-the-single-responsibility-principle)
- [6: What is the Open/Closed Principle?](#6-what-is-the-openclosed-principle)
- [7: What is the Liskov Substitution Principle?](#7-what-is-the-liskov-substitution-principle)
- [8: What is the Interface Segregation Principle?](#8-what-is-the-interface-segregation-principle)
- [9: What is the Dependency Inversion Principle?](#9-what-is-the-dependency-inversion-principle)
- [10: Why are meaningful names important?](#10-why-are-meaningful-names-important)
- [11: What makes a good variable name?](#11-what-makes-a-good-variable-name)
- [12: How should you name functions?](#12-how-should-you-name-functions)
- [13: How should you name classes?](#13-how-should-you-name-classes)
- [14: How should you name boolean variables?](#14-how-should-you-name-boolean-variables)
- [15: What is a magic number and why is it a problem?](#15-what-is-a-magic-number-and-why-is-it-a-problem)
- [16: Should you use abbreviations in names?](#16-should-you-use-abbreviations-in-names)
- [17: What is Hungarian notation and should you use it?](#17-what-is-hungarian-notation-and-should-you-use-it)
- [18: What does "use consistent names" mean?](#18-what-does-use-consistent-names-mean)
- [19: How long should a function be?](#19-how-long-should-a-function-be)
- [20: What does "a function should do one thing" mean?](#20-what-does-a-function-should-do-one-thing-mean)
- [21: How many parameters should a function have?](#21-how-many-parameters-should-a-function-have)
- [22: What is a flag argument and why is it considered a code smell?](#22-what-is-a-flag-argument-and-why-is-it-considered-a-code-smell)
- [23: What is a side effect?](#23-what-is-a-side-effect)
- [24: What is a pure function?](#24-what-is-a-pure-function)
- [25: What is a guard clause?](#25-what-is-a-guard-clause)
- [26: Why is deep nesting a problem?](#26-why-is-deep-nesting-a-problem)
- [27: What is the DRY principle?](#27-what-is-the-dry-principle)
- [28: What is the KISS principle?](#28-what-is-the-kiss-principle)
- [29: What is the YAGNI principle?](#29-what-is-the-yagni-principle)
- [30: What is the Boy Scout Rule?](#30-what-is-the-boy-scout-rule)
- [31: When are comments useful?](#31-when-are-comments-useful)
- [32: When are comments a bad sign?](#32-when-are-comments-a-bad-sign)
- [33: What should you do with commented-out code?](#33-what-should-you-do-with-commented-out-code)
- [34: Are TODO comments OK?](#34-are-todo-comments-ok)
- [35: What is self-documenting code?](#35-what-is-self-documenting-code)
- [36: Why is consistent formatting important?](#36-why-is-consistent-formatting-important)
- [37: What is the difference between a formatter and a linter?](#37-what-is-the-difference-between-a-formatter-and-a-linter)
- [38: What is a code smell?](#38-what-is-a-code-smell)
- [39: What is the "long method" smell?](#39-what-is-the-long-method-smell)
- [40: What is the "large class" smell?](#40-what-is-the-large-class-smell)
- [41: What is the "duplicated code" smell?](#41-what-is-the-duplicated-code-smell)
- [42: What is "dead code"?](#42-what-is-dead-code)
- [43: What is refactoring?](#43-what-is-refactoring)
- [44: Is refactoring the same as rewriting?](#44-is-refactoring-the-same-as-rewriting)
- [45: When should you refactor?](#45-when-should-you-refactor)
- [46: What is the "rule of three"?](#46-what-is-the-rule-of-three)
- [47: What is technical debt?](#47-what-is-technical-debt)
- [48: What is coupling?](#48-what-is-coupling)
- [49: What is cohesion?](#49-what-is-cohesion)
- [50: How are coupling and cohesion related?](#50-how-are-coupling-and-cohesion-related)
- [51: What is encapsulation?](#51-what-is-encapsulation)
- [52: What is abstraction?](#52-what-is-abstraction)
- [53: What is the difference between composition and inheritance?](#53-what-is-the-difference-between-composition-and-inheritance)
- [54: Why do people say "favor composition over inheritance"?](#54-why-do-people-say-favor-composition-over-inheritance)
- [55: Why are interfaces useful for clean code?](#55-why-are-interfaces-useful-for-clean-code)
- [56: What is dependency injection?](#56-what-is-dependency-injection)
- [57: What are the common ways to inject dependencies?](#57-what-are-the-common-ways-to-inject-dependencies)
- [58: What is separation of concerns?](#58-what-is-separation-of-concerns)
- [59: What is the Law of Demeter?](#59-what-is-the-law-of-demeter)
- [60: Can you give a simple example of an SRP violation?](#60-can-you-give-a-simple-example-of-an-srp-violation)
- [61: How can you tell that a class has too many responsibilities?](#61-how-can-you-tell-that-a-class-has-too-many-responsibilities)
- [62: Can you give a simple example of the Open/Closed Principle?](#62-can-you-give-a-simple-example-of-the-openclosed-principle)
- [63: What is the classic Rectangle and Square example of an LSP violation?](#63-what-is-the-classic-rectangle-and-square-example-of-an-lsp-violation)
- [64: Can you give a simple example of the Interface Segregation Principle?](#64-can-you-give-a-simple-example-of-the-interface-segregation-principle)
- [65: Can you give a simple example of the Dependency Inversion Principle?](#65-can-you-give-a-simple-example-of-the-dependency-inversion-principle)
- [66: Is the Dependency Inversion Principle the same as dependency injection?](#66-is-the-dependency-inversion-principle-the-same-as-dependency-injection)
- [67: Does SOLID only apply to classes and object-oriented code?](#67-does-solid-only-apply-to-classes-and-object-oriented-code)
- [68: Should you use exceptions or error codes?](#68-should-you-use-exceptions-or-error-codes)
- [69: Why is an empty catch block a bad idea?](#69-why-is-an-empty-catch-block-a-bad-idea)
- [70: Why should you avoid returning null?](#70-why-should-you-avoid-returning-null)
- [71: What makes a good error message?](#71-what-makes-a-good-error-message)
- [72: What does "fail fast" mean?](#72-what-does-fail-fast-mean)
- [73: Why are tests important for clean code?](#73-why-are-tests-important-for-clean-code)
- [74: What makes a test clean?](#74-what-makes-a-test-clean)
- [75: What is the Arrange-Act-Assert pattern?](#75-what-is-the-arrange-act-assert-pattern)
- [76: What are the FIRST principles for tests?](#76-what-are-the-first-principles-for-tests)
- [77: Should a test have only one assertion?](#77-should-a-test-have-only-one-assertion)
- [78: How should you name tests?](#78-how-should-you-name-tests)
- [79: What is test-driven development (TDD)?](#79-what-is-test-driven-development-tdd)
- [80: What is the red-green-refactor cycle?](#80-what-is-the-red-green-refactor-cycle)
- [81: How does code review help keep code clean?](#81-how-does-code-review-help-keep-code-clean)
- [82: What should you look for when reviewing code for cleanliness?](#82-what-should-you-look-for-when-reviewing-code-for-cleanliness)
- [83: What is the "long parameter list" smell?](#83-what-is-the-long-parameter-list-smell)
- [84: What is primitive obsession?](#84-what-is-primitive-obsession)
- [85: What are data clumps?](#85-what-are-data-clumps)
- [86: What is feature envy?](#86-what-is-feature-envy)
- [87: What is shotgun surgery?](#87-what-is-shotgun-surgery)
- [88: What is divergent change?](#88-what-is-divergent-change)
- [89: Why are repeated switch statements considered a smell?](#89-why-are-repeated-switch-statements-considered-a-smell)
- [90: What is speculative generality?](#90-what-is-speculative-generality)
- [91: What is the "comments as deodorant" idea?](#91-what-is-the-comments-as-deodorant-idea)
- [92: What is a temporary field?](#92-what-is-a-temporary-field)
- [93: What is a message chain?](#93-what-is-a-message-chain)
- [94: What is the "middle man" smell?](#94-what-is-the-middle-man-smell)
- [95: What is a lazy class?](#95-what-is-a-lazy-class)
- [96: What is inappropriate intimacy?](#96-what-is-inappropriate-intimacy)
- [97: What is "refused bequest"?](#97-what-is-refused-bequest)
- [98: What is a "mysterious name"?](#98-what-is-a-mysterious-name)
- [99: Why is global mutable state a problem?](#99-why-is-global-mutable-state-a-problem)
- [100: Why does clean code prefer immutable data?](#100-why-does-clean-code-prefer-immutable-data)
- [101: What is polymorphism and how does it help clean code?](#101-what-is-polymorphism-and-how-does-it-help-clean-code)
- [102: What is the Strategy pattern?](#102-what-is-the-strategy-pattern)
- [103: What does "program to an interface, not an implementation" mean?](#103-what-does-program-to-an-interface-not-an-implementation-mean)
- [104: What is spaghetti code?](#104-what-is-spaghetti-code)
- [105: What is wrong with copy-paste programming?](#105-what-is-wrong-with-copy-paste-programming)
- [106: What is premature optimization?](#106-what-is-premature-optimization)
- [107: What is cyclomatic complexity?](#107-what-is-cyclomatic-complexity)
- [108: Why should files be kept small?](#108-why-should-files-be-kept-small)
- [109: What is the stepdown rule?](#109-what-is-the-stepdown-rule)
- [110: What is the newspaper metaphor in clean code?](#110-what-is-the-newspaper-metaphor-in-clean-code)
- [111: How should you use blank lines and vertical spacing?](#111-how-should-you-use-blank-lines-and-vertical-spacing)
- [112: What is the problem with "utils" or "helpers" files?](#112-what-is-the-problem-with-utils-or-helpers-files)
- [113: What is Command-Query Separation?](#113-what-is-command-query-separation)
- [114: What does "tell, don't ask" mean?](#114-what-does-tell-dont-ask-mean)
- [115: What is an explaining variable?](#115-what-is-an-explaining-variable)
- [116: What is "mental mapping" in names?](#116-what-is-mental-mapping-in-names)
- [117: What are noise words in names?](#117-what-are-noise-words-in-names)
- [118: Why should you avoid cute or funny names?](#118-why-should-you-avoid-cute-or-funny-names)
- [119: How should you name arrays and collections?](#119-how-should-you-name-arrays-and-collections)
- [120: What are the common naming conventions in JavaScript and TypeScript?](#120-what-are-the-common-naming-conventions-in-javascript-and-typescript)
- [121: Why should you avoid double negatives?](#121-why-should-you-avoid-double-negatives)
- [122: When is the ternary operator a good idea and when not?](#122-when-is-the-ternary-operator-a-good-idea-and-when-not)
- [123: How do optional chaining and nullish coalescing help clean code?](#123-how-do-optional-chaining-and-nullish-coalescing-help-clean-code)
- [124: How does destructuring improve readability?](#124-how-does-destructuring-improve-readability)
- [125: Why should you prefer const over let?](#125-why-should-you-prefer-const-over-let)
- [126: Why is async/await usually cleaner than callbacks or promise chains?](#126-why-is-asyncawait-usually-cleaner-than-callbacks-or-promise-chains)
- [127: When are array methods like map and filter cleaner than loops?](#127-when-are-array-methods-like-map-and-filter-cleaner-than-loops)
- [128: Should a function have only one return statement?](#128-should-a-function-have-only-one-return-statement)
- [129: How does TypeScript help with clean code?](#129-how-does-typescript-help-with-clean-code)
- [130: Why should you avoid the any type?](#130-why-should-you-avoid-the-any-type)
- [131: Should you use enums or string union types in TypeScript?](#131-should-you-use-enums-or-string-union-types-in-typescript)
- [132: Why should you keep variable scope as small as possible?](#132-why-should-you-keep-variable-scope-as-small-as-possible)
- [133: What is the principle of least astonishment?](#133-what-is-the-principle-of-least-astonishment)
- [134: Which ESLint rules help enforce clean code?](#134-which-eslint-rules-help-enforce-clean-code)
- [135: Why should pull requests and commits be small?](#135-why-should-pull-requests-and-commits-be-small)
- [136: What makes a good commit message?](#136-what-makes-a-good-commit-message)
- [137: Is clean code subjective?](#137-is-clean-code-subjective)
- [138: Does writing clean code slow you down?](#138-does-writing-clean-code-slow-you-down)
- [139: Is there a conflict between clean code and performance?](#139-is-there-a-conflict-between-clean-code-and-performance)
- [140: Why is clever code a problem?](#140-why-is-clever-code-a-problem)
- [141: How do you keep React components clean?](#141-how-do-you-keep-react-components-clean)
- [142: How do custom hooks help keep React code clean?](#142-how-do-custom-hooks-help-keep-react-code-clean)
- [143: Why are very large React components a problem?](#143-why-are-very-large-react-components-a-problem)
- [144: What is the "one level of abstraction per function" rule?](#144-what-is-the-one-level-of-abstraction-per-function-rule)
- [145: What is the problem with long conditional expressions?](#145-what-is-the-problem-with-long-conditional-expressions)
- [146: What is a "Swiss Army knife" function?](#146-what-is-a-swiss-army-knife-function)
- [147: How can you make code easier to search?](#147-how-can-you-make-code-easier-to-search)
- [148: Why prefer named exports over default exports?](#148-why-prefer-named-exports-over-default-exports)
- [149: What is "code that lies"?](#149-what-is-code-that-lies)
- [150: Which books are commonly recommended for learning clean code?](#150-which-books-are-commonly-recommended-for-learning-clean-code)

### Moderate Questions (151-300)

- [151: How do you do the Extract Function refactoring?](#151-how-do-you-do-the-extract-function-refactoring)
- [152: When would you inline a function instead of extracting one?](#152-when-would-you-inline-a-function-instead-of-extracting-one)
- [153: What is the Replace Temp with Query refactoring?](#153-what-is-the-replace-temp-with-query-refactoring)
- [154: How do you rename something safely in a large codebase?](#154-how-do-you-rename-something-safely-in-a-large-codebase)
- [155: What is the Introduce Parameter Object refactoring?](#155-what-is-the-introduce-parameter-object-refactoring)
- [156: How does Replace Conditional with Polymorphism work?](#156-how-does-replace-conditional-with-polymorphism-work)
- [157: What is the Decompose Conditional refactoring?](#157-what-is-the-decompose-conditional-refactoring)
- [158: What is the Consolidate Conditional Expression refactoring?](#158-what-is-the-consolidate-conditional-expression-refactoring)
- [159: What is the Split Phase refactoring?](#159-what-is-the-split-phase-refactoring)
- [160: When should you move a function to another module or class?](#160-when-should-you-move-a-function-to-another-module-or-class)
- [161: What is the Extract Class refactoring?](#161-what-is-the-extract-class-refactoring)
- [162: What is a value object?](#162-what-is-a-value-object)
- [163: What does it mean to encapsulate a collection?](#163-what-does-it-mean-to-encapsulate-a-collection)
- [164: How do you remove a flag argument?](#164-how-do-you-remove-a-flag-argument)
- [165: What is the Replace Loop with Pipeline refactoring?](#165-what-is-the-replace-loop-with-pipeline-refactoring)
- [166: What is the Split Variable refactoring?](#166-what-is-the-split-variable-refactoring)
- [167: How do you refactor safely, step by step?](#167-how-do-you-refactor-safely-step-by-step)
- [168: Why should refactoring and behavior changes be in separate commits?](#168-why-should-refactoring-and-behavior-changes-be-in-separate-commits)
- [169: How do you apply SRP to a React component?](#169-how-do-you-apply-srp-to-a-react-component)
- [170: What is a "fat controller" and how do you fix it?](#170-what-is-a-fat-controller-and-how-do-you-fix-it)
- [171: What is the difference between SRP and "a function should do one thing"?](#171-what-is-the-difference-between-srp-and-a-function-should-do-one-thing)
- [172: Can you explain the "actor" idea in SRP with an example?](#172-can-you-explain-the-actor-idea-in-srp-with-an-example)
- [173: Can SRP be taken too far?](#173-can-srp-be-taken-too-far)
- [174: How does Express middleware show the Open/Closed Principle?](#174-how-does-express-middleware-show-the-openclosed-principle)
- [175: How can a lookup table help with the Open/Closed Principle?](#175-how-can-a-lookup-table-help-with-the-openclosed-principle)
- [176: How does composition in React relate to the Open/Closed Principle?](#176-how-does-composition-in-react-relate-to-the-openclosed-principle)
- [177: When is it fine to just modify code instead of following OCP?](#177-when-is-it-fine-to-just-modify-code-instead-of-following-ocp)
- [178: Why is throwing "not implemented" in a subclass an LSP problem?](#178-why-is-throwing-not-implemented-in-a-subclass-an-lsp-problem)
- [179: What are preconditions and postconditions in LSP?](#179-what-are-preconditions-and-postconditions-in-lsp)
- [180: Does TypeScript's type checker guarantee LSP?](#180-does-typescripts-type-checker-guarantee-lsp)
- [181: How do you apply ISP in TypeScript?](#181-how-do-you-apply-isp-in-typescript)
- [182: How does ISP apply to React component props?](#182-how-does-isp-apply-to-react-component-props)
- [183: What is a role interface?](#183-what-is-a-role-interface)
- [184: How would you apply DIP in a typical Node.js backend?](#184-how-would-you-apply-dip-in-a-typical-nodejs-backend)
- [185: How can you apply DIP in a React app?](#185-how-can-you-apply-dip-in-a-react-app)
- [186: How does NestJS support dependency injection?](#186-how-does-nestjs-support-dependency-injection)
- [187: What is a composition root?](#187-what-is-a-composition-root)
- [188: What is the difference between a stub, a mock, a spy and a fake?](#188-what-is-the-difference-between-a-stub-a-mock-a-spy-and-a-fake)
- [189: Why are fakes often better than mocks?](#189-why-are-fakes-often-better-than-mocks)
- [190: What is over-mocking and why is it a problem?](#190-what-is-over-mocking-and-why-is-it-a-problem)
- [191: What does "test behavior, not implementation" mean?](#191-what-does-test-behavior-not-implementation-mean)
- [192: Should you test private methods?](#192-should-you-test-private-methods)
- [193: What is legacy code?](#193-what-is-legacy-code)
- [194: What is a characterization test?](#194-what-is-a-characterization-test)
- [195: What is a seam in legacy code?](#195-what-is-a-seam-in-legacy-code)
- [196: How do you add tests to code that's hard to test?](#196-how-do-you-add-tests-to-code-thats-hard-to-test)
- [197: How do you deal with time and randomness to keep code testable?](#197-how-do-you-deal-with-time-and-randomness-to-keep-code-testable)
- [198: What is the Null Object pattern?](#198-what-is-the-null-object-pattern)
- [199: What is the Result type pattern?](#199-what-is-the-result-type-pattern)
- [200: How do you create custom error classes, and why?](#200-how-do-you-create-custom-error-classes-and-why)
- [201: What is the difference between cyclomatic and cognitive complexity?](#201-what-is-the-difference-between-cyclomatic-and-cognitive-complexity)
- [202: Should you organize folders by feature or by type?](#202-should-you-organize-folders-by-feature-or-by-type)
- [203: Why are circular dependencies a problem and how do you fix them?](#203-why-are-circular-dependencies-a-problem-and-how-do-you-fix-them)
- [204: What are the pros and cons of barrel files?](#204-what-are-the-pros-and-cons-of-barrel-files)
- [205: What is an anemic domain model?](#205-what-is-an-anemic-domain-model)
- [206: How do you break up a God class step by step?](#206-how-do-you-break-up-a-god-class-step-by-step)
- [207: What is "functional core, imperative shell"?](#207-what-is-functional-core-imperative-shell)
- [208: How should you handle configuration cleanly?](#208-how-should-you-handle-configuration-cleanly)
- [209: How do feature flags affect code cleanliness?](#209-how-do-feature-flags-affect-code-cleanliness)
- [210: What does clean logging look like?](#210-what-does-clean-logging-look-like)
- [211: When should you use Promise.all instead of sequential awaits?](#211-when-should-you-use-promiseall-instead-of-sequential-awaits)
- [212: What is a floating promise and why is it a bug risk?](#212-what-is-a-floating-promise-and-why-is-it-a-bug-risk)
- [213: Where should errors be caught in a layered application?](#213-where-should-errors-be-caught-in-a-layered-application)
- [214: Why should input be validated at the boundaries of the system?](#214-why-should-input-be-validated-at-the-boundaries-of-the-system)
- [215: What is the difference between defensive programming and trusting your inputs?](#215-what-is-the-difference-between-defensive-programming-and-trusting-your-inputs)
- [216: How do you use assertions to protect invariants?](#216-how-do-you-use-assertions-to-protect-invariants)
- [217: What is the "wrong abstraction" and why can it be worse than duplication?](#217-what-is-the-wrong-abstraction-and-why-can-it-be-worse-than-duplication)
- [218: What do the acronyms WET and AHA mean?](#218-what-do-the-acronyms-wet-and-aha-mean)
- [219: Is DRY about code or about knowledge?](#219-is-dry-about-code-or-about-knowledge)
- [220: How do you balance DRY and coupling between services or packages?](#220-how-do-you-balance-dry-and-coupling-between-services-or-packages)
- [221: When should you write JSDoc or TSDoc comments?](#221-when-should-you-write-jsdoc-or-tsdoc-comments)
- [222: What is an Architecture Decision Record (ADR)?](#222-what-is-an-architecture-decision-record-adr)
- [223: How should you structure tests with describe and it blocks?](#223-how-should-you-structure-tests-with-describe-and-it-blocks)
- [224: What are test data builders or factories?](#224-what-are-test-data-builders-or-factories)
- [225: Why should tests avoid logic like loops and conditionals?](#225-why-should-tests-avoid-logic-like-loops-and-conditionals)
- [226: What makes tests flaky and how do you avoid it?](#226-what-makes-tests-flaky-and-how-do-you-avoid-it)
- [227: What does code coverage tell you, and what doesn't it tell you?](#227-what-does-code-coverage-tell-you-and-what-doesnt-it-tell-you)
- [228: What are the pros and cons of snapshot tests?](#228-what-are-the-pros-and-cons-of-snapshot-tests)
- [229: What is the testing pyramid, and what is the testing trophy?](#229-what-is-the-testing-pyramid-and-what-is-the-testing-trophy)
- [230: What is the Repository pattern?](#230-what-is-the-repository-pattern)
- [231: What is a service layer?](#231-what-is-a-service-layer)
- [232: What are DTOs and why map between them and domain objects?](#232-what-are-dtos-and-why-map-between-them-and-domain-objects)
- [233: What is the difference between Template Method and Strategy?](#233-what-is-the-difference-between-template-method-and-strategy)
- [234: How does the Decorator pattern help follow the Open/Closed Principle?](#234-how-does-the-decorator-pattern-help-follow-the-openclosed-principle)
- [235: Why should you wrap third-party libraries?](#235-why-should-you-wrap-third-party-libraries)
- [236: When is a factory function useful?](#236-when-is-a-factory-function-useful)
- [237: How do events help decouple code?](#237-how-do-events-help-decouple-code)
- [238: What is the dependency rule in a layered architecture?](#238-what-is-the-dependency-rule-in-a-layered-architecture)
- [239: How can you enforce import rules in a codebase?](#239-how-can-you-enforce-import-rules-in-a-codebase)
- [240: How do you give code review feedback about clean code without being rude?](#240-how-do-you-give-code-review-feedback-about-clean-code-without-being-rude)
- [241: What static analysis tools help measure code quality?](#241-what-static-analysis-tools-help-measure-code-quality)
- [242: How does pair programming help code quality?](#242-how-does-pair-programming-help-code-quality)
- [243: How would you refactor a long function with many responsibilities? Walk through an example.](#243-how-would-you-refactor-a-long-function-with-many-responsibilities-walk-through-an-example)
- [244: How do you replace boolean parameters with an options object?](#244-how-do-you-replace-boolean-parameters-with-an-options-object)
- [245: How do you decide if a comment should be turned into code?](#245-how-do-you-decide-if-a-comment-should-be-turned-into-code)
- [246: What is the "boolean trap" in APIs?](#246-what-is-the-boolean-trap-in-apis)
- [247: How do you keep a module's public API small?](#247-how-do-you-keep-a-modules-public-api-small)
- [248: What is temporal coupling?](#248-what-is-temporal-coupling)
- [249: What is a hidden dependency?](#249-what-is-a-hidden-dependency)
- [250: Why are singletons often considered a code smell?](#250-why-are-singletons-often-considered-a-code-smell)
- [251: How do discriminated unions make state handling cleaner?](#251-how-do-discriminated-unions-make-state-handling-cleaner)
- [252: How do you make a switch statement exhaustive in TypeScript?](#252-how-do-you-make-a-switch-statement-exhaustive-in-typescript)
- [253: How do readonly and as const help write cleaner TypeScript?](#253-how-do-readonly-and-as-const-help-write-cleaner-typescript)
- [254: When are generics a good idea and when do they hurt readability?](#254-when-are-generics-a-good-idea-and-when-do-they-hurt-readability)
- [255: Should you use function overloads or union parameter types?](#255-should-you-use-function-overloads-or-union-parameter-types)
- [256: What is wrong with having many optional parameters?](#256-what-is-wrong-with-having-many-optional-parameters)
- [257: How do you keep REST API naming clean and consistent?](#257-how-do-you-keep-rest-api-naming-clean-and-consistent)
- [258: How do clean code ideas apply to CSS?](#258-how-do-clean-code-ideas-apply-to-css)
- [259: How do clean code ideas apply to SQL?](#259-how-do-clean-code-ideas-apply-to-sql)
- [260: Why should a team have a written style guide?](#260-why-should-a-team-have-a-written-style-guide)
- [261: How do you share formatting and editor settings across a team?](#261-how-do-you-share-formatting-and-editor-settings-across-a-team)
- [262: How do pre-commit hooks help keep code clean?](#262-how-do-pre-commit-hooks-help-keep-code-clean)
- [263: What are quality gates in CI?](#263-what-are-quality-gates-in-ci)
- [264: Why should you remove unused dependencies?](#264-why-should-you-remove-unused-dependencies)
- [265: How do higher-order functions support SOLID?](#265-how-do-higher-order-functions-support-solid)
- [266: How can closures be used for dependency injection?](#266-how-can-closures-be-used-for-dependency-injection)
- [267: When should you use classes and when plain functions in TypeScript?](#267-when-should-you-use-classes-and-when-plain-functions-in-typescript)
- [268: Why can too many getters and setters be a problem?](#268-why-can-too-many-getters-and-setters-be-a-problem)
- [269: What is the difference between readonly in TypeScript and Object.freeze?](#269-what-is-the-difference-between-readonly-in-typescript-and-objectfreeze)
- [270: What are the types of cohesion, from worst to best?](#270-what-are-the-types-of-cohesion-from-worst-to-best)
- [271: What are the types of coupling, from worst to best?](#271-what-are-the-types-of-coupling-from-worst-to-best)
- [272: What is control coupling and how do you avoid it?](#272-what-is-control-coupling-and-how-do-you-avoid-it)
- [273: What is stamp coupling and when does it matter?](#273-what-is-stamp-coupling-and-when-does-it-matter)
- [274: How do you avoid misusing useEffect in React?](#274-how-do-you-avoid-misusing-useeffect-in-react)
- [275: What is derived state and why shouldn't you store it?](#275-what-is-derived-state-and-why-shouldnt-you-store-it)
- [276: What is state colocation?](#276-what-is-state-colocation)
- [277: When should you use React context instead of passing props?](#277-when-should-you-use-react-context-instead-of-passing-props)
- [278: What are compound components?](#278-what-are-compound-components)
- [279: Is the container/presentational pattern still useful in React?](#279-is-the-containerpresentational-pattern-still-useful-in-react)
- [280: How do error boundaries help keep React code clean?](#280-how-do-error-boundaries-help-keep-react-code-clean)
- [281: How should you name event handlers and callback props in React?](#281-how-should-you-name-event-handlers-and-callback-props-in-react)
- [282: How do you keep a global store (Redux, Zustand) clean as it grows?](#282-how-do-you-keep-a-global-store-redux-zustand-clean-as-it-grows)
- [283: How should a front-end API client layer look?](#283-how-should-a-front-end-api-client-layer-look)
- [284: Why should business logic stay out of UI components?](#284-why-should-business-logic-stay-out-of-ui-components)
- [285: How do you handle errors in async Express route handlers cleanly?](#285-how-do-you-handle-errors-in-async-express-route-handlers-cleanly)
- [286: How do you handle cross-cutting concerns cleanly?](#286-how-do-you-handle-cross-cutting-concerns-cleanly)
- [287: How can TypeScript decorators help with cross-cutting concerns?](#287-how-can-typescript-decorators-help-with-cross-cutting-concerns)
- [288: How do you override dependencies in tests when using DI?](#288-how-do-you-override-dependencies-in-tests-when-using-di)
- [289: What are contract tests for interface implementations?](#289-what-are-contract-tests-for-interface-implementations)
- [290: Should repositories be tested with unit tests or integration tests?](#290-should-repositories-be-tested-with-unit-tests-or-integration-tests)
- [291: What is mutation testing?](#291-what-is-mutation-testing)
- [292: How do you convince a manager to spend time on refactoring?](#292-how-do-you-convince-a-manager-to-spend-time-on-refactoring)
- [293: How should a team track technical debt?](#293-how-should-a-team-track-technical-debt)
- [294: What questions do you ask to check SOLID in a code review?](#294-what-questions-do-you-ask-to-check-solid-in-a-code-review)
- [295: What is the Strangler Fig pattern?](#295-what-is-the-strangler-fig-pattern)
- [296: How do you introduce SOLID into an existing codebase without a rewrite?](#296-how-do-you-introduce-solid-into-an-existing-codebase-without-a-rewrite)
- [297: What is the difference between a library and a framework, in terms of dependency direction?](#297-what-is-the-difference-between-a-library-and-a-framework-in-terms-of-dependency-direction)
- [298: What is Inversion of Control?](#298-what-is-inversion-of-control)
- [299: How do you keep a long list of if-else checks for validation clean?](#299-how-do-you-keep-a-long-list-of-if-else-checks-for-validation-clean)
- [300: How do you make sure clean code rules don't slow the team down?](#300-how-do-you-make-sure-clean-code-rules-dont-slow-the-team-down)

### Advanced Questions (301-450)

- [301: What are the main criticisms of the "Clean Code" book?](#301-what-are-the-main-criticisms-of-the-clean-code-book)
- [302: What are deep and shallow modules?](#302-what-are-deep-and-shallow-modules)
- [303: What is information hiding?](#303-what-is-information-hiding)
- [304: What is information leakage?](#304-what-is-information-leakage)
- [305: Is SOLID still relevant today?](#305-is-solid-still-relevant-today)
- [306: How does SOLID map to functional programming?](#306-how-does-solid-map-to-functional-programming)
- [307: How do SOLID principles apply at the architecture level?](#307-how-do-solid-principles-apply-at-the-architecture-level)
- [308: Can applying SRP to microservices go wrong?](#308-can-applying-srp-to-microservices-go-wrong)
- [309: How does Conway's law relate to SRP?](#309-how-does-conways-law-relate-to-srp)
- [310: What are the package cohesion principles REP, CCP and CRP?](#310-what-are-the-package-cohesion-principles-rep-ccp-and-crp)
- [311: Why is there tension between REP, CCP and CRP?](#311-why-is-there-tension-between-rep-ccp-and-crp)
- [312: What is the Acyclic Dependencies Principle?](#312-what-is-the-acyclic-dependencies-principle)
- [313: What is the Stable Dependencies Principle?](#313-what-is-the-stable-dependencies-principle)
- [314: What is the Stable Abstractions Principle?](#314-what-is-the-stable-abstractions-principle)
- [315: How do you measure a module's instability?](#315-how-do-you-measure-a-modules-instability)
- [316: What are the "zone of pain" and the "zone of uselessness"?](#316-what-are-the-zone-of-pain-and-the-zone-of-uselessness)
- [317: What is connascence?](#317-what-is-connascence)
- [318: How do you use connascence's strength, locality and degree?](#318-how-do-you-use-connascences-strength-locality-and-degree)
- [319: What is the history constraint in the Liskov Substitution Principle?](#319-what-is-the-history-constraint-in-the-liskov-substitution-principle)
- [320: How do covariance and contravariance relate to LSP?](#320-how-do-covariance-and-contravariance-relate-to-lsp)
- [321: How does TypeScript handle parameter variance, and what is method bivariance?](#321-how-does-typescript-handle-parameter-variance-and-what-is-method-bivariance)
- [322: Why are arrays in TypeScript an LSP risk?](#322-why-are-arrays-in-typescript-an-lsp-risk)
- [323: What is Design by Contract?](#323-what-is-design-by-contract)
- [324: How does LSP apply to exceptions?](#324-how-does-lsp-apply-to-exceptions)
- [325: What is "protected variation"?](#325-what-is-protected-variation)
- [326: How do you decide where to put extension points?](#326-how-do-you-decide-where-to-put-extension-points)
- [327: How do you resolve the tension between OCP and YAGNI?](#327-how-do-you-resolve-the-tension-between-ocp-and-yagni)
- [328: What is the difference between a header interface and a role interface, and why does it matter for ISP?](#328-what-is-the-difference-between-a-header-interface-and-a-role-interface-and-why-does-it-matter-for-isp)
- [329: Under DIP, who should own the interface?](#329-under-dip-who-should-own-the-interface)
- [330: How do you apply DIP across packages in a monorepo?](#330-how-do-you-apply-dip-across-packages-in-a-monorepo)
- [331: What is the Service Locator pattern and why is it often called an anti-pattern?](#331-what-is-the-service-locator-pattern-and-why-is-it-often-called-an-anti-pattern)
- [332: What are the pros and cons of DI containers?](#332-what-are-the-pros-and-cons-of-di-containers)
- [333: What is constructor over-injection and what does it tell you?](#333-what-is-constructor-over-injection-and-what-does-it-tell-you)
- [334: What is an aggregate service (or facade service) in the context of DI?](#334-what-is-an-aggregate-service-or-facade-service-in-the-context-of-di)
- [335: What is Clean Architecture?](#335-what-is-clean-architecture)
- [336: What is hexagonal architecture (ports and adapters)?](#336-what-is-hexagonal-architecture-ports-and-adapters)
- [337: How do Clean, Hexagonal and Onion architectures differ?](#337-how-do-clean-hexagonal-and-onion-architectures-differ)
- [338: What is "screaming architecture"?](#338-what-is-screaming-architecture)
- [339: Is Clean Architecture overkill for most web apps?](#339-is-clean-architecture-overkill-for-most-web-apps)
- [340: What is vertical slice architecture?](#340-what-is-vertical-slice-architecture)
- [341: What is a use case (or interactor) in Clean Architecture?](#341-what-is-a-use-case-or-interactor-in-clean-architecture)
- [342: What is the cost of mapping data between layers, and how do you keep it manageable?](#342-what-is-the-cost-of-mapping-data-between-layers-and-how-do-you-keep-it-manageable)
- [343: What does "the framework is a detail" mean?](#343-what-does-the-framework-is-a-detail-mean)
- [344: Is treating the database as a detail realistic?](#344-is-treating-the-database-as-a-detail-realistic)
- [345: What are entities, value objects and aggregates in Domain-Driven Design?](#345-what-are-entities-value-objects-and-aggregates-in-domain-driven-design)
- [346: How do aggregates protect invariants?](#346-how-do-aggregates-protect-invariants)
- [347: What are bounded contexts and the ubiquitous language?](#347-what-are-bounded-contexts-and-the-ubiquitous-language)
- [348: What is an anti-corruption layer?](#348-what-is-an-anti-corruption-layer)
- [349: What is the difference between domain events and integration events?](#349-what-is-the-difference-between-domain-events-and-integration-events)
- [350: How do you deal with naming when two parts of the business use the same word differently?](#350-how-do-you-deal-with-naming-when-two-parts-of-the-business-use-the-same-word-differently)
- [351: What does "make illegal states unrepresentable" mean?](#351-what-does-make-illegal-states-unrepresentable-mean)
- [352: What does "parse, don't validate" mean?](#352-what-does-parse-dont-validate-mean)
- [353: What are branded types in TypeScript?](#353-what-are-branded-types-in-typescript)
- [354: What are the trade-offs of heavy type-driven design in TypeScript?](#354-what-are-the-trade-offs-of-heavy-type-driven-design-in-typescript)
- [355: What are the trade-offs between Result types and exceptions in TypeScript?](#355-what-are-the-trade-offs-between-result-types-and-exceptions-in-typescript)
- [356: How do you document which errors a function can throw when TypeScript has no checked exceptions?](#356-how-do-you-document-which-errors-a-function-can-throw-when-typescript-has-no-checked-exceptions)
- [357: How do you wrap errors without losing context?](#357-how-do-you-wrap-errors-without-losing-context)
- [358: How should a Node.js process handle unexpected errors at the top level?](#358-how-should-a-nodejs-process-handle-unexpected-errors-at-the-top-level)
- [359: What is "test-induced design damage"?](#359-what-is-test-induced-design-damage)
- [360: What are the London (mockist) and Chicago (classicist) schools of TDD?](#360-what-are-the-london-mockist-and-chicago-classicist-schools-of-tdd)
- [361: What are sociable and solitary unit tests?](#361-what-are-sociable-and-solitary-unit-tests)
- [362: What is a "unit" in unit testing?](#362-what-is-a-unit-in-unit-testing)
- [363: How can test fakes drift away from the real implementation, and how do you prevent it?](#363-how-can-test-fakes-drift-away-from-the-real-implementation-and-how-do-you-prevent-it)
- [364: What is property-based testing?](#364-what-is-property-based-testing)
- [365: What is approval testing (golden master testing)?](#365-what-is-approval-testing-golden-master-testing)
- [366: How do you refactor safely when you can't add tests first?](#366-how-do-you-refactor-safely-when-you-cant-add-tests-first)
- [367: What is the Parallel Change (expand and contract) technique?](#367-what-is-the-parallel-change-expand-and-contract-technique)
- [368: What is Branch by Abstraction?](#368-what-is-branch-by-abstraction)
- [369: How do codemods help with large-scale refactoring?](#369-how-do-codemods-help-with-large-scale-refactoring)
- [370: What is the Mikado Method?](#370-what-is-the-mikado-method)
- [371: What is hotspot analysis, and how does it help decide where to refactor?](#371-what-is-hotspot-analysis-and-how-does-it-help-decide-where-to-refactor)
- [372: Why can code quality metrics be dangerous as targets?](#372-why-can-code-quality-metrics-be-dangerous-as-targets)
- [373: What is the "clean code, horrible performance" debate about?](#373-what-is-the-clean-code-horrible-performance-debate-about)
- [374: How do abstractions affect performance in JavaScript specifically?](#374-how-do-abstractions-affect-performance-in-javascript-specifically)
- [375: How does immutability affect performance, and how do libraries help?](#375-how-does-immutability-affect-performance-and-how-do-libraries-help)
- [376: When is duplication better than abstraction in performance-critical code?](#376-when-is-duplication-better-than-abstraction-in-performance-critical-code)
- [377: How can shared mutable state cause race conditions in single-threaded Node.js?](#377-how-can-shared-mutable-state-cause-race-conditions-in-single-threaded-nodejs)
- [378: What is the fragile base class problem in detail?](#378-what-is-the-fragile-base-class-problem-in-detail)
- [379: Why did React move from class components and mixins to hooks?](#379-why-did-react-move-from-class-components-and-mixins-to-hooks)
- [380: How do you do composition with delegation in TypeScript?](#380-how-do-you-do-composition-with-delegation-in-typescript)
- [381: What are mixins in TypeScript, and when should you use them?](#381-what-are-mixins-in-typescript-and-when-should-you-use-them)
- [382: How does semantic versioning relate to OCP and LSP?](#382-how-does-semantic-versioning-relate-to-ocp-and-lsp)
- [383: What is Hyrum's law and how does it affect API design?](#383-what-is-hyrums-law-and-how-does-it-affect-api-design)
- [384: What is a leaky abstraction?](#384-what-is-a-leaky-abstraction)
- [385: Why are ORMs often called leaky abstractions?](#385-why-are-orms-often-called-leaky-abstractions)
- [386: What does Ousterhout mean by "general-purpose modules are deeper"?](#386-what-does-ousterhout-mean-by-general-purpose-modules-are-deeper)
- [387: What does "define errors out of existence" mean?](#387-what-does-define-errors-out-of-existence-mean)
- [388: What does "pull complexity downwards" mean?](#388-what-does-pull-complexity-downwards-mean)
- [389: What is the difference between tactical and strategic programming?](#389-what-is-the-difference-between-tactical-and-strategic-programming)
- [390: What is the second-system effect, and how does it relate to rewrites?](#390-what-is-the-second-system-effect-and-how-does-it-relate-to-rewrites)
- [391: What is Postel's law, and why is it now questioned?](#391-what-is-postels-law-and-why-is-it-now-questioned)
- [392: How should you think about comments according to Ousterhout, compared to "Clean Code"?](#392-how-should-you-think-about-comments-according-to-ousterhout-compared-to-clean-code)
- [393: How do you choose between a short name and a precise name?](#393-how-do-you-choose-between-a-short-name-and-a-precise-name)
- [394: How does team ownership affect code quality?](#394-how-does-team-ownership-affect-code-quality)
- [395: What is the difference between essential and accidental complexity?](#395-what-is-the-difference-between-essential-and-accidental-complexity)
- [396: What does "coupling is the enemy of change" mean in practice for modern web apps?](#396-what-does-coupling-is-the-enemy-of-change-mean-in-practice-for-modern-web-apps)
- [397: How do you design a stable API contract between front-end and back-end?](#397-how-do-you-design-a-stable-api-contract-between-front-end-and-back-end)
- [398: What is the "Tell, Don't Ask" principle's limit?](#398-what-is-the-tell-dont-ask-principles-limit)
- [399: How do you keep a codebase consistent when many teams work in it?](#399-how-do-you-keep-a-codebase-consistent-when-many-teams-work-in-it)
- [400: How has AI-assisted coding changed the importance of clean code?](#400-how-has-ai-assisted-coding-changed-the-importance-of-clean-code)
- [401: A checkout function has a switch over payment providers that grows every month. How would you redesign it?](#401-a-checkout-function-has-a-switch-over-payment-providers-that-grows-every-month-how-would-you-redesign-it)
- [402: A notification service sends email, SMS and push, and some channels don't support all features (like attachments). How do you model it?](#402-a-notification-service-sends-email-sms-and-push-and-some-channels-dont-support-all-features-like-attachments-how-do-you-model-it)
- [403: A form component has grown to 30 props. How do you clean it up?](#403-a-form-component-has-grown-to-30-props-how-do-you-clean-it-up)
- [404: You inherit a 3,000-line utils.ts that everything imports. What do you do?](#404-you-inherit-a-3000-line-utilsts-that-everything-imports-what-do-you-do)
- [405: A service class takes 12 constructor dependencies. How do you approach it?](#405-a-service-class-takes-12-constructor-dependencies-how-do-you-approach-it)
- [406: Your team's tests break on every refactor, even when behavior doesn't change. What's going wrong and how do you fix it?](#406-your-teams-tests-break-on-every-refactor-even-when-behavior-doesnt-change-whats-going-wrong-and-how-do-you-fix-it)
- [407: A Bird base class has a fly() method, and now you need a Penguin. What do you do?](#407-a-bird-base-class-has-a-fly-method-and-now-you-need-a-penguin-what-do-you-do)
- [408: Discount rules change every week and the code is a growing if-else chain. How would you restructure it?](#408-discount-rules-change-every-week-and-the-code-is-a-growing-if-else-chain-how-would-you-restructure-it)
- [409: What is the Specification pattern?](#409-what-is-the-specification-pattern)
- [410: Your team keeps arguing about how much abstraction to add. How do you resolve it?](#410-your-team-keeps-arguing-about-how-much-abstraction-to-add-how-do-you-resolve-it)
- [411: A junior developer submitted a pull request with factories, strategies and an abstract base class for a feature that has one case. How do you review it?](#411-a-junior-developer-submitted-a-pull-request-with-factories-strategies-and-an-abstract-base-class-for-a-feature-that-has-one-case-how-do-you-review-it)
- [412: You must change a feature in a legacy Express app with no tests and global state everywhere. Where do you start?](#412-you-must-change-a-feature-in-a-legacy-express-app-with-no-tests-and-global-state-everywhere-where-do-you-start)
- [413: Validation rules are duplicated between the React front-end and the Node back-end and keep drifting apart. How do you fix it?](#413-validation-rules-are-duplicated-between-the-react-front-end-and-the-node-back-end-and-keep-drifting-apart-how-do-you-fix-it)
- [414: Should business logic live in the database (stored procedures, triggers) or in the application?](#414-should-business-logic-live-in-the-database-stored-procedures-triggers-or-in-the-application)
- [415: The users module imports from the orders module and orders imports from users. How do you break the cycle?](#415-the-users-module-imports-from-the-orders-module-and-orders-imports-from-users-how-do-you-break-the-cycle)
- [416: A shared "common" library is used by 20 services and every change needs coordinated releases. What do you do?](#416-a-shared-common-library-is-used-by-20-services-and-every-change-needs-coordinated-releases-what-do-you-do)
- [417: How would you refactor a function like exportData(format, compress, encrypt, upload)?](#417-how-would-you-refactor-a-function-like-exportdataformat-compress-encrypt-upload)
- [418: You need to replace a third-party analytics SDK that is called directly in 200 places. How do you do it?](#418-you-need-to-replace-a-third-party-analytics-sdk-that-is-called-directly-in-200-places-how-do-you-do-it)
- [419: A single React context holds the user, theme, cart and feature flags, and the app re-renders too much. How do you fix it?](#419-a-single-react-context-holds-the-user-theme-cart-and-feature-flags-and-the-app-re-renders-too-much-how-do-you-fix-it)
- [420: A function returns a string, a number, null or an array depending on its input. How do you clean it up?](#420-a-function-returns-a-string-a-number-null-or-an-array-depending-on-its-input-how-do-you-clean-it-up)
- [421: Error handling is inconsistent across the codebase. How do you bring it under control?](#421-error-handling-is-inconsistent-across-the-codebase-how-do-you-bring-it-under-control)
- [422: The unit test suite takes 20 minutes because every test hits a real database. How do you speed it up while keeping confidence?](#422-the-unit-test-suite-takes-20-minutes-because-every-test-hits-a-real-database-how-do-you-speed-it-up-while-keeping-confidence)
- [423: In a live coding interview, you're asked to refactor a messy function. How do you approach it?](#423-in-a-live-coding-interview-youre-asked-to-refactor-a-messy-function-how-do-you-approach-it)
- [424: Should shared HTTP behavior (auth headers, retries, logging) be done with inheritance or composition?](#424-should-shared-http-behavior-auth-headers-retries-logging-be-done-with-inheritance-or-composition)
- [425: A team uses classes with only static methods for everything. What's the problem?](#425-a-team-uses-classes-with-only-static-methods-for-everything-whats-the-problem)
- [426: How would you migrate a large codebase that uses any everywhere to strict TypeScript?](#426-how-would-you-migrate-a-large-codebase-that-uses-any-everywhere-to-strict-typescript)
- [427: A front-end codebase has a deep BaseComponent > FormComponent > ValidatedFormComponent hierarchy. How do you get out of it?](#427-a-front-end-codebase-has-a-deep-basecomponent--formcomponent--validatedformcomponent-hierarchy-how-do-you-get-out-of-it)
- [428: How would you design a plugin system for a web application?](#428-how-would-you-design-a-plugin-system-for-a-web-application)
- [429: Different tenants need slightly different behavior, and the code is full of if (tenant === "acme"). How do you clean it up?](#429-different-tenants-need-slightly-different-behavior-and-the-code-is-full-of-if-tenant--acme-how-do-you-clean-it-up)
- [430: Your app talks to a REST API, and you need to migrate to a GraphQL API gradually. How do you structure it?](#430-your-app-talks-to-a-rest-api-and-you-need-to-migrate-to-a-graphql-api-gradually-how-do-you-structure-it)
- [431: How do you handle resource cleanup (listeners, timers, connections) cleanly?](#431-how-do-you-handle-resource-cleanup-listeners-timers-connections-cleanly)
- [432: How does explicit resource management with using work?](#432-how-does-explicit-resource-management-with-using-work)
- [433: Logging is scattered and sometimes includes passwords and tokens. How do you fix it?](#433-logging-is-scattered-and-sometimes-includes-passwords-and-tokens-how-do-you-fix-it)
- [434: Date handling code is spread all over the app with manual timezone math. What would you do?](#434-date-handling-code-is-spread-all-over-the-app-with-manual-timezone-math-what-would-you-do)
- [435: Code was made very DRY across three teams' features, and now every change needs all three teams to agree. What happened, and how do you fix it?](#435-code-was-made-very-dry-across-three-teams-features-and-now-every-change-needs-all-three-teams-to-agree-what-happened-and-how-do-you-fix-it)
- [436: When would you choose a state machine for UI or business logic?](#436-when-would-you-choose-a-state-machine-for-ui-or-business-logic)
- [437: What is the State pattern and how does it differ from a reducer-style state machine?](#437-what-is-the-state-pattern-and-how-does-it-differ-from-a-reducer-style-state-machine)
- [438: How does the Command pattern help with features like undo or job queues?](#438-how-does-the-command-pattern-help-with-features-like-undo-or-job-queues)
- [439: What is CQRS, and how is it related to Command-Query Separation?](#439-what-is-cqrs-and-how-is-it-related-to-command-query-separation)
- [440: When is event sourcing overkill?](#440-when-is-event-sourcing-overkill)
- [441: How do you know when to stop refactoring?](#441-how-do-you-know-when-to-stop-refactoring)
- [442: How do you measure if a refactoring was successful?](#442-how-do-you-measure-if-a-refactoring-was-successful)
- [443: How do you make a codebase easy for new developers to understand?](#443-how-do-you-make-a-codebase-easy-for-new-developers-to-understand)
- [444: How do you balance simplicity and flexibility in a design?](#444-how-do-you-balance-simplicity-and-flexibility-in-a-design)
- [445: How do you design for testability without over-abstracting?](#445-how-do-you-design-for-testability-without-over-abstracting)
- [446: What would you put in a team's definition of "clean enough" for a pull request?](#446-what-would-you-put-in-a-teams-definition-of-clean-enough-for-a-pull-request)
- [447: How would you explain SOLID to a non-technical stakeholder?](#447-how-would-you-explain-solid-to-a-non-technical-stakeholder)
- [448: What are common mistakes when applying SOLID?](#448-what-are-common-mistakes-when-applying-solid)
- [449: How do clean code principles change between a startup prototype and a mature product?](#449-how-do-clean-code-principles-change-between-a-startup-prototype-and-a-mature-product)
- [450: What is your overall approach to writing clean code day to day?](#450-what-is-your-overall-approach-to-writing-clean-code-day-to-day)

---

# Easy Questions (1-150)

## 1: What is clean code?

Clean code is code that other people (and you, six months later) can read, understand and change without much trouble. It has clear names, small focused functions, no surprises, and tests that show it works.

It's not about clever tricks or making the code as short as possible. The main question is: how long does it take someone new to understand this and safely change it?

## 2: Why does clean code matter if the code already works?

Code is read many more times than it's written. Every bug fix and new feature starts with someone reading the existing code. If that code is messy, each change takes longer and is more likely to break something.

Messy code also slows the team down over time. At first you ship fast, but after a year every small change takes days because nobody is sure what the code does.

## 3: Who is Robert C. Martin and why is he linked to clean code?

Robert C. Martin, often called "Uncle Bob", is a software engineer who wrote the book "Clean Code" (2008) and later "Clean Architecture" (2017). He also put the SOLID principles together under that name in the early 2000s (the acronym itself was suggested by Michael Feathers).

His books are not the only source on this topic, and some of his advice is debated today, but most interview questions about clean code come from his ideas.

## 4: What does SOLID stand for?

SOLID is five design principles for object-oriented code:

- **S**ingle Responsibility Principle: a module should have one reason to change.
- **O**pen/Closed Principle: open for extension, closed for modification.
- **L**iskov Substitution Principle: subtypes must be usable wherever the base type is expected.
- **I**nterface Segregation Principle: don't force clients to depend on methods they don't use.
- **D**ependency Inversion Principle: depend on abstractions, not on concrete details.

## 5: What is the Single Responsibility Principle?

The Single Responsibility Principle (SRP) says a class or module should have only one reason to change. Robert Martin later explained it as "a module should be responsible to one, and only one, actor", meaning one group of people who ask for changes.

For example, a class that calculates an invoice total and also formats it as a PDF has two reasons to change: billing rules and document layout. Splitting it into two classes means a layout change can't break the math.

## 6: What is the Open/Closed Principle?

The Open/Closed Principle (OCP) says code should be open for extension but closed for modification. You should be able to add new behavior by adding new code, not by editing code that already works and is tested.

A common way to do this is to depend on an interface and add new implementations of it, instead of adding another `if` branch to an existing function every time a new case appears.

## 7: What is the Liskov Substitution Principle?

The Liskov Substitution Principle (LSP), named after Barbara Liskov, says that if `B` is a subtype of `A`, you should be able to use a `B` anywhere an `A` is expected without the program breaking or behaving strangely.

In practice, a subclass should not throw errors the parent doesn't throw, should not demand stricter input, and should not return weaker results than the parent promises.

## 8: What is the Interface Segregation Principle?

The Interface Segregation Principle (ISP) says clients should not be forced to depend on methods they don't use. Instead of one big interface, prefer several small ones that each fit a specific need.

If a `Printer` interface has `print`, `scan` and `fax`, a simple printer class has to implement `scan` and `fax` with empty bodies or errors. Splitting it into `Printer`, `Scanner` and `Fax` fixes that.

## 9: What is the Dependency Inversion Principle?

The Dependency Inversion Principle (DIP) has two parts:

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

For example, an `OrderService` should depend on an `OrderRepository` interface, not directly on a `PostgresOrderRepository` class. Then you can swap the database or use a fake in tests without touching the service.

## 10: Why are meaningful names important?

Names are the first thing a reader sees, and they are most of what the reader uses to understand code. A good name tells you what something is or does, so you don't have to read its implementation.

```ts
// Bad
const d = 7;

// Good
const daysUntilExpiry = 7;
```

If you need a comment to explain what a variable holds, the name is probably not good enough.

## 11: What makes a good variable name?

A good variable name:

- Says what the value is, not how it's stored (`users`, not `userArray`).
- Is specific enough to be clear in its scope (`retryCount`, not `count` if there are several counts).
- Is pronounceable and searchable (`createdAt`, not `crtdTs`).
- Matches the words the team and the business use.

The longer a variable lives and the wider its scope, the more descriptive its name should be. A loop index `i` is fine; a module-level `i` is not.

## 12: How should you name functions?

Functions do things, so name them with a verb or verb phrase: `sendEmail`, `calculateTotal`, `isValid`, `getUserById`.

The name should describe everything the function does. If the honest name is `validateAndSaveAndNotify`, that's a sign the function does too much and should be split.

## 13: How should you name classes?

Classes usually represent things, so name them with nouns or noun phrases: `Invoice`, `UserRepository`, `PaymentGateway`.

Avoid vague names like `Manager`, `Processor`, `Helper` or `Data` on their own. They don't say what the class does and tend to become a place where unrelated code piles up.

## 14: How should you name boolean variables?

Name booleans so they read like a yes/no question: `isActive`, `hasPermission`, `canEdit`, `shouldRetry`.

Avoid negative names like `isNotValid` or `disableLogging`, because conditions like `if (!isNotValid)` are hard to read. Use the positive form and negate it when needed.

## 15: What is a magic number and why is it a problem?

A magic number is a literal number in the code with no explanation of what it means.

```ts
// Bad
if (password.length < 8) { ... }
setTimeout(refresh, 300000);

// Good
const MIN_PASSWORD_LENGTH = 8;
const FIVE_MINUTES_MS = 5 * 60 * 1000;

if (password.length < MIN_PASSWORD_LENGTH) { ... }
setTimeout(refresh, FIVE_MINUTES_MS);
```

Named constants explain the meaning, and if the value changes you update one place instead of searching for every `8` in the codebase. The same goes for magic strings like `"admin"` or `"pending"`.

## 16: Should you use abbreviations in names?

Mostly no. Abbreviations save a few keystrokes but cost reading time, and different people abbreviate differently (`usr`, `usrNm`, `uName`).

Common, well-known abbreviations are fine: `id`, `url`, `html`, `api`, `db`. Everything else should be written out. Editors autocomplete long names anyway.

## 17: What is Hungarian notation and should you use it?

Hungarian notation puts the type in the name, like `strName`, `iCount` or `arrUsers`. It made sense in languages without good type info in the editor.

With TypeScript and modern editors you can see the type by hovering, so the prefix just adds noise and can lie if the type changes. The one prefix many TypeScript codebases still drop is `I` for interfaces (`IUser`); the official TypeScript style does not use it.

## 18: What does "use consistent names" mean?

Pick one word per concept and use it everywhere. If you fetch data with `getUser` in one place, don't use `fetchOrder`, `retrieveProduct` and `loadInvoice` for the same kind of operation in others.

Consistency lets readers guess names correctly and search the codebase easily. It also helps to use the same words the business uses (if the product team says "subscription", don't call it `plan` in code).

## 19: How long should a function be?

There's no exact number, but shorter is usually better. A common guideline is that a function should fit on your screen without scrolling, and often it's much shorter, around 5 to 20 lines.

The real rule is that a function should do one thing at one level of detail. If you can pull out part of it into a well-named function, it's probably doing more than one thing.

## 20: What does "a function should do one thing" mean?

It means everything inside the function works toward a single purpose, at the same level of detail. A quick test: can you describe what the function does without using "and"?

```ts
// Does several things
function registerUser(data) {
  // validate input
  // hash password
  // save to database
  // send welcome email
}

// Does one thing: coordinates the steps
async function registerUser(data: SignupData) {
  const input = validateSignup(data);
  const user = createUser(input);
  await userRepository.save(user);
  await sendWelcomeEmail(user);
}
```

The second version still does several steps, but its one job is "register a user", and each step lives in its own function.

## 21: How many parameters should a function have?

Fewer is better. Zero to two parameters is easy to read. Three is acceptable. More than that is hard to remember and easy to pass in the wrong order.

When you need many values, group them into an object:

```ts
// Hard to read at the call site
createUser("Ann", "ann@example.com", true, false, "admin");

// Clear
createUser({
  name: "Ann",
  email: "ann@example.com",
  isVerified: true,
  sendWelcomeEmail: false,
  role: "admin",
});
```

## 22: What is a flag argument and why is it considered a code smell?

A flag argument is a boolean parameter that changes what the function does:

```ts
render(user, true);
```

At the call site you can't tell what `true` means. It also shows that the function does two different things depending on the flag. A cleaner option is usually two functions, like `renderPreview(user)` and `renderFull(user)`, or at least a named option like `render(user, { preview: true })`.

## 23: What is a side effect?

A side effect is anything a function does besides returning a value: changing a variable outside itself, writing to a database, logging, sending an HTTP request, or changing its input.

Side effects are not bad in themselves; programs need them. The problem is hidden side effects. A function called `checkPassword` that also logs the user in is surprising and leads to bugs. Keep side effects visible in the name and keep them separate from logic where you can.

## 24: What is a pure function?

A pure function always returns the same output for the same input and has no side effects.

```ts
// Pure
function add(a: number, b: number) {
  return a + b;
}

// Not pure: depends on and changes outside state
let total = 0;
function addToTotal(n: number) {
  total += n;
  return total;
}
```

Pure functions are easy to test, easy to reason about and safe to reuse. Clean code tries to put as much logic as possible in pure functions.

## 25: What is a guard clause?

A guard clause is an early return at the top of a function that handles an edge case so the main logic doesn't have to be nested.

```ts
function getDiscount(user: User | null) {
  if (!user) return 0;
  if (!user.isMember) return 0;

  return user.years > 5 ? 0.2 : 0.1;
}
```

Without guard clauses this would be a stack of nested `if` blocks.

## 26: Why is deep nesting a problem?

Each level of nesting is one more condition the reader has to keep in their head. Code that is four or five levels deep is hard to follow and easy to break when you change it.

Ways to reduce nesting: guard clauses and early returns, extracting the inner block into a function, and using array methods like `filter` and `map` instead of nested loops with `if` inside.

## 27: What is the DRY principle?

DRY stands for "Don't Repeat Yourself". It comes from the book "The Pragmatic Programmer", which says every piece of knowledge should have a single, clear place in the system.

If the rule "a username is 3 to 20 characters" is checked in five places and the rule changes, you'll probably miss one. Putting it in one function or constant fixes that.

## 28: What is the KISS principle?

KISS means "Keep It Simple, Stupid" (often softened to "Keep It Simple"). Pick the simplest solution that solves the actual problem.

Simple code has fewer bugs and is easier to change. Developers often add layers, abstractions or generic frameworks "just in case", and KISS is a reminder not to.

## 29: What is the YAGNI principle?

YAGNI means "You Aren't Gonna Need It". It comes from Extreme Programming: don't build features or flexibility until you actually need them.

Code you write for an imagined future still has to be read, tested and maintained today, and often the future turns out different from what you guessed. It's cheaper to add the feature when it's really needed.

## 30: What is the Boy Scout Rule?

"Leave the campground cleaner than you found it." Applied to code: whenever you touch a file, make it a little better. Rename a confusing variable, remove dead code, split a long function.

Small improvements on every change keep the codebase from slowly getting worse. Keep these cleanups small and related to what you're working on, so pull requests stay easy to review.

## 31: When are comments useful?

Comments are useful when they explain things the code can't:

- **Why** something is done in a non-obvious way ("we retry 3 times because the payment API sometimes returns 502 on the first call").
- Warnings about consequences ("this runs on every request, keep it fast").
- Legal headers, links to specs or tickets.
- Public API docs (JSDoc/TSDoc) for libraries and shared code.

## 32: When are comments a bad sign?

Comments that explain **what** the code does are usually a sign the code isn't clear enough.

```ts
// Bad: comment explains unclear code
// check if user can get free shipping
if (u.t === 2 && o.amt > 50) { ... }

// Better: code explains itself
if (user.isPremium && order.amount > FREE_SHIPPING_THRESHOLD) { ... }
```

Comments also go out of date, because people change code and forget the comment. A wrong comment is worse than none.

## 33: What should you do with commented-out code?

Delete it. Version control (Git) already keeps the old version if you ever need it.

Commented-out code confuses readers: nobody knows if it's important, why it's there, or whether it still works. Over time it piles up and nobody dares to remove it.

## 34: Are TODO comments OK?

A few are fine as short-term notes, but they tend to stay forever. If you leave one, make it useful: say what needs doing and link a ticket.

```ts
// TODO(PAY-123): remove after all clients use the v2 endpoint
```

Many teams use a lint rule or a CI check to list TODOs so they don't get forgotten.

## 35: What is self-documenting code?

Self-documenting code is code whose names and structure make it clear what it does without extra comments. You get there with good names, small functions and simple control flow.

It doesn't mean "never write comments". It means comments are saved for the "why", not the "what".

## 36: Why is consistent formatting important?

Consistent formatting means the reader can focus on what the code does instead of how it looks. It also keeps diffs clean, because changes aren't mixed with whitespace edits.

Don't argue about style in code reviews. Use a formatter like Prettier and let it decide, then run it automatically on save or in a pre-commit hook.

## 37: What is the difference between a formatter and a linter?

A formatter (like Prettier) only changes how code looks: spacing, line breaks, quotes, semicolons. It doesn't change behavior.

A linter (like ESLint) looks for problems in the code: unused variables, possible bugs, risky patterns, too-complex functions. Some lint rules can auto-fix, but their main job is catching mistakes, not layout.

## 38: What is a code smell?

A code smell is a sign that something might be wrong in the design. It's not a bug, and the code may work fine, but it often points to a problem that will make changes harder later.

The term was made popular by Kent Beck and Martin Fowler in the book "Refactoring". Common smells: long functions, large classes, duplicated code, long parameter lists and lots of `switch` statements on the same type.

## 39: What is the "long method" smell?

A function that has grown too long to understand at a glance. Long functions usually mix several tasks and several levels of detail, which makes them hard to test and easy to break.

The fix is usually "Extract Function": find blocks that do one thing (often there's a comment above them already) and move them into well-named functions.

## 40: What is the "large class" smell?

A class with too many fields, methods or lines of code. It usually has more than one responsibility, so it changes for many different reasons.

Large classes are often called "God objects" when they end up knowing about and controlling almost everything. The fix is to find groups of fields and methods that belong together and extract them into their own classes.

## 41: What is the "duplicated code" smell?

The same or very similar code appears in more than one place. When a bug is fixed in one copy, the others stay broken.

Fix it by extracting the shared part into a function, class or module. Be careful though: code that looks the same but represents different business rules may need to change separately later, so not every duplicate should be merged.

## 42: What is "dead code"?

Code that is never run or whose result is never used: unused functions, unreachable branches, old feature flags that are always off, unused variables and imports.

Dead code adds reading time and makes people afraid to change things. Delete it. Tools like ESLint (`no-unused-vars`), TypeScript (`noUnusedLocals`) and tools like Knip can find a lot of it.

## 43: What is refactoring?

Refactoring is changing the structure of code without changing what it does. The goal is to make the code easier to understand and change.

Martin Fowler describes it as a series of small, safe steps, each keeping the code working. Good tests are what make refactoring safe, because they tell you right away if you changed behavior by mistake.

## 44: Is refactoring the same as rewriting?

No. Refactoring is small steps, each keeping the program working, usually mixed in with normal feature work.

Rewriting means throwing code away and building it again. It's much riskier: it takes longer than planned, and the old code often had bug fixes and edge cases nobody remembered. Refactoring is almost always the safer choice.

## 45: When should you refactor?

Common times to refactor:

- Before adding a feature, to make the change easier ("make the change easy, then make the easy change", Kent Beck).
- When fixing a bug in code that's hard to understand.
- During code review, when something is confusing.
- When you notice the same thing done three times (the "rule of three").

Don't refactor code you don't need to touch, and don't refactor without tests if you can avoid it.

## 46: What is the "rule of three"?

The rule of three says: the first time you write something, just write it. The second time, you can tolerate the duplicate. The third time, extract it.

The idea is that two examples are often not enough to see the right abstraction. By the third you know what's really shared and what's different.

## 47: What is technical debt?

Technical debt is the extra cost of future work caused by taking shortcuts now. Ward Cunningham came up with the term: like money debt, you get something now (speed), but you pay "interest" later in slower changes and more bugs.

Some debt is a fine business choice if you plan to pay it back. The problem is debt nobody tracks, which keeps growing until every change is painful.

## 48: What is coupling?

Coupling is how much one module depends on another. With tight coupling, a change in one module forces changes in others. With loose coupling, modules can change on their own.

You want low coupling. Ways to get it: depend on interfaces instead of concrete classes, pass dependencies in instead of creating them inside, and avoid reaching into other modules' internal data.

## 49: What is cohesion?

Cohesion is how closely the things inside a module belong together. High cohesion means all the functions and data in a module work toward the same purpose.

You want high cohesion. A `DateUtils` module with date helpers is cohesive. A `Utils` module with date helpers, string helpers and API calls is not.

## 50: How are coupling and cohesion related?

They usually move together in opposite directions. When related code is grouped together (high cohesion), modules need to talk to each other less (low coupling).

The goal is often stated as "high cohesion, low coupling". SRP is mostly about cohesion, while DIP and ISP are mostly about coupling.

## 51: What is encapsulation?

Encapsulation means keeping a module's internal data and details hidden, and letting others interact with it only through a clear public interface.

```ts
class BankAccount {
  #balance = 0;

  deposit(amount: number) {
    if (amount <= 0) throw new Error("Amount must be positive");
    this.#balance += amount;
  }

  get balance() {
    return this.#balance;
  }
}
```

Nobody outside can set `#balance` to a negative number, because the only way to change it is through `deposit`, which checks the rules.

## 52: What is abstraction?

Abstraction means showing only what someone needs to use a thing and hiding how it works. When you call `fetch(url)`, you don't think about sockets or TLS.

In your own code, a good abstraction has a simple interface that matches what callers want to do, like `paymentGateway.charge(order)`, without exposing which payment provider is behind it.

## 53: What is the difference between composition and inheritance?

Inheritance is an "is-a" relationship: `Dog extends Animal`. The subclass gets the parent's code and can override parts of it.

Composition is a "has-a" relationship: a class holds other objects and uses them to do its work.

```ts
// Composition
class Car {
  constructor(
    private engine: Engine,
    private gps: Gps,
  ) {}

  start() {
    this.engine.start();
  }
}
```

## 54: Why do people say "favor composition over inheritance"?

Inheritance ties the subclass tightly to the parent. A change in the parent can break all subclasses (the "fragile base class" problem), and deep hierarchies are hard to follow.

Composition is more flexible. You can mix behaviors, swap parts at runtime and test each part on its own. Inheritance still makes sense for true "is-a" relationships with shallow hierarchies, but composition should be the default choice.

## 55: Why are interfaces useful for clean code?

An interface describes what something can do without saying how. Code that depends on an interface doesn't care which implementation it gets.

```ts
interface EmailSender {
  send(to: string, subject: string, body: string): Promise<void>;
}
```

Now the rest of the app can send emails without knowing if it's SendGrid, Amazon SES or a fake used in tests. This is the base of OCP, ISP and DIP.

## 56: What is dependency injection?

Dependency injection (DI) means a class receives the things it needs (its dependencies) from outside instead of creating them itself.

```ts
// Without DI: hard-coded dependency
class OrderService {
  private repo = new PostgresOrderRepository();
}

// With DI: dependency is passed in
class OrderService {
  constructor(private repo: OrderRepository) {}
}
```

With DI you can pass a fake repository in tests and swap the real one without changing `OrderService`.

## 57: What are the common ways to inject dependencies?

- **Constructor injection**: dependencies are passed to the constructor. This is the most common and clearest way, because the class can't be created without them.
- **Parameter injection**: the dependency is passed to the one function that needs it.
- **Property (setter) injection**: the dependency is set on a property after creation. It's easy to forget, so use it only for optional dependencies.

In frameworks like Angular and NestJS, a DI container creates objects and passes in their dependencies for you.

## 58: What is separation of concerns?

Separation of concerns means splitting a program into parts that each deal with one area: for example, UI, business logic and data access.

When concerns are mixed (a React component that builds SQL queries, say), any change touches everything. When they're separated, you can change the database without touching the UI, and test business rules without a browser.

## 59: What is the Law of Demeter?

The Law of Demeter, also called "talk only to your friends", says a method should only call methods on:

- its own object,
- its parameters,
- objects it creates,
- its direct fields.

It shouldn't reach through other objects:

```ts
// Breaks the rule
const city = order.getCustomer().getAddress().getCity();

// Better
const city = order.getShippingCity();
```

Long chains tie your code to the internal structure of many objects. If any of them changes, your code breaks.

## 60: Can you give a simple example of an SRP violation?

```ts
class UserService {
  createUser(data: UserInput) {
    if (!data.email.includes("@")) throw new Error("Invalid email");
    const user = { ...data, id: crypto.randomUUID() };
    db.query("INSERT INTO users ...", user);
    smtp.send(user.email, "Welcome!");
    console.log(`User created: ${user.id}`);
  }
}
```

This one method handles validation, saving, emailing and logging. A change in the email template, the database or the validation rules all touch the same class. A cleaner version passes in a validator, a repository and an email sender, and `createUser` only coordinates them.

## 61: How can you tell that a class has too many responsibilities?

Some warning signs:

- You can't describe the class without saying "and".
- It has many imports from unrelated areas (database, HTTP, email, file system).
- Different people or teams keep editing it for different reasons.
- Its tests need a lot of setup and mocks.
- It's very long, or its methods use different groups of fields.

## 62: Can you give a simple example of the Open/Closed Principle?

Without OCP, every new shape means editing the same function:

```ts
function area(shape: Shape) {
  if (shape.type === "circle") return Math.PI * shape.r ** 2;
  if (shape.type === "square") return shape.side ** 2;
  // add another if for every new shape
}
```

With OCP, each shape knows its own area, and you add new shapes without touching existing code:

```ts
interface Shape {
  area(): number;
}

class Circle implements Shape {
  constructor(private r: number) {}
  area() {
    return Math.PI * this.r ** 2;
  }
}

class Square implements Shape {
  constructor(private side: number) {}
  area() {
    return this.side ** 2;
  }
}

const totalArea = (shapes: Shape[]) =>
  shapes.reduce((sum, s) => sum + s.area(), 0);
```

## 63: What is the classic Rectangle and Square example of an LSP violation?

Mathematically a square is a rectangle, so it's tempting to write `class Square extends Rectangle`. But a rectangle lets you set width and height separately, and a square can't:

```ts
class Rectangle {
  constructor(
    public width: number,
    public height: number,
  ) {}
  setWidth(w: number) {
    this.width = w;
  }
  setHeight(h: number) {
    this.height = h;
  }
  area() {
    return this.width * this.height;
  }
}

class Square extends Rectangle {
  setWidth(w: number) {
    this.width = w;
    this.height = w;
  }
  setHeight(h: number) {
    this.width = h;
    this.height = h;
  }
}

function resize(r: Rectangle) {
  r.setWidth(5);
  r.setHeight(4);
  console.log(r.area()); // expects 20, a Square gives 16
}
```

Code written for `Rectangle` breaks when it gets a `Square`. The lesson: an "is-a" relationship in the real world doesn't always mean you should use inheritance in code. Here they shouldn't share a mutable base class.

## 64: Can you give a simple example of the Interface Segregation Principle?

```ts
// Too big
interface Worker {
  work(): void;
  eat(): void;
}

class Robot implements Worker {
  work() {
    /* ... */
  }
  eat() {
    throw new Error("Robots don't eat");
  }
}

// Split
interface Workable {
  work(): void;
}
interface Eatable {
  eat(): void;
}

class Human implements Workable, Eatable {
  work() {
    /* ... */
  }
  eat() {
    /* ... */
  }
}

class Robot implements Workable {
  work() {
    /* ... */
  }
}
```

Now `Robot` doesn't have to pretend it can eat.

## 65: Can you give a simple example of the Dependency Inversion Principle?

```ts
// The high-level code defines what it needs
interface Logger {
  log(message: string): void;
}

class CheckoutService {
  constructor(private logger: Logger) {}

  checkout(orderId: string) {
    // business logic
    this.logger.log(`Order ${orderId} checked out`);
  }
}

// Low-level details implement it
class ConsoleLogger implements Logger {
  log(message: string) {
    console.log(message);
  }
}

const service = new CheckoutService(new ConsoleLogger());
```

`CheckoutService` doesn't know about the console, a file or a logging service. It only knows the `Logger` interface.

## 66: Is the Dependency Inversion Principle the same as dependency injection?

No. They're related but different:

- **Dependency Inversion** is a design rule: depend on abstractions, and let the high-level code own those abstractions.
- **Dependency Injection** is a technique: pass dependencies in from outside.

You can use DI and still break DIP (injecting a concrete `PostgresRepository` class). And you can follow DIP without a DI framework, just by passing interfaces through constructors by hand.

## 67: Does SOLID only apply to classes and object-oriented code?

The principles were written with OOP in mind, but the ideas apply to functions and modules too.

- SRP: a function or a module should have one job.
- OCP: you can extend behavior by passing in functions (callbacks, strategies) instead of editing code.
- ISP: a function should take only the data it needs, not a huge object.
- DIP: pass functions or modules as parameters instead of importing concrete implementations directly.

In React, for example, SRP applies to components and hooks just as much as to classes.

## 68: Should you use exceptions or error codes?

In JavaScript and TypeScript, throwing errors is the normal way to signal something unexpected went wrong. Error codes (returning `-1` or `false`) are easy to ignore, and the caller has to check every return value.

For errors that are an expected part of the flow (like "user not found" or "validation failed"), some teams return a result object instead of throwing, so the type system forces callers to handle it. Either way, be consistent across the codebase.

## 69: Why is an empty catch block a bad idea?

An empty `catch` hides the error. The program keeps going in a broken state, and when something fails later, there's no trace of the real cause.

```ts
// Bad
try {
  await saveOrder(order);
} catch {}

// Better
try {
  await saveOrder(order);
} catch (error) {
  logger.error("Failed to save order", { orderId: order.id, error });
  throw error;
}
```

If you really mean to ignore an error, write a comment that explains why.

## 70: Why should you avoid returning null?

Every function that might return `null` forces every caller to check for it. Forget one check and you get "Cannot read properties of null".

Alternatives:

- Return an empty array or empty object for "no results".
- Throw an error if a missing value is truly unexpected.
- Use a type like `User | undefined` with `strictNullChecks` on, so TypeScript forces callers to handle it.
- Use the Null Object pattern (a default object that does nothing).

## 71: What makes a good error message?

A good error message says what went wrong, with enough context to find the cause, and ideally what to do about it.

```ts
// Bad
throw new Error("Invalid input");

// Good
throw new Error(`Invalid email "${email}" for user ${userId}: missing @`);
```

Be careful not to put passwords, tokens or other secrets in error messages, since they end up in logs.

## 72: What does "fail fast" mean?

Fail fast means checking for problems as early as possible and stopping right away with a clear error, instead of carrying bad data through the system.

For example, check that required environment variables exist when the app starts, not when the first request needs them an hour later. Validate input at the edge of your API, not deep inside the database layer.

## 73: Why are tests important for clean code?

Tests let you change code without fear. Without them, every refactor is a risk, so people stop cleaning code and it slowly rots.

Tests also act as living documentation: they show how the code is meant to be used and what it should do in edge cases.

## 74: What makes a test clean?

A clean test:

- Tests one behavior and has a name that says which.
- Is easy to read top to bottom, with obvious setup, action and check.
- Doesn't depend on other tests or on running in a certain order.
- Doesn't hide important values in shared helpers far away.
- Fails with a message that tells you what broke.

Test code is real code. It deserves the same care as production code.

## 75: What is the Arrange-Act-Assert pattern?

Arrange-Act-Assert (AAA) splits a test into three parts:

```ts
test("applies 10% discount for members", () => {
  // Arrange
  const cart = new Cart({ isMember: true });
  cart.add({ price: 100 });

  // Act
  const total = cart.total();

  // Assert
  expect(total).toBe(90);
});
```

It makes tests easy to scan. The same idea is called Given-When-Then in BDD.

## 76: What are the FIRST principles for tests?

FIRST describes good unit tests:

- **Fast**: they run in milliseconds, so you run them often.
- **Independent**: they don't depend on each other or on order.
- **Repeatable**: same result every time, on any machine (no reliance on real time, network or random data without a seed).
- **Self-validating**: they pass or fail on their own; nobody reads logs to decide.
- **Timely**: written at the same time as (or before) the code.

## 77: Should a test have only one assertion?

The rule is better stated as "one behavior per test". Several assertions are fine if they all check the same behavior, like checking a few fields of a returned object.

What you want to avoid is one big test that checks five unrelated things. When it fails, you don't know which behavior broke, and the first failing assertion hides the rest.

## 78: How should you name tests?

A test name should say what behavior is being checked and under what condition, so that a failing test explains itself.

```ts
// Vague
test("discount", ...);

// Clear
test("gives no discount when cart total is below 50", ...);
test("throws when coupon has expired", ...);
```

Reading just the test names should give a good idea of what the code does.

## 79: What is test-driven development (TDD)?

TDD is a way of working where you write a failing test before the code that makes it pass. You repeat this in small cycles.

It pushes you toward small, testable units with clear interfaces, because hard-to-test code is painful to write tests for first. Not every team uses strict TDD, but the habit of thinking about tests early tends to produce cleaner code.

## 80: What is the red-green-refactor cycle?

It's the TDD loop:

1. **Red**: write a small test that fails.
2. **Green**: write the simplest code that makes it pass.
3. **Refactor**: clean up the code (and tests) while keeping all tests green.

The refactor step is the one people skip, and it's where most of the clean code comes from.

## 81: How does code review help keep code clean?

Code review gets a second pair of eyes on every change. The reviewer is a fresh reader, so if they find something confusing, future readers will too.

It also spreads knowledge across the team and keeps conventions consistent. Leave style questions to tools like Prettier and ESLint, so reviews can focus on design, naming, correctness and tests.

## 82: What should you look for when reviewing code for cleanliness?

- Are names clear and consistent?
- Does each function and class do one thing?
- Is there duplication that should be shared?
- Are errors handled properly, not swallowed?
- Are there tests, and do they test behavior rather than internals?
- Is anything over-engineered for the current need?
- Would someone new to this code understand it?

## 83: What is the "long parameter list" smell?

A function with many parameters is hard to call correctly. It's easy to swap two arguments of the same type, and it often means the function does too much.

Fixes: group related parameters into an object (Introduce Parameter Object), pass a whole object instead of picking fields out of it, or split the function.

## 84: What is primitive obsession?

Primitive obsession is using basic types (`string`, `number`, `boolean`) for things that have their own rules and meaning, like money, email addresses, phone numbers or IDs.

```ts
// Easy to mix up
function transfer(fromId: string, toId: string, amount: number) {}

// Clearer
function transfer(from: AccountId, to: AccountId, amount: Money) {}
```

A small type or class for the concept puts its validation and behavior in one place.

## 85: What are data clumps?

Data clumps are groups of values that always appear together, like `street`, `city`, `zip` and `country`, or `startDate` and `endDate`.

If you keep passing the same three or four values around together, make them one object (`Address`, `DateRange`). It shortens parameter lists and gives you a home for related logic, like `dateRange.contains(date)`.

## 86: What is feature envy?

Feature envy is when a method uses another object's data more than its own. It's a sign the method lives in the wrong place.

```ts
// In some OrderPrinter class
function shippingLabel(order: Order) {
  return `${order.customer.name}, ${order.customer.address.street}, ${order.customer.address.city}`;
}
```

This logic is mostly about the customer's address, so it probably belongs on `Customer` or `Address`.

## 87: What is shotgun surgery?

Shotgun surgery is when one small change forces you to edit many files in many places. For example, adding a new user role means touching 15 files.

It means one concept is spread across the codebase instead of being in one place. The fix is to move the scattered pieces together.

## 88: What is divergent change?

Divergent change is the opposite of shotgun surgery: one class gets changed for many different, unrelated reasons. You edit it when the database changes, when the UI changes and when tax rules change.

It's a direct sign of an SRP violation. Split the class so each part changes for one reason.

## 89: Why are repeated switch statements considered a smell?

One `switch` isn't a problem. The smell is when the same `switch` on the same type shows up in many places. When a new case appears, you have to find and update every one of them.

Fixes: replace the switch with polymorphism (each type implements its own behavior), or use a lookup map in one place.

```ts
const shippingCost: Record<ShippingType, number> = {
  standard: 5,
  express: 15,
  overnight: 30,
};
```

## 90: What is speculative generality?

Speculative generality is code written for future needs that never came: abstract base classes with one subclass, unused parameters, hooks nobody calls, config options nobody sets.

It's the opposite of YAGNI. Remove it. If the need ever shows up, you'll design it better with real requirements in hand.

## 91: What is the "comments as deodorant" idea?

It's a phrase from Martin Fowler's "Refactoring": comments are sometimes used to cover up bad code, like deodorant covers a smell.

When you feel the need to write a comment explaining a block of code, first try to make the code clearer: extract a function with a good name, rename variables, simplify the logic. Often the comment then isn't needed.

## 92: What is a temporary field?

A temporary field is a class field that is only set and used in some situations and is empty the rest of the time. Readers can't tell when it's valid.

```ts
class ReportGenerator {
  private tempTotals?: number[]; // only used inside generate()
}
```

Fix it by making it a local variable, passing it as a parameter, or moving the code that uses it into its own class.

## 93: What is a message chain?

A message chain is a long line of calls where each one returns another object, like `a.getB().getC().getD().doSomething()`.

It ties the caller to the whole structure in between. This is what the Law of Demeter warns about. Fix it by adding a method on the first object that does the work, so the caller doesn't need to know the path.

## 94: What is the "middle man" smell?

A middle man is a class where most methods just pass calls to another class without adding anything.

```ts
class UserManager {
  constructor(private repo: UserRepository) {}
  find(id: string) {
    return this.repo.find(id);
  }
  save(user: User) {
    return this.repo.save(user);
  }
}
```

If the class adds no value, remove it and let callers use the real object. This is the opposite side of the Law of Demeter, so you need balance between the two.

## 95: What is a lazy class?

A lazy class is a class that does so little it isn't worth having: maybe it was shrunk by refactoring, or it was created for a future need that never came.

Every class costs something to read and understand. If it doesn't pull its weight, merge it into the class that uses it.

## 96: What is inappropriate intimacy?

Inappropriate intimacy is when two classes know too much about each other's internals, like reading each other's private fields or depending on each other's internal structure.

It makes both hard to change. Move methods so each class handles its own data, or extract the shared part into a third class.

## 97: What is "refused bequest"?

Refused bequest is when a subclass inherits methods or data it doesn't want, and overrides them to do nothing or throw errors.

It's a sign the inheritance is wrong, and often an LSP violation too. Use composition instead, or move the unwanted methods out of the base class.

## 98: What is a "mysterious name"?

A mysterious name is a function, variable or class name that doesn't tell you what it does: `process()`, `handle()`, `data2`, `doStuff`, `tmp`.

Martin Fowler put it first in the list of smells in the second edition of "Refactoring", because renaming is the simplest and often most useful refactoring. If you can't think of a good name, that's often a hint the code itself isn't clear yet.

## 99: Why is global mutable state a problem?

Global mutable state can be changed from anywhere, so when it has the wrong value you have to search the whole codebase to find out who changed it.

It also makes tests depend on each other (one test leaves the global in a weird state for the next) and causes bugs with concurrency. Prefer passing data explicitly, or keep state inside a module with a small, controlled set of functions that change it.

## 100: Why does clean code prefer immutable data?

Immutable data can't change after it's created. If an object can't change, you don't have to wonder whether some other function changed it behind your back.

```ts
// Mutating
function addItem(cart: Cart, item: Item) {
  cart.items.push(item);
}

// Not mutating
function addItem(cart: Cart, item: Item): Cart {
  return { ...cart, items: [...cart.items, item] };
}
```

React state, Redux and many other tools rely on this, since they compare references to know what changed.

## 101: What is polymorphism and how does it help clean code?

Polymorphism means different types can be used through the same interface, and each one does the right thing on its own. The caller doesn't need to check which type it has.

```ts
interface Notifier {
  notify(message: string): Promise<void>;
}

async function alertAll(notifiers: Notifier[], message: string) {
  for (const n of notifiers) await n.notify(message);
}
```

`alertAll` works for email, SMS and Slack notifiers without a single `if`. Adding a new channel means adding a class, not editing this function.

## 102: What is the Strategy pattern?

The Strategy pattern puts each variant of an algorithm behind the same interface, so you can pick one at runtime.

```ts
type PricingStrategy = (base: number) => number;

const regular: PricingStrategy = (base) => base;
const blackFriday: PricingStrategy = (base) => base * 0.7;

function finalPrice(base: number, strategy: PricingStrategy) {
  return strategy(base);
}
```

It's one of the most common ways to follow the Open/Closed Principle. In TypeScript a strategy can simply be a function.

## 103: What does "program to an interface, not an implementation" mean?

It means your code should depend on what an object can do (its interface), not on the specific class behind it.

If a function takes a `Storage` interface instead of `LocalStorageAdapter`, it works with any storage: local storage, IndexedDB, or an in-memory fake in tests. The phrase comes from the "Design Patterns" book by the Gang of Four.

## 104: What is spaghetti code?

Spaghetti code is code with tangled, hard-to-follow control flow. Everything calls everything, logic jumps around, and there's no clear structure.

It usually grows over time from quick fixes without refactoring. You can't change one part without understanding the whole thing, which is exactly what clean code tries to avoid.

## 105: What is wrong with copy-paste programming?

Copy-paste programming means copying a block of code and tweaking it instead of reusing or generalizing it. It's fast at first, but every copy carries the same bugs, and fixes must be applied to all of them.

It also hides the differences between copies: a reader has to compare them line by line to see what's actually different.

## 106: What is premature optimization?

Premature optimization means making code faster (and usually more complicated) before you know it's a performance problem. Donald Knuth said "premature optimization is the root of all evil".

Write clear code first, then measure. Optimize only the parts the profiler shows are slow, and keep the rest readable.

## 107: What is cyclomatic complexity?

Cyclomatic complexity counts the number of independent paths through a function. Every `if`, `else if`, loop, `case`, `&&`, `||` and `?:` adds one.

A function with complexity 1 has a single path. Over about 10, it's hard to understand and needs many tests to cover every path. ESLint has a `complexity` rule to warn when functions get too complex.

## 108: Why should files be kept small?

Small files are easier to read, easier to name and easier to review. A 3,000-line file almost always has several responsibilities mixed together.

There's no strict limit, but if a file is hard to scroll through or hard to give a single name, it's a sign to split it. Many teams use the ESLint `max-lines` rule as a soft warning.

## 109: What is the stepdown rule?

The stepdown rule says code should read from top to bottom like a story, going from high-level to low-level. The main function comes first, and the functions it calls come right after it.

```ts
export function generateReport(orders: Order[]) {
  const totals = calculateTotals(orders);
  return formatReport(totals);
}

function calculateTotals(orders: Order[]) {
  /* ... */
}

function formatReport(totals: Totals) {
  /* ... */
}
```

The reader can stop reading once they've gone deep enough.

## 110: What is the newspaper metaphor in clean code?

A source file should read like a newspaper article. The headline (file and class name) tells you what it's about. The first lines give the big picture. Details come further down.

A reader should be able to understand the main idea from the top of the file and only scroll down if they need the details.

## 111: How should you use blank lines and vertical spacing?

Use blank lines to separate different ideas, like paragraphs in text. Keep related lines close together without blank lines between them.

For example, put a blank line between the setup and the main logic of a function, and keep a variable's declaration close to where it's used. Formatters handle indentation, but grouping lines is still up to you.

## 112: What is the problem with "utils" or "helpers" files?

A file called `utils.ts` or `helpers.ts` has no clear purpose, so everything ends up in it: date formatting, API calls, string helpers, validation. It becomes a large, low-cohesion module that everything imports.

Name files by what they contain instead: `formatDate.ts`, `currency.ts`, `slugify.ts`. Or put the helper next to the feature that uses it.

## 113: What is Command-Query Separation?

Command-Query Separation (CQS), from Bertrand Meyer, says a function should either do something (a command) or answer something (a query), but not both.

```ts
// Mixes both: changes state and returns whether it worked
if (set("username", "bob")) { ... }

// Separated
if (!exists("username")) {
  set("username", "bob");
}
```

Queries with no side effects are safe to call any number of times, which makes code easier to reason about. Some common exceptions exist, like `array.pop()` or `stack.pop()`.

## 114: What does "tell, don't ask" mean?

"Tell, don't ask" means you should tell an object what to do instead of asking it for its data and making the decision yourself.

```ts
// Asking
if (account.balance >= amount) {
  account.balance -= amount;
}

// Telling
account.withdraw(amount);
```

The rule about having enough money now lives inside `Account`, where it belongs, instead of being repeated by every caller.

## 115: What is an explaining variable?

An explaining variable is a local variable that gives a name to part of a complex expression.

```ts
// Hard to read
if (user.age >= 18 && user.country === "US" && !user.isBanned && user.emailVerified) { ... }

// Clearer
const isAdult = user.age >= 18;
const isUsUser = user.country === "US";
const canParticipate = isAdult && isUsUser && !user.isBanned && user.emailVerified;

if (canParticipate) { ... }
```

## 116: What is "mental mapping" in names?

Mental mapping is when the reader has to translate a name in their head to know what it means. For example, `r` is "the URL with the protocol removed", or `x` holds "the current customer".

Readers shouldn't have to remember a private dictionary. Use the real name: `hostAndPath`, `customer`.

## 117: What are noise words in names?

Noise words are parts of a name that add length but no meaning: `Data`, `Info`, `Object`, `Manager`, `the`, `a`.

`ProductData` and `ProductInfo` and `Product` likely mean the same thing, and a reader can't tell the difference. If two names need to be different, make the difference meaningful: `ProductSummary` vs `ProductDetails`.

## 118: Why should you avoid cute or funny names?

Names like `nukeAll()`, `yeet()` or `holyHandGrenade()` might be funny to the author, but other people won't know what they do, and the joke stops being funny after the first read.

Use clear, boring names: `deleteAllItems()`. Code is for communicating with other developers, not for jokes.

## 119: How should you name arrays and collections?

Use the plural of what's inside: `users`, `orderIds`, `selectedFiles`. In a loop, the singular name works for each item:

```ts
for (const user of users) {
  sendInvite(user);
}
```

For maps, a name that shows the key and value helps: `usersById`, `priceBySku`.

## 120: What are the common naming conventions in JavaScript and TypeScript?

- `camelCase` for variables, functions and methods: `userName`, `getUser`.
- `PascalCase` for classes, interfaces, types, enums and React components: `UserService`, `OrderStatus`, `UserCard`.
- `UPPER_SNAKE_CASE` for true constants, usually module-level: `MAX_RETRIES`, `API_URL`.
- `kebab-case` is common for file names: `user-service.ts` (though some teams use `PascalCase` for component files).

The exact style matters less than using it consistently across the project.

## 121: Why should you avoid double negatives?

Double negatives force the reader to stop and work out the logic:

```ts
// Hard
if (!isNotEnabled) { ... }
if (!user.isNotVerified === false) { ... }

// Easy
if (isEnabled) { ... }
```

Name booleans in the positive form and negate them only once if you need to.

## 122: When is the ternary operator a good idea and when not?

A ternary is great for short, simple choices between two values:

```ts
const label = isActive ? "Active" : "Inactive";
```

It becomes hard to read when it's nested or when the branches are long or have side effects. In those cases use `if`/`else`, a lookup object, or extract a function.

```ts
// Hard to read
const fee = a ? (b ? 1 : c ? 2 : 3) : 4;
```

## 123: How do optional chaining and nullish coalescing help clean code?

Optional chaining (`?.`) and nullish coalescing (`??`) replace long null checks with short, readable code:

```ts
// Before
const city =
  user && user.address && user.address.city ? user.address.city : "Unknown";

// After
const city = user?.address?.city ?? "Unknown";
```

Use `??` instead of `||` for defaults when `0`, `""` or `false` are valid values, since `||` would replace them too.

## 124: How does destructuring improve readability?

Destructuring pulls out the values you need with their names, so the code below doesn't repeat `props.` or `user.` everywhere. In function parameters, it also documents which fields the function actually uses.

```ts
function UserCard({ name, email, avatarUrl }: UserCardProps) {
  return (
    <div>
      <img src={avatarUrl} alt="" />
      <p>{name}</p>
      <p>{email}</p>
    </div>
  );
}
```

## 125: Why should you prefer const over let?

`const` tells the reader the variable won't be reassigned, so they don't have to look for later changes. Use `let` only when you really need to reassign, and avoid `var` (it's function-scoped and hoisted, which causes surprising bugs).

Note that `const` doesn't make objects immutable; it only prevents reassigning the variable.

## 126: Why is async/await usually cleaner than callbacks or promise chains?

`async`/`await` lets you write asynchronous code that reads top to bottom like normal code, with normal `try`/`catch` for errors.

```ts
// Promise chain
getUser(id)
  .then((user) => getOrders(user.id))
  .then((orders) => render(orders))
  .catch(handleError);

// async/await
try {
  const user = await getUser(id);
  const orders = await getOrders(user.id);
  render(orders);
} catch (error) {
  handleError(error);
}
```

Nested callbacks ("callback hell") are the hardest to read of all.

## 127: When are array methods like map and filter cleaner than loops?

Array methods say what you're doing, not how:

```ts
const activeEmails = users
  .filter((user) => user.isActive)
  .map((user) => user.email);
```

A `for` loop with an `if` and a `push` does the same thing but the reader has to work out the intent. Loops are still fine when you need to `break` early, do `await` in sequence, or when performance really matters in a hot path.

## 128: Should a function have only one return statement?

The "single exit point" rule comes from older languages like C, where multiple returns could skip cleanup code. In modern languages with `try`/`finally` and garbage collection, it's not needed.

Early returns usually make code cleaner, because they handle edge cases first and leave the main logic un-nested. Just avoid return statements hidden deep in the middle of a long function.

## 129: How does TypeScript help with clean code?

TypeScript makes the shape of data explicit. Function signatures tell you what goes in and what comes out without reading the body. Renaming and refactoring are safer, because the compiler finds every place you broke.

It also catches whole classes of bugs, like typos in property names and missing null checks, before the code runs.

## 130: Why should you avoid the any type?

`any` turns off type checking for that value and everything it touches. Bugs that TypeScript would catch slip through, and readers lose the information about what the value really is.

Use a real type, a generic, or `unknown` (which forces you to check the type before using the value). ESLint's `@typescript-eslint/no-explicit-any` rule helps keep `any` out.

## 131: Should you use enums or string union types in TypeScript?

Both name a fixed set of values. Many teams prefer string union types:

```ts
type OrderStatus = "pending" | "paid" | "shipped";
```

They have no runtime code, work well with JSON, and give good autocomplete. TypeScript enums generate extra JavaScript and have some odd behavior (numeric enums accept any number). Also, newer Node.js "type stripping" mode doesn't support enums. If you want a runtime object too, a `const` object with `as const` is a common middle ground.

## 132: Why should you keep variable scope as small as possible?

The smaller a variable's scope, the fewer lines can read or change it, so there's less to keep in your head.

Declare variables close to where they're used, inside the block that needs them. Prefer local variables over class fields, and class fields over module-level or global variables.

## 133: What is the principle of least astonishment?

The principle of least astonishment (or least surprise) says code should behave the way people expect from its name and context.

A function called `getUser` shouldn't create a user if one doesn't exist. A `sort` helper shouldn't also remove duplicates. When code surprises readers, they make wrong assumptions and introduce bugs.

## 134: Which ESLint rules help enforce clean code?

Some useful built-in ESLint rules:

- `complexity`: limits cyclomatic complexity.
- `max-depth`: limits how deep blocks can nest.
- `max-params`: limits function parameters.
- `max-lines-per-function` and `max-lines`: warn about long functions and files.
- `no-unused-vars`, `no-shadow`, `eqeqeq`, `prefer-const`.

Plugins like `typescript-eslint`, `eslint-plugin-unicorn` and `eslint-plugin-sonarjs` add more. Treat size limits as warnings that start a conversation, not hard rules.

## 135: Why should pull requests and commits be small?

Small pull requests are easier to review well. A reviewer looking at 50 lines will actually read them; a reviewer looking at 2,000 lines will just scroll and approve.

Small changes are also easier to revert if something goes wrong, and less likely to conflict with other people's work. Keep refactors and feature changes in separate commits so reviewers can see what changed behavior.

## 136: What makes a good commit message?

A good commit message says what changed and why, in a way that helps someone reading the history later.

```text
fix(cart): round totals to two decimals before tax

Tax was calculated on unrounded totals, which caused 1-cent
differences between the cart and the invoice.
```

Many teams use Conventional Commits (`feat:`, `fix:`, `refactor:`), which also makes changelogs easier to generate.

## 137: Is clean code subjective?

Partly. People disagree on details like function length, how many comments to write, or how much to abstract.

But many things are not subjective: clear names beat cryptic ones, duplicated business rules lead to bugs, and code without tests is risky to change. A team should agree on its conventions, write them down, and enforce what it can with tools.

## 138: Does writing clean code slow you down?

In the very short term, a little: naming things well and writing tests takes some extra minutes. But messy code slows you down quickly, often within weeks, because every change takes longer and causes more bugs.

For throwaway prototypes or one-off scripts, it's fine to care less. For code that will live and change, clean code is faster overall.

## 139: Is there a conflict between clean code and performance?

Sometimes, but less often than people think. Most performance problems come from bad algorithms, too many network calls or database queries, not from extracting a small function.

Write clean code first and measure. If a hot spot really needs optimizing, do it in that one place, keep it well isolated, and add a comment explaining why it looks the way it does.

## 140: Why is clever code a problem?

Clever code uses tricks to be short or impressive: dense one-liners, bitwise hacks, unusual language features. It feels good to write but is slow to read and easy to break.

```ts
// Clever
const r = a.reduce(
  (m, x) => ((m[x.k] ??= []).push(x), m),
  {} as Record<string, X[]>,
);

// Clear
const grouped = Object.groupBy(items, (item) => item.key);
```

Write code for the person who will maintain it, and assume they're tired and in a hurry.

## 141: How do you keep React components clean?

- Keep components small and focused on one piece of UI.
- Move data fetching and complex logic into custom hooks or separate modules.
- Split big components into smaller ones when the JSX gets long.
- Give props clear names and types, and avoid passing huge objects when only two fields are needed.
- Avoid deep prop drilling; use composition (`children`) or context when it fits.

## 142: How do custom hooks help keep React code clean?

Custom hooks pull state and side-effect logic out of components, so the component only deals with rendering.

```tsx
function useUser(id: string) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    let ignore = false;
    fetchUser(id).then((u) => {
      if (!ignore) setUser(u);
    });
    return () => {
      ignore = true;
    };
  }, [id]);

  return user;
}

function Profile({ id }: { id: string }) {
  const user = useUser(id);
  if (!user) return <Spinner />;
  return <h1>{user.name}</h1>;
}
```

The logic can be reused and tested on its own, and the component is easy to read. (In real apps a data library like TanStack Query often replaces hand-written fetching hooks.)

## 143: Why are very large React components a problem?

A 500-line component usually mixes data fetching, state, business rules and a lot of markup. It's hard to read, hard to test and re-renders more than it needs to.

Split it by responsibility: pull logic into hooks, and pull sections of the UI into smaller components with clear props.

## 144: What is the "one level of abstraction per function" rule?

All the statements in a function should be at the same level of detail. Mixing high-level steps with low-level details makes the function hard to read.

```ts
// Mixed levels
async function checkout(cart: Cart) {
  validateCart(cart);
  const total = cart.items.reduce((s, i) => s + i.price * i.qty, 0) * 1.2;
  await chargeCustomer(cart.customerId, total);
}

// Same level
async function checkout(cart: Cart) {
  validateCart(cart);
  const total = calculateTotalWithTax(cart);
  await chargeCustomer(cart.customerId, total);
}
```

## 145: What is the problem with long conditional expressions?

Long conditions with many `&&` and `||` are hard to read and easy to get wrong, especially when mixed without parentheses.

Extract them into a well-named variable or function:

```ts
function isEligibleForRefund(order: Order) {
  return order.status === "delivered" && daysSince(order.deliveredAt) <= 30 && !order.isFinalSale;
}

if (isEligibleForRefund(order)) { ... }
```

## 146: What is a "Swiss Army knife" function?

It's a function that tries to handle every possible case through lots of options and flags: `formatData(data, type, mode, options, extra)`. It ends up with a huge body full of `if`s for each combination.

It's usually cleaner to have several small, specific functions (`formatCurrency`, `formatDate`) than one generic one with ten options.

## 147: How can you make code easier to search?

- Use full, unique names instead of short ones (`MAX_UPLOAD_SIZE_MB` is easy to grep, `7` isn't).
- Avoid building names dynamically, like `this["handle" + type]()`, because nobody can find the callers with a search.
- Use named exports instead of default exports, so the same thing has the same name everywhere it's imported.
- Keep translation keys, event names and route names as constants.

## 148: Why prefer named exports over default exports?

With default exports, each file can import the same thing under a different name:

```ts
import Button from "./Button";
import Btn from "./Button";
```

Named exports force a consistent name, help editors auto-import and refactor reliably, and make search work. Some frameworks still require default exports in certain files, like Next.js pages, so use them there.

## 149: What is "code that lies"?

Code that lies is code where the names, comments or types say one thing and the behavior does another. For example, `isValid()` that also saves to the database, a comment describing old behavior, or a type that says `string` while the value is sometimes `null`.

It's worse than unclear code, because readers trust it and build bugs on top of it. Keep names, comments and types up to date when you change behavior.

## 150: Which books are commonly recommended for learning clean code?

- "Clean Code" by Robert C. Martin
- "Refactoring" (2nd edition, with JavaScript examples) by Martin Fowler
- "The Pragmatic Programmer" by David Thomas and Andrew Hunt
- "A Philosophy of Software Design" by John Ousterhout
- "Working Effectively with Legacy Code" by Michael Feathers
- "Clean Architecture" by Robert C. Martin

It's worth reading more than one, because they disagree on some points (Ousterhout, for example, argues against very small functions).

# Moderate Questions (151-300)

## 151: How do you do the Extract Function refactoring?

1. Find a block of code that does one thing (a comment above it is often a hint).
2. Create a new function with a name that says what the block does.
3. Move the code into it. Variables the block reads become parameters; a variable it changes and the rest of the code uses becomes the return value.
4. Replace the original block with a call. Run the tests.

```ts
// Before
function printOwing(invoice: Invoice) {
  let outstanding = 0;
  for (const o of invoice.orders) outstanding += o.amount;
  console.log(`Name: ${invoice.customer}`);
  console.log(`Amount: ${outstanding}`);
}

// After
function printOwing(invoice: Invoice) {
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}
```

Most editors (VS Code, WebStorm) can do this automatically, which is safer than doing it by hand.

## 152: When would you inline a function instead of extracting one?

When the function's body is as clear as its name, or the function only passes a call through, the extra hop just adds reading time.

```ts
function isAdult(age: number) {
  return moreThanEighteen(age);
}
function moreThanEighteen(age: number) {
  return age >= 18;
}
```

Inline `moreThanEighteen`. Inlining is also a good first step when a group of functions is split badly: put them back together, then extract them again in a better way.

## 153: What is the Replace Temp with Query refactoring?

It replaces a temporary variable that holds a calculated value with a function that calculates it.

```ts
// Before
const basePrice = quantity * itemPrice;
if (basePrice > 1000) return basePrice * 0.95;
return basePrice * 0.98;

// After
get basePrice() {
  return this.quantity * this.itemPrice;
}
```

This makes the value available to other methods and often makes Extract Function easier, since there are fewer local variables to pass around. Only do it when the calculation is cheap and has no side effects.

## 154: How do you rename something safely in a large codebase?

- Use the editor's "Rename Symbol" (F2 in VS Code). With TypeScript, it updates every reference correctly, including imports.
- Search for the old name as text too, to catch strings, docs, config files, tests and dynamic access that the type checker can't see.
- For public APIs used by other teams or packages, keep the old name as a deprecated alias for a while, then remove it.
- Do the rename in its own commit so the review is easy.

## 155: What is the Introduce Parameter Object refactoring?

When several parameters always travel together, group them into one object.

```ts
// Before
function amountInvoiced(start: Date, end: Date) {}
function amountReceived(start: Date, end: Date) {}

// After
class DateRange {
  constructor(
    readonly start: Date,
    readonly end: Date,
  ) {}

  contains(date: Date) {
    return date >= this.start && date <= this.end;
  }
}

function amountInvoiced(range: DateRange) {}
function amountReceived(range: DateRange) {}
```

The bonus is that the new object becomes a natural home for related behavior, like `contains`.

## 156: How does Replace Conditional with Polymorphism work?

When you switch on a type to choose behavior, move each branch into a class (or object) for that type.

```ts
// Before
function speed(bird: Bird) {
  switch (bird.type) {
    case "european":
      return 35;
    case "african":
      return 40 - 2 * bird.coconuts;
    case "norwegian":
      return bird.isNailed ? 0 : 10 + bird.voltage / 10;
  }
}

// After
interface Bird {
  speed(): number;
}

class EuropeanSwallow implements Bird {
  speed() {
    return 35;
  }
}

class AfricanSwallow implements Bird {
  constructor(private coconuts: number) {}
  speed() {
    return 40 - 2 * this.coconuts;
  }
}
```

It's worth it when the same switch appears in several places. For one small switch, keep the switch.

## 157: What is the Decompose Conditional refactoring?

Pull the condition and each branch of a complex `if` into well-named functions.

```ts
// Before
if (date >= plan.summerStart && date <= plan.summerEnd) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}

// After
charge = isSummer(date, plan)
  ? summerCharge(quantity, plan)
  : regularCharge(quantity, plan);
```

The code now says what is being decided, not just how.

## 158: What is the Consolidate Conditional Expression refactoring?

When several checks lead to the same result, combine them into one condition and give it a name.

```ts
// Before
function disabilityAmount(employee: Employee) {
  if (employee.seniority < 2) return 0;
  if (employee.monthsDisabled > 12) return 0;
  if (employee.isPartTime) return 0;
  // ...
}

// After
function disabilityAmount(employee: Employee) {
  if (isNotEligibleForDisability(employee)) return 0;
  // ...
}
```

Only do this when the checks really are one rule. If they're separate rules that happen to share a result, keeping them apart may be clearer.

## 159: What is the Split Phase refactoring?

Split Phase breaks code that does two different kinds of work in sequence into two separate steps, with a data structure passed between them.

A typical example is "parse, then process":

```ts
// After
function priceOrder(input: string) {
  const order = parseOrder(input); // phase 1: turn raw input into data
  return calculatePrice(order); // phase 2: business logic on clean data
}
```

The business logic no longer cares about the input format, and each phase can be tested on its own.

## 160: When should you move a function to another module or class?

Move a function when it uses more data or functions from another module than from its own (feature envy), or when it changes together with code in another module.

Good modules keep things that change together in the same place. If you keep editing two files together for every change, some code is probably in the wrong one.

## 161: What is the Extract Class refactoring?

When a class does two jobs, move the fields and methods for one job into a new class.

```ts
// Before: Person handles both identity and phone formatting
class Person {
  name = "";
  officeAreaCode = "";
  officeNumber = "";
  telephoneNumber() {
    return `(${this.officeAreaCode}) ${this.officeNumber}`;
  }
}

// After
class TelephoneNumber {
  constructor(
    private areaCode: string,
    private number: string,
  ) {}
  toString() {
    return `(${this.areaCode}) ${this.number}`;
  }
}

class Person {
  name = "";
  constructor(public officePhone: TelephoneNumber) {}
}
```

A hint that you need this: a subset of fields is always used together, or some fields share a prefix.

## 162: What is a value object?

A value object is a small object defined by its values, not by an identity. Two `Money` objects with the same amount and currency are equal, just like two numbers `5` are equal. Value objects are usually immutable.

```ts
class Money {
  private constructor(
    readonly cents: number,
    readonly currency: string,
  ) {}

  static of(amount: number, currency: string) {
    if (!Number.isFinite(amount)) throw new Error("Invalid amount");
    return new Money(Math.round(amount * 100), currency);
  }

  add(other: Money) {
    if (other.currency !== this.currency) throw new Error("Currency mismatch");
    return new Money(this.cents + other.cents, this.currency);
  }

  equals(other: Money) {
    return this.cents === other.cents && this.currency === other.currency;
  }
}
```

They're the usual fix for primitive obsession: the validation lives in one place, and you can't add euros to dollars by mistake.

## 163: What does it mean to encapsulate a collection?

Don't hand out direct access to a class's internal array, because callers can change it without the class knowing.

```ts
class Course {
  #students: Student[] = [];

  get students(): readonly Student[] {
    return this.#students;
  }

  enroll(student: Student) {
    if (this.#students.length >= 30) throw new Error("Course is full");
    this.#students.push(student);
  }
}
```

The `readonly` type stops TypeScript users from calling `push` on the returned array. If you need protection at runtime too, return a copy.

## 164: How do you remove a flag argument?

Replace the one function with a flag by separate functions for each case. The shared part goes into a private helper.

```ts
// Before
function bookConcert(customer: Customer, isPremium: boolean) { ... }
bookConcert(customer, true);

// After
function bookPremiumConcert(customer: Customer) { ... }
function bookRegularConcert(customer: Customer) { ... }
```

If the flag comes from data at runtime (like a form value), keeping it as a parameter can be fine. The smell is mainly about literal `true`/`false` at call sites.

## 165: What is the Replace Loop with Pipeline refactoring?

It turns a loop that filters, transforms and collects into a chain of array methods.

```ts
// Before
const names: string[] = [];
for (const person of people) {
  if (person.job === "programmer") {
    names.push(person.name);
  }
}

// After
const names = people
  .filter((person) => person.job === "programmer")
  .map((person) => person.name);
```

Each step in the pipeline does one thing and can be read on its own.

## 166: What is the Split Variable refactoring?

When one variable is reused for two different things, give each use its own variable.

```ts
// Before
let temp = 2 * (height + width);
console.log(temp);
temp = height * width;
console.log(temp);

// After
const perimeter = 2 * (height + width);
console.log(perimeter);
const area = height * width;
console.log(area);
```

Each variable now has one meaning and can be `const`.

## 167: How do you refactor safely, step by step?

1. Make sure there are tests covering the behavior. If not, write some first.
2. Make one small change, like a single rename or extract.
3. Run the tests.
4. Commit.
5. Repeat.

If a test fails, you know it was the last tiny change, so you can fix or undo it quickly. Long refactors without running tests are how bugs sneak in.

## 168: Why should refactoring and behavior changes be in separate commits?

A refactor commit should change no behavior, so a reviewer can check it quickly: does it do the same thing, just structured differently? A feature commit should change behavior, and the reviewer focuses on whether the new behavior is right.

Mixing them makes both harder to review, and if something breaks, you can't easily revert one without the other.

## 169: How do you apply SRP to a React component?

A common SRP problem in React is a component that fetches data, transforms it, handles form state and renders a large UI.

Split it:

- A custom hook or data library (like TanStack Query) for fetching.
- Plain functions for transforming data, which are easy to unit test.
- Small presentational components that just take props and render.
- A container or page component that wires them together.

```tsx
function OrdersPage() {
  const { data: orders, isPending } = useOrders();
  if (isPending) return <Spinner />;
  return <OrdersTable rows={toOrderRows(orders)} />;
}
```

## 170: What is a "fat controller" and how do you fix it?

A fat controller is an HTTP route handler that holds all the logic: validation, business rules, database queries and response formatting.

```ts
// Fat controller
app.post("/orders", async (req, res) => {
  // 80 lines of validation, pricing, SQL, emails...
});

// Thin controller
app.post("/orders", async (req, res) => {
  const input = createOrderSchema.parse(req.body);
  const order = await orderService.create(input);
  res.status(201).json(toOrderResponse(order));
});
```

The controller only translates HTTP to a function call and back. Business logic lives in a service that can be tested without HTTP.

## 171: What is the difference between SRP and "a function should do one thing"?

They're often mixed up. "Do one thing" is about functions: each function should do one task at one level of detail.

SRP is about modules and classes, and it's about reasons to change. Robert Martin later clarified that SRP means a module should answer to one actor (one group of stakeholders). A class can have many methods and still follow SRP, as long as they all change for the same reason.

## 172: Can you explain the "actor" idea in SRP with an example?

Robert Martin uses an `Employee` class with three methods:

- `calculatePay()`, used by accounting (the CFO's team).
- `reportHours()`, used by HR (the COO's team).
- `save()`, used by database admins (the CTO's team).

If `calculatePay` and `reportHours` share a helper for regular hours, a change requested by accounting can silently break HR's report. Three different actors depend on one class. The fix is to split it so each actor's code lives in its own class, often with a small facade that ties them together.

## 173: Can SRP be taken too far?

Yes. If every class has a single method and every concept is split into five files, readers have to jump through many tiny pieces to follow one simple flow. That's also hard to understand.

John Ousterhout calls this "classitis". The goal is code that's easy to change, not the smallest possible units. Keep things together when they really change together.

## 174: How does Express middleware show the Open/Closed Principle?

Express is closed for modification (you don't edit Express to add features) but open for extension through middleware.

```ts
app.use(helmet());
app.use(express.json());
app.use(requestLogger);
app.use(authenticate);
```

Each middleware adds behavior to the request pipeline without changing the framework or the other middleware. Plugin systems in Vite, ESLint, Fastify and Babel work the same way.

## 175: How can a lookup table help with the Open/Closed Principle?

A map from keys to handlers lets you add new cases without touching the dispatch logic.

```ts
const exporters: Record<string, (data: Report) => string> = {
  csv: toCsv,
  json: toJson,
  xml: toXml,
};

function exportReport(format: string, data: Report) {
  const exporter = exporters[format];
  if (!exporter) throw new Error(`Unsupported format: ${format}`);
  return exporter(data);
}
```

Adding PDF means adding one entry. `exportReport` never changes. You can go further and let other modules register exporters, so even the map doesn't have to be edited.

## 176: How does composition in React relate to the Open/Closed Principle?

A component that accepts `children` or slot props can be extended with new content without changing its code.

```tsx
function Card({ title, actions, children }: CardProps) {
  return (
    <section className="card">
      <header>
        <h2>{title}</h2>
        {actions}
      </header>
      {children}
    </section>
  );
}
```

The alternative, adding a new boolean prop for every new variant (`showButton`, `isCompact`, `hasFooter`), means editing the component every time and quickly turns it into a mess of conditions.

## 177: When is it fine to just modify code instead of following OCP?

Most of the time, honestly. OCP is useful at points where you expect new variants, like payment methods, export formats or notification channels. Applying it everywhere means interfaces and plugin systems for code that will never be extended.

If you own the code, it's well tested and there's only one or two variants, editing the function is simpler. Add the extension point when the second or third variant actually shows up.

## 178: Why is throwing "not implemented" in a subclass an LSP problem?

If a base class or interface promises a method, callers expect to be able to call it. A subclass that throws "not implemented" breaks that promise.

```ts
class ReadOnlyFileStore extends FileStore {
  write() {
    throw new Error("Not supported");
  }
}
```

Any code written for `FileStore` that calls `write` now crashes when it gets this subclass. The fix is usually ISP: split reading and writing into separate interfaces, and only implement the ones you support.

## 179: What are preconditions and postconditions in LSP?

A precondition is what must be true before a method runs (for example, "amount must be positive"). A postcondition is what the method guarantees afterward (for example, "the returned list is sorted").

For a subtype to follow LSP:

- It can't require more (stricter preconditions). If the parent accepts any positive number, the child can't demand numbers over 100.
- It can't promise less (weaker postconditions). If the parent returns a sorted list, the child must too.

The child can accept more and promise more, but not the other way round.

## 180: Does TypeScript's type checker guarantee LSP?

No. TypeScript checks that the shapes match: same method names, compatible parameter and return types. It can't check behavior.

A class can match an interface perfectly and still break LSP by throwing unexpected errors, ignoring input, returning data in a different order, or changing shared state in surprising ways. Contract tests (the same test suite run against every implementation) are a good way to catch these.

## 181: How do you apply ISP in TypeScript?

Make functions and components depend only on what they use. TypeScript makes this easy with small interfaces and utility types like `Pick`.

```ts
interface User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
  createdAt: Date;
}

// Only needs two fields
function greeting(user: Pick<User, "name">) {
  return `Hello, ${user.name}`;
}
```

Now `greeting` can be called with any object that has a `name`, it's easier to test, and it can't accidentally use `passwordHash`.

## 182: How does ISP apply to React component props?

Pass only the data a component needs, not a whole domain object.

```tsx
// Depends on the entire User type
function Avatar({ user }: { user: User }) {
  return <img src={user.avatarUrl} alt={user.name} />;
}

// Depends only on what it uses
function Avatar({ src, alt }: { src: string; alt: string }) {
  return <img src={src} alt={alt} />;
}
```

The second version is reusable for teams, products or anything with an image, and changes to `User` don't affect it. With React.memo, smaller props also mean fewer needless re-renders.

## 183: What is a role interface?

A role interface describes one role a class plays for a specific client, instead of everything the class can do. The opposite is a "header interface" that just copies all the public methods of a class.

```ts
interface OrderReader {
  findById(id: string): Promise<Order | undefined>;
}

interface OrderWriter {
  save(order: Order): Promise<void>;
}

class OrderRepository implements OrderReader, OrderWriter { ... }
```

A reporting service only needs `OrderReader`, so it can't save orders by mistake, and its tests only need to fake one method.

## 184: How would you apply DIP in a typical Node.js backend?

Have the business logic define the interfaces it needs, and have the infrastructure implement them.

```ts
// domain/ports.ts
export interface UserRepository {
  findByEmail(email: string): Promise<User | undefined>;
  save(user: User): Promise<void>;
}

// application/register-user.ts
export class RegisterUser {
  constructor(private users: UserRepository, private hasher: PasswordHasher) {}
  // ...
}

// infrastructure/prisma-user-repository.ts
export class PrismaUserRepository implements UserRepository { ... }
```

The business code imports nothing from Prisma, Express or any library. The dependency arrow points from infrastructure to the domain, not the other way.

## 185: How can you apply DIP in a React app?

Components and hooks shouldn't import concrete API clients directly if you want to swap or fake them. Some options:

- Pass functions as props (`onSave`, `loadData`).
- Provide services through React context and read them with a hook.
- Use a data library whose fetcher can be swapped in tests.

```tsx
const ApiContext = createContext<ApiClient | null>(null);

function useApi() {
  const api = useContext(ApiContext);
  if (!api) throw new Error("useApi must be used inside ApiProvider");
  return api;
}
```

In tests you wrap the component with a provider that passes a fake client. For network-level faking, many teams use Mock Service Worker (MSW) instead.

## 186: How does NestJS support dependency injection?

NestJS has a built-in DI container. You mark classes with `@Injectable()`, register them as providers in a module, and Nest passes them into constructors.

```ts
@Injectable()
export class OrdersService {
  constructor(private readonly repo: OrdersRepository) {}
}
```

To depend on an interface (TypeScript interfaces don't exist at runtime), you use a token:

```ts
export const PAYMENT_GATEWAY = Symbol("PAYMENT_GATEWAY");

@Module({
  providers: [{ provide: PAYMENT_GATEWAY, useClass: StripeGateway }],
})
export class PaymentsModule {}

@Injectable()
export class CheckoutService {
  constructor(@Inject(PAYMENT_GATEWAY) private gateway: PaymentGateway) {}
}
```

Angular's DI works in a similar way, with `inject()` and `InjectionToken`.

## 187: What is a composition root?

The composition root is the one place in the app, usually at startup, where all the objects are created and wired together.

```ts
// main.ts
const db = new Pool({ connectionString: process.env.DATABASE_URL });
const users = new PgUserRepository(db);
const mailer = new SesMailer();
const registerUser = new RegisterUser(users, mailer);

startServer({ registerUser });
```

Everything else just receives what it needs. This keeps the knowledge of "which concrete class is used" in one file, which makes swapping implementations and building test setups simple. A DI container is just an automated composition root.

## 188: What is the difference between a stub, a mock, a spy and a fake?

These are all test doubles (stand-ins for real dependencies):

- **Stub**: returns canned answers. "When `getUser` is called, return this user."
- **Mock**: is set up with expectations and verifies how it was called. "Expect `send` to be called once with this email."
- **Spy**: wraps or records calls so you can check them after the fact.
- **Fake**: a simple working implementation, like an in-memory repository instead of a real database.

In Jest and Vitest, `vi.fn()`/`jest.fn()` can act as stubs, spies or mocks depending on how you use them.

## 189: Why are fakes often better than mocks?

Mocks tie the test to how the code calls its dependencies. If you refactor and call the repository differently but get the same result, mock-based tests break anyway.

A fake, like an in-memory repository, lets you test the outcome: "after registering, the user exists and has this email". Tests become less brittle and read more like real usage.

```ts
class InMemoryUserRepository implements UserRepository {
  private users = new Map<string, User>();
  async findByEmail(email: string) {
    return [...this.users.values()].find((u) => u.email === email);
  }
  async save(user: User) {
    this.users.set(user.id, user);
  }
}
```

## 190: What is over-mocking and why is it a problem?

Over-mocking is when a test replaces almost everything around the code under test with mocks. The test ends up checking that the code calls certain functions in a certain order, not that it produces the right result.

These tests break on every refactor even when behavior is unchanged, and they can pass while the real system is broken because the mocks don't behave like the real thing. Mock at the boundaries (network, time, payment provider), and use real objects or fakes for the rest.

## 191: What does "test behavior, not implementation" mean?

Tests should check what the code does from the outside (its inputs and outputs, or what the user sees), not how it does it internally.

```ts
// Tests implementation
expect(component.state.isOpen).toBe(true);

// Tests behavior
await user.click(screen.getByRole("button", { name: "Menu" }));
expect(screen.getByRole("menu")).toBeVisible();
```

Behavior tests survive refactoring. That's the whole point: tests should give you freedom to change the internals.

## 192: Should you test private methods?

Usually not directly. Private methods are implementation details; test them through the public methods that use them.

If a private method is so complex that you really want to test it on its own, that's often a sign it belongs in its own module or class with a public interface. Extract it and test that.

## 193: What is legacy code?

Michael Feathers, in "Working Effectively with Legacy Code", defines legacy code simply as code without tests. Age doesn't matter: code written last week with no tests is legacy code.

Without tests you can't change code safely, so every change is a gamble. His book is about how to get such code under test step by step.

## 194: What is a characterization test?

A characterization test captures what the code currently does, whatever that is, not what it should do. You use it before refactoring code you don't fully understand.

1. Call the code with some input.
2. Write an assertion you know is wrong.
3. Let the test fail and show the actual output.
4. Update the assertion to match the actual output.

Now you have a safety net. If a refactor changes the output, the test tells you. Snapshot tests can be used for this too.

## 195: What is a seam in legacy code?

A seam (from Michael Feathers) is a place where you can change what the code does without editing the code in that place. For example, a dependency passed in as a parameter is a seam: in tests you pass a fake.

When legacy code creates its own dependencies (`new Database()` inside a function), there's no seam, so you can't test it in isolation. Small, careful changes like moving `new Database()` into a constructor parameter create seams.

## 196: How do you add tests to code that's hard to test?

Common steps:

1. Find the change point: the code you need to change.
2. Find a test point: a place where you can observe the result.
3. Break dependencies with the smallest, safest edits: pass dependencies as parameters, extract a function out of a big method, wrap global calls (like `Date.now()` or `fetch`) behind small functions you can replace.
4. Write characterization tests.
5. Now make your change and refactor with tests running.

Use the editor's automated refactorings for the dependency-breaking steps, since you don't have tests yet to catch mistakes.

## 197: How do you deal with time and randomness to keep code testable?

Code that calls `Date.now()`, `new Date()` or `Math.random()` directly is hard to test, because the result changes every run.

Pass them in as dependencies:

```ts
function isExpired(token: Token, now: Date = new Date()) {
  return token.expiresAt < now;
}

test("token expires after expiry date", () => {
  expect(isExpired(token, new Date("2030-01-01"))).toBe(true);
});
```

Test tools also let you fake timers (`vi.useFakeTimers()`, `jest.useFakeTimers()`), which helps when you can't change the code.

## 198: What is the Null Object pattern?

Instead of returning `null` and making every caller check it, return an object with the same interface that does nothing or returns safe defaults.

```ts
interface Logger {
  log(message: string): void;
}

const noopLogger: Logger = {
  log() {},
};

class Service {
  constructor(private logger: Logger = noopLogger) {}

  run() {
    this.logger.log("running"); // no null check needed
  }
}
```

It works well for optional collaborators like loggers or analytics. Don't use it when a missing value is a real error that callers need to know about.

## 199: What is the Result type pattern?

A Result type makes errors part of the return value instead of throwing, so the type system forces callers to handle failure.

```ts
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

function parseAge(input: string): Result<number, string> {
  const age = Number(input);
  if (!Number.isInteger(age) || age < 0) {
    return { ok: false, error: `Invalid age: ${input}` };
  }
  return { ok: true, value: age };
}

const result = parseAge(form.age);
if (!result.ok) {
  showError(result.error);
} else {
  save(result.value);
}
```

It works well for expected failures like validation. Libraries like `neverthrow` provide a ready-made version. Unexpected failures (bugs, a crashed database) are usually still thrown.

## 200: How do you create custom error classes, and why?

Custom error classes let callers handle specific errors differently and carry useful context.

```ts
class NotFoundError extends Error {
  constructor(resource: string, id: string) {
    super(`${resource} ${id} not found`);
    this.name = "NotFoundError";
  }
}

try {
  await getOrder(id);
} catch (error) {
  if (error instanceof NotFoundError) return res.status(404).end();
  throw error;
}
```

You can also pass the original error with the `cause` option (`new Error("...", { cause: err })`) so you don't lose the original stack trace.

## 201: What is the difference between cyclomatic and cognitive complexity?

Cyclomatic complexity counts paths through the code, which tells you roughly how many tests you need. But it treats a flat `switch` with 10 cases the same as 10 nested `if`s, even though the nested version is much harder to read.

Cognitive complexity (created by SonarSource) tries to measure how hard code is for a human to understand. It adds more for nesting, breaks in linear flow (like `goto`, `break` to a label, recursion) and mixed boolean operators, and less for structures that are easy to read. It's used by SonarQube and `eslint-plugin-sonarjs`.

## 202: Should you organize folders by feature or by type?

By type means folders like `components/`, `hooks/`, `services/`, `utils/`. By feature means folders like `checkout/`, `profile/`, `search/`, each containing its own components, hooks and services.

For small apps, by type is fine. As the app grows, by feature usually works better: code that changes together lives together, you can see what the app does from the folder list, and deleting a feature means deleting a folder. Shared code goes in a separate `shared/` or `lib/` folder.

## 203: Why are circular dependencies a problem and how do you fix them?

A circular dependency is when module A imports B and B imports A (directly or through other modules). It causes real bugs in JavaScript: one module may see the other's exports as `undefined` during startup. It also means the two modules can't be understood or changed separately.

Fixes:

- Move the shared code into a third module both can import.
- Apply DIP: have one side depend on an interface and inject the implementation.
- Merge the modules if they're really one thing.

Tools like `madge` or `dependency-cruiser` can find cycles, and ESLint's `import/no-cycle` rule can block new ones.

## 204: What are the pros and cons of barrel files?

A barrel file is an `index.ts` that re-exports things from a folder, so others can write `import { Button } from "@/components"`.

Pros: shorter imports and a clear public API for a folder.

Cons: they can slow down tests and dev servers (importing one thing loads the whole barrel), they make circular imports more likely, and they can hurt tree shaking in some setups. Many teams use barrels only at package or feature boundaries, not in every folder.

## 205: What is an anemic domain model?

An anemic domain model has classes that only hold data (fields with getters and setters) while all the logic lives in separate service classes.

```ts
// Anemic
class Order {
  items: Item[] = [];
  status = "draft";
}

class OrderService {
  submit(order: Order) {
    if (order.items.length === 0) throw new Error("Empty order");
    order.status = "submitted";
  }
}
```

Martin Fowler calls this an anti-pattern for complex domains, because rules get spread across services and any code can put an object in an invalid state. A richer model puts the rules on the object itself (`order.submit()`). For simple CRUD apps, plain data and services are often fine.

## 206: How do you break up a God class step by step?

1. Add characterization tests around its public behavior if it doesn't have tests.
2. List its fields and methods and group them by which fields each method uses. Groups that share fields usually form a hidden class.
3. Extract one group at a time into a new class, and have the old class delegate to it.
4. Update callers to use the new class directly, when it makes sense.
5. Repeat until the old class is small or gone.

Don't try to do it in one big pull request. Small steps keep the system working and the reviews manageable.

## 207: What is "functional core, imperative shell"?

It's a way to structure code (named by Gary Bernhardt) where all the decisions and logic live in pure functions (the core), and all the I/O like databases, HTTP and files lives in a thin outer layer (the shell).

```ts
// Core: pure, easy to test
function decideRefund(order: Order, today: Date): RefundDecision { ... }

// Shell: does I/O and calls the core
async function handleRefundRequest(orderId: string) {
  const order = await db.orders.find(orderId);
  const decision = decideRefund(order, new Date());
  await db.refunds.save(decision);
}
```

The core can be tested with plain values, no mocks needed. The shell is simple enough that a few integration tests cover it.

## 208: How should you handle configuration cleanly?

- Read environment variables in one place, not with `process.env.X` all over the code.
- Validate them at startup and fail fast with a clear message if something is missing.
- Turn them into a typed config object and pass that around (or inject it).

```ts
import { z } from "zod";

const Env = z.object({
  DATABASE_URL: z.string().url(),
  PORT: z.coerce.number().default(3000),
  NODE_ENV: z.enum(["development", "test", "production"]),
});

export const config = Env.parse(process.env);
```

Now the rest of the code gets `config.PORT` as a number and never has to check whether it's set.

## 209: How do feature flags affect code cleanliness?

Feature flags are useful, but each flag adds a branch, and old flags that are always on are dead code in disguise.

To keep them clean:

- Check the flag in as few places as possible, ideally once at a high level.
- Give each flag an owner and an expected removal date.
- Remove the flag and the old code path soon after the rollout is done.
- Never reuse an old flag name for a new feature.

## 210: What does clean logging look like?

- Use a logger with levels (`debug`, `info`, `warn`, `error`) instead of `console.log` everywhere.
- Log structured data (JSON fields), not just long strings, so logs can be searched.
- Include context like request ID, user ID or order ID.
- Never log passwords, tokens, or full personal data.
- Log an error once, where it's handled, not at every layer it passes through.

```ts
logger.info({ orderId, userId, total }, "Order placed");
```

## 211: When should you use Promise.all instead of sequential awaits?

If the calls don't depend on each other, run them at the same time with `Promise.all`:

```ts
// Slow: waits for each one in turn
const user = await getUser(id);
const settings = await getSettings(id);

// Faster and just as clear
const [user, settings] = await Promise.all([getUser(id), getSettings(id)]);
```

Use `Promise.allSettled` when you want every result even if some fail. Keep sequential `await` when the second call needs the result of the first.

## 212: What is a floating promise and why is it a bug risk?

A floating promise is a promise that is created but never awaited or handled.

```ts
function save() {
  saveToServer(data); // no await, no .catch
}
```

If it rejects, the error is lost or crashes the process as an unhandled rejection, and the caller thinks the work is done when it isn't. The `@typescript-eslint/no-floating-promises` rule catches these. If you really want fire-and-forget, make it explicit with `void saveToServer(data).catch(logError)`.

## 213: Where should errors be caught in a layered application?

Catch an error where you can actually do something about it: retry, show a message, return a specific HTTP status, or use a fallback.

Lower layers (repositories, services) should usually let errors bubble up, maybe wrapped with more context. The top layer (the HTTP handler or a global error middleware) turns them into responses and logs them once.

```ts
app.use((err, req, res, next) => {
  if (err instanceof NotFoundError)
    return res.status(404).json({ error: err.message });
  logger.error({ err }, "Unhandled error");
  res.status(500).json({ error: "Internal error" });
});
```

Catching and re-throwing at every layer just adds noise.

## 214: Why should input be validated at the boundaries of the system?

Data from outside (HTTP requests, forms, files, third-party APIs, environment variables) can be anything. Validate it once, where it enters, and turn it into a typed, trusted object.

After that, the inner code can trust its inputs and doesn't need defensive checks everywhere. Libraries like Zod, Valibot or class-validator make this easy, and they give you the TypeScript type from the same schema.

## 215: What is the difference between defensive programming and trusting your inputs?

Defensive programming means checking for bad input and odd states everywhere, just in case. Too much of it fills code with checks that can never fail, which hides the real logic.

A cleaner approach: validate hard at the boundaries, then trust the types inside. Use assertions for things that should never happen ("this is a bug if it's false"), so they fail loudly instead of being silently handled.

## 216: How do you use assertions to protect invariants?

An invariant is something that must always be true, like "an order total is never negative". An assertion checks it and fails loudly if it isn't.

```ts
function assert(condition: unknown, message: string): asserts condition {
  if (!condition) throw new Error(`Assertion failed: ${message}`);
}

function applyDiscount(total: number, discount: number) {
  const result = total - discount;
  assert(result >= 0, "discount larger than total");
  return result;
}
```

The `asserts condition` return type also tells TypeScript to narrow types after the call. Node.js has a built-in `node:assert` module too.

## 217: What is the "wrong abstraction" and why can it be worse than duplication?

Sandi Metz said "duplication is far cheaper than the wrong abstraction". It happens like this: someone sees two similar pieces of code and merges them into one function. Later a new case comes along that's a bit different, so someone adds a parameter and an `if`. Then another. Soon the shared function is a mess of flags that nobody understands.

When you notice this, it's often best to inline the abstraction back into each caller, delete the unused branches in each copy, and then look for the right abstraction with fresh eyes.

## 218: What do the acronyms WET and AHA mean?

- **WET** ("Write Everything Twice") is a joke opposite of DRY. It's used to mean: it's OK to duplicate once before abstracting, similar to the rule of three.
- **AHA** ("Avoid Hasty Abstractions"), named by Kent C. Dodds, means prefer duplication over the wrong abstraction, and wait until you understand the common parts before extracting them.

Both push back against applying DRY too early.

## 219: Is DRY about code or about knowledge?

About knowledge. "The Pragmatic Programmer" defines DRY as "every piece of knowledge must have a single, unambiguous, authoritative representation within a system".

Two functions with the same lines of code but representing different business rules are not a DRY violation. For example, "max username length is 20" and "max product code length is 20" may look the same but will change for different reasons. Merging them couples two unrelated rules.

## 220: How do you balance DRY and coupling between services or packages?

Sharing code between services or packages creates coupling: a change to the shared library can force every service to update and redeploy together.

Inside one module, prefer DRY. Across service or team boundaries, some duplication is often cheaper than a shared library that everyone depends on. Shared code that is stable and generic (logging, HTTP helpers) is fine to share. Shared business logic usually isn't.

## 221: When should you write JSDoc or TSDoc comments?

Write them for public APIs: functions and classes that other teams, packages or library users will call without reading the code. Explain what the function does, what its parameters mean, what it returns, what it throws, and any important edge cases.

```ts
/**
 * Splits a list into chunks of the given size.
 * The last chunk may be smaller.
 * @throws RangeError if size is less than 1
 */
export function chunk<T>(items: T[], size: number): T[][] { ... }
```

With TypeScript, don't repeat types in the comments, since the signature already shows them. For private helpers, a good name usually is enough.

## 222: What is an Architecture Decision Record (ADR)?

An ADR is a short document that records an important technical decision: the context, the decision, the options considered and the consequences.

It answers "why is it built this way?" long after the people who made the decision have moved on. Code shows what was done; ADRs show why. They're usually kept as markdown files in the repo, for example in `docs/adr/`.

## 223: How should you structure tests with describe and it blocks?

Group tests by the unit or feature, then by the situation, and name each test as a sentence.

```ts
describe("Cart", () => {
  describe("when empty", () => {
    it("has a total of zero", () => { ... });
    it("cannot be checked out", () => { ... });
  });

  describe("with a coupon", () => {
    it("applies the discount to the subtotal", () => { ... });
  });
});
```

The test report then reads like a list of the cart's rules.

## 224: What are test data builders or factories?

They're helpers that create test objects with sensible defaults, so each test only sets the fields it cares about.

```ts
function buildUser(overrides: Partial<User> = {}): User {
  return {
    id: "user-1",
    name: "Test User",
    email: "test@example.com",
    isAdmin: false,
    ...overrides,
  };
}

test("admins can delete posts", () => {
  const admin = buildUser({ isAdmin: true });
  expect(canDeletePost(admin)).toBe(true);
});
```

The reader immediately sees that `isAdmin` is what matters in this test. When the `User` type gets a new required field, you update one builder instead of fifty tests.

## 225: Why should tests avoid logic like loops and conditionals?

Logic in tests can have bugs of its own, and nobody tests the tests. A test with `if`s and loops is also harder to read: you have to run it in your head to know what it checks.

Keep tests straight-line: set up, act, assert, with literal expected values. If you want to run the same check with many inputs, use `test.each`, which keeps each case visible.

```ts
test.each([
  ["", false],
  ["a@b.co", true],
  ["no-at-sign", false],
])("isValidEmail(%s) returns %s", (input, expected) => {
  expect(isValidEmail(input)).toBe(expected);
});
```

## 226: What makes tests flaky and how do you avoid it?

Flaky tests sometimes pass and sometimes fail without any code change. Common causes:

- Depending on real time, timezones or timers.
- Shared state between tests (globals, database rows left over).
- Depending on test order.
- Real network calls.
- In UI tests, not waiting for the right thing (fixed `sleep`s instead of waiting for an element).

Fix the root cause instead of adding retries. Flaky tests teach the team to ignore failures, which defeats the purpose of having tests.

## 227: What does code coverage tell you, and what doesn't it tell you?

Coverage tells you which lines or branches ran during tests. Low coverage is useful information: those parts are not tested at all.

High coverage doesn't mean the code is well tested. A test can run every line without checking the results. Chasing 100% often leads to useless tests of trivial code. Use coverage to find gaps, not as a target to hit. Mutation testing is a better way to check test quality.

## 228: What are the pros and cons of snapshot tests?

Snapshot tests save the output (like rendered HTML or a JSON object) and fail when it changes.

Pros: very quick to write, good for catching unexpected changes in large outputs, and useful as characterization tests.

Cons: they don't say what is correct, only what changed. Large snapshots get approved without reading ("just press `u`"), and they break on every harmless change. Keep snapshots small and focused, or use inline snapshots so the expected value is visible in the test.

## 229: What is the testing pyramid, and what is the testing trophy?

The testing pyramid (Mike Cohn) says: many fast unit tests at the bottom, fewer integration tests in the middle, and a few slow end-to-end tests at the top.

The testing trophy (Kent C. Dodds) is a version for front-end apps that puts the most weight on integration tests, with static analysis (TypeScript, ESLint) at the base. The idea is that integration tests give the most confidence for the effort.

Both agree on the main point: don't rely only on slow end-to-end tests, and don't only test tiny units in isolation.

## 230: What is the Repository pattern?

A repository hides how data is stored behind an interface that looks like a collection of domain objects.

```ts
interface OrderRepository {
  findById(id: string): Promise<Order | undefined>;
  findByCustomer(customerId: string): Promise<Order[]>;
  save(order: Order): Promise<void>;
}
```

Business code calls `orders.findById(id)` and doesn't know whether it's Postgres, MongoDB or an in-memory map. It keeps SQL or ORM calls in one place and makes the business logic easy to test with a fake repository.

## 231: What is a service layer?

A service layer holds the application's use cases, like "place order" or "cancel subscription". It sits between the entry points (HTTP controllers, CLI, queue consumers) and the domain and data layers.

It coordinates the work: loads data through repositories, calls domain logic, saves results, and triggers side effects like sending emails. This keeps controllers thin and lets the same use case be called from HTTP, a job or a test.

## 232: What are DTOs and why map between them and domain objects?

A DTO (Data Transfer Object) is a plain object shaped for sending data across a boundary, like an API response or request body.

Keeping DTOs separate from domain objects means:

- You can change the database or domain model without breaking the API contract.
- You don't leak internal fields (like `passwordHash`) by accident.
- Each side can have the shape that suits it.

```ts
function toUserResponse(user: User): UserResponse {
  return { id: user.id, name: user.name, email: user.email };
}
```

For small CRUD apps the mapping can feel like extra work, so use judgment.

## 233: What is the difference between Template Method and Strategy?

Both let you vary parts of an algorithm.

- **Template Method** uses inheritance: a base class defines the steps, and subclasses override some steps.
- **Strategy** uses composition: the varying part is an object or function passed in.

```ts
// Strategy
class ReportGenerator {
  constructor(private formatter: (rows: Row[]) => string) {}
  generate(rows: Row[]) {
    return this.formatter(rows);
  }
}
```

Strategy is usually preferred today, because it's easier to combine, test and change at runtime, and it avoids deep inheritance.

## 234: How does the Decorator pattern help follow the Open/Closed Principle?

A decorator wraps an object with the same interface and adds behavior before or after calling it. You add features like caching, logging or retries without changing the original class.

```ts
class CachedProductRepository implements ProductRepository {
  private cache = new Map<string, Product>();

  constructor(private inner: ProductRepository) {}

  async findById(id: string) {
    const hit = this.cache.get(id);
    if (hit) return hit;
    const product = await this.inner.findById(id);
    if (product) this.cache.set(id, product);
    return product;
  }
}

const repo = new CachedProductRepository(new SqlProductRepository(db));
```

Each decorator does one thing (SRP), and you can stack them in any order.

## 235: Why should you wrap third-party libraries?

Wrapping a third-party library in your own small interface (the Adapter pattern) means:

- The rest of your code depends on your interface, not on the library's API.
- If the library changes or you replace it, you update one file.
- You expose only what you use, with names that fit your domain.
- Tests can fake your small interface instead of mocking a big library.

```ts
export interface Analytics {
  track(event: string, props?: Record<string, unknown>): void;
}

export class SegmentAnalytics implements Analytics {
  track(event: string, props?: Record<string, unknown>) {
    segment.track({ event, properties: props });
  }
}
```

Don't wrap everything, though. Wrapping React or your main framework usually costs more than it saves.

## 236: When is a factory function useful?

A factory function hides how an object is created, which is useful when creation needs logic: picking an implementation, setting defaults, or validating.

```ts
function createStorage(env: string): Storage {
  if (env === "test") return new InMemoryStorage();
  if (env === "production") return new S3Storage(config.bucket);
  return new LocalDiskStorage("./uploads");
}
```

The callers just get a `Storage` and don't care which one. The "which implementation" decision lives in one place.

## 237: How do events help decouple code?

With events, one module announces that something happened, and other modules react, without the first module knowing who listens.

```ts
// Order module
events.emit("order.placed", { orderId, customerId });

// Separate modules
events.on("order.placed", sendConfirmationEmail);
events.on("order.placed", updateInventory);
```

Adding a new reaction doesn't require touching the order code, which follows OCP. The trade-off is that the flow is harder to follow, because you can't see all the effects of placing an order in one place. Use events for side effects, not for the main logic.

## 238: What is the dependency rule in a layered architecture?

Dependencies should point in one direction only: from outer layers (UI, controllers, database code) toward inner layers (business logic). Inner layers never import outer ones.

So your domain code shouldn't import Express, React, Prisma or the AWS SDK. When the domain needs something from the outside (like saving data), it defines an interface, and the outer layer implements it. This is DIP applied at the architecture level.

## 239: How can you enforce import rules in a codebase?

- ESLint's built-in `no-restricted-imports` rule can block certain imports, like importing the database client from UI code.
- `eslint-plugin-boundaries` or `eslint-plugin-import`'s `no-restricted-paths` let you define layers and which can import which.
- `dependency-cruiser` checks dependency rules in CI and can draw dependency graphs.
- In Nx monorepos, the `@nx/enforce-module-boundaries` rule uses project tags.

Rules that run automatically survive much better than rules written only in a wiki.

## 240: How do you give code review feedback about clean code without being rude?

- Comment on the code, not the person: "this function is hard to follow" instead of "you wrote confusing code".
- Explain why, so it's a lesson and not just an order.
- Ask questions when you're not sure: "could this be a separate function?"
- Mark small things as optional ("nit:") so the author knows what's blocking.
- Point out good things too.
- If it's a long discussion, talk in person or on a call.

## 241: What static analysis tools help measure code quality?

- **TypeScript** in `strict` mode catches type errors and null issues.
- **ESLint** with `typescript-eslint` for bugs and code style rules.
- **SonarQube / SonarCloud** for code smells, duplication, complexity, and security issues, with trends over time.
- **Knip** for unused files, exports and dependencies.
- **dependency-cruiser** or **madge** for dependency rules and cycles.
- **CodeQL** and similar tools for security analysis.

Tools catch the mechanical issues, so humans can focus on design in reviews.

## 242: How does pair programming help code quality?

With pairing, two developers work on the same code at the same time. One types and the other reviews, thinks ahead and spots problems. It's like a continuous code review.

It catches unclear names and design problems early, spreads knowledge, and keeps both people from cutting corners. Mob (or ensemble) programming does the same with the whole team. The trade-off is that it uses two people's time, so teams usually use it for tricky or important work.

## 243: How would you refactor a long function with many responsibilities? Walk through an example.

```ts
async function handleSignup(req: Request) {
  const { email, password } = req.body;
  if (!email || !email.includes("@"))
    return { status: 400, error: "Bad email" };
  if (!password || password.length < 8)
    return { status: 400, error: "Weak password" };
  const existing = await db.query("SELECT id FROM users WHERE email = $1", [
    email,
  ]);
  if (existing.rows.length) return { status: 409, error: "Taken" };
  const hash = await bcrypt.hash(password, 12);
  const id = crypto.randomUUID();
  await db.query(
    "INSERT INTO users (id, email, password_hash) VALUES ($1, $2, $3)",
    [id, email, hash],
  );
  await mailer.send(email, "Welcome!", "Thanks for signing up");
  return { status: 201, body: { id } };
}
```

Steps:

1. Write a few tests for the current behavior (valid signup, bad email, weak password, taken email).
2. Extract validation into a schema or `validateSignup` function.
3. Extract the SQL into a `UserRepository` with `existsByEmail` and `create`.
4. Extract password hashing behind a `PasswordHasher`.
5. Move the main flow into a `registerUser` use case that takes those as dependencies.
6. Leave `handleSignup` to parse the request, call `registerUser`, and map the result or errors to HTTP responses.

Run the tests after each step.

## 244: How do you replace boolean parameters with an options object?

When a function has several optional booleans or settings, use one options object with defaults:

```ts
interface FetchOptions {
  retries?: number;
  timeoutMs?: number;
  useCache?: boolean;
}

async function fetchJson(
  url: string,
  { retries = 3, timeoutMs = 5000, useCache = true }: FetchOptions = {},
) {
  // ...
}

fetchJson("/api/users", { useCache: false });
```

Call sites are readable, the order doesn't matter, and adding a new option doesn't break existing callers.

## 245: How do you decide if a comment should be turned into code?

Ask whether the comment describes what the code does or why it does it.

- "What" comments can usually become a function name, a variable name or a constant.
- "Why" comments (business reasons, workarounds for bugs in other systems, performance reasons) should stay as comments.

```ts
// Before
// convert cents to dollars and add tax
const x = (c / 100) * 1.08;

// After
const priceInDollars = centsToDollars(priceInCents);
const priceWithTax = addSalesTax(priceInDollars);
```

## 246: What is the "boolean trap" in APIs?

The boolean trap is when a function or component takes booleans whose meaning isn't clear at the call site, or when two related booleans can be set to an impossible combination.

```tsx
<Button primary secondary /> // which one wins?
```

Use a single prop with named values instead:

```tsx
type ButtonVariant = "primary" | "secondary" | "ghost";

<Button variant="primary" />;
```

## 247: How do you keep a module's public API small?

- Export only what other modules need. Keep helpers unexported.
- In packages, use the `exports` field in `package.json` to control which files can be imported.
- Use `#private` fields or `private` members in classes.
- In a feature folder, expose a single entry file and treat everything else as internal.

The smaller the public API, the more freedom you have to change the internals later without breaking anyone.

## 248: What is temporal coupling?

Temporal coupling is when methods must be called in a specific order to work, but nothing in the code enforces that order.

```ts
const client = new ApiClient();
client.setBaseUrl(url);
client.setToken(token);
client.init(); // forget this and every call fails
client.get("/users");
```

Fix it by making wrong orders impossible: pass everything the object needs in the constructor or a factory, so it's ready to use as soon as it exists.

```ts
const client = createApiClient({ baseUrl: url, token });
```

## 249: What is a hidden dependency?

A hidden dependency is something a function or class needs that isn't visible in its signature: a global variable, a singleton it reaches for, an imported module-level client, or an environment variable it reads directly.

```ts
function getPrice(id: string) {
  return globalCache.get(id) ?? db.prices.find(id); // two hidden dependencies
}
```

Readers can't see what the code depends on, and tests have to set up globals or mock modules. Making dependencies explicit as parameters fixes both problems.

## 250: Why are singletons often considered a code smell?

A singleton is a class that allows only one instance and gives global access to it (`Database.getInstance()`). It's basically a global variable with a nicer name.

Problems: hidden dependencies, shared state between tests, and code tied to one concrete class. It's fine to have only one instance of something (one database pool per app), but create it once in the composition root and pass it in, instead of making the class enforce it and having everyone reach for it globally.

## 251: How do discriminated unions make state handling cleaner?

Instead of several booleans that can conflict (`isLoading`, `isError`, `data`), use one union type with a `status` field.

```ts
// Booleans: can be isLoading and isError at the same time
interface State {
  isLoading: boolean;
  isError: boolean;
  data?: User[];
  error?: string;
}

// Discriminated union: only valid states exist
type State =
  | { status: "loading" }
  | { status: "error"; error: string }
  | { status: "success"; data: User[] };
```

TypeScript narrows the type when you check `status`, so `data` is only available in the success case. Bugs from impossible combinations go away.

## 252: How do you make a switch statement exhaustive in TypeScript?

Use the `never` type in the default branch. If someone adds a new case to the union and forgets to handle it, the code won't compile.

```ts
type Shape =
  { kind: "circle"; radius: number } | { kind: "square"; side: number };

function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side ** 2;
    default: {
      const unhandled: never = shape;
      throw new Error(`Unhandled shape: ${JSON.stringify(unhandled)}`);
    }
  }
}
```

The `@typescript-eslint/switch-exhaustiveness-check` rule does a similar check.

## 253: How do readonly and as const help write cleaner TypeScript?

They tell readers and the compiler that something shouldn't change.

```ts
interface Config {
  readonly apiUrl: string;
  readonly retries: number;
}

function sum(values: readonly number[]) {
  // values.push(1); // error
  return values.reduce((a, b) => a + b, 0);
}

const ROLES = ["admin", "editor", "viewer"] as const;
type Role = (typeof ROLES)[number]; // "admin" | "editor" | "viewer"
```

Taking `readonly` arrays as parameters also documents that the function won't change its input. Note that these are compile-time only; they don't freeze anything at runtime.

## 254: When are generics a good idea and when do they hurt readability?

Generics are good when a function or type works the same way for many types and you want to keep the type information:

```ts
function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}
```

They hurt when they're used where a plain type would do, or when types get so complex (several nested conditional types) that nobody can read the error messages. A rule of thumb: if a type parameter appears only once in the signature, you probably don't need it.

## 255: Should you use function overloads or union parameter types?

Prefer union types when the function does the same thing for each type:

```ts
function format(value: string | number) { ... }
```

Use overloads only when the return type depends on the input type in a way a union can't express. Overloads are harder to read and maintain, and the implementation signature is easy to get wrong. If overloads lead to very different behavior per input, separate functions with clear names are usually better.

## 256: What is wrong with having many optional parameters?

A function like `create(name, email?, age?, isAdmin?, sendEmail?)` forces callers to pass `undefined` to skip parameters, and the meaning of each position is unclear:

```ts
create("Ann", undefined, undefined, true);
```

Use an options object for optional values. If different combinations of options really mean different operations, split it into separate functions.

## 257: How do you keep REST API naming clean and consistent?

- Use nouns for resources and plural names: `/users`, `/orders/{id}`.
- Let HTTP methods say the action: `GET /orders`, `POST /orders`, `DELETE /orders/{id}`.
- Use one casing style for paths and one for JSON fields, everywhere.
- Nest only when the relationship is real and shallow: `/users/{id}/orders`.
- Use standard status codes instead of always returning 200 with an error message.

An OpenAPI spec and a linter like Spectral can enforce the rules across teams.

## 258: How do clean code ideas apply to CSS?

- Name classes after what things are, not how they look (`.error-message`, not `.red-text`).
- Use design tokens or CSS custom properties instead of magic values: `var(--space-4)`, not `17px`.
- Keep specificity low and avoid `!important`.
- Scope styles to components (CSS Modules, a naming method like BEM, or utility classes) so changes don't leak.
- Delete unused styles.

## 259: How do clean code ideas apply to SQL?

- Use clear table and column names, with one naming style.
- Format queries with one clause per line so they're easy to scan.
- Use CTEs (`WITH ...`) to name intermediate steps instead of deeply nested subqueries.
- Avoid `SELECT *` in application code; list the columns you need.
- Keep queries in the data access layer, not mixed into business logic or UI code.
- Use parameters, never string concatenation (which also protects against SQL injection).

## 260: Why should a team have a written style guide?

A style guide records the decisions the team has made: naming rules, folder structure, how errors are handled, how tests are written. It stops the same debates from happening in every code review, and it helps new people learn the conventions quickly.

Keep it short, and enforce as much as possible with tools (Prettier, ESLint, TypeScript settings). The guide should cover what tools can't check.

## 261: How do you share formatting and editor settings across a team?

- Commit a Prettier config (`.prettierrc`) and an `.editorconfig` file to the repo.
- Commit ESLint config and TypeScript settings.
- Add recommended editor extensions and settings (for example `.vscode/extensions.json`).
- Run the formatter and linter in CI so nothing unformatted gets merged.

This way, everyone's code looks the same, no matter which editor or personal settings they use.

## 262: How do pre-commit hooks help keep code clean?

Pre-commit hooks run checks before each commit. A common JavaScript setup uses Husky (to manage Git hooks) and lint-staged (to run tools only on staged files).

```json
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md,css}": "prettier --write"
  }
}
```

Problems are caught before they reach review. Keep hooks fast, or people will skip them with `--no-verify`. Slower checks like the full test suite belong in CI.

## 263: What are quality gates in CI?

A quality gate is a set of checks that must pass before code can be merged: type checking, linting, tests, coverage thresholds, maybe SonarQube rules like "no new critical issues" or "no new duplicated code".

The main idea is that the main branch never gets worse. Focus gates on new code ("clean as you code") rather than requiring legacy code to be fixed all at once.

## 264: Why should you remove unused dependencies?

Unused packages slow down installs and builds, increase the security risk (more code that can have vulnerabilities) and confuse readers who wonder what they're for.

Tools like Knip or `depcheck` find unused dependencies. Also watch for multiple libraries that do the same thing (two date libraries, two HTTP clients) and pick one.

## 265: How do higher-order functions support SOLID?

A higher-order function takes or returns another function. This gives you OCP and DIP without classes.

```ts
function withRetry<T>(fn: () => Promise<T>, retries = 3): () => Promise<T> {
  return async () => {
    for (let attempt = 1; ; attempt++) {
      try {
        return await fn();
      } catch (error) {
        if (attempt >= retries) throw error;
      }
    }
  };
}

const fetchUsersWithRetry = withRetry(() => fetchUsers());
```

`fetchUsers` was extended without changing it, and the retry logic has a single responsibility.

## 266: How can closures be used for dependency injection?

You can inject dependencies into a factory function and return functions that use them through a closure.

```ts
function makeUserService(deps: { repo: UserRepository; mailer: Mailer }) {
  return {
    async register(email: string) {
      const user = await deps.repo.create(email);
      await deps.mailer.sendWelcome(user);
      return user;
    },
  };
}

const userService = makeUserService({ repo: pgRepo, mailer: sesMailer });
```

This is a common style in functional TypeScript codebases. It works the same as constructor injection, without `this` or classes.

## 267: When should you use classes and when plain functions in TypeScript?

Plain functions and modules are often enough: for stateless logic, utilities and transformations, they're simpler and easier to test.

Classes make sense when you have state plus behavior that protects it (like `BankAccount`), when you have several implementations of an interface, or when a framework expects them (Angular, NestJS). There's no need to wrap a pure function in a class just to look object-oriented.

## 268: Why can too many getters and setters be a problem?

A class with a getter and a setter for every field isn't really encapsulated. Anyone can read and change anything, just with extra steps. The rules about what values are valid end up spread across the callers.

Instead of `setStatus("cancelled")`, offer methods that express real actions and protect the rules, like `cancel()`, which checks that the order hasn't shipped yet.

## 269: What is the difference between readonly in TypeScript and Object.freeze?

- `readonly` is a compile-time check. TypeScript stops you from assigning, but at runtime the object can still be changed (for example, by plain JavaScript code or after a type cast).
- `Object.freeze` works at runtime: assigning to a frozen object throws in strict mode (and silently fails otherwise). It's shallow, so nested objects can still change.

For most TypeScript code, `readonly` is enough and costs nothing at runtime. Use `Object.freeze` for constants or objects that untrusted code might touch.

## 270: What are the types of cohesion, from worst to best?

The classic list (from Larry Constantine's structured design work):

1. **Coincidental**: things grouped for no reason (`misc.ts`).
2. **Logical**: grouped because they're the same kind of thing, like all validators.
3. **Temporal**: grouped because they run at the same time, like startup code.
4. **Procedural**: grouped because they run in a sequence.
5. **Communicational**: grouped because they work on the same data.
6. **Sequential**: the output of one part is the input of the next.
7. **Functional**: everything works together for one well-defined task.

Aim for functional cohesion. Coincidental and logical cohesion are signs that a module should be split.

## 271: What are the types of coupling, from worst to best?

The classic list:

1. **Content coupling**: one module changes or reads another's internals directly.
2. **Common coupling**: modules share global data.
3. **External coupling**: modules share an external format or protocol.
4. **Control coupling**: one module tells another how to behave by passing a flag.
5. **Stamp coupling**: a module receives a whole data structure but uses only part of it.
6. **Data coupling**: modules share only the simple data they need.

You can't remove coupling, but you can aim for the looser kinds at the bottom of the list.

## 272: What is control coupling and how do you avoid it?

Control coupling is when a caller passes a flag that controls what the other module does internally. The caller has to know about the inside of the callee.

```ts
process(order, "validate-only");
process(order, "full");
```

The fix is the same as for flag arguments: split into separate functions (`validateOrder`, `processOrder`), or use polymorphism so each variant is its own object.

## 273: What is stamp coupling and when does it matter?

Stamp coupling is passing a whole object to a function that uses only a few of its fields. The function now depends on the shape of the whole object, and it's not clear which fields it really needs.

```ts
function shippingLabel(order: Order) {
  return `${order.customerName}\n${order.address}`;
}
```

If the function only needs two fields, take those two (or a small type with `Pick`). This is ISP at the function level. Passing whole objects is fine when the function really uses most of them.

## 274: How do you avoid misusing useEffect in React?

A common mess is using `useEffect` to keep state in sync with other state or props:

```tsx
// Unnecessary effect and extra render
const [fullName, setFullName] = useState("");
useEffect(() => {
  setFullName(`${first} ${last}`);
}, [first, last]);

// Just calculate it
const fullName = `${first} ${last}`;
```

The React docs ("You Might Not Need an Effect") list more cases: handle user actions in event handlers, not effects; reset state with a `key`; and fetch data with a framework or a library. Effects are for syncing with things outside React, like subscriptions or DOM APIs.

## 275: What is derived state and why shouldn't you store it?

Derived state is data you can calculate from other data you already have, like a filtered list, a total or a full name.

Storing it separately means you have two sources of truth that can get out of sync. Calculate it when you need it instead. If the calculation is expensive, cache it (with `useMemo` in React, or a memoized selector) rather than storing a copy.

## 276: What is state colocation?

State colocation means keeping state as close as possible to where it's used. If only one component needs it, keep it in that component. Lift it up only when siblings need to share it.

Putting everything in a global store "just in case" makes components depend on global state, causes extra re-renders and makes the code harder to follow.

## 277: When should you use React context instead of passing props?

Passing props down a few levels is fine and very clear. It becomes a problem ("prop drilling") when many components in the middle just forward props they don't use.

Before reaching for context, try composition: pass components as `children` so the data skips the middle layers. Use context for data that many components at different levels really need, like the current user, theme or locale. Avoid putting fast-changing values in one big context, since every consumer re-renders when it changes.

## 278: What are compound components?

Compound components are a group of components that work together and share state implicitly, giving a flexible API instead of a long list of props.

```tsx
<Tabs defaultValue="profile">
  <Tabs.List>
    <Tabs.Trigger value="profile">Profile</Tabs.Trigger>
    <Tabs.Trigger value="billing">Billing</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="profile">
    <ProfileForm />
  </Tabs.Content>
  <Tabs.Content value="billing">
    <BillingForm />
  </Tabs.Content>
</Tabs>
```

Compare that with `<Tabs tabs={[...]} renderTab={...} tabClassName="..." />`. The compound version is open for extension (you can put anything inside) without adding new props. Libraries like Radix UI use this pattern.

## 279: Is the container/presentational pattern still useful in React?

The original idea was: container components handle data and logic, presentational components just render props. Dan Abramov, who made it popular, later said hooks made it less necessary to split components this way.

The idea behind it is still good: keep data fetching and business logic out of UI components. Today that's usually done with custom hooks, server components or data libraries instead of separate container components.

## 280: How do error boundaries help keep React code clean?

An error boundary catches errors thrown during rendering in its child tree and shows a fallback UI instead of crashing the whole app.

Instead of wrapping every component's render logic in `try`/`catch`, you put a few boundaries at sensible places (around a page, a widget or a route). The `react-error-boundary` package gives a ready-made component. Note that error boundaries don't catch errors in event handlers or async code; handle those where they happen.

## 281: How should you name event handlers and callback props in React?

A common convention:

- Props that receive callbacks start with `on`: `onClick`, `onSave`, `onUserSelect`.
- The functions that handle them inside a component start with `handle`: `handleClick`, `handleSave`.

```tsx
function UserList({ onUserSelect }: { onUserSelect: (id: string) => void }) {
  function handleRowClick(id: string) {
    onUserSelect(id);
  }
  // ...
}
```

Name callbacks after what happened (`onUserSelect`), not what the parent will do (`openUserModal`), so the component stays reusable.

## 282: How do you keep a global store (Redux, Zustand) clean as it grows?

- Split it into slices by feature or domain, each with its own state and actions.
- Keep in the store only state that's truly global. Server data is usually better handled by TanStack Query, RTK Query or similar.
- Don't store derived data; compute it with selectors.
- Name actions as events that happened (`orderPlaced`), not as setters (`setOrderStatus`).
- Keep components using selectors and hooks instead of reading the store shape directly, so the shape can change.

## 283: How should a front-end API client layer look?

Put all HTTP calls in one module or a set of feature modules, instead of calling `fetch` from components.

```ts
export const ordersApi = {
  list: () => http.get<Order[]>("/orders"),
  get: (id: string) => http.get<Order>(`/orders/${id}`),
  create: (input: CreateOrderInput) => http.post<Order>("/orders", input),
};
```

The shared `http` helper handles the base URL, auth headers, JSON parsing and error mapping once. Components and hooks call `ordersApi.list()` and don't care about URLs or headers. You can also generate this layer from an OpenAPI spec.

## 284: Why should business logic stay out of UI components?

UI components change often for visual reasons. Business rules (pricing, permissions, validation) change for business reasons. Mixing them means a design change can break a rule, and you can't test the rule without rendering a component.

Put rules in plain functions or modules, and have components call them:

```ts
export function canEditPost(user: User, post: Post) {
  return user.role === "admin" || post.authorId === user.id;
}
```

The same rule can then be reused on the server, where it must be checked anyway.

## 285: How do you handle errors in async Express route handlers cleanly?

In Express 4, a rejected promise in a route handler isn't passed to the error middleware, so people wrapped every handler with a helper or used `express-async-errors`.

Express 5 fixes this: if an async handler throws or returns a rejected promise, Express calls `next(err)` for you. So with Express 5 you can write plain async handlers and keep all error handling in one error middleware. Fastify and NestJS also handle async errors out of the box.

## 286: How do you handle cross-cutting concerns cleanly?

Cross-cutting concerns are things many parts of the app need: logging, authentication, caching, metrics, retries. Copying that code into every function breaks SRP and DRY.

Common ways to keep them in one place:

- HTTP middleware (Express, Fastify hooks).
- Decorators or wrapper functions around services.
- Interceptors and guards in NestJS or Angular.
- Higher-order functions like `withRetry` or `withLogging`.

The business code then only contains business logic.

## 287: How can TypeScript decorators help with cross-cutting concerns?

TypeScript 5.0 added support for standard ECMAScript decorators. A method decorator can wrap a method with extra behavior:

```ts
function logged<This, Args extends unknown[], R>(
  target: (this: This, ...args: Args) => R,
  context: ClassMethodDecoratorContext<This, (this: This, ...args: Args) => R>,
) {
  return function (this: This, ...args: Args): R {
    console.log(`Calling ${String(context.name)}`);
    return target.call(this, ...args);
  };
}

class OrderService {
  @logged
  placeOrder(id: string) {
    /* ... */
  }
}
```

Frameworks like NestJS and Angular still use the older "experimental" decorators, which have a different signature. Don't overuse decorators: hidden behavior can surprise readers.

## 288: How do you override dependencies in tests when using DI?

With constructor injection, just pass fakes:

```ts
const service = new RegisterUser(
  new InMemoryUserRepository(),
  new FakeMailer(),
);
```

With a DI container, use its testing tools. In NestJS:

```ts
const moduleRef = await Test.createTestingModule({
  imports: [AppModule],
})
  .overrideProvider(PAYMENT_GATEWAY)
  .useValue(new FakePaymentGateway())
  .compile();
```

Angular's `TestBed` has `providers` and `overrideProvider` for the same purpose. Being able to swap dependencies this easily is one of the main benefits of DIP.

## 289: What are contract tests for interface implementations?

When several classes implement the same interface, write one shared test suite that describes how any implementation must behave, and run it against each one.

```ts
function userRepositoryContract(create: () => Promise<UserRepository>) {
  test("returns a saved user by email", async () => {
    const repo = await create();
    await repo.save(buildUser({ email: "a@b.co" }));
    expect(await repo.findByEmail("a@b.co")).toBeDefined();
  });
}

describe("InMemoryUserRepository", () =>
  userRepositoryContract(async () => new InMemoryUserRepository()));
describe("PgUserRepository", () => userRepositoryContract(createTestPgRepo));
```

This is how you check LSP in practice: the fake you use in other tests is proven to behave like the real thing.

## 290: Should repositories be tested with unit tests or integration tests?

Mostly integration tests against a real database (often in a Docker container, for example with Testcontainers). A repository's job is to talk to the database correctly, and mocking the database driver tests almost nothing.

Unit tests are for the logic that uses the repository. Those tests use a fake repository, which is fast and simple.

## 291: What is mutation testing?

Mutation testing checks how good your tests are. A tool makes small changes ("mutants") to your code, like changing `>` to `>=` or `true` to `false`, and runs the tests. If the tests still pass, that mutant "survived", which means the tests don't really check that behavior.

For JavaScript and TypeScript, Stryker is the common tool. It's slow on big codebases, so it's often run only on important modules or on changed files.

## 292: How do you convince a manager to spend time on refactoring?

Talk about business results, not code beauty:

- Show how long similar changes took recently and how much a cleanup would cut that.
- Point to bugs that came from the messy area.
- Suggest small, regular refactoring as part of feature work, not a big separate project.
- Pick the areas that change most often; cleaning code that nobody touches has little value.

Refactoring tied to a feature that's on the roadmap is the easiest to get approved.

## 293: How should a team track technical debt?

- Write debt items in the issue tracker like other work, with a short description of the cost ("adding a payment method takes 3 days because...").
- Label them so they can be found and counted.
- Review them during planning and pick some each sprint, or keep a fixed share of time for them.
- Prefer paying off debt in code you're about to change anyway.

Debt that only lives in people's heads gets forgotten, and debt in a huge list nobody looks at isn't much better.

## 294: What questions do you ask to check SOLID in a code review?

- **SRP**: Does this class or module change for more than one reason? Does it mix business rules with I/O?
- **OCP**: Will adding the next variant mean editing this function again? Is that likely?
- **LSP**: Do subclasses or implementations behave the way callers expect? Any "not supported" errors?
- **ISP**: Do callers depend on big interfaces but use only a small part?
- **DIP**: Does business logic import database, HTTP or framework code directly?

And always: is this complexity justified by a real need right now?

## 295: What is the Strangler Fig pattern?

The Strangler Fig pattern (named by Martin Fowler) replaces an old system bit by bit instead of in one big rewrite. You put a routing layer in front, build new features or replacements in new code, and send more and more traffic to the new code. When nothing uses the old part anymore, you delete it.

It works for whole systems and for modules inside one app. It's much safer than a big-bang rewrite because the system keeps working and you get feedback from real use early.

## 296: How do you introduce SOLID into an existing codebase without a rewrite?

- Don't refactor everything. Start with code that changes often or causes bugs.
- When adding a feature to a messy area, first refactor just enough to make the change easy.
- Introduce interfaces at boundaries you need to fake in tests, like the database, external APIs and the clock.
- Extract business rules from controllers and components into plain modules as you touch them.
- Add lint rules for new code (import boundaries, complexity) so things don't get worse.

Over months, the parts that matter get cleaner without a risky big project.

## 297: What is the difference between a library and a framework, in terms of dependency direction?

With a library, your code calls it: you decide when and how. With a framework, it calls your code: you fill in pieces and it controls the flow. This is called Inversion of Control, or "don't call us, we'll call you".

For clean design, keep your business logic independent of the framework. Let the framework call thin adapters (controllers, components), and have those call your own code. Then a framework upgrade or change doesn't force a rewrite of the business rules.

## 298: What is Inversion of Control?

Inversion of Control (IoC) means some outside code controls the flow and calls your code, instead of your code controlling everything. Frameworks, event handlers, callbacks and DI containers are all examples.

Dependency injection is one specific kind of IoC: instead of a class creating its dependencies, something outside creates them and hands them in. IoC is the broad idea, DI is one technique, and DIP is the design rule about which direction dependencies should point.

## 299: How do you keep a long list of if-else checks for validation clean?

Use a schema library or a list of small rules instead of a long chain of `if`s:

```ts
const SignupSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  age: z.number().int().min(13),
});

const result = SignupSchema.safeParse(input);
if (!result.success) return { errors: result.error.flatten().fieldErrors };
```

Each rule is declared once, the error messages come back per field, and the TypeScript type is created from the same schema.

## 300: How do you make sure clean code rules don't slow the team down?

- Automate formatting and lint checks so nobody argues about them.
- Keep rules few and focused on real problems the team has had.
- Treat size and complexity limits as warnings, and allow exceptions with a short comment.
- Review design early (a short chat or draft PR) instead of after a big change is done.
- Revisit the rules now and then and drop the ones that don't help.

The goal of clean code is to ship faster over time. Rules that only add friction should go.

# Advanced Questions (301-450)

## 301: What are the main criticisms of the "Clean Code" book?

- **Too-small functions**: the book's examples split code into many 3-5 line functions. Critics like John Ousterhout say this creates "shallow" functions and forces the reader to jump around to follow simple logic.
- **Side effects in examples**: some examples move local variables into class fields so methods have fewer parameters, which adds hidden state.
- **Comments**: the book is very negative about comments. Ousterhout argues comments are needed to describe interfaces and design decisions.
- **Performance**: people like Casey Muratori showed that heavy use of polymorphism and small virtual calls can be much slower in performance-critical code.
- **Dated examples**: the examples are in older Java style.

Most of the core ideas (good names, small focused units, tests, no duplication of knowledge) are still widely accepted. A good answer shows you know both sides.

## 302: What are deep and shallow modules?

The terms come from John Ousterhout's "A Philosophy of Software Design". A module's cost is its interface (what users must learn), and its benefit is the functionality it hides.

- A **deep** module has a simple interface and hides a lot of work. Unix file I/O (`open`, `read`, `write`, `close`) is a classic example.
- A **shallow** module has an interface almost as complex as what it does, like a function that just renames another one.

Many tiny classes and methods can add up to a system of shallow modules, where the reader learns many interfaces but each hides very little. Aim for deep modules.

## 303: What is information hiding?

Information hiding, from David Parnas's 1972 paper, says each module should hide a design decision that is likely to change, like a data format, an algorithm or which external service is used. Other modules only see an interface that stays stable when the decision changes.

Parnas showed that splitting a system by "steps in the process" (read input, then process, then output) tends to spread decisions across modules, while splitting it by "decisions that might change" keeps each change local. This is the root of encapsulation, SRP and OCP.

## 304: What is information leakage?

Information leakage (Ousterhout's term) is when one design decision is reflected in several modules. If you change the decision, all of them must change.

A common example is two classes that both know a file format: one reads it and one writes it. Even without importing each other, they're tightly coupled. The fix is to put the knowledge in one place, like a single class that both reads and writes the format.

Another form is "temporal decomposition": splitting code by the order operations happen in, which often spreads the same knowledge across steps.

## 305: Is SOLID still relevant today?

Mostly yes, but how you apply it has changed. The ideas behind it (manage dependencies, keep things that change together in one place, depend on stable interfaces) apply to functions, modules, packages and services, not just classes.

What has changed: modern code is less class-heavy, TypeScript's structural typing makes interfaces lighter, and the industry is more aware of the cost of too many abstractions. SOLID works best as a set of questions to ask when design feels painful, not as rules to apply everywhere up front.

## 306: How does SOLID map to functional programming?

- **SRP**: small functions, each with one job, composed together.
- **OCP**: higher-order functions. Pass behavior in as a function instead of editing code.
- **LSP**: any function with the right type signature and the same behavior contract can be swapped in.
- **ISP**: functions take only the arguments they need, not large objects.
- **DIP**: functions receive their effects (like a `save` function) as arguments, or effects are pushed to the edges ("functional core, imperative shell").

Some functional programmers say SOLID is just "use functions and composition" stated in OOP terms. That's mostly fair.

## 307: How do SOLID principles apply at the architecture level?

- **SRP**: each service or bounded context owns one business capability and answers to one team.
- **OCP**: systems are extended with new services, event consumers or plugins rather than by editing core services.
- **LSP**: different implementations of an API (versions, providers) must honor the same contract.
- **ISP**: APIs are designed for specific consumers, sometimes with a "backend for frontend" per client type.
- **DIP**: services depend on contracts (API schemas, event schemas), not on each other's internals or databases.

## 308: Can applying SRP to microservices go wrong?

Yes. Splitting services too finely creates a "distributed monolith": services that can't be deployed alone because every feature needs changes in several of them, now with network calls, partial failures and distributed transactions on top.

The SRP idea of "one reason to change" should be applied to business capabilities, not technical layers. A "user service", "user validation service" and "user email service" that always change together are really one responsibility split in three.

## 309: How does Conway's law relate to SRP?

Conway's law says systems tend to mirror the communication structure of the organization that builds them. Robert Martin's "actor" version of SRP is closely related: code that serves different groups of people should be separate, because those groups will ask for different changes.

In practice, module and service boundaries work best when they line up with team boundaries. Teams sometimes reorganize on purpose to get the architecture they want, which is called the "inverse Conway maneuver".

## 310: What are the package cohesion principles REP, CCP and CRP?

From Robert Martin's work on component design:

- **REP (Reuse/Release Equivalence Principle)**: the unit of reuse is the unit of release. Things released together should be versioned and documented together.
- **CCP (Common Closure Principle)**: group classes that change for the same reasons at the same times. It's SRP for packages.
- **CRP (Common Reuse Principle)**: don't force users of a package to depend on things they don't use. It's ISP for packages.

## 311: Why is there tension between REP, CCP and CRP?

CCP and REP push toward bigger packages (group things that change and ship together). CRP pushes toward smaller ones (don't make people depend on extra stuff).

Focus on CCP and you get fewer releases but users pull in code they don't need. Focus on CRP and you get many tiny packages, and a single change may need releases of several of them. Early in a project, CCP usually matters more (easy development). As more teams reuse the code, the balance shifts toward CRP and REP.

## 312: What is the Acyclic Dependencies Principle?

The Acyclic Dependencies Principle (ADP) says the dependency graph between packages or modules must have no cycles.

With a cycle, the modules in it effectively become one big module: you can't build, test or release one without the others. Break cycles with DIP (introduce an interface owned by one side) or by extracting the shared part into a new module that both depend on.

## 313: What is the Stable Dependencies Principle?

The Stable Dependencies Principle (SDP) says depend in the direction of stability. A module that many others depend on is hard to change (it's "stable"). A module that changes often should not be depended on by stable modules, or every change will ripple outward.

For example, your core domain types should be stable, and UI code (which changes often) depends on them, not the other way around.

## 314: What is the Stable Abstractions Principle?

The Stable Abstractions Principle (SAP) says a module should be as abstract as it is stable. Stable modules (many dependents) should mostly contain interfaces and abstractions, so they can be extended without being changed. Unstable modules should contain concrete code, which is fine because nothing depends on them.

Together with SDP, it means dependencies should point toward abstractions. That's DIP at the package level.

## 315: How do you measure a module's instability?

Robert Martin defined:

- **Ca** (afferent coupling): how many modules depend on this one (incoming).
- **Ce** (efferent coupling): how many modules this one depends on (outgoing).
- **Instability I = Ce / (Ca + Ce)**, from 0 to 1.

I = 0 means maximally stable: many dependents, no dependencies of its own. I = 1 means maximally unstable: nothing depends on it, and it depends on others. SDP says a module's I should be higher than the I of the modules it depends on. Tools like `dependency-cruiser` can produce the numbers you need.

## 316: What are the "zone of pain" and the "zone of uselessness"?

Martin plots abstractness (A, the share of abstract types in a module) against instability (I). The ideal line from (A=1, I=0) to (A=0, I=1) is called the main sequence.

- **Zone of pain** (low A, low I): concrete and depended on by many. Hard to change. A database schema is a typical example. It's OK if the code rarely changes (like a standard library), painful if it changes often.
- **Zone of uselessness** (high A, high I): abstract, but nobody depends on it. Usually leftover interfaces with no users.

## 317: What is connascence?

Connascence (Meilir Page-Jones) is a more detailed way to describe coupling. Two pieces of code are connascent if changing one requires changing the other to keep the program correct.

Static forms, from weaker to stronger:

- **Name**: both use the same name.
- **Type**: both agree on a type.
- **Meaning**: both agree on what a value means (like `1` = admin).
- **Position**: both agree on the order of values (positional parameters).
- **Algorithm**: both use the same algorithm (like the same hash function).

Dynamic forms include execution order, timing, values that must change together and identity. The advice is to turn strong forms into weaker ones, like replacing connascence of meaning (magic number) with connascence of name (a named constant).

## 318: How do you use connascence's strength, locality and degree?

- **Strength**: how hard it is to discover and refactor. Name is weak; timing is strong.
- **Locality**: how close the connected pieces are. Strong connascence inside one function is fine; the same across services is dangerous.
- **Degree**: how many pieces are involved. Two places agreeing is OK; fifty is a problem.

Rule of thumb: the farther apart two pieces of code are, the weaker their connascence should be. This gives you a more exact language for code review than "this is too coupled".

## 319: What is the history constraint in the Liskov Substitution Principle?

Barbara Liskov and Jeannette Wing's 1994 definition includes, besides pre- and postconditions, the history constraint: a subtype must not allow state changes that the base type doesn't allow.

The classic example: if an `ImmutablePoint` type promises its coordinates never change, a `MutablePoint` subtype that adds `setX` breaks that promise. Code that relied on the point never changing (caching it, using it as a map key) breaks.

This is why you can make a mutable type a subtype of a read-only view, but not of an immutable type.

## 320: How do covariance and contravariance relate to LSP?

For a subtype to be safely usable in place of the base type:

- **Return types can be covariant**: the subtype may return a more specific type. If the base returns `Animal`, the subtype may return `Dog`.
- **Parameter types should be contravariant**: the subtype may accept a more general type. If the base accepts `Dog`, the subtype may accept `Animal`, but not something narrower.

This is LSP's "require no more, promise no less" rule expressed in types.

## 321: How does TypeScript handle parameter variance, and what is method bivariance?

With `strictFunctionTypes` on (part of `strict`), TypeScript checks function-type parameters contravariantly, which is correct.

But methods declared with method syntax in interfaces and classes are still checked bivariantly, for compatibility. That lets some unsafe substitutions through:

```ts
interface Animal {
  name: string;
}
interface Dog extends Animal {
  bark(): void;
}

interface Handler {
  handle(a: Animal): void; // method syntax: bivariant
}

const dogHandler: Handler = {
  handle(d: Dog) {
    d.bark();
  }, // allowed, but unsafe
};

dogHandler.handle({ name: "cat" }); // crashes at runtime
```

Declaring it as a property, `handle: (a: Animal) => void`, makes TypeScript reject this. The `@typescript-eslint/method-signature-style` rule can enforce the property style.

## 322: Why are arrays in TypeScript an LSP risk?

TypeScript treats mutable arrays as covariant: `Dog[]` is assignable to `Animal[]`. That's convenient but unsound:

```ts
const dogs: Dog[] = [];
const animals: Animal[] = dogs;
animals.push({ name: "cat" }); // allowed
dogs[0].bark(); // runtime error
```

A mutable `Dog[]` doesn't really behave like a mutable `Animal[]`, since an `Animal[]` should accept any animal. Using `readonly Animal[]` as the parameter type is safe, because a read-only array is truly covariant. This is another reason to prefer `readonly` arrays in function parameters.

## 323: What is Design by Contract?

Design by Contract, from Bertrand Meyer (and built into the Eiffel language), says each method has a contract:

- **Preconditions**: what the caller must make true before calling.
- **Postconditions**: what the method guarantees after it runs.
- **Invariants**: what is always true about the object between calls.

LSP is essentially the rule for how contracts can change in subtypes. TypeScript has no built-in contracts, so teams use types for what they can, assertions for the rest, and tests to check that implementations respect the contract.

## 324: How does LSP apply to exceptions?

A subtype shouldn't throw new kinds of exceptions that callers of the base type don't expect and can't handle. If `Storage.save` is documented to throw only `StorageError`, an implementation that throws a raw `AxiosError` or `PrismaClientKnownRequestError` leaks its internals and breaks callers' error handling.

Implementations should catch their library-specific errors and wrap them in the errors the interface promises, keeping the original as `cause`.

## 325: What is "protected variation"?

Protected Variation is Craig Larman's name for the idea behind OCP and information hiding: find the points where change or instability is expected, and put a stable interface around them.

It's a useful framing because it makes clear that you don't protect everything, only the points where you've seen or can reasonably expect change: payment providers, tax rules, external APIs, storage. Wrapping things that never change just adds layers.

## 326: How do you decide where to put extension points?

- Look at history: what has changed in the past? `git log` on a file shows which parts change often.
- Look at the business: which rules does the product team keep tweaking? Which integrations are likely to be swapped?
- Wait for the second or third case before adding the abstraction, unless the cost of changing later is very high (like a public API).
- Put extension points at the edges (I/O, integrations), where they also help testing.

Guessing wrong costs complexity forever, so be conservative.

## 327: How do you resolve the tension between OCP and YAGNI?

OCP says design so new behavior can be added without changing code. YAGNI says don't build things you don't need yet. Taken to extremes, they contradict each other.

The usual answer: write the simple version first (YAGNI). When a change shows you where variation really happens, refactor to make that spot open for extension (OCP), and then add the new case. Robert Martin himself describes this as "take the first bullet": let the first change tell you what kind of change to protect against.

## 328: What is the difference between a header interface and a role interface, and why does it matter for ISP?

A header interface mirrors all the public methods of one class, like `IUserService` with all 25 methods of `UserService`. It doesn't help ISP: every client still depends on everything, and the interface changes every time the class does.

Role interfaces are defined from the client's point of view: what does this specific caller need? A class can implement several of them. This is what ISP actually asks for. In TypeScript, thanks to structural typing, a client can even declare the small interface it needs right next to itself, and any object with matching methods will fit.

## 329: Under DIP, who should own the interface?

The high-level module (the consumer) should own it. That's the "inversion": the low-level module depends on an interface defined by the high-level one, instead of the high-level module depending on whatever the low-level one offers.

In practice, the `UserRepository` interface lives in the domain or application module, and `PgUserRepository` in the infrastructure module imports it. If the interface lives next to the implementation in the infrastructure module, the domain still depends on infrastructure, and the dependency hasn't really been inverted.

## 330: How do you apply DIP across packages in a monorepo?

Put interfaces in the package that uses them (or in a small, stable contracts package) and implementations in separate packages that depend on it.

```text
packages/
  orders-core/       # domain + interfaces (PaymentGateway, OrderRepository)
  orders-postgres/   # implements OrderRepository, depends on orders-core
  payments-stripe/   # implements PaymentGateway, depends on orders-core
  api/               # composition root, wires everything
```

`orders-core` has no dependency on Postgres or Stripe. Tools like Nx module boundary rules or `dependency-cruiser` can enforce that it stays that way.

## 331: What is the Service Locator pattern and why is it often called an anti-pattern?

A service locator is a global registry that code asks for its dependencies:

```ts
class OrderService {
  place(order: Order) {
    const repo = ServiceLocator.get<OrderRepository>("OrderRepository");
    // ...
  }
}
```

It does decouple you from concrete classes, but the dependencies are hidden. You can't tell what `OrderService` needs without reading all its code, missing registrations fail only at runtime, and tests must set up the global registry. Constructor injection shows dependencies in the signature instead. Mark Seemann's writing on DI is the usual reference for this argument.

## 332: What are the pros and cons of DI containers?

Pros:

- They wire large object graphs automatically.
- They manage lifetimes (singleton, per request, transient).
- Frameworks like NestJS and Angular integrate them deeply, with good test tools.

Cons:

- Wiring becomes "magic": it's harder to see what gets created and when.
- Errors (missing providers, cycles) show up at startup instead of compile time.
- Decorators and tokens add boilerplate in TypeScript, since interfaces don't exist at runtime.

For small and medium Node.js apps, manual wiring in a composition root (often called "pure DI") is usually clear enough. Use a container when the framework provides one or the graph gets large.

## 333: What is constructor over-injection and what does it tell you?

Constructor over-injection is when a class needs many dependencies, say eight or more:

```ts
constructor(
  private users: UserRepository,
  private orders: OrderRepository,
  private payments: PaymentGateway,
  private mailer: Mailer,
  private sms: SmsSender,
  private analytics: Analytics,
  private audit: AuditLog,
  private features: FeatureFlags,
) {}
```

DI didn't cause the problem; it made it visible. The class almost certainly has several responsibilities. Fixes: split the class, group related dependencies behind a facade (for example, a `Notifier` that wraps `mailer` and `sms`), or move side effects like analytics and audit into event handlers or decorators.

## 334: What is an aggregate service (or facade service) in the context of DI?

When several dependencies are always used together for one purpose, you can hide them behind a single higher-level service. For example, `mailer`, `sms` and `push` become one `NotificationService` with `notify(user, message)`, which decides the channel.

This isn't just moving the parameters around. It creates a real concept with its own responsibility, and the original class becomes simpler because it no longer decides which channel to use. If the new service only forwards calls with no logic, it's just a middle man.

## 335: What is Clean Architecture?

Clean Architecture is Robert Martin's version of layered architecture, usually drawn as circles:

- **Entities**: core business rules.
- **Use cases**: application-specific business rules.
- **Interface adapters**: controllers, presenters, gateways that convert data.
- **Frameworks and drivers**: web framework, database, UI, external services.

The key rule is the dependency rule: source code dependencies point only inward. Inner circles know nothing about outer ones. Data crosses boundaries as simple structures, and outer layers implement interfaces that inner layers define.

## 336: What is hexagonal architecture (ports and adapters)?

Hexagonal architecture, from Alistair Cockburn, puts the application core in the middle and lets it talk to the outside world only through ports (interfaces). Adapters implement those ports for specific technologies.

- **Driving (primary) adapters** call into the app: HTTP controllers, CLI commands, tests.
- **Driven (secondary) adapters** are called by the app: database repositories, email senders, payment APIs.

The core doesn't care if it's driven by HTTP or a test, or whether it stores data in Postgres or memory. This makes testing easy and lets you swap technologies at the edges.

## 337: How do Clean, Hexagonal and Onion architectures differ?

They share the same core idea: business logic in the center, dependencies pointing inward, infrastructure at the edges behind interfaces.

The differences are mostly in naming and detail:

- **Hexagonal** focuses on ports and adapters, with no fixed number of inner layers.
- **Onion** (Jeffrey Palermo) names concentric layers: domain model, domain services, application services, infrastructure.
- **Clean** (Robert Martin) combines these with named circles and adds ideas like screaming architecture and the use case as a central unit.

In interviews, it's usually enough to explain the shared dependency rule and why it helps.

## 338: What is "screaming architecture"?

Screaming architecture means the top-level structure of a project should tell you what the application does, not which framework it uses.

A folder list like `controllers/`, `models/`, `views/` tells you "this is an MVC app". A list like `billing/`, `scheduling/`, `patients/` tells you "this is a healthcare scheduling app". The second is easier to navigate and keeps related code together.

## 339: Is Clean Architecture overkill for most web apps?

Often, yes. For a CRUD app where business logic is thin, full Clean Architecture means a lot of mapping between layers, many interfaces with one implementation, and lots of files for every simple feature.

It pays off when business rules are complex, when the app will live for many years, or when you really expect to change infrastructure. A pragmatic middle ground: keep business rules in plain modules without framework imports, wrap external services, and skip the extra layers where there's nothing to protect.

## 340: What is vertical slice architecture?

Vertical slice architecture (popularized by Jimmy Bogard) organizes code by feature or request instead of by technical layer. Each slice, like "PlaceOrder" or "GetInvoice", contains everything it needs: handler, validation, data access and response mapping.

Slices don't share much, so changing one feature rarely affects another. Shared abstractions are added only when they're really needed. It works well with CQRS-style handlers and fits teams that find layered architectures too heavy. The trade-off is some duplication between slices.

## 341: What is a use case (or interactor) in Clean Architecture?

A use case is a class or function that runs one application action, like `PlaceOrder` or `ResetPassword`. It takes a simple input, uses entities and ports (repositories, gateways) to do the work, and returns a simple output.

```ts
export class PlaceOrder {
  constructor(
    private orders: OrderRepository,
    private payments: PaymentGateway,
  ) {}

  async execute(input: PlaceOrderInput): Promise<PlaceOrderOutput> {
    const order = Order.create(input.customerId, input.items);
    await this.payments.charge(order.total, input.paymentToken);
    await this.orders.save(order);
    return { orderId: order.id };
  }
}
```

Each use case is easy to find, test and reason about, and the list of use cases describes what the system can do.

## 342: What is the cost of mapping data between layers, and how do you keep it manageable?

In strict layered designs, data is mapped from request DTO to command, to entity, to persistence model and back. Each mapping is code to write, test and update when a field changes.

To keep it manageable:

- Map only at real boundaries where the shapes differ, like the public API and the database.
- Use TypeScript utility types to derive related types instead of redefining them.
- Generate types where you can (from OpenAPI, Prisma or a schema library).
- Accept that some layers can share types in simple features.

## 343: What does "the framework is a detail" mean?

Robert Martin argues that the web framework, the database and the UI are details: implementation choices that business rules shouldn't depend on. Your business rules should work the same way whether they're called from Express, a queue worker or a test.

In practice you rarely swap frameworks, so the main benefit isn't swapping. It's that business logic stays testable without spinning up the framework, and framework upgrades only touch the outer layer.

## 344: Is treating the database as a detail realistic?

Partly. You can hide queries behind repositories so business logic doesn't import an ORM. But databases affect design in ways an interface can't hide: transactions, consistency, query performance and how data is loaded.

Pretending the database doesn't exist can lead to N+1 queries or to loading huge object graphs into memory. A realistic approach is to keep the business rules independent, while letting repositories and queries be designed with the real database in mind. Read-heavy queries often skip the domain model entirely and query the database directly for a specific view.

## 345: What are entities, value objects and aggregates in Domain-Driven Design?

- **Entity**: an object with an identity that stays the same as its data changes, like a `Customer` with an ID.
- **Value object**: an object defined only by its values, usually immutable, like `Money` or `Address`.
- **Aggregate**: a cluster of entities and value objects treated as one unit for changes, with one entity as the root. Outside code can only change the aggregate through its root.

For example, an `Order` aggregate contains `OrderLine`s. You add a line with `order.addLine(...)`, never by editing an `OrderLine` directly, so `Order` can check its rules.

## 346: How do aggregates protect invariants?

The aggregate root is the only way in, so it can check every rule before allowing a change.

```ts
class Order {
  #lines: OrderLine[] = [];
  #status: "draft" | "placed" = "draft";

  addLine(product: ProductId, qty: number, price: Money) {
    if (this.#status !== "draft")
      throw new Error("Cannot change a placed order");
    if (qty <= 0) throw new Error("Quantity must be positive");
    this.#lines.push(new OrderLine(product, qty, price));
  }

  place() {
    if (this.#lines.length === 0) throw new Error("Order is empty");
    this.#status = "placed";
  }
}
```

The aggregate is also the unit of saving and of transactions: you load and save the whole order together. Keep aggregates small; large ones cause locking and performance problems.

## 347: What are bounded contexts and the ubiquitous language?

The **ubiquitous language** is the shared vocabulary developers and business people use for a domain. The same words appear in conversations, docs and code.

A **bounded context** is the boundary within which one model and its language apply. The word "customer" can mean different things in sales (a lead with contact info) and in billing (an account with payment details). Instead of one giant `Customer` class that tries to serve everyone, each context has its own model.

This is SRP and naming applied at a large scale.

## 348: What is an anti-corruption layer?

An anti-corruption layer is a translation layer between your model and an external system (or legacy system) that has a different, messier model. It converts their concepts into yours so their structure doesn't leak into your code.

```ts
class LegacyCrmCustomerAdapter implements CustomerDirectory {
  async find(id: CustomerId): Promise<Customer> {
    const raw = await legacyCrm.getCust({ CUST_NO: id.value });
    return new Customer(
      CustomerId.of(raw.CUST_NO),
      raw.NM_FIRST + " " + raw.NM_LAST,
    );
  }
}
```

It's the Adapter pattern used for a whole external model. It's especially useful during migrations with the Strangler Fig pattern.

## 349: What is the difference between domain events and integration events?

- **Domain events** describe something that happened inside one bounded context (`OrderPlaced`). They're used inside the same service, often in the same process or transaction, to trigger side effects without coupling.
- **Integration events** are published to other services, usually through a message broker. They're a public contract, so they need stable schemas, versioning and care about what data they expose.

Mixing them up leads to leaking internal details to other teams, or to over-engineering internal events with versioning they don't need.

## 350: How do you deal with naming when two parts of the business use the same word differently?

Don't force one shared model. Treat it as two bounded contexts, each with its own type, even if the name is the same:

```ts
// sales/customer.ts
export interface Customer {
  id: string;
  name: string;
  leadSource: string;
}

// billing/customer.ts
export interface Customer {
  id: string;
  billingEmail: string;
  paymentMethodId: string;
}
```

Or use more precise names where the contexts meet (`Prospect` vs `BillingAccount`). Share only the ID between them. A single `Customer` with every field from every department becomes a God object that everyone is afraid to change.

## 351: What does "make illegal states unrepresentable" mean?

It means designing your types so that invalid combinations of data can't be created at all, so you don't need runtime checks or comments to prevent them.

```ts
// Allows illegal states: verified but no verifiedAt, or the other way round
interface Email {
  address: string;
  isVerified: boolean;
  verifiedAt?: Date;
}

// Only legal states exist
type Email =
  | { kind: "unverified"; address: string }
  | { kind: "verified"; address: string; verifiedAt: Date };
```

The phrase comes from Yaron Minsky (OCaml), and it's a big part of type-driven design. Fewer possible states means fewer bugs and fewer tests.

## 352: What does "parse, don't validate" mean?

The idea, from Alexis King's article, is that a validator checks data and throws it away (`isValidEmail(s): boolean`), so later code still has a plain `string` and has to trust or re-check it. A parser checks data and returns a more precise type that proves the check happened.

```ts
type Email = string & { readonly __brand: "Email" };

function parseEmail(input: string): Email {
  if (!/^[^@\s]+@[^@\s]+$/.test(input)) throw new Error(`Invalid email: ${input}`);
  return input as Email;
}

function sendWelcome(to: Email) { ... } // can't be called with an unchecked string
```

Parse at the boundary once, and the rest of the code works with types that can't be invalid. Schema libraries like Zod work the same way: `schema.parse(input)` returns typed data.

## 353: What are branded types in TypeScript?

TypeScript uses structural typing, so two `string` types are interchangeable even if they mean different things. A brand adds a fake property to make them distinct at compile time, with no runtime cost.

```ts
type UserId = string & { readonly __brand: "UserId" };
type OrderId = string & { readonly __brand: "OrderId" };

function getOrder(id: OrderId) { ... }

const userId = "u_1" as UserId;
getOrder(userId); // compile error
```

Create branded values only in one place (a parser or factory), so the cast happens once. Zod supports this with `.brand<"UserId">()`. It's a cheap fix for primitive obsession.

## 354: What are the trade-offs of heavy type-driven design in TypeScript?

Benefits: many bugs become compile errors, the types document the rules, and refactoring is safer.

Costs:

- Complex types (deep conditional and mapped types) are hard to read and give confusing error messages.
- Type-checking can get slow in big codebases.
- TypeScript's types are erased at runtime, so you still need runtime validation at boundaries.
- New team members may struggle with clever type-level code.

Use precise types for domain concepts and state, but keep the type code itself as simple as the problem allows.

## 355: What are the trade-offs between Result types and exceptions in TypeScript?

**Result types**:

- Errors are visible in the signature, and the compiler forces handling.
- Good for expected failures (validation, "not found", business rule violations).
- But they add boilerplate, spread through every caller, and don't fit well with libraries and frameworks that throw.

**Exceptions**:

- Less code, and work naturally with `async`/`await` and frameworks.
- But nothing in the type tells you what a function might throw, and `catch` gives you `unknown`.

A common middle ground: use Results for expected domain failures in the core, exceptions for unexpected problems, and convert between them at boundaries. Consistency within a codebase matters more than which one you choose.

## 356: How do you document which errors a function can throw when TypeScript has no checked exceptions?

TypeScript can't express thrown types in the signature, and `catch (e)` is always `unknown` (with `useUnknownInCatchVariables`, part of `strict`). Options:

- Use `@throws` in TSDoc for public functions.
- Throw a small set of custom error classes and handle them with `instanceof`.
- Return Result types for errors callers are expected to handle.
- Write tests that show each error case.

Also, always narrow in `catch` before using the error:

```ts
catch (error) {
  if (error instanceof ValidationError) return badRequest(error.message);
  throw error;
}
```

## 357: How do you wrap errors without losing context?

When you catch a low-level error and throw a higher-level one, pass the original as `cause`:

```ts
try {
  await s3.send(new PutObjectCommand(params));
} catch (error) {
  throw new StorageError(`Failed to upload ${key}`, { cause: error });
}

class StorageError extends Error {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = "StorageError";
  }
}
```

Callers see a meaningful error from your domain, and logs and debuggers still show the full chain with the original stack trace. Node.js prints `cause` chains automatically.

## 358: How should a Node.js process handle unexpected errors at the top level?

- Listen to `unhandledRejection` and `uncaughtException`, log the error with as much context as possible, and then exit. Since Node.js 15, an unhandled rejection crashes the process by default.
- Don't try to keep running after an `uncaughtException`: the process may be in a broken state. Let your process manager or container platform restart it.
- On `SIGTERM`, stop accepting new requests, finish in-flight work, close connections, then exit (graceful shutdown).

Keep this code in one place at startup, not scattered across modules.

## 359: What is "test-induced design damage"?

David Heinemeier Hansson used this term to criticize designs that get more complex only to make them unit-testable: extra interfaces with one implementation, layers of indirection, and mocks for everything, even when integration tests would cover the code just as well.

The counterpoint is that hard-to-test code is often badly coupled, and making it testable improves the design. Both are true sometimes. A good rule: add an abstraction when it reflects a real boundary (like an external service), not just to make a mock possible.

## 360: What are the London (mockist) and Chicago (classicist) schools of TDD?

- **Chicago / classicist** (Kent Beck, Martin Fowler's description): test units of behavior with real collaborators where possible. Use test doubles only for awkward dependencies like the database or network. Tests check state and results.
- **London / mockist** ("Growing Object-Oriented Software, Guided by Tests" by Freeman and Pryce): test each class in isolation, mocking its collaborators, and check interactions. Design proceeds outside-in, discovering interfaces through mocks.

Classicist tests survive refactoring better. Mockist tests can help design interfaces between objects but are more coupled to implementation. Many teams mix them: mockist at system boundaries, classicist inside.

## 361: What are sociable and solitary unit tests?

These are Martin Fowler's terms:

- **Solitary** tests replace all collaborators of the unit under test with doubles.
- **Sociable** tests let the unit use its real collaborators, as long as they're fast and deterministic.

Sociable tests catch bugs in how units work together and don't break when you move code between collaborators. Solitary tests pinpoint failures more exactly. Most teams lean toward sociable tests for domain logic and use doubles only for slow or external dependencies.

## 362: What is a "unit" in unit testing?

It doesn't have to be one class or one function. A better definition is a unit of behavior: something meaningful the code does, which might involve several classes working together.

If "unit" means "one class", every refactor that splits or merges classes breaks tests. If it means "one behavior", tests survive internal restructuring. Vladimir Khorikov's book "Unit Testing Principles, Practices, and Patterns" explains this view well.

## 363: How can test fakes drift away from the real implementation, and how do you prevent it?

A fake (like an in-memory repository) is written once and then the real implementation changes: new constraints, different sorting, new errors on duplicates. Tests using the fake keep passing, but the real system behaves differently. This is an LSP violation in your test code.

Prevent it by running the same contract test suite against both the fake and the real implementation (see question 289). When the real one changes behavior, the contract tests fail for the fake until it's updated too.

## 364: What is property-based testing?

Instead of writing specific examples, you describe properties that should hold for all inputs, and the tool generates hundreds of random inputs to try to break them. When it finds a failure, it shrinks the input to the smallest failing case.

```ts
import fc from "fast-check";

test("sorting twice equals sorting once", () => {
  fc.assert(
    fc.property(fc.array(fc.integer()), (arr) => {
      const once = [...arr].sort((a, b) => a - b);
      const twice = [...once].sort((a, b) => a - b);
      expect(twice).toEqual(once);
    }),
  );
});
```

It's great for parsers, serializers (round-trip: `parse(format(x)) === x`), and pure business logic. `fast-check` is the common library for JavaScript.

## 365: What is approval testing (golden master testing)?

Approval testing records the full output of the code for a set of inputs (the "golden master") and fails when the output changes. When a change is intended, you review the difference and approve the new output.

It's very useful before refactoring legacy code that has complex output you don't fully understand, like reports or generated documents. Generate many input combinations, record the outputs, refactor, and check that nothing changed. Snapshot testing in Jest and Vitest is a form of it.

## 366: How do you refactor safely when you can't add tests first?

Sometimes code is too tangled to test without changing it. Then:

- Use only automated refactorings from the IDE (rename, extract function, extract variable, move), which are very unlikely to change behavior.
- Make tiny, mechanical steps, and commit each one.
- Lean on the compiler: with TypeScript, change a signature and let the errors show you every call site.
- Pair with someone or get a careful review for these steps.
- Add tests as soon as a seam appears.

Some teams call these "provable refactorings": changes so mechanical they can be trusted without tests.

## 367: What is the Parallel Change (expand and contract) technique?

Parallel Change lets you change an interface used in many places without a big-bang change:

1. **Expand**: add the new version next to the old one (new method, new field, new endpoint). Both work.
2. **Migrate**: move callers to the new version one by one, in small safe commits.
3. **Contract**: when nothing uses the old version, remove it.

It's used for function signatures, database columns, API fields and events. The code is always in a working state, and each step can be deployed on its own.

## 368: What is Branch by Abstraction?

Branch by Abstraction is a way to replace a large component on the main branch without a long-lived feature branch:

1. Put an abstraction (interface) in front of the old component.
2. Move all callers to use the abstraction.
3. Build the new implementation behind the same abstraction, step by step, with a toggle to choose which one runs.
4. Switch over, then delete the old implementation and maybe the toggle.

It's DIP used as a migration tool. It works well with trunk-based development, since everything is merged often and the system keeps working.

## 369: How do codemods help with large-scale refactoring?

A codemod is a script that changes code automatically by editing its syntax tree, not with find-and-replace. It can rename an API across thousands of files, change import paths, or rewrite a call pattern.

Common tools: `jscodeshift`, `ts-morph` (uses the TypeScript compiler API, so it understands types), and `ast-grep`. Libraries like React and Next.js ship official codemods for their upgrades.

Run codemods in their own commits, review a sample of the changes, and rely on type checks and tests to catch edge cases the script missed.

## 370: What is the Mikado Method?

The Mikado Method is a way to do a large refactoring safely:

1. Write down the goal.
2. Try to make the change directly.
3. If things break, write down what needs to change first (the prerequisites), then **revert** your change.
4. Pick a prerequisite and repeat from step 2.
5. When you reach a change that works without breaking anything, commit it and move back up the graph.

You end up with a graph of dependencies (named after the Mikado pick-up sticks game) and make progress from the leaves to the goal, always keeping the code working. The key habit is reverting instead of piling fixes on a broken build.

## 371: What is hotspot analysis, and how does it help decide where to refactor?

A hotspot is code that is both complex and changed often. Complex code that nobody touches isn't worth cleaning. Simple code that changes often is fine. Complex code that changes all the time is where messy code costs the most.

You can find change frequency from Git:

```bash
git log --since="1 year ago" --name-only --format="" | sort | uniq -c | sort -rn | head -20
```

Combine that with a complexity measure (lines of code or a complexity tool). Adam Tornhill's "Your Code as a Crime Scene" and the CodeScene tool are built around this idea.

## 372: Why can code quality metrics be dangerous as targets?

Goodhart's law says: when a measure becomes a target, it stops being a good measure. If teams are rewarded for 90% coverage, they write tests with no assertions. If functions must be under 20 lines, people split them in odd places. If complexity must stay under 10, logic moves into lookup tables nobody understands.

Use metrics to find areas worth looking at and to see trends, not as goals that decide performance reviews. Pair them with human judgment in code review.

## 373: What is the "clean code, horrible performance" debate about?

In 2023, Casey Muratori showed a benchmark where following some "Clean Code" advice (polymorphism instead of switch, small virtual functions, hiding data in objects) made a calculation many times slower than a straightforward switch-and-table version in C++.

The fair takeaway: in hot paths (game engines, data processing, tight loops), how data is laid out and how many indirect calls happen really matter, and the clean code rules weren't written with that in mind. For typical web app code, the slow parts are I/O, network and database queries, and readability matters more. Know which kind of code you're writing.

## 374: How do abstractions affect performance in JavaScript specifically?

Usually less than people fear. Modern engines (V8, JavaScriptCore) inline small functions, and polymorphic calls are fast when call sites see a few object shapes.

Things that can hurt in hot paths:

- Call sites that see many different object shapes ("megamorphic"), which stop some optimizations.
- Creating lots of short-lived objects or closures in tight loops (garbage collector pressure).
- Long chains of `map`/`filter`/`reduce` over huge arrays, each creating a new array.
- Spreading objects to copy them in loops.

Measure with the profiler before changing anything, and keep any optimized code isolated with a comment.

## 375: How does immutability affect performance, and how do libraries help?

Copying objects and arrays on every change costs memory and time, especially for big structures. Naive deep copies are the worst case.

Ways to handle it:

- **Structural sharing**: copy only the changed path and reuse the rest. Spread syntax does this one level at a time.
- **Immer**: lets you write code that looks like mutation (`draft.items.push(x)`) and produces an immutable result with structural sharing. Redux Toolkit uses it.
- `structuredClone` for true deep copies when you really need them.

For most UI state, the cost is small and the benefit (simple change detection, fewer bugs) is large.

## 376: When is duplication better than abstraction in performance-critical code?

In hot paths, a generic abstraction may add overhead: indirect calls, extra parameters, checks for cases that don't apply. Two specialized versions of a loop, each tuned for its case, can be much faster than one generic version.

If you do this, keep the duplicated code close together, write a comment explaining why, and cover both versions with the same tests (or a property test comparing them). It's a deliberate exception, not a new habit.

## 377: How can shared mutable state cause race conditions in single-threaded Node.js?

Node.js runs JavaScript on one thread, but `await` gives other code a chance to run in between. If two requests read and update the same state around an `await`, one update can be lost:

```ts
async function addCredit(userId: string, amount: number) {
  const user = await db.users.find(userId); // both requests read 100
  user.credit += amount; // both compute 110
  await db.users.save(user); // second save overwrites first
}
```

Fixes: let the database do the update atomically (`UPDATE users SET credit = credit + $1`), use transactions with the right isolation level or row locks, use optimistic locking with a version column, or serialize work per user with a queue. Clean code makes this easier to see: if state changes only happen in a few clearly named places, races are easier to spot.

## 378: What is the fragile base class problem in detail?

When a subclass depends on how its parent works internally, a seemingly safe change in the parent can break it. A classic example:

```ts
class CountingSet<T> extends Set<T> {
  addCount = 0;

  add(value: T) {
    this.addCount++;
    return super.add(value);
  }
}
```

In JavaScript, the `Set` constructor calls `this.add` for each value you pass in, so `new CountingSet([1, 2])` already counts 2. That's fine if you know it, but the subclass depends on an internal detail of the parent. If a parent class later starts calling `add` from another method, or stops calling it, the counts change silently.

Composition avoids this: wrap a `Set` and forward only the methods you choose, so the parent's internals can't affect you.

## 379: Why did React move from class components and mixins to hooks?

Mixins (in the old `createClass` API) let components share behavior, but they caused name clashes, hidden dependencies between mixins, and it was hard to know where a method came from. Class components with higher-order components and render props fixed some of that but led to "wrapper hell" and logic split across lifecycle methods.

Hooks let you share stateful logic by calling plain functions, with explicit inputs and outputs, and group related code together instead of splitting it by lifecycle. It's a move from inheritance-style reuse to composition.

## 380: How do you do composition with delegation in TypeScript?

Instead of extending a class to reuse its behavior, hold an instance and forward calls you want to expose.

```ts
class AuditedRepository<T extends { id: string }> implements Repository<T> {
  constructor(
    private inner: Repository<T>,
    private audit: AuditLog,
  ) {}

  find(id: string) {
    return this.inner.find(id);
  }

  async save(entity: T) {
    await this.inner.save(entity);
    await this.audit.record("save", entity.id);
  }
}
```

It's a bit more typing than `extends`, but you control exactly what's exposed and you're not tied to the parent's internals. Both objects implement the same interface, so callers can use either one.

## 381: What are mixins in TypeScript, and when should you use them?

TypeScript supports class mixins: functions that take a class and return a new class extending it.

```ts
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
  };
}

class User {
  constructor(public name: string) {}
}

const TimestampedUser = Timestamped(User);
const user = new TimestampedUser("Ann");
```

They can add small, independent capabilities, but they share the problems of inheritance: name clashes, hidden ordering issues and hard-to-read types. Plain composition or helper functions are usually clearer. Use mixins sparingly, mostly in libraries.

## 382: How does semantic versioning relate to OCP and LSP?

Semantic versioning (major.minor.patch) is a promise about compatibility:

- **Patch and minor** releases must not break existing users. That's OCP and LSP across versions: you extend behavior and the new version must be substitutable for the old one.
- **Major** releases may break things, and users must change their code.

Ways to stay compatible: add new optional parameters instead of changing existing ones, add new functions instead of changing behavior, deprecate before removing, and use Parallel Change for larger moves.

## 383: What is Hyrum's law and how does it affect API design?

Hyrum's law (from Hyrum Wright at Google): "With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody."

So even details you never documented, like the order of items in a response, error message text or timing, become part of the real contract. To limit this: expose as little as possible, randomize or vary things you don't promise (for example, Go randomizes map iteration order), and document clearly what is and isn't guaranteed.

## 384: What is a leaky abstraction?

Joel Spolsky's "Law of Leaky Abstractions" says all non-trivial abstractions leak to some degree: details they're supposed to hide sometimes affect you anyway.

Examples: TCP hides packet loss until the network is slow, then your app freezes. An ORM hides SQL until a query becomes slow and you need to know what SQL it generates. `fetch` hides HTTP until you hit CORS.

The lesson isn't to avoid abstractions. It's to know what's underneath the ones you use, and when designing your own, to be honest in the interface about things like errors, latency and cost.

## 385: Why are ORMs often called leaky abstractions?

ORMs make database rows look like objects in memory. But databases behave differently from objects:

- Accessing a related property in a loop can fire a query per item (the N+1 problem).
- Transactions, locks and isolation levels matter and can't be hidden.
- Some queries are much easier and faster in plain SQL.

Modern tools like Prisma and Drizzle are more explicit about queries, which helps. Whatever you use, check the generated SQL for important queries and keep data access in repositories, so performance fixes stay in one place.

## 386: What does Ousterhout mean by "general-purpose modules are deeper"?

He suggests designing modules to be "somewhat general-purpose": the interface should be general enough to cover several uses, while the implementation handles today's needs.

For example, for a text editor, instead of methods like `backspace()` and `deleteSelection()`, a general `delete(start, end)` method is simpler and works for every case. The UI code handles what "backspace" means. General interfaces tend to be simpler and lead to deeper modules. This doesn't contradict YAGNI as long as you don't build features nobody needs; it's about the shape of the interface.

## 387: What does "define errors out of existence" mean?

It's one of Ousterhout's ideas: many errors can be removed by designing the API so the error case simply can't happen or isn't an error.

Examples:

- `Array.prototype.slice` with an end index past the array length just returns what's available instead of throwing.
- A `delete(key)` that does nothing if the key doesn't exist, instead of throwing "not found". The caller wanted the key gone, and it is.
- `mkdir -p` doesn't fail if the directory already exists.

Every error a function can throw is something every caller must think about. Fewer error cases means simpler code everywhere.

## 388: What does "pull complexity downwards" mean?

Ousterhout argues that when complexity can't be avoided, the module should handle it inside, rather than pushing it to its callers through configuration options or extra steps.

A module is used by many callers but written once, so complexity inside it is paid once, while complexity in its interface is paid by every caller. For example, a good HTTP client picks sensible timeouts and retry defaults instead of forcing every caller to configure them.

## 389: What is the difference between tactical and strategic programming?

From "A Philosophy of Software Design":

- **Tactical programming** focuses on getting the current feature working as fast as possible. Each shortcut is small, but they add up, and the system gets more complex with every change.
- **Strategic programming** treats working code as not enough. You also invest a bit of time in good design with each change, like finding a cleaner structure or improving docs.

Ousterhout suggests spending about 10-20% of development time on these investments. It pays back within months through faster changes.

## 390: What is the second-system effect, and how does it relate to rewrites?

Fred Brooks described the second-system effect in "The Mythical Man-Month": the second version of a system tends to be over-designed, because the team adds every feature and idea they had to leave out of the first.

Combined with the fact that old code holds years of bug fixes and edge cases, this is why big rewrites so often fail or run late (Joel Spolsky's "Things You Should Never Do" is the famous essay about Netscape). Incremental refactoring and the Strangler Fig pattern are the safer path in most cases.

## 391: What is Postel's law, and why is it now questioned?

Postel's law (the robustness principle): "Be conservative in what you send, be liberal in what you accept."

It helped early internet protocols work across many implementations. But being liberal in what you accept means broken inputs keep working, other systems start relying on that, and over time the real format becomes whatever the most forgiving implementation accepts. It has also caused security issues when different systems parse the same input differently. Modern API design usually prefers strict validation with clear errors, which fits "fail fast".

## 392: How should you think about comments according to Ousterhout, compared to "Clean Code"?

"Clean Code" treats most comments as a failure to write clear code. Ousterhout argues comments are needed for things code can't say:

- **Interface comments**: what a module or function does, its parameters, side effects and errors, so callers don't have to read the implementation.
- **Design decisions**: why it's built this way, what was tried and rejected.
- **Precise meaning of variables**: units, ranges, whether a boundary is inclusive.

Both agree that comments repeating the code are useless. The practical middle ground: good names first, plus comments for interfaces and for "why".

## 393: How do you choose between a short name and a precise name?

A name should be precise enough to create the right picture in the reader's mind, and no longer than that. Ousterhout's test: if a name could reasonably refer to several things, it's too vague. If it's hard to find a precise name, the thing might not have a clear purpose.

Context matters too. Inside a `User` class, `name` is clear; at module level, `userDisplayName` might be needed. Loop indices and short lambdas can use short names because their scope is tiny.

## 394: How does team ownership affect code quality?

Code with clear owners tends to stay cleaner: the owners feel responsible for its design and know its history. Code that "everyone" owns often slowly decays, because nobody feels responsible for refactoring it.

Common approaches are `CODEOWNERS` files to route reviews to the right people, and team-owned modules aligned with business areas. Pure "collective ownership" (from Extreme Programming) can work in small teams with strong shared standards, pairing and good tests.

## 395: What is the difference between essential and accidental complexity?

Fred Brooks, in "No Silver Bullet", split complexity into:

- **Essential complexity**: comes from the problem itself. Tax rules are complicated because tax law is complicated.
- **Accidental complexity**: comes from our tools and choices: confusing abstractions, unnecessary layers, poor names, boilerplate.

Clean code can't remove essential complexity, but it can stop accidental complexity from piling on top of it and make the essential parts clear and well organized.

## 396: What does "coupling is the enemy of change" mean in practice for modern web apps?

Every coupling point is a place where one change forces another. In web apps, common hidden couplings include:

- Front-end and back-end sharing a database model directly, so a column rename breaks the UI.
- Services reading each other's databases.
- Tests coupled to CSS class names or DOM structure.
- Components coupled to a global store's exact shape.
- Shared "common" libraries with business logic used by many teams.

Reduce coupling at the places that change most: put contracts (API schemas, events, accessible roles in tests) between parts instead of internal details.

## 397: How do you design a stable API contract between front-end and back-end?

- Write the contract down: OpenAPI, GraphQL schema, or a shared schema library in a monorepo.
- Generate types and clients from it so both sides stay in sync.
- Make additive changes only (new optional fields, new endpoints), and deprecate before removing.
- Don't expose database models directly. Map to response types.
- Test the contract, for example with consumer-driven contract tests (like Pact) or schema validation in CI.

This is ISP and DIP at the system level: both sides depend on the contract, not on each other's internals.

## 398: What is the "Tell, Don't Ask" principle's limit?

Taken too far, "Tell, Don't Ask" pushes every operation that uses an object's data onto that object. A `User` class ends up with methods for rendering, emailing, exporting to CSV and calculating taxes, because each uses user data. That breaks SRP.

The balance: put behavior that protects the object's own rules and invariants on the object. Operations that just read data for another purpose (display, reporting, serialization) can live elsewhere and ask for what they need. Martin Fowler has written that he doesn't use "Tell, Don't Ask" as a strict rule for this reason.

## 399: How do you keep a codebase consistent when many teams work in it?

- Shared tooling: one lint config, one Prettier config, one TypeScript base config, shipped as internal packages in a monorepo.
- Generators or templates for new modules, so everyone starts from the same structure.
- Architecture rules enforced in CI (import boundaries, dependency rules).
- A short, living set of docs: style guide, ADRs, examples of "the right way".
- A small group (often called a guild or platform team) that maintains the shared setup and reviews proposals to change it.

Consistency matters more than any single choice. A codebase where everything is done one slightly-imperfect way is easier to work in than one with five "better" ways.

## 400: How has AI-assisted coding changed the importance of clean code?

AI coding assistants make writing code much faster, which means more code to read and review. They also work better in clean codebases: clear names, small modules, consistent patterns and good tests give the assistant better context, and tests catch its mistakes.

Common problems with generated code: duplicated logic instead of reusing existing helpers, inconsistent naming and patterns, unnecessary abstractions, swallowed errors, invented APIs and missing edge cases. Reviewing generated code with the same clean code standards as human code, and keeping clear project conventions written down, matters more than before, not less.

## 401: A checkout function has a switch over payment providers that grows every month. How would you redesign it?

Start by defining a `PaymentProvider` interface with what checkout needs, then move each case into its own implementation and look them up from a registry.

```ts
interface PaymentProvider {
  readonly id: string;
  charge(amount: Money, token: string): Promise<ChargeResult>;
  refund(chargeId: string, amount: Money): Promise<void>;
}

class PaymentProviderRegistry {
  private providers = new Map<string, PaymentProvider>();

  register(provider: PaymentProvider) {
    this.providers.set(provider.id, provider);
  }

  get(id: string): PaymentProvider {
    const provider = this.providers.get(id);
    if (!provider) throw new Error(`Unknown payment provider: ${id}`);
    return provider;
  }
}
```

Checkout now calls `registry.get(method).charge(...)`. Adding a provider means a new class and one `register` call in the composition root (OCP). Each provider gets its own tests, and a shared contract test suite checks they all behave the same way (LSP). Do it step by step: extract one provider at a time while the switch still handles the rest.

## 402: A notification service sends email, SMS and push, and some channels don't support all features (like attachments). How do you model it?

Don't put `sendAttachment` on a shared interface that SMS can't implement. Split capabilities into small interfaces (ISP):

```ts
interface MessageSender {
  send(to: Recipient, message: Message): Promise<void>;
}

interface AttachmentSender {
  sendWithAttachments(to: Recipient, message: Message, files: File[]): Promise<void>;
}

class EmailSender implements MessageSender, AttachmentSender { ... }
class SmsSender implements MessageSender { ... }
```

Code that needs attachments asks for an `AttachmentSender`, so it can never get SMS by mistake. A `NotificationService` that picks channels based on user preferences depends only on these interfaces (DIP), and the concrete senders are wired at startup.

## 403: A form component has grown to 30 props. How do you clean it up?

Look at why it has so many props. Usually it's one of these:

- **Many boolean variants** (`isCompact`, `showFooter`, `hideLabels`): replace with a `variant` prop or split into separate components.
- **Many render customizations**: switch to composition with `children` or compound components (`<Form.Field>`, `<Form.Actions>`).
- **Passing data and callbacks through to children**: let the parent render those children directly.
- **Form logic mixed in**: move it into a form library (like React Hook Form) or a custom hook.

Do it gradually: add the new composable API next to the old props, migrate callers, then remove the old props (Parallel Change).

## 404: You inherit a 3,000-line utils.ts that everything imports. What do you do?

1. Find out what's used: tools like Knip or the editor's "find references" show which exports are used and by whom. Delete dead ones first.
2. Group the remaining functions by topic (dates, money, strings, API helpers, domain logic).
3. Move each group to its own module. If a helper is only used by one feature, move it into that feature folder.
4. Keep `utils.ts` temporarily re-exporting the moved functions, mark it deprecated, and use a codemod or the editor to update imports.
5. Delete `utils.ts` when nothing imports it, and add a lint rule to stop a new one from appearing.

Domain logic hiding in "utils" (like `calculateShippingCost`) is the most important find: it belongs in the domain, with tests.

## 405: A service class takes 12 constructor dependencies. How do you approach it?

Too many dependencies is a strong sign of too many responsibilities.

1. List which methods use which dependencies. Methods that share a small subset usually form a separate responsibility.
2. Extract those groups into their own services.
3. Look for dependencies always used together (like `mailer`, `sms`, `push`) and put them behind a higher-level abstraction such as `Notifier`.
4. Move side effects that aren't part of the main flow (analytics, audit logs, cache invalidation) to event handlers or decorators.

After this, the original class often becomes a thin coordinator with three or four dependencies, or disappears entirely.

## 406: Your team's tests break on every refactor, even when behavior doesn't change. What's going wrong and how do you fix it?

The tests are coupled to implementation details. Common causes:

- Heavy mocking that checks which internal functions were called and how.
- Testing private methods or internal state.
- UI tests that query by CSS classes or component internals.
- Snapshot tests of large, unstable outputs.

Fixes: test through public interfaces and check outcomes; replace mocks with fakes for internal collaborators, and keep mocks only at real boundaries; in UI tests, query by role and text like a user would (Testing Library); shrink snapshots to the important parts. When you touch a brittle test, rewrite it in the better style rather than patching it.

## 407: A Bird base class has a fly() method, and now you need a Penguin. What do you do?

Making `Penguin.fly()` throw or do nothing breaks LSP: code that loops over birds and calls `fly()` will crash or behave wrongly.

The problem is the base class assumes all birds fly. Fix the model:

```ts
interface Bird {
  name: string;
  eat(): void;
}

interface FlyingBird extends Bird {
  fly(): void;
}

class Sparrow implements FlyingBird { ... }
class Penguin implements Bird { ... }
```

Code that needs flying asks for `FlyingBird`. The general lesson: when a subtype can't honor the base type's promises, the abstraction is wrong, and the fix is in the hierarchy, not in the subtype.

## 408: Discount rules change every week and the code is a growing if-else chain. How would you restructure it?

Turn each rule into a small object or function with the same interface, and evaluate them as a list.

```ts
interface DiscountRule {
  applies(cart: Cart, customer: Customer): boolean;
  discount(cart: Cart): Money;
}

const rules: DiscountRule[] = [
  new LoyaltyDiscount(),
  new BulkDiscount(10),
  new HolidayDiscount(holidayDates),
];

function totalDiscount(cart: Cart, customer: Customer): Money {
  return rules
    .filter((rule) => rule.applies(cart, customer))
    .reduce(
      (sum, rule) => sum.add(rule.discount(cart)),
      Money.zero(cart.currency),
    );
}
```

New rules are new classes, each tested alone. Make the policy for combining rules (stack all, best one only, max cap) explicit in one place. If business people need to change rules without deploys, store rule parameters in a database or config, but avoid building a full rules engine until it's truly needed.

## 409: What is the Specification pattern?

The Specification pattern puts a business rule that answers "does this object match?" into its own object, so rules can be named, reused and combined.

```ts
interface Spec<T> {
  isSatisfiedBy(item: T): boolean;
}

const and = <T>(...specs: Spec<T>[]): Spec<T> => ({
  isSatisfiedBy: (item) => specs.every((s) => s.isSatisfiedBy(item)),
});

const isOverdue: Spec<Invoice> = {
  isSatisfiedBy: (i) => i.dueDate < new Date() && !i.paid,
};
const isLarge: Spec<Invoice> = {
  isSatisfiedBy: (i) => i.amount.cents > 100_000,
};

const needsEscalation = and(isOverdue, isLarge);
```

It comes from Eric Evans and Martin Fowler. It's useful for complex filtering and validation rules. For simple cases, a well-named function is enough.

## 410: Your team keeps arguing about how much abstraction to add. How do you resolve it?

- Agree on a default: start simple, abstract on the second or third real case, except at clear boundaries (external services, I/O) where an interface is cheap and helps testing.
- Make decisions with concrete examples, not in the abstract. "Show me the next two cases this would support."
- Use time-boxed spikes when it's unclear, and compare both versions.
- Write the decision down as an ADR so the same debate doesn't repeat.
- Revisit later: if the simple version hurts, refactor; if the abstraction is unused, remove it.

## 411: A junior developer submitted a pull request with factories, strategies and an abstract base class for a feature that has one case. How do you review it?

Be kind and specific. Acknowledge the effort and that they know the patterns. Then explain the cost: more files to read, more indirection, more to maintain, and it's based on guesses about future needs.

Suggest the simplest version that works, and explain when each pattern would earn its place ("when we get a second provider, extracting this interface will take ten minutes"). Pairing on the simplification often teaches more than comments. Avoid making them feel the learning was wasted; knowing patterns is useful, and knowing when not to use them is the next step.

## 412: You must change a feature in a legacy Express app with no tests and global state everywhere. Where do you start?

1. Find the exact code paths for the feature, using logs, debugging or tracing.
2. Write a few end-to-end or HTTP-level characterization tests (for example with Supertest) that record current behavior. These don't need the code to be testable inside.
3. Make the smallest dependency-breaking changes needed around the code you'll touch: pass the global DB client as a parameter, wrap `Date.now()`, extract the logic out of the route handler.
4. Add unit tests for the extracted logic.
5. Make your feature change, with tests.

Don't try to fix the whole app. Leave the part you touched cleaner and tested.

## 413: Validation rules are duplicated between the React front-end and the Node back-end and keep drifting apart. How do you fix it?

Define the rules once in a shared schema and use it on both sides. In a monorepo or shared package:

```ts
// packages/contracts/signup.ts
export const SignupSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});
export type SignupInput = z.infer<typeof SignupSchema>;
```

The front-end uses it for form validation (React Hook Form has a Zod resolver), and the back-end uses it to parse requests. The back-end must still validate, since clients can't be trusted. Keep only rules both sides need in the shared schema; server-only checks (like "email already taken") stay on the server.

## 414: Should business logic live in the database (stored procedures, triggers) or in the application?

It depends, but for most web apps, keep business logic in the application:

- Easier to test, version, review and debug with normal tools.
- Easier to read for the whole team, not just database specialists.
- Easier to change and deploy.

The database is still the right place for data integrity rules it can enforce well: foreign keys, unique constraints, `NOT NULL`, check constraints. These act as a last line of defense even when application code has bugs. Heavy data processing over large sets can also be faster in SQL. Avoid triggers with hidden business logic, since they're side effects no one sees in the application code.

## 415: The users module imports from the orders module and orders imports from users. How do you break the cycle?

First, find out why each side needs the other. Common fixes:

- **Move the shared piece**: if both need a `UserSummary` type, move it to a small shared module.
- **Invert one dependency**: orders needs "get customer name", so orders defines a `CustomerDirectory` interface and users implements it (DIP).
- **Use events**: users needs to react when an order is placed, so orders emits `OrderPlaced` and users subscribes, without orders knowing about users.
- **Merge**: if the two are so tangled that every change touches both, they may really be one module.

Then add `import/no-cycle` or a `dependency-cruiser` rule so the cycle doesn't come back.

## 416: A shared "common" library is used by 20 services and every change needs coordinated releases. What do you do?

The library violates CCP and CRP: it bundles unrelated things that change for different reasons, and every service depends on all of it.

- Split it by reason to change: logging, HTTP helpers, auth, domain types, each as its own package with its own version.
- Move business logic out of it and back into the services that own it, even if that means some duplication.
- Keep what remains small, stable and backward compatible, with semantic versioning so services can upgrade on their own schedule.
- Prefer contracts (API schemas, event schemas) over shared code between services.

## 417: How would you refactor a function like exportData(format, compress, encrypt, upload)?

The flags mix four separate concerns in one function, and the combinations grow fast. Split it into a pipeline of small steps:

```ts
const formatters = { csv: toCsv, json: toJson } satisfies Record<
  string,
  (rows: Row[]) => Buffer
>;

async function exportData(
  rows: Row[],
  format: keyof typeof formatters,
  steps: Array<(data: Buffer) => Promise<Buffer>>,
) {
  let data = formatters[format](rows);
  for (const step of steps) data = await step(data);
  return data;
}

const file = await exportData(rows, "csv", [gzip, encryptWith(key)]);
await uploadToS3(file, path);
```

Each step does one thing and can be tested alone. Uploading is a separate action, since it's I/O and not a transformation (CQS). Adding a new step or format doesn't change existing code.

## 418: You need to replace a third-party analytics SDK that is called directly in 200 places. How do you do it?

1. Create your own small `Analytics` interface based on how the app actually uses the SDK.
2. Write an adapter for the current SDK that implements it.
3. Replace the 200 direct calls with your interface, using a codemod or careful search-and-replace, in small commits. Nothing changes in behavior yet.
4. Write an adapter for the new SDK.
5. Switch the composition root to the new adapter (maybe behind a feature flag, or send to both for a while to compare).
6. Remove the old SDK and its adapter.

This is Branch by Abstraction. Next time a vendor changes, it's a one-file job.

## 419: A single React context holds the user, theme, cart and feature flags, and the app re-renders too much. How do you fix it?

One big context breaks SRP and causes every consumer to re-render when any value changes.

- Split it into separate contexts by concern and change rate: `UserContext`, `ThemeContext`, `CartContext`, `FeatureFlagsContext`.
- Memoize provider values (`useMemo`) so they don't change on every render. (With the React Compiler, much of this memoization happens automatically.)
- Move fast-changing state like the cart to a store with selectors (Zustand, Redux) so components subscribe only to the parts they use.
- Keep server data in a data-fetching library rather than in context.

Profile with React DevTools before and after to confirm the improvement.

## 420: A function returns a string, a number, null or an array depending on its input. How do you clean it up?

A function with many return types forces every caller to check what it got, and the type tells them little. It's usually several functions merged into one.

- Split it into separate functions, each with one return type.
- If the result really can be different kinds of things, return a discriminated union so callers can handle each case with type narrowing.
- Replace `null` with a clear "not found" variant, an empty array, or an error, depending on what it means.

## 421: Error handling is inconsistent across the codebase. How do you bring it under control?

1. Write down the strategy: which errors are thrown, which are returned as results, what custom error classes exist, and where errors are caught and logged.
2. Create a small set of shared error classes (`NotFoundError`, `ValidationError`, `ConflictError`, `UnauthorizedError`).
3. Add one central error handler per entry point (HTTP middleware, job runner, React error boundary) that maps errors to responses and logs them once.
4. Turn on lint rules like `no-floating-promises`, `only-throw-error` and a rule against empty catch blocks.
5. Fix old code as you touch it, starting with the riskiest paths (payments, auth).

## 422: The unit test suite takes 20 minutes because every test hits a real database. How do you speed it up while keeping confidence?

- Separate the business logic from data access (repositories, functional core). Test the logic with in-memory fakes; those tests run in milliseconds.
- Keep real-database tests for repositories and a few critical flows, and run them in a separate, smaller integration suite.
- For the integration tests: reuse one database container, run each test in a transaction that's rolled back, and run test files in parallel with separate schemas.
- Run contract tests so the fakes behave like the real repositories.

This shift usually improves the design too, because it forces a clear boundary between logic and I/O.

## 423: In a live coding interview, you're asked to refactor a messy function. How do you approach it?

1. Read it and explain what it does out loud. Ask about anything unclear.
2. Check for tests. If there are none, write a few quick ones first, or at least say that you would.
3. Start with safe, small steps: rename unclear variables, extract explaining variables, add guard clauses to reduce nesting.
4. Extract functions for each separate responsibility.
5. Look for duplication and magic values.
6. Run the tests after each step, and explain why you're making each change.
7. Stop when it's clearly better, and mention what you'd do next with more time.

Interviewers care more about your process and reasoning than about reaching a perfect result.

## 424: Should shared HTTP behavior (auth headers, retries, logging) be done with inheritance or composition?

Composition. A `BaseApiClient` that every client extends quickly becomes a fragile base class, and you can't easily mix behaviors (retries without logging, say).

Instead, compose small wrappers around a single fetch function:

```ts
type Fetcher = (input: Request) => Promise<Response>;

const withAuth =
  (getToken: () => string) =>
  (next: Fetcher): Fetcher =>
  (req) => {
    req.headers.set("Authorization", `Bearer ${getToken()}`);
    return next(req);
  };

const withLogging =
  (next: Fetcher): Fetcher =>
  async (req) => {
    const res = await next(req);
    logger.info({ url: req.url, status: res.status });
    return res;
  };

const http = withLogging(withAuth(getToken)(fetch));
```

This is the middleware or interceptor style that libraries like `ky` and Axios interceptors also use.

## 425: A team uses classes with only static methods for everything. What's the problem?

A class with only static methods is just a module with extra syntax. In TypeScript, a plain module with exported functions does the same job more simply.

The bigger issue is that static calls are hard-wired dependencies. `OrderService.place()` calling `PaymentUtils.charge()` statically can't be given a fake payment in tests without module mocking, and you can't swap implementations. Static methods are fine for pure helpers with no dependencies (like `Money.of(10)` factories). For anything with I/O or that might need to vary, use instances passed in through constructors.

## 426: How would you migrate a large codebase that uses any everywhere to strict TypeScript?

- Turn on strict options one at a time, and use `// @ts-expect-error` or per-folder configs to allow existing errors while blocking new ones.
- Add `@typescript-eslint/no-explicit-any` and the `no-unsafe-*` rules as warnings first, and as errors for new or changed files.
- Type the boundaries first: API responses (with schemas), function signatures of core modules, shared types. Types spread inward from there.
- Prefer `unknown` plus narrowing to `any` when the type is truly not known.
- Track the count of `any` uses over time, and celebrate it going down.

Typing the most-changed and most-used files first gives the most value quickly.

## 427: A front-end codebase has a deep BaseComponent > FormComponent > ValidatedFormComponent hierarchy. How do you get out of it?

Deep UI hierarchies make each component depend on several layers of parent behavior, and a change at the top can break everything.

- Identify what each layer provides (lifecycle helpers, form state, validation).
- Recreate each capability as a hook, utility or wrapper component that can be used alone.
- Migrate components one at a time to use those directly, instead of extending.
- When a layer has no subclasses left, delete it.

New code should never extend the old bases. Add a lint rule or review checklist item for that while migrating.

## 428: How would you design a plugin system for a web application?

- Define a small, stable plugin interface with explicit hooks the core calls:

```ts
interface Plugin {
  name: string;
  setup(api: PluginApi): void | Promise<void>;
}

interface PluginApi {
  onOrderPlaced(handler: (order: Order) => Promise<void>): void;
  addMenuItem(item: MenuItem): void;
  registerExporter(format: string, exporter: Exporter): void;
}
```

- The core only knows the interface; plugins never import core internals. Expose only what plugins need (ISP).
- Isolate failures: one failing plugin shouldn't crash the app. Catch and log errors per plugin.
- Version the plugin API and keep it backward compatible.

This is OCP at the application level, the same way Vite, ESLint and Fastify plugins work.

## 429: Different tenants need slightly different behavior, and the code is full of if (tenant === "acme"). How do you clean it up?

Tenant checks spread through the code are shotgun surgery waiting to happen.

- Turn the differences into configuration where possible: feature flags, limits and settings stored per tenant.
- For behavior differences, define interfaces at the points that vary (pricing, invoice format, approval flow) and select an implementation per tenant once, at the start of the request.
- Pass the chosen strategies into the code (DIP), so business logic never checks tenant names.

Also push back on new one-off customizations. Each one adds a branch the team maintains forever.

## 430: Your app talks to a REST API, and you need to migrate to a GraphQL API gradually. How do you structure it?

Hide data access behind interfaces owned by the app, shaped around what the features need, not around REST or GraphQL:

```ts
interface ProductCatalog {
  getProduct(id: string): Promise<Product>;
  search(query: string): Promise<Product[]>;
}
```

Implement `RestProductCatalog` first (wrapping existing code), move all components and hooks to use the interface, then add `GraphqlProductCatalog`. Switch per feature or with a flag, and remove the REST version when done. The UI never knows which protocol it's using.

## 431: How do you handle resource cleanup (listeners, timers, connections) cleanly?

Leaked event listeners, intervals and open connections are common bugs, especially in long-running Node.js processes and single-page apps.

- Pair every setup with its cleanup in the same place: return a cleanup function from React effects, use `AbortController` to remove many listeners at once.
- Use `try`/`finally` to release resources even when errors happen.
- In TypeScript 5.2+, `using` declarations call `[Symbol.dispose]()` automatically when the variable goes out of scope (and `await using` for async cleanup), where the runtime supports it.

```ts
const controller = new AbortController();
window.addEventListener("resize", onResize, { signal: controller.signal });
window.addEventListener("scroll", onScroll, { signal: controller.signal });
// later
controller.abort(); // removes both listeners
```

## 432: How does explicit resource management with using work?

`using` is a newer JavaScript feature (supported by TypeScript since 5.2) for automatic cleanup. An object that has a `[Symbol.dispose]()` method is disposed when the block it was declared in ends, even if an error is thrown.

```ts
function openTempFile(path: string) {
  const handle = fs.openSync(path, "w");
  return {
    handle,
    [Symbol.dispose]() {
      fs.closeSync(handle);
      fs.rmSync(path);
    },
  };
}

function writeReport() {
  using file = openTempFile("/tmp/report.txt");
  fs.writeSync(file.handle, "data");
} // file is closed and deleted here
```

For async cleanup, use `[Symbol.asyncDispose]` with `await using`. It replaces many `try`/`finally` blocks and makes it hard to forget cleanup. Check runtime support (or polyfill `Symbol.dispose`) before relying on it.

## 433: Logging is scattered and sometimes includes passwords and tokens. How do you fix it?

- Replace scattered `console.log` calls with one logger (like Pino) configured in one place.
- Use the logger's redaction feature for sensitive field paths (`password`, `authorization`, `token`, `cardNumber`).
- Log structured objects with explicit fields instead of dumping whole request bodies or user objects.
- Add a request ID to every log line through middleware or `AsyncLocalStorage`, so you don't need to pass it around manually.
- Add a lint rule (`no-console`) for application code, and review logging in pull requests.

## 434: Date handling code is spread all over the app with manual timezone math. What would you do?

- Centralize date logic in one module with clear functions (`startOfBusinessDay`, `formatForUser`, `addBusinessDays`).
- Store and send timestamps in UTC (ISO 8601 strings), and convert to the user's timezone only for display.
- Use a solid library instead of hand-written math: the new built-in `Temporal` API where available (it's shipping in modern browsers and runtimes, with polyfills for the rest), or `date-fns` with `@date-fns/tz`.
- Inject a clock (`now()`) so date logic is testable.
- Add tests for daylight saving changes and month ends, which are where hand-written date code usually breaks.

## 435: Code was made very DRY across three teams' features, and now every change needs all three teams to agree. What happened, and how do you fix it?

The shared abstraction merged code that looked the same but belonged to different teams with different reasons to change. DRY was applied to code, not to knowledge, and the result is coupling across team boundaries.

Fix it by un-sharing: copy the shared code into each team's module, let each team simplify its copy to what it actually needs, and delete the shared version. Keep only truly generic, stable parts shared. This feels like going backwards, but it removes the coordination cost, which is usually much more expensive than a little duplication.

## 436: When would you choose a state machine for UI or business logic?

When a flow has several states with rules about which transitions are allowed: checkout steps, upload progress, a subscription lifecycle, multi-step forms, connection handling.

Booleans and ad-hoc `if`s let impossible combinations happen (submitting while already submitted, retrying after success). A state machine makes states and transitions explicit:

```ts
type UploadState =
  | { status: "idle" }
  | { status: "uploading"; progress: number }
  | { status: "done"; url: string }
  | { status: "failed"; error: string };

type UploadEvent =
  | { type: "START" }
  | { type: "PROGRESS"; progress: number }
  | { type: "SUCCESS"; url: string }
  | { type: "FAIL"; error: string };

function next(state: UploadState, event: UploadEvent): UploadState {
  switch (state.status) {
    case "idle":
      return event.type === "START"
        ? { status: "uploading", progress: 0 }
        : state;
    case "uploading":
      if (event.type === "PROGRESS")
        return { status: "uploading", progress: event.progress };
      if (event.type === "SUCCESS") return { status: "done", url: event.url };
      if (event.type === "FAIL")
        return { status: "failed", error: event.error };
      return state;
    default:
      return state;
  }
}
```

For complex machines, libraries like XState add visualization and features such as nested and parallel states.

## 437: What is the State pattern and how does it differ from a reducer-style state machine?

The State pattern (from the Gang of Four) gives each state its own class with the same interface. The object delegates behavior to its current state object, and states decide the next state.

```ts
interface OrderState {
  pay(order: Order): void;
  ship(order: Order): void;
}

class PendingState implements OrderState {
  pay(order: Order) {
    order.setState(new PaidState());
  }
  ship() {
    throw new Error("Cannot ship an unpaid order");
  }
}
```

A reducer-style machine keeps states as data and puts all transitions in one function. In TypeScript and React code, the data-plus-reducer style is more common: it's easier to serialize, test and visualize. The class-based State pattern fits when each state has a lot of distinct behavior.

## 438: How does the Command pattern help with features like undo or job queues?

The Command pattern turns an action into an object with everything needed to run it. Because it's data, you can store it, queue it, log it, retry it, or undo it.

```ts
interface Command {
  execute(): void;
  undo(): void;
}

class History {
  private done: Command[] = [];

  run(command: Command) {
    command.execute();
    this.done.push(command);
  }

  undo() {
    this.done.pop()?.undo();
  }
}
```

The editor doesn't need to know what each command does (OCP). The same idea is behind Redux actions and job payloads sent to a queue.

## 439: What is CQRS, and how is it related to Command-Query Separation?

CQS (Bertrand Meyer) is a rule for methods: a method either changes state or returns data, not both.

CQRS (Command Query Responsibility Segregation, Greg Young) applies the same idea at the architecture level: use separate models for writes (commands, with business rules and validation) and reads (queries, often optimized views or denormalized tables).

CQRS helps when reads and writes have very different needs, like complex domain rules on writes and fast, varied dashboards on reads. For simple CRUD it adds complexity without much benefit. It's often confused with event sourcing, but you can use CQRS without it.

## 440: When is event sourcing overkill?

Event sourcing stores every change as an event and rebuilds the current state by replaying them. It gives a full history and audit log, and makes some features (like time travel or rebuilding projections) easy.

It's overkill when:

- You don't need history beyond basic audit fields.
- The domain is mostly CRUD.
- The team has no experience with eventual consistency, event versioning and rebuilding projections.

The cost is high: events are a permanent contract that must be versioned, queries need separate projections, and debugging is harder. An audit table or change log usually covers the real need.

## 441: How do you know when to stop refactoring?

Stop when:

- The change you came to make is now easy and done.
- Further changes would be based on guesses about future needs.
- You're making the code different, not clearly better (moving between two equally good designs).
- The area isn't changed often enough to repay more effort.
- The pull request is getting too big to review well.

Write down remaining ideas as follow-ups, especially in code you'll touch again soon. Refactoring is a means to faster, safer changes, not a goal on its own.

## 442: How do you measure if a refactoring was successful?

Look at results, not just how the code looks:

- Changes in that area take less time, and pull requests touching it are smaller.
- Fewer bugs and incidents come from it.
- New team members can work in it sooner.
- Tests are faster and less flaky.
- Metrics like complexity, file size or coupling went down in the hotspot you targeted.

Compare a few months before and after when possible. If nobody can name a real improvement, it's a sign to focus future refactoring on code that changes more often.

## 443: How do you make a codebase easy for new developers to understand?

- A README that explains how to run, test and deploy in a few commands.
- A short architecture overview: main modules, how data flows, key decisions (ADRs).
- Consistent structure and naming, so learning one feature teaches you the others.
- Folder names that describe the business (screaming architecture).
- Good tests that show how modules are used.
- Clear entry points and a composition root where wiring happens.
- Automated setup (scripts, dev containers) so nobody spends days configuring.

A good check: ask each new hire what confused them in their first two weeks, and fix those things.

## 444: How do you balance simplicity and flexibility in a design?

Simplicity should be the default. Flexibility has a cost: more code, more indirection, more concepts to learn, and you pay that cost even if the flexibility is never used.

Add flexibility when you have evidence of change: a second real use case, a history of changes in that area, or a boundary with an external system you don't control. Make it easy to add flexibility later by keeping code well-tested and modules small, so refactoring is cheap. Cheap refactoring is what lets you choose simplicity with confidence.

## 445: How do you design for testability without over-abstracting?

- Push I/O to the edges and keep logic pure. Pure functions need no abstraction to be testable.
- Add interfaces only at real boundaries: database, external APIs, clock, randomness, file system.
- Use constructor or parameter injection for those boundaries, with default values for production if it helps.
- Use real collaborators for internal code instead of mocking everything.
- For external HTTP, consider network-level fakes (like MSW or a test server) instead of wrapping every client.

If you're adding an interface only so a mock can be passed in, and there will never be a second implementation, reconsider.

## 446: What would you put in a team's definition of "clean enough" for a pull request?

- Formatted, linted and type-checked with no new warnings.
- Names that a teammate understands without asking.
- No dead code, commented-out code or debug logs.
- Tests for new behavior and bug fixes, focused on behavior.
- Errors handled or deliberately passed up, never swallowed.
- No new duplication of business rules.
- Public functions and non-obvious decisions documented.
- The pull request is small and focused, and refactors are separate from behavior changes.

Keep the list short enough that people actually use it.

## 447: How would you explain SOLID to a non-technical stakeholder?

- **SRP**: each part of the system has one job, so changing billing doesn't break the signup page.
- **OCP**: we can add new things, like a new payment method, by adding a piece instead of rewiring existing ones.
- **LSP**: replacement parts must really fit, like a spare tire that works on the car.
- **ISP**: each part only connects to what it needs, so unrelated changes don't affect it.
- **DIP**: our core business rules don't depend on specific vendors, so switching vendors is cheaper.

The business result is faster, safer changes and lower cost to switch suppliers.

## 448: What are common mistakes when applying SOLID?

- Creating an interface for every class, even with one implementation and no boundary to protect.
- Splitting classes so finely that simple flows are spread across many files (SRP overdone).
- Building plugin systems and extension points nobody asked for (OCP overdone).
- Using inheritance for code reuse and then fighting LSP problems.
- Confusing DI frameworks with DIP and injecting concrete classes everywhere.
- Treating the principles as rules to apply up front instead of tools to fix real problems when change hurts.

## 449: How do clean code principles change between a startup prototype and a mature product?

In an early prototype, speed of learning matters most. It's reasonable to skip some tests, keep things in fewer files and accept duplication, because a lot of the code will be thrown away.

As the product finds users and the team grows, the balance shifts: code lives longer, more people read it, and bugs cost more. That's when to invest in tests, module boundaries, consistent conventions and refactoring. The mistake is either over-engineering the prototype or never switching modes once the code becomes the real product. Basic habits like clear names and small functions cost almost nothing and are worth keeping at every stage.

## 450: What is your overall approach to writing clean code day to day?

A good answer is personal, but usually covers:

- Make it work, make it right, then (only if needed) make it fast.
- Pick clear names, and rename as soon as a better one comes to mind.
- Keep functions and modules focused, and keep business logic away from I/O and frameworks.
- Write tests for behavior, and refactor in small steps with tests running.
- Prefer simple code and composition; add abstractions when real needs show up.
- Let tools handle formatting and mechanical checks, and use reviews for design.
- Leave each file a little better than you found it.
- Treat principles like SOLID, DRY and YAGNI as guides for judgment, not rules to follow blindly.
