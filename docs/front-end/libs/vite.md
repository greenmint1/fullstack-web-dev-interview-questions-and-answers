# Vite Interview Questions and Answers

_Last updated: October 28, 2026_

450 Vite interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers are for Vite 8 (8.x), which uses Rolldown as its bundler and Oxc for transforms and minification, for both dev and production. Older setups (esbuild for dev and Rollup for production, `build.rollupOptions`, the `esbuild` config option) are mentioned where they still matter, since many projects still run Vite 5, 6 or 7.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

# Easy Questions (1-150)

## 1: What is Vite?

Vite is a build tool and dev server for front-end projects. It has two parts:

- a **dev server** that serves your source files as native ES modules, with very fast Hot Module Replacement (HMR)
- a **build command** that bundles your code for production with Rolldown

It was created by Evan You (the author of Vue), but it works with React, Vue, Svelte, Solid, Preact, Lit, plain JavaScript and more.

## 2: How do you pronounce Vite and what does the name mean?

It is pronounced "veet", like "street". It is the French word for "quick", which is the main goal of the tool.

## 3: Why was Vite created? What problem does it solve?

Older bundler-based dev servers (like webpack dev server) had to bundle the whole app before they could serve anything. On big projects that means waiting a long time for the server to start, and HMR updates slow down as the app grows.

Vite avoids this by not bundling your source code in development. The browser asks for modules as it needs them and Vite transforms only those files. Dependencies are pre-bundled once and cached. So startup is fast and HMR speed does not depend much on app size.

## 4: How do you create a new Vite project?

Use `create-vite`:

```bash
npm create vite@latest
```

It asks for a project name, a framework and a variant (TypeScript or JavaScript). You can also pass everything on the command line:

```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npm run dev
```

With pnpm or yarn: `pnpm create vite`, `yarn create vite`.

## 5: Which templates does create-vite offer?

The official templates include `vanilla`, `vue`, `react`, `preact`, `lit`, `svelte`, `solid` and `qwik`, each with a `-ts` version (for example `react-ts`, `vue-ts`). There are also community templates, which you can use with tools like `degit`.

## 6: What Node.js version does Vite 8 need?

Vite 8 needs Node.js 20.19+ or 22.12+ (same as Vite 7). These versions support `require(esm)` without a flag, so Vite can be published as ESM only.

## 7: What are the main npm scripts in a Vite project?

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

- `vite` (or `vite dev`, `vite serve`) starts the dev server.
- `vite build` creates the production build in `dist`.
- `vite preview` serves the `dist` folder locally so you can check the build.

React and Vue TypeScript templates usually run `tsc -b` (or `vue-tsc -b`) before `vite build`, because Vite does not type check.

## 8: What is the default port of the Vite dev server?

`5173`. If the port is taken, Vite tries the next one (5174, 5175 and so on). The preview server uses `4173` by default.

```js
export default defineConfig({
  server: { port: 3000 },
});
```

## 9: What is vite.config.js?

It is the config file Vite loads from the project root. It can be `vite.config.js`, `.mjs`, `.ts`, `.cjs`, `.mts` or `.cts`. You export a config object, usually wrapped in `defineConfig` to get type hints.

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
});
```

## 10: What does defineConfig do?

`defineConfig` is a helper that returns the config you pass in. It does nothing at runtime. Its only job is to give you TypeScript types and autocomplete in the editor, even in a plain `.js` file.

You can also use a JSDoc comment instead:

```js
/** @type {import('vite').UserConfig} */
export default {
  // ...
};
```

## 11: Why is index.html in the project root and not in a public folder?

In Vite, `index.html` is the entry point of the app, not a static file. Vite reads it, finds the `<script type="module" src="...">` tags and other links, and uses them as the start of the module graph. That is why it lives in the project root (or in the folder set by `root`).

```html
<!doctype html>
<html>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## 12: What does the project root mean in Vite?

The root is the folder that contains `index.html`. By default it is the current working directory. Absolute URLs in your source code (like `/src/main.ts`) are resolved against this folder. You can change it with `root` in the config or by passing a path: `vite serve some/sub/dir`.

## 13: What are native ES modules and why does Vite use them?

Native ES modules are the `import` and `export` syntax that browsers understand directly when a script has `type="module"`. The browser downloads each imported file with a separate request.

Vite uses this in development: instead of building one big bundle, it lets the browser request modules one by one and transforms each file on demand. This is the main reason the dev server starts so fast.

## 14: How is Vite different from webpack?

- **Dev mode:** webpack bundles the app before serving it. Vite serves source files as native ESM and only transforms what the browser asks for.
- **Config:** Vite has sensible defaults, so most projects need very little config. webpack often needs loaders and plugins for basic things like CSS or TypeScript.
- **Production:** webpack uses its own bundler. Vite 8 uses Rolldown (earlier versions used Rollup).
- **Speed:** Vite is usually much faster to start and to update in dev, because the heavy work is done by tools written in Rust (Rolldown and Oxc).

webpack is still more flexible in some edge cases and has a very large plugin ecosystem, and many older projects still use it.

## 15: What is Rolldown?

Rolldown is a JavaScript bundler written in Rust, made by the Vite team (VoidZero). It has a Rollup-compatible plugin API, so most Rollup and Vite plugins still work. Since Vite 8, Rolldown is the single bundler for both dependency pre-bundling in dev and production builds. Rolldown 1.0 was released in May 2026.

## 16: What is Oxc and how does Vite use it?

Oxc (the JavaScript Oxidation Compiler) is a set of JavaScript tools written in Rust: parser, transformer, minifier, resolver and linter. Vite 8 uses Oxc to:

- transform TypeScript and JSX
- minify JavaScript in production (the default `build.minify` value is `'oxc'`)

Before Vite 8 these jobs were done by esbuild.

## 17: What did Vite use before Rolldown?

Vite 2 to 7 used two tools:

- **esbuild** for dependency pre-bundling in dev, TS/JSX transforms and minification
- **Rollup** for production builds

This sometimes caused small differences between dev and production behavior. Vite 8 replaced both with Rolldown (plus Oxc), so dev and build use the same pipeline.

## 18: Does Vite support TypeScript out of the box?

Yes. You can import `.ts` and `.tsx` files without any setup. Vite only strips the types (with Oxc). It does not type check. You run type checking separately, for example `tsc --noEmit` in your build script, in CI, or in your editor.

## 19: Why doesn't Vite type check TypeScript?

Type checking needs the whole program, and it is slow. Vite transforms each file on its own, which is very fast. The Vite team chose to leave type checking to the IDE and to a separate `tsc` run. If you want errors in the browser overlay during dev, you can use a plugin like `vite-plugin-checker`.

## 20: What is the public folder?

Files in `public/` are copied as they are to the root of the output folder and served at `/` in dev. They are not processed or hashed. Use it for files that:

- must keep their exact name, like `robots.txt` or `favicon.ico`
- are never imported in your code

```html
<link rel="icon" href="/favicon.ico" />
```

Always reference them with an absolute path, without `public` in the URL.

## 21: What is the difference between the public folder and importing an asset?

- **Imported assets** (`import logo from './logo.png'`) go through the build. They get a content hash in the file name, small ones can be inlined as base64, and missing files cause a build error.
- **Public files** are copied as they are, keep their name and are never checked.

Prefer imports for most assets. Use `public` only for files that need a fixed name or are not referenced from code.

## 22: How do you import an image in Vite?

Import it like a module. You get the final URL as a string.

```js
import logoUrl from "./assets/logo.png";

const img = document.createElement("img");
img.src = logoUrl; // "/assets/logo-B3x9fK2a.png" in production
```

In dev the URL is something like `/src/assets/logo.png`. In production it is the hashed file in `dist/assets`.

## 23: How do you import CSS in Vite?

Just import the file. Vite injects it into the page in dev (with HMR) and extracts it into a `.css` file in production.

```js
import "./styles.css";
```

`@import` inside CSS files is also supported, and Vite inlines those imports.

## 24: What are CSS Modules and how do you use them in Vite?

Any file ending with `.module.css` (or `.module.scss` etc.) is treated as a CSS Module. Class names are made unique, and the import gives you an object that maps the original names to the generated ones.

```css
/* button.module.css */
.primary {
  color: white;
}
```

```js
import styles from "./button.module.css";

button.className = styles.primary;
```

## 25: Does Vite support Sass, Less and Stylus?

Yes. You just install the preprocessor, no plugin is needed:

```bash
npm add -D sass-embedded # or sass
npm add -D less
npm add -D stylus
```

Then import `.scss`, `.sass`, `.less` or `.styl` files directly.

## 26: How does Vite support PostCSS?

If the project has a PostCSS config (`postcss.config.js` and similar), Vite applies it to all imported CSS automatically. You can also put the config inline in `vite.config` under `css.postcss`.

## 27: How do you use environment variables in Vite?

Vite exposes env variables on `import.meta.env`. Variables from `.env` files are exposed to client code only if they start with `VITE_`.

```bash
# .env
VITE_API_URL=https://api.example.com
DB_PASSWORD=secret
```

```js
console.log(import.meta.env.VITE_API_URL); // works
console.log(import.meta.env.DB_PASSWORD); // undefined
```

## 28: Why do env variables need the VITE_ prefix?

To avoid leaking secrets by mistake. Everything exposed to client code ends up in the JavaScript bundle that anyone can read. The prefix forces you to choose on purpose which variables are public. You can change the prefix with `envPrefix`.

## 29: What built-in env variables does Vite provide?

- `import.meta.env.MODE`: the current mode (`development`, `production` or a custom one)
- `import.meta.env.BASE_URL`: the base URL from the `base` option
- `import.meta.env.PROD`: `true` in production
- `import.meta.env.DEV`: `true` in development (always the opposite of `PROD`)
- `import.meta.env.SSR`: `true` when the code runs on the server

```js
if (import.meta.env.DEV) {
  console.log("debug info");
}
```

## 30: Which .env files does Vite load?

```
.env                # loaded in all modes
.env.local          # loaded in all modes, ignored by git
.env.[mode]         # loaded only in the given mode
.env.[mode].local   # loaded only in the given mode, ignored by git
```

Mode-specific files win over generic ones, and `.local` files win over non-local ones. Variables that already exist in the shell when you run Vite have the highest priority.

## 31: What is a mode in Vite?

A mode is a name that decides which `.env.[mode]` file is loaded and the value of `import.meta.env.MODE`. By default `vite dev` uses `development` and `vite build` uses `production`. You can set a custom one:

```bash
vite build --mode staging
```

This loads `.env.staging`.

## 32: What is the difference between mode and NODE_ENV?

They are separate. `mode` controls which `.env` files are loaded and `import.meta.env.MODE`. `NODE_ENV` controls `process.env.NODE_ENV` and whether libraries use their production code. For example, `vite build --mode staging` still sets `NODE_ENV` to `production` by default, so you get a production build with staging env values.

## 33: How do you add TypeScript types for your own env variables?

Create a `vite-env.d.ts` (or any `.d.ts` file included by tsconfig) and extend `ImportMetaEnv`:

```ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_APP_TITLE: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## 34: What does the vite/client type reference give you?

It adds types for Vite-specific features in client code:

- asset imports (`.svg`, `.png`, `.css` etc.)
- `import.meta.env`
- `import.meta.hot` (HMR API)
- `import.meta.glob`

You add it with `/// <reference types="vite/client" />` or in `tsconfig.json` under `compilerOptions.types: ["vite/client"]`.

## 35: What is Hot Module Replacement (HMR)?

HMR updates changed modules in the running app without a full page reload. For example, if you edit a React component, only that component is replaced and its state is usually kept. Vite has HMR built in, and framework plugins (React, Vue, Svelte) hook into it so you get this behavior with no extra setup.

## 36: What happens when a module cannot be hot updated?

Vite walks up the importers of the changed file looking for an "HMR boundary", a module that accepts updates. If none is found, Vite does a full page reload. Changes to `vite.config` or `.env` files restart the dev server.

## 37: How do you install a Vite plugin?

Install the package and add it to the `plugins` array:

```bash
npm add -D @vitejs/plugin-vue
```

```js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
});
```

## 38: What official plugins does Vite have?

- `@vitejs/plugin-vue` for Vue 3 single file components
- `@vitejs/plugin-vue-jsx` for Vue 3 JSX
- `@vitejs/plugin-react` for React (Fast Refresh with Oxc)
- `@vitejs/plugin-react-swc` for React with SWC
- `@vitejs/plugin-rsc` for React Server Components
- `@vitejs/plugin-legacy` for older browser support

Other frameworks maintain their own plugins, for example `@sveltejs/vite-plugin-svelte`.

## 39: What is the difference between @vitejs/plugin-react and @vitejs/plugin-react-swc?

Both give you React Fast Refresh. `plugin-react` v6 uses Oxc for the Refresh transform and no longer depends on Babel. `plugin-react-swc` uses SWC. In older versions the main reason to choose SWC was speed, since `plugin-react` used Babel. Today the difference is small. SWC is useful if you need SWC plugins.

## 40: Where does vite build put the output?

