# esbuild Interview Questions and Answers

_Last updated: October 28, 2026_

120 esbuild interview questions with answers, split into three levels: 40 easy, 40 moderate and 40 advanced.

The answers target esbuild 0.28. Since esbuild is still on 0.x versions, minor releases can contain breaking changes, so the notes mention the version where something changed when it matters (for example the dev server security changes in 0.25.0). Code examples use the JavaScript API unless the question says otherwise.

## Table of Contents

- [Easy Questions (1-40)](#easy-questions-1-40)
- [Moderate Questions (41-80)](#moderate-questions-41-80)
- [Advanced Questions (81-120)](#advanced-questions-81-120)

### Easy Questions (1-40)

- [1: What is esbuild?](#1-what-is-esbuild)
- [2: Why is esbuild so fast?](#2-why-is-esbuild-so-fast)
- [3: How do you install esbuild?](#3-how-do-you-install-esbuild)
- [4: How do you bundle a file with the esbuild CLI?](#4-how-do-you-bundle-a-file-with-the-esbuild-cli)
- [5: What are the ways to use esbuild?](#5-what-are-the-ways-to-use-esbuild)
- [6: How do you run a build from JavaScript?](#6-how-do-you-run-a-build-from-javascript)
- [7: What is the difference between `build` and `transform`?](#7-what-is-the-difference-between-build-and-transform)
- [8: What is an entry point?](#8-what-is-an-entry-point)
- [9: What is the difference between `outfile` and `outdir`?](#9-what-is-the-difference-between-outfile-and-outdir)
- [10: What output formats does esbuild support?](#10-what-output-formats-does-esbuild-support)
- [11: What does the `platform` option do?](#11-what-does-the-platform-option-do)
- [12: What does the `target` option do?](#12-what-does-the-target-option-do)
- [13: How do you minify the output?](#13-how-do-you-minify-the-output)
- [14: How do you generate source maps?](#14-how-do-you-generate-source-maps)
- [15: Does esbuild support TypeScript?](#15-does-esbuild-support-typescript)
- [16: Does esbuild support JSX?](#16-does-esbuild-support-jsx)
- [17: What is a loader in esbuild?](#17-what-is-a-loader-in-esbuild)
- [18: How do you import a JSON file?](#18-how-do-you-import-a-json-file)
- [19: Can esbuild bundle CSS?](#19-can-esbuild-bundle-css)
- [20: What does `--bundle` actually do?](#20-what-does---bundle-actually-do)
- [21: What is tree shaking?](#21-what-is-tree-shaking)
- [22: What is an external module?](#22-what-is-an-external-module)
- [23: How do you mark all npm packages as external?](#23-how-do-you-mark-all-npm-packages-as-external)
- [24: What is watch mode?](#24-what-is-watch-mode)
- [25: Does esbuild have a dev server?](#25-does-esbuild-have-a-dev-server)
- [26: Does esbuild support hot module replacement (HMR)?](#26-does-esbuild-support-hot-module-replacement-hmr)
- [27: How do you enable live reload with the esbuild dev server?](#27-how-do-you-enable-live-reload-with-the-esbuild-dev-server)
- [28: What does the `define` option do?](#28-what-does-the-define-option-do)
- [29: How do you use environment variables in a browser bundle?](#29-how-do-you-use-environment-variables-in-a-browser-bundle)
- [30: Does esbuild check TypeScript types?](#30-does-esbuild-check-typescript-types)
- [31: How do you import an image with esbuild?](#31-how-do-you-import-an-image-with-esbuild)
- [32: What does `--log-level` do?](#32-what-does---log-level-do)
- [33: How do you build several entry points at once?](#33-how-do-you-build-several-entry-points-at-once)
- [34: Can esbuild bundle Node.js code?](#34-can-esbuild-bundle-nodejs-code)
- [35: What does `banner` and `footer` do?](#35-what-does-banner-and-footer-do)
- [36: What does `--global-name` do?](#36-what-does---global-name-do)
- [37: Can esbuild compile code for old browsers like IE11?](#37-can-esbuild-compile-code-for-old-browsers-like-ie11)
- [38: What is the `write` option?](#38-what-is-the-write-option)
- [39: Which popular tools use esbuild?](#39-which-popular-tools-use-esbuild)
- [40: What does `esbuild --version` show and why does the version matter?](#40-what-does-esbuild---version-show-and-why-does-the-version-matter)

### Moderate Questions (41-80)

- [41: What is a build context and why would you use one?](#41-what-is-a-build-context-and-why-would-you-use-one)
- [42: Why should you call `dispose()` on a context?](#42-why-should-you-call-dispose-on-a-context)
- [43: How do you write a simple esbuild plugin?](#43-how-do-you-write-a-simple-esbuild-plugin)
- [44: What is the difference between `onResolve` and `onLoad`?](#44-what-is-the-difference-between-onresolve-and-onload)
- [45: What is a namespace in an esbuild plugin?](#45-what-is-a-namespace-in-an-esbuild-plugin)
- [46: Why does the `filter` in a plugin have to be a regex?](#46-why-does-the-filter-in-a-plugin-have-to-be-a-regex)
- [47: What are `onStart` and `onEnd` used for?](#47-what-are-onstart-and-onend-used-for)
- [48: How do you use `build.resolve()` inside a plugin?](#48-how-do-you-use-buildresolve-inside-a-plugin)
- [49: How do path aliases from `tsconfig.json` work with esbuild?](#49-how-do-path-aliases-from-tsconfigjson-work-with-esbuild)
- [50: Which `tsconfig.json` settings does esbuild read?](#50-which-tsconfigjson-settings-does-esbuild-read)
- [51: Why do you need `isolatedModules` when using esbuild with TypeScript?](#51-why-do-you-need-isolatedmodules-when-using-esbuild-with-typescript)
- [52: How does esbuild handle CSS modules?](#52-how-does-esbuild-handle-css-modules)
- [53: How do you use Sass, Less or PostCSS with esbuild?](#53-how-do-you-use-sass-less-or-postcss-with-esbuild)
- [54: How does code splitting work in esbuild?](#54-how-does-code-splitting-work-in-esbuild)
- [55: How do dynamic imports work in esbuild?](#55-how-do-dynamic-imports-work-in-esbuild)
- [56: How do you control output file names?](#56-how-do-you-control-output-file-names)
- [57: How do you find the hashed file names after a build to put them in HTML?](#57-how-do-you-find-the-hashed-file-names-after-a-build-to-put-them-in-html)
- [58: What is the metafile?](#58-what-is-the-metafile)
- [59: How do you see what makes your bundle large?](#59-how-do-you-see-what-makes-your-bundle-large)
- [60: How do you remove `console.log` and `debugger` from production builds?](#60-how-do-you-remove-consolelog-and-debugger-from-production-builds)
- [61: What does `inject` do?](#61-what-does-inject-do)
- [62: How does esbuild handle CommonJS and ES module mixing?](#62-how-does-esbuild-handle-commonjs-and-es-module-mixing)
- [63: What are `mainFields` and `conditions`?](#63-what-are-mainfields-and-conditions)
- [64: How do you build a library that ships both ESM and CommonJS?](#64-how-do-you-build-a-library-that-ships-both-esm-and-commonjs)
- [65: How do you create type declaration files (`.d.ts`) with esbuild?](#65-how-do-you-create-type-declaration-files-dts-with-esbuild)
- [66: How does esbuild handle decorators?](#66-how-does-esbuild-handle-decorators)
- [67: What does `keepNames` do?](#67-what-does-keepnames-do)
- [68: How do legal comments work?](#68-how-do-legal-comments-work)
- [69: How do you run esbuild in Node.js scripts that also need to work in CI?](#69-how-do-you-run-esbuild-in-nodejs-scripts-that-also-need-to-work-in-ci)
- [70: How do you handle `__dirname` and `require` in an ESM bundle for Node.js?](#70-how-do-you-handle-__dirname-and-require-in-an-esm-bundle-for-nodejs)
- [71: What does the `jsx` option accept and when do you use each value?](#71-what-does-the-jsx-option-accept-and-when-do-you-use-each-value)
- [72: How do you use esbuild to run TypeScript directly in Node.js?](#72-how-do-you-use-esbuild-to-run-typescript-directly-in-nodejs)
- [73: What is the difference between `esbuild` and `esbuild-wasm`?](#73-what-is-the-difference-between-esbuild-and-esbuild-wasm)
- [74: Why does esbuild sometimes fail after copying `node_modules` between machines?](#74-why-does-esbuild-sometimes-fail-after-copying-node_modules-between-machines)
- [75: How do you build an app that loads CSS, images and fonts?](#75-how-do-you-build-an-app-that-loads-css-images-and-fonts)
- [76: What is `outbase` and when do you need it?](#76-what-is-outbase-and-when-do-you-need-it)
- [77: How do you change the output file extension?](#77-how-do-you-change-the-output-file-extension)
- [78: How do you read esbuild errors and warnings in the API?](#78-how-do-you-read-esbuild-errors-and-warnings-in-the-api)
- [79: How do you silence or turn a specific warning into an error?](#79-how-do-you-silence-or-turn-a-specific-warning-into-an-error)
- [80: How would you migrate a simple Webpack project to esbuild?](#80-how-would-you-migrate-a-simple-webpack-project-to-esbuild)

### Advanced Questions (81-120)

- [81: How does esbuild work internally, step by step?](#81-how-does-esbuild-work-internally-step-by-step)
- [82: How does the JavaScript API talk to the Go binary?](#82-how-does-the-javascript-api-talk-to-the-go-binary)
- [83: Why do JavaScript plugins slow esbuild down, and how do you keep them fast?](#83-why-do-javascript-plugins-slow-esbuild-down-and-how-do-you-keep-them-fast)
- [84: What are the limits of `buildSync` and `transformSync`?](#84-what-are-the-limits-of-buildsync-and-transformsync)
- [85: How do incremental rebuilds work?](#85-how-do-incremental-rebuilds-work)
- [86: How does esbuild watch mode detect file changes?](#86-how-does-esbuild-watch-mode-detect-file-changes)
- [87: How do `sideEffects`, `/* @__PURE__ */` and `/* #__NO_SIDE_EFFECTS__ */` help tree shaking?](#87-how-do-sideeffects--__pure__--and--__no_side_effects__--help-tree-shaking)
- [88: A team imports one icon from a library and the bundle grows by 500 KB. What do you check?](#88-a-team-imports-one-icon-from-a-library-and-the-bundle-grows-by-500-kb-what-do-you-check)
- [89: When does esbuild wrap modules instead of joining them into one scope?](#89-when-does-esbuild-wrap-modules-instead-of-joining-them-into-one-scope)
- [90: Why does esbuild warn about direct `eval`?](#90-why-does-esbuild-warn-about-direct-eval)
- [91: What is property mangling and what are the risks?](#91-what-is-property-mangling-and-what-are-the-risks)
- [92: How does esbuild's minifier compare to Terser, and what does it assume about your code?](#92-how-does-esbuilds-minifier-compare-to-terser-and-what-does-it-assume-about-your-code)
- [93: How does syntax lowering work, and how can you tune it with `supported`?](#93-how-does-syntax-lowering-work-and-how-can-you-tune-it-with-supported)
- [94: What are the rules for top-level `await` in esbuild?](#94-what-are-the-rules-for-top-level-await-in-esbuild)
- [95: What is `useDefineForClassFields` and why can it change behavior?](#95-what-is-usedefineforclassfields-and-why-can-it-change-behavior)
- [96: How does esbuild handle TypeScript enums and namespaces?](#96-how-does-esbuild-handle-typescript-enums-and-namespaces)
- [97: What are the known problems with code splitting in esbuild?](#97-what-are-the-known-problems-with-code-splitting-in-esbuild)
- [98: What should you know about CSS handling in esbuild beyond basic bundling?](#98-what-should-you-know-about-css-handling-in-esbuild-beyond-basic-bundling)
- [99: What security issues should you know about the esbuild dev server?](#99-what-security-issues-should-you-know-about-the-esbuild-dev-server)
- [100: What supply chain concerns are there with installing esbuild?](#100-what-supply-chain-concerns-are-there-with-installing-esbuild)
- [101: How do you proxy API requests while using the esbuild dev server?](#101-how-do-you-proxy-api-requests-while-using-the-esbuild-dev-server)
- [102: How would you bundle a Node.js app for AWS Lambda with esbuild?](#102-how-would-you-bundle-a-nodejs-app-for-aws-lambda-with-esbuild)
- [103: How do you use esbuild in a monorepo?](#103-how-do-you-use-esbuild-in-a-monorepo)
- [104: How do you find and fix duplicate packages in a bundle?](#104-how-do-you-find-and-fix-duplicate-packages-in-a-bundle)
- [105: How do you cache expensive work in a plugin across rebuilds?](#105-how-do-you-cache-expensive-work-in-a-plugin-across-rebuilds)
- [106: A NestJS app breaks when built with esbuild because of `emitDecoratorMetadata`. What can you do?](#106-a-nestjs-app-breaks-when-built-with-esbuild-because-of-emitdecoratormetadata-what-can-you-do)
- [107: Why do file hashes change for files you didn't touch?](#107-why-do-file-hashes-change-for-files-you-didnt-touch)
- [108: How do you handle source maps for production?](#108-how-do-you-handle-source-maps-for-production)
- [109: The bundled app behaves differently from the unbundled code. How do you debug it?](#109-the-bundled-app-behaves-differently-from-the-unbundled-code-how-do-you-debug-it)
- [110: The build takes 20 seconds with esbuild. What's likely going on?](#110-the-build-takes-20-seconds-with-esbuild-whats-likely-going-on)
- [111: How do you handle Node.js built-ins in a browser bundle?](#111-how-do-you-handle-nodejs-built-ins-in-a-browser-bundle)
- [112: How do you bundle web workers with esbuild?](#112-how-do-you-bundle-web-workers-with-esbuild)
- [113: Does esbuild support import attributes?](#113-does-esbuild-support-import-attributes)
- [114: How do you use esbuild to remove debug-only code from production builds?](#114-how-do-you-use-esbuild-to-remove-debug-only-code-from-production-builds)
- [115: What do you need to think about when building a library (not an app) with esbuild?](#115-what-do-you-need-to-think-about-when-building-a-library-not-an-app-with-esbuild)
- [116: What do `charset` and `lineLimit` do, and when do they matter?](#116-what-do-charset-and-linelimit-do-and-when-do-they-matter)
- [117: How does esbuild compare to Webpack, Rollup, Rolldown and SWC, and when would you not use it?](#117-how-does-esbuild-compare-to-webpack-rollup-rolldown-and-swc-and-when-would-you-not-use-it)
- [118: How do you use esbuild from Go?](#118-how-do-you-use-esbuild-from-go)
- [119: How would you use esbuild's `transform` API inside a test runner or custom loader?](#119-how-would-you-use-esbuilds-transform-api-inside-a-test-runner-or-custom-loader)
- [120: How would you design a production build setup for a single-page app using only esbuild?](#120-how-would-you-design-a-production-build-setup-for-a-single-page-app-using-only-esbuild)

---

# Easy Questions (1-40)

## 1: What is esbuild?

esbuild is a JavaScript and TypeScript bundler and minifier. It takes your source files, follows the imports, and outputs one or more files that a browser or Node.js can run. It can also just transform a single file (for example TypeScript to JavaScript) without bundling.

It was created by Evan Wallace and is written in Go, which is a big part of why it is so much faster than older tools like Webpack or Rollup.

## 2: Why is esbuild so fast?

A few reasons:

- It is written in Go and compiled to native code, so it doesn't pay the cost of starting and warming up a JavaScript engine.
- It uses many CPU cores at once. Parsing, printing and source map generation run in parallel.
- It does very few passes over the code. Most of the work happens in about three full passes over the AST, and the data stays in memory the whole time.
- It was written from scratch with speed in mind and doesn't depend on third-party parsers or plugins for core features.

A typical result is that a build which takes 30+ seconds in Webpack takes well under a second in esbuild.

## 3: How do you install esbuild?

```bash
npm install --save-dev --save-exact esbuild
```

Using `--save-exact` is recommended because esbuild is still on 0.x versions, and minor versions (0.27 to 0.28 for example) can contain breaking changes. After installing you can run it with `npx esbuild` or from an npm script.

## 4: How do you bundle a file with the esbuild CLI?

```bash
npx esbuild src/app.ts --bundle --outfile=dist/app.js
```

`src/app.ts` is the entry point, `--bundle` tells esbuild to follow the imports and put everything in one file, and `--outfile` is where the result goes. Without `--bundle`, esbuild only transforms that one file and leaves the `import` statements as they are.

## 5: What are the ways to use esbuild?

There are three main ways:

- **CLI**: `esbuild` command with flags. Good for simple builds and npm scripts.
- **JavaScript API**: `import * as esbuild from 'esbuild'` in Node.js. Good when you need plugins or more logic in the build.
- **Go API**: `github.com/evanw/esbuild/pkg/api` if your tooling is written in Go.

There is also `esbuild-wasm`, a WebAssembly build that runs in the browser or in places where the native binary can't run.

## 6: How do you run a build from JavaScript?

```js
import * as esbuild from "esbuild";

await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outfile: "dist/app.js",
});
```

`build()` returns a promise with the result, which includes `errors`, `warnings` and, if you asked for them, `metafile` and `outputFiles`. If the build fails, the promise rejects with an error that has `errors` and `warnings` arrays.

## 7: What is the difference between `build` and `transform`?

`build` works on files on disk. It can bundle, resolve imports, use plugins, and write output files.

`transform` works on a single string of code. It doesn't touch the file system, doesn't resolve imports and can't bundle. It's useful when another tool already has the code in memory and just needs it converted, for example TypeScript to JavaScript or minified.

```js
const result = await esbuild.transform("let x: number = 1", { loader: "ts" });
console.log(result.code); // let x = 1;
```

## 8: What is an entry point?

An entry point is a file where esbuild starts the build. When bundling, esbuild reads the entry point, follows every `import` and `require` from it, and puts all of the reached code into the output.

You can pass several entry points. Each one gets its own output file:

```bash
npx esbuild src/home.ts src/admin.ts --bundle --outdir=dist
```

## 9: What is the difference between `outfile` and `outdir`?

`outfile` is used when there is exactly one output file. `outdir` is a folder, and is needed when there are several entry points, when code splitting is on, or when the build produces extra files like images or CSS next to the JavaScript.

You can't use both at the same time.

## 10: What output formats does esbuild support?

Three formats:

- **`iife`**: wraps the code in a function that runs right away. For `<script>` tags in old-style pages.
- **`cjs`**: CommonJS, with `require` and `module.exports`. For Node.js.
- **`esm`**: ES modules, with `import` and `export`. For modern browsers, Node.js and other bundlers.

```bash
npx esbuild src/index.ts --bundle --format=esm --outfile=dist/index.js
```

If you don't set it and you're bundling, the default is `iife` for the browser platform and `cjs` for the node platform.

## 11: What does the `platform` option do?

`platform` tells esbuild where the code will run. It can be `browser` (default), `node`, or `neutral`.

With `node`, built-in modules like `fs` and `path` are marked as external, the default format becomes `cjs`, and package resolution prefers Node-style fields. With `browser`, esbuild prefers the `browser` field in `package.json`. `neutral` sets almost nothing for you, which is useful for code meant for other runtimes or libraries that will be bundled again later.

## 12: What does the `target` option do?

`target` tells esbuild which JavaScript and CSS versions the output must work in. Newer syntax is rewritten to older syntax when needed.

```bash
npx esbuild app.js --bundle --target=es2020,chrome100,safari15 --outfile=out.js
```

For example, with a target that doesn't support `??`, esbuild turns `a ?? b` into a longer expression. If some syntax can't be lowered to your target, esbuild reports an error instead of producing broken code.

## 13: How do you minify the output?

Add `--minify` (or `minify: true` in the API):

```bash
npx esbuild app.ts --bundle --minify --outfile=out.js
```

Minifying removes whitespace, shortens local variable names, and rewrites code into shorter forms. You can turn these on one by one with `minifyWhitespace`, `minifyIdentifiers` and `minifySyntax` if you only want some of them.

## 14: How do you generate source maps?

```bash
npx esbuild app.ts --bundle --sourcemap --outfile=out.js
```

This writes `out.js.map` and adds a `//# sourceMappingURL=` comment at the end of `out.js`. Other values:

- `inline`: the map is put inside the JS file as a base64 comment.
- `external`: writes the `.map` file but doesn't add the comment.
- `both`: inline and a separate file.

Source maps let the browser DevTools show your original TypeScript instead of the bundled code.

## 15: Does esbuild support TypeScript?

Yes, out of the box. Files ending in `.ts`, `.tsx`, `.mts` and `.cts` are understood without any config.

But esbuild only removes the types. It does **not** check them. A file with type errors will still build fine. To catch type errors you need to run `tsc --noEmit` separately, for example in CI or in your editor.

## 16: Does esbuild support JSX?

Yes. `.jsx` and `.tsx` files work out of the box. By default esbuild turns JSX into `React.createElement` calls. For the newer React JSX runtime, use:

```bash
npx esbuild app.jsx --bundle --jsx=automatic --outfile=out.js
```

With `jsx: 'automatic'`, esbuild imports from `react/jsx-runtime` for you, so you don't need `import React` in every file. If you use a `.js` file with JSX in it, you need to tell esbuild with `--loader:.js=jsx`.

## 17: What is a loader in esbuild?

A loader tells esbuild how to read a file type. Common loaders:

- `js`, `jsx`, `ts`, `tsx`: source code.
- `json`: parsed into an object.
- `css`: CSS file.
- `text`: file content as a string.
- `file`: copies the file to the output folder and gives you its URL.
- `dataurl`: puts the file inline as a `data:` URL.
- `base64`, `binary`: file content as base64 string or `Uint8Array`.
- `copy`: copies the file as-is.
- `empty`: treats the file as empty.

Loaders are chosen by file extension. You can change them:

```bash
npx esbuild app.js --bundle --loader:.png=file --loader:.svg=text --outdir=dist
```

## 18: How do you import a JSON file?

Just import it. The `json` loader is on by default for `.json` files:

```js
import pkg from "./package.json";
import { version } from "./package.json";
console.log(pkg.name, version);
```

Named imports work for top-level keys, and when bundling with tree shaking, unused top-level keys can be removed.

## 19: Can esbuild bundle CSS?

Yes. You can use a CSS file as an entry point, and esbuild follows its `@import` rules and `url()` references. You can also import CSS from JavaScript:

```js
import "./styles.css";
```

When you do that, esbuild creates a separate CSS file next to the JavaScript output (for example `app.js` and `app.css`). It doesn't inject the CSS into the page; you still need a `<link>` tag for it. esbuild also minifies CSS and lowers some newer CSS syntax for older browsers.

## 20: What does `--bundle` actually do?

Bundling means taking a file and all of its imports, recursively, and joining them into the output. Without bundling, each file is transformed on its own and imports are left untouched.

Bundling is off by default. You almost always want it on for browser apps, because it cuts the number of network requests and enables tree shaking.

## 21: What is tree shaking?

Tree shaking means removing code that is never used. If you import one function from a library with fifty functions, the other forty-nine can be left out of the bundle.

esbuild does tree shaking automatically when bundling. It works best with ES modules (`import`/`export`), because they are static. CommonJS (`require`) is much harder to analyze, so CommonJS code is mostly kept as a whole.

## 22: What is an external module?

An external module is an import that esbuild leaves as is instead of putting it into the bundle. It stays as an `import` or `require` in the output and will be loaded at runtime.

```bash
npx esbuild server.ts --bundle --platform=node --external:pg --outfile=dist/server.js
```

This is common for Node.js packages with native code, or for libraries where you want the user to install the dependency themselves.

## 23: How do you mark all npm packages as external?

Use `packages: 'external'`:

```bash
npx esbuild src/index.ts --bundle --platform=node --packages=external --outfile=dist/index.js
```

esbuild then bundles only your own code and keeps every import that looks like a package (anything not starting with `.` or `/`) as an import. This is useful for Node.js servers and libraries, where `node_modules` will be available at runtime anyway.

## 24: What is watch mode?

Watch mode rebuilds automatically when you save a file.

```bash
npx esbuild app.ts --bundle --outfile=out.js --watch
```

In the JavaScript API, you create a context and call `watch()`:

```js
const ctx = await esbuild.context({
  entryPoints: ["app.ts"],
  bundle: true,
  outfile: "out.js",
});
await ctx.watch();
```

Rebuilds are incremental, so they are usually much faster than the first build.

## 25: Does esbuild have a dev server?

Yes, a simple one. It serves your files and builds on each request, so you always get the latest code.

```bash
npx esbuild src/app.ts --bundle --outdir=www/js --servedir=www
```

This serves the `www` folder, and requests for `www/js/app.js` get the freshly built bundle from memory. It's meant for local development only, not for production.

## 26: Does esbuild support hot module replacement (HMR)?

No. esbuild has live reload, but not HMR. Live reload means the whole page refreshes when the code changes. HMR, which swaps modules without losing page state, is not built in.

If you need HMR, tools like Vite give you that. For CSS, you can get close to hot reload with esbuild by listening to the change event and swapping the `<link>` tag instead of reloading the page.

## 27: How do you enable live reload with the esbuild dev server?

Add this to your app code (only in development):

```js
new EventSource("/esbuild").addEventListener("change", () => location.reload());
```

And run esbuild with both watch and serve:

```js
const ctx = await esbuild.context({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outdir: "www/js",
});
await ctx.watch();
await ctx.serve({ servedir: "www" });
```

When a rebuild finishes, the server sends a `change` event on `/esbuild`, and the page reloads.

## 28: What does the `define` option do?

`define` replaces global identifiers with constant values at build time. The most common use is setting the environment:

```bash
npx esbuild app.js --bundle --define:process.env.NODE_ENV=\"production\" --outfile=out.js
```

```js
await esbuild.build({
  entryPoints: ["app.js"],
  bundle: true,
  define: { "process.env.NODE_ENV": '"production"' },
  outfile: "out.js",
});
```

Note the extra quotes: the value must be valid JSON or an identifier, so a string needs to be `'"production"'`. After the replacement, code like `if (process.env.NODE_ENV !== 'production')` becomes dead code and is removed by the minifier.

## 29: How do you use environment variables in a browser bundle?

The browser has no `process.env`, so you replace those values at build time with `define`:

```js
await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outfile: "dist/app.js",
  define: {
    "process.env.API_URL": JSON.stringify(
      process.env.API_URL ?? "http://localhost:3000",
    ),
  },
});
```

`JSON.stringify` adds the quotes for you. Only put values in the bundle that are safe to be public, because anyone can read them in the final JavaScript.

## 30: Does esbuild check TypeScript types?

No. This is one of the most common surprises. esbuild strips type annotations and outputs JavaScript, but it never runs the TypeScript type checker. That's part of why it's fast.

The usual setup is: esbuild for building, and `tsc --noEmit` for type checking, either in parallel during development or as a separate CI step.

```json
{
  "scripts": {
    "build": "esbuild src/index.ts --bundle --outfile=dist/index.js",
    "typecheck": "tsc --noEmit"
  }
}
```

## 31: How do you import an image with esbuild?

Set a loader for the image extension. With the `file` loader, esbuild copies the image to the output folder and the import gives you its path:

```js
import logo from "./logo.png";
document.querySelector("img").src = logo;
```

```bash
npx esbuild app.js --bundle --loader:.png=file --outdir=dist
```

For small images you can use `dataurl` instead, which inlines the image into the JavaScript as a `data:` URL. That saves a request but makes the bundle bigger.

## 32: What does `--log-level` do?

It controls how much esbuild prints to the terminal. The values are `verbose`, `debug`, `info`, `warning`, `error` and `silent`.

The CLI defaults to `info`, which prints a short summary of output files. The JavaScript API defaults to `warning`, so it only prints warnings and errors. You'll often set `logLevel: 'info'` in API scripts so you can see what was built.

## 33: How do you build several entry points at once?

Pass them all, and use `outdir`:

```js
await esbuild.build({
  entryPoints: ["src/home.ts", "src/admin.ts", "src/login.ts"],
  bundle: true,
  outdir: "dist",
});
```

You can also use an object to choose the output name, or a glob pattern like `src/pages/*.ts`. esbuild expands globs itself, which helps on Windows where the shell doesn't.

```js
entryPoints: { main: 'src/index.ts', worker: 'src/worker.ts' }
```

## 34: Can esbuild bundle Node.js code?

Yes. Set `platform: 'node'`:

```bash
npx esbuild src/server.ts --bundle --platform=node --target=node22 --outfile=dist/server.js
```

Bundling a Node.js app into one file is useful for serverless functions (smaller uploads, faster cold starts) and for CLI tools. Packages with native `.node` addons usually need to be marked as external, since esbuild can't bundle compiled binaries into JavaScript.

## 35: What does `banner` and `footer` do?

They add text to the start or end of each output file. A common use is adding a license comment or a shebang line:

```js
await esbuild.build({
  entryPoints: ["src/cli.ts"],
  bundle: true,
  platform: "node",
  outfile: "dist/cli.js",
  banner: { js: "#!/usr/bin/env node" },
});
```

You set them per file type, for example `banner: { js: '...', css: '...' }`. Note that esbuild already keeps a shebang that's at the top of the entry file, so you only need the banner if the entry doesn't have one.

## 36: What does `--global-name` do?

When the format is `iife`, `globalName` puts the entry point's exports on a global variable:

```bash
npx esbuild src/lib.ts --bundle --format=iife --global-name=MyLib --outfile=dist/lib.js
```

After loading `lib.js` with a `<script>` tag, you can call `MyLib.someFunction()` from the page. Without it, the exports are not reachable from outside the bundle. It can also be a dotted path like `window.MyLib`.

## 37: Can esbuild compile code for old browsers like IE11?

Only partly. esbuild can lower a lot of modern syntax, but it doesn't fully support converting ES6+ syntax to ES5. If your target is `es5` and the code uses things like `class`, `let`, or generators, esbuild will report an error for the syntax it can't convert.

It also doesn't add polyfills. If you use `Array.prototype.includes` or `Promise`, you must add polyfills yourself (for example with core-js). For real legacy browser support, people usually run Babel or SWC after or instead of esbuild.

## 38: What is the `write` option?

By default, `build()` writes the output files to disk. With `write: false`, it keeps them in memory and returns them in `result.outputFiles`:

```js
const result = await esbuild.build({
  entryPoints: ["app.ts"],
  bundle: true,
  outfile: "out.js",
  write: false,
});

for (const file of result.outputFiles) {
  console.log(file.path, file.text.length);
}
```

Each file has `path`, `contents` (a `Uint8Array`), `text` and `hash`. This is handy for tests, custom servers, or when you want to change the output before saving it.

## 39: Which popular tools use esbuild?

- **Angular CLI**: the `application` builder (default since Angular 17) uses esbuild.
- **Vite**: up to Vite 7, esbuild handled dependency pre-bundling, TypeScript/JSX transforms in dev, and minification. Vite 8 moved to Rolldown and Oxc for most of this.
- **tsx**: runs TypeScript files in Node.js using esbuild.
- **tsup**: a library bundler built on top of esbuild.
- **AWS CDK**: the `NodejsFunction` construct bundles Lambda code with esbuild.

Many teams also use esbuild directly through small build scripts.

## 40: What does `esbuild --version` show and why does the version matter?

It prints the installed esbuild version, like `0.28.2`. Versions matter more than usual with esbuild, because it hasn't hit 1.0 yet. The project uses the second number (the `x` in `0.x.y`) for breaking changes, so going from 0.27 to 0.28 can break your build, while 0.28.1 to 0.28.2 should be safe.

That's why the docs recommend pinning an exact version and reading the changelog before upgrading.

# Moderate Questions (41-80)

## 41: What is a build context and why would you use one?

`esbuild.context()` creates a long-lived build object that keeps its state between builds. It has these methods:

- `rebuild()`: build again, reusing cached work from the last build.
- `watch()`: rebuild on file changes.
- `serve()`: start the dev server.
- `cancel()`: stop the current build.
- `dispose()`: free the resources when you're done.

```js
const ctx = await esbuild.context({
  entryPoints: ["app.ts"],
  bundle: true,
  outfile: "out.js",
});
await ctx.rebuild();
await ctx.rebuild(); // faster, files that didn't change are not parsed again
await ctx.dispose();
```

Use it whenever you build the same thing more than once, like in a dev tool or a test runner. For a single production build, plain `build()` is enough.

## 42: Why should you call `dispose()` on a context?

A context holds memory, file watchers and maybe a running HTTP server. If you don't dispose it, those stay alive and your Node.js process may never exit.

```js
const ctx = await esbuild.context(options);
try {
  await ctx.rebuild();
} finally {
  await ctx.dispose();
}
```

In long-running tools, forgetting `dispose()` when restarting builds is a common cause of memory leaks.

## 43: How do you write a simple esbuild plugin?

A plugin is an object with a `name` and a `setup` function. Inside `setup` you register callbacks like `onResolve` and `onLoad`:

```js
const envPlugin = {
  name: "env",
  setup(build) {
    build.onResolve({ filter: /^env$/ }, (args) => ({
      path: args.path,
      namespace: "env-ns",
    }));

    build.onLoad({ filter: /.*/, namespace: "env-ns" }, () => ({
      contents: JSON.stringify({ MODE: process.env.MODE ?? "dev" }),
      loader: "json",
    }));
  },
};

await esbuild.build({
  entryPoints: ["app.js"],
  bundle: true,
  outfile: "out.js",
  plugins: [envPlugin],
});
```

Now `import env from 'env'` in your code gives you that object.

## 44: What is the difference between `onResolve` and `onLoad`?

- **`onResolve`** runs when esbuild sees an import path. It decides where that path points: a file path, an external module, or a path in a custom namespace.
- **`onLoad`** runs when esbuild needs the content of a resolved path. It returns the file contents and the loader to use.

So `onResolve` answers "which module is this?" and `onLoad` answers "what is inside it?". Both take a `filter` regex, and optionally a `namespace`, to decide which paths they handle. If a callback returns nothing, esbuild moves on to the next plugin and finally to its own default behavior.

## 45: What is a namespace in an esbuild plugin?

Every module in esbuild has a path and a namespace. Normal files on disk are in the `file` namespace. Plugins can put modules in their own namespace, which is useful for virtual modules that don't exist on disk.

```js
build.onResolve({ filter: /^virtual:config$/ }, (args) => ({
  path: args.path,
  namespace: "virtual",
}));

build.onLoad({ filter: /.*/, namespace: "virtual" }, () => ({
  contents: "export default { debug: true }",
  loader: "js",
}));
```

The namespace also stops other plugins and the default loader from trying to read that path from disk.

## 46: Why does the `filter` in a plugin have to be a regex?

esbuild uses the filter to decide, inside Go, whether to call your JavaScript callback at all. Calling into JavaScript is slow compared to the rest of esbuild, so a tight filter skips most of those calls.

```js
// Good: only .yaml files go to JavaScript
build.onLoad({ filter: /\.ya?ml$/ }, loadYaml);

// Bad: every single file goes to JavaScript
build.onLoad({ filter: /.*/ }, (args) => {
  if (!args.path.endsWith(".yaml")) return; /* ... */
});
```

The filter uses Go's regex engine, which doesn't support lookahead, lookbehind or backreferences. If your regex uses those, esbuild throws an error.

## 47: What are `onStart` and `onEnd` used for?

`onStart` runs at the start of each build and `onEnd` runs when each build finishes. They are useful in watch mode, where builds keep happening:

```js
const timingPlugin = {
  name: "timing",
  setup(build) {
    let start;
    build.onStart(() => {
      start = Date.now();
    });
    build.onEnd((result) => {
      console.log(
        `build ended with ${result.errors.length} errors in ${Date.now() - start}ms`,
      );
    });
  },
};
```

`onEnd` gets the build result, so you can use it to send notifications, copy files, or print a custom summary. There is also `onDispose` for cleanup when the context is disposed.

## 48: How do you use `build.resolve()` inside a plugin?

`build.resolve()` asks esbuild to resolve a path the normal way, including other plugins. It's useful when your plugin wants to redirect an import but still let esbuild find the real file:

```js
build.onResolve({ filter: /^@app\// }, async (args) => {
  const result = await build.resolve(args.path.replace("@app/", "./src/"), {
    kind: args.kind,
    resolveDir: args.resolveDir,
  });
  if (result.errors.length > 0) return { errors: result.errors };
  return { path: result.path };
});
```

Be careful not to make the plugin resolve the same path back into itself, or you get an endless loop. Pass something in `pluginData` or change the path to avoid that.

## 49: How do path aliases from `tsconfig.json` work with esbuild?

esbuild reads `tsconfig.json` and respects `paths` and `baseUrl` when bundling. So this works without a plugin:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```

```ts
import { formatDate } from "@/utils/date";
```

There is also the `alias` option, which replaces whole package names (for example `alias: { 'lodash': 'lodash-es' }`). `alias` only works on package-style names, not relative paths, so for `@/` style paths you normally rely on `tsconfig.json`.

## 50: Which `tsconfig.json` settings does esbuild read?

esbuild reads only the settings that change how code is converted, not type checking settings. The main ones:

- `paths` and `baseUrl` for import resolution.
- `jsx`, `jsxFactory`, `jsxFragmentFactory`, `jsxImportSource`.
- `experimentalDecorators` and `useDefineForClassFields`.
- `verbatimModuleSyntax` (and the older `preserveValueImports` and `importsNotUsedAsValues`).
- `alwaysStrict` and `strict`, for whether to add `"use strict"`.
- `extends`, so shared base configs work.

It doesn't use `tsconfig`'s `target` as the output target. You set that with esbuild's own `target` option. You can point to a different file with `tsconfig: 'tsconfig.build.json'` or pass the settings inline with `tsconfigRaw`.

## 51: Why do you need `isolatedModules` when using esbuild with TypeScript?

esbuild compiles each file on its own, without type info from other files. Some TypeScript features need that info. For example, when you write `export { User } from './types'`, esbuild can't tell whether `User` is a type (which should be removed) or a value.

Turning on `isolatedModules` (or `verbatimModuleSyntax`) in `tsconfig.json` makes `tsc` report code that a single-file compiler can't handle. The fix is usually to write `export type { User }` or `import type`. esbuild doesn't need the flag itself, but your type checker should use it so you catch these problems early.

## 52: How does esbuild handle CSS modules?

Files ending in `.module.css` use the `local-css` loader by default. Class names in them are made unique, and importing the file gives you an object with the generated names:

```css
/* button.module.css */
.primary {
  background: blue;
}
```

```js
import styles from "./button.module.css";
button.className = styles.primary; // something like "button_primary"
```

You can switch any file to this behavior with `loader: { '.css': 'local-css' }`. Inside a module file, `:global(.name)` keeps a class name unchanged.

## 53: How do you use Sass, Less or PostCSS with esbuild?

esbuild only understands plain CSS. For anything else you need a plugin. Common ones from the community:

- `esbuild-sass-plugin` for Sass/SCSS.
- `esbuild-plugin-less` for Less.
- `esbuild-style-plugin` or a custom plugin for PostCSS (Tailwind, Autoprefixer and so on).

A custom PostCSS plugin is short: an `onLoad` for `\.css$` that reads the file, runs PostCSS on it and returns `{ contents: result.css, loader: 'css' }`. Keep in mind that plugins run in JavaScript and slow the build down, so only add the ones you need.

## 54: How does code splitting work in esbuild?

Code splitting pulls code shared between entry points, and code behind dynamic `import()`, into separate chunk files:

```bash
npx esbuild src/home.ts src/admin.ts --bundle --splitting --format=esm --outdir=dist
```

If both pages use the same library, it goes into one shared chunk instead of being copied twice. Code splitting only works with `format: 'esm'` and needs `outdir`. It's been marked as a work in progress in the docs for a long time, so test it well in your app.

## 55: How do dynamic imports work in esbuild?

`import('./page.js')` with a string literal is bundled as a separate module. With `--splitting`, it becomes its own chunk loaded on demand. Without splitting, the code is put into the main bundle and the `import()` just resolves to it.

esbuild also supports some simple patterns with variables, as long as the path starts with a known folder:

```js
const mod = await import(`./locales/${lang}.js`);
```

esbuild turns this into a lookup of every file matching `./locales/*.js`. Fully dynamic paths like `import(someVariable)` can't be bundled; esbuild leaves them as they are and shows a warning.

## 56: How do you control output file names?

Use `entryNames`, `chunkNames` and `assetNames`. They take a template with placeholders like `[name]`, `[hash]`, `[dir]` and `[ext]`:

```js
await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  splitting: true,
  format: "esm",
  outdir: "dist",
  entryNames: "[name]-[hash]",
  chunkNames: "chunks/[name]-[hash]",
  assetNames: "assets/[name]-[hash]",
  loader: { ".png": "file" },
});
```

Adding `[hash]` gives each file a name based on its content, which lets you cache files forever on a CDN. When content changes, the name changes too.

## 57: How do you find the hashed file names after a build to put them in HTML?

esbuild doesn't create HTML files for you. Ask for a `metafile` and read the output names from it:

```js
const result = await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outdir: "dist",
  entryNames: "[name]-[hash]",
  metafile: true,
});

const outputs = result.metafile.outputs;
const js = Object.keys(outputs).find(
  (p) => outputs[p].entryPoint === "src/app.ts",
);
// write js into your index.html template
```

There are also community plugins like `@craftamap/esbuild-plugin-html` that do this for you.

## 58: What is the metafile?

The metafile is a JSON description of the build. With `metafile: true`, the result has a `metafile` object with two parts:

- `inputs`: every input file, its size and what it imports.
- `outputs`: every output file, its size, which inputs went into it and how many bytes each one added.

```bash
npx esbuild app.ts --bundle --outfile=out.js --metafile=meta.json
```

You can upload the file to esbuild's online bundle analyzer (esbuild.github.io/analyze) to see a chart of what's taking up space.

## 59: How do you see what makes your bundle large?

Three easy options:

1. Use `--analyze` on the CLI to print a size report in the terminal.
2. In the API, use `analyzeMetafile`:

   ```js
   const result = await esbuild.build({ ...options, metafile: true });
   console.log(await esbuild.analyzeMetafile(result.metafile));
   ```

3. Upload the metafile to esbuild's online analyzer.

Look for big libraries you didn't expect, the same package showing up twice (for example two versions of `lodash`), and CommonJS packages that can't be tree shaken.

## 60: How do you remove `console.log` and `debugger` from production builds?

Use `drop`:

```js
await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  minify: true,
  drop: ["console", "debugger"],
  outfile: "dist/app.js",
});
```

This removes all `console.*` calls (including their arguments, so any side effects in the arguments are gone too) and all `debugger` statements. If you want to remove only some calls, like `console.log` but not `console.error`, use `pure: ['console.log']` instead, which lets the minifier remove those calls when their result isn't used.

## 61: What does `inject` do?

`inject` automatically imports a file into every file in the bundle where it's needed. It's mostly used for shims of globals:

```js
// process-shim.js
export const process = { env: {} };
```

```js
await esbuild.build({
  entryPoints: ["app.js"],
  bundle: true,
  inject: ["./process-shim.js"],
  outfile: "out.js",
});
```

Now any code that uses the global `process` gets the shim instead. A classic use was injecting `React` for old JSX code, but with `jsx: 'automatic'` that's no longer needed.

## 62: How does esbuild handle CommonJS and ES module mixing?

esbuild lets you `import` a CommonJS module and `require` an ES module. To make that work, it wraps CommonJS modules in a small helper (`__commonJS`) and converts between the two shapes with helpers like `__toESM`.

What a default import of a CommonJS module gives you is the main tricky part. esbuild follows Node.js: in most cases `import x from 'cjs-lib'` gives you `module.exports`, but if the module sets `__esModule` (a marker that Babel and TypeScript add), you get `exports.default` instead. Mixing the two works, but CommonJS code can't be tree shaken well, so ES module versions of packages are better when they exist.

## 63: What are `mainFields` and `conditions`?

They control which file esbuild picks from a package's `package.json`.

- **`mainFields`** lists old-style fields to check in order. For the browser platform the default is `browser,module,main`; for node it's `main,module`.
- **`conditions`** adds custom conditions for the `exports` field. esbuild always uses `default`, uses `import` or `require` depending on the import style, and `browser` or `node` depending on the platform. If you don't set any custom conditions, it also adds `module`.

```js
await esbuild.build({
  entryPoints: ["app.js"],
  bundle: true,
  conditions: ["development"],
  outfile: "out.js",
});
```

If a package has an `exports` field, esbuild uses it and ignores `mainFields` for that package.

## 64: How do you build a library that ships both ESM and CommonJS?

Run two builds and point to them from `package.json`:

```js
const shared = {
  entryPoints: ["src/index.ts"],
  bundle: true,
  packages: "external",
  sourcemap: true,
};

await Promise.all([
  esbuild.build({ ...shared, format: "esm", outfile: "dist/index.mjs" }),
  esbuild.build({ ...shared, format: "cjs", outfile: "dist/index.cjs" }),
]);
```

```json
{
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    }
  }
}
```

esbuild doesn't create `.d.ts` files, so you run `tsc --emitDeclarationOnly` for the types. Tools like `tsup` wrap all of this in one command.

## 65: How do you create type declaration files (`.d.ts`) with esbuild?

You can't; esbuild doesn't generate them. Because it doesn't do type checking, it doesn't have the type info needed.

The usual way is to run the TypeScript compiler just for declarations:

```bash
tsc --emitDeclarationOnly --declaration --outDir dist
```

Or use a tool that does both, like `tsup` (esbuild for the JS plus its own `.d.ts` step), or roll up the declarations into one file with API Extractor or `rollup-plugin-dts`.

## 66: How does esbuild handle decorators?

esbuild supports both kinds:

- **TypeScript experimental decorators** when `experimentalDecorators: true` is set in `tsconfig.json`. These are the ones used by Angular, NestJS and TypeORM.
- **Standard JavaScript decorators** (the TC39 version) otherwise. esbuild lowers them for targets that don't support them.

What esbuild does **not** support is `emitDecoratorMetadata`, because that needs type info. Libraries that depend on `reflect-metadata` and type-based injection, like NestJS, often break with plain esbuild. People fix it with a plugin that runs `tsc` or SWC on those files, or use SWC for that project instead.

## 67: What does `keepNames` do?

Minification renames functions and classes, so `function UserService() {}` might become `function a() {}`. That breaks code that reads `.name`, like some logging, error messages or dependency injection.

`keepNames: true` adds small helper calls that set the original `name` property back:

```bash
npx esbuild app.ts --bundle --minify --keep-names --outfile=out.js
```

The names are still short in the code, but `UserService.name` returns `"UserService"`. It makes the bundle a bit bigger.

## 68: How do legal comments work?

Legal comments are comments that start with `//!` or `/*!`, or contain `@license` or `@preserve`. esbuild keeps them by default even when minifying. The `legalComments` option controls where they go:

- `eof`: moved to the end of the file (the default when bundling).
- `inline`: kept where they are.
- `linked`: moved to a `.LEGAL.txt` file with a link comment.
- `external`: moved to a `.LEGAL.txt` file with no link.
- `none`: removed.

Removing them may break the license terms of the libraries you use, so check before setting `none`.

## 69: How do you run esbuild in Node.js scripts that also need to work in CI?

Put the build in a plain `build.mjs` file and run it with Node:

```js
// build.mjs
import * as esbuild from "esbuild";

const isProd = process.argv.includes("--prod");

await esbuild.build({
  entryPoints: ["src/index.ts"],
  bundle: true,
  minify: isProd,
  sourcemap: !isProd,
  outdir: "dist",
  logLevel: "info",
});
```

```json
{ "scripts": { "build": "node build.mjs --prod", "dev": "node build.mjs" } }
```

If the build fails, `build()` rejects, the error is printed, and Node exits with a non-zero code, which makes CI fail as it should.

## 70: How do you handle `__dirname` and `require` in an ESM bundle for Node.js?

ES modules don't have `__dirname`, `__filename` or `require`. If a bundled CommonJS package uses `require('some-builtin')`, esbuild can show "Dynamic require of 'x' is not supported" at runtime. A common fix is a banner:

```js
await esbuild.build({
  entryPoints: ["src/server.ts"],
  bundle: true,
  platform: "node",
  format: "esm",
  outfile: "dist/server.mjs",
  banner: {
    js: [
      "import { createRequire } from 'node:module';",
      "const require = createRequire(import.meta.url);",
    ].join("\n"),
  },
});
```

In your own code, use `import.meta.dirname` and `import.meta.filename` (Node 20.11+) instead of `__dirname` and `__filename`.

## 71: What does the `jsx` option accept and when do you use each value?

- **`transform`** (default): JSX becomes `React.createElement(...)` calls. You can change the function with `jsxFactory` and `jsxFragment`, for example `h` and `Fragment` for Preact.
- **`automatic`**: uses the new JSX runtime and imports from `react/jsx-runtime`. Set `jsxImportSource` for other libraries, like `preact` or `@emotion/react`.
- **`preserve`**: leaves JSX in the output, for when another tool will handle it later.

There is also `jsxDev: true`, which uses `react/jsx-dev-runtime` and adds file and line info for better React warnings in development.

## 72: How do you use esbuild to run TypeScript directly in Node.js?

esbuild itself doesn't run code, but tools built on it do. The most used is `tsx`:

```bash
npx tsx src/script.ts
npx tsx watch src/server.ts
```

You can also do a quick one-off build and run:

```bash
npx esbuild src/script.ts --bundle --platform=node --outfile=tmp/script.js && node tmp/script.js
```

Note that recent Node.js versions can run `.ts` files on their own by stripping types, but only for syntax that can be removed without changes (no enums or namespaces, for example). `tsx` handles all TypeScript syntax.

## 73: What is the difference between `esbuild` and `esbuild-wasm`?

`esbuild` uses a native binary for your OS and CPU. `esbuild-wasm` is the same code compiled to WebAssembly. It has the same API, but:

- It's several times slower, mostly because it doesn't use multiple cores as well.
- It works in the browser and in places where the native binary can't be installed.
- In the browser you must call `initialize()` first.

```js
import * as esbuild from "esbuild-wasm";

await esbuild.initialize({
  wasmURL: "https://unpkg.com/esbuild-wasm@0.28.2/esbuild.wasm",
});
const result = await esbuild.transform("const x: number = 1", { loader: "ts" });
```

It's used for online playgrounds and tools that compile code in the browser.

## 74: Why does esbuild sometimes fail after copying `node_modules` between machines?

esbuild installs a native binary for your exact OS and CPU, through an optional dependency like `@esbuild/darwin-arm64` or `@esbuild/linux-x64`. If you run `npm install` on a Mac and copy `node_modules` into a Linux Docker image, the Linux binary is missing and you get an error that the platform doesn't match.

The fix is to run `npm ci` inside the target environment (for example in the Dockerfile), and to not install with `--no-optional` / `--omit=optional`. Adding `node_modules` to `.dockerignore` stops it from being copied by accident.

## 75: How do you build an app that loads CSS, images and fonts?

Set loaders for each file type and use `outdir`:

```js
await esbuild.build({
  entryPoints: ["src/index.tsx"],
  bundle: true,
  outdir: "dist",
  loader: {
    ".png": "file",
    ".jpg": "file",
    ".svg": "file",
    ".woff2": "file",
  },
  assetNames: "assets/[name]-[hash]",
  publicPath: "/static",
});
```

CSS `url()` references to fonts and images are followed too, and the copied files get the same hashed names. `publicPath` puts a prefix in front of the asset URLs, which you need if the files are served from a CDN or a sub folder.

## 76: What is `outbase` and when do you need it?

When you have several entry points in different folders, esbuild keeps their folder structure in the output, starting from the lowest common folder. `outbase` lets you set that starting folder yourself:

```bash
npx esbuild src/pages/home/index.ts src/pages/about/index.ts \
  --bundle --outdir=dist --outbase=src
```

This creates `dist/pages/home/index.js` and `dist/pages/about/index.js`. Without `outbase`, the common folder is `src/pages`, so you'd get `dist/home/index.js` and `dist/about/index.js`. Setting it makes the output paths stable when you add or remove entry points.

## 77: How do you change the output file extension?

Use `outExtension`:

```js
await esbuild.build({
  entryPoints: ["src/index.ts"],
  bundle: true,
  format: "esm",
  platform: "node",
  outdir: "dist",
  outExtension: { ".js": ".mjs" },
});
```

This is common for Node.js packages, where `.mjs` and `.cjs` tell Node how to load the file no matter what `"type"` is set in `package.json`. If you use `outfile`, you can just give the file the extension you want.

## 78: How do you read esbuild errors and warnings in the API?

`build()` returns warnings in `result.warnings`. If there are errors, it throws, and the error has `errors` and `warnings` arrays. Each message has `text`, `location` (file, line, column, the line text), and `notes`.

```js
try {
  await esbuild.build(options);
} catch (e) {
  const messages = await esbuild.formatMessages(e.errors, {
    kind: "error",
    color: true,
  });
  console.error(messages.join("\n"));
  process.exit(1);
}
```

`formatMessages` prints them the same way the CLI does. Most of the time you don't need to do this, since esbuild already logs the messages based on `logLevel`.

## 79: How do you silence or turn a specific warning into an error?

Use `logOverride` with the warning's ID (it's shown in brackets in the message, like `[direct-eval]`):

```js
await esbuild.build({
  entryPoints: ["app.ts"],
  bundle: true,
  outfile: "out.js",
  logOverride: {
    "direct-eval": "silent",
    "unsupported-dynamic-import": "error",
  },
});
```

On the CLI it's `--log-override:direct-eval=silent`. This is better than raising the global `logLevel`, which hides every warning, not just the one you've decided is fine.

## 80: How would you migrate a simple Webpack project to esbuild?

A rough plan:

1. Write a `build.mjs` with the same entry points, output folder and `define` values as the Webpack config.
2. Replace loaders: TS/JSX work out of the box, plain CSS and CSS modules work, images and fonts use the `file` loader. Sass, PostCSS or SVG-as-component need plugins.
3. Replace `HtmlWebpackPlugin` with a small script or plugin that writes `index.html` using the metafile.
4. Replace `webpack-dev-server` with `ctx.serve()` and live reload. Note there's no HMR.
5. Add `tsc --noEmit` for types, since `ts-loader` type checking is gone.
6. Compare bundle sizes and test the app, especially places that rely on Webpack-only features like `require.context` or module federation.

Things that depend heavily on Webpack plugins may be easier to move to Vite or Rspack instead.

# Advanced Questions (81-120)

## 81: How does esbuild work internally, step by step?

At a high level a build has three stages:

1. **Scan**: starting from the entry points, esbuild resolves, reads and parses files. Each file is parsed on its own goroutine, so many files are parsed at the same time. Parsing, scope setup and symbol declaration are done in one pass over the source, and syntax lowering for the target happens right after.
2. **Link**: in one thread, esbuild connects imports to exports across files, works out tree shaking, decides which modules need wrappers, and splits code into chunks.
3. **Print**: each output file is generated (with minification and source maps) in parallel again.

The AST is created once and kept in memory, and there are no repeated "parse, print, parse again" steps between tools. This design, more than any single trick, is where the speed comes from.

## 82: How does the JavaScript API talk to the Go binary?

When you call `build()` the first time, the `esbuild` npm package starts the native binary as a child process and keeps it running. Requests and responses go over stdin/stdout using a small binary protocol. All builds in the same Node.js process share that one child process.

This has a few effects:

- The first call has a small startup cost, later calls are cheap.
- Plugin callbacks are messages sent back to Node.js, then the answer is sent to Go. That round trip is why JS plugins slow builds down.
- The child process keeps Node alive in some setups. `esbuild.stop()` shuts it down if you need a clean exit.

## 83: Why do JavaScript plugins slow esbuild down, and how do you keep them fast?

Everything inside esbuild runs in parallel in Go. A JS plugin callback has to send data to Node.js, run on the single JS thread, and send results back. If a callback runs for every file, the build becomes limited by that one thread.

Ways to keep it fast:

- Use a narrow `filter` regex so Go skips the call for files you don't care about.
- Use a `namespace` filter when you work with virtual modules.
- Cache expensive work (Babel, Sass) between rebuilds, keyed by path and file contents or mtime.
- If you write tooling in Go, Go plugins run in the same process and have no IPC cost.

A useful test is to build with and without your plugins and compare times.

## 84: What are the limits of `buildSync` and `transformSync`?

The sync APIs block the Node.js thread until the work is done. Because of that:

- They can't use plugins. Plugin callbacks need the JS thread, which is blocked.
- There is no `context`, `watch` or `serve` in sync form.
- They block everything else in the process, including servers.

They are fine for small scripts or places that require a sync answer, like old `require` hooks. In everything else, use the async APIs. They also run faster when you have several builds, because builds can run at the same time.

## 85: How do incremental rebuilds work?

A context keeps the results of the last build: file contents, parsed ASTs, resolver results and so on. On `rebuild()`, esbuild checks which files changed and only parses those again. Linking and printing still run, but they are fast compared to parsing.

```js
const ctx = await esbuild.context({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outdir: "dist",
});
const r1 = await ctx.rebuild(); // full build
const r2 = await ctx.rebuild(); // reuses unchanged files
```

Plugin results are not cached by esbuild. If your `onLoad` runs Sass for every file, it will run again on every rebuild unless you cache it yourself. That's often why a rebuild with plugins is much slower than one without.

## 86: How does esbuild watch mode detect file changes?

esbuild uses polling instead of OS file watching APIs like `inotify` or `FSEvents`. This works the same on all platforms and avoids problems with watcher limits and network drives.

To keep CPU use low, it doesn't check every file every time. It checks a random part of the files on each tick, and checks files that changed recently more often, so a change is noticed quickly but the whole tree is only fully scanned over a few seconds. The `delay` option (`--watch-delay`) adds a wait in milliseconds before rebuilding, which helps when an editor or another tool writes many files at once.

Plugins that read extra files (for example a config file) should return them in `watchFiles` or `watchDirs`, or watch mode won't know about them.

## 87: How do `sideEffects`, `/* @__PURE__ */` and `/* #__NO_SIDE_EFFECTS__ */` help tree shaking?

esbuild can only remove code if it's sure the code does nothing when it runs. These hints tell it that:

- **`"sideEffects": false`** in a package's `package.json` says importing a file from the package has no side effects. If nothing from a file is used, the whole file can be dropped. It can also be a list of files that do have side effects, like `["*.css"]`.
- **`/* @__PURE__ */`** before a call says that one call can be removed if its result isn't used:

  ```js
  export const Button = /* @__PURE__ */ createComponent("button");
  ```

- **`/* #__NO_SIDE_EFFECTS__ */`** before a function declaration says every call to that function is pure.

If these hints are wrong, esbuild will remove code that was needed, so library authors must be careful with them. `ignoreAnnotations: true` makes esbuild ignore them all when you suspect a package is lying.

## 88: A team imports one icon from a library and the bundle grows by 500 KB. What do you check?

Steps I'd take:

1. **Look at the metafile** (`--analyze` or the online analyzer) to see which files from the package were included.
2. **Check if the package is ESM.** If only a CommonJS build exists, or esbuild picks the `main` field over `module`, tree shaking mostly stops working. Check `exports` and `mainFields`.
3. **Check `sideEffects`.** Without `"sideEffects": false`, esbuild has to keep every file a barrel `index.js` touches if those files run top-level code.
4. **Look for top-level code** in the library, like `registerIcons(...)` calls or class static blocks, which count as side effects.
5. **Import a deeper path**, for example `lib/icons/Home` instead of `lib`, if the package supports it.

Often the fix is switching to the package's ESM build, using deep imports, or replacing the library with one that's built for tree shaking.

## 89: When does esbuild wrap modules instead of joining them into one scope?

Normally esbuild uses scope hoisting for ES modules: all modules are put into one flat scope, with names changed to avoid clashes. There are no wrapper functions, so the output is small and fast.

Some modules must be wrapped in a function instead:

- **CommonJS modules** are wrapped in `__commonJS(...)`, since they need their own `module` and `exports`.
- **ES modules loaded with `require()`** are wrapped in `__esm(...)` so they run lazily when required, like CommonJS would.
- **Modules using direct `eval`** may need to keep their own scope.

Wrapped code can't be tree shaken or minified as well, so a codebase that mixes `require` and `import` heavily ends up with a bigger bundle.

## 90: Why does esbuild warn about direct `eval`?

Direct `eval(code)` can read and change any variable in the scope around it, and esbuild can't know which ones. So esbuild has to:

- not rename any variables in that scope or its parent scopes, which hurts minification,
- often not join that module with others in one scope.

Indirect eval, `(0, eval)(code)`, runs in the global scope and doesn't have these problems. The same goes for `new Function(code)`. If you need to run code strings, use one of those and the warning goes away. If the eval is inside a library you can't change, you can hide the warning with `logOverride: { 'direct-eval': 'silent' }`, but the size cost is still there.

## 91: What is property mangling and what are the risks?

Normal minification only renames local variables. `mangleProps` also renames object properties whose names match a regex:

```js
await esbuild.build({
  entryPoints: ["src/index.ts"],
  bundle: true,
  minify: true,
  mangleProps: /^_/,
  outfile: "dist/index.js",
});
```

Here, `obj._internalState` might become `obj.a`. It can save a lot of space in large codebases, but it's risky:

- If a property is used from outside the bundle (a JSON API, `localStorage`, another script), the names won't match.
- Access by string, like `obj['_' + name]`, isn't renamed.
- Separate builds (like a main bundle and a worker) give different names unless you share `mangleCache` between them.

Use a clear naming rule (like a trailing `_`), use `reserveProps` for exceptions, and save the `mangleCache` from `result.mangleCache` to keep names the same between builds.

## 92: How does esbuild's minifier compare to Terser, and what does it assume about your code?

esbuild's minifier is tens of times faster than Terser. The output is usually close in size, often within a few percent, sometimes slightly bigger. Terser runs extra passes and has optional "unsafe" options, so it can squeeze out a bit more.

Some things to know about esbuild's minifier:

- Function and class names change. Use `keepNames` if your code reads `.name`.
- `Function.prototype.toString()` returns the minified code, so code that parses functions as strings (some old DI frameworks) breaks.
- It won't rename anything near direct `eval`.
- It doesn't remove property accesses or calls it can't prove are safe, since getters can have side effects.

Some teams use esbuild to bundle and Terser just for final minification, but for most apps the small size gain isn't worth the slower build.

## 93: How does syntax lowering work, and how can you tune it with `supported`?

esbuild has a table of which JS and CSS features each browser and runtime version supports. Based on `target`, it rewrites features that are missing: `?.`, `??`, class fields, `async`/`await`, object spread, CSS nesting and others.

If the table is wrong for your case, or you want to force a choice, use `supported`:

```js
await esbuild.build({
  entryPoints: ["app.js"],
  bundle: true,
  target: "es2022",
  supported: {
    bigint: false, // treat BigInt literals as not supported
    "class-static-blocks": false,
  },
  outfile: "out.js",
});
```

Remember that lowering only changes syntax. New built-in functions and objects (`Array.prototype.at`, `structuredClone`) still need polyfills. Also, some lowering makes code bigger and slower, so don't pick an older target than you really need.

## 94: What are the rules for top-level `await` in esbuild?

- It only works when the output format is `esm`. With `cjs` or `iife`, esbuild reports an error, because those formats can't pause while loading.
- A module that uses top-level `await` (or imports one that does) can't be loaded with `require()`. esbuild reports an error for that too.
- When bundling, modules with top-level `await` are joined in a way that keeps the order of `await` correct, but they still slow down the start of everything that imports them.

For libraries, top-level `await` forces all users onto ESM, so it's best to keep it in app entry points only.

## 95: What is `useDefineForClassFields` and why can it change behavior?

There are two ways to compile a class field like `name = 'x'`:

- **Define semantics** (the JS standard): the field is created with `Object.defineProperty`. It does not call setters from a parent class.
- **Assign semantics** (old TypeScript default): the constructor does `this.name = 'x'`, which does call a parent setter.

esbuild reads `useDefineForClassFields` from `tsconfig.json`. If it isn't set, esbuild follows TypeScript and looks at the `target` in `tsconfig.json`: below `ES2022` means `false`, `ES2022` or newer means `true`. If there's no `target` either, the default is `true`. This matters with frameworks that use decorators or parent class setters (old MobX, Lit, Angular with experimental decorators). A wrong value can cause bugs like fields that are `undefined` after construction or setters not being called, with no error at build time.

## 96: How does esbuild handle TypeScript enums and namespaces?

esbuild compiles `enum` and `namespace` to the same JavaScript `tsc` creates. Since it works one file at a time, `const enum` is treated like a normal `enum`: an object is created, instead of the values only being inlined.

When bundling, esbuild can still inline enum values (including across files) as an optimization, so `Color.Red` may become `0` in the output. But you can't depend on `const enum` being fully erased, and a `declare const enum` from a `.d.ts` file won't work at all because there's no code to read the values from. Many teams avoid enums and use plain objects with `as const` instead, which work the same in every tool.

## 97: What are the known problems with code splitting in esbuild?

The docs still call code splitting a work in progress. Things to watch for:

- **ESM only.** No splitting for `cjs` or `iife`.
- **Execution order.** When shared code moves into a chunk, the order in which top-level code runs can differ from the unbundled order. Code that depends on import order (polyfills, global setup) can break. Keeping setup code in the entry file, before other imports, helps.
- **Chunk names.** You only control them with `chunkNames`; there's no way to group modules into named chunks like Webpack's `splitChunks`. Newer versions also report an error when two chunks would get the same output path.
- **CSS.** CSS imported from split JS ends up in separate CSS files, and you have to load them yourself in the right order.

If you need fine control over chunks, Rollup, Rolldown or Webpack are better fits.

## 98: What should you know about CSS handling in esbuild beyond basic bundling?

- **Lowering:** esbuild rewrites some modern CSS based on `target`, for example nesting, newer color syntax and range media queries. It also adds a few vendor prefixes, but it isn't a full Autoprefixer.
- **Order:** for CSS files, `@import` order sets the cascade. For CSS imported from JS, the order of `import` statements in your JS decides the order in the output CSS. Moving imports around can change which rule wins.
- **CSS modules:** `local-css` gives you scoped class names. `composes` works within certain limits.
- **`url()`:** referenced files go through loaders. Missing files are errors, and URLs you want left as they are (like `/fonts/a.woff2` served by the server) need to be marked external with `external: ['/fonts/*']`.
- **No CSS-in-JS:** styled-components or Emotion work, but at runtime; esbuild doesn't extract that CSS.

## 99: What security issues should you know about the esbuild dev server?

The dev server is for local use only. Before version 0.25.0, it sent `Access-Control-Allow-Origin: *`, so any website you visited could send requests to your local esbuild server and read your source code. Since 0.25.0:

- CORS is off by default. You can allow certain origins with `cors: { origin: [...] }` (or `--cors-origin=`).
- Requests whose `Host` header doesn't match the configured host are rejected, which blocks DNS rebinding attacks.

Other good habits: don't bind to `0.0.0.0` unless you must (for example inside a container), never use `serve` in production, and keep esbuild up to date. If you run an older version, upgrading is the fix.

## 100: What supply chain concerns are there with installing esbuild?

esbuild ships native binaries. The `esbuild` package depends on one optional package per platform (`@esbuild/linux-x64` and so on). If that package is missing, an install script tries to download the binary directly from the npm registry.

Things to keep in mind:

- Install scripts run code during `npm install`. Some teams turn them off (`--ignore-scripts`), which works with esbuild as long as the optional platform package was installed.
- Since 0.28.0, esbuild checks the hash of the downloaded binary against hashes stored in the main package.
- Use a lockfile and an exact version so builds can't silently pull a new binary.
- `ESBUILD_BINARY_PATH` lets you point to a binary you built or checked yourself, which is useful in locked-down environments.

## 101: How do you proxy API requests while using the esbuild dev server?

esbuild's `serve` has no proxy option. The usual pattern is a small Node.js server in front of it that sends `/api` to your backend and everything else to esbuild:

```js
import * as esbuild from "esbuild";
import http from "node:http";

const ctx = await esbuild.context({
  entryPoints: ["src/app.ts"],
  bundle: true,
  outdir: "www/js",
});
await ctx.watch();
const { port } = await ctx.serve({
  servedir: "www",
  fallback: "www/index.html",
});

http
  .createServer((req, res) => {
    const target = req.url.startsWith("/api")
      ? { hostname: "localhost", port: 4000 }
      : { hostname: "127.0.0.1", port };

    const proxyReq = http.request(
      { ...target, path: req.url, method: req.method, headers: req.headers },
      (proxyRes) => {
        res.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(res);
      },
    );
    req.pipe(proxyReq);
  })
  .listen(3000);
```

`fallback` makes the server return `index.html` for unknown paths, which you need for single-page apps with client-side routing. `serve` also accepts `keyfile` and `certfile` for HTTPS, and an `onRequest` callback for logging.

## 102: How would you bundle a Node.js app for AWS Lambda with esbuild?

```js
await esbuild.build({
  entryPoints: ["src/handler.ts"],
  bundle: true,
  platform: "node",
  target: "node22",
  format: "esm",
  outfile: "dist/handler.mjs",
  sourcemap: true,
  minify: true,
  external: ["@aws-sdk/*"],
  mainFields: ["module", "main"],
  banner: {
    js: "import { createRequire } from 'node:module'; const require = createRequire(import.meta.url);",
  },
});
```

Points to explain:

- The AWS SDK v3 is already in the Node.js Lambda runtime, so marking it external makes the zip smaller (bundle it if you need an exact version).
- `mainFields: ['module', 'main']` prefers ESM builds of packages for better tree shaking.
- Native modules (like `sharp` or `bcrypt`) must be external and installed for the Lambda's OS.
- Set `NODE_OPTIONS=--enable-source-maps` so stack traces point to your TypeScript.
- A smaller bundle means faster cold starts, which is the main reason to bundle at all.

## 103: How do you use esbuild in a monorepo?

Common problems and fixes:

- **Building internal packages from source.** Instead of building every package first, add a custom condition in each internal package's `exports`, like `"source": "./src/index.ts"`, and build apps with `conditions: ['source']`. esbuild then bundles the TypeScript source directly.
- **Symlinks.** Workspaces link packages with symlinks. esbuild follows them to the real path by default, which is usually what you want. `preserveSymlinks` changes that, but can cause duplicate packages.
- **`tsconfig` paths.** esbuild finds the nearest `tsconfig.json` for each file, so each package can have its own paths and JSX settings.
- **Shared config.** Put the common build options in a shared module and spread them in each package's build script.
- **Speed.** Run builds for many packages in one Node.js process with `Promise.all`, so they share the same esbuild child process.

## 104: How do you find and fix duplicate packages in a bundle?

Signs: the bundle is bigger than expected, or React shows "Invalid hook call" because two copies of React are loaded.

To find them, search the metafile inputs for the same package in different `node_modules` paths:

```js
const inputs = Object.keys(result.metafile.inputs);
console.log(inputs.filter((p) => p.includes("node_modules/react/")));
```

Fixes, in order of preference:

1. Fix the dependency tree: `npm dedupe`, matching version ranges, or `overrides` (npm) / `resolutions` (Yarn) / `pnpm.overrides`.
2. Make library packages list shared libraries like React as `peerDependencies`.
3. As a last resort, a small plugin that resolves that package name from the project root, so every import gets the same copy.

## 105: How do you cache expensive work in a plugin across rebuilds?

esbuild doesn't cache plugin results, so you do it yourself. Key the cache by path and something that changes with the file, like `mtime` or a content hash:

```js
import fs from "node:fs/promises";

const cache = new Map();

const slowTransformPlugin = {
  name: "slow-transform",
  setup(build) {
    build.onLoad({ filter: /\.special\.js$/ }, async (args) => {
      const { mtimeMs } = await fs.stat(args.path);
      const cached = cache.get(args.path);
      if (cached && cached.mtimeMs === mtimeMs) return cached.result;

      const source = await fs.readFile(args.path, "utf8");
      const result = {
        contents: await expensiveTransform(source),
        loader: "js",
      };
      cache.set(args.path, { mtimeMs, result });
      return result;
    });
  },
};
```

If the output depends on other files (like Sass partials), include them in the cache key and return them in `watchFiles`, or changes to those files won't trigger a rebuild.

## 106: A NestJS app breaks when built with esbuild because of `emitDecoratorMetadata`. What can you do?

esbuild can compile the decorators, but it doesn't emit `design:paramtypes` metadata, since that needs type info. NestJS uses that metadata for dependency injection, so services end up `undefined`.

Options:

1. **Use a plugin that runs SWC or `tsc` on files with decorators.** SWC can emit decorator metadata and is still fast. The plugin uses `onLoad` with a filter for `.ts` files, checks if the file contains `@`, and only then runs SWC.
2. **Add explicit `@Inject()` tokens** everywhere so DI doesn't need metadata. This works but is noisy.
3. **Use SWC or `tsc` for the whole project** and skip esbuild for this app. Nest CLI has a built-in SWC builder.

The key point for the interview is knowing why it breaks: esbuild works one file at a time without types.

## 107: Why do file hashes change for files you didn't touch?

A chunk's hash covers its own content, and that content includes the import paths of other chunks, which contain their hashes. So if a shared chunk changes, its hash changes, every chunk that imports it now has a different import path, and their hashes change too. One small change can rename many files and break long-term caching.

Ways to reduce it:

- Keep code that changes often (app code) separate from code that rarely changes (vendor code), for example with separate entry points or builds.
- Avoid putting build-time values like timestamps into shared modules.
- Use an import map to point to hashed files, so chunks import a stable name and only the map changes. This needs extra setup and isn't built into esbuild.

## 108: How do you handle source maps for production?

You usually want source maps for error tracking but don't want to publish your source code. Options:

- `sourcemap: 'external'`: writes `.map` files but doesn't add the `sourceMappingURL` comment. Upload the maps to your error tracker (Sentry and similar) and don't deploy them to the public server.
- `sourcesContent: false`: leaves the original source text out of the map, so it only has positions. Smaller maps, but tools need the source files to show code.
- `sourceRoot`: sets the base path written in the map, which helps when tools look up files.

For Node.js apps, run with `--enable-source-maps` so stack traces use the maps. Keep in mind this has a runtime cost when lots of errors are thrown, since every stack trace is mapped.

## 109: The bundled app behaves differently from the unbundled code. How do you debug it?

A practical order:

1. **Turn off minify** to see readable output. If the bug goes away, look at `keepNames`, `mangleProps`, `drop` and `pure`.
2. **Check `target`** and look at the lowered code for the failing feature. Class fields and decorators are common causes (see `useDefineForClassFields`).
3. **Check which file a package resolved to**, using the metafile or `logLevel: 'verbose'`. A different `exports` condition or `mainFields` may have picked a different build.
4. **Look for CommonJS/ESM interop issues**, like a default import giving you `{ default: ... }` instead of the function.
5. **Check `define`**. A missing or wrong value can turn real code into dead code that gets removed.
6. **Check execution order** if you use code splitting.

Using `transform` on a single file or the esbuild online playground helps narrow it down.

## 110: The build takes 20 seconds with esbuild. What's likely going on?

esbuild by itself should handle even large apps in a second or two, so the time is almost always spent somewhere else:

- **JS plugins** with a broad filter, especially Sass, PostCSS, Babel or SVG transforms running on every file.
- **Type checking** run as part of the build script (`tsc` inside a plugin or before the build).
- **Many separate builds** started one after another instead of in parallel, or a new context created on every rebuild.
- **Huge inputs**, like large JSON files or generated code.
- **Antivirus or slow disks** on Windows or network drives.

To measure, run the same build with no plugins, then add them back one by one, and log timings in `onStart`/`onEnd`. `logLevel: 'verbose'` also shows what esbuild is doing.

## 111: How do you handle Node.js built-ins in a browser bundle?

esbuild doesn't add polyfills for Node.js modules. If a package imports `buffer` or `path` and you build for the browser, you get a "Could not resolve" error.

Options:

- **Use `alias`** to point to browser versions:

  ```js
  await esbuild.build({
    entryPoints: ["src/app.ts"],
    bundle: true,
    alias: { path: "path-browserify" },
    inject: ["./buffer-shim.js"], // exports { Buffer } from 'buffer'
    outfile: "dist/app.js",
  });
  ```

- **Respect the `browser` field.** Packages can set `"fs": false` in their `browser` field, and esbuild then uses an empty module.
- **Mark it external** or use the `empty` loader if the code path never runs in the browser.

The best fix is usually to pick a library that doesn't depend on Node.js at all.

## 112: How do you bundle web workers with esbuild?

esbuild doesn't automatically bundle `new Worker(new URL('./worker.ts', import.meta.url))` the way Vite or Webpack do. The usual approach is to build the worker as its own entry point:

```js
await esbuild.build({
  entryPoints: { app: "src/app.ts", worker: "src/worker.ts" },
  bundle: true,
  format: "esm",
  outdir: "dist",
});
```

```js
// in app.ts
const worker = new Worker("/dist/worker.js", { type: "module" });
```

If you use hashed names, read the worker's output path from the metafile and pass it in with `define`. Another option is to build the worker first with `write: false` and inline its code as a string or a Blob URL into the main bundle, which avoids the extra request.

## 113: Does esbuild support import attributes?

Yes. esbuild understands the `with` syntax:

```js
import config from "./config.json" with { type: "json" };
import template from "./email.html" with { type: "text" };
import wasmBytes from "./module.wasm" with { type: "bytes" };
```

- `type: 'json'` uses the JSON loader.
- `type: 'text'` (since 0.28.0) works like the `text` loader.
- `type: 'bytes'` (since 0.25.11) works like the `binary` loader and gives a `Uint8Array`.

When the import is external, the attributes are kept in the output so the runtime can check them. The old `assert` syntax is deprecated in the language and you should use `with`.

## 114: How do you use esbuild to remove debug-only code from production builds?

Combine `define` with dead code elimination:

```js
// in code
if (__DEV__) {
  enableDebugPanel();
}
```

```js
await esbuild.build({
  entryPoints: ["src/app.ts"],
  bundle: true,
  minify: true,
  define: { __DEV__: "false" },
  outfile: "dist/app.js",
});
```

The `if` becomes `if (false)` and is removed, and if `enableDebugPanel` isn't used anywhere else, tree shaking removes it and its imports too. `dropLabels` is another option: it removes labeled blocks, like `DEV: { ... }`, without needing a global variable:

```js
DEV: console.log("state", state);
```

```bash
npx esbuild app.js --bundle --drop-labels=DEV --outfile=out.js
```

For TypeScript, declare `__DEV__` in a `.d.ts` file so the type checker knows about it.

## 115: What do you need to think about when building a library (not an app) with esbuild?

- **Don't bundle dependencies.** Use `packages: 'external'` so users don't get duplicate copies.
- **Ship ESM** (and CJS only if you need to support older users), with a proper `exports` map.
- **Don't minify,** or only lightly. The app's bundler will minify, and readable code helps users debug.
- **Choose a modest `target`**, but not too old. Over-lowering makes code bigger for everyone.
- **Set `"sideEffects": false`** in `package.json` if it's true, and keep files free of top-level side effects so users can tree shake.
- **Consider not bundling at all,** and transform each file one by one (one output file per source file). This keeps the module structure and gives the user's bundler the best chance to tree shake.
- **Generate `.d.ts` files** with `tsc`, since esbuild doesn't.

## 116: What do `charset` and `lineLimit` do, and when do they matter?

By default esbuild escapes non-ASCII characters, so `"ქართული"` becomes `"ქ..."`. This avoids problems when the server sends the file without the right encoding, but it makes text-heavy bundles bigger. `charset: 'utf8'` keeps the characters as they are, which is fine if your server sends `charset=utf-8`.

`lineLimit` splits very long lines in minified output:

```js
await esbuild.build({
  entryPoints: ["app.ts"],
  bundle: true,
  minify: true,
  lineLimit: 500,
  outfile: "out.js",
});
```

A whole bundle on one line can be slow in some editors and tools, and some old systems have line length limits. It adds a few bytes, so only use it if you hit one of those problems.

## 117: How does esbuild compare to Webpack, Rollup, Rolldown and SWC, and when would you not use it?

- **Webpack**: the most features and plugins (module federation, HMR, fine-grained chunking), but much slower.
- **Rollup**: very good output for libraries and fine control over chunks, but slower and written in JS.
- **Rolldown**: a Rust bundler with a Rollup-compatible API, now used by Vite. Similar speed to esbuild with more Rollup-style features.
- **SWC**: mainly a fast compiler (like Babel), with decorator metadata and plugin support; it's not mainly a bundler.

I wouldn't use plain esbuild when the project needs HMR, module federation, fine control over chunks, a large Babel plugin setup, very old browser support (ES5), or decorator metadata. In those cases esbuild may still be used inside another tool, just not as the whole build.

## 118: How do you use esbuild from Go?

```go
package main

import (
	"os"

	"github.com/evanw/esbuild/pkg/api"
)

func main() {
	result := api.Build(api.BuildOptions{
		EntryPoints: []string{"src/app.ts"},
		Bundle:      true,
		Outfile:     "dist/app.js",
		Write:       true,
		LogLevel:    api.LogLevelInfo,
	})
	if len(result.Errors) > 0 {
		os.Exit(1)
	}
}
```

The Go API has the same options as the JS API, plus `api.Transform` and `api.Context`. Plugins are written in Go too, with `api.Plugin` and `build.OnResolve` / `build.OnLoad`. Because they run in the same process, there is no IPC cost, so Go plugins are much faster than JS ones. It's a good fit if your dev tools or server are already in Go.

## 119: How would you use esbuild's `transform` API inside a test runner or custom loader?

Test runners and loaders often get one file at a time and need JavaScript back. `transform` fits that well:

```js
import { transform } from "esbuild";

export async function compile(source, filename) {
  const result = await transform(source, {
    loader: filename.endsWith("x") ? "tsx" : "ts",
    format: "cjs",
    target: "node22",
    sourcemap: "inline",
    sourcefile: filename,
    jsx: "automatic",
  });
  return result.code;
}
```

`sourcefile` sets the file name used in errors and source maps, so stack traces point to the right test file. `sourcemap: 'inline'` keeps the map with the code, which most runners understand. Since `transform` doesn't resolve imports, the runner is still in charge of loading dependencies. Tools like `esbuild-register` and `tsx` work in a similar way.

## 120: How would you design a production build setup for a single-page app using only esbuild?

A build script that:

1. **Builds JS and CSS** from `src/main.tsx` with `bundle`, `minify`, `splitting`, `format: 'esm'`, a `target` based on your browser support, and `sourcemap: 'external'`.
2. **Hashes file names** with `entryNames: '[name]-[hash]'`, `chunkNames` and `assetNames`, and sets `publicPath` to the CDN URL.
3. **Sets values** with `define` (`process.env.NODE_ENV`, API URL) and removes debug code with `drop` or `dropLabels`.
4. **Writes `index.html`** using the metafile to insert the hashed JS and CSS file names, plus `<link rel="modulepreload">` for chunks the entry imports right away.
5. **Checks size** with `analyzeMetafile` and fails CI if the main bundle goes over a set limit.
6. **Runs `tsc --noEmit` and lint in parallel** with the build, since esbuild doesn't check types.
7. **Uploads source maps** to the error tracker and deploys only the other files.

For development, the same options go into a context with `watch()` and `serve()` plus live reload. Keeping one shared options object for both makes dev and prod behave the same.
