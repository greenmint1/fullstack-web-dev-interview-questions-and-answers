# Storybook Interview Questions and Answers

_Last updated: October 28, 2026_

90 Storybook interview questions with answers, split into three levels: 30 easy, 30 moderate and 30 advanced.

The answers target Storybook 10 (ESM-only, `storybook/test`, the Vitest addon, `sb.mock` module mocking and CSF Factories in preview). Code examples use React with Vite unless the question says otherwise, but most of the ideas work the same way in Vue, Angular and Svelte.

## Table of Contents

- [Easy Questions (1-30)](#easy-questions-1-30)
- [Moderate Questions (31-60)](#moderate-questions-31-60)
- [Advanced Questions (61-90)](#advanced-questions-61-90)

### Easy Questions (1-30)

- [1: What is Storybook?](#1-what-is-storybook)
- [2: Why would a team use Storybook?](#2-why-would-a-team-use-storybook)
- [3: What is a story?](#3-what-is-a-story)
- [4: How do you add Storybook to an existing project?](#4-how-do-you-add-storybook-to-an-existing-project)
- [5: How do you start Storybook and how do you build it?](#5-how-do-you-start-storybook-and-how-do-you-build-it)
- [6: What files are in the `.storybook` folder?](#6-what-files-are-in-the-storybook-folder)
- [7: What is CSF?](#7-what-is-csf)
- [8: What can you put in the default export (meta) of a story file?](#8-what-can-you-put-in-the-default-export-meta-of-a-story-file)
- [9: What are args?](#9-what-are-args)
- [10: What is the Controls panel?](#10-what-is-the-controls-panel)
- [11: What is the Actions panel and how do you log events?](#11-what-is-the-actions-panel-and-how-do-you-log-events)
- [12: What is an addon?](#12-what-is-an-addon)
- [13: How do you install an addon?](#13-how-do-you-install-an-addon)
- [14: What are parameters?](#14-what-are-parameters)
- [15: What is a decorator?](#15-what-is-a-decorator)
- [16: What is Autodocs?](#16-what-is-autodocs)
- [17: How does Storybook decide where a story appears in the sidebar?](#17-how-does-storybook-decide-where-a-story-appears-in-the-sidebar)
- [18: How do you change the name a story shows in the sidebar?](#18-how-do-you-change-the-name-a-story-shows-in-the-sidebar)
- [19: What is the difference between the Canvas and the Docs page?](#19-what-is-the-difference-between-the-canvas-and-the-docs-page)
- [20: How do you check how a component looks on different screen sizes?](#20-how-do-you-check-how-a-component-looks-on-different-screen-sizes)
- [21: How do you change the background color behind a story?](#21-how-do-you-change-the-background-color-behind-a-story)
- [22: How would you write stories for loading, error and empty states?](#22-how-would-you-write-stories-for-loading-error-and-empty-states)
- [23: What is a play function?](#23-what-is-a-play-function)
- [24: Which frameworks does Storybook support?](#24-which-frameworks-does-storybook-support)
- [25: What is MDX in Storybook?](#25-what-is-mdx-in-storybook)
- [26: Where should you put story files?](#26-where-should-you-put-story-files)
- [27: How do you serve images, fonts or other static files in Storybook?](#27-how-do-you-serve-images-fonts-or-other-static-files-in-storybook)
- [28: How do you load global CSS and fonts for all stories?](#28-how-do-you-load-global-css-and-fonts-for-all-stories)
- [29: How do you deploy Storybook?](#29-how-do-you-deploy-storybook)
- [30: Can you open a story directly by URL?](#30-can-you-open-a-story-directly-by-url)

### Moderate Questions (31-60)

- [31: What is the difference between CSF2 and CSF3?](#31-what-is-the-difference-between-csf2-and-csf3)
- [32: How are args merged between preview, meta and story?](#32-how-are-args-merged-between-preview-meta-and-story)
- [33: How do you customize the controls for a prop?](#33-how-do-you-customize-the-controls-for-a-prop)
- [34: How do you hide a prop from Controls or show a control only in some cases?](#34-how-do-you-hide-a-prop-from-controls-or-show-a-control-only-in-some-cases)
- [35: When do you need a custom `render` function?](#35-when-do-you-need-a-custom-render-function)
- [36: How do you write an interaction test in Storybook?](#36-how-do-you-write-an-interaction-test-in-storybook)
- [37: What does `step` do in a play function?](#37-what-does-step-do-in-a-play-function)
- [38: How do you wait for async UI in a play function?](#38-how-do-you-wait-for-async-ui-in-a-play-function)
- [39: How do you render a component that needs a provider, like a theme or a router?](#39-how-do-you-render-a-component-that-needs-a-provider-like-a-theme-or-a-router)
- [40: What are globals and how do you add a toolbar switch?](#40-what-are-globals-and-how-do-you-add-a-toolbar-switch)
- [41: What is the difference between args, parameters and globals?](#41-what-is-the-difference-between-args-parameters-and-globals)
- [42: What are loaders?](#42-what-are-loaders)
- [43: What is `beforeEach` in Storybook and how do you clean up?](#43-what-is-beforeeach-in-storybook-and-how-do-you-clean-up)
- [44: How do you mock API requests in Storybook?](#44-how-do-you-mock-api-requests-in-storybook)
- [45: What is the Vitest addon?](#45-what-is-the-vitest-addon)
- [46: How do you check accessibility in Storybook?](#46-how-do-you-check-accessibility-in-storybook)
- [47: What is visual testing and how does Storybook do it?](#47-what-is-visual-testing-and-how-does-storybook-do-it)
- [48: What are tags and how are they used?](#48-what-are-tags-and-how-are-they-used)
- [49: How do you customize a component's docs page?](#49-how-do-you-customize-a-components-docs-page)
- [50: How does Storybook get prop types and descriptions for the docs table?](#50-how-does-storybook-get-prop-types-and-descriptions-for-the-docs-table)
- [51: How can you reuse stories in unit tests?](#51-how-can-you-reuse-stories-in-unit-tests)
- [52: How do you change the Vite or Webpack config that Storybook uses?](#52-how-do-you-change-the-vite-or-webpack-config-that-storybook-uses)
- [53: How do environment variables work in Storybook?](#53-how-do-environment-variables-work-in-storybook)
- [54: How do you use Storybook with Next.js?](#54-how-do-you-use-storybook-with-nextjs)
- [55: How do you write stories for Angular components?](#55-how-do-you-write-stories-for-angular-components)
- [56: How do you update args from inside a story?](#56-how-do-you-update-args-from-inside-a-story)
- [57: How do you change the look of the Storybook UI itself?](#57-how-do-you-change-the-look-of-the-storybook-ui-itself)
- [58: What is Storybook Composition?](#58-what-is-storybook-composition)
- [59: How do you upgrade Storybook to a new major version?](#59-how-do-you-upgrade-storybook-to-a-new-major-version)
- [60: Is there a linter for story files?](#60-is-there-a-linter-for-story-files)

### Advanced Questions (61-90)

- [61: How is Storybook built internally? What are the manager and the preview?](#61-how-is-storybook-built-internally-what-are-the-manager-and-the-preview)
- [62: How does Storybook find stories without running every file?](#62-how-does-storybook-find-stories-without-running-every-file)
- [63: How does Storybook stay fast with thousands of stories?](#63-how-does-storybook-stay-fast-with-thousands-of-stories)
- [64: How would you speed up building and testing Storybook in CI?](#64-how-would-you-speed-up-building-and-testing-storybook-in-ci)
- [65: How does module mocking work in Storybook 10?](#65-how-does-module-mocking-work-in-storybook-10)
- [66: How did module mocking work before `sb.mock`, and when might you still see it?](#66-how-did-module-mocking-work-before-sbmock-and-when-might-you-still-see-it)
- [67: What are CSF Factories?](#67-what-are-csf-factories)
- [68: What changed in Storybook 10 being ESM-only?](#68-what-changed-in-storybook-10-being-esm-only)
- [69: What is `mount` in a play function and when do you need it?](#69-what-is-mount-in-a-play-function-and-when-do-you-need-it)
- [70: How does the Vitest addon turn stories into tests?](#70-how-does-the-vitest-addon-turn-stories-into-tests)
- [71: Where do Storybook tests fit compared to unit tests and E2E tests?](#71-where-do-storybook-tests-fit-compared-to-unit-tests-and-e2e-tests)
- [72: Your visual tests are flaky. What are the usual causes and fixes?](#72-your-visual-tests-are-flaky-what-are-the-usual-causes-and-fixes)
- [73: How do you visually test the same story in light and dark themes and several viewports?](#73-how-do-you-visually-test-the-same-story-in-light-and-dark-themes-and-several-viewports)
- [74: How do you write a custom Storybook addon?](#74-how-do-you-write-a-custom-storybook-addon)
- [75: In what order do decorators run, and why does it matter?](#75-in-what-order-do-decorators-run-and-why-does-it-matter)
- [76: How do parameters merge, and how do you turn off a feature for one story?](#76-how-do-parameters-merge-and-how-do-you-turn-off-a-feature-for-one-story)
- [77: How would you set up Storybook for a design system in a monorepo?](#77-how-would-you-set-up-storybook-for-a-design-system-in-a-monorepo)
- [78: What should you think about for security when publishing Storybook?](#78-what-should-you-think-about-for-security-when-publishing-storybook)
- [79: How do you handle components with side effects like timers, localStorage or analytics?](#79-how-do-you-handle-components-with-side-effects-like-timers-localstorage-or-analytics)
- [80: Can you write stories for React Server Components?](#80-can-you-write-stories-for-react-server-components)
- [81: How do you measure test coverage from Storybook tests?](#81-how-do-you-measure-test-coverage-from-storybook-tests)
- [82: A story works in the Storybook UI but fails when run with the Vitest addon in CI. How do you debug it?](#82-a-story-works-in-the-storybook-ui-but-fails-when-run-with-the-vitest-addon-in-ci-how-do-you-debug-it)
- [83: How would you write stories for a large component that depends on many things (store, API, router, feature flags)?](#83-how-would-you-write-stories-for-a-large-component-that-depends-on-many-things-store-api-router-feature-flags)
- [84: How do you type stories correctly in TypeScript, and why is `satisfies` used?](#84-how-do-you-type-stories-correctly-in-typescript-and-why-is-satisfies-used)
- [85: How can Storybook help AI coding agents?](#85-how-can-storybook-help-ai-coding-agents)
- [86: How do you stop a Storybook from going stale over time?](#86-how-do-you-stop-a-storybook-from-going-stale-over-time)
- [87: How would you design a CI pipeline around Storybook?](#87-how-would-you-design-a-ci-pipeline-around-storybook)
- [88: How do you document and version a design system with Storybook?](#88-how-do-you-document-and-version-a-design-system-with-storybook)
- [89: How do you handle internationalization and right-to-left layouts in Storybook?](#89-how-do-you-handle-internationalization-and-right-to-left-layouts-in-storybook)
- [90: When is Storybook not worth it?](#90-when-is-storybook-not-worth-it)

---

# Easy Questions (1-30)

## 1: What is Storybook?

Storybook is a tool for building, viewing and testing UI components on their own, outside of your app. You write "stories" that render a component in a given state, and Storybook shows them in a browser UI where you can click through them, change props and read docs.

It works with React, Vue, Angular, Svelte, Web Components and a few other frameworks. Teams use it for component development, design systems, documentation and testing (interaction, accessibility and visual tests).

## 2: Why would a team use Storybook?

The main reasons:

- **Build components in isolation**: you don't need to log in, fill a form or click through five pages to see the state you are working on.
- **See every state in one place**: loading, error, empty, long text, disabled and so on are all written down as stories.
- **Living documentation**: designers, QA and other developers can browse the components without running the app.
- **Testing**: the same stories can be used for interaction tests, accessibility checks and visual regression tests.
- **Reuse**: people can find an existing component before building a new one.

## 3: What is a story?

A story is one rendered state of a component. For a `Button` you might have `Primary`, `Secondary`, `Disabled` and `Loading` stories. Each story is a named export in a `.stories` file and usually just sets the props (args) for that state.

```tsx
export const Disabled: Story = {
  args: { label: "Save", disabled: true },
};
```

A good rule: if a state is worth checking by hand, it is worth a story.

## 4: How do you add Storybook to an existing project?

Run the setup command in the root of the project:

```bash
npm create storybook@latest
```

It detects your framework and builder (for example React with Vite), installs the right packages, creates the `.storybook` folder, adds example stories and adds `storybook` and `build-storybook` scripts to `package.json`. Older guides use `npx storybook@latest init`, which does the same thing.

Storybook 10 is ESM-only and needs a recent Node version (20.16+, 22.19+ or 24+).

## 5: How do you start Storybook and how do you build it?

```bash
npm run storybook        # storybook dev -p 6006
npm run build-storybook  # storybook build
```

`storybook dev` starts a dev server (by default on port 6006) with hot reload. `storybook build` creates a static site in the `storybook-static` folder. That folder is plain HTML, CSS and JavaScript, so you can host it anywhere.

## 6: What files are in the `.storybook` folder?

- **`main.ts`**: project config. Where to find stories, which addons and framework to use, static folders, builder tweaks.
- **`preview.ts`** (or `.tsx`): runs in the iframe where stories render. Global decorators, parameters, args, global CSS imports and so on go here.
- **`manager.ts`** (optional): config for the Storybook UI itself, like a custom theme or sidebar settings.

You may also see `preview-head.html` and `manager-head.html` for adding tags to the `<head>` of each frame, and `vitest.setup.ts` if you use the Vitest addon.

## 7: What is CSF?

CSF (Component Story Format) is the format Storybook uses for story files. It is just an ES module:

- the **default export** (called "meta") describes the component,
- each **named export** is a story.

```tsx
import type { Meta, StoryObj } from "@storybook/react-vite";
import { Button } from "./Button";

const meta = {
  component: Button,
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: { label: "Button", variant: "primary" },
};
```

Since it is plain JavaScript, other tools (test runners, Chromatic, codemods) can read the same files.

## 8: What can you put in the default export (meta) of a story file?

The meta object holds settings shared by all stories in the file:

- `component`: the component (used for docs and controls)
- `title`: the sidebar path (optional, it can be generated from the file path)
- `args` and `argTypes`: default props and control settings
- `parameters`: static settings for addons and features
- `decorators`: wrappers around every story
- `tags`: like `['autodocs']`
- `loaders`, `beforeEach`, `render`, `play`: shared behavior
- `subcomponents`: related components shown in the docs

Anything set on meta can be overridden on a single story.

## 9: What are args?

Args are the inputs of a story, usually the component's props. Storybook passes them to the component, shows them in the Controls panel and lets you change them live.

```tsx
export const LongLabel: Story = {
  args: {
    label: "This is a very long button label that might wrap",
  },
};
```

Because args are plain data, Storybook can merge them, save them in the URL, and reuse them in tests.

## 10: What is the Controls panel?

It is the panel under the story that lets you edit args without changing code. Storybook picks a control for each prop based on its type: a checkbox for booleans, a text field for strings, a select for unions and so on.

It's handy for checking edge cases fast (long text, empty values, odd combinations) and for non-developers who want to play with a component. You can change the control type or hide a prop with `argTypes`.

## 11: What is the Actions panel and how do you log events?

The Actions panel shows when a callback prop (like `onClick`) is called and with which arguments. The usual way is to pass `fn()` from `storybook/test`:

```tsx
import { fn } from "storybook/test";

const meta = {
  component: Button,
  args: { onClick: fn() },
} satisfies Meta<typeof Button>;
```

`fn()` creates a spy, so the call shows up in the Actions panel and you can also check it in a play function with `expect(args.onClick).toHaveBeenCalled()`.

## 12: What is an addon?

An addon is a plugin that adds features to Storybook: a new panel, a toolbar button, extra docs or a different way to test.

Since Storybook 9, many of the old "essentials" (controls, actions, viewport, backgrounds, toolbars, measure, outline, highlight) are part of the core package, so you don't install them anymore. Common addons you still add yourself are `@storybook/addon-docs`, `@storybook/addon-a11y`, `@storybook/addon-vitest`, `@storybook/addon-links` and `@chromatic-com/storybook`.

## 13: How do you install an addon?

The simplest way is the `add` command:

```bash
npx storybook add @storybook/addon-a11y
```

It installs the package and adds it to the `addons` array in `.storybook/main.ts`. You can also do it by hand:

```ts
// .storybook/main.ts
addons: ['@storybook/addon-docs', '@storybook/addon-a11y'],
```

## 14: What are parameters?

Parameters are static settings for a story. They don't change while you look at the story, and they are mostly used to configure Storybook features and addons, like the layout, backgrounds, a11y rules or Chromatic options.

```tsx
export const FullPage: Story = {
  parameters: {
    layout: "fullscreen", // 'centered' | 'padded' | 'fullscreen'
  },
};
```

You can set them in `preview.ts` (all stories), on meta (one file) or on a single story. They are merged, with the most specific level winning.

## 15: What is a decorator?

A decorator is a function that wraps a story. You use it to add extra markup or context around the component, like padding, a theme provider or a router.

```tsx
const meta = {
  component: Card,
  decorators: [
    (Story) => (
      <div style={{ padding: 24, maxWidth: 400 }}>
        <Story />
      </div>
    ),
  ],
} satisfies Meta<typeof Card>;
```

Decorators can be added at the story, component (meta) or global (`preview.ts`) level.

## 16: What is Autodocs?

Autodocs creates a documentation page for a component from its stories. The page shows the component description, the first story with a Controls table, and then all other stories with their source code.

You turn it on with a tag, either for one component or for everything in `preview.ts`:

```tsx
const meta = {
  component: Button,
  tags: ["autodocs"],
} satisfies Meta<typeof Button>;
```

It needs `@storybook/addon-docs` to be installed. Prop descriptions come from TypeScript types and JSDoc comments on the component.

## 17: How does Storybook decide where a story appears in the sidebar?

If you set `title` on meta, that is used. Slashes create groups:

```tsx
const meta = {
  title: "Forms/Inputs/TextField",
  component: TextField,
} satisfies Meta<typeof TextField>;
```

If you leave `title` out, Storybook generates it from the file path relative to the stories glob (this is called auto-title). So `src/components/Forms/TextField.stories.tsx` shows up as `Components/Forms/TextField`. Most teams just rely on auto-title so folders and the sidebar stay in sync.

## 18: How do you change the name a story shows in the sidebar?

By default the export name is turned into words: `WithIcon` becomes "With Icon". To change it, use `name`:

```tsx
export const WithIcon: Story = {
  name: "With leading icon",
  args: { icon: "plus" },
};
```

Changing the name does not change the story ID, which still comes from the export name. In old CSF2 code you may see `storyName` instead.

## 19: What is the difference between the Canvas and the Docs page?

The **Canvas** shows one story at a time with the addon panels (Controls, Actions, Interactions and so on) below it. It is where you work on and test a single state.

The **Docs** page shows the whole component: description, props table and several stories on one page. It is meant for reading and is what most people outside the dev team will look at.

## 20: How do you check how a component looks on different screen sizes?

Use the viewport tool in the toolbar. It resizes the preview iframe to preset sizes like small mobile, large mobile and tablet. You can also add your own sizes and set a default for a story:

```tsx
export const Mobile: Story = {
  globals: {
    viewport: { value: "mobile1", isRotated: false },
  },
};
```

Since the iframe really changes width, media queries and container queries react the same way they would in a real browser window.

## 21: How do you change the background color behind a story?

Use the backgrounds tool in the toolbar. You define the options in parameters and pick one with globals:

```tsx
// .storybook/preview.ts
parameters: {
  backgrounds: {
    options: {
      light: { name: 'Light', value: '#ffffff' },
      dark: { name: 'Dark', value: '#1a1a1a' },
    },
  },
},
```

```tsx
export const OnDark: Story = {
  globals: { backgrounds: { value: "dark" } },
};
```

This is useful for components that need to work on both light and dark surfaces.

## 22: How would you write stories for loading, error and empty states?

Write one story per state and pass the props that produce it. That keeps every state easy to find and easy to test.

```tsx
export const Loading: Story = { args: { status: "loading" } };

export const Empty: Story = { args: { status: "success", items: [] } };

export const Error: Story = {
  args: { status: "error", errorMessage: "Could not load orders" },
};

export const WithData: Story = {
  args: { status: "success", items: mockOrders },
};
```

If the component fetches its own data, you mock the request (for example with MSW) or the data module instead of passing props.

## 23: What is a play function?

A play function is code that runs after a story renders. You use it to interact with the component (click, type, tab) and to check the result. That turns a story into an interaction test.

```tsx
import { expect } from "storybook/test";

export const FilledForm: Story = {
  play: async ({ canvas, userEvent }) => {
    await userEvent.type(canvas.getByLabelText("Email"), "jane@example.com");
    await userEvent.click(canvas.getByRole("button", { name: "Sign in" }));
    await expect(canvas.getByText("Welcome back")).toBeInTheDocument();
  },
};
```

You can watch each step in the Interactions panel.

## 24: Which frameworks does Storybook support?

Official frameworks include React, Vue 3, Angular, Svelte and SvelteKit, Preact, Web Components, Next.js, React Native (a separate on-device setup plus React Native Web) and HTML. Each has its own framework package, for example `@storybook/react-vite`, `@storybook/nextjs-vite`, `@storybook/angular` or `@storybook/vue3-vite`.

The framework package sets up the renderer and the builder (Vite or Webpack) for you, so you usually don't configure the bundler from scratch.

## 25: What is MDX in Storybook?

MDX is Markdown with JSX inside it. In Storybook you use `.mdx` files to write custom documentation pages: guides, design token pages, usage notes, or a component page with text between examples.

```mdx
import { Meta, Canvas, Controls } from "@storybook/addon-docs/blocks";
import * as ButtonStories from "./Button.stories";

<Meta of={ButtonStories} />

# Button

Use the primary button for the main action on a page.

<Canvas of={ButtonStories.Primary} />
<Controls />
```

Stories themselves should stay in CSF files. MDX is for docs.

## 26: Where should you put story files?

Most teams put the story file next to the component:

```
src/components/Button/
  Button.tsx
  Button.stories.tsx
  Button.test.tsx
```

The `stories` field in `.storybook/main.ts` tells Storybook which files to load, for example `'../src/**/*.stories.@(js|jsx|ts|tsx)'` and `'../src/**/*.mdx'`. Keeping stories close to the code makes them easier to find and harder to forget when the component changes.

## 27: How do you serve images, fonts or other static files in Storybook?

Use `staticDirs` in `main.ts`:

```ts
// .storybook/main.ts
const config: StorybookConfig = {
  staticDirs: ["../public"],
  // or map a folder to a path:
  // staticDirs: [{ from: '../src/assets', to: '/assets' }],
};
```

Files in those folders are served from the root (or from the `to` path), just like a `public` folder in Vite or Next.js. You can also import assets directly in your components if your bundler handles them.

## 28: How do you load global CSS and fonts for all stories?

Import them in `.storybook/preview.ts`, the same way your app's entry file does:

```ts
// .storybook/preview.ts
import "../src/styles/globals.css";
import "@fontsource/inter";
```

For fonts loaded with a `<link>` tag, put the tag in `.storybook/preview-head.html`. If the components look different in Storybook than in the app, missing global styles are the first thing to check.

## 29: How do you deploy Storybook?

Run `storybook build` and deploy the `storybook-static` folder. It is a static site, so you can deploy it like any other: GitHub Pages, Netlify, Vercel, S3 plus CloudFront, or an internal server.

Many teams publish it with Chromatic, which also hosts a version per branch or pull request and runs visual tests. A good habit is to build Storybook in CI for every pull request, so reviewers can open a link and see the changed components.

## 30: Can you open a story directly by URL?

Yes. Each story has an ID made from its title and export name, like `components-button--primary`, and you can link to it:

```
http://localhost:6006/?path=/story/components-button--primary
http://localhost:6006/?path=/docs/components-button--docs
```

You can also set args in the URL, for example `&args=label:Hello;disabled:!true`. To show only the story without the Storybook UI, use the iframe URL: `iframe.html?id=components-button--primary&viewMode=story`. That is handy for sharing a state with a designer or embedding it somewhere.

# Moderate Questions (31-60)

## 31: What is the difference between CSF2 and CSF3?

In CSF2 every story was a function, and you made variants by cloning a template:

```tsx
// CSF2 (legacy)
const Template = (args) => <Button {...args} />;
export const Primary = Template.bind({});
Primary.args = { label: "Button", primary: true };
```

In CSF3 a story is an object. If you don't give a `render` function, Storybook renders `meta.component` with the args for you:

```tsx
// CSF3
export const Primary: Story = {
  args: { label: "Button", primary: true },
};
```

CSF3 has less boilerplate, args are merged from meta automatically, and it is easier to type and to analyze statically. You can convert old files with `npx storybook migrate csf-2-to-3 --glob="src/**/*.stories.tsx"`.

## 32: How are args merged between preview, meta and story?

Args are merged from the least specific to the most specific level:

1. `args` in `.storybook/preview.ts` (all stories)
2. `args` on meta (all stories in the file)
3. `args` on the story
4. args changed by the user in Controls or set in the URL

A later level overrides keys from an earlier one, but keeps the keys it doesn't set. So you can put shared defaults on meta and only write the differences in each story:

```tsx
const meta = {
  component: Alert,
  args: { title: "Heads up", dismissible: true },
} satisfies Meta<typeof Alert>;

export const NotDismissible: Story = {
  args: { dismissible: false }, // title still comes from meta
};
```

## 33: How do you customize the controls for a prop?

Use `argTypes`. You can change the control type, set the list of options, or map simple values to complex ones:

```tsx
const meta = {
  component: Icon,
  argTypes: {
    size: {
      control: { type: "range", min: 12, max: 64, step: 4 },
    },
    color: { control: "color" },
    name: {
      control: "select",
      options: ["home", "search", "settings"],
    },
    badge: {
      options: ["none", "dot", "count"],
      mapping: {
        none: undefined,
        dot: <Dot />,
        count: <Count value={3} />,
      },
    },
  },
} satisfies Meta<typeof Icon>;
```

`mapping` is useful because controls can only hold serializable values. You show simple labels in the UI and Storybook passes the real value (a React element, a function, a date) to the component.

## 34: How do you hide a prop from Controls or show a control only in some cases?

To hide a prop from the Controls panel and the docs table:

```tsx
argTypes: {
  className: { table: { disable: true } },
  onChange: { control: false }, // keep it in the table, but no control
},
```

To show a control only when another arg has a certain value, use `if`:

```tsx
argTypes: {
  hasIcon: { control: 'boolean' },
  icon: { control: 'select', options: ['plus', 'trash'], if: { arg: 'hasIcon' } },
},
```

You can also hide a whole group with `parameters.controls.exclude`, for example `exclude: /^on.*/` to hide all event handlers.

## 35: When do you need a custom `render` function?

When the story needs more than "render the component with these args". Common cases are compound components, rendering several instances side by side, or wrapping the component with siblings:

```tsx
export const InsideAList: Story = {
  render: (args) => (
    <ul>
      <ListItem {...args} />
      <ListItem {...args} label="Second item" />
      <ListItem {...args} label="Third item" />
    </ul>
  ),
};
```

Keep passing `args` through, otherwise Controls won't affect the story. If you need the same `render` for every story in the file, put it on meta. If you need it to wrap something in a provider, a decorator is usually a better fit.

## 36: How do you write an interaction test in Storybook?

Write a `play` function that uses `userEvent` to act like a user and `expect` to check the result. Both come from `storybook/test`, and the `canvas` (Testing Library queries scoped to the story) and `userEvent` are passed in the play context:

```tsx
import { expect, fn } from "storybook/test";

const meta = {
  component: LoginForm,
  args: { onSubmit: fn() },
} satisfies Meta<typeof LoginForm>;
export default meta;

export const SubmitsValues: Story = {
  play: async ({ args, canvas, userEvent }) => {
    await userEvent.type(canvas.getByLabelText("Email"), "jane@example.com");
    await userEvent.type(canvas.getByLabelText("Password"), "secret123");
    await userEvent.click(canvas.getByRole("button", { name: /sign in/i }));

    await expect(args.onSubmit).toHaveBeenCalledWith({
      email: "jane@example.com",
      password: "secret123",
    });
  },
};
```

The Interactions panel lists every step, and you can go back and forward through them to see the component at each point. In CI you run the same story as a test with the Vitest addon.

## 37: What does `step` do in a play function?

`step` groups several actions under a label. The Interactions panel shows the groups, which makes long tests easier to read and failures easier to locate.

```tsx
play: async ({ canvas, userEvent, step }) => {
  await step('Fill in shipping address', async () => {
    await userEvent.type(canvas.getByLabelText('Street'), 'Main St 1');
    await userEvent.type(canvas.getByLabelText('City'), 'Tbilisi');
  });

  await step('Submit', async () => {
    await userEvent.click(canvas.getByRole('button', { name: 'Continue' }));
  });
},
```

## 38: How do you wait for async UI in a play function?

Use the async queries or `waitFor`, never fixed timeouts:

```tsx
import { expect, waitFor } from 'storybook/test';

// inside the story
play: async ({ canvas, userEvent }) => {
  await userEvent.click(canvas.getByRole('button', { name: 'Load more' }));

  // waits until the element appears (default timeout 1000ms)
  const rows = await canvas.findAllByRole('row');
  await expect(rows).toHaveLength(20);

  // or wait for any condition
  await waitFor(() => expect(canvas.queryByText('Loading...')).not.toBeInTheDocument());
},
```

`findBy*` and `waitFor` keep retrying until the check passes or the timeout runs out. A fixed `setTimeout` is either too short on a slow CI machine or wastes time on a fast one. Remember to `await` every `expect`, otherwise the Interactions panel may not show it correctly.

## 39: How do you render a component that needs a provider, like a theme or a router?

Add a decorator that wraps the story in the provider. If every component needs it, put it in `preview.tsx`:

```tsx
// .storybook/preview.tsx
import type { Preview } from "@storybook/react-vite";
import { ThemeProvider } from "../src/theme";
import { MemoryRouter } from "react-router";

const preview: Preview = {
  decorators: [
    (Story) => (
      <MemoryRouter>
        <ThemeProvider theme="light">
          <Story />
        </ThemeProvider>
      </MemoryRouter>
    ),
  ],
};

export default preview;
```

If only some stories need it, add the decorator to that meta or story. For things like a Redux store you often create a fresh store per story inside the decorator, so state from one story doesn't leak into the next.

## 40: What are globals and how do you add a toolbar switch?

Globals are values that apply to the whole Storybook, not to one story, for example the theme or the locale. You define them with `globalTypes` and give a default with `initialGlobals`:

```tsx
// .storybook/preview.tsx
const preview: Preview = {
  globalTypes: {
    theme: {
      description: "Color theme",
      toolbar: {
        title: "Theme",
        icon: "circlehollow",
        items: ["light", "dark"],
        dynamicTitle: true,
      },
    },
  },
  initialGlobals: { theme: "light" },
  decorators: [
    (Story, context) => (
      <ThemeProvider theme={context.globals.theme}>
        <Story />
      </ThemeProvider>
    ),
  ],
};
```

This adds a dropdown to the toolbar, and the decorator reads the selected value from `context.globals`. A story can force a value with `globals: { theme: 'dark' }`.

## 41: What is the difference between args, parameters and globals?

- **Args**: inputs for one story, usually props. They can change at runtime through Controls.
- **Parameters**: static settings for the story and addons. They don't change while viewing the story.
- **Globals**: values for the whole Storybook (theme, locale, viewport), usually changed from the toolbar. They stay the same when you switch stories.

A quick test: if it's a prop of the component, it's an arg. If it configures a tool, it's a parameter. If the user switches it for all stories at once, it's a global.

## 42: What are loaders?

Loaders are async functions that run before a story renders. Their result is available as `loaded` in the story context:

```tsx
export const WithUser: Story = {
  loaders: [
    async () => ({
      user: await (await fetch("/mocks/user.json")).json(),
    }),
  ],
  render: (args, { loaded: { user } }) => <Profile {...args} user={user} />,
};
```

They're useful for loading data or doing async setup that the render function needs. For things like mocking modules, seeding storage or setting the date, `beforeEach` is usually cleaner. Keep in mind that data from loaders doesn't show up in Controls, because it's not an arg.

## 43: What is `beforeEach` in Storybook and how do you clean up?

`beforeEach` runs before each story renders (and before the play function). You can set it in `preview.ts`, on meta or on a story. If it returns a function, Storybook runs that function as cleanup when you leave the story or rerun it.

```tsx
import { mocked } from "storybook/test";
import { getCurrentUser } from "../lib/session";

const meta = {
  component: Header,
  beforeEach: async () => {
    mocked(getCurrentUser).mockReturnValue({ name: "Jane" });
    localStorage.setItem("sidebar", "collapsed");

    return () => {
      localStorage.clear();
    };
  },
} satisfies Meta<typeof Header>;
```

There's also `beforeAll` in `preview.ts` for setup that should run once for the whole Storybook.

## 44: How do you mock API requests in Storybook?

The most common way is MSW (Mock Service Worker) with `msw-storybook-addon`. MSW intercepts network requests in the browser, so the component code stays the same.

```tsx
// .storybook/preview.ts
import { initialize, mswLoader } from "msw-storybook-addon";

initialize();

const preview: Preview = {
  loaders: [mswLoader],
};
```

```tsx
// UserList.stories.tsx
import { http, HttpResponse, delay } from "msw";

export const Success: Story = {
  parameters: {
    msw: {
      handlers: [
        http.get("/api/users", () =>
          HttpResponse.json([{ id: 1, name: "Jane" }]),
        ),
      ],
    },
  },
};

export const Slow: Story = {
  parameters: {
    msw: {
      handlers: [
        http.get("/api/users", async () => {
          await delay("infinite");
        }),
      ],
    },
  },
};
```

You need to run `npx msw init public/` once and add `public` to `staticDirs` so the service worker file is served.

## 45: What is the Vitest addon?

`@storybook/addon-vitest` turns your stories into Vitest tests. Every story becomes a test that renders the component in a real browser (Vitest browser mode with Playwright) and runs its play function. A story with no play function is still a "smoke test": it fails if the component throws while rendering.

You can run the tests from the testing widget in the Storybook sidebar, or from the command line:

```bash
npx vitest --project=storybook
```

It works with Vite-based frameworks (like `@storybook/react-vite`, `@storybook/nextjs-vite`, `@storybook/vue3-vite`). It can also run accessibility checks and collect coverage. Projects on Webpack can use the older `@storybook/test-runner` instead.

## 46: How do you check accessibility in Storybook?

Add `@storybook/addon-a11y`. It runs axe-core against each story and shows violations, passes and incomplete checks in an Accessibility panel. It can also highlight the elements with problems.

With the Vitest addon, a11y checks also run as part of your tests. You control how strict they are with `parameters.a11y.test`:

```ts
// .storybook/preview.ts
parameters: {
  a11y: {
    test: 'error', // 'error' fails the test, 'todo' only warns, 'off' skips
  },
},
```

You can set `'todo'` globally while you fix existing issues and `'error'` for components that are already clean. Automated checks only catch part of real a11y issues, so manual keyboard and screen reader testing is still needed.

## 47: What is visual testing and how does Storybook do it?

Visual testing takes a screenshot of each story and compares it with an accepted baseline. If pixels change, the test flags it and someone reviews whether the change is wanted.

The usual tool is Chromatic (made by the Storybook team). With `@chromatic-com/storybook` installed you can run visual tests from the Storybook UI, and in CI you run:

```bash
npx chromatic --project-token=$CHROMATIC_PROJECT_TOKEN
```

Chromatic renders each story in real browsers, shows diffs in a review UI and can block a pull request until changes are accepted. Other options include Playwright screenshots of story iframes, or tools like Percy and Lost Pixel.

## 48: What are tags and how are they used?

Tags are labels on stories, set on preview, meta or story level. Storybook has some built-in ones:

- `autodocs`: create a docs page
- `dev`: show in the sidebar (on by default)
- `test`: include in test runs (on by default)

A `!` removes a tag. For example, a story that only exists for testing and should not clutter the sidebar:

```tsx
export const KeyboardNavigationTest: Story = {
  tags: ["!dev", "!autodocs"],
  play: async ({ canvas, userEvent }) => {
    // ...
  },
};
```

You can also add your own tags like `experimental` or `deprecated` and filter by them in the sidebar or in test config.

## 49: How do you customize a component's docs page?

You have a few options, from small to big changes:

- **JSDoc comments** on the component and props show up as descriptions.
- **`parameters.docs`** lets you change things like the description or source code display:

```tsx
parameters: {
  docs: {
    description: { component: 'Use for the main action on a page.' },
    source: { type: 'code' },
  },
},
```

- **A custom page template** with `parameters.docs.page`, built from doc blocks like `Title`, `Description`, `Primary`, `Controls` and `Stories`.
- **An MDX file** attached to the stories with `<Meta of={ButtonStories} />` for full control over the page.

## 50: How does Storybook get prop types and descriptions for the docs table?

It uses a docgen tool to read the component source. For React the default is `react-docgen`, which is fast. If your props use complex TypeScript types (imported types, generics, utility types) you can switch to `react-docgen-typescript`, which is more accurate but slower:

```ts
// .storybook/main.ts
typescript: {
  reactDocgen: 'react-docgen-typescript',
},
```

Comments on props become descriptions:

```tsx
type ButtonProps = {
  /** Text shown inside the button */
  label: string;
  /** Visual style of the button */
  variant?: "primary" | "secondary";
};
```

Angular uses Compodoc for the same job, and Vue uses `vue-component-meta` or `vue-docgen-api`.

## 51: How can you reuse stories in unit tests?

Use portable stories. `composeStories` takes a story file and returns components with all args, decorators, loaders and project config applied:

```tsx
// Button.test.tsx
import { composeStories } from "@storybook/react-vite";
import { render, screen } from "@testing-library/react";
import * as stories from "./Button.stories";

const { Primary, Disabled } = composeStories(stories);

test("primary button shows its label", () => {
  render(<Primary />);
  expect(screen.getByRole("button", { name: "Button" })).toBeInTheDocument();
});

test("runs the story play function", async () => {
  await Disabled.run();
});
```

For this to pick up global decorators, call `setProjectAnnotations` with your preview config in the test setup file. If you use the Vitest addon, you usually don't need this, because it already runs every story as a test.

## 52: How do you change the Vite or Webpack config that Storybook uses?

Use `viteFinal` or `webpackFinal` in `main.ts`. Storybook passes its config and you return a changed version:

```ts
// .storybook/main.ts
import type { StorybookConfig } from "@storybook/react-vite";
import { mergeConfig } from "vite";
import { fileURLToPath } from "node:url";

const config: StorybookConfig = {
  framework: "@storybook/react-vite",
  stories: ["../src/**/*.stories.@(ts|tsx)"],
  async viteFinal(config) {
    return mergeConfig(config, {
      resolve: {
        alias: { "@": fileURLToPath(new URL("../src", import.meta.url)) },
      },
    });
  },
};

export default config;
```

With Vite, Storybook already loads your project's `vite.config` by default, so most aliases and plugins work without changes. You mostly need `viteFinal` for Storybook-only tweaks.

## 53: How do environment variables work in Storybook?

With the Vite builder, variables that start with `VITE_` are available as `import.meta.env.VITE_...`, same as in your app. Storybook also exposes variables that start with `STORYBOOK_`. You can set extra ones in `main.ts`:

```ts
env: (config) => ({
  ...config,
  API_BASE_URL: 'https://mock.example.com',
}),
```

Remember that these values end up in the built JavaScript. A deployed Storybook is a public static site in most setups, so never put secrets or private API keys in them.

## 54: How do you use Storybook with Next.js?

Use the Next.js framework package, preferably `@storybook/nextjs-vite` (there is also the Webpack-based `@storybook/nextjs`). It handles things like `next/image`, `next/font`, `next/link`, routing and CSS setup for you.

For components that use the App Router hooks (`useRouter`, `usePathname`, `useSearchParams` from `next/navigation`), turn on the app directory mode and set the route:

```tsx
export const ActiveLink: Story = {
  parameters: {
    nextjs: {
      appDirectory: true,
      navigation: { pathname: "/settings/profile" },
    },
  },
};
```

Storybook mocks the router, so calls like `router.push` show up in the Actions panel instead of navigating.

## 55: How do you write stories for Angular components?

You use `@storybook/angular`. Dependencies are provided with decorators: `moduleMetadata` for imports and declarations, `applicationConfig` for app-level providers.

```ts
import type { Meta, StoryObj } from "@storybook/angular";
import { applicationConfig, moduleMetadata } from "@storybook/angular";
import { provideHttpClient } from "@angular/common/http";
import { provideAnimations } from "@angular/platform-browser/animations";
import { UserCardComponent } from "./user-card.component";
import { AvatarComponent } from "../avatar/avatar.component";

const meta: Meta<UserCardComponent> = {
  component: UserCardComponent,
  decorators: [
    moduleMetadata({ imports: [AvatarComponent] }),
    applicationConfig({
      providers: [provideHttpClient(), provideAnimations()],
    }),
  ],
};
export default meta;

type Story = StoryObj<UserCardComponent>;

export const Default: Story = {
  args: { name: "Jane Doe", role: "Admin" },
};
```

Inputs map to args and outputs show up as actions. Storybook runs through Angular builders in `angular.json`, and docs use Compodoc.

## 56: How do you update args from inside a story?

Use the `useArgs` hook from `storybook/preview-api`. It's common for controlled components, where the component calls `onChange` and the story has to update the `value` arg so the UI and Controls stay in sync:

```tsx
import { useArgs } from "storybook/preview-api";

export const Controlled: Story = {
  args: { checked: false },
  render: function Render(args) {
    const [, updateArgs] = useArgs();
    return <Switch {...args} onChange={(checked) => updateArgs({ checked })} />;
  },
};
```

Using a named function for `render` keeps hook lint rules happy.

## 57: How do you change the look of the Storybook UI itself?

Create a theme in `.storybook/manager.ts`:

```ts
import { addons } from "storybook/manager-api";
import { create } from "storybook/theming";

addons.setConfig({
  theme: create({
    base: "light",
    brandTitle: "Acme Design System",
    brandUrl: "https://acme.example.com",
    brandImage: "/logo.svg",
    colorPrimary: "#0055ff",
    colorSecondary: "#0055ff",
  }),
});
```

This changes the sidebar, toolbar and panels. To use the same theme on docs pages, also set `parameters.docs.theme` in `preview.ts`.

## 58: What is Storybook Composition?

Composition lets one Storybook show stories from other published Storybooks in its sidebar. You list them under `refs` in `main.ts`:

```ts
refs: {
  'design-system': {
    title: 'Acme Design System',
    url: 'https://design.acme.example.com',
  },
},
```

It's useful in big companies where each team owns its own Storybook, or when an app wants to show the shared design system next to its own components. The referenced Storybooks are loaded at runtime, so they aren't rebuilt with your project.

## 59: How do you upgrade Storybook to a new major version?

Run the upgrade command:

```bash
npx storybook@latest upgrade
```

It updates all Storybook packages to matching versions and then runs automigrations, which are small scripts that fix config for known breaking changes (renamed packages, moved imports, removed options). After that:

1. Read the migration guide for the version you're moving to.
2. Run `npx storybook doctor` to check for mismatched versions or duplicated packages.
3. Run your story tests and visual tests to catch anything that renders differently.

All `storybook` and `@storybook/*` packages should be on the same version. Mixed versions are a common cause of strange errors.

## 60: Is there a linter for story files?

Yes, `eslint-plugin-storybook`. It catches common mistakes, for example a missing default export, an `await` missing before `userEvent` or `expect` in a play function, or importing from packages that should come from `storybook/test`.

```js
// eslint.config.js
import storybook from "eslint-plugin-storybook";

export default [
  // ...your other configs
  ...storybook.configs["flat/recommended"],
];
```

`npm create storybook` usually sets it up for you if the project already uses ESLint.

# Advanced Questions (61-90)

## 61: How is Storybook built internally? What are the manager and the preview?

Storybook runs as two separate apps:

- **Manager**: the Storybook UI (sidebar, toolbar, addon panels). It is a prebuilt React app and doesn't load your components.
- **Preview**: an iframe where your stories render. This is built with your project's builder (Vite or Webpack) and includes your components, `preview.ts`, decorators and so on.

They talk through a **channel** built on `postMessage`. When you change a control, the manager sends an event like `updateStoryArgs`, the preview re-renders and sends events back (for example a new action or a test result).

Keeping the preview in an iframe means your component's CSS and JavaScript can't break the Storybook UI, and the Storybook UI styles don't leak into your components. It also makes viewport resizing real, since the iframe really changes width.

## 62: How does Storybook find stories without running every file?

On startup Storybook builds a story **index**. It reads each file matched by the `stories` globs and statically analyzes it (parses the code, it doesn't execute it) to get the title, the exported stories, their names and tags. The result is served as `index.json` and drives the sidebar and search.

Because of this, CSF files must be statically analyzable:

- the default export must be an object (or `preview.meta(...)` with CSF Factories),
- `title`, if set, should be a string literal,
- stories must be named exports, not generated in a loop.

```tsx
// This won't work: the indexer can't see these stories
sizes.forEach((size) => {
  exports[size] = { args: { size } };
});
```

Tools like Chromatic and the Vitest addon also rely on the index, so the same rules matter for them. You can add custom indexers through `experimental_indexers` in `main.ts` to load stories from other file formats.

## 63: How does Storybook stay fast with thousands of stories?

Mostly through on-demand loading. Storybook builds the index from static analysis first, and only loads (compiles and runs) a story file when you open one of its stories. With Vite, files are compiled on request anyway. With Webpack you can turn on `lazyCompilation` in the builder options.

So startup time depends mainly on how many files have to be indexed, not on how heavy every component is. Where it still gets slow:

- very wide `stories` globs that scan `node_modules` or build output
- heavy `preview.ts` imports that every story pays for (big icon sets, the whole app's providers)
- slow docgen on large TypeScript codebases
- many addons

Keep globs tight, keep the preview file light, and only load the heavy providers in the stories that need them.

## 64: How would you speed up building and testing Storybook in CI?

A few things that usually help the most:

- **`storybook build --test`**: builds a version meant for testing. It skips things that tests don't need, like docs pages and some addons, so it's a lot faster.
- **Turn off docgen when you don't need it**: `typescript: { reactDocgen: false }` in a test-only build.
- **Use the Vite builder** if you're still on Webpack.
- **Cache** `node_modules` and the Vite cache between CI runs, and install only the Playwright browser you need (`npx playwright install chromium`).
- **Run only what changed**: Chromatic's TurboSnap and Vitest's `--changed` flag can skip stories whose dependencies didn't change.
- **Shard** the Vitest tests across machines with `--shard=1/4` and so on.

Measure first. Often one slow docgen setup or a huge global decorator is the real cause.

## 65: How does module mocking work in Storybook 10?

Storybook 10 added `sb.mock`, which is based on Vitest's mocking. You register mocks once in `.storybook/preview.ts`:

```ts
// .storybook/preview.ts
import { sb } from "storybook/test";

// replace every export with a spy that does nothing
sb.mock(import("../src/lib/analytics.ts"));

// keep the real code, but record calls
sb.mock(import("../src/lib/session.ts"), { spy: true });

// use the file from ../src/lib/__mocks__/api.ts if it exists
sb.mock(import("../src/lib/api.ts"));
```

Then in a story you change the behavior per story:

```tsx
import { expect, mocked } from "storybook/test";
import { getCurrentUser } from "../lib/session";
import { trackEvent } from "../lib/analytics";

export const LoggedIn: Story = {
  beforeEach: () => {
    mocked(getCurrentUser).mockReturnValue({ id: "1", name: "Jane" });
  },
  play: async ({ canvas, userEvent }) => {
    await userEvent.click(canvas.getByRole("button", { name: "Upgrade" }));
    await expect(trackEvent).toHaveBeenCalledWith("upgrade_clicked");
  },
};
```

It works with both Vite and Webpack, in dev and in the built Storybook, and spies are reset between stories. It's a good fit for components that import things directly (analytics, feature flags, auth helpers) instead of getting them as props.

## 66: How did module mocking work before `sb.mock`, and when might you still see it?

The older approach used Node.js subpath imports with a `storybook` condition in `package.json`:

```json
{
  "imports": {
    "#lib/session": {
      "storybook": "./src/lib/session.mock.ts",
      "default": "./src/lib/session.ts"
    },
    "#*": ["./src/*", "./src/*.ts", "./src/*.tsx"]
  }
}
```

The component imports `#lib/session`. In Storybook the bundler resolves it to the mock file, and in the app it resolves to the real one. The mock file usually wraps the real functions in `fn()` so stories can change them.

You'll still see this in projects that started on Storybook 8 or 9. It works, but every mocked module has to be imported through a `#` path, which changes your app code. With `sb.mock` the app code stays untouched, so in new projects `sb.mock` is the better default.

## 67: What are CSF Factories?

CSF Factories is a newer way to write stories with full type safety. Instead of plain objects, you build everything through functions that carry types from the main config to the preview to each story:

```ts
// .storybook/main.ts
import { defineMain } from "@storybook/react-vite/node";

export default defineMain({
  framework: "@storybook/react-vite",
  stories: ["../src/**/*.stories.@(ts|tsx)"],
  addons: ["@storybook/addon-docs", "@storybook/addon-a11y"],
});
```

```ts
// .storybook/preview.ts
import { definePreview } from "@storybook/react-vite";
import addonDocs from "@storybook/addon-docs";
import addonA11y from "@storybook/addon-a11y";

export default definePreview({
  addons: [addonDocs(), addonA11y()],
});
```

```tsx
// Button.stories.tsx
import preview from "../../.storybook/preview";
import { Button } from "./Button";

const meta = preview.meta({ component: Button, args: { label: "Button" } });

export const Primary = meta.story({ args: { variant: "primary" } });
export const PrimaryLarge = Primary.extend({ args: { size: "large" } });
```

Benefits: addon parameters are typed (because addons are passed to `definePreview`), you can extend a story instead of spreading args by hand, and stories can be used in tests without `composeStories`. In Storybook 10 it's in preview status, it started with React and is spreading to other frameworks, and the plan is to make it the default in Storybook 11. Regular CSF3 keeps working, and there's an automigration to convert files.

## 68: What changed in Storybook 10 being ESM-only?

Storybook 10 ships only ES modules. Things to know:

- `.storybook/main` must be valid ESM. `require()`, `module.exports` and `__dirname` don't work there. Use `import`, `export default` and `import.meta.url` (or `import.meta.dirname`).
- It needs Node 20.16+, 22.19+ or 24+, which can `require()` ESM, so CommonJS tools can still load Storybook.
- The install size dropped a lot, since packages no longer ship both CJS and ESM builds.

```ts
// old (CJS)
const path = require("path");
config.resolve.alias["@"] = path.resolve(__dirname, "../src");

// new (ESM)
import { fileURLToPath } from "node:url";
config.resolve.alias["@"] = fileURLToPath(new URL("../src", import.meta.url));
```

Most of this is handled by `npx storybook@latest upgrade`, but custom addons and config helpers written in CommonJS need to be converted by hand.

## 69: What is `mount` in a play function and when do you need it?

Normally the story renders first and then the play function runs. If you destructure `mount` from the context, Storybook waits and lets you decide when to render. That lets you run setup that depends on the test itself before the component appears:

```tsx
import { expect, mocked } from "storybook/test";
import { getFeatureFlags } from "../lib/flags";

export const NewCheckoutFlow: Story = {
  play: async ({ mount, userEvent }) => {
    mocked(getFeatureFlags).mockReturnValue({ newCheckout: true });

    const canvas = await mount();

    await userEvent.click(canvas.getByRole("button", { name: "Checkout" }));
    await expect(canvas.getByText("Step 1 of 2")).toBeInTheDocument();
  },
};
```

In React you can also pass a JSX element to `mount` to render something different with data created in the play function. For setup that isn't tied to one test, `beforeEach` is usually simpler.

## 70: How does the Vitest addon turn stories into tests?

The `storybookTest` Vitest plugin reads your story files and transforms each one into a test file at build time. Every story in the index becomes a test case that:

1. applies project config from `.storybook/preview` (decorators, parameters, `beforeAll`, `beforeEach`),
2. runs loaders,
3. renders the story in a real browser through Vitest browser mode (Playwright),
4. runs the play function, if there is one,
5. runs extra checks such as a11y if the addon is installed.

It uses the same "portable stories" machinery as `composeStories`, so a story behaves the same in the Storybook UI and in the test.

You can control which stories run with tags:

```ts
// vitest.config.ts (inside the storybook project)
storybookTest({
  configDir: '.storybook',
  tags: {
    include: ['test'],
    exclude: ['experimental'],
    skip: ['skip-test'],
  },
}),
```

Because tests run in a real browser, things like CSS, layout, focus and `ResizeObserver` work for real, unlike in jsdom.

## 71: Where do Storybook tests fit compared to unit tests and E2E tests?

A rough split that works for most teams:

- **Unit tests (Vitest/Jest)**: pure logic. Utils, reducers, hooks, formatters. Fast and no rendering needed.
- **Storybook tests**: components and small groups of components. Rendering, interactions, a11y and visual checks for each state. They run in a real browser but don't need the whole app or a backend.
- **E2E tests (Playwright/Cypress)**: a small number of key user flows through the real app: login, checkout, sign up. They catch problems in routing, the API and the wiring between pages.

The point is that most UI bugs live in components and their states, and Storybook tests can cover those cheaply. E2E tests stay few because they are slow and break more often. Don't write a Storybook test that just repeats a unit test, or an E2E test for something a story already covers.

## 72: Your visual tests are flaky. What are the usual causes and fixes?

Common causes:

- **Dates and times**: "3 minutes ago", today's date in a calendar. Fix by mocking the date in `beforeEach` (for example with `mockdate` or `sb.mock` on your date helper).
- **Random data**: Faker or `Math.random()` in mocks. Use fixed data or a fixed seed.
- **Animations and transitions**: the screenshot is taken mid-animation. Disable them for tests, respect `prefers-reduced-motion`, or use Chromatic's `pauseAnimationAtEnd`.
- **Fonts and images loading late**: preload fonts, use local images, and wait for them in a loader or play function.
- **Network**: real API calls. Mock everything with MSW or module mocks.
- **Non-deterministic order**: lists sorted by something not stable.

You can check `isChromatic()` (from `chromatic/isChromatic`) to turn off things like animations only in visual tests, and use `parameters.chromatic.delay` as a last resort. As a rule, if a story renders differently on reload, it will be flaky in visual tests.

## 73: How do you visually test the same story in light and dark themes and several viewports?

With Chromatic you use **modes**. A mode is a set of globals (theme, viewport, locale) that Chromatic applies before taking a snapshot. Define them once and reuse them:

```ts
// .storybook/modes.ts
// viewport names must match the viewport options in your preview config
export const allModes = {
  "light desktop": { theme: "light", viewport: "desktop" },
  "dark desktop": { theme: "dark", viewport: "desktop" },
  "light mobile": { theme: "light", viewport: "mobile1" },
};
```

```tsx
// .storybook/preview.tsx
import { allModes } from './modes';

parameters: {
  chromatic: {
    modes: {
      'light desktop': allModes['light desktop'],
      'dark desktop': allModes['dark desktop'],
    },
  },
},
```

Each mode gets its own baseline. This only works if your theme decorator reads `context.globals.theme`, so the globals setup has to be right first. Be careful with the number of modes, because each one multiplies the snapshot count and the cost.

## 74: How do you write a custom Storybook addon?

An addon usually has a manager part (UI in the Storybook interface) and sometimes a preview part (decorators or code that runs next to the stories). A simple panel that reads a parameter:

```tsx
// .storybook/addons/design-notes/manager.tsx
import React from "react";
import { addons, types, useParameter } from "storybook/manager-api";
import { AddonPanel } from "storybook/internal/components";

const ADDON_ID = "acme/design-notes";

function Notes() {
  const notes = useParameter<string>("designNotes", "No notes for this story.");
  return <div style={{ padding: 16 }}>{notes}</div>;
}

addons.register(ADDON_ID, () => {
  addons.add(`${ADDON_ID}/panel`, {
    type: types.PANEL,
    title: "Design notes",
    render: ({ active }) => (
      <AddonPanel active={!!active}>
        <Notes />
      </AddonPanel>
    ),
  });
});
```

Then a story sets `parameters: { designNotes: 'Use only in the header.' }`. For local addons you can import the file in `.storybook/manager.ts`. To publish one, start from the Addon Kit template. If the preview and manager need to talk (for example the panel shows data from the rendered component), use `useChannel` with your own event names.

## 75: In what order do decorators run, and why does it matter?

Decorators from all levels are combined. Story decorators are the innermost, then meta (component) decorators, and global decorators from `preview.ts` are the outermost. Inside one array, the first decorator is closest to the story.

```
GlobalDecorator
  MetaDecorator
    StoryDecorator
      <Component />
```

It matters when one decorator depends on another. For example, if a story-level decorator uses `useTheme()`, the `ThemeProvider` has to be in a global or meta decorator, because those wrap it from outside. If you put both in the same array in the wrong order, the inner one won't find the context.

Also note that every decorator re-renders with the story. A decorator that creates a new store or client on every render (instead of once per story) can cause lost state or extra network calls.

## 76: How do parameters merge, and how do you turn off a feature for one story?

Parameters are deep merged from preview to meta to story. Objects are merged key by key, so a story can change one nested value without repeating the rest. Arrays are not merged, they're replaced.

That makes it easy to turn features off for a single story:

```tsx
export const ThirdPartyEmbed: Story = {
  parameters: {
    a11y: { test: "off" }, // known issue in the vendor iframe
    chromatic: { disableSnapshot: true }, // content changes on every load
    layout: "fullscreen",
  },
};
```

You can also turn off a specific a11y rule instead of all of them:

```tsx
parameters: {
  a11y: {
    config: { rules: [{ id: 'color-contrast', enabled: false }] },
  },
},
```

Prefer turning off as little as possible, and leave a comment with the reason, so it doesn't stay off forever.

## 77: How would you set up Storybook for a design system in a monorepo?

Two common setups:

1. **One Storybook for the whole repo**: a single `.storybook` folder (often in its own package like `apps/storybook`) with globs that point into all packages, for example `'../../packages/*/src/**/*.stories.tsx'`. Simple, one URL, one set of tests.
2. **One Storybook per package**, combined with **Composition** (`refs`) into a main one. Each team owns its own config and builds independently, which scales better for large orgs.

Things to get right either way:

- Stories should import components the way consumers do (package name), or at least through the same entry, so you test what you ship.
- Tokens, global styles and fonts should be loaded once in the preview.
- Use the same framework and Storybook version across packages.
- Run Storybook tests and visual tests per pull request, ideally only for changed packages.
- Publish the built Storybook per release so consumers can see docs for the version they use.

## 78: What should you think about for security when publishing Storybook?

- **Everything in the build is public to whoever can open it.** Environment variables exposed to the preview, mock data and comments in source code shown in docs all end up in the static files. Don't put secrets, real customer data or internal URLs there.
- **Private components**: if your Storybook shows unreleased features, host it behind auth (Chromatic has private projects, or put it behind your SSO or a VPN).
- **Don't expose the dev server.** `storybook dev` is meant for local use. Don't run it on a public host.
- **Embedded stories**: if you embed story iframes in other sites, think about clickjacking and set headers like `Content-Security-Policy: frame-ancestors` on your hosting.
- **Addons are code you run**: third-party addons run in your build and in the browser. Treat them like any other dependency, check who maintains them and keep them updated.
- **Telemetry**: Storybook collects anonymous usage data. Turn it off if your company requires it with `core: { disableTelemetry: true }` or `STORYBOOK_DISABLE_TELEMETRY=1`.

## 79: How do you handle components with side effects like timers, localStorage or analytics?

Keep each story isolated and repeatable:

- **Storage**: seed it in `beforeEach` and clear it in the returned cleanup function, so one story doesn't change the next.
- **Timers**: for components with countdowns or debounces, mock the time instead of waiting. Mock the date for "time ago" text.
- **Analytics and logging**: mock the module (`sb.mock`) so nothing is sent from Storybook, and so you can assert that the right events fire.
- **Global listeners and subscriptions**: make sure the component cleans them up on unmount. Storybook unmounts when you switch stories, so leaks show up quickly as doubled events.

```tsx
const meta = {
  component: CookieBanner,
  beforeEach: () => {
    localStorage.removeItem("cookie-consent");
    return () => localStorage.removeItem("cookie-consent");
  },
} satisfies Meta<typeof CookieBanner>;
```

If a component is hard to isolate, that's often a sign it's doing too much and its side effects should move to a hook or service that you can mock.

## 80: Can you write stories for React Server Components?

Partly. Storybook has experimental RSC support for its Next.js frameworks. You turn it on in `main.ts`:

```ts
features: {
  experimentalRSC: true,
},
```

Storybook then renders async server components in the browser inside a `Suspense` boundary. The component code runs in the browser, not on a server, so anything that needs the server (database access, file system, secrets, `server-only` modules) has to be mocked with module mocks or MSW.

In practice many teams keep server components thin: they fetch the data and pass it to client or presentational components, and those are what get most of the stories. That gives better stories and better tests without needing the experimental flag for everything.

## 81: How do you measure test coverage from Storybook tests?

With the Vitest addon you can collect coverage from stories. Install a coverage provider (`@vitest/coverage-v8` or `@vitest/coverage-istanbul`) and either turn on coverage in the testing widget in the Storybook sidebar, or run:

```bash
npx vitest --project=storybook --coverage
```

The report shows which lines of your components are run by your stories and play functions. That's useful for spotting states nobody wrote a story for, like an error branch or a rare prop combination.

Coverage only tells you code ran, not that something checked the result. A story without a play function can give high coverage while asserting nothing except "it didn't crash". Use it to find gaps, not as a goal on its own.

## 82: A story works in the Storybook UI but fails when run with the Vitest addon in CI. How do you debug it?

Things to check, roughly in order:

1. **Read the error and run it locally** with `npx vitest --project=storybook` and the same browser. Many CI-only failures also fail locally in headless mode.
2. **Timing**: CI machines are slower. Look for `getBy*` right after an async action, missing `await` before `userEvent` or `expect`, or animations. Use `findBy*` and `waitFor`.
3. **State leaking between stories**: in the UI you usually open one story at a time, but tests run many in a row. Look for shared stores, module-level variables, storage, or mocks that aren't reset.
4. **Environment differences**: missing env variables, fonts not installed in CI, a different viewport size, timezone or locale. Set `TZ` and locale explicitly in CI if dates are involved.
5. **Network**: a request that works locally but isn't mocked, so it fails or hangs in CI.
6. **Browser not installed**: make sure CI runs `npx playwright install chromium` (with `--with-deps` on Linux).

Vitest browser mode can save screenshots on failure, which helps a lot when you can't reproduce it locally.

## 83: How would you write stories for a large component that depends on many things (store, API, router, feature flags)?

First try to split it. Move the dependencies into a container and keep a presentational component that takes plain props. The presentational part gets most of the stories, and they become simple:

```tsx
// OrderPage.tsx: container, gets data from hooks
export function OrderPage() {
  const { data, status } = useOrder(useParams().id);
  return <OrderView order={data} status={status} />;
}

// OrderView.stories.tsx: plain props, easy states
export const Shipped: Story = {
  args: { status: "success", order: mockShippedOrder },
};
```

For the container itself (or when you can't refactor), mock the dependencies at the edges:

- router and store through decorators with fresh instances per story,
- HTTP through MSW handlers per story,
- feature flags and auth through `sb.mock`,
- shared mocks in reusable decorators or `beforeEach` functions so each story file stays short.

Page-level stories with everything mocked are valuable, but keep a few of them for key screens and push most states down to smaller components.

## 84: How do you type stories correctly in TypeScript, and why is `satisfies` used?

The recommended pattern:

```tsx
import type { Meta, StoryObj } from "@storybook/react-vite";
import { Button } from "./Button";

const meta = {
  component: Button,
  args: { label: "Button" },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

// label is required on Button, but it's already set on meta,
// so TypeScript doesn't ask for it here
export const Primary: Story = {
  args: { variant: "primary" },
};
```

With `satisfies`, TypeScript checks that meta is valid but keeps its exact type, including which args were already provided. `StoryObj<typeof meta>` uses that to make those args optional in stories. If you wrote `const meta: Meta<typeof Button> = {...}`, that information would be lost and every story would need to repeat the required props.

Import types from your framework package (like `@storybook/react-vite`), not from the renderer package directly. CSF Factories go further and type addon parameters as well.

## 85: How can Storybook help AI coding agents?

Storybook already has what an agent needs to work with your UI: a list of components, their props, documented states (stories) and tests. Recent 10.x versions build on that with an MCP server (in preview, starting with React) that gives agents access to your component docs and stories and lets them run your Storybook tests.

The practical workflow is:

1. The agent looks up existing components and how they're used instead of inventing new ones.
2. It writes or updates the component and adds stories for the new states.
3. It runs the story tests (interaction, a11y) to check its own work.
4. A human reviews the result in Storybook or in the visual test diff.

The quality of this depends on your stories. Well-documented components with clear stories and tests give an agent good context. A Storybook with three outdated stories gives it nothing useful.

## 86: How do you stop a Storybook from going stale over time?

Stale Storybooks are very common. Things that help:

- **Run every story as a test in CI** (Vitest addon). A broken story then breaks the build instead of quietly staying broken.
- **Visual tests on pull requests**, so changes to components are reviewed together with their stories.
- **Type-check story files** with the rest of the code. Use `satisfies Meta<typeof Component>` so renamed or removed props fail the build.
- **Lint stories** with `eslint-plugin-storybook`.
- **Keep stories next to components** so they're edited together.
- **Make it part of "done"**: new component or new state means a new story. Add it to the pull request template.
- **Delete stories for removed components** instead of leaving them, and use a `deprecated` tag for components on the way out.

## 87: How would you design a CI pipeline around Storybook?

A setup that works well for most teams, for each pull request:

1. **Lint and type-check**, including story files.
2. **Story tests** with the Vitest addon: render every story, run play functions, run a11y checks. These are fast and catch most broken components.
3. **Build Storybook** (`storybook build`) and fail on build errors.
4. **Visual tests** with Chromatic (or similar) against the build, with TurboSnap to only snapshot affected stories.
5. **Publish a preview link** of the built Storybook on the pull request so reviewers and designers can check it.

On the main branch, accept visual baselines and deploy the Storybook to its permanent URL. Order the steps from cheapest to most expensive so failures show up early, and run independent ones in parallel.

## 88: How do you document and version a design system with Storybook?

- **Docs live next to the components**: autodocs for the API, plus MDX pages for usage guidelines, do's and don'ts, tokens and patterns.
- **Introduction and foundations pages** in MDX: colors, typography, spacing, icons. You can render tokens from the same source the code uses so they never drift.
- **Publish per version**: deploy the Storybook for each release (for example `/v3/`, `/v4/`) or rely on Chromatic's per-build URLs, so teams on older versions still have matching docs.
- **Mark status with tags**: `beta`, `deprecated` and so on, and show them in the sidebar.
- **Changelog and migration notes** in MDX for breaking changes.
- **Composition** lets product teams pull the published design system into their own Storybook.

The aim is that Storybook is the single place people go to learn how to use a component, and it's always in sync with the released code.

## 89: How do you handle internationalization and right-to-left layouts in Storybook?

Add a `locale` global with a toolbar switch, and a decorator that sets up your i18n library and the `dir` attribute:

```tsx
// .storybook/preview.tsx
const preview: Preview = {
  globalTypes: {
    locale: {
      description: "Language",
      toolbar: {
        icon: "globe",
        items: [
          { value: "en", title: "English" },
          { value: "ka", title: "Georgian" },
          { value: "ar", title: "Arabic" },
        ],
      },
    },
  },
  initialGlobals: { locale: "en" },
  decorators: [
    (Story, context) => {
      const locale = context.globals.locale;
      document.documentElement.dir = locale === "ar" ? "rtl" : "ltr";
      document.documentElement.lang = locale;
      return (
        <I18nProvider locale={locale}>
          <Story />
        </I18nProvider>
      );
    },
  ],
};
```

Then add stories (or Chromatic modes) for long translations and RTL, since those break layouts most often. Long German or Georgian words and Arabic text show overflow and alignment problems that English stories never will.

## 90: When is Storybook not worth it?

Storybook has real costs: setup and upgrades, slower CI, extra config to mock providers and data, and stories that need maintenance. It may not be worth it when:

- the app is small, has few reusable components and a small team,
- the UI is mostly server-rendered pages with little interactive component logic,
- it's a short-lived prototype,
- nobody will maintain the stories, so they'll rot and give false confidence.

It pays off most when you have a design system or shared component library, several teams or designers who need to see components, many component states to test, or a need for visual regression testing. A middle ground for smaller projects is to add stories only for shared components and the trickiest UI, instead of trying to cover everything.