In `dist` by default. JS, CSS and assets go into `dist/assets` with hashed file names. You can change the folder with `build.outDir` and the assets subfolder with `build.assetsDir`.

## 41: What does vite preview do?

It starts a simple static server for the `dist` folder so you can test the production build on your machine. It is not a production server and should not be used to host your app.

```bash
npm run build
npm run preview
```

## 42: How do you change the base path for deploying under a sub-folder?

Use the `base` option. For example, for GitHub Pages at `https://user.github.io/my-repo/`:

```js
export default defineConfig({
  base: "/my-repo/",
});
```

Vite rewrites asset URLs in JS, CSS and HTML to use this base. In code you can read it with `import.meta.env.BASE_URL`.

## 43: How do you set up a path alias like @ for src?

Use `resolve.alias`:

```ts
import { defineConfig } from "vite";
import { fileURLToPath, URL } from "node:url";

export default defineConfig({
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
```

For TypeScript you also add `paths` in `tsconfig.json`. Since Vite 8 you can set `resolve.tsconfigPaths: true` to let Vite read `paths` from tsconfig directly, so you don't need both.

## 44: How do you open the browser automatically when the dev server starts?

```js
export default defineConfig({
  server: { open: true },
});
```

Or on the command line: `vite --open`. You can also pass a path: `open: '/docs'`.

## 45: How do you make the dev server reachable from other devices on the network?

By default Vite listens only on `localhost`. To listen on all addresses:

```bash
vite --host
```

or

```js
export default defineConfig({
  server: { host: true }, // same as '0.0.0.0'
});
```

Then you can open the app from your phone with your computer's IP address.

## 46: What is dependency pre-bundling?

When you start the dev server for the first time, Vite scans your code for imports of npm packages and bundles them with Rolldown into `node_modules/.vite/deps`. This does two things:

- converts CommonJS and UMD packages to ESM so the browser can load them
- merges packages with many internal files (like `lodash-es`) into one file, so the browser does not make hundreds of requests

The result is cached, so later starts are fast.

## 47: Where is the pre-bundle cache stored and how do you clear it?

In `node_modules/.vite`. Vite rebuilds it when your lockfile, the relevant parts of `vite.config`, or `NODE_ENV` change. To force a rebuild:

```bash
vite --force
```

or delete the `node_modules/.vite` folder.

## 48: Does Vite support JSX?

Yes, `.jsx` and `.tsx` files are transformed with Oxc. For React you normally use `@vitejs/plugin-react`, which also adds Fast Refresh. For other JSX libraries you can configure the factory with the `oxc` option:

```js
export default defineConfig({
  oxc: {
    jsx: {
      runtime: "classic",
      pragma: "h",
      pragmaFrag: "Fragment",
    },
  },
});
```

## 49: Can you import JSON files in Vite?

Yes. You can import the whole object or a single field with a named import, which helps tree shaking.

```js
import pkg from "./package.json";
import { version } from "./package.json";
```

## 50: What does import.meta.glob do?

It imports many files that match a glob pattern. By default the imports are lazy (dynamic imports).

```js
const modules = import.meta.glob("./pages/*.js");
// { './pages/about.js': () => import('./pages/about.js'), ... }

for (const path in modules) {
  modules[path]().then((mod) => console.log(path, mod));
}
```

It is a Vite feature, not standard JavaScript. Vite turns it into normal imports at build time.

## 51: How do you import all files eagerly with import.meta.glob?

Pass `eager: true`. The modules are imported statically and you get the module objects directly.

```js
const modules = import.meta.glob("./locales/*.json", { eager: true });
// { './locales/en.json': { default: {...} }, ... }
```

Use it when you need all the files right away. Keep the lazy default when the files are big or not always needed.

## 52: What does the ?raw suffix do?

It imports the file content as a plain string.

```js
import shaderSource from "./shader.glsl?raw";
import readme from "./README.md?raw";
```

## 53: What does the ?url suffix do?

It gives you the URL of the file instead of its content. This is useful for files Vite would normally process in a different way, or files that are not in the default asset list.

```js
import workletUrl from "./audio-worklet.js?url";

await audioContext.audioWorklet.addModule(workletUrl);
```

## 54: How do you load a web worker in Vite?

The recommended way is the standard `new Worker(new URL(...))` syntax. Vite detects it and bundles the worker.

```js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
```

You can also use the `?worker` suffix:

```js
import MyWorker from "./worker.js?worker";

const worker = new MyWorker();
```

## 55: What is new URL(path, import.meta.url) used for in Vite?

It builds a URL to a static asset relative to the current module, using standard JavaScript. Vite detects this pattern at build time and rewrites the path to the final hashed asset.

```js
const imgUrl = new URL("./img.png", import.meta.url).href;
```

The path must be a static string (or a simple template string), otherwise Vite cannot find the file. This does not work in SSR.

## 56: How do you read the current mode inside vite.config?

Export a function instead of an object. It receives `command`, `mode`, `isSsrBuild` and `isPreview`.

```js
export default defineConfig(({ command, mode }) => {
  if (command === "serve") {
    return {/* dev config */};
  }
  return {/* build config */};
});
```

## 57: Can vite.config be async?

Yes. The config function can return a promise.

```js
export default defineConfig(async ({ mode }) => {
  const data = await loadSomething();
  return {
    define: { __DATA__: JSON.stringify(data) },
  };
});
```

## 58: How do you set up a proxy for API requests during development?

Use `server.proxy`. This is useful to avoid CORS problems when your API runs on a different port.

```js
export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8080",
        changeOrigin: true,
      },
    },
  },
});
```

Now `fetch('/api/users')` in the browser goes to `http://localhost:8080/api/users`. The proxy only works in dev (and `vite preview`), not in the production build.

## 59: How do you rewrite the path in a dev proxy?

Use the `rewrite` option:

```js
server: {
  proxy: {
    "/api": {
      target: "http://localhost:8080",
      changeOrigin: true,
      rewrite: (path) => path.replace(/^\/api/, ""),
    },
  },
},
```

`/api/users` becomes `http://localhost:8080/users`.

## 60: What does the define option do?

`define` replaces global identifiers with constant values at build time.

```js
export default defineConfig({
  define: {
    __APP_VERSION__: JSON.stringify("1.2.0"),
    __DEV_TOOLS__: false,
  },
});
```

```js
console.log(__APP_VERSION__); // "1.2.0"
```

Values must be valid JavaScript expressions, so wrap strings in `JSON.stringify`. In TypeScript, declare them in a `.d.ts` file: `declare const __APP_VERSION__: string`.

## 61: What does the build.sourcemap option do?

It decides whether the production build creates source maps. The default is `false`.

- `true`: creates separate `.map` files and adds a comment pointing to them
- `'inline'`: puts the source map inside the JS file as a data URL
- `'hidden'`: creates `.map` files but without the comment, useful for uploading to error tracking tools like Sentry

## 62: What is the default build target in Vite 8?

`'baseline-widely-available'`. This means browsers that are in the Baseline "widely available" list. In Vite 8 this is Chrome 111, Edge 111, Firefox 114 and Safari 16.4. You can change it:

```js
export default defineConfig({
  build: { target: "es2022" },
});
```

## 63: Does Vite add polyfills for older browsers?

No, not by default. Vite only transforms syntax down to the `build.target`. It does not add polyfills for APIs like `Promise.withResolvers`. For older browsers you can use `@vitejs/plugin-legacy`, which creates a legacy bundle with polyfills.

## 64: What does build.outDir do?

It sets the output folder. The default is `dist`, relative to the project root.

```js
export default defineConfig({
  build: { outDir: "build" },
});
```

## 65: What does build.emptyOutDir do?

It deletes the output folder before building. It is `true` by default when `outDir` is inside the root. If `outDir` is outside the root, Vite warns you and does not empty it unless you set it to `true`, to avoid deleting important files by accident.

## 66: What is build.assetsInlineLimit?

Imported assets smaller than this limit (default `4096` bytes, 4 KiB) are inlined as base64 data URLs instead of separate files. This saves HTTP requests for small icons.

```js
export default defineConfig({
  build: { assetsInlineLimit: 0 }, // never inline
});
```

You can also force it per import with `?inline` or `?no-inline`.

## 67: What file types does Vite treat as assets by default?

Common image, media and font types, for example `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`, `.avif`, `.ico`, `.mp4`, `.webm`, `.mp3`, `.wav`, `.woff`, `.woff2`, `.ttf`, `.otf`, `.pdf` and others. Importing one gives you its URL. You can add more types with `assetsInclude`:

```js
export default defineConfig({
  assetsInclude: ["**/*.gltf"],
});
```

## 68: How do you use an SVG file in Vite?

By default, importing an SVG gives you its URL:

```js
import iconUrl from "./icon.svg";
```

To get the SVG markup as a string, use `?raw`. To import it as a React or Vue component you need a plugin, for example `vite-plugin-svgr` for React or `vite-svg-loader` for Vue.

## 69: How do you lazy load a module in Vite?

Use a dynamic `import()`. Vite creates a separate chunk for it.

```js
button.addEventListener("click", async () => {
  const { openEditor } = await import("./editor.js");
  openEditor();
});
```

In React you combine it with `React.lazy`, in Vue with `defineAsyncComponent` or lazy routes.

## 70: What does the --port flag do and what is strictPort?

`vite --port 3000` sets the port. If it is taken, Vite tries the next one. If you set `server.strictPort: true`, Vite exits with an error instead, which is useful when another tool expects the app on an exact port.

## 71: How do you enable HTTPS on the dev server?

Pass an `https` object with a key and certificate:

```js
import fs from "node:fs";

export default defineConfig({
  server: {
    https: {
      key: fs.readFileSync("localhost-key.pem"),
      cert: fs.readFileSync("localhost.pem"),
    },
  },
});
```

For a quick self-signed certificate you can use `@vitejs/plugin-basic-ssl`. Tools like `mkcert` create certificates your browser trusts.

## 72: What is the difference between dependencies and source code in Vite's dev server?

Vite splits modules into two groups:

- **Dependencies** (from `node_modules`) rarely change. They are pre-bundled once and served with strong cache headers.
- **Source code** (your files) changes often. It is transformed on demand when the browser requests it, and Vite uses `304 Not Modified` checks so unchanged files are not sent again.

## 73: Can you use CommonJS packages with Vite?

Yes. In dev, CommonJS packages from `node_modules` are converted to ESM during pre-bundling. In production Rolldown handles CommonJS natively. Your own source code should be ESM, though. `require()` in source files is not supported in the browser.

## 74: What does vite build --watch do?

It rebuilds the project whenever a file changes, like a watch mode for production builds. This is useful for libraries or browser extensions where you need real build output, not the dev server.

```bash
vite build --watch
```

## 75: What is the difference between vite dev and vite build output?

`vite dev` does not write files to disk. It keeps everything in memory and serves modules one by one. `vite build` creates bundled, minified, hashed files in `dist` that you deploy. Code behavior should be the same, but things like env values (`DEV`/`PROD`), source maps and chunking are different.

## 76: How do you clear the terminal behavior or log level in Vite?

Use `logLevel` and `clearScreen`:

```js
export default defineConfig({
  logLevel: "warn", // 'info' | 'warn' | 'error' | 'silent'
  clearScreen: false, // keep previous logs, useful with other tools
});
```

Or on the command line: `vite --logLevel warn --clearScreen false`.

## 77: What is the cacheDir option?

It sets where Vite stores its cache, including pre-bundled deps. The default is `node_modules/.vite`. You might change it if `node_modules` is read-only, or to keep separate caches for different configs.

## 78: How do you add global SCSS variables to every component?

Use `css.preprocessorOptions` with `additionalData`:

```js
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/styles/variables" as *;`,
      },
    },
  },
});
```

This code is added to the top of every SCSS file. Only put variables and mixins here, not real CSS rules, or they will be repeated in every file.

## 79: Does Vite need a plugin for Vue single file components?

Yes, `.vue` files need `@vitejs/plugin-vue`. When you create a project with the `vue` template, it is already set up. The same is true for Svelte (`@sveltejs/vite-plugin-svelte`) and other frameworks with their own file formats.

## 80: How does a Vite React project start the app?

`index.html` loads `src/main.tsx`, which renders the root component:

```tsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./index.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

## 81: What is Vitest?

Vitest is a test runner built on top of Vite. It uses the same config, plugins and transforms as your app, so you don't need a separate Babel or ts-jest setup. Its API is mostly compatible with Jest (`describe`, `it`, `expect`, `vi.fn()`), and it has a fast watch mode.

## 82: How do you add Vitest to a Vite project?

```bash
npm add -D vitest
```

```ts
// vite.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "jsdom",
  },
});
```

```json
{ "scripts": { "test": "vitest" } }
```

You can also use a separate `vitest.config.ts`.

## 83: Which frameworks and meta-frameworks are built on Vite?

Many popular tools use Vite under the hood: Nuxt, SvelteKit, Astro, SolidStart, Qwik City, Remix and React Router (framework mode), TanStack Start, Analog (Angular), VitePress and Storybook (Vite builder). Angular CLI also uses Vite for its dev server.

## 84: What is VitePress?

