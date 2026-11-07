# Jest Interview Questions and Answers

_Last updated: October 29, 2026_

450 Jest interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Jest 30 (the current major version). Things that changed in Jest 30, like the removed matcher aliases, `--testPathPatterns`, `defineConfig` and the `using` support for spies, are pointed out where they matter. Older patterns are mentioned when you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

# Easy Questions (1-150)

## 1: What is Jest?

Jest is a JavaScript testing framework. It was created at Facebook (now Meta) and is now maintained under the OpenJS Foundation. It works with plain JavaScript, TypeScript, Node.js code and front-end code like React.

It comes with most things you need in one package:

- A test runner that finds and runs your test files
- An assertion library (`expect` and its matchers)
- Mock functions and module mocking
- Fake timers
- Snapshot testing
- Code coverage

## 2: Why do teams choose Jest?

Mostly because it works with very little setup. You install one package, write a `*.test.js` file and run `npx jest`. There is no need to pick a separate runner, assertion library and mocking library like you would with Mocha, Chai and Sinon.

Other reasons:

- It runs test files in parallel in separate workers, so big suites are faster.
- Each test file runs in its own sandbox, so files don't leak state into each other.
- Watch mode only reruns tests related to changed files.
- It has a large community, and many tools (React Testing Library, Next.js, NestJS) have ready-made Jest setups.

## 3: How do you install Jest in a project?

Install it as a dev dependency and add a test script:

```bash
npm install --save-dev jest
```

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

Now `npm test` runs all your tests. If you need a browser-like environment (for DOM code), also install `jest-environment-jsdom`, because it is not bundled with Jest anymore.

## 4: How do you write and run your first test?

Create a function and a test file next to it:

```js
// sum.js
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```

```js
// sum.test.js
const sum = require("./sum");

test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});
```

Run `npx jest` or `npm test`. Jest finds `sum.test.js`, runs it and prints a pass or fail summary.

## 5: How does Jest find test files?

By default Jest uses the `testMatch` option, which looks for:

- Files inside any `__tests__` folder
- Files ending with `.test.js` or `.spec.js` (and the same for `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs`, `.mts`, `.cts`)

It skips `node_modules` by default. You can change this with `testMatch` (glob patterns) or `testRegex` (a regular expression), but not both at once.

## 6: What is the difference between test and it?

There is no difference. `it` is an alias of `test`. Some people use `it` because it reads like a sentence:

```js
it("returns an empty array when there is no data", () => {
  expect(getItems()).toEqual([]);
});

test("returns an empty array when there is no data", () => {
  expect(getItems()).toEqual([]);
});
```

Pick one style and use it across the project.

## 7: What does describe do?

`describe` groups related tests together. It makes the output easier to read and lets you share setup hooks (`beforeEach`, `afterEach`) for just that group. You can nest `describe` blocks.

```js
describe("Cart", () => {
  describe("addItem", () => {
    test("adds a new item", () => {});
    test("increases quantity for an existing item", () => {});
  });
});
```

## 8: What is expect in Jest?

`expect` is the function you use to check values. You pass it the value you got, and then call a matcher on the result to say what you expected:

```js
expect(user.name).toBe("Anna");
```

If the check fails, the matcher throws an error and Jest marks the test as failed, showing what was expected and what was received.

## 9: What is a matcher?

A matcher is a method on the object returned by `expect` that does the actual check. `toBe`, `toEqual`, `toContain`, `toThrow` and `toHaveBeenCalledWith` are all matchers.

Jest has many built-in matchers, and you can add your own with `expect.extend`. There are also libraries with extra matchers, like `@testing-library/jest-dom` and `jest-extended`.

## 10: What is the difference between toBe and toEqual?

`toBe` uses `Object.is`, so it checks if two values are exactly the same. For objects and arrays that means the same reference.

`toEqual` checks the values recursively, so two different objects with the same content are equal.

```js
test("toBe vs toEqual", () => {
  const a = { id: 1 };
  const b = { id: 1 };

  expect(a).toBe(a); // passes, same reference
  expect(a).not.toBe(b); // different references
  expect(a).toEqual(b); // passes, same content
});
```

Use `toBe` for primitives (numbers, strings, booleans) and `toEqual` for objects and arrays.

## 11: What is toStrictEqual and how is it different from toEqual?

`toStrictEqual` is a stricter version of `toEqual`. The main differences:

- `toEqual` ignores properties with an `undefined` value. `toStrictEqual` does not.
- `toEqual` ignores array holes (`[, 1]` equals `[undefined, 1]`). `toStrictEqual` does not.
- `toStrictEqual` checks that the objects have the same class. A class instance is not equal to a plain object with the same fields.

```js
class User {
  constructor(name) {
    this.name = name;
  }
}

test("strict equality", () => {
  expect({ a: 1, b: undefined }).toEqual({ a: 1 }); // passes
  expect({ a: 1, b: undefined }).not.toStrictEqual({ a: 1 });
  expect(new User("Anna")).toEqual({ name: "Anna" }); // passes
  expect(new User("Anna")).not.toStrictEqual({ name: "Anna" });
});
```

## 12: Which matchers check for null, undefined and truthiness?

- `toBeNull()` passes only for `null`
- `toBeUndefined()` passes only for `undefined`
- `toBeDefined()` is the opposite of `toBeUndefined()`
- `toBeTruthy()` passes for anything an `if` statement treats as true
- `toBeFalsy()` passes for `false`, `0`, `''`, `null`, `undefined` and `NaN`

```js
test("null and friends", () => {
  const value = null;
  expect(value).toBeNull();
  expect(value).toBeDefined();
  expect(value).toBeFalsy();
});
```

Prefer the specific ones (`toBeNull`, `toBe(false)`) when you know the exact value. `toBeTruthy` can hide bugs, because a string like `'false'` is truthy.

## 13: How do you compare numbers in Jest?

Use the comparison matchers:

```js
test("numbers", () => {
  const value = 2 + 2;
  expect(value).toBeGreaterThan(3);
  expect(value).toBeGreaterThanOrEqual(4);
  expect(value).toBeLessThan(5);
  expect(value).toBeLessThanOrEqual(4);
  expect(value).toBe(4);
  expect(value).toEqual(4);
});
```

For integers `toBe` and `toEqual` do the same thing.

## 14: How do you test floating point numbers?

Use `toBeCloseTo` instead of `toBe`, because floating point math has small rounding errors:

```js
test("adding floats", () => {
  expect(0.1 + 0.2).not.toBe(0.3); // 0.30000000000000004
  expect(0.1 + 0.2).toBeCloseTo(0.3);
  expect(1.005).toBeCloseTo(1.0, 1); // second argument is the number of digits
});
```

The default precision is 2 digits after the decimal point.

## 15: How do you check strings?

Use `toBe` for an exact match, `toMatch` for a regular expression or a substring, and `toHaveLength` for the length:

```js
test("strings", () => {
  const message = "Order 123 was shipped";
  expect(message).toMatch(/order \d+/i);
  expect(message).toMatch("shipped");
  expect(message).toHaveLength(21);
});
```

## 16: How do you check that an array contains an item?

Use `toContain` for primitives and `toContainEqual` for objects:

```js
test("arrays", () => {
  const fruits = ["apple", "banana"];
  expect(fruits).toContain("banana");

  const users = [{ id: 1 }, { id: 2 }];
  expect(users).toContainEqual({ id: 2 });
});
```

`toContain` uses `===`, so it will not find an object unless it is the same reference. `toContain` also works on strings, Sets and other iterables.

## 17: What does toHaveLength do?

It checks the `length` property of a value, so it works with arrays, strings and anything else that has `length`:

```js
expect([1, 2, 3]).toHaveLength(3);
expect("abc").toHaveLength(3);
```

It gives a clearer error message than `expect(arr.length).toBe(3)` because Jest prints the whole received value.

## 18: How do you check that an object has a property?

Use `toHaveProperty`. You can pass a dot path or an array path, and optionally the expected value:

```js
test("toHaveProperty", () => {
  const user = { name: "Anna", address: { city: "Tbilisi" } };

  expect(user).toHaveProperty("name");
  expect(user).toHaveProperty("address.city", "Tbilisi");
  expect(user).toHaveProperty(["address", "city"], "Tbilisi");
});
```

## 19: How do you test that a function throws an error?

Use `toThrow`. You can check that any error was thrown, or pass a string, a regex, an error class or an error object:

```js
function withdraw(amount) {
  if (amount < 0) throw new RangeError("Amount must be positive");
}

test("throws on negative amount", () => {
  expect(() => withdraw(-5)).toThrow();
  expect(() => withdraw(-5)).toThrow(RangeError);
  expect(() => withdraw(-5)).toThrow("must be positive");
  expect(() => withdraw(-5)).toThrow(/positive/);
});
```

In Jest 30 the old alias `toThrowError` was removed. Use `toThrow`.

## 20: Why do you need to wrap the code in a function when using toThrow?

If you write `expect(withdraw(-5)).toThrow()`, the function runs and throws before `expect` is even called. The error escapes and the test fails with that error instead of passing.

When you pass a function (`() => withdraw(-5)`), Jest calls it inside a `try/catch` and can check the thrown error.

## 21: What does .not do?

`.not` flips any matcher, so the test passes when the matcher would normally fail:

```js
expect(2 + 2).not.toBe(5);
expect(["a", "b"]).not.toContain("c");
expect(mockFn).not.toHaveBeenCalled();
```

## 22: How do you test code that returns a promise?

Return the promise from the test. Jest waits for it to resolve. If it rejects, the test fails.

```js
test("loads the user", () => {
  return fetchUser(1).then((user) => {
    expect(user.name).toBe("Anna");
  });
});
```

Most people use `async/await` instead because it is easier to read (see the next question).

## 23: How do you use async/await in Jest tests?

Mark the test function as `async` and `await` the code you are testing:

```js
test("loads the user", async () => {
  const user = await fetchUser(1);
  expect(user.name).toBe("Anna");
});

test("fails for a missing user", async () => {
  await expect(fetchUser(999)).rejects.toThrow("Not found");
});
```

Jest waits for the async function to finish before it moves on.

## 24: What are .resolves and .rejects?

They unwrap a promise before running the matcher. `.resolves` checks the resolved value and `.rejects` checks the rejection reason:

```js
test("resolves and rejects", async () => {
  await expect(Promise.resolve(42)).resolves.toBe(42);
  await expect(Promise.reject(new Error("boom"))).rejects.toThrow("boom");
});
```

You must `await` (or `return`) the expression. Without it, the test finishes before the promise settles and the assertion never runs.

## 25: How do you test callback-based code with done?

Add a `done` parameter to the test function. Jest will wait until you call `done()`. If you call `done(error)`, the test fails.

```js
test("reads the config", (done) => {
  readConfig((err, config) => {
    try {
      expect(err).toBeNull();
      expect(config.port).toBe(3000);
      done();
    } catch (error) {
      done(error);
    }
  });
});
```

The `try/catch` matters. Without it a failed `expect` throws inside the callback, `done` is never called and you get a timeout instead of a clear error. You cannot use `done` and return a promise in the same test; Jest throws an error if you do. For new code, wrapping the callback in a promise and using `async/await` is usually cleaner.

## 26: What happens if you forget to await or return a promise in a test?

The test function returns before the promise settles, so Jest marks the test as passed. Any `expect` inside a `.then()` runs later or not at all. If the assertion fails after the test is done, you may see a confusing error attached to a different test, or no error at all.

```js
// Bug: always passes
test("bad test", () => {
  fetchUser(1).then((user) => {
    expect(user.name).toBe("wrong name");
  });
});
```

The fix is to `return` the promise or use `async/await`. The `@typescript-eslint/no-floating-promises` rule and `eslint-plugin-jest` (`jest/valid-expect`) catch many of these mistakes.

## 27: What do beforeEach and afterEach do?

`beforeEach` runs before every test in its scope and `afterEach` runs after every test. They are used to create fresh data, reset mocks or clean up.

```js
let cart;

beforeEach(() => {
  cart = new Cart();
});

afterEach(() => {
  jest.clearAllMocks();
});

test("starts empty", () => {
  expect(cart.items).toHaveLength(0);
});
```

Hooks can be async. If they return a promise, Jest waits for it.

## 28: What do beforeAll and afterAll do?

`beforeAll` runs once before all the tests in its scope, and `afterAll` runs once after all of them. They are for expensive setup that can be shared, like starting a server or connecting to a test database.

```js
let server;

beforeAll(async () => {
  server = await startServer();
});

afterAll(async () => {
  await server.close();
});
```

Be careful with shared state. If one test changes data created in `beforeAll`, the next tests see that change.

## 29: How does the scope of hooks work with describe blocks?

A hook at the top of the file applies to every test in the file. A hook inside a `describe` only applies to the tests in that `describe` (and its nested blocks).

```js
beforeEach(() => console.log("top"));

describe("group", () => {
  beforeEach(() => console.log("inner"));

  test("a", () => {}); // logs "top" then "inner"
});

test("b", () => {}); // logs only "top"
```

## 30: In what order do Jest hooks and describe blocks run?

Jest first runs all `describe` bodies to collect the tests. Then it runs the tests in the order they were collected. For each test:

1. Outer `beforeEach` hooks run before inner ones.
2. The test runs.
3. Inner `afterEach` hooks run before outer ones.

`beforeAll` runs once before the first test in its block, and `afterAll` runs once after the last test.

A common mistake is putting setup code directly inside `describe` instead of a hook. That code runs during collection, before any test or hook.

## 31: How do you run only one test?

Use `test.only` (or `it.only`, `describe.only`). Within that file, Jest runs only the tests marked with `.only` and skips the rest.

```js
test.only("this one runs", () => {});
test("this one is skipped", () => {});
```

`fit` and `fdescribe` are older aliases. Don't commit `.only` by mistake. The `jest/no-focused-tests` lint rule helps catch it.

## 32: How do you skip a test?

Use `test.skip` (or `it.skip`, `describe.skip`). The test is reported as skipped and does not run.

```js
test.skip("waiting for the API fix", () => {});
```

`xit`, `xtest` and `xdescribe` are aliases. Skipped tests should be temporary, with a clear reason, or they get forgotten.

## 33: What is test.todo?

`test.todo` marks a test you plan to write later. It takes only a name, with no function, and shows up as "todo" in the summary.

```js
test.todo("handles an expired coupon");
```

It is useful when you are planning cases before writing them. Jest throws an error if you pass a test function to `test.todo`.

## 34: What is a mock function?

A mock function is a fake function that records how it was called. You can check how many times it was called, with which arguments and what it returned. You can also tell it what to return.

Mocks are used to replace real dependencies (an API client, a database call, a callback) so you can test one piece of code on its own.

## 35: How do you create a mock function?

Use `jest.fn()`. You can optionally pass an implementation:

```js
test("calls the callback for each item", () => {
  const callback = jest.fn();
  [1, 2].forEach(callback);

  expect(callback).toHaveBeenCalledTimes(2);
  expect(callback).toHaveBeenCalledWith(1, 0, [1, 2]);
});

const double = jest.fn((x) => x * 2);
double(4); // 8
```

## 36: What is mock.calls?

Every mock function has a `.mock` property with data about its calls. `mock.calls` is an array with one entry per call, and each entry is the array of arguments.

```js
test("mock.calls", () => {
  const fn = jest.fn();
  fn("a", 1);
  fn("b", 2);

  expect(fn.mock.calls).toEqual([
    ["a", 1],
    ["b", 2],
  ]);
  expect(fn.mock.calls[1][0]).toBe("b");
});
```

`mock.lastCall` gives the arguments of the last call.

## 37: What is mock.results?

`mock.results` holds what each call returned or threw. Each entry has a `type` (`'return'`, `'throw'` or `'incomplete'`) and a `value`.

```js
test("mock.results", () => {
  const fn = jest.fn((x) => x + 1);
  fn(1);

  expect(fn.mock.results[0]).toEqual({ type: "return", value: 2 });
});
```

There is also `mock.instances` (the `this` objects when called with `new`) and `mock.contexts` (the `this` value for each call).

## 38: What are mockReturnValue and mockReturnValueOnce?

`mockReturnValue` sets the value returned on every call. `mockReturnValueOnce` sets the value for the next call only. You can chain several `Once` calls. When they run out, the mock falls back to `mockReturnValue` (or `undefined`).

```js
test("return values", () => {
  const getRole = jest
    .fn()
    .mockReturnValue("user")
    .mockReturnValueOnce("admin")
    .mockReturnValueOnce("editor");

  expect(getRole()).toBe("admin");
  expect(getRole()).toBe("editor");
  expect(getRole()).toBe("user");
  expect(getRole()).toBe("user");
});
```

## 39: What is mockImplementation?

It sets the function that runs when the mock is called. Use it when the return value depends on the arguments or when you need side effects. `mockImplementationOnce` works for a single call.

```js
test("mockImplementation", () => {
  const getPrice = jest.fn().mockImplementation((id) => (id === 1 ? 10 : 0));

  expect(getPrice(1)).toBe(10);
  expect(getPrice(2)).toBe(0);
});
```

`jest.fn(impl)` is a short way to write `jest.fn().mockImplementation(impl)`.

## 40: How do you mock a function that returns a promise?

Use `mockResolvedValue` and `mockRejectedValue` (plus their `Once` versions):

```js
test("async mocks", async () => {
  const fetchUser = jest.fn().mockResolvedValue({ id: 1, name: "Anna" });
  await expect(fetchUser()).resolves.toEqual({ id: 1, name: "Anna" });

  const failing = jest.fn().mockRejectedValue(new Error("Network error"));
  await expect(failing()).rejects.toThrow("Network error");
});
```

`mockResolvedValue(x)` is the same as `mockImplementation(() => Promise.resolve(x))`.

## 41: What does toHaveBeenCalled check?

It checks that a mock function was called at least once. With `.not` it checks that it was never called.

```js
test("toHaveBeenCalled", () => {
  const onSave = jest.fn();
  saveForm({ valid: true }, onSave);

  expect(onSave).toHaveBeenCalled();
});
```

In Jest 30 the old alias `toBeCalled` was removed, so use `toHaveBeenCalled`.

## 42: What does toHaveBeenCalledTimes check?

It checks the exact number of calls:

```js
expect(sendEmail).toHaveBeenCalledTimes(1);
expect(logger.error).toHaveBeenCalledTimes(0);
```

This is often better than `toHaveBeenCalled`, because calling something twice by accident (like sending two emails) is a real bug.

## 43: What does toHaveBeenCalledWith check?

It checks that at least one call had exactly these arguments. Arguments are compared with the same rules as `toEqual`.

```js
test("toHaveBeenCalledWith", () => {
  const track = jest.fn();
  track("click", { button: "buy" });

  expect(track).toHaveBeenCalledWith("click", { button: "buy" });
  expect(track).toHaveBeenCalledWith("click", expect.any(Object));
});
```

## 44: How do you check the arguments of a specific call?

Use `toHaveBeenLastCalledWith` for the last call and `toHaveBeenNthCalledWith` for a specific call (counting from 1):

```js
test("specific calls", () => {
  const log = jest.fn();
  log("first");
  log("second");
  log("third");

  expect(log).toHaveBeenNthCalledWith(1, "first");
  expect(log).toHaveBeenNthCalledWith(2, "second");
  expect(log).toHaveBeenLastCalledWith("third");
});
```

The old aliases `lastCalledWith` and `nthCalledWith` were removed in Jest 30.

## 45: What is jest.spyOn?

`jest.spyOn(object, 'method')` wraps an existing method in a mock. By default the original method still runs, but now you can check how it was called. You can also replace its behavior with `mockImplementation` or `mockReturnValue`.

```js
const mathUtils = {
  add: (a, b) => a + b,
};

test("spyOn", () => {
  const spy = jest.spyOn(mathUtils, "add");

  expect(mathUtils.add(1, 2)).toBe(3); // real code still runs
  expect(spy).toHaveBeenCalledWith(1, 2);

  spy.mockRestore(); // put the original method back
});
```

## 46: How do you mock a whole module?

Call `jest.mock('module-path')` at the top of the test file. Every exported function of that module becomes a mock function that returns `undefined`:

