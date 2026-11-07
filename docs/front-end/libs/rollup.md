# Rollup Interview Questions and Answers

_Last updated: October 29, 2026_

120 Rollup interview questions with answers, split into three levels: 40 easy, 40 moderate and 40 advanced.

The answers target Rollup 4 (4.66 at the time of writing), which uses a native SWC-based parser and needs Node.js 18 or newer. Plugin examples use the official `@rollup/plugin-*` packages where they exist. Older habits that you will still see in real projects, like `onwarn` or configs written as CommonJS, are mentioned where they matter.

## Table of Contents

- [Easy Questions (1-40)](#easy-questions-1-40)
- [Moderate Questions (41-80)](#moderate-questions-41-80)
- [Advanced Questions (81-120)](#advanced-questions-81-120)

### Easy Questions (1-40)

- [1: What is Rollup?](#1-what-is-rollup)
- [2: What problem does a bundler like Rollup solve?](#2-what-problem-does-a-bundler-like-rollup-solve)
- [3: How do you install Rollup?](#3-how-do-you-install-rollup)
- [4: How do you run a basic build from the command line?](#4-how-do-you-run-a-basic-build-from-the-command-line)
- [5: What is a Rollup config file?](#5-what-is-a-rollup-config-file)
- [6: What does the input option do?](#6-what-does-the-input-option-do)
- [7: What is the difference between output.file and output.dir?](#7-what-is-the-difference-between-outputfile-and-outputdir)
- [8: Which output formats does Rollup support?](#8-which-output-formats-does-rollup-support)
- [9: What is tree shaking?](#9-what-is-tree-shaking)
- [10: Why does tree shaking work better with ES modules than CommonJS?](#10-why-does-tree-shaking-work-better-with-es-modules-than-commonjs)
- [11: What is a Rollup plugin?](#11-what-is-a-rollup-plugin)
- [12: Why can't Rollup import packages from node_modules by default?](#12-why-cant-rollup-import-packages-from-node_modules-by-default)
- [13: What does @rollup/plugin-commonjs do?](#13-what-does-rollupplugin-commonjs-do)
- [14: What is an external dependency?](#14-what-is-an-external-dependency)
- [15: How do you minify the output?](#15-how-do-you-minify-the-output)
- [16: How do you generate source maps?](#16-how-do-you-generate-source-maps)
- [17: What is watch mode?](#17-what-is-watch-mode)
- [18: What does output.name do?](#18-what-does-outputname-do)
- [19: What does output.globals do?](#19-what-does-outputglobals-do)
- [20: Can a config file export more than one build?](#20-can-a-config-file-export-more-than-one-build)
- [21: What is code splitting in Rollup?](#21-what-is-code-splitting-in-rollup)
- [22: How do dynamic imports work with Rollup?](#22-how-do-dynamic-imports-work-with-rollup)
- [23: What are chunks and assets?](#23-what-are-chunks-and-assets)
- [24: How do you change output file names?](#24-how-do-you-change-output-file-names)
- [25: Why put a hash in the file name?](#25-why-put-a-hash-in-the-file-name)
- [26: How do you use TypeScript with Rollup?](#26-how-do-you-use-typescript-with-rollup)
- [27: How do you import JSON files?](#27-how-do-you-import-json-files)
- [28: How do you replace values like process.env.NODE_ENV?](#28-how-do-you-replace-values-like-processenvnode_env)
- [29: What does the -c flag do and can you give it a file name?](#29-what-does-the--c-flag-do-and-can-you-give-it-a-file-name)
- [30: Why do people name the config rollup.config.mjs?](#30-why-do-people-name-the-config-rollupconfigmjs)
- [31: How do you get autocompletion in the config file?](#31-how-do-you-get-autocompletion-in-the-config-file)
- [32: How do you pass environment values to the config from the CLI?](#32-how-do-you-pass-environment-values-to-the-config-from-the-cli)
- [33: What does the banner option do?](#33-what-does-the-banner-option-do)
- [34: What is the difference between Rollup and Webpack?](#34-what-is-the-difference-between-rollup-and-webpack)
- [35: How is Rollup related to Vite?](#35-how-is-rollup-related-to-vite)
- [36: What does "scope hoisting" mean?](#36-what-does-scope-hoisting-mean)
- [37: What happens if two modules use the same variable name?](#37-what-happens-if-two-modules-use-the-same-variable-name)
- [38: What does the Unresolved dependencies warning mean?](#38-what-does-the-unresolved-dependencies-warning-mean)
- [39: What is the "this is undefined" warning?](#39-what-is-the-this-is-undefined-warning)
- [40: How do you clean the dist folder before a build?](#40-how-do-you-clean-the-dist-folder-before-a-build)

### Moderate Questions (41-80)

- [41: How do you write a simple Rollup plugin?](#41-how-do-you-write-a-simple-rollup-plugin)
- [42: What is the difference between build hooks and output generation hooks?](#42-what-is-the-difference-between-build-hooks-and-output-generation-hooks)
- [43: What do resolveId, load and transform do?](#43-what-do-resolveid-load-and-transform-do)
- [44: What are the different hook kinds?](#44-what-are-the-different-hook-kinds)
- [45: How do you create a virtual module?](#45-how-do-you-create-a-virtual-module)
- [46: What does @rollup/plugin-node-resolve do with package.json fields?](#46-what-does-rollupplugin-node-resolve-do-with-packagejson-fields)
- [47: Why does plugin order matter?](#47-why-does-plugin-order-matter)
- [48: What is the difference between plugins and output.plugins?](#48-what-is-the-difference-between-plugins-and-outputplugins)
- [49: How do you mark all dependencies as external in a library build?](#49-how-do-you-mark-all-dependencies-as-external-in-a-library-build)
- [50: How do you build a library as both ESM and CommonJS?](#50-how-do-you-build-a-library-as-both-esm-and-commonjs)
- [51: What does output.exports do?](#51-what-does-outputexports-do)
- [52: What does output.interop do?](#52-what-does-outputinterop-do)
- [53: How do you control chunk splitting with manualChunks?](#53-how-do-you-control-chunk-splitting-with-manualchunks)
- [54: What does output.preserveModules do?](#54-what-does-outputpreservemodules-do)
- [55: What does inlineDynamicImports do?](#55-what-does-inlinedynamicimports-do)
- [56: How does Rollup handle CSS?](#56-how-does-rollup-handle-css)
- [57: How do you emit an asset from a plugin?](#57-how-do-you-emit-an-asset-from-a-plugin)
- [58: How do you reference an emitted file's URL from code?](#58-how-do-you-reference-an-emitted-files-url-from-code)
- [59: What are the main options of @rollup/plugin-commonjs?](#59-what-are-the-main-options-of-rollupplugin-commonjs)
- [60: How do you use Babel with Rollup?](#60-how-do-you-use-babel-with-rollup)
- [61: How do you set up path aliases?](#61-how-do-you-set-up-path-aliases)
- [62: How do you generate TypeScript declaration files?](#62-how-do-you-generate-typescript-declaration-files)
- [63: How do you use Rollup with the JavaScript API?](#63-how-do-you-use-rollup-with-the-javascript-api)
- [64: How do you use watch mode from the JavaScript API?](#64-how-do-you-use-watch-mode-from-the-javascript-api)
- [65: What is the treeshake option and what presets does it have?](#65-what-is-the-treeshake-option-and-what-presets-does-it-have)
- [66: What is a side effect and how does it affect tree shaking?](#66-what-is-a-side-effect-and-how-does-it-affect-tree-shaking)
- [67: How does the package.json sideEffects field work with Rollup?](#67-how-does-the-packagejson-sideeffects-field-work-with-rollup)
- [68: What do the pure and no-side-effects annotations do?](#68-what-do-the-pure-and-no-side-effects-annotations-do)
- [69: What is the difference between onLog and onwarn?](#69-what-is-the-difference-between-onlog-and-onwarn)
- [70: How do you make the build fail on warnings?](#70-how-do-you-make-the-build-fail-on-warnings)
- [71: What does the CIRCULAR_DEPENDENCY warning mean and should you fix it?](#71-what-does-the-circular_dependency-warning-mean-and-should-you-fix-it)
- [72: How do you see what is making the bundle big?](#72-how-do-you-see-what-is-making-the-bundle-big)
- [73: How do you write a TypeScript config file?](#73-how-do-you-write-a-typescript-config-file)
- [74: How do you export a function from the config file?](#74-how-do-you-export-a-function-from-the-config-file)
- [75: How do you build an IIFE or UMD bundle for a script tag?](#75-how-do-you-build-an-iife-or-umd-bundle-for-a-script-tag)
- [76: What does the cache option do?](#76-what-does-the-cache-option-do)
- [77: How do you import files like .wasm or images?](#77-how-do-you-import-files-like-wasm-or-images)
- [78: How do you handle dynamic imports that use variables in the path?](#78-how-do-you-handle-dynamic-imports-that-use-variables-in-the-path)
- [79: How do you combine Rollup with esbuild or SWC for speed?](#79-how-do-you-combine-rollup-with-esbuild-or-swc-for-speed)
- [80: How do you keep the "use client" directive or other module-level directives?](#80-how-do-you-keep-the-use-client-directive-or-other-module-level-directives)

### Advanced Questions (81-120)

- [81: What changed in Rollup 4 compared to Rollup 3?](#81-what-changed-in-rollup-4-compared-to-rollup-3)
- [82: Why does Rollup 4 sometimes fail with "Cannot find module @rollup/rollup-..."?](#82-why-does-rollup-4-sometimes-fail-with-cannot-find-module-rolluprollup-)
- [83: How does Rollup's tree shaking work internally?](#83-how-does-rollups-tree-shaking-work-internally)
- [84: Why does a function call sometimes stay in the bundle even though its result isn't used?](#84-why-does-a-function-call-sometimes-stay-in-the-bundle-even-though-its-result-isnt-used)
- [85: What are treeshake.moduleSideEffects and propertyReadSideEffects?](#85-what-are-treeshakemodulesideeffects-and-propertyreadsideeffects)
- [86: How does Rollup handle live bindings?](#86-how-does-rollup-handle-live-bindings)
- [87: How does Rollup decide what goes into each chunk?](#87-how-does-rollup-decide-what-goes-into-each-chunk)
- [88: What is preserveEntrySignatures?](#88-what-is-preserveentrysignatures)
- [89: What does hoistTransitiveImports do?](#89-what-does-hoisttransitiveimports-do)
- [90: How do content hashes work, and why does a change in one file change hashes in other files?](#90-how-do-content-hashes-work-and-why-does-a-change-in-one-file-change-hashes-in-other-files)
- [91: What does augmentChunkHash do?](#91-what-does-augmentchunkhash-do)
- [92: How do you resolve an id with other plugins from inside your own resolveId?](#92-how-do-you-resolve-an-id-with-other-plugins-from-inside-your-own-resolveid)
- [93: What is this.load and when do you use it?](#93-what-is-thisload-and-when-do-you-use-it)
- [94: How do plugins share data with each other?](#94-how-do-plugins-share-data-with-each-other)
- [95: What are hook filters and why were they added?](#95-what-are-hook-filters-and-why-were-they-added)
- [96: How do you control when a plugin hook runs compared to other plugins?](#96-how-do-you-control-when-a-plugin-hook-runs-compared-to-other-plugins)
- [97: What is syntheticNamedExports?](#97-what-is-syntheticnamedexports)
- [98: What does shimMissingExports do?](#98-what-does-shimmissingexports-do)
- [99: How does Rollup chain source maps from multiple plugins?](#99-how-does-rollup-chain-source-maps-from-multiple-plugins)
- [100: Which output options help with source maps in production?](#100-which-output-options-help-with-source-maps-in-production)
- [101: What does shouldTransformCachedModule do?](#101-what-does-shouldtransformcachedmodule-do)
- [102: How do you measure where build time goes?](#102-how-do-you-measure-where-build-time-goes)
- [103: What is maxParallelFileOps and when would you change it?](#103-what-is-maxparallelfileops-and-when-would-you-change-it)
- [104: How do you parse code into an AST inside a plugin?](#104-how-do-you-parse-code-into-an-ast-inside-a-plugin)
- [105: What do resolveImportMeta and resolveFileUrl do?](#105-what-do-resolveimportmeta-and-resolvefileurl-do)
- [106: How do you bundle a Web Worker with Rollup?](#106-how-do-you-bundle-a-web-worker-with-rollup)
- [107: What is implicitlyLoadedAfterOneOf?](#107-what-is-implicitlyloadedafteroneof)
- [108: Why can manualChunks break your app and how do you avoid it?](#108-why-can-manualchunks-break-your-app-and-how-do-you-avoid-it)
- [109: How would you debug a "process is not defined" error in a browser bundle?](#109-how-would-you-debug-a-process-is-not-defined-error-in-a-browser-bundle)
- [110: Why might lodash not get tree shaken, and how do you fix it?](#110-why-might-lodash-not-get-tree-shaken-and-how-do-you-fix-it)
- [111: How do you avoid shipping duplicate copies of React in a library?](#111-how-do-you-avoid-shipping-duplicate-copies-of-react-in-a-library)
- [112: What is the jsx option in Rollup 4?](#112-what-is-the-jsx-option-in-rollup-4)
- [113: How do you make a library work well for tree shaking in consumers' bundlers?](#113-how-do-you-make-a-library-work-well-for-tree-shaking-in-consumers-bundlers)
- [114: What is the dual package hazard and how does it affect a Rollup library?](#114-what-is-the-dual-package-hazard-and-how-does-it-affect-a-rollup-library)
- [115: How would you set up Rollup for a monorepo with many packages?](#115-how-would-you-set-up-rollup-for-a-monorepo-with-many-packages)
- [116: What security issues should you think about in a Rollup build?](#116-what-security-issues-should-you-think-about-in-a-rollup-build)
- [117: How do Rollup and Rolldown compare?](#117-how-do-rollup-and-rolldown-compare)
- [118: How would you test a Rollup plugin?](#118-how-would-you-test-a-rollup-plugin)
- [119: How would you build a library that ships to npm, a CDN and Node?](#119-how-would-you-build-a-library-that-ships-to-npm-a-cdn-and-node)
- [120: A Rollup build that used to take 20 seconds now takes 3 minutes. How would you investigate?](#120-a-rollup-build-that-used-to-take-20-seconds-now-takes-3-minutes-how-would-you-investigate)

---

# Easy Questions (1-40)

## 1: What is Rollup?

Rollup is a JavaScript module bundler. It takes your source files, follows their `import` statements, and combines them into one or more output files. It was built around ES modules from the start, which is why it does tree shaking well and produces clean, readable output.

It is used a lot for building libraries (React, Vue, Svelte and many npm packages were built with it) and it was the production bundler inside Vite up to Vite 7.

## 2: What problem does a bundler like Rollup solve?

Browsers and package consumers often want a small number of files, not hundreds of separate modules. A bundler resolves the dependency graph, removes code that is never used, and writes files in the format you need (ES modules, CommonJS, a script tag build and so on). Without it you would ship many small files, extra network requests and dead code.

## 3: How do you install Rollup?

Install it as a dev dependency in your project:

```bash
npm install --save-dev rollup
```

Then run it through `npx rollup` or an npm script. Installing it globally works too, but a local install keeps the version fixed per project. Rollup 4 needs Node.js 18 or newer.

## 4: How do you run a basic build from the command line?

Pass the input file, the output file and the format:

```bash
npx rollup src/main.js --file dist/bundle.js --format es
```

The short form is `npx rollup src/main.js -o dist/bundle.js -f es`. If you leave out `--file`, Rollup prints the result to stdout.

## 5: What is a Rollup config file?

It is a file, usually `rollup.config.js` or `rollup.config.mjs`, that exports the build options so you don't have to type them on the command line every time. You run it with `-c` (or `--config`):

```js
// rollup.config.mjs
export default {
  input: "src/main.js",
  output: {
    file: "dist/bundle.js",
    format: "es",
  },
};
```

```bash
npx rollup -c
```

## 6: What does the input option do?

`input` tells Rollup where to start. It can be one file, an array of files, or an object where the keys become the output chunk names:

```js
export default {
  input: {
    main: "src/main.js",
    admin: "src/admin.js",
  },
  output: { dir: "dist", format: "es" },
};
```

This produces `dist/main.js` and `dist/admin.js`, plus any shared chunks.

## 7: What is the difference between output.file and output.dir?

`output.file` writes a single file. It only works when the build produces one chunk. `output.dir` writes into a folder and is required when there is more than one chunk, for example with several entry points or dynamic imports. You can't use both in the same output object.

## 8: Which output formats does Rollup support?

- `es` (aliases `esm`, `module`): ES modules with `import` and `export`.
- `cjs` (alias `commonjs`): CommonJS for Node.js with `require` and `module.exports`.
- `iife`: a self-running function, for a plain `<script>` tag.
- `umd`: works as AMD, CommonJS and a global variable.
- `amd`: for AMD loaders like RequireJS.
- `system` (alias `systemjs`): for the SystemJS loader.

## 9: What is tree shaking?

Tree shaking means removing code that is never used. Rollup looks at what is actually imported and used, starting from the entry points, and leaves out the rest:

```js
// math.js
export const add = (a, b) => a + b;
export const multiply = (a, b) => a * b;

// main.js
import { add } from "./math.js";
console.log(add(1, 2));
```

The output contains `add` but not `multiply`. Rollup made this popular in the JavaScript world.

## 10: Why does tree shaking work better with ES modules than CommonJS?

ES module imports and exports are static. They have to be at the top level and use fixed names, so Rollup can see exactly what is used without running the code. CommonJS `require` is a normal function call that can be conditional or use computed names, so a bundler can't be sure what is used and has to keep more code.

## 11: What is a Rollup plugin?

A plugin is an object with a `name` and some hook functions that Rollup calls during the build. Plugins add things Rollup doesn't do by itself, such as finding packages in `node_modules`, converting CommonJS, compiling TypeScript or minifying. You add them to the `plugins` array:

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";

export default {
  input: "src/main.js",
  output: { file: "dist/bundle.js", format: "es" },
  plugins: [nodeResolve()],
};
```

## 12: Why can't Rollup import packages from node_modules by default?

By default Rollup only resolves relative and absolute paths. It doesn't know Node's lookup rules for bare imports like `import _ from "lodash-es"`, so it treats them as external and shows an "Unresolved dependencies" warning. To bundle them, add `@rollup/plugin-node-resolve`, which finds the package and reads its `package.json`.

## 13: What does @rollup/plugin-commonjs do?

Many npm packages are still published as CommonJS. Rollup only understands ES modules, so `@rollup/plugin-commonjs` converts `require` and `module.exports` into ES module syntax before Rollup processes them. It is almost always used together with `@rollup/plugin-node-resolve`:

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";

export default {
  input: "src/main.js",
  output: { file: "dist/bundle.js", format: "es" },
  plugins: [nodeResolve(), commonjs()],
};
```

## 14: What is an external dependency?

An external is a module that Rollup leaves out of the bundle and keeps as an import in the output. This is normal for libraries, where you don't want to ship a copy of `react` or `lodash` inside your package:

```js
export default {
  input: "src/index.js",
  external: ["react", "react-dom"],
  output: { file: "dist/index.js", format: "es" },
};
```

The output keeps `import React from "react"` and the user's own bundler provides it.

## 15: How do you minify the output?

Rollup doesn't minify by itself. Use a plugin like `@rollup/plugin-terser`, usually as an output plugin:

```js
import terser from "@rollup/plugin-terser";

export default {
  input: "src/main.js",
  output: {
    file: "dist/bundle.min.js",
    format: "es",
    plugins: [terser()],
  },
};
```

## 16: How do you generate source maps?

Set `output.sourcemap`:

```js
output: {
  file: "dist/bundle.js",
  format: "es",
  sourcemap: true,
}
```

`true` writes a separate `.map` file and adds a comment pointing to it. `"inline"` puts the map inside the bundle as a data URL. `"hidden"` writes the `.map` file but leaves out the comment, which is handy when you upload maps to an error tracker but don't want to serve them publicly.

## 17: What is watch mode?

Watch mode rebuilds when a source file changes. Use `-w` or `--watch`:

```bash
npx rollup -c -w
```

Rollup only rebuilds the modules that changed, so later builds are faster than the first one. You can also set `watch` options in the config, like `watch.include` and `watch.exclude`.

## 18: What does output.name do?

`output.name` is the global variable name for `iife` and `umd` builds. Without it, Rollup can't expose your exports in a browser script:

```js
output: {
  file: "dist/my-lib.umd.js",
  format: "umd",
  name: "MyLib",
}
```

After loading the script, the library is available as `window.MyLib`.

## 19: What does output.globals do?

For `iife` and `umd` builds, external imports need to come from global variables. `globals` maps the module id to the global name:

```js
export default {
  input: "src/index.js",
  external: ["jquery"],
  output: {
    file: "dist/plugin.js",
    format: "iife",
    name: "MyPlugin",
    globals: { jquery: "$" },
  },
};
```

If you leave it out, Rollup guesses a name and shows a warning.

## 20: Can a config file export more than one build?

Yes. Export an array of config objects, and Rollup runs them all. You can also give one input several outputs:

```js
export default {
  input: "src/index.js",
  output: [
    { file: "dist/index.mjs", format: "es" },
    { file: "dist/index.cjs", format: "cjs" },
  ],
};
```

Several outputs from one input only parse the code once, which is faster than separate configs.

## 21: What is code splitting in Rollup?

Code splitting means Rollup writes more than one chunk. It happens when you have several entry points or use dynamic `import()`. Code shared by several entries goes into a shared chunk so it isn't duplicated. You need `output.dir` and a format that supports it (`es`, `cjs`, `amd` or `system`; `iife` and `umd` can't split).

## 22: How do dynamic imports work with Rollup?

A dynamic `import()` creates a separate chunk that loads on demand:

```js
button.addEventListener("click", async () => {
  const { openChart } = await import("./chart.js");
  openChart();
});
```

Rollup writes `chart.js` (and its dependencies) as its own chunk, and the main bundle loads it only when the button is clicked.

## 23: What are chunks and assets?

A chunk is a JavaScript output file made from one or more modules. An asset is any other file Rollup writes, such as CSS, an image or a JSON file, usually emitted by a plugin. In the bundle object that plugins see, each item has `type: "chunk"` or `type: "asset"`.

## 24: How do you change output file names?

Use `entryFileNames`, `chunkFileNames` and `assetFileNames` with placeholders:

```js
output: {
  dir: "dist",
  format: "es",
  entryFileNames: "[name].[hash].js",
  chunkFileNames: "chunks/[name]-[hash].js",
  assetFileNames: "assets/[name]-[hash][extname]",
}
```

Common placeholders are `[name]`, `[hash]`, `[format]` and, for assets, `[extname]` and `[ext]`.

## 25: Why put a hash in the file name?

The hash changes when the file content changes. That lets you cache files for a long time in the browser and on the CDN, because a new version always has a new URL. Files that didn't change keep their old hash, so users don't download them again.

## 26: How do you use TypeScript with Rollup?

Use a plugin. The official one is `@rollup/plugin-typescript`, which uses the TypeScript compiler and respects your `tsconfig.json`:

```js
import typescript from "@rollup/plugin-typescript";

export default {
  input: "src/index.ts",
  output: { dir: "dist", format: "es" },
  plugins: [typescript()],
};
```

Faster options that only strip types without type checking are `rollup-plugin-esbuild` and `@rollup/plugin-swc`. With those you run `tsc --noEmit` separately for type checks.

## 27: How do you import JSON files?

Add `@rollup/plugin-json`. It turns a JSON file into an ES module, and you can even import single properties, so unused ones get tree shaken:

```js
import json from "@rollup/plugin-json";

export default {
  input: "src/main.js",
  output: { file: "dist/bundle.js", format: "es" },
  plugins: [json()],
};
```

```js
import { version } from "../package.json";
console.log(version);
```

## 28: How do you replace values like process.env.NODE_ENV?

Use `@rollup/plugin-replace`:

```js
import replace from "@rollup/plugin-replace";

export default {
  plugins: [
    replace({
      preventAssignment: true,
      "process.env.NODE_ENV": JSON.stringify("production"),
    }),
  ],
};
```

Don't forget `JSON.stringify`, otherwise the value is inserted as `production` without quotes and becomes a variable name. `preventAssignment` stops it from replacing the left side of an assignment like `process.env.NODE_ENV = "x"`.

## 29: What does the -c flag do and can you give it a file name?

`-c` (or `--config`) tells Rollup to use a config file. With no value it looks for `rollup.config.mjs`, then `rollup.config.cjs`, then `rollup.config.js`. You can pass a specific file:

```bash
npx rollup -c rollup.lib.config.mjs
```

## 30: Why do people name the config rollup.config.mjs?

Rollup loads the config file through Node.js. If your `package.json` doesn't have `"type": "module"`, Node treats `.js` files as CommonJS and `export default` fails. The `.mjs` extension always means ES module, so it works in every project. Another option is `--bundleConfigAsCjs`, which makes Rollup bundle the config to CommonJS first.

## 31: How do you get autocompletion in the config file?

Wrap the config in `defineConfig`, which comes from the `rollup` package. It doesn't change anything at runtime, it only gives your editor the types:

```js
import { defineConfig } from "rollup";

export default defineConfig({
  input: "src/main.js",
  output: { file: "dist/bundle.js", format: "es" },
});
```

A JSDoc comment like `/** @type {import('rollup').RollupOptions} */` does the same thing.

## 32: How do you pass environment values to the config from the CLI?

Use `--environment`. The values end up in `process.env`:

```bash
npx rollup -c --environment BUILD:production,ANALYZE
```

```js
const isProd = process.env.BUILD === "production";
```

`ANALYZE` without a value becomes `"true"`. You can also use your own flags with a `config` prefix, like `--configDebug`, and read them from the command line args when the config exports a function.

## 33: What does the banner option do?

`output.banner` adds text at the top of every chunk, for example a license comment. `output.footer` adds text at the end:

```js
output: {
  file: "dist/lib.js",
  format: "es",
  banner: "/*! my-lib v1.2.0 | MIT License */",
}
```

There are also `intro` and `outro`, which go inside the wrapper (for example inside the IIFE function) instead of outside it.

## 34: What is the difference between Rollup and Webpack?

Both are bundlers, but they have different focus. Webpack was built for applications: it handles every kind of asset through loaders, has a dev server and hot reload, and adds a runtime to manage modules. Rollup was built around ES modules and produces flat output with almost no extra code, which is great for libraries. Today both can build apps and libraries, but Rollup is still the common pick for publishing packages.

## 35: How is Rollup related to Vite?

Vite used Rollup for production builds up to Vite 7, and its plugin system is an extension of Rollup's plugin API, so most Rollup plugins also work in Vite. Since Vite 8 the default bundler is Rolldown, a Rust bundler that keeps a Rollup-compatible plugin API. Rollup itself is still maintained and widely used.

## 36: What does "scope hoisting" mean?

Instead of wrapping every module in its own function (as older bundlers did), Rollup puts all module code in one shared scope and renames variables when names clash. The output is smaller and runs a bit faster because there are no extra function calls or module registry. Rollup has always worked this way.

## 37: What happens if two modules use the same variable name?

Rollup renames one of them in the output so they don't clash:

```js
// a.js
const count = 1;
export const a = count;

// b.js
const count = 2;
export const b = count;
```

In the bundle you will see `count` and `count$1`. Exported names stay the same for the outside world; only internal names change.

## 38: What does the Unresolved dependencies warning mean?

Rollup couldn't find a module, so it treated it as external. Usually it means you forgot `@rollup/plugin-node-resolve`, made a typo in the path, or meant to mark the package as external. If the import really is external, add it to `external` so the warning goes away and the intent is clear.

## 39: What is the "this is undefined" warning?

In ES modules, `this` at the top level is `undefined`. When Rollup sees top-level `this` (common in code compiled by old TypeScript or Babel versions), it warns and replaces it with `undefined`. Most of the time it's harmless. If some code really needs it, you can change it with the `context` or `moduleContext` options.

## 40: How do you clean the dist folder before a build?

Rollup doesn't delete old files. You can add a step in your npm script:

```json
{
  "scripts": {
    "build": "rm -rf dist && rollup -c"
  }
}
```

For cross-platform scripts, use a package like `rimraf` or `del-cli`, or a small plugin that removes the folder in `buildStart`.

# Moderate Questions (41-80)

## 41: How do you write a simple Rollup plugin?

A plugin is a function that returns an object with a `name` and the hooks you need. This one replaces a placeholder in every JavaScript file:

```js
export default function buildTime() {
  return {
    name: "build-time",
    transform(code, id) {
      if (!id.endsWith(".js")) return null;
      return {
        code: code.replaceAll(
          "__BUILD_TIME__",
          JSON.stringify(new Date().toISOString()),
        ),
        map: null,
      };
    },
  };
}
```

Returning `null` means "I don't handle this file", so Rollup moves on. In real plugins, use `magic-string` to change code so you can return a correct source map instead of `map: null`.

## 42: What is the difference between build hooks and output generation hooks?

Build hooks run while Rollup reads and analyzes modules: `options`, `buildStart`, `resolveId`, `load`, `transform`, `moduleParsed`, `buildEnd` and others. They run once per `rollup()` call.

Output generation hooks run while Rollup writes chunks: `outputOptions`, `renderStart`, `renderChunk`, `generateBundle`, `writeBundle` and others. They run once for every output. So with two outputs (ESM and CJS), `transform` runs once per module but `renderChunk` runs for each output.

## 43: What do resolveId, load and transform do?

- `resolveId(source, importer)` turns an import string like `"./utils"` into a module id, usually an absolute path. It can also mark it as external.
- `load(id)` returns the source code for an id. By default Rollup reads the file from disk.
- `transform(code, id)` changes the code after loading, for example compiling TypeScript or JSX.

For each module Rollup calls them in this order, and for the first two it stops at the first plugin that returns something other than `null`.

## 44: What are the different hook kinds?

- `async`: the hook can return a promise.
- `first`: hooks run one by one until one returns a value that isn't `null` or `undefined` (for example `resolveId` and `load`).
- `sequential`: hooks run one by one, each one gets the result of the previous one (for example `transform` and `renderChunk`).
- `parallel`: all plugins run at the same time and Rollup waits for all of them (for example `buildStart` and `writeBundle`).

## 45: How do you create a virtual module?

Answer the id in `resolveId` and return code from `load`. By convention, the resolved id starts with `\0` so other plugins (like node-resolve or commonjs) skip it:

```js
export default function virtualEnv() {
  const virtualId = "virtual:env";
  const resolvedId = "\0" + virtualId;
  return {
    name: "virtual-env",
    resolveId(source) {
      if (source === virtualId) return resolvedId;
    },
    load(id) {
      if (id === resolvedId) {
        return `export const mode = ${JSON.stringify(process.env.NODE_ENV ?? "development")};`;
      }
    },
  };
}
```

```js
import { mode } from "virtual:env";
```

## 46: What does @rollup/plugin-node-resolve do with package.json fields?

It finds the right file to load from a package. It reads the `exports` field first and matches conditions like `import`, `default`, `module` and, with `browser: true`, `browser`. If there's no `exports`, it falls back to `mainFields`, by default `["module", "main"]`. You can add your own conditions with `exportConditions`, for example `["development"]`.

```js
nodeResolve({
  browser: true,
  exportConditions: ["development"],
  extensions: [".js", ".ts"],
});
```

## 47: Why does plugin order matter?

Hooks run in the order the plugins are listed, so a plugin sees the output of the plugins before it. Some typical rules:

- `alias` goes early so it can change import paths before other plugins resolve them.
- `node-resolve` usually goes before `commonjs`.
- `commonjs` usually goes before `babel`, so Babel sees ES module code.
- Minifiers go at the end or in `output.plugins`.

If something doesn't work, the plugin order is one of the first things to check.

## 48: What is the difference between plugins and output.plugins?

`plugins` (top level) can use all hooks, including build hooks like `transform`. `output.plugins` only use output generation hooks and run for one output only. That makes them a good place for things that only apply to one output, like minifying just the `.min.js` build:

```js
import terser from "@rollup/plugin-terser";

export default {
  input: "src/index.js",
  output: [
    { file: "dist/lib.js", format: "es" },
    { file: "dist/lib.min.js", format: "es", plugins: [terser()] },
  ],
};
```

## 49: How do you mark all dependencies as external in a library build?

Read them from `package.json` and use a function so deep imports like `lodash-es/debounce` also count:

```js
import { readFileSync } from "node:fs";

const pkg = JSON.parse(
  readFileSync(new URL("./package.json", import.meta.url), "utf8"),
);
const deps = [
  ...Object.keys(pkg.dependencies ?? {}),
  ...Object.keys(pkg.peerDependencies ?? {}),
];

export default {
  input: "src/index.js",
  external: (id) => deps.some((dep) => id === dep || id.startsWith(dep + "/")),
  output: { dir: "dist", format: "es" },
};
```

It's also common to make Node built-ins like `node:fs` external with `id.startsWith("node:")`.

## 50: How do you build a library as both ESM and CommonJS?

Use one input with two outputs and point to them from `package.json`:

```js
export default {
  input: "src/index.js",
  external: ["react"],
  output: [
    { file: "dist/index.mjs", format: "es", sourcemap: true },
    {
      file: "dist/index.cjs",
      format: "cjs",
      sourcemap: true,
      exports: "named",
    },
  ],
};
```

```json
{
  "name": "my-lib",
  "type": "module",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs"
    }
  }
}
```

Add a `"types"` condition first if you ship TypeScript declarations.

## 51: What does output.exports do?

It controls how exports look in CommonJS, AMD and UMD output:

- `auto` (default): picks based on what the entry exports.
- `default`: only one default export, which becomes `module.exports = value`.
- `named`: exports become properties, and the default export becomes `exports.default`.
- `none`: the entry exports nothing.

Mixing a default and named exports with `auto` gives the `MIXED_EXPORTS` warning, because CommonJS users would need to write `require("lib").default`. Setting `exports: "named"` makes the choice explicit.

## 52: What does output.interop do?

It controls how a CommonJS-style external's default import is read, for example `import React from "react"` in a `cjs` or `umd` build. The options are `default` (the default), `esModule`, `auto`, `defaultOnly` and `compat`. `auto` checks the `__esModule` flag at runtime and works for most mixed packages. `esModule` assumes the externals are transpiled ES modules and gives the smallest code. Pick the one that matches how your externals are published.

## 53: How do you control chunk splitting with manualChunks?

`output.manualChunks` lets you group modules into named chunks. A common use is a vendor chunk:

```js
output: {
  dir: "dist",
  format: "es",
  manualChunks(id) {
    if (id.includes("node_modules")) {
      return "vendor";
    }
  },
}
```

The object form works too: `manualChunks: { react: ["react", "react-dom"] }`. By default, Rollup also pulls the dependencies of those modules into the same chunk. Be careful with one big vendor chunk: it can make pages download code they don't need.

## 54: What does output.preserveModules do?

Instead of combining modules into chunks, Rollup writes one output file per input module, keeping your folder structure:

```js
output: {
  dir: "dist",
  format: "es",
  preserveModules: true,
  preserveModulesRoot: "src",
}
```

This is popular for component libraries, because the user's bundler can tree shake at the file level and deep imports like `my-lib/button` are possible. `preserveModulesRoot` removes the `src` folder from the output paths.

## 55: What does inlineDynamicImports do?

`output.inlineDynamicImports: true` puts dynamically imported modules into the main chunk instead of separate files. You need it when you want one file but the code has `import()`, for example for an `iife` build or a single file Node script. The `import()` calls still work, they just resolve to code that is already in the bundle.

## 56: How does Rollup handle CSS?

Rollup only understands JavaScript, so CSS needs a plugin. Common options are `rollup-plugin-postcss` (can inject styles, extract a CSS file, and run PostCSS and CSS modules) or a small custom plugin that emits a CSS asset. In a Vite project, Vite handles CSS for you. For a library you usually extract a separate `.css` file so users can decide how to load it.

## 57: How do you emit an asset from a plugin?

Call `this.emitFile` with `type: "asset"`:

```js
export default function versionFile() {
  return {
    name: "version-file",
    generateBundle() {
      this.emitFile({
        type: "asset",
        fileName: "version.json",
        source: JSON.stringify({ builtAt: Date.now() }),
      });
    },
  };
}
```

If you pass `name` instead of `fileName`, Rollup uses `assetFileNames` and can add a hash. `emitFile` returns a reference id you can use later with `this.getFileName(referenceId)`.

## 58: How do you reference an emitted file's URL from code?

Use `import.meta.ROLLUP_FILE_URL_<referenceId>`. Rollup replaces it with the correct URL for the output format:

```js
import { readFileSync } from "node:fs";

export default function svgUrl() {
  return {
    name: "svg-url",
    load(id) {
      if (!id.endsWith(".svg")) return null;
      const referenceId = this.emitFile({
        type: "asset",
        name: id.split("/").pop(),
        source: readFileSync(id),
      });
      return `export default import.meta.ROLLUP_FILE_URL_${referenceId};`;
    },
  };
}
```

`@rollup/plugin-url` does this for you with images and fonts.

## 59: What are the main options of @rollup/plugin-commonjs?

- `include` / `exclude`: which files to convert. By default it only looks at files that use CommonJS.
- `transformMixedEsModules`: also convert files that mix `import` and `require`.
- `requireReturnsDefault`: what `require()` of an ES module returns.
- `ignoreDynamicRequires`: leave `require(variable)` calls alone instead of failing.
- `strictRequires`: wrap modules in functions so `require` runs lazily in the original order, which fixes problems with circular requires and side effects.
- `defaultIsModuleExports`: whether the default import equals `module.exports`.

## 60: How do you use Babel with Rollup?

Use `@rollup/plugin-babel`, place it after `commonjs`, and choose how helpers are included:

```js
import { babel } from "@rollup/plugin-babel";

export default {
  plugins: [
    nodeResolve(),
    commonjs(),
    babel({
      babelHelpers: "bundled",
      exclude: "node_modules/**",
    }),
  ],
};
```

`babelHelpers: "bundled"` puts one copy of each helper in the bundle, which is good for apps. For libraries, `"runtime"` with `@babel/plugin-transform-runtime` imports helpers from `@babel/runtime` instead, so many libraries can share them.

## 61: How do you set up path aliases?

Use `@rollup/plugin-alias`:

```js
import alias from "@rollup/plugin-alias";
import { fileURLToPath } from "node:url";

export default {
  plugins: [
    alias({
      entries: [
        {
          find: "@",
          replacement: fileURLToPath(new URL("./src", import.meta.url)),
        },
      ],
    }),
    nodeResolve(),
  ],
};
```

Note that TypeScript `paths` in `tsconfig.json` are only for the type checker. Rollup doesn't read them, so you need the alias plugin (or a plugin that reads `tsconfig` paths) too.

## 62: How do you generate TypeScript declaration files?

Two common ways:

1. `@rollup/plugin-typescript` with `declaration: true` and `declarationDir` inside the output directory. It writes one `.d.ts` per source file.
2. `rollup-plugin-dts` as a second build, which bundles all declarations into one file:

```js
import { dts } from "rollup-plugin-dts";

export default [
  {
    input: "src/index.ts",
    output: { file: "dist/index.js", format: "es" },
    plugins: [typescript()],
  },
  {
    input: "src/index.ts",
    output: { file: "dist/index.d.ts", format: "es" },
    plugins: [dts()],
  },
];
```

Many projects also just run `tsc --emitDeclarationOnly` next to Rollup.

## 63: How do you use Rollup with the JavaScript API?

Import `rollup`, create a bundle, write the outputs and close it:

```js
import { rollup } from "rollup";

let bundle;
try {
  bundle = await rollup({ input: "src/main.js" });
  await bundle.write({ file: "dist/bundle.js", format: "es" });
} catch (error) {
  console.error(error);
  process.exitCode = 1;
} finally {
  await bundle?.close();
}
```

Use `bundle.generate()` instead of `write()` to get the code in memory without writing files. `close()` lets plugins clean up in their `closeBundle` hook.

## 64: How do you use watch mode from the JavaScript API?

Use `watch()` and listen to events:

```js
import { watch } from "rollup";

const watcher = watch({
  input: "src/main.js",
  output: { dir: "dist", format: "es" },
});

watcher.on("event", (event) => {
  if (event.code === "BUNDLE_END") {
    console.log(`Built in ${event.duration}ms`);
    event.result.close();
  }
  if (event.code === "ERROR") {
    console.error(event.error);
    event.result?.close();
  }
});

// later: await watcher.close();
```

The event codes are `START`, `BUNDLE_START`, `BUNDLE_END`, `END` and `ERROR`. You should close `event.result` so plugins can free resources.

## 65: What is the treeshake option and what presets does it have?

`treeshake` is `true` by default. You can set it to `false` to turn tree shaking off (useful for debugging), or use a preset:

- `"recommended"`: works for most code, ignores some rare cases.
- `"safest"`: keeps more code to avoid breaking unusual code.
- `"smallest"`: removes as much as possible and assumes your code has no hidden side effects.

You can combine a preset with single options:

```js
treeshake: {
  preset: "smallest",
  propertyReadSideEffects: true,
}
```

## 66: What is a side effect and how does it affect tree shaking?

A side effect is code that does something just by running, like changing a global, adding a polyfill or logging. Rollup must keep code with side effects even if nothing imports its exports. If Rollup can't prove a function call is free of side effects, it keeps the call. That's why badly written or "unknown" code often stays in the bundle even when unused.

## 67: How does the package.json sideEffects field work with Rollup?

`"sideEffects": false` in a package's `package.json` tells bundlers that importing a module from it does nothing by itself, so modules whose exports aren't used can be dropped. You can also list files that do have side effects:

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js"]
}
```

With Rollup, this field is read by `@rollup/plugin-node-resolve`. You can also control it directly with `treeshake.moduleSideEffects`.

## 68: What do the pure and no-side-effects annotations do?

`/*#__PURE__*/` before a function call tells Rollup that this one call has no side effects, so it can be removed if the result isn't used:

```js
export const store = /*#__PURE__*/ createStore();
```

`/*#__NO_SIDE_EFFECTS__*/` before a function declaration marks every call of that function as pure:

```js
/*#__NO_SIDE_EFFECTS__*/
export function defineComponent(options) {
  return options;
}
```

Rollup respects them as long as `treeshake.annotations` is `true`, which is the default.

## 69: What is the difference between onLog and onwarn?

Both let you handle messages from Rollup. `onwarn` is older and only gets warnings. `onLog` gets all logs (`warn`, `info` and `debug`) and is the newer, preferred way:

```js
export default {
  onLog(level, log, handler) {
    if (
      log.code === "CIRCULAR_DEPENDENCY" &&
      log.ids?.[0]?.includes("node_modules")
    ) {
      return; // ignore circular deps inside packages
    }
    if (level === "warn") {
      handler("error", log); // turn other warnings into errors
      return;
    }
    handler(level, log);
  },
};
```

The `logLevel` option (`"info"` by default) controls which logs are shown.

## 70: How do you make the build fail on warnings?

On the CLI use `--failAfterWarnings`. It finishes the build, then exits with an error if there were warnings. In the config you can turn warnings into errors with `onLog`, as in the previous answer. In CI this helps you catch new circular dependencies or missing exports before they reach production.

## 71: What does the CIRCULAR_DEPENDENCY warning mean and should you fix it?

It means module A imports B and B (directly or through other modules) imports A. Rollup can bundle it, but the order of execution may mean one module reads a variable before it's set, which gives `undefined` or a TDZ error at runtime. Circular deps in your own code are worth fixing, often by moving shared code to a third module. Circular deps inside `node_modules` are usually ignored.

## 72: How do you see what is making the bundle big?

Use `rollup-plugin-visualizer`, which creates an HTML report (treemap, sunburst and others) of what each module contributes:

```js
import { visualizer } from "rollup-plugin-visualizer";

export default {
  plugins: [visualizer({ filename: "stats.html", gzipSize: true })],
};
```

You can also check `bundle.modules` in `generateBundle` to see each module's rendered size, or turn tree shaking off and on to compare.

## 73: How do you write a TypeScript config file?

Rollup loads config files with Node, so a `.ts` file needs a plugin to compile it:

```bash
npx rollup -c rollup.config.ts --configPlugin typescript
```

`--configPlugin` loads the plugin (here `@rollup/plugin-typescript`) only to transform the config file. In the config you can then use `defineConfig` with full types. Remember that `tsconfig.json` must include the config file, or the plugin will skip it.

## 74: How do you export a function from the config file?

A config can export a function. Rollup calls it with the CLI args and uses what it returns, which can be a promise:

```js
// rollup.config.mjs
export default (commandLineArgs) => {
  const isProd = commandLineArgs.configProd === true;
  return {
    input: "src/main.js",
    output: { file: "dist/bundle.js", format: "es", sourcemap: !isProd },
  };
};
```

```bash
npx rollup -c --configProd
```

Using the `config` prefix for custom flags stops Rollup from complaining that it doesn't know the flag.

## 75: How do you build an IIFE or UMD bundle for a script tag?

Use the `iife` or `umd` format, give it a `name`, and include the dependencies or map them with `globals`:

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
import terser from "@rollup/plugin-terser";

export default {
  input: "src/widget.js",
  output: {
    file: "dist/widget.min.js",
    format: "iife",
    name: "Widget",
    sourcemap: true,
  },
  plugins: [nodeResolve({ browser: true }), terser()],
};
```

These formats can't do code splitting, so if your code has `import()` you also need `inlineDynamicImports: true`.

## 76: What does the cache option do?

When you build several times with the JavaScript API, you can pass the previous bundle's cache so Rollup skips modules that didn't change:

```js
let cache;

async function build() {
  const bundle = await rollup({ input: "src/main.js", cache });
  cache = bundle.cache;
  await bundle.write({ dir: "dist", format: "es" });
  await bundle.close();
}
```

Watch mode does this for you. Plugins can also store their own data in `this.cache`.

## 77: How do you import files like .wasm or images?

Use the matching plugin:

- `@rollup/plugin-url`: small files become base64 data URLs, larger ones are copied and imported as URLs.
- `@rollup/plugin-image`: images as base64 strings.
- `@rollup/plugin-wasm`: imports WebAssembly modules, inlined or as separate files.

You can also write a small plugin with `this.emitFile` and `import.meta.ROLLUP_FILE_URL_...`, as shown earlier.

## 78: How do you handle dynamic imports that use variables in the path?

Rollup can't know which files a fully dynamic import needs. `@rollup/plugin-dynamic-import-vars` turns a template string import into code that covers all files matching the pattern:

```js
import dynamicImportVars from "@rollup/plugin-dynamic-import-vars";

export default {
  plugins: [dynamicImportVars()],
};
```

```js
const messages = await import(`./locales/${lang}.js`);
```

The path must start with `./` or `../` and have a file extension, so the plugin can build the list of matching files.

## 79: How do you combine Rollup with esbuild or SWC for speed?

The TypeScript plugin and Babel are slow on big projects. `rollup-plugin-esbuild` or `@rollup/plugin-swc` do the same transform much faster in native code, and can also minify. Rollup still does the bundling and tree shaking:

```js
import esbuild from "rollup-plugin-esbuild";

export default {
  input: "src/index.ts",
  output: { dir: "dist", format: "es" },
  plugins: [esbuild({ target: "es2020", minify: true })],
};
```

The trade-off is that they don't type check, so run `tsc --noEmit` in CI.

## 80: How do you keep the "use client" directive or other module-level directives?

Rollup removes directives like `"use client"` from modules when it bundles them, because after bundling they would apply to the whole chunk, and it shows a `MODULE_LEVEL_DIRECTIVE` warning. For React Server Components libraries, the common fixes are:

- Use `preserveModules: true` so each file stays separate, plus a plugin like `rollup-plugin-preserve-directives` to keep the directive at the top of each output file.
- Or add the directive with `output.banner` for a chunk that should be all client code.

# Advanced Questions (81-120)

## 81: What changed in Rollup 4 compared to Rollup 3?

The main changes:

- The parser was switched from Acorn to SWC's parser, written in Rust. Rollup ships it as native binaries in platform packages like `@rollup/rollup-linux-x64-gnu`. For platforms without a binary there is `@rollup/wasm-node`.
- Node.js 18 or newer is required.
- Import assertions were replaced by import attributes (`with { type: "json" }`), and the plugin API uses `attributes` instead of `assertions`.
- `this.resolve` uses `skipSelf: true` by default, so a plugin calling it from its own `resolveId` doesn't loop on itself.
- The default `maxParallelFileOps` went up to 1000.

Most config files work without changes. The usual problems come from plugins that used removed APIs, or from CI images where the optional native package wasn't installed.

## 82: Why does Rollup 4 sometimes fail with "Cannot find module @rollup/rollup-..."?

Rollup 4 loads a native binary from an optional dependency for your OS and CPU. If `node_modules` or the lock file was created on a different platform (for example on macOS and then copied into a Linux Docker image), or if optional dependencies were skipped with `--omit=optional`, the right package is missing. The fixes are: install dependencies inside the target environment, don't skip optional deps, or delete the lock file and reinstall. Using the `@rollup/wasm-node` package (for example through npm `overrides`) also works, it's just slower.

## 83: How does Rollup's tree shaking work internally?

Rollup parses every module into an AST and builds a scope for each one, linking every variable use to its declaration across modules. Then it starts from the entry points and marks statements as "included" if they have side effects or are needed by something already included. It repeats this until nothing new gets included, because including one thing can make another thing needed.

Along the way it tracks values, so it can drop code like `if (false) {}`, find out that an object property is never read, or see that a function call has no side effects. When it can't be sure, for example when a value escapes into unknown code, it "deoptimizes" and keeps the code to stay safe.

## 84: Why does a function call sometimes stay in the bundle even though its result isn't used?

Rollup keeps any call it can't prove is free of side effects. Common reasons:

- The function comes from an external module or is passed in, so Rollup can't see its body.
- The function changes a global, writes to a parameter or reads a property that might have a getter.
- The code is in a class with a static block or uses `Object.defineProperty`.

You can fix it by adding `/*#__PURE__*/` to the call, `/*#__NO_SIDE_EFFECTS__*/` to the function, listing it in `treeshake.manualPureFunctions`, or by rewriting the code so the side effect goes away. `experimentalLogSideEffects: true` logs the first side effect Rollup finds in each module, which helps find the cause.

## 85: What are treeshake.moduleSideEffects and propertyReadSideEffects?

`moduleSideEffects` decides whether a module is kept just because it is imported, even when none of its exports are used. It can be `true`, `false`, `"no-external"` (externals have no side effects), a list of ids or a function `(id, external) => boolean`. Setting it to `false` is the biggest win but breaks imports that are only there for their side effects, like `import "./polyfill.js"`.

`propertyReadSideEffects` (default `true`) assumes a property read might trigger a getter. Setting it to `false` lets Rollup remove unused reads like `obj.a;`, but it's wrong if your code depends on getters running.

## 86: How does Rollup handle live bindings?

ES module exports are live: if a module changes an exported `let`, importers see the new value. Rollup keeps this by referring to the same variable instead of copying the value. Since everything is in one scope after bundling, it usually just works without extra code.

For CommonJS-like output with externals, `output.externalLiveBindings` (default `true`) creates getters so re-exported values stay live. Setting it to `false` gives smaller code but freezes the values, which is fine if no external ever reassigns its exports.

## 87: How does Rollup decide what goes into each chunk?

Without `manualChunks`, Rollup looks at which entry points (static or dynamic) each module is reachable from. Modules reachable from the same set of entries go into the same chunk. So a module used only by entry A goes into A's chunk, and a module used by both A and B goes into a shared chunk. This means no module is ever duplicated and code never runs twice, but it can create many small chunks. `output.experimentalMinChunkSize` can merge small chunks into others when it is safe, so there are fewer requests.

## 88: What is preserveEntrySignatures?

It controls whether an entry chunk must export exactly what its entry module exports:

- `"exports-only"` (default): keep the signature if the entry has exports, otherwise Rollup may merge other code in freely.
- `"strict"`: the entry chunk exports exactly the entry module's exports. Rollup may need an extra facade chunk to do this.
- `"allow-extension"`: the chunk can export more than the entry, but never less.
- `false`: no guarantee, useful for apps where nobody imports the entry.

For libraries, `"strict"` is the safe choice. For apps, `false` can give fewer chunks. Emitted chunks can set their own `preserveSignature`.

## 89: What does hoistTransitiveImports do?

When an entry chunk imports a chunk that imports other chunks, Rollup adds empty imports of those other chunks to the entry by default (`hoistTransitiveImports: true`). This lets the browser start downloading all of them right away instead of finding them one level at a time. It costs a few extra import lines. You can turn it off if those lines cause trouble, and it's ignored with `preserveModules`.

## 90: How do content hashes work, and why does a change in one file change hashes in other files?

Since Rollup 3, file names with `[hash]` are first rendered with placeholders. After all chunks are rendered, Rollup computes each hash from the chunk's content plus the hashes of the chunks it imports, then swaps the placeholders for the real values. Because a chunk's code contains the file names of its imports, changing a leaf chunk changes its hash and the import paths in all chunks that import it, so their hashes change too.

That's correct behavior, but it can bust the cache for many files. Keeping often-changing code in leaf chunks and stable vendor code apart helps. In `renderChunk`, plugins must leave the placeholders as they are.

## 91: What does augmentChunkHash do?

It lets a plugin add extra data to a chunk's hash. Use it when the plugin changes output in a way Rollup can't see from the code, for example values injected later in `generateBundle`:

```js
export default function buildFlags(flags) {
  return {
    name: "build-flags",
    augmentChunkHash(chunkInfo) {
      if (chunkInfo.isEntry) {
        return JSON.stringify(flags);
      }
    },
  };
}
```

Without it, two builds with different content could get the same file name, and users would get stale files from the cache.

## 92: How do you resolve an id with other plugins from inside your own resolveId?

Call `this.resolve`. It runs the `resolveId` hooks of all plugins (except yours, since `skipSelf` is `true` by default) and Rollup's default resolution:

```js
export default function ignoreTestHelpers() {
  return {
    name: "ignore-test-helpers",
    async resolveId(source, importer, options) {
      const resolved = await this.resolve(source, importer, options);
      if (resolved && resolved.id.includes("/__test-helpers__/")) {
        return { id: "\0empty", moduleSideEffects: false };
      }
      return resolved;
    },
    load(id) {
      if (id === "\0empty") return "export default {}";
    },
  };
}
```

Pass `options` through so things like `isEntry` and `attributes` aren't lost.

## 93: What is this.load and when do you use it?

`this.load({ id })` loads, transforms and parses a module and returns its `ModuleInfo`. It's useful when your plugin needs to look at a module before deciding something, for example in `resolveId` or `transform`:

```js
async resolveId(source, importer, options) {
  const resolved = await this.resolve(source, importer, options);
  if (!resolved || resolved.external) return resolved;
  const info = await this.load(resolved);
  if (info.hasDefaultExport === false) {
    this.warn(`${source} has no default export`);
  }
  return resolved;
}
```

With `resolveDependencies: true` the module's imports are resolved too, which you need for walking the graph. Be careful: awaiting `this.load` for a module that is waiting on you can cause a deadlock in circular graphs.

## 94: How do plugins share data with each other?

There are a few ways:

- `meta` on modules: `resolveId`, `load` and `transform` can return `meta: { myPlugin: {...} }`, and others read it with `this.getModuleInfo(id).meta`.
- The `api` property: a plugin can expose methods, and others find it in the `options` or `buildStart` hook through the plugins list.
- `custom` options in `this.resolve(source, importer, { custom: { myPlugin: {...} } })`, which reach other plugins' `resolveId`.

Use your plugin's name as the key in `meta` and `custom` so plugins don't overwrite each other's data.

## 95: What are hook filters and why were they added?

A hook filter is a `filter` property on `resolveId`, `load` or `transform` that tells Rollup when to call the hook:

```js
export default function graphql() {
  return {
    name: "graphql",
    transform: {
      filter: { id: { include: /\.graphql$/ } },
      handler(code) {
        return { code: `export default ${JSON.stringify(code)};`, map: null };
      },
    },
  };
}
```

`id` can be a string (picomatch pattern, except in `resolveId`), a regex, a list, or an object with `include` and `exclude`. `transform` can also filter by `code`. The result is the same as checking inside the handler, but Rollup can skip the call completely. That matters more in Rolldown and Vite, where skipping the call avoids crossing from Rust into JavaScript for every module.

## 96: How do you control when a plugin hook runs compared to other plugins?

Write the hook as an object with `order` and `handler`:

```js
export default function earlyTransform() {
  return {
    name: "early-transform",
    transform: {
      order: "pre",
      handler(code, id) {
        // runs before transform hooks without an order
      },
    },
  };
}
```

`order` can be `"pre"`, `"post"` or `null`. For parallel hooks like `writeBundle`, you can add `sequential: true` so this hook runs after earlier ones finish and before later ones start. This is better than telling users "put this plugin first".

## 97: What is syntheticNamedExports?

A module can set `syntheticNamedExports` (from `resolveId`, `load` or `transform`) so that missing named exports are read as properties of one export, by default `default`. The CommonJS plugin uses this: a converted module only has a default export (the `module.exports` object), but `import { readFile } from "cjs-lib"` still works because Rollup reads `readFile` from that object. Real named exports always win over synthetic ones.

## 98: What does shimMissingExports do?

If a module imports a name that another module doesn't export, Rollup throws an error by default. With `shimMissingExports: true`, Rollup instead creates a variable with value `undefined` for that name and shows a warning. It's a way to get legacy or broken code to build, but it hides real bugs, so use it only as a temporary fix.

## 99: How does Rollup chain source maps from multiple plugins?

Each `transform` hook can return a `map`. Rollup combines the maps from all transforms, and then from `renderChunk` hooks, so the final map points back to the original source. If one plugin changes code and returns `map: null` or no map, the chain breaks and positions after that point are wrong. Rollup warns about this with `SOURCEMAP_BROKEN`. Plugins should use `magic-string` and return `s.generateMap({ hires: true })`, or return `{ mappings: "" }` when the change doesn't move any code.

## 100: Which output options help with source maps in production?

- `sourcemap: "hidden"`: write maps but don't add the comment, so you can upload them to Sentry and not expose them.
- `sourcemapExcludeSources: true`: don't embed the original source text, which makes maps smaller and hides your code.
- `sourcemapPathTransform`: change the paths in `sources`, for example to make them relative to the repo.
- `sourcemapIgnoreList`: mark files (by default those in `node_modules`) so DevTools skips them while debugging.
- `sourcemapBaseUrl`: use an absolute URL in the comment, useful when maps are on another host.

## 101: What does shouldTransformCachedModule do?

When you build with a cache, Rollup reuses transformed code for modules that didn't change. But sometimes the result depends on something outside the file, like a config file or another module. `shouldTransformCachedModule` lets a plugin say "transform this one again":

```js
shouldTransformCachedModule({ id, meta }) {
  return meta.myPlugin?.configVersion !== currentConfigVersion;
}
```

A simpler option for file dependencies is `this.addWatchFile(path)` in `transform`, which makes Rollup re-run it when that file changes.

## 102: How do you measure where build time goes?

Set `perf: true` and read the timings:

```js
const bundle = await rollup({ input: "src/main.js", perf: true });
await bundle.generate({ format: "es" });
console.log(bundle.getTimings());
await bundle.close();
```

On the CLI, `--perf` prints them. The timings show parsing, each plugin's hooks, tree shaking and rendering. Very often one slow `transform` plugin (Babel or the TypeScript plugin) takes most of the time, and switching to esbuild or SWC for that step gives the biggest win.

## 103: What is maxParallelFileOps and when would you change it?

It limits how many files Rollup reads or writes at the same time. The default is 1000. On systems with a low open file limit, a big project can fail with `EMFILE: too many open files`, and lowering it fixes that. On fast disks raising it rarely helps much. It's worth knowing about when a build works on one machine and fails in a container with stricter limits.

## 104: How do you parse code into an AST inside a plugin?

In hooks, use `this.parse(code)`. Outside the plugin context, Rollup 4 exports the same parser:

```js
import { parseAst } from "rollup/parseAst";

const ast = parseAst("export const a = 1;");
console.log(ast.body[0].type); // ExportNamedDeclaration
```

There's also `parseAstAsync`, which can parse off the main thread. The AST follows the ESTree format. Also, `transform` can return an `ast` along with `code` so Rollup doesn't parse it again, but it must match the code exactly.

## 105: What do resolveImportMeta and resolveFileUrl do?

`resolveImportMeta` lets a plugin decide what `import.meta` or `import.meta.someProp` becomes in the output. Rollup has defaults per format; for example in a CJS build `import.meta.url` turns into code based on `__filename` or `document.currentScript`.

`resolveFileUrl` controls the code for `import.meta.ROLLUP_FILE_URL_...` references, for example to load assets from a CDN:

```js
resolveFileUrl({ fileName }) {
  return `new URL(${JSON.stringify(fileName)}, "https://cdn.example.com/").href`;
}
```

## 106: How do you bundle a Web Worker with Rollup?

Two common ways:

1. Add the worker as its own entry point or emit it from a plugin with `this.emitFile({ type: "chunk", id: "src/worker.js" })`, then use the reference in `new Worker(import.meta.ROLLUP_FILE_URL_<ref>, { type: "module" })`.
2. Use a plugin like `@surma/rollup-plugin-off-main-thread` that also handles worker code splitting for browsers without module workers.

Watch out for the format: a classic worker can't use `import`, so either use `{ type: "module" }` or build the worker as `iife`.

## 107: What is implicitlyLoadedAfterOneOf?

It's an option for emitted chunks. It tells Rollup that this chunk is always loaded after one of the listed modules has already run. A good example is a service worker or a page script loaded from an HTML file. Rollup can then leave out of the chunk any code that those modules already loaded, instead of duplicating it or creating an extra shared chunk. It's mostly useful in HTML or multi-page plugins.

## 108: Why can manualChunks break your app and how do you avoid it?

`manualChunks` changes which code ends up together, and that can change execution order. If you put a module into a manual chunk that also ends up importing from the entry chunk, you can get a circular import between chunks. Then some code runs before what it depends on, and you get errors like "Cannot access X before initialization". Also, since dependencies are pulled into the manual chunk by default, a big vendor chunk can contain code that some pages never use.

To avoid it: keep manual chunks to stable libraries without side effects, check the output for chunks that import each other, and consider `output.onlyExplicitManualChunks` so dependencies aren't pulled in automatically. It's deprecated as an option because it becomes the default behavior in Rollup 5.

## 109: How would you debug a "process is not defined" error in a browser bundle?

Some dependency reads `process.env.NODE_ENV` or other Node globals, and browsers don't have `process`. Steps:

1. Search the output for `process.` to find which module it comes from (source maps or the visualizer help).
2. Add `@rollup/plugin-replace` to replace `process.env.NODE_ENV` with a string.
3. Make sure `nodeResolve({ browser: true })` is set, so packages with a browser build use it.
4. If a package really needs Node APIs, find a browser version or a polyfill, but adding polyfills should be a last step.

## 110: Why might lodash not get tree shaken, and how do you fix it?

The `lodash` package is CommonJS. After `@rollup/plugin-commonjs` converts it, it's one big module object and Rollup can't tell which functions you use, so you get the whole library. Fixes:

- Use `lodash-es`, which is ES modules, and import named functions.
- Or import single files like `lodash/debounce`.

The same applies to any CommonJS package: tree shaking works best with ES module packages.

## 111: How do you avoid shipping duplicate copies of React in a library?

Mark React as external and list it in `peerDependencies`, not `dependencies`:

```js
export default {
  input: "src/index.jsx",
  external: ["react", "react-dom", "react/jsx-runtime"],
  output: { dir: "dist", format: "es" },
  jsx: "react-jsx",
};
```

`react/jsx-runtime` is easy to forget. If your plugins compile JSX to the new runtime, that import shows up and gets bundled unless you mark it external. Using a function in `external` that also matches subpaths is the safest. In an app with linked packages (monorepos), `nodeResolve({ dedupe: ["react"] })` makes all imports resolve to one copy.

## 112: What is the jsx option in Rollup 4?

Rollup 4 can parse and transform JSX by itself with the `jsx` option. It accepts `false` (default), a preset like `"react"`, `"react-jsx"`, `"preserve"` or `"preserve-react"`, or an object with your own settings such as `factory`, `fragment` and `importSource`. `"preserve"` keeps JSX in the output for another tool to handle. It's handy for simple JSX libraries, but if you also use TypeScript or need more Babel features, you'll still use a plugin for the transform.

## 113: How do you make a library work well for tree shaking in consumers' bundlers?

- Publish ES module output, not only CommonJS.
- Set `"sideEffects": false` (or list files with side effects) in `package.json`.
- Consider `preserveModules: true` so each module is a separate file.
- Avoid top-level code with side effects, like registering things on import.
- Add `/*#__PURE__*/` to top-level calls like `createContext()` or `defineComponent()`.
- Don't export one big object; export functions separately.
- Use the `exports` field so users get the ES module build.

## 114: What is the dual package hazard and how does it affect a Rollup library?

If a package ships both ESM and CJS builds, Node can load both in the same app: one from an `import` and another from a `require`. Then you have two copies of module state, so things like `instanceof` checks, singletons or React context can break. Ways to deal with it:

- Ship only ESM (Node 20.19+ and 22.12+ can `require()` ES modules).
- Keep state in one shared CJS file that both builds import.
- Make the ESM build a thin wrapper that re-exports the CJS build.

Rollup can build any of these, but you need to choose the design.

## 115: How would you set up Rollup for a monorepo with many packages?

A common approach:

- Each package has a small `rollup.config.mjs` that imports a shared config factory from a tools package, so plugin versions and settings stay the same.
- The factory reads each package's `package.json` to set `input`, outputs and `external` (all dependencies and peer dependencies).
- A task runner like Turborepo or Nx builds packages in dependency order and caches results.
- Declarations are built with `tsc -b` using project references, or `rollup-plugin-dts`.

Running one Rollup process with an array of configs for all packages also works, but it's harder to cache and to build just one package.

## 116: What security issues should you think about in a Rollup build?

- Plugins run with full access to your machine and CI secrets. Use well-known ones, pin versions and check the lock file.
- `@rollup/plugin-replace` or `define`-style setups can put secrets into public bundles if you replace every `process.env` key. Only replace values you want public.
- Source maps with `sourcesContent` expose your source code. Use `hidden` maps or exclude sources in public builds.
- File names can come from user data in plugins. Recent Rollup 4 versions throw an error when an output file path would leave the output directory, and `output.sanitizeFileName` cleans unsafe characters.
- Watch mode and dev server plugins should not be exposed to the network.

## 117: How do Rollup and Rolldown compare?

Rolldown is a bundler written in Rust by the Vite team. It aims to keep Rollup's plugin API and most of its options while being much faster, and it includes things Rollup leaves to plugins, like node resolution, CommonJS support, TypeScript and JSX transforms and minification. Vite 8 uses it by default.

Rollup is still the more mature option, with very predictable output and the largest plugin ecosystem, and is a solid choice for libraries. When moving a Rollup config to Rolldown, most plugins work, but some options and plugin APIs differ. Hook filters are one feature that came about to make plugins fast in both.

## 118: How would you test a Rollup plugin?

Call `rollup()` in a test with your plugin and a small virtual or fixture input, then check the generated output:

```js
import { rollup } from "rollup";
import { expect, test } from "vitest";
import myPlugin from "../src/index.js";

test("transforms .graphql files", async () => {
  const bundle = await rollup({
    input: "test/fixtures/main.js",
    plugins: [myPlugin()],
  });
  const { output } = await bundle.generate({ format: "es" });
  await bundle.close();

  expect(output[0].code).toContain("query GetUser");
});
```

Test against the real output, not internal functions, because hook order and context behavior matter. Also test watch mode and error cases (`await expect(rollup(...)).rejects.toThrow()`).

## 119: How would you build a library that ships to npm, a CDN and Node?

One config with several outputs:

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
import terser from "@rollup/plugin-terser";

export default [
  {
    input: "src/index.js",
    external: ["date-fns"],
    output: [
      { file: "dist/index.mjs", format: "es", sourcemap: true },
      {
        file: "dist/index.cjs",
        format: "cjs",
        exports: "named",
        sourcemap: true,
      },
    ],
  },
  {
    input: "src/index.js",
    plugins: [nodeResolve({ browser: true })],
    output: {
      file: "dist/index.umd.min.js",
      format: "umd",
      name: "MyLib",
      sourcemap: true,
      plugins: [terser()],
    },
  },
];
```

The npm builds keep dependencies external. The CDN build bundles everything so it works with one `<script>` tag. Then point `exports`, `main`, `module` and `unpkg`/`jsdelivr` fields in `package.json` at the right files.

## 120: A Rollup build that used to take 20 seconds now takes 3 minutes. How would you investigate?

1. Run with `--perf` (or `perf: true`) to see which plugin or phase grew.
2. Check what changed: a new dependency, a new plugin, a plugin upgrade or a change to `include`/`exclude` so a slow plugin now processes `node_modules`.
3. Look at the module count in the visualizer. A wrong import, for example a barrel file or an icon package imported as a whole, can pull in thousands of modules.
4. Check `transform` plugins without filters that run on every file. Add `include` options or hook filters.
5. Replace Babel or the TypeScript plugin with esbuild or SWC if only syntax transforms are needed, and type check separately.
6. Check for source map settings like `hires` maps or `sourcemap: true` in extra outputs you don't need.
7. In CI, check memory. If Node is close to its heap limit, garbage collection slows the build a lot, and `--max-old-space-size` or fewer parallel builds can help.
