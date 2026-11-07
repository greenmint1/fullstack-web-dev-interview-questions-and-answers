# JavaScript Data Structures Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions about data structures in JavaScript, split into three levels: 150 easy, 150 moderate and 150 advanced. The answers use modern JavaScript up to ES2025 (`Map`, `Set` and its new methods, `WeakMap`, `WeakRef`, typed arrays, iterator helpers, `Object.groupBy`, `toSorted()` and friends), plus a few newer features that already work in current browsers. Classic structures like stacks, queues, linked lists, trees, heaps, tries and graphs are written by hand, because JavaScript doesn't ship them. Algorithm questions (sorting, searching, dynamic programming) live in a separate file, so this one sticks to how data is stored and why.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is a data structure?](#1-what-is-a-data-structure)
- [2: Why should a front-end developer know data structures?](#2-why-should-a-front-end-developer-know-data-structures)
- [3: What is the difference between primitive and reference types?](#3-what-is-the-difference-between-primitive-and-reference-types)
- [4: What data structures does JavaScript give you out of the box?](#4-what-data-structures-does-javascript-give-you-out-of-the-box)
- [5: What is an array in JavaScript?](#5-what-is-an-array-in-javascript)
- [6: Are JavaScript arrays real arrays like in C?](#6-are-javascript-arrays-real-arrays-like-in-c)
- [7: What is the time complexity of common array operations?](#7-what-is-the-time-complexity-of-common-array-operations)
- [8: What is the difference between push and unshift?](#8-what-is-the-difference-between-push-and-unshift)
- [9: What is the difference between pop and shift?](#9-what-is-the-difference-between-pop-and-shift)
- [10: What is a sparse array?](#10-what-is-a-sparse-array)
- [11: What happens when you change an array's length property?](#11-what-happens-when-you-change-an-arrays-length-property)
- [12: What does at() do?](#12-what-does-at-do)
- [13: What are the different ways to create an array?](#13-what-are-the-different-ways-to-create-an-array)
- [14: How do you create an array of n items filled with values?](#14-how-do-you-create-an-array-of-n-items-filled-with-values)
- [15: What goes wrong with new Array(3).fill({})?](#15-what-goes-wrong-with-new-array3fill)
- [16: How do you create a 2D array (grid)?](#16-how-do-you-create-a-2d-array-grid)
- [17: How do you copy an array?](#17-how-do-you-copy-an-array)
- [18: What is the difference between a shallow copy and a deep copy?](#18-what-is-the-difference-between-a-shallow-copy-and-a-deep-copy)
- [19: What is structuredClone?](#19-what-is-structuredclone)
- [20: Why is JSON.parse(JSON.stringify(obj)) a weak way to deep copy?](#20-why-is-jsonparsejsonstringifyobj-a-weak-way-to-deep-copy)
- [21: Which array methods mutate the array and which don't?](#21-which-array-methods-mutate-the-array-and-which-dont)
- [22: What are toSorted, toReversed, toSpliced and with?](#22-what-are-tosorted-toreversed-tospliced-and-with)
- [23: Why does [10, 1, 2].sort() give [1, 10, 2]?](#23-why-does-10-1-2sort-give-1-10-2)
- [24: What is the difference between find, findIndex, findLast and findLastIndex?](#24-what-is-the-difference-between-find-findindex-findlast-and-findlastindex)
- [25: What is the difference between includes and indexOf?](#25-what-is-the-difference-between-includes-and-indexof)
- [26: How do you check if a value is an array?](#26-how-do-you-check-if-a-value-is-an-array)
- [27: How do you swap two items in an array?](#27-how-do-you-swap-two-items-in-an-array)
- [28: How do plain objects work as a data structure?](#28-how-do-plain-objects-work-as-a-data-structure)
- [29: What is the difference between dot notation and bracket notation?](#29-what-is-the-difference-between-dot-notation-and-bracket-notation)
- [30: What do Object.keys, Object.values and Object.entries return?](#30-what-do-objectkeys-objectvalues-and-objectentries-return)
- [31: What does Object.fromEntries do?](#31-what-does-objectfromentries-do)
- [32: How do you check if an object has a property?](#32-how-do-you-check-if-an-object-has-a-property)
- [33: Why is Object.hasOwn better than obj.hasOwnProperty?](#33-why-is-objecthasown-better-than-objhasownproperty)
- [34: What does the delete operator do?](#34-what-does-the-delete-operator-do)
- [35: What types can object keys be?](#35-what-types-can-object-keys-be)
- [36: In what order are object keys listed?](#36-in-what-order-are-object-keys-listed)
- [37: What does Object.freeze do?](#37-what-does-objectfreeze-do)
- [38: What is the difference between freeze, seal and preventExtensions?](#38-what-is-the-difference-between-freeze-seal-and-preventextensions)
- [39: How do you safely read deeply nested data?](#39-how-do-you-safely-read-deeply-nested-data)
- [40: How do you set a default for a missing value in a data structure?](#40-how-do-you-set-a-default-for-a-missing-value-in-a-data-structure)
- [41: What is a Map?](#41-what-is-a-map)
- [42: When should you use a Map instead of a plain object?](#42-when-should-you-use-a-map-instead-of-a-plain-object)
- [43: What are the main methods of a Map?](#43-what-are-the-main-methods-of-a-map)
- [44: How do you loop over a Map?](#44-how-do-you-loop-over-a-map)
- [45: How do you convert between a Map and an object?](#45-how-do-you-convert-between-a-map-and-an-object)
- [46: How does a Map compare keys?](#46-how-does-a-map-compare-keys)
- [47: Why does map.get({ id: 1 }) return undefined after map.set({ id: 1 }, "x")?](#47-why-does-mapget-id-1--return-undefined-after-mapset-id-1--x)
- [48: What is a Set?](#48-what-is-a-set)
- [49: What are the main methods of a Set?](#49-what-are-the-main-methods-of-a-set)
- [50: How do you remove duplicates from an array?](#50-how-do-you-remove-duplicates-from-an-array)
- [51: Why doesn't a Set remove duplicate objects?](#51-why-doesnt-a-set-remove-duplicate-objects)
- [52: Does a Set keep the order of items?](#52-does-a-set-keep-the-order-of-items)
- [53: What is a WeakMap?](#53-what-is-a-weakmap)
- [54: What is a WeakSet?](#54-what-is-a-weakset)
- [55: Why can't you loop over a WeakMap or check its size?](#55-why-cant-you-loop-over-a-weakmap-or-check-its-size)
- [56: What is a stack?](#56-what-is-a-stack)
- [57: How do you implement a stack in JavaScript?](#57-how-do-you-implement-a-stack-in-javascript)
- [58: Where do stacks show up in front-end work?](#58-where-do-stacks-show-up-in-front-end-work)
- [59: What is the call stack?](#59-what-is-the-call-stack)
- [60: What causes "Maximum call stack size exceeded"?](#60-what-causes-maximum-call-stack-size-exceeded)
- [61: What is a queue?](#61-what-is-a-queue)
- [62: Why is using an array with shift() a slow queue?](#62-why-is-using-an-array-with-shift-a-slow-queue)
- [63: Where do queues show up in front-end work?](#63-where-do-queues-show-up-in-front-end-work)
- [64: What is the difference between a stack and a queue?](#64-what-is-the-difference-between-a-stack-and-a-queue)
- [65: What is a deque?](#65-what-is-a-deque)
- [66: What is a linked list?](#66-what-is-a-linked-list)
- [67: How do you write a linked list node in JavaScript?](#67-how-do-you-write-a-linked-list-node-in-javascript)
- [68: What is the difference between a singly and a doubly linked list?](#68-what-is-the-difference-between-a-singly-and-a-doubly-linked-list)
- [69: When would you pick a linked list over an array?](#69-when-would-you-pick-a-linked-list-over-an-array)
- [70: How do you loop over a linked list?](#70-how-do-you-loop-over-a-linked-list)
- [71: How do you add a node to the start of a linked list?](#71-how-do-you-add-a-node-to-the-start-of-a-linked-list)
- [72: What is a tree?](#72-what-is-a-tree)
- [73: What do root, leaf, parent, child, depth and height mean in a tree?](#73-what-do-root-leaf-parent-child-depth-and-height-mean-in-a-tree)
- [74: Why is the DOM a tree?](#74-why-is-the-dom-a-tree)
- [75: What is a binary tree?](#75-what-is-a-binary-tree)
- [76: What is a binary search tree (BST)?](#76-what-is-a-binary-search-tree-bst)
- [77: How do you represent a general tree in JavaScript?](#77-how-do-you-represent-a-general-tree-in-javascript)
- [78: What is a graph?](#78-what-is-a-graph)
- [79: What is the difference between a directed and an undirected graph?](#79-what-is-the-difference-between-a-directed-and-an-undirected-graph)
- [80: What is a weighted graph?](#80-what-is-a-weighted-graph)
- [81: What are the two common ways to store a graph?](#81-what-are-the-two-common-ways-to-store-a-graph)
- [82: Where do graphs show up in web development?](#82-where-do-graphs-show-up-in-web-development)
- [83: What is a hash table?](#83-what-is-a-hash-table)
- [84: What is a hash function?](#84-what-is-a-hash-function)
- [85: What is a hash collision?](#85-what-is-a-hash-collision)
- [86: Are JavaScript objects and Maps hash tables?](#86-are-javascript-objects-and-maps-hash-tables)
- [87: What is a heap?](#87-what-is-a-heap)
- [88: What is the difference between a min heap and a max heap?](#88-what-is-the-difference-between-a-min-heap-and-a-max-heap)
- [89: What is a priority queue?](#89-what-is-a-priority-queue)
- [90: What is a trie?](#90-what-is-a-trie)
- [91: What is a matrix and how do you store one in JavaScript?](#91-what-is-a-matrix-and-how-do-you-store-one-in-javascript)
- [92: Is a string a data structure?](#92-is-a-string-a-data-structure)
- [93: What does it mean that strings are immutable?](#93-what-does-it-mean-that-strings-are-immutable)
- [94: How do you turn a string into an array of characters correctly?](#94-how-do-you-turn-a-string-into-an-array-of-characters-correctly)
- [95: Does JavaScript have tuples?](#95-does-javascript-have-tuples)
- [96: What happened to the Records and Tuples proposal?](#96-what-happened-to-the-records-and-tuples-proposal)
- [97: What is JSON?](#97-what-is-json)
- [98: What is the difference between JSON and a JavaScript object?](#98-what-is-the-difference-between-json-and-a-javascript-object)
- [99: What does JSON.stringify skip or change?](#99-what-does-jsonstringify-skip-or-change)
- [100: How do you save a Map or Set as JSON?](#100-how-do-you-save-a-map-or-set-as-json)
- [101: What is an iterable?](#101-what-is-an-iterable)
- [102: Which built-in types are iterable?](#102-which-built-in-types-are-iterable)
- [103: What is the difference between for...of and for...in?](#103-what-is-the-difference-between-forof-and-forin)
- [104: What does the spread operator work on?](#104-what-does-the-spread-operator-work-on)
- [105: What is an array-like object and how do you turn it into an array?](#105-what-is-an-array-like-object-and-how-do-you-turn-it-into-an-array)
- [106: What is the difference between a NodeList and an HTMLCollection?](#106-what-is-the-difference-between-a-nodelist-and-an-htmlcollection)
- [107: What is a typed array?](#107-what-is-a-typed-array)
- [108: What is an ArrayBuffer?](#108-what-is-an-arraybuffer)
- [109: What is the difference between a normal array and a typed array?](#109-what-is-the-difference-between-a-normal-array-and-a-typed-array)
- [110: What is a Symbol and why use one as an object key?](#110-what-is-a-symbol-and-why-use-one-as-an-object-key)
- [111: What is the difference between mutable and immutable data?](#111-what-is-the-difference-between-mutable-and-immutable-data)
- [112: Why do React and Redux want you to update state immutably?](#112-why-do-react-and-redux-want-you-to-update-state-immutably)
- [113: How do you update a nested object without mutating it?](#113-how-do-you-update-a-nested-object-without-mutating-it)
- [114: How do you add, remove and update items in an array without mutating it?](#114-how-do-you-add-remove-and-update-items-in-an-array-without-mutating-it)
- [115: How do you choose the right data structure for a task?](#115-how-do-you-choose-the-right-data-structure-for-a-task)
- [116: What does Object.groupBy do?](#116-what-does-objectgroupby-do)
- [117: How is Map.groupBy different from Object.groupBy?](#117-how-is-mapgroupby-different-from-objectgroupby)
- [118: What do flat and flatMap do?](#118-what-do-flat-and-flatmap-do)
- [119: How do you count how many times each value appears?](#119-how-do-you-count-how-many-times-each-value-appears)
- [120: How can you use an object or Map as a lookup table instead of a switch?](#120-how-can-you-use-an-object-or-map-as-a-lookup-table-instead-of-a-switch)
- [121: How do you turn an array of objects into an object keyed by id?](#121-how-do-you-turn-an-array-of-objects-into-an-object-keyed-by-id)
- [122: What is a dictionary (associative array)?](#122-what-is-a-dictionary-associative-array)
- [123: How do you build a simple cache?](#123-how-do-you-build-a-simple-cache)
- [124: What operations does a stack usually have?](#124-what-operations-does-a-stack-usually-have)
- [125: What is a circular buffer (ring buffer)?](#125-what-is-a-circular-buffer-ring-buffer)
- [126: What new methods does Set have?](#126-what-new-methods-does-set-have)
- [127: What is the difference between difference and symmetricDifference?](#127-what-is-the-difference-between-difference-and-symmetricdifference)
- [128: How do you check if an array or object is empty?](#128-how-do-you-check-if-an-array-or-object-is-empty)
- [129: What does splice do?](#129-what-does-splice-do)
- [130: What is the difference between slice and splice?](#130-what-is-the-difference-between-slice-and-splice)
- [131: What is the difference between concat and spread for joining arrays?](#131-what-is-the-difference-between-concat-and-spread-for-joining-arrays)
- [132: What is the difference between a Map's size and an object's key count?](#132-what-is-the-difference-between-a-maps-size-and-an-objects-key-count)
- [133: How do you empty a Map or a Set?](#133-how-do-you-empty-a-map-or-a-set)
- [134: Why is [] === [] false?](#134-why-is----false)
- [135: How do you compare two objects by their content?](#135-how-do-you-compare-two-objects-by-their-content)
- [136: What is the difference between linear and non-linear data structures?](#136-what-is-the-difference-between-linear-and-non-linear-data-structures)
- [137: What is the difference between static and dynamic data structures?](#137-what-is-the-difference-between-static-and-dynamic-data-structures)
- [138: What is an abstract data type (ADT)?](#138-what-is-an-abstract-data-type-adt)
- [139: What is a node in a data structure?](#139-what-is-a-node-in-a-data-structure)
- [140: Does JavaScript have pointers?](#140-does-javascript-have-pointers)
- [141: How does garbage collection decide what to free?](#141-how-does-garbage-collection-decide-what-to-free)
- [142: How can a Map cause a memory leak?](#142-how-can-a-map-cause-a-memory-leak)
- [143: What is the difference between null and an empty structure?](#143-what-is-the-difference-between-null-and-an-empty-structure)
- [144: How do you loop over an object's keys and values?](#144-how-do-you-loop-over-an-objects-keys-and-values)
- [145: How do you transform all values of an object?](#145-how-do-you-transform-all-values-of-an-object)
- [146: How do you create a Map from an array of pairs?](#146-how-do-you-create-a-map-from-an-array-of-pairs)
- [147: What happens if you use an object as a key in a plain object?](#147-what-happens-if-you-use-an-object-as-a-key-in-a-plain-object)
- [148: What are the most common data structures asked about in front-end interviews?](#148-what-are-the-most-common-data-structures-asked-about-in-front-end-interviews)
- [149: What is the difference between an array and a Set for storing unique items?](#149-what-is-the-difference-between-an-array-and-a-set-for-storing-unique-items)
- [150: Why should you know the cost of operations on each structure?](#150-why-should-you-know-the-cost-of-operations-on-each-structure)

### Moderate Questions (151-300)

- [151: How do you write a Stack class with private fields?](#151-how-do-you-write-a-stack-class-with-private-fields)
- [152: How do you build a queue with O(1) dequeue?](#152-how-do-you-build-a-queue-with-o1-dequeue)
- [153: How do you build a queue using two stacks?](#153-how-do-you-build-a-queue-using-two-stacks)
- [154: How do you build a deque with O(1) operations at both ends?](#154-how-do-you-build-a-deque-with-o1-operations-at-both-ends)
- [155: How do you implement a singly linked list with append, prepend and remove?](#155-how-do-you-implement-a-singly-linked-list-with-append-prepend-and-remove)
- [156: How do you implement a doubly linked list?](#156-how-do-you-implement-a-doubly-linked-list)
- [157: What edge cases should you test in a linked list?](#157-what-edge-cases-should-you-test-in-a-linked-list)
- [158: How do you find the middle of a linked list in one pass?](#158-how-do-you-find-the-middle-of-a-linked-list-in-one-pass)
- [159: How do you check if a linked list has a cycle?](#159-how-do-you-check-if-a-linked-list-has-a-cycle)
- [160: How do you make a linked list work with for...of and spread?](#160-how-do-you-make-a-linked-list-work-with-forof-and-spread)
- [161: What is a circular linked list and where is it used?](#161-what-is-a-circular-linked-list-and-where-is-it-used)
- [162: How do you insert a value into a binary search tree?](#162-how-do-you-insert-a-value-into-a-binary-search-tree)
- [163: How do you find the smallest and largest values in a BST?](#163-how-do-you-find-the-smallest-and-largest-values-in-a-bst)
- [164: How do you delete a node from a BST?](#164-how-do-you-delete-a-node-from-a-bst)
- [165: How do you do an in-order traversal of a BST without recursion?](#165-how-do-you-do-an-in-order-traversal-of-a-bst-without-recursion)
- [166: How do you walk a tree level by level?](#166-how-do-you-walk-a-tree-level-by-level)
- [167: How do you check if a binary tree is a valid BST?](#167-how-do-you-check-if-a-binary-tree-is-a-valid-bst)
- [168: How do you count the nodes and leaves of a tree?](#168-how-do-you-count-the-nodes-and-leaves-of-a-tree)
- [169: How do you find a node by id in a nested tree, like a menu?](#169-how-do-you-find-a-node-by-id-in-a-nested-tree-like-a-menu)
- [170: How do you flatten a tree into a list?](#170-how-do-you-flatten-a-tree-into-a-list)
- [171: How do you implement a min heap?](#171-how-do-you-implement-a-min-heap)
- [172: How does a heap fit into a plain array?](#172-how-does-a-heap-fit-into-a-plain-array)
- [173: How do you build a heap from an existing array in O(n)?](#173-how-do-you-build-a-heap-from-an-existing-array-in-on)
- [174: How do you use a heap as a priority queue for tasks?](#174-how-do-you-use-a-heap-as-a-priority-queue-for-tasks)
- [175: How do you implement a trie with insert, search and startsWith?](#175-how-do-you-implement-a-trie-with-insert-search-and-startswith)
- [176: How do you write a Graph class with an adjacency list?](#176-how-do-you-write-a-graph-class-with-an-adjacency-list)
- [177: How do you find the shortest path in an unweighted graph?](#177-how-do-you-find-the-shortest-path-in-an-unweighted-graph)
- [178: When would you use an adjacency matrix instead of a list?](#178-when-would-you-use-an-adjacency-matrix-instead-of-a-list)
- [179: What is topological sorting and where does a front-end developer see it?](#179-what-is-topological-sorting-and-where-does-a-front-end-developer-see-it)
- [180: How do you implement a hash table from scratch with chaining?](#180-how-do-you-implement-a-hash-table-from-scratch-with-chaining)
- [181: What is open addressing in a hash table?](#181-what-is-open-addressing-in-a-hash-table)
- [182: What is a load factor and why do hash tables resize?](#182-what-is-a-load-factor-and-why-do-hash-tables-resize)
- [183: How does a simple string hash function like djb2 work?](#183-how-does-a-simple-string-hash-function-like-djb2-work)
- [184: How do you build an LRU cache with a Map?](#184-how-do-you-build-an-lru-cache-with-a-map)
- [185: How do you implement a fixed-size ring buffer?](#185-how-do-you-implement-a-fixed-size-ring-buffer)
- [186: How did people do set operations before the new Set methods?](#186-how-did-people-do-set-operations-before-the-new-set-methods)
- [187: Can you pass something that isn't a Set to the new Set methods?](#187-can-you-pass-something-that-isnt-a-set-to-the-new-set-methods)
- [188: How do you use two values as one Map key?](#188-how-do-you-use-two-values-as-one-map-key)
- [189: How can a WeakMap store private data for objects?](#189-how-can-a-weakmap-store-private-data-for-objects)
- [190: How do you cache results per object without leaking memory?](#190-how-do-you-cache-results-per-object-without-leaking-memory)
- [191: What are WeakRef and FinalizationRegistry?](#191-what-are-weakref-and-finalizationregistry)
- [192: Can you use symbols as WeakMap keys?](#192-can-you-use-symbols-as-weakmap-keys)
- [193: What exactly is the iterator protocol?](#193-what-exactly-is-the-iterator-protocol)
- [194: How do you make a custom collection class iterable?](#194-how-do-you-make-a-custom-collection-class-iterable)
- [195: How do generators help when walking data structures?](#195-how-do-generators-help-when-walking-data-structures)
- [196: What are iterator helpers?](#196-what-are-iterator-helpers)
- [197: What does Iterator.from do?](#197-what-does-iteratorfrom-do)
- [198: What is the difference between lazy and eager processing of a collection?](#198-what-is-the-difference-between-lazy-and-eager-processing-of-a-collection)
- [199: What are async iterables?](#199-what-are-async-iterables)
- [200: What does Array.fromAsync do?](#200-what-does-arrayfromasync-do)
- [201: What does normalizing state mean?](#201-what-does-normalizing-state-mean)
- [202: Why normalize data instead of keeping the nested API response?](#202-why-normalize-data-instead-of-keeping-the-nested-api-response)
- [203: What is createEntityAdapter in Redux Toolkit?](#203-what-is-createentityadapter-in-redux-toolkit)
- [204: How do you update an item in a nested array immutably?](#204-how-do-you-update-an-item-in-a-nested-array-immutably)
- [205: How does Immer let you write mutations but still get immutable updates?](#205-how-does-immer-let-you-write-mutations-but-still-get-immutable-updates)
- [206: How do you deep freeze an object?](#206-how-do-you-deep-freeze-an-object)
- [207: How do you write a simple deep clone function?](#207-how-do-you-write-a-simple-deep-clone-function)
- [208: What can't structuredClone copy?](#208-what-cant-structuredclone-copy)
- [209: How do you write a deep equality check?](#209-how-do-you-write-a-deep-equality-check)
- [210: What is the difference between ===, Object.is and SameValueZero?](#210-what-is-the-difference-between--objectis-and-samevaluezero)
- [211: What happens to a Map's order when you set an existing key again?](#211-what-happens-to-a-maps-order-when-you-set-an-existing-key-again)
- [212: Why would you use a Map instead of an object for data keyed by numeric ids?](#212-why-would-you-use-a-map-instead-of-an-object-for-data-keyed-by-numeric-ids)
- [213: How can several typed arrays share one ArrayBuffer?](#213-how-can-several-typed-arrays-share-one-arraybuffer)
- [214: What is a DataView and when do you need it?](#214-what-is-a-dataview-and-when-do-you-need-it)
- [215: What is Uint8ClampedArray and where is it used?](#215-what-is-uint8clampedarray-and-where-is-it-used)
- [216: How do you convert between strings and bytes?](#216-how-do-you-convert-between-strings-and-bytes)
- [217: How do Blob and File relate to ArrayBuffer?](#217-how-do-blob-and-file-relate-to-arraybuffer)
- [218: How do you store a 2D grid in a flat array?](#218-how-do-you-store-a-2d-grid-in-a-flat-array)
- [219: How do you store a sparse matrix efficiently?](#219-how-do-you-store-a-sparse-matrix-efficiently)
- [220: How do you use a number as a set of boolean flags?](#220-how-do-you-use-a-number-as-a-set-of-boolean-flags)
- [221: How do you build a bitset for many flags?](#221-how-do-you-build-a-bitset-for-many-flags)
- [222: What is a disjoint set (union-find)?](#222-what-is-a-disjoint-set-union-find)
- [223: How do you implement union-find with path compression?](#223-how-do-you-implement-union-find-with-path-compression)
- [224: What is a monotonic stack?](#224-what-is-a-monotonic-stack)
- [225: How do you build a stack that returns its minimum in O(1)?](#225-how-do-you-build-a-stack-that-returns-its-minimum-in-o1)
- [226: How do you build undo and redo with stacks?](#226-how-do-you-build-undo-and-redo-with-stacks)
- [227: How would you model browser back and forward navigation?](#227-how-would-you-model-browser-back-and-forward-navigation)
- [228: How do you find all elements at a certain depth in the DOM?](#228-how-do-you-find-all-elements-at-a-certain-depth-in-the-dom)
- [229: How do you build an event emitter with Map and Set?](#229-how-do-you-build-an-event-emitter-with-map-and-set)
- [230: How do you keep a list of subscribers in a store?](#230-how-do-you-keep-a-list-of-subscribers-in-a-store)
- [231: How do you detect circular imports in a dependency graph?](#231-how-do-you-detect-circular-imports-in-a-dependency-graph)
- [232: How do you memoize a function with several arguments?](#232-how-do-you-memoize-a-function-with-several-arguments)
- [233: When does it pay off to turn an array into a Set for lookups?](#233-when-does-it-pay-off-to-turn-an-array-into-a-set-for-lookups)
- [234: When is a plain object better than a Map?](#234-when-is-a-plain-object-better-than-a-map)
- [235: How do you count frequencies and get the top items?](#235-how-do-you-count-frequencies-and-get-the-top-items)
- [236: Should you use Object.groupBy, Map.groupBy or reduce for grouping?](#236-should-you-use-objectgroupby-mapgroupby-or-reduce-for-grouping)
- [237: Is a linked list faster than an array in JavaScript for inserts?](#237-is-a-linked-list-faster-than-an-array-in-javascript-for-inserts)
- [238: What are packed and holey arrays?](#238-what-are-packed-and-holey-arrays)
- [239: Why does mixing types in an array affect performance?](#239-why-does-mixing-types-in-an-array-affect-performance)
- [240: Why shouldn't you use delete on array items?](#240-why-shouldnt-you-use-delete-on-array-items)
- [241: What is the maximum length of an array?](#241-what-is-the-maximum-length-of-an-array)
- [242: How do you sort a Map by its values?](#242-how-do-you-sort-a-map-by-its-values)
- [243: How do you sort an object by its keys?](#243-how-do-you-sort-an-object-by-its-keys)
- [244: What is Object.create(null) and when do you use it?](#244-what-is-objectcreatenull-and-when-do-you-use-it)
- [245: What is prototype pollution?](#245-what-is-prototype-pollution)
- [246: How can a Proxy make an observable data structure?](#246-how-can-a-proxy-make-an-observable-data-structure)
- [247: Why use Reflect inside Proxy traps?](#247-why-use-reflect-inside-proxy-traps)
- [248: How do you add parent links to a tree, and why?](#248-how-do-you-add-parent-links-to-a-tree-and-why)
- [249: How do you serialize and rebuild a binary tree?](#249-how-do-you-serialize-and-rebuild-a-binary-tree)
- [250: How do you get the path from the root to a node, like breadcrumbs?](#250-how-do-you-get-the-path-from-the-root-to-a-node-like-breadcrumbs)
- [251: How do you filter a tree but keep the parents of matching nodes?](#251-how-do-you-filter-a-tree-but-keep-the-parents-of-matching-nodes)
- [252: How would you model a file system in JavaScript?](#252-how-would-you-model-a-file-system-in-javascript)
- [253: How should you store nested comments?](#253-how-should-you-store-nested-comments)
- [254: How do you count how many words start with a prefix using a trie?](#254-how-do-you-count-how-many-words-start-with-a-prefix-using-a-trie)
- [255: Heap or sorted array for a priority queue?](#255-heap-or-sorted-array-for-a-priority-queue)
- [256: What are the time complexities of a binary heap?](#256-what-are-the-time-complexities-of-a-binary-heap)
- [257: What is the difference between a balanced and an unbalanced BST?](#257-what-is-the-difference-between-a-balanced-and-an-unbalanced-bst)
- [258: What happens if you insert sorted data into a plain BST?](#258-what-happens-if-you-insert-sorted-data-into-a-plain-bst)
- [259: How do you represent a weighted graph in JavaScript?](#259-how-do-you-represent-a-weighted-graph-in-javascript)
- [260: What is an edge list and when is it useful?](#260-what-is-an-edge-list-and-when-is-it-useful)
- [261: What is an implicit graph?](#261-what-is-an-implicit-graph)
- [262: Is Map lookup always O(1)?](#262-is-map-lookup-always-o1)
- [263: Why doesn't new Set([[1, 2], [1, 2]]) remove the duplicate pair?](#263-why-doesnt-new-set1-2-1-2-remove-the-duplicate-pair)
- [264: How do you use coordinates like [x, y] as a key?](#264-how-do-you-use-coordinates-like-x-y-as-a-key)
- [265: How do you implement a queue with a linked list?](#265-how-do-you-implement-a-queue-with-a-linked-list)
- [266: How do you keep equal-priority items in insertion order in a heap?](#266-how-do-you-keep-equal-priority-items-in-insertion-order-in-a-heap)
- [267: How would you schedule UI work by priority?](#267-how-would-you-schedule-ui-work-by-priority)
- [268: How do you build a cache where entries expire after some time?](#268-how-do-you-build-a-cache-where-entries-expire-after-some-time)
- [269: What is an LFU cache?](#269-what-is-an-lfu-cache)
- [270: How do you remove the nth node from the end of a linked list?](#270-how-do-you-remove-the-nth-node-from-the-end-of-a-linked-list)
- [271: How do you find where two linked lists join?](#271-how-do-you-find-where-two-linked-lists-join)
- [272: How do you check if a linked list is a palindrome with O(1) extra memory?](#272-how-do-you-check-if-a-linked-list-is-a-palindrome-with-o1-extra-memory)
- [273: Why is an LRU cache often built with a doubly linked list plus a hash map?](#273-why-is-an-lru-cache-often-built-with-a-doubly-linked-list-plus-a-hash-map)
- [274: Why are push and pop on an array O(1) even though arrays sometimes resize?](#274-why-are-push-and-pop-on-an-array-o1-even-though-arrays-sometimes-resize)
- [275: Should you store extra data on DOM elements with dataset or with a WeakMap?](#275-should-you-store-extra-data-on-dom-elements-with-dataset-or-with-a-weakmap)
- [276: How do you track visited nodes when walking a graph?](#276-how-do-you-track-visited-nodes-when-walking-a-graph)
- [277: How do you avoid infinite loops when walking objects that may have cycles?](#277-how-do-you-avoid-infinite-loops-when-walking-objects-that-may-have-cycles)
- [278: How do you JSON.stringify an object with circular references?](#278-how-do-you-jsonstringify-an-object-with-circular-references)
- [279: How do you use a replacer and reviver to store Map, Set and Date in JSON?](#279-how-do-you-use-a-replacer-and-reviver-to-store-map-set-and-date-in-json)
- [280: Why do Dates come back as strings after JSON.parse, and how do you fix it?](#280-why-do-dates-come-back-as-strings-after-jsonparse-and-how-do-you-fix-it)
- [281: How do you put a BigInt in JSON?](#281-how-do-you-put-a-bigint-in-json)
- [282: How do you write a generic Stack in TypeScript?](#282-how-do-you-write-a-generic-stack-in-typescript)
- [283: What do readonly arrays and as const do in TypeScript?](#283-what-do-readonly-arrays-and-as-const-do-in-typescript)
- [284: What is the difference between Record and Map in TypeScript?](#284-what-is-the-difference-between-record-and-map-in-typescript)
- [285: How do you model tree nodes with different types in TypeScript?](#285-how-do-you-model-tree-nodes-with-different-types-in-typescript)
- [286: How do you replace an item at an index without mutating?](#286-how-do-you-replace-an-item-at-an-index-without-mutating)
- [287: What is the difference between object spread and Object.assign?](#287-what-is-the-difference-between-object-spread-and-objectassign)
- [288: Should you write data structures as classes or factory functions?](#288-should-you-write-data-structures-as-classes-or-factory-functions)
- [289: Why use private class fields (#) in data structures?](#289-why-use-private-class-fields--in-data-structures)
- [290: Can Map.groupBy group by object keys?](#290-can-mapgroupby-group-by-object-keys)
- [291: How do you test your own data structure implementation?](#291-how-do-you-test-your-own-data-structure-implementation)
- [292: What data structures would you use for a todo app with filters and drag-and-drop reordering?](#292-what-data-structures-would-you-use-for-a-todo-app-with-filters-and-drag-and-drop-reordering)
- [293: How would you store messages in a chat app?](#293-how-would-you-store-messages-in-a-chat-app)
- [294: How do you use a Set in React state?](#294-how-do-you-use-a-set-in-react-state)
- [295: What problems can Map and Set cause in app state?](#295-what-problems-can-map-and-set-cause-in-app-state)
- [296: How do you remove items from a Map while looping over it?](#296-how-do-you-remove-items-from-a-map-while-looping-over-it)
- [297: How do you merge two Maps?](#297-how-do-you-merge-two-maps)
- [298: How do you invert an object or Map (swap keys and values)?](#298-how-do-you-invert-an-object-or-map-swap-keys-and-values)
- [299: How do you chunk an array into groups of n?](#299-how-do-you-chunk-an-array-into-groups-of-n)
- [300: How do you zip two arrays into pairs?](#300-how-do-you-zip-two-arrays-into-pairs)

### Advanced Questions (301-450)

- [301: How does V8 store objects internally?](#301-how-does-v8-store-objects-internally)
- [302: What is dictionary mode, and what pushes an object into it?](#302-what-is-dictionary-mode-and-what-pushes-an-object-into-it)
- [303: What are elements kinds in V8?](#303-what-are-elements-kinds-in-v8)
- [304: How are Map and Set implemented in V8?](#304-how-are-map-and-set-implemented-in-v8)
- [305: How can a hash table also keep insertion order?](#305-how-can-a-hash-table-also-keep-insertion-order)
- [306: How does a Map hash an object key if objects have no hash code?](#306-how-does-a-map-hash-an-object-key-if-objects-have-no-hash-code)
- [307: How do the memory costs of objects, arrays and Maps compare?](#307-how-do-the-memory-costs-of-objects-arrays-and-maps-compare)
- [308: What are Smis and heap numbers, and why should you care?](#308-what-are-smis-and-heap-numbers-and-why-should-you-care)
- [309: How does an array's backing store grow?](#309-how-does-an-arrays-backing-store-grow)
- [310: How does V8 represent strings, and why can concatenation be cheap?](#310-how-does-v8-represent-strings-and-why-can-concatenation-be-cheap)
- [311: Is building a string with += in a loop slow?](#311-is-building-a-string-with--in-a-loop-slow)
- [312: How does garbage collection affect the design of data structures?](#312-how-does-garbage-collection-affect-the-design-of-data-structures)
- [313: What is object pooling, and when is it worth it?](#313-what-is-object-pooling-and-when-is-it-worth-it)
- [314: What is the difference between an array of structs and a struct of arrays?](#314-what-is-the-difference-between-an-array-of-structs-and-a-struct-of-arrays)
- [315: When are typed arrays clearly faster than normal arrays?](#315-when-are-typed-arrays-clearly-faster-than-normal-arrays)
- [316: What is SharedArrayBuffer, and why does it need cross-origin isolation?](#316-what-is-sharedarraybuffer-and-why-does-it-need-cross-origin-isolation)
- [317: What does Atomics do?](#317-what-does-atomics-do)
- [318: How would you build a ring buffer shared between the main thread and a worker?](#318-how-would-you-build-a-ring-buffer-shared-between-the-main-thread-and-a-worker)
- [319: What are resizable ArrayBuffers?](#319-what-are-resizable-arraybuffers)
- [320: What does ArrayBuffer.prototype.transfer do, and what is a detached buffer?](#320-what-does-arraybufferprototypetransfer-do-and-what-is-a-detached-buffer)
- [321: What is Float16Array?](#321-what-is-float16array)
- [322: What newer methods help convert bytes to base64 and hex?](#322-what-newer-methods-help-convert-bytes-to-base64-and-hex)
- [323: What does the structured clone algorithm support, and how does transfer work with it?](#323-what-does-the-structured-clone-algorithm-support-and-how-does-transfer-work-with-it)
- [324: What are the rules for WeakRef.deref()?](#324-what-are-the-rules-for-weakrefderef)
- [325: What are the pitfalls of FinalizationRegistry?](#325-what-are-the-pitfalls-of-finalizationregistry)
- [326: What is an ephemeron, and why does it matter for WeakMap?](#326-what-is-an-ephemeron-and-why-does-it-matter-for-weakmap)
- [327: How do you find a memory leak caused by a cache or registry?](#327-how-do-you-find-a-memory-leak-caused-by-a-cache-or-registry)
- [328: How does an AVL tree stay balanced?](#328-how-does-an-avl-tree-stay-balanced)
- [329: What rules does a red-black tree follow?](#329-what-rules-does-a-red-black-tree-follow)
- [330: What is a B-tree, and why do databases use it?](#330-what-is-a-b-tree-and-why-do-databases-use-it)
- [331: What is a skip list?](#331-what-is-a-skip-list)
- [332: What is a Fenwick tree (binary indexed tree)?](#332-what-is-a-fenwick-tree-binary-indexed-tree)
- [333: How would you find overlapping events in a calendar quickly?](#333-how-would-you-find-overlapping-events-in-a-calendar-quickly)
- [334: What is a quadtree, and how does it help with canvas hit testing?](#334-what-is-a-quadtree-and-how-does-it-help-with-canvas-hit-testing)
- [335: What is a spatial hash grid, and when is it better than a quadtree?](#335-what-is-a-spatial-hash-grid-and-when-is-it-better-than-a-quadtree)
- [336: What is a k-d tree?](#336-what-is-a-k-d-tree)
- [337: What is a rope, and why do text editors use something like it?](#337-what-is-a-rope-and-why-do-text-editors-use-something-like-it)
- [338: What is a gap buffer?](#338-what-is-a-gap-buffer)
- [339: What is a piece table?](#339-what-is-a-piece-table)
- [340: What data structures are behind collaborative editing (CRDTs)?](#340-what-data-structures-are-behind-collaborative-editing-crdts)
- [341: What is a hash array mapped trie (HAMT)?](#341-what-is-a-hash-array-mapped-trie-hamt)
- [342: How does a persistent linked list share structure?](#342-how-does-a-persistent-linked-list-share-structure)
- [343: Immutable.js or Immer: what is the difference?](#343-immutablejs-or-immer-what-is-the-difference)
- [344: How does a persistent vector give fast immutable updates?](#344-how-does-a-persistent-vector-give-fast-immutable-updates)
- [345: What is a radix tree, and how is it different from a trie?](#345-what-is-a-radix-tree-and-how-is-it-different-from-a-trie)
- [346: What are suffix arrays and suffix trees used for?](#346-what-are-suffix-arrays-and-suffix-trees-used-for)
- [347: What is a count-min sketch?](#347-what-is-a-count-min-sketch)
- [348: What is HyperLogLog?](#348-what-is-hyperloglog)
- [349: What is cuckoo hashing?](#349-what-is-cuckoo-hashing)
- [350: What is Robin Hood hashing?](#350-what-is-robin-hood-hashing)
- [351: What is a hash flooding attack?](#351-what-is-a-hash-flooding-attack)
- [352: How do you write a safe deep merge?](#352-how-do-you-write-a-safe-deep-merge)
- [353: Are Map and Object.create(null) enough to stop prototype pollution?](#353-are-map-and-objectcreatenull-enough-to-stop-prototype-pollution)
- [354: What data structure does Vue's reactivity system use to track dependencies?](#354-what-data-structure-does-vues-reactivity-system-use-to-track-dependencies)
- [355: How are signals stored as a dependency graph?](#355-how-are-signals-stored-as-a-dependency-graph)
- [356: Why is the virtual DOM a tree, and how do keys change the diff?](#356-why-is-the-virtual-dom-a-tree-and-how-do-keys-change-the-diff)
- [357: How does React Fiber represent the component tree?](#357-how-does-react-fiber-represent-the-component-tree)
- [358: How are hooks stored, and why can't you call them conditionally?](#358-how-are-hooks-stored-and-why-cant-you-call-them-conditionally)
- [359: What queues does the browser event loop use?](#359-what-queues-does-the-browser-event-loop-use)
- [360: What trees does the browser build to render a page?](#360-what-trees-does-the-browser-build-to-render-a-page)
- [361: What data structure helps a virtual list with variable row heights?](#361-what-data-structure-helps-a-virtual-list-with-variable-row-heights)
- [362: How do you find the first visible row from a scroll position?](#362-how-do-you-find-the-first-visible-row-from-a-scroll-position)
- [363: Snapshots or commands: how should undo history be stored?](#363-snapshots-or-commands-how-should-undo-history-be-stored)
- [364: How do Immer patches help with undo and syncing?](#364-how-do-immer-patches-help-with-undo-and-syncing)
- [365: How does a normalized GraphQL client cache work?](#365-how-does-a-normalized-graphql-client-cache-work)
- [366: How would you design a client-side cache with tag-based invalidation?](#366-how-would-you-design-a-client-side-cache-with-tag-based-invalidation)
- [367: How would you limit a cache by total size in bytes instead of entry count?](#367-how-would-you-limit-a-cache-by-total-size-in-bytes-instead-of-entry-count)
- [368: How would you store an infinite scroll feed so items don't repeat or jump?](#368-how-would-you-store-an-infinite-scroll-feed-so-items-dont-repeat-or-jump)
- [369: How would you combine a trie and a heap for ranked autocomplete?](#369-how-would-you-combine-a-trie-and-a-heap-for-ranked-autocomplete)
- [370: How would you design a notification queue with priorities and no duplicates?](#370-how-would-you-design-a-notification-queue-with-priorities-and-no-duplicates)
- [371: How do calendar apps lay out overlapping events side by side?](#371-how-do-calendar-apps-lay-out-overlapping-events-side-by-side)
- [372: What data structures does a spreadsheet need for recalculation?](#372-what-data-structures-does-a-spreadsheet-need-for-recalculation)
- [373: How would you design a file explorer tree that loads folders lazily?](#373-how-would-you-design-a-file-explorer-tree-that-loads-folders-lazily)
- [374: How do you keep a big list sorted when new items arrive?](#374-how-do-you-keep-a-big-list-sorted-when-new-items-arrive)
- [375: JavaScript has no sorted map. What are your options?](#375-javascript-has-no-sorted-map-what-are-your-options)
- [376: How do you implement a sorted map with a BST in JavaScript?](#376-how-do-you-implement-a-sorted-map-with-a-bst-in-javascript)
- [377: How do you build a deque on a circular buffer that grows?](#377-how-do-you-build-a-deque-on-a-circular-buffer-that-grows)
- [378: Why is a circular buffer faster than an object-based queue?](#378-why-is-a-circular-buffer-faster-than-an-object-based-queue)
- [379: How do you support "change priority" in a heap?](#379-how-do-you-support-change-priority-in-a-heap)
- [380: What are Fibonacci and pairing heaps?](#380-what-are-fibonacci-and-pairing-heaps)
- [381: Why is union-find "almost" O(1)?](#381-why-is-union-find-almost-o1)
- [382: How can you store a huge graph in typed arrays?](#382-how-can-you-store-a-huge-graph-in-typed-arrays)
- [383: How do bundlers represent the module graph?](#383-how-do-bundlers-represent-the-module-graph)
- [384: How do you make a trie use less memory?](#384-how-do-you-make-a-trie-use-less-memory)
- [385: What is a DAWG?](#385-what-is-a-dawg)
- [386: What is the Eytzinger layout?](#386-what-is-the-eytzinger-layout)
- [387: How do bitmasks represent small sets?](#387-how-do-bitmasks-represent-small-sets)
- [388: When does immutable updating become too slow?](#388-when-does-immutable-updating-become-too-slow)
- [389: Should you use Object.freeze in production code?](#389-should-you-use-objectfreeze-in-production-code)
- [390: Without Records and Tuples, how can you get value-based equality for keys?](#390-without-records-and-tuples-how-can-you-get-value-based-equality-for-keys)
- [391: How would you build a Map that compares keys by content?](#391-how-would-you-build-a-map-that-compares-keys-by-content)
- [392: What goes wrong if you use JSON.stringify as a cache key?](#392-what-goes-wrong-if-you-use-jsonstringify-as-a-cache-key)
- [393: How do you write a full deep equality check that handles Map, Set, typed arrays and cycles?](#393-how-do-you-write-a-full-deep-equality-check-that-handles-map-set-typed-arrays-and-cycles)
- [394: How do you deep clone something with cycles and special types by hand?](#394-how-do-you-deep-clone-something-with-cycles-and-special-types-by-hand)
- [395: How do you serialize and restore class instances?](#395-how-do-you-serialize-and-restore-class-instances)
- [396: When would you use a binary format like MessagePack or Protocol Buffers instead of JSON?](#396-when-would-you-use-a-binary-format-like-messagepack-or-protocol-buffers-instead-of-json)
- [397: How do you handle a JSON response too large to parse at once?](#397-how-do-you-handle-a-json-response-too-large-to-parse-at-once)
- [398: How is data organized in IndexedDB?](#398-how-is-data-organized-in-indexeddb)
- [399: What should you keep in mind when saving data structures to localStorage?](#399-what-should-you-keep-in-mind-when-saving-data-structures-to-localstorage)
- [400: What does it cost to send a large data structure to a Web Worker?](#400-what-does-it-cost-to-send-a-large-data-structure-to-a-web-worker)
- [401: How do you pass a large dataset to a worker without copying?](#401-how-do-you-pass-a-large-dataset-to-a-worker-without-copying)
- [402: How can you measure how much memory your data structures use?](#402-how-can-you-measure-how-much-memory-your-data-structures-use)
- [403: What is the difference between shallow size and retained size?](#403-what-is-the-difference-between-shallow-size-and-retained-size)
- [404: How can a data structure keep detached DOM nodes alive?](#404-how-can-a-data-structure-keep-detached-dom-nodes-alive)
- [405: How do closures accidentally keep big data structures in memory?](#405-how-do-closures-accidentally-keep-big-data-structures-in-memory)
- [406: How does laziness in iterator helpers work with infinite sequences?](#406-how-does-laziness-in-iterator-helpers-work-with-infinite-sequences)
- [407: When should a data pipeline use generators instead of arrays?](#407-when-should-a-data-pipeline-use-generators-instead-of-arrays)
- [408: How do streams use queues for backpressure?](#408-how-do-streams-use-queues-for-backpressure)
- [409: How do you build an async queue that producers push to and consumers await?](#409-how-do-you-build-an-async-queue-that-producers-push-to-and-consumers-await)
- [410: What happens if you modify a Map or Set while iterating over it?](#410-what-happens-if-you-modify-a-map-or-set-while-iterating-over-it)
- [411: What happens if you modify an array while using forEach or map?](#411-what-happens-if-you-modify-an-array-while-using-foreach-or-map)
- [412: What does the spec guarantee about sort stability and compare functions?](#412-what-does-the-spec-guarantee-about-sort-stability-and-compare-functions)
- [413: How should you sort strings for users?](#413-how-should-you-sort-strings-for-users)
- [414: When is an array index really an index?](#414-when-is-an-array-index-really-an-index)
- [415: Why are +0 and -0 the same key in a Map?](#415-why-are-0-and--0-the-same-key-in-a-map)
- [416: How do different array methods treat NaN?](#416-how-do-different-array-methods-treat-nan)
- [417: What is Symbol.species, and why is it a problem when you subclass Array?](#417-what-is-symbolspecies-and-why-is-it-a-problem-when-you-subclass-array)
- [418: How do you safely extend Map or Set?](#418-how-do-you-safely-extend-map-or-set)
- [419: How can a Proxy add negative indexing to arrays?](#419-how-can-a-proxy-add-negative-indexing-to-arrays)
- [420: What makes arrays "exotic objects" in the spec?](#420-what-makes-arrays-exotic-objects-in-the-spec)
- [421: How do getters in data structures interact with JSON and copying?](#421-how-do-getters-in-data-structures-interact-with-json-and-copying)
- [422: Why does Object.groupBy return an object with a null prototype?](#422-why-does-objectgroupby-return-an-object-with-a-null-prototype)
- [423: How does Map.groupBy decide which items share a group?](#423-how-does-mapgroupby-decide-which-items-share-a-group)
- [424: How is sort() on a typed array different from sort() on an array?](#424-how-is-sort-on-a-typed-array-different-from-sort-on-an-array)
- [425: How do you parse a binary format like a PNG header in JavaScript?](#425-how-do-you-parse-a-binary-format-like-a-png-header-in-javascript)
- [426: Why does endianness matter when you share typed arrays across systems?](#426-why-does-endianness-matter-when-you-share-typed-arrays-across-systems)
- [427: How do you pack many booleans into a small amount of memory?](#427-how-do-you-pack-many-booleans-into-a-small-amount-of-memory)
- [428: How would you store millions of numeric ids for fast membership checks?](#428-how-would-you-store-millions-of-numeric-ids-for-fast-membership-checks)
- [429: What are Roaring bitmaps?](#429-what-are-roaring-bitmaps)
- [430: How do you choose between sparse and dense representations?](#430-how-do-you-choose-between-sparse-and-dense-representations)
- [431: Design a structure with O(1) insert, delete and getRandom.](#431-design-a-structure-with-o1-insert-delete-and-getrandom)
- [432: Design a time-based key-value store where get(key, time) returns the value at that time.](#432-design-a-time-based-key-value-store-where-getkey-time-returns-the-value-at-that-time)
- [433: Design a snapshot array: set(index, value), snap() and get(index, snapId).](#433-design-a-snapshot-array-setindex-value-snap-and-getindex-snapid)
- [434: Design a hit counter that returns hits in the last 5 minutes.](#434-design-a-hit-counter-that-returns-hits-in-the-last-5-minutes)
- [435: Design a leaderboard that supports updating scores and getting the top k.](#435-design-a-leaderboard-that-supports-updating-scores-and-getting-the-top-k)
- [436: Design an in-memory file system with mkdir, ls, addContent and readContent.](#436-design-an-in-memory-file-system-with-mkdir-ls-addcontent-and-readcontent)
- [437: Design an MRU tab switcher like Ctrl+Tab in a browser or editor.](#437-design-an-mru-tab-switcher-like-ctrltab-in-a-browser-or-editor)
- [438: Design an LFU cache with O(1) operations.](#438-design-an-lfu-cache-with-o1-operations)
- [439: How can an event log be the main data structure of a front-end app?](#439-how-can-an-event-log-be-the-main-data-structure-of-a-front-end-app)
- [440: How do you store item order so several users can reorder a list without conflicts?](#440-how-do-you-store-item-order-so-several-users-can-reorder-a-list-without-conflicts)
- [441: Why can't you diff two trees in linear time in general, and how do frameworks get around it?](#441-why-cant-you-diff-two-trees-in-linear-time-in-general-and-how-do-frameworks-get-around-it)
- [442: What is a Merkle tree, and how could a front-end app use the idea?](#442-what-is-a-merkle-tree-and-how-could-a-front-end-app-use-the-idea)
- [443: What is content-addressed storage, and why does it help caching?](#443-what-is-content-addressed-storage-and-why-does-it-help-caching)
- [444: How do you avoid misleading microbenchmarks when comparing data structures?](#444-how-do-you-avoid-misleading-microbenchmarks-when-comparing-data-structures)
- [445: A chart needs to show 1 million points and stay smooth. What data structures would you use?](#445-a-chart-needs-to-show-1-million-points-and-stay-smooth-what-data-structures-would-you-use)
- [446: How would you filter 50,000 products by many facets (brand, color, size, price) instantly?](#446-how-would-you-filter-50000-products-by-many-facets-brand-color-size-price-instantly)
- [447: What is an inverted index, and how would you build one for client-side search?](#447-what-is-an-inverted-index-and-how-would-you-build-one-for-client-side-search)
- [448: How would you keep a large live-updating table (prices, statuses) fast?](#448-how-would-you-keep-a-large-live-updating-table-prices-statuses-fast)
- [449: How do you explain data structure trade-offs in an interview?](#449-how-do-you-explain-data-structure-trade-offs-in-an-interview)
- [450: What is the most common data structure mistake in front-end code, in your experience?](#450-what-is-the-most-common-data-structure-mistake-in-front-end-code-in-your-experience)

---

# Easy Questions (1-150)

## 1: What is a data structure?

A data structure is a way to organize data in memory so you can use it well. Each one makes some operations cheap and others expensive. An array is great for reading by index, a `Set` is great for checking "do I already have this?", and a queue is great for handling things in the order they came in. Picking the right one is mostly about knowing which operations you will do most often.

## 2: Why should a front-end developer know data structures?

Front-end code is full of them: the DOM is a tree, browser history is a stack, the event loop uses queues, app state is usually objects and arrays, and caches are maps. When a list of 20,000 items makes the page slow, the fix is often a better data structure, like a `Map` for lookups instead of calling `find()` in a loop. Interviewers also use these questions to see if you understand the cost of the code you write.

## 3: What is the difference between primitive and reference types?

Primitives (`string`, `number`, `bigint`, `boolean`, `undefined`, `null`, `symbol`) are stored and compared by value. Objects, arrays, functions, maps and sets are reference types: a variable holds a reference to the object, not the object itself.

```js
let a = 5;
let b = a;
b++; // a is still 5

const x = { n: 1 };
const y = x;
y.n = 2; // x.n is now 2, both point to the same object
```

## 4: What data structures does JavaScript give you out of the box?

Arrays, plain objects, `Map`, `Set`, `WeakMap`, `WeakSet`, `WeakRef`, typed arrays (`Uint8Array`, `Float64Array` and others) with `ArrayBuffer` and `DataView`, and strings. JSON is a text format built on objects and arrays. There is no built-in stack, queue, linked list, tree, heap or graph, so you build those yourself, usually on top of arrays, objects and maps.

## 5: What is an array in JavaScript?

An array is an ordered list of values, accessed by a numeric index that starts at 0. JavaScript arrays can grow and shrink, and can hold any mix of types.

```js
const items = ["a", 1, { id: 3 }];
items.push(true);
console.log(items[0], items.length); // "a" 4
```

## 6: Are JavaScript arrays real arrays like in C?

Not by the language spec. An array is a special object whose keys are string indexes ("0", "1", ...) with a `length` property that updates on its own. In practice, engines like V8 store arrays as real contiguous memory when they can (for example, when they hold only small integers or only doubles), and fall back to slower storage when you create big holes or mix in odd keys. So they behave like normal arrays as long as you use them like normal arrays.

## 7: What is the time complexity of common array operations?

- Read or write by index: O(1)
- `push` / `pop` at the end: O(1) (amortized for `push`)
- `shift` / `unshift` at the start: O(n), because every other element moves
- `splice` in the middle: O(n)
- `includes`, `indexOf`, `find`: O(n)
- `slice`, `concat`, spread copy: O(n)

## 8: What is the difference between push and unshift?

`push` adds items to the end of an array, `unshift` adds them to the start. Both return the new length. `push` is cheap because nothing else moves. `unshift` has to shift every existing element one slot to the right, so it gets slower as the array grows.

```js
const arr = [2, 3];
arr.push(4); // [2, 3, 4]
arr.unshift(1); // [1, 2, 3, 4]
```

## 9: What is the difference between pop and shift?

`pop` removes and returns the last element, `shift` removes and returns the first one. `pop` is O(1). `shift` is O(n) because all remaining elements move down by one index. Both return `undefined` on an empty array instead of throwing.

## 10: What is a sparse array?

A sparse array has holes: indexes that don't exist at all, which is different from holding `undefined`.

```js
const a = [1, , 3]; // hole at index 1
const b = new Array(3); // three holes
a[10] = 5; // indexes 3-9 are now holes

console.log(1 in a); // false
```

Methods treat holes differently: `forEach` and `map` skip them, `for...of` and `Array.from` give `undefined`. Holes also make arrays slower in engines, so avoid them.

## 11: What happens when you change an array's length property?

Setting `length` to a smaller number deletes everything past that index. Setting it to a bigger number adds holes at the end.

```js
const arr = [1, 2, 3, 4, 5];
arr.length = 2; // [1, 2]
arr.length = 0; // [] , a quick way to empty an array in place
```

Emptying with `length = 0` changes the original array, so every other reference to it sees an empty array too. `arr = []` only rebinds your variable.

## 12: What does at() do?

`at()` reads an element by index and accepts negative numbers, which count from the end. It works on arrays, strings and typed arrays.

```js
const arr = [10, 20, 30];
arr.at(0); // 10
arr.at(-1); // 30, instead of arr[arr.length - 1]
```

## 13: What are the different ways to create an array?

```js
const a = [1, 2, 3]; // literal, the usual way
const b = Array.of(7); // [7]
const c = Array.from("abc"); // ["a", "b", "c"]
const d = Array.from({ length: 3 }, (_, i) => i * 2); // [0, 2, 4]
const e = new Array(3); // three empty holes, not [3]
```

The trap is `new Array(n)`: with a single number it makes an empty array of that length, but with any other single value it makes a one-element array. `Array.of` doesn't have that problem.

## 14: How do you create an array of n items filled with values?

```js
const zeros = new Array(5).fill(0); // [0, 0, 0, 0, 0]
const nums = Array.from({ length: 5 }, (_, i) => i + 1); // [1, 2, 3, 4, 5]
```

Use `fill` for the same primitive value everywhere and `Array.from` with a callback when each item should be computed or should be a separate object.

## 15: What goes wrong with new Array(3).fill({})?

`fill` puts the same value in every slot. With an object, that means every slot holds a reference to one single object.

```js
const rows = new Array(3).fill({});
rows[0].x = 1;
console.log(rows[2].x); // 1, they are all the same object

const fixed = Array.from({ length: 3 }, () => ({}));
```

## 16: How do you create a 2D array (grid)?

Create each row separately so rows don't share the same array.

```js
const rows = 3,
  cols = 4;
const grid = Array.from({ length: rows }, () => new Array(cols).fill(0));
grid[1][2] = 5;
```

`new Array(rows).fill(new Array(cols).fill(0))` looks right but every row is the same array, so writing to one row writes to all of them.

## 17: How do you copy an array?

```js
const original = [1, 2, 3];
const a = [...original];
const b = original.slice();
const c = Array.from(original);
const d = structuredClone(original); // deep copy
```

The first three are shallow copies: the new array is separate, but if it holds objects, both arrays point to the same objects.

## 18: What is the difference between a shallow copy and a deep copy?

A shallow copy creates a new top-level container but keeps references to the same nested objects. A deep copy copies everything all the way down.

```js
const user = { name: "Ana", tags: ["admin"] };
const shallow = { ...user };
shallow.tags.push("editor");
console.log(user.tags); // ["admin", "editor"], shared

const deep = structuredClone(user);
deep.tags.push("guest");
console.log(user.tags); // unchanged
```

## 19: What is structuredClone?

`structuredClone` is a built-in function that makes a deep copy of a value. It handles nested objects, arrays, `Map`, `Set`, `Date`, `RegExp`, typed arrays and even circular references. It throws on functions and DOM nodes, and it doesn't keep class prototypes, so a class instance comes back as a plain object.

```js
const state = { list: [1, 2], meta: new Map([["page", 1]]) };
const copy = structuredClone(state);
```

## 20: Why is JSON.parse(JSON.stringify(obj)) a weak way to deep copy?

It only works for plain JSON data. It drops `undefined`, functions and symbols, turns `Date` into a string, turns `Map` and `Set` into `{}`, turns `NaN` and `Infinity` into `null`, throws on `BigInt` and throws on circular references. It's also slower than `structuredClone` for most cases. Use `structuredClone` unless you specifically want JSON behavior.

## 21: Which array methods mutate the array and which don't?

Mutating: `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`, `fill`, `copyWithin`.

Non-mutating (return something new): `map`, `filter`, `slice`, `concat`, `flat`, `flatMap`, `toSorted`, `toReversed`, `toSpliced`, `with`, plus read-only ones like `find`, `includes`, `indexOf`, `some`, `every`, `reduce`, `join`.

Knowing this matters for React and other state libraries, where changing an array in place can stop the UI from updating.

## 22: What are toSorted, toReversed, toSpliced and with?

They are non-mutating versions of `sort`, `reverse`, `splice` and index assignment, added in ES2023. Each returns a new array and leaves the original alone.

```js
const nums = [3, 1, 2];
nums.toSorted(); // [1, 2, 3]
nums.toReversed(); // [2, 1, 3]
nums.toSpliced(1, 1); // [3, 2]
nums.with(0, 99); // [99, 1, 2]
console.log(nums); // [3, 1, 2]
```

## 23: Why does [10, 1, 2].sort() give [1, 10, 2]?

Without a compare function, `sort` converts items to strings and compares them as text, and "10" comes before "2" in text order. Pass a compare function for numbers.

```js
[10, 1, 2].sort((a, b) => a - b); // [1, 2, 10]
```

## 24: What is the difference between find, findIndex, findLast and findLastIndex?

`find` returns the first element that matches, or `undefined`. `findIndex` returns its index, or `-1`. `findLast` and `findLastIndex` do the same thing starting from the end.

```js
const logs = [
  { lvl: "info" },
  { lvl: "error", id: 1 },
  { lvl: "error", id: 2 },
];
logs.find((l) => l.lvl === "error").id; // 1
logs.findLast((l) => l.lvl === "error").id; // 2
logs.findIndex((l) => l.lvl === "warn"); // -1
```

## 25: What is the difference between includes and indexOf?

`includes` returns a boolean, `indexOf` returns the position or `-1`. The other difference is `NaN`: `includes` uses SameValueZero, so it finds `NaN`, while `indexOf` uses `===`, so it doesn't.

```js
[NaN].includes(NaN); // true
[NaN].indexOf(NaN); // -1
```

## 26: How do you check if a value is an array?

Use `Array.isArray`. `typeof` returns `"object"` for arrays, so it can't tell them apart from other objects.

```js
typeof []; // "object"
Array.isArray([]); // true
Array.isArray({ length: 0 }); // false
```

`Array.isArray` also works for arrays that come from another iframe, where `instanceof Array` fails.

## 27: How do you swap two items in an array?

Use destructuring assignment.

```js
const arr = ["a", "b", "c"];
[arr[0], arr[2]] = [arr[2], arr[0]]; // ["c", "b", "a"]
```

For a non-mutating swap, use `with` twice: `arr.with(0, arr[2]).with(2, arr[0])`.

## 28: How do plain objects work as a data structure?

A plain object is a collection of key-value pairs. Keys are strings or symbols, values can be anything. Objects are the most common way to model a "record" (a user, a product) and are often used as simple dictionaries for lookups by key.

```js
const user = { id: 1, name: "Ana", active: true };
const priceById = { a1: 9.99, b2: 4.5 };
priceById["b2"]; // 4.5
```

## 29: What is the difference between dot notation and bracket notation?

Dot notation (`obj.name`) works when the key is a valid identifier written in code. Bracket notation (`obj["first-name"]`, `obj[key]`) works with any string, with keys that have spaces or dashes, and with keys stored in variables.

```js
const field = "email";
const user = { email: "a@b.com", "last-login": "today" };
user[field]; // "a@b.com"
user["last-login"]; // "today"
```

## 30: What do Object.keys, Object.values and Object.entries return?

They return arrays of an object's own enumerable string keys, their values, or `[key, value]` pairs. Symbol keys and inherited properties are left out.

```js
const scores = { ana: 10, ben: 7 };
Object.keys(scores); // ["ana", "ben"]
Object.values(scores); // [10, 7]
Object.entries(scores); // [["ana", 10], ["ben", 7]]
```

## 31: What does Object.fromEntries do?

It does the opposite of `Object.entries`: it builds an object from a list of `[key, value]` pairs. It also accepts a `Map`.

```js
const prices = { apple: 1, pear: 2 };
const doubled = Object.fromEntries(
  Object.entries(prices).map(([k, v]) => [k, v * 2]),
); // { apple: 2, pear: 4 }

Object.fromEntries(new Map([["a", 1]])); // { a: 1 }
```

## 32: How do you check if an object has a property?

- `"key" in obj` checks own and inherited properties.
- `Object.hasOwn(obj, "key")` checks only own properties.
- `obj.key !== undefined` is not reliable, because a property can exist and hold `undefined`.

```js
const o = { a: undefined };
"a" in o; // true
Object.hasOwn(o, "a"); // true
"toString" in o; // true, inherited
Object.hasOwn(o, "toString"); // false
```

## 33: Why is Object.hasOwn better than obj.hasOwnProperty?

`hasOwnProperty` is a method on `Object.prototype`, so it breaks on objects created with `Object.create(null)` (they don't have it) and on objects that have their own `hasOwnProperty` key. `Object.hasOwn(obj, key)` is a static function, so it always works.

```js
const dict = Object.create(null);
dict.x = 1;
// dict.hasOwnProperty("x"); // TypeError
Object.hasOwn(dict, "x"); // true
```

## 34: What does the delete operator do?

`delete obj.key` removes a property from an object and returns `true` (also when the property didn't exist). It doesn't free memory directly; it just removes the key, and the value can be garbage collected if nothing else uses it. On arrays, `delete arr[i]` leaves a hole instead of shifting items, so use `splice` or `filter` there. In hot code, deleting properties can also make objects slower in V8, which is one reason to use a `Map` for data that changes a lot.

## 35: What types can object keys be?

Only strings and symbols. Anything else is converted to a string. Numbers become `"1"`, and objects become `"[object Object]"`, which is a common bug.

```js
const o = {};
o[1] = "a";
o[{}] = "b";
console.log(Object.keys(o)); // ["1", "[object Object]"]
```

If you need real non-string keys, use a `Map`.

## 36: In what order are object keys listed?

Own string keys follow this order: first keys that look like array indexes ("0", "1", "42") in ascending number order, then other string keys in the order they were added. Symbol keys come after, also in insertion order.

```js
const o = { b: 1, 2: "x", a: 2, 1: "y" };
Object.keys(o); // ["1", "2", "b", "a"]
```

If you need full insertion order for any key, use a `Map`.

## 37: What does Object.freeze do?

`Object.freeze` makes an object's own properties read-only and stops new properties from being added or removed. In strict mode, writing to a frozen object throws; otherwise it's silently ignored. It's shallow: nested objects can still change.

```js
const config = Object.freeze({ api: "/v1", flags: { beta: true } });
config.api = "/v2"; // ignored (throws in strict mode)
config.flags.beta = false; // works, nested object isn't frozen
```

## 38: What is the difference between freeze, seal and preventExtensions?

- `Object.preventExtensions`: no new properties. You can still change and delete existing ones.
- `Object.seal`: no new properties and no deleting. You can still change values.
- `Object.freeze`: no adding, deleting or changing.

All three are shallow and can be checked with `Object.isExtensible`, `Object.isSealed` and `Object.isFrozen`.

## 39: How do you safely read deeply nested data?

Use optional chaining (`?.`). It stops and returns `undefined` if something in the chain is `null` or `undefined`, instead of throwing.

```js
const res = { data: { user: null } };
res.data.user?.address?.city; // undefined
res.data.items?.[0]; // undefined
res.onDone?.(); // calls only if it exists
```

## 40: How do you set a default for a missing value in a data structure?

Use `??` (nullish coalescing). It only falls back when the value is `null` or `undefined`, so real values like `0`, `""` and `false` are kept. `||` falls back on any falsy value, which is often wrong.

```js
const settings = { pageSize: 0 };
settings.pageSize || 20; // 20, wrong
settings.pageSize ?? 20; // 0, correct
```

## 41: What is a Map?

A `Map` is a built-in collection of key-value pairs where keys can be any value: strings, numbers, objects, functions. It keeps insertion order, knows its size, and is built for frequent adds and removes.

```js
const visits = new Map();
visits.set("/home", 3);
visits.set("/about", 1);
visits.get("/home"); // 3
visits.size; // 2
```

## 42: When should you use a Map instead of a plain object?

Use a `Map` when keys are not strings, when keys come from users or outside data (no risk of hitting `__proto__` or `constructor`), when you add and remove entries often, when you need the size quickly, or when insertion order matters for every key. Use a plain object for fixed-shape records (a user, a config) and for data you send as JSON.

## 43: What are the main methods of a Map?

```js
const m = new Map([["a", 1]]);
m.set("b", 2); // returns the map, so calls can chain
m.get("a"); // 1
m.has("c"); // false
m.delete("a"); // true
m.size; // 1
m.clear(); // empties it
```

## 44: How do you loop over a Map?

`Map` is iterable and gives `[key, value]` pairs in insertion order. You can also use `keys()`, `values()`, `entries()` or `forEach`.

```js
const m = new Map([
  ["x", 1],
  ["y", 2],
]);
for (const [key, value] of m) console.log(key, value);
m.forEach((value, key) => console.log(key, value));
[...m.keys()]; // ["x", "y"]
```

Note that `forEach` passes the value first, then the key.

## 45: How do you convert between a Map and an object?

```js
const obj = { a: 1, b: 2 };
const map = new Map(Object.entries(obj));
const back = Object.fromEntries(map);
```

Going from a Map to an object only makes sense when the keys are strings (or numbers you're fine turning into strings).

## 46: How does a Map compare keys?

It uses SameValueZero. That's like `===`, except `NaN` equals `NaN`, and `+0` and `-0` are the same key. Objects are compared by reference.

```js
const m = new Map();
m.set(NaN, "not a number");
m.get(NaN); // "not a number"
m.set(0, "zero");
m.get(-0); // "zero"
```

## 47: Why does map.get({ id: 1 }) return undefined after map.set({ id: 1 }, "x")?

Because those are two different objects. Map compares object keys by reference, not by content. To find the value you need the exact same object you used as the key.

```js
const key = { id: 1 };
const m = new Map([[key, "x"]]);
m.get(key); // "x"
m.get({ id: 1 }); // undefined
```

If you want to look up by content, use a primitive key like the id: `m.set(1, "x")`.

## 48: What is a Set?

A `Set` is a collection of unique values. Adding a value that's already there does nothing. It keeps insertion order and checks membership fast.

```js
const tags = new Set(["js", "css"]);
tags.add("js"); // no change
tags.has("css"); // true
tags.size; // 2
```

## 49: What are the main methods of a Set?

```js
const s = new Set();
s.add(1).add(2); // add returns the set
s.has(1); // true
s.delete(1); // true
s.size; // 1
s.clear();
```

A `Set` also has `keys()`, `values()`, `entries()` and `forEach`. `keys()` and `values()` are the same thing, and `entries()` gives `[value, value]` pairs so the API matches `Map`.

## 50: How do you remove duplicates from an array?

```js
const ids = [3, 1, 3, 2, 1];
const unique = [...new Set(ids)]; // [3, 1, 2]
```

This keeps the first time each value appears. It works for primitives. For objects with the same content, you need a key like `id` (see question 51).

## 51: Why doesn't a Set remove duplicate objects?

A `Set` checks uniqueness by reference. Two objects with the same fields are still two different objects.

```js
const s = new Set([{ id: 1 }, { id: 1 }]);
s.size; // 2

const users = [{ id: 1 }, { id: 1 }, { id: 2 }];
const uniqueUsers = [...new Map(users.map((u) => [u.id, u])).values()];
```

## 52: Does a Set keep the order of items?

Yes. A `Set` iterates in insertion order. If you delete a value and add it again, it moves to the end. That makes a `Set` handy for "recently used" lists where you want unique items in order.

## 53: What is a WeakMap?

A `WeakMap` is like a `Map`, but keys must be objects (or non-registered symbols), and it holds them weakly. If nothing else in your program references a key object, it can be garbage collected, and its entry goes away with it. It only has `get`, `set`, `has` and `delete`.

```js
const meta = new WeakMap();
let el = document.querySelector("#btn");
meta.set(el, { clicks: 0 });
el = null; // once the element is gone from the DOM too, the entry can be collected
```

## 54: What is a WeakSet?

A `WeakSet` is a set of objects held weakly. It answers "have I seen this object?" without keeping the object alive. It only has `add`, `has` and `delete`. A common use is marking objects as visited or processed.

```js
const processed = new WeakSet();
function handle(obj) {
  if (processed.has(obj)) return;
  processed.add(obj);
  // ...
}
```

## 55: Why can't you loop over a WeakMap or check its size?

Because entries can disappear at any time when the garbage collector runs. If you could list them, your code's result would depend on when GC happened, which isn't predictable. So `WeakMap` and `WeakSet` have no `size`, no `keys()` and no iteration.

## 56: What is a stack?

A stack is a Last In, First Out (LIFO) structure. You add to the top (push) and remove from the top (pop), like a stack of plates. The last item you put in is the first one you take out.

## 57: How do you implement a stack in JavaScript?

An array already works as a stack with `push` and `pop`, both O(1).

```js
const stack = [];
stack.push(1);
stack.push(2);
stack.at(-1); // 2, peek
stack.pop(); // 2
stack.length === 0; // isEmpty check
```

## 58: Where do stacks show up in front-end work?

Undo and redo in editors, the browser's back button, the JavaScript call stack, matching opening and closing tags or brackets, going "back" in a multi-step form or nested modal, and walking a tree without recursion. Any time you need "go back to the last thing", a stack is a good fit.

## 59: What is the call stack?

The call stack is how the JavaScript engine keeps track of which function is running. When you call a function, a frame with its local variables is pushed on the stack. When the function returns, its frame is popped and execution continues in the caller. The stack trace you see in an error is a snapshot of this stack.

## 60: What causes "Maximum call stack size exceeded"?

The call stack has a size limit. If functions keep calling each other without returning, usually from recursion with no base case or a base case that's never reached, the stack fills up and the engine throws a `RangeError`. Very deep but correct recursion (for example, over a tree with 100,000 levels) can hit it too. The fix is a correct base case, or switching to a loop with your own stack array.

## 61: What is a queue?

A queue is a First In, First Out (FIFO) structure. You add items at the back (enqueue) and take them from the front (dequeue), like a line at a shop. The first item in is the first one out.

## 62: Why is using an array with shift() a slow queue?

`push` to enqueue is O(1), but `shift` to dequeue is O(n) because every remaining element moves forward by one. With small queues it doesn't matter. With thousands of items processed in a loop, it turns an O(n) job into O(n²). A faster queue keeps a head index instead of shifting (see question 152).

## 63: Where do queues show up in front-end work?

The event loop's task and microtask queues, requests waiting for a free slot when you limit concurrency, toast notifications shown one after another, upload queues, animation frames, and breadth-first search over the DOM or a tree. Anywhere things must be handled in the order they arrived.

## 64: What is the difference between a stack and a queue?

Both hold items waiting to be handled. A stack takes out the most recent item first (LIFO), a queue takes out the oldest item first (FIFO). Depth-first search uses a stack, breadth-first search uses a queue. Undo uses a stack; a print or upload line uses a queue.

## 65: What is a deque?

A deque (double-ended queue, said "deck") lets you add and remove at both the front and the back in O(1). It can act as a stack or a queue. JavaScript arrays can do all four operations, but `shift` and `unshift` are O(n), so a real deque is usually built with a circular buffer or a doubly linked list.

## 66: What is a linked list?

A linked list is a chain of nodes. Each node holds a value and a reference to the next node. The list keeps a reference to the first node (the head). There's no index, so to reach the 50th item you walk from the head. In exchange, adding or removing a node at a known spot is O(1), with no shifting.

## 67: How do you write a linked list node in JavaScript?

```js
class ListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

const head = new ListNode(1, new ListNode(2, new ListNode(3)));
// 1 -> 2 -> 3 -> null
```

## 68: What is the difference between a singly and a doubly linked list?

In a singly linked list, each node points only to the next node, so you can only walk forward. In a doubly linked list, each node also points to the previous node. That costs one more reference per node, but lets you walk backward and remove a node in O(1) when you already have a reference to it, because you can reach its neighbor on both sides.

## 69: When would you pick a linked list over an array?

A linked list wins when you insert or remove items at the front or in the middle a lot and you already hold a reference to the spot. An array wins for reading by index, looping fast (data sits close together in memory), sorting and using all the built-in methods. In everyday JavaScript, arrays win most of the time. Linked lists are useful inside things like LRU caches and queues.

## 70: How do you loop over a linked list?

Start at the head and follow `next` until you hit `null`.

```js
function toArray(head) {
  const out = [];
  let node = head;
  while (node) {
    out.push(node.value);
    node = node.next;
  }
  return out;
}
```

## 71: How do you add a node to the start of a linked list?

Create a new node that points to the current head, then make it the new head. It's O(1), no matter how long the list is.

```js
function prepend(head, value) {
  return new ListNode(value, head);
}

let head = null;
head = prepend(head, 3);
head = prepend(head, 2); // 2 -> 3
```

## 72: What is a tree?

A tree is a structure made of nodes connected in a hierarchy. There's one root node at the top, and every other node has exactly one parent and any number of children. There are no loops. Folder structures, the DOM, menus with submenus, comment threads and org charts are all trees.

## 73: What do root, leaf, parent, child, depth and height mean in a tree?

- Root: the top node with no parent.
- Parent and child: a node directly above or below another.
- Siblings: nodes with the same parent.
- Leaf: a node with no children.
- Depth of a node: how many edges from the root to that node (the root has depth 0).
- Height of a tree: the depth of the deepest leaf.

## 74: Why is the DOM a tree?

The HTML document is nested: `html` holds `head` and `body`, `body` holds sections, sections hold paragraphs. Each element has one parent and a list of children, which is exactly a tree. That's why you have `parentNode`, `children`, `firstElementChild`, `nextElementSibling`, and why `querySelector` and event bubbling work by walking up or down the tree.

## 75: What is a binary tree?

A binary tree is a tree where each node has at most two children, usually called `left` and `right`. It's the base for binary search trees, heaps and expression trees.

```js
class TreeNode {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}
```

## 76: What is a binary search tree (BST)?

A BST is a binary tree with an ordering rule: for each node, every value in its left subtree is smaller and every value in its right subtree is bigger. That lets you search, insert and delete in O(log n) on average by going left or right at each step. If the tree becomes lopsided (for example, by inserting sorted data), it turns into a chain and those operations become O(n).

## 77: How do you represent a general tree in JavaScript?

Usually as objects with a `children` array. This is how menus, file trees and API responses often look.

```js
const tree = {
  id: "root",
  children: [
    { id: "docs", children: [{ id: "a.txt", children: [] }] },
    { id: "src", children: [] },
  ],
};
```

## 78: What is a graph?

A graph is a set of nodes (also called vertices) connected by edges. Unlike a tree, there's no root, a node can connect to any number of other nodes, and there can be cycles. Trees are actually a special kind of graph. Social networks, maps, links between web pages and module imports are graphs.

## 79: What is the difference between a directed and an undirected graph?

In an undirected graph, an edge goes both ways: if A is connected to B, B is connected to A (like friends on Facebook). In a directed graph, an edge has a direction: A can point to B without B pointing to A (like following on X, or module A importing module B).

## 80: What is a weighted graph?

A weighted graph has a number on each edge, like distance, cost or time. A map app uses weights for road lengths or travel times, so it can find the cheapest route, not just the one with the fewest steps.

## 81: What are the two common ways to store a graph?

An adjacency list stores, for each node, a list of its neighbors. It uses memory proportional to nodes plus edges and is the usual choice. An adjacency matrix is a 2D grid where `matrix[a][b]` says if there's an edge from a to b. It uses n² memory but checks a single edge in O(1). Sparse graphs (most real ones) use lists; small, dense graphs can use a matrix.

```js
const adj = new Map([
  ["A", ["B", "C"]],
  ["B", ["C"]],
  ["C", []],
]);
```

## 82: Where do graphs show up in web development?

Module dependency graphs in bundlers like Vite and webpack, routes between pages, social connections, recommendation systems, task dependencies in project tools, workflow editors, and state machines (states are nodes, transitions are edges). Even the DOM plus event listeners can be seen as a graph when you're debugging memory leaks.

## 83: What is a hash table?

A hash table stores key-value pairs in an array of buckets. A hash function turns each key into a number, which picks the bucket. Because you jump straight to the bucket instead of searching, lookup, insert and delete are O(1) on average. `Map`, `Set` and plain objects in JavaScript engines are all built on hash tables in some form.

## 84: What is a hash function?

A function that turns a key into a number (a hash), which is then used to pick a bucket. A good hash function is fast, always gives the same output for the same input, and spreads keys evenly across buckets so they don't pile up in one place.

## 85: What is a hash collision?

A collision happens when two different keys get the same bucket. It can't be avoided completely, because there are more possible keys than buckets. Hash tables handle it either by keeping a small list in each bucket (chaining) or by looking for the next free bucket (open addressing). Too many collisions make lookups slow, closer to O(n).

## 86: Are JavaScript objects and Maps hash tables?

From your point of view, yes: both give fast lookups by key. Under the hood it's more complex. V8 stores objects with a fixed set of keys using hidden classes (shapes), which is faster than a hash table, and switches to a hash table ("dictionary mode") when an object has lots of added and removed keys. `Map` and `Set` are always hash tables that also remember insertion order.

## 87: What is a heap?

A heap is a tree-shaped structure where every parent is ordered relative to its children. In a min heap, every parent is smaller than or equal to its children, so the smallest item is always at the top. It's usually stored in a plain array. Getting the top is O(1), adding or removing is O(log n). It's the standard way to build a priority queue.

Note: this "heap" is a data structure. It's not the same thing as the memory heap where JavaScript stores objects.

## 88: What is the difference between a min heap and a max heap?

A min heap keeps the smallest value at the top, a max heap keeps the largest. Same structure, opposite order. In JavaScript you usually write one heap class that takes a compare function, and pass `(a, b) => a - b` for min or `(a, b) => b - a` for max.

## 89: What is a priority queue?

A priority queue is a queue where each item has a priority, and you always take out the item with the highest (or lowest) priority first, not the oldest one. Think of an emergency room. It's usually built with a heap. Examples: task schedulers, Dijkstra's shortest path, and picking the next most important notification.

## 90: What is a trie?

A trie (prefix tree) stores strings character by character. Each node is one character, and a path from the root spells out a word. Words with the same start share nodes. It makes prefix lookups fast, which is why it's used for autocomplete, spell checkers and routers that match URL paths.

## 91: What is a matrix and how do you store one in JavaScript?

A matrix is a 2D grid of values in rows and columns. In JavaScript you usually store it as an array of arrays, and read a cell with `grid[row][col]`. Game boards, images, spreadsheets and seating charts are all matrices.

```js
const board = [
  ["X", "O", "X"],
  [" ", "X", "O"],
  ["O", " ", "X"],
];
board[1][2]; // "O"
```

## 92: Is a string a data structure?

Yes. A string is an ordered, read-only sequence of UTF-16 code units. You can read characters by index and get the length, like an array, but you can't change a character in place. String methods like `slice`, `toUpperCase` and `replace` always return a new string.

## 93: What does it mean that strings are immutable?

You can't change a string after it's created. `str[0] = "X"` does nothing (or throws in strict mode). Every "change" creates a new string. That's why building a big string with `+=` in a loop can create lots of temporary strings; collecting parts in an array and calling `join("")` is the common alternative, though modern engines handle `+=` well in most cases.

## 94: How do you turn a string into an array of characters correctly?

`str.split("")` splits by UTF-16 code units, which breaks emoji and some other characters into two broken halves. `Array.from(str)` and `[...str]` split by code points, which is correct for most characters.

```js
const s = "hi😀";
s.split("").length; // 4
[...s].length; // 3
```

For characters made of several code points (like family emoji or flags), use `Intl.Segmenter` to split by what the user sees as one character.

## 95: Does JavaScript have tuples?

Not as a separate type. People use short arrays as tuples, for example `[key, value]` pairs from `Object.entries`, or `[state, setState]` from React's `useState`. TypeScript adds tuple types like `[string, number]` that check the length and type of each position, but at runtime it's still an array.

## 96: What happened to the Records and Tuples proposal?

It proposed deeply immutable `#{ }` and `#[ ]` values that would be compared by content, so `#[1, 2] === #[1, 2]` would be `true`. It stayed at Stage 2 for years and was withdrawn in 2025, mainly because engine teams had performance concerns with the new `===` behavior. A follow-up idea about value-based keys for `Map` and `Set` is being discussed separately, but today you still compare objects by reference or by your own code.

## 97: What is JSON?

JSON (JavaScript Object Notation) is a text format for data. It supports objects, arrays, strings, numbers, booleans and `null`. It's the standard format for APIs and config files. In JavaScript you convert with `JSON.stringify` (value to text) and `JSON.parse` (text to value).

## 98: What is the difference between JSON and a JavaScript object?

JSON is a string; a JavaScript object lives in memory. JSON is also stricter: keys must be double-quoted strings, there are no comments, no trailing commas, no `undefined`, no functions, no `Date`, `Map` or `Set`. Any JSON text is valid JavaScript syntax, but most JavaScript objects can't be turned into JSON without losing something.

## 99: What does JSON.stringify skip or change?

- `undefined`, functions and symbols: dropped from objects, turned into `null` in arrays.
- `NaN` and `Infinity`: become `null`.
- `Date`: becomes an ISO string (through its `toJSON` method).
- `Map` and `Set`: become `{}`.
- `BigInt`: throws a `TypeError`.
- Circular references: throws a `TypeError`.

```js
JSON.stringify({ a: undefined, b: [undefined], c: new Map([[1, 2]]) });
// '{"b":[null],"c":{}}'
```

## 100: How do you save a Map or Set as JSON?

Turn it into an array first, and turn it back after parsing.

```js
const m = new Map([
  ["a", 1],
  ["b", 2],
]);
const json = JSON.stringify([...m]); // '[["a",1],["b",2]]'
const restored = new Map(JSON.parse(json));

const s = new Set([1, 2]);
const restoredSet = new Set(JSON.parse(JSON.stringify([...s])));
```

## 101: What is an iterable?

An iterable is any object that has a `Symbol.iterator` method returning an iterator. Iterables work with `for...of`, spread (`...`), destructuring, `Array.from`, `new Map()`, `new Set()`, `Promise.all` and more. It's the common way JavaScript loops over different data structures.

## 102: Which built-in types are iterable?

Arrays, strings, `Map`, `Set`, typed arrays, `arguments`, DOM collections like `NodeList`, and the iterators returned by generators and methods like `map.entries()`. Plain objects are not iterable, so `for (const x of {})` throws. Use `Object.entries(obj)` to loop over an object with `for...of`.

## 103: What is the difference between for...of and for...in?

`for...of` loops over the values of an iterable (array items, string characters, Map entries). `for...in` loops over the enumerable string keys of an object, including inherited ones. Don't use `for...in` on arrays: you get string indexes, possibly in odd order, plus any extra properties.

```js
const arr = ["a", "b"];
for (const v of arr) console.log(v); // "a", "b"
for (const k in arr) console.log(k); // "0", "1"
```

## 104: What does the spread operator work on?

In arrays and function calls (`[...x]`, `fn(...x)`), spread works on any iterable: arrays, strings, Maps, Sets, generators. In object literals (`{...x}`), it copies own enumerable properties from any object. That's why `[...new Set(arr)]` works but `[...{a: 1}]` throws, while `{...[1, 2]}` gives `{0: 1, 1: 2}`.

## 105: What is an array-like object and how do you turn it into an array?

An array-like object has a `length` and indexed keys but isn't a real array, so it lacks methods like `map`. Examples: `arguments`, some DOM collections, and `{ length: 2, 0: "a", 1: "b" }`.

```js
const arrayLike = { length: 2, 0: "a", 1: "b" };
Array.from(arrayLike); // ["a", "b"]
Array.prototype.map.call(arrayLike, (s) => s.toUpperCase());
```

Spread only works if the object is also iterable.

## 106: What is the difference between a NodeList and an HTMLCollection?

Both are array-like lists of DOM nodes. `querySelectorAll` returns a static `NodeList`: a snapshot that doesn't change when the DOM changes. `getElementsByClassName`, `getElementsByTagName` and `element.children` return a live `HTMLCollection` that updates on its own. A live list can surprise you if you remove elements while looping over it. `NodeList` has `forEach`; `HTMLCollection` doesn't, so use `Array.from` or `for...of`.

## 107: What is a typed array?

A typed array is an array-like view over raw binary memory where every item has the same numeric type and size, like `Uint8Array` (bytes), `Int32Array` or `Float64Array`. The length is fixed when you create it. They're used for images, audio, WebGL, WebSockets with binary data, file parsing and fast number crunching.

```js
const bytes = new Uint8Array(4);
bytes[0] = 255;
bytes[1] = 256; // wraps to 0
```

## 108: What is an ArrayBuffer?

An `ArrayBuffer` is a fixed-size block of raw bytes. You can't read it directly. You create a view on top of it, a typed array or a `DataView`, to read and write numbers in a specific format. Several views can share one buffer.

```js
const buf = new ArrayBuffer(8);
const view = new Uint32Array(buf); // 2 items of 4 bytes each
view[0] = 42;
```

## 109: What is the difference between a normal array and a typed array?

A normal array can hold any type, can grow and shrink, and can have holes. A typed array holds only one numeric type, has a fixed length, is always dense, and stores numbers as raw bytes. Typed arrays use much less memory for numbers and can be sent to Web Workers or WebGL without conversion. They lack methods that change length, like `push` and `splice`.

## 110: What is a Symbol and why use one as an object key?

A `Symbol` is a unique primitive value. Two symbols are never equal, even with the same description. As object keys, they don't collide with string keys, they're skipped by `Object.keys`, `for...in` and `JSON.stringify`, so they're useful for hidden or library-level metadata. Well-known symbols like `Symbol.iterator` let you plug into language features.

```js
const id = Symbol("id");
const user = { name: "Ana", [id]: 123 };
Object.keys(user); // ["name"]
user[id]; // 123
```

## 111: What is the difference between mutable and immutable data?

Mutable data can be changed in place: `arr.push(x)`, `obj.name = "x"`. Immutable data never changes; to "update" it you make a new copy with the change. Immutable updates are easier to reason about and let you detect changes with a cheap `===` check, which is why React, Redux and many other libraries expect them. The cost is extra copying.

## 112: Why do React and Redux want you to update state immutably?

They detect changes by comparing references. If you mutate an array and pass the same array back, `oldState === newState` is `true`, so React may skip the re-render and memoized components won't update. Creating a new array or object for every change gives a new reference, which is a quick and reliable signal that something changed.

```js
setTodos((todos) => [...todos, newTodo]); // new array, React re-renders
```

## 113: How do you update a nested object without mutating it?

Copy every level on the path to the value you change, and keep the rest as is.

```js
const state = { user: { name: "Ana", address: { city: "Tbilisi" } } };

const next = {
  ...state,
  user: {
    ...state.user,
    address: { ...state.user.address, city: "Batumi" },
  },
};
```

Libraries like Immer let you write this as a normal mutation and do the copying for you.

## 114: How do you add, remove and update items in an array without mutating it?

```js
const list = [
  { id: 1, done: false },
  { id: 2, done: false },
];

const added = [...list, { id: 3, done: false }];
const removed = list.filter((item) => item.id !== 1);
const updated = list.map((item) =>
  item.id === 2 ? { ...item, done: true } : item,
);
const atIndex = list.with(0, { id: 1, done: true });
```

## 115: How do you choose the right data structure for a task?

Start from the operations you'll do most often and how many items you'll have. Need order and index access? Array. Fast lookup by key? `Map` or object. Uniqueness or fast "is it there"? `Set`. Last-in-first-out? Stack. First-in-first-out? Queue. Hierarchy? Tree. Connections between things? Graph. Always the smallest or largest next? Heap. For small data, the simplest option is usually fine.

## 116: What does Object.groupBy do?

`Object.groupBy` (ES2024) groups items of any iterable into an object, using the key your callback returns.

```js
const products = [
  { name: "apple", type: "fruit" },
  { name: "carrot", type: "veg" },
  { name: "pear", type: "fruit" },
];
const byType = Object.groupBy(products, (p) => p.type);
// { fruit: [apple, pear], veg: [carrot] }
```

The result is an object with a `null` prototype, so it has no `toString` or `hasOwnProperty` methods.

## 117: How is Map.groupBy different from Object.groupBy?

`Map.groupBy` returns a `Map` instead of an object. Use it when the group keys aren't strings, for example objects, or when you want `Map` features like `size`.

```js
const byLength = Map.groupBy(["a", "bb", "cc"], (s) => s.length);
byLength.get(2); // ["bb", "cc"]
```

## 118: What do flat and flatMap do?

`flat(depth)` turns nested arrays into a flatter array. The default depth is 1, and `Infinity` flattens everything. `flatMap` maps each item and then flattens by one level, which is handy when each item turns into zero, one or many items.

```js
[1, [2, [3, [4]]]].flat(); // [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat(Infinity); // [1, 2, 3, 4]
["a b", "c"].flatMap((s) => s.split(" ")); // ["a", "b", "c"]
```

## 119: How do you count how many times each value appears?

Use a `Map` (or an object) as a counter.

```js
const words = ["js", "css", "js", "html", "js"];
const counts = new Map();
for (const w of words) counts.set(w, (counts.get(w) ?? 0) + 1);
counts.get("js"); // 3
```

## 120: How can you use an object or Map as a lookup table instead of a switch?

Put the cases in an object or `Map` and read by key. It's shorter, easier to extend, and the data can live outside the function.

```js
const statusText = {
  200: "OK",
  404: "Not Found",
  500: "Server Error",
};
const label = statusText[code] ?? "Unknown";
```

## 121: How do you turn an array of objects into an object keyed by id?

This is often called indexing or normalizing, and it turns repeated O(n) `find` calls into O(1) lookups.

```js
const users = [
  { id: "u1", name: "Ana" },
  { id: "u2", name: "Ben" },
];
const byId = Object.fromEntries(users.map((u) => [u.id, u]));
// or: const byId = new Map(users.map(u => [u.id, u]));
byId.u2.name; // "Ben"
```

## 122: What is a dictionary (associative array)?

A dictionary is a collection where you look up values by a key instead of a number index. Other languages call it a map, hash or dict. In JavaScript you use a `Map` or a plain object for it. It's one of the most used structures in everyday code: caches, translations, settings, counters, indexes by id.

## 123: How do you build a simple cache?

Store computed results in a `Map` keyed by the input, and check it before doing the work again.

```js
const cache = new Map();
function getSquare(n) {
  if (cache.has(n)) return cache.get(n);
  const result = n * n; // pretend this is slow
  cache.set(n, result);
  return result;
}
```

A cache like this grows forever, so real ones add a size limit or expiry (see questions 184 and 271).

## 124: What operations does a stack usually have?

`push(item)` adds to the top, `pop()` removes and returns the top, `peek()` returns the top without removing it, `isEmpty()` checks if it's empty, and `size` gives the count. All of them should be O(1).

## 125: What is a circular buffer (ring buffer)?

A circular buffer is a fixed-size array where the end wraps around to the start. It keeps a read index and a write index. When it's full, new items either overwrite the oldest ones or get rejected. It's used for things like keeping the last 100 log lines, audio buffers, and fast queues where you know the maximum size.

## 126: What new methods does Set have?

Since ES2025, `Set` has methods for set math. They return a new `Set` or a boolean and don't change the original.

```js
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

a.union(b); // {1, 2, 3, 4}
a.intersection(b); // {2, 3}
a.difference(b); // {1}
a.symmetricDifference(b); // {1, 4}
a.isSubsetOf(b); // false
a.isSupersetOf(new Set([1])); // true
a.isDisjointFrom(new Set([9])); // true
```

## 127: What is the difference between difference and symmetricDifference?

`a.difference(b)` gives items that are in `a` but not in `b`. `a.symmetricDifference(b)` gives items that are in exactly one of the two sets, so it's like `a.difference(b)` plus `b.difference(a)`. For example, to find tags that were removed, use `oldTags.difference(newTags)`; to find all tags that changed in either direction, use `symmetricDifference`.

## 128: How do you check if an array or object is empty?

```js
const arr = [];
arr.length === 0; // true

const obj = {};
Object.keys(obj).length === 0; // true

const m = new Map();
m.size === 0; // true
```

Note that `Object.keys` only checks own enumerable string keys, which is what you want in almost every case.

## 129: What does splice do?

`splice(start, deleteCount, ...items)` changes an array in place: it removes `deleteCount` items starting at `start`, inserts the new items there, and returns the removed items.

```js
const arr = ["a", "b", "c", "d"];
const removed = arr.splice(1, 2, "x"); // removed = ["b", "c"]
console.log(arr); // ["a", "x", "d"]
```

Use `toSpliced` if you want the same result as a new array.

## 130: What is the difference between slice and splice?

`slice(start, end)` returns a copy of part of the array and doesn't change the original. `splice(start, count, ...items)` changes the original by removing and/or adding items, and returns what was removed. Easy way to remember: splice has a "p" for "permanent" change.

## 131: What is the difference between concat and spread for joining arrays?

Both return a new array. Spread works with any iterable and lets you put items anywhere: `[first, ...a, ...b, last]`. `concat` is a method that flattens array arguments one level and adds other values as they are. For joining a few arrays, they're the same in practice, so pick what reads better.

```js
const a = [1],
  b = [2];
[...a, ...b]; // [1, 2]
a.concat(b, 3); // [1, 2, 3]
```

## 132: What is the difference between a Map's size and an object's key count?

A `Map` keeps a `size` property that's always up to date, so reading it is O(1). An object doesn't track its key count; `Object.keys(obj).length` builds an array of keys every time, which is O(n). If you check the count often, a `Map` is a better fit.

## 133: How do you empty a Map or a Set?

Call `clear()`. It removes all entries in place, so every other reference to the same Map or Set sees it empty.

```js
const seen = new Set([1, 2, 3]);
seen.clear();
seen.size; // 0
```

## 134: Why is [] === [] false?

Arrays and objects are compared by reference. `[] === []` creates two different arrays, so they're not the same reference, even though both are empty. The same goes for `{} === {}`. To compare by content you need to check the items yourself or use a deep equality helper.

## 135: How do you compare two objects by their content?

For a shallow check, compare the keys and each value.

```js
function shallowEqual(a, b) {
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every((k) => Object.hasOwn(b, k) && Object.is(a[k], b[k]));
}
shallowEqual({ x: 1 }, { x: 1 }); // true
```

React uses this kind of shallow check for `memo` and many state libraries do the same. For nested data you need a deep comparison (see question 209).

## 136: What is the difference between linear and non-linear data structures?

In a linear structure, items are in a sequence and each one has at most one before and one after: arrays, linked lists, stacks, queues. In a non-linear structure, an item can connect to several others: trees, graphs, heaps, tries. Linear ones are walked with a simple loop; non-linear ones need traversal like depth-first or breadth-first search.

## 137: What is the difference between static and dynamic data structures?

A static structure has a fixed size set when it's created, like a typed array or a fixed ring buffer. A dynamic structure can grow and shrink, like a JavaScript array, `Map` or linked list. Static ones are predictable in memory use; dynamic ones are more flexible but may need to reallocate memory when they grow.

## 138: What is an abstract data type (ADT)?

An ADT describes what a structure does, not how it's built. A "stack" is an ADT: push, pop, peek, LIFO. You can build it with an array or a linked list, and code that uses it doesn't need to know which. Thinking in ADTs helps you swap implementations later, for example replacing an array queue with a faster one, without changing the callers.

## 139: What is a node in a data structure?

A node is one unit in a linked structure like a linked list, tree or graph. It holds a value and references to other nodes (`next`, `left`, `right`, `children`, `parent`). In JavaScript, a node is just an object, and the "references" are normal object references.

## 140: Does JavaScript have pointers?

Not in the C sense: you can't get a memory address or do pointer math. But every object variable holds a reference, and references work like safe pointers. That's all you need to build linked lists, trees and graphs: a node's `next` property holds a reference to another node object.

## 141: How does garbage collection decide what to free?

JavaScript engines free objects that are no longer reachable. Starting from roots (global variables, the current call stack, active closures), the collector follows every reference. Anything it can't reach is garbage. So a data structure stays in memory as long as something reachable still points to it, even if your code never uses it again.

## 142: How can a Map cause a memory leak?

A `Map` holds strong references to its keys and values. If you use objects (like DOM nodes or component instances) as keys and never delete them, they can't be garbage collected, even after they're removed from the page. The `Map` keeps them alive. Use a `WeakMap` when the entry should live only as long as the key object does, or remember to delete entries.

```js
const listeners = new Map();
listeners.set(element, handler);
element.remove(); // element is still kept alive by the Map
```

## 143: What is the difference between null and an empty structure?

`null` means "there is no value", while `[]`, `{}` or `new Map()` means "there is a value, and it's empty". APIs that return `[]` for "no results" are easier to use, because callers can call `map` or `length` without null checks. Keep `null` for cases where "missing" and "empty" mean different things, like "not loaded yet" versus "loaded with zero items".

## 144: How do you loop over an object's keys and values?

```js
const prices = { apple: 1.2, pear: 0.8 };

for (const [name, price] of Object.entries(prices)) {
  console.log(name, price);
}
```

`Object.entries` only includes own enumerable string keys, so you don't pick up inherited properties like you can with `for...in`.

## 145: How do you transform all values of an object?

Turn it into entries, map them, and build a new object.

```js
const celsius = { mon: 20, tue: 25 };
const fahrenheit = Object.fromEntries(
  Object.entries(celsius).map(([day, c]) => [day, (c * 9) / 5 + 32]),
);
// { mon: 68, tue: 77 }
```

## 146: How do you create a Map from an array of pairs?

Pass any iterable of `[key, value]` pairs to the constructor.

```js
const pairs = [
  ["en", "Hello"],
  ["ka", "Gamarjoba"],
];
const greetings = new Map(pairs);
greetings.get("ka"); // "Gamarjoba"
```

## 147: What happens if you use an object as a key in a plain object?

The object is converted to a string, which for plain objects is always `"[object Object]"`. So every object key ends up on the same property and overwrites the others.

```js
const a = { id: 1 },
  b = { id: 2 };
const store = {};
store[a] = "first";
store[b] = "second";
store[a]; // "second"
```

Use a `Map` or `WeakMap` for object keys.

## 148: What are the most common data structures asked about in front-end interviews?

Arrays and their methods, objects, `Map` and `Set` (and when to use each), `WeakMap`, stacks, queues, linked lists, trees (especially the DOM and nested JSON), binary search trees, heaps or priority queues, tries for autocomplete, graphs for dependencies, and hash tables. Also practical things: immutable updates, deep vs shallow copies, normalizing API data and building an LRU cache.

## 149: What is the difference between an array and a Set for storing unique items?

An array allows duplicates and checks membership with `includes` in O(n). A `Set` only keeps unique values and checks with `has` in O(1) on average. An array gives you index access, sorting and all array methods; a `Set` doesn't. Many projects keep data in a `Set` for fast checks and turn it into an array (`[...set]`) when they need to render or sort it.

## 150: Why should you know the cost of operations on each structure?

Because the same code can be fast with one structure and slow with another. `list.find(x => x.id === id)` inside a loop over 10,000 items is 100 million checks; a `Map` lookup makes it 10,000. `arr.shift()` in a loop over a big queue is O(n²); a head index makes it O(n). On the front end, slow code blocks the main thread and makes the page freeze, so knowing these costs pays off directly.

# Moderate Questions (151-300)

## 151: How do you write a Stack class with private fields?

Private fields (`#items`) stop outside code from changing the internal array and breaking the stack rules.

```js
class Stack {
  #items = [];

  push(item) {
    this.#items.push(item);
    return this;
  }
  pop() {
    return this.#items.pop();
  }
  peek() {
    return this.#items.at(-1);
  }
  get size() {
    return this.#items.length;
  }
  isEmpty() {
    return this.#items.length === 0;
  }
}
```

## 152: How do you build a queue with O(1) dequeue?

Keep the items in an object (or array) and track a head and tail index instead of calling `shift`.

```js
class Queue {
  #items = {};
  #head = 0;
  #tail = 0;

  enqueue(item) {
    this.#items[this.#tail++] = item;
  }
  dequeue() {
    if (this.#head === this.#tail) return undefined;
    const item = this.#items[this.#head];
    delete this.#items[this.#head++];
    return item;
  }
  peek() {
    return this.#items[this.#head];
  }
  get size() {
    return this.#tail - this.#head;
  }
}
```

Another common version uses an array with a head index and cuts off the used front part once it gets big (`items = items.slice(head); head = 0`).

## 153: How do you build a queue using two stacks?

Push new items onto an "in" stack. To dequeue, pop from an "out" stack; if it's empty, move everything from "in" to "out" first, which reverses the order. Each item moves at most once, so dequeue is O(1) amortized.

```js
class TwoStackQueue {
  #in = [];
  #out = [];

  enqueue(x) {
    this.#in.push(x);
  }
  dequeue() {
    if (this.#out.length === 0) {
      while (this.#in.length) this.#out.push(this.#in.pop());
    }
    return this.#out.pop();
  }
  get size() {
    return this.#in.length + this.#out.length;
  }
}
```

## 154: How do you build a deque with O(1) operations at both ends?

One simple way uses an object with two indexes that can go negative.

```js
class Deque {
  #items = {};
  #front = 0; // index of first item
  #back = 0; // index after last item

  pushBack(x) {
    this.#items[this.#back++] = x;
  }
  pushFront(x) {
    this.#items[--this.#front] = x;
  }
  popBack() {
    if (this.size === 0) return undefined;
    const x = this.#items[--this.#back];
    delete this.#items[this.#back];
    return x;
  }
  popFront() {
    if (this.size === 0) return undefined;
    const x = this.#items[this.#front];
    delete this.#items[this.#front++];
    return x;
  }
  get size() {
    return this.#back - this.#front;
  }
}
```

A circular buffer over an array is faster in practice (see question 378), but this version is easy to write in an interview.

## 155: How do you implement a singly linked list with append, prepend and remove?

Keep both `head` and `tail` so appending is O(1).

```js
class LinkedList {
  head = null;
  tail = null;
  size = 0;

  append(value) {
    const node = { value, next: null };
    if (!this.head) this.head = this.tail = node;
    else this.tail = this.tail.next = node;
    this.size++;
  }

  prepend(value) {
    this.head = { value, next: this.head };
    if (!this.tail) this.tail = this.head;
    this.size++;
  }

  remove(value) {
    if (!this.head) return false;
    if (this.head.value === value) {
      this.head = this.head.next;
      if (!this.head) this.tail = null;
      this.size--;
      return true;
    }
    let prev = this.head;
    while (prev.next && prev.next.value !== value) prev = prev.next;
    if (!prev.next) return false;
    if (prev.next === this.tail) this.tail = prev;
    prev.next = prev.next.next;
    this.size--;
    return true;
  }
}
```

## 156: How do you implement a doubly linked list?

Each node has `prev` and `next`. Removing a node you already have is O(1), because you can reach both neighbors.

```js
class DoublyLinkedList {
  head = null;
  tail = null;

  push(value) {
    const node = { value, prev: this.tail, next: null };
    if (this.tail) this.tail.next = node;
    else this.head = node;
    this.tail = node;
    return node;
  }

  removeNode(node) {
    if (node.prev) node.prev.next = node.next;
    else this.head = node.next;
    if (node.next) node.next.prev = node.prev;
    else this.tail = node.prev;
    node.prev = node.next = null;
  }
}
```

## 157: What edge cases should you test in a linked list?

Empty list, list with one node, removing the head, removing the tail (and updating `tail`), removing a value that doesn't exist, duplicate values, and making sure `size` stays right after every operation. Most bugs in linked list code come from forgetting to update `head` or `tail` when the list becomes empty or has one node.

## 158: How do you find the middle of a linked list in one pass?

Use two pointers: `slow` moves one step and `fast` moves two. When `fast` reaches the end, `slow` is in the middle.

```js
function middle(head) {
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}
```

For an even length this returns the second of the two middle nodes.

## 159: How do you check if a linked list has a cycle?

Use the same slow and fast pointers. If there's a cycle, the fast one eventually laps the slow one and they meet. If `fast` reaches `null`, there's no cycle. This uses O(1) memory, unlike storing visited nodes in a `Set`.

```js
function hasCycle(head) {
  let slow = head,
    fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

## 160: How do you make a linked list work with for...of and spread?

Add a `[Symbol.iterator]` method. A generator makes it short.

```js
class LinkedList {
  head = null;
  // ...append, prepend...

  *[Symbol.iterator]() {
    let node = this.head;
    while (node) {
      yield node.value;
      node = node.next;
    }
  }
}

const list = new LinkedList();
// after adding items:
[...list];
for (const v of list) console.log(v);
```

## 161: What is a circular linked list and where is it used?

In a circular linked list, the last node points back to the first instead of `null`. You can go around forever, which fits round-robin scheduling, image carousels that loop, turn order in games and playlists on repeat. When you loop over it, stop when you get back to the starting node, or you'll never finish.

## 162: How do you insert a value into a binary search tree?

Start at the root, go left if the value is smaller and right if it's bigger, and put the new node in the first empty spot.

```js
class BST {
  root = null;

  insert(value) {
    const node = { value, left: null, right: null };
    if (!this.root) {
      this.root = node;
      return;
    }
    let cur = this.root;
    while (true) {
      if (value === cur.value) return; // ignore duplicates
      const side = value < cur.value ? "left" : "right";
      if (!cur[side]) {
        cur[side] = node;
        return;
      }
      cur = cur[side];
    }
  }
}
```

## 163: How do you find the smallest and largest values in a BST?

The smallest value is the leftmost node; the largest is the rightmost node. Just keep going left (or right) until there's no child.

```js
function min(node) {
  while (node?.left) node = node.left;
  return node?.value;
}
function max(node) {
  while (node?.right) node = node.right;
  return node?.value;
}
```

## 164: How do you delete a node from a BST?

There are three cases. A leaf: just remove it. A node with one child: replace it with that child. A node with two children: replace its value with its in-order successor (the smallest value in its right subtree), then delete that successor from the right subtree.

```js
function remove(node, value) {
  if (!node) return null;
  if (value < node.value) node.left = remove(node.left, value);
  else if (value > node.value) node.right = remove(node.right, value);
  else {
    if (!node.left) return node.right;
    if (!node.right) return node.left;
    let succ = node.right;
    while (succ.left) succ = succ.left;
    node.value = succ.value;
    node.right = remove(node.right, succ.value);
  }
  return node;
}
// bst.root = remove(bst.root, 5);
```

## 165: How do you do an in-order traversal of a BST without recursion?

Use your own stack. Go left as far as you can, pushing nodes; then pop one, visit it, and move to its right child. For a BST this gives the values in sorted order.

```js
function* inOrder(root) {
  const stack = [];
  let node = root;
  while (node || stack.length) {
    while (node) {
      stack.push(node);
      node = node.left;
    }
    node = stack.pop();
    yield node.value;
    node = node.right;
  }
}
```

Using a generator means callers can stop early, for example after the first 10 values.

## 166: How do you walk a tree level by level?

Use a queue (breadth-first). Process all nodes at the current level before moving to the next.

```js
function levels(root) {
  if (!root) return [];
  const result = [];
  let level = [root];
  while (level.length) {
    result.push(level.map((n) => n.value));
    level = level.flatMap((n) => [n.left, n.right].filter(Boolean));
  }
  return result;
}
```

Swapping the whole level array each round avoids `shift` and makes grouping by level easy.

## 167: How do you check if a binary tree is a valid BST?

Each node must be within a range set by its ancestors, not just bigger than its left child and smaller than its right child. Pass the allowed range down.

```js
function isValidBST(node, min = -Infinity, max = Infinity) {
  if (!node) return true;
  if (node.value <= min || node.value >= max) return false;
  return (
    isValidBST(node.left, min, node.value) &&
    isValidBST(node.right, node.value, max)
  );
}
```

The common mistake is only comparing a node with its direct children, which passes trees like `5 -> left 3 -> right 7`, where 7 is wrongly on the left of 5.

## 168: How do you count the nodes and leaves of a tree?

```js
function countNodes(node) {
  if (!node) return 0;
  return 1 + countNodes(node.left) + countNodes(node.right);
}

function countLeaves(node) {
  if (!node) return 0;
  if (!node.left && !node.right) return 1;
  return countLeaves(node.left) + countLeaves(node.right);
}
```

For a general tree with `children`, sum over the children array instead of `left` and `right`.

## 169: How do you find a node by id in a nested tree, like a menu?

Depth-first search with a stack works for any depth without risking a stack overflow.

```js
function findById(root, id) {
  const stack = [root];
  while (stack.length) {
    const node = stack.pop();
    if (node.id === id) return node;
    if (node.children) stack.push(...node.children);
  }
  return null;
}
```

If you look up nodes by id often, build a `Map` of id to node once and reuse it.

## 170: How do you flatten a tree into a list?

Walk the tree and collect each node, often with its depth so you can render it with indentation (like a tree view or nested comments).

```js
function flatten(nodes, depth = 0, out = []) {
  for (const node of nodes) {
    out.push({ id: node.id, name: node.name, depth });
    if (node.children?.length) flatten(node.children, depth + 1, out);
  }
  return out;
}
```

A flat list is easier to virtualize, filter and keep keyboard focus in than a deeply nested one.

## 171: How do you implement a min heap?

Store it in an array. Add to the end and move it up while it's smaller than its parent. To remove the top, move the last item to the top and move it down while it's bigger than a child.

```js
class MinHeap {
  #a = [];
  constructor(compare = (x, y) => x - y) {
    this.compare = compare;
  }
  get size() {
    return this.#a.length;
  }
  peek() {
    return this.#a[0];
  }

  push(value) {
    const a = this.#a;
    a.push(value);
    let i = a.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.compare(a[i], a[p]) >= 0) break;
      [a[i], a[p]] = [a[p], a[i]];
      i = p;
    }
  }

  pop() {
    const a = this.#a;
    if (a.length === 0) return undefined;
    const top = a[0];
    const last = a.pop();
    if (a.length) {
      a[0] = last;
      let i = 0;
      while (true) {
        const l = 2 * i + 1,
          r = l + 1;
        let m = i;
        if (l < a.length && this.compare(a[l], a[m]) < 0) m = l;
        if (r < a.length && this.compare(a[r], a[m]) < 0) m = r;
        if (m === i) break;
        [a[i], a[m]] = [a[m], a[i]];
        i = m;
      }
    }
    return top;
  }
}
```

## 172: How does a heap fit into a plain array?

A heap is a complete binary tree (every level is full except maybe the last, which fills from the left), so it can be stored in an array with no gaps. For a node at index `i`:

- left child: `2 * i + 1`
- right child: `2 * i + 2`
- parent: `Math.floor((i - 1) / 2)`

No node objects or pointers are needed, which saves memory and keeps data close together.

## 173: How do you build a heap from an existing array in O(n)?

Instead of pushing items one by one (O(n log n)), start from the last parent and "sift down" each node, moving toward the root. Most nodes are near the bottom and only move a little, so the total work is O(n).

```js
function heapify(a, compare = (x, y) => x - y) {
  for (let i = (a.length >> 1) - 1; i >= 0; i--) {
    let j = i;
    while (true) {
      const l = 2 * j + 1,
        r = l + 1;
      let m = j;
      if (l < a.length && compare(a[l], a[m]) < 0) m = l;
      if (r < a.length && compare(a[r], a[m]) < 0) m = r;
      if (m === j) break;
      [a[j], a[m]] = [a[m], a[j]];
      j = m;
    }
  }
  return a;
}
```

## 174: How do you use a heap as a priority queue for tasks?

Store objects and compare by priority.

```js
const tasks = new MinHeap((a, b) => a.priority - b.priority);
tasks.push({ name: "render", priority: 1 });
tasks.push({ name: "analytics", priority: 5 });
tasks.push({ name: "input", priority: 0 });

tasks.pop().name; // "input"
tasks.pop().name; // "render"
```

## 175: How do you implement a trie with insert, search and startsWith?

```js
class Trie {
  #root = { children: new Map(), end: false };

  insert(word) {
    let node = this.#root;
    for (const ch of word) {
      if (!node.children.has(ch)) {
        node.children.set(ch, { children: new Map(), end: false });
      }
      node = node.children.get(ch);
    }
    node.end = true;
  }

  #walk(str) {
    let node = this.#root;
    for (const ch of str) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node;
  }

  search(word) {
    return this.#walk(word)?.end === true;
  }

  startsWith(prefix) {
    return this.#walk(prefix) !== null;
  }
}
```

Every operation is O(length of the word), no matter how many words are stored.

## 176: How do you write a Graph class with an adjacency list?

A `Map` from node to a `Set` of neighbors gives O(1) add, remove and "are they connected" checks.

```js
class Graph {
  #adj = new Map();

  addNode(n) {
    if (!this.#adj.has(n)) this.#adj.set(n, new Set());
  }
  addEdge(a, b, directed = false) {
    this.addNode(a);
    this.addNode(b);
    this.#adj.get(a).add(b);
    if (!directed) this.#adj.get(b).add(a);
  }
  removeNode(n) {
    for (const neighbors of this.#adj.values()) neighbors.delete(n);
    this.#adj.delete(n);
  }
  neighbors(n) {
    return this.#adj.get(n) ?? new Set();
  }
  hasEdge(a, b) {
    return this.#adj.get(a)?.has(b) ?? false;
  }
}
```

## 177: How do you find the shortest path in an unweighted graph?

Use breadth-first search and remember where you came from, then walk back from the target.

```js
function shortestPath(graph, start, goal) {
  const prev = new Map([[start, null]]);
  let frontier = [start];
  while (frontier.length) {
    const next = [];
    for (const node of frontier) {
      if (node === goal) {
        const path = [];
        for (let n = goal; n !== null; n = prev.get(n)) path.push(n);
        return path.reverse();
      }
      for (const nb of graph.neighbors(node)) {
        if (!prev.has(nb)) {
          prev.set(nb, node);
          next.push(nb);
        }
      }
    }
    frontier = next;
  }
  return null;
}
```

BFS gives the fewest edges. For weighted edges you need Dijkstra's algorithm with a priority queue.

## 178: When would you use an adjacency matrix instead of a list?

When the graph is small and dense (lots of edges), or when you need to check "is there an edge from a to b" constantly. A matrix gives O(1) edge checks and is easy to store in a typed array, but it uses n² memory and listing a node's neighbors costs O(n). For 10,000 nodes, a matrix is 100 million cells, which is usually too much.

```js
const n = 4;
const matrix = new Uint8Array(n * n);
const addEdge = (a, b) => {
  matrix[a * n + b] = 1;
};
const hasEdge = (a, b) => matrix[a * n + b] === 1;
```

## 179: What is topological sorting and where does a front-end developer see it?

A topological sort orders the nodes of a directed graph with no cycles so that every node comes before the nodes that depend on it. Bundlers use it to decide module execution order, build tools like Nx and Turborepo use it to run tasks in the right order, and spreadsheets use it to recalculate cells.

```js
function topoSort(deps) {
  // Map<node, Set<dependency>>
  const order = [];
  const state = new Map(); // 1 = visiting, 2 = done
  const visit = (n) => {
    if (state.get(n) === 2) return;
    if (state.get(n) === 1) throw new Error(`Cycle at ${n}`);
    state.set(n, 1);
    for (const d of deps.get(n) ?? []) visit(d);
    state.set(n, 2);
    order.push(n);
  };
  for (const n of deps.keys()) visit(n);
  return order; // dependencies first
}
```

## 180: How do you implement a hash table from scratch with chaining?

```js
class HashTable {
  #buckets = Array.from({ length: 16 }, () => []);
  #count = 0;

  #hash(key) {
    let h = 0;
    for (const ch of String(key)) h = (h * 31 + ch.codePointAt(0)) | 0;
    return Math.abs(h) % this.#buckets.length;
  }

  set(key, value) {
    const bucket = this.#buckets[this.#hash(key)];
    const entry = bucket.find((e) => e[0] === key);
    if (entry) entry[1] = value;
    else {
      bucket.push([key, value]);
      if (++this.#count > this.#buckets.length * 0.75) this.#resize();
    }
  }

  get(key) {
    return this.#buckets[this.#hash(key)].find((e) => e[0] === key)?.[1];
  }

  #resize() {
    const old = this.#buckets.flat();
    this.#buckets = Array.from({ length: this.#buckets.length * 2 }, () => []);
    this.#count = 0;
    for (const [k, v] of old) this.set(k, v);
  }
}
```

In real code you'd use `Map`, but writing this shows you understand buckets, collisions and resizing.

## 181: What is open addressing in a hash table?

Instead of keeping a list per bucket, every entry lives directly in the main array. On a collision, you look at other slots in a fixed pattern until you find a free one. The simplest pattern is linear probing: try the next slot, then the next. Deleting needs care: you leave a "deleted" marker (tombstone) so later lookups don't stop too early. Open addressing is cache-friendly because there are no extra lists, but it slows down a lot when the table gets full.

## 182: What is a load factor and why do hash tables resize?

The load factor is entries divided by buckets. As it grows, more keys share buckets and lookups slow down. So when it passes a limit (often around 0.75), the table creates a bigger bucket array, usually double, and moves every entry. That move is O(n), but it happens rarely enough that inserts stay O(1) on average.

## 183: How does a simple string hash function like djb2 work?

It starts with a number and, for each character, multiplies the current hash by 33 and adds the character code. The multiplication spreads the bits around so similar strings get different hashes.

```js
function djb2(str) {
  let h = 5381;
  for (let i = 0; i < str.length; i++) {
    h = ((h << 5) + h + str.charCodeAt(i)) | 0; // h * 33 + c
  }
  return h >>> 0; // make it unsigned
}
```

This is fine for bucketing and cache keys. It's not safe for passwords or anything security-related; use the Web Crypto API for that.

## 184: How do you build an LRU cache with a Map?

A `Map` keeps insertion order, so the first key is the least recently used. On `get`, delete the key and set it again to move it to the end. On `set`, if you're over capacity, delete the first key.

```js
class LRUCache {
  #map = new Map();
  constructor(capacity) {
    this.capacity = capacity;
  }

  get(key) {
    if (!this.#map.has(key)) return undefined;
    const value = this.#map.get(key);
    this.#map.delete(key);
    this.#map.set(key, value);
    return value;
  }

  set(key, value) {
    this.#map.delete(key);
    this.#map.set(key, value);
    if (this.#map.size > this.capacity) {
      this.#map.delete(this.#map.keys().next().value);
    }
  }
}
```

## 185: How do you implement a fixed-size ring buffer?

```js
class RingBuffer {
  #data;
  #start = 0;
  #length = 0;

  constructor(capacity) {
    this.#data = new Array(capacity);
  }

  push(item) {
    const cap = this.#data.length;
    this.#data[(this.#start + this.#length) % cap] = item;
    if (this.#length < cap) this.#length++;
    else this.#start = (this.#start + 1) % cap; // overwrite oldest
  }

  toArray() {
    const cap = this.#data.length;
    return Array.from(
      { length: this.#length },
      (_, i) => this.#data[(this.#start + i) % cap],
    );
  }
}

const lastLogs = new RingBuffer(3);
[1, 2, 3, 4].forEach((n) => lastLogs.push(n));
lastLogs.toArray(); // [2, 3, 4]
```

Memory never grows, which is what you want for "keep the last N events" in logging or monitoring code.

## 186: How did people do set operations before the new Set methods?

With spread and `filter`. You'll still see this in older code or when you need to support old browsers.

```js
const union = new Set([...a, ...b]);
const intersection = new Set([...a].filter((x) => b.has(x)));
const difference = new Set([...a].filter((x) => !b.has(x)));
const isSubset = [...a].every((x) => b.has(x));
```

The built-in methods are shorter and can skip work, for example `intersection` loops over the smaller set.

## 187: Can you pass something that isn't a Set to the new Set methods?

Yes, as long as it's "set-like": it needs a numeric `size`, a `has()` method and a `keys()` method that returns an iterator. A `Map` works, since it has all three, and its keys are used. A plain array does not work, because it has no `size` or `has`; wrap it in `new Set(arr)` first.

```js
const ids = new Set([1, 2, 3]);
const byId = new Map([
  [2, "b"],
  [3, "c"],
]);
ids.intersection(byId); // Set {2, 3}
```

## 188: How do you use two values as one Map key?

`Map` compares object keys by reference, so `[a, b]` won't work as a key. Common options: join primitives into a string key, or nest maps.

```js
// String key, works if parts are primitives and can't contain the separator
const key = `${userId}|${date}`;
cache.set(key, value);

// Nested maps, works with any key types including objects
const grid = new Map();
function setCell(row, col, v) {
  if (!grid.has(row)) grid.set(row, new Map());
  grid.get(row).set(col, v);
}
```

## 189: How can a WeakMap store private data for objects?

Before private class fields existed, people kept private state in a `WeakMap` keyed by the instance. It still works well when you want to attach data to objects you don't own, like DOM nodes or objects from a library.

```js
const privateData = new WeakMap();

class Counter {
  constructor() {
    privateData.set(this, { count: 0 });
  }
  increment() {
    privateData.get(this).count++;
  }
  get value() {
    return privateData.get(this).count;
  }
}
```

When an instance is garbage collected, its private data goes with it.

## 190: How do you cache results per object without leaking memory?

Use a `WeakMap` keyed by the input object. When the object is no longer used anywhere else, its cache entry goes away too.

```js
const cache = new WeakMap();

function computeStats(data) {
  if (cache.has(data)) return cache.get(data);
  const stats = { total: data.items.reduce((s, i) => s + i.price, 0) };
  cache.set(data, stats);
  return stats;
}
```

This is how many selector libraries cache results for state objects.

## 191: What are WeakRef and FinalizationRegistry?

A `WeakRef` holds a weak reference to an object; `deref()` returns the object, or `undefined` if it has been collected. A `FinalizationRegistry` lets you register a callback that may run some time after an object is collected. Together they can build caches that drop entries under memory pressure. But GC timing is unpredictable and callbacks might never run, so don't use them for important logic.

```js
const ref = new WeakRef(bigObject);
const registry = new FinalizationRegistry((key) => cache.delete(key));
registry.register(bigObject, "report-1");

const obj = ref.deref();
if (obj) {
  // still alive
}
```

## 192: Can you use symbols as WeakMap keys?

Since ES2023, yes, but only symbols that aren't registered. `Symbol("x")` works; `Symbol.for("x")` throws, because registered symbols live forever in a global registry and could never be collected. Well-known symbols like `Symbol.iterator` can't be used either.

```js
const wm = new WeakMap();
const token = Symbol("session");
wm.set(token, { started: Date.now() });
// wm.set(Symbol.for("x"), 1); // TypeError
```

## 193: What exactly is the iterator protocol?

An iterator is an object with a `next()` method that returns `{ value, done }`. When `done` is `true`, the loop stops. An iterable is an object whose `[Symbol.iterator]()` method returns an iterator. An iterator can also have `return()`, which `for...of` calls when you `break` early, so it can clean up.

```js
const countdown = {
  [Symbol.iterator]() {
    let n = 3;
    return {
      next: () =>
        n > 0 ? { value: n--, done: false } : { value: undefined, done: true },
    };
  },
};
[...countdown]; // [3, 2, 1]
```

## 194: How do you make a custom collection class iterable?

Implement `[Symbol.iterator]`, usually as a generator. You can also add `keys()`, `values()` and `entries()` to match built-in collections.

```js
class Range {
  constructor(start, end, step = 1) {
    Object.assign(this, { start, end, step });
  }
  *[Symbol.iterator]() {
    for (let i = this.start; i < this.end; i += this.step) yield i;
  }
}

[...new Range(0, 10, 3)]; // [0, 3, 6, 9]
```

## 195: How do generators help when walking data structures?

A generator can pause after each value, so you can walk a tree or graph and hand out nodes one at a time. The caller can stop early, and you don't build a full array in memory.

```js
function* walk(node) {
  yield node;
  for (const child of node.children ?? []) yield* walk(child);
}

for (const node of walk(menuTree)) {
  if (node.id === "settings") break; // stops walking right away
}
```

Note that `yield*` with recursion still uses the call stack, so very deep trees are better handled with an explicit stack.

## 196: What are iterator helpers?

Since ES2025, iterators have methods like arrays: `map`, `filter`, `take`, `drop`, `flatMap`, `reduce`, `toArray`, `forEach`, `some`, `every` and `find`. They're lazy: nothing runs until you ask for values, and only as many items as needed are processed.

```js
function* naturals() {
  let n = 1;
  while (true) yield n++;
}

naturals()
  .filter((n) => n % 2 === 0)
  .map((n) => n * n)
  .take(3)
  .toArray(); // [4, 16, 36]
```

They work on any built-in iterator, like `map.values()` or `set.keys()`, so you don't have to turn them into arrays first.

## 197: What does Iterator.from do?

`Iterator.from` wraps an iterable or iterator-like object so you can use iterator helpers on it, even if it doesn't inherit from `Iterator.prototype`.

```js
const it = Iterator.from(new Set([1, 2, 3, 4]));
it.drop(1).take(2).toArray(); // [2, 3]
```

Built-in iterators already have the helpers, so you mostly need it for objects from libraries that implement `next()` by hand.

## 198: What is the difference between lazy and eager processing of a collection?

Eager processing, like array `map` and `filter`, does all the work right away and builds a new array at every step. Lazy processing, like iterator helpers and generators, does work only when the next value is asked for, one item at a time through the whole chain. Lazy is better for big or endless sequences and when you only need the first few results. Eager is simpler and fine for small arrays.

```js
const big = Array.from({ length: 1_000_000 }, (_, i) => i);
big
  .map((x) => x * 2)
  .filter((x) => x % 3 === 0)
  .slice(0, 5); // processes all items
big
  .values()
  .map((x) => x * 2)
  .filter((x) => x % 3 === 0)
  .take(5)
  .toArray(); // stops early
```

## 199: What are async iterables?

An async iterable has a `[Symbol.asyncIterator]` method whose `next()` returns a promise. You loop over it with `for await...of`. It's a good fit for data that arrives over time: paginated APIs, streams, WebSocket messages.

```js
async function* fetchPages(url) {
  while (url) {
    const res = await fetch(url);
    const page = await res.json();
    yield* page.items;
    url = page.next;
  }
}

for await (const item of fetchPages("/api/items")) {
  console.log(item);
}
```

## 200: What does Array.fromAsync do?

`Array.fromAsync` builds an array from an async iterable (or an iterable of promises) and returns a promise of that array. It's the async version of `Array.from`, and it works in all current major browsers and Node.js.

```js
const items = await Array.fromAsync(fetchPages("/api/items"));
const doubled = await Array.fromAsync([Promise.resolve(1), 2], (x) => x * 2); // [2, 4]
```

Unlike `Promise.all`, it waits for items one at a time, in order.

## 201: What does normalizing state mean?

It means storing each kind of entity once, in a lookup table by id, and referring to related entities by id instead of nesting copies. It's the same idea as tables in a database.

```js
// Nested (hard to update)
const posts = [
  { id: 1, author: { id: 7, name: "Ana" }, comments: [/* ... */] },
];

// Normalized
const state = {
  users: { byId: { 7: { id: 7, name: "Ana" } }, allIds: [7] },
  posts: {
    byId: { 1: { id: 1, authorId: 7, commentIds: [10, 11] } },
    allIds: [1],
  },
};
```

## 202: Why normalize data instead of keeping the nested API response?

When the same user appears in 50 posts, the nested version has 50 copies, and renaming the user means finding and updating all of them. With normalized data you update one place. Lookups by id are O(1), updates touch less of the state (so fewer components re-render), and `allIds` keeps the order separate from the data. The cost is that you have to join the data back when rendering.

## 203: What is createEntityAdapter in Redux Toolkit?

It's a helper that manages a normalized `{ ids, entities }` structure for you. It gives reducers like `addOne`, `upsertMany`, `removeOne`, `updateOne`, and selectors like `selectAll` and `selectById`, and can keep `ids` sorted with a compare function.

```js
import { createEntityAdapter, createSlice } from "@reduxjs/toolkit";

const todosAdapter = createEntityAdapter({
  sortComparer: (a, b) => a.title.localeCompare(b.title),
});

const todosSlice = createSlice({
  name: "todos",
  initialState: todosAdapter.getInitialState(),
  reducers: { todoAdded: todosAdapter.addOne },
});
```

## 204: How do you update an item in a nested array immutably?

Copy each level on the way down, and use `map` to replace only the item that changes.

```js
const board = {
  columns: [
    {
      id: "todo",
      cards: [
        { id: 1, title: "A" },
        { id: 2, title: "B" },
      ],
    },
    { id: "done", cards: [] },
  ],
};

const next = {
  ...board,
  columns: board.columns.map((col) =>
    col.id !== "todo"
      ? col
      : {
          ...col,
          cards: col.cards.map((c) => (c.id === 2 ? { ...c, title: "B2" } : c)),
        },
  ),
};
```

Unchanged columns and cards keep their old references, so memoized components for them won't re-render.

## 205: How does Immer let you write mutations but still get immutable updates?

`produce` gives your function a draft, which is a `Proxy` over the real state. When you change the draft, Immer records which parts changed and creates copies of just those objects and their parents. Everything else is shared with the old state. By default it also freezes the result, so later accidental mutations fail.

```js
import { produce } from "immer";

const next = produce(state, (draft) => {
  draft.user.address.city = "Batumi";
  draft.todos.push({ id: 3, text: "New" });
});
```

Redux Toolkit uses Immer inside `createSlice`, which is why you can write `state.value++` in reducers.

## 206: How do you deep freeze an object?

`Object.freeze` is shallow, so you need to walk the structure.

```js
function deepFreeze(obj) {
  for (const value of Object.values(obj)) {
    if (value && typeof value === "object" && !Object.isFrozen(value)) {
      deepFreeze(value);
    }
  }
  return Object.freeze(obj);
}
```

The `isFrozen` check also stops infinite loops on circular references. Note that freezing a `Map` or `Set` doesn't stop `set()` or `add()`, because their entries aren't properties.

## 207: How do you write a simple deep clone function?

```js
function deepClone(value) {
  if (value === null || typeof value !== "object") return value;
  if (Array.isArray(value)) return value.map(deepClone);
  if (value instanceof Date) return new Date(value);
  if (value instanceof Map)
    return new Map([...value].map(([k, v]) => [deepClone(k), deepClone(v)]));
  if (value instanceof Set) return new Set([...value].map(deepClone));
  return Object.fromEntries(
    Object.entries(value).map(([k, v]) => [k, deepClone(v)]),
  );
}
```

This doesn't handle circular references or class prototypes. In real code, use `structuredClone`; write your own only when you need special rules (see question 394 for cycles).

## 208: What can't structuredClone copy?

Functions, DOM nodes, getters and setters (they get turned into plain values), symbol keys, and property descriptors like non-writable. Class instances lose their prototype and come back as plain objects, so their methods are gone. Functions and DOM nodes make it throw a `DataCloneError`.

```js
class Point {
  constructor(x) {
    this.x = x;
  }
  len() {
    return this.x;
  }
}
const copy = structuredClone(new Point(3));
copy instanceof Point; // false
copy.len; // undefined
```

## 209: How do you write a deep equality check?

```js
function deepEqual(a, b) {
  if (Object.is(a, b)) return true;
  if (typeof a !== "object" || typeof b !== "object" || !a || !b) return false;
  if (Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;
  if (a instanceof Date) return a.getTime() === b.getTime();

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every((k) => Object.hasOwn(b, k) && deepEqual(a[k], b[k]));
}
```

For a full version that handles `Map`, `Set` and cycles, see question 393. Libraries like Lodash's `isEqual` or `dequal` cover these cases already.

## 210: What is the difference between ===, Object.is and SameValueZero?

- `===`: `NaN !== NaN`, and `+0 === -0`.
- `Object.is`: `Object.is(NaN, NaN)` is `true`, and `Object.is(0, -0)` is `false`.
- SameValueZero: like `Object.is`, except `+0` and `-0` are equal. `Map`, `Set` and `includes` use it.

React uses `Object.is` to compare state and hook dependencies.

## 211: What happens to a Map's order when you set an existing key again?

Nothing. Setting an existing key updates the value but keeps its original position. To move a key to the end (like in an LRU cache), you have to `delete` it first and then `set` it.

```js
const m = new Map([
  ["a", 1],
  ["b", 2],
]);
m.set("a", 9);
[...m.keys()]; // ["a", "b"]
m.delete("a");
m.set("a", 9);
[...m.keys()]; // ["b", "a"]
```

## 212: Why would you use a Map instead of an object for data keyed by numeric ids?

Objects put integer-like keys first and sort them by number, so the order you added them in is lost. Also, keys turn into strings, so you get `"42"` back, not `42`. A `Map` keeps the keys as numbers and keeps insertion order. That matters when, for example, you want messages in the order they arrived but keyed by numeric id.

```js
const o = {};
o[30] = "c";
o[10] = "a";
o[20] = "b";
Object.keys(o); // ["10", "20", "30"]

const m = new Map([
  [30, "c"],
  [10, "a"],
  [20, "b"],
]);
[...m.keys()]; // [30, 10, 20]
```

## 213: How can several typed arrays share one ArrayBuffer?

Each typed array is just a view. You can create several views over the same buffer, even of different types, and they all read and write the same bytes.

```js
const buf = new ArrayBuffer(4);
const bytes = new Uint8Array(buf);
const int = new Uint32Array(buf);

int[0] = 0x01020304;
console.log(bytes); // [4, 3, 2, 1] on little-endian machines (almost all of them)
```

`subarray()` also creates a view over the same memory, while `slice()` copies.

## 214: What is a DataView and when do you need it?

A `DataView` reads and writes numbers of different types at any byte offset in a buffer, and lets you choose the byte order (endianness). Typed arrays always use the machine's byte order and need aligned offsets. Use `DataView` to parse binary formats and network protocols where fields have mixed sizes and a fixed byte order.

```js
const view = new DataView(buffer);
const version = view.getUint8(0);
const length = view.getUint32(1, false); // big-endian
const scale = view.getFloat32(5, true); // little-endian
```

## 215: What is Uint8ClampedArray and where is it used?

It's a typed array of bytes that clamps values to the range 0 to 255 instead of wrapping. Setting 300 gives 255 and setting -5 gives 0, and decimals are rounded. Canvas `ImageData.data` uses it, because pixel color channels must stay in that range.

```js
const ctx = canvas.getContext("2d");
const img = ctx.getImageData(0, 0, canvas.width, canvas.height);
const px = img.data; // Uint8ClampedArray, RGBA RGBA ...
for (let i = 0; i < px.length; i += 4) px[i] = px[i] * 1.5; // brighter red, clamped
ctx.putImageData(img, 0, 0);
```

## 216: How do you convert between strings and bytes?

Use `TextEncoder` and `TextDecoder`. They work with UTF-8 by default.

```js
const bytes = new TextEncoder().encode("héllo"); // Uint8Array
const text = new TextDecoder().decode(bytes); // "héllo"
```

Don't use `charCodeAt` to build bytes yourself; it gives UTF-16 code units, not UTF-8 bytes.

## 217: How do Blob and File relate to ArrayBuffer?

A `Blob` is an immutable chunk of binary data with a MIME type, and a `File` is a `Blob` with a name and last-modified date. They don't give direct access to bytes; you read them with `await blob.arrayBuffer()`, `await blob.text()` or `blob.stream()`. You can also build a Blob from strings, typed arrays and buffers, and pass it to `fetch`, `URL.createObjectURL` or a download link.

```js
const blob = new Blob([JSON.stringify(data)], { type: "application/json" });
const buf = await blob.arrayBuffer();
```

## 218: How do you store a 2D grid in a flat array?

Use one array of size `rows * cols` and compute the index as `row * cols + col`. It uses less memory than an array of arrays, keeps data together, and works with typed arrays.

```js
const cols = 100,
  rows = 50;
const grid = new Uint8Array(rows * cols);
const idx = (r, c) => r * cols + c;

grid[idx(3, 7)] = 1;
const row = Math.floor(i / cols),
  col = i % cols; // index back to coordinates
```

Game boards, pixel buffers and heatmaps often use this layout.

## 219: How do you store a sparse matrix efficiently?

If most cells are empty, store only the filled ones in a `Map` keyed by position.

```js
const cells = new Map();
const key = (r, c) => `${r},${c}`;

cells.set(key(1000, 2000), "=SUM(A1:A3)");
cells.get(key(1000, 2000));
cells.get(key(0, 0)) ?? ""; // empty cell
```

A spreadsheet with a million possible cells but only a few hundred filled stays tiny this way. For numeric keys, `r * maxCols + c` avoids building strings.

## 220: How do you use a number as a set of boolean flags?

Give each flag one bit and use bitwise operators. It's compact and fast to combine and check.

```js
const READ = 1 << 0; // 1
const WRITE = 1 << 1; // 2
const DELETE = 1 << 2; // 4

let perms = READ | WRITE;
const canWrite = (perms & WRITE) !== 0; // true
perms &= ~WRITE; // remove WRITE
perms ^= DELETE; // toggle DELETE
```

JavaScript bitwise operators work on 32-bit integers, so one number holds up to 32 flags. React uses this idea for its internal fiber flags and lanes.

## 221: How do you build a bitset for many flags?

Use a `Uint32Array` where each item holds 32 bits.

```js
class BitSet {
  constructor(size) {
    this.words = new Uint32Array(Math.ceil(size / 32));
  }
  set(i) {
    this.words[i >>> 5] |= 1 << (i & 31);
  }
  clear(i) {
    this.words[i >>> 5] &= ~(1 << (i & 31));
  }
  has(i) {
    return (this.words[i >>> 5] & (1 << (i & 31))) !== 0;
  }
}

const seen = new BitSet(1_000_000); // about 125 KB
seen.set(123456);
seen.has(123456); // true
```

A `Set` of a million numbers takes many megabytes; this takes about 125 KB.

## 222: What is a disjoint set (union-find)?

It's a structure that tracks which items belong to the same group. It has two operations: `find(x)` returns the group leader for `x`, and `union(a, b)` joins two groups. It answers "are these two connected?" almost in constant time. It's used for connected components, detecting cycles in undirected graphs, Kruskal's algorithm and grouping things like merged accounts.

## 223: How do you implement union-find with path compression?

Each item points to a parent. `find` follows parents to the root and, on the way back, points every node directly at the root (path compression). Union by size attaches the smaller tree to the bigger one.

```js
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.size = new Array(n).fill(1);
  }
  find(x) {
    while (this.parent[x] !== x) {
      this.parent[x] = this.parent[this.parent[x]]; // path halving
      x = this.parent[x];
    }
    return x;
  }
  union(a, b) {
    let ra = this.find(a),
      rb = this.find(b);
    if (ra === rb) return false;
    if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    this.size[ra] += this.size[rb];
    return true;
  }
}
```

## 224: What is a monotonic stack?

A monotonic stack is a stack whose items always stay in increasing (or decreasing) order. Before pushing, you pop everything that would break the order. It solves "next greater element" style problems in O(n), because each item is pushed and popped at most once.

```js
function nextGreater(nums) {
  const result = new Array(nums.length).fill(-1);
  const stack = []; // indexes, values decreasing
  nums.forEach((n, i) => {
    while (stack.length && nums[stack.at(-1)] < n) {
      result[stack.pop()] = n;
    }
    stack.push(i);
  });
  return result;
}
nextGreater([2, 1, 3]); // [3, 3, -1]
```

## 225: How do you build a stack that returns its minimum in O(1)?

Keep a second stack of minimums. Each time you push, also push the smaller of the new value and the current minimum.

```js
class MinStack {
  #items = [];
  #mins = [];

  push(x) {
    this.#items.push(x);
    this.#mins.push(this.#mins.length ? Math.min(x, this.#mins.at(-1)) : x);
  }
  pop() {
    this.#mins.pop();
    return this.#items.pop();
  }
  min() {
    return this.#mins.at(-1);
  }
}
```

## 226: How do you build undo and redo with stacks?

Keep two stacks. Every new change pushes the previous state onto `undo` and clears `redo`. Undo moves the current state to `redo` and pops from `undo`; redo does the opposite.

```js
class History {
  #undo = [];
  #redo = [];
  constructor(initial) {
    this.current = initial;
  }

  push(state) {
    this.#undo.push(this.current);
    this.current = state;
    this.#redo.length = 0;
  }
  undo() {
    if (!this.#undo.length) return this.current;
    this.#redo.push(this.current);
    return (this.current = this.#undo.pop());
  }
  redo() {
    if (!this.#redo.length) return this.current;
    this.#undo.push(this.current);
    return (this.current = this.#redo.pop());
  }
}
```

With immutable state, each saved snapshot shares unchanged parts with the others, so this uses less memory than it looks.

## 227: How would you model browser back and forward navigation?

Two stacks again: `back` and `forward`. Visiting a new page pushes the current one onto `back` and clears `forward`. Back pops from `back` and pushes the current page onto `forward`. Another option is one array plus a current index, which is how the real `history` API looks: `history.length` and moving with `history.go(n)`.

## 228: How do you find all elements at a certain depth in the DOM?

Walk the DOM breadth-first with a queue and track the level.

```js
function elementsAtDepth(root, depth) {
  let level = [root];
  for (let d = 0; d < depth; d++) {
    level = level.flatMap((el) => [...el.children]);
  }
  return level;
}
elementsAtDepth(document.body, 2);
```

For big DOM walks, `document.createTreeWalker` is a built-in iterator that's fast and lets you filter node types.

## 229: How do you build an event emitter with Map and Set?

A `Map` from event name to a `Set` of listeners. The `Set` stops the same function from being added twice and makes removing O(1).

```js
class Emitter {
  #listeners = new Map();

  on(event, fn) {
    if (!this.#listeners.has(event)) this.#listeners.set(event, new Set());
    this.#listeners.get(event).add(fn);
    return () => this.off(event, fn);
  }
  off(event, fn) {
    this.#listeners.get(event)?.delete(fn);
  }
  emit(event, ...args) {
    for (const fn of [...(this.#listeners.get(event) ?? [])]) fn(...args);
  }
}
```

Copying the set before looping means a listener that unsubscribes itself during `emit` doesn't change the loop.

## 230: How do you keep a list of subscribers in a store?

Most small stores (Zustand, Redux, `useSyncExternalStore` based stores) use a `Set` of callbacks. `subscribe` adds a function and returns a function that removes it.

```js
function createStore(initial) {
  let state = initial;
  const listeners = new Set();
  return {
    getState: () => state,
    setState(update) {
      state = { ...state, ...update };
      listeners.forEach((l) => l(state));
    },
    subscribe(l) {
      listeners.add(l);
      return () => listeners.delete(l);
    },
  };
}
```

## 231: How do you detect circular imports in a dependency graph?

Do a depth-first search and keep a set of nodes on the current path. If you reach a node that's already on the path, you've found a cycle. The path itself tells you the cycle.

```js
function findCycle(graph) {
  // Map<string, string[]>
  const done = new Set();
  const path = [];
  const onPath = new Set();

  function dfs(n) {
    if (onPath.has(n)) return [...path.slice(path.indexOf(n)), n];
    if (done.has(n)) return null;
    onPath.add(n);
    path.push(n);
    for (const dep of graph.get(n) ?? []) {
      const cycle = dfs(dep);
      if (cycle) return cycle;
    }
    onPath.delete(n);
    path.pop();
    done.add(n);
    return null;
  }
  for (const n of graph.keys()) {
    const c = dfs(n);
    if (c) return c; // e.g. ["a.js", "b.js", "a.js"]
  }
  return null;
}
```

## 232: How do you memoize a function with several arguments?

A simple way is a string key from the arguments. For object arguments, a tree of maps (one level per argument) compares by reference and avoids serializing.

```js
function memoize(fn) {
  const root = new Map();
  const RESULT = Symbol("result");
  return (...args) => {
    let node = root;
    for (const arg of args) {
      if (!node.has(arg)) node.set(arg, new Map());
      node = node.get(arg);
    }
    if (!node.has(RESULT)) node.set(RESULT, fn(...args));
    return node.get(RESULT);
  };
}
```

Use `WeakMap` levels instead of `Map` when the arguments are objects that should be garbage collected.

## 233: When does it pay off to turn an array into a Set for lookups?

Building a `Set` costs O(n). If you check membership once, `includes` is fine. If you check many times, like filtering one list against another, the `Set` wins: O(n + m) instead of O(n × m).

```js
const blocked = new Set(blockedIds); // once
const visible = posts.filter((p) => !blocked.has(p.authorId));
```

For very small arrays (a handful of items), `includes` can be just as fast, so don't bother.

## 234: When is a plain object better than a Map?

When the data has a known, fixed set of string keys (a record), when it goes to or comes from JSON, when you want destructuring and spread, and when TypeScript should check each property. Engines are also very fast at objects with a stable shape. A `Map` is better as a dictionary with changing keys; an object is better as a record.

## 235: How do you count frequencies and get the top items?

Count with a `Map`, then sort its entries.

```js
const counts = new Map();
for (const tag of tags) counts.set(tag, (counts.get(tag) ?? 0) + 1);

const top3 = [...counts]
  .toSorted((a, b) => b[1] - a[1])
  .slice(0, 3)
  .map(([tag]) => tag);
```

For a huge number of distinct items where you only need the top few, a small heap of size k is faster than sorting everything.

## 236: Should you use Object.groupBy, Map.groupBy or reduce for grouping?

Use `Object.groupBy` when keys are strings and you want a plain object, and `Map.groupBy` when keys are non-strings or you need `Map` features. Use `reduce` (or a loop) when you need something the built-ins don't do, like counting instead of collecting, or putting one item in several groups.

```js
const byStatus = Object.groupBy(orders, (o) => o.status);
const byCustomer = Map.groupBy(orders, (o) => o.customer); // object keys
const totals = orders.reduce((acc, o) => {
  acc[o.status] = (acc[o.status] ?? 0) + o.total;
  return acc;
}, {});
```

## 237: Is a linked list faster than an array in JavaScript for inserts?

On paper, inserting in the middle of a linked list is O(1) and in an array it's O(n). In practice, arrays are often faster for small and medium sizes. Array items sit next to each other in memory, which the CPU cache loves, and moving items is a fast memory copy. Linked list nodes are scattered objects, and you still need O(n) to walk to the right spot. Linked lists win when you already hold a reference to the node and the list is large.

## 238: What are packed and holey arrays?

V8 tracks whether an array has holes. A packed array has no holes, so the engine can skip checks when reading. Once an array gets a hole, for example `new Array(5)` or `arr[100] = x` on a short array, it becomes holey and stays holey even if you fill the holes later. Holey arrays need extra checks on reads, so they're a bit slower.

```js
const packed = [1, 2, 3];
const holey = new Array(3); // holey from the start
const better = Array.from({ length: 3 }, () => 0); // packed
```

## 239: Why does mixing types in an array affect performance?

V8 picks the most specific storage it can: small integers only (SMI), then doubles, then generic elements. Adding a decimal to an integer array switches it to doubles; adding a string or object switches it to generic. These changes only go one way. Arrays of one numeric type are faster to loop over and use less memory. For big numeric data, a typed array guarantees it.

## 240: Why shouldn't you use delete on array items?

`delete arr[i]` removes the item but doesn't shift the rest or change `length`. You get a hole, which methods treat inconsistently, and the array becomes holey and slower.

```js
const a = [1, 2, 3];
delete a[1];
console.log(a, a.length); // [1, <empty>, 3] 3

a.splice(1, 1); // the right way, or a.filter(...) / a.toSpliced(...)
```

## 241: What is the maximum length of an array?

2³² − 1 (about 4.29 billion), because array indexes are 32-bit unsigned integers. A property like `arr[4294967295]` is just a normal property and doesn't change `length`. In practice you'll run out of memory far before that. Typed arrays have different limits that depend on the engine and available memory.

## 242: How do you sort a Map by its values?

A `Map` keeps insertion order, so you sort its entries and build a new `Map`.

```js
const scores = new Map([
  ["ana", 7],
  ["ben", 10],
  ["cy", 3],
]);
const sorted = new Map([...scores].toSorted((a, b) => b[1] - a[1]));
[...sorted.keys()]; // ["ben", "ana", "cy"]
```

## 243: How do you sort an object by its keys?

Get the entries, sort them, and rebuild. Keep in mind that integer-like keys always come first in ascending order no matter what you do, so this only works for non-numeric keys.

```js
const obj = { banana: 2, apple: 1, cherry: 3 };
const sorted = Object.fromEntries(
  Object.entries(obj).toSorted(([a], [b]) => a.localeCompare(b)),
);
```

If you need a specific order with numeric keys, use an array of entries or a `Map`.

## 244: What is Object.create(null) and when do you use it?

It creates an object with no prototype, so it has no inherited keys like `toString`, `constructor` or `__proto__`. That makes it a safer dictionary for keys that come from users or outside data. `Object.groupBy` returns this kind of object.

```js
const dict = Object.create(null);
dict["__proto__"] = "safe"; // just a normal key here
"toString" in dict; // false
```

These objects don't have `hasOwnProperty`, so check keys with `Object.hasOwn` or `in`. A `Map` is often the better choice anyway.

## 245: What is prototype pollution?

It happens when code copies user-controlled keys into an object and a key like `__proto__` or `constructor.prototype` ends up changing `Object.prototype`. After that, every object in the app has the injected property, which can break logic or open security holes.

```js
const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
function merge(target, src) {
  for (const k in src) {
    if (typeof src[k] === "object") merge((target[k] ??= {}), src[k]);
    else target[k] = src[k];
  }
}
merge({}, payload);
({}).isAdmin; // true, every object is affected
```

Fixes: skip `__proto__`, `constructor` and `prototype` keys, use `Object.create(null)` or `Map` for dictionaries, and validate input.

## 246: How can a Proxy make an observable data structure?

A `Proxy` can intercept reads and writes. On write, you notify listeners. This is the basic idea behind Vue's reactivity and MobX.

```js
function observable(target, onChange) {
  return new Proxy(target, {
    set(obj, key, value, receiver) {
      const old = obj[key];
      const ok = Reflect.set(obj, key, value, receiver);
      if (old !== value) onChange(key, value, old);
      return ok;
    },
  });
}

const state = observable({ count: 0 }, (k, v) => console.log(k, v));
state.count++; // logs: count 1
```

Nested objects need their own proxies, which real libraries create lazily on read.

## 247: Why use Reflect inside Proxy traps?

`Reflect` methods do the default behavior for each trap and take the same arguments. Using `Reflect.get(target, key, receiver)` instead of `target[key]` makes getters and inheritance work right, because `this` points to the proxy. They also return booleans for success instead of throwing, which matches what traps should return.

## 248: How do you add parent links to a tree, and why?

Parent links let you walk up from any node, which you need for breadcrumbs, "expand all ancestors" in a tree view, or bubbling events in your own component tree.

```js
function addParents(node, parent = null) {
  node.parent = parent;
  for (const child of node.children ?? []) addParents(child, node);
  return node;
}

function pathTo(node) {
  const path = [];
  for (let n = node; n; n = n.parent) path.unshift(n.name);
  return path;
}
```

The downside: the tree now has cycles, so `JSON.stringify` throws. A separate `Map` from node id to parent id avoids that.

## 249: How do you serialize and rebuild a binary tree?

Write the nodes in pre-order, with `null` for missing children. Reading it back in the same order rebuilds the exact shape.

```js
function serialize(root) {
  const out = [];
  (function walk(n) {
    if (!n) {
      out.push(null);
      return;
    }
    out.push(n.value);
    walk(n.left);
    walk(n.right);
  })(root);
  return JSON.stringify(out);
}

function deserialize(json) {
  const vals = JSON.parse(json);
  let i = 0;
  return (function build() {
    const v = vals[i++];
    if (v === null) return null;
    return { value: v, left: build(), right: build() };
  })();
}
```

## 250: How do you get the path from the root to a node, like breadcrumbs?

Search depth-first and keep the current path. When you find the node, return a copy of it.

```js
function findPath(nodes, id, path = []) {
  for (const node of nodes) {
    path.push(node);
    if (node.id === id) return [...path];
    const found = findPath(node.children ?? [], id, path);
    if (found) return found;
    path.pop();
  }
  return null;
}
findPath(menu, "billing")?.map((n) => n.label); // ["Settings", "Account", "Billing"]
```

## 251: How do you filter a tree but keep the parents of matching nodes?

This is what a tree view search does: show matching nodes plus the path to them. Rebuild the tree, keeping a node if it matches or if any child survives.

```js
function filterTree(nodes, match) {
  return nodes.flatMap((node) => {
    const children = filterTree(node.children ?? [], match);
    if (match(node) || children.length) return [{ ...node, children }];
    return [];
  });
}

filterTree(files, (n) => n.name.includes("test"));
```

The original tree isn't changed, so clearing the search just shows the original again.

## 252: How would you model a file system in JavaScript?

A tree where folders have a `children` map and files have content or size. A `Map` keyed by name gives fast lookup by path segment.

```js
const root = { type: "dir", name: "/", children: new Map() };

function mkdirp(path) {
  let node = root;
  for (const part of path.split("/").filter(Boolean)) {
    if (!node.children.has(part)) {
      node.children.set(part, { type: "dir", name: part, children: new Map() });
    }
    node = node.children.get(part);
  }
  return node;
}
mkdirp("/src/components/ui");
```

## 253: How should you store nested comments?

APIs often return a flat list with `parentId`, which is easy to store and paginate. For rendering, build a tree once, or keep a `Map` from `parentId` to child ids and render recursively from that.

```jsx
const childrenOf = Map.groupBy(comments, (c) => c.parentId ?? "root");
function Thread({ parentId = "root" }) {
  return (childrenOf.get(parentId) ?? []).map((c) => (
    <Comment key={c.id} comment={c}>
      <Thread parentId={c.id} />
    </Comment>
  ));
}
```

Storing the full nested tree in state makes updates deep and painful; the flat form keeps them simple.

## 254: How do you count how many words start with a prefix using a trie?

Store a counter on each node that you increase every time a word passes through it. Then the prefix's node holds the answer right away.

```js
class PrefixCounter {
  #root = { next: new Map(), count: 0 };

  add(word) {
    let node = this.#root;
    for (const ch of word) {
      if (!node.next.has(ch)) node.next.set(ch, { next: new Map(), count: 0 });
      node = node.next.get(ch);
      node.count++;
    }
  }
  countPrefix(prefix) {
    let node = this.#root;
    for (const ch of prefix) {
      node = node.next.get(ch);
      if (!node) return 0;
    }
    return node.count;
  }
}
```

## 255: Heap or sorted array for a priority queue?

A sorted array gives O(1) access to the top but O(n) inserts, since items have to shift. A heap gives O(log n) for both inserts and removals. If you insert rarely and read the whole sorted order often, a sorted array is fine. If you insert and remove often, like a scheduler or Dijkstra, a heap is the right choice.

## 256: What are the time complexities of a binary heap?

- `peek`: O(1)
- `push`: O(log n)
- `pop`: O(log n)
- build from an array (heapify): O(n)
- search for any value: O(n), because a heap is only partly ordered
- remove a random item: O(n) to find it, unless you keep a position map (see question 379)

## 257: What is the difference between a balanced and an unbalanced BST?

In a balanced BST, the left and right subtrees of every node have about the same height, so the height is about log₂(n) and operations are O(log n). In an unbalanced tree, one side can be much deeper, and in the worst case it becomes a linked list with height n. Self-balancing trees like AVL and red-black trees rotate nodes after inserts and deletes to stay balanced.

## 258: What happens if you insert sorted data into a plain BST?

Each new value is bigger than everything before, so it always goes to the right. The tree becomes a long chain going right, every operation turns into O(n), and recursive code can hit the stack limit. Fixes: use a self-balancing tree, shuffle the input first, or build a balanced tree from the sorted array by always picking the middle element as the root.

```js
function fromSorted(arr, lo = 0, hi = arr.length - 1) {
  if (lo > hi) return null;
  const mid = (lo + hi) >> 1;
  return {
    value: arr[mid],
    left: fromSorted(arr, lo, mid - 1),
    right: fromSorted(arr, mid + 1, hi),
  };
}
```

## 259: How do you represent a weighted graph in JavaScript?

Store the weight with each neighbor, for example as a `Map` of neighbor to weight.

```js
const roads = new Map([
  [
    "A",
    new Map([
      ["B", 5],
      ["C", 2],
    ]),
  ],
  ["B", new Map([["D", 1]])],
  [
    "C",
    new Map([
      ["B", 1],
      ["D", 7],
    ]),
  ],
  ["D", new Map()],
]);

roads.get("A").get("C"); // 2
for (const [next, cost] of roads.get("C")) console.log(next, cost);
```

## 260: What is an edge list and when is it useful?

An edge list is just an array of edges, like `[from, to, weight]`. It's the simplest format and is common in API responses and files. It's good for algorithms that look at all edges, like Kruskal's (sort the edges by weight) or Bellman-Ford. It's bad for "give me the neighbors of X", which takes O(E), so you usually convert it to an adjacency list.

```js
const edges = [
  ["A", "B", 5],
  ["A", "C", 2],
];
const adj = Map.groupBy(edges, ([from]) => from);
```

## 261: What is an implicit graph?

A graph you never store as nodes and edges; you compute neighbors when you need them. A grid is the classic example: each cell's neighbors are the cells up, down, left and right. Puzzle states are another: neighbors are the states one move away. This saves memory, especially when the graph is huge or infinite.

```js
const dirs = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];
function* neighbors(grid, r, c) {
  for (const [dr, dc] of dirs) {
    const nr = r + dr,
      nc = c + dc;
    if (grid[nr]?.[nc] === 0) yield [nr, nc]; // 0 = open cell
  }
}
```

## 262: Is Map lookup always O(1)?

It's O(1) on average. The spec only requires it to be "sublinear", but engines use hash tables, so in practice it's constant time. Single operations can be slower when the table grows and rehashes, and in theory many keys landing in the same bucket would slow lookups down. For normal app code, treat `get`, `set`, `has` and `delete` as O(1).

## 263: Why doesn't new Set([[1, 2], [1, 2]]) remove the duplicate pair?

Each `[1, 2]` is a separate array object, and `Set` compares objects by reference. To get unique pairs, store a string key instead, or keep a `Map` from the key to the original pair.

```js
const pairs = [
  [1, 2],
  [1, 2],
  [2, 1],
];
const unique = [...new Map(pairs.map((p) => [p.join(","), p])).values()];
// [[1, 2], [2, 1]]
```

## 264: How do you use coordinates like [x, y] as a key?

Turn them into a primitive: a string like `"3,4"`, or a single number like `y * width + x` if you know the width. Numbers are faster than strings and use less memory.

```js
const visited = new Set();
const key = (x, y) => y * 10_000 + x;

visited.add(key(3, 4));
visited.has(key(3, 4)); // true
```

For negative or unbounded coordinates, a string key is the safe choice.

## 265: How do you implement a queue with a linked list?

Keep `head` for dequeue and `tail` for enqueue. Both are O(1), with no index bookkeeping and no memory left behind by removed items.

```js
class LinkedQueue {
  #head = null;
  #tail = null;
  size = 0;

  enqueue(value) {
    const node = { value, next: null };
    if (this.#tail) this.#tail.next = node;
    else this.#head = node;
    this.#tail = node;
    this.size++;
  }
  dequeue() {
    if (!this.#head) return undefined;
    const { value } = this.#head;
    this.#head = this.#head.next;
    if (!this.#head) this.#tail = null;
    this.size--;
    return value;
  }
}
```

## 266: How do you keep equal-priority items in insertion order in a heap?

A heap isn't stable: items with the same priority can come out in any order. Add an increasing counter to each item and use it to break ties.

```js
let seq = 0;
const pq = new MinHeap((a, b) => a.priority - b.priority || a.seq - b.seq);
pq.push({ priority: 1, seq: seq++, task: "first" });
pq.push({ priority: 1, seq: seq++, task: "second" });
pq.pop().task; // "first"
```

## 267: How would you schedule UI work by priority?

Put tasks in a priority queue and run them in small chunks, checking the time so you give the main thread back to the browser often. User input gets high priority, background work like analytics or prefetching gets low priority. The browser's `scheduler.postTask` (where supported) gives you priorities like `"user-blocking"`, `"user-visible"` and `"background"`, so you don't always have to build the queue yourself.

```js
await scheduler.postTask(() => renderResults(), { priority: "user-visible" });
await scheduler.postTask(() => sendAnalytics(), { priority: "background" });
```

## 268: How do you build a cache where entries expire after some time?

Store the expiry time with each value and check it on read.

```js
class TTLCache {
  #map = new Map();
  constructor(ttlMs) {
    this.ttl = ttlMs;
  }

  set(key, value) {
    this.#map.set(key, { value, expires: Date.now() + this.ttl });
  }
  get(key) {
    const entry = this.#map.get(key);
    if (!entry) return undefined;
    if (Date.now() > entry.expires) {
      this.#map.delete(key);
      return undefined;
    }
    return entry.value;
  }
}
```

Expired entries that are never read stay in memory, so add a size limit or clean up from time to time.

## 269: What is an LFU cache?

LFU means Least Frequently Used. When the cache is full, it removes the item that was used the fewest times, not the one used longest ago. It's good when some items stay popular for a long time. The trouble is that an item used a lot in the past can stay forever even if nobody needs it now, so real LFU caches often reduce counts over time. A full O(1) design is in question 440.

## 270: How do you remove the nth node from the end of a linked list?

Move one pointer n steps ahead, then move both until the first reaches the end. The second pointer is now just before the node to remove. A dummy node in front makes removing the head work the same way.

```js
function removeNthFromEnd(head, n) {
  const dummy = { next: head };
  let fast = dummy,
    slow = dummy;
  for (let i = 0; i < n; i++) fast = fast.next;
  while (fast.next) {
    fast = fast.next;
    slow = slow.next;
  }
  slow.next = slow.next.next;
  return dummy.next;
}
```

## 271: How do you find where two linked lists join?

Walk both lists with two pointers. When one reaches the end, move it to the start of the other list. Both pointers travel the same total distance, so they meet at the shared node, or both become `null` if there isn't one.

```js
function intersection(a, b) {
  let p = a,
    q = b;
  while (p !== q) {
    p = p ? p.next : b;
    q = q ? q.next : a;
  }
  return p;
}
```

## 272: How do you check if a linked list is a palindrome with O(1) extra memory?

Find the middle, reverse the second half, and compare it with the first half. If callers need the list unchanged, reverse the second half back afterward.

```js
function isPalindrome(head) {
  let slow = head,
    fast = head;
  while (fast?.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let prev = null;
  while (slow) {
    [slow.next, prev, slow] = [prev, slow, slow.next];
  }

  for (let l = head, r = prev; r; l = l.next, r = r.next) {
    if (l.value !== r.value) return false;
  }
  return true;
}
```

The easy version just copies values into an array and compares from both ends, which uses O(n) memory.

## 273: Why is an LRU cache often built with a doubly linked list plus a hash map?

The map gives O(1) lookup from key to node. The doubly linked list keeps usage order: move a node to the front on every access, and remove from the back when the cache is full. Because the list is doubly linked, removing a node from the middle is O(1). In JavaScript, a `Map` alone gives the same result thanks to insertion order, but the list version is what interviewers expect in other languages and in "don't use Map order" follow-ups.

## 274: Why are push and pop on an array O(1) even though arrays sometimes resize?

When the backing storage is full, the engine allocates a bigger block (growing by a factor, not by one slot) and copies the items. That copy is O(n), but it happens so rarely that the average cost per `push` stays constant. This is called amortized O(1). `pop` never needs to grow the storage.

## 275: Should you store extra data on DOM elements with dataset or with a WeakMap?

`dataset` (`data-*` attributes) only stores strings, shows up in the HTML, and is good for small config that CSS or other scripts also read. A `WeakMap` keyed by the element can hold any value (objects, functions, component instances), stays invisible in the DOM, and lets the data be garbage collected with the element. Adding custom properties directly to element objects works but can clash with future DOM properties.

## 276: How do you track visited nodes when walking a graph?

Use a `Set` of node ids (or the node objects). Check before you visit, and add right when you put a node in the queue or stack, not when you take it out, so it isn't queued twice.

```js
function bfs(start, getNeighbors) {
  const visited = new Set([start]);
  const queue = [start];
  for (let i = 0; i < queue.length; i++) {
    for (const nb of getNeighbors(queue[i])) {
      if (!visited.has(nb)) {
        visited.add(nb);
        queue.push(nb);
      }
    }
  }
  return visited;
}
```

Reading `queue[i]` with an index instead of `shift()` keeps this O(V + E).

## 277: How do you avoid infinite loops when walking objects that may have cycles?

Keep a `WeakSet` of objects you've already seen and skip them.

```js
function countObjects(root) {
  const seen = new WeakSet();
  let count = 0;
  (function walk(v) {
    if (!v || typeof v !== "object" || seen.has(v)) return;
    seen.add(v);
    count++;
    for (const child of Object.values(v)) walk(child);
  })(root);
  return count;
}

const a = { name: "a" };
a.self = a;
countObjects(a); // 1, no infinite loop
```

A `WeakSet` is a good choice here because it doesn't keep the objects alive after you're done.

## 278: How do you JSON.stringify an object with circular references?

`JSON.stringify` throws on cycles. Use a replacer that tracks objects on the current path and swaps repeats for a marker.

```js
function safeStringify(value) {
  const stack = [];
  return JSON.stringify(value, function (key, val) {
    if (typeof val !== "object" || val === null) return val;
    while (stack.length && stack.at(-1) !== this) stack.pop();
    if (stack.includes(val)) return "[Circular]";
    stack.push(val);
    return val;
  });
}
```

Inside a replacer, `this` is the object that holds the current key, which lets you track the path. If you need to rebuild the cycles later, use a library like `flatted` or `structuredClone` (for in-memory copies).

## 279: How do you use a replacer and reviver to store Map, Set and Date in JSON?

Tag special types in the replacer and turn them back in the reviver.

```js
const replacer = (key, value) => {
  if (value instanceof Map) return { $type: "Map", value: [...value] };
  if (value instanceof Set) return { $type: "Set", value: [...value] };
  return value;
};
const reviver = (key, value) => {
  if (value?.$type === "Map") return new Map(value.value);
  if (value?.$type === "Set") return new Set(value.value);
  return value;
};

const json = JSON.stringify({ tags: new Set(["a"]) }, replacer);
JSON.parse(json, reviver).tags.has("a"); // true
```

## 280: Why do Dates come back as strings after JSON.parse, and how do you fix it?

`JSON.stringify` calls `Date.prototype.toJSON`, which gives an ISO string. JSON has no date type, so `JSON.parse` leaves it as a string. You can convert known fields after parsing, or use a reviver.

```js
const iso = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$/;
const data = JSON.parse(text, (k, v) =>
  typeof v === "string" && iso.test(v) ? new Date(v) : v,
);
```

Converting known fields by name is safer than a regex, because a user might type a string that looks like a date. Schema libraries like Zod can do it with `z.coerce.date()`.

## 281: How do you put a BigInt in JSON?

`JSON.stringify` throws on `BigInt`. Convert it to a string in a replacer and back in a reviver, or send large ids as strings from the API in the first place.

```js
const json = JSON.stringify({ id: 12345678901234567890n }, (k, v) =>
  typeof v === "bigint" ? v.toString() : v,
); // '{"id":"12345678901234567890"}'

const id = BigInt(JSON.parse(json).id);
```

This also matters for big numeric ids from APIs: a `number` loses precision past `Number.MAX_SAFE_INTEGER`, so ids like Twitter's are sent as strings.

## 282: How do you write a generic Stack in TypeScript?

Use a type parameter so the stack keeps the type of its items.

```ts
class Stack<T> {
  #items: T[] = [];

  push(item: T): void {
    this.#items.push(item);
  }
  pop(): T | undefined {
    return this.#items.pop();
  }
  peek(): T | undefined {
    return this.#items.at(-1);
  }
  get size(): number {
    return this.#items.length;
  }
}

const s = new Stack<number>();
s.push(1);
// s.push("a"); // type error
```

## 283: What do readonly arrays and as const do in TypeScript?

`readonly T[]` (or `ReadonlyArray<T>`) removes mutating methods like `push` and `sort` from the type, so the compiler stops you from changing the array. `as const` makes a literal deeply readonly and keeps exact literal types, which is useful for lookup tables and tuples.

```ts
const roles = ["admin", "editor", "viewer"] as const;
type Role = (typeof roles)[number]; // "admin" | "editor" | "viewer"

function total(nums: readonly number[]) {
  // nums.push(1); // error
  return nums.reduce((a, b) => a + b, 0);
}
```

These are compile-time only; at runtime the array can still change unless you freeze it.

## 284: What is the difference between Record and Map in TypeScript?

`Record<K, V>` is a type for a plain object whose keys are `K` (strings, numbers or symbols) and values are `V`. `Map<K, V>` is the runtime `Map` class, where `K` can be any type. Use `Record` for JSON-shaped data and fixed key sets; use `Map` for dictionaries with dynamic keys or non-string keys. With `Record<string, V>`, turn on `noUncheckedIndexedAccess` so reads are typed as `V | undefined`.

## 285: How do you model tree nodes with different types in TypeScript?

Use a discriminated union: each node type has a shared `type` field with a different literal value. TypeScript then narrows the type in `switch` statements.

```ts
type Expr =
  | { type: "num"; value: number }
  | { type: "add"; left: Expr; right: Expr }
  | { type: "mul"; left: Expr; right: Expr };

function evaluate(e: Expr): number {
  switch (e.type) {
    case "num":
      return e.value;
    case "add":
      return evaluate(e.left) + evaluate(e.right);
    case "mul":
      return evaluate(e.left) * evaluate(e.right);
  }
}
```

This is how ASTs, rich text documents and UI schema trees are usually typed.

## 286: How do you replace an item at an index without mutating?

Use `with(index, value)`. It returns a copy with one slot changed and supports negative indexes. It throws a `RangeError` if the index is out of range, which catches bugs.

```js
const steps = ["draft", "review", "publish"];
const next = steps.with(1, "approved"); // ["draft", "approved", "publish"]
steps.with(-1, "done"); // ["draft", "review", "done"]
```

Before ES2023 you'd write `steps.map((s, i) => i === 1 ? "approved" : s)`.

## 287: What is the difference between object spread and Object.assign?

Both copy own enumerable properties shallowly. Spread `{...a, ...b}` always creates a new object. `Object.assign(target, ...sources)` writes into `target`, so it mutates it, and it calls setters on the target, while spread defines new properties. For immutable updates use spread; use `Object.assign` when you really want to change an existing object.

## 288: Should you write data structures as classes or factory functions?

Both work. Classes give you private fields (`#items`), `instanceof` checks, shared methods on the prototype (less memory with many instances) and getters like `size`. Factory functions with closures also hide state well and avoid `this` problems when methods are passed as callbacks. For structures with many instances, like tree nodes, use plain objects or a class; for single-instance things like a store, either is fine.

## 289: Why use private class fields (#) in data structures?

They make the internal storage impossible to reach from outside, so nobody can do `stack.items.splice(0, 1)` and break the rules of the structure. You can change the inside later, for example from an array to a linked list, without breaking users. `#field in obj` also lets you check if an object is a real instance of your class.

## 290: Can Map.groupBy group by object keys?

Yes. Keys are compared by reference, so items that return the same object end up in the same group. This is useful when you group by a related entity you already have as an object.

```js
const ana = { name: "Ana" },
  ben = { name: "Ben" };
const tasks = [
  { title: "A", owner: ana },
  { title: "B", owner: ben },
  { title: "C", owner: ana },
];
const byOwner = Map.groupBy(tasks, (t) => t.owner);
byOwner.get(ana).length; // 2
```

With `Object.groupBy`, both owners would turn into `"[object Object]"` and land in one group.

## 291: How do you test your own data structure implementation?

Test the edge cases (empty, one item, full, duplicates), check that invariants hold after each operation (heap order, BST order, `size` matches the real count), and compare against a simple reference. For example, run thousands of random operations on your heap and on a sorted array, and check that they always agree. That last method, a form of property-based testing, catches bugs that hand-written tests miss.

```js
const heap = new MinHeap();
const ref = [];
for (let i = 0; i < 10_000; i++) {
  if (Math.random() < 0.6) {
    const v = Math.random();
    heap.push(v);
    ref.push(v);
  } else {
    ref.sort((a, b) => a - b);
    console.assert(heap.pop() === ref.shift());
  }
}
```

## 292: What data structures would you use for a todo app with filters and drag-and-drop reordering?

A `Map` (or object) from id to todo for O(1) updates, and an array of ids for the order. Reordering only changes the id array. Filters (all, active, done) are computed views over the ids, memoized so they don't recompute on every render. Selected items fit in a `Set` of ids. This is the normalized shape again, and it keeps updates small.

## 293: How would you store messages in a chat app?

A `Map` from conversation id to an array of message ids sorted by time, and a `Map` from message id to message. New messages usually come at the end, so pushing is cheap. Older history loads at the start; prepend a whole page at once instead of one by one. Messages that might arrive out of order are placed with a binary search on the timestamp. A `Set` of seen message ids stops duplicates when the same message comes from both the API and a WebSocket.

## 294: How do you use a Set in React state?

React needs a new reference to see a change, but `add` and `delete` mutate the set. Create a new `Set` for every update.

```jsx
const [selected, setSelected] = useState(() => new Set());

function toggle(id) {
  setSelected((prev) => {
    const next = new Set(prev);
    next.has(id) ? next.delete(id) : next.add(id);
    return next;
  });
}

<input
  type="checkbox"
  checked={selected.has(item.id)}
  onChange={() => toggle(item.id)}
/>;
```

## 295: What problems can Map and Set cause in app state?

They aren't JSON-friendly, so things like Redux DevTools, persisting to `localStorage` and server-side rendering hydration need extra work. Redux warns about non-serializable values in state by default. Mutating them in place doesn't change the reference, so UI libraries miss updates. Many teams keep plain objects and arrays in global state and use `Map` and `Set` inside components or in derived data.

## 296: How do you remove items from a Map while looping over it?

You can delete entries during a `for...of` loop over a `Map` or `Set`; the spec says deleted entries that haven't been visited yet are skipped, and nothing breaks.

```js
for (const [key, entry] of cache) {
  if (entry.expires < Date.now()) cache.delete(key);
}
```

Adding new entries during the loop is also allowed, but they will be visited too, which can make a loop run forever if you keep adding.

## 297: How do you merge two Maps?

Spread both into a new `Map`. When keys repeat, the later one wins.

```js
const defaults = new Map([
  ["theme", "light"],
  ["lang", "en"],
]);
const user = new Map([["theme", "dark"]]);
const settings = new Map([...defaults, ...user]);
settings.get("theme"); // "dark"
```

For a custom merge (like adding counts), loop and combine values yourself.

## 298: How do you invert an object or Map (swap keys and values)?

```js
const codes = { en: "English", ka: "Georgian" };
const byName = Object.fromEntries(
  Object.entries(codes).map(([k, v]) => [v, k]),
);
// { English: "en", Georgian: "ka" }

const m = new Map([
  ["a", 1],
  ["b", 2],
]);
const inverted = new Map([...m].map(([k, v]) => [v, k]));
```

If two keys share a value, only the last one survives. Group into arrays if you need all of them.

## 299: How do you chunk an array into groups of n?

```js
function chunk(arr, size) {
  return Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
    arr.slice(i * size, i * size + size),
  );
}
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```

This is common for batching API requests, building grid rows and paging data on the client.

## 300: How do you zip two arrays into pairs?

```js
const names = ["a", "b", "c"];
const scores = [1, 2, 3];
const pairs = names.map((n, i) => [n, scores[i]]); // [["a", 1], ["b", 2], ["c", 3]]
const byName = new Map(pairs);
```

If the arrays can have different lengths, decide on purpose: cut to the shorter one with `Math.min`, or fill missing values with `undefined`.

# Advanced Questions (301-450)

## 301: How does V8 store objects internally?

Each object points to a hidden class (V8 calls it a "map", other engines call it a "shape") that describes its layout: which properties it has and at what offset each value sits. Objects created the same way, with the same properties in the same order, share one hidden class. That lets V8 read `obj.x` from a fixed offset instead of looking it up by name. Adding a property creates a transition to a new hidden class, so objects that get properties in different orders end up with different classes.

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
} // all Points share one shape
const a = { x: 1, y: 2 };
const b = { y: 2, x: 1 }; // different shape from a
```

## 302: What is dictionary mode, and what pushes an object into it?

When an object's shape changes too much, V8 stops using hidden classes for it and stores its properties in a hash table, called dictionary (or slow) mode. Common causes: deleting properties (except the last one added), adding a very large number of properties, or using an object as a hash map with many dynamic keys. Lookups still work, but inline caches can't speed them up. That's one practical reason to use `Map` for dictionaries and keep records with a fixed shape.

## 303: What are elements kinds in V8?

V8 stores array items (the "elements") separately from named properties and tracks what kind they are: `PACKED_SMI_ELEMENTS` (small integers), `PACKED_DOUBLE_ELEMENTS`, `PACKED_ELEMENTS` (anything), and `HOLEY_` versions of each. Transitions only go toward more general kinds: SMI to double to generic, and packed to holey. An array that ever held a string stays generic even after you remove it. Keeping arrays packed and of one type lets the engine generate tighter loops.

```js
const a = [1, 2, 3]; // PACKED_SMI
a.push(4.5); // PACKED_DOUBLE
a.push("x"); // PACKED_ELEMENTS
a[10] = 1; // HOLEY_ELEMENTS
```

## 304: How are Map and Set implemented in V8?

They use deterministic hash tables (based on a design by Tyler Close). Entries are stored in a flat array in insertion order, and a separate bucket array holds the index of the first entry for each hash, with entries in the same bucket linked by index. Deleting marks an entry as removed instead of shifting, and the table is rebuilt when it grows or has too many deleted slots. This design gives O(1) average operations and makes iteration in insertion order fast and stable.

## 305: How can a hash table also keep insertion order?

Keep entries in an append-only array and use the hash buckets only to point into that array. Iteration just walks the array in order, skipping deleted slots. A classic hash table with a linked list per bucket has no global order, which is why Java's `HashMap` doesn't keep order and `LinkedHashMap` adds a separate list. JavaScript's spec requires insertion order for `Map` and `Set`, so engines chose a design that gives it for free.

## 306: How does a Map hash an object key if objects have no hash code?

The engine gives each object a random identity hash the first time it's used as a key in a `Map`, `Set` or `WeakMap`, and stores it with the object (in V8, in the object's properties backing store or a header field). The same object always returns the same hash, so lookups work, while the hash has nothing to do with the object's content. That's also why two objects with equal content are different keys.

## 307: How do the memory costs of objects, arrays and Maps compare?

A plain object with a stable shape is the most compact for records: just a header plus one slot per property, and the property names live once in the shared hidden class. A packed array is similar, one slot per item. A `Map` has more overhead per entry, because it stores the key, value and a chain link, plus bucket space, and it keeps spare capacity. Typed arrays are the cheapest for numbers: 8 bytes per `Float64`, 1 byte per `Uint8`, with no per-item boxing. For millions of items these differences matter; for hundreds they don't. Use heap snapshots to measure instead of guessing.

## 308: What are Smis and heap numbers, and why should you care?

V8 stores small integers (Smis, 31 bits on most 64-bit builds with pointer compression) directly inside the value slot, so they need no extra memory. Other numbers, like decimals or large integers, are stored as boxed `HeapNumber` objects, except inside double arrays and some object fields where V8 can keep raw doubles. In hot code, a field that switches between integer and decimal values can cause shape changes and extra allocations. For big numeric data, typed arrays avoid the question entirely.

## 309: How does an array's backing store grow?

When you `push` past the current capacity, V8 allocates a new backing store about 1.5 times bigger (plus a small constant) and copies the elements over. Most pushes then just write into spare capacity, which is why `push` is amortized O(1). If you know the final size, building the array with `Array.from({ length: n }, fn)` or filling a preallocated typed array avoids repeated growth. Shrinking with `pop` or `length = 0` may also release memory later.

## 310: How does V8 represent strings, and why can concatenation be cheap?

V8 has several string types. Sequential strings store characters in one block, one byte per character for Latin-1 and two for others. Cons strings (ropes) are created by `a + b`: just a node pointing to both parts, so concatenation is O(1). Sliced strings point into a parent string for `slice` and `substring`. A cons string is flattened into a sequential string when you read characters from it. One side effect: a small slice can keep a huge parent string alive in memory.

## 311: Is building a string with += in a loop slow?

Usually not anymore. Because `+=` creates cons strings, appending is cheap, and the engine flattens once when you read the result. `array.join("")` is still fine and sometimes clearer when parts are built separately. What does stay slow is reading characters from the string inside the same loop that appends to it, since each read can force flattening. Measure in your target engine before rewriting working code.

## 312: How does garbage collection affect the design of data structures?

V8 uses a generational collector: most objects die young and are cleaned quickly in the young generation, and long-lived objects move to the old generation, which is collected less often but costs more. Structures made of millions of small node objects (linked lists, tree nodes, wrapper objects) make GC do more work and can cause pauses. Flat arrays, typed arrays and fewer, bigger objects cut that cost. That's why high-performance code often stores trees or graphs in arrays of indexes instead of linked objects.

## 313: What is object pooling, and when is it worth it?

A pool keeps reusable objects instead of creating new ones and dropping them. You `acquire` an object, use it, and `release` it back. It reduces GC pressure in hot loops, like particles in a game or vectors in a physics step at 60 frames per second. In normal app code it's rarely worth it: modern GCs handle short-lived objects well, and pools add bugs like using an object after you released it.

```js
class Pool {
  #free = [];
  constructor(create) {
    this.create = create;
  }
  acquire() {
    return this.#free.pop() ?? this.create();
  }
  release(obj) {
    this.#free.push(obj);
  }
}
const vectors = new Pool(() => ({ x: 0, y: 0 }));
```

## 314: What is the difference between an array of structs and a struct of arrays?

An array of structs (AoS) is the usual `[{ x, y, vx, vy }, ...]`. A struct of arrays (SoA) keeps one array per field: `{ x: Float32Array, y: Float32Array, ... }`. SoA uses typed arrays, has no per-object overhead, and a loop that touches only `x` and `vx` reads memory in order, which is cache-friendly. It's common in games, charts with huge datasets and WebGL. AoS is easier to read and better when you usually need all fields of one item together.

```js
const n = 100_000;
const particles = {
  x: new Float32Array(n),
  y: new Float32Array(n),
  vx: new Float32Array(n),
  vy: new Float32Array(n),
};
for (let i = 0; i < n; i++) {
  particles.x[i] += particles.vx[i];
  particles.y[i] += particles.vy[i];
}
```

## 315: When are typed arrays clearly faster than normal arrays?

For large numeric data that you loop over a lot: images, audio samples, chart points, physics, matrices. They use a known fixed type, so the engine never checks types or boxes numbers, memory is compact, and they can go to WebGL, WebGPU, Web Audio, WebAssembly and workers without conversion. For small arrays, mixed data, or code that needs `push` and `splice`, normal arrays are just as good and easier to use.

## 316: What is SharedArrayBuffer, and why does it need cross-origin isolation?

A `SharedArrayBuffer` is memory that several threads (the main thread and workers) can read and write at the same time, without copying. After the Spectre attacks, browsers only allow it on pages that are cross-origin isolated, because shared memory makes very precise timers possible. To turn it on, the page must send `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp` (or `credentialless`). You can check with `self.crossOriginIsolated`.

## 317: What does Atomics do?

`Atomics` gives safe operations on shared integer typed arrays: `load`, `store`, `add`, `sub`, `compareExchange` and more happen as one step, so two threads can't mix up a read and a write. `Atomics.wait` and `Atomics.notify` let a worker sleep until another thread signals it, and `Atomics.waitAsync` does the same without blocking. These are the building blocks for locks, counters and queues shared between threads.

```js
const shared = new Int32Array(new SharedArrayBuffer(4));
Atomics.add(shared, 0, 1); // safe increment from any thread
Atomics.notify(shared, 0); // wake a waiting worker
```

`Atomics.wait` isn't allowed on the browser main thread, since it would freeze the page.

## 318: How would you build a ring buffer shared between the main thread and a worker?

Put the data and two indexes (read and write) in a `SharedArrayBuffer`. With one producer and one consumer, each side only writes its own index, and both use `Atomics.load` and `Atomics.store` so the other side sees updates in the right order. The producer writes data, then moves the write index; the consumer reads data, then moves the read index. The buffer is full when the write index is one slot behind the read index. Audio worklets use this pattern to pass samples without copying or locks.

```js
// layout: [readIdx, writeIdx] + data
const meta = new Int32Array(sab, 0, 2);
const data = new Float32Array(sab, 8, capacity);

function push(value) {
  const w = Atomics.load(meta, 1),
    r = Atomics.load(meta, 0);
  const next = (w + 1) % capacity;
  if (next === r) return false; // full
  data[w] = value;
  Atomics.store(meta, 1, next);
  return true;
}
```

## 319: What are resizable ArrayBuffers?

Since ES2024, you can create an `ArrayBuffer` with a `maxByteLength` and grow or shrink it later with `resize()`, without allocating a new buffer and copying. Typed arrays created without a fixed length track the buffer's size on their own. `SharedArrayBuffer` has a similar `grow()` (it can only grow). This helps when you stream data of unknown size, like reading a file in chunks.

```js
const buf = new ArrayBuffer(1024, { maxByteLength: 1024 * 1024 });
const view = new Uint8Array(buf); // length-tracking
buf.resize(4096);
view.length; // 4096
```

## 320: What does ArrayBuffer.prototype.transfer do, and what is a detached buffer?

`transfer()` (ES2024) moves the memory to a new `ArrayBuffer` and detaches the old one: its `byteLength` becomes 0, and any views on it stop working. It can also change the size at the same time. The same thing happens when you send a buffer to a worker with `postMessage(buf, [buf])`: ownership moves instead of copying, which is very fast for large data, but the sender can no longer use it.

```js
const a = new ArrayBuffer(8);
const b = a.transfer();
a.detached; // true
a.byteLength; // 0
```

## 321: What is Float16Array?

`Float16Array` (ES2025) stores 16-bit (half precision) floating point numbers, using half the memory of `Float32Array`. It's useful for GPU work, machine learning model weights and textures, where half precision is common and memory matters. Values are rounded when written, and `Math.f16round` gives the same rounding for single numbers. `DataView` got `getFloat16` and `setFloat16` too. Check browser support before relying on it, since it shipped later in some engines.

## 322: What newer methods help convert bytes to base64 and hex?

`Uint8Array.fromBase64`, `Uint8Array.prototype.toBase64`, `Uint8Array.fromHex` and `toHex`, plus `setFromBase64` and `setFromHex` for writing into an existing array. They replace the old `btoa`/`atob` tricks, which only work with "binary strings" and break on non-Latin-1 text. They're a newer addition, so check support in your target browsers and have a fallback.

```js
const bytes = new TextEncoder().encode("héllo");
const b64 = bytes.toBase64(); // "aMOpbGxv"
Uint8Array.fromBase64(b64); // back to bytes
bytes.toHex(); // "68c3a96c6c6f"
```

## 323: What does the structured clone algorithm support, and how does transfer work with it?

It's used by `structuredClone`, `postMessage`, `IndexedDB` and `history.pushState`. It copies primitives (except symbols), plain objects, arrays, `Date`, `RegExp`, `Map`, `Set`, `ArrayBuffer`, typed arrays, `Blob`, `File`, `ImageData`, `Error` types and more, and keeps shared and circular references intact. With the `transfer` option, buffers and some objects (like `MessagePort`, `ImageBitmap`, `OffscreenCanvas`, streams) are moved instead of copied.

```js
const buf = new ArrayBuffer(1e6);
const copy = structuredClone({ buf }, { transfer: [buf] });
buf.byteLength; // 0, the memory moved into copy.buf
```

## 324: What are the rules for WeakRef.deref()?

`deref()` returns the object or `undefined` if it's been collected. The spec says an object you `deref` stays alive until the end of the current synchronous job, so two calls in the same tick give the same result and you won't see it vanish mid-function. Across `await` or timers, it can disappear at any time. Engines are free to collect late or never, so code must work whether or not collection happens. Always store the dereferenced value in a local variable and check it once.

## 325: What are the pitfalls of FinalizationRegistry?

Callbacks run at some point after collection, maybe much later, maybe never (for example, if the page closes). They can't access the collected object, only the "held value" you registered. If the held value references the target, the target can never be collected. Don't use it to release important resources like file handles or server sessions; use explicit `close()` or `dispose()` methods, or `using` with `Symbol.dispose` where supported. It's fine for best-effort cleanup like removing dead entries from a cache of `WeakRef`s.

## 326: What is an ephemeron, and why does it matter for WeakMap?

A `WeakMap` entry is an ephemeron: its value is kept alive only while its key is alive. That holds even if the value references the key. In a normal `Map` that would be a leak, but in a `WeakMap` the cycle is collected once nothing outside points to the key. This is what makes `WeakMap` safe for attaching metadata to objects you don't control. It's also why engines need special GC logic for them, and why huge numbers of WeakMap entries can make GC slower.

## 327: How do you find a memory leak caused by a cache or registry?

Take a heap snapshot in Chrome DevTools, do the action that leaks a few times, take another snapshot, and use the "Comparison" view to see which object types grew. Pick a leaked object and look at its "Retainers" to find what's holding it, often a `Map`, an array of listeners, or a closure. The "Allocation instrumentation on timeline" tool shows objects created over time that never get freed. The usual fixes: remove entries when things unmount, add size limits, or switch to a `WeakMap`.

## 328: How does an AVL tree stay balanced?

Every node tracks its height, and for every node the heights of its left and right subtrees can differ by at most 1. After an insert or delete, walk back up and check this balance factor. If it's off, fix it with a rotation: single right or left rotations for the "left-left" and "right-right" cases, and double rotations for "left-right" and "right-left". Height stays below about 1.44 log₂(n), so lookups are fast.

```js
const h = (n) => n?.height ?? 0;
const update = (n) => {
  n.height = 1 + Math.max(h(n.left), h(n.right));
  return n;
};

function rotateRight(y) {
  const x = y.left;
  y.left = x.right;
  x.right = y;
  update(y);
  return update(x);
}
```

## 329: What rules does a red-black tree follow?

Every node is red or black, the root is black, a red node can't have a red child, and every path from a node down to its empty leaves has the same number of black nodes. Together, these rules make the longest path at most twice the shortest, so height is O(log n). It's less strictly balanced than AVL, so lookups can be a bit slower, but inserts and deletes need fewer rotations. Java's `TreeMap`, C++'s `std::map` and the Linux kernel use red-black trees.

## 330: What is a B-tree, and why do databases use it?

A B-tree is a balanced search tree where each node holds many keys (often hundreds) and has many children. The tree is very short and wide, so finding a key reads only a few nodes. Each node fits a disk page, which makes it ideal for storage where reading a block is expensive. B+ trees keep all values in the leaves and link leaves together for fast range scans. SQLite and Postgres use B-tree variants, and Firefox and Safari store IndexedDB data in SQLite (Chrome uses LevelDB, a different sorted structure). Either way, IndexedDB keeps keys sorted, which is why range queries with `IDBKeyRange` are fast.

## 331: What is a skip list?

A skip list is a sorted linked list with extra "express lanes". Each node is randomly given a height; higher levels skip over many nodes. Search starts at the top level, moves right while the next key is smaller, and drops down a level when it can't. On average, search, insert and delete are O(log n). It's simpler to write than a balanced tree and works well with concurrency. Redis uses skip lists for sorted sets.

## 332: What is a Fenwick tree (binary indexed tree)?

A Fenwick tree stores partial sums in an array so you can update a value and get a prefix sum both in O(log n), using bit tricks on the index. It's smaller and simpler than a segment tree but only supports operations that can be undone, like sums.

```js
class Fenwick {
  constructor(n) {
    this.tree = new Float64Array(n + 1);
  }
  add(i, delta) {
    // i is 0-based
    for (i++; i < this.tree.length; i += i & -i) this.tree[i] += delta;
  }
  prefixSum(i) {
    // sum of [0..i]
    let s = 0;
    for (i++; i > 0; i -= i & -i) s += this.tree[i];
    return s;
  }
}
```

A front-end use: a virtual list with variable row heights, where you update one row's height and need the offset of any row quickly.

## 333: How would you find overlapping events in a calendar quickly?

An interval tree: a BST ordered by start time where each node also stores the maximum end time in its subtree. To find events overlapping a range, you skip any subtree whose max end is before your range start. Queries are O(log n + k), where k is the number of matches. For a single day view with a few dozen events, sorting by start and sweeping is simpler and fast enough; the tree pays off with thousands of events and frequent queries.

## 334: What is a quadtree, and how does it help with canvas hit testing?

A quadtree splits 2D space into four squares, and splits each square again when it holds too many items. To find which shapes are under the mouse, or which items are on screen, you only check squares that overlap the point or viewport, instead of every shape. That turns O(n) checks into roughly O(log n) for evenly spread data. It's used in maps, diagram editors, games and big scatter plots.

## 335: What is a spatial hash grid, and when is it better than a quadtree?

A spatial hash divides space into fixed-size cells and stores each item in a `Map` keyed by its cell coordinates. Lookups are O(1) per cell, and the code is short. It works best when items are similar in size and spread evenly, like particles or game units. A quadtree adapts better to uneven data and items of very different sizes. Both beat checking every item against every other for collisions.

```js
const cell = 64;
const key = (x, y) => `${Math.floor(x / cell)},${Math.floor(y / cell)}`;
const grid = new Map();
function insert(item) {
  const k = key(item.x, item.y);
  if (!grid.has(k)) grid.set(k, []);
  grid.get(k).push(item);
}
```

## 336: What is a k-d tree?

A k-d tree is a binary tree for points in k dimensions. Each level splits on one axis (x, then y, then x again for 2D), using the median point. It's used for nearest-neighbor search: find the closest store to a user, the closest data point to the mouse in a chart, or nearby colors in a palette. Average search is O(log n) for low dimensions; in high dimensions it becomes no better than a full scan.

## 337: What is a rope, and why do text editors use something like it?

A rope stores a long string as a balanced binary tree of smaller strings, where each node knows the length of its left subtree. Inserting or deleting in the middle of a huge document becomes O(log n) instead of copying the whole string. Finding the character at a position walks down by lengths. Editors handle files with millions of characters this way, and many keep line counts in each node too, so "go to line" is fast.

## 338: What is a gap buffer?

A gap buffer is an array with an empty "gap" at the cursor. Typing fills the gap and deleting widens it, both O(1). Moving the cursor moves the gap, which copies the characters in between, so it's cheap when edits happen near each other, as they do when people type. Emacs uses a gap buffer. Its weakness is jumping between distant spots, like multi-cursor editing far apart.

## 339: What is a piece table?

A piece table keeps the original file as one read-only buffer and all added text in an append-only buffer. The document is a list of "pieces", each pointing to a range in one of the two buffers. Edits only add pieces or split them; nothing is copied or deleted, which makes undo simple. VS Code uses a piece table with the pieces stored in a red-black tree (a "piece tree") so lookups by offset and line are O(log n).

## 340: What data structures are behind collaborative editing (CRDTs)?

A CRDT (conflict-free replicated data type) is a structure designed so that copies on different devices can be changed independently and then merged into the same result, without a central server deciding. For text, sequence CRDTs give every character a unique id with ordering info, so inserts at the same spot from two users end up in the same order everywhere, and deletes leave tombstones. Libraries like Yjs and Automerge implement them. Simpler CRDTs include counters that only grow, and sets where adds and removes are tagged.

## 341: What is a hash array mapped trie (HAMT)?

A HAMT is a persistent (immutable) hash map. It hashes the key and uses chunks of the hash bits (often 5 bits, so 32 branches) to pick a path in a trie. Each node stores a bitmap of which children exist plus a compact array of only those children. An "update" copies only the nodes along one path, about log₃₂(n) of them, and shares everything else with the old version. Immutable.js `Map`, Clojure's maps and Scala's immutable maps use it.

## 342: How does a persistent linked list share structure?

Adding to the front of an immutable list creates one new node that points to the old list. The old list is unchanged and both versions share all the old nodes. Two lists can share a common tail forever with no copying. It only works well at the front; changing the end means copying the whole list. This is why functional languages build lists by prepending.

```js
const empty = null;
const cons = (head, tail) => Object.freeze({ head, tail });
const a = cons(2, cons(3, empty));
const b = cons(1, a); // b shares all of a's nodes
```

## 343: Immutable.js or Immer: what is the difference?

Immutable.js gives you its own persistent data structures (`List`, `Map`, `Record`) built on tries, with structural sharing for every update. It's efficient for very large collections changed often, but you must use its API everywhere and convert to plain JS for rendering and JSON. Immer works on plain objects and arrays: you write normal mutations on a draft, and it copies just the changed path. Most new projects use Immer (Redux Toolkit includes it) because the data stays normal JavaScript.

## 344: How does a persistent vector give fast immutable updates?

It's a wide tree, usually 32 children per node, with the items in the leaves. Updating index i copies only the nodes on the path to that leaf (about log₃₂(n), so 4 or 5 nodes for a million items) and shares the rest. Appending works the same way, often with a "tail" buffer to make it even cheaper. Clojure's vectors and Immutable.js `List` work like this. Compared with copying a plain array on every change, which is O(n), this is what makes large immutable lists practical.

## 345: What is a radix tree, and how is it different from a trie?

A radix tree (compressed trie) merges chains of nodes that have only one child into a single edge labeled with a whole substring. So "/users/profile" and "/users/settings" share a "/users/" edge instead of seven single-character nodes. It uses much less memory and fewer hops. Fast HTTP routers like `find-my-way` (used by Fastify) use radix trees to match URL paths, including route parameters.

## 346: What are suffix arrays and suffix trees used for?

A suffix array is a sorted list of the starting positions of all suffixes of a string. A suffix tree is a compressed trie of all suffixes. Both answer "does this pattern appear in the text, and where?" in time based on the pattern length, after building the index once. They're used in full-text search, DNA analysis and finding the longest repeated substring. In front-end work you'd rarely build one by hand, but they explain how some search libraries work.

## 347: What is a count-min sketch?

A count-min sketch estimates how often items appear in a stream using a small, fixed amount of memory. It's a 2D array of counters with one hash function per row. To add an item, increase one counter in each row. To estimate a count, take the minimum of the item's counters. It can overcount (due to collisions) but never undercounts. It's used for "heavy hitters" like most clicked links or most frequent errors when you can't store a counter for every distinct value.

## 348: What is HyperLogLog?

HyperLogLog estimates how many distinct items are in a huge set, like unique visitors, using a few kilobytes of memory and about 1 to 2 percent error. It hashes each item and looks at the number of leading zero bits; long runs of zeros are rare, so the longest run seen hints at how many distinct items there were. Many registers are averaged to reduce error, and two sketches can be merged. Redis and analytics systems use it widely.

## 349: What is cuckoo hashing?

Cuckoo hashing uses two hash functions, so each key has two possible slots. Lookups check at most two places, which makes them O(1) in the worst case, not just on average. On insert, if both slots are taken, the new key kicks out an existing one, which then moves to its other slot, possibly kicking out another key, like a cuckoo bird. If this loops too long, the table is rebuilt with new hash functions. Cuckoo filters, a Bloom filter alternative that supports deletes, are based on it.

## 350: What is Robin Hood hashing?

It's a type of open addressing. While inserting, if the new key has traveled farther from its ideal slot than the key sitting in the current slot, they swap, and you keep inserting the displaced key. This "takes from the rich and gives to the poor": it keeps probe lengths even, so worst-case lookups stay short and failed lookups can stop early. Rust's old standard `HashMap` used it before moving to SwissTable.

## 351: What is a hash flooding attack?

If an attacker knows your hash function, they can send many keys that all land in the same bucket, for example as JSON keys or query parameters. Every insert and lookup then becomes O(n), and parsing one request can take seconds of CPU time, a denial of service. Defenses include seeded random hash functions (like SipHash in many languages), limits on input size and number of keys, and tree-based buckets for long chains. JavaScript engines seed their hashes, but your own server-side code should still cap request sizes.

## 352: How do you write a safe deep merge?

A deep merge copies keys from a source into a target recursively, which is the classic place for prototype pollution. Block dangerous keys, only copy own properties, and only recurse into plain objects.

```js
const isPlain = (v) =>
  v !== null &&
  typeof v === "object" &&
  [Object.prototype, null].includes(Object.getPrototypeOf(v));
const BLOCKED = new Set(["__proto__", "constructor", "prototype"]);

function deepMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (BLOCKED.has(key)) continue;
    const value = source[key];
    if (isPlain(value)) {
      if (!isPlain(target[key])) target[key] = {};
      deepMerge(target[key], value);
    } else {
      target[key] = value;
    }
  }
  return target;
}
```

## 353: Are Map and Object.create(null) enough to stop prototype pollution?

They stop the most common case: reading and writing user keys like `__proto__` won't touch `Object.prototype`. But pollution can still happen elsewhere: a library that deep merges, code that does `obj[a][b] = c` with two user-controlled keys, or query string parsers that build nested objects. Defense in depth: validate input with a schema, keep dependencies updated, and in Node.js consider `--disable-proto=delete`. Freezing `Object.prototype` at startup is a stronger option, but it can break libraries that change prototypes.

## 354: What data structure does Vue's reactivity system use to track dependencies?

A `WeakMap` from each reactive object to a `Map` from property key to a set of effects that read it (`WeakMap<target, Map<key, Dep>>`). When an effect runs, every reactive read adds the current effect to that property's set. When a property is written, Vue looks up its set and schedules those effects. The `WeakMap` means a reactive object that's no longer used can be garbage collected together with its tracking data. Recent Vue versions use linked-list based dependency nodes internally for speed, but the lookup idea is the same.

## 355: How are signals stored as a dependency graph?

Each signal is a node that knows the computed values and effects that depend on it, and each computed knows its sources. Reading a signal inside a computed adds an edge. When a signal changes, it marks its dependents as dirty (push), but computeds only re-run when someone reads them (pull). Keeping versions or a "dirty" flag per node lets the system skip computeds whose inputs didn't actually change. Preact Signals, for example, stores these edges in doubly linked lists, so subscribing and unsubscribing are O(1) with no extra arrays.

## 356: Why is the virtual DOM a tree, and how do keys change the diff?

The virtual DOM mirrors the real DOM, so it's a tree of plain objects describing elements and components. Diffing two arbitrary trees is O(n³), so React and others use rules to make it O(n): compare level by level, assume a different element type means a different subtree, and match children by `key`. With keys, the diff builds a lookup from key to old child, so reordered items are moved instead of re-created. Without stable keys (or with index keys on lists that change order), items get matched to the wrong old child, which causes wrong state and extra DOM work.

## 357: How does React Fiber represent the component tree?

Each fiber is an object with `child` (first child), `sibling` (next sibling) and `return` (parent) pointers, so the tree is really a set of linked lists. This lets React walk the whole tree with a loop instead of recursion, pause at any fiber, give control back to the browser, and continue later from the same spot. Each fiber also has an `alternate` pointing to its copy in the other tree (current vs work-in-progress), which is how React builds the next UI without touching what's on screen.

## 358: How are hooks stored, and why can't you call them conditionally?

Each fiber keeps its hooks as a linked list in `memoizedState`, one node per hook call in the order they ran. On every render, React walks this list in order and matches the first `useState` call to the first node, the second to the second, and so on. There are no names or ids. If a hook is skipped behind an `if`, every later hook reads the wrong node. That's the reason for the Rules of Hooks.

## 359: What queues does the browser event loop use?

There are task queues (timers, I/O, user events, `postMessage`), and the browser can pick between task sources by priority. After each task, the microtask queue (promise callbacks, `queueMicrotask`, `MutationObserver`) is fully drained, including microtasks added while draining. Then, when it's time to render, the browser runs `requestAnimationFrame` callbacks, style, layout and paint. Knowing these are separate queues explains why a promise loop can freeze the page while a `setTimeout` loop doesn't.

```js
setTimeout(() => console.log("task"));
Promise.resolve().then(() => console.log("microtask"));
console.log("sync");
// sync, microtask, task
```

## 360: What trees does the browser build to render a page?

The DOM tree from HTML and the CSSOM tree from CSS. Together, they produce the render tree (the layout tree in Chrome), which only has visible elements with computed styles; `display: none` nodes are left out, while pseudo-elements are added. Layout computes boxes on that tree, then paint and compositing use layer trees and display lists. Changes that affect geometry rerun layout on part of the tree, which is why reading `offsetHeight` right after changing styles can be expensive.

## 361: What data structure helps a virtual list with variable row heights?

You need fast answers to two questions: "where does row i start?" and "which row is at scroll offset y?". Keep an array of prefix sums of row heights: offset of row i is `prefix[i]`, and the row at offset y is found by binary search. If heights change often (rows measured after render), a Fenwick tree lets you update one height and still get offsets in O(log n), instead of rebuilding prefix sums in O(n).

## 362: How do you find the first visible row from a scroll position?

Binary search the prefix sums for the last row whose start is less than or equal to the scroll position.

```js
// offsets[i] = top of row i, sorted ascending
function rowAt(offsets, scrollTop) {
  let lo = 0,
    hi = offsets.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (offsets[mid] <= scrollTop) lo = mid;
    else hi = mid - 1;
  }
  return lo;
}
```

Then render rows from there until their top passes `scrollTop + viewportHeight`, plus a few extra (overscan) to avoid blank flashes while scrolling.

## 363: Snapshots or commands: how should undo history be stored?

Snapshots store the whole state after each change. With immutable data and structural sharing, each snapshot only costs the changed parts, and undo is just picking an earlier state. Commands store the operation and how to reverse it (`{ do, undo }`), which uses less memory for huge documents but needs a correct inverse for every action. Big editors often mix them: commands for history, plus occasional snapshots so you don't replay too much. Either way, cap the history length.

## 364: How do Immer patches help with undo and syncing?

With `produceWithPatches`, Immer returns the new state, a list of patches describing what changed, and inverse patches that undo it. Patches are small JSON objects like `{ op: "replace", path: ["todos", 0, "done"], value: true }`. You can store inverse patches for undo, send forward patches to a server or other tabs, and apply them with `applyPatches`. You need to call `enablePatches()` once first.

```js
import { enablePatches, produceWithPatches, applyPatches } from "immer";
enablePatches();

const [next, patches, inverse] = produceWithPatches(state, (d) => {
  d.count++;
});
const undone = applyPatches(next, inverse); // back to state
```

## 365: How does a normalized GraphQL client cache work?

Clients like Apollo and urql's Graphcache split each response into objects, identify each by `__typename` plus `id`, and store them in a flat map like `{ "User:7": {...}, "Post:1": { author: { __ref: "User:7" } } }`. Queries are stored as references into that map. When any query or mutation returns `User:7`, the single cached entry updates and every query showing that user re-renders. It's a normalized store built automatically from the schema.

## 366: How would you design a client-side cache with tag-based invalidation?

Store entries in a `Map` from cache key to `{ data, tags }`, and keep a reverse index: a `Map` from tag to a `Set` of keys. Invalidating a tag looks up the set and deletes or marks those entries as stale in O(number of affected entries). This is how RTK Query's `providesTags` / `invalidatesTags` and Next.js `revalidateTag` work conceptually.

```js
const entries = new Map();
const byTag = new Map();

function put(key, data, tags) {
  entries.set(key, { data, tags });
  for (const t of tags) {
    if (!byTag.has(t)) byTag.set(t, new Set());
    byTag.get(t).add(key);
  }
}
function invalidate(tag) {
  for (const key of byTag.get(tag) ?? []) entries.delete(key);
  byTag.delete(tag);
}
```

A full version also removes keys from their other tags' sets when deleting, so the index doesn't grow forever.

## 367: How would you limit a cache by total size in bytes instead of entry count?

Store each entry's size, keep a running total, and evict least recently used entries until you're under the limit. For strings, size is about `length * 2`; for buffers, use `byteLength`; for objects, estimate (for example, with the length of their JSON) or let the caller pass a size. The `lru-cache` npm package supports this with `maxSize` and `sizeCalculation`, and also lets you combine it with TTL.

```js
set(key, value, size) {
  if (this.map.has(key)) this.total -= this.map.get(key).size;
  this.map.delete(key);
  this.map.set(key, { value, size });
  this.total += size;
  for (const [k, e] of this.map) {
    if (this.total <= this.maxBytes) break;
    this.map.delete(k);
    this.total -= e.size;
  }
}
```

## 368: How would you store an infinite scroll feed so items don't repeat or jump?

Keep a `Map` from id to item and an array of ids in display order, plus a `Set` of seen ids. New pages append only ids you haven't seen; new items at the top go into a separate "pending" list and are shown only when the user taps "new posts", so the content under the reader doesn't move. Use a cursor (like the last item's id or timestamp) for paging instead of page numbers, which skip or repeat items when new ones arrive. For very long sessions, drop items far above the viewport and keep their measured heights.

## 369: How would you combine a trie and a heap for ranked autocomplete?

The trie finds all words with the typed prefix. To return the top k by popularity without scanning every match, either keep a small min heap of size k while walking the matching subtree, or store the top k results directly on each trie node and update them when popularity changes. The second option makes queries O(prefix length) at the cost of more memory and slower updates. For a small static list, a sorted array plus binary search on the prefix is often enough.

## 370: How would you design a notification queue with priorities and no duplicates?

A priority queue (heap) ordered by priority and then by time, plus a `Map` from notification key to its entry, so a repeat of the same notification updates the existing one ("3 new messages") instead of adding another. Show at most N at once; when one is dismissed or times out, pop the next. Dismissed keys can go into a `Set` with a short TTL so the same alert doesn't come straight back.

## 371: How do calendar apps lay out overlapping events side by side?

Sort events by start time (then by longer duration first). Sweep through them, grouping events whose times overlap into clusters. Inside a cluster, place each event in the first column whose last event has already ended; a min heap of column end times makes that fast. The number of columns in a cluster sets the width of each event. Some apps then widen events into free columns to their right.

## 372: What data structures does a spreadsheet need for recalculation?

A sparse map of cells, and a dependency graph with edges from each cell to the cells that use it. When a cell changes, find all cells reachable from it, sort them topologically, and recompute in that order, so every cell is computed once and after its inputs. Detect cycles while sorting and show `#REF!` or a circular reference error. Keeping both directions of edges (uses and used-by) makes updating a formula's dependencies cheap.

## 373: How would you design a file explorer tree that loads folders lazily?

Store nodes in a `Map` from id to node, and each folder's state: not loaded, loading, loaded, error. Children are arrays of ids filled when a folder is first expanded. Expanded folders go in a `Set`. For rendering, flatten only the visible part (expanded paths) into an array and virtualize it. Keep in-flight requests in a `Map` from folder id to promise, so expanding the same folder twice doesn't fetch twice. Moves and renames update one node and two parent child lists.

## 374: How do you keep a big list sorted when new items arrive?

Find the insert position with binary search (O(log n)), then insert with `splice` (O(n), but it's a fast memory move). That's usually much faster than pushing and re-sorting the whole list.

```js
function insertSorted(arr, item, compare) {
  let lo = 0,
    hi = arr.length;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (compare(arr[mid], item) <= 0) lo = mid + 1;
    else hi = mid;
  }
  arr.splice(lo, 0, item);
  return lo;
}
```

Using `<= 0` puts equal items after existing ones, keeping insertion order among ties. For hundreds of thousands of inserts, consider a balanced tree or a skip list.

## 375: JavaScript has no sorted map. What are your options?

For small or rarely changing data: keep a sorted array and use binary search. For frequent inserts and range queries: write or import a balanced BST, B-tree or skip list (packages like `sorted-btree` or `@js-sdsl/ordered-map`). If you only need "sorted when displayed", use a normal `Map` and sort its entries when you read them. Pick based on how often you insert compared to how often you need ordered reads.

## 376: How do you implement a sorted map with a BST in JavaScript?

Wrap a BST and add the operations a sorted map needs: `get`, `set`, `delete`, in-order iteration, and range queries. Range queries skip subtrees that are fully outside the range.

```js
class SortedMap {
  #root = null;
  #cmp;
  constructor(cmp = (a, b) => (a < b ? -1 : a > b ? 1 : 0)) {
    this.#cmp = cmp;
  }

  set(key, value) {
    if (!this.#root) {
      this.#root = { key, value, left: null, right: null };
      return;
    }
    let n = this.#root;
    while (true) {
      const c = this.#cmp(key, n.key);
      if (c === 0) {
        n.value = value;
        return;
      }
      const side = c < 0 ? "left" : "right";
      if (!n[side]) {
        n[side] = { key, value, left: null, right: null };
        return;
      }
      n = n[side];
    }
  }

  *range(lo, hi, n = this.#root) {
    if (!n) return;
    if (this.#cmp(lo, n.key) < 0) yield* this.range(lo, hi, n.left);
    if (this.#cmp(lo, n.key) <= 0 && this.#cmp(n.key, hi) <= 0)
      yield [n.key, n.value];
    if (this.#cmp(n.key, hi) < 0) yield* this.range(lo, hi, n.right);
  }
}
```

Without balancing, sorted input makes it a chain, so a real one should use AVL or red-black rules (or a B-tree).

## 377: How do you build a deque on a circular buffer that grows?

Use an array whose size is a power of two, with `head` and `length`. Indexes wrap with `& (capacity - 1)`. When it's full, copy the items in order into an array twice as big.

```js
class RingDeque {
  #buf = new Array(8);
  #head = 0;
  #len = 0;

  #grow() {
    const old = this.#buf,
      cap = old.length;
    this.#buf = new Array(cap * 2);
    for (let i = 0; i < this.#len; i++)
      this.#buf[i] = old[(this.#head + i) & (cap - 1)];
    this.#head = 0;
  }
  pushBack(x) {
    if (this.#len === this.#buf.length) this.#grow();
    this.#buf[(this.#head + this.#len++) & (this.#buf.length - 1)] = x;
  }
  pushFront(x) {
    if (this.#len === this.#buf.length) this.#grow();
    this.#head = (this.#head - 1) & (this.#buf.length - 1);
    this.#buf[this.#head] = x;
    this.#len++;
  }
  popFront() {
    if (!this.#len) return undefined;
    const x = this.#buf[this.#head];
    this.#buf[this.#head] = undefined; // let GC collect it
    this.#head = (this.#head + 1) & (this.#buf.length - 1);
    this.#len--;
    return x;
  }
  get size() {
    return this.#len;
  }
}
```

All operations are amortized O(1), items stay in one array, and cleared slots don't keep old objects alive.

## 378: Why is a circular buffer faster than an object-based queue?

An object with integer keys that keep growing (head and tail indexes going up forever) doesn't stay a nice packed array; the engine may switch it to dictionary storage, so every access is a hash lookup. A ring buffer reuses the same packed array slots, so access is a plain index read, memory stays compact, and there's nothing for GC to clean per item. In benchmarks with millions of operations, ring buffers are often several times faster.

## 379: How do you support "change priority" in a heap?

Keep a `Map` from item to its index in the heap array, and update it on every swap. To change an item's priority, look up its index, update the value, and sift up or down. Removing any item works the same way: swap it with the last item, pop, then sift. Dijkstra's algorithm and task schedulers that reprioritize jobs need this.

```js
#swap(i, j) {
  const a = this.items;
  [a[i], a[j]] = [a[j], a[i]];
  this.pos.set(a[i], i);
  this.pos.set(a[j], j);
}
decreaseKey(item, newPriority) {
  item.priority = newPriority;
  this.#siftUp(this.pos.get(item));
}
```

A simpler trick when you can't track positions: push a new entry and ignore stale ones when you pop them ("lazy deletion").

## 380: What are Fibonacci and pairing heaps?

They're heaps designed for fast "decrease key" and merge. A Fibonacci heap gives amortized O(1) insert, merge and decrease-key, and O(log n) delete-min, which improves Dijkstra in theory. In practice its overhead makes it slower than a binary heap for most real inputs. Pairing heaps are simpler, with very good real-world speed. For JavaScript apps, a binary heap on an array is almost always the right choice.

## 381: Why is union-find "almost" O(1)?

With both path compression and union by rank (or size), any sequence of m operations takes O(m · α(n)), where α is the inverse Ackermann function. α grows so slowly that it's at most 4 for any n you could fit in the universe. With only one of the two tricks, you get O(log n) per operation. That's why union-find is the go-to choice for incremental connectivity questions.

## 382: How can you store a huge graph in typed arrays?

Use Compressed Sparse Row (CSR) format. Give nodes ids 0 to n-1. Store all neighbor lists back to back in one `Int32Array` (`edges`), and keep `offsets`, where node i's neighbors are `edges[offsets[i]]` to `edges[offsets[i + 1] - 1]`. It's very compact, cache-friendly and can be sent to a worker by transfer. Adding edges later is expensive, so build it once from an edge list.

```js
function toCSR(n, edgeList) {
  const offsets = new Int32Array(n + 1);
  for (const [from] of edgeList) offsets[from + 1]++;
  for (let i = 0; i < n; i++) offsets[i + 1] += offsets[i];
  const edges = new Int32Array(edgeList.length);
  const fill = offsets.slice(0, n);
  for (const [from, to] of edgeList) edges[fill[from]++] = to;
  return { offsets, edges };
}
```

Graph visualizations with hundreds of thousands of nodes (like Sigma.js and Cosmograph) store data this way.

## 383: How do bundlers represent the module graph?

Each module is a node with its id (resolved path), source, transformed code, and a list of imports and importers. Edges go both ways: from a module to its dependencies, and back to the modules that import it. The back edges matter for hot module replacement: when a file changes, Vite walks importers upward to find the nearest module that accepts the update. Tree shaking walks the graph to see which exports are used, and code splitting finds groups of modules reachable only from a dynamic `import()`.

## 384: How do you make a trie use less memory?

Use a `Map` or plain object for children instead of a 26-slot array per node when the alphabet is big or sparse. Merge single-child chains (radix tree). Share identical suffixes (DAWG, see question 385). For a static word list, store the whole trie in typed arrays: node arrays of first-child index, sibling index and character code. Each change cuts the cost of millions of small JavaScript objects, which can easily use 50 to 100 bytes each.

## 385: What is a DAWG?

A DAWG (directed acyclic word graph) is a trie where identical subtrees are merged, so words with the same ending share nodes the way words with the same beginning do in a trie. For a big dictionary it can be many times smaller than a trie while still answering "is this a word?" and prefix queries. Building it takes more work (you need to find identical subtrees, usually by hashing them), so it fits fixed word lists shipped with an app, like a spell checker or a word game dictionary.

## 386: What is the Eytzinger layout?

It stores a sorted array in the order of a breadth-first walk of a balanced BST: the root (the median) at index 1, its children at 2 and 3, and so on, like a heap. A binary search then moves from `i` to `2i` or `2i + 1`, and the first few levels sit together in memory, which helps the CPU cache and prefetching. For large static sorted arrays searched very often, it can beat plain binary search. It's a niche trick but a nice example of how memory layout matters.

## 387: How do bitmasks represent small sets?

If items come from a small known list (up to 32 for normal bitwise operators, or more with `BigInt`), each item gets one bit, and a set is just a number. Union is `a | b`, intersection is `a & b`, membership is `(set >> i) & 1`, and the full set is `(1 << n) - 1`. It's fast and works as a `Map` key, so it's common in dynamic programming over subsets ("which cities have I visited?") and permission systems.

```js
const visitedAll = (1 << n) - 1;
const key = (mask, city) => mask * n + city; // memo key for DP over subsets
```

## 388: When does immutable updating become too slow?

Copying an array of n items for every change is O(n). It's fine at a few thousand items, but adding 10,000 items one by one with spread is O(n²), and updating one cell in a 100,000-row grid on every keystroke can drop frames. Signs: GC pauses and long tasks in the Performance panel. Fixes: batch changes into one copy, use structural sharing (Immer only copies changed paths), normalize so updates touch small objects, use persistent structures, or keep that part mutable and use a version counter to trigger renders.

## 389: Should you use Object.freeze in production code?

For constants and config, yes; it catches accidental writes in strict mode. For large state trees updated often, deep freezing every new object costs time, so some libraries only do it in development. Freezing doesn't make reads faster in a meaningful way. Remember that it's shallow, doesn't protect `Map` or `Set` contents, and makes writes throw in strict mode code (all ES modules and classes), so a forgotten mutation shows up as a crash, which is often what you want.

## 390: Without Records and Tuples, how can you get value-based equality for keys?

Turn the value into a canonical primitive key: a string or number built the same way every time. For objects, that means sorting keys before serializing, because `JSON.stringify` keeps insertion order. Another option is interning: keep a `Map` from canonical string to one shared object, so equal values always give the same reference and `===` works.

```js
const pool = new Map();
function intern(point) {
  const key = `${point.x},${point.y}`;
  if (!pool.has(key)) pool.set(key, Object.freeze({ ...point }));
  return pool.get(key);
}
intern({ x: 1, y: 2 }) === intern({ x: 1, y: 2 }); // true
```

The pool keeps every value alive, so pair it with `WeakRef`s or limits if it can grow without bound.

## 391: How would you build a Map that compares keys by content?

Wrap a `Map` and hash each key to a canonical string. Store `[originalKey, value]` so you can still list the real keys.

```js
const canon = (v) =>
  v && typeof v === "object"
    ? Array.isArray(v)
      ? `[${v.map(canon).join(",")}]`
      : `{${Object.keys(v)
          .sort()
          .map((k) => JSON.stringify(k) + ":" + canon(v[k]))
          .join(",")}}`
    : (JSON.stringify(v) ?? String(v));

class ValueMap {
  #m = new Map();
  set(k, v) {
    this.#m.set(canon(k), [k, v]);
    return this;
  }
  get(k) {
    return this.#m.get(canon(k))?.[1];
  }
  has(k) {
    return this.#m.has(canon(k));
  }
  *[Symbol.iterator]() {
    yield* this.#m.values();
  }
}

const m = new ValueMap().set({ b: 2, a: 1 }, "x");
m.get({ a: 1, b: 2 }); // "x"
```

Hashing on every call costs O(size of key), so this is for small keys.

## 392: What goes wrong if you use JSON.stringify as a cache key?

Key order: `{a: 1, b: 2}` and `{b: 2, a: 1}` give different strings. Lost values: `undefined` disappears, `NaN` becomes `null`, so different inputs can share a key. `Map`, `Set` and class instances turn into `{}`. `Date` becomes a string, so a date and its ISO string collide. It throws on `BigInt` and cycles. And it's slow for big objects. It's fine for simple, known shapes like `{ page, sort }`, which is why React Query and SWR hash query keys with sorted object keys.

## 393: How do you write a full deep equality check that handles Map, Set, typed arrays and cycles?

```js
function deepEqual(a, b, seen = new Map()) {
  if (Object.is(a, b)) return true;
  if (typeof a !== "object" || typeof b !== "object" || !a || !b) return false;
  if (Object.getPrototypeOf(a) !== Object.getPrototypeOf(b)) return false;
  if (seen.get(a) === b) return true; // already comparing this pair
  seen.set(a, b);

  if (a instanceof Date) return a.getTime() === b.getTime();
  if (a instanceof RegExp) return a.source === b.source && a.flags === b.flags;
  if (ArrayBuffer.isView(a)) {
    return a.length === b.length && a.every((v, i) => Object.is(v, b[i]));
  }
  if (a instanceof Map) {
    if (a.size !== b.size) return false;
    for (const [k, v] of a)
      if (!b.has(k) || !deepEqual(v, b.get(k), seen)) return false;
    return true;
  }
  if (a instanceof Set) {
    if (a.size !== b.size) return false;
    for (const v of a) if (!b.has(v)) return false;
    return true;
  }
  const ka = Reflect.ownKeys(a),
    kb = Reflect.ownKeys(b);
  if (ka.length !== kb.length) return false;
  return ka.every((k) => Object.hasOwn(b, k) && deepEqual(a[k], b[k], seen));
}
```

Note that `Map` keys and `Set` values are still compared by identity; matching object keys by content would need an O(n²) search. Also, `ArrayBuffer.isView` is true for `DataView` too, which has no `length` or `every`, so a complete version handles it separately.

## 394: How do you deep clone something with cycles and special types by hand?

Keep a `WeakMap` from each original object to its copy. Before copying an object, check the map; if it's there, return the existing copy. Register the copy before copying its children so cycles point to it.

```js
function clone(value, seen = new WeakMap()) {
  if (value === null || typeof value !== "object") return value;
  if (seen.has(value)) return seen.get(value);

  if (value instanceof Date) return new Date(value);
  if (value instanceof RegExp) return new RegExp(value.source, value.flags);

  let copy;
  if (value instanceof Map) {
    copy = new Map();
    seen.set(value, copy);
    for (const [k, v] of value) copy.set(clone(k, seen), clone(v, seen));
    return copy;
  }
  if (value instanceof Set) {
    copy = new Set();
    seen.set(value, copy);
    for (const v of value) copy.add(clone(v, seen));
    return copy;
  }
  copy = Array.isArray(value)
    ? []
    : Object.create(Object.getPrototypeOf(value));
  seen.set(value, copy);
  for (const key of Reflect.ownKeys(value)) copy[key] = clone(value[key], seen);
  return copy;
}
```

Unlike `structuredClone`, this keeps prototypes and symbol keys, but it doesn't copy private fields or internal slots of built-ins it doesn't know.

## 395: How do you serialize and restore class instances?

`JSON.stringify` calls `toJSON()` if it exists, so a class can write a type tag plus its data. On the way back, a reviver looks at the tag and calls a static `fromJSON`. Keep a registry from tag to class, never `eval` or look up constructors by user-provided names on `window`.

```js
class Money {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }
  toJSON() {
    return { $type: "Money", amount: this.amount, currency: this.currency };
  }
  static fromJSON(o) {
    return new Money(o.amount, o.currency);
  }
}

const registry = { Money };
const revive = (k, v) =>
  v?.$type && registry[v.$type] ? registry[v.$type].fromJSON(v) : v;

const back = JSON.parse(JSON.stringify({ price: new Money(5, "EUR") }), revive);
back.price instanceof Money; // true
```

Libraries like `superjson` and `devalue` do this for `Date`, `Map`, `Set`, `BigInt` and more.

## 396: When would you use a binary format like MessagePack or Protocol Buffers instead of JSON?

When payloads are large or frequent: real-time games, trading dashboards, telemetry, big lists over WebSockets. Binary formats are smaller (numbers aren't text, keys can be numeric field ids in protobuf) and can be faster to parse for numeric data. Protobuf also gives a schema, so both sides agree on types. JSON wins on simplicity, debugging, browser support with no extra code and very fast native `JSON.parse`. Try compressing JSON with gzip or brotli first; it often closes most of the size gap.

## 397: How do you handle a JSON response too large to parse at once?

`JSON.parse` needs the whole string in memory and blocks the main thread while it runs. Options: ask the API to paginate; switch to NDJSON (one JSON object per line) and parse each line as it arrives from `response.body`; use a streaming parser; or do the parse in a Web Worker so the UI stays responsive. Transferring the result back still costs a structured clone, so send back only what the UI needs.

```js
const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
let buffer = "";
while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  buffer += value;
  const lines = buffer.split("\n");
  buffer = lines.pop();
  for (const line of lines) if (line) handle(JSON.parse(line));
}
if (buffer) handle(JSON.parse(buffer));
```

## 398: How is data organized in IndexedDB?

A database holds object stores (like tables). Each store keeps records sorted by a primary key, which can be a number, string, date, binary, or array of those. Indexes are extra sorted structures on a field of the stored objects, including multi-entry indexes over arrays (like tags). Queries are by exact key or by `IDBKeyRange` (between, above, below), and cursors walk records in key order. There's no full query language, so you design keys and indexes around the queries you need, like with a key-value store.

```js
const store = db.createObjectStore("messages", { keyPath: "id" });
store.createIndex("byConversationTime", ["conversationId", "sentAt"]);
// later: index.getAll(IDBKeyRange.bound([convId, 0], [convId, Infinity]))
```

## 399: What should you keep in mind when saving data structures to localStorage?

It only stores strings, so you need to serialize (and revive `Map`, `Set`, `Date`). It's synchronous and blocks the main thread, so big writes on every change cause jank. Limits are around 5 MB per origin. Data is shared between tabs; listen to the `storage` event to sync. Version the stored shape so you can migrate after you change the structure. For large or structured data, IndexedDB is the better fit.

## 400: What does it cost to send a large data structure to a Web Worker?

`postMessage` structured-clones the data: it walks the whole object graph and copies it, which takes time on the sending thread and doubles memory until one side drops its copy. For a big object tree this can block for tens or hundreds of milliseconds. Ways to reduce it: send typed arrays and transfer their buffers (no copy), send only the changes, keep the data in the worker and send results back, or use `SharedArrayBuffer` for numeric data both sides need.

## 401: How do you pass a large dataset to a worker without copying?

Put it in an `ArrayBuffer` (numbers in typed arrays, strings encoded with `TextEncoder`) and list the buffer in the transfer list. The memory moves to the worker almost instantly, and the sender's buffer becomes detached.

```js
const points = new Float64Array(2_000_000);
worker.postMessage({ points }, [points.buffer]);
points.length; // 0, ownership moved
```

The worker can send it back the same way when it's done, so you can ping-pong one buffer without allocating.

## 402: How can you measure how much memory your data structures use?

In DevTools, heap snapshots show "shallow size" (the object itself) and "retained size" (everything that would be freed if it were gone). Sort by retained size to find the biggest structures. In code, `performance.memory` is non-standard and Chrome-only; `performance.measureUserAgentSpecificMemory()` is the newer API, but it needs a cross-origin isolated page and is only in Chromium-based browsers. For quick experiments in Node.js, use `process.memoryUsage().heapUsed` before and after building a structure, with `--expose-gc` to force collection first.

## 403: What is the difference between shallow size and retained size?

Shallow size is the memory used by the object itself: its header and property slots, not the things it points to. Retained size is the memory that would be freed if this object were deleted, including everything only reachable through it. A `Map` with a shallow size of a few kilobytes can retain hundreds of megabytes of cached objects. When hunting leaks, look for objects with large retained size and follow their retainer chains.

## 404: How can a data structure keep detached DOM nodes alive?

If an array, `Map` or `Set` holds a DOM element after it's removed from the page, the element and its whole subtree (plus their event listeners and anything those closures capture) stay in memory. Common examples: a list of rendered rows in a custom virtual list, a cache from id to element, or a listener registry. In heap snapshots, search for "Detached" to find them. Fixes: use a `WeakMap` or `WeakRef` for element references, and clean up on unmount or `disconnectedCallback`.

## 405: How do closures accidentally keep big data structures in memory?

A closure keeps every variable it uses from its outer scope. In V8, closures created in the same scope share one context object, so if one closure uses a big array, another long-lived closure from the same scope (like an event handler) can keep that array alive even though it never reads it. Fixes: move the big data out of the scope of long-lived callbacks, set it to `null` when done, or pull the callback into a separate function that only gets what it needs.

```js
function setup() {
  const huge = new Array(1e6).fill("x");
  const summary = huge.length; // keep only what you need
  button.onclick = () => console.log(summary);
}
```

## 406: How does laziness in iterator helpers work with infinite sequences?

Each helper wraps the previous iterator and pulls one value at a time. `take(n)` stops pulling after n values and calls `return()` on the source, so a generator's `finally` block runs. `filter` on an infinite source with no matches never finishes, and `toArray` or `reduce` on an infinite iterator without `take` never returns. Also, iterators are single-use: once consumed, they're done, unlike arrays.

```js
function* ids() {
  try {
    let i = 0;
    while (true) yield i++;
  } finally {
    console.log("cleanup");
  }
}
ids()
  .map((x) => x * 2)
  .take(2)
  .toArray(); // [0, 2], then logs "cleanup"
```

## 407: When should a data pipeline use generators instead of arrays?

When the data is big or comes in over time, and each step only needs one item at a time: parsing log lines, walking a huge tree, reading paginated APIs, streaming CSV rows. Generators use memory for one item instead of the whole dataset at each step, and they can stop early. Arrays are faster for small to medium data you'll loop over several times, and give you sorting, random access and `length`. Sorting or grouping always needs the full data, so it breaks laziness.

## 408: How do streams use queues for backpressure?

Each `ReadableStream` and `WritableStream` has an internal queue with a high water mark set by its queuing strategy. When the queue is above that mark, `desiredSize` goes to zero or below, the stream stops calling `pull()` on the source, and `pipeTo` waits before reading more. That way a fast producer can't fill memory faster than a slow consumer handles it. You choose `CountQueuingStrategy` (number of chunks) or `ByteLengthQueuingStrategy` (bytes) depending on what you want to limit.

```js
const stream = new ReadableStream(
  {
    async pull(controller) {
      controller.enqueue(await fetchNextChunk());
    },
  },
  new CountQueuingStrategy({ highWaterMark: 4 }),
);
```

## 409: How do you build an async queue that producers push to and consumers await?

Keep two queues: values waiting for a consumer and consumers waiting for a value. Whichever side arrives first waits in its queue. Making it async iterable gives you `for await` on top.

```js
class AsyncQueue {
  #values = [];
  #waiters = [];

  push(value) {
    const waiter = this.#waiters.shift();
    if (waiter) waiter(value);
    else this.#values.push(value);
  }
  next() {
    if (this.#values.length) return Promise.resolve(this.#values.shift());
    return new Promise((resolve) => this.#waiters.push(resolve));
  }
  async *[Symbol.asyncIterator]() {
    while (true) yield await this.next();
  }
}

const q = new AsyncQueue();
(async () => {
  for await (const msg of q) console.log(msg);
})();
q.push("hello");
```

A production version adds `close()`, error handling, and a size limit with backpressure, and replaces `shift()` with a real queue.

## 410: What happens if you modify a Map or Set while iterating over it?

The spec defines it: an entry deleted before being reached is skipped, an entry added during iteration will be visited, and an existing key that's updated keeps its place. So deleting during iteration is safe. Adding during iteration can loop forever, for example `for (const x of s) s.add(x + 1)`. Deleting and re-adding the same key moves it to the end, so it can be visited twice. If you need to change the collection a lot, iterate over a copy: `for (const x of [...s])`.

## 411: What happens if you modify an array while using forEach or map?

These methods read `length` once at the start, then read each index when they get to it. Items you push during the loop aren't visited. Items you change ahead of the current index are seen with the new value. Removing items shifts the rest, so the loop skips the item that moved into the current slot. The safe pattern is to build a new array with `filter` or `map`, or loop backward when removing in place.

```js
const arr = [1, 2, 3, 4];
arr.forEach((x, i) => {
  if (x % 2 === 0) arr.splice(i, 1);
});
// arr is [1, 3], but only by luck; [2, 4, 6] would leave [4]
```

## 412: What does the spec guarantee about sort stability and compare functions?

Since ES2019, `Array.prototype.sort` and `toSorted` must be stable: equal items keep their relative order. That lets you sort by several keys by doing several sorts, least important first. The compare function must be consistent: return a negative number, zero or a positive number, give the same answer for the same pair every time, and be transitive. A compare function like `() => Math.random() - 0.5` or one that returns booleans breaks this, and the result is "implementation-defined", meaning it can be different in each browser. `undefined` items always go to the end without calling the compare function.

## 413: How should you sort strings for users?

Default `sort()` compares UTF-16 code units, so "Z" comes before "a" and "é" ends up after "z". Use `localeCompare` or, for many comparisons, an `Intl.Collator`, which is much faster when reused. Collator options handle case, accents and numbers inside strings.

```js
const collator = new Intl.Collator("en", {
  numeric: true,
  sensitivity: "base",
});
["item10", "Item2", "item1"].toSorted(collator.compare);
// ["item1", "Item2", "item10"]
```

## 414: When is an array index really an index?

Only keys that are canonical string forms of integers from 0 to 2³² − 2 are array indexes. `arr["1"]` is index 1, but `arr["01"]`, `arr["-1"]`, `arr["1.5"]` and `arr[4294967295]` are just normal properties: they don't change `length` and aren't visited by `forEach` or `map`. That's why `arr[-1]` doesn't read the last item in JavaScript, and why `at(-1)` was added.

```js
const a = [];
a[-1] = "x";
a.length; // 0
Object.keys(a); // ["-1"]
```

## 415: Why are +0 and -0 the same key in a Map?

`Map` and `Set` use SameValueZero, and the spec also turns a `-0` key into `+0` when you add it. So `map.set(-0, "x")` stores the key as `+0`, and both `get(0)` and `get(-0)` find it, and listing the keys gives `0`. Usually that's what you want, but if your code needs to tell them apart (rare: some math or graphics code), you have to encode the sign yourself, for example with `Object.is(x, -0)` before storing.

## 416: How do different array methods treat NaN?

Methods that use `===` can't find `NaN`: `indexOf`, `lastIndexOf`. Methods that use SameValueZero can: `includes`, and `Map`/`Set` lookups. Methods with your own callback depend on your check: `findIndex(Number.isNaN)` works. This is a common interview trick and a real source of bugs when cleaning data.

```js
const vals = [1, NaN];
vals.indexOf(NaN); // -1
vals.includes(NaN); // true
vals.findIndex(Number.isNaN); // 1
new Set([NaN, NaN]).size; // 1
```

## 417: What is Symbol.species, and why is it a problem when you subclass Array?

When you call `map`, `filter` or `slice` on an `Array` subclass, the result is created using `this.constructor[Symbol.species]`, which is your subclass by default. That means your constructor runs with arguments you didn't plan for (like the new length), which can break subclasses with custom constructors. You can set `static get [Symbol.species]() { return Array; }` to return plain arrays. There have been proposals to remove species because it complicates engines and caused security bugs, so newer methods like `toSorted` and `with` always return plain arrays and ignore it.

## 418: How do you safely extend Map or Set?

Subclassing works (`class DefaultMap extends Map`), but be careful: the `Map` constructor calls `this.set` for each initial entry, so your overridden `set` runs before your own constructor body finishes. Using composition (a class that holds a private `Map`) avoids this and lets you control the API.

```js
class DefaultMap extends Map {
  #make;
  constructor(make, entries) {
    super(entries); // runs this.set for each entry before #make is set
    this.#make = make;
  }
  get(key) {
    if (!this.has(key)) this.set(key, this.#make(key));
    return super.get(key);
  }
}

const groups = new DefaultMap(() => []);
groups.get("a").push(1);
```

## 419: How can a Proxy add negative indexing to arrays?

Intercept `get` and `set`, turn negative integer keys into positive indexes, and forward everything else.

```js
function withNegative(arr) {
  const fix = (target, key) => {
    if (typeof key === "string" && /^-\d+$/.test(key))
      return String(target.length + Number(key));
    return key;
  };
  return new Proxy(arr, {
    get: (t, k, r) => Reflect.get(t, fix(t, k), r),
    set: (t, k, v, r) => Reflect.set(t, fix(t, k), v, r),
  });
}

const a = withNegative([1, 2, 3]);
a[-1]; // 3
```

It's a fun trick, but proxies make every access slower and confuse some tools, so in real code just use `at()`.

## 420: What makes arrays "exotic objects" in the spec?

Normal objects store properties with no special rules. Arrays have a special `[[DefineOwnProperty]]`: writing an index at or beyond `length` makes `length` grow, and writing a smaller `length` deletes the extra indexes. That behavior can't be copied with normal getters and setters, which is why it's called exotic. Other exotic objects include typed arrays (indexes are always in range and numeric), `String` objects, `arguments` and `Proxy`.

## 421: How do getters in data structures interact with JSON and copying?

`JSON.stringify` calls getters and writes their current values, and spread and `Object.assign` also read getters and copy the values as plain properties. Getters defined on a class prototype (like `get size()`) aren't own properties, so they're skipped by `JSON.stringify`, spread and `Object.keys`. So a class with private fields and getters often serializes to `{}`. Add a `toJSON()` method to control what gets written.

```js
class Cart {
  #items = [1, 2];
  get count() {
    return this.#items.length;
  }
  toJSON() {
    return { items: this.#items };
  }
}
JSON.stringify(new Cart()); // '{"items":[1,2]}'
```

## 422: Why does Object.groupBy return an object with a null prototype?

So that group names can't clash with inherited properties. If you group by a user-provided field and one value is `"constructor"` or `"toString"`, a normal object would already have those keys from its prototype, and `result.toString` would return a function instead of `undefined` when no group exists. The trade-off: `result.hasOwnProperty(...)` doesn't exist, and some old tools print it oddly. Use `Object.hasOwn` and `Object.keys` with it.

## 423: How does Map.groupBy decide which items share a group?

It compares keys with SameValueZero, the same rule `Map` uses. Primitives group by value; `NaN` groups with `NaN`; `0` and `-0` group together; objects only group together when the callback returns the exact same object. A common bug is returning a new object or array from the callback, like `item => [item.year, item.month]`, which puts every item in its own group. Return a primitive, like a string `"2026-10"`, when you need a composite key.

## 424: How is sort() on a typed array different from sort() on an array?

Typed arrays sort numerically by default, so `new Int32Array([10, 1, 2]).sort()` gives `[1, 2, 10]`. Normal arrays sort as strings by default. Typed arrays also have `toSorted`, `toReversed` and `with`, which return a new typed array of the same type. Typed array sort is usually much faster than an array sort with a compare function, because the engine knows every item is a number of one type.

```js
new Float64Array([3.5, -1, 2]).sort(); // Float64Array [-1, 2, 3.5]
[10, -1, 2].sort(); // [-1, 10, 2], compared as strings
```

Note that NaN goes to the end of a typed array sort.

## 425: How do you parse a binary format like a PNG header in JavaScript?

Read the file as an `ArrayBuffer`, then use `DataView` for multi-byte numbers with the right endianness (PNG uses big-endian) and `Uint8Array` for raw bytes.

```js
async function pngSize(file) {
  const buf = await file.slice(0, 24).arrayBuffer();
  const bytes = new Uint8Array(buf);
  const sig = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  if (!sig.every((b, i) => bytes[i] === b)) throw new Error("Not a PNG");
  const view = new DataView(buf);
  return { width: view.getUint32(16), height: view.getUint32(20) }; // IHDR, big-endian
}
```

Reading only the first 24 bytes with `slice` keeps it fast even for huge files.

## 426: Why does endianness matter when you share typed arrays across systems?

Typed arrays use the byte order of the machine, which is little-endian on almost every device today. If you send raw bytes from a `Uint32Array` to a server or file format that expects big-endian (network byte order, many file formats), the numbers come out wrong. `DataView` takes an explicit `littleEndian` flag, so it gives the same result on any machine. Rule of thumb: typed arrays for in-memory work, `DataView` for reading and writing formats.

## 427: How do you pack many booleans into a small amount of memory?

Use one bit per boolean in a `Uint8Array` or `Uint32Array` (see the bitset in question 221). For one million flags, that's 125 KB instead of about 8 MB for an array of booleans or much more for a `Set`. You can count set bits quickly by checking 32 at a time. Use cases: "seen" flags for millions of ids, seat maps, pixel masks, and feature flags per user stored compactly.

```js
function popcount32(x) {
  x -= (x >>> 1) & 0x55555555;
  x = (x & 0x33333333) + ((x >>> 2) & 0x33333333);
  return (((x + (x >>> 4)) & 0x0f0f0f0f) * 0x01010101) >>> 24;
}
```

## 428: How would you store millions of numeric ids for fast membership checks?

A `Set` of millions of numbers works but can use hundreds of megabytes and takes time to build. A sorted `Uint32Array` with binary search uses 4 bytes per id and gives O(log n) lookups; build it once and transfer it to a worker if needed. If ids are dense within a range, a bitset is even smaller and O(1). If ids are huge and sparse, or you need fast unions and intersections, a compressed bitmap like Roaring is the best fit.

```js
function hasId(sorted, id) {
  let lo = 0,
    hi = sorted.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    if (sorted[mid] === id) return true;
    if (sorted[mid] < id) lo = mid + 1;
    else hi = mid - 1;
  }
  return false;
}
```

## 429: What are Roaring bitmaps?

Roaring bitmaps split 32-bit integers into chunks by their high 16 bits. Each chunk is stored in the best format for its data: a sorted array of 16-bit values when sparse, an 8 KB bitset when dense, or a list of runs when values are consecutive. Set operations like union and intersection run chunk by chunk and are very fast. Search engines, analytics databases and tools like Elasticsearch and Apache Druid use them. In JavaScript, there are packages such as `roaring` (Node.js) and WebAssembly builds for the browser.

## 430: How do you choose between sparse and dense representations?

Dense (arrays, typed arrays, bitsets, matrices) stores every possible position: fast O(1) access, compact when most positions are used, but wasteful when most are empty. Sparse (`Map` of position to value, coordinate lists, adjacency lists) stores only what exists: compact for mostly-empty data but with more overhead per entry and slower access. A rough rule: if more than about 10 to 30 percent of positions are filled, dense is usually better. Spreadsheets, graphs, game maps and huge feature vectors all face this choice.

## 431: Design a structure with O(1) insert, delete and getRandom.

Keep values in an array (for random access) and a `Map` from value to its index. To delete, swap the value with the last item, update that item's index in the map, then pop.

```js
class RandomizedSet {
  #items = [];
  #index = new Map();

  insert(v) {
    if (this.#index.has(v)) return false;
    this.#index.set(v, this.#items.length);
    this.#items.push(v);
    return true;
  }
  remove(v) {
    const i = this.#index.get(v);
    if (i === undefined) return false;
    const last = this.#items.pop();
    if (i < this.#items.length) {
      this.#items[i] = last;
      this.#index.set(last, i);
    }
    this.#index.delete(v);
    return true;
  }
  getRandom() {
    return this.#items[Math.floor(Math.random() * this.#items.length)];
  }
}
```

## 432: Design a time-based key-value store where get(key, time) returns the value at that time.

For each key, keep an array of `[time, value]` pairs. If writes come in time order, the array stays sorted, so `get` uses binary search to find the last entry with time ≤ the requested time.

```js
class TimeMap {
  #data = new Map();

  set(key, value, time) {
    if (!this.#data.has(key)) this.#data.set(key, []);
    this.#data.get(key).push([time, value]); // assumes increasing time
  }
  get(key, time) {
    const list = this.#data.get(key) ?? [];
    let lo = 0,
      hi = list.length - 1,
      ans = undefined;
    while (lo <= hi) {
      const mid = (lo + hi) >> 1;
      if (list[mid][0] <= time) {
        ans = list[mid][1];
        lo = mid + 1;
      } else hi = mid - 1;
    }
    return ans;
  }
}
```

This is how feature-flag history, document version lookups and "state at time t" debugging tools work.

## 433: Design a snapshot array: set(index, value), snap() and get(index, snapId).

Copying the whole array on each `snap` is O(n) per snapshot. Instead, store for each index a list of `[snapId, value]` changes. `snap()` just increments a counter. `get` binary searches that index's list for the last change at or before `snapId`. Memory grows with the number of changes, not with snapshots times size. It's the same idea as multi-version storage in databases.

```js
class SnapshotArray {
  #history;
  #snap = 0;
  constructor(n) {
    this.#history = Array.from({ length: n }, () => [[0, 0]]);
  }

  set(i, v) {
    const h = this.#history[i];
    if (h.at(-1)[0] === this.#snap) h.at(-1)[1] = v;
    else h.push([this.#snap, v]);
  }
  snap() {
    return this.#snap++;
  }
  get(i, id) {
    const h = this.#history[i];
    let lo = 0,
      hi = h.length - 1;
    while (lo < hi) {
      const mid = (lo + hi + 1) >> 1;
      if (h[mid][0] <= id) lo = mid;
      else hi = mid - 1;
    }
    return h[lo][1];
  }
}
```

## 434: Design a hit counter that returns hits in the last 5 minutes.

Use a ring buffer with one slot per second (300 slots). Each slot stores the timestamp it belongs to and a count. On a hit, if the slot's timestamp is old, reset it. To count, sum the slots whose timestamp is within the window. Memory is fixed and both operations are O(300), which is constant.

```js
class HitCounter {
  #times = new Int32Array(300);
  #counts = new Int32Array(300);

  hit(t) {
    // t in seconds
    const i = t % 300;
    if (this.#times[i] !== t) {
      this.#times[i] = t;
      this.#counts[i] = 0;
    }
    this.#counts[i]++;
  }
  getHits(t) {
    let total = 0;
    for (let i = 0; i < 300; i++)
      if (t - this.#times[i] < 300) total += this.#counts[i];
    return total;
  }
}
```

A queue of timestamps is simpler but grows with traffic; the buckets version doesn't.

## 435: Design a leaderboard that supports updating scores and getting the top k.

Keep a `Map` from player to score for O(1) updates. For top k: if k is small and reads are rare, scan with a small heap (O(n log k)). If reads are frequent, keep players in a sorted structure (balanced BST, skip list, or a sorted array with binary search re-insertion) so top k is O(k) and an update is a remove plus insert. Redis sorted sets, built on skip lists, are the standard back-end tool for this; on the front end you usually only show the top part the server sends.

## 436: Design an in-memory file system with mkdir, ls, addContent and readContent.

Model it as a tree: directories have a `Map` of children, files have a content string. Every operation splits the path and walks from the root. `ls` on a directory returns sorted child names; on a file it returns the file name.

```js
class FileSystem {
  #root = { children: new Map() };

  #walk(path, create) {
    let node = this.#root;
    for (const part of path.split("/").filter(Boolean)) {
      if (!node.children.has(part)) {
        if (!create) return null;
        node.children.set(part, { children: new Map() });
      }
      node = node.children.get(part);
    }
    return node;
  }
  mkdir(path) {
    this.#walk(path, true);
  }
  addContent(path, text) {
    const node = this.#walk(path, true);
    node.content = (node.content ?? "") + text;
  }
  readContent(path) {
    return this.#walk(path, false)?.content ?? "";
  }
  ls(path) {
    const node = this.#walk(path, false);
    if (!node) return [];
    if (node.content !== undefined) return [path.split("/").at(-1)];
    return [...node.children.keys()].sort();
  }
}
```

## 437: Design an MRU tab switcher like Ctrl+Tab in a browser or editor.

Keep tabs in most-recently-used order. A `Map` from tab id to tab works because of insertion order: when a tab is focused, `delete` and `set` it to move it to the end, so the end is the most recent. Opening the switcher reads the keys in reverse. While the user is still holding Ctrl and cycling, don't reorder; only commit the move when they release, so repeated Tab presses walk through the list instead of swapping the top two.

## 438: Design an LFU cache with O(1) operations.

Keep three things: a `Map` from key to `{ value, freq }`, a `Map` from frequency to an ordered set of keys (a `Set` keeps insertion order, so the first key is the least recent at that frequency), and the current minimum frequency. On access, move the key from its frequency bucket to `freq + 1`, and bump `minFreq` if its old bucket is now empty. To evict, take the first key from the `minFreq` bucket. New keys start at frequency 1, so `minFreq` resets to 1.

```js
class LFUCache {
  #vals = new Map();
  #buckets = new Map();
  #min = 0;
  constructor(cap) {
    this.cap = cap;
  }

  #touch(key) {
    const e = this.#vals.get(key);
    const b = this.#buckets.get(e.freq);
    b.delete(key);
    if (b.size === 0) {
      this.#buckets.delete(e.freq);
      if (this.#min === e.freq) this.#min++;
    }
    e.freq++;
    if (!this.#buckets.has(e.freq)) this.#buckets.set(e.freq, new Set());
    this.#buckets.get(e.freq).add(key);
  }
  get(key) {
    if (!this.#vals.has(key)) return undefined;
    this.#touch(key);
    return this.#vals.get(key).value;
  }
  set(key, value) {
    if (this.cap === 0) return;
    if (this.#vals.has(key)) {
      this.#vals.get(key).value = value;
      this.#touch(key);
      return;
    }
    if (this.#vals.size >= this.cap) {
      const b = this.#buckets.get(this.#min);
      const old = b.keys().next().value;
      b.delete(old);
      if (b.size === 0) this.#buckets.delete(this.#min);
      this.#vals.delete(old);
    }
    this.#vals.set(key, { value, freq: 1 });
    if (!this.#buckets.has(1)) this.#buckets.set(1, new Set());
    this.#buckets.get(1).add(key);
    this.#min = 1;
  }
}
```

## 439: How can an event log be the main data structure of a front-end app?

In event sourcing, you store an append-only list of events ("item added", "price changed") and compute the current state by replaying them through a reducer. Redux is close to this: actions are events, and DevTools can replay them. Benefits: full history, easy undo and time travel, syncing by sending events, and debugging by replaying a user's session. Costs: the log grows, so you take periodic snapshots and replay only events after the latest one, and changing event shapes needs versioning.

## 440: How do you store item order so several users can reorder a list without conflicts?

Storing an integer position means one move can change many rows, and two users moving at once overwrite each other. Fractional indexing gives each item a sortable key, and a moved item gets a new key between its neighbors (between "a" and "b" you can pick "an"), so only one row changes. Libraries like `fractional-indexing` generate string keys that never run out of room between two values. Ties from two users inserting at the same spot are broken by adding a random or user-based suffix.

## 441: Why can't you diff two trees in linear time in general, and how do frameworks get around it?

The minimum tree edit distance between two ordered trees takes about O(n³) with the best general algorithms, which is far too slow for a UI with thousands of nodes on every update. Frameworks give up on the minimum and use assumptions: compare only nodes at the same level and position, treat a different type as a full replacement, and use keys to match moved children. These rules give O(n) diffs that are almost always good enough, and when they're not (like moving a subtree to a new parent), the framework re-creates it.

## 442: What is a Merkle tree, and how could a front-end app use the idea?

A Merkle tree stores a hash for every leaf, and each parent stores the hash of its children's hashes. Two copies with the same root hash are identical; if roots differ, you compare child hashes and only go down into the branches that differ, finding changes in O(log n) steps instead of comparing everything. Git, IPFS, blockchains and sync systems use it. In a client app, it can speed up syncing a large local dataset with the server: exchange hashes level by level and only download the changed chunks.

## 443: What is content-addressed storage, and why does it help caching?

Data is stored under the hash of its content instead of a name. The same content always gets the same key, so duplicates are stored once, and a key's content can never change, so caches can keep it forever. Build tools use this for output file names (`app.3f9a1c.js`) so browsers can cache them for a year, and package managers like pnpm store each file once by hash. For data structures, it means immutable, shareable pieces that are trivially safe to cache.

## 444: How do you avoid misleading microbenchmarks when comparing data structures?

Engines optimize based on how code runs, so tiny benchmarks often measure the wrong thing: the JIT may remove work whose result isn't used, warmed-up code is much faster than cold code, and a test with one key type can produce different shapes than real data. Use realistic sizes and data, use the result (for example, sum it and print it), run enough iterations to warm up, run in the target browser, and compare with a profiler in the real app. A `Map` vs object result from a 1,000-key test may flip at 1,000,000 keys.

## 445: A chart needs to show 1 million points and stay smooth. What data structures would you use?

Store the points as typed arrays (struct of arrays: `Float64Array` for x, `Float32Array` for y) instead of a million objects; it cuts memory by many times and GC pauses disappear. Since x is usually sorted, find the visible range with binary search. Downsample per pixel column (min and max per bucket, or the LTTB algorithm) so you only draw a few thousand points. Use a k-d tree or a grid for hover lookups. Do the heavy work in a worker with transferred buffers, and draw with canvas or WebGL instead of SVG nodes.

## 446: How would you filter 50,000 products by many facets (brand, color, size, price) instantly?

Precompute, for each facet value, the set of matching product indexes, stored as a bitset (`Uint32Array`) of 50,000 bits, about 6 KB each. A filter like "brand A or B, and color red" becomes bitwise OR within a facet and AND across facets, done 32 products at a time. Counts for each option ("Red (124)") come from popcount of the AND with the current result. Price ranges use the products sorted by price plus binary search to build a bitset. All of this takes milliseconds and can run in a worker.

## 447: What is an inverted index, and how would you build one for client-side search?

An inverted index maps each word to the list of documents that contain it, like the index at the back of a book. To build it, split each document into words (lowercase them, remove accents with `normalize("NFD")`, maybe stem them), and add the document id to each word's list. To search, look up each query word and intersect the lists, then rank by how often and where the words appear. Prefix search adds a sorted word list or a trie over the index keys. Libraries like MiniSearch, Lunr and FlexSearch do this in the browser.

```js
const index = new Map();
docs.forEach((doc, id) => {
  for (const word of new Set(doc.text.toLowerCase().match(/\p{L}+/gu) ?? [])) {
    if (!index.has(word)) index.set(word, new Set());
    index.get(word).add(id);
  }
});
const search = (q) =>
  q
    .toLowerCase()
    .split(/\s+/)
    .map((w) => index.get(w) ?? new Set())
    .reduce((a, b) => a.intersection(b));
```

## 448: How would you keep a large live-updating table (prices, statuses) fast?

Store rows in a `Map` from id to a mutable row object, and send updates as small patches. Keep the sorted order as an array of ids, and when one value changes, move only that id with a binary search insert instead of re-sorting. Batch updates per animation frame so a burst of 500 updates causes one render. Only render visible rows (virtualization), and let each row subscribe to its own id so an update re-renders one row, not the table. If updates are numeric and huge in number, typed arrays per column work even better.

## 449: How do you explain data structure trade-offs in an interview?

Start from the operations and their frequency ("we read by id much more than we insert"), then the size of the data, then memory limits. Name the structure, the complexity of the key operations, and what you give up. For example: "A Map for O(1) lookups by id, plus an array of ids for order, because we reorder often and render in order; the cost is keeping the two in sync." Mention what you'd change if the numbers changed, like moving to typed arrays at a million items. Interviewers care more about this reasoning than about the perfect answer.

## 450: What is the most common data structure mistake in front-end code, in your experience?

Using the wrong lookup structure in a hot path: calling `find`, `includes` or `filter` on arrays inside loops or inside render, which quietly turns O(n) work into O(n²) as data grows. The fix is usually small: build a `Map` or `Set` once (and memoize it), then do O(1) lookups. Close second: mutating arrays or objects that a UI library expects to be replaced, which causes missing updates. Both are cheap to fix once you know to look for them.