```js
// userService.js uses ./api
const api = require("./api");
const { getUserName } = require("./userService");

jest.mock("./api");

test("gets the user name", async () => {
  api.fetchUser.mockResolvedValue({ name: "Anna" });

  await expect(getUserName(1)).resolves.toBe("Anna");
  expect(api.fetchUser).toHaveBeenCalledWith(1);
});
```

Jest moves `jest.mock` calls to the top of the file (this is called hoisting), so the mock is in place before the `require` runs, even though it looks like it comes after.

## 47: How do you give jest.mock a factory function?

Pass a function as the second argument. Whatever it returns is used as the module:

```js
jest.mock("./config", () => ({
  apiUrl: "http://localhost:4000",
  getTimeout: jest.fn(() => 1000),
}));
```

This is useful when you want specific values instead of auto-generated mocks, or when the real module can't even be loaded in tests. For an ES module with a default export, return `{ __esModule: true, default: ... }`.

## 48: What is the **mocks** folder?

It is a folder where you put manual mocks. For a user module, create `__mocks__` next to the file:

```
src/
  api.js
  __mocks__/
    api.js
```

Then `jest.mock('./api')` in a test uses `src/__mocks__/api.js` instead of the auto-generated mock.

For packages from `node_modules`, put the `__mocks__` folder next to `node_modules` (in the project root, or in one of the `roots` folders). Those mocks are applied automatically without calling `jest.mock`, except for Node core modules like `fs`, which always need an explicit `jest.mock('fs')`.

## 49: What is the difference between mockClear, mockReset and mockRestore?

- `mockClear()` clears the recorded data (`mock.calls`, `mock.results` and so on). The implementation stays.
- `mockReset()` does what `mockClear` does and also removes any implementation and return values, including the one passed to `jest.fn(impl)`. After a reset the mock returns `undefined`.
- `mockRestore()` does everything `mockReset` does and, for mocks created with `jest.spyOn`, puts back the original method.

```js
test("reset vs clear", () => {
  const fn = jest.fn().mockReturnValue(5);
  fn();

  fn.mockClear();
  expect(fn).not.toHaveBeenCalled();
  expect(fn()).toBe(5); // implementation kept

  fn.mockReset();
  expect(fn()).toBeUndefined(); // implementation removed
});
```

`jest.clearAllMocks()`, `jest.resetAllMocks()` and `jest.restoreAllMocks()` do the same for all mocks at once.

## 50: What is snapshot testing?

A snapshot test saves the output of some code to a file the first time it runs. On the next runs, Jest compares the new output with the saved one. If they are different, the test fails.

```js
test("renders the user card", () => {
  const html = renderUserCard({ name: "Anna", role: "admin" });
  expect(html).toMatchSnapshot();
});
```

It is handy for large outputs that are boring to assert by hand, like serialized UI, generated config or error messages. The downside is that people tend to update snapshots without reading the diff.

## 51: Where does Jest store snapshots?

In a `__snapshots__` folder next to the test file. For `card.test.js` the file is `__snapshots__/card.test.js.snap`. Each snapshot is saved under a key made from the test name and a counter:

```js
// Jest Snapshot v1, https://jestjs.io/docs/snapshot-testing

exports[`renders the user card 1`] = `"<div class="card">Anna (admin)</div>"`;
```

The file is plain JavaScript and is meant to be readable in code review.

## 52: How do you update snapshots?

When a change in output is expected, run Jest with `-u` (`--updateSnapshot`):

```bash
npx jest -u
npx jest card.test.js -u
```

In watch mode you can press `u` to update all failing snapshots, or `i` to go through them one by one. Always read the diff first. If you update without looking, the snapshot test stops catching anything.

## 53: What is an inline snapshot?

`toMatchInlineSnapshot()` writes the snapshot into the test file itself instead of a separate `.snap` file. The first run fills in the argument for you:

```js
test("formats the price", () => {
  expect(formatPrice(1234.5)).toMatchInlineSnapshot(`"$1,234.50"`);
});
```

Inline snapshots are easier to review because the expected value is right next to the code. They work best for small outputs. Jest formats the written code with Prettier if it can find it in the project.

## 54: Should snapshot files be committed to git?

Yes. Snapshot files are part of the test. If they are not in git, every machine and every CI run creates new snapshots and the tests can never fail.

Review snapshot changes in pull requests like any other code. In CI, Jest runs with `--ci` (automatic when the `CI` environment variable is set), and in that mode it does not write new snapshots. A missing snapshot fails the test instead.

## 55: How do you collect code coverage with Jest?

Run Jest with `--coverage` (or set `collectCoverage: true` in the config):

```bash
npx jest --coverage
```

Jest prints a table in the terminal and writes reports to the `coverage/` folder. Open `coverage/lcov-report/index.html` in a browser to see which lines were not run. Add `coverage/` to `.gitignore`.

## 56: What do the four coverage numbers mean?

- **Statements**: percent of statements that ran.
- **Branches**: percent of branches that ran, like both sides of an `if`, a ternary or `&&`.
- **Functions**: percent of functions that were called at least once.
- **Lines**: percent of lines with code that ran.

Branch coverage is usually the most useful one, because it shows paths you never tested, like the `else` case or an error case. 100% coverage does not mean the code is correct, only that it ran.

## 57: Where do you put Jest configuration?

You can use any of these:

- `jest.config.js`, `jest.config.ts`, `jest.config.mjs`, `jest.config.cjs` or `jest.config.json` in the project root
- A `"jest"` key in `package.json`
- A file passed with `--config path/to/config`

```js
// jest.config.js
/** @type {import('jest').Config} */
module.exports = {
  testEnvironment: "node",
  clearMocks: true,
};
```

The `@type` comment gives you autocomplete in the editor. Jest 30 also exports a `defineConfig` helper that does the same with less typing.

## 58: What is testEnvironment?

`testEnvironment` decides what global objects the tests run with:

- `node` (the default): a Node.js environment, with no `window` or `document`.
- `jsdom`: a fake browser environment with `window`, `document`, DOM APIs and events. It needs the `jest-environment-jsdom` package.

```js
module.exports = {
  testEnvironment: "jsdom",
};
```

Use `node` for back-end code and `jsdom` for code that touches the DOM, like React components.

## 59: What is jsdom and what can't it do?

jsdom is a JavaScript implementation of the DOM and other web standards that runs in Node.js. It lets you create elements, fire events and query the page in tests without a real browser.

It does not do layout or rendering. `getBoundingClientRect()` returns zeros, `offsetWidth` is 0, CSS is not really applied, and APIs like `matchMedia`, `IntersectionObserver` and `ResizeObserver` are missing. For those you add mocks, and for real visual or layout checks you use a browser tool like Playwright.

## 60: How do you change the test environment for a single file?

Add a docblock comment at the very top of the test file:

```js
/**
 * @jest-environment jsdom
 */

test("creates a button", () => {
  const button = document.createElement("button");
  expect(button.tagName).toBe("BUTTON");
});
```

This is useful when most of the project runs in `node` but a few files need the DOM, or the other way around.

## 61: What is watch mode?

`jest --watch` keeps Jest running and reruns tests when you save a file. It only runs tests related to files changed since the last git commit, so it is fast during development.

While it runs you can press keys to filter tests:

- `a` to run all tests
- `f` to run only failed tests
- `p` to filter by file name
- `t` to filter by test name
- `u` to update snapshots
- `q` to quit

## 62: What is the difference between --watch and --watchAll?

`--watch` uses git (or Mercurial) to find changed files and runs only the tests related to them. It needs a git repository.

`--watchAll` reruns all tests whenever any file changes. Use it when the project is not in git or when you want to run everything every time.

## 63: How do you run a single test file?

Pass the file path, or part of it, to Jest. It is treated as a regex pattern matched against test file paths:

```bash
npx jest src/cart/cart.test.js
npx jest cart
npm test -- cart
```

With `npm test` you need `--` so npm passes the arguments to Jest. In Jest 30 the config option is `--testPathPatterns` (the old `--testPathPattern` was renamed).

## 64: How do you run tests by name?

Use `-t` (`--testNamePattern`) with a regex. Jest runs only the tests whose full name (including the `describe` names) matches:

```bash
npx jest -t "adds an item"
npx jest cart.test.js -t "Cart addItem"
```

Tests that don't match are reported as skipped.

## 65: What are fake timers?

Fake timers replace `setTimeout`, `setInterval`, `Date` and similar APIs with versions you control from the test. Instead of waiting 5 real seconds, you tell Jest to move time forward 5 seconds right away.

This makes tests for debounce, retries, polling and timeouts fast and stable. Jest uses `@sinonjs/fake-timers` under the hood.

## 66: How do you use jest.useFakeTimers and runAllTimers?

```js
function delayedGreeting(callback) {
  setTimeout(() => callback("hello"), 1000);
}

test("calls the callback after 1 second", () => {
  jest.useFakeTimers();
  const callback = jest.fn();

  delayedGreeting(callback);
  expect(callback).not.toHaveBeenCalled();

  jest.runAllTimers();
  expect(callback).toHaveBeenCalledWith("hello");
});
```

`jest.runAllTimers()` runs every pending timer, including timers created by other timers. If code keeps scheduling new timers forever (like a `setInterval`), it stops after 100,000 timers and throws an error. Use `runOnlyPendingTimers` or `advanceTimersByTime` for those cases.

## 67: What does jest.advanceTimersByTime do?

It moves fake time forward by the given number of milliseconds and runs every timer that becomes due in that window:

```js
test("polls every second", () => {
  jest.useFakeTimers();
  const poll = jest.fn();
  setInterval(poll, 1000);

  jest.advanceTimersByTime(3500);
  expect(poll).toHaveBeenCalledTimes(3);
});
```

This gives you more control than `runAllTimers`, and it is the right choice for intervals.

## 68: How do you go back to real timers?

Call `jest.useRealTimers()`. A common pattern:

```js
beforeEach(() => {
  jest.useFakeTimers();
});

afterEach(() => {
  jest.useRealTimers();
});
```

You can also turn on fake timers for the whole project with `fakeTimers: { enableGlobally: true }` in the config.

## 69: What is test.each?

`test.each` runs the same test with different data, so you don't copy and paste the same test many times:

```js
test.each([
  [1, 1, 2],
  [2, 3, 5],
  [-1, 1, 0],
])("add(%i, %i) returns %i", (a, b, expected) => {
  expect(add(a, b)).toBe(expected);
});
```

Each row becomes its own test with its own name in the output. The `%i`, `%s` and similar placeholders are filled in with the row values.

## 70: What is describe.each?

It works like `test.each` but repeats a whole `describe` block for each row:

```js
describe.each([
  ["admin", true],
  ["guest", false],
])("when the role is %s", (role, canDelete) => {
  test(`canDelete is ${canDelete}`, () => {
    expect(getPermissions(role).canDelete).toBe(canDelete);
  });
});
```

## 71: What is expect.any?

`expect.any(Constructor)` matches any value created by that constructor (or of that primitive type). It is useful when a value changes every run, like an id or a date:

```js
test("creates an order", () => {
  const order = createOrder({ item: "book" });

  expect(order).toEqual({
    id: expect.any(String),
    item: "book",
    createdAt: expect.any(Date),
  });
});
```

`expect.any(Number)` also matches primitive numbers, and `expect.any(String)` matches primitive strings.

## 72: What is expect.anything?

`expect.anything()` matches any value except `null` and `undefined`. It is handy when you only care that an argument was passed:

```js
expect(logger.info).toHaveBeenCalledWith("User created", expect.anything());
```

## 73: What is expect.objectContaining?

It matches an object that has at least the given properties. Extra properties are ignored:

```js
test("sends the event", () => {
  const send = jest.fn();
  send({ type: "signup", userId: 7, timestamp: Date.now() });

  expect(send).toHaveBeenCalledWith(
    expect.objectContaining({ type: "signup", userId: 7 }),
  );
});
```

## 74: What is expect.arrayContaining?

It matches an array that contains all the given items, in any order. The received array can have extra items:

```js
expect(["a", "b", "c"]).toEqual(expect.arrayContaining(["c", "a"]));
```

`expect.not.arrayContaining([...])` matches arrays that don't contain all of those items.

## 75: What are expect.stringContaining and expect.stringMatching?

They match strings inside bigger structures like objects or call arguments:

```js
expect(logger.error).toHaveBeenCalledWith(expect.stringContaining("timeout"));

expect(user).toEqual({
  email: expect.stringMatching(/@example\.com$/),
});
```

`stringContaining` checks for a substring and `stringMatching` checks a regex or a substring.

## 76: What is babel-jest?

`babel-jest` is the transformer Jest uses by default to turn modern JavaScript, JSX and TypeScript into code Node can run. If a Babel config file (like `babel.config.js`) exists in the project, Jest applies it to your files automatically.

It is installed together with Jest. Babel only removes TypeScript types, it does not check them.

## 77: How do you use Jest with TypeScript?

There are two common ways:

1. **ts-jest**: compiles TS with the TypeScript compiler and can report type errors in tests.

   ```bash
   npm install --save-dev ts-jest @types/jest
   npx ts-jest config:init
   ```

2. **babel-jest** with `@babel/preset-typescript`: faster, but it only strips types and does not check them. You run `tsc --noEmit` separately for type checking.

Other fast options are `@swc/jest` and `esbuild`-based transformers. For types, use `@types/jest` (global types) or import from `@jest/globals`.

## 78: What is @jest/globals?

It is a package that lets you import Jest functions explicitly instead of using globals:

```js
import { describe, expect, jest, test } from "@jest/globals";

test("works with explicit imports", () => {
  const fn = jest.fn();
  fn();
  expect(fn).toHaveBeenCalled();
});
```

It is useful with TypeScript (no need for `@types/jest`), with ES modules, and when you set `injectGlobals: false` so the globals don't exist at all.

## 79: What is the difference between @types/jest and @jest/globals?

`@types/jest` is a community package on DefinitelyTyped that adds global types for `describe`, `test`, `expect` and `jest`. Its version may lag behind Jest itself.

`@jest/globals` is published by the Jest team with every release, so its types always match the Jest version you have. You have to import from it in each file. Both are fine; just don't mix them in one project, because their types for custom matchers are declared in different places.

## 80: What do rootDir and roots do?

- `rootDir` is the root folder Jest works from. It defaults to the folder with the config file (or `package.json`). You can use `<rootDir>` in other options.
- `roots` is a list of folders where Jest looks for tests and modules. It defaults to `['<rootDir>']`.

```js
module.exports = {
  roots: ["<rootDir>/src"],
};
```

Limiting `roots` makes Jest faster because it scans fewer files.

## 81: What is testPathIgnorePatterns?

It is a list of regex patterns. Test files whose path matches any of them are skipped. The default is `['/node_modules/']`.

```js
module.exports = {
  testPathIgnorePatterns: ["/node_modules/", "/dist/", "/e2e/"],
};
```

A common use is to keep Jest away from Playwright or Cypress tests that also end in `.spec.ts`.

## 82: How do you handle CSS and image imports in Jest?

Node can't import `.css` or `.png` files, so tests crash on `import './styles.css'`. Map them to simple stubs with `moduleNameMapper`:

```js
module.exports = {
  moduleNameMapper: {
    "\\.(css|less|scss)$": "identity-obj-proxy",
    "\\.(png|jpg|svg)$": "<rootDir>/test/fileMock.js",
  },
};
```

```js
// test/fileMock.js
module.exports = "test-file-stub";
```

`identity-obj-proxy` returns the class name itself for CSS modules, so `styles.button` becomes `'button'`.

## 83: What is setupFilesAfterEnv?

It is a list of files that run before each test file, after the test framework is ready. That means you can use `expect`, `jest` and hooks inside them.

```js
module.exports = {
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
};
```

```js
// jest.setup.js
require("@testing-library/jest-dom");

afterEach(() => {
  jest.clearAllMocks();
});
```

It is the usual place to add custom matchers and global hooks.

## 84: What do the clearMocks, resetMocks and restoreMocks options do?

They clean up mocks before every test, so you don't need to do it by hand:

- `clearMocks: true` calls `jest.clearAllMocks()` before each test.
- `resetMocks: true` calls `jest.resetAllMocks()` before each test.
- `restoreMocks: true` calls `jest.restoreAllMocks()` before each test.

```js
module.exports = {
  clearMocks: true,
};
```

`clearMocks` is a safe default. `resetMocks` also removes implementations, including ones set in a `jest.mock` factory, which surprises people.

## 85: What is the difference between a test suite and a test in Jest output?

In Jest output, a test suite is a test file. A test is a single `test` or `it` call. The summary shows both:

```
Test Suites: 1 failed, 11 passed, 12 total
Tests:       2 failed, 140 passed, 142 total
```

A suite can also fail without any failing test, for example when the file has a syntax error or a module can't be imported.

## 86: How do you read a failing test in Jest output?

Jest shows:

1. The full test name, including `describe` names.
2. The matcher that failed, with expected and received values. For objects it shows a diff with `-` for expected and `+` for received.
3. The code frame, which is the lines of your test around the failing `expect`, with a marker on the exact line.

```
  ● Cart › addItem › adds a new item

    expect(received).toEqual(expected) // deep equality

    - Expected  - 1
    + Received  + 1

      {
    -   "count": 2,
    +   "count": 1,
      }
```

Start with the diff. Most of the time it tells you what is wrong.

## 87: What does --verbose do?

It prints every test name with its result, grouped by `describe`, instead of just the file name:

```bash
npx jest --verbose
```

When you run a single test file, Jest shows this view by default.

## 88: What does the --ci flag do?

`--ci` tells Jest it is running in a CI system. The main change is that new snapshots are not written automatically. A test with a missing snapshot fails instead of passing.

Jest turns this on by itself when it detects a CI environment (for example when the `CI` environment variable is set). Use `--ci=false` to turn it off.

## 89: What does --bail do?

`--bail` stops the run after the first failing test suite. `--bail=3` stops after 3 failing suites.

```bash
npx jest --bail
```

It saves time in CI when one failure means the rest doesn't matter, for example in a smoke test step.

## 90: What does --passWithNoTests do?

Normally Jest exits with an error if it finds no tests. `--passWithNoTests` makes it exit with success instead.

It is handy in monorepos or with `lint-staged`, where Jest might run with a filter that matches no test files.

## 91: What does jest --init do?

It asks a few questions (TypeScript or not, test environment, coverage, mock cleanup) and creates a `jest.config.js` (or `.ts`) file. The file lists all options as comments, which is a nice way to see what can be configured.

```bash
npx jest --init
```

## 92: What does --listTests do?

It prints the paths of all test files Jest would run with the current options, and does not run them. It is useful to check that `testMatch`, `roots` and ignore patterns pick up the right files.

```bash
npx jest --listTests
```

## 93: What does --silent do?

It hides `console.log`, `console.warn` and other console output from tests. The test results are still printed.

```bash
npx jest --silent
```

It is useful when the code logs a lot and you only care about pass or fail. Don't use it to hide real warnings that should be fixed.

## 94: What does toMatchObject do?

It checks that an object contains the given properties with matching values. Extra properties in the received object are ignored. It also works with nested objects and arrays of objects:

```js
test("toMatchObject", () => {
  const user = {
    id: 1,
    name: "Anna",
    address: { city: "Tbilisi", zip: "0100" },
  };

  expect(user).toMatchObject({ name: "Anna", address: { city: "Tbilisi" } });
});
```

## 95: What does toBeInstanceOf check?

It checks that a value was created by a class, using `instanceof`:

```js
class ValidationError extends Error {}

test("toBeInstanceOf", () => {
  const error = new ValidationError("bad input");
  expect(error).toBeInstanceOf(ValidationError);
  expect(error).toBeInstanceOf(Error);
});
```

## 96: How do you check for NaN?

Use `toBeNaN()`. `toBe(NaN)` also works because `Object.is(NaN, NaN)` is `true`, but `toBeNaN` reads better:

```js
expect(parseInt("abc")).toBeNaN();
expect(Number("12")).not.toBeNaN();
```

## 97: What is expect.assertions?

`expect.assertions(n)` checks that exactly `n` assertions were called during the test. It is mainly used in async tests to make sure assertions in callbacks or `catch` blocks really ran:

```js
test("rejects with a 404", async () => {
  expect.assertions(1);
  try {
    await fetchUser(999);
  } catch (error) {
    expect(error.status).toBe(404);
  }
});
```

