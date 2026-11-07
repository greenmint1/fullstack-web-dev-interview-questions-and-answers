# WebAssembly (WASM) Interview Questions and Answers

_Last updated: October 28, 2026_

60 WebAssembly interview questions with answers, split into three levels: 20 easy, 20 moderate and 20 advanced.

The answers target WebAssembly 3.0 (finalized in September 2025) and WASI 0.3 (released in June 2026). Examples use the browser `WebAssembly` JavaScript API, Emscripten for C/C++ and wasm-bindgen for Rust. Older approaches you will still see in existing projects, like Asyncify or WASI Preview 1, are mentioned where it makes sense.

## Table of Contents

- [Easy Questions (1-20)](#easy-questions-1-20)
- [Moderate Questions (21-40)](#moderate-questions-21-40)
- [Advanced Questions (41-60)](#advanced-questions-41-60)

### Easy Questions (1-20)

- [1: What is WebAssembly?](#1-what-is-webassembly)
- [2: Why was WebAssembly created?](#2-why-was-webassembly-created)
- [3: Does WebAssembly replace JavaScript?](#3-does-webassembly-replace-javascript)
- [4: Which languages can compile to WebAssembly?](#4-which-languages-can-compile-to-webassembly)
- [5: What is the difference between .wasm and .wat files?](#5-what-is-the-difference-between-wasm-and-wat-files)
- [6: What is inside a Wasm module?](#6-what-is-inside-a-wasm-module)
- [7: What value types does WebAssembly have?](#7-what-value-types-does-webassembly-have)
- [8: How do you load and run a .wasm file in the browser?](#8-how-do-you-load-and-run-a-wasm-file-in-the-browser)
- [9: What is the difference between WebAssembly.Module and WebAssembly.Instance?](#9-what-is-the-difference-between-webassemblymodule-and-webassemblyinstance)
- [10: What are imports and exports in Wasm?](#10-what-are-imports-and-exports-in-wasm)
- [11: What is linear memory?](#11-what-is-linear-memory)
- [12: Is WebAssembly always faster than JavaScript?](#12-is-webassembly-always-faster-than-javascript)
- [13: Is WebAssembly secure?](#13-is-webassembly-secure)
- [14: Which browsers support WebAssembly?](#14-which-browsers-support-webassembly)
- [15: What does the server need to do to serve .wasm files correctly?](#15-what-does-the-server-need-to-do-to-serve-wasm-files-correctly)
- [16: What is Emscripten?](#16-what-is-emscripten)
- [17: What are wasm-bindgen and wasm-pack?](#17-what-are-wasm-bindgen-and-wasm-pack)
- [18: Can WebAssembly access the DOM directly?](#18-can-webassembly-access-the-dom-directly)
- [19: Can WebAssembly run outside the browser?](#19-can-webassembly-run-outside-the-browser)
- [20: What are common use cases for WebAssembly?](#20-what-are-common-use-cases-for-webassembly)

### Moderate Questions (21-40)

- [21: How do you pass a string from JavaScript to Wasm and back?](#21-how-do-you-pass-a-string-from-javascript-to-wasm-and-back)
- [22: How does JavaScript read and write Wasm memory?](#22-how-does-javascript-read-and-write-wasm-memory)
- [23: How does memory growth work?](#23-how-does-memory-growth-work)
- [24: What is the difference between instantiateStreaming, instantiate, compile and the sync constructors?](#24-what-is-the-difference-between-instantiatestreaming-instantiate-compile-and-the-sync-constructors)
- [25: How do you use a Wasm module with a bundler like Vite or webpack?](#25-how-do-you-use-a-wasm-module-with-a-bundler-like-vite-or-webpack)
- [26: How do you call JavaScript functions from Wasm?](#26-how-do-you-call-javascript-functions-from-wasm)
- [27: What are WebAssembly tables and what are they used for?](#27-what-are-webassembly-tables-and-what-are-they-used-for)
- [28: What is WebAssembly.Global?](#28-what-is-webassemblyglobal)
- [29: What happens when Wasm code hits an error?](#29-what-happens-when-wasm-code-hits-an-error)
- [30: How do you debug WebAssembly in the browser?](#30-how-do-you-debug-webassembly-in-the-browser)
- [31: How do you reduce the size of a .wasm file?](#31-how-do-you-reduce-the-size-of-a-wasm-file)
- [32: How do you run a Wasm module in a Web Worker?](#32-how-do-you-run-a-wasm-module-in-a-web-worker)
- [33: How do you compile C code with Emscripten and call it from JavaScript?](#33-how-do-you-compile-c-code-with-emscripten-and-call-it-from-javascript)
- [34: How do you build a Rust library for the browser?](#34-how-do-you-build-a-rust-library-for-the-browser)
- [35: What is AssemblyScript and when would you use it?](#35-what-is-assemblyscript-and-when-would-you-use-it)
- [36: Why can calling Wasm from JavaScript in a loop be slow?](#36-why-can-calling-wasm-from-javascript-in-a-loop-be-slow)
- [37: How does caching of Wasm modules work?](#37-how-does-caching-of-wasm-modules-work)
- [38: How do you allow WebAssembly with a strict Content Security Policy?](#38-how-do-you-allow-webassembly-with-a-strict-content-security-policy)
- [39: How do you test code compiled to WebAssembly?](#39-how-do-you-test-code-compiled-to-webassembly)
- [40: How do you decide if a part of your app should move to WebAssembly?](#40-how-do-you-decide-if-a-part-of-your-app-should-move-to-webassembly)

### Advanced Questions (41-60)

- [41: How does a browser engine compile and run WebAssembly?](#41-how-does-a-browser-engine-compile-and-run-webassembly)
- [42: What does it mean that WebAssembly is a stack machine with structured control flow?](#42-what-does-it-mean-that-webassembly-is-a-stack-machine-with-structured-control-flow)
- [43: How do threads work in WebAssembly?](#43-how-do-threads-work-in-webassembly)
- [44: What is WebAssembly SIMD and how do you use it?](#44-what-is-webassembly-simd-and-how-do-you-use-it)
- [45: What is Wasm GC and why does it matter?](#45-what-is-wasm-gc-and-why-does-it-matter)
- [46: How does exception handling work in WebAssembly?](#46-how-does-exception-handling-work-in-webassembly)
- [47: What is Memory64 and when should you use it?](#47-what-is-memory64-and-when-should-you-use-it)
- [48: What's new in WebAssembly 3.0?](#48-whats-new-in-webassembly-30)
- [49: What is the WebAssembly Component Model?](#49-what-is-the-webassembly-component-model)
- [50: What is WASI and how did it change between versions?](#50-what-is-wasi-and-how-did-it-change-between-versions)
- [51: What are the limits of the WebAssembly security model?](#51-what-are-the-limits-of-the-webassembly-security-model)
- [52: How do you detect which Wasm features the browser supports?](#52-how-do-you-detect-which-wasm-features-the-browser-supports)
- [53: How do you call async JavaScript APIs from synchronous Wasm code?](#53-how-do-you-call-async-javascript-apis-from-synchronous-wasm-code)
- [54: What are JS String Builtins?](#54-what-are-js-string-builtins)
- [55: What is ESM integration for WebAssembly?](#55-what-is-esm-integration-for-webassembly)
- [56: How is memory managed in a Wasm app and how do leaks happen?](#56-how-is-memory-managed-in-a-wasm-app-and-how-do-leaks-happen)
- [57: What are common performance pitfalls with WebAssembly?](#57-what-are-common-performance-pitfalls-with-webassembly)
- [58: How is WebAssembly used on the server and at the edge, and how does it compare to containers?](#58-how-is-webassembly-used-on-the-server-and-at-the-edge-and-how-does-it-compare-to-containers)
- [59: You need to bring an existing C++ image processing library to a web app. How would you approach it?](#59-you-need-to-bring-an-existing-c-image-processing-library-to-a-web-app-how-would-you-approach-it)
- [60: A Wasm module is slower than expected in production. How do you investigate?](#60-a-wasm-module-is-slower-than-expected-in-production-how-do-you-investigate)

---

# Easy Questions (1-20)

## 1: What is WebAssembly?

WebAssembly (Wasm) is a binary instruction format that runs in a small virtual machine inside the browser, next to JavaScript. You usually don't write it by hand. You write code in a language like C, C++, Rust or Go, compile it to a `.wasm` file, and load that file from JavaScript.

It is a W3C standard and is supported by all major browsers. It can also run outside the browser, in Node.js, Deno, Bun and standalone runtimes like Wasmtime and Wasmer.

## 2: Why was WebAssembly created?

JavaScript is flexible but hard to make fast in a predictable way, because the engine has to guess types at runtime. Before Wasm, Mozilla made asm.js, a strict subset of JavaScript that engines could optimize well. It worked, but files were big and parsing text was slow.

WebAssembly was the follow-up, designed together by Mozilla, Google, Microsoft and Apple. The goals were:

- near native speed for heavy code
- a compact binary format that is fast to download and decode
- a safe sandbox, same as JavaScript
- a way to bring existing C/C++ code and libraries to the web

## 3: Does WebAssembly replace JavaScript?

No. Wasm is meant to work together with JavaScript, not replace it. JavaScript is still the language for the UI, DOM, events and most app logic. Wasm is useful for the parts that are heavy on CPU, like image processing, video encoding, physics, compression or parsing large files.

A normal setup is a JavaScript app that loads one or more Wasm modules and calls their functions when it needs to do heavy work.

## 4: Which languages can compile to WebAssembly?

Many. The most common ones:

- **C and C++** with Emscripten or plain Clang/LLVM
- **Rust** with the `wasm32-unknown-unknown`, `wasm32-wasip1` or `wasm32-wasip2` targets and tools like `wasm-bindgen`
- **Go** with the standard compiler (`GOOS=js GOARCH=wasm` or `GOOS=wasip1 GOARCH=wasm`) or TinyGo for smaller output
- **AssemblyScript**, a TypeScript-like language made for Wasm
- **Kotlin, Dart, Java (J2CL), OCaml** using Wasm GC
- **C#/.NET** through Blazor
- **Zig**, **Swift**, **Python** (Pyodide runs CPython compiled to Wasm)

Languages with a garbage collector used to ship their own GC inside the module, which made files large. Wasm GC fixes that for compilers that support it.

## 5: What is the difference between .wasm and .wat files?

A `.wasm` file is the binary format. This is what the browser downloads and runs.

A `.wat` file is the text format (WebAssembly Text). It shows the same module in a readable form using S-expressions. It is used for learning, debugging and small hand written examples.

```wat
(module
  (func $add (export "add") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.add))
```

You can convert between them with the `wat2wasm` and `wasm2wat` tools from WABT, or with `wasm-tools parse` and `wasm-tools print`.

## 6: What is inside a Wasm module?

A module is made of sections. The main ones:

- **Type**: function signatures
- **Import**: functions, memories, tables and globals the module needs from the outside (usually from JavaScript)
- **Function** and **Code**: the module's own functions and their bodies
- **Memory**: the linear memory the module uses
- **Table**: tables of references, mostly used for indirect function calls
- **Global**: global variables
- **Export**: what the module makes visible to the host
- **Start**: an optional function that runs on instantiation
- **Data** and **Element**: data to put into memory and tables at startup
- **Custom**: extra data like function names or debug info, ignored by the engine when running

## 7: What value types does WebAssembly have?

The basic number types are:

- `i32` and `i64`: 32 and 64 bit integers. There is no separate signed or unsigned type, the instruction decides (for example `i32.div_s` vs `i32.div_u`).
- `f32` and `f64`: 32 and 64 bit floats.

There are also:

- `v128`: a 128 bit vector used by SIMD instructions.
- Reference types like `funcref` (a reference to a function) and `externref` (a reference to a host value, like a JavaScript object). With Wasm GC there are more reference types, such as `structref`, `arrayref` and `i31ref`.

There are no strings, arrays or objects at the basic level. Higher-level types are built on top of memory or GC types by the compiler.

## 8: How do you load and run a .wasm file in the browser?

The recommended way is `WebAssembly.instantiateStreaming`. It compiles the module while it is still downloading.

```js
const { instance } = await WebAssembly.instantiateStreaming(fetch("/add.wasm"));

console.log(instance.exports.add(2, 3)); // 5
```

If you already have the bytes (for example from a file input), use `WebAssembly.instantiate(bytes)` instead. Tools like Emscripten and wasm-bindgen generate this loading code for you, so in real projects you usually call a generated `init()` function.

## 9: What is the difference between WebAssembly.Module and WebAssembly.Instance?

- **Module** is compiled, stateless code. It has no memory or values yet. It can be shared between workers with `postMessage` and instantiated many times.
- **Instance** is a module plus its state: memory, tables, globals and the imports you passed in. Its `exports` property is where you find the functions to call.

```js
const module = await WebAssembly.compileStreaming(fetch("/add.wasm"));
const instance1 = await WebAssembly.instantiate(module);
const instance2 = await WebAssembly.instantiate(module); // separate state
```

## 10: What are imports and exports in Wasm?

Exports are things the module makes available to the host: functions, memory, tables or globals. You find them on `instance.exports`.

Imports are things the module needs from the host. You pass them in an import object when you instantiate. The import object has two levels: module name and field name.

```wat
(module
  (import "env" "log" (func $log (param i32)))
  (func (export "run")
    i32.const 42
    call $log))
```

```js
const importObject = {
  env: {
    log: (value) => console.log("from wasm:", value),
  },
};

const { instance } = await WebAssembly.instantiateStreaming(
  fetch("/run.wasm"),
  importObject,
);
instance.exports.run(); // from wasm: 42
```

If an import is missing, instantiation fails with a `LinkError`.

## 11: What is linear memory?

Linear memory is one big, continuous block of bytes that a Wasm module reads and writes. It is like a large `ArrayBuffer` and addresses are just numbers (offsets) into it. Languages like C and Rust put their stack, heap and static data in this memory.

Memory size is counted in pages of 64 KiB. JavaScript can see the same bytes through `memory.buffer`, which is how data is shared between JS and Wasm.

```js
const memory = new WebAssembly.Memory({ initial: 1, maximum: 10 }); // 64 KiB to 640 KiB
const bytes = new Uint8Array(memory.buffer);
bytes[0] = 255;
```

## 12: Is WebAssembly always faster than JavaScript?

No. Wasm is usually faster and, more importantly, more predictable for CPU heavy work like number crunching, codecs, compression or simulations. There is no type guessing and no deoptimization like in JavaScript JIT.

But modern JavaScript engines are very fast, and for typical app code (DOM updates, small functions, working with JSON and objects) JavaScript is often just as fast or faster. Calling between JS and Wasm and copying data across has a cost, so moving small pieces of logic to Wasm can even make things slower. Always measure before and after.

## 13: Is WebAssembly secure?

Wasm runs in the same sandbox as JavaScript. It follows the same-origin policy and the same permissions. A module can't access files, the network or the DOM on its own. It can only call functions that the host gave it through imports.

Its memory is separated from the engine's memory, every memory access is bounds checked, and the code is validated before it runs. Control flow is structured, so code can't jump to random addresses.

That said, bugs inside the module still exist. A buffer overflow in C code compiled to Wasm can't escape the sandbox, but it can still corrupt the module's own memory and data.

## 14: Which browsers support WebAssembly?

All modern browsers support the core of WebAssembly: Chrome, Edge, Firefox and Safari, on desktop and mobile. It has been supported since 2017. Internet Explorer never supported it.

Newer features like threads, SIMD, Wasm GC, exception handling or Memory64 came later and their support differs between browsers and versions. For those, check a table like [webassembly.org/features](https://webassembly.org/features/) and use feature detection.

## 15: What does the server need to do to serve .wasm files correctly?

The server must send `.wasm` files with the `Content-Type: application/wasm` header. `instantiateStreaming` and `compileStreaming` refuse to work with any other type and throw a `TypeError`.

Other good practices:

- enable compression (Brotli or gzip), because Wasm compresses well
- use long cache headers together with a content hash in the file name
- if the file is on another origin, send proper CORS headers

## 16: What is Emscripten?

Emscripten is a compiler toolchain that turns C and C++ code into WebAssembly plus a JavaScript glue file. It is based on LLVM/Clang. The glue code loads the module and emulates many things C programs expect, like a file system, `printf`, POSIX functions, pthreads, and SDL or OpenGL (mapped to WebGL).

It is the standard tool for porting existing C/C++ projects to the web. Well known examples built with it include ports of SQLite, FFmpeg, and many game engines.

```bash
emcc hello.c -O3 -o hello.js
```

## 17: What are wasm-bindgen and wasm-pack?

They are Rust tools for working with WebAssembly in the browser.

- **wasm-bindgen** generates the glue between Rust and JavaScript. It lets you pass strings, objects, closures and promises across the boundary instead of only numbers. The `web-sys` and `js-sys` crates built on it give Rust access to browser APIs.
- **wasm-pack** is a build tool that runs cargo, wasm-bindgen and `wasm-opt`, and produces a folder ready to publish to npm or import in a bundler.

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    format!("Hello, {name}!")
}
```

## 18: Can WebAssembly access the DOM directly?

No. Wasm has no built-in access to the DOM or other web APIs. Everything goes through JavaScript: the module imports JS functions and calls them, and those functions touch the DOM.

Tools like wasm-bindgen (`web-sys`) and Emscripten (`emscripten::val`) hide this so it looks like direct access, but under the hood every DOM call is still a call into JavaScript. That's why frameworks that render UI from Wasm (like Yew, Leptos or Blazor) have some overhead for DOM heavy work.

## 19: Can WebAssembly run outside the browser?

Yes. Wasm is not tied to the web. It runs in:

- **Node.js, Deno and Bun**, using the same `WebAssembly` JavaScript API
- **Standalone runtimes** like Wasmtime, Wasmer and WasmEdge
- **Edge and serverless platforms** like Cloudflare Workers, Fastly Compute and Fermyon Spin
- **Plugin systems** in apps like Envoy, Zed, Shopify Functions and databases

Outside the browser, modules use **WASI** (WebAssembly System Interface) to get things like files, clocks, environment variables and sockets in a safe, standard way.

## 20: What are common use cases for WebAssembly?

- Image, audio and video editing in the browser (Figma, Photoshop on the web, ffmpeg.wasm)
- Games and game engines (Unity and Unreal web exports)
- Porting existing desktop apps and libraries (AutoCAD web, Google Earth, SQLite in the browser)
- CAD, 3D, maps and data visualization
- Compression, encryption, hashing and parsing
- Running other languages in the browser (Pyodide for Python, Ruby, PHP)
- Machine learning in the browser (ONNX Runtime Web, TensorFlow.js Wasm backend)
- Plugins and serverless functions on the server side

# Moderate Questions (21-40)

## 21: How do you pass a string from JavaScript to Wasm and back?

Core Wasm functions only take numbers, so a string has to be written into linear memory and passed as a pointer and a length. The module usually exports an `alloc` function so JS can get space in its memory.

```js
const { memory, alloc, dealloc, to_upper } = instance.exports;

// JS -> Wasm
const input = new TextEncoder().encode("hello");
const ptr = alloc(input.length);
new Uint8Array(memory.buffer, ptr, input.length).set(input);

// Wasm writes the result in place, JS reads it back
to_upper(ptr, input.length);
const result = new TextDecoder().decode(
  new Uint8Array(memory.buffer, ptr, input.length),
);

dealloc(ptr, input.length);
console.log(result); // HELLO
```

In practice you let tools do this. wasm-bindgen and Emscripten (`ccall`, `cwrap`, `stringToUTF8`, `UTF8ToString`) generate the copy code for you. For languages using Wasm GC, the JS String Builtins feature lets Wasm work with JS strings directly.

## 22: How does JavaScript read and write Wasm memory?

Through typed array views over `memory.buffer`. The memory comes either from `instance.exports.memory` or from a `WebAssembly.Memory` you created and passed as an import.

```js
const memory = instance.exports.memory;

const floats = new Float32Array(memory.buffer, ptr, count);
floats[0] = 1.5;

const view = new DataView(memory.buffer);
const value = view.getInt32(ptr, true); // Wasm is little-endian
```

Two things to remember:

- Wasm memory is always little-endian, so pass `true` to `DataView` methods.
- When the memory grows, the old `ArrayBuffer` is detached and all views on it become empty. Create views right before you use them, or recreate them after any call that might allocate.

## 23: How does memory growth work?

Memory starts at an `initial` size in 64 KiB pages and can grow up to an optional `maximum`. It grows from Wasm with the `memory.grow` instruction (this is what `malloc` does when it runs out of space) or from JS with `memory.grow(pages)`. Both return the old size in pages.

```js
const memory = new WebAssembly.Memory({ initial: 16, maximum: 1024 });
const oldPages = memory.grow(4); // add 256 KiB
```

Things to know:

- Memory can grow but never shrink.
- A 32-bit memory can be at most 4 GiB (65536 pages). Browsers may allow less in practice, especially on mobile.
- Growing can fail if the browser can't get the memory. In Wasm `memory.grow` returns `-1`, in JS it throws a `RangeError`.
- In Emscripten you need `-sALLOW_MEMORY_GROWTH` or the memory size is fixed.

## 24: What is the difference between instantiateStreaming, instantiate, compile and the sync constructors?

- `WebAssembly.instantiateStreaming(fetchPromise, imports)`: compiles while downloading and returns `{ module, instance }`. Best choice in most cases.
- `WebAssembly.compileStreaming(fetchPromise)`: same, but returns only a `Module`. Useful when you want to instantiate later or send the module to workers.
- `WebAssembly.instantiate(bytesOrModule, imports)`: works with an `ArrayBuffer` or an already compiled `Module`. With bytes it returns `{ module, instance }`, with a module it returns just the `Instance`.
- `new WebAssembly.Module(bytes)` and `new WebAssembly.Instance(module, imports)`: synchronous. They block the thread while compiling, and browsers limit the module size you can compile this way on the main thread. Use them only for small modules or inside workers.

## 25: How do you use a Wasm module with a bundler like Vite or webpack?

Most of the time you import the JS glue generated by your toolchain (wasm-pack, Emscripten), and it loads the `.wasm` file itself. The bundler only needs to copy the `.wasm` file and give its URL.

Vite can also load `.wasm` files directly with the `?init` suffix:

```js
import init from "./example.wasm?init";

const instance = await init({ env: { log: console.log } });
instance.exports.run();
```

Or get the URL and load it yourself:

```js
import wasmUrl from "./example.wasm?url";

const { instance } = await WebAssembly.instantiateStreaming(fetch(wasmUrl));
```

webpack 5 supports Wasm imports through `experiments: { asyncWebAssembly: true }`. If you want ESM style `import { add } from './x.wasm'` in Vite, use `vite-plugin-wasm`.

## 26: How do you call JavaScript functions from Wasm?

You declare an import in the module and pass a matching function in the import object. Arguments and return values are converted between JS and Wasm types: JS numbers become `i32`/`f32`/`f64`, `BigInt` maps to `i64`, and `externref` can hold any JS value.

With Rust and wasm-bindgen, you describe the JS function with `extern "C"`:

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern "C" {
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);
}

#[wasm_bindgen]
pub fn run() {
    log("hello from Rust");
}
```

With Emscripten you can use `EM_JS`, `EM_ASM` or a JS library file (`--js-library`).

## 27: What are WebAssembly tables and what are they used for?

A table is an array of references, usually function references (`funcref`). Wasm code can't hold raw function addresses in memory, so for indirect calls it stores an index into a table and uses `call_indirect`. The engine checks that the function at that index has the expected signature, or it traps.

This is how C function pointers, C++ virtual methods and Rust trait objects work after compiling to Wasm. Tables can also hold `externref` values, and they can be created from JS with `new WebAssembly.Table(...)` and shared between modules for dynamic linking.

## 28: What is WebAssembly.Global?

A `Global` is a single typed value that can be shared between JS and one or more Wasm instances. It can be mutable or immutable.

```js
const counter = new WebAssembly.Global({ value: "i32", mutable: true }, 0);

const { instance } = await WebAssembly.instantiateStreaming(fetch("/m.wasm"), {
  env: { counter },
});

counter.value = 10; // the module sees the new value
```

Compilers use globals for things like the stack pointer. In everyday app code you rarely create them yourself.

## 29: What happens when Wasm code hits an error?

The engine stops the code with a **trap**, which shows up in JavaScript as a `WebAssembly.RuntimeError`. Common causes:

- memory access out of bounds
- integer division by zero
- `unreachable` instruction (Rust `panic!` usually ends here)
- `call_indirect` with a wrong signature or a null entry
- stack overflow from deep recursion

```js
try {
  instance.exports.process(ptr, len);
} catch (err) {
  if (err instanceof WebAssembly.RuntimeError) {
    console.error("wasm trapped:", err.message);
  }
}
```

After a trap the module's memory might be in a broken state (for example a half-finished `malloc`), so it is safer to create a new instance than to keep using it. Other errors are `CompileError` (invalid bytes) and `LinkError` (missing or wrong imports). For Rust, the `console_error_panic_hook` crate prints the panic message instead of just "unreachable".

## 30: How do you debug WebAssembly in the browser?

- **Chrome DevTools** can show Wasm in the Sources panel, set breakpoints and step through code. With DWARF debug info (`-g` in Emscripten, debug builds in Rust) and the "C/C++ DevTools Support (DWARF)" extension, you see the original C/C++/Rust source and variables.
- **Firefox** supports source maps for Wasm and shows the text format when no source map exists.
- **Function names** come from the `name` custom section. Keep it in builds you profile, otherwise stack traces show only `wasm-function[123]`.
- **Logging** through an imported JS function is still the simplest tool.
- `wasm-tools print` or `wasm2wat` let you look at what the compiler produced, and `wasm-objdump` shows sections and sizes.

## 31: How do you reduce the size of a .wasm file?

- Build in release mode with size optimizations: `-Os` or `-Oz` in Emscripten, `opt-level = "z"` or `"s"` in Rust.
- Turn on link time optimization (`lto = true` in Rust, `-flto` in Clang).
- Run `wasm-opt -Oz` from Binaryen (wasm-pack and Emscripten do this already).
- Strip debug info and the names section in production.
- In Rust, set `panic = "abort"`, and avoid heavy formatting (`format!`, `{:?}`) in hot paths, since it pulls in a lot of code.
- Remove unused features and dependencies. Use `twiggy` to find what takes space.
- For Go, consider TinyGo, which gives much smaller files.
- Serve with Brotli compression. Wasm often shrinks to a third of its size or less.

## 32: How do you run a Wasm module in a Web Worker?

Heavy Wasm work on the main thread blocks the UI just like heavy JavaScript. Move it to a worker:

```js
// worker.js
let instance;

self.onmessage = async (event) => {
  if (!instance) {
    ({ instance } = await WebAssembly.instantiateStreaming(
      fetch("/image.wasm"),
    ));
  }
  const result = instance.exports.process(event.data);
  self.postMessage(result);
};
```

```js
// main.js
const worker = new Worker(new URL("./worker.js", import.meta.url), {
  type: "module",
});
worker.onmessage = (event) => console.log("done", event.data);
worker.postMessage(42);
```

For large data, send `ArrayBuffer`s as transferables to avoid copying. A compiled `WebAssembly.Module` can also be sent with `postMessage`, so you compile once and instantiate in many workers. Libraries like Comlink make the message passing nicer.

## 33: How do you compile C code with Emscripten and call it from JavaScript?

```c
// add.c
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
int add(int a, int b) {
    return a + b;
}
```

```bash
emcc add.c -O3 -o add.js \
  -sMODULARIZE -sEXPORT_ES6 \
  -sEXPORTED_RUNTIME_METHODS=ccall,cwrap
```

```js
import createModule from "./add.js";

const Module = await createModule();
console.log(Module._add(2, 3)); // direct call, note the underscore

const add = Module.cwrap("add", "number", ["number", "number"]);
console.log(add(4, 5));
```

`EMSCRIPTEN_KEEPALIVE` (or `-sEXPORTED_FUNCTIONS=_add`) keeps the function from being removed as dead code. `MODULARIZE` and `EXPORT_ES6` give you a factory function instead of a global `Module` object. For C++ classes, Embind (`--bind` / `-lembind`) is the usual way to expose them to JS.

## 34: How do you build a Rust library for the browser?

```bash
cargo new --lib my-lib
```

```toml
# Cargo.toml
[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
wasm-bindgen = "0.2"
```

```rust
// src/lib.rs
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn sum(values: &[f64]) -> f64 {
    values.iter().sum()
}
```

```bash
wasm-pack build --target web
```

```js
import init, { sum } from "./pkg/my_lib.js";

await init();
console.log(sum(new Float64Array([1, 2, 3]))); // 6
```

Use `--target bundler` for webpack/Vite projects and `--target nodejs` for Node. You can also skip wasm-pack and run `cargo build --target wasm32-unknown-unknown` and then the `wasm-bindgen` CLI yourself.

## 35: What is AssemblyScript and when would you use it?

AssemblyScript is a language with TypeScript-like syntax that compiles straight to WebAssembly. It uses Wasm types like `i32`, `f64` and `u8` instead of `number`.

```ts
export function add(a: i32, b: i32): i32 {
  return a + b;
}
```

It is a good fit for a JavaScript or TypeScript team that wants to write a small, fast module without learning Rust or C++. But it is not TypeScript: there are no union types, no `any`, no closures in the usual JS sense, and normal npm packages don't work in it. For large projects or when you need a big library ecosystem, Rust or C++ are more common choices.

## 36: Why can calling Wasm from JavaScript in a loop be slow?

Calls between JS and Wasm are cheap in modern engines, but not free. Each call has to convert arguments and the return value, and tools like wasm-bindgen often add more work, like copying strings or arrays into linear memory and back.

If you call a tiny Wasm function a million times from JS, the overhead can be bigger than the work itself. Better patterns:

- send a whole batch of data at once (one call with a pointer to an array, not one call per item)
- keep the data in Wasm memory across calls instead of copying it back and forth
- move the loop itself into Wasm
- avoid passing strings and objects on hot paths, use numbers and shared memory

## 37: How does caching of Wasm modules work?

Browsers cache the downloaded `.wasm` file with normal HTTP caching. On top of that, Chrome and Firefox cache the compiled machine code when you use `compileStreaming` or `instantiateStreaming`, so the next load can skip most of the compile time. That code cache is tied to the URL and the response, so it works best when the file doesn't change.

What helps:

- use a content hash in the file name and long `Cache-Control` headers
- always use the streaming APIs
- don't fetch the module through a path that changes every time (like a query string with a timestamp)

Storing a `WebAssembly.Module` in IndexedDB used to be an option, but browsers removed that, so don't rely on it.

## 38: How do you allow WebAssembly with a strict Content Security Policy?

If your CSP has a `script-src` without `'unsafe-eval'`, browsers block Wasm compilation. Instead of allowing `'unsafe-eval'` (which also allows `eval()` in JS), add `'wasm-unsafe-eval'`. It allows only Wasm compilation.

```http
Content-Security-Policy: script-src 'self' 'wasm-unsafe-eval'
```

It is supported in all current major browsers. The `.wasm` file also has to be allowed by `connect-src` if it is fetched from another origin.

## 39: How do you test code compiled to WebAssembly?

- **Test the source language first.** Most logic in Rust or C++ can be tested with normal native unit tests (`cargo test`, GoogleTest). This is fast and covers most bugs.
- **Test the Wasm build itself** for things that only exist there: JS bindings, memory handling, browser APIs. In Rust use `wasm-bindgen-test`, which runs tests in Node or a headless browser with `wasm-pack test --headless --chrome`.
- **Test from the JS side** with Vitest or Jest running in Node, which supports the `WebAssembly` API. Load the module once in a setup file.
- **End-to-end tests** with Playwright check that the whole page, including loading the `.wasm` file with the right headers, works in real browsers.

## 40: How do you decide if a part of your app should move to WebAssembly?

Start with profiling, not guessing. Move code to Wasm when:

- it is CPU heavy and shows up clearly in the profiler (encoding, parsing, math, simulation)
- there is a mature library in C, C++ or Rust that you want to reuse
- you need predictable performance without JIT warmup and deopt surprises
- the same code has to run on server, mobile and web

Keep it in JavaScript when:

- it mostly works with the DOM, network or JS objects
- it is made of many small calls across the boundary
- the work is light and JS is already fast enough
- the extra download size and build complexity aren't worth it

A good way is to build a small proof of concept, measure real numbers, and then decide.

# Advanced Questions (41-60)

## 41: How does a browser engine compile and run WebAssembly?

The steps in V8 (Chrome, Edge, Node) are roughly:

1. **Decode and validate** the module. Validation checks types, stack usage and control flow for every function in a single pass, so invalid code never runs.
2. **Baseline compile** with Liftoff. It is a fast, simple compiler that produces machine code quickly, so the app starts fast. With streaming APIs this happens while the bytes are still downloading.
3. **Tier up** hot functions with TurboFan, the optimizing compiler. This runs in the background, and once ready, the faster code is used.
4. **Cache** the compiled code so later page loads can skip compilation.

Firefox and Safari use the same idea with their own compilers (a baseline tier plus an optimizing tier). Unlike JavaScript, there is no type speculation, so optimized Wasm code doesn't get thrown away and recompiled because types changed.

## 42: What does it mean that WebAssembly is a stack machine with structured control flow?

Instructions take their operands from an implicit value stack and push results back. `i32.add` pops two `i32` values and pushes the sum. This makes the binary format compact, since most instructions don't need to name registers. The engine turns this into register based machine code during compilation, so there is no real stack at runtime.

Control flow is structured: there is no `goto`. You only have `block`, `loop`, `if`, and branches (`br`, `br_if`, `br_table`) that jump to the end of an enclosing block or the start of an enclosing loop. Because of that:

- a function can be validated in one fast pass
- the stack height and types are known at every point
- code can't jump into the middle of an instruction or to a random address, which is a big part of the security model

Compilers like LLVM use an algorithm (often called relooper or stackifier) to turn arbitrary control flow from C into this structured form.

## 43: How do threads work in WebAssembly?

Wasm threads are built from three parts:

- **Shared memory**: `new WebAssembly.Memory({ initial, maximum, shared: true })`, backed by a `SharedArrayBuffer`. Shared memory must have a maximum.
- **Web Workers**: each thread is a worker with its own instance of the same module, all using the same shared memory.
- **Atomic instructions**: `i32.atomic.rmw.add`, `memory.atomic.wait32`, `memory.atomic.notify` and others, for locks and synchronization.

`SharedArrayBuffer` only works when the page is cross-origin isolated, so the server must send:

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

Check it in JS with `self.crossOriginIsolated`. These headers can break third-party embeds, ads and popups that don't send CORP/CORS headers, which is a common blocker in real projects.

Emscripten supports pthreads with `-pthread` and `-sPTHREAD_POOL_SIZE`. In Rust, threads in the browser need nightly features and extra setup, so many projects use `wasm-bindgen-rayon`. Note that the main browser thread can't block on `memory.atomic.wait`, so locks there have to spin or be avoided.

## 44: What is WebAssembly SIMD and how do you use it?

SIMD (single instruction, multiple data) adds the `v128` type and instructions that work on several values at once, for example 4 floats or 16 bytes in one instruction. It can give big speedups for image processing, audio, video codecs, ML inference and physics.

Enable it at compile time:

```bash
# C/C++
emcc -O3 -msimd128 filter.c -o filter.js

# Rust
RUSTFLAGS="-C target-feature=+simd128" cargo build --release --target wasm32-unknown-unknown
```

Compilers can auto-vectorize simple loops, but for the best results you write intrinsics (`wasm_simd128.h` in C, `core::arch::wasm32` in Rust). Emscripten can also translate many SSE intrinsics.

**Relaxed SIMD**, part of Wasm 3.0, adds faster instructions (like fused multiply-add) whose results can differ slightly between CPUs. It is useful for ML, but not for code that needs bit-for-bit identical results everywhere.

Since older browsers might not support SIMD, ship two builds and pick one with feature detection.

## 45: What is Wasm GC and why does it matter?

Before Wasm GC, languages like Java, Kotlin, Dart or C# had to compile their whole garbage collector into the module and manage objects inside linear memory. That made modules big, and the language GC and the browser GC couldn't see each other, so cycles between JS objects and Wasm objects could leak.

Wasm GC (part of Wasm 3.0, supported in all major browsers) adds `struct` and `array` types that live on the host's GC heap. The browser's own garbage collector manages them. Benefits:

- much smaller modules, since there is no bundled GC
- objects can reference JS objects and back without leaks
- better performance in many cases

Kotlin/Wasm, Dart and Flutter web (`--wasm`), Java through J2CL (used by Google Sheets) and OCaml use it. It is mainly a feature for compiler authors. C, C++ and Rust keep using linear memory.

## 46: How does exception handling work in WebAssembly?

Wasm has native exception instructions. You define **tags** (exception types) and use `throw`, and the current version uses `try_table` with `catch` clauses and an `exnref` value to rethrow (`throw_ref`). This newer design is part of Wasm 3.0. An older version with `try`/`catch`/`delegate` instructions is still supported by browsers because many existing modules use it.

Exceptions can cross the JS boundary: a JS error thrown in an imported function can be caught in Wasm, and a Wasm exception shows up in JS as a `WebAssembly.Exception`.

Before this, Emscripten emulated C++ exceptions by calling into JavaScript `try`/`catch` around every call that might throw, which was slow and made code larger. Today you can use:

```bash
emcc -O3 -fwasm-exceptions app.cpp -o app.js
```

C++ exceptions are disabled by default in Emscripten, so code that relies on them must be built with an exception flag. In Rust, panics are not exceptions; by default they abort, and unwinding in Wasm needs extra flags.

## 47: What is Memory64 and when should you use it?

Memory64 allows a memory to use 64-bit addresses (`i64` instead of `i32`). A regular 32-bit memory is limited to 4 GiB. With Memory64 the theoretical limit is much higher, but browsers still cap it (the JS API limit is 16 GiB). It is part of Wasm 3.0.

Use it only if you really need more than 4 GiB, for example big datasets, large ML models, or CAD and video tools working with huge files.

The downside is speed. With 32-bit memory on 64-bit machines, engines reserve a large virtual address range with guard pages, so bounds checks are almost free (a bad access just hits a guard page). With 64-bit addresses that trick doesn't work, so the engine adds explicit bounds checks on memory access, and pointers take twice the space. Build with `-sMEMORY64` in Emscripten or the `wasm64-unknown-unknown` target in Rust.

## 48: What's new in WebAssembly 3.0?

WebAssembly 3.0 was finalized in September 2025. It collects many features that were developed as separate proposals:

- **Wasm GC**: structs and arrays managed by the host GC
- **Typed function references**: call functions through typed references with `call_ref`, no table needed
- **Exception handling** with `exnref` and `try_table`
- **Memory64**: 64-bit addressing
- **Multiple memories**: one module can have several memories
- **Tail calls**: `return_call` and `return_call_indirect`, important for functional languages
- **Relaxed SIMD**: faster SIMD with some allowed differences between platforms
- **Deterministic profile**: a mode where everything behaves the same on every platform, useful for blockchains or replay
- **JS String Builtins** in the JS API

Wasm 2.0 had already added SIMD, bulk memory operations (`memory.copy`, `memory.fill`), reference types, multi-value returns, sign extension operators and non-trapping float-to-int conversions.

## 49: What is the WebAssembly Component Model?

Core Wasm modules only share numbers and memory. Two modules written in different languages can't easily pass strings, lists or records to each other because each language lays them out in memory in its own way.

The Component Model adds a layer on top of core modules:

- **WIT** (WebAssembly Interface Types) is a language for describing interfaces with rich types like `string`, `list`, `record`, `variant`, `option`, `result` and `resource`.
- A **component** wraps one or more core modules and exposes typed imports and exports.
- The **canonical ABI** defines how those types are copied between components, so a Rust component can call a Python or JS component.

```wit
package example:greeter;

interface greet {
  greet: func(name: string) -> string;
}

world greeter {
  export greet;
}
```

Tools: `wit-bindgen` generates bindings for many languages, `wasm-tools` composes components, and `jco` turns components into JS modules so they can run in browsers and Node. WASI 0.2 and later are built on the Component Model. Browsers don't run components natively yet, so in the browser you go through `jco`.

## 50: What is WASI and how did it change between versions?

WASI (WebAssembly System Interface) is a set of standard APIs for running Wasm outside the browser: files, clocks, random numbers, environment variables, sockets, HTTP. It uses a capability model: a module only gets access to what the host explicitly grants, like a specific directory.

- **WASI Preview 1 (0.1)**: a POSIX-like set of functions imported from `wasi_snapshot_preview1`. Still widely supported (Rust `wasm32-wasip1`, Go `GOOS=wasip1`).
- **WASI 0.2** (January 2024): rebuilt on the Component Model with WIT interfaces like `wasi:cli`, `wasi:filesystem`, `wasi:sockets` and `wasi:http`. Rust target: `wasm32-wasip2`.
- **WASI 0.3** (June 2026): adds native async to the Component Model with `stream` and `future` types, so components can do non-blocking I/O without the workarounds 0.2 needed. Runtimes like Wasmtime support it, and language toolchains are still catching up.

```bash
wasmtime run --dir=./data app.wasm
wasmtime serve http-handler.wasm   # for wasi:http components
```

## 51: What are the limits of the WebAssembly security model?

The sandbox protects the host from the module: a module can't touch memory outside its own, can't call functions it wasn't given, and can't jump to arbitrary code. But it doesn't make the code inside the module safe.

- **Memory bugs still happen inside linear memory.** A buffer overflow in C can overwrite other data in the same memory, like a function table index or a security flag.
- **No memory protections inside the module.** There are no read-only pages, no ASLR, and stack canaries are not on by default, so some exploits are easier than in native code.
- **Imports are the attack surface.** If you give the module a function that runs `eval` or writes `innerHTML`, a bug in the module can become XSS.
- **Side channels** like Spectre apply to Wasm too, which is one reason `SharedArrayBuffer` needs cross-origin isolation.
- **Supply chain**: a `.wasm` file from npm is hard to review. Prefer building from source or trusted publishers.

Treat data coming out of a module like any other untrusted input, and keep the imports minimal.

## 52: How do you detect which Wasm features the browser supports?

Use `WebAssembly.validate` with a tiny module that uses the feature. If the browser doesn't understand the instruction, validation returns `false`. The `wasm-feature-detect` library does this for you:

```js
import { simd, threads, exceptions } from "wasm-feature-detect";

const hasSimd = await simd();
const hasThreads = (await threads()) && self.crossOriginIsolated;

const url = hasSimd ? "/codec.simd.wasm" : "/codec.wasm";
const { instance } = await WebAssembly.instantiateStreaming(
  fetch(url),
  imports,
);
```

A common setup is to build several versions (baseline, SIMD, SIMD with threads) and load the best one. Remember that threads also need the cross-origin isolation headers, not only engine support.

## 53: How do you call async JavaScript APIs from synchronous Wasm code?

C, C++ and Rust code compiled to Wasm is usually synchronous, but many web APIs return promises (`fetch`, IndexedDB, file reading). Options:

- **JSPI (JavaScript Promise Integration)**: lets Wasm suspend while waiting for a promise and continue when it resolves, without changing the code. You wrap the async import with `WebAssembly.Suspending` and the export with `WebAssembly.promising`.

```js
const imports = {
  env: {
    loadData: new WebAssembly.Suspending(async (id) => {
      const res = await fetch(`/data/${id}`);
      return (await res.json()).value;
    }),
  },
};

const { instance } = await WebAssembly.instantiateStreaming(
  fetch("/app.wasm"),
  imports,
);
const run = WebAssembly.promising(instance.exports.run);
const result = await run(); // returns a Promise
```

- **Asyncify** (Emscripten `-sASYNCIFY`, or Binaryen): rewrites the code so it can unwind and rewind the stack. Works everywhere, but makes code bigger and slower. With Emscripten, `-sJSPI` uses JSPI instead where available.
- **Change the design**: have JS do the async work first and then call Wasm with the result, or run Wasm in a worker and block on `Atomics.wait` while another thread does the async work.

JSPI is shipped in Chrome and is coming to other browsers, so check support before relying on it.

## 54: What are JS String Builtins?

For languages that compile with Wasm GC (Kotlin, Dart, Java), strings were a pain. Either they copied every string between a Wasm array and a JS string, or they imported small JS glue functions for each string operation, which the engine couldn't optimize well.

JS String Builtins give Wasm a standard set of imports under `wasm:js-string` (like `length`, `charCodeAt`, `concat`, `substring`, `fromCharCodeArray`) that the engine implements natively and can inline. You turn them on at compile time:

```js
const { instance } = await WebAssembly.instantiateStreaming(
  fetch("/app.wasm"),
  imports,
  {
    builtins: ["js-string"],
  },
);
```

The module keeps strings as `externref` and works with real JS strings, so passing strings to and from the DOM costs almost nothing. For C/C++/Rust that use linear memory, nothing changes; they still encode and decode bytes.

## 55: What is ESM integration for WebAssembly?

The goal is to load Wasm with normal `import` statements instead of `fetch` plus `instantiateStreaming`. There are two parts:

- **Source phase imports** (a TC39 proposal) give you the compiled module, and you instantiate it yourself:

```js
import source wasmModule from "./lib.wasm";

const instance = await WebAssembly.instantiate(wasmModule, imports);
```

- **Full ESM integration**: `import { add } from './lib.wasm'`, where the module's imports are resolved as other ES modules.

This is still being rolled out. Node.js and Deno already support some of it, while browser support is still in progress. Bundlers have had their own version for years (webpack `asyncWebAssembly`, `vite-plugin-wasm`). For code that has to work everywhere today, use the JS API or the glue code your toolchain generates.

## 56: How is memory managed in a Wasm app and how do leaks happen?

For C, C++ and Rust, memory is managed inside linear memory by the language allocator (`malloc`/`free`, Rust's allocator). The browser GC doesn't know about it. Common problems:

- **Forgotten frees across the boundary.** wasm-bindgen gives JS an object for each exported Rust struct. That object holds a pointer into Wasm memory, and you have to call `.free()` when done. wasm-bindgen can use `FinalizationRegistry` as a fallback, but you shouldn't count on it.
- **Memory never shrinks.** If a peak of work grows memory to 1 GiB, it stays at 1 GiB until the instance is dropped, even after everything is freed.
- **Fragmentation** in long-running apps can make memory grow over time.
- **Keeping old instances alive** through closures or event listeners keeps their whole memory alive.

What helps: free objects explicitly (with `using` and `Symbol.dispose` if your bindings support it), reuse buffers instead of allocating per call, and for one-off big jobs, run them in a separate instance or worker and throw it away afterwards.

## 57: What are common performance pitfalls with WebAssembly?

- **Copying data back and forth** between JS and Wasm. Keep data in Wasm memory and pass pointers.
- **Too many small calls** across the boundary instead of batched work.
- **Debug builds**: an unoptimized build can be 10 times slower. Always profile `-O2`/`-O3` or `--release` builds.
- **Big modules** that take a long time to download and compile. Split rarely used features into separate modules and load them lazily.
- **Running on the main thread**, which blocks input and rendering. Use workers.
- **Missing SIMD or threads** when the workload could use them.
- **Memory64** when it isn't needed, which adds bounds-check cost.
- **Asyncify**, which makes code bigger and slower. Prefer JSPI or a different design.
- **Heavy glue code**: wasm-bindgen or Embind conversions on hot paths (strings, `JsValue`, closures) can cost more than the work.

## 58: How is WebAssembly used on the server and at the edge, and how does it compare to containers?

On the server, Wasm is used for serverless functions (Cloudflare Workers, Fastly Compute, Fermyon Spin), plugin systems (Envoy proxy filters, databases, editors like Zed) and sandboxing untrusted code.

Compared to containers:

- **Startup**: Wasm instances start in microseconds to milliseconds, containers take much longer. Good for scale-to-zero and per-request isolation.
- **Size**: modules are often a few MB, while container images are often hundreds of MB.
- **Isolation**: a Wasm sandbox is lightweight and capability based, and a single process can run thousands of instances safely.
- **Portability**: the same `.wasm` file runs on any CPU and OS the runtime supports.

Limits: not every language or library works well under WASI yet, there is less tooling for debugging and monitoring, and you can't run arbitrary Linux software. Containers are still the better choice for full apps with complex dependencies. Docker can run Wasm workloads side by side with containers through containerd shims.

## 59: You need to bring an existing C++ image processing library to a web app. How would you approach it?

1. **Check the library**: dependencies, threading, file system use, SIMD intrinsics, exceptions, and license.
2. **Build it with Emscripten** using its CMake support (`emcmake cmake`, `emmake make`). Fix or disable parts that don't work on the web, like direct file access or OS specific code.
3. **Design a small API**. Don't expose the whole library. Expose a few functions like `processImage(ptr, width, height, options)` with Embind or plain C exports.
4. **Pass pixels efficiently**: get `ImageData` from a canvas, copy its bytes into Wasm memory once, process in place, and read the result back with a `Uint8ClampedArray` view. Or use `OffscreenCanvas` in a worker.
5. **Run it in a worker** so the UI stays responsive.
6. **Turn on `-msimd128`**, and threads if the headers can be set. Ship a fallback build without them.
7. **Optimize size**: `-O3` or `-Oz`, LTO, remove unused parts, Brotli compression, lazy load the module only when the user opens the editor.
8. **Measure**: compare speed with a JS version or a native build, check memory use, and test on low-end mobile devices.

## 60: A Wasm module is slower than expected in production. How do you investigate?

1. **Confirm the build**: check it is an optimized release build and that `wasm-opt` ran. A debug build is a very common cause.
2. **Profile in the browser**: record with the Chrome DevTools Performance panel. Keep the `name` section (or use a build with symbols) so you see real function names.
3. **Split the time**: is it download and compile, JS glue and copying, or the Wasm code itself? Check the Network panel for size and compression, and look for a lot of time in glue functions.
4. **Look at the boundary**: count calls between JS and Wasm, check for string or array conversions on each call, and see if the work can be batched.
5. **Check memory**: frequent `memory.grow` calls, or code recreating typed array views and copying buffers over and over.
6. **Check features**: is the SIMD build actually loaded? Are threads off because the page isn't cross-origin isolated?
7. **Compare with native**: run the same code natively with the same input. If native is slow too, the problem is the algorithm, not Wasm.
8. **Fix and measure again**, one change at a time.
