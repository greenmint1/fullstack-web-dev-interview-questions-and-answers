# Python Interview Questions and Answers

_Last updated: November 25, 2026_

This file has 450 Python interview questions and answers: 150 easy, 150 moderate and 150 advanced. The answers target Python 3.14 and 3.15 (released October 2026) and point out when a feature needs a recent version. Code examples are plain CPython with the standard library unless a package is named.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is Python?](#1-what-is-python)
- [2: What is the difference between Python and CPython?](#2-what-is-the-difference-between-python-and-cpython)
- [3: Is Python compiled or interpreted?](#3-is-python-compiled-or-interpreted)
- [4: What does dynamically typed mean?](#4-what-does-dynamically-typed-mean)
- [5: How do you check the Python version?](#5-how-do-you-check-the-python-version)
- [6: Why does indentation matter in Python?](#6-why-does-indentation-matter-in-python)
- [7: What are the built-in data types in Python?](#7-what-are-the-built-in-data-types-in-python)
- [8: What is the difference between a list and a tuple?](#8-what-is-the-difference-between-a-list-and-a-tuple)
- [9: What is a dictionary?](#9-what-is-a-dictionary)
- [10: What is a set?](#10-what-is-a-set)
- [11: How do you create an empty set?](#11-how-do-you-create-an-empty-set)
- [12: What is None?](#12-what-is-none)
- [13: What is the difference between == and is?](#13-what-is-the-difference-between--and-is)
- [14: What are mutable and immutable objects?](#14-what-are-mutable-and-immutable-objects)
- [15: How do you write a comment in Python?](#15-how-do-you-write-a-comment-in-python)
- [16: What is a docstring?](#16-what-is-a-docstring)
- [17: How do you define a function?](#17-how-do-you-define-a-function)
- [18: What are default arguments?](#18-what-are-default-arguments)
- [19: What are args and kwargs (the star and double star parameters)?](#19-what-are-args-and-kwargs-the-star-and-double-star-parameters)
- [20: What is the difference between positional and keyword arguments?](#20-what-is-the-difference-between-positional-and-keyword-arguments)
- [21: What is a lambda function?](#21-what-is-a-lambda-function)
- [22: What is a list comprehension?](#22-what-is-a-list-comprehension)
- [23: What are dict and set comprehensions?](#23-what-are-dict-and-set-comprehensions)
- [24: How do you write an if statement?](#24-how-do-you-write-an-if-statement)
- [25: What is the ternary (conditional) expression in Python?](#25-what-is-the-ternary-conditional-expression-in-python)
- [26: How does a for loop work in Python?](#26-how-does-a-for-loop-work-in-python)
- [27: What does range() do?](#27-what-does-range-do)
- [28: What is a while loop?](#28-what-is-a-while-loop)
- [29: What do break, continue and pass do?](#29-what-do-break-continue-and-pass-do)
- [30: What is the else clause on a loop?](#30-what-is-the-else-clause-on-a-loop)
- [31: How do you use enumerate()?](#31-how-do-you-use-enumerate)
- [32: What does zip() do?](#32-what-does-zip-do)
- [33: What is string slicing?](#33-what-is-string-slicing)
- [34: How do you get the length of a list or string?](#34-how-do-you-get-the-length-of-a-list-or-string)
- [35: What are f-strings?](#35-what-are-f-strings)
- [36: What are some common string methods?](#36-what-are-some-common-string-methods)
- [37: How do you join a list of strings?](#37-how-do-you-join-a-list-of-strings)
- [38: Are strings mutable in Python?](#38-are-strings-mutable-in-python)
- [39: How do you convert between types?](#39-how-do-you-convert-between-types)
- [40: What values are falsy in Python?](#40-what-values-are-falsy-in-python)
- [41: What are the logical operators in Python?](#41-what-are-the-logical-operators-in-python)
- [42: What is the difference between / and //?](#42-what-is-the-difference-between--and-)
- [43: How do you raise a number to a power?](#43-how-do-you-raise-a-number-to-a-power)
- [44: How big can integers get in Python?](#44-how-big-can-integers-get-in-python)
- [45: Why does 0.1 + 0.2 not equal 0.3?](#45-why-does-01--02-not-equal-03)
- [46: How do you get user input?](#46-how-do-you-get-user-input)
- [47: How do you print without a newline?](#47-how-do-you-print-without-a-newline)
- [48: What is a module?](#48-what-is-a-module)
- [49: What is a package?](#49-what-is-a-package)
- [50: What are the different ways to import?](#50-what-are-the-different-ways-to-import)
- [51: What does the if name == "main" check do?](#51-what-does-the-if-name--main-check-do)
- [52: What is pip?](#52-what-is-pip)
- [53: What is a virtual environment?](#53-what-is-a-virtual-environment)
- [54: What is requirements.txt?](#54-what-is-requirementstxt)
- [55: What is PEP 8?](#55-what-is-pep-8)
- [56: What is a PEP?](#56-what-is-a-pep)
- [57: How do you handle exceptions?](#57-how-do-you-handle-exceptions)
- [58: How do you raise an exception?](#58-how-do-you-raise-an-exception)
- [59: How do you catch more than one exception type?](#59-how-do-you-catch-more-than-one-exception-type)
- [60: How do you create a custom exception?](#60-how-do-you-create-a-custom-exception)
- [61: What are some common built-in exceptions?](#61-what-are-some-common-built-in-exceptions)
- [62: Why should you avoid a bare except?](#62-why-should-you-avoid-a-bare-except)
- [63: How do you read a file?](#63-how-do-you-read-a-file)
- [64: How do you write to a file?](#64-how-do-you-write-to-a-file)
- [65: What is the with statement?](#65-what-is-the-with-statement)
- [66: What is pathlib?](#66-what-is-pathlib)
- [67: How do you work with JSON in Python?](#67-how-do-you-work-with-json-in-python)
- [68: What is a class?](#68-what-is-a-class)
- [69: What is the init method?](#69-what-is-the-init-method)
- [70: What is self?](#70-what-is-self)
- [71: What is the difference between class attributes and instance attributes?](#71-what-is-the-difference-between-class-attributes-and-instance-attributes)
- [72: What is inheritance?](#72-what-is-inheritance)
- [73: What does super() do?](#73-what-does-super-do)
- [74: What is method overriding?](#74-what-is-method-overriding)
- [75: Does Python support method overloading?](#75-does-python-support-method-overloading)
- [76: What is encapsulation in Python?](#76-what-is-encapsulation-in-python)
- [77: What are instance methods, class methods and static methods?](#77-what-are-instance-methods-class-methods-and-static-methods)
- [78: What is the str method used for?](#78-what-is-the-str-method-used-for)
- [79: What is a dataclass?](#79-what-is-a-dataclass)
- [80: What are type hints?](#80-what-are-type-hints)
- [81: How do you write an optional type?](#81-how-do-you-write-an-optional-type)
- [82: What is the global keyword?](#82-what-is-the-global-keyword)
- [83: What is the nonlocal keyword?](#83-what-is-the-nonlocal-keyword)
- [84: What is scope in Python (the LEGB rule)?](#84-what-is-scope-in-python-the-legb-rule)
- [85: How do you copy a list?](#85-how-do-you-copy-a-list)
- [86: What is the difference between a shallow copy and a deep copy?](#86-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy)
- [87: How do you sort a list?](#87-how-do-you-sort-a-list)
- [88: What are the main list methods?](#88-what-are-the-main-list-methods)
- [89: How do you safely get a value from a dict?](#89-how-do-you-safely-get-a-value-from-a-dict)
- [90: How do you loop over a dictionary?](#90-how-do-you-loop-over-a-dictionary)
- [91: How do you merge two dictionaries?](#91-how-do-you-merge-two-dictionaries)
- [92: What are the set operations?](#92-what-are-the-set-operations)
- [93: What is tuple unpacking?](#93-what-is-tuple-unpacking)
- [94: What is the in operator?](#94-what-is-the-in-operator)
- [95: What are any() and all()?](#95-what-are-any-and-all)
- [96: What do map() and filter() do?](#96-what-do-map-and-filter-do)
- [97: What are min(), max() and sum()?](#97-what-are-min-max-and-sum)
- [98: What is the difference between a function and a method?](#98-what-is-the-difference-between-a-function-and-a-method)
- [99: What is an iterable?](#99-what-is-an-iterable)
- [100: What is an iterator?](#100-what-is-an-iterator)
- [101: What is a generator?](#101-what-is-a-generator)
- [102: What is a generator expression?](#102-what-is-a-generator-expression)
- [103: What is the difference between return and yield?](#103-what-is-the-difference-between-return-and-yield)
- [104: What is a decorator?](#104-what-is-a-decorator)
- [105: What does the del statement do?](#105-what-does-the-del-statement-do)
- [106: How do you check the type of an object?](#106-how-do-you-check-the-type-of-an-object)
- [107: What are keywords in Python?](#107-what-are-keywords-in-python)
- [108: What is the walrus operator?](#108-what-is-the-walrus-operator)
- [109: What is the match statement?](#109-what-is-the-match-statement)
- [110: How do you get the current date and time?](#110-how-do-you-get-the-current-date-and-time)
- [111: How do you generate random numbers?](#111-how-do-you-generate-random-numbers)
- [112: What is the math module?](#112-what-is-the-math-module)
- [113: What is the os module used for?](#113-what-is-the-os-module-used-for)
- [114: What is the sys module used for?](#114-what-is-the-sys-module-used-for)
- [115: How do you read command-line arguments?](#115-how-do-you-read-command-line-arguments)
- [116: What is the difference between append() and extend()?](#116-what-is-the-difference-between-append-and-extend)
- [117: What is the difference between remove(), pop() and del on a list?](#117-what-is-the-difference-between-remove-pop-and-del-on-a-list)
- [118: How do you reverse a list?](#118-how-do-you-reverse-a-list)
- [119: How do you remove duplicates from a list?](#119-how-do-you-remove-duplicates-from-a-list)
- [120: How do you count items in a list?](#120-how-do-you-count-items-in-a-list)
- [121: What is a nested function?](#121-what-is-a-nested-function)
- [122: What is a closure?](#122-what-is-a-closure)
- [123: Are functions objects in Python?](#123-are-functions-objects-in-python)
- [124: What is recursion?](#124-what-is-recursion)
- [125: What is the difference between a script and a module?](#125-what-is-the-difference-between-a-script-and-a-module)
- [126: How do you run a module as a script?](#126-how-do-you-run-a-module-as-a-script)
- [127: What is the REPL?](#127-what-is-the-repl)
- [128: What do dir() and help() do?](#128-what-do-dir-and-help-do)
- [129: What is the id() function?](#129-what-is-the-id-function)
- [130: What are bytes and how are they different from str?](#130-what-are-bytes-and-how-are-they-different-from-str)
- [131: What are raw strings?](#131-what-are-raw-strings)
- [132: How do you write a multiline string?](#132-how-do-you-write-a-multiline-string)
- [133: How do you check if a string contains only digits?](#133-how-do-you-check-if-a-string-contains-only-digits)
- [134: What is the difference between find() and index() on strings?](#134-what-is-the-difference-between-find-and-index-on-strings)
- [135: How do you check if a key exists in a dictionary?](#135-how-do-you-check-if-a-key-exists-in-a-dictionary)
- [136: What is the difference between a list and an array?](#136-what-is-the-difference-between-a-list-and-an-array)
- [137: How do you flatten a list of lists?](#137-how-do-you-flatten-a-list-of-lists)
- [138: What is the round() function?](#138-what-is-the-round-function)
- [139: What is the abs() function?](#139-what-is-the-abs-function)
- [140: What is the difference between break and return?](#140-what-is-the-difference-between-break-and-return)
- [141: What is chained comparison?](#141-what-is-chained-comparison)
- [142: What is the difference between a statement and an expression?](#142-what-is-the-difference-between-a-statement-and-an-expression)
- [143: What is an assert statement?](#143-what-is-an-assert-statement)
- [144: What is the pass statement used for?](#144-what-is-the-pass-statement-used-for)
- [145: How do you format numbers in f-strings?](#145-how-do-you-format-numbers-in-f-strings)
- [146: What is an f-string debug specifier?](#146-what-is-an-f-string-debug-specifier)
- [147: How do you comment out a block of code quickly?](#147-how-do-you-comment-out-a-block-of-code-quickly)
- [148: What are the naming rules for variables?](#148-what-are-the-naming-rules-for-variables)
- [149: What is the Zen of Python?](#149-what-is-the-zen-of-python)
- [150: What is the difference between Python 2 and Python 3?](#150-what-is-the-difference-between-python-2-and-python-3)

### Moderate Questions (151-300)

- [151: Why is a mutable default argument a bug?](#151-why-is-a-mutable-default-argument-a-bug)
- [152: What is the late binding problem with closures in loops?](#152-what-is-the-late-binding-problem-with-closures-in-loops)
- [153: What are keyword-only and positional-only parameters?](#153-what-are-keyword-only-and-positional-only-parameters)
- [154: How do you unpack arguments when calling a function?](#154-how-do-you-unpack-arguments-when-calling-a-function)
- [155: What is collections.defaultdict?](#155-what-is-collectionsdefaultdict)
- [156: What is collections.deque and when do you use it?](#156-what-is-collectionsdeque-and-when-do-you-use-it)
- [157: What is a namedtuple and how does it compare to a dataclass?](#157-what-is-a-namedtuple-and-how-does-it-compare-to-a-dataclass)
- [158: What is a ChainMap?](#158-what-is-a-chainmap)
- [159: What does functools.lru_cache do?](#159-what-does-functoolslru_cache-do)
- [160: What is functools.partial?](#160-what-is-functoolspartial)
- [161: What does functools.reduce do?](#161-what-does-functoolsreduce-do)
- [162: Why should you use functools.wraps in decorators?](#162-why-should-you-use-functoolswraps-in-decorators)
- [163: How do you write a decorator that takes arguments?](#163-how-do-you-write-a-decorator-that-takes-arguments)
- [164: What is a class decorator?](#164-what-is-a-class-decorator)
- [165: What is a property?](#165-what-is-a-property)
- [166: What is functools.cached_property?](#166-what-is-functoolscached_property)
- [167: What are dunder (magic) methods?](#167-what-are-dunder-magic-methods)
- [168: How do you make a class support the + operator?](#168-how-do-you-make-a-class-support-the--operator)
- [169: How do you make objects comparable and sortable?](#169-how-do-you-make-objects-comparable-and-sortable)
- [170: Why does defining eq make a class unhashable?](#170-why-does-defining-eq-make-a-class-unhashable)
- [171: How do you make a class iterable?](#171-how-do-you-make-a-class-iterable)
- [172: How do you make a class work with len() and indexing?](#172-how-do-you-make-a-class-work-with-len-and-indexing)
- [173: What does the call method do?](#173-what-does-the-call-method-do)
- [174: How do you write a context manager with a class?](#174-how-do-you-write-a-context-manager-with-a-class)
- [175: How do you write a context manager with contextlib?](#175-how-do-you-write-a-context-manager-with-contextlib)
- [176: What other contextlib helpers are useful?](#176-what-other-contextlib-helpers-are-useful)
- [177: What is an abstract base class?](#177-what-is-an-abstract-base-class)
- [178: What is typing.Protocol?](#178-what-is-typingprotocol)
- [179: What is duck typing?](#179-what-is-duck-typing)
- [180: What is multiple inheritance and the MRO?](#180-what-is-multiple-inheritance-and-the-mro)
- [181: What is a mixin?](#181-what-is-a-mixin)
- [182: What is composition and why is it often preferred over inheritance?](#182-what-is-composition-and-why-is-it-often-preferred-over-inheritance)
- [183: What is slots?](#183-what-is-slots)
- [184: What useful options does dataclass have?](#184-what-useful-options-does-dataclass-have)
- [185: How do you validate fields in a dataclass?](#185-how-do-you-validate-fields-in-a-dataclass)
- [186: What is Pydantic used for?](#186-what-is-pydantic-used-for)
- [187: What is an Enum?](#187-what-is-an-enum)
- [188: How do you write generic functions and classes with the new syntax?](#188-how-do-you-write-generic-functions-and-classes-with-the-new-syntax)
- [189: What is TypedDict?](#189-what-is-typeddict)
- [190: What are Literal, Final and ClassVar?](#190-what-are-literal-final-and-classvar)
- [191: How do you type hint a callable?](#191-how-do-you-type-hint-a-callable)
- [192: What is the difference between typing.List and list in type hints?](#192-what-is-the-difference-between-typinglist-and-list-in-type-hints)
- [193: What are mypy and Pyright?](#193-what-are-mypy-and-pyright)
- [194: What is Ruff?](#194-what-is-ruff)
- [195: What is pyproject.toml?](#195-what-is-pyprojecttoml)
- [196: What is uv?](#196-what-is-uv)
- [197: What is the difference between a wheel and a source distribution?](#197-what-is-the-difference-between-a-wheel-and-a-source-distribution)
- [198: What is an editable install?](#198-what-is-an-editable-install)
- [199: How does Python find modules on import?](#199-how-does-python-find-modules-on-import)
- [200: What is a circular import and how do you fix it?](#200-what-is-a-circular-import-and-how-do-you-fix-it)
- [201: What does all do in a module?](#201-what-does-all-do-in-a-module)
- [202: What is the difference between absolute and relative imports?](#202-what-is-the-difference-between-absolute-and-relative-imports)
- [203: How do you use the logging module?](#203-how-do-you-use-the-logging-module)
- [204: Why use logging instead of print?](#204-why-use-logging-instead-of-print)
- [205: Why should you pass arguments to a logger instead of using an f-string?](#205-why-should-you-pass-arguments-to-a-logger-instead-of-using-an-f-string)
- [206: How do you write tests with pytest?](#206-how-do-you-write-tests-with-pytest)
- [207: What are pytest fixtures?](#207-what-are-pytest-fixtures)
- [208: What is pytest.mark.parametrize?](#208-what-is-pytestmarkparametrize)
- [209: How do you mock things in tests?](#209-how-do-you-mock-things-in-tests)
- [210: What is the difference between Mock and MagicMock?](#210-what-is-the-difference-between-mock-and-magicmock)
- [211: What is unittest?](#211-what-is-unittest)
- [212: How do you measure test coverage?](#212-how-do-you-measure-test-coverage)
- [213: How do you debug Python code?](#213-how-do-you-debug-python-code)
- [214: How do you measure how long code takes?](#214-how-do-you-measure-how-long-code-takes)
- [215: How do you profile a Python program?](#215-how-do-you-profile-a-python-program)
- [216: What is itertools and what are its most useful functions?](#216-what-is-itertools-and-what-are-its-most-useful-functions)
- [217: How does itertools.groupby work?](#217-how-does-itertoolsgroupby-work)
- [218: How do you split a list into chunks?](#218-how-do-you-split-a-list-into-chunks)
- [219: What does yield from do?](#219-what-does-yield-from-do)
- [220: What does the send() method on a generator do?](#220-what-does-the-send-method-on-a-generator-do)
- [221: How do you write an iterator class by hand?](#221-how-do-you-write-an-iterator-class-by-hand)
- [222: What is exception chaining?](#222-what-is-exception-chaining)
- [223: What are exception groups and except*?](#223-what-are-exception-groups-and-except)
- [224: How do you add notes to an exception?](#224-how-do-you-add-notes-to-an-exception)
- [225: What is the EAFP style?](#225-what-is-the-eafp-style)
- [226: What is the warnings module?](#226-what-is-the-warnings-module)
- [227: How do you use regular expressions in Python?](#227-how-do-you-use-regular-expressions-in-python)
- [228: What is the difference between re.match, re.search and re.fullmatch?](#228-what-is-the-difference-between-rematch-research-and-refullmatch)
- [229: How do you read and write CSV files?](#229-how-do-you-read-and-write-csv-files)
- [230: How do you read a TOML file?](#230-how-do-you-read-a-toml-file)
- [231: How do you use SQLite from Python?](#231-how-do-you-use-sqlite-from-python)
- [232: How do you run a shell command from Python?](#232-how-do-you-run-a-shell-command-from-python)
- [233: How do you work with environment variables and config?](#233-how-do-you-work-with-environment-variables-and-config)
- [234: How do you handle time zones?](#234-how-do-you-handle-time-zones)
- [235: How do you parse and do math with dates?](#235-how-do-you-parse-and-do-math-with-dates)
- [236: What is the Decimal type for?](#236-what-is-the-decimal-type-for)
- [237: What is pickle and why is it risky?](#237-what-is-pickle-and-why-is-it-risky)
- [238: How do you make an object JSON serializable?](#238-how-do-you-make-an-object-json-serializable)
- [239: How do you use heapq?](#239-how-do-you-use-heapq)
- [240: What is bisect used for?](#240-what-is-bisect-used-for)
- [241: How do you sort by multiple keys?](#241-how-do-you-sort-by-multiple-keys)
- [242: What are operator.itemgetter and attrgetter?](#242-what-are-operatoritemgetter-and-attrgetter)
- [243: What are template strings (t-strings)?](#243-what-are-template-strings-t-strings)
- [244: What is the difference between threads, processes and async in Python?](#244-what-is-the-difference-between-threads-processes-and-async-in-python)
- [245: What is the GIL?](#245-what-is-the-gil)
- [246: How do you use concurrent.futures?](#246-how-do-you-use-concurrentfutures)
- [247: How do you start a thread?](#247-how-do-you-start-a-thread)
- [248: How do you share data safely between threads?](#248-how-do-you-share-data-safely-between-threads)
- [249: How do you use multiprocessing?](#249-how-do-you-use-multiprocessing)
- [250: What is async and await?](#250-what-is-async-and-await)
- [251: What is the difference between asyncio.gather and TaskGroup?](#251-what-is-the-difference-between-asynciogather-and-taskgroup)
- [252: How do you add a timeout to async code?](#252-how-do-you-add-a-timeout-to-async-code)
- [253: What happens if you call a blocking function inside async code?](#253-what-happens-if-you-call-a-blocking-function-inside-async-code)
- [254: How do you make HTTP requests in Python?](#254-how-do-you-make-http-requests-in-python)
- [255: What is the difference between WSGI and ASGI?](#255-what-is-the-difference-between-wsgi-and-asgi)
- [256: What are the main Python web frameworks?](#256-what-are-the-main-python-web-frameworks)
- [257: What does a basic FastAPI endpoint look like?](#257-what-does-a-basic-fastapi-endpoint-look-like)
- [258: What does a basic Flask app look like?](#258-what-does-a-basic-flask-app-look-like)
- [259: What is an ORM, and which ones are common in Python?](#259-what-is-an-orm-and-which-ones-are-common-in-python)
- [260: What is the N+1 query problem in an ORM?](#260-what-is-the-n1-query-problem-in-an-orm)
- [261: How do you run background jobs in a Python web app?](#261-how-do-you-run-background-jobs-in-a-python-web-app)
- [262: What are Gunicorn and Uvicorn?](#262-what-are-gunicorn-and-uvicorn)
- [263: How do you handle signals and graceful shutdown?](#263-how-do-you-handle-signals-and-graceful-shutdown)
- [264: How do you read a large file without loading it into memory?](#264-how-do-you-read-a-large-file-without-loading-it-into-memory)
- [265: How do you build a data pipeline with generators?](#265-how-do-you-build-a-data-pipeline-with-generators)
- [266: How do you use the tempfile module?](#266-how-do-you-use-the-tempfile-module)
- [267: How do you copy, move and delete files and folders?](#267-how-do-you-copy-move-and-delete-files-and-folders)
- [268: What is structural pattern matching good for beyond simple values?](#268-what-is-structural-pattern-matching-good-for-beyond-simple-values)
- [269: How do class patterns work in match?](#269-how-do-class-patterns-work-in-match)
- [270: What is the difference between match and a dict of functions?](#270-what-is-the-difference-between-match-and-a-dict-of-functions)
- [271: What are frozenset and frozendict?](#271-what-are-frozenset-and-frozendict)
- [272: How do you make a read-only dict on Python versions before 3.15?](#272-how-do-you-make-a-read-only-dict-on-python-versions-before-315)
- [273: What are lazy imports in Python 3.15?](#273-what-are-lazy-imports-in-python-315)
- [274: What is the difference between str.format, % formatting and f-strings?](#274-what-is-the-difference-between-strformat--formatting-and-f-strings)
- [275: How do you pad, align and truncate strings?](#275-how-do-you-pad-align-and-truncate-strings)
- [276: What is the difference between sorted(dict) and sorting dict items?](#276-what-is-the-difference-between-sorteddict-and-sorting-dict-items)
- [277: What is the difference between dict.setdefault and defaultdict?](#277-what-is-the-difference-between-dictsetdefault-and-defaultdict)
- [278: What is the Counter class good for?](#278-what-is-the-counter-class-good-for)
- [279: How do you compare two lists for differences?](#279-how-do-you-compare-two-lists-for-differences)
- [280: What is the difference between a shallow copy of a dict and dict(d)?](#280-what-is-the-difference-between-a-shallow-copy-of-a-dict-and-dictd)
- [281: How do you call a parent method when overriding a property?](#281-how-do-you-call-a-parent-method-when-overriding-a-property)
- [282: What is the difference between getattr, setattr and hasattr?](#282-what-is-the-difference-between-getattr-setattr-and-hasattr)
- [283: What is the getattr method on a class?](#283-what-is-the-getattr-method-on-a-class)
- [284: What is a module-level getattr?](#284-what-is-a-module-level-getattr)
- [285: What is Self in type hints?](#285-what-is-self-in-type-hints)
- [286: What is typing.overload?](#286-what-is-typingoverload)
- [287: How do you avoid runtime cost from type-only imports?](#287-how-do-you-avoid-runtime-cost-from-type-only-imports)
- [288: What changed with annotations in Python 3.14?](#288-what-changed-with-annotations-in-python-314)
- [289: What does the functools.singledispatch decorator do?](#289-what-does-the-functoolssingledispatch-decorator-do)
- [290: What is the difference between is and == for small integers and strings?](#290-what-is-the-difference-between-is-and--for-small-integers-and-strings)
- [291: How do you write a simple CLI app with subcommands?](#291-how-do-you-write-a-simple-cli-app-with-subcommands)
- [292: How do you hash passwords in Python?](#292-how-do-you-hash-passwords-in-python)
- [293: How do you compare secrets safely?](#293-how-do-you-compare-secrets-safely)
- [294: How do you parse URLs and query strings?](#294-how-do-you-parse-urls-and-query-strings)
- [295: How do you compress data in Python?](#295-how-do-you-compress-data-in-python)
- [296: What is a UUID and how do you create one?](#296-what-is-a-uuid-and-how-do-you-create-one)
- [297: How do you install a specific Python version and switch between them?](#297-how-do-you-install-a-specific-python-version-and-switch-between-them)
- [298: What is Jupyter and when is it used?](#298-what-is-jupyter-and-when-is-it-used)
- [299: What libraries are common for data work?](#299-what-libraries-are-common-for-data-work)
- [300: How do you vectorize work with NumPy instead of looping?](#300-how-do-you-vectorize-work-with-numpy-instead-of-looping)

### Advanced Questions (301-450)

- [301: How does CPython manage memory?](#301-how-does-cpython-manage-memory)
- [302: How does reference counting work and what are its limits?](#302-how-does-reference-counting-work-and-what-are-its-limits)
- [303: How does the cyclic garbage collector work?](#303-how-does-the-cyclic-garbage-collector-work)
- [304: What are immortal objects?](#304-what-are-immortal-objects)
- [305: What is the free-threaded build of Python?](#305-what-is-the-free-threaded-build-of-python)
- [306: How does the free-threaded build stay thread-safe without the GIL?](#306-how-does-the-free-threaded-build-stay-thread-safe-without-the-gil)
- [307: What are subinterpreters and how are they different from threads?](#307-what-are-subinterpreters-and-how-are-they-different-from-threads)
- [308: What is Python bytecode and how can you look at it?](#308-what-is-python-bytecode-and-how-can-you-look-at-it)
- [309: What is the specializing adaptive interpreter?](#309-what-is-the-specializing-adaptive-interpreter)
- [310: What is the CPython JIT compiler?](#310-what-is-the-cpython-jit-compiler)
- [311: What is a code object versus a function object?](#311-what-is-a-code-object-versus-a-function-object)
- [312: What is a frame object?](#312-what-is-a-frame-object)
- [313: How are closures implemented?](#313-how-are-closures-implemented)
- [314: How does attribute lookup work on an instance?](#314-how-does-attribute-lookup-work-on-an-instance)
- [315: What is a descriptor?](#315-what-is-a-descriptor)
- [316: What is the difference between data and non-data descriptors?](#316-what-is-the-difference-between-data-and-non-data-descriptors)
- [317: How do methods become bound methods?](#317-how-do-methods-become-bound-methods)
- [318: What does the set_name hook do?](#318-what-does-the-set_name-hook-do)
- [319: What is a metaclass?](#319-what-is-a-metaclass)
- [320: When should you use init_subclass instead of a metaclass?](#320-when-should-you-use-init_subclass-instead-of-a-metaclass)
- [321: What are the steps when Python executes a class statement?](#321-what-are-the-steps-when-python-executes-a-class-statement)
- [322: What is the difference between new and init?](#322-what-is-the-difference-between-new-and-init)
- [323: How does the C3 linearization (MRO) work?](#323-how-does-the-c3-linearization-mro-work)
- [324: What is cooperative multiple inheritance?](#324-what-is-cooperative-multiple-inheritance)
- [325: How does super() work without arguments?](#325-how-does-super-work-without-arguments)
- [326: How are dicts implemented in CPython?](#326-how-are-dicts-implemented-in-cpython)
- [327: Why must dict keys be hashable and what makes a good hash?](#327-why-must-dict-keys-be-hashable-and-what-makes-a-good-hash)
- [328: What is hash randomization?](#328-what-is-hash-randomization)
- [329: How are lists implemented, and what are their time complexities?](#329-how-are-lists-implemented-and-what-are-their-time-complexities)
- [330: How are strings stored in CPython?](#330-how-are-strings-stored-in-cpython)
- [331: What is string interning and when does it matter?](#331-what-is-string-interning-and-when-does-it-matter)
- [332: What sorting algorithm does Python use?](#332-what-sorting-algorithm-does-python-use)
- [333: How does sys.getsizeof differ from the real memory use of an object?](#333-how-does-sysgetsizeof-differ-from-the-real-memory-use-of-an-object)
- [334: How do you find a memory leak in a Python service?](#334-how-do-you-find-a-memory-leak-in-a-python-service)
- [335: What are weak references and when do you use them?](#335-what-are-weak-references-and-when-do-you-use-them)
- [336: Why can holding on to an exception cause a memory leak?](#336-why-can-holding-on-to-an-exception-cause-a-memory-leak)
- [337: What does the del method do and what are its pitfalls?](#337-what-does-the-del-method-do-and-what-are-its-pitfalls)
- [338: How does the import system work internally?](#338-how-does-the-import-system-work-internally)
- [339: How would you write a custom import hook?](#339-how-would-you-write-a-custom-import-hook)
- [340: What are namespace packages?](#340-what-are-namespace-packages)
- [341: What are entry points and how are they used for plugins?](#341-what-are-entry-points-and-how-are-they-used-for-plugins)
- [342: How does asyncio's event loop work?](#342-how-does-asyncios-event-loop-work)
- [343: What is the difference between a coroutine, a Task and a Future?](#343-what-is-the-difference-between-a-coroutine-a-task-and-a-future)
- [344: Why must you keep a reference to tasks created with create_task?](#344-why-must-you-keep-a-reference-to-tasks-created-with-create_task)
- [345: How does cancellation work in asyncio?](#345-how-does-cancellation-work-in-asyncio)
- [346: How do you limit concurrency in asyncio?](#346-how-do-you-limit-concurrency-in-asyncio)
- [347: What is backpressure and how do you handle it in Python?](#347-what-is-backpressure-and-how-do-you-handle-it-in-python)
- [348: What are context variables?](#348-what-are-context-variables)
- [349: How do you call async code from sync code and sync code from async code?](#349-how-do-you-call-async-code-from-sync-code-and-sync-code-from-async-code)
- [350: What is uvloop?](#350-what-is-uvloop)
- [351: How do async generators and async context managers work?](#351-how-do-async-generators-and-async-context-managers-work)
- [352: What is structured concurrency and why does it matter?](#352-what-is-structured-concurrency-and-why-does-it-matter)
- [353: Why is threading still useful in CPython with the GIL?](#353-why-is-threading-still-useful-in-cpython-with-the-gil)
- [354: How does the GIL decide when to switch threads?](#354-how-does-the-gil-decide-when-to-switch-threads)
- [355: Which operations are atomic in CPython?](#355-which-operations-are-atomic-in-cpython)
- [356: How do you avoid deadlocks?](#356-how-do-you-avoid-deadlocks)
- [357: What are the start methods in multiprocessing?](#357-what-are-the-start-methods-in-multiprocessing)
- [358: How do you share data between processes?](#358-how-do-you-share-data-between-processes)
- [359: When would you pick processes, threads, async, subinterpreters or free-threading?](#359-when-would-you-pick-processes-threads-async-subinterpreters-or-free-threading)
- [360: How do you speed up a slow CPU-bound Python function?](#360-how-do-you-speed-up-a-slow-cpu-bound-python-function)
- [361: What are common micro-optimizations in Python, and when do they matter?](#361-what-are-common-micro-optimizations-in-python-and-when-do-they-matter)
- [362: How do C extensions work with Python?](#362-how-do-c-extensions-work-with-python)
- [363: What is the stable ABI (abi3)?](#363-what-is-the-stable-abi-abi3)
- [364: What is ctypes and when would you use it?](#364-what-is-ctypes-and-when-would-you-use-it)
- [365: What is PyPy and when would you use it?](#365-what-is-pypy-and-when-would-you-use-it)
- [366: What is Cython?](#366-what-is-cython)
- [367: What is mypyc?](#367-what-is-mypyc)
- [368: How does eval and exec work and why are they dangerous?](#368-how-does-eval-and-exec-work-and-why-are-they-dangerous)
- [369: What are the main security risks in Python web apps?](#369-what-are-the-main-security-risks-in-python-web-apps)
- [370: How do you prevent path traversal when serving files?](#370-how-do-you-prevent-path-traversal-when-serving-files)
- [371: What is ReDoS and how does it affect Python?](#371-what-is-redos-and-how-does-it-affect-python)
- [372: How do you protect against supply chain attacks with Python packages?](#372-how-do-you-protect-against-supply-chain-attacks-with-python-packages)
- [373: What is ParamSpec and why is it useful for decorators?](#373-what-is-paramspec-and-why-is-it-useful-for-decorators)
- [374: What is variance in generics?](#374-what-is-variance-in-generics)
- [375: What is the difference between TypeGuard and TypeIs?](#375-what-is-the-difference-between-typeguard-and-typeis)
- [376: What is Annotated used for?](#376-what-is-annotated-used-for)
- [377: What are Never and NoReturn?](#377-what-are-never-and-noreturn)
- [378: What are TypeVarTuple and default type parameters?](#378-what-are-typevartuple-and-default-type-parameters)
- [379: Should you validate type hints at runtime?](#379-should-you-validate-type-hints-at-runtime)
- [380: How do comprehensions handle scope?](#380-how-do-comprehensions-handle-scope)
- [381: Why can't a class body variable be used inside a comprehension in the same class?](#381-why-cant-a-class-body-variable-be-used-inside-a-comprehension-in-the-same-class)
- [382: What happens when finally has a return statement?](#382-what-happens-when-finally-has-a-return-statement)
- [383: What happens when you close a generator?](#383-what-happens-when-you-close-a-generator)
- [384: What is the classic bug with iterators being exhausted?](#384-what-is-the-classic-bug-with-iterators-being-exhausted)
- [385: How is the f-string syntax different since Python 3.12?](#385-how-is-the-f-string-syntax-different-since-python-312)
- [386: Why were t-strings added when f-strings already exist?](#386-why-were-t-strings-added-when-f-strings-already-exist)
- [387: How does sys.monitoring differ from sys.settrace?](#387-how-does-sysmonitoring-differ-from-syssettrace)
- [388: What are audit hooks?](#388-what-are-audit-hooks)
- [389: How do you debug a stuck or slow Python process in production?](#389-how-do-you-debug-a-stuck-or-slow-python-process-in-production)
- [390: What is faulthandler?](#390-what-is-faulthandler)
- [391: How do you reduce Python startup time?](#391-how-do-you-reduce-python-startup-time)
- [392: How does Python decide when to recompile .pyc files?](#392-how-does-python-decide-when-to-recompile-pyc-files)
- [393: How do you build a good Docker image for a Python app?](#393-how-do-you-build-a-good-docker-image-for-a-python-app)
- [394: What are dependency groups and inline script metadata?](#394-what-are-dependency-groups-and-inline-script-metadata)
- [395: What is pylock.toml?](#395-what-is-pylocktoml)
- [396: How does pip resolve dependencies?](#396-how-does-pip-resolve-dependencies)
- [397: What are manylinux wheels?](#397-what-are-manylinux-wheels)
- [398: How do you structure a large Python application?](#398-how-do-you-structure-a-large-python-application)
- [399: How do you do dependency injection in Python?](#399-how-do-you-do-dependency-injection-in-python)
- [400: How do you implement a singleton in Python?](#400-how-do-you-implement-a-singleton-in-python)
- [401: Is functools.lru_cache thread-safe?](#401-is-functoolslru_cache-thread-safe)
- [402: Why can lru_cache on a method cause memory leaks?](#402-why-can-lru_cache-on-a-method-cause-memory-leaks)
- [403: How do you design a retry with exponential backoff?](#403-how-do-you-design-a-retry-with-exponential-backoff)
- [404: How would you implement a rate limiter in Python?](#404-how-would-you-implement-a-rate-limiter-in-python)
- [405: Why use time.monotonic instead of time.time for measuring durations?](#405-why-use-timemonotonic-instead-of-timetime-for-measuring-durations)
- [406: How do datetimes handle daylight saving time transitions?](#406-how-do-datetimes-handle-daylight-saving-time-transitions)
- [407: How do you handle Unicode text correctly?](#407-how-do-you-handle-unicode-text-correctly)
- [408: How do you configure logging for a whole application?](#408-how-do-you-configure-logging-for-a-whole-application)
- [409: How do you log safely from multiple processes?](#409-how-do-you-log-safely-from-multiple-processes)
- [410: What is property-based testing?](#410-what-is-property-based-testing)
- [411: What are common mocking mistakes?](#411-what-are-common-mocking-mistakes)
- [412: How do you test code that depends on the current time?](#412-how-do-you-test-code-that-depends-on-the-current-time)
- [413: How do you test async code?](#413-how-do-you-test-async-code)
- [414: How do you test code that talks to a real database?](#414-how-do-you-test-code-that-talks-to-a-real-database)
- [415: How do database transactions work with SQLAlchemy sessions?](#415-how-do-database-transactions-work-with-sqlalchemy-sessions)
- [416: Why can database connection pools break after fork?](#416-why-can-database-connection-pools-break-after-fork)
- [417: How do you make Celery tasks safe to retry?](#417-how-do-you-make-celery-tasks-safe-to-retry)
- [418: How do you add caching to a Python web service?](#418-how-do-you-add-caching-to-a-python-web-service)
- [419: A FastAPI endpoint is slow under load. How do you find the cause?](#419-a-fastapi-endpoint-is-slow-under-load-how-do-you-find-the-cause)
- [420: A worker process's memory keeps growing until it gets killed. What do you do?](#420-a-worker-processs-memory-keeps-growing-until-it-gets-killed-what-do-you-do)
- [421: CPU is at 100% on one core but the service is slow. What might be happening?](#421-cpu-is-at-100-on-one-core-but-the-service-is-slow-what-might-be-happening)
- [422: How do you safely load YAML?](#422-how-do-you-safely-load-yaml)
- [423: How do you prevent SSRF when your app fetches URLs given by users?](#423-how-do-you-prevent-ssrf-when-your-app-fetches-urls-given-by-users)
- [424: How should you handle secrets in a Python application?](#424-how-should-you-handle-secrets-in-a-python-application)
- [425: What is the difference between deepcopy and pickling for cloning objects?](#425-what-is-the-difference-between-deepcopy-and-pickling-for-cloning-objects)
- [426: How do you customize pickling for a class?](#426-how-do-you-customize-pickling-for-a-class)
- [427: What is the buffer protocol and memoryview?](#427-what-is-the-buffer-protocol-and-memoryview)
- [428: How do generators compare with lists for memory and speed?](#428-how-do-generators-compare-with-lists-for-memory-and-speed)
- [429: How do you implement the observer or event pattern in Python?](#429-how-do-you-implement-the-observer-or-event-pattern-in-python)
- [430: What is the Liskov substitution principle and how does it apply in Python?](#430-what-is-the-liskov-substitution-principle-and-how-does-it-apply-in-python)
- [431: How do you make a class immutable?](#431-how-do-you-make-a-class-immutable)
- [432: How is attrs different from dataclasses?](#432-how-is-attrs-different-from-dataclasses)
- [433: What is msgspec and when would you use it over Pydantic?](#433-what-is-msgspec-and-when-would-you-use-it-over-pydantic)
- [434: How does class getitem work?](#434-how-does-class-getitem-work)
- [435: What is the difference between an abstract property and a regular abstract method?](#435-what-is-the-difference-between-an-abstract-property-and-a-regular-abstract-method)
- [436: Why is chaining classmethod and property no longer supported?](#436-why-is-chaining-classmethod-and-property-no-longer-supported)
- [437: How do you write a plugin system with abstract base classes and entry points together?](#437-how-do-you-write-a-plugin-system-with-abstract-base-classes-and-entry-points-together)
- [438: What happens when you modify a list while iterating over it?](#438-what-happens-when-you-modify-a-list-while-iterating-over-it)
- [439: What is the difference between str and repr when logging exceptions?](#439-what-is-the-difference-between-str-and-repr-when-logging-exceptions)
- [440: How do you handle very deep recursion?](#440-how-do-you-handle-very-deep-recursion)
- [441: How does Python's integer type handle very large numbers efficiently?](#441-how-does-pythons-integer-type-handle-very-large-numbers-efficiently)
- [442: How would you design a module that must work on several Python versions?](#442-how-would-you-design-a-module-that-must-work-on-several-python-versions)
- [443: What does the dis module show you that helps with performance questions?](#443-what-does-the-dis-module-show-you-that-helps-with-performance-questions)
- [444: How do you benchmark code fairly in Python?](#444-how-do-you-benchmark-code-fairly-in-python)
- [445: What are the trade-offs of using asyncio for a database-heavy service?](#445-what-are-the-trade-offs-of-using-asyncio-for-a-database-heavy-service)
- [446: How do you share state between asyncio and threads safely?](#446-how-do-you-share-state-between-asyncio-and-threads-safely)
- [447: What does gc.freeze do and why do some services use it?](#447-what-does-gcfreeze-do-and-why-do-some-services-use-it)
- [448: How do you safely run untrusted Python code?](#448-how-do-you-safely-run-untrusted-python-code)
- [449: What were the main changes in Python 3.14 and 3.15?](#449-what-were-the-main-changes-in-python-314-and-315)
- [450: What makes Python code "Pythonic"?](#450-what-makes-python-code-pythonic)

---

# Easy Questions (1-150)

## 1: What is Python?

Python is a general purpose, high level programming language. It is dynamically typed, garbage collected, and has a large standard library. People use it for web back ends, scripts, data work, machine learning, automation and testing.

The code is easy to read because blocks are marked by indentation instead of braces.

## 2: What is the difference between Python and CPython?

Python is the language. CPython is the main implementation of it, written in C, and it is what you get from python.org. Other implementations exist, like PyPy (with a JIT), MicroPython (for small devices) and GraalPy. When people say "Python" they usually mean CPython.

## 3: Is Python compiled or interpreted?

Both, in a way. CPython first compiles your source code to bytecode (`.pyc` files), then a virtual machine runs that bytecode. There is no separate build step you run by hand, so it feels like an interpreted language. Recent versions also have an optional experimental JIT compiler.

## 4: What does dynamically typed mean?

Variables don't have fixed types. A name just points to an object, and the object has the type. The same name can point to an int now and a string later.

```python
x = 10
x = "ten"  # fine
```

Python is also strongly typed: it won't silently turn `"1" + 1` into something. That line raises `TypeError`.

## 5: How do you check the Python version?

From the shell run `python --version` (or `python3 --version`). From code, use `sys.version` or `sys.version_info`.

```python
import sys

print(sys.version_info >= (3, 12))
```

## 6: Why does indentation matter in Python?

Indentation is part of the syntax. It decides which lines belong to an `if`, a loop, a function or a class. Mixing tabs and spaces or indenting wrongly gives an `IndentationError`. The standard is 4 spaces per level.

```python
if True:
    print("inside")
print("outside")
```

## 7: What are the built-in data types in Python?

The common ones are:

- Numbers: `int`, `float`, `complex`, `bool`
- Text: `str`
- Sequences: `list`, `tuple`, `range`
- Binary: `bytes`, `bytearray`, `memoryview`
- Mappings: `dict` (and `frozendict` since 3.15)
- Sets: `set`, `frozenset`
- `None`, which has its own type `NoneType`

## 8: What is the difference between a list and a tuple?

A list is mutable: you can add, remove and change items. A tuple is immutable: once created it can't change. Tuples are a bit smaller and faster, can be used as dict keys (if their items are hashable), and are often used for fixed groups of values like a point `(x, y)`.

```python
items = [1, 2]
items.append(3)

point = (1, 2)
# point[0] = 5  -> TypeError
```

## 9: What is a dictionary?

A `dict` stores key-value pairs. Lookups by key are fast (average O(1)) because it is a hash table. Keys must be hashable. Since Python 3.7, dicts keep insertion order.

```python
user = {"name": "Ana", "age": 30}
print(user["name"])
user["email"] = "ana@example.com"
```

## 10: What is a set?

A `set` is an unordered collection of unique, hashable items. It is good for removing duplicates and for fast membership checks.

```python
tags = {"python", "web", "python"}
print(tags)          # {'python', 'web'}
print("web" in tags) # True
```

## 11: How do you create an empty set?

Use `set()`. Writing `{}` creates an empty dict, not a set.

```python
s = set()
d = {}
print(type(s), type(d))
```

## 12: What is None?

`None` is a special object that means "no value". Functions that don't return anything return `None`. There is only one `None` object, so you compare with `is`:

```python
if result is None:
    print("nothing came back")
```

## 13: What is the difference between == and is?

`==` checks if two objects have equal values (it calls `__eq__`). `is` checks if two names point to the very same object in memory. Use `is` for `None`, `True` and `False`, and `==` for everything else.

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False
```

## 14: What are mutable and immutable objects?

Mutable objects can change after creation: `list`, `dict`, `set`, `bytearray` and most user classes. Immutable objects can't: `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`. When you "change" a string you really create a new one.

## 15: How do you write a comment in Python?

A single line comment starts with `#`. Python has no block comment syntax, so you put `#` on every line. Triple-quoted strings are sometimes used for long notes, but they are really string expressions, and at the top of a function they become a docstring.

## 16: What is a docstring?

A docstring is a string literal placed as the first statement of a module, function, class or method. Python stores it in the `__doc__` attribute, and tools like `help()` and IDEs show it.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add.__doc__)
```

## 17: How do you define a function?

Use `def`, a name, parameters in parentheses, and an indented body. Use `return` to send back a value.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ana"))
```

## 18: What are default arguments?

A parameter can have a default value that is used when the caller doesn't pass it. Default values are evaluated once, when the function is defined, not on every call. That is why you shouldn't use a mutable object like `[]` as a default.

```python
def connect(host, port=5432):
    return f"{host}:{port}"
```

## 19: What are args and kwargs (the star and double star parameters)?

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dict. The names are just a convention; the stars do the work.

```python
def log(*args, **kwargs):
    print(args, kwargs)

log(1, 2, level="info")  # (1, 2) {'level': 'info'}
```

## 20: What is the difference between positional and keyword arguments?

Positional arguments are matched by their order. Keyword arguments are matched by name, so their order doesn't matter.

```python
def move(x, y):
    return x, y

move(1, 2)        # positional
move(y=2, x=1)    # keyword
```

## 21: What is a lambda function?

A lambda is a small anonymous function written in one expression. It is handy for short callbacks such as a `key` for sorting. For anything longer, use `def`.

```python
users = [{"name": "Bo", "age": 40}, {"name": "Al", "age": 25}]
users.sort(key=lambda u: u["age"])
```

## 22: What is a list comprehension?

It is a short way to build a list from an iterable, with an optional filter.

```python
squares = [n * n for n in range(10) if n % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]
```

It is usually faster and easier to read than a loop with `append`.

## 23: What are dict and set comprehensions?

They work like list comprehensions but build a dict or a set.

```python
words = ["apple", "bob", "cat"]
lengths = {w: len(w) for w in words}
first_letters = {w[0] for w in words}
```

## 24: How do you write an if statement?

Use `if`, then optional `elif` branches and an optional `else`.

```python
score = 72
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"
```

## 25: What is the ternary (conditional) expression in Python?

Python writes it as `value_if_true if condition else value_if_false`.

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

## 26: How does a for loop work in Python?

A `for` loop goes over the items of any iterable: a list, string, dict, file, range and so on. It doesn't use an index counter like C.

```python
for name in ["Ana", "Bo"]:
    print(name)

for i in range(3):
    print(i)  # 0, 1, 2
```

## 27: What does range() do?

`range(start, stop, step)` gives a lazy sequence of integers. `stop` is not included. It doesn't build a full list in memory, so `range(10**9)` is cheap.

```python
list(range(2, 10, 3))  # [2, 5, 8]
```

## 28: What is a while loop?

A `while` loop runs as long as its condition is true.

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

## 29: What do break, continue and pass do?

- `break` exits the loop right away.
- `continue` skips the rest of the current iteration and goes to the next one.
- `pass` does nothing. It is a placeholder where a statement is required, like an empty function body.

## 30: What is the else clause on a loop?

A `for` or `while` loop can have an `else` block. It runs only if the loop finished without hitting `break`. It is useful for search loops.

```python
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("found even")
        break
else:
    print("no even numbers")
```

## 31: How do you use enumerate()?

`enumerate()` gives you the index and the item together, so you don't need `range(len(...))`.

```python
for i, fruit in enumerate(["apple", "pear"], start=1):
    print(i, fruit)
```

## 32: What does zip() do?

`zip()` walks over several iterables in parallel and gives tuples. It stops at the shortest one. Pass `strict=True` to get an error if the lengths differ.

```python
names = ["Ana", "Bo"]
ages = [30, 40]
for name, age in zip(names, ages, strict=True):
    print(name, age)
```

## 33: What is string slicing?

Slicing takes part of a sequence with `[start:stop:step]`. `stop` is not included, and negative numbers count from the end.

```python
s = "python"
s[0:2]   # 'py'
s[-3:]   # 'hon'
s[::-1]  # 'nohtyp'
```

## 34: How do you get the length of a list or string?

Use the built-in `len()`. It works on any object that has a `__len__` method.

```python
len([1, 2, 3])  # 3
len("hello")    # 5
```

## 35: What are f-strings?

f-strings (formatted string literals) let you put expressions inside `{}` in a string that starts with `f`. They are the most common way to format strings today.

```python
name = "Ana"
total = 12.5
print(f"{name} owes {total:.2f} dollars")
print(f"{total=}")  # total=12.5, handy for debugging
```

## 36: What are some common string methods?

- `strip()`, `lstrip()`, `rstrip()` remove whitespace
- `lower()`, `upper()`, `title()`
- `split()` and `join()`
- `replace(old, new)`
- `startswith()`, `endswith()`
- `find()` and `index()`
- `removeprefix()` and `removesuffix()`

```python
", ".join(["a", "b"])        # 'a, b'
"a,b,c".split(",")           # ['a', 'b', 'c']
"report.csv".removesuffix(".csv")  # 'report'
```

## 37: How do you join a list of strings?

Call `join()` on the separator string, not on the list.

```python
words = ["one", "two", "three"]
print(" ".join(words))
```

All items must be strings, so convert numbers first: `", ".join(map(str, nums))`.

## 38: Are strings mutable in Python?

No. Strings are immutable. Methods like `upper()` return a new string. Building a big string with `+=` in a loop creates many temporary strings, so collect parts in a list and `join` them instead.

## 39: How do you convert between types?

Call the type like a function: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`, `bool()`.

```python
int("42")          # 42
float("3.5")       # 3.5
str(10)            # '10'
list("abc")        # ['a', 'b', 'c']
int("ff", 16)      # 255
```

Invalid input like `int("abc")` raises `ValueError`.

## 40: What values are falsy in Python?

`False`, `None`, zero of any number type (`0`, `0.0`), and empty collections (`""`, `[]`, `()`, `{}`, `set()`, `range(0)`). Everything else is truthy by default. Classes can change this with `__bool__` or `__len__`.

```python
items = []
if not items:
    print("empty")
```

## 41: What are the logical operators in Python?

`and`, `or` and `not`. `and` and `or` short-circuit and return one of the operands, not always a bool.

```python
name = "" or "guest"   # 'guest'
x = 0 and 10           # 0
```

## 42: What is the difference between / and //?

`/` is true division and always returns a float. `//` is floor division: it rounds down toward negative infinity. `%` gives the remainder.

```python
7 / 2    # 3.5
7 // 2   # 3
-7 // 2  # -4
7 % 2    # 1
```

## 43: How do you raise a number to a power?

Use `**` or the built-in `pow()`. `pow(base, exp, mod)` does fast modular power.

```python
2 ** 10        # 1024
pow(2, 10, 7)  # 2
```

## 44: How big can integers get in Python?

Python `int` has arbitrary precision. It grows as needed and is limited only by memory. There is no overflow like in C or JavaScript numbers. Converting very long int strings is capped by default (4300 digits) to avoid slow parsing attacks; you can change it with `sys.set_int_max_str_digits()`.

## 45: Why does 0.1 + 0.2 not equal 0.3?

Python floats are IEEE 754 double precision numbers, and 0.1 can't be stored exactly in binary. So `0.1 + 0.2` is `0.30000000000000004`. Use `math.isclose()` to compare floats, and `decimal.Decimal` for money.

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

## 46: How do you get user input?

Use `input()`. It always returns a string, so convert it if you need a number.

```python
age = int(input("Your age: "))
```

## 47: How do you print without a newline?

Pass `end` to `print()`. You can also change the separator with `sep`.

```python
print("loading", end="...")
print(1, 2, 3, sep=", ")
```

## 48: What is a module?

A module is a `.py` file. Its functions, classes and variables can be used in other files with `import`. Modules help you split code into logical pieces and reuse it.

```python
# utils.py
def slugify(text):
    return text.lower().replace(" ", "-")

# main.py
from utils import slugify
```

## 49: What is a package?

A package is a folder of modules. A regular package has an `__init__.py` file, which runs when the package is imported. You import from it with dots, like `from app.models import User`.

## 50: What are the different ways to import?

```python
import json                   # use as json.dumps
import numpy as np            # alias
from os import path           # import one name
from os.path import join, exists
from . import utils           # relative import inside a package
```

Avoid `from module import *`: it fills your namespace with unknown names and makes code harder to read.

## 51: What does the if name == "main" check do?

Every module has a `__name__` variable. When you run a file directly, `__name__` is `"__main__"`. When it is imported, `__name__` is the module name. So this check lets a file run some code only when it is executed as a script, not when imported.

```python
def main():
    print("running")

if __name__ == "__main__":
    main()
```

## 52: What is pip?

pip is the standard tool for installing packages from PyPI (the Python Package Index).

```bash
python -m pip install requests
python -m pip install "django>=5,<6"
python -m pip list
python -m pip uninstall requests
```

Running it as `python -m pip` makes sure you use the pip that belongs to the Python you expect.

## 53: What is a virtual environment?

A virtual environment is a folder with its own Python interpreter link and its own installed packages. It keeps each project's dependencies separate, so two projects can use different versions of the same library.

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

## 54: What is requirements.txt?

It is a plain text file listing the packages a project needs, one per line, often with versions. You install them with `pip install -r requirements.txt`. Many newer projects list dependencies in `pyproject.toml` instead and use a lock file from a tool like uv or Poetry.

```text
requests==2.32.3
fastapi>=0.115
```

## 55: What is PEP 8?

PEP 8 is the official style guide for Python code. Some of its main points:

- 4 spaces per indent level
- `snake_case` for functions and variables, `PascalCase` for classes, `UPPER_CASE` for constants
- Two blank lines around top-level functions and classes
- Imports at the top, grouped as standard library, third-party, local

Tools like Ruff and Black apply these rules for you.

## 56: What is a PEP?

PEP stands for Python Enhancement Proposal. It is a design document that proposes a new feature or process for Python, for example PEP 8 (style), PEP 484 (type hints) or PEP 810 (lazy imports). The steering council accepts or rejects them.

## 57: How do you handle exceptions?

Use `try` and `except`. Add `else` for code that runs only when no error happened, and `finally` for cleanup that always runs.

```python
try:
    value = int(text)
except ValueError:
    print("not a number")
else:
    print("parsed", value)
finally:
    print("done")
```

## 58: How do you raise an exception?

Use `raise` with an exception instance or class.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
```

Inside an `except` block, a bare `raise` re-raises the current exception.

## 59: How do you catch more than one exception type?

List the types. Since Python 3.14 you can leave out the parentheses when there is no `as` clause; with `as`, the parentheses are still required.

```python
try:
    do_work()
except (KeyError, IndexError) as e:
    print("lookup failed:", e)

# 3.14+
try:
    do_work()
except KeyError, IndexError:
    print("lookup failed")
```

## 60: How do you create a custom exception?

Subclass `Exception` (or a more specific built-in exception).

```python
class PaymentError(Exception):
    pass

class CardDeclined(PaymentError):
    def __init__(self, code):
        super().__init__(f"card declined: {code}")
        self.code = code
```

Having your own base class lets callers catch all errors from your library with one `except`.

## 61: What are some common built-in exceptions?

- `ValueError`: right type, bad value (`int("x")`)
- `TypeError`: wrong type (`"a" + 1`)
- `KeyError`: missing dict key
- `IndexError`: list index out of range
- `AttributeError`: missing attribute
- `FileNotFoundError`: file doesn't exist
- `ZeroDivisionError`
- `ImportError` / `ModuleNotFoundError`
- `StopIteration`: iterator is finished

## 62: Why should you avoid a bare except?

`except:` with no type catches everything, including `KeyboardInterrupt` and `SystemExit`, so Ctrl+C may not stop your program and real bugs get hidden. Catch specific exceptions, or `except Exception` if you really need a catch-all, and log the error.

## 63: How do you read a file?

Use `open()` inside a `with` block so the file closes for you. Pass an encoding for text files.

```python
with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

Since 3.15, UTF-8 is the default text encoding, but writing `encoding="utf-8"` is still a good habit for code that runs on older versions.

## 64: How do you write to a file?

Open it with mode `"w"` (overwrite) or `"a"` (append).

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    print("second line", file=f)
```

Use `"rb"` and `"wb"` for binary data like images.

## 65: What is the with statement?

`with` uses a context manager to set something up and always clean it up, even if an error happens. Files, locks, database connections and temp directories all support it.

```python
import threading

lock = threading.Lock()
with lock:
    print("only one thread here")
```

## 66: What is pathlib?

`pathlib` gives an object-oriented way to work with file paths. It is usually nicer than `os.path` string functions.

```python
from pathlib import Path

config = Path.home() / ".myapp" / "config.toml"
if config.exists():
    text = config.read_text(encoding="utf-8")

for p in Path("src").rglob("*.py"):
    print(p.name)
```

## 67: How do you work with JSON in Python?

Use the built-in `json` module.

```python
import json

data = {"name": "Ana", "tags": ["a", "b"]}
text = json.dumps(data, indent=2)
back = json.loads(text)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)
```

## 68: What is a class?

A class is a blueprint for creating objects. It groups data (attributes) and behavior (methods).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"

rex = Dog("Rex")
print(rex.bark())
```

## 69: What is the init method?

`__init__` is the method Python calls right after a new object is created. You use it to set the starting attributes. It is an initializer, not the real constructor: the object is created by `__new__` before `__init__` runs.

## 70: What is self?

`self` is the first parameter of an instance method and refers to the object the method was called on. Python passes it automatically: `rex.bark()` is really `Dog.bark(rex)`. The name `self` is a convention, not a keyword.

## 71: What is the difference between class attributes and instance attributes?

A class attribute is defined on the class and shared by all instances. An instance attribute is set on `self` and belongs to one object.

```python
class Counter:
    created = 0           # class attribute

    def __init__(self):
        self.value = 0    # instance attribute
        Counter.created += 1
```

## 72: What is inheritance?

Inheritance lets a class reuse and extend another class. The child class gets the parent's methods and can override them.

```python
class Animal:
    def speak(self):
        return "..."

class Cat(Animal):
    def speak(self):
        return "meow"
```

## 73: What does super() do?

`super()` gives you access to the parent class's methods, following the method resolution order. It is most often used to call the parent's `__init__`.

```python
class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
```

## 74: What is method overriding?

When a child class defines a method with the same name as one in the parent, the child's version is used for its instances. That is overriding. You can still call the parent's version with `super()`.

## 75: Does Python support method overloading?

Not in the Java sense. If you define two methods with the same name, the second replaces the first. You get similar results with default arguments, `*args`, or `functools.singledispatch`, which picks a function by the type of the first argument.

## 76: What is encapsulation in Python?

Python has no real `private` keyword. By convention, a name starting with `_` is internal and shouldn't be used from outside. A name starting with two underscores (like `__secret`) gets name mangling to `_ClassName__secret`, which helps avoid clashes in subclasses but isn't real security.

## 77: What are instance methods, class methods and static methods?

- Instance methods take `self` and work with one object.
- Class methods take `cls` and work with the class. They are often used as alternative constructors.
- Static methods take neither; they are plain functions placed in the class namespace.

```python
class Date:
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    @classmethod
    def from_string(cls, s):
        return cls(*map(int, s.split("-")))

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

## 78: What is the str method used for?

`__str__` returns a readable string for users. `print()` and `str()` call it. `__repr__` returns a string for developers, ideally one that looks like code to recreate the object. If only `__repr__` is defined, `str()` falls back to it.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

## 79: What is a dataclass?

`@dataclass` creates `__init__`, `__repr__` and `__eq__` for you from the class annotations. It cuts out a lot of boilerplate for classes that mainly hold data.

```python
from dataclasses import dataclass, field

@dataclass
class Order:
    id: int
    items: list[str] = field(default_factory=list)
    paid: bool = False

o = Order(1)
print(o)  # Order(id=1, items=[], paid=False)
```

## 80: What are type hints?

Type hints are optional annotations that say what types a function expects and returns. Python doesn't enforce them at runtime. Tools like mypy, Pyright and IDEs use them to find bugs.

```python
def total(prices: list[float], tax: float = 0.2) -> float:
    return sum(prices) * (1 + tax)
```

## 81: How do you write an optional type?

Use `X | None` (Python 3.10+). The older form is `Optional[X]` from `typing`.

```python
def find_user(user_id: int) -> User | None:
    ...
```

## 82: What is the global keyword?

`global` lets a function assign to a module-level variable. Without it, an assignment inside a function creates a new local variable. Using a lot of globals makes code hard to follow, so try to pass values in and return them instead.

```python
count = 0

def bump():
    global count
    count += 1
```

## 83: What is the nonlocal keyword?

`nonlocal` lets a nested function assign to a variable in the enclosing function's scope.

```python
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc
```

## 84: What is scope in Python (the LEGB rule)?

When Python looks up a name, it checks four scopes in order:

1. Local (inside the current function)
2. Enclosing (outer functions)
3. Global (module level)
4. Built-in (names like `len`, `print`)

The first match wins.

## 85: How do you copy a list?

Use `list.copy()`, `list(old)` or `old[:]`. These make a shallow copy. Writing `b = a` doesn't copy; both names point to the same list.

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
```

## 86: What is the difference between a shallow copy and a deep copy?

A shallow copy creates a new outer object but keeps references to the same inner objects. A deep copy copies everything recursively.

```python
import copy

a = [[1, 2], [3]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)
a[0].append(99)
print(shallow[0])  # [1, 2, 99]
print(deep[0])     # [1, 2]
```

## 87: How do you sort a list?

`list.sort()` sorts in place and returns `None`. `sorted()` returns a new list and works on any iterable. Both take `key` and `reverse`.

```python
nums = [3, 1, 2]
nums.sort()
names = sorted(["bo", "Al", "cy"], key=str.lower, reverse=True)
```

Python's sort is stable: equal items keep their original order.

## 88: What are the main list methods?

- `append(x)`, `extend(iterable)`, `insert(i, x)`
- `pop([i])`, `remove(x)`, `clear()`
- `index(x)`, `count(x)`
- `sort()`, `reverse()`, `copy()`

`append([1, 2])` adds one item (a list), while `extend([1, 2])` adds two items.

## 89: How do you safely get a value from a dict?

Use `get()`, which returns `None` (or a default you pass) when the key is missing, instead of raising `KeyError`.

```python
config = {"debug": True}
port = config.get("port", 8000)
```

## 90: How do you loop over a dictionary?

```python
prices = {"apple": 1.2, "pear": 0.9}

for key in prices:
    print(key)

for value in prices.values():
    print(value)

for key, value in prices.items():
    print(key, value)
```

## 91: How do you merge two dictionaries?

Use `|` (Python 3.9+) to make a new dict, or `|=` / `update()` to change one in place. On duplicate keys, the right side wins.

```python
defaults = {"debug": False, "port": 8000}
overrides = {"port": 9000}
config = defaults | overrides  # {'debug': False, 'port': 9000}
```

## 92: What are the set operations?

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # union {1, 2, 3, 4}
a & b   # intersection {2, 3}
a - b   # difference {1}
a ^ b   # symmetric difference {1, 4}
```

## 93: What is tuple unpacking?

You can assign the items of a sequence to several names at once. A starred name collects the rest.

```python
x, y = (10, 20)
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
a, b = b, a                    # swap
```

## 94: What is the in operator?

`in` checks membership. It works on strings (substring), lists, tuples, sets and dicts (keys).

```python
"py" in "python"      # True
3 in [1, 2, 3]        # True
"name" in {"name": 1} # True
```

For big collections, checking a set or dict is much faster than a list.

## 95: What are any() and all()?

`any()` returns `True` if at least one item is truthy. `all()` returns `True` if every item is truthy (and for an empty iterable). Both stop as soon as the answer is known.

```python
nums = [2, 4, 7]
any(n % 2 for n in nums)        # True
all(n > 0 for n in nums)        # True
```

## 96: What do map() and filter() do?

`map(func, iterable)` applies a function to each item. `filter(func, iterable)` keeps the items where the function returns a truthy value. Both return lazy iterators. List comprehensions often do the same thing more clearly.

```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda n: n * 2, nums))
evens = list(filter(lambda n: n % 2 == 0, nums))
```

## 97: What are min(), max() and sum()?

They return the smallest item, the largest item and the total. `min` and `max` take a `key` and a `default` for empty input.

```python
users = [{"n": "a", "age": 30}, {"n": "b", "age": 20}]
youngest = min(users, key=lambda u: u["age"])
max([], default=0)  # 0
sum([0.5, 1.5], start=10)  # 12.0
```

## 98: What is the difference between a function and a method?

A function is defined on its own with `def`. A method is a function defined inside a class and called on an object, which gets passed as `self`. `len(x)` is a function; `x.append(1)` is a method call.

## 99: What is an iterable?

An iterable is anything you can loop over: lists, strings, dicts, files, generators. Technically, it has an `__iter__` method that returns an iterator (or a `__getitem__` that accepts 0, 1, 2 ...).

## 100: What is an iterator?

An iterator is an object that gives the next value each time you call `next()` on it, and raises `StopIteration` when it is done. You get one from an iterable with `iter()`. An iterator can only be used once.

```python
it = iter([1, 2])
next(it)  # 1
next(it)  # 2
next(it)  # StopIteration
```

## 101: What is a generator?

A generator is a function that uses `yield`. Calling it doesn't run the body; it returns a generator object. Each `next()` runs the code until the next `yield` and pauses there. Generators produce values one at a time, so they use very little memory.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)
```

## 102: What is a generator expression?

It looks like a list comprehension but with parentheses. It produces values lazily instead of building a full list.

```python
total = sum(n * n for n in range(1_000_000))
```

## 103: What is the difference between return and yield?

`return` ends the function and sends back one value. `yield` sends back a value but pauses the function so it can continue later. A function with `yield` becomes a generator.

## 104: What is a decorator?

A decorator is a function that takes a function and returns a new one, usually adding behavior around it. The `@` syntax is a shortcut for `func = decorator(func)`.

```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

## 105: What does the del statement do?

`del` removes a name binding, a list item, a slice or a dict key. It doesn't directly free memory; the object is freed when nothing else references it.

```python
nums = [1, 2, 3]
del nums[0]
d = {"a": 1}
del d["a"]
```

## 106: How do you check the type of an object?

Use `type(obj)` to get the exact type, and `isinstance(obj, cls)` to check if it is an instance of a class or its subclasses. `isinstance` is usually what you want.

```python
isinstance(True, int)   # True, bool is a subclass of int
type(True) is int       # False
isinstance(3, int | float)  # True
```

## 107: What are keywords in Python?

Keywords are reserved words you can't use as names, like `if`, `for`, `def`, `class`, `return`, `None`, `True`, `lambda`, `async` and `await`. There are also soft keywords that are only special in certain places: `match`, `case`, `_`, `type` and, since 3.15, `lazy`. You can list them with the `keyword` module.

## 108: What is the walrus operator?

`:=` assigns a value inside an expression. It helps avoid calling something twice.

```python
import re

if (m := re.search(r"\d+", "order 42")):
    print(m.group())

while (line := input()) != "quit":
    print(line)
```

## 109: What is the match statement?

`match` (Python 3.10+) is structural pattern matching. It compares a value against patterns and can pull data out at the same time.

```python
def handle(cmd):
    match cmd.split():
        case ["go", direction]:
            return f"going {direction}"
        case ["quit"]:
            return "bye"
        case _:
            return "unknown"
```

## 110: How do you get the current date and time?

Use the `datetime` module. Prefer timezone-aware datetimes.

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M"))
```

`datetime.utcnow()` is deprecated because it returns a naive object.

## 111: How do you generate random numbers?

Use the `random` module for simulations and games. For tokens and passwords, use `secrets`.

```python
import random, secrets

random.randint(1, 6)
random.choice(["a", "b", "c"])
random.shuffle(cards)
token = secrets.token_urlsafe(32)
```

## 112: What is the math module?

`math` has math functions for floats and ints: `sqrt`, `floor`, `ceil`, `log`, `sin`, `pi`, `inf`, `gcd`, `isclose`, `prod` and more.

```python
import math
math.sqrt(16)   # 4.0
math.ceil(2.1)  # 3
math.prod([2, 3, 4])  # 24
```

## 113: What is the os module used for?

`os` talks to the operating system: environment variables, process info, and file system calls.

```python
import os

db_url = os.environ.get("DATABASE_URL", "sqlite:///dev.db")
os.makedirs("logs", exist_ok=True)
print(os.getcwd())
```

For paths, `pathlib` is usually easier.

## 114: What is the sys module used for?

`sys` gives access to the interpreter: `sys.argv` (command-line arguments), `sys.path` (import search path), `sys.exit()`, `sys.stdin`, `sys.stdout` and `sys.version_info`.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("usage: app.py FILE")
```

## 115: How do you read command-line arguments?

For simple cases use `sys.argv`. For real CLIs use `argparse`, which handles flags, help text and errors.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
print(args.path, args.verbose)
```

## 116: What is the difference between append() and extend()?

`append(x)` adds `x` as a single item. `extend(iterable)` adds every item from the iterable.

```python
a = [1]
a.append([2, 3])   # [1, [2, 3]]
b = [1]
b.extend([2, 3])   # [1, 2, 3]
```

## 117: What is the difference between remove(), pop() and del on a list?

- `remove(x)` deletes the first item equal to `x` (by value).
- `pop(i)` deletes the item at index `i` and returns it (last item by default).
- `del lst[i]` deletes by index or slice and returns nothing.

## 118: How do you reverse a list?

`lst.reverse()` reverses in place. `lst[::-1]` returns a reversed copy. `reversed(lst)` returns a lazy iterator.

## 119: How do you remove duplicates from a list?

`list(set(items))` removes duplicates but loses order. To keep order, use `dict.fromkeys`.

```python
items = [3, 1, 3, 2, 1]
unique = list(dict.fromkeys(items))  # [3, 1, 2]
```

## 120: How do you count items in a list?

For one value, use `list.count()`. For all values, use `collections.Counter`.

```python
from collections import Counter

words = ["a", "b", "a", "c", "a"]
Counter(words).most_common(1)  # [('a', 3)]
```

## 121: What is a nested function?

A function defined inside another function. It can read the outer function's variables and is often used for helpers and decorators.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner(10)
```

## 122: What is a closure?

A closure is an inner function that remembers variables from the enclosing scope even after the outer function has returned.

```python
def multiplier(n):
    def times(x):
        return x * n
    return times

double = multiplier(2)
double(5)  # 10
```

## 123: Are functions objects in Python?

Yes. Functions are first-class objects. You can store them in variables, put them in lists or dicts, pass them to other functions and return them.

```python
ops = {"add": lambda a, b: a + b, "sub": lambda a, b: a - b}
ops["add"](2, 3)  # 5
```

## 124: What is recursion?

A function that calls itself. It needs a base case to stop. Python has a recursion limit (about 1000 by default) and no tail call optimization, so deep recursion can raise `RecursionError`.

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
```

## 125: What is the difference between a script and a module?

They are both `.py` files. A script is meant to be run directly (`python app.py`). A module is meant to be imported. One file can be both, using the `if __name__ == "__main__":` check.

## 126: How do you run a module as a script?

Use `python -m module_name`. It finds the module on `sys.path` and runs it as `__main__`. This is how you run tools like `python -m pip`, `python -m venv` or `python -m http.server 8000`.

## 127: What is the REPL?

The REPL (read, eval, print loop) is the interactive prompt you get when you run `python` with no file. It is good for quick tests. Since 3.13, the default REPL has colors, multiline editing and history. Use `help()` and `dir()` there to explore objects.

## 128: What do dir() and help() do?

`dir(obj)` lists an object's attributes and methods. `help(obj)` shows its documentation.

```python
dir(str)
help(str.split)
```

## 129: What is the id() function?

`id(obj)` returns an integer that is unique for the object while it is alive. In CPython it is the memory address. `a is b` is the same as `id(a) == id(b)`.

## 130: What are bytes and how are they different from str?

`str` holds Unicode text. `bytes` holds raw 8-bit values. You convert with `encode()` and `decode()`.

```python
text = "café"
data = text.encode("utf-8")  # b'caf\xc3\xa9'
data.decode("utf-8")         # 'café'
```

Network sockets and binary files work with bytes.

## 131: What are raw strings?

A raw string starts with `r` and doesn't treat backslashes as escape characters. They are common for regular expressions and Windows paths.

```python
pattern = r"\d+\.\d+"
```

## 132: How do you write a multiline string?

Use triple quotes. `textwrap.dedent` removes common leading spaces.

```python
sql = """
SELECT id, name
FROM users
WHERE active = 1
"""
```

## 133: How do you check if a string contains only digits?

Use `isdigit()` or `isdecimal()`. Similar methods: `isalpha()`, `isalnum()`, `isspace()`, `isupper()`.

```python
"123".isdigit()   # True
"12.3".isdigit()  # False
```

## 134: What is the difference between find() and index() on strings?

Both return the position of a substring. `find()` returns `-1` if it is not found. `index()` raises `ValueError`.

## 135: How do you check if a key exists in a dictionary?

Use `in`.

```python
if "email" in user:
    send(user["email"])
```

`"x" in d.keys()` works too, but `in d` is shorter.

## 136: What is the difference between a list and an array?

A Python list can hold items of any type and grows as needed. The `array` module gives compact arrays of one numeric type. For numeric work, NumPy arrays are the usual choice because they are fast and support math on the whole array at once.

## 137: How do you flatten a list of lists?

```python
nested = [[1, 2], [3], [4, 5]]
flat = [x for sub in nested for x in sub]

import itertools
flat = list(itertools.chain.from_iterable(nested))
```

## 138: What is the round() function?

`round(x, n)` rounds to `n` decimal places. It uses banker's rounding (round half to even), so `round(2.5)` is `2` and `round(3.5)` is `4`. Floats can also look wrong, like `round(2.675, 2)` giving `2.67`, because of binary storage.

## 139: What is the abs() function?

`abs(x)` returns the absolute value. It works with ints, floats and complex numbers (where it returns the magnitude), and custom classes with `__abs__`.

## 140: What is the difference between break and return?

`break` exits only the nearest loop and keeps running the function. `return` exits the whole function.

## 141: What is chained comparison?

Python lets you chain comparisons, and it reads like math.

```python
age = 25
if 18 <= age < 65:
    print("working age")
```

This is the same as `18 <= age and age < 65`, but `age` is only evaluated once.

## 142: What is the difference between a statement and an expression?

An expression produces a value: `2 + 3`, `f(x)`, `a if b else c`. A statement does something: `if`, `for`, `def`, `import`, an assignment. You can't put a statement where a value is expected, which is why lambdas can only hold one expression.

## 143: What is an assert statement?

`assert condition, message` raises `AssertionError` if the condition is false. It is for checking your own assumptions during development and in tests. Don't use it for input validation: running Python with `-O` removes all asserts.

```python
assert isinstance(port, int), "port must be an int"
```

## 144: What is the pass statement used for?

It is a no-op placeholder where Python needs a statement but you have nothing to write yet, like an empty class or an `except` that you intend to fill in later. `...` (Ellipsis) is often used the same way in stubs.

## 145: How do you format numbers in f-strings?

Use a format spec after a colon.

```python
price = 1234.5678
f"{price:.2f}"     # '1234.57'
f"{price:,.2f}"    # '1,234.57'
f"{0.256:.1%}"     # '25.6%'
f"{42:05d}"        # '00042'
f"{'hi':>6}"       # '    hi'
```

## 146: What is an f-string debug specifier?

Putting `=` after an expression in an f-string prints both the expression and its value. It is useful for quick debugging.

```python
user_id = 7
print(f"{user_id=}")  # user_id=7
```

## 147: How do you comment out a block of code quickly?

Put `#` in front of each line. Most editors do this with a shortcut like Ctrl+/ or Cmd+/. Avoid wrapping code in triple-quoted strings to disable it; it still gets parsed and can confuse readers.

## 148: What are the naming rules for variables?

Names can contain letters, digits and underscores, can't start with a digit, can't be a keyword, and are case-sensitive. By convention, use `snake_case`. Avoid shadowing built-ins like `list`, `id`, `type` or `input`.

## 149: What is the Zen of Python?

It is a list of 19 short guidelines about Python's design, written by Tim Peters. You see it with `import this`. Examples: "Readability counts", "Explicit is better than implicit", "There should be one, and preferably only one, obvious way to do it".

## 150: What is the difference between Python 2 and Python 3?

Python 2 reached end of life in January 2020, so all new code should use Python 3. Main differences: `print` is a function, strings are Unicode by default, `/` always does true division, `range` is lazy, and many APIs return iterators instead of lists. You may still meet Python 2 only in very old legacy systems.

# Moderate Questions (151-300)

## 151: Why is a mutable default argument a bug?

Default values are created once, when `def` runs. If the default is a list or dict and the function changes it, the change stays for the next call.

```python
def add_item(item, items=[]):   # bug
    items.append(item)
    return items

add_item(1)  # [1]
add_item(2)  # [1, 2], not [2]
```

The fix is to default to `None` and create the object inside:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## 152: What is the late binding problem with closures in loops?

Closures look up variables when they are called, not when they are created. So functions made in a loop all see the last value.

```python
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]  # [2, 2, 2]
```

Bind the value at creation time with a default argument: `lambda i=i: i`, or use `functools.partial`.

## 153: What are keyword-only and positional-only parameters?

Parameters after `*` must be passed by keyword. Parameters before `/` must be passed by position.

```python
def create_user(name, /, *, admin=False):
    ...

create_user("ana", admin=True)   # ok
create_user(name="ana")          # TypeError
create_user("ana", True)         # TypeError
```

Keyword-only parameters make calls easier to read. Positional-only ones let you rename parameters later without breaking callers.

## 154: How do you unpack arguments when calling a function?

Use `*` for a sequence and `**` for a dict.

```python
def connect(host, port, timeout=5):
    ...

args = ["db.local", 5432]
opts = {"timeout": 10}
connect(*args, **opts)
```

## 155: What is collections.defaultdict?

A dict that creates a default value for missing keys by calling a factory function. It removes the "check if key exists, then create" step.

```python
from collections import defaultdict

by_team = defaultdict(list)
for name, team in [("ana", "a"), ("bo", "b"), ("cy", "a")]:
    by_team[team].append(name)
# {'a': ['ana', 'cy'], 'b': ['bo']}
```

## 156: What is collections.deque and when do you use it?

A double-ended queue with O(1) appends and pops from both ends. A list is O(n) for `pop(0)` and `insert(0, x)`. With `maxlen`, it keeps only the last N items.

```python
from collections import deque

q = deque(maxlen=3)
for n in range(5):
    q.append(n)
print(q)        # deque([2, 3, 4], maxlen=3)
q.appendleft(1)
q.popleft()
```

## 157: What is a namedtuple and how does it compare to a dataclass?

`namedtuple` makes a tuple subclass with named fields. It is immutable, small and works anywhere a tuple works. `typing.NamedTuple` is the typed form. A dataclass is a regular class, mutable by default, supports defaults and methods more naturally, and isn't a tuple.

```python
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

p = Point(1, 2)
x, y = p
```

## 158: What is a ChainMap?

`collections.ChainMap` groups several dicts into one view. Lookups search them in order. It is useful for layered config, like command-line args over env vars over defaults.

```python
from collections import ChainMap

config = ChainMap(cli_args, env_vars, defaults)
config["port"]
```

## 159: What does functools.lru_cache do?

It caches the results of a function based on its arguments, so repeated calls with the same arguments return right away. `maxsize` limits the cache; `functools.cache` is the same with no limit. Arguments must be hashable.

```python
from functools import cache

@cache
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

fib(100)
fib.cache_info()
```

## 160: What is functools.partial?

`partial` creates a new function with some arguments already filled in.

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
square(5)  # 25
```

## 161: What does functools.reduce do?

`reduce` combines items of an iterable into one value by applying a function cumulatively. For common cases like sum or max, the built-ins are clearer.

```python
from functools import reduce
import operator

reduce(operator.mul, [1, 2, 3, 4])  # 24
```

## 162: Why should you use functools.wraps in decorators?

Without it, the wrapper replaces the original function's `__name__`, `__doc__`, `__module__` and other metadata. That breaks logging, docs, debugging and tools that inspect functions. `@wraps(func)` copies that metadata and sets `__wrapped__` to the original.

## 163: How do you write a decorator that takes arguments?

Add one more level of function: the outer one takes the arguments and returns the actual decorator.

```python
import functools, time

def retry(times=3, delay=0.5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(times=5)
def fetch():
    ...
```

## 164: What is a class decorator?

A decorator applied to a class. It gets the class and returns a class (often the same one, changed). `@dataclass` is a class decorator. They are a simpler option than metaclasses for many tasks.

```python
REGISTRY = {}

def register(cls):
    REGISTRY[cls.__name__] = cls
    return cls

@register
class EmailHandler:
    pass
```

## 165: What is a property?

`@property` lets you expose a method as an attribute. You can add a setter for validation without changing how callers use the class.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("negative balance")
        self._balance = value
```

## 166: What is functools.cached_property?

It runs a method once on first access and stores the result on the instance, so later accesses are plain attribute reads. It needs the instance to have a `__dict__`, so it doesn't work with `__slots__` unless you add `__dict__` to them.

```python
from functools import cached_property

class Report:
    @cached_property
    def rows(self):
        return load_rows_from_db()
```

## 167: What are dunder (magic) methods?

Methods with double underscores on both sides, like `__init__`, `__len__`, `__add__` or `__eq__`. Python calls them for built-in operations: `len(x)` calls `x.__len__()`, `a + b` calls `a.__add__(b)`. Defining them lets your classes work with operators and built-ins.

## 168: How do you make a class support the + operator?

Define `__add__`. Return `NotImplemented` for types you don't support so Python can try the other side's `__radd__`.

```python
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.cents + other.cents)
```

## 169: How do you make objects comparable and sortable?

Define `__eq__` and `__lt__` (and others), or define `__eq__` plus one ordering method and use `functools.total_ordering` to fill the rest. A dataclass with `order=True` also does it.

```python
from dataclasses import dataclass

@dataclass(order=True)
class Version:
    major: int
    minor: int

sorted([Version(1, 2), Version(1, 0)])
```

## 170: Why does defining eq make a class unhashable?

If you define `__eq__` without `__hash__`, Python sets `__hash__` to `None`. That is because objects that are equal must have the same hash, and the default hash (by identity) would break that rule. If your object is immutable, define `__hash__` based on the same fields as `__eq__`; a dataclass with `frozen=True` does this for you.

## 171: How do you make a class iterable?

Define `__iter__`. The easiest way is to make it a generator.

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        yield from self.songs

for s in Playlist(["a", "b"]):
    print(s)
```

## 172: How do you make a class work with len() and indexing?

Define `__len__` and `__getitem__`. With `__getitem__`, you can also support slices by checking for a `slice` object.

```python
class Deck:
    def __init__(self):
        self.cards = list(range(52))

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]
```

## 173: What does the call method do?

Defining `__call__` makes instances callable like functions. It is useful for objects that hold config or state and then act like a function.

```python
class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

triple = Multiplier(3)
triple(4)  # 12
```

## 174: How do you write a context manager with a class?

Define `__enter__` and `__exit__`. `__exit__` gets the exception info (or `None`s). Returning `True` from it swallows the exception.

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False

with Timer() as t:
    sum(range(10**6))
print(t.elapsed)
```

## 175: How do you write a context manager with contextlib?

Use `@contextmanager` on a generator that yields once. Code before `yield` is setup, code after is cleanup. Put the cleanup in `finally` so it runs on errors.

```python
from contextlib import contextmanager
import os

@contextmanager
def chdir_temp(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)
```

Python 3.11 added `contextlib.chdir`, which does exactly this.

## 176: What other contextlib helpers are useful?

- `suppress(*exceptions)` ignores given exceptions.
- `ExitStack` manages a dynamic number of context managers.
- `closing(obj)` calls `obj.close()` at the end.
- `nullcontext()` is a do-nothing context manager.
- `redirect_stdout` sends prints to another stream.

```python
from contextlib import suppress, ExitStack
import os

with suppress(FileNotFoundError):
    os.remove("tmp.txt")

with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
```

## 177: What is an abstract base class?

An ABC (from the `abc` module) defines methods that subclasses must implement. You can't create an instance of a class that still has abstract methods.

```python
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, key: str, data: bytes) -> None: ...

class S3Storage(Storage):
    def save(self, key, data):
        ...
```

## 178: What is typing.Protocol?

A `Protocol` describes the methods an object must have, without requiring inheritance. This is structural typing ("duck typing" that the type checker understands).

```python
from typing import Protocol

class Closeable(Protocol):
    def close(self) -> None: ...

def shutdown(items: list[Closeable]) -> None:
    for item in items:
        item.close()
```

Any class with a `close()` method matches. Add `@runtime_checkable` if you need `isinstance` checks.

## 179: What is duck typing?

"If it walks like a duck and quacks like a duck, it is a duck." Python code usually cares whether an object has the needed methods, not what its class is. For example, anything with a `read()` method can be used where a file is expected.

## 180: What is multiple inheritance and the MRO?

A class can inherit from several parents. Python decides the lookup order with the method resolution order (MRO), computed with the C3 algorithm. You can see it with `ClassName.__mro__` or `ClassName.mro()`. `super()` follows the MRO, not just the direct parent.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
D.__mro__  # D, B, C, A, object
```

## 181: What is a mixin?

A mixin is a small class that adds one piece of behavior and is meant to be combined with other classes through multiple inheritance. It usually has no `__init__` of its own.

```python
import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class User(JsonMixin):
    def __init__(self, name):
        self.name = name
```

## 182: What is composition and why is it often preferred over inheritance?

Composition means an object holds other objects and delegates work to them, instead of inheriting from them. It keeps classes small, avoids deep hierarchies and makes it easy to swap parts in tests.

```python
class OrderService:
    def __init__(self, repo, mailer):
        self.repo = repo
        self.mailer = mailer
```

## 183: What is slots?

Defining `__slots__` tells Python the fixed set of attributes a class has. Instances then don't get a `__dict__`, which saves memory and makes attribute access a bit faster. You can't add new attributes that aren't listed.

```python
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y
```

`@dataclass(slots=True)` creates slots for you.

## 184: What useful options does dataclass have?

- `frozen=True`: immutable instances, and hashable
- `slots=True`: use `__slots__`
- `kw_only=True`: all fields keyword-only
- `order=True`: adds comparison methods
- `field(default_factory=...)`: mutable defaults
- `__post_init__`: run checks after the generated `__init__`

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    host: str
    port: int = 8000
    tags: tuple[str, ...] = ()
```

## 185: How do you validate fields in a dataclass?

Use `__post_init__`, which runs right after the generated `__init__`.

```python
from dataclasses import dataclass

@dataclass
class Range:
    low: int
    high: int

    def __post_init__(self):
        if self.low > self.high:
            raise ValueError("low must be <= high")
```

For lots of input validation (like API payloads), a library like Pydantic is more convenient.

## 186: What is Pydantic used for?

Pydantic validates and converts data using type hints. It is used a lot in FastAPI and for settings. It parses input, coerces types where it makes sense, and gives clear errors.

```python
from pydantic import BaseModel, EmailStr

class SignUp(BaseModel):
    email: EmailStr
    age: int

data = SignUp.model_validate({"email": "a@b.com", "age": "30"})
data.age  # 30 (int)
```

`EmailStr` needs the extra `pydantic[email]` package.

## 187: What is an Enum?

`enum.Enum` defines a set of named constant values. Members are unique objects you compare with `is` or `==`.

```python
from enum import Enum, StrEnum, auto

class Status(StrEnum):
    ACTIVE = auto()   # 'active'
    BANNED = auto()

class Color(Enum):
    RED = 1
    GREEN = 2

Status("active") is Status.ACTIVE  # True
```

`StrEnum` and `IntEnum` members also behave like `str` and `int`. `Flag` supports bitwise combos.

## 188: How do you write generic functions and classes with the new syntax?

Since Python 3.12 you can declare type parameters in square brackets, without importing `TypeVar`.

```python
def first[T](items: list[T]) -> T:
    return items[0]

class Box[T]:
    def __init__(self, value: T):
        self.value = value

type Pair[K, V] = tuple[K, V]
```

The `type` statement creates a type alias.

## 189: What is TypedDict?

`TypedDict` describes the keys and value types of a plain dict, which is useful for JSON data. At runtime it is still a normal dict.

```python
from typing import TypedDict, NotRequired

class UserPayload(TypedDict):
    id: int
    name: str
    email: NotRequired[str]
```

Python 3.15 adds `closed` and `extra_items` options (PEP 728) to control what other keys are allowed.

## 190: What are Literal, Final and ClassVar?

- `Literal["a", "b"]`: the value must be one of these exact values.
- `Final`: the name must not be reassigned.
- `ClassVar`: an attribute that belongs to the class, not instances (dataclasses skip it).

```python
from typing import Literal, Final

Mode = Literal["r", "w"]
MAX_RETRIES: Final = 3

def open_file(path: str, mode: Mode) -> None: ...
```

## 191: How do you type hint a callable?

Use `collections.abc.Callable[[arg types], return type]`.

```python
from collections.abc import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

For decorators that keep the wrapped function's signature, use `ParamSpec` (shown in the advanced section).

## 192: What is the difference between typing.List and list in type hints?

Since Python 3.9, built-in types support subscripting, so write `list[int]`, `dict[str, int]`, `tuple[int, ...]`. `typing.List`, `typing.Dict` and so on are old aliases, now deprecated. Also import abstract types like `Iterable` and `Mapping` from `collections.abc`.

## 193: What are mypy and Pyright?

They are static type checkers. They read your type hints and report mismatches without running the code. mypy is the original one; Pyright is fast and powers Pylance in VS Code. Newer Rust-based checkers like ty (from Astral) and Pyrefly (from Meta) also exist. Run one in CI to catch bugs early.

## 194: What is Ruff?

Ruff is a very fast linter and formatter written in Rust. It replaces Flake8, isort, pyupgrade, many plugins and (with `ruff format`) Black, in one tool configured in `pyproject.toml`.

```bash
ruff check . --fix
ruff format .
```

## 195: What is pyproject.toml?

It is the standard config file for Python projects. It holds project metadata (name, version, dependencies), the build backend, and settings for tools like Ruff, pytest and mypy.

```toml
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["httpx>=0.27", "pydantic>=2"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
```

## 196: What is uv?

uv is a fast Python package and project manager from Astral, written in Rust. It can install Python versions, create virtual environments, resolve and lock dependencies (`uv.lock`), and run commands in the project environment. It replaces pip, pip-tools, virtualenv and pyenv for many teams.

```bash
uv init myapp
uv add fastapi
uv run pytest
uv python install 3.14
```

## 197: What is the difference between a wheel and a source distribution?

A source distribution (sdist, `.tar.gz`) contains source code and must be built on install. A wheel (`.whl`) is already built and just gets unpacked, so it installs much faster. Packages with C extensions ship separate wheels for each platform and Python version.

## 198: What is an editable install?

`pip install -e .` (or `uv pip install -e .`) installs your project so that Python imports it from your source folder. Changes to the code take effect without reinstalling. It is common during development.

## 199: How does Python find modules on import?

It checks `sys.modules` (the cache) first. If the module isn't there, it searches the folders in `sys.path` in order: the script's folder, `PYTHONPATH` entries, the standard library, and `site-packages`. The first match is loaded, run once and cached.

## 200: What is a circular import and how do you fix it?

It happens when module A imports B and B imports A. One of them sees a partly loaded module and you get `ImportError` or `AttributeError`. Fixes:

- Move shared code into a third module.
- Import inside the function that needs it.
- Import the module (`import a`) instead of names (`from a import x`).
- For type hints only, import under `if TYPE_CHECKING:`.

## 201: What does all do in a module?

`__all__` is a list of names that `from module import *` exports. It also tells readers and tools what the public API is. Names not in it can still be imported directly.

```python
__all__ = ["connect", "Client"]
```

## 202: What is the difference between absolute and relative imports?

Absolute imports use the full path from the project root: `from app.db import session`. Relative imports use dots from the current package: `from .db import session`, `from ..utils import slug`. Relative imports only work inside packages, not in a file run as a script. PEP 8 prefers absolute imports.

## 203: How do you use the logging module?

Get a logger per module, and configure handlers once at app startup.

```python
import logging

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    logger.info("starting")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("math failed")  # logs the traceback
```

## 204: Why use logging instead of print?

Logging has levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), timestamps, logger names, and can send output to files, stdout or external services. You can change verbosity without editing code. `print` has none of that and mixes with normal output.

## 205: Why should you pass arguments to a logger instead of using an f-string?

`logger.debug("user %s", user_id)` only builds the string if the message will actually be logged. An f-string is always built, even when DEBUG is off. Also, tools that group log messages work better when the message template stays the same.

## 206: How do you write tests with pytest?

Write functions starting with `test_` in files named `test_*.py`, and use plain `assert`. pytest shows detailed diffs when an assert fails.

```python
# test_math.py
import pytest
from mymath import divide

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

Run with `pytest` or `pytest -k divide -x`.

## 207: What are pytest fixtures?

Fixtures provide setup data or resources to tests. A test asks for one by naming it as a parameter. Code after `yield` is teardown. Scope controls how often a fixture is created.

```python
import pytest

@pytest.fixture
def db():
    conn = make_test_db()
    yield conn
    conn.close()

def test_insert(db):
    db.insert({"id": 1})
    assert db.count() == 1
```

Put shared fixtures in `conftest.py`.

## 208: What is pytest.mark.parametrize?

It runs one test with several sets of inputs.

```python
import pytest

@pytest.mark.parametrize("text,expected", [
    ("hello", 5),
    ("", 0),
    ("ab", 2),
])
def test_len(text, expected):
    assert len(text) == expected
```

## 209: How do you mock things in tests?

Use `unittest.mock`. `patch` replaces an object for the length of a test, at the place where it is looked up.

```python
from unittest.mock import patch

# app/weather.py does: import httpx; httpx.get(...)
@patch("app.weather.httpx.get")
def test_temp(mock_get):
    mock_get.return_value.json.return_value = {"temp": 20}
    assert get_temp("Paris") == 20
    mock_get.assert_called_once()
```

pytest's built-in `monkeypatch` fixture is another option for setting attributes and env vars.

## 210: What is the difference between Mock and MagicMock?

`Mock` creates attributes and methods on demand and records calls. `MagicMock` also supports magic methods like `__len__`, `__iter__` and `__enter__`, so it works with `len()`, loops and `with`. `AsyncMock` is for async functions. `create_autospec` or `spec=` makes the mock match a real object's API so typos fail.

## 211: What is unittest?

It is the built-in test framework, based on JUnit style classes. You subclass `unittest.TestCase` and use methods like `assertEqual`. pytest can run unittest tests too, and most new projects use pytest because it needs less boilerplate.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
```

## 212: How do you measure test coverage?

Use `coverage.py`, usually through the `pytest-cov` plugin.

```bash
pytest --cov=app --cov-report=term-missing
```

High coverage doesn't mean good tests, but low coverage shows code that is never exercised.

## 213: How do you debug Python code?

Call `breakpoint()` to drop into `pdb` at that line. Common commands: `n` (next), `s` (step into), `c` (continue), `p expr` (print), `l` (list code), `w` (stack), `q` (quit). IDEs like VS Code and PyCharm give a visual debugger with the same features. Since 3.14 you can attach pdb to a running process with `python -m pdb -p PID`.

## 214: How do you measure how long code takes?

Use `time.perf_counter()` for one-off timing and `timeit` for small snippets, because it runs the code many times.

```python
import timeit

timeit.timeit("sum(range(1000))", number=10_000)
```

From the shell: `python -m timeit "sum(range(1000))"`.

## 215: How do you profile a Python program?

`cProfile` shows how much time each function takes.

```bash
python -m cProfile -s cumtime app.py
```

Python 3.15 adds the `profiling` package: `profiling.tracing` (the same as cProfile) and `profiling.sampling`, a low-overhead sampling profiler that can attach to a running process. Third-party tools like py-spy and Scalene are also popular.

## 216: What is itertools and what are its most useful functions?

`itertools` has fast building blocks for working with iterators:

- `chain`, `islice`, `cycle`, `repeat`, `count`
- `groupby`, `accumulate`, `pairwise`, `batched`
- `product`, `permutations`, `combinations`
- `takewhile`, `dropwhile`, `zip_longest`

```python
from itertools import islice, count

list(islice(count(10, 5), 3))  # [10, 15, 20]
```

## 217: How does itertools.groupby work?

It groups consecutive items with the same key. The input must be sorted by that key first, otherwise the same key shows up in several groups.

```python
from itertools import groupby

rows = sorted(orders, key=lambda o: o["status"])
for status, group in groupby(rows, key=lambda o: o["status"]):
    print(status, len(list(group)))
```

## 218: How do you split a list into chunks?

Use `itertools.batched` (Python 3.12+). It yields tuples. Since 3.13, `strict=True` raises an error if the last batch is short.

```python
from itertools import batched

for chunk in batched(range(10), 4):
    print(chunk)
# (0, 1, 2, 3) (4, 5, 6, 7) (8, 9)
```

## 219: What does yield from do?

`yield from iterable` yields every item from another iterable or generator. With a sub-generator, it also passes `send()` and `throw()` through and returns the sub-generator's return value.

```python
def walk(tree):
    yield tree.value
    for child in tree.children:
        yield from walk(child)
```

## 220: What does the send() method on a generator do?

`gen.send(value)` resumes a generator and makes the paused `yield` expression evaluate to `value`. You must start the generator with `next()` (or `send(None)`) first.

```python
def averager():
    total = count = 0
    avg = None
    while True:
        value = yield avg
        total += value
        count += 1
        avg = total / count

g = averager()
next(g)
g.send(10)  # 10.0
g.send(20)  # 15.0
```

## 221: How do you write an iterator class by hand?

Define `__iter__` returning `self`, and `__next__` that returns the next value or raises `StopIteration`.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

## 222: What is exception chaining?

When you raise a new exception inside `except`, Python links the original one as `__context__` and shows both tracebacks. `raise New() from err` sets `__cause__` and says the new error was directly caused by the old one. `raise New() from None` hides the original.

```python
try:
    config = json.loads(text)
except json.JSONDecodeError as err:
    raise ConfigError("bad config file") from err
```

## 223: What are exception groups and except*?

`ExceptionGroup` (Python 3.11+) holds several exceptions at once, which happens with concurrent tasks. `except*` handles matching exceptions inside a group, and the rest keep going up.

```python
try:
    raise ExceptionGroup("many", [ValueError("a"), TypeError("b")])
except* ValueError as eg:
    print("values:", eg.exceptions)
except* TypeError as eg:
    print("types:", eg.exceptions)
```

## 224: How do you add notes to an exception?

Call `err.add_note("...")` (Python 3.11+). The note is printed under the traceback. It is useful for adding context like a file name or row number without changing the exception type.

```python
try:
    parse(row)
except ValueError as err:
    err.add_note(f"row number {i}")
    raise
```

## 225: What is the EAFP style?

"Easier to ask forgiveness than permission." In Python it is common to just try an operation and handle the exception, instead of checking first (LBYL, "look before you leap"). EAFP avoids race conditions, like a file being deleted between the check and the open.

```python
try:
    value = cache[key]
except KeyError:
    value = cache[key] = compute(key)
```

## 226: What is the warnings module?

`warnings` lets code warn about things that aren't errors, like deprecated APIs. Warnings can be filtered, shown once, or turned into errors (`python -W error`), which is a good setting in tests. Since 3.13 there is a `@warnings.deprecated` decorator that also tells type checkers.

```python
import warnings

warnings.warn("use new_api() instead", DeprecationWarning, stacklevel=2)
```

## 227: How do you use regular expressions in Python?

Use the `re` module. Compile patterns you use often.

```python
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
EMAIL.findall("mail ana@x.com or bo@y.org")

m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-11")
m.group("year")  # '2026'

re.sub(r"\s+", " ", "a   b    c")  # 'a b c'
```

## 228: What is the difference between re.match, re.search and re.fullmatch?

`re.match` only matches at the start of the string. `re.search` finds the first match anywhere. `re.fullmatch` requires the whole string to match, which is what you want for validation.

## 229: How do you read and write CSV files?

Use the `csv` module. Open the file with `newline=""`.

```python
import csv

with open("users.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["email"])

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name"])
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Ana"})
```

## 230: How do you read a TOML file?

Use `tomllib` (Python 3.11+). It only reads; open the file in binary mode.

```python
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
print(data["project"]["name"])
```

## 231: How do you use SQLite from Python?

The built-in `sqlite3` module. Always use placeholders for values to avoid SQL injection.

```python
import sqlite3

with sqlite3.connect("app.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES (?)", ("Ana",))
    for row in conn.execute("SELECT id, name FROM users"):
        print(row)
```

The `with` block commits or rolls back the transaction but doesn't close the connection.

## 232: How do you run a shell command from Python?

Use `subprocess.run`. Pass arguments as a list to avoid shell injection.

```python
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    capture_output=True, text=True, check=True,
)
print(result.stdout)
```

`check=True` raises `CalledProcessError` on a non-zero exit code. Avoid `shell=True` with user input.

## 233: How do you work with environment variables and config?

Read them with `os.environ`. For apps, load them once into a settings object. `pydantic-settings` is popular for typed settings, and `python-dotenv` loads a local `.env` file in development.

```python
import os

DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
DATABASE_URL = os.environ["DATABASE_URL"]  # fail fast if missing
```

## 234: How do you handle time zones?

Use `zoneinfo` (Python 3.9+) with timezone-aware datetimes. Store and compare times in UTC, and convert to local time only for display.

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

now = datetime.now(timezone.utc)
tokyo = now.astimezone(ZoneInfo("Asia/Tokyo"))
```

## 235: How do you parse and do math with dates?

Use `datetime.fromisoformat`, `strptime` and `timedelta`.

```python
from datetime import datetime, timedelta

d = datetime.fromisoformat("2026-11-25T10:00:00+00:00")
deadline = d + timedelta(days=7)
(deadline - d).days  # 7
datetime.strptime("25/11/2026", "%d/%m/%Y")
```

## 236: What is the Decimal type for?

`decimal.Decimal` does exact base-10 math with controllable precision and rounding. Use it for money. Create it from strings, not floats, to avoid carrying float errors.

```python
from decimal import Decimal, ROUND_HALF_UP

price = Decimal("19.99")
total = (price * 3).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

## 237: What is pickle and why is it risky?

`pickle` serializes almost any Python object to bytes and back. It is fast and convenient, but loading pickle data can run arbitrary code. Never unpickle data from an untrusted source. For data exchange, use JSON, MessagePack or Protocol Buffers.

## 238: How do you make an object JSON serializable?

`json.dumps` only knows basic types. Pass a `default` function for others, or convert to a dict first.

```python
import json
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Event:
    name: str
    at: datetime

def encode(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"can't serialize {type(obj)}")

json.dumps(asdict(Event("deploy", datetime.now())), default=encode)
```

## 239: How do you use heapq?

`heapq` turns a list into a min-heap. It is useful for priority queues and for "top N" problems.

```python
import heapq

tasks = []
heapq.heappush(tasks, (2, "write"))
heapq.heappush(tasks, (1, "plan"))
heapq.heappop(tasks)   # (1, 'plan')

heapq.nlargest(3, [5, 1, 9, 7, 3])  # [9, 7, 5]
```

Python 3.14 added max-heap functions like `heapq.heappush_max`.

## 240: What is bisect used for?

`bisect` finds positions in a sorted list with binary search, and `insort` inserts while keeping it sorted.

```python
import bisect

scores = [10, 20, 30, 40]
bisect.bisect_left(scores, 25)  # 2
bisect.insort(scores, 25)
```

The `key` parameter is supported since 3.10.

## 241: How do you sort by multiple keys?

Return a tuple from the key function. To reverse one key, negate a number or sort in two stable passes.

```python
users.sort(key=lambda u: (u["team"], -u["score"]))

from operator import itemgetter
users.sort(key=itemgetter("team", "name"))
```

## 242: What are operator.itemgetter and attrgetter?

They create fast functions that get an item or attribute. They are often used as sort keys.

```python
from operator import attrgetter, itemgetter

sorted(users, key=attrgetter("last_name", "first_name"))
get_ids = itemgetter("id")
```

## 243: What are template strings (t-strings)?

Python 3.14 added t-strings (PEP 750). They look like f-strings but start with `t`, and instead of a `str` they produce a `string.templatelib.Template` object that keeps the static parts and the values separately. Libraries can then escape values safely, for example for HTML or SQL.

```python
from string.templatelib import Template, Interpolation
from html import escape

def html(t: Template) -> str:
    out = []
    for part in t:
        if isinstance(part, Interpolation):
            out.append(escape(str(part.value)))
        else:
            out.append(part)
    return "".join(out)

name = "<script>"
html(t"<p>{name}</p>")  # '<p>&lt;script&gt;</p>'
```

## 244: What is the difference between threads, processes and async in Python?

- Threads share memory and are good for I/O-bound work. On the default build, the GIL lets only one thread run Python code at a time.
- Processes have separate memory and each has its own interpreter, so they can use all CPU cores for CPU-bound work.
- Async (asyncio) runs many tasks in one thread, switching at `await` points. It is best for lots of concurrent network I/O.

## 245: What is the GIL?

The Global Interpreter Lock is a mutex in CPython that allows only one thread to run Python bytecode at a time. It makes the interpreter simpler and single-threaded code fast, but limits CPU-bound threads. It is released during blocking I/O and in many C extensions. Since Python 3.14, the free-threaded build (without the GIL) is officially supported, though the default build still has it.

## 246: How do you use concurrent.futures?

It gives a simple pool API for threads and processes.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

urls = ["https://example.com", "https://example.org"]

with ThreadPoolExecutor(max_workers=8) as pool:
    futures = {pool.submit(httpx.get, u): u for u in urls}
    for fut in as_completed(futures):
        print(futures[fut], fut.result().status_code)
```

Swap in `ProcessPoolExecutor` for CPU-heavy work.

## 247: How do you start a thread?

```python
import threading

def worker(n):
    print("working on", n)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

Use `daemon=True` for background threads that shouldn't block program exit.

## 248: How do you share data safely between threads?

Use a `threading.Lock` around shared changes, or pass data through a `queue.Queue`, which is thread-safe. Even `counter += 1` is not atomic, since it is several bytecode steps.

```python
import threading

lock = threading.Lock()
counter = 0

def add():
    global counter
    with lock:
        counter += 1
```

## 249: How do you use multiprocessing?

```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool() as pool:
        print(pool.map(square, range(10)))
```

The `if __name__ == "__main__":` guard is required with the `spawn` start method (the default on Windows and macOS, and the default on Linux since 3.14 is `forkserver`), because child processes import the main module.

## 250: What is async and await?

`async def` defines a coroutine function. Calling it returns a coroutine object that does nothing until awaited or scheduled. `await` pauses the coroutine until the awaited thing is done, letting the event loop run other tasks in the meantime.

```python
import asyncio

async def fetch(n):
    await asyncio.sleep(1)
    return n

async def main():
    results = await asyncio.gather(fetch(1), fetch(2), fetch(3))
    print(results)  # takes about 1 second, not 3

asyncio.run(main())
```

## 251: What is the difference between asyncio.gather and TaskGroup?

`asyncio.TaskGroup` (Python 3.11+) is the newer, safer option. If one task fails, it cancels the others and raises an `ExceptionGroup`. With `gather`, other tasks keep running after a failure unless you handle it yourself.

```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch(1))
        t2 = tg.create_task(fetch(2))
    print(t1.result(), t2.result())
```

## 252: How do you add a timeout to async code?

Use `asyncio.timeout` (3.11+) as a context manager, or `asyncio.wait_for`.

```python
import asyncio

async def main():
    try:
        async with asyncio.timeout(2):
            await slow_call()
    except TimeoutError:
        print("too slow")
```

## 253: What happens if you call a blocking function inside async code?

It blocks the whole event loop, so every other task stops until it returns. Common culprits: `time.sleep`, `requests.get`, heavy CPU work, sync database drivers. Use async libraries (`httpx`, `asyncpg`), or move the blocking call to a thread with `asyncio.to_thread`.

```python
data = await asyncio.to_thread(read_big_file, path)
```

## 254: How do you make HTTP requests in Python?

`requests` is the classic sync library. `httpx` supports both sync and async with a similar API. Reuse a client so connections are pooled, and always set a timeout.

```python
import httpx

with httpx.Client(timeout=10) as client:
    r = client.get("https://api.github.com/repos/python/cpython")
    r.raise_for_status()
    print(r.json()["stargazers_count"])

async with httpx.AsyncClient() as client:
    r = await client.get("https://example.com")
```

## 255: What is the difference between WSGI and ASGI?

WSGI is the older standard interface between Python web apps and servers. It is synchronous: one request per worker thread at a time. ASGI is the async successor; it supports async views, WebSockets and long-lived connections. Flask and classic Django use WSGI (served by Gunicorn), FastAPI and Starlette use ASGI (served by Uvicorn, Hypercorn or Granian). Django supports both.

## 256: What are the main Python web frameworks?

- Django: full-stack, with ORM, admin, auth, migrations and templates.
- Flask: small and flexible, you choose the extras.
- FastAPI: async-first API framework built on Starlette and Pydantic, with automatic OpenAPI docs.
- Others: Litestar, Starlette, Sanic, Tornado.

## 257: What does a basic FastAPI endpoint look like?

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemIn(BaseModel):
    name: str
    price: float

@app.post("/items", status_code=201)
async def create_item(item: ItemIn):
    return {"id": 1, **item.model_dump()}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404)
    return {"id": 1}
```

Run it with `fastapi dev main.py` or `uvicorn main:app`.

## 258: What does a basic Flask app look like?

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.post("/echo")
def echo():
    return request.get_json()

if __name__ == "__main__":
    app.run(debug=True)
```

## 259: What is an ORM, and which ones are common in Python?

An ORM maps database tables to classes and rows to objects, so you query with Python code instead of raw SQL. Common ones are SQLAlchemy (the most used outside Django), the Django ORM, SQLModel (SQLAlchemy plus Pydantic), Tortoise ORM and Peewee.

```python
from sqlalchemy import String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)

with Session(engine) as session:
    user = session.scalars(select(User).where(User.email == "a@b.com")).first()
```

## 260: What is the N+1 query problem in an ORM?

You load a list of N objects with one query, then access a relationship on each, which fires one more query per object. Fix it with eager loading: `select_related` / `prefetch_related` in Django, or `selectinload` / `joinedload` in SQLAlchemy.

```python
from sqlalchemy.orm import selectinload

stmt = select(User).options(selectinload(User.orders))
```

## 261: How do you run background jobs in a Python web app?

For simple fire-and-forget tasks, FastAPI's `BackgroundTasks` runs work after the response. For real jobs (retries, scheduling, running on other machines), use a task queue: Celery, RQ, Dramatiq or arq, with Redis or RabbitMQ as the broker. Django 6.0 also added a built-in tasks framework with pluggable backends.

## 262: What are Gunicorn and Uvicorn?

Gunicorn is a production WSGI server that runs several worker processes. Uvicorn is an ASGI server. A common setup used to be Gunicorn managing Uvicorn workers; today Uvicorn can manage its own workers (`uvicorn app:app --workers 4`). Put a reverse proxy or load balancer in front for TLS and static files.

## 263: How do you handle signals and graceful shutdown?

Use the `signal` module to react to SIGTERM (sent by Docker and Kubernetes) and finish current work before exiting.

```python
import signal, sys

running = True

def stop(signum, frame):
    global running
    running = False

signal.signal(signal.SIGTERM, stop)

while running:
    process_next_job()
sys.exit(0)
```

In asyncio, use `loop.add_signal_handler` instead. Web servers like Uvicorn and Gunicorn already handle this.

## 264: How do you read a large file without loading it into memory?

Iterate the file object line by line, or read in fixed-size chunks.

```python
def chunks(path, size=1024 * 1024):
    with open(path, "rb") as f:
        while chunk := f.read(size):
            yield chunk

import hashlib
h = hashlib.sha256()
for c in chunks("big.iso"):
    h.update(c)
```

## 265: How do you build a data pipeline with generators?

Chain generators so each step handles one item at a time. Memory stays flat no matter how big the input is.

```python
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        yield from f

def parse(lines):
    for line in lines:
        yield line.rstrip().split(",")

def only_errors(rows):
    return (r for r in rows if r[1] == "ERROR")

for row in only_errors(parse(read_lines("app.log"))):
    print(row)
```

## 266: How do you use the tempfile module?

It creates temporary files and folders that are cleaned up for you.

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    p = Path(tmp) / "data.txt"
    p.write_text("hi")
# folder is deleted here
```

## 267: How do you copy, move and delete files and folders?

Use `shutil` for higher-level file operations and `pathlib` for single files.

```python
import shutil
from pathlib import Path

shutil.copy2("a.txt", "backup/a.txt")
shutil.copytree("src", "dist", dirs_exist_ok=True)
shutil.move("old.log", "archive/")
shutil.rmtree("build")
Path("tmp.txt").unlink(missing_ok=True)
```

Python 3.14 added `Path.copy()` and `Path.move()` too.

## 268: What is structural pattern matching good for beyond simple values?

It can match by shape: sequences, dict keys, class attributes, and add guards.

```python
def handle(event):
    match event:
        case {"type": "click", "x": int(x), "y": int(y)}:
            return f"click at {x},{y}"
        case {"type": "key", "key": str(k)} if k.isupper():
            return f"shift key {k}"
        case [first, *rest]:
            return f"batch of {len(rest) + 1}"
        case _:
            return "unknown"
```

## 269: How do class patterns work in match?

`ClassName(attr=pattern)` checks `isinstance` and then the attributes. Positional patterns use the class's `__match_args__`, which dataclasses set for you.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def where(p):
    match p:
        case Point(0, 0):
            return "origin"
        case Point(x=0):
            return "on y axis"
        case Point():
            return "somewhere"
```

## 270: What is the difference between match and a dict of functions?

For dispatching on a single value, a dict of handlers is short and easy to extend at runtime. `match` is better when you need to look at the structure of data, pull values out, or use guards. Don't use `match` as a plain switch on strings if a dict is clearer.

## 271: What are frozenset and frozendict?

`frozenset` is an immutable, hashable set. `frozendict` is a new built-in in Python 3.15 (PEP 814): an immutable mapping that is hashable when its values are. Both can be used as dict keys or set items, and are safe to share as constants. On older versions, `types.MappingProxyType` gives a read-only view of a dict.

```python
allowed = frozenset({"GET", "POST"})
defaults = frozendict(host="localhost", port=8000)  # 3.15+
```

## 272: How do you make a read-only dict on Python versions before 3.15?

Wrap it in `types.MappingProxyType`. It is a live read-only view: changes to the original dict show through, but you can't change it through the proxy.

```python
from types import MappingProxyType

_settings = {"debug": False}
SETTINGS = MappingProxyType(_settings)
SETTINGS["debug"] = True  # TypeError
```

## 273: What are lazy imports in Python 3.15?

PEP 810 adds the `lazy` soft keyword. A lazy import binds the name right away, but the module is only loaded the first time the name is used. This can cut startup time for CLIs and big apps.

```python
lazy import json
lazy from decimal import Decimal

def save(data):
    return json.dumps(data)  # json loads here, on first use
```

Errors such as a missing module show up at first use instead of at the import line. Lazy imports are only allowed at module level, not inside functions or `try` blocks.

## 274: What is the difference between str.format, % formatting and f-strings?

All three format strings. `%` is the oldest (`"%s is %d" % (name, age)`), `str.format` came next (`"{} is {}".format(name, age)`), and f-strings are the newest and fastest to read and run. Use f-strings in new code. `%` style is still used in logging calls, and `str.format` is handy when the template is stored separately from the values.

## 275: How do you pad, align and truncate strings?

```python
f"{'id':<6}|"      # 'id    |'
f"{'id':>6}|"      # '    id|'
f"{'id':^6}|"      # '  id  |'
f"{'long text':.4}"  # 'long'
"7".zfill(3)       # '007'
```

`textwrap.shorten` cuts text at word boundaries and adds a placeholder.

## 276: What is the difference between sorted(dict) and sorting dict items?

`sorted(d)` returns a sorted list of keys. To sort by value, sort the items.

```python
scores = {"ana": 3, "bo": 9, "cy": 5}
sorted(scores)                                   # ['ana', 'bo', 'cy']
sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
dict(sorted(scores.items(), key=lambda kv: kv[1]))
```

## 277: What is the difference between dict.setdefault and defaultdict?

`setdefault(key, default)` returns the value for `key`, inserting `default` first if it is missing. It works on any dict, but the default object is created on every call even if not needed. `defaultdict` only calls the factory when a key is actually missing.

```python
groups = {}
groups.setdefault("a", []).append(1)
```

## 278: What is the Counter class good for?

`Counter` counts hashable items and supports math between counters.

```python
from collections import Counter

c = Counter("mississippi")
c.most_common(2)        # [('i', 4), ('s', 4)]
c["z"]                  # 0, no KeyError
Counter(a=3) - Counter(a=1)  # Counter({'a': 2})
c.total()               # 11
```

## 279: How do you compare two lists for differences?

Use sets if order and duplicates don't matter. Use `Counter` if duplicates matter. Use `difflib` for a human-readable diff.

```python
old, new = ["a", "b", "c"], ["b", "c", "d"]
set(new) - set(old)  # {'d'} added
set(old) - set(new)  # {'a'} removed
```

## 280: What is the difference between a shallow copy of a dict and dict(d)?

They are the same: `d.copy()`, `dict(d)` and `{**d}` all make a shallow copy. Nested lists or dicts inside are still shared. Use `copy.deepcopy` when you need nested objects copied too.

## 281: How do you call a parent method when overriding a property?

Use `super()` on the property, or call the parent's getter through the class.

```python
class Base:
    @property
    def name(self):
        return "base"

class Child(Base):
    @property
    def name(self):
        return super().name + "-child"
```

## 282: What is the difference between getattr, setattr and hasattr?

They work with attributes by name, as strings. `getattr(obj, "x", default)` reads, `setattr(obj, "x", value)` writes, `hasattr(obj, "x")` checks, and `delattr` deletes. They are useful when the attribute name comes from data, like a config or a dispatcher.

```python
handler = getattr(self, f"handle_{event_type}", self.handle_unknown)
handler(event)
```

## 283: What is the getattr method on a class?

`__getattr__` is called only when normal attribute lookup fails. It is often used for proxies and wrappers. Don't confuse it with `__getattribute__`, which runs for every attribute access and is much easier to break.

```python
class Proxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        return getattr(self._target, name)
```

## 284: What is a module-level getattr?

A module can define a `__getattr__(name)` function (PEP 562). It is called when someone accesses a name the module doesn't have. Libraries use it for lazy loading and for deprecation warnings on old names.

```python
# mylib/__init__.py
import warnings

def __getattr__(name):
    if name == "old_func":
        warnings.warn("use new_func", DeprecationWarning, stacklevel=2)
        from .core import new_func
        return new_func
    raise AttributeError(name)
```

## 285: What is Self in type hints?

`typing.Self` (3.11+) means "an instance of the current class". It is used for methods that return `self` or create a new instance, and it works correctly in subclasses.

```python
from typing import Self

class Query:
    def where(self, cond: str) -> Self:
        self.conds.append(cond)
        return self
```

## 286: What is typing.overload?

`@overload` describes several call signatures for one function, so type checkers know the return type depends on the input. You write the stubs, then one real implementation without `@overload`.

```python
from typing import overload

@overload
def load(raw: bytes) -> dict: ...
@overload
def load(raw: None) -> None: ...
def load(raw):
    return None if raw is None else json.loads(raw)
```

## 287: How do you avoid runtime cost from type-only imports?

Put them under `if TYPE_CHECKING:`. Type checkers see the import, but it doesn't run at runtime. This also helps avoid circular imports. Since Python 3.14, annotations are evaluated lazily, so you no longer need to quote those names in annotations.

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models import User

def greet(user: User) -> str:
    return f"hi {user.name}"
```

## 288: What changed with annotations in Python 3.14?

PEP 649 and PEP 749 made annotations lazy. They are stored as code and only evaluated when someone asks for them, for example with `annotationlib.get_annotations()`. This means forward references work without quotes, and imports used only in annotations cost nothing at definition time. `from __future__ import annotations` is no longer needed for that and will be deprecated later.

## 289: What does the functools.singledispatch decorator do?

It turns a function into a generic function that picks an implementation based on the type of the first argument. `singledispatchmethod` does the same for methods.

```python
from functools import singledispatch

@singledispatch
def to_text(obj):
    return str(obj)

@to_text.register
def _(obj: list):
    return ", ".join(map(to_text, obj))

@to_text.register
def _(obj: float):
    return f"{obj:.2f}"
```

## 290: What is the difference between is and == for small integers and strings?

CPython caches small ints (-5 to 256) and interns some strings, so `a is b` can be `True` for equal values by accident. For other values it is `False`. Since this is an implementation detail, never use `is` to compare numbers or strings; Python even gives a `SyntaxWarning` for `x is 1`.

## 291: How do you write a simple CLI app with subcommands?

Use `argparse` with subparsers, or a library like Typer or Click.

```python
import argparse

parser = argparse.ArgumentParser(prog="tool")
sub = parser.add_subparsers(dest="cmd", required=True)

add = sub.add_parser("add")
add.add_argument("name")

sub.add_parser("list")

args = parser.parse_args()
if args.cmd == "add":
    print("adding", args.name)
```

## 292: How do you hash passwords in Python?

Never store plain passwords or use a fast hash like SHA-256 for them. Use a slow, salted password hash: Argon2 (`argon2-cffi`), bcrypt, or `hashlib.scrypt` from the standard library.

```python
from argon2 import PasswordHasher

ph = PasswordHasher()
stored = ph.hash("s3cret")
ph.verify(stored, "s3cret")  # True or raises
```

## 293: How do you compare secrets safely?

Use `hmac.compare_digest` (or `secrets.compare_digest`). It takes the same time no matter where the strings differ, which prevents timing attacks on tokens and signatures.

```python
import hmac, hashlib

expected = hmac.new(key, body, hashlib.sha256).hexdigest()
if not hmac.compare_digest(expected, received_signature):
    raise PermissionError("bad signature")
```

## 294: How do you parse URLs and query strings?

Use `urllib.parse`.

```python
from urllib.parse import urlparse, parse_qs, urlencode, quote

u = urlparse("https://site.com/search?q=python&page=2")
u.netloc            # 'site.com'
parse_qs(u.query)   # {'q': ['python'], 'page': ['2']}
urlencode({"q": "a b", "page": 1})  # 'q=a+b&page=1'
quote("a/b c")      # 'a/b%20c'
```

## 295: How do you compress data in Python?

The standard library has `gzip`, `zlib`, `bz2`, `lzma`, `zipfile` and `tarfile`. Python 3.14 added the `compression` package with Zstandard support in `compression.zstd`.

```python
import gzip

with gzip.open("log.gz", "wt", encoding="utf-8") as f:
    f.write("hello\n")

from compression import zstd   # 3.14+
packed = zstd.compress(b"data" * 1000)
```

## 296: What is a UUID and how do you create one?

A UUID is a 128-bit unique id. `uuid.uuid4()` is random. Python 3.14 added `uuid.uuid7()`, which starts with a timestamp, so ids sort by creation time and work better as database primary keys.

```python
import uuid

uuid.uuid4()
uuid.uuid7()   # 3.14+
```

## 297: How do you install a specific Python version and switch between them?

Use a version manager: `uv python install 3.14`, pyenv, or the official installers. On Windows, the Python install manager (`py`) lists and runs several versions. Pin the version per project with `requires-python` in `pyproject.toml` or a `.python-version` file.

## 298: What is Jupyter and when is it used?

Jupyter notebooks mix code cells, output, charts and notes in one document. They are popular for data exploration, teaching and prototyping. They are not a good place for production code: logic should move into modules with tests.

## 299: What libraries are common for data work?

- NumPy: fast n-dimensional arrays
- pandas and Polars: tables (DataFrames)
- Matplotlib, Seaborn, Plotly: charts
- scikit-learn: classic machine learning
- PyTorch: deep learning
- DuckDB: fast SQL on local files

## 300: How do you vectorize work with NumPy instead of looping?

NumPy runs operations on whole arrays in C, which is often 10-100 times faster than a Python loop.

```python
import numpy as np

prices = np.array([10.0, 20.0, 30.0])
qty = np.array([1, 3, 2])
total = (prices * qty).sum()    # 130.0
expensive = prices[prices > 15] # array([20., 30.])
```

# Advanced Questions (301-450)

## 301: How does CPython manage memory?

Every object is a C struct that starts with a reference count and a pointer to its type. When the count drops to zero, the object is freed right away. Small objects (512 bytes or less) come from pymalloc, an allocator that keeps pools of fixed-size blocks so it doesn't call the system `malloc` for each object. A separate cyclic garbage collector handles reference cycles that refcounting can't free.

## 302: How does reference counting work and what are its limits?

Each new reference (assigning, passing to a function, putting in a list) increments the count, and dropping one decrements it. `sys.getrefcount(obj)` shows it (one higher, because of the argument). The upside is that memory is freed quickly and predictably. The downsides: every reference change costs a bit, it isn't thread-safe without a lock (one reason for the GIL), and it can't free cycles like `a.self = a`.

## 303: How does the cyclic garbage collector work?

The `gc` module tracks container objects (lists, dicts, class instances and so on). Periodically it looks at a set of tracked objects, subtracts the references that come from inside that set, and anything left with zero outside references is unreachable garbage. Historically it used three generations so young objects are checked more often. You can tune it with `gc.set_threshold`, run it with `gc.collect()`, or turn it off with `gc.disable()` in special cases (some services do this and call `gc.freeze()` before forking).

## 304: What are immortal objects?

PEP 683 (Python 3.12) made some objects immortal: `None`, `True`, `False`, small ints and some interned strings. Their reference count never changes, so the interpreter skips the work of updating it. This helps performance with many threads or subinterpreters, and avoids copy-on-write page faults after `fork` caused by refcount updates.

## 305: What is the free-threaded build of Python?

It is a CPython build without the GIL (PEP 703), so threads can run Python code on several cores at once. It was experimental in 3.13 and became officially supported (but not the default) in 3.14 (PEP 779). You install it as a separate interpreter, often called `python3.14t`. Single-threaded code runs a bit slower, and C extensions must be marked as safe for it; if an extension isn't, the GIL is turned back on at import unless you force it off.

```python
import sys
sys._is_gil_enabled()  # False on a free-threaded run
```

## 306: How does the free-threaded build stay thread-safe without the GIL?

It uses several techniques: biased reference counting (the owner thread updates a fast local count, other threads use atomic operations on a shared count), per-object locks for built-in containers like `list` and `dict`, mimalloc as the memory allocator, deferred reference counting for some objects, and immortal objects. Your own code still needs locks for compound operations; the build only keeps the interpreter's internals safe.

## 307: What are subinterpreters and how are they different from threads?

A subinterpreter is a separate Python interpreter inside the same process, with its own modules and state, and (since 3.12) its own GIL. Python 3.14 added `concurrent.interpreters` (PEP 734) and `InterpreterPoolExecutor`. They give real parallelism like processes, but start faster and use less memory. Objects can't be shared freely; you pass data through queues, and only some types can be shared.

```python
from concurrent.futures import InterpreterPoolExecutor

with InterpreterPoolExecutor() as pool:
    print(list(pool.map(pow, [2, 3], [10, 10])))
```

## 308: What is Python bytecode and how can you look at it?

CPython compiles each function to a code object containing bytecode instructions for its stack-based virtual machine. The `dis` module shows them.

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Bytecode is a CPython detail and changes between versions, which is why `.pyc` files are stored per version in `__pycache__`.

## 309: What is the specializing adaptive interpreter?

Since Python 3.11 (PEP 659), CPython watches which types actually flow through each instruction. After a few runs, it rewrites a generic instruction into a specialized one, for example `BINARY_OP` into `BINARY_OP_ADD_INT`, or a general attribute load into one that knows the exact slot. If the guess stops being true, it falls back. This is the main reason 3.11 was much faster than 3.10.

## 310: What is the CPython JIT compiler?

Since 3.13, CPython can be built with an experimental JIT. It takes hot traces of specialized micro-ops and turns them into machine code using a copy-and-patch technique: precompiled templates stitched together at runtime. It is off by default in official builds; you enable it with `PYTHON_JIT=1` when the build supports it. Speedups so far are modest and depend heavily on the workload.

## 311: What is a code object versus a function object?

A code object (`func.__code__`) holds the compiled bytecode, constants, variable names and other static info. It has no state. A function object wraps a code object and adds runtime context: globals, default values, closure cells, name and annotations. Many function objects can share one code object, for example every closure made by the same factory.

## 312: What is a frame object?

A frame holds the state of one running function call: local variables, the instruction pointer and a link to the previous frame. `sys._getframe()` and `inspect.currentframe()` give access to it. Since 3.11, CPython creates lightweight internal frames and only builds full Python frame objects when something asks for them, like a traceback or a debugger, which saves time on every call.

## 313: How are closures implemented?

Variables used by an inner function are stored in cell objects instead of normal local slots. The outer function and the inner function both reference the same cell, so changes are visible to both. You can see them in `func.__closure__` and the names in `func.__code__.co_freevars`.

```python
def outer():
    x = 1
    def inner():
        return x
    return inner

f = outer()
f.__closure__[0].cell_contents  # 1
```

## 314: How does attribute lookup work on an instance?

For `obj.name`, Python calls `type(obj).__getattribute__`, which by default does this:

1. Look up `name` in the type's MRO. If it is a data descriptor (defines `__set__` or `__delete__`), call its `__get__`.
2. Otherwise, look in `obj.__dict__`.
3. Otherwise, if the class attribute is a non-data descriptor (like a function), call its `__get__`; if it is a plain value, return it.
4. Otherwise call `__getattr__` if defined, or raise `AttributeError`.

## 315: What is a descriptor?

A descriptor is an object that defines `__get__`, `__set__` or `__delete__` and lives as a class attribute. It controls what happens when that attribute is read or written on instances. Properties, methods, `classmethod`, `staticmethod` and `__slots__` are all built on descriptors.

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()
    def __init__(self, price):
        self.price = price
```

## 316: What is the difference between data and non-data descriptors?

A data descriptor defines `__set__` or `__delete__`, and it wins over the instance `__dict__`. A non-data descriptor defines only `__get__`, and an instance attribute with the same name hides it. That is why you can override a method on one instance, and why `cached_property` (a non-data descriptor) works by writing its value into the instance dict.

## 317: How do methods become bound methods?

Functions are non-data descriptors. When you access `obj.method`, `function.__get__(obj, type)` returns a bound method object that stores the function and the instance. Calling it calls the function with the instance as the first argument. CPython optimizes `obj.method()` calls so it usually doesn't create the bound method object at all.

## 318: What does the set_name hook do?

`__set_name__(self, owner, name)` is called on a descriptor (or any class attribute) when the owning class is created. It tells the descriptor which class it belongs to and the attribute name, so you don't have to repeat the name like `price = Positive("price")`.

## 319: What is a metaclass?

A metaclass is the class of a class. Classes are created by calling their metaclass, which is `type` by default. A custom metaclass can change how a class is built: add methods, validate attributes, register the class. ORMs and frameworks have used them a lot.

```python
class Registry(type):
    classes = {}
    def __new__(mcs, name, bases, ns):
        cls = super().__new__(mcs, name, bases, ns)
        mcs.classes[name] = cls
        return cls

class Plugin(metaclass=Registry):
    pass
```

## 320: When should you use init_subclass instead of a metaclass?

`__init_subclass__` is a classmethod on a base class that runs each time a subclass is defined. It covers most metaclass uses (registering subclasses, checking required attributes, reading class keyword arguments) with much less complexity, and it doesn't cause metaclass conflicts in multiple inheritance.

```python
class Handler:
    registry = {}

    def __init_subclass__(cls, event, **kwargs):
        super().__init_subclass__(**kwargs)
        Handler.registry[event] = cls

class OnSignup(Handler, event="signup"):
    pass
```

## 321: What are the steps when Python executes a class statement?

1. Resolve the bases and pick the metaclass.
2. Call `metaclass.__prepare__` to get the namespace (a dict).
3. Run the class body in that namespace.
4. Call `metaclass(name, bases, namespace)` to create the class.
5. Call `__set_name__` on attributes that have it, then `__init_subclass__` on the parent.
6. Apply class decorators, bottom to top.

## 322: What is the difference between new and init?

`__new__` is a static method that creates and returns the new instance. `__init__` sets up an instance that already exists. You override `__new__` when subclassing immutable types (`int`, `str`, `tuple`) because their value must be set at creation, and for patterns like caching instances. If `__new__` returns an object that isn't an instance of the class, `__init__` isn't called.

```python
class Celsius(float):
    def __new__(cls, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        return super().__new__(cls, value)
```

## 323: How does the C3 linearization (MRO) work?

C3 builds the MRO by merging the parents' MROs and the list of direct bases. It keeps two rules: a class comes before its parents, and the order of bases in the class statement is kept. If no order can satisfy both, class creation fails with `TypeError: Cannot create a consistent method resolution order`. This is what makes cooperative `super()` calls predictable in diamond shapes.

## 324: What is cooperative multiple inheritance?

Every class in the hierarchy calls `super()` and passes along arguments it doesn't use, usually through `**kwargs`. That way each `__init__` in the MRO runs exactly once, even in a diamond.

```python
class Base:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Named(Base):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Aged(Base):
    def __init__(self, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)

class Person(Named, Aged):
    pass

Person(name="Ana", age=30)
```

## 325: How does super() work without arguments?

The compiler sees `super` used in a method and creates a hidden `__class__` cell with the class where the method is defined. At runtime, `super()` reads that cell and the method's first argument, and starts the lookup after that class in the instance's MRO. That is why zero-argument `super()` doesn't work in functions defined outside the class body.

## 326: How are dicts implemented in CPython?

A dict is a hash table split in two arrays: a compact array of entries (hash, key, value) in insertion order, and a smaller sparse index array pointing into it. This layout saves memory and gives ordered iteration for free. Lookups use the hash to find a slot and probe with a perturbation scheme on collision. The table resizes when about two thirds full. Instances of the same class can share keys (key-sharing dicts), which saves memory for objects with the same attributes.

## 327: Why must dict keys be hashable and what makes a good hash?

The dict stores keys by their hash and checks equality only on hash matches. If a key's hash changed after insertion, the dict could never find it again, so keys must be immutable in the parts that affect hash and equality. Equal objects must have equal hashes. A good hash spreads values evenly; the usual way is `hash((self.a, self.b))` over the same fields used in `__eq__`.

## 328: What is hash randomization?

Since Python 3.3, `str` and `bytes` hashes are salted with a random value per process. This stops attackers from sending many keys that collide on purpose and slow dict lookups to O(n) (hash flooding DoS). It also means set iteration order of strings can differ between runs. `PYTHONHASHSEED` fixes the seed for reproducible runs.

## 329: How are lists implemented, and what are their time complexities?

A list is a dynamic array of pointers to objects. It over-allocates when it grows, so `append` is amortized O(1). Indexing and `len` are O(1). `insert(0, x)`, `pop(0)` and `x in lst` are O(n). Slicing copies, so it is O(k). For a queue, use `collections.deque`.

## 330: How are strings stored in CPython?

Since PEP 393, a `str` picks the smallest storage that fits its widest character: 1 byte per char for Latin-1, 2 for the BMP, or 4 for others. So one emoji can make a long string use 4 times the memory. Strings also cache their hash. Identifiers and some literals are interned, so equal names share one object and comparisons can use identity.

## 331: What is string interning and when does it matter?

Interning keeps one shared copy of equal strings. Python interns identifiers, attribute names and many short literals automatically. You can intern strings yourself with `sys.intern()`, which saves memory and speeds up dict lookups when you have many repeated strings, for example keys parsed from a large file.

## 332: What sorting algorithm does Python use?

`list.sort` and `sorted` use Timsort, a stable hybrid of merge sort and insertion sort that finds existing runs in the data, so it is very fast on partly sorted input. Since 3.11, the rule that decides which runs to merge is Powersort's, which gives better merge orders. Worst case is O(n log n), and the best case is O(n) for sorted input.

## 333: How does sys.getsizeof differ from the real memory use of an object?

`sys.getsizeof` returns only the size of the object itself, not the objects it references. A list of 1000 strings reports roughly the pointer array, not the strings. For the real footprint, walk the references (with care for shared objects) or measure with `tracemalloc`, or tools like Pympler and memray.

## 334: How do you find a memory leak in a Python service?

1. Confirm it with metrics: memory grows and never drops after GC.
2. Use `tracemalloc` to compare snapshots and see which lines allocate the growing memory.
3. Use `gc.get_objects()` or objgraph to count objects by type and see what keeps them alive.
4. Use memray for native allocations, which often come from C extensions.

Common causes: unbounded caches (like `lru_cache` with `maxsize=None` on many keys), global lists that only grow, reference cycles with objects holding big buffers, and tracebacks holding frames.

```python
import tracemalloc

tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
run_workload()
snap2 = tracemalloc.take_snapshot()
for stat in snap2.compare_to(snap1, "lineno")[:10]:
    print(stat)
```

## 335: What are weak references and when do you use them?

A weak reference points to an object without increasing its reference count, so it doesn't keep it alive. Use them for caches and observer lists where you don't want the cache to prevent cleanup. `weakref.WeakValueDictionary`, `WeakKeyDictionary`, `WeakSet` and `weakref.finalize` are the common tools.

```python
import weakref

class Image: ...

cache = weakref.WeakValueDictionary()
img = Image()
cache["logo"] = img
del img
"logo" in cache  # False after the object is freed
```

## 336: Why can holding on to an exception cause a memory leak?

An exception has a `__traceback__`, which references every frame in the stack, and those frames reference all their local variables. Storing the exception (for example in a list of errors) keeps all of that alive. Python deletes the `as err` name at the end of the `except` block for this reason. If you need to keep errors, store the message or call `traceback.clear_frames(tb)`.

## 337: What does the del method do and what are its pitfalls?

`__del__` runs when an object is about to be destroyed. Its timing isn't guaranteed (especially with cycles or other implementations like PyPy), exceptions in it are only printed, and it can run during interpreter shutdown when modules are half torn down. Prefer context managers or `weakref.finalize` for cleanup.

## 338: How does the import system work internally?

`import x` calls `importlib`'s machinery: check `sys.modules`; if missing, ask each finder in `sys.meta_path` for a module spec; the spec's loader creates the module object, puts it in `sys.modules` before running it (which is why circular imports see a partial module), then executes the module code in its namespace. `sys.path_hooks` and `sys.path_importer_cache` handle searching file system paths.

## 339: How would you write a custom import hook?

Add a finder object with a `find_spec` method to `sys.meta_path`. It returns a `ModuleSpec` with your loader, and the loader's `exec_module` fills the module. This is how tools import modules from zip files, databases or remote sources, or rewrite code on import (pytest rewrites assert statements this way).

```python
import sys
from importlib.abc import MetaPathFinder, Loader
from importlib.util import spec_from_loader

class ConstLoader(Loader):
    def create_module(self, spec):
        return None
    def exec_module(self, module):
        module.VALUE = 42

class ConstFinder(MetaPathFinder):
    def find_spec(self, name, path, target=None):
        if name == "magic_const":
            return spec_from_loader(name, ConstLoader())
        return None

sys.meta_path.insert(0, ConstFinder())
import magic_const
print(magic_const.VALUE)
```

## 340: What are namespace packages?

A namespace package is a package without an `__init__.py` (PEP 420). Its parts can live in several folders on `sys.path`, and Python merges them into one package. This lets separate distributions install into the same top-level name, like `google.cloud.storage` and `google.cloud.pubsub`. A common bug is forgetting `__init__.py` and getting a namespace package by accident, which some tools handle differently.

## 341: What are entry points and how are they used for plugins?

Entry points are named hooks declared in package metadata. A package can register functions under a group name, and the host app finds them at runtime with `importlib.metadata.entry_points`. pytest plugins and console scripts work this way.

```toml
[project.entry-points."myapp.plugins"]
csv = "myapp_csv:CsvExporter"
```

```python
from importlib.metadata import entry_points

for ep in entry_points(group="myapp.plugins"):
    plugin = ep.load()
```

## 342: How does asyncio's event loop work?

The event loop keeps a queue of ready callbacks and a list of timers, and asks the OS selector (epoll, kqueue, IOCP) which sockets are ready. Each loop iteration runs the ready callbacks. A `Task` wraps a coroutine and drives it by calling `send()` on it; when the coroutine awaits a `Future` that isn't done, the task attaches a callback to the future and gives control back. When the future gets a result, the callback schedules the task to continue.

## 343: What is the difference between a coroutine, a Task and a Future?

A coroutine is the object returned by an `async def` function; it doesn't run until awaited or wrapped in a task. A `Future` is a low-level placeholder for a result that will be set later. A `Task` is a Future that runs a coroutine on the event loop concurrently. `asyncio.create_task(coro())` schedules it right away; `await coro()` runs it inline without concurrency.

## 344: Why must you keep a reference to tasks created with create_task?

The event loop only keeps a weak reference to tasks. If you create a task and drop the result, it can be garbage collected before it finishes. Keep tasks in a set and remove them when done, or use a `TaskGroup`.

```python
background = set()

task = asyncio.create_task(send_email(user))
background.add(task)
task.add_done_callback(background.discard)
```

## 345: How does cancellation work in asyncio?

`task.cancel()` throws `CancelledError` into the coroutine at its current `await`. The coroutine can clean up in `finally` or `except CancelledError`, but it should re-raise it; swallowing it breaks timeouts and TaskGroups. `asyncio.shield()` protects an inner operation from outer cancellation. `asyncio.timeout` uses cancellation internally and turns it into `TimeoutError`.

## 346: How do you limit concurrency in asyncio?

Use an `asyncio.Semaphore` so only N tasks run a section at once. This protects the remote service and your own resources.

```python
import asyncio, httpx

sem = asyncio.Semaphore(10)

async def fetch(client, url):
    async with sem:
        r = await client.get(url)
        return r.status_code

async def main(urls):
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(fetch(client, u)) for u in urls]
    return [t.result() for t in tasks]
```

## 347: What is backpressure and how do you handle it in Python?

Backpressure is slowing down producers when consumers can't keep up, so memory doesn't grow without limit. In asyncio, use a bounded `asyncio.Queue(maxsize=N)`: `await queue.put()` waits when it is full. With streams, `await writer.drain()` waits until the send buffer is drained. In threads, `queue.Queue(maxsize=N)` blocks producers the same way.

## 348: What are context variables?

`contextvars.ContextVar` stores values that are local to the current context. Each asyncio task runs in its own copy of the context, so a value set in one request handler doesn't leak to another. They are the async-safe replacement for thread-locals, used for request ids, current user and tracing.

```python
from contextvars import ContextVar

request_id: ContextVar[str] = ContextVar("request_id", default="-")

async def handler(req):
    request_id.set(req.headers.get("x-request-id", "none"))
    await do_work()

def log(msg):
    print(f"[{request_id.get()}] {msg}")
```

## 349: How do you call async code from sync code and sync code from async code?

From sync to async: `asyncio.run(coro())` at the top level, or `asyncio.run_coroutine_threadsafe(coro, loop)` to submit work to a loop running in another thread. From async to sync blocking code: `await asyncio.to_thread(func, *args)` or `loop.run_in_executor(pool, func)`. Don't call `asyncio.run` inside a running loop; it raises an error.

## 350: What is uvloop?

uvloop is a drop-in replacement for the asyncio event loop, built on libuv (the same library Node.js uses). It is usually 2-4 times faster for network-heavy work. Uvicorn uses it automatically when installed. You enable it with `uvloop.run(main())`.

## 351: How do async generators and async context managers work?

An `async def` function with `yield` is an async generator, used with `async for`. Async context managers define `__aenter__` and `__aexit__`, or use `contextlib.asynccontextmanager`.

```python
from contextlib import asynccontextmanager

async def ticks(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

@asynccontextmanager
async def db_session():
    conn = await pool.acquire()
    try:
        yield conn
    finally:
        await pool.release(conn)

async def main():
    async for t in ticks(3):
        print(t)
```

## 352: What is structured concurrency and why does it matter?

It means concurrent tasks have a clear owner and scope: they start inside a block and are all finished (or cancelled) when the block exits. Errors are never lost, and no task runs on after its parent is gone. In Python you get it with `asyncio.TaskGroup` or with the Trio and AnyIO libraries. Free-floating `create_task` calls are the opposite and often cause leaked tasks and silent failures.

## 353: Why is threading still useful in CPython with the GIL?

The GIL is released during blocking I/O (sockets, files, `time.sleep`) and by many C extensions (NumPy, hashlib on large data, compression). So threads give real speedups for I/O-bound work and for code that spends time in such extensions. They only fail to help with pure Python CPU-bound loops, and even that changes on the free-threaded build.

## 354: How does the GIL decide when to switch threads?

A thread holding the GIL keeps it until it blocks on I/O or until another thread asks for it and the switch interval passes (5 ms by default, see `sys.getswitchinterval()`). The waiting thread then sets a flag, and the running thread releases the GIL at the next safe point between bytecodes. Since this can happen between any two bytecodes, operations like `x += 1` are not atomic.

## 355: Which operations are atomic in CPython?

On the default build, single operations implemented in C on built-in types are effectively atomic because they hold the GIL: `list.append`, `dict[key] = value`, `dict.get`, `deque.append`. Read-modify-write sequences like `counter += 1` or `if key not in d: d[key] = ...` are not. On free-threaded builds, built-in containers use per-object locks to keep the same safety. Don't rely on this in complex code; use a lock.

## 356: How do you avoid deadlocks?

- Always take multiple locks in the same global order.
- Hold locks for as short a time as possible and never call unknown code while holding one.
- Use timeouts: `lock.acquire(timeout=5)`.
- Prefer queues and message passing over shared state.
- Use `RLock` only when the same thread really must re-enter.

To debug a hang, dump all thread stacks with `faulthandler.dump_traceback_later` or `py-spy dump --pid PID`.

## 357: What are the start methods in multiprocessing?

- `fork`: copies the parent process. Fast, but unsafe if the parent has threads (locks can be copied in a locked state). Not available on Windows.
- `spawn`: starts a fresh interpreter and imports the main module. Safe, slower to start. Default on Windows and macOS.
- `forkserver`: forks children from a clean server process. Default on Linux since 3.14.

Choose with `multiprocessing.get_context("spawn")`.

## 358: How do you share data between processes?

Processes don't share memory by default, so arguments and results are pickled and sent through pipes. For larger data, use `multiprocessing.shared_memory.SharedMemory` (works well with NumPy arrays), `multiprocessing.Value`/`Array`, a `Manager` (slower, proxied), or an external store like Redis. Keep data passed to workers small, because pickling it can cost more than the work itself.

## 359: When would you pick processes, threads, async, subinterpreters or free-threading?

- Many network calls, high concurrency: asyncio.
- Some blocking I/O, or sync libraries: threads.
- CPU-bound pure Python on the default build: processes (or subinterpreters for lighter workers).
- CPU-bound work in NumPy or other C code that releases the GIL: threads are often enough.
- CPU-bound threads with shared memory, and your dependencies support it: free-threaded build.

## 360: How do you speed up a slow CPU-bound Python function?

First profile to find the real hot spot. Then, roughly in order: pick a better algorithm or data structure; use built-ins and the standard library (they are in C); vectorize with NumPy or Polars; cache repeated work; then move the hot loop to compiled code with Cython, Numba, mypyc or a Rust extension through PyO3; finally use parallelism across cores.

## 361: What are common micro-optimizations in Python, and when do they matter?

Local variable access is faster than global or attribute access, so hot loops sometimes bind `append = out.append`. Comprehensions are faster than equivalent loops. `str.join` beats `+=` for strings. `set` lookups beat list scans. These matter only in tight loops that profiling shows are hot; the specializing interpreter already removes some of the gap.

## 362: How do C extensions work with Python?

A C extension is a shared library that uses the Python C API to define modules, functions and types. CPython loads it like a normal module. Extensions can release the GIL around long C work. Tools that make this easier: Cython (Python-like syntax compiled to C), pybind11 and nanobind (C++), PyO3 with maturin (Rust), and `ctypes` or `cffi` for calling existing C libraries without writing an extension.

## 363: What is the stable ABI (abi3)?

The limited C API is a subset of the C API that stays compatible across Python versions. Extensions built against it produce `abi3` wheels that work on the current and all later CPython versions, so maintainers don't need a new wheel per release. Python 3.15 extends stable ABI support to free-threaded builds.

## 364: What is ctypes and when would you use it?

`ctypes` calls functions in C shared libraries directly from Python, without compiling anything. It is good for small integrations with a system library. It is easy to crash the process with wrong argument types, so you must declare `argtypes` and `restype` carefully.

```python
import ctypes, ctypes.util

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.strlen.argtypes = [ctypes.c_char_p]
libc.strlen.restype = ctypes.c_size_t
libc.strlen(b"hello")  # 5
```

## 365: What is PyPy and when would you use it?

PyPy is an alternative Python implementation with a tracing JIT. Long-running, pure Python CPU-heavy code can run several times faster. Downsides: it lags behind CPython's newest versions, C extensions run slower or need special support, and startup and memory use are higher. It suits algorithmic workloads more than code that mostly calls C libraries.

## 366: What is Cython?

Cython is a language that is a superset of Python with optional C types. It compiles to a C extension. Adding types to hot loops (`cdef int i`) can make them run near C speed. It is used heavily by scientific libraries and is a common step before writing pure C or Rust.

## 367: What is mypyc?

mypyc compiles type-annotated Python modules to C extensions using the same type info as mypy. Code that is fully typed and avoids very dynamic features can run several times faster without rewriting it in another language. mypy and Black are compiled with it.

## 368: How does eval and exec work and why are they dangerous?

`eval` evaluates an expression string and `exec` runs a block of code. With untrusted input, they allow full code execution: an attacker can import `os` and run commands. Restricting `globals` and `__builtins__` doesn't make them safe; there are many escapes. To parse literal data, use `ast.literal_eval` or `json.loads`.

```python
import ast

ast.literal_eval("[1, 2, {'a': 3}]")  # safe for literals only
```

## 369: What are the main security risks in Python web apps?

- Injection: SQL (use parameters), shell (`subprocess` with lists, no `shell=True`), templates (don't render user input as a template).
- Unsafe deserialization: `pickle`, `yaml.load` (use `yaml.safe_load`), and `marshal`.
- XML attacks like billion laughs and XXE (use `defusedxml`).
- Path traversal when joining user input into paths.
- SSRF when fetching user-provided URLs.
- Secrets in code or logs.
- Vulnerable dependencies (scan with `pip-audit`).

## 370: How do you prevent path traversal when serving files?

Resolve the final path and check it stays inside the allowed folder.

```python
from pathlib import Path

BASE = Path("/srv/uploads").resolve()

def safe_path(user_name: str) -> Path:
    p = (BASE / user_name).resolve()
    if not p.is_relative_to(BASE):
        raise PermissionError("invalid path")
    return p
```

`resolve()` handles `..` and symlinks. Never trust the file name from the client.

## 371: What is ReDoS and how does it affect Python?

Regular expression denial of service: Python's `re` engine uses backtracking, and patterns with nested quantifiers like `(a+)+$` can take exponential time on crafted input. One request can lock a CPU core. Fix it by avoiding nested repeats, limiting input length, using atomic groups or possessive quantifiers (supported since 3.11), or using an engine with linear time like `google-re2`.

## 372: How do you protect against supply chain attacks with Python packages?

Pin exact versions with a lock file that includes hashes (uv, pip-tools with `--generate-hashes`, Poetry). Review new dependencies, watch for typo-squatted names, run `pip-audit` in CI, prefer trusted publishing on PyPI for your own packages, and install with `--require-hashes` in production. Avoid running `pip install` with packages from untrusted indexes.

## 373: What is ParamSpec and why is it useful for decorators?

`ParamSpec` captures the full parameter list of a function, so a decorator can say "the wrapper takes exactly the same arguments as the wrapped function". Without it, decorated functions lose their signature in type checkers.

```python
from collections.abc import Callable
import functools, time

def timed[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(func.__name__, time.perf_counter() - start)
    return wrapper
```

`Concatenate` lets you add or remove leading parameters, for example a decorator that injects a database session.

## 374: What is variance in generics?

Variance says whether `Box[Child]` can be used where `Box[Parent]` is expected. Covariant: yes (read-only containers like `Sequence`). Contravariant: the reverse (things that only take values, like a `Callable` argument). Invariant: neither (mutable containers like `list`, because you could put a different subclass in). With the 3.12 syntax, type checkers infer variance automatically; with `TypeVar` you set `covariant=True` or `contravariant=True`.

## 375: What is the difference between TypeGuard and TypeIs?

Both let a function tell the type checker that a value has a narrower type when it returns `True`. `TypeIs` (3.13) also narrows in the `False` branch and requires the narrowed type to be compatible with the input type, which is what you usually want. `TypeGuard` only narrows in the `True` branch and can narrow to unrelated types, like `list[object]` to `list[str]`.

```python
from typing import TypeIs

def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)
```

## 376: What is Annotated used for?

`Annotated[T, metadata]` attaches extra info to a type without changing it for type checkers. Libraries read the metadata at runtime. FastAPI uses it for dependencies and query parameters, and Pydantic for constraints.

```python
from typing import Annotated
from fastapi import Depends, Query

async def list_items(
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    db: Annotated[Session, Depends(get_db)] = None,
): ...
```

## 377: What are Never and NoReturn?

Both mean "this never produces a value". `NoReturn` is used for functions that always raise or exit. `Never` (3.11) is the bottom type and is also used in other places, for example in an `assert_never` check that proves all cases of a union or enum were handled.

```python
from typing import assert_never

def area(shape: Circle | Square) -> float:
    match shape:
        case Circle(): return 3.14 * shape.r ** 2
        case Square(): return shape.side ** 2
        case _: assert_never(shape)
```

## 378: What are TypeVarTuple and default type parameters?

`TypeVarTuple` (written `*Ts` in the new syntax) stands for any number of types, which is useful for typing things like array shapes or functions that forward a variable number of arguments. PEP 696 (3.13) lets type parameters have defaults, so `class Box[T = int]` means `Box` alone is `Box[int]`.

## 379: Should you validate type hints at runtime?

Normally no: hints are for static tools, and Python ignores them at runtime for speed. Validate at the edges of your system instead, where data comes in (HTTP requests, config files, queues), with Pydantic, msgspec or attrs validators. Libraries like beartype or typeguard can check hints at runtime during tests if you want that.

## 380: How do comprehensions handle scope?

A comprehension's loop variable doesn't leak into the enclosing scope. Since 3.12 (PEP 709), CPython inlines list, dict and set comprehensions into the enclosing function instead of creating a hidden function, which makes them faster, but scoping behavior stays the same. A walrus inside a comprehension, however, binds the name in the enclosing scope on purpose.

```python
data = [1, 5, 12]
if any((big := x) > 10 for x in data):
    print(big)  # 12
```

## 381: Why can't a class body variable be used inside a comprehension in the same class?

Names defined in a class body aren't visible to nested scopes, and the part of a comprehension after the first `for` runs in its own scope. So this fails:

```python
class Config:
    base = 10
    values = [base * i for i in range(3)]          # NameError
    values = [b * i for b in [base] for i in range(3)]  # works
```

Only the first iterable is evaluated in the class scope. Move the logic to a function or module level.

## 382: What happens when finally has a return statement?

A `return` in `finally` overrides any return in `try` and silently swallows an exception that was being raised. That hides bugs. Since Python 3.14 (PEP 765), `return`, `break` and `continue` that exit a `finally` block give a `SyntaxWarning`.

```python
def f():
    try:
        raise ValueError
    finally:
        return "ok"   # the ValueError disappears
```

## 383: What happens when you close a generator?

`gen.close()` raises `GeneratorExit` at the paused `yield`. `finally` blocks and `with` exits inside the generator run, so resources are freed. If the generator catches `GeneratorExit` and yields again, Python raises `RuntimeError`. Generators that aren't fully consumed are closed when garbage collected, which may be later than you expect, so close them explicitly or use `contextlib.closing` when they hold resources.

## 384: What is the classic bug with iterators being exhausted?

Iterators and generators can only be consumed once. Code that loops twice over the same generator silently gets nothing the second time.

```python
nums = (n for n in range(3))
sum(nums)   # 3
sum(nums)   # 0, already exhausted
```

The same happens with `map`, `filter`, `zip` and file objects. Convert to a list if you need several passes, or use `itertools.tee` carefully.

## 385: How is the f-string syntax different since Python 3.12?

PEP 701 moved f-strings into the real grammar. Now you can reuse the same quote type inside the braces, write backslashes and comments in expressions, and nest f-strings to any depth. Error messages also point to the right spot.

```python
names = ["a", "b"]
f"{", ".join(names)}"         # valid since 3.12
f"{'\n'.join(names)}"
```

## 386: Why were t-strings added when f-strings already exist?

f-strings turn into a plain `str` right away, so a library can't tell which parts were literal and which came from variables. That makes it easy to build SQL or HTML with injected user input. t-strings give a `Template` object, so libraries can escape or parameterize each value, or build something that isn't a string at all, like a prepared query with separate parameters. They don't have a `__str__` that renders them, so you can't use them by accident as normal strings.

## 387: How does sys.monitoring differ from sys.settrace?

`sys.settrace` calls a Python function for every line, call and return, which slows code heavily, so debuggers and coverage were slow. `sys.monitoring` (PEP 669, 3.12) lets tools subscribe only to the events they need, per code object, and switch them off once seen. coverage.py uses it to make coverage runs much faster.

## 388: What are audit hooks?

PEP 578 added `sys.addaudithook`. CPython raises audit events for sensitive operations like `open`, `subprocess.Popen`, `socket.connect`, `exec` and imports. A hook can log them or raise to block them. They are useful for security monitoring and sandbox-like checks, but they aren't a real sandbox because Python code can still do a lot.

```python
import sys

def hook(event, args):
    if event == "subprocess.Popen":
        print("spawning", args[0])

sys.addaudithook(hook)
```

## 389: How do you debug a stuck or slow Python process in production?

- `py-spy dump --pid PID` prints every thread's stack without stopping the process.
- `py-spy top` or `py-spy record` shows where CPU time goes.
- Python 3.14 lets you attach `pdb` to a running process (`python -m pdb -p PID`) through PEP 768's safe external debugger interface.
- Python 3.15's `profiling.sampling` can attach to a running process and profile it with low overhead.
- `faulthandler` dumps tracebacks on crashes or on a signal.

## 390: What is faulthandler?

`faulthandler` prints Python tracebacks for all threads when the process crashes from a segfault or similar fatal error, where a normal traceback is impossible. It can also dump stacks after a timeout or on a signal. Turn it on with `python -X faulthandler` or `PYTHONFAULTHANDLER=1`; it is cheap enough for production.

## 391: How do you reduce Python startup time?

Measure first with `python -X importtime app.py`, which shows how long each import takes. Then: import heavy modules only where needed (or with `lazy import` on 3.15), avoid work at module import time, trim unused dependencies, and make sure `.pyc` files are compiled ahead of time in Docker images. For CLIs, startup time is often most of the run time.

## 392: How does Python decide when to recompile .pyc files?

By default, the `.pyc` header stores the source file's modification time and size. On import, if they don't match, the module is recompiled. PEP 552 added hash-based `.pyc` files, which check a hash of the source instead; this gives reproducible builds. `python -m compileall` precompiles a tree, which is good for read-only containers.

## 393: How do you build a good Docker image for a Python app?

- Use a slim official base image with a pinned version (for example `python:3.14-slim`).
- Use a multi-stage build: install dependencies in one stage, copy only the virtual environment into the final one.
- Copy and install the lock file before the source code, so the dependency layer is cached.
- Set `PYTHONDONTWRITEBYTECODE=1` (or precompile), and `PYTHONUNBUFFERED=1` so logs show up right away.
- Run as a non-root user and handle SIGTERM for graceful shutdown.

## 394: What are dependency groups and inline script metadata?

PEP 735 adds `[dependency-groups]` in `pyproject.toml` for things like dev and test dependencies that aren't part of the published package. PEP 723 lets a single script declare its own dependencies in a comment block, and tools like uv and pipx install them when running it.

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
import httpx
print(httpx.get("https://example.com").status_code)
```

Run it with `uv run script.py`.

## 395: What is pylock.toml?

PEP 751 defined a standard lock file format, `pylock.toml`. Before it, each tool had its own lock format (`poetry.lock`, `uv.lock`, `requirements.txt` with hashes). The standard file lists exact versions, hashes and sources, so any compatible installer can reproduce the same environment. uv can export it, and recent pip versions can write it with `pip lock`.

## 396: How does pip resolve dependencies?

Since pip 20.3, a backtracking resolver looks for a set of versions that meets every package's requirements. If a choice leads to a conflict, it goes back and tries other versions. Loose constraints across many packages can make it slow. uv uses a faster resolver (PubGrub-based). Conflicts show up as errors instead of a silently broken environment, which is what the old pip did.

## 397: What are manylinux wheels?

Linux wheels with compiled code must work across many distributions. The manylinux tags (like `manylinux_2_28_x86_64`) promise that the wheel only depends on a glibc version at or below the one in the tag and a small set of system libraries. `auditwheel` checks this and bundles other needed libraries into the wheel. `musllinux` tags do the same for Alpine.

## 398: How do you structure a large Python application?

Use the `src/` layout so tests run against the installed package, not loose files. Split code by feature or domain (`orders/`, `billing/`) rather than by technical layer only. Keep the web framework at the edges: route handlers call services, services use repositories or clients defined as interfaces (Protocols). Keep config in one settings object, and avoid work at import time.

## 399: How do you do dependency injection in Python?

Usually just pass dependencies into constructors or functions, and wire them up at the app's entry point. Python doesn't need a heavy container. Frameworks help: FastAPI has `Depends`, and libraries like `dependency-injector` or `svcs` exist for larger apps. The main goal is that tests can pass fakes without patching module globals.

```python
class SignupService:
    def __init__(self, users: UserRepo, mailer: Mailer):
        self.users = users
        self.mailer = mailer
```

## 400: How do you implement a singleton in Python?

The simplest singleton is a module: it is imported once and cached in `sys.modules`, so module-level objects are shared. If you need a class, create one instance at module level, or cache it with `functools.cache` on a factory function. Avoid the `__new__` trick unless needed. Singletons make testing harder, so pass the instance in where you can.

```python
from functools import cache

@cache
def get_settings() -> Settings:
    return Settings()
```

## 401: Is functools.lru_cache thread-safe?

The cache's internal data structure is kept consistent across threads, so it won't get corrupted. But it doesn't stop two threads from computing the same missing value at the same time; both will run the function. If the function is expensive or has side effects, add your own lock or a per-key "in progress" marker.

## 402: Why can lru_cache on a method cause memory leaks?

`@lru_cache` on a method includes `self` in the cache key, so the cache holds a strong reference to every instance it has seen. Those instances never get freed while the cache lives (which is as long as the class). Use `cached_property` for per-instance values, put the cache on the instance, or cache a module-level function with only hashable inputs.

## 403: How do you design a retry with exponential backoff?

Retry only errors that are likely temporary (timeouts, 429, 503), cap the number of attempts, double the delay each time, and add random jitter so many clients don't retry at the same moment. Respect `Retry-After` headers. Libraries like `tenacity` and `stamina` do this well.

```python
import random, time

def call_with_retry(func, attempts=5, base=0.2, cap=10):
    for i in range(attempts):
        try:
            return func()
        except TimeoutError:
            if i == attempts - 1:
                raise
            delay = min(cap, base * 2 ** i)
            time.sleep(random.uniform(0, delay))
```

## 404: How would you implement a rate limiter in Python?

A token bucket is common: tokens refill at a fixed rate up to a max, and each request takes one. For a single process, keep the state in memory with a lock. For many workers, keep it in Redis with an atomic Lua script or a sliding window with sorted sets, so all processes share the limit.

```python
import time, threading

class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate, self.capacity = rate, capacity
        self.tokens = capacity
        self.updated = time.monotonic()
        self.lock = threading.Lock()

    def allow(self) -> bool:
        with self.lock:
            now = time.monotonic()
            self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
            self.updated = now
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False
```

## 405: Why use time.monotonic instead of time.time for measuring durations?

`time.time()` follows the system clock, which can jump forward or backward (NTP sync, manual changes, leap seconds). Durations computed from it can be negative or wrong. `time.monotonic()` never goes backward, and `time.perf_counter()` is monotonic with the highest resolution, so use them for timeouts and benchmarks.

## 406: How do datetimes handle daylight saving time transitions?

When clocks go back, a local time like 01:30 happens twice. Python uses the `fold` attribute (0 or 1) to pick which one. When clocks go forward, some local times don't exist. Doing arithmetic on aware datetimes in a local zone uses wall-clock time, which can give surprising results across a transition. Do the math in UTC and convert at the end.

## 407: How do you handle Unicode text correctly?

Decode bytes at the boundary, work with `str` inside, encode on output. Be explicit about encodings. Normalize text before comparing, because "é" can be one code point or two (`unicodedata.normalize("NFC", s)`). Use `casefold()` instead of `lower()` for case-insensitive matching. Remember that `len()` counts code points, not what a user sees as characters.

## 408: How do you configure logging for a whole application?

Configure once at startup with `logging.config.dictConfig`. Libraries should only create loggers and never add handlers (other than `NullHandler`). In production, log to stdout in JSON so the platform can collect it, and include request ids through a filter or `contextvars`.

```python
import logging.config

logging.config.dictConfig({
    "version": 1,
    "formatters": {"plain": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "plain"}},
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {"sqlalchemy.engine": {"level": "WARNING"}},
})
```

## 409: How do you log safely from multiple processes?

Writing to one file from several processes can interleave or lose lines, especially with rotation. Options: log to stdout and let the container runtime collect it; use `QueueHandler` in workers and one `QueueListener` in the main process; or send logs to syslog or a log collector. `QueueHandler` also keeps slow handlers off the request path in single-process apps.

## 410: What is property-based testing?

Instead of writing specific examples, you describe what inputs look like and what must always be true, and a library generates many inputs, including edge cases. When a test fails, it shrinks the input to the smallest failing case. In Python this is Hypothesis.

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_keeps_length(xs):
    assert len(sorted(xs)) == len(xs)

@given(st.text())
def test_roundtrip(s):
    assert s.encode("utf-8").decode("utf-8") == s
```

## 411: What are common mocking mistakes?

- Patching where the object is defined instead of where it is looked up. If `app.service` does `from app.client import fetch`, you must patch `app.service.fetch`.
- Mocks that accept any call, so a renamed method still passes. Use `autospec=True` or `create_autospec`.
- Mocking so much that the test only checks the mock setup.
- Forgetting `AsyncMock` for coroutines, so `await` fails.

For outside services, a fake in-memory version or a test container is often better than a mock.

## 412: How do you test code that depends on the current time?

Don't call `datetime.now()` deep in your logic; pass in a clock function or the current time. In tests, pass a fixed value. If you can't change the code, use a library like `time-machine` or `freezegun` to freeze time.

```python
from datetime import datetime, timezone
from collections.abc import Callable

def is_expired(expires_at: datetime, now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)) -> bool:
    return now() >= expires_at
```

## 413: How do you test async code?

Use the `pytest-asyncio` or `anyio` pytest plugin so test functions can be `async def`. Use `AsyncMock` for async dependencies, and `httpx.AsyncClient` with `ASGITransport` to call a FastAPI app in memory.

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.anyio
async def test_health():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        r = await client.get("/health")
    assert r.status_code == 200
```

## 414: How do you test code that talks to a real database?

Run the real database engine in tests (Testcontainers or a Docker Compose service), not SQLite pretending to be Postgres. Wrap each test in a transaction and roll it back at the end, or truncate tables between tests, so tests stay isolated and fast. Run migrations once per session.

## 415: How do database transactions work with SQLAlchemy sessions?

A `Session` starts a transaction on first use and keeps it until `commit()` or `rollback()`. Objects you load are tracked in the identity map, and changes are flushed as SQL before queries and on commit. Use `with Session(engine) as s, s.begin():` so the transaction commits on success and rolls back on error. Keep one session per request or unit of work, never share it between threads or tasks.

## 416: Why can database connection pools break after fork?

If a process opens connections and then forks (Gunicorn with `preload_app`, multiprocessing with `fork`), parent and child share the same sockets. Their traffic gets mixed and you see random protocol errors. Create engines and pools after the fork (in a post-fork hook), or call `engine.dispose(close=False)` in the child so it opens its own connections.

## 417: How do you make Celery tasks safe to retry?

Make them idempotent: running a task twice must give the same result as once. Use a unique key per operation and check it before doing the work (for example a payment id with a unique DB constraint). Set `acks_late=True` so tasks are re-delivered if a worker dies, and use `autoretry_for` with backoff for temporary errors. Pass ids, not whole objects, so tasks read fresh data.

## 418: How do you add caching to a Python web service?

Use layers: an in-process cache (`functools.lru_cache` or `cachetools.TTLCache`) for small, hot, rarely changing data; Redis for shared caches across workers; and HTTP caching headers for clients and CDNs. Pick a clear invalidation rule (TTL, or delete on write), and protect against cache stampedes with locks or early refresh so many workers don't recompute the same key at once.

## 419: A FastAPI endpoint is slow under load. How do you find the cause?

1. Check whether `async def` handlers call blocking code (sync DB driver, `requests`, CPU work). That blocks the event loop for every request.
2. Look at traces (OpenTelemetry) to see time spent in DB, external calls and serialization.
3. Check the DB: slow queries, N+1 queries, pool size too small (requests waiting for a connection).
4. Profile a worker with py-spy under load.
5. Check worker count and CPU limits.

Plain `def` handlers run in a thread pool, which is a quick fix when the code is blocking.

## 420: A worker process's memory keeps growing until it gets killed. What do you do?

Confirm it is a leak and not just fragmentation or a big cache (check `tracemalloc` and object counts). Compare snapshots over time to find the code that allocates. Look for unbounded module-level caches, growing lists, references held by long-lived objects or closures, and C extensions leaking (use memray with native traces). As a short-term protection, set `max_requests` in Gunicorn or `--max-tasks-per-child` in Celery so workers restart periodically.

## 421: CPU is at 100% on one core but the service is slow. What might be happening?

On the default build, a CPU-heavy task in one thread or one asyncio task blocks the others because of the GIL or the single event loop. Use `py-spy top` to find the hot function. Fixes: move CPU work to a process pool, a separate worker service, or compiled code; run more worker processes; or on free-threaded Python, use threads. Also check for accidental busy loops and regex backtracking.

## 422: How do you safely load YAML?

`yaml.load` with the default or full loader can create arbitrary Python objects from tags, which can lead to code execution. Always use `yaml.safe_load` for untrusted or even semi-trusted input; it only builds basic types. For config, TOML with `tomllib` is a simpler option.

## 423: How do you prevent SSRF when your app fetches URLs given by users?

Allow only `http` and `https`, resolve the host name, and reject private, loopback, link-local and metadata addresses (like `169.254.169.254`) using `ipaddress`. Connect to the IP you checked, so a DNS rebinding can't swap it, and disable or re-check redirects. Set short timeouts and a size limit on the response.

```python
import ipaddress, socket

def is_public(host: str) -> bool:
    for info in socket.getaddrinfo(host, None):
        ip = ipaddress.ip_address(info[4][0])
        if not ip.is_global:
            return False
    return True
```

## 424: How should you handle secrets in a Python application?

Load them from the environment or a secret manager (AWS Secrets Manager, Vault) at startup, never commit them, and never log them. Pydantic's `SecretStr` hides values in reprs and logs. Use `secrets` for generating tokens, and `hmac.compare_digest` for comparing them. Rotate secrets and keep them out of exception messages and error trackers.

## 425: What is the difference between deepcopy and pickling for cloning objects?

`copy.deepcopy` walks the object graph in memory, keeps a memo dict to handle shared references and cycles, and uses `__deepcopy__` if defined. Pickle round-tripping (`pickle.loads(pickle.dumps(x))`) also clones but is slower to write and read, and fails on objects that can't be pickled, like locks and lambdas. For simple data, explicit construction (`dataclasses.replace`, a dict comprehension) is clearer and faster than both.

## 426: How do you customize pickling for a class?

Define `__getstate__` and `__setstate__` to control what is saved and how it is restored, for example to skip a lock or an open connection. `__reduce__` gives full control by returning a callable and its arguments. Python 3.11 added a default `object.__getstate__`.

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["lock"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.lock = threading.Lock()
```

## 427: What is the buffer protocol and memoryview?

The buffer protocol lets objects like `bytes`, `bytearray`, `array.array` and NumPy arrays expose their raw memory to other code without copying. `memoryview` is the Python way to use it: slicing a memoryview doesn't copy, which matters for large binary data like network packets or file chunks.

```python
data = bytearray(b"hello world")
view = memoryview(data)
part = view[6:]        # no copy
part[0] = ord("W")
print(data)            # bytearray(b'hello World')
```

## 428: How do generators compare with lists for memory and speed?

A list holds every item in memory at once, while a generator holds only its paused frame. For large or infinite data, generators use near constant memory. For small data that you go through several times, a list is often faster, because each generator step has overhead and you'd have to rebuild the generator anyway. Choose based on size and how many passes you need.

## 429: How do you implement the observer or event pattern in Python?

Keep a list of callbacks per event name and call them when the event fires. Use weak references if subscribers shouldn't be kept alive by the emitter. For async code, gather the coroutine callbacks.

```python
from collections import defaultdict

class Events:
    def __init__(self):
        self._handlers = defaultdict(list)

    def on(self, name, handler):
        self._handlers[name].append(handler)

    def emit(self, name, *args):
        for handler in list(self._handlers[name]):
            handler(*args)

bus = Events()
bus.on("signup", lambda user: print("welcome", user))
bus.emit("signup", "ana")
```

## 430: What is the Liskov substitution principle and how does it apply in Python?

A subclass should work anywhere its parent is used, without surprises. In Python that means overrides should accept at least the same arguments, return compatible types, and not raise new kinds of errors for valid input. Type checkers flag incompatible overrides. A common violation is a subclass that raises `NotImplementedError` for a method callers rely on; that usually means the hierarchy is wrong.

## 431: How do you make a class immutable?

Use `@dataclass(frozen=True)` or `NamedTuple`. For a regular class, define `__slots__` and block `__setattr__` and `__delattr__`, setting values with `object.__setattr__` in `__init__`. Python can't stop all mutation (a determined caller can still call `object.__setattr__`), and attributes that hold lists can still be changed in place, so use tuples and frozensets inside.

## 432: How is attrs different from dataclasses?

attrs came before dataclasses and inspired them. It has more features: validators and converters on fields, slots by default with `@define`, better performance options, and more control over equality and hashing. Dataclasses are in the standard library and enough for most cases. Use attrs (or msgspec and Pydantic for serialization-heavy code) when you need those extra features.

## 433: What is msgspec and when would you use it over Pydantic?

msgspec is a fast serialization and validation library for JSON and MessagePack. Its `Struct` types are very cheap to create and decode, often several times faster than Pydantic, with lower memory use. It has fewer features for complex validation and settings. It fits high-throughput services where decoding and encoding are a real cost.

## 434: How does class getitem work?

`__class_getitem__` is a classmethod called when you subscript a class, like `MyList[int]`. It lets classes support generic syntax without a metaclass. `typing.Generic` and built-ins like `list` use it to return generic alias objects. You rarely write it yourself; with the 3.12 syntax `class Box[T]:` you get it automatically.

## 435: What is the difference between an abstract property and a regular abstract method?

You can stack `@property` on top of `@abstractmethod` to require subclasses to provide an attribute. Subclasses can satisfy it with a property or with a class attribute of the same name. The order matters: `@property` must be the outer decorator.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def sides(self) -> int: ...

class Triangle(Shape):
    sides = 3
```

## 436: Why is chaining classmethod and property no longer supported?

Python 3.9 allowed `@classmethod` to wrap other descriptors like `@property` to make "class properties". It caused subtle bugs and was deprecated in 3.11 and removed in 3.13. Use a metaclass property, a plain class attribute, or a small custom descriptor whose `__get__` uses the owner class.

## 437: How do you write a plugin system with abstract base classes and entry points together?

Define the interface as an ABC or Protocol in your core package. Plugins implement it in separate packages and register through an entry point group. At startup, load the entry points, check that each loaded class matches the interface, and keep them in a registry keyed by name. Handle import errors per plugin so one broken plugin doesn't take down the app.

## 438: What happens when you modify a list while iterating over it?

The loop uses an index internally, so removing items shifts later items and skips some; adding items can make the loop run forever. For dicts and sets, changing the size during iteration raises `RuntimeError`. Loop over a copy (`for x in items[:]`), or build a new list with a comprehension.

```python
nums = [1, 2, 2, 3]
nums = [n for n in nums if n != 2]
```

## 439: What is the difference between str and repr when logging exceptions?

`str(err)` gives just the message, which can be empty (for example `KeyError` shows only the key, and `TimeoutError()` shows nothing). `repr(err)` includes the type. In logs, use `logger.exception(...)` inside `except` to get the full traceback, or `%r` for the error object, so you never end up with a blank error line.

## 440: How do you handle very deep recursion?

Rewrite it as a loop with an explicit stack; that is the reliable fix. You can raise the limit with `sys.setrecursionlimit`, but deep C stacks can still crash the process. Since 3.12, pure Python-to-Python calls don't use the C stack in the same way, so the risk is lower, but recursion through C code (like `repr` of a deep structure) can still overflow.

```python
def walk(root):
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        stack.extend(node.children)
```

## 441: How does Python's integer type handle very large numbers efficiently?

Ints are stored as arrays of 30-bit "digits" with a sign. Small ints fit in one digit and have fast paths. Big multiplications use Karatsuba for large sizes. Conversions between int and decimal strings are quadratic for huge numbers, which is why Python limits them to 4300 digits by default (a defense against DoS). Use `hex()` or `int.to_bytes` for huge values if you need speed.

## 442: How would you design a module that must work on several Python versions?

Set `requires-python` to the lowest supported version and test every version in CI (for example with `nox` or `tox`). Use feature checks like `sys.version_info >= (3, 15)` or `try/except ImportError` to pick newer APIs. `typing_extensions` gives newer typing features on older versions. Avoid new syntax (like `lazy import`, `except A, B` without parentheses, or the `type` statement) that won't even parse on older versions.

## 443: What does the dis module show you that helps with performance questions?

It shows the bytecode, including specialized instructions after warm-up (`dis.dis(func, adaptive=True)`). You can see why one version is slower, for example a global lookup in a loop (`LOAD_GLOBAL`) versus a local (`LOAD_FAST`), or extra attribute loads. It is a learning and debugging tool; real decisions should still come from profiling and benchmarks.

## 444: How do you benchmark code fairly in Python?

Use `timeit` or `pyperf` instead of a single `time.time()` call. Warm up first so the specializing interpreter settles, run many loops, report the median and spread, and keep the machine quiet. Test realistic input sizes. Compare on the Python version you deploy, because results change between versions.

## 445: What are the trade-offs of using asyncio for a database-heavy service?

Async helps when you have many concurrent requests waiting on I/O: one process can handle thousands of open connections. But the database itself is often the bottleneck, so async doesn't make queries faster, and pool size still limits throughput. Async drivers and ORMs add complexity, and one blocking call stalls everything. For a moderate number of requests, sync code with threads is simpler and just as fast.

## 446: How do you share state between asyncio and threads safely?

asyncio objects are not thread-safe. From another thread, use `loop.call_soon_threadsafe(callback)` or `asyncio.run_coroutine_threadsafe(coro, loop)` to hand work to the loop. Use a `queue.Queue` for thread-to-thread, and from async code read it through `asyncio.to_thread(q.get)`. Never `await` an `asyncio.Future` from a thread other than the loop's.

## 447: What does gc.freeze do and why do some services use it?

`gc.freeze()` moves all current tracked objects into a permanent generation that the collector ignores. Pre-fork servers call it in the parent after loading the app. Then the children don't touch those objects during GC, which avoids writing to shared memory pages and copying them (copy-on-write). This saves a lot of memory per worker. Instagram popularized this approach.

## 448: How do you safely run untrusted Python code?

You can't do it safely inside the same interpreter: restricted `exec`, audit hooks and removed builtins can all be escaped. Run it in a separate process inside a real sandbox: a container or microVM (gVisor, Firecracker), with no network, a read-only file system, CPU and memory limits and a timeout. WebAssembly builds of Python (Pyodide, WASI) are another isolation option.

## 449: What were the main changes in Python 3.14 and 3.15?

Python 3.14: template strings (t-strings), lazy evaluation of annotations, official support for the free-threaded build, `concurrent.interpreters`, Zstandard in `compression.zstd`, `except` without parentheses, warnings for control flow in `finally`, remote debugger attach, `uuid7`, and `forkserver` as the Linux default for multiprocessing.

Python 3.15: explicit lazy imports with `lazy import`, the `frozendict` built-in, UTF-8 as the default encoding, the `profiling` package with a sampling profiler, typed extra items for `TypedDict`, an improved JIT, and stable ABI support for free-threaded builds.

## 450: What makes Python code "Pythonic"?

It uses the language's own idioms instead of copying patterns from other languages: iterate directly instead of using indexes, use comprehensions, context managers, unpacking, `enumerate` and `zip`, rely on duck typing and EAFP, prefer simple functions and modules over deep class hierarchies, and follow PEP 8. Above all it is easy to read, because code is read much more often than it is written.