Without `expect.assertions(1)`, this test passes if `fetchUser` resolves, because the `catch` never runs.

## 98: What is expect.hasAssertions?

`expect.hasAssertions()` checks that at least one assertion ran in the test. Use it when the exact number is not known or not important:

```js
test("validates every item", () => {
  expect.hasAssertions();
  getItems().forEach((item) => {
    expect(item.price).toBeGreaterThan(0);
  });
});
```

If `getItems()` returns an empty array, this test fails instead of passing silently.

## 99: What is the Arrange, Act, Assert pattern?

It is a simple way to structure a test in three parts:

1. **Arrange**: set up the data and mocks.
2. **Act**: call the code you are testing.
3. **Assert**: check the result.

```js
test("applies a 10% discount", () => {
  // Arrange
  const cart = new Cart();
  cart.add({ price: 100 });

  // Act
  cart.applyCoupon("SAVE10");

  // Assert
  expect(cart.total).toBe(90);
});
```

Keeping these parts clear makes tests easier to read and spot what is being tested.

## 100: How should you name test files and where should you put them?

Common options:

- Next to the source file: `cart.js` and `cart.test.js`.
- In a `__tests__` folder next to the code: `__tests__/cart.test.js`.
- In a top-level `test/` or `tests/` folder that mirrors `src/`.

Both `.test.js` and `.spec.js` work by default. Putting tests next to the code makes them easy to find and move together. Whatever you pick, use the same pattern across the project.

## 101: Should tests depend on each other?

No. Each test should set up what it needs and work on its own, in any order. If test B only passes because test A ran first and left some data behind, then running B alone with `.only` or `-t` fails, and reordering tests breaks the suite.

Use `beforeEach` to create fresh state, and clean up in `afterEach`. Jest's `--randomize` flag shuffles test order inside each file and helps you find hidden dependencies.

## 102: What is the difference between a unit test and an integration test in Jest?

Jest can run both. The difference is how much real code runs:

- A **unit test** checks one function or class on its own. Its dependencies (database, HTTP, other modules) are mocked.
- An **integration test** checks several parts working together with fewer mocks, like an Express route with a real (test) database, or a React component with its child components and a mocked API.

Unit tests are faster and point to the exact broken piece. Integration tests catch problems in how pieces fit together. Most projects need both.

## 103: Can Jest run end-to-end tests in a real browser?

Not by itself. Jest runs in Node.js, and even with the `jsdom` environment there is no real browser, no real layout and no real network between a front end and a back end.

For end-to-end tests use a tool made for it, like Playwright or Cypress. A common setup is Jest for unit and integration tests, and Playwright for a smaller set of end-to-end tests.

## 104: What changed in Jest 30?

Jest 30 came out in June 2025, about three years after Jest 29. The main changes:

- Node 14, 16, 19 and 21 are no longer supported. The minimum TypeScript version is 5.4.
- `jest-environment-jsdom` moved from jsdom 21 to jsdom 26.
- Many matcher aliases were removed, like `toBeCalled` and `toThrowError`.
- `--testPathPattern` became `--testPathPatterns`.
- `jest.genMockFromModule` was removed. Use `jest.createMockFromModule`.
- Faster module resolution and lower memory use.
- New features like `expect.arrayOf`, `jest.unstable_unmockModule`, `jest.onGenerateMock`, and `using` support for spies.

Later 30.x releases added helpers like `defineConfig` and `mergeConfig` for config files. Check the official migration guide before upgrading a large project.

## 105: Which matcher aliases were removed in Jest 30?

These aliases are gone, and you use the full names instead:

| Removed            | Use instead                |
| ------------------ | -------------------------- |
| `toBeCalled`       | `toHaveBeenCalled`         |
| `toBeCalledTimes`  | `toHaveBeenCalledTimes`    |
| `toBeCalledWith`   | `toHaveBeenCalledWith`     |
| `lastCalledWith`   | `toHaveBeenLastCalledWith` |
| `nthCalledWith`    | `toHaveBeenNthCalledWith`  |
| `toReturn`         | `toHaveReturned`           |
| `toReturnTimes`    | `toHaveReturnedTimes`      |
| `toReturnWith`     | `toHaveReturnedWith`       |
| `lastReturnedWith` | `toHaveLastReturnedWith`   |
| `nthReturnedWith`  | `toHaveNthReturnedWith`    |
| `toThrowError`     | `toThrow`                  |

The `jest/no-alias-methods` rule from `eslint-plugin-jest` can fix these for you automatically.

## 106: What is the default test timeout and how do you change it?

The default timeout is 5 seconds per test. If a test (or hook) takes longer, it fails with a timeout error. You can change it in three ways:

```js
// 1. For one test, as the third argument
test("slow import", async () => {
  await importBigFile();
}, 20_000);

// 2. For the rest of a file
jest.setTimeout(10_000);
```

```js
// 3. For the whole project in jest.config.js
module.exports = {
  testTimeout: 10_000,
};
```

Hooks also accept a timeout as the second argument: `beforeAll(fn, 30_000)`. If a test times out, first check for a missing `await` or a `done` that is never called before you raise the limit.

## 107: How do you test code that writes to the console?

Spy on the console method and replace it with an empty function, so the output doesn't clutter the test run:

```js
test("warns when the config is missing", () => {
  const warn = jest.spyOn(console, "warn").mockImplementation(() => {});

  loadConfig(undefined);

  expect(warn).toHaveBeenCalledWith("Config not found, using defaults");
  warn.mockRestore();
});
```

Call `mockRestore()` (or use `restoreMocks: true`) so the real console comes back for other tests.

## 108: How do you mock Math.random?

Use `jest.spyOn` on `Math`:

```js
function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

test("rolls a six", () => {
  const spy = jest.spyOn(Math, "random").mockReturnValue(0.99);
  expect(rollDice()).toBe(6);
  spy.mockRestore();
});
```

A cleaner long-term option is to pass a random function into your code as an argument, so tests can pass a fixed one without mocking globals.

## 109: How do you mock the current date?

Use fake timers and `setSystemTime`:

```js
function isWeekend() {
  const day = new Date().getDay();
  return day === 0 || day === 6;
}

test("Saturday is a weekend day", () => {
  jest.useFakeTimers().setSystemTime(new Date("2025-01-04T12:00:00Z"));
  expect(isWeekend()).toBe(true);
  jest.useRealTimers();
});
```

Both `new Date()` and `Date.now()` return the fake time. You can also pass the time when turning on fake timers: `jest.useFakeTimers({ now: new Date('2025-01-04') })`. Watch out for time zones: `getDay()` uses local time, so pick a time that is the same day in every zone your CI might use, or set `TZ`.

## 110: How do you test a class?

Create an instance, call its methods and check the results or state. Use `beforeEach` to get a fresh instance for every test:

```js
class Counter {
  #value = 0;
  increment() {
    this.#value += 1;
  }
  get value() {
    return this.#value;
  }
}

describe("Counter", () => {
  let counter;

  beforeEach(() => {
    counter = new Counter();
  });

  test("starts at 0", () => {
    expect(counter.value).toBe(0);
  });

  test("increments by 1", () => {
    counter.increment();
    expect(counter.value).toBe(1);
  });
});
```

Test the public methods. Private fields are an implementation detail, and you can't reach `#private` fields from a test anyway.

## 111: What is mockName used for?

`mockName('name')` gives a mock a name that shows up in error messages instead of the default `jest.fn()`:

```js
const onSubmit = jest.fn().mockName("onSubmit");
expect(onSubmit).toHaveBeenCalled();
// Error: expect(onSubmit).toHaveBeenCalled()
```

It helps when a test has several mocks and you want to know quickly which one failed.

## 112: What does mockReturnThis do?

It makes the mock return `this`, which is useful for mocking chainable APIs:

```js
test("mockReturnThis", () => {
  const query = {
    where: jest.fn().mockReturnThis(),
    orderBy: jest.fn().mockReturnThis(),
    limit: jest.fn().mockReturnValue([{ id: 1 }]),
  };

  const rows = query.where("active", true).orderBy("name").limit(10);
  expect(rows).toEqual([{ id: 1 }]);
  expect(query.where).toHaveBeenCalledWith("active", true);
});
```

## 113: What is the jest object?

`jest` is a global object (also available from `@jest/globals`) with helper methods for tests. The main groups are:

- **Mocks**: `jest.fn`, `jest.spyOn`, `jest.mock`, `jest.clearAllMocks`, `jest.replaceProperty`
- **Modules**: `jest.requireActual`, `jest.resetModules`, `jest.isolateModules`
- **Timers**: `jest.useFakeTimers`, `jest.advanceTimersByTime`, `jest.setSystemTime`
- **Misc**: `jest.setTimeout`, `jest.retryTimes`

It is a different thing from `expect`, which is for assertions.

## 114: How do you run all tests in one folder?

Pass the folder path as a pattern:

```bash
npx jest src/orders
npm test -- src/orders
```

The argument is a regex matched against the full test file paths, so `orders` alone also works, but it may match other folders too. To run several patterns, pass them all: `npx jest orders payments`.

## 115: When do you use jest.mock and when jest.spyOn?

- Use `jest.mock` to replace a whole module that your code imports, like an API client or a database driver. The real module is not loaded at all (unless you ask for it).
- Use `jest.spyOn` to watch or replace one method on an existing object, while keeping the rest of the object real. It is easy to undo with `mockRestore`.

```js
jest.mock("./emailClient"); // whole module is fake

const spy = jest.spyOn(Date, "now").mockReturnValue(0); // one method is fake
```

A simple rule: mock modules at the boundary of your system (network, database, file system), and spy when you only need to control or check one method.

## 116: Do tests inside one file run in order?

Yes. By default tests in a file run one after another, in the order they appear. The next test starts only after the previous one (including its async work and hooks) is finished.

You can change this with `test.concurrent`, which starts tests at the same time, or `--randomize`, which shuffles the order. Even though order is stable by default, write tests that don't rely on it.

## 117: Do test files run in parallel?

Yes. Jest runs test files in parallel using worker processes. The number of workers defaults to the number of CPU cores minus one in normal mode, and half of the available cores in watch mode. You can change it:

```bash
npx jest --maxWorkers=4
npx jest --maxWorkers=50%
npx jest --runInBand   # one file at a time in the main process
```

When there is only one test file, or when Jest thinks it will be faster, it runs in band automatically.

## 118: Are test files isolated from each other?

Yes. Each test file gets its own module registry and its own global environment. A module loaded in one file is a fresh copy in another file, and global variables set in one file are not visible in another.

Tests inside the same file are not isolated in this way. They share the same modules and globals, so state can leak between them. That is why you reset state in `beforeEach` or `afterEach`.

## 119: How do you test DOM code with Jest?

Set `testEnvironment` to `jsdom`, build the DOM you need, run your code and check the result. Use `dispatchEvent` or `.click()` to trigger events:

```js
/**
 * @jest-environment jsdom
 */

function setupToggle(button, panel) {
  button.addEventListener("click", () => {
    panel.hidden = !panel.hidden;
  });
}

test("toggles the panel on click", () => {
  document.body.innerHTML = `
    <button id="toggle">Toggle</button>
    <div id="panel" hidden></div>
  `;
  const button = document.getElementById("toggle");
  const panel = document.getElementById("panel");

  setupToggle(button, panel);
  button.click();

  expect(panel.hidden).toBe(false);
});
```

For anything more than small cases, `@testing-library/dom` gives you better queries and event helpers.

## 120: How do Jest and React Testing Library work together?

They do different jobs. Jest is the test runner: it finds tests, runs them, gives you `expect`, mocks and the jsdom environment. React Testing Library (RTL) renders React components into that jsdom and gives you ways to find elements and interact with them like a user would.

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Counter from "./Counter";

test("increments the count", async () => {
  render(<Counter />);

  await userEvent.click(screen.getByRole("button", { name: /increment/i }));

  expect(screen.getByText("Count: 1")).toBeInTheDocument();
});
```

`toBeInTheDocument` comes from `@testing-library/jest-dom`, which adds DOM matchers to Jest.

## 121: Is there a fail function in Jest?

Not anymore. `fail()` came from Jasmine, and Jest's default runner, `jest-circus`, does not define it. Calling it gives `ReferenceError: fail is not defined`.

To fail a test on purpose, throw an error:

```js
throw new Error("This code should not be reached");
```

For "this should have thrown" cases, use `expect(...).rejects.toThrow()` or `expect.assertions(n)` instead.

## 122: How do you check both the type and the message of a thrown error?

Call `toThrow` twice, once with the class and once with the message. Or pass an asymmetric matcher that checks several fields:

```js
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

function parseAge(value) {
  if (Number.isNaN(Number(value)))
    throw new ValidationError("Age must be a number");
  return Number(value);
}

test("throws a ValidationError with a clear message", () => {
  expect(() => parseAge("abc")).toThrow(ValidationError);
  expect(() => parseAge("abc")).toThrow("Age must be a number");

  expect(() => parseAge("abc")).toThrow(
    expect.objectContaining({
      name: "ValidationError",
      message: "Age must be a number",
    }),
  );
});
```

When you pass an error instance, like `toThrow(new Error('x'))`, Jest compares the message (and in Jest 30 also `cause`), not the class, so don't rely on it to check the type.

## 123: How do you test that an async function throws?

Use `rejects.toThrow` and `await` it:

```js
async function getUser(id) {
  if (!id) throw new Error("id is required");
  return { id };
}

test("throws without an id", async () => {
  await expect(getUser()).rejects.toThrow("id is required");
});
```

Notice you pass the promise (`getUser()`), not a function like with sync `toThrow`. Wrapping it in an arrow function also works for `rejects`, since Jest calls the function and uses the promise it returns.

## 124: How does toEqual handle Dates, Sets and Maps?

`toEqual` knows how to compare these types:

- Two `Date` objects are equal if they hold the same time.
- Two `Set` objects are equal if they have the same values, in any order.
- Two `Map` objects are equal if they have the same keys and values.

```js
test("special types", () => {
  expect(new Date("2025-01-01")).toEqual(new Date("2025-01-01"));
  expect(new Set([1, 2])).toEqual(new Set([2, 1]));
  expect(new Map([["a", 1]])).toEqual(new Map([["a", 1]]));
});
```

## 125: How do you mock a default export?

For an ES module with a default export (compiled by Babel or TypeScript), return `__esModule: true` and a `default` key from the factory:

```js
// logger.js
export default function log(message) {
  console.log(message);
}
```

```js
import log from "./logger";
import { saveUser } from "./saveUser";

jest.mock("./logger", () => ({
  __esModule: true,
  default: jest.fn(),
}));

test("logs after saving", () => {
  saveUser({ name: "Anna" });
  expect(log).toHaveBeenCalledWith("User saved");
});
```

Without `__esModule: true`, the interop code treats the whole object as the default export and `log` would be the object, not your mock function.

## 126: What is the difference between npx jest and npm test?

`npx jest` runs the Jest binary from `node_modules` directly. `npm test` runs whatever is in the `"test"` script of `package.json`, which is often just `jest`, but may include extra flags or environment variables.

To pass extra flags through `npm test`, put them after `--`:

```bash
npm test -- --watch
npm test -- cart -t "adds an item"
```

## 127: What do toHaveReturned and toHaveReturnedWith check?

They check what a mock function returned, not how it was called:

- `toHaveReturned()` checks that the mock returned at least once without throwing.
- `toHaveReturnedTimes(n)` checks the number of successful returns.
- `toHaveReturnedWith(value)` checks that at least one call returned this value.
- `toHaveLastReturnedWith` and `toHaveNthReturnedWith` check a specific call.

```js
test("toHaveReturnedWith", () => {
  const double = jest.fn((x) => x * 2);
  double(2);
  expect(double).toHaveReturnedWith(4);
});
```

## 128: Does a test without assertions pass?

Yes. A test passes as long as it doesn't throw and doesn't time out. That means a test where the `expect` calls are skipped (for example inside a `catch` that never runs, or inside an empty loop) passes silently.

To protect against this, use `expect.assertions(n)` or `expect.hasAssertions()` in tests that have assertions in callbacks or branches. The `jest/expect-expect` lint rule warns about tests with no `expect` at all.

## 129: What are test doubles?

"Test double" is the general name for anything that replaces a real dependency in a test. Common kinds:

- **Stub**: returns fixed data, like `jest.fn().mockReturnValue(42)`.
- **Spy**: records calls to a real function, like `jest.spyOn(obj, 'method')`.
- **Mock**: a fake that you also check, like asserting `toHaveBeenCalledWith`.
- **Fake**: a simple working version, like an in-memory repository instead of a database.

In Jest, `jest.fn()` can act as a stub, spy or mock depending on how you use it. People often call all of them "mocks".

## 130: What exit code does Jest return?

Jest exits with code `0` when all tests pass and `1` when any test fails, a suite fails to run, or coverage is below the threshold. CI systems use this to mark the build as failed.

```bash
npx jest && echo "all good"
```

## 131: What is the Jest cache and how do you clear it?

Jest caches transformed files (for example, TypeScript compiled to JavaScript) and data about your file system, so the next run is faster. The cache lives in a temp folder by default. You can see the folder with `npx jest --showConfig` (look for `cacheDirectory`).

When tests behave strangely after changing Babel config, transformers or dependencies, clear it:

```bash
npx jest --clearCache
```

You can also run once without cache using `--no-cache`.

## 132: What is jest.mocked?

`jest.mocked(fn)` is a TypeScript helper. It does nothing at runtime, it just returns the same value, but it changes the type so TypeScript knows the function is a mock:

```ts
import { jest, test, expect } from "@jest/globals";
import { fetchUser } from "./api";

jest.mock("./api");

test("typed mock", async () => {
  jest.mocked(fetchUser).mockResolvedValue({ id: 1, name: "Anna" });

  await expect(fetchUser(1)).resolves.toEqual({ id: 1, name: "Anna" });
});
```

Without it you would need a cast like `(fetchUser as jest.Mock)`. TypeScript also checks that the value you pass to `mockResolvedValue` matches the real return type.

## 133: How do you test a function that changes its argument?

Pass an object, call the function and check the object afterwards:

```js
function addTag(post, tag) {
  post.tags.push(tag);
}

test("adds the tag to the post", () => {
  const post = { tags: ["js"] };
  addTag(post, "jest");
  expect(post.tags).toEqual(["js", "jest"]);
});
```

If the function should not change its argument, freeze the input with `Object.freeze` or keep a copy and compare it after the call. A frozen object makes changes throw in strict mode, which ES modules always use.

## 134: How do you write good test names?

A good name says what is being tested, in what situation and what should happen. When the test fails, the name alone should tell you what broke.

```js
// Hard to understand when it fails
test("works", () => {});
test("test 2", () => {});

// Clear
test("returns 0 when the cart is empty", () => {});
test("throws when the coupon is expired", () => {});
```

Using `describe` for the function or class name keeps each test name short: `Cart › total › returns 0 when the cart is empty`.

## 135: Should you use beforeEach or a setup function?

Both work. `beforeEach` with shared variables is fine for simple cases. A setup function that returns what the test needs is often clearer, because each test shows exactly what it uses and can pass options:

```js
function setup(overrides = {}) {
  const repo = { save: jest.fn(), find: jest.fn() };
  const service = new UserService(repo, { maxUsers: 10, ...overrides });
  return { repo, service };
}

test("saves a new user", () => {
  const { repo, service } = setup();
  service.create({ name: "Anna" });
  expect(repo.save).toHaveBeenCalled();
});

test("refuses when the limit is reached", () => {
  const { service } = setup({ maxUsers: 0 });
  expect(() => service.create({ name: "Anna" })).toThrow("limit");
});
```

## 136: What is eslint-plugin-jest?

It is an ESLint plugin with rules for Jest tests. Some useful rules:

- `jest/no-focused-tests`: catches `test.only` left in the code.
- `jest/no-disabled-tests`: warns about skipped tests.
- `jest/valid-expect`: catches `expect` without a matcher or a missing `await` on `.resolves`.
- `jest/expect-expect`: warns about tests with no assertions.
- `jest/no-alias-methods`: replaces old matcher aliases (useful when moving to Jest 30).

```js
// eslint.config.js
import jest from "eslint-plugin-jest";

