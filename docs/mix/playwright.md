# Playwright Interview Questions and Answers

_Last updated: October 29, 2026_

450 Playwright interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers target Playwright 1.6x with the Playwright Test runner (`@playwright/test`) and TypeScript. The focus is on the current way of writing tests: role-based locators, web-first assertions, fixtures, projects and the trace viewer. Older patterns like `ElementHandle`, `page.waitForSelector()` and `page.$()` are mentioned where you will still see them in real projects.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

---

# Easy Questions (1-150)

## 1: What is Playwright?

Playwright is an open source tool from Microsoft for automating web browsers. It is mostly used for end-to-end (E2E) testing, but you can also use it for scraping, generating PDFs or screenshots, or any other browser automation.

It comes in two parts:

- **Playwright Library** (`playwright`): the API to launch browsers and control pages.
- **Playwright Test** (`@playwright/test`): a full test runner built on top of the library, with fixtures, assertions, parallel runs, retries, reports and traces.

Most teams use Playwright Test, and this guide is focused on it.

## 2: Which browsers does Playwright support?

Playwright supports three browser engines:

- **Chromium** (Chrome, Edge and other Chromium-based browsers)
- **Firefox**
- **WebKit** (the engine behind Safari)

It runs on Windows, Linux and macOS, headless or headed. You can also run tests against branded browsers like Google Chrome and Microsoft Edge using the `channel` option. Since 1.57, the default Chromium build Playwright downloads is Chrome for Testing.

## 3: Which programming languages can you use with Playwright?

Playwright has official versions for:

