# Turbopack Interview Questions and Answers

_Last updated: November 25, 2026_

150 Turbopack interview questions with answers, split into three levels: 50 easy, 50 moderate and 50 advanced.

The answers are for Turbopack as it ships in Next.js 16 (16.4), where it is the default bundler for both `next dev` and `next build`. Older setups (the `--turbopack` flag, `experimental.turbo` config, webpack as the default) are mentioned where they still matter, since many projects still run Next.js 14 or 15.

## Table of Contents

- [Easy Questions (1-50)](#easy-questions-1-50)
- [Moderate Questions (51-100)](#moderate-questions-51-100)
- [Advanced Questions (101-150)](#advanced-questions-101-150)

### Easy Questions (1-50)

- [1: What is Turbopack?](#1-what-is-turbopack)
- [2: Why was Turbopack created when webpack already existed?](#2-why-was-turbopack-created-when-webpack-already-existed)
- [3: What language is Turbopack written in?](#3-what-language-is-turbopack-written-in)
- [4: Who maintains Turbopack and where does the code live?](#4-who-maintains-turbopack-and-where-does-the-code-live)
- [5: Is Turbopack the same thing as Turborepo?](#5-is-turbopack-the-same-thing-as-turborepo)
- [6: Can you use Turbopack outside of Next.js?](#6-can-you-use-turbopack-outside-of-nextjs)
- [7: How do you start the Next.js dev server with Turbopack?](#7-how-do-you-start-the-nextjs-dev-server-with-turbopack)
- [8: Is Turbopack used for production builds?](#8-is-turbopack-used-for-production-builds)
- [9: How do you switch back to webpack in Next.js 16?](#9-how-do-you-switch-back-to-webpack-in-nextjs-16)
- [10: What does "incremental computation" mean in Turbopack?](#10-what-does-incremental-computation-mean-in-turbopack)
- [11: What does it mean that Turbopack bundles lazily in development?](#11-what-does-it-mean-that-turbopack-bundles-lazily-in-development)
- [12: What is Fast Refresh and does Turbopack support it?](#12-what-is-fast-refresh-and-does-turbopack-support-it)
- [13: What is HMR?](#13-what-is-hmr)
- [14: Does Turbopack support TypeScript?](#14-does-turbopack-support-typescript)
- [15: Does Turbopack type-check your TypeScript code?](#15-does-turbopack-type-check-your-typescript-code)
- [16: Which JavaScript module formats does Turbopack understand?](#16-which-javascript-module-formats-does-turbopack-understand)
- [17: Does Turbopack support JSX?](#17-does-turbopack-support-jsx)
- [18: What is SWC and how is it related to Turbopack?](#18-what-is-swc-and-how-is-it-related-to-turbopack)
- [19: Does Turbopack support CSS out of the box?](#19-does-turbopack-support-css-out-of-the-box)
- [20: What is Lightning CSS?](#20-what-is-lightning-css)
- [21: How do you use a CSS Module with Turbopack?](#21-how-do-you-use-a-css-module-with-turbopack)
- [22: Does Turbopack support Sass?](#22-does-turbopack-support-sass)
- [23: Does Turbopack support Less?](#23-does-turbopack-support-less)
- [24: Does Turbopack support PostCSS and Tailwind CSS?](#24-does-turbopack-support-postcss-and-tailwind-css)
- [25: Where do you configure Turbopack in a Next.js project?](#25-where-do-you-configure-turbopack-in-a-nextjs-project)
- [26: What was experimental.turbo?](#26-what-was-experimentalturbo)
- [27: What does the turbopack.rules option do?](#27-what-does-the-turbopackrules-option-do)
- [28: What does the turbopack.resolveAlias option do?](#28-what-does-the-turbopackresolvealias-option-do)
- [29: What does the turbopack.resolveExtensions option do?](#29-what-does-the-turbopackresolveextensions-option-do)
- [30: Does Turbopack support webpack plugins?](#30-does-turbopack-support-webpack-plugins)
- [31: Does Turbopack support webpack loaders?](#31-does-turbopack-support-webpack-loaders)
- [32: What happens to the webpack() function in next.config.js when you use Turbopack?](#32-what-happens-to-the-webpack-function-in-nextconfigjs-when-you-use-turbopack)
- [33: What is a module graph?](#33-what-is-a-module-graph)
- [34: What is a chunk?](#34-what-is-a-chunk)
- [35: What is code splitting and how do you get it with Turbopack?](#35-what-is-code-splitting-and-how-do-you-get-it-with-turbopack)
- [36: What is tree shaking?](#36-what-is-tree-shaking)
- [37: Does Turbopack minify code in production?](#37-does-turbopack-minify-code-in-production)
- [38: Does Turbopack support source maps?](#38-does-turbopack-support-source-maps)
- [39: Can you use environment variables with Turbopack?](#39-can-you-use-environment-variables-with-turbopack)
- [40: Does Turbopack support import.meta.env?](#40-does-turbopack-support-importmetaenv)
- [41: Can you import images and other static files with Turbopack?](#41-can-you-import-images-and-other-static-files-with-turbopack)
- [42: Can you import JSON files with Turbopack?](#42-can-you-import-json-files-with-turbopack)
- [43: Which operating systems does Turbopack support?](#43-which-operating-systems-does-turbopack-support)
- [44: Is Turbopack faster than webpack?](#44-is-turbopack-faster-than-webpack)
- [45: What is the filesystem cache in Turbopack?](#45-what-is-the-filesystem-cache-in-turbopack)
- [46: How do you clear the Turbopack cache?](#46-how-do-you-clear-the-turbopack-cache)
- [47: What is the turbopack.root option?](#47-what-is-the-turbopackroot-option)
- [48: Does Turbopack need Babel?](#48-does-turbopack-need-babel)
- [49: Does Turbopack work with React Server Components?](#49-does-turbopack-work-with-react-server-components)
- [50: How do you check that your app is actually using Turbopack?](#50-how-do-you-check-that-your-app-is-actually-using-turbopack)

### Moderate Questions (51-100)

- [51: How do you pass options to a webpack loader in turbopack.rules?](#51-how-do-you-pass-options-to-a-webpack-loader-in-turbopackrules)
- [52: How do glob patterns in turbopack.rules match files?](#52-how-do-glob-patterns-in-turbopackrules-match-files)
- [53: What is the condition field in turbopack.rules?](#53-what-is-the-condition-field-in-turbopackrules)
- [54: What does the foreign condition mean?](#54-what-does-the-foreign-condition-mean)
- [55: How do you run a loader only on files that contain certain text?](#55-how-do-you-run-a-loader-only-on-files-that-contain-certain-text)
- [56: What is the type field in a Turbopack rule?](#56-what-is-the-type-field-in-a-turbopack-rule)
- [57: What is the difference between as and type in a rule?](#57-what-is-the-difference-between-as-and-type-in-a-rule)
- [58: How do you set up SVG imports as React components with Turbopack?](#58-how-do-you-set-up-svg-imports-as-react-components-with-turbopack)
- [59: Can you use MDX with Turbopack?](#59-can-you-use-mdx-with-turbopack)
- [60: How do you use resolveAlias with the browser condition?](#60-how-do-you-use-resolvealias-with-the-browser-condition)
- [61: How do you replace a Node.js module that breaks in the browser?](#61-how-do-you-replace-a-nodejs-module-that-breaks-in-the-browser)
- [62: How does Turbopack handle tsconfig paths?](#62-how-does-turbopack-handle-tsconfig-paths)
- [63: How do you handle the Sass tilde import syntax with Turbopack?](#63-how-do-you-handle-the-sass-tilde-import-syntax-with-turbopack)
- [64: How do you configure Turbopack in a monorepo?](#64-how-do-you-configure-turbopack-in-a-monorepo)
- [65: Why does Turbopack fail to resolve a package that is linked from outside the project?](#65-why-does-turbopack-fail-to-resolve-a-package-that-is-linked-from-outside-the-project)
- [66: What does transpilePackages do with Turbopack?](#66-what-does-transpilepackages-do-with-turbopack)
- [67: What does serverExternalPackages do?](#67-what-does-serverexternalpackages-do)
- [68: What magic comments does Turbopack support?](#68-what-magic-comments-does-turbopack-support)
- [69: What does turbopackIgnore do and when would you use it?](#69-what-does-turbopackignore-do-and-when-would-you-use-it)
- [70: What is import.meta.glob in Turbopack?](#70-what-is-importmetaglob-in-turbopack)
- [71: How does CSS ordering differ between Turbopack and webpack?](#71-how-does-css-ordering-differ-between-turbopack-and-webpack)
- [72: Which CSS Modules features from webpack's css-loader are not supported?](#72-which-css-modules-features-from-webpacks-css-loader-are-not-supported)
- [73: Why might decimal numbers in your CSS look different after switching to Turbopack?](#73-why-might-decimal-numbers-in-your-css-look-different-after-switching-to-turbopack)
- [74: How does Babel work with Turbopack?](#74-how-does-babel-work-with-turbopack)
- [75: How do you enable styled-components support with Turbopack?](#75-how-do-you-enable-styled-components-support-with-turbopack)
- [76: How do you use Web Workers with Turbopack?](#76-how-do-you-use-web-workers-with-turbopack)
- [77: How do you import a WebAssembly file with Turbopack?](#77-how-do-you-import-a-webassembly-file-with-turbopack)
- [78: How do you speed up CI builds with the Turbopack build cache?](#78-how-do-you-speed-up-ci-builds-with-the-turbopack-build-cache)
- [79: How do you turn off the Turbopack filesystem cache?](#79-how-do-you-turn-off-the-turbopack-filesystem-cache)
- [80: How do you migrate a next.config.js from webpack to Turbopack?](#80-how-do-you-migrate-a-nextconfigjs-from-webpack-to-turbopack)
- [81: How do you replace webpack's DefinePlugin in a Turbopack project?](#81-how-do-you-replace-webpacks-defineplugin-in-a-turbopack-project)
- [82: Why does Fast Refresh sometimes do a full reload instead of a hot update?](#82-why-does-fast-refresh-sometimes-do-a-full-reload-instead-of-a-hot-update)
- [83: How do you collect a trace to report a Turbopack performance problem?](#83-how-do-you-collect-a-trace-to-report-a-turbopack-performance-problem)
- [84: How do you analyze bundle size with Turbopack?](#84-how-do-you-analyze-bundle-size-with-turbopack)
- [85: What do the development and production conditions do in rules?](#85-what-do-the-development-and-production-conditions-do-in-rules)
- [86: How do you write a simple custom loader for Turbopack?](#86-how-do-you-write-a-simple-custom-loader-for-turbopack)
- [87: How do you load a YAML file with Turbopack?](#87-how-do-you-load-a-yaml-file-with-turbopack)
- [88: How do you import GraphQL files with Turbopack?](#88-how-do-you-import-graphql-files-with-turbopack)
- [89: How is Turbopack different from Vite in development?](#89-how-is-turbopack-different-from-vite-in-development)
- [90: How is Turbopack different from Rspack?](#90-how-is-turbopack-different-from-rspack)
- [91: What does the ignoreIssue option do?](#91-what-does-the-ignoreissue-option-do)
- [92: Why do you get "Module not found" errors after switching to Turbopack?](#92-why-do-you-get-module-not-found-errors-after-switching-to-turbopack)
- [93: What is a client boundary in Turbopack's graph?](#93-what-is-a-client-boundary-in-turbopacks-graph)
- [94: Why might a package work with webpack but break with Turbopack?](#94-why-might-a-package-work-with-webpack-but-break-with-turbopack)
- [95: Does Turbopack support require.context?](#95-does-turbopack-support-requirecontext)
- [96: What changed in Turbopack in Next.js 16.3?](#96-what-changed-in-turbopack-in-nextjs-163)
- [97: How does Turbopack handle environment-specific code like if (process.env.NODE_ENV === 'production')?](#97-how-does-turbopack-handle-environment-specific-code-like-if-processenvnode_env--production)
- [98: How do you enable the React Compiler with Turbopack?](#98-how-do-you-enable-the-react-compiler-with-turbopack)
- [99: What should you check if Turbopack dev uses too much memory?](#99-what-should-you-check-if-turbopack-dev-uses-too-much-memory)
- [100: Should you keep a webpack fallback after moving to Turbopack?](#100-should-you-keep-a-webpack-fallback-after-moving-to-turbopack)

### Advanced Questions (101-150)

- [101: How does Turbopack's incremental engine work at a high level?](#101-how-does-turbopacks-incremental-engine-work-at-a-high-level)
- [102: What is function-level caching and why does it matter?](#102-what-is-function-level-caching-and-why-does-it-matter)
- [103: Why does a change sometimes stop spreading early in Turbopack's graph?](#103-why-does-a-change-sometimes-stop-spreading-early-in-turbopacks-graph)
- [104: What are value cells (Vc) in Turbopack's code?](#104-what-are-value-cells-vc-in-turbopacks-code)
- [105: Why does Turbopack use one module graph for client and server?](#105-why-does-turbopack-use-one-module-graph-for-client-and-server)
- [106: How does the same file get compiled differently for client and server in one graph?](#106-how-does-the-same-file-get-compiled-differently-for-client-and-server-in-one-graph)
- [107: Why does Turbopack bundle in dev instead of serving unbundled ES modules like Vite?](#107-why-does-turbopack-bundle-in-dev-instead-of-serving-unbundled-es-modules-like-vite)
- [108: How does lazy compilation in dev interact with the filesystem cache?](#108-how-does-lazy-compilation-in-dev-interact-with-the-filesystem-cache)
- [109: How does Turbopack know a cached result on disk is still valid after a restart?](#109-how-does-turbopack-know-a-cached-result-on-disk-is-still-valid-after-a-restart)
- [110: What can cause a stale or broken filesystem cache and how do you handle it?](#110-what-can-cause-a-stale-or-broken-filesystem-cache-and-how-do-you-handle-it)
- [111: Why must loader options be serializable in Turbopack?](#111-why-must-loader-options-be-serializable-in-turbopack)
- [112: How does Turbopack run JavaScript loaders from Rust?](#112-how-does-turbopack-run-javascript-loaders-from-rust)
- [113: Why are some parts of the webpack loader API not supported?](#113-why-are-some-parts-of-the-webpack-loader-api-not-supported)
- [114: Why will Turbopack never support webpack plugins?](#114-why-will-turbopack-never-support-webpack-plugins)
- [115: Why doesn't Turbopack support Yarn Plug'n'Play?](#115-why-doesnt-turbopack-support-yarn-plugnplay)
- [116: How are module IDs handled in dev versus production?](#116-how-are-module-ids-handled-in-dev-versus-production)
- [117: How do content hashes in chunk file names help caching?](#117-how-do-content-hashes-in-chunk-file-names-help-caching)
- [118: What is scope hoisting and does Turbopack do it?](#118-what-is-scope-hoisting-and-does-turbopack-do-it)
- [119: How does Turbopack do tree shaking at a finer level than whole modules?](#119-how-does-turbopack-do-tree-shaking-at-a-finer-level-than-whole-modules)
- [120: What are side effects and why do they matter for tree shaking?](#120-what-are-side-effects-and-why-do-they-matter-for-tree-shaking)
- [121: Why are barrel files bad for bundler performance and how does Next.js help?](#121-why-are-barrel-files-bad-for-bundler-performance-and-how-does-nextjs-help)
- [122: How does Turbopack handle package.json exports and conditions?](#122-how-does-turbopack-handle-packagejson-exports-and-conditions)
- [123: What is the dual package hazard and how can it show up with Turbopack?](#123-what-is-the-dual-package-hazard-and-how-can-it-show-up-with-turbopack)
- [124: How does HMR work under the hood with Turbopack?](#124-how-does-hmr-work-under-the-hood-with-turbopack)
- [125: How are server-side changes picked up in dev?](#125-how-are-server-side-changes-picked-up-in-dev)
- [126: What does turbopackMemoryEviction do?](#126-what-does-turbopackmemoryeviction-do)
- [127: What is the trade-off of turning off the dev filesystem cache?](#127-what-is-the-trade-off-of-turning-off-the-dev-filesystem-cache)
- [128: How would you debug a production bug that only happens with Turbopack, not webpack?](#128-how-would-you-debug-a-production-bug-that-only-happens-with-turbopack-not-webpack)
- [129: What are debug IDs and why are they useful?](#129-what-are-debug-ids-and-why-are-they-useful)
- [130: What security issues should you think about with Turbopack builds?](#130-what-security-issues-should-you-think-about-with-turbopack-builds)
- [131: How does the server-only package protect you at build time?](#131-how-does-the-server-only-package-protect-you-at-build-time)
- [132: Why does Turbopack limit resolution and watching to the root?](#132-why-does-turbopack-limit-resolution-and-watching-to-the-root)
- [133: How would you migrate a large app with a heavy custom webpack config to Turbopack?](#133-how-would-you-migrate-a-large-app-with-a-heavy-custom-webpack-config-to-turbopack)
- [134: How can you replace a webpack plugin that generated a file at build time?](#134-how-can-you-replace-a-webpack-plugin-that-generated-a-file-at-build-time)
- [135: What happens when a loader is slow and runs on many files?](#135-what-happens-when-a-loader-is-slow-and-runs-on-many-files)
- [136: How do you handle a library that ships a Babel plugin required for it to work?](#136-how-do-you-handle-a-library-that-ships-a-babel-plugin-required-for-it-to-work)
- [137: How does the Edge runtime affect what Turbopack can bundle?](#137-how-does-the-edge-runtime-affect-what-turbopack-can-bundle)
- [138: Why did the Next.js team make Turbopack the default in 16 instead of keeping it opt-in?](#138-why-did-the-nextjs-team-make-turbopack-the-default-in-16-instead-of-keeping-it-opt-in)
- [139: How would you prove that Turbopack actually made your team faster?](#139-how-would-you-prove-that-turbopack-actually-made-your-team-faster)
- [140: How does Turbopack's design compare to incremental builds in webpack 5's persistent cache?](#140-how-does-turbopacks-design-compare-to-incremental-builds-in-webpack-5s-persistent-cache)
- [141: What is the downside of fine-grained incremental computation?](#141-what-is-the-downside-of-fine-grained-incremental-computation)
- [142: Why might a dynamic import with a variable path cause problems?](#142-why-might-a-dynamic-import-with-a-variable-path-cause-problems)
- [143: How does Turbopack handle CommonJS interop edge cases?](#143-how-does-turbopack-handle-commonjs-interop-edge-cases)
- [144: What is the role of the Turbopack runtime in the browser?](#144-what-is-the-role-of-the-turbopack-runtime-in-the-browser)
- [145: Why are minification and source maps handled differently in dev?](#145-why-are-minification-and-source-maps-handled-differently-in-dev)
- [146: How should you handle a third-party package that reads its own files with fs at runtime on the server?](#146-how-should-you-handle-a-third-party-package-that-reads-its-own-files-with-fs-at-runtime-on-the-server)
- [147: Scenario: HMR became slow after adding a new library. How do you investigate?](#147-scenario-hmr-became-slow-after-adding-a-new-library-how-do-you-investigate)
- [148: Scenario: the build passes locally but fails in CI with Turbopack. What do you check?](#148-scenario-the-build-passes-locally-but-fails-in-ci-with-turbopack-what-do-you-check)
- [149: When would you still choose webpack for a Next.js project today?](#149-when-would-you-still-choose-webpack-for-a-nextjs-project-today)
- [150: What are the main limits of Turbopack today that you should know before adopting it?](#150-what-are-the-main-limits-of-turbopack-today-that-you-should-know-before-adopting-it)

---

# Easy Questions (1-50)

## 1: What is Turbopack?

Turbopack is a bundler written in Rust, made by Vercel. It takes your JavaScript, TypeScript, CSS and other files, follows the imports between them, and turns them into the bundles the browser and server need. It is built into Next.js and is the default bundler there since Next.js 16. Its main goal is speed, especially fast startup and fast updates while you are coding.

## 2: Why was Turbopack created when webpack already existed?

Webpack is written in JavaScript and was designed before today's large apps with thousands of modules. On big Next.js apps, dev server startup and Fast Refresh got slow. Turbopack was written from scratch in Rust with incremental computation at its core, so it only redoes the work that changed. Vercel built it so Next.js could stay fast as apps grow.

## 3: What language is Turbopack written in?

Turbopack is written in Rust. It uses SWC (also written in Rust) to parse and transform JavaScript and TypeScript, and Lightning CSS for CSS. Using a compiled language with real multi-threading is a big part of why it is faster than JavaScript-based bundlers.

## 4: Who maintains Turbopack and where does the code live?

Vercel maintains it, together with the Next.js team. The source code lives inside the `vercel/next.js` repository on GitHub, in the `turbopack/` folder. It used to live in the `vercel/turborepo` repository and was moved later to sit next to the Next.js code that uses it.

## 5: Is Turbopack the same thing as Turborepo?

No. Both come from Vercel and have similar names, but they solve different problems. Turborepo is a build system for monorepos: it runs tasks like `build` and `test` across packages and caches their results. Turbopack is a bundler that turns your app's source files into bundles. You can use them together, for example Turborepo running `next build` that uses Turbopack inside.

## 6: Can you use Turbopack outside of Next.js?

Not in a supported way today. Turbopack is shipped as part of Next.js and the documented way to use it is through `next dev` and `next build`. There is no official standalone CLI or npm package you can point at any project, like you can with Vite or webpack. A general-purpose version has been talked about, but the current focus is Next.js.

## 7: How do you start the Next.js dev server with Turbopack?

In Next.js 16 you don't need to do anything special. `next dev` uses Turbopack by default.

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

In Next.js 15 you had to opt in with `next dev --turbopack` (or the older `--turbo` flag in Next.js 14).

## 8: Is Turbopack used for production builds?

Yes, in Next.js 16 `next build` uses Turbopack by default. Production builds were experimental in 15.3, beta in 15.5, and became stable and default in 16.0. Before that, Turbopack was only used for the dev server and production builds still went through webpack.

## 9: How do you switch back to webpack in Next.js 16?

Add the `--webpack` flag to the commands in `package.json`:

```json
{
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack"
  }
}
```

This is useful when you depend on a webpack plugin or a custom `webpack()` config that Turbopack does not support.

## 10: What does "incremental computation" mean in Turbopack?

It means Turbopack splits the work into many small functions and remembers the result of each one. When a file changes, it figures out which results depend on that file and recomputes only those. Everything else comes from the cache. So editing one component does not rebuild the whole app, only the small part of the graph that is affected.

## 11: What does it mean that Turbopack bundles lazily in development?

In dev, Turbopack only compiles what the dev server is actually asked for. If you open `/dashboard`, it builds the code for that route and its imports, not every page in the app. Other routes get compiled the first time you visit them. This keeps startup fast even in apps with hundreds of routes.

## 12: What is Fast Refresh and does Turbopack support it?

Fast Refresh is React's hot reloading: when you save a component file, the change shows up in the browser in a moment and the component state is kept when possible. Turbopack supports Fast Refresh out of the box. Because it only recompiles the changed module and what depends on it, updates stay fast even in large apps.

## 13: What is HMR?

HMR stands for Hot Module Replacement. It is the mechanism that swaps an updated module into a running app without a full page reload. Turbopack's dev server sends updates to the browser over a WebSocket connection, and the runtime replaces the changed modules. Fast Refresh in React is built on top of HMR.

## 14: Does Turbopack support TypeScript?

Yes, with no setup. Turbopack strips TypeScript types using SWC, so `.ts` and `.tsx` files just work. It also reads `paths` and `baseUrl` from `tsconfig.json` to resolve aliases like `@/components/Button`. Keep in mind it does not type-check your code. You still need `tsc` or your editor for that.

## 15: Does Turbopack type-check your TypeScript code?

No. Turbopack only removes the types so the code can run, which is why it is fast. Type errors will not stop the dev server. Run `tsc --noEmit` in CI or rely on your editor to catch type errors. `next build` runs its own type-check step separately, unless you turn it off with `typescript.ignoreBuildErrors`.

## 16: Which JavaScript module formats does Turbopack understand?

It handles ES modules (`import`/`export`) and CommonJS (`require`/`module.exports`), and you can mix them in the same project. It also supports dynamic `import()` for code splitting. AMD is only partly supported. ES modules are preferred because they allow better tree shaking.

## 17: Does Turbopack support JSX?

Yes. `.jsx` and `.tsx` files are compiled with SWC, and React's automatic JSX runtime is set up for you by Next.js. You don't need Babel or any extra config to write JSX.

## 18: What is SWC and how is it related to Turbopack?

SWC (Speedy Web Compiler) is a Rust-based JavaScript and TypeScript compiler. Turbopack uses it to parse files, strip types, compile JSX and apply other transforms. You can think of SWC as the part that understands a single file, and Turbopack as the part that connects all the files together into bundles.

## 19: Does Turbopack support CSS out of the box?

Yes. Global CSS, CSS Modules (`.module.css`), CSS nesting and `@import` all work without extra setup. Turbopack uses Lightning CSS to parse, transform and minify CSS. In Next.js the usual rules still apply, for example global CSS is imported from the root layout.

## 20: What is Lightning CSS?

Lightning CSS is a fast CSS parser, transformer and minifier written in Rust, made by the Parcel team. Turbopack uses it for all CSS work: handling CSS Modules, lowering modern syntax for older browsers, and minifying. It is much faster than doing the same work in JavaScript.

## 21: How do you use a CSS Module with Turbopack?

The same way as in any Next.js app. Name the file `*.module.css` and import it as an object:

```css
/* Button.module.css */
.primary {
  background: #0070f3;
  color: white;
}
```

```jsx
import styles from "./Button.module.css";

export function Button({ children }) {
  return <button className={styles.primary}>{children}</button>;
}
```

Turbopack turns `primary` into a unique class name so it doesn't clash with other files.

## 22: Does Turbopack support Sass?

Yes. In Next.js, `.scss` and `.sass` files work out of the box once you install the `sass` package. CSS Modules work with Sass too, using `.module.scss`. One thing that is not supported is custom Sass functions passed through `sassOptions.functions`.

## 23: Does Turbopack support Less?

Not by default. There is no built-in Less support. If you need it, you can try adding `less-loader` through `turbopack.rules`, but stylesheet loaders are not officially supported, so many teams move off Less or keep using webpack for those projects.

## 24: Does Turbopack support PostCSS and Tailwind CSS?

Yes. If your project has a PostCSS config file (for example `postcss.config.mjs`), Turbopack finds it and runs PostCSS on your CSS. That is how Tailwind CSS works too, through the `@tailwindcss/postcss` plugin. PostCSS runs in a pool of Node.js workers because the plugins are JavaScript.

## 25: Where do you configure Turbopack in a Next.js project?

In `next.config.js` (or `next.config.ts`) under the top-level `turbopack` key:

```js
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  turbopack: {
    resolveAlias: {
      underscore: "lodash",
    },
  },
};

module.exports = nextConfig;
```

Before Next.js 15.3 this config lived under `experimental.turbo`.

## 26: What was experimental.turbo?

It was the old place for Turbopack options in `next.config.js`, used from Next.js 13 to 15.2. In 15.3 it was renamed to the top-level `turbopack` key. The old name still works as an alias, but you should migrate. There is a codemod for it:

```bash
npx @next/codemod@latest next-experimental-turbo-to-turbopack .
```

## 27: What does the turbopack.rules option do?

It lets you run webpack loaders on certain files. You match files with a glob and list the loaders to apply. A common example is turning SVG files into React components:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.svg": {
        loaders: ["@svgr/webpack"],
        as: "*.js",
      },
    },
  },
};
```

The `as` field tells Turbopack to treat the loader output as a JavaScript file.

## 28: What does the turbopack.resolveAlias option do?

It maps one import path to another, like `resolve.alias` in webpack. For example, you can make every import of `underscore` load `lodash` instead:

```js
module.exports = {
  turbopack: {
    resolveAlias: {
      underscore: "lodash",
    },
  },
};
```

For simple path aliases like `@/`, it is usually better to use `paths` in `tsconfig.json`, which Turbopack already understands.

## 29: What does the turbopack.resolveExtensions option do?

It sets which file extensions Turbopack tries when an import has no extension, like `import x from './utils'`. The defaults are `.tsx`, `.ts`, `.jsx`, `.js`, `.mjs` and `.json`. If you set this option, it replaces the defaults, so you have to list them again:

```js
module.exports = {
  turbopack: {
    resolveExtensions: [".mdx", ".tsx", ".ts", ".jsx", ".js", ".mjs", ".json"],
  },
};
```

## 30: Does Turbopack support webpack plugins?

No. Webpack plugins hook deep into webpack's internals (its compiler and compilation objects), and Turbopack has a completely different architecture, so they can't run. Turbopack does support many webpack loaders through `turbopack.rules`. If a project relies on a webpack plugin, you need to find another way to do the same thing or keep using `--webpack`.

## 31: Does Turbopack support webpack loaders?

Yes, a subset. Loaders like `@svgr/webpack`, `babel-loader`, `yaml-loader`, `raw-loader`, `svg-inline-loader`, `string-replace-loader` and `graphql-tag/loader` are tested. Loaders must return JavaScript, and their options must be plain values that can be serialized. Loaders that produce CSS or transform images are not supported.

## 32: What happens to the webpack() function in next.config.js when you use Turbopack?

Turbopack does not run it. The `webpack(config)` callback only changes webpack's config object, and Turbopack does not use that object. In Next.js 16, `next build` fails on purpose when it finds a custom webpack config, so you don't ship a build that quietly skipped your changes. To fix it, move what the callback does into `turbopack` options (for example `rules` or `resolveAlias`), or keep webpack with `next build --webpack`.

## 33: What is a module graph?

The module graph is the map of all files in the app and the imports between them. The bundler starts from entry points (in Next.js these are pages, layouts and route handlers), follows each import, and builds this graph. Turbopack builds one graph that covers client, server and edge code together, then uses it to create chunks.

## 34: What is a chunk?

A chunk is one output file the bundler creates, containing one or more modules. Instead of shipping your whole app as one big file, Turbopack splits it into chunks so the browser only downloads what the current page needs. Shared code can go into shared chunks so it is downloaded once and cached.

## 35: What is code splitting and how do you get it with Turbopack?

Code splitting means breaking the app into smaller pieces that load on demand. In Next.js, each route is already split automatically. You can split further with dynamic imports:

```jsx
import dynamic from "next/dynamic";

const Chart = dynamic(() => import("./Chart"), { ssr: false });

export default function Page() {
  return <Chart />;
}
```

Turbopack puts `Chart` and its imports into a separate chunk that loads only when needed.

## 36: What is tree shaking?

Tree shaking is removing code that is exported but never used. If you import one function from a utility file, the other functions should not end up in the bundle. Turbopack does tree shaking in production builds and works best with ES modules, since their imports and exports can be read without running the code.

## 37: Does Turbopack minify code in production?

Yes. `next build` with Turbopack minifies JavaScript with SWC and CSS with Lightning CSS. In development, minification is off so builds are faster and the code is easier to debug.

## 38: Does Turbopack support source maps?

Yes. In development you get source maps by default, so stack traces and browser DevTools point to your original files. For production, Next.js controls browser source maps with `productionBrowserSourceMaps` in `next.config.js`, which is off by default.

## 39: Can you use environment variables with Turbopack?

Yes, the usual Next.js rules apply. Variables from `.env` files are loaded, and only those starting with `NEXT_PUBLIC_` are inlined into client code. Server code can read any `process.env` value at runtime.

```js
// works in client components
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
```

## 40: Does Turbopack support import.meta.env?

Yes. Turbopack supports `import.meta.env.DEV`, `import.meta.env.PROD`, `import.meta.env.MODE`, `import.meta.env.BASE_URL` and `import.meta.env.SSR`, similar to Vite. This helps when you share code with a Vite project. In a Next.js-only codebase, `process.env.NODE_ENV` is still more common.

## 41: Can you import images and other static files with Turbopack?

Yes. Importing an image gives you an object you can pass to `next/image`, with the width and height filled in:

```jsx
import Image from "next/image";
import logo from "./logo.png";

export default function Header() {
  return <Image src={logo} alt="Logo" />;
}
```

Files in the `public/` folder are served as-is and you reference them by URL, like `/favicon.ico`.

## 42: Can you import JSON files with Turbopack?

Yes. JSON imports work without config:

```js
import data from "./countries.json";

console.log(data.length);
```

The file is parsed at build time and included in the bundle, so avoid importing very large JSON files into client code.

## 43: Which operating systems does Turbopack support?

It runs on macOS, Windows and Linux (both glibc and musl), on x64 and ARM64. On platforms where Next.js has no native binary, like FreeBSD, Next.js falls back to a WASM build of SWC, and that fallback does not support Turbopack, so you have to use `--webpack` there.

## 44: Is Turbopack faster than webpack?

In most Next.js apps, yes, and by a lot. Vercel reports much faster dev server startup and Fast Refresh, and faster production builds, especially in large apps. The exact gain depends on the project. The speed comes from Rust, parallel work, lazy bundling in dev and caching at a very fine level.

## 45: What is the filesystem cache in Turbopack?

Turbopack saves its computed results to disk so it doesn't start from zero next time. When you restart `next dev` or run `next build` again, most of the work is loaded from the cache. In Next.js 16.1 this became the default for dev, and in 16.3 for builds. The dev cache is in `.next/dev/cache/turbopack` and the build cache in `.next/cache/turbopack`.

## 46: How do you clear the Turbopack cache?

Stop the dev server and delete the `.next` folder:

```bash
rm -rf .next
```

This removes both the dev and the build cache. It is a common first step when something looks broken after an upgrade or a big config change.

## 47: What is the turbopack.root option?

It tells Turbopack the top folder of your project. Turbopack only resolves and watches files inside the root. It is detected automatically by looking for a lockfile (like `package-lock.json` or `pnpm-lock.yaml`). You set it by hand in monorepos when the detection picks the wrong folder:

```js
const path = require("path");

module.exports = {
  turbopack: {
    root: path.join(__dirname, ".."),
  },
};
```

## 48: Does Turbopack need Babel?

No. SWC handles everything Babel usually does in a Next.js app, and it is much faster. If your project has a Babel config file (like `.babelrc` or `babel.config.js`), Turbopack sees it and runs `babel-loader` automatically, but this slows things down. Only keep Babel if you need a plugin that has no SWC version.

## 49: Does Turbopack work with React Server Components?

Yes. React Server Components are one of the main reasons Turbopack builds a single graph for client and server. It understands the `'use client'` and `'use server'` directives and splits code into server and client parts correctly. It works with the App Router and the Pages Router.

## 50: How do you check that your app is actually using Turbopack?

When you run `next dev` or `next build`, Next.js prints the bundler in the first lines of output, for example `▲ Next.js 16.x (Turbopack)`. If you see "webpack" instead, check your scripts for a `--webpack` flag. In Next.js 15 you would check for `--turbopack` in the `dev` script.

# Moderate Questions (51-100)

## 51: How do you pass options to a webpack loader in turbopack.rules?

Use an object with `loader` and `options` instead of a plain string:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.svg": {
        loaders: [
          {
            loader: "@svgr/webpack",
            options: { icon: true },
          },
        ],
        as: "*.js",
      },
    },
  },
};
```

The options must be plain JSON-like values (strings, numbers, booleans, arrays, objects). You can't pass functions or plugin instances created with `require()`, because Turbopack sends the options to a separate Node.js process that runs the loader.

## 52: How do glob patterns in turbopack.rules match files?

A glob without a `/` matches only the file name, so `'*.svg'` matches any SVG anywhere in the project. A glob with a `/` matches the path relative to the project, for example `'./src/icons/*.svg'`. If more than one rule matches a file, they all run, in the order they are listed.

## 53: What is the condition field in turbopack.rules?

It lets you apply a rule only when extra conditions are true, beyond the glob. You can use built-in conditions like `browser`, `node`, `foreign`, `development` and `production`, or match on `path`, `content`, `query` or `contentType`. You can combine them with `all`, `any` and `not`:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.svg": {
        condition: { not: "foreign" },
        loaders: ["@svgr/webpack"],
        as: "*.js",
      },
    },
  },
};
```

This runs SVGR only on your own SVG files and leaves the ones in `node_modules` alone. Conditions were added in Next.js 16.0.

## 54: What does the foreign condition mean?

`foreign` is true for code in `node_modules` (and some Next.js internal code). It is useful when you want a loader to run only on your own source, which is faster and avoids breaking packages that already ship ready-to-use files. Use `{ not: 'foreign' }` for "my code only".

## 55: How do you run a loader only on files that contain certain text?

Use the `content` condition with a regular expression. Turbopack reads the file and runs the rule only if the content matches:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.js": {
        condition: { content: /__BUILD_TIME__/ },
        loaders: [
          {
            loader: "string-replace-loader",
            options: { search: "__BUILD_TIME__", replace: "2026-11-25" },
          },
        ],
      },
    },
  },
};
```

This keeps the loader from running on every JavaScript file in the project.

## 56: What is the type field in a Turbopack rule?

It tells Turbopack what kind of module the file is, without needing a loader. Values include `asset`, `ecmascript`, `typescript`, `css`, `css-module`, `json`, `wasm`, `text`, `raw` and `bytes`. For example, you can import `.txt` files as strings:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.txt": { type: "text" },
    },
  },
};
```

`type` was added in Next.js 16.2. Before that you needed `raw-loader` for this.

## 57: What is the difference between as and type in a rule?

`as` renames the result of the loaders so Turbopack processes it as another file type, for example `as: '*.js'` after SVGR outputs JavaScript. `type` sets the module type directly, for example `type: 'text'` to get a file's content as a string. Use `as` when a loader produces code, and `type` when you only want Turbopack to treat a file in a built-in way.

## 58: How do you set up SVG imports as React components with Turbopack?

Install `@svgr/webpack` and add a rule:

```js
// next.config.js
module.exports = {
  turbopack: {
    rules: {
      "*.svg": {
        loaders: ["@svgr/webpack"],
        as: "*.js",
      },
    },
  },
};
```

```jsx
import Logo from "./logo.svg";

export function Header() {
  return <Logo width={120} />;
}
```

Note that with this rule every SVG import becomes a component, so `next/image` with a static SVG import won't work the same way. Use a `condition` or a separate folder if you need both.

## 59: Can you use MDX with Turbopack?

Yes, through `@next/mdx`, which supports Turbopack. The catch is that remark and rehype plugins must be passed by name as strings, not as imported functions, because loader options have to be serializable:

```js
// next.config.mjs
import createMDX from "@next/mdx";

const withMDX = createMDX({
  options: {
    remarkPlugins: ["remark-gfm"],
    rehypePlugins: [],
  },
});

export default withMDX({
  pageExtensions: ["js", "jsx", "md", "mdx", "ts", "tsx"],
});
```

Plugins that need function options can't be configured this way.

## 60: How do you use resolveAlias with the browser condition?

You can give an alias a different target for browser code:

```js
module.exports = {
  turbopack: {
    resolveAlias: {
      mocha: { browser: "mocha/browser-entry.js" },
    },
  },
};
```

Now client code that imports `mocha` gets the browser entry, while server code uses the normal one. `browser` is the only condition supported in `resolveAlias`.

## 61: How do you replace a Node.js module that breaks in the browser?

A common fix is to alias it to an empty module or a small browser version for client code only:

```js
module.exports = {
  turbopack: {
    resolveAlias: {
      fs: { browser: "./src/empty.js" },
    },
  },
};
```

```js
// src/empty.js
export default {};
```

A better long-term fix is to make sure server-only code never gets imported from client components, for example by using the `server-only` package.

## 62: How does Turbopack handle tsconfig paths?

It reads `compilerOptions.paths` and `baseUrl` from `tsconfig.json` (or `jsconfig.json`) and resolves the aliases for you:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

So `import { Button } from '@/components/Button'` works without any `resolveAlias`. Keep aliases in `tsconfig.json` so your editor, TypeScript and the bundler all agree.

## 63: How do you handle the Sass tilde import syntax with Turbopack?

Webpack's `sass-loader` let you write `@import '~bootstrap/scss/bootstrap';` to import from `node_modules`. Turbopack doesn't support the `~` prefix. Either remove the tilde, or add an alias:

```js
module.exports = {
  turbopack: {
    resolveAlias: {
      "~*": "*",
    },
  },
};
```

Removing the tilde is the cleaner fix, since modern Sass resolves packages without it.

## 64: How do you configure Turbopack in a monorepo?

Usually it just works, because Turbopack finds the root from the lockfile at the top of the repo. If you have more than one lockfile, or the app is nested in an unusual way, set `turbopack.root` to the monorepo root:

```js
const path = require("path");

module.exports = {
  turbopack: {
    root: path.join(__dirname, "../.."),
  },
};
```

Shared packages that ship untranspiled TypeScript should also be listed in `transpilePackages`.

## 65: Why does Turbopack fail to resolve a package that is linked from outside the project?

Turbopack only resolves files inside `turbopack.root`. If you use `npm link` or a symlink that points outside the root, the target is outside, so the import fails. You can set `root` to a parent folder that contains both, or in Next.js 16.4 use `experimental.turbopackAdditionalRoots` for symlink targets. Avoid making the root too big, because Turbopack may watch every file inside it.

## 66: What does transpilePackages do with Turbopack?

It tells Next.js to compile certain packages from `node_modules` like your own code, instead of using them as they are. This is useful for monorepo packages that ship TypeScript or JSX:

```js
module.exports = {
  transpilePackages: ["@acme/ui"],
};
```

It works the same with Turbopack and webpack.

## 67: What does serverExternalPackages do?

It tells Next.js not to bundle certain packages into the server output and instead load them with Node's normal `require` at runtime. This is needed for packages with native addons or that read their own files at runtime, like some database drivers:

```js
module.exports = {
  serverExternalPackages: ["sharp", "better-sqlite3"],
};
```

Next.js already has a built-in list of common packages that are treated this way.

## 68: What magic comments does Turbopack support?

They go inside dynamic `import()`, `require()`, `require.resolve()` and `new Worker()`:

- `webpackIgnore: true` tells both webpack and Turbopack to leave the import alone.
- `turbopackIgnore: true` does the same, but only for Turbopack.
- `turbopackOptional: true` tells Turbopack not to report an error if the module can't be found.

```js
const plugin = await import(/* turbopackIgnore: true */ pluginPath);
```

Other webpack magic comments like `webpackChunkName` don't do anything in Turbopack.

## 69: What does turbopackIgnore do and when would you use it?

It tells Turbopack not to bundle that import and to leave it as a real runtime `import()` or `require()`. You use it when the path is only known at runtime, for example loading a user plugin from disk on the server. Without it, Turbopack would try to resolve the path at build time and either fail or pull in too many files.

## 70: What is import.meta.glob in Turbopack?

It imports many files that match a pattern in one go, like in Vite. It was added in Next.js 16.3 and only works with Turbopack:

```js
const posts = import.meta.glob("./posts/*.mdx");

for (const path in posts) {
  const mod = await posts[path]();
  console.log(path, mod.metadata);
}
```

By default each file is loaded lazily. Pass `{ eager: true }` to import them all right away. A pattern starting with `!` excludes files. Note that `import.meta.globEager()` is not supported.

## 71: How does CSS ordering differ between Turbopack and webpack?

Turbopack orders CSS Modules by the order of the JavaScript imports that bring them in. Webpack could give slightly different results, especially when the same CSS is imported from several places. If your styles only worked because of a lucky order, they may look different after the switch. The fix is to avoid relying on order: use more specific selectors or keep each component's styles in its own module.

## 72: Which CSS Modules features from webpack's css-loader are not supported?

Turbopack doesn't support some older CSS Modules features: `:local` and `:global` on their own (only the function form `:global(.class)` works), `@value`, `:import` and `:export`, and `composes` or `@import` from a plain `.css` file (a `.css` file is always global). If a project uses these, rewrite them before moving to Turbopack.

## 73: Why might decimal numbers in your CSS look different after switching to Turbopack?

Lightning CSS rounds numbers to 5 decimal places, while webpack's CSS tools kept up to 10. So `1.4705882353` becomes `1.47059`. The visual result is the same, but snapshot tests or CSS diff tools may flag it. Update the snapshots, it's not a real bug.

## 74: How does Babel work with Turbopack?

If Turbopack finds a Babel config file in the project, it automatically runs `babel-loader` on your code, using its built-in version. You don't need a rule for it. But Babel is much slower than SWC, so check if you really need it. Many old Babel plugins (like styled-components or emotion) have SWC versions you can turn on in `next.config.js` with the `compiler` option.

## 75: How do you enable styled-components support with Turbopack?

Use the built-in SWC transform, not the Babel plugin:

```js
module.exports = {
  compiler: {
    styledComponents: true,
  },
};
```

This gives you server-side rendering support and readable class names in dev. Delete the Babel config if it was only there for styled-components, so Turbopack doesn't fall back to `babel-loader`.

## 76: How do you use Web Workers with Turbopack?

Use the standard `new URL()` pattern, which Turbopack understands and bundles as a separate entry:

```js
"use client";

export function startWorker() {
  const worker = new Worker(new URL("./worker.js", import.meta.url));
  worker.onmessage = (e) => console.log(e.data);
  worker.postMessage({ n: 40 });
  return worker;
}
```

Call `startWorker()` from an event handler or `useEffect`, since `Worker` doesn't exist during server rendering.

Turbopack sees the `new URL(..., import.meta.url)` call inside `new Worker()` and builds `worker.js` and its imports into its own chunk.

## 77: How do you import a WebAssembly file with Turbopack?

You can import `.wasm` files and Turbopack treats them as WebAssembly modules. You can also be explicit with a rule:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.wasm": { type: "wasm" },
    },
  },
};
```

For packages built with tools like `wasm-pack`, follow their bundler instructions. If something doesn't load, check whether the package expects a webpack-specific setup like `experiments.asyncWebAssembly`.

## 78: How do you speed up CI builds with the Turbopack build cache?

Since Next.js 16.3 the build cache is on by default and lives in `.next/cache`. It only helps if CI keeps that folder between runs. For example in GitHub Actions:

```yaml
- uses: actions/cache@v4
  with:
    path: .next/cache
    key: next-${{ hashFiles('package-lock.json') }}-${{ hashFiles('src/**') }}
    restore-keys: |
      next-${{ hashFiles('package-lock.json') }}-
```

Vercel restores this cache for you automatically.

## 79: How do you turn off the Turbopack filesystem cache?

Set the experimental options to `false`:

```js
module.exports = {
  experimental: {
    turbopackFileSystemCacheForDev: false,
    turbopackFileSystemCacheForBuild: false,
  },
};
```

You'd do this to rule the cache out while debugging a strange issue, or when disk space is very limited. Both are `true` by default in current Next.js 16.

## 80: How do you migrate a next.config.js from webpack to Turbopack?

Go through the `webpack()` callback line by line:

1. Loader rules (`module.rules`) become `turbopack.rules`.
2. `resolve.alias` becomes `turbopack.resolveAlias`.
3. `resolve.extensions` becomes `turbopack.resolveExtensions`.
4. `DefinePlugin` values often become env variables or `NEXT_PUBLIC_` vars.
5. Other plugins need a different solution, or a reason to stay on webpack.

Then run `next dev` and `next build` and compare the output. Keep the old webpack config for a while if you need `--webpack` as a fallback.

## 81: How do you replace webpack's DefinePlugin in a Turbopack project?

For values known at build time, use environment variables. `NEXT_PUBLIC_` variables are inlined in client code:

```bash
# .env
NEXT_PUBLIC_APP_VERSION=1.4.0
```

You can also use the `env` option in `next.config.js`, which inlines values into both server and client code:

```js
module.exports = {
  env: {
    BUILD_TIME: new Date().toISOString(),
  },
};
```

## 82: Why does Fast Refresh sometimes do a full reload instead of a hot update?

Fast Refresh only keeps state when a file exports React components only. If the file also exports a plain value or function used outside React, or the component is an anonymous default export, React can't safely swap it, so it reloads the page. Also, if the error is in a file imported outside the React tree, a full reload happens. Name your components and keep non-component exports in separate files.

## 83: How do you collect a trace to report a Turbopack performance problem?

Run the dev server with the internal trace flag:

```bash
next dev --internal-trace
```

Use the app until the slow part happens, then stop the server. The trace is written to `.next-profiles/trace-turbopack.bin`. You can attach this file to a GitHub issue so the Next.js team can see where time was spent.

## 84: How do you analyze bundle size with Turbopack?

`@next/bundle-analyzer` is a webpack plugin, so it does not work with Turbopack. Next.js 16.1 added an experimental analyzer that works with Turbopack:

```bash
next experimental-analyze
```

It shows which modules end up in each route and why they are there. You can also check the route sizes printed at the end of `next build`.

## 85: What do the development and production conditions do in rules?

They let you run a loader only in `next dev` or only in `next build`:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.js": {
        condition: { all: ["production", { not: "foreign" }] },
        loaders: ["./loaders/strip-debug.js"],
      },
    },
  },
};
```

This is handy for loaders that are slow and only needed for the final build, or for debug helpers you only want while coding.

## 86: How do you write a simple custom loader for Turbopack?

A loader is a function that gets the file content and returns JavaScript. It uses the same API as webpack loaders:

```js
// loaders/upper.js
module.exports = function (source) {
  const text = JSON.stringify(source.toUpperCase());
  return `export default ${text};`;
};
```

```js
// next.config.js
module.exports = {
  turbopack: {
    rules: {
      "*.shout": {
        loaders: ["./loaders/upper.js"],
        as: "*.js",
      },
    },
  },
};
```

Keep loaders simple: some parts of the webpack loader API, like `emitFile` and `loadModule`, are not available.

## 87: How do you load a YAML file with Turbopack?

Install `yaml-loader` and add a rule:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.yaml": {
        loaders: ["yaml-loader"],
        as: "*.js",
      },
    },
  },
};
```

```js
import config from "./config.yaml";

console.log(config.title);
```

## 88: How do you import GraphQL files with Turbopack?

Use `graphql-tag/loader`, which is one of the tested loaders:

```js
module.exports = {
  turbopack: {
    rules: {
      "*.graphql": {
        loaders: ["graphql-tag/loader"],
        as: "*.js",
      },
    },
  },
};
```

```js
import GetUser from "./get-user.graphql";

const result = await client.query({ query: GetUser });
```

## 89: How is Turbopack different from Vite in development?

Vite serves your source files as native ES modules in dev and lets the browser request each one, only pre-bundling dependencies. Turbopack bundles in dev too, but lazily, only for the routes you open. Bundling avoids the browser making thousands of requests in large apps. Both cache and only redo changed work. In practice both are fast, and the bigger difference is that Turbopack is tied to Next.js while Vite works with many frameworks.

## 90: How is Turbopack different from Rspack?

Rspack is also a Rust bundler, but it is built to be compatible with webpack's API, so many webpack plugins and configs work with small changes. Turbopack has its own architecture based on incremental computation and does not try to support webpack plugins, only some loaders. Rspack is a drop-in path for webpack users. Turbopack is designed around Next.js and its server and client graph.

## 91: What does the ignoreIssue option do?

`turbopack.ignoreIssue` lets you hide specific Turbopack warnings or errors that you know are safe, for example a warning from a package you can't change. Use it carefully and with narrow matches. Hiding a real problem just moves the error to runtime.

## 92: Why do you get "Module not found" errors after switching to Turbopack?

The usual causes are: an import that relied on a webpack alias from the old `webpack()` config, the Sass `~` prefix, a file outside `turbopack.root` (for example a linked package), or an extension that isn't in `resolveExtensions`. Check the import path in the error, then fix it with `resolveAlias`, `tsconfig` paths, `root`, or by adding the extension.

## 93: What is a client boundary in Turbopack's graph?

When a server component imports a file with `'use client'`, that import is a boundary. Turbopack stops treating the code after it as server code and puts it into the client graph, creating client chunks for it. On the server side only a reference is kept. This is why a `'use client'` file and everything it imports end up in the browser bundle.

## 94: Why might a package work with webpack but break with Turbopack?

Some packages depend on webpack-specific behavior: `require.context`, webpack globals like `__webpack_require__`, a webpack plugin to set them up, or loose CommonJS patterns. Others ship code that only works with a certain module resolution. Check the package's issues for Turbopack reports, update it, or work around it with `resolveAlias`, `transpilePackages` or `serverExternalPackages`.

## 95: Does Turbopack support require.context?

`require.context` is a webpack feature, and Turbopack's main answer for "import many files by pattern" is `import.meta.glob`, added in Next.js 16.3. If your code uses `require.context`, test it under Turbopack, and if it doesn't work, rewrite it:

```js
// webpack style
// const ctx = require.context('./icons', false, /\.svg$/);

// Turbopack style
const icons = import.meta.glob("./icons/*.svg", { eager: true });
```

## 96: What changed in Turbopack in Next.js 16.3?

The main changes were: dev memory usage cut by up to about 90% on large apps (with the dev cache on), the filesystem cache turned on by default for `next build`, `import.meta.glob` support, an experimental Rust version of the React Compiler, a smaller runtime, support for local PostCSS configs, and faster HMR startup on big apps.

## 97: How does Turbopack handle environment-specific code like if (process.env.NODE_ENV === 'production')?

`process.env.NODE_ENV` is replaced with a fixed string at build time, so the condition becomes `if ('production' === 'production')`. The minifier then removes the dead branch. This means dev-only code inside such checks doesn't end up in the production bundle. Reading `process.env` with a dynamic key, like `process.env[name]`, can't be replaced this way.

## 98: How do you enable the React Compiler with Turbopack?

Turn on `reactCompiler` in `next.config.js`:

```js
module.exports = {
  reactCompiler: true,
};
```

By default this uses the Babel version of the compiler, which slows builds. Next.js 16.3 added an experimental Rust version you can try with `experimental.turbopackRustReactCompiler: true`, which Vercel says compiles noticeably faster.

## 99: What should you check if Turbopack dev uses too much memory?

First update Next.js, since 16.3 cut dev memory a lot. Make sure the dev filesystem cache is on, because memory eviction depends on it, and that `experimental.turbopackMemoryEviction` hasn't been set to `false`. Check that `turbopack.root` isn't too broad, so it isn't watching unrelated folders. If it's still high, collect a trace with `--internal-trace` and report it.

## 100: Should you keep a webpack fallback after moving to Turbopack?

For a while, yes. Keeping `--webpack` scripts (for example `dev:webpack`, `build:webpack`) lets you check if a bug comes from the bundler or your code. Once production has run on Turbopack for some time without problems, remove the webpack config so you don't keep two setups in sync.

# Advanced Questions (101-150)

## 101: How does Turbopack's incremental engine work at a high level?

Turbopack is built on an engine called Turbo Tasks. Every step of the build (reading a file, parsing it, resolving an import, building a chunk) is a function whose result is stored. While a function runs, the engine records which other results it read. That gives a dependency graph between tasks. When a file changes, the engine marks the task that read it as dirty, follows the graph to find everything that depended on it, and reruns only those tasks. If a rerun gives the same result as before, the change stops spreading there.

## 102: What is function-level caching and why does it matter?

Most bundlers cache per file or per module: if a file changes, its whole processing is redone. Turbopack caches each small function call with its inputs. For example, "get the exports of module X" is cached separately from "parse module X". If you edit the body of a function but not its exports, the work that only depends on the exports doesn't rerun. This makes updates in big graphs much cheaper.

## 103: Why does a change sometimes stop spreading early in Turbopack's graph?

When a task reruns after a change, the engine compares the new result with the old one. If they are equal, tasks that depend on it are not rerun, even though one of their inputs was marked dirty. For example, changing a comment in a file changes the source but may not change the list of imports, so module graph building doesn't need to rerun. This "early cutoff" is a big reason HMR stays fast.

## 104: What are value cells (Vc) in Turbopack's code?

In the Rust source, results of Turbo Tasks are stored in cells, and functions pass around references to them, written as `Vc<T>`. A `Vc` is like a handle to a value the engine is tracking. When a task reads a `Vc`, the engine records the dependency. When the cell's value changes, readers get invalidated. You don't need this to use Turbopack, but it explains how the engine knows exactly what depends on what.

## 105: Why does Turbopack use one module graph for client and server?

Next.js apps have code for the browser, Node.js and the edge runtime, and with React Server Components these are mixed in the same files and trees. With webpack, Next.js ran several separate compilers and had to keep them in sync by hand. Turbopack puts all environments in one graph, so it can see where `'use client'` and `'use server'` boundaries are, share work like parsing between environments, and update everything correctly after a single change.

## 106: How does the same file get compiled differently for client and server in one graph?

Each module in Turbopack is processed in a context that says which environment it is for (browser, Node.js, edge), which conditions apply when resolving packages, and which transforms to use. The same source file can show up as two different modules, one per context. Reading and parsing the file can be shared, while the resolve and transform steps run separately per environment.

## 107: Why does Turbopack bundle in dev instead of serving unbundled ES modules like Vite?

Unbundled dev means one browser request per module. In apps with thousands of modules, that can mean slow page loads in dev, even with HTTP/2, plus a deep waterfall as the browser discovers imports one level at a time. Turbopack's bet is that with fine-grained caching, bundling is cheap enough to do on every change, and you avoid the request waterfall. Lazy bundling keeps startup fast by only building the requested routes.

## 108: How does lazy compilation in dev interact with the filesystem cache?

Lazy compilation decides what to build: only the routes you open. The filesystem cache decides what to reuse: anything built in an earlier session that is still valid. With both on, restarting `next dev` and opening a route you visited yesterday mostly loads from disk. A route you have never opened is built fresh. They solve different problems: lazy for first startup, cache for restarts.

## 109: How does Turbopack know a cached result on disk is still valid after a restart?

When the dev server starts with a persisted cache, Turbopack has to check which inputs changed while it wasn't running. It compares the files on disk with what it recorded (file content or metadata), plus config and dependency versions. Changed inputs are marked dirty and invalidation spreads through the saved task graph, just like during a live session. Tasks that are not affected are reused as they are.

## 110: What can cause a stale or broken filesystem cache and how do you handle it?

Most often: changes Turbopack can't see as file changes, like a loader that reads an env variable or a file outside the root, a package changed in place in `node_modules` (for example by a patch script), or a bug after a Next.js upgrade. Symptoms are old code showing up or strange build errors that disappear after deleting `.next`. Fix the cause where you can (make loaders depend only on their inputs), and as a quick fix delete `.next` or turn the cache off to confirm.

## 111: Why must loader options be serializable in Turbopack?

Turbopack runs webpack loaders in separate Node.js processes, not in the Rust process. Options are sent to those processes as data, so they must be JSON-like. Serializable options are also part of the cache key: Turbopack needs to compare options to know if a cached result is still valid, and it can't compare a function. That's why `require('remark-gfm')` as an option doesn't work, but the string `'remark-gfm'` can.

## 112: How does Turbopack run JavaScript loaders from Rust?

It keeps a pool of Node.js worker processes. When a file needs a loader, Turbopack sends the source and options to a worker, which runs the loader through a webpack-compatible loader runner and sends back the result. The `experimental.turbopackPluginRuntimeStrategy` option controls how these run, with child processes as the default. Crossing between Rust and Node has a cost, so loaders are one of the slower parts of a Turbopack build.

## 113: Why are some parts of the webpack loader API not supported?

Methods like `this.loadModule`, `this.importModule` and `this.emitFile` let a loader reach back into the bundler: compile another module, run it, or write extra output files. In webpack this is easy because the loader runs inside webpack. In Turbopack the loader runs in a separate Node process, and any side effect like that would also need to be tracked by the incremental engine to stay correct. `this.fs` only supports `readFile` for the same reason.

## 114: Why will Turbopack never support webpack plugins?

Webpack plugins tap into webpack's hook system and change its internal objects (compilation, chunks, module factories) directly. Turbopack has no such objects. Its data lives in Rust, in a cached and incremental form. Supporting plugins would mean rebuilding webpack's object model and hooks on top of Turbopack, and any plugin could break the incremental tracking. The team chose to support loaders, which are pure transforms, and build common plugin features into Next.js.

## 115: Why doesn't Turbopack support Yarn Plug'n'Play?

Yarn PnP replaces `node_modules` with zip archives and a resolver file (`.pnp.cjs`) that must be used to find packages. Supporting it means hooking into that resolver and reading files from zip archives, for every lookup, in a way that works with Turbopack's file watching and caching. The Next.js docs list it as not planned. Projects using PnP need to switch Yarn to `nodeLinker: node-modules` or use `--webpack`.

## 116: How are module IDs handled in dev versus production?

In dev, `turbopackModuleIds` defaults to `named`, so module IDs are readable paths, which helps debugging. In production it defaults to `deterministic`, which gives short IDs based on a hash so they stay the same between builds when the module doesn't change. Stable IDs matter for long-term caching: if IDs shifted on every build, unchanged chunks would get new content and new file names, and users would download them again.

## 117: How do content hashes in chunk file names help caching?

Production chunks are named with a hash of their content. If a chunk doesn't change between deploys, its URL stays the same and browsers can keep using their cached copy, so these files can be served with a long `Cache-Control` max-age. If anything inside changes, the hash changes and the browser fetches the new file. Deterministic module IDs are needed for this, otherwise unrelated changes would change every hash.

## 118: What is scope hoisting and does Turbopack do it?

Scope hoisting puts several ES modules into one function scope instead of wrapping each in its own function. This makes the code smaller and a bit faster, because calls between modules become direct references and the minifier can do more. Turbopack does this in production builds, controlled by `experimental.turbopackScopeHoisting`. It is harder with CommonJS or modules with unclear side effects, so those stay wrapped.

## 119: How does Turbopack do tree shaking at a finer level than whole modules?

Turbopack can split a module into fragments based on its top-level statements and what each export needs. If you import one export, only the statements that export depends on (and anything with side effects) are kept. This is controlled by options like `experimental.turbopackModuleFragments` and `turbopackRemoveUnusedExports`. It helps with big utility files and barrel files, where most of the code isn't used by a given route.

## 120: What are side effects and why do they matter for tree shaking?

A module has side effects if just importing it does something, like changing a global, adding a polyfill or importing CSS. A bundler can only drop unused imports when it knows dropping them changes nothing. The `"sideEffects": false` field in a package's `package.json` tells bundlers it is safe. Turbopack also tries to detect side-effect-free modules itself (`experimental.turbopackInferModuleSideEffects`, on by default). A wrong `sideEffects` field in a package can lead to missing CSS or missing setup code.

## 121: Why are barrel files bad for bundler performance and how does Next.js help?

A barrel file (`index.js` that re-exports everything) makes the bundler load and parse every re-exported module, even if you need only one. For icon libraries this can be thousands of files. Next.js has `optimizePackageImports`, which rewrites imports from listed packages to point directly at the file that exports the name. Many popular libraries are on the default list. Turbopack's fine-grained tree shaking helps too, but avoiding barrels in your own code is still the best fix.

## 122: How does Turbopack handle package.json exports and conditions?

It follows the `exports` field in `package.json` and picks an entry based on the active conditions. Browser code uses conditions like `browser`, `import` or `require`, and `default`. Server code uses `node` and, for React Server Components, `react-server`. Turbopack also supports the `module-sync` condition (fixed in 16.3). If a package has wrong or incomplete `exports`, you may get the wrong build of it, for example a Node build in the browser.

## 123: What is the dual package hazard and how can it show up with Turbopack?

When a package ships both ESM and CommonJS builds, the same app can end up loading both: one through `import` and one through `require`. Then you have two copies of its module state, for example two React contexts or two singletons that don't see each other. In Next.js this shows up as "hooks can only be called inside a component" or a context provider that doesn't work. Fix it by making all imports go through the same format, with `resolveAlias`, or by updating the package.

## 124: How does HMR work under the hood with Turbopack?

The browser opens a WebSocket to the dev server and subscribes to the chunks it has loaded. When a file changes, Turbopack recomputes the affected modules and sends only the changed module code. The Turbopack runtime in the browser replaces those modules and runs the HMR accept logic, which React Fast Refresh uses to re-render components while keeping state. If no module accepts the update, the runtime falls back to a full reload. Next.js 16.3 merged these subscriptions to cut startup cost on large apps.

## 125: How are server-side changes picked up in dev?

For server components and route handlers, Turbopack rebuilds the server output and Next.js reloads the affected server modules. The client then refetches the React Server Components payload for the current route, so you see the new server-rendered output without a full page reload. Because client and server are in one graph, a change in a shared file updates both sides together.

## 126: What does turbopackMemoryEviction do?

Added in Next.js 16.3, memory eviction lets Turbopack drop task results from memory once they are safely written to the filesystem cache, and load them back from disk when needed. This is how dev memory dropped by up to about 90% on very large apps. It needs the dev filesystem cache to be on. The default is `'auto'`, and setting it to `false` keeps everything in memory, which can help if disk is slow but uses much more RAM.

## 127: What is the trade-off of turning off the dev filesystem cache?

Without it, every `next dev` restart compiles everything from scratch for each route you open, so restarts are slower. Memory eviction also can't work, so a long dev session can use much more memory. The upside is that no stale cache can cause problems, and no disk space is used. It makes sense as a debugging step, rarely as a permanent setting.

## 128: How would you debug a production bug that only happens with Turbopack, not webpack?

First confirm it: build the same commit with `next build` and `next build --webpack` and compare. Then narrow it down: check CSS order differences, side effects that got tree-shaken, a package resolving to a different `exports` entry, or a webpack-only feature that silently did nothing. Build with minification turned off (`experimental.turbopackMinify: false`) to read the output. Once you have a small reproduction, check existing issues on the Next.js repo and open one with it.

## 129: What are debug IDs and why are they useful?

A debug ID is a unique ID written into both a JavaScript file and its source map. Error tracking tools (like Sentry) use it to match a minified stack frame to the right source map, even if file names or URLs change between deploys. Turn it on with `turbopack.debugIds: true`. The IDs are available at runtime on `globalThis._debugIds`. It's more reliable than matching by URL, which breaks with CDNs and versioned paths.

## 130: What security issues should you think about with Turbopack builds?

Mostly the same as with any bundler. Only `NEXT_PUBLIC_` variables should be inlined in client code, so never prefix secrets that way. Importing server code into a client component can pull secrets or private logic into the browser bundle, so use the `server-only` package to make that an error. Public source maps expose your source, so keep `productionBrowserSourceMaps` off unless you upload them privately to an error tracker. And loaders run arbitrary Node code during the build, so only use trusted ones.

## 131: How does the server-only package protect you at build time?

`server-only` is a package that throws an error when imported in a client environment. Because Turbopack resolves it with the client conditions in the browser graph, the build fails if a file importing it ever ends up in client code:

```js
// lib/db.js
import "server-only";

export async function getUser(id) {
  // database code with secrets
}
```

So if someone imports `getUser` from a `'use client'` file, you get a build error instead of shipping database code to the browser.

## 132: Why does Turbopack limit resolution and watching to the root?

Watching and hashing files costs time and memory, and the engine must track every file it reads to keep the cache correct. Limiting everything to one root keeps that set clear and bounded. It also stops the build from depending on files in random places on the machine, which would make results differ between machines and break caching. That's why a root that is too broad (like your home folder) can hurt performance.

## 133: How would you migrate a large app with a heavy custom webpack config to Turbopack?

Make a list of everything the webpack config does and sort it: loaders (move to `turbopack.rules`), aliases (move to `resolveAlias` or tsconfig paths), defines (move to env), plugins (find a built-in Next.js feature, a loader, or a build script). Move it one piece at a time with dev on Turbopack first, while production still uses `--webpack`. Compare build output and run e2e tests on both. Switch production when the tests pass, and keep the webpack fallback for one or two releases.

## 134: How can you replace a webpack plugin that generated a file at build time?

Since Turbopack loaders can't emit files and plugins aren't supported, move that work out of the bundler. Run a Node script before the build (for example a `prebuild` npm script) that writes the file into `public/` or into a source file the app imports:

```json
{
  "scripts": {
    "prebuild": "node scripts/generate-sitemap.js",
    "build": "next build"
  }
}
```

For things like sitemaps and robots files, Next.js has built-in `sitemap.js` and `robots.js` route files that are an even better fit.

## 135: What happens when a loader is slow and runs on many files?

Each file goes from Rust to a Node worker and back, so a slow loader on thousands of files can dominate the build and slow HMR. To fix it, make the glob narrower, add a `condition` like `{ not: 'foreign' }` to skip `node_modules`, use a `content` condition so the loader only runs when needed, or replace the loader with a built-in feature (SWC transform, `type: 'text'`). A trace from `--internal-trace` shows how much time goes into loaders.

## 136: How do you handle a library that ships a Babel plugin required for it to work?

First check if an SWC version exists. Next.js has built-in SWC options for styled-components, emotion, Relay and some others under `compiler`. If not, look for an SWC plugin. As a last resort, keep a Babel config, which makes Turbopack run `babel-loader` with that plugin on your code. That works, but every file now goes through Babel, so builds and HMR get slower. Limit the cost by moving that code into a small package if possible.

## 137: How does the Edge runtime affect what Turbopack can bundle?

Code for the edge runtime (for example middleware or routes with `export const runtime = 'edge'`) is bundled in an edge context with different conditions and no Node.js built-ins like `fs` or `child_process`. Imports that work in Node can fail here at build time. Turbopack resolves packages with edge-friendly conditions where the package supports them. Note that the `edge-light` rule condition is deprecated, and Next.js 16 pushes middleware toward the Node.js runtime through `proxy.js`.

## 138: Why did the Next.js team make Turbopack the default in 16 instead of keeping it opt-in?

By then most active dev sessions on Next.js 15 already used Turbopack, it was stable for dev, and builds had been in beta and tested on large apps like vercel.com. Keeping two bundlers as equal defaults doubles the testing and bug surface. Making Turbopack the default moves most users to the faster path, while `--webpack` stays as an escape hatch for projects that depend on webpack plugins or features Turbopack doesn't have.

## 139: How would you prove that Turbopack actually made your team faster?

Measure before and after on the same machine and commit. For dev: time to first page load after `next dev` starts (cold and with cache), and time for a change to show up in the browser. For builds: `next build` time with and without a restored cache in CI. Record memory use for long dev sessions too. Run each several times and compare medians, since single runs vary a lot.

## 140: How does Turbopack's design compare to incremental builds in webpack 5's persistent cache?

Webpack 5's persistent cache saves processed modules to disk and reuses them, but the caching unit is mostly the module, and many steps (like chunk graph building and optimization) still rerun on every build. Turbopack tracks dependencies at the function level for all steps, including resolving, graph building and chunking, so a small change can skip much more. Webpack also has to keep JavaScript object graphs in memory, while Turbopack's Rust data is more compact.

## 141: What is the downside of fine-grained incremental computation?

Tracking every task and its dependencies costs memory and some time. For a single cold build of a small app, that overhead can make the gain smaller. The engine is also complex: a missed dependency means a stale result, which is a harder bug to find than "slow build". That's why Turbopack needed several releases to reduce memory (eviction in 16.3) and why cache bugs, while rare, are worth reporting with a reproduction.

## 142: Why might a dynamic import with a variable path cause problems?

With ``import(`./locales/${lang}.json`)`` the bundler can't know the exact file at build time. Turbopack has to include every file that could match the pattern in the folder, which can add many chunks or files you didn't expect. A completely dynamic path like `import(somePath)` can't be resolved at all. Use a fixed map of imports or `import.meta.glob` to be explicit, or `turbopackIgnore` if the import is meant to stay a runtime import.

```js
const locales = {
  en: () => import("./locales/en.json"),
  de: () => import("./locales/de.json"),
};

const messages = await locales[lang]();
```

## 143: How does Turbopack handle CommonJS interop edge cases?

When ESM imports a CommonJS module, the bundler has to guess the shape: is `module.exports` the default export, or are its properties named exports? Turbopack follows the common Node.js and bundler behavior, but packages that set `__esModule` incorrectly or reassign `module.exports` late can give `undefined` imports or `default.default`. If you hit this, check how the package exports, try a default import instead of named imports, or alias to the package's ESM build.

## 144: What is the role of the Turbopack runtime in the browser?

Bundled code needs a small runtime to register modules, load chunks on demand, and handle HMR in dev. Turbopack's runtime is shared by all chunks and is responsible for things like `import()` loading a chunk over the network and running its modules in the right order. Next.js 16.3 shipped a smaller runtime, which reduces the JavaScript every page has to download and parse.

## 145: Why are minification and source maps handled differently in dev?

In dev, the goal is fast updates and readable errors. Minifying takes time and makes code hard to read, so `turbopackMinify` is off by default in dev and on in builds. Source maps are kept on in dev so errors point to your files. In builds, server source maps help with server error stack traces, while browser source maps are opt-in because they expose your code.

## 146: How should you handle a third-party package that reads its own files with fs at runtime on the server?

Bundling such a package breaks the file paths it expects, since the files are not next to the bundled code anymore. Add it to `serverExternalPackages` so it stays in `node_modules` and loads with Node's `require`. Next.js output file tracing then copies the package and its files into the standalone output if you use `output: 'standalone'`. For your own code, prefer `path.join(process.cwd(), ...)` and keep those files in a known folder.

## 147: Scenario: HMR became slow after adding a new library. How do you investigate?

Check whether the library is imported from a file that many routes share, like the root layout, because then every change in that area touches a huge part of the graph. Check if a loader or Babel started running (for example, the library added a Babel config). Look for a barrel import that pulls in thousands of modules, and add it to `optimizePackageImports`. Then collect a trace with `next dev --internal-trace` to see which tasks take the time.

## 148: Scenario: the build passes locally but fails in CI with Turbopack. What do you check?

Compare Node.js and Next.js versions, and make sure CI does a clean install from the lockfile. Check the platform: Alpine images need the musl build of `@next/swc` to be installed (a lockfile made on macOS can miss it), and unsupported platforms fall back to WASM, which can't run Turbopack. Look for case-sensitive imports that work on macOS but not on Linux. Check if CI restores an old `.next/cache` from another branch or version. Also check env variables, since missing ones can change which code paths get bundled.

## 149: When would you still choose webpack for a Next.js project today?

When the project depends on a webpack plugin with no replacement, uses Yarn PnP, needs a stylesheet or image loader (Less, some image optimizers), uses `experimental.urlImports`, or runs on a platform without native bindings. Also when a large legacy config can't be migrated yet. In those cases `--webpack` is a valid choice, but treat it as temporary, since new Next.js features and fixes land in Turbopack first.

## 150: What are the main limits of Turbopack today that you should know before adopting it?

It is only usable through Next.js, so you can't pick it for a non-Next app. Webpack plugins don't work and only a subset of the loader API is available. Some older CSS Modules features, Less, Yarn PnP and custom Sass functions aren't supported. CSS ordering and some edge cases can differ from webpack. And it does no type checking. For most Next.js apps none of these is a blocker, but you should check them against your project before you switch.