export default [
  {
    files: ["**/*.test.js"],
    ...jest.configs["flat/recommended"],
  },
];
```

## 137: What is @testing-library/jest-dom?

It is a library that adds DOM-specific matchers to Jest, like:

- `toBeInTheDocument()`
- `toBeVisible()`
- `toBeDisabled()`
- `toHaveTextContent('Hello')`
- `toHaveAttribute('href', '/home')`
- `toHaveValue('abc')`

You load it once in a setup file:

```js
// jest.setup.js (listed in setupFilesAfterEnv)
import "@testing-library/jest-dom";
```

These matchers give better error messages than checking DOM properties by hand.

## 138: How do you mock fetch in a simple test?

Node 18+ has a global `fetch`, so you can spy on it:

```js
async function getTodo(id) {
  const res = await fetch(`https://api.example.com/todos/${id}`);
  if (!res.ok) throw new Error("Request failed");
  return res.json();
}

test("returns the todo", async () => {
  const fetchSpy = jest.spyOn(globalThis, "fetch").mockResolvedValue({
    ok: true,
    json: async () => ({ id: 1, title: "Write tests" }),
  });

  await expect(getTodo(1)).resolves.toEqual({ id: 1, title: "Write tests" });
  expect(fetchSpy).toHaveBeenCalledWith("https://api.example.com/todos/1");

  fetchSpy.mockRestore();
});
```

In the `jsdom` environment `fetch` may not exist at all, so you would assign `globalThis.fetch = jest.fn()` instead. For bigger projects, a library like MSW that mocks at the network level is usually easier to maintain.

## 139: How do you check that an array or object is empty?

```js
expect([]).toHaveLength(0);
expect([]).toEqual([]);
expect({}).toEqual({});
expect(Object.keys(result)).toHaveLength(0);
```

`toHaveLength(0)` gives a clear message showing the received array when it fails. Note that `expect({}).toEqual({})` also passes for `{ a: undefined }`, so use `toStrictEqual({})` if that matters.

## 140: Does toEqual care about array order?

Yes. `toEqual([1, 2])` fails for `[2, 1]`. If order does not matter, you can:

```js
expect(result).toEqual(expect.arrayContaining([1, 2]));
expect(result).toHaveLength(2);

// or sort before comparing
expect([...result].sort()).toEqual([1, 2]);
```

`arrayContaining` alone allows extra items, so add a length check if you need an exact set. Sets are the exception: `toEqual` ignores order for `Set` values.

## 141: What is a test fixture?

A fixture is fixed data or state that tests use as input. It can be an object in the test file, a JSON file, or a set of database rows created before tests.

```js
// fixtures/users.js
module.exports = {
  admin: { id: 1, name: "Admin", role: "admin" },
  guest: { id: 2, name: "Guest", role: "guest" },
};
```

```js
const { admin } = require("./fixtures/users");

test("admins can delete posts", () => {
  expect(canDeletePost(admin)).toBe(true);
});
```

Keep fixtures small and close to the tests that use them. Huge shared fixtures make it hard to tell which field a test depends on.

## 142: How does Jest report slow tests?

Jest marks a test file as slow in the output when it takes longer than `slowTestThreshold` seconds (5 by default). With `--verbose`, each test shows its duration in milliseconds.

```js
module.exports = {
  slowTestThreshold: 2,
};
```

To find the slowest tests in a big suite, a JSON report (`--json --outputFile=report.json`) has timing for each file and test.

## 143: Can Jest work with ES modules?

Yes, in two ways:

1. **Through a transformer (most common)**: Babel, ts-jest or SWC turn `import`/`export` into CommonJS before Jest runs the code. This works well and supports `jest.mock` hoisting.
2. **Native ESM**: Jest can run real ES modules if you start Node with `--experimental-vm-modules`. This support is still marked experimental, and module mocking uses a different API (`jest.unstable_mockModule`).

```bash
node --experimental-vm-modules node_modules/jest/bin/jest.js
```

For most projects the transformer approach is the simpler choice.

## 144: Why use toHaveBeenCalledWith instead of checking mock.calls directly?

Both work. `toHaveBeenCalledWith` is shorter and gives a nicer error message that lists all actual calls and shows a diff. It also supports asymmetric matchers like `expect.any`.

`mock.calls` is useful when you need something the matchers can't express, like grabbing a callback that was passed in and calling it:

```js
test("calls the saved callback", () => {
  const subscribe = jest.fn();
  startListening(subscribe);

  const handler = subscribe.mock.calls[0][0];
  handler({ type: "ping" });

  // check what handler did...
});
```

## 145: Why should tests be deterministic?

A deterministic test gives the same result every time for the same code. If a test sometimes passes and sometimes fails (a flaky test), people stop trusting the suite and start ignoring failures, which means real bugs get missed.

Common sources of randomness are the current time, `Math.random`, real network calls, time zones, test order and timers. Control them with fake timers, mocks, fixed seeds and clean setup for each test.

## 146: How do you test a function that returns a function?

Call the outer function to get the inner one, then call that and check the result:

```js
function multiplier(factor) {
  return (value) => value * factor;
}

test("creates a doubling function", () => {
  const double = multiplier(2);
  expect(typeof double).toBe("function");
  expect(double(5)).toBe(10);
});
```

The same idea works for middleware, React hooks factories and other higher-order functions.

## 147: What do the negated asymmetric matchers do?

Jest has "not" versions of some asymmetric matchers that you can use inside `toEqual` or `toHaveBeenCalledWith`:

- `expect.not.objectContaining(obj)`
- `expect.not.arrayContaining(arr)`
- `expect.not.stringContaining(str)`
- `expect.not.stringMatching(regex)`

```js
test("does not send the password", () => {
  const send = jest.fn();
  send({ name: "Anna", email: "a@example.com" });

  expect(send).toHaveBeenCalledWith(
    expect.not.objectContaining({ password: expect.anything() }),
  );
});
```

## 148: How do you test getters and setters?

Just use them like normal properties. A setter test sets a value and then reads it back or checks the side effect:

```js
class Temperature {
  #celsius = 0;
  get fahrenheit() {
    return this.#celsius * 1.8 + 32;
  }
  set fahrenheit(value) {
    this.#celsius = (value - 32) / 1.8;
  }
}

test("converts between units", () => {
  const t = new Temperature();
  t.fahrenheit = 212;
  expect(t.fahrenheit).toBe(212);
});
```

To spy on a getter or setter of an object, use `jest.spyOn(obj, 'prop', 'get')` or `'set'`.

## 149: What should the first tests for a new function cover?

A simple checklist:

1. **The normal case**: typical input gives the expected output.
2. **Edge cases**: empty arrays, empty strings, zero, negative numbers, very large values, `null` or `undefined`.
3. **Error cases**: invalid input throws or returns an error the way it should.
4. **Boundaries**: the exact values where behavior changes, like `age === 18` for an "is adult" check.

```js
describe("isAdult", () => {
  test.each([
    [17, false],
    [18, true],
    [65, true],
  ])("isAdult(%i) is %s", (age, expected) => {
    expect(isAdult(age)).toBe(expected);
  });

  test("throws for negative ages", () => {
    expect(() => isAdult(-1)).toThrow();
  });
});
```

## 150: What are common mistakes beginners make with Jest?

- Forgetting to `await` or `return` a promise, so the test passes without checking anything.
- Using `toBe` to compare objects instead of `toEqual`.
- Calling the function inside `expect` when using `toThrow` instead of wrapping it in an arrow function.
- Not resetting mocks between tests, so call counts from one test leak into the next.
- Committing `test.only` or `test.skip`.
- Updating snapshots with `-u` without reading the diff.
- Mocking so much that the test only checks the mocks, not real behavior.
- Testing implementation details (private state, internal calls) instead of the result.

---

# Moderate Questions (151-300)

## 151: What is the difference between setupFiles and setupFilesAfterEnv?

Both run before each test file, but at different times:

- `setupFiles` runs right after the test environment is created, before the test framework is installed. `expect`, `test` and hooks are not available yet. Use it for things like environment variables, polyfills and global stubs.
- `setupFilesAfterEnv` runs after the test framework is installed. Use it for custom matchers, global `beforeEach`/`afterEach` hooks and libraries like `@testing-library/jest-dom`.

```js
module.exports = {
  setupFiles: ["<rootDir>/test/env.js"], // process.env.API_URL = '...'
  setupFilesAfterEnv: ["<rootDir>/test/setup.js"], // expect.extend(...), afterEach(...)
};
```

Both run once per test file, not once for the whole run. For once-per-run work, use `globalSetup`.

## 152: How do you partially mock a module with jest.requireActual?

Use a factory that spreads the real module and replaces only some exports:

```js
// utils.js
export const formatDate = (d) => d.toISOString().slice(0, 10);
export const generateId = () => Math.random().toString(36).slice(2);
```

```js
import { formatDate, generateId } from "./utils";

jest.mock("./utils", () => ({
  ...jest.requireActual("./utils"),
  generateId: jest.fn(() => "fixed-id"),
}));

test("only generateId is mocked", () => {
  expect(generateId()).toBe("fixed-id");
  expect(formatDate(new Date("2025-03-01"))).toBe("2025-03-01");
});
```

`jest.requireActual` loads the real module, ignoring any mock. Keep in mind that functions inside `utils.js` that call `generateId` still call the real one, because they use the local binding, not the mocked export.

## 153: How do you mock named and default exports at the same time?

Return both from the factory, and set `__esModule: true`:

```js
import api, { fetchUser } from "./api";

jest.mock("./api", () => ({
  __esModule: true,
  default: { baseUrl: "http://test" },
  fetchUser: jest.fn(),
}));

test("both exports are mocked", () => {
  expect(api.baseUrl).toBe("http://test");
  expect(jest.isMockFunction(fetchUser)).toBe(true);
});
```

If you use automatic mocking (`jest.mock('./api')` with no factory), Jest handles this for you and mocks every function, including the default export.

## 154: Why must variables used in a jest.mock factory start with "mock"?

Because `jest.mock` calls are hoisted above the imports. If the factory used a normal variable from the test file, that variable would not exist yet when the factory runs. To prevent this bug, `babel-plugin-jest-hoist` throws an error when a factory uses an outside variable:

```
The module factory of `jest.mock()` is not allowed to reference any out-of-scope variables.
```

Variables whose name starts with `mock` are allowed, as an escape hatch. It's your job to make sure they are only used lazily, inside a function that runs later:

```js
const mockSend = jest.fn();

jest.mock("./mailer", () => ({
  send: (...args) => mockSend(...args), // used lazily, so this is fine
}));
```

Using `mockSend` directly as the value (`send: mockSend`) can be `undefined` if the module is loaded before the variable is set, so wrapping it in a function is safer.

## 155: What is jest.doMock and when do you use it?

`jest.doMock` is like `jest.mock`, but it is not hoisted. It only affects modules that are required after it runs. That makes it useful when you need different mocks in different tests:

```js
beforeEach(() => {
  jest.resetModules();
});

test("uses the production URL", () => {
  jest.doMock("./config", () => ({ env: "production" }));
  const { getApiUrl } = require("./api");
  expect(getApiUrl()).toBe("https://api.example.com");
});

test("uses the local URL", () => {
  jest.doMock("./config", () => ({ env: "development" }));
  const { getApiUrl } = require("./api");
  expect(getApiUrl()).toBe("http://localhost:3000");
});
```

You need `require` (or dynamic `import`) after `doMock`, and `resetModules` so a cached copy of the module is not reused.

## 156: What do jest.resetModules and jest.isolateModules do?

- `jest.resetModules()` clears the module registry, so the next `require` loads a fresh copy of each module. Use it when a module keeps state (like a singleton or config read at import time) and you want a clean copy.
- `jest.isolateModules(fn)` gives the function its own registry. Modules required inside it don't share state with modules outside it.

```js
test("each copy has its own counter", () => {
  let counterA;
  let counterB;

  jest.isolateModules(() => {
    counterA = require("./counter");
  });
  jest.isolateModules(() => {
    counterB = require("./counter");
  });

  counterA.increment();
  expect(counterB.value()).toBe(0);
});
```

`jest.isolateModulesAsync` is the version for async callbacks.

## 157: How do you test code that reads process.env?

Change `process.env` in the test and restore it afterwards. If the module reads the variable at import time, you also need a fresh copy of the module:

```js
const ORIGINAL_ENV = process.env;

beforeEach(() => {
  jest.resetModules();
  process.env = { ...ORIGINAL_ENV };
});

afterAll(() => {
  process.env = ORIGINAL_ENV;
});

test("uses the port from the environment", () => {
  process.env.PORT = "8080";
  const config = require("./config");
  expect(config.port).toBe(8080);
});
```

`jest.replaceProperty(process, 'env', { ...process.env, PORT: '8080' })` is another option that is undone by `restoreAllMocks`.

## 158: How do you mock a package from node_modules?

Three common ways:

1. `jest.mock('package-name')` in the test file, with or without a factory.
2. A manual mock in a `__mocks__` folder next to `node_modules` (in a `roots` folder). For scoped packages, use a subfolder: `__mocks__/@scope/package.js`. These mocks are used automatically in every test.
3. `moduleNameMapper` to point the package to a stub file.

```js
// __mocks__/uuid.js
module.exports = {
  v4: jest.fn(() => "00000000-0000-0000-0000-000000000000"),
};
```

To use the real package in one test while the manual mock exists, call `jest.unmock('uuid')` or use `jest.requireActual('uuid')`.

## 159: How do you mock Node core modules like fs?

Core modules are never mocked automatically, even with a `__mocks__/fs.js` file. You must call `jest.mock` explicitly:

```js
const fs = require("fs");
const { readConfig } = require("./readConfig");

jest.mock("fs");

test("parses the config file", () => {
  fs.readFileSync.mockReturnValue('{"port": 3000}');
  expect(readConfig("app.json")).toEqual({ port: 3000 });
});
```

For `node:` imports, use the same specifier the code uses (`jest.mock('node:fs')`). For code that does a lot of file work, a fake file system like `memfs`, or writing to a temp folder, is often more realistic than mocking each call.

## 160: How do you mock axios?

The simplest way is `jest.mock('axios')` and setting return values per test:

```js
import axios from "axios";
import { getUser } from "./userApi";

jest.mock("axios");

test("returns the user data", async () => {
  axios.get.mockResolvedValue({ data: { id: 1, name: "Anna" } });

  await expect(getUser(1)).resolves.toEqual({ id: 1, name: "Anna" });
  expect(axios.get).toHaveBeenCalledWith("/users/1");
});
```

If your code uses `axios.create()`, the instance is a different object, so you have to mock `create` to return an object with mocked methods. Many teams avoid this by mocking at the network level with MSW or nock instead, which also works if you later replace axios with `fetch`.

## 161: How do you mock a class with jest.mock?

Automatic mocking replaces the class with a mock constructor, and all its methods with mock functions that return `undefined`:

```js
import { EmailClient } from "./EmailClient";
import { notifyUser } from "./notifyUser";

jest.mock("./EmailClient");

test("sends a welcome email", () => {
  notifyUser({ email: "a@example.com" });

  expect(EmailClient).toHaveBeenCalledTimes(1);
  const instance = EmailClient.mock.instances[0];
  expect(instance.send).toHaveBeenCalledWith("a@example.com", "Welcome!");
});
```

To control the methods, use a factory or `mockImplementation`:

```js
const mockSend = jest.fn().mockResolvedValue("ok");
jest.mock("./EmailClient", () => ({
  EmailClient: jest.fn().mockImplementation(() => ({ send: mockSend })),
}));
```

Note that methods are only on `mock.instances` when the class is automocked. With a factory that returns a plain object, check `mockSend` directly.

## 162: How do you mock one method of a class?

Spy on the prototype. Every instance, including ones created inside the code you test, uses the spy:

```js
import { PaymentGateway } from "./PaymentGateway";
import { checkout } from "./checkout";

test("charges the card", async () => {
  const charge = jest
    .spyOn(PaymentGateway.prototype, "charge")
    .mockResolvedValue({ status: "paid" });

  await checkout({ total: 50 });

  expect(charge).toHaveBeenCalledWith(50);
  charge.mockRestore();
});
```

This does not work for methods defined as arrow function class fields (`charge = () => {}`), because those live on each instance, not the prototype.

## 163: How do you spy on a getter or a setter?

Pass `'get'` or `'set'` as the third argument to `jest.spyOn`:

```js
const settings = {
  get theme() {
    return "light";
  },
};

test("mocks a getter", () => {
  const spy = jest.spyOn(settings, "theme", "get").mockReturnValue("dark");

  expect(settings.theme).toBe("dark");
  expect(spy).toHaveBeenCalled();
  spy.mockRestore();
});
```

The property must be defined as a getter or setter on the object (or its prototype), and it must be configurable.

## 164: What is jest.replaceProperty?

It replaces a non-function property on an object for the test, and can be restored like a spy:

```js
const config = { featureFlag: false };

test("runs with the flag on", () => {
  const replaced = jest.replaceProperty(config, "featureFlag", true);
  expect(config.featureFlag).toBe(true);

  replaced.restore();
  expect(config.featureFlag).toBe(false);
});
```

`jest.restoreAllMocks()` and `restoreMocks: true` also restore replaced properties. It throws if the property does not exist, and it throws for functions, telling you to use `jest.spyOn` instead.

## 165: How does the using keyword work with jest.spyOn in Jest 30?

Jest 30 mocks support JavaScript's explicit resource management (`Symbol.dispose`). If you create a spy with `using`, it is restored automatically when the block ends:

```js
test("logs a warning", () => {
  using warn = jest.spyOn(console, "warn").mockImplementation(() => {});

  doSomethingDeprecated();
  expect(warn).toHaveBeenCalled();
}); // console.warn is restored here
```

Your code has to get through the transform step first. The default `babel-jest` setup fails with a syntax error on `using` unless you add the Babel plugin for explicit resource management. TypeScript 5.2+ (with ts-jest) understands it, and Node 24 runs it natively if the file is not transformed. It is a nice way to avoid forgetting `mockRestore()`, especially when a spy is only needed in part of a test.

## 166: What is mockFn.withImplementation?

It replaces a mock's implementation only while a callback runs, then restores the previous one:

```js
test("withImplementation", () => {
  const getPrice = jest.fn(() => 10);

  getPrice.withImplementation(
    () => 99,
    () => {
      expect(getPrice()).toBe(99);
    },
  );

  expect(getPrice()).toBe(10);
});
```

If the callback is async, `withImplementation` returns a promise you need to `await`. It is cleaner than setting and resetting an implementation by hand.

## 167: How do you type mocks in TypeScript?

Common options:

```ts
import { jest } from "@jest/globals";
import * as api from "./api";
import type { UserService } from "./UserService";

jest.mock("./api");

// 1. jest.mocked for imported modules
const mockedApi = jest.mocked(api);
mockedApi.fetchUser.mockResolvedValue({ id: 1, name: "Anna" });

// 2. jest.fn with the function type
const onSave = jest.fn<(id: number) => Promise<void>>();

// 3. jest.Mocked<T> for an object of mocks
const userService: jest.Mocked<UserService> = {
  find: jest.fn(),
  save: jest.fn(),
};
```

With `@jest/globals`, types like `jest.Mocked` and `jest.MockedFunction` are available on the imported `jest`. Typed mocks catch mistakes like returning the wrong shape from `mockResolvedValue`. For objects with many methods, `jest-mock-extended` can create typed mocks automatically.

## 168: What is jest.createMockFromModule?

It loads a module, generates an automatic mock from it and returns that mock, without registering it. It is mostly used inside manual mocks to start from the automock and then change a few parts:

```js
// __mocks__/fileStore.js
const fileStore = jest.createMockFromModule("../fileStore");

fileStore.read = jest.fn(() => "fake content");

module.exports = fileStore;
```

It replaced `jest.genMockFromModule`, which was removed in Jest 30.

## 169: How do you test timers that are mixed with promises?

`jest.advanceTimersByTime` runs timer callbacks, but it doesn't wait for promises created inside them. Use the async versions, which also let pending promises settle:

```js
async function waitAndFetch(fetchData) {
  await new Promise((resolve) => setTimeout(resolve, 1000));
  return fetchData();
}