- JavaScript and TypeScript (Node.js)
- Python
- Java
- .NET (C#)

The browser API is almost the same in all of them. The Playwright Test runner (`@playwright/test`) is only for JavaScript and TypeScript. Other languages use their own test runners, for example pytest for Python or JUnit/TestNG for Java.

## 4: How do you set up Playwright in a new project?

Run the init command in your project folder:

```bash
npm init playwright@latest
```

It asks a few questions (TypeScript or JavaScript, test folder name, add a GitHub Actions workflow, install browsers) and then creates:

- `playwright.config.ts`
- a `tests/` folder with an example test
- `package.json` with `@playwright/test` as a dev dependency
- optionally `.github/workflows/playwright.yml`

## 5: How do you install the browsers Playwright needs?

Playwright uses its own browser builds, which you install with:

```bash
npx playwright install
```

You can install only one browser, and on Linux (especially in CI) you can also install the system libraries the browsers need:

```bash
npx playwright install chromium
npx playwright install --with-deps
```

The browser versions are tied to the Playwright version, so after you upgrade `@playwright/test` you need to run `npx playwright install` again.

## 6: How do you write a basic Playwright test?

Import `test` and `expect` from `@playwright/test`, then use the `page` fixture:

```ts
import { test, expect } from "@playwright/test";

test("home page has a title", async ({ page }) => {
  await page.goto("https://playwright.dev/");
  await expect(page).toHaveTitle(/Playwright/);
});
```

Each test gets a fresh `page` in a fresh browser context, so tests do not share cookies or local storage.

## 7: How do you run Playwright tests?

```bash
npx playwright test
```

Some common variations:

```bash
npx playwright test tests/login.spec.ts   # one file
npx playwright test login                 # files matching "login"
npx playwright test tests/login.spec.ts:15 # the test at line 15
npx playwright test -g "add to cart"      # tests with this title
npx playwright test --project=chromium    # one project only
npx playwright test --headed              # show the browser
```

## 8: What is the difference between headless and headed mode?

In headless mode the browser runs without a visible window. It is the default in Playwright Test, and it is what you use in CI because it is faster and doesn't need a display.

In headed mode you can see the browser while the test runs. It is useful when writing or debugging tests. You turn it on with `--headed` on the command line or with `headless: false` in the config.

```ts
// playwright.config.ts
export default defineConfig({
  use: { headless: false },
});
```

## 9: What are the test and expect functions?

`test` declares a test. It takes a title and an async function that receives fixtures like `page`, `context` or `request`.

`expect` makes assertions. Playwright's `expect` includes the usual Jest-style matchers (`toBe`, `toEqual`, `toContain`) plus web-first matchers like `toBeVisible()` and `toHaveText()` that wait and retry.

```ts
test("counter increments", async ({ page }) => {
  await page.goto("/counter");
  await page.getByRole("button", { name: "Increment" }).click();
  await expect(page.getByTestId("count")).toHaveText("1");
});
```

## 10: What is a fixture in Playwright Test?

A fixture is something a test needs, set up before the test and cleaned up after it. You ask for fixtures by destructuring them in the test function, and Playwright creates only the ones you ask for.

```ts
test("example", async ({ page, request, browserName }) => {
  // page, request and browserName are fixtures
});
```

Fixtures replace a lot of what you would do in `beforeEach`/`afterEach` in other runners. You can also create your own fixtures with `test.extend()`.

## 11: What built-in fixtures does Playwright Test provide?

The main ones are:

- `page`: a new page in a new browser context, for each test.
- `context`: the browser context that `page` belongs to.
- `browser`: the browser instance, shared between tests in the same worker.
- `browserName`: `'chromium'`, `'firefox'` or `'webkit'`.
- `request`: an `APIRequestContext` for sending HTTP requests without a browser.

You also have access to `testInfo` as the second argument of the test function.

## 12: How do you open a URL in Playwright?

Use `page.goto()`:

```ts
await page.goto("https://example.com/login");
```

By default, `goto` waits for the `load` event. You can change that with `waitUntil`:

```ts
await page.goto("/dashboard", { waitUntil: "domcontentloaded" });
```

`goto` returns the main resource response (or `null`), so you can check the status:

```ts
const response = await page.goto("/");
expect(response?.status()).toBe(200);
```

## 13: What is baseURL and why is it useful?

`baseURL` is set in the config so you can use relative URLs in your tests:

```ts
// playwright.config.ts
export default defineConfig({
  use: { baseURL: "http://localhost:3000" },
});
```

```ts
await page.goto("/login"); // goes to http://localhost:3000/login
```

This way you can run the same tests against local, staging and production just by changing one value, usually from an environment variable.

## 14: What is a locator?

A locator is a way to find element(s) on the page. You create it with methods like `page.getByRole()` or `page.locator()`.

A locator doesn't search the page when you create it. It finds the element only when you act on it (click, fill, assert). Every time you use it, it searches again, so it always works with the current DOM. This is why locators don't go "stale" the way old element handles do.

```ts
const submit = page.getByRole("button", { name: "Submit" });
await submit.click();
```

## 15: How does getByRole work?

`getByRole` finds elements by their ARIA role and accessible name, the same way screen readers see them. It is the recommended locator in most cases.

```ts
await page.getByRole("button", { name: "Sign in" }).click();
await page.getByRole("link", { name: "Pricing" }).click();
await page.getByRole("checkbox", { name: "Remember me" }).check();
await expect(page.getByRole("heading", { name: "Welcome" })).toBeVisible();
```

Common roles are `button`, `link`, `textbox`, `checkbox`, `radio`, `heading`, `list`, `listitem`, `row`, `cell`, `dialog` and `combobox`. Native HTML elements have implicit roles, so a `<button>` is a `button` without needing a `role` attribute.

## 16: How does getByText work?

`getByText` finds elements by the text they contain. By default it matches a substring, ignores case and trims whitespace.

```ts
page.getByText("Welcome back"); // substring, case-insensitive
page.getByText("Welcome back", { exact: true }); // whole text, case-sensitive
page.getByText(/welcome, \w+/i); // regex
```

It is good for non-interactive content like paragraphs or messages. For buttons and links, `getByRole` with a `name` is better.

## 17: How do you find form fields with getByLabel and getByPlaceholder?

`getByLabel` finds an input by the text of its `<label>`, `aria-labelledby` or `aria-label`:

```ts
await page.getByLabel("Email").fill("user@example.com");
await page.getByLabel("Password").fill("secret");
```

`getByPlaceholder` finds an input by its placeholder text:

```ts
await page.getByPlaceholder("Search products").fill("shoes");
```

Prefer `getByLabel`, since a labeled input is also better for accessibility. Use `getByPlaceholder` when the field has no label.

## 18: What are getByAltText and getByTitle used for?

`getByAltText` finds elements, usually images, by their `alt` text:

```ts
await page.getByAltText("Company logo").click();
```

`getByTitle` finds elements by their `title` attribute:

```ts
await expect(page.getByTitle("Issues count")).toHaveText("25 issues");
```

## 19: What is getByTestId and when should you use it?

`getByTestId` finds elements by the `data-testid` attribute:

```html
<button data-testid="checkout-btn">Pay now</button>
```

```ts
await page.getByTestId("checkout-btn").click();
```

Test ids are stable because they don't change when the text or styling changes. The downside is that they don't test anything the user sees. Use them when role or text locators don't work well, for example for elements with no clear name or with text that changes a lot. You can change the attribute name with `testIdAttribute` in the config.

## 20: How do you use CSS and XPath selectors in Playwright?

Use `page.locator()`:

```ts
page.locator(".product-card");
page.locator("#main > ul li:first-child");
page.locator('xpath=//button[@type="submit"]');
page.locator("//button"); // strings starting with // or .. are treated as XPath
```

CSS and XPath work, but they are tied to the DOM structure and break when the markup changes. Playwright recommends user-facing locators (`getByRole`, `getByLabel`, `getByText`) first and CSS/XPath only when there is no better option.

## 21: In what order should you prefer locators?

Playwright's docs suggest roughly this order:

1. `getByRole` (best for interactive elements)
2. `getByLabel` (form fields)
3. `getByPlaceholder`
4. `getByText` (non-interactive content)
5. `getByAltText`, `getByTitle`
6. `getByTestId`
7. CSS or XPath with `page.locator()` (last resort)

The idea is to find elements the way a user does. If a test can't find a button by its role and name, a screen reader user may also have trouble with it.

## 22: How do you click an element?

```ts
await page.getByRole("button", { name: "Save" }).click();
```

There are options for other cases:

```ts
await locator.dblclick();
await locator.click({ button: "right" });
await locator.click({ modifiers: ["Shift"] });
await locator.click({ position: { x: 10, y: 10 } });
```

Before clicking, Playwright waits until the element is visible, stable, enabled and able to receive the click.

## 23: What is the difference between fill and pressSequentially?

`fill()` sets the value of an input in one go. It focuses the element, clears it, and fires an `input` event. It is fast and what you should use in most cases.

`pressSequentially()` types one character at a time, firing keyboard events for each key. Use it when the page reacts to each key press, for example an autocomplete that needs `keydown` events.

```ts
await page.getByLabel("Name").fill("Alice");
await page.getByLabel("Search").pressSequentially("play", { delay: 100 });
```

`locator.type()` is the older name for `pressSequentially()` and is deprecated.

## 24: How do you press keys like Enter or Tab?

Use `locator.press()` or `page.keyboard.press()`:

```ts
await page.getByLabel("Search").press("Enter");
await page.keyboard.press("Tab");
await page.keyboard.press("Control+A");
await page.keyboard.press("ControlOrMeta+C"); // Ctrl on Windows/Linux, Cmd on macOS
```

Key names follow the `KeyboardEvent.key` values: `Enter`, `Escape`, `ArrowDown`, `Backspace`, `F1` and so on.

## 25: How do you check and uncheck checkboxes and radio buttons?

```ts
await page.getByRole("checkbox", { name: "Subscribe" }).check();
await page.getByRole("checkbox", { name: "Subscribe" }).uncheck();
await page.getByRole("radio", { name: "Express shipping" }).check();

// set to a value from a variable
await page.getByLabel("Accept terms").setChecked(true);
```

`check()` does nothing if the box is already checked, and it fails if the state didn't change after the click.

## 26: How do you select an option in a dropdown?

For a native `<select>` element use `selectOption()`. You can pass the value, the label or several values for a multi-select:

```ts
await page.getByLabel("Country").selectOption("ge"); // by value or label
await page.getByLabel("Country").selectOption({ label: "Georgia" });
await page.getByLabel("Colors").selectOption(["red", "blue"]); // multi-select
```

Custom dropdowns built with `<div>`s are not real selects, so you click to open them and then click the option, usually with `getByRole('option', { name: '...' })`.

## 27: How do you hover over an element?

```ts
await page.getByRole("button", { name: "Account" }).hover();
await page.getByRole("menuitem", { name: "Settings" }).click();
```

`hover()` moves the mouse over the element after the same actionability checks as click. It is useful for menus and tooltips that appear on hover.

## 28: How do you upload a file?

Use `setInputFiles()` on the file input:

```ts
await page.getByLabel("Upload avatar").setInputFiles("fixtures/avatar.png");

// several files
await page.getByLabel("Attachments").setInputFiles(["a.pdf", "b.pdf"]);

// clear the selection
await page.getByLabel("Attachments").setInputFiles([]);

// from memory
await page.getByLabel("Upload").setInputFiles({
  name: "notes.txt",
  mimeType: "text/plain",
  buffer: Buffer.from("hello"),
});
```

## 29: What is auto-waiting in Playwright?

Before doing an action, Playwright automatically waits for the element to be ready. For example, before `click()` it waits until the element:

- is attached to the DOM
- is visible
- is stable (not animating)
- receives events (not covered by another element)
- is enabled

If the element is not ready before the timeout, the action fails with a clear error that explains which check failed. Because of this, you almost never need manual waits or sleeps.

## 30: What are actionability checks?

Actionability checks are the conditions Playwright checks before an action. Different actions need different checks:

| Check           | Meaning                                         |
| --------------- | ----------------------------------------------- |
| Visible         | has a non-empty box and no `visibility: hidden` |
| Stable          | same bounding box for two animation frames      |
| Enabled         | not `disabled`                                  |
| Editable        | enabled and not `readonly`                      |
| Receives events | is the element hit by a click at that point     |

For example, `click()` needs all of them except editable, `fill()` needs visible, enabled and editable, and `focus()` needs no checks. You can skip most of them with `force: true`, but that usually hides a real problem.

## 31: What are web-first assertions?

Web-first assertions are `expect` matchers that work on locators or pages and retry until the condition is true or the timeout runs out (5 seconds by default).

```ts
await expect(page.getByText("Saved")).toBeVisible();
await expect(page).toHaveURL(/\/dashboard/);
```

They are async, so you must `await` them. Because they retry, they handle content that appears after an API call without any manual waiting.

## 32: What is the difference between toHaveText and toContainText?

`toHaveText` checks the full text of the element. `toContainText` checks that the text includes a substring.

```ts
// element text: "Total: $42.00"
await expect(locator).toHaveText("Total: $42.00");
await expect(locator).toContainText("$42");
await expect(locator).toHaveText(/Total: \$\d+/);
```

If the locator matches several elements, you can pass an array to check all of them in order:

```ts
await expect(page.getByRole("listitem")).toHaveText([
  "Apples",
  "Bananas",
  "Cherries",
]);
```

## 33: How do you check the value of an input?

Use `toHaveValue`:

```ts
await page.getByLabel("Email").fill("a@b.com");
await expect(page.getByLabel("Email")).toHaveValue("a@b.com");
```

For a multi-select there is `toHaveValues(['red', 'blue'])`. `toHaveText` doesn't work on inputs, because an input's value is not its text content.

## 34: How do you check the page URL and title?

```ts
await expect(page).toHaveURL("http://localhost:3000/dashboard");
await expect(page).toHaveURL(/\/dashboard$/);
await expect(page).toHaveTitle("Dashboard | MyApp");
```

These retry, so they work well after a click that triggers a navigation. If `baseURL` is set, `toHaveURL` also accepts a relative path like `'/dashboard'`.

## 35: How do you check how many elements match a locator?

Use `toHaveCount`:

```ts
await expect(page.getByRole("listitem")).toHaveCount(3);
await expect(page.locator(".error")).toHaveCount(0);
```

There is also `locator.count()`, but it doesn't wait. Use the assertion when the number may still change.

## 36: How do you check if an element is visible or hidden?

```ts
await expect(page.getByText("Loading...")).toBeHidden();
await expect(page.getByRole("dialog")).toBeVisible();
await expect(page.getByRole("dialog")).not.toBeVisible();
```

An element is hidden if it doesn't exist, has `display: none`, `visibility: hidden` or has an empty size. `toBeHidden()` and `not.toBeVisible()` mean the same thing.

## 37: How do you check if a button is enabled or disabled?

```ts
await expect(page.getByRole("button", { name: "Submit" })).toBeDisabled();
await page.getByLabel("Name").fill("Alice");
await expect(page.getByRole("button", { name: "Submit" })).toBeEnabled();
```

`toBeDisabled` checks the native `disabled` attribute on form controls and `aria-disabled="true"` on other elements.

## 38: How do you check if a checkbox is checked?

```ts
await expect(page.getByRole("checkbox", { name: "Remember me" })).toBeChecked();
await expect(
  page.getByRole("checkbox", { name: "Newsletter" }),
).not.toBeChecked();
await expect(page.getByLabel("Agree")).toBeChecked({ checked: false });
```

## 39: How do you check attributes and CSS classes?

```ts
await expect(page.getByRole("link", { name: "Docs" })).toHaveAttribute(
  "href",
  "/docs",
);
await expect(page.getByRole("tab", { name: "Home" })).toHaveAttribute(
  "aria-selected",
  "true",
);

await expect(page.getByTestId("alert")).toHaveClass(/error/);
await expect(page.getByTestId("alert")).toContainClass("error");
```

`toHaveClass` with a string checks the full `class` attribute. `toContainClass` (added in 1.52) checks that specific class names are present, which is usually what you want.

## 40: How do you negate an assertion?

Put `.not` before the matcher:

```ts
await expect(page.getByText("Error")).not.toBeVisible();
await expect(page).not.toHaveURL(/login/);
await expect(page.getByRole("button")).not.toBeDisabled();
```

Negated web-first assertions also retry, so `not.toBeVisible()` waits until the element goes away.

## 41: What is the difference between generic and web-first assertions?

Generic assertions like `expect(value).toBe(5)` check a plain value once. They don't wait or retry.

Web-first assertions like `expect(locator).toHaveText('5')` work on locators and pages and keep retrying.

A common mistake is:

```ts
// bad: reads the text once, no retry
expect(await page.getByTestId("count").textContent()).toBe("5");

// good: retries until the text is 5
await expect(page.getByTestId("count")).toHaveText("5");
```

## 42: What are soft assertions?

A soft assertion doesn't stop the test when it fails. The test continues, and at the end it is marked as failed with all the failures listed.

```ts
await expect.soft(page.getByTestId("name")).toHaveText("Alice");
await expect.soft(page.getByTestId("email")).toHaveText("alice@example.com");
await page.getByRole("link", { name: "Settings" }).click();
```

They are useful when you want to check many independent things on one page and see all the problems in one run.

## 43: How do you add a custom message to an assertion?

Pass the message as the second argument to `expect`:

```ts
await expect(
  page.getByText("Welcome"),
  "user should be logged in",
).toBeVisible();
```

The message shows up in the error and in the report, which makes failures easier to understand.

## 44: How do you group tests?

Use `test.describe`:

```ts
test.describe("cart", () => {
  test("add item", async ({ page }) => {
    /* ... */
  });
  test("remove item", async ({ page }) => {
    /* ... */
  });
});
```

Groups can be nested. Hooks inside a `describe` apply only to the tests in that group, and you can set options for the group with `test.use()` or `test.describe.configure()`.

## 45: What are beforeEach and afterEach hooks?

They run before and after each test in the file or `describe` block:

```ts
test.beforeEach(async ({ page }) => {
  await page.goto("/login");
});

test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    console.log(`${testInfo.title} failed on ${page.url()}`);
  }
});
```

Hooks get the same fixtures as tests. For setup that many files share, a custom fixture is usually cleaner than repeating `beforeEach`.

## 46: What are beforeAll and afterAll hooks?

They run once per worker, before the first test and after the last test in the file or group:

```ts
test.beforeAll(async ({ request }) => {
  await request.post("/api/test/reset");
});
```

You can't use `page` or `context` in `beforeAll`, because those are created per test. If a test fails, the worker restarts and `beforeAll` runs again in the new worker, so don't assume it runs only once per run.

## 47: How do you skip a test?

```ts
test.skip("not ready yet", async ({ page }) => {});

test("only on chromium", async ({ page, browserName }) => {
  test.skip(browserName !== "chromium", "Chromium only feature");
  // ...
});

test.describe("mobile", () => {
  test.skip(({ isMobile }) => !isMobile, "mobile only");
  // tests...
});
```

A skipped test is not run and is shown as skipped in the report.

## 48: What does test.only do?

`test.only` runs only that test (and other `.only` tests) and skips the rest. `test.describe.only` does the same for a group.

```ts
test.only("focus on this", async ({ page }) => {});
```

It is handy while debugging, but you don't want it committed. Set `forbidOnly: !!process.env.CI` in the config so CI fails if someone forgets a `.only`.

## 49: What are test.fixme and test.fail?

- `test.fixme()` marks a test as broken and skips it. Use it for tests that fail and you plan to fix later.
- `test.fail()` marks a test as "expected to fail". Playwright runs it and reports a problem if it **passes**. Use it to document a known bug: when the bug is fixed, the test will tell you.

```ts
test.fixme("crashes on safari", async ({ page }) => {});

test("known bug #123", async ({ page }) => {
  test.fail();
  // ...
});
```

## 50: What does test.slow do?

`test.slow()` triples the timeout for the test. Use it for tests that are slow on purpose, like a big file upload.

```ts
test("upload large file", async ({ page }) => {
  test.slow();
  // ...
});

test("slow on webkit", async ({ page, browserName }) => {
  test.slow(browserName === "webkit", "webkit is slow here");
});
```

## 51: How do you tag tests?

Pass a `tag` in the test details, or put `@tag` in the title. Tags must start with `@`.

```ts
test(
  "checkout works",
  { tag: ["@smoke", "@payments"] },
  async ({ page }) => {},
);

test.describe("admin", { tag: "@admin" }, () => {
  test("can delete user", async ({ page }) => {});
});
```

Then filter by tag on the command line:

```bash
npx playwright test --grep @smoke
npx playwright test --grep-invert @slow
```

## 52: How do you run only some tests with grep?

`--grep` (or `-g`) runs tests whose full title (file, describe blocks, test title and tags) matches a regular expression. `--grep-invert` runs the ones that don't match.

```bash
npx playwright test --grep "login"
npx playwright test --grep "@smoke|@critical"
npx playwright test --grep-invert @flaky
```

You can also set `grep` and `grepInvert` in the config or per project, for example to make a "smoke" project.

## 53: What are annotations?

Annotations attach extra info to a test that shows up in the report. Besides the built-in ones (`skip`, `fixme`, `fail`, `slow`), you can add your own:

```ts
test(
  "pay with card",
  {
    annotation: {
      type: "issue",
      description: "https://github.com/org/repo/issues/42",
    },
  },
  async ({ page }) => {},
);
```

You can also add them while the test runs:

```ts
test.info().annotations.push({
  type: "browser version",
  description: browser.version(),
});
```

## 54: What is playwright.config.ts?

It is the main config file for Playwright Test. It defines where tests are, which browsers to run, timeouts, retries, reporters and default options for every test.

```ts
import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,
  reporter: "html",
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
  ],
});
```

`defineConfig` is a helper that gives you type checking and autocomplete for the config object.

## 55: How does Playwright find test files?

It looks inside `testDir` (default: the folder with the config file) for files that match `testMatch`. The default pattern matches files ending in `.spec.ts`, `.test.ts`, `.spec.js`, `.test.js` and similar.

```ts
export default defineConfig({
  testDir: "./e2e",
  testMatch: "**/*.e2e.ts",
  testIgnore: "**/drafts/**",
});
```

## 56: What timeouts does Playwright have?

The main ones:

| Timeout            | Default | Set with                                 |
| ------------------ | ------- | ---------------------------------------- |
| Test timeout       | 30 s    | `timeout` in config, `test.setTimeout()` |
| Assertion timeout  | 5 s     | `expect: { timeout }` in config          |
| Action timeout     | none    | `use: { actionTimeout }`                 |
| Navigation timeout | none    | `use: { navigationTimeout }`             |
| Global timeout     | none    | `globalTimeout` in config                |

The test timeout covers the test and its `beforeEach`/`afterEach` hooks and fixtures. Actions and navigations have no own limit by default, so they are only stopped by the test timeout.

## 57: How do you change the timeout for one test?

```ts
test("long report", async ({ page }) => {
  test.setTimeout(120_000);
  // ...
});
```

For a single assertion or action, pass `timeout`:

```ts
await expect(page.getByText("Report ready")).toBeVisible({ timeout: 30_000 });
await page.getByRole("button", { name: "Export" }).click({ timeout: 10_000 });
```

## 58: What are projects in Playwright?

A project is a group of tests that run with the same settings. The most common use is running the same tests in several browsers:

```ts
projects: [
  { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
  { name: 'webkit', use: { ...devices['Desktop Safari'] } },
  { name: 'mobile', use: { ...devices['Pixel 7'] } },
],
```

Projects can also have different `testDir`, `retries`, `grep` or environment settings, and they can depend on each other (for example, a setup project that logs in first).

## 59: What is the devices object?

`devices` is a list of ready-made settings for popular browsers and phones. Each entry sets the viewport, user agent, device scale factor, `isMobile`, `hasTouch` and the default browser.

```ts
import { devices } from '@playwright/test';

{ name: 'iphone', use: { ...devices['iPhone 15'] } }
```

You can use it per project in the config or per file with `test.use({ ...devices['Pixel 7'] })`.

## 60: What is the use section in the config?

`use` sets options for the built-in fixtures: browser, context and page settings. Anything in `use` applies to all tests, and you can override it per project, per file or per `describe` block.

```ts
use: {
  baseURL: 'http://localhost:3000',
  headless: true,
  viewport: { width: 1280, height: 720 },
  locale: 'en-US',
  screenshot: 'only-on-failure',
  video: 'retain-on-failure',
  trace: 'on-first-retry',
},
```

## 61: How do you override options for a file or group?

Use `test.use()` at the top of the file or inside a `describe`:

```ts
test.use({ locale: "de-DE", timezoneId: "Europe/Berlin" });

test.describe("dark mode", () => {
  test.use({ colorScheme: "dark" });
  test("header looks right", async ({ page }) => {});
});
```

`test.use()` can't be called inside a test, because the options are needed before the fixtures are created.

## 62: How do you set the viewport size?

In the config or with `test.use()`:

```ts
use: { viewport: { width: 1920, height: 1080 } }
```

Or change it during a test:

```ts
await page.setViewportSize({ width: 375, height: 812 });
```

The default viewport is 1280x720.

## 63: How do you take screenshots automatically when a test fails?

Set `screenshot` in `use`:

```ts
use: {
  screenshot: "only-on-failure";
}
```

Options are `'off'`, `'on'`, `'only-on-failure'` and `'on-first-failure'`. The screenshots are saved in the `test-results` folder and attached to the HTML report.

## 64: How do you record videos of tests?

```ts
use: {
  video: "retain-on-failure";
}
```

Common values:

- `'off'`: no video (default)
- `'on'`: record every test
- `'retain-on-failure'`: record every test, keep only failed ones
- `'on-first-retry'`: record only when retrying a failed test

Videos are saved as `.webm` files and attached to the report. Recording slows tests down a bit, so most teams only keep videos for failures.

## 65: What is a trace in Playwright?

A trace is a recording of a test run that you open in the Trace Viewer. It contains:

- every action and assertion, with timing
- DOM snapshots before and after each action
- screenshots (a filmstrip)
- network requests
- console logs
- the test source code

```ts
use: {
  trace: "on-first-retry";
}
```

Traces are the best tool for debugging tests that failed in CI, because you can see exactly what happened without running the test again.

## 66: How do you open a trace?

From the HTML report, click the trace icon of a test. Or open the file directly:

```bash
npx playwright show-trace test-results/my-test/trace.zip
```

You can also drag a trace file to `trace.playwright.dev`, which runs fully in the browser and doesn't upload the trace anywhere.

## 67: What does the retries option do?

`retries` sets how many times a failed test is run again:

```ts
export default defineConfig({
  retries: process.env.CI ? 2 : 0,
});
```

If a test fails and then passes on a retry, it is marked as **flaky** in the report. Retries help keep CI green, but they hide problems if nobody looks at the flaky tests. You can also retry from the CLI with `--retries=2`.

## 68: What are workers?

Workers are separate OS processes that run tests in parallel. Each worker starts its own browser. By default Playwright uses half of the CPU cores.

```ts
export default defineConfig({
  workers: process.env.CI ? 2 : undefined,
});
```

```bash
npx playwright test --workers=4
npx playwright test --workers=1   # run one at a time
```

## 69: What does fullyParallel do?

By default, files run in parallel but tests inside one file run one after another in the same worker. With `fullyParallel: true`, tests inside a file are also spread across workers.

```ts
export default defineConfig({
  fullyParallel: true,
});
```

This makes runs faster, but every test must be independent and not rely on state left by a previous test in the same file.

## 70: Which reporters does Playwright have?

Built-in reporters:

- `list`: one line per test (default locally)
- `line`: one line that updates
- `dot`: a dot per test (default on CI)
- `html`: an interactive web report
- `json`: results as JSON
- `junit`: JUnit XML for CI tools
- `github`: annotations in GitHub Actions
- `blob`: raw results, used to merge sharded reports

```ts
reporter: [['list'], ['html', { open: 'never' }]],
```

```bash
npx playwright test --reporter=dot
```

## 71: How do you open the HTML report?

```bash
npx playwright show-report
```

By default the report opens automatically if tests fail locally. The report lets you filter by status, browser and tag, see errors and steps, and open screenshots, videos and traces for each test.

## 72: What is codegen?

Codegen opens a browser and records your actions as Playwright code. It picks good locators (role, text, test id) for you.

```bash
npx playwright codegen http://localhost:3000
npx playwright codegen --device="iPhone 15" playwright.dev
```

It's a good way to get started on a test or to find a locator for a hard element. The generated code still needs cleaning up and real assertions.

## 73: What is UI mode?

UI mode is an interactive app for running and debugging tests:

```bash
npx playwright test --ui
```

In UI mode you can:

- see all tests and run them one by one or in groups
- watch files and rerun tests when they change
- step through a test with DOM snapshots (like a live trace)
- pick locators from the page
- see network requests, console logs and errors

It is the most comfortable way to work on tests locally.

## 74: How do you debug a test with the Playwright Inspector?

Run the test with `--debug`:

```bash
npx playwright test login.spec.ts --debug
```

This opens a headed browser and the Playwright Inspector. The test stops before the first action, and you can step through each action, see which element a locator matches, and edit locators live. You can also set `PWDEBUG=1` to get the same behavior.

## 75: What does page.pause do?

`page.pause()` stops the test and opens the Inspector at that point, so you can look at the page and try locators.

```ts
test("debug me", async ({ page }) => {
  await page.goto("/checkout");
  await page.pause();
  await page.getByRole("button", { name: "Pay" }).click();
});
```

It only works in headed mode. Don't forget to remove it before you commit.

## 76: What does the VS Code extension for Playwright do?

The official "Playwright Test for VSCode" extension lets you:

- run and debug tests from the editor gutter or Test Explorer
- set breakpoints and debug with the VS Code debugger
- record new tests with codegen ("Record new")
- pick locators from the browser ("Pick locator")
- show the browser while running, and open traces

It reads your `playwright.config.ts`, so projects and settings are the same as on the command line.

## 77: What are Browser, BrowserContext and Page?

- **Browser**: a running browser instance (Chromium, Firefox or WebKit). Launching it is relatively slow.
- **BrowserContext**: an isolated session inside the browser, like a fresh incognito profile. It has its own cookies, local storage, cache and permissions. Creating one is fast.
- **Page**: a single tab inside a context.

```ts
const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
```

In Playwright Test, the browser is shared per worker, and each test gets its own context and page.

## 78: Why does each test get its own browser context?

Isolation. A new context has no cookies, storage or cache from other tests, so one test can't break another by leaving the user logged in or adding items to a cart.

Since creating a context takes only a few milliseconds, you get full isolation without the cost of starting a new browser for each test.

## 79: How do you open a second page in the same test?

Create a new page from the same context, so it shares cookies and storage:

```ts
test("two tabs", async ({ page, context }) => {
  await page.goto("/inbox");
  const page2 = await context.newPage();
  await page2.goto("/settings");
});
```

To simulate two different users, create a second context with `browser.newContext()`.

## 80: How do you take a screenshot?

```ts
await page.screenshot({ path: "home.png" });
await page.screenshot({ path: "full.png", fullPage: true });

// only one element
await page.getByTestId("chart").screenshot({ path: "chart.png" });
```

`screenshot()` also returns a `Buffer`, which you can attach to the report with `testInfo.attach()`.

## 81: How do you get the page title and URL?

```ts
const title = await page.title();
const url = page.url(); // not async
```

In tests, prefer the assertions `toHaveTitle` and `toHaveURL`, because they wait for the value to change.

## 82: How do you go back, forward or reload?

```ts
await page.goBack();
await page.goForward();
await page.reload();
```

Each of these waits for the navigation to finish, like `goto`.

## 83: How do you wait for a navigation to finish?

Usually you don't need to: the next action or assertion will wait. When you need to be sure the URL changed, use `waitForURL` or `toHaveURL`:

```ts
await page.getByRole("button", { name: "Login" }).click();
await page.waitForURL("**/dashboard");
// or
await expect(page).toHaveURL(/dashboard/);
```

`waitForURL` accepts a string, glob, regex or a function.

## 84: What does waitForLoadState do?

It waits until the page reaches a load state:

- `'load'`: the `load` event fired (default)
- `'domcontentloaded'`: the `DOMContentLoaded` event fired
- `'networkidle'`: no network requests for at least 500 ms

```ts
await page.waitForLoadState("domcontentloaded");
```

Playwright discourages `'networkidle'` for tests, because apps with polling or analytics may never become idle, and it doesn't tell you the page is ready. Waiting for a specific element is more reliable.

## 85: Why should you avoid waitForTimeout?

`page.waitForTimeout(3000)` just sleeps. It makes tests slow when the app is fast and still flaky when the app is slower than the sleep.

Instead, wait for something that shows the app is ready:

```ts
// bad
await page.waitForTimeout(3000);

// good
await expect(page.getByText("Order placed")).toBeVisible();
```

`waitForTimeout` is fine for debugging, but shouldn't stay in a real test.

## 86: How do you read the text or value of an element?

```ts
const text = await page.getByTestId("price").textContent(); // raw textContent
const visible = await page.getByTestId("price").innerText(); // rendered text
const value = await page.getByLabel("Email").inputValue(); // input value
const href = await page.getByRole("link").first().getAttribute("href");
```

These don't retry. Use them when you need the value in code, for example to use it in the next step. To check a value, use assertions like `toHaveText` or `toHaveValue` instead.

## 87: How do you get the text of all matching elements?

```ts
const names = await page.getByRole("listitem").allTextContents();
const visibleNames = await page.getByRole("listitem").allInnerTexts();
```

Or loop over the locators:

```ts
for (const row of await page.getByRole("row").all()) {
  console.log(await row.textContent());
}
```

`all()` doesn't wait for elements to appear, so make sure the list has loaded first (for example with `toHaveCount`).

## 88: How do you pick the first, last or nth element?

```ts
page.getByRole("listitem").first();
page.getByRole("listitem").last();
page.getByRole("listitem").nth(2); // zero-based, the third item
```

These are easy to use but fragile, since the order can change. When possible, filter by text or other content instead.

## 89: How do you filter locators?

Use `filter()` with text or with another locator:

```ts
// the row that contains "Alice"
const row = page.getByRole("row").filter({ hasText: "Alice" });
await row.getByRole("button", { name: "Edit" }).click();

// the product card that has a "Sale" badge
page.locator(".product").filter({ has: page.getByText("Sale") });

// items without "Archived"
page.getByRole("listitem").filter({ hasNotText: "Archived" });
```

## 90: How do you chain locators?

Call a locator method on another locator to search inside it:

```ts
const dialog = page.getByRole("dialog", { name: "Edit profile" });
await dialog.getByLabel("Name").fill("Bob");
await dialog.getByRole("button", { name: "Save" }).click();
```

This narrows the search to the dialog, so a "Save" button elsewhere on the page doesn't cause a conflict.

## 91: What is strict mode for locators?

Locators are strict: if an action like `click()` or `fill()` matches more than one element, Playwright throws an error instead of picking one.

```
Error: strict mode violation: getByRole('button', { name: 'Delete' }) resolved to 3 elements
```

This protects you from clicking the wrong element. Fix it by making the locator more specific (chain it inside a row, use `filter`, use `exact: true`), or use `first()`/`nth()` when you really mean "any of them". Assertions like `toHaveCount` and methods like `count()` or `all()` work with many elements.

## 92: How do you work with iframes?

Use `frameLocator()` or `contentFrame()` to get into the frame, then use locators as usual:

```ts
const frame = page.frameLocator("#payment-iframe");
await frame.getByLabel("Card number").fill("4242424242424242");

// same thing with contentFrame
await page
  .locator("#payment-iframe")
  .contentFrame()
  .getByLabel("CVC")
  .fill("123");
```

Playwright can reach into cross-origin iframes as well.

## 93: How do you handle alert, confirm and prompt dialogs?

By default, Playwright dismisses dialogs automatically. To handle one yourself, add a listener before the action that opens it:

```ts
page.once("dialog", async (dialog) => {
  expect(dialog.message()).toBe("Delete this item?");
  await dialog.accept(); // or dialog.dismiss()
});
await page.getByRole("button", { name: "Delete" }).click();
```

For a `prompt()`, pass the text: `dialog.accept('my answer')`.

## 94: How do you handle a link that opens a new tab?

Wait for the `page` event on the context while clicking:

```ts
const pagePromise = context.waitForEvent("page");
await page.getByRole("link", { name: "Open docs" }).click();
const newPage = await pagePromise;

await newPage.waitForLoadState();
await expect(newPage).toHaveTitle(/Docs/);
```

For a `window.open()` popup from a page, you can also use `page.waitForEvent('popup')`.

## 95: How do you test a file download?

Start waiting for the `download` event, then click:

```ts
const downloadPromise = page.waitForEvent("download");
await page.getByRole("button", { name: "Export CSV" }).click();
const download = await downloadPromise;

expect(download.suggestedFilename()).toBe("report.csv");
await download.saveAs("downloads/" + download.suggestedFilename());
```

Downloaded files are deleted when the browser context closes, so save them if you need them.

## 96: How do you use the keyboard API?

`page.keyboard` sends low-level key events to whatever is focused:

```ts
await page.keyboard.type("Hello"); // types text
await page.keyboard.press("Shift+Tab");
await page.keyboard.down("Shift");
await page.keyboard.press("ArrowDown");
await page.keyboard.up("Shift");
await page.keyboard.insertText("ąčę"); // inserts text without key events
```

For most cases, `locator.fill()` and `locator.press()` are simpler.

## 97: How do you use the mouse API?

`page.mouse` works with coordinates:

```ts
await page.mouse.move(100, 200);
await page.mouse.down();
await page.mouse.move(300, 200, { steps: 10 });
await page.mouse.up();
await page.mouse.wheel(0, 500); // scroll down
await page.mouse.click(50, 50);
```

It is useful for drawing on a canvas, sliders or custom drag and drop. For normal elements use locator actions.

## 98: How do you drag and drop?

```ts
await page.getByText("Task 1").dragTo(page.getByTestId("done-column"));
```

`dragTo` moves the mouse from the center of the source to the center of the target. If the app uses a library that needs more mouse events, do it manually with `hover()`, `page.mouse.down()`, `hover()` on the target and `page.mouse.up()`.

## 99: How do you scroll in Playwright?

Usually you don't need to: actions scroll the element into view automatically. When you do need it:

```ts
await page.getByText("Footer link").scrollIntoViewIfNeeded();
await page.mouse.wheel(0, 1000);
await page
  .getByTestId("list")
  .evaluate((el) => (el.scrollTop = el.scrollHeight));
```

## 100: What is the difference between isVisible and toBeVisible?

`locator.isVisible()` returns `true` or `false` right away, without waiting. `expect(locator).toBeVisible()` retries until the element is visible or the timeout passes.

```ts
// checks once
if (await page.getByText("Cookie banner").isVisible()) {
  await page.getByRole("button", { name: "Accept" }).click();
}

// waits for it
await expect(page.getByText("Saved")).toBeVisible();
```

Use `isVisible()` only for optional branches. For checks, always use the assertion.

## 101: What is testInfo?

`testInfo` is an object with information about the running test. You get it as the second argument of a test or hook, or with `test.info()`.

```ts
test("example", async ({ page }, testInfo) => {
  console.log(testInfo.title); // test title
  console.log(testInfo.project.name); // project name
  console.log(testInfo.retry); // 0 on first run, 1 on first retry
  await testInfo.attach("note", { body: "hello", contentType: "text/plain" });
});
```

It also has `status`, `expectedStatus`, `outputDir`, `outputPath()`, `annotations` and `workerIndex`.

## 102: What is test.step?

`test.step` splits a test into named steps that show up in the report, UI mode and trace. It makes long tests easier to read and failures easier to find.

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

A step can return a value, and steps can be nested.

## 103: How do you use environment variables in Playwright tests?

Read them with `process.env`. Many projects load a `.env` file with `dotenv` at the top of the config:

```ts
// playwright.config.ts
import "dotenv/config";
import { defineConfig } from "@playwright/test";

export default defineConfig({
  use: { baseURL: process.env.BASE_URL ?? "http://localhost:3000" },
});
```

```bash
BASE_URL=https://staging.example.com npx playwright test
```

Keep secrets like passwords in environment variables or CI secrets, never in the test code.

## 104: Do you need to compile TypeScript before running Playwright tests?

No. Playwright Test transforms TypeScript on the fly, so you can run `.ts` tests directly with `npx playwright test`. It only strips types, it doesn't type-check. To catch type errors, run `tsc --noEmit` separately, for example in CI.

You can also write tests in plain JavaScript. The API is the same, you just lose the type checking and autocomplete.

## 105: What happens if you forget to await a Playwright call?

Most Playwright methods return promises. If you forget `await`, the test moves on without waiting, and you get odd results: an action that runs after the test ended, an assertion that never really runs, or errors like "Target page, context or browser has been closed".

```ts
// bug: assertion is never awaited, test may pass even if it should fail
expect(page.getByText("Saved")).toBeVisible();

// correct
await expect(page.getByText("Saved")).toBeVisible();
```

Turn on the `@typescript-eslint/no-floating-promises` lint rule to catch this.

## 106: How does Playwright compare to Selenium?

|             | Playwright                                                     | Selenium                              |
| ----------- | -------------------------------------------------------------- | ------------------------------------- |
| Protocol    | own protocol over a WebSocket to patched/instrumented browsers | WebDriver (W3C standard), plus BiDi   |
| Waiting     | auto-waits for elements, retrying assertions                   | mostly manual explicit waits          |
| Test runner | built-in (`@playwright/test`)                                  | none, use JUnit, pytest, etc.         |
| Browsers    | Chromium, Firefox, WebKit                                      | all major browsers, incl. real Safari |
| Isolation   | cheap browser contexts                                         | usually a new browser session         |
| Tools       | codegen, trace viewer, UI mode                                 | Selenium IDE, Grid                    |

Playwright is usually faster and less flaky to write tests with. Selenium has a longer history, more language bindings, and works with real branded browsers and device clouds through WebDriver.

## 107: How does Playwright compare to Cypress?

- **Architecture**: Cypress runs your test code inside the browser next to the app. Playwright runs tests in Node.js and controls the browser from outside.
- **Multiple tabs and origins**: Playwright handles them easily. Cypress has limits (`cy.origin()` for other domains, no real multi-tab).
- **Browsers**: Playwright supports WebKit. Cypress supports Chromium-based browsers and Firefox, with WebKit only experimental.
- **Parallelism**: free and built in for Playwright. Cypress parallelization across machines is mainly through its paid Cloud.
- **Syntax**: Playwright uses normal `async/await`. Cypress uses its own command chain.

Cypress has a very good interactive runner and component testing. Playwright is usually faster and more flexible.

## 108: How is Playwright different from Puppeteer?

Puppeteer was made by the Chrome team and focuses on Chrome and Firefox. Some of the same people later built Playwright at Microsoft, so the APIs look similar.

Playwright adds WebKit support, a full test runner, locators with auto-waiting, web-first assertions, browser contexts as the main isolation model, tracing and codegen. Puppeteer is a lower-level library and you bring your own test runner.

## 109: How do you list tests without running them?

```bash
npx playwright test --list
npx playwright test --list --grep @smoke
```

It prints every test that would run, with its project. It is useful to check that your filters and config pick the right tests.

## 110: How do you check and update the Playwright version?

```bash
npx playwright --version
npm install -D @playwright/test@latest
npx playwright install --with-deps
```

After updating the package you must install the matching browsers. If you use the Playwright Docker image in CI, update its tag to the same version too, otherwise the browsers won't match.

## 111: What is slowMo?

`slowMo` slows down every Playwright operation by the given number of milliseconds. It helps you watch what a test does in headed mode.

```ts
use: {
  launchOptions: { slowMo: 500 },
},
```

It is only for debugging. Don't use it to "fix" flaky tests.

## 112: How do you run tests in Google Chrome or Microsoft Edge instead of Chromium?

Use the `channel` option:

```ts
projects: [
  { name: 'chrome', use: { ...devices['Desktop Chrome'], channel: 'chrome' } },
  { name: 'edge', use: { ...devices['Desktop Edge'], channel: 'msedge' } },
],
```

The branded browser must be installed on the machine. You can install it with `npx playwright install chrome` or `npx playwright install msedge`.

## 113: How do you test some HTML without a server?

Use `page.setContent()`:

```ts
test("button works", async ({ page }) => {
  await page.setContent(`
    <button onclick="this.textContent = 'Clicked'">Click me</button>
  `);
  await page.getByRole("button").click();
  await expect(page.getByRole("button")).toHaveText("Clicked");
});
```

`page.content()` does the opposite and returns the full HTML of the page.

## 114: How do you run JavaScript in the page?

Use `page.evaluate()`. The function runs in the browser, and the return value is sent back to Node.js:

```ts
const width = await page.evaluate(() => window.innerWidth);

const total = await page.evaluate(([a, b]) => a + b, [1, 2]);

await page.evaluate(() => localStorage.setItem("token", "abc"));
```

The function can't use variables from your test file directly. Pass them as an argument.

## 115: How do you read console messages from the page?

Listen to the `console` event:

```ts
page.on("console", (msg) => {
  console.log(`[${msg.type()}] ${msg.text()}`);
});
await page.goto("/");
```

You can also collect errors and fail the test if any appeared:

```ts
const errors: string[] = [];
page.on("console", (msg) => {
  if (msg.type() === "error") errors.push(msg.text());
});
await page.goto("/");
expect(errors).toEqual([]);
```

## 116: How do you catch uncaught JavaScript errors on the page?

Listen to `pageerror`:

```ts
const errors: Error[] = [];
page.on("pageerror", (error) => errors.push(error));

await page.goto("/");
await page.getByRole("button", { name: "Load" }).click();

expect(errors).toHaveLength(0);
```

`pageerror` fires for exceptions that nothing on the page caught, which are often real bugs.

## 117: How do you test a REST API with Playwright?

Use the `request` fixture. It sends HTTP requests without a browser and uses `baseURL` from the config:

```ts
test("create a todo", async ({ request }) => {
  const response = await request.post("/api/todos", {
    data: { title: "Buy milk" },
  });
  expect(response.status()).toBe(201);

  const todo = await response.json();
  expect(todo.title).toBe("Buy milk");
});
```

There are methods for `get`, `post`, `put`, `patch`, `delete`, `head` and `fetch`.

## 118: What does toBeOK check?

`toBeOK()` checks that an API response has a status in the 200-299 range:

```ts
const response = await request.get("/api/health");
await expect(response).toBeOK();
```

If it fails, the error includes the response details, which makes it more useful than `expect(response.ok()).toBe(true)`.

## 119: What do toBeEmpty, toBeFocused and toBeEditable check?

```ts
await expect(page.getByLabel("Search")).toBeEmpty(); // empty input or no text
await expect(page.getByLabel("Email")).toBeFocused(); // has keyboard focus
await expect(page.getByLabel("Username")).toBeEditable(); // enabled and not readonly
```

`toBeFocused` is handy for accessibility tests, for example checking that focus moves into a dialog when it opens.

## 120: How do you check a CSS property?

Use `toHaveCSS` with the computed value:

```ts
await expect(page.getByRole("button", { name: "Delete" })).toHaveCSS(
  "background-color",
  "rgb(220, 38, 38)",
);
await expect(page.getByTestId("sidebar")).toHaveCSS("display", "none");
```

The browser returns computed values, so colors are in `rgb()` format, not hex or names.

## 121: What is the difference between toBeAttached, toBeVisible and toBeInViewport?

- `toBeAttached()`: the element is in the DOM, visible or not.
- `toBeVisible()`: the element is in the DOM and visible (has size, not hidden by CSS).
- `toBeInViewport()`: the element is visible and inside the current viewport, so the user can see it without scrolling.

```ts
await expect(page.locator("input[type=hidden]")).toBeAttached();
await expect(page.getByText("Back to top")).toBeInViewport();
await expect(page.getByTestId("ad")).toBeInViewport({ ratio: 0.5 });
```

## 122: How do you check accessible names and roles?

```ts
const button = page.getByTestId("close");
await expect(button).toHaveAccessibleName("Close dialog");
await expect(button).toHaveRole("button");
await expect(page.getByLabel("Email")).toHaveAccessibleDescription(
  "We never share it",
);
```

These are useful when you use test ids but still want to check the element is accessible.

## 123: What does locator.waitFor do?

`waitFor()` waits until the element reaches a state: `'attached'`, `'detached'`, `'visible'` (default) or `'hidden'`.

```ts
await page.getByText("Loading").waitFor({ state: "hidden" });
const value = await page.getByTestId("result").textContent();
```

In tests you usually prefer an assertion like `toBeHidden()`. `waitFor` is useful in Page Objects or scripts when you need to wait but don't want an assertion.

## 124: What are page.waitForSelector and page.$ and should you still use them?

These are older APIs. `page.$()` and `page.$$()` return `ElementHandle`s, and `page.waitForSelector()` waits for a selector and returns a handle.

```ts
// legacy
const el = await page.$("#submit");
await el?.click();

// modern
await page.locator("#submit").click();
```

Element handles point to one specific DOM node. If the framework re-renders it, the handle is stale. Locators search again each time, auto-wait and are strict, so Playwright recommends them. You'll still see the old APIs in older code.

## 125: How do you clear an input, focus or blur an element?

```ts
await page.getByLabel("Name").clear();
await page.getByLabel("Name").focus();
await page.getByLabel("Name").blur();
```

`clear()` is the same as `fill('')`. `blur()` is useful to trigger "on blur" validation.

## 126: How do you tap on a mobile device?

Use `tap()`. It needs `hasTouch: true`, which mobile entries in `devices` already set:

```ts
test.use({ ...devices["iPhone 15"] });

test("tap menu", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Menu" }).tap();
});
```

`click()` also works on mobile emulation, but `tap()` fires touch events, which some apps need.

## 127: What does dispatchEvent do?

It fires a DOM event on the element directly, without moving the mouse or doing actionability checks:

```ts
await page.getByRole("button").dispatchEvent("click");
await page.getByTestId("zone").dispatchEvent("dragstart", { dataTransfer });
```

It is useful for events that are hard to trigger normally. For normal clicks, prefer `click()`, because it behaves like a real user.

## 128: What are the test-results and playwright-report folders?

- `test-results/` holds artifacts from the last run: screenshots, videos, traces and other files, in one folder per test. It is cleaned at the start of each run. You can change it with `outputDir`.
- `playwright-report/` holds the HTML report.

Add both to `.gitignore`, together with `blob-report/` and `playwright/.auth/` if you store login state there.

## 129: How do you test with a different language or time zone?

Set `locale` and `timezoneId`:

```ts
test.use({ locale: "fr-FR", timezoneId: "Europe/Paris" });

test("shows french date", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByTestId("date")).toContainText("janvier");
});
```

`locale` changes `navigator.language`, the `Accept-Language` header and number/date formatting. `timezoneId` changes the browser's time zone.

## 130: How do you test dark mode?

Set `colorScheme`:

```ts
test.use({ colorScheme: "dark" });
```

Or change it during the test:

```ts
await page.emulateMedia({ colorScheme: "dark" });
```

This makes `prefers-color-scheme: dark` media queries match.

## 131: How do you set geolocation and permissions?

```ts
test.use({
  geolocation: { latitude: 41.7151, longitude: 44.8271 },
  permissions: ["geolocation"],
});

test("shows nearby stores", async ({ page, context }) => {
  await page.goto("/stores");
  await context.setGeolocation({ latitude: 40.7128, longitude: -74.006 }); // change later
});
```

Other permissions you can grant include `'notifications'`, `'clipboard-read'`, `'clipboard-write'` and `'camera'`, depending on the browser.

## 132: How do you emulate a mobile device?

Use one of the `devices` entries:

```ts
import { test, devices } from "@playwright/test";

test.use({ ...devices["Pixel 7"] });
```

This sets the viewport, user agent, device scale factor, `isMobile` and `hasTouch`. Keep in mind this is emulation in a desktop browser engine. It's good for layout and touch tests, but it's not a real phone.

## 133: How do you test offline behavior?

```ts
test("shows offline banner", async ({ page, context }) => {
  await page.goto("/");
  await context.setOffline(true);
  await page.getByRole("button", { name: "Refresh" }).click();
  await expect(page.getByText("You are offline")).toBeVisible();
  await context.setOffline(false);
});
```

You can also start offline with `test.use({ offline: true })`.

## 134: How do you set a custom user agent?

```ts
test.use({ userAgent: "MyTestBot/1.0" });
```

Keep in mind that `devices` entries already set a user agent. If you spread a device and also set `userAgent`, put yours after the spread so it wins.

## 135: How do you add or read cookies?

Cookies belong to the browser context:

```ts
await context.addCookies([
  { name: "consent", value: "yes", domain: "localhost", path: "/" },
]);

const cookies = await context.cookies();
expect(cookies.find((c) => c.name === "session")).toBeDefined();

await context.clearCookies();
```

## 136: How do you read or change localStorage?

Use `page.evaluate()`:

```ts
await page.goto("/");
await page.evaluate(() => localStorage.setItem("onboarding-done", "true"));
await page.reload();

const theme = await page.evaluate(() => localStorage.getItem("theme"));
```

To set it before any page script runs, use `context.addInitScript()` or a saved `storageState`.

## 137: How do you use Playwright without the test runner?

Install `playwright` and launch a browser yourself:

```ts
import { chromium } from "playwright";

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto("https://example.com");
await page.screenshot({ path: "example.png" });
await browser.close();
```

This is useful for scripts like scraping, screenshots or PDF generation. For tests, use `@playwright/test`, which handles browsers, contexts, retries and reports for you.

## 138: What is a flaky test?

A flaky test passes sometimes and fails sometimes without any code change. Common causes are:

- timing problems (acting before the page is ready, fixed sleeps)
- tests depending on each other or on shared data
- unstable locators
- slow or random backend responses
- animations
- time and date logic

Playwright marks a test as flaky when it fails and then passes on retry. Flaky tests should be fixed, not just retried, because people stop trusting a suite that fails randomly.

## 139: In what order do hooks and fixtures run?

For each test, roughly:

1. Worker fixtures and `beforeAll` hooks (once per worker)
2. Test fixtures the test needs (like `page`)
3. `beforeEach` hooks, outer `describe` first
4. The test
5. `afterEach` hooks, inner `describe` first
6. Test fixture teardown
7. `afterAll` hooks and worker fixture teardown when the worker finishes

Fixtures are set up only when a test or hook asks for them.

## 140: Can you use Playwright with Jest or Vitest?

You can use the Playwright library (`playwright`) from any Node test runner. But the Playwright team recommends `@playwright/test` for E2E tests, because it gives you fixtures, browser contexts per test, web-first assertions, parallel workers, retries, traces and reports out of the box.

Vitest has a browser mode that can use Playwright as its browser provider. That is for running unit and component tests in a real browser, not for writing Playwright E2E tests.

## 141: How do you log network requests?

```ts
page.on("request", (request) =>
  console.log(">>", request.method(), request.url()),
);
page.on("response", (response) =>
  console.log("<<", response.status(), response.url()),
);
page.on("requestfailed", (request) =>
  console.log("failed", request.url(), request.failure()?.errorText),
);
```

For debugging, the network tab in the trace viewer and UI mode is usually easier than logging.

## 142: What does the exact option do in getBy methods?

By default, text matching in `getByText`, `getByLabel`, `getByRole` name and similar is a case-insensitive substring match. `exact: true` makes it a case-sensitive, full-string match.

```ts
page.getByRole("button", { name: "Save" }); // also matches "Save draft"
page.getByRole("button", { name: "Save", exact: true }); // only "Save"
```

This is a common fix for strict mode violations.

## 143: How do you find headings, rows or cells with getByRole?

```ts
page.getByRole("heading", { name: "Orders", level: 2 });

const row = page.getByRole("row", { name: /Order #1042/ });
await expect(row.getByRole("cell").nth(2)).toHaveText("Shipped");

page.getByRole("tab", { selected: true });
page.getByRole("checkbox", { checked: true });
page.getByRole("button", { pressed: true });
page.getByRole("treeitem", { expanded: false });
```

`getByRole` has options for ARIA states like `checked`, `selected`, `expanded`, `pressed`, `disabled` and `level`.

## 144: Can you use regular expressions in locators?

Yes. Most text options accept a regex:

```ts
page.getByRole("button", { name: /sign (in|up)/i });
page.getByText(/^Total: \$\d+\.\d{2}$/);
page.getByRole("listitem").filter({ hasText: /out of stock/i });
await expect(page).toHaveURL(/\/orders\/\d+/);
```

Regex is useful for dynamic text like ids, prices and dates.

## 145: What is the difference between page.locator and the getBy methods?

`page.locator(selector)` takes a CSS or XPath selector (or other Playwright selector engines). The `getBy*` methods are built-in helpers that find elements by what users see: role, text, label, placeholder, alt text, title, test id.

Both return a `Locator`, and you can mix them:

```ts
page.locator(".sidebar").getByRole("link", { name: "Settings" });
```

Prefer the `getBy*` methods and use `locator()` for cases they don't cover.

## 146: How do you send extra HTTP headers with every request?

```ts
use: {
  extraHTTPHeaders: {
    'x-test-run': 'e2e',
    Authorization: `Bearer ${process.env.API_TOKEN}`,
  },
},
```

These headers are sent by the browser and by the `request` fixture. You can also set them on a page with `page.setExtraHTTPHeaders()`.

## 147: What is the Pick locator feature?

"Pick locator" lets you hover over an element in the browser and see the locator Playwright would use for it. You find it in the Inspector, UI mode, the trace viewer and the VS Code extension.

It is a quick way to get a good locator for a hard element, and you can copy it straight into your test.

## 148: How do you handle a cookie consent banner?

A few options, from best to worst:

1. Set the consent cookie or local storage before the test, so the banner never shows (`context.addCookies()` or a saved `storageState`).
2. Dismiss it in a fixture or `beforeEach`.
3. Use `page.addLocatorHandler()` to close it automatically whenever it appears and blocks an action.

```ts
await context.addCookies([
  { name: "cookie_consent", value: "accepted", url: "http://localhost:3000" },
]);
```

## 149: How should you organize test files?

A common layout:

```
tests/
  auth.setup.ts
  auth/
    login.spec.ts
  cart/
    add-to-cart.spec.ts
  checkout/
    checkout.spec.ts
pages/
  LoginPage.ts
  CartPage.ts
fixtures/
  index.ts
playwright.config.ts
```

Group tests by feature, keep page objects and fixtures in their own folders, and keep each test focused on one user flow. Smaller files also spread better across workers.

## 150: What makes a good Playwright test?

- It tests what the user sees and does, not implementation details.
- It uses user-facing locators (`getByRole`, `getByLabel`).
- It uses web-first assertions and never fixed sleeps.
- It is independent: it creates its own data and doesn't depend on other tests.
- It sets up state the fast way (API calls, saved login) and only uses the UI for what is being tested.
- It has a clear title and checks a clear result.
- It controls third-party things it doesn't own, like external APIs, with mocks.

---

# Moderate Questions (151-300)

## 151: What is the Page Object Model?

The Page Object Model (POM) is a pattern where each page or big component of the app gets a class. The class holds the locators and the actions for that page, and tests call those methods instead of using locators directly.

Benefits:

- If the UI changes, you update one class instead of many tests.
- Tests read more like user stories (`loginPage.login(user)`).
- Common steps are not copy-pasted.

The main risk is making page objects too big or putting assertions and logic in them that belong in tests.

## 152: How do you write a page object in Playwright?

```ts
// pages/LoginPage.ts
import { type Page, type Locator, expect } from "@playwright/test";

export class LoginPage {
  readonly email: Locator;
  readonly password: Locator;
  readonly submit: Locator;

  constructor(readonly page: Page) {
    this.email = page.getByLabel("Email");
    this.password = page.getByLabel("Password");
    this.submit = page.getByRole("button", { name: "Sign in" });
  }

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

```ts
test("user can log in", async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.goto();
  await loginPage.login("alice@example.com", "secret");
  await expect(page).toHaveURL("/dashboard");
});
```

Since locators are lazy, it's fine to create them in the constructor.

## 153: How do you combine page objects with fixtures?

Create the page objects in custom fixtures, so tests just ask for them:

```ts
// fixtures.ts
import { test as base } from "@playwright/test";
import { LoginPage } from "./pages/LoginPage";
import { CartPage } from "./pages/CartPage";

