# Webpack Interview Questions and Answers

_Last updated: October 28, 2026_

120 webpack interview questions with answers, split into three levels: 40 easy, 40 moderate and 40 advanced.

The answers target webpack 5 (the 5.10x releases), which is still the current major version. webpack 6 is on the roadmap but not released yet. Code examples use CommonJS `webpack.config.js` files since that's what you'll see in most projects.

## Table of Contents

- [Easy Questions (1-40)](#easy-questions-1-40)
- [Moderate Questions (41-80)](#moderate-questions-41-80)
- [Advanced Questions (81-120)](#advanced-questions-81-120)

### Easy Questions (1-40)

- [1: What is webpack?](#1-what-is-webpack)
- [2: Why do we need a bundler at all?](#2-why-do-we-need-a-bundler-at-all)
- [3: What is the dependency graph?](#3-what-is-the-dependency-graph)
- [4: How do you install webpack?](#4-how-do-you-install-webpack)
- [5: What is webpack.config.js?](#5-what-is-webpackconfigjs)
- [6: Can webpack run without a config file?](#6-can-webpack-run-without-a-config-file)
- [7: What is an entry point?](#7-what-is-an-entry-point)
- [8: How do you set up multiple entry points?](#8-how-do-you-set-up-multiple-entry-points)
- [9: What does the output option do?](#9-what-does-the-output-option-do)
- [10: What are loaders?](#10-what-are-loaders)
- [11: What are plugins?](#11-what-are-plugins)
- [12: What is the difference between a loader and a plugin?](#12-what-is-the-difference-between-a-loader-and-a-plugin)
- [13: What is the mode option?](#13-what-is-the-mode-option)
- [14: What is the difference between development and production mode?](#14-what-is-the-difference-between-development-and-production-mode)
- [15: How do you import CSS files with webpack?](#15-how-do-you-import-css-files-with-webpack)
- [16: How do you handle images and fonts in webpack 5?](#16-how-do-you-handle-images-and-fonts-in-webpack-5)
- [17: What are the four asset module types?](#17-what-are-the-four-asset-module-types)
- [18: What is babel-loader used for?](#18-what-is-babel-loader-used-for)
- [19: How do you use TypeScript with webpack?](#19-how-do-you-use-typescript-with-webpack)
- [20: What does HtmlWebpackPlugin do?](#20-what-does-htmlwebpackplugin-do)
- [21: What is webpack-dev-server?](#21-what-is-webpack-dev-server)
- [22: What is Hot Module Replacement (HMR)?](#22-what-is-hot-module-replacement-hmr)
- [23: What is a source map and how do you enable it?](#23-what-is-a-source-map-and-how-do-you-enable-it)
- [24: What is a chunk?](#24-what-is-a-chunk)
- [25: What is the difference between a module, a chunk and a bundle?](#25-what-is-the-difference-between-a-module-a-chunk-and-a-bundle)
- [26: What is [contenthash] in file names?](#26-what-is-contenthash-in-file-names)
- [27: How do you clean the dist folder before each build?](#27-how-do-you-clean-the-dist-folder-before-each-build)
- [28: What is resolve.extensions?](#28-what-is-resolveextensions)
- [29: What is resolve.alias?](#29-what-is-resolvealias)
- [30: What does watch mode do?](#30-what-does-watch-mode-do)
- [31: What are the common webpack CLI commands?](#31-what-are-the-common-webpack-cli-commands)
- [32: Which module formats does webpack support?](#32-which-module-formats-does-webpack-support)
- [33: In what order are loaders applied?](#33-in-what-order-are-loaders-applied)
- [34: How do you pass options to a loader?](#34-how-do-you-pass-options-to-a-loader)
- [35: What is DefinePlugin?](#35-what-is-defineplugin)
- [36: How do you use environment variables in the webpack config?](#36-how-do-you-use-environment-variables-in-the-webpack-config)
- [37: What is publicPath?](#37-what-is-publicpath)
- [38: What is a vendor chunk?](#38-what-is-a-vendor-chunk)
- [39: What is MiniCssExtractPlugin?](#39-what-is-minicssextractplugin)
- [40: What is the target option?](#40-what-is-the-target-option)

### Moderate Questions (41-80)

- [41: What is code splitting and what are the ways to do it in webpack?](#41-what-is-code-splitting-and-what-are-the-ways-to-do-it-in-webpack)
- [42: How does dynamic import() work and what are magic comments?](#42-how-does-dynamic-import-work-and-what-are-magic-comments)
- [43: What does SplitChunksPlugin do by default?](#43-what-does-splitchunksplugin-do-by-default)
- [44: How do you configure cacheGroups in splitChunks?](#44-how-do-you-configure-cachegroups-in-splitchunks)
- [45: What is the runtime chunk and why would you split it out?](#45-what-is-the-runtime-chunk-and-why-would-you-split-it-out)
- [46: What is tree shaking and what does it need to work?](#46-what-is-tree-shaking-and-what-does-it-need-to-work)
- [47: What is the sideEffects field in package.json?](#47-what-is-the-sideeffects-field-in-packagejson)
- [48: What is the difference between usedExports and sideEffects optimizations?](#48-what-is-the-difference-between-usedexports-and-sideeffects-optimizations)
- [49: How do you set up long-term caching?](#49-how-do-you-set-up-long-term-caching)
- [50: What is persistent caching in webpack 5?](#50-what-is-persistent-caching-in-webpack-5)
- [51: What is the difference between prefetch and preload?](#51-what-is-the-difference-between-prefetch-and-preload)
- [52: How do you split webpack config for development and production?](#52-how-do-you-split-webpack-config-for-development-and-production)
- [53: How do you set up a proxy in webpack-dev-server?](#53-how-do-you-set-up-a-proxy-in-webpack-dev-server)
- [54: Why do routes return 404 on refresh in webpack-dev-server and how do you fix it?](#54-why-do-routes-return-404-on-refresh-in-webpack-dev-server-and-how-do-you-fix-it)
- [55: Which devtool option should you use in development and production?](#55-which-devtool-option-should-you-use-in-development-and-production)
- [56: How do you customize minification in webpack?](#56-how-do-you-customize-minification-in-webpack)
- [57: How do you find out what makes your bundle big?](#57-how-do-you-find-out-what-makes-your-bundle-big)
- [58: What are performance hints?](#58-what-are-performance-hints)
- [59: What are externals and when would you use them?](#59-what-are-externals-and-when-would-you-use-them)
- [60: Why do you get errors about Node.js core modules like crypto or path in webpack 5?](#60-why-do-you-get-errors-about-nodejs-core-modules-like-crypto-or-path-in-webpack-5)
- [61: How do you use CSS Modules with webpack?](#61-how-do-you-use-css-modules-with-webpack)
- [62: How do you set up Sass and PostCSS with webpack?](#62-how-do-you-set-up-sass-and-postcss-with-webpack)
- [63: What do test, include, exclude and oneOf do in a rule?](#63-what-do-test-include-exclude-and-oneof-do-in-a-rule)
- [64: What is resourceQuery and how can you use it?](#64-what-is-resourcequery-and-how-can-you-use-it)
- [65: How do you build a library with webpack?](#65-how-do-you-build-a-library-with-webpack)
- [66: Can webpack build several configurations at once?](#66-can-webpack-build-several-configurations-at-once)
- [67: How do you expose environment variables to your frontend code?](#67-how-do-you-expose-environment-variables-to-your-frontend-code)
- [68: How can you make a slow webpack build faster?](#68-how-can-you-make-a-slow-webpack-build-faster)
- [69: What is ProvidePlugin?](#69-what-is-provideplugin)
- [70: How do you stop a library like moment.js from bundling all its locales?](#70-how-do-you-stop-a-library-like-momentjs-from-bundling-all-its-locales)
- [71: What happens when you import a module with a variable in the path?](#71-what-happens-when-you-import-a-module-with-a-variable-in-the-path)
- [72: What is require.context and import.meta.webpackContext?](#72-what-is-requirecontext-and-importmetawebpackcontext)
- [73: How do you lazy load routes in a React app built with webpack?](#73-how-do-you-lazy-load-routes-in-a-react-app-built-with-webpack)
- [74: How do you debug "Module not found: Error: Can't resolve" errors?](#74-how-do-you-debug-module-not-found-error-cant-resolve-errors)
- [75: How do you control the build output in the terminal?](#75-how-do-you-control-the-build-output-in-the-terminal)
- [76: How do you set up React Fast Refresh with webpack?](#76-how-do-you-set-up-react-fast-refresh-with-webpack)
- [77: How do you use Web Workers with webpack 5?](#77-how-do-you-use-web-workers-with-webpack-5)
- [78: What does new URL('./file', import.meta.url) do in webpack?](#78-what-does-new-urlfile-importmetaurl-do-in-webpack)
- [79: What is the difference between fullhash, chunkhash and contenthash?](#79-what-is-the-difference-between-fullhash-chunkhash-and-contenthash)
- [80: What were the main changes from webpack 4 to webpack 5?](#80-what-were-the-main-changes-from-webpack-4-to-webpack-5)

### Advanced Questions (81-120)

- [81: Walk through what happens inside webpack during a build.](#81-walk-through-what-happens-inside-webpack-during-a-build)
- [82: What is Tapable?](#82-what-is-tapable)
- [83: How do you write a custom webpack plugin?](#83-how-do-you-write-a-custom-webpack-plugin)
- [84: How do you write a custom loader?](#84-how-do-you-write-a-custom-loader)
- [85: What are pitching loaders?](#85-what-are-pitching-loaders)
- [86: What does the webpack runtime code do?](#86-what-does-the-webpack-runtime-code-do)
- [87: How does webpack load an async chunk at runtime?](#87-how-does-webpack-load-an-async-chunk-at-runtime)
- [88: What is Module Federation?](#88-what-is-module-federation)
- [89: How does sharing work in Module Federation and what is the eager consumption error?](#89-how-does-sharing-work-in-module-federation-and-what-is-the-eager-consumption-error)
- [90: What is scope hoisting?](#90-what-is-scope-hoisting)
- [91: How does tree shaking work internally in webpack?](#91-how-does-tree-shaking-work-internally-in-webpack)
- [92: Why does CommonJS make tree shaking harder?](#92-why-does-commonjs-make-tree-shaking-harder)
- [93: How does webpack know when to invalidate the persistent cache?](#93-how-does-webpack-know-when-to-invalidate-the-persistent-cache)
- [94: Why can the hash of a file change even though its content didn't, and how does webpack 5 handle it?](#94-why-can-the-hash-of-a-file-change-even-though-its-content-didnt-and-how-does-webpack-5-handle-it)
- [95: How do you control where asset modules are written and how they are named?](#95-how-do-you-control-where-asset-modules-are-written-and-how-they-are-named)
- [96: How do you output ES modules from webpack?](#96-how-do-you-output-es-modules-from-webpack)
- [97: What are some useful options under experiments in webpack 5?](#97-what-are-some-useful-options-under-experiments-in-webpack-5)
- [98: What is lazy compilation and when would you use it?](#98-what-is-lazy-compilation-and-when-would-you-use-it)
- [99: How do you make webpack work with a strict Content Security Policy?](#99-how-do-you-make-webpack-work-with-a-strict-content-security-policy)
- [100: How do you add Subresource Integrity to webpack bundles?](#100-how-do-you-add-subresource-integrity-to-webpack-bundles)
- [101: How do you set the public path at runtime?](#101-how-do-you-set-the-public-path-at-runtime)
- [102: How do you profile a slow webpack build?](#102-how-do-you-profile-a-slow-webpack-build)
- [103: How would you speed up builds in a large monorepo with webpack?](#103-how-would-you-speed-up-builds-in-a-large-monorepo-with-webpack)
- [104: A production bundle is 3 MB. How would you approach reducing it?](#104-a-production-bundle-is-3-mb-how-would-you-approach-reducing-it)
- [105: How do you find and fix duplicate packages in a bundle?](#105-how-do-you-find-and-fix-duplicate-packages-in-a-bundle)
- [106: How do you set up webpack for server-side rendering?](#106-how-do-you-set-up-webpack-for-server-side-rendering)
- [107: Your Module Federation host breaks after a remote deploys a new React version. How do you debug and prevent it?](#107-your-module-federation-host-breaks-after-a-remote-deploys-a-new-react-version-how-do-you-debug-and-prevent-it)
- [108: What are the trade-offs when configuring splitChunks for many small chunks?](#108-what-are-the-trade-offs-when-configuring-splitchunks-for-many-small-chunks)
- [109: How does webpack resolve a bare import like import x from 'some-package'?](#109-how-does-webpack-resolve-a-bare-import-like-import-x-from-some-package)
- [110: What is the difference between javascript/auto and javascript/esm module types?](#110-what-is-the-difference-between-javascriptauto-and-javascriptesm-module-types)
- [111: Why can importing a CommonJS module from an ES module give unexpected results?](#111-why-can-importing-a-commonjs-module-from-an-es-module-give-unexpected-results)
- [112: What security problems can a webpack config cause?](#112-what-security-problems-can-a-webpack-config-cause)
- [113: Users see ChunkLoadError after a deploy. Why does it happen and how do you handle it?](#113-users-see-chunkloaderror-after-a-deploy-why-does-it-happen-and-how-do-you-handle-it)
- [114: How do you get emitted assets in a plugin, and what is processAssets?](#114-how-do-you-get-emitted-assets-in-a-plugin-and-what-is-processassets)
- [115: What is a child compiler?](#115-what-is-a-child-compiler)
- [116: How do you run webpack from Node.js code?](#116-how-do-you-run-webpack-from-nodejs-code)
- [117: How do you make webpack builds reproducible across machines?](#117-how-do-you-make-webpack-builds-reproducible-across-machines)
- [118: When would you choose webpack, Vite or Rspack for a new project?](#118-when-would-you-choose-webpack-vite-or-rspack-for-a-new-project)
- [119: What is Rspack and how compatible is it with webpack?](#119-what-is-rspack-and-how-compatible-is-it-with-webpack)
- [120: How would you debug a loader or plugin that behaves wrong?](#120-how-would-you-debug-a-loader-or-plugin-that-behaves-wrong)

---

# Easy Questions (1-40)

## 1: What is webpack?

webpack is a module bundler for JavaScript applications. It starts from one or more entry files, follows every `import` and `require`, and builds a dependency graph of all the modules your app uses. Then it outputs one or more bundles that the browser can load.

It doesn't only handle JavaScript. With loaders it can also process CSS, images, fonts, TypeScript, JSON and pretty much any other file type, and treat them as modules too.

## 2: Why do we need a bundler at all?

Browsers can load ES modules natively now, but shipping hundreds of small source files to production is still slow, and the browser can't read things like TypeScript, JSX, Sass or imports from `node_modules` by package name.

A bundler solves this. It resolves package imports, transforms code the browser doesn't understand, combines files into fewer requests, removes unused code, minifies the output and adds content hashes to file names so caching works well.

## 3: What is the dependency graph?

It's the map webpack builds of how your modules depend on each other. webpack starts from the entry point, parses it, finds every import, then does the same for each imported file, and so on until there are no new files left.

Everything that ends up in the bundle is in this graph. A file that nothing imports won't be bundled, even if it sits in your `src` folder.

## 4: How do you install webpack?

You install webpack and the CLI as dev dependencies:

```bash
npm install --save-dev webpack webpack-cli
```

Then you can run it with `npx webpack` or add a script to `package.json`:

```json
{
  "scripts": {
    "build": "webpack --mode production"
  }
}
```

## 5: What is webpack.config.js?

It's the configuration file webpack looks for in the project root by default. It's a regular Node.js module that exports a config object (or a function that returns one, or an array of configs).

```js
const path = require("path");

module.exports = {
  mode: "development",
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
};
```

You can point to a different file with `webpack --config webpack.prod.js`. The config can also be written as `webpack.config.mjs` (ESM) or in TypeScript if you have a loader like `ts-node` installed.

## 6: Can webpack run without a config file?

Yes. Since webpack 4 there are defaults, so a config file is optional. Without one, webpack uses `./src/index.js` as the entry and writes the output to `./dist/main.js`.

If you don't set `mode`, webpack falls back to `production` and prints a warning telling you to set it. For anything beyond a toy project you'll need a config file anyway, to add loaders and plugins.

## 7: What is an entry point?

The entry point is the module webpack starts from when building the dependency graph. By default it's `./src/index.js`.

```js
module.exports = {
  entry: "./src/main.js",
};
```

Each entry produces its own bundle (an "entry chunk"), plus any extra chunks created by code splitting.

## 8: How do you set up multiple entry points?

Pass an object to `entry`. Each key becomes the chunk name, which you can use in the output file name with `[name]`.

```js
module.exports = {
  entry: {
    app: "./src/app.js",
    admin: "./src/admin.js",
  },
  output: {
    filename: "[name].bundle.js",
  },
};
```

This creates `app.bundle.js` and `admin.bundle.js`. It's common for multi-page apps where each page has its own script. You can also use `dependOn` to let one entry share modules with another instead of duplicating them.

## 9: What does the output option do?

`output` tells webpack where to write the bundles and how to name them. The two main fields are `path` (an absolute directory) and `filename`.

```js
const path = require("path");

module.exports = {
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "[name].[contenthash].js",
    clean: true,
  },
};
```

There are other fields too, like `publicPath`, `chunkFilename` for non-entry chunks, `assetModuleFilename` for assets, and `library` when you build a library.

## 10: What are loaders?

Loaders transform files before webpack adds them to the dependency graph. Out of the box webpack only understands JavaScript and JSON. Loaders let it handle other file types, or change JavaScript before bundling.

```js
module.exports = {
  module: {
    rules: [
      { test: /\.css$/i, use: ["style-loader", "css-loader"] },
      { test: /\.tsx?$/, use: "ts-loader", exclude: /node_modules/ },
    ],
  },
};
```

Each rule has a `test` (which files it matches) and `use` (which loaders to apply). Common loaders are `babel-loader`, `ts-loader`, `css-loader`, `style-loader`, `sass-loader` and `postcss-loader`.

## 11: What are plugins?

Plugins hook into the whole build process and can do things loaders can't, like generating an HTML file, extracting CSS into separate files, defining global constants, or analyzing the bundle.

```js
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  plugins: [new HtmlWebpackPlugin({ template: "./src/index.html" })],
};
```

A plugin is usually a class you create with `new` and add to the `plugins` array. A lot of webpack's own features are built as plugins internally.

## 12: What is the difference between a loader and a plugin?

A loader works on one file at a time. It gets the file's source, transforms it and returns the result. For example, `babel-loader` turns modern JS into older JS, and `css-loader` turns a CSS file into a JS module.

A plugin works on the build as a whole. It can listen to events during the compilation and change chunks, assets or the output. For example, `HtmlWebpackPlugin` creates an HTML file with all the generated script tags.

Short version: loaders transform individual modules, plugins handle everything else.

## 13: What is the mode option?

`mode` tells webpack which set of built-in defaults to use. It can be `development`, `production` or `none`.

```js
module.exports = {
  mode: "production",
};
```

You can also set it from the CLI with `webpack --mode=production`. The mode also sets `process.env.NODE_ENV` inside your bundled code to the same value, which libraries like React use to strip dev-only code.

## 14: What is the difference between development and production mode?

`development` focuses on fast rebuilds and easy debugging. It uses readable module names, includes source maps through `eval`, and skips minification.

`production` focuses on small and fast output. It turns on minification with Terser, tree shaking (`usedExports` and `sideEffects`), scope hoisting, deterministic module and chunk ids, and performance hints that warn about large files. Production builds are slower, but the result is much smaller.

## 15: How do you import CSS files with webpack?

You need two loaders: `css-loader` reads the CSS file and resolves `@import` and `url()` inside it, and `style-loader` injects the CSS into the page using `<style>` tags at runtime.

```bash
npm install --save-dev style-loader css-loader
```

```js
module.exports = {
  module: {
    rules: [{ test: /\.css$/i, use: ["style-loader", "css-loader"] }],
  },
};
```

Then in your code you just write `import './styles.css';`. For production you usually replace `style-loader` with `MiniCssExtractPlugin.loader` so the CSS ends up in a separate `.css` file.

## 16: How do you handle images and fonts in webpack 5?

webpack 5 has built-in asset modules, so you don't need `file-loader` or `url-loader` anymore.

```js
module.exports = {
  module: {
    rules: [
      { test: /\.(png|jpe?g|gif|svg)$/i, type: "asset/resource" },
      { test: /\.(woff2?|ttf|eot)$/i, type: "asset/resource" },
    ],
  },
};
```

When you `import logo from './logo.png'`, webpack copies the file to the output folder and `logo` contains its final URL. The same thing happens for `url()` references inside CSS.

## 17: What are the four asset module types?

- `asset/resource` emits a separate file and exports its URL. This replaced `file-loader`.
- `asset/inline` exports the file as a data URI (base64). This replaced `url-loader`.
- `asset/source` exports the raw file content as a string. This replaced `raw-loader`.
- `asset` picks between `resource` and `inline` automatically. Files smaller than 8 KB are inlined, bigger files are emitted as files.

You can change the size limit for `asset`:

```js
{
  test: /\.svg$/i,
  type: 'asset',
  parser: { dataUrlCondition: { maxSize: 4 * 1024 } },
}
```

## 18: What is babel-loader used for?

`babel-loader` runs your JavaScript through Babel, so you can write modern syntax or JSX and have it compiled to code your target browsers support.

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: { presets: ["@babel/preset-env", "@babel/preset-react"] },
        },
      },
    ],
  },
};
```

Excluding `node_modules` is important, otherwise Babel processes every dependency and the build gets very slow. Usually the Babel options live in `babel.config.js` instead of the webpack config.

## 19: How do you use TypeScript with webpack?

The common way is `ts-loader`, which runs the TypeScript compiler on `.ts` and `.tsx` files.

```js
module.exports = {
  entry: "./src/index.ts",
  module: {
    rules: [{ test: /\.tsx?$/, use: "ts-loader", exclude: /node_modules/ }],
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js"],
  },
};
```

Adding the extensions to `resolve.extensions` lets you write `import { x } from './utils'` without the `.ts` part. Another option is `babel-loader` with `@babel/preset-typescript`, which is faster but doesn't type-check, so you run `tsc --noEmit` separately.

## 20: What does HtmlWebpackPlugin do?

It creates an HTML file in the output folder and adds `<script>` (and `<link>` for extracted CSS) tags for all the bundles webpack generated. This is handy when file names contain hashes, because you don't have to update the HTML by hand after every build.

```js
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({
      title: "My App",
      template: "./src/index.html",
    }),
  ],
};
```

Without a `template` it generates a basic HTML file. To build several pages you add one instance of the plugin per page.

## 21: What is webpack-dev-server?

It's a development server that builds your app in memory (no files written to disk) and serves it, usually at `http://localhost:8080`. It rebuilds when you save a file and updates the browser automatically.

```bash
npm install --save-dev webpack-dev-server
npx webpack serve --mode development
```

```js
module.exports = {
  devServer: {
    static: "./public",
    port: 3000,
    open: true,
  },
};
```

## 22: What is Hot Module Replacement (HMR)?

HMR swaps changed modules in the running app without a full page reload. That way you keep the app state (for example, form inputs or the current route) while you edit code.

In webpack-dev-server it's turned on by default (`hot: true`). CSS handled by `style-loader` updates out of the box. For JavaScript you need code that accepts updates, either written by hand with `module.hot.accept()` or, more commonly, provided by a framework tool such as React Refresh or Vue Loader.

## 23: What is a source map and how do you enable it?

A source map connects the bundled, minified code back to your original source files. With it, errors and breakpoints in DevTools point to the real file and line instead of line 1 of `main.js`.

You enable it with the `devtool` option:

```js
module.exports = {
  devtool: "source-map",
};
```

There are many values. `eval-cheap-module-source-map` is a good choice in development because it's fast to rebuild. `source-map` is the most accurate and is often used in production. `false` turns source maps off.

## 24: What is a chunk?

A chunk is a group of modules that webpack puts together and usually writes out as one file. There are a few kinds:

- Entry chunks, one per entry point.
- Async chunks, created by dynamic `import()`.
- Split chunks, created by `SplitChunksPlugin`, for example a vendor chunk with code from `node_modules`.
- The runtime chunk, if you move the webpack runtime into its own file.

## 25: What is the difference between a module, a chunk and a bundle?

- A module is a single file in your source code, like `utils.js` or `button.css`.
- A chunk is a group of modules webpack decides to put together during the build.
- A bundle is the final output file written to disk, like `main.3f2a1b.js`.

In most cases one chunk becomes one bundle, so people often use the two words for the same thing. The difference shows up when, for example, a chunk produces both a JS file and a CSS file.

## 26: What is [contenthash] in file names?

`[contenthash]` is replaced with a hash of the file's content. If the content doesn't change between builds, the hash stays the same. If it changes, the hash changes.

```js
module.exports = {
  output: {
    filename: "[name].[contenthash].js",
  },
};
```

This lets you cache files in the browser for a very long time (even a year). When you deploy new code, only the files that changed get new names, so users download only those.

## 27: How do you clean the dist folder before each build?

In webpack 5 you set `output.clean`:

```js
module.exports = {
  output: {
    clean: true,
  },
};
```

This removes old files from the output folder before writing new ones. Before this option existed, people used `clean-webpack-plugin`, which you'll still see in older projects.

## 28: What is resolve.extensions?

It's the list of extensions webpack tries, in order, when an import has no extension.

```js
module.exports = {
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
};
```

With this, `import App from './App'` finds `App.tsx`. Setting this option replaces the default list (`['.js', '.json', '.wasm']`). If you want to keep the defaults, add `'...'` to the array. Keep the list short, since every extra extension means extra file system lookups.

## 29: What is resolve.alias?

It lets you create shortcuts for import paths, so you don't need long relative paths like `../../../components/Button`.

```js
const path = require("path");

module.exports = {
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
      "@components": path.resolve(__dirname, "src/components"),
    },
  },
};
```

Now you can write `import Button from '@components/Button'`. If you use TypeScript, add the same paths in `tsconfig.json` under `compilerOptions.paths`, or use `tsconfig-paths-webpack-plugin` so you only define them once.

## 30: What does watch mode do?

In watch mode webpack keeps running and rebuilds when a file in the dependency graph changes. It only rebuilds what changed, so it's much faster than a fresh build.

```bash
npx webpack --watch
# or
npx webpack watch
```

Unlike webpack-dev-server, watch mode writes the files to disk and doesn't serve them or reload the browser. It's useful when another server (for example a backend) serves your built files.

## 31: What are the common webpack CLI commands?

- `webpack` or `webpack build` runs a build.
- `webpack serve` starts webpack-dev-server.
- `webpack watch` builds and watches for changes.
- `webpack --mode production` sets the mode.
- `webpack --config webpack.prod.js` uses a different config file.
- `webpack --env production` passes values to a config exported as a function.
- `webpack --stats verbose` or `--json stats.json` shows or saves build stats.
- `webpack info` prints system and package versions, useful for bug reports.

## 32: Which module formats does webpack support?

webpack understands ES modules (`import`/`export`), CommonJS (`require`/`module.exports`) and AMD (`define`/`require`). You can even mix them in one project, and webpack handles the interop between them.

ES modules are the best choice for your own code because they are static. webpack can see exactly what is imported and exported at build time, which makes tree shaking work. CommonJS is dynamic, so webpack has a much harder time removing unused code from it.

## 33: In what order are loaders applied?

Loaders in a `use` array run from right to left (or bottom to top if written on several lines).

```js
{
  test: /\.scss$/i,
  use: ['style-loader', 'css-loader', 'sass-loader'],
}
```

Here `sass-loader` runs first and turns Sass into CSS, then `css-loader` turns the CSS into a JS module, and finally `style-loader` injects it into the page. If you put them in the wrong order, the build fails because a loader gets input it doesn't understand.

## 34: How do you pass options to a loader?

Use the object form with `loader` and `options`:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: { modules: true, importLoaders: 1 },
          },
          "postcss-loader",
        ],
      },
    ],
  },
};
```

You can mix strings and objects in the same `use` array. Each loader documents its own options.

## 35: What is DefinePlugin?

`DefinePlugin` replaces identifiers in your code with values at build time. It's often used for feature flags or config like an API URL.

```js
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.DefinePlugin({
      __API_URL__: JSON.stringify("https://api.example.com"),
      __FEATURE_X__: JSON.stringify(false),
    }),
  ],
};
```

The values are inserted as code, not as strings, which is why you wrap them with `JSON.stringify`. Without it, `'https://api.example.com'` would be inserted as bare text and break the code. When a flag is `false`, the minifier can remove the code behind `if (__FEATURE_X__)` completely.

## 36: How do you use environment variables in the webpack config?

Export a function instead of an object. webpack calls it with `env` (values from `--env`) and `argv` (all CLI options).

```js
module.exports = (env, argv) => {
  const isProd = argv.mode === "production";

  return {
    mode: isProd ? "production" : "development",
    devtool: isProd ? "source-map" : "eval-cheap-module-source-map",
  };
};
```

```bash
npx webpack --mode production --env analyze
```

Inside the function, `env.analyze` is `true`. You can also read `process.env` in the config like in any Node script, since the config file runs in Node.

## 37: What is publicPath?

`output.publicPath` is the URL prefix webpack uses when it loads chunks and assets in the browser. For example, if your files are served from a CDN:

```js
module.exports = {
  output: {
    publicPath: "https://cdn.example.com/assets/",
  },
};
```

Now lazy chunks are loaded from `https://cdn.example.com/assets/123.js` and images get that prefix too. In webpack 5 the default for browser builds is `'auto'`, which figures out the path from the current script's URL. If your app is served under a sub-path and routes break on reload, setting `publicPath: '/'` or the correct sub-path is a common fix.

## 38: What is a vendor chunk?

It's a chunk with third-party code from `node_modules`, kept separate from your own code. Libraries like React change much less often than your app code, so when they are in their own file, users can keep them cached between deploys.

```js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: "all",
    },
  },
};
```

With `chunks: 'all'`, webpack's default cache groups already move shared code from `node_modules` into separate vendor chunks.

## 39: What is MiniCssExtractPlugin?

It extracts CSS into separate `.css` files instead of injecting it with JavaScript. This is what you want in production: the browser can download CSS in parallel with JS, cache it separately, and there is no flash of unstyled content while JS loads.

```js
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [new MiniCssExtractPlugin({ filename: "[name].[contenthash].css" })],
};
```

In development many people keep `style-loader` because it works better with HMR.

## 40: What is the target option?

`target` tells webpack which environment the bundle will run in, so it can generate the right runtime code and handle built-in modules correctly.

```js
module.exports = {
  target: "node",
};
```

Common values are `web` (browsers), `node` (Node.js, `require` for built-ins like `fs` works), `webworker`, `electron-main` and `electron-renderer`. You can also use `browserslist`, which reads your browserslist config. If there is a browserslist config in the project, that's the default; otherwise it's `web`.

# Moderate Questions (41-80)

## 41: What is code splitting and what are the ways to do it in webpack?

Code splitting means breaking the app into several smaller files so the browser only loads what it needs for the current page, and loads the rest later.

There are three ways:

1. Multiple entry points, set by hand in `entry`.
2. `SplitChunksPlugin` (`optimization.splitChunks`), which moves shared modules and vendor code into separate chunks.
3. Dynamic `import()`, which creates a separate async chunk that is loaded on demand.

Dynamic imports usually give the biggest win, because you can keep whole pages or heavy features out of the first load.

## 42: How does dynamic import() work and what are magic comments?

`import()` returns a promise for a module. webpack sees it at build time and puts the imported module (and its dependencies) into a separate chunk that is fetched only when the code runs.

```js
button.addEventListener("click", async () => {
  const { openEditor } = await import(
    /* webpackChunkName: "editor" */ "./editor.js"
  );
  openEditor();
});
```

Magic comments are special comments inside `import()` that control how webpack handles it:

- `webpackChunkName` sets the chunk's name.
- `webpackPrefetch: true` and `webpackPreload: true` add resource hints.
- `webpackMode` can be `lazy` (default), `lazy-once`, `eager` or `weak`.
- `webpackExports` limits which exports are included.
- `webpackIgnore: true` tells webpack to leave the `import()` alone.

## 43: What does SplitChunksPlugin do by default?

In webpack 5 it's enabled by default with these main settings:

- `chunks: 'async'`, so it only splits code that is loaded with `import()`.
- `minSize: 20000` (about 20 KB), so tiny chunks aren't created.
- `maxAsyncRequests: 30` and `maxInitialRequests: 30`.
- Two cache groups: `defaultVendors` for anything in `node_modules`, and `default` for modules used by at least 2 chunks.

Because the default is `async`, your initial bundle won't be split. Most apps set `chunks: 'all'` so that vendor code in the initial bundle is split out too.

## 44: How do you configure cacheGroups in splitChunks?

Cache groups let you decide which modules go into which chunk. For example, putting React into its own chunk and the rest of `node_modules` into another:

```js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: "all",
      cacheGroups: {
        react: {
          test: /[\\/]node_modules[\\/](react|react-dom|scheduler)[\\/]/,
          name: "react",
          priority: 20,
        },
        vendors: {
          test: /[\\/]node_modules[\\/]/,
          name: "vendors",
          priority: 10,
        },
      },
    },
  },
};
```

`priority` decides which group wins when a module matches more than one. The `[\\/]` part matches both Unix and Windows path separators. Be careful with a fixed `name` for all of `node_modules`: you get one big file that every page has to load, even pages that only use a small part of it.

## 45: What is the runtime chunk and why would you split it out?

The runtime is the small piece of code webpack adds to load and connect modules: `__webpack_require__`, the module cache, the code that loads async chunks, and the map from chunk ids to file names.

That map changes when any async chunk changes, and by default the runtime lives inside the entry chunk. So a change in one lazy page also changes the hash of your main bundle. Moving the runtime out fixes this:

```js
module.exports = {
  optimization: {
    runtimeChunk: "single",
  },
};
```

`'single'` creates one runtime shared by all entries. That's also important on multi-entry pages, because two separate runtimes on one page would create two separate module caches and can cause modules to run twice.

## 46: What is tree shaking and what does it need to work?

Tree shaking removes exports that are never imported. If `utils.js` exports ten functions and you use one, the other nine shouldn't end up in the bundle.

It needs:

- ES module syntax (`import`/`export`). CommonJS is much harder to analyze.
- Babel or TypeScript not converting your modules to CommonJS. For Babel, use `@babel/preset-env` with `modules: false` (or the default `auto`, which keeps ESM under webpack). For TypeScript, use `"module": "esnext"` or similar.
- `mode: 'production'`, which turns on `usedExports` and the minifier that actually deletes the dead code.
- `sideEffects` information in `package.json` so whole unused files can be skipped.

## 47: What is the sideEffects field in package.json?

It tells webpack whether importing a file can do something by itself, like adding a global, a polyfill or a CSS rule. If a package says it has no side effects, webpack can skip whole files whose exports you don't use.

```json
{
  "name": "my-lib",
  "sideEffects": false
}
```

If some files do have side effects, list them so they aren't dropped:

```json
{
  "sideEffects": ["*.css", "./src/polyfills.js"]
}
```

A common bug is setting `"sideEffects": false` in an app and then losing CSS imported with `import './styles.css'`, because webpack thinks the import is unused. You can also set `sideEffects` per rule in the webpack config.

## 48: What is the difference between usedExports and sideEffects optimizations?

They work at different levels.

`optimization.usedExports` works inside a module. webpack marks which exports are used, and the minifier (Terser) then removes the unused ones as dead code. The module itself is still included.

`optimization.sideEffects` works on whole modules. If a module has no side effects and none of its exports are used, webpack skips it entirely, without even including its code. It also lets webpack skip "barrel" files (like `index.js` that only re-exports) and jump directly to the real module.

`sideEffects` is usually the more effective of the two, because it removes complete files instead of relying on the minifier.

## 49: How do you set up long-term caching?

The goal is that file names change only when their content changes. The usual setup:

```js
module.exports = {
  output: {
    filename: "[name].[contenthash].js",
    chunkFilename: "[name].[contenthash].js",
  },
  optimization: {
    moduleIds: "deterministic",
    runtimeChunk: "single",
    splitChunks: { chunks: "all" },
  },
};
```

- `[contenthash]` ties the name to the content.
- `moduleIds: 'deterministic'` (default in production) keeps module ids stable when you add or remove other modules.
- `runtimeChunk: 'single'` stops the runtime's chunk map from changing the main bundle hash.
- Splitting vendor code keeps rarely changing libraries in their own files.

Then serve these files with `Cache-Control: max-age=31536000, immutable`, and serve `index.html` with no caching so it always points to the latest files.

## 50: What is persistent caching in webpack 5?

webpack 5 can save its build cache to disk so the next build (even after restarting the process) can reuse the work.

```js
module.exports = {
  cache: {
    type: "filesystem",
    buildDependencies: {
      config: [__filename],
    },
  },
};
```

The cache is stored in `node_modules/.cache/webpack` by default. The `buildDependencies.config` line tells webpack to throw away the cache when the config file changes. On big projects this can make a second cold start several times faster. In development the default is `memory` cache, and in production caching is off unless you turn it on.

## 51: What is the difference between prefetch and preload?

Both are added with magic comments on a dynamic import.

```js
import(/* webpackPrefetch: true */ "./settings-page.js");
import(/* webpackPreload: true */ "./chart-lib.js");
```

- Prefetch adds `<link rel="prefetch">`. The browser downloads the chunk when it's idle, after the current page has loaded. Use it for things the user will probably need later, like the next page.
- Preload adds `<link rel="preload">`. The chunk downloads in parallel with the parent chunk, with high priority. Use it for something needed right away by the current page.

Prefetch is the safer one. Using preload wrong hurts performance because it competes with resources the page really needs.

## 52: How do you split webpack config for development and production?

A common pattern is three files: a common config, and one for each mode, merged with `webpack-merge`.

```js
// webpack.common.js
module.exports = {
  entry: "./src/index.js",
  module: { rules: [/* shared loaders */] },
};
```

```js
// webpack.prod.js
const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");

module.exports = merge(common, {
  mode: "production",
  devtool: "source-map",
});
```

`merge` concatenates arrays (like `plugins` and `rules`) and merges objects deeply. Another approach is a single config exported as a function that checks `argv.mode`. Either works; the function version is simpler for small projects.

## 53: How do you set up a proxy in webpack-dev-server?

Use a proxy when your frontend runs on one port and the API runs on another. This avoids CORS issues in development.

```js
module.exports = {
  devServer: {
    proxy: [
      {
        context: ["/api"],
        target: "http://localhost:4000",
        changeOrigin: true,
      },
    ],
  },
};
```

Now a request from the app to `/api/users` is forwarded to `http://localhost:4000/api/users`. In webpack-dev-server v5 `proxy` must be an array. The older object syntax (`proxy: { '/api': '...' }`) from v4 is no longer supported. To drop the `/api` prefix you add `pathRewrite: { '^/api': '' }`.

## 54: Why do routes return 404 on refresh in webpack-dev-server and how do you fix it?

Single page apps with client-side routing (like React Router with browser history) have URLs like `/users/5` that don't match a real file. When you refresh, the dev server looks for that file, can't find it and returns 404.

The fix is `historyApiFallback`, which serves `index.html` for any unknown route:

```js
module.exports = {
  devServer: {
    historyApiFallback: true,
  },
  output: {
    publicPath: "/",
  },
};
```

Setting `publicPath: '/'` matters too. Otherwise on a nested route like `/users/5` the browser may request `/users/main.js` instead of `/main.js`. Your production server needs the same fallback rule.

## 55: Which devtool option should you use in development and production?

In development you want fast rebuilds and good enough mapping. `eval-cheap-module-source-map` is a popular choice: it maps to the original source per line and rebuilds quickly. `eval-source-map` is more accurate but slower.

In production the choice depends on whether the source should be public:

- `source-map` creates full `.map` files and adds a comment linking to them.
- `hidden-source-map` creates the maps but doesn't add the comment, so you can upload them to an error tracker (like Sentry) without exposing them to users.
- `nosources-source-map` gives stack traces with file names and lines but without the source code.
- `false` creates no maps.

Never use `eval-*` options in production. They are big and slow.

## 56: How do you customize minification in webpack?

In production webpack minifies JS with `TerserPlugin`. You can change its settings through `optimization.minimizer`:

```js
const TerserPlugin = require("terser-webpack-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
  optimization: {
    minimizer: ["...", new CssMinimizerPlugin()],
  },
};
```

The `'...'` string means "keep the default minimizers" (Terser). Without it, setting `minimizer` replaces Terser and your JS won't be minified. CSS isn't minified by default, so you add `CssMinimizerPlugin`.

To change Terser options, pass your own instance instead of `'...'`, for example `new TerserPlugin({ terserOptions: { compress: { drop_console: true } } })`. `TerserPlugin` can also use faster minifiers like SWC or esbuild through its `minify` option.

## 57: How do you find out what makes your bundle big?

The most popular tool is `webpack-bundle-analyzer`. It shows an interactive treemap of every module in every chunk and its size.

```js
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");

module.exports = {
  plugins: [new BundleAnalyzerPlugin()],
};
```

You can also save build stats and load them in a tool:

```bash
npx webpack --profile --json stats.json
```

The `stats.json` file works with the official analyzer at webpack.github.io/analyse, with Statoscope, and with the bundle analyzer CLI. Things to look for: large libraries you only use a small part of (like full `lodash` or `moment` with all locales), the same package bundled twice in different versions, and heavy code that could be lazy loaded.

## 58: What are performance hints?

In production webpack warns you when an asset or entry point is too big. The default limit is 250,000 bytes (around 244 KiB) per asset and per entry point.

```js
module.exports = {
  performance: {
    hints: "error",
    maxAssetSize: 300000,
    maxEntrypointSize: 300000,
  },
};
```

`hints` can be `'warning'`, `'error'` or `false`. Setting it to `'error'` in CI is a simple way to stop the bundle from slowly growing. You can also use `assetFilter` to ignore files like source maps or large images.

## 59: What are externals and when would you use them?

`externals` tells webpack not to bundle a dependency and instead expect it to exist at runtime.

```js
module.exports = {
  externals: {
    react: "React",
    "react-dom": "ReactDOM",
  },
};
```

With this config, `import React from 'react'` reads the global `window.React`, which you load yourself (for example from a CDN script tag). Common uses:

- Building a library, so it doesn't include its own copy of React or other peer dependencies.
- Building a Node.js app, where `node_modules` stay on disk and don't need to be bundled.
- Loading big libraries from a CDN.

## 60: Why do you get errors about Node.js core modules like crypto or path in webpack 5?

webpack 4 and earlier automatically added browser polyfills for Node core modules (`path`, `crypto`, `buffer`, `stream` and others). webpack 5 removed this, because it often added a lot of code people didn't know about.

So if a package uses `require('crypto')`, you now get an error like "BREAKING CHANGE: webpack < 5 used to include polyfills for node.js core modules by default". You have a few options:

```js
module.exports = {
  resolve: {
    fallback: {
      path: require.resolve("path-browserify"),
      crypto: false,
    },
  },
};
```

Pointing to a polyfill package adds it back. Setting `false` gives an empty module, which is fine if the code path isn't used in the browser. The best fix is often to find a browser-friendly version of the package. For globals like `Buffer` or `process`, use `ProvidePlugin`.

## 61: How do you use CSS Modules with webpack?

CSS Modules make class names local to the file by turning them into unique names. `css-loader` supports this. By default, files that match `*.module.css` (or `.module.scss` and so on) are treated as CSS Modules automatically.

```css
/* Button.module.css */
.primary {
  background: blue;
}
```

```js
import * as styles from "./Button.module.css";

button.className = styles.primary;
```

Note that in `css-loader` v7 the `namedExport` option became `true` by default, so the old `import styles from './Button.module.css'` stops working and you use the namespace import shown above. If you want the old style, set it back:

```js
{
  loader: 'css-loader',
  options: { modules: { namedExport: false } },
}
```

## 62: How do you set up Sass and PostCSS with webpack?

Chain the loaders so Sass is compiled first, then PostCSS runs (for autoprefixer and similar), then `css-loader` and `style-loader` (or `MiniCssExtractPlugin.loader`).

```bash
npm install --save-dev sass sass-loader postcss postcss-loader autoprefixer css-loader style-loader
```

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          "style-loader",
          { loader: "css-loader", options: { importLoaders: 2 } },
          "postcss-loader",
          "sass-loader",
        ],
      },
    ],
  },
};
```

`importLoaders: 2` makes sure CSS pulled in with `@import` also goes through the two loaders after `css-loader`. PostCSS plugins are configured in `postcss.config.js`.

## 63: What do test, include, exclude and oneOf do in a rule?

- `test` matches files by a regex on the file path, usually the extension.
- `include` limits the rule to certain folders.
- `exclude` skips certain folders, most often `node_modules`.
- `oneOf` is a list of rules where only the first match is used.

```js
const path = require("path");

module.exports = {
  module: {
    rules: [
      {
        oneOf: [
          { test: /\.svg$/i, resourceQuery: /react/, use: ["@svgr/webpack"] },
          { test: /\.svg$/i, type: "asset/resource" },
        ],
      },
      {
        test: /\.js$/,
        include: path.resolve(__dirname, "src"),
        use: "babel-loader",
      },
    ],
  },
};
```

`include` is usually better than `exclude` for performance, because webpack checks fewer files. `oneOf` is useful when one file type should be handled differently in different cases.

## 64: What is resourceQuery and how can you use it?

`resourceQuery` matches the query string in an import path. This lets you load the same file in different ways depending on how it's imported.

```js
module.exports = {
  module: {
    rules: [
      { resourceQuery: /raw/, type: "asset/source" },
      { resourceQuery: /url/, type: "asset/resource" },
    ],
  },
};
```

```js
import shaderCode from "./shader.glsl?raw";
import workerUrl from "./data.json?url";
```

The first import gives you the file as a string, the second gives you a URL. Vite uses the same `?raw` and `?url` style, so this is handy when you want similar behavior in webpack.

## 65: How do you build a library with webpack?

Set `output.library` so webpack exposes your entry's exports instead of just running the code.

```js
const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "my-lib.js",
    library: {
      name: "MyLib",
      type: "umd",
    },
    globalObject: "this",
  },
  externals: {
    lodash: "lodash",
  },
};
```

`type: 'umd'` works with CommonJS, AMD and a global variable. Other types include `commonjs2`, `module` (ESM, needs `experiments.outputModule: true`) and `window`. Put peer dependencies in `externals` so they don't get bundled. For pure libraries many teams use Rollup or tsup instead, but webpack works fine, especially when the library has assets or complex loaders.

## 66: Can webpack build several configurations at once?

Yes. If the config exports an array, webpack builds each config, in parallel where it can.

```js
module.exports = [
  {
    name: "client",
    target: "web",
    entry: "./src/client.js",
  },
  {
    name: "server",
    target: "node",
    entry: "./src/server.js",
  },
];
```

This is common for server-side rendering (one build for the browser, one for Node) or for building a library in several formats. You can build one by name with `webpack --config-name client`. The `dependencies` field lets one config wait for another, and `parallelism` limits how many run at the same time.

## 67: How do you expose environment variables to your frontend code?

The code runs in the browser, so `process.env` doesn't exist there. webpack only replaces values you tell it to replace at build time.

```js
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.EnvironmentPlugin({
      API_URL: "http://localhost:4000",
      SENTRY_DSN: "",
    }),
  ],
};
```

`EnvironmentPlugin` is a shortcut for `DefinePlugin` with `process.env` keys. The values in the object are defaults used when the variable isn't set. Now `process.env.API_URL` in your code gets replaced with the value at build time. `dotenv-webpack` does the same but reads from a `.env` file.

Remember these values end up in the public JS file. Never put secrets there.

## 68: How can you make a slow webpack build faster?

Some common steps, roughly in order of how much they help:

- Turn on persistent caching with `cache: { type: 'filesystem' }`.
- Replace `babel-loader` or `ts-loader` with `swc-loader` or `esbuild-loader`, which are much faster. Run type checks separately with `fork-ts-checker-webpack-plugin` or `tsc --noEmit`.
- Limit loaders with `include` so they only process `src`.
- Use a cheaper `devtool` in development, like `eval-cheap-module-source-map`.
- Make sure you're on the latest webpack and loader versions.
- Don't run production-only plugins (minifiers, analyzers) in development.
- Use `experiments.lazyCompilation` in development so unvisited routes aren't built.
- For expensive loaders, `thread-loader` can run them in worker processes, but it has startup cost, so measure first.

Measure with `--profile` or `ProfilingPlugin` before and after, so you know what actually helped.

## 69: What is ProvidePlugin?

`ProvidePlugin` automatically imports a module when a certain free variable is used in your code. You don't have to write the import in every file.

```js
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.ProvidePlugin({
      $: "jquery",
      process: "process/browser",
      Buffer: ["buffer", "Buffer"],
    }),
  ],
};
```

Now any file that uses `$` gets jQuery imported for it. In webpack 5 it's mostly used to provide `process` and `Buffer` globals for old packages that expect them. The array form `['buffer', 'Buffer']` means "use the `Buffer` export of the `buffer` package".

## 70: How do you stop a library like moment.js from bundling all its locales?

moment loads locales with a dynamic `require('./locale/' + name)`. webpack can't know which ones you need, so it bundles all of them, which adds a few hundred KB.

You can ignore them with `IgnorePlugin` and import only the ones you need:

```js
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.IgnorePlugin({
      resourceRegExp: /^\.\/locale$/,
      contextRegExp: /moment$/,
    }),
  ],
};
```

```js
import moment from "moment";
import "moment/locale/de";
```

Or use `ContextReplacementPlugin` to keep only certain locales: `new webpack.ContextReplacementPlugin(/moment[/\\]locale$/, /de|fr/)`. The better long-term fix is to switch to a smaller library like date-fns or Day.js.

## 71: What happens when you import a module with a variable in the path?

When the path isn't fully static, like ``import(`./locales/${lang}.json`)``, webpack can't know the exact file. Instead it creates a context module: it includes every file that could match the pattern (here, every `.json` file in `./locales`) and picks the right one at runtime.

```js
async function loadLocale(lang) {
  const messages = await import(`./locales/${lang}.json`);
  return messages.default;
}
```

This works, but you need to keep the pattern tight. Something like `import(variable)` with no fixed part can't be resolved and gives a warning. A very broad pattern like ``import(`../${path}`)`` can pull in far more files than you want. For `import()`, each matched file gets its own chunk by default.

## 72: What is require.context and import.meta.webpackContext?

Both let you import a group of files that match a pattern, which is useful for things like auto-registering components or loading all test files.

```js
const icons = import.meta.webpackContext("./icons", {
  recursive: false,
  regExp: /\.svg$/,
});

icons.keys().forEach((key) => {
  console.log(key, icons(key));
});
```

`require.context(directory, useSubdirectories, regExp)` is the older form. `import.meta.webpackContext` was added in webpack 5.70 as the ESM-friendly version with an options object. Both are webpack-specific, so this code won't work with other bundlers without changes.

## 73: How do you lazy load routes in a React app built with webpack?

Use `React.lazy` with a dynamic `import()`. webpack creates a separate chunk for each lazy route.

```jsx
import { lazy, Suspense } from "react";
import { Routes, Route } from "react-router";

const Dashboard = lazy(
  () => import(/* webpackChunkName: "dashboard" */ "./pages/Dashboard"),
);
const Settings = lazy(
  () => import(/* webpackChunkName: "settings" */ "./pages/Settings"),
);

export function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

`React.lazy` needs the module to have a default export. Splitting by route is usually the easiest win, because the user only downloads the code for the page they open.

## 74: How do you debug "Module not found: Error: Can't resolve" errors?

Read the full error. It lists the path webpack tried to resolve and the directory it looked from. Then check:

- The file name and case. macOS and Windows file systems are usually case-insensitive, Linux is not, so `./Button` vs `./button.js` can work locally and fail in CI.
- Missing extensions. If you import `./utils` and the file is `utils.ts`, add `.ts` to `resolve.extensions`.
- Aliases. `@/components` only works if it's in `resolve.alias` (adding it to `tsconfig.json` alone isn't enough).
- The package is installed and its `package.json` `exports` field actually exposes the path you import.
- Node core modules like `fs` or `crypto` in browser code (see `resolve.fallback`).
- ESM packages that need full paths with extensions (the "fully specified" error).

Running with `--stats-error-details` or setting `stats: { errorDetails: true }` shows each place webpack looked.

## 75: How do you control the build output in the terminal?

The `stats` option controls what webpack prints after a build.

```js
module.exports = {
  stats: "errors-warnings",
};
```

Presets include `'none'`, `'minimal'`, `'errors-only'`, `'errors-warnings'`, `'normal'` (default) and `'verbose'`. You can also pass an object to turn on specific details, like `{ modules: false, children: false, errorDetails: true }`.

Other useful flags: `--progress` shows a progress bar, and `infrastructureLogging: { level: 'verbose' }` shows logs from webpack's internals like the cache. If a warning from a third-party package isn't useful, you can hide it with `ignoreWarnings`.

## 76: How do you set up React Fast Refresh with webpack?

React Fast Refresh is the React version of HMR. It keeps component state while you edit. With webpack you use `@pmmmwh/react-refresh-webpack-plugin` together with the `react-refresh` Babel plugin.

```js
const ReactRefreshWebpackPlugin = require("@pmmmwh/react-refresh-webpack-plugin");

const isDev = process.env.NODE_ENV !== "production";

module.exports = {
  mode: isDev ? "development" : "production",
  module: {
    rules: [
      {
        test: /\.[jt]sx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            plugins: [isDev && require.resolve("react-refresh/babel")].filter(
              Boolean,
            ),
          },
        },
      },
    ],
  },
  plugins: [isDev && new ReactRefreshWebpackPlugin()].filter(Boolean),
  devServer: { hot: true },
};
```

Only turn it on in development. If you use `swc-loader`, SWC has its own `refresh` option instead of the Babel plugin.

## 77: How do you use Web Workers with webpack 5?

webpack 5 supports workers natively. Use `new Worker` with `new URL(..., import.meta.url)`:

```js
const worker = new Worker(new URL("./heavy-task.worker.js", import.meta.url), {
  type: "module",
});

worker.postMessage({ numbers: [1, 2, 3] });
worker.onmessage = (event) => console.log(event.data);
```

webpack sees this pattern, bundles the worker file and its imports into a separate chunk, and replaces the URL with the right path. You don't need `worker-loader` anymore. The worker file can use `import` and npm packages like any other module.

## 78: What does new URL('./file', import.meta.url) do in webpack?

It's the standard way (also supported by Vite and browsers) to get a URL to a file relative to the current module. webpack recognizes it and treats the file as an asset: it copies the file to the output folder and replaces the expression with the final URL.

```js
const imageUrl = new URL("./images/hero.png", import.meta.url);
document.querySelector("img").src = imageUrl.href;
```

This is useful when you need a URL but don't want an `import` statement, for example for workers, WASM files or audio files. It also makes the code more portable between bundlers, since it's not webpack-specific syntax.

## 79: What is the difference between fullhash, chunkhash and contenthash?

- `[fullhash]` is a hash of the whole compilation. Any change anywhere changes it for every file. It was called `[hash]` in webpack 4.
- `[chunkhash]` is a hash of a chunk. If the chunk includes JS and extracted CSS, both share it, so a CSS change also changes the JS file name.
- `[contenthash]` is a hash of the content of the specific output file. A CSS change only changes the CSS file name.

For long-term caching use `[contenthash]`. `[fullhash]` is mostly useful for things like a version string where you want any change to bust it.

## 80: What were the main changes from webpack 4 to webpack 5?

The ones that come up most often:

- Asset modules replaced `file-loader`, `url-loader` and `raw-loader`.
- Persistent caching to disk with `cache: { type: 'filesystem' }`.
- Module Federation for sharing code between separately deployed apps.
- Automatic Node.js core module polyfills were removed.
- Deterministic module and chunk ids by default in production, which helps long-term caching.
- Better tree shaking, including nested exports and some CommonJS patterns.
- `[hash]` was renamed to `[fullhash]`, and `output.clean` was added.
- Native support for workers and `new URL(..., import.meta.url)`.
- Top-level await, now on by default (since 5.83).

When upgrading, the Node polyfills and old loaders are usually what break first.

# Advanced Questions (81-120)

## 81: Walk through what happens inside webpack during a build.

Roughly:

1. webpack reads and normalizes the config, creates a `Compiler` object and calls `apply(compiler)` on every plugin. Most built-in features are plugins too, added based on your options.
2. `compiler.run()` (or `watch()`) creates a `Compilation` object, which holds the state of one build.
3. In the `make` phase, each entry is added. For every module webpack resolves its path (using `enhanced-resolve`), runs the matching loaders, then parses the result into an AST (webpack uses `acorn`) to find `import`, `require` and other dependencies. Each dependency goes through the same steps, which builds the module graph.
4. In the `seal` phase, webpack creates chunks from entries and dynamic imports, runs optimizations (marking used exports, side effects, `SplitChunksPlugin`, module concatenation, id assignment), generates code for every module and chunk, and computes hashes.
5. Assets are created, then plugins can change them in `processAssets` (minifiers run here).
6. In `emit`, files are written to `output.path` through the output file system, and the `done` hook fires with the stats.

In watch mode, the `Compiler` stays alive and each rebuild creates a new `Compilation`, reusing cached modules that didn't change.

## 82: What is Tapable?

Tapable is the small library webpack uses for its plugin system. The `Compiler`, `Compilation`, module factories and parsers all expose `hooks` objects made of Tapable hooks, and plugins "tap" into them.

There are different hook types:

- `SyncHook` calls every tapped function in order.
- `SyncBailHook` stops as soon as one function returns something other than `undefined`.
- `SyncWaterfallHook` passes each function's return value to the next one.
- `AsyncSeriesHook` runs async functions one after another.
- `AsyncParallelHook` runs async functions at the same time.

You tap sync hooks with `tap`, and async hooks with `tapAsync` (callback style) or `tapPromise`:

```js
compiler.hooks.emit.tapPromise("MyPlugin", async (compilation) => {
  await doSomethingAsync();
});
```

The hook type matters when writing a plugin. For example, returning a value from a bail hook changes webpack's behavior, while in a normal `SyncHook` it's ignored.

## 83: How do you write a custom webpack plugin?

A plugin is a class (or object) with an `apply(compiler)` method. Inside it you tap into hooks.

```js
class BuildTimePlugin {
  constructor(options = {}) {
    this.label = options.label || "Build";
  }

  apply(compiler) {
    let start;

    compiler.hooks.compile.tap("BuildTimePlugin", () => {
      start = Date.now();
    });

    compiler.hooks.done.tap("BuildTimePlugin", (stats) => {
      const logger = compiler.getInfrastructureLogger("BuildTimePlugin");
      const status = stats.hasErrors() ? "failed" : "succeeded";
      logger.info(`${this.label} ${status} in ${Date.now() - start} ms`);
    });
  }
}

module.exports = BuildTimePlugin;
```

```js
module.exports = {
  plugins: [new BuildTimePlugin({ label: "Client build" })],
};
```

The first argument to `tap` is the plugin name, which shows up in profiles and errors. Use webpack's logger instead of `console.log`, so the output respects the `infrastructureLogging` settings.

## 84: How do you write a custom loader?

A loader is a function that gets the source of a file and returns the transformed source. `this` is the loader context, which has helpers.

```js
// loaders/banner-loader.js
module.exports = function bannerLoader(source) {
  const { text } = this.getOptions({
    type: "object",
    properties: { text: { type: "string" } },
  });

  return `/* ${text} */\n${source}`;
};
```

For async work, call `this.async()` and use the callback it returns:

```js
module.exports = function asyncLoader(source) {
  const callback = this.async();

  transform(source)
    .then((result) => callback(null, result.code, result.map))
    .catch((err) => callback(err));
};
```

```js
const path = require("path");

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
          loader: path.resolve(__dirname, "loaders/banner-loader.js"),
          options: { text: "Built with webpack" },
        },
      },
    ],
  },
};
```

Some details: loaders are cacheable by default, so they should be pure (same input gives same output). If a loader reads other files, register them with `this.addDependency(file)` so watch mode notices changes. Set `module.exports.raw = true` if the loader needs a `Buffer` instead of a string, for example for images.

## 85: What are pitching loaders?

Loaders normally run right to left. But before that, webpack runs each loader's optional `pitch` method from left to right. If a `pitch` returns a value, webpack skips the remaining loaders (and the file isn't even read) and goes back through only the loaders to the left.

```js
module.exports = function (source) {
  return source;
};

module.exports.pitch = function (remainingRequest, precedingRequest, data) {
  data.startedAt = Date.now();
};
```

For loaders `a`, `b`, `c`, the order is: `a.pitch`, `b.pitch`, `c.pitch`, read file, `c`, `b`, `a`. If `b.pitch` returns something, the order becomes `a.pitch`, `b.pitch`, `a`.

`style-loader` is the classic example. Its `pitch` returns code like `import content from "!!css-loader!./file.css"` and then injects that content. That's why `style-loader` doesn't receive the CSS as a normal `source` argument. The `data` object is shared between a loader's `pitch` and its normal phase.

## 86: What does the webpack runtime code do?

When you look at an unminified bundle, you'll see code webpack added around your modules. The main parts:

- `__webpack_modules__`, an object mapping module ids to functions. Each of your modules is wrapped in a function.
- `__webpack_module_cache__`, which stores modules that already ran, so each module executes only once.
- `__webpack_require__(moduleId)`, which checks the cache, runs the module function if needed and returns its `exports`.
- Helpers on `__webpack_require__`, like `.d` (define getters for ES exports), `.r` (mark as ES module), `.o` (has own property), `.e` (load a chunk), `.p` (public path).

```js
function __webpack_require__(moduleId) {
  var cachedModule = __webpack_module_cache__[moduleId];
  if (cachedModule !== undefined) return cachedModule.exports;

  var module = (__webpack_module_cache__[moduleId] = { exports: {} });
  __webpack_modules__[moduleId](module, module.exports, __webpack_require__);
  return module.exports;
}
```

webpack only includes the runtime helpers your code actually needs, so a simple bundle has a small runtime.

## 87: How does webpack load an async chunk at runtime?

When code calls `import('./page.js')`, webpack compiles it to something like `__webpack_require__.e(chunkId).then(__webpack_require__.bind(__webpack_require__, moduleId))`.

For the `web` target the steps are:

1. `__webpack_require__.e` checks whether the chunk is already loaded or loading. If not, it creates a promise and stores it.
2. It builds the URL from `publicPath` plus the chunk file name (from the chunk id to file name map in the runtime) and adds a `<script>` tag.
3. The chunk file, when it runs, pushes itself into a global array: `(self["webpackChunkmy_app"] = self["webpackChunkmy_app"] || []).push([[chunkId], { ...modules }])`.
4. The runtime has replaced that array's `push` method, so it receives the modules, adds them to `__webpack_modules__` and resolves the promise.
5. Then `__webpack_require__` runs the module.

This is often called JSONP-style loading. The global name comes from `output.chunkLoadingGlobal`, which is based on `output.uniqueName` (by default the `name` in `package.json`). Two webpack apps on one page need different names, or their chunks will conflict.

## 88: What is Module Federation?

Module Federation lets separately built and deployed webpack apps share code at runtime. One app (the remote) exposes modules, and another (the host) loads them over the network, like a dynamic import from another server.

```js
// remote app: webpack.config.js
const { ModuleFederationPlugin } = require("webpack").container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: "checkout",
      filename: "remoteEntry.js",
      exposes: {
        "./Cart": "./src/Cart",
      },
      shared: { react: { singleton: true }, "react-dom": { singleton: true } },
    }),
  ],
};
```

```js
// host app: webpack.config.js
new ModuleFederationPlugin({
  name: "shell",
  remotes: {
    checkout: "checkout@https://checkout.example.com/remoteEntry.js",
  },
  shared: { react: { singleton: true }, "react-dom": { singleton: true } },
});
```

```js
// in the host
const Cart = React.lazy(() => import("checkout/Cart"));
```

It's mainly used for micro-frontends. Today there's also `@module-federation/enhanced` (Module Federation 2.0), which adds a runtime API, type sharing and works with Rspack too.

## 89: How does sharing work in Module Federation and what is the eager consumption error?

`shared` lists packages that apps should share instead of each loading its own copy. At runtime, the apps register the versions they have and the shared scope picks one based on semver.

Important options:

- `singleton: true` makes sure only one copy is loaded. React needs this, because two Reacts on one page break hooks.
- `requiredVersion` says which version range this app needs. If the loaded version doesn't match, you get a warning.
- `strictVersion: true` turns that warning into an error.
- `eager: true` bundles the shared module into the initial chunk instead of loading it async.

A common error is "Shared module is not available for eager consumption". It happens because shared modules are loaded asynchronously, but your entry file imports React synchronously before the shared scope is ready. The standard fix is an async boundary:

```js
// index.js
import("./bootstrap");
```

```js
// bootstrap.js
import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

createRoot(document.getElementById("root")).render(<App />);
```

The dynamic import gives webpack a chance to load the shared modules first. Setting `eager: true` also removes the error but makes the initial bundle bigger.

## 90: What is scope hoisting?

Normally webpack wraps every module in its own function, which adds code and a small runtime cost for each module. Scope hoisting (module concatenation) merges ES modules into one function scope where it's safe, like Rollup does.

It's turned on in production through `optimization.concatenateModules`. Benefits: smaller output, faster execution, and better minification because the minifier can see across modules.

It doesn't work for every module. It bails out for CommonJS modules, modules using `eval`, modules shared between several chunks in certain ways, and a few other cases. You can see why with:

```js
module.exports = {
  stats: { optimizationBailout: true },
};
```

If a lot of your code isn't being concatenated, the stats output tells you which modules and why.

## 91: How does tree shaking work internally in webpack?

It happens in steps:

1. While parsing, webpack records the exports of each ES module and which exports each import uses.
2. With `optimization.providedExports` and `usedExports`, it walks the module graph and marks each export as used or unused.
3. With `optimization.sideEffects`, it skips modules that have no side effects and whose exports aren't used, and it can redirect re-exports to the original module.
4. During code generation, unused exports are no longer exported (you'll see comments like `/* unused harmony export foo */` in development builds with `usedExports` on).
5. The minifier (Terser by default) then removes the code that is no longer referenced.

Step 5 means webpack itself doesn't delete the function body. It removes the export, and the minifier deletes dead code. That's why calls with possible side effects at the top level of a module can stay in the bundle. You can mark them as safe to remove with the `/*#__PURE__*/` annotation:

```js
export const theme = /*#__PURE__*/ createTheme({ primary: "blue" });
```

## 92: Why does CommonJS make tree shaking harder?

CommonJS is dynamic. `module.exports` can be changed at any time, `require` can be called inside conditions, and the path can be a variable. webpack can't be sure at build time what a module exports or what is used.

```js
const utils = require("./utils");
const name = getFunctionName();
utils[name]();
```

Here webpack has no way to know which function is used, so it keeps everything. webpack 5 does handle some simple CommonJS patterns (like `exports.foo = ...` and `require('./x').foo`), but anything dynamic disables the optimization for that module.

This is why libraries ship an ES module build (`"module"` or `"exports"` with an `import` condition in `package.json`), and why you see recommendations to use `lodash-es` instead of `lodash`.

## 93: How does webpack know when to invalidate the persistent cache?

webpack stores a snapshot for each cached item: the files, directories and packages it depends on, with timestamps or content hashes. On the next build it checks these, and only rebuilds what changed.

What it can't detect on its own is changes to the build tooling itself, like your config file or a custom loader. That's why you set `buildDependencies`:

```js
module.exports = {
  cache: {
    type: "filesystem",
    version: process.env.APP_ENV,
    buildDependencies: {
      config: [__filename, require.resolve("./loaders/my-loader.js")],
    },
  },
};
```

- `buildDependencies` lists files whose changes should wipe the cache. webpack also follows their own dependencies.
- `version` lets you bust the cache when something outside files changes, like an environment variable used in `DefinePlugin`.
- `name` keeps separate caches for different configs, like dev and prod.

Packages in `node_modules` are treated as immutable and checked by version from `package.json`, controlled by `snapshot.managedPaths`. If you patch files in `node_modules` by hand, the cache won't notice.

## 94: Why can the hash of a file change even though its content didn't, and how does webpack 5 handle it?

In older setups, hashes were often calculated before the final output was ready. Things like module ids changing when you add a new file, the runtime's chunk map changing, or the minifier's output being different from what was hashed could all change a hash even if the real content stayed the same, or the opposite.

webpack 5 addresses this with:

- `moduleIds: 'deterministic'` and `chunkIds: 'deterministic'`, which create short ids based on the module path, so adding a module doesn't renumber the others.
- `optimization.realContentHash` (on by default in production), which recalculates `[contenthash]` from the final asset content after minification and processing, and updates references to it.
- Splitting the runtime with `runtimeChunk: 'single'`, so changes in the chunk map only change the small runtime file.

If hashes still change unexpectedly, compare two `stats.json` files to see which modules or ids changed.

## 95: How do you control where asset modules are written and how they are named?

There are a few levels of control:

```js
module.exports = {
  output: {
    assetModuleFilename: "assets/[hash][ext][query]",
  },
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|webp)$/i,
        type: "asset",
        parser: {
          dataUrlCondition: { maxSize: 10 * 1024 },
        },
        generator: {
          filename: "images/[name].[contenthash:8][ext]",
          publicPath: "https://img.example.com/",
        },
      },
    ],
  },
};
```

- `output.assetModuleFilename` sets the default name for all assets.
- `generator.filename` overrides it per rule.
- `generator.publicPath` and `generator.outputPath` let you serve some assets from a different URL or folder.
- `parser.dataUrlCondition` sets when the `asset` type inlines files. It can also be a function for custom logic.
- `generator.dataUrl` lets you change how data URIs are encoded, for example using a custom encoder for SVG.
- `generator.emit: false` gives you the URL without writing the file, which is useful for server builds.

## 96: How do you output ES modules from webpack?

By default webpack outputs scripts that use its own module system. To produce real ES modules (with `import`/`export`), turn on the experiment and set the library type:

```js
module.exports = {
  experiments: {
    outputModule: true,
  },
  output: {
    module: true,
    library: { type: "module" },
    chunkFormat: "module",
  },
};
```

This is useful for building libraries that other bundlers will consume, or for apps that run as `<script type="module">`. For libraries, the newer `library.type: 'modern-module'` keeps exports closer to the original source, which helps tree shaking in the consumer's bundler.

It's still behind `experiments` in webpack 5, so check the release notes when you upgrade if you depend on it.

## 97: What are some useful options under experiments in webpack 5?

- `topLevelAwait` lets you use `await` at the top level of a module. It's on by default since 5.83.
- `asyncWebAssembly` lets you import `.wasm` files as async modules, following the newer WebAssembly ESM proposal.
- `outputModule` outputs ES modules (see the previous question).
- `lazyCompilation` builds dynamic imports and entries only when they're requested in development.
- `css` turns on native CSS support, so webpack can handle CSS without `css-loader` and `MiniCssExtractPlugin`. The webpack team plans to make this the default in webpack 6.
- `buildHttp` lets you import modules directly from `https://` URLs with a lockfile.
- `futureDefaults` turns on the defaults planned for the next major version, so you can test your project against them early.

Experiments can change in minor versions, so pin your webpack version if you rely on them.

## 98: What is lazy compilation and when would you use it?

With lazy compilation, webpack doesn't build dynamic imports (and optionally entries) when the dev server starts. It builds them only when the browser actually requests them.

```js
module.exports = {
  experiments: {
    lazyCompilation: {
      entries: false,
      imports: true,
    },
  },
};
```

In a big app with many routes, this makes dev server startup much faster, since you usually only open a few pages during a session. The cost is a short delay the first time you visit a route, while webpack compiles it.

It's meant for development only. It also needs the dev server's backend to talk to the browser, so it works best with `webpack serve`.

## 99: How do you make webpack work with a strict Content Security Policy?

A strict CSP can block things webpack does by default:

- `eval`-based source maps (`devtool: 'eval...'`) need `unsafe-eval`. Use a non-eval `devtool` like `source-map` in production.
- `style-loader` injects `<style>` tags, which a strict `style-src` blocks. Use `MiniCssExtractPlugin` in production.
- Scripts for lazy chunks are added at runtime and need a nonce if your CSP uses nonces.

For the nonce, set `__webpack_nonce__` before any chunk loads. webpack adds it to every script tag it creates:

```js
// first module in the entry
__webpack_nonce__ = document.querySelector('meta[name="csp-nonce"]').content;
```

The server generates a new nonce for each request and puts it in both the CSP header and the page. If your site uses Trusted Types, set `output.trustedTypes` so webpack creates script URLs through a Trusted Types policy.

## 100: How do you add Subresource Integrity to webpack bundles?

Subresource Integrity (SRI) adds an `integrity` hash to script and link tags, so the browser refuses to run a file that was changed on the CDN. webpack doesn't do this by itself. You use `webpack-subresource-integrity`:

```js
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { SubresourceIntegrityPlugin } = require("webpack-subresource-integrity");

module.exports = {
  output: {
    crossOriginLoading: "anonymous",
  },
  plugins: [
    new HtmlWebpackPlugin(),
    new SubresourceIntegrityPlugin({ hashFuncNames: ["sha384"] }),
  ],
};
```

The plugin adds `integrity` to the tags in the HTML and also to the lazy chunks loaded at runtime. `crossOriginLoading` is required, because the browser only checks integrity on cross-origin requests made with CORS. Your CDN must send the right CORS headers. Any later step that changes files (like a CDN that minifies them again) will break the hashes.

## 101: How do you set the public path at runtime?

Sometimes you don't know the asset URL at build time, for example when the same build is deployed to different CDNs or the app is embedded in other sites. webpack has two options.

`publicPath: 'auto'` (the default in webpack 5 for web targets) works out the path from the URL of the script that is running, using `document.currentScript`.

Or you set it yourself with `__webpack_public_path__` before anything else loads:

```js
// public-path.js
__webpack_public_path__ = window.APP_CONFIG.cdnUrl;
```

```js
// index.js
import "./public-path";
import "./app";
```

It has to be in a separate file imported first. Because ES imports are hoisted, setting it in the same file as other imports would run too late. This only affects chunks and assets loaded by the runtime. Script tags already written in the HTML need to be correct on their own.

## 102: How do you profile a slow webpack build?

Start by finding out where the time goes instead of guessing.

```bash
npx webpack --profile --progress
```

`--profile` adds timing info to stats, and `--progress` shows which phase is slow. For more detail, use the built-in `ProfilingPlugin`:

```js
const webpack = require("webpack");

module.exports = {
  plugins: [
    new webpack.debug.ProfilingPlugin({ outputPath: "profiling/events.json" }),
  ],
};
```

It creates a Chrome trace file you can open in the Chrome DevTools Performance panel. You'll see how long each plugin hook and loader took.

You can also run webpack with `node --cpu-prof node_modules/webpack/bin/webpack.js` and open the `.cpuprofile` in DevTools. `speed-measure-webpack-plugin` was popular before, but it doesn't work well with webpack 5 and is no longer maintained. For memory issues, `node --inspect` and heap snapshots help find plugins holding on to old compilations.

## 103: How would you speed up builds in a large monorepo with webpack?

Some ideas, from easiest to hardest:

- Turn on the filesystem cache, and keep it between CI runs by caching `node_modules/.cache/webpack`.
- Use fast transpilers (`swc-loader` or `esbuild-loader`) and move type checking out of the build.
- Point loaders at the right folders with `include`, and set `resolve.symlinks` correctly for workspace packages.
- Consume internal packages from source with the right `resolve.alias` or `conditionNames`, instead of building each package separately and then rebundling it.
- Only build what changed, using a monorepo tool like Nx or Turborepo that caches build outputs per project.
- Split big apps into smaller deployables (for example with Module Federation) so each team builds only their part.
- Try Rspack, which is designed as a mostly drop-in replacement and is much faster on large codebases.

`DllPlugin` was the old way to prebuild vendor code. With persistent caching in webpack 5 it's rarely worth the extra setup.

## 104: A production bundle is 3 MB. How would you approach reducing it?

1. Measure. Run `webpack-bundle-analyzer` and look at the biggest modules and duplicates. Check the gzip or Brotli sizes, not only the raw sizes.
2. Make sure it's really a production build: `mode: 'production'`, minification on, no `eval` source maps, and `process.env.NODE_ENV` set to `production` so React and other libs drop dev code.
3. Lazy load. Split routes and heavy features (charts, editors, PDF viewers) with dynamic `import()`.
4. Fix tree shaking. Check that Babel or TypeScript isn't turning ESM into CommonJS, use ESM versions of libraries (`lodash-es`), and import only what you need.
5. Replace or trim heavy libraries. Remove `moment` locales, swap big libraries for smaller ones, and check whether a polyfill is really needed for your target browsers.
6. Remove duplicates. If two versions of a package are bundled, align them in `package.json` or with `resolve.alias`.
7. Split vendors and add `[contenthash]` so repeat visits reuse cached files.
8. Set `performance.hints: 'error'` with a budget in CI so it doesn't grow back.

## 105: How do you find and fix duplicate packages in a bundle?

Duplicates happen when different dependencies need different versions of the same package, so npm installs several copies. Each copy gets bundled.

To find them:

- `webpack-bundle-analyzer` shows the same package name in several places.
- `npm ls package-name` (or `yarn why`, `pnpm why`) shows which dependencies pull in which version.
- `duplicate-package-checker-webpack-plugin` warns during the build.

To fix them:

- Update dependencies so they agree on a version range, then reinstall. `npm dedupe` can help.
- Use `overrides` (npm), `resolutions` (Yarn) or `pnpm.overrides` to force one version.
- As a last resort, force webpack to use one copy:

```js
const path = require("path");

module.exports = {
  resolve: {
    alias: {
      react: path.resolve(__dirname, "node_modules/react"),
    },
  },
};
```

Forcing a single version is only safe if the versions are compatible. For packages like React, duplicates don't just waste space, they also cause runtime errors like "Invalid hook call".

## 106: How do you set up webpack for server-side rendering?

You usually build twice: once for the browser and once for Node.

```js
const nodeExternals = require("webpack-node-externals");

const client = {
  name: "client",
  target: "web",
  entry: "./src/client.jsx",
  output: {
    filename: "[name].[contenthash].js",
    path: __dirname + "/dist/client",
  },
};

const server = {
  name: "server",
  target: "node",
  entry: "./src/server.jsx",
  externalsPresets: { node: true },
  externals: [nodeExternals()],
  output: {
    filename: "server.js",
    path: __dirname + "/dist/server",
    library: { type: "commonjs2" },
  },
};

module.exports = [client, server];
```

Points to watch:

- `target: 'node'` and `externals` keep Node built-ins and `node_modules` out of the server bundle.
- CSS and assets should not be injected on the server. Use `css-loader` with `modules: { exportOnlyLocals: true }` for CSS Modules, and `generator.emit: false` for assets, so the server gets class names and URLs without duplicating files.
- The server needs to know which client files to include in the HTML. Plugins like `webpack-manifest-plugin` write a manifest the server can read.

Frameworks like Next.js handle all of this for you, which is why custom SSR webpack setups are less common now.

## 107: Your Module Federation host breaks after a remote deploys a new React version. How do you debug and prevent it?

Steps to debug:

- Check the console for shared module warnings like "Unsatisfied version". They tell you which package and versions don't match.
- In DevTools, check whether React was loaded twice. Two copies usually show up as "Invalid hook call" errors.
- Check the `shared` config on both sides. If `singleton` is missing on one side, or `requiredVersion` ranges don't overlap, you can end up with two copies or a version that doesn't fit.

To prevent it:

- Use `singleton: true` for React, React DOM and any library that keeps global state (routers, state managers).
- Agree on version ranges across teams and use `strictVersion` where a mismatch would really break things, so the problem shows up as a clear error.
- Version your remotes. Point hosts at a versioned `remoteEntry.js` URL or use a manifest, instead of always loading the latest build.
- Add contract or end-to-end tests that load the host with the new remote before releasing it.
- Keep a fallback (an error boundary and a fallback UI) around remote components, so one broken remote doesn't take down the whole page.

## 108: What are the trade-offs when configuring splitChunks for many small chunks?

More chunks means better caching (a change in one module only invalidates a small file) and less unused code per page. But it also means more requests, more runtime work to connect chunks, and worse compression, because gzip and Brotli work better on bigger files.

With HTTP/2 or HTTP/3, many parallel requests are cheaper than with HTTP/1.1, but they're still not free. Options that control this:

```js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: "all",
      minSize: 20000,
      maxSize: 250000,
      maxInitialRequests: 25,
      maxAsyncRequests: 30,
    },
  },
};
```

- `minSize` stops tiny chunks from being created.
- `maxSize` tries to split chunks bigger than the limit. It's a hint, not a hard rule, and it doesn't split a single module that is bigger than the limit.
- `maxInitialRequests` and `maxAsyncRequests` cap the number of parallel requests for an entry or an `import()`.

There's no single right setting. Test real pages with Lighthouse or WebPageTest on a slow network and compare.

## 109: How does webpack resolve a bare import like import x from 'some-package'?

webpack uses `enhanced-resolve`. For a bare import it:

1. Looks for a `node_modules/some-package` folder, starting from the current file's folder and going up (configured by `resolve.modules`).
2. Reads its `package.json`. If there's an `exports` field, it uses it and checks the conditions in `resolve.conditionNames`, such as `webpack`, `development` or `production`, `browser`, `import` or `require`, and `module`. If a subpath isn't listed in `exports`, the import fails, even if the file exists.
3. If there's no `exports`, it uses `resolve.mainFields`. For the `web` target the default is `['browser', 'module', 'main']`, so a browser or ESM build is preferred over the CommonJS one.
4. Tries the extensions from `resolve.extensions` and `index` files (`resolve.mainFiles`) when needed.

Before all this, `resolve.alias` is applied. If something resolves to the wrong file, setting `stats: { errorDetails: true }` shows each path webpack tried, and `resolve.byDependency` lets you use different resolve options for `import` and `require`.

## 110: What is the difference between javascript/auto and javascript/esm module types?

webpack decides how strict to be when parsing a file based on its module type:

- `javascript/auto` is used for normal `.js` files. Both ESM and CommonJS syntax are allowed, and webpack figures out which one the file uses.
- `javascript/esm` is used for `.mjs` files, and for `.js` files inside a package with `"type": "module"`. It follows Node's ESM rules: no `require` or `module.exports`, and imports of CommonJS modules only get the `default` export (which is `module.exports`).
- `javascript/dynamic` is CommonJS only.

The strict mode is where the "fully specified" rule comes from. In `javascript/esm`, relative imports must include the file extension, so `import './utils'` fails and must be `import './utils.js'`. If a third-party package triggers this error, you can relax it for that package:

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.m?js$/,
        resolve: { fullySpecified: false },
      },
    ],
  },
};
```

## 111: Why can importing a CommonJS module from an ES module give unexpected results?

CommonJS has one export, `module.exports`, while ES modules have a `default` export plus named exports. Bundlers have to map one to the other, and they don't all do it the same way.

```js
// lib.cjs
module.exports = { greet: () => "hi" };
```

```js
import lib from "./lib.cjs";
import { greet } from "./lib.cjs";
```

In a normal `.js` file (`javascript/auto`), webpack allows both imports. In an `.mjs` file (`javascript/esm`), only the default import works, matching Node.

It gets tricky with code compiled from ESM to CommonJS by Babel or TypeScript. That code sets `exports.__esModule = true`, and webpack then treats `exports.default` as the default export. So `import x from 'pkg'` might give you the function in webpack but an object `{ default: fn }` in Node or another tool. When you see `x.default is not a function` or `x is not a function`, this interop is the usual cause. Checking which file the package resolves to (its ESM or CJS build) often explains it.

## 112: What security problems can a webpack config cause?

- Exposing secrets. Anything passed to `DefinePlugin`, `EnvironmentPlugin` or `dotenv-webpack` ends up in the public JS. Doing something like `'process.env': JSON.stringify(process.env)` leaks every variable on the build machine, including CI tokens.
- Public source maps. `source-map` in production lets anyone read your original source code, including comments. Use `hidden-source-map` and upload maps to your error tracker, or block `.map` files on the server.
- Running a dev server in production, or exposing it to the network. Use `allowedHosts` and don't bind to `0.0.0.0` on untrusted networks. Older versions had DNS rebinding issues, so keep webpack-dev-server updated.
- Supply chain risk. Loaders and plugins run with full access to your machine and CI. Pin versions with a lockfile, review new build dependencies and run `npm audit`.
- CSP problems from `eval` source maps or injected styles (see the CSP question).

## 113: Users see ChunkLoadError after a deploy. Why does it happen and how do you handle it?

The user's browser has the old `main.js` loaded. Its runtime knows the old chunk file names. After a deploy, those old files are deleted from the server, so when the user goes to a lazy route, `import()` requests a file that no longer exists and fails with `ChunkLoadError`.

Ways to handle it:

- Keep old assets on the server or CDN for some time after each deploy (for example, upload new files without deleting old ones and clean up after a few days). This is the most reliable fix.
- Catch the error and reload the page once, so the user gets the new version:

```js
function lazyWithReload(factory) {
  return React.lazy(async () => {
    try {
      return await factory();
    } catch (error) {
      if (
        error.name === "ChunkLoadError" &&
        !sessionStorage.getItem("reloaded")
      ) {
        sessionStorage.setItem("reloaded", "1");
        window.location.reload();
      }
      throw error;
    }
  });
}
```

- Don't cache `index.html` so new visits always get the latest file names.
- Check that `publicPath` is correct. A wrong `publicPath` causes the same error on every lazy chunk, not just after deploys.

## 114: How do you get emitted assets in a plugin, and what is processAssets?

In webpack 5 the right place to add, change or remove output files is the `processAssets` hook of the compilation. It runs in stages, so plugins run in a predictable order (for example, your plugin can run before or after minification).

```js
const { Compilation, sources } = require("webpack");

class AssetListPlugin {
  apply(compiler) {
    compiler.hooks.thisCompilation.tap("AssetListPlugin", (compilation) => {
      compilation.hooks.processAssets.tap(
        {
          name: "AssetListPlugin",
          stage: Compilation.PROCESS_ASSETS_STAGE_REPORT,
        },
        (assets) => {
          const list = Object.keys(assets).sort().join("\n");
          compilation.emitAsset("assets.txt", new sources.RawSource(list));
        },
      );
    });
  }
}

module.exports = AssetListPlugin;
```

Some of the stages, in order: `ADDITIONAL`, `PRE_PROCESS`, `DERIVED`, `ADDITIONS`, `OPTIMIZE`, `OPTIMIZE_SIZE` (minifiers), `DEV_TOOLING` (source maps), `SUMMARIZE`, `OPTIMIZE_HASH`, `REPORT`. Use `compilation.emitAsset`, `updateAsset` and `deleteAsset` instead of changing `compilation.assets` directly. Older plugins that add assets in the `emit` hook still work but print a deprecation warning. Tapping `thisCompilation` instead of `compilation` keeps the plugin from running in child compilations.

## 115: What is a child compiler?

A child compiler is a separate compilation that runs inside the main one, with its own entries and settings, but sharing the parent's file system and some caches. Plugins create them with `compilation.createChildCompiler(name, outputOptions, plugins)`.

Examples:

- `HtmlWebpackPlugin` uses one to compile the HTML template, so templates can use loaders and `require`.
- `MiniCssExtractPlugin` used child compilers in older versions to evaluate CSS modules.
- Service worker plugins like Workbox's `InjectManifest` compile the service worker file with one.

Child compilers make the build slower and add complexity. Hooks tapped on `compiler.hooks.compilation` also fire for child compilations, which is a common source of plugins running twice. That's why plugins that only care about the main build use `thisCompilation`.

## 116: How do you run webpack from Node.js code?

Use the Node API, which is useful for custom build scripts and tools.

```js
const webpack = require("webpack");
const config = require("./webpack.config.js");

const compiler = webpack(config);

compiler.run((err, stats) => {
  if (err) {
    console.error(err.stack || err);
    process.exitCode = 1;
    return;
  }

  console.log(stats.toString({ colors: true, chunks: false }));

  if (stats.hasErrors()) {
    process.exitCode = 1;
  }

  compiler.close((closeErr) => {
    if (closeErr) console.error(closeErr);
  });
});
```

There are two kinds of errors. `err` means webpack itself failed (bad config, crash). Compilation errors like syntax errors in your code are in `stats` and you check them with `stats.hasErrors()`. Many scripts only check `err` and miss real build errors. Always call `compiler.close()` when done, so the persistent cache is saved and resources are released. For watch mode, use `compiler.watch(watchOptions, callback)`.

## 117: How do you make webpack builds reproducible across machines?

The same commit should give the same output files everywhere, so caching and deploys behave predictably. Things that break this:

- Different dependency versions. Commit the lockfile and use `npm ci`.
- Different Node or webpack versions. Pin them with `engines`, `.nvmrc` or a Docker image.
- Absolute paths in the output. webpack uses paths relative to `context` for ids, but some loaders and plugins put absolute paths into code or source maps. Check the output for your home folder or CI paths.
- Non-deterministic ids. Use `moduleIds: 'deterministic'` and `chunkIds: 'deterministic'` (production default) and avoid `'named'` ids in production builds.
- Build-time values like `Date.now()` or the git commit hash injected with `DefinePlugin`. These are fine if expected, but they change hashes on every build.
- File order from the file system, for example in context modules. webpack sorts these, but custom plugins may not.

To check, build twice in clean environments and compare the output folders with a diff.

## 118: When would you choose webpack, Vite or Rspack for a new project?

- Vite is the default for most new single-page apps today. Its dev server serves native ES modules and only transforms files the browser requests, so it starts almost instantly, and the config is simpler. Production builds use Rollup (and Rolldown in newer versions).
- Rspack is a webpack-compatible bundler written in Rust. It supports most webpack config options, loaders and plugins, and is often 5 to 10 times faster. It's a good choice when you have an existing webpack setup and want speed without rewriting everything.
- webpack makes sense when you depend on plugins that have no Vite or Rspack version, need very custom build logic, or you have a large existing setup that works and isn't worth migrating.

In an interview it helps to say it depends on the project. For an existing large webpack project, migrating to Rspack is usually lower risk than moving to Vite. For a new project with no special needs, Vite or a framework (Next.js, Angular CLI, and so on) is usually simpler.

## 119: What is Rspack and how compatible is it with webpack?

Rspack is a bundler written in Rust by ByteDance's web infra team. It follows webpack's architecture and config format closely, so many projects can switch by changing the import:

```js
const rspack = require("@rspack/core");

module.exports = {
  entry: "./src/index.js",
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        use: { loader: "builtin:swc-loader" },
      },
    ],
  },
  plugins: [new rspack.HtmlRspackPlugin()],
};
```

Most popular loaders (`sass-loader`, `postcss-loader`, `babel-loader`) work, and many webpack plugins work too. Rspack also has built-in Rust versions of common tools, like `builtin:swc-loader`, CSS support and `HtmlRspackPlugin`, which are faster than their JavaScript counterparts.

The limits: plugins that depend on deep webpack internals (some `Compilation` APIs or the module graph) may not work or need a Rspack version. Check the compatibility list in the Rspack docs before migrating. Rspack 1.0 was released in 2024, and it's used in production by large companies.

## 120: How would you debug a loader or plugin that behaves wrong?

- Add logging with webpack's logger: `compiler.getInfrastructureLogger('MyPlugin')` in plugins, or `this.getLogger()` in loaders. Turn on output with `infrastructureLogging: { level: 'verbose' }` or `stats: { logging: 'verbose' }`.
- Use the Node debugger. Run `node --inspect-brk node_modules/webpack/bin/webpack.js`, open `chrome://inspect` and set breakpoints inside the loader or plugin code.
- Turn off caching while debugging (`cache: false`), otherwise webpack may skip your loader because the result is already cached.
- Test a loader in isolation with `loader-runner`, the same package webpack uses to run loaders, so you don't need a full build.
- Look at the generated code with `mode: 'development'` and `devtool: false`, so the output is readable and not wrapped in `eval`.
- Use `stats: { errorDetails: true, moduleTrace: true }` to see where an error comes from in the dependency chain.
- Check your plugin isn't running twice because of child compilations (use `thisCompilation`), and that async hooks call their callback or return a promise, otherwise the build hangs.