test("fetches after one second", async () => {
  jest.useFakeTimers();
  const fetchData = jest.fn().mockResolvedValue("data");

  const promise = waitAndFetch(fetchData);
  await jest.advanceTimersByTimeAsync(1000);

  await expect(promise).resolves.toBe("data");
  jest.useRealTimers();
});
```

There are also `runAllTimersAsync`, `runOnlyPendingTimersAsync` and `advanceTimersToNextTimerAsync`.

## 170: How do you test a debounce function?

Use fake timers, call the function several times, and check it runs only once after the delay:

```js
function debounce(fn, ms) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

test("calls the function once after the last call", () => {
  jest.useFakeTimers();
  const search = jest.fn();
  const debouncedSearch = debounce(search, 300);

  debouncedSearch("a");
  debouncedSearch("ab");
  debouncedSearch("abc");

  jest.advanceTimersByTime(299);
  expect(search).not.toHaveBeenCalled();

  jest.advanceTimersByTime(1);
  expect(search).toHaveBeenCalledTimes(1);
  expect(search).toHaveBeenCalledWith("abc");

  jest.useRealTimers();
});
```

Checking at 299 ms and then at 300 ms makes sure the delay is exact.

## 171: What does jest.runOnlyPendingTimers do?

It runs only the timers that are pending right now. Timers created while running them are left for later. This is what you need for code that reschedules itself, where `runAllTimers` would loop until it hits the limit:

```js
function startHeartbeat(ping) {
  function beat() {
    ping();
    setTimeout(beat, 5000);
  }
  setTimeout(beat, 5000);
}

test("pings once per tick", () => {
  jest.useFakeTimers();
  const ping = jest.fn();
  startHeartbeat(ping);

  jest.runOnlyPendingTimers();
  expect(ping).toHaveBeenCalledTimes(1);

  jest.runOnlyPendingTimers();
  expect(ping).toHaveBeenCalledTimes(2);

  jest.useRealTimers();
});
```

## 172: What does the doNotFake option do?

It tells Jest which APIs to leave real when fake timers are on:

```js
jest.useFakeTimers({
  doNotFake: ["nextTick", "queueMicrotask"],
});
```

The list can include `Date`, `hrtime`, `nextTick`, `performance`, `queueMicrotask`, `requestAnimationFrame`, `cancelAnimationFrame`, `requestIdleCallback`, `cancelIdleCallback`, `setImmediate`, `clearImmediate`, `setInterval`, `clearInterval`, `setTimeout` and `clearTimeout`.

This helps with libraries that break when `nextTick` or `queueMicrotask` are faked, like some database drivers. You can also set it globally with `fakeTimers: { enableGlobally: true, doNotFake: [...] }`.

## 173: What does the advanceTimers option of useFakeTimers do?

With `advanceTimers: true`, fake time moves forward automatically along with real time. With a number, fake time moves that many milliseconds for every real millisecond:

```js
jest.useFakeTimers({ advanceTimers: true });
```

This is useful when you can't call `advanceTimersByTime` yourself, for example with `@testing-library/user-event`, which uses timers internally. You still keep the ability to jump ahead with `advanceTimersByTime` when you need to.

## 174: What is the difference between setSystemTime, jest.now and getRealSystemTime?

All of these only matter when fake timers are on:

- `jest.setSystemTime(date)` changes the fake current time (what `Date.now()` and `new Date()` return). It does not run any timers.
- `jest.now()` returns the current fake time in milliseconds.
- `jest.getRealSystemTime()` returns the real time from the system, ignoring the fake clock.

```js
test("system time", () => {
  jest.useFakeTimers();
  jest.setSystemTime(new Date("2030-01-01T00:00:00Z"));

  expect(Date.now()).toBe(new Date("2030-01-01T00:00:00Z").getTime());
  expect(jest.getRealSystemTime()).toBeLessThan(Date.now());

  jest.useRealTimers();
});
```

Moving the clock with `setSystemTime` does not fire timers that would have fired in between. Use `advanceTimersByTime` for that.

## 175: How do you mock localStorage?

jsdom already has a working `localStorage`, so often you don't need a mock at all. Just clear it between tests:

```js
afterEach(() => {
  localStorage.clear();
});

test("saves the theme", () => {
  saveTheme("dark");
  expect(localStorage.getItem("theme")).toBe("dark");
});
```

If you need to spy on calls or force an error (like a full storage), spy on the prototype, since `localStorage` methods come from `Storage.prototype`:

```js
test("handles a full storage", () => {
  jest.spyOn(Storage.prototype, "setItem").mockImplementation(() => {
    throw new DOMException("Quota exceeded", "QuotaExceededError");
  });

  expect(() => saveTheme("dark")).not.toThrow();
});
```

## 176: How do you mock window.matchMedia?

jsdom does not implement `matchMedia`, so code that uses it crashes with "window.matchMedia is not a function". Add a mock in a setup file:

```js
// jest.setup.js
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: jest.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    addListener: jest.fn(), // old API
    removeListener: jest.fn(), // old API
    dispatchEvent: jest.fn(),
  })),
});
```

In a test that needs a match, override it: `window.matchMedia.mockImplementation((q) => ({ ...base, matches: q === '(max-width: 600px)' }))`.

## 177: How do you mock IntersectionObserver and ResizeObserver?

jsdom has neither. A simple mock class in a setup file stops the crashes:

```js
// jest.setup.js
class MockIntersectionObserver {
  constructor(callback) {
    this.callback = callback;
  }
  observe = jest.fn();
  unobserve = jest.fn();
  disconnect = jest.fn();
  takeRecords = jest.fn(() => []);
}

window.IntersectionObserver = MockIntersectionObserver;
window.ResizeObserver = class {
  observe = jest.fn();
  unobserve = jest.fn();
  disconnect = jest.fn();
};
```

To test behavior like lazy loading, keep a reference to the callback and call it yourself with fake entries: `observer.callback([{ isIntersecting: true, target: element }])`.

## 178: How do you handle window.location in jsdom?

In recent jsdom versions (used by Jest 30), `window.location` and its methods can't be replaced. `Object.defineProperty(window, 'location', ...)` throws "Cannot redefine property", `jest.spyOn(window.location, 'assign')` throws, and `delete window.location` silently does nothing.

What works:

- For reading the URL, change it with the History API:

  ```js
  window.history.pushState({}, "", "/orders?id=5");
  expect(window.location.search).toBe("?id=5");
  ```

- For the starting URL, set `testEnvironmentOptions: { url: 'https://example.com/app' }`.
- For navigation like `location.assign(url)` or `location.reload()`, wrap it in your own small module (`navigation.js`) and mock that module in tests.

The wrapper approach is the most stable because it doesn't depend on jsdom details.

## 179: How do you set the URL for jsdom tests?

Use `testEnvironmentOptions.url` in the config. The default is `http://localhost/`:

```js
module.exports = {
  testEnvironment: "jsdom",
  testEnvironmentOptions: {
    url: "https://shop.example.com/",
  },
};
```

This affects `window.location`, `document.URL`, relative URL resolution, and the origin used for `localStorage` and cookies. Inside a test you can change the path with `history.pushState` or `history.replaceState`.

## 180: How do you check the order of calls between different mocks?

Each mock records a global call number in `mock.invocationCallOrder`. Compare those numbers:

```js
test("opens the connection before querying", async () => {
  const connect = jest.fn();
  const query = jest.fn();

  await runReport({ connect, query });

  expect(connect.mock.invocationCallOrder[0]).toBeLessThan(
    query.mock.invocationCallOrder[0],
  );
});
```

Another way is to have both mocks push to a shared array and check the array: `expect(events).toEqual(['connect', 'query'])`. That is often easier to read.

## 181: How do you write a custom matcher?

Use `expect.extend`. A matcher returns an object with `pass` and a `message` function:

```js
expect.extend({
  toBeWithinRange(received, floor, ceiling) {
    const pass = received >= floor && received <= ceiling;
    return {
      pass,
      message: () =>
        `expected ${this.utils.printReceived(received)} ${
          pass ? "not " : ""
        }to be within range ${floor} - ${ceiling}`,
    };
  },
});

test("custom matcher", () => {
  expect(5).toBeWithinRange(1, 10);
  expect(50).not.toBeWithinRange(1, 10);
});
```

The message is used when the check fails, so write it for both the normal and the `.not` case. Put `expect.extend` in a `setupFilesAfterEnv` file to use the matcher everywhere.

## 182: How do you add TypeScript types for a custom matcher?

Use declaration merging. With `@jest/globals`, extend the `Matchers` interface of the `expect` package:

```ts
// jest.d.ts
import "expect";

declare module "expect" {
  interface AsymmetricMatchers {
    toBeWithinRange(floor: number, ceiling: number): void;
  }
  interface Matchers<R> {
    toBeWithinRange(floor: number, ceiling: number): R;
  }
}
```

With `@types/jest`, extend the global namespace instead:

```ts
declare global {
  namespace jest {
    interface Matchers<R> {
      toBeWithinRange(floor: number, ceiling: number): R;
    }
  }
}
export {};
```

Make sure the file is included by your `tsconfig.json`.

## 183: Can custom matchers be used as asymmetric matchers?

Yes. Every matcher added with `expect.extend` is also available on `expect` itself, as an asymmetric matcher:

```js
test("asymmetric custom matcher", () => {
  expect({ age: 30, name: "Anna" }).toEqual({
    age: expect.toBeWithinRange(18, 65),
    name: expect.any(String),
  });
});
```

This lets you reuse one check both as a normal assertion and inside objects or `toHaveBeenCalledWith`. For TypeScript, add it to the `AsymmetricMatchers` interface too.

## 184: What is jest-extended?

It is a community library with many extra matchers, like `toBeArray`, `toBeEmpty`, `toIncludeAllMembers`, `toHaveBeenCalledOnce`, `toBeAfter`, `toStartWith` and `toSatisfy`.

```js
// jest.setup.js (setupFilesAfterEnv)
const matchers = require("jest-extended");
expect.extend(matchers);
```

```js
test("jest-extended", () => {
  expect([3, 1, 2]).toIncludeSameMembers([1, 2, 3]);
  expect("jest testing").toStartWith("jest");
});
```

It saves you from writing small helpers, but adds a dependency and matchers that new team members may not know.

## 185: When do you use toMatchObject and when expect.objectContaining?

They check similar things (an object has at least these properties), but in different places:

- `toMatchObject` is a matcher. You use it directly: `expect(user).toMatchObject({ name: 'Anna' })`.
- `expect.objectContaining` is an asymmetric matcher. You use it inside other checks, like `toHaveBeenCalledWith` or nested in `toEqual`.

There is one difference in how they treat nested objects. `toMatchObject` applies the "subset" rule all the way down, so nested objects can have extra properties too. `objectContaining` checks each listed property with normal equality, so nested objects must match exactly unless you nest another `objectContaining`.

## 186: What are property matchers in snapshots?

They let you snapshot an object that has fields that change on every run, like ids and dates. You pass asymmetric matchers as the first argument, and those fields are checked by type instead of value:

```js
test("creates a user", () => {
  const user = createUser({ name: "Anna" });

  expect(user).toMatchSnapshot({
    id: expect.any(String),
    createdAt: expect.any(Date),
  });
});
```

The snapshot file stores `Any<String>` and `Any<Date>` for those fields, so the test stays stable.

## 187: What is a snapshot serializer?

A serializer controls how a value is turned into text in a snapshot. You can add one to hide noise (like random ids or long timestamps) or to print a custom type in a readable way:

```js
// test/dateSerializer.js
module.exports = {
  test: (value) => value instanceof Date,
  serialize: (value) => `Date<${value.toISOString().slice(0, 10)}>`,
};
```

```js
// jest.config.js
module.exports = {
  snapshotSerializers: ["<rootDir>/test/dateSerializer.js"],
};
```

You can also add one in a single file with `expect.addSnapshotSerializer(serializer)`. Libraries like `@emotion/jest` ship serializers for their own objects.

## 188: When are snapshots a bad idea?

- When the snapshot is huge. Nobody reviews a 500-line diff, so changes get accepted blindly.
- When the output changes often for unimportant reasons (class names, ids, timestamps). The test becomes noise.
- When you are checking a specific behavior. `expect(total).toBe(90)` says what matters; a snapshot of the whole page does not.
- When the snapshot is created before the code is correct. It just locks in the bug.

Snapshots work best for small, stable outputs where any change is worth a look, like an error message, a serialized config or a small component's markup.

## 189: What are obsolete snapshots and how do you remove them?

A snapshot is obsolete when no test uses it anymore, for example after you rename or delete a test. Jest reports them at the end of the run:

```
1 snapshot obsolete from 1 test suite. To remove it, run `npm test -- -u`.
```

Run with `-u` to delete them. Obsolete snapshots also make Jest exit with code `1`, even when all tests pass, so CI will catch leftovers.

## 190: How do you snapshot an error message?

Use `toThrowErrorMatchingSnapshot` or `toThrowErrorMatchingInlineSnapshot`. They save the message of the thrown error:

```js
test("rejects an invalid email", () => {
  expect(() => validateEmail("nope")).toThrowErrorMatchingInlineSnapshot(
    `"Invalid email: nope"`,
  );
});

test("async version", async () => {
  await expect(
    signup({ email: "nope" }),
  ).rejects.toThrowErrorMatchingSnapshot();
});
```

This works well for long error messages, like validation errors that list many fields.

## 191: What is coverageThreshold?

It makes Jest fail when coverage drops below a minimum. You can set it globally, per folder, per file or with a glob:

```js
module.exports = {
  collectCoverage: true,
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 85,
      statements: 85,
    },
    "./src/payments/": {
      branches: 95,
    },
  },
};
```

A positive number is a minimum percent. A negative number is the maximum count of uncovered items allowed, like `statements: -10`. Set the threshold close to your current coverage and raise it over time, so it stops coverage from going down without forcing pointless tests.

## 192: What does collectCoverageFrom do?

By default Jest only reports coverage for files that were loaded by at least one test. Files that no test imports don't show up at all, so the numbers look better than they are.

`collectCoverageFrom` lists the files that should always be included, with glob patterns:

```js
module.exports = {
  collectCoverageFrom: [
    "src/**/*.{js,ts,tsx}",
    "!src/**/*.d.ts",
    "!src/**/index.ts",
    "!src/**/*.stories.tsx",
  ],
};
```

Patterns starting with `!` exclude files. With this option, untested files show up with 0% coverage.

## 193: What is the difference between the babel and v8 coverage providers?

- `babel` (the default) uses Istanbul. It adds counters to your code during the transform step, then counts what ran. It is very accurate and well tested, but it makes tests a bit slower and only covers code that goes through Babel.
- `v8` uses the coverage data built into the V8 engine, and does not change your code. It is usually faster and works with any transformer, but the results can be a little different from Istanbul, especially for branches.

```js
module.exports = {
  coverageProvider: "v8",
};
```

If you switch providers, expect the numbers to move a bit and adjust thresholds.

## 194: What does coverageReporters control?

It sets the formats of the coverage report. The default is `['clover', 'json', 'lcov', 'text']`:

- `text`: the table printed in the terminal.
- `text-summary`: a short summary instead of the full table.
- `lcov`: an `lcov.info` file plus an HTML report. Most coverage services (Codecov, Coveralls, SonarQube) read `lcov.info`.
- `json` / `json-summary`: machine-readable data.
- `html`: just the HTML report.
- `cobertura`: XML used by tools like Azure DevOps and GitLab.

```js
module.exports = {
  coverageReporters: ["text-summary", "lcov"],
};
```

## 195: How do you exclude code from coverage?

- To exclude whole files or folders, use `coveragePathIgnorePatterns` (regex) or `!` patterns in `collectCoverageFrom`.
- To exclude a few lines, use comments. With the `babel` provider, Istanbul comments work:

  ```js
  /* istanbul ignore next */
  function debugOnly() {
    console.log(state);
  }

  /* istanbul ignore else */
  if (isBrowser) {
    attach();
  }
  ```

- With the `v8` provider, use `/* c8 ignore next */` or `/* c8 ignore start */ ... /* c8 ignore stop */`.

Use these rarely and for a reason, like debug-only code or a branch that can't happen in tests. Ignoring code just to reach a number defeats the purpose.

## 196: What is test.concurrent?

`test.concurrent` starts the test without waiting for the previous one to finish, so async tests in the same file run at the same time:

```js
test.concurrent("fetches users", async () => {
  const users = await fetchUsers();
  expect(users.length).toBeGreaterThan(0);
});

test.concurrent("fetches orders", async () => {
  const orders = await fetchOrders();
  expect(orders.length).toBeGreaterThan(0);
});
```

The `maxConcurrency` option (default 5) limits how many run at once. It only helps when tests spend most of their time waiting on I/O. Concurrent tests must not share state, and `beforeEach`/`afterEach` hooks don't give each concurrent test its own clean setup the way they do for normal tests, so don't rely on them here. The feature is still marked experimental in the docs.

## 197: What is test.failing?

`test.failing` marks a test that you expect to fail. If it fails, Jest reports it as passed. If it starts passing, Jest reports it as failed, so you know to remove the marker.

```js
test.failing("rounds half up (known bug #123)", () => {
  expect(roundPrice(2.345)).toBe(2.35);
});
```

It is useful for writing a test for a known bug before fixing it. There are also `test.only.failing` and `test.skip.failing`. It only works with the default `jest-circus` runner.

## 198: How do you use test.each with a tagged template?

Write a table where the first row is the column names and each `${}` is a value. The test gets an object:

```js
test.each`
  a    | b    | expected
  ${1} | ${1} | ${2}
  ${1} | ${2} | ${3}
  ${2} | ${1} | ${3}
`("returns $expected when $a is added to $b", ({ a, b, expected }) => {
  expect(a + b).toBe(expected);
});
```

The table style is easy to read when there are several inputs. You use `$name` in the title to insert a value, and `$name.path` for nested properties.

## 199: What placeholders can you use in test.each titles?

With array rows, values are inserted in order:

- `%s` string, `%d` number, `%i` integer, `%f` float
- `%j` JSON, `%o` object, `%p` pretty-format (good for objects and arrays)
- `%#` index of the row (starting at 0)
- `%$` number of the test case (starting at 1)
- `%%` a literal percent sign

With object rows (or tagged templates), use `$property` and `$property.nested`:

```js
test.each([
  { input: "Hello", expected: "hello" },
  { input: "WORLD", expected: "world" },
])("lowercases $input to $expected", ({ input, expected }) => {
  expect(input.toLowerCase()).toBe(expected);
});
```

Object rows are often better than arrays because the test reads clearly and adding a field doesn't shift the others.

## 200: What is the projects option?

`projects` lets one Jest run handle several configurations at once. Each project has its own settings, like test environment, transforms and setup files:

```js
module.exports = {
  projects: [
    {
      displayName: "server",
      testEnvironment: "node",
      testMatch: ["<rootDir>/server/**/*.test.ts"],
    },
    {
      displayName: "client",
      testEnvironment: "jsdom",
      testMatch: ["<rootDir>/client/**/*.test.tsx"],
      setupFilesAfterEnv: ["<rootDir>/client/jest.setup.ts"],
    },
  ],
};
```

You can also list paths to other config files: `projects: ['<rootDir>/packages/*']`. Jest runs all projects in one process pool and prints one combined report, which is handy in monorepos.

## 201: How do you map TypeScript path aliases in Jest?

Jest doesn't read `paths` from `tsconfig.json`. If your code imports `@/utils/date`, you need a matching `moduleNameMapper`:

```json
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```

```js
// jest.config.js
module.exports = {
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1",
  },
};
```

With `ts-jest`, the `pathsToModuleNameMapper` helper can build this from your tsconfig so you don't have to keep both in sync by hand.

## 202: What is moduleDirectories?

It is the list of folder names Jest searches when you import a bare module name (not a relative path). The default is `['node_modules']`.

```js
module.exports = {
  moduleDirectories: ["node_modules", "<rootDir>/src"],
};
```

With this, `import Button from 'components/Button'` resolves to `src/components/Button`. It must match what your bundler does, or the code will work in tests but not in the app (or the other way around).

## 203: What does the transform option do?