type Pages = { loginPage: LoginPage; cartPage: CartPage };

export const test = base.extend<Pages>({
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },
  cartPage: async ({ page }, use) => {
    await use(new CartPage(page));
  },
});
export { expect } from "@playwright/test";
```

```ts
import { test, expect } from "./fixtures";

test("login", async ({ loginPage }) => {
  await loginPage.goto();
  await loginPage.login("alice@example.com", "secret");
});
```

This removes the `new LoginPage(page)` boilerplate from every test.

## 154: How do you create a custom fixture?

Use `test.extend()`. Each fixture is an async function that gets other fixtures and a `use` function. Code before `use` is setup, `use(value)` passes the value to the test, and code after `use` is teardown.

```ts
import { test as base } from "@playwright/test";

type MyFixtures = { todoPage: TodoPage };

export const test = base.extend<MyFixtures>({
  todoPage: async ({ page }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.goto();
    await todoPage.addItem("first item");
    await use(todoPage);
    await todoPage.removeAll();
  },
});
```

## 155: How does fixture teardown work?

Everything after `await use(...)` runs after the test, even if the test failed. That makes fixtures a good place for cleanup:

```ts
export const test = base.extend<{ user: User }>({
  user: async ({ request }, use) => {
    const res = await request.post("/api/users", { data: { name: "temp" } });
    const user = await res.json();

    await use(user);

    await request.delete(`/api/users/${user.id}`);
  },
});
```

Setup and teardown stay in one place, which is easier to read than a `beforeEach` and `afterEach` pair.

## 156: What is a worker-scoped fixture?

By default, fixtures are test-scoped: created for each test. A worker-scoped fixture is created once per worker process and shared by all tests that run in that worker.

```ts
type WorkerFixtures = { dbConnection: Db };

export const test = base.extend<{}, WorkerFixtures>({
  dbConnection: [
    async ({}, use) => {
      const db = await connect(process.env.DB_URL!);
      await use(db);
      await db.close();
    },
    { scope: "worker" },
  ],
});
```

Use it for expensive things like a DB connection, a test account or a server. Worker fixtures can only depend on other worker fixtures.

## 157: What is an automatic fixture?

An automatic fixture runs for every test, even if the test doesn't ask for it. Set `auto: true`:

```ts
export const test = base.extend<{ logOnFailure: void }>({
  logOnFailure: [
    async ({ page }, use, testInfo) => {
      const logs: string[] = [];
      page.on("console", (msg) => logs.push(msg.text()));
      await use();
      if (testInfo.status !== testInfo.expectedStatus) {
        await testInfo.attach("console", {
          body: logs.join("\n"),
          contentType: "text/plain",
        });
      }
    },
    { auto: true },
  ],
});
```

It's useful for things every test should do, like collecting logs or checking for errors.

## 158: What is an option fixture?

An option fixture is a value you can set from the config or `test.use()`. Mark it with `option: true` and give it a default:

```ts
type Options = { defaultItem: string };

export const test = base.extend<Options>({
  defaultItem: ["Buy milk", { option: true }],
  todoPage: async ({ page, defaultItem }, use) => {
    const todoPage = new TodoPage(page);
    await todoPage.addItem(defaultItem);
    await use(todoPage);
  },
});
```

```ts
// playwright.config.ts
import type { Options } from "./fixtures";

export default defineConfig<Options>({
  projects: [{ name: "shopping", use: { defaultItem: "Buy eggs" } }],
});
```

## 159: How do you override a built-in fixture?

Define a fixture with the same name. For example, make every `page` go to the base URL first:

```ts
export const test = base.extend({
  page: async ({ page }, use) => {
    await page.goto("/");
    await use(page);
  },
});
```

You can also override options like `storageState`, `locale` or `baseURL` the same way, or compute them from other fixtures.

## 160: How do you combine fixtures from several modules?

Use `mergeTests` and `mergeExpects`:

```ts
import { mergeTests, mergeExpects } from "@playwright/test";
import { test as dbTest, expect as dbExpect } from "./db-fixtures";
import { test as a11yTest, expect as a11yExpect } from "./a11y-fixtures";

export const test = mergeTests(dbTest, a11yTest);
export const expect = mergeExpects(dbExpect, a11yExpect);
```

This lets teams keep fixtures in separate files and combine only the ones a test needs.

## 161: What is storageState?

`storageState` is a JSON snapshot of a browser context's cookies, local storage and, optionally, IndexedDB. You can save it after logging in and reuse it so tests start already logged in.

```ts
// save
await page.context().storageState({ path: "playwright/.auth/user.json" });

// reuse
test.use({ storageState: "playwright/.auth/user.json" });
```

Logging in once and reusing the state saves a lot of time compared to logging in through the UI in every test.

## 162: How do you log in once and reuse the session in all tests?

Create a setup project that logs in and saves the state, then make the other projects depend on it:

```ts
// tests/auth.setup.ts
import { test as setup, expect } from "@playwright/test";

const authFile = "playwright/.auth/user.json";

setup("authenticate", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill(process.env.USER_EMAIL!);
  await page.getByLabel("Password").fill(process.env.USER_PASSWORD!);
  await page.getByRole("button", { name: "Sign in" }).click();
  await expect(page.getByRole("button", { name: "Account" })).toBeVisible();
  await page.context().storageState({ path: authFile });
});
```

```ts
// playwright.config.ts
projects: [
  { name: 'setup', testMatch: /.*\.setup\.ts/ },
  {
    name: 'chromium',
    use: { ...devices['Desktop Chrome'], storageState: 'playwright/.auth/user.json' },
    dependencies: ['setup'],
  },
],
```

Add `playwright/.auth` to `.gitignore`, since the file contains real session cookies.

## 163: How do you test with several user roles?

Save one storage state per role in the setup project, then pick the role with `test.use()`:

```ts
setup("admin", async ({ page }) => {
  // log in as admin
  await page.context().storageState({ path: "playwright/.auth/admin.json" });
});
setup("user", async ({ page }) => {
  // log in as user
  await page.context().storageState({ path: "playwright/.auth/user.json" });
});
```

```ts
test.describe("admin panel", () => {
  test.use({ storageState: "playwright/.auth/admin.json" });
  test("can ban users", async ({ page }) => {});
});
```

For a test that needs both roles at once, create two contexts:

```ts
test("admin and user chat", async ({ browser }) => {
  const adminContext = await browser.newContext({
    storageState: "playwright/.auth/admin.json",
  });
  const userContext = await browser.newContext({
    storageState: "playwright/.auth/user.json",
  });
  const adminPage = await adminContext.newPage();
  const userPage = await userContext.newPage();
  // ...
  await adminContext.close();
  await userContext.close();
});
```

## 164: When should you use one account per worker instead of a shared account?

A shared account is fine when tests only read data. When tests change server state (settings, cart, profile), parallel tests using the same account can break each other.

In that case, use one account per worker with a worker-scoped fixture:

```ts
export const test = base.extend<{}, { workerStorageState: string }>({
  storageState: ({ workerStorageState }, use) => use(workerStorageState),

  workerStorageState: [
    async ({ browser }, use) => {
      const id = test.info().parallelIndex;
      const fileName = `playwright/.auth/user-${id}.json`;
      const page = await browser.newPage({ storageState: undefined });
      await page.goto("/login");
      await page.getByLabel("Email").fill(`user${id}@example.com`);
      await page.getByLabel("Password").fill(process.env.PASSWORD!);
      await page.getByRole("button", { name: "Sign in" }).click();
      await page.waitForURL("/dashboard");
      await page.context().storageState({ path: fileName });
      await page.close();
      await use(fileName);
    },
    { scope: "worker" },
  ],
});
```

`parallelIndex` goes from 0 to `workers - 1`, so you need that many test accounts.

## 165: What are globalSetup and globalTeardown?

They are files that run once before all tests and once after all tests:

```ts
export default defineConfig({
  globalSetup: "./global-setup.ts",
  globalTeardown: "./global-teardown.ts",
});
```

```ts
// global-setup.ts
import type { FullConfig } from "@playwright/test";

export default async function globalSetup(config: FullConfig) {
  await resetDatabase();
  process.env.RUN_ID = Date.now().toString();
}
```

A global setup can also return a function, which then works as the teardown.

## 166: Should you use globalSetup or a setup project?

Playwright recommends setup projects (with `dependencies`) for most cases, because:

- they show up in the HTML report
- they can be traced, so you can debug them in the trace viewer
- they can use fixtures like `page` and `request`
- they respect config options like `use`, `headless` and `baseURL`

`globalSetup` runs outside the test runner, so none of that is available. It's still fine for simple non-browser work like setting environment variables or starting a service. Setup projects can have a `teardown` project too.

## 167: How do you start your app before the tests run?

Use the `webServer` option. Playwright runs the command, waits until the URL responds, runs the tests, and then stops the server.

```ts
export default defineConfig({
  webServer: {
    command: "npm run start",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
  use: { baseURL: "http://localhost:3000" },
});
```

`reuseExistingServer: true` uses a server you already started locally, so you don't need to restart it every run.

## 168: How do you start several servers, like a frontend and an API?

Pass an array:

```ts
webServer: [
  {
    command: 'npm run start:api',
    url: 'http://localhost:4000/health',
    reuseExistingServer: !process.env.CI,
  },
  {
    command: 'npm run start:web',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
],
```

Other useful options are `cwd`, `env`, `stdout: 'pipe'` to see server logs, and `gracefulShutdown` to stop the server with a specific signal.

## 169: How do you mock an API response?

Use `page.route()` to intercept requests and `route.fulfill()` to answer them:

```ts
test("shows empty state", async ({ page }) => {
  await page.route("**/api/orders", (route) => route.fulfill({ json: [] }));
  await page.goto("/orders");
  await expect(page.getByText("No orders yet")).toBeVisible();
});
```

The route must be set up before the page makes the request, so add it before `goto` or before the click that triggers it.

## 170: What can you pass to route.fulfill?

```ts
await page.route("**/api/user", (route) =>
  route.fulfill({
    status: 200,
    contentType: "application/json",
    headers: { "x-mock": "1" },
    body: JSON.stringify({ name: "Alice" }),
  }),
);

// shortcut for JSON
await page.route("**/api/user", (route) =>
  route.fulfill({ json: { name: "Alice" } }),
);

// from a file
await page.route("**/api/products", (route) =>
  route.fulfill({ path: "mocks/products.json" }),
);

// error response
await page.route("**/api/pay", (route) =>
  route.fulfill({ status: 500, json: { error: "boom" } }),
);
```

## 171: How do you change a request before it is sent?

Use `route.continue()` with overrides:

```ts
await page.route("**/api/**", async (route) => {
  const headers = {
    ...route.request().headers(),
    "x-feature-flag": "new-checkout",
  };
  await route.continue({ headers });
});

await page.route("**/api/search", (route) =>
  route.continue({ postData: JSON.stringify({ query: "forced" }) }),
);
```

You can override `url`, `method`, `headers` and `postData`. The URL change can't switch the protocol.

## 172: How do you change a real response from the server?

Fetch the real response with `route.fetch()`, change it, and fulfill with it:

```ts
await page.route("**/api/products", async (route) => {
  const response = await route.fetch();
  const json = await response.json();
  json.push({ id: 999, name: "Test product", price: 0 });
  await route.fulfill({ response, json });
});
```

This keeps most of the real data but lets you add edge cases, like a very long product name or a missing field.

## 173: How do you block requests, for example images or analytics?

Use `route.abort()`:

```ts
// block images
await page.route("**/*.{png,jpg,jpeg,webp}", (route) => route.abort());

// block by resource type
await page.route("**/*", (route) =>
  route.request().resourceType() === "image" ? route.abort() : route.continue(),
);

// block third-party trackers
await context.route(/google-analytics|hotjar/, (route) => route.abort());
```

Blocking third-party scripts makes tests faster and avoids flakiness from services you don't control.

## 174: How do URL patterns work in page.route?

`page.route()` accepts a glob string, a regex, or a function:

```ts
await page.route("**/api/users/*", handler); // glob
await page.route(/\/api\/users\/\d+$/, handler); // regex
await page.route((url) => url.pathname.startsWith("/api"), handler); // function
```

Glob rules:

- `*` matches any characters except `/`
- `**` matches any characters including `/`
- `{a,b}` matches either option

Since 1.52, `?` and `[]` are not glob characters anymore, so use a regex if you need them. A common mistake is that `'/api/users'` without `**` doesn't match a full URL like `http://localhost:3000/api/users`, unless `baseURL` is set.

## 175: How do you wait for a specific API response?

Start waiting before the action that triggers the request:

```ts
const responsePromise = page.waitForResponse("**/api/orders");
await page.getByRole("button", { name: "Place order" }).click();
const response = await responsePromise;

expect(response.status()).toBe(201);
const order = await response.json();
```

You can also pass a function:

```ts
page.waitForResponse(
  (res) =>
    res.url().includes("/api/orders") && res.request().method() === "POST",
);
```

If you call `waitForResponse` after the click, the response may already be done and you'll wait forever.

## 176: How do you check what data the page sent to the server?

Wait for the request and read its body:

```ts
const requestPromise = page.waitForRequest(
  (req) => req.url().endsWith("/api/feedback") && req.method() === "POST",
);
await page.getByLabel("Message").fill("Great app");
await page.getByRole("button", { name: "Send" }).click();
const request = await requestPromise;

expect(request.postDataJSON()).toEqual({ message: "Great app", rating: 5 });
expect(request.headers()["content-type"]).toContain("application/json");
```

## 177: How do you record and replay network traffic with HAR files?

A HAR file stores requests and responses. Playwright can record one and then serve responses from it:

```ts
// record (or update) the HAR
await page.routeFromHAR("hars/products.har", {
  url: "**/api/**",
  update: true,
});
await page.goto("/products");
```

```ts
// replay from the HAR
await page.routeFromHAR("hars/products.har", { url: "**/api/**" });
await page.goto("/products");
```

You can also record with the CLI: `npx playwright open --save-har=example.har --save-har-glob="**/api/**" http://localhost:3000`. Requests that are not in the HAR are aborted by default (`notFound: 'abort'`), or you can let them go to the network with `notFound: 'fallback'`.

## 178: How do you create an API request context with different settings?

Use `playwright.request.newContext()`, for example to call an API with an admin token while the browser is logged in as a normal user:

```ts
import { test, expect, request } from "@playwright/test";

test("admin creates item, user sees it", async ({ page }) => {
  const adminApi = await request.newContext({
    baseURL: "http://localhost:4000",
    extraHTTPHeaders: { Authorization: `Bearer ${process.env.ADMIN_TOKEN}` },
  });

  await adminApi.post("/api/items", { data: { name: "New item" } });
  await adminApi.dispose();

  await page.goto("/items");
  await expect(page.getByText("New item")).toBeVisible();
});
```

Call `dispose()` when done to free resources.

## 179: How do you prepare test data through the API in a UI test?

Creating data through the UI is slow and tests things that are not the point of the test. Create it through the API, then use the UI only for what you test:

```ts
test("user can delete a project", async ({ page, request }) => {
  const res = await request.post("/api/projects", {
    data: { name: "To delete" },
  });
  const project = await res.json();

  await page.goto(`/projects/${project.id}`);
  await page.getByRole("button", { name: "Delete project" }).click();
  await page.getByRole("button", { name: "Confirm" }).click();

  await expect(page).toHaveURL("/projects");
  await expect(page.getByText("To delete")).toHaveCount(0);
});
```

## 180: What is the difference between the request fixture, page.request and context.request?

- `request` fixture: a standalone API context. It uses `baseURL` and `extraHTTPHeaders` from the config but doesn't share cookies with the browser.
- `context.request` (and `page.request`, which is the same thing): shares the cookie storage with the browser context. If the browser is logged in, API calls are logged in too, and cookies set by the API response are visible in the browser.

```ts
test("api uses browser session", async ({ page }) => {
  await page.goto("/login");
  // ... log in through UI
  const res = await page.request.get("/api/me");
  await expect(res).toBeOK();
});
```

## 181: How does visual testing work in Playwright?

Use `toHaveScreenshot()`. The first run saves a "golden" screenshot. Later runs take a new one and compare pixel by pixel.

```ts
test("landing page looks right", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveScreenshot("landing.png");
  await expect(page.getByTestId("pricing-table")).toHaveScreenshot();
});
```

The assertion retries until two screenshots in a row are the same, so it handles small render delays. On a mismatch, the report shows the expected, actual and diff images.

## 182: How do you update screenshot snapshots?

```bash
npx playwright test --update-snapshots
```

The values are:

- `missing`: only write snapshots that don't exist yet
- `changed`: update snapshots that don't match (the default when you pass the flag)
- `all`: rewrite all snapshots
- `none`: never write

```bash
npx playwright test --update-snapshots=missing
```

Always look at the diffs before you commit new snapshots. Otherwise you may commit a bug as the new "expected".

## 183: How do you make visual tests less flaky?

Use the options of `toHaveScreenshot`:

```ts
await expect(page).toHaveScreenshot("dashboard.png", {
  mask: [page.getByTestId("current-time"), page.getByTestId("avatar")],
  maxDiffPixels: 100, // or maxDiffPixelRatio: 0.01
  threshold: 0.2, // color difference allowed per pixel
  animations: "disabled", // default for toHaveScreenshot
  fullPage: true,
});
```

Also:

- mock data so content is the same every run
- hide dynamic parts with `mask` or a `stylePath` CSS file
- run visual tests in the same OS and browser (for example the Playwright Docker image), because fonts and rendering differ between machines

## 184: Why do snapshot files have the browser and OS in their name?

By default, snapshot names look like `landing-chromium-linux.png`. Rendering differs between browsers and operating systems, so one golden image can't work for all of them.

This also means snapshots made on a Mac won't match on Linux CI. Generate them in the same environment as CI, usually with Docker. You can change the naming with `snapshotPathTemplate`:

```ts
export default defineConfig({
  snapshotPathTemplate: "{testDir}/__screenshots__/{testFilePath}/{arg}{ext}",
});
```

## 185: How do you snapshot text or other non-image data?

Use `toMatchSnapshot()` with a string or buffer:

```ts
test("api schema did not change", async ({ request }) => {
  const res = await request.get("/api/schema");
  expect(await res.text()).toMatchSnapshot("schema.txt");
});
```

The first run writes the file, and later runs compare against it. For images, prefer `toHaveScreenshot()`, which handles waiting and stable screenshots for you.

## 186: What is an ARIA snapshot?

An ARIA snapshot is a YAML view of the accessibility tree of an element: roles, names and states. `toMatchAriaSnapshot()` compares the page structure to it.

```ts
await expect(page.getByRole("navigation")).toMatchAriaSnapshot(`
  - navigation:
    - link "Home"
    - link "Pricing"
    - link "Docs"
`);
```

It is a good middle ground between pixel screenshots and many small assertions. It doesn't break on styling changes, but it catches missing elements, wrong text and wrong roles. You can match partly, use regex for names, and update snapshots with `--update-snapshots`. `locator.ariaSnapshot()` returns the YAML so you can see what the page looks like.

## 187: How do you run accessibility checks in Playwright?

Use `@axe-core/playwright`:

```ts
import AxeBuilder from "@axe-core/playwright";

test("home page has no a11y violations", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa"])
    .exclude("#third-party-widget")
    .analyze();

  expect(results.violations).toEqual([]);
});
```

Automated checks find only part of the accessibility problems (missing labels, low contrast, wrong ARIA). Keyboard and screen reader testing still has to be done separately.

## 188: How do you run tests inside one file in parallel?

```ts
test.describe.configure({ mode: "parallel" });

test("a", async ({ page }) => {});
test("b", async ({ page }) => {});
```

Or set `fullyParallel: true` for the whole project. Tests in parallel mode can't share state through variables, and each worker runs its own `beforeAll`. `test.describe.parallel()` is the older way and is deprecated.

## 189: What is serial mode?

Serial mode runs the tests in a group one after another, and if one fails, the rest are skipped. On retry, the whole group runs again.

```ts
test.describe.configure({ mode: "serial" });

let page: Page;

test.beforeAll(async ({ browser }) => {
  page = await browser.newPage();
});

test("step 1: create order", async () => {
  /* ... */
});
test("step 2: pay for order", async () => {
  /* ... */
});
```

Playwright doesn't recommend it, because tests that depend on each other are slower and harder to debug. It's better to make one longer test with `test.step()`.

## 190: What is sharding?

Sharding splits the test suite across several machines. Each machine runs a part:

```bash
npx playwright test --shard=1/4
npx playwright test --shard=2/4
npx playwright test --shard=3/4
npx playwright test --shard=4/4
```

With `fullyParallel: true`, tests are split one by one, which gives better balance. Without it, whole files are split, so one very big file can make one shard much slower than the others.

## 191: How do you merge reports from several shards?

Use the `blob` reporter on each shard, collect the blob files, and merge them:

```ts
reporter: process.env.CI ? 'blob' : 'html',
```

```bash
# after all shards finish and their blob-report folders are copied into all-blob-reports/
npx playwright merge-reports --reporter html ./all-blob-reports
```

The result is one HTML report with all tests, as if they ran on one machine.

## 192: How do you run Playwright in GitHub Actions?

A basic workflow (similar to what `npm init playwright` creates):

```yaml
name: Playwright Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with:
          node-version: lts/*
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30
```

Uploading the report as an artifact lets you open traces from failed CI runs.

## 193: How do you run Playwright tests in Docker?

Use the official image, which has Node.js, the browsers and all system libraries:

```bash
docker run --rm --ipc=host -v $(pwd):/work -w /work \
  mcr.microsoft.com/playwright:v1.64.1-noble \
  npx playwright test
```

Keep the image tag the same as your `@playwright/test` version. `--ipc=host` is recommended for Chromium, because otherwise it can run out of shared memory and crash.

## 194: What config settings are usually different on CI?

```ts
export default defineConfig({
  forbidOnly: !!process.env.CI, // fail if test.only is committed
  retries: process.env.CI ? 2 : 0, // retry flaky tests on CI
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI ? [["dot"], ["html", { open: "never" }]] : "list",
  use: {
    trace: "on-first-retry",
  },
  webServer: {
    command: "npm run start",
    url: "http://localhost:3000",
    reuseExistingServer: !process.env.CI,
  },
});
```

The number of workers depends on the CI machine. Small runners often do better with 1-2 workers than with the default.

## 195: How can a test know if it is a retry?

Use `testInfo.retry`. It's `0` on the first run and goes up on each retry:

```ts
test("flaky backend", async ({ page }, testInfo) => {
  if (testInfo.retry > 0) {
    await resetTestData();
  }
  // ...
});
```

You can use it to clean up state before retrying. Don't use it to make the test easier on retry, because that hides real bugs.

## 196: What are the trace modes and which one should you use?

- `'off'`: no trace
- `'on'`: trace every test (slow, big files)
- `'retain-on-failure'`: trace every test, delete traces of passing tests
- `'on-first-retry'`: trace only the first retry of a failed test
- `'on-all-retries'`: trace all retries
- `'retain-on-first-failure'`: trace each test's first run, keep it only if it fails

`'on-first-retry'` is the usual choice for CI with retries, since it costs nothing when tests pass. If you don't use retries, `'retain-on-failure'` is better, because otherwise you never get a trace. Locally, you can force traces with `--trace on`.

## 197: How do you write a custom reporter?

Create a class that implements the `Reporter` interface:

```ts
// my-reporter.ts
import type {
  Reporter,
  FullConfig,
  Suite,
  TestCase,
  TestResult,
  FullResult,
} from "@playwright/test/reporter";

class MyReporter implements Reporter {
  onBegin(config: FullConfig, suite: Suite) {
    console.log(`Running ${suite.allTests().length} tests`);
  }
  onTestEnd(test: TestCase, result: TestResult) {
    console.log(`${test.title}: ${result.status} (${result.duration}ms)`);
  }
  onEnd(result: FullResult) {
    console.log(`Finished: ${result.status}`);
  }
}
export default MyReporter;
```

```ts
reporter: [['list'], ['./my-reporter.ts']],
```

Custom reporters are often used to send results to Slack, a dashboard or a test management tool.

## 198: How do you use the JUnit reporter?

```ts
reporter: [
  ['junit', { outputFile: 'results/junit.xml' }],
  ['html', { open: 'never' }],
],
```

Many CI tools (Jenkins, GitLab, Azure DevOps, CircleCI) read JUnit XML to show test results in their UI. You can also set the output file with the `PLAYWRIGHT_JUNIT_OUTPUT_FILE` environment variable.

## 199: How do you attach files or data to the test report?

Use `testInfo.attach()`:

```ts
test("export", async ({ page }, testInfo) => {
  const screenshot = await page.screenshot();
  await testInfo.attach("after export", {
    body: screenshot,
    contentType: "image/png",
  });

  await testInfo.attach("server log", {
    path: "logs/server.log",
    contentType: "text/plain",
  });
});
```

Attachments show up in the HTML report. This is useful for extra debug info like API responses, logs or a screenshot at an important moment.

## 200: How do you write parameterized tests?

Loop over the data and create a test for each item. Each test needs a unique title:

```ts
const users = [
  { role: "admin", canDelete: true },
  { role: "editor", canDelete: false },
];

for (const { role, canDelete } of users) {
  test(`${role} delete button visibility`, async ({ page }) => {
    await page.goto(`/as/${role}/posts/1`);
    const button = page.getByRole("button", { name: "Delete" });
    if (canDelete) await expect(button).toBeVisible();
    else await expect(button).toBeHidden();
  });
}
```

You can also loop around `test.describe` blocks to repeat whole groups.

## 201: How do you run the same tests with different settings using projects?

Define an option fixture and set it per project. The tests run once for each project:

```ts
// fixtures.ts
export type TestOptions = { apiVersion: "v1" | "v2" };

export const test = base.extend<TestOptions>({
  apiVersion: ["v1", { option: true }],
});
```

```ts
// playwright.config.ts
export default defineConfig<TestOptions>({
  projects: [
    { name: "api-v1", use: { apiVersion: "v1" } },
    { name: "api-v2", use: { apiVersion: "v2" } },
  ],
});
```

```ts
test("lists users", async ({ request, apiVersion }) => {
  const res = await request.get(`/api/${apiVersion}/users`);
  await expect(res).toBeOK();
});
```

## 202: How do you drive tests from a JSON or CSV file?

Read the file at the top of the test file and loop over the rows:

```ts
import fs from "node:fs";
import path from "node:path";
import { parse } from "csv-parse/sync";

const records = parse(fs.readFileSync(path.join(__dirname, "logins.csv")), {
  columns: true,
  skip_empty_lines: true,
});

for (const record of records) {
  test(`login: ${record.case}`, async ({ page }) => {
    await page.goto("/login");
    await page.getByLabel("Email").fill(record.email);
    await page.getByLabel("Password").fill(record.password);
    await page.getByRole("button", { name: "Sign in" }).click();
    await expect(page.getByRole("alert")).toHaveText(record.expectedMessage);
  });
}
```

The file is read when tests are collected, in every worker, so keep it small and fast to load.

## 203: How do you set retries or a timeout for one group of tests?

Use `test.describe.configure()`:

```ts
test.describe("payment provider", () => {
  test.describe.configure({ retries: 3, timeout: 60_000 });

  test("pay by card", async ({ page }) => {});
  test("pay by paypal", async ({ page }) => {});
});
```

You can also set `retries` and `timeout` per project in the config.

## 204: What options does locator.filter support?

```ts
const rows = page.getByRole("row");

rows.filter({ hasText: "Pending" }); // contains text
rows.filter({ hasNotText: "Archived" }); // doesn't contain text
rows.filter({ has: page.getByRole("button", { name: "Retry" }) }); // has a child
rows.filter({ hasNot: page.getByRole("checkbox", { checked: true }) });
page.getByRole("button").filter({ visible: true }); // only visible ones
```

The inner locator in `has`/`hasNot` is relative to the outer one, so it must not start from a different page or frame. Filters can be chained.

## 205: What do locator.and and locator.or do?

`and()` matches elements that match both locators:

```ts
const subscribe = page.getByRole("button").and(page.getByTitle("Subscribe"));
```

`or()` matches either one. It is handy when the page can show one of two things:

```ts
const newEmail = page.getByRole("button", { name: "New email" });
const dialog = page.getByText("Confirm security settings");

await expect(newEmail.or(dialog).first()).toBeVisible();
if (await dialog.isVisible()) {
  await page.getByRole("button", { name: "Dismiss" }).click();
}
await newEmail.click();
```

If both match at the same time, `or()` returns several elements, which is why `.first()` is used above.

## 206: How does Playwright handle shadow DOM?

Most locators go through open shadow roots automatically, so you don't need any special syntax:

```ts
// <my-card> has a shadow root with a button inside
await page.getByRole("button", { name: "Buy" }).click();
await page.locator("my-card button").click();
```

Two exceptions: XPath doesn't go into shadow roots, and closed shadow roots are not accessible.

## 207: How do you work with nested iframes or find a frame by name?

Chain `frameLocator`/`contentFrame` for nested frames:

```ts
const inner = page.frameLocator("#outer-frame").frameLocator("#inner-frame");
await inner.getByRole("button", { name: "Submit" }).click();
```

You can also get a `Frame` object by name or URL:

```ts
const frame =
  page.frame({ name: "checkout" }) ?? page.frame({ url: /stripe\.com/ });
await frame?.getByLabel("Card number").fill("4242 4242 4242 4242");
```

`frameLocator` is usually better because it waits for the frame. `page.frame()` returns `null` if the frame isn't there yet.

## 208: How do you upload a file when there is no visible input element?

Some upload buttons create the `<input type=file>` on the fly. Wait for the `filechooser` event:

```ts
const fileChooserPromise = page.waitForEvent("filechooser");
await page.getByRole("button", { name: "Upload photo" }).click();
const fileChooser = await fileChooserPromise;
await fileChooser.setFiles("fixtures/photo.jpg");
```

`fileChooser.isMultiple()` tells you if the input accepts several files.

## 209: How do you control time in tests?

Use the Clock API (`page.clock`):

```ts
test("session expires after 30 minutes", async ({ page }) => {
  await page.clock.install({ time: new Date("2026-01-15T09:00:00") });
  await page.goto("/dashboard");

  await page.clock.fastForward("30:00"); // mm:ss
  await expect(page.getByText("Session expired")).toBeVisible();
});
```

Other methods:

- `setFixedTime(date)`: `Date.now()` always returns this, timers keep running
- `setSystemTime(date)`: changes the current time without running timers
- `runFor(ms)`: moves time forward and runs all timers in between
- `pauseAt(date)`: jumps to a time and pauses there

`install()` must be called before the page code uses timers, so call it before `goto`.

## 210: What is addInitScript used for?

`addInitScript` runs a script in every page (and frame) before any of the page's own scripts. It's used to set up the environment:

```ts
await page.addInitScript(() => {
  localStorage.setItem("feature-flags", JSON.stringify({ newCheckout: true }));
  (window as any).__E2E__ = true;
});
await page.goto("/");

// from a file
await context.addInitScript({ path: "./mocks/random.js" });
```

It runs again on every navigation and reload.

## 211: What is exposeFunction?

`exposeFunction` adds a function to `window` in the page. When the page calls it, the code runs in Node.js and the result goes back to the page.

```ts
await page.exposeFunction("sha256", (text: string) =>
  crypto.createHash("sha256").update(text).digest("hex"),
);

await page.setContent(`
  <script>
    async function onClick() {
      document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
    }
  </script>
  <button onclick="onClick()">Click</button>
  <div></div>
`);
```

It is useful when the page needs to call back into the test, for example to report events.

## 212: How do you run JavaScript on an element?

Use `locator.evaluate()` for one element and `evaluateAll()` for all matches:

```ts
const color = await page
  .getByRole("button")
  .first()
  .evaluate((el) => getComputedStyle(el).backgroundColor);

const hrefs = await page
  .getByRole("link")
  .evaluateAll((links) => links.map((a) => (a as HTMLAnchorElement).href));

await page.getByTestId("list").evaluate((el, top) => (el.scrollTop = top), 500);
```

The second argument is passed into the browser function. Only data that can be serialized (JSON-like values, plus a few types like `Date` and `Map`) can go back and forth.

## 213: What are JSHandle and ElementHandle?

A `JSHandle` is a reference to an object inside the page that stays in the browser. An `ElementHandle` is a `JSHandle` that points to a DOM element.

```ts
const windowHandle = await page.evaluateHandle(() => window);
const bodyHandle = await page.evaluateHandle(() => document.body);
await windowHandle.dispose();
```

Handles are needed when an object can't be serialized, like `window` or a `DataTransfer`. For elements, Playwright recommends locators instead of `ElementHandle`, because handles point to one node and break if it is replaced.

## 214: What is expect.poll?

`expect.poll` turns any async function into a retrying assertion. It calls the function until the matcher passes or the timeout runs out:

```ts
await expect
  .poll(
    async () => {
      const res = await page.request.get("/api/jobs/42");
      return (await res.json()).status;
    },
    {
      message: "job should finish",
      timeout: 30_000,
      intervals: [1_000, 2_000, 5_000],
    },
  )
  .toBe("done");
```

It is useful for things that are not on the page, like a background job or an email.

## 215: What is expect(...).toPass?

`toPass` retries a whole block of code until it passes without throwing:

```ts
await expect(async () => {
  const res = await page.request.get("/api/status");
  expect(res.status()).toBe(200);
  expect(await res.json()).toMatchObject({ ready: true });
}).toPass({ timeout: 60_000, intervals: [1_000, 2_000, 10_000] });
```

The difference from `expect.poll` is that `toPass` retries several steps and assertions together. By default it has no timeout of its own, so set `timeout` or it can run until the test times out.

## 216: How do you add a custom matcher?

Use `expect.extend()`:

```ts
import { expect as baseExpect, type Locator } from "@playwright/test";

export const expect = baseExpect.extend({
  async toHaveAmount(
    locator: Locator,
    expected: number,
    options?: { timeout?: number },
  ) {
    const name = "toHaveAmount";
    let pass: boolean;
    let actual: number | undefined;
    try {
      await baseExpect(locator).toHaveAttribute(
        "data-amount",
        String(expected),
        options,
      );
      pass = true;
    } catch {
      pass = false;
      actual = Number(await locator.getAttribute("data-amount"));
    }

    return {
      name,
      pass,
      expected,
      actual,
      message: () => `expected amount ${expected}, got ${actual}`,
    };
  },
});
```

```ts
await expect(page.getByTestId("cart")).toHaveAmount(3);
```

## 217: What is addLocatorHandler?

`page.addLocatorHandler()` registers a handler for an overlay that can appear at random times, like a newsletter popup or cookie banner. Before each action and auto-waiting assertion, Playwright checks if the overlay is visible and runs your handler to close it.

```ts
await page.addLocatorHandler(
  page.getByRole("dialog", { name: "Join our newsletter" }),
  async () => {
    await page.getByRole("button", { name: "No thanks" }).click();
  },
);

await page.goto("/");
await page.getByRole("link", { name: "Shop" }).click(); // works even if the popup shows up
```

There are options like `times` (run at most N times) and `noWaitAfter`. Remove it with `page.removeLocatorHandler()`.

## 218: How do you test a responsive layout at several screen sizes?

Use projects or a loop with `test.use`:

```ts
const sizes = [
  { name: "mobile", width: 375, height: 812 },
  { name: "tablet", width: 768, height: 1024 },
  { name: "desktop", width: 1440, height: 900 },
];

for (const size of sizes) {
  test.describe(size.name, () => {
    test.use({ viewport: { width: size.width, height: size.height } });

    test("navigation", async ({ page }) => {
      await page.goto("/");
      if (size.width < 768) {
        await expect(page.getByRole("button", { name: "Menu" })).toBeVisible();
      } else {
        await expect(
          page.getByRole("navigation").getByRole("link", { name: "Pricing" }),
        ).toBeVisible();
      }
    });
  });
}
```

For real mobile behavior (touch, mobile user agent), use `devices` entries in projects instead of only the viewport.

## 219: How do you test a site behind HTTP basic auth?

Use `httpCredentials`:

```ts
use: {
  httpCredentials: {
    username: process.env.BASIC_USER!,
    password: process.env.BASIC_PASS!,
  },
},
```

Playwright answers the auth challenge for you. It also works for the `request` fixture.

## 220: How do you test a site with a self-signed HTTPS certificate?

Set `ignoreHTTPSErrors`:

```ts
use: { ignoreHTTPSErrors: true },
```

Only use it for test environments. For client certificate (mTLS) setups, there is the `clientCertificates` option.

## 221: How do you run tests through a proxy?

```ts
use: {
  proxy: {
    server: 'http://proxy.example.com:3128',
    bypass: 'localhost,*.internal',
    username: 'user',
    password: 'pass',
  },
},
```

You can set a proxy for the whole browser in `launchOptions` or per context. A proxy is sometimes used to reach staging environments or to inspect traffic with tools like mitmproxy.

## 222: How do you mock a WebSocket?

Use `page.routeWebSocket()`:

```ts
await page.routeWebSocket("wss://example.com/ws", (ws) => {
  ws.onMessage((message) => {
    if (message === "ping") ws.send("pong");
  });
});
```

The handler replaces the real server. You can also connect to the real server and only change some messages, using `ws.connectToServer()`. To just watch WebSocket traffic, listen to `page.on('websocket')`.

## 223: How do you fail a test automatically when the page logs errors?

Use an auto fixture:

```ts
export const test = base.extend<{ failOnConsoleErrors: void }>({
  failOnConsoleErrors: [
    async ({ page }, use) => {
      const errors: string[] = [];
      page.on("console", (msg) => {
        if (msg.type() === "error") errors.push(msg.text());
      });
      page.on("pageerror", (err) => errors.push(err.message));

      await use();

      expect(errors, "page should have no console errors").toEqual([]);
    },
    { auto: true },
  ],
});
```

In practice you usually need an allow list for known noise, like third-party scripts.

## 224: How do you run tests against different environments?

Keep one config and pick the environment with a variable:

```ts
const envs = {
  local: "http://localhost:3000",
  staging: "https://staging.example.com",
  prod: "https://www.example.com",
} as const;

const env = (process.env.TEST_ENV ?? "local") as keyof typeof envs;

export default defineConfig({
  use: { baseURL: envs[env] },
  webServer:
    env === "local"
      ? { command: "npm run dev", url: envs.local, reuseExistingServer: true }
      : undefined,
});
```

```bash
TEST_ENV=staging npx playwright test --grep @smoke
```

Tests that change data should usually not run against production. Use tags to choose which tests are safe there.

## 225: What do --last-failed and --only-changed do?

- `--last-failed` reruns only the tests that failed in the last run. Good for fixing things locally.
- `--only-changed` runs only test files that changed since a git ref, plus test files that import changed files.

```bash
npx playwright test --last-failed
npx playwright test --only-changed=origin/main
```

`--only-changed` follows imports between files, but it can't know which tests hit which backend code, so it's a fast first check, not a full replacement for the whole suite.

## 226: How do you check if a test is flaky?

Run it many times:

```bash
npx playwright test checkout.spec.ts --repeat-each=20 --workers=4
```

`--repeat-each` runs each test N times. Running with more workers puts more load on the machine, which brings timing problems out faster. If a test fails even once out of 20, it's flaky.

## 227: What does failOnFlakyTests do?

With `failOnFlakyTests: true` in the config (or `--fail-on-flaky-tests` on the command line), the run fails if any test was flaky, meaning it failed first and passed on retry.

```ts
export default defineConfig({
  retries: 2,
  failOnFlakyTests: !!process.env.CI,
});
```

It's useful if your team wants to treat flakiness as a real failure while still collecting traces from retries.

## 228: How do you make some tests run only in some projects?

Use `testMatch`, `testIgnore`, `grep` or `grepInvert` on the project:

```ts
projects: [
  { name: 'api', testDir: './tests/api' },
  {
    name: 'chromium',
    testDir: './tests/e2e',
    use: { ...devices['Desktop Chrome'] },
  },
  {
    name: 'mobile',
    testDir: './tests/e2e',
    grep: /@mobile/,
    use: { ...devices['iPhone 15'] },
  },
],
```

Or skip inside the test using the project name:

```ts
test.skip(test.info().project.name === "mobile", "desktop only");
```

## 229: What useful options does codegen have?

```bash
npx playwright codegen --viewport-size="800,600" localhost:3000
npx playwright codegen --device="Pixel 7" localhost:3000
npx playwright codegen --color-scheme=dark localhost:3000
npx playwright codegen --timezone="Europe/Rome" --lang="it-IT" localhost:3000
npx playwright codegen --save-storage=auth.json localhost:3000  # log in, save state
npx playwright codegen --load-storage=auth.json localhost:3000  # start logged in
npx playwright codegen --target=python localhost:3000
```

In the codegen window you can also record assertions (visibility, text, value) and pick locators.

## 230: What can you do in UI mode besides running tests?

- **Watch mode**: click the eye icon on a test or file and it reruns when you save.
- **Timeline and DOM snapshots**: hover over actions to see the page at that moment, like a trace.
- **Pick locator**: click on the page to get a locator.
- **Filters**: by text, tag, project and status.
- **Network, console, errors and attachments** tabs for each action.
- **Pop out the DOM snapshot** to inspect it with browser DevTools.

You can also run UI mode on a remote machine or container with `--ui-host` and `--ui-port`.

## 231: How do you see Playwright's internal logs?

Set the `DEBUG` environment variable:

```bash
DEBUG=pw:api npx playwright test
DEBUG=pw:browser npx playwright test    # browser process logs
DEBUG=pw:webserver npx playwright test  # webServer output
```

`pw:api` prints each API call and what it waits for, which helps when an action seems to hang.

## 232: How do steps help with reporting, and what does box do?

Steps group actions in the report. They can return values, and `box: true` makes errors point to the step call instead of the code inside it:

```ts
async function login(page: Page, user: string) {
  await test.step(
    "log in",
    async () => {
      await page.getByLabel("User").fill(user);
      await page.getByRole("button", { name: "Sign in" }).click();
      await expect(page.getByText(`Hi, ${user}`)).toBeVisible();
    },
    { box: true },
  );
}

const orderId = await test.step("create order", async () => {
  return await createOrder(page);
});
```

With `box: true`, a failure inside a helper is reported at the line in the test that called `login()`, which is usually what you want for shared helpers. Steps can also have a `timeout`, and `test.step.skip()` skips one.

## 233: What is Playwright component testing?

Component testing mounts a single component (React, Vue and others) in a real browser and tests it with Playwright's API:

```tsx
import { test, expect } from "@playwright/experimental-ct-react";
import { Button } from "./Button";

test("calls onClick", async ({ mount }) => {
  let clicked = false;
  const component = await mount(
    <Button title="Submit" onClick={() => (clicked = true)} />,
  );
  await component.click();
  expect(clicked).toBe(true);
});
```

It uses Vite to bundle components. It is still marked experimental, and Playwright has said some of the framework packages are no longer being updated, so check the docs before you build a big suite on it. Many teams use Vitest browser mode or Testing Library for component tests and Playwright for E2E.

## 234: How do you use path aliases from tsconfig in tests?

Playwright reads the `paths` from `tsconfig.json` when it loads test files:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@pages/*": ["tests/pages/*"],
      "@fixtures": ["tests/fixtures/index.ts"]
    }
  }
}
```

```ts
import { test } from "@fixtures";
import { LoginPage } from "@pages/LoginPage";
```

If your tests need a different tsconfig than the app, set it with the `tsconfig` option in the config or `--tsconfig` on the command line.

## 235: Which ESLint rules help with Playwright tests?

Use `eslint-plugin-playwright` and the TypeScript rule for promises:

```js
// eslint.config.js
import playwright from "eslint-plugin-playwright";
import tseslint from "typescript-eslint";

export default tseslint.config({
  files: ["tests/**/*.ts"],
  extends: [playwright.configs["flat/recommended"]],
  languageOptions: { parserOptions: { projectService: true } },
  rules: {
    "@typescript-eslint/no-floating-promises": "error",
  },
});
```

The plugin catches things like missing `await` on assertions, `page.pause()` left in code, `waitForTimeout`, focused tests and use of `ElementHandle`.

## 236: How do you test form validation?

Test both the browser's built-in validation and your own messages:

```ts
test("email is required", async ({ page }) => {
  await page.goto("/signup");
  await page.getByRole("button", { name: "Create account" }).click();

  await expect(page.getByText("Email is required")).toBeVisible();
  await expect(page.getByLabel("Email")).toHaveAttribute(
    "aria-invalid",
    "true",
  );
});

