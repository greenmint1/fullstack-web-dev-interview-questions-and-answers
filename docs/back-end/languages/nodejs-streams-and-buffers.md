# Node.js Streams and Buffers Interview Questions and Answers

_Last updated: November 19, 2026_

150 interview questions with answers about streams and buffers in Node.js, split into three levels: 50 easy, 50 moderate and 50 advanced.

The answers are based on the current Node.js LTS lines (24 and 26). Code examples are ES modules (`.mjs` or `"type": "module"`) and import core modules with the `node:` prefix. Older APIs like `new Buffer()` and `buf.slice()` are mentioned only where you will still see them in real code.

## Table of Contents

- [Easy Questions (1-50)](#easy-questions-1-50)
- [Moderate Questions (51-100)](#moderate-questions-51-100)
- [Advanced Questions (101-150)](#advanced-questions-101-150)

### Easy Questions (1-50)

- [1: What is a Buffer in Node.js?](#1-what-is-a-buffer-in-nodejs)
- [2: Why does Node.js need Buffers when JavaScript already has strings?](#2-why-does-nodejs-need-buffers-when-javascript-already-has-strings)
- [3: How do you create a Buffer?](#3-how-do-you-create-a-buffer)
- [4: What is the difference between Buffer.alloc and Buffer.allocUnsafe?](#4-what-is-the-difference-between-bufferalloc-and-bufferallocunsafe)
- [5: Why is new Buffer() deprecated?](#5-why-is-new-buffer-deprecated)
- [6: How do you convert a Buffer to a string?](#6-how-do-you-convert-a-buffer-to-a-string)
- [7: Which encodings does Buffer support?](#7-which-encodings-does-buffer-support)
- [8: Why can buffer.length differ from string.length?](#8-why-can-bufferlength-differ-from-stringlength)
- [9: How do you get the byte size of a string without creating a Buffer?](#9-how-do-you-get-the-byte-size-of-a-string-without-creating-a-buffer)
- [10: How do you read and write single bytes in a Buffer?](#10-how-do-you-read-and-write-single-bytes-in-a-buffer)
- [11: How do you join several Buffers into one?](#11-how-do-you-join-several-buffers-into-one)
- [12: How do you compare two Buffers?](#12-how-do-you-compare-two-buffers)
- [13: What does buf.subarray() do, and how is it different from buf.slice()?](#13-what-does-bufsubarray-do-and-how-is-it-different-from-bufslice)
- [14: How do you make a real copy of a Buffer?](#14-how-do-you-make-a-real-copy-of-a-buffer)
- [15: How is Buffer related to Uint8Array?](#15-how-is-buffer-related-to-uint8array)
- [16: Do you need to import Buffer?](#16-do-you-need-to-import-buffer)
- [17: How do you read and write numbers in a Buffer?](#17-how-do-you-read-and-write-numbers-in-a-buffer)
- [18: What is endianness?](#18-what-is-endianness)
- [19: How do you convert between base64, hex and text?](#19-how-do-you-convert-between-base64-hex-and-text)
- [20: What happens when you JSON.stringify a Buffer?](#20-what-happens-when-you-jsonstringify-a-buffer)
- [21: How do you search inside a Buffer?](#21-how-do-you-search-inside-a-buffer)
- [22: What is a stream in Node.js?](#22-what-is-a-stream-in-nodejs)
- [23: Why use streams instead of reading everything into memory?](#23-why-use-streams-instead-of-reading-everything-into-memory)
- [24: What are the four types of streams?](#24-what-are-the-four-types-of-streams)
- [25: How do you read a file with a Readable stream?](#25-how-do-you-read-a-file-with-a-readable-stream)
- [26: How do you write to a file with a Writable stream?](#26-how-do-you-write-to-a-file-with-a-writable-stream)
- [27: What is a Duplex stream? Give an example.](#27-what-is-a-duplex-stream-give-an-example)
- [28: What is a Transform stream? Give an example.](#28-what-is-a-transform-stream-give-an-example)
- [29: Which events do streams emit?](#29-which-events-do-streams-emit)
- [30: What is the difference between the end and finish events?](#30-what-is-the-difference-between-the-end-and-finish-events)
- [31: What is the difference between finish and close?](#31-what-is-the-difference-between-finish-and-close)
- [32: What does pipe() do?](#32-what-does-pipe-do)
- [33: What is wrong with pipe() when it comes to errors?](#33-what-is-wrong-with-pipe-when-it-comes-to-errors)
- [34: What is stream.pipeline() and why should you use it?](#34-what-is-streampipeline-and-why-should-you-use-it)
- [35: How do you handle errors in streams?](#35-how-do-you-handle-errors-in-streams)
- [36: How do you read a file line by line?](#36-how-do-you-read-a-file-line-by-line)
- [37: How do you copy a file with streams?](#37-how-do-you-copy-a-file-with-streams)
- [38: Are HTTP requests and responses streams?](#38-are-http-requests-and-responses-streams)
- [39: How do you send a file as an HTTP response using streams?](#39-how-do-you-send-a-file-as-an-http-response-using-streams)
- [40: What is highWaterMark?](#40-what-is-highwatermark)
- [41: What are the default highWaterMark values?](#41-what-are-the-default-highwatermark-values)
- [42: What is object mode?](#42-what-is-object-mode)
- [43: What does Readable.from() do?](#43-what-does-readablefrom-do)
- [44: How do you consume a Readable stream with for await?](#44-how-do-you-consume-a-readable-stream-with-for-await)
- [45: What does write() return?](#45-what-does-write-return)
- [46: What does end() do on a Writable stream?](#46-what-does-end-do-on-a-writable-stream)
- [47: What does setEncoding() do on a Readable stream?](#47-what-does-setencoding-do-on-a-readable-stream)
- [48: Are process.stdin and process.stdout streams?](#48-are-processstdin-and-processstdout-streams)
- [49: How do you stop a stream early?](#49-how-do-you-stop-a-stream-early)
- [50: When should you use fs.readFile and when fs.createReadStream?](#50-when-should-you-use-fsreadfile-and-when-fscreatereadstream)

### Moderate Questions (51-100)

- [51: What is backpressure?](#51-what-is-backpressure)
- [52: How do you handle backpressure when you call write() yourself?](#52-how-do-you-handle-backpressure-when-you-call-write-yourself)
- [53: How does pipe() handle backpressure internally?](#53-how-does-pipe-handle-backpressure-internally)
- [54: What are flowing mode and paused mode?](#54-what-are-flowing-mode-and-paused-mode)
- [55: How do you use the readable event and read()?](#55-how-do-you-use-the-readable-event-and-read)
- [56: What do pause() and resume() do?](#56-what-do-pause-and-resume-do)
- [57: How do you write a custom Readable stream?](#57-how-do-you-write-a-custom-readable-stream)
- [58: How do you write a custom Writable stream?](#58-how-do-you-write-a-custom-writable-stream)
- [59: How do you write a custom Transform stream?](#59-how-do-you-write-a-custom-transform-stream)
- [60: Can you create a stream without writing a class?](#60-can-you-create-a-stream-without-writing-a-class)
- [61: What are _writev, cork() and uncork()?](#61-what-are-_writev-cork-and-uncork)
- [62: What does the allowHalfOpen option do on a Duplex stream?](#62-what-does-the-allowhalfopen-option-do-on-a-duplex-stream)
- [63: What is a PassThrough stream used for?](#63-what-is-a-passthrough-stream-used-for)
- [64: How do you know when a stream is fully done?](#64-how-do-you-know-when-a-stream-is-fully-done)
- [65: How do you use async generators inside pipeline()?](#65-how-do-you-use-async-generators-inside-pipeline)
- [66: What are the Readable helper methods like map and filter?](#66-what-are-the-readable-helper-methods-like-map-and-filter)
- [67: How do you cancel a stream pipeline?](#67-how-do-you-cancel-a-stream-pipeline)
- [68: What are Web Streams, and does Node.js support them?](#68-what-are-web-streams-and-does-nodejs-support-them)
- [69: How do you convert between Node streams and Web Streams?](#69-how-do-you-convert-between-node-streams-and-web-streams)
- [70: What are the main differences between Node streams and Web Streams?](#70-what-are-the-main-differences-between-node-streams-and-web-streams)
- [71: How do you save a fetch() response to a file without loading it all into memory?](#71-how-do-you-save-a-fetch-response-to-a-file-without-loading-it-all-into-memory)
- [72: How do you split a stream into lines when lines can cross chunk boundaries?](#72-how-do-you-split-a-stream-into-lines-when-lines-can-cross-chunk-boundaries)
- [73: What goes wrong if you call chunk.toString() on every chunk of UTF-8 data?](#73-what-goes-wrong-if-you-call-chunktostring-on-every-chunk-of-utf-8-data)
- [74: How do you stream a large JSON array to an HTTP client?](#74-how-do-you-stream-a-large-json-array-to-an-http-client)
- [75: How do you handle a large file upload without buffering it in memory?](#75-how-do-you-handle-a-large-file-upload-without-buffering-it-in-memory)
- [76: How do you stream rows from a database?](#76-how-do-you-stream-rows-from-a-database)
- [77: How does chunked transfer encoding relate to streams?](#77-how-does-chunked-transfer-encoding-relate-to-streams)
- [78: How do you serve a part of a file, for example for video seeking?](#78-how-do-you-serve-a-part-of-a-file-for-example-for-video-seeking)
- [79: How do you calculate a hash of a large file?](#79-how-do-you-calculate-a-hash-of-a-large-file)
- [80: How do you gzip an HTTP response with streams?](#80-how-do-you-gzip-an-http-response-with-streams)
- [81: How do you send one stream to two destinations?](#81-how-do-you-send-one-stream-to-two-destinations)
- [82: What happens when you call destroy() with an error?](#82-what-happens-when-you-call-destroy-with-an-error)
- [83: What do autoDestroy and emitClose do?](#83-what-do-autodestroy-and-emitclose-do)
- [84: How do you check how full a stream's buffer is?](#84-how-do-you-check-how-full-a-streams-buffer-is)
- [85: What is the Buffer pool?](#85-what-is-the-buffer-pool)
- [86: Does Buffer.from(arrayBuffer) copy the data?](#86-does-bufferfromarraybuffer-copy-the-data)
- [87: When would you use TextEncoder and TextDecoder instead of Buffer?](#87-when-would-you-use-textencoder-and-textdecoder-instead-of-buffer)
- [88: What are Blob and File in Node.js?](#88-what-are-blob-and-file-in-nodejs)
- [89: How do you check if a value is a Buffer, or if bytes are valid UTF-8?](#89-how-do-you-check-if-a-value-is-a-buffer-or-if-bytes-are-valid-utf-8)
- [90: Why should you use crypto.timingSafeEqual to compare secrets?](#90-why-should-you-use-cryptotimingsafeequal-to-compare-secrets)
- [91: How do you parse a binary header with Buffer methods?](#91-how-do-you-parse-a-binary-header-with-buffer-methods)
- [92: How do you read and write 64-bit integers in a Buffer?](#92-how-do-you-read-and-write-64-bit-integers-in-a-buffer)
- [93: How do you write data with a known length into a pre-allocated Buffer?](#93-how-do-you-write-data-with-a-known-length-into-a-pre-allocated-buffer)
- [94: How do you test a stream?](#94-how-do-you-test-a-stream)
- [95: What is node:stream/consumers?](#95-what-is-nodestreamconsumers)
- [96: Why would a stream pipeline hang and never finish?](#96-why-would-a-stream-pipeline-hang-and-never-finish)
- [97: What is the problem with an async function as a data event handler?](#97-what-is-the-problem-with-an-async-function-as-a-data-event-handler)
- [98: How do you use streams with child processes?](#98-how-do-you-use-streams-with-child-processes)
- [99: What can cause a memory leak when working with streams?](#99-what-can-cause-a-memory-leak-when-working-with-streams)
- [100: How do you count bytes or show progress while streaming?](#100-how-do-you-count-bytes-or-show-progress-while-streaming)

### Advanced Questions (101-150)

- [101: How does a Readable stream's internal buffer work?](#101-how-does-a-readable-streams-internal-buffer-work)
- [102: How does a Writable stream buffer writes?](#102-how-does-a-writable-stream-buffer-writes)
- [103: Is highWaterMark a hard memory limit?](#103-is-highwatermark-a-hard-memory-limit)
- [104: How do you choose a good highWaterMark?](#104-how-do-you-choose-a-good-highwatermark)
- [105: What is tricky about backpressure in object mode?](#105-what-is-tricky-about-backpressure-in-object-mode)
- [106: How does backpressure work with async generators in pipeline()?](#106-how-does-backpressure-work-with-async-generators-in-pipeline)
- [107: Why does pipe() leak resources on errors and pipeline() does not?](#107-why-does-pipe-leak-resources-on-errors-and-pipeline-does-not)
- [108: What are _construct and _destroy used for?](#108-what-are-_construct-and-_destroy-used-for)
- [109: What is _final in a Writable?](#109-what-is-_final-in-a-writable)
- [110: How is a Transform different from a Duplex internally?](#110-how-is-a-transform-different-from-a-duplex-internally)
- [111: How do you write a Transform that limits throughput, for example to 1 MB per second?](#111-how-do-you-write-a-transform-that-limits-throughput-for-example-to-1-mb-per-second)
- [112: How do you batch objects into groups in a stream?](#112-how-do-you-batch-objects-into-groups-in-a-stream)
- [113: How do you process stream items in parallel but with a limit?](#113-how-do-you-process-stream-items-in-parallel-but-with-a-limit)
- [114: Does parallel processing in a stream keep the order?](#114-does-parallel-processing-in-a-stream-keep-the-order)
- [115: What happens when one source is piped to a fast and a slow destination?](#115-what-happens-when-one-source-is-piped-to-a-fast-and-a-slow-destination)
- [116: What is stream.compose()?](#116-what-is-streamcompose)
- [117: What does Duplex.from() do?](#117-what-does-duplexfrom-do)
- [118: What happens to a stream when you break out of a for await loop?](#118-what-happens-to-a-stream-when-you-break-out-of-a-for-await-loop)
- [119: Why shouldn't you mix data events and async iteration on the same stream?](#119-why-shouldnt-you-mix-data-events-and-async-iteration-on-the-same-stream)
- [120: What does Readable.from('some string') emit?](#120-what-does-readablefromsome-string-emit)
- [121: How can a small Buffer keep a lot of memory alive?](#121-how-can-a-small-buffer-keep-a-lot-of-memory-alive)
- [122: Where is Buffer memory stored, and how do you measure it?](#122-where-is-buffer-memory-stored-and-how-do-you-measure-it)
- [123: What is the maximum size of a Buffer or a string?](#123-what-is-the-maximum-size-of-a-buffer-or-a-string)
- [124: What are the security risks of Buffer.allocUnsafe?](#124-what-are-the-security-risks-of-bufferallocunsafe)
- [125: What happens when you decode invalid UTF-8 or use the wrong encoding?](#125-what-happens-when-you-decode-invalid-utf-8-or-use-the-wrong-encoding)
- [126: How do you pass a Buffer to a worker thread without copying it?](#126-how-do-you-pass-a-buffer-to-a-worker-thread-without-copying-it)
- [127: When would you use SharedArrayBuffer instead of transferring?](#127-when-would-you-use-sharedarraybuffer-instead-of-transferring)
- [128: How would you design a pipeline that processes a 50 GB CSV file?](#128-how-would-you-design-a-pipeline-that-processes-a-50-gb-csv-file)
- [129: How do you stream a large database export as a download and handle the client leaving halfway?](#129-how-do-you-stream-a-large-database-export-as-a-download-and-handle-the-client-leaving-halfway)
- [130: How do you detect that a client disconnected during a streaming response?](#130-how-do-you-detect-that-a-client-disconnected-during-a-streaming-response)
- [131: How do you handle a stalled upload or download?](#131-how-do-you-handle-a-stalled-upload-or-download)
- [132: How do you limit the size of a streamed upload?](#132-how-do-you-limit-the-size-of-a-streamed-upload)
- [133: How does the order of events go for a Transform in a pipeline that finishes normally?](#133-how-does-the-order-of-events-go-for-a-transform-in-a-pipeline-that-finishes-normally)
- [134: How do you proxy an HTTP request to another server with streams?](#134-how-do-you-proxy-an-http-request-to-another-server-with-streams)
- [135: How do you implement Server-Sent Events with Node streams?](#135-how-do-you-implement-server-sent-events-with-node-streams)
- [136: Why can compression break streaming responses like SSE?](#136-why-can-compression-break-streaming-responses-like-sse)
- [137: What is the performance cost of object mode and small chunks?](#137-what-is-the-performance-cost-of-object-mode-and-small-chunks)
- [138: What happens if a transform does CPU-heavy work?](#138-what-happens-if-a-transform-does-cpu-heavy-work)
- [139: When should you choose Web Streams over Node streams in a Node.js app?](#139-when-should-you-choose-web-streams-over-node-streams-in-a-nodejs-app)
- [140: What are byte streams and BYOB readers in Web Streams?](#140-what-are-byte-streams-and-byob-readers-in-web-streams)
- [141: How do you parse a length-prefixed binary protocol from a stream?](#141-how-do-you-parse-a-length-prefixed-binary-protocol-from-a-stream)
- [142: What is the problem with calling Buffer.concat on every chunk in a parser?](#142-what-is-the-problem-with-calling-bufferconcat-on-every-chunk-in-a-parser)
- [143: When does a Readable start flowing, and can you lose data?](#143-when-does-a-readable-start-flowing-and-can-you-lose-data)
- [144: What do ERR_STREAM_PREMATURE_CLOSE and ERR_STREAM_WRITE_AFTER_END mean?](#144-what-do-err_stream_premature_close-and-err_stream_write_after_end-mean)
- [145: Are writes to process.stdout synchronous?](#145-are-writes-to-processstdout-synchronous)
- [146: How do you test that your stream code respects backpressure?](#146-how-do-you-test-that-your-stream-code-respects-backpressure)
- [147: Show a common way to accidentally ignore backpressure in a custom Readable.](#147-show-a-common-way-to-accidentally-ignore-backpressure-in-a-custom-readable)
- [148: How would you build resumable downloads with streams?](#148-how-would-you-build-resumable-downloads-with-streams)
- [149: How do you debug which step in a long pipeline is slow?](#149-how-do-you-debug-which-step-in-a-long-pipeline-is-slow)
- [150: An API service runs out of memory when users download large reports. How would you investigate and fix it?](#150-an-api-service-runs-out-of-memory-when-users-download-large-reports-how-would-you-investigate-and-fix-it)

---

# Easy Questions (1-50)

## 1: What is a Buffer in Node.js?

A Buffer is a fixed-size chunk of memory that holds raw bytes. You use it when you work with binary data: file contents, network packets, images, compressed data and so on.

Each item in a Buffer is one byte, a number from 0 to 255. Once a Buffer is created, its size can't change.

## 2: Why does Node.js need Buffers when JavaScript already has strings?

JavaScript strings are made for text. They are stored as UTF-16 and you can't safely put arbitrary bytes in them. Files, sockets and crypto functions work with bytes, not text.

Node added Buffer early on to fill this gap, before JavaScript had typed arrays. Today Buffer is built on top of `Uint8Array`, but it still adds many helpers for encodings and reading numbers.

## 3: How do you create a Buffer?

There are three main ways:

```js
const a = Buffer.from("hello"); // from a string (UTF-8 by default)
const b = Buffer.from([1, 2, 3]); // from an array of bytes
const c = Buffer.alloc(10); // 10 bytes, all set to 0
const d = Buffer.allocUnsafe(10); // 10 bytes, not cleared
```

`Buffer.from()` also accepts another Buffer (it copies it) and an `ArrayBuffer` (it shares memory with it).

## 4: What is the difference between Buffer.alloc and Buffer.allocUnsafe?

`Buffer.alloc(size)` gives you memory filled with zeros. `Buffer.allocUnsafe(size)` gives you memory that is not cleared, so it can contain old data from other parts of the process.

`allocUnsafe` is faster because it skips the zero-fill step. Use it only if you are going to overwrite every byte right away. Otherwise you can leak old data (for example, parts of earlier requests) to a client.

## 5: Why is new Buffer() deprecated?

`new Buffer(x)` did different things depending on the type of `x`. With a number it allocated memory that was not cleared. If user input like a JSON number reached that call by mistake, the app could return uninitialized memory. This was a real security problem.

It was replaced by `Buffer.from()`, `Buffer.alloc()` and `Buffer.allocUnsafe()`, which make the intent clear. `new Buffer()` still works but prints a deprecation warning (DEP0005).

## 6: How do you convert a Buffer to a string?

Call `toString()` with an encoding. The default is UTF-8.

```js
const buf = Buffer.from("héllo");
buf.toString(); // 'héllo'
buf.toString("hex"); // '68c3a96c6c6f'
buf.toString("base64"); // 'aMOpbGxv'
buf.toString("utf8", 0, 1); // 'h' (only bytes 0 to 1)
```

## 7: Which encodings does Buffer support?

The common ones are `utf8` (the default), `hex`, `base64`, `base64url`, `latin1` (also called `binary`), `ascii` and `utf16le` (also `ucs2`).

You can check a name with `Buffer.isEncoding('utf8')`. If you pick the wrong encoding, you don't get an error, you just get the wrong text, so be careful when you decode.

## 8: Why can buffer.length differ from string.length?

`string.length` counts UTF-16 code units, while `buffer.length` counts bytes. Many characters take more than one byte in UTF-8.

```js
const s = "héllo";
s.length; // 5
Buffer.from(s).length; // 6, because 'é' takes 2 bytes
```

This matters for things like the `Content-Length` header, which must be in bytes.

## 9: How do you get the byte size of a string without creating a Buffer?

Use `Buffer.byteLength()`:

```js
Buffer.byteLength("héllo"); // 6
Buffer.byteLength("aGVsbG8=", "base64"); // 5
```

It is the right way to set `Content-Length` for a string body.

## 10: How do you read and write single bytes in a Buffer?

Use index access, like with an array:

```js
const buf = Buffer.alloc(3);
buf[0] = 65;
buf[1] = 256; // stored as 0, values wrap around modulo 256
buf[2] = -1; // stored as 255
console.log(buf); // <Buffer 41 00 ff>
```

Reading past the end returns `undefined`, and writing past the end is silently ignored. The Buffer does not grow.

## 11: How do you join several Buffers into one?

Use `Buffer.concat()`:

```js
const parts = [Buffer.from("foo"), Buffer.from("bar")];
const all = Buffer.concat(parts); // <Buffer 66 6f 6f 62 61 72>
```

If you already know the total length, pass it as the second argument to save a loop over the list. A common pattern is to collect chunks from a stream in an array and call `Buffer.concat()` once at the end.

## 12: How do you compare two Buffers?

`a.equals(b)` returns `true` if both have the same bytes. `Buffer.compare(a, b)` (or `a.compare(b)`) returns `-1`, `0` or `1`, which makes it usable for sorting.

```js
Buffer.from("abc").equals(Buffer.from("abc")); // true
[bufB, bufA].sort(Buffer.compare);
```

Don't use `===`. It compares references, not content. For secrets like tokens, use `crypto.timingSafeEqual()` instead (see question 90).

## 13: What does buf.subarray() do, and how is it different from buf.slice()?

`buf.subarray(start, end)` returns a new Buffer that points to the same memory. No bytes are copied, so changing one changes the other.

```js
const buf = Buffer.from("hello");
const part = buf.subarray(0, 2);
part[0] = 72; // 'H'
buf.toString(); // 'Hello'
```

`buf.slice()` does the same thing on Buffers, but it is deprecated in the docs because `Uint8Array.prototype.slice()` makes a copy and the two behave differently. Use `subarray()` in new code.

## 14: How do you make a real copy of a Buffer?

```js
const copy = Buffer.from(original); // new memory, same bytes
```

Or copy into an existing Buffer with `copy()`:

```js
const target = Buffer.alloc(10);
source.copy(target, 0, 0, 5); // targetStart, sourceStart, sourceEnd
```

## 15: How is Buffer related to Uint8Array?

`Buffer` is a subclass of `Uint8Array`. Every Buffer is a `Uint8Array`, so you can pass a Buffer to any API that expects a `Uint8Array`.

Buffer adds Node specific methods like `toString(encoding)`, `readUInt32BE()` and `equals()`. The other way around does not work: a plain `Uint8Array` does not have those methods, but you can wrap it without copying with `Buffer.from(u8.buffer, u8.byteOffset, u8.byteLength)`.

## 16: Do you need to import Buffer?

No. `Buffer` is a global. Still, many code bases import it to make the dependency clear and to keep linters happy:

```js
import { Buffer } from "node:buffer";
```

The `node:buffer` module also exports other things, like `Blob`, `constants` and `isUtf8()`.

## 17: How do you read and write numbers in a Buffer?

Buffer has methods for each number type and byte order. `BE` means big-endian, `LE` means little-endian.

```js
const buf = Buffer.alloc(6);
buf.writeUInt16BE(500, 0);
buf.writeInt32LE(-42, 2);

buf.readUInt16BE(0); // 500
buf.readInt32LE(2); // -42
```

There are also `readFloatLE`, `readDoubleBE`, `readBigUInt64LE` and others. They throw a `RangeError` if you read past the end.

## 18: What is endianness?

It is the order in which the bytes of a multi-byte number are stored. Big-endian puts the most significant byte first. Little-endian puts it last.

The number `0x1234` is `12 34` in big-endian and `34 12` in little-endian. Network protocols usually use big-endian. Most CPUs (x86, ARM) use little-endian. When you parse a binary format, check its spec for the byte order.

## 19: How do you convert between base64, hex and text?

Go through a Buffer:

```js
const b64 = Buffer.from("hello").toString("base64"); // 'aGVsbG8='
const text = Buffer.from(b64, "base64").toString("utf8"); // 'hello'
const hex = Buffer.from("hello").toString("hex"); // '68656c6c6f'
const url = Buffer.from("hi?").toString("base64url"); // 'aGk_', safe for URLs
```

`base64url` uses `-` and `_` instead of `+` and `/` and drops the `=` padding. JWTs use it.

## 20: What happens when you JSON.stringify a Buffer?

You get an object with a `type` and a `data` array:

```js
JSON.stringify(Buffer.from("hi"));
// '{"type":"Buffer","data":[104,105]}'
```

This is big and slow for binary data. If you need to send bytes in JSON, convert them to base64 first.

## 21: How do you search inside a Buffer?

Buffer has `indexOf()`, `lastIndexOf()` and `includes()`. They accept a string, a number or another Buffer.

```js
const buf = Buffer.from("a,b,c");
buf.indexOf(","); // 1
buf.includes("c"); // true
buf.indexOf(0x2c, 2); // 3, search for byte 0x2c starting at index 2
```

`fill()` sets all bytes (or a range) to a value, for example `buf.fill(0)`.

## 22: What is a stream in Node.js?

A stream is a way to handle data piece by piece instead of all at once. The data arrives (or leaves) in chunks, and you process each chunk as it comes.

For example, instead of reading a 2 GB log file into memory, you read it in 64 KiB chunks. Memory use stays small, and you can start working on the first chunk before the rest is read.

## 23: Why use streams instead of reading everything into memory?

- Memory: you only keep a few chunks in memory, not the whole file or response.
- Speed to first byte: you can start sending or processing data right away.
- Composability: you can connect small steps (read, unzip, parse, write) into a chain.
- Backpressure: a fast producer slows down when the consumer can't keep up.

For small files or bodies, reading everything at once is simpler and fine.

## 24: What are the four types of streams?

- Readable: you read data from it. Example: `fs.createReadStream()`, an HTTP request on the server.
- Writable: you write data to it. Example: `fs.createWriteStream()`, an HTTP response on the server.
- Duplex: both readable and writable, and the two sides are independent. Example: a TCP socket.
- Transform: a duplex stream where the output is computed from the input. Example: `zlib.createGzip()`.

## 25: How do you read a file with a Readable stream?

```js
import { createReadStream } from "node:fs";

const stream = createReadStream("big.log", { encoding: "utf8" });

stream.on("data", (chunk) => {
  console.log("got", chunk.length, "characters");
});
stream.on("end", () => console.log("done"));
stream.on("error", (err) => console.error(err));
```

Without the `encoding` option, chunks are Buffers.

## 26: How do you write to a file with a Writable stream?

```js
import { createWriteStream } from "node:fs";

const out = createWriteStream("out.txt");
out.write("first line\n");
out.write("second line\n");
out.end("last line\n");

out.on("finish", () => console.log("all data written"));
out.on("error", (err) => console.error(err));
```

Use the `flags: 'a'` option to append instead of overwrite.

## 27: What is a Duplex stream? Give an example.

A Duplex stream has a readable side and a writable side that work independently. What you write is not directly what you read.

A TCP socket is the classic example. You write bytes that go to the other machine, and you read bytes that the other machine sends back.

```js
import net from "node:net";

const socket = net.connect(80, "example.com");
socket.write(
  "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n",
);
socket.on("data", (chunk) => process.stdout.write(chunk));
```

## 28: What is a Transform stream? Give an example.

A Transform is a Duplex where the output depends on the input. You write data in, it changes the data, and you read the result out.

Examples: `zlib.createGzip()` compresses, `crypto.createCipheriv()` encrypts, and a custom transform could turn text to uppercase or parse CSV lines.

## 29: Which events do streams emit?

Streams are EventEmitters. The common events are:

- Readable: `data`, `end`, `readable`, `error`, `close`, `pause`, `resume`.
- Writable: `drain`, `finish`, `error`, `close`, `pipe`, `unpipe`.

`error` is the most important one to handle. An `error` event with no listener crashes the process.

## 30: What is the difference between the end and finish events?

`end` is emitted by a Readable when there is no more data to read. `finish` is emitted by a Writable after you called `end()` and all data was flushed to the underlying system.

A Duplex or Transform can emit both, one for each side.

## 31: What is the difference between finish and close?

`finish` means all data was written. `close` means the stream and its underlying resource (like a file descriptor) are closed. `close` usually comes after `finish` and is the last event.

If a stream is destroyed early, you may get `close` without `finish` or `end`. That is how you can tell a stream was cut off.

## 32: What does pipe() do?

`readable.pipe(writable)` takes everything from a readable stream and writes it to a writable stream. It also handles backpressure: it pauses the readable when the writable is full and resumes it on `drain`.

```js
createReadStream("in.txt").pipe(createWriteStream("out.txt"));
```

It returns the destination, so you can chain: `a.pipe(gzip).pipe(out)`.

## 33: What is wrong with pipe() when it comes to errors?

`pipe()` does not forward errors. If the source fails, the destination is not closed. If the destination fails, the source keeps the file open. You need an `error` handler on every stream in the chain, and you have to clean up by hand. This often leads to leaked file descriptors.

That is why `pipeline()` exists.

## 34: What is stream.pipeline() and why should you use it?

`pipeline()` connects streams like `pipe()`, but also handles errors and cleanup. If any stream fails, it destroys all of them and gives you the error once.

The promise version is the easiest to use:

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";
import { createGzip } from "node:zlib";

await pipeline(
  createReadStream("app.log"),
  createGzip(),
  createWriteStream("app.log.gz"),
);
console.log("compressed");
```

There is also a callback version in `node:stream`. Use `pipeline()` by default in new code.

## 35: How do you handle errors in streams?

- With `pipeline()`: wrap it in `try/catch` (promise version) or check the callback's error.
- With single streams: add an `error` listener.
- In async iteration: errors are thrown inside `for await`, so use `try/catch`.

```js
try {
  for await (const chunk of createReadStream("missing.txt")) {
    console.log(chunk);
  }
} catch (err) {
  console.error("read failed:", err.code); // ENOENT
}
```

## 36: How do you read a file line by line?

Use `node:readline` with a read stream:

```js
import { createReadStream } from "node:fs";
import { createInterface } from "node:readline";

const rl = createInterface({
  input: createReadStream("data.txt"),
  crlfDelay: Infinity, // treat \r\n as one line break
});

for await (const line of rl) {
  console.log(line);
}
```

It reads the file in chunks and splits it into lines for you.

## 37: How do you copy a file with streams?

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";

await pipeline(createReadStream("a.mp4"), createWriteStream("b.mp4"));
```

For a plain copy, `fs.promises.copyFile()` is simpler and can use OS level copy. Streams make sense when you also want to change the data or track progress.

## 38: Are HTTP requests and responses streams?

Yes. On the server, `req` is a Readable stream (the request body) and `res` is a Writable stream (the response body). On the client side it's the other way around.

```js
import http from "node:http";

http
  .createServer(async (req, res) => {
    let size = 0;
    for await (const chunk of req) size += chunk.length;
    res.end(`got ${size} bytes\n`);
  })
  .listen(3000);
```

## 39: How do you send a file as an HTTP response using streams?

```js
import http from "node:http";
import { createReadStream } from "node:fs";
import { pipeline } from "node:stream/promises";

http
  .createServer(async (req, res) => {
    res.setHeader("Content-Type", "video/mp4");
    try {
      await pipeline(createReadStream("movie.mp4"), res);
    } catch (err) {
      console.error("stream failed:", err.code);
    }
  })
  .listen(3000);
```

The file is sent chunk by chunk, so a 4 GB file does not need 4 GB of memory. If the client disconnects, `pipeline()` closes the file.

## 40: What is highWaterMark?

`highWaterMark` is the amount of data a stream buffers before it tells the producer to stop. For a Readable it is how much it reads ahead. For a Writable it is how much it accepts before `write()` returns `false`.

It is a threshold, not a hard limit. You can still push more data past it, but the stream signals that you should wait.

## 41: What are the default highWaterMark values?

- Byte streams: 64 KiB since Node.js 22 (it was 16 KiB before).
- `fs.createReadStream()`: 64 KiB (this was already the default).
- Object mode streams: 16 objects.

You can set it per stream with the `highWaterMark` option, and you can read or change the global default with `stream.getDefaultHighWaterMark()` and `stream.setDefaultHighWaterMark()`.

## 42: What is object mode?

By default, streams only carry Buffers, strings or `Uint8Array`s. In object mode, a stream can carry any JavaScript value, like objects from a database or parsed JSON lines.

```js
import { Readable } from "node:stream";

const users = new Readable({
  objectMode: true,
  read() {
    this.push({ id: 1, name: "Ana" });
    this.push(null); // end of stream
  },
});
```

In object mode `highWaterMark` counts objects, not bytes.

## 43: What does Readable.from() do?

It creates a Readable stream from an iterable or async iterable, like an array or an async generator. It uses object mode by default.

```js
import { Readable } from "node:stream";

const stream = Readable.from(["a", "b", "c"]);

async function* numbers() {
  for (let i = 0; i < 3; i++) yield i;
}
const numStream = Readable.from(numbers());
```

It is very handy for tests and for turning generator code into a stream.

## 44: How do you consume a Readable stream with for await?

Readable streams are async iterables, so `for await` works:

```js
for await (const chunk of createReadStream("file.txt")) {
  console.log(chunk.length);
}
```

This is the simplest way to read a stream. It handles backpressure for you, because the next chunk is only read after your loop body finishes, and errors are thrown as exceptions.

## 45: What does write() return?

`writable.write(chunk)` returns `true` if the internal buffer is still under `highWaterMark`, and `false` if it is full.

`false` does not mean the write failed. The chunk is accepted and buffered. It means "please stop writing until the `drain` event". Ignoring it is how apps run out of memory (see question 51).

## 46: What does end() do on a Writable stream?

`writable.end()` says "no more data is coming". You can pass a last chunk: `end('bye')`. After all buffered data is written, the stream emits `finish`.

Calling `write()` after `end()` gives an `ERR_STREAM_WRITE_AFTER_END` error.

## 47: What does setEncoding() do on a Readable stream?

It makes the stream emit strings instead of Buffers, decoded with the given encoding.

```js
const stream = createReadStream("notes.txt");
stream.setEncoding("utf8");
stream.on("data", (chunk) => console.log(typeof chunk)); // 'string'
```

It is better than calling `chunk.toString()` yourself, because it correctly handles characters that are split between two chunks (see question 73).

## 48: Are process.stdin and process.stdout streams?

Yes. `process.stdin` is a Readable, and `process.stdout` and `process.stderr` are Writables. That is why you can pipe them:

```js
import { pipeline } from "node:stream/promises";
import { createGzip } from "node:zlib";

// cat file.txt | node gzip.mjs > file.txt.gz
await pipeline(process.stdin, createGzip(), process.stdout);
```

## 49: How do you stop a stream early?

Call `stream.destroy()`. It stops reading or writing and releases the underlying resource. You can pass an error, `stream.destroy(err)`, and it will be emitted as an `error` event.

When you `break` out of a `for await` loop over a stream, the stream is destroyed for you.

## 50: When should you use fs.readFile and when fs.createReadStream?

Use `fs.readFile()` (or `fs.promises.readFile()`) for small files that you need as a whole, like a config file or a small JSON file. It's simple and fast.

Use `fs.createReadStream()` for large files, for files of unknown size, or when you want to send the data somewhere (an HTTP response, a compressor) while you read it. A good rule: if the file can be bigger than a few megabytes, or there can be many of them in parallel, stream it.

# Moderate Questions (51-100)

## 51: What is backpressure?

Backpressure is what happens when data comes in faster than it can go out. For example, you read a file from a fast SSD and send it to a slow client. If nothing slows the reader down, the data piles up in memory until the process crashes.

Streams solve this with a signal: `write()` returns `false` when the writable's buffer is full, and the producer should stop until the `drain` event. `pipe()`, `pipeline()` and `for await` do this for you. When you call `write()` by hand, you have to do it yourself.

## 52: How do you handle backpressure when you call write() yourself?

Check the return value and wait for `drain`:

```js
import { createWriteStream } from "node:fs";
import { once } from "node:events";

const out = createWriteStream("numbers.txt");

for (let i = 0; i < 10_000_000; i++) {
  if (!out.write(`${i}\n`)) {
    await once(out, "drain"); // wait until the buffer is empty again
  }
}
out.end();
await once(out, "finish");
```

Without the `await once(out, 'drain')` line, this loop would buffer millions of strings in memory.

## 53: How does pipe() handle backpressure internally?

`pipe()` listens to `data` on the source and calls `dest.write(chunk)`. When `write()` returns `false`, it calls `source.pause()`. When the destination emits `drain`, it calls `source.resume()`.

So the source only reads as fast as the destination can write. `pipeline()` uses the same logic underneath and adds error handling and cleanup.

## 54: What are flowing mode and paused mode?

A Readable stream is in one of two modes:

- Paused mode: data waits in the internal buffer until you call `read()`. This is the starting mode.
- Flowing mode: data is pushed to you through `data` events as fast as it arrives.

A stream switches to flowing mode when you add a `data` listener, call `resume()` or call `pipe()`. It goes back to paused mode when you call `pause()` (if there are no pipe destinations) or remove the pipes.

## 55: How do you use the readable event and read()?

The `readable` event fires when there is data in the buffer (or the stream ended). You then pull data with `read()` until it returns `null`.

```js
const stream = createReadStream("file.bin");

stream.on("readable", () => {
  let chunk;
  while ((chunk = stream.read()) !== null) {
    console.log("read", chunk.length, "bytes");
  }
});
stream.on("end", () => console.log("done"));
```

You can pass a size, `read(4)`, to get exactly 4 bytes. That is useful for parsing binary headers. In most code `for await` is simpler.

## 56: What do pause() and resume() do?

`pause()` stops a flowing stream from emitting `data` events. The data stays in the internal buffer, and once the buffer is full the stream stops reading from the source. `resume()` starts the flow again.

They are useful if you do async work per chunk with `data` events:

```js
stream.on("data", async (chunk) => {
  stream.pause();
  await saveToDb(chunk);
  stream.resume();
});
```

With `for await` you don't need this, because the loop waits for your code.

## 57: How do you write a custom Readable stream?

Extend `Readable` and implement `_read()`. Call `this.push(data)` to add data and `this.push(null)` to end the stream.

```js
import { Readable } from "node:stream";

class Counter extends Readable {
  constructor(max) {
    super();
    this.n = 0;
    this.max = max;
  }

  _read() {
    this.n += 1;
    if (this.n > this.max) {
      this.push(null);
    } else {
      this.push(`${this.n}\n`);
    }
  }
}

new Counter(5).pipe(process.stdout);
```

Node calls `_read()` whenever it wants more data. If `push()` returns `false`, stop pushing until `_read()` is called again.

## 58: How do you write a custom Writable stream?

Implement `_write(chunk, encoding, callback)` and call `callback()` when you are done with the chunk. Pass an error to the callback if it failed.

```js
import { Writable } from "node:stream";

class DbWriter extends Writable {
  constructor(db) {
    super({ objectMode: true });
    this.db = db;
  }

  _write(row, encoding, callback) {
    this.db.insert(row).then(() => callback(), callback);
  }
}
```

Node will not call `_write()` again until you call the callback, so writes happen one at a time and in order.

## 59: How do you write a custom Transform stream?

Implement `_transform(chunk, encoding, callback)`. Push zero or more output chunks and then call the callback. Optionally implement `_flush(callback)` to push data at the very end.

```js
import { Transform } from "node:stream";

class Upper extends Transform {
  _transform(chunk, encoding, callback) {
    callback(null, chunk.toString().toUpperCase());
  }
}

process.stdin.pipe(new Upper()).pipe(process.stdout);
```

`callback(null, data)` is a shortcut for `this.push(data); callback();`.

## 60: Can you create a stream without writing a class?

Yes. Pass the methods as options to the constructor:

```js
import { Transform } from "node:stream";

const toJsonLines = new Transform({
  objectMode: true,
  transform(obj, encoding, callback) {
    callback(null, JSON.stringify(obj) + "\n");
  },
});
```

The same works for `new Readable({ read() {} })`, `new Writable({ write() {} })` and `new Duplex({ read() {}, write() {} })`. Inside these functions `this` is the stream, so don't use arrow functions if you need `this`.

## 61: What are _writev, cork() and uncork()?

`_writev(chunks, callback)` lets a Writable handle many buffered chunks in one call. This is useful if one big write is cheaper than many small ones, like one network packet or one batch insert.

`cork()` tells the stream to buffer writes instead of sending them. `uncork()` flushes them, and if `_writev` exists, they go out in one call.

```js
socket.cork();
socket.write("header\r\n");
socket.write("body\r\n");
process.nextTick(() => socket.uncork());
```

Calling `uncork()` in `process.nextTick()` lets all writes from the same tick be grouped.

## 62: What does the allowHalfOpen option do on a Duplex stream?

With `allowHalfOpen: true` (the default), one side can end while the other stays open. For a TCP socket it means the other side can stop sending, and you can still send your reply.

With `allowHalfOpen: false`, when the readable side ends, the writable side ends too. `net.createServer()` has its own `allowHalfOpen` option for sockets, which is `false` by default.

## 63: What is a PassThrough stream used for?

`PassThrough` is a Transform that outputs exactly what it gets. It is useful as a placeholder or a connector:

- Return a stream right away from a function and fill it later.
- Spy on data in a pipeline, for example to count bytes.
- Give tests a stream they can write to and read from.

```js
import { PassThrough } from "node:stream";

function startDownload() {
  const out = new PassThrough();
  fetchSomehow().then(
    (src) => src.pipe(out),
    (err) => out.destroy(err),
  );
  return out;
}
```

## 64: How do you know when a stream is fully done?

Use `finished()`. It waits until the stream has ended, finished or failed, and handles all the edge cases (like `close` without `end`).

```js
import { finished } from "node:stream/promises";

const out = createWriteStream("log.txt");
out.end("bye\n");
await finished(out);
console.log("file is written");
```

It rejects if the stream errors or closes too early (`ERR_STREAM_PREMATURE_CLOSE`).

## 65: How do you use async generators inside pipeline()?

`pipeline()` accepts async generator functions as steps. Each one gets the previous stream as an async iterable and yields new values:

```js
import { pipeline } from "node:stream/promises";
import { createReadStream, createWriteStream } from "node:fs";

await pipeline(
  createReadStream("in.txt", { encoding: "utf8" }),
  async function* (source) {
    for await (const chunk of source) {
      yield chunk.toUpperCase();
    }
  },
  createWriteStream("out.txt"),
);
```

This is often easier to read than a Transform class, and backpressure still works because the generator only runs when the next step asks for data.

## 66: What are the Readable helper methods like map and filter?

Readable streams have array-like helpers: `map()`, `filter()`, `forEach()`, `toArray()`, `some()`, `every()`, `find()`, `reduce()`, `flatMap()`, `drop()` and `take()`. `map` and `filter` return new streams. Check their stability in the docs for your Node version, some of them are still marked experimental.

```js
import { Readable } from "node:stream";

const result = await Readable.from([1, 2, 3, 4])
  .filter((n) => n % 2 === 0)
  .map((n) => n * 10)
  .toArray();
// [20, 40]
```

`map()`, `filter()` and `forEach()` take a `concurrency` option to run async work in parallel.

## 67: How do you cancel a stream pipeline?

Pass an `AbortSignal`:

```js
import { pipeline } from "node:stream/promises";

const ac = new AbortController();
setTimeout(() => ac.abort(), 5000);

try {
  await pipeline(source, transform, dest, { signal: ac.signal });
} catch (err) {
  if (err.name === "AbortError") console.log("cancelled after 5s");
  else throw err;
}
```

For a single stream, `stream.addAbortSignal(signal, stream)` destroys it when the signal fires. `AbortSignal.timeout(ms)` is a short way to create a signal that aborts after a time.

## 68: What are Web Streams, and does Node.js support them?

Web Streams are the browser standard for streams: `ReadableStream`, `WritableStream` and `TransformStream`. Node supports them as globals and through `node:stream/web`.

`fetch()` in Node returns a response whose `body` is a web `ReadableStream`, not a Node Readable. So you will meet both kinds in the same app. Other web stream classes in Node include `TextDecoderStream`, `CompressionStream` and `DecompressionStream`.

## 69: How do you convert between Node streams and Web Streams?

Use the static helpers:

```js
import { Readable, Writable } from "node:stream";

const nodeReadable = Readable.fromWeb(webReadable);
const webReadable2 = Readable.toWeb(nodeReadable);
const nodeWritable = Writable.fromWeb(webWritable);
```

`Duplex.fromWeb()` and `Duplex.toWeb()` work the same way for pairs. Also, `pipeline()` accepts web streams directly in many cases.

## 70: What are the main differences between Node streams and Web Streams?

- Node streams are EventEmitters with `data`, `end` and `error` events. Web streams use readers, writers and promises.
- Node streams have `pipe()` and `pipeline()`. Web streams have `pipeTo()` and `pipeThrough()`.
- Web streams lock: once you get a reader, nobody else can read until you release it.
- Web streams run the same in browsers, Deno, Bun and edge runtimes. Node streams only exist in Node and in runtimes that copy its API.
- Most of the Node ecosystem (fs, http, zlib, many libraries) still uses Node streams.

Use web streams for code that must run in many runtimes. Use Node streams for Node-only code that talks to Node APIs.

## 71: How do you save a fetch() response to a file without loading it all into memory?

```js
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";

const res = await fetch("https://example.com/big.zip");
if (!res.ok) throw new Error(`HTTP ${res.status}`);

await pipeline(Readable.fromWeb(res.body), createWriteStream("big.zip"));
```

`res.body` is a web stream, so it is turned into a Node stream first. Calling `res.arrayBuffer()` instead would load the whole file into memory.

## 72: How do you split a stream into lines when lines can cross chunk boundaries?

Keep the last unfinished line and prepend it to the next chunk:

```js
import { Transform } from "node:stream";

function splitLines() {
  let rest = "";
  return new Transform({
    readableObjectMode: true,
    transform(chunk, encoding, callback) {
      const lines = (rest + chunk).split("\n");
      rest = lines.pop(); // may be an incomplete line
      for (const line of lines) this.push(line);
      callback();
    },
    flush(callback) {
      if (rest) this.push(rest);
      callback();
    },
  });
}
```

Chunk boundaries are random. A chunk can end in the middle of a line, or even in the middle of a character. Call `setEncoding('utf8')` on the source so the chunks are already strings and split characters are handled (see question 73). For simple cases, `readline` already does all of this.

## 73: What goes wrong if you call chunk.toString() on every chunk of UTF-8 data?

A multi-byte character can be split between two chunks. If you decode each chunk on its own, both halves turn into the replacement character `�` and the text gets corrupted.

The fix is to use `stream.setEncoding('utf8')` or `StringDecoder`, which keep the unfinished bytes until the next chunk arrives:

```js
import { StringDecoder } from "node:string_decoder";

const decoder = new StringDecoder("utf8");
let text = "";
for await (const chunk of stream) text += decoder.write(chunk);
text += decoder.end();
```

This bug often goes unnoticed in tests that use only English text.

## 74: How do you stream a large JSON array to an HTTP client?

Write the brackets and commas yourself, and send each item as it is ready:

```js
import { pipeline } from "node:stream/promises";

async function* toJsonArray(rows) {
  yield "[";
  let first = true;
  for await (const row of rows) {
    yield (first ? "" : ",") + JSON.stringify(row);
    first = false;
  }
  yield "]";
}

app.get("/export", async (req, res) => {
  res.setHeader("Content-Type", "application/json");
  await pipeline(toJsonArray(db.streamRows()), res);
});
```

Many APIs use NDJSON instead (one JSON object per line). It is easier for the client to parse while it reads.

## 75: How do you handle a large file upload without buffering it in memory?

Stream the request body straight to its destination. For a raw body:

```js
http.createServer(async (req, res) => {
  try {
    await pipeline(req, createWriteStream(`/uploads/${randomUUID()}`));
    res.end("ok");
  } catch (err) {
    res.statusCode = 500;
    res.end("upload failed");
  }
});
```

For `multipart/form-data`, use a streaming parser like `busboy`. It gives you each file as a Readable stream, which you can pipe to disk or to cloud storage (for example with the S3 `Upload` helper from `@aws-sdk/lib-storage`). Avoid middleware that buffers the whole file in memory for big uploads.

## 76: How do you stream rows from a database?

Most drivers can give you a cursor or a stream instead of loading all rows:

```js
// MongoDB: the cursor is async iterable
for await (const doc of collection.find({ active: true })) {
  await handle(doc);
}

// PostgreSQL with pg-query-stream
import QueryStream from "pg-query-stream";
const stream = client.query(new QueryStream("SELECT * FROM events"));
await pipeline(stream, toCsv, res);
```

The driver fetches rows in batches as you consume them. This keeps memory flat even for millions of rows.

## 77: How does chunked transfer encoding relate to streams?

If you write to an HTTP/1.1 response without setting `Content-Length`, Node uses `Transfer-Encoding: chunked`. Each `res.write()` is sent as a separate chunk, and `res.end()` sends the final empty chunk.

This lets you send a response before you know its total size, which is what you want when streaming. If you know the size (for example a file), set `Content-Length`, so the client can show progress.

## 78: How do you serve a part of a file, for example for video seeking?

Read the `Range` header and use the `start` and `end` options of `createReadStream()` (both inclusive):

```js
const { size } = await stat(file);
const match = /bytes=(\d*)-(\d*)/.exec(req.headers.range ?? "");

if (match) {
  const start = match[1] ? Number(match[1]) : 0;
  const end = match[2] ? Number(match[2]) : size - 1;
  res.writeHead(206, {
    "Content-Range": `bytes ${start}-${end}/${size}`,
    "Accept-Ranges": "bytes",
    "Content-Length": end - start + 1,
  });
  await pipeline(createReadStream(file, { start, end }), res);
}
```

In a real app also return `416` for invalid ranges. Frameworks and `send`/`serve-static` already do this.

## 79: How do you calculate a hash of a large file?

`crypto.createHash()` returns a Transform-like stream, so you can pipe the file into it:

```js
import { createHash } from "node:crypto";
import { createReadStream } from "node:fs";

const hash = createHash("sha256");
for await (const chunk of createReadStream("big.iso")) hash.update(chunk);
console.log(hash.digest("hex"));
```

Memory use stays constant no matter how big the file is.

## 80: How do you gzip an HTTP response with streams?

Check `Accept-Encoding` and put a zlib stream between the source and the response:

```js
import { createGzip } from "node:zlib";

http.createServer(async (req, res) => {
  const src = createReadStream("report.csv");
  if (/\bgzip\b/.test(req.headers["accept-encoding"] ?? "")) {
    res.setHeader("Content-Encoding", "gzip");
    await pipeline(src, createGzip(), res);
  } else {
    await pipeline(src, res);
  }
});
```

Don't set `Content-Length` to the original file size when you compress. In production this is often done by a reverse proxy or the `compression` middleware instead.

## 81: How do you send one stream to two destinations?

Pipe the same source to both. The source then moves at the speed of the slower destination.

```js
const src = createReadStream("video.mp4");
src.pipe(createWriteStream("backup.mp4"));
src.pipe(createHash("md5").setEncoding("hex")).on("data", (hex) => {
  console.log("md5:", hex);
});
```

`pipe()` does not handle errors for you, so add `error` handlers or wrap each branch in `pipeline()`. For web streams there is `readable.tee()`, which gives you two branches.

## 82: What happens when you call destroy() with an error?

The stream is marked as destroyed, `_destroy()` runs to clean up the resource, then `error` is emitted with your error, and then `close`. Any pending writes are dropped, and further `write()` calls fail.

`pipeline()` reacts to this by destroying the other streams in the chain and rejecting with that error.

## 83: What do autoDestroy and emitClose do?

- `autoDestroy` (default `true`): the stream calls `destroy()` on itself after it ends or finishes. This releases resources without you having to do it.
- `emitClose` (default `true`): the stream emits `close` after it is destroyed.

Both used to be `false` by default in old Node versions. Turning them off is rarely a good idea in new code.

## 84: How do you check how full a stream's buffer is?

Streams have read-only properties for this:

- `readable.readableLength` and `writable.writableLength`: bytes (or objects) in the buffer.
- `readableHighWaterMark` and `writableHighWaterMark`: the thresholds.
- `writable.writableNeedDrain`: `true` if `write()` returned `false` and `drain` has not fired yet.
- `readableEnded`, `writableFinished`, `destroyed`: state flags.

They are useful for logging and for libraries that need to know if they should wait before writing.

## 85: What is the Buffer pool?

Node keeps a pre-allocated 8 KiB block of memory (`Buffer.poolSize`). Small Buffers made with `Buffer.allocUnsafe()`, `Buffer.from(string)` and `Buffer.from(array)` are cut from this block instead of getting their own memory. This makes creating many small Buffers much faster.

Only sizes smaller than half of the pool size use it. `Buffer.alloc()` never uses the pool. A side effect is that `buf.buffer` (the underlying `ArrayBuffer`) can be bigger than the Buffer and shared with other Buffers, so always use `buf.byteOffset` and `buf.byteLength` together with `buf.buffer`.

## 86: Does Buffer.from(arrayBuffer) copy the data?

No. `Buffer.from(arrayBuffer, byteOffset, length)` creates a view over the same memory. Changes in one are visible in the other.

```js
const ab = new ArrayBuffer(4);
const buf = Buffer.from(ab);
buf[0] = 1;
new Uint8Array(ab)[0]; // 1
```

`Buffer.from(buffer)` and `Buffer.from(uint8Array)` do copy. If you want a copy from a typed array view, `Buffer.copyBytesFrom(view, offset, length)` makes it clear.

## 87: When would you use TextEncoder and TextDecoder instead of Buffer?

`TextEncoder` turns a string into a UTF-8 `Uint8Array`, and `TextDecoder` turns bytes back into a string. They are web standards, so the same code works in browsers, Deno, Bun and Node.

Use them in shared or front-end compatible code. Use Buffer in Node-only code when you need other encodings like hex or base64 or need the binary read and write helpers. `TextDecoder` with `{ stream: true }` also handles characters split across chunks.

## 88: What are Blob and File in Node.js?

`Blob` is an immutable piece of binary data with a MIME type. `File` is a Blob with a name and a last modified date. Both are globals in current Node versions and match the browser API.

```js
const blob = new Blob(["hello"], { type: "text/plain" });
await blob.text(); // 'hello'
const stream = blob.stream(); // web ReadableStream
```

You meet them with `fetch()` and `FormData`, for example when you upload a file to another API. `fs.openAsBlob(path)` gives you a Blob backed by a file on disk.

## 89: How do you check if a value is a Buffer, or if bytes are valid UTF-8?

```js
import { isUtf8 } from "node:buffer";

Buffer.isBuffer(value); // true for Buffer instances
value instanceof Uint8Array; // true for Buffers and plain Uint8Arrays
isUtf8(buf); // true if the bytes are valid UTF-8
```

`isUtf8()` is useful before you treat uploaded data as text.

## 90: Why should you use crypto.timingSafeEqual to compare secrets?

`buf.equals()` and `===` stop at the first different byte. An attacker who can measure response times can guess a secret (like an HMAC signature) one byte at a time.

`crypto.timingSafeEqual(a, b)` always takes the same time for the same length:

```js
import { timingSafeEqual } from "node:crypto";

const expected = Buffer.from(expectedSig, "hex");
const actual = Buffer.from(receivedSig, "hex");
const ok =
  expected.length === actual.length && timingSafeEqual(expected, actual);
```

It throws if the lengths differ, so check the length first.

## 91: How do you parse a binary header with Buffer methods?

Read each field at its offset with the right type and byte order. Example: a PNG file starts with an 8 byte signature, then the IHDR chunk, where width and height are 32-bit big-endian numbers at offsets 16 and 20.

```js
import { open } from "node:fs/promises";

const fh = await open("image.png");
const { buffer } = await fh.read(Buffer.alloc(24), 0, 24, 0);
await fh.close();

const isPng = buffer
  .subarray(0, 8)
  .equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]));
const width = buffer.readUInt32BE(16);
const height = buffer.readUInt32BE(20);
```

You only read 24 bytes, not the whole image.

## 92: How do you read and write 64-bit integers in a Buffer?

JavaScript numbers can't hold every 64-bit integer exactly, so Buffer uses `BigInt` for them:

```js
const buf = Buffer.alloc(8);
buf.writeBigUInt64BE(2n ** 63n);
buf.readBigUInt64BE(); // 9223372036854775808n
```

There are signed and unsigned versions in both byte orders. Convert to `Number` only if you know the value is below `Number.MAX_SAFE_INTEGER`.

## 93: How do you write data with a known length into a pre-allocated Buffer?

`buf.write(string, offset, encoding)` writes a string and returns the number of bytes written. It never writes past the end, it cuts the string instead.

```js
const buf = Buffer.alloc(10);
const n = buf.write("héllo", 0, "utf8"); // 6
buf.subarray(0, n).toString(); // 'héllo'
```

Combined with the number write methods, this lets you build a binary message in one Buffer without many small allocations.

## 94: How do you test a stream?

- Feed input with `Readable.from([...])`.
- Collect output with the helpers from `node:stream/consumers` or with `toArray()`.
- Check errors with `assert.rejects()` around `pipeline()`.

```js
import { test } from "node:test";
import assert from "node:assert/strict";
import { Readable } from "node:stream";

test("splitLines joins lines across chunks", async () => {
  const out = await Readable.from(["ab\nc", "d\n"])
    .pipe(splitLines())
    .toArray();
  assert.deepEqual(out, ["ab", "cd"]);
});
```

Also test small chunk sizes (even 1 byte per chunk), because that is where boundary bugs show up.

## 95: What is node:stream/consumers?

It has helper functions that read a whole stream and return the result as a promise: `text()`, `json()`, `buffer()`, `arrayBuffer()` and `blob()`.

```js
import { json } from "node:stream/consumers";

http.createServer(async (req, res) => {
  const body = await json(req);
  res.end(`hello ${body.name}`);
});
```

They work with Node streams, web streams and async iterables. They read everything into memory, so use them only for bodies with a known size limit.

## 96: Why would a stream pipeline hang and never finish?

Common causes:

- A custom `_write()` or `_transform()` never calls its callback, so no more data is sent.
- A custom Readable never calls `push(null)`, so it never ends.
- Nobody reads from a Readable or a Transform, so its buffer fills up and everything upstream pauses.
- A Writable never gets `end()`.
- An error was swallowed somewhere, for example in an `async` callback with no `try/catch`.

To find it, log the `readableLength`, `writableLength` and the `end`, `finish` and `close` events of each step and see where the data stops.

## 97: What is the problem with an async function as a data event handler?

The stream does not wait for your promise. It keeps emitting `data` events while your earlier calls are still running. You lose backpressure, you lose order, and if the promise rejects, the error is not handled by the stream.

```js
// Bad: runs many saves at the same time, no backpressure
stream.on("data", async (row) => {
  await save(row);
});

// Good: one at a time, errors go to the try/catch
for await (const row of stream) {
  await save(row);
}
```

## 98: How do you use streams with child processes?

`spawn()` gives you a child process whose `stdin` is a Writable and whose `stdout` and `stderr` are Readables:

```js
import { spawn } from "node:child_process";
import { pipeline } from "node:stream/promises";

const ffmpeg = spawn("ffmpeg", ["-i", "pipe:0", "-f", "mp3", "pipe:1"]);
await Promise.all([
  pipeline(createReadStream("in.wav"), ffmpeg.stdin),
  pipeline(ffmpeg.stdout, createWriteStream("out.mp3")),
]);
```

`exec()` and `execFile()` buffer all output in memory and have a `maxBuffer` limit, so use `spawn()` for large output.

## 99: What can cause a memory leak when working with streams?

- Ignoring the return value of `write()` and pushing data faster than it can be written.
- Not reading a stream at all, while still keeping references to it.
- Adding listeners in a loop or per request on a long-lived stream (you'll see `MaxListenersExceededWarning`).
- Not destroying streams on error when you use `pipe()`, so file descriptors and sockets stay open.
- Holding on to small `subarray()` views of large Buffers (see question 121).

Most of these go away if you use `pipeline()` and `for await`.

## 100: How do you count bytes or show progress while streaming?

Add a small step in the middle that counts and passes the data on:

```js
const { size } = await stat("big.zip");
let done = 0;

await pipeline(
  createReadStream("big.zip"),
  async function* (source) {
    for await (const chunk of source) {
      done += chunk.length;
      process.stdout.write(`\r${Math.round((done / size) * 100)}%`);
      yield chunk;
    }
  },
  createWriteStream("copy.zip"),
);
```

The same idea works for upload size limits: count bytes and throw once they pass the limit (see question 132).

# Advanced Questions (101-150)

## 101: How does a Readable stream's internal buffer work?

A Readable keeps a list of chunks that were pushed but not read yet. When you (or the underlying source) call `push(chunk)`, the chunk is added to that list, and `push()` returns `true` while the buffered size is below `highWaterMark`.

When the buffer is under `highWaterMark` and the stream wants more data, it calls `_read()`. Once the buffer reaches the threshold, it stops calling `_read()`. When the consumer reads and the buffer gets smaller, it calls `_read()` again. So `_read()` is the "give me more" signal and the return value of `push()` is the "slow down" signal.

## 102: How does a Writable stream buffer writes?

A Writable passes one chunk at a time to `_write()`. While that write is in progress, new chunks from `write()` go into an internal buffer. When the callback of `_write()` is called, the next buffered chunk is sent.

`writableLength` is the total size of the chunk in progress plus the buffered ones. When it reaches `highWaterMark`, `write()` returns `false`. When the buffer is empty again, the stream emits `drain`. If `_writev()` exists, all buffered chunks can be sent in one call instead of one by one.

## 103: Is highWaterMark a hard memory limit?

No. It only controls when the stream says "stop". If the producer ignores `false` from `write()` or `push()`, the data is still accepted and memory keeps growing.

A single chunk can also be bigger than `highWaterMark`. If you push a 10 MB Buffer into a stream with a 64 KiB threshold, the 10 MB is still stored. If you need a real memory limit, you have to respect backpressure and keep chunk sizes small yourself.

## 104: How do you choose a good highWaterMark?

There is no single right value. Things to think about:

- Larger values mean fewer `_read()` and `_write()` calls and fewer system calls, so better throughput for big sequential I/O.
- Smaller values mean less memory per stream. With 10,000 open connections, 64 KiB each is already 640 MB in the worst case.
- For slow consumers a large buffer just hides the problem for a bit longer.

Start with the defaults, measure throughput and memory with real data, and change it only for streams where it makes a clear difference.

## 105: What is tricky about backpressure in object mode?

In object mode, `highWaterMark` counts objects, not bytes. With the default of 16, a stream holds 16 objects whether each is 10 bytes or 10 MB.

If objects can be large (for example whole documents or images), lower `highWaterMark`, or batch by size yourself. Also be careful with transforms that turn one input into many outputs. They can push a lot of data from one `_transform()` call even though the buffer is "full".

## 106: How does backpressure work with async generators in pipeline()?

An async generator only runs when someone asks for its next value. In `pipeline()`, the next step pulls from the generator, and when the destination is full, it stops pulling. The generator then sits at its `yield` until there is room.

```js
await pipeline(
  source,
  async function* (rows) {
    for await (const row of rows) {
      yield transform(row); // waits here if the next step is full
    }
  },
  dest,
);
```

That is why async generators are a safe way to write transforms. You get backpressure without managing it by hand.

## 107: Why does pipe() leak resources on errors and pipeline() does not?

With `a.pipe(b)`, if `b` fails, `a` is only unpiped. It is not destroyed, so it keeps its file descriptor or socket open and may stay paused forever. If `a` fails, `b` is not ended or destroyed either.

`pipeline()` adds listeners to every stream. When any of them errors or closes too early, it calls `destroy()` on all streams in the chain, waits for them to close, and reports the first error. In a server that handles many requests, the `pipe()` version slowly leaks file descriptors and memory.

## 108: What are _construct and _destroy used for?

`_construct(callback)` runs once before the first `_read()` or `_write()`. Use it for async setup, like opening a file or connecting. The stream buffers calls until you call the callback.

`_destroy(err, callback)` runs when the stream is destroyed, on success or error. Use it to release resources.

```js
import { Writable } from "node:stream";
import { open } from "node:fs/promises";

class FileWriter extends Writable {
  constructor(path) {
    super();
    this.path = path;
  }
  _construct(callback) {
    open(this.path, "w").then((fh) => {
      this.fh = fh;
      callback();
    }, callback);
  }
  _write(chunk, enc, callback) {
    this.fh.write(chunk).then(() => callback(), callback);
  }
  _destroy(err, callback) {
    if (!this.fh) return callback(err);
    this.fh.close().then(
      () => callback(err),
      (closeErr) => callback(err || closeErr),
    );
  }
}
```

## 109: What is _final in a Writable?

`_final(callback)` runs after `end()` is called and all buffered writes are done, but before `finish` is emitted. It is the place to flush your own buffers or send a "done" message.

For example, a batching writer that collects rows and inserts every 500 should insert the last partial batch in `_final()`. If you forget, the last rows are lost and `finish` still fires, so the bug is easy to miss.

## 110: How is a Transform different from a Duplex internally?

In a Duplex, the readable and writable sides are separate. You implement `_read()` and `_write()`, and they don't depend on each other.

In a Transform, Node connects them for you. `_write()` calls your `_transform()`, what you push goes to the readable buffer, and the write callback is held back if the readable side is full. That way backpressure flows from the reader, through the transform, back to the writer. A Transform has two buffers, one on each side, so it can hold up to about two `highWaterMark`s of data.

## 111: How do you write a Transform that limits throughput, for example to 1 MB per second?

Delay the callback based on how many bytes went through:

```js
import { Transform } from "node:stream";
import { setTimeout as sleep } from "node:timers/promises";

function throttle(bytesPerSecond) {
  const start = Date.now();
  let sent = 0;
  return new Transform({
    async transform(chunk, enc, callback) {
      sent += chunk.length;
      const expectedMs = (sent / bytesPerSecond) * 1000;
      const waitMs = expectedMs - (Date.now() - start);
      if (waitMs > 0) await sleep(waitMs);
      callback(null, chunk);
    },
  });
}
```

Because the callback is delayed, the writable side buffer fills up and backpressure slows down the source. Nothing piles up in memory.

## 112: How do you batch objects into groups in a stream?

Collect items and push them when the batch is full, and push the rest in `flush`:

```js
function batch(size) {
  let items = [];
  return new Transform({
    objectMode: true,
    transform(item, enc, callback) {
      items.push(item);
      if (items.length >= size) {
        this.push(items);
        items = [];
      }
      callback();
    },
    flush(callback) {
      if (items.length) this.push(items);
      callback();
    },
  });
}

await pipeline(csvRows, batch(500), dbBulkInsertWriter);
```

Batching is the usual way to make inserts into a database or calls to a bulk API much faster.

## 113: How do you process stream items in parallel but with a limit?

Use `readable.map()` with the `concurrency` option:

```js
const results = Readable.from(urls).map(
  async (url) => {
    const res = await fetch(url);
    return { url, status: res.status };
  },
  { concurrency: 10 },
);

for await (const r of results) console.log(r);
```

At most 10 requests run at the same time, and results come out in the same order as the input. Libraries like `p-limit` give you the same idea outside of streams.

## 114: Does parallel processing in a stream keep the order?

`readable.map()` with `concurrency` keeps the input order. If item 1 is slow and item 2 is fast, item 2 waits until item 1 is done. That can hurt throughput when task times vary a lot.

If order does not matter, you can write a custom Writable or Transform that starts tasks and pushes results as they finish, while still limiting the number of tasks in flight. Be clear about which one you need. Out-of-order output is a real bug for things like log files or CSV exports.

## 115: What happens when one source is piped to a fast and a slow destination?

The source can only move as fast as the slowest destination. When the slow one returns `false` from `write()`, the source pauses for everyone, so the fast one waits too.

If this is a problem, you can give the slow branch its own buffer (for example write to a temp file or queue first), or drop data for the slow consumer if that's acceptable (like live metrics). Just never remove backpressure by buffering without a limit in memory.

## 116: What is stream.compose()?

`compose()` combines several streams or async generator functions into one Duplex stream. You write to the first one and read from the last one.

```js
import { compose } from "node:stream";
import { createGzip } from "node:zlib";

const csvToGzip = compose(async function* (rows) {
  for await (const row of rows) yield row.join(",") + "\n";
}, createGzip());

await pipeline(
  Readable.from([
    [1, 2],
    [3, 4],
  ]),
  csvToGzip,
  createWriteStream("a.csv.gz"),
);
```

It is useful when you want to hand out a reusable piece of a pipeline as one stream. It is still marked experimental in the docs.

## 117: What does Duplex.from() do?

`Duplex.from()` creates a Duplex from many kinds of input: a stream, an async generator function, a promise, a Blob, a web stream pair, or an object with `readable` and `writable` properties.

```js
import { Duplex } from "node:stream";

const upper = Duplex.from(async function* (source) {
  for await (const chunk of source) yield String(chunk).toUpperCase();
});
```

It is a quick way to turn generator code into something you can pass to APIs that expect a stream.

## 118: What happens to a stream when you break out of a for await loop?

The stream is destroyed. `break`, `return` and a thrown error all call the iterator's `return()` method, and the stream's iterator then calls `destroy()`. The file or socket is closed.

```js
for await (const chunk of createReadStream("huge.log")) {
  if (chunk.includes("ERROR")) break; // the stream is closed here
}
```

This is usually what you want. If you need to read the rest of the stream later, `readable.iterator({ destroyOnReturn: false })` keeps it open, but it is marked experimental.

## 119: Why shouldn't you mix data events and async iteration on the same stream?

Both consume data from the same buffer. Adding a `data` listener switches the stream to flowing mode, and those chunks are no longer available to the iterator, so the loop sees some chunks and misses others. Mixing `readable`, `data` and `pipe()` has similar problems.

Pick one way to consume a stream. If two parts of the app need the data, use a PassThrough or a tee and give each part its own branch.

## 120: What does Readable.from('some string') emit?

It emits the whole string as a single chunk. It does not split it into characters, even though strings are iterable. The same is true for a Buffer.

```js
await Readable.from("hello").toArray(); // ['hello']
await Readable.from(["h", "i"]).toArray(); // ['h', 'i']
```

This was decided for performance, since emitting one chunk per character would be very slow. If you want several chunks, pass an array or a generator.

## 121: How can a small Buffer keep a lot of memory alive?

`subarray()` returns a view, not a copy. As long as the view exists, the whole underlying memory stays alive.

```js
const big = await readFile("100mb.bin");
const header = big.subarray(0, 16);
cache.set(key, header); // keeps all 100 MB in memory
```

The same happens with Buffers from the 8 KiB pool, where one small long-lived Buffer keeps the whole slab. If you store a small piece for a long time, copy it: `Buffer.from(big.subarray(0, 16))`. Then the large Buffer can be freed.

## 122: Where is Buffer memory stored, and how do you measure it?

Buffer data is stored outside the V8 heap. Only the small JavaScript object is on the heap. That is why a process can use more memory than `--max-old-space-size` would suggest.

`process.memoryUsage()` shows it in `arrayBuffers` (memory for all ArrayBuffers and Buffers) and `external` (all memory outside the heap that V8 knows about). If `rss` keeps growing but `heapUsed` doesn't, look at Buffers that are not freed, like caches of Buffers or large streams buffering data.

## 123: What is the maximum size of a Buffer or a string?

The Buffer limit is in `buffer.constants.MAX_LENGTH`. It depends on the Node version and the platform, and on 64-bit systems it is very large in current versions. The string limit is much smaller: `buffer.constants.MAX_STRING_LENGTH`, about 2^29 (roughly 536 million) characters on 64-bit V8.

So `readFile()` of a 1 GB file may work, but `toString()` on it fails with `ERR_STRING_TOO_LONG`. This is one more reason to stream large text files instead of turning them into one string.

## 124: What are the security risks of Buffer.allocUnsafe?

The memory is not cleared, so it may contain old data from the same process: passwords, tokens, other users' request bodies. If any part of that Buffer is sent to a client or written to a log before being fully overwritten, that data leaks.

Rules: use `Buffer.alloc()` unless you measured a real need for speed, overwrite every byte before use, and never pass a user-controlled number to `allocUnsafe()`. The `--zero-fill-buffers` flag makes all new Buffers zero-filled, which you can use for extra safety at some cost to performance.

## 125: What happens when you decode invalid UTF-8 or use the wrong encoding?

Invalid UTF-8 bytes turn into the replacement character `�`. No error is thrown, so data can be silently corrupted. If you then encode the string back, you get different bytes than you started with.

`latin1` (also called `binary`) maps each byte to one character, so it round trips any bytes, but the text looks wrong for non-Latin data. `ascii` drops the high bit of each byte in some cases. To avoid surprises, keep binary data as Buffers, decode only when you know the encoding, and check with `isUtf8()` when the source is not trusted.

## 126: How do you pass a Buffer to a worker thread without copying it?

Put its `ArrayBuffer` in the transfer list of `postMessage()`. The memory is moved to the worker, and in the sender the ArrayBuffer becomes detached (length 0).

```js
const buf = Buffer.alloc(1024 * 1024);
worker.postMessage(buf, [buf.buffer]);
console.log(buf.length); // 0, it now belongs to the worker
```

Be careful with Buffers from the pool (`allocUnsafe()` with small sizes, `Buffer.from(string)`): their `buf.buffer` is shared with other Buffers. Node marks pooled memory as not transferable, so you can't move it this way. Use `Buffer.alloc()` or a dedicated `ArrayBuffer` for data you want to transfer.

## 127: When would you use SharedArrayBuffer instead of transferring?

Transferring moves memory to one thread. `SharedArrayBuffer` lets several threads see the same memory at the same time. This is useful for large data that many workers read, or for shared counters and flags.

```js
const shared = new SharedArrayBuffer(1024);
const view = Buffer.from(shared);
worker.postMessage(shared); // both sides see the same bytes
```

You have to handle concurrent access yourself, usually with `Atomics`. For most apps, sending messages or transferring is simpler and safer.

## 128: How would you design a pipeline that processes a 50 GB CSV file?

- Read with `createReadStream()` and parse with a streaming CSV parser (like `csv-parse`), which outputs objects in object mode.
- Validate and transform rows in an async generator step.
- Batch rows (for example 1,000 per batch) and write them with bulk inserts in a custom Writable.
- Connect everything with `pipeline()`, so errors stop everything and close the file.
- Track the line number or byte offset, so a failed run can resume from the last committed batch instead of starting over.
- Write bad rows to a separate error file instead of stopping the whole job.

Memory stays flat because only a few batches are in flight at a time. The database is usually the bottleneck, so tune batch size and the number of parallel inserts against it.

## 129: How do you stream a large database export as a download and handle the client leaving halfway?

Use `pipeline()` from the database cursor to the response:

```js
app.get("/export.csv", async (req, res) => {
  res.setHeader("Content-Type", "text/csv");
  res.setHeader("Content-Disposition", 'attachment; filename="export.csv"');
  try {
    await pipeline(db.cursor("SELECT * FROM orders"), toCsvLines, res);
  } catch (err) {
    if (err.code === "ERR_STREAM_PREMATURE_CLOSE") return; // client left
    req.log.error(err);
  }
});
```

When the client disconnects, the response closes, `pipeline()` destroys the cursor, and the database query is stopped. Without that, the server keeps reading rows nobody will receive. Once headers are sent, you can't change the status code, so an error in the middle can only be shown by cutting the connection.

## 130: How do you detect that a client disconnected during a streaming response?

Listen to `close` on the response and check if it finished:

```js
res.on("close", () => {
  if (!res.writableFinished) {
    console.log("client went away before the end");
    cleanup();
  }
});
```

`pipeline()` already handles this case for its own streams. You need manual handling for work outside the pipeline, like a timer that writes Server-Sent Events or a background job started for this request.

## 131: How do you handle a stalled upload or download?

A stream can stay open forever if the other side stops sending but doesn't close the connection. Ways to handle it:

- Set server timeouts: `server.requestTimeout`, `server.headersTimeout` and socket timeouts with `socket.setTimeout()`.
- Add an idle timer in your pipeline that resets on each chunk and destroys the stream when it fires.
- Pass `AbortSignal.timeout(ms)` to `pipeline()` for a total time limit.

```js
await pipeline(req, createWriteStream(path), {
  signal: AbortSignal.timeout(10 * 60_000),
});
```

Each open stalled stream holds a socket and memory, so a missing timeout is also a denial-of-service risk.

## 132: How do you limit the size of a streamed upload?

Count bytes as they go through and stop when the limit is reached:

```js
function limitSize(maxBytes) {
  let total = 0;
  return async function* (source) {
    for await (const chunk of source) {
      total += chunk.length;
      if (total > maxBytes) {
        const err = new Error("payload too large");
        err.status = 413;
        throw err;
      }
      yield chunk;
    }
  };
}

await pipeline(req, limitSize(50 * 1024 * 1024), createWriteStream(tmpPath));
```

Don't trust the `Content-Length` header alone, since the client can lie or use chunked encoding. On failure, delete the partly written file.

## 133: How does the order of events go for a Transform in a pipeline that finishes normally?

For a Transform in a successful pipeline, the usual order is:

1. The writable side gets `end()` from upstream.
2. `_flush()` runs and pushes the last data.
3. `finish` is emitted (the writable side is done).
4. `end` is emitted when the last data has been read by the next step.
5. `close` is emitted after `autoDestroy` destroys the stream.

If something fails, you get `error` and then `close`, and `end` or `finish` may never come. That is why waiting for `close`, or using `finished()`, is safer than waiting for `end` or `finish` alone.

## 134: How do you proxy an HTTP request to another server with streams?

Pipe the incoming request into the outgoing one, and the upstream response back into your response:

```js
import http from "node:http";
import { pipeline } from "node:stream/promises";

http
  .createServer((req, res) => {
    const upstream = http.request(
      {
        host: "internal-api",
        port: 8080,
        path: req.url,
        method: req.method,
        headers: req.headers,
      },
      async (upRes) => {
        res.writeHead(upRes.statusCode, upRes.headers);
        await pipeline(upRes, res).catch(() => {});
      },
    );
    pipeline(req, upstream).catch(() => res.destroy());
  })
  .listen(3000);
```

Backpressure works both ways: a slow client slows down reading from upstream, and a slow upstream slows down reading the upload. In real code also remove hop-by-hop headers like `connection`, and add timeouts. Tools like `http-proxy` or undici's proxy features handle many of these details.

## 135: How do you implement Server-Sent Events with Node streams?

SSE is a long-lived HTTP response with `Content-Type: text/event-stream`, where each message is `data: ...` followed by a blank line.

```js
app.get("/events", (req, res) => {
  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
  });

  const send = (data) => res.write(`data: ${JSON.stringify(data)}\n\n`);
  const timer = setInterval(() => send({ time: Date.now() }), 1000);

  res.on("close", () => clearInterval(timer));
});
```

Clean up on `close`, or you leak timers and subscriptions for every client that left. If `write()` returns `false` for a slow client, decide whether to skip messages or disconnect it, instead of buffering forever.

## 136: Why can compression break streaming responses like SSE?

Compressors collect data until they have enough to compress well. A small SSE message can sit inside gzip's buffer and never reach the client until more data comes.

Fixes: flush the compressor after each message (zlib streams have `flush()`, and the `compression` middleware adds `res.flush()`), or turn off compression for event streams. Proxies like nginx can also buffer responses, which is why SSE setups often send the `X-Accel-Buffering: no` header or turn off proxy buffering.

## 137: What is the performance cost of object mode and small chunks?

Each chunk passes through several function calls, buffer bookkeeping and sometimes events. With 64 KiB chunks this overhead is tiny. With millions of tiny objects or one-byte chunks, the overhead becomes the main cost.

To speed things up: batch small items into arrays, use bigger chunks for byte streams, and avoid long chains of trivial transforms (combine them into one step). Measure with `--cpu-prof` or a flame graph before changing things.

## 138: What happens if a transform does CPU-heavy work?

Transforms run on the main thread. If `_transform()` takes 200 ms of CPU per chunk, the event loop is blocked for that time, and every other request in the process waits.

Options: make chunks smaller so each piece of work is short, move the heavy work to `worker_threads` (for example with a pool like `piscina`), or use native streams that do the work off the main thread. zlib and crypto streams already run their work in the libuv thread pool.

## 139: When should you choose Web Streams over Node streams in a Node.js app?

Choose Web Streams when the code must run outside Node too (browsers, edge runtimes, Deno, Bun), when you work mostly with `fetch()`, `Response` and `Blob`, or when a framework is built on them (many edge-first frameworks are).

Choose Node streams when you work with `fs`, `net`, `http`, `zlib` and the large npm ecosystem, or when performance matters a lot. Node streams have been tuned for longer, and code that doesn't convert between the two kinds is faster. Converting between the two in a hot path adds overhead, so try to stay on one side for the main data flow.

## 140: What are byte streams and BYOB readers in Web Streams?

A web `ReadableStream` with `type: 'bytes'` is a byte stream. It supports a BYOB ("bring your own buffer") reader, where the consumer passes its own buffer and the stream fills it.

```js
const reader = stream.getReader({ mode: "byob" });
let buf = new Uint8Array(4096);
const { value, done } = await reader.read(buf);
// value is a view of the filled part; the old buf is detached
buf = new Uint8Array(value.buffer);
```

This avoids allocating a new buffer for each chunk, which helps for high-throughput binary data. Node streams don't have a direct equivalent; the closest is reading with a reused Buffer through `filehandle.read()`.

## 141: How do you parse a length-prefixed binary protocol from a stream?

Each message is, for example, a 4-byte big-endian length followed by that many bytes. Chunks don't match message boundaries, so buffer until you have a full message:

```js
async function* frames(source) {
  let buf = Buffer.alloc(0);
  for await (const chunk of source) {
    buf = Buffer.concat([buf, chunk]);
    while (buf.length >= 4) {
      const len = buf.readUInt32BE(0);
      if (buf.length < 4 + len) break; // wait for more data
      yield buf.subarray(4, 4 + len);
      buf = buf.subarray(4 + len);
    }
  }
  if (buf.length) throw new Error("stream ended in the middle of a frame");
}

for await (const msg of frames(socket)) handle(msg);
```

Also check `len` against a maximum. Otherwise a bad or hostile peer can send a huge length and make you buffer gigabytes.

## 142: What is the problem with calling Buffer.concat on every chunk in a parser?

`Buffer.concat()` copies all bytes every time. If a message is large and arrives in many small chunks, you copy the growing buffer again and again, which is O(n²) in the worst case.

Better: keep a list of chunks and a total length, and only concat when you have a full message. Or, if you know the message size from the header, allocate a Buffer of that size once and copy each chunk into it with `chunk.copy(target, offset)`.

## 143: When does a Readable start flowing, and can you lose data?

A Readable starts flowing when you add a `data` listener, call `pipe()` or `resume()`, or start iterating. Before that, data waits in the buffer up to `highWaterMark`, so you don't lose data just by attaching listeners a bit later.

You can lose data if the stream is already flowing and nobody listens to `data`, for example after calling `resume()` only to "drain" it, or after removing the only `data` listener without pausing. In old (streams1-era) code, streams emitted data right away, which is where the "attach your listener in the same tick" advice comes from.

## 144: What do ERR_STREAM_PREMATURE_CLOSE and ERR_STREAM_WRITE_AFTER_END mean?

`ERR_STREAM_PREMATURE_CLOSE` means a stream closed before it ended or finished. The usual reason is that the other side went away: an HTTP client disconnected, or a socket was reset. In a server it is often normal and should be logged at a low level, not treated as a bug.

`ERR_STREAM_WRITE_AFTER_END` means something called `write()` after `end()`. That is a real bug in your code, often a race where two async paths both write to the same response, or a timer that still runs after the response ended.

## 145: Are writes to process.stdout synchronous?

It depends on what stdout is connected to (a file, a terminal or a pipe) and on the operating system. In some cases writes are synchronous, in others they are async and buffered.

The practical problem: if you write a lot of output and then call `process.exit()`, the async part may be lost. Prefer setting `process.exitCode` and letting the process end on its own, or wait for the write callback before exiting. Loggers like pino have their own handling for this.

## 146: How do you test that your stream code respects backpressure?

Use a slow destination with a small `highWaterMark` and check how much the source produced:

```js
let produced = 0;
const source = new Readable({
  read() {
    produced += 1;
    this.push(Buffer.alloc(1024));
  },
});

const slow = new Writable({
  highWaterMark: 4 * 1024,
  write(chunk, enc, callback) {
    setTimeout(callback, 10);
  },
});

source.pipe(yourTransform).pipe(slow);
await new Promise((r) => setTimeout(r, 200));
assert.ok(
  produced < 100,
  `source produced ${produced} chunks, backpressure is broken`,
);
source.destroy();
```

If the code under test ignores backpressure, `produced` grows very fast. Watching `process.memoryUsage().arrayBuffers` in a longer test works too.

## 147: Show a common way to accidentally ignore backpressure in a custom Readable.

Pushing everything at once from `_read()`, or from an outside event source, without checking `push()`:

```js
// Bad: pushes all rows no matter what
_read() {
  for (const row of this.allRows) this.push(row);
  this.push(null);
}

// Better: push until push() returns false, then wait for the next _read()
_read() {
  while (this.i < this.allRows.length) {
    if (!this.push(this.allRows[this.i++])) return;
  }
  this.push(null);
}
```

The same mistake happens when wrapping an event source (like a message queue consumer): you need to pause the source when `push()` returns `false` and resume it in `_read()`.

## 148: How would you build resumable downloads with streams?

On the server, support `Range` requests (see question 78) and send `Accept-Ranges: bytes` and a stable `ETag`. On the client:

1. Check how many bytes of the file you already have on disk.
2. Send `Range: bytes=<size>-` and `If-Range: <etag>`.
3. If the server replies `206`, append to the file (`createWriteStream(path, { flags: 'a' })`). If it replies `200`, the file changed, so start over.
4. Verify a checksum at the end.

For uploads the same idea works with a protocol like tus or S3 multipart uploads, where each part is uploaded and confirmed on its own, so a failure only repeats one part.

## 149: How do you debug which step in a long pipeline is slow?

- Add a small pass-through step between each stage that logs chunk counts and timestamps, and see where the gaps are.
- Watch `readableLength` and `writableLength`. A full buffer before a step and an empty one after it means that step is the bottleneck.
- Use `--cpu-prof` or `0x`/`clinic flame` to see if a step burns CPU.
- Check event loop delay with `perf_hooks.monitorEventLoopDelay()`. High delay means some step blocks the main thread.

Usually the slow step is the external one (database, network API) or a CPU-heavy transform. Fix that step with batching, concurrency or a worker, not the whole pipeline.

## 150: An API service runs out of memory when users download large reports. How would you investigate and fix it?

First find where the memory goes. Take a heap snapshot or check `process.memoryUsage()`. If `arrayBuffers` or `external` is huge, Buffers are piling up. Then look at the code for the report download. Common causes:

- The report is built fully in memory (`rows.map(...).join()`, `res.send(bigString)`) instead of streamed.
- The code uses `res.write()` in a loop and ignores its return value, so slow clients make data pile up.
- Streams are connected with `pipe()` and are never destroyed when the client leaves.

The fix is to stream from the database cursor through a CSV step to the response with `pipeline()`, so memory per download is bounded and a disconnect stops the query. Add a limit on concurrent exports and timeouts, and test with a slow client (for example `curl --limit-rate 10k`) to confirm memory stays flat.