`transform` maps file patterns to transformers, which turn the source into code Jest can run:

```js
module.exports = {
  transform: {
    "^.+\\.(t|j)sx?$": "@swc/jest",
    "^.+\\.svg$": "<rootDir>/test/svgTransform.js",
  },
};
```

If you set `transform`, the default `babel-jest` rule is replaced. If you still want Babel for JS files, add it explicitly: `'^.+\\.jsx?$': 'babel-jest'`. Transformed files are cached, so the cost is mostly on the first run.

## 204: Why does Jest fail with "Cannot use import statement outside a module" for a package in node_modules?

Jest does not transform files in `node_modules` by default (`transformIgnorePatterns` is `['/node_modules/', '\\.pnp\\.[^\\/]+$']`). If a package only ships ES modules, Node gets `import` syntax in a CommonJS context and crashes.

The fix is to let Jest transform that package:

```js
module.exports = {
  transformIgnorePatterns: ["/node_modules/(?!(nanoid|lodash-es|uuid)/)"],
};
```

The regex means "ignore everything in node_modules except these packages". With pnpm the path looks like `node_modules/.pnpm/nanoid@5.0.0/node_modules/nanoid`, so the pattern may need `.pnpm/` handling. Other options are mapping the package to a CommonJS build with `moduleNameMapper`, or mocking it.

## 205: What is testEnvironmentOptions?

It passes options to the test environment. What is allowed depends on the environment. For `jsdom`:

```js
module.exports = {
  testEnvironment: "jsdom",
  testEnvironmentOptions: {
    url: "https://example.com/",
    userAgent: "Mozilla/5.0 (test)",
    customExportConditions: [""],
  },
};
```

- `url` sets the page URL.
- `customExportConditions` controls which `exports` conditions are used when resolving packages. jsdom uses `['browser']` by default, which makes some packages load their browser build. Setting it to `['']` or `['node', 'node-addons']` makes them load the Node build.
- `globalsCleanup` (Jest 30) controls how Jest cleans globals between test files (`'soft'` by default, or `'on'` / `'off'`).

## 206: What are globalSetup and globalTeardown?

They are modules that run once for the whole test run, not once per file. `globalSetup` runs before any test file and `globalTeardown` runs after all of them:

```js
// jest.config.js
module.exports = {
  globalSetup: "<rootDir>/test/globalSetup.js",
  globalTeardown: "<rootDir>/test/globalTeardown.js",
};
```

```js
// test/globalSetup.js
module.exports = async function () {
  globalThis.__DB__ = await startTestDatabase();
  process.env.DATABASE_URL = globalThis.__DB__.url;
};
```

```js
// test/globalTeardown.js
module.exports = async function () {
  await globalThis.__DB__.stop();
};
```

They are a good place to start Docker containers, seed data or build something once. They run in the main process, outside the test sandbox, so `jest.fn()` and `expect` are not available there.

## 207: How do you share values from globalSetup with tests?

Variables set on `globalThis` in `globalSetup` are only visible in `globalTeardown`, not in tests, because tests run in separate sandboxes (often in other processes). To pass data to tests:

- Set `process.env` values. Worker processes inherit the environment of the main process.
- Write to a temp file (for example a JSON file with connection details) and read it in a setup file or test.

```js
// globalSetup.js
module.exports = async function () {
  const db = await startTestDatabase();
  process.env.DATABASE_URL = db.url;
  globalThis.__DB__ = db; // only for globalTeardown
};
```

Only send simple strings this way. Objects like a database client can't be shared between processes; each test file has to create its own connection.

## 208: How do you set up Jest for a React project?

The usual pieces:

```bash
npm install --save-dev jest jest-environment-jsdom @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

```js
// jest.config.js
module.exports = {
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
  moduleNameMapper: {
    "\\.(css|scss)$": "identity-obj-proxy",
  },
};
```

```js
// jest.setup.js
import "@testing-library/jest-dom";
```

You also need a transformer for JSX: `babel-jest` with `@babel/preset-env` and `@babel/preset-react` (plus `@babel/preset-typescript` for TS), or `ts-jest`/`@swc/jest`. Frameworks often have their own preset, like `next/jest` for Next.js.

## 209: How do you test a custom React hook?

Use `renderHook` from React Testing Library. It renders a tiny component that calls the hook and gives you the result:

```jsx
import { renderHook, act } from "@testing-library/react";
import { useCounter } from "./useCounter";

test("increments the counter", () => {
  const { result } = renderHook(() => useCounter(5));

  act(() => {
    result.current.increment();
  });

  expect(result.current.count).toBe(6);
});
```

Wrap state updates in `act`. For hooks that need context (like a theme or a query client), pass a `wrapper` option with the provider. `renderHook` used to come from `@testing-library/react-hooks`, which is now deprecated.

## 210: How do you test an Express API with supertest?

Export the app without calling `listen`, and pass it to `supertest`. It starts the server on a random port for each request:

```js
// app.js
const express = require("express");
const app = express();
app.use(express.json());

app.post("/users", (req, res) => {
  if (!req.body.name)
    return res.status(400).json({ error: "name is required" });
  res.status(201).json({ id: 1, name: req.body.name });
});

module.exports = app;
```

```js
// app.test.js
const request = require("supertest");
const app = require("./app");

test("creates a user", async () => {
  const res = await request(app).post("/users").send({ name: "Anna" });

  expect(res.status).toBe(201);
  expect(res.body).toEqual({ id: 1, name: "Anna" });
});

test("validates the name", async () => {
  const res = await request(app).post("/users").send({});
  expect(res.status).toBe(400);
});
```

Keeping `app.listen()` in a separate `server.js` file means tests never leave a server running.

## 211: How do you test code that talks to a database?

There are a few levels:

1. **Mock the data layer** (repository or model) in unit tests. Fast, but doesn't catch query bugs.
2. **Use an in-memory or lightweight version**, like SQLite or `mongodb-memory-server`. Faster than a real server, but may behave a bit differently.
3. **Use the real database in a container** (Docker or Testcontainers) started in `globalSetup`. Slowest, but closest to production.

For levels 2 and 3, keep tests independent:

- Clean tables in `beforeEach`, or run each test in a transaction and roll it back.
- When files run in parallel, give each worker its own database or schema (for example using `process.env.JEST_WORKER_ID`), or run DB tests with `--runInBand`.
- Close connections in `afterAll`, or Jest won't exit.

## 212: How do you test with an in-memory MongoDB?

`mongodb-memory-server` downloads and runs a real `mongod` binary in a temp folder, so you don't need MongoDB installed:

```js
const { MongoMemoryServer } = require("mongodb-memory-server");
const mongoose = require("mongoose");
const User = require("./User");

let mongo;

beforeAll(async () => {
  mongo = await MongoMemoryServer.create();
  await mongoose.connect(mongo.getUri());
});

afterEach(async () => {
  await mongoose.connection.db.dropDatabase();
});

afterAll(async () => {
  await mongoose.disconnect();
  await mongo.stop();
});

test("saves a user", async () => {
  await User.create({ name: "Anna" });
  expect(await User.countDocuments()).toBe(1);
});
```

The first run downloads the binary, which can be slow in CI. Cache it, or start one server in `globalSetup` and share its URI through `process.env`.

## 213: How do you debug a Jest test?

Options from simple to more powerful:

- Add `console.log` and run only that test with `-t`.
- Run Node's debugger and attach Chrome DevTools (`chrome://inspect`) or your editor:

  ```bash
  node --inspect-brk node_modules/.bin/jest --runInBand path/to/file.test.js
  ```

- In VS Code, open a "JavaScript Debug Terminal" and run `npx jest file.test.js`. Breakpoints in your code and tests just work.
- Put a `debugger;` statement in the code to stop there.

`--runInBand` is important when debugging, because by default tests run in worker processes that the debugger isn't attached to. Also increase the timeout or the test will fail while you are paused.

## 214: When do you use --runInBand?

`--runInBand` (`-i`) runs all test files one after another in the main process, without workers. Use it when:

- Debugging, so the debugger is attached to the process that runs tests.
- Tests share an external resource (one database, one port) and can't run in parallel.
- The CI machine has very few CPUs and workers only add overhead.
- You want to rule out parallelism as the cause of a flaky test.

For most suites on a normal machine, parallel workers are faster.

## 215: What does --detectOpenHandles do?

It makes Jest track async resources (timers, sockets, servers, file handles) that are still open after tests finish, and print where each one was created:

```
Jest has detected the following 1 open handle potentially keeping Jest from exiting:

  ●  TCPSERVERWRAP

      3 | const app = require('./app');
    > 4 | app.listen(3000);
```

It slows tests down, so use it to find the problem, not all the time. It also implies `--runInBand`.

## 216: How do you fix "Jest did not exit one second after the test run has completed"?

This warning means something is still keeping Node's event loop busy after all tests are done. Common causes:

- A database or Redis connection that was never closed.
- A server started with `listen()` and never closed.
- A `setInterval` or long `setTimeout` that was never cleared.
- A file watcher or message queue consumer still running.

Steps to fix it:

1. Run `npx jest --detectOpenHandles` to see where the handle came from.
2. Close the resource in `afterAll`: `await db.close()`, `server.close()`, `clearInterval(id)`.
3. For timers in app code, use `.unref()` on Node timers that shouldn't keep the process alive.

## 217: What does --forceExit do and why should you avoid it?

`--forceExit` makes Jest kill the process after tests finish, even if handles are still open. It hides the "did not exit" problem instead of fixing it.

The leaked handles are often real bugs (a connection pool that never closes in production too), and forcing exit can cut off cleanup code, like writing files or flushing logs. Use it only as a temporary fix while you track down the leak with `--detectOpenHandles`.

## 218: How should you set maxWorkers in CI?

Jest decides the number of workers from the CPU count it sees. In containers, Node may see all the host's CPUs even if the container is limited to two, so Jest starts too many workers, and they fight for CPU and memory.

Set it explicitly:

```bash
npx jest --ci --maxWorkers=2
# or a percent of what Jest sees
npx jest --ci --maxWorkers=50%
```

Try a few values and compare total time. If workers run out of memory, use fewer workers or set `workerIdleMemoryLimit` so workers restart when they grow too large.

## 219: What do --onlyChanged and --changedSince do?

Both use git to run only tests related to changed files:

- `--onlyChanged` (`-o`): tests related to files changed but not committed yet. This is what `--watch` uses.
- `--changedSince=main`: tests related to files changed since a branch or commit.

```bash
npx jest --changedSince=origin/main
```

"Related" means the test file imports the changed file directly or indirectly. Jest builds this from its dependency graph. It is a good way to speed up pull request checks, but you should still run the full suite on the main branch, because the graph can miss things like config files, JSON imports through custom loaders or global setup changes.

## 220: What does --findRelatedTests do?

It takes a list of source files and runs the tests that depend on them:

```bash
npx jest --findRelatedTests src/cart.js src/price.js
```

It is often used with `lint-staged` to run tests for staged files before a commit:

```json
{
  "lint-staged": {
    "*.{js,ts}": [
      "eslint --fix",
      "jest --bail --findRelatedTests --passWithNoTests"
    ]
  }
}
```

`--passWithNoTests` prevents an error when a changed file has no tests.

## 221: How do you split tests across several CI machines?

Use `--shard`. Each machine runs a part of the test files:

```yaml
# GitHub Actions
strategy:
  matrix:
    shard: [1, 2, 3, 4]
steps:
  - run: npx jest --ci --shard=${{ matrix.shard }}/4
```

Jest splits by test file, not by individual test. If coverage is on, each shard produces its own report, and you need to merge them in a later step (for example with `nyc merge` or `istanbul-merge`) before checking thresholds.

## 222: What do --randomize and --seed do?

`--randomize` shuffles the order of tests within each file. It helps find tests that only pass because an earlier test left some state behind.

```bash
npx jest --randomize
npx jest --randomize --seed=1234
```

Jest prints the seed it used (also with `--showSeed`). If a random order fails, run again with the same `--seed` to get the same order and debug it. Inside tests, `jest.getSeed()` returns the seed, which you can also use to make your own random data repeatable.

## 223: What does --collectTests do?

`--collectTests` is a newer flag (added during the Jest 30.x releases) that finds and lists all tests without running them. It prints a tree of test files, `describe` blocks and test names.

```bash
npx jest --collectTests
npx jest src/cart --collectTests
```

It is useful to check what a filter (`-t`, path patterns) would pick, to count tests, or to see what `test.each` generates. Compare with `--listTests`, which only lists test file paths.

## 224: What is jest.retryTimes?

`jest.retryTimes(n)` retries failing tests in the file up to `n` times. It must be called at the top level of the file (or in a `describe` block):

```js
jest.retryTimes(2, { logErrorsBeforeRetry: true });

test("talks to the staging API", async () => {
  const res = await fetch("https://staging.example.com/health");
  expect(res.ok).toBe(true);
});
```

Options include `logErrorsBeforeRetry`, `waitBeforeRetry` (ms), `retryImmediately` and `entireDescribe`. It only works with the default `jest-circus` runner. Retries hide flakiness, so use them for tests that depend on things outside your control, not to cover up bugs in your own code.

## 225: How do you deal with flaky tests?

1. **Reproduce it.** Run it many times alone and with the full suite. Try `--runInBand`, `--randomize` with a seed, and a different `--maxWorkers`.
2. **Find the cause.** Common ones are real timers and `Date`, missing `await`, shared state between tests, test order, real network calls, time zones and race conditions in the code.
3. **Fix the cause**, not the symptom. Use fake timers, mock the network, reset state in `beforeEach`, and wait for the real condition instead of a fixed sleep.
4. **If you can't fix it right away**, quarantine it: skip it with a linked ticket, or move it to a separate job, so it doesn't block everyone.

Raising timeouts and adding retries make the failures less visible, but the problem stays.

## 226: What reporters does Jest support?

Built-in reporters:

- `default`: the usual output.
- `summary`: only the summary and failed test details at the end.
- `github-actions`: prints failures in a format GitHub shows as inline annotations on the pull request.

Popular third-party reporters are `jest-junit` (JUnit XML for CI dashboards) and `jest-html-reporters`.

```js
module.exports = {
  reporters: [
    "default",
    ["jest-junit", { outputDirectory: "reports", outputName: "junit.xml" }],
  ],
};
```

Setting `reporters` replaces the default list, so include `'default'` (or `'summary'`) if you still want terminal output. You can also pass reporters on the command line with `--reporters`.

## 227: How do you run Jest in GitHub Actions?

```yaml
name: test
on: [push, pull_request]

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
      - run: npx jest --ci --coverage --maxWorkers=2
```

Tips:

- `--ci` stops new snapshots from being written.
- Add the `github-actions` reporter to get failures as annotations on the pull request: `--reporters=default --reporters=github-actions`.
- Upload the `coverage/` folder as an artifact or send `lcov.info` to a coverage service.
- Use a matrix with `--shard` for large suites.

## 228: How do you configure ts-jest?

Install it and add it to `transform` (or use its preset):

```bash
npm install --save-dev ts-jest @types/jest
```

```js
// jest.config.js
module.exports = {
  testEnvironment: "node",
  transform: {
    "^.+\\.tsx?$": ["ts-jest", { tsconfig: "tsconfig.test.json" }],
  },
};
```

ts-jest type checks each test file and the files it imports, and reports type errors as test failures. That is nice for catching mistakes, but it makes runs slower. A common setup is to turn type checking off in ts-jest (transpile only) and run `tsc --noEmit` as a separate CI step. Check the ts-jest docs for the current option name, since it has changed between versions.

## 229: What is @swc/jest?

`@swc/jest` is a transformer that uses SWC, a compiler written in Rust, to turn TypeScript and JSX into JavaScript. It is much faster than ts-jest and Babel, especially on large projects and first runs.

```js
module.exports = {
  transform: {
    "^.+\\.(t|j)sx?$": "@swc/jest",
  },
};
```

Like Babel, it only removes types and does not check them, so run `tsc --noEmit` separately. It reads `.swcrc` if you have one. Most `jest.mock` hoisting works the same as with Babel.

## 230: How do you write the Jest config in TypeScript?

Create `jest.config.ts`. In Jest 30 you can use `defineConfig` for types and autocomplete:

```ts
// jest.config.ts
import { defineConfig } from "jest";

export default defineConfig({
  testEnvironment: "node",
  clearMocks: true,
  coverageProvider: "v8",
});
```

The older way, `const config: Config = {...}` with `import type { Config } from 'jest'`, still works.

To load a TS config, Jest first tries Node's built-in type stripping (available in recent Node versions; the file's module format must match, so use `.mts` or `"type": "module"` for `import`/`export` syntax). If that fails, it uses `ts-node`. You can pick another loader with a docblock at the top of the file, like `/** @jest-config-loader esbuild-register */`.

## 231: What does mergeConfig do?

`mergeConfig(defaults, overrides)` (added in Jest 30.x) merges two config objects, with the second one winning. It is handy when several packages share a base config:

```ts
// packages/api/jest.config.ts
import { defineConfig, mergeConfig } from "jest";
import base from "../../jest.config.base";

export default mergeConfig(
  base,
  defineConfig({
    displayName: "api",
    testEnvironment: "node",
  }),
);
```

Before this helper, people used object spread, which doesn't merge nested objects like `moduleNameMapper` or `coverageThreshold`.

## 232: How do you run Jest with native ES modules?

1. Tell Jest not to transform your code, or use a transformer that keeps ESM.
2. Make Node treat your files as ESM (`"type": "module"` in `package.json`, or `.mjs` files).
3. Start Node with `--experimental-vm-modules`.

```json
{
  "type": "module",
  "scripts": {
    "test": "node --experimental-vm-modules node_modules/jest/bin/jest.js"
  },
  "jest": {
    "transform": {}
  }
}
```

In ESM test files, the `jest` object is not a global injected the same way, so import it: `import { jest } from '@jest/globals'`. `jest.mock` is not hoisted in ESM; use `jest.unstable_mockModule` with dynamic `import()`. This support is still experimental, so expect some rough edges.

## 233: How do you mock a module with native ESM?

Use `jest.unstable_mockModule` and then load the modules with dynamic `import()`, because static imports run before your mock code:

```js
import { jest, test, expect } from "@jest/globals";

jest.unstable_mockModule("./api.js", () => ({
  fetchUser: jest.fn(async () => ({ id: 1, name: "Anna" })),
}));

const { fetchUser } = await import("./api.js");
const { getUserName } = await import("./userService.js");

test("uses the mocked api", async () => {
  await expect(getUserName(1)).resolves.toBe("Anna");
  expect(fetchUser).toHaveBeenCalledWith(1);
});
```

A factory is required (there is no automock in this API). `jest.unstable_unmockModule` (Jest 30) removes the mock again. The `unstable_` prefix means the API may still change.

## 234: How do you mock a dynamic import?

With a Babel or TS transform, `import('./module')` is turned into a `require` wrapped in a promise, so `jest.mock` works as usual:

```js
// loadChart.js
export async function loadChart() {
  const { renderChart } = await import("./heavyChart");
  return renderChart();
}
```

```js
import { loadChart } from "./loadChart";

jest.mock("./heavyChart", () => ({
  renderChart: jest.fn(() => "chart"),
}));

test("loads the chart lazily", async () => {
  await expect(loadChart()).resolves.toBe("chart");
});
```

With native ESM, use `jest.unstable_mockModule` before the code runs the dynamic import.

## 235: How do you test an event emitter?

Attach a mock listener and check it was called, or wait for the event with `events.once`:

```js
const { EventEmitter, once } = require("node:events");

class Job extends EventEmitter {
  run() {
    setImmediate(() => this.emit("done", { ok: true }));
  }
}

test("emits done", async () => {
  const job = new Job();
  const listener = jest.fn();
  job.on("done", listener);

  job.run();
  const [result] = await once(job, "done");

  expect(result).toEqual({ ok: true });
  expect(listener).toHaveBeenCalledTimes(1);
});
```

`once` returns a promise that resolves with the event arguments, and it rejects if the emitter emits `'error'` first.

## 236: How do you test that a promise is still pending?

There is no built-in matcher. A common trick is to race the promise against a value that resolves right after the current microtasks:

```js
const PENDING = Symbol("pending");

async function stateOf(promise) {
  return Promise.race([
    promise,
    new Promise((r) => setImmediate(() => r(PENDING))),
  ]);
}

test("waits for confirmation before resolving", async () => {
  const { promise, confirm } = createConfirmation();

  expect(await stateOf(promise)).toBe(PENDING);

  confirm();
  await expect(promise).resolves.toBe("confirmed");
});
```

This only works with real `setImmediate`, so if fake timers are on, add `setImmediate` to `doNotFake` or use a different flush helper.

## 237: How do you mock crypto.randomUUID or the uuid package?

For the built-in `crypto.randomUUID`, spy on it:

```js
test("assigns an id", () => {
  jest
    .spyOn(crypto, "randomUUID")
    .mockReturnValue("11111111-1111-1111-1111-111111111111");

  expect(createOrder().id).toBe("11111111-1111-1111-1111-111111111111");
});
```

For the `uuid` package, mock the module:

```js
jest.mock("uuid", () => ({ v4: () => "fixed-uuid" }));
```

Often you don't need a fixed value at all. Check the format with `expect.stringMatching(/^[0-9a-f-]{36}$/)` or `expect.any(String)` and keep the real generator.

## 238: What are test data builders or factories?

They are helper functions that create test objects with sensible defaults, so each test only sets the fields it cares about:

```js
let nextId = 1;

function buildUser(overrides = {}) {
  return {
    id: nextId++,
    name: "Test User",
    email: "test@example.com",
    role: "user",
    active: true,
    ...overrides,
  };
}

test("inactive users cannot log in", () => {
  const user = buildUser({ active: false });
  expect(canLogIn(user)).toBe(false);
});
```

When the `User` shape changes, you update one builder instead of fifty tests. Libraries like `@faker-js/faker` and `fishery` help with this, but a plain function is often enough.

## 239: How do you organize tests in a large project?

Some patterns that scale well:

- Keep unit tests next to the code (`cart.ts`, `cart.test.ts`) so they move together.
- Keep slower integration tests in a separate folder or with a different suffix (`*.int.test.ts`), and use `projects` or `testMatch` to run them separately.
- Put shared helpers (builders, custom render functions, test servers) in a `test/` or `testing/` folder.
- Use one `describe` per unit (function, class, component) and nested `describe` blocks for situations ("when the cart is empty").
- Keep global setup small. Too much magic in setup files makes tests hard to understand.

## 240: When should you use dependency injection instead of jest.mock?

Dependency injection means passing dependencies in (as arguments or constructor params) instead of importing them directly. Then the test passes a fake:

```js
// With DI
export function createUserService({ db, mailer }) {
  return {
    async register(user) {
      await db.insert(user);
      await mailer.send(user.email, "Welcome");
    },
  };
}

test("sends a welcome email", async () => {
  const db = { insert: jest.fn() };
  const mailer = { send: jest.fn() };
  await createUserService({ db, mailer }).register({ email: "a@x.com" });
  expect(mailer.send).toHaveBeenCalledWith("a@x.com", "Welcome");
});
```

DI tests are explicit, don't depend on module paths or hoisting, and work the same in Jest, Vitest or any other runner. `jest.mock` is handy when you can't change the code (third-party modules, legacy code), or when adding DI would make the code much more complicated.

## 241: What is over-mocking and why is it a problem?

Over-mocking is when a test mocks so much that it no longer tests real behavior. Signs:

- Every import of the module under test is mocked.
- The test checks that internal functions were called in a certain order, instead of checking the result.
- The test still passes when you break the real code.
- A simple refactor breaks many tests even though behavior didn't change.

Mock at the edges of your system (network, database, time, randomness) and let your own code run for real. If something is hard to test without heavy mocking, that is often a sign the code needs to be split differently.

## 242: Should you test private functions?

Usually no. Test them through the public functions that use them. Private helpers are implementation details, and testing them directly makes refactoring harder.

If a private function is so complex that you really want to test it on its own, that is often a sign it should be its own module with its own public API. Moving it out and exporting it is cleaner than exporting it only for tests. Some teams use a naming convention like `export const _forTesting = {...}`, but that should be rare.

## 243: What does "testing implementation details" mean?

It means the test checks how the code works instead of what it does. Examples:

- Checking a component's internal state instead of what it renders.
- Asserting that a private helper was called.
- Snapshotting the whole internal data structure.
- Checking the exact CSS classes when you care about visibility.

These tests break when you refactor, even though users see no difference, and they can pass while the real behavior is broken. Prefer asserting on outputs, returned values, rendered text, network calls made, and other things a user or caller can observe.

## 244: How does Jest handle unhandled promise rejections?

An unhandled rejection in a test (a promise that rejects with no `catch` and no `await`) can fail the test or be reported against whatever test is running when Node notices it. This makes the error appear in the wrong place.

Jest 30 has a `--waitForUnhandledRejections` option (renamed from `--waitNextEventLoopTurnForUnhandledRejectionEvents`). It gives Node one event loop turn after each test to report unhandled rejections, so they are attached to the right test. It costs a little speed.

The real fix is to always `await` or `return` promises in tests and to handle rejections in the code.

## 245: How do you make tests fail when console.error is called?

React and many libraries report problems with `console.error` (like a missing `key` prop or an `act` warning). If you ignore them, real bugs slip through. You can make them fail tests in a setup file:

```js
// jest.setup.js
let errorSpy;

beforeEach(() => {
  errorSpy = jest.spyOn(console, "error");
});

afterEach(() => {
  const calls = errorSpy.mock.calls;
  errorSpy.mockRestore();
  if (calls.length > 0) {
    throw new Error(
      `console.error was called:\n${calls.map((c) => c.join(" ")).join("\n")}`,
    );
  }
});
```

Throwing in `afterEach` fails the current test. Libraries like `jest-fail-on-console` do the same thing with more options. When a test expects an error, mock `console.error` in that test.

## 246: How does Jest compare to Vitest?

Vitest has an API that is mostly compatible with Jest (`describe`, `test`, `expect`, `vi.fn` instead of `jest.fn`), so moving between them is fairly easy.

- **Vitest** runs on Vite. It uses your Vite config and plugins, supports ESM and TypeScript natively without extra setup, is usually faster in watch mode, and has a browser mode for running tests in a real browser.
- **Jest** has been around longer, has more plugins, presets and answers online, and is the default in many existing projects (React Native, older CRA apps, many Node back ends). ESM support is still experimental.

For a new Vite-based front-end, Vitest is the natural choice. For an existing Jest project that works well, there is often no strong reason to switch.

## 247: How does Jest compare to Mocha?