VitePress is a static site generator built on Vite and Vue, made for documentation sites. You write Markdown and it builds a fast static site. The Vite docs themselves are made with VitePress.

## 85: How do you see what Vite is doing during a build or dev start?

Use `--debug` to print debug logs, or narrow them with a filter:

```bash
vite --debug
vite --debug hmr
vite build --debug
```

You can also use `--profile` to create a CPU profile of the startup or build.

## 86: How do you run Vite with a specific config file?

```bash
vite --config my-config.js
vite build -c configs/vite.prod.config.ts
```

By default Vite looks for `vite.config.*` in the current folder.

## 87: What does the server.hmr option do?

It configures the HMR connection. You can turn HMR off or change the WebSocket settings, for example when the dev server runs behind a proxy.

```js
export default defineConfig({
  server: {
    hmr: { overlay: false }, // no error overlay
  },
});
```

`server.hmr: false` disables HMR completely.

## 88: What is the error overlay?

When there is a compile or runtime error in dev, Vite shows a full screen overlay in the browser with the error message, the file and a code frame. Click it or fix the error to close it. You can disable it with `server.hmr.overlay: false`.

## 89: What does build.minify do?

It decides how JavaScript is minified. In Vite 8:

- `'oxc'` (default for client builds): uses the Oxc minifier
- `'terser'`: uses Terser (slower, you must install `terser`)
- `false`: no minification
- `'esbuild'`: deprecated, needs `esbuild` installed

SSR builds are not minified by default.

## 90: What does build.cssMinify do?

It controls CSS minification. The default in Vite 8 is `'lightningcss'`. You can set it to `false` to keep CSS readable, or to `'esbuild'` (deprecated). By default it follows `build.minify`: if JS minification is off for the client, CSS minification is off too.

## 91: What is Lightning CSS?

Lightning CSS is a fast CSS parser, transformer and minifier written in Rust. In Vite 8 it is the default CSS minifier and is installed with Vite. You can also use it instead of PostCSS for transforms like vendor prefixing and nesting:

```js
export default defineConfig({
  css: { transformer: "lightningcss" },
});
```

## 92: What does vite optimize do?

It was a CLI command to pre-bundle dependencies by hand. It is deprecated. Pre-bundling happens automatically when the dev server starts, and you can use `vite --force` to redo it.

## 93: How do you check which version of Vite you are using?

```bash
npx vite --version
```

In code you can import `version` from `vite`. In a plugin you can read `this.meta.viteVersion`.

## 94: What is the difference between vite and create-vite packages?

- `vite` is the build tool itself. It is a dev dependency of your project.
- `create-vite` is a scaffolding tool that creates a new project from a template. You run it once with `npm create vite@latest`.

## 95: How do you use Tailwind CSS with Vite?

For Tailwind CSS v4, use the official Vite plugin:

```bash
npm add -D tailwindcss @tailwindcss/vite
```

```js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

```css
/* src/index.css */
@import "tailwindcss";
```

Tailwind v3 used a PostCSS plugin instead.

## 96: What does the server.watch option do?

It passes options to the file watcher. For example, when files are on a network drive, in WSL2 with files on Windows, or inside some Docker setups, file events may not work and you need polling:

```js
export default defineConfig({
  server: {
    watch: { usePolling: true },
  },
});
```

Polling uses more CPU, so only turn it on if you need it.

## 97: What is the difference between root-relative and relative URLs in index.html?

Both work. `/src/main.ts` starts from the project root, `./src/main.ts` starts from the HTML file. Vite processes `<script type="module">`, `<link rel="stylesheet">`, `<img src>` and similar tags and rewrites them to the built files during the build.

## 98: Can a Vite app have more than one HTML page?

Yes. Add more HTML files and list them as inputs for the build:

```js
import { resolve } from "node:path";

export default defineConfig({
  build: {
    rolldownOptions: {
      input: {
        main: resolve(import.meta.dirname, "index.html"),
        admin: resolve(import.meta.dirname, "admin/index.html"),
      },
    },
  },
});
```

In dev, `/admin/` serves `admin/index.html` with no config.

## 99: What does vite build print at the end?

It prints a list of output files with their sizes and gzip sizes. Chunks over 500 kB (after minification) trigger a warning. You can change the limit with `build.chunkSizeWarningLimit`, and skip the gzip calculation with `build.reportCompressedSize: false` to make builds of large projects a bit faster.

## 100: How do you deploy a Vite app as a static site?

Run `vite build` and upload the `dist` folder to any static host: Netlify, Vercel, Cloudflare Pages, GitHub Pages, S3 with CloudFront, an Nginx server, and so on. For single page apps with client-side routing, configure the host to serve `index.html` for unknown paths. If the app is not at the domain root, set `base`.

## 101: How do you handle client-side routing on the dev server?

Nothing is needed. Vite's dev server already falls back to `index.html` for unknown paths when `appType` is `'spa'` (the default), so routes like `/users/42` work with React Router or Vue Router. The same is true for `vite preview`.

## 102: What is the appType option?

It tells Vite what kind of app it is serving:

- `'spa'` (default): adds the HTML fallback middleware for single page apps
- `'mpa'`: no SPA fallback, for multi-page apps
- `'custom'`: no HTML middlewares at all, used for SSR setups where your own server handles HTML

## 103: How do you import a file as a base64 data URL?

Use the `?inline` suffix:

```js
import iconDataUrl from "./icon.png?inline";
// "data:image/png;base64,..."
```

For CSS, `?inline` returns the processed CSS as a string and does not inject it into the page.

## 104: What is the env directory option?

`envDir` sets the folder Vite loads `.env` files from. By default it is the project root.

```js
export default defineConfig({
  envDir: "./config/env",
});
```

## 105: Can you use top-level await in Vite?

Yes, as long as your `build.target` supports it. The default target supports top-level await. If you set an older target like `es2020`, the build fails because top-level await cannot be transformed to older syntax.

## 106: How do you import a package that only has a default export in CommonJS?

You can usually write a normal default import, and Vite handles the interop:

```js
import dayjs from "dayjs";
```

In Vite 8 the rules for CJS default imports changed slightly. A default import gives you `module.exports` when the module is not marked with `__esModule`, and `module.exports.default` when it is.

## 107: What does the json option in vite.config do?

It controls how JSON imports are handled:

- `json.namedExports` (default `true`): allows named imports like `import { version } from './package.json'`
- `json.stringify` (default `'auto'`): large JSON files are exported as `JSON.parse("...")`, which is faster to parse than a JavaScript object literal

## 108: How does Vite handle .mjs, .cjs, .mts and .cts files?

They are all supported. `.mts` and `.cts` are TypeScript files, transformed like `.ts`. Note that browser code should still be ESM, so `.cjs` files in your source will only work if they are bundled (in production) or if a dependency is pre-bundled.

## 109: Can you import a module without the file extension?

Yes, Vite tries extensions from `resolve.extensions`. The default list is `['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json']`. Vue files are not in the list on purpose, so you should write `import App from './App.vue'` with the extension.

## 110: What happens when you save vite.config.ts during dev?

Vite notices the change and restarts the dev server automatically with the new config. You don't need to stop and start it by hand. The same happens when `.env` files change.

## 111: Which keyboard shortcuts are available in the Vite dev server terminal?

Press `h` + Enter to see them. The common ones:

- `r`: restart the server
- `u`: show the server URLs
- `o`: open in the browser
- `c`: clear the console
- `q`: quit

## 112: What is the purpose of the vite-env.d.ts file in templates?

It holds `/// <reference types="vite/client" />` so TypeScript knows about Vite-specific imports and `import.meta.env`. Without it, imports like `import logo from './logo.svg'` give a type error. Newer templates may put `vite/client` in `tsconfig.app.json` under `types` instead.

## 113: Why does the TypeScript template have several tsconfig files?

New templates usually have:

- `tsconfig.json`: the root file that only has `references` to the others
- `tsconfig.app.json`: settings for your app code in `src` (browser)
- `tsconfig.node.json`: settings for `vite.config.ts` (Node.js)

App code and config code run in different environments and need different `lib` and `types` settings, so they are split.

## 114: How do you import a CSS file without applying it, just to get the text?

Use `?inline`:

```js
import css from "./theme.css?inline";

const sheet = new CSSStyleSheet();
sheet.replaceSync(css);
document.adoptedStyleSheets = [sheet];
```

This is handy for web components with Shadow DOM.

## 115: What are the CSS source maps in dev?

By default Vite does not create CSS source maps in dev to keep it fast. You can turn them on:

```js
export default defineConfig({
  css: { devSourcemap: true },
});
```

Then DevTools shows the original `.scss` file and line for each rule.

## 116: What is the difference between npm run dev and npx vite?

They do the same if the `dev` script is just `vite`. `npm run dev` runs whatever is in the script, which may include flags (like `vite --host`) or other tools. `npx vite` runs the locally installed Vite binary directly.

## 117: How do you change the host name allowed by the dev server?

Use `server.allowedHosts`. By default Vite only accepts requests with `localhost`, IP addresses and some local host names in the `Host` header. This protects you from DNS rebinding attacks. If you use a custom domain or a tunnel:

```js
export default defineConfig({
  server: {
    allowedHosts: ["myapp.local", ".ngrok-free.app"],
  },
});
```

A value starting with a dot allows all subdomains.

## 118: Does Vite work with monorepos?

Yes. Vite works well with pnpm, npm and yarn workspaces. Linked packages (not inside `node_modules`) are treated as source code, so they get HMR and are not pre-bundled. Vite also detects the workspace root, so it can serve files from it.

## 119: How do you exclude a dependency from pre-bundling?

```js
export default defineConfig({
  optimizeDeps: {
    exclude: ["my-esm-lib"],
  },
});
```

Only do this for packages that are already proper ESM with few internal files. If an excluded package has CommonJS dependencies, you usually need to `include` those.

## 120: How do you force a dependency to be pre-bundled?

Add it to `optimizeDeps.include`. This is useful when Vite's import scan does not find a dependency, for example when it is imported only by code that a plugin creates, or for deep imports.

```js
export default defineConfig({
  optimizeDeps: {
    include: ["lodash-es", "some-lib/sub-path"],
  },
});
```

## 121: Can Vite build a library instead of an app?

Yes, with library mode:

```js
import { resolve } from "node:path";

export default defineConfig({
  build: {
    lib: {
      entry: resolve(import.meta.dirname, "src/index.ts"),
      name: "MyLib",
      fileName: "my-lib",
    },
  },
});
```

The entry is a JS/TS file instead of `index.html`. By default it outputs `es` and `umd` formats (or `es` and `cjs` when there are several entries).

## 122: What is a chunk?

A chunk is one JavaScript output file. The bundler splits code into chunks: an entry chunk, chunks for dynamic imports, and shared chunks for code used by several of them. Smaller chunks mean the browser downloads only what a page needs.

## 123: Why do built file names contain a hash?

The hash (like `index-B2xF9kLz.js`) is based on the file content. When content changes, the name changes. This lets you cache these files forever on a CDN (`Cache-Control: max-age=31536000, immutable`), because a new version always has a new name. Only `index.html` needs a short cache.

## 124: What does vite build --emptyOutDir false do?

It keeps existing files in the output folder instead of deleting them before the build. For example, when two builds write to the same folder.

## 125: How do you pass a different config for the preview server?

Use the `preview` options. They default to the `server` options where it makes sense.

```js
export default defineConfig({
  preview: {
    port: 8080,
    open: true,
  },
});
```

## 126: How do you import a WebAssembly file?

Use the `?init` suffix. You get a function that instantiates the module:

```js
import init from "./example.wasm?init";

const instance = await init({ imports: {} });
instance.exports.test();
```

Since Vite 8 this also works in SSR, and Vite 8.1 adds support for importing `.wasm` files directly following the WebAssembly ESM integration proposal.

## 127: What is the difference between import.meta.env.PROD and checking mode === 'production'?

`PROD` is `true` whenever the app runs in production (`NODE_ENV=production`), even with a custom mode like `staging`. `MODE` is the mode name. So `vite build --mode staging` gives `PROD === true` and `MODE === 'staging'`.

## 128: Are env variables replaced at build time or read at runtime?

At build time. Vite replaces `import.meta.env.VITE_X` with the literal value when it builds. If you change the value, you must rebuild. If you need runtime config (one build for many environments), load a JSON file or read values injected into `index.html` by your server.

## 129: How do you use a variable from .env inside index.html?

Use `%VAR_NAME%` syntax:

```html
<title>%VITE_APP_TITLE%</title>
```

Only variables exposed to the client (with the `VITE_` prefix) and the built-in ones like `%MODE%` work. A missing variable is left as is in the HTML.

## 130: What is the role of plugin order?

Plugins run in the order they are in the `plugins` array, grouped by their `enforce` value (`'pre'`, normal, `'post'`). Some plugins must run before others, for example a plugin that transforms a custom file type into JS must run before plugins that handle JS. Plugin docs usually say if order matters.

## 131: Can you use a Rollup plugin in Vite?

Most of the time, yes. Vite's plugin API extends Rollup's, and Rolldown supports the same hooks. Rollup plugins that don't depend on Rollup-only behavior work in Vite 8 without changes. Some hooks are not supported in Rolldown (for example `shouldTransformCachedModule` and `resolveFileUrl`), so plugins that use them may break.