test("native validation message", async ({ page }) => {
  await page.goto("/signup");
  await page.getByLabel("Email").fill("not-an-email");
  const message = await page
    .getByLabel("Email")
    .evaluate((el: HTMLInputElement) => el.validationMessage);
  expect(message).not.toBe("");
});
```

`toHaveAccessibleErrorMessage()` checks the error linked with `aria-errormessage`.

## 237: How do you test a sortable table?

Read the column values after sorting and compare with a sorted copy:

```ts
test("sort by price", async ({ page }) => {
  await page.goto("/products");
  await page.getByRole("columnheader", { name: "Price" }).click();

  const priceCells = page.getByRole("row").locator("td:nth-child(3)");
  await expect(
    page.getByRole("columnheader", { name: "Price" }),
  ).toHaveAttribute("aria-sort", "ascending");

  const prices = (await priceCells.allTextContents()).map((t) =>
    Number(t.replace("$", "")),
  );
  expect(prices).toEqual([...prices].sort((a, b) => a - b));
});
```

Wait for something that shows the sort finished (like `aria-sort`) before reading the values, because `allTextContents()` doesn't retry.

## 238: How do you handle loading spinners and content that appears later?

Wait for the final state, not the spinner. Web-first assertions already retry:

```ts
await page.getByRole("button", { name: "Search" }).click();
await expect(page.getByRole("listitem")).toHaveCount(10);
```

If you need to be sure the old content went away first:

```ts
await expect(page.getByTestId("spinner")).toBeHidden();
await expect(page.getByRole("row")).toHaveCount(25);
```

Watch out: if the spinner appears a bit after the click, checking `toBeHidden()` right away can pass before it even showed up. Asserting the expected content is safer.

## 239: How do animations affect tests and how do you deal with them?

Playwright waits for elements to be stable before clicking, so most animations are fine. Problems usually come from screenshots, from elements that move while you read their position, or from very long transitions.

Options:

- `toHaveScreenshot` stops CSS animations by default (`animations: 'disabled'`).
- Set `reducedMotion: 'reduce'` (in `use` or `page.emulateMedia`) if the app respects `prefers-reduced-motion`.
- Inject CSS to turn off transitions in tests:

```ts
await page.addStyleTag({
  content:
    "*, *::before, *::after { transition: none !important; animation: none !important; }",
});
```

## 240: What does force: true do and when should you use it?

`force: true` skips the actionability checks (visible, stable, enabled, receives events) and does the action anyway:

```ts
await page
  .getByRole("checkbox", { name: "Hidden input" })
  .check({ force: true });
```

It is sometimes needed for custom controls where the real input is hidden under a styled element. But often it hides a real bug, like a modal covering the button. If you need `force`, first check why the normal action fails, and prefer clicking the visible element the user would click.

## 241: What does the trial option do?

`trial: true` runs all actionability checks but doesn't do the action. It's a way to wait until an element is ready to be clicked without clicking it:

```ts
await page.getByRole("button", { name: "Submit" }).click({ trial: true });
```

It is also useful for hovering over an element to show a tooltip without triggering a click handler.

## 242: How do you test copy to clipboard?

Grant clipboard permissions (in Chromium) and read the clipboard with `evaluate`:

```ts
test.use({ permissions: ["clipboard-read", "clipboard-write"] });

test("copy link", async ({ page }) => {
  await page.goto("/share");
  await page.getByRole("button", { name: "Copy link" }).click();
  const text = await page.evaluate(() => navigator.clipboard.readText());
  expect(text).toContain("/share/");
});
```

Clipboard permissions differ between browsers, so these tests are often limited to Chromium.

## 243: How do you handle secrets in Playwright tests?

- Keep passwords, tokens and API keys in environment variables or a secret manager, never in the repo.
- Locally, use a `.env` file that is in `.gitignore`.
- On CI, use the CI's secrets and pass them as environment variables.
- Don't commit `storageState` files, they contain session cookies.
- Be careful with traces, videos and screenshots: they can contain typed passwords and tokens in requests. Limit who can download CI artifacts.
- Use dedicated test accounts with only the permissions they need.

## 244: How do you clean up test data?

Common approaches:

- **Fixture teardown**: create data in a fixture and delete it after `use()`, so cleanup runs even when the test fails.
- **Unique data**: give data unique names (with a timestamp or worker index) so leftovers don't break other tests.
- **Reset endpoint or script**: a test-only API that resets the database, called in a setup project.
- **Fresh environment**: start a new database (for example in Docker) for each CI run.

Cleaning up in `afterEach` works too, but fixtures keep setup and cleanup together.

## 245: Why is test independence important?

Each test should be able to run alone, in any order, on any worker. If test B needs test A to run first:

- you can't run B alone when debugging
- parallel runs and sharding may run them on different workers or machines
- a failure in A makes B fail too, which hides the real cause
- retries only rerun B, which may not work without A

Playwright helps by giving each test a fresh browser context. You still need to keep server-side data independent.

## 246: How do you test a Next.js or Vite app with webServer?

Locally, run the dev server. On CI, test the production build, which is closer to what users get and avoids slow dev compilation:

```ts
webServer: {
  command: process.env.CI ? 'npm run build && npm run start' : 'npm run dev',
  url: 'http://localhost:3000',
  reuseExistingServer: !process.env.CI,
  timeout: 180_000,
},
```

If the build happens in an earlier CI step, use only `npm run start` in `webServer` so you don't build twice.

## 247: Why and how should you block third-party scripts in tests?

Third-party scripts (analytics, chat widgets, ads) make tests slower and can fail or show popups at random. Unless you test them, block them:

```ts
export const test = base.extend({
  context: async ({ context }, use) => {
    await context.route(
      /(googletagmanager|segment|intercom|hotjar)\./,
      (route) => route.abort(),
    );
    await use(context);
  },
});
```

Routing on the context covers popups and new tabs too, not just the first page.

## 248: Why might you set serviceWorkers to block?

Service workers can serve requests from their own cache, and those requests may not go through `page.route()`. This makes network mocking unreliable.

```ts
use: { serviceWorkers: 'block' },
```

Blocking them makes all requests go through Playwright's routing. If you test PWA or offline features, keep them on (`'allow'`, the default) and test that behavior on purpose.

## 249: What is a persistent context?

`launchPersistentContext` starts a browser with a real user data directory on disk, so data stays between runs, like a normal browser profile:

```ts
import { chromium } from "playwright";

const context = await chromium.launchPersistentContext("/tmp/my-profile", {
  headless: false,
});
const page = context.pages()[0] ?? (await context.newPage());
```

It is needed for testing browser extensions and for scripts that should keep a login. In normal tests, use regular contexts, which are isolated and faster.

## 250: What is connectOverCDP?

`chromium.connectOverCDP()` connects Playwright to a Chromium browser that is already running, using the Chrome DevTools Protocol:

```ts
const browser = await chromium.connectOverCDP("http://localhost:9222");
const context = browser.contexts()[0];
const page = context.pages()[0];
```

It's used to automate a browser started by another tool or a cloud browser service. It only works with Chromium, and it has lower fidelity than Playwright's own protocol, so `browserType.connect()` with a Playwright server is preferred when possible.

## 251: How do you test a Chrome extension?

Extensions only work in Chromium with a persistent context. Load the unpacked extension with launch args:

```ts
import { test as base, chromium, type BrowserContext } from "@playwright/test";
import path from "node:path";

export const test = base.extend<{
  context: BrowserContext;
  extensionId: string;
}>({
  context: async ({}, use) => {
    const pathToExtension = path.join(__dirname, "my-extension");
    const context = await chromium.launchPersistentContext("", {
      channel: "chromium",
      args: [
        `--disable-extensions-except=${pathToExtension}`,
        `--load-extension=${pathToExtension}`,
      ],
    });
    await use(context);
    await context.close();
  },
  extensionId: async ({ context }, use) => {
    let [worker] = context.serviceWorkers();
    if (!worker) worker = await context.waitForEvent("serviceworker");
    await use(worker.url().split("/")[2]);
  },
});
```

Then open `chrome-extension://${extensionId}/popup.html` in a page to test the popup. Only Manifest V3 extensions are supported now.

## 252: Can Playwright test Electron apps?

Yes, with the experimental `_electron` API:

```ts
import { _electron as electron, test, expect } from "@playwright/test";

test("app starts", async () => {
  const app = await electron.launch({ args: ["main.js"] });
  const window = await app.firstWindow();
  await expect(window).toHaveTitle("My App");

  const appPath = await app.evaluate(async ({ app }) => app.getAppPath());
  console.log(appPath);

  await app.close();
});
```

`window` is a normal `Page`, so locators and assertions work. `app.evaluate()` runs code in Electron's main process.

## 253: Can Playwright test on real Android or iOS devices?

Playwright has experimental Android support for Chrome on Android and Android WebView, through `_android` and ADB. There is no support for real iOS devices.

For most teams, mobile testing in Playwright means emulation (`devices['iPhone 15']`), which runs a desktop engine with a mobile viewport, user agent and touch. For real device coverage, teams usually use a device cloud or a tool like Appium.

## 254: How do you get the video file of a test?

```ts
test("records", async ({ page }, testInfo) => {
  await page.goto("/");
  // ...
  const videoPath = await page.video()?.path();
  console.log(videoPath);
});
```

The video is complete only after the page or context closes. You can set the video size:

```ts
use: {
  video: { mode: 'retain-on-failure', size: { width: 1280, height: 720 } },
},
```

In Playwright Test, videos are attached to the report automatically, so you rarely need the path yourself.

## 255: What options does page.screenshot have?

```ts
await page.screenshot({
  path: "shot.png",
  fullPage: true, // the whole scrollable page
  clip: { x: 0, y: 0, width: 800, height: 400 }, // one area
  type: "jpeg",
  quality: 80, // jpeg only
  omitBackground: true, // transparent background (png)
  mask: [page.getByTestId("user-email")], // hide sensitive parts
  animations: "disabled",
  caret: "hide",
});
```

## 256: How do you generate a PDF of a page?

Use `page.pdf()`. It only works in Chromium, and the PDF uses print CSS:

```ts
await page.goto("/invoice/42");
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: "invoice.pdf",
  format: "A4",
  printBackground: true,
  margin: { top: "20mm", bottom: "20mm" },
});
```

This is often used in backend services for invoices and reports, not only in tests.

## 257: What does locator.highlight do?

`highlight()` draws a box around the matched elements on the page. It's a debugging helper to see what a locator matches when running headed:

```ts
await page.getByRole("row").filter({ hasText: "Alice" }).highlight();
await page.pause();
```

Don't leave it in committed tests.

## 258: What is globalTimeout?

`globalTimeout` limits how long the whole test run can take. When it is reached, the run stops and the remaining tests are reported as not run.

```ts
export default defineConfig({
  globalTimeout: process.env.CI ? 60 * 60 * 1000 : undefined, // 1 hour on CI
});
```

It protects CI from a stuck run using the runner for hours.

## 259: How do you stop the run after a number of failures?

Use `maxFailures` or `-x`:

```ts
export default defineConfig({
  maxFailures: process.env.CI ? 10 : undefined,
});
```

```bash
npx playwright test -x          # stop after the first failure
npx playwright test --max-failures=5
```

If something basic is broken, like the app not starting, you don't want to wait for hundreds of tests to time out.

## 260: What does preserveOutput do?

`preserveOutput` controls whether files in the test output folder are kept:

- `'always'`: keep output for all tests (default)
- `'failures-only'`: keep output only for failed tests
- `'never'`: delete all output

```ts
export default defineConfig({ preserveOutput: "failures-only" });
```

It is about files that tests write to `testInfo.outputDir`. Screenshot, video and trace modes are controlled separately.

## 261: What does the github reporter do?

On GitHub Actions, the `github` reporter adds annotations for failures, so errors show up in the "Files changed" tab of a pull request, at the right line:

```ts
reporter: process.env.CI ? [['github'], ['html', { open: 'never' }]] : 'list',
```

It is usually combined with another reporter, because annotations alone don't show passed tests or traces.

## 262: How would you migrate tests from Cypress to Playwright?

The main mapping:

| Cypress                 | Playwright                                                  |
| ----------------------- | ----------------------------------------------------------- |
| `cy.visit('/')`         | `await page.goto('/')`                                      |
| `cy.get('[data-cy=x]')` | `page.getByTestId('x')` (with `testIdAttribute: 'data-cy'`) |
| `cy.contains('Save')`   | `page.getByText('Save')` or `getByRole`                     |
| `.should('be.visible')` | `await expect(locator).toBeVisible()`                       |
| `cy.intercept()`        | `page.route()`                                              |
| `cy.wait('@alias')`     | `page.waitForResponse()`                                    |
| `cy.session()`          | `storageState` with a setup project                         |
| custom commands         | fixtures and helper functions                               |

The biggest change is moving from Cypress's command chain to normal `async/await`. A good approach is to migrate the most valuable flows first, run both suites for a while, and switch CI once Playwright covers the same flows.

