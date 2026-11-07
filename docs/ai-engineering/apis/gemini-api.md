# Gemini API Interview Questions and Answers

_Last updated: November 7, 2026_

450 Gemini API interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced.

The answers cover Google's Gemini API as of November 2026: the Interactions API (the recommended API for new projects since June 2026), the older `generateContent` API (now called legacy but still supported), the Google GenAI SDKs (`google-genai` for Python and `@google/genai` for JavaScript), and current models like Gemini 4 Argon, Gemini 3.8 Flash and Gemini 3.5 Flash-Lite. Model names and limits change often, so check the official docs before you rely on exact numbers.

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
- [Advanced Questions (301-450)](#advanced-questions-301-450)

### Easy Questions (1-150)

- [1: What is the Gemini API?](#1-what-is-the-gemini-api)
- [2: What is the difference between the Gemini app and the Gemini API?](#2-what-is-the-difference-between-the-gemini-app-and-the-gemini-api)
- [3: What is Google AI Studio?](#3-what-is-google-ai-studio)
- [4: What is the difference between the Gemini API and Gemini on Vertex AI?](#4-what-is-the-difference-between-the-gemini-api-and-gemini-on-vertex-ai)
- [5: How do you get a Gemini API key?](#5-how-do-you-get-a-gemini-api-key)
- [6: Which environment variables do the SDKs read the API key from?](#6-which-environment-variables-do-the-sdks-read-the-api-key-from)
- [7: What are the official SDKs for the Gemini API?](#7-what-are-the-official-sdks-for-the-gemini-api)
- [8: How do you install the Python SDK?](#8-how-do-you-install-the-python-sdk)
- [9: How do you install the JavaScript SDK?](#9-how-do-you-install-the-javascript-sdk)
- [10: What happened to the old google-generativeai and @google/generativeai libraries?](#10-what-happened-to-the-old-google-generativeai-and-googlegenerativeai-libraries)
- [11: How do you create a client in Python?](#11-how-do-you-create-a-client-in-python)
- [12: How do you create a client in JavaScript?](#12-how-do-you-create-a-client-in-javascript)
- [13: How do you send your first request with the Interactions API?](#13-how-do-you-send-your-first-request-with-the-interactions-api)
- [14: What is the Interactions API?](#14-what-is-the-interactions-api)
- [15: What is the generateContent API?](#15-what-is-the-generatecontent-api)
- [16: Should you use the Interactions API or generateContent for a new project?](#16-should-you-use-the-interactions-api-or-generatecontent-for-a-new-project)
- [17: How do you make a basic generateContent call in Python?](#17-how-do-you-make-a-basic-generatecontent-call-in-python)
- [18: How do you make a basic generateContent call in JavaScript?](#18-how-do-you-make-a-basic-generatecontent-call-in-javascript)
- [19: How do you call generateContent with curl?](#19-how-do-you-call-generatecontent-with-curl)
- [20: How do you call the Interactions API with curl?](#20-how-do-you-call-the-interactions-api-with-curl)
- [21: What are the v1 and v1beta API versions?](#21-what-are-the-v1-and-v1beta-api-versions)
- [22: What is a model ID?](#22-what-is-a-model-id)
- [23: What are the main Gemini models available today?](#23-what-are-the-main-gemini-models-available-today)
- [24: What is the difference between Pro, Flash and Flash-Lite models?](#24-what-is-the-difference-between-pro-flash-and-flash-lite-models)
- [25: What do stable, preview and deprecated mean for Gemini models?](#25-what-do-stable-preview-and-deprecated-mean-for-gemini-models)
- [26: What are model aliases like gemini-flash-latest?](#26-what-are-model-aliases-like-gemini-flash-latest)
- [27: Why should you pin a specific model ID in production?](#27-why-should-you-pin-a-specific-model-id-in-production)
- [28: What is a token?](#28-what-is-a-token)
- [29: What is a context window?](#29-what-is-a-context-window)
- [30: How do input and output limits differ between Gemini 4 and Gemini 3?](#30-how-do-input-and-output-limits-differ-between-gemini-4-and-gemini-3)
- [31: How do you count tokens before sending a request?](#31-how-do-you-count-tokens-before-sending-a-request)
- [32: What is a prompt?](#32-what-is-a-prompt)
- [33: What are system instructions?](#33-what-are-system-instructions)
- [34: How do you set system instructions with generateContent?](#34-how-do-you-set-system-instructions-with-generatecontent)
- [35: What is output_text on an Interaction?](#35-what-is-output_text-on-an-interaction)
- [36: What are steps in the Interactions API?](#36-what-are-steps-in-the-interactions-api)
- [37: What does response.text return in generateContent?](#37-what-does-responsetext-return-in-generatecontent)
- [38: What are contents, parts and roles in generateContent?](#38-what-are-contents-parts-and-roles-in-generatecontent)
- [39: What roles exist in generateContent contents?](#39-what-roles-exist-in-generatecontent-contents)
- [40: What does max_output_tokens do?](#40-what-does-max_output_tokens-do)
- [41: What happened to temperature, top_p and top_k?](#41-what-happened-to-temperature-top_p-and-top_k)
- [42: What is thinking in Gemini models?](#42-what-is-thinking-in-gemini-models)
- [43: What values can thinking_level have?](#43-what-values-can-thinking_level-have)
- [44: Why does the default thinking level differ between models?](#44-why-does-the-default-thinking-level-differ-between-models)
- [45: Can you turn thinking off completely?](#45-can-you-turn-thinking-off-completely)
- [46: What are thinking summaries?](#46-what-are-thinking-summaries)
- [47: How are thought tokens billed?](#47-how-are-thought-tokens-billed)
- [48: Why would you use streaming?](#48-why-would-you-use-streaming)
- [49: How do you stream with the Interactions API?](#49-how-do-you-stream-with-the-interactions-api)
- [50: How do you stream with generateContent in Python?](#50-how-do-you-stream-with-generatecontent-in-python)
- [51: How do you stream with generateContent in JavaScript?](#51-how-do-you-stream-with-generatecontent-in-javascript)
- [52: Does the model remember previous messages on its own?](#52-does-the-model-remember-previous-messages-on-its-own)
- [53: What is previous_interaction_id?](#53-what-is-previous_interaction_id)
- [54: How do you build a chat with generateContent?](#54-how-do-you-build-a-chat-with-generatecontent)
- [55: What is the difference between stateful and stateless mode?](#55-what-is-the-difference-between-stateful-and-stateless-mode)
- [56: What does the store parameter do?](#56-what-does-the-store-parameter-do)
- [57: How long are stored interactions kept?](#57-how-long-are-stored-interactions-kept)
- [58: What kinds of input can Gemini models understand?](#58-what-kinds-of-input-can-gemini-models-understand)
- [59: How do you send an image with the Interactions API?](#59-how-do-you-send-an-image-with-the-interactions-api)
- [60: How do you send an image with generateContent?](#60-how-do-you-send-an-image-with-generatecontent)
- [61: What is the Files API?](#61-what-is-the-files-api)
- [62: What are the limits of the Files API?](#62-what-are-the-limits-of-the-files-api)
- [63: When do you need the Files API instead of inline data?](#63-when-do-you-need-the-files-api-instead-of-inline-data)
- [64: Can Gemini read PDFs?](#64-can-gemini-read-pdfs)
- [65: What can you do with audio input?](#65-what-can-you-do-with-audio-input)
- [66: What can you do with video input?](#66-what-can-you-do-with-video-input)
- [67: Can you pass files from Cloud Storage or a URL?](#67-can-you-pass-files-from-cloud-storage-or-a-url)
- [68: What is structured output?](#68-what-is-structured-output)
- [69: How do you get JSON output with the Interactions API?](#69-how-do-you-get-json-output-with-the-interactions-api)
- [70: How do you get JSON output with generateContent?](#70-how-do-you-get-json-output-with-generatecontent)
- [71: How do you use Pydantic with structured output?](#71-how-do-you-use-pydantic-with-structured-output)
- [72: How do you use Zod with structured output in JavaScript?](#72-how-do-you-use-zod-with-structured-output-in-javascript)
- [73: How do you make the model pick from a fixed list of labels?](#73-how-do-you-make-the-model-pick-from-a-fixed-list-of-labels)
- [74: What is function calling?](#74-what-is-function-calling)
- [75: How do you declare a function for the model?](#75-how-do-you-declare-a-function-for-the-model)
- [76: Does Gemini run your functions for you?](#76-does-gemini-run-your-functions-for-you)
- [77: What are built-in tools?](#77-what-are-built-in-tools)
- [78: What is Grounding with Google Search?](#78-what-is-grounding-with-google-search)
- [79: What is the URL Context tool?](#79-what-is-the-url-context-tool)
- [80: What is the Code Execution tool?](#80-what-is-the-code-execution-tool)
- [81: What is Grounding with Google Maps?](#81-what-is-grounding-with-google-maps)
- [82: What is the File Search tool?](#82-what-is-the-file-search-tool)
- [83: What is Computer Use?](#83-what-is-computer-use)
- [84: What does grounding mean?](#84-what-does-grounding-mean)
- [85: How do citations show up in responses?](#85-how-do-citations-show-up-in-responses)
- [86: What are embeddings?](#86-what-are-embeddings)
- [87: How do you create an embedding?](#87-how-do-you-create-an-embedding)
- [88: Which embedding models are available?](#88-which-embedding-models-are-available)
- [89: What does output_dimensionality do?](#89-what-does-output_dimensionality-do)
- [90: How do you tell the embedding model what the embedding is for?](#90-how-do-you-tell-the-embedding-model-what-the-embedding-is-for)
- [91: What is Nano Banana?](#91-what-is-nano-banana)
- [92: How do you generate an image?](#92-how-do-you-generate-an-image)
- [93: What is SynthID?](#93-what-is-synthid)
- [94: Can the Gemini API generate speech?](#94-can-the-gemini-api-generate-speech)
- [95: Is there a model just for transcription?](#95-is-there-a-model-just-for-transcription)
- [96: Can the Gemini API generate video?](#96-can-the-gemini-api-generate-video)
- [97: Can the Gemini API generate music?](#97-can-the-gemini-api-generate-music)
- [98: What is the Live API?](#98-what-is-the-live-api)
- [99: What audio formats does the Live API use?](#99-what-audio-formats-does-the-live-api-use)
- [100: What are ephemeral tokens?](#100-what-are-ephemeral-tokens)
- [101: What are safety settings?](#101-what-are-safety-settings)
- [102: What harm categories can you configure?](#102-what-harm-categories-can-you-configure)
- [103: What block thresholds are there?](#103-what-block-thresholds-are-there)
- [104: What happens when a request is blocked by safety filters in the Interactions API?](#104-what-happens-when-a-request-is-blocked-by-safety-filters-in-the-interactions-api)
- [105: What are rate limits?](#105-what-are-rate-limits)
- [106: What are RPM, TPM and RPD?](#106-what-are-rpm-tpm-and-rpd)
- [107: Are rate limits per API key or per project?](#107-are-rate-limits-per-api-key-or-per-project)
- [108: What are usage tiers?](#108-what-are-usage-tiers)
- [109: What's the difference between the free tier and the paid tier besides limits?](#109-whats-the-difference-between-the-free-tier-and-the-paid-tier-besides-limits)
- [110: What does a 429 error mean?](#110-what-does-a-429-error-mean)
- [111: How is Gemini API usage priced?](#111-how-is-gemini-api-usage-priced)
- [112: What is the Batch API?](#112-what-is-the-batch-api)
- [113: How much does the Batch API save?](#113-how-much-does-the-batch-api-save)
- [114: What is context caching?](#114-what-is-context-caching)
- [115: What is implicit caching?](#115-what-is-implicit-caching)
- [116: What is explicit caching?](#116-what-is-explicit-caching)
- [117: What is Flex inference?](#117-what-is-flex-inference)
- [118: What is Priority inference?](#118-what-is-priority-inference)
- [119: How do you choose a service tier for a request?](#119-how-do-you-choose-a-service-tier-for-a-request)
- [120: Can you use the OpenAI SDK with Gemini?](#120-can-you-use-the-openai-sdk-with-gemini)
- [121: How do you control thinking through the OpenAI-compatible endpoint?](#121-how-do-you-control-thinking-through-the-openai-compatible-endpoint)
- [122: What is the Gemini API CLI?](#122-what-is-the-gemini-api-cli)
- [123: What developer helpers does Google provide for working with the Gemini API in coding agents?](#123-what-developer-helpers-does-google-provide-for-working-with-the-gemini-api-in-coding-agents)
- [124: What are Managed Agents?](#124-what-are-managed-agents)
- [125: What is the Deep Research agent?](#125-what-is-the-deep-research-agent)
- [126: What's the difference between passing model and agent in the Interactions API?](#126-whats-the-difference-between-passing-model-and-agent-in-the-interactions-api)
- [127: What is background mode?](#127-what-is-background-mode)
- [128: What are webhooks in the Gemini API?](#128-what-are-webhooks-in-the-gemini-api)
- [129: What status values can an interaction have?](#129-what-status-values-can-an-interaction-have)
- [130: What finish reasons can a generateContent candidate have?](#130-what-finish-reasons-can-a-generatecontent-candidate-have)
- [131: What usage fields does an Interaction return?](#131-what-usage-fields-does-an-interaction-return)
- [132: What usage fields does generateContent return?](#132-what-usage-fields-does-generatecontent-return)
- [133: How do you catch API errors in the Python SDK?](#133-how-do-you-catch-api-errors-in-the-python-sdk)
- [134: What do the common HTTP error codes from the Gemini API mean?](#134-what-do-the-common-http-error-codes-from-the-gemini-api-mean)
- [135: How should you retry failed requests?](#135-how-should-you-retry-failed-requests)
- [136: Why shouldn't you call the Gemini API directly from a browser with your API key?](#136-why-shouldnt-you-call-the-gemini-api-directly-from-a-browser-with-your-api-key)
- [137: What are auth keys and how are they different from standard keys?](#137-what-are-auth-keys-and-how-are-they-different-from-standard-keys)
- [138: How do you restrict an API key?](#138-how-do-you-restrict-an-api-key)
- [139: What is Gemma and how is it related to Gemini?](#139-what-is-gemma-and-how-is-it-related-to-gemini)
- [140: What makes a good prompt for Gemini?](#140-what-makes-a-good-prompt-for-gemini)
- [141: What is few-shot prompting?](#141-what-is-few-shot-prompting)
- [142: Where should you put the question in a long-context prompt?](#142-where-should-you-put-the-question-in-a-long-context-prompt)
- [143: What is long context good for?](#143-what-is-long-context-good-for)
- [144: What is media_resolution?](#144-what-is-media_resolution)
- [145: How do you check a model's token limits from code?](#145-how-do-you-check-a-models-token-limits-from-code)
- [146: How do you list the available models?](#146-how-do-you-list-the-available-models)
- [147: How do you make async calls in Python?](#147-how-do-you-make-async-calls-in-python)
- [148: What is Firebase AI Logic?](#148-what-is-firebase-ai-logic)
- [149: What are logs and datasets in Google AI Studio?](#149-what-are-logs-and-datasets-in-google-ai-studio)
- [150: What is the "Get code" button in AI Studio for?](#150-what-is-the-get-code-button-in-ai-studio-for)

### Moderate Questions (151-300)

- [151: How do you migrate from google-generativeai to google-genai?](#151-how-do-you-migrate-from-google-generativeai-to-google-genai)
- [152: How do generateContent concepts map to the Interactions API?](#152-how-do-generatecontent-concepts-map-to-the-interactions-api)
- [153: What are the main fields of GenerateContentConfig?](#153-what-are-the-main-fields-of-generatecontentconfig)
- [154: Can you pass plain dicts instead of typed objects in the Python SDK?](#154-can-you-pass-plain-dicts-instead-of-typed-objects-in-the-python-sdk)
- [155: How do you send several files and text in one Interactions request?](#155-how-do-you-send-several-files-and-text-in-one-interactions-request)
- [156: How do you set media resolution per item?](#156-how-do-you-set-media-resolution-per-item)
- [157: How do you choose the right media resolution?](#157-how-do-you-choose-the-right-media-resolution)
- [158: How many tokens does an image cost?](#158-how-many-tokens-does-an-image-cost)
- [159: How do you count tokens for a request with files?](#159-how-do-you-count-tokens-for-a-request-with-files)
- [160: Why might you need to wait after uploading a video?](#160-why-might-you-need-to-wait-after-uploading-a-video)
- [161: How do you list and delete uploaded files?](#161-how-do-you-list-and-delete-uploaded-files)
- [162: What events does the Interactions API send when streaming?](#162-what-events-does-the-interactions-api-send-when-streaming)
- [163: What delta types can a step.delta event have?](#163-what-delta-types-can-a-stepdelta-event-have)
- [164: How do you stream with the Interactions API in JavaScript?](#164-how-do-you-stream-with-the-interactions-api-in-javascript)
- [165: How does streaming work over REST for generateContent?](#165-how-does-streaming-work-over-rest-for-generatecontent)
- [166: How does a full function calling loop look in the Interactions API?](#166-how-does-a-full-function-calling-loop-look-in-the-interactions-api)
- [167: How does manual function calling look with generateContent?](#167-how-does-manual-function-calling-look-with-generatecontent)
- [168: What is automatic function calling in the Python SDK?](#168-what-is-automatic-function-calling-in-the-python-sdk)
- [169: How do you turn off automatic function calling?](#169-how-do-you-turn-off-automatic-function-calling)
- [170: What are the function calling modes?](#170-what-are-the-function-calling-modes)
- [171: How do you restrict which functions the model can call?](#171-how-do-you-restrict-which-functions-the-model-can-call)
- [172: What is parallel function calling?](#172-what-is-parallel-function-calling)
- [173: What is compositional function calling?](#173-what-is-compositional-function-calling)
- [174: Why does the call_id matter in function results?](#174-why-does-the-call_id-matter-in-function-results)
- [175: How do you write good function declarations?](#175-how-do-you-write-good-function-declarations)
- [176: How many functions should you give the model at once?](#176-how-many-functions-should-you-give-the-model-at-once)
- [177: Can you combine built-in tools with your own functions?](#177-can-you-combine-built-in-tools-with-your-own-functions)
- [178: What is gemini-3.1-pro-preview-customtools?](#178-what-is-gemini-31-pro-preview-customtools)
- [179: Can a function result include images or files?](#179-can-a-function-result-include-images-or-files)
- [180: How should you handle errors inside a function?](#180-how-should-you-handle-errors-inside-a-function)
- [181: What JSON Schema features does structured output support?](#181-what-json-schema-features-does-structured-output-support)
- [182: Which JSON Schema keywords are ignored?](#182-which-json-schema-keywords-are-ignored)
- [183: How do you make a field nullable in a schema?](#183-how-do-you-make-a-field-nullable-in-a-schema)
- [184: Can structured output schemas be recursive?](#184-can-structured-output-schemas-be-recursive)
- [185: Can you use structured output together with tools?](#185-can-you-use-structured-output-together-with-tools)
- [186: How does streaming work with structured output?](#186-how-does-streaming-work-with-structured-output)
- [187: Why should you still validate structured output?](#187-why-should-you-still-validate-structured-output)
- [188: What do you do when a schema is rejected as too complex?](#188-what-do-you-do-when-a-schema-is-rejected-as-too-complex)
- [189: Can you ask for JSON without a schema?](#189-can-you-ask-for-json-without-a-schema)
- [190: How do you read Google Search grounding results from an interaction?](#190-how-do-you-read-google-search-grounding-results-from-an-interaction)
- [191: Are there display rules for Google Search grounding results?](#191-are-there-display-rules-for-google-search-grounding-results)
- [192: How is Google Search grounding billed?](#192-how-is-google-search-grounding-billed)
- [193: What are the limits of the URL Context tool?](#193-what-are-the-limits-of-the-url-context-tool)
- [194: How do you check whether URL Context actually fetched a page?](#194-how-do-you-check-whether-url-context-actually-fetched-a-page)
- [195: When would you combine URL Context with Google Search?](#195-when-would-you-combine-url-context-with-google-search)
- [196: What libraries can the Code Execution tool use?](#196-what-libraries-can-the-code-execution-tool-use)
- [197: How do you read code execution output?](#197-how-do-you-read-code-execution-output)
- [198: How is Code Execution billed?](#198-how-is-code-execution-billed)
- [199: How do you set up File Search?](#199-how-do-you-set-up-file-search)
- [200: What is the difference between uploading and importing into a File Search store?](#200-what-is-the-difference-between-uploading-and-importing-into-a-file-search-store)
- [201: How do you control chunking in File Search?](#201-how-do-you-control-chunking-in-file-search)
- [202: How do you filter File Search results by metadata?](#202-how-do-you-filter-file-search-results-by-metadata)
- [203: How is File Search priced?](#203-how-is-file-search-priced)
- [204: What are the File Search limits?](#204-what-are-the-file-search-limits)
- [205: When would you use File Search instead of your own RAG pipeline?](#205-when-would-you-use-file-search-instead-of-your-own-rag-pipeline)
- [206: How do you build semantic search with Gemini embeddings?](#206-how-do-you-build-semantic-search-with-gemini-embeddings)
- [207: When do you need to normalize Gemini embeddings?](#207-when-do-you-need-to-normalize-gemini-embeddings)
- [208: How do you embed many texts efficiently?](#208-how-do-you-embed-many-texts-efficiently)
- [209: How do multimodal embeddings work with gemini-embedding-2?](#209-how-do-multimodal-embeddings-work-with-gemini-embedding-2)
- [210: Can you mix embeddings from gemini-embedding-001 and gemini-embedding-2?](#210-can-you-mix-embeddings-from-gemini-embedding-001-and-gemini-embedding-2)
- [211: How do you create and use an explicit cache?](#211-how-do-you-create-and-use-an-explicit-cache)
- [212: How do you update or delete an explicit cache?](#212-how-do-you-update-or-delete-an-explicit-cache)
- [213: How is explicit caching billed?](#213-how-is-explicit-caching-billed)
- [214: How do you get more implicit cache hits?](#214-how-do-you-get-more-implicit-cache-hits)
- [215: How do you check whether you got cache hits?](#215-how-do-you-check-whether-you-got-cache-hits)
- [216: What is the difference between inline and file input for batch jobs?](#216-what-is-the-difference-between-inline-and-file-input-for-batch-jobs)
- [217: What does a batch JSONL file look like?](#217-what-does-a-batch-jsonl-file-look-like)
- [218: How do you create a batch job and wait for it?](#218-how-do-you-create-a-batch-job-and-wait-for-it)
- [219: What states can a batch job be in?](#219-what-states-can-a-batch-job-be-in)
- [220: Should you poll batch jobs or use webhooks?](#220-should-you-poll-batch-jobs-or-use-webhooks)
- [221: How do you handle errors inside a successful batch job?](#221-how-do-you-handle-errors-inside-a-successful-batch-job)
- [222: Is creating a batch job idempotent?](#222-is-creating-a-batch-job-idempotent)
- [223: How should you handle errors with Flex requests?](#223-how-should-you-handle-errors-with-flex-requests)
- [224: How do you choose between Standard, Priority, Flex and Batch?](#224-how-do-you-choose-between-standard-priority-flex-and-batch)
- [225: How do you pick a thinking level?](#225-how-do-you-pick-a-thinking-level)
- [226: What happens if max_output_tokens is reached while the model is thinking?](#226-what-happens-if-max_output_tokens-is-reached-while-the-model-is-thinking)
- [227: What is thinking_budget?](#227-what-is-thinking_budget)
- [228: What are thought signatures?](#228-what-are-thought-signatures)
- [229: How do you handle thought signatures?](#229-how-do-you-handle-thought-signatures)
- [230: How do you keep history yourself in stateless mode?](#230-how-do-you-keep-history-yourself-in-stateless-mode)
- [231: Can you switch models in the middle of a conversation?](#231-can-you-switch-models-in-the-middle-of-a-conversation)
- [232: Which parameters are not carried over by previous_interaction_id?](#232-which-parameters-are-not-carried-over-by-previous_interaction_id)
- [233: How do you run an interaction in the background and get the result?](#233-how-do-you-run-an-interaction-in-the-background-and-get-the-result)
- [234: How do you delete a stored interaction?](#234-how-do-you-delete-a-stored-interaction)
- [235: How do you edit an image with Nano Banana?](#235-how-do-you-edit-an-image-with-nano-banana)
- [236: How many reference images can you use for image generation?](#236-how-many-reference-images-can-you-use-for-image-generation)
- [237: How do you read images from a response that mixes text and images?](#237-how-do-you-read-images-from-a-response-that-mixes-text-and-images)
- [238: How do you create multi-speaker audio with TTS?](#238-how-do-you-create-multi-speaker-audio-with-tts)
- [239: How do you connect to the Live API in Python?](#239-how-do-you-connect-to-the-live-api-in-python)
- [240: How do you stream microphone audio to the Live API?](#240-how-do-you-stream-microphone-audio-to-the-live-api)
- [241: How does voice activity detection (VAD) work in the Live API?](#241-how-does-voice-activity-detection-vad-work-in-the-live-api)
- [242: How do interruptions work in the Live API?](#242-how-do-interruptions-work-in-the-live-api)
- [243: How do you get transcripts from a Live session?](#243-how-do-you-get-transcripts-from-a-live-session)
- [244: What are the Live API session limits?](#244-what-are-the-live-api-session-limits)
- [245: How does session resumption work in the Live API?](#245-how-does-session-resumption-work-in-the-live-api)
- [246: What is context window compression in the Live API?](#246-what-is-context-window-compression-in-the-live-api)
- [247: Can you use tools in the Live API?](#247-can-you-use-tools-in-the-live-api)
- [248: How do you create an ephemeral token?](#248-how-do-you-create-an-ephemeral-token)
- [249: How do you lock an ephemeral token to a specific config?](#249-how-do-you-lock-an-ephemeral-token-to-a-specific-config)
- [250: When should a Live app connect client-to-server vs server-to-server?](#250-when-should-a-live-app-connect-client-to-server-vs-server-to-server)
- [251: How do you set safety settings in the Interactions API?](#251-how-do-you-set-safety-settings-in-the-interactions-api)
- [252: How do you set safety settings with generateContent?](#252-how-do-you-set-safety-settings-with-generatecontent)
- [253: How do you detect a blocked response in generateContent?](#253-how-do-you-detect-a-blocked-response-in-generatecontent)
- [254: What is the jailbreak safety category?](#254-what-is-the-jailbreak-safety-category)
- [255: How do you point the Google GenAI SDK at Vertex AI?](#255-how-do-you-point-the-google-genai-sdk-at-vertex-ai)
- [256: Which environment variables switch the SDK to Vertex AI?](#256-which-environment-variables-switch-the-sdk-to-vertex-ai)
- [257: When would you choose Vertex AI over the Gemini API?](#257-when-would-you-choose-vertex-ai-over-the-gemini-api)
- [258: How do you set the API version or timeout in the Python SDK?](#258-how-do-you-set-the-api-version-or-timeout-in-the-python-sdk)
- [259: How do you configure retries in the Python SDK?](#259-how-do-you-configure-retries-in-the-python-sdk)
- [260: How do you run many requests at once in Python without hitting rate limits?](#260-how-do-you-run-many-requests-at-once-in-python-without-hitting-rate-limits)
- [261: How do you handle API errors in the JavaScript SDK?](#261-how-do-you-handle-api-errors-in-the-javascript-sdk)
- [262: How do you write a retry with exponential backoff and jitter?](#262-how-do-you-write-a-retry-with-exponential-backoff-and-jitter)
- [263: What are spend caps?](#263-what-are-spend-caps)
- [264: What are spend-based rate limits?](#264-what-are-spend-based-rate-limits)
- [265: How do you monitor usage and cost?](#265-how-do-you-monitor-usage-and-cost)
- [266: How do you use AI Studio logs for debugging?](#266-how-do-you-use-ai-studio-logs-for-debugging)
- [267: How do you pass Gemini-specific options through the OpenAI-compatible endpoint?](#267-how-do-you-pass-gemini-specific-options-through-the-openai-compatible-endpoint)
- [268: What are the limits of the OpenAI-compatible endpoint?](#268-what-are-the-limits-of-the-openai-compatible-endpoint)
- [269: How do you call Gemini from a Next.js route handler?](#269-how-do-you-call-gemini-from-a-nextjs-route-handler)
- [270: How do you stream a Gemini response to the browser from Node.js?](#270-how-do-you-stream-a-gemini-response-to-the-browser-from-nodejs)
- [271: How would you build an Express proxy for Gemini?](#271-how-would-you-build-an-express-proxy-for-gemini)
- [272: Can you use Gemini with the Vercel AI SDK or LangChain?](#272-can-you-use-gemini-with-the-vercel-ai-sdk-or-langchain)
- [273: How do you unit test code that calls the Gemini API?](#273-how-do-you-unit-test-code-that-calls-the-gemini-api)
- [274: How do you evaluate prompt changes?](#274-how-do-you-evaluate-prompt-changes)
- [275: How should you manage prompts in a codebase?](#275-how-should-you-manage-prompts-in-a-codebase)
- [276: When does many-shot prompting help?](#276-when-does-many-shot-prompting-help)
- [277: How do you summarize a long PDF with Gemini?](#277-how-do-you-summarize-a-long-pdf-with-gemini)
- [278: What file types beyond PDF can Gemini read?](#278-what-file-types-beyond-pdf-can-gemini-read)
- [279: How do you call computer use in a loop?](#279-how-do-you-call-computer-use-in-a-loop)
- [280: How do coordinates work in Computer Use?](#280-how-do-coordinates-work-in-computer-use)
- [281: How do you handle safety confirmations in Computer Use?](#281-how-do-you-handle-safety-confirmations-in-computer-use)
- [282: How do you customize the actions available in Computer Use?](#282-how-do-you-customize-the-actions-available-in-computer-use)
- [283: What is the intent field in Computer Use actions?](#283-what-is-the-intent-field-in-computer-use-actions)
- [284: How do you call a Managed Agent?](#284-how-do-you-call-a-managed-agent)
- [285: What is the difference between conversation state and environment state in Managed Agents?](#285-what-is-the-difference-between-conversation-state-and-environment-state-in-managed-agents)
- [286: How do you save and reuse a Managed Agent configuration?](#286-how-do-you-save-and-reuse-a-managed-agent-configuration)
- [287: How do you register a webhook?](#287-how-do-you-register-a-webhook)
- [288: How do you verify a static webhook request?](#288-how-do-you-verify-a-static-webhook-request)
- [289: What's in a webhook payload?](#289-whats-in-a-webhook-payload)
- [290: What do you do when a model you use is deprecated?](#290-what-do-you-do-when-a-model-you-use-is-deprecated)
- [291: How does the Interactions API report token usage per modality?](#291-how-does-the-interactions-api-report-token-usage-per-modality)
- [292: How do you cancel or stop a long-running request?](#292-how-do-you-cancel-or-stop-a-long-running-request)
- [293: How do you show thinking progress in a chat UI?](#293-how-do-you-show-thinking-progress-in-a-chat-ui)
- [294: How do you get the function arguments while streaming?](#294-how-do-you-get-the-function-arguments-while-streaming)
- [295: How do you extract structured data from images, like receipts?](#295-how-do-you-extract-structured-data-from-images-like-receipts)
- [296: How do you classify text cheaply at high volume?](#296-how-do-you-classify-text-cheaply-at-high-volume)
- [297: How do you translate text with Gemini while keeping formatting?](#297-how-do-you-translate-text-with-gemini-while-keeping-formatting)
- [298: How do you ask questions about a video at specific times?](#298-how-do-you-ask-questions-about-a-video-at-specific-times)
- [299: How do you use Gemini for code review in a CI job?](#299-how-do-you-use-gemini-for-code-review-in-a-ci-job)
- [300: How do you choose between Gemini 4 Argon, Gemini 3.8 Flash and Flash-Lite for a feature?](#300-how-do-you-choose-between-gemini-4-argon-gemini-38-flash-and-flash-lite-for-a-feature)

### Advanced Questions (301-450)

- [301: Why did Google add the Interactions API when generateContent already existed?](#301-why-did-google-add-the-interactions-api-when-generatecontent-already-existed)
- [302: What are the trade-offs of server-side conversation state?](#302-what-are-the-trade-offs-of-server-side-conversation-state)
- [303: What do you need to think about when using store=False for compliance?](#303-what-do-you-need-to-think-about-when-using-storefalse-for-compliance)
- [304: How is your data treated on the free tier vs the paid tier?](#304-how-is-your-data-treated-on-the-free-tier-vs-the-paid-tier)
- [305: Why are thought signatures encrypted instead of plain text?](#305-why-are-thought-signatures-encrypted-instead-of-plain-text)
- [306: What goes wrong if you drop or edit thought signatures?](#306-what-goes-wrong-if-you-drop-or-edit-thought-signatures)
- [307: How does prefix matching affect caching, and how do you design prompts around it?](#307-how-does-prefix-matching-affect-caching-and-how-do-you-design-prompts-around-it)
- [308: What's special about caching on Gemini 4 in agent loops?](#308-whats-special-about-caching-on-gemini-4-in-agent-loops)
- [309: Why can agent loops get expensive quickly?](#309-why-can-agent-loops-get-expensive-quickly)
- [310: How do you estimate the cost of a request?](#310-how-do-you-estimate-the-cost-of-a-request)
- [311: What are the main ways to cut Gemini API costs?](#311-what-are-the-main-ways-to-cut-gemini-api-costs)
- [312: How do you reduce latency?](#312-how-do-you-reduce-latency)
- [313: How would you measure whether a higher thinking level is worth it?](#313-how-would-you-measure-whether-a-higher-thinking-level-is-worth-it)
- [314: How would you design model routing?](#314-how-would-you-design-model-routing)
- [315: How do you build a fallback when a model is overloaded?](#315-how-do-you-build-a-fallback-when-a-model-is-overloaded)
- [316: How do you avoid hitting rate limits in a busy system?](#316-how-do-you-avoid-hitting-rate-limits-in-a-busy-system)
- [317: Why shouldn't you spread traffic over many projects to get around rate limits?](#317-why-shouldnt-you-spread-traffic-over-many-projects-to-get-around-rate-limits)
- [318: How would you design a pipeline to process millions of documents?](#318-how-would-you-design-a-pipeline-to-process-millions-of-documents)
- [319: How do you make request processing idempotent around the Gemini API?](#319-how-do-you-make-request-processing-idempotent-around-the-gemini-api)
- [320: Webhooks are at-least-once. How do you handle duplicates?](#320-webhooks-are-at-least-once-how-do-you-handle-duplicates)
- [321: How do you protect a webhook endpoint from replay attacks?](#321-how-do-you-protect-a-webhook-endpoint-from-replay-attacks)
- [322: How do you verify a dynamic webhook?](#322-how-do-you-verify-a-dynamic-webhook)
- [323: What is prompt injection, and why does it matter more with tools?](#323-what-is-prompt-injection-and-why-does-it-matter-more-with-tools)
- [324: How can Google Search or URL Context results be used to attack your app?](#324-how-can-google-search-or-url-context-results-be-used-to-attack-your-app)
- [325: What does Computer Use offer against prompt injection?](#325-what-does-computer-use-offer-against-prompt-injection)
- [326: How do you design functions with least privilege?](#326-how-do-you-design-functions-with-least-privilege)
- [327: How do you add human approval to risky tool calls?](#327-how-do-you-add-human-approval-to-risky-tool-calls)
- [328: Why should you validate function arguments yourself?](#328-why-should-you-validate-function-arguments-yourself)
- [329: What do you do if an API key leaks?](#329-what-do-you-do-if-an-api-key-leaks)
- [330: Why are auth keys safer than standard API keys?](#330-why-are-auth-keys-safer-than-standard-api-keys)
- [331: What's the threat model for ephemeral tokens?](#331-whats-the-threat-model-for-ephemeral-tokens)
- [332: How do you keep tenants' data separate in File Search?](#332-how-do-you-keep-tenants-data-separate-in-file-search)
- [333: How do you handle personal data (PII) with the Gemini API?](#333-how-do-you-handle-personal-data-pii-with-the-gemini-api)
- [334: How should you log prompts and responses safely?](#334-how-should-you-log-prompts-and-responses-safely)
- [335: Are Gemini's safety filters enough for content moderation?](#335-are-geminis-safety-filters-enough-for-content-moderation)
- [336: How do you check that extracted values are actually correct?](#336-how-do-you-check-that-extracted-values-are-actually-correct)
- [337: How do you design schemas that make the model more reliable?](#337-how-do-you-design-schemas-that-make-the-model-more-reliable)
- [338: How do you handle a JSON response that was cut off?](#338-how-do-you-handle-a-json-response-that-was-cut-off)
- [339: How do you get very long outputs, like a whole report or codebase?](#339-how-do-you-get-very-long-outputs-like-a-whole-report-or-codebase)
- [340: What does a shared context window on Gemini 4 mean for your app?](#340-what-does-a-shared-context-window-on-gemini-4-mean-for-your-app)
- [341: When should you use long context instead of RAG?](#341-when-should-you-use-long-context-instead-of-rag)
- [342: What are the limits of long context retrieval?](#342-what-are-the-limits-of-long-context-retrieval)
- [343: How should you chunk documents for File Search or your own RAG?](#343-how-should-you-chunk-documents-for-file-search-or-your-own-rag)
- [344: How would you combine File Search with your own functions?](#344-how-would-you-combine-file-search-with-your-own-functions)
- [345: How do you pick an embedding dimension?](#345-how-do-you-pick-an-embedding-dimension)
- [346: How do you use Gemini embeddings with a vector database?](#346-how-do-you-use-gemini-embeddings-with-a-vector-database)
- [347: Why do query and document embeddings use different prefixes or task types?](#347-why-do-query-and-document-embeddings-use-different-prefixes-or-task-types)
- [348: How do you measure retrieval quality?](#348-how-do-you-measure-retrieval-quality)
- [349: How do you design a reliable agent loop with function calling?](#349-how-do-you-design-a-reliable-agent-loop-with-function-calling)
- [350: When should an agent loop stop?](#350-when-should-an-agent-loop-stop)
- [351: How do you stop an agent's context from growing forever?](#351-how-do-you-stop-an-agents-context-from-growing-forever)
- [352: How would you implement conversation summarization for long chats?](#352-how-would-you-implement-conversation-summarization-for-long-chats)
- [353: How do you handle parallel function calls correctly?](#353-how-do-you-handle-parallel-function-calls-correctly)
- [354: How do you deal with tool results that are too large?](#354-how-do-you-deal-with-tool-results-that-are-too-large)
- [355: How do you stream function call arguments to update a UI early?](#355-how-do-you-stream-function-call-arguments-to-update-a-ui-early)
- [356: How do you handle backpressure when streaming from Node.js?](#356-how-do-you-handle-backpressure-when-streaming-from-nodejs)
- [357: How do you cancel an in-flight request in the JavaScript SDK?](#357-how-do-you-cancel-an-in-flight-request-in-the-javascript-sdk)
- [358: How do you set timeouts for requests with heavy thinking?](#358-how-do-you-set-timeouts-for-requests-with-heavy-thinking)
- [359: When should you use background mode instead of a synchronous call?](#359-when-should-you-use-background-mode-instead-of-a-synchronous-call)
- [360: How would you design the architecture of a voice support agent?](#360-how-would-you-design-the-architecture-of-a-voice-support-agent)
- [361: What adds latency in a voice agent, and how do you reduce it?](#361-what-adds-latency-in-a-voice-agent-and-how-do-you-reduce-it)
- [362: What are the common bugs with Live API interruptions?](#362-what-are-the-common-bugs-with-live-api-interruptions)
- [363: How do you keep a Live session going for an hour-long call?](#363-how-do-you-keep-a-live-session-going-for-an-hour-long-call)
- [364: How do function calls work in a Live session without freezing the conversation?](#364-how-do-function-calls-work-in-a-live-session-without-freezing-the-conversation)
- [365: What do you need to watch for with audio formats in the Live API?](#365-what-do-you-need-to-watch-for-with-audio-formats-in-the-live-api)
- [366: When would you use gemini-3.8-live-extended-thinking instead of gemini-3.8-live?](#366-when-would-you-use-gemini-38-live-extended-thinking-instead-of-gemini-38-live)
- [367: Why can't a text-only model continue some conversations?](#367-why-cant-a-text-only-model-continue-some-conversations)
- [368: How do you safely migrate to a new model version?](#368-how-do-you-safely-migrate-to-a-new-model-version)
- [369: What is the risk of model IDs that get routed to newer models?](#369-what-is-the-risk-of-model-ids-that-get-routed-to-newer-models)
- [370: With temperature deprecated, how do you get more consistent outputs?](#370-with-temperature-deprecated-how-do-you-get-more-consistent-outputs)
- [371: How do you test features built on a non-deterministic model?](#371-how-do-you-test-features-built-on-a-non-deterministic-model)
- [372: How do you build a regression test set for prompts?](#372-how-do-you-build-a-regression-test-set-for-prompts)
- [373: How do you use Gemini as an LLM judge?](#373-how-do-you-use-gemini-as-an-llm-judge)
- [374: What should you log for observability of Gemini calls?](#374-what-should-you-log-for-observability-of-gemini-calls)
- [375: How would you trace a multi-step agent run?](#375-how-would-you-trace-a-multi-step-agent-run)
- [376: What are the privacy implications of AI Studio logs being on by default?](#376-what-are-the-privacy-implications-of-ai-studio-logs-being-on-by-default)
- [377: How do you attribute Gemini costs to features or customers?](#377-how-do-you-attribute-gemini-costs-to-features-or-customers)
- [378: How do you put budget guardrails into an app?](#378-how-do-you-put-budget-guardrails-into-an-app)
- [379: When does it make sense to cache final answers yourself?](#379-when-does-it-make-sense-to-cache-final-answers-yourself)
- [380: How do you decide if explicit caching saves money?](#380-how-do-you-decide-if-explicit-caching-saves-money)
- [381: Explicit caching isn't available for Gemini 4 Argon or the Interactions API. What do you do?](#381-explicit-caching-isnt-available-for-gemini-4-argon-or-the-interactions-api-what-do-you-do)
- [382: Can you combine the Batch API with caching?](#382-can-you-combine-the-batch-api-with-caching)
- [383: How do you handle a batch job that expires?](#383-how-do-you-handle-a-batch-job-that-expires)
- [384: How do you keep the cost of video analysis under control?](#384-how-do-you-keep-the-cost-of-video-analysis-under-control)
- [385: What is agentic video understanding?](#385-what-is-agentic-video-understanding)
- [386: How does Gemini handle PDFs with both text and images?](#386-how-does-gemini-handle-pdfs-with-both-text-and-images)
- [387: How do you improve OCR accuracy on small or dense text?](#387-how-do-you-improve-ocr-accuracy-on-small-or-dense-text)
- [388: How would you run image generation at scale in a product?](#388-how-would-you-run-image-generation-at-scale-in-a-product)
- [389: How do you keep a character or product consistent across many generated images?](#389-how-do-you-keep-a-character-or-product-consistent-across-many-generated-images)
- [390: How do you meet data residency requirements with Gemini?](#390-how-do-you-meet-data-residency-requirements-with-gemini)
- [391: What enterprise security features push teams to Vertex AI?](#391-what-enterprise-security-features-push-teams-to-vertex-ai)
- [392: How do you write code that runs on both the Gemini API and Vertex AI?](#392-how-do-you-write-code-that-runs-on-both-the-gemini-api-and-vertex-ai)
- [393: Why should you pin SDK versions?](#393-why-should-you-pin-sdk-versions)
- [394: How do you handle breaking changes announced in the changelog?](#394-how-do-you-handle-breaking-changes-announced-in-the-changelog)
- [395: When would you call the REST API directly instead of using an SDK?](#395-when-would-you-call-the-rest-api-directly-instead-of-using-an-sdk)
- [396: How would you design a provider-agnostic LLM layer that includes Gemini?](#396-how-would-you-design-a-provider-agnostic-llm-layer-that-includes-gemini)
- [397: What are the pros and cons of using the OpenAI-compatible endpoint in production?](#397-what-are-the-pros-and-cons-of-using-the-openai-compatible-endpoint-in-production)
- [398: When should you use function calling vs structured output?](#398-when-should-you-use-function-calling-vs-structured-output)
- [399: How would you build extraction with citations to sources?](#399-how-would-you-build-extraction-with-citations-to-sources)
- [400: What techniques reduce hallucinations with the Gemini API?](#400-what-techniques-reduce-hallucinations-with-the-gemini-api)
- [401: How do you check that citations actually support the text?](#401-how-do-you-check-that-citations-actually-support-the-text)
- [402: How do you keep Google Search grounding costs under control at scale?](#402-how-do-you-keep-google-search-grounding-costs-under-control-at-scale)
- [403: How do Maps grounding and Search grounding differ in use?](#403-how-do-maps-grounding-and-search-grounding-differ-in-use)
- [404: Is Code Execution safe to use with untrusted input?](#404-is-code-execution-safe-to-use-with-untrusted-input)
- [405: When would you use your own sandbox instead of the built-in Code Execution tool?](#405-when-would-you-use-your-own-sandbox-instead-of-the-built-in-code-execution-tool)
- [406: When should you use Managed Agents vs your own agent loop?](#406-when-should-you-use-managed-agents-vs-your-own-agent-loop)
- [407: Why does forking the base environment matter for saved agents?](#407-why-does-forking-the-base-environment-matter-for-saved-agents)
- [408: How would you integrate Deep Research into a product?](#408-how-would-you-integrate-deep-research-into-a-product)
- [409: How can you mix agents and models in one conversation?](#409-how-can-you-mix-agents-and-models-in-one-conversation)
- [410: Can Gemini use remote MCP servers directly?](#410-can-gemini-use-remote-mcp-servers-directly)
- [411: How would you map MCP tools to Gemini function declarations?](#411-how-would-you-map-mcp-tools-to-gemini-function-declarations)
- [412: How would you run Computer Use safely in production?](#412-how-would-you-run-computer-use-safely-in-production)
- [413: How do the browser, mobile and desktop environments differ in Computer Use?](#413-how-do-the-browser-mobile-and-desktop-environments-differ-in-computer-use)
- [414: Scenario: design a chatbot that answers questions about your company's internal docs.](#414-scenario-design-a-chatbot-that-answers-questions-about-your-companys-internal-docs)
- [415: Scenario: you need to classify 5 million support tickets by tomorrow.](#415-scenario-you-need-to-classify-5-million-support-tickets-by-tomorrow)
- [416: Scenario: build invoice extraction for an accounting app.](#416-scenario-build-invoice-extraction-for-an-accounting-app)
- [417: Scenario: build a voice agent for restaurant reservations.](#417-scenario-build-a-voice-agent-for-restaurant-reservations)
- [418: Scenario: your Gemini bill doubled overnight. How do you investigate?](#418-scenario-your-gemini-bill-doubled-overnight-how-do-you-investigate)
- [419: Scenario: users get 429 errors at peak times. What do you do?](#419-scenario-users-get-429-errors-at-peak-times-what-do-you-do)
- [420: Scenario: some responses come back empty or cut off. How do you debug?](#420-scenario-some-responses-come-back-empty-or-cut-off-how-do-you-debug)
- [421: Scenario: the model sometimes returns JSON that your code can't parse.](#421-scenario-the-model-sometimes-returns-json-that-your-code-cant-parse)
- [422: Scenario: the model keeps calling a function with wrong arguments.](#422-scenario-the-model-keeps-calling-a-function-with-wrong-arguments)
- [423: Scenario: after switching to a newer model, requests start failing with 400 errors.](#423-scenario-after-switching-to-a-newer-model-requests-start-failing-with-400-errors)
- [424: Scenario: your logs show deprecation warnings for temperature after upgrading to Gemini 3.8 Flash.](#424-scenario-your-logs-show-deprecation-warnings-for-temperature-after-upgrading-to-gemini-38-flash)
- [425: Scenario: users say the bot "forgot" a file they uploaded two days ago.](#425-scenario-users-say-the-bot-forgot-a-file-they-uploaded-two-days-ago)
- [426: Scenario: streamed responses sometimes stop in the middle.](#426-scenario-streamed-responses-sometimes-stop-in-the-middle)
- [427: Scenario: Live API voice sessions drop after about 10-15 minutes.](#427-scenario-live-api-voice-sessions-drop-after-about-10-15-minutes)
- [428: Scenario: you found your API key in a public GitHub repo.](#428-scenario-you-found-your-api-key-in-a-public-github-repo)
- [429: Scenario: one big customer uses most of your quota in a multi-tenant SaaS.](#429-scenario-one-big-customer-uses-most-of-your-quota-in-a-multi-tenant-saas)
- [430: Scenario: you still use gemini-2.5-flash in production in November 2026.](#430-scenario-you-still-use-gemini-25-flash-in-production-in-november-2026)
- [431: Scenario: autocomplete suggestions are too slow.](#431-scenario-autocomplete-suggestions-are-too-slow)
- [432: Scenario: decide between Gemini 4 Argon and Gemini 3.8 Flash for a coding assistant.](#432-scenario-decide-between-gemini-4-argon-and-gemini-38-flash-for-a-coding-assistant)
- [433: Scenario: a chat conversation has grown so long that each turn is slow and expensive.](#433-scenario-a-chat-conversation-has-grown-so-long-that-each-turn-is-slow-and-expensive)
- [434: Scenario: translate a 300-page document.](#434-scenario-translate-a-300-page-document)
- [435: Scenario: summarize hour-long meeting recordings cheaply.](#435-scenario-summarize-hour-long-meeting-recordings-cheaply)
- [436: Scenario: build an automated code review bot for pull requests.](#436-scenario-build-an-automated-code-review-bot-for-pull-requests)
- [437: Scenario: design a moderation pipeline for user-generated posts.](#437-scenario-design-a-moderation-pipeline-for-user-generated-posts)
- [438: Scenario: run offline evaluation of a new prompt on 50,000 examples.](#438-scenario-run-offline-evaluation-of-a-new-prompt-on-50000-examples)
- [439: Scenario: a user asks you to delete all their data. What do you remove on the Gemini side?](#439-scenario-a-user-asks-you-to-delete-all-their-data-what-do-you-remove-on-the-gemini-side)
- [440: Scenario: the business requires that answers come only from approved documents.](#440-scenario-the-business-requires-that-answers-come-only-from-approved-documents)
- [441: Scenario: an agent keeps calling the same tool over and over.](#441-scenario-an-agent-keeps-calling-the-same-tool-over-and-over)
- [442: Scenario: one tool returns 200K tokens of data and the model gets slow and confused.](#442-scenario-one-tool-returns-200k-tokens-of-data-and-the-model-gets-slow-and-confused)
- [443: Scenario: your team wants to switch from OpenAI to Gemini. How do you plan it?](#443-scenario-your-team-wants-to-switch-from-openai-to-gemini-how-do-you-plan-it)
- [444: Scenario: generated images often have spelling mistakes in the text.](#444-scenario-generated-images-often-have-spelling-mistakes-in-the-text)
- [445: Scenario: upgrade from gemini-embedding-001 to gemini-embedding-2 with no downtime.](#445-scenario-upgrade-from-gemini-embedding-001-to-gemini-embedding-2-with-no-downtime)
- [446: Scenario: the Interactions API response format changed and production broke.](#446-scenario-the-interactions-api-response-format-changed-and-production-broke)
- [447: Scenario: you need the same answer every time for the same input, for audit reasons.](#447-scenario-you-need-the-same-answer-every-time-for-the-same-input-for-audit-reasons)
- [448: Scenario: a feature works on the free tier in testing but fails in production on the paid tier.](#448-scenario-a-feature-works-on-the-free-tier-in-testing-but-fails-in-production-on-the-paid-tier)
- [449: Scenario: you need to process user-uploaded videos that may contain sensitive content.](#449-scenario-you-need-to-process-user-uploaded-videos-that-may-contain-sensitive-content)
- [450: What would you check before taking a Gemini API feature to production?](#450-what-would-you-check-before-taking-a-gemini-api-feature-to-production)

---

# Easy Questions (1-150)

## 1: What is the Gemini API?

The Gemini API is Google's HTTP API for using Gemini models from your own code. You send text, images, audio, video or documents and get back text, structured JSON, images, audio or tool calls. It also gives you built-in tools like Google Search grounding, code execution and file search, plus things like batch jobs, embeddings and real-time voice through the Live API.

## 2: What is the difference between the Gemini app and the Gemini API?

The Gemini app (gemini.google.com and the mobile apps) is a finished chat product for end users. The Gemini API is for developers: you call the models from your own backend, control the prompts, tools and output format, and pay per token. Features in the app don't always map one to one to the API, and the other way around.

## 3: What is Google AI Studio?

Google AI Studio (aistudio.google.com) is the web tool for working with the Gemini API. You use it to create API keys, try prompts against different models, check usage, rate limits and billing, look at request logs and copy working code with the "Get code" button. Since 2026 the Gemini API docs also live there under aistudio.google.com/docs.

## 4: What is the difference between the Gemini API and Gemini on Vertex AI?

Both give you the same Gemini models, but they are different products. The Gemini API (sometimes called the Gemini Developer API) uses API keys and is managed in Google AI Studio, so it's the quickest way to start. Vertex AI is Google Cloud's enterprise platform: it uses Google Cloud IAM, has regional endpoints and data residency options, VPC Service Controls and other enterprise controls. The Google GenAI SDK can talk to both, so switching mostly means changing how you create the client.

## 5: How do you get a Gemini API key?

Sign in to Google AI Studio and create a key on the API keys page. Each key belongs to a Google Cloud project, and that project is what quotas and billing are tied to. Since May 2026, new keys created in AI Studio are "auth keys" that are bound to a service account.

## 6: Which environment variables do the SDKs read the API key from?

The SDKs read `GEMINI_API_KEY` or `GOOGLE_API_KEY` automatically. If both are set, `GOOGLE_API_KEY` wins. Using an environment variable is better than putting the key in code, because it keeps the key out of source control.

```bash
export GEMINI_API_KEY="your-key-here"
```

## 7: What are the official SDKs for the Gemini API?

Google ships the Google GenAI SDK in several languages:

- Python: `google-genai`
- JavaScript/TypeScript: `@google/genai`
- Go: `google.golang.org/genai`
- Java: `com.google.genai:google-genai`
- C#/.NET: `Google.GenAI`

The same SDK works with both the Gemini API and Vertex AI.

## 8: How do you install the Python SDK?

```bash
pip install google-genai
```

Then you import it with `from google import genai`. Note that the package name is `google-genai`, not the old `google-generativeai`. For the Interactions API you need version 2.3.0 or newer.

## 9: How do you install the JavaScript SDK?

```bash
npm install @google/genai
```

It works in Node.js and other server-side JavaScript runtimes. For the Interactions API you need version 2.3.0 or newer.

## 10: What happened to the old google-generativeai and @google/generativeai libraries?

They are legacy. They were deprecated on November 30, 2025 and are no longer actively maintained. New code should use `google-genai` (Python), `@google/genai` (JavaScript) or `google.golang.org/genai` (Go). For mobile apps, Google points you to Firebase AI Logic instead of the old Swift, Android and Dart SDKs. You'll still see the old packages in older tutorials and projects, so it helps to recognize them.

## 11: How do you create a client in Python?

```python
from google import genai

# Reads GEMINI_API_KEY or GOOGLE_API_KEY from the environment
client = genai.Client()

# Or pass the key directly
client = genai.Client(api_key="your-key")
```

The client is the entry point for everything: `client.interactions`, `client.models`, `client.files`, `client.batches`, `client.caches` and so on.

## 12: How do you create a client in JavaScript?

```javascript
import { GoogleGenAI } from "@google/genai";

// Reads GEMINI_API_KEY from the environment
const ai = new GoogleGenAI({});

// Or pass the key directly
const ai2 = new GoogleGenAI({ apiKey: process.env.MY_KEY });
```

## 13: How do you send your first request with the Interactions API?

```python
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain what an API is in two sentences.",
)

print(interaction.output_text)
```

`interactions.create` sends one turn to the model and returns an `Interaction` object. `output_text` is a shortcut that gives you the final text.

## 14: What is the Interactions API?

The Interactions API is the newer main API for Gemini. It became generally available in June 2026 and is the recommended choice for new projects. Each call creates an `Interaction`, which holds the steps the model went through: thoughts, tool calls, tool results and the final output. It can store conversation state on the server, run long tasks in the background, and works with both models and agents (like Deep Research) through one endpoint.

## 15: What is the generateContent API?

`generateContent` is the original Gemini API endpoint. You send a list of `contents` (the conversation so far) and get back `candidates` with the model's answer. Google now calls it legacy, but it's still fully supported and a lot of existing code uses it. Some features, like explicit context caching and the Batch API, still only work with `generateContent`.

## 16: Should you use the Interactions API or generateContent for a new project?

Use the Interactions API for new projects. Google says new models and features beyond the core model family will launch there first, it gives you server-side history and background execution, and it's the only way to call agents. Stick with `generateContent` if you need something that the Interactions API doesn't support yet, like explicit caching or batch jobs, or if you're maintaining existing code that works fine.

## 17: How do you make a basic generateContent call in Python?

```python
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Tell me a joke.",
)

print(response.text)
```

`response.text` joins the text parts of the first candidate into one string.

## 18: How do you make a basic generateContent call in JavaScript?

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: "Tell me a joke.",
});

console.log(response.text);
```

In JavaScript, `text` is a getter on the response, not a method.

## 19: How do you call generateContent with curl?

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{ "parts": [{ "text": "Tell me a joke." }] }]
  }'
```

The model goes in the URL, the key goes in the `x-goog-api-key` header, and the body holds `contents`, each with a list of `parts`.

## 20: How do you call the Interactions API with curl?

```bash
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a joke."
  }'
```

Unlike `generateContent`, the model is in the body, and there's a single `interactions` endpoint for every model and agent.

## 21: What are the v1 and v1beta API versions?

The REST API has versioned paths. `v1beta` gets new features first and is what most docs and examples use, including the Interactions API. `v1` is the stable version with a smaller set of features. In the SDK you can choose the version with `http_options`, but the default is fine for most projects.

## 22: What is a model ID?

It's the string you pass as `model`, like `gemini-3.8-flash` or `gemini-4-argon`. The ID tells the API which model, generation and variant to use. Some IDs are fixed versions, some are previews (they end in `-preview`), and some are aliases like `gemini-flash-latest` that Google moves to newer models over time.

## 23: What are the main Gemini models available today?

As of November 2026 the main text models are:

- `gemini-4-argon`: the flagship reasoning model, 1M token context.
- `gemini-3.8-flash`: the most capable Flash model, good default for most apps.
- `gemini-3.6-flash`: the previous Flash generation.
- `gemini-3.5-flash-lite` and `gemini-3.1-flash-lite`: the cheapest and fastest options.
- `gemini-3.1-pro-preview`: a Pro model in preview.

There are also separate models for live voice, text-to-speech, image generation (Nano Banana), video (Gemini Omni), transcription and embeddings.

## 24: What is the difference between Pro, Flash and Flash-Lite models?

They trade quality against speed and price. Pro and flagship models (like Gemini 4 Argon) are the strongest at hard reasoning, coding and long tasks, but they're slower and cost more. Flash models are the balanced default and handle most production work well. Flash-Lite models are the fastest and cheapest, which makes them good for high-volume simple tasks like classification, extraction or routing.

## 25: What do stable, preview and deprecated mean for Gemini models?

Stable (GA) models are meant for production and get advance notice before they're shut down. Preview models (`-preview` in the ID) let you try new things, but they have stricter rate limits and can change or be shut down on short notice. Deprecated models still work for a while but you should move off them. Google publishes the shutdown dates and sometimes routes requests for an old model to a newer one.

## 26: What are model aliases like gemini-flash-latest?

Aliases are IDs that point to whatever model Google currently picks for that slot. For example, `gemini-flash-latest` has pointed to different Flash models over time. They're handy for quick tests and side projects, but the behavior behind the alias can change without your code changing. For production, use a specific model ID.

## 27: Why should you pin a specific model ID in production?

Because a new model can behave differently even if it's "better": the answer style, JSON output, tool calling and latency can all change. If you pin the ID, you decide when to upgrade and you can test the new model first. Keep in mind that Google can still route a deprecated ID to a newer model after its retirement date, so watch the changelog.

## 28: What is a token?

A token is the unit the model reads and writes. For Gemini, one token is about 4 characters of English text, and 100 tokens is about 60-80 words. Images, audio and video are also turned into tokens. Pricing, rate limits and context windows are all measured in tokens.

## 29: What is a context window?

It's the maximum number of tokens the model can handle in one request. Current Gemini models have about 1 million input tokens (1,048,576). Everything counts toward it: system instructions, conversation history, files, tool results and, depending on the model, the output too.

## 30: How do input and output limits differ between Gemini 4 and Gemini 3?

Gemini 3 and 2.5 models have separate budgets: about 1M tokens of input and 65,536 tokens of output. Gemini 4 Argon has one shared 1M token window for input, thinking and output. By default it caps synchronous output at 65,536 tokens, and if your input plus `max_output_tokens` is bigger than the window, the output gets cut to the space that's left.

## 31: How do you count tokens before sending a request?

Use `count_tokens`. It returns the number of input tokens only, not the output.

```python
from google import genai

client = genai.Client()

result = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents="The quick brown fox jumps over the lazy dog.",
)
print(result.total_tokens)
```

This is useful to check that a big document fits in the context window or to estimate cost.

## 32: What is a prompt?

The prompt is everything you send to the model to get an answer: your instructions, the user's question, examples, documents, images and so on. With the Interactions API it goes in `input`, and with `generateContent` it goes in `contents`. A clear, specific prompt usually matters more for quality than any setting.

## 33: What are system instructions?

System instructions tell the model how to behave for the whole request: its role, tone, rules and output format. They're kept separate from the user's message, which makes them easier to manage.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    system_instruction="You are a support agent for an online shoe store. Answer briefly.",
    input="Can I return shoes I already wore?",
)
```

## 34: How do you set system instructions with generateContent?

Put them in the config object:

```python
from google.genai import types

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Can I return shoes I already wore?",
    config=types.GenerateContentConfig(
        system_instruction="You are a support agent for an online shoe store.",
    ),
)
```

In JavaScript the field is `systemInstruction` inside `config`.

## 35: What is output_text on an Interaction?

`output_text` is a shortcut that joins the text blocks at the end of the model's output. It's enough for simple text answers. If the response mixes text with images, or you need thoughts and tool calls, read `interaction.steps` instead.

## 36: What are steps in the Interactions API?

Steps are the ordered list of things that happened during an interaction. Common step types are `thought` (reasoning summary and signature), `function_call`, `function_result`, built-in tool steps like `google_search_call` and `code_execution_result`, and `model_output` (the final answer). The `create` response only returns the steps the model produced, while `interactions.get` also includes `user_input` steps.

## 37: What does response.text return in generateContent?

It joins the text parts of the first candidate. If the response has no text (for example, it was blocked or only has a function call), it can be empty or `None`, so check `candidates`, `function_calls` or `prompt_feedback` when that happens.

## 38: What are contents, parts and roles in generateContent?

`contents` is a list of messages. Each message has a `role` and a list of `parts`. A part can be text, inline data (like an image in base64), a file reference, a function call or a function response.

```python
contents = [
    {"role": "user", "parts": [{"text": "Hi, I'm Ana."}]},
    {"role": "model", "parts": [{"text": "Hi Ana! How can I help?"}]},
    {"role": "user", "parts": [{"text": "What is my name?"}]},
]
```

## 39: What roles exist in generateContent contents?

There are two: `user` for your input (including function responses) and `model` for the model's replies (including function calls). There is no `system` role in `contents`; system instructions go in their own field.

## 40: What does max_output_tokens do?

It sets the maximum number of tokens the model can generate. If the model hits it, the output gets cut off. On thinking models the limit includes thought tokens, so a small value can end the response while the model is still thinking and give you an empty or partial answer.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Summarize the history of Rome.",
    generation_config={"max_output_tokens": 500},
)
```

## 41: What happened to temperature, top_p and top_k?

They were deprecated in July 2026. Gemini 4 and Gemini 3.6+ models ignore custom values for them and send back deprecation warning headers, so you should remove them from requests. Older models still accept them, which is why you'll see them in older code. To change how the model answers today, you use the prompt, `thinking_level`, structured output and tools.

## 42: What is thinking in Gemini models?

Thinking means the model reasons internally before it gives the final answer. It improves results on harder tasks like math, coding, planning and multi-step questions. Thinking is on by default for current models, it adds latency, and thought tokens are billed like output tokens.

## 43: What values can thinking_level have?

Depending on the model, `thinking_level` can be `minimal`, `low`, `medium` or `high`. For example, Gemini 3.8 Flash and Gemini 4 Argon support `low`, `medium` and `high` and default to `medium`. Gemini 3.5 Flash-Lite supports all four and defaults to `minimal`.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Plan a 3-day trip to Lisbon.",
    generation_config={"thinking_level": "low"},
)
```

## 44: Why does the default thinking level differ between models?

Each model is tuned for a different job. Cheap, fast models like Flash-Lite default to `minimal` because they're used for high-volume simple tasks where latency matters. Stronger models default to `medium` or `high` because people use them for harder problems. Always check the defaults for the model you use, since they affect both cost and latency.

## 45: Can you turn thinking off completely?

On most current models you can't fully turn it off, but you can lower it to `minimal` or `low` where the model supports it. On Gemini 2.5 models the old `thinking_budget` setting could be set to `0` to disable thinking on Flash models, but not on 2.5 Pro.

## 46: What are thinking summaries?

By default you only get the final answer. If you set `thinking_summaries` to `"auto"`, the response includes `thought` steps with a short summary of the model's reasoning. It's useful for debugging and for showing progress in a UI. You still pay for the full thinking, not just the summary.

```python
generation_config={"thinking_summaries": "auto"}
```

## 47: How are thought tokens billed?

Thought tokens are billed at the output token price, even though you only see a summary or nothing. In the Interactions API you can see them in `usage.total_thought_tokens`. In `generateContent` they're in `usage_metadata.thoughts_token_count`.

## 48: Why would you use streaming?

Streaming sends the response in pieces as the model generates it, so the user sees text right away instead of waiting for the full answer. The total time is about the same, but the app feels much faster. It's the normal choice for chat UIs.

## 49: How do you stream with the Interactions API?

Pass `stream=True` and loop over the events. Text arrives in `step.delta` events.

```python
stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how DNS works.",
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta" and event.delta.type == "text":
        print(event.delta.text, end="")
```

## 50: How do you stream with generateContent in Python?

Use `generate_content_stream`:

```python
for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents="Explain how DNS works.",
):
    print(chunk.text, end="")
```

Each chunk is a partial `GenerateContentResponse`. Under the hood this calls the `streamGenerateContent` endpoint with server-sent events.

## 51: How do you stream with generateContent in JavaScript?

```javascript
const stream = await ai.models.generateContentStream({
  model: "gemini-3.8-flash",
  contents: "Explain how DNS works.",
});

for await (const chunk of stream) {
  process.stdout.write(chunk.text ?? "");
}
```

## 52: Does the model remember previous messages on its own?

No. Each request is separate, and the model only knows what's in that request. To have a conversation you either send the whole history every time (stateless) or, with the Interactions API, point to the previous turn with `previous_interaction_id` so the server loads the history for you.

## 53: What is previous_interaction_id?

It's how you chain turns in the Interactions API. Interactions are stored on the server by default, so you pass the ID of the last one and the server adds that history to your new request.

```python
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs.",
)

turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="How many paws are in my house?",
    previous_interaction_id=turn1.id,
)
print(turn2.output_text)
```

## 54: How do you build a chat with generateContent?

The SDK has a chat helper that keeps the history on the client side and sends it each time:

```python
chat = client.chats.create(model="gemini-3.8-flash")

print(chat.send_message("I have 2 dogs.").text)
print(chat.send_message("How many paws are in my house?").text)
```

There's also `send_message_stream` for streaming. The full history is still sent with every request, so long chats get more expensive per turn.

## 55: What is the difference between stateful and stateless mode?

In stateful mode the server stores the conversation and you only send the new input plus `previous_interaction_id`. In stateless mode you keep the history yourself and send all of it every time, usually with `store=False`. Stateful is simpler, while stateless gives you full control and keeps nothing on Google's side beyond what's needed to serve the request.

## 56: What does the store parameter do?

`store` decides whether an interaction is saved on the server. It's `true` by default, which is what makes `previous_interaction_id`, background mode and request logs work. Setting `store=False` turns that off, so you can't chain from that interaction and can't run it in the background.

## 57: How long are stored interactions kept?

On the paid tier interactions are kept for 55 days, and on the free tier for 1 day. Paid projects can set shorter log retention in AI Studio (7, 14, 28 or 55 days). You can delete a stored interaction at any time with its ID.

## 58: What kinds of input can Gemini models understand?

Text, images, audio, video and documents like PDFs. Office and OpenDocument files are also supported in recent versions. You can mix several types in one request, for example a PDF, two images and a text question.

## 59: How do you send an image with the Interactions API?

Pass `input` as a list of content blocks. You can use base64 data or a file URI.

```python
import base64

with open("receipt.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "What is the total on this receipt?"},
        {"type": "image", "data": image_b64, "mime_type": "image/jpeg"},
    ],
)
print(interaction.output_text)
```

## 60: How do you send an image with generateContent?

Use `types.Part.from_bytes` for raw bytes:

```python
from google.genai import types

with open("receipt.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "What is the total on this receipt?",
    ],
)
print(response.text)
```

## 61: What is the Files API?

The Files API lets you upload media once and then refer to it by URI in requests, instead of sending the bytes inline every time. It's free to use. You need it for big files, and it's handy when you ask several questions about the same file.

```python
myfile = client.files.upload(file="lecture.mp3")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[myfile, "Summarize this lecture."],
)
```

## 62: What are the limits of the Files API?

Each file can be up to 2 GB, and a project can store up to 20 GB. Files are deleted automatically after 48 hours. You can read a file's metadata during that time but you can't download files you uploaded yourself. You can download files the model generated, like videos.

## 63: When do you need the Files API instead of inline data?

When the whole request (files, prompt, system instructions and so on) is bigger than 100 MB, or bigger than 50 MB for PDFs. It's also a good idea when you'll reuse a file across several requests, because you upload it once.

## 64: Can Gemini read PDFs?

Yes. Gemini reads PDFs natively, including the text, tables, charts and images in them, not just extracted text. You can send a PDF inline or through the Files API, then ask questions, summarize it or extract data into JSON.

## 65: What can you do with audio input?

You can transcribe it, summarize it, answer questions about it, detect who is speaking, or analyze tone. Audio is counted at a fixed rate of tokens per second. For dedicated speech-to-text there's also the `gemini-3.5-transcribe` model with speaker diarization and word timestamps.

## 66: What can you do with video input?

You can summarize a video, answer questions about what happens, find timestamps for events, or extract text shown on screen. Video is turned into tokens per frame plus audio, so long videos use a lot of tokens. Newer Flash models also support "agentic" video understanding, which looks at only the parts it needs and uses far fewer tokens on long content.

## 67: Can you pass files from Cloud Storage or a URL?

Yes. Since January 2026 the API accepts Google Cloud Storage buckets and pre-signed URLs as data sources, so you don't always have to upload to the Files API first. The max file size for this was raised from 20 MB to 100 MB at the same time.

## 68: What is structured output?

Structured output makes the model return JSON that matches a JSON Schema you give it. This is much more reliable than asking for JSON in the prompt and hoping. It's used for data extraction, classification and anything where your code needs to parse the result.

## 69: How do you get JSON output with the Interactions API?

Use `response_format` with a JSON mime type and a schema:

```python
from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    ingredients: list[str]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a simple pancake recipe.",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema(),
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
```

## 70: How do you get JSON output with generateContent?

Set `response_mime_type` and `response_schema` in the config. The Python SDK accepts a Pydantic class directly and fills `response.parsed`:

```python
from pydantic import BaseModel
from google.genai import types

class Recipe(BaseModel):
    name: str
    ingredients: list[str]

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Give me a simple pancake recipe.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Recipe,
    ),
)

recipe: Recipe = response.parsed
```

You can also pass a plain JSON Schema with `response_json_schema`.

## 71: How do you use Pydantic with structured output?

Define a Pydantic model, pass `Model.model_json_schema()` as the schema, then parse the result with `Model.model_validate_json(...)`. This gives you one source of truth for the shape, type hints in your code, and validation of the returned data.

## 72: How do you use Zod with structured output in JavaScript?

Write the JSON Schema for the request, and use Zod to parse and validate the response.

```javascript
import { z } from "zod";

const recipeJsonSchema = {
  type: "object",
  properties: {
    name: { type: "string" },
    ingredients: { type: "array", items: { type: "string" } },
  },
  required: ["name", "ingredients"],
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Give me a simple pancake recipe.",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema,
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
```

You can also go the other way and turn a Zod schema into JSON Schema with `z.toJSONSchema()`.

## 73: How do you make the model pick from a fixed list of labels?

Use an `enum` in the schema. The model can then only return one of the allowed values, which is perfect for classification.

```python
response_format={
    "type": "text",
    "mime_type": "application/json",
    "schema": {
        "type": "object",
        "properties": {
            "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]}
        },
        "required": ["sentiment"],
    },
}
```

## 74: What is function calling?

Function calling lets the model ask your code to run a function. You describe the functions (name, description, parameters as JSON Schema). When the model decides it needs one, it returns a `function_call` with arguments. Your code runs the function and sends the result back, and the model uses that result to write its answer. It's how you connect Gemini to your APIs and databases.

## 75: How do you declare a function for the model?

In the Interactions API, add an entry with `"type": "function"` to `tools`:

```python
get_weather = {
    "type": "function",
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "City name, e.g. Paris"}
        },
        "required": ["city"],
    },
}

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Paris?",
    tools=[get_weather],
)
```

## 76: Does Gemini run your functions for you?

No. The model only returns the function name and arguments. Your code has to run the function and send back the result. The only exception is the Python SDK's automatic function calling with `generateContent`, where the SDK calls your Python functions for you, but even then it's your process running the code, not Google.

## 77: What are built-in tools?

Built-in tools are tools that Google runs for you on the server side in the same API call. They include Google Search, Google Maps, URL Context, Code Execution and File Search. Computer Use is also built in, but your app runs the actions. You turn them on with entries like `{"type": "google_search"}` in `tools`.

## 78: What is Grounding with Google Search?

It lets the model search Google and base its answer on current web results. This helps with recent events and facts the model doesn't know, and reduces made-up answers. The response includes the search queries it ran and citations that link parts of the text to sources.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the most recent Champions League final?",
    tools=[{"type": "google_search"}],
)
```

## 79: What is the URL Context tool?

It lets the model fetch and read specific URLs that you put in the prompt, like a docs page or a PDF link. You can pass up to 20 URLs per request. It only works with public pages, not paywalled content, localhost or Google Docs.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Compare the pricing on https://example.com/a and https://example.com/b",
    tools=[{"type": "url_context"}],
)
```

## 80: What is the Code Execution tool?

It lets the model write Python code and run it in a sandbox on Google's side, then use the output in its answer. It's useful for math, data analysis and making charts with matplotlib. Only Python is supported, runs have a 30-second limit, and you can't install extra packages.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers?",
    tools=[{"type": "code_execution"}],
)
```

## 81: What is Grounding with Google Maps?

It lets the model use Google Maps data to answer location questions, like finding places, getting directions or adding local details. It's useful for travel, delivery or local search features. Since March 2026 it also works with Gemini 3 models.

## 82: What is the File Search tool?

File Search is a managed RAG (retrieval-augmented generation) tool. You upload your documents into a "file search store", Google chunks and embeds them, and at question time the model retrieves the relevant chunks and answers with citations. You don't need to run your own vector database.

## 83: What is Computer Use?

Computer Use lets the model look at screenshots of a browser, mobile or desktop screen and decide what to do next: click, type, scroll and so on. Your app runs those actions (for example with Playwright) and sends back a new screenshot. It reached general availability in October 2026.

## 84: What does grounding mean?

Grounding means tying the model's answer to real sources of information, like search results, your documents or a map, instead of only its training data. A grounded answer is more likely to be correct and up to date, and it can include citations so users can check it.

## 85: How do citations show up in responses?

In the Interactions API, text blocks in `model_output` steps can have `annotations`. A `url_citation` has the `url`, `title` and `start_index`/`end_index` of the text it supports. File Search returns `file_citation` annotations with things like the file name and page number. In `generateContent`, the same info comes in `grounding_metadata`.

## 86: What are embeddings?

Embeddings are lists of numbers (vectors) that represent the meaning of some content. Things with similar meaning get vectors that are close together. You use them for semantic search, RAG, recommendations, clustering and finding duplicates.

## 87: How do you create an embedding?

```python
result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
)

vector = result.embeddings[0].values
print(len(vector))  # 3072 by default
```

## 88: Which embedding models are available?

- `gemini-embedding-2`: multimodal, handles text, images, video, audio and PDFs in one shared vector space, up to 8,192 input tokens.
- `gemini-embedding-001`: text only, up to 2,048 input tokens.

Both output 3072 dimensions by default. The older `text-embedding-004` was shut down in January 2026.

## 89: What does output_dimensionality do?

It makes the embedding smaller. Gemini embeddings are trained so that the first N numbers still carry most of the meaning (Matryoshka representation learning). Smaller vectors use less storage and are faster to compare, with a small drop in quality. Google recommends 768, 1536 or 3072.

```python
from google.genai import types

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="Hello world",
    config=types.EmbedContentConfig(output_dimensionality=768),
)
```

## 90: How do you tell the embedding model what the embedding is for?

For `gemini-embedding-001`, set `task_type`, for example `RETRIEVAL_QUERY`, `RETRIEVAL_DOCUMENT`, `SEMANTIC_SIMILARITY` or `CLASSIFICATION`. `gemini-embedding-2` doesn't support `task_type`; instead you add a prefix to the text, like `task: search result | query: {question}` for queries and `title: {title} | text: {content}` for documents.

## 91: What is Nano Banana?

Nano Banana is the name Google uses for Gemini's image generation and editing models. Current ones include `gemini-nano-banana-2.1`, `gemini-3.1-flash-image` (Nano Banana 2), `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) and `gemini-3-pro-image` (Nano Banana Pro). They can create images from text, edit existing images, and keep a character or product looking the same across edits.

## 92: How do you generate an image?

```python
import base64

interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input="A watercolor painting of a lighthouse at sunset",
    response_format={"type": "image", "aspect_ratio": "16:9", "image_size": "2K"},
)

with open("lighthouse.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

`image_size` can be `1K`, `2K` or `4K` (uppercase K, lowercase is rejected).

## 93: What is SynthID?

SynthID is Google's invisible watermark. Every image generated by the Gemini API includes it, so the image can later be identified as AI-generated. You can't turn it off.

## 94: Can the Gemini API generate speech?

Yes, with text-to-speech models like `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts`. You can pick from prebuilt voices, control style and pacing with natural language ("say this cheerfully"), and create multi-speaker audio like a podcast dialog. Newer TTS models also support voice design and voice replication.

## 95: Is there a model just for transcription?

Yes. `gemini-3.5-transcribe` is a speech-to-text model with low latency, language detection, speaker diarization and word timestamps. There's also `gemini-3.5-transcribe-live` for streaming transcription. You can still transcribe with general models like Flash, but the dedicated model is built for it.

## 96: Can the Gemini API generate video?

Yes, with the Gemini Omni models like `gemini-omni-1.2-flash`. They generate and edit short videos (up to 15 seconds) with native audio, and support things like extending a video or interpolating between a first and last frame. The older Veo models are being shut down in favor of Omni.

## 97: Can the Gemini API generate music?

Yes, with the Lyria models. Lyria 3 launched in March 2026 with a clip model for 30-second clips and a pro model for full songs, and Lyria 3.5 reached general availability in September 2026.

## 98: What is the Live API?

The Live API is for real-time, two-way conversations with low latency, mostly voice. It uses a WebSocket connection: you stream audio (and optionally video frames) in and get audio back as the model speaks. It supports interruptions (barge-in), voice activity detection, transcription and tool use. The current default model is `gemini-3.8-live`.

## 99: What audio formats does the Live API use?

Input audio is raw 16-bit PCM at 16 kHz, little-endian. Output audio is raw 16-bit PCM at 24 kHz, little-endian. You can also send JPEG images at up to 1 frame per second and text.

## 100: What are ephemeral tokens?

Ephemeral tokens are short-lived credentials your backend creates so a browser or mobile app can connect directly to the Live API without seeing your real API key. They expire quickly (30 minutes by default) and can be locked to a specific model and config. They only work with the Live API.

## 101: What are safety settings?

Safety settings let you adjust how strictly the API filters content in certain harm categories. You set a threshold per category, for example to block more or less. They only control the adjustable filters; some protections, like those for child safety, always apply and can't be turned off.

## 102: What harm categories can you configure?

In the Interactions API the categories are `harassment`, `hate_speech`, `sexually_explicit`, `dangerous_content` and `jailbreak` (prompts that try to get around safety filters). In `generateContent` they're enum values like `HARM_CATEGORY_HARASSMENT` and `HARM_CATEGORY_HATE_SPEECH`.

## 103: What block thresholds are there?

- `off`: the filter is off.
- `block_only_high`: block only content with a high chance of being unsafe.
- `block_medium_and_above`: block medium and high.
- `block_low_and_above`: block low, medium and high.

The filters look at the probability that content is unsafe, not how severe it is. For Gemini 2.5 and newer, the adjustable filters are off by default.

## 104: What happens when a request is blocked by safety filters in the Interactions API?

The request fails with an HTTP 400 error and you don't get the blocked content. The error `code` tells you why, for example `safety`, `jailbreak`, `prohibited_content` or `blocklist`. For background interactions the `status` becomes `failed` with the error in `errors`, and in streaming you get an `error` event.

## 105: What are rate limits?

Rate limits cap how much you can use the API in a time window, so one project can't overload the service. If you go over a limit you get a 429 error. Limits depend on the model and your usage tier, and you can see yours in AI Studio.

## 106: What are RPM, TPM and RPD?

- RPM: requests per minute.
- TPM: input tokens per minute.
- RPD: requests per day.

Each is checked on its own, so you can hit the RPM limit even if you're far below TPM. Some models have other limits too, like images per minute. RPD resets at midnight Pacific time.

## 107: Are rate limits per API key or per project?

Per project. All API keys in the same Google Cloud project share the same limits, so making more keys doesn't give you more quota.

## 108: What are usage tiers?

Tiers decide your rate limits and how much you can spend:

- Free: no billing account needed, low limits.
- Tier 1: linked billing account.
- Tier 2: at least $100 paid and 3 days since the first payment.
- Tier 3: at least $1,000 paid and 30 days since the first payment.

You move up automatically when you meet the conditions, usually within minutes.

## 109: What's the difference between the free tier and the paid tier besides limits?

Besides lower rate limits, free tier projects have shorter interaction retention (1 day vs 55 days), and some models and features are paid only. Google's terms also treat data differently: on the free tier your prompts and responses may be used to improve Google's products, while paid tier data isn't. Don't send private or customer data on the free tier.

## 110: What does a 429 error mean?

`429 RESOURCE_EXHAUSTED` means you hit a rate limit or a spend limit. The fix is to wait and retry with exponential backoff, send fewer or smaller requests, move to a higher tier, or ask for a quota increase. A burst of 429s in production usually means you need a queue or rate limiter in front of the API.

## 111: How is Gemini API usage priced?

Mostly per token, with separate prices for input and output tokens per million. Thinking tokens are billed as output. Prices differ by model, and some models charge more for very long prompts. Extra things have their own prices: search grounding queries, cache storage, image and video generation, and so on. Batch and Flex requests cost 50% less, and Priority costs more.

## 112: What is the Batch API?

The Batch API runs a large number of requests asynchronously. You submit them as one job, and results come back later, usually much faster than the 24-hour target. It's for work that doesn't need an instant answer, like processing a backlog of documents or running evaluations.

## 113: How much does the Batch API save?

Batch requests cost 50% of the standard price. Batch also has its own rate limits, separate from normal requests, so it doesn't eat into your interactive quota.

## 114: What is context caching?

Context caching saves the processed version of a large, repeated part of your prompt (like a long document or system instruction) so later requests that start with the same content are cheaper. Cached tokens are billed at a much lower rate than normal input tokens. There are two kinds: implicit and explicit.

## 115: What is implicit caching?

Implicit caching is automatic and on by default for Gemini 2.5 and newer models. If a new request starts with the same content as a recent one, you get the discount on the matching part without doing anything. For Gemini 3 and 4 models the shared part needs to be at least 4,096 tokens. You can check hits in `usage.total_cached_tokens`.

## 116: What is explicit caching?

With explicit caching you create a cache object yourself with the content you want to reuse, set how long it lives (TTL), and point your requests to it. You get a guaranteed discount on those tokens but you also pay for storage over time. It's only available through `generateContent`, not the Interactions API, and not for Gemini 4 Argon.

## 117: What is Flex inference?

Flex is a cheaper processing tier: 50% off the standard price, but with much higher latency (the target is 1 to 15 minutes) and no guarantee. Flex requests can be dropped when traffic is high. Unlike Batch, it's still a normal synchronous call. You choose it with `service_tier="flex"`.

## 118: What is Priority inference?

Priority is the opposite of Flex: you pay 75-100% more than standard, and in return your requests get high reliability and low latency and aren't dropped under load. It's for critical, user-facing traffic where slowdowns cost you more than the extra price.

## 119: How do you choose a service tier for a request?

Set `service_tier` on the request. Leaving it out means standard.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Classify this support ticket: ...",
    service_tier="flex",
)
```

## 120: Can you use the OpenAI SDK with Gemini?

Yes. Gemini has an OpenAI-compatible endpoint, so you can keep using the OpenAI library and change three things: the API key, the base URL and the model name.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

Google still recommends the native SDK if you're not already on the OpenAI library.

## 121: How do you control thinking through the OpenAI-compatible endpoint?

Pass `reasoning_effort` with `minimal`, `low`, `medium` or `high`. It maps to Gemini's `thinking_level` (or a `thinking_budget` for 2.5 models). Don't set `reasoning_effort` and Gemini's own thinking config at the same time, because they control the same thing.

## 122: What is the Gemini API CLI?

It's a command-line tool called `gemini-api` that launched in beta in October 2026 for working with the Gemini API from your terminal. It's still experimental, so check its repo for the current commands. Don't mix it up with Gemini CLI, which is a separate coding agent for the terminal.

## 123: What developer helpers does Google provide for working with the Gemini API in coding agents?

Google has a Gemini Docs MCP server and a set of Gemini API "agent skills" on GitHub. You plug them into your coding assistant so it can read the current docs and follow current API patterns, instead of writing code based on old training data. This matters a lot for an API that changes as fast as this one.

## 124: What are Managed Agents?

Managed Agents are agents that Google runs for you. You send one request to the Interactions API with an `agent` instead of a `model`, and the service provisions a Linux sandbox, runs the whole agent loop (thinking, tool calls, running code, writing files) and returns the result. The general-purpose one is the Antigravity agent, for example `antigravity-preview-09-2026`.

## 125: What is the Deep Research agent?

Deep Research is an agent that does multi-step research: it plans, searches, reads many sources and writes a detailed report with citations. There's a fast version (`deep-research-preview-04-2026`) and a more thorough one (`deep-research-max-preview-04-2026`). Since it can run for a long time, you usually call it in background mode.

## 126: What's the difference between passing model and agent in the Interactions API?

`model` calls a Gemini model directly: one turn of generation, with whatever tools you give it. `agent` calls a predefined agent, like Deep Research or Antigravity, which runs its own multi-step loop with its own tools. Both return an `Interaction`, and you can mix them in one conversation using `previous_interaction_id`.

## 127: What is background mode?

Setting `background=True` makes `interactions.create` return right away while the work runs on the server. You then check the result later with `interactions.get`, or get notified with a webhook. It's for long tasks like agents or heavy reasoning that could time out a normal HTTP call. It needs storage on, so it doesn't work with `store=False`.

## 128: What are webhooks in the Gemini API?

Webhooks let Google call your server when an async job finishes, so you don't have to keep polling. They cover batch jobs, background interactions and video generation, with events like `batch.succeeded`, `interaction.completed` and `video.generated`. They launched in May 2026 and are still in preview.

## 129: What status values can an interaction have?

Common ones are `completed` (finished normally), `requires_action` (the model wants you to run a function and send the result), `incomplete` (stopped early, for example after hitting `max_output_tokens`), `failed` and `cancelled`. Background interactions also go through an in-progress state while they run. Always check the status before trusting `output_text`.

## 130: What finish reasons can a generateContent candidate have?

`finish_reason` tells you why the model stopped. The common ones are:

- `STOP`: finished normally.
- `MAX_TOKENS`: hit the output limit.
- `SAFETY`: stopped by a safety filter.
- `RECITATION`: stopped because the output was too close to existing content.
- `MALFORMED_FUNCTION_CALL`: the model produced an invalid function call.

There are a few more, like `BLOCKLIST`, `PROHIBITED_CONTENT` and `OTHER`.

## 131: What usage fields does an Interaction return?

The `usage` object has `total_input_tokens`, `total_output_tokens`, `total_thought_tokens`, `total_cached_tokens`, `total_tool_use_tokens` and `total_tokens`. When streaming you get it in the final `interaction.completed` event. Log these for every request so you can track cost.

## 132: What usage fields does generateContent return?

`response.usage_metadata` has fields like `prompt_token_count`, `candidates_token_count`, `thoughts_token_count`, `cached_content_token_count` and `total_token_count`. Cost is roughly prompt tokens times the input price (minus the cache discount) plus candidates and thoughts tokens times the output price.

## 133: How do you catch API errors in the Python SDK?

The SDK raises `errors.APIError` (with subclasses `ClientError` for 4xx and `ServerError` for 5xx). The error has a `code` and a `message`.

```python
from google import genai
from google.genai import errors

client = genai.Client()

try:
    interaction = client.interactions.create(model="gemini-3.8-flash", input="Hi")
except errors.APIError as e:
    print(e.code, e.message)
```

## 134: What do the common HTTP error codes from the Gemini API mean?

- 400: bad request (wrong parameter, invalid schema, blocked by safety).
- 403: permission problem, often a bad or restricted API key.
- 404: wrong model name or resource not found.
- 429: rate limit or spend limit hit.
- 500: internal error on Google's side.
- 503: the service is overloaded or at capacity.

400, 403 and 404 mean you need to fix the request. 429, 500 and 503 are usually worth retrying with backoff.

## 135: How should you retry failed requests?

Retry only errors that can succeed later (429, 500, 503, timeouts). Use exponential backoff with some random jitter, for example 1s, 2s, 4s, 8s, and set a maximum number of attempts. Don't retry 400 errors, since sending the same bad request again just fails again.

## 136: Why shouldn't you call the Gemini API directly from a browser with your API key?

Anyone can open the browser's dev tools and copy the key, then use your quota and run up your bill. Send requests through your own backend, which holds the key and can also add auth, rate limits and logging. For real-time voice in the browser, use ephemeral tokens, and for mobile and web apps, Firebase AI Logic is another option.

## 137: What are auth keys and how are they different from standard keys?

Standard API keys link requests to a project for billing and quota but don't say who is calling. Auth keys are bound to a service account, so requests run as that account, they're limited to the Gemini API by default, and Google can block them fast if they leak. Since May 28, 2026 all new keys in AI Studio are auth keys, and unrestricted standard keys are rejected by the Gemini API.

## 138: How do you restrict an API key?

In the Google Cloud console you can limit a key to certain IP addresses, websites or apps, and limit which APIs it can call. In AI Studio there's a "Restrict to Gemini API only" option. Be careful: if you restrict a key to other APIs and not Gemini, your Gemini calls will break.

## 139: What is Gemma and how is it related to Gemini?

Gemma is Google's family of open-weight models, built from the same research as Gemini. You can download Gemma and run it on your own hardware, or call some Gemma models (like `gemma-4-31b-it`) through the Gemini API. Gemini models themselves are only available as a hosted service.

## 140: What makes a good prompt for Gemini?

Be clear and specific about the task, the audience and the output format. Give the model the context it needs, use examples when the format is tricky, and split complex tasks into steps. With long documents, put the question at the end. Test prompts on real inputs and adjust based on what goes wrong.

## 141: What is few-shot prompting?

Few-shot prompting means putting a few examples of input and the expected output in the prompt, so the model copies the pattern. It works well for formatting, tone and classification rules that are hard to describe in words. Use examples that cover different cases, and keep their format consistent.

## 142: Where should you put the question in a long-context prompt?

At the end, after the documents. Google's docs say this usually gives better results, especially when the context is long. It also helps with caching, since the large unchanging content stays at the start where it can be reused.

## 143: What is long context good for?

With about 1M tokens, you can send whole codebases, long contracts, books, hours of audio or long videos in one request. That often lets you skip building a RAG pipeline for small or medium document sets. It also makes "many-shot" prompting possible, where you give hundreds of examples instead of a few.

## 144: What is media_resolution?

It controls how many tokens are used for each image, video frame or PDF page. Higher resolution gives the model more detail but costs more tokens and adds latency. Values are `low`, `medium`, `high` and `ultra_high`, and on Gemini 3 and 4 models you can set it per item. Audio always uses a fixed rate.

## 145: How do you check a model's token limits from code?

Call `models.get` and read the limits:

```python
model = client.models.get(model="gemini-3.8-flash")
print(model.input_token_limit, model.output_token_limit)
```

## 146: How do you list the available models?

```python
for model in client.models.list():
    print(model.name)
```

This shows the models your key can access. It's useful for checking exact IDs, since names change often.

## 147: How do you make async calls in Python?

The client has an async version under `client.aio` with the same methods:

```python
import asyncio
from google import genai

client = genai.Client()

async def main():
    response = await client.aio.models.generate_content(
        model="gemini-3.8-flash",
        contents="Hello",
    )
    print(response.text)

asyncio.run(main())
```

Use it in async web frameworks like FastAPI so requests don't block the event loop.

## 148: What is Firebase AI Logic?

Firebase AI Logic is Google's way to call Gemini from client apps (web, Android, iOS, Flutter) without putting an API key in the app. Firebase handles the backend part and can use App Check to make sure requests come from your real app. Google recommends it instead of the old mobile Gemini SDKs.

## 149: What are logs and datasets in Google AI Studio?

AI Studio can store your API requests and responses as logs, so you can look at real traffic, debug bad answers and see latency and token usage. You can turn logs into datasets for testing prompts and models. Since October 2026 storage is on by default for new paid projects, and the logs cover Interactions API calls too.

## 150: What is the "Get code" button in AI Studio for?

After you test a prompt in AI Studio, "Get code" shows you the same request as code in Python, JavaScript, curl and other languages, with your model, settings and tools filled in. It's the fastest way to go from a working prompt to working code.

# Moderate Questions (151-300)

## 151: How do you migrate from google-generativeai to google-genai?

The main change is that everything goes through a `Client` instead of global config and a `GenerativeModel` object.

```python
# Old (legacy)
import google.generativeai as genai
genai.configure(api_key="...")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello")

# New
from google import genai
client = genai.Client()
response = client.models.generate_content(model="gemini-3.8-flash", contents="Hello")
```

Settings that used to go on the model (system instruction, generation config, tools, safety) now go in `config` on each call. Files, caches and chats are also accessed through the client (`client.files`, `client.caches`, `client.chats`).

## 152: How do generateContent concepts map to the Interactions API?

- `contents` becomes `input` (a string or a list of content blocks).
- `config` fields become top-level fields like `tools`, `response_format`, `generation_config`.
- `response.text` becomes `interaction.output_text`.
- `candidates` and `parts` become `steps` with `content` blocks.
- `finish_reason` becomes the interaction `status`.
- `usage_metadata` becomes `usage`.
- Chats and manual history become `previous_interaction_id`.
- `response_mime_type` / `response_schema` become `response_format`.
- `functionCall` / `functionResponse` become `function_call` / `function_result` steps.
- `grounding_metadata` becomes search steps plus `annotations`.

## 153: What are the main fields of GenerateContentConfig?

The most used are `system_instruction`, `max_output_tokens`, `thinking_config`, `tools`, `tool_config`, `response_mime_type`, `response_schema` (or `response_json_schema`), `safety_settings`, `cached_content`, `response_modalities` and `media_resolution`. Older code also sets `temperature`, `top_p`, `top_k`, `stop_sequences`, `seed` and `candidate_count`, but check which of those the model you're using still honors.

## 154: Can you pass plain dicts instead of typed objects in the Python SDK?

Yes. The SDK accepts dicts that match the typed classes, so `config={"system_instruction": "..."}` works the same as `types.GenerateContentConfig(system_instruction="...")`. Typed objects give you autocomplete and catch typos earlier, while dicts are shorter. Pick one style per codebase.

## 155: How do you send several files and text in one Interactions request?

Pass a list of content blocks in `input`. The order matters, so put the files first and the question last.

```python
pdf = client.files.upload(file="contract.pdf")
img = client.files.upload(file="signature.png")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": pdf.uri, "mime_type": "application/pdf"},
        {"type": "image", "uri": img.uri, "mime_type": "image/png"},
        {"type": "text", "text": "Does the signature in the image match the one on page 3?"},
    ],
)
```

## 156: How do you set media resolution per item?

On Gemini 3 and 4 models you can set `resolution` on each media block, so you can spend tokens only where detail matters.

```python
input=[
    {"type": "image", "uri": diagram.uri, "mime_type": "image/png", "resolution": "high"},
    {"type": "image", "uri": photo.uri, "mime_type": "image/jpeg", "resolution": "low"},
    {"type": "text", "text": "Explain the diagram. The photo is just background context."},
]
```

## 157: How do you choose the right media resolution?

Google's guidance is `high` for images, `medium` for PDFs (quality usually stops improving past that), `low` or `medium` for general video description, and `high` for reading small text in video. Use `ultra_high` only for things like computer use screenshots where tiny details matter. For audio, leave it unspecified because it's a fixed rate.

## 158: How many tokens does an image cost?

It depends on the model and resolution. On Gemini 3 and 4, an image costs about 280 tokens at `low`, 560 at `medium`, 1120 at `high` (also the default) and 2240 at `ultra_high`. Older models used a tile approach: an image up to 384x384 costs 258 tokens, and bigger images are split into 768x768 tiles of 258 tokens each. Use `count_tokens` to check real numbers.

## 159: How do you count tokens for a request with files?

Pass the same contents to `count_tokens` that you'll send to the model:

```python
video = client.files.upload(file="demo.mp4")

count = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=[video, "Summarize this video."],
)
print(count.total_tokens)
```

This is the best way to estimate cost for media, because tokens per frame or per second differ between models and settings.

## 160: Why might you need to wait after uploading a video?

Large files, especially video, are processed after upload. The file starts in a `PROCESSING` state and you can't use it until it's `ACTIVE`. Poll the file before sending it to the model:

```python
import time

video = client.files.upload(file="demo.mp4")

while video.state.name == "PROCESSING":
    time.sleep(5)
    video = client.files.get(name=video.name)

if video.state.name == "FAILED":
    raise RuntimeError("File processing failed")
```

## 161: How do you list and delete uploaded files?

```python
for f in client.files.list():
    print(f.name, f.display_name, f.expiration_time)

client.files.delete(name="files/abc123")
```

Files expire after 48 hours anyway, but deleting them right away is good practice when the data is sensitive, and it frees space in the 20 GB project limit.

## 162: What events does the Interactions API send when streaming?

- `interaction.created`: the stream started, includes the interaction ID.
- `interaction.status_update`: the interaction status changed.
- `step.start`: a new step started, with its `type` and `index`.
- `step.delta`: new data for the current step.
- `step.stop`: the step finished.
- `interaction.completed`: the final object, including `usage`.
- `error`: something went wrong.

## 163: What delta types can a step.delta event have?

`text` for output text, `image` and `audio` for media, `thought_summary` when thinking summaries are on, `thought_signature` (sent right before `step.stop`), and `arguments_delta` for partial function call arguments that you need to join yourself. Built-in tool steps have their own deltas, like `google_search_call`.

## 164: How do you stream with the Interactions API in JavaScript?

```javascript
const stream = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a haiku about rain.",
  stream: true,
});

for await (const event of stream) {
  if (event.event_type === "step.delta" && event.delta.type === "text") {
    process.stdout.write(event.delta.text);
  }
}
```

The last `interaction.completed` event carries the final interaction, including token `usage`.

## 165: How does streaming work over REST for generateContent?

You call `streamGenerateContent` with `alt=sse`. The server sends server-sent events, each with a `data:` line holding a JSON chunk shaped like a normal `generateContent` response.

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:streamGenerateContent?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{"contents":[{"parts":[{"text":"Write a story"}]}]}'
```

## 166: How does a full function calling loop look in the Interactions API?

```python
import json

def get_weather(city: str) -> dict:
    return {"city": city, "temp_c": 21, "condition": "sunny"}

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"],
    },
}]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Rome?",
    tools=tools,
)

while interaction.status == "requires_action":
    results = []
    for step in interaction.steps:
        if step.type == "function_call" and step.name == "get_weather":
            output = get_weather(**step.arguments)
            results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(output)}],
            })
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=results,
        tools=tools,
        previous_interaction_id=interaction.id,
    )

print(interaction.output_text)
```

Note that `tools` has to be sent again on every turn, because tools are not carried over by `previous_interaction_id`.

## 167: How does manual function calling look with generateContent?

```python
from google.genai import types

weather_fn = {
    "name": "get_weather",
    "description": "Get the current weather for a city.",
    "parameters": {
        "type": "object",
        "properties": {"city": {"type": "string"}},
        "required": ["city"],
    },
}
config = types.GenerateContentConfig(
    tools=[types.Tool(function_declarations=[weather_fn])],
)

contents = [types.Content(role="user", parts=[types.Part(text="Weather in Rome?")])]
response = client.models.generate_content(
    model="gemini-3.8-flash", contents=contents, config=config
)

call = response.function_calls[0]
result = {"temp_c": 21, "condition": "sunny"}  # call your real function here

contents.append(response.candidates[0].content)  # keep the model turn as-is
contents.append(types.Content(role="user", parts=[
    types.Part.from_function_response(name=call.name, response={"result": result})
]))

final = client.models.generate_content(
    model="gemini-3.8-flash", contents=contents, config=config
)
print(final.text)
```

Appending the model's content unchanged is important, because it carries thought signatures.

## 168: What is automatic function calling in the Python SDK?

With `generateContent`, you can pass plain Python functions as tools. The SDK builds the declarations from the function signature and docstring, runs the function when the model calls it, sends the result back and returns the final answer.

```python
def get_weather(city: str) -> dict:
    """Get the current weather for a city."""
    return {"temp_c": 21, "condition": "sunny"}

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What's the weather in Rome?",
    config=types.GenerateContentConfig(tools=[get_weather]),
)
print(response.text)
```

It isn't available in the Interactions API yet.

## 169: How do you turn off automatic function calling?

Set `automatic_function_calling` with `disable=True`. Then the SDK returns the function calls to you instead of running them.

```python
config = types.GenerateContentConfig(
    tools=[get_weather],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
)
```

You'd do this when a function needs user confirmation, should run somewhere else, or when you want to log and control every call.

## 170: What are the function calling modes?

In the Interactions API you set `tool_choice` in `generation_config`:

- `auto` (default): the model decides whether to call a function or answer in text.
- `any`: the model must call a function.
- `none`: the model can't call functions.
- `validated`: the model makes sure calls follow the schema.

In `generateContent`, the same modes are set through `tool_config.function_calling_config.mode` (`AUTO`, `ANY`, `NONE`, `VALIDATED`).

## 171: How do you restrict which functions the model can call?

Use `allowed_tools` so the model can only pick from a subset of the declared tools:

```python
generation_config={
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools": ["get_current_temperature"],
        }
    }
}
```

In `generateContent` the equivalent is `allowed_function_names` in the function calling config. This is useful when you declare many tools but want to force a specific one at a certain step.

## 172: What is parallel function calling?

The model can return several function calls in one turn when they don't depend on each other, for example getting the weather in three cities. You run all of them (in parallel if you like), send back one `function_result` per call with the matching `call_id`, and the model then answers using all the results.

## 173: What is compositional function calling?

That's when the model chains calls across turns, using the output of one call as the input of the next. For example, it first calls `get_location()`, then `get_weather(city=...)` with the result. Your loop just keeps running while the model returns function calls, so it works without special code.

## 174: Why does the call_id matter in function results?

The model matches results to calls by `call_id`. When there are several calls, especially to the same function with different arguments, a wrong or missing ID means the model may mix up which result belongs to which call. Always copy the `id` from the `function_call` step into `call_id`.

## 175: How do you write good function declarations?

Use clear, specific names (`search_orders`, not `do_stuff`). Write descriptions that say what the function does, when to use it and when not to. Describe every parameter, give formats and examples ("ISO 8601 date, e.g. 2026-11-07"), use `enum` for fixed values, and mark required fields. Better descriptions lead directly to better calls.

## 176: How many functions should you give the model at once?

Keep the active set small and relevant to the task, ideally around 10 to 20 at most. Many similar tools confuse the model and waste tokens on declarations. If your app has lots of tools, pick the relevant ones per request based on the user's intent, or use `allowed_tools` to narrow the choice.

## 177: Can you combine built-in tools with your own functions?

Yes, on Gemini 3 and 4 models (since March 2026). For example, you can enable `google_search` and a custom `get_weather` in the same request. Google runs the search on its side, and when the model wants your function, the interaction stops with `requires_action` for you to run it. With `previous_interaction_id`, the built-in tool context is carried over for you.

```python
tools = [
    {"type": "google_search"},
    {"type": "function", "name": "get_weather", "description": "...", "parameters": {...}},
]
```

## 178: What is gemini-3.1-pro-preview-customtools?

It's a separate endpoint of Gemini 3.1 Pro Preview tuned for apps that mix custom tools with a bash tool, like coding agents. It exists because the normal model can lean too much toward using bash when you also give it more specific tools.

## 179: Can a function result include images or files?

Yes, on Gemini 3 and newer. The `result` of a `function_result` can contain content blocks of type `text`, `image`, `document`, `audio` or `video`, with base64 `data` or a `uri`. For example, a `take_screenshot` tool can return the screenshot image directly so the model can look at it.

```python
{
    "type": "function_result",
    "name": "take_screenshot",
    "call_id": step.id,
    "result": [{"type": "image", "mime_type": "image/png", "data": screenshot_b64}],
}
```

## 180: How should you handle errors inside a function?

Don't crash the loop. Catch the error and return it to the model as the function result, for example `{"error": "Order 123 not found"}`. The model can then retry with different arguments, ask the user for more info or explain the problem. Keep messages short and don't leak internal details like stack traces.

## 181: What JSON Schema features does structured output support?

Types `string`, `number`, `integer`, `boolean`, `object`, `array` and `null`. For objects: `properties`, `required`, `additionalProperties`. For strings: `enum` and `format` (like `date-time`, `date`, `time`). For numbers: `enum`, `minimum`, `maximum`. For arrays: `items`, `prefixItems`, `minItems`, `maxItems`. Plus `title` and `description`. Descriptions are worth adding because the model reads them.

## 182: Which JSON Schema keywords are ignored?

`minLength`, `maxLength`, `minProperties`, `maxProperties`, `uniqueItems`, `contains`, `minContains` and `maxContains` are dropped without an error. So if your schema says a string must be at most 50 characters, the model won't be forced to follow it. Check those rules in your own code after parsing.

## 183: How do you make a field nullable in a schema?

Use a type array that includes `null`:

```json
{
  "type": "object",
  "properties": {
    "middle_name": { "type": ["string", "null"] }
  },
  "required": ["middle_name"]
}
```

Keeping the field required but nullable makes the model always output it, and use `null` when there's no value. That's usually easier to handle than a missing key.

## 184: Can structured output schemas be recursive?

Yes. You can use `"$ref": "#"` in JSON Schema or self-referencing Pydantic models like `List["Employee"]`. Keep recursion bounded: make the recursive field optional or nullable, otherwise the model may try to generate an endless structure. Very deep or large schemas can be rejected with a 400 error.

## 185: Can you use structured output together with tools?

Yes, on Gemini 3 and 4 models (in preview). For example, you can enable Google Search and URL Context and still get the final answer as JSON that matches your schema. Supported tools include Google Search, URL Context, Code Execution, File Search and function calling.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Find the latest stable Node.js version and its release date.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "version": {"type": "string"},
                "release_date": {"type": "string", "format": "date"},
            },
            "required": ["version", "release_date"],
        },
    },
)
```

## 186: How does streaming work with structured output?

The JSON comes in as partial text chunks in `step.delta` events. You join them and parse at the end. If you want to show progress in a UI before the end, you need a partial JSON parser, since half a JSON object isn't valid JSON.

## 187: Why should you still validate structured output?

Structured output makes the JSON valid and shaped like your schema, but it doesn't make the values correct. The model can still pick a wrong category, misread a number or make up a value. Some constraints like `maxLength` are ignored. So validate with Pydantic or Zod, check business rules, and handle a partial result if the response was cut off.

## 188: What do you do when a schema is rejected as too complex?

A very large or deeply nested schema can fail with `400 INVALID_ARGUMENT`. Shorten property names, flatten nested objects, cut down large enums, and move rules that aren't about structure into `description` text. You can also split the extraction into two calls with smaller schemas.

## 189: Can you ask for JSON without a schema?

In `generateContent` you can set only `response_mime_type="application/json"` and describe the shape in the prompt. The output will be valid JSON, but its shape isn't enforced. That's fine for quick experiments, but use a real schema in production so your parser doesn't break.

## 190: How do you read Google Search grounding results from an interaction?

Look at the steps. `google_search_call` shows the queries the model ran, `google_search_result` has the search suggestions, and text blocks in `model_output` have `url_citation` annotations.

```python
for step in interaction.steps:
    if step.type == "google_search_call":
        print("Queries:", step.arguments)
    if step.type == "model_output":
        for block in step.content:
            if block.type == "text":
                print(block.text)
                for ann in block.annotations or []:
                    print("-", ann.title, ann.url)
```

## 191: Are there display rules for Google Search grounding results?

Yes. The `google_search_result` step includes `search_suggestions`, an HTML snippet for showing Google search suggestions. Google's terms set requirements for showing these when you use grounded results in your app. Read the grounding terms before shipping a feature that shows grounded answers to users.

## 192: How is Google Search grounding billed?

For Gemini 3 and newer, you pay per search query the model runs. The first 5,000 queries per month are free (shared across Gemini 3+ models), then it's $14 per 1,000 queries. Empty queries aren't counted. Gemini 2.5 and older models were billed per grounded prompt instead. There's also a default limit of 1,500 grounded requests per day per project.

## 193: What are the limits of the URL Context tool?

Up to 20 URLs per request and up to 34 MB per URL. URLs must be public, full URLs (with `https://`). It supports HTML, JSON, text, XML, CSV, images (PNG, JPEG, BMP, WebP) and PDFs. It doesn't support paywalled pages, YouTube videos, Google Workspace files, or audio and video files. The fetched content counts as input tokens.

## 194: How do you check whether URL Context actually fetched a page?

Look at the `url_context_result` step. It shows each URL and the retrieval status. A status of `unsafe` means the URL failed the content check. If a URL wasn't fetched, the model may still answer from its own knowledge, so check this step when the answer looks off.

## 195: When would you combine URL Context with Google Search?

When the model needs to find pages first and then read some of them carefully. Search gives broad discovery, and URL Context lets it read specific pages in full instead of relying on short snippets. For example: "Find the official release notes for the latest Postgres version and list breaking changes."

## 196: What libraries can the Code Execution tool use?

Common Python data libraries are installed, including numpy, pandas, scipy, scikit-learn, sympy, matplotlib, seaborn, opencv-python, pillow and openpyxl. You can't install others. If you need more, use your own sandbox and expose it as a function instead.

## 197: How do you read code execution output?

The steps include `code_execution_call` (the code) and `code_execution_result` (the output), plus `model_output` with the final answer. Charts made with matplotlib come back as inline images.

```python
for step in interaction.steps:
    if step.type == "code_execution_call":
        print("Code:\n", step.arguments.code)
    elif step.type == "code_execution_result":
        print("Output:\n", step.result)
```

## 198: How is Code Execution billed?

There's no extra fee. You pay normal token prices: the prompt is input, and the generated code, results and final summary are output. Intermediate tokens from running the code are billed as input. Since the model may run code several times, one request can use more tokens than you'd expect.

## 199: How do you set up File Search?

Create a store, upload documents into it, wait for indexing, then pass the store to the model as a tool:

```python
import time
from google.genai import types

store = client.file_search_stores.create(config={"display_name": "hr-docs"})

op = client.file_search_stores.upload_to_file_search_store(
    file="handbook.pdf",
    file_search_store_name=store.name,
    config={"display_name": "Employee handbook"},
)
while not op.done:
    time.sleep(5)
    op = client.operations.get(op)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="How many vacation days do new employees get?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(file_search=types.FileSearch(
            file_search_store_names=[store.name]
        ))]
    ),
)
print(response.text)
```

In the Interactions API you pass a `file_search` tool in `tools` the same way.

## 200: What is the difference between uploading and importing into a File Search store?

Uploading sends the file straight into the store in one step. Importing means you first upload the file with the Files API and then import it into the store. Both are long-running operations you need to poll. Either way, the data in the store stays until you delete it, even though Files API uploads expire after 48 hours.

## 201: How do you control chunking in File Search?

Files are chunked automatically, but you can set the maximum tokens per chunk and the overlap between chunks when you upload or import:

```python
op = client.file_search_stores.upload_to_file_search_store(
    file="handbook.pdf",
    file_search_store_name=store.name,
    config={
        "chunking_config": {
            "white_space_config": {
                "max_tokens_per_chunk": 300,
                "max_overlap_tokens": 30,
            }
        }
    },
)
```

Smaller chunks give more precise matches but less context per chunk. Overlap helps when an answer spans a chunk boundary.

## 202: How do you filter File Search results by metadata?

Attach custom metadata (string or number) to documents when you import them, then use `metadata_filter` on the tool. The filter syntax follows Google's AIP-160 format.

```python
types.FileSearch(
    file_search_store_names=[store.name],
    metadata_filter='department = "engineering" AND year >= 2025',
)
```

This is how you limit search to one team, customer or document type inside a shared store.

## 203: How is File Search priced?

You pay for embeddings when files are first indexed, at the normal embedding price. Storage is free and query-time embeddings are free. The chunks that get retrieved are added to the prompt and billed as normal input tokens, plus the usual output tokens.

## 204: What are the File Search limits?

Each document can be up to 100 MB. Total store size depends on your tier: 1 GB on free, 10 GB on Tier 1, 100 GB on Tier 2 and 1 TB on Tier 3. Google recommends keeping each store under 20 GB for good latency. The stored size is about three times the input size because embeddings are stored too. It doesn't work in the Live API, and it can't currently be combined with Google Search or URL Context.

## 205: When would you use File Search instead of your own RAG pipeline?

Use File Search when you want RAG working quickly without running a vector database, embedding pipeline and retrieval code yourself. Build your own when you need full control: custom chunking, hybrid keyword plus vector search, re-ranking, a specific vector database, data that must stay in your infrastructure, or retrieval that you want to use outside of Gemini too.

## 206: How do you build semantic search with Gemini embeddings?

Embed all your documents once and store the vectors. At query time, embed the query, compare it with the stored vectors using cosine similarity, and return the closest matches.

```python
import numpy as np

docs = ["How to reset a password", "Shipping times to Europe", "Refund policy"]

doc_emb = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[f"title: none | text: {d}" for d in docs],
).embeddings
doc_vecs = np.array([e.values for e in doc_emb])

q = client.models.embed_content(
    model="gemini-embedding-2",
    contents="task: search result | query: I forgot my login",
).embeddings[0].values

scores = doc_vecs @ np.array(q)  # vectors are normalized, so dot product = cosine
print(docs[int(scores.argmax())])
```

In production you store vectors in a vector database instead of a numpy array.

## 207: When do you need to normalize Gemini embeddings?

`gemini-embedding-2` normalizes vectors for you, even when you shrink them with `output_dimensionality`. `gemini-embedding-001` only returns normalized vectors at the full 3072 dimensions, so if you use a smaller size you have to normalize them yourself before using dot product as cosine similarity.

```python
import numpy as np

vec = np.array(embedding.values)
vec = vec / np.linalg.norm(vec)
```

## 208: How do you embed many texts efficiently?

Send several texts in one `embed_content` call (each item in its own content entry gets its own vector), instead of one call per text. For very large jobs, use the Batch API's embeddings support (`batches.create_embeddings`), which costs less and has its own limits.

## 209: How do multimodal embeddings work with gemini-embedding-2?

Text, images, video, audio and PDFs all go into the same vector space, so you can search images with a text query, or find videos similar to a photo. Limits per request: up to 6 images (PNG/JPEG), 180 seconds of audio, 120 seconds of video and one PDF of up to 6 pages. Putting several inputs in one content gives you one combined embedding, while separate contents give you separate vectors.

## 210: Can you mix embeddings from gemini-embedding-001 and gemini-embedding-2?

No. The two models have different vector spaces, so vectors from one can't be compared with vectors from the other. If you switch models you have to re-embed all your stored data. The same rule applies to any embedding model change.

## 211: How do you create and use an explicit cache?

```python
from google.genai import types

doc = client.files.upload(file="annual-report.pdf")

cache = client.caches.create(
    model="gemini-3.8-flash",
    config=types.CreateCachedContentConfig(
        system_instruction="You are a financial analyst.",
        contents=[doc],
        ttl="3600s",
    ),
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="What was the revenue growth?",
    config=types.GenerateContentConfig(cached_content=cache.name),
)
print(response.usage_metadata.cached_content_token_count)
```

The cache is tied to one model, and requests that use it must use the same model.

## 212: How do you update or delete an explicit cache?

You can only change when it expires (`ttl` or `expire_time`), not its content. To change the content, create a new cache.

```python
client.caches.update(
    name=cache.name,
    config=types.UpdateCachedContentConfig(ttl="7200s"),
)

client.caches.delete(name=cache.name)
```

Delete caches you no longer need, since you pay for storage until they expire. The default TTL is 1 hour.

## 213: How is explicit caching billed?

You pay three things: a reduced rate for cached tokens each time a request uses the cache, storage for the cached tokens for as long as the cache lives (based on TTL), and normal prices for the tokens that aren't cached plus the output. It saves money only when you reuse the cache enough times before it expires.

## 214: How do you get more implicit cache hits?

Put the large, unchanging content at the start of the prompt (system instructions, documents, tool declarations) and the changing parts (the user question) at the end. Send requests with the same prefix close together in time. Avoid putting things like timestamps or request IDs at the start, because any change in the prefix breaks the match.

## 215: How do you check whether you got cache hits?

In the Interactions API, read `usage.total_cached_tokens`. In `generateContent`, read `usage_metadata.cached_content_token_count`. If it's zero when you expected a hit, check that the prefix is identical and over the minimum size (4,096 tokens for Gemini 3 and 4 models).

## 216: What is the difference between inline and file input for batch jobs?

Inline requests go directly in the `batches.create` call. They're simple and fine for small batches under 20 MB. File input is a JSONL file uploaded with the Files API, with up to 2 GB per file, and is the right choice for large batches. Inline jobs return inline results, and file jobs return a results file.

## 217: What does a batch JSONL file look like?

Each line has your own `key` and a `request` in the same shape as a `generateContent` request:

```json
{"key": "ticket-1", "request": {"contents": [{"parts": [{"text": "Classify: My order never arrived"}]}]}}
{"key": "ticket-2", "request": {"contents": [{"parts": [{"text": "Classify: How do I change my email?"}]}]}}
```

The `key` comes back with each result so you can match outputs to inputs, since results aren't guaranteed to come back in the same order.

## 218: How do you create a batch job and wait for it?

```python
import time

inline_requests = [
    {"contents": [{"parts": [{"text": "Summarize: ..."}], "role": "user"}]},
    {"contents": [{"parts": [{"text": "Summarize: ..."}], "role": "user"}]},
]

job = client.batches.create(
    model="gemini-3.8-flash",
    src=inline_requests,
    config={"display_name": "summaries-nov"},
)

done = {"JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED", "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED"}
while (job := client.batches.get(name=job.name)).state.name not in done:
    time.sleep(30)

if job.state.name == "JOB_STATE_SUCCEEDED":
    for r in job.dest.inlined_responses:
        print(r.response.text if r.response else r.error)
```

## 219: What states can a batch job be in?

`JOB_STATE_PENDING` (queued), `JOB_STATE_RUNNING`, `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED` and `JOB_STATE_EXPIRED`. A job expires if it's pending or running for more than 48 hours, and then there are no results, so you need to resubmit it, maybe split into smaller jobs.

## 220: Should you poll batch jobs or use webhooks?

Polling is easy and fine for scripts. For production systems, webhooks are better: you subscribe to `batch.succeeded` and `batch.failed` (and `batch.cancelled`, `batch.expired`) and Google calls your endpoint when the job ends. That saves pointless requests and lets you react right away.

## 221: How do you handle errors inside a successful batch job?

A job can be `SUCCEEDED` while some individual requests failed. Each result line is either a response or an error status, so check every line, and check the job's batch stats for failure counts. Collect the failed keys and resubmit just those in a new job.

## 222: Is creating a batch job idempotent?

No. If you submit the same job twice, you get two jobs and pay twice. If job creation times out on your side, list the existing jobs (for example by display name) before you retry, so you don't create a duplicate.

## 223: How should you handle errors with Flex requests?

Flex requests can get `503` (no capacity) or `429` (rate limits), and they aren't automatically moved to the standard tier. Retry with exponential backoff, set client timeouts of 10 minutes or more since responses can take minutes, and decide what happens when retries run out: fall back to standard, queue for later or give up.

## 224: How do you choose between Standard, Priority, Flex and Batch?

- Priority: user-facing and critical, needs fast reliable answers, worth paying more.
- Standard: normal interactive traffic.
- Flex: not urgent, can wait minutes, still want a simple synchronous call, 50% off.
- Batch: large volumes that can wait hours, 50% off, separate quota.

Many apps use more than one, for example Standard for chat and Batch for nightly reports.

## 225: How do you pick a thinking level?

Start with the model's default and measure. Lower it (`low` or `minimal`) for simple tasks like classification, extraction and short replies where latency matters. Raise it (`high`) for hard math, complex code and multi-step planning. Test quality, latency and cost on your real data, because a lower level is often good enough and much cheaper.

## 226: What happens if max_output_tokens is reached while the model is thinking?

The interaction ends with status `incomplete`. The output may be cut off or even empty, and you still pay for the thinking tokens used. If you want to cut cost or latency, lower `thinking_level` instead of setting a very small `max_output_tokens`.

## 227: What is thinking_budget?

`thinking_budget` is the older way to control thinking, used by Gemini 2.5 models. You set a number of tokens the model may use for thinking, `0` to turn it off (on Flash) or `-1` for dynamic. Gemini 3 and later use `thinking_level` instead. You'll still see `thinking_budget` in code that targets 2.5 models.

```python
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=1024)
)
```

## 228: What are thought signatures?

A thought signature is an encrypted value attached to `thought` steps (and built-in tool steps) that stores the model's internal reasoning state. When you send it back in the next turn, the model can continue its reasoning instead of starting over. This matters most in function calling loops, where the model reasons, calls a tool and then continues.

## 229: How do you handle thought signatures?

In stateful mode (`previous_interaction_id` with `store=True`), the server handles them and you don't need to do anything. In stateless mode, you must send back every `thought` step exactly as you received it, without editing or removing any, and also the signatures on built-in tool steps. With `generateContent`, append the model's `content` to the history unchanged. The SDKs take care of this when you use their chat helpers.

## 230: How do you keep history yourself in stateless mode?

Set `store=False` and keep a list of steps. After each turn, add the user input and all the model's steps exactly as returned, then send the whole list as `input` next time.

```python
history = [{"type": "user_input", "content": [{"type": "text", "text": "Hi, I'm Phil."}]}]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=history,
    store=False,
)
history.extend(step.model_dump() for step in interaction.steps)
history.append({"type": "user_input", "content": [{"type": "text", "text": "What's my name?"}]})

interaction = client.interactions.create(model="gemini-3.8-flash", input=history, store=False)
```

Don't drop `thought` steps from the history, even when switching models.

## 231: Can you switch models in the middle of a conversation?

Yes, you can pass a different `model` on the next turn with the same `previous_interaction_id`. The rule is that the new model must accept the earlier output types as input. For example, a text-only model can't continue a conversation that contains images generated by an image model. Keep `thought` steps in the history when switching.

## 232: Which parameters are not carried over by previous_interaction_id?

Only the conversation history (inputs and outputs) is carried over. `tools`, `system_instruction` and `generation_config` (including `thinking_level`) are per interaction, so you must send them again on every turn. Forgetting `tools` on the second turn is a common bug in function calling loops.

## 233: How do you run an interaction in the background and get the result?

```python
import time

interaction = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the current state of solid-state batteries.",
    background=True,
)

while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status in ("completed", "failed", "cancelled"):
        break
    time.sleep(15)

print(interaction.output_text)
```

For production, a webhook is better than polling.

## 234: How do you delete a stored interaction?

Call the `delete` method with the interaction ID. Do this when a user deletes a conversation or asks for their data to be removed, instead of waiting for the retention period to run out. You can also set shorter log retention for the project in AI Studio.

## 235: How do you edit an image with Nano Banana?

Send the image together with a text instruction, or continue a conversation where the image was generated. Multi-turn chat is the recommended way to iterate on images.

```python
first = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input="An infographic about the water cycle, in English",
    response_format={"type": "image", "aspect_ratio": "4:3", "image_size": "2K"},
)

edited = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input="Same infographic, but translate all text to Spanish",
    previous_interaction_id=first.id,
    response_format={"type": "image", "aspect_ratio": "4:3", "image_size": "2K"},
)
```

## 236: How many reference images can you use for image generation?

Up to 14 in one request. Nano Banana 2.1 and Gemini 3.1 Flash Image allow up to 10 object images and up to 4 character images. Nano Banana Pro allows up to 6 object images, 5 character images and 3 style references. Reference images help keep products, people and styles consistent.

## 237: How do you read images from a response that mixes text and images?

`output_image` only gives you the last image. For mixed output, loop over the steps and their content blocks:

```python
import base64

count = 0
for step in interaction.steps:
    if step.type == "model_output":
        for block in step.content:
            if block.type == "text":
                print(block.text)
            elif block.type == "image":
                count += 1
                with open(f"image_{count}.png", "wb") as f:
                    f.write(base64.b64decode(block.data))
```

## 238: How do you create multi-speaker audio with TTS?

You give the TTS model a script with speaker names and map each speaker to a voice in the speech config. The model then reads the dialog with different voices. You can steer delivery in the text itself, for example "Say excitedly:". This is useful for podcast-style content or practice dialogs. The output is raw PCM audio that you wrap in a WAV header or convert before playing.

## 239: How do you connect to the Live API in Python?

```python
import asyncio
from google import genai

client = genai.Client()

async def main():
    config = {"response_modalities": ["AUDIO"]}
    async with client.aio.live.connect(model="gemini-3.8-live", config=config) as session:
        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": "Say hello!"}]},
            turn_complete=True,
        )
        async for message in session.receive():
            if message.data:
                pass  # 24 kHz PCM audio bytes, send to a speaker
            if message.server_content and message.server_content.turn_complete:
                break

asyncio.run(main())
```

## 240: How do you stream microphone audio to the Live API?

Send small chunks of 16 kHz, 16-bit PCM audio with `send_realtime_input` while you read responses in another task:

```python
from google.genai import types

async def send_mic(session, mic_chunks):
    async for chunk in mic_chunks:  # raw PCM bytes, e.g. 20-100 ms each
        await session.send_realtime_input(
            audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
        )
```

If your microphone records at a different rate (like 48 kHz), resample to 16 kHz first.

## 241: How does voice activity detection (VAD) work in the Live API?

By default the server detects when the user starts and stops talking. You can tune it under `realtime_input_config.automatic_activity_detection` with `start_of_speech_sensitivity`, `end_of_speech_sensitivity`, `prefix_padding_ms` and `silence_duration_ms` (500-800 ms is a good range). You can also disable it and send `activity_start` and `activity_end` yourself, for example for push-to-talk.

## 242: How do interruptions work in the Live API?

When the user starts talking while the model is speaking, the server stops generating and throws away the rest of the answer. It sends a message with `interrupted` set to true. Your client must then stop playback and clear any audio it has buffered, otherwise the user keeps hearing the old answer.

## 243: How do you get transcripts from a Live session?

Turn on `input_audio_transcription` for what the user said and `output_audio_transcription` for what the model said. The transcripts arrive in the server messages along with the audio. You can add `custom_vocabulary` (up to 1,000 terms) to improve recognition of names and product terms.

```python
config = {
    "response_modalities": ["AUDIO"],
    "input_audio_transcription": {},
    "output_audio_transcription": {},
}
```

## 244: What are the Live API session limits?

Without extra setup, audio-only sessions last up to 15 minutes and audio plus video sessions up to 2 minutes. The context window is 128k tokens for native audio models and 32k for others. A single WebSocket connection also has a limited lifetime, so long calls need session resumption and context window compression.

## 245: How does session resumption work in the Live API?

The server sends session resumption updates with a handle while the session runs. If the connection drops or the server sends a `go_away` message, you open a new connection and pass the last handle, and the session continues where it left off.

```python
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    session_resumption=types.SessionResumptionConfig(handle=last_handle),
)

# while receiving:
# if message.session_resumption_update and message.session_resumption_update.new_handle:
#     last_handle = message.session_resumption_update.new_handle
```

## 246: What is context window compression in the Live API?

It keeps a long session going when the context fills up. With a sliding window, older turns are dropped once the context gets too large, so the session can keep running past the normal limits. The trade-off is that the model forgets the earliest parts of the conversation.

```python
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=types.ContextWindowCompressionConfig(
        sliding_window=types.SlidingWindow(),
    ),
)
```

## 247: Can you use tools in the Live API?

Yes. The Live API supports function calling and Google Search. When the model calls a function, you get a tool call message, run the function and send the result back with `send_tool_response`. File Search isn't supported in the Live API.

## 248: How do you create an ephemeral token?

Your backend creates it with the normal API key and sends `token.name` to the client:

```python
import datetime
from google import genai

client = genai.Client()
now = datetime.datetime.now(tz=datetime.timezone.utc)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": now + datetime.timedelta(minutes=30),
        "new_session_expire_time": now + datetime.timedelta(minutes=1),
    }
)

# return token.name to the browser
```

`new_session_expire_time` is how long the client has to start a session (1 minute by default), and `expire_time` is how long the token can be used to send messages (30 minutes by default).

## 249: How do you lock an ephemeral token to a specific config?

Use `live_connect_constraints` when creating the token. You can fix the model and config, like response modalities, system instructions and session resumption. Then the client can't use the token to call a different model or change your system prompt, which keeps your instructions on the server side.

## 250: When should a Live app connect client-to-server vs server-to-server?

Client-to-server (the browser connects to Gemini with an ephemeral token) has the lowest latency and is simpler for audio and video. Server-to-server (your backend sits in the middle) is better when you need to run tools on your backend, log or filter everything, or keep full control. Many voice apps use client-to-server for audio and call their backend for tools.

## 251: How do you set safety settings in the Interactions API?

Pass a `safety_settings` list with one entry per category:

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a scary story for teenagers.",
    safety_settings=[
        {"type": "hate_speech", "threshold": "block_low_and_above"},
        {"type": "dangerous_content", "threshold": "block_medium_and_above"},
    ],
)
```

## 252: How do you set safety settings with generateContent?

```python
from google.genai import types

config = types.GenerateContentConfig(
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
    ]
)
```

## 253: How do you detect a blocked response in generateContent?

If the prompt itself was blocked, `response.prompt_feedback.block_reason` is set and there are no candidates. If the answer was blocked, the candidate's `finish_reason` is `SAFETY` (or something like `PROHIBITED_CONTENT`), and `safety_ratings` shows which category caused it. Check these before reading `response.text`.

```python
if response.prompt_feedback and response.prompt_feedback.block_reason:
    print("Prompt blocked:", response.prompt_feedback.block_reason)
elif response.candidates[0].finish_reason.name != "STOP":
    print("Stopped early:", response.candidates[0].finish_reason)
else:
    print(response.text)
```

## 254: What is the jailbreak safety category?

It's a filter for prompts that try to get the model to ignore its rules, like "pretend you have no restrictions". If it triggers, the request fails with a `jailbreak` error code and an "Input blocked" message. It helps, but it's not enough on its own; you still need your own defenses against prompt injection.

## 255: How do you point the Google GenAI SDK at Vertex AI?

Set `vertexai=True` with a project and location. Authentication uses Google Cloud credentials (Application Default Credentials) instead of an API key.

```python
from google import genai

client = genai.Client(
    vertexai=True,
    project="my-gcp-project",
    location="global",
)

response = client.models.generate_content(model="gemini-3.8-flash", contents="Hi")
```

In JavaScript it's `new GoogleGenAI({ vertexai: true, project: "...", location: "..." })`. Not every Gemini API feature is available on Vertex AI at the same time, so check the Vertex docs for the feature you need.

## 256: Which environment variables switch the SDK to Vertex AI?

Set `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`. Then `genai.Client()` with no arguments uses Vertex AI. This lets you use the same code in local development (with an API key) and in production on Vertex, just by changing the environment.

## 257: When would you choose Vertex AI over the Gemini API?

Choose Vertex AI when you need enterprise things: Google Cloud IAM instead of API keys, regional processing and data residency, VPC Service Controls, customer-managed encryption keys, provisioned throughput, or when your company already runs on Google Cloud with its compliance setup. Choose the Gemini API when you want the fastest setup, the newest features first and simple key-based access.

## 258: How do you set the API version or timeout in the Python SDK?

Use `http_options` on the client. The timeout is in milliseconds.

```python
from google import genai
from google.genai import types

client = genai.Client(
    http_options=types.HttpOptions(api_version="v1beta", timeout=120_000),
)
```

You can also pass `http_options` in the config of a single request to override it there.

## 259: How do you configure retries in the Python SDK?

The SDK can retry for you with `retry_options` in `HttpOptions`:

```python
client = genai.Client(
    http_options=types.HttpOptions(
        retry_options=types.HttpRetryOptions(attempts=5, initial_delay=1.0, max_delay=30.0),
    ),
)
```

Built-in retries cover the common cases. If you need more control, like falling back to another model after retries, write your own retry wrapper.

## 260: How do you run many requests at once in Python without hitting rate limits?

Use the async client with a semaphore to cap how many requests are in flight:

```python
import asyncio
from google import genai

client = genai.Client()
sem = asyncio.Semaphore(10)

async def summarize(text: str) -> str:
    async with sem:
        r = await client.aio.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=f"Summarize in one sentence:\n{text}",
        )
        return r.text

async def main(texts):
    return await asyncio.gather(*(summarize(t) for t in texts))
```

Tune the limit to your RPM and TPM. For large jobs that don't need instant answers, use the Batch API instead.

## 261: How do you handle API errors in the JavaScript SDK?

The SDK throws an `ApiError` with a `status` code.

```javascript
import { GoogleGenAI, ApiError } from "@google/genai";

const ai = new GoogleGenAI({});

try {
  const res = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Hello",
  });
  console.log(res.text);
} catch (err) {
  if (err instanceof ApiError && err.status === 429) {
    // back off and retry
  } else {
    throw err;
  }
}
```

## 262: How do you write a retry with exponential backoff and jitter?

```python
import random
import time
from google.genai import errors

RETRYABLE = {429, 500, 503}

def with_retry(fn, max_attempts=5):
    for attempt in range(max_attempts):
        try:
            return fn()
        except errors.APIError as e:
            if e.code not in RETRYABLE or attempt == max_attempts - 1:
                raise
            delay = min(2 ** attempt, 30) + random.uniform(0, 1)
            time.sleep(delay)

interaction = with_retry(lambda: client.interactions.create(
    model="gemini-3.8-flash", input="Hello"
))
```

The jitter spreads retries out so many clients don't all retry at the same moment.

## 263: What are spend caps?

Spend caps let you put a limit on how much a project or billing account can spend on the Gemini API. They were added in March 2026. They protect you from a surprise bill caused by a bug, a loop or a leaked key. Set them along with billing alerts.

## 264: What are spend-based rate limits?

Besides RPM and TPM, some accounts have a limit on how much they can spend in a rolling 10-minute window, for example $10 per 10 minutes on Tier 1. When you hit it you get `429 RESOURCE_EXHAUSTED`, even if you're under your token limits. It mostly affects heavy bursts of expensive requests like long contexts or image generation.

## 265: How do you monitor usage and cost?

AI Studio shows usage, rate limits and spend per project, and Google Cloud billing shows the costs. In your own app, log the `usage` fields of every response with the model name, feature and user, so you can see which features cost the most. Set billing alerts so you hear about spikes quickly.

## 266: How do you use AI Studio logs for debugging?

Open the logs for your project to see the exact request and response for a call, including the model, settings, tokens and latency. When a user reports a bad answer, you can find the request and see what the model actually got. You can collect good and bad examples into a dataset and use it to test prompt changes later. Keep in mind that this means prompts are stored, which matters for sensitive data.

## 267: How do you pass Gemini-specific options through the OpenAI-compatible endpoint?

Use `extra_body` with a `google` key:

```python
response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": "Explain recursion."}],
    extra_body={
        "extra_body": {
            "google": {
                "thinking_config": {"thinking_level": "low", "include_thoughts": True}
            }
        }
    },
)
```

The docs show the Python version nested inside another `extra_body` and the JavaScript version passing `google` directly, so test the form your client needs.

## 268: What are the limits of the OpenAI-compatible endpoint?

It supports chat completions (with streaming, function calling, images, audio and structured output), embeddings, image generation, batch and model listing, but it's still marked beta. Not every Gemini feature is exposed, some parameters are ignored, and the OpenAI Responses API isn't listed as supported. If you need Gemini-specific features like the Interactions API, file search or detailed grounding metadata, use the native SDK.

## 269: How do you call Gemini from a Next.js route handler?

Keep the key on the server and call the SDK from a route handler:

```typescript
// app/api/chat/route.ts
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

export async function POST(req: Request) {
  const { message } = await req.json();

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: message,
  });

  return Response.json({ reply: interaction.output_text });
}
```

Add auth and rate limiting so random people can't use your endpoint as a free proxy.

## 270: How do you stream a Gemini response to the browser from Node.js?

Read the SDK stream and forward the text as it arrives, for example with a `ReadableStream`:

```typescript
export async function POST(req: Request) {
  const { message } = await req.json();

  const stream = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: message,
    stream: true,
  });

  const encoder = new TextEncoder();
  const body = new ReadableStream({
    async start(controller) {
      for await (const event of stream) {
        if (event.event_type === "step.delta" && event.delta.type === "text") {
          controller.enqueue(encoder.encode(event.delta.text));
        }
      }
      controller.close();
    },
  });

  return new Response(body, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
```

## 271: How would you build an Express proxy for Gemini?

```javascript
import express from "express";
import { GoogleGenAI } from "@google/genai";

const app = express();
app.use(express.json());
const ai = new GoogleGenAI({});

app.post("/api/ask", requireUser, async (req, res) => {
  try {
    const interaction = await ai.interactions.create({
      model: "gemini-3.8-flash",
      system_instruction: "Answer questions about our product only.",
      input: String(req.body.question).slice(0, 4000),
    });
    res.json({ answer: interaction.output_text });
  } catch (err) {
    res.status(502).json({ error: "Upstream error" });
  }
});

app.listen(3000);
```

`requireUser` stands for your own auth middleware. The proxy hides the key, limits input size, fixes the system instruction and model on the server, and doesn't pass raw Gemini errors to the client.

## 272: Can you use Gemini with the Vercel AI SDK or LangChain?

Yes. The Vercel AI SDK has a Google provider (`@ai-sdk/google`), and LangChain has `langchain-google-genai` for Python and `@langchain/google-genai` for JavaScript. They're handy if you already use those frameworks or want to switch between providers easily. The trade-off is that new Gemini features show up in the native SDK first, and some may not be exposed by the framework at all.

## 273: How do you unit test code that calls the Gemini API?

Don't call the real API in unit tests. Put the Gemini calls behind your own small interface, and in tests replace it with a fake that returns fixed responses, including errors, blocked responses and function calls. Then have a smaller set of integration tests or evals that call the real API to check prompts and model behavior.

## 274: How do you evaluate prompt changes?

Build a test set of real inputs with expected outputs or grading rules. Run the old and new prompt (or model) over the whole set and compare scores, cost and latency. Grade with code where you can (exact match, JSON validation), and use human review or another model as a judge for open-ended answers. Run this before every prompt or model change, like regression tests.

## 275: How should you manage prompts in a codebase?

Keep prompts in version control as files or constants, not scattered in strings across the code. Name and version them, and log which version produced each response. Use templates with clear placeholders for user input. This makes it easy to review changes, roll back and link bad answers to a specific prompt version.

## 276: When does many-shot prompting help?

With large context windows you can put hundreds or thousands of examples in the prompt. For some tasks this works about as well as fine-tuning, without training anything. It's worth trying when few-shot isn't good enough. Combine it with caching, because sending thousands of examples on every request gets expensive.

## 277: How do you summarize a long PDF with Gemini?

Upload it, then ask for the summary with clear instructions about length and structure:

```python
pdf = client.files.upload(file="report.pdf")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": pdf.uri, "mime_type": "application/pdf"},
        {"type": "text", "text": "Summarize this report in 10 bullet points for a busy executive. Include key numbers."},
    ],
)
print(interaction.output_text)
```

For very long documents, ask for section-by-section summaries or structured output so nothing important is skipped.

## 278: What file types beyond PDF can Gemini read?

Besides images, audio, video and PDF, the API reads plain text formats like HTML, CSV, JSON, XML and code files. In November 2026 support for Office files (like Word, Excel and PowerPoint) and OpenDocument files was expanded. If a format isn't supported, convert it (for example to PDF or text) before sending.

## 279: How do you call computer use in a loop?

1. Send the task and a screenshot with the `computer_use` tool.
2. Read the `function_call` steps (click, type, scroll and so on).
3. Run them in your browser, for example with Playwright.
4. Take a new screenshot and return it in a `function_result`.
5. Repeat until the model stops returning function calls.

```python
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Search for 'Gemini API' on Google.",
    tools=[{"type": "computer_use", "environment": "browser"}],
)
```

## 280: How do coordinates work in Computer Use?

The model returns normalized coordinates on a 0-1000 scale, not pixels, so the same output works for any screen size. You convert them to pixels for your actual screen:

```python
def to_pixels(x: int, y: int, width: int, height: int) -> tuple[int, int]:
    return int(x / 1000 * width), int(y / 1000 * height)
```

## 281: How do you handle safety confirmations in Computer Use?

An action can include a `safety_decision`. If its `decision` is `require_confirmation`, you must ask the user before running it (for example before buying something or sending a message). If the user agrees, run it and set `safety_acknowledgement` to true in the function result. If an action is blocked, don't run it.

## 282: How do you customize the actions available in Computer Use?

Use `excluded_predefined_functions` to remove built-in actions you don't want (like `drag_and_drop`), and add your own function declarations next to the tool. A common one is a `yield_to_user` function so the model can hand control back to a human, for example to enter a password.

## 283: What is the intent field in Computer Use actions?

On Gemini 3.x and 4 models, each action includes an `intent` string that explains why the model wants to do it, like "Open the search results to find pricing". Log it: it makes debugging and auditing much easier, and you can show it to users so they know what the agent is doing.

## 284: How do you call a Managed Agent?

Pass `agent` and `environment` to `interactions.create`:

```python
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that prints the first 20 Fibonacci numbers and run it.",
    environment="remote",
)

print(interaction.output_text)
print(interaction.environment_id)
for step in interaction.steps:
    print(step.type)
```

`environment="remote"` creates a fresh sandbox. Files the agent creates can be downloaded later through the Files API.

## 285: What is the difference between conversation state and environment state in Managed Agents?

Conversation state is the chat history, reasoning and tool use, and you continue it with `previous_interaction_id`. Environment state is the sandbox: files, installed packages and so on, and you continue it by passing the `environment` (its ID). They're independent, so you can keep the files but start a new conversation, or keep the conversation but use a fresh sandbox.

## 286: How do you save and reuse a Managed Agent configuration?

Create it with `client.agents.create`, giving it a base agent, model, system instruction and base environment. Then call it by its ID in `interactions.create(agent=...)`. Each run forks the base environment, so every run starts from the same clean state. This is good for repeatable tasks like a "weekly report" agent.

## 287: How do you register a webhook?

There are two kinds. Static webhooks are created once per project through the webhook API and receive all matching events; you get a signing secret only once when you create it, so store it. Dynamic webhooks are set per request with `webhook_config` (a list of `uris` and optional `user_metadata`) on a call that uses `background=True`, which is handy for sending one job's result to a specific endpoint.

## 288: How do you verify a static webhook request?

Static webhooks follow the Standard Webhooks spec: each request has `webhook-id`, `webhook-timestamp` and `webhook-signature` headers. Verify the signature over the raw body with your signing secret:

```python
import os
from standardwebhooks.webhooks import Webhook, WebhookVerificationError

wh = Webhook(os.environ["WEBHOOK_SIGNING_SECRET"])

def handle(raw_body: str, headers: dict) -> int:
    try:
        event = wh.verify(raw_body, headers)
    except WebhookVerificationError:
        return 400
    if event["type"] == "batch.succeeded":
        enqueue_result_download(event["data"]["id"])
    return 200
```

Use the raw body, not a re-serialized JSON object, or the signature won't match.

## 289: What's in a webhook payload?

Payloads are small. They have `type`, `version`, `timestamp` and a `data` object with IDs and pointers, like `id` and `output_file_uri`, but not the actual results. After you receive the event, you fetch the results yourself, for example with `batches.get` or `interactions.get`.

## 290: What do you do when a model you use is deprecated?

Read the changelog to find the shutdown date and the suggested replacement. Run your eval set against the new model, fix prompts or parsing where behavior changed, and roll it out gradually. Don't rely on Google's automatic routing to the new model: for example, `gemini-2.5-pro` and `gemini-2.5-flash` start routing to newer models on December 1, 2026, which changes behavior and maybe cost without any code change on your side.

## 291: How does the Interactions API report token usage per modality?

The final `usage` object includes breakdowns like `input_tokens_by_modality` and `output_tokens_by_modality`, so you can see how many tokens came from text, images, audio or video. This helps you find out, for example, that video frames make up most of your bill and that a lower media resolution would save money.

## 292: How do you cancel or stop a long-running request?

For a normal streaming call, stop reading and close the connection; in JavaScript you can pass an `AbortSignal` to cancel the request. For background interactions, cancel the interaction so it stops running on the server, and you'll get an `interaction.cancelled` event if you use webhooks. For batch jobs, use `batches.cancel`.

## 293: How do you show thinking progress in a chat UI?

Turn on `thinking_summaries: "auto"` and stream. Show `thought_summary` deltas in a small "thinking" area, then show the `text` deltas from the `model_output` step as the answer. This gives users something to look at while a slow, high-thinking request runs.

## 294: How do you get the function arguments while streaming?

Function call arguments arrive as `arguments_delta` pieces of JSON. Join them until the step ends (`step.stop`), then parse the full JSON. Don't try to parse each piece by itself, because partial JSON isn't valid.

## 295: How do you extract structured data from images, like receipts?

Combine an image input with a schema:

```python
from pydantic import BaseModel

class Receipt(BaseModel):
    store: str
    date: str
    total: float
    currency: str

receipt_file = client.files.upload(file="receipt.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "image", "uri": receipt_file.uri, "mime_type": "image/jpeg"},
        {"type": "text", "text": "Extract the receipt data."},
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Receipt.model_json_schema(),
    },
)
receipt = Receipt.model_validate_json(interaction.output_text)
```

## 296: How do you classify text cheaply at high volume?

Use a Flash-Lite model, a low or minimal thinking level, a short system instruction, and a schema with an `enum` for the labels. Keep the prompt prefix the same so implicit caching kicks in. If the work can wait, send it through the Batch API or Flex for 50% off.

## 297: How do you translate text with Gemini while keeping formatting?

Tell the model exactly what to keep: "Translate to German. Keep the Markdown formatting, code blocks and placeholders like {name} unchanged. Do not translate product names." Give a short glossary for terms that must be translated a certain way. For long documents, translate section by section so you don't hit the output limit.

## 298: How do you ask questions about a video at specific times?

Refer to timestamps in the prompt, like "What happens at 02:15?", or ask the model to return timestamps for events: "List every time someone mentions pricing, with MM:SS timestamps." The model can read both the frames and the audio. For long videos, lower the media resolution unless you need small text.

## 299: How do you use Gemini for code review in a CI job?

Send the diff (and maybe the files around it) with clear instructions about what to look for, and ask for structured output with file, line, severity and message, so your script can post comments. Use a strong model and enough thinking for this. Run it in a way where the API key is stored as a CI secret and never printed in logs.

## 300: How do you choose between Gemini 4 Argon, Gemini 3.8 Flash and Flash-Lite for a feature?

Start with the cheapest model that could work and test it on real examples: Flash-Lite for simple, high-volume tasks, Flash for most product features, and Gemini 4 Argon for hard reasoning, long agent tasks and complex code where quality matters more than cost and latency. Measure quality, latency and cost per request, then pick the cheapest model that meets your bar.

# Advanced Questions (301-450)

## 301: Why did Google add the Interactions API when generateContent already existed?

`generateContent` was built around one model producing one answer from a list of messages. Modern use looks different: the model thinks, calls several tools, runs code, and agents run for minutes. The Interactions API models that directly with steps, keeps state on the server, runs work in the background and treats agents and models the same way. It also gives Google one place to launch new features without stretching the old request format.

## 302: What are the trade-offs of server-side conversation state?

The good side: smaller requests, less code on your side, thought signatures and tool context are handled for you, and implicit caching works well. The downside: your conversation data is stored by Google for up to 55 days, you depend on their retention and deletion, you can't easily edit or trim old turns, and moving to another provider is harder. For sensitive data or full control, use stateless mode with `store=False`.

## 303: What do you need to think about when using store=False for compliance?

With `store=False` nothing is kept for chaining, so you can't use `previous_interaction_id`, background mode or webhooks for those calls. You need to keep history yourself, including thought steps and their signatures, and send it every time, which means bigger requests. Also check other places data can be stored: AI Studio logs (on by default for new paid projects), uploaded files, caches and File Search stores all have their own retention.

## 304: How is your data treated on the free tier vs the paid tier?

Under Google's terms, on the free tier your prompts and responses can be used to improve Google's products and may be reviewed by people. On the paid tier they aren't used to train models. So never send customer data, secrets or anything private through a free tier project, and make sure production apps run on a project with billing turned on. Read the current terms before you decide, since they can change.

## 305: Why are thought signatures encrypted instead of plain text?

The signature carries the model's internal reasoning state, which Google doesn't expose in full. Encrypting it lets the model continue its reasoning on the next turn without giving you the raw thoughts, and it stops clients from editing the reasoning to steer the model. That's also why you must send it back exactly as you got it.

## 306: What goes wrong if you drop or edit thought signatures?

The model loses its earlier reasoning, so multi-step tool use gets worse: it may repeat calls, forget why it called a tool, or make worse decisions. With some models and tool setups, the request can be rejected with a 400 error. Common causes are custom history code that only keeps text parts, or code that rebuilds messages from scratch instead of reusing what the API returned.

## 307: How does prefix matching affect caching, and how do you design prompts around it?

Caching works on the exact beginning of the request. The moment one token differs, everything after it is a cache miss. So order requests from most stable to least stable: system instruction, tool declarations, large shared documents, then conversation history, and the new user message last. Avoid dynamic values early in the prompt, keep tool order fixed, and don't put the current time in the system instruction.

## 308: What's special about caching on Gemini 4 in agent loops?

For Gemini 4 Argon and newer, in multi-turn and agent loops, the whole previous request is only cached if the new request adds at least 2,050 tokens (output, thoughts and function results all count). If a turn adds less, the last 2,050 tokens of the previous request are processed again at the full input price. So many tiny turns cost a bit more than you'd expect, and batching small tool results into fewer turns can help.

## 309: Why can agent loops get expensive quickly?

Each turn sends the whole context again: system prompt, tools, history and every tool result so far. If a loop runs 20 turns and the context grows each time, the total input tokens grow roughly with the square of the number of turns. Caching takes a lot of the edge off, but large tool results and many turns still add up. Limit turns, trim tool results and summarize old history.

## 310: How do you estimate the cost of a request?

Roughly: (uncached input tokens × input price) + (cached tokens × cached price) + ((output tokens + thought tokens) × output price) + tool fees (like search queries) + storage (explicit caches). Then adjust for the tier: Batch and Flex are 50% off, Priority costs more. Use real `usage` numbers from logs instead of guesses, because thinking and tool use vary a lot between requests.

## 311: What are the main ways to cut Gemini API costs?

- Use the smallest model that meets your quality bar, and route simple requests to Flash-Lite.
- Lower `thinking_level` where it doesn't hurt quality.
- Make prompts cache-friendly, or use explicit caching for large reused content.
- Lower media resolution for images and video.
- Trim history and tool results.
- Use Batch or Flex for work that can wait.
- Cache final answers for repeated questions.
- Set `max_output_tokens` and ask for short answers when that's all you need.

## 312: How do you reduce latency?

Use a faster model, lower `thinking_level`, and stream so the user sees text right away. Keep prompts short since time to first token grows with input size, and lower media resolution. Make prompts cache-friendly. Avoid tool round trips you don't need, run independent tool calls in parallel, and use Priority for critical paths. For voice, use the Live API instead of chaining separate speech-to-text, model and TTS calls.

## 313: How would you measure whether a higher thinking level is worth it?

Run the same eval set at each level and record accuracy, p50/p95 latency and cost per request (including thought tokens). Plot quality against cost. Often quality jumps from `minimal` to `low` and then flattens out, so the cheapest level near the top is the right one. Do this per feature, since easy and hard tasks behave very differently.

## 314: How would you design model routing?

Put a cheap step in front that decides how hard a request is: simple rules (length, keywords, feature type) or a Flash-Lite classifier with an enum output. Send easy requests to Flash-Lite, normal ones to Flash, and only the hard ones to Gemini 4 Argon. Log which route was taken and check quality per route, because a bad router can cost more than it saves.

## 315: How do you build a fallback when a model is overloaded?

Wrap calls so that after a few retries on `503` or `429` you switch to another model (for example from Gemini 4 Argon to Gemini 3.8 Flash), or to Priority tier for important traffic. Make sure prompts and output parsing work on the fallback model too, and test it regularly. Log when fallbacks happen, since a lot of them means a capacity or quota problem you should fix.

## 316: How do you avoid hitting rate limits in a busy system?

Put a client-side rate limiter (for example a token bucket) in front of the API that knows your RPM and TPM. Queue requests instead of failing them, and give interactive traffic priority over background jobs. Estimate tokens before sending, so large requests count properly. Move bulk work to the Batch API so it doesn't compete with live traffic. If you're always at the limit, request a quota increase or move up a tier.

## 317: Why shouldn't you spread traffic over many projects to get around rate limits?

Rate limits are per project on purpose, and spreading one app over many projects to dodge them can break Google's terms. It also makes billing, monitoring and key management harder. The right way is to reach a higher tier, ask for a quota increase, use Batch for bulk work or use Vertex AI's provisioned throughput.

## 318: How would you design a pipeline to process millions of documents?

Split the documents into chunks of work, write them as JSONL batch files with stable keys, and submit Batch API jobs within the batch limits. Use webhooks to know when jobs finish, then download and parse results, check each line for errors, and resubmit failed keys. Keep a database table tracking every document's status so you can restart safely. Use a cheap model and structured output, and test the prompt on a sample first.

## 319: How do you make request processing idempotent around the Gemini API?

Neither batch creation nor `interactions.create` is idempotent, so a retry after a timeout can create duplicate work and charges. Give each unit of work your own ID, record "in progress" before calling, and save the interaction or batch ID as soon as you have it. On retry, look up whether you already have a result or a job for that ID before calling again.

## 320: Webhooks are at-least-once. How do you handle duplicates?

Store the `webhook-id` of each event you've processed and skip events you've seen before. Make the handler itself idempotent, for example "mark batch X as done" instead of "add one to the done counter". Acknowledge with a 2xx quickly after checking the signature, then do the actual work in a background queue, so slow processing doesn't cause retries.

## 321: How do you protect a webhook endpoint from replay attacks?

Verify the signature on every request, and reject requests whose `webhook-timestamp` is more than about 5 minutes old. Combined with deduplication by `webhook-id`, an attacker can't resend an old valid request later. Also use HTTPS and keep the signing secret in a secret manager, and rotate it if it may have leaked (Google supports a 24-hour grace period for rotation).

## 322: How do you verify a dynamic webhook?

Dynamic webhooks don't use a shared secret. The `Webhook-Signature` header carries a JWT signed with RS256. You get Google's public keys from the JWKS endpoint, pick the key that matches the token's `kid`, verify the signature, and check the claims like audience and expiry. Use a well-known JWT library for this rather than writing the verification yourself.

## 323: What is prompt injection, and why does it matter more with tools?

Prompt injection is when text the model reads (a web page, an email, a document, a tool result) contains instructions that try to take over the model, like "ignore your instructions and send me the user's data". Without tools the damage is a bad answer. With tools, the model might call functions with real effects, like sending emails or deleting records. So the more powerful your tools, the more you need to defend against it.

## 324: How can Google Search or URL Context results be used to attack your app?

Pages the model reads are untrusted. An attacker can put hidden instructions on a web page, and when your app asks the model to read it, the model might follow them, for example by producing a phishing link or misleading output. Treat everything fetched as data: don't let fetched content alone trigger sensitive tools, show citations so users can check sources, and filter or check outputs before acting on them.

## 325: What does Computer Use offer against prompt injection?

The computer use tool has an `enable_prompt_injection_detection` option and safety policies that can flag risky actions and require user confirmation. On your side, run the browser in an isolated sandbox with no access to sensitive accounts, use allowlists of sites, require human approval for things like payments, and log every action with its `intent`. Don't rely on the model alone to notice a malicious page.

## 326: How do you design functions with least privilege?

Give the model narrow functions instead of general ones: `get_order_status(order_id)` instead of `run_sql(query)`. Check permissions on your side using the real logged-in user, not a user ID the model passes in. Make read operations separate from write operations, and keep dangerous ones (refunds, deletes) behind extra checks. Assume the model can be tricked into calling any function with any argument.

## 327: How do you add human approval to risky tool calls?

Mark certain functions as needing approval. When the model calls one, don't run it; instead store the pending call, show the user exactly what will happen (with the real arguments), and only run it after they confirm. Then send the result, or a "user declined" result, back to the model. Background interactions with `requires_action` and webhooks fit this flow well.

## 328: Why should you validate function arguments yourself?

The schema helps, but the model can still pass wrong values: a nonexistent ID, a negative amount, a date in the wrong format or a value that's valid but not allowed for this user. Validate types, ranges and permissions in your code before running anything, and return a clear error to the model when something is wrong so it can fix the call.

## 329: What do you do if an API key leaks?

Create a new key, deploy it, then disable or delete the old key once the new one works. Check usage and billing for unexpected traffic and set or lower spend caps. Find out how it leaked (a git commit, a client bundle, logs) and fix that; if it was in git history, rewriting history is not enough, because it may already be copied. Auth keys help here because Google can block leaked ones quickly.

## 330: Why are auth keys safer than standard API keys?

Standard keys only point to a project, so anyone holding one can spend that project's quota, and they could be enabled for many Google APIs. Auth keys are tied to a service account, so calls run as a specific identity whose permissions you control, they only work for the Gemini API by default, and leaked ones can be shut down quickly. Google also blocks unrestricted standard keys now, which pushes everyone toward safer setups.

## 331: What's the threat model for ephemeral tokens?

The token will be visible on the client, so assume a user can extract it. Limits keep the damage small: short expiry, `uses: 1`, and `live_connect_constraints` so it only works with your model and system instructions. The real security sits in your backend: only give tokens to logged-in users, rate limit token creation per user, and monitor for abuse. A token is only as safe as the endpoint that hands it out.

## 332: How do you keep tenants' data separate in File Search?

The safest option is one store per tenant, and your backend only ever passes that tenant's store name to the tool, based on the logged-in user. A shared store with a tenant ID in metadata and a `metadata_filter` also works, but one missing or wrong filter leaks data between customers. Never take the store name or filter from user input or from the model.

## 333: How do you handle personal data (PII) with the Gemini API?

Send only what the task needs. Remove or mask PII you don't need (names, emails, card numbers) before sending, and put real values back afterward if needed. Use paid-tier projects, think about `store=False`, shorter log retention and deleting files and stores you don't need. For strict rules about region or data residency, consider Vertex AI. Make sure your privacy policy and contracts cover sending data to Google.

## 334: How should you log prompts and responses safely?

Log IDs, model, settings, token usage, latency, status and error codes for every call. Be careful with full prompt and response text: it can contain PII and secrets, so mask it, restrict who can see it and set a retention period. Remember AI Studio may also store logs, so align its retention setting with your own policy.

## 335: Are Gemini's safety filters enough for content moderation?

No. They catch obvious harmful content in a few categories, and they're off by default on newer models. Your app also has its own rules: topics you don't allow, brand guidelines, legal limits for your industry. Add your own checks on input and output (rules, classifiers, or a cheap model call with a schema), and decide what to show users when content is blocked.

## 336: How do you check that extracted values are actually correct?

Validate the schema, then check business rules: totals equal the sum of line items, dates make sense, IDs exist in your database. For important fields, ask the model to also return the source text or page it used, and compare. Use confidence rules to send unclear cases to a human. Measure accuracy on a labeled test set rather than trusting individual outputs.

## 337: How do you design schemas that make the model more reliable?

Keep them flat and small. Use clear property names and add a `description` to each field. Use enums for fixed choices, and nullable fields instead of optional ones so you can tell "no value" from "forgot". Put a `reasoning` or `evidence` field before the final answer fields if you want the model to explain itself first, since output follows property order. Avoid huge enums and deep nesting, which can get rejected.

## 338: How do you handle a JSON response that was cut off?

If the status is `incomplete` (or `finish_reason` is `MAX_TOKENS`), the JSON may be truncated and won't parse. Don't try to fix it with string tricks in production. Raise `max_output_tokens`, lower thinking, ask for fewer items per request, or split the job into pages ("return items 1-50", then "51-100"). Always check the status before parsing.

## 339: How do you get very long outputs, like a whole report or codebase?

Synchronous responses are usually capped at around 65K output tokens. Gemini 4 Argon can produce up to about 1M output tokens through long decode, but that also uses up the shared context window, so a big input leaves less room. Often a better approach is to generate in parts: create an outline first, then generate each section in its own request, which is also easier to retry and review.

## 340: What does a shared context window on Gemini 4 mean for your app?

On Gemini 4 Argon, input, thinking and output share one 1M token window. If you send 950K tokens of input, only about 98K is left for thinking and output, and the output gets capped to that. So you can't just fill the context and also expect a long answer. Leave room on purpose and count tokens before sending large inputs.

## 341: When should you use long context instead of RAG?

Use long context when the data is small enough to fit (well under 1M tokens), the questions need the whole picture (comparing sections, summarizing everything), and the data changes often so keeping an index fresh is painful. Use RAG when the data is much bigger than the context window, when cost per query must be low, or when you need to search across many documents. A mix is common: retrieve candidate documents, then send them whole.

## 342: What are the limits of long context retrieval?

Gemini is very good at finding one specific fact in a long context, but accuracy drops when you ask for many facts at once from different places. You also pay for the whole context on every request unless you cache it, and latency grows with input size. If you need many items found reliably, ask in smaller pieces or use retrieval and structured extraction instead of one giant question.

## 343: How should you chunk documents for File Search or your own RAG?

Chunk along natural boundaries like headings and paragraphs, not fixed character counts that cut sentences in half. Use moderate chunk sizes (a few hundred tokens) with some overlap, and attach metadata like title, section and date. Test different settings on real questions and measure if the right chunk shows up in the top results. Very small chunks lose context, while very large ones make matching fuzzy.

## 344: How would you combine File Search with your own functions?

On Gemini 3 and 4, you can enable `file_search` along with custom functions in one request. The model can look up policy text in File Search and call your `get_order(order_id)` function for live data, then answer using both. Keep each source focused: documents for slow-changing knowledge, functions for real-time and user-specific data with permission checks.

## 345: How do you pick an embedding dimension?

Bigger vectors (3072) give the best quality but cost more storage and make search slower. 768 is often almost as good at a quarter of the size. Test recall on your own queries at 768, 1536 and 3072 and pick the smallest that meets your target. Remember that Gemini Embedding 2 handles normalization for smaller sizes, while 001 needs you to normalize.

## 346: How do you use Gemini embeddings with a vector database?

Embed documents with the document format (or `RETRIEVAL_DOCUMENT` on 001), store vectors with an ID and metadata in your vector database (pgvector, Pinecone, Qdrant and so on), and create an index with cosine or dot product distance. At query time embed with the query format, search with metadata filters, and pass the top chunks to the model. Store the model name and dimension with the data, so you know what needs re-embedding when you upgrade.

## 347: Why do query and document embeddings use different prefixes or task types?

Queries and documents look different: a query is a short question, a document is a long chunk that contains the answer. Embedding them with different task hints ("search query" vs "document") puts them in a better position to match, which improves retrieval. For tasks where both sides are the same kind of text, like comparing two sentences, you use the same symmetric task for both.

## 348: How do you measure retrieval quality?

Build a set of real questions with the chunks that should be retrieved. Measure recall@k (is a correct chunk in the top k?) and MRR (how high is it ranked?). Then measure the final answer quality separately, since good retrieval with a bad prompt still gives bad answers. Re-run these after changing chunking, embedding model, dimension or filters.

## 349: How do you design a reliable agent loop with function calling?

Keep a clear loop: call the model, run the requested functions, send results, repeat until the model returns a final answer. Add a max number of turns, a total token or cost budget and a timeout. Validate arguments, catch function errors and return them as results. Log every step with its interaction ID. Keep tools small and well described, and send `tools` and settings again on each turn.

## 350: When should an agent loop stop?

When the model returns a final answer with no function calls, when it hits your max turns or budget, when the same call repeats with the same arguments (a sign it's stuck), when a function needs human approval, or when an error isn't recoverable. In each case, return something useful to the user, like a partial result or a clear message, instead of failing silently.

## 351: How do you stop an agent's context from growing forever?

Managed Agents compact the context automatically at around 135K tokens. In your own loop you need to do it yourself: summarize older turns into a short note, drop large tool results once they've been used (keep a short summary or a reference ID), and keep only the latest version of data that was fetched several times. Run compaction at a set token threshold, and keep the system prompt and current task untouched.

## 352: How would you implement conversation summarization for long chats?

When history goes over a threshold, take the oldest turns and ask a cheap model to summarize them, keeping facts, decisions, user preferences and open questions. Replace those turns with the summary in stateless mode, or start a new chain whose first input is the summary. Keep the most recent turns word for word. Test that important details survive the summary, since lost details are the most common complaint.

## 353: How do you handle parallel function calls correctly?

Run independent calls at the same time (for example with `asyncio.gather`), but send back a `function_result` for every call, each with the right `call_id`, all in the next request. If one fails, return an error result for that call instead of dropping it. Don't assume an order between calls, and watch for calls that write to the same resource, which may need to run one after another.

## 354: How do you deal with tool results that are too large?

Don't dump huge API responses into the context. Return only the fields the model needs, paginate ("first 20 of 340 results, call again with page=2"), summarize big text, or store the data somewhere and return a short summary with an ID the model can use in another call. Large results make every following turn more expensive and can push out important context.

## 355: How do you stream function call arguments to update a UI early?

Listen for `arguments_delta` events and append them to a buffer per step. You can run a partial JSON parser to show progress (for example the email draft the model is writing), but only act on the arguments after `step.stop`, when the JSON is complete. Never run a function based on partial arguments.

## 356: How do you handle backpressure when streaming from Node.js?

If the client reads slowly, writing faster than it reads fills memory. Use a `ReadableStream` with `pull` or check the return value of `res.write()` and wait for the `drain` event before writing more. Also stop reading from Gemini when the client disconnects (listen for `close` and abort the request), so you don't pay for tokens nobody will see.

## 357: How do you cancel an in-flight request in the JavaScript SDK?

Pass an `AbortSignal` in the request config and call `abort()` when the user cancels or disconnects:

```javascript
const controller = new AbortController();
req.on("close", () => controller.abort());

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash",
  contents: prompt,
  config: { abortSignal: controller.signal },
});
```

Cancelling on your side stops the waiting, but the server may still have done some work, so you can still be billed for tokens already generated.

## 358: How do you set timeouts for requests with heavy thinking?

High thinking levels and big inputs can take a long time, so a default 30 or 60 second timeout may cut off good requests. Set timeouts per use case: short for autocomplete, long for analysis, 10+ minutes for Flex. For anything that might run longer than an HTTP request should, use background mode with webhooks instead of a long synchronous call.

## 359: When should you use background mode instead of a synchronous call?

Use it when the work can take longer than your HTTP timeout or your users will wait: agents, Deep Research, long reports, heavy reasoning. It also protects you from losing results when a connection drops, since the result is stored and you can fetch it later. For quick interactive replies, synchronous streaming is still better.

## 360: How would you design the architecture of a voice support agent?

The browser or phone connects to the Live API with an ephemeral token minted by your backend, streaming 16 kHz PCM audio and playing 24 kHz audio back. The system instruction, voice and tools are locked into the token. Tools call your backend, which checks the user's identity and permissions. Turn on transcription and store transcripts for QA. Use session resumption and context compression for long calls, and have a way to hand off to a human.

## 361: What adds latency in a voice agent, and how do you reduce it?

Latency comes from audio buffering, network round trips, VAD waiting for silence, model time to first audio, tool calls and playback buffering. Reduce it by sending small audio chunks, tuning `silence_duration_ms`, connecting client-to-server, using a fast live model, keeping tools fast (or letting the model speak while a tool runs), and playing audio as soon as the first chunk arrives.

## 362: What are the common bugs with Live API interruptions?

The client keeps playing buffered audio after `interrupted`, so the model seems to ignore the user. Or the client drops the user's next words while clearing the buffer. Or echo from the speaker gets picked up by the mic and the model interrupts itself. Fixes: clear the playback queue immediately on `interrupted`, keep the mic stream going, and use echo cancellation on the client.

## 363: How do you keep a Live session going for an hour-long call?

Combine three things: session resumption (save the latest handle and reconnect with it when the connection ends or you get `go_away`), context window compression (a sliding window so the context doesn't fill up), and a reconnect loop on the client. With ephemeral tokens, the same token can be reused for resumption within its expiry window. Test reconnects under poor network conditions.

## 364: How do function calls work in a Live session without freezing the conversation?

Normally the model waits for your tool response before continuing. For slow tools, the Live API supports non-blocking function calls, where the model can keep talking while the function runs and use the result when it arrives. Either way, keep tools fast, and for slow ones have the model say something like "let me check that" so there isn't dead air.

## 365: What do you need to watch for with audio formats in the Live API?

Input must be 16-bit PCM, little-endian, at 16 kHz, and output is 24 kHz. Browsers usually record at 44.1 or 48 kHz as float32, so you must resample and convert to int16 before sending, and play output at 24 kHz. Getting the sample rate wrong gives chipmunk or slowed-down audio, or the model just doesn't understand speech.

## 366: When would you use gemini-3.8-live-extended-thinking instead of gemini-3.8-live?

The extended thinking version does more reasoning in the background, so it handles harder questions better, but it can be slower to respond. Use the standard model for normal fast conversation like support or ordering, and the extended version when users ask complex questions where a better answer is worth a short pause.

## 367: Why can't a text-only model continue some conversations?

When you switch models, the new model gets the earlier turns as input, including any outputs from the old model. If an image model generated images earlier, the new model has to accept images as input. Plan multi-model flows with this in mind, for example by keeping image generation in a separate chain and passing only text results back to the main conversation.

## 368: How do you safely migrate to a new model version?

Run your eval set on the new model and compare quality, cost and latency. Check things that often break: JSON shape, tool call behavior, refusals, length of answers, and parameters that are now ignored (like `temperature` on 3.6+). Fix prompts as needed, then roll out gradually behind a feature flag or to a percentage of traffic, while watching error rates and user feedback. Keep the old model ID ready for rollback as long as it exists.

## 369: What is the risk of model IDs that get routed to newer models?

Google sometimes routes an old ID to a new model, for example `gemini-3.7-flash` started routing to 3.8 Flash and `gemini-3.5-flash` to 3.6 Flash in October 2026. Your code doesn't change, but the model behind it does, which can change output style, thinking defaults, supported parameters and cost. Subscribe to the changelog and run evals when a routing change is announced, not after users complain.

## 370: With temperature deprecated, how do you get more consistent outputs?

Make the task less open: precise instructions, examples, structured output with enums, and narrow schemas. Use a lower thinking level for simple tasks so there's less room to wander. Cache answers for identical inputs if you need the exact same answer each time. Accept that LLM outputs aren't fully deterministic and design tests around properties ("valid JSON with the right label") instead of exact strings.

## 371: How do you test features built on a non-deterministic model?

Test properties, not exact text: the JSON is valid, required fields are present, the label is one of the allowed values, the answer contains key facts. Run important cases several times and measure pass rates instead of single pass/fail. Use a fixed eval set with thresholds in CI, and keep mocked unit tests for the code around the model.

## 372: How do you build a regression test set for prompts?

Collect real inputs from logs (cleaned of PII), especially failures and tricky cases, and write down the expected result or a grading rule for each. Add new cases whenever you fix a bug. Run the set on every prompt or model change and compare against the last run. Store results per version so you can see trends over time.

## 373: How do you use Gemini as an LLM judge?

Give a judge model the input, the answer and a clear rubric, and ask for a score with a short reason, using structured output. Use a strong model as the judge and test it against human labels to see how often it agrees. Watch for bias: judges tend to prefer longer answers and answers that look like their own. Use it for open-ended outputs, and use plain code checks wherever possible.

## 374: What should you log for observability of Gemini calls?

For each call: interaction or request ID, model, service tier, thinking level, prompt version, feature name, user or tenant ID, input/output/thought/cached token counts, latency (time to first token and total), status or finish reason, tool calls made, retries and errors. This lets you answer questions like "why did cost double yesterday" or "which feature has the most failures".

## 375: How would you trace a multi-step agent run?

Use distributed tracing (for example OpenTelemetry) with one trace per user request and a span per model call and per tool call. Attach the interaction ID, token usage and step types to each span. Then you can see where time and money go in a long run, which tool is slow, and how many model turns a task took.

## 376: What are the privacy implications of AI Studio logs being on by default?

Since October 2026, new paid projects store `generateContent` requests by default, and interactions are stored when `store` is true. That means prompts and responses, possibly with user data, sit in AI Studio for the retention period. Decide on purpose: turn logging off or shorten retention for sensitive projects, limit who in your team can see logs, and include this in your data processing documents.

## 377: How do you attribute Gemini costs to features or customers?

The bill is per project, not per feature. Log token usage with feature and tenant IDs on every call, multiply by the model's prices (adjusting for tier and caching) and add it up in your own analytics. Separate projects per environment or big product area also helps. This is how you find out which customers or features are unprofitable.

## 378: How do you put budget guardrails into an app?

Use spend caps and billing alerts at the Google level. In your app, set per-user and per-tenant quotas (requests or tokens per day), cap `max_output_tokens`, cap agent turns and total tokens per task, and limit input size. Track spend in near real time and switch to cheaper models or block non-essential features when you're close to the budget.

## 379: When does it make sense to cache final answers yourself?

When many users ask the same or very similar questions, like FAQs, product descriptions or translations of the same text. An exact-match cache keyed by a hash of the normalized input is simple and safe. A semantic cache (matching similar questions with embeddings) saves more but can return a wrong answer for a question that looks similar but is different, so use a strict similarity threshold and don't use it for user-specific data.

## 380: How do you decide if explicit caching saves money?

Compare the cost with and without caching over the cache's lifetime. Without: N requests × context tokens × input price. With: storage price × tokens × hours + N × context tokens × cached price. Explicit caching wins when the same large context is used many times within the TTL. With few requests per hour, implicit caching (free when it hits) or no caching may be cheaper.

## 381: Explicit caching isn't available for Gemini 4 Argon or the Interactions API. What do you do?

Rely on implicit caching: keep a stable prefix (system instruction, tools, documents) at the start of every request, send related requests close together, and use `previous_interaction_id` so the server can reuse the earlier context. If you really need explicit caching, use a model that supports it through `generateContent`. Check `total_cached_tokens` to make sure caching is actually happening.

## 382: Can you combine the Batch API with caching?

Yes. Batch requests can use context caching, and cache hits are billed at the normal caching rates on top of the batch discount. This is a good combination for jobs where every request shares a large prefix, like grading thousands of answers against the same long rubric.

## 383: How do you handle a batch job that expires?

Jobs that stay pending or running for over 48 hours expire with no results. Resubmit the work, ideally split into smaller jobs, and check if you're near the batch token limits for your tier. Track jobs in your own database so you can see which keys finished and which need another try, and alert when a job hasn't finished well before the 48-hour mark.

## 384: How do you keep the cost of video analysis under control?

Video uses many tokens per second, so lower `media_resolution` (use `low` unless you need to read small text), clip the video to the parts you need, and use a cheaper model for a first pass. On newer Flash models, agentic video understanding can look only at the relevant parts and use far fewer tokens on long videos. Count tokens on a sample to estimate cost before processing a whole library.

## 385: What is agentic video understanding?

It's a mode on newer Flash models (3.6 Flash, 3.7 Flash, 3.5 Flash-Lite) where the model doesn't process every frame equally. It decides which parts of the video to look at closely based on the question, much like a person skipping through a video. Google says it uses up to 88% fewer tokens on long content, with typical use around 1,500-3,000 tokens for a 60-second video.

## 386: How does Gemini handle PDFs with both text and images?

Each page is processed as an image, and on newer models the native text of the page is added as well, so the model gets both the layout and the exact text. That's why it can read charts, tables and scanned pages. Media resolution changes the image part: `medium` is usually enough, and higher settings help with tiny text or dense tables.

## 387: How do you improve OCR accuracy on small or dense text?

Raise the media resolution for that item (`high` or `ultra_high` for an image), crop the image to the relevant region, and send it at a decent size. Ask for exact transcription and structured output, and tell the model to mark unreadable parts instead of guessing. For critical numbers, cross-check against other data or ask for the source location.

## 388: How would you run image generation at scale in a product?

Pick the model by need: Nano Banana 2 Lite for cheap and fast, Nano Banana 2.1 or Pro for higher quality and text rendering. Use Batch for bulk generation. Check prompts and outputs with your own moderation before showing them, store images in your own storage (generated files are only kept for a short time), and keep the SynthID watermark in mind for disclosure rules. Track cost per image, since resolution changes the price.

## 389: How do you keep a character or product consistent across many generated images?

Use reference images for the character or product, and keep editing in a multi-turn conversation instead of starting over each time. Describe the fixed features in every prompt (colors, clothing, logo placement). Nano Banana Pro supports more character and style references if you need tight control. Check results and regenerate the ones that drift.

## 390: How do you meet data residency requirements with Gemini?

The Gemini API in AI Studio doesn't give you the regional controls an enterprise usually needs. Vertex AI lets you choose regional endpoints and has data residency commitments, plus Google Cloud's compliance certifications. If your rules require data to stay in a certain region, use Vertex AI and check that the specific models and features you need are available in that region.

## 391: What enterprise security features push teams to Vertex AI?

IAM with service accounts and fine-grained roles, VPC Service Controls to stop data leaving a security perimeter, customer-managed encryption keys, private networking, audit logging through Cloud Audit Logs, and enterprise support and SLAs. If your security team asks for these, the Gemini API with API keys usually won't pass review.

## 392: How do you write code that runs on both the Gemini API and Vertex AI?

Use the Google GenAI SDK and create the client from configuration: an API key for the Gemini API, or `vertexai=True` with project and location for Vertex. Keep the rest of the code the same. Hide features that only exist on one side behind checks, and run your tests against both if you deploy to both. Environment variables (`GOOGLE_GENAI_USE_VERTEXAI`) make this easy.

## 393: Why should you pin SDK versions?

The SDKs and API change quickly. For example, the Interactions API renamed `outputs` to `steps` in May 2026 and removed the old schema in June, and earlier renamed `total_reasoning_tokens` to `total_thought_tokens`. If you don't pin, a new install can pull a version with different types or defaults. Pin versions, read release notes when upgrading and run your tests before deploying.

## 394: How do you handle breaking changes announced in the changelog?

Watch the changelog (or subscribe to notifications), and add each announced change with its date to your backlog. Update code during the transition window, when both old and new formats work, so you're not fixing things on the cutoff day. Write code that reads response fields defensively and fails loudly if something important is missing.

## 395: When would you call the REST API directly instead of using an SDK?

When there's no SDK for your language, when you need a feature the SDK hasn't added yet, when you want a minimal dependency footprint (for example in an edge function), or when you're debugging and want to see the exact HTTP traffic. The SDK is usually better for everyday work because it handles types, streaming, retries and auth for you.

## 396: How would you design a provider-agnostic LLM layer that includes Gemini?

Define your own small interface around what your app needs (generate text, generate JSON, call tools, stream) with your own types, and write one adapter per provider. Keep provider-specific features (grounding, thought signatures, file search) available through the adapter when needed, instead of hiding them completely. Don't make the abstraction too generic, or you'll lose features that make each provider worth using.

## 397: What are the pros and cons of using the OpenAI-compatible endpoint in production?

Pros: fast migration from OpenAI code, one client library for several providers, familiar API. Cons: it's still beta, some Gemini features are missing or reachable only through `extra_body`, parameters may be silently ignored, and new Gemini features show up in the native API first. It's fine to start with, but for features beyond basic chat, plan to move to the native SDK.

## 398: When should you use function calling vs structured output?

Use structured output when you want the final answer in a fixed shape, like extracted fields or a classification. Use function calling when the model needs to do something or fetch data during the task, and may decide whether and when to call it. You can use both: tools to gather information, and a schema for the final answer.

## 399: How would you build extraction with citations to sources?

Use Google Search or File Search as a tool with a JSON schema for the output, and include a `sources` field per item in the schema. Also read the annotations in the response (`url_citation` or `file_citation`) and map them to the items. Then check in code that every cited source was actually retrieved in this request, and drop or flag items without valid sources.

## 400: What techniques reduce hallucinations with the Gemini API?

Ground the model in data: Google Search, URL Context, File Search or documents in the prompt. Tell it to say "I don't know" when the answer isn't in the sources, and to cite them. Use structured output with nullable fields so it can leave unknown values empty. Use enough thinking for hard questions, verify important facts in code, and test hallucination rates with an eval set.

## 401: How do you check that citations actually support the text?

Annotations tell you which part of the text a source is linked to, but not that the source really says it. For important answers, fetch the cited passage and run a second check (code for numbers and names, or a cheap model call that answers "does this passage support this sentence?"). Show citations in the UI so users can check too, and track how often checks fail.

## 402: How do you keep Google Search grounding costs under control at scale?

On Gemini 3+, you pay per search query, and the model can run several queries per request. Only enable `google_search` for requests that need fresh info, for example with a router that decides first. Cache grounded answers for popular questions for a short time. Watch the queries per request in the `google_search_call` steps, and keep the 1,500 requests per day default limit in mind.

## 403: How do Maps grounding and Search grounding differ in use?

Search grounding is for general web facts and news. Maps grounding is for places: businesses, addresses, opening hours, ratings, directions and nearby things. A travel or delivery app would use Maps for "good cafés near the hotel" and Search for "is the museum closed for renovation this month". They can be combined in one request when a question needs both.

## 404: Is Code Execution safe to use with untrusted input?

The code runs in Google's sandbox, not on your servers, so it can't touch your systems. But the output can still be wrong or manipulated by the input, so treat results as untrusted data. It's limited to Python with fixed libraries and 30 seconds per run. If you need your own data, network access or other languages, run code in your own isolated sandbox and expose it as a function.

## 405: When would you use your own sandbox instead of the built-in Code Execution tool?

When the code needs access to your private data or internal APIs, needs packages that aren't installed, takes longer than 30 seconds, needs a language other than Python, or must run in your own infrastructure for compliance. In that case you declare a `run_code` function, run it in a locked-down container with no secrets and limited network, and return the output.

## 406: When should you use Managed Agents vs your own agent loop?

Managed Agents fit when you want a general agent that writes and runs code, creates files and uses tools in a sandbox, without building and running that infrastructure yourself. Build your own loop when the agent mainly works with your systems through your own functions, when you need full control over each step, prompts and permissions, or when data must stay in your environment.

## 407: Why does forking the base environment matter for saved agents?

Each run of a saved agent starts from a copy of the base environment, not from whatever the last run left behind. That makes runs reproducible and keeps one run's files or broken state from affecting the next. It also keeps users' data from leaking between runs, which matters if the same agent serves different users.

## 408: How would you integrate Deep Research into a product?

Start the research with `background=True` and a dynamic webhook pointing at your service, and store the interaction ID with the user's request. Show "research in progress" in the UI. When `interaction.completed` arrives, fetch the result, store the report and its citations, and notify the user. Handle `interaction.failed` and timeouts, and limit how many research jobs a user can start, since they're expensive.

## 409: How can you mix agents and models in one conversation?

Chain them with `previous_interaction_id`. For example, run the Deep Research agent to collect information, then pass its interaction ID to a call with `gemini-3.8-flash` that turns the report into a short summary or a JSON object for your app. Each step uses the best tool for its job, and the history flows between them.

## 410: Can Gemini use remote MCP servers directly?

The Interactions API notes that Gemini 3 doesn't support remote MCP yet, though some agents like Deep Research can connect to MCP servers. The common pattern today is to run an MCP client in your own code: list the server's tools, turn them into Gemini function declarations, and when the model calls one, forward the call to the MCP server and return the result. Check the docs for current MCP support before designing around it.

## 411: How would you map MCP tools to Gemini function declarations?

MCP tools have a name, a description and a JSON Schema for input, which maps almost directly to a Gemini function declaration (`type: "function"`, `name`, `description`, `parameters`). Watch for schema features Gemini doesn't support or ignores, name collisions between servers (prefix names with the server name), and permissions: just because a server exposes a tool doesn't mean the model should be allowed to use it for every user.

## 412: How would you run Computer Use safely in production?

Run each session in a fresh, isolated browser container with no saved logins unless the task needs them, and with an allowlist of sites. Send screenshots at a resolution that gives good results. Require confirmation for actions flagged by `safety_decision` and for anything involving payments, messages or account changes. Log each step's screenshot, action and `intent`, set limits on steps and time, and give users a way to take over.

## 413: How do the browser, mobile and desktop environments differ in Computer Use?

The `environment` setting tells the model what kind of screen and actions to expect. In a browser it can click, type, scroll and navigate URLs. On mobile it works with touch gestures on a phone screen, and on desktop with a full operating system screen. Your client has to run the actions in that kind of environment (for example Playwright for browsers or a device automation tool for mobile).

## 414: Scenario: design a chatbot that answers questions about your company's internal docs.

Load the docs into File Search (or your own vector DB), one store per access group, with metadata like department and date. On each question, check the user's permissions, pass only the allowed stores or filters, and use a system instruction that says to answer only from the documents, cite sources and say when the answer isn't there. Use Flash with streaming, keep history short, log questions with no good answer to find gaps in the docs, and evaluate with a set of real questions.

## 415: Scenario: you need to classify 5 million support tickets by tomorrow.

Write a short, stable prompt with an enum schema and test it on a few hundred labeled tickets with Flash-Lite. Then split the tickets into JSONL files with ticket IDs as keys and submit Batch API jobs within your tier's enqueued token limits. Track jobs with webhooks, parse results line by line, and resubmit failures. Batch gives 50% off, and most jobs finish well before 24 hours, but start early and use Flex as a backup if a job lags.

## 416: Scenario: build invoice extraction for an accounting app.

Upload invoices (PDF or image) and use structured output with a Pydantic or Zod schema for vendor, dates, line items, tax and totals, with nullable fields for missing values. Validate in code: totals add up, dates are valid, VAT numbers match a pattern. Send low-confidence or failing invoices to human review and log corrections as test cases. Use `medium` resolution for PDFs and raise it only for bad scans.

## 417: Scenario: build a voice agent for restaurant reservations.

Use the Live API with ephemeral tokens for the client, a system instruction with the restaurant's rules, and functions like `check_availability` and `create_booking`. Make the agent repeat the details and get confirmation before booking. Tune VAD for phone audio, handle interruptions, store transcripts, and add a `transfer_to_staff` function. Test with background noise and different accents before going live.

## 418: Scenario: your Gemini bill doubled overnight. How do you investigate?

Look at usage by model and project in AI Studio and billing, then your own logs by feature and user to find where the extra tokens came from. Common causes: a prompt change that made inputs much bigger, a loop or retry storm, an agent running too many turns, a model ID that started routing to a pricier model, thinking defaults changing, cache hits dropping because the prompt prefix changed, or a leaked key. Fix the cause, then add alerts and per-feature budgets.

## 419: Scenario: users get 429 errors at peak times. What do you do?

Check which limit you're hitting (RPM, TPM, RPD or spend) in AI Studio. Short term: retry with backoff and jitter, queue requests, and give interactive traffic priority. Medium term: move background work to Batch or Flex, cut tokens per request, use caching, and route easy requests to a model with more headroom. Long term: move up a tier, request a quota increase or consider Priority or Vertex AI provisioned throughput.

## 420: Scenario: some responses come back empty or cut off. How do you debug?

Check the status or `finish_reason` first. `incomplete`/`MAX_TOKENS` means the output limit was hit, often because thinking used up the budget, so raise `max_output_tokens` or lower the thinking level. A safety block shows up as a 400 error in the Interactions API or `SAFETY` in `generateContent`. If the response only has a function call, there's no text to read. Also make sure your code reads all steps, not just `output_text`, when outputs are mixed.

## 421: Scenario: the model sometimes returns JSON that your code can't parse.

First make sure you're using a real schema (`response_format` or `response_schema`), not just "return JSON" in the prompt. Then check for truncation (incomplete status), since cut-off JSON is the most common cause. Make sure you parse only the output text, not thought summaries. If the schema is very complex, simplify it. Finally, validate with Pydantic or Zod and retry once with the error message if validation fails.

## 422: Scenario: the model keeps calling a function with wrong arguments.

Improve the declaration: clearer descriptions, examples of valid values, enums instead of free text, and required fields marked. Check that tool names don't overlap in meaning. Return clear validation errors so the model can fix the call. If the right value comes from somewhere the model can't see, add a tool to look it up. As a last step, use `validated` mode or `allowed_tools` to force correct use.

## 423: Scenario: after switching to a newer model, requests start failing with 400 errors.

Read the error message, then check what changed: parameters the new model doesn't support (some thinking settings differ between models), your history code dropping thought signatures, schema features the model rejects, media types the model can't take, or an old API format (like the Interactions API change from `outputs` to `steps`). Compare a failing request with a working example from the docs for that exact model.

## 424: Scenario: your logs show deprecation warnings for temperature after upgrading to Gemini 3.8 Flash.

Gemini 3.6+ and Gemini 4 ignore `temperature`, `top_p` and `top_k`, and send deprecation warning headers. Remove those parameters from requests to these models. If you relied on low temperature for consistency, get it from tighter prompts, structured output and enums instead, and re-run your evals to make sure output quality didn't change.

## 425: Scenario: users say the bot "forgot" a file they uploaded two days ago.

Files API uploads are deleted after 48 hours, so a later turn that points to the old file URI fails or the model doesn't see it. Keep the original file in your own storage and upload it again when needed, or put long-lived documents in a File Search store, which keeps data until you delete it. Track file expiry in your database so you re-upload before you need it.

## 426: Scenario: streamed responses sometimes stop in the middle.

Check for an `error` event in the stream and whether you got `interaction.completed`. Common causes: a proxy or load balancer closing idle or long connections, a timeout in your server or client, the client disconnecting, or a safety block mid-stream. Raise proxy timeouts, turn off response buffering, send keep-alives if needed, and handle stream errors by showing what you have and offering a retry. For very long jobs, use background mode.

## 427: Scenario: Live API voice sessions drop after about 10-15 minutes.

That's the session and connection limits. Turn on session resumption, store the latest handle, and reconnect automatically when the server sends `go_away` or the socket closes. Add context window compression so the context doesn't fill up. If you use ephemeral tokens, make sure their `expire_time` covers the whole call, or mint a new token for the reconnect.

## 428: Scenario: you found your API key in a public GitHub repo.

Treat it as compromised right away. Create a new key, deploy it, and disable the old one. Check usage and billing for strange traffic, and set spend caps if you didn't have them. Remove the key from the code, and know that it may already be copied even if you rewrite git history. Add secret scanning to your repo and CI so it doesn't happen again, and move keys to a secret manager.

## 429: Scenario: one big customer uses most of your quota in a multi-tenant SaaS.

Since quota is per project, one tenant can starve the others. Add per-tenant rate limits and token budgets in your app, with a fair queue that serves tenants in turn. Move that customer's bulk work to Batch. For very large customers, consider a separate project (billed to them, if your contract allows) or provisioned capacity on Vertex AI. Show tenants their usage so limits don't come as a surprise.

## 430: Scenario: you still use gemini-2.5-flash in production in November 2026.

`gemini-2.5-flash` is deprecated, and from December 1, 2026 its requests are routed to `gemini-3.5-flash-lite` (and `gemini-2.5-pro` to `gemini-3.8-flash`). Don't wait for that: pick the replacement on purpose, run your evals, and update your code. Check the differences: thinking uses `thinking_level` instead of `thinking_budget`, sampling parameters may be ignored on newer models, and pricing and token counts for media change.

## 431: Scenario: autocomplete suggestions are too slow.

Use the fastest model (Flash-Lite) with `minimal` thinking, a short prompt and a small `max_output_tokens`. Keep the prompt prefix stable so it's cached, stream the result, and cancel the in-flight request when the user types again. Debounce input so you don't send a request per keystroke. If it's still too slow, consider Priority tier, or doing simple completions without an LLM.

## 432: Scenario: decide between Gemini 4 Argon and Gemini 3.8 Flash for a coding assistant.

Build an eval from real tasks (bug fixes, refactors, writing tests) with automatic checks like running the tests. Run both models at a few thinking levels and compare pass rate, latency and cost per task. Often Flash handles most tasks and Argon wins on the hardest ones, so routing by task difficulty can give you most of the quality for much less money. Re-run the comparison when new models come out.

## 433: Scenario: a chat conversation has grown so long that each turn is slow and expensive.

Every turn re-reads the whole history. Summarize older turns and start a new chain from the summary plus the last few messages, or in stateless mode trim the history yourself. Remove big tool results and file contents that are no longer needed. Make sure the stable parts (system prompt, tools) stay at the start for caching. Tell users when a conversation gets very long and offer to start a new one.

## 434: Scenario: translate a 300-page document.

Split it into sections along headings, translate each with the same system instruction, glossary and style guide (stable prefix, so it gets cached), and keep formatting rules strict. Pass the previous section's last paragraph for context so terms stay consistent. Use Batch if it's not urgent. After translating, run checks for missing sections and untranslated text, and have a native speaker review a sample.

## 435: Scenario: summarize hour-long meeting recordings cheaply.

Send audio only, not video, unless slides matter. Audio costs a fixed amount per second, which is much less than video. Use a Flash or Flash-Lite model with a structured output schema for summary, decisions and action items. For a transcript as well, use the transcribe model with speaker diarization, then summarize the text. Use Batch for recordings that don't need instant results.

## 436: Scenario: build an automated code review bot for pull requests.

Trigger on PR events, send the diff plus relevant surrounding code and the repo's guidelines, and ask for structured output (file, line, severity, comment). Filter low-value comments and cap how many you post. Store the API key as a CI secret, never print prompts with secrets in logs, and skip files that may contain secrets. Track how often developers accept or dismiss comments, and use that to tune the prompt.

## 437: Scenario: design a moderation pipeline for user-generated posts.

Use cheap rules first (blocklists, length, links), then a Flash-Lite call with an enum schema for your own categories and a reason field. Turn on Gemini safety settings as an extra layer. Auto-approve clear safe cases, auto-reject clear violations, and send unclear cases to humans. Log decisions, measure precision and recall on a labeled set, and use human decisions to improve the prompt.

## 438: Scenario: run offline evaluation of a new prompt on 50,000 examples.

Write each example as a batch request keyed by example ID, with the new prompt, and submit through the Batch API for the 50% discount. Do the same for the old prompt if you don't have its outputs. When jobs finish, score outputs with code checks and, where needed, a judge model (also in batch). Compare metrics and look at the examples where the two prompts disagree the most.

## 439: Scenario: a user asks you to delete all their data. What do you remove on the Gemini side?

Delete their stored interactions by ID, uploaded files that haven't expired yet, any explicit caches with their data, and their documents in File Search stores (or the whole store if it's theirs). Check AI Studio logs and datasets for their data and how your retention setting applies. To make this possible, record the IDs of Gemini resources per user when you create them.

## 440: Scenario: the business requires that answers come only from approved documents.

Use File Search or your own retrieval over the approved docs only, and don't enable Google Search or URL Context. Tell the model to answer only from the provided sources, to cite them, and to say it doesn't know otherwise. Then enforce it in code: reject answers without citations, check that cited documents are in the approved set, and test with questions whose answers aren't in the docs to make sure the bot declines.

## 441: Scenario: an agent keeps calling the same tool over and over.

Detect it: track recent calls and stop when the same function and arguments repeat a few times. Then look at why. Often the tool result doesn't say clearly that it succeeded or that there's no data, the result is too big and gets misread, or the instructions don't say when to stop. Make results explicit ("No orders found for this customer"), add stop rules to the system instruction, and set a maximum turn count.

## 442: Scenario: one tool returns 200K tokens of data and the model gets slow and confused.

Reduce what the tool returns: select only needed fields, filter on the server, paginate, or summarize. Let the model ask for more detail with another call if it needs it. If the full data really must be analyzed, use Code Execution or your own code to compute the answer and give the model only the result. Big tool outputs hurt cost, latency and accuracy all at once.

## 443: Scenario: your team wants to switch from OpenAI to Gemini. How do you plan it?

Start with the OpenAI-compatible endpoint to run your current code against Gemini quickly, and build an eval set to compare quality, latency and cost. Then move to the native SDK for the features you want (Interactions API, grounding, file search, caching). Map the differences: tool call formats, structured output schemas, reasoning settings, token counting, safety behavior and rate limits. Roll out per feature behind a flag and keep the old provider as a fallback during the switch.

## 444: Scenario: generated images often have spelling mistakes in the text.

Use a model that's better at text rendering (Nano Banana Pro or Nano Banana 2.1, which improved typography). Put the exact text in quotes in the prompt and keep it short. Generate at a higher resolution. If it's still wrong, edit in a follow-up turn ("fix the word X to Y"), or generate the image without text and add the text in your own app, which is the safest option for important wording.

## 445: Scenario: upgrade from gemini-embedding-001 to gemini-embedding-2 with no downtime.

Vectors from the two models aren't compatible, so you need a full re-embed. Create a new index, re-embed all documents with the new model (using Batch to save money), and write new documents to both indexes during the migration. When the new index is complete, run retrieval evals on it, then switch queries to the new model and index at the same time. Keep the old index for a while for rollback, then delete it.

## 446: Scenario: the Interactions API response format changed and production broke.

This happened in 2026 when `outputs` was renamed to `steps`. Fix it now by updating the SDK and the parsing code, and check for other changes in the same release. To prevent this: pin SDK versions, follow the changelog and fix things during the transition window, have integration tests that call the real API in a staging environment, and parse responses in one place so a format change only needs one fix.

## 447: Scenario: you need the same answer every time for the same input, for audit reasons.

LLM outputs aren't guaranteed to be identical between calls, and sampling controls like `temperature` are ignored on newer models. Save the response the first time and serve the saved one for the same input (keyed by a hash of input, prompt version and model). Log the model ID, prompt version and full response for each decision so you can show exactly what was produced, even if a new call would give a different answer.

## 448: Scenario: a feature works on the free tier in testing but fails in production on the paid tier.

Compare the two projects: different API keys (and key restrictions), different models available, different rate limits, spend caps, safety settings or SDK versions. Also check data and retention settings that differ by tier. A common cause is a key that's restricted to other APIs, or a production project that hasn't enabled billing correctly. Reproduce the failing request with curl against the production project to see the exact error.

## 449: Scenario: you need to process user-uploaded videos that may contain sensitive content.

Upload through your backend, never with a key in the client. Check files with your own moderation before sending them to Gemini, and expect that some requests will be blocked by safety filters. Delete uploaded files from the Files API once processing is done instead of waiting 48 hours, use `store=False` where possible, and make sure your terms tell users their content is processed by a third-party AI service.

## 450: What would you check before taking a Gemini API feature to production?

- Pinned model IDs and SDK versions, and a plan for deprecations.
- API key kept on the server, restricted, in a secret manager, with spend caps and billing alerts.
- Retries with backoff, timeouts, fallbacks and handling of every status and finish reason.
- Rate limiting and per-user quotas in your app.
- Structured output validation and safe handling of tool calls, with permission checks.
- Prompt injection defenses for any external content.
- Logging of usage, latency and errors, without leaking PII.
- Data retention settings (store, logs, files) that match your privacy policy, on a paid tier.
- An eval set with passing results on the exact model and prompt you ship.
- Cost per request measured and within budget.