Mocha is only a test runner. You add an assertion library (Chai, Node's `assert`), a mocking library (Sinon), a coverage tool (c8, nyc) and maybe `jsdom` yourself. That gives you full control but more setup.

Jest includes all of that out of the box, plus snapshots, parallel workers by default and module mocking. Mocha runs all tests in one process by default, which is simpler and sometimes faster for small suites, while Jest isolates each file. Jest's module mocking (`jest.mock`) has no direct match in Mocha; you would use tools like `proxyquire` or DI instead.

## 248: How does Jest compare to the built-in Node.js test runner?

Node has a built-in runner (`node:test`) with `describe`, `it`, hooks, mocks (`mock.fn`, `mock.method`, `mock.timers`), coverage and watch mode. You don't need any dependency, and it runs real ESM and (in recent Node) TypeScript with type stripping.

Jest still offers more: a richer `expect` with many matchers, snapshot testing, `jsdom`, module mocking with hoisting, `projects`, many reporters and integrations, and a large community. The built-in runner is a good option for small libraries and back-end packages where you want zero dependencies. Jest is more convenient for front-end code and big apps.

## 249: How do you migrate from Jest 29 to Jest 30?

Main steps:

1. Check your Node version (18.14+, 20, 22 or 24+) and TypeScript version (5.4+).
2. Update `jest`, `jest-environment-jsdom`, `babel-jest`, `ts-jest`, `@types/jest` and other Jest packages together.
3. Replace removed matcher aliases (`toBeCalled`, `toThrowError` and others). `eslint-plugin-jest` with `jest/no-alias-methods` can fix them.
4. Replace `jest.genMockFromModule` with `jest.createMockFromModule`.
5. Rename `--testPathPattern` to `--testPathPatterns` in scripts and CI.
6. Rerun snapshots and read the changes. Some formatting changed.
7. Fix jsdom changes, for example code that replaced `window.location`.
8. Run the whole suite, fix failures, then remove workarounds that are no longer needed.

Read the official upgrade guide for the full list, since some smaller changes (like how `.mjs`/`.cjs` files are picked up or how `exports` are resolved) may affect only some projects.

## 250: What is moduleFileExtensions?

It lists the file extensions Jest tries when you import a module without an extension. The default is `['js', 'mjs', 'cjs', 'jsx', 'ts', 'mts', 'cts', 'tsx', 'json', 'node']`.

```js
module.exports = {
  moduleFileExtensions: ["ts", "tsx", "js", "json"],
};
```

Extensions earlier in the list are tried first. Keeping only the ones you use makes resolution a little faster. If a test can't find a module like `./Button.vue`, the extension may be missing from this list (and you also need a transform for it).

## 251: What does the injectGlobals option do?

By default Jest puts `describe`, `test`, `expect`, `jest` and the hooks on the global scope. With `injectGlobals: false`, it doesn't, and you must import them:

```js
// jest.config.js
module.exports = {
  injectGlobals: false,
};
```

```js
import { describe, expect, jest, test } from "@jest/globals";
```

Teams use this to avoid global types clashing with other tools (for example Cypress, which also defines `expect`), and to make dependencies clear in every file.

## 252: What does errorOnDeprecated do?

With `errorOnDeprecated: true`, calling a deprecated Jest API throws an error instead of just working, which helps you find old code before an upgrade removes it.

```js
module.exports = {
  errorOnDeprecated: true,
};
```

It is useful to turn on for a while before a major version upgrade.

## 253: What is expect.arrayOf?

`expect.arrayOf(matcher)` was added in Jest 30. It matches an array where every element matches the given value or matcher:

```js
test("every item has an id", () => {
  const items = [
    { id: 1, name: "a" },
    { id: 2, name: "b" },
  ];

  expect(items).toEqual(
    expect.arrayOf(expect.objectContaining({ id: expect.any(Number) })),
  );
});
```

Note that an empty array also matches, since there is no element that fails. Add a length check if the array must not be empty. `expect.not.arrayOf(...)` matches when at least one element does not match.

## 254: What is expect.closeTo?

It is the asymmetric version of `toBeCloseTo`. Use it to compare floats inside objects or arrays:

```js
test("calculates totals", () => {
  expect(getInvoice()).toEqual({
    subtotal: expect.closeTo(30.3, 2),
    tax: expect.closeTo(6.06, 2),
  });
});
```

The second argument is the number of digits to check after the decimal point (2 by default).

## 255: How do you test a React component that loads data?

Mock the data source (the API module, `fetch`, or the network with MSW), render the component and wait for the result with `findBy` queries:

```jsx
import { render, screen } from "@testing-library/react";
import { fetchUsers } from "./api";
import UserList from "./UserList";

jest.mock("./api");

test("shows the users after loading", async () => {
  fetchUsers.mockResolvedValue([{ id: 1, name: "Anna" }]);

  render(<UserList />);

  expect(screen.getByText(/loading/i)).toBeInTheDocument();
  expect(await screen.findByText("Anna")).toBeInTheDocument();
});

test("shows an error", async () => {
  fetchUsers.mockRejectedValue(new Error("Server error"));

  render(<UserList />);

  expect(await screen.findByRole("alert")).toHaveTextContent("Server error");
});
```

`findBy*` waits (up to 1 second by default) for the element to appear, so you don't need manual sleeps.

## 256: What is the "not wrapped in act(...)" warning?

React prints this warning when a component's state changes outside of `act()`, often after a test has already finished checking things. It means your test didn't wait for some update, like a promise resolving after the test ended.

Common fixes:

- Wait for the final state with `await screen.findBy...` or `await waitFor(...)`.
- Use `await userEvent.click(...)`, since `user-event` actions are async.
- Make sure mocked promises resolve before the test ends.
- When you advance fake timers manually, wrap it: `act(() => jest.advanceTimersByTime(1000))`.

React Testing Library wraps `render`, `fireEvent` and its async utilities in `act` for you, so you rarely need to call `act` yourself.

## 257: How do you use fake timers with @testing-library/user-event?

`user-event` uses timers between actions. With fake timers and no setup, its promises never resolve and the test hangs. Tell it how to advance time:

```jsx
import userEvent from "@testing-library/user-event";
import { render, screen } from "@testing-library/react";

test("shows a toast and hides it after 3 seconds", async () => {
  jest.useFakeTimers();
  const user = userEvent.setup({ advanceTimers: jest.advanceTimersByTime });

  render(<SaveButton />);
  await user.click(screen.getByRole("button", { name: "Save" }));
  expect(screen.getByText("Saved")).toBeInTheDocument();

  act(() => {
    jest.advanceTimersByTime(3000);
  });
  expect(screen.queryByText("Saved")).not.toBeInTheDocument();

  jest.useRealTimers();
});
```

`act` here comes from `@testing-library/react`.

## 258: How do you use Jest with Next.js?

Next.js ships a helper, `next/jest`, that sets up transforms with SWC, handles CSS and image imports, loads `.env` files and ignores `.next/`:

```js
// jest.config.js
const nextJest = require("next/jest");

const createJestConfig = nextJest({ dir: "./" });

module.exports = createJestConfig({
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
});
```

You can test client components, hooks and utilities this way. Async Server Components can't be rendered by React Testing Library in Jest, so Next.js suggests end-to-end tests for those.

## 259: How do you test Express middleware without supertest?

Call the middleware with fake `req`, `res` and `next` objects:

```js
function requireAuth(req, res, next) {
  if (!req.headers.authorization) {
    return res.status(401).json({ error: "Unauthorized" });
  }
  next();
}

function mockRes() {
  const res = {};
  res.status = jest.fn().mockReturnValue(res);
  res.json = jest.fn().mockReturnValue(res);
  return res;
}

test("rejects requests without a token", () => {
  const req = { headers: {} };
  const res = mockRes();
  const next = jest.fn();

  requireAuth(req, res, next);

  expect(res.status).toHaveBeenCalledWith(401);
  expect(next).not.toHaveBeenCalled();
});

test("calls next with a token", () => {
  const next = jest.fn();
  requireAuth({ headers: { authorization: "Bearer x" } }, mockRes(), next);
  expect(next).toHaveBeenCalledWith();
});
```

This is fast and focused. Use supertest when you want to check the whole route, with all middleware in order.

## 260: How do you mock a module differently in just one test?

If the module is already mocked with `jest.mock`, change its behavior in that test:

```js
import { getFlags } from "./flags";

jest.mock("./flags", () => ({
  getFlags: jest.fn(() => ({ newCheckout: false })),
}));

test("uses the old checkout by default", () => {
  expect(renderCheckout()).toContain("old");
});

test("uses the new checkout when the flag is on", () => {
  getFlags.mockReturnValueOnce({ newCheckout: true });
  expect(renderCheckout()).toContain("new");
});
```

If the module reads the value at import time, or you need a completely different factory, use `jest.resetModules()`, `jest.doMock()` and `require` inside the test (see `jest.doMock`).

## 261: How do you set a mocked module's return value per test without leaking between tests?

Set the value in each test (or in `beforeEach`) and make sure mocks are reset between tests:

```js
import { fetchPrice } from "./priceApi";

jest.mock("./priceApi");

beforeEach(() => {
  jest.mocked(fetchPrice).mockResolvedValue(100);
});

afterEach(() => {
  jest.resetAllMocks();
});

test("normal price", async () => {
  await expect(getTotal(2)).resolves.toBe(200);
});

test("discounted price", async () => {
  jest.mocked(fetchPrice).mockResolvedValueOnce(50);
  await expect(getTotal(2)).resolves.toBe(100);
});
```

Leftover `Once` values are a common source of leaks: if a test sets two `mockResolvedValueOnce` values but uses only one, the next test gets the other one unless you reset.

## 262: What does the automock option do?

With `automock: true`, every module your tests import is replaced with an automatic mock, unless you call `jest.unmock()` for it. Node core modules are not affected.

```js
module.exports = {
  automock: true,
};
```

```js
jest.unmock("./cart"); // the module under test must be real

const Cart = require("./cart");
```

It is rarely used today. You end up writing `unmock` for most of your own code, and auto-generated mocks of complex modules can behave in surprising ways. Explicit `jest.mock` calls are easier to understand.

## 263: What does jest.requireMock do?

`jest.requireMock('module')` returns the mock version of a module, even if the module isn't mocked in this file. It uses the manual mock from `__mocks__` if there is one, or an automatic mock.

```js
const fs = jest.requireMock("fs");
```

It is the opposite of `jest.requireActual`. It is handy inside factories or helpers when you want to grab a mock without changing how the rest of the file loads the module.

## 264: How does jest.mock resolve the module path?

The path in `jest.mock(path)` is resolved the same way as a `require` from the test file:

- Relative paths (`'./api'`) are relative to the test file, not to the file that imports the module.
- Bare names (`'axios'`) are resolved through `node_modules` and `moduleDirectories`.
- `moduleNameMapper` rules apply, so aliases like `'@/api'` work.

The mock applies to the resolved file. So if your test does `jest.mock('../src/api')` and `src/service.js` imports `./api`, both point to the same file and the mock is used. A wrong relative path is a common reason a mock "doesn't work".

## 265: Can you mock a module that doesn't exist?

Yes, with the `virtual` option. Jest won't try to resolve the path:

```js
jest.mock("app-config", () => ({ apiUrl: "http://test" }), { virtual: true });

const config = require("app-config");
```

This is useful for modules that only exist at runtime, like ones provided by a bundler, a platform or a generated file that isn't built in tests.

## 266: How do you test code that works with the file system?

Two common approaches:

1. **Use a real temp folder.** Create it before the test and delete it after:

   ```js
   const fs = require("node:fs/promises");
   const os = require("node:os");
   const path = require("node:path");

   let dir;

   beforeEach(async () => {
     dir = await fs.mkdtemp(path.join(os.tmpdir(), "export-test-"));
   });

   afterEach(async () => {
     await fs.rm(dir, { recursive: true, force: true });
   });

   test("writes the report", async () => {
     await writeReport(dir, [{ id: 1 }]);
     const content = await fs.readFile(path.join(dir, "report.json"), "utf8");
     expect(JSON.parse(content)).toEqual([{ id: 1 }]);
   });
   ```

2. **Use an in-memory file system** like `memfs`, by mocking `fs` with it.

Real temp folders are simple and catch real problems (permissions, paths). In-memory file systems are faster and let you set up complex folder trees easily.

## 267: How do you mock HTTP calls with nock?

`nock` intercepts Node's HTTP requests and returns the responses you define. Your code (axios, `got`, `http`) runs for real up to the network layer:

```js
const nock = require("nock");
const { getRepo } = require("./github");

afterEach(() => {
  nock.cleanAll();
});

test("returns the repo name", async () => {
  nock("https://api.github.com")
    .get("/repos/jestjs/jest")
    .reply(200, { full_name: "jestjs/jest" });

  await expect(getRepo("jestjs/jest")).resolves.toBe("jestjs/jest");
});
```

`nock.disableNetConnect()` in a setup file makes any unmocked request fail, so tests never hit real APIs by accident. Check the nock docs for your version's support of the built-in `fetch`, since older versions only intercepted the `http` module.

## 268: How do you use MSW with Jest?

Mock Service Worker (MSW) defines request handlers that work at the network level. In Jest you use its Node server:

```js
// test/server.js
import { setupServer } from "msw/node";
import { http, HttpResponse } from "msw";

export const server = setupServer(
  http.get("https://api.example.com/user", () => {
    return HttpResponse.json({ name: "Anna" });
  }),
);
```

```js
// jest.setup.js
import { server } from "./test/server";

beforeAll(() => server.listen({ onUnhandledRequest: "error" }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

```js
test("shows an error when the API fails", async () => {
  server.use(
    http.get(
      "https://api.example.com/user",
      () => new HttpResponse(null, { status: 500 }),
    ),
  );
  // render and assert...
});
```

MSW 2 relies on `fetch`, `Response`, `TextEncoder` and other web APIs that the jsdom environment doesn't provide. The MSW docs suggest using `jest-fixed-jsdom` as the test environment, or adding those globals yourself.

## 269: What is jest-circus?

`jest-circus` is the default test runner in Jest (since version 27). It is the part that runs `describe`, `test` and hooks inside a test file. It replaced `jest-jasmine2`, which was based on Jasmine.

Features that only work with circus include `test.failing`, `jest.retryTimes` and custom test environments that listen to test events (`handleTestEvent`). You can change the runner with the `testRunner` option, but there is rarely a reason to. The old Jasmine-only globals like `fail()`, `pending()` and `jasmine.*` don't exist in circus.

## 270: How do you set environment variables for all tests?

Put them in a file listed in `setupFiles`, which runs before each test file:

```js
// jest.config.js
module.exports = {
  setupFiles: ["<rootDir>/test/setEnv.js"],
};
```

```js
// test/setEnv.js
process.env.NODE_ENV = "test";
process.env.API_URL = "http://localhost:4000";
// or load a file
require("dotenv").config({ path: ".env.test" });
```

Jest already sets `NODE_ENV` to `'test'` if it isn't set. For values that must exist before Jest starts (like `TZ`), set them in the npm script or in `globalSetup`.

## 271: How do you run only some projects in a multi-project setup?

Give each project a `displayName`, then use `--selectProjects` or `--ignoreProjects`:

```js
module.exports = {
  projects: [
    { displayName: "api", testMatch: ["<rootDir>/api/**/*.test.ts"] },
    {
      displayName: "web",
      testMatch: ["<rootDir>/web/**/*.test.tsx"],
      testEnvironment: "jsdom",
    },
  ],
};
```

```bash
npx jest --selectProjects api
npx jest --ignoreProjects web
```

The display name also appears next to each test file in the output, which makes it easy to see which project a failure belongs to.

## 272: What does --showConfig do?

It prints the final config Jest will use, after merging defaults, your config file, presets and CLI flags, and then exits without running tests.

```bash
npx jest --showConfig
```

Use it when a setting doesn't seem to take effect, to check which `transform`, `moduleNameMapper`, `testEnvironment` or `cacheDirectory` Jest is actually using.

## 273: What does "flushing promises" mean and how do you do it?

Sometimes code starts a promise but doesn't give you anything to `await`, like a click handler that calls an API. To check the result, you need to let pending promise callbacks run first. That is called flushing promises:

```js
const flushPromises = () => new Promise((resolve) => setImmediate(resolve));

test("saves after click", async () => {
  const save = jest.fn().mockResolvedValue("ok");
  const status = { text: "" };

  onClickSave(save, status); // does: save().then(() => (status.text = 'Saved'))
  await flushPromises();

  expect(status.text).toBe("Saved");
});
```

`setImmediate` runs after the current microtasks, so promise callbacks queued before it get to run. With fake timers on, `setImmediate` may be faked too; use `await jest.runAllTimersAsync()` or `doNotFake: ['setImmediate']` in that case. When possible, it is cleaner to make the code return its promise.

## 274: How do you test code that uses requestAnimationFrame?

Fake timers also fake `requestAnimationFrame`. Use `jest.advanceTimersToNextFrame()` to run the next frame:

```js
/**
 * @jest-environment jsdom
 */

function fadeIn(element) {
  element.style.opacity = "0";
  requestAnimationFrame(() => {
    element.style.opacity = "1";
  });
}

test("sets opacity on the next frame", () => {
  jest.useFakeTimers();
  const el = document.createElement("div");

  fadeIn(el);
  expect(el.style.opacity).toBe("0");

  jest.advanceTimersToNextFrame();
  expect(el.style.opacity).toBe("1");

  jest.useRealTimers();
});
```

A frame is treated as about 16 ms, so `jest.advanceTimersByTime(16)` works as well.

## 275: How do you check that a mock was called with a callback?

Use `expect.any(Function)` for the callback argument, then grab the callback from `mock.calls` if you need to test what it does:

```js
test("registers a click handler", () => {
  const element = { addEventListener: jest.fn() };
  const onClick = jest.fn();

  bindButton(element, onClick);

  expect(element.addEventListener).toHaveBeenCalledWith(
    "click",
    expect.any(Function),
  );

  const handler = element.addEventListener.mock.calls[0][1];
  handler({ preventDefault: jest.fn() });
  expect(onClick).toHaveBeenCalled();
});
```

## 276: Does toHaveBeenCalledWith allow extra arguments?

No. The arguments are compared as a whole list, so the number of arguments must match. Even a trailing `undefined` counts:

```js
test("argument count matters", () => {
  const fn = jest.fn();
  fn(3, undefined);

  expect(fn).not.toHaveBeenCalledWith(3);
  expect(fn).toHaveBeenCalledWith(3, undefined);
});
```

If you only care about the first argument, check `fn.mock.calls[0][0]` directly, or use `expect.anything()` for the ones you don't care about.

## 277: How do you check part of a long string?

For long text or HTML, a full equality check is fragile. Check only the important parts:

```js
test("email contains the order details", () => {
  const html = renderOrderEmail({ id: 42, total: 99.5 });

  expect(html).toContain("Order #42");
  expect(html).toMatch(/Total:\s*\$99\.50/);
  expect(html).not.toContain("undefined");
});
```

Checking that the output doesn't contain `undefined`, `NaN` or `[object Object]` is a cheap way to catch template bugs.

## 278: What do --json and --outputFile do?

`--json` prints the results as JSON instead of the normal output. Add `--outputFile` to write that JSON to a file:

```bash
npx jest --json --outputFile=test-results.json
```

The JSON includes each test file and test with its status, duration and failure messages. You can use it to build dashboards, find the slowest tests, or feed results into other tools.

## 279: How do you see coverage for just one file?

Run the related tests and limit `collectCoverageFrom` to that file:

```bash
npx jest src/cart --coverage --collectCoverageFrom=src/cart/cart.ts
```

This gives a clear view of what is missing in that file, without the noise of the whole project. The HTML report at `coverage/lcov-report/index.html` highlights uncovered lines and branches.

## 280: How do you test errors that are logged instead of thrown?

If the code catches an error and logs it, check the logger:

```js
const logger = require("./logger");
const { syncOrders } = require("./sync");

jest.mock("./logger");

test("logs and continues when one order fails", async () => {
  const api = {
    send: jest
      .fn()
      .mockRejectedValueOnce(new Error("timeout"))
      .mockResolvedValue("ok"),
  };

  await syncOrders(api, [{ id: 1 }, { id: 2 }]);

  expect(logger.error).toHaveBeenCalledWith(
    "Failed to sync order",
    expect.objectContaining({ orderId: 1, error: expect.any(Error) }),
  );
  expect(api.send).toHaveBeenCalledTimes(2);
});
```

Also check the important side effect: the code kept going after the error.

## 281: How do you test code that calls process.exit?

If `process.exit` actually runs, it kills the Jest worker. Spy on it and replace it:

```js
function main(args) {
  if (!args.includes("--config")) {
    console.error("Missing --config");
    process.exit(1);
  }
}

test("exits with 1 when --config is missing", () => {
  const exit = jest.spyOn(process, "exit").mockImplementation(() => {
    throw new Error("process.exit called");
  });
  jest.spyOn(console, "error").mockImplementation(() => {});

  expect(() => main([])).toThrow("process.exit called");
  expect(exit).toHaveBeenCalledWith(1);

  jest.restoreAllMocks();
});
```

Throwing from the mock stops the function at the same point where the real exit would. A cleaner design is to have `main` return an exit code and call `process.exit` in a tiny wrapper you don't need to test.

## 282: How do you test a CLI script?

For the logic, export functions and test them directly. For the real command (argument parsing, exit codes, output), run it as a child process:

```js
const { execFile } = require("node:child_process");
const { promisify } = require("node:util");

const run = promisify(execFile);

test("prints the version", async () => {
  const { stdout } = await run("node", ["bin/cli.js", "--version"]);
  expect(stdout.trim()).toMatch(/^\d+\.\d+\.\d+$/);
});

test("fails on an unknown command", async () => {
  await expect(run("node", ["bin/cli.js", "nope"])).rejects.toMatchObject({
    code: 1,
    stderr: expect.stringContaining("Unknown command"),
  });
});
```

Process tests are slower, so keep most cases as unit tests and only a few as full runs.

## 283: How do you mock child_process?

Mock the module and set up what `exec`, `execFile` or `spawn` should do:

```js
const { execFile } = require("node:child_process");
const { getGitBranch } = require("./git");

jest.mock("node:child_process");

test("returns the current branch", async () => {
  execFile.mockImplementation((cmd, args, callback) => {
    callback(null, "main\n", "");
  });

  await expect(getGitBranch()).resolves.toBe("main");
  expect(execFile).toHaveBeenCalledWith(
    "git",
    ["branch", "--show-current"],
    expect.any(Function),
  );
});
```

For `spawn`, return a fake object that is an `EventEmitter` with `stdout` and `stderr` streams, and emit `'data'` and `'close'` events from the test.

## 284: How do you test a module that does work when it is imported?

Some modules run code at import time: they read config, connect to a service or register something. To test that, control what exists before the import and load the module inside the test:

```js
beforeEach(() => {
  jest.resetModules();
});

test("throws when DATABASE_URL is missing", () => {
  delete process.env.DATABASE_URL;
  expect(() => require("./db")).toThrow("DATABASE_URL is required");
});

test("connects with the given URL", () => {
  process.env.DATABASE_URL = "postgres://test";
  const pg = require("pg");
  jest.mock("pg");

  require("./db");
  expect(pg.Pool).toHaveBeenCalledWith({ connectionString: "postgres://test" });
});
```

`jest.mock` in the second test is hoisted to the top of the file, so `pg` is mocked for all tests in this file. If side effects make tests this awkward, consider exporting an `init()` function instead of doing work on import.

## 285: How do you clean up the DOM between tests?

With React Testing Library, cleanup is automatic: it unmounts rendered components after each test (when `afterEach` is available globally). For plain DOM tests, reset it yourself:

```js
afterEach(() => {
  document.body.innerHTML = "";
  document.head.innerHTML = "";
});
```

Also clean up global listeners your code added (`window.addEventListener`), timers and anything stored in `localStorage`. Each test file gets a fresh jsdom, but tests in the same file share one.

## 286: What is the snapshotFormat option?

It passes options to `pretty-format`, which turns values into snapshot text. Jest's defaults are `{ escapeString: false, printBasicPrototype: false }`:

- `escapeString: false` means quotes inside strings aren't escaped with backslashes.
- `printBasicPrototype: false` means objects and arrays print as `{}` and `[]` instead of `Object {}` and `Array []`.

```js
module.exports = {
  snapshotFormat: {
    printBasicPrototype: true, // old style, from before Jest 29
  },
};
```

Changing these options changes every snapshot, so do it once and update all snapshots in one commit.

## 287: How do you set the time zone for tests?

Set the `TZ` environment variable. The safest way is in the npm script or in `globalSetup`, so it applies before any test code runs:

```json
{
  "scripts": {
    "test": "TZ=UTC jest"
  }
}
```

```js
// globalSetup.js
module.exports = async () => {
  process.env.TZ = "UTC";
};
```

The `TZ=UTC jest` syntax doesn't work in Windows `cmd`; use `globalSetup` or the `cross-env` package there. To test behavior in a specific time zone, you can also run a project with a different `TZ`, or pass `timeZone` to `Intl.DateTimeFormat` in the code so it doesn't depend on the machine.

## 288: Should you create database data in beforeAll or beforeEach?

- `beforeEach` gives every test fresh data. Tests are independent and can run in any order, but setup runs many times and the suite is slower.
- `beforeAll` sets up data once per file. It is faster, but tests that change data affect later tests.

A common middle ground: create the schema and read-only reference data in `beforeAll`, and create or clean the rows a test changes in `beforeEach`. Another option is to wrap each test in a transaction and roll it back in `afterEach`, which is fast and keeps tests isolated, as long as the code under test uses the same connection.

## 289: How do you check that a mock was never called with certain arguments?

Use `.not.toHaveBeenCalledWith`. It passes if no call matched those arguments:

```js
test("does not log the password", () => {
  const log = jest.fn();
  login({ user: "anna", password: "secret" }, log);

  expect(log).not.toHaveBeenCalledWith(expect.stringContaining("secret"));
});
```

Be careful: this passes if the argument count is different, too. If `log` is called with two arguments and you check one, the check passes even if the first argument contains `secret`. For important checks, look at every call: `expect(log.mock.calls.flat().join(' ')).not.toContain('secret')`.

## 290: How do you mock a function that is called from the same module?

If `a()` and `b()` are in the same file and `a` calls `b`, mocking the export `b` usually doesn't affect `a`, because `a` calls the local function, not the exported one:

```js
// math.js
export function double(x) {
  return x * 2;
}
export function quadruple(x) {
  return double(double(x)); // calls the local double
}
```

`jest.mock('./math', () => ({ ...jest.requireActual('./math'), double: jest.fn() }))` won't change what `quadruple` calls. Options:

- Move `double` to its own module and mock that module.
- Pass `double` in as a parameter (dependency injection).
- Test `quadruple` with the real `double`, which is often the right call for pure functions anyway.

## 291: How do you mock an exported constant?

You can't reassign an imported binding, and `jest.replaceProperty` doesn't work on ES module namespaces. Use a `jest.mock` factory:

```js
import { MAX_ITEMS } from "./limits";
import { canAddItem } from "./cart";

jest.mock("./limits", () => ({
  ...jest.requireActual("./limits"),
  MAX_ITEMS: 2,
}));

test("stops at the limit", () => {
  expect(MAX_ITEMS).toBe(2);
  expect(canAddItem([1, 2])).toBe(false);
});
```

If you need different values in different tests, use a getter in the factory that reads a variable, or `jest.doMock` with `jest.resetModules`. A config object or a function (`getMaxItems()`) is easier to change in tests than a bare constant.

## 292: What are watch plugins?

Watch plugins add new keys and features to `jest --watch`. The most popular is `jest-watch-typeahead`, which lets you type a file name or test name and see matching ones as you type:

```js
module.exports = {
  watchPlugins: [
    "jest-watch-typeahead/filename",
    "jest-watch-typeahead/testname",
  ],
};
```

You can write your own plugin by implementing hooks like `apply` and `onKey`, for example to add a key that runs only integration tests.

## 293: How do you print the DOM when a test fails?

With React Testing Library, use `screen.debug()` to print the current DOM, or `screen.debug(element)` for one element:

```jsx
test("shows the form", () => {
  render(<SignupForm />);
  screen.debug(); // prints the HTML
});
```

When a `getBy` query fails, Testing Library already prints the DOM in the error. Long output is cut at 7000 characters; set the `DEBUG_PRINT_LIMIT` environment variable to see more. `prettyDOM(element)` returns the same output as a string. `screen.logTestingPlaygroundURL()` gives you a link to a tool that suggests the best query.

## 294: How do you test async generators?

Collect the values with `for await` or `Array.fromAsync` (Node 22+), then compare:

```js
async function* paginate(fetchPage) {
  let page = 1;
  while (true) {
    const items = await fetchPage(page);
    if (items.length === 0) return;
    yield* items;
    page += 1;
  }
}

test("yields items from all pages", async () => {
  const fetchPage = jest
    .fn()
    .mockResolvedValueOnce([1, 2])
    .mockResolvedValueOnce([3])
    .mockResolvedValueOnce([]);

  const result = [];
  for await (const item of paginate(fetchPage)) {
    result.push(item);
  }

  expect(result).toEqual([1, 2, 3]);
  expect(fetchPage).toHaveBeenCalledTimes(3);
});
```

To test early stopping, call `.next()` manually and check that no more pages are fetched.

## 295: How do you check calls to a mocked constructor?

A mocked class is a mock function, so you can check `new` calls with the usual matchers. `mock.instances` holds the created objects:

```js
import { Logger } from "./Logger";
import { createApp } from "./app";

jest.mock("./Logger");

test("creates one logger with the app name", () => {
  createApp({ name: "shop" });

  expect(Logger).toHaveBeenCalledTimes(1);
  expect(Logger).toHaveBeenCalledWith({ prefix: "shop" });

  const logger = Logger.mock.instances[0];
  expect(logger.info).toHaveBeenCalledWith("App started");
});
```

## 296: How do you avoid repeating the same jest.mock in many files?

Options:

- **Manual mocks for packages**: a file in the root `__mocks__` folder (like `__mocks__/axios.js`) is used automatically in every test for that `node_modules` package.
- **jest.mock in a setup file**: calls in `setupFilesAfterEnv` apply to every test file.
- **moduleNameMapper** to point a module to a stub for all tests.
- **A helper** that sets up common mock behavior, called from `beforeEach`.

Global mocks are convenient but hidden. Someone reading a test may not know `axios` is fake. Keep the list short and document it in the setup file.

## 297: How do you speed up a slow test file?

Look for the usual suspects first:

- **Real timers and sleeps**: replace `await sleep(1000)` with fake timers or with waiting for the real condition.
- **Heavy setup in beforeEach** that could be in `beforeAll` (if it's read-only).
- **Importing huge modules** just to test a small function. Mock heavy dependencies or split the module.
- **Real network calls** that time out or are slow. Mock them.
- **Large snapshots** of big trees that take time to serialize and compare.
- **Too many tests in one file**. Jest parallelizes by file, so splitting a 2,000-test file can help.

Use `--verbose` to see each test's duration, and fix the slowest ones first.

## 298: What does a good Jest config for a TypeScript Node project look like?

A solid starting point:

```ts
// jest.config.ts
import { defineConfig } from "jest";

export default defineConfig({
  testEnvironment: "node",
  roots: ["<rootDir>/src"],
  transform: {
    "^.+\\.ts$": "@swc/jest",
  },
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/src/$1",
  },
  setupFilesAfterEnv: ["<rootDir>/test/setup.ts"],
  clearMocks: true,
  restoreMocks: true,
  collectCoverageFrom: ["src/**/*.ts", "!src/**/*.d.ts", "!src/**/index.ts"],
  coverageProvider: "v8",
  coverageThreshold: {
    global: { branches: 80, lines: 80 },
  },
});
```

Run `tsc --noEmit` as a separate step for type checking, since SWC only strips types.

## 299: How do you test code that retries a failed request?

Make the mock fail a few times and then succeed:

```js
async function withRetry(fn, attempts = 3) {
  let lastError;
  for (let i = 0; i < attempts; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;
    }
  }
  throw lastError;
}

test("succeeds on the third try", async () => {
  const fn = jest
    .fn()
    .mockRejectedValueOnce(new Error("fail 1"))
    .mockRejectedValueOnce(new Error("fail 2"))
    .mockResolvedValue("ok");

  await expect(withRetry(fn)).resolves.toBe("ok");
  expect(fn).toHaveBeenCalledTimes(3);
});

test("gives up after 3 tries", async () => {
  const fn = jest.fn().mockRejectedValue(new Error("down"));

  await expect(withRetry(fn)).rejects.toThrow("down");
  expect(fn).toHaveBeenCalledTimes(3);
});
```

Test both the success path and the "gives up" path, and check the call count so you know the retry limit is correct.

## 300: How do you test a React component that needs a context provider or router?

Wrap it in the providers it needs. To avoid repeating this in every test, write a custom render function:

```jsx
// test/render.jsx
import { render } from "@testing-library/react";
import { MemoryRouter } from "react-router";
import { ThemeProvider } from "../src/theme";

export function renderWithProviders(ui, { route = "/", theme = "light" } = {}) {
  return render(
    <ThemeProvider value={theme}>
      <MemoryRouter initialEntries={[route]}>{ui}</MemoryRouter>
    </ThemeProvider>,
  );
}
```

```jsx
import { screen } from "@testing-library/react";
import { renderWithProviders } from "../test/render";
import Header from "./Header";

test("highlights the current page", () => {
  renderWithProviders(<Header />, { route: "/orders" });
  expect(screen.getByRole("link", { name: "Orders" })).toHaveAttribute(
    "aria-current",
    "page",
  );
});
```

Using real providers with test values is usually better than mocking `useContext`.