## 263: How do you change the attribute used by getByTestId?

Set `testIdAttribute` in the config:

```ts
export default defineConfig({
  use: { testIdAttribute: "data-qa" },
});
```

```ts
await page.getByTestId("submit").click(); // finds [data-qa="submit"]
```

This is useful when the app already uses `data-cy`, `data-qa` or `data-test`.

## 264: How do you authenticate API tests?

Either send a token header, or reuse a saved storage state:

```ts
// token in config, for the request fixture
use: {
  baseURL: 'https://api.example.com',
  extraHTTPHeaders: { Authorization: `Bearer ${process.env.API_TOKEN}` },
},
```

```ts
// cookies from a UI login, for a new API context
const api = await request.newContext({
  baseURL: "http://localhost:3000",
  storageState: "playwright/.auth/user.json",
});
const res = await api.get("/api/me");
await expect(res).toBeOK();
```

You can also get a token in a setup project with an API login and save it to a file or environment variable.

## 265: How do you test that a page is protected and redirects to login?

```ts
test.describe("logged out", () => {
  test.use({ storageState: { cookies: [], origins: [] } });

  test("redirects to login", async ({ page }) => {
    await page.goto("/account");
    await expect(page).toHaveURL(/\/login\?next=%2Faccount/);
    await expect(page.getByRole("heading", { name: "Sign in" })).toBeVisible();
  });
});
```

Setting an empty `storageState` makes sure the test is logged out even if the project uses a saved login.

## 266: How do you simulate slow or failing API responses?

```ts
// server error
await page.route("**/api/orders", (route) => route.fulfill({ status: 500 }));

// network failure
await page.route("**/api/orders", (route) => route.abort("failed"));

// slow response
await page.route("**/api/orders", async (route) => {
  await new Promise((resolve) => setTimeout(resolve, 3_000));
  await route.continue();
});
```

These are good for testing error messages, retry buttons and loading states that are hard to trigger with a real backend.

## 267: What is route.fallback?

When several route handlers match the same URL, the last registered one runs first. `route.continue()` sends the request to the network and stops there. `route.fallback()` passes it to the next matching handler instead.

```ts
// general handler, registered first
await page.route("**/*", (route) => {
  const headers = { ...route.request().headers(), "x-e2e": "1" };
  return route.fallback({ headers });
});

// specific handler, registered later, runs first
await page.route("**/api/user", (route) => {
  if (route.request().method() === "GET")
    return route.fulfill({ json: { name: "Alice" } });
  return route.fallback();
});
```

This lets you layer handlers, for example a general one in a fixture and specific ones in tests.

## 268: How do you remove a route handler?

```ts
const handler = (route: Route) => route.fulfill({ json: [] });
await page.route("**/api/items", handler);
// ...
await page.unroute("**/api/items", handler); // remove one handler
await page.unroute("**/api/items"); // remove all handlers for the URL
await page.unrouteAll({ behavior: "wait" }); // remove all, wait for running handlers
```

`unrouteAll` with `behavior: 'ignoreErrors'` is useful at the end of a test when handlers may still be running and the page is closing.

## 269: How do you create a teardown for a setup project?

Add a `teardown` project and point to it from the setup project:

```ts
projects: [
  { name: 'setup db', testMatch: /global\.setup\.ts/, teardown: 'cleanup db' },
  { name: 'cleanup db', testMatch: /global\.teardown\.ts/ },
  { name: 'chromium', use: { ...devices['Desktop Chrome'] }, dependencies: ['setup db'] },
],
```

```ts
// global.teardown.ts
import { test as teardown } from "@playwright/test";

teardown("delete database", async ({}) => {
  await deleteTestDatabase();
});
```

The teardown runs after all projects that depend on the setup are done.

## 270: How do you save files a test creates?

Use `testInfo.outputPath()`. It returns a path inside the test's own output folder, so parallel tests don't overwrite each other's files:

```ts
test("export", async ({ page }, testInfo) => {
  const downloadPromise = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export" }).click();
  const download = await downloadPromise;

  const file = testInfo.outputPath("export.csv");
  await download.saveAs(file);
});
```

## 271: What is page.waitForFunction?

It waits until a function returns a truthy value in the page:

```ts
await page.waitForFunction(() => (window as any).appReady === true);

await page.waitForFunction(
  (count) => document.querySelectorAll(".item").length >= count,
  10,
  { timeout: 10_000 },
);
```

It's useful for app state that isn't visible in the DOM. If the condition is about elements, locators and assertions are easier.

## 272: How do you wait for any page or context event?

Use `waitForEvent` with an optional predicate:

```ts
const consoleMsg = page.waitForEvent("console", (msg) =>
  msg.text().includes("ready"),
);
await page.goto("/");
await consoleMsg;

const requestFinished = page.waitForEvent("requestfinished", (r) =>
  r.url().endsWith("/api/save"),
);
```

Like `waitForResponse`, start waiting before the action that triggers the event.

## 273: What should you watch out for with locator.all()?

`all()` returns a locator for each element that matches **right now**. It doesn't wait for the list to load, and the list can change after you call it.

```ts
// may return 0 items if the list hasn't loaded yet
const items = await page.getByRole("listitem").all();

// wait first
await expect(page.getByRole("listitem")).toHaveCount(5);
for (const item of await page.getByRole("listitem").all()) {
  await expect(item).toContainText("$");
}
```

Each returned locator is based on its position (`nth`), so if items are added or removed while you loop, you may act on the wrong one.

## 274: How do you test several languages or time zones with projects?

```ts
projects: [
  { name: 'en', use: { ...devices['Desktop Chrome'], locale: 'en-US', timezoneId: 'America/New_York' } },
  { name: 'de', use: { ...devices['Desktop Chrome'], locale: 'de-DE', timezoneId: 'Europe/Berlin' } },
  { name: 'ja', use: { ...devices['Desktop Chrome'], locale: 'ja-JP', timezoneId: 'Asia/Tokyo' } },
],
```

In the tests, keep expected text in a translation file and read it with `test.info().project.name` or the `locale` fixture, instead of hardcoding English.

## 275: What options does the HTML reporter have?

```ts
reporter: [['html', {
  open: 'never',             // 'always' | 'never' | 'on-failure'
  outputFolder: 'my-report',
  host: '0.0.0.0',           // for show-report
  port: 9323,
  title: 'Nightly E2E',
  noSnippets: true,          // hide code snippets in steps
}]],
```

You can also set `PLAYWRIGHT_HTML_OPEN=never` as an environment variable. The report is a static site, so you can host it on any static file server or as a CI artifact.

## 276: When would you use the JSON reporter?

When you want to process results with your own scripts, for example to post a summary to Slack, track test durations or find the slowest tests:

```ts
reporter: [['json', { outputFile: 'results.json' }]],
```

```js
const results = require("./results.json");
console.log(results.stats); // expected, unexpected, flaky, skipped, duration
```

For anything that needs results as they happen, write a custom reporter instead.

## 277: How do you create unique test data when tests run in parallel?

Add something unique to names and emails:

```ts
test("register", async ({ page }, testInfo) => {
  const id = `${testInfo.workerIndex}-${Date.now()}`;
  const email = `user-${id}@example.com`;

  await page.goto("/register");
  await page.getByLabel("Email").fill(email);
  // ...
});
```

You can also use `crypto.randomUUID()` or a library like Faker. Unique data stops parallel tests from fighting over the same records, and leftovers from earlier runs won't cause conflicts.

## 278: How do you check the content of a downloaded file?

Save it or read it as a stream, then check the content:

```ts
import fs from "node:fs/promises";

test("csv export", async ({ page }, testInfo) => {
  const downloadPromise = page.waitForEvent("download");
  await page.getByRole("button", { name: "Export CSV" }).click();
  const download = await downloadPromise;

  const file = testInfo.outputPath(download.suggestedFilename());
  await download.saveAs(file);

  const content = await fs.readFile(file, "utf8");
  const lines = content.trim().split("\n");
  expect(lines[0]).toBe("id,name,email");
  expect(lines).toHaveLength(11);
});
```

For files the server generates, you can also call the download URL with `page.request` and check the response directly.

## 279: How do you check that a request was not sent?

Collect matching requests and check the list at the end:

```ts
test("no tracking without consent", async ({ page }) => {
  const trackingRequests: string[] = [];
  page.on("request", (req) => {
    if (req.url().includes("/collect")) trackingRequests.push(req.url());
  });

  await page.goto("/");
  await page.getByRole("button", { name: "Reject all" }).click();
  await page.getByRole("link", { name: "Products" }).click();
  await expect(page.getByRole("heading", { name: "Products" })).toBeVisible();

  expect(trackingRequests).toEqual([]);
});
```

Proving something didn't happen always depends on timing. Do the check after a clear point in the flow, like a page finishing loading.

## 280: How do you check that images loaded correctly?

Check the `naturalWidth` of the image, which is `0` for broken images:

```ts
const images = page.locator("img");
for (const img of await images.all()) {
  await img.scrollIntoViewIfNeeded(); // for lazy-loaded images
  await expect
    .poll(() =>
      img.evaluate(
        (el: HTMLImageElement) => el.complete && el.naturalWidth > 0,
      ),
    )
    .toBe(true);
}
```

You can also listen for failed responses on image requests.

## 281: How do you check for broken links?

Collect the links and request them with the API client:

```ts
test("no broken links on home page", async ({ page, request }) => {
  await page.goto("/");
  const hrefs = await page
    .locator('a[href^="/"]')
    .evaluateAll((links) => [
      ...new Set(links.map((a) => a.getAttribute("href")!)),
    ]);

  for (const href of hrefs) {
    const res = await request.get(href);
    expect.soft(res.status(), `${href} should not be broken`).toBeLessThan(400);
  }
});
```

Soft assertions let you see all broken links in one run.

## 282: How do you test an autocomplete or combobox?

```ts
test("choose a city", async ({ page }) => {
  await page.goto("/booking");
  const city = page.getByRole("combobox", { name: "City" });

  await city.pressSequentially("Tbil");
  await expect(page.getByRole("option")).toHaveCount(1);
  await page.getByRole("option", { name: "Tbilisi" }).click();

  await expect(city).toHaveValue("Tbilisi");
});
```

`pressSequentially` is used because many autocompletes react to key events, and `fill` might not trigger the search. If the search uses a debounce, the assertions wait for it.

## 283: How do you test a date picker?

There are two approaches:

1. Type the date into the input if the picker allows it. This is fast and stable:

```ts
await page.getByLabel("Check-in").fill("2026-03-14");
```

2. Click through the calendar when the picker is what you test:

```ts
await page.getByLabel("Check-in").click();
await page.getByRole("button", { name: "Next month" }).click();
await page.getByRole("gridcell", { name: "14" }).click();
```

Use the Clock API to fix "today", otherwise a test that picks "next month" behaves differently each month.

## 284: How do you type into a rich text editor?

Rich text editors use `contenteditable` elements. `fill()` works on them, but for editors that rely on key events, typing works better:

```ts
const editor = page.getByRole("textbox", { name: "Post body" });
await editor.click();
await page.keyboard.type("Hello ");
await page.keyboard.press("ControlOrMeta+B");
await page.keyboard.type("world");

await expect(editor.locator("strong")).toHaveText("world");
```

## 285: How do you test a slider or range input?

For a native `<input type="range">`, `fill()` sets the value:

```ts
await page.getByRole("slider", { name: "Volume" }).fill("75");
```

For a custom slider, use the keyboard (most accessible sliders support arrow keys) or the mouse:

```ts
const slider = page.getByRole("slider", { name: "Price" });
await slider.focus();
await slider.press("ArrowRight");

const box = (await slider.boundingBox())!;
await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
await page.mouse.down();
await page.mouse.move(box.x + 200, box.y + box.height / 2, { steps: 5 });
await page.mouse.up();
```

## 286: How do you test infinite scroll?

Scroll to the end of the list and check that more items load:

```ts
test("loads more products on scroll", async ({ page }) => {
  await page.goto("/products");
  const items = page.getByRole("article");
  await expect(items).toHaveCount(20);

  await items.last().scrollIntoViewIfNeeded();
  await expect(items).toHaveCount(40);
});
```

Scrolling the last item into view triggers the `IntersectionObserver` most infinite scroll code uses. `toHaveCount` waits until the next page arrives.

## 287: Should you use hooks or fixtures?

Use **hooks** (`beforeEach`, `afterEach`) for setup that only one file needs.

Use **fixtures** when:

- several files need the same setup
- setup and cleanup belong together
- only some tests need the setup (fixtures are lazy, hooks always run)
- you want to share expensive things per worker
- you want to configure things per project

In bigger projects, most shared setup ends up in fixtures, and hooks are used for small, file-specific things like `page.goto()`.

## 288: How do you keep page objects from becoming too large?

- Split by component, not just by page: a `Header`, `ProductCard` or `DataTable` class that pages reuse.
- Keep page objects about locators and actions. Leave most assertions in the tests, so the test shows what it checks.
- Don't wrap every single locator in a method. Expose locators as properties and let tests use them.
- Avoid deep inheritance. Composition (a page that has a `header` property) is easier to follow.

```ts
class ProductCard {
  constructor(readonly root: Locator) {}
  readonly addButton = this.root.getByRole("button", { name: "Add to cart" });
  price() {
    return this.root.getByTestId("price");
  }
}

class ProductsPage {
  constructor(readonly page: Page) {}
  card(name: string) {
    return new ProductCard(
      this.page.getByRole("article").filter({ hasText: name }),
    );
  }
}
```

## 289: How do you test a link with target=_blank?

You can check the attributes, or follow the new tab:

```ts
const link = page.getByRole("link", { name: "Terms" });
await expect(link).toHaveAttribute("target", "_blank");
await expect(link).toHaveAttribute("rel", /noopener/);

const popupPromise = page.waitForEvent("popup");
await link.click();
const popup = await popupPromise;
await expect(popup).toHaveURL(/\/terms/);
```

Checking attributes is faster. Following the link proves the target page works.

## 290: How do you test a tooltip?

Hover over the element, then check the tooltip:

```ts
await page.getByRole("button", { name: "Info" }).hover();
await expect(page.getByRole("tooltip")).toHaveText("Prices include VAT");

await page.mouse.move(0, 0);
await expect(page.getByRole("tooltip")).toBeHidden();
```

If the tooltip is only a `title` attribute, the browser draws it outside the DOM, so check the attribute instead with `toHaveAttribute('title', ...)`.

## 291: How many assertions should a test have?

There's no fixed rule. A test should check one behavior, but that behavior can need several assertions. For example, after placing an order you might check the confirmation message, the order number and the cart being empty.

What to avoid:

- tests with no real assertions (just clicking around)
- huge tests that check many unrelated features, which are hard to debug
- many small tests that each repeat a slow setup just to check one thing

Use `test.step` to structure longer tests and `expect.soft` when you want to see all failures at once.

## 292: What is the difference between page.on and page.once?

`page.on` adds a listener that runs for every event until you remove it. `page.once` runs only for the next event.

```ts
page.once("dialog", (dialog) => dialog.accept());

const logRequest = (req: Request) => console.log(req.url());
page.on("request", logRequest);
// ...
page.off("request", logRequest);
```

A common bug is adding `page.on('dialog', ...)` in a helper that is called several times, so the handler runs more than once and the second `accept()` throws.

## 293: How do you test print styles?

Switch the media type to print and check the page or take a screenshot:

```ts
test("print view hides navigation", async ({ page }) => {
  await page.goto("/invoice/42");
  await page.emulateMedia({ media: "print" });
  await expect(page.getByRole("navigation")).toBeHidden();
  await expect(page).toHaveScreenshot("invoice-print.png");
});
```

Set `media: null` to go back to normal screen media.

## 294: How do you test a modal dialog?

Check that it opens with focus inside, that Escape closes it and that focus goes back:

```ts
test("delete dialog", async ({ page }) => {
  await page.goto("/projects/1");
  const openButton = page.getByRole("button", { name: "Delete project" });
  await openButton.click();

  const dialog = page.getByRole("dialog", { name: "Delete project?" });
  await expect(dialog).toBeVisible();
  await expect(dialog.getByRole("button", { name: "Cancel" })).toBeFocused();

  await page.keyboard.press("Escape");
  await expect(dialog).toBeHidden();
  await expect(openButton).toBeFocused();
});
```

## 295: How do you test keyboard navigation?

Press Tab and check which element has focus:

```ts
test("skip link and tab order", async ({ page }) => {
  await page.goto("/");
  await page.keyboard.press("Tab");
  await expect(
    page.getByRole("link", { name: "Skip to content" }),
  ).toBeFocused();

  await page.keyboard.press("Enter");
  await page.keyboard.press("Tab");
  await expect(page.getByRole("main").getByRole("link").first()).toBeFocused();
});
```

Note that WebKit on macOS doesn't move focus to links with Tab by default, so these tests may need a different expectation per browser.

## 296: How do you test a toast message that disappears quickly?

Web-first assertions start checking right away and retry often, so a toast that stays for a second or two is usually fine:

```ts
await page.getByRole("button", { name: "Save" }).click();
await expect(page.getByRole("status")).toHaveText("Saved");
```

If it's too fast, you can freeze time with the Clock API so the hide timer doesn't fire:

```ts
await page.clock.install();
await page.goto("/settings");
await page.getByRole("button", { name: "Save" }).click();
await expect(page.getByRole("status")).toHaveText("Saved");
await page.clock.runFor(5_000);
await expect(page.getByRole("status")).toBeHidden();
```

## 297: How do you open DevTools automatically in headed mode?

The old `devtools: true` launch option was removed in 1.58. Pass the Chromium flag instead:

```ts
use: {
  launchOptions: {
    args: ['--auto-open-devtools-for-tabs'],
  },
},
```

Combine it with `--headed` or `headless: false`. For most debugging, the trace viewer and UI mode give you the same information without a live DevTools window.

## 298: How should you name and structure a test?

- Name tests by behavior: `'shows an error when the card is declined'`, not `'test 3'` or `'checkout test'`.
- Follow arrange, act, assert: set up state, do the action, check the result.
- Use `describe` blocks for the feature or page, and tags for type (`@smoke`, `@regression`).

```ts
test.describe("checkout", () => {
  test(
    "shows an error when the card is declined",
    { tag: "@payments" },
    async ({ page }) => {
      // arrange
      await page.route("**/api/pay", (route) =>
        route.fulfill({ status: 402, json: { code: "card_declined" } }),
      );
      await page.goto("/checkout");
      // act
      await page.getByRole("button", { name: "Pay" }).click();
      // assert
      await expect(page.getByRole("alert")).toHaveText(
        "Your card was declined",
      );
    },
  );
});
```

## 299: How do you mock GraphQL requests?

All GraphQL requests usually go to one URL, so check the operation name in the body:

```ts
await page.route("**/graphql", async (route) => {
  const { operationName } = route.request().postDataJSON();

  if (operationName === "GetUser") {
    return route.fulfill({
      json: { data: { user: { id: "1", name: "Alice" } } },
    });
  }
  return route.fallback();
});
```

## 300: How do you debug a test that fails only in one browser?

1. Run only that project, headed: `npx playwright test cart.spec.ts --project=webkit --headed`.
2. Open the trace and compare it with a passing run in another browser.
3. Look for browser differences: date and input formats, focus behavior, scrolling, CSS support, and APIs like clipboard or permissions.
4. Check if the app itself is broken in that browser. That is a real bug, not a test problem.
5. If it really is a known limitation, skip with a reason: `test.skip(browserName === 'webkit', 'reason')`.

Many "WebKit-only failures" are real Safari bugs, which is exactly why you run tests there.

---

# Advanced Questions (301-450)

## 301: How does Playwright communicate with the browser?

Playwright uses a client-server design. Your test code (the client) sends commands to a Playwright driver/server, which talks to the browser:

- **Chromium**: Chrome DevTools Protocol (CDP).
- **Firefox**: a Playwright-specific protocol called Juggler, built into a patched Firefox.
- **WebKit**: a Playwright-specific protocol on top of WebKit's inspector protocol, in a patched WebKit.

In Node.js, the client and server run in the same process. In Python, Java and .NET, the client talks to a Node.js driver process over a pipe. All browser communication goes over one persistent connection, unlike WebDriver, which sends a separate HTTP request per command. This is one reason Playwright is fast and can listen to events (network, console, dialogs) as they happen.

## 302: Why does Playwright use its own browser builds?

Firefox and WebKit don't offer the deep automation hooks Playwright needs (network interception, isolated contexts, input events at the right level), so Playwright ships patched builds of them. For Chromium, Playwright now downloads Chrome for Testing builds, since CDP already gives what it needs.

The trade-off: the WebKit build is not the same as real Safari on macOS or iOS. It is close enough to catch most WebKit engine issues, but not things specific to Safari's app or OS integration. Each Playwright version is tied to specific browser versions, which is why you must run `npx playwright install` after upgrading.

## 303: How does auto-waiting work internally?

When you call an action like `click()`:

1. Playwright resolves the locator to an element. If none match, it waits and tries again.
2. It runs the actionability checks for that action: visible, stable (same bounding box over two animation frames), enabled, editable.
3. It scrolls the element into view.
4. It does a hit-target check: the element at the click point must be the target or inside it.
5. It fires the input events.

If a check fails, it waits a bit and starts over from step 1, until the timeout. Because it re-resolves the locator each time, a re-rendered element is handled fine. The error message tells you which check kept failing, for example "element is not stable" or "another element intercepts pointer events".

## 304: What happens internally when a locator is resolved?

A locator is just a description (a chain of selector parts). Nothing happens until you call an action or assertion. Then Playwright sends the selector to an injected script in the page, which runs the selector engines (role, text, css, etc.) against the current DOM.

For actions, if the selector matches more than one element, Playwright throws a strict mode error. For assertions that work on many elements (`toHaveCount`, `toHaveText([...])`), all matches are used. Because the query runs again on each retry, locators never point to a stale element, unlike `ElementHandle`s, which keep a reference to one node.

## 305: What is the hit-target check and why does it fail?

Before a pointer action, Playwright checks that the element at the click point is the target element or one of its children. If another element is on top, you get:

```
<div class="overlay">...</div> intercepts pointer events
```

Common causes:

- a modal, cookie banner or loading overlay covering the page
- a sticky header covering an element after scrolling
- a transparent element on top of a custom checkbox
- an animation still running

The fix depends on the cause: close the overlay (or use `addLocatorHandler`), wait for the loading overlay to be hidden, click the visible label instead of the hidden input, or fix the layout. Using `force: true` skips the check, but a real user would also fail to click.

## 306: How do web-first assertions retry, and how do their timeouts interact?

A web-first assertion runs its check, and if it fails, it re-queries the element and checks again at increasing intervals until it passes or `expect.timeout` (5 s by default) runs out. Each try uses a fresh DOM state.

The assertion timeout is separate from the test timeout. If the test timeout (30 s) ends first, the test fails with "Test timeout exceeded" while waiting. So making `expect.timeout` bigger than the remaining test time has no effect.

Some assertions need extra care:

- `toHaveScreenshot` waits until two screenshots in a row match, then compares with the golden file.
- `not.` assertions retry until the negative is true.
- Generic matchers like `toBe` never retry. Wrap them in `expect.poll` if you need retrying.

## 307: How does Playwright Test isolate tests across workers?

Each worker is a separate Node.js process with its own browser instance. Inside a worker, each test gets a new `BrowserContext`, so cookies, storage and cache are separate.

Things that are **not** isolated by Playwright:

- Module-level variables in your test files and helpers, within one worker. Tests that run one after another in the same worker share them.
- Worker-scoped fixtures, shared by tests in that worker.
- The backend and database, shared by everything.

So tests can still affect each other through global variables or server data. That's your job to manage.

## 308: In what order are fixtures set up, and what timeout do they use?

Fixtures form a dependency graph. Playwright sets up only the fixtures the test (and its hooks) need, plus auto fixtures, in dependency order, and tears them down in reverse order.

Test-scoped fixtures share the test timeout. A slow fixture can eat up the test's time. You can give a fixture its own timeout:

```ts
export const test = base.extend<{ slowData: Data }>({
  slowData: [
    async ({}, use) => {
      const data = await loadBigDataset();
      await use(data);
    },
    { timeout: 60_000 },
  ],
});
```

Worker fixtures have their own timeout, which defaults to the test timeout. Fixture setup and teardown also show up as steps in traces and reports, which helps find slow fixtures.

## 309: What happens to a worker when a test fails?

When a test fails, Playwright throws away that worker process (with its browser and worker fixtures) and starts a new one for the remaining tests. This makes sure a broken state doesn't leak into the next tests.

Consequences:

- `beforeAll` and worker fixtures can run more than once per run.
- Expensive worker setup gets repeated after every failure, so a suite with many failures gets even slower.
- Module-level state is reset after a failure but not between passing tests, which can make bugs appear only in some orders.

## 310: How does Playwright decide which tests run on which worker?

By default, Playwright groups tests by file (and by project). Each file is a unit of work. Workers pick up the next file when they're free, and tests inside a file run in order.

With `fullyParallel: true` or `mode: 'parallel'`, each test is its own unit, so tests from one file can go to different workers. Tests that need the same worker fixture parameters stay grouped where needed.

The order isn't guaranteed, which is why tests must not depend on each other. There is a `--shuffle` option in recent versions to randomize order and find hidden dependencies.

## 311: How do you balance shards so they finish at the same time?

Playwright splits tests evenly by count, not by duration. With `fullyParallel: false`, it splits by file, so a single 10-minute file makes one shard slow.

Ways to balance:

- Turn on `fullyParallel: true` so tests are split one by one.
- Break up very long test files.
- Move slow tests (big imports, long flows) into their own project, possibly with its own shard settings.
- Look at the merged HTML report (the timeline/speedboard views) to see which shard and tests are the slowest.

Some teams write their own split based on past durations, using `--test-list` with a file of test ids for each shard.

## 312: How do you choose the number of workers?

Each worker runs a full browser, which takes CPU and memory. Too many workers makes the machine slow, and slow machines cause timeouts and flakiness.

Rules of thumb:

- Start with the number of CPU cores, or a bit less, and measure.
- Watch memory: each Chromium can take a few hundred MB.
- On small CI runners (2 vCPU), 1-2 workers is often fastest overall.
- Your app and backend also need resources, especially if they run on the same machine.

Check total run time and the flaky rate for a few values. The fastest setting is often lower than you expect, and scaling out with shards is usually better than very high workers on one machine.

## 313: What are the deeper causes of flaky Playwright tests?

Beyond obvious sleeps, common causes are:

- **Actions before the app is ready**: clicking before hydration or before event handlers attach.
- **Not waiting for the result of an action**: navigating away before a save request finished.
- **Race with requests**: starting `waitForResponse` after the click.
- **Shared data**: parallel tests editing the same user or record.
- **Order dependence**: module-level state or leftover data.
- **Time**: tests near midnight, time zones, `Date.now()` in the app.
- **Randomness**: random A/B variants, random data from fakers with edge cases.
- **Environment**: slower CI, fewer CPUs, different fonts for screenshots.
- **Third parties**: analytics, chat widgets, external APIs.
- **Backend**: eventual consistency, caching, rate limits.

The trace usually shows which one it is: compare what the page looked like at the failing action with what the test expected.

## 314: How do you reproduce a flaky test that only fails on CI?

1. Get the trace from the CI artifacts and look at the failing step, the DOM snapshot, network and console.
2. Run it many times locally under load: `--repeat-each=50 --workers=8`.
3. Make your machine slower: run with CI-like workers, throttle CPU with CDP, or run inside the same Docker image.
4. Run the whole file or project, not just the test, since it may depend on order or shared data.
5. Use `--shuffle` to change the order.
6. Check CI-only differences: environment variables, `baseURL`, time zone, locale, screen size, secrets, data.

```ts
// CPU throttling in Chromium
const client = await page.context().newCDPSession(page);
await client.send("Emulation.setCPUThrottlingRate", { rate: 4 });
```

## 315: Why do you start waitForResponse before the action, and when is Promise.all used?

If you start waiting after the action, the response may already have arrived, and you'll wait for a response that never comes. Starting the wait first avoids that race:

```ts
const responsePromise = page.waitForResponse("**/api/save");
await page.getByRole("button", { name: "Save" }).click();
await responsePromise;
```

An older style does the same thing with `Promise.all`:

```ts
const [response] = await Promise.all([
  page.waitForResponse("**/api/save"),
  page.getByRole("button", { name: "Save" }).click(),
]);
```

Both are correct. The "promise first, then action, then await" style is easier to read and is what the docs use now. One thing to watch: if the action throws, the waiting promise is left without a handler, so it can fail later with an unrelated timeout.

## 316: How do you handle clicks that happen before the app is hydrated?

With SSR frameworks (Next.js, Nuxt, Angular SSR), the HTML shows up before JavaScript attaches event handlers. Playwright sees a visible, enabled button and clicks it, but nothing happens because React hasn't hydrated yet.

Fixes:

- Wait for a sign that the app is interactive, like an element only rendered on the client or an attribute the app sets after hydration:

```ts
await page.goto("/");
await expect(page.locator('html[data-hydrated="true"]')).toBeAttached();
```

- Assert the result of the click with retry (`toPass`) when the UI really allows early clicks.
- Fix the app: disable buttons until hydrated, which also helps real users on slow devices.

Avoid `networkidle` as a fix. It's slower and doesn't guarantee hydration.

## 317: How do you choose the waitUntil option for page.goto?

- `'load'` (default): waits for the `load` event, so all images, styles and sync scripts are loaded. It can be slow on pages with heavy assets.
- `'domcontentloaded'`: waits only for the HTML to be parsed. It is faster, and works well when the next step is a web-first assertion anyway.
- `'commit'`: returns as soon as the response starts and the document begins loading. Useful when you only care about the navigation starting.
- `'networkidle'`: discouraged. It waits for 500 ms with no network activity, which may never happen with polling or websockets.