## 132: How do you apply a plugin only during build?

Set `apply: 'build'` (or `'serve'` for dev only):

```js
import { visualizer } from "rollup-plugin-visualizer";

export default defineConfig({
  plugins: [{ ...visualizer(), apply: "build" }],
});
```

## 133: How do you see the size of each dependency in your bundle?

Use a bundle analyzer plugin, for example `rollup-plugin-visualizer`, which creates an HTML treemap after `vite build`. Vite 8 also has Vite Devtools (the `devtools` option) for looking at the module graph and build output.

## 134: What is build.cssCodeSplit?

When `true` (default), CSS imported by an async chunk is put in its own CSS file and loaded together with that chunk. When `false`, all CSS is merged into one file. One CSS file can be simpler but means users download styles for pages they may never visit.

## 135: What does build.copyPublicDir do?

It decides whether files in `public` are copied to `outDir`. The default is `true`. You can turn it off, for example in library mode where you don't want public files in the package.

## 136: How do you change the public folder location?

Use `publicDir`:

```js
export default defineConfig({
  publicDir: "static",
});
```

Set it to `false` to turn the feature off.

## 137: How do you know if code runs in the dev server or in the build output?

Use `import.meta.env.DEV` or `import.meta.env.PROD`. Since these are replaced with literal booleans, code inside `if (import.meta.env.DEV) { ... }` is removed from the production bundle by tree shaking.

## 138: Can you use process.env in Vite client code?

Not by default. `process` is a Node.js global and does not exist in the browser. Use `import.meta.env` instead. Vite does replace `process.env.NODE_ENV` in library dependencies, since many packages check it. If an old library uses other `process.env` values, you can add them with `define`.

## 139: What is the difference between server.open and the o shortcut?

Both open the app in the browser. `server.open` does it once when the server starts. Pressing `o` + Enter in the terminal does it whenever you want.

## 140: Where do framework plugins like plugin-vue fit in the Vite plugin pipeline?

They are normal Vite plugins. For example, `plugin-vue` uses the `transform` hook to compile `.vue` files into JavaScript and CSS modules, and the HMR hooks to update components without a reload. After that, Vite's core plugins handle the result like any other JS file.

## 141: What is the server.headers option?

It adds HTTP headers to every response from the dev server:

```js
export default defineConfig({
  server: {
    headers: {
      "Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy": "require-corp",
    },
  },
});
```

These two headers, for example, are needed to use `SharedArrayBuffer`.

## 142: How do you use React Router or Vue Router with lazy loaded routes in Vite?

Use dynamic imports in route definitions. Vite creates one chunk per route.

```js
// Vue Router
const routes = [
  { path: "/", component: () => import("./pages/Home.vue") },
  { path: "/about", component: () => import("./pages/About.vue") },
];
```

## 143: How does Vite handle fonts?

Fonts referenced in CSS with `url()` are treated as assets: they are copied to `dist/assets` with a hash, and the URL in the CSS is rewritten. Small fonts can be inlined as base64 if they are under `assetsInlineLimit`, but `.woff2` files are usually bigger than 4 KiB.

## 144: What does the resolve.extensions option do?

It lists the extensions Vite tries when an import has none. Changing it is rarely needed, and adding too many extensions can slow down resolving. It is better to write the extension in imports for non-standard files.

## 145: Can you use Vite without a framework?

Yes. The `vanilla` and `vanilla-ts` templates have no framework. You get the dev server, HMR for CSS, TypeScript support, asset handling and the production build. This works well for small sites, prototypes, and libraries.

## 146: What happens if you import a file that doesn't exist?

In dev, you get an error in the terminal and the error overlay in the browser (`Failed to resolve import ...`). In the build, it is a build error. This is one of the reasons to import assets instead of putting them in `public`, since public files are never checked.

## 147: How do you add a favicon to a Vite app?

Put the file in `public` and reference it with an absolute path in `index.html`:

```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
```

You can also keep it in `src` and use a relative path, then Vite hashes it like other assets.

## 148: Does Vite support CSS nesting?

Yes, native CSS nesting is supported by modern browsers and passes through as is. If your `build.cssTarget` includes older browsers, Lightning CSS (when used as the transformer) or the `postcss-nesting` plugin can lower it. Sass and Less have their own nesting too.

## 149: What does the --mode flag do with vite preview?

`vite preview` does not build anything, so `--mode` only affects which config is loaded (for example, if your config function checks `mode`). The values inside the built files were set during `vite build`.

## 150: Where can you find Vite plugins?

- The official docs list official plugins
- The community list `awesome-vite` on GitHub
- npm, by searching for `vite-plugin`

Many Rollup plugins also work with Vite.

# Moderate Questions (151-300)

## 151: How do you read env variables inside vite.config?

`.env` files are not loaded into `process.env` when the config runs, because Vite needs the config to know which `envDir` and mode to use. Use `loadEnv`:

```ts
import { defineConfig, loadEnv } from "vite";

export default defineConfig(({ mode }) => {
  // third argument '' loads all variables, not only VITE_ ones
  const env = loadEnv(mode, process.cwd(), "");

  return {
    server: { port: Number(env.PORT) || 5173 },
    define: { __API__: JSON.stringify(env.API_URL) },
  };
});
```

## 152: How does the HMR API work in plain JavaScript?

A module can accept its own updates with `import.meta.hot.accept`. Always wrap HMR code in `if (import.meta.hot)` so it is removed in production.

```js
export let count = 0;

if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    if (newModule) {
      console.log("updated, new count:", newModule.count);
    }
  });
}
```

`newModule` is `undefined` if the new version had a syntax error.

## 153: How do you accept updates from a dependency module?

Pass the path of the dependency (or an array of paths) to `accept`:

```js
import { render } from "./render.js";

render();

if (import.meta.hot) {
  import.meta.hot.accept("./render.js", (newRender) => {
    newRender?.render();
  });
}
```

Now edits to `render.js` don't reload the page. This module handles them.

## 154: What is import.meta.hot.dispose used for?

It runs cleanup before the module is replaced, for example removing event listeners or timers the old version created. Without it, you get duplicate listeners after each update.

```js
const id = setInterval(tick, 1000);

if (import.meta.hot) {
  import.meta.hot.dispose(() => {
    clearInterval(id);
  });
}
```

## 155: How do you keep state between HMR updates with import.meta.hot.data?

`import.meta.hot.data` is an object that stays the same across versions of the same module. Save values in `dispose` and read them in the new version.

```js
let count = import.meta.hot?.data.count ?? 0;

if (import.meta.hot) {
  import.meta.hot.dispose((data) => {
    data.count = count;
  });
  import.meta.hot.accept();
}
```

Mutate properties of `data`. Don't assign a new object to `import.meta.hot.data` itself.

## 156: What does import.meta.hot.invalidate do?

It tells Vite that this module cannot handle the update after all, so the update moves up to its importers (and may end in a full reload). It is used inside an `accept` callback when you find out the change is not safe to apply.

```js
import.meta.hot.accept((mod) => {
  if (cannotHandle(mod)) {
    import.meta.hot.invalidate("exports changed");
  }
});
```

## 157: What does import.meta.hot.prune do?

It registers a callback that runs when the module is no longer imported on the page, for example after you remove an import. Vite uses it to remove styles of CSS files that are no longer used. Your own modules can use it to clean up side effects.

## 158: Why must import.meta.hot calls be written in a specific form?

Vite finds HMR code with static analysis. It looks for `import.meta.hot.accept(` written directly. If you alias it, like `const hot = import.meta.hot; hot.accept()`, Vite does not see it and the module is not treated as an HMR boundary. The guard `if (import.meta.hot)` is fine.

## 159: How do you listen to HMR events like a full reload or an error?

Use `import.meta.hot.on`:

```js
if (import.meta.hot) {
  import.meta.hot.on("vite:beforeUpdate", (payload) => {
    console.log("updating", payload.updates);
  });
  import.meta.hot.on("vite:beforeFullReload", () => {
    saveDraft();
  });
  import.meta.hot.on("vite:error", (err) => console.error(err));
}
```

Other events include `vite:afterUpdate`, `vite:beforePrune`, `vite:invalidate`, `vite:ws:connect` and `vite:ws:disconnect`.

## 160: How does React Fast Refresh work with Vite and what breaks it?

`@vitejs/plugin-react` adds Fast Refresh code to modules that export React components. When such a file changes, only the components are replaced and their state is kept. It falls back to a full reload when a file exports both components and non-component values (like constants or functions), because those exports can't be updated safely. The ESLint rule `react-refresh/only-export-components` warns you about this.

## 161: How do you split vendor code into its own chunk in Vite 8?

Use Rolldown's `codeSplitting` option with groups:

```js
export default defineConfig({
  build: {
    rolldownOptions: {
      output: {
        codeSplitting: {
          groups: [
            {
              name: "react-vendor",
              test: /node_modules[\\/]react/,
              priority: 20,
            },
            { name: "vendor", test: /node_modules/, priority: 10 },
          ],
        },
      },
    },
  },
});
```

When groups overlap, the one with the higher `priority` wins.

## 162: What happened to manualChunks in Vite 8?

`build.rollupOptions.output.manualChunks` came from Rollup. In Vite 8 the object form is removed and the function form is deprecated. The replacement is Rolldown's `output.codeSplitting` option, which supports groups with `test`, `priority`, `minSize`, `maxSize` and `minShareCount`. In Vite 7 and earlier you will still see code like this:

```js
// legacy (Vite 7 and older)
manualChunks(id) {
  if (id.includes("node_modules")) return "vendor";
}
```

## 163: What is build.rolldownOptions and how does it relate to build.rollupOptions?

`build.rolldownOptions` passes options directly to Rolldown, for example `input`, `external`, `output`, `plugins`. In Vite 8 `build.rollupOptions` is a deprecated alias for it, so old configs still work. New code should use `rolldownOptions`.

## 164: What is the oxc option and how does it relate to the esbuild option?

The `oxc` option configures the Oxc transformer used for TS and JSX files: `include`, `exclude`, `jsx`, `jsxInject`, `define` and others. In Vite 8 the old `esbuild` option is deprecated and converted to `oxc` automatically. Some esbuild options have no Oxc version, for example `esbuild.banner`/`footer` (use a plugin) and `esbuild.supported`.

```js
export default defineConfig({
  oxc: {
    jsxInject: `import React from 'react'`,
  },
});
```

## 165: How do you build a library with several entry points?

Pass an object to `build.lib.entry`:

```js
export default defineConfig({
  build: {
    lib: {
      entry: {
        index: resolve(import.meta.dirname, "src/index.ts"),
        utils: resolve(import.meta.dirname, "src/utils.ts"),
      },
      formats: ["es", "cjs"],
    },
  },
});
```

UMD and IIFE formats only work with a single entry.

## 166: How do you keep React out of your library bundle?

Mark it as external, so the consumer's app provides it:

```js
export default defineConfig({
  build: {
    lib: { entry: "src/index.ts", formats: ["es"] },
    rolldownOptions: {
      external: ["react", "react-dom", "react/jsx-runtime"],
    },
  },
});
```

Also list React in `peerDependencies` of your `package.json`. Otherwise the app may end up with two copies of React, which breaks hooks.

## 167: How should package.json look for a library built with Vite?

```json
{
  "name": "my-lib",
  "type": "module",
  "files": ["dist"],
  "main": "./dist/my-lib.umd.cjs",
  "module": "./dist/my-lib.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/my-lib.js",
      "require": "./dist/my-lib.umd.cjs"
    },
    "./style.css": "./dist/my-lib.css"
  }
}
```

`exports` is what modern tools use. `main` and `module` are fallbacks for older tools.

## 168: How do you generate .d.ts files for a library built with Vite?

Vite does not create type declarations. Options:

- run `tsc --emitDeclarationOnly` as a separate step
- use a plugin like `vite-plugin-dts` or `unplugin-dts`

```json
{
  "scripts": {
    "build": "vite build && tsc -p tsconfig.build.json --emitDeclarationOnly"
  }
}
```

## 169: How does CSS work in library mode?

All CSS imported by the library is extracted into one CSS file in `dist`. Users must import it themselves (`import 'my-lib/style.css'`). You can set its name with `build.lib.cssFileName`. If you want CSS to be injected automatically, you need a plugin, or use CSS-in-JS, but many teams prefer the separate file because it is simple and works with SSR.

## 170: What is @vitejs/plugin-legacy and how does it work?

It adds support for old browsers that don't support native ESM or modern syntax.

```js
import legacy from "@vitejs/plugin-legacy";

export default defineConfig({
  plugins: [legacy({ targets: ["defaults", "not IE 11"] })],
});
```

It creates a second set of chunks transformed with Babel and polyfills from core-js, loaded with `<script nomodule>`. Modern browsers load the normal ESM build and ignore the legacy one. It makes the build slower and bigger, so only use it if you really need old browsers. Transforming to ES5 or lower is not supported with Vite 8.

## 171: How do you set a relative base so the build works from any folder?

