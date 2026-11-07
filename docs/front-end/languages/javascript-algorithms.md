# JavaScript Algorithms Interview Questions and Answers

_Last updated: October 28, 2026_

450 interview questions about algorithms in JavaScript, split into three levels: 150 easy, 150 moderate and 150 advanced. The code uses modern JavaScript (ES2023 and newer), including `Map`, `Set`, `toSorted()`, `findLast()`, `Object.groupBy()`, the new `Set` methods and iterator helpers. Most questions are the kind you get in coding rounds, but there are also questions about how algorithms show up in real front-end work: lists, search, DOM trees, async tasks and keeping the UI fast.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is an algorithm?](#1-what-is-an-algorithm)
- [2: Why should a front-end developer care about algorithms?](#2-why-should-a-front-end-developer-care-about-algorithms)
- [3: What is Big O notation?](#3-what-is-big-o-notation)
- [4: What is the difference between time complexity and space complexity?](#4-what-is-the-difference-between-time-complexity-and-space-complexity)
- [5: What does O(1) mean? Give an example.](#5-what-does-o1-mean-give-an-example)
- [6: What does O(n) mean? Give an example.](#6-what-does-on-mean-give-an-example)
- [7: What does O(n²) mean? Give an example.](#7-what-does-on²-mean-give-an-example)
- [8: What does O(log n) mean?](#8-what-does-olog-n-mean)
- [9: What does O(n log n) mean?](#9-what-does-on-log-n-mean)
- [10: What is exponential time, O(2ⁿ)?](#10-what-is-exponential-time-o2ⁿ)
- [11: What are best case, average case and worst case?](#11-what-are-best-case-average-case-and-worst-case)
- [12: Why do we drop constants and smaller terms in Big O?](#12-why-do-we-drop-constants-and-smaller-terms-in-big-o)
- [13: What is the time complexity of accessing an array element by index?](#13-what-is-the-time-complexity-of-accessing-an-array-element-by-index)
- [14: What is the complexity of push, pop, shift and unshift?](#14-what-is-the-complexity-of-push-pop-shift-and-unshift)
- [15: What is the complexity of includes, indexOf and find?](#15-what-is-the-complexity-of-includes-indexof-and-find)
- [16: Why is Set.has faster than Array.includes for lookups?](#16-why-is-sethas-faster-than-arrayincludes-for-lookups)
- [17: What is the complexity of reading a key from an object or a Map?](#17-what-is-the-complexity-of-reading-a-key-from-an-object-or-a-map)
- [18: Is building a string with += inside a loop slow in JavaScript?](#18-is-building-a-string-with--inside-a-loop-slow-in-javascript)
- [19: How do you reverse a string?](#19-how-do-you-reverse-a-string)
- [20: How do you check if a string is a palindrome?](#20-how-do-you-check-if-a-string-is-a-palindrome)
- [21: How do you count the vowels in a string?](#21-how-do-you-count-the-vowels-in-a-string)
- [22: How do you find the largest number in an array?](#22-how-do-you-find-the-largest-number-in-an-array)
- [23: How do you find both the min and the max in one pass?](#23-how-do-you-find-both-the-min-and-the-max-in-one-pass)
- [24: How do you sum the numbers in an array?](#24-how-do-you-sum-the-numbers-in-an-array)
- [25: How do you calculate the average of an array?](#25-how-do-you-calculate-the-average-of-an-array)
- [26: How do you remove duplicates from an array?](#26-how-do-you-remove-duplicates-from-an-array)
- [27: How do you count how many times each element appears?](#27-how-do-you-count-how-many-times-each-element-appears)
- [28: What is linear search?](#28-what-is-linear-search)
- [29: What is binary search and how do you write it?](#29-what-is-binary-search-and-how-do-you-write-it)
- [30: What does binary search require, and what happens if you ignore it?](#30-what-does-binary-search-require-and-what-happens-if-you-ignore-it)
- [31: How do you solve FizzBuzz?](#31-how-do-you-solve-fizzbuzz)
- [32: How do you calculate a factorial?](#32-how-do-you-calculate-a-factorial)
- [33: How do you write Fibonacci recursively?](#33-how-do-you-write-fibonacci-recursively)
- [34: Why is the naive recursive Fibonacci slow?](#34-why-is-the-naive-recursive-fibonacci-slow)
- [35: How do you write Fibonacci in O(n) time and O(1) space?](#35-how-do-you-write-fibonacci-in-on-time-and-o1-space)
- [36: What is recursion?](#36-what-is-recursion)
- [37: What is a base case and what happens if you forget it?](#37-what-is-a-base-case-and-what-happens-if-you-forget-it)
- [38: What is the maximum recursion depth in JavaScript?](#38-what-is-the-maximum-recursion-depth-in-javascript)
- [39: Recursion or iteration: which should you use?](#39-recursion-or-iteration-which-should-you-use)
- [40: How do you reverse an array in place?](#40-how-do-you-reverse-an-array-in-place)
- [41: What is the difference between reverse() and toReversed()?](#41-what-is-the-difference-between-reverse-and-toreversed)
- [42: Why does \[10, 9, 1, 2\].sort() give a strange result?](#42-why-does-10-9-1-2sort-give-a-strange-result)
- [43: How do you sort numbers correctly?](#43-how-do-you-sort-numbers-correctly)
- [44: Is Array.prototype.sort stable?](#44-is-arrayprototypesort-stable)
- [45: What is toSorted() and when would you use it?](#45-what-is-tosorted-and-when-would-you-use-it)
- [46: How do you sort an array of objects by a property?](#46-how-do-you-sort-an-array-of-objects-by-a-property)
- [47: Why use localeCompare for sorting strings?](#47-why-use-localecompare-for-sorting-strings)
- [48: How does bubble sort work?](#48-how-does-bubble-sort-work)
- [49: How does selection sort work?](#49-how-does-selection-sort-work)
- [50: How does insertion sort work?](#50-how-does-insertion-sort-work)
- [51: When is insertion sort a good choice?](#51-when-is-insertion-sort-a-good-choice)
- [52: What does it mean for a sort to be stable?](#52-what-does-it-mean-for-a-sort-to-be-stable)
- [53: What is an in-place algorithm?](#53-what-is-an-in-place-algorithm)
- [54: How do you check if two strings are anagrams?](#54-how-do-you-check-if-two-strings-are-anagrams)
- [55: How do you capitalize the first letter of each word?](#55-how-do-you-capitalize-the-first-letter-of-each-word)
- [56: How do you find the longest word in a sentence?](#56-how-do-you-find-the-longest-word-in-a-sentence)
- [57: How do you count the words in a string?](#57-how-do-you-count-the-words-in-a-string)
- [58: How do you check if a string contains only digits?](#58-how-do-you-check-if-a-string-contains-only-digits)
- [59: How do you truncate a string and add "..."?](#59-how-do-you-truncate-a-string-and-add-)
- [60: How do you repeat a string n times?](#60-how-do-you-repeat-a-string-n-times)
- [61: What is the two-pointer technique?](#61-what-is-the-two-pointer-technique)
- [62: How do you check if an array is sorted?](#62-how-do-you-check-if-an-array-is-sorted)
- [63: How do you merge two sorted arrays into one sorted array?](#63-how-do-you-merge-two-sorted-arrays-into-one-sorted-array)
- [64: How do you find the second largest number in an array?](#64-how-do-you-find-the-second-largest-number-in-an-array)
- [65: How do you split an array into chunks of a given size?](#65-how-do-you-split-an-array-into-chunks-of-a-given-size)
- [66: How do you flatten a nested array?](#66-how-do-you-flatten-a-nested-array)
- [67: How do you flatten an array without flat()?](#67-how-do-you-flatten-an-array-without-flat)
- [68: How do you find the intersection of two arrays?](#68-how-do-you-find-the-intersection-of-two-arrays)
- [69: How do you find the difference between two arrays?](#69-how-do-you-find-the-difference-between-two-arrays)
- [70: How do you get the union of two arrays?](#70-how-do-you-get-the-union-of-two-arrays)
- [71: How do you find the missing number in an array of 1 to n?](#71-how-do-you-find-the-missing-number-in-an-array-of-1-to-n)
- [72: How do you find a duplicate in an array?](#72-how-do-you-find-a-duplicate-in-an-array)
- [73: How do you rotate an array by k positions?](#73-how-do-you-rotate-an-array-by-k-positions)
- [74: How do you move all zeros to the end while keeping the order of other items?](#74-how-do-you-move-all-zeros-to-the-end-while-keeping-the-order-of-other-items)
- [75: What is the Two Sum problem and what is the brute-force solution?](#75-what-is-the-two-sum-problem-and-what-is-the-brute-force-solution)
- [76: How do you solve Two Sum in O(n)?](#76-how-do-you-solve-two-sum-in-on)
- [77: What is the frequency counter pattern?](#77-what-is-the-frequency-counter-pattern)
- [78: How do you check if a number is prime?](#78-how-do-you-check-if-a-number-is-prime)
- [79: What is the Sieve of Eratosthenes?](#79-what-is-the-sieve-of-eratosthenes)
- [80: How do you find the greatest common divisor (GCD)?](#80-how-do-you-find-the-greatest-common-divisor-gcd)
- [81: How do you find the least common multiple (LCM)?](#81-how-do-you-find-the-least-common-multiple-lcm)
- [82: How do you sum the digits of a number?](#82-how-do-you-sum-the-digits-of-a-number)
- [83: How do you reverse the digits of an integer?](#83-how-do-you-reverse-the-digits-of-an-integer)
- [84: How do you check if a number is a palindrome without converting it to a string?](#84-how-do-you-check-if-a-number-is-a-palindrome-without-converting-it-to-a-string)
- [85: How do you check if a number is a power of two?](#85-how-do-you-check-if-a-number-is-a-power-of-two)
- [86: How do you check if a number is even or odd?](#86-how-do-you-check-if-a-number-is-even-or-odd)
- [87: How do you swap two variables without a temp variable?](#87-how-do-you-swap-two-variables-without-a-temp-variable)
- [88: How do you create an array of numbers from 1 to n?](#88-how-do-you-create-an-array-of-numbers-from-1-to-n)
- [89: How do you shuffle an array correctly?](#89-how-do-you-shuffle-an-array-correctly)
- [90: Why is arr.sort(() => Math.random() - 0.5) a bad way to shuffle?](#90-why-is-arrsort--mathrandom---05-a-bad-way-to-shuffle)
- [91: How do you get a random integer between min and max?](#91-how-do-you-get-a-random-integer-between-min-and-max)
- [92: Is chaining map, filter and reduce slower than one loop?](#92-is-chaining-map-filter-and-reduce-slower-than-one-loop)
- [93: What is the difference between for, for...of and forEach when writing algorithms?](#93-what-is-the-difference-between-for-forof-and-foreach-when-writing-algorithms)
- [94: How do some, every and find help you exit early?](#94-how-do-some-every-and-find-help-you-exit-early)
- [95: How do you use an array as a stack?](#95-how-do-you-use-an-array-as-a-stack)
- [96: How do you use an array as a queue, and what is the problem with it?](#96-how-do-you-use-an-array-as-a-queue-and-what-is-the-problem-with-it)
- [97: How do you check if brackets in a string are balanced?](#97-how-do-you-check-if-brackets-in-a-string-are-balanced)
- [98: What is a linked list?](#98-what-is-a-linked-list)
- [99: What is a hash table?](#99-what-is-a-hash-table)
- [100: When should you use a Map instead of a plain object in algorithms?](#100-when-should-you-use-a-map-instead-of-a-plain-object-in-algorithms)
- [101: What is a tree?](#101-what-is-a-tree)
- [102: What is the difference between a binary tree and a binary search tree?](#102-what-is-the-difference-between-a-binary-tree-and-a-binary-search-tree)
- [103: What are the main ways to traverse a tree?](#103-what-are-the-main-ways-to-traverse-a-tree)
- [104: What is a graph?](#104-what-is-a-graph)
- [105: What is the difference between BFS and DFS?](#105-what-is-the-difference-between-bfs-and-dfs)
- [106: What is a greedy algorithm?](#106-what-is-a-greedy-algorithm)
- [107: What is divide and conquer?](#107-what-is-divide-and-conquer)
- [108: What is dynamic programming?](#108-what-is-dynamic-programming)
- [109: What is memoization?](#109-what-is-memoization)
- [110: What is a brute-force solution and is it ever a good answer?](#110-what-is-a-brute-force-solution-and-is-it-ever-a-good-answer)
- [111: How should you approach an algorithm question in an interview?](#111-how-should-you-approach-an-algorithm-question-in-an-interview)
- [112: What edge cases should you check for in algorithm problems?](#112-what-edge-cases-should-you-check-for-in-algorithm-problems)
- [113: How do you quickly test an algorithm in JavaScript?](#113-how-do-you-quickly-test-an-algorithm-in-javascript)
- [114: Why does 0.1 + 0.2 !== 0.3, and why does it matter for algorithms?](#114-why-does-01--02--03-and-why-does-it-matter-for-algorithms)
- [115: What is Number.MAX_SAFE_INTEGER and when do you need BigInt?](#115-what-is-numbermax_safe_integer-and-when-do-you-need-bigint)
- [116: What is the difference between Math.floor and Math.trunc for integer division?](#116-what-is-the-difference-between-mathfloor-and-mathtrunc-for-integer-division)
- [117: How does the % operator work with negative numbers?](#117-how-does-the--operator-work-with-negative-numbers)
- [118: What is the difference between charCodeAt and codePointAt?](#118-what-is-the-difference-between-charcodeat-and-codepointat)
- [119: Can you change a character in a JavaScript string directly?](#119-can-you-change-a-character-in-a-javascript-string-directly)
- [120: Why can splitting a string with split("") break emoji?](#120-why-can-splitting-a-string-with-split-break-emoji)
- [121: How do you check if two arrays are equal?](#121-how-do-you-check-if-two-arrays-are-equal)
- [122: How do you compare two objects shallowly?](#122-how-do-you-compare-two-objects-shallowly)
- [123: What is the difference between find, findIndex, findLast and findLastIndex?](#123-what-is-the-difference-between-find-findindex-findlast-and-findlastindex)
- [124: How do you find the first non-repeating character in a string?](#124-how-do-you-find-the-first-non-repeating-character-in-a-string)
- [125: How do you find the longest run of the same value in an array?](#125-how-do-you-find-the-longest-run-of-the-same-value-in-an-array)
- [126: How do you check if an array has any duplicates?](#126-how-do-you-check-if-an-array-has-any-duplicates)
- [127: How do you check if a sentence is a pangram?](#127-how-do-you-check-if-a-sentence-is-a-pangram)
- [128: How do you compress a string like "aaabcc" into "a3b1c2"?](#128-how-do-you-compress-a-string-like-aaabcc-into-a3b1c2)
- [129: How do you convert a number to binary and back?](#129-how-do-you-convert-a-number-to-binary-and-back)
- [130: How do you convert a Roman numeral to an integer?](#130-how-do-you-convert-a-roman-numeral-to-an-integer)
- [131: How do you check if a year is a leap year?](#131-how-do-you-check-if-a-year-is-a-leap-year)
- [132: How do you sum the numbers from 1 to n without a loop?](#132-how-do-you-sum-the-numbers-from-1-to-n-without-a-loop)
- [133: How do you find the most frequent element in an array?](#133-how-do-you-find-the-most-frequent-element-in-an-array)
- [134: How do you group items by a key?](#134-how-do-you-group-items-by-a-key)
- [135: How do you zip two arrays together?](#135-how-do-you-zip-two-arrays-together)
- [136: How do you remove duplicate objects by id?](#136-how-do-you-remove-duplicate-objects-by-id)
- [137: What is wrong with Array(3).fill(\[\]) for a 2D array?](#137-what-is-wrong-with-array3fill-for-a-2d-array)
- [138: How do you transpose a matrix?](#138-how-do-you-transpose-a-matrix)
- [139: How do you sum the diagonals of a square matrix?](#139-how-do-you-sum-the-diagonals-of-a-square-matrix)
- [140: How do you search for a value in a 2D array?](#140-how-do-you-search-for-a-value-in-a-2d-array)
- [141: What is the complexity of two nested loops over different arrays?](#141-what-is-the-complexity-of-two-nested-loops-over-different-arrays)
- [142: What does amortized time mean?](#142-what-does-amortized-time-mean)
- [143: What is the space complexity of a recursive function?](#143-what-is-the-space-complexity-of-a-recursive-function)
- [144: What is the complexity of slice, splice, concat and spread?](#144-what-is-the-complexity-of-slice-splice-concat-and-spread)
- [145: What is an off-by-one error?](#145-what-is-an-off-by-one-error)
- [146: How do you avoid infinite loops in while loops?](#146-how-do-you-avoid-infinite-loops-in-while-loops)
- [147: Why can Math.max(...arr) fail on very large arrays?](#147-why-can-mathmaxarr-fail-on-very-large-arrays)
- [148: What algorithm does JavaScript's built-in sort use?](#148-what-algorithm-does-javascripts-built-in-sort-use)
- [149: How do you count the number of unique values?](#149-how-do-you-count-the-number-of-unique-values)
- [150: What is the difference between an algorithm and a data structure?](#150-what-is-the-difference-between-an-algorithm-and-a-data-structure)

### Moderate Questions (151-300)

- [151: How does merge sort work?](#151-how-does-merge-sort-work)
- [152: How does quick sort work?](#152-how-does-quick-sort-work)
- [153: What is the worst case of quick sort and how do you avoid it?](#153-what-is-the-worst-case-of-quick-sort-and-how-do-you-avoid-it)
- [154: When would you pick merge sort over quick sort, or the other way around?](#154-when-would-you-pick-merge-sort-over-quick-sort-or-the-other-way-around)
- [155: How does heap sort work?](#155-how-does-heap-sort-work)
- [156: What is counting sort and when can you use it?](#156-what-is-counting-sort-and-when-can-you-use-it)
- [157: What is radix sort?](#157-what-is-radix-sort)
- [158: What is bucket sort?](#158-what-is-bucket-sort)
- [159: Why can't comparison sorts be faster than O(n log n)?](#159-why-cant-comparison-sorts-be-faster-than-on-log-n)
- [160: What is TimSort?](#160-what-is-timsort)
- [161: How do you sort by several keys, for example by last name and then first name?](#161-how-do-you-sort-by-several-keys-for-example-by-last-name-and-then-first-name)
- [162: How do you find the first and last position of a value in a sorted array?](#162-how-do-you-find-the-first-and-last-position-of-a-value-in-a-sorted-array)
- [163: What is a "lower bound" binary search?](#163-what-is-a-lower-bound-binary-search)
- [164: How do you search in a rotated sorted array?](#164-how-do-you-search-in-a-rotated-sorted-array)
- [165: How do you find a peak element in an array?](#165-how-do-you-find-a-peak-element-in-an-array)
- [166: What is "binary search on the answer"?](#166-what-is-binary-search-on-the-answer)
- [167: How do you find the integer square root without Math.sqrt?](#167-how-do-you-find-the-integer-square-root-without-mathsqrt)
- [168: What is the sliding window technique? Show the fixed-size version.](#168-what-is-the-sliding-window-technique-show-the-fixed-size-version)
- [169: How do you find the longest substring without repeating characters?](#169-how-do-you-find-the-longest-substring-without-repeating-characters)
- [170: How do you find the shortest subarray with a sum of at least a target?](#170-how-do-you-find-the-shortest-subarray-with-a-sum-of-at-least-a-target)
- [171: How do you find a pair with a given sum in a sorted array?](#171-how-do-you-find-a-pair-with-a-given-sum-in-a-sorted-array)
- [172: How do you solve Three Sum (all unique triplets that sum to zero)?](#172-how-do-you-solve-three-sum-all-unique-triplets-that-sum-to-zero)
- [173: How do you solve "container with most water"?](#173-how-do-you-solve-container-with-most-water)
- [174: How do you remove duplicates from a sorted array in place?](#174-how-do-you-remove-duplicates-from-a-sorted-array-in-place)
- [175: How do you sort an array of 0s, 1s and 2s in one pass?](#175-how-do-you-sort-an-array-of-0s-1s-and-2s-in-one-pass)
- [176: What are prefix sums and what are they used for?](#176-what-are-prefix-sums-and-what-are-they-used-for)
- [177: How do you count subarrays that sum to k?](#177-how-do-you-count-subarrays-that-sum-to-k)
- [178: What is Kadane's algorithm?](#178-what-is-kadanes-algorithm)
- [179: How do you compute the product of an array except self without division?](#179-how-do-you-compute-the-product-of-an-array-except-self-without-division)
- [180: How do you find the best time to buy and sell a stock once?](#180-how-do-you-find-the-best-time-to-buy-and-sell-a-stock-once)
- [181: What is the Boyer-Moore voting algorithm?](#181-what-is-the-boyer-moore-voting-algorithm)
- [182: How do you merge overlapping intervals?](#182-how-do-you-merge-overlapping-intervals)
- [183: How do you insert a new interval into a sorted list of non-overlapping intervals?](#183-how-do-you-insert-a-new-interval-into-a-sorted-list-of-non-overlapping-intervals)
- [184: How do you check if a person can attend all meetings?](#184-how-do-you-check-if-a-person-can-attend-all-meetings)
- [185: How do you group anagrams together?](#185-how-do-you-group-anagrams-together)
- [186: How do you find the longest common prefix of a list of strings?](#186-how-do-you-find-the-longest-common-prefix-of-a-list-of-strings)
- [187: When is sorting better than counting for anagram checks, and the other way around?](#187-when-is-sorting-better-than-counting-for-anagram-checks-and-the-other-way-around)
- [188: How do you find the longest palindromic substring?](#188-how-do-you-find-the-longest-palindromic-substring)
- [189: How do you reverse the order of words in a sentence?](#189-how-do-you-reverse-the-order-of-words-in-a-sentence)
- [190: How do you check for a palindrome while ignoring spaces, punctuation and case?](#190-how-do-you-check-for-a-palindrome-while-ignoring-spaces-punctuation-and-case)
- [191: How do you convert an integer to a Roman numeral?](#191-how-do-you-convert-an-integer-to-a-roman-numeral)
- [192: How do you implement indexOf for substrings yourself?](#192-how-do-you-implement-indexof-for-substrings-yourself)
- [193: How do you check if two strings are isomorphic?](#193-how-do-you-check-if-two-strings-are-isomorphic)
- [194: How do you check if a ransom note can be built from a magazine?](#194-how-do-you-check-if-a-ransom-note-can-be-built-from-a-magazine)
- [195: How do you implement a singly linked list in JavaScript?](#195-how-do-you-implement-a-singly-linked-list-in-javascript)
- [196: How do you reverse a linked list?](#196-how-do-you-reverse-a-linked-list)
- [197: How do you detect a cycle in a linked list?](#197-how-do-you-detect-a-cycle-in-a-linked-list)
- [198: How do you find the middle of a linked list in one pass?](#198-how-do-you-find-the-middle-of-a-linked-list-in-one-pass)
- [199: How do you merge two sorted linked lists?](#199-how-do-you-merge-two-sorted-linked-lists)
- [200: How do you remove the nth node from the end of a linked list?](#200-how-do-you-remove-the-nth-node-from-the-end-of-a-linked-list)
- [201: How do you build a stack that returns the minimum in O(1)?](#201-how-do-you-build-a-stack-that-returns-the-minimum-in-o1)
- [202: How do you evaluate an expression in Reverse Polish Notation?](#202-how-do-you-evaluate-an-expression-in-reverse-polish-notation)
- [203: What is a monotonic stack? Show "next greater element".](#203-what-is-a-monotonic-stack-show-next-greater-element)
- [204: How do you build a queue from two stacks?](#204-how-do-you-build-a-queue-from-two-stacks)
- [205: How do you build a fast queue in JavaScript without shift()?](#205-how-do-you-build-a-fast-queue-in-javascript-without-shift)
- [206: What is a circular buffer (ring buffer)?](#206-what-is-a-circular-buffer-ring-buffer)
- [207: How do you insert a value into a binary search tree?](#207-how-do-you-insert-a-value-into-a-binary-search-tree)
- [208: How do you search a binary search tree?](#208-how-do-you-search-a-binary-search-tree)
- [209: How do you write preorder, inorder and postorder traversal?](#209-how-do-you-write-preorder-inorder-and-postorder-traversal)
- [210: How do you do a level order (BFS) traversal of a binary tree?](#210-how-do-you-do-a-level-order-bfs-traversal-of-a-binary-tree)
- [211: How do you find the maximum depth of a binary tree?](#211-how-do-you-find-the-maximum-depth-of-a-binary-tree)
- [212: How do you check if a binary tree is a valid BST?](#212-how-do-you-check-if-a-binary-tree-is-a-valid-bst)
- [213: How do you invert (mirror) a binary tree?](#213-how-do-you-invert-mirror-a-binary-tree)
- [214: How do you find the lowest common ancestor in a BST?](#214-how-do-you-find-the-lowest-common-ancestor-in-a-bst)
- [215: How do you check if a binary tree is height-balanced?](#215-how-do-you-check-if-a-binary-tree-is-height-balanced)
- [216: How do you do an inorder traversal without recursion?](#216-how-do-you-do-an-inorder-traversal-without-recursion)
- [217: How do you walk the DOM tree recursively?](#217-how-do-you-walk-the-dom-tree-recursively)
- [218: How would you write your own getElementsByClassName?](#218-how-would-you-write-your-own-getelementsbyclassname)
- [219: How do you flatten a nested object into dot-notation keys?](#219-how-do-you-flatten-a-nested-object-into-dot-notation-keys)
- [220: How do you turn dot-notation keys back into a nested object?](#220-how-do-you-turn-dot-notation-keys-back-into-a-nested-object)
- [221: How do you deep clone an object?](#221-how-do-you-deep-clone-an-object)
- [222: How do you write a deep equality check?](#222-how-do-you-write-a-deep-equality-check)
- [223: How do you get a nested value by a path string, like lodash get?](#223-how-do-you-get-a-nested-value-by-a-path-string-like-lodash-get)
- [224: How do you represent a graph in JavaScript?](#224-how-do-you-represent-a-graph-in-javascript)
- [225: How do you implement BFS on a graph?](#225-how-do-you-implement-bfs-on-a-graph)
- [226: How do you implement DFS on a graph?](#226-how-do-you-implement-dfs-on-a-graph)
- [227: How do you find the shortest path in an unweighted graph?](#227-how-do-you-find-the-shortest-path-in-an-unweighted-graph)
- [228: How do you count islands in a grid?](#228-how-do-you-count-islands-in-a-grid)
- [229: How do you detect a cycle in a directed graph?](#229-how-do-you-detect-a-cycle-in-a-directed-graph)
- [230: What is topological sort and how do you do it?](#230-what-is-topological-sort-and-how-do-you-do-it)
- [231: Where does topological sort show up in front-end work?](#231-where-does-topological-sort-show-up-in-front-end-work)
- [232: How do you count connected components in an undirected graph?](#232-how-do-you-count-connected-components-in-an-undirected-graph)
- [233: How does flood fill work?](#233-how-does-flood-fill-work)
- [234: What is a clean way to move in four directions on a grid?](#234-what-is-a-clean-way-to-move-in-four-directions-on-a-grid)
- [235: What is backtracking?](#235-what-is-backtracking)
- [236: How do you generate all subsets of an array?](#236-how-do-you-generate-all-subsets-of-an-array)
- [237: How do you generate all permutations of an array?](#237-how-do-you-generate-all-permutations-of-an-array)
- [238: How do you generate all combinations of k items from n?](#238-how-do-you-generate-all-combinations-of-k-items-from-n)
- [239: How do you solve Combination Sum (numbers can be reused)?](#239-how-do-you-solve-combination-sum-numbers-can-be-reused)
- [240: How do you generate all valid combinations of n pairs of parentheses?](#240-how-do-you-generate-all-valid-combinations-of-n-pairs-of-parentheses)
- [241: How do you search for a word in a grid of letters?](#241-how-do-you-search-for-a-word-in-a-grid-of-letters)
- [242: How do you solve "climbing stairs" with dynamic programming?](#242-how-do-you-solve-climbing-stairs-with-dynamic-programming)
- [243: What is the difference between top-down and bottom-up dynamic programming?](#243-what-is-the-difference-between-top-down-and-bottom-up-dynamic-programming)
- [244: How do you find the minimum number of coins to make an amount?](#244-how-do-you-find-the-minimum-number-of-coins-to-make-an-amount)
- [245: How do you count the number of ways to make change?](#245-how-do-you-count-the-number-of-ways-to-make-change)
- [246: How do you solve the House Robber problem?](#246-how-do-you-solve-the-house-robber-problem)
- [247: How do you find the longest common subsequence of two strings?](#247-how-do-you-find-the-longest-common-subsequence-of-two-strings)
- [248: How do you calculate the edit distance (Levenshtein distance) between two strings?](#248-how-do-you-calculate-the-edit-distance-levenshtein-distance-between-two-strings)
- [249: How do you solve the 0/1 knapsack problem?](#249-how-do-you-solve-the-01-knapsack-problem)
- [250: How do you find the length of the longest increasing subsequence?](#250-how-do-you-find-the-length-of-the-longest-increasing-subsequence)
- [251: How many unique paths are there in a grid when you can only move right or down?](#251-how-many-unique-paths-are-there-in-a-grid-when-you-can-only-move-right-or-down)
- [252: How can you reduce memory in dynamic programming?](#252-how-can-you-reduce-memory-in-dynamic-programming)
- [253: How do you write a generic memoize function?](#253-how-do-you-write-a-generic-memoize-function)
- [254: How do you choose a cache key when memoizing a function with several arguments?](#254-how-do-you-choose-a-cache-key-when-memoizing-a-function-with-several-arguments)
- [255: How do you solve the Jump Game with a greedy approach?](#255-how-do-you-solve-the-jump-game-with-a-greedy-approach)
- [256: When does a greedy algorithm give the wrong answer?](#256-when-does-a-greedy-algorithm-give-the-wrong-answer)
- [257: How do you implement a min-heap (priority queue) in JavaScript?](#257-how-do-you-implement-a-min-heap-priority-queue-in-javascript)
- [258: How do you find the top K most frequent elements?](#258-how-do-you-find-the-top-k-most-frequent-elements)
- [259: How do you find the kth largest element in an array?](#259-how-do-you-find-the-kth-largest-element-in-an-array)
- [260: How do you merge k sorted arrays?](#260-how-do-you-merge-k-sorted-arrays)
- [261: How do bitwise operators work in JavaScript, and what is the catch?](#261-how-do-bitwise-operators-work-in-javascript-and-what-is-the-catch)
- [262: How do you find the one number that appears once when every other number appears twice?](#262-how-do-you-find-the-one-number-that-appears-once-when-every-other-number-appears-twice)
- [263: How do you count the number of 1 bits in a number?](#263-how-do-you-count-the-number-of-1-bits-in-a-number)
- [264: How can you use a bitmask to represent a set of options?](#264-how-can-you-use-a-bitmask-to-represent-a-set-of-options)
- [265: How do you implement debounce?](#265-how-do-you-implement-debounce)
- [266: How do you implement throttle?](#266-how-do-you-implement-throttle)
- [267: How do you implement Promise.all yourself?](#267-how-do-you-implement-promiseall-yourself)
- [268: How do you run async tasks with a concurrency limit?](#268-how-do-you-run-async-tasks-with-a-concurrency-limit)
- [269: How do you retry an async call with exponential backoff?](#269-how-do-you-retry-an-async-call-with-exponential-backoff)
- [270: How do you implement an LRU cache?](#270-how-do-you-implement-an-lru-cache)
- [271: How do you implement Array.prototype.reduce yourself?](#271-how-do-you-implement-arrayprototypereduce-yourself)
- [272: How do you implement flat() with a depth argument?](#272-how-do-you-implement-flat-with-a-depth-argument)
- [273: How do you implement currying?](#273-how-do-you-implement-currying)
- [274: How do you implement compose and pipe?](#274-how-do-you-implement-compose-and-pipe)
- [275: How do you binary search over objects or dates?](#275-how-do-you-binary-search-over-objects-or-dates)
- [276: How do you calculate pagination values?](#276-how-do-you-calculate-pagination-values)
- [277: How would you implement a simple fuzzy search for a list?](#277-how-would-you-implement-a-simple-fuzzy-search-for-a-list)
- [278: How do you highlight search matches in text safely?](#278-how-do-you-highlight-search-matches-in-text-safely)
- [279: How do you calculate which rows to render in a virtual list with fixed row heights?](#279-how-do-you-calculate-which-rows-to-render-in-a-virtual-list-with-fixed-row-heights)
- [280: How do you find which items were added, removed or changed between two lists?](#280-how-do-you-find-which-items-were-added-removed-or-changed-between-two-lists)
- [281: How do you rotate a square matrix 90 degrees clockwise in place?](#281-how-do-you-rotate-a-square-matrix-90-degrees-clockwise-in-place)
- [282: How do you read a matrix in spiral order?](#282-how-do-you-read-a-matrix-in-spiral-order)
- [283: How do you set a whole row and column to zero if a cell is zero?](#283-how-do-you-set-a-whole-row-and-column-to-zero-if-a-cell-is-zero)
- [284: How do you check if a Sudoku board is valid?](#284-how-do-you-check-if-a-sudoku-board-is-valid)
- [285: How do you generate Pascal's triangle?](#285-how-do-you-generate-pascals-triangle)
- [286: How do you check if a string contains a permutation of another string?](#286-how-do-you-check-if-a-string-contains-a-permutation-of-another-string)
- [287: When should you use an array of 26 counts instead of a Map for letter counting?](#287-when-should-you-use-an-array-of-26-counts-instead-of-a-map-for-letter-counting)
- [288: How do you turn a recursive function into an iterative one?](#288-how-do-you-turn-a-recursive-function-into-an-iterative-one)
- [289: Does JavaScript support tail call optimization?](#289-does-javascript-support-tail-call-optimization)
- [290: How can generators help with algorithms?](#290-how-can-generators-help-with-algorithms)
- [291: What are iterator helpers and why are they useful for algorithms?](#291-what-are-iterator-helpers-and-why-are-they-useful-for-algorithms)
- [292: What are the new Set methods?](#292-what-are-the-new-set-methods)
- [293: How do you work out the time complexity of a recursive function?](#293-how-do-you-work-out-the-time-complexity-of-a-recursive-function)
- [294: What is the Master Theorem?](#294-what-is-the-master-theorem)
- [295: How does stable sorting help when users sort a table by several columns?](#295-how-does-stable-sorting-help-when-users-sort-a-table-by-several-columns)
- [296: What are common comparator mistakes?](#296-what-are-common-comparator-mistakes)
- [297: How can you make sorting large lists of strings faster?](#297-how-can-you-make-sorting-large-lists-of-strings-faster)
- [298: How do you check if a string has balanced brackets while ignoring brackets inside quotes?](#298-how-do-you-check-if-a-string-has-balanced-brackets-while-ignoring-brackets-inside-quotes)
- [299: How do you implement an undo/redo history?](#299-how-do-you-implement-an-undoredo-history)
- [300: How do you decide which data structure to use for a problem?](#300-how-do-you-decide-which-data-structure-to-use-for-a-problem)

### Advanced Questions (301-450)

- [301: How does Dijkstra's algorithm work?](#301-how-does-dijkstras-algorithm-work)
- [302: How do you implement Dijkstra in JavaScript?](#302-how-do-you-implement-dijkstra-in-javascript)
- [303: Why does Dijkstra fail with negative weights, and what do you use instead?](#303-why-does-dijkstra-fail-with-negative-weights-and-what-do-you-use-instead)
- [304: What is A* search?](#304-what-is-a-search)
- [305: What is the Floyd-Warshall algorithm?](#305-what-is-the-floyd-warshall-algorithm)
- [306: What is Union-Find (disjoint set union)?](#306-what-is-union-find-disjoint-set-union)
- [307: How does Kruskal's algorithm find a minimum spanning tree?](#307-how-does-kruskals-algorithm-find-a-minimum-spanning-tree)
- [308: How does Prim's algorithm differ from Kruskal's?](#308-how-does-prims-algorithm-differ-from-kruskals)
- [309: How do you detect a cycle in an undirected graph?](#309-how-do-you-detect-a-cycle-in-an-undirected-graph)
- [310: How do you check if a graph is bipartite?](#310-how-do-you-check-if-a-graph-is-bipartite)
- [311: What are strongly connected components and how do you find them?](#311-what-are-strongly-connected-components-and-how-do-you-find-them)
- [312: What is bidirectional BFS?](#312-what-is-bidirectional-bfs)
- [313: How do you solve Word Ladder?](#313-how-do-you-solve-word-ladder)
- [314: How do you clone a graph?](#314-how-do-you-clone-a-graph)
- [315: What is a trie and how do you implement one?](#315-what-is-a-trie-and-how-do-you-implement-one)
- [316: How do you build autocomplete with a trie?](#316-how-do-you-build-autocomplete-with-a-trie)
- [317: Trie or sorted array with binary search for autocomplete?](#317-trie-or-sorted-array-with-binary-search-for-autocomplete)
- [318: How does the KMP string search algorithm work?](#318-how-does-the-kmp-string-search-algorithm-work)
- [319: How does Rabin-Karp work?](#319-how-does-rabin-karp-work)
- [320: How do you find the longest common substring of two strings?](#320-how-do-you-find-the-longest-common-substring-of-two-strings)
- [321: What is catastrophic backtracking in regular expressions?](#321-what-is-catastrophic-backtracking-in-regular-expressions)
- [322: What is a segment tree?](#322-what-is-a-segment-tree)
- [323: What is a Fenwick tree (Binary Indexed Tree)?](#323-what-is-a-fenwick-tree-binary-indexed-tree)
- [324: When would you choose prefix sums, a Fenwick tree or a segment tree?](#324-when-would-you-choose-prefix-sums-a-fenwick-tree-or-a-segment-tree)
- [325: How does Quickselect work, and what is its worst case?](#325-how-does-quickselect-work-and-what-is-its-worst-case)
- [326: How do you find the median of two sorted arrays in O(log(min(n, m)))?](#326-how-do-you-find-the-median-of-two-sorted-arrays-in-ologminn-m)
- [327: How do you keep track of the median of a stream of numbers?](#327-how-do-you-keep-track-of-the-median-of-a-stream-of-numbers)
- [328: How do you find the maximum in every sliding window of size k?](#328-how-do-you-find-the-maximum-in-every-sliding-window-of-size-k)
- [329: How do you find the largest rectangle in a histogram?](#329-how-do-you-find-the-largest-rectangle-in-a-histogram)
- [330: How do you solve Trapping Rain Water?](#330-how-do-you-solve-trapping-rain-water)
- [331: How do you build an LRU cache with O(1) operations without relying on Map order?](#331-how-do-you-build-an-lru-cache-with-o1-operations-without-relying-on-map-order)
- [332: How would you implement an LFU (least frequently used) cache?](#332-how-would-you-implement-an-lfu-least-frequently-used-cache)
- [333: What is reservoir sampling?](#333-what-is-reservoir-sampling)
- [334: What is a Bloom filter?](#334-what-is-a-bloom-filter)
- [335: How do you write a simple string hash function, and what are its limits?](#335-how-do-you-write-a-simple-string-hash-function-and-what-are-its-limits)
- [336: What is hash flooding and why does it matter for JavaScript objects and Maps?](#336-what-is-hash-flooding-and-why-does-it-matter-for-javascript-objects-and-maps)
- [337: What are the memory risks of memoization, and how do you limit them?](#337-what-are-the-memory-risks-of-memoization-and-how-do-you-limit-them)
- [338: How do you solve Word Break?](#338-how-do-you-solve-word-break)
- [339: How do you find the longest increasing subsequence in O(n log n)?](#339-how-do-you-find-the-longest-increasing-subsequence-in-on-log-n)
- [340: How do you reconstruct the actual edits from an edit distance table?](#340-how-do-you-reconstruct-the-actual-edits-from-an-edit-distance-table)
- [341: How do text diff tools like git diff work?](#341-how-do-text-diff-tools-like-git-diff-work)
- [342: Why can't frameworks use a full tree diff algorithm for the virtual DOM?](#342-why-cant-frameworks-use-a-full-tree-diff-algorithm-for-the-virtual-dom)
- [343: How do keyed list updates find the minimum DOM moves?](#343-how-do-keyed-list-updates-find-the-minimum-dom-moves)
- [344: What is bitmask dynamic programming? Use the Traveling Salesman Problem as an example.](#344-what-is-bitmask-dynamic-programming-use-the-traveling-salesman-problem-as-an-example)
- [345: How do you solve N-Queens?](#345-how-do-you-solve-n-queens)
- [346: How do you write a Sudoku solver?](#346-how-do-you-write-a-sudoku-solver)
- [347: What is pruning in backtracking and why does it matter?](#347-what-is-pruning-in-backtracking-and-why-does-it-matter)
- [348: How do you find the minimum number of meeting rooms needed?](#348-how-do-you-find-the-minimum-number-of-meeting-rooms-needed)
- [349: What rate limiting algorithms do you know?](#349-what-rate-limiting-algorithms-do-you-know)
- [350: Why add jitter to exponential backoff?](#350-why-add-jitter-to-exponential-backoff)
- [351: How would you build a task scheduler that runs async tasks by priority with a concurrency limit?](#351-how-would-you-build-a-task-scheduler-that-runs-async-tasks-by-priority-with-a-concurrency-limit)
- [352: How do you avoid race conditions in a search-as-you-type feature?](#352-how-do-you-avoid-race-conditions-in-a-search-as-you-type-feature)
- [353: How do bundlers detect circular dependencies, and why are they a problem?](#353-how-do-bundlers-detect-circular-dependencies-and-why-are-they-a-problem)
- [354: Why can a heavy algorithm freeze the page, and how does the event loop relate to it?](#354-why-can-a-heavy-algorithm-freeze-the-page-and-how-does-the-event-loop-relate-to-it)
- [355: How do you split a long computation into chunks so the UI stays responsive?](#355-how-do-you-split-a-long-computation-into-chunks-so-the-ui-stays-responsive)
- [356: When should you move an algorithm to a Web Worker?](#356-when-should-you-move-an-algorithm-to-a-web-worker)
- [357: How do you avoid the cost of copying large data to and from a worker?](#357-how-do-you-avoid-the-cost-of-copying-large-data-to-and-from-a-worker)
- [358: Why are typed arrays faster for numeric algorithms?](#358-why-are-typed-arrays-faster-for-numeric-algorithms)
- [359: What are V8 "elements kinds" and how can they affect algorithm speed?](#359-what-are-v8-elements-kinds-and-how-can-they-affect-algorithm-speed)
- [360: Why is new Array(n) sometimes slower than building an array with push?](#360-why-is-new-arrayn-sometimes-slower-than-building-an-array-with-push)
- [361: How do hidden classes and inline caches affect algorithm code?](#361-how-do-hidden-classes-and-inline-caches-affect-algorithm-code)
- [362: What are the pitfalls of benchmarking algorithms in JavaScript?](#362-what-are-the-pitfalls-of-benchmarking-algorithms-in-javascript)
- [363: How do you check the memory use of an algorithm in the browser?](#363-how-do-you-check-the-memory-use-of-an-algorithm-in-the-browser)
- [364: Map or object: which performs better for frequent inserts and deletes?](#364-map-or-object-which-performs-better-for-frequent-inserts-and-deletes)
- [365: Is building a big string with an array and join faster than +=?](#365-is-building-a-big-string-with-an-array-and-join-faster-than-)
- [366: What is a trampoline and when would you use it?](#366-what-is-a-trampoline-and-when-would-you-use-it)
- [367: How do you traverse a very deep structure (like a huge JSON or a long linked chain) safely?](#367-how-do-you-traverse-a-very-deep-structure-like-a-huge-json-or-a-long-linked-chain-safely)
- [368: How do you compare floating point numbers safely in algorithms?](#368-how-do-you-compare-floating-point-numbers-safely-in-algorithms)
- [369: How do you compute a^b mod m efficiently?](#369-how-do-you-compute-ab-mod-m-efficiently)
- [370: Why is Math.random not enough for some algorithms, and how do you get an unbiased random integer?](#370-why-is-mathrandom-not-enough-for-some-algorithms-and-how-do-you-get-an-unbiased-random-integer)
- [371: How do you get reproducible random numbers (a seeded PRNG)?](#371-how-do-you-get-reproducible-random-numbers-a-seeded-prng)
- [372: How would you test that a shuffle is unbiased?](#372-how-would-you-test-that-a-shuffle-is-unbiased)
- [373: How would you sort 1 million rows in the browser without freezing the page?](#373-how-would-you-sort-1-million-rows-in-the-browser-without-freezing-the-page)
- [374: How do you implement natural sort ("file2" before "file10")?](#374-how-do-you-implement-natural-sort-file2-before-file10)
- [375: How do fuzzy finders like fzf or VS Code's quick open rank results?](#375-how-do-fuzzy-finders-like-fzf-or-vs-codes-quick-open-rank-results)
- [376: How would you build fast client-side full-text search?](#376-how-would-you-build-fast-client-side-full-text-search)
- [377: How would you design a typeahead component from an algorithm point of view?](#377-how-would-you-design-a-typeahead-component-from-an-algorithm-point-of-view)
- [378: How do you render a virtual list where rows have different heights?](#378-how-do-you-render-a-virtual-list-where-rows-have-different-heights)
- [379: How does a masonry layout algorithm work?](#379-how-does-a-masonry-layout-algorithm-work)
- [380: How do you detect collisions between many objects efficiently?](#380-how-do-you-detect-collisions-between-many-objects-efficiently)
- [381: How does a quadtree work?](#381-how-does-a-quadtree-work)
- [382: How do you check if a point is inside a polygon?](#382-how-do-you-check-if-a-point-is-inside-a-polygon)
- [383: How do you simplify a line with many points, for example for a chart or map?](#383-how-do-you-simplify-a-line-with-many-points-for-example-for-a-chart-or-map)
- [384: How do you downsample a large time series for a chart without losing its shape?](#384-how-do-you-downsample-a-large-time-series-for-a-chart-without-losing-its-shape)
- [385: How do you find the data point nearest to the mouse on a line chart?](#385-how-do-you-find-the-data-point-nearest-to-the-mouse-on-a-line-chart)
- [386: How do collaborative editors merge concurrent changes? Compare OT and CRDTs.](#386-how-do-collaborative-editors-merge-concurrent-changes-compare-ot-and-crdts)
- [387: How do you compute a JSON diff and apply it as a patch?](#387-how-do-you-compute-a-json-diff-and-apply-it-as-a-patch)
- [388: How do you deep clone an object that has circular references?](#388-how-do-you-deep-clone-an-object-that-has-circular-references)
- [389: How do you write a deep equal that handles cycles, NaN, Map and Set?](#389-how-do-you-write-a-deep-equal-that-handles-cycles-nan-map-and-set)
- [390: How do you serialize and deserialize a binary tree?](#390-how-do-you-serialize-and-deserialize-a-binary-tree)
- [391: How do you find the lowest common ancestor of two nodes in any binary tree?](#391-how-do-you-find-the-lowest-common-ancestor-of-two-nodes-in-any-binary-tree)
- [392: How do you find the diameter of a binary tree?](#392-how-do-you-find-the-diameter-of-a-binary-tree)
- [393: How do you find the maximum path sum in a binary tree?](#393-how-do-you-find-the-maximum-path-sum-in-a-binary-tree)
- [394: How do you build a tree from a flat list with parentId in O(n)?](#394-how-do-you-build-a-tree-from-a-flat-list-with-parentid-in-on)
- [395: What is Morris traversal?](#395-what-is-morris-traversal)
- [396: How can generators make tree traversal code cleaner?](#396-how-can-generators-make-tree-traversal-code-cleaner)
- [397: How do you find the kth smallest value in a BST?](#397-how-do-you-find-the-kth-smallest-value-in-a-bst)
- [398: How do you count the number of paths in a directed acyclic graph?](#398-how-do-you-count-the-number-of-paths-in-a-directed-acyclic-graph)
- [399: How do you find shortest paths in a DAG faster than Dijkstra?](#399-how-do-you-find-shortest-paths-in-a-dag-faster-than-dijkstra)
- [400: How do you find the cheapest route with at most k stops?](#400-how-do-you-find-the-cheapest-route-with-at-most-k-stops)
- [401: How do you compute Fibonacci in O(log n)?](#401-how-do-you-compute-fibonacci-in-olog-n)
- [402: Why not use Binet's formula for Fibonacci in JavaScript?](#402-why-not-use-binets-formula-for-fibonacci-in-javascript)
- [403: What are Catalan numbers and where do they show up?](#403-what-are-catalan-numbers-and-where-do-they-show-up)
- [404: How do you compute "n choose k" without overflow?](#404-how-do-you-compute-n-choose-k-without-overflow)
- [405: How do you count inversions in an array?](#405-how-do-you-count-inversions-in-an-array)
- [406: How do you find the maximum product of a subarray?](#406-how-do-you-find-the-maximum-product-of-a-subarray)
- [407: How do you find the minimum window substring that contains all characters of another string?](#407-how-do-you-find-the-minimum-window-substring-that-contains-all-characters-of-another-string)
- [408: How do you count subarrays with exactly K distinct values?](#408-how-do-you-count-subarrays-with-exactly-k-distinct-values)
- [409: What is a difference array?](#409-what-is-a-difference-array)
- [410: How do 2D prefix sums work?](#410-how-do-2d-prefix-sums-work)
- [411: How do you find the prime factors of a number?](#411-how-do-you-find-the-prime-factors-of-a-number)
- [412: Explain amortized analysis using a dynamic array that doubles in size.](#412-explain-amortized-analysis-using-a-dynamic-array-that-doubles-in-size)
- [413: What are the costs of common JavaScript built-ins that people often get wrong?](#413-what-are-the-costs-of-common-javascript-built-ins-that-people-often-get-wrong)
- [414: What are common hidden O(n²) patterns in JavaScript code?](#414-what-are-common-hidden-on²-patterns-in-javascript-code)
- [415: Why is spreading in a reduce accumulator O(n²), and how do you fix it?](#415-why-is-spreading-in-a-reduce-accumulator-on²-and-how-do-you-fix-it)
- [416: How can you guess the expected complexity from the input limits?](#416-how-can-you-guess-the-expected-complexity-from-the-input-limits)
- [417: How do you approach a problem you've never seen before in an interview?](#417-how-do-you-approach-a-problem-youve-never-seen-before-in-an-interview)
- [418: What is property-based testing and how does it help with algorithms?](#418-what-is-property-based-testing-and-how-does-it-help-with-algorithms)
- [419: What are common space-time trade-offs in algorithms?](#419-what-are-common-space-time-trade-offs-in-algorithms)
- [420: How do you add a time limit (TTL) to a memoized function?](#420-how-do-you-add-a-time-limit-ttl-to-a-memoized-function)
- [421: What is the algorithmic cost of immutable updates, and what is structural sharing?](#421-what-is-the-algorithmic-cost-of-immutable-updates-and-what-is-structural-sharing)
- [422: How do persistent data structures like those in Immutable.js work?](#422-how-do-persistent-data-structures-like-those-in-immutablejs-work)
- [423: You need to remove duplicates from 10 million items in the browser. How do you approach it?](#423-you-need-to-remove-duplicates-from-10-million-items-in-the-browser-how-do-you-approach-it)
- [424: How would you find the top 10 most common errors from a huge stream of log events?](#424-how-would-you-find-the-top-10-most-common-errors-from-a-huge-stream-of-log-events)
- [425: What is a Count-Min Sketch?](#425-what-is-a-count-min-sketch)
- [426: What is HyperLogLog?](#426-what-is-hyperloglog)
- [427: How would you build offline autocomplete over 100,000 city names?](#427-how-would-you-build-offline-autocomplete-over-100000-city-names)
- [428: How do you detect circular references between spreadsheet cells and choose the recalculation order?](#428-how-do-you-detect-circular-references-between-spreadsheet-cells-and-choose-the-recalculation-order)
- [429: How do signals (in Angular, Solid, Preact or Vue) decide what to recompute?](#429-how-do-signals-in-angular-solid-preact-or-vue-decide-what-to-recompute)
- [430: How does React's scheduler keep the UI responsive while rendering a big tree?](#430-how-does-reacts-scheduler-keep-the-ui-responsive-while-rendering-a-big-tree)
- [431: What garbage collection algorithms does V8 use, and why should algorithm code care?](#431-what-garbage-collection-algorithms-does-v8-use-and-why-should-algorithm-code-care)
- [432: How are JavaScript Map and Set implemented, and why do they keep insertion order?](#432-how-are-javascript-map-and-set-implemented-and-why-do-they-keep-insertion-order)
- [433: In what order are object keys returned, and why does it matter for algorithms?](#433-in-what-order-are-object-keys-returned-and-why-does-it-matter-for-algorithms)
- [434: Why can some regexes be slow, and are there engines that avoid backtracking?](#434-why-can-some-regexes-be-slow-and-are-there-engines-that-avoid-backtracking)
- [435: How do you make string algorithms work correctly with emoji and accented letters?](#435-how-do-you-make-string-algorithms-work-correctly-with-emoji-and-accented-letters)
- [436: Why do you need Unicode normalization when comparing strings?](#436-why-do-you-need-unicode-normalization-when-comparing-strings)
- [437: Walk through optimizing a slow function from O(n²) to O(n).](#437-walk-through-optimizing-a-slow-function-from-on²-to-on)
- [438: What do you say when an interviewer asks "can you do better?"](#438-what-do-you-say-when-an-interviewer-asks-can-you-do-better)
- [439: How do you design an algorithm to detect when a user has been idle?](#439-how-do-you-design-an-algorithm-to-detect-when-a-user-has-been-idle)
- [440: How would you implement "infinite scroll" without the list getting slower over time?](#440-how-would-you-implement-infinite-scroll-without-the-list-getting-slower-over-time)
- [441: How does a browser engine match CSS selectors efficiently?](#441-how-does-a-browser-engine-match-css-selectors-efficiently)
- [442: How would you implement a simple "diff" for two lines of text to show changes word by word?](#442-how-would-you-implement-a-simple-diff-for-two-lines-of-text-to-show-changes-word-by-word)
- [443: How do you merge many overlapping time ranges coming from different sources efficiently?](#443-how-do-you-merge-many-overlapping-time-ranges-coming-from-different-sources-efficiently)
- [444: How do you pick a random item with weighted probabilities?](#444-how-do-you-pick-a-random-item-with-weighted-probabilities)
- [445: How do you implement consistent hashing, and when would front-end developers meet it?](#445-how-do-you-implement-consistent-hashing-and-when-would-front-end-developers-meet-it)
- [446: How would you detect that two large files are the same (or find changed chunks) in the browser?](#446-how-would-you-detect-that-two-large-files-are-the-same-or-find-changed-chunks-in-the-browser)
- [447: What is the difference between a stable algorithm and a deterministic one, and why do both matter in UIs?](#447-what-is-the-difference-between-a-stable-algorithm-and-a-deterministic-one-and-why-do-both-matter-in-uis)
- [448: How would you implement a scheduler that runs callbacks at the right time when you have thousands of timers?](#448-how-would-you-implement-a-scheduler-that-runs-callbacks-at-the-right-time-when-you-have-thousands-of-timers)
- [449: What should you consider before using a clever algorithm in production front-end code?](#449-what-should-you-consider-before-using-a-clever-algorithm-in-production-front-end-code)
- [450: What is the most important thing to show in an algorithms interview?](#450-what-is-the-most-important-thing-to-show-in-an-algorithms-interview)

---

# Easy Questions (1-150)

## 1: What is an algorithm?

An algorithm is a list of steps that solves a problem. You give it some input, it follows the steps, and it gives you an output. A recipe is a good everyday example. In code, an algorithm can be as small as "find the biggest number in an array" or as big as "find the shortest route between two cities".

## 2: Why should a front-end developer care about algorithms?

Front-end code works with data all the time: filtering lists, sorting tables, searching, walking the DOM tree, grouping items, diffing old and new state. If you pick a slow approach, the page freezes because JavaScript runs on the main thread. Interviews also use algorithm questions to see how you think, how you handle edge cases and how you talk about trade-offs.

## 3: What is Big O notation?

Big O describes how the running time (or memory use) of an algorithm grows when the input gets bigger. It ignores exact numbers like milliseconds and focuses on the growth rate. For example, O(n) means the work grows in a straight line with the input size, and O(n²) means doubling the input makes the work about four times bigger.

## 4: What is the difference between time complexity and space complexity?

Time complexity is about how many steps the algorithm takes as the input grows. Space complexity is about how much extra memory it needs. They are often a trade-off: you can make a lookup faster by storing extra data in a `Map`, which costs memory. When people say "space complexity" they usually mean extra space, not counting the input itself.

## 5: What does O(1) mean? Give an example.

O(1) is constant time. The work doesn't change with the size of the input.

```js
const first = arr[0]; // O(1)
const has = set.has("apple"); // O(1) on average
arr.push(42); // O(1) amortized
```

It doesn't mean "fast", it means "doesn't grow". A constant-time operation can still be slow if it does a lot of fixed work.

## 6: What does O(n) mean? Give an example.

O(n) is linear time. If the input has n items, you do work roughly proportional to n. Looping once over an array is the classic example.

```js
function sum(arr) {
  let total = 0;
  for (const x of arr) total += x;
  return total;
}
```

## 7: What does O(n²) mean? Give an example.

O(n²) is quadratic time. It usually comes from a loop inside a loop over the same data.

```js
function hasDuplicate(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) return true;
    }
  }
  return false;
}
```

With 1,000 items that is about 500,000 comparisons. With 100,000 items it becomes billions, which will freeze a browser tab.

## 8: What does O(log n) mean?

O(log n) means each step cuts the problem down by a constant factor, usually in half. Binary search is the standard example: in a sorted array of 1,000,000 items you need at most about 20 steps to find a value. Logarithmic algorithms stay fast even for huge inputs.

## 9: What does O(n log n) mean?

O(n log n) is the typical cost of good sorting algorithms like merge sort, heap sort and the sort built into JavaScript engines. You can think of it as "do log n levels of work, and each level touches all n items". It is a bit slower than linear but much faster than quadratic for large inputs.

## 10: What is exponential time, O(2ⁿ)?

Exponential time means the work doubles every time the input grows by one. Naive recursive Fibonacci and generating all subsets of a set are examples. These algorithms are fine for n around 20 to 25, but they become unusable very quickly after that.

## 11: What are best case, average case and worst case?

They describe how an algorithm behaves on different inputs of the same size. Linear search finds the item at index 0 in the best case (O(1)), and has to check every item in the worst case (O(n)). Interviewers usually want the worst case unless they say otherwise, because that is what you can promise.

## 12: Why do we drop constants and smaller terms in Big O?

Big O is about growth for large inputs. For O(2n + 10), the "2" and the "+ 10" don't change the shape of the growth, so we write O(n). For O(n² + n), the n² part grows much faster and soon makes the n part irrelevant, so we write O(n²). Constants still matter in practice, but Big O is not meant to show them.

## 13: What is the time complexity of accessing an array element by index?

O(1). JavaScript engines store normal arrays in a continuous block of memory when they can, so `arr[i]` jumps straight to the right slot. Even for "holey" or dictionary-mode arrays, access by index is still treated as constant time on average.

## 14: What is the complexity of push, pop, shift and unshift?

- `push` and `pop` work at the end of the array, so they are O(1) (amortized for `push`).
- `shift` and `unshift` work at the start, so every other element has to move by one position. That makes them O(n).

This is why using `shift()` in a loop to build a queue can get slow with large arrays.

## 15: What is the complexity of includes, indexOf and find?

All of them are O(n) because they may have to check every element until they find a match. Calling one of them inside a loop over another array gives you O(n × m), which is a common hidden performance problem.

## 16: Why is Set.has faster than Array.includes for lookups?

`Set` is backed by a hash table, so `has` is O(1) on average. `Array.includes` scans the array from the start, so it is O(n).

```js
const ids = new Set(users.map((u) => u.id));
const active = orders.filter((o) => ids.has(o.userId)); // O(n + m)
```

If you need to check membership many times, turn the array into a `Set` first.

## 17: What is the complexity of reading a key from an object or a Map?

O(1) on average for both. Objects and Maps are hash-based, so lookup by key doesn't depend on how many keys there are. For algorithm work, `Map` is usually the better choice because keys can be any type, it keeps insertion order, and it is optimized for frequent adds and deletes.

## 18: Is building a string with += inside a loop slow in JavaScript?

In modern engines it is usually fine. V8 uses a structure called a rope (or cons string) so `+=` doesn't copy the whole string every time. In theory, strings are immutable, so naive concatenation could be O(n²), and in older engines it was. Using an array and `join("")` is still a fine and readable option when you build a string from many parts.

## 19: How do you reverse a string?

```js
const reverse = (str) => [...str].reverse().join("");

reverse("hello"); // "olleh"
```

Spreading with `[...str]` splits by code points, so emoji like "😀" don't break. `str.split("")` splits by UTF-16 code units and can break characters made of surrogate pairs. You can also write a loop that goes from the end to the start. All versions are O(n).

## 20: How do you check if a string is a palindrome?

A palindrome reads the same forward and backward. The two-pointer version avoids creating a new string:

```js
function isPalindrome(str) {
  let left = 0;
  let right = str.length - 1;
  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}

isPalindrome("racecar"); // true
```

Time is O(n) and extra space is O(1).

## 21: How do you count the vowels in a string?

```js
function countVowels(str) {
  const vowels = new Set(["a", "e", "i", "o", "u"]);
  let count = 0;
  for (const ch of str.toLowerCase()) {
    if (vowels.has(ch)) count++;
  }
  return count;
}

countVowels("Hello World"); // 3
```

A one-liner with regex also works: `(str.match(/[aeiou]/gi) ?? []).length`.

## 22: How do you find the largest number in an array?

```js
function max(arr) {
  if (arr.length === 0) return undefined;
  let result = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > result) result = arr[i];
  }
  return result;
}
```

`Math.max(...arr)` is shorter, but it returns `-Infinity` for an empty array and can throw a `RangeError` for very large arrays because of the limit on function arguments.

## 23: How do you find both the min and the max in one pass?

```js
function minMax(arr) {
  let min = Infinity;
  let max = -Infinity;
  for (const x of arr) {
    if (x < min) min = x;
    if (x > max) max = x;
  }
  return { min, max };
}
```

One loop is O(n), same as calling `Math.min` and `Math.max` separately, but you only walk the data once.

## 24: How do you sum the numbers in an array?

```js
const sum = arr.reduce((acc, x) => acc + x, 0);
```

Always pass the starting value `0`. Without it, `reduce` throws a `TypeError` on an empty array. A plain `for...of` loop is just as good and some people find it easier to read.

## 25: How do you calculate the average of an array?

```js
function average(arr) {
  if (arr.length === 0) return 0; // or NaN, depending on what you need
  return arr.reduce((acc, x) => acc + x, 0) / arr.length;
}
```

The empty array case is the main thing interviewers look for. Without the check you divide by zero and get `NaN`.

## 26: How do you remove duplicates from an array?

```js
const unique = [...new Set(arr)];
```

This is O(n) and keeps the order of first appearance. It compares values with the SameValueZero rule, so `NaN` is treated as equal to `NaN`, but two different objects with the same content are not duplicates. For objects you need to dedupe by a key (see the question about unique objects by id).

## 27: How do you count how many times each element appears?

Use a `Map` (or an object) as a frequency counter:

```js
function countItems(arr) {
  const counts = new Map();
  for (const item of arr) {
    counts.set(item, (counts.get(item) ?? 0) + 1);
  }
  return counts;
}

countItems(["a", "b", "a"]); // Map { "a" => 2, "b" => 1 }
```

This is O(n) time and O(k) space, where k is the number of distinct values.

## 28: What is linear search?

Linear search checks each element one by one until it finds the target or reaches the end.

```js
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i;
  }
  return -1;
}
```

It is O(n) and works on any array, sorted or not. `indexOf` and `includes` do the same thing.

## 29: What is binary search and how do you write it?

Binary search finds a value in a sorted array by checking the middle element and throwing away the half that can't contain the target.

```js
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) low = mid + 1;
    else high = mid - 1;
  }
  return -1;
}
```

It runs in O(log n) time and O(1) space.

## 30: What does binary search require, and what happens if you ignore it?

The array must be sorted by the same rule you use to compare. If it isn't, binary search can skip over the target and return `-1` even though the value is there. If you need to search an unsorted array only once, sorting first (O(n log n)) is slower than a plain linear search (O(n)). Sorting pays off only when you search many times.

## 31: How do you solve FizzBuzz?

Print numbers from 1 to n, but "Fizz" for multiples of 3, "Buzz" for multiples of 5 and "FizzBuzz" for both.

```js
for (let i = 1; i <= 100; i++) {
  let out = "";
  if (i % 3 === 0) out += "Fizz";
  if (i % 5 === 0) out += "Buzz";
  console.log(out || i);
}
```

Building the string piece by piece avoids a separate check for 15.

## 32: How do you calculate a factorial?

```js
// iterative
function factorial(n) {
  let result = 1;
  for (let i = 2; i <= n; i++) result *= i;
  return result;
}

// recursive
const factorialRec = (n) => (n <= 1 ? 1 : n * factorialRec(n - 1));
```

Both are O(n). Results above `170!` become `Infinity`, and anything above `18!` is bigger than `Number.MAX_SAFE_INTEGER`, so it loses precision. Use `BigInt` if you need exact large values.

## 33: How do you write Fibonacci recursively?

```js
function fib(n) {
  if (n < 2) return n;
  return fib(n - 1) + fib(n - 2);
}

fib(10); // 55
```

It matches the math definition, which is why interviewers like it as a starting point. The next question is usually why it is slow.

## 34: Why is the naive recursive Fibonacci slow?

Each call makes two more calls, and the same values get calculated again and again. `fib(5)` calls `fib(3)` twice, `fib(2)` three times and so on. The number of calls grows roughly like 2ⁿ (more exactly about 1.6ⁿ). `fib(45)` already takes seconds. You fix it with memoization or with a loop.

## 35: How do you write Fibonacci in O(n) time and O(1) space?

```js
function fib(n) {
  let a = 0;
  let b = 1;
  for (let i = 0; i < n; i++) {
    [a, b] = [b, a + b];
  }
  return a;
}
```

You only keep the last two values, so memory stays constant. For n above 78 the result goes past `Number.MAX_SAFE_INTEGER`, so switch to `BigInt` (`0n`, `1n`) if you need exact values.

## 36: What is recursion?

Recursion is when a function calls itself to solve a smaller version of the same problem. Every recursive function needs a base case that stops the calls and a recursive case that moves toward the base case. It fits naturally with tree-shaped data like the DOM, nested comments or folder structures.

## 37: What is a base case and what happens if you forget it?

The base case is the condition where the function returns without calling itself again. Without it, or if the recursive call never gets closer to it, the function keeps calling itself until the call stack is full. Then JavaScript throws `RangeError: Maximum call stack size exceeded`.

## 38: What is the maximum recursion depth in JavaScript?

There is no fixed number in the spec. It depends on the engine, the stack size and how much each call stores. In Chrome and Node.js it is usually around 10,000 frames, but it can be less if each frame has many local variables. If your input can be very deep (a big linked list, a deeply nested JSON), use a loop with your own stack instead of recursion.

## 39: Recursion or iteration: which should you use?

Recursion is often shorter and clearer for trees, graphs and divide-and-conquer problems. Iteration avoids stack overflow and the overhead of function calls, so it is safer for long linear processes. Any recursive algorithm can be rewritten as a loop with an explicit stack. In interviews, write whichever is clearer and mention the depth limit if the input can be large.

## 40: How do you reverse an array in place?

Swap elements from both ends moving toward the middle:

```js
function reverseInPlace(arr) {
  let i = 0;
  let j = arr.length - 1;
  while (i < j) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
    i++;
    j--;
  }
  return arr;
}
```

O(n) time, O(1) extra space. This is what `arr.reverse()` does for you.

## 41: What is the difference between reverse() and toReversed()?

`reverse()` changes the original array. `toReversed()` (ES2023) returns a new reversed array and leaves the original alone.

```js
const a = [1, 2, 3];
const b = a.toReversed(); // [3, 2, 1], a is still [1, 2, 3]
a.reverse(); // a is now [3, 2, 1]
```

The same pair exists for sorting and splicing: `sort()`/`toSorted()` and `splice()`/`toSpliced()`. The non-mutating versions are handy with React or other state that should not be changed directly.

## 42: Why does [10, 9, 1, 2].sort() give a strange result?

Without a comparator, `sort()` converts items to strings and compares them by UTF-16 code units. So `"10"` comes before `"2"` because `"1"` is smaller than `"2"`.

```js
[10, 9, 1, 2].sort(); // [1, 10, 2, 9]
```

This is one of the most common JavaScript gotchas in interviews.

## 43: How do you sort numbers correctly?

Pass a comparator that returns a negative number, zero or a positive number:

```js
nums.sort((a, b) => a - b); // ascending
nums.sort((a, b) => b - a); // descending
```

If the result is negative, `a` goes first. If positive, `b` goes first. If zero, their order stays the same.

## 44: Is Array.prototype.sort stable?

Yes. Since ES2019 the spec requires `sort` to be stable, and all modern engines follow it. Stable means items that compare as equal keep their original order. That lets you sort by one key and then by another and get a correct multi-level order.

## 45: What is toSorted() and when would you use it?

`toSorted()` (ES2023) works like `sort()` but returns a new array instead of changing the original.

```js
const sorted = prices.toSorted((a, b) => a - b);
```

Use it when the original array is shared or is part of state, for example in React where you shouldn't mutate state. Before ES2023, people wrote `[...arr].sort(...)` to get the same result.

## 46: How do you sort an array of objects by a property?

```js
const users = [
  { name: "Ana", age: 31 },
  { name: "Ben", age: 25 },
];

users.toSorted((a, b) => a.age - b.age); // by number
users.toSorted((a, b) => a.name.localeCompare(b.name)); // by string
```

Use subtraction for numbers and `localeCompare` for strings. Don't return `a.age > b.age`, because a boolean is not a valid comparator result.

## 47: Why use localeCompare for sorting strings?

The default comparison uses code unit values, so `"Z"` comes before `"a"` and accented letters end up in odd places. `localeCompare` sorts the way people expect in a given language.

```js
["b", "Z", "é", "a"].sort(); // ["Z", "a", "b", "é"]
["b", "Z", "é", "a"].sort((a, b) => a.localeCompare(b)); // ["a", "b", "é", "Z"]

["file10", "file2"].sort((a, b) =>
  a.localeCompare(b, undefined, { numeric: true }),
); // ["file2", "file10"]
```

The `numeric: true` option gives you "natural" sorting of numbers inside strings.

## 48: How does bubble sort work?

Bubble sort walks through the array and swaps neighbors that are in the wrong order. After each pass the largest remaining item "bubbles" to the end.

```js
function bubbleSort(arr) {
  for (let end = arr.length - 1; end > 0; end--) {
    let swapped = false;
    for (let i = 0; i < end; i++) {
      if (arr[i] > arr[i + 1]) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
        swapped = true;
      }
    }
    if (!swapped) break; // already sorted
  }
  return arr;
}
```

It is O(n²) in the average and worst case and O(n) on already sorted input thanks to the `swapped` flag. It's only used for teaching.

## 49: How does selection sort work?

Selection sort finds the smallest item in the unsorted part and swaps it into place at the front.

```js
function selectionSort(arr) {
  for (let i = 0; i < arr.length - 1; i++) {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) min = j;
    }
    if (min !== i) [arr[i], arr[min]] = [arr[min], arr[i]];
  }
  return arr;
}
```

It is always O(n²), even if the input is already sorted, and it is not stable. Its one advantage is that it does at most n − 1 swaps.

## 50: How does insertion sort work?

Insertion sort builds a sorted part on the left. It takes the next item and shifts larger items to the right until it finds the right spot.

```js
function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    const current = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > current) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = current;
  }
  return arr;
}
```

O(n²) worst case, O(n) best case, stable and in place.

## 51: When is insertion sort a good choice?

It is fast for small arrays and for arrays that are almost sorted, because each item only moves a short distance. That is why real sorting algorithms like TimSort use insertion sort for small chunks. It also works well when items arrive one at a time and you need to keep a list sorted.

## 52: What does it mean for a sort to be stable?

A stable sort keeps equal items in the same order they had before sorting. Say you have a list already sorted by name and you sort it by department. With a stable sort, people inside each department are still sorted by name. Merge sort, insertion sort and the built-in `Array.prototype.sort` are stable. Quick sort, heap sort and selection sort usually are not.

## 53: What is an in-place algorithm?

An in-place algorithm changes the input directly and uses only a small, constant amount of extra memory (or O(log n) for some recursive ones). Reversing an array by swapping ends and insertion sort are in place. Merge sort usually isn't, because it needs a temporary array. In-place saves memory but destroys the original data, which can be a problem if other code still uses it.

## 54: How do you check if two strings are anagrams?

Two strings are anagrams if they have the same letters with the same counts. Count the letters of one string, then subtract with the other:

```js
function isAnagram(a, b) {
  if (a.length !== b.length) return false;
  const counts = new Map();
  for (const ch of a) counts.set(ch, (counts.get(ch) ?? 0) + 1);
  for (const ch of b) {
    const c = counts.get(ch);
    if (!c) return false;
    counts.set(ch, c - 1);
  }
  return true;
}
```

This is O(n). Sorting both strings and comparing also works but is O(n log n).

## 55: How do you capitalize the first letter of each word?

```js
function titleCase(str) {
  return str
    .split(" ")
    .map((w) => (w ? w[0].toUpperCase() + w.slice(1).toLowerCase() : w))
    .join(" ");
}

titleCase("hello wORLD"); // "Hello World"
```

The check for empty `w` handles double spaces. Ask the interviewer whether the rest of each word should be lowercased, because that is a requirement, not an obvious default.

## 56: How do you find the longest word in a sentence?

```js
function longestWord(sentence) {
  let longest = "";
  for (const word of sentence.split(/\s+/)) {
    if (word.length > longest.length) longest = word;
  }
  return longest;
}
```

Splitting on `/\s+/` handles several spaces in a row. If punctuation should be ignored, clean it first with something like `word.replace(/[^\p{L}\p{N}]/gu, "")`.

## 57: How do you count the words in a string?

```js
const countWords = (str) => str.trim().split(/\s+/).filter(Boolean).length;

countWords("  hello   big world "); // 3
```

`trim()` and the `filter(Boolean)` handle extra spaces and the empty string. For real multilingual text, `Intl.Segmenter` with `granularity: "word"` is more accurate.

## 58: How do you check if a string contains only digits?

```js
const isDigits = (str) => /^\d+$/.test(str);

isDigits("12345"); // true
isDigits("12a45"); // false
isDigits(""); // false
```

`^` and `$` make the regex match the whole string. Don't use `!isNaN(str)`, because it accepts things like `" "`, `"1e3"` and `"0x1f"`.

## 59: How do you truncate a string and add "..."?

```js
function truncate(str, max) {
  return str.length > max ? str.slice(0, max - 3) + "..." : str;
}

truncate("Hello world", 8); // "Hello..."
```

Ask whether `max` includes the dots. In UI code, CSS `text-overflow: ellipsis` is often a better tool than doing this in JavaScript.

## 60: How do you repeat a string n times?

```js
"ab".repeat(3); // "ababab"
```

If asked to write it by hand, a loop that appends is fine. A faster trick doubles the string, which needs only O(log n) concatenations:

```js
function repeat(str, n) {
  let result = "";
  while (n > 0) {
    if (n & 1) result += str;
    str += str;
    n >>= 1;
  }
  return result;
}
```

## 61: What is the two-pointer technique?

You keep two indexes into the data and move them based on some rule, instead of using nested loops. Common setups are one pointer at each end moving toward the middle (palindrome check, pair sum in a sorted array) or a slow and a fast pointer moving the same way (removing duplicates in place). It often turns an O(n²) solution into O(n).

## 62: How do you check if an array is sorted?

```js
function isSorted(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] > arr[i]) return false;
  }
  return true;
}
```

Compare each item with the one before it. It is O(n) and returns early on the first problem. Empty and one-item arrays count as sorted.

## 63: How do you merge two sorted arrays into one sorted array?

Use two pointers and always take the smaller current item:

```js
function mergeSorted(a, b) {
  const result = [];
  let i = 0;
  let j = 0;
  while (i < a.length && j < b.length) {
    result.push(a[i] <= b[j] ? a[i++] : b[j++]);
  }
  while (i < a.length) result.push(a[i++]);
  while (j < b.length) result.push(b[j++]);
  return result;
}
```

This is O(n + m). Using `<=` keeps it stable. `[...a, ...b].sort()` works too but is O((n + m) log(n + m)) and ignores the fact that the inputs are already sorted.

## 64: How do you find the second largest number in an array?

```js
function secondLargest(arr) {
  let first = -Infinity;
  let second = -Infinity;
  for (const x of arr) {
    if (x > first) {
      second = first;
      first = x;
    } else if (x > second && x < first) {
      second = x;
    }
  }
  return second === -Infinity ? undefined : second;
}
```

One pass, O(n). The `x < first` check skips duplicates of the max, so `[5, 5, 3]` returns `3`. Ask the interviewer if duplicates should count.

## 65: How do you split an array into chunks of a given size?

```js
function chunk(arr, size) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```

O(n) time. This comes up when you send items to an API in batches or render a grid row by row.

## 66: How do you flatten a nested array?

```js
[1, [2, [3, [4]]]].flat(); // [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat(Infinity); // [1, 2, 3, 4]
```

`flat()` goes one level deep by default. Pass a number for more levels or `Infinity` for all of them. `flatMap()` maps and then flattens one level, which is useful when each item turns into zero or more items.

## 67: How do you flatten an array without flat()?

```js
function flatten(arr) {
  const result = [];
  for (const item of arr) {
    if (Array.isArray(item)) result.push(...flatten(item));
    else result.push(item);
  }
  return result;
}
```

This is the usual recursive answer. For very deep nesting you can hit the stack limit, and spreading huge sub-arrays into `push` can hit the argument limit. An iterative version with an explicit stack avoids both.

## 68: How do you find the intersection of two arrays?

```js
function intersection(a, b) {
  const setB = new Set(b);
  return [...new Set(a)].filter((x) => setB.has(x));
}

intersection([1, 2, 2, 3], [2, 3, 4]); // [2, 3]
```

O(n + m) thanks to the `Set`. The naive `a.filter((x) => b.includes(x))` is O(n × m). With ES2025 you can also write `new Set(a).intersection(new Set(b))`.

## 69: How do you find the difference between two arrays?

Items that are in `a` but not in `b`:

```js
function difference(a, b) {
  const setB = new Set(b);
  return a.filter((x) => !setB.has(x));
}
```

For the symmetric difference (items in only one of the two arrays), do it both ways and combine, or use `setA.symmetricDifference(setB)` in ES2025.

## 70: How do you get the union of two arrays?

```js
const union = [...new Set([...a, ...b])];
```

This keeps one copy of each value in order of first appearance. With ES2025 Set methods: `new Set(a).union(new Set(b))`.

## 71: How do you find the missing number in an array of 1 to n?

The sum of 1 to n is `n * (n + 1) / 2`. Subtract the actual sum:

```js
function missingNumber(arr) {
  const n = arr.length + 1;
  const expected = (n * (n + 1)) / 2;
  const actual = arr.reduce((s, x) => s + x, 0);
  return expected - actual;
}

missingNumber([1, 2, 4, 5]); // 3
```

O(n) time, O(1) space. For very large n you could overflow safe integers, and the XOR trick (XOR all numbers 1..n with all array items) avoids that.

## 72: How do you find a duplicate in an array?

```js
function findDuplicate(arr) {
  const seen = new Set();
  for (const x of arr) {
    if (seen.has(x)) return x;
    seen.add(x);
  }
  return undefined;
}
```

O(n) time and O(n) space. If the array has n + 1 numbers in the range 1..n and you can't use extra space, Floyd's cycle detection solves it in O(1) space, but that is a harder follow-up.

## 73: How do you rotate an array by k positions?

```js
const rotateRight = (arr, k) => {
  if (arr.length === 0) return [];
  k %= arr.length;
  return [...arr.slice(-k), ...arr.slice(0, -k)];
};

rotateRight([1, 2, 3, 4, 5], 2); // [4, 5, 1, 2, 3]
```

The modulo handles `k` bigger than the length. When `k` is 0, `slice(-0)` returns the whole array and `slice(0, -0)` returns an empty one, so the result is still correct. The in-place version reverses the whole array, then reverses the first k items and the rest separately. That uses O(1) extra space.

## 74: How do you move all zeros to the end while keeping the order of other items?

```js
function moveZeros(arr) {
  let write = 0;
  for (let read = 0; read < arr.length; read++) {
    if (arr[read] !== 0) arr[write++] = arr[read];
  }
  while (write < arr.length) arr[write++] = 0;
  return arr;
}
```

A slow pointer (`write`) marks where the next non-zero goes and a fast pointer (`read`) scans. O(n) time, O(1) space, in place.

## 75: What is the Two Sum problem and what is the brute-force solution?

Given an array and a target, return the indexes of two numbers that add up to the target. The brute-force way checks every pair:

```js
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
  return null;
}
```

It's O(n²). It is a fine first answer if you say so and then improve it.

## 76: How do you solve Two Sum in O(n)?

Store each number's index in a `Map` and look for the complement as you go:

```js
function twoSum(nums, target) {
  const seen = new Map(); // value -> index
  for (let i = 0; i < nums.length; i++) {
    const need = target - nums[i];
    if (seen.has(need)) return [seen.get(need), i];
    seen.set(nums[i], i);
  }
  return null;
}
```

One pass, O(n) time and O(n) space. Checking before inserting stops you from using the same item twice.

## 77: What is the frequency counter pattern?

You build a map of counts for one input, then use it to answer questions in one more pass. It replaces nested loops with two separate loops, so O(n²) becomes O(n). Anagram checks, "first non-repeating character", "most frequent element" and "can you build string A from the letters of string B" all use it.

## 78: How do you check if a number is prime?

```js
function isPrime(n) {
  if (n < 2) return false;
  if (n % 2 === 0) return n === 2;
  for (let i = 3; i * i <= n; i += 2) {
    if (n % i === 0) return false;
  }
  return true;
}
```

You only need to test divisors up to √n, because if n = a × b then one of them is at most √n. Skipping even numbers halves the work. This is O(√n).

## 79: What is the Sieve of Eratosthenes?

It finds all primes up to n by crossing out multiples of each prime.

```js
function primesUpTo(n) {
  const isPrime = new Uint8Array(n + 1).fill(1);
  isPrime[0] = isPrime[1] = 0;
  for (let i = 2; i * i <= n; i++) {
    if (isPrime[i]) {
      for (let j = i * i; j <= n; j += i) isPrime[j] = 0;
    }
  }
  const primes = [];
  for (let i = 2; i <= n; i++) if (isPrime[i]) primes.push(i);
  return primes;
}
```

It runs in O(n log log n) and is much faster than checking each number separately. A `Uint8Array` uses less memory than a normal array of booleans.

## 80: How do you find the greatest common divisor (GCD)?

Use Euclid's algorithm: the GCD of a and b is the same as the GCD of b and `a % b`.

```js
function gcd(a, b) {
  while (b !== 0) [a, b] = [b, a % b];
  return Math.abs(a);
}

gcd(48, 18); // 6
```

It runs in O(log(min(a, b))) steps.

## 81: How do you find the least common multiple (LCM)?

```js
const lcm = (a, b) => (a === 0 || b === 0 ? 0 : Math.abs((a / gcd(a, b)) * b));

lcm(4, 6); // 12
```

Divide before multiplying (`a / gcd * b`) so the middle result stays smaller and you are less likely to go past safe integer range.

## 82: How do you sum the digits of a number?

```js
function sumDigits(n) {
  n = Math.abs(n);
  let sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
}

sumDigits(1234); // 10
```

A string version also works: `[...String(Math.abs(n))].reduce((s, d) => s + Number(d), 0)`. The math version avoids creating strings.

## 83: How do you reverse the digits of an integer?

```js
function reverseInt(n) {
  const reversed = Number(String(Math.abs(n)).split("").reverse().join(""));
  return Math.sign(n) * reversed;
}

reverseInt(-123); // -321
reverseInt(120); // 21
```

Handle the sign separately, and know that trailing zeros disappear. Some versions of this question also ask you to return 0 if the result goes outside the 32-bit integer range.

## 84: How do you check if a number is a palindrome without converting it to a string?

```js
function isNumberPalindrome(n) {
  if (n < 0) return false;
  let original = n;
  let reversed = 0;
  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return original === reversed;
}
```

Negative numbers aren't palindromes because of the minus sign. The string version `String(n) === [...String(n)].reverse().join("")` is fine unless the interviewer forbids it.

## 85: How do you check if a number is a power of two?

```js
const isPowerOfTwo = (n) => n > 0 && (n & (n - 1)) === 0;

isPowerOfTwo(16); // true
isPowerOfTwo(18); // false
```

A power of two has exactly one bit set. Subtracting 1 flips that bit and sets all lower bits, so `n & (n - 1)` is 0. Bitwise operators in JavaScript convert numbers to 32-bit integers, so only trust this for numbers below 2³¹. For bigger numbers use `Number.isInteger(Math.log2(n))`.

## 86: How do you check if a number is even or odd?

```js
const isEven = (n) => n % 2 === 0;
const isOdd = (n) => n % 2 !== 0;
```

Don't write `n % 2 === 1` for odd, because `-3 % 2` is `-1` in JavaScript. `(n & 1) === 1` also works for integers in 32-bit range, but `%` is clearer and just as fast in practice.

## 87: How do you swap two variables without a temp variable?

```js
let a = 1;
let b = 2;
[a, b] = [b, a];
```

Array destructuring is the modern way and also works for array items: `[arr[i], arr[j]] = [arr[j], arr[i]]`. You might be asked about the XOR or arithmetic tricks (`a = a + b; b = a - b; a = a - b`), but they are harder to read and the arithmetic one can lose precision with large numbers.

## 88: How do you create an array of numbers from 1 to n?

```js
const range = Array.from({ length: n }, (_, i) => i + 1);
// or
const range2 = [...Array(n).keys()].map((i) => i + 1);
```

`Array.from` with a length object and a mapping function is the most common way. A plain `for` loop with `push` is also fine.

## 89: How do you shuffle an array correctly?

Use the Fisher-Yates (Knuth) shuffle. Go from the end and swap each item with a random item at or before it:

```js
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
```

It runs in O(n) and every order is equally likely.

## 90: Why is arr.sort(() => Math.random() - 0.5) a bad way to shuffle?

Sorting algorithms expect a comparator that is consistent: if a < b now, it should still be true later. A random comparator breaks that rule, so the result depends on how the engine's sort works and is not uniform. Some orders come up much more often than others. It is also O(n log n) instead of O(n). Use Fisher-Yates.

## 91: How do you get a random integer between min and max?

```js
function randomInt(min, max) {
  // includes both min and max
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
```

`Math.random()` returns a number in `[0, 1)`, so multiplying by the size of the range and flooring gives an even spread. Using `Math.round` instead of `Math.floor` is a common bug, because it makes the two end values half as likely as the others.

## 92: Is chaining map, filter and reduce slower than one loop?

Each method walks the array again and `map` and `filter` create new arrays. So `arr.filter(...).map(...).reduce(...)` does three passes and allocates two temporary arrays. It is still O(n) in total, and for normal UI data sizes the difference doesn't matter. For very large arrays or hot code paths, one `for` loop (or iterator helpers, which are lazy) can be noticeably faster.

## 93: What is the difference between for, for...of and forEach when writing algorithms?

- `for (let i = 0; ...)` gives you the index and lets you `break`, `continue` and jump around.
- `for...of` is cleaner when you only need values, and also supports `break` and `continue`. It works with any iterable: arrays, strings, `Map`, `Set`.
- `forEach` can't be stopped early (except by throwing) and doesn't work with `await` the way people expect.

For algorithms that need early exit, prefer `for` or `for...of`.

## 94: How do some, every and find help you exit early?

They stop as soon as they know the answer. `some` stops at the first `true`, `every` stops at the first `false`, and `find`/`findIndex` stop at the first match.

```js
const hasNegative = nums.some((n) => n < 0);
const allValid = forms.every((f) => f.valid);
const admin = users.find((u) => u.role === "admin");
```

They are still O(n) in the worst case, but they often do much less work than `filter(...).length > 0`.

## 95: How do you use an array as a stack?

A stack is last in, first out (LIFO). Use `push` to add and `pop` to remove from the end. Both are O(1).

```js
const stack = [];
stack.push(1);
stack.push(2);
stack.pop(); // 2
stack.at(-1); // 1, peek without removing
```

Stacks show up in undo history, matching brackets, the browser back button and turning recursion into a loop.

## 96: How do you use an array as a queue, and what is the problem with it?

A queue is first in, first out (FIFO). With an array you `push` to add and `shift` to remove from the front.

```js
const queue = [];
queue.push("a");
queue.push("b");
queue.shift(); // "a"
```

The problem is that `shift` is O(n), because all the other items move down. For small queues it doesn't matter. For BFS on a big graph, use a head index or a proper queue class instead.

## 97: How do you check if brackets in a string are balanced?

Push opening brackets on a stack and pop when you see a closing one:

```js
function isValid(str) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];
  for (const ch of str) {
    if (ch === "(" || ch === "[" || ch === "{") stack.push(ch);
    else if (ch in pairs) {
      if (stack.pop() !== pairs[ch]) return false;
    }
  }
  return stack.length === 0;
}

isValid("{[()]}"); // true
isValid("([)]"); // false
```

O(n) time and O(n) space. Don't forget the final check: `"(("` has no mismatch but is still not balanced.

## 98: What is a linked list?

A linked list is a chain of nodes where each node holds a value and a reference to the next node. Adding or removing at the head is O(1), but finding the i-th item is O(n) because you have to walk from the start. JavaScript has no built-in linked list, so you build one with objects like `{ value, next }`. In interviews it is mostly used to test pointer handling.

## 99: What is a hash table?

A hash table stores key-value pairs. A hash function turns each key into an index in an internal array, so lookups, inserts and deletes are O(1) on average. When two keys land on the same index (a collision), the table handles it with chaining or probing. In JavaScript, `Map`, `Set` and plain objects are all built on hash tables.

## 100: When should you use a Map instead of a plain object in algorithms?

Use `Map` when:

- keys are not strings (numbers stay numbers, objects can be keys)
- you add and remove keys a lot
- you need the size (`map.size`) or insertion order
- keys come from user input (an object key like `"__proto__"` or `"constructor"` can cause bugs)

Plain objects are fine for fixed, known string keys, like a lookup table of brackets.

## 101: What is a tree?

A tree is a structure made of nodes, where each node has a value and a list of children, and there are no cycles. There is one root at the top. The DOM, a file system, nested comments and a JSON object are all trees. Many tree algorithms are recursive because each child is itself the root of a smaller tree.

## 102: What is the difference between a binary tree and a binary search tree?

A binary tree is any tree where each node has at most two children (left and right). A binary search tree (BST) adds a rule: every value in the left subtree is smaller than the node, and every value in the right subtree is larger. That rule lets you search, insert and delete in O(log n) when the tree is balanced, but it can drop to O(n) if the tree turns into a long chain.

## 103: What are the main ways to traverse a tree?

- **Depth-first (DFS):** go as deep as possible before backing up. For binary trees there are three orders: preorder (node, left, right), inorder (left, node, right) and postorder (left, right, node).
- **Breadth-first (BFS)** or level order: visit all nodes at depth 0, then depth 1, and so on, using a queue.

An inorder traversal of a BST gives the values in sorted order.

## 104: What is a graph?

A graph is a set of nodes (vertices) connected by edges. Edges can be directed (one way, like "A follows B") or undirected (both ways, like a friendship), and can have weights (like distance). Unlike a tree, a graph can have cycles and doesn't need a root. Social networks, road maps and module dependency graphs are all graphs.

## 105: What is the difference between BFS and DFS?

BFS explores neighbors level by level using a queue. It finds the shortest path in an unweighted graph. DFS goes deep along one path before backtracking, using recursion or a stack. It is good for detecting cycles, topological sorting and exploring all paths. Both visit every node and edge once, so both are O(V + E).

## 106: What is a greedy algorithm?

A greedy algorithm makes the choice that looks best right now at each step and never goes back. It is usually simple and fast. It works only for problems where local best choices lead to the global best result, like making change with standard coin values or picking the most non-overlapping meetings. For other problems it gives wrong answers, so you need to check that greedy actually works.

## 107: What is divide and conquer?

You split a problem into smaller parts of the same kind, solve each part (often recursively), and combine the results. Merge sort splits an array in half, sorts each half and merges them. Binary search is a simpler case that only needs to solve one of the halves. It often leads to O(n log n) or O(log n) algorithms.

## 108: What is dynamic programming?

Dynamic programming (DP) solves problems that break into overlapping subproblems. Instead of solving the same subproblem many times, you solve each one once and store the result. You can do it top-down with recursion plus a cache (memoization) or bottom-up by filling a table. Fibonacci, climbing stairs, coin change and longest common subsequence are classic DP problems.

## 109: What is memoization?

Memoization means caching the result of a function call so the next call with the same input returns the cached value.

```js
function fib(n, memo = new Map()) {
  if (n < 2) return n;
  if (memo.has(n)) return memo.get(n);
  const result = fib(n - 1, memo) + fib(n - 2, memo);
  memo.set(n, result);
  return result;
}
```

This turns Fibonacci from about O(2ⁿ) to O(n). It only works for pure functions, where the same input always gives the same output.

## 110: What is a brute-force solution and is it ever a good answer?

Brute force tries all possibilities, like checking every pair in Two Sum. It is usually slow, but it is easy to get right. In an interview it's a good first step: say it out loud, give its complexity, and then improve it. In real code, brute force is often fine when the input is small, like a list of 20 menu items.

## 111: How should you approach an algorithm question in an interview?

1. Repeat the problem in your own words and ask about inputs, outputs and limits.
2. Go through one or two examples by hand, including an edge case.
3. Describe a simple solution and its complexity.
4. Improve it if needed, and explain why the new version is better.
5. Write the code while talking through it.
6. Test it with your examples and edge cases.

Talking while you work matters as much as the final code.

## 112: What edge cases should you check for in algorithm problems?

Common ones are: empty input (`[]`, `""`), a single element, all elements the same, negative numbers and zero, duplicates, already sorted or reverse sorted input, very large input, `null` or `undefined`, and for strings, uppercase/lowercase, spaces and Unicode characters like emoji. Mentioning them before you write code shows the interviewer you think about real data.

## 113: How do you quickly test an algorithm in JavaScript?

For a quick check, write a few asserts:

```js
console.assert(isPalindrome("racecar") === true, "racecar");
console.assert(isPalindrome("") === true, "empty");
console.assert(isPalindrome("ab") === false, "ab");
```

In a project, write unit tests with Vitest, Jest or the built-in `node:test` runner. For algorithms it also helps to compare your fast version against a slow brute-force version on many random inputs.

## 114: Why does 0.1 + 0.2 !== 0.3, and why does it matter for algorithms?

JavaScript numbers are 64-bit floating point (IEEE 754), and values like 0.1 can't be stored exactly in binary. So `0.1 + 0.2` gives `0.30000000000000004`. In algorithms this breaks equality checks with decimals, money sums and geometry. Compare with a small tolerance (`Math.abs(a - b) < Number.EPSILON`, or a tolerance that fits your data), or work in whole units like cents.

## 115: What is Number.MAX_SAFE_INTEGER and when do you need BigInt?

`Number.MAX_SAFE_INTEGER` is 2⁵³ − 1 (9,007,199,254,740,991). Above it, not every integer can be stored exactly, so `2 ** 53 + 1 === 2 ** 53` is `true`. If your algorithm works with large integers, like big factorials, Fibonacci past n = 78 or large IDs, use `BigInt`:

```js
const big = 2n ** 64n; // 18446744073709551616n
```

You can't mix `BigInt` and `Number` in math without converting.

## 116: What is the difference between Math.floor and Math.trunc for integer division?

Both drop the decimal part, but they differ for negative numbers. `Math.floor` rounds down toward negative infinity, `Math.trunc` cuts toward zero.

```js
Math.floor(-7 / 2); // -4
Math.trunc(-7 / 2); // -3
```

For a binary search midpoint with non-negative indexes, both give the same result. The trick `(a / b) | 0` also truncates but only for 32-bit values.

## 117: How does the % operator work with negative numbers?

In JavaScript, `%` is a remainder, not a true modulo. The result has the same sign as the left side.

```js
-7 % 3; // -1, not 2
```

If you need a value that is always between 0 and n − 1, for example when wrapping an index in a circular list, use `((x % n) + n) % n`.

## 118: What is the difference between charCodeAt and codePointAt?

`charCodeAt(i)` returns the UTF-16 code unit at index i (0 to 65535). `codePointAt(i)` returns the full Unicode code point, which can be bigger for characters like emoji that use two code units.

```js
"A".charCodeAt(0); // 65
"😀".charCodeAt(0); // 55357 (half of a surrogate pair)
"😀".codePointAt(0); // 128512
```

Algorithms like Caesar cipher or "count letter frequencies with an array of 26" often use `charCodeAt(i) - 97` to map `a` to 0.

## 119: Can you change a character in a JavaScript string directly?

No. Strings are immutable, so `str[0] = "X"` does nothing (and throws in strict mode). You have to build a new string, for example with `slice`, or convert the string to an array, change it, and `join` it back.

```js
const chars = [...str];
chars[0] = "X";
const result = chars.join("");
```

Keep this in mind when an algorithm says "in place" on a string. In JavaScript you always need an array for that.

## 120: Why can splitting a string with split("") break emoji?

`split("")` splits by UTF-16 code units. Characters outside the basic range, like emoji, are stored as two code units, so they get cut in half.

```js
"a😀".split(""); // ["a", "\ud83d", "\ude00"]
[..."a😀"]; // ["a", "😀"]
```

Spread and `for...of` split by code points. Even that is not perfect for combined emoji like 👨‍👩‍👧 or flags. For what users see as one character, use `Intl.Segmenter`.

## 121: How do you check if two arrays are equal?

`===` only checks if both variables point to the same array. To compare contents:

```js
function arraysEqual(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) {
    if (!Object.is(a[i], b[i])) return false;
  }
  return true;
}
```

This is a shallow comparison, O(n). `JSON.stringify(a) === JSON.stringify(b)` is a quick hack but fails for `undefined`, `NaN`, functions and objects with different key order.

## 122: How do you compare two objects shallowly?

```js
function shallowEqual(a, b) {
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(
    (key) => Object.hasOwn(b, key) && Object.is(a[key], b[key]),
  );
}
```

React uses this kind of check to decide whether props changed in `memo`. It is O(k) where k is the number of keys, and it doesn't look inside nested objects.

## 123: What is the difference between find, findIndex, findLast and findLastIndex?

`find` returns the first matching item, `findIndex` returns its index (or `-1`). `findLast` and `findLastIndex` (ES2023) search from the end.

```js
const logs = [
  { level: "error", id: 1 },
  { level: "info", id: 2 },
  { level: "error", id: 3 },
];
logs.findLast((l) => l.level === "error"); // { level: "error", id: 3 }
logs.findLastIndex((l) => l.level === "error"); // 2
```

Before ES2023 you had to reverse a copy of the array or write a backwards loop.

## 124: How do you find the first non-repeating character in a string?

Count first, then scan again in the original order:

```js
function firstUnique(str) {
  const counts = new Map();
  for (const ch of str) counts.set(ch, (counts.get(ch) ?? 0) + 1);
  for (const ch of str) {
    if (counts.get(ch) === 1) return ch;
  }
  return null;
}

firstUnique("swiss"); // "w"
```

Two passes, O(n) time. A nested loop would be O(n²).

## 125: How do you find the longest run of the same value in an array?

```js
function longestStreak(arr) {
  if (arr.length === 0) return 0;
  let best = 1;
  let current = 1;
  for (let i = 1; i < arr.length; i++) {
    current = arr[i] === arr[i - 1] ? current + 1 : 1;
    best = Math.max(best, current);
  }
  return best;
}

longestStreak([1, 1, 0, 1, 1, 1]); // 3
```

Keep a running count and reset it when the value changes. O(n) time, O(1) space.

## 126: How do you check if an array has any duplicates?

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

O(n) time. If you want to stop as soon as you find the first duplicate (useful for big arrays), loop and add to a `Set`, returning `true` when `has` is already true.

## 127: How do you check if a sentence is a pangram?

A pangram uses every letter of the alphabet at least once.

```js
function isPangram(str) {
  const letters = new Set(str.toLowerCase().match(/[a-z]/g));
  return letters.size === 26;
}

isPangram("The quick brown fox jumps over the lazy dog"); // true
```

`match` returns `null` if there are no letters, and `new Set(null)` is just an empty set, so this works for empty strings too.

## 128: How do you compress a string like "aaabcc" into "a3b1c2"?

```js
function compress(str) {
  let result = "";
  let count = 1;
  for (let i = 1; i <= str.length; i++) {
    if (str[i] === str[i - 1]) {
      count++;
    } else {
      result += str[i - 1] + count;
      count = 1;
    }
  }
  return result;
}

compress("aaabcc"); // "a3b1c2"
```

Looping to `str.length` (one past the end) flushes the last group, because `str[str.length]` is `undefined`. A common follow-up is to return the original string if the compressed one is not shorter. This simple form of compression is called run-length encoding.

## 129: How do you convert a number to binary and back?

```js
(10).toString(2); // "1010"
parseInt("1010", 2); // 10
(255).toString(16); // "ff"
```

`toString(radix)` and `parseInt(str, radix)` work with bases 2 to 36. If you must do it by hand, keep dividing by 2 and collect the remainders in reverse order.

## 130: How do you convert a Roman numeral to an integer?

Add each value, but subtract when a smaller symbol comes before a larger one (like IV = 4):

```js
function romanToInt(s) {
  const values = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    const current = values[s[i]];
    const next = values[s[i + 1]] ?? 0;
    total += current < next ? -current : current;
  }
  return total;
}

romanToInt("MCMXCIV"); // 1994
```

One pass, O(n).

## 131: How do you check if a year is a leap year?

```js
const isLeapYear = (y) => (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;

isLeapYear(2024); // true
isLeapYear(1900); // false
isLeapYear(2000); // true
```

Divisible by 4, except centuries, unless the century is divisible by 400. In real apps you can also let the `Date` object decide: `new Date(y, 1, 29).getMonth() === 1`.

## 132: How do you sum the numbers from 1 to n without a loop?

Use Gauss's formula:

```js
const sumTo = (n) => (n * (n + 1)) / 2;

sumTo(100); // 5050
```

This is O(1). Interviewers sometimes ask for the loop version first and then ask if you can do better. Knowing a math shortcut is a good way to show you look beyond the obvious answer.

## 133: How do you find the most frequent element in an array?

```js
function mostFrequent(arr) {
  const counts = new Map();
  let best = undefined;
  let bestCount = 0;
  for (const x of arr) {
    const c = (counts.get(x) ?? 0) + 1;
    counts.set(x, c);
    if (c > bestCount) {
      best = x;
      bestCount = c;
    }
  }
  return best;
}
```

Track the winner while you count, so you need only one pass. Ask what to return on a tie. This version returns the one that reached the top count first.

## 134: How do you group items by a key?

ES2024 added `Object.groupBy` and `Map.groupBy`:

```js
const products = [
  { name: "apple", type: "fruit" },
  { name: "carrot", type: "vegetable" },
  { name: "pear", type: "fruit" },
];

Object.groupBy(products, (p) => p.type);
// { fruit: [apple, pear], vegetable: [carrot] }
```

Use `Map.groupBy` when the keys are not strings. Before that, people used `reduce` with an object. Either way it is O(n). Note that `Object.groupBy` returns an object with a `null` prototype.

## 135: How do you zip two arrays together?

```js
const zip = (a, b) =>
  Array.from({ length: Math.min(a.length, b.length) }, (_, i) => [a[i], b[i]]);

zip(["a", "b", "c"], [1, 2, 3]); // [["a", 1], ["b", 2], ["c", 3]]
```

Ask whether the result should stop at the shorter array or fill with `undefined`. A related trick is turning the zipped pairs into an object with `Object.fromEntries`.

## 136: How do you remove duplicate objects by id?

```js
function uniqueBy(arr, key) {
  const seen = new Set();
  return arr.filter((item) => {
    const k = item[key];
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });
}

uniqueBy(users, "id");
```

This keeps the first occurrence. If you want the last one instead, you can use `[...new Map(arr.map((x) => [x.id, x])).values()]`, because later entries overwrite earlier ones in the Map.

## 137: What is wrong with Array(3).fill([]) for a 2D array?

`fill` puts the same array reference in every slot, so changing one row changes all of them:

```js
const grid = Array(3).fill([]);
grid[0].push(1);
console.log(grid); // [[1], [1], [1]]
```

Create a new array for each row instead:

```js
const grid2 = Array.from({ length: 3 }, () => Array(4).fill(0));
```

This bug shows up a lot in grid and DP problems.

## 138: How do you transpose a matrix?

Swap rows and columns:

```js
const transpose = (m) => m[0].map((_, col) => m.map((row) => row[col]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
]); // [[1, 4], [2, 5], [3, 6]]
```

O(rows × cols) time. For a square matrix you can also do it in place by swapping `m[i][j]` with `m[j][i]` for `j > i`. This code assumes the matrix has at least one row.

## 139: How do you sum the diagonals of a square matrix?

```js
function diagonalSum(m) {
  const n = m.length;
  let sum = 0;
  for (let i = 0; i < n; i++) {
    sum += m[i][i]; // main diagonal
    sum += m[i][n - 1 - i]; // other diagonal
  }
  if (n % 2 === 1) sum -= m[(n - 1) / 2][(n - 1) / 2]; // center counted twice
  return sum;
}
```

O(n). The center element in an odd-sized matrix belongs to both diagonals, which is the edge case interviewers look for.

## 140: How do you search for a value in a 2D array?

The simple way loops over rows and columns, O(rows × cols):

```js
function findInGrid(grid, target) {
  for (let r = 0; r < grid.length; r++) {
    const c = grid[r].indexOf(target);
    if (c !== -1) return [r, c];
  }
  return null;
}
```

If each row and column is sorted, you can start at the top-right corner and move left or down, which is O(rows + cols).

## 141: What is the complexity of two nested loops over different arrays?

O(n × m), where n and m are the two sizes. People sometimes say O(n²), but that is only true if both arrays have about the same size. It matters in real code: comparing 10,000 orders against 50 users is 500,000 steps, which is fine, but 10,000 against 10,000 is 100 million.

## 142: What does amortized time mean?

Amortized time is the average cost of an operation over a long sequence of operations. `push` on an array is O(1) amortized: most pushes are cheap, but sometimes the engine has to allocate a bigger block and copy everything (O(n)). Because the size usually doubles, those expensive copies are rare enough that the average per push stays constant.

## 143: What is the space complexity of a recursive function?

Every call that hasn't returned yet takes space on the call stack. So a recursive function that goes n levels deep uses O(n) space, even if it doesn't create any arrays. Recursive Fibonacci with memoization uses O(n) for the cache and O(n) for the stack. Binary search written recursively uses O(log n) stack space, while the loop version uses O(1).

## 144: What is the complexity of slice, splice, concat and spread?

- `slice(start, end)` copies the selected part: O(k) for k items.
- `splice` removes or inserts and shifts the rest: O(n) in general.
- `concat` and `[...a, ...b]` copy all items: O(n + m).

They look like one step in code, but they all do work proportional to the data. Calling them inside loops is a common source of hidden O(n²).

## 145: What is an off-by-one error?

It is a bug where a loop or index goes one step too far or stops one step too early. Examples: using `i <= arr.length` (reads `undefined` at the end), using `high = arr.length` with `low <= high` in binary search, or forgetting the last group in string compression. Test with arrays of length 0, 1 and 2 to catch them.

## 146: How do you avoid infinite loops in while loops?

Make sure every path through the loop changes something the condition depends on. In binary search, for example, if you write `low = mid` instead of `low = mid + 1`, the loop can get stuck when `low` and `high` are next to each other. When unsure, step through a two-element example by hand. In a browser, an infinite loop freezes the whole tab, because the main thread never gets back to the event loop.

## 147: Why can Math.max(...arr) fail on very large arrays?

Spread passes every item as a separate function argument, and engines limit how many arguments a call can have (often around 100,000, but it varies). With a huge array you get `RangeError: Maximum call stack size exceeded` or a similar error. Use a loop or `reduce` instead:

```js
const max = arr.reduce((m, x) => (x > m ? x : m), -Infinity);
```

The same issue applies to `arr.push(...bigArray)`.

## 148: What algorithm does JavaScript's built-in sort use?

The spec doesn't say which algorithm to use, only that the sort must be stable. V8 (Chrome, Node.js, Edge) uses TimSort since 2018 (V8 7.0). Firefox and Safari use merge sort variants. All of them run in O(n log n) in the worst case. TimSort is very fast on data that is already partly sorted.

## 149: How do you count the number of unique values?

```js
const countUnique = (arr) => new Set(arr).size;
```

O(n) time and space. If the array is already sorted, you can count without extra memory by checking where `arr[i] !== arr[i - 1]`.

## 150: What is the difference between an algorithm and a data structure?

A data structure is a way to organize and store data, like an array, a `Map`, a tree or a graph. An algorithm is a set of steps that works on that data, like sorting, searching or finding a path. They go together: the right data structure can make an algorithm much faster. For example, a `Set` makes "have I seen this before?" checks O(1), which turns many O(n²) algorithms into O(n).

---

# Moderate Questions (151-300)

## 151: How does merge sort work?

Merge sort splits the array in half, sorts each half recursively and then merges the two sorted halves.

```js
function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  const result = [];
  let i = 0;
  let j = 0;
  while (i < left.length && j < right.length) {
    result.push(left[i] <= right[j] ? left[i++] : right[j++]);
  }
  return result.concat(left.slice(i), right.slice(j));
}
```

It is always O(n log n), it is stable, and it needs O(n) extra memory. It also works well for linked lists and for sorting data that doesn't fit in memory.

## 152: How does quick sort work?

Quick sort picks a pivot, moves smaller items to its left and larger items to its right (partitioning), then sorts both sides recursively.

```js
function quickSort(arr, lo = 0, hi = arr.length - 1) {
  if (lo >= hi) return arr;
  const pivot = arr[hi];
  let i = lo;
  for (let j = lo; j < hi; j++) {
    if (arr[j] < pivot) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }
  [arr[i], arr[hi]] = [arr[hi], arr[i]];
  quickSort(arr, lo, i - 1);
  quickSort(arr, i + 1, hi);
  return arr;
}
```

This is the Lomuto partition scheme. Average time is O(n log n), it sorts in place, and it is not stable.

## 153: What is the worst case of quick sort and how do you avoid it?

The worst case is O(n²). It happens when the pivot is always the smallest or largest item, for example when you pick the last element of an already sorted array. Then each partition only removes one item. To avoid it, pick a random pivot or use "median of three" (the median of the first, middle and last items). Many arrays with lots of equal values also hurt basic quick sort, which is why three-way partitioning exists.

## 154: When would you pick merge sort over quick sort, or the other way around?

Pick merge sort when you need stability, a guaranteed O(n log n), or you are sorting linked lists or streamed data. Pick quick sort when memory is tight, since it sorts in place, and when average speed matters most. Quick sort is often faster in practice because it works on nearby memory and does fewer moves. In JavaScript you usually just call the built-in sort, but interviewers want to see you know these trade-offs.

## 155: How does heap sort work?

Heap sort first turns the array into a max-heap, where every parent is larger than its children. Then it repeatedly swaps the root (the largest item) to the end of the array, shrinks the heap by one and fixes the heap again ("sift down"). It runs in O(n log n) in every case and sorts in place with O(1) extra memory, but it is not stable and is usually slower in practice than quick sort because it jumps around in memory.

## 156: What is counting sort and when can you use it?

Counting sort counts how many times each value appears and then writes them out in order. It doesn't compare items.

```js
function countingSort(arr, max) {
  const counts = new Array(max + 1).fill(0);
  for (const x of arr) counts[x]++;
  const result = [];
  for (let v = 0; v <= max; v++) {
    for (let k = 0; k < counts[v]; k++) result.push(v);
  }
  return result;
}
```

It is O(n + k), where k is the range of values. It only works for integers (or things you can map to integers) in a small range, like ages or test scores from 0 to 100.

## 157: What is radix sort?

Radix sort sorts numbers digit by digit, from the least significant digit to the most significant, using a stable sort (often counting sort) for each digit. For n numbers with d digits it is O(d × (n + b)), where b is the base. It can beat O(n log n) for many fixed-size integers, like sorting a million 32-bit IDs. It is not general purpose, because you need keys that split into digits.

## 158: What is bucket sort?

Bucket sort spreads items into a number of buckets by range, sorts each bucket (often with insertion sort) and then joins the buckets. It works well when values are spread evenly over a known range, like random floats between 0 and 1, and then it runs close to O(n). If most items land in one bucket, it falls back to the speed of the inner sort.

## 159: Why can't comparison sorts be faster than O(n log n)?

A comparison sort only learns about the order by comparing pairs. There are n! possible orders of n items, and each comparison can at best cut the possibilities in half. So you need at least log₂(n!) comparisons, which is about n log n. Counting sort and radix sort get around this limit because they don't compare items; they use the values themselves.

## 160: What is TimSort?

TimSort is a hybrid of merge sort and insertion sort, created by Tim Peters for Python. It finds runs that are already sorted (or reverse sorted) in the data, extends short runs with insertion sort, and merges runs in a smart order. It is stable, O(n log n) in the worst case and O(n) for already sorted data. V8 uses it for `Array.prototype.sort`, which is why sorting a mostly-sorted list in Chrome is very fast.

## 161: How do you sort by several keys, for example by last name and then first name?

Write a comparator that checks the next key only when the earlier ones are equal:

```js
people.sort(
  (a, b) =>
    a.lastName.localeCompare(b.lastName) ||
    a.firstName.localeCompare(b.firstName) ||
    b.age - a.age, // then age, oldest first
);
```

`||` moves to the next comparison when the result is `0`. Because the built-in sort is stable, you could also sort by the least important key first and the most important key last, but one comparator is clearer.

## 162: How do you find the first and last position of a value in a sorted array?

Run binary search but don't stop when you find the value. Keep going left (for the first) or right (for the last):

```js
function findFirst(arr, target) {
  let lo = 0;
  let hi = arr.length - 1;
  let result = -1;
  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    if (arr[mid] === target) {
      result = mid;
      hi = mid - 1; // keep looking left
    } else if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return result;
}
```

The last position is the same with `lo = mid + 1` on a match. Both are O(log n), and the count of the value is `last - first + 1`.

## 163: What is a "lower bound" binary search?

Lower bound returns the first index where the item is greater than or equal to the target. That is also the position where you'd insert the target to keep the array sorted.

```js
function lowerBound(arr, target) {
  let lo = 0;
  let hi = arr.length; // note: not length - 1
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}
```

This form (`lo < hi`, `hi = mid`) is less error-prone than the classic version and is useful for inserting into sorted lists and for range queries.

## 164: How do you search in a rotated sorted array?

An array like `[4, 5, 6, 7, 0, 1, 2]` was sorted and then rotated. At each step of binary search, at least one half is still sorted. Check which half is sorted and whether the target is inside it:

```js
function searchRotated(nums, target) {
  let lo = 0;
  let hi = nums.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    if (nums[mid] === target) return mid;
    if (nums[lo] <= nums[mid]) {
      // left half is sorted
      if (target >= nums[lo] && target < nums[mid]) hi = mid - 1;
      else lo = mid + 1;
    } else {
      // right half is sorted
      if (target > nums[mid] && target <= nums[hi]) lo = mid + 1;
      else hi = mid - 1;
    }
  }
  return -1;
}
```

O(log n), assuming no duplicates.

## 165: How do you find a peak element in an array?

A peak is an item bigger than its neighbors. You can find one in O(log n) with binary search: if `nums[mid] < nums[mid + 1]`, a peak must exist to the right (the values go up, and the edge counts as negative infinity), otherwise one exists on the left including `mid`.

```js
function findPeak(nums) {
  let lo = 0;
  let hi = nums.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (nums[mid] < nums[mid + 1]) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}
```

This shows binary search works on any problem where you can safely throw away half, not just sorted arrays.

## 166: What is "binary search on the answer"?

Instead of searching an array, you search over possible answers. You need a check function that says "is this answer good enough?", and the answers must be monotonic (if x works, everything bigger also works, or the other way around). Examples: the smallest ship capacity that ships all packages in D days, or the minimum eating speed to finish in H hours. Each check costs O(n), so the total is O(n log(range)).

## 167: How do you find the integer square root without Math.sqrt?

```js
function intSqrt(x) {
  let lo = 0;
  let hi = x;
  while (lo <= hi) {
    const mid = (lo + hi) >>> 1;
    if (mid * mid <= x) lo = mid + 1;
    else hi = mid - 1;
  }
  return hi; // largest number whose square is <= x
}

intSqrt(17); // 4
```

This is binary search on the answer, O(log x). The `>>> 1` trick only works for values below 2³², so use `Math.floor((lo + hi) / 2)` for larger inputs.

## 168: What is the sliding window technique? Show the fixed-size version.

A sliding window looks at a continuous part of an array or string and moves it forward one step at a time, updating the result instead of recalculating from scratch. Example: max sum of any k consecutive numbers.

```js
function maxSumK(arr, k) {
  if (arr.length < k) return null;
  let sum = 0;
  for (let i = 0; i < k; i++) sum += arr[i];
  let best = sum;
  for (let i = k; i < arr.length; i++) {
    sum += arr[i] - arr[i - k]; // add new item, drop old one
    best = Math.max(best, sum);
  }
  return best;
}
```

This is O(n) instead of O(n × k).

## 169: How do you find the longest substring without repeating characters?

Use a variable-size sliding window. Grow it on the right, and when you see a repeat, move the left side past the earlier copy:

```js
function longestUniqueSubstring(s) {
  const lastSeen = new Map();
  let start = 0;
  let best = 0;
  for (let end = 0; end < s.length; end++) {
    const ch = s[end];
    if (lastSeen.has(ch) && lastSeen.get(ch) >= start) {
      start = lastSeen.get(ch) + 1;
    }
    lastSeen.set(ch, end);
    best = Math.max(best, end - start + 1);
  }
  return best;
}

longestUniqueSubstring("abcabcbb"); // 3
```

Each character is processed once, so it's O(n).

## 170: How do you find the shortest subarray with a sum of at least a target?

This works for arrays of positive numbers. Grow the window to the right until the sum is big enough, then shrink it from the left as long as it still is:

```js
function minSubarrayLen(target, nums) {
  let start = 0;
  let sum = 0;
  let best = Infinity;
  for (let end = 0; end < nums.length; end++) {
    sum += nums[end];
    while (sum >= target) {
      best = Math.min(best, end - start + 1);
      sum -= nums[start++];
    }
  }
  return best === Infinity ? 0 : best;
}
```

O(n), since each index enters and leaves the window once. With negative numbers the sliding window doesn't work, and you need prefix sums with a monotonic deque instead.

## 171: How do you find a pair with a given sum in a sorted array?

Put one pointer at each end. If the sum is too small, move the left pointer right; if too big, move the right pointer left.

```js
function pairSumSorted(arr, target) {
  let i = 0;
  let j = arr.length - 1;
  while (i < j) {
    const sum = arr[i] + arr[j];
    if (sum === target) return [i, j];
    if (sum < target) i++;
    else j--;
  }
  return null;
}
```

O(n) time and O(1) space, better on memory than the hash map version because the array is already sorted.

## 172: How do you solve Three Sum (all unique triplets that sum to zero)?

Sort the array, fix one number, then use two pointers for the other two. Skip duplicates to avoid repeated triplets.

```js
function threeSum(nums) {
  nums = nums.toSorted((a, b) => a - b);
  const result = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let lo = i + 1;
    let hi = nums.length - 1;
    while (lo < hi) {
      const sum = nums[i] + nums[lo] + nums[hi];
      if (sum === 0) {
        result.push([nums[i], nums[lo], nums[hi]]);
        while (lo < hi && nums[lo] === nums[lo + 1]) lo++;
        while (lo < hi && nums[hi] === nums[hi - 1]) hi--;
        lo++;
        hi--;
      } else if (sum < 0) lo++;
      else hi--;
    }
  }
  return result;
}
```

O(n²) time, which is the expected answer for this problem.

## 173: How do you solve "container with most water"?

You get heights of vertical lines and need the two lines that hold the most water. Start with the widest container and move the pointer at the shorter line inward, because moving the taller one can't help:

```js
function maxArea(heights) {
  let i = 0;
  let j = heights.length - 1;
  let best = 0;
  while (i < j) {
    const area = Math.min(heights[i], heights[j]) * (j - i);
    best = Math.max(best, area);
    if (heights[i] < heights[j]) i++;
    else j--;
  }
  return best;
}
```

O(n) instead of checking all O(n²) pairs.

## 174: How do you remove duplicates from a sorted array in place?

```js
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  let write = 1;
  for (let read = 1; read < nums.length; read++) {
    if (nums[read] !== nums[write - 1]) {
      nums[write++] = nums[read];
    }
  }
  nums.length = write; // optional: trim the array
  return write;
}
```

Because the array is sorted, duplicates sit next to each other. A slow pointer marks where the next unique value goes. O(n) time, O(1) space.

## 175: How do you sort an array of 0s, 1s and 2s in one pass?

This is the Dutch national flag problem. Keep three pointers: everything before `low` is 0, everything after `high` is 2, and `mid` scans.

```js
function sortColors(nums) {
  let low = 0;
  let mid = 0;
  let high = nums.length - 1;
  while (mid <= high) {
    if (nums[mid] === 0) {
      [nums[low], nums[mid]] = [nums[mid], nums[low]];
      low++;
      mid++;
    } else if (nums[mid] === 1) {
      mid++;
    } else {
      [nums[mid], nums[high]] = [nums[high], nums[mid]];
      high--; // don't move mid, the swapped-in value is unchecked
    }
  }
  return nums;
}
```

O(n), in place. The same idea is used for three-way partitioning in quick sort.

## 176: What are prefix sums and what are they used for?

A prefix sum array stores the running total up to each position. After building it once in O(n), you can get the sum of any range in O(1).

```js
function buildPrefix(arr) {
  const prefix = [0];
  for (const x of arr) prefix.push(prefix.at(-1) + x);
  return prefix;
}

const prefix = buildPrefix([3, 1, 4, 1, 5]);
const rangeSum = (i, j) => prefix[j + 1] - prefix[i]; // sum of arr[i..j]
rangeSum(1, 3); // 1 + 4 + 1 = 6
```

The extra `0` at the start removes the special case for ranges that start at index 0. It is useful when you answer many range questions on data that doesn't change.

## 177: How do you count subarrays that sum to k?

Combine prefix sums with a `Map`. If the running sum now is `sum` and you've seen `sum - k` before, every earlier spot with that value starts a subarray that sums to k.

```js
function subarraySum(nums, k) {
  const seen = new Map([[0, 1]]);
  let sum = 0;
  let count = 0;
  for (const x of nums) {
    sum += x;
    count += seen.get(sum - k) ?? 0;
    seen.set(sum, (seen.get(sum) ?? 0) + 1);
  }
  return count;
}

subarraySum([1, 1, 1], 2); // 2
```

O(n) and it works with negative numbers, unlike the sliding window.

## 178: What is Kadane's algorithm?

Kadane's algorithm finds the largest sum of a continuous subarray in O(n). At each position, you either extend the current subarray or start a new one, whichever is bigger.

```js
function maxSubarray(nums) {
  let current = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    current = Math.max(nums[i], current + nums[i]);
    best = Math.max(best, current);
  }
  return best;
}

maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]); // 6
```

Starting from `nums[0]` instead of `0` makes it correct when all numbers are negative.

## 179: How do you compute the product of an array except self without division?

For each index, the answer is (product of everything to the left) × (product of everything to the right). Do two passes:

```js
function productExceptSelf(nums) {
  const n = nums.length;
  const result = new Array(n).fill(1);
  let left = 1;
  for (let i = 0; i < n; i++) {
    result[i] = left;
    left *= nums[i];
  }
  let right = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= right;
    right *= nums[i];
  }
  return result;
}

productExceptSelf([1, 2, 3, 4]); // [24, 12, 8, 6]
```

O(n) time, and O(1) extra space if you don't count the output. Division would break when the array contains a zero.

## 180: How do you find the best time to buy and sell a stock once?

Track the lowest price so far and the best profit if you sold today:

```js
function maxProfit(prices) {
  let minPrice = Infinity;
  let best = 0;
  for (const p of prices) {
    minPrice = Math.min(minPrice, p);
    best = Math.max(best, p - minPrice);
  }
  return best;
}

maxProfit([7, 1, 5, 3, 6, 4]); // 5
```

One pass, O(n). The brute-force version that checks every buy/sell pair is O(n²).

## 181: What is the Boyer-Moore voting algorithm?

It finds the majority element (one that appears more than n/2 times) in O(n) time and O(1) space. Keep a candidate and a counter. Same value adds one, different value subtracts one, and when the counter hits zero you pick a new candidate.

```js
function majority(nums) {
  let candidate = null;
  let count = 0;
  for (const x of nums) {
    if (count === 0) candidate = x;
    count += x === candidate ? 1 : -1;
  }
  return candidate;
}
```

If the majority is not guaranteed to exist, do a second pass to check that the candidate really appears more than n/2 times.

## 182: How do you merge overlapping intervals?

Sort by start, then walk through and either extend the last interval or add a new one:

```js
function mergeIntervals(intervals) {
  const sorted = intervals.toSorted((a, b) => a[0] - b[0]);
  const result = [];
  for (const [start, end] of sorted) {
    const last = result.at(-1);
    if (last && start <= last[1]) {
      last[1] = Math.max(last[1], end);
    } else {
      result.push([start, end]);
    }
  }
  return result;
}

mergeIntervals([
  [1, 3],
  [8, 10],
  [2, 6],
]); // [[1, 6], [8, 10]]
```

O(n log n) because of the sort. `Math.max` handles intervals fully inside another one, like `[1, 10]` and `[2, 3]`. In front-end work this shows up in calendar views and highlighting text ranges.

## 183: How do you insert a new interval into a sorted list of non-overlapping intervals?

Add all intervals that end before the new one starts, merge all that overlap with it, then add the rest:

```js
function insertInterval(intervals, newInterval) {
  const result = [];
  let [start, end] = newInterval;
  let i = 0;
  while (i < intervals.length && intervals[i][1] < start) {
    result.push(intervals[i++]);
  }
  while (i < intervals.length && intervals[i][0] <= end) {
    start = Math.min(start, intervals[i][0]);
    end = Math.max(end, intervals[i][1]);
    i++;
  }
  result.push([start, end]);
  while (i < intervals.length) result.push(intervals[i++]);
  return result;
}
```

O(n) because the input is already sorted.

## 184: How do you check if a person can attend all meetings?

Sort the meetings by start time and check if any meeting starts before the previous one ends:

```js
function canAttendAll(meetings) {
  const sorted = meetings.toSorted((a, b) => a[0] - b[0]);
  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i][0] < sorted[i - 1][1]) return false;
  }
  return true;
}
```

O(n log n). Ask whether a meeting ending at 10:00 and another starting at 10:00 count as overlapping. Here they don't.

## 185: How do you group anagrams together?

Give every word a key that is the same for all its anagrams, then group by that key:

```js
function groupAnagrams(words) {
  const groups = new Map();
  for (const w of words) {
    const key = [...w].sort().join("");
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(w);
  }
  return [...groups.values()];
}

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);
// [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

Sorting each word costs O(k log k), so total is O(n × k log k). For lowercase English letters, a key built from 26 letter counts makes it O(n × k).

## 186: How do you find the longest common prefix of a list of strings?

```js
function longestCommonPrefix(strs) {
  if (strs.length === 0) return "";
  let prefix = strs[0];
  for (const s of strs.slice(1)) {
    while (!s.startsWith(prefix)) {
      prefix = prefix.slice(0, -1);
      if (prefix === "") return "";
    }
  }
  return prefix;
}

longestCommonPrefix(["flower", "flow", "flight"]); // "fl"
```

O(S), where S is the total number of characters. Another neat trick: sort the list and compare only the first and the last strings.

## 187: When is sorting better than counting for anagram checks, and the other way around?

Counting with a `Map` (or a 26-slot array for lowercase letters) is O(n) and is the faster choice for long strings. Sorting (`[...a].sort().join("")`) is O(n log n) but shorter to write and also gives you a key you can use to group words. For short words in a big list, the sorting key is common and fine. Both should handle case and spaces the way the problem asks.

## 188: How do you find the longest palindromic substring?

Expand around each possible center. A palindrome has a center at a character (odd length) or between two characters (even length):

```js
function longestPalindrome(s) {
  let start = 0;
  let maxLen = 0;
  const expand = (l, r) => {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      l--;
      r++;
    }
    if (r - l - 1 > maxLen) {
      start = l + 1;
      maxLen = r - l - 1;
    }
  };
  for (let i = 0; i < s.length; i++) {
    expand(i, i); // odd length
    expand(i, i + 1); // even length
  }
  return s.slice(start, start + maxLen);
}

longestPalindrome("babad"); // "bab"
```

O(n²) time and O(1) space. Manacher's algorithm does it in O(n), but it is rarely expected.

## 189: How do you reverse the order of words in a sentence?

```js
const reverseWords = (s) => s.trim().split(/\s+/).reverse().join(" ");

reverseWords("  the sky  is blue "); // "blue is sky the"
```

The trim and the `\s+` split handle extra spaces. If asked to do it in place on a character array, reverse the whole array first, then reverse each word.

## 190: How do you check for a palindrome while ignoring spaces, punctuation and case?

Use two pointers and skip characters that are not letters or digits:

```js
function isCleanPalindrome(s) {
  const isAlnum = (ch) => /[\p{L}\p{N}]/u.test(ch);
  let i = 0;
  let j = s.length - 1;
  while (i < j) {
    if (!isAlnum(s[i])) {
      i++;
      continue;
    }
    if (!isAlnum(s[j])) {
      j--;
      continue;
    }
    if (s[i].toLowerCase() !== s[j].toLowerCase()) return false;
    i++;
    j--;
  }
  return true;
}

isCleanPalindrome("A man, a plan, a canal: Panama"); // true
```

This avoids building a cleaned copy, so it uses O(1) extra space. The shorter version cleans first with `replace(/[^\p{L}\p{N}]/gu, "")` and uses O(n) space.

## 191: How do you convert an integer to a Roman numeral?

Use a list of values from largest to smallest, including the subtractive pairs, and keep subtracting:

```js
function intToRoman(num) {
  const table = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];
  let result = "";
  for (const [value, symbol] of table) {
    while (num >= value) {
      result += symbol;
      num -= value;
    }
  }
  return result;
}

intToRoman(1994); // "MCMXCIV"
```

This is a greedy algorithm, and it works here because of how the Roman number system is built.

## 192: How do you implement indexOf for substrings yourself?

The naive approach tries every starting position:

```js
function strStr(haystack, needle) {
  if (needle === "") return 0;
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let j = 0;
    while (j < needle.length && haystack[i + j] === needle[j]) j++;
    if (j === needle.length) return i;
  }
  return -1;
}
```

It's O(n × m) in the worst case. For long texts, KMP or Rabin-Karp get it to O(n + m). In practice `str.indexOf` is fast and you should use it.

## 193: How do you check if two strings are isomorphic?

Two strings are isomorphic if you can replace characters in one to get the other, with a one-to-one mapping ("egg" and "add" are, "foo" and "bar" are not).

```js
function isIsomorphic(s, t) {
  if (s.length !== t.length) return false;
  const st = new Map();
  const ts = new Map();
  for (let i = 0; i < s.length; i++) {
    const a = s[i];
    const b = t[i];
    if ((st.has(a) && st.get(a) !== b) || (ts.has(b) && ts.get(b) !== a)) {
      return false;
    }
    st.set(a, b);
    ts.set(b, a);
  }
  return true;
}
```

You need both maps, otherwise "ab" and "aa" would pass. O(n).

## 194: How do you check if a ransom note can be built from a magazine?

Count the letters available in the magazine, then use them up for the note:

```js
function canConstruct(note, magazine) {
  const counts = new Map();
  for (const ch of magazine) counts.set(ch, (counts.get(ch) ?? 0) + 1);
  for (const ch of note) {
    const c = counts.get(ch) ?? 0;
    if (c === 0) return false;
    counts.set(ch, c - 1);
  }
  return true;
}
```

O(n + m). This is the frequency counter pattern again.

## 195: How do you implement a singly linked list in JavaScript?

```js
class ListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class LinkedList {
  head = null;
  size = 0;

  prepend(value) {
    this.head = new ListNode(value, this.head);
    this.size++;
  }

  append(value) {
    const node = new ListNode(value);
    if (!this.head) this.head = node;
    else {
      let cur = this.head;
      while (cur.next) cur = cur.next;
      cur.next = node;
    }
    this.size++;
  }

  *[Symbol.iterator]() {
    for (let cur = this.head; cur; cur = cur.next) yield cur.value;
  }
}
```

`prepend` is O(1), `append` is O(n) unless you also keep a `tail` reference. Making it iterable lets you use `[...list]` and `for...of`.

## 196: How do you reverse a linked list?

Walk through the list and point each node back to the previous one:

```js
function reverseList(head) {
  let prev = null;
  let cur = head;
  while (cur) {
    const next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }
  return prev; // new head
}
```

O(n) time and O(1) space. Save `next` before you change `cur.next`, or you lose the rest of the list. It is one of the most common linked list questions.

## 197: How do you detect a cycle in a linked list?

Use Floyd's tortoise and hare: a slow pointer moves one step, a fast pointer moves two. If there is a cycle, they meet. If the fast pointer reaches `null`, there is no cycle.

```js
function hasCycle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

O(n) time and O(1) space. A `Set` of visited nodes also works but uses O(n) memory.

## 198: How do you find the middle of a linked list in one pass?

Same idea as cycle detection. When the fast pointer reaches the end, the slow one is in the middle.

```js
function middle(head) {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}
```

For an even number of nodes this returns the second of the two middle nodes. Merge sort on linked lists uses this to split the list.

## 199: How do you merge two sorted linked lists?

Use a dummy head node so you don't need special cases for the first node:

```js
function mergeLists(a, b) {
  const dummy = new ListNode(0);
  let tail = dummy;
  while (a && b) {
    if (a.value <= b.value) {
      tail.next = a;
      a = a.next;
    } else {
      tail.next = b;
      b = b.next;
    }
    tail = tail.next;
  }
  tail.next = a ?? b;
  return dummy.next;
}
```

O(n + m) time, O(1) extra space, because you only relink existing nodes.

## 200: How do you remove the nth node from the end of a linked list?

Move a fast pointer n steps ahead, then move both pointers until the fast one reaches the end. The slow one is then just before the node to remove.

```js
function removeNthFromEnd(head, n) {
  const dummy = new ListNode(0, head);
  let fast = dummy;
  let slow = dummy;
  for (let i = 0; i <= n; i++) fast = fast.next;
  while (fast) {
    fast = fast.next;
    slow = slow.next;
  }
  slow.next = slow.next.next;
  return dummy.next;
}
```

One pass. The dummy node handles removing the head.

## 201: How do you build a stack that returns the minimum in O(1)?

Keep a second stack that stores the current minimum at each level:

```js
class MinStack {
  #items = [];
  #mins = [];

  push(x) {
    this.#items.push(x);
    const min = this.#mins.length ? Math.min(x, this.#mins.at(-1)) : x;
    this.#mins.push(min);
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

Every operation is O(1). The extra memory is O(n). You can save memory by only pushing to `#mins` when the new value is less than or equal to the current minimum.

## 202: How do you evaluate an expression in Reverse Polish Notation?

In RPN, operators come after their operands: `["2", "1", "+", "3", "*"]` means `(2 + 1) * 3`. Push numbers on a stack, and when you see an operator, pop two numbers and push the result.

```js
function evalRPN(tokens) {
  const stack = [];
  const ops = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => Math.trunc(a / b),
  };
  for (const t of tokens) {
    if (t in ops) {
      const b = stack.pop();
      const a = stack.pop();
      stack.push(ops[t](a, b));
    } else {
      stack.push(Number(t));
    }
  }
  return stack.pop();
}
```

The order of `a` and `b` matters for `-` and `/`. O(n).

## 203: What is a monotonic stack? Show "next greater element".

A monotonic stack keeps its items in increasing or decreasing order. When a new item breaks the order, you pop items, and each pop is the moment you find an answer for that item.

```js
function nextGreater(nums) {
  const result = new Array(nums.length).fill(-1);
  const stack = []; // indexes, values decreasing
  for (let i = 0; i < nums.length; i++) {
    while (stack.length && nums[stack.at(-1)] < nums[i]) {
      result[stack.pop()] = nums[i];
    }
    stack.push(i);
  }
  return result;
}

nextGreater([2, 1, 2, 4, 3]); // [4, 2, 4, -1, -1]
```

Each index is pushed and popped once, so it's O(n). "Daily temperatures" and "stock span" use the same pattern.

## 204: How do you build a queue from two stacks?

Push to an "in" stack. When you need to dequeue and the "out" stack is empty, move everything from "in" to "out", which reverses the order.

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
}
```

Each item is moved at most once, so both operations are O(1) amortized. This is a good example to explain amortized analysis.

## 205: How do you build a fast queue in JavaScript without shift()?

Keep a head index and only move it forward:

```js
class Queue {
  #items = [];
  #head = 0;

  enqueue(x) {
    this.#items.push(x);
  }

  dequeue() {
    if (this.#head === this.#items.length) return undefined;
    const x = this.#items[this.#head];
    this.#items[this.#head++] = undefined; // let GC collect it
    if (this.#head > 1024 && this.#head * 2 > this.#items.length) {
      this.#items = this.#items.slice(this.#head);
      this.#head = 0;
    }
    return x;
  }

  get size() {
    return this.#items.length - this.#head;
  }
}
```

Dequeue is O(1) amortized. The cleanup step stops the array from growing forever. A linked list or a ring buffer also works.

## 206: What is a circular buffer (ring buffer)?

A circular buffer is a fixed-size array where the write position wraps around to the start when it reaches the end. It is good for "keep the last N items", like recent log lines, frame times for an FPS counter or audio samples.

```js
class RingBuffer {
  #data;
  #start = 0;
  #size = 0;

  constructor(capacity) {
    this.#data = new Array(capacity);
  }

  push(x) {
    const end = (this.#start + this.#size) % this.#data.length;
    this.#data[end] = x;
    if (this.#size < this.#data.length) this.#size++;
    else this.#start = (this.#start + 1) % this.#data.length; // overwrite oldest
  }

  toArray() {
    return Array.from(
      { length: this.#size },
      (_, i) => this.#data[(this.#start + i) % this.#data.length],
    );
  }
}
```

All operations are O(1) and memory never grows.

## 207: How do you insert a value into a binary search tree?

```js
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function insert(root, value) {
  if (!root) return new TreeNode(value);
  if (value < root.value) root.left = insert(root.left, value);
  else root.right = insert(root.right, value);
  return root;
}

let root = null;
for (const v of [8, 3, 10, 1, 6]) root = insert(root, v);
```

Go left if the value is smaller, right otherwise, until you find an empty spot. It's O(h), where h is the height: O(log n) for a balanced tree and O(n) if you insert sorted data.

## 208: How do you search a binary search tree?

```js
function search(root, target) {
  let cur = root;
  while (cur) {
    if (target === cur.value) return cur;
    cur = target < cur.value ? cur.left : cur.right;
  }
  return null;
}
```

Each step goes down one level and throws away the other subtree, which is binary search on a tree. O(h) time and O(1) space for the loop version.

## 209: How do you write preorder, inorder and postorder traversal?

```js
function preorder(node, out = []) {
  if (!node) return out;
  out.push(node.value);
  preorder(node.left, out);
  preorder(node.right, out);
  return out;
}

function inorder(node, out = []) {
  if (!node) return out;
  inorder(node.left, out);
  out.push(node.value);
  inorder(node.right, out);
  return out;
}

function postorder(node, out = []) {
  if (!node) return out;
  postorder(node.left, out);
  postorder(node.right, out);
  out.push(node.value);
  return out;
}
```

The only difference is where you visit the node. Preorder is used to copy a tree, inorder gives sorted output in a BST, and postorder is used when children must be handled before the parent, like deleting a folder tree or calculating sizes.

## 210: How do you do a level order (BFS) traversal of a binary tree?

Use a queue and process one level at a time:

```js
function levelOrder(root) {
  if (!root) return [];
  const result = [];
  let level = [root];
  while (level.length) {
    result.push(level.map((n) => n.value));
    const next = [];
    for (const node of level) {
      if (node.left) next.push(node.left);
      if (node.right) next.push(node.right);
    }
    level = next;
  }
  return result;
}
```

Using a fresh array for each level avoids `shift()` and also gives you the level grouping for free. O(n) time.

## 211: How do you find the maximum depth of a binary tree?

```js
const maxDepth = (node) =>
  node ? 1 + Math.max(maxDepth(node.left), maxDepth(node.right)) : 0;
```

The depth of a node is one more than the deeper of its two children. O(n) time, and O(h) stack space. For very deep, unbalanced trees, the BFS version from the previous question avoids stack overflow: just count the levels.

## 212: How do you check if a binary tree is a valid BST?

Checking only that each node is bigger than its left child and smaller than its right child is not enough. Every node must be inside a range set by all its ancestors.

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

O(n). Another approach is to do an inorder traversal and check that the values are strictly increasing.

## 213: How do you invert (mirror) a binary tree?

Swap the left and right children of every node:

```js
function invert(node) {
  if (!node) return null;
  [node.left, node.right] = [invert(node.right), invert(node.left)];
  return node;
}
```

O(n) time. It's a short question, but it checks that you understand recursion on trees.

## 214: How do you find the lowest common ancestor in a BST?

Start at the root. If both values are smaller, go left. If both are larger, go right. Otherwise the current node is where they split, so it is the answer.

```js
function lcaBST(root, a, b) {
  let cur = root;
  while (cur) {
    if (a < cur.value && b < cur.value) cur = cur.left;
    else if (a > cur.value && b > cur.value) cur = cur.right;
    else return cur;
  }
  return null;
}
```

O(h). This uses the BST ordering. For a general binary tree you need a different approach (see the advanced section).

## 215: How do you check if a binary tree is height-balanced?

A tree is balanced if, for every node, the heights of the left and right subtrees differ by at most 1. Compute heights bottom-up and return `-1` as soon as you find a problem:

```js
function isBalanced(root) {
  const height = (node) => {
    if (!node) return 0;
    const l = height(node.left);
    if (l === -1) return -1;
    const r = height(node.right);
    if (r === -1 || Math.abs(l - r) > 1) return -1;
    return 1 + Math.max(l, r);
  };
  return height(root) !== -1;
}
```

O(n). The naive version that calls a separate `height` function at every node is O(n²) for skewed trees.

## 216: How do you do an inorder traversal without recursion?

Use your own stack. Go left as far as possible, then visit, then go right:

```js
function inorderIterative(root) {
  const result = [];
  const stack = [];
  let cur = root;
  while (cur || stack.length) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    cur = stack.pop();
    result.push(cur.value);
    cur = cur.right;
  }
  return result;
}
```

This avoids stack overflow on very deep trees and is a common follow-up after the recursive version.

## 217: How do you walk the DOM tree recursively?

```js
function walk(node, visit, depth = 0) {
  visit(node, depth);
  for (const child of node.children) {
    walk(child, visit, depth + 1);
  }
}

walk(document.body, (el, depth) => {
  console.log(" ".repeat(depth * 2) + el.tagName);
});
```

This is a preorder DFS. `children` only includes elements. Use `childNodes` if you also need text and comment nodes. It's a good front-end version of tree traversal, and interviewers sometimes ask you to write your own `getElementsByClassName` this way.

## 218: How would you write your own getElementsByClassName?

```js
function byClassName(root, className) {
  const result = [];
  const stack = [root];
  while (stack.length) {
    const el = stack.pop();
    if (el.classList?.contains(className)) result.push(el);
    for (let i = el.children.length - 1; i >= 0; i--) {
      stack.push(el.children[i]);
    }
  }
  return result;
}
```

Pushing children in reverse keeps the result in document order. The iterative version is safe for deep DOM trees. The browser also has `TreeWalker` (`document.createTreeWalker`) built for this kind of walk.

## 219: How do you flatten a nested object into dot-notation keys?

```js
function flattenObject(obj, prefix = "", out = {}) {
  for (const [key, value] of Object.entries(obj)) {
    const path = prefix ? `${prefix}.${key}` : key;
    if (value && typeof value === "object" && !Array.isArray(value)) {
      flattenObject(value, path, out);
    } else {
      out[path] = value;
    }
  }
  return out;
}

flattenObject({ a: 1, b: { c: 2, d: { e: 3 } } });
// { a: 1, "b.c": 2, "b.d.e": 3 }
```

Ask how arrays, empty objects, `Date` and `null` should be handled. This is common for form libraries, translation files and query strings.

## 220: How do you turn dot-notation keys back into a nested object?

```js
function unflatten(flat) {
  const result = {};
  for (const [path, value] of Object.entries(flat)) {
    const keys = path.split(".");
    let cur = result;
    keys.forEach((key, i) => {
      if (i === keys.length - 1) cur[key] = value;
      else cur = cur[key] ??= {};
    });
  }
  return result;
}

unflatten({ a: 1, "b.c": 2, "b.d.e": 3 }); // { a: 1, b: { c: 2, d: { e: 3 } } }
```

`??=` creates the middle object only if it doesn't exist yet. Be careful with keys like `__proto__` if the input comes from users, since it can lead to prototype pollution.

## 221: How do you deep clone an object?

Use `structuredClone`, which is built into browsers and Node.js:

```js
const copy = structuredClone(original);
```

It handles nested objects, arrays, `Map`, `Set`, `Date` and circular references. It can't clone functions, DOM nodes or class instances with their prototype. If you have to write it yourself, recurse over arrays and plain objects and use a `WeakMap` to handle cycles. `JSON.parse(JSON.stringify(x))` loses `undefined`, `Date`, `Map`, `Set` and fails on cycles.

## 222: How do you write a deep equality check?

```js
function deepEqual(a, b) {
  if (Object.is(a, b)) return true;
  if (typeof a !== "object" || typeof b !== "object" || !a || !b) return false;
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every((k) => Object.hasOwn(b, k) && deepEqual(a[k], b[k]));
}
```

This covers plain objects and arrays. A full version also needs to handle `Date`, `Map`, `Set`, `RegExp` and circular references. Time is O(n) over all nested values.

## 223: How do you get a nested value by a path string, like lodash get?

```js
function get(obj, path, fallback) {
  const keys = Array.isArray(path)
    ? path
    : path.replace(/\[(\w+)\]/g, ".$1").split(".");
  let cur = obj;
  for (const key of keys) {
    if (cur == null) return fallback;
    cur = cur[key];
  }
  return cur === undefined ? fallback : cur;
}

get({ a: { b: [{ c: 5 }] } }, "a.b[0].c"); // 5
get({ a: 1 }, "a.x.y", "none"); // "none"
```

The regex turns `b[0]` into `b.0`. In normal code, optional chaining (`obj?.a?.b?.[0]?.c`) does the same when the path is known ahead of time.

## 224: How do you represent a graph in JavaScript?

The two common ways:

```js
// adjacency list: good for sparse graphs (most real graphs)
const graph = new Map([
  ["A", ["B", "C"]],
  ["B", ["D"]],
  ["C", ["D"]],
  ["D", []],
]);

// adjacency matrix: good for dense graphs or fast "is there an edge?" checks
const matrix = [
  [0, 1, 1, 0],
  [0, 0, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0],
];
```

A list uses O(V + E) memory and makes it quick to loop over neighbors. A matrix uses O(V²) memory but checks one edge in O(1).

## 225: How do you implement BFS on a graph?

```js
function bfs(graph, start) {
  const visited = new Set([start]);
  const queue = [start];
  const order = [];
  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    order.push(node);
    for (const next of graph.get(node) ?? []) {
      if (!visited.has(next)) {
        visited.add(next);
        queue.push(next);
      }
    }
  }
  return order;
}
```

Mark nodes as visited when you add them to the queue, not when you take them out. Otherwise the same node can be queued many times. The `head` index avoids slow `shift()`. O(V + E).

## 226: How do you implement DFS on a graph?

```js
// recursive
function dfs(graph, node, visited = new Set()) {
  visited.add(node);
  for (const next of graph.get(node) ?? []) {
    if (!visited.has(next)) dfs(graph, next, visited);
  }
  return visited;
}

// iterative
function dfsIterative(graph, start) {
  const visited = new Set();
  const stack = [start];
  while (stack.length) {
    const node = stack.pop();
    if (visited.has(node)) continue;
    visited.add(node);
    for (const next of graph.get(node) ?? []) stack.push(next);
  }
  return visited;
}
```

Both are O(V + E). The iterative version doesn't hit the recursion limit on long paths, but it visits neighbors in a slightly different order.

## 227: How do you find the shortest path in an unweighted graph?

Use BFS and remember where each node came from, then walk back from the target:

```js
function shortestPath(graph, start, target) {
  const prev = new Map([[start, null]]);
  const queue = [start];
  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    if (node === target) break;
    for (const next of graph.get(node) ?? []) {
      if (!prev.has(next)) {
        prev.set(next, node);
        queue.push(next);
      }
    }
  }
  if (!prev.has(target)) return null;
  const path = [];
  for (let n = target; n !== null; n = prev.get(n)) path.push(n);
  return path.reverse();
}
```

BFS reaches each node first by the shortest route, which is why it works without weights. For weighted edges, use Dijkstra.

## 228: How do you count islands in a grid?

Loop over every cell. When you find unvisited land, count an island and flood out from it to mark the whole island:

```js
function numIslands(grid) {
  const rows = grid.length;
  const cols = grid[0]?.length ?? 0;
  let count = 0;
  const sink = (r, c) => {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] !== "1") return;
    grid[r][c] = "0";
    sink(r + 1, c);
    sink(r - 1, c);
    sink(r, c + 1);
    sink(r, c - 1);
  };
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1") {
        count++;
        sink(r, c);
      }
    }
  }
  return count;
}
```

O(rows × cols). This changes the input. If you shouldn't, use a `visited` set. For big grids, use BFS to avoid deep recursion.

## 229: How do you detect a cycle in a directed graph?

Use DFS with three states: not visited, in progress (on the current path) and done. If you reach a node that is in progress, you found a cycle.

```js
function hasCycle(graph) {
  const state = new Map(); // 1 = in progress, 2 = done
  const visit = (node) => {
    if (state.get(node) === 1) return true;
    if (state.get(node) === 2) return false;
    state.set(node, 1);
    for (const next of graph.get(node) ?? []) {
      if (visit(next)) return true;
    }
    state.set(node, 2);
    return false;
  };
  for (const node of graph.keys()) {
    if (visit(node)) return true;
  }
  return false;
}
```

A simple visited set is not enough in a directed graph, because reaching a "done" node from a different path is not a cycle. O(V + E).

## 230: What is topological sort and how do you do it?

A topological sort orders the nodes of a directed graph so that every edge goes from earlier to later. It only exists if there are no cycles. Kahn's algorithm repeatedly takes nodes that have no incoming edges:

```js
function topoSort(graph) {
  const inDegree = new Map();
  for (const node of graph.keys()) inDegree.set(node, inDegree.get(node) ?? 0);
  for (const edges of graph.values()) {
    for (const n of edges) inDegree.set(n, (inDegree.get(n) ?? 0) + 1);
  }
  const queue = [...inDegree].filter(([, d]) => d === 0).map(([n]) => n);
  const order = [];
  for (let head = 0; head < queue.length; head++) {
    const node = queue[head];
    order.push(node);
    for (const next of graph.get(node) ?? []) {
      inDegree.set(next, inDegree.get(next) - 1);
      if (inDegree.get(next) === 0) queue.push(next);
    }
  }
  if (order.length !== inDegree.size) throw new Error("Graph has a cycle");
  return order;
}
```

O(V + E). If some nodes never reach zero in-degree, there's a cycle.

## 231: Where does topological sort show up in front-end work?

Anywhere you have things that depend on other things and must run in the right order. Bundlers like Vite, webpack and Rollup order modules by their imports. Monorepo tools like Nx and Turborepo build packages after their dependencies. Task runners order build steps. Spreadsheet-like forms recalculate fields after the fields they depend on. When the graph has a cycle, these tools report a circular dependency.

## 232: How do you count connected components in an undirected graph?

Start a DFS or BFS from every node you haven't seen yet. Each start is a new component.

```js
function countComponents(n, edges) {
  const graph = Array.from({ length: n }, () => []);
  for (const [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
  }
  const seen = new Array(n).fill(false);
  let count = 0;
  for (let i = 0; i < n; i++) {
    if (seen[i]) continue;
    count++;
    const stack = [i];
    seen[i] = true;
    while (stack.length) {
      for (const next of graph[stack.pop()]) {
        if (!seen[next]) {
          seen[next] = true;
          stack.push(next);
        }
      }
    }
  }
  return count;
}
```

O(V + E). Union-Find is another way that works well when edges arrive one by one.

## 233: How does flood fill work?

Flood fill changes a connected area of the same color to a new color, like the paint bucket tool in an image editor.

```js
function floodFill(image, sr, sc, newColor) {
  const old = image[sr][sc];
  if (old === newColor) return image;
  const stack = [[sr, sc]];
  while (stack.length) {
    const [r, c] = stack.pop();
    if (image[r]?.[c] !== old) continue;
    image[r][c] = newColor;
    stack.push([r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]);
  }
  return image;
}
```

The early return when the color is already the new color prevents an infinite loop. Optional chaining handles going off the grid. O(number of cells).

## 234: What is a clean way to move in four directions on a grid?

Use a directions array instead of writing four separate calls:

```js
const DIRS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

function neighbors(grid, r, c) {
  const result = [];
  for (const [dr, dc] of DIRS) {
    const nr = r + dr;
    const nc = c + dc;
    if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length) {
      result.push([nr, nc]);
    }
  }
  return result;
}
```

Add the four diagonal pairs if the problem allows eight directions. When you store visited cells in a `Set`, use a string key like `` `${r},${c}` `` or a number like `r * cols + c`, since arrays are compared by reference.

## 235: What is backtracking?

Backtracking builds a solution step by step. At each step it tries a choice, goes deeper, and if that path can't lead to a valid answer, it undoes the choice and tries the next one. It's a DFS over a tree of choices. It is used for subsets, permutations, combinations, Sudoku and N-Queens. The general shape is "choose, explore, un-choose".

## 236: How do you generate all subsets of an array?

```js
function subsets(nums) {
  const result = [];
  const current = [];
  const backtrack = (start) => {
    result.push([...current]);
    for (let i = start; i < nums.length; i++) {
      current.push(nums[i]);
      backtrack(i + 1);
      current.pop();
    }
  };
  backtrack(0);
  return result;
}

subsets([1, 2, 3]); // [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
```

There are 2ⁿ subsets, so time is O(n × 2ⁿ). Copy `current` when you save it, because you keep changing the same array.

## 237: How do you generate all permutations of an array?

```js
function permutations(nums) {
  const result = [];
  const used = new Array(nums.length).fill(false);
  const current = [];
  const backtrack = () => {
    if (current.length === nums.length) {
      result.push([...current]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      current.push(nums[i]);
      backtrack();
      current.pop();
      used[i] = false;
    }
  };
  backtrack();
  return result;
}
```

There are n! permutations, so it's O(n × n!). That's fine for n up to about 8 to 10. If the input has duplicates, sort it and skip `nums[i]` when it equals `nums[i - 1]` and `used[i - 1]` is false.

## 238: How do you generate all combinations of k items from n?

```js
function combine(n, k) {
  const result = [];
  const current = [];
  const backtrack = (start) => {
    if (current.length === k) {
      result.push([...current]);
      return;
    }
    for (let i = start; i <= n - (k - current.length) + 1; i++) {
      current.push(i);
      backtrack(i + 1);
      current.pop();
    }
  };
  backtrack(1);
  return result;
}

combine(4, 2); // [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

The upper limit in the loop stops early when there aren't enough numbers left to fill the combination. That's a simple form of pruning.

## 239: How do you solve Combination Sum (numbers can be reused)?

Find all combinations of candidates that add up to a target, where each number can be used many times:

```js
function combinationSum(candidates, target) {
  const result = [];
  const current = [];
  const sorted = candidates.toSorted((a, b) => a - b);
  const backtrack = (start, remaining) => {
    if (remaining === 0) {
      result.push([...current]);
      return;
    }
    for (let i = start; i < sorted.length; i++) {
      if (sorted[i] > remaining) break; // sorted, so nothing after fits
      current.push(sorted[i]);
      backtrack(i, remaining - sorted[i]); // i, not i + 1: allow reuse
      current.pop();
    }
  };
  backtrack(0, target);
  return result;
}
```

Passing `i` instead of `i + 1` allows reuse, and starting from `start` avoids the same combination in a different order.

## 240: How do you generate all valid combinations of n pairs of parentheses?

Add `(` while you still have some left, and add `)` only when it wouldn't close more than you've opened:

```js
function generateParens(n) {
  const result = [];
  const build = (str, open, close) => {
    if (str.length === 2 * n) {
      result.push(str);
      return;
    }
    if (open < n) build(str + "(", open + 1, close);
    if (close < open) build(str + ")", open, close + 1);
  };
  build("", 0, 0);
  return result;
}

generateParens(3); // ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

Because you never build an invalid string, there's no need to check validity at the end.

## 241: How do you search for a word in a grid of letters?

Start a DFS from every cell that matches the first letter. Mark cells as used while on the current path and unmark them when you backtrack.

```js
function exist(board, word) {
  const rows = board.length;
  const cols = board[0].length;
  const dfs = (r, c, i) => {
    if (i === word.length) return true;
    if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] !== word[i]) {
      return false;
    }
    const saved = board[r][c];
    board[r][c] = "#"; // mark as used
    const found =
      dfs(r + 1, c, i + 1) ||
      dfs(r - 1, c, i + 1) ||
      dfs(r, c + 1, i + 1) ||
      dfs(r, c - 1, i + 1);
    board[r][c] = saved; // undo
    return found;
  };
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (dfs(r, c, 0)) return true;
    }
  }
  return false;
}
```

Worst case is O(rows × cols × 4^L) where L is the word length, but in practice the early mismatches prune most paths.

## 242: How do you solve "climbing stairs" with dynamic programming?

You can climb 1 or 2 steps at a time. How many ways are there to reach step n? The ways to reach step n are the ways to reach n − 1 plus the ways to reach n − 2.

```js
function climbStairs(n) {
  let oneBack = 1; // ways to reach step 1
  let twoBack = 1; // ways to reach step 0
  for (let i = 2; i <= n; i++) {
    [twoBack, oneBack] = [oneBack, oneBack + twoBack];
  }
  return oneBack;
}

climbStairs(5); // 8
```

It's Fibonacci in disguise. O(n) time and O(1) space. Many DP problems start with "how many ways can I get here?".

## 243: What is the difference between top-down and bottom-up dynamic programming?

Top-down starts from the original problem, recurses into smaller ones and caches results (memoization). It is easy to write from the recursive formula and only solves subproblems you actually need. Bottom-up starts from the smallest subproblems and fills a table up to the answer. It avoids recursion (and stack limits), and often lets you keep only the last row or two, saving memory. Both have the same Big O.

## 244: How do you find the minimum number of coins to make an amount?

`dp[a]` is the fewest coins to make amount `a`. For each amount, try every coin:

```js
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;
  for (let a = 1; a <= amount; a++) {
    for (const coin of coins) {
      if (coin <= a) dp[a] = Math.min(dp[a], dp[a - coin] + 1);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}

coinChange([1, 2, 5], 11); // 3 (5 + 5 + 1)
```

O(amount × coins). A greedy "take the biggest coin" approach fails for coin sets like `[1, 3, 4]` with amount 6.

## 245: How do you count the number of ways to make change?

```js
function countWays(coins, amount) {
  const dp = new Array(amount + 1).fill(0);
  dp[0] = 1;
  for (const coin of coins) {
    for (let a = coin; a <= amount; a++) {
      dp[a] += dp[a - coin];
    }
  }
  return dp[amount];
}

countWays([1, 2, 5], 5); // 4
```

The order of the loops matters. Coins in the outer loop counts combinations (1+2 and 2+1 are the same). Amounts in the outer loop would count permutations instead. Interviewers like to ask why.

## 246: How do you solve the House Robber problem?

You can't rob two houses next to each other. At each house, the best total is either the best up to the previous house (skip this one) or this house plus the best up to two houses back.

```js
function rob(houses) {
  let prev = 0; // best up to i - 1
  let prev2 = 0; // best up to i - 2
  for (const money of houses) {
    [prev2, prev] = [prev, Math.max(prev, prev2 + money)];
  }
  return prev;
}

rob([2, 7, 9, 3, 1]); // 12
```

O(n) time, O(1) space. It's a good example of a DP with a "take it or skip it" choice.

## 247: How do you find the longest common subsequence of two strings?

A subsequence keeps the order but can skip characters. `dp[i][j]` is the LCS length of the first i chars of `a` and the first j chars of `b`.

```js
function lcs(a, b) {
  const dp = Array.from({ length: a.length + 1 }, () =>
    new Array(b.length + 1).fill(0),
  );
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      dp[i][j] =
        a[i - 1] === b[j - 1]
          ? dp[i - 1][j - 1] + 1
          : Math.max(dp[i - 1][j], dp[i][j - 1]);
    }
  }
  return dp[a.length][b.length];
}

lcs("abcde", "ace"); // 3
```

O(n × m) time and space. LCS is the basis of many text diff tools.

## 248: How do you calculate the edit distance (Levenshtein distance) between two strings?

Edit distance is the minimum number of inserts, deletes and replacements to turn one string into another.

```js
function editDistance(a, b) {
  let prev = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    for (let j = 1; j <= b.length; j++) {
      cur[j] =
        a[i - 1] === b[j - 1]
          ? prev[j - 1]
          : 1 + Math.min(prev[j - 1], prev[j], cur[j - 1]);
    }
    prev = cur;
  }
  return prev[b.length];
}

editDistance("kitten", "sitting"); // 3
```

O(n × m) time and O(m) space with the two-row trick. It's used for "did you mean...?" suggestions and fuzzy search.

## 249: How do you solve the 0/1 knapsack problem?

You have items with weights and values and a bag with a weight limit. Each item can be taken once. `dp[w]` is the best value with capacity `w`:

```js
function knapsack(weights, values, capacity) {
  const dp = new Array(capacity + 1).fill(0);
  for (let i = 0; i < weights.length; i++) {
    for (let w = capacity; w >= weights[i]; w--) {
      dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
    }
  }
  return dp[capacity];
}

knapsack([1, 3, 4], [15, 20, 30], 4); // 35
```

Looping `w` backwards makes sure each item is used only once. Looping forward would turn it into the unbounded knapsack. O(n × capacity).

## 250: How do you find the length of the longest increasing subsequence?

The simple DP: `dp[i]` is the length of the longest increasing subsequence that ends at `i`.

```js
function lis(nums) {
  const dp = new Array(nums.length).fill(1);
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
  return Math.max(0, ...dp);
}

lis([10, 9, 2, 5, 3, 7, 101, 18]); // 4 (2, 3, 7, 101)
```

O(n²). There's an O(n log n) version using binary search, covered in the advanced section.

## 251: How many unique paths are there in a grid when you can only move right or down?

Each cell can be reached from the cell above or the cell to the left:

```js
function uniquePaths(rows, cols) {
  const dp = new Array(cols).fill(1);
  for (let r = 1; r < rows; r++) {
    for (let c = 1; c < cols; c++) {
      dp[c] += dp[c - 1]; // above (old dp[c]) + left (dp[c - 1])
    }
  }
  return dp[cols - 1];
}

uniquePaths(3, 7); // 28
```

One row of memory is enough. There's also a math answer: choose (rows − 1) downs out of (rows + cols − 2) moves. With obstacles, set `dp[c] = 0` on blocked cells.

## 252: How can you reduce memory in dynamic programming?

Look at which earlier cells each step uses. If row `i` only needs row `i - 1`, keep two rows (or one row updated carefully) instead of the whole table. If a 1D DP only needs the last two values, keep two variables. This turns O(n × m) memory into O(m), or O(n) into O(1). The catch is that you lose the full table, so you can't rebuild the actual solution path, only its value.

## 253: How do you write a generic memoize function?

```js
function memoize(fn) {
  const cache = new Map();
  return function (...args) {
    const key = args.length === 1 ? args[0] : JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const slowSquare = (n) => n * n;
const fastSquare = memoize(slowSquare);
```

Use `cache.has` instead of checking for `undefined`, so a function that returns `undefined` is cached too. For a recursive function, the recursive calls must go through the memoized version, or only the top call is cached.

## 254: How do you choose a cache key when memoizing a function with several arguments?

For one primitive argument, use it directly as a `Map` key. For several primitives, join them into a string (`` `${a}|${b}` ``) or use `JSON.stringify(args)`. For object arguments, `JSON.stringify` is slow and breaks for cycles and key order, so a nested `Map` per argument or a `WeakMap` keyed by the object is better. A `WeakMap` also lets the cache entry be garbage collected when the object is no longer used.

## 255: How do you solve the Jump Game with a greedy approach?

Each item is the max jump length from that position. Can you reach the last index? Keep track of the farthest index you can reach so far:

```js
function canJump(nums) {
  let farthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false; // stuck
    farthest = Math.max(farthest, i + nums[i]);
  }
  return true;
}

canJump([2, 3, 1, 1, 4]); // true
canJump([3, 2, 1, 0, 4]); // false
```

O(n). A DP solution also works but is O(n²). This is a case where greedy is both correct and simpler.

## 256: When does a greedy algorithm give the wrong answer?

When the best choice now blocks a better overall result later. The classic example is coin change with coins `[1, 3, 4]` and amount 6. Greedy takes 4, then 1, then 1 (three coins), but 3 + 3 uses only two. To trust greedy, you need a reason it works, like an exchange argument ("swapping any choice for the greedy one never makes things worse"). If you can't find one, try DP.

## 257: How do you implement a min-heap (priority queue) in JavaScript?

JavaScript has no built-in heap, so you write one on top of an array. The parent of index `i` is `(i - 1) >> 1`, and its children are `2i + 1` and `2i + 2`.

```js
class MinHeap {
  #a = [];
  #less;

  constructor(less = (x, y) => x < y) {
    this.#less = less;
  }

  get size() {
    return this.#a.length;
  }

  peek() {
    return this.#a[0];
  }

  push(x) {
    const a = this.#a;
    a.push(x);
    let i = a.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (!this.#less(a[i], a[p])) break;
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
        const l = 2 * i + 1;
        const r = l + 1;
        let m = i;
        if (l < a.length && this.#less(a[l], a[m])) m = l;
        if (r < a.length && this.#less(a[r], a[m])) m = r;
        if (m === i) break;
        [a[i], a[m]] = [a[m], a[i]];
        i = m;
      }
    }
    return top;
  }
}
```

`push` and `pop` are O(log n), `peek` is O(1). Passing a `less` function lets you use it as a max-heap or with objects.

## 258: How do you find the top K most frequent elements?

Count with a `Map`, then pick the top K. The simplest way sorts the counts (O(n log n)). Bucket sort by frequency is O(n):

```js
function topKFrequent(nums, k) {
  const counts = new Map();
  for (const x of nums) counts.set(x, (counts.get(x) ?? 0) + 1);
  const buckets = Array.from({ length: nums.length + 1 }, () => []);
  for (const [value, count] of counts) buckets[count].push(value);
  const result = [];
  for (let c = buckets.length - 1; c > 0 && result.length < k; c--) {
    result.push(...buckets[c]);
  }
  return result.slice(0, k);
}

topKFrequent([1, 1, 1, 2, 2, 3], 2); // [1, 2]
```

A min-heap of size k is a third option, O(n log k), and works well when data arrives as a stream.

## 259: How do you find the kth largest element in an array?

Three common answers:

1. Sort and take index `n - k`: O(n log n), simplest.
2. Keep a min-heap of size k: push each number, pop when the size goes over k. The top is the answer. O(n log k).
3. Quickselect: partition like quick sort, but only recurse into the side that contains the answer. O(n) on average, O(n²) worst case.

```js
function kthLargest(nums, k) {
  const heap = new MinHeap();
  for (const x of nums) {
    heap.push(x);
    if (heap.size > k) heap.pop();
  }
  return heap.peek();
}
```

Mention the trade-offs. The heap version is the usual favorite because it is safe and works on streams.

## 260: How do you merge k sorted arrays?

Put the first item of each array into a min-heap along with which array it came from. Pop the smallest, add it to the result, and push the next item from the same array.

```js
function mergeK(arrays) {
  const heap = new MinHeap((a, b) => a.value < b.value);
  arrays.forEach((arr, i) => {
    if (arr.length) heap.push({ value: arr[0], arr: i, idx: 0 });
  });
  const result = [];
  while (heap.size) {
    const { value, arr, idx } = heap.pop();
    result.push(value);
    if (idx + 1 < arrays[arr].length) {
      heap.push({ value: arrays[arr][idx + 1], arr, idx: idx + 1 });
    }
  }
  return result;
}
```

O(N log k) where N is the total number of items. Merging the arrays two at a time in pairs also gets O(N log k). Concatenating and sorting is O(N log N).

## 261: How do bitwise operators work in JavaScript, and what is the catch?

`&`, `|`, `^`, `~`, `<<`, `>>` and `>>>` convert numbers to 32-bit signed integers (except `>>>`, which gives an unsigned result), do the operation and convert back. So anything above 2³¹ − 1 or with decimals gets cut down:

```js
(2 ** 31) | 0; // -2147483648
5.7 | 0; // 5
-1 >>> 0; // 4294967295
```

They are useful for flags, small sets and tricks like `x & 1`, but don't use them on large numbers or IDs. For bigger values, `BigInt` supports the same operators.

## 262: How do you find the one number that appears once when every other number appears twice?

XOR all the numbers. `x ^ x` is 0 and `x ^ 0` is x, so the pairs cancel out:

```js
const singleNumber = (nums) => nums.reduce((acc, x) => acc ^ x, 0);

singleNumber([4, 1, 2, 1, 2]); // 4
```

O(n) time and O(1) space. A `Set` or a count map works too but uses O(n) memory. This works only for 32-bit integers.

## 263: How do you count the number of 1 bits in a number?

```js
function countBits(n) {
  let count = 0;
  while (n !== 0) {
    n &= n - 1; // removes the lowest set bit
    count++;
  }
  return count;
}

countBits(11); // 3 (1011)
```

This loop runs once per set bit, not once per bit. A simpler way is `n.toString(2).replaceAll("0", "").length`. Both work for non-negative 32-bit integers.

## 264: How can you use a bitmask to represent a set of options?

Give each option its own bit and combine them with `|`:

```js
const READ = 1 << 0; // 1
const WRITE = 1 << 1; // 2
const ADMIN = 1 << 2; // 4

let perms = READ | WRITE; // 3
const canWrite = (perms & WRITE) !== 0; // true
perms &= ~WRITE; // remove WRITE
perms ^= ADMIN; // toggle ADMIN
```

Checking, adding and removing are O(1), and the whole set fits in one number. React uses lanes and flags stored this way internally. You can also loop from 0 to 2ⁿ − 1 to go through every subset of n items.

## 265: How do you implement debounce?

Debounce delays a function until it hasn't been called for a set time. It's used for search inputs and resize handlers.

```js
function debounce(fn, wait) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), wait);
  };
}

const onSearch = debounce((q) => fetchResults(q), 300);
input.addEventListener("input", (e) => onSearch(e.target.value));
```

Every call resets the timer, so the function only runs after the user stops typing for 300 ms. Common follow-ups are a `leading` option (run on the first call) and a `cancel` method.

## 266: How do you implement throttle?

Throttle runs a function at most once per time window, no matter how often it's called. It's used for scroll and mousemove handlers.

```js
function throttle(fn, wait) {
  let last = 0;
  let timer = null;
  let lastArgs;
  return function (...args) {
    lastArgs = args;
    const remaining = wait - (Date.now() - last);
    if (remaining <= 0) {
      clearTimeout(timer);
      timer = null;
      last = Date.now();
      fn.apply(this, args);
    } else if (!timer) {
      timer = setTimeout(() => {
        last = Date.now();
        timer = null;
        fn.apply(this, lastArgs);
      }, remaining);
    }
  };
}
```

This version also runs one last time at the end of the window with the latest arguments (a trailing call), so the final scroll position isn't lost. For animation work, `requestAnimationFrame` is often a better fit than a fixed time.

## 267: How do you implement Promise.all yourself?

```js
function promiseAll(items) {
  return new Promise((resolve, reject) => {
    const results = [];
    let remaining = 0;
    let index = 0;
    for (const item of items) {
      const i = index++;
      remaining++;
      Promise.resolve(item).then((value) => {
        results[i] = value;
        if (--remaining === 0) resolve(results);
      }, reject);
    }
    if (remaining === 0) resolve(results);
  });
}
```

Keep results in the original order by index, not in the order they finish. Reject as soon as one fails. Handle the empty input case, which resolves right away with `[]`.

## 268: How do you run async tasks with a concurrency limit?

Start up to `limit` workers. Each worker takes the next task until none are left:

```js
async function runWithLimit(tasks, limit) {
  const results = new Array(tasks.length);
  let next = 0;
  async function worker() {
    while (next < tasks.length) {
      const i = next++;
      results[i] = await tasks[i]();
    }
  }
  await Promise.all(
    Array.from({ length: Math.min(limit, tasks.length) }, worker),
  );
  return results;
}

// tasks are functions that return promises
await runWithLimit(
  urls.map((u) => () => fetch(u)),
  3,
);
```

`next++` is safe here because JavaScript runs one piece of code at a time. This is useful for uploads or API calls when you don't want to send 500 requests at once. If one task fails, this version rejects the whole thing. Use `Promise.allSettled`-style handling if you need all results.

## 269: How do you retry an async call with exponential backoff?

```js
async function retry(fn, { retries = 3, base = 200 } = {}) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt >= retries) throw err;
      const delay = base * 2 ** attempt + Math.random() * base; // jitter
      await new Promise((r) => setTimeout(r, delay));
    }
  }
}

const data = await retry(() => fetch("/api/data").then((r) => r.json()));
```

The delay doubles after each failure (200, 400, 800 ms...). The random jitter stops many clients from retrying at exactly the same moment. Only retry errors that can succeed later, like network errors or 503, not 400 or 404.

## 270: How do you implement an LRU cache?

An LRU (least recently used) cache drops the item that was used longest ago when it's full. In JavaScript, `Map` keeps insertion order, so you can delete and re-insert a key to mark it as recent:

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
    this.#map.set(key, value); // move to the end (most recent)
    return value;
  }

  set(key, value) {
    this.#map.delete(key);
    this.#map.set(key, value);
    if (this.#map.size > this.capacity) {
      const oldest = this.#map.keys().next().value;
      this.#map.delete(oldest);
    }
  }
}
```

Both operations are O(1). The classic version uses a hash map plus a doubly linked list, which interviewers may ask for if they don't want you to rely on `Map` order.

## 271: How do you implement Array.prototype.reduce yourself?

```js
function reduce(arr, callback, ...init) {
  let i = 0;
  let acc;
  if (init.length) {
    acc = init[0];
  } else {
    while (i < arr.length && !(i in arr)) i++; // skip holes
    if (i >= arr.length) {
      throw new TypeError("Reduce of empty array with no initial value");
    }
    acc = arr[i++];
  }
  for (; i < arr.length; i++) {
    if (i in arr) acc = callback(acc, arr[i], i, arr);
  }
  return acc;
}
```

Using rest parameters lets you tell "no initial value" apart from an initial value of `undefined`. The `i in arr` check skips holes in sparse arrays, like the real method. Interviewers like this question because it checks edge cases.

## 272: How do you implement flat() with a depth argument?

```js
function flat(arr, depth = 1) {
  const result = [];
  for (const item of arr) {
    if (Array.isArray(item) && depth > 0) {
      result.push(...flat(item, depth - 1));
    } else {
      result.push(item);
    }
  }
  return result;
}

flat([1, [2, [3, [4]]]], 2); // [1, 2, 3, [4]]
```

An iterative version uses a stack of `[item, depth]` pairs. The built-in `flat` also removes holes from sparse arrays.

## 273: How do you implement currying?

Currying turns `f(a, b, c)` into `f(a)(b)(c)`. Keep collecting arguments until you have as many as the function expects:

```js
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) return fn.apply(this, args);
    return (...more) => curried.apply(this, [...args, ...more]);
  };
}

const add3 = curry((a, b, c) => a + b + c);
add3(1)(2)(3); // 6
add3(1, 2)(3); // 6
```

`fn.length` doesn't count rest parameters or parameters with default values, so this doesn't work well for those functions.

## 274: How do you implement compose and pipe?

```js
const pipe =
  (...fns) =>
  (x) =>
    fns.reduce((acc, fn) => fn(acc), x);
const compose =
  (...fns) =>
  (x) =>
    fns.reduceRight((acc, fn) => fn(acc), x);

const slugify = pipe(
  (s) => s.trim(),
  (s) => s.toLowerCase(),
  (s) => s.replace(/\s+/g, "-"),
);

slugify("  Hello World "); // "hello-world"
```

`pipe` runs functions left to right, `compose` right to left. They're a simple use of `reduce`.

## 275: How do you binary search over objects or dates?

Binary search works on any sorted array as long as you compare by the same key used for sorting:

```js
// events sorted by timestamp
function findFirstAfter(events, time) {
  let lo = 0;
  let hi = events.length;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (events[mid].timestamp < time) lo = mid + 1;
    else hi = mid;
  }
  return lo; // index of the first event at or after `time`
}
```

This is useful for chart tooltips (find the data point nearest to the mouse), log viewers and time-based filters. For `Date` objects, compare `date.getTime()` values.

## 276: How do you calculate pagination values?

```js
function paginate(total, page, pageSize) {
  const totalPages = Math.max(1, Math.ceil(total / pageSize));
  const current = Math.min(Math.max(1, page), totalPages);
  const start = (current - 1) * pageSize;
  const end = Math.min(start + pageSize, total);
  return { totalPages, current, start, end };
}

paginate(95, 10, 10); // { totalPages: 10, current: 10, start: 90, end: 95 }
```

Clamp the page so it stays in range, and use `Math.ceil` for the page count. The last page is often partly full, which is where off-by-one bugs come from.

## 277: How would you implement a simple fuzzy search for a list?

A simple version checks if the query letters appear in order (a subsequence) and gives a better score to matches that are close together or at the start:

```js
function fuzzyScore(query, text) {
  query = query.toLowerCase();
  text = text.toLowerCase();
  let score = 0;
  let qi = 0;
  let lastMatch = -1;
  for (let ti = 0; ti < text.length && qi < query.length; ti++) {
    if (text[ti] === query[qi]) {
      score += ti === lastMatch + 1 ? 3 : 1; // bonus for consecutive matches
      if (ti === 0) score += 2; // bonus for matching the start
      lastMatch = ti;
      qi++;
    }
  }
  return qi === query.length ? score : 0;
}

const results = items
  .map((item) => ({ item, score: fuzzyScore(query, item) }))
  .filter((r) => r.score > 0)
  .sort((a, b) => b.score - a.score);
```

This is O(n × L) for n items of length L, which is fine for a few thousand items. For bigger lists, use a prebuilt index or a library like Fuse.js.

## 278: How do you highlight search matches in text safely?

Escape special regex characters in the user's query, then split the text on the match:

```js
const escapeRegExp = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function highlightParts(text, query) {
  if (!query) return [{ text, match: false }];
  const re = new RegExp(`(${escapeRegExp(query)})`, "gi");
  return text
    .split(re)
    .filter(Boolean)
    .map((part) => ({
      text: part,
      match: part.toLowerCase() === query.toLowerCase(),
    }));
}
```

Return parts and render them with your framework (for example `<mark>` for matches), instead of building an HTML string, so you don't open an XSS hole. Without escaping, a query like `c++` throws an error. Newer engines also have the built-in `RegExp.escape`.

## 279: How do you calculate which rows to render in a virtual list with fixed row heights?

```js
function visibleRange(
  scrollTop,
  viewportHeight,
  rowHeight,
  total,
  overscan = 5,
) {
  const first = Math.floor(scrollTop / rowHeight);
  const visibleCount = Math.ceil(viewportHeight / rowHeight);
  const start = Math.max(0, first - overscan);
  const end = Math.min(total, first + visibleCount + overscan);
  return { start, end, offsetY: start * rowHeight };
}
```

You render only rows `start` to `end` and move them down by `offsetY` inside a container with the full height (`total * rowHeight`). This is O(1) per scroll. Overscan renders a few extra rows so fast scrolling doesn't show empty space. Variable heights need prefix sums and binary search.

## 280: How do you find which items were added, removed or changed between two lists?

Index both lists by id, then compare:

```js
function diffById(oldList, newList) {
  const oldMap = new Map(oldList.map((x) => [x.id, x]));
  const newMap = new Map(newList.map((x) => [x.id, x]));
  const added = newList.filter((x) => !oldMap.has(x.id));
  const removed = oldList.filter((x) => !newMap.has(x.id));
  const changed = newList.filter(
    (x) => oldMap.has(x.id) && !shallowEqual(oldMap.get(x.id), x),
  );
  return { added, removed, changed };
}
```

O(n + m) instead of O(n × m) with nested `find` calls. This is the same idea frameworks use with `key` props to match old and new list items.

## 281: How do you rotate a square matrix 90 degrees clockwise in place?

Transpose it, then reverse each row:

```js
function rotate(matrix) {
  const n = matrix.length;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
  for (const row of matrix) row.reverse();
  return matrix;
}

rotate([
  [1, 2],
  [3, 4],
]); // [[3, 1], [4, 2]]
```

O(n²) time and O(1) extra space. For counter-clockwise, reverse each row first and then transpose (or transpose and reverse the order of rows).

## 282: How do you read a matrix in spiral order?

Keep four borders and shrink them after each side:

```js
function spiral(m) {
  const result = [];
  if (m.length === 0) return result;
  let top = 0;
  let bottom = m.length - 1;
  let left = 0;
  let right = m[0].length - 1;
  while (top <= bottom && left <= right) {
    for (let c = left; c <= right; c++) result.push(m[top][c]);
    top++;
    for (let r = top; r <= bottom; r++) result.push(m[r][right]);
    right--;
    if (top <= bottom) {
      for (let c = right; c >= left; c--) result.push(m[bottom][c]);
      bottom--;
    }
    if (left <= right) {
      for (let r = bottom; r >= top; r--) result.push(m[r][left]);
      left++;
    }
  }
  return result;
}
```

The two `if` checks stop you from reading the same row or column twice in non-square matrices. O(rows × cols).

## 283: How do you set a whole row and column to zero if a cell is zero?

First record which rows and columns have a zero, then update. Don't update while you scan, or the new zeros spread everywhere.

```js
function setZeroes(m) {
  const rows = new Set();
  const cols = new Set();
  m.forEach((row, r) =>
    row.forEach((v, c) => {
      if (v === 0) {
        rows.add(r);
        cols.add(c);
      }
    }),
  );
  m.forEach((row, r) =>
    row.forEach((_, c) => {
      if (rows.has(r) || cols.has(c)) row[c] = 0;
    }),
  );
  return m;
}
```

O(rows × cols) time, O(rows + cols) space. The O(1) space version uses the first row and column as the markers.

## 284: How do you check if a Sudoku board is valid?

Check that no digit repeats in any row, column or 3×3 box. One pass with sets is enough:

```js
function isValidSudoku(board) {
  const seen = new Set();
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const v = board[r][c];
      if (v === ".") continue;
      const box = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      const keys = [`r${r}:${v}`, `c${c}:${v}`, `b${box}:${v}`];
      if (keys.some((k) => seen.has(k))) return false;
      keys.forEach((k) => seen.add(k));
    }
  }
  return true;
}
```

The box index formula `floor(r / 3) * 3 + floor(c / 3)` is the useful trick here. This checks the board is valid, not that it's solvable.

## 285: How do you generate Pascal's triangle?

Each row starts and ends with 1, and every inner value is the sum of the two values above it:

```js
function pascal(numRows) {
  const rows = [];
  for (let i = 0; i < numRows; i++) {
    const row = [1];
    for (let j = 1; j < i; j++) row.push(rows[i - 1][j - 1] + rows[i - 1][j]);
    if (i > 0) row.push(1);
    rows.push(row);
  }
  return rows;
}

pascal(4); // [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

O(n²). The value at row n, position k is "n choose k", which is useful for combinatorics questions.

## 286: How do you check if a string contains a permutation of another string?

Use a fixed-size sliding window of the length of the shorter string and compare letter counts:

```js
function checkInclusion(p, s) {
  if (p.length > s.length) return false;
  const need = new Array(26).fill(0);
  const have = new Array(26).fill(0);
  const idx = (ch) => ch.charCodeAt(0) - 97;
  for (let i = 0; i < p.length; i++) {
    need[idx(p[i])]++;
    have[idx(s[i])]++;
  }
  const same = () => need.every((n, i) => n === have[i]);
  if (same()) return true;
  for (let i = p.length; i < s.length; i++) {
    have[idx(s[i])]++;
    have[idx(s[i - p.length])]--;
    if (same()) return true;
  }
  return false;
}

checkInclusion("ab", "eidbaooo"); // true ("ba")
```

Comparing 26 counts is constant work, so the total is O(n). This assumes lowercase English letters.

## 287: When should you use an array of 26 counts instead of a Map for letter counting?

When the input is limited to lowercase (or uppercase) English letters, an array (or `Int32Array`) of 26 counts is faster and uses less memory than a `Map`, and comparing two count arrays is a fixed amount of work. Use `charCodeAt(i) - 97` as the index. As soon as the input can contain any Unicode character, mixed case or punctuation, switch to a `Map` so you don't get wrong indexes or silent bugs.

## 288: How do you turn a recursive function into an iterative one?

Replace the call stack with your own stack. Push the starting state, then loop: pop a state, process it and push the states that the recursive calls would have used.

```js
// recursive
function sumTree(node) {
  if (!node) return 0;
  return node.value + node.children.reduce((s, c) => s + sumTree(c), 0);
}

// iterative
function sumTreeIterative(root) {
  let total = 0;
  const stack = root ? [root] : [];
  while (stack.length) {
    const node = stack.pop();
    total += node.value;
    stack.push(...node.children);
  }
  return total;
}
```

This avoids stack overflow on deep data. When the order of work matters (like postorder), you may need to store extra state, such as a "visited children" flag.

## 289: Does JavaScript support tail call optimization?

The ES2015 spec includes proper tail calls in strict mode, but only Safari (JavaScriptCore) implements them. V8 (Chrome, Node.js) and SpiderMonkey (Firefox) do not. So a tail-recursive function like `const loop = (n, acc) => n === 0 ? acc : loop(n - 1, acc + n)` will still overflow the stack in Chrome for large n. Don't rely on TCO in JavaScript. Use a loop or a trampoline instead.

## 290: How can generators help with algorithms?

Generators produce values lazily, one at a time, so you can describe infinite or very long sequences without building an array:

```js
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

function* take(iter, n) {
  for (const x of iter) {
    if (n-- <= 0) return;
    yield x;
  }
}

[...take(fibonacci(), 10)]; // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

They are also handy for tree traversals (`yield*` for children), permutations, and paging through API results.

## 291: What are iterator helpers and why are they useful for algorithms?

Iterator helpers (ES2025) add methods like `map`, `filter`, `take`, `drop`, `flatMap`, `reduce`, `some`, `every`, `find` and `toArray` to iterators. Unlike array methods, they are lazy: they process one item at a time and stop as soon as they can.

```js
const firstThreeBig = Iterator.from(hugeArray.values())
  .filter((x) => x > 1000)
  .map((x) => x * 2)
  .take(3)
  .toArray();
```

No intermediate arrays are created, and the work stops after 3 matches. They're supported in current Chrome, Firefox, Safari and Node.js 22+.

## 292: What are the new Set methods?

ES2025 added set operations directly on `Set`:

```js
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

a.union(b); // Set {1, 2, 3, 4}
a.intersection(b); // Set {2, 3}
a.difference(b); // Set {1}
a.symmetricDifference(b); // Set {1, 4}
a.isSubsetOf(b); // false
a.isSupersetOf(new Set([1])); // true
a.isDisjointFrom(new Set([9])); // true
```

They return new sets and don't change the originals. Before this, you had to write these with spread and `filter`.

## 293: How do you work out the time complexity of a recursive function?

Write how much work one call does plus how many calls it makes and on what size. That's the recurrence. Then picture the recursion tree: count the levels and the work per level.

- Binary search: T(n) = T(n/2) + O(1), log n levels with constant work → O(log n).
- Merge sort: T(n) = 2T(n/2) + O(n), log n levels with n work each → O(n log n).
- Naive Fibonacci: T(n) = T(n−1) + T(n−2) + O(1), the tree roughly doubles each level → O(2ⁿ).

## 294: What is the Master Theorem?

It gives the answer for recurrences of the form T(n) = a·T(n/b) + O(nᵈ), where a is the number of subproblems, n/b their size and nᵈ the work to split and combine.

- If d > log_b(a): O(nᵈ) (the top level dominates).
- If d = log_b(a): O(nᵈ log n) (all levels equal).
- If d < log_b(a): O(n^(log_b a)) (the leaves dominate).

Merge sort has a = 2, b = 2, d = 1, so it's the middle case: O(n log n). You rarely need it in a front-end interview, but it's a quick way to check divide-and-conquer answers.

## 295: How does stable sorting help when users sort a table by several columns?

When a user clicks "Department" and then "Name", they usually expect rows to be sorted by name, and within the same name, still in department order. With a stable sort, you can just sort by the new column and the previous order stays as the tie-breaker. Since `Array.prototype.sort` is stable in all modern engines, this works out of the box. If you need full control, build a comparator from a list of sort keys instead.

## 296: What are common comparator mistakes?

- Returning a boolean: `(a, b) => a > b`. It never returns a negative number, so the result is wrong or depends on the engine.
- Using `a - b` on strings, which gives `NaN`.
- Comparators that aren't consistent, like random values or ones that change during the sort.
- Not handling `null`, `undefined` or `NaN` in the data.
- Sorting a shared array in place when other code expects the original order (use `toSorted`).

A good comparator always returns negative, zero or positive, and gives the same answer for the same pair.

## 297: How can you make sorting large lists of strings faster?

`a.localeCompare(b)` creates locale settings on every call, which is slow for thousands of items. Create one `Intl.Collator` and reuse its `compare` function:

```js
const collator = new Intl.Collator("en", {
  numeric: true,
  sensitivity: "base",
});
names.sort(collator.compare);
```

For expensive keys (like computing a value from each object), compute the keys once, sort the pairs and map back. This is called "decorate, sort, undecorate" (or the Schwartzian transform) and avoids recomputing the key O(n log n) times.

## 298: How do you check if a string has balanced brackets while ignoring brackets inside quotes?

Add a small state to the stack algorithm that tracks whether you are inside a string:

```js
function balancedIgnoringStrings(code) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];
  let quote = null;
  for (let i = 0; i < code.length; i++) {
    const ch = code[i];
    if (quote) {
      if (ch === "\\")
        i++; // skip escaped character
      else if (ch === quote) quote = null;
    } else if (ch === '"' || ch === "'" || ch === "`") {
      quote = ch;
    } else if ("([{".includes(ch)) {
      stack.push(ch);
    } else if (ch in pairs) {
      if (stack.pop() !== pairs[ch]) return false;
    }
  }
  return stack.length === 0 && !quote;
}
```

This is a tiny state machine, the same idea that tokenizers and syntax highlighters use. O(n).

## 299: How do you implement an undo/redo history?

Use two stacks. Every new action is pushed to the undo stack and clears the redo stack. Undo pops from undo and pushes to redo; redo does the opposite.

```js
class History {
  #undo = [];
  #redo = [];

  constructor(state) {
    this.state = state;
  }

  set(next) {
    this.#undo.push(this.state);
    this.#redo = [];
    this.state = next;
  }

  undo() {
    if (!this.#undo.length) return;
    this.#redo.push(this.state);
    this.state = this.#undo.pop();
  }

  redo() {
    if (!this.#redo.length) return;
    this.#undo.push(this.state);
    this.state = this.#redo.pop();
  }
}
```

Storing full snapshots is simple and works well with immutable state. For big documents, store commands or diffs instead, and cap the stack size.

## 300: How do you decide which data structure to use for a problem?

Look at the operations you need most often:

- fast lookup by key or "seen before?" → `Map` / `Set`
- keep order and access by index → array
- add/remove at the end → array as a stack
- FIFO processing → queue
- always get the smallest or largest → heap
- hierarchy → tree
- relationships with cycles → graph
- prefix search → trie

Then check the sizes. For 50 items, the simplest code wins. For 1,000,000 items, the complexity of each operation matters.

---

# Advanced Questions (301-450)

## 301: How does Dijkstra's algorithm work?

Dijkstra finds the shortest paths from one start node to all other nodes in a graph with non-negative edge weights. It keeps a tentative distance for every node, always picks the unvisited node with the smallest distance, and then tries to improve the distances of its neighbors ("relaxation"). Once a node is picked, its distance is final. With a binary heap it runs in O((V + E) log V).

## 302: How do you implement Dijkstra in JavaScript?

Use the min-heap from earlier with `[distance, node]` pairs. Since there is no "decrease key", just push a new pair and skip stale ones when you pop them:

```js
function dijkstra(graph, start) {
  // graph: Map<node, Array<[neighbor, weight]>>
  const dist = new Map([[start, 0]]);
  const heap = new MinHeap((a, b) => a[0] < b[0]);
  heap.push([0, start]);
  while (heap.size) {
    const [d, node] = heap.pop();
    if (d > (dist.get(node) ?? Infinity)) continue; // stale entry
    for (const [next, w] of graph.get(node) ?? []) {
      const nd = d + w;
      if (nd < (dist.get(next) ?? Infinity)) {
        dist.set(next, nd);
        heap.push([nd, next]);
      }
    }
  }
  return dist;
}
```

To get the actual path, also store `prev.set(next, node)` when you improve a distance. Using an array scan instead of a heap gives O(V²), which is fine for small or dense graphs.

## 303: Why does Dijkstra fail with negative weights, and what do you use instead?

Dijkstra assumes that once a node has the smallest distance, no later path can make it shorter. A negative edge breaks that: a longer path can become cheaper after it, but the node is already finalized. Use Bellman-Ford instead, which relaxes all edges V − 1 times:

```js
function bellmanFord(n, edges, start) {
  const dist = new Array(n).fill(Infinity);
  dist[start] = 0;
  for (let i = 0; i < n - 1; i++) {
    for (const [u, v, w] of edges) {
      if (dist[u] + w < dist[v]) dist[v] = dist[u] + w;
    }
  }
  for (const [u, v, w] of edges) {
    if (dist[u] + w < dist[v]) throw new Error("Negative cycle");
  }
  return dist;
}
```

O(V × E). The extra pass detects negative cycles, where no shortest path exists.

## 304: What is A* search?

A* is Dijkstra with a hint. It orders nodes by `g + h`, where g is the cost from the start so far and h is a heuristic estimate of the cost to the goal. If h never overestimates the real cost (it's "admissible"), A* still finds the shortest path, but explores far fewer nodes because it heads toward the goal. On grids, Manhattan distance (4 directions) or Euclidean distance are common heuristics. It's used in games and map routing. With h = 0 it becomes Dijkstra.

## 305: What is the Floyd-Warshall algorithm?

It finds shortest paths between every pair of nodes. For each node k, it checks whether going through k makes the path from i to j shorter:

```js
function floydWarshall(dist) {
  // dist: n x n matrix, Infinity for no edge, 0 on the diagonal
  const n = dist.length;
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][k] + dist[k][j] < dist[i][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }
  return dist;
}
```

O(V³) time and O(V²) space, so it's for small graphs (a few hundred nodes). The k loop must be the outer one. It handles negative edges but not negative cycles.

## 306: What is Union-Find (disjoint set union)?

Union-Find tracks which items belong to the same group. `find(x)` returns the group's representative, `union(a, b)` merges two groups.

```js
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(0);
  }

  find(x) {
    while (this.parent[x] !== x) {
      this.parent[x] = this.parent[this.parent[x]]; // path halving
      x = this.parent[x];
    }
    return x;
  }

  union(a, b) {
    let ra = this.find(a);
    let rb = this.find(b);
    if (ra === rb) return false;
    if (this.rank[ra] < this.rank[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    if (this.rank[ra] === this.rank[rb]) this.rank[ra]++;
    return true;
  }
}
```

With path compression and union by rank, each operation is almost O(1) (inverse Ackermann, which is below 5 for any realistic n). It's used for Kruskal's algorithm, connected components and grouping duplicates.

## 307: How does Kruskal's algorithm find a minimum spanning tree?

A minimum spanning tree connects all nodes with the least total edge weight and no cycles. Kruskal sorts the edges by weight and adds each edge if it connects two different groups:

```js
function kruskal(n, edges) {
  const uf = new UnionFind(n);
  const tree = [];
  let total = 0;
  for (const [u, v, w] of edges.toSorted((a, b) => a[2] - b[2])) {
    if (uf.union(u, v)) {
      tree.push([u, v, w]);
      total += w;
      if (tree.length === n - 1) break;
    }
  }
  return { tree, total };
}
```

O(E log E) because of the sort. It's a greedy algorithm that is proven to be correct. Real uses include network design and clustering.

## 308: How does Prim's algorithm differ from Kruskal's?

Prim grows one tree from a starting node. At each step it adds the cheapest edge that connects the tree to a new node, using a min-heap of edges. Kruskal works on edges globally and merges many small trees. Prim is usually better for dense graphs with an adjacency list or matrix. Kruskal is simpler when you already have a list of edges and the graph is sparse. Both are O(E log V) with a heap.

## 309: How do you detect a cycle in an undirected graph?

Two common ways:

1. **Union-Find:** for each edge, if both ends already have the same root, the edge closes a cycle.
2. **DFS:** if you reach a visited node that is not the parent you came from, there's a cycle.

```js
function hasCycleUndirected(n, edges) {
  const uf = new UnionFind(n);
  for (const [a, b] of edges) {
    if (!uf.union(a, b)) return true;
  }
  return false;
}
```

You can't use the "in progress" coloring from directed graphs directly, because in an undirected graph every edge leads back to the parent.

## 310: How do you check if a graph is bipartite?

A graph is bipartite if you can color the nodes with two colors so no edge connects two nodes of the same color. Do BFS and give each neighbor the opposite color:

```js
function isBipartite(graph) {
  // graph: array of neighbor arrays
  const color = new Array(graph.length).fill(-1);
  for (let start = 0; start < graph.length; start++) {
    if (color[start] !== -1) continue;
    color[start] = 0;
    const queue = [start];
    for (let h = 0; h < queue.length; h++) {
      const node = queue[h];
      for (const next of graph[node]) {
        if (color[next] === -1) {
          color[next] = 1 - color[node];
          queue.push(next);
        } else if (color[next] === color[node]) {
          return false;
        }
      }
    }
  }
  return true;
}
```

O(V + E). The outer loop handles graphs with several disconnected parts. A graph is bipartite exactly when it has no odd-length cycle.

## 311: What are strongly connected components and how do you find them?

In a directed graph, a strongly connected component (SCC) is a group of nodes where every node can reach every other node. Tarjan's algorithm finds them in one DFS using discovery times and "low-link" values. Kosaraju's algorithm does two DFS passes: one on the graph to get finishing order, and one on the reversed graph in reverse finishing order. Both are O(V + E). In practice, SCCs show up when you need to find groups of modules that import each other in a cycle.

## 312: What is bidirectional BFS?

You run BFS from the start and from the goal at the same time, and stop when the two searches meet. If each node has b neighbors and the path length is d, normal BFS explores about bᵈ nodes, while two searches explore about 2 × b^(d/2), which is much smaller. It works when you know the goal and can walk edges backward. Word Ladder and "degrees of separation" in social graphs are good examples.

## 313: How do you solve Word Ladder?

Find the shortest number of steps to change one word into another, changing one letter at a time, with each step being a valid word. It's a BFS where words are nodes and one-letter changes are edges.

```js
function ladderLength(begin, end, wordList) {
  const words = new Set(wordList);
  if (!words.has(end)) return 0;
  let level = [begin];
  let steps = 1;
  const letters = "abcdefghijklmnopqrstuvwxyz";
  while (level.length) {
    const next = [];
    for (const word of level) {
      if (word === end) return steps;
      for (let i = 0; i < word.length; i++) {
        for (const ch of letters) {
          const candidate = word.slice(0, i) + ch + word.slice(i + 1);
          if (words.has(candidate)) {
            words.delete(candidate); // mark visited
            next.push(candidate);
          }
        }
      }
    }
    level = next;
    steps++;
  }
  return 0;
}
```

Generating neighbors by changing letters is O(L × 26) per word, which is much faster than comparing against every word. Deleting from the set doubles as the visited check.

## 314: How do you clone a graph?

Walk the graph and keep a `Map` from original node to its copy, so each node is copied once and cycles don't loop forever:

```js
function cloneGraph(node, copies = new Map()) {
  if (!node) return null;
  if (copies.has(node)) return copies.get(node);
  const copy = { value: node.value, neighbors: [] };
  copies.set(node, copy); // set before recursing to handle cycles
  for (const n of node.neighbors) copy.neighbors.push(cloneGraph(n, copies));
  return copy;
}
```

O(V + E). The same "map old to new" idea is how `structuredClone` handles circular references.

## 315: What is a trie and how do you implement one?

A trie (prefix tree) stores strings character by character. Each node has children keyed by character and a flag for "a word ends here".

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

  #walk(prefix) {
    let node = this.#root;
    for (const ch of prefix) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node;
  }

  has(word) {
    return this.#walk(word)?.end === true;
  }

  startsWith(prefix) {
    return this.#walk(prefix) !== null;
  }
}
```

Insert and lookup are O(L) for a word of length L, no matter how many words are stored.

## 316: How do you build autocomplete with a trie?

Walk down to the node for the prefix, then collect words below it with DFS, stopping when you have enough results:

```js
// add this method to the Trie class
suggest(prefix, limit = 10) {
  const start = this.#walk(prefix);
  const results = [];
  const dfs = (node, path) => {
    if (results.length >= limit) return;
    if (node.end) results.push(path);
    for (const [ch, child] of node.children) dfs(child, path + ch);
  };
  if (start) dfs(start, prefix);
  return results;
}
```

To rank by popularity, store a count on each end node, or keep the top few words in each node so you don't need to search the subtree at all. That trades memory for speed.

## 317: Trie or sorted array with binary search for autocomplete?

A sorted array of words plus binary search (lower bound for the prefix, then read forward while words still start with it) uses much less memory, is simple, and is fast enough for tens of thousands of words. A trie gives O(L) lookups independent of list size and makes it easy to attach per-prefix data like top suggestions, but each node is an object with a `Map`, which is heavy in JavaScript. For a front-end with a static list, the sorted array is often the better choice. For live, ranked suggestions over huge lists, a trie (or a compressed radix tree) wins.

## 318: How does the KMP string search algorithm work?

KMP (Knuth-Morris-Pratt) avoids re-checking characters after a mismatch. It precomputes, for each position in the pattern, the length of the longest proper prefix that is also a suffix (the "failure" table). On a mismatch, it jumps back in the pattern using that table instead of moving back in the text.

```js
function kmpSearch(text, pattern) {
  if (pattern === "") return 0;
  const fail = new Array(pattern.length).fill(0);
  for (let i = 1, k = 0; i < pattern.length; i++) {
    while (k > 0 && pattern[i] !== pattern[k]) k = fail[k - 1];
    if (pattern[i] === pattern[k]) k++;
    fail[i] = k;
  }
  for (let i = 0, k = 0; i < text.length; i++) {
    while (k > 0 && text[i] !== pattern[k]) k = fail[k - 1];
    if (text[i] === pattern[k]) k++;
    if (k === pattern.length) return i - k + 1;
  }
  return -1;
}
```

O(n + m) in all cases. The naive approach can be O(n × m) on inputs like `"aaaa...ab"`.

## 319: How does Rabin-Karp work?

Rabin-Karp compares hashes instead of strings. It computes a hash of the pattern and a rolling hash of each window of the text. Moving the window by one character updates the hash in O(1) (remove the leftmost character, add the new one). Only when hashes match does it compare the actual strings, to rule out collisions. Average time is O(n + m). It's good for searching many patterns at once and for finding duplicate substrings. In JavaScript, keep the hash under a modulus so it stays within safe integer range.

## 320: How do you find the longest common substring of two strings?

Unlike a subsequence, a substring must be continuous. `dp[i][j]` is the length of the common substring ending at `a[i - 1]` and `b[j - 1]`:

```js
function longestCommonSubstring(a, b) {
  let best = 0;
  let endA = 0;
  let prev = new Array(b.length + 1).fill(0);
  for (let i = 1; i <= a.length; i++) {
    const cur = new Array(b.length + 1).fill(0);
    for (let j = 1; j <= b.length; j++) {
      if (a[i - 1] === b[j - 1]) {
        cur[j] = prev[j - 1] + 1;
        if (cur[j] > best) {
          best = cur[j];
          endA = i;
        }
      }
    }
    prev = cur;
  }
  return a.slice(endA - best, endA);
}
```

The difference from LCS is that a mismatch resets the value to 0 instead of carrying the max. O(n × m) time. Suffix arrays or suffix automata can do it faster but are rarely expected.

## 321: What is catastrophic backtracking in regular expressions?

JavaScript's regex engine uses backtracking. Patterns with nested or overlapping quantifiers, like `/^(a+)+$/` or `/(\w+\s?)*$/`, can try an exponential number of ways to match when the input almost matches but fails at the end. A string of 30 `a`s followed by `!` can freeze the page for seconds. If the regex runs on user input, this is a denial of service bug called ReDoS. Avoid nested quantifiers, make alternatives not overlap, limit the input length, and test regexes with tools that detect this.

## 322: What is a segment tree?

A segment tree stores answers for ranges (sum, min, max) in a binary tree, so you can both query a range and update a single value in O(log n).

```js
class SegmentTree {
  constructor(arr) {
    this.n = arr.length;
    this.tree = new Array(2 * this.n).fill(0);
    for (let i = 0; i < this.n; i++) this.tree[this.n + i] = arr[i];
    for (let i = this.n - 1; i > 0; i--) {
      this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
    }
  }

  update(i, value) {
    i += this.n;
    this.tree[i] = value;
    for (i >>= 1; i > 0; i >>= 1) {
      this.tree[i] = this.tree[2 * i] + this.tree[2 * i + 1];
    }
  }

  query(l, r) {
    // sum of [l, r)
    let sum = 0;
    for (l += this.n, r += this.n; l < r; l >>= 1, r >>= 1) {
      if (l & 1) sum += this.tree[l++];
      if (r & 1) sum += this.tree[--r];
    }
    return sum;
  }
}
```

This is the compact bottom-up version. Prefix sums are faster for queries but need O(n) to update. A segment tree is the middle ground when you have many of both.

## 323: What is a Fenwick tree (Binary Indexed Tree)?

A Fenwick tree also supports prefix sums with updates in O(log n), using less code and memory than a segment tree:

```js
class Fenwick {
  constructor(n) {
    this.tree = new Array(n + 1).fill(0);
  }

  add(i, delta) {
    for (i++; i < this.tree.length; i += i & -i) this.tree[i] += delta;
  }

  prefixSum(i) {
    // sum of [0, i]
    let sum = 0;
    for (i++; i > 0; i -= i & -i) sum += this.tree[i];
    return sum;
  }
}
```

`i & -i` gives the lowest set bit, which decides the range each slot covers. It works for sums (and other operations that can be undone), but not for min or max over arbitrary ranges, where a segment tree is needed.

## 324: When would you choose prefix sums, a Fenwick tree or a segment tree?

- **Prefix sums:** data doesn't change, many range queries. O(1) query, O(n) update.
- **Fenwick tree:** sums with frequent updates. O(log n) for both, tiny code.
- **Segment tree:** frequent updates and queries for min, max, GCD or custom merges, or range updates with lazy propagation. O(log n), more code.

For a dashboard that recalculates totals over a time range while new data comes in, a Fenwick tree is a good fit. For a static chart, prefix sums are enough.

## 325: How does Quickselect work, and what is its worst case?

Quickselect finds the kth smallest item. It partitions like quick sort, but only recurses into the side that contains index k:

```js
function quickselect(arr, k) {
  let lo = 0;
  let hi = arr.length - 1;
  while (lo < hi) {
    const p = lo + Math.floor(Math.random() * (hi - lo + 1));
    [arr[p], arr[hi]] = [arr[hi], arr[p]];
    let store = lo;
    for (let i = lo; i < hi; i++) {
      if (arr[i] < arr[hi]) {
        [arr[i], arr[store]] = [arr[store], arr[i]];
        store++;
      }
    }
    [arr[store], arr[hi]] = [arr[hi], arr[store]];
    if (store === k) return arr[k];
    if (store < k) lo = store + 1;
    else hi = store - 1;
  }
  return arr[lo];
}
```

Average O(n) because each step throws away part of the array. Worst case is O(n²) with bad pivots, which a random pivot makes very unlikely. Median of medians guarantees O(n) but is slower in practice.

## 326: How do you find the median of two sorted arrays in O(log(min(n, m)))?

Binary search for a cut in the smaller array such that everything on the left of both cuts is less than or equal to everything on the right:

```js
function findMedian(a, b) {
  if (a.length > b.length) [a, b] = [b, a];
  const total = a.length + b.length;
  const half = Math.floor((total + 1) / 2);
  let lo = 0;
  let hi = a.length;
  while (lo <= hi) {
    const i = (lo + hi) >> 1; // items taken from a
    const j = half - i; // items taken from b
    const aLeft = i > 0 ? a[i - 1] : -Infinity;
    const aRight = i < a.length ? a[i] : Infinity;
    const bLeft = j > 0 ? b[j - 1] : -Infinity;
    const bRight = j < b.length ? b[j] : Infinity;
    if (aLeft <= bRight && bLeft <= aRight) {
      return total % 2
        ? Math.max(aLeft, bLeft)
        : (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2;
    }
    if (aLeft > bRight) hi = i - 1;
    else lo = i + 1;
  }
}
```

The `Infinity` sentinels remove most edge cases. Merging both arrays is O(n + m), which is a fine first answer.

## 327: How do you keep track of the median of a stream of numbers?

Use two heaps: a max-heap for the smaller half and a min-heap for the larger half. Keep their sizes within one of each other.

```js
class RunningMedian {
  low = new MinHeap((a, b) => a > b); // max-heap
  high = new MinHeap((a, b) => a < b); // min-heap

  add(x) {
    if (this.low.size === 0 || x <= this.low.peek()) this.low.push(x);
    else this.high.push(x);
    if (this.low.size > this.high.size + 1) this.high.push(this.low.pop());
    else if (this.high.size > this.low.size) this.low.push(this.high.pop());
  }

  median() {
    if (this.low.size > this.high.size) return this.low.peek();
    return (this.low.peek() + this.high.peek()) / 2;
  }
}
```

`add` is O(log n) and `median` is O(1). It's useful for live metrics, like the median response time in a monitoring panel.

## 328: How do you find the maximum in every sliding window of size k?

Use a deque of indexes whose values are in decreasing order. The front is always the max of the current window.

```js
function maxSlidingWindow(nums, k) {
  const deque = []; // indexes
  let head = 0;
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    if (head < deque.length && deque[head] <= i - k) head++; // out of window
    while (deque.length > head && nums[deque.at(-1)] <= nums[i]) deque.pop();
    deque.push(i);
    if (i >= k - 1) result.push(nums[deque[head]]);
  }
  return result;
}

maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3); // [3, 3, 5, 5, 6, 7]
```

Each index is added and removed once, so it's O(n). Using a head index instead of `shift` keeps removals from the front O(1).

## 329: How do you find the largest rectangle in a histogram?

Use a monotonic increasing stack of indexes. When a shorter bar arrives, pop taller bars and compute the rectangle each popped bar can form:

```js
function largestRectangle(heights) {
  const stack = [];
  let best = 0;
  for (let i = 0; i <= heights.length; i++) {
    const h = i === heights.length ? 0 : heights[i];
    while (stack.length && heights[stack.at(-1)] > h) {
      const height = heights[stack.pop()];
      const left = stack.length ? stack.at(-1) + 1 : 0;
      best = Math.max(best, height * (i - left));
    }
    stack.push(i);
  }
  return best;
}

largestRectangle([2, 1, 5, 6, 2, 3]); // 10
```

The extra bar of height 0 at the end flushes the stack. O(n). The same idea solves "maximal rectangle of 1s in a matrix" row by row.

## 330: How do you solve Trapping Rain Water?

Water above each bar is `min(maxLeft, maxRight) - height`. With two pointers you can do it in one pass and O(1) space:

```js
function trap(height) {
  let l = 0;
  let r = height.length - 1;
  let leftMax = 0;
  let rightMax = 0;
  let water = 0;
  while (l < r) {
    if (height[l] < height[r]) {
      leftMax = Math.max(leftMax, height[l]);
      water += leftMax - height[l];
      l++;
    } else {
      rightMax = Math.max(rightMax, height[r]);
      water += rightMax - height[r];
      r--;
    }
  }
  return water;
}

trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]); // 6
```

The side with the lower wall is the limiting one, so you can safely compute its water using only its own max.

## 331: How do you build an LRU cache with O(1) operations without relying on Map order?

Combine a hash map (key → node) with a doubly linked list ordered by use. The head is the most recent, the tail is the least recent.

```js
class LRU {
  #map = new Map();
  #head = { prev: null, next: null };
  #tail = { prev: null, next: null };

  constructor(capacity) {
    this.capacity = capacity;
    this.#head.next = this.#tail;
    this.#tail.prev = this.#head;
  }

  #unlink(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  #addFront(node) {
    node.next = this.#head.next;
    node.prev = this.#head;
    this.#head.next.prev = node;
    this.#head.next = node;
  }

  get(key) {
    const node = this.#map.get(key);
    if (!node) return undefined;
    this.#unlink(node);
    this.#addFront(node);
    return node.value;
  }

  set(key, value) {
    let node = this.#map.get(key);
    if (node) {
      node.value = value;
      this.#unlink(node);
    } else {
      node = { key, value };
      this.#map.set(key, node);
      if (this.#map.size > this.capacity) {
        const lru = this.#tail.prev;
        this.#unlink(lru);
        this.#map.delete(lru.key);
      }
    }
    this.#addFront(node);
  }
}
```

The dummy head and tail nodes remove all `null` checks. Storing the key in the node is needed so you can delete it from the map when you evict.

## 332: How would you implement an LFU (least frequently used) cache?

Keep three things: a map from key to `{ value, freq }`, a map from frequency to an ordered set of keys (a `Set` keeps insertion order, so the first key is the least recent at that frequency), and the current minimum frequency.

- `get`: move the key from `freq` to `freq + 1`. If the old frequency set is now empty and it was the minimum, increase the minimum.
- `set` on a new key when full: evict the first key from the set at the minimum frequency, then insert the new key with frequency 1 and set the minimum to 1.

All operations are O(1). LFU keeps popular items longer than LRU, but items that were popular long ago can stay forever unless you add aging.

## 333: What is reservoir sampling?

It picks k random items from a stream of unknown length, with each item equally likely, using O(k) memory:

```js
function reservoirSample(iterable, k) {
  const sample = [];
  let i = 0;
  for (const item of iterable) {
    if (i < k) sample.push(item);
    else {
      const j = Math.floor(Math.random() * (i + 1));
      if (j < k) sample[j] = item;
    }
    i++;
  }
  return sample;
}
```

Item number i (0-based) replaces a sample slot with probability k/(i + 1), which works out to equal chances for everyone. It's useful for sampling logs, analytics events or a random subset of rows to preview.

## 334: What is a Bloom filter?

A Bloom filter is a bit array plus several hash functions. To add an item, set the bits at all its hash positions. To check an item, see if all those bits are set. It can say "definitely not present" or "maybe present", never a false "no". It uses far less memory than a `Set`, at the cost of some false positives that you tune with the size and number of hashes. Browsers have used them for things like checking URLs against a block list before making a slower exact check.

## 335: How do you write a simple string hash function, and what are its limits?

```js
function djb2(str) {
  let hash = 5381;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) + hash + str.charCodeAt(i)) | 0; // hash * 33 + c
  }
  return hash >>> 0; // unsigned 32-bit
}
```

`| 0` keeps the value a 32-bit integer so it doesn't lose precision. This is fine for bucketing, cache keys and Bloom filters, but it is not secure: collisions are easy to create on purpose. For security (passwords, integrity checks) use `crypto.subtle.digest("SHA-256", ...)`.

## 336: What is hash flooding and why does it matter for JavaScript objects and Maps?

If an attacker can choose keys that all hash to the same bucket, a hash table degrades from O(1) to O(n) per operation, and a few thousand crafted keys can make a server spend seconds on one request. This hit many languages around 2011, including Node.js. Modern engines use randomized hash seeds so attackers can't predict collisions. In your own code, don't build a custom hash table keyed by untrusted input with a simple hash like djb2, and limit the number of keys you accept, for example in parsed JSON or query strings.

## 337: What are the memory risks of memoization, and how do you limit them?

An unbounded cache grows forever and keeps every argument and result alive. In a long-running SPA this becomes a memory leak. Ways to limit it:

- use an LRU cache with a maximum size
- add a time-to-live and drop old entries
- use a `WeakMap` when keys are objects, so entries go away when the object is garbage collected
- scope the cache to a component or request instead of a module-level variable

Also remember that memoizing cheap functions can be slower than recomputing, because the key building and lookup cost more than the work itself.

## 338: How do you solve Word Break?

Can a string be split into words from a dictionary? `dp[i]` is true if the first i characters can be split:

```js
function wordBreak(s, words) {
  const dict = new Set(words);
  const maxLen = Math.max(0, ...words.map((w) => w.length));
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;
  for (let i = 1; i <= s.length; i++) {
    for (let j = Math.max(0, i - maxLen); j < i; j++) {
      if (dp[j] && dict.has(s.slice(j, i))) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[s.length];
}

wordBreak("applepenapple", ["apple", "pen"]); // true
```

Limiting `j` by the longest word length cuts the work a lot. Plain recursion without memoization is exponential on inputs like `"aaaa...ab"`.

## 339: How do you find the longest increasing subsequence in O(n log n)?

Keep an array `tails` where `tails[i]` is the smallest possible tail of an increasing subsequence of length i + 1. For each number, binary search for where it fits and replace that value:

```js
function lisLength(nums) {
  const tails = [];
  for (const x of nums) {
    let lo = 0;
    let hi = tails.length;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      if (tails[mid] < x) lo = mid + 1;
      else hi = mid;
    }
    tails[lo] = x;
  }
  return tails.length;
}
```

`tails` is not the actual subsequence, only its length is correct. To rebuild the sequence, also store, for each item, the index of its predecessor. This algorithm is used by Vue 3 and Inferno to move the fewest DOM nodes when a keyed list is reordered.

## 340: How do you reconstruct the actual edits from an edit distance table?

Keep the full DP table, then walk back from the bottom-right corner. At each cell, see which neighbor produced the value: diagonal with equal characters is "keep", diagonal plus one is "replace", up is "delete", left is "insert".

```js
function editScript(a, b) {
  const dp = Array.from({ length: a.length + 1 }, (_, i) =>
    Array.from({ length: b.length + 1 }, (_, j) =>
      i === 0 ? j : j === 0 ? i : 0,
    ),
  );
  for (let i = 1; i <= a.length; i++) {
    for (let j = 1; j <= b.length; j++) {
      dp[i][j] =
        a[i - 1] === b[j - 1]
          ? dp[i - 1][j - 1]
          : 1 + Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
    }
  }

  const ops = [];
  let i = a.length;
  let j = b.length;
  while (i > 0 || j > 0) {
    if (i > 0 && j > 0 && a[i - 1] === b[j - 1]) {
      ops.push(["keep", a[i - 1]]);
      i--;
      j--;
    } else if (i > 0 && j > 0 && dp[i][j] === dp[i - 1][j - 1] + 1) {
      ops.push(["replace", a[i - 1], b[j - 1]]);
      i--;
      j--;
    } else if (i > 0 && dp[i][j] === dp[i - 1][j] + 1) {
      ops.push(["delete", a[i - 1]]);
      i--;
    } else {
      ops.push(["insert", b[j - 1]]);
      j--;
    }
  }
  return ops.reverse();
}
```

You need O(n × m) memory to do this, which is why the space-optimized version only gives the number.

## 341: How do text diff tools like git diff work?

Most use Myers' diff algorithm. It finds the shortest edit script (fewest inserts and deletes) between two sequences of lines by exploring "diagonals" of the edit graph in order of how many edits they need. It runs in O((n + m) × d), where d is the number of differences, so it is very fast when files are similar, which is the common case. Libraries like `diff` (jsdiff) use it in JavaScript. Variants such as patience diff and histogram diff produce output that is easier for humans to read when code blocks move around.

## 342: Why can't frameworks use a full tree diff algorithm for the virtual DOM?

The best known algorithms for the minimal edit distance between two general trees are around O(n³), which is far too slow for thousands of nodes on every render. React and other frameworks use heuristics that give O(n): elements of different types produce different trees, so the whole subtree is replaced, and children in lists are matched by `key`. These rules are not always minimal, but in practice they are fast and good enough. That is why stable, unique keys matter so much for list performance.

## 343: How do keyed list updates find the minimum DOM moves?

When a keyed list is reordered, the framework matches old and new items by key. The items that don't need to move are the ones whose old positions already form an increasing sequence in the new order. Vue 3 computes the longest increasing subsequence of old indexes, keeps those nodes in place and moves only the rest. React's algorithm is simpler: it walks the new list and moves nodes whose old index is less than the last placed index, which is O(n) but can move more nodes than needed in some cases (like moving the last item to the front).

## 344: What is bitmask dynamic programming? Use the Traveling Salesman Problem as an example.

When the state includes "which items have been used" and n is small (up to about 20), you can store that set as a bitmask. For TSP, `dp[mask][i]` is the cheapest way to visit the cities in `mask` and end at city i.

```js
function tsp(dist) {
  const n = dist.length;
  const FULL = 1 << n;
  const dp = Array.from({ length: FULL }, () => new Array(n).fill(Infinity));
  dp[1][0] = 0; // start at city 0
  for (let mask = 1; mask < FULL; mask++) {
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i)) || dp[mask][i] === Infinity) continue;
      for (let j = 0; j < n; j++) {
        if (mask & (1 << j)) continue;
        const next = mask | (1 << j);
        dp[next][j] = Math.min(dp[next][j], dp[mask][i] + dist[i][j]);
      }
    }
  }
  return Math.min(...dp[FULL - 1].map((d, i) => d + dist[i][0]));
}
```

O(2ⁿ × n²), which is much better than O(n!) for brute force, but still only works for small n.

## 345: How do you solve N-Queens?

Place one queen per row and backtrack. Track used columns and both diagonals in sets so each check is O(1):

```js
function solveNQueens(n) {
  const results = [];
  const cols = new Set();
  const diag1 = new Set(); // r - c
  const diag2 = new Set(); // r + c
  const queens = [];
  const place = (r) => {
    if (r === n) {
      results.push(
        queens.map((c) => ".".repeat(c) + "Q" + ".".repeat(n - c - 1)),
      );
      return;
    }
    for (let c = 0; c < n; c++) {
      if (cols.has(c) || diag1.has(r - c) || diag2.has(r + c)) continue;
      cols.add(c);
      diag1.add(r - c);
      diag2.add(r + c);
      queens.push(c);
      place(r + 1);
      cols.delete(c);
      diag1.delete(r - c);
      diag2.delete(r + c);
      queens.pop();
    }
  };
  place(0);
  return results;
}

solveNQueens(4).length; // 2
```

The diagonal trick is the key insight: cells on the same "\" diagonal share `r - c`, and on the same "/" diagonal they share `r + c`.

## 346: How do you write a Sudoku solver?

Find an empty cell, try digits 1 to 9 that don't break the rules, recurse, and undo if it fails:

```js
function solveSudoku(board) {
  const ok = (r, c, d) => {
    const br = r - (r % 3);
    const bc = c - (c % 3);
    for (let i = 0; i < 9; i++) {
      if (board[r][i] === d || board[i][c] === d) return false;
      if (board[br + Math.floor(i / 3)][bc + (i % 3)] === d) return false;
    }
    return true;
  };
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (board[r][c] !== ".") continue;
      for (let d = 1; d <= 9; d++) {
        const ch = String(d);
        if (ok(r, c, ch)) {
          board[r][c] = ch;
          if (solveSudoku(board)) return true;
          board[r][c] = ".";
        }
      }
      return false; // no digit fits here
    }
  }
  return true; // no empty cells left
}
```

A big speedup is to always pick the empty cell with the fewest possible digits first, and to track row/column/box usage with bitmasks instead of scanning.

## 347: What is pruning in backtracking and why does it matter?

Pruning means stopping a branch as soon as you know it can't lead to a valid or better answer. Examples: stop when the remaining sum is negative in combination sum, skip duplicates after sorting, stop when the current cost is already above the best found (branch and bound), or check constraints when you place an item rather than at the end. The worst case is still exponential, but good pruning can make the real running time thousands of times smaller.

## 348: How do you find the minimum number of meeting rooms needed?

Sort meetings by start time and keep a min-heap of end times for rooms in use. If the earliest ending room is free, reuse it:

```js
function minMeetingRooms(meetings) {
  const sorted = meetings.toSorted((a, b) => a[0] - b[0]);
  const ends = new MinHeap();
  for (const [start, end] of sorted) {
    if (ends.size && ends.peek() <= start) ends.pop();
    ends.push(end);
  }
  return ends.size;
}

minMeetingRooms([
  [0, 30],
  [5, 10],
  [15, 20],
]); // 2
```

O(n log n). Another way is to sort starts and ends separately and sweep with two pointers, counting how many meetings are active at once. The same idea lays out overlapping events side by side in a calendar view.

## 349: What rate limiting algorithms do you know?

- **Fixed window:** count requests per time window (like per minute). Simple, but allows bursts at the window edges.
- **Sliding window log:** store timestamps and count those in the last N seconds. Accurate but uses more memory.
- **Sliding window counter:** mix of the two using weighted counts from the current and previous window.
- **Token bucket:** tokens refill at a fixed rate, each request uses one. Allows short bursts up to the bucket size.
- **Leaky bucket:** requests are processed at a constant rate, extra ones wait or are dropped.

```js
function tokenBucket(capacity, refillPerSec) {
  let tokens = capacity;
  let last = performance.now();
  return function tryTake() {
    const now = performance.now();
    tokens = Math.min(capacity, tokens + ((now - last) / 1000) * refillPerSec);
    last = now;
    if (tokens >= 1) {
      tokens--;
      return true;
    }
    return false;
  };
}
```

On the front end you use these to protect APIs from your own UI, like limiting analytics events or autosave calls.

## 350: Why add jitter to exponential backoff?

If many clients fail at the same moment (for example, the server restarts), plain exponential backoff makes them all retry at the same moments too: 1s, 2s, 4s. That creates waves of traffic that can knock the server over again. Jitter adds randomness so retries spread out. "Full jitter" picks a random delay between 0 and the backoff value:

```js
const delay = Math.random() * Math.min(maxDelay, base * 2 ** attempt);
```

Also cap the maximum delay and the number of attempts, and respect a `Retry-After` header if the server sends one.

## 351: How would you build a task scheduler that runs async tasks by priority with a concurrency limit?

Keep a priority queue of waiting tasks and a counter of running ones. Whenever a task finishes or a new one is added, start tasks from the top of the queue until the limit is reached.

```js
class Scheduler {
  #queue = new MinHeap(
    (a, b) =>
      a.priority < b.priority || (a.priority === b.priority && a.seq < b.seq),
  );
  #running = 0;
  #seq = 0;

  constructor(limit) {
    this.limit = limit;
  }

  add(task, priority = 0) {
    return new Promise((resolve, reject) => {
      this.#queue.push({ task, priority, seq: this.#seq++, resolve, reject });
      this.#next();
    });
  }

  #next() {
    while (this.#running < this.limit && this.#queue.size) {
      const { task, resolve, reject } = this.#queue.pop();
      this.#running++;
      Promise.resolve()
        .then(task)
        .then(resolve, reject)
        .finally(() => {
          this.#running--;
          this.#next();
        });
    }
  }
}
```

The `seq` tie-breaker keeps tasks with the same priority in FIFO order, since a heap is not stable. Image loaders and prefetchers use this kind of scheduler to load visible images first.

## 352: How do you avoid race conditions in a search-as-you-type feature?

Responses can come back out of order, so a slow response for "ap" can overwrite the result for "app". Fixes:

- cancel the previous request with `AbortController` when a new one starts
- or tag each request with an id and ignore responses that aren't for the latest id

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

Combine it with debounce to cut the number of requests and a small cache of recent queries so going back to an earlier query is instant.

## 353: How do bundlers detect circular dependencies, and why are they a problem?

A bundler builds a directed graph of modules from their imports and walks it with DFS. A module that is reached again while it's still "in progress" means there is a cycle. Cycles are allowed in ES modules, but they can cause bugs: one module may read an export from another that hasn't finished running yet, so it sees `undefined` or hits a "Cannot access before initialization" error. Tools like `madge` or ESLint's `import/no-cycle` rule find them. The usual fix is to move the shared code into a third module that both import.

## 354: Why can a heavy algorithm freeze the page, and how does the event loop relate to it?

JavaScript runs on the main thread, which also handles rendering and user input. A long synchronous loop (sorting a million rows, a big regex, deep recursion) blocks the event loop, so no clicks are handled and no frames are painted until it finishes. Any task over 50 ms is counted as a "long task" and hurts INP (Interaction to Next Paint). Options are making the algorithm faster, splitting the work into chunks, or moving it off the main thread to a Web Worker.

## 355: How do you split a long computation into chunks so the UI stays responsive?

Process a batch, then yield to the browser so it can handle input and paint, and continue:

```js
async function processInChunks(items, handle, budgetMs = 8) {
  let i = 0;
  while (i < items.length) {
    const start = performance.now();
    while (i < items.length && performance.now() - start < budgetMs) {
      handle(items[i++]);
    }
    await yieldToMain();
  }
}

function yieldToMain() {
  if (globalThis.scheduler?.yield) return scheduler.yield();
  return new Promise((resolve) => setTimeout(resolve, 0));
}
```

`scheduler.yield()` is available in Chromium-based browsers and is being added to others. It continues your task before other queued tasks. `setTimeout` is the fallback. Using a time budget instead of a fixed batch size adapts to slow and fast devices.

## 356: When should you move an algorithm to a Web Worker?

When it takes more than a few dozen milliseconds and doesn't need the DOM: parsing big files, sorting or filtering huge datasets, image processing, search indexing, diffing large texts, compression. The worker runs on its own thread, so the UI stays smooth.

```js
// main.js
const worker = new Worker(new URL("./sort-worker.js", import.meta.url), {
  type: "module",
});
worker.postMessage(bigArray);
worker.onmessage = (e) => render(e.data);

// sort-worker.js
self.onmessage = (e) => {
  self.postMessage(e.data.toSorted((a, b) => a - b));
};
```

The cost is copying data between threads (structured clone), so for small inputs the round trip can take longer than just doing the work.

## 357: How do you avoid the cost of copying large data to and from a worker?

- **Transferable objects:** pass an `ArrayBuffer` in the transfer list, and ownership moves to the worker without copying: `worker.postMessage(buf, [buf])`. The sender can no longer use it.
- **SharedArrayBuffer:** both threads see the same memory. Use `Atomics` to coordinate. It requires the page to be cross-origin isolated (COOP and COEP headers).
- Send only what the worker needs, like ids and sort keys, instead of whole objects.

Typed arrays plus transfer is the usual way to move millions of numbers cheaply.

## 358: Why are typed arrays faster for numeric algorithms?

A `Float64Array` or `Int32Array` stores raw numbers in one continuous buffer with a fixed type. The engine doesn't have to check types or deal with holes, the data fits better in CPU caches, and you can transfer it to workers or WebAssembly without conversion. Sorting a `Float64Array` with `sort()` compares numbers numerically by default (no comparator needed) and is usually much faster than sorting a normal array with a comparator. The downside is a fixed length and only numbers.

## 359: What are V8 "elements kinds" and how can they affect algorithm speed?

V8 tracks what kind of values an array holds, like `PACKED_SMI_ELEMENTS` (small integers, no holes), `PACKED_DOUBLE_ELEMENTS` and `PACKED_ELEMENTS` (any values), plus `HOLEY_` versions of each. Fast paths exist for the more specific kinds. The transitions only go one way: once an array gets a float, an object or a hole, it never goes back to the faster kind. So in hot loops, keep arrays of one type, avoid holes, and don't mix numbers with `undefined` or strings.

## 360: Why is new Array(n) sometimes slower than building an array with push?

`new Array(n)` creates an array with n holes, so V8 marks it as `HOLEY`. Every read has to check for holes and may look up the prototype chain. Filling it later doesn't make it "packed" again. For most code the difference is tiny, but in tight numeric loops it can show. Alternatives are `Array.from({ length: n }, () => 0)`, `new Array(n).fill(0)` (still holey in V8 but with no actual holes, so reads are fast enough), or a typed array when the values are numbers.

## 361: How do hidden classes and inline caches affect algorithm code?

V8 gives objects with the same properties added in the same order the same hidden class (also called a shape or map). Code that always sees one shape at a property access ("monomorphic") is fast because V8 caches where the property lives. If the same line sees many different shapes, it becomes "megamorphic" and slower. In algorithms that create many nodes (trees, graphs, heaps), create them with a class or a factory that always sets the same fields in the same order, and avoid adding or deleting properties later.

## 362: What are the pitfalls of benchmarking algorithms in JavaScript?

- The JIT needs time to warm up, so the first runs are slower.
- If you don't use the result, the engine may remove the work entirely (dead code elimination).
- Tiny inputs measure overhead, not the algorithm.
- `Date.now()` is too coarse. Use `performance.now()`.
- Garbage collection can pause in the middle of a run.
- Results differ between engines and devices.

Run many iterations, use realistic input sizes, keep the result (for example, sum it), compare medians, and use a tool like Tinybench or `mitata` instead of a hand-rolled loop. Most importantly, measure in the real app with the Performance panel.

## 363: How do you check the memory use of an algorithm in the browser?

Use Chrome DevTools: the Memory panel lets you take heap snapshots before and after and compare them, and the allocation timeline shows where objects are created. In Node.js, `process.memoryUsage().heapUsed` gives a quick number. `performance.measureUserAgentSpecificMemory()` is available in Chromium for cross-origin isolated pages. In interviews it's enough to reason about space complexity, but in real projects you should check for big temporary arrays, unbounded caches and closures that keep large data alive.

## 364: Map or object: which performs better for frequent inserts and deletes?

`Map` is designed for frequent additions and removals and stays fast. Objects are optimized for a fixed set of properties. Using `delete` on objects can push them into a slower "dictionary mode", and integer-like keys are stored differently from string keys. For algorithm work with dynamic keys (counters, caches, visited sets), `Map` and `Set` are usually faster and safer. For a small, fixed record, a plain object is fine and can be faster to read.

## 365: Is building a big string with an array and join faster than +=?

Not always. V8 represents `a + b` as a rope (a "cons string" pointing to both parts), so `+=` in a loop is fast, and the string gets flattened once when you read from it. `join` allocates the parts array plus the final string. For most cases they're close, and `+=` is often a bit faster. What does hurt is reading characters from the string in the same loop where you keep appending, because each read may force flattening. Write the clearest version, then measure if it's hot.

## 366: What is a trampoline and when would you use it?

A trampoline lets you write recursive code that doesn't grow the call stack. Instead of calling itself, the function returns a thunk (a function that does the next step), and a loop keeps calling thunks until it gets a real value:

```js
const trampoline =
  (fn) =>
  (...args) => {
    let result = fn(...args);
    while (typeof result === "function") result = result();
    return result;
  };

const sumTo = trampoline(function step(n, acc = 0) {
  return n === 0 ? acc : () => step(n - 1, acc + n);
});

sumTo(1_000_000); // 500000500000, no stack overflow
```

Since V8 doesn't do tail call optimization, this is one way to keep a recursive style for very deep processes. A plain loop is usually simpler and faster.

## 367: How do you traverse a very deep structure (like a huge JSON or a long linked chain) safely?

Use an explicit stack (or queue) instead of recursion, so the depth is limited by heap memory, not the call stack:

```js
function countLeaves(root) {
  let count = 0;
  const stack = [root];
  while (stack.length) {
    const value = stack.pop();
    if (value !== null && typeof value === "object") {
      for (const child of Object.values(value)) stack.push(child);
    } else {
      count++;
    }
  }
  return count;
}
```

If the data may contain cycles (object graphs, not JSON), add a `WeakSet` of visited objects. For postorder work, push a marker like `{ node, done: true }` to know when all children are finished.

## 368: How do you compare floating point numbers safely in algorithms?

Never use `===` on results of float math. Compare with a tolerance that fits the size of the numbers:

```js
function nearlyEqual(a, b, relTol = 1e-9, absTol = 1e-12) {
  return (
    Math.abs(a - b) <=
    Math.max(relTol * Math.max(Math.abs(a), Math.abs(b)), absTol)
  );
}

nearlyEqual(0.1 + 0.2, 0.3); // true
```

`Number.EPSILON` alone is only right for numbers near 1. For money, store integer cents (or use `BigInt`) instead of floats. In geometry, choose the tolerance based on the unit (for example, half a pixel). Summing many floats also builds up error, which `Math.sumPrecise` (a recent addition) or Kahan summation reduces.

## 369: How do you compute a^b mod m efficiently?

Use fast exponentiation by squaring, which needs O(log b) multiplications. In JavaScript, use `BigInt` so the products don't lose precision:

```js
function modPow(base, exp, mod) {
  base = BigInt(base) % BigInt(mod);
  exp = BigInt(exp);
  mod = BigInt(mod);
  let result = 1n;
  while (exp > 0n) {
    if (exp & 1n) result = (result * base) % mod;
    base = (base * base) % mod;
    exp >>= 1n;
  }
  return result;
}

modPow(2, 100, 1_000_000_007); // 976371285n
```

With normal numbers, `a * b` can go past 2⁵³ when the modulus is around 10⁹, so the result silently becomes wrong. That's a common bug when porting competitive programming code to JavaScript.

## 370: Why is Math.random not enough for some algorithms, and how do you get an unbiased random integer?

`Math.random()` is not cryptographically secure, so don't use it for tokens, IDs or anything security-related. Use `crypto.getRandomValues()` or `crypto.randomUUID()`. When turning random bytes into a range, `x % n` is biased unless n divides the range evenly. Rejection sampling fixes that:

```js
function secureRandomInt(n) {
  const max = Math.floor(0x1_0000_0000 / n) * n; // largest multiple of n below 2^32
  const buf = new Uint32Array(1);
  do {
    crypto.getRandomValues(buf);
  } while (buf[0] >= max);
  return buf[0] % n;
}
```

Values at or above `max` are thrown away, so every result from 0 to n − 1 is equally likely.

## 371: How do you get reproducible random numbers (a seeded PRNG)?

`Math.random()` can't be seeded. For tests, simulations, procedural content or replays, write a small seeded generator such as mulberry32:

```js
function mulberry32(seed) {
  return function () {
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const rand = mulberry32(42);
rand(); // same sequence every time for seed 42
```

`Math.imul` does 32-bit integer multiplication, which is needed because normal `*` on large numbers loses the low bits. Seeded generators like this are fast but not secure.

## 372: How would you test that a shuffle is unbiased?

Shuffle a small array (like `[1, 2, 3]`) many times, say 600,000, and count how often each of the 6 orders appears. Each should be close to 100,000. A chi-square test tells you whether the differences are bigger than random noise. The `sort(() => Math.random() - 0.5)` approach fails this test clearly, while Fisher-Yates passes. A common off-by-one bug in Fisher-Yates is picking `j` from the whole array (`Math.random() * n`) instead of `0..i`, which also produces a biased result.

## 373: How would you sort 1 million rows in the browser without freezing the page?

1. Move the sort to a Web Worker.
2. Don't send whole row objects. Send the sort key column as a typed array plus an index array, sort the indexes, and send the order back as a transferable `Uint32Array`.
3. For string keys, use one `Intl.Collator` and precompute collation-friendly keys if possible.
4. Render with virtualization so only visible rows exist in the DOM.
5. Cache sorted orders per column so toggling back is instant.

The sort itself is O(n log n). The bigger wins usually come from avoiding data copies and DOM work.

## 374: How do you implement natural sort ("file2" before "file10")?

The easy and correct way is `Intl.Collator` with `numeric: true`:

```js
const natural = new Intl.Collator(undefined, {
  numeric: true,
  sensitivity: "base",
});
["file10.txt", "file2.txt", "File1.txt"].sort(natural.compare);
// ["File1.txt", "file2.txt", "file10.txt"]
```

If you have to write it yourself, split each string into chunks of digits and non-digits (`/(\d+)/`), then compare chunk by chunk: numbers by value, text by `localeCompare`. Watch out for leading zeros, very long digit runs that go past safe integer range (compare by length, then as strings), and decimal points.

## 375: How do fuzzy finders like fzf or VS Code's quick open rank results?

They check that the query is a subsequence of the candidate, then score the match. Bonuses go to matches at the start of the string, after separators (`/`, `_`, `-`, `.`), at camelCase boundaries and on consecutive characters. Penalties go to gaps. Finding the best-scoring alignment is a small DP (similar to the Smith-Waterman algorithm), which is O(n × m) per candidate. To stay fast over thousands of files, they first filter with a cheap subsequence check and only score the survivors.

## 376: How would you build fast client-side full-text search?

Build an inverted index: a map from each word (token) to the list of documents that contain it.

```js
function buildIndex(docs) {
  const index = new Map();
  docs.forEach((doc, id) => {
    const words = new Set(doc.text.toLowerCase().match(/\p{L}+/gu) ?? []);
    for (const w of words) {
      if (!index.has(w)) index.set(w, []);
      index.get(w).push(id);
    }
  });
  return index;
}

function search(index, query) {
  const terms = query.toLowerCase().match(/\p{L}+/gu) ?? [];
  if (terms.length === 0) return [];
  const lists = terms.map((t) => new Set(index.get(t) ?? []));
  return [...lists.reduce((a, b) => a.intersection(b))];
}
```

Real search engines add stemming, stop words, prefix matching for search-as-you-type and ranking (TF-IDF or BM25). Libraries like MiniSearch, FlexSearch and Lunr do this in the browser. Build the index in a worker or at build time for large datasets.

## 377: How would you design a typeahead component from an algorithm point of view?

- **Input:** debounce keystrokes (150 to 300 ms) and ignore queries below a minimum length.
- **Requests:** cancel stale requests with `AbortController` or ignore out-of-order responses.
- **Caching:** an LRU cache of query → results. You can also filter the cached results of a shorter prefix locally while the new request is in flight.
- **Matching:** for local data, a sorted array with prefix binary search or a trie. For fuzzy matching, a scored subsequence match.
- **Ranking:** combine match quality with popularity or recency.
- **Rendering:** limit results, highlight matches safely, use keyboard navigation and virtualization for long lists.

Interviewers want to see you connect algorithms with real UI concerns.

## 378: How do you render a virtual list where rows have different heights?

Keep an array of measured (or estimated) heights and a prefix sum array of their top offsets. To find the first visible row for a scroll position, binary search the offsets:

```js
function firstVisible(offsets, scrollTop) {
  // offsets[i] = top position of row i, sorted ascending
  let lo = 0;
  let hi = offsets.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >>> 1;
    if (offsets[mid] <= scrollTop) lo = mid;
    else hi = mid - 1;
  }
  return lo;
}
```

Then add rows until their total height covers the viewport. When a row's real height is measured and differs from the estimate, update the offsets from that row onward (or use a Fenwick tree so updates are O(log n)). Libraries like TanStack Virtual do this for you.

## 379: How does a masonry layout algorithm work?

Masonry places items into columns. The simple greedy version puts each item into the column that is currently the shortest:

```js
function masonry(items, columnCount, gap) {
  const heights = new Array(columnCount).fill(0);
  return items.map((item) => {
    let col = 0;
    for (let c = 1; c < columnCount; c++) {
      if (heights[c] < heights[col]) col = c;
    }
    const top = heights[col];
    heights[col] += item.height + gap;
    return { ...item, col, top };
  });
}
```

It's O(n × columns), or O(n log columns) with a heap. It keeps the reading order mostly left to right and the column heights balanced. Native CSS masonry layout is still being worked on by browsers, so JavaScript layouts are still common.

## 380: How do you detect collisions between many objects efficiently?

Checking every pair is O(n²). Instead, put objects into a spatial structure and only compare objects that are close:

- **Uniform grid / spatial hash:** divide space into cells, put each object into the cells it touches, and only compare objects in the same cell. Great when objects are similar in size.
- **Quadtree:** split space recursively into four parts where objects are dense. Better when objects bunch together.
- **Sweep and prune:** sort by x, and only compare objects whose x ranges overlap.

The actual check for two axis-aligned boxes is simple:

```js
const overlaps = (a, b) =>
  a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
```

This matters for canvas games, drag-and-drop editors and charts with many points under the mouse.

## 381: How does a quadtree work?

A quadtree is a tree where each node covers a rectangle and splits into four children (NW, NE, SW, SE) when it holds more than a set number of points.

```js
class QuadTree {
  constructor(bounds, capacity = 4) {
    this.bounds = bounds; // { x, y, w, h }
    this.capacity = capacity;
    this.points = [];
    this.children = null;
  }

  contains(p, b = this.bounds) {
    return p.x >= b.x && p.x < b.x + b.w && p.y >= b.y && p.y < b.y + b.h;
  }

  insert(p) {
    if (!this.contains(p)) return false;
    if (!this.children && this.points.length < this.capacity) {
      this.points.push(p);
      return true;
    }
    if (!this.children) this.#split();
    return this.children.some((c) => c.insert(p));
  }

  #split() {
    const { x, y, w, h } = this.bounds;
    const hw = w / 2;
    const hh = h / 2;
    this.children = [
      new QuadTree({ x, y, w: hw, h: hh }, this.capacity),
      new QuadTree({ x: x + hw, y, w: hw, h: hh }, this.capacity),
      new QuadTree({ x, y: y + hh, w: hw, h: hh }, this.capacity),
      new QuadTree({ x: x + hw, y: y + hh, w: hw, h: hh }, this.capacity),
    ];
    for (const p of this.points) this.children.some((c) => c.insert(p));
    this.points = [];
  }

  query(range, found = []) {
    const b = this.bounds;
    const intersects =
      range.x < b.x + b.w &&
      range.x + range.w > b.x &&
      range.y < b.y + b.h &&
      range.y + range.h > b.y;
    if (!intersects) return found;
    for (const p of this.points) if (this.contains(p, range)) found.push(p);
    this.children?.forEach((c) => c.query(range, found));
    return found;
  }
}
```

Range queries skip whole regions that don't overlap, so they're roughly O(log n + k) for evenly spread points. Maps and scatter plots with thousands of points use this for hover and selection. A real version also needs a maximum depth so many identical points don't split forever.

## 382: How do you check if a point is inside a polygon?

Use ray casting: draw a horizontal ray from the point and count how many polygon edges it crosses. An odd count means inside.

```js
function pointInPolygon([px, py], polygon) {
  let inside = false;
  for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
    const [xi, yi] = polygon[i];
    const [xj, yj] = polygon[j];
    const crosses =
      yi > py !== yj > py && px < ((xj - xi) * (py - yi)) / (yj - yi) + xi;
    if (crosses) inside = !inside;
  }
  return inside;
}
```

O(n) for a polygon with n vertices. It's used for clicking on map regions or custom shapes on a canvas. Points exactly on an edge are an edge case you should mention.

## 383: How do you simplify a line with many points, for example for a chart or map?

The Ramer-Douglas-Peucker algorithm keeps the endpoints, finds the point farthest from the straight line between them, and if it's farther than a tolerance, keeps it and recurses on both halves. Otherwise it drops all points in between.

```js
function simplify(points, epsilon) {
  if (points.length < 3) return points;
  const [ax, ay] = points[0];
  const [bx, by] = points.at(-1);
  const len = Math.hypot(bx - ax, by - ay) || 1;
  let maxDist = 0;
  let index = 0;
  for (let i = 1; i < points.length - 1; i++) {
    const [px, py] = points[i];
    const d =
      Math.abs((by - ay) * px - (bx - ax) * py + bx * ay - by * ax) / len;
    if (d > maxDist) {
      maxDist = d;
      index = i;
    }
  }
  if (maxDist <= epsilon) return [points[0], points.at(-1)];
  const left = simplify(points.slice(0, index + 1), epsilon);
  const right = simplify(points.slice(index), epsilon);
  return [...left.slice(0, -1), ...right];
}
```

Average O(n log n), worst O(n²). Libraries like Simplify.js and many map libraries use it to draw long paths quickly.

## 384: How do you downsample a large time series for a chart without losing its shape?

Drawing 1,000,000 points on an 800-pixel-wide chart wastes time. Simple averaging per bucket hides spikes. Better options:

- **Min/max per pixel bucket:** keep the min and max of each bucket so peaks stay visible.
- **LTTB (Largest-Triangle-Three-Buckets):** split data into buckets and from each bucket pick the point that forms the largest triangle with the previously chosen point and the average of the next bucket. It keeps the visual shape very well.

Both are O(n). Charting libraries like ECharts offer LTTB as a built-in sampling option.

## 385: How do you find the data point nearest to the mouse on a line chart?

Convert the mouse x position to a data value (inverse of the x scale), then binary search the sorted x values and compare the two neighbors:

```js
function nearestIndex(xs, target) {
  let lo = 0;
  let hi = xs.length - 1;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (xs[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  if (lo > 0 && target - xs[lo - 1] < xs[lo] - target) return lo - 1;
  return lo;
}
```

O(log n) per mouse move instead of scanning all points. D3 has the same thing built in as `d3.bisector`. For scatter plots where x isn't sorted, use a quadtree or a k-d tree.

## 386: How do collaborative editors merge concurrent changes? Compare OT and CRDTs.

- **Operational Transformation (OT):** each edit is an operation like "insert 'a' at 5". When two users edit at the same time, a server transforms one operation against the other so both end in the same state. Google Docs uses OT. It needs a central server to order operations, and the transform functions are tricky to get right.
- **CRDTs (Conflict-free Replicated Data Types):** each character gets a unique, ordered id, so edits can be applied in any order on any peer and still converge. Yjs and Automerge are popular JavaScript CRDT libraries. They work offline and peer to peer, but use more memory for metadata.

For a new collaborative feature in JavaScript today, a CRDT library is usually the practical choice.

## 387: How do you compute a JSON diff and apply it as a patch?

Walk both objects together. For keys only in the old object, emit "remove". For keys only in the new one, emit "add". For keys in both, recurse into objects or emit "replace" if the values differ.

```js
function diff(a, b, path = "") {
  const ops = [];
  const isObj = (v) => v && typeof v === "object";
  for (const key of Object.keys(a)) {
    const p = `${path}/${key}`;
    if (!(key in b)) ops.push({ op: "remove", path: p });
    else if (isObj(a[key]) && isObj(b[key]))
      ops.push(...diff(a[key], b[key], p));
    else if (!Object.is(a[key], b[key]))
      ops.push({ op: "replace", path: p, value: b[key] });
  }
  for (const key of Object.keys(b)) {
    if (!(key in a))
      ops.push({ op: "add", path: `${path}/${key}`, value: b[key] });
  }
  return ops;
}
```

This uses the JSON Patch (RFC 6902) shape. A real version escapes `/` and `~` in keys and handles arrays smarter (with LCS) so inserting one item doesn't replace every item after it. Sending patches instead of full documents saves bandwidth for autosave and sync.

## 388: How do you deep clone an object that has circular references?

Keep a `WeakMap` from each original object to its copy. If you see an object again, return the existing copy:

```js
function deepClone(value, seen = new WeakMap()) {
  if (value === null || typeof value !== "object") return value;
  if (seen.has(value)) return seen.get(value);
  if (value instanceof Date) return new Date(value);
  if (value instanceof Map) {
    const m = new Map();
    seen.set(value, m);
    for (const [k, v] of value) m.set(deepClone(k, seen), deepClone(v, seen));
    return m;
  }
  if (value instanceof Set) {
    const s = new Set();
    seen.set(value, s);
    for (const v of value) s.add(deepClone(v, seen));
    return s;
  }
  const copy = Array.isArray(value)
    ? []
    : Object.create(Object.getPrototypeOf(value));
  seen.set(value, copy);
  for (const key of Reflect.ownKeys(value))
    copy[key] = deepClone(value[key], seen);
  return copy;
}
```

Register the copy in the map before recursing, or a cycle will loop forever. In real code, use `structuredClone` unless you need to keep prototypes or symbol keys.

## 389: How do you write a deep equal that handles cycles, NaN, Map and Set?

- Use `Object.is` for primitives so `NaN` equals `NaN` (decide whether `0` and `-0` should be equal).
- Check that both values have the same prototype or type tag.
- Compare `Date` by time, `RegExp` by source and flags.
- For `Map`, compare sizes and then each key's value. For `Set` of primitives, check each item with `has`. Sets of objects need a matching search, which is O(n²).
- Keep a `WeakMap` of pairs already being compared. If you meet the same pair again, assume equal for now, which handles cycles.

The hard parts are deciding the rules (are `{a: undefined}` and `{}` equal?) and the cost: it's O(total size) for most data, worse for sets of objects.

## 390: How do you serialize and deserialize a binary tree?

Use a preorder traversal and write a marker for empty children:

```js
function serialize(root) {
  const out = [];
  const walk = (node) => {
    if (!node) {
      out.push("#");
      return;
    }
    out.push(node.value);
    walk(node.left);
    walk(node.right);
  };
  walk(root);
  return out.join(",");
}

function deserialize(data) {
  const tokens = data.split(",");
  let i = 0;
  const build = () => {
    const t = tokens[i++];
    if (t === "#") return null;
    const node = new TreeNode(Number(t));
    node.left = build();
    node.right = build();
    return node;
  };
  return build();
}
```

The null markers make the structure unique, so you don't need a second traversal. O(n) both ways. A level-order format, like the one LeetCode uses, also works.

## 391: How do you find the lowest common ancestor of two nodes in any binary tree?

Recurse down. If the current node is one of the targets, return it. If both targets are found in different subtrees, the current node is the LCA:

```js
function lca(root, p, q) {
  if (!root || root === p || root === q) return root;
  const left = lca(root.left, p, q);
  const right = lca(root.right, p, q);
  if (left && right) return root;
  return left ?? right;
}
```

O(n). For DOM nodes, which have parent pointers, it's easier: collect the ancestors of one node into a `Set`, then walk up from the other until you hit one. The DOM also offers `a.contains(b)` and `compareDocumentPosition` for related checks.

## 392: How do you find the diameter of a binary tree?

The diameter is the longest path between any two nodes. For each node, the longest path through it is the left height plus the right height. Compute heights bottom-up and track the best:

```js
function diameter(root) {
  let best = 0;
  const height = (node) => {
    if (!node) return 0;
    const l = height(node.left);
    const r = height(node.right);
    best = Math.max(best, l + r);
    return 1 + Math.max(l, r);
  };
  height(root);
  return best; // number of edges
}
```

O(n). The pattern of "return one thing to the parent, but update a global answer with another" comes up in many tree problems.

## 393: How do you find the maximum path sum in a binary tree?

Similar to the diameter. Each node returns the best sum of a path going down from it in one direction, and the answer considers paths that bend at the node:

```js
function maxPathSum(root) {
  let best = -Infinity;
  const down = (node) => {
    if (!node) return 0;
    const l = Math.max(0, down(node.left)); // ignore negative branches
    const r = Math.max(0, down(node.right));
    best = Math.max(best, node.value + l + r);
    return node.value + Math.max(l, r);
  };
  down(root);
  return best;
}
```

`Math.max(0, ...)` lets the path skip a branch that would only lower the sum. Starting `best` at `-Infinity` handles trees with only negative values.

## 394: How do you build a tree from a flat list with parentId in O(n)?

A nested loop that finds children for each item is O(n²). Instead, index all items by id first, then attach each one to its parent:

```js
function buildTree(items) {
  const byId = new Map(
    items.map((item) => [item.id, { ...item, children: [] }]),
  );
  const roots = [];
  for (const node of byId.values()) {
    const parent = byId.get(node.parentId);
    if (parent) parent.children.push(node);
    else roots.push(node);
  }
  return roots;
}

buildTree([
  { id: 1, parentId: null },
  { id: 2, parentId: 1 },
  { id: 3, parentId: 1 },
  { id: 4, parentId: 2 },
]);
```

Two passes, O(n), and the order of items doesn't matter. This is very common for menus, comment threads, file trees and org charts that come from an API as flat rows. Ask what to do with orphans (parent not found) and cycles.

## 395: What is Morris traversal?

Morris traversal does an inorder traversal of a binary tree with O(1) extra space: no recursion and no stack. It temporarily points the rightmost node of each left subtree back to the current node (a "thread"), uses that link to return, and then removes it.

```js
function morrisInorder(root) {
  const out = [];
  let cur = root;
  while (cur) {
    if (!cur.left) {
      out.push(cur.value);
      cur = cur.right;
    } else {
      let pred = cur.left;
      while (pred.right && pred.right !== cur) pred = pred.right;
      if (!pred.right) {
        pred.right = cur; // create thread
        cur = cur.left;
      } else {
        pred.right = null; // remove thread
        out.push(cur.value);
        cur = cur.right;
      }
    }
  }
  return out;
}
```

Still O(n) time. It changes the tree during the walk, so it's not safe if other code reads the tree at the same time.

## 396: How can generators make tree traversal code cleaner?

A recursive generator with `yield*` lets callers iterate lazily and stop early:

```js
function* inorder(node) {
  if (!node) return;
  yield* inorder(node.left);
  yield node.value;
  yield* inorder(node.right);
}

for (const v of inorder(root)) {
  if (v > 100) break; // stops the traversal, no wasted work
  console.log(v);
}
```

The downside is speed and stack depth: each level of `yield*` adds a generator frame, so very deep trees can still overflow and it's slower than a plain loop. For balanced trees it's a nice, readable API.

## 397: How do you find the kth smallest value in a BST?

Do an inorder traversal and stop at the kth value:

```js
function kthSmallest(root, k) {
  const stack = [];
  let cur = root;
  while (cur || stack.length) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    cur = stack.pop();
    if (--k === 0) return cur.value;
    cur = cur.right;
  }
  return undefined;
}
```

O(h + k). If you need this often while the tree changes, store the size of each subtree in its node. Then you can go directly left or right in O(h), like an order-statistic tree.

## 398: How do you count the number of paths in a directed acyclic graph?

Process nodes in topological order. The number of paths to a node is the sum of paths to all nodes that point to it:

```js
function countPaths(graph, start, end) {
  const order = topoSort(graph);
  const ways = new Map([[start, 1]]);
  for (const node of order) {
    const w = ways.get(node) ?? 0;
    if (w === 0) continue;
    for (const next of graph.get(node) ?? []) {
      ways.set(next, (ways.get(next) ?? 0) + w);
    }
  }
  return ways.get(end) ?? 0;
}
```

O(V + E). This is DP on a DAG. Without the "acyclic" part, the number of paths could be infinite. Counts can grow very fast, so use `BigInt` if needed.

## 399: How do you find shortest paths in a DAG faster than Dijkstra?

In a DAG, process nodes in topological order and relax each node's outgoing edges once. By the time you reach a node, all paths into it have been considered.

```js
function dagShortest(graph, start) {
  const dist = new Map([[start, 0]]);
  for (const node of topoSort(graph)) {
    if (!dist.has(node)) continue;
    for (const [next, w] of graph.get(node) ?? []) {
      const nd = dist.get(node) + w;
      if (nd < (dist.get(next) ?? Infinity)) dist.set(next, nd);
    }
  }
  return dist;
}
```

O(V + E), and it works with negative weights. Negate the weights and you get the longest path, which is how the "critical path" of a build or project plan is found. (Here `topoSort` needs to read neighbors from `[neighbor, weight]` pairs.)

## 400: How do you find the cheapest route with at most k stops?

Dijkstra doesn't handle a limit on the number of edges directly. A clean solution is Bellman-Ford limited to k + 1 rounds, using a copy of the distances from the previous round:

```js
function cheapestWithStops(n, flights, src, dst, k) {
  let dist = new Array(n).fill(Infinity);
  dist[src] = 0;
  for (let round = 0; round <= k; round++) {
    const next = [...dist];
    for (const [u, v, price] of flights) {
      if (dist[u] + price < next[v]) next[v] = dist[u] + price;
    }
    dist = next;
  }
  return dist[dst] === Infinity ? -1 : dist[dst];
}
```

The copy makes sure each round only extends paths by one edge. O(k × E).

## 401: How do you compute Fibonacci in O(log n)?

Use matrix exponentiation. The matrix `[[1, 1], [1, 0]]` raised to the power n contains F(n). Square-and-multiply needs only O(log n) matrix multiplications:

```js
function fibFast(n) {
  const mul = (A, B) => [
    [
      A[0][0] * B[0][0] + A[0][1] * B[1][0],
      A[0][0] * B[0][1] + A[0][1] * B[1][1],
    ],
    [
      A[1][0] * B[0][0] + A[1][1] * B[1][0],
      A[1][0] * B[0][1] + A[1][1] * B[1][1],
    ],
  ];
  let result = [
    [1n, 0n],
    [0n, 1n],
  ];
  let base = [
    [1n, 1n],
    [1n, 0n],
  ];
  let e = BigInt(n);
  while (e > 0n) {
    if (e & 1n) result = mul(result, base);
    base = mul(base, base);
    e >>= 1n;
  }
  return result[0][1];
}

fibFast(100); // 354224848179261915075n
```

`BigInt` keeps large results exact. The same trick works for any linear recurrence, like "number of ways to tile a board".

## 402: Why not use Binet's formula for Fibonacci in JavaScript?

Binet's formula, F(n) = (φⁿ − ψⁿ) / √5, gives the answer in O(1) math operations. But it uses floating point, and the rounding error grows with n. In JavaScript it starts giving wrong answers somewhere around n = 70, before the result even passes `Number.MAX_SAFE_INTEGER`. It's a nice thing to mention, but for exact results use the loop, matrix exponentiation or fast doubling with `BigInt`.

## 403: What are Catalan numbers and where do they show up?

Catalan numbers (1, 1, 2, 5, 14, 42, ...) count many structures: valid parentheses strings with n pairs, distinct BSTs with n nodes, ways to triangulate a polygon, and paths in a grid that never cross the diagonal.

```js
function catalan(n) {
  const c = [1n];
  for (let i = 1; i <= n; i++) {
    c[i] = 0n;
    for (let j = 0; j < i; j++) c[i] += c[j] * c[i - 1 - j];
  }
  return c[n];
}

catalan(4); // 14n
```

Spotting that a counting problem gives 1, 2, 5, 14 for small inputs is often the fastest way to the formula.

## 404: How do you compute "n choose k" without overflow?

Multiply and divide step by step, which keeps every middle result an exact integer:

```js
function choose(n, k) {
  if (k < 0 || k > n) return 0n;
  k = Math.min(k, n - k);
  let result = 1n;
  for (let i = 1; i <= k; i++) {
    result = (result * BigInt(n - k + i)) / BigInt(i);
  }
  return result;
}

choose(52, 5); // 2598960n
```

After step i, `result` is C(n − k + i, i), so the division is always exact. Using factorials directly overflows quickly. If you need the result modulo a prime, use modular inverses (Fermat's little theorem with `modPow`).

## 405: How do you count inversions in an array?

An inversion is a pair `i < j` with `arr[i] > arr[j]`. It measures how unsorted an array is. Count them during merge sort: when you take an item from the right half, every remaining item in the left half forms an inversion with it.

```js
function countInversions(arr) {
  if (arr.length < 2) return { sorted: arr, count: 0 };
  const mid = arr.length >> 1;
  const L = countInversions(arr.slice(0, mid));
  const R = countInversions(arr.slice(mid));
  const sorted = [];
  let count = L.count + R.count;
  let i = 0;
  let j = 0;
  while (i < L.sorted.length && j < R.sorted.length) {
    if (L.sorted[i] <= R.sorted[j]) sorted.push(L.sorted[i++]);
    else {
      sorted.push(R.sorted[j++]);
      count += L.sorted.length - i;
    }
  }
  return {
    sorted: [...sorted, ...L.sorted.slice(i), ...R.sorted.slice(j)],
    count,
  };
}
```

O(n log n) instead of O(n²). It's used to compare rankings (how different are two orderings?).

## 406: How do you find the maximum product of a subarray?

Like Kadane's, but a negative number can turn the smallest product into the largest, so track both:

```js
function maxProduct(nums) {
  let max = nums[0];
  let min = nums[0];
  let best = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const x = nums[i];
    if (x < 0) [max, min] = [min, max];
    max = Math.max(x, max * x);
    min = Math.min(x, min * x);
    best = Math.max(best, max);
  }
  return best;
}

maxProduct([2, 3, -2, 4]); // 6
maxProduct([-2, 3, -4]); // 24
```

O(n) time, O(1) space. Zeros reset both values naturally, because `Math.max(x, ...)` restarts from `x`.

## 407: How do you find the minimum window substring that contains all characters of another string?

Use a sliding window with counts. Expand right until the window has everything, then shrink from the left as long as it still does:

```js
function minWindow(s, t) {
  const need = new Map();
  for (const ch of t) need.set(ch, (need.get(ch) ?? 0) + 1);
  let missing = t.length;
  let start = 0;
  let bestStart = 0;
  let bestLen = Infinity;
  for (let end = 0; end < s.length; end++) {
    const ch = s[end];
    if (need.has(ch)) {
      if (need.get(ch) > 0) missing--;
      need.set(ch, need.get(ch) - 1);
    }
    while (missing === 0) {
      if (end - start + 1 < bestLen) {
        bestLen = end - start + 1;
        bestStart = start;
      }
      const left = s[start++];
      if (need.has(left)) {
        need.set(left, need.get(left) + 1);
        if (need.get(left) > 0) missing++;
      }
    }
  }
  return bestLen === Infinity ? "" : s.slice(bestStart, bestStart + bestLen);
}

minWindow("ADOBECODEBANC", "ABC"); // "BANC"
```

Counts can go negative when the window has extras. The `missing` counter avoids comparing whole maps on every step. O(n + m).

## 408: How do you count subarrays with exactly K distinct values?

Counting "exactly K" with a sliding window is awkward, but "at most K" is easy. Then exactly(K) = atMost(K) − atMost(K − 1):

```js
function atMostK(nums, k) {
  const counts = new Map();
  let start = 0;
  let total = 0;
  for (let end = 0; end < nums.length; end++) {
    counts.set(nums[end], (counts.get(nums[end]) ?? 0) + 1);
    while (counts.size > k) {
      const x = nums[start++];
      counts.set(x, counts.get(x) - 1);
      if (counts.get(x) === 0) counts.delete(x);
    }
    total += end - start + 1; // subarrays ending at `end`
  }
  return total;
}

const exactlyK = (nums, k) => atMostK(nums, k) - atMostK(nums, k - 1);

exactlyK([1, 2, 1, 2, 3], 2); // 7
```

O(n). The "at most" trick is worth remembering for any "exactly" counting problem.

## 409: What is a difference array?

A difference array lets you add a value to a whole range in O(1). You add at the start and subtract right after the end, then a prefix sum gives the final values:

```js
function applyRangeAdds(n, updates) {
  const diff = new Array(n + 1).fill(0);
  for (const [l, r, value] of updates) {
    diff[l] += value;
    diff[r + 1] -= value;
  }
  const result = [];
  let running = 0;
  for (let i = 0; i < n; i++) {
    running += diff[i];
    result.push(running);
  }
  return result;
}

applyRangeAdds(5, [
  [1, 3, 2],
  [2, 4, 3],
]); // [0, 2, 5, 5, 3]
```

O(n + number of updates). It's the trick behind "car pooling", "how many bookings overlap each day" and counting how many events are active at each minute in a calendar.

## 410: How do 2D prefix sums work?

Store the sum of the rectangle from `(0, 0)` to each cell. Any rectangle sum is then four lookups:

```js
function build2D(grid) {
  const R = grid.length;
  const C = grid[0].length;
  const P = Array.from({ length: R + 1 }, () => new Array(C + 1).fill(0));
  for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
      P[r + 1][c + 1] = grid[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c];
    }
  }
  return (r1, c1, r2, c2) =>
    P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1];
}
```

Building is O(R × C), each query is O(1). Image processing uses the same idea (an "integral image") for fast box blurs and face detection.

## 411: How do you find the prime factors of a number?

Divide by 2 while you can, then by odd numbers up to √n. Whatever is left above 1 is a prime factor:

```js
function primeFactors(n) {
  const factors = [];
  while (n % 2 === 0) {
    factors.push(2);
    n /= 2;
  }
  for (let d = 3; d * d <= n; d += 2) {
    while (n % d === 0) {
      factors.push(d);
      n /= d;
    }
  }
  if (n > 1) factors.push(n);
  return factors;
}

primeFactors(360); // [2, 2, 2, 3, 3, 5]
```

O(√n). For factoring many numbers up to a limit, precompute the smallest prime factor of each number with a sieve, then each factorization is O(log n).

## 412: Explain amortized analysis using a dynamic array that doubles in size.

When a dynamic array is full, it allocates a new block twice as big and copies everything. That copy is O(n), but it only happens after n cheap pushes. Total copying over n pushes is 1 + 2 + 4 + ... + n, which is less than 2n. So n pushes cost O(n) in total, which is O(1) amortized per push. If the array grew by a fixed amount (say +10) instead of doubling, total copying would be O(n²). That's why growth by a factor is used everywhere, including JavaScript engines.

## 413: What are the costs of common JavaScript built-ins that people often get wrong?

- `arr.unshift(x)` / `arr.shift()`: O(n), not O(1).
- `arr.splice(i, 1)` in the middle: O(n).
- `arr.includes`, `indexOf`, `find`: O(n).
- `[...arr]`, `slice()`, `concat`, `Object.assign({}, obj)`, `{...obj}`: O(n), they copy.
- `str.slice`, `substring`: can be O(1) in V8 (sliced strings) but you shouldn't count on it.
- `JSON.stringify` / `JSON.parse`: O(size of the data).
- `arr.sort`: O(n log n).
- `Object.keys(obj).length`: O(k), it builds an array. `map.size` is O(1).
- `new Set(arr)`: O(n), so building it inside a loop is O(n²).

## 414: What are common hidden O(n²) patterns in JavaScript code?

```js
// 1. spreading the accumulator in reduce
const byId = items.reduce((acc, x) => ({ ...acc, [x.id]: x }), {}); // O(n²)

// 2. includes/find inside a loop or filter
const common = a.filter((x) => b.includes(x)); // O(n × m)

// 3. removing from the front in a loop
while (queue.length) process(queue.shift()); // O(n²)

// 4. concat inside a loop
let all = [];
for (const page of pages) all = all.concat(page); // copies every time
```

Fixes: mutate the accumulator or use `Object.fromEntries`/`Map`, build a `Set` first, use a head index, and use `push(...page)` or `flat()`. These patterns are invisible with 100 items and painful with 50,000.

## 415: Why is spreading in a reduce accumulator O(n²), and how do you fix it?

`{ ...acc, [key]: value }` creates a new object and copies every existing key on every step. Step 1 copies 0 keys, step 2 copies 1, ..., step n copies n − 1: about n²/2 copies in total. With 10,000 items that's 50 million property copies and a lot of garbage.

```js
// O(n): mutate the accumulator you own
const byId = items.reduce((acc, x) => {
  acc[x.id] = x;
  return acc;
}, {});

// or
const byId2 = Object.fromEntries(items.map((x) => [x.id, x]));
const byId3 = new Map(items.map((x) => [x.id, x]));
```

Mutating the accumulator is fine because it's a new object created by this `reduce` call. No one else has a reference to it.

## 416: How can you guess the expected complexity from the input limits?

A rough rule: JavaScript can do about 10⁷ to 10⁸ simple operations per second. So:

| n up to      | expected complexity |
| ------------ | ------------------- |
| 10–12        | O(n!)               |
| 20–25        | O(2ⁿ)               |
| 100–500      | O(n³)               |
| 1,000–10,000 | O(n²)               |
| 10⁵–10⁶      | O(n log n) or O(n)  |
| 10⁹ and more | O(log n) or O(1)    |

If the problem says n ≤ 10⁵, an O(n²) solution will be too slow, so look for sorting, hashing, two pointers or a heap. In a front-end context, also remember the budget is 16 ms per frame, not one second.

## 417: How do you approach a problem you've never seen before in an interview?

1. Clarify the input, output, limits and edge cases.
2. Solve a small example by hand and watch what you actually do.
3. Write the brute-force idea and its complexity.
4. Look for the bottleneck: repeated lookups (use a hash map), repeated work on overlapping parts (DP or prefix sums), sorted data (binary search or two pointers), "top k" (heap), "connected" (graph traversal).
5. Check if a known pattern fits: sliding window, monotonic stack, backtracking, union-find.
6. Code it, then test with normal and edge cases.

Saying your thinking out loud is what lets the interviewer help you when you get stuck.

## 418: What is property-based testing and how does it help with algorithms?

Instead of writing specific examples, you describe properties that should always hold and let a library generate hundreds of random inputs. If one fails, it shrinks it to the smallest failing case. With fast-check:

```js
import fc from "fast-check";

fc.assert(
  fc.property(fc.array(fc.integer()), (arr) => {
    const sorted = mySort([...arr]);
    const expected = [...arr].sort((a, b) => a - b);
    return JSON.stringify(sorted) === JSON.stringify(expected);
  }),
);
```

Good properties for algorithms: "same result as a slow but obviously correct version", "output is sorted and has the same items", "encode then decode gives back the input". It finds edge cases you didn't think of, like empty arrays and duplicates.

## 419: What are common space-time trade-offs in algorithms?

- Hash maps and sets: extra memory for O(1) lookups (Two Sum).
- Memoization and DP tables: memory to avoid repeated work.
- Prefix sums: O(n) memory for O(1) range queries.
- Precomputed indexes (inverted index, trie): memory and build time for fast search.
- Caches (LRU): memory for fewer network calls.
- The other direction: in-place algorithms and streaming (reservoir sampling, Bloom filters) save memory but may be slower or less exact.

On mobile devices with little memory, the "save memory" side matters more than on servers.

## 420: How do you add a time limit (TTL) to a memoized function?

Store the time each entry was created and treat old entries as missing:

```js
function memoizeWithTTL(fn, ttlMs, maxSize = 500) {
  const cache = new Map();
  return (key) => {
    const hit = cache.get(key);
    if (hit && Date.now() - hit.time < ttlMs) return hit.value;
    const value = fn(key);
    cache.delete(key);
    cache.set(key, { value, time: Date.now() });
    if (cache.size > maxSize) cache.delete(cache.keys().next().value);
    return value;
  };
}
```

The size limit drops the oldest entry, so it's also a simple LRU-by-write. If `fn` returns a promise, also remove the entry when the promise rejects, so failures aren't cached.

## 421: What is the algorithmic cost of immutable updates, and what is structural sharing?

Copying a whole array or object on every change is O(n) per update, so n updates in a row cost O(n²). Structural sharing avoids that: when you change one part of a nested structure, you copy only the path from the root to the changed item and reuse everything else. Updating `state.users[5].name` copies the root, the `users` array and user 5, but not the other users. That's what Immer and well-written reducers do. Reference equality checks (`prev === next`) then tell you exactly which parts changed.

## 422: How do persistent data structures like those in Immutable.js work?

They use trees with a high branching factor, usually 32. Immutable.js `List` is a vector trie and `Map` is a hash array mapped trie (HAMT). An update copies only the nodes on the path from the root to the changed leaf, about log₃₂(n) nodes, which is at most 7 for a billion items. So updates are "effectively O(1)" and every old version stays valid and shares most of its memory with the new one. The cost is slower reads than a plain array and conversion overhead between plain JS and these structures.

## 423: You need to remove duplicates from 10 million items in the browser. How do you approach it?

- If the items are numbers, use a typed array and sort it, then remove neighbors that are equal. O(n log n) and very compact memory.
- If they're strings or ids, a `Set` is O(n) but 10 million entries can use hundreds of MB. Check if that fits on the target devices.
- If memory is tight and a tiny error rate is OK, use a Bloom filter to skip known items.
- Process in chunks or in a Web Worker so the page stays responsive.
- Better still, ask if the work can be done on the server or streamed so you never hold everything at once.

The interviewer wants trade-offs, not one "right" answer.

## 424: How would you find the top 10 most common errors from a huge stream of log events?

Exact: keep a `Map` of error key to count, and at the end (or periodically) use a min-heap of size 10 to pick the top. That is O(n log 10) time but memory grows with the number of distinct errors.

Approximate: if there are millions of distinct keys, use a Count-Min Sketch for counts plus a small heap of candidates, or the Space-Saving algorithm, which tracks only k counters and gives good "heavy hitter" results with fixed memory. Error tracking tools first normalize messages (strip ids and numbers) to group similar errors, which reduces the number of keys a lot.

## 425: What is a Count-Min Sketch?

A Count-Min Sketch estimates how many times each item appeared in a stream, using fixed memory. It's a small 2D array of counters with d rows, each with its own hash function. To add an item, increment one counter per row. To estimate a count, take the minimum of its d counters. Collisions can only make counts too high, never too low, and the minimum limits the error. It's used for frequency tracking, rate limiting and finding heavy hitters when storing every key isn't possible.

## 426: What is HyperLogLog?

HyperLogLog estimates the number of distinct items (cardinality) in a stream using a few kilobytes of memory, even for billions of items. It hashes each item and looks at the number of leading zeros in the hash. Seeing a long run of zeros suggests many distinct items have been seen. It splits items into many buckets and averages the estimates to reduce error to around 1 to 2 percent. Analytics tools use it to count unique visitors. Redis has it built in as `PFADD` / `PFCOUNT`.

## 427: How would you build offline autocomplete over 100,000 city names?

1. At build time, normalize names (lowercase, remove accents with `normalize("NFD")` and stripping combining marks) and sort them.
2. Ship the list as a compact file and load it lazily or in a worker.
3. For prefix search, binary search for the first match and read forward up to the limit. That's O(log n + k).
4. For matches in the middle of names or typos, add a small inverted index of word starts, or use fuzzy scoring on the prefix-filtered candidates.
5. Rank by population or user history, debounce input and cache recent queries.

A sorted array is likely smaller and faster to load than a trie of 100,000 words in JavaScript objects.

## 428: How do you detect circular references between spreadsheet cells and choose the recalculation order?

Treat cells as nodes and "A1 uses B2" as an edge from B2 to A1. When a formula changes, run cycle detection with DFS from that cell. If you find a cycle, show a `#REF!`-style error. When a value changes, collect all cells that depend on it (DFS or BFS forward), then topologically sort only that affected part and recalculate in that order. That way each cell is computed once, after all its inputs. Recomputing every cell on every change works for small sheets but doesn't scale.

## 429: How do signals (in Angular, Solid, Preact or Vue) decide what to recompute?

They build a dependency graph at runtime. When a computed value or effect runs, every signal it reads records it as a dependent. When a signal changes, it doesn't recompute everything right away. It marks dependents as "dirty" or "maybe dirty" (push). When something reads a computed value, it checks if any of its sources actually changed and recomputes only if needed (pull). This push-pull approach avoids "glitches" (seeing a half-updated state) and skips work when a value ends up unchanged. It's a graph traversal plus lazy evaluation, much like the spreadsheet example.

## 430: How does React's scheduler keep the UI responsive while rendering a big tree?

React's Fiber architecture turns rendering into a loop over units of work (one fiber per component) instead of one deep recursive call. In concurrent rendering, React works in short time slices (around 5 ms) and checks if it should yield to the browser, so input events and painting can happen in between. Updates have priorities (lanes): a click is urgent, a `startTransition` update can be interrupted and restarted. The algorithm is basically an interruptible tree traversal with a priority queue of pending work.

## 431: What garbage collection algorithms does V8 use, and why should algorithm code care?

V8 uses a generational collector. New objects go into a small "young generation" that is cleaned often with a fast copying collector (scavenger), because most objects die young. Objects that survive are moved to the "old generation", which is cleaned with mark-sweep-compact, mostly in parallel and concurrently with your code. Algorithms that create many short-lived objects (temporary arrays in each loop step, `[a, b]` pairs, spread copies) put pressure on the young generation and cause frequent small pauses. Reusing buffers and avoiding temporary allocations in hot loops can noticeably smooth out frame times.

## 432: How are JavaScript Map and Set implemented, and why do they keep insertion order?

The spec requires iteration in insertion order and sublinear average access time, but doesn't fix the implementation. V8 uses deterministic hash tables (based on Tyler Close's design): entries are stored in an array in insertion order, and a separate hash table of buckets points into that array. Lookups go through the buckets, iteration walks the entries array. Deleted entries leave holes that are cleaned up when the table is rebuilt. That's why iteration order is predictable and why `Map` makes a good LRU base.

## 433: In what order are object keys returned, and why does it matter for algorithms?

`Object.keys`, `for...in` and `JSON.stringify` return keys in this order: integer-like keys (such as `"1"`, `"42"`) in ascending numeric order first, then string keys in insertion order, then symbols (only for `Reflect.ownKeys`). So `{ b: 1, 2: 1, a: 1, 1: 1 }` lists `1, 2, b, a`. If your algorithm relies on insertion order with numeric-looking keys (like ids), a plain object will reorder them. Use a `Map` instead.

## 434: Why can some regexes be slow, and are there engines that avoid backtracking?

JavaScript's default regex engine (Irregexp in V8) is a backtracking engine. It supports features like backreferences and lookbehind, but some patterns can take exponential time on bad input. Engines like RE2 and Rust's regex use automata to guarantee linear time but drop some features. V8 has an experimental linear-time engine behind a flag, and you can use RE2 through a library in Node.js. In browser code, the practical defense is writing safe patterns and limiting input length.

## 435: How do you make string algorithms work correctly with emoji and accented letters?

- Iterate by code points (`for...of`, spread) instead of indexes, so surrogate pairs aren't split.
- For "characters" as users see them (including combined emoji and flags), use `Intl.Segmenter`:

```js
const seg = new Intl.Segmenter("en", { granularity: "grapheme" });
const graphemes = [...seg.segment("👨‍👩‍👧é")].map((s) => s.segment);
graphemes.length; // 2
```

- Reversing, truncating and counting length should use graphemes when the result is shown to users, or you'll cut characters in half.

`"👨‍👩‍👧".length` is 8, because it's several code points joined with zero-width joiners.

## 436: Why do you need Unicode normalization when comparing strings?

The same visible text can have different code points. "é" can be one code point (U+00E9) or "e" plus a combining accent (U+0065 U+0301). They look the same but `===` says they're different, and their `length` differs.

```js
const a = "café";
const b = "café";
a === b; // false
a.normalize("NFC") === b.normalize("NFC"); // true
```

Normalize input before using strings as keys in a `Map`, deduplicating, searching or comparing. For accent-insensitive search, normalize to NFD and strip combining marks with `/\p{M}/gu`, or use `Intl.Collator` with `sensitivity: "base"`.

## 437: Walk through optimizing a slow function from O(n²) to O(n).

Say you need to attach each order's customer:

```js
// O(n × m): find inside map
const result = orders.map((o) => ({
  ...o,
  customer: customers.find((c) => c.id === o.customerId),
}));
```

Steps: notice the repeated linear search, build an index once, then look up in O(1):

```js
const byId = new Map(customers.map((c) => [c.id, c]));
const result2 = orders.map((o) => ({ ...o, customer: byId.get(o.customerId) }));
```

Now it's O(n + m). The general recipe: find the inner loop, ask what question it answers, and precompute the answers in a hash map, a sorted array or a prefix sum.

## 438: What do you say when an interviewer asks "can you do better?"

First check what "better" means: time, memory, simpler code, or handling bigger input. Then think about the lower bound. You can't beat O(n) if you have to look at every item, and comparison sorting can't beat O(n log n). If you're already at the bound, say so and explain why. If not, look for repeated work you can cache, structure you're not using (sorted input, small value range), or a better data structure. It's also fine to say the current solution is good enough for the stated limits and that the faster version would be harder to maintain.

## 439: How do you design an algorithm to detect when a user has been idle?

Track the time of the last activity (`pointermove`, `keydown`, `scroll`, `visibilitychange`). Updating a single timestamp on every event is O(1) and cheap, unlike resetting a `setTimeout` on every mouse move. Then check with one interval or timer whether `Date.now() - lastActivity > limit`. Use passive listeners, throttle the handlers if they do more than set a number, and sync between tabs with `BroadcastChannel` or `localStorage` events so one active tab keeps the session alive. The browser's Idle Detection API exists in Chromium but needs permission and is not widely available.

## 440: How would you implement "infinite scroll" without the list getting slower over time?

- Load pages with cursor-based pagination (not offsets) so inserts on the server don't create duplicates or gaps.
- Deduplicate incoming items by id with a `Set`.
- Use `IntersectionObserver` on a sentinel element instead of listening to every scroll event.
- Virtualize the list so DOM size stays constant no matter how many items are loaded.
- Cap the number of items kept in memory and drop ones far above the viewport if the list can be huge.
- Avoid in-flight duplicate requests with a loading flag.

The algorithm parts are dedupe (hash set), windowing (prefix sums or fixed heights) and keeping the cursor.

## 441: How does a browser engine match CSS selectors efficiently?

Browsers match selectors right to left. For `.menu li a`, they first find candidate `a` elements, then walk up the ancestors to check for `li` and `.menu`. Most elements fail on the rightmost part, so the expensive ancestor walk happens rarely. Rules are also bucketed by their rightmost id, class or tag in hash maps, so for each element the engine only checks rules that could possibly match. Bloom filters of ancestor ids and classes let the engine quickly skip descendant selectors that can't match. That's why very general rightmost selectors like `*` or `[data-x]` can cost more than they look.

## 442: How would you implement a simple "diff" for two lines of text to show changes word by word?

Split both lines into words, compute the LCS table of the word arrays, then walk back through it to label each word as kept, removed or added:

```js
function wordDiff(a, b) {
  const x = a.split(/\s+/);
  const y = b.split(/\s+/);
  const dp = Array.from({ length: x.length + 1 }, () =>
    new Array(y.length + 1).fill(0),
  );
  for (let i = x.length - 1; i >= 0; i--) {
    for (let j = y.length - 1; j >= 0; j--) {
      dp[i][j] =
        x[i] === y[j]
          ? dp[i + 1][j + 1] + 1
          : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const out = [];
  let i = 0;
  let j = 0;
  while (i < x.length && j < y.length) {
    if (x[i] === y[j]) {
      out.push({ type: "same", word: x[i] });
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1])
      out.push({ type: "removed", word: x[i++] });
    else out.push({ type: "added", word: y[j++] });
  }
  while (i < x.length) out.push({ type: "removed", word: x[i++] });
  while (j < y.length) out.push({ type: "added", word: y[j++] });
  return out;
}
```

Filling the table from the end lets you walk forward and output the diff in order without reversing. O(n × m), fine for sentences and paragraphs. For whole documents, use Myers' algorithm via a library.

## 443: How do you merge many overlapping time ranges coming from different sources efficiently?

If each source is already sorted, don't concatenate and sort. Use a k-way merge with a min-heap by start time (O(N log k)), and merge intervals on the fly as they come out of the heap, extending the last range when it overlaps. This keeps memory low and works on streams, like merging availability from several calendars to find free slots. To find free time, walk the merged busy ranges and output the gaps between them.

## 444: How do you pick a random item with weighted probabilities?

Build a prefix sum of the weights, pick a random number in `[0, total)`, and binary search for where it falls:

```js
function weightedPicker(items, weights) {
  const prefix = [];
  let total = 0;
  for (const w of weights) prefix.push((total += w));
  return () => {
    const r = Math.random() * total;
    let lo = 0;
    let hi = prefix.length - 1;
    while (lo < hi) {
      const mid = (lo + hi) >>> 1;
      if (prefix[mid] > r) hi = mid;
      else lo = mid + 1;
    }
    return items[lo];
  };
}

const pick = weightedPicker(["common", "rare", "epic"], [80, 15, 5]);
```

Setup is O(n), each pick is O(log n). If you need millions of picks, the alias method gives O(1) per pick after O(n) setup. This is used for A/B test splits, loot tables and sampling.

## 445: How do you implement consistent hashing, and when would front-end developers meet it?

Consistent hashing places servers (and many "virtual nodes" for each) on a ring of hash values. A key goes to the first server clockwise from its hash. When a server is added or removed, only the keys near it move, instead of almost all keys like with `hash % n`.

```js
// sorted ring of [hash, server]; find the first hash >= key's hash
function pickServer(ring, keyHash) {
  let lo = 0;
  let hi = ring.length;
  while (lo < hi) {
    const mid = (lo + hi) >>> 1;
    if (ring[mid][0] < keyHash) lo = mid + 1;
    else hi = mid;
  }
  return ring[lo % ring.length][1]; // wrap around
}
```

Front-end developers meet it in CDNs and caches behind their apps, in sharded WebSocket servers, and in client-side load balancing between edge regions.

## 446: How would you detect that two large files are the same (or find changed chunks) in the browser?

Hash them with `crypto.subtle.digest("SHA-256", buffer)` and compare hashes. For large files, read with `file.stream()` and hash in chunks (with a library, since `subtle.digest` doesn't support streaming). To find which parts changed, split the file into chunks and hash each one. Fixed-size chunks break when bytes are inserted near the start, so tools like rsync and many backup systems use content-defined chunking: a rolling hash decides where chunks end, so an insert only changes nearby chunks. Upload tools use this to send only changed chunks.

## 447: What is the difference between a stable algorithm and a deterministic one, and why do both matter in UIs?

A stable sort keeps equal items in their original order. A deterministic algorithm gives the same output for the same input every time. In UIs both matter: if sorting or layout isn't stable and deterministic, rows jump around on every re-render, React keys get matched differently, snapshot tests fail randomly, and server-rendered HTML doesn't match the client (hydration errors). Avoid `Math.random()`, `Date.now()` and iteration over unordered data in render paths, and add a tie-breaker (like id) to comparators.

## 448: How would you implement a scheduler that runs callbacks at the right time when you have thousands of timers?

Calling `setTimeout` thousands of times works but is hard to manage and cancel in bulk. Instead, keep a min-heap of `{ time, callback }` ordered by time, and set one real timer for the earliest one. When it fires, run every task whose time has passed, then reset the timer for the new earliest. Adding is O(log n) and cancelling can be done lazily with a "cancelled" flag. Game loops, animation libraries and the Node.js timer implementation use similar ideas (Node groups timers with the same duration into lists).

## 449: What should you consider before using a clever algorithm in production front-end code?

- **Input size:** for 100 items, simple code is fast enough and easier to read.
- **Maintainability:** will the next developer understand a Fenwick tree in a component?
- **Bundle size:** a library for a fancy data structure adds kilobytes for every user.
- **Correctness:** clever code has more edge cases. Add tests, ideally property-based.
- **Measure first:** profile with the Performance panel and confirm the algorithm is actually the bottleneck. Often the real cost is DOM work, layout or network.
- **Platform help:** sometimes the fix is a Web Worker, virtualization or doing the work on the server.

Use the advanced algorithm when the numbers say you need it, and write a comment explaining why.

## 450: What is the most important thing to show in an algorithms interview?

Clear thinking matters more than memorized solutions. Interviewers want to see that you clarify the problem, start with something that works, reason about complexity honestly, improve step by step, write readable code and test it, including edge cases. Explaining trade-offs ("this uses O(n) memory, but if memory is tight we could sort instead") shows you would make good decisions on real projects. If you get stuck, say what you're trying and why. A good discussion with a partly finished solution often scores better than a silent, perfect one.