In practice, `'domcontentloaded'` plus an assertion on the content you need is often the fastest stable option.

## 318: What problems come up when running Playwright in containers?

- **Shared memory**: Docker's default `/dev/shm` is 64 MB, and Chromium can crash with "Target closed" or "page crashed". Use `--ipc=host` or a bigger `--shm-size`.
- **Zombie processes**: without an init process, child browser processes can pile up. Use `--init`.
- **Root user**: Chromium needs `--no-sandbox` when running as root, which Playwright handles, but running as a non-root user is safer for untrusted sites.
- **Fonts and locales**: missing fonts change screenshots and text layout. The official image includes common fonts.
- **Version mismatch**: the image tag must match the `@playwright/test` version.
- **Resources**: CPU and memory limits on the container make tests slower and timeouts more likely.

## 319: What changed with Chrome for Testing and the new headless mode?

In the past, headless Chromium was a separate, lighter implementation ("old headless") that behaved a bit differently from real Chrome. Chrome replaced it with "new headless", which is the real browser without a window.

In Playwright:

- Since 1.49, the `chrome` and `msedge` channels use new headless mode.
- Playwright still ships `chromium-headless-shell` for the default headless Chromium runs, which is faster and lighter.
- Since 1.57, Playwright's Chromium builds come from Chrome for Testing.
- You can opt into new headless for the bundled Chromium with `channel: 'chromium'`.

New headless is closer to what users run, so it can catch more real issues, but it is a bit heavier.

## 320: What exactly is stored in a trace, and what are the risks?

A trace zip contains:

- the list of actions with timing and parameters (including text typed into fields)
- DOM snapshots before, during and after each action, with styles and resources
- screenshots for the filmstrip
- network logs with headers and bodies
- console messages and errors
- test source files and attachments

This means traces can contain passwords, tokens, cookies and personal data. Don't attach traces from tests that use real customer data, limit who can download CI artifacts, keep retention short, and consider `trace: { mode: 'on-first-retry', snapshots: true, screenshots: false, sources: false }` style settings if you need smaller or safer traces. Using test-only accounts and fake data is the best protection.

## 321: How much do traces, videos and screenshots cost in run time?

All three add overhead:

- **Trace**: DOM snapshots on every action, plus screenshots. This can make tests noticeably slower and traces can be tens of MB.
- **Video**: the browser encodes frames continuously, which uses CPU for the whole test.
- **Screenshots on failure**: cheap, since it's only one image.

This is why `trace: 'on-first-retry'` and `video: 'retain-on-failure'` or `'on-first-retry'` are common on CI. If you see much slower runs after turning on `trace: 'on'`, that's expected. Use it only while investigating.

## 322: How would you speed up a slow Playwright suite?

Measure first: use the HTML report to find the slowest tests and fixtures. Then:

- **Skip UI for setup**: log in with `storageState`, create data through the API.
- **Parallelize**: `fullyParallel: true`, tune workers, add shards.
- **Remove waits**: delete `waitForTimeout` and `networkidle`.
- **Mock slow third parties**: block analytics and external widgets.
- **Avoid repeating expensive setup**: move it into worker fixtures or setup projects.
- **Reduce artifact cost**: traces and videos only on retry or failure.
- **Run fewer browsers per PR**: Chromium on every PR, all browsers nightly.
- **Run what changed**: `--only-changed` or tag-based smoke runs for PRs.
- **Test the production build**: dev servers compile on demand and are slow.
- **Fix the app**: slow pages make slow tests, which is useful feedback too.

## 323: How do you reuse login state efficiently in a big suite?