Use `base: './'` (or an empty string). All asset URLs become relative, so you can open the build from any sub-path, or even from a file inside an Electron app.

```js
export default defineConfig({
  base: "./",
});
```

It does not work well with client-side routing on nested URLs, because relative paths change with the URL.

## 172: What is the build manifest and when do you need it?

With `build.manifest: true`, Vite writes `.vite/manifest.json` in `outDir`. It maps each source entry to its built files, CSS and imported chunks.

```json
{
  "src/main.ts": {
    "file": "assets/main-4Bx2.js",
    "src": "src/main.ts",
    "isEntry": true,
    "css": ["assets/main-a8Qk.css"],
    "imports": ["_shared-Bf9c.js"]
  }
}
```

You need it when a backend (Laravel, Rails, Django) renders the HTML instead of Vite. The backend reads the manifest to output the correct `<script>` and `<link>` tags.

## 173: How do you use Vite with a traditional backend like Laravel or Django?

1. Set `build.manifest: true` and set your entry with `build.rolldownOptions.input` (a JS file, not HTML).
2. In dev, the backend template adds the Vite client and your entry from the dev server:

```html
<script type="module" src="http://localhost:5173/@vite/client"></script>
<script type="module" src="http://localhost:5173/src/main.js"></script>
```

3. In production, the backend reads `manifest.json` and outputs the hashed file names.

Laravel has an official plugin (`laravel-vite-plugin`) that does this. Also set `server.origin` or `server.cors` so assets load correctly from the dev server.

## 174: What does build.modulePreload do?

Vite adds `<link rel="modulepreload">` for chunks the entry imports, and for dynamic imports it preloads the chunk's dependencies in parallel with the chunk. This avoids request waterfalls. The default `{ polyfill: true }` adds a small polyfill for browsers without `modulepreload`. You can turn it off or filter dependencies with `resolveDependencies`.

## 175: What is the vite:preloadError event?

When a dynamic import fails to load (often after a new deployment removed old chunk files), Vite fires `vite:preloadError` on `window`. You can catch it and reload the page so the user gets the new version.

```js
window.addEventListener("vite:preloadError", (event) => {
  event.preventDefault(); // stop the error from being thrown
  window.location.reload();
});
```

Keeping old chunk files on the server for a while after a deploy also helps.

## 176: How do you import files with a query using import.meta.glob?

Use the `query` and `import` options:

```js
// all SVGs as raw strings
const icons = import.meta.glob("./icons/*.svg", {
  query: "?raw",
  import: "default",
  eager: true,
});
```

`import: 'default'` gives you the default export directly instead of the module object. The old `as: 'raw'` option was removed.

## 177: What rules apply to import.meta.glob patterns?

- They must be string literals. You can't use variables.
- They must be relative (`./`), absolute from the root (`/`), or alias paths.
- You can pass an array, and use `!` for negative patterns: `import.meta.glob(['./dir/*.js', '!**/bar.js'])`.
- The `base` option changes the base folder for the result keys.
- Since Vite 8.1, `caseSensitive: false` matches files regardless of letter case.

## 178: How do dynamic imports with variables work in Vite?

Vite supports dynamic imports with template strings in some cases:

```js
const module = await import(`./locales/${lang}.js`);
```

Rules: the path must start with `./` or `../`, must have a file extension, and the variable can only be one level (it cannot contain a `/`). Vite turns it into a glob import behind the scenes. For more complex cases, use `import.meta.glob` yourself.

## 179: How do you configure CSS Modules class names?

Use `css.modules`:

```js
export default defineConfig({
  css: {
    modules: {
      localsConvention: "camelCaseOnly", // .btn-primary -> styles.btnPrimary
      generateScopedName: "[name]__[local]___[hash:base64:5]",
    },
  },
});
```

When `css.transformer` is `'lightningcss'`, you configure CSS Modules with `css.lightningcss.cssModules` instead.

## 180: How does Vite handle url() and @import in CSS?

`url()` paths are resolved like JS imports: relative files are processed as assets and get hashed names, and aliases work too. `@import` statements are inlined by Vite (it uses `postcss-import` internally for plain CSS, or the preprocessor's own system for Sass/Less). Aliases also work in `@import`.

## 181: Which Sass API does Vite use?

Vite 7 and later only support the modern Sass API (`sass` or `sass-embedded`). The legacy API was removed. `sass-embedded` is faster, and Vite uses it if it is installed. If an old config had `api: 'legacy'` under `css.preprocessorOptions.scss`, you have to remove it and migrate deprecated features like `@import` to `@use`.

## 182: When would you switch css.transformer to lightningcss?

When you want faster CSS processing and don't need PostCSS plugins. Lightning CSS handles vendor prefixes, nesting, and lowering modern syntax based on your targets. You lose custom PostCSS plugins (for example, Tailwind v3's PostCSS plugin). Vite 8.1 added `@import` of external files and file dependencies for plugins, and the team is thinking about making it the default in the next major.

## 183: What is server.warmup?

It tells the dev server to transform some files in advance, before the browser asks for them. This helps when the first page load is slow because of a long chain of imports.

```js
export default defineConfig({
  server: {
    warmup: {
      clientFiles: ["./src/components/BigComponent.vue", "./src/utils/*.js"],
    },
  },
});
```

Only add files that are used often, or you make startup slower.

## 184: What do server.fs.allow and server.fs.deny do?

They control which files the dev server can serve with `/@fs/` URLs.

- `fs.strict` (default `true`) blocks files outside the allowed list.
- `fs.allow` lists allowed folders. By default it is the workspace root.
- `fs.deny` blocks sensitive files. The default list includes `.env`, `.env.*`, certificate files like `*.pem`, `.npmrc` and `.git` folders.

```js
server: {
  fs: { allow: [searchForWorkspaceRoot(process.cwd()), "../shared-assets"] },
},
```

## 185: What does optimizeDeps.entries do?

By default Vite scans all HTML files in the project to find dependencies to pre-bundle. `entries` sets other files to start from. It is useful when your entry is not HTML (backend integration) or when scanning picks up files it shouldn't.

```js
optimizeDeps: {
  entries: ["src/main.ts", "src/admin/main.ts"],
},
```

## 186: What is the "new dependencies optimized, reloading page" message?

If Vite finds a new dependency while you browse (for example a lazy loaded route imports a package the first scan missed), it has to pre-bundle again and reload the page. On a big project this can happen several times. To avoid it, add those packages to `optimizeDeps.include` so they are bundled at startup.

## 187: How do you fix two copies of the same package (like React) in a monorepo?

Use `resolve.dedupe` so all imports of the package resolve to the copy in the project root:

```js
export default defineConfig({
  resolve: {
    dedupe: ["react", "react-dom"],
  },
});
```

Two copies of React break hooks (`Invalid hook call`), and two copies of Vue break `provide`/`inject`.

## 188: What are resolve.conditions and resolve.mainFields?

- `resolve.conditions` lists extra conditions used when reading the `exports` field of `package.json` (for example `'development'`, `'browser'`, or custom ones).
- `resolve.mainFields` is the list of fields to try when a package has no `exports`, like `['browser', 'module', 'jsnext:main', 'jsnext']`.

You change them when a package publishes special builds, for example a custom `source` condition for linked monorepo packages.

## 189: How do you proxy WebSocket connections in the dev server?

Set `ws: true`:

```js
server: {
  proxy: {
    "/socket.io": {
      target: "ws://localhost:3000",
      ws: true,
    },
  },
},
```

## 190: How do you access the underlying proxy instance to add logging or headers?

Use the `configure` callback. It receives the `http-proxy` instance:

```js
server: {
  proxy: {
    "/api": {
      target: "http://localhost:8080",
      changeOrigin: true,
      configure: (proxy) => {
        proxy.on("proxyReq", (proxyReq, req) => {
          proxyReq.setHeader("x-dev-user", "test");
          console.log("proxy", req.method, req.url);
        });
      },
    },
  },
},
```

## 191: How do you change the env variable prefix?

```js
export default defineConfig({
  envPrefix: ["VITE_", "PUBLIC_"],
});
```

Never set it to `''`. Vite refuses that, because it would expose every variable, including secrets, to the client.

## 192: How do you configure web workers in the build?

Use the `worker` options:

```js
export default defineConfig({
  worker: {
    format: "es", // 'es' or 'iife' (default)
    plugins: () => [someWorkerPlugin()],
    rolldownOptions: {/* ... */},
  },
});
```

Use `format: 'es'` if your worker uses code splitting or dynamic imports. Worker plugins are separate from main plugins, so add what the worker needs there.

## 193: How do you use shared workers or inline workers?

With query suffixes:

```js
import MySharedWorker from "./shared.js?sharedworker";
import InlineWorker from "./worker.js?worker&inline";

const shared = new MySharedWorker();
const inline = new InlineWorker(); // worker code inlined as base64
```

Inline workers avoid a separate request, which can help in library mode.

## 194: How do you set up the React Compiler with Vite?

With `@vitejs/plugin-react` v6, Babel is no longer included, so you add `@rolldown/plugin-babel` and use the `reactCompilerPreset` helper:

```bash
npm add -D @rolldown/plugin-babel @babel/core babel-plugin-react-compiler
```

```js
import { defineConfig } from "vite";
import react, { reactCompilerPreset } from "@vitejs/plugin-react";
import babel from "@rolldown/plugin-babel";

export default defineConfig({
  plugins: [react(), babel({ presets: [reactCompilerPreset()] })],
});
```

In plugin-react v5 you passed `babel: { plugins: ['babel-plugin-react-compiler'] }` to `react()`.

## 195: How do you debug a slow Vite dev server?

- Run `vite --profile`, open the app, then press `p` + Enter to save a `.cpuprofile`, and open it in a tool like speedscope.
- Run `vite --debug plugin-transform` to see how long each plugin takes per file.
- Use `vite-plugin-inspect` or Vite Devtools to see the transform result of each plugin.
- Check for barrel files that import hundreds of modules, plugins that do heavy work on every file, and missing `server.warmup`.

## 196: What is vite-plugin-inspect?

A plugin that adds a page (`/__inspect/`) to the dev server. It shows each module, the plugins that transformed it, the code after every step, and how long each step took. It is very useful for debugging plugins or slow transforms.

## 197: Why are barrel files bad for Vite dev performance?

A barrel file (`index.ts` that re-exports everything) means importing one thing makes the browser load every file the barrel re-exports. In dev Vite does not bundle source code, so this can be hundreds of requests and transforms. Import directly from the file you need (`./utils/slugify` instead of `./utils`) to load fewer modules.

## 198: How do you run the dev server inside Docker with working HMR?

```js
export default defineConfig({
  server: {
    host: true, // listen on 0.0.0.0 in the container
    port: 5173,
    strictPort: true,
    watch: { usePolling: true }, // only if file events don't work
  },
});
```

Map the port with `-p 5173:5173`. If the browser reaches the server through another port or host, set `server.hmr.clientPort` (or `hmr.host`) so the HMR WebSocket connects to the right place.

## 199: Why doesn't HMR work behind a reverse proxy, and how do you fix it?

The browser opens the HMR WebSocket using the page's host and port, but Vite listens on its own port. If the proxy does not forward WebSocket upgrades, or uses a different port, the connection fails. Fixes:

- enable WebSocket forwarding in the proxy (Nginx: `proxy_set_header Upgrade` and `Connection`)
- set `server.hmr.clientPort` to the port the browser uses (for example 443)
- set `server.hmr.path` if the proxy routes by path

## 200: How do you configure Vitest separately from the app config while sharing settings?

Use `mergeConfig` with your Vite config:

```ts
// vitest.config.ts
import { defineConfig, mergeConfig } from "vitest/config";
import viteConfig from "./vite.config";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      environment: "jsdom",
      setupFiles: ["./src/test-setup.ts"],
    },
  }),
);
```

If `vite.config` exports a function, call it first, or use `defineConfig((env) => mergeConfig(viteConfig(env), ...))`.

## 201: How does server-side rendering (SSR) work with Vite at a high level?

A typical Vite SSR app has:

- `index.html` with a placeholder like `<!--app-html-->`
- `src/entry-client.ts` that hydrates the app in the browser
- `src/entry-server.ts` that exports a `render()` function
- a Node server (Express, Fastify, Hono...) that loads `entry-server`, calls `render(url)`, puts the HTML in the template and sends it

In dev, the server runs Vite in middleware mode so it can load `entry-server` with HMR. In production you build the client and the server separately and the server imports the built files. Most people use a framework (Nuxt, SvelteKit, React Router, TanStack Start) instead of setting this up by hand.

## 202: How do you use Vite in middleware mode with Express?

```js
import express from "express";
import fs from "node:fs/promises";
import { createServer as createViteServer } from "vite";

const app = express();
const vite = await createViteServer({
  server: { middlewareMode: true },
  appType: "custom",
});

app.use(vite.middlewares);

app.use("*all", async (req, res, next) => {
  try {
    const url = req.originalUrl;
    let template = await fs.readFile("index.html", "utf-8");
    template = await vite.transformIndexHtml(url, template);
    const { render } = await vite.ssrLoadModule("/src/entry-server.ts");
    const html = template.replace("<!--app-html-->", await render(url));
    res.status(200).set({ "Content-Type": "text/html" }).end(html);
  } catch (e) {
    vite.ssrFixStacktrace(e);
    next(e);
  }
});

app.listen(5173);
```

`ssrLoadModule` is the older API. The Environment API offers a module runner (`createServerModuleRunner`) as the newer way, but `ssrLoadModule` is still widely used.

## 203: How do you build an SSR app for production?

Run two builds:

```json
{
  "scripts": {
    "build:client": "vite build --outDir dist/client",
    "build:server": "vite build --ssr src/entry-server.ts --outDir dist/server"
  }
}
```

The `--ssr` flag builds for Node: no minification by default, dependencies stay external, and `import.meta.env.SSR` is `true`. In production your server reads `dist/client/index.html` and imports `dist/server/entry-server.js`.

## 204: What do ssr.external and ssr.noExternal do?

In SSR builds, Vite keeps dependencies from `node_modules` external by default. Node loads them at runtime instead of bundling them.

- `ssr.noExternal`: force some packages to be bundled. Needed for packages that ship CSS, use Vite-specific features, or are ESM-only in ways Node can't load.
- `ssr.external`: force linked packages (not in `node_modules`) to stay external.

```js
export default defineConfig({
  ssr: {
    noExternal: ["some-ui-lib"],
  },
});
```

Setting `noExternal: true` bundles everything, which is useful for platforms like edge workers.

## 205: What is the SSR manifest?

With `vite build --ssrManifest`, Vite writes `.vite/ssr-manifest.json` that maps each module ID to the chunks and assets it uses. During rendering you track which modules were used for this page (for example Vue's `ctx.modules`) and use the manifest to add `<link rel="modulepreload">` tags for exactly those chunks. This avoids loading waterfalls after hydration.

## 206: How do you write a simple Vite plugin?

A plugin is an object with a `name` and some hooks. Usually you export a function that returns it, so users can pass options.

```js
export default function bannerPlugin(text) {
  return {
    name: "banner",
    transform(code, id) {
      if (!id.endsWith(".js")) return null;
      return { code: `/* ${text} */\n${code}`, map: null };
    },
  };
}
```

```js
plugins: [bannerPlugin("My app")],
```

Returning `null` means "I don't handle this file".

## 207: What are the universal hooks a Vite plugin can use?

These come from the Rollup/Rolldown API and run in both dev and build:

- `options`, `buildStart`, `buildEnd`, `closeBundle`: start and end of the process
- `resolveId`: decide what file an import points to
- `load`: return the content of a module
- `transform`: change the code of a module

Build-only output hooks like `renderChunk` and `generateBundle` only run during `vite build`.

## 208: What are Vite-specific plugin hooks?

- `config`: change the config before it is resolved (return a partial config to merge)
- `configResolved`: read the final config
- `configureServer`: add middlewares to the dev server
- `configurePreviewServer`: same for the preview server
- `transformIndexHtml`: change `index.html`
- `handleHotUpdate`: customize HMR (the Environment API version is `hotUpdate`)

## 209: How do you create a virtual module?

Use `resolveId` and `load`. By convention user code imports it with a `virtual:` prefix and the resolved ID starts with `\0`, so other plugins skip it.

```js
export default function versionPlugin() {
  const id = "virtual:app-info";
  const resolvedId = "\0" + id;

  return {
    name: "app-info",
    resolveId(source) {
      if (source === id) return resolvedId;
    },
    load(loadId) {
      if (loadId === resolvedId) {
        return `export const builtAt = ${JSON.stringify(new Date().toISOString())}`;
      }
    },
  };
}
```

```js
import { builtAt } from "virtual:app-info";
```

## 210: How do you add a middleware to the dev server from a plugin?

Use `configureServer`:

```js
const mockApi = () => ({
  name: "mock-api",
  configureServer(server) {
    server.middlewares.use("/api/health", (req, res) => {
      res.setHeader("Content-Type", "application/json");
      res.end(JSON.stringify({ ok: true }));
    });
  },
});
```

Middlewares added directly run before Vite's own middlewares. If you return a function from `configureServer`, the code inside runs after Vite's middlewares (but before the HTML fallback), which is how you serve custom HTML.

## 211: How do you inject tags into index.html from a plugin?

Return tag descriptors from `transformIndexHtml`:

```js
const analytics = () => ({
  name: "analytics",
  transformIndexHtml() {
    return [
      {
        tag: "script",
        attrs: { src: "https://example.com/a.js", defer: true },
        injectTo: "head",
      },
    ];
  },
});
```

`injectTo` can be `'head'`, `'body'`, `'head-prepend'` or `'body-prepend'`. You can also return a changed HTML string.

## 212: What are plugin hook filters and why use them?

Hook filters let you tell Vite (and Rolldown) which modules a hook cares about. The hook is not called at all for other modules. In Vite 8 this matters a lot for speed, because calling a JS hook from Rust code for every module has a cost.

```js
export default function yamlPlugin() {
  return {
    name: "yaml",
    transform: {
      filter: { id: /\.ya?ml$/ },
      handler(code, id) {
        return { code: `export default ${toJson(code)}`, moduleType: "js" };
      },
    },
  };
}
```

Filters are supported since Vite 6.3. `@rolldown/pluginutils` has helpers like `exactRegex` and `prefixRegex`.

## 213: What is moduleType in a load or transform result?

In Vite 8, when a plugin turns non-JS content (like YAML or a custom format) into JavaScript in `load` or `transform`, it should return `moduleType: 'js'`. Rolldown decides how to parse a module from its type, and without it Rolldown may try to treat the module as the original file type.

## 214: What does enforce: 'pre' and 'post' mean for plugins?

It changes when the plugin runs compared to Vite's core plugins:

1. Alias
2. User plugins with `enforce: 'pre'`
3. Vite core plugins
4. User plugins without `enforce`
5. Vite build plugins
6. User plugins with `enforce: 'post'`
7. Vite post-build plugins (minify, manifest, reporting)

Use `'pre'` if you must see the original code before Vite transforms it, and `'post'` if you need the final code.

## 215: How can one plugin package provide several plugins?

Return an array. Vite flattens nested arrays and ignores falsy values, so you can also add plugins conditionally.

```js
export default defineConfig(({ mode }) => ({
  plugins: [
    react(),
    mode === "analyze" && visualizer(),
    myPluginPack(), // returns [pluginA(), pluginB()]
  ],
}));
```

## 216: How do you transform TypeScript in a plugin without writing your own parser?

Use `transformWithOxc` exported from `vite`:

```js
import { transformWithOxc } from "vite";

const result = await transformWithOxc(tsCode, "file.ts", {
  lang: "ts",
});
console.log(result.code);
```

`transformWithEsbuild` is deprecated in Vite 8 and needs `esbuild` installed.

## 217: How do you emit an extra file from a plugin during the build?

Use `this.emitFile` in a build hook:

```js
const robots = () => ({
  name: "robots",
  apply: "build",
  generateBundle() {
    this.emitFile({
      type: "asset",
      fileName: "robots.txt",
      source: "User-agent: *\nAllow: /\n",
    });
  },
});
```

In Vite 8 you must use `this.emitFile` instead of adding keys to the `bundle` object.

## 218: How can plugin code on the server talk to the browser?

Through the HMR WebSocket. On the server use `server.ws.send` and `server.ws.on`. In the browser use `import.meta.hot.on` and `import.meta.hot.send`.

```js
// plugin
configureServer(server) {
  server.ws.on("my:ping", (data, client) => {
    client.send("my:pong", { time: Date.now() });
  });
}
```

```js
// client
import.meta.hot?.send("my:ping", {});
import.meta.hot?.on("my:pong", (data) => console.log(data.time));
```

Prefix event names to avoid conflicts with other plugins.

## 219: What is mergeConfig?

A helper that deep merges two Vite configs. Arrays are concatenated, and objects are merged key by key.

```js
import { mergeConfig } from "vite";
import base from "./vite.base.config";

export default mergeConfig(base, {
  build: { sourcemap: true },
});
```

It works on config objects, not config functions. Call the function first if needed.

## 220: How do you use Vite from Node.js code instead of the CLI?

Vite exports `createServer`, `build`, `preview` and `resolveConfig`:

```js
import { createServer, build, preview } from "vite";

const server = await createServer({ configFile: "./vite.config.ts" });
await server.listen();
server.printUrls();

await build({ root: "./site", build: { outDir: "out" } });

const previewServer = await preview({ preview: { port: 8080 } });
previewServer.printUrls();
```

This is how frameworks and tools build on top of Vite.

## 221: How do you serve built assets from a CDN?

Set `base` to the CDN URL. All asset URLs in HTML, JS and CSS will point there.

```js
export default defineConfig({
  base: "https://cdn.example.com/my-app/",
});
```

If only some files should come from the CDN, or the URL depends on runtime values, use `experimental.renderBuiltUrl`.

## 222: What is experimental.renderBuiltUrl?

It lets you decide the URL of each built file. It is useful when assets and HTML are on different domains, or when JS must compute the URL at runtime.

```js
export default defineConfig({
  experimental: {
    renderBuiltUrl(filename, { hostType }) {
      if (hostType === "js") {
        return { runtime: `window.__assetsPath(${JSON.stringify(filename)})` };
      }
      return { relative: true };
    },
  },
});
```

`hostType` is `'js'`, `'css'` or `'html'`. As the name says, it is still experimental.

## 223: How do you set a CSP nonce for scripts and styles Vite adds?

Use `html.cspNonce`. Vite adds a `nonce` attribute to the script and style tags it creates and a `<meta property="csp-nonce">` tag so dynamically added elements get it too.

```js
export default defineConfig({
  html: { cspNonce: "NONCE_PLACEHOLDER" },
});
```

Your server must replace the placeholder with a new random value for every request, and send the same value in the `Content-Security-Policy` header.

## 224: What is build.cssTarget and when do you need it?

It sets the browser target for CSS minification separately from JS. By default it is the same as `build.target`. You need it when your JS can be modern but CSS must support an older browser, for example an Android WebView that supports modern JS but not some newer CSS syntax like `#RGBA` colors.

## 225: Why might a modern feature like a private class field still work in dev but break in an old browser after build?

Vite only lowers syntax in production down to `build.target`. In dev, code is transformed minimally and served for modern browsers. If you need to support a browser older than the default target, set `build.target` for it (for example `['chrome100', 'safari15']`). For browsers that need ES5 you need `@vitejs/plugin-legacy`, but plugin-legacy can't go to ES5 or lower in Vite 8.

## 226: How do you hide dependency code from DevTools stack traces?

Vite adds `x_google_ignoreList` to source maps in dev, so Chrome DevTools hides frames from `node_modules` by default. You can change which files are ignored with `server.sourcemapIgnoreList`:

```js
server: {
  sourcemapIgnoreList: (sourcePath) => sourcePath.includes("node_modules"),
},
```

## 227: How do you build a Progressive Web App with Vite?

Use `vite-plugin-pwa`. It creates the web app manifest and a service worker (with Workbox), and handles precaching of your built files.

```js
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig({
  plugins: [
    VitePWA({
      registerType: "autoUpdate",
      manifest: { name: "My App", short_name: "App", theme_color: "#222" },
    }),
  ],
});
```

## 228: How does tree shaking work in a Vite build?

Rolldown analyzes ES module imports and exports and drops exports that are never used. It also uses the `sideEffects` field in a package's `package.json`. If a package says `"sideEffects": false`, unused modules from it can be dropped completely. CommonJS code is harder to shake, so ESM dependencies give smaller bundles. In Vite 8, Oxc's semantic analysis helps Rolldown shake code more precisely.

## 229: What does the sideEffects field mean and how can it break your app?

`"sideEffects": false` tells the bundler that importing a module does nothing except export values. The bundler can drop the import if no exports are used. If a module does have side effects (like `import './polyfill.js'` or importing CSS), the bundler might remove it. In that case list those files: `"sideEffects": ["*.css", "./src/polyfill.js"]`.

## 230: What does resolve.tsconfigPaths do and is there a cost?

When `true` (Vite 8+), Vite reads `compilerOptions.paths` from your tsconfig files and resolves imports with them, so you don't need to duplicate aliases in `resolve.alias`. It is off by default because it has a small performance cost. Before Vite 8, people used the `vite-tsconfig-paths` plugin for this.

## 231: Does Vite support TypeScript decorators?

- **Legacy TS decorators** (`experimentalDecorators`) are transformed by Oxc. Since Vite 8, `emitDecoratorMetadata` is also supported without an extra plugin, which matters for libraries like TypeORM or NestJS-style DI.
- **Standard (TC39) decorators** are not lowered by Oxc yet. If your target browsers don't support them, you need Babel (`@rolldown/plugin-babel` with `@babel/plugin-proposal-decorators`) or SWC.

## 232: How do you replace React with Preact in a Vite app?

Use an alias, so imports of React go to `preact/compat`:

```js
export default defineConfig({
  resolve: {
    alias: {
      react: "preact/compat",
      "react-dom": "preact/compat",
      "react/jsx-runtime": "preact/jsx-runtime",
    },
  },
});
```

The official `@preact/preset-vite` plugin does this for you and adds Preact HMR.

## 233: What does server.cors do by default?

Since Vite 6 the dev server allows CORS requests only from `localhost`, `127.0.0.1` and `::1` origins (any port). Other origins are blocked. Before, it allowed any origin, which let any website read your source code while the dev server was running. If a backend on another domain loads your dev assets, allow it:

```js
server: {
  cors: { origin: "https://backend.test" },
},
```

## 234: What is server.origin?

It sets the origin used for generated asset URLs during dev, like `http://localhost:5173`. It is used in backend integration, where the HTML comes from another server (for example `http://app.test`) and URLs like `/assets/logo.png` would otherwise point to the backend instead of Vite.

## 235: How do you write in-source tests with Vitest?

Put tests in the same file as the code inside `if (import.meta.vitest)`. In production, define `import.meta.vitest` as `undefined` so the tests are removed.

```ts
export function add(a: number, b: number) {
  return a + b;
}

if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest;
  it("adds", () => {
    expect(add(1, 2)).toBe(3);
  });
}
```

```ts
// vite.config.ts
export default defineConfig({
  define: { "import.meta.vitest": "undefined" },
  test: { includeSource: ["src/**/*.ts"] },
});
```

## 236: How do you mock a module in Vitest?

Use `vi.mock`. It is hoisted to the top of the file, so it runs before imports.

```ts
import { vi, it, expect } from "vitest";
import { getUser } from "./api";
import { showUser } from "./profile";

vi.mock("./api", () => ({
  getUser: vi.fn(async () => ({ name: "Ann" })),
}));

it("shows the user name", async () => {
  expect(await showUser()).toBe("Ann");
  expect(getUser).toHaveBeenCalled();
});
```

## 237: How do you reference a file from public in JavaScript when base is set?

Don't hardcode `/`. Use `import.meta.env.BASE_URL`:

```js
const url = `${import.meta.env.BASE_URL}images/hero.jpg`;
```

Vite only rewrites URLs it can see (imports, HTML, CSS). A string you build in JS is not rewritten, so without `BASE_URL` it breaks when the app is not at the domain root.

## 238: How can you optimize images in a Vite build?

Vite copies images as they are. To resize or compress them you add a plugin:

- `vite-imagetools`: transform images with query params, like `import hero from './hero.jpg?w=800&format=webp'`
- `vite-plugin-image-optimizer`: compress all images during the build

You can also optimize images ahead of time or use an image CDN.

## 239: How do you customize output file names?

Use Rolldown output options:

```js
build: {
  rolldownOptions: {
    output: {
      entryFileNames: "js/[name]-[hash].js",
      chunkFileNames: "js/[name]-[hash].js",
      assetFileNames: "assets/[name]-[hash][extname]",
    },
  },
},
```

Each can also be a function, for example to put fonts and images in different folders based on `assetInfo.names`.

## 240: How do you make a file like service-worker.js keep a fixed name in the build?

Add it as a separate input and give it a name without a hash:

```js
build: {
  rolldownOptions: {
    input: {
      main: "index.html",
      sw: "src/sw.ts",
    },
    output: {
      entryFileNames: (chunk) =>
        chunk.name === "sw" ? "sw.js" : "assets/[name]-[hash].js",
    },
  },
},
```

A service worker must keep the same URL, or the browser will see it as a new worker.

## 241: How do you migrate a Create React App project to Vite?

1. Remove `react-scripts`. Install `vite` and `@vitejs/plugin-react`.
2. Add a `vite.config.ts` with the React plugin.
3. Move `public/index.html` to the root, remove `%PUBLIC_URL%`, and add `<script type="module" src="/src/index.tsx"></script>`.
4. Rename env variables from `REACT_APP_*` to `VITE_*` and replace `process.env.X` with `import.meta.env.X`.
5. Rename files with JSX from `.js` to `.jsx` (or set up `oxc.include` to treat `.js` as JSX).
6. Update scripts to `vite`, `vite build`, `vite preview`, and replace Jest with Vitest if you want.
7. Set `server.port: 3000` and `build.outDir: 'build'` if other tools expect the old values.

## 242: What webpack features need to be replaced when moving to Vite?

- `require.context` becomes `import.meta.glob`
- `process.env.X` becomes `import.meta.env.X` (and the `VITE_` prefix)
- `require()` in source code becomes `import`
- webpack loaders become Vite plugins or built-in features (CSS, assets, TS work without setup)
- `DefinePlugin` becomes `define`
- `devServer.proxy` becomes `server.proxy`
- magic comments like `/* webpackChunkName */` don't work. Use `codeSplitting` groups instead.

## 243: How do you migrate a complex project from Vite 7 to Vite 8?

The Vite team suggests two steps:

1. While on Vite 7, switch the `vite` package to `rolldown-vite` (`"vite": "npm:rolldown-vite@7.2.2"`). This is Vite 7 with Rolldown, so you can find Rolldown problems separately.
2. Then upgrade to `vite@^8`.

Then go through the migration guide: `build.rollupOptions` to `build.rolldownOptions`, `esbuild` to `oxc`, `manualChunks` to `codeSplitting`, CommonJS default import changes, and plugins that use unsupported hooks. Many options are converted automatically, so small projects often need no changes.

## 244: What is the devtools option in Vite 8?

`devtools` turns on Vite Devtools, a UI to look at how your app is processed: module graph, plugin transforms, build output and chunk sizes. It replaces some of what people did with `vite-plugin-inspect` and bundle visualizers.

## 245: What does server.forwardConsole do?

It sends `console` logs and errors from the browser to the dev server's terminal. This is mainly for AI coding agents that read the terminal but can't see the browser. By default it turns on automatically when Vite detects a coding agent and is off otherwise.

## 246: How do you build an IIFE bundle for a script tag?

Use library mode with the `iife` format and a global name:

```js
export default defineConfig({
  build: {
    lib: {
      entry: "src/widget.ts",
      name: "MyWidget", // window.MyWidget
      formats: ["iife"],
      fileName: () => "widget.js",
    },
  },
});
```

Users can then load it with `<script src="widget.js"></script>`.

## 247: How do you map externals to globals in a UMD or IIFE library build?

Use `output.globals`, so the bundle uses a global variable for an external package:

```js
build: {
  lib: { entry: "src/index.ts", name: "MyLib", formats: ["umd"] },
  rolldownOptions: {
    external: ["vue"],
    output: { globals: { vue: "Vue" } },
  },
},
```

## 248: The app shows a blank page after deploying. What do you check first?

1. Open DevTools: are JS and CSS files returning 404? Usually `base` is wrong for the deploy path.
2. Is the server serving `index.html` for routes? Without the SPA fallback, deep links return 404.
3. Are files served with the right MIME type? A `text/html` response for a `.js` file (often the SPA fallback answering a missing file) causes "Failed to load module script".
4. Are env variables set at build time? A missing `VITE_API_URL` can cause a crash at startup.
5. Does `vite preview` show the same problem? If not, it is a server config problem.

## 249: Why is an env variable undefined in the browser?

Common reasons:

- it doesn't start with `VITE_` (or your `envPrefix`)
- the `.env` file is not in `envDir` (the root by default)
- you added it while the dev server was running and it didn't restart
- it was set on the hosting platform after the build. Env values are fixed at build time
- you read it with `process.env` instead of `import.meta.env`

## 250: Why does HMR sometimes do a full reload even for a small change?

- The changed module is not inside any HMR boundary (no framework plugin or `accept` handles it).
- A React file exports both components and other values, so Fast Refresh can't update it.
- There is a circular import, and the update chain reaches a module that can't accept it.
- The file is imported by `vite.config` or is an env file, which restarts the server.

Running `vite --debug hmr` shows why each update became a full reload.

## 251: How do you fix a linked monorepo package written in CommonJS that fails in dev?

Linked packages are treated as source code and are not pre-bundled, so CommonJS code in them is not converted to ESM. Add the package to `optimizeDeps.include` so it gets pre-bundled:

```js
export default defineConfig({
  optimizeDeps: {
    include: ["@my-org/legacy-utils"],
  },
});
```

The better long-term fix is to publish the package as ESM.

## 252: What does optimizeDeps.noDiscovery do?

When `true`, Vite does not scan your code or discover dependencies at runtime. Only packages in `optimizeDeps.include` are pre-bundled. This is useful when you know your dependencies are ESM and you want to avoid the optimizer, or in test runners where scanning is not useful.

## 253: What does optimizeDeps.holdUntilCrawlEnd do?

It is `true` by default. On a cold start, Vite waits until all static imports have been crawled before it sends the pre-bundled deps to the browser. That way, if a new dependency is found during the crawl, it can be included without a page reload. Setting it to `false` can make the first load faster in some projects, at the risk of extra reloads.

## 254: How do you use Storybook with Vite?

Use the `@storybook/react-vite` (or `vue3-vite`, `svelte-vite` and so on) framework package. Storybook then uses Vite to build stories and loads your `vite.config` automatically, so aliases, plugins and CSS setup are shared. You can change the config for Storybook only with `viteFinal` in `.storybook/main.ts`.

## 255: What is the --configLoader option?

It controls how Vite loads the config file:

- `bundle` (default): bundles the config with its imports into a temp file and runs it
- `runner`: uses the module runner to load it on the fly, no temp file
- `native`: uses Node's own module loader (the config must be valid for Node, for example `.mjs` or a TS file Node can strip)

```bash
vite --configLoader runner
```

`runner` is helpful in monorepos where a temp file in the project causes problems.

## 256: Why can a big JSON import be slow and how does Vite help?

A large object literal in JS is slower to parse than the same data in `JSON.parse("...")`, because the JS parser has more work to do. With `json.stringify: 'auto'` (default), Vite outputs `JSON.parse` for JSON files bigger than 10 kB. If you set `json.stringify: true`, named exports from JSON are turned off.

## 257: How do you get the URL of a CSS file instead of injecting it?

Use `?url`:

```js
import themeUrl from "./themes/dark.css?url";

const link = document.createElement("link");
link.rel = "stylesheet";
link.href = themeUrl;
document.head.append(link);
```

In production this gives you the URL of the built (minified, hashed) CSS file. It is useful for themes you switch at runtime.

## 258: How do you configure PostCSS in Vite: config file or inline?

Both work. A `postcss.config.js` is found automatically and is also used by other tools. Inline config in `vite.config` avoids an extra file:

```js
import autoprefixer from "autoprefixer";

export default defineConfig({
  css: {
    postcss: { plugins: [autoprefixer()] },
  },
});
```

If you provide inline config, Vite does not look for a config file.

## 259: What does css.preprocessorMaxWorkers do?

Sass, Less and Stylus run in worker threads. This option sets how many workers can be used. The default is `true`, which means CPU count minus one. Setting it to `0` runs the preprocessors in the main thread. Lower it if your build runs out of memory on CI.

## 260: How do you test the production build in end-to-end tests?

Build once and run `vite preview` as the server for tests. With Playwright:

```ts
// playwright.config.ts
export default defineConfig({
  webServer: {
    command: "npm run build && npm run preview -- --port 4173",
    port: 4173,
    reuseExistingServer: !process.env.CI,
  },
  use: { baseURL: "http://localhost:4173" },
});
```

Testing against the build catches problems the dev server hides, like wrong `base` or missing chunks.

## 261: How do you deploy a Vite app to GitHub Pages?

1. Set `base: '/<repo-name>/'` (not needed for `user.github.io` repos or custom domains).
2. Build with GitHub Actions and upload `dist`:

```yaml
- uses: actions/checkout@v4
- uses: actions/setup-node@v4
  with:
    node-version: 22
- run: npm ci
- run: npm run build
- uses: actions/upload-pages-artifact@v3
  with:
    path: dist
- uses: actions/deploy-pages@v4
```

GitHub Pages has no SPA fallback, so use hash routing or copy `index.html` to `404.html`.

## 262: How do you configure Nginx for a Vite SPA?

```nginx
server {
  listen 80;
  root /var/www/app/dist;

  location /assets/ {
    add_header Cache-Control "public, max-age=31536000, immutable";
  }

  location / {
    try_files $uri $uri/ /index.html;
    add_header Cache-Control "no-cache";
  }
}
```

Hashed files in `/assets/` can be cached forever. `index.html` must always be checked again so users get new deploys. `try_files` gives the SPA fallback.

## 263: What is experimental bundled dev mode?

Added in Vite 8.1 (it was called Full Bundle Mode before). In dev, Vite serves bundled files made by Rolldown instead of one file per module. This cuts the number of requests, which helps very large apps where thousands of modules make the first page load slow. Turn it on with `vite --experimental-bundle` or `experimental.bundledDev: true`. Some third-party plugins don't work with it yet.

## 264: What is the chunk import map feature?

Normally, when one chunk changes, every chunk that imports it also changes (its content includes the hashed file name), so many files get new hashes and users download more after a deploy. With `build.chunkImportMap` (experimental, Vite 8.1), chunks import each other by stable names and an import map in the HTML maps those names to hashed files. A change then only re-hashes the changed chunk. It currently does not work with `experimental.renderBuiltUrl`.

## 265: How do you give a library output a custom file name per format?

`build.lib.fileName` can be a function:

```js
build: {
  lib: {
    entry: "src/index.ts",
    formats: ["es", "cjs"],
    fileName: (format, entryName) =>
      `${entryName}.${format === "es" ? "mjs" : "cjs"}`,
  },
},
```

## 266: What do build.ssrEmitAssets and build.emitAssets do?

In SSR builds Vite does not write asset files by default, because the client build already creates them. Set `build.ssrEmitAssets: true` if the server build needs its own copies of assets. `build.emitAssets` is the same for non-client environments in the Environment API.

## 267: When should you use define and when env variables?

- Use **env variables** for values that change between environments (API URLs, feature flags per deploy). They come from `.env` files or the shell.
- Use **define** for build-time constants that come from code or files, like the app version from `package.json`, a build date, or flags that should remove code (`__DEV_TOOLS__: false`).

Both are replaced at build time.

## 268: How do you fix "global is not defined" errors?

Some old packages use Node's `global` instead of `globalThis`. Fix it with `define`:

```js
export default defineConfig({
  define: { global: "globalThis" },
});
```

Be careful: `define` replaces every `global` identifier in your code too. A better fix is to replace or update the package.

## 269: Why do packages that use Node built-ins like buffer or crypto fail in Vite?

Vite does not add polyfills for Node built-ins in the browser, like webpack 4 did. Imports of `buffer`, `stream`, `crypto` and so on get replaced with an empty module that warns. Options:

- use a browser-friendly package instead
- install the polyfill (`buffer` package) and alias it
- use a plugin like `vite-plugin-node-polyfills`

## 270: Can SSR code use secrets from process.env?

Yes, server code runs in Node, so `process.env.DB_PASSWORD` works and is not exposed to the browser. Be careful with shared code. If a module that reads secrets is imported by client code too, the secret can end up in the client bundle (if replaced by `define`) or the code just breaks. Keep server-only code in server-only files.

## 271: What is html.additionalAssetSources?

Added in Vite 8.1. Vite processes asset URLs in standard HTML attributes like `<img src>` and `<link href>`. This option lets you add other elements and attributes, for example a custom element with a `src` attribute, so Vite also bundles and rewrites those URLs.

## 272: What is server.preTransformRequests?

When `true` (default), Vite starts transforming a module's static imports as soon as it transforms the module, before the browser asks for them. This saves time on page load because the transforms run in parallel with the browser's requests. You can turn it off to reduce CPU use, but pages will load slower.

## 273: How do you build without writing files to disk?

Use the JavaScript API with `build.write: false`. The result contains the output in memory.

```js
import { build } from "vite";

const result = await build({
  build: { write: false },
});

const output = Array.isArray(result) ? result[0].output : result.output;
for (const file of output) {
  console.log(file.fileName, file.type);
}
```

This is useful for tests or tools that process the output further.

## 274: How do you replace Vite's logger?

Use `customLogger`, for example to send logs to your own system or hide some warnings:

```js
import { createLogger, defineConfig } from "vite";

const logger = createLogger();
const originalWarn = logger.warn;

logger.warn = (msg, options) => {
  if (msg.includes("some noisy warning")) return;
  originalWarn(msg, options);
};

export default defineConfig({ customLogger: logger });
```

## 275: How do you use the Vite dev server for a browser extension?

Browser extensions have special entry points (manifest, background, content scripts) and can't load modules from `localhost` easily. Use a plugin like `@crxjs/vite-plugin` or a framework like WXT, which build the extension from the manifest and add HMR support. Without these you can run `vite build --watch` and reload the extension by hand.

## 276: How do you use Vite with Electron?

Use a tool that understands Electron's main and renderer processes, for example `electron-vite` or Electron Forge's Vite template. The renderer is a normal Vite app. The main and preload scripts are built for Node. In production, set `base: './'` so assets load from the file system.

## 277: How does Vite generate preload code for dynamic imports?

When you write `import('./page.js')`, Vite wraps it in a small helper (`__vitePreload`). Before importing the chunk, the helper adds `<link rel="modulepreload">` for the chunk's dependencies and `<link rel="stylesheet">` for its CSS, so they all load in parallel. Without this, the browser would load the chunk, then find its imports, then load those, which is slower.

## 278: What does build.license do?

When enabled, Vite writes a file with the licenses of the dependencies bundled into your app (by default `.vite/license.md` in the output). Many licenses (like MIT) require you to keep the license text when you distribute the code, and this helps with that.

## 279: How do you build a site with prerendered (static) pages using Vite?

Plain Vite only builds an SPA. For prerendering:

- use a framework with SSG support (Astro, Nuxt, SvelteKit, VitePress, React Router with `prerender`)
- or use a plugin like `vite-ssg` for Vue
- or do it yourself: build client and server, then in a Node script call `render(url)` for each route and write the HTML files to `dist`

## 280: How do you use module federation with Vite?

Use `@module-federation/vite`, the official plugin from the Module Federation team. It lets one Vite app expose modules and another load them at runtime. Rolldown also has its own module federation support, which Vite 8 can use. Both host and remotes must agree on shared dependencies (like React) to avoid loading two copies.

## 281: How do you add Vite to an existing multi-page app with plain HTML files?

Put each HTML file in the project and list them as inputs. Vite processes their scripts and styles, and you get HMR and bundling.

```js
export default defineConfig({
  appType: "mpa",
  build: {
    rolldownOptions: {
      input: {
        home: "index.html",
        contact: "contact.html",
        blog: "blog/index.html",
      },
    },
  },
});
```

`appType: 'mpa'` turns off the SPA fallback, so unknown URLs return 404 like a real static site.

## 282: Can you run Vite with Bun or Deno?

Yes. Vite works with Bun (`bun create vite`, `bunx --bun vite`) and with Deno (`deno run -A npm:create-vite`). Vite still uses its own pipeline, so Bun or Deno only replace the JavaScript runtime that runs Vite. Most plugins work, but some Node-specific behavior may differ.

## 283: Where does Vite look for the PostCSS, Tailwind and browserslist config?

- PostCSS: `postcss.config.js` (and other formats) from the root and parent folders, unless `css.postcss` is set inline
- Tailwind v4: config is in your CSS (`@import "tailwindcss"` and `@theme`), the plugin finds sources automatically
- browserslist: Vite does not use it for `build.target`. Autoprefixer (PostCSS) and plugin-legacy do read it

## 284: How do you speed up the TypeScript type check in a Vite build?

`vite build` itself does not check types. The slow part is `tsc -b`. Options:

- run `tsc` and `vite build` in parallel in CI instead of in sequence
- use project references with incremental builds (`tsc -b` with `.tsbuildinfo`)
- try `tsgo` (TypeScript native preview) for a faster check
- in dev, use `vite-plugin-checker` so checks run in a worker without blocking HMR

## 285: How do you use the Vite dev server with HTTPS and a custom domain?

1. Map the domain to `127.0.0.1` in `/etc/hosts` (for example `myapp.test`).
2. Create a certificate with `mkcert myapp.test`.
3. Configure Vite:

```js
server: {
  host: "myapp.test",
  https: {
    key: fs.readFileSync("myapp.test-key.pem"),
    cert: fs.readFileSync("myapp.test.pem"),
  },
  allowedHosts: ["myapp.test"],
},
```

This is helpful for testing cookies, OAuth redirects or service workers that need HTTPS.

## 286: What does the --force flag do?

`vite --force` ignores the dependency cache and pre-bundles all dependencies again. Use it when you patched something in `node_modules`, or when the cache looks broken (strange errors from a dependency, or old code). The same as `optimizeDeps.force: true`.

## 287: How do you handle "Outdated Optimize Dep" 504 errors in the browser?

The browser asked for a pre-bundled dependency from an old optimizer run. It happens after Vite re-bundled deps while the page was open. Usually a page reload fixes it. If it keeps happening, add the late-discovered dependencies to `optimizeDeps.include`, or clear the cache with `--force`.

## 288: How do you use Vue JSX with Vite?

Install `@vitejs/plugin-vue-jsx`:

```js
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";

export default defineConfig({
  plugins: [vue(), vueJsx()],
});
```

Then you can write `.jsx`/`.tsx` files and use JSX in `<script lang="tsx">` in SFCs, with HMR.

## 289: How do you remove console.log calls from the production build?

Use the minifier's drop options:

```js
export default defineConfig({
  build: {
    rolldownOptions: {
      output: {
        minify: {
          compress: { dropConsole: true, dropDebugger: true },
        },
      },
    },
  },
});
```

In Vite 7 and older this was `esbuild: { drop: ['console', 'debugger'] }`, which Vite 8 still converts. Make sure you really want to remove `console.error` too.

## 290: What does server.hmr.clientPort do?

It sets the port the browser uses for the HMR WebSocket, without changing the port Vite listens on. Use it when the browser connects through a proxy or a port mapping (for example the proxy is on 443 and Vite on 5173).

## 291: How do you keep both a dev and a production config without repeating everything?

Use a config function and branch on `command` or `mode`:

```js
export default defineConfig(({ command, mode }) => {
  const isBuild = command === "build";

  return {
    plugins: [react(), isBuild && compressionPlugin()],
    build: { sourcemap: mode === "staging" },
    server: isBuild
      ? undefined
      : { proxy: { "/api": "http://localhost:8080" } },
  };
});
```

Or put shared settings in a base file and use `mergeConfig`.

## 292: How do you build an app that runs in a sub-path that is only known at runtime?

`base` is fixed at build time. For runtime paths:

- use `base: './'` for relative URLs (works if routes are not nested)
- or use `experimental.renderBuiltUrl` with a `runtime` expression that reads a global set by the server, like `window.__BASE__`

The HTML must also point to the right path, so the server usually rewrites `index.html`.

## 293: What is the difference between ssrLoadModule and the module runner?

`server.ssrLoadModule(url)` is the old API to load and run a module on the server with Vite's transforms. The module runner (part of the Environment API) is the newer, more general way. It runs modules in any runtime (Node, workers, edge runtimes) and talks to the Vite server through a transport. `ssrLoadModule` is still supported, but new framework code uses the module runner.

## 294: What does vite build --app do?

It builds all environments of the app (for example `client` and `ssr`) in one command, using the `builder` config. Without it, `vite build` only builds the client environment. Frameworks use the `builder.buildApp` hook to control the order of builds.

```js
export default defineConfig({
  builder: {
    async buildApp(builder) {
      await builder.build(builder.environments.client);
      await builder.build(builder.environments.ssr);
    },
  },
});
```

## 295: How do you set different config for client and SSR in one Vite config?

With the Environment API you can put per-environment options under `environments`:

```js
export default defineConfig({
  build: { sourcemap: false },
  environments: {
    client: {
      build: { outDir: "dist/client" },
    },
    ssr: {
      build: { outDir: "dist/server" },
      resolve: { noExternal: ["some-lib"] },
    },
  },
});
```

Top-level options act as defaults for all environments.

## 296: Why is it a problem to import server-only modules in client code, and how do you protect against it?

The client bundle includes everything it imports, so server code with secrets or Node APIs ends up in the browser (or breaks the build). Ways to protect:

- name files `*.server.ts` and use a framework that blocks them in client code (React Router, SvelteKit's `$lib/server`)
- use a package like `server-only` that throws when bundled for the client
- write a small plugin that fails the build if a client environment imports from a `server/` folder

## 297: How do you make Vite treat .js files as JSX?

Set `oxc.include` and the language for those files, or simply rename files to `.jsx`. Renaming is the cleanest. For a big migration from CRA you can do:

```js
export default defineConfig({
  oxc: {
    include: /src\/.*\.[jt]sx?$/,
    lang: "jsx",
  },
});
```

Also tell the dependency scanner (`optimizeDeps.rolldownOptions.moduleTypes`) that `.js` files can contain JSX, or the scan may fail on them.

## 298: How do you write a Vite config in TypeScript that imports other TS files?

Just import them. With the default `bundle` loader, Vite bundles the config and its local imports, so `.ts` imports work. Packages from `node_modules` are not bundled into it. If an imported package is TypeScript only, use `--configLoader runner`.

## 299: How do you add a custom HMR handler for a non-JS file type like a Markdown file?

Use `hotUpdate` (or the older `handleHotUpdate`) in a plugin and send a custom event:

```js
const markdownHmr = () => ({
  name: "markdown-hmr",
  hotUpdate({ file, server }) {
    if (this.environment.name !== "client" || !file.endsWith(".md")) return;
    server.ws.send({ type: "custom", event: "md:update", data: { file } });
    return [];
  },
});
```

The client listens with `import.meta.hot.on('md:update', ...)` and reloads the content. Returning `[]` stops Vite's default handling.

## 300: How do you check that your Vite build output is correct before deploy?

- run `vite preview` and click through the app
- check `dist` for unexpected large chunks (`build` output, bundle visualizer, Vite Devtools)
- run e2e tests against the preview server
- check that `index.html` points to files that exist and use the right `base`
- make sure no secrets ended up in `dist` (search the files for API keys)

# Advanced Questions (301-450)