- Log in once per role in a setup project and save `storageState` files.
- If tests change account data, use one account per worker (keyed on `parallelIndex`) with a worker fixture.
- Log in through the API instead of the UI when possible, then write the cookies to the storage state file.
- Check if the saved state is still valid before reusing it across runs (for example, compare the token's expiry), to avoid re-logging in on every local run.
- Keep one real UI login test so the login page itself is still tested.

```ts
setup("api login", async ({ request }) => {
  await request.post("/api/login", {
    data: {
      email: process.env.USER_EMAIL,
      password: process.env.USER_PASSWORD,
    },
  });
  await request.storageState({ path: "playwright/.auth/user.json" });
});
```

## 324: How do you scale a Playwright suite to thousands of tests?

- **Structure**: fixtures and page/component objects shared across teams, with clear ownership per folder.
- **Execution**: sharding across many machines, merged reports, and smart selection (tags, `--only-changed`) so PRs don't run everything.
- **Data**: each test creates and owns its data, so tests can run in any order and any shard.
- **Environments**: stable, isolated test environments, often one per PR or per run.
- **Flakiness**: track flaky rates over time, quarantine flaky tests with an owner and deadline, and don't let retries hide problems.
- **Speed budgets**: alert on tests that get much slower.
- **Test pyramid**: push checks that don't need a browser down to API or unit tests.

At this size, the bigger problems are usually test data, environments and ownership, not Playwright itself.

## 325: How would you layer a Playwright test framework?

A common layering:

1. **Config**: `playwright.config.ts` with projects for browsers, environments and setup.
2. **Fixtures**: the entry point for tests. They provide page objects, API clients, test data and logged-in contexts.
3. **Page and component objects**: locators and user actions.
4. **API clients and data builders**: create and delete test data quickly.
5. **Tests**: short, readable, focused on behavior and assertions.

The rule is that tests depend on fixtures, fixtures depend on page objects and API clients, and nothing depends on tests. This keeps changes local: a UI change touches one page object, a data model change touches one builder.

## 326: How do you design a fixture-based framework so tests stay readable?

Have tests ask for what they need by name, and let fixtures hide the plumbing:

```ts
type Fixtures = {
  api: ApiClient;
  newProject: Project;
  projectPage: ProjectPage;
};

export const test = base.extend<Fixtures>({
  api: async ({ request }, use) => use(new ApiClient(request)),

  newProject: async ({ api }, use) => {
    const project = await api.createProject({ name: `p-${Date.now()}` });
    await use(project);
    await api.deleteProject(project.id);
  },

  projectPage: async ({ page, newProject }, use) => {
    const projectPage = new ProjectPage(page);
    await projectPage.goto(newProject.id);
    await use(projectPage);
  },
});
```

```ts
test("rename project", async ({ projectPage }) => {
  await projectPage.rename("Renamed");
  await expect(projectPage.title).toHaveText("Renamed");
});
```

Since fixtures are lazy, a test that only needs `api` doesn't pay for a browser page.

## 327: How do you type fixtures properly in TypeScript?

`test.extend` takes two type parameters: test-scoped fixtures and worker-scoped fixtures. Options are typed the same way and the config can be typed with `defineConfig<Options>()`.

```ts
type TestFixtures = { todoPage: TodoPage };
type WorkerFixtures = { account: { email: string; password: string } };
export type Options = { apiURL: string };

export const test = base.extend<TestFixtures & Options, WorkerFixtures>({
  apiURL: ["http://localhost:4000", { option: true }],
  account: [
    async ({}, use, workerInfo) => {
      await use({
        email: `user${workerInfo.workerIndex}@test.dev`,
        password: "pw",
      });
    },
    { scope: "worker" },
  ],
  todoPage: async ({ page }, use) => use(new TodoPage(page)),
});
```

With this, `test.use({ apiURL: '...' })` and config `use` are type-checked, and wrong fixture names fail at compile time.

## 328: How do you pass environment-specific config into tests cleanly?

Make it an option fixture instead of reading `process.env` everywhere:

```ts
export type EnvOptions = { env: { apiURL: string; adminEmail: string } };

export const test = base.extend<EnvOptions>({
  env: [
    { apiURL: "http://localhost:4000", adminEmail: "admin@local" },
    { option: true },
  ],
});
```

```ts
// playwright.config.ts
const environments = {
  staging: {
    apiURL: "https://api.staging.example.com",
    adminEmail: "qa@example.com",
  },
};

export default defineConfig<EnvOptions>({
  projects: [
    {
      name: "staging",
      use: {
        baseURL: "https://staging.example.com",
        env: environments.staging,
      },
    },
  ],
});
```

Tests then use `({ env })` and don't care where the values come from. It's also easy to override in one test with `test.use`.

## 329: How do you keep server data isolated when tests run in parallel?

Options from simple to strong:

1. **Unique data per test**: unique names, emails and ids, so tests don't touch each other's records.
2. **Account per worker**: tests in different workers use different users or tenants.
3. **Tenant per test**: create an org or workspace per test through the API, if the app supports multi-tenancy.
4. **Database per worker**: each worker gets its own schema or database, and the app routes requests by a header:

```ts
export const test = base.extend<{}, { dbName: string }>({
  dbName: [
    async ({}, use, workerInfo) => {
      const name = `test_${workerInfo.parallelIndex}`;
      await createDatabaseFromTemplate(name);
      await use(name);
    },
    { scope: "worker" },
  ],
});
```

The stronger the isolation, the more setup work, but the fewer "random" failures.

## 330: What are the options for resetting the database between tests?

- **Truncate and seed** before the run (setup project). Simple, but tests during the run still share state.
- **Transaction rollback** per test. Common in backend tests but hard in E2E, since the app uses its own connections.
- **Template database clone** (for example `CREATE DATABASE ... TEMPLATE` in Postgres) per worker or per test. Fast and fully isolated.
- **Snapshot restore** of a Docker volume or DB snapshot.
- **Test-only reset endpoint** that the app exposes only in test environments.
- **No reset**: every test creates its own data and never relies on what's already there.

For E2E against a shared staging environment, "no reset, unique data, clean up after" is often the only option. For CI with its own database, cloning templates per worker works very well.

## 331: How do you test a real-time feature with two users?

Use two browser contexts in one test:

```ts
test("chat message arrives for other user", async ({ browser }) => {
  const alice = await browser.newContext({
    storageState: "playwright/.auth/alice.json",
  });
  const bob = await browser.newContext({
    storageState: "playwright/.auth/bob.json",
  });
  const alicePage = await alice.newPage();
  const bobPage = await bob.newPage();

  await alicePage.goto("/chat/room-1");
  await bobPage.goto("/chat/room-1");

  await alicePage.getByRole("textbox", { name: "Message" }).fill("Hi Bob");
  await alicePage.keyboard.press("Enter");

  await expect(bobPage.getByRole("log")).toContainText("Hi Bob");

  await alice.close();
  await bob.close();
});
```

Each context is a separate session, so they act like two different people. Close the contexts at the end, since only the built-in `context` fixture is closed for you.

## 332: How do you test WebSocket behavior beyond simple mocks?

With `routeWebSocket`, you can sit between the page and the real server and change messages in both directions:

```ts
await page.routeWebSocket("wss://example.com/live", (ws) => {
  const server = ws.connectToServer();

  ws.onMessage((message) => {
    // page -> server
    server.send(message);
  });

  server.onMessage((message) => {
    // server -> page, drop heartbeat messages
    if (message !== '{"type":"heartbeat"}') ws.send(message);
  });
});
```

This lets you test things like reconnect logic (close the socket with `ws.close()`), out-of-order messages, or a message the real server rarely sends. To only watch traffic, use `page.on('websocket')` and its `framesent` and `framereceived` events.

## 333: What are the downsides of HAR-based mocking and how do you manage them?

Downsides:

- HAR files get stale when the API changes, so tests pass against old responses.
- They can be big and hard to review in pull requests.
- They may contain tokens, cookies or personal data.
- Matching is by URL and method (and body for POST), so changing query params or bodies can cause misses.

Ways to manage them:

- Only record the API URLs you need (`url: '**/api/**'`) and use `content: 'attach'` or `'omit'` to keep them smaller.
- Re-record on a schedule or when the API changes, with `update: true`.
- Strip secrets before committing.
- Keep a few tests running against the real backend so you notice when it changes.

## 334: How do you combine Playwright API tests with schema validation?

Playwright's `request` sends calls, and a schema library checks the shape of the response:

```ts
import { z } from "zod";

const User = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  createdAt: z.string().datetime(),
});

test("GET /users/:id matches the contract", async ({ request }) => {
  const res = await request.get("/api/users/123");
  await expect(res).toBeOK();
  const parsed = User.safeParse(await res.json());
  expect(parsed.success, JSON.stringify(parsed.error?.issues)).toBe(true);
});
```

If the frontend and these tests share the same schema, a backend change that breaks the frontend's assumptions fails here before it fails in the UI. For real contract testing between teams, tools like Pact are a better fit.

## 335: How do you make visual tests stable across machines?

Rendering depends on the OS, fonts, GPU, browser version and even CPU, so the main rule is: generate and compare screenshots in the same environment.

- Run visual tests in the official Playwright Docker image, both locally (to update snapshots) and in CI.
- Pin the Playwright version so the browser doesn't change underneath you.
- Make content deterministic: mock data, fix time with the Clock API, fix random values.
- Wait for fonts: `await page.evaluate(() => document.fonts.ready)`.
- Hide or mask dynamic parts.
- Use small tolerances (`maxDiffPixelRatio`) only for anti-aliasing noise, not to hide real changes.

## 336: How do you organize snapshots for many browsers and platforms?

By default, each project and platform gets its own snapshot (`name-chromium-linux.png`). With many projects this gets heavy. Options:

- Run visual tests in only one project (for example Chromium in Linux Docker), and use other browsers for functional tests.
- Use `snapshotPathTemplate` to control the folder layout, for example putting snapshots in a folder per project:

```ts
snapshotPathTemplate: '{testDir}/__snapshots__/{projectName}/{testFilePath}/{arg}{ext}',
```

- Use `{platform}` only if you really compare on several OSes. Dropping it means all OSes share one baseline, which only works if all runs happen in the same Docker image.

## 337: What is stylePath used for in screenshot assertions?

`stylePath` injects a CSS file while taking the screenshot. It's a clean way to hide or freeze dynamic parts without changing the app:

```css
/* screenshot.css */
[data-testid="clock"],
.ad-slot,
.avatar img {
  visibility: hidden !important;
}
* {
  caret-color: transparent !important;
}
```

```ts
export default defineConfig({
  expect: {
    toHaveScreenshot: { stylePath: "./screenshot.css" },
  },
});
```

The CSS is only applied during screenshots, so it doesn't affect the rest of the test.

## 338: When do you use visual, ARIA or DOM assertions?

- **DOM/web-first assertions** (`toHaveText`, `toBeVisible`): for specific behavior. Precise and easy to understand when they fail.
- **ARIA snapshots** (`toMatchAriaSnapshot`): for checking structure and content of a section (a menu, a form, a table) without caring about styling. Less brittle than screenshots, and they also check accessibility.
- **Visual snapshots** (`toHaveScreenshot`): for layout and styling, like a broken CSS change, overlapping elements or wrong colors. Most sensitive and the most expensive to keep stable.

A good suite uses mostly web-first assertions, ARIA snapshots for bigger structures, and a small number of visual tests for key pages and components.

## 339: What are the limits of automated accessibility testing with Playwright?

Axe and similar tools catch maybe a third to half of WCAG issues: missing labels, low contrast, invalid ARIA, missing alt text, duplicate ids. They can't judge:

- if alt text is actually meaningful
- if focus order makes sense
- if a custom widget is usable with a keyboard
- if screen reader announcements are clear
- if content makes sense when zoomed

With Playwright you can cover some of this by writing explicit tests: keyboard navigation, focus management in dialogs, `toHaveAccessibleName`, ARIA snapshots, and emulation of `forcedColors` or `reducedMotion`. Manual testing with real assistive tools is still needed.

## 340: How can Playwright be used for security testing?

Playwright isn't a security scanner, but it's useful for checking security behavior in flows:

- **Headers**: check responses for CSP, `Strict-Transport-Security`, `X-Content-Type-Options`.
- **Cookies**: check `HttpOnly`, `Secure` and `SameSite` with `context.cookies()`.
- **Access control**: log in as a low-privilege user and try to open admin pages or call admin APIs.
- **XSS checks**: enter payloads in inputs and assert that no dialog opens and the payload is shown as text.
- **Session handling**: check logout invalidates the session, and that old cookies don't work.

```ts
test("stored XSS payload is not executed", async ({ page }) => {
  let dialogOpened = false;
  page.on("dialog", (d) => {
    dialogOpened = true;
    return d.dismiss();
  });

  await page.goto("/profile");
  await page.getByLabel("Bio").fill("<img src=x onerror=alert(1)>");
  await page.getByRole("button", { name: "Save" }).click();
  await page.reload();

  expect(dialogOpened).toBe(false);
});
```

It can also drive the app through a proxy like OWASP ZAP so the scanner sees real authenticated traffic.

## 341: What is bypassCSP and when would you use it?

`bypassCSP: true` makes the browser ignore the page's Content Security Policy:

```ts
test.use({ bypassCSP: true });
```

It's needed when you inject scripts or styles that the CSP would block, like `addScriptTag` with a test library or axe running in a strict CSP page. The risk is that you no longer test the real CSP, so a CSP that breaks your own app won't fail the tests. Keep at least one project running without it.

## 342: How do you test a login with two-factor authentication (TOTP)?

Use a test account with a known TOTP secret, and generate the code in the test:

```ts
import { TOTP } from "otpauth";

test("login with 2FA", async ({ page }) => {
  const totp = new TOTP({ secret: process.env.TEST_TOTP_SECRET! });

  await page.goto("/login");
  await page.getByLabel("Email").fill(process.env.USER_EMAIL!);
  await page.getByLabel("Password").fill(process.env.USER_PASSWORD!);
  await page.getByRole("button", { name: "Sign in" }).click();

  await page.getByLabel("Authentication code").fill(totp.generate());
  await page.getByRole("button", { name: "Verify" }).click();
  await expect(page).toHaveURL("/dashboard");
});
```

Do this in the auth setup project and save `storageState`, so the 2FA flow runs once and not in every test. For SMS or email codes, read the code from a test inbox or an SMS provider's test API.

## 343: How do you handle third-party login like Google or Okta in tests?

Automating real third-party login pages is fragile: they change, add bot detection and CAPTCHAs, and may block automated logins. Better options:

- Use the provider's test tenant or a test IdP you control (for example Keycloak in Docker) for a few real login tests.
- In most tests, skip the provider: log in through a test-only backend endpoint or create a session token directly, then save `storageState`.
- Mock the redirect callback in lower environments.
- Keep at least one test that goes through the full flow against a sandbox, so you know the integration still works.

## 344: How do you test passkeys or WebAuthn?

In Chromium you can use a virtual authenticator through CDP:

```ts
test("register a passkey", async ({ page }) => {
  const client = await page.context().newCDPSession(page);
  await client.send("WebAuthn.enable");
  await client.send("WebAuthn.addVirtualAuthenticator", {
    options: {
      protocol: "ctap2",
      transport: "internal",
      hasResidentKey: true,
      hasUserVerification: true,
      isUserVerified: true,
    },
  });

  await page.goto("/settings/security");
  await page.getByRole("button", { name: "Add passkey" }).click();
  await expect(page.getByText("Passkey added")).toBeVisible();
});
```

The virtual authenticator answers WebAuthn requests without a real device. Recent Playwright versions also added a built-in credentials API for this, so check the docs for your version. The CDP way only works in Chromium.

## 345: How do you deal with CAPTCHA in automated tests?

You don't solve it. CAPTCHAs are designed to block automation. Options:

- Turn CAPTCHA off in test environments with a config flag.
- Use the provider's test keys (reCAPTCHA and hCaptcha have site keys that always pass).
- Allow-list the test runner's IPs or send a secret header that the backend checks.
- Mock the verification call on the backend in test environments.

If you have to run against production, test the flows that come after CAPTCHA using a session created another way.

## 346: How do you keep storageState files secure?

Storage state files contain real session cookies and tokens. Anyone with the file can act as that user until the session expires.

- Add the auth folder to `.gitignore`.
- Generate them at the start of each CI run, don't cache them across runs or share them as artifacts.
- Use test accounts with limited permissions, never real users or admins with production access.
- Keep session lifetimes short in test environments.
- Be careful with traces and HTML reports, which can contain the same cookies in network logs.

## 347: What are the limits of passing data to and from page.evaluate?

Arguments and return values are serialized between Node.js and the browser. Supported types are JSON-like values plus some extras: `Date`, `RegExp`, `Map`, `Set`, `URL`, typed arrays, `undefined`, `NaN`, `Infinity`, `-0`, `BigInt`, `Error`, and `JSHandle`/`ElementHandle`s.

What doesn't work:

- Functions and closures can't be passed as values. The function you evaluate also can't use variables from the test file.
- Class instances lose their prototype.
- DOM nodes can't be returned as values, only as handles (`evaluateHandle`).
- Huge results are slow, since everything goes over the protocol.

```ts
const minPrice = 10;
// wrong: minPrice is not defined in the browser
await page.evaluate(
  () => document.querySelectorAll(`[data-price]`).length > minPrice,
);
// right
await page.evaluate(
  (min) => document.querySelectorAll("[data-price]").length > min,
  minPrice,
);
```

## 348: What is the difference between exposeFunction and exposeBinding?

Both add a function to `window` that runs in Node.js. `exposeBinding` also passes a `source` object with the `page`, `frame` and `context` that made the call:

```ts
await context.exposeBinding(
  "reportEvent",
  async ({ page, frame }, name: string) => {
    console.log(`event ${name} from ${frame.url()}`);
  },
);
```

Use it when you need to know which page or frame called you, for example when collecting analytics events from several frames.

## 349: How do you make the app deterministic using addInitScript?

Override sources of randomness and environment before the app's code runs:

```ts
await context.addInitScript(() => {
  let seed = 42;
  Math.random = () => {
    seed = (seed * 16807) % 2147483647;
    return (seed - 1) / 2147483646;
  };

  localStorage.setItem("experiment:checkout", "variant-b");
  (window as any).__DISABLE_ANIMATIONS__ = true;
});
```

Combine this with the Clock API for time and `route` for data, and the same test gets the same page every run. This is especially important for visual tests.

## 350: What should you know about the Clock API in more depth?

- `clock.install()` replaces `Date`, `setTimeout`, `setInterval`, `requestAnimationFrame`, `performance.now` and similar in the page. After install, time only moves when you tell it to (or it keeps running if you only set a time without pausing).
- `setFixedTime()` makes `Date.now()` always return the same value but leaves timers working normally. Good when you only care about "what day is it".
- `fastForward()` jumps ahead and fires due timers once, like a laptop waking from sleep.
- `runFor()` moves time forward step by step and fires every timer along the way, like time really passing.
- `pauseAt()` moves to a time and stops there, so you can step from a known point.

Install it before `page.goto()`, otherwise the page already captured the real timers. The clock applies to the browser context, so it doesn't affect your backend's time.

## 351: How do you test time zone and daylight saving time bugs?

Run the same test in several time zones and around DST changes:

```ts
for (const timezoneId of [
  "America/New_York",
  "Europe/London",
  "Asia/Kolkata",
  "Pacific/Auckland",
]) {
  test.describe(timezoneId, () => {
    test.use({ timezoneId });

    test("meeting shows the right local time on DST day", async ({ page }) => {
      await page.clock.setFixedTime(new Date("2026-03-29T00:30:00Z")); // EU DST change
      await page.goto("/meetings/42");
      await expect(page.getByTestId("meeting-time")).not.toHaveText(
        "Invalid Date",
      );
    });
  });
}
```

Time zones with non-hour offsets (Kolkata, +5:30) and the southern hemisphere (Auckland) catch many bugs. The backend's time zone is separate, so make sure your test environment's server time zone is also known.

## 352: In what order do route handlers run, and how do page and context routes interact?

- Handlers are checked in reverse order of registration. The last one added runs first.
- If a handler calls `fulfill`, `abort` or `continue`, that ends it. If it calls `fallback`, the next matching handler runs.
- Page routes run before context routes. If no page route handles the request (or they all fall back), context routes are checked.

This lets you put general rules on the context (block trackers, add headers) and specific mocks on the page in tests. If a mock "doesn't work", check whether a later handler for a broader pattern catches the request first.

## 353: Do route handlers catch requests from web workers and service workers?

- Requests from dedicated web workers go through context routing, so `context.route()` catches them.
- Requests made by a service worker go through `context.route()` in Chromium, but the page's own requests may be answered by the service worker's cache before routing sees them. That's why `serviceWorkers: 'block'` is recommended when you mock the network.
- `page.route()` only sees requests made by that page, not by the service worker.

When a mock doesn't apply, look at the network tab in the trace to see who made the request.

## 354: How do you simulate a slow network?

Playwright doesn't have a built-in throttle option, but there are two ways:

1. Delay specific responses with `route` (works in all browsers):

```ts
await page.route("**/api/**", async (route) => {
  await new Promise((r) => setTimeout(r, 2_000));
  await route.continue();
});
```

2. Use CDP in Chromium to throttle everything:

```ts
const client = await page.context().newCDPSession(page);
await client.send("Network.emulateNetworkConditions", {
  offline: false,
  latency: 400,
  downloadThroughput: (500 * 1024) / 8,
  uploadThroughput: (500 * 1024) / 8,
});
```

The CDP way is closer to a real slow connection, since it affects all resources including scripts and images.

## 355: When and how would you use a CDPSession?

A `CDPSession` sends raw Chrome DevTools Protocol commands. Use it for things Playwright doesn't expose, only in Chromium:

```ts
const client = await page.context().newCDPSession(page);

await client.send("Emulation.setCPUThrottlingRate", { rate: 6 });
await client.send("Performance.enable");
const { metrics } = await client.send("Performance.getMetrics");

client.on("Network.webSocketFrameReceived", (e) =>
  console.log(e.response.payloadData),
);
await client.send("Network.enable");
```

Common uses: CPU throttling, performance metrics, heap snapshots, WebAuthn, and coverage details. Tests that use CDP can't run in Firefox or WebKit, so skip them there or put them in a Chromium-only project.

## 356: How do you measure Web Vitals or page performance in Playwright?

Read performance data from the page:

```ts
test("LCP is under 2.5s", async ({ page }) => {
  await page.goto("/");
  const lcp = await page.evaluate(
    () =>
      new Promise<number>((resolve) => {
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          resolve(entries[entries.length - 1].startTime);
        }).observe({ type: "largest-contentful-paint", buffered: true });
      }),
  );
  expect(lcp).toBeLessThan(2_500);
});
```

You can also read `performance.getEntriesByType('navigation')` for TTFB and load times, or inject the `web-vitals` library with `addInitScript`.

Be careful about using these as hard gates: CI machines are noisy, and lab numbers differ from real users. Track trends over time, and use fixed throttling and several runs if you do set budgets.

## 357: How do you run Lighthouse together with Playwright?

Lighthouse needs Chromium with a remote debugging port. Launch the browser with one, log in with Playwright, then run Lighthouse against the same browser:

```ts
import { chromium } from "playwright";
import lighthouse from "lighthouse";

const browser = await chromium.launch({
  args: ["--remote-debugging-port=9222"],
});
const page = await browser.newPage();
await page.goto("http://localhost:3000/login");
// ... log in with Playwright

const result = await lighthouse("http://localhost:3000/dashboard", {
  port: 9222,
  output: "json",
  onlyCategories: ["performance", "accessibility"],
});
console.log(result?.lhr.categories.performance.score);
await browser.close();
```

Community packages like `playwright-lighthouse` wrap this. Lighthouse runs are slow, so keep them in a separate project or a nightly job.

## 358: How can you detect memory leaks with Playwright?

In Chromium, you can measure the JS heap before and after repeating an action many times:

```ts
test("opening and closing the modal does not leak", async ({ page }) => {
  await page.goto("/");
  const client = await page.context().newCDPSession(page);

  const heap = async () => {
    await client.send("HeapProfiler.collectGarbage");
    return (await page.evaluate(
      () => (performance as any).memory.usedJSHeapSize,
    )) as number;
  };

  const before = await heap();
  for (let i = 0; i < 50; i++) {
    await page.getByRole("button", { name: "Open" }).click();
    await page.getByRole("button", { name: "Close" }).click();
  }
  const after = await heap();

  expect(after - before).toBeLessThan(5 * 1024 * 1024);
});
```

`performance.memory` is Chromium-only and not very precise. For deeper analysis, take heap snapshots through CDP and compare them, or use tools like Meta's MemLab, which uses Puppeteer for the same idea.

## 359: How do you collect JavaScript code coverage with Playwright?

Chromium has a coverage API:

```ts
test("collect coverage", async ({ page }) => {
  await page.coverage.startJSCoverage();
  await page.goto("/");
  await page.getByRole("button", { name: "Load more" }).click();
  const coverage = await page.coverage.stopJSCoverage();
  // coverage is in V8 format, convert with a tool like v8-to-istanbul or monocart-coverage-reports
});
```

Another approach is to build the app with Istanbul instrumentation and read `window.__coverage__` after each test. Either way, E2E coverage is useful for finding untested areas, but chasing a high E2E coverage number is usually not worth the effort.

## 360: How does the reporter API work in more detail?

A reporter gets events during the run:

- `onConfigure(config)` and `onBegin(config, suite)`: before tests run. `suite` holds the full tree of projects, files, describes and tests.
- `onTestBegin(test, result)` and `onTestEnd(test, result)`: per test attempt. Retries call these again with a new `result`.
- `onStepBegin` / `onStepEnd`: for each step, including hooks, fixtures and `expect` calls.
- `onStdOut` / `onStdErr`: output from tests.
- `onError(error)`: errors outside tests, like a broken config.
- `onEnd(result)`: the overall status. It can return a new status.
- `onExit()`: last chance for async work, like uploading results.
- `printsToStdio()`: return `false` if your reporter doesn't print, so Playwright adds a default terminal reporter.

`test.outcome()` gives `'expected'`, `'unexpected'`, `'flaky'` or `'skipped'`, which is easier than reading each attempt yourself.

## 361: How do you create a custom selector engine?

Register it with `selectors.register()` before creating pages:

```ts
import { test as base, selectors } from "@playwright/test";

export const test = base.extend<{}, { registerSelectors: void }>({
  registerSelectors: [
    async ({}, use) => {
      await selectors.register("tag", () => ({
        query(root: Element, selector: string) {
          return root.querySelector(selector);
        },
        queryAll(root: Element, selector: string) {
          return Array.from(root.querySelectorAll(selector));
        },
      }));
      await use();
    },
    { scope: "worker", auto: true },
  ],
});
```

```ts
await page.locator("tag=button").click();
```

It's rarely needed. Most of the time `getBy*`, `filter` and `testIdAttribute` cover it. It can be useful for apps with their own component markers.

## 362: How do you write stable locators for an app with poor accessibility and no test ids?

- Start by adding test ids or proper labels to the app if you can. It's often a small change and the best long-term fix.
- If you can't change the app, anchor on stable things: visible text the business cares about, a nearby label, or a section heading, then go down from there:

```ts
const billing = page
  .locator("section")
  .filter({ has: page.getByRole("heading", { name: "Billing" }) });
await billing.locator("input").first().fill("...");
```

- Avoid generated class names (`.css-1x2y3z`), deep CSS paths and index-based XPath.
- Keep the ugly locators in page objects, so when the app gets better you change one place.

Hard-to-locate elements are also often hard for screen reader users, so it's worth reporting.

## 363: How do you test a virtualized list?

A virtualized list only renders the rows on screen. Rows that are far away don't exist in the DOM, so `getByText('Item 500')` fails even though the item is "in the list".

Approaches:

- Scroll the container until the item appears:

```ts
const list = page.getByTestId("virtual-list");
const target = page.getByText("Item 500");

await expect(async () => {
  await list.evaluate((el) => el.scrollBy(0, 400));
  await expect(target).toBeVisible({ timeout: 200 });
}).toPass({ timeout: 20_000 });
```

- Use the app's search or filter to bring the item to the top. This is usually the more realistic user path.
- Don't use `toHaveCount` to count all items. Check the total from the UI's counter or the API.

## 364: How do you test a canvas or WebGL app?

Playwright can't see inside a `<canvas>`, so you use other signals:

- **Screenshots**: `toHaveScreenshot` on the canvas element, with fixed data and time.
- **App state**: expose state on `window` in test builds and read it with `evaluate`.
- **Pixel checks**: read pixels with `evaluate` and `getContext('2d').getImageData()`.
- **Mouse input by coordinates**: use `page.mouse` with positions relative to the canvas's `boundingBox()`.

```ts
const canvas = page.locator("canvas#editor");
const box = (await canvas.boundingBox())!;
await page.mouse.click(box.x + 100, box.y + 50);
await expect
  .poll(() => page.evaluate(() => (window as any).editor.shapes.length))
  .toBe(1);
```

WebGL can render differently across GPUs and headless modes, so screenshot tests on WebGL often need to run in one fixed environment, sometimes with GPU flags.

## 365: Why does dragTo sometimes not work, and what can you do?

`dragTo` uses mouse events. It works for libraries based on mouse or pointer events. Problems come up with:

- **Native HTML5 drag and drop** in some browsers and libraries, which listen for `dragstart`, `dragover` and `drop` with a `DataTransfer`.
- **Libraries that need several move events** or a minimum distance before a drag starts.

Fixes:

```ts
// step by step with several moves
await page.getByText("Card A").hover();
await page.mouse.down();
await page.getByTestId("column-done").hover();
await page.getByTestId("column-done").hover({ position: { x: 20, y: 20 } });
await page.mouse.up();

// or dispatch HTML5 drag events yourself
const dataTransfer = await page.evaluateHandle(() => new DataTransfer());
await page.getByText("Card A").dispatchEvent("dragstart", { dataTransfer });
await page.getByTestId("column-done").dispatchEvent("drop", { dataTransfer });
```

Dispatching events is less realistic but works when the library only checks the events.

## 366: How do you test hover menus that close too fast?

A menu might close when the mouse moves across a gap between the trigger and the menu. Playwright moves the mouse in a straight line when you `hover()` the menu item, which may pass over empty space.

Fixes:

- Hover the trigger, then move directly onto the item with `hover()` on the item. Playwright doesn't stop in between, so it usually works.
- If the menu also opens on click or keyboard (it should, for accessibility), use that instead.
- Use `page.mouse.move(x, y, { steps })` to control the path.
- If the app adds a close delay on mouse leave, the test may need to move faster, not slower. Avoid `slowMo` here.

## 367: What does "element is not attached to the DOM" mean?

It means the element was removed or replaced while Playwright was working with it, usually because the framework re-rendered it.

With locators, Playwright retries and finds the new element, so this is rare. You mostly see it with:

- `ElementHandle`s, which point to the old node
- `locator.all()` results used after the list re-rendered
- `evaluate` on an element that was replaced between resolve and run

Fix it by using locators and assertions instead of handles, waiting for the list to be stable (`toHaveCount`) before iterating, and re-querying after actions that trigger re-renders.

## 368: How do you avoid strict mode violations in dynamic lists?

Instead of `nth()`, find the item by its content, then act inside it:

```ts
// fragile: index may change when sorting or new items arrive
await page.getByRole("button", { name: "Edit" }).nth(2).click();

// stable: the row that is about this order
const row = page.getByRole("row").filter({ hasText: "Order #1042" });
await row.getByRole("button", { name: "Edit" }).click();
```

If even the content isn't unique (two "Untitled" rows), make the test data unique, or use test ids that include the record id (`data-testid="order-1042"`).

## 369: Can Playwright reach elements in closed shadow roots?

No. Closed shadow roots are hidden from outside JavaScript by design, and Playwright's selectors can't go into them. Options:

- Ask the component authors to use open shadow roots in test builds, or expose the needed parts via attributes or slots.
- Interact at the host level: keyboard input after focusing the host, or clicks at coordinates.
- Check the result in the light DOM or the app state instead of inside the component.

## 370: How does Playwright handle cross-origin iframes?

Playwright can work with cross-origin iframes, including when the browser runs them in a separate process (site isolation). `frameLocator()` and `contentFrame()` work the same as for same-origin frames.

Things to know:

- `page.evaluate()` runs only in the main frame. Use `frame.evaluate()` or a locator inside the frame.
- Some providers (payment forms, for example) build their iframes dynamically and nest them. Use a locator that matches by `title` or `name` rather than by position.
- If the iframe loads slowly, frame locators wait for it like any other element.

## 371: How do you handle an OAuth login popup window?

Wait for the popup, work in it, and wait for it to close:

```ts
const popupPromise = page.waitForEvent("popup");
await page.getByRole("button", { name: "Sign in with Provider" }).click();
const popup = await popupPromise;

await popup.getByLabel("Email").fill(process.env.SSO_USER!);
await popup.getByLabel("Password").fill(process.env.SSO_PASS!);
await popup.getByRole("button", { name: "Allow" }).click();

await popup.waitForEvent("close");
await expect(page.getByText("Signed in")).toBeVisible();
```

Context-level routes, init scripts and settings apply to popups too, since they're in the same context.

## 372: How do you test syncing between tabs of the same user?

Open two pages in the same context. They share storage, so `storage` events and `BroadcastChannel` work as in a real browser:

```ts
test("logout in one tab logs out the other", async ({ context }) => {
  const tab1 = await context.newPage();
  const tab2 = await context.newPage();
  await tab1.goto("/dashboard");
  await tab2.goto("/dashboard");

  await tab1.getByRole("button", { name: "Log out" }).click();

  await expect(tab2.getByRole("heading", { name: "Signed out" })).toBeVisible();
});
```

Background tabs may be throttled by the browser in headed mode, so if the app uses timers to sync, the other tab may update slower than you expect.

## 373: How do downloads work when the browser runs on a remote machine?

When you connect to a remote browser with `browserType.connect()`, files are downloaded on the remote machine. Playwright streams them back when you call `download.saveAs()` or `download.createReadStream()`. `download.path()` doesn't work with remote browsers, because the path is on the other machine.

```ts
const download = await downloadPromise;
const stream = await download.createReadStream();
// or
await download.saveAs(testInfo.outputPath("file.zip"));
```

So, in shared fixtures, use `saveAs` or streams, not `path()`, if the suite may run against remote browsers.

## 374: How do you test dropping files onto a drop zone?

A drop zone that listens for `drop` needs a `DataTransfer` with files. Create it in the page:

```ts
const dataTransfer = await page.evaluateHandle(() => {
  const dt = new DataTransfer();
  const file = new File(["hello world"], "hello.txt", { type: "text/plain" });
  dt.items.add(file);
  return dt;
});

await page.getByTestId("dropzone").dispatchEvent("drop", { dataTransfer });
await expect(page.getByText("hello.txt")).toBeVisible();
```

If the drop zone also has a hidden `<input type=file>`, `setInputFiles()` on it is simpler and tests the same upload logic. Recent Playwright versions also added a `locator.drop()` helper, so check the docs for your version.

## 375: What are the cross-browser issues with clipboard tests?

- **Chromium**: needs `clipboard-read`/`clipboard-write` permissions for the async clipboard API.
- **Firefox**: these permissions don't exist in the same way, and reading the clipboard from page script is restricted.
- **WebKit**: clipboard access needs a user gesture and works differently.
- Headless browsers may use an isolated clipboard, which is good for parallel tests but means you can't check the system clipboard.

Practical approach: test copy/paste fully in Chromium, and in other browsers check that the copy button shows its success message. For paste, you can type with `insertText` or dispatch a `paste` event with a `DataTransfer`.

## 376: What can't mobile emulation catch?

Emulation sets viewport, user agent, touch and device scale factor, but it still runs a desktop engine on a desktop OS. It can't catch:

- Real iOS Safari bugs (the WebKit build is close but not the same)
- Mobile-specific performance (slow CPU, memory limits)
- Virtual keyboard behavior and how it changes the viewport
- Real touch gestures like pinch zoom or momentum scrolling
- Browser UI like the address bar collapsing, safe areas and notches
- OS integrations: share sheets, file pickers, app links

It's good for responsive layout and touch-specific code paths. For the rest, use real devices or a device cloud for a small set of key flows.

## 377: How do you emulate swipe or other touch gestures?

`tap()` is built in, but gestures like swipe aren't. Dispatch touch events yourself:

```ts
async function swipeLeft(locator: Locator) {
  const box = (await locator.boundingBox())!;
  const startX = box.x + box.width * 0.8;
  const endX = box.x + box.width * 0.2;
  const y = box.y + box.height / 2;

  await locator.dispatchEvent("touchstart", {
    touches: [{ identifier: 0, clientX: startX, clientY: y }],
  });
  await locator.dispatchEvent("touchmove", {
    touches: [{ identifier: 0, clientX: endX, clientY: y }],
  });
  await locator.dispatchEvent("touchend", { touches: [] });
}
```

In Chromium you can also use CDP `Input.dispatchTouchEvent` for more realistic events. If the app uses pointer events instead of touch events, `page.mouse` moves may be enough.

## 378: How does Playwright component testing work under the hood?

When you run component tests:

1. Playwright collects the components your tests `mount`.
2. It builds a small bundle with Vite that includes those components and an index page (`playwright/index.html` and `playwright/index.tsx`).
3. It serves the bundle and opens it in the browser.
4. `mount()` sends the component reference and its props to the page, where it's rendered.

Limits that come from this:

- Props must be serializable, or plain callbacks (which Playwright wires through). You can't pass complex objects like class instances.
- The test file runs in Node.js and the component in the browser, so you can't import and call component internals directly from the test.
- Your app's providers (router, theme, store) must be set up in `playwright/index.tsx` with hooks like `beforeMount`.

## 379: How do you set up Playwright in a monorepo?

Common setups:

- **One Playwright package** (for example `apps/e2e`) that tests several apps, with a project per app and `webServer` entries for each.
- **Playwright per app** with a shared package for fixtures, page objects and helpers, so each app owns its tests.

Things to watch:

- Keep one version of `@playwright/test` across the repo. Two versions mean two browser sets and confusing errors.
- Each `playwright.config.ts` resolves paths relative to itself.
- Shared fixture packages should export `test` and `expect`, and apps should import from there, not from `@playwright/test` directly.
- Use your monorepo tool (Nx, Turborepo) to run only the E2E suites affected by a change.

## 380: How does Playwright handle TypeScript and ESM?

Playwright Test has its own transform (based on Babel) that strips TypeScript types when it loads test files, config and imported helpers. It doesn't type-check.

- It supports both CommonJS and ESM. If `package.json` has `"type": "module"`, files are loaded as ESM.
- `tsconfig.json` `paths` and `baseUrl` are respected.
- Code in `node_modules` is not transformed, so a shared package written in TypeScript must be built first, or be part of the workspace and not inside `node_modules`.
- Decorators and some newer TS features depend on what the transform supports.

Run `tsc --noEmit` in CI to catch type errors, since the test run won't.

## 381: How do you pass data from global setup to tests?

`globalSetup` runs in a different process from the workers, so normal variables don't carry over. Options:

- **Environment variables** set in `globalSetup` are passed to workers:

```ts
export default async function globalSetup() {
  process.env.TENANT_ID = await createTenant();
}
```

- **Files**: write JSON to disk (like `storageState`) and read it in tests or fixtures.
- **Setup projects** instead of `globalSetup`: still separate processes, so use files too, but you get traces and fixtures.

Avoid trying to share live objects like DB connections. Create them in worker fixtures instead.

## 382: How do you capture extra artifacts only when a test fails?

Use an auto fixture that checks the result after `use()`:

```ts
export const test = base.extend<{ failureArtifacts: void }>({
  failureArtifacts: [
    async ({ page }, use, testInfo) => {
      const requests: string[] = [];
      page.on("requestfinished", async (req) => {
        const res = await req.response();
        requests.push(`${req.method()} ${req.url()} ${res?.status()}`);
      });

      await use();

      if (testInfo.status !== testInfo.expectedStatus) {
        await testInfo.attach("network.txt", {
          body: requests.join("\n"),
          contentType: "text/plain",
        });
        await testInfo.attach("local-storage.json", {
          body: JSON.stringify(
            await page.evaluate(() => ({ ...localStorage })),
            null,
            2,
          ),
          contentType: "application/json",
        });
        // fetch backend logs for this test using an id you sent in a header
      }
    },
    { auto: true },
  ],
});
```

Sending a per-test request id header (with `extraHTTPHeaders`) lets you link test failures to backend logs.

## 383: What is expect.configure?

`expect.configure()` creates a new `expect` with different defaults:

```ts
const slowExpect = expect.configure({ timeout: 30_000 });
await slowExpect(page.getByText("Report ready")).toBeVisible();

const softExpect = expect.configure({ soft: true });
await softExpect(page.getByTestId("price")).toHaveText("$10");
```

It's cleaner than passing `{ timeout }` to every call when one area of the app is known to be slow, and it keeps the default `expect` strict for everything else.

## 384: How should a team handle flaky tests?

A good policy usually looks like this:

1. **Detect**: track flaky results over time (the HTML report shows them, and many teams send results to a dashboard).
2. **Triage fast**: each flaky test gets an owner and a ticket.
3. **Quarantine**: if it can't be fixed quickly, tag it (`@quarantine`) and run it in a separate non-blocking job, so it doesn't block merges but still runs.
4. **Fix the cause**: use traces to find the real reason. Don't just raise timeouts.
5. **Deadline**: quarantined tests that aren't fixed within an agreed time get deleted or rewritten.

```bash
npx playwright test --grep-invert @quarantine      # blocking job
npx playwright test --grep @quarantine || true     # non-blocking job
```

`failOnFlakyTests` can be turned on once the suite is stable, to stop new flakiness from sneaking in.

## 385: How do you select which tests to run for a pull request?

Options from simple to complex:

- **Tags**: run `@smoke` on every PR, everything nightly.
- **Changed files**: `--only-changed=origin/main` runs test files that changed or import changed files.
- **Path mapping**: map app folders to test folders or tags in a script (changes in `src/checkout/**` run `@checkout`).
- **Coverage-based selection**: record which app files each test touches and pick tests from the PR diff. Powerful but needs tooling.

Always run the full suite somewhere (main branch, nightly, before release), because no selection method is perfect.

## 386: How do you cache Playwright browsers in CI?

Browsers are downloaded to `~/.cache/ms-playwright` on Linux. Cache that folder keyed on the Playwright version:

```yaml
- name: Get Playwright version
  id: pw
  run: echo "version=$(npx playwright --version | awk '{print $2}')" >> "$GITHUB_OUTPUT"

- uses: actions/cache@v4
  id: pw-cache
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ runner.os }}-${{ steps.pw.outputs.version }}

- run: npx playwright install --with-deps
  if: steps.pw-cache.outputs.cache-hit != 'true'
- run: npx playwright install-deps
  if: steps.pw-cache.outputs.cache-hit == 'true'
```

System dependencies are not in the cache, so you still need `install-deps` on a cache hit. Playwright's docs note that restoring the cache is often about as fast as downloading, so measure before adding this. Using the Playwright Docker image avoids both steps.

## 387: Why must the Docker image version match the Playwright package version?

Each Playwright version expects specific browser builds. The Docker image contains the browsers for its own version. If your `@playwright/test` is newer or older than the image, Playwright looks for browser builds that aren't there and fails with "Executable doesn't exist", or asks you to run `npx playwright install`.

Keep them in sync, for example by reading the version from `package.json` in CI, and update both in the same pull request. Tools like Renovate can group them.

## 388: How do you run tests against a remote browser server?

Start a Playwright server on the remote machine:

```bash
npx playwright run-server --port 3000
```

Then point the tests at it:

```ts
use: {
  connectOptions: {
    wsEndpoint: 'ws://browser-host:3000/',
  },
},
```

The tests run locally, but the browsers run on the remote machine. The client and server Playwright versions must match. One thing to be careful about: `localhost` in the test's URLs now means the remote machine. Use `exposeNetwork` in `connectOptions` to let the remote browser reach your local services, or use a hostname both sides can reach.

## 389: What are the security risks of a Playwright browser server?

A `run-server` endpoint lets anyone who can reach it launch browsers and run code in them. Through the browser they can access your internal network, read local files in some cases, and use your machine's IP.

- Never expose it to the public internet.
- Put it behind a private network, VPN or authenticated proxy.
- Run it in a container with limited network access and resources.
- Use one server per CI job when possible, and shut it down after.

The same applies to Chrome's remote debugging port (`--remote-debugging-port`). Anyone who can connect fully controls the browser, including its cookies.

## 390: What are the pros and cons of running tests on a cloud browser service?

Several services (including Microsoft's own Playwright cloud offering on Azure, and others) run browsers for you. Your tests run in CI but connect to their browsers through `connectOptions`.

Pros:

- Many more parallel browsers than one CI machine can handle.
- No browser maintenance.
- Some offer real devices or extra OS/browser versions.

Cons:

- Network latency on every command, so individual tests can get slower.
- Your test environment must be reachable from the cloud, or you need a tunnel.
- Cost per minute.
- Data, cookies and screenshots leave your network.

They make the most sense for very large suites where shards on your own CI are too slow or too expensive.

## 391: How do you set up sharding with merged reports in GitHub Actions?

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2, 3, 4]
        shardTotal: [4]
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with: { node-version: lts/* }
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: blob-report-${{ matrix.shardIndex }}
          path: blob-report
          retention-days: 1

  merge-reports:
    if: ${{ !cancelled() }}
    needs: [test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-node@v5
        with: { node-version: lts/* }
      - run: npm ci
      - uses: actions/download-artifact@v4
        with:
          path: all-blob-reports
          pattern: blob-report-*
          merge-multiple: true
      - run: npx playwright merge-reports --reporter html ./all-blob-reports
      - uses: actions/upload-artifact@v4
        with:
          name: html-report
          path: playwright-report
```

The config should use `reporter: process.env.CI ? 'blob' : 'html'`. `fail-fast: false` keeps other shards running when one fails, so you get the full picture.

## 392: How do retries work for serial groups compared to normal tests?

- **Normal tests**: only the failed test is retried, in a new worker.
- **Serial mode** (`mode: 'serial'`): if one test fails, the remaining tests in the group are skipped, and on retry the **whole group** runs again from the start, because later tests depend on earlier ones.
- **beforeAll**: runs again in the new worker for the retry.

This makes serial groups expensive when they're flaky: one flaky step reruns all steps. It's another reason to prefer one test with `test.step` or independent tests.

## 393: How do you handle very long end-to-end workflows?

For flows that really need many steps (onboarding, a long wizard, an order through fulfillment):

- Write one test with `test.step` for each phase, so the report shows where it failed.
- Raise the timeout for that test (`test.setTimeout` or `test.slow()`).
- Skip phases you're not testing by setting up state through the API.
- Use `expect.poll` for backend phases (jobs, emails) instead of long sleeps.
- Keep these few. Most coverage should come from shorter, focused tests that start from the right state.

## 394: What is the full timeout hierarchy in Playwright Test?

From biggest to smallest:

1. **globalTimeout**: the whole run.
2. **Test timeout** (`timeout`, default 30 s): the test plus its `beforeEach`/`afterEach` hooks and test-scoped fixtures. `beforeAll`/`afterAll` hooks get their own timeout of the same size.
3. **Fixture timeout**: optional, per fixture.
4. **expect timeout** (default 5 s): each web-first assertion.
5. **actionTimeout** and **navigationTimeout** (no default): each action and each navigation.
6. **Per-call timeout**: `{ timeout }` on a single action or assertion.

A smaller timeout can't extend a bigger one. If an action has `timeout: 60_000` but the test has only 10 s left, the test timeout wins. `timeout: 0` means "no timeout" for most of these.

## 395: How do you handle slow environments without making tests slow everywhere?

- Set timeouts per project. A `staging` project can have a longer test and expect timeout than `local`:

```ts
projects: [
  { name: 'local', use: { baseURL: 'http://localhost:3000' } },
  {
    name: 'staging',
    timeout: 90_000,
    expect: { timeout: 15_000 },
    use: { baseURL: 'https://staging.example.com', actionTimeout: 15_000 },
  },
],
```

- Use `test.slow()` for specific slow tests, with a condition if needed.
- Since web-first assertions return as soon as they pass, bigger timeouts only make _failures_ slower, not passing tests. That makes raising them in slow environments fairly safe.
- If everything needs long timeouts, look at the environment itself. That's a performance problem worth reporting.

## 396: What are workerIndex and parallelIndex, and how are they different?

- `workerIndex`: a unique number for each worker process started during the run. When a worker restarts after a failure, the new one gets a new, higher index.
- `parallelIndex`: a number from `0` to `workers - 1` that says which "slot" the worker is in. A restarted worker gets the same `parallelIndex` as the one it replaced.

They're also available as `TEST_WORKER_INDEX` and `TEST_PARALLEL_INDEX` environment variables.

Use `parallelIndex` to pick a test account from a fixed pool (`user-0` to `user-3` for 4 workers), because it never goes past the number of workers. `workerIndex` can grow, so it's better for unique names.

## 397: How do you debug a test that hangs?

A hanging test usually means something waits forever:

- A `waitForEvent`, `waitForResponse` or `waitForRequest` started after the event already happened.
- A promise that never settles in your helper code.
- A `toPass` without a timeout.
- A fixture teardown waiting on something, like a server that won't close.
- An unhandled `beforeunload` dialog when closing.

Steps:

1. Look at where the test timeout error says it was stuck. Playwright shows the pending call.
2. Run with `DEBUG=pw:api` to see the last API call.
3. Open the trace and see the last action.
4. Give the waits explicit timeouts so they fail with a clear message instead of using up the test timeout.

## 398: What problems can event listeners cause in tests?

- **Errors in listeners are easy to miss**: an exception in a `page.on('response', ...)` callback doesn't fail the test, and an async handler that rejects can show up as an unrelated error later.
- **Leaking listeners**: adding the same listener in a helper called many times means it runs many times.
- **Work after the test ends**: an async handler still running when the page closes throws "Target closed" errors.
- **Order**: a `page.once('dialog')` added after the action that triggers the dialog is too late.

Keep handlers simple (collect data into an array), check the collected data at the end with an assertion, remove handlers with `page.off()` when done, and use `page.unrouteAll({ behavior: 'ignoreErrors' })` for route handlers.

## 399: How do you fail tests on unexpected server errors?

Watch responses in an auto fixture and fail if any API call returned a 5xx:

```ts
export const test = base.extend<{ noServerErrors: void }>({
  noServerErrors: [
    async ({ page }, use, testInfo) => {
      const failures: string[] = [];
      page.on("response", (res) => {
        if (res.status() >= 500 && res.url().includes("/api/")) {
          failures.push(
            `${res.status()} ${res.request().method()} ${res.url()}`,
          );
        }
      });

      await use();

      if (!testInfo.annotations.some((a) => a.type === "allow-5xx")) {
        expect(failures, "unexpected server errors").toEqual([]);
      }
    },
    { auto: true },
  ],
});
```

This catches backend errors that the UI hides (for example, a failed request that the page silently retries). The annotation lets tests that check error handling opt out.

## 400: How do you control feature flags in tests?

Options, depending on how flags are loaded:

- **Mock the flag API**:

```ts
await page.route("**/api/flags", (route) =>
  route.fulfill({ json: { newCheckout: true } }),
);
```

- **Set local storage or a cookie** the app reads, with `addInitScript` or `addCookies`.
- **Use the flag service's test API** to target a test user.
- **Pass a header or query param** that the backend respects in test environments.

Wrap it in an option fixture so tests can say `test.use({ flags: { newCheckout: true } })`. Run important tests with both flag values while a flag is being rolled out, and delete the old version when the flag is removed.

## 401: How do you test right-to-left (RTL) layouts?

Run a project with an RTL locale and check direction and layout:

```ts
test.describe("arabic", () => {
  test.use({ locale: "ar-EG" });

  test("layout is mirrored", async ({ page }) => {
    await page.goto("/?lang=ar");
    await expect(page.locator("html")).toHaveAttribute("dir", "rtl");

    const nav = await page.getByRole("navigation").boundingBox();
    const main = await page.getByRole("main").boundingBox();
    expect(nav!.x).toBeGreaterThan(main!.x); // sidebar on the right
    await expect(page).toHaveScreenshot("home-rtl.png");
  });
});
```

Visual tests are the most useful here, since RTL bugs are mostly about layout: icons not flipped, wrong padding, text overflow. Long translations (German, Finnish) are worth a visual check too.

## 402: How do you test flows that send emails?

Don't use a real inbox. Use a fake SMTP server with an HTTP API, such as Mailpit, in the test environment, and read the email from the test:

```ts
test("password reset email", async ({ page, request }) => {
  const email = `reset-${Date.now()}@test.local`;
  await createUser(request, email);

  await page.goto("/forgot-password");
  await page.getByLabel("Email").fill(email);
  await page.getByRole("button", { name: "Send reset link" }).click();

  const link = await expect
    .poll(
      async () => {
        const res = await request.get(
          `http://localhost:8025/api/v1/search?query=to:${email}`,
        );
        const { messages } = await res.json();
        return messages[0]?.ID;
      },
      { timeout: 15_000 },
    )
    .not.toBeUndefined()
    .then(async () => {
      const res = await request.get(
        `http://localhost:8025/api/v1/search?query=to:${email}`,
      );
      const { messages } = await res.json();
      const msg = await (
        await request.get(
          `http://localhost:8025/api/v1/message/${messages[0].ID}`,
        )
      ).json();
      return msg.Text.match(/https?:\/\/\S+reset\S+/)![0];
    });

  await page.goto(link);
  await expect(
    page.getByRole("heading", { name: "Choose a new password" }),
  ).toBeVisible();
});
```

Wrap the mailbox calls in a small helper or fixture so tests just call `mailbox.waitForLink(email)`. For staging environments that send real emails, services with test inboxes and APIs work the same way.

## 403: How do you check the content of a generated PDF?

Download the PDF and parse it with a library like `pdf-parse`:

```ts
import pdf from "pdf-parse";
import fs from "node:fs/promises";

test("invoice PDF has the total", async ({ page }, testInfo) => {
  const downloadPromise = page.waitForEvent("download");
  await page.getByRole("button", { name: "Download invoice" }).click();
  const file = testInfo.outputPath("invoice.pdf");
  await (await downloadPromise).saveAs(file);

  const { text, numpages } = await pdf(await fs.readFile(file));
  expect(numpages).toBe(1);
  expect(text).toContain("Total: $120.00");
});
```

If the PDF opens in a browser tab instead of downloading, fetch its URL with `page.request` and parse the response body. For layout checks, convert pages to images and use visual comparison.

## 404: How do you write a reliable standalone Playwright script?

Make sure the browser closes even when something fails, and add timeouts:

```ts
import { chromium } from "playwright";

async function main() {
  const browser = await chromium.launch();
  try {
    const context = await browser.newContext({ locale: "en-US" });
    context.setDefaultTimeout(15_000);
    const page = await context.newPage();

    await page.goto("https://example.com/report", {
      waitUntil: "domcontentloaded",
    });
    await page.getByRole("button", { name: "Generate" }).click();
    await page.getByText("Ready").waitFor();
    await page.pdf({ path: "report.pdf" });
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```

Recent versions also support `await using` with Playwright objects, which closes them automatically at the end of the block. For long-running services, reuse one browser and create a new context per job, since launching a browser per job is slow.

## 405: What is Playwright MCP?

Playwright MCP is a Model Context Protocol server that lets AI agents (like Claude Code, Copilot or Cursor) control a browser through Playwright. Instead of screenshots, it gives the model the page's accessibility snapshot, a structured text view of roles, names and states, plus references to elements so the model can click and type.

It's used for:

- letting an AI agent explore an app and write tests
- debugging a page with an AI assistant
- general browser automation by agents

It runs as `npx @playwright/mcp@latest` and is configured in the AI tool's MCP settings. The accessibility-snapshot approach is fast and cheap compared to screenshot-based agents, but it depends on the page having a good accessibility tree.

## 406: What are Playwright Test Agents?

Added in 1.56, Test Agents are AI agent definitions that Playwright generates for your AI tool with `npx playwright init-agents --loop=<tool>` (for example `claude` or `vscode`). There are three:

- **Planner**: explores the app and writes a test plan in Markdown.
- **Generator**: turns the plan into Playwright tests, checking locators against the live app.
- **Healer**: runs failing tests, looks at the failure and tries to fix the test.

They work on top of your existing config and seed tests. Like any generated code, the tests need review: the agent can "fix" a test by making it assert the wrong thing, or hide a real bug as a test problem.

## 407: How do you test an app built from micro frontends?

- **Test each micro frontend** on its own in its repo, with the shell and other remotes mocked or stubbed.
- **Test the integration** with a smaller set of E2E tests against the composed app, focusing on the seams: navigation between remotes, shared auth, shared state and events, and version mismatches.
- **Use route mocking** to replace a remote's `remoteEntry.js` with a local or specific build, to test combinations:

```ts
await page.route("**/checkout/remoteEntry.js", (route) =>
  route.fulfill({ path: "builds/checkout-v2/remoteEntry.js" }),
);
```

- **Check failure handling**: abort the request for one remote and make sure the shell shows a fallback instead of a blank page.

## 408: What is different about testing server-rendered apps?

- **Hydration**: the page is visible before it's interactive (see the hydration question). Wait for a sign of hydration before interacting.
- **Server data**: data is loaded on the server, so `page.route()` can't mock it. The request never comes from the browser. You need to mock at the backend (a mock API server, MSW on the server, test data in the DB).
- **Hydration mismatch errors**: listen for console errors about mismatches, they're real bugs.
- **Caching**: SSR and ISR caches can serve stale pages between tests. Disable caching in the test environment or use unique data.
- **JavaScript off**: you can test that critical content renders without JS with `test.use({ javaScriptEnabled: false })`.

## 409: How do you wait correctly for client-side route changes in a SPA?

In a SPA, clicking a link changes the URL with `history.pushState` and then loads data. The URL changes before the new page is ready.

```ts
await page.getByRole("link", { name: "Orders" }).click();
await expect(page).toHaveURL("/orders"); // URL changed
await expect(page.getByRole("heading", { name: "Orders" })).toBeVisible(); // page rendered
await expect(page.getByRole("row")).not.toHaveCount(0); // data loaded
```

A common mistake is to check only the URL and then read data that hasn't loaded. Another is to use `page.waitForNavigation()` (deprecated) or `waitForLoadState`, which don't apply to client-side navigation, since no new document loads. Wait for the content you need.

## 410: What other media features can you emulate for accessibility testing?

```ts
await page.emulateMedia({
  reducedMotion: "reduce",
  forcedColors: "active", // Windows high contrast mode
  colorScheme: "dark",
  contrast: "more", // prefers-contrast
});
```

You can also set them in `use` (`reducedMotion`, `forcedColors`, `colorScheme`, `contrast`) for a whole project. These let you check that the app respects user settings: animations stop, focus outlines are still visible in forced colors, and nothing important relies on color alone. Combine with screenshots to review how the page looks in each mode.

## 411: How do you test retry and backoff logic in the app?

Combine route mocking (to fail the first calls) with the Clock API (to skip the wait):

```ts
test("retries after a failure", async ({ page }) => {
  await page.clock.install();
  let calls = 0;
  await page.route("**/api/data", (route) => {
    calls++;
    return calls < 3
      ? route.fulfill({ status: 503 })
      : route.fulfill({ json: { items: [1, 2] } });
  });

  await page.goto("/data");
  await expect(page.getByText("Retrying...")).toBeVisible();

  await page.clock.runFor(10_000); // let the backoff timers fire
  await expect(page.getByRole("listitem")).toHaveCount(2);
  expect(calls).toBe(3);
});
```

This tests the full behavior (message, retries, final success) in milliseconds instead of waiting for real backoff delays.

## 412: When should E2E tests mock the backend and when should they use the real one?

**Real backend**:

- Proves the whole system works together.
- Catches API contract changes and integration bugs.
- Slower, needs test data management, and more prone to flakiness.

**Mocked backend**:

- Fast, deterministic, and makes edge cases easy (errors, empty states, huge lists).
- Can drift from the real API and give false confidence.

A common split: a smaller set of critical user journeys against a real backend, and a larger set of UI-behavior tests with mocks. Keep mocks honest by generating them from real responses (HAR, recorded fixtures) or sharing schemas with the backend.

## 413: Where do Playwright tests fit in the test pyramid?

E2E tests are the top of the pyramid: the most realistic, but the slowest and most expensive to maintain. A healthy setup:

- **Unit tests**: lots, for logic.
- **Component and integration tests**: for UI pieces and service boundaries.
- **API tests**: Playwright's `request` is good for these too, fast and no browser.
- **E2E tests**: fewer, for critical user journeys across the stack.

A common anti-pattern is the "ice cream cone": mostly E2E tests, few unit tests. Every form validation case is tested through the browser, the suite takes an hour, and failures are hard to diagnose. If a check doesn't need a real browser and the full stack, push it down a level.

## 414: When is Playwright not the right tool?

- **Native mobile apps**: use Appium, Detox, Maestro or XCUITest/Espresso.
- **Unit testing pure logic**: Vitest or Jest are much faster.
- **Load testing**: browsers are too heavy. Use k6, Gatling or Artillery (k6 has a browser module for a few real-browser checks).
- **Real Safari or real devices**: Playwright's WebKit is not the same as Safari on iOS.
- **Desktop apps** other than Electron.
- **Scraping sites that forbid it**: technical ability doesn't mean permission. Check terms of use and robots rules.

## 415: How do you keep a big suite maintainable when the UI changes often?

- Use user-facing locators. They break when what the user sees changes, which is often when the test should be looked at anyway.
- Keep locators in page or component objects, not spread across tests.
- Add test ids for elements without good names, and agree on a naming convention with developers.
- Make developers part of test ownership: tests live in the same repo and run on their PRs.
- Delete tests that cover low-value paths and fail often. A smaller, trusted suite is better than a big ignored one.
- Use codegen and "Pick locator" to quickly fix broken locators, and ARIA snapshots to cover structure with less code.

## 416: What do you look for when reviewing a Playwright test?

- Every Playwright call is awaited.
- No `waitForTimeout`, no `networkidle`, no `force: true` without a comment.
- Locators are user-facing and specific, without `nth()` unless order matters.
- Assertions are web-first (`await expect(locator)...`), not `expect(await locator.textContent())`.
- The test checks a real result, not just that clicks didn't throw.
- The test creates its own data and cleans up, and doesn't depend on other tests.
- Setup uses API or storage state, not long UI flows.
- No secrets or hardcoded environment URLs.
- The title says what behavior is tested.
- No leftover `test.only`, `page.pause()` or `console.log`.

## 417: Tests pass locally but fail in CI. How do you approach it?

1. **Look at the trace** from CI first. It usually shows the problem directly: a different page, an error message, a missing element.
2. **Check environment differences**: `baseURL`, env variables and secrets, time zone and locale, viewport, test data, feature flags, which backend the CI uses.
3. **Check resources**: CI is often slower. Try locally with the same number of workers and CPU throttling, or in the same Docker image.
4. **Check order and parallelism**: CI may run with `fullyParallel` and different shards, exposing test dependencies.
5. **Check the build**: CI may test a production build, where timing and behavior differ from the dev server.
6. **Check fonts and OS** for visual tests.

Fix the cause rather than adding retries or longer timeouts only on CI.

## 418: The E2E suite takes an hour. What would you do?

1. **Measure**: find the slowest tests and fixtures in the report. Often 10% of the tests take half the time.
2. **Quick wins**: remove sleeps and `networkidle`, reuse login with `storageState`, create data through the API, block third-party scripts.
3. **Parallelize**: turn on `fullyParallel`, fix tests that can't run in parallel, tune workers, add shards with merged reports.
4. **Reduce artifact overhead**: traces and videos only on retry.
5. **Run less per PR**: smoke tests and `--only-changed` on PRs, full suite on main and nightly, all browsers only nightly.
6. **Move tests down**: checks that don't need a browser become API, component or unit tests.
7. **Delete duplicates**: many suites test the same thing several times.

Set a time budget afterwards (for example, PR runs under 10 minutes) and watch it, or it will slowly grow back.

## 419: Tests start failing because the login endpoint is rate limited. What do you do?

The usual cause is every test logging in through the UI or API. Fixes:

- Log in once per role (or once per worker) in a setup project and reuse `storageState`.
- Reuse the saved state across local runs while the session is still valid.
- Spread logins across several test accounts.
- Ask for the rate limit to be raised or turned off for test accounts or test IPs in non-production environments.
- Keep only a few tests that really test the login flow itself.

If the rate limiting is a feature you need to test, write a specific test for it with its own account.

## 420: A visual test is flaky with small pixel differences. How do you fix it?

1. Open the diff image in the report and see what changes: text, an image, a shadow, a cursor, a whole-page shift.
2. Fix the cause:
   - **Dynamic data or time**: mock data, use the Clock API.
   - **Fonts**: wait for `document.fonts.ready`, use the same Docker image everywhere.
   - **Animations or carets**: `animations: 'disabled'`, `caret: 'hide'` (defaults in `toHaveScreenshot`).
   - **Lazy images**: scroll or wait for them to load.
   - **Third-party content**: mask it or block it.
   - **Anti-aliasing noise**: a small `maxDiffPixelRatio`.
3. Screenshot a smaller element instead of the full page, so unrelated changes don't affect it.

Raising the threshold until it passes is the last option, because it also hides real regressions.

## 421: All E2E tests pass, but a bug still reached production. What would you look at?

- **Was the scenario tested at all?** Many bugs are in paths no test covers: edge-case data, roles, browsers, mobile.
- **Did the test check the right thing?** A test can click through a flow and never assert the result.
- **Was it mocked?** A mocked API can return data the real one doesn't.
- **Was it hidden by retries?** A flaky test that failed on the first try may have been pointing at the real bug.
- **Environment differences**: config, data volume, third-party services, feature flags in production.
- **Was the test skipped or quarantined?**

Then add a test that reproduces the bug (it should fail before the fix), and think about whether the bug belongs in a lower-level test or in production monitoring.

## 422: How do you test a payment form inside a third-party iframe like Stripe?

- Use the provider's **test mode** and test card numbers in a test environment.
- Enter card details through the iframe with a frame locator:

```ts
const card = page.frameLocator(
  'iframe[title="Secure card payment input frame"]',
);
await card.getByPlaceholder("Card number").fill("4242 4242 4242 4242");
await card.getByPlaceholder("MM / YY").fill("12 / 30");
await card.getByPlaceholder("CVC").fill("123");
await page.getByRole("button", { name: "Pay" }).click();
await expect(page.getByText("Payment successful")).toBeVisible();
```

- For 3-D Secure, use the provider's test cards that trigger the challenge and complete it in the nested iframe.
- Keep these tests few: third-party iframes change their markup and are slower. For most checkout tests, mock your own backend's payment endpoint instead.

## 423: A test fails on certain days of the month. How do you fix it?

This usually means the test or the app depends on the current date: "next month" from the 31st, end of year, a leap day, a DST change, a weekend, or a time zone difference near midnight.

Fixes:

- Fix the time with `page.clock.setFixedTime()` or `install({ time })` so the test always runs on a known date.
- Make test data relative to that fixed date, not to `new Date()` in the test.
- Make sure the backend's "now" is consistent too, or seed data with fixed dates.
- Add specific tests for the edge dates (month end, Feb 29, DST change) instead of hitting them by accident.

## 424: How would you migrate a large Selenium suite to Playwright?

1. **Start with a pilot**: pick a few important flows, rewrite them in Playwright, and run both suites in CI. Compare stability and speed.
2. **Set up the foundation**: config, projects, auth setup, fixtures, page objects and CI with reports, before mass migration.
3. **Don't translate line by line**: Selenium code is full of explicit waits and `findElement` with XPath. Rewrite with locators, web-first assertions and API setup.
4. **Migrate by area**: move one feature at a time and delete the Selenium tests for it once the new ones are stable.
5. **Train the team**: async/await habits, locators, traces.
6. **Keep the cases that need Selenium**: real Safari or device clouds over WebDriver, if they matter to you.

Most teams see big drops in flakiness and run time, mostly from auto-waiting, browser contexts and parallel runs.

## 425: Tests randomly fail with "Target page, context or browser has been closed". What causes it?

Common causes:

- **Missing await**: an action runs after the test finished and the page was closed.
- **Event handlers still running** after the test ends (async `page.on` or `page.route` handlers).
- **The page crashed**: Chromium out of memory, often due to small `/dev/shm` in Docker. Listen for `page.on('crash')`.
- **The test closed the page or context itself**, then used it again.
- **The test timed out**, and the error from the pending action is reported after the browser was torn down.

Check for floating promises with ESLint, look at the trace for the last action, and for crashes run Docker with `--ipc=host` and fewer workers.

## 426: How do you check that analytics events are sent correctly?

Intercept the analytics requests and check their payloads, without letting them reach the real service:

```ts
test("purchase event is tracked", async ({ page }) => {
  const events: any[] = [];
  await page.route("**/collect**", async (route) => {
    const body = route.request().postData();
    if (body)
      events.push(
        ...body
          .split("\n")
          .filter(Boolean)
          .map((line) => Object.fromEntries(new URLSearchParams(line))),
      );
    await route.fulfill({ status: 204 });
  });

  await page.goto("/checkout");
  await page.getByRole("button", { name: "Pay" }).click();
  await expect(page.getByText("Thank you")).toBeVisible();

  await expect.poll(() => events.find((e) => e.en === "purchase")).toBeTruthy();
});
```

The exact format depends on the analytics tool. If the app pushes to a `dataLayer`, it's often easier to read `window.dataLayer` with `evaluate`.

## 427: You're setting up E2E testing for a new project. What's your plan?

1. **Decide scope**: list the critical user journeys (sign up, log in, main workflow, payment). These are the first tests.
2. **Set up the foundation**: `npm init playwright`, TypeScript, ESLint with the Playwright plugin and `no-floating-promises`, a fixtures file, an auth setup project.
3. **Test environment**: how the app and its data run in CI (Docker Compose, seeded DB, `webServer`), and how data is created (API helpers).
4. **CI**: run on every PR, Chromium first, reports and traces as artifacts, retries with `trace: 'on-first-retry'`.
5. **Conventions**: locator priority, test id naming, folder layout, tags.
6. **Grow carefully**: add browsers, visual tests and sharding when needed.
7. **Keep it healthy**: watch run time and flaky rate from the start.

Agree with developers that E2E tests are part of the definition of done for features, not something QA catches up on later.

## 428: How do you test a direct upload to cloud storage with a presigned URL?

The browser uploads straight to S3 (or similar), not to your backend. Options:

- **Real upload** to a test bucket, then check through your API that the file is there. Needs a test bucket with CORS set up for your test origin.
- **Local S3-compatible storage** like MinIO or LocalStack in CI.
- **Mock the upload request** with `page.route()` to test the UI states (progress, success, failure) without real storage:

```ts
await page.route(/s3\.amazonaws\.com/, (route) => {
  if (route.request().method() === "PUT") return route.fulfill({ status: 200 });
  return route.continue();
});
```

Use mocks for most UI tests, and keep one test against real (or MinIO) storage to catch CORS and signing problems.

## 429: How do you test an app that runs A/B experiments?

Random variants make tests flaky. Make the variant fixed:

- Force it with a cookie, query param or local storage key that the experiment tool supports.
- Mock the experiment service response with `page.route()`.
- Use a test user that's excluded from experiments, so tests always see the control.

```ts
await context.addCookies([
  { name: "exp_checkout", value: "B", url: "http://localhost:3000" },
]);
```

Run important tests against each active variant, especially before a variant is rolled out to everyone.

## 430: How do you test content that depends on the user's country or IP?

Playwright can't change the client IP by itself. Options:

- Let the backend read a test header (like `x-test-country`) in non-production environments, and set it with `extraHTTPHeaders`.
- Mock the geo-IP lookup the app does with `page.route()` if it's done in the browser.
- Use a proxy in the target country with the `proxy` option, for a small number of real checks.
- Set `locale`, `timezoneId` and `geolocation` too, since apps often mix these signals.

## 431: How do you test a multi-step wizard that saves progress?

Test the steps, and test resuming:

```ts
test("wizard resumes after reload", async ({ page }) => {
  await page.goto("/onboarding");
  await page.getByLabel("Company name").fill("Acme");
  await page.getByRole("button", { name: "Next" }).click();
  await expect(
    page.getByRole("heading", { name: "Step 2 of 4" }),
  ).toBeVisible();

  await page.reload();
  await expect(
    page.getByRole("heading", { name: "Step 2 of 4" }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Back" }).click();
  await expect(page.getByLabel("Company name")).toHaveValue("Acme");
});
```

Also test deep links to later steps (should redirect if earlier steps are missing), validation per step, and resuming in a new context if progress is saved on the server. For tests that focus on step 4, start there with data set up through the API instead of clicking through steps 1-3.

## 432: How do you test a permissions matrix for many roles efficiently?

Testing every page for every role through the UI is slow. Split it:

- **API level**: loop over roles and endpoints with the `request` fixture and check status codes. This is fast and covers the real security boundary.

```ts
const matrix = [
  { role: "admin", endpoint: "/api/users", status: 200 },
  { role: "viewer", endpoint: "/api/users", status: 403 },
];

for (const { role, endpoint, status } of matrix) {
  test(`${role} -> ${endpoint} = ${status}`, async ({ playwright }) => {
    const api = await playwright.request.newContext({
      storageState: `playwright/.auth/${role}.json`,
    });
    const res = await api.get(endpoint);
    expect(res.status()).toBe(status);
    await api.dispose();
  });
}
```

- **UI level**: a few tests per role checking that menus and buttons match what the role can do.

The API tests protect the data. The UI tests make sure users aren't shown actions they can't take.

## 433: Memory usage grows during a long test run. What could cause it?

- **Contexts or pages not closed**: contexts created with `browser.newContext()` in tests or worker fixtures must be closed manually.
- **Data collected in module-level arrays** (logs, requests) that grows across tests in a worker.
- **Big traces or videos** kept in memory before writing.
- **Worker fixtures** holding large data.
- **The app itself leaking** in a long serial test that never reloads.

Check that every `newContext()`/`newPage()` you create is closed, keep collected data inside test-scoped fixtures, and watch memory per worker. If it's the app leaking, that's a bug worth reporting.

## 434: Tests interfere with each other through a backend cache. How do you deal with it?

Example: test A changes a product price, and test B, running in parallel, sees the old price for a minute because of a cache.

Options:

- Give each test its own data (its own product), so caches never mix.
- Turn off or shorten caching in the test environment, or add a test-only cache flush endpoint.
- Assert with retry (`expect.poll` or web-first assertions with a longer timeout) where eventual consistency is expected behavior.
- Send a header that makes the backend skip the cache for test traffic, if the team agrees to it.

Data isolation is usually the best fix, since it also solves other parallel-run problems.

## 435: How do you test Server-Sent Events?

SSE is a normal HTTP response that stays open, so you can mock it with `route.fulfill` and a `text/event-stream` body:

```ts
await page.route("**/api/stream", (route) =>
  route.fulfill({
    status: 200,
    headers: {
      "content-type": "text/event-stream",
      "cache-control": "no-cache",
    },
    body: 'data: {"progress": 50}\n\ndata: {"progress": 100}\n\n',
  }),
);

await page.goto("/job/1");
await expect(page.getByRole("progressbar")).toHaveAttribute(
  "aria-valuenow",
  "100",
);
```

`route.fulfill` sends the whole body at once and closes the stream, so it can't simulate events arriving over time. For that, run a small test SSE server, or let the real backend send events and use web-first assertions to wait for each state.

## 436: How do you test browser notifications?

Grant the permission and replace `Notification` to record calls:

```ts
test.use({ permissions: ["notifications"] });

test("shows notification on new message", async ({ page }) => {
  await page.addInitScript(() => {
    (window as any).__notifications = [];
    class FakeNotification {
      static permission = "granted";
      static requestPermission = async () => "granted";
      constructor(title: string, options?: NotificationOptions) {
        (window as any).__notifications.push({ title, body: options?.body });
      }
      close() {}
    }
    (window as any).Notification = FakeNotification;
  });

  await page.goto("/inbox");
  // trigger a new message...
  await expect
    .poll(() => page.evaluate(() => (window as any).__notifications))
    .toContainEqual(expect.objectContaining({ title: "New message" }));
});
```

Real OS notifications are outside the page and can't be checked with Playwright. Testing push messages from a service worker needs more setup.

## 437: How do you share tests between mobile and desktop when the flows are different?

Keep the test the same and hide the difference in page objects:

```ts
class Navigation {
  constructor(
    private page: Page,
    private isMobile: boolean,
  ) {}

  async goTo(name: string) {
    if (this.isMobile) {
      await this.page.getByRole("button", { name: "Menu" }).click();
    }
    await this.page.getByRole("navigation").getByRole("link", { name }).click();
  }
}

export const test = base.extend<{ nav: Navigation }>({
  nav: async ({ page, isMobile }, use) => use(new Navigation(page, isMobile)),
});
```

The `isMobile` fixture comes from the project's device settings. Tests that are truly different on mobile (swipe gestures, bottom sheets) should be separate tests tagged for the mobile project.

## 438: How can Playwright be used for monitoring production?

You can run a few read-only Playwright tests on a schedule against production (synthetic monitoring):

- Pick critical journeys that don't change data, or use dedicated monitoring accounts with cleanup.
- Run them every few minutes from CI or a scheduled job.
- Use short timeouts, no retries (or one), and send failures to alerting.
- Attach traces and screenshots to alerts so on-call can see what happened.
- Tag these tests (`@monitor`) so they're separate from the E2E suite.

Be careful with analytics and business metrics: exclude monitoring traffic so it doesn't count as real users.

## 439: Which metrics would you track to keep a Playwright suite healthy?

- **Total run time** per pipeline, and the slowest tests.
- **Flaky rate**: share of tests that passed only on retry, and which tests are flaky most often.
- **Failure rate on main**: failures not caused by real bugs mean the suite isn't trusted.
- **Time to fix** broken or quarantined tests.
- **Number of quarantined or skipped tests**, and how long they've been skipped.
- **Escaped bugs**: production bugs in areas that have tests.

You can get most of these from JSON or blob reports, or a custom reporter that pushes results to a dashboard.

## 440: How do you handle beforeunload dialogs?

A page with a `beforeunload` handler (like "You have unsaved changes") shows a dialog when you leave. In Playwright:

- `page.close()` doesn't run `beforeunload` handlers by default.
- `page.close({ runBeforeUnload: true })` runs them and you get a `dialog` event of type `beforeunload`.
- Navigation with `goto` or a click also triggers it, and the dialog is auto-dismissed unless you handle it.

```ts
test("warns about unsaved changes", async ({ page }) => {
  await page.goto("/editor");
  await page.getByRole("textbox").fill("draft");

  const dialogPromise = page.waitForEvent("dialog");
  page.close({ runBeforeUnload: true });
  const dialog = await dialogPromise;

  expect(dialog.type()).toBe("beforeunload");
  await dialog.dismiss(); // stay on the page
});
```

## 441: Why not share one page across all tests to save time?

It's tempting because it skips context creation and navigation, but:

- Tests depend on order and leftover state.
- One failure leaves the page in a bad state, and many later tests fail too.
- Retries and parallel runs don't work well.
- Debugging needs the whole chain of previous tests.

Creating a context costs milliseconds. The real time goes into logins, navigations and data setup, and those can be made fast with `storageState` and API calls while keeping isolation. Shared pages only make sense in rare serial flows.

## 442: How do you test offline support in a PWA?

Let the service worker install, then go offline and reload:

```ts
test("works offline after first visit", async ({ page, context }) => {
  await page.goto("/");
  await page.evaluate(() => navigator.serviceWorker.ready);

  await context.setOffline(true);
  await page.reload();

  await expect(page.getByRole("heading", { name: "Notes" })).toBeVisible();
  await expect(page.getByText("You are offline")).toBeVisible();
});
```

Keep `serviceWorkers: 'allow'` for these tests. You can inspect service workers with `context.serviceWorkers()` and wait for one with `context.waitForEvent('serviceworker')`. Test this in a production build, since many frameworks disable the service worker in dev.

## 443: How do you test camera or microphone features?

In Chromium, use fake media devices:

```ts
test.use({
  permissions: ["camera", "microphone"],
  launchOptions: {
    args: [
      "--use-fake-ui-for-media-stream",
      "--use-fake-device-for-media-stream",
      // '--use-file-for-fake-video-capture=fixtures/face.y4m',
    ],
  },
});

test("video preview starts", async ({ page }) => {
  await page.goto("/call");
  await page.getByRole("button", { name: "Start camera" }).click();
  await expect
    .poll(() =>
      page.locator("video").evaluate((v: HTMLVideoElement) => v.readyState),
    )
    .toBeGreaterThanOrEqual(2);
});
```

The fake device sends a test pattern, or a file you provide. For WebRTC calls, open two contexts and check that each side receives a stream. Firefox has its own prefs for fake media, set with `firefoxUserPrefs`.

## 444: How do you test what happens when the user denies a permission?

Don't grant it. In a new context, permissions start as "prompt", and Playwright's headless browsers usually deny the prompt. To be explicit:

```ts
test("shows manual address form when location is denied", async ({
  page,
  context,
}) => {
  await context.clearPermissions();
  await page.addInitScript(() => {
    navigator.geolocation.getCurrentPosition = (_ok, fail) =>
      fail?.({
        code: 1,
        message: "User denied Geolocation",
      } as GeolocationPositionError);
  });

  await page.goto("/stores");
  await page.getByRole("button", { name: "Use my location" }).click();
  await expect(page.getByLabel("Postcode")).toBeVisible();
});
```

Overriding the API with `addInitScript` makes the denied case deterministic across browsers.

## 445: How do you upgrade Playwright safely in a large repo?

1. Read the release notes for every version you skip, especially "Breaking changes" (for example removed selectors, changed defaults, glob changes).
2. Upgrade `@playwright/test`, the browsers and the Docker image together in one PR.
3. Run the full suite in all projects. Expect some visual snapshot updates, since the browsers changed. Review them, don't blindly accept.
4. Fix deprecation warnings while you're there.
5. Upgrade regularly (every release or two). Small jumps are much easier than skipping a year of versions.

Tools like Renovate or Dependabot can open the PR automatically, grouping the npm package and the Docker image.

## 446: Can storageState save IndexedDB data?

Yes, since 1.51 you can include IndexedDB:

```ts
await page.context().storageState({ path: "auth.json", indexedDB: true });
```

This matters for apps that keep auth tokens in IndexedDB, like some Firebase setups. Without it, the saved state has cookies and local storage but the app still looks logged out. Session storage isn't included and needs to be set with `addInitScript` if you need it.

## 447: How do you check that the app doesn't send duplicate requests?

Count requests during the action:

```ts
test("search sends one request per query", async ({ page }) => {
  const searchCalls: string[] = [];
  page.on("request", (req) => {
    if (req.url().includes("/api/search")) searchCalls.push(req.url());
  });

  await page.goto("/");
  await page.getByRole("searchbox").pressSequentially("laptop", { delay: 50 });
  await expect(page.getByRole("listitem").first()).toBeVisible();

  expect(searchCalls).toHaveLength(1); // debounced
});
```

This catches bugs like a missing debounce, a `useEffect` that runs twice, or a button that submits twice on double click. Run the action at a realistic speed, since debounce behavior depends on timing.

## 448: How do you test a login that moves across domains, like app.example.com to auth.example.com?

Playwright handles cross-domain navigation in one page and one context, so the flow just works:

```ts
await page.goto("https://app.example.com");
await page.getByRole("link", { name: "Sign in" }).click();
await page.waitForURL("https://auth.example.com/**");
await page.getByLabel("Email").fill(user.email);
await page.getByLabel("Password").fill(user.password);
await page.getByRole("button", { name: "Continue" }).click();
await page.waitForURL("https://app.example.com/**");
```

Things to watch:

- `storageState` saves cookies for all domains, so the saved state works for both.
- `baseURL` only applies to relative URLs. Use full URLs for the auth domain.
- Cookie settings like `SameSite` and third-party cookie blocking can behave differently per browser, which is worth testing in WebKit and Firefox too.

## 449: A test is passing but slow. What do you check?

Open its trace or the report and look at the step timings:

- **Long `goto` calls**: heavy pages or `waitUntil: 'load'` waiting for images and third-party scripts. Block third parties, try `domcontentloaded`.
- **Long setup**: logging in or creating data through the UI. Move to API or `storageState`.
- **Assertions that wait for the full timeout before passing**: usually `not.toBeVisible()` on something that disappears slowly, or a wrong assertion that only passes when a later re-render happens.
- **Fixed waits** hidden in helpers.
- **Slow fixtures**: shown as separate steps in the trace.
- **Slow app**: the trace's network tab shows slow API calls. That's a real performance issue to report.

## 450: What are the most common mistakes in Playwright test suites?

- Missing `await`, especially on `expect`.
- Using `waitForTimeout` or `networkidle` instead of waiting for real conditions.
- Reading values and asserting with generic matchers (`expect(await el.textContent())`) instead of web-first assertions.
- CSS and XPath locators tied to markup, or `nth()` everywhere.
- Logging in through the UI in every test.
- Tests that depend on each other or share data.
- Retries used to hide flakiness, and nobody looks at flaky tests.
- Too many E2E tests for things that belong in unit or API tests.
- `force: true` to "fix" clicks that a real user couldn't do.
- Visual tests run on different machines than where snapshots were made.
- Secrets committed in config, storage state files or reports.
- Not upgrading Playwright for a long time, then facing many breaking changes at once.
